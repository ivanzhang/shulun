#!/usr/bin/env python3
"""生成 strict psi epsilon 预算分摊路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_psi_epsilon_budget_partition_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-psi-epsilon-budget-partition-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 60

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-psi-epsilon-budget-partition-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-psi-epsilon-budget-partition-router.md"

TRANSITION = MONOGRAPH / "prime-matrix-strict-finite-verified-zero-tail-transition-router.json"
DUSART_SPLICE = MONOGRAPH / "prime-matrix-strict-dusart-analytic-kernel-threshold-router.json"
PSI_PRESSURE = MONOGRAPH / "prime-matrix-strict-psi-epsilon-table-internalization-router.json"
GENERATOR = MONOGRAPH / "prime-matrix-strict-epsilon-table-generator-audit-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [TRANSITION, DUSART_SPLICE, PSI_PRESSURE, GENERATOR, CLAIM_STATUS]

TARGET = "PsiEpsilonBudgetPartitionLedger"
CONVENTION = "SameExplicitFormulaConventionLedger"
FINITE_ZERO_BUDGET = "FiniteVerifiedZeroMainBlockNumericalBudgetLedger"
ZERO_FREE_TAIL_BUDGET = "ZeroFreeTailNumericalBudgetLedger"
PRIME_POWER_BUDGET = "PrimePowerAndTrivialZeroCorrectionBudgetLedger"
ROUNDING_BUDGET = "DirectedRoundingAndIntervalPropagationBudgetLedger"
HASH_INTERFACE = "TableGeneratorHashInterfaceLedger"
FINITE_ENDPOINT = "FiniteRHHeightEndpointLedger"
TAIL_START = "ZeroFreeTailStartHeightLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TARGET_REL = Decimal(1) / Decimal(36_260)
EPS_HIGH = Decimal("0.00002224")
EPS_MIDDLE = Decimal("0.00002841")
GAP_COEFF = Decimal("0.9999")
EXP_NEG_14 = Decimal(-14).exp()
MIDDLE_GAP = GAP_COEFF * EXP_NEG_14
MIDDLE_THETA_RESULT = EPS_MIDDLE - MIDDLE_GAP
HIGH_THETA_SLACK = TARGET_REL - EPS_HIGH
MIDDLE_THETA_SLACK = TARGET_REL - MIDDLE_THETA_RESULT


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_dec(value: Decimal) -> str:
    """稳定输出 Decimal 小数。"""
    return format(value, ".18e")


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


def budget_caps() -> list[dict[str, str]]:
    """列出必须同时满足的预算上限。"""
    return [
        {
            "site": "high tail x>=e^28",
            "cap_type": "psi table relative cap",
            "cap": fmt_dec(EPS_HIGH),
            "derived_theta_slack": fmt_dec(HIGH_THETA_SLACK),
            "consequence": "finite-zero + zero-free-tail + corrections + rounding must fit below eps_psi(28)",
        },
        {
            "site": "middle strip 8e11<=x<=e^28",
            "cap_type": "psi table relative cap",
            "cap": fmt_dec(EPS_MIDDLE),
            "derived_theta_slack": fmt_dec(MIDDLE_THETA_SLACK),
            "consequence": "after psi-theta gap, unbudgeted error must be < middle theta slack",
        },
        {
            "site": "middle theta splice",
            "cap_type": "unallocated splice slack",
            "cap": fmt_dec(MIDDLE_THETA_SLACK),
            "derived_theta_slack": fmt_dec(MIDDLE_THETA_SLACK),
            "consequence": "this is only about 4.46e-11, so no hidden rounding or convention error is tolerable",
        },
    ]


def pressure_factor(pressure: dict[str, Any], site_prefix: str) -> float | None:
    """从既有压力证书读取粗模板失败倍数。"""
    for item in pressure.get("pressure_rows", []):
        if str(item.get("site", "")).startswith(site_prefix):
            value = item.get("gap_factor")
            return float(value) if value is not None else None
    return None


def build_result() -> dict[str, Any]:
    """构造 psi epsilon 预算分摊证书。"""
    transition = load_json(TRANSITION)
    splice = load_json(DUSART_SPLICE)
    pressure = load_json(PSI_PRESSURE)
    generator = load_json(GENERATOR)
    active = transition.get("next_direct_attack_target") == TARGET
    arithmetic_ready = (
        splice.get("dusart_analytic_kernel_threshold_arithmetic_splice_closed") is True
        and HIGH_THETA_SLACK > 0
        and MIDDLE_THETA_SLACK > 0
    )
    table_values_extracted = generator.get("epsilon_table_statement_extraction_closed") is True
    coarse_template_rejected = pressure.get("current_c1280_c65536_template_beats_psi_epsilon_targets") is False
    high_gap = pressure_factor(pressure, "high tail")
    middle_gap = pressure_factor(pressure, "middle left")
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            transition.get("counterexample_assumption_only") is True
            and transition.get("row_column_unconditional_closed") is False,
            True,
            "本步只审查假设反例链可调用的 psi 表预算，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "PsiEpsilonBudgetPartitionGateActive",
            active,
            True,
            "有限零点到尾项桥接证书已把下一最窄点压到 psi epsilon 预算分摊。",
            TARGET,
        ),
        row(
            "BudgetCapsArithmeticFixed",
            arithmetic_ready and table_values_extracted,
            True,
            "高尾 cap、中段 cap 与中段 theta 拼接余量已被精确固定，不能再用模糊常数吸收误差。",
            "budget caps fixed, component bounds still open",
        ),
        row(
            "MiddleSpliceTinySlackGuard",
            MIDDLE_THETA_SLACK > 0,
            True,
            "中段 theta 拼接余量约 4.46e-11；任何未登记舍入、尾项或公式差异都会破坏拼接。",
            f"{CONVENTION} AND {ROUNDING_BUDGET}",
        ),
        row(
            "CurrentCoarseContourRejectedForBudget",
            coarse_template_rejected,
            True,
            f"既有 C=1280,C_Z=65536 模板失败：高尾约 {high_gap:.3e} 倍，中段约 {middle_gap:.3e} 倍。",
            f"{FINITE_ZERO_BUDGET} AND {ZERO_FREE_TAIL_BUDGET}",
        ),
        row(
            CONVENTION,
            False,
            False,
            "预算分摊前必须先固定同一显式公式、截断、平滑、prime-power 与 zero-free tail 口径。",
            "without this, component budgets are not comparable",
        ),
        row(
            FINITE_ZERO_BUDGET,
            False,
            False,
            "需要有限 verified-zero 主块在 e^28 与 8e11 两个端点及区间传播中的数值上界。",
            FINITE_ENDPOINT,
        ),
        row(
            ZERO_FREE_TAIL_BUDGET,
            False,
            False,
            "需要零点自由尾项在同一表公式中的数值上界，并证明不与 finite-zero 主块重复扣费。",
            TAIL_START,
        ),
        row(
            PRIME_POWER_BUDGET,
            False,
            False,
            "需要素数幂、平凡零点和端点修正在 psi 表口径下的剩余预算。",
            CONVENTION,
        ),
        row(
            ROUNDING_BUDGET,
            False,
            False,
            "需要外向舍入和区间传播误差严格小于中段极薄余量。",
            HASH_INTERFACE,
        ),
        row(
            TARGET,
            False,
            False,
            "当前只固定预算上限和失败模板；尚未给出各组件相加小于 cap 的可复算账本。",
            f"{CONVENTION} AND {FINITE_ZERO_BUDGET} AND {ZERO_FREE_TAIL_BUDGET} AND {PRIME_POWER_BUDGET} AND {ROUNDING_BUDGET}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "psi epsilon 预算分摊不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_psi_epsilon_budget_partition_router",
        "status": "psi_epsilon_budget_caps_fixed_component_partition_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "budget_caps_arithmetic_fixed": arithmetic_ready and table_values_extracted,
        "middle_splice_tiny_slack_guard_closed": MIDDLE_THETA_SLACK > 0,
        "current_coarse_contour_rejected_for_budget": coarse_template_rejected,
        "psi_epsilon_budget_partition_closed": False,
        "same_explicit_formula_convention_closed": False,
        "finite_verified_zero_main_block_budget_closed": False,
        "zero_free_tail_numerical_budget_closed": False,
        "prime_power_and_trivial_zero_budget_closed": False,
        "directed_rounding_budget_closed": False,
        "table_generator_hash_interface_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "budget_caps": budget_caps(),
        "coarse_template_gap_factors": {
            "high_tail_b28": high_gap,
            "middle_left_8e11": middle_gap,
        },
        "replacement_self_contained": {
            TARGET: (
                f"{CONVENTION} AND {FINITE_ZERO_BUDGET} AND {ZERO_FREE_TAIL_BUDGET} AND "
                f"{PRIME_POWER_BUDGET} AND {ROUNDING_BUDGET} AND {HASH_INTERFACE}"
            ),
            CONVENTION: "must be closed before numerical component budgets can be added",
        },
        "next_direct_attack_target": CONVENTION,
        "parallel_attack_targets": [FINITE_ZERO_BUDGET, ZERO_FREE_TAIL_BUDGET, ROUNDING_BUDGET, HASH_INTERFACE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "psi epsilon 预算分摊的上限已经固定：高尾表值 cap 为 2.224e-5，中段表值 cap 为 2.841e-5，"
            "但中段接入 theta(x)-x<x/36260 后只剩约 4.46e-11 的未分配余量。"
            "因此不能再用粗 contour 或未登记舍入误差含混通过；必须先固定同一显式公式口径，"
            "再逐项给出 finite-zero 主块、zero-free tail、修正项和舍入 hash 的数值账本。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict psi epsilon 预算分摊路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"budget_caps_arithmetic_fixed={fmt_bool(result['budget_caps_arithmetic_fixed'])}",
        f"middle_splice_tiny_slack_guard_closed={fmt_bool(result['middle_splice_tiny_slack_guard_closed'])}",
        f"current_coarse_contour_rejected_for_budget={fmt_bool(result['current_coarse_contour_rejected_for_budget'])}",
        f"psi_epsilon_budget_partition_closed={fmt_bool(result['psi_epsilon_budget_partition_closed'])}",
        f"same_explicit_formula_convention_closed={fmt_bool(result['same_explicit_formula_convention_closed'])}",
        f"finite_verified_zero_main_block_budget_closed={fmt_bool(result['finite_verified_zero_main_block_budget_closed'])}",
        f"zero_free_tail_numerical_budget_closed={fmt_bool(result['zero_free_tail_numerical_budget_closed'])}",
        f"directed_rounding_budget_closed={fmt_bool(result['directed_rounding_budget_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 预算上限",
        "",
        "| site | cap_type | cap | derived_theta_slack | consequence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["budget_caps"]:
        lines.append(
            "| {site} | {cap_type} | `{cap}` | `{derived}` | {consequence} |".format(
                site=table_cell(item["site"]),
                cap_type=table_cell(item["cap_type"]),
                cap=table_cell(item["cap"]),
                derived=table_cell(item["derived_theta_slack"]),
                consequence=table_cell(item["consequence"]),
            )
        )
    lines.extend(["", "## 2. 粗模板失败倍数", "", "```text"])
    for key, value in result["coarse_template_gap_factors"].items():
        lines.append(f"{key}={value:.12e}")
    lines.extend(["```", "", "## 3. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 4. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 5. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
