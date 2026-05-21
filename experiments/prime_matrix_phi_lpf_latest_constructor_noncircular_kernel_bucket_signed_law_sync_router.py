#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor noncircular kernel 到 bucket signed law 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_noncircular_kernel_bucket_signed_law_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_ROW_FIXED_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.json"
)
STRICT_KERNEL_CERT = DOCS / "prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json"
SUPPORT_STRIPPED_CERT = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
PHI_LPF_CERT = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"
LPF_CANDIDATE_CERT = DOCS / "prime-matrix-lpf-candidate-row-map-alpha-rule-router.json"

SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
NONCIRCULAR_KERNEL = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
PRECAUCHY_DECL = "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
PHI_SUPPORT = "PhiLPFPrimitiveRowSupportAndCapacityLedger"
SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
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


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象，不能把缺失当作证明。"""
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
        LATEST_ROW_FIXED_CERT,
        STRICT_KERNEL_CERT,
        SUPPORT_STRIPPED_CERT,
        PHI_LPF_CERT,
        LPF_CANDIDATE_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def signed_side_gate_after_sync() -> str:
    """给出 Phi-LPF 支撑剥离后的 mandatory signed 侧门。"""
    return f"{SIGNED_LAW} AND {SIGNED_SURVIVAL} AND {ROW_MASS}"


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
    """列出从 latest constructor kernel 到 bucket signed law 的同步链。"""
    return [
        NONCIRCULAR_KERNEL,
        PRECAUCHY_DECL,
        f"{PHI_SUPPORT} AND {SIGNED_LAW}",
        "LPF/Phi support and capacity stripped off",
        SIGNED_LAW,
    ]


def support_samples(support: dict[str, Any]) -> list[dict[str, Any]]:
    """读取既有支撑审计样本。"""
    samples = support.get("sample_support_audit", [])
    return samples if isinstance(samples, list) else []


def signed_law_fields(support: dict[str, Any]) -> list[dict[str, str]]:
    """读取既有 signed law 字段合同。"""
    fields = support.get("signed_law_fields", [])
    return fields if isinstance(fields, list) else []


def build_rows(
    latest: dict[str, Any],
    strict_kernel: dict[str, Any],
    support: dict[str, Any],
    phi: dict[str, Any],
    lpf_candidate: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest constructor kernel bucket-law 同步判定表。"""
    latest_kernel_active = (
        latest.get("next_primary_attack_target") == NONCIRCULAR_KERNEL
        and latest.get("row_level_coarse_target_removed") is True
    )
    strict_kernel_imported = (
        strict_kernel.get("noncircular_kernel_router_closed") is True
        and strict_kernel.get("next_direct_attack_target") == PRECAUCHY_DECL
    )
    support_stripping_imported = (
        support.get("hardpoint_before_router") == NONCIRCULAR_KERNEL
        and support.get("next_direct_attack_target") == SIGNED_LAW
    )
    phi_lpf_capacity_closed = (
        support.get("support_and_capacity_components_closed") is True
        and support.get("phi_lpf_support_bijection_proved") is True
        and phi.get("prime_count_identity_from_phi_lpf_proved") is True
        and lpf_candidate.get("lpf_candidate_row_emission_map_closed") is True
    )
    kernel_coarse_removed = (
        latest_kernel_active and strict_kernel_imported and support_stripping_imported and phi_lpf_capacity_closed
    )

    return [
        row(
            "LatestConstructorNoncircularKernelTargetImported",
            latest_kernel_active,
            False,
            "上一层 row-level fixed-point cut 已把 latest constructor 主攻压到非循环 signed emission kernel。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "StrictKernelFirstFieldImported",
            strict_kernel_imported,
            False,
            "strict kernel 路由把合法 kernel 的首字段钉到 Cauchy 前 actual noncanonical emitter declaration line。",
            PRECAUCHY_DECL,
        ),
        row(
            "PhiLPFSupportStrippingImported",
            support_stripping_imported,
            False,
            "既有 support-stripped 证书把 noncircular kernel 拆成已闭合 LPF/Phi 支撑容量与未闭合 bucket signed law。",
            f"{PHI_SUPPORT} AND {SIGNED_LAW}",
        ),
        row(
            "PhiLPFSupportAndCapacityClosed",
            phi_lpf_capacity_closed,
            True,
            "LPF 唯一 owner、Phi 递推、candidate row map 与 p>sqrt(N) 零质量已经支付无符号支撑/容量。",
            PHI_SUPPORT,
        ),
        row(
            "UnsignedPhiLPFBucketCannotEmitSignedCoefficient",
            phi_lpf_capacity_closed,
            True,
            "LPF/Phi 桶只给 `(p,m)` support key 与容量，不给 sign、local factor、branch key 或推前前 signed 求和。",
            SIGNED_LAW,
        ),
        row(
            "NoncircularKernelCoarseTargetRemoved",
            kernel_coarse_removed,
            False,
            "constructor 前沿不再停在 noncircular kernel 口；其找行/容量部分剥离后剩 bucket signed coefficient law。",
            signed_side_gate_after_sync(),
        ),
        row(
            "PhiLPFBucketSignedCoefficientLawCurrentCorpusProved",
            False,
            False,
            "当前材料没有对每个 LPF/Phi support key 正向赋 signed coefficient、非零 local factor 和 prepushforward identity。",
            SIGNED_LAW,
        ),
        row(
            "SignedSurvivalAndRowMassStillParallel",
            True,
            False,
            "bucket signed law 仍不自动给非零 signed survival，也不自动支付 same-formal-unit row-mass/no-heavy-row。",
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
            "本层只把 noncircular kernel 的无符号部分剥离到 LPF/Phi 桶，不证明 signed law 或无条件全局矛盾。",
            retained_parallel_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json(LATEST_ROW_FIXED_CERT)
    strict_kernel = load_json(STRICT_KERNEL_CERT)
    support = load_json(SUPPORT_STRIPPED_CERT)
    phi = load_json(PHI_LPF_CERT)
    lpf_candidate = load_json(LPF_CANDIDATE_CERT)
    rows = build_rows(latest, strict_kernel, support, phi, lpf_candidate)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_noncircular_kernel_bucket_signed_law_sync_router",
        "status": "phi_lpf_latest_constructor_noncircular_kernel_cut_to_bucket_signed_law_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_constructor_noncircular_kernel_target_imported": rows[0]["closed"],
        "strict_kernel_first_field_imported": rows[1]["closed"],
        "phi_lpf_support_stripping_imported": rows[2]["closed"],
        "phi_lpf_support_and_capacity_closed": rows[3]["closed"],
        "unsigned_phi_lpf_bucket_cannot_emit_signed_coefficient": rows[4]["closed"],
        "noncircular_kernel_coarse_target_removed": rows[5]["closed"],
        "noncircular_signed_coefficient_emission_kernel_proved": False,
        "phi_lpf_bucket_signed_coefficient_law_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "tail_harmonic_upper_0850_proved": False,
        "tail_skeleton_lower_401_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": NONCIRCULAR_KERNEL,
        "absorbed_to": constructor_basis_after_sync(),
        "next_primary_attack_target": SIGNED_LAW,
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
        "signed_law_fields": signed_law_fields(support),
        "sample_support_audit": support_samples(support),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor 的非循环 signed emission kernel 接入 Phi-LPF 支撑剥离证书。"
            "strict kernel 纪律要求 Cauchy 前声明且不得读取 downstream payment/Phi、row table 或零行覆盖；"
            "LPF/Phi 层已经用最小素因子 owner 与 Phi 递推支付 `(p,m)` support key、候选行容量和大素数零质量。"
            "因此 constructor 主攻不再是找行、数行或支撑容量，而是对每个 Phi-LPF bucket 正向给出 "
            "`PhiLPFBucketSignedCoefficientLawBeforePushforward`。该 signed law、signed survival、row-mass、"
            "PDEC scope、ExactUV/key、harmonic/skeleton、Rate 与 DStructure 仍未证明；行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor noncircular kernel bucket signed-law sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_noncircular_kernel_target_imported={fmt_bool(result['latest_constructor_noncircular_kernel_target_imported'])}",
        f"strict_kernel_first_field_imported={fmt_bool(result['strict_kernel_first_field_imported'])}",
        f"phi_lpf_support_stripping_imported={fmt_bool(result['phi_lpf_support_stripping_imported'])}",
        f"phi_lpf_support_and_capacity_closed={fmt_bool(result['phi_lpf_support_and_capacity_closed'])}",
        f"unsigned_phi_lpf_bucket_cannot_emit_signed_coefficient={fmt_bool(result['unsigned_phi_lpf_bucket_cannot_emit_signed_coefficient'])}",
        f"noncircular_kernel_coarse_target_removed={fmt_bool(result['noncircular_kernel_coarse_target_removed'])}",
        f"noncircular_signed_coefficient_emission_kernel_proved={fmt_bool(result['noncircular_signed_coefficient_emission_kernel_proved'])}",
        f"phi_lpf_bucket_signed_coefficient_law_proved={fmt_bool(result['phi_lpf_bucket_signed_coefficient_law_proved'])}",
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
            "## 2. 支撑样本读数",
            "",
            "| N | pi(N) | composites | support keys | bijection |",
            "| ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["sample_support_audit"]:
        lines.append(
            f"| {item['N']} | {item['prime_count']} | {item['composite_count']} | "
            f"{item['phi_lpf_support_key_count']} | `{fmt_bool(item['support_bijection_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 3. bucket signed law 合同",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["signed_law_fields"]:
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
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 最新保留基",
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
