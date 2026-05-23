#!/usr/bin/env python3
"""生成两条替代线 new-joint six-field 同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_new_joint_sixfield_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-new-joint-sixfield-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-new-joint-sixfield-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-new-joint-sixfield-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-new-joint-sixfield-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-new-joint-sixfield-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-canonical-exact-certificate-sync-router.json"
NEW_JOINT_OBLIGATION = DOCS / "prime-matrix-strict-new-joint-formula-terminal-obligation-router.json"
CANONICAL_EXIT = DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
OUTSIDE_LOOP = DOCS / "prime-matrix-strict-independent-source-bridge-outside-loop-attack-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
SIX_FIELD = "NewActualJointAlphaDeltaSixFieldConstructorArtifact"
EXACT_CERT = "AcyclicCanonicalExactSameSetPromotionCertificate"
NEW_SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
SOURCE_IDENTITY = "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab"
STRENGTHENED_ANTIATOM = "FullSNonAPStrengthenedSourceAntiAtomForActualSource"
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
    paths = [
        Path(__file__).resolve(),
        PREVIOUS,
        NEW_JOINT_OBLIGATION,
        CANONICAL_EXIT,
        OUTSIDE_LOOP,
        DSTRUCTURE,
        PAPER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def internal_basis() -> str:
    """同步后的内部自足活动基。"""
    front = (
        f"({SIX_FIELD} OR {EXACT_CERT} OR {NEW_SOURCE_ENTROPY} "
        f"OR {SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM})"
    )
    return (
        f"{front} AND {UV_INCIDENCE} AND {HIGH_MODEL} AND {PDEC_RATE} "
        f"AND {RATE} AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF})"
    )


def external_no_blackbox_basis() -> str:
    """外部无黑箱版本仍需匹配的同对象强输入。"""
    return f"({FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_AUTOMORPHIC}) AND {DSTRUCTURE_GATE}"


def formula_field_names(data: dict[str, Any]) -> list[str]:
    """从 strict 证书提取 six-field 名称。"""
    fields = data.get("formula_fields", [])
    names = [item.get("field", "") for item in fields if item.get("field")]
    return names


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """构造同步判定表。"""
    previous_imported = (
        data["previous"].get("status")
        == "two_replacement_lines_canonical_exact_certificate_synced_open"
        and NEW_JOINT in data["previous"].get("internal_basis_after_sync", "")
    )
    new_joint_obligation = (
        data["new_joint"].get("status")
        == "new_joint_formula_terminal_obligation_open_no_current_internal_formula_artifact"
        and data["new_joint"].get("new_joint_formula_is_current_internal_noncycle_target") is True
    )
    six_fields_present = len(formula_field_names(data["new_joint"])) == 6
    old_route_fixed_point = (
        data["new_joint"].get("old_joint_constructor_route_returns_to_signed_source_fixed_point") is True
    )
    new_formula_present = (
        data["new_joint"].get("new_explicit_joint_constructor_formula_artifact_present") is True
    )
    terminal_macrocycle = data["new_joint"].get("terminal_descent_alternative_is_macrocycle") is True
    source_identity_open = data["outside_loop"].get("source_identity_proved") is False
    antiatom_open = data["outside_loop"].get("strengthened_actual_source_antiatom_proved") is False
    canonical_open = (
        data["canonical"].get("acyclic_canonical_exact_same_set_promotion_certificate_proved")
        is False
    )
    new_entropy_open = data["canonical"].get("new_actual_source_entropy_theorem_proved") is False
    dstructure_author_remaining = data["dstructure"].get("external_lemma_author_side_remaining")
    dstructure_split = (
        dstructure_author_remaining in ("none", [], None)
        and DSTRUCTURE_GATE in data["dstructure"].get("external_lemma_non_author_remaining", [])
    ) or str(data["dstructure"].get("status", "")).startswith("dstructure_rankin_author_remainder_split")

    return [
        row(
            "CanonicalExactFrontImported",
            previous_imported,
            True,
            "上一层已把 canonical-lock 粗名同步为 exact same-set 证书或新 source entropy，并仍携带 new-joint。",
            NEW_JOINT,
        ),
        row(
            "NewJointTerminalObligationImported",
            new_joint_obligation,
            False,
            "strict 证书确认 new-joint 不是声明容器，而是 actual joint alpha/delta primitive word/coefficient 的终端公式义务。",
            SIX_FIELD,
        ),
        row(
            "SixFieldFormulaContractPinned",
            six_fields_present,
            False,
            "六字段合同包括 source tuple、formal unit、basis word、signed coefficient、UV/Phi pairing 与预算/回流。",
            SIX_FIELD,
        ),
        row(
            "OldJointRouteRejectedAsFixedPoint",
            old_route_fixed_point,
            True,
            "旧 joint rule 经 alpha-side、same-row、row-level、signed-emitter 回到 signed-source 固定点，不能替代新公式。",
            SIX_FIELD,
        ),
        row(
            "TerminalDescentAlternativeRejectedAsMacrocycle",
            terminal_macrocycle,
            True,
            "没有新公式时，terminal descent 替代路线已登记为 terminal-source-pair-joint 宏循环。",
            SIX_FIELD,
        ),
        row(
            "NewSixFieldArtifactStillOpen",
            new_formula_present is False,
            False,
            "当前仓库没有提交满足六字段合同的 actual joint alpha/delta 构造公式。",
            SIX_FIELD,
        ),
        row(
            "CanonicalAndSourceAlternativesStillParallel",
            canonical_open and new_entropy_open and source_identity_open and antiatom_open,
            False,
            "new-joint 同步不支付 canonical exact 证书、新 source entropy、source identity 或 strengthened antiatom。",
            f"{EXACT_CERT} OR {NEW_SOURCE_ENTROPY} OR {SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM}",
        ),
        row(
            "ExactUVIncidenceStillParallel",
            data["outside_loop"].get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "本层只压缩 new-joint，不支付 actual exact-UV bounded multiplicity incidence。",
            UV_INCIDENCE,
        ),
        row(
            "RateAndDStructureStillCarried",
            dstructure_split,
            False,
            "RatePreservation 与 DStructure/Rankin 仍是并行晋级门，本层不触碰。",
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
            "同步后真剩余更精确，但没有得到目标命题的无条件矛盾闭合。",
            internal_basis(),
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "new_joint": read_json(NEW_JOINT_OBLIGATION),
        "canonical": read_json(CANONICAL_EXIT),
        "outside_loop": read_json(OUTSIDE_LOOP),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "two_replacement_lines_new_joint_sixfield_sync_router",
        "status": "two_replacement_lines_new_joint_sixfield_synced_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "new_joint_coarse_label_active_after_sync": False,
        "new_joint_sixfield_artifact_proved": False,
        "old_joint_route_counts_as_proof": False,
        "external_lemma_version_closed_conditionally": True,
        "external_no_blackbox_version_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "six_field_artifact": SIX_FIELD,
        "six_field_contract": formula_field_names(data["new_joint"]),
        "internal_basis_after_sync": internal_basis(),
        "external_lemma_basis_after_sync": f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}",
        "external_no_blackbox_basis_after_sync": external_no_blackbox_basis(),
        "direct_attack_atoms_after_sync": [
            SIX_FIELD,
            EXACT_CERT,
            NEW_SOURCE_ENTROPY,
            SOURCE_IDENTITY,
            STRENGTHENED_ANTIATOM,
            UV_INCIDENCE,
            PDEC_RATE,
            RATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ],
        "next_noncycle_author_attack": SIX_FIELD,
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "canonical exact-certificate 同步后仍保留的 NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact "
            "不能再作为粗名出口。导入 strict terminal-obligation 证书后，它被精确为 six-field actual joint "
            "alpha/delta constructor artifact。旧 joint rule、terminal descent、pair-energy 等路线都回到固定点或宏循环。"
            "当前 six-field 工件未提交；其他 canonical/source/ExactUV/Rate/DStructure 硬门仍并行开放。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix 两条替代线 new-joint six-field 同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"new_joint_coarse_label_active_after_sync={fmt_bool(payload['new_joint_coarse_label_active_after_sync'])}",
        f"new_joint_sixfield_artifact_proved={fmt_bool(payload['new_joint_sixfield_artifact_proved'])}",
        f"old_joint_route_counts_as_proof={fmt_bool(payload['old_joint_route_counts_as_proof'])}",
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
    lines.extend(["", "## 3. Six-field 合同", ""])
    for field in payload["six_field_contract"]:
        lines.append(f"- `{field}`")
    lines.extend(
        [
            "",
            "## 4. 内部自足版",
            "",
            "```text",
            payload["internal_basis_after_sync"],
            "```",
            "",
            "## 5. 外部两线",
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
            "## 6. 直接主攻原子",
            "",
        ]
    )
    for atom in payload["direct_attack_atoms_after_sync"]:
        lines.append(f"- `{atom}`")
    lines.extend(["", "## 7. 状态快照", "", "| field | value |", "| --- | --- |"])
    for key, value in payload["status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(["", "## 8. 依赖哈希", "", "| file | sha256 |", "| --- | --- |"])
    for name, digest in payload["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """执行证书生成。"""
    write_outputs(build_payload())


if __name__ == "__main__":
    main()
