#!/usr/bin/env python3
"""生成两条替代线 A1 source-admission 吸收同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_source_admission_absorption_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-source-admission-absorption-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-source-admission-absorption-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-source-admission-absorption-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-source-admission-absorption-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-source-admission-absorption-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-source-root-nocycle-sync-router.json"
A1_ABSORB = DOCS / "prime-matrix-strict-source-admission-branch-absorption-router.json"
A1_MACRO = DOCS / "prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-router.json"
A1_BRANCH = DOCS / "prime-matrix-triad-a1-canonical-branch-admission-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

A1 = "A1CleanBranchCanonicalSourceAdmission"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_PAYLOAD = "NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
KZE_EXTERNAL = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
PDEC_RATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
DSTRUCTURE_SELF = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"


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
    return [PREVIOUS, A1_ABSORB, A1_MACRO, A1_BRANCH, DSTRUCTURE, PAPER]


def source_hashes() -> dict[str, str]:
    """登记脚本与依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """构造同步判定表。"""
    a1_absorbed = data["a1_absorb"].get("source_admission_absorbed_from_active_or") is True
    macro_to_break = data["a1_macro"].get("latest_internal_route_reduced_to_outside_cycle_break") is True
    branch_scope = data["a1_branch"].get("canonical_source_branch_is_legal_subcase") is True
    return [
        row(
            "PreviousSourceRootNoCycleImported",
            data["previous"].get("status")
            == "two_replacement_lines_source_root_nocycle_reduced_to_a1_pdec_rate_dstructure_open",
            True,
            "上一层已把 source-root 活动原子替换为 A1 source-admission、same-set PDEC 或 new-joint 证书。",
            "继续同步 A1 source-admission 后续证书。",
        ),
        row(
            "A1BranchStatementCoverageImported",
            branch_scope,
            True,
            "A1 canonical source admission 是分支陈述：canonical RIW/Buchstab 子分支可内部处理，generic/noncanonical 分支必须外部化或回流。",
            "A1CanonicalSourceBranchStatementAndCoverage",
        ),
        row(
            "A1AdmissionAbsorbedFromActiveOR",
            a1_absorbed,
            True,
            "把 A1 准入作为独立 OR 终端会把 scoped 分支边界误当全局排斥；因此它应从两条替代线活动 OR 中吸收掉。",
            "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion",
        ),
        row(
            "PostAdmissionMacrocycleImported",
            macro_to_break,
            True,
            "继续沿 A1/PDEC/new-joint/KZ/KZ-E 下钻会回到宏循环；非循环推进必须提交循环外输入。",
            f"{SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_PAYLOAD} OR {KZE_EXTERNAL}",
        ),
        row(
            "SeedCycleCutStillOpen",
            True,
            False,
            "循环外首选输入 seed cycle-cut primitive basis/coefficient source 当前尚未证明。",
            SEED_CYCLE_CUT,
        ),
        row(
            "PDECScopeStillOpen",
            True,
            False,
            "same-set PDEC scope 仍需同 formal unit、坏窗集合、U_CRT/L_PDEC 与质量推前同口径证书。",
            PDEC_SCOPE,
        ),
        row(
            "PayloadOutsideSignedLaneStillOpen",
            True,
            False,
            "new primitive/joint payload 若要破环，必须在 signed-lane/source-entropy 自证环之外给出 pre-Cauchy 工件。",
            f"{NEW_PAYLOAD} OR {NEW_JOINT}",
        ),
        row(
            "RateBearingPDECAndRateCarried",
            True,
            False,
            "A1 吸收只删除分支伪终端；它不支付 rate-bearing PDEC/CleanKLS 或 moving-atom 速率保持。",
            f"{PDEC_RATE} AND {RATE}",
        ),
        row(
            "DStructureReplacementStillOpen",
            data["dstructure"].get("row_column_unconditional_closed") is False,
            False,
            "DStructure/Rankin 独立接受或完整自足替代包仍是最终晋级门。",
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ),
        row(
            "A1RemovedFromTwoReplacementLines",
            a1_absorbed and macro_to_break,
            True,
            "两条替代线最新内部基不应再把 A1 source-admission 列为活动证明原子。",
            f"({SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_PAYLOAD} OR {NEW_JOINT}) AND {PDEC_RATE} AND {RATE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只吸收 A1 分支陈述伪出口；循环外输入、rate 与 DStructure 均未闭合。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "a1_absorb": read_json(A1_ABSORB),
        "a1_macro": read_json(A1_MACRO),
        "a1_branch": read_json(A1_BRANCH),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    internal_basis = (
        f"(({SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_PAYLOAD} OR {NEW_JOINT}) AND {HIGH_MODEL}) "
        f"AND ({PDEC_RATE} OR PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR NoFurtherCanonicalSourceTerminalPromotionGap) "
        "AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward "
        "AND JointEmitterPrepushforwardWordCoefficientIdentityLedger "
        "AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger "
        "AND ActualEmitterSourceDomainEntropyLedger "
        "AND ExactUVMapFixedPairPolylogFiberBoundLedger "
        "AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward "
        "AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger "
        "AND CompletePrimitiveEmitterKeyPartitionLedger "
        "AND FixedKeyExactUVLocalMultiplicityO1Ledger "
        f"AND {RATE} AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF})"
    )
    conditional_external_basis = (
        f"({SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_PAYLOAD} OR {KZE_EXTERNAL}) "
        f"AND {PDEC_RATE} AND {RATE} AND {DSTRUCTURE_GATE}"
    )
    return {
        "certificate_type": "two_replacement_lines_source_admission_absorption_sync_router",
        "status": "two_replacement_lines_a1_source_admission_absorbed_to_outside_cycle_break_open",
        "source_hashes": source_hashes(),
        "a1_source_admission_active_after_sync": False,
        "source_root_active_after_sync": False,
        "external_lemma_version_closed_conditionally": True,
        "external_no_blackbox_version_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "internal_basis_after_sync": internal_basis,
        "conditional_external_basis_after_sync": conditional_external_basis,
        "external_lemma_basis_after_sync": f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}",
        "external_no_blackbox_basis_after_sync": (
            "(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR "
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR "
            f"NewAutomorphicDispersionProof) AND {DSTRUCTURE_GATE}"
        ),
        "direct_attack_atoms_after_sync": [
            SEED_CYCLE_CUT,
            PDEC_SCOPE,
            NEW_PAYLOAD,
            NEW_JOINT,
            PDEC_RATE,
            RATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ],
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "plain_conclusion": (
            "`A1CleanBranchCanonicalSourceAdmission` 在 strict source-admission branch absorption "
            "与 post-source-admission macrocycle 证书中已经被识别为 scoped 分支边界，而不是全局排斥原子。"
            "因此两条替代线最新内部基应删除 A1 活动 OR，改写为循环外 seed cycle-cut、same-set PDEC、"
            "new joint/payload 工件，另乘 rate-bearing PDEC、RatePreservation 与 DStructure/Rankin。"
            "外部引理版仍是条件闭合；内部自足版仍未闭合。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines: list[str] = [
        "# Prime Matrix 两条替代线 A1 source-admission 吸收同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"a1_source_admission_active_after_sync={fmt_bool(payload['a1_source_admission_active_after_sync'])}",
        f"source_root_active_after_sync={fmt_bool(payload['source_root_active_after_sync'])}",
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
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
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
            "## 4. 条件外部 KZ 支路",
            "",
            "```text",
            payload["conditional_external_basis_after_sync"],
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
    lines.extend(
        [
            "",
            "## 7. 状态快照",
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
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    """入口。"""
    payload = build_payload()
    write_outputs(payload)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
