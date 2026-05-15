#!/usr/bin/env python3
"""审计 z=61 固定核心闭环与已有无循环/持久相位输入的匹配边界。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_fixed_core_cycle_nonpersistence_comparator.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-nonpersistence-comparator.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-nonpersistence-comparator.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-nonpersistence-comparator.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-nonpersistence-comparator.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-nonpersistence-comparator.md"

SOURCES = {
    "cycle": "prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-ledger-router.json",
    "prefix_persistence": "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json",
    "common_kernel_no_free_cycle": "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
    "source_loop_cut": "prime-matrix-clean-core-source-loop-cut-router.json",
    "true_structure_cycle_cut": "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
}

NEXT_TARGET = "PrefixGateSignedPhaseBalanceOrPersistentPhasePDECExclusion"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads((DOCS / name).read_text(encoding="utf-8"))


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_fixed_core_cycle_nonpersistence_comparator.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for file_name in SOURCES.values():
        result[f"docs/monograph/{file_name}"] = file_sha256(DOCS / file_name)
    return result


def audit() -> dict[str, Any]:
    """执行非持久性匹配审查。"""
    cycle = load(SOURCES["cycle"])
    prefix = load(SOURCES["prefix_persistence"])
    no_free = load(SOURCES["common_kernel_no_free_cycle"])
    source_loop = load(SOURCES["source_loop_cut"])
    true_cut = load(SOURCES["true_structure_cycle_cut"])

    # 旧无循环材料只能排除“免费且无名”的回流；当前对象已经有固定相位名和样本命中。
    generic_no_cycle_imported = bool(no_free["free_common_kernel_return_cycle_excluded"])
    persistent_phase_materialized = (
        prefix["phase_condition"] == "b ≡ 0 (mod 28842)"
        and prefix["phase_hit_total_multiplicity"] == 3
        and prefix["phase_hits_by_sign"] == {"negative": 1, "positive": 2, "zero": 0}
        and abs(prefix["positive_over_negative_phase_actual"] - 2.0) < 1e-12
    )
    fixed_core_cycle_named = (
        cycle["z61_fixed_core_cycle_ledger_closed_for_formal_unit"]
        and cycle["core"] == 4807
        and cycle["modulus"] == 57684
        and cycle["selected_carry"] == 6
        and cycle["selected_original_sign_word"] == "--++-"
        and persistent_phase_materialized
    )
    old_no_cycle_insufficient = (
        generic_no_cycle_imported
        and no_free["named_return_exclusion_proved"] is False
        and no_free["unified_terminal_budget_strict_inequality_proved"] is False
        and fixed_core_cycle_named
    )
    direct_short_return_not_available = true_cut["early_zero_forces_stable_short_return_or_defect_proved"] is False
    source_loop_not_a_proof = source_loop["source_loop_cut_closed"] and not source_loop[
        "acyclic_pre_cauchy_source_seed_proved"
    ]

    obligations = [
        {
            "name": "PrefixGateSignedPhaseBalance",
            "closed": False,
            "why_needed": (
                "固定相位 `b≡0 mod 28842` 已持久出现；必须证明正侧 quotient 2,4 "
                "全局伴随并吸收负侧 quotient 1。"
            ),
        },
        {
            "name": "PersistentPhasePDECExclusion",
            "closed": False,
            "why_needed": "若 signed balance 不能全局证明，就要排斥这个命名持久相位 PDEC。",
        },
        {
            "name": "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect",
            "closed": False,
            "why_needed": (
                "若要直接从早期零行反例链撞出矛盾，还必须证明短稳定同标签复现或相位缺陷登记。"
            ),
        },
    ]

    comparator_closed = fixed_core_cycle_named and old_no_cycle_insufficient and source_loop_not_a_proof

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_fixed_core_cycle_nonpersistence_comparator",
        "status": "z61_fixed_core_cycle_requires_named_persistent_phase_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_bucket": cycle["target_bucket"],
        "target_omega": cycle["target_omega"],
        "target_shell": cycle["target_shell"],
        "core": cycle["core"],
        "modulus": cycle["modulus"],
        "phase_condition": prefix["phase_condition"],
        "phase_hit_total_multiplicity": prefix["phase_hit_total_multiplicity"],
        "phase_hits_by_sign": prefix["phase_hits_by_sign"],
        "positive_over_negative_phase_actual": prefix["positive_over_negative_phase_actual"],
        "generic_no_free_cycle_imported": generic_no_cycle_imported,
        "fixed_core_cycle_named_persistent_phase_materialized": fixed_core_cycle_named,
        "generic_no_free_cycle_does_not_exclude_named_persistent_phase": old_no_cycle_insufficient,
        "source_loop_cut_imported_but_not_seed_proof": source_loop_not_a_proof,
        "direct_short_return_contradiction_input_available": not direct_short_return_not_available,
        "fixed_core_cycle_nonpersistence_comparator_closed": comparator_closed,
        "prefix_gate_signed_phase_balance_proved": False,
        "persistent_phase_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "remaining_obligations": obligations,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "已有通用无循环输入可以排除免费无名回流，但不能排除当前 z=61 固定核心闭环，"
            "因为该闭环已经登记为命名持久相位 `b≡0 mod 28842`，且样本中负侧一次、正侧两次。"
            "因此当前最窄剩余不是继续重跑局部闭环，而是证明 PrefixGate signed phase balance "
            "全局成立，或排斥 PersistentPhase-PDEC；直接短复现矛盾仍缺 "
            "`StableShortSameLabelRecurrenceOrRegisteredPhaseDefect` 输入。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 fixed-core cycle nonpersistence comparator",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fixed_core_cycle_named_persistent_phase_materialized={fmt_bool(result['fixed_core_cycle_named_persistent_phase_materialized'])}",
        f"generic_no_free_cycle_does_not_exclude_named_persistent_phase={fmt_bool(result['generic_no_free_cycle_does_not_exclude_named_persistent_phase'])}",
        f"prefix_gate_signed_phase_balance_proved={fmt_bool(result['prefix_gate_signed_phase_balance_proved'])}",
        f"persistent_phase_pdec_excluded={fmt_bool(result['persistent_phase_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 匹配结论",
        "",
        "| check | value |",
        "| --- | --- |",
        f"| target | `{result['target_bucket']}, omega={result['target_omega']}, shell={result['target_shell']}` |",
        f"| core/M | `{result['core']} / {result['modulus']}` |",
        f"| phase | `{result['phase_condition']}` |",
        f"| phase hits by sign | `{result['phase_hits_by_sign']}` |",
        f"| positive/negative phase actual | `{result['positive_over_negative_phase_actual']:.6f}` |",
        f"| generic no-free cycle imported | {fmt_bool(result['generic_no_free_cycle_imported'])} |",
        f"| generic no-cycle sufficient here | {fmt_bool(not result['generic_no_free_cycle_does_not_exclude_named_persistent_phase'])} |",
        f"| direct short-return input available | {fmt_bool(result['direct_short_return_contradiction_input_available'])} |",
        "",
        "## 2. 剩余义务",
        "",
        "| obligation | closed | why needed |",
        "| --- | --- | --- |",
    ]
    for item in result["remaining_obligations"]:
        lines.append(f"| `{item['name']}` | {fmt_bool(item['closed'])} | {item['why_needed']} |")
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：旧无循环输入与当前固定核心闭环的适用边界已明确。",
            "- 未闭合：PrefixGate signed phase balance 或 PersistentPhase-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
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
                "fixed_core_cycle_named_persistent_phase_materialized": result[
                    "fixed_core_cycle_named_persistent_phase_materialized"
                ],
                "generic_no_free_cycle_does_not_exclude_named_persistent_phase": result[
                    "generic_no_free_cycle_does_not_exclude_named_persistent_phase"
                ],
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
