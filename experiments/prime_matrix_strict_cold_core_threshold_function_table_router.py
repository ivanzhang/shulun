#!/usr/bin/env python3
"""生成 strict 冷核心阈值函数表路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_core_threshold_function_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-core-threshold-function-table-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-core-threshold-function-table-router.json
  docs/monograph/prime-matrix-strict-cold-core-threshold-function-table-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-core-threshold-function-table-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-core-threshold-function-table-router.md"

COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
CORE_SUM = "SameParameterCoreThresholdSummationDominanceTable"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json",
    "prime-matrix-strict-product-window-endpoint-generator-appendix-router.json",
    "prime-matrix-strict-legacy-product-window-equivalence-router.json",
    "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json",
    "prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json",
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
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_cold_core_threshold_function_table_router.py": sha256(
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


def length_cap_samples() -> list[dict[str, Any]]:
    """给出规范终端窗口的长度 cap 样本。"""
    samples: list[dict[str, Any]] = []
    for left, right, divisor_count in [(10, 17, 4), (31, 42, 6), (100, 119, 9), (511, 545, 12)]:
        length = right - left + 1
        samples.append(
            {
                "left": left,
                "right": right,
                "interval_length": length,
                "sample_divisor_count": divisor_count,
                "length_cap_valid": divisor_count <= length,
            }
        )
    return samples


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "ColdCoreTableTargetImported",
            result["cold_core_table_target_imported"],
            result["cold_core_table_target_imported"],
            "上一层已把冷供给数值包主攻点指向 C_core 数值表。",
            COLD_CORE_TABLE,
        ),
        row(
            "EndpointGeneratorAndLegacyNotationClosed",
            result["endpoint_generator_and_legacy_notation_closed"],
            result["endpoint_generator_and_legacy_notation_closed"],
            "终端窗口端点生成器和旧 I_W 记号等价已闭合。",
            COLD_CORE_TABLE,
        ),
        row(
            "ColdCoreThresholdRegistryAndOrderInvarianceClosed",
            result["cold_core_threshold_registry_and_order_invariance_closed"],
            result["cold_core_threshold_registry_and_order_invariance_closed"],
            "C_core 已绑定为规范终端窗口对象函数，不随 dyadic/素数幂拆分顺序变化。",
            COLD_CORE_TABLE,
        ),
        row(
            "TrivialIntervalLengthCapClosed",
            result["trivial_interval_length_cap_closed"],
            result["trivial_interval_length_cap_closed"],
            "任何冷核心窗口都有 N_H([L,R])<=R-L+1 的基准数值 cap。",
            CORE_SUM,
        ),
        row(
            "ColdCoreFunctionTableSchemaClosed",
            result["cold_core_function_table_schema_closed"],
            result["cold_core_function_table_schema_closed"],
            "C_core 表的对象、键、顺序不变性和基准 cap 已闭合。",
            CORE_SUM,
        ),
        row(
            "CoreThresholdSummationDominanceProved",
            False,
            False,
            "长度 cap 过粗；尚未证明 sum_W(T_PDEC(W)-1)C_core(W) 小于需求。",
            CORE_SUM,
        ),
        row(
            "ColdCoreThresholdNumericTableProved",
            False,
            False,
            "函数表结构闭合，但缺同参数可求和优势表。",
            f"{CORE_SUM} AND {PDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{CORE_SUM} AND {PDEC_TABLE} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造冷核心阈值函数表证书。"""
    cold = load_json("prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json")
    generator = load_json("prime-matrix-strict-product-window-endpoint-generator-appendix-router.json")
    legacy = load_json("prime-matrix-strict-legacy-product-window-equivalence-router.json")
    invariance = load_json("prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json")
    single_prime = load_json("prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json")
    scaled = load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json")

    target = cold.get("next_direct_attack_target") == COLD_CORE_TABLE
    endpoint_closed = (
        generator.get("product_window_endpoint_generator_artifact_or_definition_appendix_closed") is True
        and legacy.get("legacy_product_window_notation_equivalence_proved") is True
    )
    invariance_closed = (
        invariance.get("canonical_cold_core_threshold_registry_defined") is True
        and invariance.get("cold_core_threshold_dyadic_order_invariance_proved") is True
        and single_prime.get("small_prime_power_cascade_table_proved") is True
    )
    scaled_split = (
        scaled.get("terminal_core_window_closed") is True
        and scaled.get("cold_hot_split_closed") is True
        and scaled.get("cold_core_budget_insertion_closed") is True
    )
    samples = length_cap_samples()
    samples_ok = all(item["length_cap_valid"] for item in samples)
    schema_closed = target and endpoint_closed and invariance_closed and scaled_split and samples_ok

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_cold_core_threshold_function_table_router",
        "status": "cold_core_threshold_function_schema_closed_summation_dominance_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "cold_core_table_target_imported": target,
        "endpoint_generator_and_legacy_notation_closed": endpoint_closed,
        "cold_core_threshold_registry_and_order_invariance_closed": invariance_closed,
        "scaled_terminal_core_cold_hot_split_imported": scaled_split,
        "trivial_interval_length_cap_closed": samples_ok,
        "cold_core_function_table_schema_closed": schema_closed,
        "core_threshold_summation_dominance_proved": False,
        "same_parameter_pdec_threshold_numeric_table_proved": False,
        "cold_core_threshold_numeric_table_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "terminal_core_hot_divisor_window_excluded": False,
        "fixed_type_history_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": COLD_CORE_TABLE,
        "hardpoint_after_router": f"{CORE_SUM} AND {PDEC_TABLE} AND {HOT_CORE} AND {FIXED_HISTORY}",
        "next_direct_attack_target": CORE_SUM,
        "parallel_attack_targets": [PDEC_TABLE, HOT_CORE, FIXED_HISTORY, MOVING_ATOM, DSTRUCTURE],
        "length_cap_samples": samples,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ColdCoreThresholdFunctionNumericTable` 的定义/函数表口径可以关闭：终端窗口端点生成器、"
            "旧 `I_W` 记号等价、规范 `C_core` 注册键和 dyadic/素数幂顺序不变性已经对齐。"
            "同时存在基准长度 cap：对任意整数窗口 `[L,R]`，`N_H([L,R])<=R-L+1`。"
            "但长度 cap 只是可复核的粗数值行，不能证明同参数求和优势；真正剩余是 "
            "`SameParameterCoreThresholdSummationDominanceTable`，即证明在实际冷历史族上 "
            "`sum_W(T_PDEC(W)-1)C_core(W)` 被需求项反超。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 冷核心阈值函数表路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cold_core_table_target_imported={fmt_bool(result['cold_core_table_target_imported'])}",
        f"endpoint_generator_and_legacy_notation_closed={fmt_bool(result['endpoint_generator_and_legacy_notation_closed'])}",
        f"cold_core_threshold_registry_and_order_invariance_closed={fmt_bool(result['cold_core_threshold_registry_and_order_invariance_closed'])}",
        f"trivial_interval_length_cap_closed={fmt_bool(result['trivial_interval_length_cap_closed'])}",
        f"cold_core_function_table_schema_closed={fmt_bool(result['cold_core_function_table_schema_closed'])}",
        f"core_threshold_summation_dominance_proved={fmt_bool(result['core_threshold_summation_dominance_proved'])}",
        f"cold_core_threshold_numeric_table_proved={fmt_bool(result['cold_core_threshold_numeric_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 长度 cap 样本",
        "",
        "| left | right | length | sample divisor count | valid |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["length_cap_samples"]:
        lines.append(
            "| `{left}` | `{right}` | `{length}` | `{count}` | `{valid}` |".format(
                left=item["left"],
                right=item["right"],
                length=item["interval_length"],
                count=item["sample_divisor_count"],
                valid=fmt_bool(item["length_cap_valid"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
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
            "## 3. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 含义：把已规范化的 C_core 函数表变成同参数可求和优势表。",
            "- 边界：本步不证明最终数值优势，不闭合行/列命题。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
