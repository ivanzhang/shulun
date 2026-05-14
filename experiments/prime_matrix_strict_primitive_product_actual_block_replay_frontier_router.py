#!/usr/bin/env python3
"""同步 primitive product Rankin 到 actual block replay 的最新前沿。

用法示例：
  python3 experiments/prime_matrix_strict_primitive_product_actual_block_replay_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-primitive-product-actual-block-replay-frontier-router.json

输出：
  docs/monograph/prime-matrix-strict-primitive-product-actual-block-replay-frontier-router.json
  docs/monograph/prime-matrix-strict-primitive-product-actual-block-replay-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-primitive-product-actual-block-replay-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-primitive-product-actual-block-replay-frontier-router.md"

ACTUAL_SCAN = DATA / "actual-cold-product-block-parameter-scan.json"
SOURCE_FILES = [
    ACTUAL_SCAN,
    DATA / "primitive-product-projection-sample-ledger.json",
    DATA / "primitive-product-rankin-p018-sample-table.json",
    DATA / "primitive-product-rankin-weight-sample-ledger.json",
    DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json",
    DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json",
    DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json",
    DOCS / "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json",
    DOCS / "prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.json",
    DOCS / "prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json",
    DOCS / "prime-matrix-strict-terminal-hot-core-return-frontier-router.json",
]

REPLAY = "ActualColdProductBlockReplayLedgerOrHotReturnPacketTable"
RUNNER = "FiniteColdProductBlockCandidateRunnerHash"
STRICT_MARGIN = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_strict_primitive_product_actual_block_replay_frontier_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def scan_rows(scan: dict[str, Any]) -> list[dict[str, Any]]:
    """提取 actual 参数扫描结果。"""
    fields = scan.get("required_fields", [])
    hits = scan.get("hits", [])
    return [
        {
            "scan_type": scan.get("scan_type", "missing"),
            "actual_parameter_ledger_found": scan.get("actual_parameter_ledger_found") is True,
            "hit_count": len(hits),
            "required_fields": ", ".join(fields),
        }
    ]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和未闭合的接口。"""
    return [
        {
            "name": "block_inventory_schema",
            "status": "closed",
            "statement": "block_id, source tuple, cold key, dyadic interval, candidate rule, and return filter are defined.",
        },
        {
            "name": "primitive_projection_rule",
            "status": "closed",
            "statement": "candidate d is projected to an order-free primitive rank profile after common-kernel filtering.",
        },
        {
            "name": "rankin_weight_formula",
            "status": "closed_formula_only",
            "statement": "two-sided dyadic Rankin/Euler weight bounds are available but need actual P,h0,Y rows.",
        },
        {
            "name": "exact_count_hot_return_dichotomy",
            "status": "closed_logic_only",
            "statement": "if exact block count exceeds P^0.18, the block is a hot-return packet; otherwise it is exact_count_pass.",
        },
        {
            "name": "actual_block_replay_ledger",
            "status": "open",
            "statement": "no actual source_tuple/P/h0/Y/common-kernel replay ledger is present in the current corpus.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ColdProductBlockInventorySchemaClosed",
            "closed": result["cold_product_block_inventory_schema_closed"],
            "proved": result["cold_product_block_inventory_schema_closed"],
            "meaning": "产品块字段和候选集合生成规则已经定义。",
            "remaining": REPLAY,
        },
        {
            "gate": "PrimitiveProjectionExecutableClosed",
            "closed": result["primitive_product_projection_rule_executable_hash_closed"],
            "proved": result["primitive_product_projection_rule_executable_hash_closed"],
            "meaning": "候选 d 到 primitive rank profile 的投影规则已经闭合。",
            "remaining": "PrimitiveProductRankinWeightP018Comparison",
        },
        {
            "gate": "RankinFormulaAndExactFallbackSynced",
            "closed": result["rankin_formula_and_exact_fallback_synced"],
            "proved": result["rankin_formula_and_exact_fallback_synced"],
            "meaning": "Rankin 上界失败不再等同支撑失败；可用 exact-count fallback 或 hot-return 二分处理。",
            "remaining": REPLAY,
        },
        {
            "gate": "ActualBlockParameterLedgerPresent",
            "closed": result["actual_cold_product_block_parameter_ledger_present"],
            "proved": result["actual_cold_product_block_parameter_ledger_present"],
            "meaning": "当前语料没有 actual source_tuple/P/h0/Y/common-kernel 参数行，不能把样本升级为全体证明。",
            "remaining": REPLAY,
        },
        {
            "gate": "PrimitiveProductSupportRankinLedgerProved",
            "closed": False,
            "proved": False,
            "meaning": "公式、投影和二分已同步，但缺 actual replay 表，因此原始产品支撑 Rankin 门仍未闭合。",
            "remaining": f"{REPLAY} AND {RUNNER}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "actual replay、非持久预算反超、持久 moving atom 和 DStructure/Rankin 仍未全部闭合。",
            "remaining": f"{REPLAY} AND {STRICT_MARGIN} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造前沿同步证书。"""
    scan = load_json(ACTUAL_SCAN)
    inventory = load_json(DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json")
    candidate = load_json(DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json")
    projection = load_json(DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json")
    weight = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json")
    fallback = load_json(DOCS / "prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.json")
    exact_hot = load_json(DOCS / "prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json")
    hot_frontier = load_json(DOCS / "prime-matrix-strict-terminal-hot-core-return-frontier-router.json")

    inventory_schema = (
        inventory.get("cold_product_dyadic_block_inventory_schema_closed") is True
        or inventory.get("cold_product_candidate_set_generator_rule_closed") is True
    )
    candidate_identity = candidate.get("window_divisor_count_envelope_closed") is True
    projection_closed = projection.get("primitive_product_projection_rule_executable_hash_closed") is True
    rankin_formula = weight.get("primitive_product_local_rankin_weight_formula_closed") is True
    fallback_closed = (
        fallback.get("rankin_failure_not_equivalent_to_support_failure_closed") is True
        and fallback.get("exact_count_fallback_schema_closed") is True
    )
    exact_hot_closed = (
        exact_hot.get("exact_count_pass_or_hot_return_dichotomy_closed") is True
        and exact_hot.get("clean_exact_overbudget_without_named_return_excluded") is True
        and hot_frontier.get("terminal_core_hot_divisor_window_independent_hardpoint_removed") is True
    )
    actual_present = scan.get("actual_parameter_ledger_found") is True and bool(scan.get("hits"))

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_primitive_product_actual_block_replay_frontier_router",
        "status": "primitive_product_rankin_synced_to_actual_block_replay_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "cold_product_block_inventory_schema_closed": inventory_schema,
        "cold_product_candidate_count_identity_closed": candidate_identity,
        "primitive_product_projection_rule_executable_hash_closed": projection_closed,
        "rankin_weight_formula_closed": rankin_formula,
        "exact_count_fallback_and_hot_return_dichotomy_closed": fallback_closed and exact_hot_closed,
        "rankin_formula_and_exact_fallback_synced": rankin_formula and fallback_closed and exact_hot_closed,
        "actual_cold_product_block_parameter_ledger_present": actual_present,
        "actual_cold_product_block_replay_ledger_proved": False,
        "primitive_product_support_rankin_ledger_proved": False,
        "cold_product_support_sparsification_beyond_tau_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "PrimitiveProductSupportRankinLedger",
        "hardpoint_after_router": REPLAY,
        "next_direct_attack_target": REPLAY,
        "parallel_attack_targets": [STRICT_MARGIN, MOVING_ATOM, DSTRUCTURE],
        "actual_scan_rows": scan_rows(scan),
        "theorem_rows": theorem_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PrimitiveProductSupportRankinLedger` 的当前缺口已经不是投影规则或 Rankin 公式："
            "primitive 投影规则已可执行，Rankin 权重公式已闭合，Rankin 失败也已通过 exact-count "
            "fallback 与 hot-return 二分同步。真正未闭合的是 actual 产品块 replay：当前语料没有"
            "`source_tuple_hash/P/h0/Y/registered_common_kernel` 参数行，不能把诊断样本升级为全体证明。"
            "因此下一最窄点是 `ActualColdProductBlockReplayLedgerOrHotReturnPacketTable`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict primitive product actual block replay 前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cold_product_block_inventory_schema_closed={fmt_bool(result['cold_product_block_inventory_schema_closed'])}",
        f"primitive_product_projection_rule_executable_hash_closed={fmt_bool(result['primitive_product_projection_rule_executable_hash_closed'])}",
        f"rankin_formula_and_exact_fallback_synced={fmt_bool(result['rankin_formula_and_exact_fallback_synced'])}",
        f"actual_cold_product_block_parameter_ledger_present={fmt_bool(result['actual_cold_product_block_parameter_ledger_present'])}",
        f"primitive_product_support_rankin_ledger_proved={fmt_bool(result['primitive_product_support_rankin_ledger_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. actual 参数扫描",
        "",
        "| scan | found | hit count | required fields |",
        "| --- | --- | ---: | --- |",
    ]
    for item in result["actual_scan_rows"]:
        lines.append(
            "| `{scan}` | `{found}` | `{count}` | {fields} |".format(
                scan=table_cell(item["scan_type"]),
                found=fmt_bool(item["actual_parameter_ledger_found"]),
                count=item["hit_count"],
                fields=table_cell(item["required_fields"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 接口状态",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["theorem_rows"]:
        lines.append(
            "| `{name}` | `{status}` | {statement} |".format(
                name=table_cell(item["name"]),
                status=table_cell(item["status"]),
                statement=table_cell(item["statement"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体任务：对每个 actual source tuple 生成 dyadic 产品块清单、候选 d 集合、exact count 或 Rankin bound；若 exact count 超过 `P^0.18`，同步生成 hot-return packet，而不是留下 clean residual。",
            "",
            "## 5. 依赖哈希",
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
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"next={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
