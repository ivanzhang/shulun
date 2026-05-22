#!/usr/bin/env python3
"""生成两条替代线 terminal-leaf/source-bridge 同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_terminal_leaf_source_bridge_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-terminal-leaf-source-bridge-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-terminal-leaf-source-bridge-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-terminal-leaf-source-bridge-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-terminal-leaf-source-bridge-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-terminal-leaf-source-bridge-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-sourcerank-terminal-kernel-sync-router.json"
KERNEL_THREE = DOCS / "prime-matrix-strict-kernel-table-three-leg-return-sync-router.json"
FIELD_CONTRACT = DOCS / "prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json"
TERMINAL_LEAF_SYNC = DOCS / "prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json"
CURRENT_LEAF = DOCS / "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json"
POST_ALPHA = DOCS / "prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.json"
NONCANONICAL_LEGAL = DOCS / "prime-matrix-strict-noncanonical-legal-closure-mode-router.json"
INDEPENDENT_SOURCE = DOCS / "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json"
CANONICAL_EXIT = DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
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
    """读取 JSON；缺失时返回空对象，便于历史归档兼容。"""
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
    paths = [
        Path(__file__).resolve(),
        PREVIOUS,
        KERNEL_THREE,
        FIELD_CONTRACT,
        TERMINAL_LEAF_SYNC,
        CURRENT_LEAF,
        POST_ALPHA,
        NONCANONICAL_LEGAL,
        INDEPENDENT_SOURCE,
        CANONICAL_EXIT,
        DSTRUCTURE,
        PAPER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def internal_basis() -> str:
    """同步后的内部自足活动基。"""
    front = (
        f"({NEW_JOINT} OR {CANONICAL_LOCK} OR {SOURCE_ADMISSION} OR {EXACT_ENTROPY})"
    )
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
        == "two_replacement_lines_sourcerank_terminal_synced_to_pointwise_kernel_open"
    )
    kernel_fixed = (
        data["kernel_three"].get("kernel_table_three_leg_return_sync_closed") is True
        and data["kernel_three"].get("three_leg_separate_attack_is_fixed_point") is True
    )
    field_boundary = data["field_contract"].get("field_contract_boundary_closed") is True
    terminal_leaf = (
        data["terminal_leaf"].get("sync_closed") is True
        and data["terminal_leaf"].get("current_leaf_firewall_active_basis_reduced") is True
    )
    current_leaf = (
        data["current_leaf"].get("current_leaf_firewall_active_basis_reduced") is True
        and data["current_leaf"].get("terminal_gap_after_current_instance_router")
        == f"{CANONICAL_LOCK} OR NoncanonicalFullSComplementLegalClosureMode"
    )
    pdec_to_new_joint = data["post_alpha"].get("pdec_scope_internal_branch_saturated") is True
    joint_loop = data["post_alpha"].get("joint_constructor_route_loops_without_new_formula") is True
    source_bridge = (
        data["independent_source"].get("independent_actual_source_bridge_concrete_sync_closed") is True
        and data["independent_source"].get("terminal_gap_after_router")
        == f"{CANONICAL_LOCK} OR {SOURCE_ADMISSION} OR {EXACT_ENTROPY}"
    )
    noncanonical_filtered = (
        data["noncanonical"].get("status")
        == "strict_noncanonical_legal_mode_filtered_to_actual_source_bridge_open"
    )
    canonical_scoped = (
        data["canonical_exit"].get("canonical_lock_nonrecursive_exit_firewall_closed") is True
        or data["canonical_exit"].get("status")
        == "strict_canonical_lock_nonrecursive_exit_refined_to_exact_same_set_certificate_or_source_entropy_open"
    )
    dstructure_author_remaining = data["dstructure"].get("external_lemma_author_side_remaining")
    dstructure_split = (
        dstructure_author_remaining in ("none", [], None)
        and DSTRUCTURE_GATE in data["dstructure"].get("external_lemma_non_author_remaining", [])
    ) or str(data["dstructure"].get("status", "")).startswith("dstructure_rankin_author_remainder_split")

    return [
        row(
            "SourceRankTerminalKernelImported",
            previous_imported,
            True,
            "上一层已把 source-rank/no-collapse 与 terminal descent 粗口汇到逐点 primitive 核表。",
            "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
        ),
        row(
            "KernelThreeLegFixedPointImported",
            kernel_fixed,
            True,
            "alpha、weight、rank 三腿分攻会回到 PDEC/CleanKLS 或同一 primitive source table。",
            "NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn",
        ),
        row(
            "NonrecursiveFieldBoundaryPinned",
            field_boundary,
            True,
            "非递归核表字段边界已闭合；真正缺口是同一 source tuple 的一次性正向构造。",
            "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple",
        ),
        row(
            "OldJointConstructorRouteReturnsToTerminalLeaf",
            terminal_leaf and joint_loop,
            True,
            "若没有新的显式 joint constructor 公式，旧 joint-alpha 路线回到 signed-source 固定点和终端叶子。",
            f"{CANONICAL_LOCK} OR NoncanonicalFullSComplementLegalClosureMode",
        ),
        row(
            "CurrentTerminalLeafReduced",
            current_leaf,
            False,
            "当前已物化 PDEC/sparse 实例不是活动数学义务；活动叶子只剩 canonical-lock 或 noncanonical legal mode。",
            f"{CANONICAL_LOCK} OR NoncanonicalFullSComplementLegalClosureMode",
        ),
        row(
            "NoncanonicalLegalModeFilteredToSourceBridge",
            noncanonical_filtered and source_bridge,
            False,
            "noncanonical legal mode 不能用 generic WFD 模板关闭，必须进入 actual source bridge 的具体原子。",
            f"{SOURCE_ADMISSION} OR {EXACT_ENTROPY}",
        ),
        row(
            "PDECScopeBranchSaturatedToNewJoint",
            pdec_to_new_joint,
            False,
            "same-set PDEC 作用域分支在当前内部材料中已饱和，若不走外部谱输入就必须给新 joint 公式。",
            NEW_JOINT,
        ),
        row(
            "NewJointFormulaStillMissing",
            data["post_alpha"].get("new_explicit_joint_constructor_formula_artifact_present") is False,
            False,
            "新 joint 公式不能由 signed-lane 环、Phi-LPF 无符号字段或 terminal descent 反推出。",
            NEW_JOINT,
        ),
        row(
            "CanonicalLockStillScopedAlternative",
            canonical_scoped,
            False,
            "canonical-lock 只能作为 exact same-set canonical 证书分支；任一账本缺失即回到 actual source entropy。",
            CANONICAL_LOCK,
        ),
        row(
            "ExactUVIncidenceStillParallel",
            data["terminal_leaf"].get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False
            and data["independent_source"].get("independent_exact_pair_l2_or_max_atom_bound_proved")
            is False,
            False,
            "核表 rank/multiplicity 口径仍需 actual exact-UV bounded multiplicity incidence 或独立 pair 能量界。",
            UV_INCIDENCE,
        ),
        row(
            "RateAndDStructureStillCarried",
            dstructure_split,
            False,
            "本层只同步前沿，不支付 moving-atom 速率保持或 DStructure/Rankin 最终晋级门。",
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
            "同步后真剩余更窄，但没有得到目标命题的无条件矛盾闭合。",
            internal_basis(),
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "kernel_three": read_json(KERNEL_THREE),
        "field_contract": read_json(FIELD_CONTRACT),
        "terminal_leaf": read_json(TERMINAL_LEAF_SYNC),
        "current_leaf": read_json(CURRENT_LEAF),
        "post_alpha": read_json(POST_ALPHA),
        "noncanonical": read_json(NONCANONICAL_LEGAL),
        "independent_source": read_json(INDEPENDENT_SOURCE),
        "canonical_exit": read_json(CANONICAL_EXIT),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "two_replacement_lines_terminal_leaf_source_bridge_sync_router",
        "status": "two_replacement_lines_terminal_leaf_source_bridge_synced_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "kernel_triad_standalone_active_after_sync": False,
        "old_joint_constructor_route_active_after_sync": False,
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
            SOURCE_ADMISSION,
            EXACT_ENTROPY,
            UV_INCIDENCE,
            PDEC_RATE,
            RATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ],
        "next_noncycle_author_attack": NEW_JOINT,
        "next_source_bridge_attack": f"{SOURCE_ADMISSION} OR {EXACT_ENTROPY}",
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "两条替代线不能继续停在 source-rank/terminal 三输入核表旧前沿。既有 strict 证书显示："
            "三腿分攻是固定点；非递归核表若没有新的 actual joint constructor 公式，会回到终端叶子；"
            "当前终端叶子再压成 canonical-lock 或 actual source bridge。因而最新内部自足剩余为 "
            "new-joint 公式、canonical-lock、A1 source admission、exact clean-core source entropy、"
            "actual exact-UV incidence、Rate 与 DStructure/Rankin。外部引理版仍只是条件闭合。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix 两条替代线 terminal-leaf/source-bridge 同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"kernel_triad_standalone_active_after_sync={fmt_bool(payload['kernel_triad_standalone_active_after_sync'])}",
        f"old_joint_constructor_route_active_after_sync={fmt_bool(payload['old_joint_constructor_route_active_after_sync'])}",
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
