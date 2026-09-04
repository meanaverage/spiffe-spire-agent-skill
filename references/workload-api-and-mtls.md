# Workload API and mTLS review

When reviewing custom Workload API communication, SPIFFE ID parsing, X.509-SVID parsing, chain verification, bundle handling, refresh, SPIFFE-aware TLS, or peer-ID extraction, first compare it against a maintained SPIFFE client implementation. For Go, inspect the selected `go-spiffe/v2` version.

Custom code may still be justified for application-specific custody, process boundaries, provenance, bounded I/O, or policy. Keep those concerns separate from SPIFFE protocol semantics.

## Relying-party perspective

Authentication evidence should come from the component that actually verified the peer. Client-supplied IDs, application JSON claims, unverified URI SANs, and stale enrollment artifacts are not equivalent.

## Trust

The peer should not select the relying party's trust anchors merely by presenting them. Accepted bundles/trust domains must be established independently.

## Rotation

Consumers should tolerate normal credential/bundle rotation without silently changing durable application identity or authority. Test current SVID retrieval, source updates, bundle changes, peer verification after rotation, stale material, and outage behavior.
