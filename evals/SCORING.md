# Evaluation scoring rubric

Score each scenario from 0–2 on four dimensions, for a maximum of 8 points.

## 1. Semantic correctness

- **2** — reaches all material expected conclusions without contradiction.
- **1** — directionally correct but misses a material lifecycle/security distinction.
- **0** — materially wrong or recommends an unsafe semantic conclusion.

## 2. Authority correctness

- **2** — identifies the appropriate source class and exact version/path when the scenario supplies one.
- **1** — cites a credible upstream source but loses version/path specificity.
- **0** — relies on community/generic advice when authoritative upstream evidence is available, or invents evidence.

## 3. Boundary correctness

- **2** — correctly separates SPIFFE/SPIRE/client behavior from deployment integration and application policy.
- **1** — conclusion is safe but the ownership boundary is vague.
- **0** — attributes application authorization/effect semantics to SPIFFE/SPIRE or otherwise crosses the boundary materially.

## 4. False-positive discipline

- **2** — avoids every `must_not` conclusion and clearly labels uncertainty.
- **1** — no dangerous conclusion, but contains unsupported speculation or overstatement.
- **0** — asserts a forbidden/unsupported conclusion or recommends weakening trust/verification without evidence.

## Suggested aggregate interpretation

- **7–8** — strong
- **5–6** — usable but needs review
- **3–4** — weak
- **0–2** — unsafe/unreliable for the scenario

Do not treat aggregate score as a security certification. Preserve per-dimension scores so improvements in recall cannot hide regressions in false-positive discipline.
