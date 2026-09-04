#!/usr/bin/env python3
"""Validate all checked-in skill evaluation corpora without external dependencies."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORPORA = (ROOT / "upstream-v1.15.3.json", ROOT / "historical-generalized-v0.json")
REQUIRED_SCENARIO_KEYS = {"id", "prompt", "expected", "must_not", "authority", "version"}


def main() -> None:
    all_ids: set[str] = set()
    total = 0
    for corpus in CORPORA:
        data = json.loads(corpus.read_text(encoding="utf-8"))
        assert data["schema"] == "spiffe-spire-agent-skill-evals/v0"
        assert isinstance(data["scenarios"], list) and data["scenarios"]

        local_ids: set[str] = set()
        for index, scenario in enumerate(data["scenarios"]):
            missing = REQUIRED_SCENARIO_KEYS - scenario.keys()
            assert not missing, f"{corpus.name} scenario {index} missing keys: {sorted(missing)}"
            scenario_id = scenario["id"]
            assert isinstance(scenario_id, str) and scenario_id
            assert scenario_id not in local_ids, f"duplicate scenario id in {corpus.name}: {scenario_id}"
            assert scenario_id not in all_ids, f"duplicate scenario id across corpora: {scenario_id}"
            local_ids.add(scenario_id)
            all_ids.add(scenario_id)
            assert isinstance(scenario["prompt"], str) and scenario["prompt"].strip()
            assert isinstance(scenario["authority"], str) and scenario["authority"].strip()
            assert isinstance(scenario["version"], str) and scenario["version"].strip()
            for key in ("expected", "must_not"):
                assert isinstance(scenario[key], list)
                assert all(isinstance(item, str) and item.strip() for item in scenario[key])
            assert scenario["expected"], f"scenario {scenario_id} has no expected conclusions"
        total += len(local_ids)
        print(f"validated {len(local_ids)} scenarios from {corpus.name}")

    print(f"validated {total} scenarios across {len(CORPORA)} corpora")


if __name__ == "__main__":
    main()
