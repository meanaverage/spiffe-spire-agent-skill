# Upstream oracle navigation

This guide helps an agent answer ordinary SPIFFE/SPIRE behavior questions from version-matched upstream evidence before inventing a custom live experiment.

## First: pin the versions

Record:

```text
SPIRE version/tag
SPIFFE client implementation
SPIFFE client version
relevant attestor/plugin
```

Do not use `main` as a substitute for a known deployed version.

## SPIRE integration-suite map

Under a tagged SPIRE checkout, start at:

```text
test/integration/suites/
```

High-value suites commonly include:

- `join-token`
- `node-attestation`
- `node-re-attestation`
- `evict-agent`
- `entries`
- `fetch-x509-svids`
- `rotation`
- `nested-rotation`
- force-rotation suites
- workload-attestor suites
- agent/server CLI suites
- upgrade suites

Use suite `README.md`, numbered executable stages, shared helpers, config, and Docker Compose together. A stage name alone may not explain the preconditions that make its assertion meaningful.

## Question → likely oracle

### Can this node attest with this attestor?
Inspect the matching node-attestation suite/plugin tests and exact configuration.

### What identity does join-token attestation produce, and can the token be reused?
Inspect the tagged `join-token` suite plus relevant server/agent implementation tests.

### What happens after eviction?
Inspect `node-re-attestation`, `evict-agent`, and the selected node-attestor implementation. Do not generalize from one attestor to another.

### Why did this workload get this SVID?
Inspect `entries`, workload-attestor/selector behavior, and Workload API retrieval from the actual workload execution identity.

### Does rotation require application restart?
Inspect the tagged `rotation` suites and the exact client source abstraction (for example, a maintained X.509 source/watch implementation).

### How should SPIFFE IDs, SVIDs, bundles, or TLS peers be parsed/verified?
Prefer the exact selected maintained SPIFFE client implementation and tests over application-local parsing.

### Is this application request authorized?
Usually no upstream SPIRE suite can answer that. Once peer identity is authenticated, application binding/authorization/effect semantics belong to the consuming application unless deliberately delegated.

## Read the executable assertion, not just prose

When upstream contains an integration test:

1. read its setup;
2. read the exact numbered stage that establishes the assertion;
3. read helper functions used by that stage;
4. inspect configuration/attestors/selectors;
5. note timing/retry assumptions;
6. record the tagged path and version;
7. translate only the demonstrated behavior into your local compatibility test.

Do not copy upstream orchestration wholesale when a smaller compatibility oracle is sufficient.

## Prefer differential tests

For custom adapters, feed equivalent test material through:

```text
maintained upstream client
        vs
application adapter
```

Classify differences as:

- intentional application restriction/profile;
- environment adaptation;
- upstream version difference;
- adapter defect;
- unresolved.

This is especially useful for SPIFFE ID parsing, X.509-SVID verification, bundle handling, TLS peer extraction, CLI/API envelope compatibility, and rotation behavior.

## Escalation ladder

Only move to a more expensive environment when the cheaper tier cannot prove the property:

```text
spec/source/test
→ local compatibility test
→ local SPIRE process/container
→ disposable VM/system
→ application composition canary
```

A VM is appropriate for OS/service-manager/socket/filesystem/privilege/network/rollback properties. It should not normally be the first place an application discovers ordinary versioned SPIRE semantics.