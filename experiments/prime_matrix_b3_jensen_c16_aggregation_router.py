#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen C_N=16 聚合障碍与重路由证书。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_c16_aggregation_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-c16-aggregation-router.json
  docs/monograph/prime-matrix-b3-jensen-c16-aggregation-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-center-anchor-aggregation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-c16-aggregation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-c16-aggregation-router.md"

OLD_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
SIGNED_MEAN_ATOM = "BacklundJensenSignedMeanBoundaryAnchorC16Ledger"
LOW_NUMERIC_ATOM = "BacklundJensenLowHeightExplicitEnvelopeNumericalLedger"
RADIUS_OPT_ATOM = "BacklundJensenRadiusOptimizationOrCNRelaxationLedger"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
DIST_CONST_ATOM = "BacklundZeroDistanceSumConstantAggregationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

BOUNDARY_PACKAGE = "BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic"
ANCHOR_PACKAGE = "BacklundIndependentJensenCenterLowerAnchorClosedSymbolic"

OUTER_RADIUS = 4.0
INNER_RADIUS = math.sqrt(5.0)
JENSEN_DENOMINATOR = math.log(OUTER_RADIUS / INNER_RADIUS)
C_N_TARGET = 16.0
C_XI_BOUNDARY_MIN = 16.0
MAX_ALLOWED_NUMERATOR = C_N_TARGET * JENSEN_DENOMINATOR
POINTWISE_FORCED_CN = C_XI_BOUNDARY_MIN / JENSEN_DENOMINATOR
NUMERATOR_DEFICIT = C_XI_BOUNDARY_MIN - MAX_ALLOWED_NUMERATOR


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
    """写出 C_N=16 聚合的重路由包。"""
    return f"({SIGNED_MEAN_ATOM} AND {LOW_NUMERIC_ATOM} AND {RADIUS_OPT_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧 C_N=16 聚合原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def obstruction_rows() -> list[dict[str, float | str]]:
    """生成点态聚合障碍表。"""
    return [
        {
            "quantity": "Jensen denominator",
            "formula": "log(4/sqrt(5))",
            "value": JENSEN_DENOMINATOR,
        },
        {
            "quantity": "allowed numerator for C_N=16",
            "formula": "16*log(4/sqrt(5))",
            "value": MAX_ALLOWED_NUMERATOR,
        },
        {
            "quantity": "pointwise boundary lower floor",
            "formula": "C_xi_boundary >= 16",
            "value": C_XI_BOUNDARY_MIN,
        },
        {
            "quantity": "forced C_N from boundary alone",
            "formula": "16/log(4/sqrt(5))",
            "value": POINTWISE_FORCED_CN,
        },
        {
            "quantity": "numerator deficit before anchor",
            "formula": "16 - 16*log(4/sqrt(5))",
            "value": NUMERATOR_DEFICIT,
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
    """生成 Jensen C_N=16 聚合障碍判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    boundary_ready = BOUNDARY_PACKAGE in basis
    anchor_ready = ANCHOR_PACKAGE in basis
    jensen_ready = "BacklundJensenDiskFormulaClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and boundary_ready and anchor_ready and jensen_ready and guard
    pointwise_failure = C_XI_BOUNDARY_MIN > MAX_ALLOWED_NUMERATOR
    return [
        row(
            "JensenC16AggregationGateActive",
            active,
            False,
            "上一层唯一内部最窄点是独立 Jensen 局部零点计数 C_N=16 聚合。",
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
            "BoundaryAnchorJensenInputsAvailable",
            boundary_ready and anchor_ready and jensen_ready,
            True,
            "独立圆周上界、圆心下界与 Jensen 公式均已闭合到符号层。",
            "无形式输入剩余。",
        ),
        row(
            "PointwiseBoundaryRouteFailsC16",
            pointwise_failure,
            True,
            "用点态圆周上界聚合时，C_xi_boundary>=16 已经超过 C_N=16 允许的 Jensen 分子预算。",
            SIGNED_MEAN_ATOM,
        ),
        row(
            "C16AggregationNotClosed",
            True,
            True,
            "当前符号包只能证明有限 C_N；不能证明目标常数 C_N=16。",
            replacement_pair(),
        ),
        row(
            "SignedMeanBoundaryAnchorNeeded",
            False,
            False,
            "必须改用 Jensen 圆周平均中的有符号因子分离，避免把 Gamma/初等/zeta 平均全部点态正化。",
            SIGNED_MEAN_ATOM,
        ),
        row(
            "LowHeightNumericalEnvelopeNeeded",
            False,
            False,
            "低高度符号常数也必须数值化或证明可被 C_N=16 预算吸收。",
            LOW_NUMERIC_ATOM,
        ),
        row(
            "RadiusOptimizationOrCNRelaxationNeeded",
            False,
            False,
            "若 signed mean 仍不足，必须优化 Jensen 半径或明确把下游 C_N 从 16 放宽。",
            RADIUS_OPT_ATOM,
        ),
        row(
            "IndependentJensenC16AggregationReduced",
            reduced,
            False,
            "旧 C_N=16 聚合原子被压成 signed mean、低高度数值包、半径优化或常数放宽三包。",
            replacement_pair(),
        ),
        row(
            "NearZeroAndDistanceStillDownstream",
            False,
            False,
            "C_N 聚合完成后才进入近零分离和倒距离常数聚合。",
            f"{NEAR_ZERO_ATOM} AND {DIST_CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Jensen C_N=16 聚合障碍与重路由证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "IndependentJensenC16AggregationReduced")
    return {
        "certificate_type": "b3_jensen_c16_aggregation_router",
        "status": "backlund_jensen_c16_aggregation_reduced_signed_mean_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_independent_jensen_c16_aggregation_reduced": reduced,
        "backlund_independent_jensen_c16_aggregation_closed": False,
        "finite_symbolic_CN_available": True,
        "C_N_target": C_N_TARGET,
        "outer_radius": OUTER_RADIUS,
        "inner_radius": INNER_RADIUS,
        "jensen_denominator": JENSEN_DENOMINATOR,
        "max_allowed_numerator": MAX_ALLOWED_NUMERATOR,
        "pointwise_boundary_floor": C_XI_BOUNDARY_MIN,
        "pointwise_forced_CN": POINTWISE_FORCED_CN,
        "numerator_deficit_before_anchor": NUMERATOR_DEFICIT,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": SIGNED_MEAN_ATOM,
        "secondary_priority": LOW_NUMERIC_ATOM,
        "tertiary_priority": RADIUS_OPT_ATOM,
        "post_jensen_priority": NEAR_ZERO_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "obstruction_rows": obstruction_rows(),
        "plain_conclusion": (
            "Jensen C_N=16 聚合尚未闭合。"
            "当前点态圆周上界路线有硬性常数障碍：仅 C_xi_boundary>=16 经 log(4/sqrt(5)) "
            "相除就强制 C_N>=27.51。下一步必须改攻有符号 Jensen 均值和低高度数值包。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen C_N=16 聚合障碍与重路由证书",
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
            "backlund_independent_jensen_c16_aggregation_reduced="
            f"{fmt_bool(result['backlund_independent_jensen_c16_aggregation_reduced'])}"
        ),
        (
            "backlund_independent_jensen_c16_aggregation_closed="
            f"{fmt_bool(result['backlund_independent_jensen_c16_aggregation_closed'])}"
        ),
        f"finite_symbolic_CN_available={fmt_bool(result['finite_symbolic_CN_available'])}",
        f"C_N_target={fmt_float(result['C_N_target'])}",
        f"jensen_denominator={fmt_float(result['jensen_denominator'])}",
        f"max_allowed_numerator={fmt_float(result['max_allowed_numerator'])}",
        f"pointwise_boundary_floor={fmt_float(result['pointwise_boundary_floor'])}",
        f"pointwise_forced_CN={fmt_float(result['pointwise_forced_CN'])}",
        f"numerator_deficit_before_anchor={fmt_float(result['numerator_deficit_before_anchor'])}",
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
        "## 2. 常数障碍",
        "",
        "| quantity | formula | value |",
        "| --- | --- | ---: |",
    ]
    for item in result["obstruction_rows"]:
        lines.append(
            "| {quantity} | {formula} | `{value}` |".format(
                quantity=table_cell(item["quantity"]),
                formula=table_cell(item["formula"]),
                value=fmt_float(float(item["value"])),
            )
        )
    lines.extend(
        [
            "",
            "结论：当前符号圆周上界包足以给出某个有限 `C_N`，但不足以给出 `C_N=16`。",
            "要继续闭合，必须回到 Jensen 平均本身，保留因子分离和有符号相消，而不是使用点态 `log^+|xi|` 包。",
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
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`。"
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
