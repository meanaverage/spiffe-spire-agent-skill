# Attestation and registration

Use this reference when reviewing node attestation, workload attestation, join-token bootstrap, registration entries, workload selection, or SVID retrieval.

## Separate the layers

A useful review order is:

```text
node attestation
    ↓
attested agent identity
    ↓
registration entries
    ↓
workload attestation / selectors
    ↓
Workload API result
    ↓
application authentication
```

Do not collapse these into one assertion.

A node becoming attested does not itself prove that a particular workload should receive a particular SVID. Registration and workload selectors remain distinct.

## Join-token lifecycle

Treat join-token behavior as version-sensitive SPIRE implementation behavior, not generic zero-trust folklore.

For the included SPIRE v1.15.3 reference baseline, inspect the tagged `test/integration/suites/join-token` suite. It explicitly exercises server startup, agent bootstrap, workload registration, SVID retrieval, and a failed reused/bad-token case.

The corresponding tagged suite documents three properties: an agent can attest with a join token; the resulting agent identity can parent workload registration; and a join token cannot be reused.

Do not infer that join-token attestation has the same re-attestation semantics as another node attestor.

## Re-attestation and eviction

When recovery or eviction is involved, identify the node-attestor semantics before prescribing a restart or rebootstrap procedure.

For SPIRE v1.15.3, `test/integration/suites/node-re-attestation` deliberately compares a re-attestable `x509pop` agent with a join-token agent. The tagged `03-evict-agents` case states that the join-token agent does not re-attest because the join-token plugin uses a trust-on-first-use model.

Therefore, for version-sensitive recovery questions:

1. identify the node attestor;
2. locate the exact-version re-attestation behavior;
3. distinguish credential recovery from application identity/authority recovery;
4. do not generalize one attestor's lifecycle to another.

## Registration entries

Treat registration entries as SPIRE issuance policy, not as application business authorization unless the application explicitly chooses that model.

When debugging a missing or wrong SVID, inspect:

- parent ID;
- SPIFFE ID;
- selectors;
- DNS names or other entry attributes;
- which agent received the entry;
- which workload selectors the agent observed;
- propagation/readiness state.

For SPIRE v1.15.3, the `entries` integration suite creates parented entries for multiple agents, retrieves SVIDs as distinct Unix UIDs, validates a shared workload identity across agents, checks DNS names, updates entries, and deletes them.

That suite is a better oracle for ordinary registration/selector semantics than a custom VM experiment.

## Review questions

- Is the code confusing an attested agent identity with a workload identity?
- Is a transient bootstrap identity being treated as durable application identity?
- Is a registration entry being treated as proof of application authorization beyond SVID issuance?
- Is the parent ID exact and current?
- Are selectors being interpreted by the correct workload attestor?
- Is the observed Workload API result proven from the workload's execution context rather than from an administrative view?
- Does recovery preserve only the intended registration inventory?

## Evidence hierarchy

For lifecycle claims, prefer exact-version SPIRE integration tests/source. For workload-client behavior after issuance, prefer the exact selected SPIFFE client implementation and its tests.