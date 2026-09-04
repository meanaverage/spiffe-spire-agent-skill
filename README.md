# spiffe-spire-agent-skill

A version-aware agent skill for engineering, reviewing, and troubleshooting SPIFFE/SPIRE systems, grounded in authoritative upstream specifications, source, and tests.

> **Don't teach agents what SPIRE does. Teach them how to determine what the exact SPIRE version does from authoritative evidence.**

## Evaluation

A frozen 2026-09-04 evaluation tested deterministic prompt packets on **12 contrastive cases that were unseen and locked at execution**, arranged as six matched semantic-twin pairs. It also reran three previously used development-regression cases separately. Each model/condition/case had three repetitions across four conditions and two exact target configurations. The harness concatenated `SKILL.md` and every Markdown reference into each skill-bearing prompt; **native skill loading and progressive disclosure were not tested**. The headline score is the sum of semantic correctness, authority correctness, boundary correctness, and false-positive discipline (0–2 each; 8 maximum). Claim-label consistency is reported separately.

| Exact recorded served target configuration | No skill | Generic control | SPIFFE/SPIRE base | **Base + adjudicated** |
|---|---:|---:|---:|---:|
| Self-hosted served alias `qwen38-27b-dflash2` · SGLang · NVFP4 · `dflash2` · TP2 · no-think · temp 0 · max 1,800; upstream model/weights not recorded | 5.333 | 7.069 | 5.569 | **7.500** |
| OpenAI `gpt-5.6-sol` · Codex CLI 0.151.0 · reasoning `medium` · ephemeral/read-only; sampling, max output, and service revision not recorded | 7.597 | 7.847 | 7.236 | **7.972** |

For the exact Qwen target, the observed mean-judge rates for the revised packet versus the base packet were **0% versus 31.94%** contradictory labels, **6.67% versus 50.00%** benign false positives, and **0% versus 38.10%** positive underclaims. Benign-FP judgments differed by grader: base was 0% (Qwen grader) versus 100% (OpenAI grader), and revised was 0% versus 13.33%. For the exact OpenAI target under the revised condition, both graders recorded 0% overclaim, underclaim, contradictory-label, benign-FP, and positive-underclaim rates on these 36 primary responses.

The run contained **288 primary and 72 development-regression target responses**. All 360 were scored by both the served alias `qwen38-27b-dflash2` (no-think, temperature 0, max 8,000; upstream model and deployment revision not recorded) and OpenAI `gpt-5.6-sol` via Codex CLI 0.151.0 (`medium` reasoning; service revision and sampling not recorded), producing **720 response-level blind grades**. Graders saw ground truth but not provider, condition, repetition, or run identity; prose could still reveal clues, and each grader scored 180 outputs from its own model identifier. There was no third-grader adjudication.

**Important:** these measurements apply only to the exact tested configurations and corpus. They are not security certification or a claim of general model superiority. Several serving/sampling details and immutable backend revisions were not recorded. Once disclosed, these 12 cases become `PUBLIC_REGRESSION_V0` and must never again support an unseen-evidence claim; future tuning/generalization claims require a new `UNRELEASED_GENERALIZATION_HOLDOUT`.

[Full evaluation methodology, configurations, scoring, validation, and limitations →](docs/evaluation.md)

### Independent evaluation

This skill is one system evaluated by the implementation-neutral
[spiffe-spire-agent-evals](https://github.com/meanaverage/spiffe-spire-agent-evals)
project. The benchmark can also evaluate other skills, prompts, agents,
generic guidance, and no-guidance baselines; using this skill is not required.

The frozen 2026-09-04 result applies only to the exact tested skill-content
packet, target configurations, corpus, graders, and methodology recorded in
the result manifest. The harness placed `SKILL.md` and every Markdown reference
into each prompt, so native skill discovery and progressive disclosure were
not tested. The result is not a security certification or a claim of general
model superiority.

See the [independent corpus and v0.1.0 release](https://github.com/meanaverage/spiffe-spire-agent-evals/releases/tag/v0.1.0)
for the methodology, limitations, provenance, and immutable result manifest.

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

The repository includes [`evals/`](evals/) with versioned reasoning scenarios and a scoring rubric. These tests do not execute SPIRE; responses are graded under a published rubric for conclusions, source/version choice, boundary ownership, and unsupported security claims.

The public baseline contains eight upstream/specification and bounded-derived scenarios covering join-token reuse, attestor-specific re-attestation, UID selection, rotation, authentication-versus-authorization, relying-party evidence, readiness, and unknown-version discipline. A separate three-case development-regression corpus contains product-neutral scenarios generalized from independently adjudicated private integration review.

Public regression cases and frozen results are maintained by the independent
[spiffe-spire-agent-evals](https://github.com/meanaverage/spiffe-spire-agent-evals)
project. Future unreleased holdouts must be governed outside public GitHub and
outside this runtime skill surface.

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
