#!/usr/bin/env python3
"""生成两条替代线 source-identity/antiatom 同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_source_identity_antiatom_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-source-identity-antiatom-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-source-identity-antiatom-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-source-identity-antiatom-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-source-identity-antiatom-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-source-identity-antiatom-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-alpha-return-bridge-sync-router.json"
OUTSIDE_LOOP = DOCS / "prime-matrix-strict-independent-source-bridge-outside-loop-attack-router.json"
CONCRETE_BRIDGE = DOCS / "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json"
ANTIATOM_AUDIT = DOCS / "prime-matrix-actual-source-antiatom-lane-audit-router.json"
CANONICAL_EXIT = DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
NEW_JOINT_OBLIGATION = DOCS / "prime-matrix-strict-new-joint-formula-terminal-obligation-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughAlphaReturn"
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
    """读取 JSON；缺失时返回空对象，便于历史证书兼容。"""
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
        OUTSIDE_LOOP,
        CONCRETE_BRIDGE,
        ANTIATOM_AUDIT,
        CANONICAL_EXIT,
        NEW_JOINT_OBLIGATION,
        DSTRUCTURE,
        PAPER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def internal_basis() -> str:
    """同步后的内部自足活动基。"""
    front = f"({NEW_JOINT} OR {CANONICAL_LOCK} OR {SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM})"
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
        == "two_replacement_lines_alpha_return_bridge_synced_open"
        and INDEPENDENT_BRIDGE in data["previous"].get("internal_basis_after_sync", "")
    )
    outside_loop_split = (
        data["outside_loop"].get("status")
        == "independent_source_bridge_outside_loop_reduced_to_source_identity_or_strengthened_antiatom_open"
        and data["outside_loop"].get("source_identity_proved") is False
        and data["outside_loop"].get("strengthened_actual_source_antiatom_proved") is False
    )
    concrete_bridge_imported = (
        data["concrete_bridge"].get("independent_actual_source_bridge_concrete_sync_closed") is True
        and data["concrete_bridge"].get("pointwise_alpha_route_counts_as_well_founded_descent") is False
    )
    generic_antiatom_refuted = (
        data["antiatom"].get("generic_self_contained_antiatom_refuted") is True
        or any(
            item.get("gate") == "GenericSelfContainedAntiAtomRefuted" and item.get("proved") is True
            for item in data["antiatom"].get("rows", [])
        )
    )
    canonical_scoped = (
        data["canonical_exit"].get("canonical_lock_refined_to_exact_same_set_certificate") is True
        and data["canonical_exit"].get("acyclic_canonical_exact_same_set_promotion_certificate_proved")
        is False
    )
    new_joint_missing = (
        data["new_joint"].get("new_explicit_joint_constructor_formula_artifact_present") is False
    )
    dstructure_author_remaining = data["dstructure"].get("external_lemma_author_side_remaining")
    dstructure_split = (
        dstructure_author_remaining in ("none", [], None)
        and DSTRUCTURE_GATE in data["dstructure"].get("external_lemma_non_author_remaining", [])
    ) or str(data["dstructure"].get("status", "")).startswith("dstructure_rankin_author_remainder_split")

    return [
        row(
            "AlphaReturnIndependentBridgeImported",
            previous_imported,
            True,
            "上一层已把 A1/source-entropy 伪出口判为 scoped canonical 或 alpha-return 回边前的 independent source bridge。",
            INDEPENDENT_BRIDGE,
        ),
        row(
            "ConcreteBridgeDisciplineImported",
            concrete_bridge_imported,
            True,
            "actual-source 桥必须在 pointwise/alpha 回边前给出；不能由 downstream entropy、ExactUV 或 pair-mass 回证。",
            INDEPENDENT_BRIDGE,
        ),
        row(
            "OutsideLoopBridgeSplitImported",
            outside_loop_split,
            False,
            "若 independent bridge 要作为非循环证明，它的非回边内容只剩 actual-source identity 或 strengthened actual-source antiatom。",
            f"{SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM}",
        ),
        row(
            "SourceIdentityOptionStillOpen",
            data["outside_loop"].get("source_identity_proved") is False,
            False,
            "source identity 必须在 Cauchy/dispersion/payment 前证明 actual full-S non-AP source 等于 canonical RIW/Buchstab 决策树源。",
            SOURCE_IDENTITY,
        ),
        row(
            "StrengthenedAntiAtomOptionStillOpen",
            data["outside_loop"].get("strengthened_actual_source_antiatom_proved") is False,
            False,
            "强化反原子必须作用在 actual final capacity measure 上；Phi-LPF/CRT 的无符号精确计数不能替代该 signed/moving 源定理。",
            STRENGTHENED_ANTIATOM,
        ),
        row(
            "GenericAntiAtomRouteRejected",
            generic_antiatom_refuted,
            True,
            "generic WFD/Type/Fourier/K4K6 反原子模板已被 moving-delta 模型排除，只能提交 strengthened actual-source 定理或外部谱输入。",
            STRENGTHENED_ANTIATOM,
        ),
        row(
            "CanonicalLockStillParallel",
            canonical_scoped,
            False,
            "canonical-lock 仍是并行分支；它需要 exact same-set canonical 五项证书，不能由 source bridge 同步支付。",
            CANONICAL_LOCK,
        ),
        row(
            "NewJointFormulaStillParallel",
            new_joint_missing,
            False,
            "new-joint 公式仍是另一条真正非循环输入；旧 joint constructor 路线已被判为 signed-source 固定点。",
            NEW_JOINT,
        ),
        row(
            "ExactUVIncidenceStillParallel",
            data["outside_loop"].get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "本层只压缩 independent bridge，不支付 actual exact-UV bounded multiplicity incidence。",
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
        "outside_loop": read_json(OUTSIDE_LOOP),
        "concrete_bridge": read_json(CONCRETE_BRIDGE),
        "antiatom": read_json(ANTIATOM_AUDIT),
        "canonical_exit": read_json(CANONICAL_EXIT),
        "new_joint": read_json(NEW_JOINT_OBLIGATION),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "two_replacement_lines_source_identity_antiatom_sync_router",
        "status": "two_replacement_lines_source_identity_antiatom_synced_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "independent_bridge_standalone_active_after_sync": False,
        "source_identity_proved": False,
        "strengthened_antiatom_proved": False,
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
            SOURCE_IDENTITY,
            STRENGTHENED_ANTIATOM,
            UV_INCIDENCE,
            PDEC_RATE,
            RATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ],
        "next_noncycle_author_attack": f"{SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM}",
        "parallel_author_attacks": [
            NEW_JOINT,
            CANONICAL_LOCK,
            UV_INCIDENCE,
            PDEC_RATE,
            RATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ],
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "alpha-return/source-bridge 同步后的 independent bridge 不能继续作为粗名出口。"
            "导入 outside-loop 攻击证书后，若它要成为非循环证明，就必须证明 actual full-S non-AP "
            "source 等于 canonical RIW/Buchstab 源，或证明 actual final capacity measure 的强化 "
            "source anti-atom。两者当前均未证明；generic WFD/Phi-LPF/CRT 无符号计数不能替代它们。"
            "new-joint、canonical-lock、ExactUV、Rate 与 DStructure/Rankin 仍是并行硬门。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix 两条替代线 source-identity/antiatom 同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"independent_bridge_standalone_active_after_sync={fmt_bool(payload['independent_bridge_standalone_active_after_sync'])}",
        f"source_identity_proved={fmt_bool(payload['source_identity_proved'])}",
        f"strengthened_antiatom_proved={fmt_bool(payload['strengthened_antiatom_proved'])}",
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
