#!/usr/bin/env python3
"""Prime Matrix 严格自足三输入基攻坚路由器。

用法示例：
  python3 experiments/prime_matrix_self_contained_three_input_basis_closure_attack_router.py

输出：
  docs/monograph/prime-matrix-self-contained-three-input-basis-closure-attack-router.json
  docs/monograph/prime-matrix-self-contained-three-input-basis-closure-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_FRONTIER = MONO / "prime-matrix-self-contained-final-frontier-consolidation-router.json"
DEFAULT_CANONICAL = MONO / "prime-matrix-canonical-terminal-promotion-closure-router.json"
DEFAULT_B3_ANCHOR = MONO / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json"
DEFAULT_MERTENS = MONO / "prime-matrix-b3-self-contained-mertens-tail-router.json"
DEFAULT_ZERO_PROXIMITY = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_DSTRUCTURE = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = MONO / "prime-matrix-self-contained-three-input-basis-closure-attack-router.json"
DEFAULT_MD = MONO / "prime-matrix-self-contained-three-input-basis-closure-attack-router.md"

NO_HIDDEN = "NoFurtherCanonicalSourceTerminalPromotionGap"
B3_MERTENS = "B3PrimeHarmonicMertensUniformEnvelopePGe100000"
B3_VARIATION = "B3BoundaryVariationOnePercentTransferLedger"
SELF_DSTRUCTURE_OLD = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

PNT_PACKAGE = "SelfContainedPrimeReciprocalMertensTailXGe20000"


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
    item: str,
    attacked: bool,
    strictly_proved: bool,
    evidence: str,
    conclusion: str,
    remaining: str,
) -> dict[str, Any]:
    """构造三输入基攻坚状态行。"""
    return {
        "item": item,
        "attacked": attacked,
        "strictly_proved": strictly_proved,
        "evidence": evidence,
        "conclusion": conclusion,
        "remaining": remaining,
    }


def build_rows(
    canonical: dict[str, Any],
    b3_anchor: dict[str, Any],
    mertens: dict[str, Any],
    zero_proximity: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """逐项判定严格自足三输入基。"""
    canonical_closed = (
        canonical.get("canonical_source_terminal_promotion_closed") is True
        and canonical.get("open_self_contained_gates") == []
        and canonical.get("narrowest_self_contained_boundary") == NO_HIDDEN
    )
    variation_closed_mod_mertens = (
        b3_anchor.get("b3_boundary_variation_one_percent_conditional_closed") is True
        and b3_anchor.get("next_priority") == "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
    )
    mertens_reduced_to_pnt = (
        mertens.get("status") == "self_contained_mertens_tail_reduced_to_explicit_pnt_package_open"
        and mertens.get("next_priority")
        == "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000"
    )
    analytic_frontier_deepened = (
        zero_proximity.get("status")
        == "zero_proximity_indentation_cost_external_closed_self_contained_open"
    )
    dstructure_boundary_closed = dstructure.get("promotion_package_boundary_closed") is True
    dstructure_accepted = dstructure.get("promotion_package_independently_accepted") is True

    return [
        row(
            NO_HIDDEN,
            canonical_closed,
            canonical_closed,
            "canonical terminal promotion closure",
            "canonical-source 终端晋级已无自足开门；这是已闭合边界，不再是活动输入。",
            "无；但它只覆盖 canonical-source 边界，不声明 unrestricted/global 定理。",
        ),
        row(
            f"{B3_MERTENS} AND {B3_VARIATION}",
            variation_closed_mod_mertens and mertens_reduced_to_pnt,
            False,
            "B3 signed-delay anchor + self-contained Mertens tail routers",
            (
                "B3BoundaryVariation 已被 20000 锚点与 BV 乘子纪律吸收；"
                "B3PrimeHarmonic/Mertens 被压成显式 PNT/Mertens 包。"
            ),
            PNT_PACKAGE,
        ),
        row(
            "DeepExplicitPNTMertensPackage",
            analytic_frontier_deepened,
            False,
            "B3 zero-proximity indentation cost router",
            (
                "显式 PNT 包已深入到 zeta/xi、Backlund/Jensen、低高度零点与轮廓常数层；"
                "外部 Backlund/Dusart 路线可旁路，但严格自足仍未闭合。"
            ),
            (
                "低高度零点/Turing 有限账本、Backlund 凹口成本或零避让抵消、"
                "C_log 聚合、PNT 轮廓常数、theta@20000 预算、B1 区间账本。"
            ),
        ),
        row(
            f"{SELF_DSTRUCTURE_OLD} / {DSTRUCTURE}",
            dstructure_boundary_closed,
            dstructure_accepted,
            "DStructure/Rankin promotion acceptance router",
            (
                "Rankin pass-or-return、D/Tail-log4/finite-verification 的作者侧边界已闭合；"
                "但独立接受仍未发生，不能由作者侧自封为无条件闭合。"
            ),
            "D-structure、Tail-log4/BG-RKS 适配、有限验证 hash、Rankin 子账本的独立验收。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行三输入基攻坚汇总。"""
    frontier = load_json(paths["frontier"])
    canonical = load_json(paths["canonical"])
    b3_anchor = load_json(paths["b3_anchor"])
    mertens = load_json(paths["mertens"])
    zero_proximity = load_json(paths["zero_proximity"])
    dstructure = load_json(paths["dstructure"])

    rows = build_rows(canonical, b3_anchor, mertens, zero_proximity, dstructure)
    strict_all_closed = all(item["strictly_proved"] for item in rows)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]

    old_basis = frontier.get("latest_strict_self_contained_basis", "")
    strict_basis_after_attack = zero_proximity.get("latest_self_contained_basis", "")
    conditional_basis = zero_proximity.get("latest_conditional_basis", "")

    return {
        "certificate_type": "prime_matrix_self_contained_three_input_basis_closure_attack_router",
        "status": "strict_three_input_basis_reduced_but_not_finally_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "old_three_input_basis": old_basis,
        "strict_basis_after_attack": strict_basis_after_attack,
        "conditional_basis_after_external_backlund_dusart": conditional_basis,
        "canonical_terminal_closed": rows[0]["strictly_proved"],
        "b3_variation_independent_atom_eliminated": rows[1]["attacked"],
        "b3_mertens_self_contained_closed": False,
        "dstructure_author_boundary_closed": rows[3]["attacked"],
        "dstructure_independently_accepted": rows[3]["strictly_proved"],
        "row_column_self_contained_closed": strict_all_closed,
        "next_narrowest_self_contained_target": "LowHeightZeroAndBacklundIndentCostSelfContainedPackage",
        "parallel_promotion_target": DSTRUCTURE,
        "strict_open_packages": [
            "DeepExplicitPNTMertensPackage",
            DSTRUCTURE,
        ],
        "atomic_open_inputs_for_next_attack": [
            "CriticalLineNoZeroOn0To14FiniteLedger",
            "CriticalStripNoOffLineZeroBelow14TuringLedger",
            "BacklundZeroProximityIndentationCostLedger",
            "BacklundCS8SlackAfterBridgeLedger",
            "ZeroFreeRegionToExplicitPNTContourConstantLedger",
            "ThetaEnvelopeTargetAt20000NumericalBudgetLedger",
            "SelfContainedMeisselMertensConstantIntervalLedgerAt20000",
            DSTRUCTURE,
        ],
        "plain_conclusion": (
            "三输入基已经被逐项攻到更窄形态：canonical 终端输入已闭合；"
            "B3 边界变差不再是独立缺口，它被 20000 锚点/BV 乘子纪律吸收到 Mertens 尾段；"
            "剩余的 B3 自足缺口是显式 PNT/Mertens 解析包。DStructure/Rankin 的作者侧边界已闭合，"
            "但独立验收未发生。因此严格全局无条件行/列命题仍未闭合。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 严格自足三输入基攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"canonical_terminal_closed={fmt_bool(result['canonical_terminal_closed'])}",
        (
            "b3_variation_independent_atom_eliminated="
            f"{fmt_bool(result['b3_variation_independent_atom_eliminated'])}"
        ),
        f"b3_mertens_self_contained_closed={fmt_bool(result['b3_mertens_self_contained_closed'])}",
        f"dstructure_author_boundary_closed={fmt_bool(result['dstructure_author_boundary_closed'])}",
        f"dstructure_independently_accepted={fmt_bool(result['dstructure_independently_accepted'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 旧三输入基",
        "",
        "```text",
        result["old_three_input_basis"],
        "```",
        "",
        "## 2. 攻坚后严格自足基",
        "",
        "```text",
        result["strict_basis_after_attack"],
        "```",
        "",
        "## 3. 外部 Backlund/Dusart 条件基",
        "",
        "```text",
        result["conditional_basis_after_external_backlund_dusart"],
        "```",
        "",
        "## 4. 三输入逐项判定",
        "",
        "| item | attacked | strictly proved | evidence | conclusion | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{item}` | `{attacked}` | `{proved}` | {evidence} | {conclusion} | {remaining} |".format(
                item=table_cell(item["item"]),
                attacked=fmt_bool(item["attacked"]),
                proved=fmt_bool(item["strictly_proved"]),
                evidence=table_cell(item["evidence"]),
                conclusion=table_cell(item["conclusion"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 下一步最窄目标",
            "",
            f"主线先攻 `{result['next_narrowest_self_contained_target']}`。",
            f"并行保留 `{result['parallel_promotion_target']}` 晋级验收门。",
            "",
            "当前原子级开放输入：",
            "",
        ]
    )
    for item in result["atomic_open_inputs_for_next_attack"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "判定：严格自足路线已经从“三项输入基”推进到“显式 PNT/Mertens 包 + DStructure/Rankin 验收门”。"
            "这是真实缩窄，不是最终闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frontier-json", type=Path, default=DEFAULT_FRONTIER)
    parser.add_argument("--canonical-json", type=Path, default=DEFAULT_CANONICAL)
    parser.add_argument("--b3-anchor-json", type=Path, default=DEFAULT_B3_ANCHOR)
    parser.add_argument("--mertens-json", type=Path, default=DEFAULT_MERTENS)
    parser.add_argument("--zero-proximity-json", type=Path, default=DEFAULT_ZERO_PROXIMITY)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "frontier": args.frontier_json,
        "canonical": args.canonical_json,
        "b3_anchor": args.b3_anchor_json,
        "mertens": args.mertens_json,
        "zero_proximity": args.zero_proximity_json,
        "dstructure": args.dstructure_json,
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
    print(result["next_narrowest_self_contained_target"])


if __name__ == "__main__":
    main()
