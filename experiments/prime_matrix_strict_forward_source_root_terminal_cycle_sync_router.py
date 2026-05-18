#!/usr/bin/env python3
"""生成 forward source-root 到终端容量环的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_forward_source_root_terminal_cycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json

输出：
  data/prime-matrix-strict-forward-source-root-terminal-cycle-sync-ledger.json
  docs/monograph/prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json
  docs/monograph/prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-forward-source-root-terminal-cycle-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json",
    "prime-matrix-strict-source-declaration-downstream-sync-router.json",
    "prime-matrix-strict-signed-lane-cycle-closure-router.json",
    "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json",
    "prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json",
    "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json",
    "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json",
    "prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json",
    "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json",
    "prime-matrix-strict-pointwise-primitive-kernel-table-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json",
    "prime-matrix-strict-alpha-carry-shell-congruence-formula-router.json",
    "prime-matrix-strict-alpha-anchor-collar-overload-return-router.json",
    "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json",
    "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json",
]

SOURCE_ROOT = "ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
KZ_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
KZ_DLS_NOCYCLE = "NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
GLOBAL_TERMINAL = "GlobalPDECorSparseTerminalExclusion"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
POINTWISE_KERNEL = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
SIGNED_LIFT = "AlphaFormulaSignedCoefficientLiftLedger"
OVERLOAD = "AlphaFormulaAnchorCollarOverloadNamedReturnLedger"


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


def get_any(obj: dict[str, Any], *paths: str) -> Any:
    """按候选路径读取上游字段，兼容顶层字段和嵌套 aggregate 字段。"""
    for path in paths:
        cur: Any = obj
        ok = True
        for part in path.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                ok = False
                break
        if ok:
            return cur
    return None


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
    """生成判定表。"""
    source_root_active = data["source_root"].get("next_direct_attack_target") == SOURCE_ROOT
    signed_cycle_closed = data["signed_cycle"].get("signed_lane_cycle_closed") is True
    new_primitive_absorbed = get_any(
        data["new_primitive"],
        "new_primitive_artifact_reduced_to_source_rank_atom",
        "aggregate.new_primitive_artifact_reduced_to_source_rank_atom",
    ) is True
    source_entropy_cycles = data["source_entropy"].get("seed_coordinate_source_cycle_detected") is True
    cyclecut_to_joint = (
        data["cyclecut"].get("next_direct_attack_target")
        == "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
    )
    antisplit_to_trace = data["antisplit"].get("built_in_pairing_reduced_to_branch_trace") is True
    source_rank_to_kernel = data["post_antisplit"].get("next_direct_attack_target") == ALPHA_ROW
    pointwise_split = data["pointwise"].get("next_direct_attack_target") == ALPHA_ROW
    unsigned_closed = data["unsigned"].get("alpha_row_unsigned_skeleton_router_closed") is True
    signed_lift_terminal = data["signed_lift_terminal"].get("signed_lift_branch_recycles_to_terminal_gap") is True
    carry_closed = data["carry"].get("alpha_formula_carry_shell_congruence_row_formula_proved") is True
    overload_schema_closed = data["overload"].get("alpha_formula_anchor_collar_overload_named_return_ledger_closed") is True
    terminal_split = data["terminal"].get("terminal_split_router_closed") is True
    clean_kls_to_ncblk = data["kz"].get("kz_e_reduced_to_ncblk_or_external") is True

    return [
        row(
            "ForwardSourceRootTargetActive",
            source_root_active,
            False,
            "上一轮把 NCBLK/source anti-atom 的 actual 路线压到 forward source-root packet。",
            SOURCE_ROOT,
        ),
        row(
            "SourceDeclarationDownstreamImported",
            data["downstream"].get("next_direct_attack_target") == "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows",
            False,
            "source-root 展开后进入 common packet 下游：signed pairing 与 ExactUV entropy/fiber 两线。",
            "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger",
        ),
        row(
            "SignedLaneCycleClosed",
            signed_cycle_closed,
            True,
            "built-in pairing、branch trace、payload origin 与 common packet 已闭成 signed-lane 自证环。",
            "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR terminal/PDEC/external input",
        ),
        row(
            "NewPrimitiveAbsorbedToSourceRank",
            new_primitive_absorbed,
            False,
            "new primitive 若要破环，必须携带 actual source-rank/no-collapse 包；它不是独立证明点。",
            "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger",
        ),
        row(
            "SourceEntropyCycleGuardImported",
            source_entropy_cycles,
            True,
            "source-domain entropy 下钻后进入 seed coordinate-source cycle，不能自证。",
            "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR terminal descent",
        ),
        row(
            "CycleCutTerminalDescentUnified",
            cyclecut_to_joint,
            False,
            "cycle-cut、terminal descent 与 PDEC 内部线被统一到 joint declaration line 或条件终端输入。",
            "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple",
        ),
        row(
            "AntiSplitTraceExactUVAtomized",
            antisplit_to_trace,
            False,
            "反分裂 built-in pairing 又回到 signed trace cycle；ExactUV 被拆成 signed row law、complete key 与 fixed-key multiplicity。",
            "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger",
        ),
        row(
            "SourceRankConvergesToPointwiseKernel",
            source_rank_to_kernel,
            False,
            "new primitive、terminal descent、source entropy 与 key/fiber 线汇到同 formal-unit 逐点 primitive alpha/delta 核表。",
            POINTWISE_KERNEL,
        ),
        row(
            "PointwiseKernelSplitImported",
            pointwise_split,
            False,
            "逐点核表已拆成 alpha row 发射、独立权重恒等式、同表 rank/multiplicity 三腿。",
            "AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows",
        ),
        row(
            "AlphaUnsignedSkeletonClosed",
            unsigned_closed and carry_closed,
            True,
            "source tuple、carry-shell、P 列距离和 layered-wheel 已给出 unsigned row skeleton。",
            "signed coefficient lift and overload return remain",
        ),
        row(
            "SignedLiftReturnsToTerminalGap",
            signed_lift_terminal,
            False,
            "signed lift 经 signed weight law 与 independent identity taxonomy 回到 moving-block/NCBLK，再回终端容量门。",
            f"{PDEC_CLEAN_KLS} AND {HIGH_MODEL}",
        ),
        row(
            "AnchorCollarOverloadReturnSchemaClosed",
            overload_schema_closed,
            True,
            "anchor-collar 过载没有专属第四出口，只能进入 PDEC/SAE/ColumnCRT/LocalSurvivor/CleanKLS 终端门。",
            f"{PDEC_CLEAN_KLS} AND {HIGH_MODEL}",
        ),
        row(
            "ForwardSourceRootSubsumedByTerminalCycle",
            source_root_active and signed_cycle_closed and new_primitive_absorbed and source_rank_to_kernel and signed_lift_terminal and overload_schema_closed,
            True,
            "当前语料中的 source-root 内部路线全部回到 signed/source-rank/alpha 终端环；source-root 不再是独立主攻名。",
            f"{PDEC_CLEAN_KLS} AND {HIGH_MODEL}",
        ),
        row(
            "TerminalSplitStillOpen",
            terminal_split,
            False,
            "PDEC/CleanKLS 终端已二分为 direct PDEC scope 或 clean Kuznetsov/DLS；两臂仍未证明。",
            f"{PDEC_SCOPE} OR {KZ_DLS}",
        ),
        row(
            "CleanKLSArmWouldCycleIfUsingNCBLKSourceRoot",
            clean_kls_to_ncblk,
            True,
            "CleanKLS/KZ-DLS 既有自足路线压到 NCBLK；若再用 source-root 线闭合，就回到本环。",
            KZ_DLS_NOCYCLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只封住 source-root 自足回环；direct PDEC scope、非循环 KZ/DLS、高段模型、Rate 与 DStructure 仍未证明。",
            f"({PDEC_SCOPE} OR {KZ_DLS_NOCYCLE}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书主体。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "source_root": load_json("prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json"),
        "downstream": load_json("prime-matrix-strict-source-declaration-downstream-sync-router.json"),
        "signed_cycle": load_json("prime-matrix-strict-signed-lane-cycle-closure-router.json"),
        "new_primitive": load_json("prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"),
        "source_entropy": load_json("prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json"),
        "cyclecut": load_json("prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json"),
        "antisplit_downstream": load_json("prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json"),
        "antisplit": load_json("prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json"),
        "post_antisplit": load_json("prime-matrix-strict-post-antisplit-source-rank-convergence-router.json"),
        "pointwise": load_json("prime-matrix-strict-pointwise-primitive-kernel-table-router.json"),
        "alpha": load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift_hardpoint": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "signed_lift_terminal": load_json("prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json"),
        "carry": load_json("prime-matrix-strict-alpha-carry-shell-congruence-formula-router.json"),
        "overload": load_json("prime-matrix-strict-alpha-anchor-collar-overload-return-router.json"),
        "terminal": load_json("prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"),
        "kz": load_json("prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json"),
    }
    hardpoint_after = f"({PDEC_SCOPE} OR {KZ_DLS_NOCYCLE}) AND {HIGH_MODEL}"
    strict_basis = f"{hardpoint_after} AND {RATE} AND {DSTRUCTURE}"
    result = {
        "certificate_type": "prime_matrix_strict_forward_source_root_terminal_cycle_sync_router",
        "status": "forward_source_root_internal_route_reduced_to_terminal_cycle_open",
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "forward_source_root_packet_proved": False,
        "forward_source_root_independent_after_router": False,
        "signed_lane_self_proof_eliminated": data["signed_cycle"].get("signed_lane_cycle_closed") is True,
        "source_rank_paths_converged_to_pointwise_kernel": data["post_antisplit"].get("all_internal_source_rank_routes_meet_at_pointwise_kernel_table") is True,
        "alpha_unsigned_skeleton_closed": data["unsigned"].get("alpha_row_unsigned_skeleton_router_closed") is True,
        "signed_lift_branch_recycles_to_terminal_gap": data["signed_lift_terminal"].get("signed_lift_branch_recycles_to_terminal_gap") is True,
        "anchor_collar_overload_return_schema_closed": data["overload"].get("alpha_formula_anchor_collar_overload_named_return_ledger_closed") is True,
        "direct_pdec_scope_match_proved": False,
        "noncircular_kuznetsov_dls_without_source_root_reuse_proved": False,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": data["source_root"].get("hardpoint_after_router", ""),
        "hardpoint_after_router": hardpoint_after,
        "strict_active_basis_after_router": strict_basis,
        "next_direct_attack_target": PDEC_SCOPE,
        "parallel_attack_targets": [KZ_DLS_NOCYCLE, HIGH_MODEL, RATE, DSTRUCTURE],
        "decision_rows": build_rows(data),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步直接攻击 `ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn`。"
            "把 common packet、signed-lane 闭环、new primitive/source-rank、cycle-cut/terminal descent、"
            "antisplit ExactUV 原子化、逐点 primitive 核表、alpha row unsigned skeleton、signed-lift 回流和 "
            "anchor-collar 过载回流全部同步后，source-root 在当前语料中没有留下独立非循环证明路线。"
            "signed 路线闭环；new primitive 与 terminal descent 汇到 source-rank/no-collapse；alpha 的 unsigned "
            "几何骨架已闭合，但 signed lift 与 overloading 都回到终端容量门。因而最新严格剩余从 source-root "
            "改写为 direct PDEC 同集作用域，或一个不再借用 NCBLK/source-root 的非循环 Kuznetsov/DLS 证明，"
            "并仍需高段模型、RatePreservation 与 DStructure/Rankin。行/列命题仍未无条件闭合。"
        ),
    }
    return result


def write_json(path: Path, obj: dict[str, Any]) -> None:
    """写入稳定排序 JSON。"""
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix strict forward source-root 终端环同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"forward_source_root_packet_proved={fmt_bool(result['forward_source_root_packet_proved'])}",
        f"forward_source_root_independent_after_router={fmt_bool(result['forward_source_root_independent_after_router'])}",
        f"signed_lane_self_proof_eliminated={fmt_bool(result['signed_lane_self_proof_eliminated'])}",
        f"source_rank_paths_converged_to_pointwise_kernel={fmt_bool(result['source_rank_paths_converged_to_pointwise_kernel'])}",
        f"alpha_unsigned_skeleton_closed={fmt_bool(result['alpha_unsigned_skeleton_closed'])}",
        f"signed_lift_branch_recycles_to_terminal_gap={fmt_bool(result['signed_lift_branch_recycles_to_terminal_gap'])}",
        f"anchor_collar_overload_return_schema_closed={fmt_bool(result['anchor_collar_overload_return_schema_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 终端环",
        "",
        "```text",
        "ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn",
        "  -> common packet downstream",
        "  -> signed-lane cycle or ExactUV/source-rank atoms",
        "  -> new primitive / terminal descent absorbed to source-rank",
        "  -> pointwise primitive alpha/delta kernel table",
        "  -> alpha row formula",
        "  -> unsigned skeleton closed",
        "  -> signed lift returns to terminal capacity",
        "  -> anchor-collar overload returns to terminal capacity",
        "  -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
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
        "## 3. 最新剩余",
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
        "## 4. 诚实边界",
        "",
        "- 本证书不证明 source-root packet，也不证明终端 PDEC/CleanKLS。",
        "- 它只说明当前内部 source-root 证明路线会回到终端容量环，不能作为非循环闭合。",
        "- CleanKLS/KZ-DLS 若再经 NCBLK/source-root 闭合就是同一环；需要非循环 KZ/DLS 证明或 direct PDEC scope。",
        "- 高段模型、RatePreservation 与 DStructure/Rankin 仍未闭合。",
        "",
        "## 5. 依赖哈希",
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
