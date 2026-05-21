#!/usr/bin/env python3
"""生成 latest row-origin table 到 Phi-LPF bucket signed law 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_row_origin_bucket_law_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_MACROCYCLE = DOCS / (
    "prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync-router.json"
)
ROW_ORIGIN_BUCKET = DOCS / "prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json"
ROW_LEVEL = DOCS / "prime-matrix-strict-row-level-origin-generation-table-router.json"
FIXED_POINT = DOCS / "prime-matrix-strict-signed-source-fixed-point-breaker-router.json"
SUPPORT_STRIPPED = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
PHI_LPF = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"

ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SEED_EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
NONCIRCULAR_KERNEL = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
SUPPORT_CAPACITY = "PhiLPFPrimitiveRowSupportAndCapacityLedger"
BUCKET_SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当证明。"""
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
    """列出依赖证书。"""
    return [
        LATEST_MACROCYCLE,
        ROW_ORIGIN_BUCKET,
        ROW_LEVEL,
        FIXED_POINT,
        SUPPORT_STRIPPED,
        PHI_LPF,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """给出 row-origin table 到 bucket signed law 的同步链。"""
    return [
        {
            "from": ROW_TABLE,
            "to": SEED_EMITTER,
            "meaning": "逐行 clean-core 原始表必须由 Cauchy 前 seed signed-row emitter 正向产生。",
        },
        {
            "from": SEED_EMITTER,
            "to": NONCIRCULAR_KERNEL,
            "meaning": "signed-source 固定点切断后，emitter 不能从来源环恢复，必须给非循环 signed coefficient kernel。",
        },
        {
            "from": NONCIRCULAR_KERNEL,
            "to": f"{SUPPORT_CAPACITY} AND {BUCKET_SIGNED_LAW}",
            "meaning": "LPF/Phi 剥离无符号 support/capacity，剩余为桶级 signed coefficient law。",
        },
        {
            "from": SUPPORT_CAPACITY,
            "to": "closed unsigned support/capacity",
            "meaning": "最小素因子 owner、support key `(p,m)`、容量和 p>sqrt(N) 零质量已由 Phi-LPF 支付。",
        },
        {
            "from": BUCKET_SIGNED_LAW,
            "to": "latest direct hardpoint",
            "meaning": "必须正向给每个 `(p,m)` 的 signed coefficient、sign/local factor 和推前前求和恒等式。",
        },
    ]


def retained_basis() -> str:
    """返回最新保留基。"""
    return (
        f"(({BUCKET_SIGNED_LAW} AND {ROW_MASS}) OR {POINTWISE_TABLE} "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}) AND {SIGNED_SURVIVAL} "
        f"AND {EXACTUV_PAIR} AND {COMPLETE_KEY} AND {FIXED_KEY} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    latest = data["latest"]
    row_bucket = data["row_bucket"]
    row_level = data["row_level"]
    fixed_point = data["fixed_point"]
    support = data["support"]
    phi_lpf = data["phi_lpf"]
    return [
        row(
            "LatestRowOriginTableImported",
            latest.get("next_primary_attack_target") == ROW_TABLE
            and latest.get("row_level_clean_core_origin_generation_table_proved") is False,
            False,
            "上一层 macrocycle cut 后，mandatory signed-survival 侧门被压到 row-level origin table。",
            ROW_TABLE,
        ),
        row(
            "RowTableRequiresSeedEmitterImported",
            row_level.get("target_input_before_router") == ROW_TABLE
            and row_level.get("next_direct_attack_target") == SEED_EMITTER,
            True,
            "row-level 表不是后验枚举，必须由无环 pre-Cauchy seed signed-row emitter 产生。",
            SEED_EMITTER,
        ),
        row(
            "SignedSourceFixedPointCutImported",
            fixed_point.get("target_input_before_router") == ROW_TABLE
            and fixed_point.get("next_direct_attack_target") == NONCIRCULAR_KERNEL
            and fixed_point.get("signed_source_fixed_point_breaker_closed") is True,
            True,
            "row-level 表的现有内部来源链回到自身，只能切到 noncircular signed coefficient kernel。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "RowOriginBucketSyncImported",
            row_bucket.get("hardpoint_before_router") == ROW_TABLE
            and row_bucket.get("next_primary_attack_target") == BUCKET_SIGNED_LAW,
            False,
            "已有 row-origin/Phi-LPF 同步把 fixed point 切断后的 hardpoint 接到 bucket signed law。",
            BUCKET_SIGNED_LAW,
        ),
        row(
            "PhiLPFSupportStrippingImported",
            row_bucket.get("phi_lpf_support_stripping_imported") is True
            and support.get("phi_lpf_support_bijection_proved") is True,
            False,
            "support-stripped 证书把 noncircular kernel 的无符号支撑与容量剥离。",
            f"{SUPPORT_CAPACITY} AND {BUCKET_SIGNED_LAW}",
        ),
        row(
            "PhiLPFSupportAndCapacityClosed",
            row_bucket.get("phi_lpf_support_and_capacity_closed") is True
            and phi_lpf.get("phi_recursive_lpf_bucket_formula_proved") is True,
            True,
            "LPF/Phi 已支付 support key、owner layer、candidate capacity 与 p>sqrt(N) 零新筛质量。",
            SUPPORT_CAPACITY,
        ),
        row(
            "UnsignedBucketCannotEmitSignedLaw",
            row_bucket.get("row_origin_table_reduced_to_phi_lpf_bucket_signed_law") is True,
            True,
            "无符号桶只给 support/capacity；signed coefficient、local factor、orientation 仍需独立公式。",
            BUCKET_SIGNED_LAW,
        ),
        row(
            "BucketSignedLawCurrentCorpusProved",
            False,
            False,
            "当前材料没有对每个 `(p,m)` support key 正向赋 signed coefficient 与 sign/local factor。",
            BUCKET_SIGNED_LAW,
        ),
        row(
            "RowMassAndExactUVStillParallel",
            row_bucket.get("same_formal_unit_row_mass_normalization_proved") is False,
            False,
            "bucket signed law 不能自动支付 row-mass/no-heavy-row、ExactUV 和 key multiplicity。",
            f"{ROW_MASS} AND {EXACTUV_PAIR} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把 latest row-origin table 同步到桶级 signed law；未证明三命题无条件闭合。",
            f"{BUCKET_SIGNED_LAW} AND {ROW_MASS}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "latest": load_json(LATEST_MACROCYCLE),
        "row_bucket": load_json(ROW_ORIGIN_BUCKET),
        "row_level": load_json(ROW_LEVEL),
        "fixed_point": load_json(FIXED_POINT),
        "support": load_json(SUPPORT_STRIPPED),
        "phi_lpf": load_json(PHI_LPF),
    }
    rows = build_rows(data)
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_row_origin_bucket_law_sync_router",
        "status": "phi_lpf_latest_constructor_row_origin_synced_to_bucket_signed_law_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "latest_row_origin_table_imported": rows[0]["closed"],
        "row_table_requires_seed_emitter_imported": rows[1]["closed"],
        "signed_source_fixed_point_cut_imported": rows[2]["closed"],
        "row_origin_bucket_sync_imported": rows[3]["closed"],
        "phi_lpf_support_stripping_imported": rows[4]["closed"],
        "phi_lpf_support_and_capacity_closed": rows[5]["closed"],
        "row_origin_table_reduced_to_phi_lpf_bucket_signed_law": rows[6]["closed"],
        "phi_lpf_bucket_signed_coefficient_law_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": ROW_TABLE,
        "absorbed_to": BUCKET_SIGNED_LAW,
        "next_primary_attack_target": BUCKET_SIGNED_LAW,
        "parallel_primary_attack_targets": [
            ROW_MASS,
            SIGNED_SURVIVAL,
            POINTWISE_TABLE,
            EXACTUV_PAIR,
            COMPLETE_KEY,
            FIXED_KEY,
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "sync_chain": sync_chain(),
        "latest_retained_basis_after_router": retained_basis(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest macrocycle cut 后的 row-level origin table 接入既有 row-origin/Phi-LPF "
            "bucket law 同步。row-level 表不能由 signed-source 固定点自证；切断固定点后，LPF/Phi "
            f"已经支付无符号 support/capacity，真正剩余是 `{BUCKET_SIGNED_LAW}`。"
            "该 signed law、row-mass、ExactUV、complete/fixed key、terminal/PDEC、模型、Rate 与 "
            "DStructure 仍未证明；行/列命题仍未无条件闭合。"
        ),
    }
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix Phi-LPF latest constructor row-origin bucket-law sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
    ]
    for key in [
        "latest_row_origin_table_imported",
        "row_table_requires_seed_emitter_imported",
        "signed_source_fixed_point_cut_imported",
        "row_origin_bucket_sync_imported",
        "phi_lpf_support_stripping_imported",
        "phi_lpf_support_and_capacity_closed",
        "row_origin_table_reduced_to_phi_lpf_bucket_signed_law",
        "phi_lpf_bucket_signed_coefficient_law_proved",
        "same_formal_unit_row_mass_normalization_proved",
        "row_column_unconditional_closed",
        "next_primary_attack_target",
    ]:
        value = cert[key]
        lines.append(f"{key}={value if not isinstance(value, bool) else fmt_bool(value)}")
    lines.extend(
        [
            "```",
            "",
            "## 1. 同步链",
            "",
            "| from | to | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for edge in cert["sync_chain"]:
        lines.append(f"| `{cell(edge['from'])}` | `{cell(edge['to'])}` | {cell(edge['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for gate in cert["gates"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
                gate=cell(gate["gate"]),
                closed=fmt_bool(gate["closed"]),
                proved=fmt_bool(gate["proved"]),
                meaning=cell(gate["meaning"]),
                remaining=cell(gate["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 最新主攻",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
            "```",
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "```json",
            json.dumps(cert["source_hashes"], ensure_ascii=False, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 ledger、JSON 与 Markdown。"""
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"phi_lpf_support_and_capacity_closed={fmt_bool(cert['phi_lpf_support_and_capacity_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
