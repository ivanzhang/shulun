#!/usr/bin/env python3
"""Prime Matrix 终端两包突破判定路由器。

用法示例：
  python3 experiments/prime_matrix_terminal_two_package_breakthrough_router.py

输出：
  docs/monograph/prime-matrix-terminal-two-package-breakthrough-router.json
  docs/monograph/prime-matrix-terminal-two-package-breakthrough-router.md
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
DEFAULT_RECTANGLE = MONO / "prime-matrix-lowheight-rectangle-count-compression-router.json"
DEFAULT_DSTRUCTURE = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_PROMOTION_IRRED = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
DEFAULT_CANONICAL = MONO / "prime-matrix-canonical-source-self-contained-final-theorem-router.json"
DEFAULT_JSON = MONO / "prime-matrix-terminal-two-package-breakthrough-router.json"
DEFAULT_MD = MONO / "prime-matrix-terminal-two-package-breakthrough-router.md"

ANALYTIC_PACKAGE = "DeepExplicitPNTMertensPackage"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
FINITE_LOWHEIGHT = "RiemannSiegelIntervalArithmetic0To14Ledger"
TURING_LOWHEIGHT = "TuringArgumentPrincipleBoxCount0To14Ledger"
RECTANGLE_COUNT = "LowHeightXiRectangleZeroCountZero0To14Ledger"
INDENT_ESCAPE = "BacklundZeroAvoidingShiftWithoutJumpLedger"
INDENT_CANCEL = "BacklundNearZeroJumpCancellationSubHalfLedger"


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
    lane: str,
    closed: bool,
    author_side_provable: bool,
    evidence: str,
    meaning: str,
    next_action: str,
) -> dict[str, Any]:
    """构造终端两包判定行。"""
    return {
        "lane": lane,
        "closed": closed,
        "author_side_provable": author_side_provable,
        "evidence": evidence,
        "meaning": meaning,
        "next_action": next_action,
    }


def build_rows(
    three_input: dict[str, Any],
    lowheight: dict[str, Any],
    rectangle: dict[str, Any],
    dstructure: dict[str, Any],
    promotion_irred: dict[str, Any],
    canonical: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成终端两包判定表。"""
    analytic_active = ANALYTIC_PACKAGE in three_input.get("strict_open_packages", [])
    lowheight_pinned = (
        lowheight.get("status") == "lowheight_backlund_self_contained_package_open_exact_tasks_pinned"
    )
    rectangle_compressed = rectangle.get("compression_closed") is True
    lowheight_closed = lowheight.get("strict_package_closed") is True

    dstructure_active = DSTRUCTURE_GATE in three_input.get("strict_open_packages", [])
    dstructure_boundary_closed = dstructure.get("promotion_package_boundary_closed") is True
    dstructure_accepted = dstructure.get("promotion_package_independently_accepted") is True
    promotion_irreducible = promotion_irred.get("promotion_author_packet_sealed") is True

    canonical_closed = canonical.get("canonical_source_self_contained_theorem_closed") is True

    return [
        row(
            "CanonicalSourceSelfContainedBoundary",
            canonical_closed,
            True,
            "canonical-source final theorem router",
            "canonical-source 自足命题已经闭合；它不是 unrestricted/global 行列定理。",
            "保持边界，不把该结论偷换成全局无条件定理。",
        ),
        row(
            "AnalyticPNTMertensPackage",
            analytic_active and lowheight_closed,
            True,
            "three-input attack + lowheight Backlund package routers",
            (
                "解析包已压到低高度 xi 矩形计数证书和 Backlund 凹口成本替代；"
                "这是仍可继续数学攻坚的包。"
            ),
            (
                f"优先构造 {RECTANGLE_COUNT}；"
                f"并行寻找 {INDENT_ESCAPE} 或 {INDENT_CANCEL}。"
            ),
        ),
        row(
            "LowHeightRectangleCountCompression",
            rectangle_compressed,
            True,
            "lowheight rectangle count compression router",
            "临界线有限账本与离线 Turing 账本已被一个 xi 矩形零点计数为 0 的单原子支配。",
            f"补 {RECTANGLE_COUNT} 的区间求值、边界非零和 winding=0 证书。",
        ),
        row(
            "AnalyticExternalBypass",
            False,
            False,
            "lowheight Backlund package router",
            "外部零点表/Backlund/Dusart 可以给条件闭合，但不构成严格自足证明。",
            "若采用外部路线，必须显式标注为 conditional/external。",
        ),
        row(
            "DStructureRankinPromotionPackage",
            dstructure_active and dstructure_accepted,
            False,
            "DStructure/Rankin promotion acceptance + irreducibility routers",
            (
                "该包边界与作者侧证据已完成，但独立验收不是作者侧可生成的数学步骤；"
                "它是晋级门，不是可内部证明的普通引理。"
            ),
            "等待或取得独立验收；作者侧只能补强可复现归档和审查清单。",
        ),
        row(
            "PromotionAuthorDossierBoundary",
            dstructure_boundary_closed and promotion_irreducible,
            True,
            "DStructure/Rankin acceptance + final promotion irreducibility routers",
            "作者侧可完成的是边界、清单、证据包、pass-or-return 与不可自审升级纪律。",
            "继续完善归档，但不能把它登记为独立接受。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行终端两包突破判定。"""
    three_input = load_json(paths["three_input"])
    lowheight = load_json(paths["lowheight"])
    rectangle = load_json(paths["rectangle"])
    dstructure = load_json(paths["dstructure"])
    promotion_irred = load_json(paths["promotion_irred"])
    canonical = load_json(paths["canonical"])

    rows = build_rows(three_input, lowheight, rectangle, dstructure, promotion_irred, canonical)
    global_strict_closed = all(
        item["closed"]
        for item in rows
        if item["lane"] in {"AnalyticPNTMertensPackage", "DStructureRankinPromotionPackage"}
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_terminal_two_package_breakthrough_router",
        "status": "terminal_two_packages_pinned_global_strict_closure_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "canonical_source_self_contained_closed": rows[0]["closed"],
        "analytic_package_strictly_closed": rows[1]["closed"],
        "dstructure_package_independently_accepted": rows[3]["closed"],
        "row_column_global_strict_self_contained_closed": global_strict_closed,
        "irreducible_terminal_packages": [
            ANALYTIC_PACKAGE,
            DSTRUCTURE_GATE,
        ],
        "next_best_math_target": RECTANGLE_COUNT
        if rectangle.get("compression_closed") is True
        else FINITE_LOWHEIGHT,
        "fallback_math_target": f"{FINITE_LOWHEIGHT} AND {TURING_LOWHEIGHT}",
        "next_best_structural_target": f"{INDENT_ESCAPE} OR {INDENT_CANCEL}",
        "non_author_side_event": DSTRUCTURE_GATE,
        "closure_decision": (
            "严格全局自足闭合需要同时完成解析包和 DStructure/Rankin 独立验收。"
            "解析包仍是数学证明任务；DStructure/Rankin 是独立验收事件，作者侧不能单方面闭合。"
        ),
        "plain_conclusion": (
            "最后两包已经被判定到终端形态：解析包可继续攻有限低高度零点证书与 Backlund 凹口抵消；"
            "DStructure/Rankin 包不是隐藏数学引理，而是独立验收门。"
            "因此下一步真正可攻的数学最窄点是低高度 xi 矩形零点计数单证书；"
            "全局严格自足闭合仍开放。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 终端两包突破判定路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"canonical_source_self_contained_closed={fmt_bool(result['canonical_source_self_contained_closed'])}",
        f"analytic_package_strictly_closed={fmt_bool(result['analytic_package_strictly_closed'])}",
        f"dstructure_package_independently_accepted={fmt_bool(result['dstructure_package_independently_accepted'])}",
        (
            "row_column_global_strict_self_contained_closed="
            f"{fmt_bool(result['row_column_global_strict_self_contained_closed'])}"
        ),
        "```",
        "",
        "## 1. 闭合判定",
        "",
        result["closure_decision"],
        "",
        "## 2. 判定表",
        "",
        "| lane | closed | author-side provable | evidence | meaning | next action |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{lane}` | `{closed}` | `{provable}` | {evidence} | {meaning} | {next_action} |".format(
                lane=table_cell(item["lane"]),
                closed=fmt_bool(item["closed"]),
                provable=fmt_bool(item["author_side_provable"]),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                next_action=table_cell(item["next_action"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"数学主攻点：`{result['next_best_math_target']}`。",
            f"结构并行点：`{result['next_best_structural_target']}`。",
            f"非作者侧事件：`{result['non_author_side_event']}`。",
            "",
            "判定：现在不应再把目标在大包之间反复切换；解析包走有限低高度证书，晋级包走独立验收。",
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
    parser.add_argument("--rectangle-json", type=Path, default=DEFAULT_RECTANGLE)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--promotion-irred-json", type=Path, default=DEFAULT_PROMOTION_IRRED)
    parser.add_argument("--canonical-json", type=Path, default=DEFAULT_CANONICAL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "three_input": args.three_input_json,
        "lowheight": args.lowheight_json,
        "rectangle": args.rectangle_json,
        "dstructure": args.dstructure_json,
        "promotion_irred": args.promotion_irred_json,
        "canonical": args.canonical_json,
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
    print(result["next_best_math_target"])


if __name__ == "__main__":
    main()
