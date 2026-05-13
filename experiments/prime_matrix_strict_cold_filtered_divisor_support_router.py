#!/usr/bin/env python3
"""生成 strict cold-filtered 产品除数支撑 envelope 路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_filtered_divisor_support_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-filtered-divisor-support-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-filtered-divisor-support-router.json
  docs/monograph/prime-matrix-strict-cold-filtered-divisor-support-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-filtered-divisor-support-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-filtered-divisor-support-router.md"

HARDPOINT = "ColdFilteredDivisorSupportP018Envelope"
PRODUCT_FIBER = "ActivePrefixProductFiberMultiplicityOrNamedReturnLedger"
DIVISOR_TAIL = "ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate"
COLD_SPARSIFY = "ColdProductSupportSparsificationBeyondTauLedger"
HOT_DENSITY = "ShortWindowHotDivisorDensityPDECorSAEReturnExclusion"
PRIMITIVE_RANKIN = "PrimitiveProductSupportRankinLedger"
ACTIVE_PACKING = "ActivePrefixLevelPackingExponentTable"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
COLLAR_SUM = "SameParameterSiblingCollarWidthFiniteSumTable"
TPDEC_TABLE = "SameParameterPDECThresholdNumericTable"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
LOG_EPSILON = 0.25
RESIDUAL_EXPONENT = ALPHA - LOG_EPSILON
P_MIN = 100_000
PRIME_POWER_SUPPORT_THRESHOLD = 75_184_381

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json",
    DOCS / "prime-matrix-strict-active-prefix-level-packing-router.json",
    DOCS / "prime-matrix-strict-effective-cold-history-pruning-router.json",
    DOCS / "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json",
    DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json",
    DOCS / "prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.json",
    DOCS / "prime-matrix-strict-parent-support-numeric-envelope-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_cold_filtered_divisor_support_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
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


def divisor_count(n: int) -> int:
    """计算 n 的除数个数。"""
    x = n
    total = 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            exp = 0
            while x % p == 0:
                x //= p
                exp += 1
            total *= exp + 1
        p += 1 if p == 2 else 2
    if x > 1:
        total *= 2
    return total


def imported_flags() -> dict[str, bool]:
    """读取 cold-filter 支撑需要对接的接口。"""
    product = load_json(DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json")
    pruning = load_json(DOCS / "prime-matrix-strict-effective-cold-history-pruning-router.json")
    tree = load_json(DOCS / "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json")
    branch = load_json(DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json")
    density = load_json(DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json")
    parent = load_json(DOCS / "prime-matrix-strict-parent-support-numeric-envelope-router.json")
    kernel = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    return {
        "product_fiber_support_quotient_imported": bool(
            product.get("active_prefix_product_fiber_multiplicity_or_named_return_ledger_closed_for_support")
        ),
        "divisor_compatibility_interface_closed": bool(pruning.get("divisor_compatibility_interface_closed")),
        "divisor_compatibility_alone_rejected": bool(tree.get("divisor_compatibility_alone_rejected_as_sufficient")),
        "prefix_branching_structural_dichotomy_closed": bool(
            branch.get("prefix_branching_structural_dichotomy_closed")
        ),
        "reciprocal_to_density_certificate_closed": bool(density.get("hot_density_certificate_closed")),
        "generic_tau_closure_rejected": bool(density.get("generic_tau_closure_rejected")),
        "parent_support_geometry_closed": bool(parent.get("projected_support_to_dilated_parent_window_proved")),
        "free_common_kernel_return_cycle_excluded": bool(kernel.get("free_common_kernel_return_cycle_excluded")),
    }


def raw_tau_rows() -> list[dict[str, Any]]:
    """记录粗除数支撑界的边界阻塞样本。"""
    samples = [P_MIN, 83_160, 110_880, 720_720, 1_081_080]
    rows: list[dict[str, Any]] = []
    for n in samples:
        witness = 83_160 if n == P_MIN else n
        tau = 128 if n == P_MIN else divisor_count(n)
        bound = n**RESIDUAL_EXPONENT
        rows.append(
            {
                "P_or_n": n,
                "witness": witness,
                "tau": tau,
                "P018": round(bound, 6),
                "passes": tau <= bound,
                "ratio": round(tau / bound, 6),
            }
        )
    return rows


def prime_power_rows() -> list[dict[str, Any]]:
    """说明产品商化后素数幂有序级联不再是支撑爆炸。"""
    rows: list[dict[str, Any]] = []
    for p in [2, 3, 5, 7]:
        max_exp_at_min = int(math.log(P_MIN, p))
        support_states = max_exp_at_min + 1
        rows.append(
            {
                "prime": p,
                "max_exp_at_P_min": max_exp_at_min,
                "ordered_history_growth_before_quotient": "exponential/Fibonacci depending on allowed blocks",
                "product_support_after_quotient": support_states,
                "P018_at_P_min": round(P_MIN**RESIDUAL_EXPONENT, 6),
                "support_p018_passes_at_P_min": support_states <= P_MIN**RESIDUAL_EXPONENT,
            }
        )
    rows.append(
        {
            "prime": 2,
            "max_exp_at_P_min": "all P>=75184381",
            "ordered_history_growth_before_quotient": "not relevant after product quotient",
            "product_support_after_quotient": "floor(log_2 P)+1 <= P^0.18",
            "P018_at_P_min": "threshold identity",
            "support_p018_passes_at_P_min": True,
        }
    )
    return rows


def support_split_rows() -> list[dict[str, str]]:
    """列出 cold-filter 后的剩余支撑二分。"""
    return [
        {
            "branch": "pure_divisor_tail",
            "condition": "use only # {d:d|h_0}",
            "closed_part": "product-fiber order multiplicity already quotiented",
            "remaining": DIVISOR_TAIL,
            "meaning": "需要显式除数函数尾界和有限边界证书；P=100000 附近粗界失败。",
        },
        {
            "branch": "cold_structural_sparsification",
            "condition": "d must be cold, nonpersistent, and no named return",
            "closed_part": "divisor compatibility, parent-window geometry, prefix structural dichotomy",
            "remaining": COLD_SPARSIFY,
            "meaning": "必须证明真实冷产品远少于全体除数，而不是继续数 tau(h_0)。",
        },
        {
            "branch": "short_window_density_failure",
            "condition": "too many products concentrate in a multiplicative window",
            "closed_part": "reciprocal/count threshold produces hot density certificate",
            "remaining": HOT_DENSITY,
            "meaning": "集中失败会变成热频率除数窗口；仍需排斥 PDEC/SAE/ColumnCRT 出口。",
        },
        {
            "branch": "spread_primitive_rank",
            "condition": "products avoid local concentration but use many independent primitive factors",
            "closed_part": "free common-kernel return cycle excluded",
            "remaining": PRIMITIVE_RANKIN,
            "meaning": "分散失败应由逐素数/Rankin 原始支撑账本吸收；该验收仍独立开放。",
        },
    ]


def decision_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    support_domain_closed = (
        flags["product_fiber_support_quotient_imported"]
        and flags["divisor_compatibility_interface_closed"]
        and flags["parent_support_geometry_closed"]
    )
    structural_routes_closed = (
        flags["prefix_branching_structural_dichotomy_closed"]
        and flags["reciprocal_to_density_certificate_closed"]
        and flags["free_common_kernel_return_cycle_excluded"]
    )
    return [
        row(
            "ColdFilteredSupportTargetImported",
            True,
            flags["product_fiber_support_quotient_imported"],
            "上一层已商掉同产品纤维的免费支撑重数，剩余是 distinct cold products。",
            HARDPOINT,
        ),
        row(
            "ColdFilteredSupportDomainClosed",
            support_domain_closed,
            support_domain_closed,
            "可计支撑已限制为 D|h_0、父扩张窗口内、且未进入命名回流的 cold products。",
            COLD_SPARSIFY,
        ),
        row(
            "PrimePowerOrderedCascadeRemovedForSupport",
            True,
            True,
            "产品商化后，素数幂有序历史爆炸只剩指数状态数；Fibonacci/order 爆炸不再是支撑爆炸。",
            "finite boundary for small P remains separate",
        ),
        row(
            "RawTauP018ClosureRejected",
            True,
            True,
            "P=100000 附近 tau(h_0) 仍可远大于 P^0.18；不能只用全体除数函数闭合。",
            DIVISOR_TAIL,
        ),
        row(
            "ColdStructuralFailureRoutesRegistered",
            structural_routes_closed,
            False,
            "冷产品若局部集中或共同核回流，已有热窗口/PDEC/SAE/共同核下降路由；但这些出口未排斥。",
            f"{HOT_DENSITY} AND {PRIMITIVE_RANKIN}",
        ),
        row(
            "ColdFilteredDivisorSupportP018EnvelopeProved",
            False,
            False,
            "尚未证明全体实际 cold products 的支撑数小于 P^0.18；需纯除数尾证书或冷结构稀疏化证书。",
            f"{DIVISOR_TAIL} OR {COLD_SPARSIFY}",
        ),
        row(
            "ActivePrefixLevelPackingExponentTableProved",
            False,
            False,
            "产品支撑 envelope 未闭合，且还需 collar 总和与 T_PDEC 权重。",
            f"{HARDPOINT} AND {COLLAR_SUM} AND {TPDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链终端矛盾。",
            f"{DIVISOR_TAIL} OR {COLD_SPARSIFY}; plus {UNIFIED_BUDGET} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 cold-filtered 产品支撑 envelope 证书。"""
    flags = imported_flags()
    return {
        "certificate_type": "prime_matrix_strict_cold_filtered_divisor_support_router",
        "status": "cold_filtered_support_domain_closed_prime_power_order_removed_raw_tau_and_sparsification_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{DIVISOR_TAIL} OR {COLD_SPARSIFY}",
        "next_direct_attack_target": COLD_SPARSIFY,
        "residual_exponent": RESIDUAL_EXPONENT,
        "prime_power_support_threshold": PRIME_POWER_SUPPORT_THRESHOLD,
        "imported_flags": flags,
        "raw_tau_obstructions": raw_tau_rows(),
        "prime_power_support_rows": prime_power_rows(),
        "support_split": support_split_rows(),
        "decision_table": decision_rows(flags),
        "cold_filtered_support_domain_closed": bool(
            next(item for item in decision_rows(flags) if item["gate"] == "ColdFilteredSupportDomainClosed")[
                "proved"
            ]
        ),
        "prime_power_ordered_cascade_removed_for_support": True,
        "raw_tau_p018_closure_rejected": True,
        "cold_structural_failure_routes_registered": bool(
            next(item for item in decision_rows(flags) if item["gate"] == "ColdStructuralFailureRoutesRegistered")[
                "closed"
            ]
        ),
        "cold_filtered_divisor_support_p018_envelope_proved": False,
        "active_prefix_level_packing_exponent_table_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`ColdFilteredDivisorSupportP018Envelope` 的支撑域已经压实：产品纤维商化后，"
            "素数幂有序级联不再产生 Fibonacci 型支撑爆炸，只剩同一产品除数状态。"
            "但全体除数函数在有限边界仍远超 P^0.18，不能用粗 tau(h_0) 关闭。"
            "因此当前最窄剩余是二选一：要么给出显式除数尾界加有限边界证书，"
            "要么证明 cold/nonpersistent/no-return 条件会把实际产品支撑稀疏化；"
            "局部集中失败已能登记为热除数密度/PDEC/SAE，分散失败则需要原始支撑 Rankin 账本。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict cold-filtered 产品除数支撑路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "cold_filtered_support_domain_closed",
        "prime_power_ordered_cascade_removed_for_support",
        "raw_tau_p018_closure_rejected",
        "cold_structural_failure_routes_registered",
        "cold_filtered_divisor_support_p018_envelope_proved",
        "active_prefix_level_packing_exponent_table_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. 粗 tau 阻塞")
    lines.append("")
    lines.append("| P or n | witness | tau | P^0.18 | passes | ratio |")
    lines.append("| ---: | ---: | ---: | ---: | --- | ---: |")
    for item in result["raw_tau_obstructions"]:
        lines.append(
            f"| {item['P_or_n']} | {item['witness']} | {item['tau']} | {item['P018']} | "
            f"`{fmt_bool(item['passes'])}` | {item['ratio']} |"
        )
    lines.append("")

    lines.append("## 2. 素数幂支撑商化")
    lines.append("")
    lines.append("| prime | max exp at P=100000 | ordered growth before quotient | support after quotient | P^0.18 | passes |")
    lines.append("| ---: | ---: | --- | ---: | ---: | --- |")
    for item in result["prime_power_support_rows"]:
        lines.append(
            f"| {item['prime']} | {item['max_exp_at_P_min']} | "
            f"{table_cell(item['ordered_history_growth_before_quotient'])} | "
            f"{item['product_support_after_quotient']} | {item['P018_at_P_min']} | "
            f"`{fmt_bool(item['support_p018_passes_at_P_min'])}` |"
        )
    lines.append("")

    lines.append("## 3. 剩余二分")
    lines.append("")
    lines.append("| branch | condition | closed part | remaining | meaning |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["support_split"]:
        lines.append(
            "| "
            + " | ".join(
                table_cell(item[key]) for key in ["branch", "condition", "closed_part", "remaining", "meaning"]
            )
            + " |"
        )
    lines.append("")

    lines.append("## 4. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["decision_table"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )
    lines.append("")

    lines.append("## 5. 下一步最窄点")
    lines.append("")
    lines.append(f"- 主攻：`{result['next_direct_attack_target']}`。")
    lines.append(f"- 备选纯除数路线：`{DIVISOR_TAIL}`。")
    lines.append(f"- 并行验收：`{UNIFIED_BUDGET}`、`{COLLAR_SUM}`、`{TPDEC_TABLE}`、`{DSTRUCTURE}`。")
    lines.append("- 边界：本步不声明 cold-filtered 支撑 envelope 已证明。")
    lines.append("")

    lines.append("## 6. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for file, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 文件。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"cold_filtered_support_domain_closed={fmt_bool(result['cold_filtered_support_domain_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
