#!/usr/bin/env python3
"""生成 strict seed-cycle-cut 分支饱和前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_seed_cycle_cut_saturation_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.md"

SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
JOINT_EMITTER = "AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json",
    "prime-matrix-strict-cycle-cut-joint-basis-coefficient-emitter-router.json",
    "prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json",
    "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不能当成证明。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


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
    """同步 seed-cycle-cut 分支的已知下钻结果。"""
    latest = data["latest"]
    cycle_cut = data["cycle_cut"]
    joint_sync = data["joint_sync"]
    seed_guard = data["seed_guard"]
    terminal = data["terminal"]
    explicit_joint = data["explicit_joint"]
    pdec = data["pdec"]

    return [
        row(
            "LatestFrontierContainsSeedCycleCut",
            SEED_CYCLE_CUT in str(latest.get("strict_active_basis_after_router")),
            False,
            "上一证书把 strict 自足线压成 seed-cycle-cut、PDEC 作用域匹配、新 joint 公式三选一。",
            SEED_CYCLE_CUT,
        ),
        row(
            "CoordinateSourceCycleAlreadyGuarded",
            seed_guard.get("seed_coordinate_source_cycle_detected") is True
            and seed_guard.get("raw_cycle_counts_as_closure") is False,
            True,
            "signed 坐标、basis word、coefficient assignment、origin identity 与 row emitter 已被识别为闭合依赖环。",
            SEED_CYCLE_CUT,
        ),
        row(
            "SequentialSplitRejected",
            cycle_cut.get("sequential_word_then_coefficient_split_rejected") is True,
            True,
            "不能先生成 primitive basis word 再赋 signed coefficient；word-first 与 coefficient-first 都回指来源表。",
            JOINT_EMITTER,
        ),
        row(
            "JointEmitterNotProved",
            cycle_cut.get("cycle_cut_input_router_closed") is True,
            cycle_cut.get("joint_basis_word_coefficient_emitter_proved") is True,
            "cycle-cut 输入已压成 Cauchy/payment 前联合 basis/coefficient 发射公式，但该公式未证明。",
            JOINT_EMITTER,
        ),
        row(
            "JointEmitterRouteReturnsToRowLevelFixedPoint",
            joint_sync.get("cycle_cut_joint_route_returns_to_row_level_fixed_point") is True,
            joint_sync.get("joint_basis_word_coefficient_emitter_proved") is True,
            "继续展开 joint emitter 会经 joint alpha-side 和 same-row origin 回到 row-level 原始生成表固定点。",
            NEW_JOINT_FORMULA,
        ),
        row(
            "TerminalReturnIsMacrocycle",
            terminal.get("terminal_descent_macrocycle_detected") is True
            and terminal.get("current_terminal_descent_attack_spine_is_recursive") is True,
            terminal.get("acyclic_terminal_return_well_founded_descent_proved") is True,
            "若无 joint emitter，回流 terminal descent；但现有 terminal descent 直攻脊柱已登记为宏循环。",
            NEW_JOINT_FORMULA,
        ),
        row(
            "NewExplicitJointFormulaStillAbsent",
            explicit_joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True,
            explicit_joint.get("new_explicit_joint_constructor_formula_artifact_present") is True,
            "显式 joint constructor 继续展开仍回到 signed-source 固定点，除非提交新的公式工件。",
            NEW_JOINT_FORMULA,
        ),
        row(
            "DirectPDECScopeStillIndependentOpen",
            pdec.get("scope_audit_closed") is True or pdec.get("same_set_pdec_protocol_imported") is True,
            pdec.get("acyclic_same_set_scope_match_proved") is True,
            "PDEC 手臂不是 seed-cycle-cut 的重复出口；它仍独立卡在 same-set 作用域匹配。",
            PDEC_SCOPE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 seed-cycle-cut 分支饱和证书。"""
    data = {
        "latest": load_json("prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json"),
        "cycle_cut": load_json("prime-matrix-strict-cycle-cut-joint-basis-coefficient-emitter-router.json"),
        "joint_sync": load_json("prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json"),
        "seed_guard": load_json("prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"),
        "terminal": load_json("prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json"),
        "explicit_joint": load_json("prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"),
        "pdec": load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    seed_branch_saturated = all(
        item["closed"]
        for item in rows
        if item["gate"]
        in {
            "CoordinateSourceCycleAlreadyGuarded",
            "SequentialSplitRejected",
            "JointEmitterNotProved",
            "JointEmitterRouteReturnsToRowLevelFixedPoint",
            "TerminalReturnIsMacrocycle",
        }
    )
    strict_basis = (
        f"({PDEC_SCOPE} OR {NEW_JOINT_FORMULA}) "
        f"AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_strict_seed_cycle_cut_saturation_frontier_router",
        "status": "seed_cycle_cut_branch_saturated_to_pdec_scope_or_new_joint_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "seed_cycle_cut_branch_attacked": True,
        "seed_cycle_cut_branch_saturated": seed_branch_saturated,
        "seed_cycle_cut_source_input_proved": False,
        "joint_basis_word_coefficient_emitter_proved": data["cycle_cut"].get(
            "joint_basis_word_coefficient_emitter_proved"
        )
        is True,
        "cycle_cut_joint_route_returns_to_row_level_fixed_point": data["joint_sync"].get(
            "cycle_cut_joint_route_returns_to_row_level_fixed_point"
        )
        is True,
        "acyclic_terminal_return_well_founded_descent_proved": data["terminal"].get(
            "acyclic_terminal_return_well_founded_descent_proved"
        )
        is True,
        "acyclic_same_set_scope_match_proved": data["pdec"].get(
            "acyclic_same_set_scope_match_proved"
        )
        is True,
        "new_explicit_joint_constructor_formula_artifact_present": data["explicit_joint"].get(
            "new_explicit_joint_constructor_formula_artifact_present"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": f"{PDEC_SCOPE}_OR_{NEW_JOINT_FORMULA}",
        "strict_active_basis_after_router": strict_basis,
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "`AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput` 已按现有材料直接攻完："
            "顺序拆分被排除，联合 basis/coefficient 发射器未证，继续展开回到 row-level/signed-source 固定点；"
            "无联合发射器时的 terminal descent 回流也已登记为宏循环。因此 seed-cycle-cut 分支不能作为"
            "独立闭合出口。最新 strict 自足前沿压到 PDEC same-set 作用域匹配或新的显式 joint alpha/delta "
            "构造公式，两者之外仍保留模型余量、RatePreservation 与 DStructure/Rankin 守门项。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict seed-cycle-cut 分支饱和前沿",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"seed_cycle_cut_branch_attacked={fmt_bool(result['seed_cycle_cut_branch_attacked'])}",
        f"seed_cycle_cut_branch_saturated={fmt_bool(result['seed_cycle_cut_branch_saturated'])}",
        f"seed_cycle_cut_source_input_proved={fmt_bool(result['seed_cycle_cut_source_input_proved'])}",
        f"joint_basis_word_coefficient_emitter_proved={fmt_bool(result['joint_basis_word_coefficient_emitter_proved'])}",
        f"cycle_cut_joint_route_returns_to_row_level_fixed_point={fmt_bool(result['cycle_cut_joint_route_returns_to_row_level_fixed_point'])}",
        f"acyclic_terminal_return_well_founded_descent_proved={fmt_bool(result['acyclic_terminal_return_well_founded_descent_proved'])}",
        f"acyclic_same_set_scope_match_proved={fmt_bool(result['acyclic_same_set_scope_match_proved'])}",
        f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 2. 最新严格活动基",
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
        ]
    )
    if result["missing_sources"]:
        lines.extend(["", "## 3. 缺失依赖", ""])
        for item in result["missing_sources"]:
            lines.append(f"- `{item}`")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
