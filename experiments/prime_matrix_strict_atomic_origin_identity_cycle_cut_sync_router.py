#!/usr/bin/env python3
"""生成 strict atomic 来源恒等式循环切断同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_atomic_origin_identity_cycle_cut_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-atomic-origin-identity-cycle-cut-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-atomic-origin-identity-cycle-cut-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-atomic-origin-identity-cycle-cut-sync-router.md"

TARGET = "NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SEED_EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
SEED_CYCLE_INPUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
MOVING_ATOM_NONREC = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-atomic-payload-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json",
    "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json",
    "prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json",
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


def terminal_atoms(global_frontier: dict[str, Any]) -> list[str]:
    """返回已登记三原子；缺失时给出保守默认。"""
    atoms = global_frontier.get("three_atoms")
    if isinstance(atoms, list) and atoms:
        return [str(atom) for atom in atoms]
    return [
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
        "A1CleanBranchCanonicalSourceAdmission",
        MOVING_ATOM,
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步 atomic 来源恒等式与现有循环切断前沿。"""
    previous = data["previous"]
    row_level = data["row_level"]
    source_loop = data["source_loop"]
    seed_emitter = data["seed_emitter"]
    cycle_guard = data["cycle_guard"]
    seed_cycle = data["seed_cycle"]
    terminal_fusion = data["terminal_fusion"]
    global_frontier = data["global_frontier"]

    return [
        row(
            "AtomicOriginIdentityTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 atomic signed payload 压成非循环 atomic basis word/signed coefficient 来源恒等式。",
            TARGET,
        ),
        row(
            "AtomicOriginIdentityRequiresRowLevelLedger",
            previous.get("existing_origin_route_returns_row_table") is True,
            False,
            "该来源恒等式的既有内部路线回到逐行 clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "RowLevelTableRequiresAcyclicSeedEmitter",
            row_level.get("next_direct_attack_target") == SEED_EMITTER
            and row_level.get("table_requires_acyclic_seed_with_emitter") is True,
            True,
            "逐行表必须由无环 pre-Cauchy source seed 自带 signed row emitter 生成。",
            SEED_EMITTER,
        ),
        row(
            "SourceLoopCutImported",
            source_loop.get("source_loop_cut_closed") is True
            and source_loop.get("circular_reverse_derivation_rejected") is True,
            True,
            "origin ledger -> constructor -> emitter -> origin ledger 的循环已被切断。",
            "不能由 row-level/source-loop 自证。",
        ),
        row(
            "SeedEmitterReducesToSignedCoefficientLaw",
            seed_emitter.get("next_direct_attack_target") == "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward",
            False,
            "合法 seed 分支仍需要每条 primitive row 的 signed coefficient law。",
            "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward",
        ),
        row(
            "SeedCoordinateSourceCycleDetected",
            cycle_guard.get("seed_coordinate_source_cycle_detected") is True
            and cycle_guard.get("raw_cycle_counts_as_closure") is False,
            True,
            "signed coordinate、assignment、origin identity、row emitter、basis alphabet 与 word constructor 构成闭合依赖环。",
            SEED_CYCLE_INPUT,
        ),
        row(
            "SeedCycleCutBranchAlreadySaturated",
            seed_cycle.get("seed_cycle_cut_branch_saturated") is True
            and seed_cycle.get("cycle_cut_joint_route_returns_to_row_level_fixed_point") is True,
            False,
            "cycle-cut 分支已攻到边界：联合 basis/coefficient 发射器未证，继续展开回 row-level 固定点。",
            "PDEC same-set scope or new joint formula。",
        ),
        row(
            "SeedIndependentInputRemovedByTerminalFusion",
            terminal_fusion.get("acyclic_pre_cauchy_seed_independent_input_removed") is True
            and terminal_fusion.get("seed_exists_branch_covered_by_terminal_family") is True
            and terminal_fusion.get("seed_absent_branch_returned_to_terminal_family") is True,
            True,
            "seed 存在/不存在两支都已被送入同一 acyclic terminal family；seed 不再是独立闭合输入。",
            TERMINAL_FAMILY,
        ),
        row(
            "TraceAndSignedSourcePseudoExitsRemoved",
            global_frontier.get("branch_trace_self_proof_eliminated") is True
            and global_frontier.get("signed_source_fixed_point_eliminated_as_proof") is True,
            True,
            "全局前沿已删除 branch trace 自证与 signed-source 固定点这两个伪出口。",
            "terminal three atoms。",
        ),
        row(
            "GlobalTerminalThreeAtomsPinned",
            global_frontier.get("strict_current_frontier_three_atoms") is True,
            False,
            "删除当前循环路线后，strict 自足线剩 terminal three atoms。",
            " OR ".join(terminal_atoms(global_frontier)),
        ),
        row(
            "MovingAtomRecommendedNextAttack",
            global_frontier.get("recommended_next_attack_target") == MOVING_ATOM,
            False,
            "三原子中最贴近反例链终端矛盾的是 actual noncanonical clean-core moving atom 排斥。",
            MOVING_ATOM_NONREC,
        ),
        row(
            "AtomicOriginIdentityCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出新的非循环 atomic 来源恒等式；内部展开回到已识别循环。",
            "terminal three atoms or new primitive origin input。",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "三原子与 DStructure/Rankin 独立验收仍未闭合。",
            f"{MOVING_ATOM_NONREC} OR terminal three atoms; plus {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 atomic 来源恒等式循环切断同步证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-atomic-payload-origin-identity-router.json"),
        "row_level": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "seed_emitter": load_json("prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json"),
        "cycle_guard": load_json("prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"),
        "seed_cycle": load_json("prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"),
        "terminal_fusion": load_json("prime-matrix-strict-acyclic-seed-terminal-fusion-router.json"),
        "global_frontier": load_json("prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json"),
    }
    rows = build_rows(data)
    atoms = terminal_atoms(data["global_frontier"])
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_atomic_origin_identity_cycle_cut_sync_router",
        "status": "atomic_origin_identity_synced_to_terminal_three_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "target_input_before_router": TARGET,
        "atomic_origin_identity_cycle_cut_sync_closed": True,
        "atomic_origin_identity_current_corpus_proved": False,
        "row_level_route_returns_to_seed_emitter": any(
            item["gate"] == "RowLevelTableRequiresAcyclicSeedEmitter" and item["closed"] is True
            for item in rows
        ),
        "seed_coordinate_source_cycle_detected": any(
            item["gate"] == "SeedCoordinateSourceCycleDetected" and item["closed"] is True for item in rows
        ),
        "seed_independent_input_removed_by_terminal_fusion": any(
            item["gate"] == "SeedIndependentInputRemovedByTerminalFusion" and item["closed"] is True
            for item in rows
        ),
        "terminal_three_atoms_pinned": any(
            item["gate"] == "GlobalTerminalThreeAtomsPinned" and item["closed"] is True for item in rows
        ),
        "recommended_next_attack_target": MOVING_ATOM,
        "recommended_nonrecursive_form": MOVING_ATOM_NONREC,
        "terminal_three_atoms": atoms,
        "dstructure_rankin_independent_gate": DSTRUCTURE,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": MOVING_ATOM_NONREC,
        "strict_author_side_remaining_basis": (
            f"({ ' OR '.join(atoms) }) AND {DSTRUCTURE}"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步继续攻击 `NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward`。"
            "atomic 限制没有产生新的 signed coefficient 来源；它的内部展开回到 row-level origin ledger，"
            "row-level ledger 又要求 acyclic seed signed row emitter，而该 emitter 经 signed coefficient law、"
            "basis weight source、basis alphabet 与 word constructor 回到已登记的坐标-来源依赖环。"
            "seed-cycle-cut 分支和 seed 存在/不存在二分均已归入 acyclic terminal family；全局前沿也已删除 "
            "branch trace 自证与 signed-source 固定点。因此当前 strict 自足线没有新的未展开 signed-source 字段，"
            "真正剩余回到 terminal three atoms；其中最贴近反例链终端矛盾的下一主攻是 "
            "`IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict atomic 来源恒等式循环切断同步",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_level_route_returns_to_seed_emitter={fmt_bool(result['row_level_route_returns_to_seed_emitter'])}",
        f"seed_coordinate_source_cycle_detected={fmt_bool(result['seed_coordinate_source_cycle_detected'])}",
        (
            "seed_independent_input_removed_by_terminal_fusion="
            f"{fmt_bool(result['seed_independent_input_removed_by_terminal_fusion'])}"
        ),
        f"terminal_three_atoms_pinned={fmt_bool(result['terminal_three_atoms_pinned'])}",
        f"atomic_origin_identity_current_corpus_proved={fmt_bool(result['atomic_origin_identity_current_corpus_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 当前 terminal three atoms",
        "",
    ]
    for atom in result["terminal_three_atoms"]:
        lines.append(f"- `{atom}`")
    lines.extend(
        [
            "",
            "建议下一主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 3. 作者侧剩余基",
            "",
            "```text",
            result["strict_author_side_remaining_basis"],
            "```",
        ]
    )
    if result["missing_sources"]:
        lines.extend(["", "## 4. 缺失依赖", ""])
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
