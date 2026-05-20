#!/usr/bin/env python3
"""生成 Phi-LPF moving-atom signed 注入拆分证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_moving_atom_signed_injection_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-moving-atom-signed-injection-split-router.json

输出：
  data/prime-matrix-phi-lpf-moving-atom-signed-injection-split-ledger.json
  docs/monograph/prime-matrix-phi-lpf-moving-atom-signed-injection-split-router.json
  docs/monograph/prime-matrix-phi-lpf-moving-atom-signed-injection-split-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-moving-atom-signed-injection-split"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREIMAGE_SYNC = DOCS / "prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-router.json"
ROW_ORIGIN = DOCS / "prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json"
SOURCE_ENTROPY = DOCS / "prime-matrix-phi-lpf-source-entropy-signed-survival-router.json"
POINTWISE_TABLE = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
SIGNED_SURVIVAL_ORIGIN = DOCS / "prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json"
RATE_PACKET = DOCS / "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json"

SIGNED_INJECTION = "LPFMovingAtomSignedPreimageMassInjectionLedger"
PREIMAGE_PARTITION = "LPFMovingAtomSourceBucketPreimagePartitionLedger"
POINTWISE_VALUE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
BUCKET_SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
PRIMITIVE_SUMMAND = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
PREPUSH_IDENTITY = "PhiLPFMovingAtomPrepushforwardSameUVSignedSumIdentity"
HALF_LANE = "LPFMovingAtomHalfMassSignLaneExtractionLemma"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
HIGH_SEGMENT = "HighSegmentModelGapAlpha043C3AnalyticLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 依赖；缺失视为未闭合。"""
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
    """登记本层依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREIMAGE_SYNC,
        ROW_ORIGIN,
        SOURCE_ENTROPY,
        POINTWISE_TABLE,
        SIGNED_SURVIVAL_ORIGIN,
        RATE_PACKET,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(deps: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 signed 注入拆分判定表。"""
    preimage = deps["preimage"]
    row_origin = deps["row_origin"]
    source_entropy = deps["source_entropy"]
    pointwise = deps["pointwise"]
    signed_origin = deps["signed_origin"]
    rate_packet = deps["rate_packet"]

    preimage_imported = (
        preimage.get("next_primary_attack_target") == SIGNED_INJECTION
        and preimage.get("moving_atom_unsigned_source_preimage_partition_closed") is True
    )
    pointwise_open = pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
    row_mass_open = (
        source_entropy.get("nonzero_signed_row_survival_proved") is False
        and source_entropy.get("same_formal_unit_row_mass_normalization_proved") is False
    )
    signed_law_open = row_origin.get("phi_lpf_bucket_signed_coefficient_law_proved") is False
    rate_open = rate_packet.get("rate_bearing_moving_atom_packet_exclusion_proved") is False
    origin_sync_imported = signed_origin.get("row_level_origin_table_imported") is True or signed_origin != {}
    return [
        row(
            "LPFPreimagePartitionImported",
            preimage_imported,
            True,
            "上一层已删除无主/prime-row 前像，moving atom 若存在必须有 LPF-owned source-bucket 前像。",
            SIGNED_INJECTION,
        ),
        row(
            "SignedInjectionHasNoUnsignedRemainder",
            preimage_imported and signed_law_open,
            True,
            "signed 注入不再包含新的计数问题；无符号桶容量已支付，剩余全是 signed value、prepushforward identity 与质量归一化字段。",
            f"{POINTWISE_VALUE_TABLE} AND {ROW_MASS}",
        ),
        row(
            "HalfMassSignLaneExtractionFiniteAlgebra",
            preimage_imported,
            True,
            "若 exact prepushforward same-(u,v) signed sum identity 已给出，|sum w_e|>=T 立即推出正/负某一 sign-lane 的绝对质量至少 T/2。",
            PREPUSH_IDENTITY,
        ),
        row(
            "PrepushforwardSameUVIdentityCurrentCorpusProved",
            False,
            False,
            "当前语料没有给出每个 LPF bucket signed coefficient 到 final same-(u,v) atom 的逐点推前前恒等式。",
            f"{POINTWISE_VALUE_TABLE} OR {BUCKET_SIGNED_LAW}",
        ),
        row(
            "PointwiseSignedValueTableStillOpen",
            pointwise_open,
            False,
            "逐点 Phi-LPF signed 表仍是直接非循环替代；沿现有来源链展开会回到 signed-source 固定点。",
            POINTWISE_VALUE_TABLE,
        ),
        row(
            "SignedSurvivalAndRowMassStillOpen",
            row_mass_open,
            False,
            "即使逐点表存在，还需证明足够多非零 signed rows、同 formal unit 总质量和 no-heavy-row/L2。",
            f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "OriginTableSyncImportedButNotProof",
            origin_sync_imported,
            False,
            "signed-survival/origin-table 同步说明该缺口会回到 primitive summand signed expression，而不是自动闭合。",
            PRIMITIVE_SUMMAND,
        ),
        row(
            "RatePacketStillParallel",
            rate_open,
            False,
            "若 signed 注入走终端包路线，仍需 PDEC/CleanKLS 速率包、高段模型余量和 RatePreservation。",
            f"{PDEC_CLEAN_KLS} AND {HIGH_SEGMENT} AND {RATE}",
        ),
        row(
            "SignedInjectionLedgerCurrentCorpusProved",
            False,
            False,
            "本层只把 signed 注入拆成逐点表/推前恒等式、半质量 sign-lane 和 row-mass；没有排斥 moving atom。",
            f"{POINTWISE_VALUE_TABLE} AND {SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层不是三目标命题无条件闭合。",
            f"{POINTWISE_VALUE_TABLE} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 signed 注入拆分证书。"""
    deps = {
        "preimage": load_json(PREIMAGE_SYNC),
        "row_origin": load_json(ROW_ORIGIN),
        "source_entropy": load_json(SOURCE_ENTROPY),
        "pointwise": load_json(POINTWISE_TABLE),
        "signed_origin": load_json(SIGNED_SURVIVAL_ORIGIN),
        "rate_packet": load_json(RATE_PACKET),
    }
    rows = build_rows(deps)
    strict_basis = (
        f"({POINTWISE_VALUE_TABLE} AND {SIGNED_SURVIVAL} AND {ROW_MASS}) "
        f"AND {RATE} AND {DSTRUCTURE}"
    )
    retained_basis = (
        f"(({POINTWISE_VALUE_TABLE} OR {BUCKET_SIGNED_LAW} OR {PRIMITIVE_SUMMAND}) "
        f"AND {SIGNED_SURVIVAL} AND {ROW_MASS}) OR "
        f"({PDEC_CLEAN_KLS} AND {HIGH_SEGMENT} AND {RATE})"
    )
    sync_chain = [
        {
            "from": SIGNED_INJECTION,
            "to": f"{PREPUSH_IDENTITY} AND {HALF_LANE}",
            "meaning": "signed 注入由逐点推前前恒等式加有限 sign-lane 半质量抽取组成。",
        },
        {
            "from": PREPUSH_IDENTITY,
            "to": f"{POINTWISE_VALUE_TABLE} OR {BUCKET_SIGNED_LAW}",
            "meaning": "same-(u,v) 推前前恒等式必须由逐点 signed 表或完整 bucket signed law 正向给出。",
        },
        {
            "from": HALF_LANE,
            "to": "closed finite algebra after identity",
            "meaning": "一旦恒等式给出，|sum w_e| 大迫使某一 sign-lane 至少承担一半绝对质量。",
        },
        {
            "from": f"{POINTWISE_VALUE_TABLE} OR {BUCKET_SIGNED_LAW}",
            "to": f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
            "meaning": "signed 值表还必须配合同 formal unit 非零存活、总质量和 no-heavy-row/L2。",
        },
    ]
    return {
        "certificate_type": "prime_matrix_phi_lpf_moving_atom_signed_injection_split_router",
        "status": "phi_lpf_moving_atom_signed_injection_split_to_pointwise_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "target_input_before_router": SIGNED_INJECTION,
        "lpf_preimage_partition_imported": rows[0]["closed"],
        "signed_injection_has_no_unsigned_remainder": rows[1]["closed"],
        "half_mass_sign_lane_extraction_finite_algebra_closed": rows[2]["closed"],
        "prepushforward_same_uv_identity_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "signed_survival_and_row_mass_proved": False,
        "signed_injection_ledger_current_corpus_proved": False,
        "row_column_unconditional_closed": False,
        "next_primary_attack_target": POINTWISE_VALUE_TABLE,
        "parallel_primary_attack_targets": [
            BUCKET_SIGNED_LAW,
            PRIMITIVE_SUMMAND,
            SIGNED_SURVIVAL,
            ROW_MASS,
            PDEC_CLEAN_KLS,
            HIGH_SEGMENT,
            RATE,
            DSTRUCTURE,
        ],
        "strict_basis_after_router": strict_basis,
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步继续拆解 `{SIGNED_INJECTION}`。上一层已经把 moving atom 的无符号前像固定到 "
            "LPF-owned source buckets；因此 signed 注入本身没有新的计数自由度。若逐点推前前 "
            "same-(u,v) signed sum identity 已给出，则大原子到某一正/负 sign-lane 的半质量抽取是"
            "有限线性代数。当前真正缺口是正向提交逐点 Phi-LPF signed value table 或完整 bucket "
            "signed law，并配合同一 formal unit 的 signed survival 与 row-mass/no-heavy-row 账本。"
            f"最新直接主攻同步为 `{POINTWISE_VALUE_TABLE}`；行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF moving-atom signed-injection split 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"lpf_preimage_partition_imported={fmt_bool(cert['lpf_preimage_partition_imported'])}",
        f"signed_injection_has_no_unsigned_remainder={fmt_bool(cert['signed_injection_has_no_unsigned_remainder'])}",
        f"half_mass_sign_lane_extraction_finite_algebra_closed={fmt_bool(cert['half_mass_sign_lane_extraction_finite_algebra_closed'])}",
        f"prepushforward_same_uv_identity_proved={fmt_bool(cert['prepushforward_same_uv_identity_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"signed_survival_and_row_mass_proved={fmt_bool(cert['signed_survival_and_row_mass_proved'])}",
        f"signed_injection_ledger_current_corpus_proved={fmt_bool(cert['signed_injection_ledger_current_corpus_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 有限 sign-lane 抽取",
        "",
        "若某个 final same-(u,v) atom 满足 `|sum_{e in F} w_e| >= T`，则在已知逐点推前前恒等式的条件下，",
        "正 lane 或负 lane 至少一个承担 `>= T/2` 的绝对质量。该步不需要新的筛计数；缺失的是 `w_e` 的逐点来源表。",
        "",
        "## 2. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. strict 基",
            "",
            "```text",
            cert["strict_basis_after_router"],
            "```",
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
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
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
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
