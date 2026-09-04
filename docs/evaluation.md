# Evaluation

This document records the frozen 2026-09-04 evaluation of deterministic prompt packets containing the adjudicated SPIFFE/SPIRE review guidance. Results apply only to the exact configurations and corpus described here. They are **not security certification**.

## Primary results: unseen at execution, PUBLIC_REGRESSION_V0 after disclosure

The primary corpus contained 12 contrastive cases that were unseen and locked before the tested skill edit, arranged as six semantic-twin pairs. Each model/condition/case was run three times, yielding 288 primary responses. Numeric scores are equal-weight means from two blinded model graders; Boolean columns below are mean-judge rates, not adjudicated event rates.

| Target configuration | Condition | Score / 8 | Consistency / 2 | Overclaim (mean-judge) | Underclaim (mean-judge) | Contradictory label (mean-judge) | Benign FP (mean-judge; 15 benign responses) | Positive underclaim (mean-judge; 21 positive responses) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Served alias `qwen38-27b-dflash2`; SGLang, NVFP4, `dflash2`, TP2, no-think, temp 0, max 1,800 | No skill | 5.333 | 0.972 | 43.06% | 26.39% | 30.56% | 50.00% | 38.10% |
| Same Qwen served configuration | Base + generic security control | 7.069 | 1.778 | 9.72% | 6.94% | 4.17% | 16.67% | 4.76% |
| Same Qwen served configuration | SPIFFE/SPIRE base | 5.569 | 0.972 | 45.83% | 23.61% | 31.94% | 50.00% | 38.10% |
| Same Qwen served configuration | Base + adjudicated guidance | **7.500** | **1.944** | **2.78%** | **0.00%** | **0.00%** | **6.67%** | **0.00%** |
| OpenAI `gpt-5.6-sol`; Codex CLI 0.151.0, reasoning effort `medium`, ephemeral/read-only | No skill | 7.597 | 1.750 | 13.89% | 0.00% | 11.11% | 0.00% | 0.00% |
| Same OpenAI configuration | Base + generic security control | 7.847 | 1.972 | 4.17% | 0.00% | 0.00% | 0.00% | 0.00% |
| Same OpenAI configuration | SPIFFE/SPIRE base | 7.236 | 1.708 | 26.39% | 0.00% | 11.11% | 13.33% | 0.00% |
| Same OpenAI configuration | Base + adjudicated guidance | **7.972** | **2.000** | **0.00%** | **0.00%** | **0.00%** | **0.00%** | **0.00%** |

For the exact Qwen target, the observed revised-packet mean was **1.931/8 above** the base-packet mean and **0.431/8 above** the word-count-near and byte-size-near generic-control mean. For the exact OpenAI target, the observed differences were **+0.736/8** and **+0.125/8**. No significance or broad superiority claim is made.

At disclosure these cases become `PUBLIC_REGRESSION_V0`. They must not be described as unseen in future runs, and future tuning/generalization claims require a new `UNRELEASED_GENERALIZATION_HOLDOUT`.

## What was scored

Four dimensions are scored from 0–2 and summed to the 8-point headline score:

1. semantic correctness;
2. authority correctness;
3. boundary correctness;
4. false-positive discipline.

Claim-label consistency is scored separately from 0–2. It checks whether the final claim strength agrees with the response's own evidence narrative; it is not simply another measure of agreement with ground truth.

A **benign false positive** is an overclaim among the five primary cases whose first expected claim is `non_finding` (15 responses per model/condition). A **positive underclaim** is an underclaim among the seven cases whose first expected claim is not `non_finding` (21 responses); that set includes `invariant_violation` and `demonstrated_bypass` ground truth. A **contradictory label** means the response's narrative denies evidence required by its own final label, or dismisses an owning-boundary invariant that the narrative itself establishes. Headline percentages are equal-weight means of the two graders' binary flags.

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

The served alias does not identify the underlying upstream model. Upstream identity, immutable weights revision/hash, exact quantization recipe, SGLang version/commit, `dflash2` definition, kernels/drivers/accelerator, omitted sampler defaults, and seed were `UNKNOWN` or `NOT_RECORDED` as specified in the frozen manifest.

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

Both targets received the same 648-byte reviewer instruction text (SHA-256 `d2507e1f5103286932c5ebcd505cce502436481efe8768c26e1e790fe8897204`): as a system message for Qwen and concatenated on stdin for Codex. Each model/condition/case had three fresh observed repetitions.

## Skill conditions

| Condition | Revision / source | Packet size |
|---|---|---:|
| No skill | none | 0 bytes / 0 words |
| Generic security control | base `fbf9d2751a526f4f0ab059fa14facd942571cc5f` + control SHA-256 `a40a05d76f6dbba471e718b9db7c64c5c07870320ec0267f80f9e3f78d210ccc` | 38,319 bytes / 4,971 words |
| SPIFFE/SPIRE base | `fbf9d2751a526f4f0ab059fa14facd942571cc5f` | 25,863 bytes / 3,295 words |
| Base + adjudicated guidance | `569e98164e64c6e1d7632511895e44a4d6e0a641` | 40,370 bytes / 5,167 words |

> The tested `BASE_PLUS_ADJUDICATED_REVISED` packet was built from skill revision `569e98164e64c6e1d7632511895e44a4d6e0a641`. Current main contains the accepted guidance through squash merge `12992f03b2489c18dfae856cfec9cd0b9fd0354f`; all 12 files in the tested packet match current main by SHA-256, but the measured Git revision remains `569e98164e64c6e1d7632511895e44a4d6e0a641`.

The generic addition itself was 12,393 bytes / 1,673 whitespace-delimited words and contained no SPIFFE-specific material; its condition also contained the complete base packet. The combined generic packet was 38,319 bytes / 4,971 words versus 40,370 bytes / 5,167 words for the revised packet. Tokenizer-token counts were `NOT_RECORDED`.

For every skill-bearing condition, the harness deterministically concatenated `SKILL.md` and every Markdown reference into one prompt packet, so all references were visible on every request. This was a **skill-content-packet evaluation**; native skill loading, filesystem discovery, routing, and progressive disclosure were not tested. Ground-truth answer fields were absent from target prompt context.

## Blinded grading

All 360 target responses were anonymously graded by both:

- served alias `qwen38-27b-dflash2`, no-think, temperature 0, max 8,000 output tokens; and
- OpenAI `gpt-5.6-sol` through Codex CLI 0.151.0, reasoning effort `medium`, ephemeral/read-only mode.

The Qwen grader's upstream model/deployment revision and the OpenAI grader's service revision/sampling settings were not recorded.

Each grader saw the rubric, full scenario ground truth, and 12 anonymous responses. Provider, condition, repetition, and run identifiers were withheld, although response prose could still contain stylistic clues. Each grader therefore also scored 180 responses produced by its own model identifier while blinded to that identity.

There were 720 response-level grades in 60 grader calls. No third-grader adjudication was used: numeric dimension scores were averaged with equal weight, while Boolean results retained mean-judge and individual/both/either-grader rates. Across 1,800 dimension comparisons, exact grader agreement was 82.44% and mean absolute difference was 0.1878 on the 0–2 scale. Boolean disagreement was materially larger in some cells: for Qwen-target base benign cases the Qwen grader reported 0% benign FP and the OpenAI grader 100%, producing the 50% mean-judge headline; revised rates were 0% and 13.33%, producing 6.67%. Individual, both/either, and mean-judge rates should be considered together.

## Development-regression corpus

Three previously used cases were rerun separately and were **not** included in the primary score.

| Target configuration | No skill | Generic control | Base | Adjudicated |
|---|---:|---:|---:|---:|
| Qwen configuration above | 4.778 | 6.222 | 5.222 | **7.111** |
| OpenAI configuration above | 7.444 | 7.889 | 7.944 | **8.000** |

## Validation and limitations

The run contained 288 primary responses and 72 development-regression responses: 360 total. All 360 target responses and 720 blind grades were accounted for. The frozen validation recorded zero retained target/grader failures, zero target/grader tool events, zero response/grade schema errors, and zero exact answer-field leakage hits.

Important limitations:

- only 12 primary cases, three development cases, three repetitions, two target configurations, and two model graders were used;
- temperature-zero repetitions are observations, not guaranteed independent statistical trials;
- the Qwen served alias does not uniquely identify immutable upstream weights;
- several serving/sampling details were not frozen;
- OpenAI service-side model revision and unexposed inference controls were not recorded;
- actual worker counts and exact invocation lines were not frozen;
- Codex's zero-tool behavior was observed, but hard filesystem/network inaccessibility of every benchmark artifact was not cryptographically established;
- the benchmark flattened every reference into context, so it does not measure native progressive-disclosure behavior;
- Boolean flags were not third-adjudicated and some per-grader rates diverged sharply;
- the holdouts were authored after diagnosing the first ablation, although locked before the skill wording change, so external validity is limited to the tested reasoning families.

These results support skill revision `569e98164e64c6e1d7632511895e44a4d6e0a641` under the tested conditions. Current main contains matching tested packet source bytes through squash merge `12992f03b2489c18dfae856cfec9cd0b9fd0354f`. The results do not establish general model capability, statistical superiority, or security certification.
