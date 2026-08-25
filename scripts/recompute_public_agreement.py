#!/usr/bin/env python3
"""Recompute exact pass agreement from the public derivative records."""

from __future__ import annotations

import csv
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
VARIABLES = ("primary_tier", "T1", "T2", "T3", "T4")


def load(pass_number: int) -> dict[str, dict]:
    records = {}
    directory = PACKAGE / "data" / f"pass_{pass_number}" / "public_records"
    for path in sorted(directory.glob("S*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        records[data["study_id"]] = data
    return records


def label(record: dict, variable: str) -> str:
    if variable == "primary_tier":
        return record["primary_tier"]["code"]
    return record["roles"][variable]["decision"]


def main() -> int:
    pass_1 = load(1)
    pass_2 = load(2)
    if set(pass_1) != set(pass_2) or len(pass_1) != 112:
        raise ValueError("The public passes must contain the same 112 Study IDs")

    results = {}
    for variable in VARIABLES:
        left = [label(pass_1[study_id], variable) for study_id in sorted(pass_1)]
        right = [label(pass_2[study_id], variable) for study_id in sorted(pass_1)]
        matches = sum(a == b for a, b in zip(left, right))
        results[variable] = {
            "matches": matches,
            "total": len(left),
            "exact_percent": round(100 * matches / len(left), 1),
        }

    with (PACKAGE / "data" / "agreement" / "agreement_metrics.csv").open(
        newline="", encoding="utf-8-sig"
    ) as handle:
        released = {row["variable"]: row for row in csv.DictReader(handle)}
    mismatches = []
    for variable, result in results.items():
        row = released[variable]
        if int(row["matches"]) != result["matches"] or float(row["exact_percent"]) != result["exact_percent"]:
            mismatches.append(variable)

    print(json.dumps({"recomputed": results, "released_metric_mismatches": mismatches}, indent=2))
    return 1 if mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())