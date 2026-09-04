# Reviewer discrimination rules

These rules improve both recall and precision. They do not tell reviewers to ignore suspicious patterns; they identify the evidence needed to distinguish a demonstrated defect from an apparent one.

## Authorization checked before a later mutation

A preliminary authorization check before mutation can look like TOCTOU. Before reporting, determine the last authority-bearing read, transaction/connection ownership, datastore isolation, competing writers, and whether nested helpers preserve that boundary.

**Finding threshold:** a realizable call path or interleaving allows authority to change after the last effective validation while the protected mutation still succeeds using stale allowed state.

**Benign condition:** current authority is re-resolved and mutation occurs in one correctly serialized boundary, with competing writers following compatible serialization.

**BAD:** Any transaction or later validation makes authorization TOCTOU impossible.

**GOOD:** Trace the final authority read, transaction ownership, nested calls, and competing writers; report TOCTOU only when stale authorized state can actually reach the effect.

Calibrate language from suspected → invariant violation → exploitability unproven/established → demonstrated bypass.

## Constant or apparently static request commitment

A constant-looking digest can suggest that altered request semantics are not bound to authorization evidence.

Before reporting, determine the complete accepted request language, canonicalization, committed bytes/semantics, receipt construction, consumer comparison, and effect-boundary consumption.

**Finding threshold:** two security-distinct accepted requests share the same authorized commitment, or valid evidence can be applied to uncommitted request semantics that reach an effect.

**Benign condition:** exactly one canonical security meaning is accepted, alterations are rejected before effects, and the commitment unambiguously identifies that meaning.

**BAD:** A constant digest is safe whenever an endpoint appears fixed.

**GOOD:** Compare the full accepted request semantics with the commitment and ask whether security-distinct accepted requests can share authorization.

## Replay concern at a pure identity transformation

A function may accept verified identity evidence repeatedly without containing a nonce or replay cache.

Before reporting, determine whether it mutates state or grants effects, what authority its result carries, all consumers, intended reuse semantics, and where freshness/idempotency/one-time consumption is enforced.

**Finding threshold:** repeated evidence reaches an authority-bearing consumer and obtains an effect intended to be unique, or the first effect boundary lacks a replay property required by its contract.

**Benign condition:** repetition occurs only at a pure authentication transformation and no effectful consumer exists, or the consumer independently enforces the required replay property.

**BAD:** Pure identity helpers never need replay analysis.

**GOOD:** Follow evidence to the first stateful or effect-authorizing consumer and locate the actual owner of replay prevention before deciding whether a defect exists.

## Old detached identity-verification evidence

Detached verification evidence can remain acceptable after the time at which it was originally verified.

Before reporting, determine whether verification is live or detached, whether certificate validity is rechecked, the protected effect's freshness contract, who can capture/submit evidence, and whether expiry, nonce consumption, channel binding, revalidation, or equivalent controls limit reuse.

**Finding threshold:** an authority-bearing consumer accepts detached evidence older than its required security horizon without an equivalent freshness control and stale acceptance affects eligibility or a protected effect.

**Benign condition:** verification is live at the decision boundary, or explicit freshness/reuse controls satisfy the effect contract.

**BAD:** An unexpired SVID makes every cached or detached verification result sufficiently fresh.

**GOOD:** Separate SVID validity from the relying party's detached-evidence freshness requirement, then trace stale evidence to the first authority-bearing consumer.

## SPIFFE ID path used as an application role

Giving privileged meaning to SPIFFE ID path segments can create concern about alternate encodings, segment confusion, prefixes, or extra components.

Before reporting, supply concrete candidate identifiers and run them through both the deployed SPIFFE parser and application classifier. Determine canonicalization, exact segment structure, trust-domain checks, and resulting authority.

**Finding threshold:** a syntactically valid/parser-accepted identifier outside the intended role language is classified into a privileged role and reaches an authorization-relevant decision.

**Benign condition:** compliant syntax validation rejects malformed alternatives and the local classifier enforces the intended exact role language for the tested class.

**BAD:** Exact string comparisons eliminate all SPIFFE ID role-confusion risk.

**GOOD:** Test concrete adversarial identifiers across both syntax and local semantic classification; SPIFFE defines identifier syntax, while the relying party defines path meaning.

## Telemetry near authorization versions or digests

Volatile telemetry sharing storage/update helpers with authority state can suggest that routine updates mutate authorization versions or digests.

Before reporting, enumerate the authority digest preimage, version fields, mutation triggers, generic row-update behavior, downstream consumers, and telemetry-only behavior.

**Finding threshold:** non-authoritative telemetry changes an authorization token/version/digest contrary to contract and causes a security or availability consequence in a dependent authorization path.

**Benign condition:** volatile fields are excluded from authority representation, versions change only on authority-relevant transitions, and focused tests show telemetry-only updates leave dependent grants stable.

**BAD:** Telemetry and authorization fields can safely share storage, so update coupling never needs review.

**GOOD:** Trace exact digest inputs and every version mutation path, then compare the authority snapshot before and after telemetry-only updates.

## Claim-strength vocabulary

Choose the conclusion after recording observed and missing evidence:

| Conclusion | Evidence gate |
|---|---|
| **Suspected** | A property failure is plausible, but discriminating evidence is incomplete. |
| **Invariant violation** | Evidence establishes failure of the security property at its owning boundary. |
| **Exploitable** | The invariant violation, plausible actor reach/control, and a meaningful security consequence are established. |
| **Demonstrated bypass** | A concrete reachable path, required actor/control condition, protected effect, and evidence that the effect should have been denied are established. |

Apply two consistency checks. A label MUST NOT assert an evidence element that the review narrative calls missing or unproven. Conversely, missing reachability or exploitation evidence MUST NOT reduce an established invariant violation to suspected or non-finding. When dispositive facts refute the alleged property failure, report a non-finding and state what changed fact would reopen it.

Skill guidance selects questions and evidence; it is not itself evidence. Cite the applicable specification, exact-version source/tests, integration path, or runtime observation instead.
