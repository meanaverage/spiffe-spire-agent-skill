# Evaluation

This document records the frozen 2026-09-04 post-tuning evaluation of the adjudicated SPIFFE/SPIRE review guidance. Results apply only to the exact configurations and corpus described here. They are **not security certification**.

## Primary unseen-holdout results

The primary corpus contained 12 unseen contrastive cases arranged as six matched semantic-twin pairs and locked before the tested skill edit. Each model/condition/case was run three times. Scores below are means from two blinded model graders.

| Target configuration | Condition | Score / 8 | Consistency / 2 | Overclaim | Underclaim | Contradictory label | Benign FP | Positive underclaim |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Qwen `qwen38-27b-dflash2`; SGLang, NVFP4, `dflash2`, TP2, no-think, temp 0, max 1,800 | No skill | 5.333 | 0.972 | 43.06% | 26.39% | 30.56% | 50.00% | 38.10% |
| Same Qwen configuration | Base + generic security control | 7.069 | 1.778 | 9.72% | 6.94% | 4.17% | 16.67% | 4.76% |
| Same Qwen configuration | SPIFFE/SPIRE base | 5.569 | 0.972 | 45.83% | 23.61% | 31.94% | 50.00% | 38.10% |
| Same Qwen configuration | Base + adjudicated guidance | **7.500** | **1.944** | **2.78%** | **0.00%** | **0.00%** | **6.67%** | **0.00%** |
| OpenAI `gpt-5.6-sol`; Codex CLI 0.151.0, reasoning effort `medium`, ephemeral/read-only | No skill | 7.597 | 1.750 | 13.89% | 0.00% | 11.11% | 0.00% | 0.00% |
| Same OpenAI configuration | Base + generic security control | 7.847 | 1.972 | 4.17% | 0.00% | 0.00% | 0.00% | 0.00% |
| Same OpenAI configuration | SPIFFE/SPIRE base | 7.236 | 1.708 | 26.39% | 0.00% | 11.11% | 13.33% | 0.00% |
| Same OpenAI configuration | Base + adjudicated guidance | **7.972** | **2.000** | **0.00%** | **0.00%** | **0.00%** | **0.00%** | **0.00%** |

For the tested Qwen configuration, adjudicated guidance exceeded the base skill by **+1.931/8** and the size-near generic-security control by **+0.431/8**. For the tested OpenAI configuration, it exceeded the base by **+0.736/8** and the generic control by **+0.125/8**.

The completed holdouts are no longer unseen once disclosed. Future tuning claims require a new unreleased holdout corpus.

## What was scored

Four dimensions are scored from 0–2 and summed to the 8-point headline score:

1. semantic correctness;
2. authority correctness;
3. boundary correctness;
4. false-positive discipline.

Claim-label consistency is scored separately from 0–2. It checks whether the final claim strength agrees with the response's own evidence narrative; it is not simply another measure of agreement with ground truth.

A **benign false positive** is an overclaim on a holdout whose expected claim is `non_finding`. A **positive underclaim** is an underclaim on a positive holdout. A **contradictory label** means the narrative denies evidence required by its final label, or dismisses an owning-boundary invariant that the narrative itself establishes.

## Target configurations

### Qwen

- served alias: `qwen38-27b-dflash2`
- runtime: self-hosted SGLang, OpenAI-compatible chat-completions API
- quantization: NVFP4
- build/kernel tag: `dflash2`
- tensor parallelism: 2
- thinking: disabled with `chat_template_kwargs.enable_thinking=false`
- temperature: 0
- maximum output: 1,800 tokens
- strict JSON-schema output
- no tools or browser interface supplied

The underlying upstream model identity, immutable weights revision, SGLang revision, omitted sampler defaults, and inference seed were not recorded.

### OpenAI / Codex

- model: `gpt-5.6-sol`
- Codex CLI: 0.151.0
- reasoning effort: `medium`
- `codex exec --ephemeral`
- isolated working directory per sample
- user configuration/workspace rules ignored
- read-only sandbox
- strict frozen output schema
- prompt prohibited tools and browsing; zero target tool events were recorded

Temperature, `top_p`, seed, maximum output tokens, service-side model revision, and exact sandbox network policy were not recorded.

Both targets received the same 648-byte reviewer instruction (SHA-256 `d2507e1f5103286932c5ebcd505cce502436481efe8768c26e1e790fe8897204`) and three fresh repetitions per model/condition/case.

## Skill conditions

| Condition | Revision / source | Packet size |
|---|---|---:|
| No skill | none | 0 bytes / 0 words |
| Generic security control | base `fbf9d2751a526f4f0ab059fa14facd942571cc5f` + control SHA-256 `a40a05d76f6dbba471e718b9db7c64c5c07870320ec0267f80f9e3f78d210ccc` | 38,319 bytes / 4,971 words |
| SPIFFE/SPIRE base | `fbf9d2751a526f4f0ab059fa14facd942571cc5f` | 25,863 bytes / 3,295 words |
| Base + adjudicated guidance | `569e98164e64c6e1d7632511895e44a4d6e0a641` | 40,370 bytes / 5,167 words |

The generic addition itself was 12,393 bytes / 1,673 words and contained no SPIFFE-specific material, but its condition also contained the complete SPIFFE/SPIRE base packet.

For skill-bearing conditions the harness flattened `SKILL.md` plus every Markdown reference into prompt context. **Native skill loading and progressive disclosure were not tested.** Ground-truth answer fields were absent from target context.

## Blinded grading

All 360 target responses were anonymously graded by both:

- Qwen `qwen38-27b-dflash2`, no-think, temperature 0, max 8,000 output tokens; and
- OpenAI `gpt-5.6-sol` through Codex CLI 0.151.0, reasoning effort `medium`, ephemeral/read-only mode.

Each grader saw the rubric, full scenario ground truth, and 12 anonymous responses. Provider, condition, repetition, and run identifiers were withheld, although response prose could still contain stylistic clues. Each grader therefore also scored 180 responses produced by its own model identifier while blinded to that identity.

There were 720 response-level grades in 60 grader calls. No third-grader adjudication was used: numeric dimension scores were averaged with equal weight, while Boolean results retained mean-judge and individual/both/either-grader rates. Across 1,800 dimension comparisons, exact grader agreement was 82.44% and mean absolute difference was 0.1878 on the 0–2 scale.

## Development-regression corpus

Three previously used cases were rerun separately and were **not** included in the primary holdout score.

| Target configuration | No skill | Generic control | Base | Adjudicated |
|---|---:|---:|---:|---:|
| Qwen configuration above | 4.778 | 6.222 | 5.222 | **7.111** |
| OpenAI configuration above | 7.444 | 7.889 | 7.944 | **8.000** |

## Validation and limitations

The run contained 288 primary-holdout responses and 72 development-regression responses: 360 total. All 360 target responses and 720 blind grades were accounted for. The frozen validation recorded zero retained target/grader failures, zero target/grader tool events, zero response/grade schema errors, and zero exact answer-field leakage hits.

Important limitations:

- only 12 unseen holdout cases, three development cases, three repetitions, two target configurations, and two model graders were used;
- temperature-zero repetitions are observations, not guaranteed independent statistical trials;
- the Qwen served alias does not uniquely identify immutable upstream weights;
- several serving/sampling details were not frozen;
- OpenAI service-side model revision and unexposed inference controls were not recorded;
- actual worker counts and exact invocation lines were not frozen;
- Codex's zero-tool behavior was observed, but hard filesystem/network inaccessibility of every benchmark artifact was not cryptographically established;
- the benchmark flattened every reference into context, so it does not measure native progressive-disclosure behavior.

These results support the tested revision under the tested conditions. They do not establish general model capability, statistical superiority, or security certification.
