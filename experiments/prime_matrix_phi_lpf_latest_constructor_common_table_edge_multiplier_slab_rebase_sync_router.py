#!/usr/bin/env python3
"""生成 latest constructor common-table edge multiplier slab rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_common_table_edge_multiplier_slab_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-edge-multiplier-slab-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-common-table-edge-multiplier-slab-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-edge-multiplier-slab-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-edge-multiplier-slab-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-common-table-edge-multiplier-slab-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

COMMON_TABLE_TRANSPORT_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-common-table-transport-stack-rebase-sync-router.json"
)
LATEST_EDGE_SLAB_CERT = DOCS / "prime-matrix-phi-lpf-latest-edge-multiplier-slab-sync-router.json"
FIRST_EDGE_SLAB_CERT = DOCS / "prime-matrix-phi-lpf-first-edge-slab-frontier-router.json"
SEMIPRIME_DIAGONAL_CERT = DOCS / "prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json"

EDGE_MULTIPLIER = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
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
    """读取 JSON 证书；缺失依赖不能当成闭合。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
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
        COMMON_TABLE_TRANSPORT_CERT,
        LATEST_EDGE_SLAB_CERT,
        FIRST_EDGE_SLAB_CERT,
        SEMIPRIME_DIAGONAL_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def source_three_atoms() -> str:
    """给出共同表 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def tail_package() -> str:
    """给出 beta-sieve/sawtooth 尾包。"""
    return f"{BETA_APPENDIX} AND {BETA_99} AND {SAWTOOTH}"


def side_table_gates() -> str:
    """给出共同表里必须平行保留的侧门。"""
    return f"{ROW_MASS} AND {ROW_SUPPORT} AND {COMPLETE_KEY} AND {FIXED_KEY}"


def first_edge_common_frontier() -> str:
    """给出 edge multiplier 拆解后的共同表前沿。"""
    return f"{source_three_atoms()} AND {FIRST_SEED} AND {INTERNAL_TRANSITION} AND {side_table_gates()}"


def pointwise_common_frontier() -> str:
    """给出逐点 signed table 旁路的共同表前沿。"""
    return f"{source_three_atoms()} AND {POINTWISE_TABLE} AND {side_table_gates()}"


def latest_internal_basis_after_router() -> str:
    """给出本层同步后的最新内部基。"""
    return f"{first_edge_common_frontier()} AND {tail_package()} AND {RATE} AND {DSTRUCTURE}"


def retained_basis() -> str:
    """给出旁路保留后的最新条件基。"""
    alternatives = (
        f"({first_edge_common_frontier()}) OR ({pointwise_common_frontier()}) "
        f"OR {PDEC_SCOPE} OR {TERMINAL_DESCENT} OR {EXTERNAL_KZ}"
    )
    return f"(({alternatives}) AND {tail_package()}) AND {RATE} AND {DSTRUCTURE}"


def sample_summary(first_edge: dict[str, Any]) -> dict[str, Any]:
    """抽取 first-edge slab 最大样本读数。"""
    samples = first_edge.get("sample_first_edge_slab_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def sync_chain() -> list[dict[str, str]]:
    """列出本层同步链。"""
    return [
        {
            "from": EDGE_MULTIPLIER,
            "to": f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
            "meaning": "共同表里的逐 edge signed multiplier 按 LPF ordered path 唯一拆成第一边 seed 与内部 adjoin transition。",
        },
        {
            "from": "mass(p,q)=Phi(floor(N/(p*q)),q)",
            "to": "unsigned occurrence / q-rough continuation support",
            "meaning": "LPF/Phi 精准桶只支付第一边 continuation 容量，不支付 signed seed、orientation 或 ExactUV 字段。",
        },
        {
            "from": "common-table side gates",
            "to": side_table_gates(),
            "meaning": "row mass、projection 前支撑、complete key 与 fixed-key multiplicity 不是 edge slab 拆解的副产品，必须继续保留。",
        },
        {
            "from": "large-threshold plus finite verification",
            "to": tail_package(),
            "meaning": "充分大阈值加有限验证仍只关闭有限桥，不能替代 beta-sieve/sawtooth 尾段。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 common-table edge slab rebase 判定表。"""
    common = data["common"]
    latest_edge = data["latest_edge"]
    first_edge = data["first_edge"]
    semiprime = data["semiprime"]

    common_edge_active = (
        common.get("next_primary_attack_target") == EDGE_MULTIPLIER
        and common.get("bucket_signed_law_removed_from_common_table") is True
    )
    latest_edge_available = (
        latest_edge.get("target_input_before_router") == EDGE_MULTIPLIER
        and latest_edge.get("edge_multiplier_split_synced_to_latest_basis") is True
    )
    first_edge_imported = (
        first_edge.get("target_input_before_router") == EDGE_MULTIPLIER
        and first_edge.get("first_edge_slab_frontier_router_closed") is True
    )
    phi_fiber_guard = (
        first_edge.get("first_edge_phi_fiber_formula_proved") is True
        and first_edge.get("semiprime_first_edge_signed_seed_table_proved") is False
    )
    semiprime_downstream = (
        semiprime.get("target_input_before_router") == FIRST_SEED
        and semiprime.get("semiprime_seed_diagonal_frontier_router_closed") is True
    )
    tail_open = common.get("tail_package_still_open") is True
    rebase_closed = all([common_edge_active, latest_edge_available, first_edge_imported, phi_fiber_guard])

    return [
        row(
            "CommonTableTransportEdgeMultiplierImported",
            common_edge_active,
            False,
            "上一层 common-table transport rebase 已把 bucket signed law 粗名替换成逐 edge multiplier。",
            EDGE_MULTIPLIER,
        ),
        row(
            "LatestEdgeMultiplierSlabReusable",
            latest_edge_available,
            True,
            "既有 latest edge slab 证书目标输入相同，可用于最新 common-table 前沿。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "FirstEdgeSlabRouterImported",
            first_edge_imported,
            True,
            "first-edge slab 证书严格拆出 prefix=1 semiprime first seed 与 prefix>1 internal transition。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "PhiFiberUnsignedOnlyGuardImported",
            phi_fiber_guard,
            True,
            "Phi(floor(N/(p*q)),q) 只给 q-rough continuation occurrence mass，不能反推 signed seed。",
            FIRST_SEED,
        ),
        row(
            "CommonTableSideGatesCarried",
            True,
            False,
            "edge slab 只替换 edge multiplier；source 三原子、row-mass/support 与 key multiplicity 仍平行保留。",
            f"{source_three_atoms()} AND {side_table_gates()}",
        ),
        row(
            "TailPackageStillOpen",
            tail_open,
            False,
            "充分大阈值和有限验证仍不能替代 beta-sieve、99% 主系数与 exact sawtooth。",
            tail_package(),
        ),
        row(
            "EdgeMultiplierSlabRebasedIntoCommonTable",
            rebase_closed,
            False,
            "最新 common-table 中的 edge multiplier 已替换为 first seed 与 internal transition 的合取。",
            first_edge_common_frontier(),
        ),
        row(
            "SemiprimeFirstSeedCurrentCorpusProved",
            False,
            False,
            "当前材料没有为所有 semiprime first edges 给出推前前 signed seed table。",
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
            "SemiprimeDiagonalDownstreamAvailable",
            semiprime_downstream,
            False,
            "first seed 可继续拆到 diagonal common packet 与 offdiagonal seed，但这仍不是 signed 表证明。",
            semiprime.get("retained_basis_after_router", FIRST_SEED),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 common-table edge slab rebase；未证明 first seed、internal transition、source 三原子、row mass/support、key multiplicity 或尾段。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "common": load_json(COMMON_TABLE_TRANSPORT_CERT),
        "latest_edge": load_json(LATEST_EDGE_SLAB_CERT),
        "first_edge": load_json(FIRST_EDGE_SLAB_CERT),
        "semiprime": load_json(SEMIPRIME_DIAGONAL_CERT),
    }
    rows = build_rows(data)
    sample = sample_summary(data["first_edge"])
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_common_table_edge_multiplier_slab_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_common_table_edge_multiplier_slab_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "common_table_transport_edge_multiplier_imported": rows[0]["closed"],
        "latest_edge_multiplier_slab_reusable": rows[1]["closed"],
        "first_edge_slab_router_imported": rows[2]["closed"],
        "first_edge_phi_fiber_formula_imported": rows[3]["closed"],
        "phi_fiber_unsigned_only_guard_imported": rows[3]["closed"],
        "common_table_side_gates_carried": rows[4]["closed"],
        "tail_package_still_open": rows[5]["closed"],
        "edge_multiplier_slab_rebased": rows[6]["closed"],
        "semiprime_diagonal_downstream_available": rows[9]["closed"],
        "edge_signed_multiplier_table_proved": False,
        "semiprime_first_edge_signed_seed_table_proved": False,
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
        "target_input_before_router": EDGE_MULTIPLIER,
        "common_table_before_router": data["common"].get("latest_internal_basis_after_router", ""),
        "latest_internal_basis_after_router": latest_internal_basis_after_router(),
        "latest_retained_basis_after_router": retained_basis(),
        "next_primary_attack_target": FIRST_SEED,
        "paired_required_attack_target": INTERNAL_TRANSITION,
        "parallel_source_packet_attack_target": source_three_atoms(),
        "parallel_common_table_side_gates": side_table_gates(),
        "parallel_direct_bypass": pointwise_common_frontier(),
        "tail_package_attack_target": tail_package(),
        "next_direct_attack_target": (
            f"{first_edge_common_frontier()} AND {BETA_APPENDIX}_THEN_ExactSawtooth"
        ),
        "sync_chain": sync_chain(),
        "sample_first_edge_slab_max_N": sample,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor common-table transport 前沿中的 "
            "`PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward` 接入 first-edge slab。"
            "edge multiplier 不是新的终端黑箱；它按 LPF ordered path 唯一拆成 "
            "`PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` 与 "
            "`PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward`。LPF/Phi 精准桶递推只支付 "
            "first-edge q-rough continuation 容量，不生成 signed seed、local factor、row mass、key "
            "multiplicity 或 beta-sieve/sawtooth 尾段。因此最新共同表硬点改为 first seed/internal "
            "transition 加 source 三原子、row-mass/support、complete/fixed key 与尾段。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor common-table edge multiplier slab rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"common_table_transport_edge_multiplier_imported={fmt_bool(result['common_table_transport_edge_multiplier_imported'])}",
        f"latest_edge_multiplier_slab_reusable={fmt_bool(result['latest_edge_multiplier_slab_reusable'])}",
        f"first_edge_slab_router_imported={fmt_bool(result['first_edge_slab_router_imported'])}",
        f"first_edge_phi_fiber_formula_imported={fmt_bool(result['first_edge_phi_fiber_formula_imported'])}",
        f"phi_fiber_unsigned_only_guard_imported={fmt_bool(result['phi_fiber_unsigned_only_guard_imported'])}",
        f"common_table_side_gates_carried={fmt_bool(result['common_table_side_gates_carried'])}",
        f"tail_package_still_open={fmt_bool(result['tail_package_still_open'])}",
        f"edge_multiplier_slab_rebased={fmt_bool(result['edge_multiplier_slab_rebased'])}",
        f"semiprime_first_edge_signed_seed_table_proved={fmt_bool(result['semiprime_first_edge_signed_seed_table_proved'])}",
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
    sample = result.get("sample_first_edge_slab_max_N") or {}
    if sample:
        lines.extend(
            [
                "",
                "## 3. 导入样本读数",
                "",
                "| N | support | first occ | internal occ | first types | max depth | Phi fiber ok |",
                "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
                (
                    f"| {sample.get('N')} | {sample.get('support_keys')} | "
                    f"{sample.get('first_edge_occurrences')} | {sample.get('internal_edge_occurrences')} | "
                    f"{sample.get('distinct_first_edge_types')} | {sample.get('max_factor_depth')} | "
                    f"`{fmt_bool(sample.get('first_edge_phi_fiber_formula_holds'))}` |"
                ),
            ]
        )
    lines.extend(
        [
            "",
            "## 4. 最新内部基",
            "",
            "```text",
            result["latest_internal_basis_after_router"],
            "```",
            "",
            "## 5. 保留条件基",
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
            "## 6. 依赖哈希",
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
