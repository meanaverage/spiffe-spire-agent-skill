# SVID rotation and trust bundles

Use this reference for X.509-SVID refresh, bundle refresh, CA rotation, stale credentials, trust-domain handling, and long-lived SPIFFE-aware clients.

## Prefer a source abstraction

Maintained SPIFFE clients commonly expose a source that follows Workload API updates rather than requiring applications to manually re-fetch and reconstruct credentials.

For the included go-spiffe/v2 v2.8.1 reference baseline, `workloadapi.X509Source` maintains the current X.509-SVID and X.509 bundle set, blocks until its initial Workload API update, exposes update notification/waiting, and supplies bundles by trust domain.

Before implementing custom polling, certificate parsing, refresh, or bundle caches, compare the required behavior against the exact selected client version.

## Rotation is ordinary operation

Do not design credential rotation as an exceptional migration event.

For SPIRE v1.15.3, the tagged `rotation` integration suite deliberately uses low TTLs and repeatedly retrieves valid workload SVIDs across SVID and SPIRE-server CA rotation periods.

Application tests should distinguish:

- SVID leaf rotation;
- signing/CA authority rotation;
- bundle-set updates;
- connection behavior across updates;
- stale cached material;
- Workload API outage;
- application-specific durable identity/authorization.

## Trust is relying-party state

A peer presenting a certificate chain does not grant the peer authority to select the relying party's accepted trust anchors.

Check:

- where accepted trust domains come from;
- where bundles come from;
- whether the bundle source is authenticated/independently configured;
- whether peer-provided material can replace or widen accepted trust;
- whether bootstrap/enrollment material is being mistaken for current trust state.

## Rotation review questions

- Can the client receive an updated SVID without restart?
- Can the client receive updated bundles without restart?
- Are old and new connections handled intentionally during rotation?
- Does the application cache a certificate, key, or bundle longer than the source contract permits?
- Does credential rotation accidentally change a durable application binding or authorization decision?
- Does a temporary Workload API outage cause unsafe fallback or only bounded unavailability?
- Are stale SVIDs/bundles rejected according to the actual TLS/client semantics?
- Does a health check prove current credential usability rather than merely process existence?

## Testing ladder

Use upstream/client tests for ordinary rotation semantics, local integration for exact application-client compatibility, and VM/system tests only for environment-specific effects such as service-manager reload behavior, filesystem/socket custody, network isolation, and rollback.