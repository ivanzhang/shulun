#!/usr/bin/env python3
"""生成 strict Table 6.3 b=28 psi/psi0 端点口径转换证书。

用法示例：
  python3 experiments/prime_matrix_strict_table63_b28_psi_endpoint_convention_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table63-b28-psi-endpoint-convention-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 80

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-table63-b28-psi-endpoint-convention-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table63-b28-psi-endpoint-convention-router.md"

PREVIOUS = DOCS / "prime-matrix-strict-table63-b28-actual-formula-declaration-router.json"
INTERNAL_PSI0 = DOCS / "prime-matrix-b3-internal-psi0-perron-formula-router.json"
TABLE63 = DOCS / "prime-matrix-strict-machine-readable-dusart-table63-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"

SOURCE_FILES = [PREVIOUS, INTERNAL_PSI0, TABLE63, CLAIM_STATUS]

TARGET = "Table63B28PsiVsPsi0EndpointConventionLedger"
KERNEL = "Table63B28KernelTruncationAndSmoothingConventionLedger"
FINITE_RH = "Table63B28FiniteRHHeightEndpointAndZeroBlockLedger"
ZERO_TAIL = "Table63B28ZeroFreeTailConstantsAndStartHeightLedger"
BUDGET = "Table63B28PsiEpsilonBudgetPartitionLedger"
ROUNDING = "Table63B28DirectedUpperRoundingAndIntervalPropagationLedger"
HASH = "Table63B28ReproducibleComputationHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

EXP28 = Decimal(28).exp()
ENDPOINT_TAX_ABS_AT_EXP28 = Decimal(14)
ENDPOINT_TAX_REL_AT_EXP28 = ENDPOINT_TAX_ABS_AT_EXP28 / EXP28
EPS = Decimal("0.00002224")
P51_MARGIN = Decimal(1) / Decimal(36260) - EPS


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
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


def proof_steps() -> list[dict[str, str]]:
    """给出 psi 与 psi0 端点转换证明。"""
    return [
        {
            "step": "table_target",
            "claim": "Table 6.3 b=28 行是普通 Chebyshev 函数 psi 的 epsilon_psi 表值。",
            "reason": "arXiv 源文件定义 psi(x)=sum_{p^alpha<=x} log p，表头写 epsilon_psi。",
        },
        {
            "step": "internal_formula_target",
            "claim": "仓库内部精确公式闭合的是 psi_0 半权端点版本。",
            "reason": "internal psi0 Perron 证书声明 psi_0(x)=sum_{n<x} Lambda(n)+1/2 Lambda(x) if x is an integer。",
        },
        {
            "step": "endpoint_difference",
            "claim": "对任意 x>1，0 <= psi(x)-psi_0(x) <= (1/2)log x。",
            "reason": "只有当 x 恰为素数幂跳点时出现半个 Lambda(x)，且 Lambda(x)<=log x。",
        },
        {
            "step": "high_tail_relative_bound",
            "claim": "对 x>=e^28，(psi(x)-psi_0(x))/x <= 14/e^28。",
            "reason": "(log x)/(2x) 在 x>e 上递减，故最大点为 x=e^28。",
        },
        {
            "step": "budget_registration",
            "claim": "该端点税只关闭口径转换；必须在后续 b=28 预算中显式扣除。",
            "reason": "端点税远小于高尾拼接余量，但不能凭空消失。",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 psi/psi0 端点口径转换证书。"""
    previous = load_json(PREVIOUS)
    internal = load_json(INTERNAL_PSI0)
    table63 = load_json(TABLE63)

    active = previous.get("next_direct_attack_target") == "IndependentTable63B28RegenerationFromExplicitFormulaLedger"
    table_targets_psi = table63.get("table63_machine_rows", [{}])[0].get("function") == "psi"
    internal_psi0_closed = internal.get("internal_psi0_exact_formula_closed") is True
    endpoint_tax_fits_p51_margin = ENDPOINT_TAX_REL_AT_EXP28 < P51_MARGIN
    endpoint_conversion_closed = active and table_targets_psi and internal_psi0_closed

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            previous.get("counterexample_assumption_only") is True
            and previous.get("row_column_unconditional_closed") is False,
            True,
            "本步只统一 Table 6.3 重建中的函数端点口径，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "IndependentRegenerationGateActive",
            active,
            True,
            "上一证书已把自足路线压到独立重建 Table 6.3 b=28。",
            "IndependentTable63B28RegenerationFromExplicitFormulaLedger",
        ),
        row(
            "Table63TargetsOrdinaryPsi",
            table_targets_psi,
            False,
            "机器表行与 arXiv 表头均指向普通 psi，而不是 psi_0。",
            TARGET,
        ),
        row(
            "InternalPsi0FormulaAvailable",
            internal_psi0_closed,
            True,
            "仓库内部 psi_0 精确显式公式已闭合，可作为重建公式起点。",
            "InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost",
        ),
        row(
            "EndpointJumpTaxBoundClosed",
            endpoint_conversion_closed,
            True,
            "psi 与 psi_0 的差只可能是一个跳点的半个 Lambda(x)，故相对税在 x>=e^28 上至多 14/e^28。",
            "endpoint tax registered",
        ),
        row(
            "EndpointTaxFitsHighTailMargin",
            endpoint_tax_fits_p51_margin,
            True,
            "端点税小于 P5.1 高尾拼接余量，但后续生成 2.224E-5 时仍需登记预算。",
            BUDGET,
        ),
        row(
            TARGET,
            endpoint_conversion_closed,
            True,
            "Table 6.3 的普通 psi 口径可由内部 psi_0 公式无损转换，代价为显式端点税。",
            "closed with endpoint tax",
        ),
        row(
            "IndependentRegenerationStillOpen",
            False,
            False,
            "端点口径闭合不等于重建表值；仍缺核/截断、有限零点高度、零点自由尾项、预算、舍入和 hash。",
            f"{KERNEL} AND {FINITE_RH} AND {ZERO_TAIL} AND {BUDGET} AND {ROUNDING} AND {HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "psi/psi0 端点口径转换不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_table63_b28_psi_endpoint_convention_router",
        "status": "table63_b28_psi_vs_psi0_endpoint_convention_closed_endpoint_tax_registered",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "table63_targets_ordinary_psi": table_targets_psi,
        "internal_psi0_formula_available": internal_psi0_closed,
        "table63_b28_psi_vs_psi0_endpoint_convention_closed": endpoint_conversion_closed,
        "endpoint_tax_fits_high_tail_margin": endpoint_tax_fits_p51_margin,
        "independent_table63_b28_regeneration_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "arithmetic": {
            "endpoint_tax_relative_bound_14_over_e28": str(ENDPOINT_TAX_REL_AT_EXP28),
            "epsilon_psi_28": str(EPS),
            "p51_high_tail_margin": str(P51_MARGIN),
            "endpoint_tax_to_margin_ratio": str(ENDPOINT_TAX_REL_AT_EXP28 / P51_MARGIN),
        },
        "proof_steps": proof_steps(),
        "replacement_self_contained": {
            TARGET: "InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost AND EndpointJumpTaxBoundClosed14OverE28",
            "IndependentTable63B28RegenerationFromExplicitFormulaLedger": (
                f"{TARGET} AND {KERNEL} AND {FINITE_RH} AND {ZERO_TAIL} AND {BUDGET} AND {ROUNDING} AND {HASH}"
            ),
        },
        "next_direct_attack_target": KERNEL,
        "parallel_attack_targets": [FINITE_RH, ZERO_TAIL, BUDGET, ROUNDING, HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Table 6.3 的 b=28 表行使用普通 `psi`，仓库内部闭合的是半权端点 `psi_0`。"
            "二者差异只可能来自跳点半权，满足 `0<=psi(x)-psi_0(x)<=0.5 log x`；"
            "因此在 `x>=e^28` 上相对端点税至多 `14/e^28`。该原子闭合，且端点税远小于高尾拼接余量，"
            "但仍必须进入后续表值预算。下一最窄点是 Table 6.3 b=28 的核/截断/平滑规则。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Table 6.3 b=28 psi/psi0 端点口径转换证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"table63_b28_psi_vs_psi0_endpoint_convention_closed={fmt_bool(result['table63_b28_psi_vs_psi0_endpoint_convention_closed'])}",
        f"endpoint_tax_fits_high_tail_margin={fmt_bool(result['endpoint_tax_fits_high_tail_margin'])}",
        f"independent_table63_b28_regeneration_closed={fmt_bool(result['independent_table63_b28_regeneration_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 数值边界",
        "",
        "| field | value |",
        "| --- | ---: |",
    ]
    for key, value in result["arithmetic"].items():
        lines.append(f"| `{table_cell(key)}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 2. 证明步骤",
            "",
            "| step | claim | reason |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["proof_steps"]:
        lines.append(f"| `{table_cell(item['step'])}` | {table_cell(item['claim'])} | {table_cell(item['reason'])} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        "table63_b28_psi_vs_psi0_endpoint_convention_closed="
        f"{fmt_bool(result['table63_b28_psi_vs_psi0_endpoint_convention_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
