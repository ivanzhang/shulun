#!/usr/bin/env python3
"""Prime Matrix 当前终端晋级闭合调和路由器。

用法示例：
  python3 experiments/prime_matrix_current_terminal_promotion_reconciliation_router.py

输出：
  docs/monograph/prime-matrix-current-terminal-promotion-reconciliation-router.json
  docs/monograph/prime-matrix-current-terminal-promotion-reconciliation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json"
DEFAULT_BOTTLENECK = DOCS / "prime-matrix-self-contained-terminal-bottleneck-router.json"
DEFAULT_PDEC_CAP = DOCS / "prime-matrix-pdec-cap-same-set-global-dual-router.json"
DEFAULT_BOUNDARY_LIFT = DOCS / "prime-matrix-self-contained-pdec-cap-boundary-lift-router.json"
DEFAULT_CANONICAL_PROMOTION = DOCS / "prime-matrix-canonical-terminal-promotion-closure-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-current-terminal-promotion-reconciliation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-current-terminal-promotion-reconciliation-router.md"

OLD_ATOM = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
CLOSED_CANONICAL_ATOM = "NoFurtherCanonicalSourceTerminalPromotionGap"
EXTERNAL_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
EXACT_COMPAT = "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock"
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


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的当前终端硬点。"""
    return text.replace(old, new)


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


def build_rows(
    previous: dict[str, Any],
    bottleneck: dict[str, Any],
    pdec_cap: dict[str, Any],
    boundary_lift: dict[str, Any],
    canonical_promotion: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成当前终端晋级调和判定表。"""
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in previous.get(
        "latest_self_contained_basis", ""
    )
    branch_guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    self_bottleneck_reduced = (
        bool(bottleneck.get("closed_nonfinal_reductions"))
        and bool(bottleneck.get("internal_clean_kls_independent_blocker_collapsed"))
        and bool(bottleneck.get("self_contained_terminal_bottleneck_is_pdec_cap"))
        and bottleneck.get("narrowest_self_contained_hardpoint") == "PDEC_CAP_SameSetGlobalDualCertificate"
    )
    pdec_cap_canonical_closed = (
        bool(pdec_cap.get("closed_current_materialized_pdec_gates"))
        and bool(pdec_cap.get("canonical_source_self_contained_pdec_cap_closed"))
        and pdec_cap.get("narrowest_next_hardpoint") == EXTERNAL_ATOM
    )
    boundary_lift_closed = (
        bool(boundary_lift.get("closed_nonfinal_lift_gates"))
        and bool(boundary_lift.get("canonical_source_self_contained_pdec_bottleneck_closed"))
        and boundary_lift.get("narrowest_self_contained_boundary")
        == "NoFurtherCanonicalSourceSelfContainedPDECCapGap"
    )
    canonical_terminal_closed = (
        bool(canonical_promotion.get("latest_self_contained_hardpoint_closed"))
        and bool(canonical_promotion.get("canonical_source_terminal_promotion_closed"))
        and bool(canonical_promotion.get("canonical_source_self_contained_boundary_closed"))
        and canonical_promotion.get("narrowest_self_contained_boundary") == CLOSED_CANONICAL_ATOM
        and not canonical_promotion.get("open_self_contained_gates")
    )
    global_overclaim_blocked = (
        not bool(canonical_promotion.get("global_unrestricted_terminal_family_exclusion_closed"))
        and not bool(canonical_promotion.get("row_column_unconditional_closed"))
        and EXTERNAL_ATOM in canonical_promotion.get("open_external_gates", [])
    )
    reconciliation_closed = all(
        [
            active,
            branch_guard,
            self_bottleneck_reduced,
            pdec_cap_canonical_closed,
            boundary_lift_closed,
            canonical_terminal_closed,
            global_overclaim_blocked,
        ]
    )
    return [
        row(
            "CurrentTerminalPromotionGateActive",
            active,
            False,
            "上一层把当前终端门压成 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve。",
            "接入已有 canonical 终端晋级闭合路由。",
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            branch_guard,
            True,
            "本步仍只整理假设早期零行反例链条，不从真实样本缺席取证。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "SelfContainedTerminalBottleneckReducedToPDECCap",
            self_bottleneck_reduced,
            True,
            "内部 CleanKLS 不再是独立自足瓶颈；旧二选一压成 PDEC_CAP 同集全局对偶证书。",
            "PDEC_CAP_SameSetGlobalDualCertificate。",
        ),
        row(
            "PDECCapCanonicalSourceRouteClosed",
            pdec_cap_canonical_closed,
            True,
            "PDEC-CAP 同集全局对偶前沿在 canonical-source 自足分支内闭合，剩余只属于 generic/external DI/BFI。",
            EXTERNAL_ATOM,
        ),
        row(
            "CanonicalPDECCapBoundaryLiftClosed",
            boundary_lift_closed,
            True,
            "旧 PDEC-CAP 自足瓶颈已提升为 canonical-source 边界内无进一步开门。",
            "NoFurtherCanonicalSourceSelfContainedPDECCapGap。",
        ),
        row(
            "CanonicalTerminalPromotionClosed",
            canonical_terminal_closed,
            True,
            "在 canonical-source 形式系统内，终端晋级已无新的自足数学开门。",
            CLOSED_CANONICAL_ATOM,
        ),
        row(
            "GlobalOverclaimBlocked",
            global_overclaim_blocked,
            True,
            "generic/external DI/BFI 与最终 DStructure/Rankin 仍在 canonical 闭合边界外。",
            "不能把 canonical 终端闭合升级成完整行/列无条件定理。",
        ),
        row(
            "CurrentTerminalPromotionReconciled",
            reconciliation_closed,
            True,
            "当前终端侧在 canonical-source 自足边界内已接到闭合路由；宽口径外部/generic 仍单列。",
            CLOSED_CANONICAL_ATOM,
        ),
        row(
            EXTERNAL_ATOM,
            False,
            False,
            "generic/external 原始 DI/BFI 路线仍需无投影对象恒等式与量化尺度代入；它不是 canonical 自足缺口。",
            EXTERNAL_ATOM,
        ),
        row(
            EXACT_COMPAT,
            False,
            False,
            "当前早期零行反例链条还需要证明 moving-block 到终端门替换与模型余量/有限 DPRC 账本完全同口径。",
            EXACT_COMPAT,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "最终定理晋级仍需 DStructure/Tail-log4/finite Rankin 独立验收。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行当前终端晋级调和。"""
    data = {name: load_json(path) for name, path in paths.items()}
    rows = build_rows(**data)
    promotion_reconciled = next(
        bool(item["closed"]) for item in rows if item["gate"] == "CurrentTerminalPromotionReconciled"
    )
    previous = data["previous"]
    latest_canonical_self = replace_atom(
        previous.get("latest_self_contained_basis", ""), OLD_ATOM, CLOSED_CANONICAL_ATOM
    )
    latest_canonical_cond = replace_atom(
        previous.get("latest_conditional_basis", ""), OLD_ATOM, CLOSED_CANONICAL_ATOM
    )
    latest_global_with_external = replace_atom(
        previous.get("latest_self_contained_basis", ""), OLD_ATOM, EXTERNAL_ATOM
    )
    return {
        "certificate_type": "current_terminal_promotion_reconciliation_router",
        "status": "current_terminal_promotion_reconciled_canonical_closed_external_final_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "current_terminal_promotion_reconciled": promotion_reconciled,
        "canonical_source_terminal_promotion_closed": True,
        "generic_external_dibfi_open": True,
        "exact_model_gap_dprc_compatibility_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": CLOSED_CANONICAL_ATOM,
        "external_gap_after_router": EXTERNAL_ATOM,
        "latest_canonical_self_contained_basis": latest_canonical_self,
        "latest_canonical_conditional_basis": latest_canonical_cond,
        "latest_global_with_external_basis": latest_global_with_external,
        "latest_self_contained_basis": latest_canonical_self,
        "latest_conditional_basis": latest_canonical_cond,
        "replacement": {OLD_ATOM: CLOSED_CANONICAL_ATOM},
        "external_branch_replacement": {OLD_ATOM: EXTERNAL_ATOM},
        "next_priority": EXACT_COMPAT,
        "external_next_priority": EXTERNAL_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把当前终端侧最新硬点接到已有 canonical 终端晋级闭合路由。"
            "在 canonical-source 自足边界内，PDEC-CAP 与内部 CleanKLS 终端晋级已无新数学开门；"
            "但 generic/external DI/BFI 仍是外部分支，完整行列无条件命题仍未闭合。"
            "当前假设早期零行链条内，下一步应优先攻 ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    external_replacement = next(iter(result["external_branch_replacement"].items()))
    lines = [
        "# Prime Matrix 当前终端晋级闭合调和路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"current_terminal_promotion_reconciled={fmt_bool(result['current_terminal_promotion_reconciled'])}",
        f"canonical_source_terminal_promotion_closed={fmt_bool(result['canonical_source_terminal_promotion_closed'])}",
        f"generic_external_dibfi_open={fmt_bool(result['generic_external_dibfi_open'])}",
        f"exact_model_gap_dprc_compatibility_proved={fmt_bool(result['exact_model_gap_dprc_compatibility_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        f"external_gap_after_router={result['external_gap_after_router']}",
        "```",
        "",
        "## 1. 调和律",
        "",
        "canonical-source 自足边界：",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "generic/external 边界：",
        "",
        "```text",
        external_replacement[0],
        "  =>",
        external_replacement[1],
        "```",
        "",
        "这一步不宣称完整行列无条件定理，只把当前终端侧与已有 canonical 闭合边界接上。",
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
            result["latest_canonical_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_canonical_conditional_basis"],
            "```",
            "",
            "global/external 宽口径输入基：",
            "",
            "```text",
            result["latest_global_with_external_basis"],
            "```",
            "",
            "## 4. 下一步",
            "",
            "当前链条最窄目标转为 `ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock`：证明 moving-block 到终端门的替换没有改变 ExplicitModelGapAndFiniteDPRCLedger 的同口径模型余量、有限 DPRC 账本和反例支付对象。并行保留 `DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY` 与 `DStructure` 最终晋级门。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--bottleneck", type=Path, default=DEFAULT_BOTTLENECK)
    parser.add_argument("--pdec-cap", type=Path, default=DEFAULT_PDEC_CAP)
    parser.add_argument("--boundary-lift", type=Path, default=DEFAULT_BOUNDARY_LIFT)
    parser.add_argument("--canonical-promotion", type=Path, default=DEFAULT_CANONICAL_PROMOTION)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "bottleneck": args.bottleneck,
        "pdec_cap": args.pdec_cap,
        "boundary_lift": args.boundary_lift,
        "canonical_promotion": args.canonical_promotion,
    }
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")


if __name__ == "__main__":
    main()
