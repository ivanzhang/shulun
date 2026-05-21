#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor row-level signed-source fixed-point 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_row_level_signed_source_fixed_point_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

TERMINAL_NEW_JOINT_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-terminal-new-joint-macrocycle-sync-router.json"
)
ROW_LEVEL_CERT = DOCS / "prime-matrix-strict-row-level-origin-generation-table-router.json"
FIXED_POINT_CERT = DOCS / "prime-matrix-strict-signed-source-fixed-point-breaker-router.json"
SEED_CYCLE_GUARD_CERT = (
    DOCS / "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"
)

SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
SEED_EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
ROW_LEVEL = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
NONCIRCULAR_KERNEL = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
HARMONIC = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
SOURCE_EXACTUV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
TERMINAL_WFD = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象，避免误判为闭合。"""
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


def dependency_paths() -> list[Path]:
    """返回本层依赖证书。"""
    return [
        TERMINAL_NEW_JOINT_CERT,
        ROW_LEVEL_CERT,
        FIXED_POINT_CERT,
        SEED_CYCLE_GUARD_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def signed_side_gate_after_sync() -> str:
    """给出 row-level fixed-point 切断后的 mandatory signed 侧门。"""
    return f"{NONCIRCULAR_KERNEL} AND {SIGNED_SURVIVAL} AND {ROW_MASS}"


def constructor_basis_after_sync() -> str:
    """给出本层同步后的 constructor 保留基。"""
    return (
        f"{SEED} AND ({PDEC_SCOPE} OR ({signed_side_gate_after_sync()})) "
        f"AND {HARMONIC} AND {SKELETON} AND {DSTRUCTURE}"
    )


def retained_parallel_basis() -> str:
    """给出本层同步后的完整保留基。"""
    return (
        f"{constructor_basis_after_sync()} AND {RATE} AND {JOINT_ROWS} AND "
        f"{JOINT_IDENTITY} AND {JOINT_RETURN} AND {SOURCE_EXACTUV} AND "
        f"{COMPLETE_KEY} AND {FIXED_KEY}"
    )


def sync_chain() -> list[str]:
    """列出从 latest constructor row-level 口到 noncircular kernel 的同步链。"""
    return [
        ROW_LEVEL,
        SEED_EMITTER,
        "signed source spine",
        "basis word / coordinate / assignment / origin identity cycle",
        ROW_LEVEL,
        "fixed point rejected as proof",
        NONCIRCULAR_KERNEL,
    ]


def build_rows(
    latest: dict[str, Any],
    row_level: dict[str, Any],
    fixed_point: dict[str, Any],
    seed_guard: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest constructor row-level fixed-point 同步判定表。"""
    latest_row_level_active = (
        latest.get("next_primary_attack_target") == ROW_LEVEL
        and latest.get("new_joint_coarse_artifact_removed") is True
    )
    row_table_to_emitter = (
        row_level.get("next_direct_attack_target") == SEED_EMITTER
        and row_level.get("row_level_origin_generation_table_router_closed") is True
    )
    fixed_point_cut = (
        fixed_point.get("current_internal_route_is_signed_source_fixed_point") is True
        and fixed_point.get("next_direct_attack_target") == NONCIRCULAR_KERNEL
    )
    seed_cycle_guarded = (
        seed_guard.get("seed_coordinate_source_cycle_detected") is True
        and seed_guard.get("raw_cycle_counts_as_closure") is False
    )
    coarse_row_level_removed = (
        latest_row_level_active and row_table_to_emitter and fixed_point_cut and seed_cycle_guarded
    )

    return [
        row(
            "LatestConstructorRowLevelTargetImported",
            latest_row_level_active,
            False,
            "上一层 terminal new-joint macrocycle cut 已把 constructor 内部主攻压到 row-level clean-core 表。",
            ROW_LEVEL,
        ),
        row(
            "RowTableToSeedEmitterImported",
            row_table_to_emitter,
            False,
            "strict row-level 证书要求该表由无环 pre-Cauchy seed signed-row emitter 正向产生。",
            SEED_EMITTER,
        ),
        row(
            "SignedSourceFixedPointCutImported",
            fixed_point_cut,
            True,
            "row table、seed/emitter、basis word、assignment、value map 与 origin identity 当前会回到同一 row table。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "SeedCoordinateSourceCycleGuardImported",
            seed_cycle_guarded,
            True,
            "seed 坐标-来源链已登记为闭环；没有独立 primitive basis/coefficient source 时不能作为证明。",
            f"{SEED_CYCLE_CUT} OR {TERMINAL_WFD}",
        ),
        row(
            "ReversePaymentAndZeroRowRecoveryStillBlocked",
            fixed_point.get("reverse_and_zero_row_recovery_blocked") is True,
            True,
            "payment 反推、来源环和早期零行 unsigned cover 均不能恢复 signed coefficient source。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "RowLevelCoarseTargetRemoved",
            coarse_row_level_removed,
            False,
            "latest constructor 前沿不再停在 row-level 表名；删除固定点后必须提交非循环 signed emission kernel。",
            signed_side_gate_after_sync(),
        ),
        row(
            "NoncircularSignedEmissionKernelCurrentCorpusProved",
            False,
            False,
            "当前材料没有不读取 row-level 表、来源恒等式、payment/Phi 下游或零行覆盖的 Cauchy 前 signed coefficient 发射核。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "SignedSurvivalAndRowMassStillParallel",
            True,
            False,
            "kernel 只解决 signed coefficient 来源；非零 signed survival 与 same-formal-unit row-mass/no-heavy-row 仍需独立支付。",
            f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "PDECScopeAndTerminalExitsStillParallel",
            True,
            False,
            "同集 PDEC scope、canonical lock、independent bridge、terminal WFD、direct pointwise table 与外部谱输入仍作为并行出口保留。",
            (
                f"{PDEC_SCOPE} OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR "
                f"{TERMINAL_WFD} OR {POINTWISE_TABLE} OR {EXTERNAL_DIBFI}"
            ),
        ),
        row(
            "TailAndConstructorSiblingFieldsStillParallel",
            True,
            False,
            "本层不证明 harmonic/skeleton、ExactUV/source entropy、complete/fixed key、joint rows、Rate 或 DStructure。",
            (
                f"{HARMONIC} AND {SKELETON} AND {SOURCE_EXACTUV} AND {COMPLETE_KEY} "
                f"AND {FIXED_KEY} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND "
                f"{JOINT_RETURN} AND {RATE} AND {DSTRUCTURE}"
            ),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只切断 row-level signed-source fixed point，没有给出无条件全局矛盾。",
            retained_parallel_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json(TERMINAL_NEW_JOINT_CERT)
    row_level = load_json(ROW_LEVEL_CERT)
    fixed_point = load_json(FIXED_POINT_CERT)
    seed_guard = load_json(SEED_CYCLE_GUARD_CERT)
    rows = build_rows(latest, row_level, fixed_point, seed_guard)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_row_level_signed_source_fixed_point_sync_router",
        "status": "phi_lpf_latest_constructor_row_level_fixed_point_cut_to_noncircular_signed_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_constructor_row_level_target_imported": rows[0]["closed"],
        "row_table_to_seed_emitter_imported": rows[1]["closed"],
        "signed_source_fixed_point_cut_imported": rows[2]["closed"],
        "seed_coordinate_source_cycle_guard_imported": rows[3]["closed"],
        "reverse_payment_and_zero_row_recovery_blocked": rows[4]["closed"],
        "row_level_coarse_target_removed": rows[5]["closed"],
        "row_level_clean_core_origin_generation_table_proved": False,
        "noncircular_signed_coefficient_emission_kernel_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "tail_harmonic_upper_0850_proved": False,
        "tail_skeleton_lower_401_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": ROW_LEVEL,
        "absorbed_to": constructor_basis_after_sync(),
        "next_primary_attack_target": NONCIRCULAR_KERNEL,
        "terminal_return_if_no_kernel": TERMINAL_FAMILY,
        "conditional_scope_or_external_target_retained": f"{PDEC_SCOPE} OR {EXTERNAL_DIBFI}",
        "parallel_attack_targets": [
            SEED,
            SIGNED_SURVIVAL,
            ROW_MASS,
            PDEC_SCOPE,
            CANONICAL_LOCK,
            INDEPENDENT_BRIDGE,
            TERMINAL_WFD,
            POINTWISE_TABLE,
            HARMONIC,
            SKELETON,
            DSTRUCTURE,
            RATE,
            JOINT_ROWS,
            JOINT_IDENTITY,
            JOINT_RETURN,
            SOURCE_EXACTUV,
            COMPLETE_KEY,
            FIXED_KEY,
        ],
        "latest_retained_basis_after_router": retained_parallel_basis(),
        "sync_chain": sync_chain(),
        "kernel_contract": fixed_point.get("kernel_contract", []),
        "seed_cycle_guard_target": seed_guard.get("next_direct_attack_target"),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor terminal new-joint cut 后留下的 "
            "`RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands` "
            "接入 strict row-level 与 signed-source fixed-point 证书。row-level 表若要成立，必须由无环 "
            "pre-Cauchy seed signed-row emitter 产生；但现有内部展开沿 basis word、coordinate、assignment、"
            "value map 与 origin identity 又回到同一 row-level 表。seed coordinate/source guard 也确认该环不能"
            "作为证明。因此本层删除 row-level 粗口，把 latest constructor 主攻同步为 "
            "`NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows`，同时继续保留 "
            "signed survival、row-mass/no-heavy-row、PDEC scope、ExactUV/key、harmonic/skeleton、Rate、"
            "DStructure 与 constructor 兄弟字段。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor row-level signed-source fixed-point sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_row_level_target_imported={fmt_bool(result['latest_constructor_row_level_target_imported'])}",
        f"row_table_to_seed_emitter_imported={fmt_bool(result['row_table_to_seed_emitter_imported'])}",
        f"signed_source_fixed_point_cut_imported={fmt_bool(result['signed_source_fixed_point_cut_imported'])}",
        f"seed_coordinate_source_cycle_guard_imported={fmt_bool(result['seed_coordinate_source_cycle_guard_imported'])}",
        f"reverse_payment_and_zero_row_recovery_blocked={fmt_bool(result['reverse_payment_and_zero_row_recovery_blocked'])}",
        f"row_level_coarse_target_removed={fmt_bool(result['row_level_coarse_target_removed'])}",
        f"row_level_clean_core_origin_generation_table_proved={fmt_bool(result['row_level_clean_core_origin_generation_table_proved'])}",
        f"noncircular_signed_coefficient_emission_kernel_proved={fmt_bool(result['noncircular_signed_coefficient_emission_kernel_proved'])}",
        f"nonzero_signed_row_survival_proved={fmt_bool(result['nonzero_signed_row_survival_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(result['same_formal_unit_row_mass_normalization_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
    ]
    lines.extend(result["sync_chain"])
    lines.extend(
        [
            "```",
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
            "## 3. noncircular kernel 合同",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["kernel_contract"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 4. 最新保留基",
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
            "条件性 scope/外部输入仍保留：",
            "",
            "```text",
            result["conditional_scope_or_external_target_retained"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
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
