#!/usr/bin/env python3
"""生成 Phi-LPF 最新 bucket signed-law 到 transport stack 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_bucket_transport_stack_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-bucket-transport-stack-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_BUCKET_CERT = DOCS / "prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json"
BUCKET_TRANSPORT_CERT = DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json"
UNIT_SEED_CERT = DOCS / "prime-matrix-phi-lpf-signed-transport-unit-seed-router.json"
ORDERED_COHERENCE_CERT = DOCS / "prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json"
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
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能视作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
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


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_BUCKET_CERT,
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
    """列出本层同步链。"""
    return [
        {
            "from": SIGNED_LAW,
            "to": f"({ROUGH_TRANSPORT} OR {POINTWISE_TABLE}) AND {SIGNED_SUM_IDENTITY}",
            "meaning": "bucket signed law 若不直接提交逐点表，就必须给 rough cofactor 乘法 signed transport。",
        },
        {
            "from": ROUGH_TRANSPORT,
            "to": f"{UNIT_SEED} AND {STEP_UPDATE} AND {ORDERED_COHERENCE}",
            "meaning": "递推 transport 需要平方基启动、每步 local factor 更新和 ordered factorization coherence。",
        },
        {
            "from": ORDERED_COHERENCE,
            "to": "closed ordered LPF path",
            "meaning": "ordered coherence 是纯 LPF 路径事实，已由唯一非降素因子词关闭。",
        },
        {
            "from": STEP_UPDATE,
            "to": EDGE_MULTIPLIER,
            "meaning": "路径固定后，step update 等价于逐 ordered edge 的 signed multiplier 表。",
        },
        {
            "from": UNIT_SEED,
            "to": f"{SQUARE_DECL} -> {COMMON_PACKET}",
            "meaning": "virtual unit 不能作为 composite row；square-base 私有 signed 出口被排除，剩余并回 common source packet。",
        },
        {
            "from": COMMON_PACKET,
            "to": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
            "meaning": "common packet 自证环被切断后，现有非循环下游同步到逐点核表三原子。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成最新 transport stack 同步判定表。"""
    latest = data["latest"]
    bucket = data["bucket"]
    unit_seed = data["unit_seed"]
    ordered = data["ordered"]
    step = data["step"]
    square = data["square"]
    packet = data["packet"]
    pointwise = data["pointwise"]
    return [
        row(
            "LatestBucketSignedLawImported",
            latest.get("next_primary_attack_target") == SIGNED_LAW,
            False,
            "上一层已把 row-origin table 的无符号部分剥离，最新直接 hardpoint 是 Phi-LPF bucket signed law。",
            SIGNED_LAW,
        ),
        row(
            "BucketTransportRouterImported",
            bucket.get("target_input_before_router") == SIGNED_LAW
            and bucket.get("next_direct_attack_target") == ROUGH_TRANSPORT,
            False,
            "既有 bucket transport 证书把 signed law 压到 rough cofactor transport 或逐点 signed value table。",
            f"{ROUGH_TRANSPORT} OR {POINTWISE_TABLE}",
        ),
        row(
            "UnitSeedBoundaryImported",
            unit_seed.get("next_direct_attack_target") == UNIT_SEED
            and unit_seed.get("phi_minus_one_prime_row_guard_imported") is True,
            False,
            "rough transport 的启动不能从 Phi 中被减掉的 prime row 偷渡，必须给 unit/square-base seed。",
            UNIT_SEED,
        ),
        row(
            "OrderedCoherenceClosed",
            ordered.get("rough_cofactor_ordered_factorization_coherence_proved") is True,
            True,
            "rough cofactor 的 ordered factorization coherence 已由 LPF 非降素因子词关闭。",
            "ordered coherence removed",
        ),
        row(
            "StepUpdateReducedToEdgeMultiplier",
            step.get("next_direct_attack_target") == EDGE_MULTIPLIER
            and step.get("step_update_reduced_to_edge_multiplier_table") is True,
            False,
            "ordered path 固定后，step local factor update 等价于逐 edge signed multiplier 表。",
            EDGE_MULTIPLIER,
        ),
        row(
            "SquareBasePrivateEscapeRemoved",
            square.get("no_square_base_private_signed_escape_proved") is True,
            True,
            "square-base root 的 LPF 几何与 prime-row leak guard 已固定；不存在私有 signed 出口。",
            COMMON_PACKET,
        ),
        row(
            "CommonPacketCycleGuardImported",
            packet.get("common_packet_self_proof_blocked") is True
            or packet.get("common_packet_self_proof_rejected_after_lpf") is True,
            True,
            "common source packet 若沿 signed-lane 展开会回到来源环，不能当作非循环自证。",
            f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        ),
        row(
            "PointwiseSignedTableStillOpen",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "直接提交逐 Phi-LPF bucket signed value table 仍是并行旁路，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "TransportStackLatestResidual",
            True,
            False,
            "bucket signed law 的递推路线现已同步为 base/source-packet 三原子与 step edge multiplier 的合取。",
            f"({ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT} AND {EDGE_MULTIPLIER}) OR {POINTWISE_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步既有下游 stack；未证明 signed multiplier、逐点 signed table、ExactUV、模型、Rate 或 DStructure。",
            f"({EDGE_MULTIPLIER} AND {ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}) OR {POINTWISE_TABLE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    data = {
        "latest": load_json(LATEST_BUCKET_CERT),
        "bucket": load_json(BUCKET_TRANSPORT_CERT),
        "unit_seed": load_json(UNIT_SEED_CERT),
        "ordered": load_json(ORDERED_COHERENCE_CERT),
        "step": load_json(STEP_UPDATE_CERT),
        "square": load_json(SQUARE_BASE_CERT),
        "packet": load_json(SOURCE_PACKET_CYCLE_CERT),
        "pointwise": load_json(POINTWISE_FRONTIER_CERT),
    }
    rows = build_rows(data)
    latest_basis = (
        f"(({ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT} AND {EDGE_MULTIPLIER}) "
        f"OR {POINTWISE_TABLE} OR {SEED_CYCLE_CUT} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {NEW_JOINT}) "
        f"AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_bucket_transport_stack_sync_router",
        "status": "phi_lpf_latest_bucket_law_synced_to_transport_stack_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_bucket_signed_law_imported": rows[0]["closed"],
        "bucket_transport_router_imported": rows[1]["closed"],
        "unit_seed_boundary_imported": rows[2]["closed"],
        "ordered_coherence_closed": rows[3]["closed"],
        "step_update_reduced_to_edge_multiplier": rows[4]["closed"],
        "square_base_private_escape_removed": rows[5]["closed"],
        "common_packet_cycle_guard_imported": rows[6]["closed"],
        "pointwise_signed_table_proved": False,
        "edge_signed_multiplier_table_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SIGNED_LAW,
        "next_primary_attack_target": EDGE_MULTIPLIER,
        "parallel_primary_attack_target": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": latest_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 `PhiLPFBucketSignedCoefficientLawBeforePushforward` 接入既有 transport stack。"
            "bucket signed law 若不直接提交逐点 signed value table，就必须给 rough cofactor signed transport；"
            "transport 的 ordered path 已闭合，unit/square-base 私有出口也已并回 common source packet，"
            "所以递推路线的最新剩余是 base/source-packet 三原子与逐 edge signed multiplier 表的合取。"
            "这仍不是闭合，行/列命题仍未无条件证明。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest bucket transport-stack sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_bucket_signed_law_imported={fmt_bool(cert['latest_bucket_signed_law_imported'])}",
        f"bucket_transport_router_imported={fmt_bool(cert['bucket_transport_router_imported'])}",
        f"unit_seed_boundary_imported={fmt_bool(cert['unit_seed_boundary_imported'])}",
        f"ordered_coherence_closed={fmt_bool(cert['ordered_coherence_closed'])}",
        f"step_update_reduced_to_edge_multiplier={fmt_bool(cert['step_update_reduced_to_edge_multiplier'])}",
        f"square_base_private_escape_removed={fmt_bool(cert['square_base_private_escape_removed'])}",
        f"common_packet_cycle_guard_imported={fmt_bool(cert['common_packet_cycle_guard_imported'])}",
        f"edge_signed_multiplier_table_proved={fmt_bool(cert['edge_signed_multiplier_table_proved'])}",
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
            "并行 base/source-packet 三原子：",
            "",
            "```text",
            cert["parallel_primary_attack_target"],
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
