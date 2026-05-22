#!/usr/bin/env python3
"""生成两条替代线 seed/payload 饱和同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_seed_payload_saturation_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-seed-payload-saturation-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-seed-payload-saturation-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-seed-payload-saturation-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-seed-payload-saturation-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-seed-payload-saturation-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-source-admission-absorption-sync-router.json"
SEED_FRONTIER = DOCS / "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"
SIGNED_LANE = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
PAYLOAD_ALIGNMENT = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"
SOURCE_RANK = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
NEW_JOINT_ALPHA = DOCS / "prime-matrix-phi-lpf-latest-new-joint-alpha-terminal-three-atoms-sync-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_PAYLOAD = "NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle"
NEW_ATOMIC_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
KZE_EXTERNAL = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"

SOURCE_RANK_PACKAGE = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
SOURCE_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"

HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
PDEC_RATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
DSTRUCTURE_SELF = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，避免把缺失误报成证明。"""
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
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def dependency_paths() -> list[Path]:
    """列出证书依赖。"""
    return [
        PREVIOUS,
        SEED_FRONTIER,
        SIGNED_LANE,
        PAYLOAD_ALIGNMENT,
        SOURCE_RANK,
        NEW_JOINT_ALPHA,
        DSTRUCTURE,
        PAPER,
    ]


def source_hashes() -> dict[str, str]:
    """登记脚本与依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def source_rank_atoms() -> str:
    """展开 source-rank/no-collapse 包的三个作者侧原子。"""
    return f"({SOURCE_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY})"


def full_internal_basis() -> str:
    """写出同步后的内部自足活动基。"""
    front = (
        f"({PDEC_SCOPE} OR {NEW_JOINT} OR {source_rank_atoms()} "
        f"OR {TERMINAL_DESCENT} OR {KZE_EXTERNAL})"
    )
    return (
        f"({front} AND {HIGH_MODEL}) "
        f"AND {PDEC_RATE} "
        "AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward "
        "AND JointEmitterPrepushforwardWordCoefficientIdentityLedger "
        "AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger "
        "AND ActualEmitterSourceDomainEntropyLedger "
        "AND ExactUVMapFixedPairPolylogFiberBoundLedger "
        "AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward "
        "AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger "
        f"AND {COMPLETE_KEY} "
        f"AND {FIXED_KEY} "
        f"AND {RATE} "
        f"AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF})"
    )


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """构造同步判定表。"""
    previous_ok = (
        data["previous"].get("status")
        == "two_replacement_lines_a1_source_admission_absorbed_to_outside_cycle_break_open"
    )
    seed_saturated = data["seed"].get("seed_cycle_cut_branch_saturated") is True
    signed_cycle_closed = data["signed"].get("signed_lane_cycle_closed") is True
    payload_rows = data["payload"].get("decision_rows", [])
    payload_reduced = any(
        item.get("gate") == "NewPrimitiveExitReducedToSourceAtomOrExternalRoutes"
        and item.get("closed") is True
        for item in payload_rows
        if isinstance(item, dict)
    )
    source_rank_atomized = (
        data["source_rank"].get("preterminal_fiber_dispersion_source_atomization_closed") is True
        or data["source_rank"].get("deterministic_source_atom_implication_closed") is True
    )
    new_joint_absorbed = (
        data["new_joint_alpha"].get("new_joint_trace_cycle_still_absorbed") is True
        or data["new_joint_alpha"].get("current_new_joint_alpha_frontier_imported") is True
    )
    return [
        row(
            "PreviousA1AbsorptionImported",
            previous_ok,
            True,
            "上一层已删除 A1 source-admission 活动伪出口，并把内部线压到 seed/PDEC/payload/new-joint 四口。",
            "继续同步 seed-cycle-cut 与 payload 后续饱和证书。",
        ),
        row(
            "SeedCycleCutBranchSaturated",
            seed_saturated,
            False,
            "现有 strict seed-cycle-cut 直接攻坚已经说明顺序拆分与 terminal descent 都回到固定点或宏循环。",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "SeedCycleCutRemovedAsIndependentOR",
            previous_ok and seed_saturated,
            True,
            "seed-cycle-cut 不能继续作为两条替代线中的独立活动 OR；它只把负担转交给 same-set PDEC 或 new-joint 工件。",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "SignedLaneCycleImportedForPayload",
            signed_cycle_closed,
            True,
            "signed payload/trace/origin/common-packet 已形成闭环；payload 标签若不新增字段，只是环内改名。",
            NEW_ATOMIC_PAYLOAD,
        ),
        row(
            "JointPayloadNameRequiresAtomicPayloadContract",
            signed_cycle_closed,
            False,
            "`NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle` 必须实例化为 pre-Cauchy atomic signed payload/trace 工件；否则不能作为证明原子。",
            NEW_ATOMIC_PAYLOAD,
        ),
        row(
            "AtomicPayloadReducedToSourceRankPackage",
            payload_reduced,
            False,
            "已有 new primitive payload source-atom alignment 说明真正新 payload 必须携带 actual source-rank/no-collapse 包。",
            SOURCE_RANK_PACKAGE,
        ),
        row(
            "SourceRankPackageAtomized",
            source_rank_atomized,
            False,
            "preterminal fiber dispersion 证书把 source-rank/no-collapse 包拆成源域熵、complete key 与 fixed-key exact-UV 局部重数。",
            f"{SOURCE_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "NewJointStillNotFormulaArtifact",
            new_joint_absorbed,
            False,
            "new-joint 继续下钻会进入 alpha/trace/signed-lane 已识别回流；若要保留，必须提交新的显式 alpha/delta 公式工件。",
            NEW_JOINT,
        ),
        row(
            "RateAndCleanKLSStillCarried",
            True,
            False,
            "seed/payload 饱和只删伪出口，不支付 rate-bearing PDEC/CleanKLS 或 moving-atom rate preservation。",
            f"{PDEC_RATE} AND {RATE}",
        ),
        row(
            "DStructureGateStillOpen",
            data["dstructure"].get("row_column_unconditional_closed") is False,
            False,
            "DStructure/Rankin 仍需独立接受，或提交完整自足替代包。",
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ),
        row(
            "ExternalLemmaBoundaryUnchanged",
            True,
            False,
            "外部引理版仍只在 FullS-KLS 外部合同与 DStructure 独立接受同时给定时条件闭合。",
            f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只删除 seed/payload 两个伪独立活动口；PDEC、new-joint/source-rank、rate 与 DStructure 均未闭合。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "seed": read_json(SEED_FRONTIER),
        "signed": read_json(SIGNED_LANE),
        "payload": read_json(PAYLOAD_ALIGNMENT),
        "source_rank": read_json(SOURCE_RANK),
        "new_joint_alpha": read_json(NEW_JOINT_ALPHA),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "two_replacement_lines_seed_payload_saturation_sync_router",
        "status": "two_replacement_lines_seed_payload_saturated_to_pdec_newjoint_sourcerank_rate_dstructure_open",
        "source_hashes": source_hashes(),
        "seed_cycle_cut_active_after_sync": False,
        "new_joint_payload_active_as_standalone_after_sync": False,
        "new_atomic_payload_contract_required": True,
        "source_rank_package_required_for_payload": True,
        "external_lemma_version_closed_conditionally": True,
        "external_no_blackbox_version_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "internal_basis_after_sync": full_internal_basis(),
        "source_rank_package_expanded": source_rank_atoms(),
        "external_lemma_basis_after_sync": f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}",
        "external_no_blackbox_basis_after_sync": (
            "(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR "
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR "
            f"NewAutomorphicDispersionProof) AND {DSTRUCTURE_GATE}"
        ),
        "direct_attack_atoms_after_sync": [
            PDEC_SCOPE,
            NEW_JOINT,
            SOURCE_ENTROPY,
            COMPLETE_KEY,
            FIXED_KEY,
            TERMINAL_DESCENT,
            PDEC_RATE,
            RATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ],
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "plain_conclusion": (
            "`AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput` 已由 strict seed-cycle-cut "
            "饱和证书压回 same-set PDEC 或 new-joint 公式，不能继续作为两条替代线的独立 OR。"
            "`NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle` 若要有数学内容，必须实例化为 "
            "pre-Cauchy atomic signed payload/trace，并进一步支付 source-rank/no-collapse 三原子。"
            "因此本层把内部线压到 PDEC、new-joint、source-rank 三原子、terminal/外部受控输入、"
            "rate-bearing PDEC、RatePreservation 与 DStructure/Rankin；仍未得到无条件闭合。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines: list[str] = [
        "# Prime Matrix 两条替代线 seed/payload 饱和同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"seed_cycle_cut_active_after_sync={fmt_bool(payload['seed_cycle_cut_active_after_sync'])}",
        f"new_joint_payload_active_as_standalone_after_sync={fmt_bool(payload['new_joint_payload_active_as_standalone_after_sync'])}",
        f"new_atomic_payload_contract_required={fmt_bool(payload['new_atomic_payload_contract_required'])}",
        f"source_rank_package_required_for_payload={fmt_bool(payload['source_rank_package_required_for_payload'])}",
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
            "其中 payload/source-rank 包展开为：",
            "",
            "```text",
            payload["source_rank_package_expanded"],
            "```",
            "",
            "## 4. 外部两线",
            "",
            "外部引理版仍只是条件闭合：",
            "",
            "```text",
            payload["external_lemma_basis_after_sync"],
            "```",
            "",
            "无黑箱外部版仍需同对象 theorem-match 或新证明：",
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
    lines.extend(
        [
            "",
            "## 6. 状态快照",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in payload["status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in payload["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """执行证书生成。"""
    write_outputs(build_payload())


if __name__ == "__main__":
    main()
