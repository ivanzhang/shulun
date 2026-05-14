#!/usr/bin/env python3
"""登记 z=61 prefix gate 分支的 PDEC 证书对象。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_pdec_registration_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PREFIX_GATE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-common-core-prefix-gate-router.json"
COMMON_CORE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json"
OVERLAP_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.md"

NEXT_TARGET = "PrefixGatePDECExclusionOrGlobalPrefixGateCapacityBound"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-common-core-prefix-gate-router.json",
    "prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json",
    "prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.json",
]


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_pdec_registration_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """登记 PrefixGate-PDEC 对象。"""
    prefix_gate = json.loads(PREFIX_GATE_JSON.read_text(encoding="utf-8"))
    common_core = json.loads(COMMON_CORE_JSON.read_text(encoding="utf-8"))
    overlap = json.loads(OVERLAP_JSON.read_text(encoding="utf-8"))
    flip_row = next(row for row in overlap["scale_rows"] if row["overlap_flips_drift_sign"])
    selected_splits = [
        {
            "core_split": row["core_split"],
            "selected_prefixes": row["selected_prefixes"],
            "selected_weight": row["selected_weight"],
            "prefix_interval": [row["prefix_lower_closed"], row["prefix_upper_open"]],
        }
        for row in prefix_gate["split_rows"]
        if row["selected_prefix_count"] > 0
    ]
    phase_modulus = common_core["b_value"]
    pdec_record = {
        "formal_unit_key": (
            "z61|bucket=unbalanced<=8|omega=4|p=36739|"
            f"C={common_core['common_core']}|b={common_core['b_value']}|prefixes=2,3"
        ),
        "p": common_core["overlap_p"],
        "b_value": common_core["b_value"],
        "phase_modulus": phase_modulus,
        "phase_residue": 0,
        "phase_condition": f"b ≡ 0 (mod {phase_modulus})",
        "common_core": common_core["common_core"],
        "common_core_factorization": common_core["common_core_factorization"],
        "hit_moduli": common_core["hit_moduli"],
        "prefixes": common_core["prefixes"],
        "selected_splits": selected_splits,
        "overlap_weight": common_core["overlap_contribution_from_moduli"],
        "needed_lift_to_reach_model_scale": flip_row["needed_lift_to_reach_model_scale"],
        "overlap_lift_surplus_over_model": flip_row["overlap_lift_surplus_over_model"],
        "full_drift_from_model": flip_row["full_drift_from_model"],
        "without_overlap_drift_from_model": flip_row["without_overlap_drift_from_model"],
    }
    upstream_closed = (
        prefix_gate["prefix_gate_identity_closed"]
        and common_core["two_three_common_core_identity_closed"]
        and overlap["single_double_hit_overlap_flip_identity_closed"]
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_prefix_gate_pdec_registration_router",
        "status": "z61_prefix_gate_pdec_registered_not_excluded",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            prefix_gate["certificate_type"],
            common_core["certificate_type"],
            overlap["certificate_type"],
        ],
        "prefix_gate_pdec_registration_closed": upstream_closed,
        "prefix_gate_pdec_record": pdec_record,
        "prefix_gate_pdec_excluded": False,
        "global_prefix_gate_capacity_bound_proved": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Prefix interval gate 分支已登记为具体 PDEC 对象：相位条件是 "
            f"`b≡0 mod {phase_modulus}`，对应 `C=4807` 的 `2C/3C` 同核双命中。"
            "该登记闭合的是失败对象的形式化与可审查性，不是排斥证明；"
            "下一步必须排斥该 PrefixGate-PDEC，或证明全局 prefix gate 容量界。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    record = result["prefix_gate_pdec_record"]
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 PrefixGate-PDEC 登记",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prefix_gate_pdec_registration_closed={fmt_bool(result['prefix_gate_pdec_registration_closed'])}",
        f"formal_unit_key={record['formal_unit_key']}",
        f"phase_condition={record['phase_condition']}",
        f"overlap_weight={fmt_float(record['overlap_weight'])}",
        f"needed_lift_to_reach_model_scale={fmt_float(record['needed_lift_to_reach_model_scale'])}",
        f"overlap_lift_surplus_over_model={fmt_float(record['overlap_lift_surplus_over_model'])}",
        f"prefix_gate_pdec_excluded={fmt_bool(result['prefix_gate_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. PDEC 对象",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| formal unit | `{record['formal_unit_key']}` |",
        f"| phase | `{record['phase_condition']}` |",
        f"| common core | `{record['common_core']}={record['common_core_factorization']}` |",
        f"| hit moduli | `{record['hit_moduli']}` |",
        f"| prefixes | `{record['prefixes']}` |",
        f"| selected splits | `{record['selected_splits']}` |",
        "",
        "## 2. 证明边界",
        "",
        "- 已闭合：PrefixGate-PDEC 失败对象登记。",
        "- 未闭合：该 PDEC 的排斥，或全局 prefix gate 容量界。",
        f"- 下一目标：`{result['next_direct_attack_target']}`。",
        "",
        "## 3. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "prefix_gate_pdec_registration_closed": result["prefix_gate_pdec_registration_closed"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
