#!/usr/bin/env python3
"""生成 latest constructor Kuznetsov/high-model 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_kuznetsov_high_model_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_HIGH_MODEL_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync-router.json"
)
STRICT_KUZNETSOV_ATOM_CERT = DOCS / "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json"
STRICT_HIGH_MODEL_TAIL_CERT = DOCS / "prime-matrix-strict-high-model-tail-update-router.json"
OLD_CONSTRUCTOR_KZ_CYCLE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync-router.json"
)

KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
NCBLK_ANTIATOM = "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
NONRECURSIVE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
BETA_APPENDIX = "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix"
BETA_99 = "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000"
SAWTOOTH = "ExactResidueWeightedFloorSawtoothTenPercentBound"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
SOURCE_EXACTUV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"


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
        CURRENT_HIGH_MODEL_REBASE_CERT,
        STRICT_KUZNETSOV_ATOM_CERT,
        STRICT_HIGH_MODEL_TAIL_CERT,
        OLD_CONSTRUCTOR_KZ_CYCLE_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def tail_package() -> str:
    """给出高段模型余量尾段自足包。"""
    return f"{BETA_APPENDIX} AND {BETA_99} AND {SAWTOOTH}"


def refined_pair() -> str:
    """给出 KZ/high-model 对同步后的前沿。"""
    return f"{NCBLK_ANTIATOM} AND {tail_package()}"


def retained_basis() -> str:
    """给出 constructor 语境下的最新保留基。"""
    return (
        f"(({NCBLK_ANTIATOM} OR {SEED} AND {TERMINAL_FAMILY} OR {NONRECURSIVE_BREAKER} "
        f"OR {NEW_JOINT} OR {PDEC_SCOPE}) AND {tail_package()}) "
        f"AND {DSTRUCTURE} AND {RATE} AND {JOINT_ROWS} AND {JOINT_IDENTITY} "
        f"AND {JOINT_RETURN} AND {SOURCE_EXACTUV} AND {SIGNED_SURVIVAL} "
        f"AND {ROW_MASS} AND {COMPLETE_KEY} AND {FIXED_KEY}"
    )


def build_rows(
    current: dict[str, Any],
    kuz: dict[str, Any],
    high_tail: dict[str, Any],
    old_kz: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 Kuznetsov/high-model rebase 判定表。"""
    current_pair_active = (
        current.get("next_direct_attack_target") == f"{KUZNETSOV_DLS} AND {HIGH_MODEL}"
        and current.get("wide_terminal_model_pair_removed") is True
    )
    kuz_atom_reduced = (
        kuz.get("terminal_gap_before_router") == KUZNETSOV_DLS
        and kuz.get("kz_a_smoothing_closed") is True
        and kuz.get("kz_b_trace_specialization_closed") is True
        and kuz.get("kz_c_bessel_decay_closed") is True
        and kuz.get("kz_d_spectral_large_sieve_closed") is True
        and kuz.get("kz_e_reduced_to_ncblk_or_external") is True
    )
    old_constructor_cycle = old_kz.get("constructor_kuznetsov_independent_exit_removed") is True
    high_tail_reduced = (
        high_tail.get("strict_high_model_tail_boundary_closed") is True
        and high_tail.get("terminal_gap_after_router") == tail_package()
    )
    beta_open = high_tail.get("self_contained_beta_sieve_appendix_proved") is False
    beta99_open = high_tail.get("beta_sieve_main_coefficient_99_proved") is False
    saw_open = high_tail.get("exact_residue_weighted_floor_sawtooth_bound_proved") is False
    rebase_removed = current_pair_active and kuz_atom_reduced and high_tail_reduced
    return [
        row(
            "LatestConstructorKuznetsovHighModelPairImported",
            current_pair_active,
            False,
            "上一层已把直接主攻钉到自足 Kuznetsov/DLS 大筛与高段模型余量。",
            f"{KUZNETSOV_DLS} AND {HIGH_MODEL}",
        ),
        row(
            "StrictKuznetsovABCDSpineImported",
            kuz_atom_reduced,
            True,
            "KZ-A/B/C/D 形式谱脊柱已闭合；KZ-E 是唯一剩余谱节省门。",
            "KZ-E well-factorable dispersion log-saving",
        ),
        row(
            "KZERReducedToNCBLKAntiAtom",
            kuz_atom_reduced,
            False,
            "KZ-E 不能由裸谱大筛自动给出；自足剩余压到 acyclic NC-BLK/source anti-atom。",
            NCBLK_ANTIATOM,
        ),
        row(
            "ConstructorKuznetsovCycleImportAgrees",
            old_constructor_cycle,
            False,
            "constructor 专属旧同步也确认 KZ/DLS 不是独立无名出口，会回到终端家族或破环包。",
            f"{TERMINAL_FAMILY} OR {NONRECURSIVE_BREAKER} OR {NEW_JOINT}",
        ),
        row(
            "StrictHighModelTailUpdateImported",
            high_tail_reduced,
            True,
            "高段模型余量已压到自足 beta-sieve 权重、99% 主系数误差和 exact sawtooth 余项界。",
            tail_package(),
        ),
        row(
            "SelfContainedBetaSieveAppendixStillOpen",
            not beta_open,
            not beta_open,
            "严格自足 Rosser-Iwaniec lower weights 构造仍未证明。",
            BETA_APPENDIX,
        ),
        row(
            "BetaSieveMainCoefficient99StillOpen",
            not beta99_open,
            not beta99_open,
            "alpha=0.43, P>=100000 的 99% 主系数显式误差仍未证明。",
            BETA_99,
        ),
        row(
            "ExactSawtoothTenPercentStillOpen",
            not saw_open,
            not saw_open,
            "权重固定后的 CRT residue-weighted floor/sawtooth 余项界仍未证明。",
            SAWTOOTH,
        ),
        row(
            "KuznetsovHighModelWidePairRemoved",
            rebase_removed,
            False,
            "KZ/high-model 宽对已被替换为 NC-BLK/source anti-atom 与 beta-sieve/sawtooth 尾段包。",
            refined_pair(),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只做非循环前沿精炼；未证明谱节省、beta-sieve、sawtooth 或三命题无条件闭合。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    current = load_json(CURRENT_HIGH_MODEL_REBASE_CERT)
    kuz = load_json(STRICT_KUZNETSOV_ATOM_CERT)
    high_tail = load_json(STRICT_HIGH_MODEL_TAIL_CERT)
    old_kz = load_json(OLD_CONSTRUCTOR_KZ_CYCLE_CERT)
    rows = build_rows(current, kuz, high_tail, old_kz)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_kuznetsov_high_model_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_kuznetsov_high_model_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_constructor_kuznetsov_high_model_pair_imported": rows[0]["closed"],
        "strict_kuznetsov_abcd_spine_imported": rows[1]["closed"],
        "kze_reduced_to_ncblk_antiatom": rows[2]["closed"],
        "constructor_kuznetsov_cycle_import_agrees": rows[3]["closed"],
        "strict_high_model_tail_update_imported": rows[4]["closed"],
        "kuznetsov_high_model_wide_pair_removed": rows[8]["closed"],
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "acyclic_ncblk_actual_block_nonconcentration_proved": False,
        "acyclic_strengthened_source_antiatom_proved": False,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": f"{KUZNETSOV_DLS} AND {HIGH_MODEL}",
        "absorbed_to": refined_pair(),
        "next_primary_attack_target": NCBLK_ANTIATOM,
        "next_direct_attack_target": f"{NCBLK_ANTIATOM} AND {BETA_APPENDIX}_THEN_ExactSawtooth",
        "parallel_attack_targets": [
            PDEC_SCOPE,
            TERMINAL_FAMILY,
            NONRECURSIVE_BREAKER,
            NEW_JOINT,
            BETA_APPENDIX,
            BETA_99,
            SAWTOOTH,
            DSTRUCTURE,
            RATE,
            JOINT_ROWS,
            JOINT_IDENTITY,
            JOINT_RETURN,
            SOURCE_EXACTUV,
            SIGNED_SURVIVAL,
            ROW_MASS,
            COMPLETE_KEY,
            FIXED_KEY,
        ],
        "latest_retained_basis_after_router": retained_basis(),
        "structural_chain": [
            f"{KUZNETSOV_DLS} AND {HIGH_MODEL}",
            f"{NCBLK_ANTIATOM} AND ({BETA_APPENDIX} AND {BETA_99} AND {SAWTOOTH})",
            "external KLS/DIBFI and standard beta-sieve imports remain conditional only",
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor 的 `SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks "
            "AND HighSegmentModelGapAlpha043C3AnalyticLedger` 接入 KZ-A--E 原子路由与高段模型尾段更新。"
            "KZ/DLS 不再作为独立无名出口，高段模型也不再停在单一黑箱；剩余是 acyclic NC-BLK/source "
            "anti-atom 与自足 beta-sieve/sawtooth 尾段包。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor Kuznetsov/high-model rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_kuznetsov_high_model_pair_imported={fmt_bool(result['latest_constructor_kuznetsov_high_model_pair_imported'])}",
        f"strict_kuznetsov_abcd_spine_imported={fmt_bool(result['strict_kuznetsov_abcd_spine_imported'])}",
        f"kze_reduced_to_ncblk_antiatom={fmt_bool(result['kze_reduced_to_ncblk_antiatom'])}",
        f"constructor_kuznetsov_cycle_import_agrees={fmt_bool(result['constructor_kuznetsov_cycle_import_agrees'])}",
        f"strict_high_model_tail_update_imported={fmt_bool(result['strict_high_model_tail_update_imported'])}",
        f"kuznetsov_high_model_wide_pair_removed={fmt_bool(result['kuznetsov_high_model_wide_pair_removed'])}",
        f"self_contained_kuznetsov_dls_large_sieve_inequality_proved={fmt_bool(result['self_contained_kuznetsov_dls_large_sieve_inequality_proved'])}",
        f"acyclic_ncblk_actual_block_nonconcentration_proved={fmt_bool(result['acyclic_ncblk_actual_block_nonconcentration_proved'])}",
        f"self_contained_beta_sieve_appendix_proved={fmt_bool(result['self_contained_beta_sieve_appendix_proved'])}",
        f"beta_sieve_main_coefficient_99_proved={fmt_bool(result['beta_sieve_main_coefficient_99_proved'])}",
        f"exact_residue_weighted_floor_sawtooth_bound_proved={fmt_bool(result['exact_residue_weighted_floor_sawtooth_bound_proved'])}",
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
            "## 3. 最新保留基",
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
            "并行仍需：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
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
