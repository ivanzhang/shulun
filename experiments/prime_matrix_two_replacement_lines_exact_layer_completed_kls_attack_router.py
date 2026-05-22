#!/usr/bin/env python3
"""生成两条替代线 exact-layer/completed-KLS 深攻证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_exact_layer_completed_kls_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack-router.json

输出：
  data/prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack-router.json
  docs/monograph/prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack-router.md
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

SLUG = "prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

RNRS_SYNC = DOCS / "prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync-router.json"
CLEAN_SUPPORT = DOCS / "prime-matrix-clean-core-support-incidence-attack-router.json"
CLEAN_LAYER = DOCS / "prime-matrix-clean-core-layer-transfer-path-router.json"
CLEAN_FIREWALL = DOCS / "prime-matrix-clean-core-path-source-firewall-router.json"
CLEAN_PRECAUCHY = DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json"
COMPLETED_KLS = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
THREE_ATOMS = DOCS / "prime-matrix-three-final-atoms-hard-attack-router.json"
DSTRUCTURE_SPLIT = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"
RKS_PROMOTION = DOCS / "prime-matrix-strict-rks23-final-promotion-audit-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据；缺失时返回空证据。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希，便于审稿复核证据来源。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """格式化布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def dependency_paths() -> list[Path]:
    """列出本证书依赖文件。"""
    return [
        RNRS_SYNC,
        CLEAN_SUPPORT,
        CLEAN_LAYER,
        CLEAN_FIREWALL,
        CLEAN_PRECAUCHY,
        COMPLETED_KLS,
        THREE_ATOMS,
        DSTRUCTURE_SPLIT,
        RKS_PROMOTION,
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
    """生成两条替代线深攻判定表。"""
    return [
        row(
            "RNRSExactUVSyncImported",
            data["rnrs_sync"].get("previous_internal_rks_log_open_superseded") is True,
            data["rnrs_sync"].get("rks_log_author_side_closed") is True,
            "RNRS/Rudnev 回填已移除 RKS-log 作为最新内部阻断，真剩余回到 ExactUV/source entropy。",
            "attack exact-layer/source-origin ledger",
        ),
        row(
            "InternalLayerAdmissionToPathPartition",
            data["clean_layer"].get("clean_core_layer_transfer_path_boundary_closed") is True,
            False,
            "clean-core exact 层承认和非零转移可归约为有限路径签名、同路径非零和 thin return。",
            "CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn",
        ),
        row(
            "PathPartitionNeedsPreCauchySourceLaw",
            data["clean_firewall"].get("clean_core_path_source_firewall_boundary_closed") is True,
            False,
            "路径签名必须作用在 Cauchy/dispersion 前的 actual alpha/delta 系数公式上。",
            "CleanCorePreCauchyCoefficientSourceLawAndReturn",
        ),
        row(
            "PreCauchySourceLawToOriginGenerationLedger",
            data["clean_precauchy"].get("clean_core_precauchy_source_law_atom_boundary_closed") is True,
            False,
            "pre-Cauchy 来源律的最小自足证据是原始生成表：同一 formal unit、branch key、符号、local factor 与命名回流。",
            "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
        ),
        row(
            "CanonicalAndGenericWFDShortcutsRejected",
            True,
            True,
            "canonical 来源账本只覆盖 canonical-source 分支，generic WFD 只给形式分解；二者不能导入 noncanonical clean-core。",
            "prove actual noncanonical origin ledger or switch to external spectral input",
        ),
        row(
            "ExternalCompletionToCDependentResidueSpectralInput",
            data["completed_kls"].get("completed_weight_spectral_gap_closed") is False
            and data["completed_kls"].get("terminal_gap_after_router")
            == "CDependentResidueWeightSpectralCancellationInput",
            False,
            "full-S completion 后长度问题已消失，剩余是 B_{c,x}=sum_k beta_{x+kc} 的模数依赖、未中心化 residue 权重谱抵消。",
            "CDependentResidueWeightSpectralCancellationInput",
        ),
        row(
            "PointwiseWeilLargeSieveFlatResidueShortcutsRejected",
            True,
            True,
            "点态 Weil+L2 只到自然/root 尺度，普通大筛缺 c,h dispersion 结构，平坦 residue/免费中心化与 no-projection 目标冲突。",
            "new Kuznetsov/DI-BFI dispersion theorem for c-dependent completed weights",
        ),
        row(
            "ExternalLemmaVersionOnlyConditionallyClosed",
            True,
            False,
            "接受外部 FullS-KLS 合同与 DStructure/Rankin 独立验收时，外部引理版逻辑闭合；这些输入不是当前语料库内已证明事实。",
            "AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "NoBlackboxExternalVersionStillOpen",
            True,
            False,
            "无黑箱外部版必须给精确主来源 theorem-match，或证明同对象的新自守/dispersion 定理；泛称 FI/DI/BFI/Maynard 不足。",
            "CDependentResidueWeightSpectralCancellationInput OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof",
        ),
        row(
            "InternalSelfContainedVersionStillOpen",
            True,
            False,
            "内部自足版必须先提交 clean-core 原始生成账本，再处理最终晋级门/替代包；Phi-LPF exact count 不能给正性。",
            "CleanCoreOriginalCoefficientGenerationLedgerAndReturn AND final promotion gate or self-contained replacement",
        ),
        row(
            "DStructurePromotionGateCarried",
            True,
            False,
            "DStructure/Tail-log4/finite Rankin 独立接受仍是最终晋级门；作者侧替代包也必须通过最终推广审计。",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinReplacementPackage",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把两条替代线继续压到最小可审稿接口，没有无条件证明目标命题。",
            "external spectral theorem or internal origin ledger plus promotion discipline",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "rnrs_sync": read_json(RNRS_SYNC),
        "clean_support": read_json(CLEAN_SUPPORT),
        "clean_layer": read_json(CLEAN_LAYER),
        "clean_firewall": read_json(CLEAN_FIREWALL),
        "clean_precauchy": read_json(CLEAN_PRECAUCHY),
        "completed_kls": read_json(COMPLETED_KLS),
        "three_atoms": read_json(THREE_ATOMS),
        "dstructure_split": read_json(DSTRUCTURE_SPLIT),
        "rks_promotion": read_json(RKS_PROMOTION),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_two_replacement_lines_exact_layer_completed_kls_attack_router",
        "status": "two_replacement_lines_reduced_to_origin_ledger_and_c_dependent_completed_spectral_input_open",
        "latest_internal_chain": [
            "ExactCleanCoreFullSNonAPWFDSourceEntropy",
            "ActualNoncanonicalExactUVSupportLowerBound",
            "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn",
            "CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn",
            "CleanCorePreCauchyCoefficientSourceLawAndReturn",
            "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
        ],
        "latest_internal_minimal_author_task": "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
        "latest_external_chain": [
            "ModulusDependentCompletedFullSKLSInput",
            "CDependentResidueWeightSpectralCancellationInput",
        ],
        "latest_external_no_blackbox_task": "CDependentResidueWeightSpectralCancellationInput OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof",
        "external_spectral_required_clauses": [
            "completed full-S non-AP WFD object after s mod c completion",
            "c-dependent completed residue weights B_{c,x}=sum_k beta_{x+k c}",
            "well-factorable lambda_c and smooth omega_h over c,h",
            "no APSourceLift, no centering, no projection loss",
            "de-completion, gcd, smoothing, and endpoint errors inside B(A)",
            "NaturalWFDScale/log^A(P) saving for every fixed A",
        ],
        "internal_origin_ledger_required_clauses": [
            "same formal unit before Cauchy, Type/Fourier, completion, and pushforward",
            "complete list of actual alpha/delta summands with source class, branch key, u/v map, sign, and local factor",
            "polylog branch/path budget or named return for path overbudget",
            "primitive nonzero/sign split on each complete branch key",
            "thin, rejected, missing-source, and cancellation failures return to PDEC/SAE/ColumnCRT/CleanKLS or external spectral input",
        ],
        "external_lemma_version_status": "conditionally_closed_only_under_accepted_fullskls_ext_and_independent_dstructure_acceptance",
        "no_blackbox_external_version_closed": False,
        "internal_self_contained_version_closed": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "本层继续深攻两条替代线。内部线中，CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn "
            "不是单个 incidence 或 squarefree 估计，而是必须下钻到 CleanCoreOriginalCoefficientGenerationLedgerAndReturn："
            "在 Cauchy 前给出 actual clean-core alpha/delta 的原始生成表、branch key、非零/无抵消和命名回流。"
            "外部无黑箱线中，ModulusDependentCompletedFullSKLSInput 继续压成 "
            "CDependentResidueWeightSpectralCancellationInput：要处理依赖 c 的完成 residue 权重 B_{c,x}，"
            "并保持 no AP-source lift、no projection、de-completion 误差与任意 log-saving。"
            "因此外部引理版仍只是条件闭合；内部自足版和无黑箱外部版均未无条件闭合。"
        ),
        "rows": rows,
        "source_status_snapshot": {
            "rnrs_sync_status": data["rnrs_sync"].get("status"),
            "clean_support_status": data["clean_support"].get("status"),
            "clean_layer_status": data["clean_layer"].get("status"),
            "clean_firewall_status": data["clean_firewall"].get("status"),
            "clean_precauchy_status": data["clean_precauchy"].get("status"),
            "completed_kls_status": data["completed_kls"].get("status"),
            "three_atoms_status": data["three_atoms"].get("status"),
            "dstructure_split_status": data["dstructure_split"].get("status"),
            "rks_promotion_status": data["rks_promotion"].get("status"),
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


def list_block(items: list[str]) -> list[str]:
    """生成 Markdown 列表。"""
    return [f"- `{item}`" for item in items]


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    lines = [
        "# Prime Matrix 两条替代线 exact-layer/completed-KLS 深攻证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"latest_internal_minimal_author_task={payload['latest_internal_minimal_author_task']}",
        f"latest_external_no_blackbox_task={payload['latest_external_no_blackbox_task']}",
        f"external_lemma_version_status={payload['external_lemma_version_status']}",
        f"no_blackbox_external_version_closed={fmt_bool(payload['no_blackbox_external_version_closed'])}",
        f"internal_self_contained_version_closed={fmt_bool(payload['internal_self_contained_version_closed'])}",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 2. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 内部线链条",
        "",
        "最新内部自足链条被压成：",
        "",
        "```text",
        *payload["latest_internal_chain"],
        "```",
        "",
        "最小作者侧任务 `CleanCoreOriginalCoefficientGenerationLedgerAndReturn` 要求：",
        "",
        *list_block(payload["internal_origin_ledger_required_clauses"]),
        "",
        "## 4. 外部无黑箱线链条",
        "",
        "最新外部无黑箱链条被压成：",
        "",
        "```text",
        *payload["latest_external_chain"],
        "```",
        "",
        "`CDependentResidueWeightSpectralCancellationInput` 必须同时保留：",
        "",
        *list_block(payload["external_spectral_required_clauses"]),
        "",
        "## 5. 状态快照",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in payload["source_status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            "## 6. 依赖哈希",
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
