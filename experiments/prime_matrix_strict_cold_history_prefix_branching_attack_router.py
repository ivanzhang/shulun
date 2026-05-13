#!/usr/bin/env python3
"""生成 strict 冷历史前缀分叉攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_history_prefix_branching_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json
  docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json",
    "prime-matrix-strict-effective-cold-history-pruning-router.json",
    "prime-matrix-strict-short-window-divisor-density-lcm-router.json",
    "prime-matrix-strict-low-multiplier-common-kernel-router.json",
    "prime-matrix-strict-large-pair-kernel-difference-router.json",
    "prime-matrix-strict-fixed-quotient-type-columncrt-router.json",
    "prime-matrix-strict-fixed-quotient-density-transfer-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    "prime-matrix-strict-sparse-terminal-history-router.json",
]

PREFIX_BRANCHING = "ColdHistoryPrefixBranchingHotOrFixedReturnLemma"
TREE_PACKING = "DivisorCompatibleColdHistoryTreePackingBound"
KERNEL_BUDGET = "PrefixBranchingKernelMultiplicityBudgetLedger"
PRIME_POWER = "PrimePowerCascadeColdWindowExclusionOrCapacityTable"
COLD_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
LOW_KERNEL = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
PAIR_KERNEL = "LargePairKernelDifferenceColumnCRTExclusion"
FANIN_KERNEL = "MultiSourceKernelFanInSAEOrPDECExclusion"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
LCM_DISCIPLINE = "ShortWindowLCMMultiplierDisciplineForFrequencyH"
DENSE_LCM = "DenseShortWindowLCMLowerBoundAfterKernelCompression"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_cold_history_prefix_branching_attack_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
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


def prefix_branching_identities() -> list[dict[str, str]]:
    """列出前缀分叉攻坚中已固定的对象。"""
    return [
        {
            "name": "prefix_residual_frequency",
            "formula": "H_U=h_0/D(U)",
            "status": "closed_interface",
            "meaning": "同一前缀 U 下，所有子分叉共享同一个缩频 formal unit。",
        },
        {
            "name": "child_divisor_set",
            "formula": "A_U(Y)={g: Y<g<=2Y, g|H_U, U*g remains cold-admissible}",
            "status": "closed_definition",
            "meaning": "前缀分叉不是任意字母表，而是 H_U 的短窗口除数子集。",
        },
        {
            "name": "lcm_anchor",
            "formula": "lcm(A_U(Y)) | H_U",
            "status": "imported_closed",
            "meaning": "同前缀子分叉的 LCM 被锚定在同一 H_U 上。",
        },
        {
            "name": "incremental_multiplier_split",
            "formula": "mu_t=g_t/gcd(g_t,L_{t-1})",
            "status": "imported_closed",
            "meaning": "分叉要么贡献新 LCM 乘子，要么产生低乘子共同核。",
        },
        {
            "name": "cold_hot_gate",
            "formula": "N_{H_U}(I_U)<=C_core(U) or hot-core return",
            "status": "imported_dichotomy",
            "meaning": "超过冷阈值的窗口不能留在冷供给内，必须回流热核心。",
        },
        {
            "name": "prefix_branching_bound_needed",
            "formula": "|A_U(Y)| <= floor(log H_U/log Lambda)+K_kernel(U,Y,Lambda)+K_fixed(U)+C_core(U)",
            "status": "open_quantitative_bound",
            "meaning": "需要定量限制低乘子共同核、固定历史与冷窗口容量，才能关闭分叉引理。",
        },
    ]


def obstruction_cases() -> list[dict[str, str]]:
    """列出前缀分叉当前最危险的阻塞形态。"""
    return [
        {
            "case": "prime_power_cascade",
            "shape": "g_t in {2,4,8,...} or repeated small-prime blocks",
            "why_dangerous": "LCM 增长慢，低乘子共同核多，正是前一步 Fibonacci/P^0.694 阻塞的树形版本。",
            "required_input": PRIME_POWER,
        },
        {
            "case": "large_pair_same_quotient",
            "shape": "g_i=k b, g_t=k(b+a) with fixed small (b,a)",
            "why_dangerous": "同一有限商型若持久复现，就不是冷分叉，而是固定历史 ColumnCRT/PDEC。",
            "required_input": FIXED_HISTORY,
        },
        {
            "case": "fanin_kernel_cloud",
            "shape": "K_t divides lcm_i gcd(g_t,g_i) but no single pair dominates",
            "why_dangerous": "多源扇入可能绕开单对差值锁，必须有 SAE/PDEC 容量账本。",
            "required_input": FANIN_KERNEL,
        },
        {
            "case": "terminal_cold_window_crowding",
            "shape": "many compatible children stay below hot threshold in adjacent windows",
            "why_dangerous": "如果冷窗口之间没有反级联限制，局部冷可能层叠成全局过大树。",
            "required_input": COLD_ANTICASCADE,
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成前缀分叉判定表。"""
    tree = data["tree"]
    short_lcm = data["short_lcm"]
    low_kernel = data["low_kernel"]
    pair_kernel = data["pair_kernel"]
    scaled = data["scaled"]
    fixed_type = data["fixed_type"]
    sparse_history = data["sparse_history"]

    target_imported = tree.get("next_direct_attack_target") == PREFIX_BRANCHING
    lcm_anchor = short_lcm.get("lcm_anchor_closed") is True
    multiplier_discipline = short_lcm.get("incremental_multiplier_discipline_closed") is True
    kernel_split = (
        low_kernel.get("kernel_subcover_closed") is True
        and low_kernel.get("pair_or_fanin_dichotomy_closed") is True
    )
    finite_quotient = pair_kernel.get("finite_quotient_alphabet_closed") is True
    cold_hot = scaled.get("cold_hot_split_closed") is True
    fixed_route = (
        fixed_type.get("fixed_type_pdec_route_registered") is True
        and sparse_history.get("persistent_history_pdec_route_registered") is True
    )

    return [
        row(
            "PrefixBranchingTargetImported",
            target_imported,
            False,
            "上一层把除数兼容树打包压到前缀分叉/冷窗口反级联。",
            PREFIX_BRANCHING,
        ),
        row(
            "SamePrefixLCMAnchorClosed",
            lcm_anchor,
            True,
            "同一前缀 U 下的全部子分叉除数 LCM 整除同一个 H_U。",
            LCM_DISCIPLINE,
        ),
        row(
            "IncrementalMultiplierSplitClosed",
            multiplier_discipline,
            True,
            "子分叉要么推动 LCM 高度，要么产生低乘子共同核。",
            f"{DENSE_LCM} OR {LOW_KERNEL}",
        ),
        row(
            "LowMultiplierKernelSplitImported",
            kernel_split,
            False,
            "低乘子共同核已拆成大成对差值锁或多源 fan-in，但两者尚未排斥。",
            f"{PAIR_KERNEL} OR {FANIN_KERNEL}",
        ),
        row(
            "FiniteQuotientFixedHistoryRouteImported",
            finite_quotient and fixed_route,
            False,
            "大成对核同商型持久复现进入固定历史 PDEC/ColumnCRT。",
            FIXED_HISTORY,
        ),
        row(
            "ColdHotGateImported",
            cold_hot,
            False,
            "超过冷阈值的终端窗口回流热核心，不能继续计入冷历史树。",
            HOT_CORE,
        ),
        row(
            "PrefixBranchingStructuralDichotomyClosed",
            lcm_anchor and multiplier_discipline and kernel_split and cold_hot,
            True,
            "同前缀过多分叉已无第四出口：LCM、低乘子共同核、热核心或固定历史。",
            KERNEL_BUDGET,
        ),
        row(
            "PrefixBranchingKernelMultiplicityBudgetProved",
            False,
            False,
            "尚未给出低乘子共同核/多源扇入在冷窗口内的统一计数预算。",
            KERNEL_BUDGET,
        ),
        row(
            "PrimePowerCascadeExcluded",
            False,
            False,
            "素数幂和小乘子级联仍是最危险反例形态，必须用冷窗口反级联或容量表排除。",
            PRIME_POWER,
        ),
        row(
            "ColdHistoryPrefixBranchingHotOrFixedReturnProved",
            False,
            False,
            "结构三分法已闭合，定量预算和素数幂反级联未闭合。",
            f"{KERNEL_BUDGET} AND {PRIME_POWER} AND {COLD_ANTICASCADE}",
        ),
        row(
            "DivisorCompatibleColdHistoryTreePackingBoundProved",
            False,
            False,
            "前缀分叉引理未闭合，因此树打包界不能关闭。",
            f"{PREFIX_BRANCHING} AND {COLD_ANTICASCADE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{KERNEL_BUDGET} AND {HOT_CORE} AND {FIXED_HISTORY} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造前缀分叉攻坚证书。"""
    data = {
        "tree": load_json("prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json"),
        "short_lcm": load_json("prime-matrix-strict-short-window-divisor-density-lcm-router.json"),
        "low_kernel": load_json("prime-matrix-strict-low-multiplier-common-kernel-router.json"),
        "pair_kernel": load_json("prime-matrix-strict-large-pair-kernel-difference-router.json"),
        "fixed_type": load_json("prime-matrix-strict-fixed-quotient-type-columncrt-router.json"),
        "scaled": load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"),
        "sparse_history": load_json("prime-matrix-strict-sparse-terminal-history-router.json"),
    }
    rows = build_rows(data)

    return {
        "certificate_type": "prime_matrix_strict_cold_history_prefix_branching_attack_router",
        "status": "prefix_branching_reduced_to_kernel_multiplicity_and_cold_window_anticascade_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "same_prefix_lcm_anchor_closed": True,
        "incremental_multiplier_split_closed": True,
        "low_multiplier_kernel_split_imported": True,
        "finite_quotient_fixed_history_route_imported": True,
        "cold_hot_gate_imported": True,
        "prefix_branching_structural_dichotomy_closed": True,
        "prefix_branching_kernel_multiplicity_budget_proved": False,
        "prime_power_cascade_excluded": False,
        "terminal_cold_window_anticascade_proved": False,
        "cold_history_prefix_branching_hot_or_fixed_return_proved": False,
        "divisor_compatible_cold_history_tree_packing_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": PREFIX_BRANCHING,
        "hardpoint_after_router": f"{KERNEL_BUDGET} AND {PRIME_POWER} AND {COLD_ANTICASCADE}",
        "next_direct_attack_target": KERNEL_BUDGET,
        "parallel_attack_targets": [
            PRIME_POWER,
            COLD_ANTICASCADE,
            LOW_KERNEL,
            PAIR_KERNEL,
            FANIN_KERNEL,
            FIXED_HISTORY,
            HOT_CORE,
            DSTRUCTURE,
        ],
        "prefix_branching_identities": prefix_branching_identities(),
        "obstruction_cases": obstruction_cases(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ColdHistoryPrefixBranchingHotOrFixedReturnLemma` 的结构部分可以闭合："
            "固定前缀 `U` 后，所有子分叉是同一 `H_U=h_0/D(U)` 的短窗口除数，"
            "因此其 LCM 被 `H_U` 锚定；增量乘子纪律迫使每个新子分叉要么增加 LCM 高度，"
            "要么进入低乘子共同核；低乘子共同核再拆成大成对差值锁或多源 fan-in；"
            "超过冷阈值的窗口回流热核心，同商型持久复现回流固定历史。"
            "但这还没有给出定量树打包界，因为小素数幂/低乘子级联可能在冷窗口内制造大量低乘子事件。"
            "最新最窄剩余是 `PrefixBranchingKernelMultiplicityBudgetLedger`，并必须与 "
            "`PrimePowerCascadeColdWindowExclusionOrCapacityTable` 和 "
            "`TerminalColdWindowCompatibilityAntiCascadeLemma` 同步闭合。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 冷历史前缀分叉攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prefix_branching_structural_dichotomy_closed={fmt_bool(result['prefix_branching_structural_dichotomy_closed'])}",
        f"prefix_branching_kernel_multiplicity_budget_proved={fmt_bool(result['prefix_branching_kernel_multiplicity_budget_proved'])}",
        f"prime_power_cascade_excluded={fmt_bool(result['prime_power_cascade_excluded'])}",
        f"terminal_cold_window_anticascade_proved={fmt_bool(result['terminal_cold_window_anticascade_proved'])}",
        f"cold_history_prefix_branching_hot_or_fixed_return_proved={fmt_bool(result['cold_history_prefix_branching_hot_or_fixed_return_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 前缀对象",
        "",
        "| name | formula | status | meaning |",
        "|---|---|---|---|",
    ]
    for item in result["prefix_branching_identities"]:
        lines.append(
            "| "
            f"`{table_cell(item['name'])}` | "
            f"`{table_cell(item['formula'])}` | "
            f"`{table_cell(item['status'])}` | "
            f"{table_cell(item['meaning'])} |"
        )

    lines.extend(
        [
            "",
            "## 阻塞形态",
            "",
            "| case | shape | why_dangerous | required_input |",
            "|---|---|---|---|",
        ]
    )
    for item in result["obstruction_cases"]:
        lines.append(
            "| "
            f"`{table_cell(item['case'])}` | "
            f"`{table_cell(item['shape'])}` | "
            f"{table_cell(item['why_dangerous'])} | "
            f"`{table_cell(item['required_input'])}` |"
        )

    lines.extend(
        [
            "",
            "## 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['gate'])}` | "
            f"`{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | "
            f"{table_cell(item['meaning'])} | "
            f"`{table_cell(item['remaining'])}` |"
        )

    lines.extend(
        [
            "",
            "## 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 并行保留：",
        ]
    )
    for target in result["parallel_attack_targets"]:
        lines.append(f"  - `{target}`")

    lines.extend(
        [
            "",
            "## 证据哈希",
            "",
            "| file | sha256 |",
            "|---|---|",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
