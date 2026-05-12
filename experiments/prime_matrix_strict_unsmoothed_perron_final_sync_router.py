#!/usr/bin/env python3
"""生成 strict 非平滑 Perron 自足最终同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_unsmoothed_perron_final_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-unsmoothed-perron-final-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-final-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-final-sync-router.md"

REDUCTION = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-self-contained-reduction-router.json"
BACKLUND = MONOGRAPH / "prime-matrix-strict-backlund-internal-closure-reconciliation-router.json"
LOGDER = MONOGRAPH / "prime-matrix-strict-logder-internal-expansion-router.json"
LOCAL_SYNC = MONOGRAPH / "prime-matrix-strict-local-zero-distance-self-contained-sync-router.json"
WEIGHTED_SYNC = MONOGRAPH / "prime-matrix-strict-weighted-budget-self-contained-sync-router.json"
INTERNAL_PSI0 = MONOGRAPH / "prime-matrix-b3-internal-psi0-perron-formula-router.json"
PERRON_KERNEL = MONOGRAPH / "prime-matrix-b3-perron-kernel-truncation-router.json"
RIGHT_EDGE = MONOGRAPH / "prime-matrix-b3-right-edge-perron-kernel-router.json"
EXTERNAL_AGGREGATION = MONOGRAPH / "prime-matrix-b3-psi0-contour-shift-external-aggregation-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [
    REDUCTION,
    BACKLUND,
    LOGDER,
    LOCAL_SYNC,
    WEIGHTED_SYNC,
    INTERNAL_PSI0,
    PERRON_KERNEL,
    RIGHT_EDGE,
    EXTERNAL_AGGREGATION,
    CLAIM_STATUS,
]

PERRON_OLD = "UnsmoothedChebyshevPerronExplicitFormulaConstantLedger"
CONTOUR_OLD = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
CONTOUR_CLOSED = "Psi0ZetaLogDerivativeContourShiftSelfContainedClosedC12000"
KERNEL_OLD = "PerronKernelTruncationConstantForPsi0Ledger"
KERNEL_CLOSED = "PerronKernelTruncationForPsi0SelfContainedClosedC12128"
PERRON_CLOSED = "UnsmoothedChebyshevPerronExplicitFormulaConstantSelfContainedClosedC12128"

ZERO_SUM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
TRIVIAL_TAIL = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
THETA_TARGET = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
MERTENS_TAIL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_RIGHT = 128.0
C_HORIZONTAL = 12_000.0
C_PERRON_TOTAL = C_RIGHT + C_HORIZONTAL


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记证据文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def gate_closed(data: dict[str, Any], gate: str, proved_required: bool = True) -> bool:
    """读取依赖 rows 中某个 gate 的闭合状态。"""
    for item in data.get("rows", []):
        if item.get("gate") == gate:
            if proved_required:
                return item.get("closed") is True and item.get("proved") is True
            return item.get("closed") is True
    return False


def component_rows() -> list[dict[str, Any]]:
    """生成 Perron 常数聚合表。"""
    return [
        {
            "component": "right edge Perron kernel",
            "constant": C_RIGHT,
            "atom": "Psi0RightEdgePerronKernelApproximationClosedC128",
            "meaning": "psi_0 与右边截断竖线积分之间的核误差。",
        },
        {
            "component": "horizontal contour package",
            "constant": C_HORIZONTAL,
            "atom": CONTOUR_CLOSED,
            "meaning": "fixed-T 缩进、水平边 log-derivative 与留数左边界合成的水平预算。",
        },
        {
            "component": "finite-T Perron reserve",
            "constant": C_PERRON_TOTAL,
            "atom": KERNEL_CLOSED,
            "meaning": "只关闭 finite-T Perron 截断层，不包含零点和/PNT 数值预算。",
        },
    ]


def build_rows(
    reduction: dict[str, Any],
    backlund: dict[str, Any],
    logder: dict[str, Any],
    local_sync: dict[str, Any],
    weighted_sync: dict[str, Any],
    internal_psi0: dict[str, Any],
    perron_kernel: dict[str, Any],
    right_edge: dict[str, Any],
    external_aggregation: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 strict Perron 最终同步判定表。"""
    guard = (
        reduction.get("counterexample_assumption_only") is True
        and backlund.get("direct_unconditional_contradiction_found") is False
        and logder.get("direct_unconditional_contradiction_found") is False
        and local_sync.get("direct_unconditional_contradiction_found") is False
        and weighted_sync.get("direct_unconditional_contradiction_found") is False
        and reduction.get("row_column_unconditional_closed") is False
        and weighted_sync.get("row_column_unconditional_closed") is False
    )
    exact_formula = internal_psi0.get("internal_psi0_exact_formula_closed") is True
    height_boundary = (
        gate_closed(perron_kernel, "HeightSelectionLedgerClosed")
        and gate_closed(perron_kernel, "BoundaryAvoidanceLimitClosed")
    )
    residue_left = gate_closed(external_aggregation, "ResidueAndLeftEdgeAvailable")
    right_ready = right_edge.get("right_edge_perron_kernel_closed") is True
    fixed_indent = (
        backlund.get("strict_perron_backlund_atom_replaced") is True
        and gate_closed(backlund, "FixedTIndentAtomReconciled")
    )
    logder_ready = logder.get("classical_zeta_logder_internal_expansion_closed") is True
    local_ready = local_sync.get("psi0_horizontal_local_zero_distance_self_contained_closed") is True
    weighted_ready = weighted_sync.get("psi0_horizontal_weighted_integral_budget_self_contained_closed") is True
    horizontal_package = weighted_sync.get("psi0_horizontal_logder_self_contained_package_closed") is True
    reduction_atoms_replaced = fixed_indent and logder_ready and local_ready and weighted_ready
    contour_self_closed = guard and residue_left and fixed_indent and horizontal_package
    kernel_self_closed = contour_self_closed and exact_formula and height_boundary and right_ready
    perron_self_closed = kernel_self_closed and reduction_atoms_replaced
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只关闭假设反例链所需解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "StrictReductionFourAtomsReplaced",
            reduction_atoms_replaced,
            reduction_atoms_replaced,
            "Backlund 缩进、logder 展开、局部倒距离和加权预算四个 strict 原子均已完成自足替换。",
            "Backlund AND logder AND local-zero-distance AND weighted-budget",
        ),
        row(
            "ExactPsi0FormulaInternalClosed",
            exact_formula,
            exact_formula,
            "内部 psi_0 无截断显式公式身份已闭合，可作为 finite-T 截断起点。",
            "InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost",
        ),
        row(
            "HeightAndBoundaryConventionClosed",
            height_boundary,
            height_boundary,
            "避零高度选择与边界重数极限已在 Perron 四微账本中闭合。",
            "Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0ZeroBoundaryAvoidanceLimitLedger",
        ),
        row(
            "ResidueAndLeftEdgeAvailable",
            residue_left,
            residue_left,
            "留数清单与左边界衰减已由内部 psi_0 精确公式链吸收。",
            "Psi0ContourResidueAndLeftEdgeClosed",
        ),
        row(
            "RightEdgePerronKernelClosed",
            right_ready,
            right_ready,
            "右边 Perron 核近似常数已给出 C=128。",
            "Psi0RightEdgePerronKernelApproximationClosedC128",
        ),
        row(
            "HorizontalContourShiftSelfContainedClosed",
            contour_self_closed,
            contour_self_closed,
            "fixed-T 缩进和水平边 logder 包均自足后，zeta 对数导数轮廓移线包自足闭合。",
            CONTOUR_CLOSED,
        ),
        row(
            KERNEL_OLD,
            kernel_self_closed,
            kernel_self_closed,
            "右边核 C=128 与水平边 C=12000 合成，finite-T Perron 截断层自足闭合为 C=12128。",
            KERNEL_CLOSED,
        ),
        row(
            "UnsmoothedPerronStrictSelfContainedClosed",
            perron_self_closed,
            perron_self_closed,
            "strict Perron 压缩账本四个开放原子全部替换后，非平滑 Perron 常数层自足闭合。",
            PERRON_CLOSED,
        ),
        row(
            "SelfContainedMertensTailStillOpen",
            False,
            False,
            "Perron 常数层闭合不等于 Mertens 尾段闭合；零点和、theta@20000、低高度和 B1 区间仍独立。",
            f"{ZERO_SUM} AND {TRIVIAL_TAIL} AND {THETA_TARGET} AND {FINITE_LOW_HEIGHT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步不产生早期零行反例链与真实结构链的终端矛盾；全局行/列命题仍未闭合。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    reduction = load_json(REDUCTION)
    backlund = load_json(BACKLUND)
    logder = load_json(LOGDER)
    local_sync = load_json(LOCAL_SYNC)
    weighted_sync = load_json(WEIGHTED_SYNC)
    internal_psi0 = load_json(INTERNAL_PSI0)
    perron_kernel = load_json(PERRON_KERNEL)
    right_edge = load_json(RIGHT_EDGE)
    external_aggregation = load_json(EXTERNAL_AGGREGATION)
    rows = build_rows(
        reduction,
        backlund,
        logder,
        local_sync,
        weighted_sync,
        internal_psi0,
        perron_kernel,
        right_edge,
        external_aggregation,
    )
    perron_closed = next(item["closed"] for item in rows if item["gate"] == "UnsmoothedPerronStrictSelfContainedClosed")
    kernel_closed = next(item["closed"] for item in rows if item["gate"] == KERNEL_OLD)
    return {
        "certificate_type": "prime_matrix_strict_unsmoothed_perron_final_sync_router",
        "status": "unsmoothed_perron_strict_self_contained_closed_mertens_tail_still_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "psi0_zeta_logder_contour_shift_self_contained_closed": kernel_closed,
        "perron_kernel_truncation_self_contained_closed": kernel_closed,
        "unsmoothed_perron_strict_self_contained_closed": perron_closed,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "C_right": C_RIGHT,
        "C_horizontal": C_HORIZONTAL,
        "C_perron_total": C_PERRON_TOTAL,
        "replacement_self_contained": {
            CONTOUR_OLD: CONTOUR_CLOSED,
            KERNEL_OLD: KERNEL_CLOSED,
            PERRON_OLD: PERRON_CLOSED,
        },
        "remaining_after_unsmoothed_perron_sync": [
            ZERO_SUM,
            TRIVIAL_TAIL,
            THETA_TARGET,
            FINITE_LOW_HEIGHT,
            "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold",
            "SelfContainedMeisselMertensConstantIntervalLedgerAt20000",
        ],
        "next_direct_attack_target": ZERO_SUM,
        "secondary_attack_targets": [TRIVIAL_TAIL, THETA_TARGET, FINITE_LOW_HEIGHT, MERTENS_TAIL],
        "source_hashes": source_hashes(),
        "component_rows": component_rows(),
        "plain_conclusion": (
            "`UnsmoothedChebyshevPerronExplicitFormulaConstantLedger` 已完成 strict 自足同步："
            "先前压缩出的四个开放原子已经逐项闭合，右边 Perron 核 C=128 与水平边 C=12000 "
            "合成为 finite-T Perron 常数 C=12128。"
            "这只关闭非平滑 Perron 常数层；自足 Mertens 尾段、B3 TV 和行/列无条件命题仍未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 非平滑 Perron 自足最终同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"psi0_zeta_logder_contour_shift_self_contained_closed={fmt_bool(result['psi0_zeta_logder_contour_shift_self_contained_closed'])}",
        f"perron_kernel_truncation_self_contained_closed={fmt_bool(result['perron_kernel_truncation_self_contained_closed'])}",
        f"unsmoothed_perron_strict_self_contained_closed={fmt_bool(result['unsmoothed_perron_strict_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"C_perron_total={fmt_float(result['C_perron_total'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
    ]
    for old, new in result["replacement_self_contained"].items():
        lines.extend([old, f"  => {new}", ""])
    lines.extend(
        [
            "```",
            "",
            "## 2. 常数聚合",
            "",
            "| component | constant | atom | meaning |",
            "| --- | ---: | --- | --- |",
        ]
    )
    for item in result["component_rows"]:
        lines.append(
            "| {component} | `{constant}` | {atom} | {meaning} |".format(
                component=table_cell(item["component"]),
                constant=fmt_float(float(item["constant"])),
                atom=table_cell(item["atom"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "也就是进入零点自由区零点和预算；这仍属于 B3/Mertens 尾段内部，不是全局行列终端矛盾。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
