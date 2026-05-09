#!/usr/bin/env python3
"""Prime Matrix B=3 psi_0 fixed-T 零点缩进路由器。

用法示例：
  python3 experiments/prime_matrix_b3_psi0_fixed_height_indentation_router.py

输出：
  docs/monograph/prime-matrix-b3-psi0-fixed-height-indentation-router.json
  docs/monograph/prime-matrix-b3-psi0-fixed-height-indentation-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zeta-logder-contour-shift-router.json"
DEFAULT_BACKLUND = DOCS / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_INTERNAL = DOCS / "prime-matrix-backlund-internal-proof-obligation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-psi0-fixed-height-indentation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-psi0-fixed-height-indentation-router.md"

FIXED_T_ATOM = "Psi0FixedHeightZeroProximityIndentationCostLedger"
HORIZONTAL_ATOM = "Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger"
GOOD_HEIGHT_ATOM = "Psi0GoodHeightTStarAveragingContourShiftLedger"
INTERNAL_BACKLUND = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
EXTERNAL_BACKLUND = "ClassicalBacklundZeroIndentationCostExternalAccepted"
OLD_BACKLUND = "BacklundZeroProximityIndentationCostLedger"
CONTOUR_ATOM = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"

NAIVE_ZERO_COUNT_COEFFICIENT = 16.0
NAIVE_PER_ZERO_JUMP = math.pi
NAIVE_FIXED_T_JUMP_COEFFICIENT = NAIVE_ZERO_COUNT_COEFFICIENT * NAIVE_PER_ZERO_JUMP


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据文件。"""
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


def fixed_t_self_replacement() -> str:
    """fixed-T 自足路线的替换原子。"""
    return INTERNAL_BACKLUND


def fixed_t_external_replacement() -> str:
    """fixed-T 外部路线的替换原子。"""
    return EXTERNAL_BACKLUND


def replace_fixed_t(text: str, replacement: str) -> str:
    """替换 fixed-T 零点缩进原子。"""
    return text.replace(FIXED_T_ATOM, replacement)


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def local_equivalence_map() -> list[dict[str, str]]:
    """说明 psi_0 fixed-T 与 Backlund 缩进的局部等价。"""
    return [
        {
            "psi0_object": "水平边 integral of -zeta'/zeta(s) x^s/s at Im(s)=T",
            "backlund_object": "固定高度附近 arg zeta / log-derivative 的避零缩进",
            "common_formal_unit": "若 rho=beta+i gamma 且 gamma 接近 T，则 -zeta'/zeta(s) 含 m/(s-rho) 主部。",
        },
        {
            "psi0_object": "固定 T 不允许改成 T* 时，水平边可能穿过或贴近零点。",
            "backlund_object": "Backlund 矩形边界也必须处理边界零点和近边界零点。",
            "common_formal_unit": "端点极限只给定义，不给 uniform jump budget。",
        },
        {
            "psi0_object": "绕开 rho 的小凹口积分成本进入 finite-T Perron 余项。",
            "backlund_object": "绕开 rho 的小凹口/branch jump 成本进入 S(T) 或 RVM 常数。",
            "common_formal_unit": "未配对正成本都归入同一近零缩进账本。",
        },
    ]


def build_rows(previous: dict[str, Any], backlund: dict[str, Any], internal: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 fixed-T 缩进判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == FIXED_T_ATOM and FIXED_T_ATOM in basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    external_ready = backlund.get("zero_proximity_indentation_cost_external_closed") is True
    self_open = backlund.get("zero_proximity_indentation_cost_self_contained_closed") is False
    internal_named = internal.get("strict_self_contained_unique_remaining") == INTERNAL_BACKLUND
    old_equivalent = internal.get("equivalent_old_remaining") == OLD_BACKLUND
    formal_match = active and guard and internal_named and old_equivalent
    singular_obstruction = active and guard
    return [
        row(
            "Psi0FixedTIndentGateActive",
            active,
            True,
            "上一层轮廓移线已把 fixed-T 缺口定位为水平边贴近零点的缩进成本。",
            FIXED_T_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析输入，不使用真实零行缺席或数值实验替代证明。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FixedTSingularityObstructionRecorded",
            singular_obstruction,
            True,
            "若零点高度等于或任意贴近 T，水平边上的 -zeta'/zeta 有极点主部；端点避零 convention 不能给统一成本。",
            f"{INTERNAL_BACKLUND} OR {EXTERNAL_BACKLUND}",
        ),
        row(
            "FormalUnitMatchesBacklundIndentation",
            formal_match,
            True,
            "psi_0 fixed-T 凹口与 Backlund 边界凹口使用同一局部 Laurent 主部、同一避零小弧和同一 jump budget。",
            INTERNAL_BACKLUND,
        ),
        row(
            "NaivePerZeroJumpBudgetRejected",
            NAIVE_FIXED_T_JUMP_COEFFICIENT > 1.0,
            True,
            "按 C_N=16 个零点逐个付 pi 级跳变会产生约 50.265 的系数，不能作为本项目小余量闭合。",
            INTERNAL_BACKLUND,
        ),
        row(
            "ExternalBacklundIndentTransfersConditionally",
            external_ready,
            False,
            "若接受经典 Backlund 零点缩进外部引理，fixed-T 缩进成本本身可在条件路线中关闭。",
            EXTERNAL_BACKLUND,
        ),
        row(
            "SelfContainedBacklundIndentStillOpen",
            self_open and internal_named,
            True,
            "严格自足路线没有新逃逸口：该 fixed-T 缺口回流到经典 Backlund 缩进内部证明。",
            INTERNAL_BACKLUND,
        ),
        row(
            FIXED_T_ATOM,
            False,
            False,
            "作者侧严格自足版未闭合；本步只完成原子等价和条件外部转接。",
            f"{INTERNAL_BACKLUND} OR {EXTERNAL_BACKLUND}",
        ),
        row(
            "Psi0ContourShiftStillNeedsHorizontalBound",
            False,
            False,
            "即使外部缩进成本被接受，完整 zeta 对数导数轮廓移线仍需水平边 away-from-zero 显式上界。",
            HORIZONTAL_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 fixed-T 缩进路由。"""
    previous = load_json(paths["previous"])
    backlund = load_json(paths["backlund"])
    internal = load_json(paths["internal"])
    rows = build_rows(previous, backlund, internal)
    reduced = next(item["closed"] for item in rows if item["gate"] == "FormalUnitMatchesBacklundIndentation")
    external_closed = next(item["closed"] for item in rows if item["gate"] == "ExternalBacklundIndentTransfersConditionally")
    self_closed = False
    latest_self = replace_fixed_t(previous.get("latest_self_contained_basis", ""), fixed_t_self_replacement())
    latest_external_fixed_t = replace_fixed_t(
        previous.get("latest_self_contained_basis", ""),
        fixed_t_external_replacement(),
    )
    return {
        "certificate_type": "b3_psi0_fixed_height_indentation_router",
        "status": "psi0_fixed_t_indentation_reduced_to_backlund_self_open_external_ready",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "psi0_fixed_t_indentation_reduced_to_backlund": reduced,
        "psi0_fixed_t_indentation_self_contained_closed": self_closed,
        "psi0_fixed_t_indentation_external_closed": external_closed,
        "zeta_logder_contour_shift_closed": False,
        "row_column_unconditional_closed": False,
        "naive_fixed_t_jump_coefficient": NAIVE_FIXED_T_JUMP_COEFFICIENT,
        "replacement_self_contained": {FIXED_T_ATOM: fixed_t_self_replacement()},
        "replacement_external": {FIXED_T_ATOM: fixed_t_external_replacement()},
        "latest_self_contained_basis": latest_self,
        "latest_external_fixed_t_basis": latest_external_fixed_t,
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": INTERNAL_BACKLUND,
        "conditional_next_priority": HORIZONTAL_ATOM,
        "alternative_priority": GOOD_HEIGHT_ATOM,
        "post_horizontal_priority": ZERO_SUM_ATOM,
        "contour_shift_atom": CONTOUR_ATOM,
        "local_equivalence_map": local_equivalence_map(),
        "plain_conclusion": (
            "`Psi0FixedHeightZeroProximityIndentationCostLedger` 不是新的独立剩余。"
            "在固定 T 合同下，它与经典 Backlund 近零缩进成本属于同一 formal unit："
            "都要处理水平/矩形边界贴近零点时的局部极点主部、小弧缩进和 jump budget。"
            "因此严格自足路线回流到 `ClassicalBacklundZeroIndentationCostInternalProofLedger`；"
            "若接受外部 `ClassicalBacklundZeroIndentationCostExternalAccepted`，fixed-T 缩进成本可条件关闭，"
            "但完整 `psi_0` 轮廓移线还必须继续证明水平边 away-from-zero 的显式 log-derivative 上界。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    self_repl = next(iter(result["replacement_self_contained"].items()))
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 psi_0 fixed-T 零点缩进路由器",
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
            "psi0_fixed_t_indentation_reduced_to_backlund="
            f"{fmt_bool(result['psi0_fixed_t_indentation_reduced_to_backlund'])}"
        ),
        (
            "psi0_fixed_t_indentation_self_contained_closed="
            f"{fmt_bool(result['psi0_fixed_t_indentation_self_contained_closed'])}"
        ),
        (
            "psi0_fixed_t_indentation_external_closed="
            f"{fmt_bool(result['psi0_fixed_t_indentation_external_closed'])}"
        ),
        f"zeta_logder_contour_shift_closed={fmt_bool(result['zeta_logder_contour_shift_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"naive_fixed_t_jump_coefficient={fmt_float(result['naive_fixed_t_jump_coefficient'])}",
        "```",
        "",
        "## 1. 原子替换",
        "",
        "严格自足 fixed-T 路线：",
        "",
        "```text",
        self_repl[0],
        "  =>",
        self_repl[1],
        "```",
        "",
        "外部 Backlund 条件路线：",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "## 2. 局部等价",
        "",
        "| psi0 object | Backlund object | common formal unit |",
        "| --- | --- | --- |",
    ]
    for item in result["local_equivalence_map"]:
        lines.append(
            "| {psi0} | {backlund} | {unit} |".format(
                psi0=table_cell(item["psi0_object"]),
                backlund=table_cell(item["backlund_object"]),
                unit=table_cell(item["common_formal_unit"]),
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
            "fixed-T 严格自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "接受外部 Backlund 缩进后的 fixed-T 条件输入基：",
            "",
            "```text",
            result["latest_external_fixed_t_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"严格自足路线继续攻 `{result['next_priority']}`；"
                f"若接受外部 Backlund 缩进，则下一步攻 `{result['conditional_next_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--backlund", type=Path, default=DEFAULT_BACKLUND)
    parser.add_argument("--internal", type=Path, default=DEFAULT_INTERNAL)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "backlund": args.backlund,
        "internal": args.internal,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
