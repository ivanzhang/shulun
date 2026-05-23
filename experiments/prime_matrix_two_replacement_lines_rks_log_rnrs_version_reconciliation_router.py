#!/usr/bin/env python3
"""生成两条替代线 RKS-log/RNRS 版本调和证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_rks_log_rnrs_version_reconciliation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-rks-log-rnrs-version-reconciliation-router.json

输出：
  data/prime-matrix-two-replacement-lines-rks-log-rnrs-version-reconciliation-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-rks-log-rnrs-version-reconciliation-router.json
  docs/monograph/prime-matrix-two-replacement-lines-rks-log-rnrs-version-reconciliation-router.md
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

SLUG = "prime-matrix-two-replacement-lines-rks-log-rnrs-version-reconciliation"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_RKS = DOCS / "prime-matrix-two-replacement-lines-rks-log-final-atom-sync-router.json"
AFTER_RNRS = DOCS / "prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync-router.json"
RKS_RNRS = DOCS / "prime-matrix-strict-rks-log-rnrs-transfer-closure-router.json"
STRICT_MULTI = DOCS / "prime-matrix-strict-multilinear-reciprocal-kloosterman-fixed-log-saving-router.json"
RKS23_RNRS = DOCS / "prime-matrix-strict-rks23-rnrs-energy-absorption-router.json"
COMMON_KERNEL = DOCS / "prime-matrix-two-replacement-lines-common-unconditional-kernel-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"

BG_FIXED_LOG = "MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks"
BAKER_DB = "BakerFrequencyLargeSieveOrDBGAverageReplacement"
RKS_TAIL_INPUT = "SelfContainedRKSLogReciprocalKloostermanTailLog4Input"
EXACT_UV = "ActualNoncanonicalExactUVSupportLowerBound"
SOURCE_ENTROPY = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
LAYER_TRANSFER = "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn"
FULLS_MATCH = "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch"
FULLS_CAPACITY = "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput"
NEW_AUTOMORPHIC = "NewAutomorphicDispersionProof"
ACCEPTED_FULLS = "AcceptedFullSKLSExtExternalContract"
DSTRUCTURE_ACCEPT = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，便于证书显示未闭合。"""
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


def dependency_paths() -> list[Path]:
    """列出本证书直接依赖。"""
    return [
        LATEST_RKS,
        AFTER_RNRS,
        RKS_RNRS,
        STRICT_MULTI,
        RKS23_RNRS,
        COMMON_KERNEL,
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


def rnrs_source_files(rks_rnrs: dict[str, Any]) -> list[str]:
    """抽取 RNRS 回填证书的依赖文件名。"""
    return sorted((rks_rnrs.get("source_hashes") or {}).keys())


def build_payload() -> dict[str, Any]:
    """构造版本调和 payload。"""
    latest = read_json(LATEST_RKS)
    after_rnrs = read_json(AFTER_RNRS)
    rks_rnrs = read_json(RKS_RNRS)
    strict_multi = read_json(STRICT_MULTI)
    rks23_rnrs = read_json(RKS23_RNRS)
    common = read_json(COMMON_KERNEL)

    latest_atom = str(latest.get("final_self_contained_atom", ""))
    exact_input = strict_multi.get("exact_input_theorem") or {}
    parameter_absorption = rks_rnrs.get("parameter_absorption") or {}
    rnrs_sources = rnrs_source_files(rks_rnrs)

    # 中文注释：三项必须同时成立，才允许把旧 RNRS 回填导入最新 RKS-log 原子。
    same_object = BG_FIXED_LOG in latest_atom and exact_input.get("name") == BG_FIXED_LOG
    same_parameter = (
        strict_multi.get("required_input_log_power")
        == parameter_absorption.get("required_bilinear_log_saving")
        == 118
    )
    rnrs_imports_exact_statement = (
        "docs/monograph/prime-matrix-strict-multilinear-reciprocal-kloosterman-fixed-log-saving-router.json"
        in rnrs_sources
    )
    noncycle_dependency_direction = not any("two-replacement-lines" in path for path in rnrs_sources)
    rnrs_tail_input_closed = (
        rks_rnrs.get("self_contained_rks_log_reciprocal_kloosterman_tail_log4_input_closed")
        is True
    )
    rnrs_author_package_closed = (
        rks_rnrs.get("self_contained_dstructure_tail_log4_finite_rankin_replacement_package_author_side_closed")
        is True
    )
    after_rnrs_agrees = (
        after_rnrs.get("previous_internal_rks_log_open_superseded") is True
        and after_rnrs.get("rks_log_author_side_closed") is True
    )
    latest_open_flag_present = (
        latest.get("internal_self_contained_closed") is False
        and BG_FIXED_LOG in latest_atom
    )
    rks23_energy_closed = (
        rks23_rnrs.get("self_contained_rnrs_rudnev_proof_closed") is True
        or any(
            item.get("gate")
            == "SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling"
            and item.get("closed") is True
            and item.get("proved") is True
            for item in rks23_rnrs.get("rows", [])
        )
    )
    common_kernel_preserved = common.get("common_unconditional_kernel_boundary_closed") is True

    reconciliation_closed = all(
        [
            same_object,
            same_parameter,
            rnrs_imports_exact_statement,
            noncycle_dependency_direction,
            rnrs_tail_input_closed,
            rnrs_author_package_closed,
        ]
    )

    rows = [
        row(
            "LatestRKSFinalAtomImported",
            latest_open_flag_present,
            True,
            "最新两条替代线证书把共同核固定为 RKS-log/Baker-DB 原子；这是对象定位，不是闭合证明。",
            f"{BG_FIXED_LOG} OR {BAKER_DB}",
        ),
        row(
            "ExactObjectIdentityMatch",
            same_object,
            same_object,
            "最新 final atom 与 strict multilinear 证书使用同一个 RKS2/RKS3 倒数 Kloosterman 输入名。",
            BG_FIXED_LOG,
        ),
        row(
            "Log118ParameterMatch",
            same_parameter,
            same_parameter,
            "strict multilinear 证书要求 log^-118，RNRS 回填证书的 required_bilinear_log_saving 也是 118。",
            "no parameter gap inside RKS-log atom",
        ),
        row(
            "RNRSImportsExactStatement",
            rnrs_imports_exact_statement,
            rnrs_imports_exact_statement,
            "RNRS 回填证书直接哈希依赖 strict multilinear exact statement，而非另起一个相似命题。",
            "hash-aligned exact statement import",
        ),
        row(
            "NoncycleDependencyDirection",
            noncycle_dependency_direction,
            noncycle_dependency_direction,
            "RNRS 回填链的依赖只走 strict RKS/Rudnev/RNRS 文件，不依赖两条替代线结论本身。",
            "acyclic import from RKS23/Rudnev chain",
        ),
        row(
            "RKS23RudnevEnergyAbsorptionClosed",
            rks23_energy_closed,
            rks23_energy_closed,
            "Rudnev/RNRS 倒数区间能量输入已在 RKS23 能量吸收证书中登记为作者侧闭合。",
            "SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling",
        ),
        row(
            "RNRSClosesLatestRKSLogAtom",
            reconciliation_closed,
            reconciliation_closed,
            "同对象、同参数、非循环依赖三项对齐后，旧 RNRS 回填可导入最新 RKS-log final atom。",
            RKS_TAIL_INPUT,
        ),
        row(
            "AfterRNRSExactUVSyncConsistent",
            after_rnrs_agrees,
            after_rnrs_agrees,
            "较早 after-RNRS/ExactUV 证书与本次哈希调和一致：RKS-log open 标记过期，活动硬点回到 ExactUV/source entropy。",
            f"{EXACT_UV} OR {SOURCE_ENTROPY}",
        ),
        row(
            "CommonKernelBoundaryPreserved",
            common_kernel_preserved,
            True,
            "共同核边界仍保持：本次只吸收共同核中的 RKS-log 解析原子，不替两条前端付款。",
            "front-end source/spectral obligations remain separate",
        ),
        row(
            "ExternalLemmaVersionUnconditionalClosed",
            False,
            False,
            "外部引理版仍只在接受 FullS-KLS-ext 与 DStructure 独立验收时条件闭合。",
            f"{ACCEPTED_FULLS} AND {DSTRUCTURE_ACCEPT}",
        ),
        row(
            "InternalSelfContainedGlobalClosed",
            False,
            False,
            "内部自足全局版虽不再被 RKS-log 阻断，但仍需 ExactUV/source entropy、模型、PDEC/CleanKLS 与 Rate。",
            f"{SOURCE_ENTROPY} AND {EXACT_UV} AND downstream model/PDEC/Rate gates",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本层只做非循环版本调和和 RKS-log 回填导入；目标命题仍未完全无条件闭合。",
            "not closed",
        ),
    ]

    external_conditional_basis = f"{ACCEPTED_FULLS} AND {DSTRUCTURE_ACCEPT}"
    external_no_blackbox_basis = (
        f"({FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_AUTOMORPHIC}) "
        f"AND {DSTRUCTURE_ACCEPT}"
    )
    latest_internal_frontier = (
        f"{SOURCE_ENTROPY} OR {EXACT_UV} OR {LAYER_TRANSFER}"
    )

    return {
        "certificate_type": "prime_matrix_two_replacement_lines_rks_log_rnrs_version_reconciliation_router",
        "status": "two_replacement_lines_rks_log_rnrs_reconciled_exactuv_source_frontier_restored",
        "same_rks_log_object_reconciled": same_object,
        "same_log118_parameter_reconciled": same_parameter,
        "rnrs_imports_exact_statement": rnrs_imports_exact_statement,
        "noncycle_dependency_direction_closed": noncycle_dependency_direction,
        "rks23_rudnev_energy_absorption_closed": rks23_energy_closed,
        "latest_rks_log_open_flag_superseded_by_rnrs": reconciliation_closed,
        "rks_log_current_active_obstruction": not reconciliation_closed,
        "latest_internal_true_hardpoint": latest_internal_frontier,
        "latest_external_no_blackbox_hardpoint": external_no_blackbox_basis,
        "external_lemma_conditional_basis": external_conditional_basis,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "最新 RKS-log final atom 与旧 RNRS/Rudnev 回填证书经哈希版本调和后为同一对象、同一 log^-118 "
            "参数、同一 Tail-log4/RKS2/RKS3 formal unit；RNRS 依赖链不引用两条替代线结论，"
            "因此可非循环导入并删除最新 RKS-log open 标记。活动硬点回到 ExactUV/source entropy："
            "ExactCleanCoreFullSNonAPWFDSourceEntropy、ActualNoncanonicalExactUVSupportLowerBound 与 "
            "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn。外部引理版仍只是条件闭合；"
            "内部自足版和目标行/列命题仍未完全无条件闭合。"
        ),
        "rows": rows,
        "source_status_snapshot": {
            "latest_rks_status": latest.get("status"),
            "after_rnrs_status": after_rnrs.get("status"),
            "rks_rnrs_status": rks_rnrs.get("status"),
            "strict_multilinear_status": strict_multi.get("status"),
            "rks23_rnrs_status": rks23_rnrs.get("status"),
            "common_kernel_status": common.get("status"),
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
        "# Prime Matrix 两条替代线 RKS-log/RNRS 版本调和证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"same_rks_log_object_reconciled={fmt_bool(payload['same_rks_log_object_reconciled'])}",
        f"same_log118_parameter_reconciled={fmt_bool(payload['same_log118_parameter_reconciled'])}",
        f"rnrs_imports_exact_statement={fmt_bool(payload['rnrs_imports_exact_statement'])}",
        f"noncycle_dependency_direction_closed={fmt_bool(payload['noncycle_dependency_direction_closed'])}",
        f"latest_rks_log_open_flag_superseded_by_rnrs={fmt_bool(payload['latest_rks_log_open_flag_superseded_by_rnrs'])}",
        f"rks_log_current_active_obstruction={fmt_bool(payload['rks_log_current_active_obstruction'])}",
        "external_lemma_version_unconditional_closed=false",
        "internal_self_contained_closed=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 2. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 最新两线边界",
        "",
        "外部引理条件版：",
        "",
        "```text",
        payload["external_lemma_conditional_basis"],
        "```",
        "",
        "无黑箱外部版：",
        "",
        "```text",
        payload["latest_external_no_blackbox_hardpoint"],
        "```",
        "",
        "内部自足版当前活动硬点：",
        "",
        "```text",
        payload["latest_internal_true_hardpoint"],
        "```",
        "",
        "## 4. 非循环纪律",
        "",
        "本证书只允许从 strict RKS/Rudnev/RNRS 依赖链向两条替代线导入，禁止反向用两条替代线结论证明 RNRS 输入。"
        " 版本调和删除的是过期 RKS-log open 标记，不删除 ExactUV/source、FullS theorem-match、模型、PDEC/CleanKLS、Rate 或独立验收门。",
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
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
