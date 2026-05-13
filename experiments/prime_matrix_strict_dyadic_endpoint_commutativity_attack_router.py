#!/usr/bin/env python3
"""生成 strict dyadic 乘积窗口端点交换律攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_dyadic_endpoint_commutativity_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json
  docs/monograph/prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-dyadic-order-canonicalization-attack-router.json",
    "prime-matrix-strict-dyadic-cold-window-cascade-attack-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
]

ENDPOINT_COMM = "DyadicProductWindowEndpointCommutativityLedger"
FORMULA_BINDING = "ProductWindowEndpointDyadicUpdateFormulaBindingLedger"
ROUNDING = "DyadicDirectedEndpointRoundingAssociativityLemma"
THRESHOLD_BINDING = "ColdCoreThresholdDyadicOrderInvarianceBindingLedger"
ROUNDING_DEFECT = "DyadicBoundaryRoundingPhaseDefectPDECRoute"
PHASE_DEFECT = "DyadicPathDependentColdWindowPhaseDefectPDECRoute"
CANON = "DyadicValuationOrderCanonicalizationOrPhaseDefectLedger"
DYADIC = "DyadicPrimePowerColdWindowCascadeExclusionLemma"
COLD_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
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
        "experiments/prime_matrix_strict_dyadic_endpoint_commutativity_attack_router.py": sha256(
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


def floor_div(n: int, d: int) -> int:
    """整数下取整除法。"""
    return n // d


def ceil_div(n: int, d: int) -> int:
    """整数上取整除法。"""
    return -((-n) // d)


def rounding_audit_rows() -> list[dict[str, Any]]:
    """给出 dyadic 端点取整结合律的有限样本审计。"""
    rows: list[dict[str, Any]] = []
    samples = [1, 2, 3, 17, 63, 64, 65, 511, 4097, 1234567]
    decompositions = [(1, 1), (1, 2), (2, 1), (3, 4), (4, 3), (5, 8), (8, 5)]
    for n in samples:
        for a, b in decompositions:
            d1, d2 = 2**a, 2**b
            floor_step = floor_div(floor_div(n, d1), d2)
            floor_once = floor_div(n, d1 * d2)
            ceil_step = ceil_div(ceil_div(n, d1), d2)
            ceil_once = ceil_div(n, d1 * d2)
            rows.append(
                {
                    "n": n,
                    "first_power": a,
                    "second_power": b,
                    "floor_step_equals_once": floor_step == floor_once,
                    "ceil_step_equals_once": ceil_step == ceil_once,
                    "floor_value": floor_once,
                    "ceil_value": ceil_once,
                }
            )
    return rows


def proof_rows() -> list[dict[str, str]]:
    """列出交换律证明原子。"""
    return [
        {
            "name": "floor_associativity",
            "statement": "floor(floor(n/a)/b)=floor(n/(ab)) for positive integers a,b,n",
            "status": "closed_elementary",
            "meaning": "外向左端点若由整数下取整给出，逐步缩放与一次缩放相同。",
        },
        {
            "name": "ceil_associativity",
            "statement": "ceil(ceil(n/a)/b)=ceil(n/(ab)) for positive integers a,b,n",
            "status": "closed_elementary",
            "meaning": "外向右端点若由整数上取整给出，逐步缩放与一次缩放相同。",
        },
        {
            "name": "dyadic_commutativity",
            "statement": "2^a 2^b=2^b 2^a and directed endpoint rounding depends only on a+b",
            "status": "closed_if_formula_bound",
            "meaning": "dyadic 顺序交换不会改变规范化后的端点。",
        },
        {
            "name": "formula_binding_gap",
            "statement": "current corpus says I_W is inherited from product window ledger, but does not expose the endpoint update formula",
            "status": "open_binding",
            "meaning": "必须把现有窗口账本绑定到上述外向端点缩放公式。",
        },
        {
            "name": "defect_route",
            "statement": "if product window endpoints are not the directed dyadic scaling endpoints, the discrepancy is a boundary phase defect",
            "status": "registered_route_open",
            "meaning": "公式绑定失败不能留作自由差异，必须进入 PDEC/ColumnCRT/热核心。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 dyadic 端点交换律判定表。"""
    canon = data["canon"]
    scaled = data["scaled"]

    target_imported = canon.get("next_direct_attack_target") == ENDPOINT_COMM
    window_exists = scaled.get("terminal_core_window_closed") is True
    rounding_ok = all(
        item["floor_step_equals_once"] and item["ceil_step_equals_once"]
        for item in rounding_audit_rows()
    )

    return [
        row(
            "EndpointCommutativityTargetImported",
            target_imported,
            False,
            "上一层已把 dyadic 顺序规范化压到窗口端点交换律。",
            ENDPOINT_COMM,
        ),
        row(
            "TerminalWindowObjectExists",
            window_exists,
            True,
            "现有材料有 I_W，但只作为继承自 product window ledger 的对象。",
            FORMULA_BINDING,
        ),
        row(
            "DyadicDirectedRoundingAssociativityClosed",
            rounding_ok,
            True,
            "若端点由 dyadic 外向整数缩放生成，则逐步缩放与一次缩放等价。",
            ROUNDING,
        ),
        row(
            "DyadicEndpointCommutativityConditionalClosed",
            rounding_ok,
            True,
            "在端点生成公式已绑定的条件下，dyadic 重排不改变 I_W。",
            FORMULA_BINDING,
        ),
        row(
            "ProductWindowEndpointFormulaBindingProved",
            False,
            False,
            "当前语料没有 machine-readable 端点更新公式，无法把 I_W 直接绑定到 dyadic 缩放。",
            FORMULA_BINDING,
        ),
        row(
            "ColdCoreThresholdOrderInvarianceProved",
            False,
            False,
            "C_core(W) 是否随 dyadic 重排不变仍需绑定到同一端点/尺度公式。",
            THRESHOLD_BINDING,
        ),
        row(
            "BoundaryRoundingDefectRouteRegistered",
            True,
            False,
            "若端点公式绑定失败，差异必须作为边界相位缺陷回流。",
            ROUNDING_DEFECT,
        ),
        row(
            "DyadicProductWindowEndpointCommutativityLedgerProved",
            False,
            False,
            "取整交换律已闭合，但端点公式绑定与阈值不变性未闭合。",
            f"{FORMULA_BINDING} AND {THRESHOLD_BINDING}",
        ),
        row(
            "DyadicValuationOrderCanonicalizationOrPhaseDefectProved",
            False,
            False,
            "端点交换律未完成，dyadic 顺序规范化仍未闭合。",
            CANON,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{FORMULA_BINDING} AND {PHASE_DEFECT} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 dyadic 端点交换律攻坚证书。"""
    data = {
        "canon": load_json("prime-matrix-strict-dyadic-order-canonicalization-attack-router.json"),
        "scaled": load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"),
    }
    rows = build_rows(data)
    rounding_rows = rounding_audit_rows()
    rounding_closed = all(
        item["floor_step_equals_once"] and item["ceil_step_equals_once"]
        for item in rounding_rows
    )

    return {
        "certificate_type": "prime_matrix_strict_dyadic_endpoint_commutativity_attack_router",
        "status": "dyadic_endpoint_commutativity_reduced_to_product_window_formula_binding_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dyadic_directed_rounding_associativity_closed": rounding_closed,
        "dyadic_endpoint_commutativity_conditional_on_formula_closed": rounding_closed,
        "product_window_endpoint_formula_binding_proved": False,
        "cold_core_threshold_order_invariance_proved": False,
        "boundary_rounding_defect_route_registered": True,
        "dyadic_product_window_endpoint_commutativity_ledger_proved": False,
        "dyadic_valuation_order_canonicalization_or_phase_defect_proved": False,
        "dyadic_prime_power_cold_window_cascade_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": ENDPOINT_COMM,
        "hardpoint_after_router": f"{FORMULA_BINDING} AND {THRESHOLD_BINDING}",
        "next_direct_attack_target": FORMULA_BINDING,
        "parallel_attack_targets": [
            THRESHOLD_BINDING,
            ROUNDING_DEFECT,
            PHASE_DEFECT,
            COLD_ANTICASCADE,
            DYADIC,
            DSTRUCTURE,
        ],
        "proof_rows": proof_rows(),
        "rounding_audit_rows": rounding_rows,
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`DyadicProductWindowEndpointCommutativityLedger` 的纯取整子引理可以闭合："
            "对正整数 `a,b,n`，`floor(floor(n/a)/b)=floor(n/(ab))` 且 "
            "`ceil(ceil(n/a)/b)=ceil(n/(ab))`；取 `a,b` 为 2 的幂时，端点外向缩放只依赖总指数。"
            "因此只要现有 product window ledger 的 `I_W` 端点确实由这种 dyadic 外向缩放公式生成，"
            "dyadic 重排交换律就成立。当前仍缺的是把 `I_W` 与 `C_core(W)` 绑定到该 machine-readable 端点公式；"
            "否则端点差异必须作为边界相位缺陷回流。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict dyadic 乘积窗口端点交换律攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dyadic_directed_rounding_associativity_closed={fmt_bool(result['dyadic_directed_rounding_associativity_closed'])}",
        f"dyadic_endpoint_commutativity_conditional_on_formula_closed={fmt_bool(result['dyadic_endpoint_commutativity_conditional_on_formula_closed'])}",
        f"product_window_endpoint_formula_binding_proved={fmt_bool(result['product_window_endpoint_formula_binding_proved'])}",
        f"cold_core_threshold_order_invariance_proved={fmt_bool(result['cold_core_threshold_order_invariance_proved'])}",
        f"dyadic_product_window_endpoint_commutativity_ledger_proved={fmt_bool(result['dyadic_product_window_endpoint_commutativity_ledger_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 证明原子",
        "",
        "| name | statement | status | meaning |",
        "|---|---|---|---|",
    ]
    for item in result["proof_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['name'])}` | "
            f"`{table_cell(item['statement'])}` | "
            f"`{table_cell(item['status'])}` | "
            f"{table_cell(item['meaning'])} |"
        )

    lines.extend(
        [
            "",
            "## 取整样本审计",
            "",
            "| n | first_power | second_power | floor_ok | ceil_ok | floor_value | ceil_value |",
            "|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["rounding_audit_rows"][:28]:
        lines.append(
            "| "
            f"{item['n']} | "
            f"{item['first_power']} | "
            f"{item['second_power']} | "
            f"`{fmt_bool(item['floor_step_equals_once'])}` | "
            f"`{fmt_bool(item['ceil_step_equals_once'])}` | "
            f"{item['floor_value']} | "
            f"{item['ceil_value']} |"
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
