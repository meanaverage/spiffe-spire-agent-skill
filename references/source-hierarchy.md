# Source hierarchy

Use the strongest available source for the claim being made.

1. **SPIFFE specifications** — protocol and identity-model requirements.
2. **Exact-version SPIRE source and integration tests** — implemented SPIRE lifecycle behavior.
3. **Exact-version maintained SPIFFE client source/tests** — client semantics such as SPIFFE ID parsing, Workload API, X.509-SVID verification, bundles, and SPIFFE-aware TLS.
4. **Official SPIFFE/SPIRE documentation** — supported configuration and concepts.
5. **First-party production consumers** — operational patterns only.
6. **Community skills/tutorials/examples** — discovery aids only.

Never resolve a disputed security-sensitive semantic claim from levels 5–6 when levels 1–4 are available.

## Conflict rule

When sources disagree:

1. Confirm versions.
2. Prefer normative SPIFFE specifications for protocol requirements.
3. Prefer exact deployed-version SPIRE behavior for SPIRE implementation questions.
4. Prefer exact selected client-library behavior for client implementation questions.
5. Record unresolved discrepancies instead of silently blending sources.
