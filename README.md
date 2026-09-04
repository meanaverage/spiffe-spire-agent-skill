# spiffe-spire-agent-skill

A version-aware agent skill for engineering, reviewing, and troubleshooting SPIFFE/SPIRE systems, grounded in authoritative upstream specifications, source, and tests.

> **Don't teach agents what SPIRE does. Teach them how to determine what the exact SPIRE version does from authoritative evidence.**

## Evaluation

A frozen post-tuning evaluation used **12 unseen contrastive holdouts in six matched semantic-twin pairs**, three fresh repetitions, four conditions, two target model configurations, and two blinded model graders. The headline score is the sum of semantic correctness, authority correctness, boundary correctness, and false-positive discipline (0–2 each; 8 maximum). Claim-label consistency is reported separately.

| Exact target configuration | No skill | Generic control | SPIFFE/SPIRE base | **Base + adjudicated** |
|---|---:|---:|---:|---:|
| Qwen `qwen38-27b-dflash2` · SGLang · NVFP4 · `dflash2` · TP2 · no-think · temp 0 · max 1,800 | 5.333 | 7.069 | 5.569 | **7.500** |
| OpenAI `gpt-5.6-sol` · Codex CLI 0.151.0 · reasoning effort `medium` · ephemeral/read-only | 7.597 | 7.847 | 7.236 | **7.972** |

For the tested Qwen configuration, adjudicated guidance reduced contradictory labels from **31.94% → 0%**, benign false positives from **50.00% → 6.67%**, and positive underclaims from **38.10% → 0%** relative to the base skill. For the tested OpenAI configuration, the adjudicated condition recorded **0% overclaim, underclaim, and contradictory-label rates** on the holdouts.

All 360 target responses were anonymously scored by both Qwen `qwen38-27b-dflash2` (no-think, temperature 0, max 8,000) and OpenAI `gpt-5.6-sol` via Codex CLI 0.151.0 (`medium` reasoning). There were **720 response-level blind grades**. Graders saw ground truth but not target provider, condition, repetition, or run identity; each grader also scored outputs from its own model identifier while blinded to that identity.

**Important:** these measurements apply only to the exact tested configurations and corpus. They are not security certification or a claim of general model superiority. The benchmark flattened `SKILL.md` and every Markdown reference into prompt context, so native skill loading and progressive disclosure were **not** tested. Several serving/sampling details and immutable backend revisions were not recorded. Completed holdouts are no longer unseen once disclosed.

[Full evaluation methodology, configurations, scoring, validation, and limitations →](docs/evaluation.md)

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
- [`references/security-review-invariants.md`](references/security-review-invariants.md) — application-authorization and relying-party review invariants
- [`references/reviewer-discrimination-rules.md`](references/reviewer-discrimination-rules.md) — evidence thresholds and false-positive discrimination
- [`references/operational-principles.md`](references/operational-principles.md) — read-only-first troubleshooting
- [`references/workflows.md`](references/workflows.md) — review, debugging, upgrade, and assurance ladders
- [`references/version-baseline.md`](references/version-baseline.md) — included example baseline

## Evaluation corpus

The repository includes [`evals/`](evals/) with versioned reasoning scenarios and a scoring rubric. These tests do not execute SPIRE; they measure whether an agent reaches the correct conclusion, chooses the correct authority/version, respects the SPIFFE/SPIRE versus application-policy boundary, and avoids unsupported security claims.

The upstream-derived corpus covers join-token reuse, attestor-specific re-attestation, UID selector behavior, SVID/bundle rotation, authentication-versus-authorization, relying-party evidence, health/readiness, and unknown-version discipline. A separate generalized historical corpus tests evidence thresholds and calibrated security claims.

A separate implementation-neutral evaluation repository is planned so public benchmark ground truth and future unreleased holdouts do not become part of the runtime skill surface.

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
