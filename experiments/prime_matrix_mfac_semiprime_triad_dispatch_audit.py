#!/usr/bin/env python3
"""审计 MFAC 半素数三项 global payload 的 actual dispatch 证据。

用法示例：
  python3 experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit.py
"""

from __future__ import annotations

import math
from typing import Any

from prime_matrix_mfac_colored_divisor_word_transport_audit import (
    build_colored_record,
    is_prime,
    source_payload,
)


REQUIRED_DISPATCH_FIELDS = (
    "pre_cauchy",
    "independent_of_downstream",
    "origin_selector",
    "actual_emitter_registered",
    "row_key",
    "orientation",
    "local_factor",
    "prepushforward_identity",
)


def build_semiprime_triad(p: int, q: int) -> list[dict[str, Any]]:
    """构造 `p<q` 对应的三项非零 Möbius global payload。"""
    if not is_prime(p) or not is_prime(q) or p >= q:
        raise ValueError("p、q 必须是满足 p<q 的素数")
    value = p * q
    entries: list[dict[str, Any]] = []
    for divisor in (p, q, value):
        record = build_colored_record(value, divisor)
        entries.append(
            {
                "divisor": divisor,
                "cofactor": value // divisor,
                "global_payload": source_payload(record),
            }
        )
    return entries


def audit_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """检查每个 triad 项是否携带完整的前向 dispatch 字段。"""
    audited: list[dict[str, Any]] = []
    for entry in entries:
        missing_fields = [
            field for field in REQUIRED_DISPATCH_FIELDS if not entry.get(field)
        ]
        audited.append(
            {
                **entry,
                "missing_fields": missing_fields,
                "admissible": not missing_fields,
            }
        )
    return audited


def audit_triad_dispatch(dispatch: dict[str, Any]) -> dict[str, Any]:
    """判定 triad 是 actual dispatch、canonical collapse 还是字段缺失。"""
    entries_value = dispatch.get("entries")
    if not isinstance(entries_value, list) or len(entries_value) != 3:
        raise ValueError("dispatch 必须包含恰好三条 triad entries")
    entries = audit_entries(entries_value)
    same_row = len({entry.get("row_key") for entry in entries}) == 1
    zero_sum = math.isclose(
        sum(float(entry["global_payload"]) for entry in entries),
        0.0,
        abs_tol=1e-12,
    )
    actual_dispatch = all(entry["admissible"] for entry in entries) and any(
        entry.get("source_class") == "actual_noncanonical" for entry in entries
    )
    return {
        "entries": entries,
        "global_payload_zero_sum": zero_sum,
        "canonical_zero_sum_collapse": same_row and zero_sum and not actual_dispatch,
        "actual_dispatch_present": actual_dispatch,
    }


def complete_synthetic_dispatch() -> dict[str, Any]:
    """返回完整、前向且非同-row 的合成 actual dispatch。"""
    entries = build_semiprime_triad(2, 3)
    for index, entry in enumerate(entries):
        entry.update(
            {
                "pre_cauchy": True,
                "independent_of_downstream": True,
                "origin_selector": f"synthetic-origin-{index}",
                "actual_emitter_registered": True,
                "row_key": f"synthetic-row-{index}",
                "orientation": 1 if index != 1 else -1,
                "local_factor": 1.0,
                "prepushforward_identity": True,
                "source_class": "actual_noncanonical",
            }
        )
    return {"entries": entries}


def same_row_zero_sum_dispatch() -> dict[str, Any]:
    """返回完整但被 canonical 同-row 合并的合成三项。"""
    entries = build_semiprime_triad(2, 3)
    for entry in entries:
        entry.update(
            {
                "pre_cauchy": True,
                "independent_of_downstream": True,
                "origin_selector": "canonical-lpf-selector",
                "actual_emitter_registered": True,
                "row_key": "canonical-lpf-row-2",
                "orientation": 1,
                "local_factor": 1.0,
                "prepushforward_identity": True,
                "source_class": "canonical",
            }
        )
    return {"entries": entries}
