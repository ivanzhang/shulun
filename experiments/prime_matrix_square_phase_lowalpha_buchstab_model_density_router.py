#!/usr/bin/env python3
"""审计 omega_B 加权前驱区间的 Buchstab 模型密度。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_buchstab_model_density_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-model-density-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-model-density-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-model-density-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-model-density-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-model-density-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31
EULER_GAMMA = 0.5772156649015329

NEXT_TARGET = "BuchstabModelConstantLedgerOrLocalDensitySpikePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-block-multiplicity-router.json",
    "prime-matrix-square-phase-lowalpha-predecessor-density-ledger.json",
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


def factor_multiset(n: int, trial_primes: list[int]) -> list[int]:
    """返回 n 的素因子重数列表，按从小到大排列。"""
    value = n
    factors: list[int] = []
    for prime in trial_primes:
        if prime * prime > value:
            break
        while value % prime == 0:
            factors.append(prime)
            value //= prime
    if value > 1:
        factors.append(value)
    return factors


def cutoffs_for_p(p: int, base_d: int = BASE_D) -> list[int]:
    """生成 dyadic cutoff。"""
    y = max(2, math.floor(p / math.e))
    cuts = [base_d]
    value = base_d
    while value < y:
        value *= 2
        cuts.append(min(value, y))
    return sorted(set(cuts))


def factor_depth_bound(p: int, z: int) -> int:
    """计算 z-rough cofactor 最大素因子个数上界。"""
    upper = (p * p + p - 1) / z
    depth = 0
    power = 1.0
    while power < upper:
        depth += 1
        power *= z + 1
    return max(0, depth - 1)


def delete_residue(allowed: bytearray, p: int, p2: int, q: int) -> None:
    """从 allowed 中删除 k == -P^2 mod q 的列。"""
    residue = (-p2) % q
    start = residue if residue != 0 else q
    if start < p:
        allowed[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)


def crossing_from_factors(p: int, q: int, factors: list[int]) -> tuple[int, int]:
    """返回 crossing 前驱 `D_-` 与剩余 `u`。"""
    prefix = q
    for idx, factor in enumerate(factors):
        before = prefix
        prefix *= factor
        if prefix > p:
            tail = 1
            for rest in factors[idx:]:
                tail *= rest
            return before, tail
    return prefix, 1


def interval_integer_capacity(p2: int, p: int, d_minus: int) -> int:
    """返回 `P^2/D < u <= (P^2+P-1)/D` 的整数容量。"""
    return max(0, (p2 + p - 1) // d_minus - p2 // d_minus)


def block_omega(d_minus: int, block_primes: list[int]) -> int:
    """计算 `D_-` 中可作为原始块素数 q 的不同因子数。"""
    return sum(1 for q in block_primes if d_minus % q == 0)


class BuchstabTable:
    """数值 Buchstab 函数表。"""

    def __init__(self, max_s: float, step: float = 0.001) -> None:
        self.step = step
        self.max_s = max(2.0, max_s + 0.01)
        self.values = self._build()

    def _build(self) -> list[float]:
        size = int(self.max_s / self.step) + 3
        values = [0.0] * size
        f_values = [0.0] * size
        delay_steps = int(round(1.0 / self.step))
        for idx in range(1, size):
            s = idx * self.step
            if s < 1.0:
                values[idx] = 0.0
                f_values[idx] = 0.0
            elif s <= 2.0:
                values[idx] = 1.0 / s
                f_values[idx] = 1.0
            else:
                prev_f = f_values[idx - 1]
                delayed_idx = max(1, idx - delay_steps - 1)
                delayed_s = delayed_idx * self.step
                delayed = 1.0 / delayed_s if delayed_s <= 2.0 else values[delayed_idx]
                f_values[idx] = prev_f + self.step * delayed
                values[idx] = f_values[idx] / s
        return values

    def value(self, s: float) -> float:
        """线性插值读取 omega(s)。"""
        if s < 1.0:
            return 0.0
        if s <= 2.0:
            return 1.0 / s
        pos = min(s / self.step, len(self.values) - 1.001)
        lo = int(pos)
        frac = pos - lo
        return self.values[lo] * (1.0 - frac) + self.values[lo + 1] * frac


def model_density(p: int, d_minus: int, table: BuchstabTable) -> tuple[float, float, float]:
    """返回 `(H, s, model_density)`。"""
    h = p / d_minus
    if h <= 2.0:
        return h, 0.0, 1.0
    x = (p * p) / d_minus
    s = math.log(x) / math.log(h)
    density = math.exp(-EULER_GAMMA) * table.value(s) / math.log(h)
    return h, s, min(1.0, max(0.0, density))


def h_bucket(h: float) -> str:
    """按 H=P/D_- 分桶。"""
    if h < 2:
        return "H0:<2"
    if h < 4:
        return "H1:[2,4)"
    if h < 8:
        return "H2:[4,8)"
    if h < 16:
        return "H3:[8,16)"
    if h < 32:
        return "H4:[16,32)"
    if h < 64:
        return "H5:[32,64)"
    if h < 128:
        return "H6:[64,128)"
    return "H7:>=128"


def register_bucket(buckets: dict[str, dict[str, float]], key: str, hits: int, weighted: int, model: float) -> None:
    """登记模型桶。"""
    row = buckets.setdefault(key, {"hits": 0.0, "weighted_capacity": 0.0, "model": 0.0, "predecessors": 0.0})
    row["hits"] += hits
    row["weighted_capacity"] += weighted
    row["model"] += model
    row["predecessors"] += 1


def finalize_buckets(buckets: dict[str, dict[str, float]]) -> dict[str, dict[str, float]]:
    """补充桶密度和比值。"""
    result: dict[str, dict[str, float]] = {}
    for key, row in sorted(buckets.items()):
        weighted = row["weighted_capacity"]
        model = row["model"]
        result[key] = {
            "hits": row["hits"],
            "weighted_capacity": weighted,
            "model": model,
            "predecessors": row["predecessors"],
            "weighted_density": 0.0 if weighted == 0 else row["hits"] / weighted,
            "actual_over_model": None if model == 0 else row["hits"] / model,
        }
    return result


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    allowed: bytearray,
    block_primes: list[int],
    trial_primes: list[int],
    table: BuchstabTable,
) -> dict[str, Any]:
    """审计一个 low-alpha block 的 Buchstab 模型密度。"""
    p2 = p * p
    predecessor_hits: dict[int, int] = {}
    predecessor_capacity: dict[int, int] = {}
    predecessor_omega: dict[int, int] = {}
    for q in block_primes:
        left = p2 // q + 1
        right = (p2 + p - 1) // q
        for m in range(left, right + 1):
            k = q * m - p2
            if not (1 <= k < p and allowed[k]):
                continue
            d_minus, _u = crossing_from_factors(p, q, factor_multiset(m, trial_primes))
            predecessor_hits[d_minus] = predecessor_hits.get(d_minus, 0) + 1
            if d_minus not in predecessor_capacity:
                predecessor_capacity[d_minus] = interval_integer_capacity(p2, p, d_minus)
                predecessor_omega[d_minus] = block_omega(d_minus, block_primes)
    buckets: dict[str, dict[str, float]] = {}
    total_hits = 0
    total_weighted = 0
    total_model = 0.0
    top_model_excess = None
    top_hit_predecessor = None
    for d_minus, hits in predecessor_hits.items():
        capacity = predecessor_capacity[d_minus]
        omega = predecessor_omega[d_minus]
        weighted = capacity * omega
        h, s, density = model_density(p, d_minus, table)
        model = weighted * density
        total_hits += hits
        total_weighted += weighted
        total_model += model
        row = {
            "d_minus": d_minus,
            "hits": hits,
            "weighted_capacity": weighted,
            "h": h,
            "s": s,
            "model_density": density,
            "model": model,
            "actual_over_model": None if model == 0 else hits / model,
        }
        if top_model_excess is None or (
            row["actual_over_model"] is not None
            and row["actual_over_model"] > top_model_excess["actual_over_model"]
        ):
            top_model_excess = row
        if top_hit_predecessor is None or hits > top_hit_predecessor["hits"]:
            top_hit_predecessor = row
        register_bucket(buckets, h_bucket(h), hits, weighted, model)
    bucket_rows = finalize_buckets(buckets)
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "cofactor_hits": total_hits,
        "active_predecessor_count": len(predecessor_hits),
        "omega_weighted_capacity_sum": total_weighted,
        "buchstab_model_sum": total_model,
        "actual_over_buchstab_model": None if total_model == 0 else total_hits / total_model,
        "weighted_density": None if total_weighted == 0 else total_hits / total_weighted,
        "top_model_excess_predecessor": top_model_excess,
        "top_hit_predecessor": top_hit_predecessor,
        "h_bucket_rows": bucket_rows,
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int], table: BuchstabTable) -> dict[str, Any]:
    """审计一个 P 的 Buchstab 模型密度。"""
    p2 = p * p
    cutoffs = cutoffs_for_p(p)
    allowed = bytearray(b"\x01") * p
    allowed[0] = 0
    prime_index = 0
    rows = []
    for cutoff in cutoffs:
        previous = 0 if not rows else rows[-1].get("cutoff", 0)
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous >= BASE_D and factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, allowed, block_primes, trial_primes, table))
        while prime_index < len(primes) and primes[prime_index] <= cutoff:
            delete_residue(allowed, p, p2, primes[prime_index])
            prime_index += 1
        if not rows or rows[-1].get("cutoff") != cutoff:
            rows.append({"p": p, "previous_cutoff": previous, "cutoff": cutoff, "skipped": True})
    low_rows = [row for row in rows if not row.get("skipped")]
    worst = max(low_rows, key=lambda item: item["cofactor_hits"], default=None)
    model_sum = sum(row["buchstab_model_sum"] for row in low_rows)
    total_hits = sum(row["cofactor_hits"] for row in low_rows)
    return {
        "p": p,
        "lowalpha_row_count": len(low_rows),
        "total_hits": total_hits,
        "buchstab_model_sum": model_sum,
        "actual_over_buchstab_model": None if model_sum == 0 else total_hits / model_sum,
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_buchstab_model_density_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行审计。"""
    max_p = max(p_list)
    table = BuchstabTable(max_s=20.0)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = sieve_bool(max(trial_limit, max_p))
    trial_primes = primes_from_flags(flags, trial_limit)
    profiles = []
    for p in p_list:
        primes = primes_from_flags(flags, max(2, math.floor(p / math.e)))
        profiles.append(audit_p(p, primes, trial_primes, table))
    rows = [row for profile in profiles for row in profile["rows"]]
    worst = max(rows, key=lambda item: item["cofactor_hits"], default=None)
    total_hits = sum(profile["total_hits"] for profile in profiles)
    total_model = sum(profile["buchstab_model_sum"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_buchstab_model_density_router",
        "status": "omega_weighted_density_reduced_to_buchstab_model_constant_or_spike_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "buchstab_model_ledger_materialized": True,
        "buchstab_model_constant_bound_proved": False,
        "local_density_spike_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "total_lowalpha_hits": total_hits,
        "total_buchstab_model": total_model,
        "total_actual_over_buchstab_model": None if total_model == 0 else total_hits / total_model,
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "`omega_B(D_-)` 加权密度已接到标准 Buchstab 模型账本："
            "每个前驱的短区间长度约为 `H=P/D_-`，粗阈值也是 `H`，"
            "模型密度为 `e^{-gamma} omega(s)/log H`。本步只给出常数账本和尖峰定位，"
            "还没有证明全局常数上界或排除局部密度尖峰 PDEC。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha Buchstab 模型密度路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"buchstab_model_ledger_materialized={fmt_bool(result['buchstab_model_ledger_materialized'])}",
        f"buchstab_model_constant_bound_proved={fmt_bool(result['buchstab_model_constant_bound_proved'])}",
        f"local_density_spike_pdec_excluded={fmt_bool(result['local_density_spike_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 总体模型",
        "",
        "| hits | Buchstab model | actual/model |",
        "| ---: | ---: | ---: |",
        f"| {result['total_lowalpha_hits']} | {result['total_buchstab_model']:.6f} | {result['total_actual_over_buchstab_model']:.6f} |",
        "",
        "## 2. 最坏 low-alpha 块",
        "",
        "| P | block | hits | model | actual/model | weighted density | top hit D_- | top model excess D_- |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['cofactor_hits']} | {worst['buchstab_model_sum']:.6f} | "
            f"{worst['actual_over_buchstab_model']:.6f} | {worst['weighted_density']:.6f} | "
            f"`{worst['top_hit_predecessor']}` | `{worst['top_model_excess_predecessor']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low blocks | hits | model | actual/model | worst block |",
            "| ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['total_hits']} | "
            f"{profile['buchstab_model_sum']:.6f} | {profile['actual_over_buchstab_model']:.6f} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：`omega_B(D_-)` 加权密度的 Buchstab 模型账本。",
            "- 未闭合：证明模型常数上界足以支付全部 low-alpha 负载。",
            "- 未闭合：若某前驱/尺度桶超过模型常数，需证明其触发 PDEC。",
            f"- 下一目标：`{NEXT_TARGET}`。",
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
                "buchstab_model_ledger_materialized": result["buchstab_model_ledger_materialized"],
                "total_actual_over_buchstab_model": result["total_actual_over_buchstab_model"],
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
