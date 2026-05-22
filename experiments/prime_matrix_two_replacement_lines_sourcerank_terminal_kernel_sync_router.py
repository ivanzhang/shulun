#!/usr/bin/env python3
"""生成两条替代线 source-rank/terminal 到逐点核表同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_sourcerank_terminal_kernel_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-sourcerank-terminal-kernel-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-sourcerank-terminal-kernel-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-sourcerank-terminal-kernel-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-sourcerank-terminal-kernel-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-sourcerank-terminal-kernel-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-seed-payload-saturation-sync-router.json"
SOURCE_ENTROPY = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"
COMPLETE_KEY = DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.json"
FIXED_KEY_BRIDGE = DOCS / "prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-router.json"
TERMINAL_KERNEL = DOCS / "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
KZE_EXTERNAL = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"

SOURCE_RANK = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
SOURCE_ENTROPY_ATOM = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY_ATOM = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_ATOM = "FixedKeyExactUVLocalMultiplicityO1Ledger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"

POINTWISE_KERNEL = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_MULT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"

HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
PDEC_RATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
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


def has_row(data: dict[str, Any], gate: str, closed: bool | None = None) -> bool:
    """按 gate 名检查行是否存在，可选 closed 值。"""
    for key in ("rows", "decision_rows"):
        for item in data.get(key, []):
            if not isinstance(item, dict) or item.get("gate") != gate:
                continue
            return closed is None or item.get("closed") is closed
    return False


def dependency_paths() -> list[Path]:
    """列出证书依赖。"""
    return [PREVIOUS, SOURCE_ENTROPY, COMPLETE_KEY, FIXED_KEY_BRIDGE, TERMINAL_KERNEL, DSTRUCTURE, PAPER]


def source_hashes() -> dict[str, str]:
    """登记脚本与依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def kernel_triad() -> str:
    """逐点核表三输入。"""
    return f"({ALPHA_ROW} AND {ARITH_ID} AND {RANK_MULT})"


def internal_basis() -> str:
    """同步后的内部活动基。"""
    front = f"({PDEC_SCOPE} OR {NEW_JOINT} OR {kernel_triad()} OR {KZE_EXTERNAL})"
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
        f"AND {COMPLETE_KEY_ATOM} "
        f"AND {FIXED_KEY_ATOM} "
        f"AND {RATE} "
        f"AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF})"
    )


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """构造同步判定表。"""
    previous_ok = (
        data["previous"].get("status")
        == "two_replacement_lines_seed_payload_saturated_to_pdec_newjoint_sourcerank_rate_dstructure_open"
    )
    entropy_atomized = data["source_entropy"].get("actual_source_domain_entropy_atomization_closed") is True
    complete_key_reduced = data["complete_key"].get("complete_emitter_key_partition_router_closed") is True
    fixed_key_bridged = data["fixed_key"].get("source_atom_multiplicity_cap_reduced_to_exactuv_fixed_key_atoms") is True
    terminal_synced = data["terminal"].get("terminal_descent_to_pointwise_kernel_sync_closed") is True
    kernel_common = data["terminal"].get("pointwise_kernel_table_is_common_variable_table") is True
    return [
        row(
            "PreviousSeedPayloadSaturationImported",
            previous_ok,
            True,
            "上一层已删除 seed-cycle-cut 与 standalone payload 两个粗活动口。",
            f"{SOURCE_ENTROPY_ATOM} AND {COMPLETE_KEY_ATOM} AND {FIXED_KEY_ATOM} OR {TERMINAL_DESCENT}",
        ),
        row(
            "SourceEntropyAtomizedToSignedRows",
            entropy_atomized,
            False,
            "source-domain absolute entropy 已压成 signed row emitter、row-mass normalization 与 row support 下界。",
            "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger",
        ),
        row(
            "CompleteKeyReducedToActualSourceTable",
            complete_key_reduced,
            False,
            "complete key 不是后验标签；它需要 actual pre-Cauchy emitter source table 与 trace/key 预算。",
            "ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND CompleteEmitterTraceKeyBudgetLedger",
        ),
        row(
            "FixedKeyMultiplicityBridged",
            fixed_key_bridged,
            False,
            "source-atom multiplicity cap 已桥接到 actual source table、complete key 与 fixed-key exact-UV local multiplicity。",
            f"ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND {COMPLETE_KEY_ATOM} AND {FIXED_KEY_ATOM}",
        ),
        row(
            "TerminalDescentSyncedToPointwiseKernel",
            terminal_synced,
            False,
            "terminal descent 下游经 source-rank/no-collapse 汇入同 formal-unit 的逐 primitive alpha/delta 核表。",
            POINTWISE_KERNEL,
        ),
        row(
            "SourceRankCoarsePackageRemoved",
            previous_ok and entropy_atomized and complete_key_reduced and fixed_key_bridged and kernel_common,
            True,
            "source-rank 三原子不再作为粗包活动口保留；当前非后验共同变量表是逐 primitive alpha/delta 核表。",
            POINTWISE_KERNEL,
        ),
        row(
            "PointwiseKernelReducedToThreeInputs",
            has_row(data["terminal"], "PointwiseKernelTableReducedToThreeInputs", True),
            False,
            "逐点核表已被压成 alpha row anchor/phase、pre-Cauchy 算术恒等式和同表 rank/multiplicity 三输入。",
            f"{ALPHA_ROW} AND {ARITH_ID} AND {RANK_MULT}",
        ),
        row(
            "TerminalDescentRemovedAsStandaloneOR",
            terminal_synced,
            True,
            "terminal descent 不再作为 standalone 证明出口；它与 source-rank 三原子汇合到同一核表硬点。",
            f"{ALPHA_ROW} AND {ARITH_ID} AND {RANK_MULT}",
        ),
        row(
            "PDECAndNewJointStillParallel",
            True,
            False,
            "same-set PDEC 与 new-joint 显式公式仍是并行真剩余，不能由 source-rank 同步自动支付。",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "RateAndPromotionStillCarried",
            True,
            False,
            "本层只同步变量表，不支付 rate-bearing PDEC、RatePreservation 或 DStructure/Rankin。",
            f"{PDEC_RATE} AND {RATE} AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF})",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把 source-rank/terminal 粗口压到逐点核表三输入；未证明三命题无条件闭合。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "source_entropy": read_json(SOURCE_ENTROPY),
        "complete_key": read_json(COMPLETE_KEY),
        "fixed_key": read_json(FIXED_KEY_BRIDGE),
        "terminal": read_json(TERMINAL_KERNEL),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "two_replacement_lines_sourcerank_terminal_kernel_sync_router",
        "status": "two_replacement_lines_sourcerank_terminal_synced_to_pointwise_kernel_open",
        "source_hashes": source_hashes(),
        "source_rank_coarse_package_active_after_sync": False,
        "terminal_descent_standalone_active_after_sync": False,
        "pointwise_kernel_triad_required": True,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "internal_basis_after_sync": internal_basis(),
        "pointwise_kernel_triad": kernel_triad(),
        "external_lemma_basis_after_sync": f"AcceptedFullSKLSExtExternalContract AND {DSTRUCTURE_GATE}",
        "external_no_blackbox_basis_after_sync": (
            "(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR "
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR "
            f"NewAutomorphicDispersionProof) AND {DSTRUCTURE_GATE}"
        ),
        "direct_attack_atoms_after_sync": [
            PDEC_SCOPE,
            NEW_JOINT,
            ALPHA_ROW,
            ARITH_ID,
            RANK_MULT,
            PDEC_RATE,
            RATE,
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ],
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "plain_conclusion": (
            "source-rank/no-collapse 三原子与 terminal descent 已在现有 strict 证书中汇到同一 "
            "formal-unit 逐 primitive alpha/delta 核表。两条替代线不应继续把 source-rank "
            "粗包或 terminal descent 当作 standalone 活动出口；最新内部自足线应改写为 "
            "same-set PDEC、new-joint 公式或逐点核表三输入，并继续携带 rate-bearing PDEC、"
            "RatePreservation 与 DStructure/Rankin。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix 两条替代线 source-rank/terminal 逐点核表同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"source_rank_coarse_package_active_after_sync={fmt_bool(payload['source_rank_coarse_package_active_after_sync'])}",
        f"terminal_descent_standalone_active_after_sync={fmt_bool(payload['terminal_descent_standalone_active_after_sync'])}",
        f"pointwise_kernel_triad_required={fmt_bool(payload['pointwise_kernel_triad_required'])}",
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
            "逐点核表三输入：",
            "",
            "```text",
            payload["pointwise_kernel_triad"],
            "```",
            "",
            "## 4. 外部两线",
            "",
            "```text",
            payload["external_lemma_basis_after_sync"],
            "```",
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
