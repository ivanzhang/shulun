#!/usr/bin/env python3
"""生成两条替代线最新真剩余同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_latest_true_remainder_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-latest-true-remainder-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-latest-true-remainder-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-latest-true-remainder-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-latest-true-remainder-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-latest-true-remainder-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-deep-terminal-sync-router.json"
FULLS_MATRIX = DOCS / "prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json"
FULLS_REMAINDER = DOCS / "prime-matrix-fulls-theorem-match-true-remainder-cut-router.json"
FULLS_KLS_ACCEPT = DOCS / "prime-matrix-fulls-kls-ext-acceptance-match-audit.json"
DSTRUCTURE_AUTHOR = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

OFFDIAG_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-router.json"
PURE_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync-router.json"
FERRERS_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-rebase-sync-router.json"
NO_SWAP_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync-router.json"
EDGE_FIELD_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync-router.json"
TRACE_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-router.json"
PAYLOAD_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-router.json"
PAYLOAD_LOOP_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-rebase-sync-router.json"
FRESH_JOINT_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-rebase-sync-router.json"
MOVING_BLOCK_REBASE = DOCS / "prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-rebase-sync-router.json"
TERMINAL_HIGH_MODEL = DOCS / "prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync-router.json"
KUZNETSOV_HIGH_MODEL = DOCS / "prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync-router.json"
STRICT_KZ_ATOM = DOCS / "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json"
STRICT_KZ_TERMINAL = DOCS / "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据；缺失时返回空对象，避免旧快照中断。"""
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
    """列出本证书依赖文件。"""
    return [
        PREVIOUS,
        FULLS_MATRIX,
        FULLS_REMAINDER,
        FULLS_KLS_ACCEPT,
        DSTRUCTURE_AUTHOR,
        OFFDIAG_REBASE,
        PURE_REBASE,
        FERRERS_REBASE,
        NO_SWAP_REBASE,
        EDGE_FIELD_REBASE,
        TRACE_REBASE,
        PAYLOAD_REBASE,
        PAYLOAD_LOOP_REBASE,
        FRESH_JOINT_REBASE,
        MOVING_BLOCK_REBASE,
        TERMINAL_HIGH_MODEL,
        KUZNETSOV_HIGH_MODEL,
        STRICT_KZ_ATOM,
        STRICT_KZ_TERMINAL,
        PAPER,
    ]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖哈希，便于复核。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """整理外部引理版与内部自足版的最新真剩余。"""
    return [
        row(
            "DeepTerminalFrontierImported",
            data["previous"].get("status") == "two_replacement_lines_synced_to_deep_terminal_basis_open",
            True,
            "上一层已把外部线钉到 ExternalDIBFIKuznetsovDispersionTheoremMatch，把内部线钉到 offdiagonal first-seed signed table。",
            "继续展开，避免停在旧标签。",
        ),
        row(
            "ExternalTheoremMatchMatrixImported",
            data["fulls_matrix"].get("status")
            == "fulls_nonap_wfd_primary_sources_screened_exact_contract_or_new_theorem_remains",
            True,
            "Full-S non-AP WFD 对象、权重、窗口、模数、投影和强度已逐项筛查。",
            "PrimarySourceDerivationClosed remains false",
        ),
        row(
            "ExternalTrueRemainderCutImported",
            data["fulls_remainder"].get("status")
            == "ap_lift_filtered_ncblk_expanded_true_remainder_external_or_actual_source_core_open",
            True,
            "APSourceLift 和 generic anti-atom 已被过滤；外部无黑箱线只剩主来源定理匹配或 actual source support/capacity 新定理。",
            "(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "ExternalLemmaVersionConditionPinned",
            True,
            False,
            "接受外部黑箱时，FullS-KLS-ext 与当前对象逐项匹配；但它仍是外部合同，不是从 DI/BFI 主来源逐行推出。",
            "AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "OffDiagonalSeedStrippedToEdgeTrace",
            data["trace"].get("latest_constructor_basis_replaces_signed_atom_fields_with_new_payload_or_exits")
            or data["trace"].get("latest_basis_replaces_signed_atom_fields_with_new_payload_or_exits"),
            False,
            "offdiagonal seed 经 tuple、pure pair、Ferrers、no-swap、edge-local field-cut 和 trace-sync，所有无符号 label 已用尽。",
            "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR named exits",
        ),
        row(
            "PayloadSourceEntropyLoopCutImported",
            data["payload_loop"].get("constructor_payload_source_entropy_loop_detected") is True,
            True,
            "new payload 若靠 source entropy 证明会回到 joint declaration，形成 constructor payload/source-entropy 自证环。",
            "FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop",
        ),
        row(
            "FreshJointReducedToMovingBlock",
            data["fresh_joint"].get("fresh_joint_declaration_reduced_to_moving_block") is True,
            False,
            "新鲜 joint declaration 不能走 constructor antisplit 旧路，必须成为独立算术恒等式；现有分类把它压到 actual moving-block/NC-BLK。",
            "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn",
        ),
        row(
            "MovingBlockTerminalSplitImported",
            data["moving_block"].get("constructor_moving_block_unnamed_exit_removed") is True,
            True,
            "moving-block/NC-BLK 不能作为无名终端，已压到 PDEC/CleanKLS 和模型账本。",
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger",
        ),
        row(
            "SelfContainedKuznetsovDLSRouteExhausted",
            data["strict_kz_terminal"].get("kz_abcd_internal_spine_closed") is True
            or data["strict_kz_terminal"].get("kz_e_reduced_to_acyclic_ncblk") is True,
            False,
            "KZ-A--D 已关闭；KZ-E well-factorable dispersion log-saving 不由裸谱大筛自动给出，回到 acyclic NC-BLK/source anti-atom 或终端家族。",
            "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom",
        ),
        row(
            "BetaSieveSawtoothTailCarried",
            True,
            False,
            "高段模型余量同步到自足 Rosser-Iwaniec beta-sieve 权重、99% 主系数显式误差与 exact sawtooth 余项界。",
            "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 AND ExactResidueWeightedFloorSawtoothTenPercentBound",
        ),
        row(
            "DStructureRankinIndependentGateCarried",
            True,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是独立晋级门；作者侧同步不能自行删除该门。",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层同步最新真剩余和循环障碍；不宣称外部引理版或内部自足版已无条件闭合。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "fulls_matrix": read_json(FULLS_MATRIX),
        "fulls_remainder": read_json(FULLS_REMAINDER),
        "fulls_kls_accept": read_json(FULLS_KLS_ACCEPT),
        "dstructure_author": read_json(DSTRUCTURE_AUTHOR),
        "offdiag": read_json(OFFDIAG_REBASE),
        "pure": read_json(PURE_REBASE),
        "ferrers": read_json(FERRERS_REBASE),
        "no_swap": read_json(NO_SWAP_REBASE),
        "edge": read_json(EDGE_FIELD_REBASE),
        "trace": read_json(TRACE_REBASE),
        "payload": read_json(PAYLOAD_REBASE),
        "payload_loop": read_json(PAYLOAD_LOOP_REBASE),
        "fresh_joint": read_json(FRESH_JOINT_REBASE),
        "moving_block": read_json(MOVING_BLOCK_REBASE),
        "terminal_high_model": read_json(TERMINAL_HIGH_MODEL),
        "kuznetsov_high_model": read_json(KUZNETSOV_HIGH_MODEL),
        "strict_kz_atom": read_json(STRICT_KZ_ATOM),
        "strict_kz_terminal": read_json(STRICT_KZ_TERMINAL),
    }
    rows = build_rows(data)
    external_no_blackbox = (
        "(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR "
        "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR "
        "NewAutomorphicDispersionProof) AND "
        "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
    )
    external_lemma = (
        "AcceptedFullSKLSExtExternalContract AND "
        "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
    )
    internal_basis = (
        "((AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom "
        "OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate "
        "OR NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage "
        "OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) "
        "AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix "
        "AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 "
        "AND ExactResidueWeightedFloorSawtoothTenPercentBound) "
        "AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward "
        "AND JointEmitterPrepushforwardWordCoefficientIdentityLedger "
        "AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger "
        "AND ActualEmitterSourceDomainEntropyLedger "
        "AND ExactUVMapFixedPairPolylogFiberBoundLedger "
        "AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward "
        "AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger "
        "AND CompletePrimitiveEmitterKeyPartitionLedger "
        "AND FixedKeyExactUVLocalMultiplicityO1Ledger "
        "AND RatePreservationLedger_FOR_moving_atom_packet "
        "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
    )
    return {
        "certificate_type": "prime_matrix_two_replacement_lines_latest_true_remainder_sync_router",
        "status": "two_replacement_lines_latest_true_remainders_synced_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "frontier_sync_only": True,
        "external_lemma_version_closed_conditionally": True,
        "external_lemma_version_condition": external_lemma,
        "external_lemma_unconditional_from_current_corpus": False,
        "external_no_blackbox_version_closed": False,
        "external_no_blackbox_latest_basis": external_no_blackbox,
        "internal_self_contained_closed": False,
        "internal_self_contained_latest_basis": internal_basis,
        "latest_internal_primary_attack_target": (
            "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom "
            "AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth"
        ),
        "latest_external_primary_attack_target": (
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR "
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput"
        ),
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "本层把上一层两个真接口继续接入仓库中已经存在的更深证书。外部线中，"
            "ExternalDIBFIKuznetsovDispersionTheoremMatch 不再作为粗标签停留；无黑箱版必须给出"
            "同对象 Full-S non-AP WFD 的主来源 theorem-match，或证明 actual noncanonical source "
            "support/capacity 新定理。若接受外部引理，则外部引理版只在 "
            "AcceptedFullSKLSExtExternalContract 与 DStructure/Rankin 独立验收同时成立时条件闭合。"
            "内部线中，offdiagonal signed seed 被剥到 edge trace/new payload/source entropy，再由"
            " payload-loop cut 与 fresh-joint taxonomy 压到 moving-block/NC-BLK；继续走自足 KZ/DLS "
            "时 KZ-A--D 已用尽，KZ-E 回到 acyclic NC-BLK/source anti-atom，并且 beta-sieve/sawtooth "
            "尾段、source/joint、signed survival、row-mass、complete/fixed-key、Rate 与 DStructure 门仍需保留。"
            "本层不宣称无条件闭合。"
        ),
        "rows": rows,
        "source_status_snapshot": {key: value.get("status") for key, value in data.items()},
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
        "# Prime Matrix 两条替代线最新真剩余同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"latest_external_primary_attack_target={payload['latest_external_primary_attack_target']}",
        f"latest_internal_primary_attack_target={payload['latest_internal_primary_attack_target']}",
        f"external_lemma_version_closed_conditionally={fmt_bool(payload['external_lemma_version_closed_conditionally'])}",
        f"external_no_blackbox_version_closed={fmt_bool(payload['external_no_blackbox_version_closed'])}",
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 2. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 外部引理版与无黑箱外部版",
        "",
        "外部引理版条件基：",
        "",
        "```text",
        payload["external_lemma_version_condition"],
        "```",
        "",
        "无黑箱外部版最新基：",
        "",
        "```text",
        payload["external_no_blackbox_latest_basis"],
        "```",
        "",
        "## 4. 内部自足版",
        "",
        "最新内部自足基：",
        "",
        "```text",
        payload["internal_self_contained_latest_basis"],
        "```",
        "",
        "关键结论：Phi-LPF/CRT/Eratosthenes 精确计数只关闭无符号 support/capacity，不能支付 KZ-E、NC-BLK/source anti-atom、signed survival、row-mass 或 beta-sieve/sawtooth。",
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
