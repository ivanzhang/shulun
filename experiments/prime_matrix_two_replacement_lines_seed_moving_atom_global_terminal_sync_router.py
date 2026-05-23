#!/usr/bin/env python3
"""生成两条替代线 seed/moving-atom/global-terminal 同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_seed_moving_atom_global_terminal_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

EXACTUV_SOURCE = DOCS / "prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier-router.json"
MOVING_ATOM_GLOBAL = DOCS / "prime-matrix-strict-moving-atom-to-global-terminal-router.json"
MOVING_ATOM_PACKET = DOCS / "prime-matrix-strict-moving-atom-terminal-packet-frontier-router.json"
PAIR_ENERGY = DOCS / "prime-matrix-strict-independent-pair-energy-attack-router.json"
GLOBAL_BOUNDARY = DOCS / "prime-matrix-global-terminal-family-boundary-router.json"
GLOBAL_SPLIT = DOCS / "prime-matrix-global-terminal-family-exclusion-split-router.json"
ACYCLIC_TERMINAL_SATURATION = DOCS / "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json"
HIGH_TAIL_RECONCILIATION = DOCS / "prime-matrix-strict-high-tail-corpus-reconciliation-router.json"
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
ACYCLIC_SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
PAIR_L2 = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
LARGE_PAIR_PACKET = "RateBearingLargePairAtomPacketExclusion"
GLOBAL_TERMINAL = "GlobalPDECorSparseTerminalExclusion"
MODEL_DPRC = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE_SELF = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
PDEC_OR_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
NONRECURSIVE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
SAME_SET_PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，便于证书显式暴露缺口。"""
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
        EXACTUV_SOURCE,
        MOVING_ATOM_GLOBAL,
        MOVING_ATOM_PACKET,
        PAIR_ENERGY,
        GLOBAL_BOUNDARY,
        GLOBAL_SPLIT,
        ACYCLIC_TERMINAL_SATURATION,
        HIGH_TAIL_RECONCILIATION,
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


def gate_state(doc: dict[str, Any], gate: str) -> tuple[bool, bool]:
    """从 rows/gates 中读取 closed/proved。"""
    for key in ("rows", "gates"):
        for item in doc.get(key, []):
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


def previous_source_basis() -> str:
    """上一层内部源侧标准形。"""
    return f"{ACYCLIC_SEED} AND {MOVING_ATOM}"


def terminal_basis_after_moving_atom_sync() -> str:
    """moving atom 接回全局终端后的内部活动基。"""
    return f"{ACYCLIC_SEED} AND {GLOBAL_TERMINAL} AND {MODEL_DPRC}"


def strict_self_contained_basis() -> str:
    """严格自足版保留 Rate 与 DStructure 的完整基。"""
    return (
        f"{terminal_basis_after_moving_atom_sync()} AND {RATE} AND {DSTRUCTURE_SELF}"
    )


def terminal_saturation_basis() -> str:
    """展开全局终端家族后的当前饱和基。"""
    return (
        f"({NONRECURSIVE_BREAKER} OR {SAME_SET_PDEC_SCOPE} OR {NEW_JOINT}) "
        f"AND {MODEL_DPRC} AND {RATE} AND {DSTRUCTURE_ACCEPT}"
    )


def build_payload() -> dict[str, Any]:
    """构造同步证书 payload。"""
    exactuv = read_json(EXACTUV_SOURCE)
    moving_global = read_json(MOVING_ATOM_GLOBAL)
    moving_packet = read_json(MOVING_ATOM_PACKET)
    pair_energy = read_json(PAIR_ENERGY)
    global_boundary = read_json(GLOBAL_BOUNDARY)
    global_split = read_json(GLOBAL_SPLIT)
    acyclic_saturation = read_json(ACYCLIC_TERMINAL_SATURATION)
    high_tail = read_json(HIGH_TAIL_RECONCILIATION)

    source_frontier_imported = (
        exactuv.get("latest_internal_source_hardpoint") == previous_source_basis()
        and exactuv.get("row_column_unconditional_closed") is False
    )
    moving_global_imported = (
        moving_global.get("terminal_gap_before_router") == previous_source_basis()
        and moving_global.get("terminal_gap_after_router")
        == terminal_basis_after_moving_atom_sync()
        and moving_global.get("strict_moving_atom_boundary_closed") is True
    )
    moving_packet_imported = (
        moving_packet.get("next_direct_attack_target")
        == "RateBearingMovingAtomTerminalPacketExclusionWithExplicitDPRC"
        and moving_packet.get("actual_noncanonical_clean_core_moving_atom_exclusion_proved")
        is False
    )
    pair_route_deduped = (
        pair_energy.get("internal_obligation_before_router") == PAIR_L2
        and pair_energy.get("internal_obligation_after_router") == LARGE_PAIR_PACKET
        and pair_energy.get("rate_bearing_large_pair_atom_packet_exclusion_proved")
        is False
    )
    global_boundary_imported = (
        global_boundary.get("current_terminal_instances_exhausted") is True
        and global_boundary.get("global_terminal_family_exclusion_closed") is False
    )
    global_split_imported = (
        global_split.get("closed_nonfinal_reductions") is True
        and global_split.get("self_contained_next_hardpoint") == PDEC_OR_KLS
    )
    acyclic_terminal_saturated = (
        acyclic_saturation.get("internal_terminal_cycle_obstruction_closed") is True
        and acyclic_saturation.get("strict_acyclic_terminal_family_proved") is False
    )
    high_tail_not_active = (
        high_tail.get("row_column_unconditional_closed") is False
        and "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000"
        not in terminal_basis_after_moving_atom_sync()
    )
    rate_pinned, _ = gate_state(moving_packet, "RateBearingRequirementPinned")
    _, global_terminal_proved = gate_state(moving_global, "GlobalTerminalCurrentCorpusProved")
    _, model_dprc_proved = gate_state(moving_global, "ExplicitModelGapDPRCCurrentCorpusProved")

    # 中文注释：本层只允许删除 moving atom 的“孤立硬点”地位，不允许删除全局终端或模型账本。
    moving_atom_isolated_removed = moving_global_imported and moving_packet_imported

    rows = [
        row(
            "ExactUVSourceFrontierImported",
            source_frontier_imported,
            source_frontier_imported,
            "上一层已把 ExactUV/source 三标签归一为无环源种子加 clean-core moving atom 排斥。",
            previous_source_basis(),
        ),
        row(
            "MovingAtomToGlobalTerminalImported",
            moving_global_imported,
            moving_global_imported,
            "strict moving-atom 证书说明：若 seed 下仍有 clean-core moving atom，则它必须进入全局 PDEC/sparse 终端并支付模型/DPRC 账本。",
            terminal_basis_after_moving_atom_sync(),
        ),
        row(
            "MovingAtomNoLongerIsolatedHardpoint",
            moving_atom_isolated_removed,
            moving_atom_isolated_removed,
            "moving atom 排斥不再作为孤立最终硬点；它被非循环接到 global terminal packet。",
            f"{GLOBAL_TERMINAL} AND {MODEL_DPRC}",
        ),
        row(
            "AcyclicSeedStillOpen",
            exactuv.get("acyclic_seed_current_corpus_proved") is False,
            False,
            "无环 pre-Cauchy noncanonical primitive source seed 尚未由当前材料证明。",
            ACYCLIC_SEED,
        ),
        row(
            "GlobalPDECSparseTerminalStillOpen",
            global_terminal_proved is False,
            False,
            "当前语料尚未全局排斥 persistent PDEC、ColumnCRT、SAE/LocalSurvivor 或 sparse terminal 家族。",
            GLOBAL_TERMINAL,
        ),
        row(
            "ExplicitModelGapDPRCStillOpen",
            model_dprc_proved is False,
            False,
            "模型余量与有限 DPRC 账本仍是独立未闭合账本。",
            MODEL_DPRC,
        ),
        row(
            "RatePreservationCarried",
            rate_pinned,
            False,
            "moving atom packet 仍需 log-power 速率保持；定性投影二分不能替代。",
            RATE,
        ),
        row(
            "PairMassRouteNotIndependentProof",
            pair_route_deduped,
            True,
            "ExactUV/pair-mass 支线不能独立闭合 source entropy；它下游压到 rate-bearing large-pair packet 或回到全局终端。",
            f"{ACYCLIC_SEED} AND {LARGE_PAIR_PACKET}",
        ),
        row(
            "GlobalTerminalBoundaryImported",
            global_boundary_imported,
            global_boundary_imported,
            "当前已物化局部 PDEC/LocalSurvivor/NC-BLK 前沿耗尽；剩余是全局终端家族排斥，不是局部样本补丁。",
            "GlobalTerminalFamilyExclusion",
        ),
        row(
            "GlobalTerminalSplitImported",
            global_split_imported,
            global_split_imported,
            "全局终端家族已拆成 PDEC-CAP 或内部 CleanKLS 大筛；最终晋级还保留 DStructure/Rankin 门。",
            f"{PDEC_OR_KLS} AND {DSTRUCTURE_ACCEPT}",
        ),
        row(
            "AcyclicTerminalSaturationImported",
            acyclic_terminal_saturated,
            False,
            "继续展开 strict acyclic terminal family 会饱和为非递归构造/同集 PDEC 作用域/新 joint 公式三臂，而非闭合证明。",
            terminal_saturation_basis(),
        ),
        row(
            "HighTailNoLongerActiveButSelfContainedPackageCarried",
            high_tail_not_active,
            False,
            "高段解析常数可被外部 Mertens/Dusart 移出活动硬点；严格自足仍需保留 zeta/Mertens 包时不得伪称终稿。",
            "self-contained high-tail package only if refusing external explicit estimates",
        ),
        row(
            "ExternalNoBlackboxFrontierCarried",
            exactuv.get("external_lemma_version_unconditional_closed") is False,
            False,
            "无黑箱外部版仍需同对象 Full-S theorem-match、actual source capacity 或 completed residue dispersion。",
            external_no_blackbox_basis(),
        ),
        row(
            "ExternalLemmaOnlyConditional",
            True,
            False,
            "外部引理版仍只在接受 FullS-KLS-ext 与 DStructure 独立验收时条件闭合；这不是完全无条件证明。",
            external_conditional_basis(),
        ),
        row(
            "InternalSelfContainedVersionClosed",
            False,
            False,
            "本层只同步并移位真硬点；未证明 seed、global terminal、DPRC/model、Rate 或自足 DStructure。",
            strict_self_contained_basis(),
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "没有把 moving atom 接回 global terminal 或外部条件接受写成目标命题无条件闭合。",
            "not closed",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_two_replacement_lines_seed_moving_atom_global_terminal_sync_router",
        "status": "two_replacement_lines_seed_moving_atom_global_terminal_synced_open",
        "previous_internal_source_hardpoint": previous_source_basis(),
        "moving_atom_isolated_hardpoint_removed": moving_atom_isolated_removed,
        "latest_internal_terminal_hardpoint": terminal_basis_after_moving_atom_sync(),
        "strict_self_contained_basis": strict_self_contained_basis(),
        "terminal_saturation_basis_if_unfolded": terminal_saturation_basis(),
        "acyclic_seed_current_corpus_proved": False,
        "moving_atom_exclusion_current_corpus_proved": False,
        "global_pdec_sparse_terminal_exclusion_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "external_lemma_conditional_basis": external_conditional_basis(),
        "latest_external_no_blackbox_hardpoint": external_no_blackbox_basis(),
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "ExactUV/source 非循环前沿的 `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn "
            "AND ActualNoncanonicalCleanCoreMovingAtomExclusion` 已与 strict moving-atom/global-terminal "
            "证书同步：moving atom 排斥不再是孤立硬点；若 seed 下仍存在 clean-core moving atom，"
            "它必须进入 GlobalPDECorSparseTerminalExclusion 并支付 ExplicitModelGapAndFiniteDPRCLedger。"
            " 因而最新内部活动基变为 AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger；严格自足版还保留 "
            "RatePreservationLedger_FOR_moving_atom_packet 与 SelfContainedDStructureTailLog4FiniteRankinReplacementPackage。"
            " ExactUV/pair-mass 支线不能作为独立闭合证明，因为它下游压到 rate-bearing large-pair packet "
            "或回到全局终端。外部引理版仍只是条件闭合，目标命题仍未无条件闭合。"
        ),
        "rows": rows,
        "source_status_snapshot": {
            "exactuv_source_status": exactuv.get("status"),
            "moving_atom_global_status": moving_global.get("status"),
            "moving_atom_packet_status": moving_packet.get("status"),
            "pair_energy_status": pair_energy.get("status"),
            "global_boundary_status": global_boundary.get("status"),
            "global_split_status": global_split.get("status"),
            "acyclic_terminal_saturation_status": acyclic_saturation.get("status"),
            "high_tail_reconciliation_status": high_tail.get("status"),
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
        "# Prime Matrix 两条替代线 seed/moving-atom/global-terminal 同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"moving_atom_isolated_hardpoint_removed={fmt_bool(payload['moving_atom_isolated_hardpoint_removed'])}",
        f"acyclic_seed_current_corpus_proved={fmt_bool(payload['acyclic_seed_current_corpus_proved'])}",
        f"moving_atom_exclusion_current_corpus_proved={fmt_bool(payload['moving_atom_exclusion_current_corpus_proved'])}",
        f"global_pdec_sparse_terminal_exclusion_proved={fmt_bool(payload['global_pdec_sparse_terminal_exclusion_proved'])}",
        f"explicit_model_gap_and_finite_dprc_ledger_proved={fmt_bool(payload['explicit_model_gap_and_finite_dprc_ledger_proved'])}",
        f"rate_preservation_ledger_proved={fmt_bool(payload['rate_preservation_ledger_proved'])}",
        f"external_lemma_version_unconditional_closed={fmt_bool(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 最新两线边界",
        "",
        "上一层内部源侧基：",
        "",
        "```text",
        payload["previous_internal_source_hardpoint"],
        "```",
        "",
        "moving atom 接回全局终端后的内部活动基：",
        "",
        "```text",
        payload["latest_internal_terminal_hardpoint"],
        "```",
        "",
        "严格自足版保留为：",
        "",
        "```text",
        payload["strict_self_contained_basis"],
        "```",
        "",
        "若继续展开终端家族，当前饱和基为：",
        "",
        "```text",
        payload["terminal_saturation_basis_if_unfolded"],
        "```",
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
        "## 4. 非循环纪律",
        "",
        "本证书只允许从 ExactUV/source 非循环前沿正向导入 strict moving-atom/global-terminal 归约。"
        " 它删除的是 moving atom 作为孤立出口的地位，不删除无环源种子、全局终端排斥、模型/DPRC、Rate 或 DStructure 门。"
        " ExactUV/pair-mass 支线若要继续使用，必须提供独立 pair energy 或 large-pair packet 排斥，不能回证 source entropy。",
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
