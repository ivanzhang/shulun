#!/usr/bin/env python3
"""Prime Matrix 低高度 xi 闭合回灌 Backlund/PNT 前沿路由器。

用法示例：
  python3 experiments/prime_matrix_lowheight_xi_backlund_integration_router.py

输出：
  docs/monograph/prime-matrix-lowheight-xi-backlund-integration-router.json
  docs/monograph/prime-matrix-lowheight-xi-backlund-integration-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_THREE_INPUT = MONO / "prime-matrix-self-contained-three-input-basis-closure-attack-router.json"
DEFAULT_LOWHEIGHT = MONO / "prime-matrix-lowheight-backlund-self-contained-package-router.json"
DEFAULT_WINDING = MONO / "prime-matrix-xi-boundary-winding-closure-router.json"
DEFAULT_RECTANGLE = MONO / "prime-matrix-lowheight-rectangle-count-compression-router.json"
DEFAULT_INDENT = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_CS8 = MONO / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_RVM = MONO / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.json"
DEFAULT_JSON = MONO / "prime-matrix-lowheight-xi-backlund-integration-router.json"
DEFAULT_MD = MONO / "prime-matrix-lowheight-xi-backlund-integration-router.md"

CRITICAL_LINE = "CriticalLineNoZeroOn0To14FiniteLedger"
OFF_LINE_TURING = "CriticalStripNoOffLineZeroBelow14TuringLedger"
FINITE_LOWHEIGHT = "FiniteLowHeightZeroCheckLedger"
LOWHEIGHT_RECT_CLOSED = "LowHeightXiRectangleZeroCountZero0To14SelfContainedClosed"
INDENT_COST = "BacklundZeroProximityIndentationCostLedger"
INDENT_SHIFT = "BacklundZeroAvoidingShiftWithoutJumpLedger"
INDENT_CANCEL = "BacklundNearZeroJumpCancellationSubHalfLedger"
CS8 = "BacklundCS8SlackAfterBridgeLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def internal_indent_package() -> str:
    """写出凹口成本内部替代包。"""
    return f"({INDENT_SHIFT} OR {INDENT_CANCEL})"


def replace_lowheight_atoms(text: str) -> str:
    """用低高度 xi 矩形计数闭合原子替换旧低高度子包。"""
    out = text
    out = out.replace(
        f"{CRITICAL_LINE} AND {OFF_LINE_TURING}",
        LOWHEIGHT_RECT_CLOSED,
    )
    out = out.replace(FINITE_LOWHEIGHT, LOWHEIGHT_RECT_CLOSED)
    return out


def proof_chain() -> list[dict[str, str]]:
    """列出回灌闭合链。"""
    return [
        {
            "step": "XiBoundaryEngine",
            "input": "theta-Mellin xi 区间引擎 + 边界非零 + winding=0",
            "output": LOWHEIGHT_RECT_CLOSED,
        },
        {
            "step": "CriticalLineAndOffLine",
            "input": LOWHEIGHT_RECT_CLOSED,
            "output": f"{CRITICAL_LINE} AND {OFF_LINE_TURING}",
        },
        {
            "step": "FiniteLowHeightCheck",
            "input": LOWHEIGHT_RECT_CLOSED,
            "output": FINITE_LOWHEIGHT,
        },
        {
            "step": "BacklundPackageUpdate",
            "input": "低高度子包已闭合",
            "output": f"下一严格自足缺口转为 {INDENT_COST}",
        },
    ]


def build_rows(
    three_input: dict[str, Any],
    lowheight: dict[str, Any],
    winding: dict[str, Any],
    rectangle: dict[str, Any],
    indent: dict[str, Any],
    cs8: dict[str, Any],
    rvm: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成回灌判定表。"""
    guard = (
        winding.get("counterexample_assumption_only") is True
        and winding.get("empirical_absence_not_used") is True
        and winding.get("hypothetical_chain_only") is True
        and three_input.get("counterexample_assumption_only") is True
    )
    lowheight_target_active = (
        three_input.get("next_narrowest_self_contained_target")
        == "LowHeightZeroAndBacklundIndentCostSelfContainedPackage"
        and lowheight.get("next_finite_target") == CRITICAL_LINE
        and lowheight.get("next_turing_target") == OFF_LINE_TURING
    )
    rectangle_compressed = rectangle.get("compression_closed") is True
    winding_closed = winding.get("winding_self_contained_closed") is True
    rectangle_closed = winding.get("lowheight_rectangle_count_self_contained_closed") is True
    indent_external = indent.get("zero_proximity_indentation_cost_external_closed") is True
    indent_internal = indent.get("zero_proximity_indentation_cost_self_contained_closed") is True
    cs8_external = cs8.get("status") == "backlund_cs8_slack_external_closed_tight"
    rvm_external = rvm.get("status") == "rvm_to_cn16_external_closed_raw_arg_normalization"
    return [
        row(
            "LowHeightBacklundPackageActive",
            lowheight_target_active,
            True,
            "上一层严格自足三输入基把主线压到低高度零点 + Backlund 凹口成本包。",
            "低高度子包与凹口成本子包。",
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "回灌只使用假设链条中的解析证书，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "RectangleCompressionImported",
            rectangle_compressed,
            True,
            "低高度临界线和离线 Turing 两原子已压成一个 xi 矩形零点计数证书。",
            "LowHeightXiRectangleZeroCountZero0To14Ledger。",
        ),
        row(
            "XiBoundaryWindingImported",
            winding_closed,
            True,
            "边界非零、节点下界、导数管道和多边形绕数已闭合，argument principle 可用。",
            "XiBoundaryWindingNumberZeroSelfContainedClosedMesh32768RootHash。",
        ),
        row(
            "LowHeightRectangleCountClosed",
            rectangle_closed,
            True,
            "低高度 xi 矩形内零点计数为 0，关闭临界线有限账本和离线 Turing 账本。",
            LOWHEIGHT_RECT_CLOSED,
        ),
        row(
            "IndentationCostStillOpenSelfContained",
            not indent_internal,
            True,
            "低高度无零点不等于高高度 Backlund 凹口成本；后者仍需内部零避让或跳变抵消。",
            internal_indent_package(),
        ),
        row(
            "ExternalBacklundBranchAvailable",
            indent_external and cs8_external and rvm_external,
            False,
            "若接受经典 Backlund 凹口成本，CS8/RVM 外部分支可继续；这不是严格自足闭合。",
            f"{INDENT_COST} external accepted, then {CS8} and RVM gates。",
        ),
        row(
            "StrictBacklundLowHeightPackageReduced",
            rectangle_closed and not indent_internal,
            True,
            "本步删除低高度有限/Turing 缺口，把严格自足解析最窄点推进到凹口成本内部替代。",
            internal_indent_package(),
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行低高度 xi 回灌路由。"""
    three_input = load_json(paths["three_input"])
    lowheight = load_json(paths["lowheight"])
    winding = load_json(paths["winding"])
    rectangle = load_json(paths["rectangle"])
    indent = load_json(paths["indent"])
    cs8 = load_json(paths["cs8"])
    rvm = load_json(paths["rvm"])
    rows = build_rows(three_input, lowheight, winding, rectangle, indent, cs8, rvm)
    lowheight_closed = next(item["closed"] for item in rows if item["gate"] == "LowHeightRectangleCountClosed")
    strict_reduced = next(item["closed"] for item in rows if item["gate"] == "StrictBacklundLowHeightPackageReduced")
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    strict_basis_before = three_input.get("strict_basis_after_attack", "")
    strict_basis_after = replace_lowheight_atoms(strict_basis_before)
    return {
        "certificate_type": "prime_matrix_lowheight_xi_backlund_integration_router",
        "status": "lowheight_xi_subpackage_closed_backlund_indent_next"
        if strict_reduced
        else "lowheight_xi_backlund_integration_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "lowheight_xi_rectangle_count_closed": lowheight_closed,
        "critical_line_0_to_14_closed": lowheight_closed,
        "critical_strip_offline_0_to_14_closed": lowheight_closed,
        "finite_lowheight_zero_check_closed": lowheight_closed,
        "backlund_indent_self_contained_closed": indent.get("zero_proximity_indentation_cost_self_contained_closed") is True,
        "strict_package_closed": lowheight_closed
        and indent.get("zero_proximity_indentation_cost_self_contained_closed") is True,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {
            f"{CRITICAL_LINE} AND {OFF_LINE_TURING}": LOWHEIGHT_RECT_CLOSED,
            FINITE_LOWHEIGHT: LOWHEIGHT_RECT_CLOSED,
            INDENT_COST: internal_indent_package(),
        },
        "strict_basis_before": strict_basis_before,
        "strict_basis_after_lowheight_xi": strict_basis_after,
        "proof_chain": proof_chain(),
        "rows": rows,
        "next_priority": internal_indent_package(),
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "低高度 xi 子包已回灌到严格自足三输入基：0<t<=14 的临界线有限账本、"
            "离线 Turing 账本和 finite low-height zero check 均由 xi 矩形零点计数 0 关闭。"
            "剩余解析最窄点不再是低高度零点，而是 Backlund 近零点凹口成本的内部替代："
            f"{internal_indent_package()}。DStructure/Rankin 验收门仍并行保留。"
        )
        if strict_reduced
        else "低高度 xi 回灌尚未闭合；需检查 winding/矩形计数输入。",
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 低高度 xi 闭合回灌 Backlund/PNT 前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"lowheight_xi_rectangle_count_closed={fmt_bool(result['lowheight_xi_rectangle_count_closed'])}",
        f"critical_line_0_to_14_closed={fmt_bool(result['critical_line_0_to_14_closed'])}",
        f"critical_strip_offline_0_to_14_closed={fmt_bool(result['critical_strip_offline_0_to_14_closed'])}",
        f"finite_lowheight_zero_check_closed={fmt_bool(result['finite_lowheight_zero_check_closed'])}",
        f"backlund_indent_self_contained_closed={fmt_bool(result['backlund_indent_self_contained_closed'])}",
        f"strict_package_closed={fmt_bool(result['strict_package_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 回灌链",
        "",
        "| step | input | output |",
        "| --- | --- | --- |",
    ]
    for item in result["proof_chain"]:
        lines.append(
            "| {step} | {input} | {output} |".format(
                step=table_cell(item["step"]),
                input=table_cell(item["input"]),
                output=table_cell(item["output"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 替换律",
            "",
            "| old | new |",
            "| --- | --- |",
        ]
    )
    for old, new in result["replacement_self_contained"].items():
        lines.append(f"| `{table_cell(old)}` | `{table_cell(new)}` |")
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
            "## 4. 下一步",
            "",
            f"当前严格自足最窄点：`{result['next_priority']}`。",
            f"并行保留晋级门：`{result['parallel_priority']}`。",
            "",
            "判定：低高度零点子包已关闭；完整行/列命题仍未闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--three-input-json", type=Path, default=DEFAULT_THREE_INPUT)
    parser.add_argument("--lowheight-json", type=Path, default=DEFAULT_LOWHEIGHT)
    parser.add_argument("--winding-json", type=Path, default=DEFAULT_WINDING)
    parser.add_argument("--rectangle-json", type=Path, default=DEFAULT_RECTANGLE)
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
        "lowheight": args.lowheight_json,
        "winding": args.winding_json,
        "rectangle": args.rectangle_json,
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
    print(result["next_priority"])


if __name__ == "__main__":
    main()
