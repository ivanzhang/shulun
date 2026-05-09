#!/usr/bin/env python3
"""Prime Matrix 终端闭合缺口直接攻坚路由器。

用法示例：
  python3 experiments/prime_matrix_terminal_closure_gap_direct_attack_router.py

输出：
  docs/monograph/prime-matrix-terminal-closure-gap-direct-attack-router.json
  docs/monograph/prime-matrix-terminal-closure-gap-direct-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_CURRENT = DOCS / "prime-matrix-final-open-input-current-attack-router.json"
DEFAULT_TAXONOMY = DOCS / "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"
DEFAULT_SELF_CONTAINED_FINAL = DOCS / "prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.json"
DEFAULT_EXTERNAL = DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
DEFAULT_PROMOTION = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-terminal-closure-gap-direct-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-terminal-closure-gap-direct-attack-router.md"

ACTUAL_SOURCE_BRIDGE = "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
EXTERNAL_CONTRACT = "AcceptFullSKLSExtExternalContract"
PRIMARY_SOURCE_PROOF = "DIBFIPrimarySourceSpecializationProof"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def row(
    gate: str,
    closed: bool,
    proved_or_accepted: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造闭合缺口判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved_or_accepted": proved_or_accepted,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    current: dict[str, Any],
    taxonomy: dict[str, Any],
    self_contained_final: dict[str, Any],
    external: dict[str, Any],
    promotion: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成最终缺口闭合判定表。"""
    current_boundary = current.get("final_open_input_boundary_closed") is True
    canonical_closed = self_contained_final.get("canonical_source_self_contained_closed") is True
    generic_refuted = self_contained_final.get("unrestricted_generic_self_contained_refuted") is True
    actual_bridge_pinned = taxonomy.get("actual_source_bridge_pinned") is True
    actual_bridge_closed = taxonomy.get("actual_source_bridge_theorem_closed") is True
    external_contract_closed = (
        taxonomy.get("external_contract_version_closed") is True
        and external.get("external_theorem_contract_closed") is True
    )
    primary_source_closed = external.get("self_contained_primary_source_proof_closed") is True
    promotion_boundary = promotion.get("promotion_package_boundary_closed") is True
    promotion_accepted = promotion.get("promotion_package_independently_accepted") is True
    return [
        row(
            "CurrentFinalInputBoundaryImported",
            current_boundary,
            False,
            "当前最终输入基已压到 source anti-atom 或外部 DI/BFI/Kuznetsov 匹配，再加独立晋级验收。",
            "判定哪些缺口是真缺口，哪些只是陈述边界。",
        ),
        row(
            "CanonicalSourceSelfContainedBranchClosed",
            canonical_closed,
            canonical_closed,
            "canonical RIW/Buchstab source 分支已有内部闭合证书。",
            "只能用于 branch-restricted 陈述，不能升级 generic unrestricted。",
        ),
        row(
            "UnrestrictedGenericSelfContainedRefuted",
            generic_refuted,
            generic_refuted,
            "unrestricted generic WFD 自足反原子被 moving-delta 模型反证。",
            "不得继续把 generic 自足版当作待证明命题。",
        ),
        row(
            "ActualSourceBridgeIsOnlySelfContainedUpgrade",
            actual_bridge_pinned,
            actual_bridge_closed,
            "若要把 canonical 分支闭合升级为实际 full-S non-AP 自足闭合，必须证明实际源锁定或实际源强化反原子。",
            ACTUAL_SOURCE_BRIDGE,
        ),
        row(
            "ExternalFullSKLSExtContractClosesMathLaneIfAccepted",
            external_contract_closed,
            external_contract_closed,
            "若接受 FullS-KLS-ext 作为外部深定理合同，generic 外部数学 lane 可闭合。",
            "仍需最终晋级验收。",
        ),
        row(
            "PrimarySourceSpecializationStillOpenWithoutBlackBox",
            True,
            primary_source_closed,
            "若不接受外部合同为黑箱，必须从 DI/BFI 原文逐项推出 FullS-KLS-ext。",
            PRIMARY_SOURCE_PROOF,
        ),
        row(
            "PromotionBoundaryClosedButNotAccepted",
            promotion_boundary,
            promotion_accepted,
            "DStructure/Tail-log4/finite Rankin 是最终晋级门，边界闭合但当前材料未获独立接受。",
            PROMOTION_GATE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行终端闭合缺口直接攻坚。"""
    current = load_json(paths["current"])
    taxonomy = load_json(paths["taxonomy"])
    self_contained_final = load_json(paths["self_contained_final"])
    external = load_json(paths["external"])
    promotion = load_json(paths["promotion"])
    rows = build_rows(current, taxonomy, self_contained_final, external, promotion)

    external_contract_closed = next(
        item for item in rows if item["gate"] == "ExternalFullSKLSExtContractClosesMathLaneIfAccepted"
    )["proved_or_accepted"]
    actual_bridge_closed = taxonomy.get("actual_source_bridge_theorem_closed") is True
    promotion_accepted = promotion.get("promotion_package_independently_accepted") is True
    all_closed = (actual_bridge_closed or external_contract_closed) and promotion_accepted

    return {
        "certificate_type": "prime_matrix_terminal_closure_gap_direct_attack_router",
        "status": "terminal_closure_gap_split_to_actual_source_or_external_contract_plus_referee_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "terminal_closure_gap_boundary_closed": True,
        "canonical_source_self_contained_branch_closed": self_contained_final.get(
            "canonical_source_self_contained_closed"
        )
        is True,
        "unrestricted_generic_self_contained_refuted": self_contained_final.get(
            "unrestricted_generic_self_contained_refuted"
        )
        is True,
        "actual_source_bridge_theorem_closed": actual_bridge_closed,
        "external_contract_math_lane_closed_if_accepted": external_contract_closed,
        "primary_source_specialization_proof_closed": external.get(
            "self_contained_primary_source_proof_closed"
        )
        is True,
        "promotion_package_independently_accepted": promotion_accepted,
        "all_required_inputs_proved_or_accepted": all_closed,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "minimum_full_self_contained_basis": f"{ACTUAL_SOURCE_BRIDGE} AND {PROMOTION_GATE}",
        "minimum_external_contract_basis": f"{EXTERNAL_CONTRACT} AND {PROMOTION_GATE}",
        "minimum_no_blackbox_external_basis": f"{PRIMARY_SOURCE_PROOF} AND {PROMOTION_GATE}",
        "next_self_contained_attack_target": ACTUAL_SOURCE_BRIDGE,
        "next_no_blackbox_external_attack_target": PRIMARY_SOURCE_PROOF,
        "parallel_referee_gate": PROMOTION_GATE,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_proof_or_acceptance_gates": [
            item["gate"] for item in rows if not item["proved_or_accepted"]
        ],
        "plain_conclusion": (
            "最终闭合缺口已拆清：canonical-source 自足版已闭合，unrestricted generic 自足版不是未攻破而是已被"
            " moving-delta 反证。要得到用户目标的全局版本，只剩两条合法路线：证明实际源桥"
            " ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput；或接受 FullS-KLS-ext 外部合同。"
            "若不接受外部黑箱，则必须补 DIBFIPrimarySourceSpecializationProof。两条数学路线之后都仍需"
            " DStructure/Tail-log4/finite Rankin 独立晋级验收。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 终端闭合缺口直接攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"terminal_closure_gap_boundary_closed={fmt_bool(result['terminal_closure_gap_boundary_closed'])}",
        (
            "canonical_source_self_contained_branch_closed="
            f"{fmt_bool(result['canonical_source_self_contained_branch_closed'])}"
        ),
        (
            "unrestricted_generic_self_contained_refuted="
            f"{fmt_bool(result['unrestricted_generic_self_contained_refuted'])}"
        ),
        (
            "actual_source_bridge_theorem_closed="
            f"{fmt_bool(result['actual_source_bridge_theorem_closed'])}"
        ),
        (
            "external_contract_math_lane_closed_if_accepted="
            f"{fmt_bool(result['external_contract_math_lane_closed_if_accepted'])}"
        ),
        (
            "primary_source_specialization_proof_closed="
            f"{fmt_bool(result['primary_source_specialization_proof_closed'])}"
        ),
        (
            "promotion_package_independently_accepted="
            f"{fmt_bool(result['promotion_package_independently_accepted'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 三种最小闭合基",
        "",
        "完全自足全局版：",
        "",
        "```text",
        result["minimum_full_self_contained_basis"],
        "```",
        "",
        "接受外部 FullS-KLS-ext 合同版：",
        "",
        "```text",
        result["minimum_external_contract_basis"],
        "```",
        "",
        "不接受外部黑箱、要求原文逐项推出版：",
        "",
        "```text",
        result["minimum_no_blackbox_external_basis"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved/accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{remaining}` |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved_or_accepted"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"自足全局版下一目标：`{result['next_self_contained_attack_target']}`。",
            f"无黑箱外部版下一目标：`{result['next_no_blackbox_external_attack_target']}`。",
            f"并行晋级门：`{result['parallel_referee_gate']}`。",
            "",
            "审稿边界：本路由不声明无条件闭合；它关闭的是终端缺口分类，并给出不可再偷换的剩余输入基。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current", type=Path, default=DEFAULT_CURRENT)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--self-contained-final", type=Path, default=DEFAULT_SELF_CONTAINED_FINAL)
    parser.add_argument("--external", type=Path, default=DEFAULT_EXTERNAL)
    parser.add_argument("--promotion", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "current": args.current,
        "taxonomy": args.taxonomy,
        "self_contained_final": args.self_contained_final,
        "external": args.external,
        "promotion": args.promotion,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
