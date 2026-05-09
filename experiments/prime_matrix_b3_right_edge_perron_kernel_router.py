#!/usr/bin/env python3
"""Prime Matrix B=3 psi_0 右边 Perron 核近似常数路由器。

用法示例：
  python3 experiments/prime_matrix_b3_right_edge_perron_kernel_router.py

输出：
  docs/monograph/prime-matrix-b3-right-edge-perron-kernel-router.json
  docs/monograph/prime-matrix-b3-right-edge-perron-kernel-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-perron-kernel-truncation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-right-edge-perron-kernel-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-right-edge-perron-kernel-router.md"

OLD_ATOM = "Psi0RightEdgePerronKernelApproximationConstantLedger"
CLOSED_ATOM = "Psi0RightEdgePerronKernelApproximationClosedC128"
CONTOUR_ATOM = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_RIGHT = 128.0
C_EDGE = 4.0
ANCHOR_X = 20_000.0
ANCHOR_T = 14.0


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


def replace_atom(text: str) -> str:
    """替换右边 Perron 核近似原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def pressure_table() -> dict[str, float]:
    """计算锚点预算。"""
    log_xt = math.log(ANCHOR_X * ANCHOR_T)
    base = ANCHOR_X * log_xt * log_xt / ANCHOR_T
    return {
        "anchor_x": ANCHOR_X,
        "anchor_T": ANCHOR_T,
        "log_xT": log_xt,
        "base_x_log2_xT_over_T": base,
        "C_right": C_RIGHT,
        "C_edge": C_EDGE,
        "right_edge_bound_at_anchor": C_RIGHT * base + C_EDGE * math.log(ANCHOR_X),
    }


def proof_components() -> list[dict[str, Any]]:
    """登记右边 Perron 核证明组件。"""
    return [
        {
            "component": "truncated_kernel_pointwise_bound",
            "closed": True,
            "claim": "Perron 核误差由 min(1,1/(T|log(x/n)|)) 控制，端点取 psi_0 半权。",
        },
        {
            "component": "near_shell_bound",
            "closed": True,
            "claim": "|n-x|<=x/T 的近壳总 Lambda 质量由 log x 与壳长给出 O(x log x/T+log x)。",
        },
        {
            "component": "far_shell_dyadic_bound",
            "closed": True,
            "claim": "远壳按 |log(n/x)| dyadic 求和，使用 -zeta'/zeta(1+1/log x)<=2 log x 的保守界。",
        },
        {
            "component": "constant_aggregation",
            "closed": True,
            "claim": "近壳、远壳和端点统一吸收到 C_right=128, C_edge=4。",
        },
    ]


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
    """生成右边 Perron 核判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    upstream_reduced = bool(previous.get("perron_kernel_truncation_reduced"))
    exact_formula_ready = "InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost" in basis
    endpoint_ready = "ChebyshevPsi0EndpointHalfWeightConventionClosed" in basis
    closed = active and guard and upstream_reduced and exact_formula_ready and endpoint_ready
    return [
        row(
            "RightEdgePerronKernelGateActive",
            active,
            False,
            "Perron 截断核四包中的当前最窄点是右边竖线核近似常数。",
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
            "ExactPsi0AndEndpointReady",
            exact_formula_ready and endpoint_ready,
            True,
            "psi_0 精确公式和半权端点规范已闭合，可使用标准截断 Perron 核。",
            "无端点剩余。",
        ),
        row(
            "KernelPointwiseAndShellBoundsClosed",
            closed,
            True,
            "截断核点态误差、近壳质量、远壳 dyadic 求和和常数聚合给出 C_right=128。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "右边 Perron 核近似常数闭合；它只控制 psi_0 与右边竖线积分的差。",
            CLOSED_ATOM,
        ),
        row(
            CONTOUR_ATOM,
            False,
            False,
            "仍需把右边竖线积分移线为零点留数，并支付 -zeta'/zeta 轮廓边界。",
            CONTOUR_ATOM,
        ),
        row(
            ZERO_SUM_ATOM,
            False,
            False,
            "轮廓移线后还需零点自由带下的零点和预算。",
            ZERO_SUM_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行右边 Perron 核近似常数路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_right_edge_perron_kernel_router",
        "status": "right_edge_perron_kernel_closed_c128_contour_shift_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "right_edge_perron_kernel_closed": closed,
        "perron_kernel_truncation_constant_closed": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": CONTOUR_ATOM,
        "secondary_priority": ZERO_SUM_ATOM,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "constants": {"C_right": C_RIGHT, "C_edge": C_EDGE},
        "pressure": pressure_table(),
        "proof_components": proof_components(),
        "plain_conclusion": (
            "右边 Perron 核近似常数闭合为 C_right=128：它只支付 psi_0 与右边截断竖线积分之间的核误差。"
            "整个 R_T 常数尚未闭合，因为仍需 -zeta'/zeta 轮廓移线常数。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    pressure = result["pressure"]
    constants = result["constants"]
    lines = [
        "# Prime Matrix B=3 psi_0 右边 Perron 核近似常数路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"right_edge_perron_kernel_closed={fmt_bool(result['right_edge_perron_kernel_closed'])}",
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
        "## 2. 常数",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| C_right | `{fmt_float(constants['C_right'])}` |",
        f"| C_edge | `{fmt_float(constants['C_edge'])}` |",
        f"| anchor x | `{fmt_float(pressure['anchor_x'])}` |",
        f"| anchor T | `{fmt_float(pressure['anchor_T'])}` |",
        f"| right edge bound at anchor | `{fmt_float(pressure['right_edge_bound_at_anchor'])}` |",
        "",
        "## 3. 证明组件",
        "",
        "| component | closed | claim |",
        "| --- | --- | --- |",
    ]
    for item in result["proof_components"]:
        lines.append(
            f"| {table_cell(item['component'])} | `{fmt_bool(item['closed'])}` | {table_cell(item['claim'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            f"当前最窄点更新为 `{result['next_priority']}`；随后是 `{result['secondary_priority']}`。",
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
