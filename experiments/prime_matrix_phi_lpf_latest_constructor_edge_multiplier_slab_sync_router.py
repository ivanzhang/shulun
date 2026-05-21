#!/usr/bin/env python3
"""生成 constructor-latest edge multiplier 到 first-edge slab 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_edge_multiplier_slab_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR_TRANSPORT_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync-router.json"
)
FIRST_EDGE_SLAB_CERT = DOCS / "prime-matrix-phi-lpf-first-edge-slab-frontier-router.json"
SEMIPRIME_DIAGONAL_CERT = DOCS / "prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"

EDGE_MULTIPLIER = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
FIRST_EDGE_FIBER = "PhiLPFFirstEdgeQRoughContinuationFiberLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
NONZERO_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失文件不能视作证明。"""
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
        LATEST_CONSTRUCTOR_TRANSPORT_CERT,
        FIRST_EDGE_SLAB_CERT,
        SEMIPRIME_DIAGONAL_CERT,
        POINTWISE_FRONTIER_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sample_summary(first_edge: dict[str, Any]) -> dict[str, Any]:
    """抽取 first-edge slab 最大样本读数。"""
    samples = first_edge.get("sample_first_edge_slab_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def sync_chain() -> list[dict[str, str]]:
    """列出 constructor-latest edge multiplier 同步链。"""
    return [
        {
            "from": EDGE_MULTIPLIER,
            "to": f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
            "meaning": "逐 edge signed multiplier 表按 prefix=1 第一边和 prefix>1 内部边唯一拆分。",
        },
        {
            "from": FIRST_EDGE_FIBER,
            "to": "mass(p,q)=Phi(floor(N/(p*q)),q)",
            "meaning": "Phi-LPF 只支付第一边 q-rough continuation 的无符号 occurrence mass。",
        },
        {
            "from": FIRST_SEED,
            "to": "signed seed value / branch key / ExactUV / named return",
            "meaning": "semiprime first seed 需要推前前 signed payload，不能由 Phi fiber 反推。",
        },
        {
            "from": INTERNAL_TRANSITION,
            "to": "nonzero predecessor / signed local factor / path product compatibility",
            "meaning": "内部 prime-adjoin transition 需要非零前缀或命名回流，不能用未知终值后验除法。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 constructor-latest edge slab 判定表。"""
    latest = data["latest"]
    first_edge = data["first_edge"]
    semiprime = data["semiprime"]
    pointwise = data["pointwise"]
    return [
        row(
            "LatestConstructorTransportHardpointImported",
            latest.get("next_primary_attack_target") == EDGE_MULTIPLIER,
            False,
            "上一层 constructor transport-stack 已把最新直接 hardpoint 压到逐 edge signed multiplier 表。",
            EDGE_MULTIPLIER,
        ),
        row(
            "ConstructorSideGatesCarried",
            latest.get("parallel_constructor_side_gates") == f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
            False,
            "edge slab 只替换 edge multiplier；signed survival 与 row-mass/no-heavy-row 仍是 constructor 侧门。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "FirstEdgeSlabRouterImported",
            first_edge.get("target_input_before_router") == EDGE_MULTIPLIER
            and first_edge.get("first_edge_slab_frontier_router_closed") is True,
            True,
            "既有 first-edge slab 证书可直接作用在 constructor-latest edge multiplier 入口。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "EdgeMultiplierSplitSyncedToConstructorBasis",
            first_edge.get("edge_table_split_into_first_seed_and_internal_transition") is True,
            True,
            "constructor 最新保留基中的 edge multiplier 可替换为 first seed slab 与 internal transition 的合取。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "FirstEdgePhiFiberFormulaImported",
            first_edge.get("first_edge_phi_fiber_formula_proved") is True,
            True,
            "第一边 `(p,q)` occurrence mass 已由 Phi(floor(N/(p*q)),q) 精确支付。",
            FIRST_EDGE_FIBER,
        ),
        row(
            "PhiFiberUnsignedOnlyGuard",
            first_edge.get("first_edge_phi_fiber_formula_proved") is True,
            True,
            "Phi fiber 是支撑/容量读数，不含 signed seed、local factor、orientation、alpha/delta 或 ExactUV payload。",
            FIRST_SEED,
        ),
        row(
            "SemiprimeFirstSeedStillOpen",
            first_edge.get("semiprime_first_edge_signed_seed_table_proved") is False,
            False,
            "当前语料没有为所有 semiprime first edges 给出推前前 signed seed 表。",
            FIRST_SEED,
        ),
        row(
            "InternalTransitionStillOpen",
            first_edge.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "当前语料没有为所有 prefix>1 内部 prime-adjoin edges 给出 signed transition law。",
            INTERNAL_TRANSITION,
        ),
        row(
            "SemiprimeDiagonalDownstreamAvailable",
            semiprime.get("target_input_before_router") == FIRST_SEED,
            False,
            "first seed 下一层可拆为 diagonal common packet 与 offdiagonal seed，但这不闭合 signed 表。",
            semiprime.get("retained_basis_after_router", FIRST_SEED),
        ),
        row(
            "SourcePacketAtomsCarriedForward",
            latest.get("parallel_primary_attack_target") == f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
            False,
            "edge slab 只替换 edge multiplier；source-packet 三原子仍保留在合取基中。",
            f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        ),
        row(
            "PointwiseSignedTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed value table 仍是并行直接旁路，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 first-edge slab 拆解；未证明 first seed、internal transition、source 三原子、signed survival、row-mass 或 ExactUV。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    data = {
        "latest": load_json(LATEST_CONSTRUCTOR_TRANSPORT_CERT),
        "first_edge": load_json(FIRST_EDGE_SLAB_CERT),
        "semiprime": load_json(SEMIPRIME_DIAGONAL_CERT),
        "pointwise": load_json(POINTWISE_FRONTIER_CERT),
    }
    rows = build_rows(data)
    sample = sample_summary(data["first_edge"])
    latest_basis = (
        f"(({ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT} AND {FIRST_SEED} AND "
        f"{INTERNAL_TRANSITION} AND {ROW_MASS}) OR {POINTWISE_TABLE} OR {BRANCH_TRACE} OR "
        f"{ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {NEW_JOINT}) "
        f"AND {NONZERO_SURVIVAL} AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_edge_multiplier_slab_sync_router",
        "status": "phi_lpf_latest_constructor_edge_multiplier_synced_to_first_edge_slab_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_constructor_transport_hardpoint_imported": rows[0]["closed"],
        "constructor_side_gates_carried": rows[1]["closed"],
        "first_edge_slab_router_imported": rows[2]["closed"],
        "edge_multiplier_split_synced_to_constructor_basis": rows[3]["closed"],
        "first_edge_phi_fiber_formula_imported": rows[4]["closed"],
        "phi_fiber_unsigned_only_guard": rows[5]["closed"],
        "semiprime_first_edge_signed_seed_table_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "edge_signed_multiplier_table_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": EDGE_MULTIPLIER,
        "next_edge_attack_targets": [FIRST_SEED, INTERNAL_TRANSITION],
        "next_primary_attack_target": FIRST_SEED,
        "paired_required_attack_target": INTERNAL_TRANSITION,
        "parallel_source_packet_attack_target": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        "parallel_constructor_side_gates": f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": latest_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "imported_largest_sample": sample,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor-latest `PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward` "
            "接入既有 first-edge slab 证书。edge multiplier 表按 LPF ordered path 唯一拆成 "
            "semiprime first-edge signed seed table 与 internal prime-adjoin signed transition law。"
            "Phi fiber 公式只支付第一边 `(p,q)` 的 q-rough continuation occurrence mass，不产生 "
            "signed seed、local factor、orientation 或 ExactUV payload。constructor 侧 signed survival "
            "与 row-mass/no-heavy-row 仍保留；行/列命题仍未无条件证明。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor edge multiplier slab sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_transport_hardpoint_imported={fmt_bool(cert['latest_constructor_transport_hardpoint_imported'])}",
        f"constructor_side_gates_carried={fmt_bool(cert['constructor_side_gates_carried'])}",
        f"first_edge_slab_router_imported={fmt_bool(cert['first_edge_slab_router_imported'])}",
        f"edge_multiplier_split_synced_to_constructor_basis={fmt_bool(cert['edge_multiplier_split_synced_to_constructor_basis'])}",
        f"first_edge_phi_fiber_formula_imported={fmt_bool(cert['first_edge_phi_fiber_formula_imported'])}",
        f"phi_fiber_unsigned_only_guard={fmt_bool(cert['phi_fiber_unsigned_only_guard'])}",
        f"semiprime_first_edge_signed_seed_table_proved={fmt_bool(cert['semiprime_first_edge_signed_seed_table_proved'])}",
        f"internal_prime_adjoin_signed_transition_law_proved={fmt_bool(cert['internal_prime_adjoin_signed_transition_law_proved'])}",
        f"nonzero_signed_row_survival_proved={fmt_bool(cert['nonzero_signed_row_survival_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(cert['same_formal_unit_row_mass_normalization_proved'])}",
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
    sample = cert.get("imported_largest_sample", {})
    if sample:
        lines.extend(
            [
                "",
                "## 3. 导入样本读数",
                "",
                "| N | support | first occ | internal occ | first types | max depth | Phi fiber ok |",
                "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
                (
                    f"| {sample['N']} | {sample['support_keys']} | {sample['first_edge_occurrences']} | "
                    f"{sample['internal_edge_occurrences']} | {sample['distinct_first_edge_types']} | "
                    f"{sample['max_factor_depth']} | `{fmt_bool(sample['first_edge_phi_fiber_formula_holds'])}` |"
                ),
            ]
        )
    lines.extend(
        [
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "下一 edge 侧主攻：",
            "",
            "```text",
            "\n".join(cert["next_edge_attack_targets"]),
            "```",
            "",
            "并行 source-packet 三原子：",
            "",
            "```text",
            cert["parallel_source_packet_attack_target"],
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
            "## 5. 依赖哈希",
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
