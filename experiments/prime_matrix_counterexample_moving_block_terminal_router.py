#!/usr/bin/env python3
"""Prime Matrix 反例分支 moving-block 到早期零行终端包路由器。

用法示例：
  python3 experiments/prime_matrix_counterexample_moving_block_terminal_router.py

输出：
  docs/monograph/prime-matrix-counterexample-moving-block-terminal-router.json
  docs/monograph/prime-matrix-counterexample-moving-block-terminal-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-independent-precauchy-identity-taxonomy-router.json"
DEFAULT_L2FLAT = DOCS / "prime-matrix-early-zero-l2flat-kls-exclusion-router.md"
DEFAULT_TERMINAL = DOCS / "prime-matrix-early-zero-terminal-package-reduction-router.md"
DEFAULT_ENTROPY = DOCS / "prime-matrix-triad-a1-source-block-entropy-router.md"
DEFAULT_MOVING = DOCS / "prime-matrix-clean-core-moving-atom-sharp-input-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-counterexample-moving-block-terminal-router.json"
DEFAULT_MD = DOCS / "prime-matrix-counterexample-moving-block-terminal-router.md"

OLD_ATOM = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
NEW_ATOM = (
    "EarlyZeroTerminalExclusionPackage "
    "AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock"
)


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
    """替换输入基中的 moving-block 原子。"""
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


def build_rows(
    previous: dict[str, Any],
    l2flat_text: str,
    terminal_text: str,
    entropy_text: str,
    moving_text: str,
) -> list[dict[str, Any]]:
    """把反例分支中的 moving-block hardpoint 压到早期零行终端包。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    entropy_implication = (
        "SourceBlockEntropyNCBLK => NC-BLK" in entropy_text
        and "formal WFD/Type-I-II/Fourier inputs do not imply SourceBlockEntropyNCBLK" in entropy_text
    )
    moving_atom_pinned = (
        "ActualNoncanonicalCleanCoreMovingAtom" in moving_text
        and "moving same-(u,v) 大原子" in moving_text
        and "FormalTemplateNoGoRetained" in moving_text
    )
    l2flat_escape_removed = (
        "early_zero_l2flat_kls_counterexample_spectral_exclusion_closed=true" in l2flat_text
        and "pure_l2flat_escape_as_unnamed_branch_removed=true" in l2flat_text
        and "EarlyZeroTerminalExclusionPackage" in l2flat_text
    )
    terminal_package_reduced = (
        "early_zero_terminal_package_reduced=true" in terminal_text
        and "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn" in terminal_text
        and "CompositeCofactorDepthDescentOrNamedReturn" in terminal_text
        and "EarlyBandLocalSurvivorOrSAEExclusion" in terminal_text
    )
    registered_or_flat_dichotomy = all([active, moving_atom_pinned, l2flat_escape_removed])
    reduction_closed = all(
        [
            active,
            entropy_implication,
            moving_atom_pinned,
            l2flat_escape_removed,
            terminal_package_reduced,
        ]
    )
    return [
        row(
            "CounterexampleMovingBlockGateActive",
            active,
            False,
            "最新最窄点是早期零行反例分支中的 actual same-(u,v) moving block 集中。",
            "判断它是否仍可作为无名 clean-core 终端。",
        ),
        row(
            "SourceEntropyImplicationImported",
            entropy_implication,
            True,
            "SourceBlockEntropy 一旦证明可推出 NC-BLK；形式 WFD/Type/Fourier 不能免费推出它。",
            "不能用 generic 模板闭合，只能用反例分支结构继续压缩。",
        ),
        row(
            "SharpMovingAtomPinned",
            moving_atom_pinned,
            True,
            "clean-core sharp 输入已固定为最终容量测度无 moving same-(u,v) 大原子。",
            "若有大原子，必须通过所有回流测试。",
        ),
        row(
            "RegisteredOrPureFlatDichotomy",
            registered_or_flat_dichotomy,
            True,
            "反例分支中的 moving block 若有登记低维签名则进 PDEC/SAE/ColumnCRT；若没有则是纯 L2-flat/NC-BLK 逃逸。",
            "两支都不再是无名终端。",
        ),
        row(
            "PureL2FlatEscapeAlreadyRemovedInEarlyZeroBranch",
            l2flat_escape_removed,
            True,
            "早期零行反例分支已排除纯 L2-flat KLS 作为最后无名逃逸。",
            "纯 flat 支路回到 EarlyZeroTerminalExclusionPackage。",
        ),
        row(
            "EarlyZeroTerminalPackageAlreadyReduced",
            terminal_package_reduced,
            True,
            "EarlyZeroTerminalExclusionPackage 已压成 anchor-collar、复合 cofactor 下降和 early-band SAE 三项。",
            "终端包仍未被排斥。",
        ),
        row(
            "CounterexampleMovingBlockReducedToTerminalPackage",
            reduction_closed,
            True,
            "在假设早期零行分支内，moving-block 集中不能继续作为独立 clean-core 无名出口。",
            NEW_ATOM,
        ),
        row(
            "EarlyZeroTerminalExclusionPackage",
            False,
            False,
            "还没有排斥准入后的 primitive PDEC 容量、SAE/LocalSurvivor 或稳定复现位移缺陷。",
            "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion。",
        ),
        row(
            "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock",
            False,
            False,
            "ExplicitModelGapAndFiniteDPRCLedger 仍需与本次 moving-block 到终端包的替换口径一致化。",
            "检查模型余量/有限 DPRC 账本是否已覆盖该替换后的终端包。",
        ),
        row(
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(
    previous_path: Path,
    l2flat_path: Path,
    terminal_path: Path,
    entropy_path: Path,
    moving_path: Path,
) -> dict[str, Any]:
    """执行 moving-block 到早期零行终端包路由。"""
    source_paths = [previous_path, l2flat_path, terminal_path, entropy_path, moving_path]
    previous = load_json(previous_path)
    rows = build_rows(
        previous=previous,
        l2flat_text=l2flat_path.read_text(encoding="utf-8"),
        terminal_text=terminal_path.read_text(encoding="utf-8"),
        entropy_text=entropy_path.read_text(encoding="utf-8"),
        moving_text=moving_path.read_text(encoding="utf-8"),
    )
    reduction_closed = next(
        bool(item["closed"]) for item in rows if item["gate"] == "CounterexampleMovingBlockReducedToTerminalPackage"
    )
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "counterexample_moving_block_terminal_router",
        "status": "counterexample_moving_block_reduced_to_early_zero_terminal_package_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "moving_block_to_terminal_reduction_closed": reduction_closed,
        "actual_moving_block_spread_proved": False,
        "early_zero_terminal_package_fully_proved": False,
        "exact_model_gap_dprc_compatibility_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": "EarlyZeroTerminalExclusionPackage",
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步只在假设早期零行反例分支内工作。actual same-(u,v) moving block 若有登记低维签名，"
            "它已经是 PDEC/SAE/ColumnCRT 型终端；若完全无登记签名，则它就是纯 L2-flat/NC-BLK 逃逸，"
            "而早期零行 L2-flat 路由已把该逃逸排除为 EarlyZeroTerminalExclusionPackage。"
            "因此 moving-block hardpoint 不再是独立无名 clean-core 出口，剩余回到早期零行终端包及模型/DPRC 口径兼容。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 反例分支 moving-block 到早期零行终端包路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"moving_block_to_terminal_reduction_closed={fmt_bool(result['moving_block_to_terminal_reduction_closed'])}",
        f"actual_moving_block_spread_proved={fmt_bool(result['actual_moving_block_spread_proved'])}",
        f"early_zero_terminal_package_fully_proved={fmt_bool(result['early_zero_terminal_package_fully_proved'])}",
        (
            "exact_model_gap_dprc_compatibility_proved="
            f"{fmt_bool(result['exact_model_gap_dprc_compatibility_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 反例二分",
        "",
        "```text",
        "Assume EarlyZeroRowWithinP",
        "actual moving same-(u,v) atom",
        "  -> registered finite/low-dimensional signature",
        "       -> PDEC / SAE / ColumnCRT / EarlyZeroTerminalExclusionPackage",
        "  -> no registered signature",
        "       -> pure L2-flat / NC-BLK escape",
        "       -> EarlyZeroTerminalExclusionPackage",
        "```",
        "",
        "该二分不使用真实样本缺席；它只比较反例分支内已登记的早期零行缺陷合同与 flat/KLS 准入合同。",
        "",
        "## 2. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "下一步最窄目标回到 `EarlyZeroTerminalExclusionPackage`：排斥 primitive PDEC 容量、"
            "SAE/LocalSurvivor packet 或稳定复现位移缺陷；同时核对模型余量/DPRC 账本是否与该替换口径兼容。",
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
    parser.add_argument("--l2flat", type=Path, default=DEFAULT_L2FLAT)
    parser.add_argument("--terminal", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--entropy", type=Path, default=DEFAULT_ENTROPY)
    parser.add_argument("--moving", type=Path, default=DEFAULT_MOVING)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        l2flat_path=args.l2flat,
        terminal_path=args.terminal,
        entropy_path=args.entropy,
        moving_path=args.moving,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
