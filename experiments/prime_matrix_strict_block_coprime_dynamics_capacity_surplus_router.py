#!/usr/bin/env python3
"""生成 strict 块互质动力容量反超路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_block_coprime_dynamics_capacity_surplus_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-block-coprime-dynamics-capacity-surplus-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-block-coprime-dynamics-capacity-surplus-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-block-coprime-dynamics-capacity-surplus-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.md",
    MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.md",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.md",
    DOCS / "local-label-conflict-scan.md",
]

EULER_GAMMA = 0.5772156649015329
MERTENS_ROUGH_CONSTANT = math.exp(-EULER_GAMMA)

BLOCK_CAPACITY = "BlockCoprimeDynamicsCapacitySurplus"
FINITE_SUPPLY = "FinitePrimeSupplyVsCoprimeDynamicsLoad"
ALPHA_ROUGH_LOAD = "AlphaPrefixRoughLoadLowerBoundExceedingHighLabelCapacity"
HIGH_LABEL_COUNT = "HighLabelPrimeCountingUpperBoundForAlphaSlice"
QUOTIENT_SHELL = "AdjacentQuotientShellCapacityOrSquareDefectLedger"
B3_REMAINDER = "B3RemainderTotalVariationBudgetForLengthP"


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


def alpha_profile(alpha: float) -> dict[str, Any]:
    """给出 alpha 切片的容量常数诊断。

    这里的常数只用于定位目标：若能证明粗筛余量至少
    c_alpha * P/log P，且 c_alpha 大于高标签容量常数，则早期零行矛盾。
    """
    full_row_hit_cap = math.ceil(1.0 / alpha)
    high_label_capacity_constant = full_row_hit_cap * (1.0 - alpha)
    return {
        "alpha": alpha,
        "full_row_hit_cap_for_q_gt_alphaP": full_row_hit_cap,
        "high_label_capacity_constant_target": high_label_capacity_constant,
        "mertens_rough_constant_reference": MERTENS_ROUGH_CONSTANT,
        "reference_surplus_if_mertens_scale_available": MERTENS_ROUGH_CONSTANT
        - high_label_capacity_constant,
        "capacity_beaten_by_mertens_scale": MERTENS_ROUGH_CONSTANT
        > high_label_capacity_constant,
    }


def exact_laws() -> list[dict[str, str]]:
    """列出本路由闭合的精确律。"""
    return [
        {
            "law": "block_high_label_capacity",
            "formula": "C_{B,z}(x)=sum_{z<q<P} #{c in B: xP+c == 0 mod q}.",
            "status": "closed_definition",
            "meaning": "早期零行中，所有 z-rough 位置必须由这个高标签容量覆盖。",
        },
        {
            "law": "block_capacity_ceiling",
            "formula": "C_{B,z}(x)<=sum_{z<q<P} ceil(|B|/q).",
            "status": "closed",
            "meaning": "同一素标签在短块中只能按同一模 q 余类重复。",
        },
        {
            "law": "full_row_alpha_half_capacity",
            "formula": "If z=alpha P and alpha>1/2, then C_{[1,P-1],z}(x)<=2(pi(P)-pi(alpha P)).",
            "status": "closed",
            "meaning": "高标签每个最多命中两列，给出最清晰的有限供给上界。",
        },
        {
            "law": "rough_load_to_contradiction",
            "formula": "If |R_{B,z}(x)|>C_{B,z}(x), then an early zero row at x is impossible.",
            "status": "closed_implication",
            "meaning": "这是反例链与真实容量链之间的直接矛盾判据。",
        },
        {
            "law": "adjacent_quotient_coprime_support",
            "formula": "For adjacent rough composites q_c m_c and q_{c+1} m_{c+1}, all prime supports across the two products are disjoint.",
            "status": "closed",
            "meaning": "商相邻互质已并入容量场，但还需要负载下界才能产生反超。",
        },
        {
            "law": "semiprime_shell_for_alpha_gt_half",
            "formula": "For alpha>1/2 and n<P^2+P, every alpha P-rough composite has at most two prime factors.",
            "status": "closed_with_small_P_boundary",
            "meaning": "粗洞在早期零行下进入高标签-商壳层；平方点作为单独缺陷账本登记。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "所有结论仍在 Assume EarlyZeroRowWithinP 下推导。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "ExactBlockCapacityFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "块内高标签供给等于各 q 的单余类命中数之和。",
            "remaining": "无。",
        },
        {
            "gate": "FullRowAlphaHalfCapacityClosed",
            "closed": True,
            "proved": True,
            "meaning": "alpha>1/2 时，全行每个高标签最多命中两列。",
            "remaining": HIGH_LABEL_COUNT,
        },
        {
            "gate": "DirectContradictionCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "若 alphaP-rough 负载超过高标签容量，早期零行立刻矛盾。",
            "remaining": ALPHA_ROUGH_LOAD,
        },
        {
            "gate": "AdjacentQuotientDynamicsIntegrated",
            "closed": True,
            "proved": True,
            "meaning": "相邻互质和商相邻互质给出支撑不交、短距不可复用和壳层容量约束。",
            "remaining": QUOTIENT_SHELL,
        },
        {
            "gate": "CoprimeDynamicsCapacitySurplusCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明某个 alpha 或块上 |R| 严格大于 C；互质动力本身不自动给负载下界。",
            "remaining": f"{ALPHA_ROUGH_LOAD} AND {HIGH_LABEL_COUNT}",
        },
        {
            "gate": "UnifiedContradictionFieldPromotedToClosure",
            "closed": False,
            "proved": False,
            "meaning": "容量反超判据已闭合，但反超输入未闭合，所以统一矛盾场不能升级为无条件闭合。",
            "remaining": f"{B3_REMAINDER} OR {ALPHA_ROUGH_LOAD} OR registered PDEC/SAE defect exclusion",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    alpha_values = [0.55, 2 / 3, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
    alpha_profiles = [alpha_profile(alpha) for alpha in alpha_values]
    return {
        "certificate_type": "prime_matrix_strict_block_coprime_dynamics_capacity_surplus_router",
        "status": "block_capacity_surplus_criterion_closed_load_surplus_input_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "exact_block_capacity_formula_closed": True,
        "full_row_alpha_half_capacity_closed": True,
        "direct_capacity_surplus_contradiction_criterion_closed": True,
        "adjacent_quotient_dynamics_integrated": True,
        "coprime_dynamics_capacity_surplus_proved": False,
        "finite_supply_vs_load_contradiction_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ALPHA_ROUGH_LOAD,
        "parallel_targets": [HIGH_LABEL_COUNT, QUOTIENT_SHELL, B3_REMAINDER],
        "exact_laws": exact_laws(),
        "decision_rows": decision_rows(),
        "alpha_capacity_profiles": alpha_profiles,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把早期零行反例链压成一个明确的容量反超判据："
            "对任意块 B 和 cutoff z，若 z-rough 位置数 |R_{B,z}(x)| 大于 "
            "高标签容量 C_{B,z}(x)，则这些位置无法全部由 P 以内素因子覆盖，早期零行矛盾。"
            "当 z=alpha P 且 alpha>1/2 时，全行容量有简单上界 "
            "2(pi(P)-pi(alpha P))。相邻互质与商相邻互质已并入该容量场，"
            "但它们本身不提供 |R| 的正下界；当前真正剩余是证明某个 alpha/块的粗洞负载"
            "严格超过有限供给容量，或证明负载不足必登记为 PDEC/SAE 缺陷并被排斥。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 块互质动力容量反超路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_block_capacity_formula_closed={fmt_bool(result['exact_block_capacity_formula_closed'])}",
        f"full_row_alpha_half_capacity_closed={fmt_bool(result['full_row_alpha_half_capacity_closed'])}",
        f"direct_capacity_surplus_contradiction_criterion_closed={fmt_bool(result['direct_capacity_surplus_contradiction_criterion_closed'])}",
        f"adjacent_quotient_dynamics_integrated={fmt_bool(result['adjacent_quotient_dynamics_integrated'])}",
        f"coprime_dynamics_capacity_surplus_proved={fmt_bool(result['coprime_dynamics_capacity_surplus_proved'])}",
        f"finite_supply_vs_load_contradiction_proved={fmt_bool(result['finite_supply_vs_load_contradiction_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确反超判据",
        "",
        "设 `B` 是一段列块，`R_{B,z}(x)` 是块内所有不含 `<=z` 素因子的列。早期零行若成立，则每个这样的列仍必须有某个 `q<P` 因子；因为它没有 `<=z` 因子，所以这个因子必在 `(z,P)` 中。",
        "",
        "```text",
        "C_{B,z}(x)=sum_{z<q<P} #{c in B: q divides xP+c}.",
        "|R_{B,z}(x)| <= C_{B,z}(x)    (早期零行的必要条件)",
        "```",
        "",
        "所以只要证明 `|R_{B,z}(x)|>C_{B,z}(x)`，就得到直接矛盾。",
        "",
        "## 2. 已闭合刚性律",
        "",
        "| law | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["exact_laws"]:
        lines.append(
            "| `{law}` | {formula} | `{status}` | {meaning} |".format(
                law=table_cell(row["law"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. alpha 全行容量诊断",
            "",
            "下表不是证明，只用于定位最窄常数目标。若能给出 `|R_{x,alpha P}| >= c_alpha P/log P`，且 `c_alpha` 大于高标签容量常数，就能触发上面的直接矛盾。",
            "",
            "| alpha | hit cap | high-label capacity constant | Mertens-scale reference | surplus if available | target beaten |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["alpha_capacity_profiles"]:
        lines.append(
            "| {alpha:.6f} | {hit} | {cap:.6f} | {ref:.6f} | {surplus:.6f} | `{beaten}` |".format(
                alpha=row["alpha"],
                hit=row["full_row_hit_cap_for_q_gt_alphaP"],
                cap=row["high_label_capacity_constant_target"],
                ref=row["mertens_rough_constant_reference"],
                surplus=row["reference_surplus_if_mertens_scale_available"],
                beaten=fmt_bool(row["capacity_beaten_by_mertens_scale"]),
            )
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
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 最新最窄输入",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步闭合的是反例链必须满足的容量不等式，以及违反该不等式时的直接矛盾；尚未证明任何具体 `alpha` 或块真的违反容量上界。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
