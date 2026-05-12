#!/usr/bin/env python3
"""生成 strict Table 6.3 b=28 生成/舍入输入基审计证书。

用法示例：
  python3 experiments/prime_matrix_strict_table63_b28_generation_rounding_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table63-b28-generation-rounding-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 50

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-table63-b28-generation-rounding-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table63-b28-generation-rounding-router.md"

TABLE63 = DOCS / "prime-matrix-strict-machine-readable-dusart-table63-router.json"
BUDGET = DOCS / "prime-matrix-strict-psi-epsilon-budget-partition-router.json"
CONVENTION = DOCS / "prime-matrix-strict-same-explicit-formula-convention-router.json"
TRANSITION = DOCS / "prime-matrix-strict-finite-verified-zero-tail-transition-router.json"
LARGE_RH = DOCS / "prime-matrix-strict-large-finite-rh-verification-router.json"
ZERO_FREE = DOCS / "prime-matrix-strict-explicit-zero-free-table-tail-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"

SOURCE_FILES = [TABLE63, BUDGET, CONVENTION, TRANSITION, LARGE_RH, ZERO_FREE, CLAIM_STATUS]

TARGET = "Table63B28GeneratedUpperRoundingCertificateFromVerifiedZeroInputsLedger"
ZERO_BINDING = "Table63B28ZeroInputToExplicitFormulaBindingLedger"
FORMULA = "Table63B28SameExplicitFormulaConventionLedger"
FINITE_RH = "Table63B28FiniteRHHeightEndpointAndZeroBlockLedger"
ZERO_TAIL = "Table63B28ZeroFreeTailConstantsAndStartHeightLedger"
NO_GAP = "Table63B28FiniteToTailNoGapNoOverlapLedger"
BUDGET_LEDGER = "Table63B28PsiEpsilonBudgetPartitionLedger"
ROUNDING = "Table63B28DirectedUpperRoundingAndIntervalPropagationLedger"
HASH = "Table63B28ReproducibleComputationHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

EPS = Decimal("0.00002224")
TARGET_RELATIVE = Decimal(1) / Decimal(36260)


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


def input_basis() -> list[dict[str, str]]:
    """列出 b=28 自足生成证明不可缺少的输入基。"""
    return [
        {
            "basis": FORMULA,
            "role": "固定 psi/psi0、核函数、截断、素数幂和平凡零点口径",
            "why_needed": "没有同一显式公式，finite-zero、zero-free tail 和表值 cap 不能相加比较。",
        },
        {
            "basis": FINITE_RH,
            "role": "给出表算法实际调用的有限 RH 高度端点和零点块证书",
            "why_needed": "Gourdon 外部来源必须转换成同一表公式的高度变量。",
        },
        {
            "basis": ZERO_TAIL,
            "role": "给出零点自由区尾项常数、起点和适用区间",
            "why_needed": "Kadiri 外部常数必须进入同一表尾项预算。",
        },
        {
            "basis": NO_GAP,
            "role": "证明有限零点块、尾项和截断高度无缺口、无重复扣费",
            "why_needed": "否则同一零点区域可能漏算或双算。",
        },
        {
            "basis": BUDGET_LEDGER,
            "role": "证明所有误差项相加小于 2.224e-5",
            "why_needed": "表行的核心是上界生成，不是数值摘录。",
        },
        {
            "basis": ROUNDING,
            "role": "证明输出 2.224E-5 是外向上舍入并覆盖整段 x>=exp(28)",
            "why_needed": "舍入方向错误会把表值从上界变成未经认证的近似。",
        },
        {
            "basis": HASH,
            "role": "给出输入、程序、版本和输出表的可复现 hash",
            "why_needed": "没有 hash 就无法区分作者侧复算与文字引用。",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 b=28 生成/舍入审计证书。"""
    table63 = load_json(TABLE63)
    budget = load_json(BUDGET)
    convention = load_json(CONVENTION)
    transition = load_json(TRANSITION)
    large_rh = load_json(LARGE_RH)
    zero_free = load_json(ZERO_FREE)

    active = table63.get("next_direct_attack_target") == TARGET
    external_row_usable = table63.get("machine_readable_table63_external_row_usable") is True
    cap_fixed = budget.get("budget_caps_arithmetic_fixed") is True
    high_tail_gap_factor = Decimal(str(budget.get("coarse_template_gap_factors", {}).get("high_tail_b28", "0")))
    transition_interface_closed = transition.get("common_variable_interface_taxonomy_closed") is True
    same_formula_open = convention.get("same_explicit_formula_convention_closed") is False
    large_rh_external = large_rh.get("external_gourdon_conditional_lane_available") is True
    zero_free_external = zero_free.get("kadiri_external_source_identified") is True
    p51_margin = TARGET_RELATIVE - EPS

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            table63.get("counterexample_assumption_only") is True
            and table63.get("row_column_unconditional_closed") is False,
            True,
            "本步仍只审计假设反例链可调用的解析表输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "GenerationRoundingGateActive",
            active,
            True,
            "上一证书把下一最窄点精确压到 b=28 表值的生成与外向舍入证书。",
            TARGET,
        ),
        row(
            "ExternalB28RowAlreadyUsable",
            external_row_usable,
            False,
            "外部路线中 b=28 表行可直接使用，且高尾拼接算术已匹配。",
            "external Table 6.3 accepted",
        ),
        row(
            "B28CapAndP51MarginFixed",
            cap_fixed and p51_margin > 0,
            True,
            "b=28 cap 为 2.224e-5，接入 1/36260 的数值余量固定。",
            f"margin={p51_margin}",
        ),
        row(
            "CoarseInternalContourRejectedForB28",
            high_tail_gap_factor > Decimal("1e12"),
            True,
            "现有 C=1280,C_Z=65536 内部粗 contour 距 b=28 表值约 10^12 倍，不能生成 Table 6.3。",
            f"gap_factor={high_tail_gap_factor}",
        ),
        row(
            "CommonVariableInterfaceKnown",
            transition_interface_closed,
            True,
            "x 区间、高度端点、零点自由阈值、显式公式、预算和 hash 六类共同变量已被分类。",
            "classification closed, values open",
        ),
        row(
            "ExternalFiniteRHAndZeroFreeSourcesAvailable",
            large_rh_external and zero_free_external,
            False,
            "Gourdon 有限零点和 Kadiri 零点自由区可作为外部来源，但尚未绑定到 b=28 表算法。",
            f"{FINITE_RH} AND {ZERO_TAIL}",
        ),
        row(
            FORMULA,
            False,
            False,
            "同一显式公式口径仍开放：当前内部 Perron 粗链自洽不等于 Dusart Table 6.3 的表算法口径。",
            "PsiVsPsi0EndpointJumpConventionLedger AND TableTruncationSmoothingAndKernelConventionLedger",
        ),
        row(
            ZERO_BINDING,
            False,
            False,
            "还没有证明有限零点块和零点自由尾项按同一显式公式进入 b=28 表行。",
            f"{FORMULA} AND {FINITE_RH} AND {ZERO_TAIL} AND {NO_GAP}",
        ),
        row(
            BUDGET_LEDGER,
            False,
            False,
            "还没有可复算数值账本证明 finite-zero、zero-free tail、素数幂、平凡零点和端点误差之和小于 2.224e-5。",
            f"{ZERO_BINDING} AND PrimePowerAndTrivialZeroCorrectionBudgetLedger",
        ),
        row(
            ROUNDING,
            False,
            False,
            "还缺外向上舍入和高尾区间传播日志，证明输出的 2.224E-5 是认证上界而非近似值。",
            HASH,
        ),
        row(
            TARGET,
            False,
            False,
            "b=28 生成/舍入证书尚未作者侧闭合；当前只关闭外部表行和所需输入基定位。",
            f"{ZERO_BINDING} AND {BUDGET_LEDGER} AND {ROUNDING} AND {HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "b=28 表值生成审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_table63_b28_generation_rounding_router",
        "status": "table63_b28_generation_rounding_reduced_to_zero_input_binding_budget_rounding_hash",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "external_b28_row_usable": external_row_usable,
        "b28_cap_and_p51_margin_fixed": cap_fixed and p51_margin > 0,
        "coarse_internal_contour_rejected_for_b28": high_tail_gap_factor > Decimal("1e12"),
        "common_variable_interface_closed": transition_interface_closed,
        "external_finite_rh_and_zero_free_sources_available": large_rh_external and zero_free_external,
        "table63_b28_generation_rounding_closed": False,
        "table63_b28_zero_input_binding_closed": False,
        "table63_b28_budget_partition_closed": False,
        "table63_b28_directed_rounding_closed": False,
        "table63_b28_reproducible_hash_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "input_basis": input_basis(),
        "arithmetic": {
            "epsilon_psi_28": str(EPS),
            "target_1_over_36260": str(TARGET_RELATIVE),
            "p51_high_tail_margin": str(p51_margin),
            "coarse_template_gap_factor_high_tail_b28": str(high_tail_gap_factor),
        },
        "replacement_self_contained": {
            TARGET: f"{ZERO_BINDING} AND {BUDGET_LEDGER} AND {ROUNDING} AND {HASH}",
            ZERO_BINDING: f"{FORMULA} AND {FINITE_RH} AND {ZERO_TAIL} AND {NO_GAP}",
            BUDGET_LEDGER: f"{ZERO_BINDING} AND PrimePowerAndTrivialZeroCorrectionBudgetLedger",
        },
        "next_direct_attack_target": ZERO_BINDING,
        "parallel_attack_targets": [FORMULA, FINITE_RH, ZERO_TAIL, NO_GAP, BUDGET_LEDGER, ROUNDING, HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`Table63B28GeneratedUpperRounding...` 不能由现有内部粗 contour 生成："
            "高尾粗模板距离 `2.224e-5` 表值约 `2.78e12` 倍。"
            "外部 Table 6.3 行已经可用，但作者侧自足生成必须补齐同一显式公式口径、"
            "有限零点高度端点、零点自由尾项起点、无缺口拼接、预算分摊、外向舍入和 hash。"
            "下一最窄点是把有限零点/零点自由输入绑定到同一 b=28 显式公式。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Table 6.3 b=28 生成/舍入输入基审计证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"external_b28_row_usable={fmt_bool(result['external_b28_row_usable'])}",
        f"b28_cap_and_p51_margin_fixed={fmt_bool(result['b28_cap_and_p51_margin_fixed'])}",
        f"coarse_internal_contour_rejected_for_b28={fmt_bool(result['coarse_internal_contour_rejected_for_b28'])}",
        f"table63_b28_generation_rounding_closed={fmt_bool(result['table63_b28_generation_rounding_closed'])}",
        f"table63_b28_zero_input_binding_closed={fmt_bool(result['table63_b28_zero_input_binding_closed'])}",
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
            "## 2. 输入基",
            "",
            "| basis | role | why needed |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["input_basis"]:
        lines.append(
            f"| `{table_cell(item['basis'])}` | {table_cell(item['role'])} | {table_cell(item['why_needed'])} |"
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
    print(f"table63_b28_generation_rounding_closed={fmt_bool(result['table63_b28_generation_rounding_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
