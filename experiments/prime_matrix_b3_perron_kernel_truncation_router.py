#!/usr/bin/env python3
"""Prime Matrix B=3 psi_0 Perron 截断核常数路由器。

用法示例：
  python3 experiments/prime_matrix_b3_perron_kernel_truncation_router.py

输出：
  docs/monograph/prime-matrix-b3-perron-kernel-truncation-router.json
  docs/monograph/prime-matrix-b3-perron-kernel-truncation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-internal-psi0-perron-formula-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-perron-kernel-truncation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-perron-kernel-truncation-router.md"

OLD_ATOM = "PerronKernelTruncationConstantForPsi0Ledger"
HEIGHT_ATOM = "Psi0PerronFiniteRectangleHeightSelectionLedger"
RIGHT_KERNEL_ATOM = "Psi0RightEdgePerronKernelApproximationConstantLedger"
CONTOUR_ATOM = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
BOUNDARY_ATOM = "Psi0ZeroBoundaryAvoidanceLimitLedger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
TRIVIAL_TAIL_ATOM = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000.0
ANCHOR_T = 14.0
TARGET_C_PERRON = 256.0
TARGET_C_EDGE = 8.0


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


def replacement_pair() -> str:
    """写出截断核常数替换包。"""
    return f"({HEIGHT_ATOM} AND {RIGHT_KERNEL_ATOM} AND {CONTOUR_ATOM} AND {BOUNDARY_ATOM})"


def replace_atom(text: str) -> str:
    """替换 Perron 截断核原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def pressure_table() -> dict[str, float]:
    """计算锚点上的截断核目标压力。"""
    log_xt = math.log(ANCHOR_X * ANCHOR_T)
    base = ANCHOR_X * log_xt * log_xt / ANCHOR_T
    edge = math.log(ANCHOR_X)
    return {
        "anchor_x": ANCHOR_X,
        "anchor_T": ANCHOR_T,
        "log_xT": log_xt,
        "base_x_log2_xT_over_T": base,
        "candidate_C_Perron": TARGET_C_PERRON,
        "candidate_C_edge": TARGET_C_EDGE,
        "candidate_bound_at_anchor": TARGET_C_PERRON * base + TARGET_C_EDGE * edge,
    }


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Perron 截断核常数判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    exact_formula_ready = bool(previous.get("internal_psi0_exact_formula_closed"))
    boundary_ready = "ChebyshevPsi0EndpointHalfWeightConventionClosed" in basis
    height_closed = True
    boundary_closed = boundary_ready
    right_kernel_closed = False
    contour_closed = False
    reduced = active and guard and exact_formula_ready and height_closed and boundary_closed
    closed = reduced and right_kernel_closed and contour_closed
    return [
        row(
            "PerronKernelGateActive",
            active,
            False,
            "上一层已闭合无截断 psi_0 精确公式，当前最窄点是 finite-T 截断核常数。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ExactPsi0FormulaAvailable",
            exact_formula_ready,
            True,
            "无截断 psi_0 显式公式已闭合，可作为 finite-T 截断的起点。",
            "InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost",
        ),
        row(
            "HeightSelectionLedgerClosed",
            height_closed,
            True,
            "取避开零点高度的 T_epsilon 并最终令 epsilon->0；高度选择只改变端点极限，不产生主预算。",
            HEIGHT_ATOM,
        ),
        row(
            "BoundaryAvoidanceLimitClosed",
            boundary_closed,
            True,
            "端点半权与避零极限已登记，边界落零按重数进入极限。",
            BOUNDARY_ATOM,
        ),
        row(
            "RightEdgeKernelApproximationConstantMissing",
            right_kernel_closed,
            False,
            "还缺直接从截断 Perron 核估计 psi_0 与右边竖线积分差的显式常数。",
            RIGHT_KERNEL_ATOM,
        ),
        row(
            "ZetaLogDerivativeContourShiftBoundMissing",
            contour_closed,
            False,
            "还缺把右边竖线移到零点留数公式时，水平边和左边界的显式 -zeta'/zeta 常数。",
            CONTOUR_ATOM,
        ),
        row(
            "PerronKernelReducedToFourMicroLedgers",
            reduced,
            False,
            "截断核常数原子已压成高度选择、右边 Perron 核近似、zeta 对数导数轮廓界、边界避零极限四项。",
            replacement_pair(),
        ),
        row(
            OLD_ATOM,
            closed,
            False,
            "只有右边 Perron 核常数和 zeta 对数导数轮廓界都完成后，才能关闭 R_T 常数。",
            replacement_pair(),
        ),
        row(
            ZERO_SUM_ATOM,
            False,
            False,
            "截断核之后还要把零点自由带代入零点和数值预算。",
            ZERO_SUM_ATOM,
        ),
        row(
            TRIVIAL_TAIL_ATOM,
            False,
            False,
            "平凡零点和素数幂尾项仍需同口径预算。",
            TRIVIAL_TAIL_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Perron 截断核常数路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "PerronKernelReducedToFourMicroLedgers"
    )
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_perron_kernel_truncation_router",
        "status": "perron_kernel_truncation_reduced_to_four_microledgers_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "perron_kernel_truncation_reduced": reduced,
        "perron_kernel_truncation_constant_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": RIGHT_KERNEL_ATOM,
        "secondary_priority": CONTOUR_ATOM,
        "post_kernel_priority": ZERO_SUM_ATOM,
        "tail_priority": TRIVIAL_TAIL_ATOM,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "candidate_bound_shape": "|R_T(x)| <= C_Perron*x*log^2(xT)/T + C_edge*log x",
        "candidate_constants": {
            "C_Perron": TARGET_C_PERRON,
            "C_edge": TARGET_C_EDGE,
        },
        "pressure": pressure_table(),
        "plain_conclusion": (
            "Perron 截断核常数层已压成四个微账本；高度选择与边界避零可由既有口径关闭，"
            "真正剩余是右边 Perron 核近似常数和 -zeta'/zeta 轮廓移线常数。当前不能声明 R_T 常数闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    pressure = result["pressure"]
    constants = result["candidate_constants"]
    lines = [
        "# Prime Matrix B=3 psi_0 Perron 截断核常数路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"perron_kernel_truncation_reduced={fmt_bool(result['perron_kernel_truncation_reduced'])}",
        f"perron_kernel_truncation_constant_closed={fmt_bool(result['perron_kernel_truncation_constant_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 候选常数合同",
        "",
        "```text",
        result["candidate_bound_shape"],
        "```",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| C_Perron | `{fmt_float(constants['C_Perron'])}` |",
        f"| C_edge | `{fmt_float(constants['C_edge'])}` |",
        f"| anchor x | `{fmt_float(pressure['anchor_x'])}` |",
        f"| anchor T | `{fmt_float(pressure['anchor_T'])}` |",
        f"| x log^2(xT)/T at anchor | `{fmt_float(pressure['base_x_log2_xT_over_T'])}` |",
        f"| candidate bound at anchor | `{fmt_float(pressure['candidate_bound_at_anchor'])}` |",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"当前最窄点更新为 `{result['next_priority']}`；之后是 `{result['secondary_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
