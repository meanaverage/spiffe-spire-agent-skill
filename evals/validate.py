#!/usr/bin/env python3
"""Validate the checked-in skill evaluation corpus without external dependencies."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORPUS = ROOT / "upstream-v1.15.3.json"
REQUIRED_SCENARIO_KEYS = {"id", "prompt", "expected", "must_not", "authority", "version"}


def main() -> None:
    data = json.loads(CORPUS.read_text(encoding="utf-8"))
    assert data["schema"] == "spiffe-spire-agent-skill-evals/v0"
    assert isinstance(data["scenarios"], list) and data["scenarios"]

    ids: set[str] = set()
    for index, scenario in enumerate(data["scenarios"]):
        missing = REQUIRED_SCENARIO_KEYS - scenario.keys()
        assert not missing, f"scenario {index} missing keys: {sorted(missing)}"
        scenario_id = scenario["id"]
        assert isinstance(scenario_id, str) and scenario_id
        assert scenario_id not in ids, f"duplicate scenario id: {scenario_id}"
        ids.add(scenario_id)
        assert isinstance(scenario["prompt"], str) and scenario["prompt"].strip()
        assert isinstance(scenario["authority"], str) and scenario["authority"].strip()
        assert isinstance(scenario["version"], str) and scenario["version"].strip()
        for key in ("expected", "must_not"):
            assert isinstance(scenario[key], list)
            assert all(isinstance(item, str) and item.strip() for item in scenario[key])
        assert scenario["expected"], f"scenario {scenario_id} has no expected conclusions"

    print(f"validated {len(ids)} scenarios from {CORPUS.name}")


if __name__ == "__main__":
    main()
