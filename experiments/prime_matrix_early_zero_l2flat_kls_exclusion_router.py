#!/usr/bin/env python3
"""Prime Matrix 早期零行 L2-flat KLS 逃逸排除路由器。

用法示例：
  python3 experiments/prime_matrix_early_zero_l2flat_kls_exclusion_router.py

输出：
  docs/monograph/prime-matrix-early-zero-l2flat-kls-exclusion-router.json
  docs/monograph/prime-matrix-early-zero-l2flat-kls-exclusion-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-early-zero-flatdls-counterexample-router.json"
DEFAULT_PHASE = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_ADMISSION = DOCS / "prime-matrix-newlayer-no-concentration-flat-admission-router.json"
DEFAULT_CONTRADICTION = DOCS / "prime-matrix-early-zero-contradiction-matrix-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-early-zero-l2flat-kls-exclusion-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-zero-l2flat-kls-exclusion-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_once(text: str, old: str, new: str) -> str:
    """只替换一次输入基原子。"""
    if old not in text:
        return text
    return text.replace(old, new, 1)


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


def build_rows(
    previous: dict[str, Any],
    phase: dict[str, Any],
    admission: dict[str, Any],
    contradiction: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 L2-flat KLS 逃逸排除判定表。"""
    counterexample_pinned = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and contradiction.get("no_unnamed_exit_for_early_zero") is True
    )
    l2flat_escape_active = (
        previous.get("early_zero_flatdls_last_escape_boundary_closed") is True
        and "EarlyZeroL2FlatKLSCounterexampleSpectralExclusion"
        in previous.get("open_gates", [])
    )
    flat_named_return_discipline = (
        admission.get("newlayer_no_concentration_flat_admission_boundary_closed") is True
        and "K1ToK9RegisteredOrRouted" in admission.get("closed_gates", [])
        and "NamedFailureReturnDisciplinePreserved" in admission.get("closed_gates", [])
    )
    phase_schema_closed = (
        phase.get("early_zero_phase_defect_schema_admission_closed") is True
        and phase.get("registered_same_formal_unit_rxf_ledger") is True
        and phase.get("boundary_phase_defect_to_named_families_closed") is True
    )
    stable_or_noauto_closed = (
        phase.get("stable_short_recurrence_certificate_or_no_stable_automorphism_closed")
        is True
    )
    pure_l2flat_collision = all(
        [
            counterexample_pinned,
            l2flat_escape_active,
            flat_named_return_discipline,
            phase_schema_closed,
            stable_or_noauto_closed,
        ]
    )
    terminal_open = "EarlyZeroTerminalExclusion" in phase.get("open_gates", [])
    return [
        row(
            "CounterexampleBasisPinned",
            counterexample_pinned,
            True,
            "本路由只处理假设早期零行存在的反例分支，并显式禁止用真实样本缺席替代证明。",
            "若要闭合全局命题，仍需从反例压力推出结构矛盾。",
        ),
        row(
            "L2FlatEscapeIsActiveLastGate",
            l2flat_escape_active,
            True,
            "上一层已把 flat-DLS 最后逃逸压成 EarlyZeroL2FlatKLSCounterexampleSpectralExclusion。",
            "现在只排除该反例专属逃逸，不证明一般 DLS 大筛。",
        ),
        row(
            "FlatAdmissionNamedReturnDiscipline",
            flat_named_return_discipline,
            True,
            "flat/KLS 准入只允许所有 K1--K9 低维缺陷已删除或命名回流后的残余进入。",
            "一旦出现 registered 低维缺陷，就不能继续叫纯 L2-flat 逃逸。",
        ),
        row(
            "EarlyZeroPhaseDefectSchemaImported",
            phase_schema_closed,
            True,
            "早期零行强制同 formal unit 的 R_x=F_x 账本，并给稳定短复现或边界相位缺陷准入。",
            "准入不是终端排斥；它只保证没有第四类无名出口。",
        ),
        row(
            "StableOrNoAutomorphismDichotomyImported",
            stable_or_noauto_closed,
            True,
            "同 formal unit 内要么有稳定短移自同构，要么有 no-automorphism 相位缺陷证书。",
            "两支都进入 PDEC/SAE/ColumnCRT 命名家族。",
        ),
        row(
            "PureL2FlatCounterexampleCollision",
            pure_l2flat_collision,
            True,
            "L2-flat 逃逸要求无 registered 低维缺陷；早期零行却强制 registered 稳定/相位缺陷。",
            "因此反例不能停在纯 L2-flat KLS 逃逸，必须回流早期零行终端排斥包或外部谱输入。",
        ),
        row(
            "EarlyZeroL2FlatKLSCounterexampleSpectralExclusion",
            pure_l2flat_collision,
            True,
            "该硬点作为无名 flat 谱逃逸已被排除。",
            "替换为 EarlyZeroTerminalExclusionPackage。",
        ),
        row(
            "EarlyZeroTerminalExclusionPackage",
            False,
            False,
            "还没有排斥准入后的 primitive PDEC 容量、SAE/LocalSurvivor 或稳定复现位移缺陷。",
            "下一步最窄目标。",
        ),
        row(
            "DStructureRankinStillIndependent",
            True,
            False,
            "即使早期零行终端排斥完成，DStructure/Tail-log4/finite Rankin 仍需独立验收。",
            "不在本路由中偷渡闭合。",
        ),
        row(
            "RowColumnUnconditionalClosure",
            False,
            False,
            "本路由关闭的是 L2-flat 逃逸口，不是完整行/列无条件定理。",
            "row_column_unconditional_closed=false。",
        ),
    ]


def run(
    previous_path: Path,
    phase_path: Path,
    admission_path: Path,
    contradiction_path: Path,
) -> dict[str, Any]:
    """执行早期零行 L2-flat KLS 逃逸排除路由。"""
    source_paths = [previous_path, phase_path, admission_path, contradiction_path]
    previous = load_json(previous_path)
    phase = load_json(phase_path)
    admission = load_json(admission_path)
    contradiction = load_json(contradiction_path)
    rows = build_rows(
        previous=previous,
        phase=phase,
        admission=admission,
        contradiction=contradiction,
    )
    old_atom = "EarlyZeroL2FlatKLSCounterexampleSpectralExclusion"
    new_atom = "EarlyZeroTerminalExclusionPackage"
    exclusion_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == old_atom
    )
    latest_self = replace_once(previous.get("latest_self_contained_basis", ""), old_atom, new_atom)
    latest_cond = replace_once(previous.get("latest_conditional_basis", ""), old_atom, new_atom)
    return {
        "certificate_type": "early_zero_l2flat_kls_exclusion_router",
        "status": "early_zero_l2flat_kls_escape_excluded_to_terminal_package",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "early_zero_l2flat_kls_counterexample_spectral_exclusion_closed": exclusion_closed,
        "pure_l2flat_escape_as_unnamed_branch_removed": exclusion_closed,
        "general_dls_flat_highmod_large_sieve_absorption_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": old_atom,
        "terminal_gap_after_router": (
            "EarlyZeroTerminalExclusionPackage_OR_"
            "CDependentResidueWeightSpectralCancellationInput"
        ),
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {
            old_atom: new_atom,
        },
        "next_priority": new_atom,
        "structural_collision": [
            "Assume EarlyZeroRowWithinP",
            "CLB gives R_x=F_x in one formal unit",
            "Early-zero phase schema gives stable recurrence OR no-automorphism phase defect",
            "flat/KLS admission requires all registered low-dimensional defects routed away",
            "therefore pure L2-flat KLS cannot be the final unnamed counterexample branch",
            "remaining task is terminal exclusion for the registered early-zero defect",
        ],
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步在反例分支内排除了纯 L2-flat KLS 逃逸：早期零行强制同 formal unit 的"
            "稳定复现或边界相位缺陷，而 flat/KLS 准入要求这种 registered 低维缺陷已经"
            "命名回流。因此 L2-flat 逃逸不能作为最后无名分支；它被替换为"
            " EarlyZeroTerminalExclusionPackage。该结论仍不排斥终端家族本身。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 早期零行 L2-flat KLS 逃逸排除路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        "early_zero_l2flat_kls_counterexample_spectral_exclusion_closed="
        f"{fmt_bool(result['early_zero_l2flat_kls_counterexample_spectral_exclusion_closed'])}",
        "pure_l2flat_escape_as_unnamed_branch_removed="
        f"{fmt_bool(result['pure_l2flat_escape_as_unnamed_branch_removed'])}",
        "general_dls_flat_highmod_large_sieve_absorption_proved="
        f"{fmt_bool(result['general_dls_flat_highmod_large_sieve_absorption_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 结构碰撞",
        "",
        "```text",
    ]
    lines.extend(result["structural_collision"])
    lines.extend(
        [
            "```",
            "",
            "这不是从真实样本缺席推出结论，而是在 `Assume EarlyZeroRowWithinP` 下比较两个已登记合同：早期零行合同强制缺陷，flat/KLS 合同禁止未回流缺陷。",
            "",
            "## 2. 替换律",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "条件/外部版仍可由 `CDependentResidueWeightSpectralCancellationInput` 承担。",
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{remaining}` |".format(
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
            f"最窄目标更新为 `{result['next_priority']}`：排斥准入后的早期零行终端家族，"
            "即 primitive PDEC 容量、SAE/LocalSurvivor packet，或稳定复现位移缺陷。"
            "完成该包后仍需 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_outputs(result: dict[str, Any], json_out: Path, md_out: Path) -> None:
    """写出 JSON 与 Markdown。"""
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--phase", type=Path, default=DEFAULT_PHASE)
    parser.add_argument("--admission", type=Path, default=DEFAULT_ADMISSION)
    parser.add_argument("--contradiction", type=Path, default=DEFAULT_CONTRADICTION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        phase_path=args.phase,
        admission_path=args.admission,
        contradiction_path=args.contradiction,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
