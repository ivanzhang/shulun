#!/usr/bin/env python3
"""审计 dyadic 一阶负载与互补因子短区间的精确对偶。

用法示例：
  python3 experiments/prime_matrix_square_phase_dyadic_first_moment_cofactor_duality.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-dyadic-first-moment-cofactor-duality.json

输出：
  docs/monograph/prime-matrix-square-phase-dyadic-first-moment-cofactor-duality.json
  docs/monograph/prime-matrix-square-phase-dyadic-first-moment-cofactor-duality.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-dyadic-first-moment-cofactor-duality.json"
OUT_MD = DOCS / "prime-matrix-square-phase-dyadic-first-moment-cofactor-duality.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

COFACTOR_TARGET = "DyadicShortCofactorRoughIntervalLoadBoundOrPDEC"
FIRST_MOMENT = "DyadicSquarePhaseFirstMomentLoadPDEC"

SOURCE_FILES = [
    "prime-matrix-square-phase-dyadic-first-moment-ledger.json",
    "prime-matrix-square-phase-dyadic-deletion-excess-split-router.json",
]


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int) -> list[int]:
    """提取不超过 limit 的素数。"""
    return [idx for idx in range(2, min(limit + 1, len(flags))) if flags[idx]]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def is_prime64(n: int) -> bool:
    """确定性 Miller-Rabin，适用于本项目的 64 位正整数。"""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in small_primes:
        if n == prime:
            return True
        if n % prime == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 3, 5, 7, 11, 13, 17]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def cutoffs_for_p(p: int, base_d: int = BASE_D) -> list[int]:
    """生成 dyadic cutoff。"""
    y = max(2, math.floor(p / math.e))
    cuts = [base_d]
    value = base_d
    while value < y:
        value *= 2
        cuts.append(min(value, y))
    return sorted(set(cuts))


def delete_residue(allowed: bytearray, p: int, p2: int, q: int) -> None:
    """从 allowed 中删除 k == -P^2 mod q 的列。"""
    residue = (-p2) % q
    start = residue if residue != 0 else q
    if start < p:
        allowed[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)


def count_hits_by_residue(allowed: bytearray, p: int, p2: int, q: int) -> int:
    """用列相位计数一阶命中。"""
    residue = (-p2) % q
    start = residue if residue != 0 else q
    if start >= p:
        return 0
    return sum(allowed[start:p:q])


def cofactor_hits_for_q(allowed: bytearray, p: int, p2: int, q: int) -> tuple[int, int, int, int]:
    """用互补因子短区间计数 q 的命中。

    返回：(命中数, 区间容量, 素互补数, 复合互补数)。
    """
    left = p2 // q + 1
    right = (p2 + p - 1) // q
    hit = 0
    prime_hit = 0
    composite_hit = 0
    for m in range(left, right + 1):
        k = q * m - p2
        if 1 <= k < p and allowed[k]:
            hit += 1
            if is_prime64(m):
                prime_hit += 1
            else:
                composite_hit += 1
    return hit, max(0, right - left + 1), prime_hit, composite_hit


def audit_p(p: int, primes: list[int]) -> dict[str, Any]:
    """审计一个 P。"""
    p2 = p * p
    y = max(2, math.floor(p / math.e))
    cutoffs = cutoffs_for_p(p)
    allowed = bytearray(b"\x01") * p
    allowed[0] = 0
    prime_index = 0
    rows = []
    mismatch_rows = []
    for cutoff in cutoffs:
        previous_cutoff = 0 if not rows else rows[-1]["cutoff"]
        block_primes = [q for q in primes if previous_cutoff < q <= cutoff]
        phase_hits = 0
        cofactor_hits = 0
        cofactor_capacity = 0
        prime_cofactor_hits = 0
        composite_cofactor_hits = 0
        active_q_count = 0
        max_q_hit = 0
        max_q_capacity = 0
        for q in block_primes:
            phase = count_hits_by_residue(allowed, p, p2, q)
            cof, cap, prime_hit, composite_hit = cofactor_hits_for_q(allowed, p, p2, q)
            if phase != cof:
                mismatch_rows.append({"p": p, "cutoff": cutoff, "q": q, "phase": phase, "cofactor": cof})
            phase_hits += phase
            cofactor_hits += cof
            cofactor_capacity += cap
            prime_cofactor_hits += prime_hit
            composite_cofactor_hits += composite_hit
            if cof:
                active_q_count += 1
            max_q_hit = max(max_q_hit, cof)
            max_q_capacity = max(max_q_capacity, cap)
        after = bytearray(allowed)
        while prime_index < len(primes) and primes[prime_index] <= cutoff:
            delete_residue(after, p, p2, primes[prime_index])
            prime_index += 1
        rows.append(
            {
                "p": p,
                "previous_cutoff": previous_cutoff,
                "cutoff": cutoff,
                "block_prime_count": len(block_primes),
                "phase_hits": phase_hits,
                "cofactor_hits": cofactor_hits,
                "cofactor_identity_ok": phase_hits == cofactor_hits,
                "cofactor_capacity": cofactor_capacity,
                "active_q_count": active_q_count,
                "prime_cofactor_hits": prime_cofactor_hits,
                "composite_cofactor_hits": composite_cofactor_hits,
                "prime_cofactor_share": None if cofactor_hits == 0 else prime_cofactor_hits / cofactor_hits,
                "max_q_hit": max_q_hit,
                "max_q_capacity": max_q_capacity,
                "hit_density_in_capacity": None if cofactor_capacity == 0 else cofactor_hits / cofactor_capacity,
            }
        )
        allowed = after
    moving_rows = [row for row in rows if row["previous_cutoff"] >= BASE_D]
    worst = max(moving_rows, key=lambda item: item["cofactor_hits"])
    return {
        "p": p,
        "y": y,
        "row_count": len(rows),
        "moving_row_count": len(moving_rows),
        "mismatch_count": len(mismatch_rows),
        "mismatch_rows": mismatch_rows[:10],
        "worst_by_cofactor_hits": worst,
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_dyadic_first_moment_cofactor_duality.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行审计。"""
    limit = max(max(p_list), 2)
    flags = sieve_bool(limit)
    profiles = []
    for p in p_list:
        primes = primes_from_flags(flags, max(2, math.floor(p / math.e)))
        profiles.append(audit_p(p, primes))
    all_rows = [
        row
        for profile in profiles
        for row in profile["rows"]
        if row["previous_cutoff"] >= BASE_D
    ]
    mismatch_count = sum(profile["mismatch_count"] for profile in profiles)
    worst = max(all_rows, key=lambda item: item["cofactor_hits"])
    worst_density = max(
        [row for row in all_rows if row["hit_density_in_capacity"] is not None],
        key=lambda item: item["hit_density_in_capacity"],
    )
    return {
        "certificate_type": "prime_matrix_square_phase_dyadic_first_moment_cofactor_duality",
        "status": "dyadic_first_moment_exactly_reduced_to_short_cofactor_rough_intervals_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "cofactor_duality_identity_checked": mismatch_count == 0,
        "cofactor_duality_mismatch_count": mismatch_count,
        "short_cofactor_interval_bound_proved": False,
        "row_column_unconditional_closed": False,
        "p_list": p_list,
        "profiles": profiles,
        "worst_by_cofactor_hits": worst,
        "worst_by_hit_density": worst_density,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": COFACTOR_TARGET,
        "previous_target": FIRST_MOMENT,
        "plain_conclusion": (
            "dyadic 一阶负载 `H_B` 与互补因子短区间计数完全相同："
            "`q` 命中进入块幸存列 `k` 当且仅当存在 `m` 使 `P^2+k=q*m`，"
            "且 `m` 位于 `(P^2/q,(P^2+P)/q]`。由于 `k` 已避开 `<=z` 的负平方相位，"
            "该 `m` 也没有 `<=z` 的素因子。当前已核验该对偶身份，下一硬点是这些短 cofactor rough 区间的负载上界或 PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase dyadic 一阶负载 cofactor 对偶账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cofactor_duality_identity_checked={fmt_bool(result['cofactor_duality_identity_checked'])}",
        f"cofactor_duality_mismatch_count={result['cofactor_duality_mismatch_count']}",
        f"short_cofactor_interval_bound_proved={fmt_bool(result['short_cofactor_interval_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 对偶恒等式",
        "",
        "对进入块幸存集 `S_z` 与 dyadic 块 `B=(z,z']`，",
        "",
        "```text",
        "H_B=sum_{q in B} |S_z cap {-P^2 mod q}|",
        "   =sum_{q in B} #{m: P^2/q < m <= (P^2+P-1)/q, q*m-P^2 in S_z}.",
        "```",
        "",
        "若 `q*m-P^2 in S_z`，则 `m` 没有 `<=z` 的素因子；否则对应小素数也会整除 `P^2+k`，与 `k in S_z` 矛盾。",
        "",
        "## 2. 极值",
        "",
        "| item | P | block | cofactor hits | capacity | hit density | prime share | max q hit | max q capacity |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for label, row in [
        ("worst_hits", result["worst_by_cofactor_hits"]),
        ("worst_density", result["worst_by_hit_density"]),
    ]:
        prime_share = row["prime_cofactor_share"]
        density = row["hit_density_in_capacity"]
        lines.append(
            f"| `{label}` | {row['p']} | `({row['previous_cutoff']},{row['cutoff']}]` | "
            f"{row['cofactor_hits']} | {row['cofactor_capacity']} | "
            f"{0.0 if density is None else density:.6f} | "
            f"{0.0 if prime_share is None else prime_share:.6f} | "
            f"{row['max_q_hit']} | {row['max_q_capacity']} |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的最大 cofactor 负载",
            "",
            "| P | y | block | cofactor hits | prime hits | composite hits | prime share | capacity | density |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_by_cofactor_hits"]
        prime_share = row["prime_cofactor_share"]
        density = row["hit_density_in_capacity"]
        lines.append(
            f"| {profile['p']} | {profile['y']} | `({row['previous_cutoff']},{row['cutoff']}]` | "
            f"{row['cofactor_hits']} | {row['prime_cofactor_hits']} | "
            f"{row['composite_cofactor_hits']} | {0.0 if prime_share is None else prime_share:.6f} | "
            f"{row['cofactor_capacity']} | {0.0 if density is None else density:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            f"- 已闭合：`{FIRST_MOMENT}` 的 cofactor 对偶身份。",
            f"- 未闭合：`{COFACTOR_TARGET}`，即短 cofactor interval 的 rough 负载上界，或其失败进入 PDEC/SAE。",
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
                "cofactor_duality_mismatch_count": result["cofactor_duality_mismatch_count"],
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
