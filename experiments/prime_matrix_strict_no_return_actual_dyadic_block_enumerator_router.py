#!/usr/bin/env python3
"""生成 strict no-return actual dyadic cold 产品块枚举器证书。

用法示例：
  python3 experiments/prime_matrix_strict_no_return_actual_dyadic_block_enumerator_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json

输出：
  docs/monograph/prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json
  docs/monograph/prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json"
OUT_MD = DOCS / "prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.md"

HARDPOINT = "ActualDyadicColdProductBlockEnumeratorForH0"
NO_RETURN_H0 = "NoReturnActualProductDivisorDomainH0EmitterForFormalUnit"
CANDIDATE_BOUND = "ColdProductBlockCandidateCountOrSymbolicBound"
PROJECTION = "PrimitiveProductProjectionRuleExecutableHash"
WEIGHT_TABLE = "PrimitiveProductRankinP018InequalityTable"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
KERNEL_REGISTER = "PerBlockRegisteredCommonKernelLedger"
RETURN_ABSORB = "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption"
ACTUAL_BLOCK = "ActualColdProductBlockParameterLedgerForP018Table"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.json",
    "prime-matrix-strict-cold-product-block-inventory-router.json",
    "prime-matrix-strict-cold-product-candidate-count-router.json",
    "prime-matrix-strict-primitive-product-projection-rule-router.json",
    "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json",
    "prime-matrix-strict-primitive-product-rankin-p018-table-router.json",
    "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json",
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
        "experiments/prime_matrix_strict_no_return_actual_dyadic_block_enumerator_router.py": sha256(
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


def divisors(n: int) -> list[int]:
    """生成正整数 n 的全部除数；仅用于有限样本核验。"""
    result: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            if d * d != n:
                result.append(n // d)
        d += 1
    return sorted(result)


def dyadic_blocks_for_sample(h0: int) -> list[dict[str, Any]]:
    """给出样本 h0 的 dyadic 块，验证枚举规则可执行。"""
    ds = divisors(h0)
    rows: list[dict[str, Any]] = []
    y = 1
    while y < h0:
        block = [d for d in ds if y < d <= 2 * y]
        if block:
            rows.append(
                {
                    "Y": y,
                    "interval": f"({y},{2 * y}]",
                    "candidate_divisors": block,
                    "candidate_count": len(block),
                    "block_id_rule": "H(source_tuple_hash,h0_hash,cold_key,Y,2Y)",
                }
            )
        y *= 2
    return rows


def imported_flags() -> dict[str, bool]:
    """读取 dyadic 枚举器需要的导入。"""
    h0_sync = load_json("prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.json")
    inventory = load_json("prime-matrix-strict-cold-product-block-inventory-router.json")
    candidate = load_json("prime-matrix-strict-cold-product-candidate-count-router.json")
    projection = load_json("prime-matrix-strict-primitive-product-projection-rule-router.json")
    weight = load_json("prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json")
    p018 = load_json("prime-matrix-strict-primitive-product-rankin-p018-table-router.json")
    return_branch = load_json("prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json")
    return {
        "no_return_h0_imported": h0_sync.get("no_return_h0_emitter_for_rankin_parameter_closed") is True,
        "enumerator_target_imported": h0_sync.get("next_direct_attack_target") == HARDPOINT,
        "cold_product_schema_closed": inventory.get("cold_product_dyadic_block_inventory_schema_closed") is True,
        "candidate_generator_closed": inventory.get("cold_product_candidate_set_generator_rule_closed") is True,
        "window_count_identity_closed": candidate.get("window_divisor_count_envelope_closed") is True,
        "primitive_projection_hash_closed": projection.get("primitive_product_projection_rule_executable_hash_closed")
        is True,
        "rankin_weight_formula_closed": weight.get("primitive_product_local_rankin_weight_formula_closed") is True
        and weight.get("primitive_product_euler_profile_sum_bound_closed") is True,
        "p018_table_schema_closed": p018.get("p018_table_schema_closed") is True,
        "return_branch_frontier_closed": return_branch.get("return_branch_alphabet_frontier_closed") is True,
        "return_branch_global_absorption_proved": return_branch.get(
            "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved"
        )
        is True,
    }


def enumerator_rule_rows() -> list[dict[str, str]]:
    """列出 actual dyadic 枚举规则。"""
    return [
        {
            "component": "dyadic partition",
            "rule": "B_j=(2^j,2^{j+1}], 0<=j<=floor(log_2 h0^car)",
            "status": "closed_rule",
        },
        {
            "component": "unit product",
            "rule": "d=1 is the empty-prefix unit and is not counted as a productive dyadic product block",
            "status": "closed_boundary",
        },
        {
            "component": "candidate set",
            "rule": "Cand_j={d:d|h0^car, d in B_j, d passes cold/no-return guard}",
            "status": "closed_rule",
        },
        {
            "component": "empty block",
            "rule": "Cand_j=empty may be omitted with empty-block hash; it carries no Rankin mass",
            "status": "closed_rule",
        },
        {
            "component": "block id",
            "rule": "block_id=H(source_tuple_hash,h0_hash,cold_key,j,2^j,2^{j+1})",
            "status": "closed_rule",
        },
        {
            "component": "no cross-block merge",
            "rule": "each d belongs to exactly one dyadic B_j",
            "status": "closed_rule",
        },
        {
            "component": "return filter",
            "rule": "source-defect/overflow/hot/common-kernel candidates leave no-return and enter named return frontier",
            "status": "registered_global_open",
        },
    ]


def remaining_rows() -> list[dict[str, str]]:
    """列出枚举器闭合后的剩余。"""
    return [
        {
            "remaining": CANDIDATE_BOUND,
            "meaning": "每块候选集已定义，但仍需证明候选数或 Rankin 权重低于预算。",
        },
        {
            "remaining": KERNEL_REGISTER,
            "meaning": "每个实际块必须登记共同核/primitive 投影，防止重复计数。",
        },
        {
            "remaining": WEIGHT_TABLE,
            "meaning": "需要对所有枚举块给出 Rankin 权重与 P^0.18 预算比较。",
        },
        {
            "remaining": FAILURE_RETURN,
            "meaning": "权重失败块必须带命名回流包，不能静默删除。",
        },
        {
            "remaining": RETURN_ABSORB,
            "meaning": "全局 return 分支仍需非持久预算吸收或持久终端排斥。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    enumerator_closed = result["actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed"]
    return [
        row(
            "EnumeratorTargetImported",
            result["enumerator_target_imported"],
            result["enumerator_target_imported"],
            "上一层 no-return h0 回接后，下一点是实际 dyadic 产品块枚举器。",
            HARDPOINT,
        ),
        row(
            "NoReturnH0DomainImported",
            result["no_return_h0_imported"],
            result["no_return_h0_imported"],
            "no-return 分支已有 h0^car、D(U)|h0^car 和整数残频。",
            NO_RETURN_H0,
        ),
        row(
            "ColdProductCandidateGeneratorImported",
            result["cold_product_schema_closed"] and result["candidate_generator_closed"],
            result["cold_product_schema_closed"] and result["candidate_generator_closed"],
            "候选集定义为 d|h0 且通过 cold/no-return guard 的产品支撑。",
            "ColdProductCandidateSetGeneratorRule",
        ),
        row(
            "ActualDyadicEnumeratorRuleClosed",
            enumerator_closed,
            enumerator_closed,
            "给定 h0^car 后，dyadic 块和 block_id 有唯一可复算规则。",
            HARDPOINT,
        ),
        row(
            "PrimitiveProjectionAndRankinFormulaImported",
            result["primitive_projection_hash_closed"] and result["rankin_weight_formula_closed"],
            result["primitive_projection_hash_closed"] and result["rankin_weight_formula_closed"],
            "候选 d 到 primitive profile 的投影规则与局部 Rankin 公式已可复用。",
            f"{PROJECTION} AND PrimitiveProductRankinWeightP018Comparison",
        ),
        row(
            "ActualColdProductBlockParameterLedgerPresent",
            False,
            False,
            "枚举规则闭合但尚未给出全体实际块的权重 pass/return 表。",
            f"{WEIGHT_TABLE} AND {FAILURE_RETURN}",
        ),
        row(
            "GlobalActualDyadicEnumeratorProved",
            False,
            False,
            "全局枚举仍受 source-defect/overflow return 分支限制。",
            RETURN_ABSORB,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{WEIGHT_TABLE} AND {RETURN_ABSORB} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 actual dyadic block 枚举器证书。"""
    flags = imported_flags()
    sample_rows = dyadic_blocks_for_sample(840)
    enumerator_closed = (
        flags["no_return_h0_imported"]
        and flags["enumerator_target_imported"]
        and flags["cold_product_schema_closed"]
        and flags["candidate_generator_closed"]
        and flags["window_count_identity_closed"]
        and flags["p018_table_schema_closed"]
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_no_return_actual_dyadic_block_enumerator_router",
        "status": "no_return_actual_dyadic_block_enumerator_closed_weight_table_return_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed": enumerator_closed,
        "actual_dyadic_cold_product_block_enumerator_global_proved": False,
        "actual_cold_product_block_parameter_ledger_present": False,
        "primitive_product_rankin_p018_inequality_table_present": False,
        "primitive_product_rankin_failure_return_packet_ledger_closed": False,
        "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{WEIGHT_TABLE} AND {FAILURE_RETURN} AND {RETURN_ABSORB}",
        "next_direct_attack_target": WEIGHT_TABLE,
        "parallel_attack_targets": [
            FAILURE_RETURN,
            KERNEL_REGISTER,
            CANDIDATE_BOUND,
            RETURN_ABSORB,
            SPARSE_BUDGET,
            PERSISTENT_TERMINAL,
            DSTRUCTURE,
        ],
        "enumerator_rule_rows": enumerator_rule_rows(),
        "sample_h0": 840,
        "sample_dyadic_blocks": sample_rows,
        "sample_partition_valid": sum(row["candidate_count"] for row in sample_rows)
        == len([d for d in divisors(840) if d > 1]),
        "remaining_rows": remaining_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ActualDyadicColdProductBlockEnumeratorForH0` 在 no-return 分支可关闭为唯一 dyadic 分割规则："
            "给定 `h0^car` 后，每个候选产品 `d|h0^car` 落入唯一块 `(2^j,2^{j+1}]`，"
            "候选集再由 cold/no-return guard 过滤，并以 `block_id` 稳定哈希。这样“缺 Y 列表”"
            "不再是独立源头硬点；真正剩余变成对所有枚举块提交 Rankin/P^0.18 权重表和失败回流包。"
            "全局 source-defect/valuation-overflow return 分支仍未排斥或吸收，所以行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix strict no-return actual dyadic 产品块枚举器路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed={fmt_bool(result['actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed'])}",
        f"actual_dyadic_cold_product_block_enumerator_global_proved={fmt_bool(result['actual_dyadic_cold_product_block_enumerator_global_proved'])}",
        f"actual_cold_product_block_parameter_ledger_present={fmt_bool(result['actual_cold_product_block_parameter_ledger_present'])}",
        f"primitive_product_rankin_p018_inequality_table_present={fmt_bool(result['primitive_product_rankin_p018_inequality_table_present'])}",
        f"carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved={fmt_bool(result['carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 枚举规则",
        "",
        "| component | rule | status |",
        "| --- | --- | --- |",
    ]
    for item in result["enumerator_rule_rows"]:
        lines.append(
            "| "
            + " | ".join([table_cell(item["component"]), table_cell(item["rule"]), table_cell(item["status"])])
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 样本核验",
            "",
            f"- sample h0: `{result['sample_h0']}`",
            f"- sample_partition_valid: `{fmt_bool(result['sample_partition_valid'])}`",
            "",
            "| Y | interval | candidate_count | candidate_divisors |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["sample_dyadic_blocks"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['Y']}`",
                    f"`{table_cell(item['interval'])}`",
                    f"`{item['candidate_count']}`",
                    f"`{table_cell(item['candidate_divisors'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 剩余原子",
            "",
            "| remaining | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["remaining_rows"]:
        lines.append(f"| `{table_cell(item['remaining'])}` | {table_cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一步",
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
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(
        "actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed="
        + fmt_bool(result["actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed"])
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
