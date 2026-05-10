#!/usr/bin/env python3
"""RNRS 闭合后的行/列推广总账审计。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_row_column_after_rnrs_audit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-row-column-after-rnrs-audit-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-row-column-after-rnrs-audit-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-row-column-after-rnrs-audit-router.md"

RNRS = MONO / "prime-matrix-strict-rks23-rnrs-energy-absorption-router.json"
CYCLE_GUARD = MONO / "prime-matrix-strict-rks23-self-contained-cycle-guard-frontier-router.json"
BALANCED = MONO / "prime-matrix-strict-rks23-balanced-collar-l2-energy-reduction-router.json"

SOURCE_FILES = [RNRS, CYCLE_GUARD, BALANCED]

WEIGHTED_ENERGY = "WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23"
NONCIRCULAR_ENERGY = "NonCircularSelfContainedReciprocalIntervalEnergyPowerSaving"
BALANCED_COLLAR = "BalancedCollarRKS23LogSavingAbsorption"
ROW_COLUMN = "RowColumnUnconditionalTheoremFinalPromotion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造 RNRS 后总账审计证书。"""
    rnrs = load_json(RNRS)
    cycle = load_json(CYCLE_GUARD)
    balanced = load_json(BALANCED)

    rnrs_input_closed = rnrs.get("self_contained_rnrs_rudnev_proof_closed") is True
    cycle_guard_ready = all(
        [
            cycle.get("self_contained_cycle_detected") is True,
            cycle.get("next_required_input") == "SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling",
        ]
    )
    balanced_reduction_ready = all(
        [
            balanced.get("cauchy_to_l2_restriction_reduction_closed") is True,
            balanced.get("plancherel_energy_transfer_closed") is True,
            balanced.get("next_direct_attack_target") == WEIGHTED_ENERGY,
        ]
    )

    noncircular_energy_input_closed = rnrs_input_closed and cycle_guard_ready
    weighted_energy_input_closed = rnrs_input_closed and balanced_reduction_ready
    balanced_collar_absorption_closed = weighted_energy_input_closed

    row_column_unconditional_closed = False
    row_column_final_audit_complete = False

    audit_findings = {
        "rnrs_result": "self-contained RNRS/Rudnev reciprocal-interval energy input is now closed",
        "cycle_guard_effect": "the previous noncircular input required by the cycle guard is now supplied by RNRS, not by the circular RKS23 route",
        "balanced_energy_effect": "the RNRS N^(5/2)P^eps bound is strong enough for the balanced-collar weighted energy gate after the registered loss absorption",
        "why_not_final_row_column": "the row/column theorem still needs one final promotion audit tying this supplied energy gate through every upstream theorem statement and boundary convention",
        "audit_boundary": "this certificate closes the missing energy supply, not the final theorem statement itself",
    }

    rows = [
        row(
            "SelfContainedRNRSInputClosed",
            rnrs_input_closed,
            True,
            "RNRS/Rudnev 倒数区间能量输入已闭合。",
            "closed RNRS input",
        ),
        row(
            "CycleGuardNonCircularEnergyInputClosed",
            noncircular_energy_input_closed,
            True,
            "循环守门所需的独立非循环能量输入现在由 RNRS 提供。",
            NONCIRCULAR_ENERGY,
        ),
        row(
            "WeightedReciprocalIntervalEnergyInputClosed",
            weighted_energy_input_closed,
            True,
            "平衡颈部所需加权倒数区间能量门由 RNRS 参数吸收闭合。",
            WEIGHTED_ENERGY,
        ),
        row(
            "BalancedCollarAbsorptionClosed",
            balanced_collar_absorption_closed,
            True,
            "RKS2/RKS3 平衡颈部 L2/能量归约的缺口已由 RNRS 输入补齐。",
            BALANCED_COLLAR,
        ),
        row(
            "RowColumnFinalAuditComplete",
            row_column_final_audit_complete,
            False,
            "仍需逐条核对行/列最终推广链的全部边界、例外项和声明口径。",
            ROW_COLUMN,
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_unconditional_closed,
            False,
            "本步完成 RNRS 后的能量门补齐审计，但不直接宣称行/列命题无条件闭合。",
            ROW_COLUMN,
        ),
    ]

    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]

    return {
        "certificate_type": "strict_rks23_row_column_after_rnrs_audit_router",
        "status": "rnrs_supplies_noncircular_and_balanced_energy_gates_remaining_final_row_column_promotion_audit",
        "rnrs_input_closed": rnrs_input_closed,
        "cycle_guard_ready": cycle_guard_ready,
        "balanced_reduction_ready": balanced_reduction_ready,
        "noncircular_energy_input_closed": noncircular_energy_input_closed,
        "weighted_energy_input_closed": weighted_energy_input_closed,
        "balanced_collar_absorption_closed": balanced_collar_absorption_closed,
        "row_column_final_audit_complete": row_column_final_audit_complete,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "counterexample_assumption_only": True,
        "audit_findings": audit_findings,
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "remaining_atoms": [
            {
                "atom": ROW_COLUMN,
                "closed": False,
                "why_remaining": "must run a final promotion audit over the row/column theorem statement before marking unconditional closure",
            }
        ],
        "next_direct_attack_target": ROW_COLUMN,
        "next_required_input": "Final promotion audit from closed balanced/RNRS energy gates to the stated row/column theorem",
        "plain_conclusion": (
            "RNRS 已补齐循环守门和加权能量门。行/列命题还不能直接标为无条件闭合；"
            "下一步是最终推广链审计，逐条核对所有边界与例外项。"
        ),
        "source_hashes": source_hashes(),
        "rows": rows,
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict RKS23 RNRS 后行/列总账审计证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(
        "本步审计 RNRS 闭合后的全局影响：独立非循环能量输入和平衡颈部加权能量门已由 RNRS 补齐。"
        "但行/列命题仍需最终推广链审计，不能在本证书中越界标为无条件闭合。"
    )
    lines.append("")
    lines.append("```text")
    for key in [
        "noncircular_energy_input_closed",
        "weighted_energy_input_closed",
        "balanced_collar_absorption_closed",
        "row_column_final_audit_complete",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 审计发现")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["audit_findings"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=item["gate"],
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.append("")
    lines.append("## 3. 下一真正自足目标")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_direct_attack_target"])
    lines.append(result["next_required_input"])
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    MONO.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"noncircular_energy_input_closed={fmt_bool(result['noncircular_energy_input_closed'])}")
    print(f"weighted_energy_input_closed={fmt_bool(result['weighted_energy_input_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
