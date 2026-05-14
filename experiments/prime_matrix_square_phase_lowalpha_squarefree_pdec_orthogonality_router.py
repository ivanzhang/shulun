#!/usr/bin/env python3
"""审计 squarefree PDEC 的系数-余项向量正交结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_squarefree_pdec_orthogonality_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-orthogonality-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-orthogonality-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-orthogonality-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-squarefree-pdec-orthogonality-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-squarefree-pdec-orthogonality-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z_LIST = attribution.DEFAULT_Z_LIST
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_ABS_CONTRIBUTION = 20.0
NEXT_TARGET = "CoefficientRemainderOrthogonalityAngleBoundOrVectorSquarefreePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json",
    "prime-matrix-square-phase-lowalpha-squarefree-pdec-pairing-ledger-router.json",
]


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
        "experiments/prime_matrix_square_phase_lowalpha_squarefree_pdec_orthogonality_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_values_and_primes(p_list: list[int]) -> tuple[list[int], list[int]]:
    """复用 Selberg 归因账本的 prime-a b 序列。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = attribution.envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = attribution.envelope.primes_from_flags(flags, trial_limit)
    values = attribution.selberg.collect_values(p_list, flags, trial_primes)
    return values, trial_primes


def row_for_z(values: list[int], primes: list[int], z: int, d_level: int, threshold: float) -> dict[str, Any]:
    """计算单个 z 层的向量正交账本。"""
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    coeffs = attribution.coefficient_by_lcm(weights)
    counts = attribution.divisibility_counts(values, sorted(coeffs))
    coeff_vector = []
    remainder_vector = []
    contribution_vector = []
    threshold_contribution = 0.0
    threshold_abs = 0.0
    threshold_count = 0
    for modulus, coefficient in coeffs.items():
        expected = len(values) / modulus
        remainder = counts[modulus] - expected
        contribution = coefficient * remainder
        coeff_vector.append(coefficient)
        remainder_vector.append(remainder)
        contribution_vector.append(contribution)
        if abs(contribution) >= threshold:
            threshold_contribution += contribution
            threshold_abs += abs(contribution)
            threshold_count += 1
    net = sum(contribution_vector)
    abs_sum = sum(abs(item) for item in contribution_vector)
    coeff_l1 = sum(abs(item) for item in coeff_vector)
    coeff_l2 = math.sqrt(sum(item * item for item in coeff_vector))
    remainder_l2 = math.sqrt(sum(item * item for item in remainder_vector))
    cauchy = coeff_l2 * remainder_l2
    subthreshold_correction = net - threshold_contribution
    direct_row = attribution.selberg.row_for_z(values, primes, z, d_level, constant=10.0)
    return {
        "z": z,
        "d_level": d_level,
        "moduli_count": len(coeffs),
        "threshold_packet_count": threshold_count,
        "coefficient_l1": coeff_l1,
        "coefficient_l2": coeff_l2,
        "remainder_l2": remainder_l2,
        "cauchy_envelope": cauchy,
        "weighted_abs_remainder": abs_sum,
        "net_remainder_inner_product": net,
        "net_remainder_from_quadratic": direct_row["selberg_remainder"],
        "inner_product_identity_error": net - direct_row["selberg_remainder"],
        "net_over_cauchy": safe_ratio(net, cauchy),
        "abs_net_over_cauchy": safe_ratio(abs(net), cauchy),
        "weighted_abs_over_cauchy": safe_ratio(abs_sum, cauchy),
        "threshold_signed_contribution": threshold_contribution,
        "threshold_abs_contribution": threshold_abs,
        "threshold_signed_over_abs": safe_ratio(abs(threshold_contribution), threshold_abs),
        "subthreshold_correction": subthreshold_correction,
        "subthreshold_correction_over_threshold_residual": safe_ratio(
            abs(subthreshold_correction), abs(threshold_contribution)
        ),
        "mertens_model": direct_row["mertens_model"],
        "net_over_mertens": safe_ratio(net, direct_row["mertens_model"]),
        "cauchy_over_mertens": safe_ratio(cauchy, direct_row["mertens_model"]),
    }


def audit(p_list: list[int], z_list: list[int], d_level: int, threshold: float) -> dict[str, Any]:
    """执行向量正交审计。"""
    values, primes = collect_values_and_primes(p_list)
    rows = [row_for_z(values, primes, z, d_level, threshold) for z in z_list]
    identity_failures = [row for row in rows if abs(row["inner_product_identity_error"]) > 1e-6]
    worst_angle = max(rows, key=lambda row: row["abs_net_over_cauchy"] or 0.0, default=None)
    best_angle = min(rows, key=lambda row: row["abs_net_over_cauchy"] or 1.0, default=None)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_squarefree_pdec_orthogonality_router",
        "status": "coefficient_remainder_inner_product_identity_closed_angle_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "coefficient_remainder_inner_product_identity_closed": len(identity_failures) == 0,
        "cauchy_vector_envelope_closed": True,
        "sample_small_angle_observed": all((row["abs_net_over_cauchy"] or 1.0) <= 0.05 for row in rows),
        "coefficient_remainder_orthogonality_angle_bound_proved": False,
        "vector_squarefree_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "abs_contribution_threshold": threshold,
        "value_count": len(values),
        "identity_failure_count": len(identity_failures),
        "rows": rows,
        "worst_angle_row": worst_angle,
        "best_angle_row": best_angle,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "跨模数正负配对不应按贪心边证明，而应回到 Selberg 余项的真实代数对象："
            "`Q_direct-Q_model=<c,R>`，其中 `c_m` 是二次型 lcm 系数，"
            "`R_m=A_m-N/m` 是 squarefree 低模余项向量。"
            "本步闭合内积恒等式和 Cauchy 包络，并显示样本净余项对应很小夹角；"
            "全局剩余是证明这种系数-余项近正交，或把大夹角命名为 VectorSquarefree-PDEC 并排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha squarefree PDEC 正交路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        (
            "coefficient_remainder_inner_product_identity_closed="
            f"{fmt_bool(result['coefficient_remainder_inner_product_identity_closed'])}"
        ),
        f"cauchy_vector_envelope_closed={fmt_bool(result['cauchy_vector_envelope_closed'])}",
        f"sample_small_angle_observed={fmt_bool(result['sample_small_angle_observed'])}",
        (
            "coefficient_remainder_orthogonality_angle_bound_proved="
            f"{fmt_bool(result['coefficient_remainder_orthogonality_angle_bound_proved'])}"
        ),
        f"vector_squarefree_pdec_excluded={fmt_bool(result['vector_squarefree_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 正交账本",
        "",
        "| z | moduli | packets | net | abs | cauchy | net/cauchy | abs/cauchy | threshold signed | subthreshold correction |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['z']} | {row['moduli_count']} | {row['threshold_packet_count']} | "
            f"{fmt_float(row['net_remainder_inner_product'])} | "
            f"{fmt_float(row['weighted_abs_remainder'])} | {fmt_float(row['cauchy_envelope'])} | "
            f"{fmt_float(row['abs_net_over_cauchy'])} | "
            f"{fmt_float(row['weighted_abs_over_cauchy'])} | "
            f"{fmt_float(row['threshold_signed_contribution'])} | "
            f"{fmt_float(row['subthreshold_correction'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：`Q_direct-Q_model=<c,R>` 的内积恒等式。",
            "- 已闭合：`|<c,R>|<=||c||_2 ||R||_2` 的向量包络。",
            "- 已校正：阈值包 residual 还会被 subthreshold 包继续修正，因此单独研究阈值配对不够。",
            "- 未闭合：全局证明 `c` 与 `R` 的夹角足够小，或证明大夹角会形成可排斥的 VectorSquarefree-PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
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
    parser.add_argument("--abs-contribution", type=float, default=DEFAULT_ABS_CONTRIBUTION)
    args = parser.parse_args()
    result = audit(
        parse_int_list(args.p_list),
        parse_int_list(args.z_list),
        args.d_level,
        args.abs_contribution,
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "identity_failure_count": result["identity_failure_count"],
                "worst_abs_net_over_cauchy": result["worst_angle_row"]["abs_net_over_cauchy"],
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
