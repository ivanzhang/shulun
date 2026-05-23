#!/usr/bin/env python3
"""生成两条替代线 ExactUV/source 非循环前沿证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_exactuv_source_noncycle_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier-router.json

输出：
  data/prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier-router.json
  docs/monograph/prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier-router.md
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

SLUG = "prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

RKS_RNRS_SYNC = DOCS / "prime-matrix-two-replacement-lines-rks-log-rnrs-version-reconciliation-router.json"
EXACT_LAYER_KLS = DOCS / "prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack-router.json"
DEEP_TERMINAL = DOCS / "prime-matrix-two-replacement-lines-deep-terminal-sync-router.json"
LATEST_TRUE = DOCS / "prime-matrix-two-replacement-lines-latest-true-remainder-sync-router.json"
EXACT_UV_TERMINAL = DOCS / "prime-matrix-exact-uv-support-terminal-attack-router.json"
CLEAN_EXACT_ENTROPY = DOCS / "prime-matrix-clean-core-exact-entropy-atom-router.json"
CLEAN_SUPPORT = DOCS / "prime-matrix-clean-core-support-incidence-attack-router.json"
CLEAN_LAYER = DOCS / "prime-matrix-clean-core-layer-transfer-path-router.json"
CLEAN_SOURCE_LOOP = DOCS / "prime-matrix-clean-core-source-loop-cut-router.json"
CLEAN_MOVING_ATOM = DOCS / "prime-matrix-clean-core-moving-atom-sharp-input-router.json"
STRICT_SOURCE_BRIDGE = DOCS / "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json"
STRICT_PAIR_MASS = DOCS / "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"

ACCEPTED_FULLS = "AcceptedFullSKLSExtExternalContract"
DSTRUCTURE_ACCEPT = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
FULLS_MATCH = "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch"
FULLS_CAPACITY = "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput"
NEW_DISPERSION = "NewAutomorphicDispersionProof"
C_DEP_SPECTRAL = "CDependentResidueWeightSpectralCancellationInput"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
EXACT_ENTROPY = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
EXACT_UV = "ActualNoncanonicalExactUVSupportLowerBound"
LAYER_TRANSFER = "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn"
ORIGIN_LEDGER = "CleanCoreOriginalCoefficientGenerationLedgerAndReturn"
ACYCLIC_SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
PAIR_L2 = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
MODEL_GATE = "HighSegmentModelGapAlpha043C3AnalyticLedger"
PDEC_RATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE_SELF = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，避免脚本硬失败。"""
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
    """列出直接依赖文件。"""
    return [
        RKS_RNRS_SYNC,
        EXACT_LAYER_KLS,
        DEEP_TERMINAL,
        LATEST_TRUE,
        EXACT_UV_TERMINAL,
        CLEAN_EXACT_ENTROPY,
        CLEAN_SUPPORT,
        CLEAN_LAYER,
        CLEAN_SOURCE_LOOP,
        CLEAN_MOVING_ATOM,
        STRICT_SOURCE_BRIDGE,
        STRICT_PAIR_MASS,
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


def row_state(doc: dict[str, Any], gate: str) -> tuple[bool, bool]:
    """读取某个 gate 的 closed/proved 状态。"""
    for item in doc.get("rows", []):
        if item.get("gate") == gate:
            return item.get("closed") is True, item.get("proved") is True
    return False, False


def external_conditional_basis() -> str:
    """外部引理条件版基。"""
    return f"{ACCEPTED_FULLS} AND {DSTRUCTURE_ACCEPT}"


def external_no_blackbox_basis() -> str:
    """无黑箱外部版基。"""
    return (
        f"({FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_DISPERSION} "
        f"OR {C_DEP_SPECTRAL} OR {EXTERNAL_DIBFI}) AND {DSTRUCTURE_ACCEPT}"
    )


def internal_source_basis() -> str:
    """内部自足源侧最窄基。"""
    return f"{ACYCLIC_SEED} AND {MOVING_ATOM}"


def internal_self_contained_basis() -> str:
    """内部自足全局基，保留并行模型、PDEC、Rate 和 DStructure 门。"""
    return (
        f"{internal_source_basis()} AND {MODEL_GATE} AND {PDEC_RATE} "
        f"AND {RATE} AND {DSTRUCTURE_SELF}"
    )


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    rks = read_json(RKS_RNRS_SYNC)
    exact_layer = read_json(EXACT_LAYER_KLS)
    deep_terminal = read_json(DEEP_TERMINAL)
    latest_true = read_json(LATEST_TRUE)
    exact_uv = read_json(EXACT_UV_TERMINAL)
    clean_entropy = read_json(CLEAN_EXACT_ENTROPY)
    clean_support = read_json(CLEAN_SUPPORT)
    clean_layer = read_json(CLEAN_LAYER)
    source_loop = read_json(CLEAN_SOURCE_LOOP)
    moving_atom = read_json(CLEAN_MOVING_ATOM)
    strict_bridge = read_json(STRICT_SOURCE_BRIDGE)
    pair_mass = read_json(STRICT_PAIR_MASS)

    rks_removed = (
        rks.get("latest_rks_log_open_flag_superseded_by_rnrs") is True
        and rks.get("rks_log_current_active_obstruction") is False
    )
    exactuv_terminal_open = row_state(exact_uv, "ExactUVSupportCurrentCorpusProved") == (False, False)
    entropy_to_support = row_state(clean_entropy, "CleanCoreTerminalSupportIncidenceCurrentCorpusProved") == (
        False,
        False,
    )
    support_to_layer = row_state(clean_support, "CleanCoreExactLayerAdmissionCurrentCorpusProved") == (
        False,
        False,
    )
    layer_to_path = row_state(clean_layer, "CleanCorePathPartitionCurrentCorpusProved") == (
        False,
        False,
    )
    source_loop_detected = row_state(source_loop, "CleanCoreSourceLoopDetected") == (True, True)
    acyclic_seed_open = row_state(source_loop, "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn") == (
        False,
        False,
    )
    moving_atom_open = row_state(moving_atom, "CleanCoreMovingAtomExclusionCurrentCorpusProved") == (
        False,
        False,
    )
    pair_mass_deduped = pair_mass.get("normal_form_after_router") == f"{ACYCLIC_SEED} AND {EXACT_ENTROPY}"
    strict_exactuv_guard = strict_bridge.get("next_internal_attack_if_exact_entropy") == f"{ACYCLIC_SEED} AND {PAIR_L2}"
    external_conditional = latest_true.get("external_lemma_version_closed_conditionally") is True
    external_no_blackbox_open = latest_true.get("external_no_blackbox_version_closed") is False
    exact_layer_origin = exact_layer.get("latest_internal_minimal_author_task") == ORIGIN_LEDGER
    deep_signed_cycle_cut = deep_terminal.get("internal_self_contained_version_closed") is False

    rows = [
        row(
            "RKSRNRSReconciliationImported",
            rks_removed,
            rks_removed,
            "RKS-log 最新 open 标记已由 RNRS/Rudnev 同对象同参数非循环导入删除。",
            "move to ExactUV/source frontier",
        ),
        row(
            "ExactUVSourceThreeLabelsOrdered",
            exactuv_terminal_open and entropy_to_support and support_to_layer,
            False,
            "Exact entropy、ExactUV support 与 clean-core layer transfer 不是三个独立出口，而是同一源侧链条的连续下钻。",
            f"{EXACT_ENTROPY} -> {EXACT_UV} -> {LAYER_TRANSFER}",
        ),
        row(
            "LayerTransferToOriginLedgerImported",
            exact_layer_origin and layer_to_path,
            False,
            "clean-core 层承认/非零转移需先给 Cauchy 前 actual alpha/delta 原始生成表。",
            ORIGIN_LEDGER,
        ),
        row(
            "SourceLoopCutImported",
            source_loop_detected,
            True,
            "origin ledger 到 constructor/formula/emitter 再回 origin ledger 的旧路线是闭环，不能当证明。",
            ACYCLIC_SEED,
        ),
        row(
            "AcyclicSeedStillOpen",
            acyclic_seed_open,
            False,
            "当前材料尚未提交不依赖 downstream payment skeleton 的无环 pre-Cauchy noncanonical primitive source seed。",
            ACYCLIC_SEED,
        ),
        row(
            "ExactUVPairEnergyGuardImported",
            strict_exactuv_guard,
            False,
            "若 exact entropy 继续走 ExactUV/pair-mass 路线，必须独立证明 pair L2/max-atom 界，不能用 entropy 结论回证。",
            f"{ACYCLIC_SEED} AND {PAIR_L2}",
        ),
        row(
            "PairMassNotSeparateTerminal",
            pair_mass_deduped,
            True,
            "pair-mass 分散失败去重为同一 clean-core moving atom/exact entropy 终端，不新增第四类硬点。",
            f"{ACYCLIC_SEED} AND {MOVING_ATOM}",
        ),
        row(
            "MovingAtomExclusionStillOpen",
            moving_atom_open,
            False,
            "当前材料仍未排斥通过所有回流测试后的 actual noncanonical clean-core moving same-(u,v) 大原子。",
            MOVING_ATOM,
        ),
        row(
            "InternalSourceHardpointNormalized",
            True,
            False,
            "内部源侧非循环标准形收窄为无环源种子加 clean-core moving atom 排斥；ExactUV/entropy/layer-transfer 只是上层接口。",
            internal_source_basis(),
        ),
        row(
            "ExternalNoBlackboxFrontierCarried",
            external_no_blackbox_open,
            False,
            "无黑箱外部版仍需同对象 Full-S theorem-match、actual source capacity 新定理或 completed residue dispersion。",
            external_no_blackbox_basis(),
        ),
        row(
            "ExternalLemmaOnlyConditional",
            external_conditional,
            False,
            "接受 FullS-KLS-ext 与 DStructure 独立验收时外部引理版作者侧条件闭合；这不是完全无条件闭合。",
            external_conditional_basis(),
        ),
        row(
            "SignedCycleCutAndTailGatesCarried",
            deep_signed_cycle_cut,
            False,
            "更深 Phi-LPF/signed-table 链已阻断自证环；模型、PDEC/CleanKLS、Rate 与 DStructure 门仍需保留。",
            f"{MODEL_GATE} AND {PDEC_RATE} AND {RATE} AND {DSTRUCTURE_SELF}",
        ),
        row(
            "InternalSelfContainedVersionClosed",
            False,
            False,
            "本层只完成硬点归一化；未证明无环源种子、moving atom 排斥或并行模型/Rate/DStructure 门。",
            internal_self_contained_basis(),
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "没有把外部条件接受、等价命名或回边同步写成目标命题无条件证明。",
            "not closed",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_two_replacement_lines_exactuv_source_noncycle_frontier_router",
        "status": "two_replacement_lines_exactuv_source_frontier_reduced_to_seed_and_moving_atom_open",
        "rks_log_current_active_obstruction": False,
        "exactuv_entropy_layer_labels_are_ordered_interfaces": True,
        "source_loop_cut_closed": source_loop_detected,
        "acyclic_seed_current_corpus_proved": False,
        "moving_atom_exclusion_current_corpus_proved": False,
        "latest_internal_source_hardpoint": internal_source_basis(),
        "latest_internal_exactuv_route_basis": f"{ACYCLIC_SEED} AND {PAIR_L2}",
        "latest_external_no_blackbox_hardpoint": external_no_blackbox_basis(),
        "external_lemma_conditional_basis": external_conditional_basis(),
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_basis": internal_self_contained_basis(),
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "RKS/RNRS 调和后，三条 ExactUV/source 标签不能再并列循环使用："
            "ExactCleanCoreFullSNonAPWFDSourceEntropy 下钻到 ActualNoncanonicalExactUVSupportLowerBound，"
            "再下钻到 CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn；该链继续收缩到 "
            "CleanCoreOriginalCoefficientGenerationLedgerAndReturn，但 origin/constructor/formula/emitter "
            "旧路形成来源闭环。当前内部源侧真剩余归一为 AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn "
            "AND ActualNoncanonicalCleanCoreMovingAtomExclusion。外部无黑箱线仍需同对象 Full-S theorem-match、"
            "actual source capacity 或 completed residue dispersion；外部引理版仍只是条件闭合。目标命题仍未完全无条件闭合。"
        ),
        "rows": rows,
        "source_status_snapshot": {
            "rks_rnrs_sync_status": rks.get("status"),
            "exact_layer_kls_status": exact_layer.get("status"),
            "deep_terminal_status": deep_terminal.get("status"),
            "latest_true_status": latest_true.get("status"),
            "exact_uv_terminal_status": exact_uv.get("status"),
            "clean_exact_entropy_status": clean_entropy.get("status"),
            "clean_support_status": clean_support.get("status"),
            "clean_layer_status": clean_layer.get("status"),
            "clean_source_loop_status": source_loop.get("status"),
            "clean_moving_atom_status": moving_atom.get("status"),
            "strict_source_bridge_status": strict_bridge.get("status"),
            "strict_pair_mass_status": pair_mass.get("status"),
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
        "# Prime Matrix 两条替代线 ExactUV/source 非循环前沿证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"rks_log_current_active_obstruction={fmt_bool(payload['rks_log_current_active_obstruction'])}",
        f"exactuv_entropy_layer_labels_are_ordered_interfaces={fmt_bool(payload['exactuv_entropy_layer_labels_are_ordered_interfaces'])}",
        f"source_loop_cut_closed={fmt_bool(payload['source_loop_cut_closed'])}",
        f"acyclic_seed_current_corpus_proved={fmt_bool(payload['acyclic_seed_current_corpus_proved'])}",
        f"moving_atom_exclusion_current_corpus_proved={fmt_bool(payload['moving_atom_exclusion_current_corpus_proved'])}",
        f"latest_internal_source_hardpoint={payload['latest_internal_source_hardpoint']}",
        f"external_lemma_version_unconditional_closed={fmt_bool(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 两条线的当前标准形",
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
        "内部源侧非循环标准形：",
        "",
        "```text",
        payload["latest_internal_source_hardpoint"],
        "```",
        "",
        "若坚持 ExactUV/pair-mass 路线，独立输入为：",
        "",
        "```text",
        payload["latest_internal_exactuv_route_basis"],
        "```",
        "",
        "内部自足全局基保留为：",
        "",
        "```text",
        payload["internal_self_contained_basis"],
        "```",
        "",
        "## 4. 非循环纪律",
        "",
        "本证书切断 origin ledger -> constructor -> formula -> emitter -> origin ledger 的来源闭环。"
        " 任何后续证明必须从 pre-Cauchy 源种子或独立 moving-atom 排斥正向进入，不能用 ExactUV/entropy 结论回证其输入。",
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
