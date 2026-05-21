#!/usr/bin/env python3
"""生成 latest constructor post-KZ-E source-admission rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_post_kze_source_admission_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-kze-source-admission-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-post-kze-source-admission-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-kze-source-admission-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-kze-source-admission-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-post-kze-source-admission-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_LATEST_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync-router.json"
)
STRICT_NCBLK_FRONTIER_CERT = DOCS / "prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json"
STRICT_FORWARD_ROOT_CERT = DOCS / "prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json"
STRICT_POST_PDEC_CERT = DOCS / "prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json"
STRICT_POST_NEW_JOINT_CERT = DOCS / "prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json"
STRICT_KZ_NOCYCLE_CERT = DOCS / "prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json"
STRICT_POST_KZE_CERT = DOCS / "prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json"
STRICT_HIGH_TAIL_CERT = DOCS / "prime-matrix-strict-high-model-tail-update-router.json"
PHI_LPF_SIGNED_LAW_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-router.json"
)

NCBLK_ANTIATOM = "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"
FORWARD_SOURCE_ROOT = "ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
NONCIRCULAR_KZ = "NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse"
KZE_DIRECT = "AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection"
SOURCE_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
EXTERNAL_KZ = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
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
PHI_LPF_SIGNED_TABLE = "PhiLPFBucketSignedCoefficientLawBeforePushforward"


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
        CURRENT_LATEST_CERT,
        STRICT_NCBLK_FRONTIER_CERT,
        STRICT_FORWARD_ROOT_CERT,
        STRICT_POST_PDEC_CERT,
        STRICT_POST_NEW_JOINT_CERT,
        STRICT_KZ_NOCYCLE_CERT,
        STRICT_POST_KZE_CERT,
        STRICT_HIGH_TAIL_CERT,
        PHI_LPF_SIGNED_LAW_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def tail_package() -> str:
    """给出高段模型余量的严格自足尾包。"""
    return f"{BETA_APPENDIX} AND {BETA_99} AND {SAWTOOTH}"


def latest_internal_basis() -> str:
    """给出当前内部非循环基。"""
    return f"{SOURCE_ADMISSION} AND {tail_package()} AND {RATE} AND {DSTRUCTURE}"


def retained_basis() -> str:
    """给出保留条件线后的 latest constructor 基。"""
    alternatives = (
        f"{SOURCE_ADMISSION} OR {EXTERNAL_KZ} OR {PDEC_SCOPE} OR {NEW_JOINT} "
        f"OR {KZE_DIRECT} OR {NONCIRCULAR_KZ} OR {PHI_LPF_SIGNED_TABLE}"
    )
    return (
        f"(({alternatives}) AND {tail_package()}) AND {RATE} AND {DSTRUCTURE} "
        f"AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN} "
        f"AND {SOURCE_EXACTUV} AND {SIGNED_SURVIVAL} AND {ROW_MASS} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY}"
    )


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 post-KZ-E/source-admission rebase 判定表。"""
    current = data["current"]
    ncblk = data["ncblk"]
    forward = data["forward"]
    post_pdec = data["post_pdec"]
    post_joint = data["post_joint"]
    kz_nocycle = data["kz_nocycle"]
    post_kze = data["post_kze"]
    high_tail = data["high_tail"]
    phi_signed = data["phi_signed"]

    latest_ncblk_tail = (
        current.get("next_primary_attack_target") == NCBLK_ANTIATOM
        and current.get("absorbed_to") == f"{NCBLK_ANTIATOM} AND {tail_package()}"
    )
    ncblk_to_source_root = ncblk.get("next_direct_attack_target") == FORWARD_SOURCE_ROOT
    source_root_to_pdec = (
        forward.get("next_direct_attack_target") == PDEC_SCOPE
        and "NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse"
        in str(forward.get("hardpoint_after_router", ""))
    )
    pdec_to_new_joint = post_pdec.get("next_direct_attack_target") == NEW_JOINT
    new_joint_to_kz = post_joint.get("next_direct_attack_target") == NONCIRCULAR_KZ
    kz_to_kze_direct = kz_nocycle.get("next_direct_attack_target") == KZE_DIRECT
    kze_to_admission = post_kze.get("next_direct_attack_target") == SOURCE_ADMISSION
    high_tail_reapplied = high_tail.get("terminal_gap_after_router") == tail_package()
    phi_lpf_unsigned_disciplined = (
        phi_signed.get("phi_lpf_support_and_capacity_closed") is True
        and phi_signed.get("unsigned_phi_lpf_bucket_cannot_emit_signed_coefficient") is True
    )
    chain_rebased = all(
        [
            latest_ncblk_tail,
            ncblk_to_source_root,
            source_root_to_pdec,
            pdec_to_new_joint,
            new_joint_to_kz,
            kz_to_kze_direct,
            kze_to_admission,
            high_tail_reapplied,
        ]
    )

    return [
        row(
            "LatestConstructorNCBLKAndTailImported",
            latest_ncblk_tail,
            False,
            "上一层已把 constructor 的 KZ/high-model 对压成 NCBLK/source anti-atom 与 beta-sieve/sawtooth 尾包。",
            f"{NCBLK_ANTIATOM} AND {tail_package()}",
        ),
        row(
            "NCBLKFrontierToSourceRootImported",
            ncblk_to_source_root,
            False,
            "strict NCBLK/source anti-atom 前沿显示 actual 路线必须先给出 forward source-root packet 或命名回流。",
            FORWARD_SOURCE_ROOT,
        ),
        row(
            "ForwardSourceRootTerminalCycleImported",
            source_root_to_pdec,
            True,
            "当前语料中的 source-root 内部路线回到终端容量环，不能作为非循环闭合。",
            f"{PDEC_SCOPE} OR {NONCIRCULAR_KZ}",
        ),
        row(
            "PostSourceRootPDECSaturationImported",
            pdec_to_new_joint,
            False,
            "direct PDEC 作用域在当前内部材料中已攻到饱和边界，若不新增 PDEC 证书则转入 new-joint 破环口。",
            NEW_JOINT,
        ),
        row(
            "PostPDECNewJointCycleImported",
            new_joint_to_kz,
            False,
            "旧 new-joint/branch-trace/signed-payload 路线回到 signed-lane/source-rank 循环。",
            NONCIRCULAR_KZ,
        ),
        row(
            "PostNewJointKZNoCycleGateImported",
            kz_to_kze_direct,
            False,
            "非循环 KZ/DLS 门禁止复用 NCBLK/source-root，因此旧 KZ-E 投影路线不能计入闭合。",
            KZE_DIRECT,
        ),
        row(
            "PostKZEDirectSourceBridgeImported",
            kze_to_admission,
            False,
            "KZ-E direct no-projection 内部路线若不接受外部 no-projection 定理，就压到 clean A1 分支 canonical source admission。",
            SOURCE_ADMISSION,
        ),
        row(
            "PhiLPFUnsignedBucketDisciplinePreserved",
            phi_lpf_unsigned_disciplined,
            True,
            "LPF/Phi 桶恒等式已支付 owner、支撑与容量；它不能从无符号 bucket 反推出 signed source。",
            f"{SOURCE_ADMISSION} OR {PHI_LPF_SIGNED_TABLE}",
        ),
        row(
            "HighModelTailReappliedAfterKZEBridge",
            high_tail_reapplied,
            True,
            "source-admission 只处理 KZ-E/no-cycle 侧；高段模型仍必须支付 beta-sieve、99% 主系数和 sawtooth 尾包。",
            tail_package(),
        ),
        row(
            "LatestInternalRouteReducedToA1SourceAdmission",
            chain_rebased,
            False,
            "latest constructor 的当前内部非循环链已重接到 A1 clean branch canonical source admission 加高段尾包。",
            latest_internal_basis(),
        ),
        row(
            "A1SourceAdmissionStillOpen",
            True,
            False,
            "canonical 分支来源锁只在证明当前 clean A1 反例分支准入 RIW/Buchstab source 后可用；当前尚未证明。",
            SOURCE_ADMISSION,
        ),
        row(
            "StrictBetaSieveSawtoothTailStillOpen",
            True,
            False,
            "自足 beta-sieve 附录、99% 主系数误差与 exact sawtooth 余项界仍未证明。",
            tail_package(),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只做 latest constructor 的非循环链 rebase；没有证明 source admission、beta-sieve/sawtooth、Rate 或 DStructure。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "current": load_json(CURRENT_LATEST_CERT),
        "ncblk": load_json(STRICT_NCBLK_FRONTIER_CERT),
        "forward": load_json(STRICT_FORWARD_ROOT_CERT),
        "post_pdec": load_json(STRICT_POST_PDEC_CERT),
        "post_joint": load_json(STRICT_POST_NEW_JOINT_CERT),
        "kz_nocycle": load_json(STRICT_KZ_NOCYCLE_CERT),
        "post_kze": load_json(STRICT_POST_KZE_CERT),
        "high_tail": load_json(STRICT_HIGH_TAIL_CERT),
        "phi_signed": load_json(PHI_LPF_SIGNED_LAW_CERT),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_post_kze_source_admission_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_post_kze_source_admission_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_constructor_ncblk_tail_imported": rows[0]["closed"],
        "strict_ncblk_to_source_root_imported": rows[1]["closed"],
        "forward_source_root_terminal_cycle_imported": rows[2]["closed"],
        "post_source_root_pdec_saturation_imported": rows[3]["closed"],
        "post_pdec_new_joint_noncycle_imported": rows[4]["closed"],
        "post_new_joint_kz_nocycle_imported": rows[5]["closed"],
        "post_kze_source_admission_imported": rows[6]["closed"],
        "phi_lpf_unsigned_bucket_discipline_preserved": rows[7]["closed"],
        "high_model_tail_beta_sawtooth_reapplied": rows[8]["closed"],
        "latest_internal_route_reduced_to_a1_source_admission": rows[9]["closed"],
        "a1_clean_branch_canonical_source_admission_proved": False,
        "exact_external_dibfi_kuznetsov_no_projection_certificate_accepted": False,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": data["current"].get("absorbed_to", ""),
        "absorbed_to": f"{SOURCE_ADMISSION} AND {tail_package()}",
        "latest_internal_basis_after_router": latest_internal_basis(),
        "latest_retained_basis_after_router": retained_basis(),
        "next_primary_attack_target": SOURCE_ADMISSION,
        "next_direct_attack_target": f"{SOURCE_ADMISSION} AND {BETA_APPENDIX}_THEN_ExactSawtooth",
        "parallel_attack_targets": [
            EXTERNAL_KZ,
            PDEC_SCOPE,
            NEW_JOINT,
            KZE_DIRECT,
            NONCIRCULAR_KZ,
            PHI_LPF_SIGNED_TABLE,
            BETA_APPENDIX,
            BETA_99,
            SAWTOOTH,
            RATE,
            DSTRUCTURE,
            JOINT_ROWS,
            JOINT_IDENTITY,
            JOINT_RETURN,
            SOURCE_EXACTUV,
            SIGNED_SURVIVAL,
            ROW_MASS,
            COMPLETE_KEY,
            FIXED_KEY,
        ],
        "structural_chain": [
            f"{NCBLK_ANTIATOM} AND {tail_package()}",
            f"{FORWARD_SOURCE_ROOT} OR named terminal return",
            f"{PDEC_SCOPE} OR {NONCIRCULAR_KZ}",
            f"{NEW_JOINT} OR {NONCIRCULAR_KZ}",
            NONCIRCULAR_KZ,
            KZE_DIRECT,
            f"{SOURCE_ADMISSION} AND {tail_package()}",
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor 的 NCBLK/source anti-atom 与 beta-sieve/sawtooth 尾包继续接入 "
            "strict source-root、PDEC、new-joint、KZ no-cycle 和 post-KZ-E direct source-bridge 链。"
            "LPF/Phi 桶恒等式在这里作为无符号 owner/support/capacity 纪律使用：它排除了从 bucket "
            "容量反推 signed source 的捷径。剩余的内部非循环首口是 A1 clean branch canonical source "
            "admission，并且仍需支付自足 beta-sieve、99% 主系数和 exact sawtooth 尾段。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor post-KZ-E source-admission rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_ncblk_tail_imported={fmt_bool(result['latest_constructor_ncblk_tail_imported'])}",
        f"strict_ncblk_to_source_root_imported={fmt_bool(result['strict_ncblk_to_source_root_imported'])}",
        f"forward_source_root_terminal_cycle_imported={fmt_bool(result['forward_source_root_terminal_cycle_imported'])}",
        f"post_source_root_pdec_saturation_imported={fmt_bool(result['post_source_root_pdec_saturation_imported'])}",
        f"post_pdec_new_joint_noncycle_imported={fmt_bool(result['post_pdec_new_joint_noncycle_imported'])}",
        f"post_new_joint_kz_nocycle_imported={fmt_bool(result['post_new_joint_kz_nocycle_imported'])}",
        f"post_kze_source_admission_imported={fmt_bool(result['post_kze_source_admission_imported'])}",
        f"phi_lpf_unsigned_bucket_discipline_preserved={fmt_bool(result['phi_lpf_unsigned_bucket_discipline_preserved'])}",
        f"high_model_tail_beta_sawtooth_reapplied={fmt_bool(result['high_model_tail_beta_sawtooth_reapplied'])}",
        f"latest_internal_route_reduced_to_a1_source_admission={fmt_bool(result['latest_internal_route_reduced_to_a1_source_admission'])}",
        f"a1_clean_branch_canonical_source_admission_proved={fmt_bool(result['a1_clean_branch_canonical_source_admission_proved'])}",
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
