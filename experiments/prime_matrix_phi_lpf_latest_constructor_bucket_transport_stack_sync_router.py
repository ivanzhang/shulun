#!/usr/bin/env python3
"""生成 constructor-latest bucket signed-law 到 transport stack 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_bucket_transport_stack_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR_BUCKET_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-router.json"
)
BUCKET_TRANSPORT_CERT = DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json"
UNIT_SEED_CERT = DOCS / "prime-matrix-phi-lpf-signed-transport-unit-seed-router.json"
ORDERED_COHERENCE_CERT = (
    DOCS / "prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json"
)
STEP_UPDATE_CERT = DOCS / "prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json"
SQUARE_BASE_CERT = DOCS / "prime-matrix-phi-lpf-square-base-source-packet-reduction-router.json"
SOURCE_PACKET_CYCLE_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"

SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
ROUGH_TRANSPORT = "PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward"
SIGNED_SUM_IDENTITY = "PhiLPFBucketPrepushforwardSignedSumIdentity"
UNIT_SEED = "PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward"
STEP_UPDATE = "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward"
ORDERED_COHERENCE = "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
EDGE_MULTIPLIER = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
SQUARE_DECL = "PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
NONZERO_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失文件只表示该依赖未证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值渲染成小写文本。"""
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
    """汇总本证书及依赖证书哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_CONSTRUCTOR_BUCKET_CERT,
        BUCKET_TRANSPORT_CERT,
        UNIT_SEED_CERT,
        ORDERED_COHERENCE_CERT,
        STEP_UPDATE_CERT,
        SQUARE_BASE_CERT,
        SOURCE_PACKET_CYCLE_CERT,
        POINTWISE_FRONTIER_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出 constructor-latest bucket law 的同步链。"""
    return [
        {
            "from": SIGNED_LAW,
            "to": f"({ROUGH_TRANSPORT} OR {POINTWISE_TABLE}) AND {SIGNED_SUM_IDENTITY}",
            "meaning": "latest constructor row-origin 后的 bucket signed law 仍要么给逐点表，要么给 rough-cofactor signed transport。",
        },
        {
            "from": ROUGH_TRANSPORT,
            "to": f"{UNIT_SEED} AND {STEP_UPDATE} AND {ORDERED_COHERENCE}",
            "meaning": "transport 递推需要启动 seed、逐步 local-factor update 和 ordered factorization coherence。",
        },
        {
            "from": ORDERED_COHERENCE,
            "to": "closed ordered LPF path",
            "meaning": "ordered path 是 LPF 非降素因子词的唯一性事实；它不是 signed 生成源。",
        },
        {
            "from": STEP_UPDATE,
            "to": EDGE_MULTIPLIER,
            "meaning": "路径固定后，step update 的 signed 内容等价于逐 ordered edge signed multiplier 表。",
        },
        {
            "from": UNIT_SEED,
            "to": f"{SQUARE_DECL} -> {COMMON_PACKET}",
            "meaning": "virtual unit 是 Phi 公式排除的 prime-row 修正，square-base 私有出口已并回 common packet。",
        },
        {
            "from": COMMON_PACKET,
            "to": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
            "meaning": "common packet 不能自证；source-packet cycle guard 把非循环要求压到三原子。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 constructor-latest transport stack 判定表。"""
    latest = data["latest"]
    bucket = data["bucket"]
    unit_seed = data["unit_seed"]
    ordered = data["ordered"]
    step = data["step"]
    square = data["square"]
    packet = data["packet"]
    pointwise = data["pointwise"]
    parallel = set(latest.get("parallel_primary_attack_targets", []))
    return [
        row(
            "LatestConstructorBucketLawImported",
            latest.get("next_primary_attack_target") == SIGNED_LAW
            and latest.get("row_origin_table_reduced_to_phi_lpf_bucket_signed_law") is True,
            False,
            "上一层 constructor row-origin 已把最新 hardpoint 压到 Phi-LPF bucket signed law。",
            SIGNED_LAW,
        ),
        row(
            "ConstructorSideGatesCarried",
            ROW_MASS in parallel and NONZERO_SURVIVAL in parallel,
            False,
            "本层只替换 bucket signed law；signed survival 与同 formal unit row-mass/no-heavy-row 仍强制保留。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "BucketTransportRouterImported",
            bucket.get("target_input_before_router") == SIGNED_LAW
            and bucket.get("next_direct_attack_target") == ROUGH_TRANSPORT,
            False,
            "既有 bucket transport 证书把 signed law 压到 rough cofactor transport 或逐点 signed table。",
            f"{ROUGH_TRANSPORT} OR {POINTWISE_TABLE}",
        ),
        row(
            "UnitSeedBoundaryImported",
            unit_seed.get("next_direct_attack_target") == UNIT_SEED
            and unit_seed.get("phi_minus_one_prime_row_guard_imported") is True,
            False,
            "rough transport 的启动不能从 Phi 中减掉的 prime-row/unit 项偷渡，必须给 unit/square-base seed。",
            UNIT_SEED,
        ),
        row(
            "OrderedCoherenceClosed",
            ordered.get("rough_cofactor_ordered_factorization_coherence_proved") is True,
            True,
            "rough cofactor ordered coherence 已由 LPF ordered path 唯一性关闭。",
            "ordered coherence removed",
        ),
        row(
            "StepUpdateReducedToEdgeMultiplier",
            step.get("next_direct_attack_target") == EDGE_MULTIPLIER
            and step.get("step_update_reduced_to_edge_multiplier_table") is True,
            False,
            "ordered path 固定后，local-factor update 的 signed 内容就是逐 edge multiplier 表。",
            EDGE_MULTIPLIER,
        ),
        row(
            "SquareBasePrivateEscapeRemoved",
            square.get("no_square_base_private_signed_escape_proved") is True,
            True,
            "square-base root 的私有 signed 出口已排除，剩余并回 common packet。",
            COMMON_PACKET,
        ),
        row(
            "CommonPacketCycleGuardImported",
            packet.get("common_packet_self_proof_blocked") is True
            or packet.get("common_packet_self_proof_rejected_after_lpf") is True,
            True,
            "common packet 沿 signed-lane 展开会回到来源环，不能作为非循环自证。",
            f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        ),
        row(
            "PointwiseSignedTableStillOpen",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "直接提交逐 Phi-LPF bucket signed value table 仍是旁路，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "ConstructorBucketTransportResidual",
            True,
            False,
            "constructor-latest bucket law 的递推路线已同步为 source 三原子、edge multiplier、signed survival 与 row-mass 的合取。",
            f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT} AND {EDGE_MULTIPLIER} AND {NONZERO_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只做非循环同步；未证明 edge multiplier、source 三原子、signed survival、row-mass、ExactUV 或 DStructure。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    data = {
        "latest": load_json(LATEST_CONSTRUCTOR_BUCKET_CERT),
        "bucket": load_json(BUCKET_TRANSPORT_CERT),
        "unit_seed": load_json(UNIT_SEED_CERT),
        "ordered": load_json(ORDERED_COHERENCE_CERT),
        "step": load_json(STEP_UPDATE_CERT),
        "square": load_json(SQUARE_BASE_CERT),
        "packet": load_json(SOURCE_PACKET_CYCLE_CERT),
        "pointwise": load_json(POINTWISE_FRONTIER_CERT),
    }
    rows = build_rows(data)
    transport_branch = (
        f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT} AND {EDGE_MULTIPLIER} AND {ROW_MASS}"
    )
    latest_basis = (
        f"(({transport_branch}) OR {POINTWISE_TABLE} OR {SEED_CYCLE_CUT} OR {TERMINAL_DESCENT} "
        f"OR {PDEC_SCOPE} OR {NEW_JOINT}) AND {NONZERO_SURVIVAL} AND {COMPLETE_KEY} AND "
        f"{FIXED_KEY} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_bucket_transport_stack_sync_router",
        "status": "phi_lpf_latest_constructor_bucket_law_synced_to_transport_stack_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_constructor_bucket_law_imported": rows[0]["closed"],
        "constructor_side_gates_carried": rows[1]["closed"],
        "bucket_transport_router_imported": rows[2]["closed"],
        "unit_seed_boundary_imported": rows[3]["closed"],
        "ordered_coherence_closed": rows[4]["closed"],
        "step_update_reduced_to_edge_multiplier": rows[5]["closed"],
        "square_base_private_escape_removed": rows[6]["closed"],
        "common_packet_cycle_guard_imported": rows[7]["closed"],
        "pointwise_signed_table_proved": False,
        "edge_signed_multiplier_table_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SIGNED_LAW,
        "next_primary_attack_target": EDGE_MULTIPLIER,
        "parallel_primary_attack_target": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        "parallel_constructor_side_gates": f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": latest_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor-latest `PhiLPFBucketSignedCoefficientLawBeforePushforward` 接入既有 "
            "transport stack。LPF/Phi 已完成 unsigned support/capacity；若不直接提交逐点 signed table，"
            "bucket signed law 必须给 rough-cofactor signed transport。ordered path 和 square-base 私有出口"
            "已关闭，但 signed step multiplier、source-packet 三原子、signed survival 与 row-mass/no-heavy-row "
            "仍未证明；行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor bucket transport-stack sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_bucket_law_imported={fmt_bool(cert['latest_constructor_bucket_law_imported'])}",
        f"constructor_side_gates_carried={fmt_bool(cert['constructor_side_gates_carried'])}",
        f"bucket_transport_router_imported={fmt_bool(cert['bucket_transport_router_imported'])}",
        f"unit_seed_boundary_imported={fmt_bool(cert['unit_seed_boundary_imported'])}",
        f"ordered_coherence_closed={fmt_bool(cert['ordered_coherence_closed'])}",
        f"step_update_reduced_to_edge_multiplier={fmt_bool(cert['step_update_reduced_to_edge_multiplier'])}",
        f"square_base_private_escape_removed={fmt_bool(cert['square_base_private_escape_removed'])}",
        f"common_packet_cycle_guard_imported={fmt_bool(cert['common_packet_cycle_guard_imported'])}",
        f"edge_signed_multiplier_table_proved={fmt_bool(cert['edge_signed_multiplier_table_proved'])}",
        f"nonzero_signed_row_survival_proved={fmt_bool(cert['nonzero_signed_row_survival_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(cert['same_formal_unit_row_mass_normalization_proved'])}",
        f"pointwise_signed_table_proved={fmt_bool(cert['pointwise_signed_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行 source-packet 三原子：",
            "",
            "```text",
            cert["parallel_primary_attack_target"],
            "```",
            "",
            "并行 constructor 侧门：",
            "",
            "```text",
            cert["parallel_constructor_side_gates"],
            "```",
            "",
            "并行直接旁路：",
            "",
            "```text",
            cert["parallel_direct_bypass"],
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
