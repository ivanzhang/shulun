#!/usr/bin/env python3
"""生成 strict cold 产品支撑稀疏化账本路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_product_support_sparsification_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-product-support-sparsification-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-product-support-sparsification-router.json
  docs/monograph/prime-matrix-strict-cold-product-support-sparsification-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.md"

HARDPOINT = "ColdProductSupportSparsificationBeyondTauLedger"
DYADIC_BLOCK = "DyadicColdProductBlockOverloadCertificate"
HOT_DENSITY = "ShortWindowHotDivisorDensityPDECorSAEReturnExclusion"
COMMON_KERNEL = "CommonKernelReturnCycleDescentOrPDECLedger"
PRIMITIVE_RANKIN = "PrimitiveProductSupportRankinLedger"
DIVISOR_TAIL = "ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate"
SUPPORT_ENV = "ColdFilteredDivisorSupportP018Envelope"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
LOG_EPSILON = 0.25
RESIDUAL_EXPONENT = ALPHA - LOG_EPSILON
P_MIN = 100_000

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-cold-filtered-divisor-support-router.json",
    DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
    DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    DOCS / "prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.json",
    DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json",
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
        "experiments/prime_matrix_strict_cold_product_support_sparsification_router.py": sha256(
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


def imported_flags() -> dict[str, bool]:
    """读取稀疏化账本需要的导入。"""
    support = load_json(DOCS / "prime-matrix-strict-cold-filtered-divisor-support-router.json")
    density = load_json(DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json")
    kernel = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    branch = load_json(DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json")
    reciprocal = load_json(DOCS / "prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.json")
    return {
        "cold_filtered_support_domain_closed": bool(support.get("cold_filtered_support_domain_closed")),
        "prime_power_ordered_cascade_removed_for_support": bool(
            support.get("prime_power_ordered_cascade_removed_for_support")
        ),
        "raw_tau_p018_closure_rejected": bool(support.get("raw_tau_p018_closure_rejected")),
        "reciprocal_to_density_certificate_closed": bool(density.get("hot_density_certificate_closed")),
        "generic_tau_closure_rejected": bool(density.get("generic_tau_closure_rejected")),
        "free_common_kernel_return_cycle_excluded": bool(kernel.get("free_common_kernel_return_cycle_excluded")),
        "prefix_branching_structural_dichotomy_closed": bool(
            branch.get("prefix_branching_structural_dichotomy_closed")
        ),
        "windowed_reciprocal_envelope_closed": bool(reciprocal.get("windowed_reciprocal_envelope_closed")),
        "hot_window_pigeonhole_closed": bool(reciprocal.get("hot_window_pigeonhole_closed")),
    }


def dyadic_rows() -> list[dict[str, Any]]:
    """给出 dyadic 块过载阈值样例。"""
    rows: list[dict[str, Any]] = []
    for p in [10**5, 10**6, 10**8, 10**12]:
        block_count = math.floor(math.log(p, 2)) + 1
        total_threshold = p**RESIDUAL_EXPONENT
        rows.append(
            {
                "P": p,
                "dyadic_blocks": block_count,
                "P018": round(total_threshold, 6),
                "block_overload_threshold": round(total_threshold / block_count, 6),
                "meaning": "if total support exceeds P^0.18, some block exceeds this threshold",
            }
        )
    return rows


def overload_case_rows() -> list[dict[str, str]]:
    """列出 dyadic 过载块的后续分支。"""
    return [
        {
            "case": "dense_local_window",
            "trigger": "many cold products occupy one short multiplicative window with large reciprocal/count mass",
            "closed_part": "hot density certificate can be produced",
            "remaining": HOT_DENSITY,
            "meaning": "局部集中不是普通除数支撑，而是热窗口/PDEC/SAE/ColumnCRT 终端。",
        },
        {
            "case": "common_kernel_cluster",
            "trigger": "many products share a low multiplier kernel or repeated quotient type",
            "closed_part": "free return cycle excluded; persistent finite type routes to PDEC",
            "remaining": COMMON_KERNEL,
            "meaning": "共同核不能免费循环，但仍需排斥 PDEC/命名回流或完成预算吸收。",
        },
        {
            "case": "primitive_dispersion",
            "trigger": "products stay sparse in every short window and avoid common-kernel clustering",
            "closed_part": "this is the only remaining nonlocal support mode",
            "remaining": PRIMITIVE_RANKIN,
            "meaning": "分散支撑必须由逐素数 Rankin/Euler 原始支撑账本给出小于 P^0.18 的总界。",
        },
        {
            "case": "pure_tau_fallback",
            "trigger": "ignore cold structure and bound all divisors",
            "closed_part": "recognized as a separate route",
            "remaining": DIVISOR_TAIL,
            "meaning": "需要显式除数尾界和有限边界；不能替代 cold 结构稀疏化。",
        },
    ]


def decision_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    structural_split_closed = (
        flags["cold_filtered_support_domain_closed"]
        and flags["reciprocal_to_density_certificate_closed"]
        and flags["free_common_kernel_return_cycle_excluded"]
        and flags["prefix_branching_structural_dichotomy_closed"]
    )
    return [
        row(
            "ColdSparsificationTargetImported",
            True,
            flags["cold_filtered_support_domain_closed"],
            "上一层已把支撑域限制为商化后的 cold/nonpersistent/no-return 产品除数。",
            HARDPOINT,
        ),
        row(
            "DyadicOverloadCertificateClosed",
            True,
            True,
            "若总 cold 产品支撑超过 P^0.18，则某个 dyadic 产品块必超过 P^0.18/(floor(log2 P)+1)。",
            DYADIC_BLOCK,
        ),
        row(
            "PrimePowerSupportCascadeAlreadyRemoved",
            True,
            flags["prime_power_ordered_cascade_removed_for_support"],
            "素数幂有序级联已经被产品商化压成指数状态，不能再作为本硬点阻塞。",
            "closed for support",
        ),
        row(
            "OverloadBlockStructuralSplitClosed",
            structural_split_closed,
            structural_split_closed,
            "一个过载 dyadic 块若不进入热窗口，就必须进入共同核簇或原始分散支撑。",
            f"{HOT_DENSITY} OR {COMMON_KERNEL} OR {PRIMITIVE_RANKIN}",
        ),
        row(
            "HotDensityOrCommonKernelExclusionProved",
            False,
            False,
            "热窗口、PDEC/SAE/ColumnCRT 和共同核命名回流尚未全部排斥。",
            f"{HOT_DENSITY} AND {COMMON_KERNEL}",
        ),
        row(
            "PrimitiveProductSupportRankinLedgerProved",
            False,
            False,
            "分散产品支撑的逐素数 Rankin/Euler 总界尚未给出。",
            PRIMITIVE_RANKIN,
        ),
        row(
            "ColdProductSupportSparsificationBeyondTauLedgerProved",
            False,
            False,
            "本步完成过载块三分法，但未证明三类坏情形都被排斥或吸收。",
            f"{HOT_DENSITY} AND {COMMON_KERNEL} AND {PRIMITIVE_RANKIN}",
        ),
        row(
            "ColdFilteredDivisorSupportP018EnvelopeProved",
            False,
            False,
            "cold 稀疏化未闭合，纯除数尾界也未闭合，因此产品支撑 envelope 仍开。",
            f"{HARDPOINT} OR {DIVISOR_TAIL}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未形成排除早期零行反例链的终端矛盾。",
            f"{PRIMITIVE_RANKIN} AND {UNIFIED_BUDGET} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 cold 产品支撑稀疏化账本。"""
    flags = imported_flags()
    decisions = decision_rows(flags)
    return {
        "certificate_type": "prime_matrix_strict_cold_product_support_sparsification_router",
        "status": "cold_product_sparsification_reduced_to_overload_block_hot_kernel_or_rankin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{HOT_DENSITY} AND {COMMON_KERNEL} AND {PRIMITIVE_RANKIN}",
        "next_direct_attack_target": PRIMITIVE_RANKIN,
        "imported_flags": flags,
        "dyadic_overload_rows": dyadic_rows(),
        "overload_cases": overload_case_rows(),
        "decision_table": decisions,
        "dyadic_overload_certificate_closed": True,
        "overload_block_structural_split_closed": bool(
            next(item for item in decisions if item["gate"] == "OverloadBlockStructuralSplitClosed")["proved"]
        ),
        "hot_density_or_common_kernel_exclusion_proved": False,
        "primitive_product_support_rankin_ledger_proved": False,
        "cold_product_support_sparsification_beyond_tau_ledger_proved": False,
        "cold_filtered_divisor_support_p018_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`ColdProductSupportSparsificationBeyondTauLedger` 已被压成 dyadic 过载块三分法："
            "若总 cold 产品支撑超过 `P^0.18`，则某个产品 dyadic 块过载；过载块若局部集中，"
            "就登记为热除数密度/PDEC/SAE；若共享低乘子共同核，就进入共同核下降或 PDEC；"
            "若既不集中也无共同核，则只剩原始分散支撑，需要逐素数 Rankin/Euler 账本。"
            "本步关闭的是拆分和过载证书，不关闭三类终端排斥。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict cold 产品支撑稀疏化路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "dyadic_overload_certificate_closed",
        "overload_block_structural_split_closed",
        "hot_density_or_common_kernel_exclusion_proved",
        "primitive_product_support_rankin_ledger_proved",
        "cold_product_support_sparsification_beyond_tau_ledger_proved",
        "cold_filtered_divisor_support_p018_envelope_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. Dyadic 过载阈值")
    lines.append("")
    lines.append("| P | dyadic blocks | P^0.18 | block overload threshold | meaning |")
    lines.append("| ---: | ---: | ---: | ---: | --- |")
    for item in result["dyadic_overload_rows"]:
        lines.append(
            f"| {item['P']} | {item['dyadic_blocks']} | {item['P018']} | "
            f"{item['block_overload_threshold']} | {item['meaning']} |"
        )
    lines.append("")

    lines.append("## 2. 过载块分支")
    lines.append("")
    lines.append("| case | trigger | closed part | remaining | meaning |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["overload_cases"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["case", "trigger", "closed_part", "remaining", "meaning"])
            + " |"
        )
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
    lines.append(f"- 并行排斥：`{HOT_DENSITY}`、`{COMMON_KERNEL}`。")
    lines.append(f"- 备选：`{DIVISOR_TAIL}`。")
    lines.append("- 边界：本步不声明 cold 产品支撑稀疏化已完成。")
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
    """生成 JSON 与 Markdown 文件。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"dyadic_overload_certificate_closed={fmt_bool(result['dyadic_overload_certificate_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
