#!/usr/bin/env python3
"""生成两条替代线 source-root/no-cycle 最新同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_source_root_nocycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-source-root-nocycle-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-source-root-nocycle-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-source-root-nocycle-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-source-root-nocycle-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-source-root-nocycle-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync-router.json"
SOURCE_ROOT = DOCS / "prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json"
PDEC_SCOPE = DOCS / "prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json"
KZ_NOCYCLE = DOCS / "prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json"
KZE_SOURCE = DOCS / "prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

SOURCE_ROOT_ATOM = "ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn"
PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT_ATOM = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
A1_SOURCE_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
KZE_EXTERNAL = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
PDEC_RATE_GATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
RATE_GATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
DSTRUCTURE_SELF_CONTAINED = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"


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
    return [PREVIOUS, SOURCE_ROOT, PDEC_SCOPE, KZ_NOCYCLE, KZE_SOURCE, DSTRUCTURE, PAPER]


def source_hashes() -> dict[str, str]:
    """登记脚本与依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """构造同步判定表。"""
    source_root_removed = data["source_root"].get("forward_source_root_independent_after_router") is False
    pdec_saturated = data["pdec"].get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
    kze_to_a1 = data["kze"].get("kze_direct_current_internal_route_reduced_to_source_admission") is True
    dstructure_author_done = data["dstructure"].get("status") == (
        "dstructure_rankin_author_remainder_split_closed_self_contained_replacement_open"
    )

    return [
        row(
            "RateTailPreviousImported",
            data["previous"].get("status") == "two_replacement_lines_rate_tail_mertens_closed_terminal_gates_open",
            True,
            "上一层已经删除自足 PNT/Mertens 尾段旧硬点，并把内部线压到 source-root、PDEC/CleanKLS、Rate 与 DStructure。",
            "同步 source-root 后续证书。",
        ),
        row(
            "SourceRootTerminalCycleImported",
            source_root_removed,
            True,
            "forward source-root 的内部路线已经回到 signed/source-rank/alpha 终端环；它不再是可作为证明的独立非循环出口。",
            f"{PDEC_SCOPE_ATOM} OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse",
        ),
        row(
            "DirectPDECScopeSaturatedButUnproved",
            pdec_saturated,
            False,
            "direct same-set PDEC 作用域审计已导入；当前语料仍缺同 formal unit、坏窗集合、U_CRT/L_PDEC 与质量推前完全同口径的证书。",
            f"{PDEC_SCOPE_ATOM} OR {NEW_JOINT_ATOM}",
        ),
        row(
            "KZNoCycleGateReducedToDirectKZE",
            data["kz"].get("next_direct_attack_target")
            == "AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection",
            False,
            "不允许复用 NCBLK/source-root 后，现有 KZ-E 路线只剩直接 well-factorable dispersion log-saving。",
            "AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection",
        ),
        row(
            "KZEDirectReducedToA1SourceAdmission",
            kze_to_a1,
            False,
            "KZ-E no-projection 自足路线若不接受外部 DI/BFI/Kuznetsov 证书，就必须在 Cauchy/dispersion 前证明 clean A1 分支准入 canonical RIW/Buchstab source。",
            A1_SOURCE_ADMISSION,
        ),
        row(
            "ExternalNoProjectionStillConditional",
            data["kze"].get("exact_external_dibfi_kuznetsov_no_projection_certificate_accepted") is False,
            False,
            "外部 no-projection DI/BFI/Kuznetsov 可作为条件输入；它不能冒充内部自足证明。",
            KZE_EXTERNAL,
        ),
        row(
            "SourceRootAtomRemovedFromTwoReplacementLines",
            source_root_removed and kze_to_a1,
            True,
            "两条替代线的最新内部清单不应再把 source-root 当作活动原子；它应被替换为 A1 source admission、fresh same-set PDEC 或 new-joint 证书。",
            f"{A1_SOURCE_ADMISSION} OR {PDEC_SCOPE_ATOM} OR {NEW_JOINT_ATOM}",
        ),
        row(
            "RateBearingPDECGateCarried",
            True,
            False,
            "rate-bearing packet 的 PDEC/CleanKLS 承重门仍未由 source-root 同步自动支付。",
            PDEC_RATE_GATE,
        ),
        row(
            "RatePreservationStillOpen",
            data["kze"].get("rate_preservation_ledger_proved") is False,
            False,
            "moving-atom packet 的速率保持账本仍是独立承重门。",
            RATE_GATE,
        ),
        row(
            "DStructureAuthorSideSplitImported",
            dstructure_author_done,
            False,
            "DStructure/Rankin 作者侧普通剩余已归零；剩余是独立接受事件，或提交完整文内自足替代包。",
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF_CONTAINED}",
        ),
        row(
            "ExternalLemmaPackageConditionPinned",
            True,
            False,
            "外部引理版只有在 FullS-KLS 外部合同与 DStructure/Rankin 独立接受同时作为输入时闭合；这不是无条件证明。",
            f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}",
        ),
        row(
            "NoBlackboxExternalLineStillOpen",
            True,
            False,
            "无黑箱外部线仍需同对象 FullS theorem-match、actual source capacity 新定理或新的自守/dispersion 证明。",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof",
        ),
        row(
            "InternalSelfContainedCondensedToTwoFreshInputs",
            source_root_removed and pdec_saturated and kze_to_a1,
            False,
            "内部自足线当前只剩 fresh source-admission/PDEC-new-joint 入口，再乘以 rate-bearing PDEC、Rate 与 DStructure 替代包。",
            f"({A1_SOURCE_ADMISSION} OR {PDEC_SCOPE_ATOM} OR {NEW_JOINT_ATOM}) AND {PDEC_RATE_GATE} AND {RATE_GATE} AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF_CONTAINED})",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只替换旧 source-root 活动原子并压窄最新真剩余；外部引理版仍是条件闭合，内部自足版仍未闭合。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "source_root": read_json(SOURCE_ROOT),
        "pdec": read_json(PDEC_SCOPE),
        "kz": read_json(KZ_NOCYCLE),
        "kze": read_json(KZE_SOURCE),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)

    external_lemma_basis = f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}"
    external_no_blackbox_basis = (
        "(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR "
        "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR "
        f"NewAutomorphicDispersionProof) AND {DSTRUCTURE_GATE}"
    )
    internal_basis = (
        f"(({A1_SOURCE_ADMISSION} OR {PDEC_SCOPE_ATOM} OR {NEW_JOINT_ATOM}) AND {HIGH_MODEL}) "
        f"AND ({PDEC_RATE_GATE} OR PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR NoFurtherCanonicalSourceTerminalPromotionGap) "
        "AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward "
        "AND JointEmitterPrepushforwardWordCoefficientIdentityLedger "
        "AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger "
        "AND ActualEmitterSourceDomainEntropyLedger "
        "AND ExactUVMapFixedPairPolylogFiberBoundLedger "
        "AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward "
        "AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger "
        "AND CompletePrimitiveEmitterKeyPartitionLedger "
        "AND FixedKeyExactUVLocalMultiplicityO1Ledger "
        f"AND {RATE_GATE} AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF_CONTAINED})"
    )
    conditional_kz_external_basis = (
        f"({A1_SOURCE_ADMISSION} OR {KZE_EXTERNAL}) AND {HIGH_MODEL} "
        f"AND {RATE_GATE} AND {DSTRUCTURE_GATE}"
    )

    return {
        "certificate_type": "two_replacement_lines_source_root_nocycle_sync_router",
        "status": "two_replacement_lines_source_root_nocycle_reduced_to_a1_pdec_rate_dstructure_open",
        "source_hashes": source_hashes(),
        "source_root_active_after_sync": False,
        "external_lemma_version_closed_conditionally": True,
        "external_no_blackbox_version_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "external_lemma_basis_after_sync": external_lemma_basis,
        "external_no_blackbox_basis_after_sync": external_no_blackbox_basis,
        "conditional_kz_external_basis_after_sync": conditional_kz_external_basis,
        "internal_basis_after_sync": internal_basis,
        "direct_attack_atoms_after_sync": [
            A1_SOURCE_ADMISSION,
            PDEC_SCOPE_ATOM,
            NEW_JOINT_ATOM,
            PDEC_RATE_GATE,
            RATE_GATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF_CONTAINED}",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof",
        ],
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "plain_conclusion": (
            "rate-bearing Mertens 尾段闭合后留下的 source-root 活动原子已经可以用后续 strict "
            "source-root 终端环、direct PDEC scope 饱和、KZ no-cycle 与 KZ-E source-bridge "
            "证书替换。当前两条替代线不应继续把 source-root 当作独立非循环出口；内部自足线压到 "
            "A1 clean branch canonical source admission、fresh same-set PDEC/new-joint 证书、"
            "rate-bearing PDEC、RatePreservation 与 DStructure 自足替代包。外部引理版仍只在 "
            "AcceptedFullSKLSExtExternalContract 与 DStructure 独立接受同时给定时条件闭合；"
            "无黑箱外部版仍需同对象 FullS theorem-match 或新 dispersion 证明。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines: list[str] = [
        "# Prime Matrix 两条替代线 source-root/no-cycle 同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
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
            "## 3. 外部引理版",
            "",
            "```text",
            payload["external_lemma_basis_after_sync"],
            "```",
            "",
            "这只是条件闭合口径：FullS-KLS 外部合同和 DStructure/Rankin 独立接受必须同时作为输入。",
            "",
            "## 4. 无黑箱外部版",
            "",
            "```text",
            payload["external_no_blackbox_basis_after_sync"],
            "```",
            "",
            "泛称 FI/DI/BFI/Kuznetsov/Maynard 不足；必须匹配同一个 completed full-S non-AP WFD 对象、权重、窗口、模数范围、投影和误差预算。",
            "",
            "## 5. 内部自足版",
            "",
            "```text",
            payload["internal_basis_after_sync"],
            "```",
            "",
            "条件外部 KZ no-projection 支路仅可写为：",
            "",
            "```text",
            payload["conditional_kz_external_basis_after_sync"],
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
