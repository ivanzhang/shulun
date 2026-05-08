#!/usr/bin/env python3
"""Prime Matrix 早期零行终端包与命名回流 schema 调和路由器。

用法示例：
  python3 experiments/prime_matrix_early_zero_terminal_schema_reconciliation_router.py

输出：
  docs/monograph/prime-matrix-early-zero-terminal-schema-reconciliation-router.json
  docs/monograph/prime-matrix-early-zero-terminal-schema-reconciliation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_CURRENT = DOCS / "prime-matrix-counterexample-moving-block-terminal-router.json"
DEFAULT_TERMINAL = DOCS / "prime-matrix-early-zero-terminal-package-reduction-router.json"
DEFAULT_ANCHOR_BRIDGE = DOCS / "prime-matrix-anchor-collar-endpoint-bridge-router.json"
DEFAULT_ANCHOR_LOWMOD = DOCS / "prime-matrix-anchor-lowmod-fixedwheel-admission-router.json"
DEFAULT_ANCHOR_TAIL = DOCS / "prime-matrix-anchor-tailcore-fiber-saturation-router.json"
DEFAULT_ANCHOR_FIBER = DOCS / "prime-matrix-anchor-fiber-saturation-return-schema-router.json"
DEFAULT_COMPOSITE = DOCS / "prime-matrix-composite-cofactor-descent-schema-router.json"
DEFAULT_EARLY_BAND = DOCS / "prime-matrix-early-band-local-survivor-return-schema-router.json"
DEFAULT_SHORTWINDOW = DOCS / "prime-matrix-dls-shortwindow-sae-return-schema-router.json"
DEFAULT_POINTLOAD = DOCS / "prime-matrix-dls-pointload-columncrt-return-schema-router.json"
DEFAULT_FIXEDWHEEL = DOCS / "prime-matrix-dls-fixedwheel-pdec-return-schema-router.json"
DEFAULT_SIGNED = DOCS / "prime-matrix-signed-geometric-variation-compatibility-merger.json"
DEFAULT_SOURCE_LOOP = DOCS / "prime-matrix-clean-core-source-loop-cut-router.json"
DEFAULT_ZERO_SEED = DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json"
DEFAULT_TAXONOMY = DOCS / "prime-matrix-independent-precauchy-identity-taxonomy-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.md"

OLD_ATOM = "EarlyZeroTerminalExclusionPackage"
NEW_ATOM = "GlobalPDECorSparseTerminalExclusion"
EXACT_COMPAT = "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock"
EXPLICIT_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的终端包原子。"""
    return text.replace(old, new)


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


def all_true(*values: Any) -> bool:
    """把证书字段规整为布尔合取。"""
    return all(bool(value) for value in values)


def build_rows(
    current: dict[str, Any],
    terminal: dict[str, Any],
    anchor_bridge: dict[str, Any],
    anchor_lowmod: dict[str, Any],
    anchor_tail: dict[str, Any],
    anchor_fiber: dict[str, Any],
    composite: dict[str, Any],
    early_band: dict[str, Any],
    shortwindow: dict[str, Any],
    pointload: dict[str, Any],
    fixedwheel: dict[str, Any],
    signed: dict[str, Any],
    source_loop: dict[str, Any],
    zero_seed: dict[str, Any],
    taxonomy: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成终端包调和判定表。"""
    basis = current.get("latest_self_contained_basis", "")
    active = current.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    branch_guard = all_true(
        current.get("counterexample_assumption_only"),
        current.get("empirical_absence_not_used"),
        current.get("hypothetical_chain_only"),
        not current.get("row_column_unconditional_closed"),
    )
    terminal_reduced = all_true(
        terminal.get("early_zero_terminal_package_reduced"),
        OLD_ATOM in terminal.get("terminal_gap_before_router", ""),
        "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn" in terminal.get("terminal_gap_after_router", ""),
        "CompositeCofactorDepthDescentOrNamedReturn" in terminal.get("terminal_gap_after_router", ""),
        "EarlyBandLocalSurvivorOrSAEExclusion" in terminal.get("terminal_gap_after_router", ""),
    )
    anchor_stack_reconciled = all_true(
        anchor_bridge.get("anchor_collar_endpoint_bridge_closed"),
        anchor_lowmod.get("anchor_lowmod_independent_input_removed"),
        anchor_tail.get("anchor_tailcore_independent_input_removed"),
        anchor_fiber.get("anchor_fiber_saturation_return_schema_closed"),
        anchor_fiber.get("anchor_specific_fiber_gap_removed"),
    )
    composite_reconciled = all_true(
        composite.get("composite_cofactor_descent_schema_closed"),
        composite.get("composite_cofactor_specific_gap_removed"),
    )
    early_band_reconciled = all_true(
        early_band.get("early_band_local_survivor_return_schema_closed"),
        early_band.get("early_band_specific_gap_removed"),
    )
    dls_schema_reconciled = all_true(
        shortwindow.get("dls_shortwindow_return_schema_closed"),
        shortwindow.get("dls_shortwindow_specific_gap_removed"),
        pointload.get("dls_pointload_return_schema_closed"),
        pointload.get("dls_pointload_specific_gap_removed"),
        pointload.get("columncrt_independent_terminal_removed"),
        fixedwheel.get("dls_fixedwheel_return_schema_closed"),
        fixedwheel.get("dls_fixedwheel_specific_gap_removed"),
    )
    signed_loop_blocked = all_true(
        signed.get("signed_variation_independent_atom_removed"),
        source_loop.get("source_loop_cut_closed"),
        source_loop.get("circular_reverse_derivation_rejected"),
        zero_seed.get("zero_row_seed_extraction_blocked"),
        zero_seed.get("geometry_source_extraction_blocked"),
        taxonomy.get("identity_taxonomy_closed"),
        current.get("moving_block_to_terminal_reduction_closed"),
    )
    reconciliation_closed = all_true(
        active,
        branch_guard,
        terminal_reduced,
        anchor_stack_reconciled,
        composite_reconciled,
        early_band_reconciled,
        dls_schema_reconciled,
        signed_loop_blocked,
    )
    return [
        row(
            "EarlyZeroTerminalPackageReopenedByMovingBlock",
            active,
            False,
            "moving-block 路由把 actual same-(u,v) clean-core 逃逸压回 EarlyZeroTerminalExclusionPackage。",
            "调和这个重新打开的抽象终端包。",
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            branch_guard,
            True,
            "本步只在 Assume EarlyZeroRowWithinP 的假设链条中整理终端义务。",
            "不使用真实样本缺席，也不宣布无条件闭合。",
        ),
        row(
            "AbstractTerminalPackageReducedToNamedChildren",
            terminal_reduced,
            True,
            "EarlyZeroTerminalExclusionPackage 已压成 anchor-collar、复合 cofactor 和 early-band 三个命名子项。",
            "这些子项需要与后续 schema 结果调和。",
        ),
        row(
            "AnchorStackSpecificGapsRemoved",
            anchor_stack_reconciled,
            True,
            "anchor-collar 容量失败已桥接到端点 PDEC 或 fiber 饱和；低模、tail-core、fiber 饱和专属无名出口均已删除。",
            "只剩全局 PDEC/SAE/ColumnCRT/sparse 终端排斥，不能保留 anchor 专属第四出口。",
        ),
        row(
            "CompositeCofactorSpecificGapRemoved",
            composite_reconciled,
            True,
            "复合 cofactor 递归壳 well-founded，持久进 PDEC，孤立进 SAE/LocalSurvivor。",
            "只剩全局 PDEC/sparse 终端排斥。",
        ),
        row(
            "EarlyBandSpecificGapRemoved",
            early_band_reconciled,
            True,
            "early-band LocalSurvivor/SAE 专属无名出口已删除。",
            "全局 short-window/packet/PDEC 终端仍归总终端门处理。",
        ),
        row(
            "DLSSpecificNamedReturnGapsRemoved",
            dls_schema_reconciled,
            True,
            "short-window、point-load/ColumnCRT、fixed-wheel 的专属无名出口均已删除。",
            "这些路由不等于数值 bound 或终端家族无条件排斥已证明。",
        ),
        row(
            "SignedSourceLoopCannotCloseTerminalPackage",
            signed_loop_blocked,
            True,
            "若终端包经 fixed-wheel/signed/source 路线回到 clean-core 来源，它形成已切断的 signed/source 环，最终又回到 moving-block/终端包。",
            "不能把这个环当作证明；必须落到全局终端排斥或外部条件分支。",
        ),
        row(
            "EarlyZeroTerminalPackageReconciledToGlobalTerminalGate",
            reconciliation_closed,
            True,
            "抽象 EarlyZeroTerminalExclusionPackage 不再是独立剩余；所有子路线要么已命名回流，要么被来源环纪律阻断。",
            NEW_ATOM,
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "仍未无条件排斥实际物化的 persistent PDEC、displacement/ColumnCRT、SAE/LocalSurvivor 或 sparse packet 终端证书。",
            "FutureExplicitPrimitivePDECSchema / FutureExplicitSparsePacketExtractorSchema / terminal family exclusion。",
        ),
        row(
            EXACT_COMPAT,
            False,
            False,
            "moving-block 到终端包的替换仍需与 ExplicitModelGapAndFiniteDPRCLedger 的模型余量和有限 DPRC 账本口径一致化。",
            EXACT_COMPAT,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行早期零行终端包调和路由。"""
    data = {name: load_json(path) for name, path in paths.items()}
    rows = build_rows(**data)
    reconciliation_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "EarlyZeroTerminalPackageReconciledToGlobalTerminalGate"
    )
    current = data["current"]
    latest_self = replace_atom(current.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom(current.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "early_zero_terminal_schema_reconciliation_router",
        "status": "early_zero_terminal_package_reconciled_to_global_terminal_frontier_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "early_zero_terminal_abstract_package_reconciled": reconciliation_closed,
        "named_return_schema_reconciliation_closed": reconciliation_closed,
        "source_loop_reimport_blocked": True,
        "early_zero_terminal_package_fully_proved": False,
        "global_pdec_or_sparse_terminal_exclusion_proved": False,
        "exact_model_gap_dprc_compatibility_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": f"{OLD_ATOM} AND {EXACT_COMPAT}",
        "terminal_gap_after_router": f"{NEW_ATOM} AND {EXACT_COMPAT}",
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": NEW_ATOM,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把 moving-block 路由重新打开的 EarlyZeroTerminalExclusionPackage 与后续已闭合的命名回流 schema 调和。"
            "anchor、复合 cofactor、early-band、DLS short-window、point-load/ColumnCRT 与 fixed-wheel 都没有专属无名出口；"
            "signed/source 路线若被用来闭合终端包，会落入已切断的来源环并最终返回 moving-block/终端包。"
            "因此抽象终端包被收缩为全局 PDEC/sparse 终端排斥门，仍未得到无条件矛盾。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 早期零行终端包命名 schema 调和路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"early_zero_terminal_abstract_package_reconciled={fmt_bool(result['early_zero_terminal_abstract_package_reconciled'])}",
        f"named_return_schema_reconciliation_closed={fmt_bool(result['named_return_schema_reconciliation_closed'])}",
        f"source_loop_reimport_blocked={fmt_bool(result['source_loop_reimport_blocked'])}",
        f"early_zero_terminal_package_fully_proved={fmt_bool(result['early_zero_terminal_package_fully_proved'])}",
        f"global_pdec_or_sparse_terminal_exclusion_proved={fmt_bool(result['global_pdec_or_sparse_terminal_exclusion_proved'])}",
        f"exact_model_gap_dprc_compatibility_proved={fmt_bool(result['exact_model_gap_dprc_compatibility_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 调和律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "这一步只删除抽象终端包的重复打开：它不证明 PDEC/SAE/ColumnCRT/LocalSurvivor/sparse 终端家族不存在。",
        "",
        "## 2. 环回纪律",
        "",
        "```text",
        "EarlyZeroTerminalExclusionPackage",
        "  -> DLS fixed-wheel / signed variation",
        "  -> actual signed source / pre-pushforward emitter",
        "  -> source-loop cut / seed no-go / identity taxonomy",
        "  -> moving-block",
        "  -> EarlyZeroTerminalExclusionPackage",
        "```",
        "",
        "该环只说明字段互相回写，不能作为矛盾证明。调和后只能保留全局终端排斥门和模型/DPRC 口径兼容门。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            "下一步最窄目标为 `GlobalPDECorSparseTerminalExclusion`：直接排斥已物化的 PDEC/SAE/ColumnCRT/LocalSurvivor/sparse 终端证书，或把证书提交到显式 primitive PDEC / sparse packet extractor 边界；同时保持 `ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock` 与 `DStructure` 独立验收门。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current", type=Path, default=DEFAULT_CURRENT)
    parser.add_argument("--terminal", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--anchor-bridge", type=Path, default=DEFAULT_ANCHOR_BRIDGE)
    parser.add_argument("--anchor-lowmod", type=Path, default=DEFAULT_ANCHOR_LOWMOD)
    parser.add_argument("--anchor-tail", type=Path, default=DEFAULT_ANCHOR_TAIL)
    parser.add_argument("--anchor-fiber", type=Path, default=DEFAULT_ANCHOR_FIBER)
    parser.add_argument("--composite", type=Path, default=DEFAULT_COMPOSITE)
    parser.add_argument("--early-band", type=Path, default=DEFAULT_EARLY_BAND)
    parser.add_argument("--shortwindow", type=Path, default=DEFAULT_SHORTWINDOW)
    parser.add_argument("--pointload", type=Path, default=DEFAULT_POINTLOAD)
    parser.add_argument("--fixedwheel", type=Path, default=DEFAULT_FIXEDWHEEL)
    parser.add_argument("--signed", type=Path, default=DEFAULT_SIGNED)
    parser.add_argument("--source-loop", type=Path, default=DEFAULT_SOURCE_LOOP)
    parser.add_argument("--zero-seed", type=Path, default=DEFAULT_ZERO_SEED)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    paths = {
        "current": args.current,
        "terminal": args.terminal,
        "anchor_bridge": args.anchor_bridge,
        "anchor_lowmod": args.anchor_lowmod,
        "anchor_tail": args.anchor_tail,
        "anchor_fiber": args.anchor_fiber,
        "composite": args.composite,
        "early_band": args.early_band,
        "shortwindow": args.shortwindow,
        "pointload": args.pointload,
        "fixedwheel": args.fixedwheel,
        "signed": args.signed,
        "source_loop": args.source_loop,
        "zero_seed": args.zero_seed,
        "taxonomy": args.taxonomy,
    }
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")


if __name__ == "__main__":
    main()
