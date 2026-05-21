#!/usr/bin/env python3
"""生成 latest constructor semiprime seed diagonal 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_semiprime_seed_diagonal_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync-router.json"
)
OLD_CONSTRUCTOR_SEMIPRIME_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-router.json"
)
SEMIPRIME_DIAGONAL_CERT = DOCS / "prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json"
SOURCE_PACKET_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"

FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
DIAGONAL_SEED = "PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward"
OFFDIAG_SEED = "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward"
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
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能被当成已证明。"""
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
        OLD_CONSTRUCTOR_SEMIPRIME_CERT,
        SEMIPRIME_DIAGONAL_CERT,
        SOURCE_PACKET_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def source_atoms() -> str:
    """给出 diagonal common packet 已携带的 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    return (
        f"(({source_atoms()} AND {OFFDIAG_SEED} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) "
        f"OR {POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} "
        f"OR {PDEC_SCOPE} OR {TERMINAL_WFD} OR {NEW_JOINT}) AND {SIGNED_SURVIVAL} "
        f"AND {SOURCE_EXACTUV} AND {COMPLETE_KEY} AND {FIXED_KEY} AND {HARMONIC} "
        f"AND {SKELETON} AND {RATE} AND {DSTRUCTURE}"
    )


def sync_chain() -> list[dict[str, str]]:
    """列出本层重挂接链条。"""
    return [
        {
            "from": FIRST_SEED,
            "to": f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
            "meaning": "LPF first-edge seed 按 p=q 与 p<q 唯一分解。",
        },
        {
            "from": DIAGONAL_SEED,
            "to": source_atoms(),
            "meaning": "diagonal square-base 不能保留私有 signed 出口，只能回到 common source-packet 三原子。",
        },
        {
            "from": FIRST_SEED,
            "to": f"{OFFDIAG_SEED} AND {source_atoms()}",
            "meaning": "在最新 rebase 基中，FIRST_SEED 的新增 signed 缺口收窄为 offdiagonal seed。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    old_constructor: dict[str, Any],
    semiprime: dict[str, Any],
    source_packet: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 semiprime diagonal rebase 判定表。"""
    latest_first_seed_active = (
        latest.get("next_primary_attack_target") == FIRST_SEED
        and latest.get("edge_multiplier_slab_rebased") is True
    )
    old_constructor_reusable = (
        old_constructor.get("target_input_before_router") == FIRST_SEED
        and old_constructor.get("latest_basis_replaces_first_seed_with_offdiag_seed") is True
        and old_constructor.get("next_primary_attack_target") == OFFDIAG_SEED
    )
    semiprime_router_imported = (
        semiprime.get("target_input_before_router") == FIRST_SEED
        and semiprime.get("semiprime_seed_diagonal_frontier_router_closed") is True
    )
    diagonal_private_removed = (
        semiprime.get("diagonal_square_base_private_signed_escape_removed") is True
        and old_constructor.get("diagonal_private_escape_removed") is True
    )
    source_cycle_guard = (
        source_packet.get("common_packet_self_proof_blocked") is True
        or source_packet.get("common_packet_self_proof_rejected_after_lpf") is True
    )
    rebase_closed = (
        latest_first_seed_active
        and old_constructor_reusable
        and semiprime_router_imported
        and diagonal_private_removed
        and source_cycle_guard
    )
    return [
        row(
            "LatestRebasedFirstSeedImported",
            latest_first_seed_active,
            False,
            "上一层 rebase 已把最新 constructor edge 路线压到 semiprime first-edge signed seed。",
            FIRST_SEED,
        ),
        row(
            "ExistingConstructorSemiprimeDiagonalReusable",
            old_constructor_reusable,
            False,
            "旧 constructor semiprime diagonal 同步证书的目标输入相同，可以在新 rebase 前沿复用。",
            f"{OFFDIAG_SEED} AND {source_atoms()}",
        ),
        row(
            "SemiprimeDiagonalRouterImported",
            semiprime_router_imported,
            True,
            "semiprime seed diagonal 证书给出 p=q 与 p<q 的无重叠拆分。",
            f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
        ),
        row(
            "DiagonalPrivateEscapeRemoved",
            diagonal_private_removed,
            True,
            "diagonal square-base lane 不生成独立 signed seed；它回到 common packet。",
            source_atoms(),
        ),
        row(
            "CommonPacketCycleGuardCarriedForward",
            source_cycle_guard,
            True,
            "common packet 自证环已被切断，不能用 diagonal lane 自证 source atoms。",
            source_atoms(),
        ),
        row(
            "SemiprimeSeedDiagonalRebased",
            rebase_closed,
            False,
            "最新 FIRST_SEED 入口已同步为 offdiagonal seed 与 source 三原子。",
            f"{OFFDIAG_SEED} AND {source_atoms()}",
        ),
        row(
            "OffDiagonalSeedCurrentCorpusProved",
            False,
            False,
            "当前材料没有为 p<q ordered semiprime first edges 给出 signed seed table。",
            OFFDIAG_SEED,
        ),
        row(
            "InternalPrimeAdjoinTransitionStillPaired",
            latest.get("paired_required_attack_target") == INTERNAL_TRANSITION,
            False,
            "first seed 收窄后，prefix>1 internal prime-adjoin transition 仍是同一 LPF 递推的配套硬点。",
            INTERNAL_TRANSITION,
        ),
        row(
            "SourceAndSideGatesStillParallel",
            True,
            False,
            "source 三原子、signed survival 与 row-mass/no-heavy-row 仍随 constructor 前沿保留。",
            f"{source_atoms()} AND {SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 rebase 同步；未证明 offdiagonal seed、internal transition、source 三原子、signed survival、row-mass 或 ExactUV。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json(LATEST_REBASE_CERT)
    old_constructor = load_json(OLD_CONSTRUCTOR_SEMIPRIME_CERT)
    semiprime = load_json(SEMIPRIME_DIAGONAL_CERT)
    source_packet = load_json(SOURCE_PACKET_CERT)
    rows = build_rows(latest, old_constructor, semiprime, source_packet)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_semiprime_seed_diagonal_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_semiprime_seed_diagonal_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_rebased_first_seed_imported": rows[0]["closed"],
        "existing_constructor_semiprime_diagonal_reusable": rows[1]["closed"],
        "semiprime_diagonal_router_imported": rows[2]["closed"],
        "diagonal_private_escape_removed": rows[3]["closed"],
        "common_packet_cycle_guard_carried_forward": rows[4]["closed"],
        "semiprime_seed_diagonal_rebased": rows[5]["closed"],
        "offdiagonal_ordered_semiprime_signed_seed_table_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": FIRST_SEED,
        "next_primary_attack_target": OFFDIAG_SEED,
        "paired_required_attack_target": INTERNAL_TRANSITION,
        "carried_source_packet_attack_target": source_atoms(),
        "parallel_constructor_side_gates": f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": retained_basis(),
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 rebase 后的 constructor `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` "
            "重新接入既有 semiprime diagonal/offdiagonal 拆分。diagonal `(p,p)` 的私有 signed 出口已被移除，"
            "只能由 source-packet 三原子承接；因此最新 seed-side 主攻收窄为 "
            "`PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`。internal transition、"
            "signed survival 与 row-mass/no-heavy-row 仍保留；行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor semiprime seed diagonal rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_rebased_first_seed_imported={fmt_bool(result['latest_rebased_first_seed_imported'])}",
        f"existing_constructor_semiprime_diagonal_reusable={fmt_bool(result['existing_constructor_semiprime_diagonal_reusable'])}",
        f"semiprime_diagonal_router_imported={fmt_bool(result['semiprime_diagonal_router_imported'])}",
        f"diagonal_private_escape_removed={fmt_bool(result['diagonal_private_escape_removed'])}",
        f"common_packet_cycle_guard_carried_forward={fmt_bool(result['common_packet_cycle_guard_carried_forward'])}",
        f"semiprime_seed_diagonal_rebased={fmt_bool(result['semiprime_seed_diagonal_rebased'])}",
        f"offdiagonal_ordered_semiprime_signed_seed_table_proved={fmt_bool(result['offdiagonal_ordered_semiprime_signed_seed_table_proved'])}",
        f"internal_prime_adjoin_signed_transition_law_proved={fmt_bool(result['internal_prime_adjoin_signed_transition_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_chain"]:
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
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
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
            "已携带 source-packet 三原子：",
            "",
            "```text",
            result["carried_source_packet_attack_target"],
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
