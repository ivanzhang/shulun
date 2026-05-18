#!/usr/bin/env python3
"""生成 strict NCBLK/source anti-atom 最新前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_ncblk_source_antiatom_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json

输出：
  data/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-ledger.json
  docs/monograph/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json
  docs/monograph/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-ncblk-source-antiatom-frontier-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.json",
    "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json",
    "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-independent-precauchy-identity-taxonomy-router.json",
    "prime-matrix-counterexample-moving-block-terminal-router.json",
    "prime-matrix-strict-moving-atom-to-global-terminal-router.json",
    "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json",
    "prime-matrix-strict-source-declaration-downstream-sync-router.json",
]

NCBLK = "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
FORWARD_SOURCE_ROOT = "ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn"
GLOBAL_TERMINAL = "GlobalPDECorSparseTerminalExclusion"
INDEPENDENT_ID = "IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn"
MOVING_SPREAD = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
EARLY_ZERO_PACKAGE = "EarlyZeroTerminalExclusionPackage"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
EXACTUV_LANE = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；缺失时返回空对象，缺失不当作证明。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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
    """登记脚本与上游证书哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成本轮前沿同步判定表。"""
    pair_frontier_ok = data["pair"].get("next_direct_attack_target") == NCBLK
    ncblk_dedup_ok = data["ncblk"].get("terminal_gap_before_router") == NCBLK
    seed_split_ok = data["support_seed"].get("terminal_gap_after_router", "").startswith(SEED)
    zero_row_nogo_ok = data["zero_seed"].get("terminal_gap_after_router") == INDEPENDENT_ID
    taxonomy_ok = data["taxonomy"].get("terminal_gap_after_router") == MOVING_SPREAD
    moving_block_ok = data["moving_block"].get("terminal_gap_after_router", "").startswith(EARLY_ZERO_PACKAGE)
    moving_atom_global_ok = data["moving_atom_global"].get("terminal_gap_after_router", "").startswith(SEED)
    source_packet_open = data["source_packet"].get("common_packet_proved") is False
    downstream_sync_ok = (
        data["source_downstream"].get("next_direct_attack_target") == BUILTIN_PAIRING
        and data["source_downstream"].get("parallel_direct_attack_target") == EXACTUV_LANE
    )

    return [
        row(
            "LatestPairEnergyFrontierImported",
            pair_frontier_ok,
            False,
            "上一轮 pair-energy 对角剥离后，直接主攻被钉为 NCBLK/source anti-atom。",
            NCBLK,
        ),
        row(
            "NCBLKDedupRouterImported",
            ncblk_dedup_ok,
            False,
            "既有 strict NCBLK 路由已说明该标签不是新无名终端；actual 失败会标准化为 moving atom 并回全局终端。",
            f"{SEED} AND {GLOBAL_TERMINAL} AND {MODEL}",
        ),
        row(
            "GenericWFDAntiAtomNoGoPreserved",
            data["ncblk"].get("generic_wfd_antiatom_no_go_imported") is True,
            True,
            "generic WFD/formal Type/Fourier 反原子被 moving-delta 模型阻断，不能作为自足证明。",
            "必须使用 actual acyclic source，或转外部谱线。",
        ),
        row(
            "ActualSourceSupportSeedSplitImported",
            seed_split_ok,
            False,
            "ExactUV/actual-source 支撑不是单个引理；它至少需要无环 pre-Cauchy seed 与 exact-pair 分散。",
            f"{SEED} AND ExactUVPairMassDispersionOrMaxAtomBoundLedger",
        ),
        row(
            "ZeroRowCannotSupplySeed",
            zero_row_nogo_ok,
            True,
            "早期零行反例只给 unsigned CRT 覆盖/payment 数据，不能反向生成 signed pre-Cauchy source seed。",
            INDEPENDENT_ID,
        ),
        row(
            "IndependentIdentityTaxonomyClosed",
            taxonomy_ok,
            True,
            "独立 pre-Cauchy 算术来源恒等式的合法来源类已穷尽；没有隐藏第四路线。",
            MOVING_SPREAD,
        ),
        row(
            "MovingBlockReturnImported",
            moving_block_ok,
            True,
            "actual noncanonical moving-block spread 若有低维签名则进 PDEC/SAE/ColumnCRT；无签名则回早期零行终端包。",
            f"{EARLY_ZERO_PACKAGE} AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock",
        ),
        row(
            "MovingAtomGlobalTerminalSyncImported",
            moving_atom_global_ok,
            False,
            "strict moving-atom 回流已把 clean-core moving atom 接到全局 PDEC/sparse 终端与模型/DPRC 账本。",
            f"{SEED} AND {GLOBAL_TERMINAL} AND {MODEL}",
        ),
        row(
            "CommonSourcePacketStillOpen",
            source_packet_open,
            False,
            "若继续正向构造 source root，仍需 common declaration packet；当前语料没有该 packet。",
            COMMON_PACKET,
        ),
        row(
            "SourceDeclarationDownstreamSplitImported",
            downstream_sync_ok,
            False,
            "common packet 的下游字段已同步为 built-in signed pairing 与 ExactUV entropy/fiber 两条子线。",
            f"{BUILTIN_PAIRING} AND {EXACTUV_LANE}",
        ),
        row(
            "NCBLKNoLongerBestNamedTarget",
            pair_frontier_ok and ncblk_dedup_ok and zero_row_nogo_ok and taxonomy_ok,
            True,
            "继续把 NCBLK 当作主攻名会遮蔽真正首字段；当前应攻 forward source-root packet 或命名终端排斥。",
            f"{FORWARD_SOURCE_ROOT} OR ({GLOBAL_TERMINAL} AND {HIGH_MODEL}) OR ({PDEC_SCOPE} AND {HIGH_MODEL})",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步和压窄 NCBLK/source anti-atom 前沿；source-root、全局终端、PDEC scope、高段模型、Rate 与 DStructure 仍未证明。",
            f"(({FORWARD_SOURCE_ROOT}) OR ({GLOBAL_TERMINAL} AND {HIGH_MODEL}) OR ({PDEC_SCOPE} AND {HIGH_MODEL})) AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书主体。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "pair": load_json("prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.json"),
        "ncblk": load_json("prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json"),
        "kz": load_json("prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json"),
        "support_seed": load_json("prime-matrix-strict-actual-source-support-seed-router.json"),
        "zero_seed": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "taxonomy": load_json("prime-matrix-independent-precauchy-identity-taxonomy-router.json"),
        "moving_block": load_json("prime-matrix-counterexample-moving-block-terminal-router.json"),
        "moving_atom_global": load_json("prime-matrix-strict-moving-atom-to-global-terminal-router.json"),
        "source_packet": load_json("prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json"),
        "source_downstream": load_json("prime-matrix-strict-source-declaration-downstream-sync-router.json"),
    }
    hardpoint_after = (
        f"({FORWARD_SOURCE_ROOT}) OR "
        f"({GLOBAL_TERMINAL} AND {HIGH_MODEL}) OR "
        f"({PDEC_SCOPE} AND {HIGH_MODEL})"
    )
    strict_basis = f"({hardpoint_after}) AND {RATE} AND {DSTRUCTURE}"
    forward_packet_fields = [
        "declaration line before Cauchy/payment",
        "primitive summand rows with branch/sign/local-factor data",
        "built-in signed word/coefficient pairing",
        "actual source-domain entropy and fixed exact (u,v) fiber bound",
        "same formal-unit exact-pair no-heavy or L2 energy ledger",
        "no downstream recovery and named return partition",
    ]
    result = {
        "certificate_type": "prime_matrix_strict_ncblk_source_antiatom_frontier_sync_router",
        "status": "ncblk_source_antiatom_synced_to_forward_source_root_or_global_terminal_open",
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "ncblk_proved": False,
        "forward_source_root_packet_proved": False,
        "global_pdec_sparse_terminal_exclusion_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": data["pair"].get("hardpoint_after_router", ""),
        "terminal_gap_after_ncblk_router": data["ncblk"].get("terminal_gap_after_router", ""),
        "hardpoint_after_router": hardpoint_after,
        "strict_active_basis_after_router": strict_basis,
        "next_direct_attack_target": FORWARD_SOURCE_ROOT,
        "parallel_attack_targets": [
            GLOBAL_TERMINAL,
            PDEC_SCOPE,
            HIGH_MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "forward_source_root_packet_fields": forward_packet_fields,
        "decision_rows": build_rows(data),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把上一轮 pair-energy 对角剥离留下的 NCBLK/source anti-atom 与仓库已有的 "
            "actual-source seed、假设零行 seed no-go、pre-Cauchy 来源分类、moving-block 回流和 "
            "source-declaration 下游同步合并。结论是：NCBLK/source anti-atom 仍未证明，但它也不应继续作为"
            "最深主攻名。generic 反原子路线已被 moving-delta 阻断；actual 路线必须先给出不从 downstream "
            "反推的 forward pre-Cauchy source-root packet。若该 source-root 不能正向给出，既有分类把失败"
            "推回 moving-block/global PDEC-sparse 终端；并行仍保留 direct PDEC 同集作用域与高段模型余量。"
            "行/列命题仍未无条件闭合。"
        ),
    }
    return result


def write_json(path: Path, obj: dict[str, Any]) -> None:
    """写入稳定排序 JSON。"""
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix strict NCBLK/source anti-atom 前沿同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"ncblk_proved={fmt_bool(result['ncblk_proved'])}",
        f"forward_source_root_packet_proved={fmt_bool(result['forward_source_root_packet_proved'])}",
        f"global_pdec_sparse_terminal_exclusion_proved={fmt_bool(result['global_pdec_sparse_terminal_exclusion_proved'])}",
        f"high_segment_model_gap_alpha043_c3_analytic_ledger_proved={fmt_bool(result['high_segment_model_gap_alpha043_c3_analytic_ledger_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
        "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom",
        "  -> generic WFD anti-atom no-go",
        "  -> actual route needs acyclic pre-Cauchy source seed",
        "  -> zero-row data cannot supply signed seed",
        "  -> independent pre-Cauchy identity taxonomy",
        "  -> actual moving-block spread / NC-BLK",
        "  -> moving-block/global PDEC-sparse terminal return",
        "  -> forward source-root packet or named terminal exclusion",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["decision_rows"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )

    lines.extend([
        "",
        "## 3. Forward source-root packet 字段",
        "",
        "| field | role |",
        "| --- | --- |",
    ])
    roles = [
        "禁止从 payment/零行覆盖图反推 source。",
        "给出实际 primitive emitter 的可审查行。",
        "关闭 signed payload 的首个非循环生产字段。",
        "支撑 ExactUV 与 source anti-atom 的真实对象。",
        "排除单 exact-pair delta 重原子。",
        "把缺字段、循环、payload 泄漏、fiber collapse 全部命名回流。",
    ]
    for field, role_text in zip(result["forward_source_root_packet_fields"], roles):
        lines.append(f"| `{cell(field)}` | {cell(role_text)} |")

    lines.extend([
        "",
        "## 4. 最新剩余",
        "",
        "```text",
        result["hardpoint_after_router"],
        "```",
        "",
        "严格活动基：",
        "",
        "```text",
        result["strict_active_basis_after_router"],
        "```",
        "",
        "下一直接主攻：",
        "",
        "```text",
        result["next_direct_attack_target"],
        "```",
        "",
        "并行保留：",
        "",
        "```text",
        " AND ".join(result["parallel_attack_targets"]),
        "```",
        "",
        "## 5. 诚实边界",
        "",
        "- 本证书不证明 NCBLK/source anti-atom，也不证明 forward source-root packet。",
        "- 它只把 NCBLK 名称下的现有路线同步到底：generic 路线阻断，actual 路线必须先交 source-root packet。",
        "- 全局 PDEC/sparse 终端、direct PDEC 同集作用域、高段模型余量、RatePreservation 与 DStructure/Rankin 仍未闭合。",
        "",
        "## 6. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ])
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、ledger 与 Markdown 文档。"""
    result = build_result()
    write_json(OUT_LEDGER, result)
    write_json(OUT_JSON, result)
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
