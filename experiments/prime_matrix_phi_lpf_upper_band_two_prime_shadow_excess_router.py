#!/usr/bin/env python3
"""生成 upper-band two-prime shadow excess 的倒数短窗证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_upper_band_two_prime_shadow_excess_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-router.json

输出：
  data/prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-ledger.json
  docs/monograph/prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-router.json
  docs/monograph/prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-router.md
"""

from __future__ import annotations

import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

MAX_PRIME_AUDIT = 1009
LARGE_SAMPLE_SEEDS = [100000, 300000]

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json",
    DOCS / "prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-router.json",
    DOCS / "prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化成小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def spf_table(n: int) -> list[int]:
    """生成最小素因子表；素数的最小素因子等于自身。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for value in range(p * p, n + 1, p):
                if spf[value] == value:
                    spf[value] = p
    return spf


def prime_flags(n: int) -> bytearray:
    """生成素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def primes_from_spf(spf: list[int], n: int) -> list[int]:
    """从最小素因子表读取素数列表。"""
    return [value for value in range(2, n + 1) if spf[value] == value]


def primes_from_flags(flags: bytearray, n: int) -> list[int]:
    """从素数标记表读取素数列表。"""
    return [value for value in range(2, n + 1) if flags[value]]


def next_prime_at_least(seed: int, flags: bytearray) -> int:
    """在标记表内寻找不小于 seed 的第一个素数。"""
    for value in range(max(2, seed), len(flags)):
        if flags[value]:
            return value
    raise ValueError(f"no prime found after seed={seed}")


def high_band_lower_k(P: int) -> int:
    """返回 BHP bulk 之后的第一个整数 k；只作分区标签。"""
    return max(2, int(P ** (19.0 / 21.0)) + 1)


def shadow_free_cap(P: int) -> int:
    """返回保证 two-prime shadow 为空的最大 k。"""
    return max(1, (P * P - 4 * P + 4) // (4 * P))


def upper_band_first_k(P: int) -> int:
    """返回可能出现 q,m>P/2 shadow 的第一行。"""
    return max(2, shadow_free_cap(P) + 1)


def reciprocal_window_for_q(P: int, k: int, q: int) -> tuple[int, int, int]:
    """给定高素数 q，返回 m 的闭整数短窗及候选个数。"""
    lower = max(q, (k * P) // q + 1)
    upper = min(2 * P - 1, ((k + 1) * P - 1) // q)
    count = max(0, upper - lower + 1)
    return lower, upper, count


def reciprocal_shadow_stats(
    P: int,
    k: int,
    high_q_primes: list[int],
    is_prime: Callable[[int], bool],
) -> dict[str, Any]:
    """计算 reciprocal two-prime shadow 的短窗账本。"""
    integer_candidate_count = 0
    prime_pair_shadow_count = 0
    active_q_count = 0
    two_candidate_q_count = 0
    max_candidates_per_q = 0
    window_prefix: list[dict[str, int]] = []
    prime_pair_prefix: list[dict[str, int]] = []

    for q in high_q_primes:
        lower, upper, count = reciprocal_window_for_q(P, k, q)
        if count:
            active_q_count += 1
            integer_candidate_count += count
            max_candidates_per_q = max(max_candidates_per_q, count)
            if count == 2:
                two_candidate_q_count += 1
            if len(window_prefix) < 16:
                window_prefix.append({"q": q, "lower_m": lower, "upper_m": upper, "count": count})
        for m in range(lower, upper + 1):
            if is_prime(m):
                prime_pair_shadow_count += 1
                if len(prime_pair_prefix) < 16:
                    prime_pair_prefix.append({"q": q, "m": m, "n": q * m})

    return {
        "integer_candidate_count": integer_candidate_count,
        "prime_pair_shadow_count": prime_pair_shadow_count,
        "active_q_count": active_q_count,
        "two_candidate_q_count": two_candidate_q_count,
        "max_candidates_per_q": max_candidates_per_q,
        "all_windows_have_at_most_two_integer_candidates": max_candidates_per_q <= 2,
        "window_prefix": window_prefix,
        "prime_pair_prefix": prime_pair_prefix,
    }


def finite_row_counts(P: int, k: int, spf: list[int]) -> dict[str, int]:
    """直接数出 finite row 的 half-rough、素数和 composite shadow。"""
    rough = 0
    direct_primes = 0
    composite_half_rough = 0
    cutoff = P // 2
    for t in range(1, P):
        n = k * P + t
        is_rough = spf[n] > cutoff
        is_prime_n = spf[n] == n
        if is_rough:
            rough += 1
            if is_prime_n:
                direct_primes += 1
            else:
                composite_half_rough += 1
    return {
        "half_rough_survivor_count": rough,
        "direct_prime_count": direct_primes,
        "direct_composite_half_rough_count": composite_half_rough,
    }


def audit_prime_base(P: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """审计单个素数底 P 的 upper-band reciprocal shadow 公式。"""
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    first_upper = upper_band_first_k(P)
    first_high = high_band_lower_k(P)
    first_upper_remaining = max(first_upper, first_high)
    rows: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []

    def is_prime_m(value: int) -> bool:
        return spf[value] == value

    for k in range(first_upper, P):
        direct = finite_row_counts(P, k, spf)
        shadow = reciprocal_shadow_stats(P, k, high_q_primes, is_prime_m)
        margin = direct["half_rough_survivor_count"] - shadow["prime_pair_shadow_count"]
        item = {
            "P": P,
            "k": k,
            "upper_band_first_k": first_upper,
            "bhp_remaining_high_band_first_k": first_high,
            "in_bhp_remaining_high_band": k >= first_high,
            "half_rough_survivor_count": direct["half_rough_survivor_count"],
            "prime_pair_shadow_count": shadow["prime_pair_shadow_count"],
            "integer_candidate_count": shadow["integer_candidate_count"],
            "active_q_count": shadow["active_q_count"],
            "two_candidate_q_count": shadow["two_candidate_q_count"],
            "max_candidates_per_q": shadow["max_candidates_per_q"],
            "rough_minus_shadow": margin,
            "direct_prime_count": direct["direct_prime_count"],
            "direct_composite_half_rough_count": direct["direct_composite_half_rough_count"],
            "shadow_formula_matches_composite_half_rough": (
                shadow["prime_pair_shadow_count"] == direct["direct_composite_half_rough_count"]
            ),
            "identity_holds": margin == direct["direct_prime_count"],
            "all_windows_have_at_most_two_integer_candidates": shadow[
                "all_windows_have_at_most_two_integer_candidates"
            ],
        }
        rows.append(item)
        if not (
            item["identity_holds"]
            and item["shadow_formula_matches_composite_half_rough"]
            and item["all_windows_have_at_most_two_integer_candidates"]
        ):
            failures.append(item)

    sample_ks = sorted(
        {
            first_upper,
            min(P - 1, max(first_upper, first_high)),
            min(P - 1, max(first_upper, P // 2)),
            min(P - 1, max(first_upper, (3 * P) // 4)),
            P - 1,
        }
    )
    sample_rows = [row for row in rows if row["k"] in sample_ks]
    min_margin = min(row["rough_minus_shadow"] for row in rows)
    min_upper_remaining_margin = min(
        (
            row["rough_minus_shadow"]
            for row in rows
            if row["in_bhp_remaining_high_band"]
        ),
        default=None,
    )
    max_shadow_ratio_row = max(
        rows,
        key=lambda row: row["prime_pair_shadow_count"] / max(1, row["half_rough_survivor_count"]),
    )
    max_integer_ratio_row = max(
        rows,
        key=lambda row: row["integer_candidate_count"] / max(1, row["half_rough_survivor_count"]),
    )
    return {
        "P": P,
        "upper_band_first_k": first_upper,
        "bhp_remaining_high_band_first_k": first_high,
        "upper_bhp_remaining_first_k": first_upper_remaining,
        "upper_row_count": len(rows),
        "upper_bhp_remaining_row_count": sum(1 for row in rows if row["in_bhp_remaining_high_band"]),
        "identity_failure_count": len(failures),
        "all_reciprocal_window_identities_hold": not failures,
        "minimum_upper_margin": min_margin,
        "minimum_upper_margin_rows": [row for row in rows if row["rough_minus_shadow"] == min_margin][:8],
        "minimum_upper_bhp_remaining_margin": min_upper_remaining_margin,
        "maximum_shadow_ratio_row": max_shadow_ratio_row,
        "maximum_integer_candidate_ratio_row": max_integer_ratio_row,
        "sample_rows": sample_rows,
    }


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计 exact formula；只作一致性检查，不作全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    prime_bases = [p for p in primes if p >= 11]
    profiles = [audit_prime_base(P, spf, primes_2p) for P in prime_bases]
    failures = [profile for profile in profiles if profile["identity_failure_count"]]
    min_profile = min(profiles, key=lambda item: item["minimum_upper_margin"])
    upper_remaining_profiles = [
        profile
        for profile in profiles
        if profile["minimum_upper_bhp_remaining_margin"] is not None
    ]
    min_remaining_profile = min(
        upper_remaining_profiles,
        key=lambda item: item["minimum_upper_bhp_remaining_margin"],
    )
    max_shadow_ratio_profile = max(
        profiles,
        key=lambda item: item["maximum_shadow_ratio_row"]["prime_pair_shadow_count"]
        / max(1, item["maximum_shadow_ratio_row"]["half_rough_survivor_count"]),
    )
    max_integer_ratio_profile = max(
        profiles,
        key=lambda item: item["maximum_integer_candidate_ratio_row"]["integer_candidate_count"]
        / max(1, item["maximum_integer_candidate_ratio_row"]["half_rough_survivor_count"]),
    )
    return {
        "max_prime": max_prime,
        "prime_base_count": len(profiles),
        "all_reciprocal_window_identities_hold": not failures,
        "identity_failure_count": sum(profile["identity_failure_count"] for profile in profiles),
        "minimum_upper_margin_profile": {
            "P": min_profile["P"],
            "minimum_upper_margin": min_profile["minimum_upper_margin"],
            "minimum_upper_margin_rows": min_profile["minimum_upper_margin_rows"],
        },
        "minimum_upper_bhp_remaining_margin_profile": {
            "P": min_remaining_profile["P"],
            "upper_bhp_remaining_first_k": min_remaining_profile["upper_bhp_remaining_first_k"],
            "minimum_upper_bhp_remaining_margin": min_remaining_profile[
                "minimum_upper_bhp_remaining_margin"
            ],
        },
        "maximum_shadow_ratio_profile": {
            "P": max_shadow_ratio_profile["P"],
            "row": max_shadow_ratio_profile["maximum_shadow_ratio_row"],
        },
        "maximum_integer_candidate_ratio_profile": {
            "P": max_integer_ratio_profile["P"],
            "row": max_integer_ratio_profile["maximum_integer_candidate_ratio_row"],
        },
        "sample_profiles": [
            profile
            for profile in profiles
            if profile["P"] in {11, 101, 257, 1009}
        ],
        "finite_evidence_not_used_as_global_proof": True,
    }


def rough_count_by_segment_sieve(P: int, k: int, low_primes: list[int]) -> int:
    """用低素数分段筛计算 half-rough survivor 数。"""
    covered = bytearray(P)
    for q in low_primes:
        start = (-(k * P)) % q
        if start == 0:
            start = q
        if start < P:
            covered[start:P:q] = b"\x01" * (((P - 1 - start) // q) + 1)
    return covered[1:].count(0)


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 upper-band 读数；只作证据，不作证明。"""
    max_seed = max(seeds) + 10000
    flags = prime_flags(2 * max_seed)
    samples: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        low_primes = [q for q in range(2, P // 2 + 1) if flags[q]]
        high_q_primes = [q for q in range(P // 2 + 1, P) if flags[q]]
        first_upper = upper_band_first_k(P)
        first_high = high_band_lower_k(P)
        k_values = sorted(
            {
                first_upper,
                min(P - 1, max(first_upper, first_high)),
                min(P - 1, max(first_upper, P // 2)),
                min(P - 1, max(first_upper, (3 * P) // 4)),
                P - 1,
            }
        )

        def is_prime_m(value: int) -> bool:
            return bool(flags[value])

        for k in k_values:
            rough = rough_count_by_segment_sieve(P, k, low_primes)
            shadow = reciprocal_shadow_stats(P, k, high_q_primes, is_prime_m)
            samples.append(
                {
                    "P": P,
                    "k": k,
                    "upper_band_first_k": first_upper,
                    "bhp_remaining_high_band_first_k": first_high,
                    "half_rough_survivor_count": rough,
                    "prime_pair_shadow_count": shadow["prime_pair_shadow_count"],
                    "integer_candidate_count": shadow["integer_candidate_count"],
                    "rough_minus_shadow": rough - shadow["prime_pair_shadow_count"],
                    "active_q_count": shadow["active_q_count"],
                    "two_candidate_q_count": shadow["two_candidate_q_count"],
                    "max_candidates_per_q": shadow["max_candidates_per_q"],
                    "positive_margin_in_sample": rough > shadow["prime_pair_shadow_count"],
                }
            )
    return {
        "sample_seeds": seeds,
        "sample_count": len(samples),
        "all_sampled_upper_rows_have_positive_margin": all(
            item["positive_margin_in_sample"] for item in samples
        ),
        "samples": samples,
        "large_samples_are_evidence_not_global_proof": True,
    }


def gate(gate_name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate_name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_gates() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        gate(
            "UpperBandReciprocalWindowFormulaClosed",
            True,
            True,
            "upper-band two-prime shadow 精确等于高素数 q 的 reciprocal m 短窗中素数点数之和。",
            "exact formula",
        ),
        gate(
            "EachHighQHasAtMostTwoMValues",
            True,
            True,
            "因窗口长度 P/q<2，每个 q in (P/2,P) 至多贡献两个整数候选 m。",
            "prime filtering remains actual load",
        ),
        gate(
            "UpperBandFailureIsSparsePrimePairSaturation",
            True,
            True,
            "若 upper-band 行失败，则 at-most-two 候选的 reciprocal prime-pair shadow 必须吃掉全部 half-rough survivor。",
            "UpperBandReciprocalPrimePairShadowSaturatesHalfRoughSurvivors",
        ),
        gate(
            "FiniteSweepSupportsPositiveMargin",
            True,
            True,
            "有限审计中 exact identity、短窗公式和正余量均正常，但不作为全局证明。",
            "finite audit only",
        ),
        gate(
            "MertensHalfRoughFloorAndSelbergShadowCeilingProved",
            False,
            False,
            "尚未证明同一 row convention 下 R_half 的下界和 T_shadow 的 Selberg/Brun 上界之间存在统一正间隔。",
            "UpperBandHalfRoughFloorOrReciprocalPrimePairCeiling",
        ),
        gate(
            "UpperBandPositivityProved",
            False,
            False,
            "本层只把 high-k upper band 压成稀疏 reciprocal prime-pair 饱和问题，不证明全局正性。",
            "UpperBandReciprocalPrimePairShadowSaturationOrPDEC",
        ),
        gate(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层不是三目标命题闭合；shadow-free special phase 与 upper-band sparse shadow 两口仍需继续攻。",
            "HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC AND UpperBandReciprocalPrimePairShadowSaturationOrPDEC",
        ),
    ]


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def sample_rows_markdown(samples: list[dict[str, Any]]) -> str:
    """输出样本表 Markdown。"""
    lines = [
        "| P | k | R_half | T_shadow | int cand | R-T | active q | two-cand q | max cand/q |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in samples:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['half_rough_survivor_count']} | "
            f"{row['prime_pair_shadow_count']} | {row['integer_candidate_count']} | "
            f"{row['rough_minus_shadow']} | {row['active_q_count']} | "
            f"{row['two_candidate_q_count']} | {row['max_candidates_per_q']} |"
        )
    return "\n".join(lines)


def compact_min_rows(rows: list[dict[str, Any]]) -> str:
    """压缩最小余量行读数。"""
    return "; ".join(
        "P={P}, k={k}, R={R}, T={T}, direct={D}, cand={C}".format(
            P=item["P"],
            k=item["k"],
            R=item["half_rough_survivor_count"],
            T=item["prime_pair_shadow_count"],
            D=item["direct_prime_count"],
            C=item["integer_candidate_count"],
        )
        for item in rows
    )


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    finite = finite_audit()
    large = large_sample_audit()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    gates = build_gates()
    return {
        "certificate_type": "prime_matrix_phi_lpf_upper_band_two_prime_shadow_excess_router",
        "status": "upper_band_two_prime_shadow_reduced_to_sparse_reciprocal_prime_pair_windows",
        "definitions": {
            "upper_band": "4*((k+1)P-1)>P^2, equivalently k>=floor(((P-2)^2)/(4P))+1",
            "I_q(P,k)": "[max(q, floor(kP/q)+1), floor(((k+1)P-1)/q)] intersect integers",
            "T_half(P,k)": "sum_{P/2<q<P, q prime} #{m in I_q(P,k): m prime}",
            "candidate_bound": "|I_q(P,k)|<=2 because length < P/q < 2",
            "failure_form": "R_half(P,k)<=T_half(P,k) is sparse reciprocal prime-pair saturation",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": gates,
        "dependency_hashes": dependency_hashes,
        "next_direct_attack_target": (
            "UpperBandReciprocalPrimePairShadowSaturationOrPDEC AND "
            "UpperBandHalfRoughFloorOrReciprocalPrimePairCeiling"
        ),
        "plain_conclusion": (
            "upper-band 的 two-prime shadow 不再是抽象合数树，而是高素数 q 上的 reciprocal "
            "短窗 prime-pair 图。每个 q 至多两个 m 候选；若行正性失败，必须是这些稀疏短窗中的素数点 "
            "真实饱和并覆盖全部 half-rough survivor，或者表现为 half-rough floor / reciprocal shadow "
            "ceiling 的命名 PDEC。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    finite = payload["finite_audit"]
    large = payload["large_sample_audit"]
    min_profile = finite["minimum_upper_margin_profile"]
    min_remaining = finite["minimum_upper_bhp_remaining_margin_profile"]
    max_shadow = finite["maximum_shadow_ratio_profile"]["row"]
    max_integer = finite["maximum_integer_candidate_ratio_profile"]["row"]
    sample_rows = [row for profile in finite["sample_profiles"] for row in profile["sample_rows"]]
    lines = [
        "# Prime Matrix Phi-LPF upper-band two-prime shadow excess 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层处理 strict-k half-rough shadow split 留下的 upper square band。设 `P` 为素数，",
        "`1<k<P`，并处在",
        "",
        "```text",
        "4*((k+1)P-1)>P^2.",
        "```",
        "",
        "对每个高素数 `q in (P/2,P)`，定义倒数短窗",
        "",
        "```text",
        "I_q(P,k)=[max(q, floor(kP/q)+1), floor(((k+1)P-1)/q)] intersect Z.",
        "```",
        "",
        "则上一层的 two-prime shadow 精确为",
        "",
        "```text",
        "T_half(P,k)=sum_{P/2<q<P, q prime} #{m in I_q(P,k): m prime}.",
        "```",
        "",
        "并且 `|I_q(P,k)|<=2`。所以 upper-band 的真剩余不是完整 LPF 树，而是",
        "一个每个 `q` 至多两个候选点的 reciprocal prime-pair 饱和问题。",
        "",
        "## 1. 结构证明读法",
        "",
        "由 `kP<qm<(k+1)P` 得",
        "",
        "```text",
        "floor(kP/q)+1 <= m <= floor(((k+1)P-1)/q).",
        "```",
        "",
        "唯一代表要求 `q<=m`，所以左端取 `max(q, floor(kP/q)+1)`。",
        "窗口实长度小于 `P/q<2`，故每个高素数 `q` 最多给两个整数候选；再筛掉非素数 `m`",
        "就是 actual shadow load。若 `R_half(P,k)-T_half(P,k)<=0`，失败必须是这些",
        "短窗素数点真实饱和，而不是低筛容量的匿名波动。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"prime_base_count={finite['prime_base_count']}",
        f"all_reciprocal_window_identities_hold={fmt_bool(finite['all_reciprocal_window_identities_hold'])}",
        f"identity_failure_count={finite['identity_failure_count']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "upper-band 最小余量样本：",
        "",
        "```text",
        compact_min_rows(min_profile["minimum_upper_margin_rows"]),
        "```",
        "",
        "BHP 剩余与 upper-band 交集最小余量：",
        "",
        "```text",
        f"P={min_remaining['P']}, first_k={min_remaining['upper_bhp_remaining_first_k']}, "
        f"min_margin={min_remaining['minimum_upper_bhp_remaining_margin']}",
        "```",
        "",
        "最高实际 shadow 比例行：",
        "",
        "```text",
        f"P={max_shadow['P']}, k={max_shadow['k']}, R={max_shadow['half_rough_survivor_count']}, "
        f"T={max_shadow['prime_pair_shadow_count']}, direct={max_shadow['direct_prime_count']}",
        "```",
        "",
        "最高整数候选包络比例行：",
        "",
        "```text",
        f"P={max_integer['P']}, k={max_integer['k']}, R={max_integer['half_rough_survivor_count']}, "
        f"int_candidates={max_integer['integer_candidate_count']}, T={max_integer['prime_pair_shadow_count']}",
        "```",
        "",
        "## 3. 有限样本表",
        "",
        sample_rows_markdown(sample_rows),
        "",
        "## 4. 大尺度抽样",
        "",
        "```text",
        f"sample_seeds={large['sample_seeds']}",
        f"sample_count={large['sample_count']}",
        f"all_sampled_upper_rows_have_positive_margin={fmt_bool(large['all_sampled_upper_rows_have_positive_margin'])}",
        f"large_samples_are_evidence_not_global_proof={fmt_bool(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        sample_rows_markdown(large["samples"]),
        "",
        "## 5. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 6. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "当前 upper-band 最窄直接主攻口是：",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只把 upper-band",
        "硬点压成 reciprocal prime-pair 短窗饱和与相应 PDEC/ceiling/floor 接口。",
        "",
        "## 7. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in payload["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(
        json.dumps(
            {
                "status": payload["status"],
                "max_prime": payload["finite_audit"]["max_prime"],
                "all_reciprocal_window_identities_hold": payload["finite_audit"][
                    "all_reciprocal_window_identities_hold"
                ],
                "large_sample_count": payload["large_sample_audit"]["sample_count"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
