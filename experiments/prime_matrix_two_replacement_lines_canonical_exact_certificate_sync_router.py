#!/usr/bin/env python3
"""生成两条替代线 canonical exact-certificate 同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_canonical_exact_certificate_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-canonical-exact-certificate-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-canonical-exact-certificate-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-canonical-exact-certificate-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-canonical-exact-certificate-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-canonical-exact-certificate-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-source-identity-antiatom-sync-router.json"
CANONICAL_EXIT = DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
NEW_JOINT_OBLIGATION = DOCS / "prime-matrix-strict-new-joint-formula-terminal-obligation-router.json"
OUTSIDE_LOOP = DOCS / "prime-matrix-strict-independent-source-bridge-outside-loop-attack-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
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

FIVE_CERT_FIELDS = [
    "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy",
    "AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity",
    "AcyclicSeedNoSourceReplacementOrPayloadCreation",
    "TerminalCertificateSameSetPushforwardIdentity",
    "NoNoncanonicalPayloadSurvivesCanonicalProjection",
]


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
        CANONICAL_EXIT,
        NEW_JOINT_OBLIGATION,
        OUTSIDE_LOOP,
        DSTRUCTURE,
        PAPER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def internal_basis() -> str:
    """同步后的内部自足活动基。"""
    front = (
        f"({NEW_JOINT} OR {EXACT_CERT} OR {NEW_SOURCE_ENTROPY} "
        f"OR {SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM})"
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
        == "two_replacement_lines_source_identity_antiatom_synced_open"
        and CANONICAL_LOCK in data["previous"].get("internal_basis_after_sync", "")
    )
    canonical_refined = (
        data["canonical"].get("status")
        == "strict_canonical_lock_nonrecursive_exit_refined_to_exact_same_set_certificate_or_source_entropy_open"
        and data["canonical"].get("canonical_lock_refined_to_exact_same_set_certificate") is True
    )
    exact_cert_proved = (
        data["canonical"].get("acyclic_canonical_exact_same_set_promotion_certificate_proved") is True
    )
    new_entropy_proved = data["canonical"].get("new_actual_source_entropy_theorem_proved") is True
    new_joint_missing = (
        data["new_joint"].get("new_explicit_joint_constructor_formula_artifact_present") is False
    )
    source_identity_open = data["outside_loop"].get("source_identity_proved") is False
    antiatom_open = data["outside_loop"].get("strengthened_actual_source_antiatom_proved") is False
    dstructure_author_remaining = data["dstructure"].get("external_lemma_author_side_remaining")
    dstructure_split = (
        dstructure_author_remaining in ("none", [], None)
        and DSTRUCTURE_GATE in data["dstructure"].get("external_lemma_non_author_remaining", [])
    ) or str(data["dstructure"].get("status", "")).startswith("dstructure_rankin_author_remainder_split")

    return [
        row(
            "SourceIdentityAntiAtomFrontImported",
            previous_imported,
            True,
            "上一层已把 independent bridge 粗名压成 source identity 或 strengthened antiatom，并仍携带 canonical-lock。",
            CANONICAL_LOCK,
        ),
        row(
            "CanonicalLockRefinedToExactSameSetImported",
            canonical_refined,
            False,
            "canonical-lock 不是单个矛盾标签；它只能是五项 exact same-set canonical 晋级证书，或回到 actual-source entropy。",
            f"{EXACT_CERT} OR {NEW_SOURCE_ENTROPY}",
        ),
        row(
            "FiveLedgerCertificateFieldsPinned",
            canonical_refined,
            False,
            "五项账本必须全部在 pre-Cauchy/source-preserving 同一集合口径下成立，不能从 terminal/payment 反推。",
            " AND ".join(FIVE_CERT_FIELDS),
        ),
        row(
            "ExactSameSetCertificateStillOpen",
            exact_cert_proved is False,
            False,
            "当前语料没有提交五项 exact same-set canonical 晋级证书。",
            EXACT_CERT,
        ),
        row(
            "NewActualSourceEntropyStillOpen",
            new_entropy_proved is False,
            False,
            "若五项任一缺失，canonical-lock 路线失效，剩余回到新的 actual clean-core source entropy 定理。",
            NEW_SOURCE_ENTROPY,
        ),
        row(
            "SourceIdentityAndAntiAtomStillParallel",
            source_identity_open and antiatom_open,
            False,
            "上一层的 source identity 与 strengthened antiatom 没有被 canonical-lock 同步支付，仍是并行非循环输入。",
            f"{SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM}",
        ),
        row(
            "NewJointFormulaStillParallel",
            new_joint_missing,
            False,
            "new-joint 公式仍是并行非循环输入；旧 joint constructor 路线不能替代它。",
            NEW_JOINT,
        ),
        row(
            "ExactUVIncidenceStillParallel",
            data["outside_loop"].get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "本层只压缩 canonical-lock，不支付 actual exact-UV bounded multiplicity incidence。",
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
            "同步后真剩余更窄，但没有得到目标命题的无条件矛盾闭合。",
            internal_basis(),
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "canonical": read_json(CANONICAL_EXIT),
        "new_joint": read_json(NEW_JOINT_OBLIGATION),
        "outside_loop": read_json(OUTSIDE_LOOP),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "two_replacement_lines_canonical_exact_certificate_sync_router",
        "status": "two_replacement_lines_canonical_exact_certificate_synced_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "canonical_lock_standalone_active_after_sync": False,
        "canonical_exact_certificate_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "external_lemma_version_closed_conditionally": True,
        "external_no_blackbox_version_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "canonical_exact_certificate_definition": " AND ".join(FIVE_CERT_FIELDS),
        "internal_basis_after_sync": internal_basis(),
        "external_lemma_basis_after_sync": f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}",
        "external_no_blackbox_basis_after_sync": external_no_blackbox_basis(),
        "direct_attack_atoms_after_sync": [
            NEW_JOINT,
            EXACT_CERT,
            NEW_SOURCE_ENTROPY,
            SOURCE_IDENTITY,
            STRENGTHENED_ANTIATOM,
            UV_INCIDENCE,
            PDEC_RATE,
            RATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ],
        "five_certificate_fields": FIVE_CERT_FIELDS,
        "next_noncycle_author_attack": f"{EXACT_CERT} OR {NEW_SOURCE_ENTROPY}",
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "source-identity/antiatom 同步后的 canonical-lock 仍不能作为粗名出口。"
            "既有 strict nonrecursive-exit 攻击证书把它精炼为 exact same-set canonical 五项晋级证书；"
            "若五项任一缺失，则 canonical-lock 不能使用，剩余回到 NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem。"
            "当前五项证书和新的 actual-source entropy 定理都未证明；new-joint、source identity、strengthened antiatom、"
            "ExactUV、Rate 与 DStructure/Rankin 仍是并行硬门。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix 两条替代线 canonical exact-certificate 同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"canonical_lock_standalone_active_after_sync={fmt_bool(payload['canonical_lock_standalone_active_after_sync'])}",
        f"canonical_exact_certificate_proved={fmt_bool(payload['canonical_exact_certificate_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(payload['new_actual_source_entropy_theorem_proved'])}",
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
            "## 3. 五项 exact same-set 证书",
            "",
        ]
    )
    for item in payload["five_certificate_fields"]:
        lines.append(f"- `{item}`")
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
