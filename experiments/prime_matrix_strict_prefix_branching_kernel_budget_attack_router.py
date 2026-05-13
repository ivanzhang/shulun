#!/usr/bin/env python3
"""生成 strict 前缀分叉共同核重数预算攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_prefix_branching_kernel_budget_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json
  docs/monograph/prime-matrix-strict-prefix-branching-kernel-budget-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-prefix-branching-kernel-budget-attack-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json",
    "prime-matrix-strict-low-multiplier-common-kernel-router.json",
    "prime-matrix-strict-large-pair-kernel-difference-router.json",
    "prime-matrix-strict-short-window-divisor-density-lcm-router.json",
]

ALPHA = 0.43
PHI = (1 + math.sqrt(5)) / 2
BASES = [2, 3, 5, 7, 11, 13, 17, 19]

KERNEL_BUDGET = "PrefixBranchingKernelMultiplicityBudgetLedger"
SMALL_PRIME_TABLE = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
PRIME_POWER = "PrimePowerCascadeColdWindowExclusionOrCapacityTable"
COLD_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
FANIN_KERNEL = "MultiSourceKernelFanInSAEOrPDECExclusion"
BOUNDED_SAE = "BoundedQuotientTypeSAEAbsorption"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
PREFIX_BRANCHING = "ColdHistoryPrefixBranchingHotOrFixedReturnLemma"
TREE_PACKING = "DivisorCompatibleColdHistoryTreePackingBound"
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
        "experiments/prime_matrix_strict_prefix_branching_kernel_budget_attack_router.py": sha256(
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


def exponent_all_blocks(p: int) -> float:
    """p^a 全有序分组模型的 P 指数。"""
    return math.log(2, p)


def exponent_one_two_blocks(p: int) -> float:
    """只允许 p 与 p^2 分组时的 P 指数。"""
    return math.log(PHI, p)


def prime_power_screen_table() -> list[dict[str, Any]]:
    """生成小素数幂级联指数筛选表。"""
    rows: list[dict[str, Any]] = []
    for p in BASES:
        all_exp = exponent_all_blocks(p)
        one_two_exp = exponent_one_two_blocks(p)
        rows.append(
            {
                "base_prime": p,
                "all_grouped_blocks_exponent": all_exp,
                "all_grouped_blocks_exceeds_alpha": all_exp > ALPHA,
                "one_two_blocks_exponent": one_two_exp,
                "one_two_blocks_exceeds_alpha": one_two_exp > ALPHA,
                "alpha": ALPHA,
            }
        )
    return rows


def dangerous_bases(key: str) -> list[int]:
    """提取超过 alpha 的危险底数。"""
    return [
        int(item["base_prime"])
        for item in prime_power_screen_table()
        if item[key] > ALPHA
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成共同核重数预算判定表。"""
    prefix = data["prefix"]
    low_kernel = data["low_kernel"]
    pair_kernel = data["pair_kernel"]
    tree = data["tree"]

    target_imported = prefix.get("next_direct_attack_target") == KERNEL_BUDGET
    structural = prefix.get("prefix_branching_structural_dichotomy_closed") is True
    low_split = low_kernel.get("pair_or_fanin_dichotomy_closed") is True
    finite_alphabet = pair_kernel.get("finite_quotient_alphabet_closed") is True
    prior_prime_power_open = tree.get("prime_power_cascade_case_closed") is False
    all_danger = dangerous_bases("all_grouped_blocks_exponent")
    fib_danger = dangerous_bases("one_two_blocks_exponent")

    return [
        row(
            "KernelBudgetTargetImported",
            target_imported,
            False,
            "上一层已把前缀分叉的定量缺口压成共同核重数预算。",
            KERNEL_BUDGET,
        ),
        row(
            "PrefixStructuralDichotomyImported",
            structural,
            True,
            "同前缀分叉无第四出口：LCM、共同核、热核心或固定历史。",
            KERNEL_BUDGET,
        ),
        row(
            "LowKernelPairFanInSplitImported",
            low_split,
            False,
            "共同核已拆为大成对差值锁与多源 fan-in，但两者仍需计数/排斥。",
            f"{FANIN_KERNEL} AND {BOUNDED_SAE}",
        ),
        row(
            "FiniteQuotientAlphabetImported",
            finite_alphabet,
            False,
            "大成对核给 O(Lambda^2) 有限商型；持久型进入固定历史。",
            FIXED_HISTORY,
        ),
        row(
            "PrimePowerExponentScreenClosed",
            True,
            True,
            "单素数幂有序分组的指数阈值可显式计算。",
            SMALL_PRIME_TABLE,
        ),
        row(
            "AllBlockDangerousBasesReduced",
            all_danger == [2, 3, 5],
            True,
            "全分组模型中，超过 alpha=0.43 的单素数底数只剩 2、3、5。",
            SMALL_PRIME_TABLE,
        ),
        row(
            "OneTwoBlockDangerousBasesReduced",
            fib_danger == [2, 3],
            True,
            "只允许 p 与 p^2 的 Fibonacci 模型中，危险底数只剩 2、3。",
            SMALL_PRIME_TABLE,
        ),
        row(
            "LargePrimePowerTailSubcriticalInModel",
            True,
            True,
            "对 p>=7 的全分组单素数幂模型，指数低于 alpha；它不是最窄阻塞。",
            SMALL_PRIME_TABLE,
        ),
        row(
            "PrimePowerCascadeColdWindowExclusionProved",
            False,
            False,
            "仍未证明 p=2,3,5 的小素数幂级联不能在冷窗口层叠。",
            f"{SMALL_PRIME_TABLE} AND {COLD_ANTICASCADE}",
        ),
        row(
            "FanInKernelCapacityBudgetProved",
            False,
            False,
            "多源 fan-in 共同核仍缺 SAE/PDEC 容量预算。",
            FANIN_KERNEL,
        ),
        row(
            "PrefixBranchingKernelMultiplicityBudgetProved",
            False,
            False,
            "指数筛选缩小了危险域，但小素数幂表与 fan-in 预算未闭合。",
            f"{SMALL_PRIME_TABLE} AND {FANIN_KERNEL}",
        ),
        row(
            "ColdHistoryPrefixBranchingHotOrFixedReturnProved",
            False,
            False,
            "共同核预算未闭合，因此前缀分叉引理仍未闭合。",
            PREFIX_BRANCHING,
        ),
        row(
            "DivisorCompatibleColdHistoryTreePackingBoundProved",
            False,
            False,
            "前缀分叉与冷窗口反级联未完成，树打包界不能关闭。",
            TREE_PACKING,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{SMALL_PRIME_TABLE} AND {COLD_ANTICASCADE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造共同核重数预算攻坚证书。"""
    data = {
        "prefix": load_json("prime-matrix-strict-cold-history-prefix-branching-attack-router.json"),
        "tree": load_json("prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json"),
        "low_kernel": load_json("prime-matrix-strict-low-multiplier-common-kernel-router.json"),
        "pair_kernel": load_json("prime-matrix-strict-large-pair-kernel-difference-router.json"),
    }
    rows = build_rows(data)
    table = prime_power_screen_table()

    return {
        "certificate_type": "prime_matrix_strict_prefix_branching_kernel_budget_attack_router",
        "status": "kernel_budget_reduced_to_small_prime_power_cascade_and_fanin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "prefix_branching_kernel_budget_target_imported": True,
        "prime_power_exponent_screen_closed": True,
        "dangerous_bases_all_grouped_blocks": dangerous_bases("all_grouped_blocks_exponent"),
        "dangerous_bases_one_two_blocks": dangerous_bases("one_two_blocks_exponent"),
        "large_prime_power_tail_subcritical_in_single_prime_model": True,
        "small_prime_power_cascade_table_proved": False,
        "prime_power_cascade_cold_window_exclusion_proved": False,
        "fanin_kernel_capacity_budget_proved": False,
        "prefix_branching_kernel_multiplicity_budget_proved": False,
        "cold_history_prefix_branching_hot_or_fixed_return_proved": False,
        "divisor_compatible_cold_history_tree_packing_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": KERNEL_BUDGET,
        "hardpoint_after_router": f"{SMALL_PRIME_TABLE} AND {FANIN_KERNEL} AND {COLD_ANTICASCADE}",
        "next_direct_attack_target": SMALL_PRIME_TABLE,
        "parallel_attack_targets": [
            FANIN_KERNEL,
            BOUNDED_SAE,
            FIXED_HISTORY,
            PRIME_POWER,
            COLD_ANTICASCADE,
            DSTRUCTURE,
        ],
        "prime_power_screen_table": table,
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PrefixBranchingKernelMultiplicityBudgetLedger` 继续压缩为小素数幂级联表。"
            "若只看单素数幂 `p^a` 的全有序分组，形式历史数指数为 `log_p 2`；"
            "超过 `alpha=0.43` 的底数只有 `p=2,3,5`。若只允许 `p` 与 `p^2` 两种步长，"
            "历史数为 Fibonacci(a)，指数为 `log_p phi`，超过 alpha 的底数只有 `p=2,3`。"
            "因此大素数幂尾部不再是最窄阻塞；真正危险集中在 `2/3/5` 小素数幂冷窗口级联，"
            "以及多源 fan-in 共同核容量预算。当前仍不能声明共同核预算或行/列命题闭合。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 前缀分叉共同核重数预算攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prime_power_exponent_screen_closed={fmt_bool(result['prime_power_exponent_screen_closed'])}",
        f"dangerous_bases_all_grouped_blocks={result['dangerous_bases_all_grouped_blocks']}",
        f"dangerous_bases_one_two_blocks={result['dangerous_bases_one_two_blocks']}",
        f"small_prime_power_cascade_table_proved={fmt_bool(result['small_prime_power_cascade_table_proved'])}",
        f"fanin_kernel_capacity_budget_proved={fmt_bool(result['fanin_kernel_capacity_budget_proved'])}",
        f"prefix_branching_kernel_multiplicity_budget_proved={fmt_bool(result['prefix_branching_kernel_multiplicity_budget_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 素数幂指数筛选表",
        "",
        "| p | all_grouped_blocks_exponent | all_exceeds_alpha | one_two_blocks_exponent | one_two_exceeds_alpha | alpha |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for item in result["prime_power_screen_table"]:
        lines.append(
            "| "
            f"{item['base_prime']} | "
            f"{item['all_grouped_blocks_exponent']:.6f} | "
            f"`{fmt_bool(item['all_grouped_blocks_exceeds_alpha'])}` | "
            f"{item['one_two_blocks_exponent']:.6f} | "
            f"`{fmt_bool(item['one_two_blocks_exceeds_alpha'])}` | "
            f"{item['alpha']:.6f} |"
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
