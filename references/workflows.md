# Workflows

## Architecture / review

1. Name the behavior.
2. Determine whether it belongs to SPIFFE semantics, SPIRE lifecycle, client implementation, deployment integration, or application policy.
3. Find exact-version upstream source/tests.
4. Decide whether local code adapts upstream behavior, adds application semantics, or reimplements upstream behavior.
5. Prefer maintained upstream implementations for generic protocol/crypto mechanics when they satisfy the required boundary.
6. Preserve application-specific security invariants when replacing mechanisms.
7. Require equivalence evidence before retiring assurance.

Review especially for: peer claims mistaken for relying-party evidence; identity mistaken for authorization; transient lifecycle IDs treated as durable application IDs; peer-selected trust; unnecessary crypto/protocol reimplementation; rotation changing application authority; rejection with side effects; and evidence transferred across revisions.

## Operational debugging

1. Establish topology: server, agents, workload, Workload API socket, trust domain, attestation plugin, registration ownership.
2. Establish exact versions.
3. Observe without mutation where possible.
4. Locate the failing boundary: connectivity, node attestation, registration, workload selection, Workload API, SVID/bundle, TLS/authentication, application authorization.
5. Compare against exact-version upstream evidence.
6. Classify before changing configuration.
7. Apply the smallest correction.
8. Re-run the narrowest proof.
9. Verify postconditions and unintended effects.

## Upgrade

Pin current baseline → identify relied-upon upstream behavior → pin candidate → compare offline → classify deltas → local integration → VM/system canary only after cheaper tiers pass.

## Assurance ladder

- Tier 0: application unit/property tests
- Tier 1: exact-version upstream-derived oracle/compatibility tests
- Tier 2: local SPIRE process/container integration
- Tier 3: disposable VM/system integration
- Tier 4: application composition / production-shaped canary

VMs should prove OS, privilege, filesystem, networking, service-manager, rollback, and composition properties—not serve as the primary oracle for ordinary SPIRE behavior.
