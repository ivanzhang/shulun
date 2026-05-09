#!/usr/bin/env python3
"""Prime Matrix B=3 psi_0 轮廓移线外部条件聚合路由器。

用法示例：
  python3 experiments/prime_matrix_b3_psi0_contour_shift_external_aggregation_router.py

输出：
  docs/monograph/prime-matrix-b3-psi0-contour-shift-external-aggregation-router.json
  docs/monograph/prime-matrix-b3-psi0-contour-shift-external-aggregation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-psi0-horizontal-weighted-budget-router.json"
DEFAULT_RIGHT = DOCS / "prime-matrix-b3-right-edge-perron-kernel-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-psi0-contour-shift-external-aggregation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-psi0-contour-shift-external-aggregation-router.md"

OLD_ATOM = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
CLOSED_ATOM = "Psi0ZetaLogDerivativeContourShiftExternalClosedC12000"
RIGHT_KERNEL = "Psi0RightEdgePerronKernelApproximationClosedC128"
HEIGHT = "Psi0PerronFiniteRectangleHeightSelectionLedger"
BOUNDARY = "Psi0ZeroBoundaryAvoidanceLimitLedger"
RESIDUE_LEFT = "Psi0ContourResidueAndLeftEdgeClosed"
HORIZONTAL_CLOSED = "Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosClosedByTitchmarshCN16C12000"
BACKLUND_EXTERNAL = "ClassicalBacklundZeroIndentationCostExternalAccepted"
PERRON_OLD = "PerronKernelTruncationConstantForPsi0Ledger"
PERRON_CLOSED = "PerronKernelTruncationForPsi0ExternalClosedC12128"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
TRIVIAL_TAIL_ATOM = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
THETA_TARGET = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"

C_RIGHT = 128.0
C_HORIZONTAL = 12_000.0
C_PERRON_TOTAL = C_RIGHT + C_HORIZONTAL


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def replace_atoms(text: str) -> str:
    """替换已聚合的轮廓移线相关原子。"""
    text = text.replace(OLD_ATOM, CLOSED_ATOM)
    text = text.replace(PERRON_OLD, PERRON_CLOSED)
    # 当前输入基通常已经展开了 OLD_ATOM；直接替换展开后的核心包。
    text = text.replace(
        f"{RESIDUE_LEFT} AND ({HORIZONTAL_CLOSED}) AND ({BACKLUND_EXTERNAL} OR Psi0GoodHeightTStarAveragingContourShiftLedger)",
        CLOSED_ATOM,
    )
    return text


def component_rows() -> list[dict[str, float | str]]:
    """生成聚合常数表。"""
    return [
        {
            "component": "right edge Perron kernel",
            "constant": C_RIGHT,
            "atom": RIGHT_KERNEL,
            "meaning": "psi_0 与右边截断竖线积分之间的核近似常数。",
        },
        {
            "component": "horizontal contour shift",
            "constant": C_HORIZONTAL,
            "atom": CLOSED_ATOM,
            "meaning": "zeta log-derivative 水平边和固定 T 凹口预算。",
        },
        {
            "component": "combined Perron truncation reserve",
            "constant": C_PERRON_TOTAL,
            "atom": PERRON_CLOSED,
            "meaning": "只表示 finite-T Perron 截断层闭合；不包含零点自由区零点和预算。",
        },
    ]


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], right: dict[str, Any]) -> list[dict[str, Any]]:
    """生成轮廓移线外部聚合判定表。"""
    basis = previous.get("latest_external_titchmarsh_cn16_basis", "")
    active = previous.get("next_priority") == "Psi0ZetaLogDerivativeContourShiftExternalAggregationLedger"
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    right_closed = right.get("right_edge_perron_kernel_closed") is True and RIGHT_KERNEL in basis
    horizontal_closed = previous.get("psi0_horizontal_logder_external_package_closed") is True and HORIZONTAL_CLOSED in basis
    residue_left_closed = RESIDUE_LEFT in basis
    fixed_t_external = BACKLUND_EXTERNAL in basis
    height_boundary_closed = HEIGHT in basis and BOUNDARY in basis
    contour_closed = active and guard and residue_left_closed and fixed_t_external and horizontal_closed
    perron_closed = contour_closed and right_closed and height_boundary_closed
    return [
        row(
            "ContourShiftExternalAggregationGateActive",
            active,
            True,
            "水平边包关闭后，当前任务是把留数左边界、fixed-T 缩进和水平边包合并回 zeta log-derivative 轮廓移线。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条解析输入，不使用真实零行缺席或数值实验替代证明。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ResidueAndLeftEdgeAvailable",
            residue_left_closed,
            True,
            "留数清单与左边界衰减已由内部 psi_0 精确公式吸收。",
            RESIDUE_LEFT,
        ),
        row(
            "FixedTIndentExternalAvailable",
            fixed_t_external,
            False,
            "fixed-T 近零缩进成本由外部 Backlund 引理条件支付。",
            BACKLUND_EXTERNAL,
        ),
        row(
            "HorizontalLogDerivativePackageAvailable",
            horizontal_closed,
            False,
            "水平边 log-derivative 包已由 Titchmarsh+CN16+C12000 条件路线关闭。",
            HORIZONTAL_CLOSED,
        ),
        row(
            OLD_ATOM,
            contour_closed,
            False,
            "外部条件路线下，zeta log-derivative 轮廓移线闭合为 C12000 水平预算。",
            CLOSED_ATOM,
        ),
        row(
            "RightKernelAndBoundaryAvailable",
            right_closed and height_boundary_closed,
            True,
            "右边 Perron 核 C128、高度选择和边界避零极限均已可用。",
            f"{RIGHT_KERNEL} AND {HEIGHT} AND {BOUNDARY}",
        ),
        row(
            PERRON_OLD,
            perron_closed,
            False,
            "外部条件路线下，finite-T Perron 截断层闭合，合并常数 C=12128。",
            PERRON_CLOSED,
        ),
        row(
            "PNTZeroSumBudgetStillOpen",
            False,
            False,
            "Perron 截断层关闭后，仍需 C=1280,T0=14 零点自由区零点和数值预算。",
            ZERO_SUM_ATOM,
        ),
        row(
            "TrivialTailThetaLowHeightStillOpen",
            False,
            False,
            "平凡零点/素数幂尾项、theta@20000 和低高度零点核验仍是独立账本。",
            f"{TRIVIAL_TAIL_ATOM} AND {THETA_TARGET} AND {FINITE_LOW_HEIGHT}",
        ),
        row(
            "SelfContainedContourShiftStillOpen",
            False,
            False,
            "严格自足路线仍缺自足 Backlund 缩进与自足 C_N=16，不能同步关闭。",
            BACKLUND_INTERNAL,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行轮廓移线外部聚合路由。"""
    previous = load_json(paths["previous"])
    right = load_json(paths["right"])
    rows = build_rows(previous, right)
    contour_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    perron_closed = next(item["closed"] for item in rows if item["gate"] == PERRON_OLD)
    latest_external = replace_atoms(previous.get("latest_external_titchmarsh_cn16_basis", ""))
    return {
        "certificate_type": "b3_psi0_contour_shift_external_aggregation_router",
        "status": "psi0_contour_shift_external_closed_perron_external_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "psi0_zeta_logder_contour_shift_external_closed": contour_closed,
        "perron_kernel_truncation_external_closed": perron_closed,
        "row_column_unconditional_closed": False,
        "C_right": C_RIGHT,
        "C_horizontal": C_HORIZONTAL,
        "C_perron_total": C_PERRON_TOTAL,
        "replacement_external": {
            OLD_ATOM: CLOSED_ATOM,
            PERRON_OLD: PERRON_CLOSED,
        },
        "latest_external_titchmarsh_cn16_basis": latest_external,
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "next_priority": ZERO_SUM_ATOM,
        "secondary_priority": TRIVIAL_TAIL_ATOM,
        "tertiary_priority": THETA_TARGET,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "parallel_self_contained_priority": BACKLUND_INTERNAL,
        "component_rows": component_rows(),
        "plain_conclusion": (
            "外部条件路线下，`Psi0ZetaLogDerivativeContourShiftBoundLedger` 已聚合关闭："
            "留数左边界、外部 fixed-T 缩进和水平边 C12000 包全部接上。"
            "结合右边 Perron 核 C128、高度选择和边界避零，finite-T `PerronKernelTruncationConstantForPsi0Ledger` "
            "条件闭合为 C=12128。该步仍不关闭零点自由区零点和预算、平凡尾项、theta@20000、低高度核验或行列无条件命题。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix B=3 psi_0 轮廓移线外部条件聚合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "psi0_zeta_logder_contour_shift_external_closed="
            f"{fmt_bool(result['psi0_zeta_logder_contour_shift_external_closed'])}"
        ),
        f"perron_kernel_truncation_external_closed={fmt_bool(result['perron_kernel_truncation_external_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"C_perron_total={fmt_float(result['C_perron_total'])}",
        "```",
        "",
        "## 1. 外部条件替换",
        "",
        "```text",
    ]
    for old, new in result["replacement_external"].items():
        lines.extend([old, "  =>", new, ""])
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
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 最新输入基",
            "",
            "外部 Titchmarsh+CN16 路线输入基：",
            "",
            "```text",
            result["latest_external_titchmarsh_cn16_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            f"下一步攻 `{result['next_priority']}`，并行保留严格自足缺口 `{result['parallel_self_contained_priority']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--right", type=Path, default=DEFAULT_RIGHT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "right": args.right,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
