# Operational principles

## Observe before mutate

Prefer read-only inspection of process/service state, socket permissions, SPIRE inventory, registration entries, Workload API availability, bundle/SVID metadata, and exact versions.

## Establish ownership of the failing boundary

Separate transport, server, agent, node attestation, workload selection, registration, Workload API client, credential verification, TLS peer authentication, application authorization, and application effects.

## Health is evidence-specific

Process existence does not prove attestation, Workload API readiness, SVID availability, bundle freshness, or authenticated application connectivity.

## Identity is not authority

A valid SPIFFE identity does not automatically establish application role, resource ownership, tenancy, deployment authority, work authority, or effect authority.

## Fail closed without erasing diagnosis

Avoid widening trust; retain bounded diagnostic classification; distinguish absent/unavailable/invalid/unknown; do not claim partial success without evidence.

## Recovery

Before destructive or credential-changing recovery, identify rollback state, bind recovery to exact intended subjects/resources, prevent unrelated inventory adoption, verify recovered state independently, and distinguish recovery of SPIRE credentials from recovery of application authority.
