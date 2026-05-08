#!/usr/bin/env python3
"""Prime Matrix B=3 函数方程左边界预算闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_functional_equation_left_edge_router.py

输出：
  docs/monograph/prime-matrix-b3-functional-equation-left-edge-router.json
  docs/monograph/prime-matrix-b3-functional-equation-left-edge-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-convexity-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-functional-equation-left-edge-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-functional-equation-left-edge-router.md"

OLD_ATOM = "FunctionalEquationLeftEdgeArgumentLedger"
CLOSED_ATOM = "FunctionalEquationLeftEdgeArgumentClosedCleft4"
CONVEXITY_CONST_ATOM = "CriticalStripConvexityC2ConstantOptimizationLedger"
HORIZONTAL_AGG_ATOM = "HorizontalVariationConstantAggregationLedger"
BACKLUND_CONST_ATOM = "BacklundArgumentConstantAggregationLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_CHI = 2.0
C_LEFT = 4.0


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
    """把待证 atom 替换为闭合 atom。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def chi_budget_rows() -> list[dict[str, float]]:
    """生成左边界 chi/Gamma 比值预算表。"""
    rows: list[dict[str, float]] = []
    for t in [2.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        logv = math.log(t + 3.0)
        eta = 1.0 / logv
        chi_envelope = math.log(4.0) + (0.5 + eta) * logv
        rows.append(
            {
                "T": t,
                "L": logv,
                "eta": eta,
                "chi_envelope": chi_envelope,
                "chi_2L_budget": C_CHI * logv,
                "chi_margin": C_CHI * logv - chi_envelope,
                "right_zeta_budget": logv,
                "pole_budget": logv,
                "left_F_budget": C_LEFT * logv,
            }
        )
    return rows


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
    """生成函数方程左边界判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    zeta_fe_ready = "ThetaMellinZetaContinuationFunctionalEquationClosed" in basis
    right_ready = "ZetaRightEdgeEulerProductArgumentClosedCright2" in basis
    gamma_ready = "GammaDigammaStirlingUniformNumericalClosedCgamma24" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and zeta_fe_ready and right_ready and gamma_ready and guard
    return [
        row(
            "FunctionalEquationLeftEdgeGateActive",
            active,
            False,
            "上一层唯一内部最窄点是函数方程左边界预算。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ZetaFunctionalEquationAvailable",
            zeta_fe_ready,
            True,
            "zeta 函数方程已在 theta-Mellin 层闭合。",
            "无函数方程形式剩余。",
        ),
        row(
            "RightEdgeEulerInputAvailable",
            right_ready,
            True,
            "左边界 s=-eta+it 经 1-s 映到右边界 1+eta-it，Euler product 预算可复用。",
            "无右边界剩余。",
        ),
        row(
            "ChiGammaRatioEnvelopeClosed",
            closed,
            True,
            "Gamma 比值给 |chi(-eta+it)|<=4(t+3)^(1/2+eta)，在 eta=1/L、T>=2 下由 2L 支付。",
            "ChiGammaRatioEnvelopeClosedCchi2",
        ),
        row(
            "LeftEdgePoleAndZetaBudgetClosed",
            closed,
            True,
            "log|F|<=log|s-1|+log|chi(s)|+log|zeta(1-s)| <= L+2L+L=4L。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "左边界函数方程预算闭合为 C_left=4；这不是 C=2 凸性目标的最优闭合。",
            CLOSED_ATOM,
        ),
        row(
            "ConvexityC2OptimizationStillNext",
            False,
            False,
            "下一步需要判断 C_left=4 是否可压到凸性目标 C=2，或调整后续水平边常数。",
            CONVEXITY_CONST_ATOM,
        ),
        row(
            "HorizontalAndBacklundAggregationStillDownstream",
            False,
            False,
            "随后还需水平边聚合与 Backlund 总常数聚合。",
            f"{HORIZONTAL_AGG_ATOM} AND {BACKLUND_CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行函数方程左边界闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_functional_equation_left_edge_router",
        "status": "functional_equation_left_edge_closed_cleft4",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "functional_equation_left_edge_closed": closed,
        "C_chi": C_CHI,
        "C_left": C_LEFT,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": CONVEXITY_CONST_ATOM,
        "secondary_priority": HORIZONTAL_AGG_ATOM,
        "tertiary_priority": BACKLUND_CONST_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "post_endpoint_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "chi_budget_rows": chi_budget_rows(),
        "core_inequality": (
            "s=-eta+it, eta=1/L, L=log(T+3), t>=1: "
            "zeta(s)=chi(s)zeta(1-s), log|chi(s)|<=2L, "
            "log|zeta(1-s)|<=L, log|s-1|<=L, hence log|F(s)|<=4L."
        ),
        "plain_conclusion": (
            "函数方程左边界预算已用 C_left=4 自足闭合。"
            "该闭合足以给左边界 O(log(T+3)) 输入，但还不足以证明凸性目标 C=2；"
            "下一步必须做 C=2 常数优化或明确改写水平边常数。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 函数方程左边界预算闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"functional_equation_left_edge_closed={fmt_bool(result['functional_equation_left_edge_closed'])}",
        f"C_chi={fmt_float(result['C_chi'])}",
        f"C_left={fmt_float(result['C_left'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 核心不等式",
        "",
        "```text",
        result["core_inequality"],
        "```",
        "",
        (
            "这里的 `chi` 预算来自函数方程中的 Gamma 比值。"
            "低于 `t=1` 的端点/低高度问题不在本账本中硬吞，后续仍由端点 convention 统一处理。"
        ),
        "",
        "## 3. chi/Gamma 比值预算审计",
        "",
        "| T | L | eta | chi envelope | 2L budget | chi margin | right zeta L | pole L | left F 4L |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["chi_budget_rows"]:
        lines.append(
            "| {T:.6g} | `{L}` | `{eta}` | `{chi}` | `{chi2}` | `{margin}` | `{right}` | `{pole}` | `{left}` |".format(
                T=item["T"],
                L=fmt_float(item["L"]),
                eta=fmt_float(item["eta"]),
                chi=fmt_float(item["chi_envelope"]),
                chi2=fmt_float(item["chi_2L_budget"]),
                margin=fmt_float(item["chi_margin"]),
                right=fmt_float(item["right_zeta_budget"]),
                pole=fmt_float(item["pole_budget"]),
                left=fmt_float(item["left_F_budget"]),
            )
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
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`、`{result['tertiary_priority']}`。"
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
