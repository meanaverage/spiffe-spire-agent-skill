# Security review invariants

Derived from independently adjudicated findings and false positives observed during real SPIFFE/SPIRE integration security review, then generalized to remove product-specific assumptions.

## Consistent application authorization state

### Invariant

When an authenticated SPIFFE identity is combined with application-owned authorization or lifecycle state, the relying party MUST evaluate a single internally consistent authority snapshot and MUST fail closed on impossible allow/deny combinations before deriving authority.

### Why it matters

Applications often encode authority in more than one representation: an allowed state plus revocation markers, status plus timestamps, or a lifecycle field plus a separate disable flag. If those representations disagree and the decision path trusts only the permissive field, authentication can flow into authority that the application's own state also says should be denied.

SPIFFE authentication does not reconcile application state. The relying party owns this consistency property.

### Review questions

- What fields, records, or services jointly determine whether this SPIFFE identity is allowed to act?
- Is there an explicit consistency table for all allow, deny, revocation, and terminal representations?
- Does the authorization snapshot reject impossible combinations before calculating roles, eligibility, or effects?
- Can every writer preserve the consistency table atomically, including recovery, migration, and administrative paths?
- Do tests inject contradictory state at the decision boundary and verify fail-closed behavior?

### Evidence required

Report an invariant violation when source, a focused test, or equivalent runtime evidence shows that the authorization decision can read an impossible combination and continue as allowed rather than rejecting it. The evidence should identify the contradictory representations, the decision path that consumes them, and the missing or ineffective consistency check.

Also trace writers, transaction boundaries, snapshot/digest behavior, and downstream authorization. Those facts determine reachability and impact; they are not prerequisites for accurately reporting the narrower fail-closed invariant violation.

### Do not overclaim

- **Invariant violation:** Contradictory authoritative state can pass the authorization snapshot or decision boundary.
- **Exploitable vulnerability:** In addition, an actor can plausibly create, preserve, or exploit that contradictory state under the deployed trust and write model.
- **Demonstrated bypass:** A reproducible trace or test shows the contradictory state producing an effect that should have been denied.
- **Theoretical risk:** The design has multiple authority representations, but no evidence yet shows an inconsistent combination reaching an allow decision.

An invariant violation is not automatically an exploitable vulnerability or a demonstrated bypass.

### SPIFFE/SPIRE boundary

This is a **SPIFFE integration and application-authorization** invariant. SPIFFE/SPIRE authenticates and issues identity; it does not define or reconcile the relying party's lifecycle, revocation, eligibility, or effect policy.

## SVID authentication does not attest request attributes

### Invariant

A relying party MUST treat a valid SVID as evidence for the authenticated SPIFFE identity, not as attestation of caller-supplied request attributes; every caller-controlled attribute that affects eligibility, authorization, or effects MUST be independently authorized at the decision boundary.

### Why it matters

Capabilities, readiness, placement, tenancy, metadata, roles, and similar fields can travel in the same request as strong identity evidence. That transport proximity does not make those fields trustworthy. A system may correctly prevent direct mutation of protected state yet still allow a self-reported value to influence candidate selection, queueing, routing, or another indirect path to effects.

### Review questions

- Which request fields come from relying-party verification, and which are supplied by the authenticated caller?
- Can a caller-controlled field change eligibility, priority, routing, role selection, resource choice, or effect scope?
- What controller-owned policy or trusted evidence authorizes each consequential attribute?
- Are indirect consumers such as selectors, queues, schedulers, and dispatchers included in the data-flow review?
- Does the final effect boundary reauthorize the chosen subject, resource, and action?

### Evidence required

Report an invariant violation when data-flow evidence or a focused test shows that a caller-controlled attribute, authenticated only by its association with a valid SVID-bearing request, changes eligibility or authority without an independent trusted policy decision.

To report a bypass, additionally establish that the caller can set the attribute and that the changed eligibility or authority reaches a protected effect despite downstream controls.

### Do not overclaim

- **Invariant violation:** A caller-controlled attribute affects an authorization-relevant decision without independent authorization.
- **Exploitable vulnerability:** The caller can control that attribute and plausibly obtain authority or access outside the intended policy.
- **Demonstrated bypass:** A reproducible trace or test shows the forged attribute causing a protected effect that the caller otherwise could not obtain.
- **Theoretical risk:** Self-reported fields exist near authorization code, but no consequential consumer or missing policy check has been shown.

Indirect eligibility influence can establish an invariant violation without proving arbitrary effect authority. Do not describe successful SVID authentication alone as attestation of the rest of the request.

### SPIFFE/SPIRE boundary

This is a **relying-party authentication and SPIFFE integration** invariant. SPIFFE/SPIRE attests the SPIFFE identity represented by the SVID under the configured trust model. Application attributes and the policy governing their consequences remain the relying party's responsibility.
