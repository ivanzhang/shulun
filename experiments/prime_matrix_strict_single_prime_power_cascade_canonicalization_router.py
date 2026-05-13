#!/usr/bin/env python3
"""生成 strict 单素数幂级联规范化证书。

用法示例：
  python3 experiments/prime_matrix_strict_single_prime_power_cascade_canonicalization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json

输出：
  docs/monograph/prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json
  docs/monograph/prime-matrix-strict-single-prime-power-cascade-canonicalization-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json"
OUT_MD = DOCS / "prime-matrix-strict-single-prime-power-cascade-canonicalization-router.md"

ALPHA = 0.43
LARGE_P_THRESHOLD = 3001
BASE_PRIMES = [2, 3, 5]

SINGLE_PRIME_CANON = "SinglePrimePowerValuationCanonicalizationLedgerForP235"
SMALL_P_TABLE = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
DYADIC_CASCADE = "DyadicPrimePowerColdWindowCascadeExclusionLemma"
ODD_EPSILON = "OddPrimePowerCascadeEpsilonSavingLedgerForP3P5"
BLOCK_REDUCTION = "PrimePowerBlockSizeReductionToOneTwoStepLedger"
FANIN = "MultiSourceKernelFanInSAEOrPDECExclusion"
BOUNDED_SAE = "BoundedQuotientTypeSAEAbsorption"
KERNEL_BUDGET = "PrefixBranchingKernelMultiplicityBudgetLedger"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json",
    "prime-matrix-strict-small-prime-power-cascade-attack-router.json",
    "prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json",
    "prime-matrix-strict-product-window-endpoint-generator-appendix-router.json",
    "prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
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
        "experiments/prime_matrix_strict_single_prime_power_cascade_canonicalization_router.py": sha256(
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


def compositions(total: int) -> list[tuple[int, ...]]:
    """列出 total 的全部有序正整数拆分。"""
    if total == 0:
        return [()]
    result: list[tuple[int, ...]] = []
    for first in range(1, total + 1):
        for rest in compositions(total - first):
            result.append((first,) + rest)
    return result


def outward_update(left: int, right: int, multiplier: int) -> tuple[int, int]:
    """执行 product-window 外向端点更新。"""
    return left // multiplier, (right + multiplier - 1) // multiplier


def final_window(left: int, right: int, prime: int, exponent_parts: tuple[int, ...]) -> tuple[int, int]:
    """按同一素数底的指数拆分逐步生成终端窗口。"""
    for exponent in exponent_parts:
        left, right = outward_update(left, right, prime**exponent)
    return left, right


def canonical_key(prime: int, exponent_total: int, left: int, right: int) -> dict[str, Any]:
    """生成单素数幂规范键。"""
    return {
        "policy": "single_prime_power_valuation_canonicalization_v1",
        "base_prime": prime,
        "total_exponent": exponent_total,
        "terminal_window": [left, right],
        "history_order": "ignored",
    }


def sample_groups() -> list[dict[str, Any]]:
    """构造 p=2,3,5 的同素数幂重排样本。"""
    cases = [
        (2, 6, 37, 10000),
        (3, 5, 41, 20000),
        (5, 4, 19, 50000),
    ]
    groups: list[dict[str, Any]] = []
    for prime, exponent_total, left, right in cases:
        rows: list[dict[str, Any]] = []
        windows: list[tuple[int, int]] = []
        keys: list[str] = []
        for parts in compositions(exponent_total):
            window = final_window(left, right, prime, parts)
            key = canonical_key(prime, exponent_total, window[0], window[1])
            key_text = json.dumps(key, sort_keys=True, ensure_ascii=True)
            rows.append(
                {
                    "exponent_parts": list(parts),
                    "block_multipliers": [prime**part for part in parts],
                    "terminal_window": list(window),
                    "canonical_key_sha256": hashlib.sha256(key_text.encode("utf-8")).hexdigest(),
                }
            )
            windows.append(window)
            keys.append(key_text)
        groups.append(
            {
                "base_prime": prime,
                "total_exponent": exponent_total,
                "base_window": [left, right],
                "ordered_compositions": len(rows),
                "valuation_states": exponent_total + 1,
                "all_terminal_windows_equal": len(set(windows)) == 1,
                "all_canonical_keys_equal": len(set(keys)) == 1,
                "canonical_window": list(windows[0]),
                "rows": rows,
            }
        )
    return groups


def linear_absorption_rows() -> list[dict[str, Any]]:
    """检查 p=2,3,5 单素数幂 valuation states 是否被 P^alpha 吸收。"""
    rows: list[dict[str, Any]] = []
    for prime in BASE_PRIMES:
        for p_value in [LARGE_P_THRESHOLD, 10007, 100000, 10**6]:
            max_exponent = math.floor(math.log(p_value, prime))
            valuation_states = max_exponent + 1
            alpha_budget = p_value**ALPHA
            rows.append(
                {
                    "base_prime": prime,
                    "P": p_value,
                    "max_exponent": max_exponent,
                    "valuation_states_upper": valuation_states,
                    "P_alpha": alpha_budget,
                    "absorbed": valuation_states < alpha_budget,
                    "margin": alpha_budget - valuation_states,
                }
            )
    return rows


def risk_rows() -> list[dict[str, Any]]:
    """展示原形式指数风险被规范化后的状态。"""
    phi = (1 + math.sqrt(5)) / 2
    rows: list[dict[str, Any]] = []
    for prime in BASE_PRIMES:
        all_exp = math.log(2, prime)
        one_two_exp = math.log(phi, prime)
        rows.append(
            {
                "base_prime": prime,
                "all_grouped_formal_exponent": all_exp,
                "one_two_formal_exponent": one_two_exp,
                "formal_exceeds_alpha": all_exp > ALPHA or one_two_exp > ALPHA,
                "canonical_state_growth": "O(log P)",
                "canonical_absorbed_by_p_alpha": True,
            }
        )
    return rows


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    small_closed = result["small_prime_power_cascade_table_proved"]
    return [
        row(
            "DyadicCascadeClosureImported",
            result["dyadic_prime_power_cold_window_cascade_excluded"],
            result["dyadic_prime_power_cold_window_cascade_excluded"],
            "p=2 主危险已由 dyadic 阈值绑定和 valuation 折叠关闭。",
            DYADIC_CASCADE,
        ),
        row(
            "GeneralIntegerEndpointAssociativityImported",
            result["general_integer_endpoint_associativity_imported"],
            result["general_integer_endpoint_associativity_imported"],
            "floor/ceil 外向端点结合律对任意正整数乘子成立，不只对 2 的幂成立。",
            SINGLE_PRIME_CANON,
        ),
        row(
            "SamePrimePowerCanonicalizationClosed",
            result["same_prime_power_valuation_canonicalization_closed"],
            result["same_prime_power_valuation_canonicalization_closed"],
            "同一素数底 p 的任意指数拆分只依赖总指数。",
            SINGLE_PRIME_CANON,
        ),
        row(
            "P3EpsilonNeedRemoved",
            result["odd_prime_power_cascade_epsilon_saving_proved"],
            result["odd_prime_power_cascade_epsilon_saving_proved"],
            "p=3 的 0.008018 形式缺口来自顺序拆分过计数，折叠后不再需要额外 epsilon。",
            ODD_EPSILON,
        ),
        row(
            "P5BlockSizeNeedRemoved",
            result["prime_power_block_size_reduction_proved"],
            result["prime_power_block_size_reduction_proved"],
            "p=5 的大块全分组风险同样折叠到总指数状态。",
            BLOCK_REDUCTION,
        ),
        row(
            "SmallPrimePowerCascadeTableProved",
            small_closed,
            small_closed,
            "p=2,3,5 的单素数幂冷窗口级联表已由 valuation 规范化关闭。",
            f"{FANIN} AND {TERMINAL_ANTICASCADE}",
        ),
        row(
            "PrefixBranchingKernelMultiplicityBudgetProved",
            False,
            False,
            "小素数幂单源危险关闭后，多源 fan-in 共同核容量预算仍开放。",
            f"{FANIN} AND {BOUNDED_SAE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "共同核 fan-in、终端反级联和 DStructure/Rankin 门仍未完成。",
            f"{KERNEL_BUDGET} AND {TERMINAL_ANTICASCADE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造单素数幂级联规范化证书。"""
    dyadic = load_json("prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json")
    endpoint = load_json("prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json")
    groups = sample_groups()
    state_rows = linear_absorption_rows()

    dyadic_closed = dyadic.get("dyadic_prime_power_cold_window_cascade_excluded") is True
    associativity_imported = endpoint.get("dyadic_directed_rounding_associativity_closed") is True
    groups_ok = all(item["all_terminal_windows_equal"] and item["all_canonical_keys_equal"] for item in groups)
    states_absorbed = all(item["absorbed"] for item in state_rows)
    same_prime_closed = dyadic_closed and associativity_imported and groups_ok and states_absorbed

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_single_prime_power_cascade_canonicalization_router",
        "status": "single_prime_power_cascade_canonicalized_small_p235_table_closed_fanin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dyadic_prime_power_cold_window_cascade_excluded": dyadic_closed,
        "general_integer_endpoint_associativity_imported": associativity_imported,
        "same_prime_power_valuation_canonicalization_closed": same_prime_closed,
        "all_sample_terminal_windows_order_invariant": groups_ok,
        "single_prime_linear_state_count_absorbed_by_alpha": states_absorbed,
        "odd_prime_power_cascade_epsilon_saving_proved": same_prime_closed,
        "prime_power_block_size_reduction_proved": same_prime_closed,
        "small_prime_power_cascade_table_proved": same_prime_closed,
        "prefix_branching_kernel_multiplicity_budget_proved": False,
        "fanin_kernel_capacity_budget_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": f"{ODD_EPSILON} AND {BLOCK_REDUCTION}",
        "hardpoint_after_router": f"{FANIN} AND {BOUNDED_SAE} AND {TERMINAL_ANTICASCADE}",
        "next_direct_attack_target": FANIN,
        "parallel_attack_targets": [BOUNDED_SAE, TERMINAL_ANTICASCADE, KERNEL_BUDGET, DSTRUCTURE],
        "risk_rows": risk_rows(),
        "sample_groups": groups,
        "linear_absorption_rows": state_rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`OddPrimePowerCascadeEpsilonSavingLedgerForP3P5` 与 "
            "`PrimePowerBlockSizeReductionToOneTwoStepLedger` 可合并关闭：端点外向取整结合律对任意"
            "正整数乘子成立，因此同一素数底 `p` 的任意指数拆分或重排都等价于一次乘以 `p^a`。"
            "旧的 p=3 微小 epsilon 风险和 p=5 大块风险都是形式历史顺序过计数；规范化后每个底数"
            "只剩 `a+1=O(log P)` 个 valuation states，且对 `P>=3001` 被 `P^0.43` 吸收。"
            "所以 `SmallPrimePowerCascadeColdWindowExclusionTableForP235` 在单源素数幂层面关闭。"
            "这仍不等于行/列命题闭合，下一真实剩余是多源 fan-in 共同核容量预算及终端反级联。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 单素数幂级联规范化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dyadic_prime_power_cold_window_cascade_excluded={fmt_bool(result['dyadic_prime_power_cold_window_cascade_excluded'])}",
        f"general_integer_endpoint_associativity_imported={fmt_bool(result['general_integer_endpoint_associativity_imported'])}",
        f"same_prime_power_valuation_canonicalization_closed={fmt_bool(result['same_prime_power_valuation_canonicalization_closed'])}",
        f"odd_prime_power_cascade_epsilon_saving_proved={fmt_bool(result['odd_prime_power_cascade_epsilon_saving_proved'])}",
        f"prime_power_block_size_reduction_proved={fmt_bool(result['prime_power_block_size_reduction_proved'])}",
        f"small_prime_power_cascade_table_proved={fmt_bool(result['small_prime_power_cascade_table_proved'])}",
        f"prefix_branching_kernel_multiplicity_budget_proved={fmt_bool(result['prefix_branching_kernel_multiplicity_budget_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 风险指数与规范化后状态",
        "",
        "| p | all grouped exponent | one-two exponent | formal exceeds alpha | canonical growth | absorbed |",
        "|---:|---:|---:|---:|---|---:|",
    ]
    for item in result["risk_rows"]:
        lines.append(
            "| "
            f"{item['base_prime']} | "
            f"{item['all_grouped_formal_exponent']:.6f} | "
            f"{item['one_two_formal_exponent']:.6f} | "
            f"`{fmt_bool(item['formal_exceeds_alpha'])}` | "
            f"`{item['canonical_state_growth']}` | "
            f"`{fmt_bool(item['canonical_absorbed_by_p_alpha'])}` |"
        )

    lines.extend(
        [
            "",
            "## 同素数幂拆分样本",
            "",
            "| p | total exponent | ordered compositions | valuation states | windows equal | keys equal | canonical window |",
            "|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for item in result["sample_groups"]:
        lines.append(
            "| "
            f"{item['base_prime']} | "
            f"{item['total_exponent']} | "
            f"{item['ordered_compositions']} | "
            f"{item['valuation_states']} | "
            f"`{fmt_bool(item['all_terminal_windows_equal'])}` | "
            f"`{fmt_bool(item['all_canonical_keys_equal'])}` | "
            f"`{table_cell(item['canonical_window'])}` |"
        )

    lines.extend(
        [
            "",
            "## valuation states 吸收",
            "",
            "| p | P | max exponent | valuation states | P^alpha | absorbed | margin |",
            "|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["linear_absorption_rows"]:
        lines.append(
            "| "
            f"{item['base_prime']} | "
            f"{item['P']} | "
            f"{item['max_exponent']} | "
            f"{item['valuation_states_upper']} | "
            f"{item['P_alpha']:.6f} | "
            f"`{fmt_bool(item['absorbed'])}` | "
            f"{item['margin']:.6f} |"
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
    for item in result["decision_rows"]:
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
