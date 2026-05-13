#!/usr/bin/env python3
"""生成 strict 小素数幂冷窗口级联攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_small_prime_power_cascade_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-small-prime-power-cascade-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-small-prime-power-cascade-attack-router.json
  docs/monograph/prime-matrix-strict-small-prime-power-cascade-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-small-prime-power-cascade-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-small-prime-power-cascade-attack-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json",
    "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
]

ALPHA = 0.43
PHI = (1 + math.sqrt(5)) / 2

SMALL_TABLE = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
DYADIC_CASCADE = "DyadicPrimePowerColdWindowCascadeExclusionLemma"
ODD_EPSILON = "OddPrimePowerCascadeEpsilonSavingLedgerForP3P5"
BLOCK_REDUCTION = "PrimePowerBlockSizeReductionToOneTwoStepLedger"
COLD_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
KERNEL_BUDGET = "PrefixBranchingKernelMultiplicityBudgetLedger"
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
        "experiments/prime_matrix_strict_small_prime_power_cascade_attack_router.py": sha256(
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


def exp_all(p: int) -> float:
    """全分组模型指数。"""
    return math.log(2, p)


def exp_one_two(p: int) -> float:
    """一二步模型指数。"""
    return math.log(PHI, p)


def risk_level(all_gap: float, one_two_gap: float) -> str:
    """按阈值缺口给出风险层级。"""
    if one_two_gap > 0.2:
        return "primary_dyadic"
    if one_two_gap > 0:
        return "epsilon_sensitive_odd"
    if all_gap > 0:
        return "block_size_sensitive"
    return "subcritical"


def cascade_rows() -> list[dict[str, Any]]:
    """生成 p=2,3,5 的精确风险表。"""
    rows: list[dict[str, Any]] = []
    for p in [2, 3, 5]:
        all_e = exp_all(p)
        one_two_e = exp_one_two(p)
        all_gap = all_e - ALPHA
        one_two_gap = one_two_e - ALPHA
        rows.append(
            {
                "p": p,
                "all_grouped_exponent": all_e,
                "all_grouped_gap": all_gap,
                "one_two_exponent": one_two_e,
                "one_two_gap": one_two_gap,
                "risk_level": risk_level(all_gap, one_two_gap),
                "needed_input": {
                    2: DYADIC_CASCADE,
                    3: ODD_EPSILON,
                    5: BLOCK_REDUCTION,
                }[p],
            }
        )
    return rows


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成小素数幂级联判定表。"""
    kernel = data["kernel"]
    scaled = data["scaled"]

    target_imported = kernel.get("next_direct_attack_target") == SMALL_TABLE
    p235_identified = kernel.get("dangerous_bases_all_grouped_blocks") == [2, 3, 5]
    cold_hot = scaled.get("cold_hot_split_closed") is True

    return [
        row(
            "SmallPrimePowerTargetImported",
            target_imported,
            False,
            "上一层已把共同核预算主攻点压成 p=2,3,5 小素数幂级联表。",
            SMALL_TABLE,
        ),
        row(
            "P235DangerousSetIdentified",
            p235_identified,
            True,
            "全分组模型中超过 alpha 的底数恰为 2、3、5。",
            SMALL_TABLE,
        ),
        row(
            "ColdHotGateAvailable",
            cold_hot,
            False,
            "任何小素数幂级联若造成终端窗口过密，应回流热核心而不是留在冷供给。",
            COLD_ANTICASCADE,
        ),
        row(
            "P5ReducedToBlockSizeControl",
            True,
            True,
            "p=5 只在任意大块分组模型中刚越过阈值；一二步模型已低于 alpha。",
            BLOCK_REDUCTION,
        ),
        row(
            "P3ReducedToSmallEpsilonSaving",
            True,
            True,
            "p=3 在一二步模型只超出 alpha 约 0.008018，是弱奇素数危险。",
            ODD_EPSILON,
        ),
        row(
            "P2PrimaryCascadeIdentified",
            True,
            True,
            "p=2 在一二步模型仍超出 alpha 约 0.264242，是唯一强主危险。",
            DYADIC_CASCADE,
        ),
        row(
            "BlockSizeReductionProved",
            False,
            False,
            "尚未证明冷历史可统一降到一二步，或大块必触发热/固定回流。",
            BLOCK_REDUCTION,
        ),
        row(
            "OddPrimeEpsilonSavingProved",
            False,
            False,
            "尚未给出 p=3 所需的微小指数节省或冷窗口反级联。",
            ODD_EPSILON,
        ),
        row(
            "DyadicCascadeExclusionProved",
            False,
            False,
            "尚未排除 dyadic 冷窗口级联；这是当前最窄主硬点。",
            DYADIC_CASCADE,
        ),
        row(
            "SmallPrimePowerCascadeTableProved",
            False,
            False,
            "p=2 主危险与 p=3/5 辅助账本未闭合。",
            f"{DYADIC_CASCADE} AND {ODD_EPSILON} AND {BLOCK_REDUCTION}",
        ),
        row(
            "PrefixBranchingKernelMultiplicityBudgetProved",
            False,
            False,
            "小素数幂表未闭合，因此共同核重数预算仍未闭合。",
            KERNEL_BUDGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{DYADIC_CASCADE} AND {COLD_ANTICASCADE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造小素数幂级联攻坚证书。"""
    data = {
        "kernel": load_json("prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json"),
        "scaled": load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"),
    }
    rows = build_rows(data)
    risks = cascade_rows()

    return {
        "certificate_type": "prime_matrix_strict_small_prime_power_cascade_attack_router",
        "status": "small_prime_cascade_reduced_to_dyadic_primary_and_odd_epsilon_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "p235_dangerous_set_identified": True,
        "p5_block_size_sensitive_only": True,
        "p3_epsilon_sensitive_odd_case": True,
        "p2_primary_dyadic_case": True,
        "block_size_reduction_proved": False,
        "odd_prime_epsilon_saving_proved": False,
        "dyadic_cascade_exclusion_proved": False,
        "small_prime_power_cascade_table_proved": False,
        "prefix_branching_kernel_multiplicity_budget_proved": False,
        "cold_history_prefix_branching_hot_or_fixed_return_proved": False,
        "divisor_compatible_cold_history_tree_packing_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SMALL_TABLE,
        "hardpoint_after_router": f"{DYADIC_CASCADE} AND {ODD_EPSILON} AND {BLOCK_REDUCTION}",
        "next_direct_attack_target": DYADIC_CASCADE,
        "parallel_attack_targets": [
            ODD_EPSILON,
            BLOCK_REDUCTION,
            COLD_ANTICASCADE,
            KERNEL_BUDGET,
            PREFIX_BRANCHING,
            TREE_PACKING,
            DSTRUCTURE,
        ],
        "cascade_risk_rows": risks,
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SmallPrimePowerCascadeColdWindowExclusionTableForP235` 进一步拆成三层风险。"
            "`p=5` 的全分组指数只比 alpha 多约 0.000677，且一二步模型已低于 alpha，"
            "所以它主要需要大块分组降阶账本。`p=3` 的一二步指数只多约 0.008018，"
            "需要很小的奇素数节省或冷窗口反级联。`p=2` 即使在一二步 Fibonacci 模型中仍为 "
            "`P^0.694`，比 alpha 多约 0.264242，是当前唯一强主危险。"
            "因此下一最窄主攻点应集中到 `DyadicPrimePowerColdWindowCascadeExclusionLemma`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 小素数幂冷窗口级联攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"p235_dangerous_set_identified={fmt_bool(result['p235_dangerous_set_identified'])}",
        f"p5_block_size_sensitive_only={fmt_bool(result['p5_block_size_sensitive_only'])}",
        f"p3_epsilon_sensitive_odd_case={fmt_bool(result['p3_epsilon_sensitive_odd_case'])}",
        f"p2_primary_dyadic_case={fmt_bool(result['p2_primary_dyadic_case'])}",
        f"dyadic_cascade_exclusion_proved={fmt_bool(result['dyadic_cascade_exclusion_proved'])}",
        f"small_prime_power_cascade_table_proved={fmt_bool(result['small_prime_power_cascade_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## p=2,3,5 风险分层",
        "",
        "| p | all_grouped_exponent | all_gap | one_two_exponent | one_two_gap | risk_level | needed_input |",
        "|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in result["cascade_risk_rows"]:
        lines.append(
            "| "
            f"{item['p']} | "
            f"{item['all_grouped_exponent']:.6f} | "
            f"{item['all_grouped_gap']:.6f} | "
            f"{item['one_two_exponent']:.6f} | "
            f"{item['one_two_gap']:.6f} | "
            f"`{table_cell(item['risk_level'])}` | "
            f"`{table_cell(item['needed_input'])}` |"
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
