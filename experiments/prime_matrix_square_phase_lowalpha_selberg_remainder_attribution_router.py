#!/usr/bin/env python3
"""审计 rough-b Selberg 二次型余项的 squarefree 模数归因。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_rough_b_selberg_quadratic_router as selberg


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.md"

DEFAULT_P_LIST = selberg.DEFAULT_P_LIST
DEFAULT_D_LEVEL = selberg.DEFAULT_D_LEVEL
DEFAULT_Z_LIST = selberg.DEFAULT_Z_LIST
NEXT_TARGET = "SelbergRemainderCoefficientL1BoundOrConcreteSquarefreePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-rough-b-selberg-quadratic-router.json",
    "prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.json",
]

envelope = selberg.envelope


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def coefficient_by_lcm(weights: dict[int, float]) -> dict[int, float]:
    """把 Selberg 二次型系数按 `m=lcm(d,e)` 合并。"""
    coeffs: dict[int, float] = defaultdict(float)
    items = list(weights.items())
    for d, lambda_d in items:
        for e, lambda_e in items:
            coeffs[selberg.lcm(d, e)] += lambda_d * lambda_e
    return dict(coeffs)


def divisibility_counts(values: list[int], moduli: list[int]) -> dict[int, int]:
    """统计每个 m 的 `m|b` 数量。"""
    result = {}
    for modulus in moduli:
        result[modulus] = sum(1 for value in values if value % modulus == 0)
    return result


def row_for_z(values: list[int], primes: list[int], z: int, d_level: int) -> dict[str, Any]:
    """计算单个 z 的余项归因。"""
    weights = selberg.selberg_weights(z, d_level, primes)
    coeffs = coefficient_by_lcm(weights)
    counts = divisibility_counts(values, sorted(coeffs))
    contributions = []
    total_remainder = 0.0
    coeff_l1 = 0.0
    weighted_abs_remainder = 0.0
    for modulus, coeff in coeffs.items():
        expected = len(values) / modulus
        remainder = counts[modulus] - expected
        contribution = coeff * remainder
        total_remainder += contribution
        coeff_l1 += abs(coeff)
        weighted_abs_remainder += abs(contribution)
        contributions.append(
            {
                "m": modulus,
                "coefficient": coeff,
                "actual": counts[modulus],
                "expected": expected,
                "remainder": remainder,
                "contribution": contribution,
                "abs_contribution": abs(contribution),
                "actual_over_expected": safe_ratio(counts[modulus], expected),
            }
        )
    top_abs = sorted(contributions, key=lambda item: item["abs_contribution"], reverse=True)[:16]
    direct_row = selberg.row_for_z(values, primes, z, d_level, constant=10.0)
    return {
        "z": z,
        "d_level": d_level,
        "support_size": len(weights),
        "lcm_moduli_count": len(coeffs),
        "coefficient_l1": coeff_l1,
        "weighted_abs_remainder": weighted_abs_remainder,
        "net_remainder": total_remainder,
        "net_remainder_from_quadratic": direct_row["selberg_remainder"],
        "remainder_identity_error": total_remainder - direct_row["selberg_remainder"],
        "weighted_abs_over_mertens": safe_ratio(weighted_abs_remainder, direct_row["mertens_model"]),
        "net_remainder_over_mertens": safe_ratio(total_remainder, direct_row["mertens_model"]),
        "top_abs_contributions": top_abs,
    }


def audit(p_list: list[int], z_list: list[int], d_level: int) -> dict[str, Any]:
    """执行 Selberg 余项归因审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    values = selberg.collect_values(p_list, flags, trial_primes)
    rows = [row_for_z(values, trial_primes, z, d_level) for z in z_list]
    identity_failures = [row for row in rows if abs(row["remainder_identity_error"]) > 1e-6]
    worst_abs = max(rows, key=lambda item: item["weighted_abs_over_mertens"] or 0.0, default=None)
    worst_net = max(rows, key=lambda item: abs(item["net_remainder_over_mertens"] or 0.0), default=None)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router",
        "status": "selberg_remainder_attributed_to_squarefree_lowmod_coefficients_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "selberg_remainder_attribution_identity_closed": len(identity_failures) == 0,
        "coefficient_l1_budget_proved": False,
        "squarefree_lowmod_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "d_level": d_level,
        "value_count": len(values),
        "identity_failure_count": len(identity_failures),
        "rows": rows,
        "worst_weighted_abs_row": worst_abs,
        "worst_net_row": worst_net,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Selberg 二次型余项已无损归因到 squarefree 低模 `m=lcm(d,e)`："
            "`Q_direct-Q_model=sum_m c_m(A_m-N/m)`。样本中归因恒等式误差为零量级。"
            "下一步不再需要寻找新的几何对象，而是证明系数 L1 与 squarefree 低模余项的乘积可求和；"
            "若某个 `m` 或一簇 `m` 贡献持久过大，就直接形成 ConcreteSquarefree-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha Selberg 余项归因路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"selberg_remainder_attribution_identity_closed={fmt_bool(result['selberg_remainder_attribution_identity_closed'])}",
        f"coefficient_l1_budget_proved={fmt_bool(result['coefficient_l1_budget_proved'])}",
        f"squarefree_lowmod_pdec_excluded={fmt_bool(result['squarefree_lowmod_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 余项归因账本",
        "",
        "| z | support | lcm moduli | coeff L1 | abs remainder | abs/Mertens | net/Mertens | identity error |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['z']} | {row['support_size']} | {row['lcm_moduli_count']} | "
            f"{fmt_float(row['coefficient_l1'])} | {fmt_float(row['weighted_abs_remainder'])} | "
            f"{fmt_float(row['weighted_abs_over_mertens'])} | "
            f"{fmt_float(row['net_remainder_over_mertens'])} | "
            f"{fmt_float(row['remainder_identity_error'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 最坏行",
            "",
            "| kind | data |",
            "| --- | --- |",
            f"| weighted abs | `{result['worst_weighted_abs_row']}` |",
            f"| net | `{result['worst_net_row']}` |",
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：`Q_direct-Q_model=sum_m c_m(A_m-N/m)` 的归因恒等式。",
            "- 已物化：每个 `z` 下最大贡献的具体 squarefree `m` 清单。",
            "- 未闭合：证明 `sum_m |c_m||A_m-N/m|` 全局可由 Mertens 余量吸收。",
            "- 未闭合：排斥持久 ConcreteSquarefree-PDEC/SAE。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--z-list", default=",".join(str(item) for item in DEFAULT_Z_LIST))
    parser.add_argument("--d-level", type=int, default=DEFAULT_D_LEVEL)
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), parse_int_list(args.z_list), args.d_level)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "selberg_remainder_attribution_identity_closed": result[
                    "selberg_remainder_attribution_identity_closed"
                ],
                "identity_failure_count": result["identity_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
