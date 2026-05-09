#!/usr/bin/env python3
"""内外两线下一最窄硬攻目标路由器。

用法示例：
  python3 experiments/prime_matrix_dual_next_narrowest_attack_router.py

输出：
  docs/monograph/prime-matrix-dual-next-narrowest-attack-router.json
  docs/monograph/prime-matrix-dual-next-narrowest-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_TERMINAL = DOCS / "prime-matrix-terminal-closure-gap-direct-attack-router.json"
DEFAULT_PROVENANCE = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
)
DEFAULT_RECONCILIATION = (
    DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
)
DEFAULT_COMPLEMENT = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.json"
DEFAULT_FULL_S_SPLIT = DOCS / "prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.json"
DEFAULT_EXTERNAL = DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
DEFAULT_PRIMARY_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
)
DEFAULT_AP_NOGO = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json"
DEFAULT_PROMOTION = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-dual-next-narrowest-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-dual-next-narrowest-attack-router.md"

NEW_SOURCE_ANTIATOM = "NewFullSNonAPSourceAntiAtomTheoremInput"
EXTERNAL_CONTRACT = "AcceptFullSKLSExtExternalContract"
NEW_FULL_S_THEOREM = "NewFullSTheoremInput"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值写为小写文本。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def route_row(
    gate: str,
    lane: str,
    boundary_closed: bool,
    proved_or_accepted: bool,
    evidence: str,
    consequence: str,
    next_target: str,
) -> dict[str, Any]:
    """构造双线硬攻路由行。"""
    return {
        "gate": gate,
        "lane": lane,
        "boundary_closed": boundary_closed,
        "proved_or_accepted": proved_or_accepted,
        "evidence": evidence,
        "consequence": consequence,
        "next_target": next_target,
    }


def build_rows(
    terminal: dict[str, Any],
    provenance: dict[str, Any],
    reconciliation: dict[str, Any],
    complement: dict[str, Any],
    full_s_split: dict[str, Any],
    external: dict[str, Any],
    primary_nogo: dict[str, Any],
    ap_nogo: dict[str, Any],
    promotion: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成自足线和外部线的下一最窄判定表。"""
    terminal_ready = (
        terminal.get("terminal_closure_gap_boundary_closed") is True
        and terminal.get("row_column_unconditional_closed") is False
    )
    canonical_removed = (
        provenance.get("terminal_gap_after_router") == "NoFurtherActualSourceProvenanceGap"
        and reconciliation.get("actual_source_bridge_closed_for_canonical_branch") is True
        and complement.get("canonical_branch_removed_from_remainder") is True
    )
    generic_refuted = complement.get("generic_wfd_template_available") is False
    self_contained_pinned = (
        full_s_split.get("terminal_gap_after_router") == NEW_SOURCE_ANTIATOM
        and full_s_split.get("self_contained_version_closed") is False
        and NEW_SOURCE_ANTIATOM in full_s_split.get("open_split_gates", [])
    )
    external_contract_available = (
        terminal.get("external_contract_math_lane_closed_if_accepted") is True
        and external.get("external_theorem_contract_closed") is True
    )
    primary_rejected = (
        primary_nogo.get("terminal_gap_after_router") == "NewFullSTheoremInputOrAPSourceLift"
        and primary_nogo.get("primary_source_specialization_closed") is False
    )
    ap_lift_rejected = (
        ap_nogo.get("ap_source_lift_rejected") is True
        and ap_nogo.get("terminal_gap_after_router") == NEW_FULL_S_THEOREM
    )
    no_blackbox_pinned = primary_rejected and ap_lift_rejected
    promotion_boundary = promotion.get("promotion_package_boundary_closed") is True
    promotion_accepted = promotion.get("promotion_package_independently_accepted") is True

    return [
        route_row(
            gate="TerminalBoundaryImported",
            lane="both",
            boundary_closed=terminal_ready,
            proved_or_accepted=False,
            evidence=terminal.get("status", "unknown"),
            consequence="旧终端已拆成自足、外部黑箱、无黑箱外部证明和独立晋级门。",
            next_target="DualLaneNextNarrowestCompression",
        ),
        route_row(
            gate="CanonicalActualSourceNoLongerNextTarget",
            lane="self-contained",
            boundary_closed=canonical_removed,
            proved_or_accepted=canonical_removed,
            evidence=provenance.get("terminal_gap_after_router", "unknown"),
            consequence="canonical 分支来源账本已闭合；继续攻它不能覆盖 noncanonical full-S 补集。",
            next_target=NEW_SOURCE_ANTIATOM,
        ),
        route_row(
            gate="GenericWFDTemplateForbidden",
            lane="self-contained",
            boundary_closed=generic_refuted,
            proved_or_accepted=generic_refuted,
            evidence="generic_wfd_template_available=false",
            consequence="moving-delta no-go 后，不能把 unrestricted generic WFD 当作自足引理继续使用。",
            next_target=NEW_SOURCE_ANTIATOM,
        ),
        route_row(
            gate="SelfContainedNextNarrowestPinned",
            lane="self-contained",
            boundary_closed=self_contained_pinned,
            proved_or_accepted=False,
            evidence=full_s_split.get("terminal_gap_after_router", "unknown"),
            consequence="完全自足线被压到一个新源定理：实际 noncanonical full-S 源的强化反原子。",
            next_target=NEW_SOURCE_ANTIATOM,
        ),
        route_row(
            gate="ExternalBlackBoxContractAvailable",
            lane="external-blackbox",
            boundary_closed=external_contract_available,
            proved_or_accepted=False,
            evidence=external.get("status", "unknown"),
            consequence="接受 FullS-KLS-ext 作为外部深定理合同时，外部数学 lane 可关闭；当前未把它登记为最终已接受输入。",
            next_target=EXTERNAL_CONTRACT,
        ),
        route_row(
            gate="PrimarySourceSpecializationRejected",
            lane="external-no-blackbox",
            boundary_closed=primary_rejected,
            proved_or_accepted=False,
            evidence=primary_nogo.get("terminal_gap_after_router", "unknown"),
            consequence="现有 DI/BFI 主来源不能逐项推出当前 full-S non-AP KLS-ext。",
            next_target="NewFullSTheoremInputOrAPSourceLift",
        ),
        route_row(
            gate="APSourceLiftRejected",
            lane="external-no-blackbox",
            boundary_closed=ap_lift_rejected,
            proved_or_accepted=ap_lift_rejected,
            evidence=ap_nogo.get("terminal_gap_after_router", "unknown"),
            consequence="non-AP generic WFD 补集不能无损回提到 AP-source；无黑箱外部线只剩新 full-S 定理证明。",
            next_target=NEW_FULL_S_THEOREM,
        ),
        route_row(
            gate="ExternalNoBlackBoxNextNarrowestPinned",
            lane="external-no-blackbox",
            boundary_closed=no_blackbox_pinned,
            proved_or_accepted=False,
            evidence="primary_source_no_go + ap_source_lift_no_go",
            consequence="若不接受黑箱合同，外部路线也不再是找旧 DI/BFI 引文，而是新增或证明能覆盖 full-S non-AP 对象的定理。",
            next_target=NEW_FULL_S_THEOREM,
        ),
        route_row(
            gate="DStructureRankinRefereeGateStillSeparate",
            lane="referee",
            boundary_closed=promotion_boundary,
            proved_or_accepted=promotion_accepted,
            evidence=promotion.get("status", "unknown"),
            consequence="任何数学 lane 闭合后，仍需 DStructure/Tail-log4/finite Rankin 独立验收。",
            next_target=PROMOTION_GATE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行下一最窄双线硬攻路由。"""
    terminal = load_json(paths["terminal"])
    provenance = load_json(paths["provenance"])
    reconciliation = load_json(paths["reconciliation"])
    complement = load_json(paths["complement"])
    full_s_split = load_json(paths["full_s_split"])
    external = load_json(paths["external"])
    primary_nogo = load_json(paths["primary_nogo"])
    ap_nogo = load_json(paths["ap_nogo"])
    promotion = load_json(paths["promotion"])

    rows = build_rows(
        terminal=terminal,
        provenance=provenance,
        reconciliation=reconciliation,
        complement=complement,
        full_s_split=full_s_split,
        external=external,
        primary_nogo=primary_nogo,
        ap_nogo=ap_nogo,
        promotion=promotion,
    )
    boundary_closed = all(row["boundary_closed"] for row in rows)
    all_required_inputs_closed = (
        any(
            row["gate"] == "SelfContainedNextNarrowestPinned"
            and row["proved_or_accepted"]
            for row in rows
        )
        or any(
            row["gate"] == "ExternalBlackBoxContractAvailable"
            and row["proved_or_accepted"]
            for row in rows
        )
        or any(
            row["gate"] == "ExternalNoBlackBoxNextNarrowestPinned"
            and row["proved_or_accepted"]
            for row in rows
        )
    ) and any(
        row["gate"] == "DStructureRankinRefereeGateStillSeparate"
        and row["proved_or_accepted"]
        for row in rows
    )

    return {
        "certificate_type": "prime_matrix_dual_next_narrowest_attack_router",
        "status": (
            "dual_next_narrowest_reduced_to_new_full_s_source_theorem_or_accepted_"
            "external_contract_plus_referee_open"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{
                str(path.relative_to(ROOT)): file_sha256(path)
                for path in paths.values()
            },
        },
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "dual_next_narrowest_boundary_closed": boundary_closed,
        "self_contained_next_target": NEW_SOURCE_ANTIATOM,
        "external_blackbox_next_target": EXTERNAL_CONTRACT,
        "external_no_blackbox_next_target": NEW_FULL_S_THEOREM,
        "parallel_referee_gate": PROMOTION_GATE,
        "self_contained_basis": f"{NEW_SOURCE_ANTIATOM} AND {PROMOTION_GATE}",
        "external_blackbox_basis": f"{EXTERNAL_CONTRACT} AND {PROMOTION_GATE}",
        "external_no_blackbox_basis": f"{NEW_FULL_S_THEOREM} AND {PROMOTION_GATE}",
        "unified_dual_basis": (
            f"(({NEW_SOURCE_ANTIATOM}) OR {EXTERNAL_CONTRACT} OR {NEW_FULL_S_THEOREM}) "
            f"AND {PROMOTION_GATE}"
        ),
        "all_required_inputs_proved_or_accepted": all_required_inputs_closed,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "closed_boundary_gates": [row["gate"] for row in rows if row["boundary_closed"]],
        "open_proof_or_acceptance_gates": [
            row["gate"] for row in rows if not row["proved_or_accepted"]
        ],
        "rows": rows,
        "plain_conclusion": (
            "下一最窄目标已经重新压缩：canonical actual-source provenance 已只在 canonical 分支关闭，"
            "不能再作为全局剩余继续攻；unrestricted generic WFD 模板已被 moving-delta 阻断。"
            "完全自足线只剩 NewFullSNonAPSourceAntiAtomTheoremInput。黑箱外部线可以明确接受 "
            "FullS-KLS-ext 合同；若不接受黑箱，则 DI/BFI 主来源特化和 APSourceLift 都已被 no-go "
            "排除，外部线也只剩 NewFullSTheoremInput。三条数学路径之后都必须通过 DStructure/"
            "Tail-log4/finite Rankin 独立验收。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 内外两线下一最窄硬攻路由器",
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
            "dual_next_narrowest_boundary_closed="
            f"{fmt_bool(result['dual_next_narrowest_boundary_closed'])}"
        ),
        (
            "all_required_inputs_proved_or_accepted="
            f"{fmt_bool(result['all_required_inputs_proved_or_accepted'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下一最窄目标",
        "",
        "完全自足线：",
        "",
        "```text",
        result["self_contained_basis"],
        "```",
        "",
        "外部黑箱合同线：",
        "",
        "```text",
        result["external_blackbox_basis"],
        "```",
        "",
        "无黑箱外部证明线：",
        "",
        "```text",
        result["external_no_blackbox_basis"],
        "```",
        "",
        "统一二线输入基：",
        "",
        "```text",
        result["unified_dual_basis"],
        "```",
        "",
        "## 2. 路由审查表",
        "",
        "| gate | lane | boundary closed | proved/accepted | evidence | consequence | next target |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{lane}` | `{boundary}` | `{proved}` | {evidence} | {consequence} | `{next}` |".format(
                gate=table_cell(row["gate"]),
                lane=table_cell(row["lane"]),
                boundary=fmt_bool(row["boundary_closed"]),
                proved=fmt_bool(row["proved_or_accepted"]),
                evidence=table_cell(row["evidence"]),
                consequence=table_cell(row["consequence"]),
                next=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 当前判定",
            "",
            "本路由闭合的是“下一步应攻哪里”的边界，不证明新 full-S 源反原子，"
            "也不把 FullS-KLS-ext 自动登记为已接受外部输入，更不替代 DStructure/Rankin 独立验收。",
            "因此完整行/列无条件命题仍未闭合；下一步最窄硬点已经固定为上述三条路径之一。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--terminal-json", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--provenance-json", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--reconciliation-json", type=Path, default=DEFAULT_RECONCILIATION)
    parser.add_argument("--complement-json", type=Path, default=DEFAULT_COMPLEMENT)
    parser.add_argument("--full-s-split-json", type=Path, default=DEFAULT_FULL_S_SPLIT)
    parser.add_argument("--external-json", type=Path, default=DEFAULT_EXTERNAL)
    parser.add_argument("--primary-nogo-json", type=Path, default=DEFAULT_PRIMARY_NOGO)
    parser.add_argument("--ap-nogo-json", type=Path, default=DEFAULT_AP_NOGO)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "terminal": args.terminal_json,
        "provenance": args.provenance_json,
        "reconciliation": args.reconciliation_json,
        "complement": args.complement_json,
        "full_s_split": args.full_s_split_json,
        "external": args.external_json,
        "primary_nogo": args.primary_nogo_json,
        "ap_nogo": args.ap_nogo_json,
        "promotion": args.promotion_json,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["unified_dual_basis"])


if __name__ == "__main__":
    main()
