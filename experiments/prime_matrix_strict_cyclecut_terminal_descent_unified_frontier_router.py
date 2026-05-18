#!/usr/bin/env python3
"""生成 cycle-cut / terminal descent / PDEC 统一前沿压缩证书。

用法示例：
  python3 experiments/prime_matrix_strict_cyclecut_terminal_descent_unified_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json

输出：
  data/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-ledger.json
  docs/monograph/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json
  docs/monograph/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.md"

SOURCE_ENTROPY_DOC = DOCS / "prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json"
SEED_CYCLE_DOC = DOCS / "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"
TERMINAL_DOC = DOCS / "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json"
PDEC_DOC = DOCS / "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
JOINT_DOC = DOCS / "prime-matrix-strict-joint-emitter-formula-field-atom-router.json"

SOURCE_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
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
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失返回空对象，缺文件不当作证明。"""
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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """登记本轮依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        SOURCE_ENTROPY_DOC,
        SEED_CYCLE_DOC,
        TERMINAL_DOC,
        PDEC_DOC,
        JOINT_DOC,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def reduction_edges() -> list[dict[str, str]]:
    """列出统一前沿的有向压缩边。"""
    return [
        {
            "from": SOURCE_ENTROPY,
            "to": f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
            "meaning": "source entropy 下游进入 signed 坐标-来源环；不能自证，只能走 cycle-cut 或 terminal descent 出口。",
        },
        {
            "from": CYCLE_CUT,
            "to": f"{PDEC_SCOPE} OR {NEW_JOINT}",
            "meaning": "seed-cycle-cut 顺序拆分被排除，联合 emitter 路线回到 row-level 固定点。",
        },
        {
            "from": TERMINAL_DESCENT,
            "to": f"{CANONICAL_LOCK} OR {NEW_JOINT} OR {INDEPENDENT_BRIDGE}",
            "meaning": "terminal descent 当前下钻链形成 TERMINAL->SOURCE->PAIR->JOINT->TERMINAL 宏循环。",
        },
        {
            "from": PDEC_SCOPE,
            "to": f"{NEW_JOINT} OR conditionally accepted same-set/external certificate",
            "meaning": "PDEC same-set 分支在当前 strict 内部语料中不再给独立非循环出口。",
        },
        {
            "from": NEW_JOINT,
            "to": JOINT_DECL,
            "meaning": "新的 actual joint alpha/delta 公式首个生产性字段是 Cauchy/payment 前联合 declaration line。",
        },
        {
            "from": JOINT_DECL,
            "to": f"{JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}",
            "meaning": "declaration line 之后仍需 rows formula、word/coefficient identity 与命名回流账本。",
        },
    ]


def joint_field_basis() -> str:
    """返回联合发射公式的完整生产性字段基。"""
    return f"{JOINT_DECL} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}"


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """合并上游证书的判定。"""
    source = data["source_entropy"]
    seed = data["seed_cycle"]
    terminal = data["terminal"]
    pdec = data["pdec"]
    joint = data["joint"]

    source_synced = source.get("next_direct_attack_target") == f"{CYCLE_CUT}_OR_{TERMINAL_DESCENT}"
    seed_saturated = seed.get("seed_cycle_cut_branch_saturated") is True
    terminal_macrocycle = terminal.get("terminal_descent_macrocycle_detected") is True
    pdec_saturated = pdec.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
    pdec_target_joint = pdec.get("next_direct_attack_target") == NEW_JOINT
    joint_atom_pinned = joint.get("next_direct_attack_target") == JOINT_DECL

    return [
        row(
            "SourceEntropyExitImported",
            source_synced,
            False,
            "source entropy 首原子已同步到 signed 坐标-来源环；该环不能作为证明。",
            f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
        ),
        row(
            "SeedCycleCutBranchSaturated",
            seed_saturated,
            False,
            "cycle-cut 分支已直接攻击到饱和：顺序拆分不成立，联合 emitter 未证且回到 signed-source 固定点。",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "TerminalDescentRejectedAsWellFoundedProof",
            terminal_macrocycle,
            False,
            "terminal descent 当前脊柱是宏循环，不能作为 well-founded descent 或矛盾。",
            f"{CANONICAL_LOCK} OR {NEW_JOINT} OR {INDEPENDENT_BRIDGE}",
        ),
        row(
            "PDECInternalBranchSaturated",
            pdec_saturated and pdec_target_joint,
            False,
            "PDEC same-set 在当前 strict 内部语料中不是独立非循环出口；条件 PDEC/外部线只能保留为输入。",
            NEW_JOINT,
        ),
        row(
            "NewJointFormulaReducedToDeclarationLine",
            joint_atom_pinned,
            False,
            "新 joint 公式已字段化；第一生产性原子是同一 actual source tuple 的 pre-Cauchy 联合 declaration line。",
            JOINT_DECL,
        ),
        row(
            "JointProductiveFieldBasisStillOpen",
            joint.get("joint_productive_field_decomposition_pinned") is True,
            False,
            "declaration line、rows formula、word/coefficient identity 与 no-downstream-return ledger 仍未合取证明。",
            joint_field_basis(),
        ),
        row(
            "CanonicalLockStillParallel",
            terminal.get("acyclic_terminal_canonical_lock_proved") is False,
            False,
            "canonical-lock 可破 terminal 宏循环，但当前仅是开放并行门。",
            CANONICAL_LOCK,
        ),
        row(
            "IndependentBridgeStillParallel",
            terminal.get("independent_actual_source_bridge_outside_pair_energy_loop_proved") is False,
            False,
            "若走 independent source bridge，必须在 ExactUV/pair-energy/joint 回环前独立证明。",
            INDEPENDENT_BRIDGE,
        ),
        row(
            "PDECOrExternalConditionStillRetained",
            True,
            False,
            "same-set PDEC 或外部 DIBFI 可作为条件输入保留，但没有在当前内部语料中无条件证明。",
            f"{PDEC_SCOPE} OR {EXTERNAL_DIBFI}",
        ),
        row(
            "CompleteFixedExactUVModelRateDStructureGatesStillOpen",
            True,
            False,
            "统一前沿只压缩 cycle/terminal/PDEC 出口；complete-key、fixed-key、ExactUV、模型余量、RatePreservation 与 DStructure 仍需独立验收。",
            f"{COMPLETE_KEY} AND {FIXED_KEY} AND {EXACT_UV} AND {MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步没有找到全局无条件矛盾；只把最新内部主攻单点压到 joint declaration line。",
            "row/column theorem still open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """生成统一前沿证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "source_entropy": load_json(SOURCE_ENTROPY_DOC),
        "seed_cycle": load_json(SEED_CYCLE_DOC),
        "terminal": load_json(TERMINAL_DOC),
        "pdec": load_json(PDEC_DOC),
        "joint": load_json(JOINT_DOC),
    }
    rows = build_rows(data)
    internal_basis = joint_field_basis()
    retained_basis = (
        f"(({internal_basis}) OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACT_UV} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    result = {
        "certificate_type": "prime_matrix_strict_cyclecut_terminal_descent_unified_frontier_router",
        "status": "cyclecut_terminal_descent_pdec_unified_to_joint_declaration_line_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "source_entropy_exit_imported": rows[0]["closed"],
        "seed_cycle_cut_branch_saturated": rows[1]["closed"],
        "terminal_descent_macrocycle_detected": rows[2]["closed"],
        "pdec_internal_branch_saturated": rows[3]["closed"],
        "new_joint_formula_reduced_to_declaration_line": rows[4]["closed"],
        "pre_cauchy_joint_declaration_line_proved": False,
        "joint_productive_field_basis_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": JOINT_DECL,
        "strict_internal_first_productive_atom": JOINT_DECL,
        "strict_internal_joint_field_basis": internal_basis,
        "unified_retained_remaining_basis": retained_basis,
        "reduction_edges": reduction_edges(),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 source-entropy 下游的两个出口继续统一：seed-cycle-cut 已饱和到 PDEC 或 new joint，"
            "terminal descent 已登记为宏循环，PDEC same-set 在当前 strict 内部语料中也已饱和。"
            "因此内部自足线的第一生产性单点压成 `PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple`；"
            "但 canonical-lock、independent source bridge、PDEC/外部谱、complete/fixed-key、ExactUV、模型余量、RatePreservation "
            "和 DStructure/Rankin 仍开放，行/列命题未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict cycle-cut / terminal descent 统一前沿",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"source_entropy_exit_imported={fmt_bool(result['source_entropy_exit_imported'])}",
        f"seed_cycle_cut_branch_saturated={fmt_bool(result['seed_cycle_cut_branch_saturated'])}",
        f"terminal_descent_macrocycle_detected={fmt_bool(result['terminal_descent_macrocycle_detected'])}",
        f"pdec_internal_branch_saturated={fmt_bool(result['pdec_internal_branch_saturated'])}",
        f"new_joint_formula_reduced_to_declaration_line={fmt_bool(result['new_joint_formula_reduced_to_declaration_line'])}",
        f"pre_cauchy_joint_declaration_line_proved={fmt_bool(result['pre_cauchy_joint_declaration_line_proved'])}",
        f"joint_productive_field_basis_proved={fmt_bool(result['joint_productive_field_basis_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 压缩边",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["reduction_edges"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(item['from'])}`",
                    f"`{cell(item['to'])}`",
                    cell(item["meaning"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(item['gate'])}`",
                    fmt_bool(item["closed"]),
                    fmt_bool(item["proved"]),
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 内部第一生产性单点",
            "",
            "```text",
            result["strict_internal_first_productive_atom"],
            "```",
            "",
            "完整 joint 字段基：",
            "",
            "```text",
            result["strict_internal_joint_field_basis"],
            "```",
            "",
            "## 4. 统一保留剩余基",
            "",
            "```text",
            result["unified_retained_remaining_basis"],
            "```",
            "",
            "## 5. 结论边界",
            "",
            "- 本文件是前沿同步与硬点压缩，不是行/列命题证明。",
            "- terminal descent 宏循环不能当作 well-founded descent。",
            "- PDEC same-set 在当前内部语料中只是条件保留线；自足破环仍需新的 joint declaration line 或其他独立输入。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(name)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """入口。"""
    result = build_result()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
