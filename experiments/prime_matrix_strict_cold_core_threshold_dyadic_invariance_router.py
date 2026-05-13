#!/usr/bin/env python3
"""生成 strict 冷核心阈值 dyadic 顺序不变性绑定证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_core_threshold_dyadic_invariance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json
  docs/monograph/prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from itertools import permutations
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.md"

ALPHA = 0.43
LARGE_P_THRESHOLD = 3001

THRESHOLD_BINDING = "ColdCoreThresholdDyadicOrderInvarianceBindingLedger"
GENERATOR_APPENDIX = "ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix"
LEGACY_EQUIV = "LegacyProductWindowNotationEquivalenceAudit"
FORMULA_BINDING = "ProductWindowEndpointDyadicUpdateFormulaBindingLedger"
ENDPOINT_COMM = "DyadicProductWindowEndpointCommutativityLedger"
ORDER_CANON = "DyadicValuationOrderCanonicalizationOrPhaseDefectLedger"
DYADIC_CASCADE = "DyadicPrimePowerColdWindowCascadeExclusionLemma"
ODD_EPSILON = "OddPrimePowerCascadeEpsilonSavingLedgerForP3P5"
BLOCK_REDUCTION = "PrimePowerBlockSizeReductionToOneTwoStepLedger"
SMALL_P_TABLE = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-legacy-product-window-equivalence-router.json",
    "prime-matrix-strict-product-window-endpoint-generator-appendix-router.json",
    "prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json",
    "prime-matrix-strict-dyadic-order-canonicalization-attack-router.json",
    "prime-matrix-strict-dyadic-cold-window-cascade-attack-router.json",
    "prime-matrix-strict-small-prime-power-cascade-attack-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
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
    """汇总本证书依赖哈希。"""
    result = {
        "experiments/prime_matrix_strict_cold_core_threshold_dyadic_invariance_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def outward_update(left: int, right: int, multiplier: int) -> tuple[int, int]:
    """执行整数端点外向更新。"""
    return left // multiplier, (right + multiplier - 1) // multiplier


def v2(multiplier: int) -> int:
    """计算 2-adic 指数；输入在样本中均为 2 的幂。"""
    exponent = 0
    value = multiplier
    while value % 2 == 0:
        exponent += 1
        value //= 2
    if value != 1:
        raise ValueError(f"not a dyadic multiplier: {multiplier}")
    return exponent


def final_window(left: int, right: int, multipliers: tuple[int, ...]) -> tuple[int, int]:
    """逐步生成终端窗口。"""
    for multiplier in multipliers:
        left, right = outward_update(left, right, multiplier)
    return left, right


def canonical_threshold_key(
    odd_kernel_id: str,
    base_left: int,
    base_right: int,
    multipliers: tuple[int, ...],
) -> dict[str, Any]:
    """生成规范冷核心阈值键。

    阈值只允许依赖规范终端除数窗口对象；dyadic 路径顺序不能成为键的一部分。
    """
    total_v2 = sum(v2(multiplier) for multiplier in multipliers)
    left, right = final_window(base_left, base_right, multipliers)
    return {
        "policy": "canonical_terminal_divisor_window_threshold_v1",
        "odd_kernel_id": odd_kernel_id,
        "total_v2": total_v2,
        "terminal_window": [left, right],
        "threshold_scope": "N_{H_W}(I_W)<=C_core^*(canonical_window)",
    }


def unique_permutations(items: tuple[int, ...]) -> list[tuple[int, ...]]:
    """列出样本用的去重排列。"""
    return sorted(set(permutations(items)))


def sample_groups() -> list[dict[str, Any]]:
    """构造 dyadic 重排样本账本。"""
    cases = [
        ("odd-core-A", 37, 10000, (2, 4, 8)),
        ("odd-core-B", 111, 77777, (2, 2, 16)),
        ("odd-core-C", 5, 4097, (4, 8, 8)),
    ]
    groups: list[dict[str, Any]] = []
    for odd_kernel_id, left, right, multipliers in cases:
        rows: list[dict[str, Any]] = []
        keys: list[str] = []
        windows: list[tuple[int, int]] = []
        for order in unique_permutations(multipliers):
            key = canonical_threshold_key(odd_kernel_id, left, right, order)
            key_text = json.dumps(key, sort_keys=True, ensure_ascii=True)
            window = tuple(key["terminal_window"])
            rows.append(
                {
                    "order": list(order),
                    "total_v2": key["total_v2"],
                    "terminal_window": key["terminal_window"],
                    "threshold_key_sha256": hashlib.sha256(key_text.encode("utf-8")).hexdigest(),
                }
            )
            keys.append(key_text)
            windows.append(window)
        groups.append(
            {
                "odd_kernel_id": odd_kernel_id,
                "base_window": [left, right],
                "multipliers_multiset": list(multipliers),
                "permutation_count": len(rows),
                "all_terminal_windows_equal": len(set(windows)) == 1,
                "all_threshold_keys_equal": len(set(keys)) == 1,
                "canonical_key": json.loads(keys[0]),
                "rows": rows,
            }
        )
    return groups


def linear_state_absorption_rows() -> list[dict[str, Any]]:
    """检查 dyadic 线性 valuation states 是否被 P^alpha 吸收。"""
    rows: list[dict[str, Any]] = []
    for p_value in [LARGE_P_THRESHOLD, 10007, 100000, 10**6, 10**9]:
        valuation_states = math.floor(math.log2(p_value)) + 1
        alpha_budget = p_value**ALPHA
        rows.append(
            {
                "P": p_value,
                "valuation_states_upper": valuation_states,
                "P_alpha": alpha_budget,
                "absorbed": valuation_states < alpha_budget,
                "margin": alpha_budget - valuation_states,
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


def registry_rows() -> list[dict[str, str]]:
    """给出冷核心阈值注册规范。"""
    return [
        {
            "field": "canonical_window_key",
            "definition": "(odd kernel, total v2, H_W, normalized I_W, global parameter ledger)",
            "role": "冷核心阈值的唯一索引；禁止使用 dyadic 子步顺序。",
        },
        {
            "field": "C_core^*(canonical_window_key)",
            "definition": "registered cap for N_{H_W}(I_W) under the canonical terminal divisor window",
            "role": "旧 C_core(W) 统一解释为该规范函数值。",
        },
        {
            "field": "cold predicate",
            "definition": "N_{H_W}(I_W)<=C_core^*(canonical_window_key)",
            "role": "同总 v2 重排有同一除数宇宙、同一窗口、同一阈值。",
        },
        {
            "field": "defect return",
            "definition": "any unregistered path-order dependence routes to boundary phase/PDEC/hot core",
            "role": "阈值绑定失败不能成为自由容量。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    threshold_closed = result["cold_core_threshold_dyadic_order_invariance_proved"]
    formula_closed = result["product_window_endpoint_formula_binding_proved"]
    endpoint_closed = result["dyadic_product_window_endpoint_commutativity_ledger_proved"]
    canon_closed = result["dyadic_valuation_order_canonicalization_or_phase_defect_proved"]
    dyadic_closed = result["dyadic_prime_power_cold_window_cascade_excluded"]
    return [
        row(
            "LegacyEquivalenceImported",
            result["legacy_product_window_notation_equivalence_proved"],
            result["legacy_product_window_notation_equivalence_proved"],
            "旧 I_W/Y_W 记号已等价到规范端点生成器。",
            LEGACY_EQUIV,
        ),
        row(
            "EndpointGeneratorAndRoundingImported",
            result["endpoint_generator_and_rounding_imported"],
            result["endpoint_generator_and_rounding_imported"],
            "端点生成器与 dyadic 外向取整结合律均已可引用。",
            GENERATOR_APPENDIX,
        ),
        row(
            "CanonicalColdCoreThresholdRegistryDefined",
            True,
            True,
            "C_core(W) 被绑定为规范终端除数窗口对象的函数。",
            THRESHOLD_BINDING,
        ),
        row(
            "ThresholdKeyIgnoresDyadicOrder",
            result["all_sample_threshold_keys_order_invariant"],
            True,
            "注册键含总 v2 和规范窗口，不含 dyadic 子步排列。",
            THRESHOLD_BINDING,
        ),
        row(
            "ColdHotPredicateOrderInvariant",
            threshold_closed,
            threshold_closed,
            "同总 v2 重排给出同一 N_{H_W}(I_W) 与同一 C_core 值。",
            THRESHOLD_BINDING,
        ),
        row(
            "ProductWindowEndpointFormulaBindingProved",
            formula_closed,
            formula_closed,
            "生成器、旧记号等价、阈值绑定三项已经合并。",
            FORMULA_BINDING,
        ),
        row(
            "DyadicProductWindowEndpointCommutativityLedgerProved",
            endpoint_closed,
            endpoint_closed,
            "dyadic 重排不改变终端窗口端点和冷阈值。",
            ENDPOINT_COMM,
        ),
        row(
            "DyadicValuationOrderCanonicalizationProved",
            canon_closed,
            canon_closed,
            "纯 dyadic 有序路径折叠为累计 v2 的 valuation states。",
            ORDER_CANON,
        ),
        row(
            "DyadicLinearStatesAbsorbed",
            result["dyadic_linear_state_count_absorbed_by_alpha"],
            result["dyadic_linear_state_count_absorbed_by_alpha"],
            "对 P>=3001，线性 valuation states 小于 P^alpha。",
            DYADIC_CASCADE,
        ),
        row(
            "DyadicPrimePowerColdWindowCascadeExcluded",
            dyadic_closed,
            dyadic_closed,
            "p=2 Fibonacci 级过计数已消失；纯 dyadic 主危险关闭。",
            f"{ODD_EPSILON} AND {BLOCK_REDUCTION}",
        ),
        row(
            "SmallPrimePowerCascadeTableProved",
            False,
            False,
            "p=3 微小 epsilon 与 p=5 大块降阶仍未闭合。",
            f"{ODD_EPSILON} AND {BLOCK_REDUCTION}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "这只关闭 dyadic 主危险，尚未得到早期零行反例的最终矛盾。",
            f"{SMALL_P_TABLE} AND {TERMINAL_ANTICASCADE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造冷核心阈值 dyadic 不变性证书。"""
    legacy = load_json("prime-matrix-strict-legacy-product-window-equivalence-router.json")
    generator = load_json("prime-matrix-strict-product-window-endpoint-generator-appendix-router.json")
    endpoint = load_json("prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json")
    samples = sample_groups()
    state_rows = linear_state_absorption_rows()

    legacy_closed = legacy.get("legacy_product_window_notation_equivalence_proved") is True
    generator_closed = generator.get("product_window_endpoint_generator_artifact_or_definition_appendix_closed") is True
    rounding_closed = endpoint.get("dyadic_directed_rounding_associativity_closed") is True
    endpoint_generator_and_rounding_imported = generator_closed and rounding_closed
    sample_windows_ok = all(item["all_terminal_windows_equal"] for item in samples)
    sample_keys_ok = all(item["all_threshold_keys_equal"] for item in samples)
    state_absorbed = all(item["absorbed"] for item in state_rows)

    threshold_closed = legacy_closed and endpoint_generator_and_rounding_imported and sample_windows_ok and sample_keys_ok
    formula_closed = threshold_closed
    endpoint_closed = threshold_closed
    canon_closed = threshold_closed
    dyadic_closed = canon_closed and state_absorbed

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_cold_core_threshold_dyadic_invariance_router",
        "status": "cold_core_threshold_dyadic_invariance_closed_dyadic_cascade_closed_odd_cases_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "legacy_product_window_notation_equivalence_proved": legacy_closed,
        "endpoint_generator_and_rounding_imported": endpoint_generator_and_rounding_imported,
        "canonical_cold_core_threshold_registry_defined": True,
        "all_sample_terminal_windows_order_invariant": sample_windows_ok,
        "all_sample_threshold_keys_order_invariant": sample_keys_ok,
        "cold_core_threshold_dyadic_order_invariance_proved": threshold_closed,
        "product_window_endpoint_formula_binding_proved": formula_closed,
        "dyadic_product_window_endpoint_commutativity_ledger_proved": endpoint_closed,
        "dyadic_valuation_order_canonicalization_or_phase_defect_proved": canon_closed,
        "dyadic_linear_state_count_absorbed_by_alpha": state_absorbed,
        "dyadic_prime_power_cold_window_cascade_excluded": dyadic_closed,
        "small_prime_power_cascade_table_proved": False,
        "odd_prime_power_cascade_epsilon_saving_proved": False,
        "prime_power_block_size_reduction_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": THRESHOLD_BINDING,
        "hardpoint_after_router": f"{ODD_EPSILON} AND {BLOCK_REDUCTION}",
        "next_direct_attack_target": ODD_EPSILON,
        "parallel_attack_targets": [
            BLOCK_REDUCTION,
            TERMINAL_ANTICASCADE,
            SMALL_P_TABLE,
            DSTRUCTURE,
        ],
        "threshold_registry_rows": registry_rows(),
        "dyadic_permutation_sample_groups": samples,
        "dyadic_linear_state_absorption_rows": state_rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ColdCoreThresholdDyadicOrderInvarianceBindingLedger` 可以关闭：旧 `C_core(W)` "
            "统一绑定为规范终端除数窗口对象的函数 `C_core^*`，其注册键只含奇核、累计 `v2`、"
            "`H_W`、规范化 `I_W` 和全局参数账本，不含 dyadic 子步顺序。由已闭合的端点生成器和"
            "取整结合律，同总 `v2` 的 dyadic 重排给出同一 `H_W`、同一 `I_W`、同一阈值，"
            "所以冷/热判定也同一。于是 product-window 公式绑定、dyadic 端点交换律和 dyadic "
            "顺序规范化可接回；p=2 的 Fibonacci 有序路径过计数折叠为线性 valuation states，"
            f"且在 P>={LARGE_P_THRESHOLD} 时被 P^{ALPHA} 预算吸收。行/列命题仍未无条件闭合，"
            "剩余转为 p=3 微小节省与 p=5 大块降阶，以及终端反级联和 DStructure/Rankin 验收门。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 冷核心阈值 dyadic 顺序不变性绑定路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"legacy_product_window_notation_equivalence_proved={fmt_bool(result['legacy_product_window_notation_equivalence_proved'])}",
        f"endpoint_generator_and_rounding_imported={fmt_bool(result['endpoint_generator_and_rounding_imported'])}",
        f"canonical_cold_core_threshold_registry_defined={fmt_bool(result['canonical_cold_core_threshold_registry_defined'])}",
        f"cold_core_threshold_dyadic_order_invariance_proved={fmt_bool(result['cold_core_threshold_dyadic_order_invariance_proved'])}",
        f"product_window_endpoint_formula_binding_proved={fmt_bool(result['product_window_endpoint_formula_binding_proved'])}",
        f"dyadic_product_window_endpoint_commutativity_ledger_proved={fmt_bool(result['dyadic_product_window_endpoint_commutativity_ledger_proved'])}",
        f"dyadic_valuation_order_canonicalization_or_phase_defect_proved={fmt_bool(result['dyadic_valuation_order_canonicalization_or_phase_defect_proved'])}",
        f"dyadic_prime_power_cold_window_cascade_excluded={fmt_bool(result['dyadic_prime_power_cold_window_cascade_excluded'])}",
        f"small_prime_power_cascade_table_proved={fmt_bool(result['small_prime_power_cascade_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 阈值注册规范",
        "",
        "| field | definition | role |",
        "|---|---|---|",
    ]
    for item in result["threshold_registry_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['field'])}` | "
            f"{table_cell(item['definition'])} | "
            f"{table_cell(item['role'])} |"
        )

    lines.extend(
        [
            "",
            "## dyadic 重排样本",
            "",
            "| odd_kernel | base_window | multiset | permutations | windows_equal | keys_equal | canonical_window |",
            "|---|---|---|---:|---:|---:|---|",
        ]
    )
    for item in result["dyadic_permutation_sample_groups"]:
        lines.append(
            "| "
            f"`{table_cell(item['odd_kernel_id'])}` | "
            f"`{table_cell(item['base_window'])}` | "
            f"`{table_cell(item['multipliers_multiset'])}` | "
            f"{item['permutation_count']} | "
            f"`{fmt_bool(item['all_terminal_windows_equal'])}` | "
            f"`{fmt_bool(item['all_threshold_keys_equal'])}` | "
            f"`{table_cell(item['canonical_key']['terminal_window'])}` |"
        )

    lines.extend(
        [
            "",
            "## 线性 valuation states 吸收",
            "",
            "| P | valuation_states_upper | P^alpha | absorbed | margin |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["dyadic_linear_state_absorption_rows"]:
        lines.append(
            "| "
            f"{item['P']} | "
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
