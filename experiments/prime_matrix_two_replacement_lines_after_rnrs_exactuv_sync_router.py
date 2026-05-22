#!/usr/bin/env python3
"""生成 RNRS 回填后的两条替代线 ExactUV 同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_after_rnrs_exactuv_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

TWO_LINES = DOCS / "prime-matrix-two-replacement-lines-terminal-attack-router.json"
RKS_RNRS = DOCS / "prime-matrix-strict-rks-log-rnrs-transfer-closure-router.json"
RKS_PROMOTION = DOCS / "prime-matrix-strict-rks23-final-promotion-audit-router.json"
EXACTUV_ATTACK = DOCS / "prime-matrix-strict-exact-uv-support-attack-router.json"
EXACTUV_TERMINAL = DOCS / "prime-matrix-exact-uv-support-terminal-attack-router.json"
CLEAN_SUPPORT = DOCS / "prime-matrix-clean-core-support-incidence-attack-router.json"
CLEAN_NORMAL = DOCS / "prime-matrix-clean-core-terminal-normal-form-router.json"
FULLS_MATCH = DOCS / "prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json"
FULLS_REMAINDER = DOCS / "prime-matrix-fulls-theorem-match-true-remainder-cut-router.json"
DSTRUCTURE_SPLIT = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空证据。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """格式化布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def dependency_paths() -> list[Path]:
    """列出依赖文件。"""
    return [
        TWO_LINES,
        RKS_RNRS,
        RKS_PROMOTION,
        EXACTUV_ATTACK,
        EXACTUV_TERMINAL,
        CLEAN_SUPPORT,
        CLEAN_NORMAL,
        FULLS_MATCH,
        FULLS_REMAINDER,
        DSTRUCTURE_SPLIT,
        CLAIM_STATUS,
        CONTRACTS,
        FRONTIER,
        EXTERNAL_INDEX,
        PAPER,
    ]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成同步判定行。"""
    return [
        row(
            "PreviousTwoLineBoundaryImported",
            True,
            True,
            "上一层已把无黑箱外部线和内部自足线分开，且禁止 Phi-LPF/CRT 重命名闭合。",
            "sync with later RNRS and ExactUV certificates",
        ),
        row(
            "RKSLogSupersededByRNRSTransfer",
            data["rks_rnrs"].get("self_contained_rks_log_reciprocal_kloosterman_tail_log4_input_closed")
            is True,
            data["rks_rnrs"].get("rks_log_rnrs_transfer_closed") is True,
            "RKS-log/TL4-L 解析核心已由 RNRS/Rudnev 倒数能量链在作者侧回填闭合；它不再是最新内部真硬点。",
            "ActualNoncanonicalExactUVSupportLowerBound",
        ),
        row(
            "DStructureReplacementAuthorDossierNoLongerRKSBlocked",
            data["rks_rnrs"].get("self_contained_dstructure_tail_log4_finite_rankin_replacement_package_author_side_closed")
            is True,
            data["rks_rnrs"].get("self_contained_dstructure_tail_log4_finite_rankin_replacement_package_author_side_closed")
            is True,
            "DStructure/Tail-log4/finite Rankin 自足替代包的作者侧 RKS 阻断已移除，但这不等于独立验收事件发生。",
            "final promotion absorption audit or independent acceptance discipline remains",
        ),
        row(
            "ExactUVSupportIsLatestInternalSourceTerminal",
            data["exactuv_terminal"].get("exact_uv_support_terminal_boundary_closed") is True
            or data["exactuv_attack"].get("strict_exact_uv_attack_boundary_closed") is True,
            False,
            "内部自足数学主攻点归一为 actual noncanonical exact u/v 支撑下界，等价地为 exact clean-core source entropy。",
            "ActualNoncanonicalExactUVSupportLowerBound OR ExactCleanCoreFullSNonAPWFDSourceEntropy",
        ),
        row(
            "CleanCoreLayerTransferStillOpen",
            data["clean_support"].get("clean_core_support_incidence_attack_boundary_closed") is True,
            False,
            "普通 squarefree 数量、K4/K6 incidence 和 canonical 支撑偷渡均已阻断；真正需要 clean-core exact 层承认、非零转移和 thin return。",
            "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn",
        ),
        row(
            "ExternalNoBlackboxNormalForm",
            data["clean_normal"].get("clean_core_terminal_normal_form_closed") is True,
            False,
            "外部无黑箱线的标准形不是泛称 DI/BFI，而是 completed、modulus-dependent Full-S KLS 输入。",
            "ModulusDependentCompletedFullSKLSInput OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof",
        ),
        row(
            "ExternalLemmaConditionalClosureStillOnlyConditional",
            True,
            False,
            "接受 FullS-KLS-ext/completed KLS 与 DStructure 独立验收时，外部引理版可条件闭合；当前语料库没有无条件化这些输入。",
            "AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层同步最新真硬点并移除过期 RKS-open 标记；未证明 ExactUV/source entropy，也未发生独立晋级验收。",
            "ExactCleanCoreFullSNonAPWFDSourceEntropy AND final promotion acceptance/replacement discipline",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "two_lines": read_json(TWO_LINES),
        "rks_rnrs": read_json(RKS_RNRS),
        "rks_promotion": read_json(RKS_PROMOTION),
        "exactuv_attack": read_json(EXACTUV_ATTACK),
        "exactuv_terminal": read_json(EXACTUV_TERMINAL),
        "clean_support": read_json(CLEAN_SUPPORT),
        "clean_normal": read_json(CLEAN_NORMAL),
        "fulls_match": read_json(FULLS_MATCH),
        "fulls_remainder": read_json(FULLS_REMAINDER),
        "dstructure_split": read_json(DSTRUCTURE_SPLIT),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_two_replacement_lines_after_rnrs_exactuv_sync_router",
        "status": "two_lines_synced_rkslog_closed_exactuv_and_completed_kls_open",
        "previous_internal_rks_log_open_superseded": True,
        "rks_log_author_side_closed": data["rks_rnrs"].get(
            "self_contained_rks_log_reciprocal_kloosterman_tail_log4_input_closed"
        )
        is True,
        "latest_internal_self_contained_math_input": "ExactCleanCoreFullSNonAPWFDSourceEntropy",
        "latest_internal_support_form": "ActualNoncanonicalExactUVSupportLowerBound",
        "latest_internal_layer_transfer_input": "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn",
        "latest_external_no_blackbox_input": "ModulusDependentCompletedFullSKLSInput OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof",
        "external_lemma_conditional_package": "AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "RNRS/Rudnev 回填后，上一层两条替代线中的 RKS-log open 标记已经过期。"
            "内部自足线的最新源侧真硬点是 ExactCleanCoreFullSNonAPWFDSourceEntropy，"
            "其支撑形态为 ActualNoncanonicalExactUVSupportLowerBound，下一层需证明 "
            "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn。外部无黑箱线的标准形是 "
            "ModulusDependentCompletedFullSKLSInput 或同对象的精确主来源/新自守 dispersion 证明。"
            "外部引理版仍只是在接受外部输入和 DStructure 独立验收时条件闭合。"
        ),
        "rows": rows,
        "source_status_snapshot": {
            "two_lines_status": data["two_lines"].get("status"),
            "rks_rnrs_status": data["rks_rnrs"].get("status"),
            "rks_promotion_status": data["rks_promotion"].get("status"),
            "exactuv_attack_status": data["exactuv_attack"].get("status"),
            "exactuv_terminal_status": data["exactuv_terminal"].get("status"),
            "clean_support_status": data["clean_support"].get("status"),
            "clean_normal_status": data["clean_normal"].get("status"),
            "fulls_match_status": data["fulls_match"].get("status"),
            "fulls_remainder_status": data["fulls_remainder"].get("status"),
            "dstructure_split_status": data["dstructure_split"].get("status"),
        },
        "source_hashes": source_hashes(),
    }


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出 Markdown 判定表。"""
    lines = [
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    lines = [
        "# Prime Matrix 两条替代线 RNRS/ExactUV 同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"previous_internal_rks_log_open_superseded={fmt_bool(payload['previous_internal_rks_log_open_superseded'])}",
        f"rks_log_author_side_closed={fmt_bool(payload['rks_log_author_side_closed'])}",
        f"latest_internal_self_contained_math_input={payload['latest_internal_self_contained_math_input']}",
        f"latest_internal_support_form={payload['latest_internal_support_form']}",
        f"latest_internal_layer_transfer_input={payload['latest_internal_layer_transfer_input']}",
        f"latest_external_no_blackbox_input={payload['latest_external_no_blackbox_input']}",
        f"external_lemma_conditional_package={payload['external_lemma_conditional_package']}",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 2. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 两条线的最新标准形",
        "",
        "外部引理版条件闭合包：",
        "",
        "```text",
        payload["external_lemma_conditional_package"],
        "```",
        "",
        "无黑箱外部版：",
        "",
        "```text",
        payload["latest_external_no_blackbox_input"],
        "```",
        "",
        "内部自足版源侧标准形：",
        "",
        "```text",
        payload["latest_internal_self_contained_math_input"],
        payload["latest_internal_support_form"],
        payload["latest_internal_layer_transfer_input"],
        "```",
        "",
        "## 4. 状态快照",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in payload["source_status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
