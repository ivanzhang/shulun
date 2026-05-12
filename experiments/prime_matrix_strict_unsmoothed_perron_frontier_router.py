#!/usr/bin/env python3
"""生成 strict 非平滑 Perron 当前前沿路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_unsmoothed_perron_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-unsmoothed-perron-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-frontier-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-frontier-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-b3-unsmoothed-perron-formula-router.md",
    MONOGRAPH / "prime-matrix-b3-internal-psi0-perron-formula-router.md",
    MONOGRAPH / "prime-matrix-b3-perron-kernel-truncation-router.md",
    MONOGRAPH / "prime-matrix-b3-right-edge-perron-kernel-router.md",
    MONOGRAPH / "prime-matrix-b3-zeta-logder-contour-shift-router.md",
    MONOGRAPH / "prime-matrix-b3-psi0-horizontal-logder-bound-router.md",
    MONOGRAPH / "prime-matrix-strict-self-contained-mertens-tail-frontier-router.md",
]

TARGET = "UnsmoothedChebyshevPerronExplicitFormulaConstantLedger"
CONTOUR_SHIFT = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
HORIZONTAL_LOGDER = "Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger"
LOCAL_ZERO_DISTANCE = "Psi0HorizontalLocalZeroDistanceSumConstantLedger"
WEIGHTED_INTEGRAL = "Psi0HorizontalWeightedIntegralBudgetLedger"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
WHOLE_STRIP_EXTERNAL = "ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted"
GOOD_HEIGHT = "Psi0GoodHeightTStarAveragingContourShiftLedger"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def frontier_items() -> list[dict[str, str]]:
    """列出非平滑 Perron 前沿。"""
    return [
        {
            "name": "internal_psi0_exact_formula",
            "status": "closed",
            "meaning": "psi_0(x)=x-sum_rho x^rho/rho-log(2pi)-1/2 log(1-x^-2) 的无截断公式已闭合。",
            "remaining": "有限 T 截断余项。",
        },
        {
            "name": "right_edge_perron_kernel",
            "status": "closed",
            "meaning": "右边 Perron 核近似常数已闭合为 C_right=128，只支付核误差。",
            "remaining": CONTOUR_SHIFT,
        },
        {
            "name": "contour_shift",
            "status": "open",
            "meaning": "右边竖线积分移线到零点留数时，水平边 log-derivative 与近零缩进成本仍开放。",
            "remaining": f"{HORIZONTAL_LOGDER} AND ({BACKLUND_INTERNAL} OR {GOOD_HEIGHT})",
        },
        {
            "name": "horizontal_logder",
            "status": "open_structural_reduction",
            "meaning": "水平边 zeta'/zeta 已压成局部零点距离和、加权积分预算，或 whole-strip 外部显式匹配。",
            "remaining": f"self: {LOCAL_ZERO_DISTANCE} AND {WEIGHTED_INTEGRAL}; external: {WHOLE_STRIP_EXTERNAL} AND {WEIGHTED_INTEGRAL}",
        },
        {
            "name": "fixed_t_vs_good_height",
            "status": "choice_open",
            "meaning": "固定 T 需要 Backlund/缩进成本；若改用好高度 T*，必须更新当前 fixed-T 合同。",
            "remaining": f"{BACKLUND_INTERNAL} OR {GOOD_HEIGHT}",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "该前沿只服务自足 Mertens/PNT 输入，不使用真实零行缺席。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "Psi0ExactFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "内部 psi_0 精确公式已闭合，不再是当前硬点。",
            "remaining": "Finite-T truncation constants.",
        },
        {
            "gate": "RightEdgeKernelClosed",
            "closed": True,
            "proved": True,
            "meaning": "Perron 右边核近似常数已闭合为 C_right=128。",
            "remaining": CONTOUR_SHIFT,
        },
        {
            "gate": "ContourShiftOpen",
            "closed": False,
            "proved": False,
            "meaning": "zeta 对数导数轮廓移线尚未闭合。",
            "remaining": f"{HORIZONTAL_LOGDER} AND ({BACKLUND_INTERNAL} OR {GOOD_HEIGHT})",
        },
        {
            "gate": "HorizontalLogderOpen",
            "closed": False,
            "proved": False,
            "meaning": "水平边 away-from-zero 上界需要内部局部零点距离和/加权积分，或外部 whole-strip 严格匹配。",
            "remaining": f"{LOCAL_ZERO_DISTANCE} AND {WEIGHTED_INTEGRAL}",
        },
        {
            "gate": "UnsmoothedPerronFrontierClosed",
            "closed": False,
            "proved": False,
            "meaning": "非平滑 Perron 子账本尚未闭合。",
            "remaining": TARGET,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_unsmoothed_perron_frontier_router",
        "status": "unsmoothed_perron_frontier_compressed_to_zeta_logder_contour_shift_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "internal_psi0_exact_formula_closed": True,
        "right_edge_perron_kernel_closed": True,
        "height_selection_closed": True,
        "zero_boundary_avoidance_closed": True,
        "unsmoothed_perron_frontier_compressed": True,
        "zeta_logder_contour_shift_proved": False,
        "horizontal_logder_bound_proved": False,
        "local_zero_distance_sum_proved": False,
        "horizontal_weighted_integral_budget_proved": False,
        "backlund_indentation_internal_proved": False,
        "good_height_tstar_contract_accepted": False,
        "unsmoothed_perron_formula_proved": False,
        "self_contained_mertens_tail_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": LOCAL_ZERO_DISTANCE,
        "parallel_attack_targets": [WEIGHTED_INTEGRAL, BACKLUND_INTERNAL, WHOLE_STRIP_EXTERNAL, GOOD_HEIGHT],
        "frontier_items": frontier_items(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "非平滑 Perron 子账本已继续压缩：内部 psi_0 精确公式与右边 Perron 核近似常数已经闭合，"
            "当前真实硬点是 zeta 对数导数轮廓移线。该硬点又被压成水平边 away-from-zero 上界、"
            "局部零点距离和、加权积分预算，以及固定 T 缩进或好高度 T* 的合同选择。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 非平滑 Perron 当前前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"internal_psi0_exact_formula_closed={fmt_bool(result['internal_psi0_exact_formula_closed'])}",
        f"right_edge_perron_kernel_closed={fmt_bool(result['right_edge_perron_kernel_closed'])}",
        f"height_selection_closed={fmt_bool(result['height_selection_closed'])}",
        f"zero_boundary_avoidance_closed={fmt_bool(result['zero_boundary_avoidance_closed'])}",
        f"unsmoothed_perron_frontier_compressed={fmt_bool(result['unsmoothed_perron_frontier_compressed'])}",
        f"zeta_logder_contour_shift_proved={fmt_bool(result['zeta_logder_contour_shift_proved'])}",
        f"horizontal_logder_bound_proved={fmt_bool(result['horizontal_logder_bound_proved'])}",
        f"local_zero_distance_sum_proved={fmt_bool(result['local_zero_distance_sum_proved'])}",
        f"horizontal_weighted_integral_budget_proved={fmt_bool(result['horizontal_weighted_integral_budget_proved'])}",
        f"backlund_indentation_internal_proved={fmt_bool(result['backlund_indentation_internal_proved'])}",
        f"good_height_tstar_contract_accepted={fmt_bool(result['good_height_tstar_contract_accepted'])}",
        f"unsmoothed_perron_formula_proved={fmt_bool(result['unsmoothed_perron_formula_proved'])}",
        f"self_contained_mertens_tail_proved={fmt_bool(result['self_contained_mertens_tail_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿表",
        "",
        "| name | status | meaning | remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["frontier_items"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    f"`{table_cell(row['status'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本步不闭合非平滑 Perron 子账本；只关闭已证子层并给出下一个真正微硬点。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    MONOGRAPH.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
