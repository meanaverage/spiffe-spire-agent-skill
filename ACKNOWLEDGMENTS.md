# Acknowledgments and provenance

This project separates **semantic authority** from **agent-skill/runbook design inspiration**.

## Semantic authority

SPIFFE/SPIRE behavior in this skill should be grounded in authoritative upstream material, principally:

- SPIFFE specifications and project documentation: https://spiffe.io/
- SPIRE source and integration tests: https://github.com/spiffe/spire
- go-spiffe source and tests: https://github.com/spiffe/go-spiffe

The initial reference baseline used while drafting this skill is SPIRE `v1.15.3` and go-spiffe/v2 `v2.8.1`. Those versions are examples/reference points, not universal recommendations.

The skill intentionally points agents back to tagged upstream material rather than copying large amounts of upstream implementation or test content.

## Agent-skill and runbook design inspiration

The public skill structure synthesizes general procedural ideas seen in several agent/runbook ecosystems. These projects are **not treated as authorities for SPIFFE/SPIRE semantics**.

### wshobson/agents — mTLS configuration skill

https://github.com/wshobson/agents

Useful design ideas include:

- a concise top-level `SKILL.md`;
- progressive disclosure into focused reference documents;
- clear trigger/use-case descriptions;
- short best-practice and troubleshooting sections.

We do not rely on its SPIRE examples as semantic authority; some examples are intentionally generic and version-specific.

### williamzujkowski/cognitive-toolworks

https://github.com/williamzujkowski/cognitive-toolworks

Useful procedural ideas include:

- prechecks before acting;
- explicit decision rules;
- abort/stop conditions;
- source freshness and uncertainty handling;
- structured outputs rather than unconstrained advice.

### NVIDIA OpenShell agent/runbook material

https://github.com/NVIDIA/OpenShell

Useful operational ideas include:

- establish topology and ownership before mutation;
- observe authoritative state first;
- separate transport, identity, configuration, and runtime failures;
- avoid treating advertised metadata or process existence as stronger authority/health evidence than it actually provides;
- prefer fail-closed diagnosis and the smallest corrective action.

Again, OpenShell is cited for operational methodology, not to define SPIFFE/SPIRE behavior.

## Original synthesis

The wording, source hierarchy, workflows, failure taxonomy, and upstream-oracle navigation in this repository are an original synthesis designed for portable Agent Skills use.

The governing principle is:

> Use community and production-agent material to improve **how an agent investigates** SPIFFE/SPIRE, while using SPIFFE/SPIRE upstream sources to determine **what SPIFFE/SPIRE actually does**.

If this repository ever conflicts with authoritative upstream behavior for the version being investigated, the upstream behavior wins and the skill should be corrected.