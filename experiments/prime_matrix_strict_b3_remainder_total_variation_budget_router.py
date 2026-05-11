#!/usr/bin/env python3
"""生成 strict B3 长度 P 余项总变差预算路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_b3_remainder_total_variation_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-b3-remainder-total-variation-budget-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.md",
    MONOGRAPH / "prime-matrix-b3-prime-word-stieltjes-integral-router.md",
    MONOGRAPH / "prime-matrix-b3-alternating-boundary-terminal-router.md",
    MONOGRAPH / "prime-matrix-b3-boundary-variation-multiplier-router.md",
    MONOGRAPH / "prime-matrix-b3-signed-delay-multiplier-anchor-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.md",
]

B3_TV = "B3RemainderTotalVariationBudgetForLengthP"
STIELTJES = "B3PrimeWordStieltjesIntegralUniformLedgerPGe100000"
BOUNDARY = "B3AlternatingBoundaryRemainderOnePercentLedger"
MERTENS = "B3PrimeHarmonicMertensUniformEnvelopePGe100000"
ANCHOR = "B3Anchor20000BoundaryVariationBudgetClosedAlpha043"
SELF_MERTENS = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
MAIN = "B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def reductions() -> list[dict[str, str]]:
    """列出 B3 TV 的压缩链。"""
    return [
        {
            "name": "raw_absolute_tv_rejected",
            "formula": "sum_d |lambda_d^-| is not the usable B3 remainder budget.",
            "status": "discipline_closed",
            "meaning": "裸绝对值会丢失 Rosser word 交错与边界面结构，不能作为自足闭合路径。",
        },
        {
            "name": "crt_remainder_as_boundary_functional",
            "formula": "A_d(x)-(P-1)/d is an endpoint/face functional after expanding lambda_d^- into prime words.",
            "status": "closed_reduction",
            "meaning": "长度 P 的 CRT 余项不是自由符号云，而由 Stieltjes 阶梯测度边界控制。",
        },
        {
            "name": "prime_word_stieltjes_import",
            "formula": "B3 prime-word sums equal iterated Stieltjes integrals over the B3 admissible polytope.",
            "status": "imported_closed",
            "meaning": "离散 prime-word 和到 Stieltjes 对象是精确重写，无解析误差。",
        },
        {
            "name": "alternating_boundary_split",
            "formula": f"{BOUNDARY} => {MERTENS} AND B3BoundaryVariationOnePercentTransferLedger.",
            "status": "imported_reduction",
            "meaning": "真正余项是 prime-harmonic/Mertens 一维包络经 B3 边界变差传播。",
        },
        {
            "name": "anchor20000_conditional_budget",
            "formula": "K_B3 <= 4e^gamma/s = 3.063444558943 and tail error <=0.001294124698.",
            "status": "conditional_external_closed",
            "meaning": "若接受外部 Mertens/Dusart 尾段，锚点 20000 后边界变差小于 1% f(s)。",
        },
        {
            "name": "self_contained_tail_boundary",
            "formula": f"Strict self-contained closure still needs {SELF_MERTENS}.",
            "status": "open_self_contained_input",
            "meaning": "完全自足版缺的是素数倒数 Mertens 尾段内联证明，不是新的零行几何命题。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本步仍只服务早期零行反例链中的 prefix 粗筛余输入，不使用真实零行缺席。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "NaiveAbsoluteTVBlocked",
            "closed": True,
            "proved": True,
            "meaning": "不能把 `sum |lambda_d^-|` 当作最终预算；必须保留 Rosser 交错和 B3 面结构。",
            "remaining": "Use signed Stieltjes boundary budget.",
        },
        {
            "gate": "SignedBoundaryReductionClosed",
            "closed": True,
            "proved": True,
            "meaning": "长度 P 余项被压成 B3 prime-word Stieltjes 边界余项，而非自由 CRT 误差云。",
            "remaining": BOUNDARY,
        },
        {
            "gate": "ConditionalExternalB3TVClosed",
            "closed": True,
            "proved": False,
            "meaning": "接受外部显式 Mertens/Dusart 尾段时，已有 20000 锚点和 delay-kernel BV 乘子可关闭 B3 TV。",
            "remaining": "External Mertens/Dusart acceptance, not strict self-contained proof.",
        },
        {
            "gate": "StrictSelfContainedB3TVProved",
            "closed": False,
            "proved": False,
            "meaning": "严格自足版仍需内联证明 prime-harmonic Mertens 尾段包络。",
            "remaining": SELF_MERTENS,
        },
        {
            "gate": "UnifiedTerminalBudgetUpdated",
            "closed": True,
            "proved": False,
            "meaning": "统一预算方程的 TV 项现在有条件外部闭合和严格自足剩余边界。",
            "remaining": f"{SELF_MERTENS} AND {FINITE_PREFIX} AND downstream terminal/cold-supply inputs",
        },
        {
            "gate": "DirectUnconditionalContradictionReached",
            "closed": False,
            "proved": False,
            "meaning": "B3 TV 的压缩尚未触发统一终端预算严格不等式。",
            "remaining": f"{MAIN} AND {FINITE_PREFIX} AND terminal/cold-supply inputs",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_b3_remainder_total_variation_budget_router",
        "status": "b3_remainder_tv_reduced_to_signed_stieltjes_boundary_conditional_external_closed_self_contained_mertens_tail_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "naive_absolute_tv_rejected": True,
        "crt_remainder_boundary_functional_reduction_closed": True,
        "prime_word_stieltjes_ledger_imported": True,
        "alternating_boundary_remainder_reduction_imported": True,
        "anchor20000_boundary_variation_budget_imported": True,
        "b3_tv_budget_conditional_external_closed": True,
        "b3_tv_budget_strict_self_contained_proved": False,
        "self_contained_mertens_tail_proved": False,
        "b3_remainder_total_variation_budget_proved": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SELF_MERTENS,
        "parallel_attack_targets": [FINITE_PREFIX, MAIN, "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse", "ColdCoreNonpersistentSupplyUpperBound"],
        "reductions": reductions(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "B3 长度 P 余项总变差缺口已经从裸 `sum |lambda_d^-|` 压缩到有符号 Stieltjes 边界预算。"
            "关键结构刚性是：CRT 余项不是可任意同号叠加的误差云；Rosser lower weights 展开为 B3 prime words 后，"
            "所有余项都落在 ordering/cap/floor/Rosser gate 的边界面上，并由 prime-harmonic 阶梯测度的 Mertens 尾段经 "
            "Buchstab delay kernel 传播。接受外部显式 Mertens/Dusart 尾段时，20000 锚点的 B3 边界变差预算已可关闭；"
            "严格自足线仍缺该 Mertens 尾段的内联证明。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict B3 长度 P 余项总变差预算路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"naive_absolute_tv_rejected={fmt_bool(result['naive_absolute_tv_rejected'])}",
        f"crt_remainder_boundary_functional_reduction_closed={fmt_bool(result['crt_remainder_boundary_functional_reduction_closed'])}",
        f"prime_word_stieltjes_ledger_imported={fmt_bool(result['prime_word_stieltjes_ledger_imported'])}",
        f"alternating_boundary_remainder_reduction_imported={fmt_bool(result['alternating_boundary_remainder_reduction_imported'])}",
        f"anchor20000_boundary_variation_budget_imported={fmt_bool(result['anchor20000_boundary_variation_budget_imported'])}",
        f"b3_tv_budget_conditional_external_closed={fmt_bool(result['b3_tv_budget_conditional_external_closed'])}",
        f"b3_tv_budget_strict_self_contained_proved={fmt_bool(result['b3_tv_budget_strict_self_contained_proved'])}",
        f"self_contained_mertens_tail_proved={fmt_bool(result['self_contained_mertens_tail_proved'])}",
        f"b3_remainder_total_variation_budget_proved={fmt_bool(result['b3_remainder_total_variation_budget_proved'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 结构压缩",
        "",
        "裸 CRT 估计只给出",
        "",
        "```text",
        "|R_{x,z}| >= (P-1)W^- - sum_d |lambda_d^-|.",
        "```",
        "",
        "但这不是可闭合的最优结构。B3 Rosser 权重应展开为 prime words；此时长度 P 余项是",
        "",
        "```text",
        "signed Stieltjes boundary remainder on B3 admissible faces.",
        "```",
        "",
        "因此当前 TV 项的真实替换是",
        "",
        "```text",
        f"{B3_TV}",
        "  =>",
        f"{STIELTJES} AND {BOUNDARY}",
        "  =>",
        f"{MERTENS} AND {ANCHOR}",
        "```",
        "",
        "其中 `ANCHOR` 在接受外部显式 Mertens/Dusart 尾段时已由 20000 锚点闭合；严格自足线仍需内联 Mertens 尾段证明。",
        "",
        "## 2. 压缩表",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["reductions"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    table_cell(row["formula"]),
                    f"`{table_cell(row['status'])}`",
                    table_cell(row["meaning"]),
                ]
            )
            + " |"
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
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
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
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本步不声明 strict 自足 B3 TV 已闭合；它只把裸 TV 缺口压成有符号 Stieltjes 边界预算，并登记外部条件闭合与自足 Mertens 尾段剩余。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    MONOGRAPH.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
