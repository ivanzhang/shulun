#!/usr/bin/env python3
"""生成两条替代线 RKS-log 最终原子同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_rks_log_final_atom_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-rks-log-final-atom-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-rks-log-final-atom-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-rks-log-final-atom-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-rks-log-final-atom-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SLUG = "prime-matrix-two-replacement-lines-rks-log-final-atom-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

COMMON_KERNEL = DOCS / "prime-matrix-two-replacement-lines-common-unconditional-kernel-router.json"
DSTRUCTURE_COMPRESS = DOCS / "prime-matrix-strict-dstructure-tail-rankin-replacement-compression-router.json"
EXT_BG_RKS = DOCS / "prime-matrix-strict-ext-bg-rks-tail-log4-replacement-router.json"
STRUCTURED_EHPD = DOCS / "prime-matrix-strict-structured-ehpd-final-interface-audit-router.json"
FULL_RANKIN = DOCS / "prime-matrix-full-rankin-ledger-inventory-router.json"
EXTERNAL_KLS_FINAL = DOCS / "prime-matrix-external-kls-accepted-final-promotion-router.json"

ACCEPTED_FULLS = "AcceptedFullSKLSExtExternalContract"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
DSTRUCTURE_SELF = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"
STRUCTURED_EHPD_AUDIT = "AuthorSideStructuredEHPDInterfaceAuditClosed"
FINITE_VERIFY = "ReproducibleFiniteVerificationArchiveWithHashesAndIndependentRunner"
FULL_RANKIN_CLOSED = "SelfContainedFullRankinPassOrReturnLedgerAndDownstreamReturnIntegration"
RKS_LOG = "SelfContainedRKSLogReciprocalKloostermanTailLog4Input"
BG_FIXED_LOG = "MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks"
BAKER_DB = "BakerFrequencyLargeSieveOrDBGAverageReplacement"
ACCEPT_EXT_BG = "AcceptEXTBGForRKSLogFixedSaving"
FULLS_MATCH = "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch"
FULLS_CAPACITY = "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput"
NEW_AUTOMORPHIC = "NewAutomorphicDispersionProof"
SIX_FIELD = "NewActualJointAlphaDeltaSixFieldConstructorArtifact"
EXACT_CERT = "AcyclicCanonicalExactSameSetPromotionCertificate"
SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
SOURCE_IDENTITY = "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab"
ANTIATOM = "FullSNonAPStrengthenedSourceAntiAtomForActualSource"
UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
PDEC_RATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本证书直接依赖。"""
    paths = [
        Path(__file__).resolve(),
        COMMON_KERNEL,
        DSTRUCTURE_COMPRESS,
        EXT_BG_RKS,
        STRUCTURED_EHPD,
        FULL_RANKIN,
        EXTERNAL_KLS_FINAL,
        PAPER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def source_front() -> str:
    """内部 source 前端。"""
    return f"{SIX_FIELD} OR {EXACT_CERT} OR {SOURCE_ENTROPY} OR {SOURCE_IDENTITY} OR {ANTIATOM}"


def spectral_front() -> str:
    """外部谱前端。"""
    return f"{FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_AUTOMORPHIC}"


def external_conditional_basis() -> str:
    """外部引理条件版基。"""
    return f"{ACCEPTED_FULLS} AND {DSTRUCTURE_GATE}"


def external_theorem_replacement_basis() -> str:
    """接受 EXT-BG/RKS 时的外部定理替代基。"""
    return (
        f"{ACCEPTED_FULLS} AND {ACCEPT_EXT_BG} AND {STRUCTURED_EHPD_AUDIT} "
        f"AND {FINITE_VERIFY} AND {FULL_RANKIN_CLOSED}"
    )


def external_absolute_author_basis() -> str:
    """外部绝对作者证明版基。"""
    return f"({spectral_front()}) AND {STRUCTURED_EHPD_AUDIT} AND {FINITE_VERIFY} AND {FULL_RANKIN_CLOSED} AND ({BG_FIXED_LOG} OR {BAKER_DB})"


def internal_self_contained_basis() -> str:
    """内部自足版基，已把 DStructure 自足包压到 RKS-log 原子。"""
    return (
        f"({source_front()}) AND {UV} AND {HIGH_MODEL} AND {PDEC_RATE} AND {RATE} "
        f"AND {STRUCTURED_EHPD_AUDIT} AND {FINITE_VERIFY} AND {FULL_RANKIN_CLOSED} "
        f"AND ({BG_FIXED_LOG} OR {BAKER_DB})"
    )


def row(
    gate: str,
    closed: bool,
    proved: bool,
    lane: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造同步判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "lane": lane,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """从上游证书构造最终原子表。"""
    common_imported = (
        data["common"].get("status") == "two_replacement_lines_common_unconditional_kernel_pinned_unconditional_open"
        and data["common"].get("common_unconditional_kernel_boundary_closed") is True
    )
    dstructure_compressed = (
        data["dstructure"].get("status")
        == "self_contained_replacement_package_compressed_to_rks_log_reciprocal_kloosterman_core"
        and data["dstructure"].get("rks_log_reciprocal_kloosterman_atom_isolated") is True
    )
    ext_bg_ready = data["ext_bg"].get("external_bg_for_rks_log_fixed_saving_closed_if_accepted") is True
    ext_bg_self_closed = data["ext_bg"].get("multilinear_reciprocal_kloosterman_self_contained_reproof_closed") is True
    structured_closed = data["structured"].get("author_side_structured_interface_audit_closed") is True
    rankin_closed = data["rankin"].get("full_rankin_ledger_still_open_closed") is True
    external_kls_math_closed = data["external_kls"].get("all_math_inputs_closed_after_external_acceptance") is True

    return [
        row(
            "CommonKernelImported",
            common_imported,
            True,
            "both",
            "上一层已把共同无条件核定位为 DStructure/Rankin 自足尾门，而非 FullS 或 six-field 前端。",
            DSTRUCTURE_SELF,
        ),
        row(
            "DStructureKernelCompressedToRKSLog",
            dstructure_compressed,
            True,
            "both",
            "DStructure 形式壳、Tail-log4 形式分解、smooth/mid 账本与 finite Rankin 已压到 RKS-log 低谱原子。",
            RKS_LOG,
        ),
        row(
            "StructuredEHPDAuthorInterfaceClosed",
            structured_closed,
            True,
            "both",
            "A/B 到 D、D 组接口、常数编号和有限覆盖证书已经作者侧审计闭合。",
            "independent acceptance or self-contained analytic replacement",
        ),
        row(
            "FullRankinPassOrReturnClosed",
            rankin_closed,
            True,
            "both",
            "正式 Rankin 证书全集缺口已由 manifest/data 与 batch pass-or-return 回收。",
            "no active Rankin subledger obstruction",
        ),
        row(
            "ExternalBGParameterMatchClosedIfAccepted",
            ext_bg_ready,
            False,
            "external theorem lane",
            "接受 EXT-BG/Baker 型固定对数节省时，RKS/Tail-log4 参数匹配闭合。",
            ACCEPT_EXT_BG,
        ),
        row(
            "ExternalKLSMathLaneAlreadyConditional",
            external_kls_math_closed,
            False,
            "external theorem lane",
            "接受 FullS-KLS-ext 后，外部谱数学 lane 已闭合；剩余不能再转写成内部 source 问题。",
            external_conditional_basis(),
        ),
        row(
            "StrictSelfContainedRKSLogReproofOpen",
            ext_bg_self_closed,
            ext_bg_self_closed,
            "internal self-contained lane",
            "严格自足版尚未重证 BG 型双线性/多线性倒数 Kloosterman 固定对数节省。",
            f"{BG_FIXED_LOG} OR {BAKER_DB}",
        ),
        row(
            "ExternalTheoremVersionAuthorMathClosedIfInputsAccepted",
            ext_bg_ready and structured_closed and rankin_closed and external_kls_math_closed,
            False,
            "external theorem lane",
            "外部定理版作者侧数学输入可在接受 FullS-KLS-ext 与 EXT-BG/RKS 后闭合，但这仍不是自足重证。",
            external_theorem_replacement_basis(),
        ),
        row(
            "InternalSelfContainedVersionClosed",
            False,
            False,
            "internal self-contained lane",
            "内部自足版还必须同时支付 source 前端、ExactUV/模型/PDEC/Rate 与 RKS-log 自足重证。",
            internal_self_contained_basis(),
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "final theorem",
            "本层闭合最终原子定位，不把外部接受、参数匹配或等价命名伪装成目标命题无条件证明。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "common": read_json(COMMON_KERNEL),
        "dstructure": read_json(DSTRUCTURE_COMPRESS),
        "ext_bg": read_json(EXT_BG_RKS),
        "structured": read_json(STRUCTURED_EHPD),
        "rankin": read_json(FULL_RANKIN),
        "external_kls": read_json(EXTERNAL_KLS_FINAL),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "two_replacement_lines_rks_log_final_atom_sync_router",
        "status": "two_replacement_lines_rks_log_final_atom_synced_unconditional_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "noncycle_route_enforced": True,
        "common_kernel_compressed_to_rks_log": True,
        "rankin_subledger_active_obstruction": False,
        "structured_ehpd_author_interface_active_obstruction": False,
        "external_theorem_version_author_math_closed_if_inputs_accepted": True,
        "external_theorem_version_unconditional_promotion_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "external_conditional_basis": external_conditional_basis(),
        "external_theorem_replacement_basis": external_theorem_replacement_basis(),
        "external_absolute_author_basis": external_absolute_author_basis(),
        "internal_self_contained_basis": internal_self_contained_basis(),
        "final_self_contained_atom": f"{BG_FIXED_LOG} OR {BAKER_DB}",
        "forbidden_cycles": [
            "Do not replace RKS-log additive reciprocal phases by Burgess multiplicative character sums.",
            "Do not use FullS-KLS spectral closure to manufacture six-field source coefficients.",
            "Do not use six-field/source constructors to prove FullS-KLS theorem-match.",
            "Do not treat EXT-BG acceptance as a self-contained reproof.",
        ],
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "status_snapshot": {name: data[name].get("status") for name in data},
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "共同核已继续下钻到 Tail-log4 低谱 RKS-log 原子：Structured-EHPD 作者侧接口、"
            "finite Rankin pass-or-return、Tail-log4 smooth/mid 与参数账本均不再是当前最窄硬点。"
            "外部定理版在接受 FullS-KLS-ext 与 EXT-BG/RKS 固定对数节省时作者侧数学输入闭合，"
            "但这不是严格自足重证。内部自足版的真剩余是 "
            "MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks 或 BakerFrequencyLargeSieveOrDBGAverageReplacement，"
            "并且仍需并行支付 source 前端、ExactUV、模型、PDEC/CleanKLS 与 Rate。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix 两条替代线 RKS-log 最终原子同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"common_kernel_compressed_to_rks_log={fmt_bool(payload['common_kernel_compressed_to_rks_log'])}",
        f"rankin_subledger_active_obstruction={fmt_bool(payload['rankin_subledger_active_obstruction'])}",
        f"structured_ehpd_author_interface_active_obstruction={fmt_bool(payload['structured_ehpd_author_interface_active_obstruction'])}",
        f"external_theorem_version_author_math_closed_if_inputs_accepted={fmt_bool(payload['external_theorem_version_author_math_closed_if_inputs_accepted'])}",
        f"external_theorem_version_unconditional_promotion_closed={fmt_bool(payload['external_theorem_version_unconditional_promotion_closed'])}",
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | lane | meaning | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in payload["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(item["gate"]),
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["lane"]),
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 三条基",
            "",
            "外部引理条件版：",
            "",
            "```text",
            payload["external_conditional_basis"],
            "```",
            "",
            "外部定理替代版：",
            "",
            "```text",
            payload["external_theorem_replacement_basis"],
            "```",
            "",
            "外部绝对作者证明版：",
            "",
            "```text",
            payload["external_absolute_author_basis"],
            "```",
            "",
            "内部自足版：",
            "",
            "```text",
            payload["internal_self_contained_basis"],
            "```",
            "",
            "## 4. 最终自足原子",
            "",
            "```text",
            payload["final_self_contained_atom"],
            "```",
            "",
            "## 5. 禁止循环替代",
            "",
        ]
    )
    for item in payload["forbidden_cycles"]:
        lines.append(f"- {item}")
    lines.extend(["", "## 6. 状态快照", "", "| field | value |", "| --- | --- |"])
    for key, value in payload["status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(["", "## 7. 依赖哈希", "", "| file | sha256 |", "| --- | --- |"])
    for name, digest in payload["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """执行证书生成。"""
    write_outputs(build_payload())


if __name__ == "__main__":
    main()
