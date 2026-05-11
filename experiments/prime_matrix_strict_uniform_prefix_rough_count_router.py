#!/usr/bin/env python3
"""生成 strict 统一 prefix 粗筛余下界路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_uniform_prefix_rough_count_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-uniform-prefix-rough-count-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.md"

HARDPOINT = "UniformPrefixRoughCountLowerBound"
MAIN_COEFF = "B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError"
REMAINDER = "B3RemainderTotalVariationBudgetForLengthP"
FINITE = "FiniteBoundaryPrefixRoughCountCertificate"
NORMALIZED = "NormalizedPrefixResidualPotentialLowerBound"
TYPE_THRESHOLD = "FormalUnitTypeThresholdLedger"
ANTICOLLAPSE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.json",
    MONOGRAPH / "prime-matrix-beta-sieve-lower-bound-dominance-router.json",
    MONOGRAPH / "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.json",
    MONOGRAPH / "prime-matrix-beta-sieve-lower-bound-dominance-router.md",
    MONOGRAPH / "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.md",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def sieve_equations() -> list[dict[str, str]]:
    """列出 prefix 粗筛余的筛权公式。"""
    return [
        {
            "equation": "lower_weight_dominance",
            "formula": "1_{(n,P(z))=1} >= sum_{d|(n,P(z))} lambda_d^-.",
            "status": "imported_closed",
        },
        {
            "equation": "prefix_count_lower_sum",
            "formula": "|R_{x,z}| >= sum_d lambda_d^- A_d(x), A_d(x)=#{1<=c<P: d divides xP+c}.",
            "status": "closed",
        },
        {
            "equation": "crt_residue_count",
            "formula": "A_d(x)=(P-1)/d + r_d(x), |r_d(x)|<=1 for squarefree d<P and gcd(d,P)=1.",
            "status": "closed",
        },
        {
            "equation": "main_error_split",
            "formula": "|R_{x,z}| >= (P-1)W^-(z,D) - sum_{d in supp lambda^-}|lambda_d^-|.",
            "status": "closed_as_reduction",
        },
        {
            "equation": "positive_rough_count_contract",
            "formula": "Need (P-1)W^- - TV(lambda^-) >= c P/log z.",
            "status": "open",
        },
    ]


def build_rows(normalized_router: dict[str, Any], dominance: dict[str, Any], main_coeff: dict[str, Any]) -> list[dict[str, Any]]:
    """生成统一 prefix 粗筛余下界判定表。"""
    dominance_closed = dominance.get("lower_weight_dominance_proved") is True
    main_reduced = main_coeff.get("beta_sieve_main_coefficient_atom_reduced") is True
    return [
        {
            "gate": "UniformPrefixRoughCountInputActive",
            "closed": normalized_router.get("next_direct_attack_target") == HARDPOINT,
            "proved": False,
            "meaning": "上一层把 M# 归一化势的核心输入定为 prefix 粗筛余统一下界。",
            "remaining": HARDPOINT,
        },
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本步仍只在假设链条里证明筛余计数输入，不使用真实零行缺席。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "BetaSieveLowerWeightDominanceImported",
            "closed": dominance_closed,
            "proved": dominance_closed,
            "meaning": "已有 beta-sieve lower weights 的逐点支配性：lower sum 不超过筛剩余指示函数。",
            "remaining": "支配性已不是当前硬点。",
        },
        {
            "gate": "PrefixSequenceRemainderFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "对每个 squarefree d<P，因 P mod d 可逆，A_d(x) 是单个 CRT 余类计数，误差绝对值 <=1。",
            "remaining": "需要总变差预算。",
        },
        {
            "gate": "MainErrorSplitClosed",
            "closed": True,
            "proved": True,
            "meaning": "|R_{x,z}| 被下界为主项 (P-1)W^- 减去 lower weights 总变差。",
            "remaining": f"{MAIN_COEFF} AND {REMAINDER}",
        },
        {
            "gate": "B3MainCoefficientTailCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "已有 checkpoint 很强，但尾段证明仍压成连续 beta 主项余量与离散素和误差。",
            "remaining": MAIN_COEFF if main_reduced else "BetaSieveMainCoefficientExplicit99PercentPGe100000",
        },
        {
            "gate": "B3RemainderTotalVariationCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 lower weight 支撑总变差相对 P/log z 足够小；这是从筛主系数到短窗口粗余量的新增必要账本。",
            "remaining": REMAINDER,
        },
        {
            "gate": "FiniteBoundaryPrefixRoughCountCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "任何显式常数路线都要留下有限 P 段；该边界 prefix 证书尚未生成。",
            "remaining": FINITE,
        },
        {
            "gate": "UniformPrefixRoughCountCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "统一 prefix 粗筛余下界已接入 beta-sieve 公式，但主系数、总变差和有限段仍未闭合。",
            "remaining": f"{MAIN_COEFF} AND {REMAINDER} AND {FINITE}",
        },
        {
            "gate": "DownstreamStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "即便粗筛余下界完成，还需类型阈值比较与标签到类型抗塌缩。",
            "remaining": f"{NORMALIZED} THEN {TYPE_THRESHOLD} AND {ANTICOLLAPSE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造统一 prefix 粗筛余下界证书。"""
    normalized_router = load_json(MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.json")
    dominance = load_json(MONOGRAPH / "prime-matrix-beta-sieve-lower-bound-dominance-router.json")
    main_coeff = load_json(MONOGRAPH / "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.json")
    return {
        "certificate_type": "prime_matrix_strict_uniform_prefix_rough_count_router",
        "status": "uniform_prefix_rough_count_reduced_to_beta_main_total_variation_finite_certificate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "beta_sieve_lower_weight_dominance_imported": dominance.get("lower_weight_dominance_proved") is True,
        "prefix_sequence_remainder_formula_closed": True,
        "main_error_split_closed": True,
        "b3_main_coefficient_tail_proved": False,
        "b3_remainder_total_variation_budget_proved": False,
        "finite_boundary_prefix_rough_count_certificate_proved": False,
        "uniform_prefix_rough_count_lower_bound_proved": False,
        "normalized_prefix_residual_potential_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{MAIN_COEFF} AND {REMAINDER} AND {FINITE}",
        "next_direct_attack_target": REMAINDER,
        "parallel_attack_targets": [MAIN_COEFF, FINITE, TYPE_THRESHOLD, ANTICOLLAPSE],
        "sieve_equations": sieve_equations(),
        "rows": build_rows(normalized_router, dominance, main_coeff),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`UniformPrefixRoughCountLowerBound` 已接到已有 beta-sieve lower-weight 体系："
            "逐点支配性已闭合；对 prefix 序列 A_d(x) 的 CRT 计数误差逐项不超过 1。"
            "因此 |R_{x,z}| 的下界等于 beta 主项减 lower weights 总变差。"
            "剩余比原命题窄：B3 主系数尾段、总变差预算、有限小 P 证书。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 统一 prefix 粗筛余下界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"beta_sieve_lower_weight_dominance_imported={fmt_bool(result['beta_sieve_lower_weight_dominance_imported'])}",
        f"prefix_sequence_remainder_formula_closed={fmt_bool(result['prefix_sequence_remainder_formula_closed'])}",
        f"main_error_split_closed={fmt_bool(result['main_error_split_closed'])}",
        f"b3_main_coefficient_tail_proved={fmt_bool(result['b3_main_coefficient_tail_proved'])}",
        f"b3_remainder_total_variation_budget_proved={fmt_bool(result['b3_remainder_total_variation_budget_proved'])}",
        f"finite_boundary_prefix_rough_count_certificate_proved={fmt_bool(result['finite_boundary_prefix_rough_count_certificate_proved'])}",
        f"uniform_prefix_rough_count_lower_bound_proved={fmt_bool(result['uniform_prefix_rough_count_lower_bound_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 筛权公式",
        "",
        "对 prefix 序列 `n_c=xP+c`，已有 lower weights 给出逐点支配：",
        "",
        "```text",
        "1_{(n_c,P(z))=1} >= sum_{d|(n_c,P(z))} lambda_d^-.",
        "```",
        "",
        "求和并使用 CRT 余类计数，得到",
        "",
        "```text",
        "|R_{x,z}| >= (P-1) W^-(z,D) - TV(lambda^-),",
        "TV(lambda^-)=sum_{d in supp lambda^-} |lambda_d^-|.",
        "```",
        "",
        "所以粗筛余下界现在只需要主项大、总变差小、有限段可证。",
        "",
        "## 2. 公式表",
        "",
        "| equation | formula | status |",
        "| --- | --- | --- |",
    ]
    for row in result["sieve_equations"]:
        lines.append(
            "| `{equation}` | {formula} | `{status}` |".format(
                equation=table_cell(row["equation"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
            )
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
    for row in result["rows"]:
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
            "审稿边界：本步只把 prefix 粗筛余下界压成 beta 主项、总变差和有限证书；尚未证明这些输入。",
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
