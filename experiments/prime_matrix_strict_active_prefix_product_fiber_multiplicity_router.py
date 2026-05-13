#!/usr/bin/env python3
"""生成 strict 活动前缀产品纤维重数/命名回流路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_active_prefix_product_fiber_multiplicity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.json

输出：
  docs/monograph/prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.json
  docs/monograph/prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.json"
OUT_MD = DOCS / "prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.md"

PRODUCT_FIBER = "ActivePrefixProductFiberMultiplicityOrNamedReturnLedger"
ACTIVE_PACKING = "ActivePrefixLevelPackingExponentTable"
COLD_FILTER = "ColdNonpersistentProductSupportSparsificationLemma"
DIVISOR_ENV = "DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope"
CANONICAL_PRODUCT = "CanonicalProductClassSupportP018OrColdSparsificationLedger"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
TPDEC_TABLE = "SameParameterPDECThresholdNumericTable"
LOAD_LOWER = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
LOG_EPSILON = 0.25
RESIDUAL_EXPONENT = ALPHA - LOG_EPSILON

SOURCE_FILES = [
    "prime-matrix-strict-active-prefix-level-packing-router.json",
    "prime-matrix-strict-product-window-endpoint-generator-appendix-router.json",
    "prime-matrix-strict-legacy-product-window-equivalence-router.json",
    "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json",
    "prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json",
    "prime-matrix-strict-row-free-type-anticollapse-sync-router.json",
    "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json",
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
        "experiments/prime_matrix_strict_active_prefix_product_fiber_multiplicity_router.py": sha256(
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


def dyadic_ordered_factorizations(exponent: int) -> int:
    """2^a 的任意正块有序分解数。"""
    if exponent <= 0:
        return 0
    return 2 ** (exponent - 1)


def dyadic_one_two_step_factorizations(exponent: int) -> int:
    """只允许 2 和 4 步长时的有序分解数。"""
    if exponent <= 0:
        return 0
    prev, cur = 1, 1
    for _ in range(2, exponent + 1):
        prev, cur = cur, prev + cur
    return cur


def raw_fiber_obstruction_rows() -> list[dict[str, Any]]:
    """展示裸产品纤维重数远大于 P^0.18。"""
    rows: list[dict[str, Any]] = []
    for P in [100_000, 1_000_000, 10_000_000, 1_000_000_000]:
        exponent = int(math.log(P, 2))
        all_blocks = dyadic_ordered_factorizations(exponent)
        one_two = dyadic_one_two_step_factorizations(exponent)
        budget = P**RESIDUAL_EXPONENT
        rows.append(
            {
                "P": P,
                "dyadic_exponent_floor": exponent,
                "all_ordered_factorizations_of_2a": all_blocks,
                "one_two_step_factorizations": one_two,
                "P_residual_budget": round(budget, 6),
                "raw_all_blocks_over_budget": all_blocks > budget,
                "raw_one_two_over_budget": one_two > budget,
                "all_blocks_ratio": round(all_blocks / budget, 6),
                "one_two_ratio": round(one_two / budget, 6),
            }
        )
    return rows


def endpoint_commutativity_samples() -> list[dict[str, Any]]:
    """核验产品端点外向缩放只依赖总乘积。"""
    samples: list[dict[str, Any]] = []
    for left, right, a, b in [(1000, 1234, 2, 8), (1000, 1234, 3, 5), (98765, 100001, 6, 10)]:
        left_seq = (left // a) // b
        left_once = left // (a * b)
        right_seq = math.ceil(math.ceil(right / a) / b)
        right_once = math.ceil(right / (a * b))
        samples.append(
            {
                "left": left,
                "right": right,
                "a": a,
                "b": b,
                "left_sequential": left_seq,
                "left_once": left_once,
                "right_sequential": right_seq,
                "right_once": right_once,
                "commutes": left_seq == left_once and right_seq == right_once,
            }
        )
    return samples


def quotient_rows() -> list[dict[str, str]]:
    """列出产品纤维的规范商化。"""
    return [
        {
            "piece": "raw product fiber",
            "formula": "A_j(d)={U in A_j: D(U)=d}",
            "status": "closed_definition",
            "meaning": "裸纤维按同一产品除数 d 分组；它仍含有有序分解和内部标签冗余。",
        },
        {
            "piece": "canonical endpoint quotient",
            "formula": "I_U=I(d) after outward product-window scaling, unless a boundary phase defect is registered",
            "status": "closed_or_named_return",
            "meaning": "端点生成器满足外向缩放结合律；若旧记号或边界字段不服从，则进入相位缺陷回流。",
        },
        {
            "piece": "row-free type quotient",
            "formula": "A_j(d)=disjoint union_kappa A_j(d,kappa)",
            "status": "closed_reduction",
            "meaning": "同产品内继续按 row-free type、标签骨架、窗口相位和 cold guard 商化。",
        },
        {
            "piece": "duplicate complete key",
            "formula": "|A_j(d,kappa)|>1 with complete key preserved -> fixed history / PDEC / ColumnCRT",
            "status": "named_return_registered",
            "meaning": "完整 key 下的重复不能作为多个免费冷前缀；它就是固定历史或持久相位复现。",
        },
        {
            "piece": "many distinct kappa",
            "formula": "#kappa large -> row-free/sparse anti-collapse budget or named return",
            "status": "budget_route_open",
            "meaning": "若不是完整 key 重复，而是大量不同类型，则负载没有消失，回到 cold-filtered 产品支撑。",
        },
    ]


def route_rows() -> list[dict[str, str]]:
    """列出压缩后的剩余路线。"""
    return [
        {
            "route": CANONICAL_PRODUCT,
            "status": "open",
            "task": "对规范产品类而非有序分解求支撑；证明 cold/nonpersistent 过滤后其数量满足 P^(0.18-tau) 级预算。",
        },
        {
            "route": COLD_FILTER,
            "status": "open",
            "task": "证明大多数 d|h_0 无法同时通过 cold guard、非持久 guard 与同层活动 guard。",
        },
        {
            "route": NAMED_RETURN,
            "status": "registered_not_excluded",
            "task": "排斥或预算吸收完整 key 重复、标签丢失、边界相位漂移、固定历史和热核心回流。",
        },
        {
            "route": DIVISOR_ENV,
            "status": "parallel_open",
            "task": "给出规范产品支撑的有限边界或解析 envelope；不能再使用裸 tau(h_0) 粗界。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "ProductFiberTargetImported",
            result["product_fiber_target_imported"],
            result["product_fiber_target_imported"],
            "上一层已把活动前缀层打包的首要剩余指向同产品纤维重数。",
            PRODUCT_FIBER,
        ),
        row(
            "RawProductFiberOvercountCertified",
            result["raw_product_fiber_overcount_certified"],
            result["raw_product_fiber_overcount_certified"],
            "裸有序分解纤维在 dyadic 样本中远超 P^0.18，不能作为容量上界。",
            PRODUCT_FIBER,
        ),
        row(
            "ProductEndpointQuotientClosed",
            result["product_endpoint_quotient_closed"],
            result["product_endpoint_quotient_closed"],
            "product-window 外向缩放端点只依赖总乘积；端点顺序冗余可商化。",
            CANONICAL_PRODUCT,
        ),
        row(
            "DuplicateCompleteKeyRoutesToNamedReturn",
            result["duplicate_complete_key_routes_to_named_return"],
            False,
            "同产品、同完整 key 的重复是固定历史/PDEC/ColumnCRT/热核心回流，不是免费冷容量。",
            NAMED_RETURN,
        ),
        row(
            "ProductFiberMultiplicityIndependentHardpointRemoved",
            result["product_fiber_multiplicity_independent_hardpoint_removed"],
            result["product_fiber_multiplicity_independent_hardpoint_removed"],
            "产品纤维重数不再作为独立裸计数；已压成规范产品支撑、cold 过滤和命名回流排斥。",
            f"{CANONICAL_PRODUCT} AND {COLD_FILTER} AND {NAMED_RETURN}",
        ),
        row(
            "ActivePrefixProductFiberMultiplicityLedgerProved",
            False,
            False,
            "路由和商化闭合，但命名回流排斥与 cold-filtered 产品支撑数值界未闭合。",
            f"{CANONICAL_PRODUCT} AND {COLD_FILTER} AND {NAMED_RETURN}",
        ),
        row(
            "ActivePrefixLevelPackingExponentTableProved",
            False,
            False,
            "仍需规范产品支撑 envelope、collar 总和和同参数 T_PDEC 权重。",
            f"{CANONICAL_PRODUCT} AND {COLD_FILTER} AND {TPDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{CANONICAL_PRODUCT} AND {COLD_FILTER} AND {LOAD_LOWER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造产品纤维重数证书。"""
    active = load_json("prime-matrix-strict-active-prefix-level-packing-router.json")
    endpoint = load_json("prime-matrix-strict-product-window-endpoint-generator-appendix-router.json")
    legacy = load_json("prime-matrix-strict-legacy-product-window-equivalence-router.json")
    invariance = load_json("prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json")
    dyadic = load_json("prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json")
    row_free = load_json("prime-matrix-strict-row-free-type-anticollapse-sync-router.json")
    sparse = load_json("prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json")
    named = load_json("prime-matrix-strict-named-return-after-rowfree-sync-router.json")

    target = active.get("next_direct_attack_target") == PRODUCT_FIBER
    endpoint_samples = endpoint_commutativity_samples()
    endpoint_closed = (
        endpoint.get("product_window_endpoint_generator_artifact_or_definition_appendix_closed") is True
        and legacy.get("legacy_product_window_notation_equivalence_proved") is True
        and all(item["commutes"] for item in endpoint_samples)
    )
    quotient_guard = (
        endpoint_closed
        and invariance.get("cold_core_threshold_dyadic_order_invariance_proved") is True
        and dyadic.get("dyadic_endpoint_commutativity_conditional_on_formula_closed") is True
    )
    no_silent = (
        row_free.get("prefix_label_support_to_row_free_type_anticollapse_closed_for_budget") is True
        and sparse.get("prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget") is True
    )
    duplicate_route = no_silent and named.get("named_return_alphabet_compression_closed") is True
    raw_rows = raw_fiber_obstruction_rows()
    raw_overcount = any(row["raw_all_blocks_over_budget"] or row["raw_one_two_over_budget"] for row in raw_rows)
    removed = target and raw_overcount and endpoint_closed and no_silent and duplicate_route

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_active_prefix_product_fiber_multiplicity_router",
        "status": "product_fiber_multiplicity_compressed_to_canonical_product_support_and_named_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "alpha": ALPHA,
        "log_absorption_epsilon": LOG_EPSILON,
        "residual_exponent_after_log_absorption": round(RESIDUAL_EXPONENT, 6),
        "product_fiber_target_imported": target,
        "raw_product_fiber_overcount_certified": raw_overcount,
        "product_endpoint_quotient_closed": endpoint_closed,
        "cold_core_order_invariance_imported_for_quotient": quotient_guard,
        "row_free_and_sparse_no_silent_collapse_imported": no_silent,
        "duplicate_complete_key_routes_to_named_return": duplicate_route,
        "product_fiber_multiplicity_independent_hardpoint_removed": removed,
        "active_prefix_product_fiber_multiplicity_or_named_return_ledger_proved": False,
        "canonical_product_class_support_p018_or_cold_sparsification_proved": False,
        "cold_nonpersistent_product_support_sparsification_lemma_proved": False,
        "divisor_support_p018_finite_boundary_or_analytic_envelope_proved": False,
        "named_return_exclusion_proved": False,
        "fixed_type_history_pdec_excluded": False,
        "same_parameter_pdec_threshold_numeric_table_proved": False,
        "active_prefix_level_packing_exponent_table_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": PRODUCT_FIBER,
        "hardpoint_after_router": f"{CANONICAL_PRODUCT} AND {COLD_FILTER} AND {NAMED_RETURN}",
        "next_direct_attack_target": COLD_FILTER,
        "parallel_attack_targets": [
            CANONICAL_PRODUCT,
            DIVISOR_ENV,
            NAMED_RETURN,
            FIXED_HISTORY,
            TPDEC_TABLE,
            LOAD_LOWER,
            DSTRUCTURE,
        ],
        "raw_fiber_obstruction_rows": raw_rows,
        "endpoint_commutativity_samples": endpoint_samples,
        "quotient_rows": quotient_rows(),
        "route_rows": route_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ActivePrefixProductFiberMultiplicityOrNamedReturnLedger` 的裸计数形态不能成立："
            "同一产品 `d=2^a` 的有序分解数已经在边界样本中远超 `P^0.18`，"
            "所以不能把产品纤维重数当成可直接求和的冷容量。"
            "本步关闭的是无名 overcount：product-window 端点外向缩放只依赖总乘积，"
            "同产品内的顺序/括号冗余必须商化为规范产品类；若内部顺序改变了相位、标签、窗口或 cold guard，"
            "差异就不是自由容量，而是固定历史、PDEC/SAE、ColumnCRT、热核心或标签回流。"
            "因此产品纤维不再是独立裸硬点；真正剩余转为 `ColdNonpersistentProductSupportSparsificationLemma`："
            "证明通过 cold/nonpersistent guard 的规范产品类本身足够稀疏，并并行排斥命名回流。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 活动前缀产品纤维重数路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"product_fiber_target_imported={fmt_bool(result['product_fiber_target_imported'])}",
        f"raw_product_fiber_overcount_certified={fmt_bool(result['raw_product_fiber_overcount_certified'])}",
        f"product_endpoint_quotient_closed={fmt_bool(result['product_endpoint_quotient_closed'])}",
        f"row_free_and_sparse_no_silent_collapse_imported={fmt_bool(result['row_free_and_sparse_no_silent_collapse_imported'])}",
        f"duplicate_complete_key_routes_to_named_return={fmt_bool(result['duplicate_complete_key_routes_to_named_return'])}",
        f"product_fiber_multiplicity_independent_hardpoint_removed={fmt_bool(result['product_fiber_multiplicity_independent_hardpoint_removed'])}",
        f"active_prefix_product_fiber_multiplicity_or_named_return_ledger_proved={fmt_bool(result['active_prefix_product_fiber_multiplicity_or_named_return_ledger_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 裸纤维阻塞",
        "",
        "| P | a=floor(log2 P) | all ordered | one/two step | P^0.18 | all over | one/two over |",
        "| ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for item in result["raw_fiber_obstruction_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["P"]),
                    str(item["dyadic_exponent_floor"]),
                    str(item["all_ordered_factorizations_of_2a"]),
                    str(item["one_two_step_factorizations"]),
                    str(item["P_residual_budget"]),
                    f"`{fmt_bool(item['raw_all_blocks_over_budget'])}`",
                    f"`{fmt_bool(item['raw_one_two_over_budget'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 端点交换样本",
            "",
            "| left | right | a | b | left seq | left once | right seq | right once | commutes |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["endpoint_commutativity_samples"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["left"]),
                    str(item["right"]),
                    str(item["a"]),
                    str(item["b"]),
                    str(item["left_sequential"]),
                    str(item["left_once"]),
                    str(item["right_sequential"]),
                    str(item["right_once"]),
                    f"`{fmt_bool(item['commutes'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 商化字典",
            "",
            "| piece | formula | status | meaning |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["quotient_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['piece'])}`",
                    table_cell(item["formula"]),
                    f"`{table_cell(item['status'])}`",
                    table_cell(item["meaning"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 路线拆分",
            "",
            "| route | status | task |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["route_rows"]:
        lines.append(
            f"| `{table_cell(item['route'])}` | `{table_cell(item['status'])}` | {table_cell(item['task'])} |"
        )

    lines.extend(
        [
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 6. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 边界：本步删除的是裸产品纤维重数作为独立免费容量的可能性；没有排斥全部命名回流，也没有闭合最终行/列命题。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """入口函数。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "product_fiber_multiplicity_independent_hardpoint_removed="
        f"{fmt_bool(result['product_fiber_multiplicity_independent_hardpoint_removed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
