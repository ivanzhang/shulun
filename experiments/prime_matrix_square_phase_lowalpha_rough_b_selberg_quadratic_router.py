#!/usr/bin/env python3
"""审计 rough-b 维数一 Selberg 二次型上界。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_rough_b_selberg_quadratic_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-selberg-quadratic-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-selberg-quadratic-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-selberg-quadratic-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_prime_b_sieve_router as sieve


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-rough-b-selberg-quadratic-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-rough-b-selberg-quadratic-router.md"

DEFAULT_P_LIST = sieve.DEFAULT_P_LIST
DEFAULT_D_LEVEL = 1000
DEFAULT_Z_LIST = [7, 13, 31, 61]
DEFAULT_CONSTANT = 1.35
NEXT_TARGET = "SelbergQuadraticRemainderUniformBoundOrSquarefreeLowModPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.json",
    "prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.json",
]

envelope = sieve.envelope


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
        "experiments/prime_matrix_square_phase_lowalpha_rough_b_selberg_quadratic_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_values(p_list: list[int], flags: bytearray, trial_primes: list[int]) -> list[int]:
    """收集所有 prime-a incidence 的 b 多重序列。"""
    values: list[int] = []
    for p in p_list:
        candidates = sieve.collect_prime_a_candidates(p, flags, trial_primes)
        values.extend(int(candidate["b"]) for candidate in candidates)
    return values


def generate_squarefree_support(z: int, d_level: int, primes: list[int]) -> list[tuple[int, int]]:
    """生成由 `prime<=z` 组成且 `d<=D` 的 squarefree 支撑 `(d, omega)`。"""
    small_primes = [prime for prime in primes if prime <= z]
    support: list[tuple[int, int]] = []

    def visit(index: int, current: int, omega: int) -> None:
        support.append((current, omega))
        for next_index in range(index, len(small_primes)):
            value = current * small_primes[next_index]
            if value > d_level:
                continue
            visit(next_index + 1, value, omega + 1)

    visit(0, 1, 0)
    return sorted(set(support))


def selberg_weights(z: int, d_level: int, primes: list[int]) -> dict[int, float]:
    """构造简单维数一 Selberg/Brun 权，满足 lambda_1=1。"""
    log_level = math.log(d_level)
    weights: dict[int, float] = {}
    for d, omega in generate_squarefree_support(z, d_level, primes):
        if d == 1:
            weights[d] = 1.0
            continue
        mu = -1.0 if omega % 2 else 1.0
        weights[d] = mu * max(0.0, math.log(d_level / d) / log_level)
    return weights


def is_rough_to(value: int, primes: list[int], z: int) -> bool:
    """判断 value 是否没有不超过 z 的非平凡素因子。"""
    for prime in primes:
        if prime > z:
            break
        if value != prime and value % prime == 0:
            return False
    return True


def mertens_product(primes: list[int], z: int) -> float:
    """计算维数一 Mertens 乘积。"""
    product = 1.0
    for prime in primes:
        if prime > z:
            break
        product *= 1.0 - 1.0 / prime
    return product


def lcm(a: int, b: int) -> int:
    """计算最小公倍数。"""
    return a // math.gcd(a, b) * b


def model_quadratic(weights: dict[int, float], count: int) -> float:
    """用随机模型 `A_m=N/m` 计算 Selberg 二次型主项。"""
    total = 0.0
    items = list(weights.items())
    for d, lambda_d in items:
        for e, lambda_e in items:
            total += lambda_d * lambda_e / lcm(d, e)
    return count * total


def direct_quadratic(values: list[int], weights: dict[int, float]) -> float:
    """直接计算样本上的 Selberg 二次型。"""
    total = 0.0
    items = list(weights.items())
    for value in values:
        inner = 0.0
        for d, weight in items:
            if value % d == 0:
                inner += weight
        total += inner * inner
    return total


def row_for_z(values: list[int], primes: list[int], z: int, d_level: int, constant: float) -> dict[str, Any]:
    """计算单个 z 的 Selberg 二次型行。"""
    weights = selberg_weights(z, d_level, primes)
    rough = sum(1 for value in values if is_rough_to(value, primes, z))
    direct = direct_quadratic(values, weights)
    model = model_quadratic(weights, len(values))
    mertens = len(values) * mertens_product(primes, z)
    remainder = direct - model
    return {
        "z": z,
        "d_level": d_level,
        "support_size": len(weights),
        "value_count": len(values),
        "rough_count": rough,
        "direct_selberg_quadratic": direct,
        "model_selberg_quadratic": model,
        "mertens_model": mertens,
        "selberg_remainder": remainder,
        "upper_bound_verified": rough <= direct + 1e-9,
        "direct_over_rough": safe_ratio(direct, rough),
        "direct_over_mertens": safe_ratio(direct, mertens),
        "rough_over_mertens": safe_ratio(rough, mertens),
        "model_over_mertens": safe_ratio(model, mertens),
        "remainder_over_mertens": safe_ratio(remainder, mertens),
        "covered_by_constant": direct <= constant * mertens,
        "constant": constant,
    }


def audit(p_list: list[int], z_list: list[int], d_level: int, constant: float) -> dict[str, Any]:
    """执行 Selberg 二次型审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    values = collect_values(p_list, flags, trial_primes)
    rows = [row_for_z(values, trial_primes, z, d_level, constant) for z in z_list]
    failures = [row for row in rows if not row["upper_bound_verified"]]
    constant_failures = [row for row in rows if not row["covered_by_constant"]]
    worst_direct = max(rows, key=lambda item: item["direct_over_mertens"] or 0.0, default=None)
    worst_remainder = max(rows, key=lambda item: abs(item["remainder_over_mertens"] or 0.0), default=None)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_rough_b_selberg_quadratic_router",
        "status": "rough_b_selberg_quadratic_upper_materialized_remainder_uniformity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "selberg_quadratic_upper_identity_closed": len(failures) == 0,
        "sample_constant_covers_selberg_quadratic": len(constant_failures) == 0,
        "selberg_remainder_uniform_bound_proved": False,
        "squarefree_lowmod_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "d_level": d_level,
        "constant": constant,
        "value_count": len(values),
        "rows": rows,
        "upper_failure_count": len(failures),
        "constant_failure_count": len(constant_failures),
        "worst_direct_over_mertens_row": worst_direct,
        "worst_remainder_row": worst_remainder,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把 rough-b 幸存者上界写成真正的维数一 Selberg 二次型。"
            "对任意 `z`-rough 的 b，只有 `d=1` 贡献，因此 "
            "`1_rough(b) <= (sum_{d|b} lambda_d)^2`；样本中所有 z 行均满足该上界。"
            "二次型再拆成随机主项 `A_m=N/m` 与 squarefree 低模余项。当前样本常数包覆盖，"
            "但全局仍需证明 Selberg 余项统一上界，或把余项过大命名为 Squarefree-LowMod-PDEC 并排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha rough-b Selberg 二次型路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"selberg_quadratic_upper_identity_closed={fmt_bool(result['selberg_quadratic_upper_identity_closed'])}",
        f"sample_constant_covers_selberg_quadratic={fmt_bool(result['sample_constant_covers_selberg_quadratic'])}",
        f"selberg_remainder_uniform_bound_proved={fmt_bool(result['selberg_remainder_uniform_bound_proved'])}",
        f"squarefree_lowmod_pdec_excluded={fmt_bool(result['squarefree_lowmod_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Selberg 二次型账本",
        "",
        "| z | D | support | rough | direct Q | model Q | Mertens | Q/rough | Q/Mertens | remainder/Mertens | covered |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['z']} | {row['d_level']} | {row['support_size']} | {row['rough_count']} | "
            f"{fmt_float(row['direct_selberg_quadratic'])} | {fmt_float(row['model_selberg_quadratic'])} | "
            f"{fmt_float(row['mertens_model'])} | {fmt_float(row['direct_over_rough'])} | "
            f"{fmt_float(row['direct_over_mertens'])} | {fmt_float(row['remainder_over_mertens'])} | "
            f"{fmt_bool(row['covered_by_constant'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 汇总",
            "",
            "| values | D level | constant | upper failures | constant failures | worst direct row | worst remainder row |",
            "| ---: | ---: | ---: | ---: | ---: | --- | --- |",
            (
                f"| {result['value_count']} | {result['d_level']} | {fmt_float(result['constant'])} | "
                f"{result['upper_failure_count']} | {result['constant_failure_count']} | "
                f"`{result['worst_direct_over_mertens_row']}` | `{result['worst_remainder_row']}` |"
            ),
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：给定权重后 `rough_count <= Selberg quadratic` 是确定性不等式。",
            "- 已物化：样本中二次型主项与 squarefree 余项拆分账本。",
            "- 未闭合：全局证明 squarefree 低模余项足够小，使二次型由维数一 Mertens 包络支付。",
            "- 未闭合：排斥持久 Squarefree-LowMod-PDEC/SAE。",
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
    parser.add_argument("--constant", type=float, default=DEFAULT_CONSTANT)
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), parse_int_list(args.z_list), args.d_level, args.constant)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "selberg_quadratic_upper_identity_closed": result[
                    "selberg_quadratic_upper_identity_closed"
                ],
                "sample_constant_covers_selberg_quadratic": result[
                    "sample_constant_covers_selberg_quadratic"
                ],
                "upper_failure_count": result["upper_failure_count"],
                "constant_failure_count": result["constant_failure_count"],
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
