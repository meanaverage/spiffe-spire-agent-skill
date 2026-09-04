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

Read `references/source-hierarchy.md` when sources disagree.
Read `references/workflows.md` for review/debug/upgrade procedures.
Read `references/operational-principles.md` for production troubleshooting.
Read `references/version-baseline.md` for the included reference baseline.
Read `references/workload-api-and-mtls.md` for client/TLS work.

## Core boundaries

- A SPIFFE ID identifies a workload or node principal.
- An SVID is a credential used to prove a SPIFFE identity.
- A trust bundle establishes trust anchors.
- SPIRE issues/manages identities according to attestation and registration state.
- Authentication establishes the peer identity observed by the relying party.
- Application authorization remains an application concern unless deliberately delegated elsewhere.

Do not infer application permissions merely from successful SPIFFE authentication.

## Output discipline

For security-relevant findings report: observed behavior; authority/source; version applicability; security consequence; smallest safe correction; and what remains unproven.

Distinguish observed fact from inference. Do not transfer evidence between source revisions, binaries, configurations, or versions without an explicit equivalence argument.
