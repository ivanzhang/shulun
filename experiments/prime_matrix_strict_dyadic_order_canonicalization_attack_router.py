#!/usr/bin/env python3
"""生成 strict dyadic 顺序规范化/相位缺陷攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_dyadic_order_canonicalization_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-dyadic-order-canonicalization-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-dyadic-order-canonicalization-attack-router.json
  docs/monograph/prime-matrix-strict-dyadic-order-canonicalization-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-dyadic-order-canonicalization-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-dyadic-order-canonicalization-attack-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-dyadic-cold-window-cascade-attack-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json",
    "prime-matrix-strict-fixed-quotient-type-columncrt-router.json",
]

CANON = "DyadicValuationOrderCanonicalizationOrPhaseDefectLedger"
ENDPOINT_COMM = "DyadicProductWindowEndpointCommutativityLedger"
PHASE_DEFECT = "DyadicPathDependentColdWindowPhaseDefectPDECRoute"
VALUATION_COMPRESS = "PureDyadicValuationStateCompressionLedger"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
COLD_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
DYADIC = "DyadicPrimePowerColdWindowCascadeExclusionLemma"
SMALL_TABLE = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
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
        "experiments/prime_matrix_strict_dyadic_order_canonicalization_attack_router.py": sha256(
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


def audit_rows() -> list[dict[str, str]]:
    """列出 dyadic 顺序规范化审查对象。"""
    return [
        {
            "object": "frequency",
            "current_formula": "H_W=h_0/D(W)",
            "depends_on_order": "no",
            "audit_result": "same total v2 gives same H_W",
        },
        {
            "object": "terminal_core_divisibility",
            "current_formula": "k | H_W",
            "depends_on_order": "no",
            "audit_result": "same total v2 gives same divisor universe",
        },
        {
            "object": "terminal_core_window",
            "current_formula": "I_W=(Y_W^-,Y_W^+] inherited from product window ledger",
            "depends_on_order": "not ruled out",
            "audit_result": "current corpus names I_W by W, not by D(W); commutativity is not proved",
        },
        {
            "object": "cold_threshold",
            "current_formula": "C_core(W)",
            "depends_on_order": "not ruled out",
            "audit_result": "current corpus does not prove C_core(W)=C_core(D(W)) for dyadic reorderings",
        },
        {
            "object": "registered_return",
            "current_formula": "path/window/label difference -> PDEC/ColumnCRT/hot core",
            "depends_on_order": "registered if difference exists",
            "audit_result": "order sensitivity can be made a named defect, but exclusion remains open",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 dyadic 顺序规范化判定表。"""
    dyadic = data["dyadic"]
    scaled = data["scaled"]
    mult = data["multiplicity"]
    fixed = data["fixed"]

    target_imported = dyadic.get("next_direct_attack_target") == CANON
    frequency_closed = (
        scaled.get("scaled_core_frequency_closed") is True
        and mult.get("history_product_identity_closed") is True
    )
    window_closed = scaled.get("terminal_core_window_closed") is True
    cold_hot = scaled.get("cold_hot_split_closed") is True
    fixed_route = fixed.get("fixed_type_pdec_route_registered") is True

    return [
        row(
            "CanonicalizationTargetImported",
            target_imported,
            False,
            "上一层已把 dyadic 主硬点压成顺序规范化或相位缺陷。",
            CANON,
        ),
        row(
            "DyadicFrequencyOrderInvariantClosed",
            frequency_closed,
            True,
            "同总 v2 的 dyadic 路径有同一 D(W)=2^s 和同一 H_W。",
            VALUATION_COMPRESS,
        ),
        row(
            "TerminalDivisorUniverseOrderInvariantClosed",
            frequency_closed,
            True,
            "终端核心除数宇宙 k|H_W 对 dyadic 顺序不敏感。",
            VALUATION_COMPRESS,
        ),
        row(
            "ProductWindowExistsButCommutativityOpen",
            window_closed,
            False,
            "I_W 已存在，但现有材料只证明按 W 定义，未证明 dyadic 重排后窗口端点相同。",
            ENDPOINT_COMM,
        ),
        row(
            "ColdThresholdOrderInvarianceOpen",
            False,
            False,
            "C_core(W) 是否只依赖累计 v2 与奇核尚未证明。",
            ENDPOINT_COMM,
        ),
        row(
            "OrderDependenceDefectRouteRegistered",
            cold_hot and fixed_route,
            False,
            "若同 H_W 的不同顺序给出不同 I_W 或标签，则该差异必须回流 PDEC/ColumnCRT/热核心。",
            PHASE_DEFECT,
        ),
        row(
            "DyadicOrderCanonicalizationOrPhaseDefectLedgerProved",
            False,
            False,
            "尚未证明 dyadic 窗口端点交换律，也未完成顺序相位缺陷排斥。",
            f"{ENDPOINT_COMM} OR {PHASE_DEFECT}",
        ),
        row(
            "DyadicPrimePowerColdWindowCascadeExcluded",
            False,
            False,
            "dyadic 二选一账本未闭合，因此 dyadic 级联仍未排除。",
            DYADIC,
        ),
        row(
            "SmallPrimePowerCascadeTableProved",
            False,
            False,
            "dyadic 未闭合，p=2,3,5 小素数表仍未闭合。",
            SMALL_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{ENDPOINT_COMM} AND {PHASE_DEFECT} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 dyadic 顺序规范化攻坚证书。"""
    data = {
        "dyadic": load_json("prime-matrix-strict-dyadic-cold-window-cascade-attack-router.json"),
        "scaled": load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"),
        "multiplicity": load_json("prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json"),
        "fixed": load_json("prime-matrix-strict-fixed-quotient-type-columncrt-router.json"),
    }
    rows = build_rows(data)

    return {
        "certificate_type": "prime_matrix_strict_dyadic_order_canonicalization_attack_router",
        "status": "dyadic_canonicalization_reduced_to_window_endpoint_commutativity_or_phase_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dyadic_frequency_order_invariant_closed": True,
        "terminal_divisor_universe_order_invariant_closed": True,
        "product_window_exists": True,
        "dyadic_product_window_endpoint_commutativity_proved": False,
        "cold_threshold_order_invariance_proved": False,
        "order_dependence_defect_route_registered": True,
        "dyadic_path_dependent_phase_defect_pdec_route_proved": False,
        "dyadic_valuation_order_canonicalization_or_phase_defect_proved": False,
        "dyadic_prime_power_cold_window_cascade_excluded": False,
        "small_prime_power_cascade_table_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": CANON,
        "hardpoint_after_router": f"{ENDPOINT_COMM} OR {PHASE_DEFECT}",
        "next_direct_attack_target": ENDPOINT_COMM,
        "parallel_attack_targets": [
            PHASE_DEFECT,
            COLD_ANTICASCADE,
            HOT_CORE,
            FIXED_HISTORY,
            DYADIC,
            DSTRUCTURE,
        ],
        "audit_rows": audit_rows(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`DyadicValuationOrderCanonicalizationOrPhaseDefectLedger` 不能直接闭合为规范化，"
            "因为当前材料只证明了 `H_W=h_0/D(W)` 和终端除数宇宙对 dyadic 顺序不敏感；"
            "窗口仍写作 `I_W`，阈值仍写作 `C_core(W)`，二者尚未证明只依赖累计 `v2`。"
            "因此最新最窄点是 `DyadicProductWindowEndpointCommutativityLedger`：若 dyadic 乘积窗口端点满足交换律，"
            "Fibonacci 顺序爆炸坍缩为 valuation states；若不满足，差异就是 `DyadicPathDependentColdWindowPhaseDefectPDECRoute`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict dyadic 顺序规范化/相位缺陷攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dyadic_frequency_order_invariant_closed={fmt_bool(result['dyadic_frequency_order_invariant_closed'])}",
        f"terminal_divisor_universe_order_invariant_closed={fmt_bool(result['terminal_divisor_universe_order_invariant_closed'])}",
        f"dyadic_product_window_endpoint_commutativity_proved={fmt_bool(result['dyadic_product_window_endpoint_commutativity_proved'])}",
        f"order_dependence_defect_route_registered={fmt_bool(result['order_dependence_defect_route_registered'])}",
        f"dyadic_valuation_order_canonicalization_or_phase_defect_proved={fmt_bool(result['dyadic_valuation_order_canonicalization_or_phase_defect_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 审查表",
        "",
        "| object | current_formula | depends_on_order | audit_result |",
        "|---|---|---|---|",
    ]
    for item in result["audit_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['object'])}` | "
            f"`{table_cell(item['current_formula'])}` | "
            f"`{table_cell(item['depends_on_order'])}` | "
            f"{table_cell(item['audit_result'])} |"
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
    for item in result["rows"]:
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
