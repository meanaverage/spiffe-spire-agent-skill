---
name: spiffe-spire
description: Version-aware engineering, review, and troubleshooting guidance for SPIFFE, SPIRE, Workload API, X.509-SVIDs, workload mTLS, attestation, registration, rotation, re-attestation, and production-readiness work.
---

# SPIFFE / SPIRE

Use this skill for architecture, implementation review, debugging, upgrade analysis, and production-readiness work involving SPIFFE or SPIRE.

## Governing rule

**Do not invent SPIFFE/SPIRE semantics.**

For version-sensitive behavior, establish deployed SPIRE and client-library versions first, then resolve disputed behavior from version-matched upstream specifications, source, tests, or official documentation. Community examples and generic zero-trust guidance are leads, not semantic authority.

## Before answering or changing code

1. Identify the SPIRE version when behavior may be version-sensitive.
2. Identify the SPIFFE client implementation/version when relevant.
3. Identify the boundary: specification, SPIRE implementation, client behavior, deployment integration, or application policy.
4. Prefer read-only observation before mutation during troubleshooting.
5. Find the narrowest authoritative upstream evidence.
6. State uncertainty when exact-version evidence is unavailable.
7. Never broaden trust or disable verification merely to diagnose a failure.

## Progressive disclosure

Load only the reference needed for the task:

- source disagreement / evidence quality → `references/source-hierarchy.md`
- architecture, review, debugging, upgrade, assurance tiers → `references/workflows.md`
- production troubleshooting discipline → `references/operational-principles.md`
- join tokens, node attestation, re-attestation, registration, selectors → `references/attestation-and-registration.md`
- X.509-SVID/bundle refresh and trust rotation → `references/rotation-and-bundles.md`
- Workload API clients and SPIFFE-aware mTLS → `references/workload-api-and-mtls.md`
- incident classification → `references/failure-taxonomy.md`
- application-authorization security invariants → `references/security-review-invariants.md`
- adjudicating plausible findings and false positives → `references/reviewer-discrimination-rules.md`
- finding exact tagged upstream evidence → `references/upstream-oracle-navigation.md`
- included example versions → `references/version-baseline.md`

Read `ACKNOWLEDGMENTS.md` when evaluating the provenance of this skill's methodology.

## Core boundaries

- A SPIFFE ID identifies a workload or node principal.
- An SVID is a credential used to prove a SPIFFE identity.
- A trust bundle establishes trust anchors.
- SPIRE issues/manages identities according to attestation and registration state.
- Authentication establishes the peer identity observed by the relying party.
- Application authorization remains an application concern unless deliberately delegated elsewhere.

Do not infer application permissions merely from successful SPIFFE authentication.

Do not assume one node attestor's bootstrap, eviction, or re-attestation lifecycle applies to another attestor.

Do not use a VM/system experiment as the first oracle for ordinary versioned SPIRE semantics when exact upstream evidence or a cheaper compatibility test can answer the question.

## Security review prompts

Before accepting a SPIFFE/SPIRE integration, ask:

- Is relying-party authentication evidence distinguished from peer claims?
- Is workload identity being mistaken for application authorization?
- Is transient attestation/bootstrap state being treated as durable application identity?
- Are trust anchors selected independently of the peer?
- Is maintained client functionality being unnecessarily reimplemented for SPIFFE IDs, SVID verification, bundle handling, or TLS?
- Can normal credential/bundle rotation occur without silently changing application authority?
- Are attestor-specific recovery and re-attestation semantics verified against the exact deployed version?
- Can a rejected request still cause application side effects?
- Is evidence bound to the source/version/configuration that actually produced it?

## Output discipline

For security-relevant findings report:

1. observed behavior;
2. authority/source;
3. version applicability;
4. failed boundary or security consequence;
5. smallest safe correction;
6. what remains unproven.

For security findings, state the boundary-specific evidence threshold and distinguish **suspicion**, **invariant violation**, **exploitability**, and **demonstrated bypass**.

Distinguish observed fact from inference. Do not transfer evidence between source revisions, binaries, configurations, or versions without an explicit equivalence argument.
