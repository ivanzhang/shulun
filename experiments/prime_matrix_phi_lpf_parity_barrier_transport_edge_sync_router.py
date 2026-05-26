#!/usr/bin/env python3
"""生成 Phi-LPF 奇偶性障碍到 transport/first-edge 前沿的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_parity_barrier_transport_edge_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.json

输出：
  data/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-parity-barrier-transport-edge-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

NONCIRCULAR_SYNC = DOCS / "prime-matrix-phi-lpf-parity-barrier-noncircular-kernel-sync-router.json"
BUCKET_STACK = DOCS / "prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-router.json"
FIRST_EDGE = DOCS / "prime-matrix-phi-lpf-first-edge-slab-frontier-router.json"
SEMIPRIME_DIAGONAL = DOCS / "prime-matrix-phi-lpf-latest-semiprime-seed-diagonal-sync-router.json"
OFFDIAG_TUPLE = DOCS / "prime-matrix-phi-lpf-latest-offdiagonal-seed-tuple-sync-router.json"
PURE_PAIR = DOCS / "prime-matrix-phi-lpf-latest-offdiagonal-pure-pair-atom-sync-router.json"
POINTWISE_TABLE_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
PRIME_DISTRIBUTION = DOCS / "prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json"
LPF_BUCKET_COUNT = DOCS / "prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    NONCIRCULAR_SYNC,
    BUCKET_STACK,
    FIRST_EDGE,
    SEMIPRIME_DIAGONAL,
    OFFDIAG_TUPLE,
    PURE_PAIR,
    POINTWISE_TABLE_CERT,
    PRIME_DISTRIBUTION,
    LPF_BUCKET_COUNT,
    EXTERNAL_INDEX,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    FRONTIER_HONEST,
    PAPER,
]

BUCKET_SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
ROUGH_TRANSPORT = "PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward"
EDGE_TABLE = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
OFFDIAG_FIRST_SEED = "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward"
OFFDIAG_TUPLE_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
PURE_PAIR_ATOM = "PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward"
ORIENTATION_PARITY = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
EXACTUV_RETURN = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
FIRST_EDGE_FIBER = "PhiLPFFirstEdgeQRoughContinuationFiberLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格转义。"""
    return str(value).replace("|", r"\|")


def compression_chain() -> list[dict[str, str]]:
    """列出从 bucket signed law 到 first-edge 子表的非循环压缩链。"""
    return [
        {
            "from": BUCKET_SIGNED_LAW,
            "to": f"{ROUGH_TRANSPORT} OR {POINTWISE_TABLE}",
            "meaning": "bucket signed law 若不直接提交逐点 signed 表，就必须给 rough cofactor signed transport。",
        },
        {
            "from": ROUGH_TRANSPORT,
            "to": f"{EDGE_TABLE} AND {ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
            "meaning": "ordered factorization 与 square-base 私有出口已剥离；递推支路剩 edge multiplier 表和 source-rank 三原子。",
        },
        {
            "from": EDGE_TABLE,
            "to": f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
            "meaning": "每条 LPF ordered path 唯一拆成第一边 semiprime seed slab 与 prefix>1 的 internal prime-adjoin transitions。",
        },
        {
            "from": FIRST_SEED,
            "to": f"{OFFDIAG_FIRST_SEED} plus carried source atoms",
            "meaning": "diagonal p=q 已回到 square-base/common source packet；新增 first-seed 缺口只剩 p<q offdiagonal 表。",
        },
        {
            "from": OFFDIAG_FIRST_SEED,
            "to": f"{OFFDIAG_TUPLE_FORMULA} AND {ORIENTATION_PARITY} AND {EXACTUV_RETURN}",
            "meaning": "LPF/Phi 已关闭 owner、first q、q-rough tail 与 Phi mass；剩余是 signed seed、orientation 与 ExactUV 字段。",
        },
        {
            "from": OFFDIAG_TUPLE_FORMULA,
            "to": f"{PURE_PAIR_ATOM} AND tail-lift/internal-transition compatibility",
            "meaning": "每个 p<q ordered type 的 first seed 原子唯一是 tail=1 pure pair p*q；tail>1 只能交给 internal transition lift。",
        },
        {
            "from": FIRST_EDGE_FIBER,
            "to": "support and occurrence mass only",
            "meaning": "Phi(floor(N/(p*q)),q) 只给 q-rough continuation 纤维大小，不给 signed seed value。",
        },
        {
            "from": POINTWISE_TABLE,
            "to": "new prepushforward signed artifact or controlled return",
            "meaning": "逐点 signed 表仍是旁路，但不能由 LPF support/count 反推，必须正向提交或命名回流。",
        },
    ]


def frontier_rows() -> list[dict[str, Any]]:
    """列出下一层可审稿硬点。"""
    return [
        {
            "priority": 1,
            "frontier": PURE_PAIR_ATOM,
            "requires": "tail=1 pure pair signed seed value, branch key, source trace or return tag",
            "proved": False,
            "why": "offdiagonal first seed 的无符号 tuple 与 tail 拆分已闭合；真正新增 signed 原子是 p*q pure pair。",
        },
        {
            "priority": 2,
            "frontier": f"{ORIENTATION_PARITY} AND {EXACTUV_RETURN}",
            "requires": "orientation parity, branch side, fixed-pair ExactUV, return tag",
            "proved": False,
            "why": "pure atom 即使定位，还必须有方向、branch side 与 ExactUV/return 字段。",
        },
        {
            "priority": 3,
            "frontier": INTERNAL_TRANSITION,
            "requires": "signed_adjoin_multiplier, nonzero_predecessor_or_return, path_product_compatibility",
            "proved": False,
            "why": "tail>1 continuation 不是新 first seed，只能由 internal prime-adjoin transition lift 支付。",
        },
        {
            "priority": 4,
            "frontier": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
            "requires": "same formal-unit primitive alpha/delta kernel table",
            "proved": False,
            "why": "source-rank 三原子是 transport 支路的并行 source packet 负载。",
        },
        {
            "priority": 5,
            "frontier": POINTWISE_TABLE,
            "requires": "complete signed value table on every Phi-LPF support key before pushforward",
            "proved": False,
            "why": "这是绕过 rough transport 的直接 signed artifact 路线。",
        },
        {
            "priority": 6,
            "frontier": f"{BRANCH_TRACE} OR {ATOMIC_TRACE} OR {PDEC_SCOPE}",
            "requires": "branch/atomic trace signed coefficient formula or controlled return",
            "proved": False,
            "why": "完整 trace 可同时供给 first seed、internal transition、return tag 与 ExactUV 字段。",
        },
        {
            "priority": 7,
            "frontier": "PointwiseThetaPsiCOneInput OR ExternalSourceKeyedTraceTypeIIFamily",
            "requires": "theta/psi at x^(1/2) row scale or admissible signed trace/Type-II family",
            "proved": False,
            "why": "这是外部或直接素数分布旁路，但当前仍缺点态行尺度或 source-keyed 系数族。",
        },
    ]


def external_rows() -> list[dict[str, Any]]:
    """列出外部输入在当前 first-edge 前沿上的接口限制。"""
    return [
        {
            "input": "Guth--Maynard / Hieu short-interval technology",
            "source": "https://arxiv.org/abs/2405.20552 and https://arxiv.org/abs/2509.04883",
            "blocker": "theta>17/30 still exceeds the strict-row scale x^(1/2)",
            "usable_after": "a pointwise row-scale theta/psi theorem or a theorem exploiting Prime Matrix source keys",
        },
        {
            "input": "Runbo Li short intervals",
            "source": "https://arxiv.org/abs/2308.04458",
            "blocker": "x^0.52 is still longer than rows of length P at x=P^2",
            "usable_after": "a zero-exception refinement to exponent 1/2 in the same row convention",
        },
        {
            "input": "FKMS / MQW / Wright / Pascadi trace, Kloosterman, Type-II inputs",
            "source": "arXiv:2511.09459, arXiv:2511.07550, arXiv:2604.25177, arXiv:2505.00653",
            "blocker": "current pure-pair data are support/tuple/fiber ledgers, not source-keyed signed coefficient families",
            "usable_after": "pure-pair seed, orientation, ExactUV return, and internal transition emit admissible signed coefficients with conductor control",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装 transport-edge 同步证书。"""
    noncircular = load_json(NONCIRCULAR_SYNC)
    bucket_stack = load_json(BUCKET_STACK)
    first_edge = load_json(FIRST_EDGE)
    semiprime_diagonal = load_json(SEMIPRIME_DIAGONAL)
    offdiag_tuple = load_json(OFFDIAG_TUPLE)
    pure_pair = load_json(PURE_PAIR)
    pointwise = load_json(POINTWISE_TABLE_CERT)
    prime_distribution = load_json(PRIME_DISTRIBUTION)

    sync_closed = all(
        [
            noncircular.get("noncircular_kernel_sync_closed") is True,
            noncircular.get("chosen_internal_primary_attack_target") == BUCKET_SIGNED_LAW,
            bucket_stack.get("latest_bucket_signed_law_imported") is True,
            bucket_stack.get("next_primary_attack_target") == EDGE_TABLE,
            first_edge.get("edge_table_split_into_first_seed_and_internal_transition") is True,
            first_edge.get("first_edge_phi_fiber_formula_proved") is True,
            first_edge.get("next_primary_attack_target") == FIRST_SEED,
            first_edge.get("paired_required_attack_target") == INTERNAL_TRANSITION,
            semiprime_diagonal.get("next_primary_attack_target") == OFFDIAG_FIRST_SEED,
            semiprime_diagonal.get("diagonal_offdiagonal_support_split_closed") is True,
            semiprime_diagonal.get("diagonal_private_escape_removed") is True,
            offdiag_tuple.get("next_primary_attack_target") == OFFDIAG_TUPLE_FORMULA,
            offdiag_tuple.get("offdiagonal_source_tuple_bijection_synced") is True,
            offdiag_tuple.get("offdiagonal_phi_tail_fiber_mass_synced") is True,
            pure_pair.get("next_primary_attack_target") == PURE_PAIR_ATOM,
            pure_pair.get("pure_pair_atom_bijection_synced") is True,
            pure_pair.get("tail_lift_no_new_first_seed_closed") is True,
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            prime_distribution.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction") is False,
        ]
    )

    retained_basis = (
        f"(({PURE_PAIR_ATOM} AND {ORIENTATION_PARITY} AND {EXACTUV_RETURN} "
        f"AND {INTERNAL_TRANSITION} AND {ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}) "
        f"OR {POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} "
        f"OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA} OR PointwiseThetaPsiCOneInput "
        f"OR ExternalSourceKeyedTraceTypeIIFamily) AND {EXACTUV_PAIR} AND {MODEL_LEDGER} "
        f"AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_parity_barrier_transport_edge_sync_router",
        "status": "phi_lpf_parity_barrier_synced_through_transport_to_first_edge_slabs_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "transport_edge_sync_closed": sync_closed,
        "noncircular_kernel_sync_imported": noncircular.get("noncircular_kernel_sync_closed") is True,
        "bucket_signed_law_imported": bucket_stack.get("latest_bucket_signed_law_imported") is True,
        "bucket_transport_stack_imported": bucket_stack.get("bucket_transport_router_imported") is True,
        "ordered_coherence_closed": bucket_stack.get("ordered_coherence_closed") is True,
        "square_base_private_escape_removed": bucket_stack.get("square_base_private_escape_removed") is True,
        "edge_multiplier_table_reached": bucket_stack.get("next_primary_attack_target") == EDGE_TABLE,
        "edge_table_split_into_first_seed_and_internal_transition": first_edge.get("edge_table_split_into_first_seed_and_internal_transition") is True,
        "first_edge_phi_fiber_formula_proved": first_edge.get("first_edge_phi_fiber_formula_proved") is True,
        "first_edge_phi_fiber_supplies_signed_seed": False,
        "diagonal_offdiagonal_support_split_closed": semiprime_diagonal.get("diagonal_offdiagonal_support_split_closed") is True,
        "diagonal_private_escape_removed": semiprime_diagonal.get("diagonal_private_escape_removed") is True,
        "offdiagonal_source_tuple_bijection_synced": offdiag_tuple.get("offdiagonal_source_tuple_bijection_synced") is True,
        "offdiagonal_phi_tail_fiber_mass_synced": offdiag_tuple.get("offdiagonal_phi_tail_fiber_mass_synced") is True,
        "pure_pair_atom_bijection_synced": pure_pair.get("pure_pair_atom_bijection_synced") is True,
        "tail_lift_no_new_first_seed_closed": pure_pair.get("tail_lift_no_new_first_seed_closed") is True,
        "pure_semiprime_pair_signed_seed_atom_proved": False,
        "offdiagonal_orientation_parity_law_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction": False,
        "external_trace_typeii_family_directly_attaches_now": False,
        "row_column_unconditional_closed": False,
        "compression_chain": compression_chain(),
        "frontier_rows": frontier_rows(),
        "external_rows": external_rows(),
        "chosen_primary_attack_target": PURE_PAIR_ATOM,
        "paired_required_attack_target": INTERNAL_TRANSITION,
        "paired_orientation_attack_target": ORIENTATION_PARITY,
        "paired_exactuv_attack_target": EXACTUV_RETURN,
        "chosen_parallel_source_rank_attack_target": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": retained_basis,
        "plain_conclusion": (
            "本步把上一轮 parity-barrier noncircular kernel 同步继续接入既有 bucket transport stack。"
            "bucket signed law 不应停留为抽象缺口；若不直接提交逐点 signed value table，"
            "它必须给 rough-cofactor signed transport。该 transport 的 ordered coherence、"
            "unit/square-base 私有出口和 common packet 回环已经被剥离，剩余 edge multiplier 表；"
            "first-edge slab 证书再把 edge multiplier 表拆成 semiprime first-edge signed seed table "
            "与 internal prime-adjoin signed transition law；diagonal 再并回 source packet，offdiagonal tuple "
            "字段与 tail lift 继续剥离后，最新直接硬点是 pure semiprime pair signed seed atom。"
            "Phi 纤维公式只支付支撑和 occurrence mass，不产生 signed seed、orientation、ExactUV "
            "或 transition local factor。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines: list[str] = [
        "# Prime Matrix Phi-LPF parity barrier transport-edge sync 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"transport_edge_sync_closed={fmt_bool(cert['transport_edge_sync_closed'])}",
        f"bucket_signed_law_imported={fmt_bool(cert['bucket_signed_law_imported'])}",
        f"edge_multiplier_table_reached={fmt_bool(cert['edge_multiplier_table_reached'])}",
        f"edge_table_split_into_first_seed_and_internal_transition={fmt_bool(cert['edge_table_split_into_first_seed_and_internal_transition'])}",
        f"first_edge_phi_fiber_formula_proved={fmt_bool(cert['first_edge_phi_fiber_formula_proved'])}",
        f"first_edge_phi_fiber_supplies_signed_seed={fmt_bool(cert['first_edge_phi_fiber_supplies_signed_seed'])}",
        f"diagonal_offdiagonal_support_split_closed={fmt_bool(cert['diagonal_offdiagonal_support_split_closed'])}",
        f"offdiagonal_source_tuple_bijection_synced={fmt_bool(cert['offdiagonal_source_tuple_bijection_synced'])}",
        f"pure_pair_atom_bijection_synced={fmt_bool(cert['pure_pair_atom_bijection_synced'])}",
        f"tail_lift_no_new_first_seed_closed={fmt_bool(cert['tail_lift_no_new_first_seed_closed'])}",
        f"pure_semiprime_pair_signed_seed_atom_proved={fmt_bool(cert['pure_semiprime_pair_signed_seed_atom_proved'])}",
        f"offdiagonal_orientation_parity_law_proved={fmt_bool(cert['offdiagonal_orientation_parity_law_proved'])}",
        f"offdiagonal_exactuv_fixed_pair_return_ledger_proved={fmt_bool(cert['offdiagonal_exactuv_fixed_pair_return_ledger_proved'])}",
        f"internal_prime_adjoin_signed_transition_law_proved={fmt_bool(cert['internal_prime_adjoin_signed_transition_law_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 非循环压缩链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for row in cert["compression_chain"]:
        lines.append(f"| `{cell(row['from'])}` | `{cell(row['to'])}` | {cell(row['meaning'])} |")

    lines.extend(
        [
            "",
            "## 2. 当前可审稿前沿",
            "",
            "| priority | frontier | requires | proved | why |",
            "| ---: | --- | --- | --- | --- |",
        ]
    )
    for row in cert["frontier_rows"]:
        lines.append(
            f"| {row['priority']} | `{cell(row['frontier'])}` | {cell(row['requires'])} | "
            f"`{fmt_bool(row['proved'])}` | {cell(row['why'])} |"
        )

    lines.extend(
        [
            "",
            "## 3. 外部输入接口",
            "",
            "| input | blocker | usable after | source |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_rows"]:
        lines.append(
            f"| {cell(row['input'])} | {cell(row['blocker'])} | "
            f"{cell(row['usable_after'])} | {cell(row['source'])} |"
        )

    lines.extend(
        [
            "",
            "## 4. 下一手",
            "",
            "```text",
            f"chosen_primary_attack_target={cert['chosen_primary_attack_target']}",
            f"paired_required_attack_target={cert['paired_required_attack_target']}",
            f"paired_orientation_attack_target={cert['paired_orientation_attack_target']}",
            f"paired_exactuv_attack_target={cert['paired_exactuv_attack_target']}",
            f"chosen_parallel_source_rank_attack_target={cert['chosen_parallel_source_rank_attack_target']}",
            f"parallel_direct_bypass={cert['parallel_direct_bypass']}",
            "```",
            "",
            "最新保留基：",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"transport_edge_sync_closed={fmt_bool(cert['transport_edge_sync_closed'])}")
    print(f"chosen_primary_attack_target={cert['chosen_primary_attack_target']}")
    print(f"paired_required_attack_target={cert['paired_required_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
