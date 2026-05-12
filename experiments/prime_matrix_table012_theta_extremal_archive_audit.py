#!/usr/bin/env python3
"""审计 strict table_012 theta 极值归档。

用法示例：
  python3 experiments/prime_matrix_table012_theta_extremal_archive_audit.py \
    --archive data/theta-table012-extremal-archive.jsonl

  python3 experiments/prime_matrix_table012_theta_extremal_archive_audit.py \
    --archive data/theta-table012-extremal-sample-first-row.jsonl \
    --allow-prefix --expected-rows 1
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 80

TABLE012 = [
    ("1E+08", 100_000_000, 200_000_000, Decimal("-0.00044")),
    ("2E+08", 200_000_000, 300_000_000, Decimal("-0.00065")),
    ("3E+08", 300_000_000, 400_000_000, Decimal("-0.00057")),
    ("4E+08", 400_000_000, 500_000_000, Decimal("-0.00049")),
    ("5E+08", 500_000_000, 600_000_000, Decimal("-0.00052")),
    ("6E+08", 600_000_000, 700_000_000, Decimal("-0.00038")),
    ("7E+08", 700_000_000, 800_000_000, Decimal("-0.00051")),
    ("8E+08", 800_000_000, 900_000_000, Decimal("-0.00044")),
    ("9E+08", 900_000_000, 1_000_000_000, Decimal("-0.00050")),
    ("1E+09", 1_000_000_000, 2_000_000_000, Decimal("-0.00021")),
    ("2E+09", 2_000_000_000, 3_000_000_000, Decimal("-0.00018")),
    ("3E+09", 3_000_000_000, 4_000_000_000, Decimal("-0.00015")),
    ("4E+09", 4_000_000_000, 5_000_000_000, Decimal("-0.00017")),
    ("5E+09", 5_000_000_000, 6_000_000_000, Decimal("-0.00018")),
    ("6E+09", 6_000_000_000, 7_000_000_000, Decimal("-0.00013")),
    ("7E+09", 7_000_000_000, 8_000_000_000, Decimal("-0.00018")),
    ("8E+09", 8_000_000_000, 9_000_000_000, Decimal("-0.00016")),
    ("9E+09", 9_000_000_000, 10_000_000_000, Decimal("-0.00010")),
    ("1E+10", 10_000_000_000, 20_000_000_000, Decimal("-0.00008")),
    ("2E+10", 20_000_000_000, 30_000_000_000, Decimal("-0.00006")),
    ("3E+10", 30_000_000_000, 40_000_000_000, Decimal("-0.00005")),
    ("4E+10", 40_000_000_000, 50_000_000_000, Decimal("-0.00007")),
    ("5E+10", 50_000_000_000, 60_000_000_000, Decimal("-0.00004")),
    ("6E+10", 60_000_000_000, 70_000_000_000, Decimal("-0.00006")),
    ("7E+10", 70_000_000_000, 80_000_000_000, Decimal("-0.00004")),
    ("8E+10", 80_000_000_000, 90_000_000_000, Decimal("-0.00006")),
    ("9E+10", 90_000_000_000, 100_000_000_000, Decimal("-0.00004")),
    ("1E+11", 100_000_000_000, 200_000_000_000, Decimal("-0.00002")),
    ("2E+11", 200_000_000_000, 300_000_000_000, Decimal("-0.00002")),
    ("3E+11", 300_000_000_000, 400_000_000_000, Decimal("-0.00001")),
    ("4E+11", 400_000_000_000, 500_000_000_000, Decimal("-0.00002")),
    ("5E+11", 500_000_000_000, 600_000_000_000, Decimal("-0.00001")),
    ("6E+11", 600_000_000_000, 700_000_000_000, Decimal("-0.00002")),
    ("7E+11", 700_000_000_000, 800_000_000_000, Decimal("-0.00001")),
]


def sha256(path: Path) -> str:
    """计算原始字节 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def iter_jsonl(path: Path):
    """逐行读取 JSONL。"""
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            stripped = line.strip()
            if stripped:
                yield line_no, json.loads(stripped)


def dec(record: dict[str, Any], key: str) -> Decimal:
    """读取十进制字段。"""
    return Decimal(str(record[key]))


def audit_archive(
    path: Path,
    expected_rows: int,
    allow_prefix: bool,
    expect_hash: str | None,
) -> dict[str, Any]:
    """审计归档行数、连续区间、余量和 hash。"""
    errors: list[str] = []
    rows: list[dict[str, Any]] = []
    min_raw_margin: Decimal | None = None
    min_guard_margin: Decimal | None = None
    min_raw_label: str | None = None
    min_guard_label: str | None = None

    for line_no, record in iter_jsonl(path):
        idx = len(rows)
        if idx >= len(TABLE012):
            errors.append(f"line {line_no}: too many rows")
            continue
        expected = TABLE012[idx]
        label, left, right, b1 = expected
        for key, expected_value in [
            ("label", label),
            ("left", left),
            ("right", right),
        ]:
            if record.get(key) != expected_value:
                errors.append(f"line {line_no}: {key}={record.get(key)!r}, expected {expected_value!r}")
        if dec(record, "b1") != b1:
            errors.append(f"line {line_no}: b1={record.get('b1')}, expected {b1}")
        if record.get("max_kind") not in {"left_endpoint", "prime_jump"}:
            errors.append(f"line {line_no}: unexpected max_kind={record.get('max_kind')!r}")
        max_x = int(record["max_x"])
        if not (left <= max_x <= right):
            errors.append(f"line {line_no}: max_x={max_x} outside [{left},{right}]")
        if record.get("passed_raw") is not True:
            errors.append(f"line {line_no}: passed_raw is not true")
        if record.get("passed_with_guard") is not True:
            errors.append(f"line {line_no}: passed_with_guard is not true")

        raw_margin = dec(record, "raw_margin")
        guard_margin = dec(record, "margin_after_guard")
        b1_margin = dec(record, "b1_minus_max_required_b1")
        deriv_lb = dec(record, "rhs_derivative_lower_bound")
        if raw_margin <= 0:
            errors.append(f"line {line_no}: raw margin is not positive")
        if guard_margin <= 0:
            errors.append(f"line {line_no}: guard margin is not positive")
        if b1_margin <= 0:
            errors.append(f"line {line_no}: b1 margin is not positive")
        if deriv_lb <= Decimal("0.99"):
            errors.append(f"line {line_no}: derivative lower bound unexpectedly small")

        if min_raw_margin is None or raw_margin < min_raw_margin:
            min_raw_margin = raw_margin
            min_raw_label = label
        if min_guard_margin is None or guard_margin < min_guard_margin:
            min_guard_margin = guard_margin
            min_guard_label = label

        rows.append(record)

    actual_rows = len(rows)
    if allow_prefix:
        if actual_rows != expected_rows:
            errors.append(f"row count {actual_rows}, expected prefix {expected_rows}")
    elif actual_rows != len(TABLE012):
        errors.append(f"row count {actual_rows}, expected {len(TABLE012)}")

    file_hash = sha256(path)
    if expect_hash is not None and file_hash != expect_hash:
        errors.append(f"sha256 mismatch: {file_hash} != {expect_hash}")

    return {
        "archive": str(path),
        "sha256": file_hash,
        "expect_hash": expect_hash,
        "passed": not errors,
        "errors": errors[:50],
        "error_count": len(errors),
        "row_count": actual_rows,
        "expected_rows": expected_rows if allow_prefix else len(TABLE012),
        "allow_prefix": allow_prefix,
        "min_raw_margin": str(min_raw_margin) if min_raw_margin is not None else None,
        "min_raw_margin_label": min_raw_label,
        "min_guard_margin": str(min_guard_margin) if min_guard_margin is not None else None,
        "min_guard_margin_label": min_guard_label,
        "first_row": rows[0] if rows else None,
        "last_row": rows[-1] if rows else None,
    }


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True, help="待审计的 JSONL 归档")
    parser.add_argument("--expect-hash", default=None, help="可选预期 SHA256")
    parser.add_argument("--allow-prefix", action="store_true", help="允许只审计前缀样本")
    parser.add_argument("--expected-rows", type=int, default=len(TABLE012), help="前缀样本行数")
    args = parser.parse_args()

    result = audit_archive(args.archive, args.expected_rows, args.allow_prefix, args.expect_hash)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
