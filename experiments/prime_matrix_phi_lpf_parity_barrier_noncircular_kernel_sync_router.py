#!/usr/bin/env python3
"""生成 Phi-LPF 奇偶性障碍到非循环 signed kernel 前沿的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_parity_barrier_noncircular_kernel_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-parity-barrier-noncircular-kernel-sync-router.json

输出：
  data/prime-matrix-phi-lpf-parity-barrier-noncircular-kernel-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-parity-barrier-noncircular-kernel-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-parity-barrier-noncircular-kernel-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-parity-barrier-noncircular-kernel-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ATOM_CUT = DOCS / "prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier-router.json"
SIGNED_ATOM_TRACE = DOCS / "prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-router.json"
NEW_PAYLOAD_SOURCE = DOCS / "prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-router.json"
SOURCE_LOOP_CUT = DOCS / "prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-sync-router.json"
ROW_LEVEL_FIXED_POINT = DOCS / "prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.json"
BUCKET_SIGNED_SYNC = DOCS / "prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-router.json"
TRACE_EXIT_CONVERGENCE = DOCS / "prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json"
POINTWISE_TABLE = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    ATOM_CUT,
    SIGNED_ATOM_TRACE,
    NEW_PAYLOAD_SOURCE,
    SOURCE_LOOP_CUT,
    ROW_LEVEL_FIXED_POINT,
    BUCKET_SIGNED_SYNC,
    TRACE_EXIT_CONVERGENCE,
    POINTWISE_TABLE,
    EXTERNAL_INDEX,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    FRONTIER_HONEST,
    PAPER,
]

PURE_ATOM = "PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward"
EDGE_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
SOURCE_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
FRESH_JOINT = "FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop"
NONCIRCULAR_KERNEL = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
BUCKET_SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
POINTWISE_SIGNED_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失不能视为证明。"""
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
    """列出从 atom-cut 到非循环 kernel 的同步链。"""
    return [
        {
            "from": EDGE_FIELDS,
            "to": NEW_PAYLOAD,
            "meaning": "同一 trace key 与 named return 矩阵删除匿名 signed-field 缺口；生产性出口只能是新 primitive payload/trace。",
        },
        {
            "from": NEW_PAYLOAD,
            "to": SOURCE_ENTROPY,
            "meaning": "新 payload 若不是 signed-lane 改名，必须携带 actual source-rank/no-collapse 包，第一原子为 source entropy。",
        },
        {
            "from": SOURCE_ENTROPY,
            "to": FRESH_JOINT,
            "meaning": "沿 constructor source-entropy downstream 展开会回到 joint declaration；原回环被切掉，必须提交 fresh independent joint declaration。",
        },
        {
            "from": "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands",
            "to": NONCIRCULAR_KERNEL,
            "meaning": "row-level 表沿 signed-source 展开会固定点自证；删除固定点后只剩非循环 pre-Cauchy signed emission kernel。",
        },
        {
            "from": NONCIRCULAR_KERNEL,
            "to": BUCKET_SIGNED_LAW,
            "meaning": "strict kernel 的找行/容量部分由 LPF/Phi support stripping 支付；剩余是每个 `(p,m)` bucket 的 signed coefficient law。",
        },
        {
            "from": NEW_PAYLOAD,
            "to": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
            "meaning": "source-rank 收敛支路把 trace/new-payload 出口汇入 alpha-row/source-rank 三原子。",
        },
    ]


def frontier_rows() -> list[dict[str, Any]]:
    """列出当前真正可攻的前沿对象。"""
    return [
        {
            "priority": 1,
            "frontier": BUCKET_SIGNED_LAW,
            "type": "bucket signed law",
            "requires": f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
            "why": "这是 noncircular kernel 剥掉 LPF/Phi 无符号支撑容量后剩下的最小正向 signed coefficient law。",
            "proved": False,
        },
        {
            "priority": 2,
            "frontier": NONCIRCULAR_KERNEL,
            "type": "internal signed kernel discipline",
            "requires": f"{BUCKET_SIGNED_LAW} on all support keys without downstream recovery",
            "why": "kernel 纪律仍是禁止回读 row-level 表、source-entropy payload 环或 Phi/payment 下游。",
            "proved": False,
        },
        {
            "priority": 3,
            "frontier": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
            "type": "source-rank pointwise kernel",
            "requires": "same formal-unit primitive alpha/delta kernel table",
            "why": "trace/new-payload/source-rank 线在逐 primitive alpha/delta 核表上汇合。",
            "proved": False,
        },
        {
            "priority": 4,
            "frontier": POINTWISE_SIGNED_TABLE,
            "type": "direct pointwise bypass",
            "requires": "complete signed values on fixed Phi-LPF support before pushforward",
            "why": "若直接给出逐点 signed table，就绕开 LPF 无符号奇偶障碍。",
            "proved": False,
        },
        {
            "priority": 5,
            "frontier": "PointwiseThetaPsiCOneInput",
            "type": "external prime-distribution bypass",
            "requires": "theta((kP,(k+1)P))>0 or psi(I)>PrimePowerTail(I) for every strict row",
            "why": "这是直接数素数的平方根行尺度输入。",
            "proved": False,
        },
        {
            "priority": 6,
            "frontier": f"{PDEC_SCOPE} OR {EXTERNAL_DIBFI}",
            "type": "controlled return or external dispersion",
            "requires": "same-set PDEC scope or source-keyed signed coefficient family suitable for dispersion/Kuznetsov",
            "why": "外部谱工具不能吃无符号 LPF support；必须先有 admissible signed family。",
            "proved": False,
        },
    ]


def external_rows() -> list[dict[str, Any]]:
    """列出外部最前沿输入的接口限制。"""
    return [
        {
            "input": "Guth--Maynard zero-density / short intervals",
            "source": "https://arxiv.org/abs/2405.20552",
            "supplies": "PNT in short intervals of length x^(17/30+o(1)) via zero-density estimates",
            "missing_interface": "Prime Matrix strict rows have length P near x=P^2, i.e. x^(1/2)",
            "direct_close_now": False,
        },
        {
            "input": "Le Duc Hieu short-interval APs of primes",
            "source": "https://arxiv.org/abs/2509.04883",
            "supplies": "many k-term arithmetic progressions of primes in every interval [x,x+x^theta] once theta>17/30",
            "missing_interface": "this transfers the same theta>17/30 threshold, still above the pointwise row scale x^(1/2)",
            "direct_close_now": False,
        },
        {
            "input": "Runbo Li Harman-sieve short intervals",
            "source": "https://arxiv.org/abs/2308.04458",
            "supplies": "prime existence in intervals [x-x^0.52,x] for large x",
            "missing_interface": "0.52 remains above the required 1/2 row scale",
            "direct_close_now": False,
        },
        {
            "input": "Fouvry--Kowalski--Michel--Sawin trace functions",
            "source": "https://arxiv.org/abs/2511.09459",
            "supplies": "bilinear trace-function bounds below Polya-Vinogradov under monodromy hypotheses",
            "missing_interface": "no ell-adic trace-function family has been constructed from the Prime Matrix source key",
            "direct_close_now": False,
        },
        {
            "input": "Milicevic--Qin--Wu Kloosterman bilinear forms",
            "source": "https://arxiv.org/abs/2511.07550",
            "supplies": "power-saving bilinear Kloosterman bounds modulo arbitrary q",
            "missing_interface": "no two-variable Kloosterman coefficient family is emitted by the current signed kernel",
            "direct_close_now": False,
        },
        {
            "input": "Wright trilinear Kloosterman fractions",
            "source": "https://arxiv.org/abs/2604.25177",
            "supplies": "trilinear Kloosterman-fraction estimates for unbalanced convolution shapes",
            "missing_interface": "no trilinear beta sequence or source-key convolution exists yet",
            "direct_close_now": False,
        },
        {
            "input": "Pascadi non-abelian / Type-II inputs",
            "source": "https://arxiv.org/abs/2511.08445",
            "supplies": "composite-modulus Type-II/Kloosterman technology",
            "missing_interface": "current LPF buckets are unsigned and not well-factorable signed coefficients",
            "direct_close_now": False,
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    atom = load_json(ATOM_CUT)
    trace = load_json(SIGNED_ATOM_TRACE)
    payload = load_json(NEW_PAYLOAD_SOURCE)
    loop = load_json(SOURCE_LOOP_CUT)
    fixed = load_json(ROW_LEVEL_FIXED_POINT)
    bucket = load_json(BUCKET_SIGNED_SYNC)
    trace_exit = load_json(TRACE_EXIT_CONVERGENCE)
    pointwise = load_json(POINTWISE_TABLE)

    sync_closed = all(
        [
            atom.get("atom_cut_frontier_synced") is True,
            atom.get("next_constructor_side_attack_target") == EDGE_FIELDS,
            trace.get("next_primary_attack_target") == NEW_PAYLOAD,
            payload.get("next_primary_attack_target") == SOURCE_ENTROPY,
            loop.get("next_primary_attack_target") == FRESH_JOINT,
            fixed.get("next_primary_attack_target") == NONCIRCULAR_KERNEL,
            bucket.get("next_primary_attack_target") == BUCKET_SIGNED_LAW,
            trace_exit.get("next_primary_attack_target") == ALPHA_ANCHOR,
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
        ]
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_parity_barrier_noncircular_kernel_sync_router",
        "status": "phi_lpf_parity_barrier_synced_to_noncircular_signed_kernel_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "noncircular_kernel_sync_closed": sync_closed,
        "atom_cut_imported": atom.get("atom_cut_frontier_synced") is True,
        "constructor_signed_atom_trace_synced": trace.get("next_primary_attack_target") == NEW_PAYLOAD,
        "new_payload_source_rank_synced": payload.get("next_primary_attack_target") == SOURCE_ENTROPY,
        "constructor_payload_loop_cut_synced": loop.get("next_primary_attack_target") == FRESH_JOINT,
        "row_level_fixed_point_cut_synced": fixed.get("next_primary_attack_target") == NONCIRCULAR_KERNEL,
        "noncircular_kernel_cut_to_bucket_signed_law_synced": bucket.get("next_primary_attack_target") == BUCKET_SIGNED_LAW,
        "trace_exit_source_rank_convergence_synced": trace_exit.get("next_primary_attack_target") == ALPHA_ANCHOR,
        "lpf_phi_unsigned_scope_exhausted": atom.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction") is False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "noncircular_signed_emission_kernel_proved": False,
        "phi_lpf_bucket_signed_coefficient_law_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "pointwise_theta_psi_c_one_input_proved": False,
        "external_trace_typeii_family_directly_attaches_now": False,
        "row_column_unconditional_closed": False,
        "compression_chain": compression_chain(),
        "frontier_rows": frontier_rows(),
        "external_rows": external_rows(),
        "chosen_internal_primary_attack_target": BUCKET_SIGNED_LAW,
        "chosen_kernel_discipline_target": NONCIRCULAR_KERNEL,
        "chosen_parallel_source_rank_attack_target": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        "parallel_direct_bypass": POINTWISE_SIGNED_TABLE,
        "latest_open_gate": (
            f"AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            f"({PDEC_SCOPE} OR ({BUCKET_SIGNED_LAW} AND {SIGNED_SURVIVAL} AND {ROW_MASS}) "
            f"OR ({ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}) OR {POINTWISE_SIGNED_TABLE} "
            "OR PointwiseThetaPsiCOneInput OR ExternalSourceKeyedTraceTypeIIFamily) "
            "AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger "
            "AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger "
            "AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "plain_conclusion": (
            "本步把上一轮 atom-cut 前沿继续同步到真正非循环的 signed kernel 门。"
            "constructor edge signed fields 经过 same-trace/key return、new payload、source entropy 后会进入 "
            "payload/source-entropy 回环；row-level 表沿 signed-source 展开也会回到自身。"
            "strict kernel 再剥掉 LPF/Phi 无符号找行和容量后，内部最快主攻是 "
            "PhiLPFBucketSignedCoefficientLawBeforePushforward，"
            "并同时支付 signed survival 与 row-mass/no-heavy-row。并行可审稿路线是 alpha-row/source-rank 三原子、"
            "逐点 signed table、点态 theta/psi 平方根行输入或命名 PDEC/外部 source-keyed trace/Type-II family。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines: list[str] = [
        "# Prime Matrix Phi-LPF parity barrier noncircular kernel sync 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"noncircular_kernel_sync_closed={fmt_bool(cert['noncircular_kernel_sync_closed'])}",
        f"lpf_phi_unsigned_scope_exhausted={fmt_bool(cert['lpf_phi_unsigned_scope_exhausted'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"noncircular_signed_emission_kernel_proved={fmt_bool(cert['noncircular_signed_emission_kernel_proved'])}",
        f"phi_lpf_bucket_signed_coefficient_law_proved={fmt_bool(cert['phi_lpf_bucket_signed_coefficient_law_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(cert['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"external_trace_typeii_family_directly_attaches_now={fmt_bool(cert['external_trace_typeii_family_directly_attaches_now'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压缩链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for row in cert["compression_chain"]:
        lines.append(f"| `{cell(row['from'])}` | `{cell(row['to'])}` | {cell(row['meaning'])} |")

    lines.extend(
        [
            "",
            "## 2. 当前真正前沿",
            "",
            "| priority | frontier | type | requires | proved | why |",
            "| ---: | --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["frontier_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["priority"]),
                    f"`{cell(row['frontier'])}`",
                    cell(row["type"]),
                    cell(row["requires"]),
                    f"`{fmt_bool(row['proved'])}`",
                    cell(row["why"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 外部输入边界",
            "",
            "| input | supplies | missing interface | direct close now | source |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(row["input"]),
                    cell(row["supplies"]),
                    cell(row["missing_interface"]),
                    f"`{fmt_bool(row['direct_close_now'])}`",
                    cell(row["source"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 下一手",
            "",
            "```text",
            f"chosen_internal_primary_attack_target={cert['chosen_internal_primary_attack_target']}",
            f"chosen_kernel_discipline_target={cert['chosen_kernel_discipline_target']}",
            f"chosen_parallel_source_rank_attack_target={cert['chosen_parallel_source_rank_attack_target']}",
            f"parallel_direct_bypass={cert['parallel_direct_bypass']}",
            "```",
            "",
            "最新开放口：",
            "",
            "```text",
            cert["latest_open_gate"],
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
    print(f"noncircular_kernel_sync_closed={fmt_bool(cert['noncircular_kernel_sync_closed'])}")
    print(f"chosen_internal_primary_attack_target={cert['chosen_internal_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
