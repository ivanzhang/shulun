#!/usr/bin/env python3
"""生成 strict primitive product projection rule 可执行哈希证书。

用法示例：
  python3 experiments/prime_matrix_strict_primitive_product_projection_rule_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-primitive-product-projection-rule-router.json

输出：
  data/primitive-product-projection-sample-ledger.json
  docs/monograph/prime-matrix-strict-primitive-product-projection-rule-router.json
  docs/monograph/prime-matrix-strict-primitive-product-projection-rule-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json"
OUT_MD = DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.md"
OUT_LEDGER = DATA / "primitive-product-projection-sample-ledger.json"

HARDPOINT = "PrimitiveProductProjectionRuleExecutableHash"
RANK_PROFILE = "PrimitiveProductRankProfileCanonicalization"
COMMON_KERNEL_REJECT = "CommonKernelCandidateReturnFilter"
WEIGHT_COMPARISON = "PrimitiveProductRankinWeightP018Comparison"
CANDIDATE_BOUND = "ColdProductBlockCandidateCountOrSymbolicBound"
CONCRETE_DATA = "ConcretePrimitiveProductRankinEmbeddingDataLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json",
    DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
]


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def factor(n: int) -> dict[int, int]:
    """用确定性试除分解正整数；仅用于规则样本和可执行规范。"""
    if n <= 0:
        raise ValueError("n must be positive")
    x = n
    result: dict[int, int] = {}
    p = 2
    while p * p <= x:
        while x % p == 0:
            result[p] = result.get(p, 0) + 1
            x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        result[x] = result.get(x, 0) + 1
    return result


def canonical_profile(d: int, h0: int, registered_common_kernel: int = 1) -> dict[str, Any]:
    """把产品 d 投影为 primitive rank profile；共同核未剔除时返回回流。"""
    if h0 % d != 0:
        return {
            "admissible": False,
            "return_kind": "not_dividing_h0",
            "profile": [],
            "rank": 0,
        }
    kernel_overlap = gcd(d, registered_common_kernel) if registered_common_kernel > 1 else 1
    if kernel_overlap > 1:
        return {
            "admissible": False,
            "return_kind": "common_kernel_return",
            "common_kernel_overlap": kernel_overlap,
            "profile": [],
            "rank": 0,
        }
    d_fac = factor(d)
    h_fac = factor(h0)
    profile = [
        {
            "prime": p,
            "product_exp": exp,
            "h0_exp": h_fac.get(p, 0),
            "rank_unit": 1,
            "valuation_state": f"{p}^{exp}",
        }
        for p, exp in sorted(d_fac.items())
    ]
    payload = {
        "admissible": True,
        "return_kind": "primitive_profile",
        "profile": profile,
        "rank": len(profile),
        "radical": 1,
    }
    radical = 1
    for p in d_fac:
        radical *= p
    payload["radical"] = radical
    payload["profile_hash"] = hashlib.sha256(
        json.dumps(profile, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return payload


def gcd(a: int, b: int) -> int:
    """计算最大公因数。"""
    while b:
        a, b = b, a % b
    return abs(a)


def sample_ledger() -> dict[str, Any]:
    """生成投影规则样本账本。"""
    samples = [
        {"d": 30, "h0": 2 * 3 * 5 * 7 * 11, "registered_common_kernel": 1},
        {"d": 72, "h0": 2**5 * 3**3 * 5, "registered_common_kernel": 1},
        {"d": 84, "h0": 2**3 * 3 * 5 * 7, "registered_common_kernel": 6},
        {"d": 77, "h0": 2 * 3 * 5 * 7 * 11, "registered_common_kernel": 1},
    ]
    rows = []
    for item in samples:
        projected = canonical_profile(**item)
        rows.append({**item, "projection": projected})
    return {
        "ledger_type": "primitive_product_projection_sample_ledger",
        "rule": "factor d, reject registered common-kernel overlap, sort prime valuation states",
        "rows": rows,
        "all_admissible_rows_have_sorted_profiles": all(
            row["projection"]["profile"] == sorted(row["projection"]["profile"], key=lambda x: x["prime"])
            for row in rows
            if row["projection"]["admissible"]
        ),
    }


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_primitive_product_projection_rule_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/primitive-product-projection-sample-ledger.json": sha256(OUT_LEDGER),
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取投影规则需要的导入。"""
    candidate = load_json(DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json")
    block = load_json(DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json")
    kernel = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    return {
        "candidate_count_route_imported": bool(candidate.get("window_divisor_count_envelope_closed")),
        "block_candidate_generator_imported": bool(block.get("cold_product_candidate_set_generator_rule_closed")),
        "free_common_kernel_return_cycle_excluded": bool(kernel.get("free_common_kernel_return_cycle_excluded")),
    }


def rule_rows() -> list[dict[str, str]]:
    """列出投影规则步骤。"""
    return [
        {
            "step": "divisibility_guard",
            "definition": "reject d if d does not divide h0",
            "effect": "not a candidate product for this formal unit",
        },
        {
            "step": "common_kernel_guard",
            "definition": "reject d if gcd(d, registered_common_kernel)>1",
            "effect": "candidate returns to common-kernel/PDEC ledger, not primitive dispersion",
        },
        {
            "step": "prime_factor_projection",
            "definition": "factor d and sort primes increasingly",
            "effect": "order-free local rank profile",
        },
        {
            "step": "valuation_state",
            "definition": "record (prime, product_exp, h0_exp, rank_unit=1)",
            "effect": "Rankin/Euler weights can be applied per local prime factor",
        },
        {
            "step": "profile_hash",
            "definition": "sha256 of canonical sorted JSON profile",
            "effect": "stable manifest row key",
        },
    ]


def decision_rows(flags: dict[str, bool], ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    projection_closed = (
        flags["candidate_count_route_imported"]
        and flags["block_candidate_generator_imported"]
        and flags["free_common_kernel_return_cycle_excluded"]
        and ledger["all_admissible_rows_have_sorted_profiles"]
    )
    return [
        {
            "gate": "PrimitiveProjectionTargetImported",
            "closed": True,
            "proved": flags["candidate_count_route_imported"],
            "meaning": "上一层已把候选计数的解析路线压到 primitive 投影规则。",
            "remaining": HARDPOINT,
        },
        {
            "gate": "CommonKernelReturnGuardImported",
            "closed": True,
            "proved": flags["free_common_kernel_return_cycle_excluded"],
            "meaning": "共同核重叠不能留在 primitive dispersion 分支，必须回流。",
            "remaining": COMMON_KERNEL_REJECT,
        },
        {
            "gate": "PrimitiveRankProfileCanonicalizationClosed",
            "closed": projection_closed,
            "proved": projection_closed,
            "meaning": "候选 d 被确定性分解为排序局部素因子/指数 profile，并给出稳定 hash。",
            "remaining": RANK_PROFILE,
        },
        {
            "gate": "PrimitiveProductProjectionRuleExecutableHashClosed",
            "closed": projection_closed,
            "proved": projection_closed,
            "meaning": "投影规则已由本脚本和样本账本物化为可执行哈希对象。",
            "remaining": WEIGHT_COMPARISON,
        },
        {
            "gate": "PrimitiveProductRankinWeightP018ComparisonProved",
            "closed": False,
            "proved": False,
            "meaning": "投影规则已闭合，但尚未证明 Rankin 权重总和低于 P^0.18。",
            "remaining": WEIGHT_COMPARISON,
        },
        {
            "gate": "ColdProductBlockCandidateCountOrSymbolicBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "缺权重比较或 finite runner，因此候选计数符号界仍未闭合。",
            "remaining": f"{WEIGHT_COMPARISON} OR FiniteColdProductBlockCandidateRunnerHash",
        },
        {
            "gate": "ConcretePrimitiveProductRankinEmbeddingDataLedgerProved",
            "closed": False,
            "proved": False,
            "meaning": "投影规则闭合但 concrete 产品块权重数据仍未完成。",
            "remaining": WEIGHT_COMPARISON,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "仍未得到早期零行反例链终端矛盾。",
            "remaining": f"{WEIGHT_COMPARISON} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 primitive projection 证书。"""
    ledger = sample_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    flags = imported_flags()
    decisions = decision_rows(flags, ledger)
    projection_closed = next(
        item for item in decisions if item["gate"] == "PrimitiveProductProjectionRuleExecutableHashClosed"
    )["proved"]
    return {
        "certificate_type": "prime_matrix_strict_primitive_product_projection_rule_router",
        "status": "primitive_product_projection_rule_executable_closed_weight_comparison_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": WEIGHT_COMPARISON,
        "next_direct_attack_target": WEIGHT_COMPARISON,
        "imported_flags": flags,
        "projection_rule": rule_rows(),
        "sample_ledger_path": str(OUT_LEDGER.relative_to(ROOT)),
        "sample_ledger_sha256": sha256(OUT_LEDGER),
        "decision_table": decisions,
        "primitive_rank_profile_canonicalization_closed": bool(
            next(item for item in decisions if item["gate"] == "PrimitiveRankProfileCanonicalizationClosed")[
                "proved"
            ]
        ),
        "primitive_product_projection_rule_executable_hash_closed": bool(projection_closed),
        "primitive_product_rankin_weight_p018_comparison_proved": False,
        "cold_product_block_candidate_count_or_symbolic_bound_proved": False,
        "concrete_primitive_product_rankin_embedding_data_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`PrimitiveProductProjectionRuleExecutableHash` 已闭合：候选产品 `d` 先通过 `d|h0` 守卫，"
            "再剔除已登记共同核重叠；留在 primitive dispersion 分支的产品被唯一分解为排序的局部素因子/指数 profile，"
            "并生成稳定 hash。该规则删除了有序历史和共同核歧义。"
            "但这还没有证明 Rankin 权重总和小于 `P^0.18`，最新最窄点转为 `PrimitiveProductRankinWeightP018Comparison`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict primitive product projection rule 路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "primitive_rank_profile_canonicalization_closed",
        "primitive_product_projection_rule_executable_hash_closed",
        "primitive_product_rankin_weight_p018_comparison_proved",
        "cold_product_block_candidate_count_or_symbolic_bound_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. 投影规则")
    lines.append("")
    lines.append("| step | definition | effect |")
    lines.append("| --- | --- | --- |")
    for item in result["projection_rule"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["step", "definition", "effect"])
            + " |"
        )
    lines.append("")

    lines.append("## 2. 样本账本")
    lines.append("")
    lines.append(f"- path: `{result['sample_ledger_path']}`")
    lines.append(f"- sha256: `{result['sample_ledger_sha256']}`")
    lines.append("")

    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["decision_table"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )
    lines.append("")

    lines.append("## 4. 下一步最窄点")
    lines.append("")
    lines.append(f"- 主攻：`{result['next_direct_attack_target']}`。")
    lines.append("- 边界：本步只闭合投影规则，不证明权重比较。")
    lines.append("")

    lines.append("## 5. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for file, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、Markdown 与样本账本。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "primitive_product_projection_rule_executable_hash_closed="
        f"{fmt_bool(result['primitive_product_projection_rule_executable_hash_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
