#!/usr/bin/env python3
"""Prime Matrix 低高度零点与 Backlund 凹口自足包路由器。

用法示例：
  python3 experiments/prime_matrix_lowheight_backlund_self_contained_package_router.py

输出：
  docs/monograph/prime-matrix-lowheight-backlund-self-contained-package-router.json
  docs/monograph/prime-matrix-lowheight-backlund-self-contained-package-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_THREE_INPUT = MONO / "prime-matrix-self-contained-three-input-basis-closure-attack-router.json"
DEFAULT_LOW_ZERO = MONO / "prime-matrix-b3-xi-nozero-below14-router.json"
DEFAULT_INDENT = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_CS8 = MONO / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_RVM = MONO / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.json"
DEFAULT_JSON = MONO / "prime-matrix-lowheight-backlund-self-contained-package-router.json"
DEFAULT_MD = MONO / "prime-matrix-lowheight-backlund-self-contained-package-router.md"

CRITICAL_LINE = "CriticalLineNoZeroOn0To14FiniteLedger"
OFF_LINE_TURING = "CriticalStripNoOffLineZeroBelow14TuringLedger"
INDENT_SHIFT = "BacklundZeroAvoidingShiftWithoutJumpLedger"
INDENT_CANCEL = "BacklundNearZeroJumpCancellationSubHalfLedger"
INDENT_COST = "BacklundZeroProximityIndentationCostLedger"
CS8 = "BacklundCS8SlackAfterBridgeLedger"
RVM_CN16 = "RVMToCN16LocalInequalityLedger"

FIRST_ZERO_REFERENCE = 14.134725141734693
HEIGHT_TARGET = 14.0
HEIGHT_MARGIN = FIRST_ZERO_REFERENCE - HEIGHT_TARGET
TURING_HEIGHT_REQUIRED = 14.0


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    proved: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def low_height_required_package() -> str:
    """写出低高度自足有限验证包。"""
    return (
        "RiemannSiegelIntervalArithmetic0To14Ledger AND "
        "CriticalLineSignSeparationFiniteLedger0To14 AND "
        "TuringArgumentPrincipleBoxCount0To14Ledger"
    )


def indentation_required_package() -> str:
    """写出凹口成本自足替代包。"""
    return f"({INDENT_SHIFT} OR {INDENT_CANCEL})"


def build_rows(
    three_input: dict[str, Any],
    low_zero: dict[str, Any],
    indent: dict[str, Any],
    cs8: dict[str, Any],
    rvm: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成低高度与凹口包判定表。"""
    next_target_matches = (
        three_input.get("next_narrowest_self_contained_target")
        == "LowHeightZeroAndBacklundIndentCostSelfContainedPackage"
    )
    external_low_zero_closed = low_zero.get("xi_nozero_below14_external_closed") is True
    self_low_zero_closed = low_zero.get("xi_nozero_below14_self_contained_proved") is True
    height_margin_positive = low_zero.get("height_margin", HEIGHT_MARGIN) > 0

    external_indent_closed = indent.get("zero_proximity_indentation_cost_external_closed") is True
    self_indent_closed = indent.get("zero_proximity_indentation_cost_self_contained_closed") is True
    naive_deficit = float(indent.get("naive_margin_deficit", math.inf))
    naive_route_blocked = naive_deficit > 0

    cs8_external_closed = cs8.get("status") == "backlund_cs8_slack_external_closed_tight"
    rvm_external_closed = rvm.get("status") == "rvm_to_cn16_external_closed_raw_arg_normalization"

    return [
        row(
            "PackageIsCurrentNarrowest",
            next_target_matches,
            next_target_matches,
            "strict three-input basis attack router",
            "三输入基收缩后，当前最窄解析包正是低高度零点 + Backlund 凹口成本。",
            "无定位剩余。",
        ),
        row(
            "ExternalLowHeightZeroCertificateAvailable",
            external_low_zero_closed and height_margin_positive,
            False,
            "B3 xi no-zero-below14 router",
            "外部首零点/Turing 证书可关闭 |Im rho|<=14 的低高度无零点输入。",
            "严格自足不能引用外部零点表作为证明主体。",
        ),
        row(
            "SelfContainedLowHeightZeroStillMissing",
            self_low_zero_closed,
            False,
            "B3 xi no-zero-below14 router",
            "仓库内还没有 Riemann-Siegel 区间算术和 Turing/argument-principle 完整账本。",
            low_height_required_package(),
        ),
        row(
            "NaiveIndentationCostRouteBlocked",
            naive_route_blocked,
            True,
            "B3 zero-proximity indentation cost router",
            (
                f"朴素凹口成本缺口为 {naive_deficit:.12f}，"
                "说明逐零点粗付不能闭合 C_S=8 预算。"
            ),
            indentation_required_package(),
        ),
        row(
            "ExternalIndentationCostAvailable",
            external_indent_closed,
            False,
            "B3 zero-proximity indentation cost router",
            "经典 Backlund 轮廓缩进可作为外部引理关闭凹口成本。",
            "严格自足仍需零避让或跳变抵消。",
        ),
        row(
            "SelfContainedIndentationCostStillMissing",
            self_indent_closed,
            False,
            "B3 zero-proximity indentation cost router",
            "当前内部材料只证明朴素路线失败，尚未证明可行的零避让/抵消替代。",
            indentation_required_package(),
        ),
        row(
            "CS8AndRVMClosedOnlyOnExternalBranch",
            cs8_external_closed and rvm_external_closed,
            False,
            "B3 CS8 slack + RVM-to-CN16 routers",
            "C_S=8 与 RVM->C_N=16 的合并在外部分支可走通，严格自足仍依赖低高度和凹口前置包。",
            f"{CS8} AND {RVM_CN16}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行低高度与 Backlund 凹口自足包路由。"""
    three_input = load_json(paths["three_input"])
    low_zero = load_json(paths["low_zero"])
    indent = load_json(paths["indent"])
    cs8 = load_json(paths["cs8"])
    rvm = load_json(paths["rvm"])
    rows = build_rows(three_input, low_zero, indent, cs8, rvm)
    strict_closed = (
        low_zero.get("xi_nozero_below14_self_contained_proved") is True
        and indent.get("zero_proximity_indentation_cost_self_contained_closed") is True
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_lowheight_backlund_self_contained_package_router",
        "status": "lowheight_backlund_self_contained_package_open_exact_tasks_pinned",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "first_zero_reference": FIRST_ZERO_REFERENCE,
        "height_target": HEIGHT_TARGET,
        "height_margin": HEIGHT_MARGIN,
        "turing_height_required": TURING_HEIGHT_REQUIRED,
        "naive_indentation_coefficient": indent.get("naive_indentation_coefficient"),
        "available_stability_margin": indent.get("available_stability_margin"),
        "naive_margin_deficit": indent.get("naive_margin_deficit"),
        "strict_package_closed": strict_closed,
        "row_column_self_contained_closed": False,
        "next_finite_target": CRITICAL_LINE,
        "next_turing_target": OFF_LINE_TURING,
        "next_structural_target": indentation_required_package(),
        "required_low_height_package": low_height_required_package(),
        "required_indentation_package": indentation_required_package(),
        "plain_conclusion": (
            "低高度-Backlund 自足包被压成两个不可再混淆的任务："
            "一是仓库内构造 0<t<=14 的 Riemann-Siegel/Turing 有限验证；"
            "二是证明近零点凹口成本存在零避让或跳变抵消。"
            "外部零点表和经典 Backlund 引理可以给条件闭合，但严格自足路线仍开放。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 低高度零点与 Backlund 凹口自足包路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"height_margin={result['height_margin']:.12f}",
        f"naive_indentation_coefficient={result['naive_indentation_coefficient']:.12f}",
        f"available_stability_margin={result['available_stability_margin']:.12f}",
        f"naive_margin_deficit={result['naive_margin_deficit']:.12f}",
        f"strict_package_closed={fmt_bool(result['strict_package_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 精确剩余包",
        "",
        "低高度有限验证包：",
        "",
        "```text",
        result["required_low_height_package"],
        "```",
        "",
        "凹口成本替代包：",
        "",
        "```text",
        result["required_indentation_package"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | evidence | meaning | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"最可执行的自足硬点是 `{result['next_finite_target']}`，随后接 `{result['next_turing_target']}`。",
            f"结构硬点并行保持为 `{result['next_structural_target']}`。",
            "",
            "判定：这一步没有闭合最终命题；它把最新剩余拆成一个有限可复核包和一个结构性抵消包。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--three-input-json", type=Path, default=DEFAULT_THREE_INPUT)
    parser.add_argument("--low-zero-json", type=Path, default=DEFAULT_LOW_ZERO)
    parser.add_argument("--indent-json", type=Path, default=DEFAULT_INDENT)
    parser.add_argument("--cs8-json", type=Path, default=DEFAULT_CS8)
    parser.add_argument("--rvm-json", type=Path, default=DEFAULT_RVM)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "three_input": args.three_input_json,
        "low_zero": args.low_zero_json,
        "indent": args.indent_json,
        "cs8": args.cs8_json,
        "rvm": args.rvm_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["next_finite_target"])


if __name__ == "__main__":
    main()
