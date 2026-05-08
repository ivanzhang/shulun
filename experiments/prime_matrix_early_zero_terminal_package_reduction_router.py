#!/usr/bin/env python3
"""Prime Matrix 早期零行终端排斥包压缩路由器。

用法示例：
  python3 experiments/prime_matrix_early_zero_terminal_package_reduction_router.py

输出：
  docs/monograph/prime-matrix-early-zero-terminal-package-reduction-router.json
  docs/monograph/prime-matrix-early-zero-terminal-package-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-early-zero-l2flat-kls-exclusion-router.json"
DEFAULT_PHASE = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_CARRY = DOCS / "prime-matrix-early-zero-carry-shell-router.json"
DEFAULT_COFACTOR = DOCS / "prime-matrix-early-zero-cofactor-depth-router.json"
DEFAULT_ANCHOR = DOCS / "prime-matrix-early-zero-anchor-collar-router.json"
DEFAULT_CONTRADICTION = DOCS / "prime-matrix-early-zero-contradiction-matrix-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-early-zero-terminal-package-reduction-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-zero-terminal-package-reduction-router.md"


REDUCED_PACKAGE = (
    "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn "
    "AND CompositeCofactorDepthDescentOrNamedReturn "
    "AND EarlyBandLocalSurvivorOrSAEExclusion"
)


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
    carry: dict[str, Any],
    cofactor: dict[str, Any],
    anchor: dict[str, Any],
    contradiction: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成终端包压缩判定表。"""
    terminal_package_active = (
        previous.get("next_priority") == "EarlyZeroTerminalExclusionPackage"
        and "EarlyZeroTerminalExclusionPackage" in previous.get("open_gates", [])
    )
    phase_no_fourth_exit = (
        phase.get("early_zero_phase_defect_schema_admission_closed") is True
        and phase.get("boundary_phase_defect_to_named_families_closed") is True
    )
    stable_branch_absorbed = "StableBranchNamedReturn" in phase.get("closed_gates", [])
    carry_support_closed = (
        carry.get("terminal_gap_after_router") == "CarryShellPrimitiveCapacityBoundOrPDECReturn"
        and "ExactCarryShellIdentity" in carry.get("closed_gates", [])
        and "PrimitivePDECSupportReframed" in carry.get("closed_gates", [])
    )
    cofactor_split_closed = (
        cofactor.get("terminal_gap_after_router")
        == "PrimePairCarryShellCapacityAndCompositeCofactorDepthDescent"
        and "SqrtGatePrimeCofactor" in cofactor.get("closed_gates", [])
        and "CompositeCofactorRecursiveReturn" in cofactor.get("closed_gates", [])
    )
    anchor_reduction_closed = (
        anchor.get("terminal_gap_after_router")
        == "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn"
        and "CanonicalLeastAnchorCollar" in anchor.get("closed_gates", [])
        and "FiberShortPrimeInterval" in anchor.get("closed_gates", [])
    )
    contradiction_matrix_compatible = (
        contradiction.get("strongest_current_frontier")
        == "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn"
        and contradiction.get("no_unnamed_exit_for_early_zero") is True
    )
    package_reduced = all(
        [
            terminal_package_active,
            phase_no_fourth_exit,
            stable_branch_absorbed,
            carry_support_closed,
            cofactor_split_closed,
            anchor_reduction_closed,
            contradiction_matrix_compatible,
        ]
    )
    return [
        row(
            "EarlyZeroTerminalPackageActive",
            terminal_package_active,
            True,
            "上一层已把 pure L2-flat 逃逸替换为 EarlyZeroTerminalExclusionPackage。",
            "现在压缩终端包本身。",
        ),
        row(
            "PhaseDefectNoFourthExit",
            phase_no_fourth_exit,
            True,
            "早期零行相位缺陷已经准入 PDEC/SAE/ColumnCRT 命名家族。",
            "还没有排斥这些命名家族。",
        ),
        row(
            "StableRecurrenceDisplacementAbsorbed",
            stable_branch_absorbed,
            True,
            "稳定短复现若存在，按 displacement PDEC、ColumnCRT 或 SAE/endpoint 吸收。",
            "不再作为独立第四项。",
        ),
        row(
            "CarryShellPrimitiveSupportClosed",
            carry_support_closed,
            True,
            "primitive PDEC 支撑已被 exact carry-shell 恒等式重写。",
            "容量不等式仍未证明。",
        ),
        row(
            "CofactorDepthSplitClosed",
            cofactor_split_closed,
            True,
            "x>=sqrt(P) 时 cofactor 必为素数；x<sqrt(P) 的复合 cofactor 只能递归或命名回流。",
            "复合递归容量/孤窗排斥仍未完成。",
        ),
        row(
            "AnchorCollarPrimePairReductionClosed",
            anchor_reduction_closed,
            True,
            "真双素分支的最小高素锚落在 x<q<sqrt((x+1)P)，固定 q 后是长度 <sqrt(P) 的短素数纤维。",
            "短纤维总容量仍未证明不足。",
        ),
        row(
            "ContradictionMatrixFrontierCompatible",
            contradiction_matrix_compatible,
            True,
            "早期零行矛盾矩阵也把当前最强前沿定位到 anchor-collar 纤维容量或命名回流。",
            "说明压缩结果与既有总图一致。",
        ),
        row(
            "EarlyZeroTerminalPackageReduced",
            package_reduced,
            True,
            "抽象 EarlyZeroTerminalExclusionPackage 被压成 anchor-collar、cofactor descent、early-band SAE 三项。",
            REDUCED_PACKAGE,
        ),
        row(
            "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn",
            False,
            False,
            "尚未证明所有 canonical collar q-fiber 的短素数容量不能覆盖 R_x。",
            "下一步最窄目标。",
        ),
        row(
            "CompositeCofactorDepthDescentOrNamedReturn",
            False,
            False,
            "尚未证明 x<sqrt(P) 的复合 cofactor 递归壳必下降到底或命名排斥。",
            "第二剩余。",
        ),
        row(
            "EarlyBandLocalSurvivorOrSAEExclusion",
            False,
            False,
            "孤立早期窗口和递归失败时的 LocalSurvivor/SAE packet 尚未全局排斥。",
            "第三剩余。",
        ),
    ]


def run(
    previous_path: Path,
    phase_path: Path,
    carry_path: Path,
    cofactor_path: Path,
    anchor_path: Path,
    contradiction_path: Path,
) -> dict[str, Any]:
    """执行早期零行终端包压缩。"""
    source_paths = [
        previous_path,
        phase_path,
        carry_path,
        cofactor_path,
        anchor_path,
        contradiction_path,
    ]
    previous = load_json(previous_path)
    phase = load_json(phase_path)
    carry = load_json(carry_path)
    cofactor = load_json(cofactor_path)
    anchor = load_json(anchor_path)
    contradiction = load_json(contradiction_path)
    rows = build_rows(
        previous=previous,
        phase=phase,
        carry=carry,
        cofactor=cofactor,
        anchor=anchor,
        contradiction=contradiction,
    )
    old_atom = "EarlyZeroTerminalExclusionPackage"
    package_reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "EarlyZeroTerminalPackageReduced"
    )
    latest_self = replace_once(previous.get("latest_self_contained_basis", ""), old_atom, REDUCED_PACKAGE)
    latest_cond = replace_once(previous.get("latest_conditional_basis", ""), old_atom, REDUCED_PACKAGE)
    return {
        "certificate_type": "early_zero_terminal_package_reduction_router",
        "status": "early_zero_terminal_package_reduced_to_anchor_collar_depth_sae",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "early_zero_terminal_package_reduced": package_reduced,
        "early_zero_terminal_package_fully_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": old_atom,
        "terminal_gap_after_router": REDUCED_PACKAGE,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {
            old_atom: REDUCED_PACKAGE,
        },
        "next_priority": "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn",
        "remaining_package": [
            "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn",
            "CompositeCofactorDepthDescentOrNamedReturn",
            "EarlyBandLocalSurvivorOrSAEExclusion",
        ],
        "structural_chain": [
            "EarlyZeroTerminalExclusionPackage",
            "=> registered stable recurrence or boundary phase defect",
            "=> exact carry-shell primitive support",
            "=> cofactor depth split",
            "=> x>=sqrt(P): canonical anchor collar short prime fibers",
            "=> x<sqrt(P): composite cofactor descent or SAE/PDEC return",
        ],
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把抽象 EarlyZeroTerminalExclusionPackage 压成已有早期零行几何硬核："
            "大行段是真双素 canonical anchor-collar 短纤维容量，早期段是复合 cofactor "
            "递归下降或 LocalSurvivor/SAE 排斥。该压缩不完成终端排斥，但删除了抽象终端包的"
            "无名性。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 早期零行终端排斥包压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"early_zero_terminal_package_reduced={fmt_bool(result['early_zero_terminal_package_reduced'])}",
        f"early_zero_terminal_package_fully_proved={fmt_bool(result['early_zero_terminal_package_fully_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 结构链",
        "",
        "```text",
    ]
    lines.extend(result["structural_chain"])
    lines.extend(
        [
            "```",
            "",
            "这仍然是在 `Assume EarlyZeroRowWithinP` 下工作；真实样本缺席不参与证明。",
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
            f"最窄目标更新为 `{result['next_priority']}`：证明 canonical anchor collar 中长度 `<sqrt(P)` "
            "的短素数纤维总容量不能覆盖 `R_x`，或证明任何过载都会产生 PDEC/SAE/ColumnCRT 命名证书。",
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
    parser.add_argument("--carry", type=Path, default=DEFAULT_CARRY)
    parser.add_argument("--cofactor", type=Path, default=DEFAULT_COFACTOR)
    parser.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
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
        carry_path=args.carry,
        cofactor_path=args.cofactor,
        anchor_path=args.anchor,
        contradiction_path=args.contradiction,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
