#!/usr/bin/env python3
"""生成 latest constructor common-table transport-stack rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_common_table_transport_stack_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-transport-stack-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-common-table-transport-stack-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-transport-stack-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-transport-stack-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-common-table-transport-stack-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

COMMON_TABLE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync-router.json"
)
TRANSPORT_STACK_CERT = DOCS / "prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-router.json"
BUCKET_TRANSPORT_CERT = DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json"
STEP_UPDATE_CERT = DOCS / "prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json"
SOURCE_PACKET_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"

SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
EDGE_MULTIPLIER = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
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
        COMMON_TABLE_CERT,
        TRANSPORT_STACK_CERT,
        BUCKET_TRANSPORT_CERT,
        STEP_UPDATE_CERT,
        SOURCE_PACKET_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def tail_package() -> str:
    """给出 beta-sieve/sawtooth 尾包。"""
    return f"{BETA_APPENDIX} AND {BETA_99} AND {SAWTOOTH}"


def source_three_atoms() -> str:
    """给出同源表三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {SAME_RANK}"


def transport_common_frontier() -> str:
    """给出 bucket signed law 被 transport stack 替换后的共同表。"""
    return (
        f"{source_three_atoms()} AND {EDGE_MULTIPLIER} AND {ROW_MASS} "
        f"AND {ROW_SUPPORT} AND {COMPLETE_KEY} AND {FIXED_KEY}"
    )


def pointwise_bypass_frontier() -> str:
    """给出直接提交逐点 signed table 时仍需携带的同表字段。"""
    return (
        f"{source_three_atoms()} AND {POINTWISE_TABLE} AND {ROW_MASS} "
        f"AND {ROW_SUPPORT} AND {COMPLETE_KEY} AND {FIXED_KEY}"
    )


def latest_basis_after_router() -> str:
    """给出当前 latest constructor 内部基。"""
    return f"{transport_common_frontier()} AND {tail_package()} AND {RATE} AND {DSTRUCTURE}"


def retained_basis() -> str:
    """给出旁路保留后的基。"""
    alternatives = (
        f"({transport_common_frontier()}) OR ({pointwise_bypass_frontier()}) "
        f"OR {PDEC_SCOPE} OR {TERMINAL_DESCENT} OR {EXTERNAL_KZ}"
    )
    return f"(({alternatives}) AND {tail_package()}) AND {RATE} AND {DSTRUCTURE}"


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 common-table transport-stack rebase 判定表。"""
    common = data["common"]
    stack = data["stack"]
    bucket = data["bucket"]
    step = data["step"]
    packet = data["packet"]

    common_imported = (
        common.get("common_same_formal_unit_signed_table_aligned") is True
        and common.get("next_primary_attack_target") == SIGNED_LAW
        and common.get("phi_lpf_bucket_signed_coefficient_law_proved") is False
    )
    stack_imported = (
        stack.get("latest_bucket_signed_law_imported") is True
        and stack.get("next_primary_attack_target") == EDGE_MULTIPLIER
    )
    signed_transport_split = (
        bucket.get("phi_lpf_bucket_signed_coefficient_law_proved") is False
        and bucket.get("phi_lpf_rough_cofactor_signed_transport_law_proved") is False
        and bucket.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
    )
    step_imported = (
        stack.get("step_update_reduced_to_edge_multiplier") is True
        and step.get("next_direct_attack_target") == EDGE_MULTIPLIER
        and step.get("edge_signed_multiplier_table_proved") is False
    )
    packet_guard = (
        stack.get("common_packet_cycle_guard_imported") is True
        and (
            packet.get("common_packet_self_proof_rejected_after_lpf") is True
            or packet.get("common_packet_self_proof_blocked") is True
        )
    )
    rebase_closed = all(
        [
            common_imported,
            stack_imported,
            signed_transport_split,
            step_imported,
            packet_guard,
        ]
    )
    tail_open = (
        common.get("self_contained_beta_sieve_appendix_proved") is False
        and common.get("beta_sieve_main_coefficient_99_proved") is False
        and common.get("exact_residue_weighted_floor_sawtooth_bound_proved") is False
    )

    return [
        row(
            "CommonSignedTableImported",
            common_imported,
            False,
            "上一层已把 constructor 三线压到同 formal unit 共同表，其中首个 signed 口是 bucket signed law。",
            common.get("common_same_formal_unit_signed_table_frontier", SIGNED_LAW),
        ),
        row(
            "BucketTransportStackImported",
            stack_imported,
            False,
            "既有 bucket transport stack 把 bucket signed law 改写为 rough-cofactor transport 或逐点 signed table。",
            f"{EDGE_MULTIPLIER} OR {POINTWISE_TABLE}",
        ),
        row(
            "SignedTransportSplitImported",
            signed_transport_split,
            False,
            "Phi 递推只给 support split；signed 递推必须支付 cofactor transport，或直接给逐点表。",
            f"PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward OR {POINTWISE_TABLE}",
        ),
        row(
            "StepUpdateReducedToEdgeMultiplier",
            step_imported,
            False,
            "ordered LPF path 已固定后，cofactor transport 的实际 signed 字段是逐 edge multiplier 表。",
            EDGE_MULTIPLIER,
        ),
        row(
            "SourcePacketCycleGuardCarried",
            packet_guard,
            True,
            "square-base/common-packet 私有出口已回流到 source 三原子，不能作为 bucket law 自证。",
            source_three_atoms(),
        ),
        row(
            "BucketSignedLawRemovedFromCommonTable",
            rebase_closed,
            False,
            "bucket signed law 粗名已被替换为 edge multiplier 或逐点 signed table 旁路。",
            transport_common_frontier(),
        ),
        row(
            "TailPackageStillOpen",
            tail_open,
            False,
            "充分大阈值和有限验证仍不能替代 beta-sieve、99% 主系数与 exact sawtooth。",
            tail_package(),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 transport-stack rebase；未证明 edge multiplier、source 三原子、row mass/support、key multiplicity 或尾段。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "common": load_json(COMMON_TABLE_CERT),
        "stack": load_json(TRANSPORT_STACK_CERT),
        "bucket": load_json(BUCKET_TRANSPORT_CERT),
        "step": load_json(STEP_UPDATE_CERT),
        "packet": load_json(SOURCE_PACKET_CERT),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_common_table_transport_stack_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_common_table_transport_stack_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "common_signed_table_imported": rows[0]["closed"],
        "bucket_transport_stack_imported": rows[1]["closed"],
        "signed_transport_split_imported": rows[2]["closed"],
        "step_update_reduced_to_edge_multiplier": rows[3]["closed"],
        "source_packet_cycle_guard_carried": rows[4]["closed"],
        "bucket_signed_law_removed_from_common_table": rows[5]["closed"],
        "tail_package_still_open": rows[6]["closed"],
        "edge_signed_multiplier_table_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncircular_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "primitive_row_support_lower_bound_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SIGNED_LAW,
        "common_table_before_router": load_json(COMMON_TABLE_CERT).get(
            "common_same_formal_unit_signed_table_frontier", ""
        ),
        "latest_internal_basis_after_router": latest_basis_after_router(),
        "latest_retained_basis_after_router": retained_basis(),
        "next_primary_attack_target": EDGE_MULTIPLIER,
        "parallel_primary_attack_target": source_three_atoms(),
        "parallel_direct_bypass": pointwise_bypass_frontier(),
        "next_direct_attack_target": (
            f"{transport_common_frontier()} AND {BETA_APPENDIX}_THEN_ExactSawtooth"
        ),
        "structural_chain": [
            f"{SIGNED_LAW} -> PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward OR {POINTWISE_TABLE}",
            "PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward -> ordered path + step local-factor update",
            f"step local-factor update -> {EDGE_MULTIPLIER}",
            f"common table -> {transport_common_frontier()}",
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把共同 signed-table 前沿中的 `PhiLPFBucketSignedCoefficientLawBeforePushforward` "
            "接入既有 rough-cofactor transport stack。LPF/Phi 递推继续只给无符号 support split；"
            "若不直接提交逐点 Phi-LPF signed value table，就必须给逐 ordered edge 的 signed multiplier 表。"
            "因此 bucket signed law 粗名被移除，最新剩余是 edge multiplier、source 三原子、row-mass/"
            "support、complete/fixed key 与 beta-sieve/sawtooth 尾段。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor common-table transport-stack rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"common_signed_table_imported={fmt_bool(result['common_signed_table_imported'])}",
        f"bucket_transport_stack_imported={fmt_bool(result['bucket_transport_stack_imported'])}",
        f"signed_transport_split_imported={fmt_bool(result['signed_transport_split_imported'])}",
        f"step_update_reduced_to_edge_multiplier={fmt_bool(result['step_update_reduced_to_edge_multiplier'])}",
        f"source_packet_cycle_guard_carried={fmt_bool(result['source_packet_cycle_guard_carried'])}",
        f"bucket_signed_law_removed_from_common_table={fmt_bool(result['bucket_signed_law_removed_from_common_table'])}",
        f"tail_package_still_open={fmt_bool(result['tail_package_still_open'])}",
        f"edge_signed_multiplier_table_proved={fmt_bool(result['edge_signed_multiplier_table_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(result['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(result['same_formal_unit_row_mass_normalization_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_o1_proved={fmt_bool(result['fixed_key_exact_uv_local_multiplicity_o1_proved'])}",
        f"self_contained_beta_sieve_appendix_proved={fmt_bool(result['self_contained_beta_sieve_appendix_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
        "\n".join(result["structural_chain"]),
        "```",
        "",
        "## 2. 判定表",
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
            "并行 source 三原子：",
            "",
            "```text",
            result["parallel_primary_attack_target"],
            "```",
            "",
            "直接逐点旁路：",
            "",
            "```text",
            result["parallel_direct_bypass"],
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
