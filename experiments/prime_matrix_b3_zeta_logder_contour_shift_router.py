#!/usr/bin/env python3
"""Prime Matrix B=3 psi_0 zeta 对数导数轮廓移线路由器。

用法示例：
  python3 experiments/prime_matrix_b3_zeta_logder_contour_shift_router.py

输出：
  docs/monograph/prime-matrix-b3-zeta-logder-contour-shift-router.json
  docs/monograph/prime-matrix-b3-zeta-logder-contour-shift-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-right-edge-perron-kernel-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-zeta-logder-contour-shift-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-zeta-logder-contour-shift-router.md"

OLD_ATOM = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
RESIDUE_ATOM = "Psi0ContourResidueAndLeftEdgeClosed"
GOOD_HEIGHT_ATOM = "Psi0GoodHeightTStarAveragingContourShiftLedger"
FIXED_T_ATOM = "Psi0FixedHeightZeroProximityIndentationCostLedger"
HORIZONTAL_ATOM = "Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
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


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replacement_pair() -> str:
    """写出轮廓移线替换包。"""
    return (
        f"({RESIDUE_ATOM} AND {HORIZONTAL_ATOM} AND "
        f"({FIXED_T_ATOM} OR {GOOD_HEIGHT_ATOM}))"
    )


def replace_atom(text: str) -> str:
    """替换轮廓移线原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


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
    """生成 zeta 对数导数轮廓移线判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    right_kernel_ready = bool(previous.get("right_edge_perron_kernel_closed"))
    analytic_basis_ready = "CompletedZetaXiFunctionalEquationAndHadamardProductClosed" in basis
    residue_closed = active and guard and right_kernel_ready and analytic_basis_ready
    horizontal_closed = False
    fixed_t_closed = False
    good_height_closed = False
    reduced = residue_closed
    closed = residue_closed and horizontal_closed and (fixed_t_closed or good_height_closed)
    return [
        row(
            "ContourShiftGateActive",
            active,
            False,
            "右边 Perron 核已闭合后，当前最窄点是把右边竖线积分移线成零点留数。",
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
            "ResidueAndLeftEdgeClosed",
            residue_closed,
            True,
            "留数清单与左边界衰减已由内部 psi_0 精确公式吸收；这里不再重复付费。",
            RESIDUE_ATOM,
        ),
        row(
            "HorizontalLogDerivativeBoundMissing",
            horizontal_closed,
            False,
            "还缺避开零点后的水平边 -zeta'/zeta 显式上界。",
            HORIZONTAL_ATOM,
        ),
        row(
            "FixedHeightZeroProximityCostMissing",
            fixed_t_closed,
            False,
            "若坚持固定 T 截断，必须支付 T 附近零点贴近水平边的缩进/近零成本。",
            FIXED_T_ATOM,
        ),
        row(
            "GoodHeightTStarAlternativeOpen",
            good_height_closed,
            False,
            "若允许改成 T* in [T,2T]，可走平均好高度路线，但这会改变当前 fixed-T 合同。",
            GOOD_HEIGHT_ATOM,
        ),
        row(
            "ContourShiftReducedToFixedTOrGoodHeight",
            reduced,
            False,
            "轮廓移线原子已压成留数左边界、水平边 log-derivative、固定 T 缩进或好高度替代。",
            replacement_pair(),
        ),
        row(
            OLD_ATOM,
            closed,
            False,
            "当前 fixed-T 轮廓移线未闭合；缺口是水平边 log-derivative 和零点贴近成本。",
            replacement_pair(),
        ),
        row(
            ZERO_SUM_ATOM,
            False,
            False,
            "轮廓移线闭合后，才进入零点自由区下的零点和数值预算。",
            ZERO_SUM_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 zeta 对数导数轮廓移线路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ContourShiftReducedToFixedTOrGoodHeight"
    )
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_zeta_logder_contour_shift_router",
        "status": "zeta_logder_contour_shift_reduced_fixed_t_gap_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zeta_logder_contour_shift_reduced": reduced,
        "zeta_logder_contour_shift_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": FIXED_T_ATOM,
        "secondary_priority": HORIZONTAL_ATOM,
        "alternative_priority": GOOD_HEIGHT_ATOM,
        "post_contour_priority": ZERO_SUM_ATOM,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "plain_conclusion": (
            "轮廓移线已经压到真正缺口：留数和左边界不是问题，问题是 fixed-T 水平边可能贴近零点，"
            "必须证明固定高度缩进成本，或明确把合同改成 T* 好高度版本。当前 fixed-T 自足链未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 psi_0 zeta 对数导数轮廓移线路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"zeta_logder_contour_shift_reduced={fmt_bool(result['zeta_logder_contour_shift_reduced'])}",
        f"zeta_logder_contour_shift_closed={fmt_bool(result['zeta_logder_contour_shift_closed'])}",
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
        "## 2. 判定表",
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
            "## 3. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 4. 下一步",
            "",
            (
                f"fixed-T 自足路线先攻 `{result['next_priority']}`；"
                f"并行可攻 `{result['secondary_priority']}`。若改合同，则研究 `{result['alternative_priority']}`。"
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
