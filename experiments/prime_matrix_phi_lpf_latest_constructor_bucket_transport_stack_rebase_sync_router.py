#!/usr/bin/env python3
"""生成 latest constructor bucket transport stack 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_bucket_transport_stack_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_BUCKET_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-router.json"
)
TRANSPORT_STACK_CERT = DOCS / "prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync-router.json"
BUCKET_TRANSPORT_CERT = DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json"
STEP_UPDATE_CERT = DOCS / "prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json"
SOURCE_PACKET_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"

SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
EDGE_MULTIPLIER = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SOURCE_EXACTUV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
HARMONIC = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
TERMINAL_WFD = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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


def dependency_paths() -> list[Path]:
    """返回本层依赖证书。"""
    return [
        LATEST_BUCKET_CERT,
        TRANSPORT_STACK_CERT,
        BUCKET_TRANSPORT_CERT,
        STEP_UPDATE_CERT,
        SOURCE_PACKET_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def residual_core() -> str:
    """给出 transport-stack rebase 后的核心剩余。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT} AND {EDGE_MULTIPLIER}"


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    return (
        f"(({residual_core()} AND {SIGNED_SURVIVAL} AND {ROW_MASS}) OR {POINTWISE_TABLE} "
        f"OR {PDEC_SCOPE} OR {TERMINAL_WFD}) AND {SOURCE_EXACTUV} AND {COMPLETE_KEY} "
        f"AND {FIXED_KEY} AND {HARMONIC} AND {SKELETON} AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(
    latest: dict[str, Any],
    stack: dict[str, Any],
    bucket: dict[str, Any],
    step: dict[str, Any],
    packet: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 rebase 同步判定表。"""
    latest_bucket_active = (
        latest.get("next_primary_attack_target") == SIGNED_LAW
        and latest.get("noncircular_kernel_coarse_target_removed") is True
    )
    transport_stack_imported = (
        stack.get("target_input_before_router") == SIGNED_LAW
        and stack.get("next_primary_attack_target") == EDGE_MULTIPLIER
        and bucket.get("next_direct_attack_target") == "PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward"
    )
    step_imported = (
        step.get("next_direct_attack_target") == EDGE_MULTIPLIER
        and step.get("step_update_reduced_to_edge_multiplier_table") is True
    )
    packet_imported = (
        packet.get("common_packet_self_proof_blocked") is True
        or packet.get("common_packet_self_proof_rejected_after_lpf") is True
    )
    rebase_closed = latest_bucket_active and transport_stack_imported and step_imported and packet_imported
    return [
        row(
            "LatestConstructorBucketSignedLawImported",
            latest_bucket_active,
            False,
            "上一层最新 constructor kernel-bucket 同步已把主攻压到 Phi-LPF bucket signed law。",
            SIGNED_LAW,
        ),
        row(
            "ExistingTransportStackImported",
            transport_stack_imported,
            False,
            "既有 constructor transport-stack 证书可复用：bucket signed law 若不走逐点表，就进入 rough-cofactor transport stack。",
            f"{residual_core()} OR {POINTWISE_TABLE}",
        ),
        row(
            "StepUpdateEdgeMultiplierImported",
            step_imported,
            False,
            "ordered path 固定后，rough-cofactor step local-factor update 等价于逐 edge signed multiplier 表。",
            EDGE_MULTIPLIER,
        ),
        row(
            "SourcePacketCycleGuardImported",
            packet_imported,
            True,
            "common packet 自证环已被切断，base/source 侧剩三原子而非闭合证明。",
            f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        ),
        row(
            "SignedSideGatesCarried",
            SIGNED_SURVIVAL in latest.get("parallel_attack_targets", [])
            and ROW_MASS in latest.get("parallel_attack_targets", []),
            False,
            "signed survival 与 same-formal-unit row-mass/no-heavy-row 仍随 constructor 主线强制保留。",
            f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "BucketTransportStackRebased",
            rebase_closed,
            False,
            "新 kernel-bucket 层已接到旧 transport stack，下一个窄口为 edge multiplier 或 source 三原子。",
            residual_core(),
        ),
        row(
            "EdgeMultiplierCurrentCorpusProved",
            False,
            False,
            "当前材料没有逐 ordered edge 的 signed multiplier 表。",
            EDGE_MULTIPLIER,
        ),
        row(
            "SourceThreeAtomsCurrentCorpusProved",
            False,
            False,
            "当前材料没有同时提交 alpha anchor emission、独立算术恒等式与 same-unit ExactUV rank multiplicity。",
            f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 rebase 同步；未证明 edge multiplier、source 三原子、signed survival、row-mass、ExactUV 或 DStructure。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json(LATEST_BUCKET_CERT)
    stack = load_json(TRANSPORT_STACK_CERT)
    bucket = load_json(BUCKET_TRANSPORT_CERT)
    step = load_json(STEP_UPDATE_CERT)
    packet = load_json(SOURCE_PACKET_CERT)
    rows = build_rows(latest, stack, bucket, step, packet)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_bucket_transport_stack_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_bucket_transport_stack_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_constructor_bucket_signed_law_imported": rows[0]["closed"],
        "existing_transport_stack_imported": rows[1]["closed"],
        "step_update_edge_multiplier_imported": rows[2]["closed"],
        "source_packet_cycle_guard_imported": rows[3]["closed"],
        "signed_side_gates_carried": rows[4]["closed"],
        "bucket_transport_stack_rebased": rows[5]["closed"],
        "edge_signed_multiplier_table_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SIGNED_LAW,
        "next_primary_attack_target": EDGE_MULTIPLIER,
        "parallel_primary_attack_target": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": retained_basis(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 constructor kernel-bucket 证书得到的 `PhiLPFBucketSignedCoefficientLawBeforePushforward` "
            "重新接到既有 transport stack。结论是：若不直接提交逐 Phi-LPF bucket signed value table，"
            "bucket signed law 必须经过 rough-cofactor transport；ordered path 与 square-base 私有出口已关闭，"
            "剩余收窄为逐 edge signed multiplier 表以及 source-packet 三原子，并且 signed survival 与 row-mass/no-heavy-row "
            "仍并行保留。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor bucket transport-stack rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_bucket_signed_law_imported={fmt_bool(result['latest_constructor_bucket_signed_law_imported'])}",
        f"existing_transport_stack_imported={fmt_bool(result['existing_transport_stack_imported'])}",
        f"step_update_edge_multiplier_imported={fmt_bool(result['step_update_edge_multiplier_imported'])}",
        f"source_packet_cycle_guard_imported={fmt_bool(result['source_packet_cycle_guard_imported'])}",
        f"signed_side_gates_carried={fmt_bool(result['signed_side_gates_carried'])}",
        f"bucket_transport_stack_rebased={fmt_bool(result['bucket_transport_stack_rebased'])}",
        f"edge_signed_multiplier_table_proved={fmt_bool(result['edge_signed_multiplier_table_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"independent_noncanonical_arithmetic_identity_proved={fmt_bool(result['independent_noncanonical_arithmetic_identity_proved'])}",
        f"same_unit_exactuv_rank_multiplicity_proved={fmt_bool(result['same_unit_exactuv_rank_multiplicity_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 最新保留基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
            "```",
            "",
            "下一内部主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "并行 source 三原子：",
            "",
            "```text",
            result["parallel_primary_attack_target"],
            "```",
            "",
            "直接旁路：",
            "",
            "```text",
            result["parallel_direct_bypass"],
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 3. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
