#!/usr/bin/env python3
"""生成 Phi-LPF latest cycle-cut / terminal 统一前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_cyclecut_terminal_unified_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_SOURCE_ENTROPY_SYNC = (
    DOCS / "prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync-router.json"
)
STRICT_UNIFIED_FRONTIER = DOCS / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json"
SEED_CYCLE_CUT_FRONTIER = DOCS / "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"
TERMINAL_MACROCYCLE = DOCS / "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json"
PDEC_SCOPE_FRONTIER = DOCS / "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
JOINT_FIELD_ATOM = DOCS / "prime-matrix-strict-joint-emitter-formula-field-atom-router.json"

CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
EXACTUV_INC = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时不当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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
    """登记本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_SOURCE_ENTROPY_SYNC,
        STRICT_UNIFIED_FRONTIER,
        SEED_CYCLE_CUT_FRONTIER,
        TERMINAL_MACROCYCLE,
        PDEC_SCOPE_FRONTIER,
        JOINT_FIELD_ATOM,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def joint_field_basis() -> str:
    """返回 joint 公式的生产性字段基。"""
    return f"{JOINT_DECL} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}"


def build_rows(
    latest_source: dict[str, Any],
    strict_unified: dict[str, Any],
    seed_cycle: dict[str, Any],
    terminal: dict[str, Any],
    pdec: dict[str, Any],
    joint: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest 统一前沿同步判定表。"""
    latest_imported = latest_source.get("next_primary_attack_target") == (
        f"{CYCLE_CUT}_OR_{TERMINAL_DESCENT}"
    )
    strict_imported = (
        strict_unified.get("next_direct_attack_target") == JOINT_DECL
        and strict_unified.get("row_column_unconditional_closed") is False
    )
    return [
        row(
            "LatestCycleOrTerminalExitImported",
            latest_imported,
            False,
            "latest source-entropy downstream 已把主攻压到 cycle-cut 或 terminal descent 二选一。",
            f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
        ),
        row(
            "StrictUnifiedFrontierImported",
            strict_imported,
            True,
            "既有 strict 统一前沿已把 cycle-cut、terminal descent 与 PDEC 内部分支压到 joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "SeedCycleCutBranchSaturated",
            strict_unified.get("seed_cycle_cut_branch_saturated") is True
            and seed_cycle.get("seed_cycle_cut_branch_saturated") is True,
            False,
            "cycle-cut 直接拆分已饱和；没有提交新 joint 公式时会回到 signed-source 固定点或 PDEC。",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "TerminalDescentMacrocycleImported",
            strict_unified.get("terminal_descent_macrocycle_detected") is True
            and terminal.get("terminal_descent_macrocycle_detected") is True,
            False,
            "terminal descent 直攻脊柱形成 terminal-source-pair-joint-terminal 宏循环，不能当作 well-founded descent。",
            f"{CANONICAL_LOCK} OR {NEW_JOINT} OR {INDEPENDENT_BRIDGE}",
        ),
        row(
            "PDECScopeInternalSaturationImported",
            strict_unified.get("pdec_internal_branch_saturated") is True
            and pdec.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True,
            False,
            "same-set PDEC 在内部语料中不再给独立非循环出口，只能保留为条件输入或转向 new joint。",
            f"{NEW_JOINT} OR {EXTERNAL_DIBFI}",
        ),
        row(
            "NewJointFormulaReducedToDeclarationLine",
            strict_unified.get("new_joint_formula_reduced_to_declaration_line") is True
            and joint.get("next_direct_attack_target") == JOINT_DECL,
            False,
            "新的 actual joint alpha/delta 公式若要破环，首个生产性字段是 pre-Cauchy joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "JointDeclarationLineCurrentCorpusProved",
            False,
            False,
            "当前语料仍未提交 joint declaration line、rows formula、prepushforward identity 与 no-return ledger 的合取证明。",
            joint_field_basis(),
        ),
        row(
            "CanonicalLockAndIndependentBridgeStillParallel",
            terminal.get("acyclic_terminal_canonical_lock_proved") is False
            and terminal.get("independent_actual_source_bridge_outside_pair_energy_loop_proved") is False,
            False,
            "terminal 宏循环仍可由 canonical-lock 或 independent source bridge 打破，但二者当前均未证明。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}",
        ),
        row(
            "ExactUVModelRateDStructureStillRequired",
            True,
            False,
            "本层只同步最新 Phi-LPF 前沿到 joint declaration line；ExactUV、模型、Rate 与 DStructure 仍是独立守门项。",
            f"{EXACTUV_INC} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步没有给出全局无条件矛盾，只把 latest 非循环主攻进一步压到 joint declaration line。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 latest cycle-cut / terminal 统一前沿同步证书。"""
    latest_source = load_json(LATEST_SOURCE_ENTROPY_SYNC)
    strict_unified = load_json(STRICT_UNIFIED_FRONTIER)
    seed_cycle = load_json(SEED_CYCLE_CUT_FRONTIER)
    terminal = load_json(TERMINAL_MACROCYCLE)
    pdec = load_json(PDEC_SCOPE_FRONTIER)
    joint = load_json(JOINT_FIELD_ATOM)
    rows = build_rows(latest_source, strict_unified, seed_cycle, terminal, pdec, joint)
    retained_basis = (
        f"(({joint_field_basis()}) OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} "
        f"OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) AND {COMPLETE_KEY} AND {FIXED_KEY_MULT} "
        f"AND {EXACTUV_INC} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_cyclecut_terminal_unified_sync_router",
        "status": "phi_lpf_latest_cyclecut_terminal_unified_to_joint_declaration_line_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_cycle_or_terminal_exit_imported": rows[0]["closed"],
        "strict_unified_frontier_imported": rows[1]["closed"],
        "seed_cycle_cut_branch_saturated": rows[2]["closed"],
        "terminal_descent_macrocycle_detected": rows[3]["closed"],
        "pdec_scope_internal_saturation_imported": rows[4]["closed"],
        "new_joint_formula_reduced_to_declaration_line": rows[5]["closed"],
        "pre_cauchy_joint_declaration_line_proved": False,
        "joint_productive_field_basis_proved": False,
        "canonical_lock_proved": False,
        "independent_actual_source_bridge_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": latest_source.get("next_primary_attack_target", ""),
        "absorbed_to": JOINT_DECL,
        "next_primary_attack_target": JOINT_DECL,
        "latest_joint_field_basis": joint_field_basis(),
        "latest_retained_basis_after_router": retained_basis,
        "reduction_edges": strict_unified.get("reduction_edges", []),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest `AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput_OR_"
            "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` 接到 strict "
            "cycle-cut/terminal/PDEC 统一前沿。cycle-cut 分支已饱和到 PDEC 或 new joint，"
            "terminal descent 已登记为宏循环，same-set PDEC 内部分支也不再给自足非循环出口。"
            "因此 latest 内部第一生产性单点压到 "
            f"`{JOINT_DECL}`；完整 joint 字段基、canonical-lock、independent bridge、PDEC/外部谱、"
            "complete/fixed-key、ExactUV、模型、Rate 与 DStructure 仍开放，行/列命题未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest cycle-cut / terminal unified sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_cycle_or_terminal_exit_imported={fmt_bool(cert['latest_cycle_or_terminal_exit_imported'])}",
        f"strict_unified_frontier_imported={fmt_bool(cert['strict_unified_frontier_imported'])}",
        f"seed_cycle_cut_branch_saturated={fmt_bool(cert['seed_cycle_cut_branch_saturated'])}",
        f"terminal_descent_macrocycle_detected={fmt_bool(cert['terminal_descent_macrocycle_detected'])}",
        f"pdec_scope_internal_saturation_imported={fmt_bool(cert['pdec_scope_internal_saturation_imported'])}",
        f"new_joint_formula_reduced_to_declaration_line={fmt_bool(cert['new_joint_formula_reduced_to_declaration_line'])}",
        f"pre_cauchy_joint_declaration_line_proved={fmt_bool(cert['pre_cauchy_joint_declaration_line_proved'])}",
        f"joint_productive_field_basis_proved={fmt_bool(cert['joint_productive_field_basis_proved'])}",
        f"canonical_lock_proved={fmt_bool(cert['canonical_lock_proved'])}",
        f"independent_actual_source_bridge_proved={fmt_bool(cert['independent_actual_source_bridge_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 导入压缩边",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["reduction_edges"]:
        lines.append(
            f"| `{cell(item.get('from', ''))}` | `{cell(item.get('to', ''))}` | "
            f"{cell(item.get('meaning', ''))} |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新第一生产性单点",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "完整 joint 字段基：",
            "",
            "```text",
            cert["latest_joint_field_basis"],
            "```",
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
