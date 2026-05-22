#!/usr/bin/env python3
"""生成 Phi-LPF punctured endpoint parity capacity 证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_punctured_endpoint_parity_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.json

输出：
  data/prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-ledger.json
  docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.json
  docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.md
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

SLUG = "prime-matrix-phi-lpf-punctured-endpoint-parity-capacity"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

MAX_PRIME_AUDIT = 1009
LARGE_SAMPLE_SEEDS = [100000, 300000]

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-router.json",
    DOCS / "prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def spf_table(n: int) -> list[int]:
    """生成最小素因子表。"""
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
    """从 SPF 表读取素数。"""
    return [value for value in range(2, n + 1) if spf[value] == value]


def primes_from_flags(flags: bytearray, n: int) -> list[int]:
    """从素数标记读取素数。"""
    return [value for value in range(2, min(n, len(flags) - 1) + 1) if flags[value]]


def next_prime_after_half(P: int, primes_2p: list[int]) -> int:
    """返回大于 P/2 的第一个素数。"""
    for q in primes_2p:
        if q > P // 2:
            return q
    raise ValueError(f"missing half cutoff prime for P={P}")


def next_prime_at_least(seed: int, flags: bytearray) -> int:
    """在标记表内寻找不小于 seed 的第一个素数。"""
    for value in range(max(2, seed), len(flags)):
        if flags[value]:
            return value
    raise ValueError(f"no prime found after seed={seed}")


def shadow_free_cap(P: int) -> int:
    """返回 shadow-free 条件允许的最大 k。"""
    return max(1, (P * P - 4 * P + 4) // (4 * P))


def upper_band_first_k(P: int) -> int:
    """返回 upper square band 第一行。"""
    return max(2, shadow_free_cap(P) + 1)


def high_band_lower_k(P: int) -> int:
    """返回 BHP bulk 后的第一个整数 k；只作分区标签。"""
    return max(2, int(P ** (19.0 / 21.0)) + 1)


def reciprocal_window_for_q(P: int, k: int, q: int) -> tuple[int, int]:
    """返回固定 q 的 m 候选闭区间。"""
    lower = max(q, (k * P) // q + 1)
    upper = min(2 * P - 1, ((k + 1) * P - 1) // q)
    return lower, upper


def finite_delta_phi_half(P: int, k: int, spf: list[int], p_half: int) -> int:
    """直接计算 Phi((k+1)P-1,p_half)-Phi(kP,p_half)。"""
    return sum(1 for t in range(1, P) if spf[k * P + t] >= p_half)


def finite_direct_prime_count(P: int, k: int, spf: list[int]) -> int:
    """直接读取该行素数数。"""
    return sum(1 for t in range(1, P) if spf[k * P + t] == k * P + t)


def forest_hole_count(
    P: int,
    k: int,
    high_q_primes: list[int],
    is_prime: Callable[[int], bool],
) -> int:
    """计算真实 high-prime semiprime forest holes 数。"""
    count = 0
    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        for m in range(lower, upper + 1):
            if is_prime(m):
                count += 1
    return count


def parity_capacity(
    P: int,
    k: int,
    high_q_primes: list[int],
) -> dict[str, int]:
    """计算 reciprocal 整数窗容量与奇偶强制扣除。

    对 q>P/2，每个 m 窗长度至多为 2。长度为 2 时必含一个偶数；
    单点窗若是偶数也不能贡献素数 m。因此这些偶候选可非循环扣除。
    """
    integer_capacity = 0
    forced_even_nonprime = 0
    nonempty_windows = 0
    length_one_windows = 0
    length_two_windows = 0
    max_window_length = 0

    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        length = max(0, upper - lower + 1)
        integer_capacity += length
        max_window_length = max(max_window_length, length)
        if length:
            nonempty_windows += 1
        if length == 1:
            length_one_windows += 1
        elif length == 2:
            length_two_windows += 1
        for m in range(lower, upper + 1):
            if m > 2 and m % 2 == 0:
                forced_even_nonprime += 1

    return {
        "integer_window_capacity": integer_capacity,
        "forced_even_nonprime_candidates": forced_even_nonprime,
        "parity_prime_ceiling": integer_capacity - forced_even_nonprime,
        "nonempty_windows": nonempty_windows,
        "length_one_windows": length_one_windows,
        "length_two_windows": length_two_windows,
        "max_window_length": max_window_length,
    }


def row_profile(P: int, k: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """构造有限行的 parity capacity 读数。"""
    p_half = next_prime_after_half(P, primes_2p)
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    cap = parity_capacity(P, k, high_q_primes)
    delta_phi = finite_delta_phi_half(P, k, spf, p_half)
    holes = forest_hole_count(P, k, high_q_primes, lambda value: spf[value] == value)
    direct = finite_direct_prime_count(P, k, spf)
    cap.update(
        {
            "P": P,
            "k": k,
            "p_half": p_half,
            "in_shadow_free_subband": k <= shadow_free_cap(P),
            "in_upper_band": k >= upper_band_first_k(P),
            "in_bhp_remaining_high_band": k >= high_band_lower_k(P),
            "delta_phi_half": delta_phi,
            "forest_hole_count": holes,
            "direct_prime_count": direct,
            "delta_minus_integer_capacity": delta_phi - cap["integer_window_capacity"],
            "delta_minus_parity_ceiling": delta_phi - cap["parity_prime_ceiling"],
            "parity_ceiling_minus_holes": cap["parity_prime_ceiling"] - holes,
            "positive_by_integer_capacity": delta_phi > cap["integer_window_capacity"],
            "positive_by_parity_ceiling": delta_phi > cap["parity_prime_ceiling"],
            "endpoint_positive_direct": direct > 0,
            "hole_leq_parity_ceiling": holes <= cap["parity_prime_ceiling"],
        }
    )
    return cap


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计；只作一致性检查，不作全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    rows: list[dict[str, Any]] = []
    for P in primes:
        if P < 11:
            continue
        for k in range(2, P):
            rows.append(row_profile(P, k, spf, primes_2p))

    parity_not_closed = [row for row in rows if not row["positive_by_parity_ceiling"]]
    parity_failures = [row for row in rows if row["delta_minus_parity_ceiling"] < 0]
    parity_ties = [row for row in rows if row["delta_minus_parity_ceiling"] == 0]
    hole_ceiling_failures = [row for row in rows if not row["hole_leq_parity_ceiling"]]
    base_ties_positive = all(row["endpoint_positive_direct"] for row in parity_ties)
    sample_rows = [
        row
        for row in rows
        if (row["P"], row["k"]) in {(11, 10), (19, 15), (101, 100), (257, 256), (1009, 1008)}
    ]
    return {
        "max_prime": max_prime,
        "row_count": len(rows),
        "closed_by_integer_window_capacity_count": sum(row["positive_by_integer_capacity"] for row in rows),
        "closed_by_parity_ceiling_count": sum(row["positive_by_parity_ceiling"] for row in rows),
        "parity_not_closed_count": len(parity_not_closed),
        "parity_failure_count": len(parity_failures),
        "parity_tie_count": len(parity_ties),
        "parity_ties_have_direct_prime": base_ties_positive,
        "hole_ceiling_failure_count": len(hole_ceiling_failures),
        "all_holes_leq_parity_ceiling": not hole_ceiling_failures,
        "minimum_delta_minus_parity_ceiling_row": min(rows, key=lambda item: item["delta_minus_parity_ceiling"]),
        "maximum_parity_ceiling_row": max(rows, key=lambda item: item["parity_prime_ceiling"]),
        "parity_not_closed_rows": parity_not_closed,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def segment_delta_phi_half(P: int, k: int, low_primes: list[int]) -> int:
    """用分段筛计算大样本 Delta Phi half。"""
    covered = bytearray(P)
    for q in low_primes:
        start = (-(k * P)) % q
        if start == 0:
            start = q
        if start < P:
            covered[start:P:q] = b"\x01" * (((P - 1 - start) // q) + 1)
    return covered[1:].count(0)


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 parity capacity 读数。"""
    max_seed = max(seeds) + 10000
    flags = prime_flags(2 * max_seed)
    samples: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        low_primes = primes_from_flags(flags, P // 2)
        high_q_primes = [q for q in range(P // 2 + 1, P) if flags[q]]
        k_values = sorted(
            {
                2,
                min(P - 1, shadow_free_cap(P)),
                min(P - 1, upper_band_first_k(P)),
                min(P - 1, max(upper_band_first_k(P), high_band_lower_k(P))),
                P - 1,
            }
        )
        for k in k_values:
            cap = parity_capacity(P, k, high_q_primes)
            delta_phi = segment_delta_phi_half(P, k, low_primes)
            holes = forest_hole_count(P, k, high_q_primes, lambda value: bool(flags[value]))
            cap.update(
                {
                    "P": P,
                    "k": k,
                    "in_shadow_free_subband": k <= shadow_free_cap(P),
                    "in_upper_band": k >= upper_band_first_k(P),
                    "delta_phi_half": delta_phi,
                    "forest_hole_count": holes,
                    "delta_minus_integer_capacity": delta_phi - cap["integer_window_capacity"],
                    "delta_minus_parity_ceiling": delta_phi - cap["parity_prime_ceiling"],
                    "positive_by_integer_capacity": delta_phi > cap["integer_window_capacity"],
                    "positive_by_parity_ceiling": delta_phi > cap["parity_prime_ceiling"],
                    "large_sample_not_global_proof": True,
                }
            )
            samples.append(cap)
    return {
        "sample_seeds": seeds,
        "sample_count": len(samples),
        "all_sampled_parity_margins_positive": all(item["positive_by_parity_ceiling"] for item in samples),
        "minimum_sample_delta_minus_parity_ceiling": min(item["delta_minus_parity_ceiling"] for item in samples),
        "samples": samples,
        "large_samples_are_evidence_not_global_proof": True,
    }


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_gates() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        gate(
            "EndpointDifferenceImported",
            True,
            True,
            "上一层已证明 prime count = DeltaPhi_half - forest holes。",
            "endpoint identity imported",
        ),
        gate(
            "ReciprocalIntegerWindowCeilingClosed",
            True,
            True,
            "|F(P,k)| 不超过 high-q reciprocal 整数短窗总容量 W_int(P,k)。",
            "integer capacity ceiling",
        ),
        gate(
            "ParityForcedCompositeCeilingClosed",
            True,
            True,
            "每个偶 m>2 不能是 prime，故 |F(P,k)|<=W_int(P,k)-E_even(P,k)。",
            "parity capacity ceiling",
        ),
        gate(
            "FiniteAuditParityCapacityClosedAfterBaseTie",
            True,
            True,
            "P<=1009 审计中 parity ceiling 只剩 P=19,k=15 的等号基例，且该行直接有素数。",
            "finite audit only",
        ),
        gate(
            "GlobalParityEndpointCapacityInequalityProved",
            False,
            False,
            "尚未证明所有 P,k 都满足 DeltaPhi_half(P,k)>W_int(P,k)-E_even(P,k) 或等号时存在额外合成候选。",
            "PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC",
        ),
        gate(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层是更强的非循环容量上界，不证明三目标命题。",
            "PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC",
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


def profile_markdown(rows: list[dict[str, Any]]) -> str:
    """输出行读数表 Markdown。"""
    lines = [
        "| P | k | Delta | W_int | E_even | parity ceiling | Delta-ceiling | holes | primes |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['delta_phi_half']} | "
            f"{row['integer_window_capacity']} | {row['forced_even_nonprime_candidates']} | "
            f"{row['parity_prime_ceiling']} | {row['delta_minus_parity_ceiling']} | "
            f"{row['forest_hole_count']} | {row.get('direct_prime_count', '')} |"
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    finite = finite_audit()
    large = large_sample_audit()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_punctured_endpoint_parity_capacity_router",
        "status": "forest_holes_bounded_by_reciprocal_integer_windows_minus_forced_even_candidates",
        "definitions": {
            "W_int(P,k)": "sum over prime q in (P/2,P) of |I_q(P,k)|",
            "E_even(P,k)": "number of candidate pairs (q,m) with m in I_q(P,k), m even and m>2",
            "C_par(P,k)": "W_int(P,k)-E_even(P,k)",
            "capacity_implication": "DeltaPhi_half(P,k)>C_par(P,k) implies pi((k+1)P-1)-pi(kP)>0",
            "remaining_saturation": "DeltaPhi_half(P,k)<=C_par(P,k) forces near-saturation of odd reciprocal candidates by primes",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "dependency_hashes": dependency_hashes,
        "next_direct_attack_target": "PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC",
        "plain_conclusion": (
            "forest holes 已由 reciprocal 整数短窗容量进一步压到奇偶容量 "
            "C_par(P,k)=W_int(P,k)-E_even(P,k)。因此只要 "
            "DeltaPhi_half(P,k)>C_par(P,k)，该 strict 行立即有素数。有限审计到 P<=1009 "
            "只剩 P=19,k=15 的等号基例，且直接素数数为 1；全局仍需证明 parity endpoint "
            "capacity inequality，或把失败相位登记为 reciprocal prime-pair saturation PDEC。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    finite = payload["finite_audit"]
    large = payload["large_sample_audit"]
    min_row = finite["minimum_delta_minus_parity_ceiling_row"]
    max_row = finite["maximum_parity_ceiling_row"]
    lines = [
        "# Prime Matrix Phi-LPF punctured endpoint parity capacity 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层继续攻击 `PuncturedPhiEndpointDifferencePositiveOrPDEC`。",
        "上一层已有精确恒等式",
        "",
        "```text",
        "prime_count(P,k)=DeltaPhi_half(P,k)-|F(P,k)|.",
        "```",
        "",
        "对每个 `q` in `(P/2,P)`，reciprocal 窗 `I_q(P,k)` 的整数长度至多为 2。",
        "把所有整数候选数为 `W_int(P,k)`；其中偶数 `m>2` 不可能为素数，记作",
        "`E_even(P,k)`。于是有非循环上界",
        "",
        "```text",
        "|F(P,k)| <= C_par(P,k) := W_int(P,k)-E_even(P,k).",
        "```",
        "",
        "因此充分条件变为",
        "",
        "```text",
        "DeltaPhi_half(P,k) > C_par(P,k).",
        "```",
        "",
        "若该不等式失败，反例必须让 odd reciprocal candidates 近乎全部成为 prime-pair holes，",
        "这就是新的更窄 saturated prime-pair 出口。",
        "",
        "## 1. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"row_count={finite['row_count']}",
        f"closed_by_integer_window_capacity_count={finite['closed_by_integer_window_capacity_count']}",
        f"closed_by_parity_ceiling_count={finite['closed_by_parity_ceiling_count']}",
        f"parity_not_closed_count={finite['parity_not_closed_count']}",
        f"parity_failure_count={finite['parity_failure_count']}",
        f"parity_tie_count={finite['parity_tie_count']}",
        f"parity_ties_have_direct_prime={fmt_bool(finite['parity_ties_have_direct_prime'])}",
        f"all_holes_leq_parity_ceiling={fmt_bool(finite['all_holes_leq_parity_ceiling'])}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最小 parity margin 行：",
        "",
        "```text",
        f"P={min_row['P']}, k={min_row['k']}, Delta={min_row['delta_phi_half']}, "
        f"C_par={min_row['parity_prime_ceiling']}, margin={min_row['delta_minus_parity_ceiling']}, "
        f"holes={min_row['forest_hole_count']}, primes={min_row['direct_prime_count']}",
        "```",
        "",
        "最大 parity ceiling 行：",
        "",
        "```text",
        f"P={max_row['P']}, k={max_row['k']}, Delta={max_row['delta_phi_half']}, "
        f"C_par={max_row['parity_prime_ceiling']}, margin={max_row['delta_minus_parity_ceiling']}",
        "```",
        "",
        "未由 strict parity inequality 闭合的有限基例：",
        "",
        profile_markdown(finite["parity_not_closed_rows"]),
        "",
        "代表样本：",
        "",
        profile_markdown(finite["sample_rows"]),
        "",
        "## 2. 大尺度抽样",
        "",
        "```text",
        f"sample_seeds={large['sample_seeds']}",
        f"sample_count={large['sample_count']}",
        f"all_sampled_parity_margins_positive={fmt_bool(large['all_sampled_parity_margins_positive'])}",
        f"minimum_sample_delta_minus_parity_ceiling={large['minimum_sample_delta_minus_parity_ceiling']}",
        f"large_samples_are_evidence_not_global_proof={fmt_bool(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        profile_markdown(large["samples"]),
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 4. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "当前最窄口为：",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只提供更强的",
        "endpoint capacity 上界和新的非循环主攻接口。",
        "",
        "## 5. 依赖哈希",
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
                "closed_by_parity_ceiling_count": payload["finite_audit"][
                    "closed_by_parity_ceiling_count"
                ],
                "parity_not_closed_count": payload["finite_audit"]["parity_not_closed_count"],
                "minimum_sample_delta_minus_parity_ceiling": payload["large_sample_audit"][
                    "minimum_sample_delta_minus_parity_ceiling"
                ],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
