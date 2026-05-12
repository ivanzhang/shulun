#!/usr/bin/env python3
"""生成 strict 非平滑 Perron 自足剩余压缩路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_unsmoothed_perron_self_contained_reduction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-unsmoothed-perron-self-contained-reduction-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-self-contained-reduction-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-self-contained-reduction-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-unified-contradiction-field-current-frontier-router.md",
    MONOGRAPH / "prime-matrix-b3-internal-psi0-perron-formula-router.json",
    MONOGRAPH / "prime-matrix-b3-right-edge-perron-kernel-router.json",
    MONOGRAPH / "prime-matrix-b3-psi0-fixed-height-indentation-router.json",
    MONOGRAPH / "prime-matrix-b3-psi0-horizontal-local-zero-distance-router.json",
    MONOGRAPH / "prime-matrix-b3-psi0-horizontal-weighted-budget-router.json",
    MONOGRAPH / "prime-matrix-b3-psi0-contour-shift-external-aggregation-router.json",
]

TARGET = "UnsmoothedChebyshevPerronExplicitFormulaConstantLedger"
INTERNAL_PSI0 = "InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost"
RIGHT_KERNEL = "Psi0RightEdgePerronKernelApproximationClosedC128"
CONTOUR_EXTERNAL = "Psi0ZetaLogDerivativeContourShiftExternalClosedC12000"
PERRON_EXTERNAL = "PerronKernelTruncationForPsi0ExternalClosedC12128"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
LOGDER_INTERNAL = "ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger"
LOCAL_DISTANCE = "Psi0HorizontalLocalZeroDistanceSumConstantLedger"
LOCAL_DISTANCE_CLOSED = "Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16"
WEIGHTED_BUDGET = "Psi0HorizontalWeightedIntegralBudgetLedger"
WEIGHTED_BUDGET_CLOSED = "Psi0HorizontalWeightedIntegralBudgetClosedC12000"
GOOD_HEIGHT = "Psi0GoodHeightTStarAveragingContourShiftLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def reduction_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 Perron 自足压缩判定行。"""
    exact = data["psi0"].get("internal_psi0_exact_formula_closed") is True
    right = data["right"].get("right_edge_perron_kernel_closed") is True
    fixed_t_external = data["indent"].get("psi0_fixed_t_indentation_external_closed") is True
    fixed_t_self = data["indent"].get("psi0_fixed_t_indentation_self_contained_closed") is True
    local_external = data["local"].get("psi0_horizontal_local_zero_distance_external_closed") is True
    local_self = data["local"].get("psi0_horizontal_local_zero_distance_self_contained_closed") is True
    weighted_external = data["weighted"].get("psi0_horizontal_weighted_integral_budget_external_closed") is True
    weighted_self = data["weighted"].get("psi0_horizontal_weighted_integral_budget_self_contained_closed") is True
    contour_external = data["contour"].get("psi0_zeta_logder_contour_shift_external_closed") is True
    perron_external = data["contour"].get("perron_kernel_truncation_external_closed") is True
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍服务统一矛盾场中的 B3/TV 输入，不使用真实零行缺席。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "Psi0ExactFormulaInternalClosed",
            "closed": exact,
            "proved": exact,
            "meaning": "psi_0 无截断显式公式身份已在作者侧闭合。",
            "remaining": INTERNAL_PSI0,
        },
        {
            "gate": "RightPerronKernelClosed",
            "closed": right,
            "proved": right,
            "meaning": "右边 Perron 核近似常数 C=128 已闭合。",
            "remaining": RIGHT_KERNEL,
        },
        {
            "gate": "ExternalFixedTIndentAndContourClosed",
            "closed": fixed_t_external and local_external and weighted_external and contour_external and perron_external,
            "proved": False,
            "meaning": "接受外部 Backlund/RVM/Titchmarsh 时，fixed-T 缩进、局部零点距离、加权水平预算和轮廓移线已条件关闭。",
            "remaining": f"{CONTOUR_EXTERNAL} AND {PERRON_EXTERNAL}",
        },
        {
            "gate": "SelfContainedFixedTIndentClosed",
            "closed": fixed_t_self,
            "proved": fixed_t_self,
            "meaning": "严格自足 fixed-T 缩进仍未完成；这是外部条件链不能直接转为作者侧证明的首要原因。",
            "remaining": BACKLUND_INTERNAL,
        },
        {
            "gate": "SelfContainedLocalZeroDistanceClosed",
            "closed": local_self,
            "proved": local_self,
            "meaning": "严格自足局部零点倒距离和需自足 C_N=16、避零缩进和内部 log-derivative 展开。",
            "remaining": f"{LOGDER_INTERNAL} AND {BACKLUND_INTERNAL} AND {LOCAL_DISTANCE}",
        },
        {
            "gate": "SelfContainedWeightedBudgetClosed",
            "closed": weighted_self,
            "proved": weighted_self,
            "meaning": "加权积分预算的算术常数已在外部条件线下闭合；自足同步仍等局部零点距离和前提。",
            "remaining": WEIGHTED_BUDGET,
        },
        {
            "gate": "GoodHeightAlternativeStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "可改走 T* 好高度平均路线，但必须重写当前 fixed-T Perron 合同，不能无声替换。",
            "remaining": GOOD_HEIGHT,
        },
        {
            "gate": "UnsmoothedPerronExternalConditionalClosed",
            "closed": perron_external,
            "proved": False,
            "meaning": "外部条件链可关闭非平滑 Perron finite-T 层。",
            "remaining": PERRON_EXTERNAL,
        },
        {
            "gate": "UnsmoothedPerronStrictSelfContainedClosed",
            "closed": False,
            "proved": False,
            "meaning": "严格自足版尚未关闭；当前已压成 Backlund 缩进、内部 log-derivative/local zero 和加权预算同步。",
            "remaining": f"{BACKLUND_INTERNAL} AND {LOGDER_INTERNAL} AND {LOCAL_DISTANCE} AND {WEIGHTED_BUDGET}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    data = {
        "frontier": load_json(MONOGRAPH / "prime-matrix-strict-unified-contradiction-field-current-frontier-router.json"),
        "psi0": load_json(MONOGRAPH / "prime-matrix-b3-internal-psi0-perron-formula-router.json"),
        "right": load_json(MONOGRAPH / "prime-matrix-b3-right-edge-perron-kernel-router.json"),
        "indent": load_json(MONOGRAPH / "prime-matrix-b3-psi0-fixed-height-indentation-router.json"),
        "local": load_json(MONOGRAPH / "prime-matrix-b3-psi0-horizontal-local-zero-distance-router.json"),
        "weighted": load_json(MONOGRAPH / "prime-matrix-b3-psi0-horizontal-weighted-budget-router.json"),
        "contour": load_json(MONOGRAPH / "prime-matrix-b3-psi0-contour-shift-external-aggregation-router.json"),
    }
    rows = reduction_rows(data)
    external_closed = next(item["closed"] for item in rows if item["gate"] == "UnsmoothedPerronExternalConditionalClosed")
    return {
        "certificate_type": "prime_matrix_strict_unsmoothed_perron_self_contained_reduction_router",
        "status": "unsmoothed_perron_external_closed_self_contained_reduced_to_backlund_logder_local_zero_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "unsmoothed_perron_external_conditional_closed": external_closed,
        "unsmoothed_perron_strict_self_contained_closed": False,
        "backlund_internal_proved": False,
        "classical_logder_internal_proved": False,
        "local_zero_distance_self_contained_proved": False,
        "weighted_budget_self_contained_proved": False,
        "good_height_contract_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": BACKLUND_INTERNAL,
        "secondary_attack_target": LOGDER_INTERNAL,
        "alternative_attack_target": GOOD_HEIGHT,
        "self_contained_replacement": (
            f"{BACKLUND_INTERNAL} AND {LOGDER_INTERNAL} AND "
            f"{LOCAL_DISTANCE} AND {WEIGHTED_BUDGET}"
        ),
        "external_replacement": f"{CONTOUR_EXTERNAL} AND {PERRON_EXTERNAL}",
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "非平滑 Perron 常数层的外部条件路线已经关闭：外部 fixed-T Backlund 缩进、"
            "局部零点距离 C=288、水平加权预算 C=12000 和右边核 C=128 已合并为 Perron C=12128。"
            "但严格自足版不能导入这些外部条件；它现在被压缩为固定高度 Backlund 缩进内部证明、"
            "内部 zeta log-derivative/local zero 展开，以及由此触发的加权预算同步。"
            "最窄主攻点更新为 ClassicalBacklundZeroIndentationCostInternalProofLedger。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 非平滑 Perron 自足剩余压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unsmoothed_perron_external_conditional_closed={fmt_bool(result['unsmoothed_perron_external_conditional_closed'])}",
        f"unsmoothed_perron_strict_self_contained_closed={fmt_bool(result['unsmoothed_perron_strict_self_contained_closed'])}",
        f"backlund_internal_proved={fmt_bool(result['backlund_internal_proved'])}",
        f"classical_logder_internal_proved={fmt_bool(result['classical_logder_internal_proved'])}",
        f"local_zero_distance_self_contained_proved={fmt_bool(result['local_zero_distance_self_contained_proved'])}",
        f"weighted_budget_self_contained_proved={fmt_bool(result['weighted_budget_self_contained_proved'])}",
        f"good_height_contract_accepted={fmt_bool(result['good_height_contract_accepted'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 条件替换边界",
        "",
        "外部条件线：",
        "",
        "```text",
        TARGET,
        "  =>",
        result["external_replacement"],
        "```",
        "",
        "严格自足线：",
        "",
        "```text",
        TARGET,
        "  =>",
        result["self_contained_replacement"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
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
            f"{result['secondary_attack_target']} OR {result['alternative_attack_target']}",
            "```",
            "",
            "审稿边界：这一步只把自足 Perron 剩余继续压缩；没有关闭 B3 TV，也没有关闭行/列无条件命题。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
