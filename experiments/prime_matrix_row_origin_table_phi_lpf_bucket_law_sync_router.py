#!/usr/bin/env python3
"""生成 row-level origin table 到 Phi-LPF bucket signed law 的同步证书。

用法示例：
  python3 experiments/prime_matrix_row_origin_table_phi_lpf_bucket_law_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json

输出：
  data/prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-ledger.json
  docs/monograph/prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json
  docs/monograph/prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-row-origin-table-phi-lpf-bucket-law-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SIGNED_SURVIVAL_ORIGIN_CERT = DOCS / "prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json"
ROW_LEVEL_CERT = DOCS / "prime-matrix-strict-row-level-origin-generation-table-router.json"
FIXED_POINT_CERT = DOCS / "prime-matrix-strict-signed-source-fixed-point-breaker-router.json"
NONCIRCULAR_KERNEL_CERT = DOCS / "prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json"
SUPPORT_STRIPPED_CERT = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
PHI_LPF_CERT = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"
LPF_CANDIDATE_CERT = DOCS / "prime-matrix-lpf-candidate-row-map-alpha-rule-router.json"

ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SEED_EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
NONCIRCULAR_KERNEL = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
PHI_SUPPORT = "PhiLPFPrimitiveRowSupportAndCapacityLedger"
SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
JOINT_EMITTER = "AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；文件缺失时返回空对象，不能把缺失当成证明。"""
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


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        SIGNED_SURVIVAL_ORIGIN_CERT,
        ROW_LEVEL_CERT,
        FIXED_POINT_CERT,
        NONCIRCULAR_KERNEL_CERT,
        SUPPORT_STRIPPED_CERT,
        PHI_LPF_CERT,
        LPF_CANDIDATE_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出本层从 row table 到 Phi-LPF signed law 的同步链。"""
    return [
        {
            "from": ROW_TABLE,
            "to": SEED_EMITTER,
            "meaning": "逐行 clean-core 原始生成表必须由 Cauchy 前 seed signed-row emitter 正向产生。",
        },
        {
            "from": SEED_EMITTER,
            "to": NONCIRCULAR_KERNEL,
            "meaning": "signed-source 固定点切断后，emitter 不能从来源环恢复，必须给非循环 signed coefficient 发射核。",
        },
        {
            "from": NONCIRCULAR_KERNEL,
            "to": f"{PHI_SUPPORT} AND {SIGNED_LAW}",
            "meaning": "LPF/Phi 已剥离无符号支撑和容量，剩余是每个 `(p,m)` 桶上的 signed law。",
        },
        {
            "from": PHI_SUPPORT,
            "to": "closed unsigned support/capacity",
            "meaning": "最小素因子桶和 Phi 递推支付 support key、owner layer、capacity 和 p>sqrt(N) 零质量。",
        },
        {
            "from": SIGNED_LAW,
            "to": "latest direct hardpoint",
            "meaning": "必须正向给 signed coefficient、sign/local factor、branch key 与推前前 alpha/delta 求和恒等式。",
        },
    ]


def signed_law_contract() -> list[dict[str, str]]:
    """列出 Phi-LPF 桶级 signed law 必须提交的字段。"""
    return [
        {
            "field": "bucket_key",
            "meaning": "已闭合 LPF/Phi support key `(p,m)`，其中 `p=LPF(pm)` 且 `m` 为 p-rough。",
        },
        {
            "field": "signed_coefficient_formula",
            "meaning": "不读取 payment/origin table 的 Cauchy 前 signed coefficient 正向公式。",
        },
        {
            "field": "sign_local_factor_nonzero",
            "meaning": "符号、local factor、非零条件和零因子命名回流。",
        },
        {
            "field": "alpha_delta_branch_key",
            "meaning": "同步输出 alpha/delta side、branch key 和 exact `(u,v)`。",
        },
        {
            "field": "prepushforward_sum_identity",
            "meaning": "全部桶级 signed rows 在 Phi/payment 推前前已经求和为 actual alpha/delta 贡献。",
        },
        {
            "field": "same_formal_unit_mass_check",
            "meaning": "与 row-mass/no-heavy-row 账本同口径登记，不能由桶容量自动推出。",
        },
    ]


def build_rows(
    signed_survival_origin: dict[str, Any],
    row_level: dict[str, Any],
    fixed_point: dict[str, Any],
    noncircular: dict[str, Any],
    support_stripped: dict[str, Any],
    phi_lpf: dict[str, Any],
    lpf_candidate: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成本层同步判定表。"""
    phi_support_closed = (
        support_stripped.get("phi_lpf_support_bijection_proved") is True
        and support_stripped.get("support_and_capacity_components_closed") is True
        and phi_lpf.get("phi_recursive_lpf_bucket_formula_proved") is True
        and lpf_candidate.get("lpf_candidate_row_emission_map_closed") is True
    )
    return [
        row(
            "RowOriginTableFrontierImported",
            signed_survival_origin.get("next_primary_attack_target") == ROW_TABLE,
            False,
            "上一层已把 Phi-LPF signed-survival 的 signed expression 缺口同步到逐行 clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "RowTableRequiresSeedEmitterImported",
            row_level.get("next_direct_attack_target") == SEED_EMITTER
            and row_level.get("row_level_origin_generation_table_router_closed") is True,
            False,
            "strict row-level 证书说明 row table 必须由无环 pre-Cauchy seed signed-row emitter 产生。",
            SEED_EMITTER,
        ),
        row(
            "SignedSourceFixedPointCutImported",
            fixed_point.get("current_internal_route_is_signed_source_fixed_point") is True,
            True,
            "row-level 表、来源恒等式、basis word 和 signed assignment 构成固定点，不能自证 signed coefficient。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "NoncircularKernelImported",
            noncircular.get("noncircular_kernel_router_closed") is True,
            False,
            "固定点切断后，真正入口是 Cauchy 前 noncircular signed coefficient emission kernel。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "PhiLPFSupportStrippingImported",
            support_stripped.get("next_direct_attack_target") == SIGNED_LAW,
            False,
            "support-stripped 证书已把 noncircular kernel 拆成已闭合 support/capacity 与未闭合 signed law。",
            f"{PHI_SUPPORT} AND {SIGNED_LAW}",
        ),
        row(
            "PhiLPFSupportAndCapacityClosed",
            phi_support_closed,
            True,
            "LPF 唯一 ownership 与 Phi 递推已经支付 `(p,m)` support key、候选容量和 owner layer。",
            PHI_SUPPORT,
        ),
        row(
            "UnsignedBucketCannotEmitSignedLaw",
            phi_support_closed,
            True,
            "LPF/Phi 桶只含无符号支撑和容量，不含 signed coefficient、local factor、orientation 或推前前恒等式。",
            SIGNED_LAW,
        ),
        row(
            "RowOriginTableReducedToPhiLPFBucketSignedLaw",
            phi_support_closed,
            False,
            "逐行 origin table 的找行/数行部分已被 Phi-LPF 剥离；剩余正是桶级 signed coefficient law。",
            SIGNED_LAW,
        ),
        row(
            "PhiLPFBucketSignedLawCurrentCorpusProved",
            False,
            False,
            "当前材料仍没有对每个 `(p,m)` support key 正向赋 signed coefficient 与 sign/local factor。",
            SIGNED_LAW,
        ),
        row(
            "RowMassStillIndependent",
            signed_survival_origin.get("same_formal_unit_row_mass_normalization_proved") is False,
            False,
            "即使 signed law 提交，same-formal-unit row-mass/no-heavy-row 仍需同口径账本。",
            ROW_MASS,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 hardpoint 并剥离 LPF/Phi 无符号部分；不证明 signed law、row mass、complete key、fixed-key multiplicity 或终端排斥。",
            f"{SIGNED_LAW} AND {ROW_MASS}",
        ),
    ]


def support_snapshot(support_stripped: dict[str, Any]) -> list[dict[str, Any]]:
    """取出支撑审计摘要，避免重做数值解释。"""
    samples = support_stripped.get("sample_support_audit", [])
    return [
        {
            "N": item.get("N"),
            "prime_count": item.get("prime_count"),
            "composite_count": item.get("composite_count"),
            "phi_lpf_support_key_count": item.get("phi_lpf_support_key_count"),
            "support_bijection_holds": item.get("support_bijection_holds"),
        }
        for item in samples
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    signed_survival_origin = load_json(SIGNED_SURVIVAL_ORIGIN_CERT)
    row_level = load_json(ROW_LEVEL_CERT)
    fixed_point = load_json(FIXED_POINT_CERT)
    noncircular = load_json(NONCIRCULAR_KERNEL_CERT)
    support_stripped = load_json(SUPPORT_STRIPPED_CERT)
    phi_lpf = load_json(PHI_LPF_CERT)
    lpf_candidate = load_json(LPF_CANDIDATE_CERT)
    rows = build_rows(
        signed_survival_origin=signed_survival_origin,
        row_level=row_level,
        fixed_point=fixed_point,
        noncircular=noncircular,
        support_stripped=support_stripped,
        phi_lpf=phi_lpf,
        lpf_candidate=lpf_candidate,
    )
    retained_basis = (
        f"({SIGNED_LAW} AND {ROW_MASS}) OR {POINTWISE_TABLE} OR {JOINT_EMITTER} "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}; parallel: {COMPLETE_KEY} AND "
        f"{FIXED_KEY_MULT} AND {EXACTUV_PAIR} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_row_origin_table_phi_lpf_bucket_law_sync_router",
        "status": "row_origin_table_reduced_to_phi_lpf_bucket_signed_law_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "row_level_origin_table_imported": rows[0]["closed"],
        "row_table_requires_seed_emitter": rows[1]["closed"],
        "signed_source_fixed_point_cut_imported": rows[2]["closed"],
        "noncircular_kernel_imported": rows[3]["closed"],
        "phi_lpf_support_stripping_imported": rows[4]["closed"],
        "phi_lpf_support_and_capacity_closed": rows[5]["closed"],
        "row_origin_table_reduced_to_phi_lpf_bucket_signed_law": rows[7]["closed"],
        "phi_lpf_bucket_signed_coefficient_law_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_level_clean_core_origin_generation_table_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": ROW_TABLE,
        "hardpoint_after_router": f"{PHI_SUPPORT} AND {SIGNED_LAW}",
        "absorbed_closed_component": PHI_SUPPORT,
        "next_primary_attack_target": SIGNED_LAW,
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "signed_law_contract": signed_law_contract(),
        "support_snapshot": support_snapshot(support_stripped),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新的逐行 clean-core origin table 硬点接入 LPF/Phi 支撑剥离证书。"
            "Row-level 表不能从来源环自证；固定点切断后必须给 noncircular pre-Cauchy signed kernel。"
            "而 LPF/Phi 已经把该 kernel 的无符号支撑、owner layer 与容量全部剥离为 `(p,m)` 桶，"
            "所以最新真正硬点不再是找行或数行，而是 `PhiLPFBucketSignedCoefficientLawBeforePushforward`。"
            "该 signed law 仍未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix row-origin table to Phi-LPF bucket signed-law sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"row_level_origin_table_imported={fmt_bool(cert['row_level_origin_table_imported'])}",
        f"row_table_requires_seed_emitter={fmt_bool(cert['row_table_requires_seed_emitter'])}",
        f"signed_source_fixed_point_cut_imported={fmt_bool(cert['signed_source_fixed_point_cut_imported'])}",
        f"noncircular_kernel_imported={fmt_bool(cert['noncircular_kernel_imported'])}",
        f"phi_lpf_support_stripping_imported={fmt_bool(cert['phi_lpf_support_stripping_imported'])}",
        f"phi_lpf_support_and_capacity_closed={fmt_bool(cert['phi_lpf_support_and_capacity_closed'])}",
        f"row_origin_table_reduced_to_phi_lpf_bucket_signed_law={fmt_bool(cert['row_origin_table_reduced_to_phi_lpf_bucket_signed_law'])}",
        f"phi_lpf_bucket_signed_coefficient_law_proved={fmt_bool(cert['phi_lpf_bucket_signed_coefficient_law_proved'])}",
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
            "## 2. LPF/Phi 支撑快照",
            "",
            "| N | pi(N) | composites | support keys | bijection |",
            "| ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in cert["support_snapshot"]:
        lines.append(
            f"| {item['N']} | {item['prime_count']} | {item['composite_count']} | "
            f"{item['phi_lpf_support_key_count']} | `{fmt_bool(item['support_bijection_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 桶级 signed law 合同",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in cert["signed_law_contract"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 最新保留基",
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
            "行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
