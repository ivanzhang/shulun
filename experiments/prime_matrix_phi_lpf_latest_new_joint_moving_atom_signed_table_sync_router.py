#!/usr/bin/env python3
"""生成 Phi-LPF latest new-joint moving-atom 到逐点 signed 表的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_moving_atom_signed_table_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-moving-atom-signed-table-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-moving-atom-signed-table-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-moving-atom-signed-table-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-moving-atom-signed-table-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-moving-atom-signed-table-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_MOVING = (
    DOCS / "prime-matrix-phi-lpf-latest-new-joint-alpha-terminal-three-atoms-sync-router.json"
)
MOVING_PREIMAGE = DOCS / "prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-router.json"
SIGNED_SPLIT = DOCS / "prime-matrix-phi-lpf-moving-atom-signed-injection-split-router.json"
POINTWISE_TABLE_DOC = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
SOURCE_SURVIVAL = DOCS / "prime-matrix-phi-lpf-source-entropy-signed-survival-router.json"
RATE_PACKET = DOCS / "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json"

INDEPENDENT_MOVING = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
LPF_PREIMAGE = "LPFMovingAtomSourceBucketPreimagePartitionLedger"
SIGNED_INJECTION = "LPFMovingAtomSignedPreimageMassInjectionLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
BUCKET_SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
SIGNED_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
HIGH_SEGMENT = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
TRANSPORT_COHERENCE = (
    "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND "
    "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
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
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def dependency_paths() -> list[Path]:
    """列出本层依赖。"""
    return [CURRENT_MOVING, MOVING_PREIMAGE, SIGNED_SPLIT, POINTWISE_TABLE_DOC, SOURCE_SURVIVAL, RATE_PACKET]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """给出同步链。"""
    return [
        {
            "from": INDEPENDENT_MOVING,
            "to": MOVING_ATOM,
            "meaning": "当前 latest 版本仍以排斥 actual clean-core moving atom 为目标。",
        },
        {
            "from": MOVING_ATOM,
            "to": LPF_PREIMAGE,
            "meaning": "LPF/Phi 前像证书删除无主、prime-row 与 virtual-unit source escape。",
        },
        {
            "from": LPF_PREIMAGE,
            "to": SIGNED_INJECTION,
            "meaning": "无符号前像分桶已闭合，剩余是同 formal unit 的 signed mass injection。",
        },
        {
            "from": SIGNED_INJECTION,
            "to": f"{POINTWISE_TABLE} OR {BUCKET_SIGNED_LAW}",
            "meaning": "signed injection split 删除剩余无符号自由度，首攻变成逐点 signed 表或完整 bucket signed law。",
        },
        {
            "from": f"{POINTWISE_TABLE} OR {BUCKET_SIGNED_LAW}",
            "to": f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
            "meaning": "signed 表还必须配合同 formal unit 非零存活、总质量和 no-heavy-row/L2。",
        },
    ]


def build_rows(
    current: dict[str, Any],
    preimage: dict[str, Any],
    signed_split: dict[str, Any],
    pointwise: dict[str, Any],
    survival: dict[str, Any],
    rate_packet: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "CurrentNewJointMovingAtomFrontierImported",
            current.get("next_primary_attack_target") == INDEPENDENT_MOVING
            and current.get("independent_moving_atom_chosen_as_narrowest") is True,
            False,
            "刚提交的 new-joint alpha terminal 三原子层把最窄直接主攻钉在 independent moving atom。",
            INDEPENDENT_MOVING,
        ),
        row(
            "MovingAtomSourceBucketPreimageImported",
            preimage.get("target_input_before_router") == INDEPENDENT_MOVING
            and preimage.get("next_primary_attack_target") == SIGNED_INJECTION
            and preimage.get("moving_atom_unsigned_source_preimage_partition_closed") is True,
            True,
            "LPF/Phi 已删除 moving atom 的无主、prime-row、virtual-unit 前像逃逸；只剩 LPF-owned signed preimage。",
            SIGNED_INJECTION,
        ),
        row(
            "LPFBucketIdentitySampleCarried",
            preimage.get("lpf_bucket_identity_sample_verified") is True,
            True,
            "N=10000 LPF/Phi 桶恒等式样本仍作为一致性读数携带；它不是全局证明替代。",
            LPF_PREIMAGE,
        ),
        row(
            "SignedInjectionSplitImported",
            signed_split.get("target_input_before_router") == SIGNED_INJECTION
            and signed_split.get("next_primary_attack_target") == POINTWISE_TABLE
            and signed_split.get("signed_injection_has_no_unsigned_remainder") is True,
            False,
            "signed injection 不再含 unsigned counting 自由度；首攻是逐点 Phi-LPF signed 表或完整 bucket signed law。",
            f"{POINTWISE_TABLE} OR {BUCKET_SIGNED_LAW}",
        ),
        row(
            "HalfMassFiniteAlgebraImported",
            signed_split.get("half_mass_sign_lane_extraction_finite_algebra_closed") is True,
            True,
            "若 prepushforward same-(u,v) signed-sum identity 已给出，大原子到某一 sign lane 的半质量抽取只是有限线性代数。",
            "identity remains open before finite algebra can be used",
        ),
        row(
            "PointwiseSignedTableStillOpen",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
            and signed_split.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 signed 表当前未证明；沿现有来源链展开会回到 signed-source 固定点。",
            POINTWISE_TABLE,
        ),
        row(
            "SignedSurvivalAndRowMassStillOpen",
            survival.get("nonzero_signed_row_survival_proved") is False
            and survival.get("same_formal_unit_row_mass_normalization_proved") is False
            and signed_split.get("signed_survival_and_row_mass_proved") is False,
            False,
            "即使 signed 表存在，还需同 formal unit 的非零 signed row 存活、总质量归一化和 no-heavy-row/L2。",
            f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "RatePacketStillParallel",
            rate_packet.get("moving_atom_low_dim_or_no_signature_interface_closed") is True,
            False,
            "若 moving atom 走速率型终端包，仍需 PDEC/CleanKLS、高段模型余量与 RatePreservation。",
            f"{PDEC_CLEAN_KLS} AND {HIGH_SEGMENT} AND {RATE}",
        ),
        row(
            "LatestMovingAtomExclusionAfterSignedSplitProved",
            False,
            False,
            "本层只把 latest moving atom 归约到逐点 signed 表、signed survival/row-mass 或速率型终端包；没有排斥 moving atom。",
            f"{POINTWISE_TABLE} AND {SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层仍是前沿同步与拆分，不是三目标命题无条件闭合。",
            f"{POINTWISE_TABLE} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    current = load_json(CURRENT_MOVING)
    preimage = load_json(MOVING_PREIMAGE)
    signed_split = load_json(SIGNED_SPLIT)
    pointwise = load_json(POINTWISE_TABLE_DOC)
    survival = load_json(SOURCE_SURVIVAL)
    rate_packet = load_json(RATE_PACKET)
    rows = build_rows(
        current=current,
        preimage=preimage,
        signed_split=signed_split,
        pointwise=pointwise,
        survival=survival,
        rate_packet=rate_packet,
    )
    strict_basis = (
        f"({POINTWISE_TABLE} AND {SIGNED_SURVIVAL} AND {ROW_MASS}) "
        f"AND {RATE} AND {DSTRUCTURE}"
    )
    retained_basis = (
        f"(({POINTWISE_TABLE} OR {BUCKET_SIGNED_LAW} OR {SIGNED_EXPR}) AND "
        f"{SIGNED_SURVIVAL} AND {ROW_MASS}) OR "
        f"({PDEC_CLEAN_KLS} AND {HIGH_SEGMENT} AND {RATE}) OR "
        f"{EXACTUV_PAIR} OR ({TRANSPORT_COHERENCE})"
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_moving_atom_signed_table_sync_router",
        "status": "phi_lpf_latest_new_joint_moving_atom_synced_to_pointwise_signed_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "current_new_joint_moving_atom_frontier_imported": rows[0]["closed"],
        "moving_atom_source_bucket_preimage_imported": rows[1]["closed"],
        "lpf_bucket_identity_sample_carried": rows[2]["closed"],
        "signed_injection_split_imported": rows[3]["closed"],
        "half_mass_finite_algebra_imported": rows[4]["closed"],
        "pointwise_signed_table_proved": False,
        "signed_survival_and_row_mass_proved": False,
        "rate_packet_exclusion_proved": False,
        "latest_moving_atom_exclusion_after_signed_split_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": INDEPENDENT_MOVING,
        "absorbed_to": POINTWISE_TABLE,
        "next_primary_attack_target": POINTWISE_TABLE,
        "parallel_primary_attack_targets": [
            BUCKET_SIGNED_LAW,
            SIGNED_EXPR,
            SIGNED_SURVIVAL,
            ROW_MASS,
            PDEC_CLEAN_KLS,
            HIGH_SEGMENT,
            RATE,
            DSTRUCTURE,
            EXACTUV_PAIR,
            TRANSPORT_COHERENCE,
        ],
        "strict_basis_after_router": strict_basis,
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步把当前 new-joint latest 的 `{INDEPENDENT_MOVING}` 接到 moving-atom 下游两层："
            "LPF/Phi 源桶前像删除无主与 prime-row 逃逸，signed-injection split 删除剩余 unsigned "
            f"counting 自由度。因此最新直接主攻推进为 `{POINTWISE_TABLE}`；并行仍需 "
            f"`{SIGNED_SURVIVAL}`、`{ROW_MASS}`、bucket signed law、primitive signed expression、"
            "PDEC/CleanKLS 速率包、高段模型余量、Rate、DStructure、ExactUV 与 rough-cofactor transport/coherence。"
            "行/列命题仍未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest new-joint moving-atom signed-table sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"current_new_joint_moving_atom_frontier_imported={fmt_bool(cert['current_new_joint_moving_atom_frontier_imported'])}",
        f"moving_atom_source_bucket_preimage_imported={fmt_bool(cert['moving_atom_source_bucket_preimage_imported'])}",
        f"lpf_bucket_identity_sample_carried={fmt_bool(cert['lpf_bucket_identity_sample_carried'])}",
        f"signed_injection_split_imported={fmt_bool(cert['signed_injection_split_imported'])}",
        f"half_mass_finite_algebra_imported={fmt_bool(cert['half_mass_finite_algebra_imported'])}",
        f"pointwise_signed_table_proved={fmt_bool(cert['pointwise_signed_table_proved'])}",
        f"signed_survival_and_row_mass_proved={fmt_bool(cert['signed_survival_and_row_mass_proved'])}",
        f"latest_moving_atom_exclusion_after_signed_split_proved={fmt_bool(cert['latest_moving_atom_exclusion_after_signed_split_proved'])}",
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
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. strict 基",
            "",
            "```text",
            cert["strict_basis_after_router"],
            "```",
            "",
            "## 4. 最新保留基",
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
            "## 5. 依赖哈希",
            "",
            "```json",
            json.dumps(cert["source_hashes"], ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    cert = build_certificate()
    print(json.dumps(cert, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
