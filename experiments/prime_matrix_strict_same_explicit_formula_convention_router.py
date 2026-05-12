#!/usr/bin/env python3
"""生成 strict 同一显式公式口径路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_same_explicit_formula_convention_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-same-explicit-formula-convention-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-same-explicit-formula-convention-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-same-explicit-formula-convention-router.md"

BUDGET = MONOGRAPH / "prime-matrix-strict-psi-epsilon-budget-partition-router.json"
GENERATOR = MONOGRAPH / "prime-matrix-strict-epsilon-table-generator-audit-router.json"
PERRON = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-final-sync-router.json"
ZERO_SUM = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
TRIVIAL_TAIL = MONOGRAPH / "prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.json"
INTERNAL_PSI0 = MONOGRAPH / "prime-matrix-b3-internal-psi0-perron-formula-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [BUDGET, GENERATOR, PERRON, ZERO_SUM, TRIVIAL_TAIL, INTERNAL_PSI0, CLAIM_STATUS]

TARGET = "SameExplicitFormulaConventionLedger"
TABLE_ALGORITHM = "PsiEpsilonTableComputationAlgorithmLedger"
PSI_VS_PSI0 = "PsiVsPsi0EndpointJumpConventionLedger"
TRUNCATION = "TableTruncationSmoothingAndKernelConventionLedger"
ZERO_SPLIT = "FiniteZeroWindowAndZeroFreeTailSplitConventionLedger"
PRIME_POWER = "PrimePowerThetaPsiTransferSameTableConventionLedger"
INTERVAL = "PsiEpsilonIntervalPropagationAndMonotonicityLedger"
ROUNDING_HASH = "ReproduciblePsiEpsilonTableComputationHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def convention_matrix() -> list[dict[str, str]]:
    """列出必须同口径的公式字段。"""
    return [
        {
            "field": "base_function",
            "internal_status": "psi_0 exact formula closed",
            "table_match_needed": "prove table uses psi, psi_0, or a converted endpoint convention with no hidden jump",
            "ledger": PSI_VS_PSI0,
        },
        {
            "field": "kernel_and_truncation",
            "internal_status": "finite-T unsmoothed Perron closed for coarse B3 chain",
            "table_match_needed": "identify the epsilon table kernel, height choice, smoothing and truncation rule",
            "ledger": TRUNCATION,
        },
        {
            "field": "zero_split",
            "internal_status": "C=1280,C_Z=65536 zero-sum envelope closed but coarse",
            "table_match_needed": "match finite verified-zero block and zero-free tail split used by the table",
            "ledger": ZERO_SPLIT,
        },
        {
            "field": "prime_power_and_theta_transfer",
            "internal_status": "prime-power transfer closed for theta/Perron route",
            "table_match_needed": "prove the same transfer direction and correction terms are used in psi epsilon table",
            "ledger": PRIME_POWER,
        },
        {
            "field": "interval_propagation",
            "internal_status": "not supplied by current Perron certificates",
            "table_match_needed": "show how b-grid or finite nodes propagate to all x in the high and middle ranges",
            "ledger": INTERVAL,
        },
        {
            "field": "rounding_output",
            "internal_status": "not supplied by current Perron certificates",
            "table_match_needed": "directed rounding and reproducible output hash for 0.00002224 and 1.00002841",
            "ledger": ROUNDING_HASH,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造同一显式公式口径证书。"""
    budget = load_json(BUDGET)
    generator = load_json(GENERATOR)
    perron = load_json(PERRON)
    zero_sum = load_json(ZERO_SUM)
    trivial_tail = load_json(TRIVIAL_TAIL)
    internal_psi0 = load_json(INTERNAL_PSI0)
    active = budget.get("next_direct_attack_target") == TARGET
    internal_formula_chain_ready = (
        perron.get("unsmoothed_perron_strict_self_contained_closed") is True
        and zero_sum.get("zero_sum_contour_budget_self_contained_closed") is True
        and trivial_tail.get("trivial_tail_prime_power_budget_self_contained_closed") is True
        and internal_psi0.get("internal_psi0_exact_formula_closed") is True
    )
    table_algorithm_open = generator.get("table_computation_algorithm_closed") is False
    interval_open = generator.get("interval_propagation_closed") is False
    hash_open = generator.get("reproducible_table_hash_closed") is False
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            budget.get("counterexample_assumption_only") is True
            and budget.get("row_column_unconditional_closed") is False,
            True,
            "本步只统一假设反例链可调用的 psi 表显式公式口径，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "SameExplicitFormulaConventionGateActive",
            active,
            True,
            "预算分摊证书已把下一最窄点压到同一显式公式口径。",
            TARGET,
        ),
        row(
            "InternalPerronConventionLocallyClosed",
            internal_formula_chain_ready,
            True,
            "仓库内部 B3/Perron 链已有 psi_0 精确公式、非平滑 Perron、零点和、平凡尾项与素数幂 convention。",
            "this is local to the coarse internal Perron route",
        ),
        row(
            "LocalConventionDoesNotImplyDusartTableConvention",
            internal_formula_chain_ready and table_algorithm_open,
            True,
            "内部 Perron convention 只说明粗链自洽；它没有给出 Schoenfeld/Dusart epsilon 表实际生成算法。",
            TABLE_ALGORITHM,
        ),
        row(
            PSI_VS_PSI0,
            False,
            False,
            "需要证明表值使用的 psi/psi_0 端点半权和跳点 convention 与内部公式可无损转换。",
            TABLE_ALGORITHM,
        ),
        row(
            TRUNCATION,
            False,
            False,
            "需要表生成器的截断高度、平滑核或非平滑核、边界避零规则和误差项定义。",
            TABLE_ALGORITHM,
        ),
        row(
            ZERO_SPLIT,
            False,
            False,
            "需要 finite verified-zero 主块与 zero-free tail 在表公式中的分界和不重复计费规则。",
            TABLE_ALGORITHM,
        ),
        row(
            PRIME_POWER,
            False,
            False,
            "需要素数幂、theta/psi 转换和常数项在表公式中的方向与符号。",
            TABLE_ALGORITHM,
        ),
        row(
            INTERVAL,
            False,
            False,
            "需要证明离散表节点如何传播到整段 x 区间，含单调性、跳点和端点。",
            INTERVAL,
        ),
        row(
            ROUNDING_HASH,
            False,
            False,
            "需要可复现计算 hash 与外向舍入证书，尤其要控制中段 4.46e-11 余量。",
            ROUNDING_HASH,
        ),
        row(
            TARGET,
            False,
            False,
            "当前只能确认内部粗 Perron 公式自洽，不能确认它与 Schoenfeld/Dusart epsilon 表同口径。",
            f"{TABLE_ALGORITHM} AND {PSI_VS_PSI0} AND {TRUNCATION} AND {ZERO_SPLIT} AND {PRIME_POWER} AND {INTERVAL} AND {ROUNDING_HASH}",
        ),
        row(
            "GeneratorOpenItemsAgreeWithConventionGap",
            table_algorithm_open and interval_open and hash_open,
            True,
            "epsilon 表生成器审计中的算法、区间传播和 hash 开放项正是 convention 未闭合的来源。",
            f"{TABLE_ALGORITHM} AND {INTERVAL} AND {ROUNDING_HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "同一显式公式口径审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_same_explicit_formula_convention_router",
        "status": "same_explicit_formula_convention_reduced_to_table_algorithm_interval_hash_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "internal_perron_convention_locally_closed": internal_formula_chain_ready,
        "local_convention_does_not_imply_dusart_table_convention": internal_formula_chain_ready and table_algorithm_open,
        "same_explicit_formula_convention_closed": False,
        "psi_vs_psi0_endpoint_jump_convention_closed": False,
        "table_truncation_smoothing_kernel_convention_closed": False,
        "finite_zero_tail_split_convention_closed": False,
        "prime_power_theta_psi_transfer_same_table_convention_closed": False,
        "interval_propagation_convention_closed": False,
        "rounding_hash_convention_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "convention_matrix": convention_matrix(),
        "replacement_self_contained": {
            TARGET: (
                f"{TABLE_ALGORITHM} AND {PSI_VS_PSI0} AND {TRUNCATION} AND {ZERO_SPLIT} AND "
                f"{PRIME_POWER} AND {INTERVAL} AND {ROUNDING_HASH}"
            ),
            TABLE_ALGORITHM: "must specify the actual Schoenfeld/Dusart epsilon-table explicit formula before budgets can be added",
        },
        "next_direct_attack_target": TABLE_ALGORITHM,
        "parallel_attack_targets": [PSI_VS_PSI0, TRUNCATION, ZERO_SPLIT, PRIME_POWER, INTERVAL, ROUNDING_HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "同一显式公式口径不能由现有内部 Perron 粗链自动获得。仓库内部确实已经有 psi_0 精确公式、"
            "非平滑 Perron、零点和与平凡尾项的自洽 convention；但 Schoenfeld/Dusart epsilon 表还缺实际生成算法、"
            "区间传播规则和可复现 hash。因此本步把 convention 缺口压回表生成算法，而不是把粗链预算直接相加。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 同一显式公式口径路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"internal_perron_convention_locally_closed={fmt_bool(result['internal_perron_convention_locally_closed'])}",
        f"local_convention_does_not_imply_dusart_table_convention={fmt_bool(result['local_convention_does_not_imply_dusart_table_convention'])}",
        f"same_explicit_formula_convention_closed={fmt_bool(result['same_explicit_formula_convention_closed'])}",
        f"psi_vs_psi0_endpoint_jump_convention_closed={fmt_bool(result['psi_vs_psi0_endpoint_jump_convention_closed'])}",
        f"table_truncation_smoothing_kernel_convention_closed={fmt_bool(result['table_truncation_smoothing_kernel_convention_closed'])}",
        f"finite_zero_tail_split_convention_closed={fmt_bool(result['finite_zero_tail_split_convention_closed'])}",
        f"prime_power_theta_psi_transfer_same_table_convention_closed={fmt_bool(result['prime_power_theta_psi_transfer_same_table_convention_closed'])}",
        f"interval_propagation_convention_closed={fmt_bool(result['interval_propagation_convention_closed'])}",
        f"rounding_hash_convention_closed={fmt_bool(result['rounding_hash_convention_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. convention 对齐矩阵",
        "",
        "| field | internal_status | table_match_needed | ledger |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["convention_matrix"]:
        lines.append(
            "| `{field}` | {internal_status} | {needed} | `{ledger}` |".format(
                field=table_cell(item["field"]),
                internal_status=table_cell(item["internal_status"]),
                needed=table_cell(item["table_match_needed"]),
                ledger=table_cell(item["ledger"]),
            )
        )
    lines.extend(["", "## 2. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 3. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
