#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor 三破环口到 joint declaration line 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_triad_unified_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_TRIAD = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-origin-cyclecut-sync-router.json"
STRICT_UNIFIED = DOCS / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json"
SEED_CYCLE = DOCS / "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"
PDEC_SCOPE_FRONTIER = DOCS / "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
JOINT_FIELD_ATOM = DOCS / "prime-matrix-strict-joint-emitter-formula-field-atom-router.json"
TERMINAL_MACROCYCLE = DOCS / "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json"

CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
TRIAD = f"{CYCLE_CUT}_OR_{PDEC_SCOPE}_OR_{NEW_JOINT}"
TRIAD_TEXT = f"{CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT}"
JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
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
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def dependency_paths() -> list[Path]:
    """列出本层依赖。"""
    return [
        CURRENT_TRIAD,
        STRICT_UNIFIED,
        SEED_CYCLE,
        PDEC_SCOPE_FRONTIER,
        JOINT_FIELD_ATOM,
        TERMINAL_MACROCYCLE,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def joint_field_basis() -> str:
    """返回 joint declaration 之后仍需正向提交的字段基。"""
    return f"{JOINT_DECL} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}"


def sync_chain() -> list[dict[str, str]]:
    """给出 constructor 三破环口统一同步链。"""
    return [
        {
            "from": CYCLE_CUT,
            "to": f"{PDEC_SCOPE} OR {NEW_JOINT}",
            "meaning": "seed cycle-cut 直接拆分在内部语料中已饱和；没有新 joint 公式就回到固定点或 PDEC。",
        },
        {
            "from": PDEC_SCOPE,
            "to": f"{NEW_JOINT} OR {EXTERNAL_DIBFI}",
            "meaning": "same-set PDEC scope 内部分支不再给自足非循环出口，只能作为条件输入或转外部谱。",
        },
        {
            "from": NEW_JOINT,
            "to": JOINT_DECL,
            "meaning": "新的 actual joint alpha/delta 公式的第一生产性字段是 pre-Cauchy joint declaration line。",
        },
        {
            "from": JOINT_DECL,
            "to": f"{JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}",
            "meaning": "declaration line 之后仍需 rows formula、prepushforward identity 与 no-return ledger。",
        },
    ]


def build_rows(
    current: dict[str, Any],
    strict_unified: dict[str, Any],
    seed_cycle: dict[str, Any],
    pdec: dict[str, Any],
    joint: dict[str, Any],
    terminal: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "CurrentConstructorTriadImported",
            current.get("next_primary_attack_target") == TRIAD
            and current.get("seed_cycle_cut_input_proved") is False
            and current.get("acyclic_same_set_scope_match_proved") is False
            and current.get("new_explicit_joint_constructor_formula_artifact_present") is False,
            False,
            "当前 constructor origin-cyclecut 层已把最窄口推进到 seed cycle-cut / same-set PDEC / new-joint 三破环口。",
            TRIAD_TEXT,
        ),
        row(
            "StrictUnifiedFrontierImported",
            strict_unified.get("next_direct_attack_target") == JOINT_DECL
            and strict_unified.get("seed_cycle_cut_branch_saturated") is True
            and strict_unified.get("pdec_internal_branch_saturated") is True
            and strict_unified.get("new_joint_formula_reduced_to_declaration_line") is True,
            True,
            "strict 统一前沿已把 cycle-cut、PDEC 和 new-joint 内部路线统一压到 joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "SeedCycleCutBranchSaturatedImported",
            seed_cycle.get("seed_cycle_cut_branch_saturated") is True
            and seed_cycle.get("next_direct_attack_target")
            == f"{PDEC_SCOPE}_OR_{NEW_JOINT}",
            False,
            "seed cycle-cut 分支当前只剩 same-set PDEC scope 或 new joint，不再提供自足闭合。",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "PDECScopeInternalSaturationImported",
            pdec.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
            and pdec.get("next_direct_attack_target") == NEW_JOINT,
            False,
            "same-set PDEC scope 在内部语料中已饱和；若不作为条件/外部输入，只能转向 new joint。",
            f"{NEW_JOINT} OR {EXTERNAL_DIBFI}",
        ),
        row(
            "NewJointReducedToDeclarationLineImported",
            joint.get("next_direct_attack_target") == JOINT_DECL
            and joint.get("pre_cauchy_joint_declaration_line_proved") is False
            and strict_unified.get("new_joint_formula_reduced_to_declaration_line") is True,
            False,
            "new-joint 若要破环，首个必须正向提交的 actual 字段是 pre-Cauchy joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "JointFieldBasisStillOpen",
            joint.get("joint_emitter_rows_formula_proved") is False
            and joint.get("joint_emitter_prepushforward_sum_identity_proved") is False
            and joint.get("joint_emitter_no_downstream_named_return_ledger_proved") is False,
            False,
            "joint declaration line 不是完整公式；还需 rows formula、word/coefficient identity 和 no-return ledger。",
            joint_field_basis(),
        ),
        row(
            "TerminalWFDParallelMacrocycleImported",
            terminal.get("terminal_descent_macrocycle_detected") is True
            and terminal.get("acyclic_terminal_canonical_lock_proved") is False
            and terminal.get("independent_actual_source_bridge_outside_pair_energy_loop_proved") is False,
            False,
            "terminal WFD 平行出口当前仍表现为 terminal-source-pair-joint-terminal 宏循环，需要 canonical lock 或 independent bridge。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}",
        ),
        row(
            "ConstructorTriadCurrentCorpusProved",
            False,
            False,
            "当前语料没有 seed cycle-cut、same-set PDEC 或 new-joint 三破环口的任意一项无条件证明。",
            TRIAD_TEXT,
        ),
        row(
            "JointDeclarationLineCurrentCorpusProved",
            False,
            False,
            "当前语料没有 pre-Cauchy joint declaration line 及完整 joint 字段基证明。",
            joint_field_basis(),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只完成 constructor 三破环口到 joint declaration line 的前沿同步，不是三目标命题无条件闭合。",
            f"{JOINT_DECL} AND {SIGNED_SURVIVAL} AND {ROW_MASS} AND {MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    current = load_json(CURRENT_TRIAD)
    strict_unified = load_json(STRICT_UNIFIED)
    seed_cycle = load_json(SEED_CYCLE)
    pdec = load_json(PDEC_SCOPE_FRONTIER)
    joint = load_json(JOINT_FIELD_ATOM)
    terminal = load_json(TERMINAL_MACROCYCLE)
    rows = build_rows(
        current=current,
        strict_unified=strict_unified,
        seed_cycle=seed_cycle,
        pdec=pdec,
        joint=joint,
        terminal=terminal,
    )
    retained_basis = (
        f"(({joint_field_basis()}) OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} "
        f"OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) AND {SIGNED_SURVIVAL} AND {ROW_MASS} "
        f"AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_constructor_triad_unified_sync_router",
        "status": "phi_lpf_latest_constructor_triad_synced_to_joint_declaration_line_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "current_constructor_triad_imported": rows[0]["closed"],
        "strict_unified_frontier_imported": rows[1]["closed"],
        "seed_cycle_cut_branch_saturated_imported": rows[2]["closed"],
        "pdec_scope_internal_saturation_imported": rows[3]["closed"],
        "new_joint_reduced_to_declaration_line_imported": rows[4]["closed"],
        "joint_field_basis_still_open": rows[5]["closed"],
        "terminal_wfd_parallel_macrocycle_imported": rows[6]["closed"],
        "seed_cycle_cut_input_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "pre_cauchy_joint_declaration_line_proved": False,
        "joint_productive_field_basis_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TRIAD,
        "absorbed_to": JOINT_DECL,
        "next_primary_attack_target": JOINT_DECL,
        "latest_joint_field_basis": joint_field_basis(),
        "parallel_primary_attack_targets": [
            CANONICAL_LOCK,
            INDEPENDENT_BRIDGE,
            PDEC_SCOPE,
            EXTERNAL_DIBFI,
            TERMINAL_DESCENT,
            SIGNED_SURVIVAL,
            ROW_MASS,
            EXACTUV_PAIR,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步把 current constructor 的三破环口 `{TRIAD}` 接入 strict 统一前沿。"
            "seed cycle-cut 内部分支已饱和到 PDEC 或 new-joint，same-set PDEC 内部分支已饱和到 "
            f"new-joint 或外部谱，而 new-joint 的第一生产性字段是 `{JOINT_DECL}`。"
            "因此 constructor latest 主攻同步到 joint declaration line；完整 joint 字段基、"
            "canonical lock、independent bridge、PDEC/外部谱、terminal WFD、signed survival、"
            "row-mass、ExactUV、模型、Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor triad-unified sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"current_constructor_triad_imported={fmt_bool(cert['current_constructor_triad_imported'])}",
        f"strict_unified_frontier_imported={fmt_bool(cert['strict_unified_frontier_imported'])}",
        f"seed_cycle_cut_branch_saturated_imported={fmt_bool(cert['seed_cycle_cut_branch_saturated_imported'])}",
        f"pdec_scope_internal_saturation_imported={fmt_bool(cert['pdec_scope_internal_saturation_imported'])}",
        f"new_joint_reduced_to_declaration_line_imported={fmt_bool(cert['new_joint_reduced_to_declaration_line_imported'])}",
        f"joint_field_basis_still_open={fmt_bool(cert['joint_field_basis_still_open'])}",
        f"terminal_wfd_parallel_macrocycle_imported={fmt_bool(cert['terminal_wfd_parallel_macrocycle_imported'])}",
        f"seed_cycle_cut_input_proved={fmt_bool(cert['seed_cycle_cut_input_proved'])}",
        f"acyclic_same_set_scope_match_proved={fmt_bool(cert['acyclic_same_set_scope_match_proved'])}",
        (
            "new_explicit_joint_constructor_formula_artifact_present="
            f"{fmt_bool(cert['new_explicit_joint_constructor_formula_artifact_present'])}"
        ),
        f"pre_cauchy_joint_declaration_line_proved={fmt_bool(cert['pre_cauchy_joint_declaration_line_proved'])}",
        f"joint_productive_field_basis_proved={fmt_bool(cert['joint_productive_field_basis_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. joint 字段基",
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
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "```json",
            json.dumps(cert["source_hashes"], ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    cert = build_certificate()
    print(json.dumps(cert, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
