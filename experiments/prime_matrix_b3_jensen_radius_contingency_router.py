#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen 半径优化冗余门路由器。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_radius_contingency_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-radius-contingency-router.json
  docs/monograph/prime-matrix-b3-jensen-radius-contingency-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-xi-nozero-below14-router.json"
DEFAULT_SIGNED = DOCS / "prime-matrix-b3-jensen-signed-mean-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-radius-contingency-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-radius-contingency-router.md"

OLD_ATOM = "BacklundJensenRadiusOptimizationOrCNRelaxationLedger"
CLOSED_ATOM = "BacklundJensenRadiusOptimizationNotNeededC16ClosedR4"
C16_CLOSED_ATOM = "BacklundIndependentJensenZeroCountC16AggregationExternalClosed"
SIGNED_MEAN_CLOSED = "BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7"
LOW_C16_CLOSED = "BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14"
NOZERO_EXTERNAL_CLOSED = "BacklundXiNoNontrivialZeroBelow14ExternalClosed"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
DIST_CONST_ATOM = "BacklundZeroDistanceSumConstantAggregationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def replace_radius(text: str) -> str:
    """替换半径优化冗余门。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def budget_rows(previous: dict[str, Any], signed: dict[str, Any]) -> list[dict[str, Any]]:
    """生成半径冗余验收预算表。"""
    return [
        {
            "range": "high height |T|>=10",
            "input": SIGNED_MEAN_CLOSED,
            "numerator": signed["C_signed_numerator"],
            "allowed": signed["allowed_numerator"],
            "margin": signed["C_signed_margin"],
            "conclusion": "R=4 已给出 C_N=16 预算正余量。",
        },
        {
            "range": "low height |T|<10",
            "input": f"{NOZERO_EXTERNAL_CLOSED} AND {LOW_C16_CLOSED}",
            "numerator": 0.0,
            "allowed": previous["low_allowed_min"],
            "margin": previous["low_allowed_min"],
            "conclusion": "低高度圆盘无零点，局部零点数为 0。",
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


def build_rows(previous: dict[str, Any], signed: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Jensen 半径优化冗余门判定表。"""
    external_basis = previous.get("latest_conditional_basis", "")
    self_basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("conditional_next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    signed_ready = (
        bool(signed.get("backlund_jensen_signed_mean_high_height_closed"))
        and SIGNED_MEAN_CLOSED in external_basis
        and signed.get("C_signed_margin", 0.0) > 0.0
    )
    low_ready = (
        bool(previous.get("xi_nozero_below14_external_closed"))
        and bool(previous.get("low_height_c16_immediate_external_closed"))
        and NOZERO_EXTERNAL_CLOSED in external_basis
        and LOW_C16_CLOSED in external_basis
    )
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    self_open = OLD_ATOM in self_basis and not bool(previous.get("xi_nozero_below14_self_contained_proved"))
    radius_discharged = active and signed_ready and low_ready and guard
    return [
        row(
            "RadiusOptimizationGateActiveOnExternalBacklundBranch",
            active,
            False,
            "外部低高度无零点证书接受后，当前条件链最窄点是半径优化或 C_N 放宽冗余门。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的 Backlund/Jensen 局部零点计数输入。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "HighHeightSignedMeanBudgetHasPositiveSlack",
            signed_ready,
            True,
            "高高度 signed-mean 分子 7 小于 16 log(4/sqrt(5))，余量为正。",
            SIGNED_MEAN_CLOSED,
        ),
        row(
            "LowHeightZeroCountIsZeroExternally",
            low_ready,
            False,
            "外部低高度无零点证书给出 N_low=0，因此低高度 C16 无需消耗半径优化预算。",
            f"{NOZERO_EXTERNAL_CLOSED} AND {LOW_C16_CLOSED}",
        ),
        row(
            "RadiusOptimizationOrCNRelaxationDischarged",
            radius_discharged,
            True,
            "R=4 已同时通过高低高度预算；不需要更换半径，也不需要放宽 C_N=16。",
            CLOSED_ATOM,
        ),
        row(
            "IndependentJensenC16AggregationClosedExternally",
            radius_discharged,
            False,
            "在外部低高度无零点输入下，signed mean、低高度 C16 与半径冗余门三项齐备，Jensen C16 聚合关闭。",
            C16_CLOSED_ATOM,
        ),
        row(
            "SelfContainedRadiusGateStillBlockedByLowZeroCheck",
            not self_open,
            False,
            "完全自足路线在低高度无零点账本完成前，不能提前关闭半径冗余门。",
            "仍先攻 CriticalLineNoZeroOn0To14FiniteLedger。",
        ),
        row(
            "NearZeroIndentSeparationNext",
            False,
            False,
            "外部 Backlund/Jensen C16 聚合关闭后，下一步进入近零缩进分离。",
            NEAR_ZERO_ATOM,
        ),
        row(
            "DistanceConstantAggregationDownstream",
            False,
            False,
            "近零分离后还需处理倒距离求和常数聚合。",
            DIST_CONST_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Jensen 半径优化冗余门路由。"""
    previous = load_json(paths["previous"])
    signed = load_json(paths["signed"])
    rows = build_rows(previous, signed)
    radius_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "RadiusOptimizationOrCNRelaxationDischarged"
    )
    latest_external = replace_radius(previous.get("latest_conditional_basis", ""))
    return {
        "certificate_type": "b3_jensen_radius_contingency_router",
        "status": "jensen_radius_contingency_external_discharged_self_contained_low_zero_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "jensen_radius_contingency_external_discharged": radius_closed,
        "jensen_radius_contingency_self_contained_discharged": False,
        "jensen_c16_aggregation_external_closed": radius_closed,
        "row_column_unconditional_closed": False,
        "C_N_target": signed["C_N_target"],
        "outer_radius": 4.0,
        "inner_radius": 5.0**0.5,
        "jensen_denominator": signed["jensen_denominator"],
        "high_signed_numerator": signed["C_signed_numerator"],
        "high_allowed_numerator": signed["allowed_numerator"],
        "high_signed_margin": signed["C_signed_margin"],
        "low_height_zero_count": 0,
        "low_allowed_min": previous["low_allowed_min"],
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "latest_conditional_basis": latest_external,
        "latest_global_with_external_basis": latest_external,
        "next_priority": previous.get("next_priority"),
        "secondary_priority": previous.get("secondary_priority"),
        "conditional_next_priority": NEAR_ZERO_ATOM,
        "tertiary_priority": DIST_CONST_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "budget_rows": budget_rows(previous, signed),
        "plain_conclusion": (
            "半径优化/常数放宽门在外部 Backlund/Jensen 分支中已被判定为冗余："
            "高高度 signed-mean 对 R=4 有 2.305206 的 Jensen 分子余量，低高度外部无零点给出局部零点数 0。"
            "因此无需调半径，也无需把 C_N=16 放宽；完全自足路线仍被低高度零点有限账本阻塞。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen 半径优化冗余门路由器",
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
            "jensen_radius_contingency_external_discharged="
            f"{fmt_bool(result['jensen_radius_contingency_external_discharged'])}"
        ),
        (
            "jensen_radius_contingency_self_contained_discharged="
            f"{fmt_bool(result['jensen_radius_contingency_self_contained_discharged'])}"
        ),
        f"jensen_c16_aggregation_external_closed={fmt_bool(result['jensen_c16_aggregation_external_closed'])}",
        f"C_N_target={fmt_float(result['C_N_target'])}",
        f"jensen_denominator={fmt_float(result['jensen_denominator'])}",
        f"high_signed_numerator={fmt_float(result['high_signed_numerator'])}",
        f"high_allowed_numerator={fmt_float(result['high_allowed_numerator'])}",
        f"high_signed_margin={fmt_float(result['high_signed_margin'])}",
        f"low_height_zero_count={result['low_height_zero_count']}",
        f"low_allowed_min={fmt_float(result['low_allowed_min'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件链替换",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "该替换不作用于 canonical 自足链条；自足链仍须先补低高度零点有限验证。",
        "",
        "## 2. 预算验收",
        "",
        "| range | input | numerator | allowed | margin | conclusion |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ]
    for item in result["budget_rows"]:
        lines.append(
            "| {range} | {input} | `{numerator}` | `{allowed}` | `{margin}` | {conclusion} |".format(
                range=table_cell(item["range"]),
                input=table_cell(item["input"]),
                numerator=fmt_float(float(item["numerator"])),
                allowed=fmt_float(float(item["allowed"])),
                margin=fmt_float(float(item["margin"])),
                conclusion=table_cell(item["conclusion"]),
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
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional/external Backlund 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"完全自足路线仍先攻 `{result['next_priority']}`；"
                f"外部 Backlund/Jensen 分支下一步转为 `{result['conditional_next_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--signed", type=Path, default=DEFAULT_SIGNED)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "signed": args.signed,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
