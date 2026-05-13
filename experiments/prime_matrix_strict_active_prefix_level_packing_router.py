#!/usr/bin/env python3
"""生成 strict 活动前缀层打包指数表路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_active_prefix_level_packing_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-active-prefix-level-packing-router.json

输出：
  docs/monograph/prime-matrix-strict-active-prefix-level-packing-router.json
  docs/monograph/prime-matrix-strict-active-prefix-level-packing-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-active-prefix-level-packing-router.json"
OUT_MD = DOCS / "prime-matrix-strict-active-prefix-level-packing-router.md"

ACTIVE_PACKING = "ActivePrefixLevelPackingExponentTable"
PRODUCT_FIBER = "ActivePrefixProductFiberMultiplicityOrNamedReturnLedger"
DIVISOR_ENV = "DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope"
COLD_FILTER = "ColdNonpersistentProductSupportSparsificationLemma"
COLLAR_SUM = "SameParameterSiblingCollarWidthFiniteSumTable"
TPDEC_TABLE = "SameParameterPDECThresholdNumericTable"
LOAD_LOWER = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
PER_LEVEL = "SameParameterPerLevelColdSupportExponentTable"
ROW_FREE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
SPARSE_ANTI = "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
LOG_EPSILON = 0.25
RESIDUAL_EXPONENT = ALPHA - LOG_EPSILON
P_MIN = 100_000

SOURCE_FILES = [
    "prime-matrix-strict-same-parameter-per-level-support-exponent-router.json",
    "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    "prime-matrix-strict-row-free-type-anticollapse-sync-router.json",
    "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json",
    "prime-matrix-strict-sparse-terminal-history-router.json",
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
        "experiments/prime_matrix_strict_active_prefix_level_packing_router.py": sha256(
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


def max_divisor_count(limit: int) -> dict[str, Any]:
    """暴力核验小边界内最大除数函数。"""
    best_n = 1
    best_tau = 1
    for n in range(2, limit + 1):
        tau = divisor_count(n)
        if tau > best_tau:
            best_n = n
            best_tau = tau
    p_residual = limit**RESIDUAL_EXPONENT
    return {
        "limit": limit,
        "max_tau_n": best_n,
        "max_tau": best_tau,
        "P_residual_exponent": round(p_residual, 6),
        "raw_divisor_bound_passes": best_tau < p_residual,
        "ratio": round(best_tau / p_residual, 6),
    }


def projection_rows() -> list[dict[str, str]]:
    """列出活动前缀到产品除数支撑的投影。"""
    return [
        {
            "name": "product_projection",
            "formula": "Phi(U)=D(U)=prod_i g_i, with D(U)|h_0",
            "status": "closed_interface",
            "meaning": "每个活动前缀投影到同一 formal unit 的一个产品除数。",
        },
        {
            "name": "level_product_fiber",
            "formula": "A_j(d)={U in A_j: D(U)=d}",
            "status": "closed_definition",
            "meaning": "同层活动前缀数分解为产品支撑数与每个产品纤维重数。",
        },
        {
            "name": "packing_identity",
            "formula": "|A_j|=sum_{d|h_0} |A_j(d)|",
            "status": "closed_identity",
            "meaning": "活动前缀打包必须同时控制产品支撑和纤维重数。",
        },
        {
            "name": "fiber_named_return_gate",
            "formula": "large |A_j(d)| -> same product/type recurrence -> named PDEC/SAE/ColumnCRT/hot return",
            "status": "registered_not_proved",
            "meaning": "同一产品下多前缀若不可区分，不能作为自由冷支撑；但全局排斥未完成。",
        },
    ]


def obstruction_rows() -> list[dict[str, Any]]:
    """列出粗除数支撑界不足的证据。"""
    rows = [
        max_divisor_count(P_MIN),
    ]
    for n in [83_160, 110_880, 720_720, 1_081_080]:
        tau = divisor_count(n)
        rows.append(
            {
                "limit": n,
                "max_tau_n": n,
                "max_tau": tau,
                "P_residual_exponent": round(n**RESIDUAL_EXPONENT, 6),
                "raw_divisor_bound_passes": tau < n**RESIDUAL_EXPONENT,
                "ratio": round(tau / (n**RESIDUAL_EXPONENT), 6),
            }
        )
    return rows


def route_rows() -> list[dict[str, str]]:
    """列出最新打包指数表的源头输入。"""
    return [
        {
            "route": PRODUCT_FIBER,
            "task": "证明同一产品 d 的活动前缀纤维若过大，必形成固定历史、PDEC/SAE、ColumnCRT、热核心或 row-free 标签回流。",
            "status": "open",
        },
        {
            "route": DIVISOR_ENV,
            "task": "给出产品除数支撑的 P^0.18 级有限/解析 envelope；粗 tau(h_0) 界在 P=100000 边界失败。",
            "status": "open",
        },
        {
            "route": COLD_FILTER,
            "task": "利用 cold/nonpersistent 条件删去大多数产品除数，而不是对所有 d|h_0 求和。",
            "status": "open",
        },
        {
            "route": COLLAR_SUM,
            "task": "活动前缀数一旦可控，还需同步控制同层 collar debit 总和。",
            "status": "parallel_open",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "ActivePackingTargetImported",
            result["active_packing_target_imported"],
            result["active_packing_target_imported"],
            "上一层已把每层冷支撑指数表压成活动前缀层打包。",
            ACTIVE_PACKING,
        ),
        row(
            "ProductProjectionClosed",
            result["product_projection_closed"],
            result["product_projection_closed"],
            "每个活动前缀投影到产品除数 D(U)|h_0。",
            ACTIVE_PACKING,
        ),
        row(
            "PackingIdentityClosed",
            result["packing_identity_closed"],
            result["packing_identity_closed"],
            "|A_j|=sum_{d|h_0}|A_j(d)|，必须同时控制除数支撑和产品纤维。",
            f"{PRODUCT_FIBER} AND {DIVISOR_ENV}",
        ),
        row(
            "RawDivisorP018BoundRejectedAtBoundary",
            result["raw_divisor_p018_bound_rejected_at_boundary"],
            result["raw_divisor_p018_bound_rejected_at_boundary"],
            "P=100000 附近 tau(h_0) 可远大于 P^0.18，不能只靠 D(U)|h_0。",
            f"{DIVISOR_ENV} OR {COLD_FILTER}",
        ),
        row(
            "NoSilentCollapseImportedForFibers",
            result["no_silent_collapse_imported_for_fibers"],
            result["no_silent_collapse_imported_for_fibers"],
            "标签塌缩不会让义务消失；同产品多前缀必须进入负载、冷供给或命名回流。",
            PRODUCT_FIBER,
        ),
        row(
            "ActivePrefixLevelPackingExponentTableProved",
            False,
            False,
            "尚未证明产品纤维重数和 cold-filtered 除数支撑满足 P^(0.18-tau) 指数界。",
            f"{PRODUCT_FIBER} AND {DIVISOR_ENV} AND {COLD_FILTER}",
        ),
        row(
            "SameParameterPerLevelColdSupportExponentTableProved",
            False,
            False,
            "活动前缀打包、collar 总和和 T_PDEC 权重仍未全部闭合。",
            f"{ACTIVE_PACKING} AND {COLLAR_SUM} AND {TPDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{PRODUCT_FIBER} AND {DIVISOR_ENV} AND {LOAD_LOWER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造活动前缀层打包证书。"""
    per_level = load_json("prime-matrix-strict-same-parameter-per-level-support-exponent-router.json")
    prefix_branch = load_json("prime-matrix-strict-cold-history-prefix-branching-attack-router.json")
    sparse_anti = load_json("prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json")
    row_free = load_json("prime-matrix-strict-row-free-type-anticollapse-sync-router.json")
    formal_mult = load_json("prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json")

    target = per_level.get("next_direct_attack_target") == ACTIVE_PACKING
    product_projection = bool(prefix_branch.get("same_prefix_lcm_anchor_closed")) or (
        formal_mult.get("history_product_identity_closed") is True
    )
    no_silent = (
        sparse_anti.get("prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget") is True
        and row_free.get("prefix_label_support_to_row_free_type_anticollapse_closed_for_budget") is True
    )
    obstructions = obstruction_rows()
    raw_rejected = any(not item["raw_divisor_bound_passes"] for item in obstructions)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_active_prefix_level_packing_router",
        "status": "active_prefix_packing_reduced_to_product_fiber_and_divisor_envelope_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "alpha": ALPHA,
        "log_absorption_epsilon": LOG_EPSILON,
        "residual_exponent_after_log_absorption": round(RESIDUAL_EXPONENT, 6),
        "active_packing_target_imported": target,
        "product_projection_closed": product_projection,
        "packing_identity_closed": product_projection,
        "raw_divisor_p018_bound_rejected_at_boundary": raw_rejected,
        "no_silent_collapse_imported_for_fibers": no_silent,
        "active_prefix_product_fiber_multiplicity_or_named_return_ledger_proved": False,
        "divisor_support_p018_finite_boundary_or_analytic_envelope_proved": False,
        "cold_nonpersistent_product_support_sparsification_lemma_proved": False,
        "active_prefix_level_packing_exponent_table_proved": False,
        "same_parameter_per_level_cold_support_exponent_table_proved": False,
        "core_history_weighted_support_measure_table_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": ACTIVE_PACKING,
        "hardpoint_after_router": f"{PRODUCT_FIBER} AND {DIVISOR_ENV} AND {COLD_FILTER}",
        "next_direct_attack_target": PRODUCT_FIBER,
        "parallel_attack_targets": [
            DIVISOR_ENV,
            COLD_FILTER,
            COLLAR_SUM,
            TPDEC_TABLE,
            LOAD_LOWER,
            NAMED_RETURN,
            ROW_FREE,
            SPARSE_ANTI,
            DSTRUCTURE,
        ],
        "projection_rows": projection_rows(),
        "obstruction_rows": obstructions,
        "route_rows": route_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ActivePrefixLevelPackingExponentTable` 已被压成产品投影问题。"
            "每个活动前缀 `U` 给出 `D(U)|h_0`，同层活动数满足 "
            "`|A_j|=sum_{d|h_0}|A_j(d)|`。因此必须同时控制产品除数支撑和同一产品纤维重数。"
            "粗除数函数界不能关闭本目标：在 `P=100000` 边界内，`tau(83160)=128`，"
            "而 `P^0.18≈7.94`，远远超预算。"
            "所以最新最窄点不是继续调常数，而是 `ActivePrefixProductFiberMultiplicityOrNamedReturnLedger`："
            "证明同一产品下多前缀若过大，必进入固定历史、PDEC/SAE、ColumnCRT、热核心或标签回流；"
            "并配合 cold-filtered 产品支撑 envelope。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 活动前缀层打包指数路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"active_packing_target_imported={fmt_bool(result['active_packing_target_imported'])}",
        f"product_projection_closed={fmt_bool(result['product_projection_closed'])}",
        f"packing_identity_closed={fmt_bool(result['packing_identity_closed'])}",
        f"raw_divisor_p018_bound_rejected_at_boundary={fmt_bool(result['raw_divisor_p018_bound_rejected_at_boundary'])}",
        f"no_silent_collapse_imported_for_fibers={fmt_bool(result['no_silent_collapse_imported_for_fibers'])}",
        f"active_prefix_level_packing_exponent_table_proved={fmt_bool(result['active_prefix_level_packing_exponent_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 产品投影",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["projection_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['name'])}`",
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
            "## 2. 粗除数界阻塞",
            "",
            "| limit/P | witness n | tau | P^0.18 | raw bound passes | ratio |",
            "| ---: | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for item in result["obstruction_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["limit"]),
                    str(item["max_tau_n"]),
                    str(item["max_tau"]),
                    str(item["P_residual_exponent"]),
                    f"`{fmt_bool(item['raw_divisor_bound_passes'])}`",
                    str(item["ratio"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 路线拆分",
            "",
            "| route | task | status |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["route_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['route'])}`",
                    table_cell(item["task"]),
                    f"`{table_cell(item['status'])}`",
                ]
            )
            + " |"
        )

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
            "## 5. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 并行：`{DIVISOR_ENV}`、`{COLD_FILTER}`、`{COLLAR_SUM}`、`{TPDEC_TABLE}`。",
            "- 边界：本步关闭产品投影和粗除数界阻塞审查；未证明活动前缀打包指数。",
            "",
            "## 6. 依赖哈希",
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
    print(f"product_projection_closed={fmt_bool(result['product_projection_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
