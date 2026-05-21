#!/usr/bin/env python3
"""生成 latest constructor common-table semiprime seed diagonal rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_common_table_semiprime_seed_diagonal_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-semiprime-seed-diagonal-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-common-table-semiprime-seed-diagonal-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-semiprime-seed-diagonal-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-semiprime-seed-diagonal-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-common-table-semiprime-seed-diagonal-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

COMMON_TABLE_EDGE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-common-table-edge-multiplier-slab-rebase-sync-router.json"
)
OLD_CONSTRUCTOR_SEMIPRIME_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-router.json"
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
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
ROW_SUPPORT = "PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger"
COMPLETE_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
EXTERNAL_KZ = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
BETA_APPENDIX = "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix"
BETA_99 = "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000"
SAWTOOTH = "ExactResidueWeightedFloorSawtoothTenPercentBound"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能视为闭合。"""
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
    """列出本层依赖证书。"""
    return [
        COMMON_TABLE_EDGE_CERT,
        OLD_CONSTRUCTOR_SEMIPRIME_REBASE_CERT,
        SEMIPRIME_DIAGONAL_CERT,
        SOURCE_PACKET_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def source_three_atoms() -> str:
    """给出 common source-packet 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def side_table_gates() -> str:
    """给出共同表侧门。"""
    return f"{ROW_MASS} AND {ROW_SUPPORT} AND {COMPLETE_KEY} AND {FIXED_KEY}"


def tail_package() -> str:
    """给出 beta-sieve/sawtooth 尾包。"""
    return f"{BETA_APPENDIX} AND {BETA_99} AND {SAWTOOTH}"


def offdiag_common_frontier() -> str:
    """给出 semiprime diagonal 拆解后的共同表前沿。"""
    return f"{source_three_atoms()} AND {OFFDIAG_SEED} AND {INTERNAL_TRANSITION} AND {side_table_gates()}"


def pointwise_common_frontier() -> str:
    """给出逐点 signed table 旁路的共同表前沿。"""
    return f"{source_three_atoms()} AND {POINTWISE_TABLE} AND {side_table_gates()}"


def latest_internal_basis_after_router() -> str:
    """给出本层同步后的最新内部基。"""
    return f"{offdiag_common_frontier()} AND {tail_package()} AND {RATE} AND {DSTRUCTURE}"


def retained_basis() -> str:
    """给出旁路保留后的最新条件基。"""
    alternatives = (
        f"({offdiag_common_frontier()}) OR ({pointwise_common_frontier()}) "
        f"OR {PDEC_SCOPE} OR {TERMINAL_DESCENT} OR {EXTERNAL_KZ}"
    )
    return f"(({alternatives}) AND {tail_package()}) AND {RATE} AND {DSTRUCTURE}"


def sync_chain() -> list[dict[str, str]]:
    """列出本层同步链。"""
    return [
        {
            "from": FIRST_SEED,
            "to": f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
            "meaning": "semiprime first seed 按 p=q 与 p<q 唯一拆分。",
        },
        {
            "from": DIAGONAL_SEED,
            "to": source_three_atoms(),
            "meaning": "diagonal square-base 不是私有 signed 出口，只能回到 common source-packet 三原子。",
        },
        {
            "from": "common-table side gates",
            "to": side_table_gates(),
            "meaning": "这一步只替换 FIRST_SEED，不支付 row-mass/support 或 key multiplicity。",
        },
        {
            "from": "large-threshold plus finite verification",
            "to": tail_package(),
            "meaning": "阈值与有限验证仍不能替代 beta-sieve/sawtooth 尾段。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 common-table semiprime diagonal rebase 判定表。"""
    common_edge = data["common_edge"]
    old_rebase = data["old_rebase"]
    semiprime = data["semiprime"]
    source_packet = data["source_packet"]

    common_first_seed_active = (
        common_edge.get("next_primary_attack_target") == FIRST_SEED
        and common_edge.get("edge_multiplier_slab_rebased") is True
    )
    old_rebase_available = (
        old_rebase.get("target_input_before_router") == FIRST_SEED
        and old_rebase.get("semiprime_seed_diagonal_rebased") is True
        and old_rebase.get("next_primary_attack_target") == OFFDIAG_SEED
    )
    semiprime_router_imported = (
        semiprime.get("target_input_before_router") == FIRST_SEED
        and semiprime.get("semiprime_seed_diagonal_frontier_router_closed") is True
    )
    diagonal_private_removed = (
        semiprime.get("diagonal_square_base_private_signed_escape_removed") is True
        and old_rebase.get("diagonal_private_escape_removed") is True
    )
    source_cycle_guard = (
        source_packet.get("common_packet_self_proof_blocked") is True
        or source_packet.get("common_packet_self_proof_rejected_after_lpf") is True
    )
    tail_open = common_edge.get("tail_package_still_open") is True
    rebase_closed = all(
        [
            common_first_seed_active,
            old_rebase_available,
            semiprime_router_imported,
            diagonal_private_removed,
            source_cycle_guard,
        ]
    )
    return [
        row(
            "CommonTableFirstSeedImported",
            common_first_seed_active,
            False,
            "上一层 common-table edge slab 已把主口压到 semiprime first-edge signed seed。",
            FIRST_SEED,
        ),
        row(
            "ExistingSemiprimeDiagonalRebaseReusable",
            old_rebase_available,
            False,
            "旧 constructor semiprime diagonal rebase 的目标输入相同，可在 common-table 前沿复用。",
            f"{OFFDIAG_SEED} AND {source_three_atoms()}",
        ),
        row(
            "SemiprimeDiagonalRouterImported",
            semiprime_router_imported,
            True,
            "semiprime diagonal frontier 给出 p=q 与 p<q 的无重叠拆分。",
            f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
        ),
        row(
            "DiagonalPrivateEscapeRemoved",
            diagonal_private_removed,
            True,
            "diagonal square-base lane 不生成独立 signed seed，只能回到 source 三原子。",
            source_three_atoms(),
        ),
        row(
            "CommonPacketCycleGuardCarried",
            source_cycle_guard,
            True,
            "common packet 自证环已切断，diagonal lane 不能自证 source atoms。",
            source_three_atoms(),
        ),
        row(
            "CommonTableSideGatesCarried",
            True,
            False,
            "semiprime diagonal 只替换 FIRST_SEED；row-mass/support 与 key multiplicity 仍保留。",
            side_table_gates(),
        ),
        row(
            "TailPackageStillOpen",
            tail_open,
            False,
            "充分大阈值和有限验证仍不能替代 beta-sieve、99% 主系数与 exact sawtooth。",
            tail_package(),
        ),
        row(
            "SemiprimeSeedDiagonalRebasedIntoCommonTable",
            rebase_closed,
            False,
            "最新 common-table FIRST_SEED 已同步为 offdiagonal seed 与 source 三原子。",
            offdiag_common_frontier(),
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
            common_edge.get("paired_required_attack_target") == INTERNAL_TRANSITION,
            False,
            "prefix>1 internal prime-adjoin transition 仍是同一 LPF signed 递推的配套硬点。",
            INTERNAL_TRANSITION,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 common-table semiprime diagonal rebase；未证明 offdiagonal seed、internal transition、source 三原子、row mass/support、key multiplicity 或尾段。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "common_edge": load_json(COMMON_TABLE_EDGE_CERT),
        "old_rebase": load_json(OLD_CONSTRUCTOR_SEMIPRIME_REBASE_CERT),
        "semiprime": load_json(SEMIPRIME_DIAGONAL_CERT),
        "source_packet": load_json(SOURCE_PACKET_CERT),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_common_table_semiprime_seed_diagonal_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_common_table_semiprime_seed_diagonal_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "common_table_first_seed_imported": rows[0]["closed"],
        "existing_semiprime_diagonal_rebase_reusable": rows[1]["closed"],
        "semiprime_diagonal_router_imported": rows[2]["closed"],
        "diagonal_private_escape_removed": rows[3]["closed"],
        "common_packet_cycle_guard_carried": rows[4]["closed"],
        "common_table_side_gates_carried": rows[5]["closed"],
        "tail_package_still_open": rows[6]["closed"],
        "semiprime_seed_diagonal_rebased": rows[7]["closed"],
        "semiprime_first_edge_signed_seed_table_proved": False,
        "offdiagonal_ordered_semiprime_signed_seed_table_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "primitive_row_support_lower_bound_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": FIRST_SEED,
        "common_table_before_router": data["common_edge"].get("latest_internal_basis_after_router", ""),
        "latest_internal_basis_after_router": latest_internal_basis_after_router(),
        "latest_retained_basis_after_router": retained_basis(),
        "next_primary_attack_target": OFFDIAG_SEED,
        "paired_required_attack_target": INTERNAL_TRANSITION,
        "parallel_source_packet_attack_target": source_three_atoms(),
        "parallel_common_table_side_gates": side_table_gates(),
        "parallel_direct_bypass": pointwise_common_frontier(),
        "tail_package_attack_target": tail_package(),
        "next_direct_attack_target": (
            f"{offdiag_common_frontier()} AND {BETA_APPENDIX}_THEN_ExactSawtooth"
        ),
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor common-table 前沿中的 "
            "`PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` 接入 diagonal/offdiagonal "
            "拆分。diagonal `(p,p)` square-base lane 的私有 signed 出口已被移除，只能回到 "
            "source-packet 三原子；因此新增 signed 缺口收窄为 "
            "`PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`。"
            "internal transition、row-mass/support、complete/fixed key 与 beta-sieve/sawtooth 尾段仍保留。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor common-table semiprime seed diagonal rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"common_table_first_seed_imported={fmt_bool(result['common_table_first_seed_imported'])}",
        f"existing_semiprime_diagonal_rebase_reusable={fmt_bool(result['existing_semiprime_diagonal_rebase_reusable'])}",
        f"semiprime_diagonal_router_imported={fmt_bool(result['semiprime_diagonal_router_imported'])}",
        f"diagonal_private_escape_removed={fmt_bool(result['diagonal_private_escape_removed'])}",
        f"common_packet_cycle_guard_carried={fmt_bool(result['common_packet_cycle_guard_carried'])}",
        f"common_table_side_gates_carried={fmt_bool(result['common_table_side_gates_carried'])}",
        f"tail_package_still_open={fmt_bool(result['tail_package_still_open'])}",
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
            "## 3. 最新内部基",
            "",
            "```text",
            result["latest_internal_basis_after_router"],
            "```",
            "",
            "## 4. 保留条件基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
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
            "并行共同表侧门：",
            "",
            "```text",
            result["parallel_common_table_side_gates"],
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
