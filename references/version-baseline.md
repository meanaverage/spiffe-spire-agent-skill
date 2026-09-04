# Included reference baseline

Initial reference baseline:

- SPIRE `v1.15.3`
- go-spiffe/v2 `v2.8.1`

This is a reference baseline, not a universal recommendation. Always establish actual deployed versions before version-sensitive claims.

SPIRE v1.15.3's integration suite includes executable scenarios for join-token, node attestation/re-attestation, eviction, rotation, entries, X.509-SVID retrieval, workload attestation, CLI behavior, and upgrades.

For example, its `node-re-attestation` suite contains:

```text
00-setup
01-start-server
02-start-agent
03-evict-agents
04-check-re-attest
```

Use exact tagged upstream files rather than copying their semantics into this skill. The skill should teach where truth lives and how to reason about it, not freeze large upstream implementations into prose.
