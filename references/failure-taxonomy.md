# Failure taxonomy

Use this taxonomy to classify a failure before changing configuration.

The goal is not to force every incident into one label. The goal is to stop downstream compensations from hiding the actual failed boundary.

## 1. Transport / reachability

Examples:
- server endpoint unreachable;
- Workload API socket absent;
- socket permissions prevent access;
- DNS/routing/firewall failure;
- timeout before protocol exchange.

Do not diagnose this as an identity-policy problem until transport is established.

## 2. SPIRE server availability/configuration

Examples:
- server not ready;
- datastore/config/plugin load failure;
- required listener unavailable;
- trust-domain/config mismatch.

Prove server readiness using server-specific evidence, not process existence alone.

## 3. Node attestation

Examples:
- join token invalid/consumed/expired;
- attestor-specific evidence rejected;
- node selector mismatch;
- agent cannot establish its attested identity.

Identify the exact node attestor and version before proposing recovery.

## 4. Agent state / re-attestation

Examples:
- evicted agent cannot re-attest with its configured attestor;
- cached state conflicts with intended bootstrap;
- agent identity differs from the identity expected by the operator.

Do not assume all attestors have equivalent recovery semantics.

## 5. Registration / propagation

Examples:
- missing entry;
- wrong parent ID;
- wrong SPIFFE ID;
- selector mismatch;
- entry update has not propagated;
- workload receives a different entry than expected.

Administrative inventory alone does not prove the workload actually received the expected SVID.

## 6. Workload attestation / selection

Examples:
- UID/process/container selector mismatch;
- workload executes under a different identity/context than expected;
- selector plugin unavailable.

Observe from the workload execution context when possible.

## 7. Workload API client

Examples:
- wrong socket endpoint;
- client cannot parse/update context;
- source closed;
- initial update never arrives;
- application uses stale manually cached material.

Compare custom behavior with the exact maintained client implementation.

## 8. SVID / bundle validity

Examples:
- expired/not-yet-valid SVID;
- chain verification failure;
- wrong trust domain;
- missing/current bundle unavailable;
- stale bundle assumption;
- key/certificate mismatch in custom adapters.

Keep credential-format/verification failures separate from application authorization.

## 9. TLS relying-party authentication

Examples:
- handshake rejects peer;
- verified peer ID differs from expected ID;
- wrong trust domain/bundle source;
- application reads a claimed identity from payload instead of verified peer state.

Authentication evidence must come from the component that actually verified the peer.

## 10. Application binding / authorization

Examples:
- verified SPIFFE identity has no application binding;
- current binding is revoked/disabled;
- authenticated identity lacks requested permission;
- authorization changed after authentication.

This is normally application policy, not a SPIRE failure.

## 11. Application effect / transaction

Examples:
- rejected request still changes state;
- replay consumed separately from protected mutation;
- authorization becomes stale before effect;
- partial failure leaves ambiguous state.

SPIFFE can authenticate the actor; it cannot prove application transaction semantics.

## 12. Evidence / observability defect

Examples:
- failure is real but retained diagnostics cannot identify the stage;
- evidence records claims not actually observed;
- raw secrets are retained unnecessarily;
- old evidence is attributed to a new source/version.

Improve bounded attribution before blindly retrying.

## Safe debugging rule

For any incident, report:

```text
failed boundary
observed evidence
exact version
known upstream behavior
unknowns
smallest next observation/correction
```

Do not widen trust, disable certificate verification, or switch to permissive identity behavior solely to make the symptom disappear.