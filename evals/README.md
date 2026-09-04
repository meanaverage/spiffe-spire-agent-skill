# Skill evaluation corpus

This directory provides small, versioned scenarios for evaluating whether an agent using this skill reaches the right conclusion **and cites the right authority**.

These are not production integration tests and do not execute SPIRE. They are reasoning/evidence-navigation tests.

## Goals

Measure whether the skill improves:

- exact-version discipline;
- selection of authoritative upstream evidence;
- separation of authentication from application authorization;
- distinction between node attestors with different lifecycle semantics;
- recognition of registration/workload-selection boundaries;
- rotation-aware client reasoning;
- failure-layer classification;
- uncertainty discipline.

## Scoring

Each scenario contains:

- `prompt`: the problem presented to the agent;
- `expected`: conclusions that should appear;
- `must_not`: conclusions that should not appear;
- `authority`: the upstream evidence class/path expected;
- `version`: the baseline to which the scenario applies.

A useful evaluation should score at least four dimensions independently:

1. **semantic correctness** — did the answer reach the right conclusion?
2. **authority correctness** — did it use the right source class/version?
3. **boundary correctness** — did it stop where SPIFFE/SPIRE authority stops?
4. **false-positive discipline** — did it avoid unsupported security claims?

## Baseline protocol

For model/skill comparisons:

1. Run scenarios without the skill.
2. Run the same scenarios with the skill.
3. Keep model/version/temperature/tool access constant where possible.
4. Score against the checked-in expectations.
5. Record disagreements rather than changing expectations to fit a model response.

Future real-world confirmed/rejected defect cases should be added as a separate corpus so these upstream-derived sanity checks remain stable.
