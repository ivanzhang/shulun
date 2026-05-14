#!/usr/bin/env python3
"""审计 prime-b 层的粗数筛 normal form。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_prime_b_sieve_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-prime-b-sieve-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-b-sieve-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-b-sieve-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_fixed_b_semiprime_incidence_router as incidence


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-prime-b-sieve-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-prime-b-sieve-router.md"

DEFAULT_P_LIST = incidence.DEFAULT_P_LIST
NEXT_TARGET = "RoughBReciprocalFloorSelbergRankinOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-fixed-b-semiprime-incidence-router.json",
    "prime-matrix-square-phase-lowalpha-semiprime-phase-sawtooth-router.json",
]

divisor = incidence.divisor
qscan = incidence.qscan
normal = incidence.normal
envelope = incidence.envelope


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
        "experiments/prime_matrix_square_phase_lowalpha_prime_b_sieve_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_prime_a_candidates(
    p: int,
    flags: bytearray,
    trial_primes: list[int],
) -> list[dict[str, Any]]:
    """收集所有 prime-a 半素数 incidence 候选。"""
    _, by_b_prime_a, _ = divisor.collect_qscan_by_b(p, flags, trial_primes)
    candidates: list[dict[str, Any]] = []
    for b, records in by_b_prime_a.items():
        for record in records:
            candidates.append({**record, "b": b})
    return candidates


def is_rough_to(value: int, primes: list[int], y: int) -> bool:
    """判断 value 是否没有不超过 y 的素因子。"""
    for prime in primes:
        if prime > y:
            break
        if value != prime and value % prime == 0:
            return False
    return True


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 prime-b 粗数筛。"""
    candidates = collect_prime_a_candidates(p, flags, trial_primes)
    max_b = max((int(candidate["b"]) for candidate in candidates), default=0)
    sqrt_max_b = math.isqrt(max_b)
    sieve_primes = [prime for prime in trial_primes if prime <= max(2, sqrt_max_b)]
    base_cutoffs = [7, 13, 31, 61, 127, 251, 503, 1009]
    cutoffs = sorted({cutoff for cutoff in base_cutoffs if cutoff <= sqrt_max_b} | {sqrt_max_b})
    rows = []
    exact_prime_count = sum(1 for candidate in candidates if candidate["prime_b"])
    for cutoff in cutoffs:
        rough_count = sum(1 for candidate in candidates if is_rough_to(int(candidate["b"]), sieve_primes, cutoff))
        rows.append(
            {
                "cutoff": cutoff,
                "rough_count": rough_count,
                "rough_over_prime_a": safe_ratio(rough_count, len(candidates)),
                "prime_b_count": exact_prime_count,
                "prime_b_over_rough": safe_ratio(exact_prime_count, rough_count),
            }
        )
    sqrt_rough = rows[-1]["rough_count"] if rows else 0
    exact_failures = []
    if sqrt_rough != exact_prime_count:
        exact_failures.append({"p": p, "sqrt_rough": sqrt_rough, "prime_b": exact_prime_count})
    top_prime_b_samples = [candidate for candidate in candidates if candidate["prime_b"]][:8]
    top_composite_rough_samples = [
        candidate
        for candidate in candidates
        if not candidate["prime_b"] and is_rough_to(int(candidate["b"]), sieve_primes, min(61, sqrt_max_b))
    ][:8]
    return {
        "p": p,
        "prime_a_fibers": len(candidates),
        "prime_b_fibers": exact_prime_count,
        "max_b": max_b,
        "sqrt_max_b": sqrt_max_b,
        "sqrt_sieve_rough_count": sqrt_rough,
        "sqrt_sieve_exact_failure_count": len(exact_failures),
        "prime_b_over_prime_a": safe_ratio(exact_prime_count, len(candidates)),
        "cutoff_rows": rows,
        "sample_exact_failures": exact_failures,
        "sample_prime_b": top_prime_b_samples,
        "sample_composite_rough_y61": top_composite_rough_samples,
    }


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 prime-b 粗数筛审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]

    prime_a_fibers = sum(profile["prime_a_fibers"] for profile in profiles)
    prime_b_fibers = sum(profile["prime_b_fibers"] for profile in profiles)
    exact_failures = sum(profile["sqrt_sieve_exact_failure_count"] for profile in profiles)
    aggregate_cutoffs = sorted({row["cutoff"] for profile in profiles for row in profile["cutoff_rows"]})
    aggregate_rows = []
    for cutoff in aggregate_cutoffs:
        rough_count = 0
        covered_prime_a = 0
        covered_prime_b = 0
        for profile in profiles:
            row_by_cutoff = {row["cutoff"]: row for row in profile["cutoff_rows"]}
            if cutoff in row_by_cutoff:
                rough_count += row_by_cutoff[cutoff]["rough_count"]
                covered_prime_a += profile["prime_a_fibers"]
                covered_prime_b += profile["prime_b_fibers"]
        aggregate_rows.append(
            {
                "cutoff": cutoff,
                "rough_count": rough_count,
                "covered_prime_a": covered_prime_a,
                "covered_prime_b": covered_prime_b,
                "rough_over_prime_a": safe_ratio(rough_count, covered_prime_a),
                "prime_b_over_rough": safe_ratio(covered_prime_b, rough_count),
            }
        )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_prime_b_sieve_router",
        "status": "prime_b_layer_reduced_to_rough_b_sieve_on_reciprocal_floor_sequence_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "sqrt_sieve_prime_b_identity_closed": exact_failures == 0,
        "rough_b_sieve_ledger_materialized": True,
        "uniform_rough_b_selberg_rankin_bound_proved": False,
        "rough_b_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "prime_a_fibers": prime_a_fibers,
        "prime_b_fibers": prime_b_fibers,
        "prime_b_over_prime_a": safe_ratio(prime_b_fibers, prime_a_fibers),
        "sqrt_sieve_exact_failure_count": exact_failures,
        "aggregate_cutoff_rows": aggregate_rows,
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "prime-b 层已经退化为 prime-a 半素数 incidence 多重序列上的粗数筛："
            "对每条候选 `(q,a,b)`，是否贡献最终 semiprime-u 只取决于 b 是否为素数，"
            "而这等价于 b 没有不超过 sqrt(b) 的素因子。样本中 sqrt(b) 筛与直接素性判断完全一致。"
            "因此剩余不再是纤维几何，而是 reciprocal-floor 生成的 b 多重序列的粗数幸存者上界；"
            "若粗幸存者无法由 Selberg/Rankin 支付，则必须输出低模粗数偏斜 PDEC/SAE。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha prime-b 粗数筛路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sqrt_sieve_prime_b_identity_closed={fmt_bool(result['sqrt_sieve_prime_b_identity_closed'])}",
        f"rough_b_sieve_ledger_materialized={fmt_bool(result['rough_b_sieve_ledger_materialized'])}",
        f"uniform_rough_b_selberg_rankin_bound_proved={fmt_bool(result['uniform_rough_b_selberg_rankin_bound_proved'])}",
        f"rough_b_pdec_excluded={fmt_bool(result['rough_b_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局账本",
        "",
        "| prime-a fibers | prime-b fibers | prime-b/prime-a | sqrt-sieve failures |",
        "| ---: | ---: | ---: | ---: |",
        (
            f"| {result['prime_a_fibers']} | {result['prime_b_fibers']} | "
            f"{fmt_float(result['prime_b_over_prime_a'])} | "
            f"{result['sqrt_sieve_exact_failure_count']} |"
        ),
        "",
        "## 2. 聚合粗数筛",
        "",
        "| cutoff | rough count | covered prime-a | covered prime-b | rough/prime-a | prime-b/rough |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["aggregate_cutoff_rows"]:
        lines.append(
            f"| {row['cutoff']} | {row['rough_count']} | {row['covered_prime_a']} | "
            f"{row['covered_prime_b']} | {fmt_float(row['rough_over_prime_a'])} | "
            f"{fmt_float(row['prime_b_over_rough'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | prime-a | prime-b | max b | sqrt max b | sqrt rough | failures |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['prime_a_fibers']} | {profile['prime_b_fibers']} | "
            f"{profile['max_b']} | {profile['sqrt_max_b']} | {profile['sqrt_sieve_rough_count']} | "
            f"{profile['sqrt_sieve_exact_failure_count']} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：在 prime-a incidence 多重序列上，`b` 为素数等价于 `sqrt(b)` 粗。",
            "- 已物化：多个低模 cutoff 下的 rough-b 幸存者账本。",
            "- 未闭合：对 reciprocal-floor 生成的 b 序列给出统一 Selberg/Rankin 粗数幸存者上界。",
            "- 未闭合：若低模粗数幸存者持续过多，需形成并排斥 PDEC/SAE。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
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
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "sqrt_sieve_prime_b_identity_closed": result["sqrt_sieve_prime_b_identity_closed"],
                "prime_a_fibers": result["prime_a_fibers"],
                "prime_b_fibers": result["prime_b_fibers"],
                "prime_b_over_prime_a": result["prime_b_over_prime_a"],
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
