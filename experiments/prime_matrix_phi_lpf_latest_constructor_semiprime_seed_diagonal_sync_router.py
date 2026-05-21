#!/usr/bin/env python3
"""生成 constructor-latest semiprime seed 到 diagonal/offdiagonal 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_semiprime_seed_diagonal_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR_EDGE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-router.json"
)
SEMIPRIME_DIAGONAL_CERT = DOCS / "prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json"
SOURCE_PACKET_CYCLE_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"

FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
DIAGONAL_SEED = "PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward"
OFFDIAG_SEED = "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
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
    """读取 JSON 证书；缺失不能当作已证明。"""
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
        LATEST_CONSTRUCTOR_EDGE_CERT,
        SEMIPRIME_DIAGONAL_CERT,
        SOURCE_PACKET_CYCLE_CERT,
        POINTWISE_FRONTIER_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def largest_sample(semiprime: dict[str, Any]) -> dict[str, Any]:
    """抽取 semiprime diagonal/offdiagonal 证书的最大样本。"""
    samples = semiprime.get("sample_semiprime_seed_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def sync_chain() -> list[dict[str, str]]:
    """列出本层同步链。"""
    source_atoms = f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"
    return [
        {
            "from": FIRST_SEED,
            "to": f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
            "meaning": "semiprime first-edge seed 类型按 p=q 与 p<q 唯一拆分。",
        },
        {
            "from": DIAGONAL_SEED,
            "to": COMMON_PACKET,
            "meaning": "diagonal `(p,p)` 是 square-base root；私有 signed 出口已移除，只能回到 common packet。",
        },
        {
            "from": COMMON_PACKET,
            "to": source_atoms,
            "meaning": "common packet 的自证环已被切断；constructor 最新前沿把其非循环需求携带为 source 三原子。",
        },
        {
            "from": FIRST_SEED,
            "to": f"{OFFDIAG_SEED} plus carried source atoms",
            "meaning": "FIRST_SEED 的 diagonal 义务由 source 三原子承接后，新增 seed 窄口是 offdiagonal 表。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 constructor-latest semiprime seed 同步判定表。"""
    latest = data["latest"]
    semiprime = data["semiprime"]
    source_packet = data["source_packet"]
    pointwise = data["pointwise"]
    source_atoms = f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"
    return [
        row(
            "LatestConstructorFirstSeedHardpointImported",
            latest.get("next_primary_attack_target") == FIRST_SEED
            and FIRST_SEED in latest.get("next_edge_attack_targets", []),
            False,
            "上一层 constructor edge slab 同步已把 FIRST_SEED 登记为直接主攻点。",
            FIRST_SEED,
        ),
        row(
            "ConstructorSideGatesCarried",
            latest.get("parallel_constructor_side_gates") == f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
            False,
            "本层只替换 FIRST_SEED；signed survival 与 row-mass/no-heavy-row 仍是 constructor 侧门。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "SemiprimeDiagonalRouterImported",
            semiprime.get("target_input_before_router") == FIRST_SEED
            and semiprime.get("semiprime_seed_diagonal_frontier_router_closed") is True,
            True,
            "既有 semiprime diagonal/offdiagonal 证书可作为 FIRST_SEED 的直接下游。",
            f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
        ),
        row(
            "DiagonalOffDiagonalSupportSplitClosed",
            semiprime.get("diagonal_offdiagonal_support_split_proved") is True,
            True,
            "LPF/Phi first-edge seed 类型唯一分成 p=q diagonal 与 p<q offdiagonal。",
            f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
        ),
        row(
            "DiagonalPrivateEscapeRemoved",
            semiprime.get("diagonal_square_base_private_signed_escape_removed") is True,
            True,
            "diagonal `(p,p)` 不再是独立 signed lane；它已回到 common source packet。",
            COMMON_PACKET,
        ),
        row(
            "CommonPacketCycleGuardCarriedForward",
            source_packet.get("common_packet_self_proof_rejected_after_lpf") is True
            or source_packet.get("common_packet_self_proof_blocked") is True,
            True,
            "common packet 不能用 signed-lane 固定点自证；latest constructor 前沿已把它携带为 source 三原子。",
            source_atoms,
        ),
        row(
            "LatestBasisReplacesFirstSeedWithOffdiagSeed",
            semiprime.get("next_primary_attack_target") == OFFDIAG_SEED
            and latest.get("parallel_source_packet_attack_target") == source_atoms,
            False,
            "在 constructor 最新基中，FIRST_SEED 的 diagonal 义务由 source 三原子承接，新增 seed 缺口收窄到 offdiagonal 表。",
            OFFDIAG_SEED,
        ),
        row(
            "OffDiagonalSeedStillOpen",
            semiprime.get("offdiagonal_ordered_semiprime_signed_seed_table_proved") is False,
            False,
            "当前材料没有为所有 p<q ordered semiprime first edges 给出 signed seed 表。",
            OFFDIAG_SEED,
        ),
        row(
            "InternalTransitionStillPaired",
            latest.get("internal_prime_adjoin_signed_transition_law_proved") is False
            or semiprime.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "FIRST_SEED 收窄后，internal prime-adjoin transition 仍是同一递推路线的配套硬点。",
            INTERNAL_TRANSITION,
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
            "本步只同步 FIRST_SEED 的 diagonal/offdiagonal 拆分；未证明 offdiagonal seed、internal transition、source 三原子、signed survival、row-mass 或 ExactUV。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    data = {
        "latest": load_json(LATEST_CONSTRUCTOR_EDGE_CERT),
        "semiprime": load_json(SEMIPRIME_DIAGONAL_CERT),
        "source_packet": load_json(SOURCE_PACKET_CYCLE_CERT),
        "pointwise": load_json(POINTWISE_FRONTIER_CERT),
    }
    rows = build_rows(data)
    source_atoms = f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"
    latest_basis = (
        f"(({source_atoms} AND {OFFDIAG_SEED} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) "
        f"OR {POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR "
        f"{TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {NEW_JOINT}) AND {NONZERO_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_semiprime_seed_diagonal_sync_router",
        "status": "phi_lpf_latest_constructor_semiprime_seed_synced_to_offdiag_and_source_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_constructor_first_seed_hardpoint_imported": rows[0]["closed"],
        "constructor_side_gates_carried": rows[1]["closed"],
        "semiprime_diagonal_router_imported": rows[2]["closed"],
        "diagonal_offdiagonal_support_split_closed": rows[3]["closed"],
        "diagonal_private_escape_removed": rows[4]["closed"],
        "common_packet_cycle_guard_carried_forward": rows[5]["closed"],
        "latest_basis_replaces_first_seed_with_offdiag_seed": rows[6]["closed"],
        "offdiagonal_ordered_semiprime_signed_seed_table_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": FIRST_SEED,
        "next_primary_attack_target": OFFDIAG_SEED,
        "paired_required_attack_target": INTERNAL_TRANSITION,
        "carried_source_packet_attack_target": source_atoms,
        "parallel_constructor_side_gates": f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": latest_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "imported_largest_sample": largest_sample(data["semiprime"]),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor-latest `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` "
            "接入既有 diagonal/offdiagonal 拆分。diagonal `(p,p)` 已无私有 signed 出口，并由 "
            "source-packet 三原子承接；因此 FIRST_SEED 的新增 signed 缺口收窄为 "
            "`PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`。internal transition、"
            "signed survival 与 row-mass/no-heavy-row 仍保留；行/列命题仍未无条件证明。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor semiprime seed diagonal sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_first_seed_hardpoint_imported={fmt_bool(cert['latest_constructor_first_seed_hardpoint_imported'])}",
        f"constructor_side_gates_carried={fmt_bool(cert['constructor_side_gates_carried'])}",
        f"semiprime_diagonal_router_imported={fmt_bool(cert['semiprime_diagonal_router_imported'])}",
        f"diagonal_offdiagonal_support_split_closed={fmt_bool(cert['diagonal_offdiagonal_support_split_closed'])}",
        f"diagonal_private_escape_removed={fmt_bool(cert['diagonal_private_escape_removed'])}",
        f"common_packet_cycle_guard_carried_forward={fmt_bool(cert['common_packet_cycle_guard_carried_forward'])}",
        f"latest_basis_replaces_first_seed_with_offdiag_seed={fmt_bool(cert['latest_basis_replaces_first_seed_with_offdiag_seed'])}",
        f"offdiagonal_ordered_semiprime_signed_seed_table_proved={fmt_bool(cert['offdiagonal_ordered_semiprime_signed_seed_table_proved'])}",
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
                "| N | first types | diag types | offdiag types | first occ | diag occ | offdiag occ | ok |",
                "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
                (
                    f"| {sample['N']} | {sample['first_edge_seed_types']} | "
                    f"{sample['diagonal_square_seed_types']} | {sample['offdiagonal_semiprime_seed_types']} | "
                    f"{sample['first_edge_occurrences']} | {sample['diagonal_square_seed_occurrences']} | "
                    f"{sample['offdiagonal_semiprime_seed_occurrences']} | "
                    f"`{fmt_bool(sample['diagonal_offdiag_occurrence_partition_holds'])}` |"
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
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "配套仍需：",
            "",
            "```text",
            cert["paired_required_attack_target"],
            "```",
            "",
            "已携带 source-packet 三原子：",
            "",
            "```text",
            cert["carried_source_packet_attack_target"],
            "```",
            "",
            "并行 constructor 侧门：",
            "",
            "```text",
            cert["parallel_constructor_side_gates"],
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
