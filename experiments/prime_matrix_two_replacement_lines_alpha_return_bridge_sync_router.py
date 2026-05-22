#!/usr/bin/env python3
"""生成两条替代线 alpha-return/source-bridge 同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_alpha_return_bridge_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-alpha-return-bridge-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-alpha-return-bridge-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-alpha-return-bridge-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-alpha-return-bridge-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SLUG = "prime-matrix-two-replacement-lines-alpha-return-bridge-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-terminal-leaf-source-bridge-sync-router.json"
ALPHA_RETURN = DOCS / "prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.json"
CANONICAL_EXIT = DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
INDEPENDENT_SOURCE = DOCS / "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughAlphaReturn"
SOURCE_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
EXACT_ENTROPY = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
UV_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
PDEC_RATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
DSTRUCTURE_SELF = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"

FULLS_MATCH = "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch"
FULLS_CAPACITY = "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput"
NEW_AUTOMORPHIC = "NewAutomorphicDispersionProof"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """登记脚本与依赖哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS, ALPHA_RETURN, CANONICAL_EXIT, INDEPENDENT_SOURCE, DSTRUCTURE, PAPER]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def internal_basis() -> str:
    """同步后的内部自足活动基。"""
    front = f"({NEW_JOINT} OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE})"
    return (
        f"{front} AND {UV_INCIDENCE} AND {HIGH_MODEL} AND {PDEC_RATE} "
        f"AND {RATE} AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF})"
    )


def external_no_blackbox_basis() -> str:
    """外部无黑箱版本仍需匹配的同对象强输入。"""
    return f"({FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_AUTOMORPHIC}) AND {DSTRUCTURE_GATE}"


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """构造同步判定表。"""
    previous_imported = (
        data["previous"].get("status")
        == "two_replacement_lines_terminal_leaf_source_bridge_synced_open"
    )
    alpha_return_imported = (
        data["alpha_return"].get("status")
        == "terminal_atoms_synced_to_alpha_return_independent_bridge_open"
        and data["alpha_return"].get("next_direct_attack_target")
        == f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}"
    )
    a1_absorbed = any(
        item.get("gate") == "A1AdmissionAbsorbedAsScopedBranch" and item.get("closed") is True
        for item in data["alpha_return"].get("rows", [])
    )
    entropy_backedge = (
        data["alpha_return"].get("moving_atom_reduced_to_exact_entropy") is True
        or any(
            item.get("gate") == "AlphaReturnRouteReclassifiedAsBackedge" and item.get("proved") is True
            for item in data["alpha_return"].get("rows", [])
        )
    )
    canonical_scoped = (
        data["canonical_exit"].get("canonical_lock_nonrecursive_exit_firewall_closed") is True
        or str(data["canonical_exit"].get("status", "")).startswith("strict_canonical_lock")
    )
    source_bridge_concrete = (
        data["independent_source"].get("independent_actual_source_bridge_concrete_sync_closed") is True
        and data["independent_source"].get("row_column_unconditional_closed") is False
    )
    dstructure_author_remaining = data["dstructure"].get("external_lemma_author_side_remaining")
    dstructure_split = (
        dstructure_author_remaining in ("none", [], None)
        and DSTRUCTURE_GATE in data["dstructure"].get("external_lemma_non_author_remaining", [])
    ) or str(data["dstructure"].get("status", "")).startswith("dstructure_rankin_author_remainder_split")

    return [
        row(
            "TerminalLeafSourceBridgeImported",
            previous_imported,
            True,
            "上一层已把两条替代线的三输入核表旧前沿接到终端叶子和 actual source bridge。",
            f"{NEW_JOINT} OR {CANONICAL_LOCK} OR {SOURCE_ADMISSION} OR {EXACT_ENTROPY}",
        ),
        row(
            "AlphaReturnBridgeImported",
            alpha_return_imported,
            True,
            "terminal atoms 到 alpha-return 同步证书把旧 pointwise/alpha 展开判为回边。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}",
        ),
        row(
            "A1AdmissionAbsorbedIntoCanonicalLock",
            a1_absorbed,
            False,
            "A1 clean-branch admission 只在 scoped canonical 分支内有效，不能作为 unrestricted noncanonical 全局矛盾。",
            CANONICAL_LOCK,
        ),
        row(
            "ExactEntropyRouteIsAlphaReturnBackedge",
            entropy_backedge,
            False,
            "exact clean-core source entropy 经 post-Mertens/kernel/pointwise/nonrecursive 路径回到终端叶子。",
            INDEPENDENT_BRIDGE,
        ),
        row(
            "IndependentSourceBridgeBeforeAlphaReturnPinned",
            source_bridge_concrete,
            False,
            "若 source bridge 要成为非循环输入，必须在进入 exact-UV/rank/alpha 回边前独立证明。",
            INDEPENDENT_BRIDGE,
        ),
        row(
            "CanonicalLockStillScopedAlternative",
            canonical_scoped,
            False,
            "canonical-lock 仍需 exact same-set canonical 证书；缺任一账本不能全局晋级。",
            CANONICAL_LOCK,
        ),
        row(
            "NewJointFormulaStillParallel",
            data["previous"].get("next_noncycle_author_attack") == NEW_JOINT,
            False,
            "new-joint 公式是另一条真正非循环出口；旧 joint constructor 路线已被上一层判为回到终端叶子。",
            NEW_JOINT,
        ),
        row(
            "ExactUVIncidenceStillParallel",
            data["independent_source"].get("independent_exact_pair_l2_or_max_atom_bound_proved") is False,
            False,
            "actual exact-UV bounded multiplicity incidence 仍是 rank/multiplicity 并行输入，不能由 alpha-return 同步支付。",
            UV_INCIDENCE,
        ),
        row(
            "RateAndDStructureStillCarried",
            dstructure_split,
            False,
            "本层只压缩 terminal atoms，不支付 rate-bearing packet 或 DStructure/Rankin 晋级门。",
            f"{RATE} AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF})",
        ),
        row(
            "ExternalLemmaVersionStillConditional",
            True,
            False,
            "外部引理版仍只在 FullS-KLS 外部合同和 DStructure/Rankin 独立接受下条件闭合。",
            f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}",
        ),
        row(
            "ExternalNoBlackboxVersionStillOpen",
            True,
            False,
            "无黑箱外部版仍需同对象 FullS theorem-match、actual source capacity 新定理或新的 automorphic/dispersion 证明。",
            external_no_blackbox_basis(),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "同步后真剩余进一步变窄，但目标命题仍未无条件闭合。",
            internal_basis(),
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "alpha_return": read_json(ALPHA_RETURN),
        "canonical_exit": read_json(CANONICAL_EXIT),
        "independent_source": read_json(INDEPENDENT_SOURCE),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "two_replacement_lines_alpha_return_bridge_sync_router",
        "status": "two_replacement_lines_alpha_return_bridge_synced_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "source_admission_standalone_active_after_sync": False,
        "exact_entropy_standalone_active_after_sync": False,
        "alpha_return_route_counts_as_descent": False,
        "external_lemma_version_closed_conditionally": True,
        "external_no_blackbox_version_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "internal_basis_after_sync": internal_basis(),
        "external_lemma_basis_after_sync": f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}",
        "external_no_blackbox_basis_after_sync": external_no_blackbox_basis(),
        "direct_attack_atoms_after_sync": [
            NEW_JOINT,
            CANONICAL_LOCK,
            INDEPENDENT_BRIDGE,
            UV_INCIDENCE,
            PDEC_RATE,
            RATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ],
        "next_noncycle_author_attack": f"{NEW_JOINT} OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}",
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "terminal-leaf/source-bridge 同步后的 source-admission 与 exact source entropy 仍不是最终出口。"
            "A1 source admission 只属于 scoped canonical 分支；exact entropy 沿 post-Mertens、kernel、"
            "pointwise table 与非递归表路径回到 alpha/terminal 回边。最新两条替代线的内部自足剩余因此压成 "
            "new-joint 公式、canonical-lock、进入 alpha 回边前的 independent actual-source bridge、"
            "actual exact-UV incidence、Rate 与 DStructure/Rankin。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix 两条替代线 alpha-return/source-bridge 同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"source_admission_standalone_active_after_sync={fmt_bool(payload['source_admission_standalone_active_after_sync'])}",
        f"exact_entropy_standalone_active_after_sync={fmt_bool(payload['exact_entropy_standalone_active_after_sync'])}",
        f"alpha_return_route_counts_as_descent={fmt_bool(payload['alpha_return_route_counts_as_descent'])}",
        f"external_lemma_version_closed_conditionally={fmt_bool(payload['external_lemma_version_closed_conditionally'])}",
        f"external_no_blackbox_version_closed={fmt_bool(payload['external_no_blackbox_version_closed'])}",
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in payload["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(item["gate"]),
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 内部自足版",
            "",
            "```text",
            payload["internal_basis_after_sync"],
            "```",
            "",
            "## 4. 外部两线",
            "",
            "外部引理版：",
            "",
            "```text",
            payload["external_lemma_basis_after_sync"],
            "```",
            "",
            "无黑箱外部版：",
            "",
            "```text",
            payload["external_no_blackbox_basis_after_sync"],
            "```",
            "",
            "## 5. 直接主攻原子",
            "",
        ]
    )
    for atom in payload["direct_attack_atoms_after_sync"]:
        lines.append(f"- `{atom}`")
    lines.extend(["", "## 6. 状态快照", "", "| field | value |", "| --- | --- |"])
    for key, value in payload["status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(["", "## 7. 依赖哈希", "", "| file | sha256 |", "| --- | --- |"])
    for name, digest in payload["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """执行证书生成。"""
    write_outputs(build_payload())


if __name__ == "__main__":
    main()
