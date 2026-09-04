# spiffe-spire-agent-skill

A version-aware agent skill for engineering, reviewing, and troubleshooting SPIFFE/SPIRE systems, grounded in authoritative upstream specifications, source, and tests.

> **Don't teach agents what SPIRE does. Teach them how to determine what the exact SPIRE version does from authoritative evidence.**

## What this skill is for

- SPIFFE/SPIRE architecture and implementation review
- node/workload attestation troubleshooting
- join-token and re-attestation lifecycle analysis
- registration-entry and workload-selector debugging
- Workload API and X.509-SVID client review
- SPIFFE-aware mTLS review
- SVID and trust-bundle rotation
- version upgrades and behavioral-delta analysis
- production-readiness and failure classification

## Source policy

The skill uses this semantic-authority hierarchy:

1. SPIFFE specifications
2. exact-version SPIRE source and integration tests
3. exact-version maintained SPIFFE client source/tests
4. official SPIFFE/SPIRE documentation
5. first-party production consumers for operational methodology
6. community skills/examples as discovery aids

Community material may improve **how the agent investigates**. It does not override upstream evidence about **what SPIFFE/SPIRE does**.

See [`references/source-hierarchy.md`](references/source-hierarchy.md) and [`ACKNOWLEDGMENTS.md`](ACKNOWLEDGMENTS.md).

## Reference library

- [`references/upstream-oracle-navigation.md`](references/upstream-oracle-navigation.md) — find the cheapest exact-version source of truth
- [`references/attestation-and-registration.md`](references/attestation-and-registration.md) — join tokens, node attestation/re-attestation, entries, selectors
- [`references/rotation-and-bundles.md`](references/rotation-and-bundles.md) — SVID refresh, CA/bundle rotation, stale trust
- [`references/workload-api-and-mtls.md`](references/workload-api-and-mtls.md) — maintained clients, relying-party authentication, TLS
- [`references/failure-taxonomy.md`](references/failure-taxonomy.md) — classify incidents before changing configuration
- [`references/operational-principles.md`](references/operational-principles.md) — read-only-first troubleshooting
- [`references/workflows.md`](references/workflows.md) — review, debugging, upgrade, and assurance ladders
- [`references/version-baseline.md`](references/version-baseline.md) — included example baseline

## Initial reference baseline

The current examples were assembled against:

- SPIRE `v1.15.3`
- go-spiffe/v2 `v2.8.1`

These are reference versions, **not recommendations**. Version-sensitive work should establish the versions actually deployed or selected before drawing conclusions.

## Deliberate boundary

This public base does not define organization-specific application authorization, durable host/resource binding, business policy, or privileged-effect semantics.

Successful SPIFFE authentication identifies a peer under a trust model. It does not automatically answer what that peer may do in the consuming application.

## Agent Skills format

The repository follows the portable `SKILL.md` plus focused `references/` pattern so it can be adapted across compatible agent environments without tying the content to one product.

## License

Apache-2.0.
