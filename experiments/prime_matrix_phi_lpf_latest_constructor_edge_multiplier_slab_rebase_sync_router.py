#!/usr/bin/env python3
"""生成 latest constructor edge multiplier slab 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_edge_multiplier_slab_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-router.json"
)
OLD_EDGE_SLAB_CERT = DOCS / "prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-router.json"
FIRST_EDGE_SLAB_CERT = DOCS / "prime-matrix-phi-lpf-first-edge-slab-frontier-router.json"
SEMIPRIME_DIAGONAL_CERT = DOCS / "prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json"

EDGE_MULTIPLIER = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
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
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"


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
        LATEST_REBASE_CERT,
        OLD_EDGE_SLAB_CERT,
        FIRST_EDGE_SLAB_CERT,
        SEMIPRIME_DIAGONAL_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    return (
        f"(({ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT} AND {FIRST_SEED} AND "
        f"{INTERNAL_TRANSITION} AND {ROW_MASS}) OR {POINTWISE_TABLE} OR {BRANCH_TRACE} "
        f"OR {ATOMIC_TRACE} OR {PDEC_SCOPE} OR {TERMINAL_WFD}) AND {SIGNED_SURVIVAL} "
        f"AND {SOURCE_EXACTUV} AND {COMPLETE_KEY} AND {FIXED_KEY} AND {HARMONIC} "
        f"AND {SKELETON} AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(
    latest: dict[str, Any],
    old_edge: dict[str, Any],
    first_edge: dict[str, Any],
    semiprime: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 edge slab rebase 判定表。"""
    latest_edge_active = (
        latest.get("next_primary_attack_target") == EDGE_MULTIPLIER
        and latest.get("bucket_transport_stack_rebased") is True
    )
    old_edge_available = (
        old_edge.get("target_input_before_router") == EDGE_MULTIPLIER
        and old_edge.get("edge_multiplier_split_synced_to_constructor_basis") is True
    )
    first_edge_imported = (
        first_edge.get("target_input_before_router") == EDGE_MULTIPLIER
        and first_edge.get("first_edge_slab_frontier_router_closed") is True
    )
    semiprime_downstream = semiprime.get("target_input_before_router") == FIRST_SEED
    rebase_closed = latest_edge_active and old_edge_available and first_edge_imported
    return [
        row(
            "LatestRebasedEdgeMultiplierImported",
            latest_edge_active,
            False,
            "上一层 rebase 已把最新 constructor 递推窄口压到逐 edge signed multiplier 表。",
            EDGE_MULTIPLIER,
        ),
        row(
            "ExistingConstructorEdgeSlabReusable",
            old_edge_available,
            False,
            "旧 constructor edge slab 同步证书的目标输入相同，可以在新 rebase 前沿复用。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "FirstEdgeSlabRouterImported",
            first_edge_imported,
            True,
            "first-edge slab 证书把 edge multiplier 唯一拆成 prefix=1 first seed 与 prefix>1 internal transition。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "PhiFiberUnsignedOnlyGuardImported",
            first_edge.get("first_edge_phi_fiber_formula_proved") is True,
            True,
            "第一边 q-rough continuation fiber 只支付 occurrence mass，不生成 signed seed 或 local factor。",
            FIRST_SEED,
        ),
        row(
            "SemiprimeDiagonalDownstreamAvailable",
            semiprime_downstream,
            False,
            "first seed 可继续拆到 diagonal common packet 与 offdiagonal seed，但这仍不是 signed 表证明。",
            semiprime.get("retained_basis_after_router", FIRST_SEED),
        ),
        row(
            "EdgeMultiplierSlabRebased",
            rebase_closed,
            False,
            "最新 constructor edge multiplier 入口已同步为 first seed 与 internal transition 的合取。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "SemiprimeFirstSeedCurrentCorpusProved",
            False,
            False,
            "当前材料没有为 semiprime first edges 给出推前前 signed seed table。",
            FIRST_SEED,
        ),
        row(
            "InternalPrimeAdjoinTransitionCurrentCorpusProved",
            False,
            False,
            "当前材料没有为 prefix>1 内部 prime-adjoin edges 给出 signed transition law。",
            INTERNAL_TRANSITION,
        ),
        row(
            "SourceAndSideGatesStillParallel",
            True,
            False,
            "source 三原子、signed survival 与 row-mass/no-heavy-row 仍保留。",
            f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT} AND {SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 rebase 同步；未证明 first seed、internal transition、source 三原子、signed survival、row-mass 或 ExactUV。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json(LATEST_REBASE_CERT)
    old_edge = load_json(OLD_EDGE_SLAB_CERT)
    first_edge = load_json(FIRST_EDGE_SLAB_CERT)
    semiprime = load_json(SEMIPRIME_DIAGONAL_CERT)
    rows = build_rows(latest, old_edge, first_edge, semiprime)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_edge_multiplier_slab_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_edge_multiplier_slab_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_rebased_edge_multiplier_imported": rows[0]["closed"],
        "existing_constructor_edge_slab_reusable": rows[1]["closed"],
        "first_edge_slab_router_imported": rows[2]["closed"],
        "phi_fiber_unsigned_only_guard_imported": rows[3]["closed"],
        "semiprime_diagonal_downstream_available": rows[4]["closed"],
        "edge_multiplier_slab_rebased": rows[5]["closed"],
        "semiprime_first_edge_signed_seed_table_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": EDGE_MULTIPLIER,
        "next_primary_attack_target": FIRST_SEED,
        "paired_required_attack_target": INTERNAL_TRANSITION,
        "parallel_source_packet_attack_target": f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": retained_basis(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 rebase 后的 constructor `PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward` "
            "接入既有 first-edge slab 证书。edge multiplier 表按 LPF ordered path 唯一拆成 "
            "`PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` 与 "
            "`PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward`。Phi fiber 只支付第一边无符号 occurrence mass，"
            "不能产生 signed seed、local factor 或 ExactUV payload。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor edge multiplier slab rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_rebased_edge_multiplier_imported={fmt_bool(result['latest_rebased_edge_multiplier_imported'])}",
        f"existing_constructor_edge_slab_reusable={fmt_bool(result['existing_constructor_edge_slab_reusable'])}",
        f"first_edge_slab_router_imported={fmt_bool(result['first_edge_slab_router_imported'])}",
        f"phi_fiber_unsigned_only_guard_imported={fmt_bool(result['phi_fiber_unsigned_only_guard_imported'])}",
        f"semiprime_diagonal_downstream_available={fmt_bool(result['semiprime_diagonal_downstream_available'])}",
        f"edge_multiplier_slab_rebased={fmt_bool(result['edge_multiplier_slab_rebased'])}",
        f"semiprime_first_edge_signed_seed_table_proved={fmt_bool(result['semiprime_first_edge_signed_seed_table_proved'])}",
        f"internal_prime_adjoin_signed_transition_law_proved={fmt_bool(result['internal_prime_adjoin_signed_transition_law_proved'])}",
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
            "配套必需：",
            "",
            "```text",
            result["paired_required_attack_target"],
            "```",
            "",
            "并行 source 三原子：",
            "",
            "```text",
            result["parallel_source_packet_attack_target"],
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
