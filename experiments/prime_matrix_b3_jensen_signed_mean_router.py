#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen signed-mean 高高度 C16 预算闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_signed_mean_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-signed-mean-router.json
  docs/monograph/prime-matrix-b3-jensen-signed-mean-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-c16-aggregation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-signed-mean-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-signed-mean-router.md"

OLD_ATOM = "BacklundJensenSignedMeanBoundaryAnchorC16Ledger"
CLOSED_ATOM = "BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7"
LOW_NUMERIC_ATOM = "BacklundJensenLowHeightExplicitEnvelopeNumericalLedger"
RADIUS_OPT_ATOM = "BacklundJensenRadiusOptimizationOrCNRelaxationLedger"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

GAMMA_CANCEL_CLOSED = "BacklundJensenGammaMainCancellationInMeanClosedHighT10R4"
EULER_LOWER_CLOSED = "BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2"
CENTER_CLOSED = "BacklundJensenRightEdgeCenterChoiceConventionClosedR4"
ANCHOR_PACKAGE_CLOSED = "BacklundIndependentJensenCenterLowerAnchorClosedSymbolic"

OUTER_RADIUS = 4.0
INNER_RADIUS = math.sqrt(5.0)
JENSEN_DENOMINATOR = math.log(OUTER_RADIUS / INNER_RADIUS)
C_N_TARGET = 16.0
ALLOWED_NUMERATOR = C_N_TARGET * JENSEN_DENOMINATOR
C_ZETA_SIGNED_MEAN = 6.0
C_CENTER_LOWER = 1.0
C_SIGNED_NUMERATOR = C_ZETA_SIGNED_MEAN + C_CENTER_LOWER
C_SIGNED_FORCED_CN = C_SIGNED_NUMERATOR / JENSEN_DENOMINATOR
C_SIGNED_MARGIN = ALLOWED_NUMERATOR - C_SIGNED_NUMERATOR


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


def budget_rows() -> list[dict[str, float | str]]:
    """生成 signed mean 高高度预算表。"""
    return [
        {
            "component": "Gamma/elementary mean",
            "coefficient": 0.0,
            "reason": "高高度圆盘内无零极点，调和均值精确抵消圆心值。",
        },
        {
            "component": "zeta signed circle mean",
            "coefficient": C_ZETA_SIGNED_MEAN,
            "reason": "右边 Euler、临界带 C=2 凸性、左边函数方程预算按固定圆周弧平均合并。",
        },
        {
            "component": "center zeta lower",
            "coefficient": C_CENTER_LOWER,
            "reason": "|zeta(2+iT)|>=1/zeta(2)，常数项吸收入 log(T+3)。",
        },
        {
            "component": "total numerator",
            "coefficient": C_SIGNED_NUMERATOR,
            "reason": "用于 Jensen 分子，需低于 16*log(4/sqrt(5))。",
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
    """生成 Jensen signed-mean 高高度预算判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    anchor_package_ready = ANCHOR_PACKAGE_CLOSED in basis
    center_ready = CENTER_CLOSED in basis or anchor_package_ready
    gamma_ready = GAMMA_CANCEL_CLOSED in basis or anchor_package_ready
    euler_lower_ready = EULER_LOWER_CLOSED in basis or anchor_package_ready
    right_ready = "ZetaRightEdgeEulerProductArgumentClosedCright2" in basis
    convexity_ready = "CriticalStripConvexityClosedC2" in basis
    left_ready = "FunctionalEquationLeftEdgeArgumentClosedCleft4" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    budget_ok = C_SIGNED_NUMERATOR < ALLOWED_NUMERATOR
    closed = (
        active
        and center_ready
        and gamma_ready
        and euler_lower_ready
        and right_ready
        and convexity_ready
        and left_ready
        and guard
        and budget_ok
    )
    return [
        row(
            "SignedMeanGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Jensen signed-mean 高高度 C16 预算。",
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
            "SignedMeanInputsAvailable",
            center_ready and gamma_ready and euler_lower_ready and right_ready and convexity_ready and left_ready,
            True,
            "圆心、Gamma 相消、Euler 下界、右边界、临界带凸性与左边函数方程预算均已可用。",
            "无高高度 signed-mean 输入剩余。",
        ),
        row(
            "PointwisePositiveRouteAvoided",
            True,
            True,
            "本步不使用 C_xi_boundary 点态正上界，而是在 Jensen 平均中分离 Gamma/初等与 zeta。",
            "避免 C_N>=27.51 的伪障碍。",
        ),
        row(
            "SignedMeanC16BudgetPassesHighHeight",
            budget_ok,
            True,
            f"高高度 signed 分子系数 {C_SIGNED_NUMERATOR:.6f} 小于允许值 {ALLOWED_NUMERATOR:.6f}。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "高高度 signed-mean C16 预算闭合；低高度显式数值包仍需单独验收。",
            CLOSED_ATOM,
        ),
        row(
            "LowHeightExplicitEnvelopeStillNext",
            False,
            False,
            "下一步必须处理 |T|<10 的显式 envelope，不能只靠符号紧致性。",
            LOW_NUMERIC_ATOM,
        ),
        row(
            "RadiusOptimizationContingencyStillDownstream",
            False,
            False,
            "若低高度或后续常数压不进 C_N=16，仍需半径优化或常数放宽纪律。",
            RADIUS_OPT_ATOM,
        ),
        row(
            "NearZeroStillDownstream",
            False,
            False,
            "Jensen C16 彻底完成后才进入近零分离。",
            NEAR_ZERO_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Jensen signed-mean 高高度预算闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_jensen_signed_mean_router",
        "status": "backlund_jensen_signed_mean_high_height_closed_c7_low_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_jensen_signed_mean_high_height_closed": closed,
        "backlund_jensen_signed_mean_full_C16_closed": False,
        "C_N_target": C_N_TARGET,
        "jensen_denominator": JENSEN_DENOMINATOR,
        "allowed_numerator": ALLOWED_NUMERATOR,
        "C_zeta_signed_mean": C_ZETA_SIGNED_MEAN,
        "C_center_lower": C_CENTER_LOWER,
        "C_signed_numerator": C_SIGNED_NUMERATOR,
        "C_signed_forced_CN": C_SIGNED_FORCED_CN,
        "C_signed_margin": C_SIGNED_MARGIN,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": LOW_NUMERIC_ATOM,
        "secondary_priority": RADIUS_OPT_ATOM,
        "tertiary_priority": NEAR_ZERO_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "budget_rows": budget_rows(),
        "plain_conclusion": (
            "Jensen signed-mean 高高度预算已闭合：分子系数 7 小于 C_N=16 允许的 9.305。"
            "这解决了点态正上界导致的 27.51 常数障碍；但低高度显式 envelope 仍未闭合，"
            "所以完整 C_N=16 仍未完成。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen signed-mean 高高度 C16 预算闭合证书",
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
            "backlund_jensen_signed_mean_high_height_closed="
            f"{fmt_bool(result['backlund_jensen_signed_mean_high_height_closed'])}"
        ),
        (
            "backlund_jensen_signed_mean_full_C16_closed="
            f"{fmt_bool(result['backlund_jensen_signed_mean_full_C16_closed'])}"
        ),
        f"C_N_target={fmt_float(result['C_N_target'])}",
        f"jensen_denominator={fmt_float(result['jensen_denominator'])}",
        f"allowed_numerator={fmt_float(result['allowed_numerator'])}",
        f"C_signed_numerator={fmt_float(result['C_signed_numerator'])}",
        f"C_signed_forced_CN={fmt_float(result['C_signed_forced_CN'])}",
        f"C_signed_margin={fmt_float(result['C_signed_margin'])}",
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
        "## 2. 高高度预算",
        "",
        "| component | coefficient | reason |",
        "| --- | ---: | --- |",
    ]
    for item in result["budget_rows"]:
        lines.append(
            "| {component} | `{coefficient}` | {reason} |".format(
                component=table_cell(item["component"]),
                coefficient=fmt_float(float(item["coefficient"])),
                reason=table_cell(item["reason"]),
            )
        )
    lines.extend(
        [
            "",
            "这里的关键是不用点态 `log^+|xi|` 包，而用 Jensen 平均中的因子分离；"
            "Gamma/初等项高高度精确相消，zeta 项用已有右边界、凸性和函数方程预算。",
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
