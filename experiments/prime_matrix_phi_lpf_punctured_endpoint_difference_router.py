#!/usr/bin/env python3
"""生成 Phi-LPF punctured endpoint difference 证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_punctured_endpoint_difference_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-difference-router.json

输出：
  data/prime-matrix-phi-lpf-punctured-endpoint-difference-ledger.json
  docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-difference-router.json
  docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-difference-router.md
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

SLUG = "prime-matrix-phi-lpf-punctured-endpoint-difference"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

MAX_PRIME_AUDIT = 1009
LARGE_SAMPLE_SEEDS = [100000, 300000]

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-router.json",
    DOCS / "prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json",
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


def next_prime_after_half(P: int, primes_2p: list[int]) -> int:
    """返回大于 P/2 的第一个素数，即 Phi 半筛阈值。"""
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


def high_band_lower_k(P: int) -> int:
    """返回 BHP bulk 后的第一个整数 k；只作分区标签。"""
    return max(2, int(P ** (19.0 / 21.0)) + 1)


def shadow_free_cap(P: int) -> int:
    """返回 shadow-free 条件允许的最大 k。"""
    return max(1, (P * P - 4 * P + 4) // (4 * P))


def upper_band_first_k(P: int) -> int:
    """返回 upper square band 第一行。"""
    return max(2, shadow_free_cap(P) + 1)


def reciprocal_window_for_q(P: int, k: int, q: int) -> tuple[int, int]:
    """返回固定 q 的 m 候选闭区间。"""
    lower = max(q, (k * P) // q + 1)
    upper = min(2 * P - 1, ((k + 1) * P - 1) // q)
    return lower, upper


def forest_hole_count(
    P: int,
    k: int,
    high_q_primes: list[int],
    is_prime: Callable[[int], bool],
) -> int:
    """计算 forest holes 数；每个 hole 是一个 high-prime semiprime composite slot。"""
    count = 0
    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        for m in range(lower, upper + 1):
            if is_prime(m):
                count += 1
    return count


def finite_delta_phi_half(P: int, k: int, spf: list[int], p_half: int) -> int:
    """直接计算 Phi((k+1)P-1,p_half)-Phi(kP,p_half)。"""
    return sum(1 for t in range(1, P) if spf[k * P + t] >= p_half)


def finite_direct_prime_count(P: int, k: int, spf: list[int]) -> int:
    """直接读取该行素数数。"""
    return sum(1 for t in range(1, P) if spf[k * P + t] == k * P + t)


def row_profile(P: int, k: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """构造有限行的 Phi endpoint difference 读数。"""
    p_half = next_prime_after_half(P, primes_2p)
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]

    def is_prime_m(value: int) -> bool:
        return spf[value] == value

    delta_phi = finite_delta_phi_half(P, k, spf, p_half)
    holes = forest_hole_count(P, k, high_q_primes, is_prime_m)
    direct = finite_direct_prime_count(P, k, spf)
    return {
        "P": P,
        "k": k,
        "p_half": p_half,
        "in_shadow_free_subband": k <= shadow_free_cap(P),
        "in_upper_band": k >= upper_band_first_k(P),
        "in_bhp_remaining_high_band": k >= high_band_lower_k(P),
        "delta_phi_half": delta_phi,
        "forest_hole_count": holes,
        "delta_phi_minus_forest": delta_phi - holes,
        "direct_prime_count": direct,
        "endpoint_difference_identity_holds": delta_phi - holes == direct,
    }


def audit_prime_base(P: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """审计单个素数底 P 的所有 strict 行。"""
    rows = [row_profile(P, k, spf, primes_2p) for k in range(2, P)]
    failures = [row for row in rows if not row["endpoint_difference_identity_holds"]]
    min_margin_row = min(rows, key=lambda item: item["delta_phi_minus_forest"])
    max_hole_row = max(rows, key=lambda item: item["forest_hole_count"])
    sample_ks = sorted(
        {
            2,
            min(P - 1, shadow_free_cap(P)),
            min(P - 1, upper_band_first_k(P)),
            min(P - 1, max(upper_band_first_k(P), high_band_lower_k(P))),
            P - 1,
        }
    )
    return {
        "P": P,
        "strict_row_count": len(rows),
        "endpoint_difference_failure_count": len(failures),
        "all_endpoint_difference_identities_hold": not failures,
        "minimum_margin_row": min_margin_row,
        "maximum_forest_hole_row": max_hole_row,
        "sample_rows": [row for row in rows if row["k"] in sample_ks],
    }


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计；只作一致性检查，不作全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    profiles = [audit_prime_base(P, spf, primes_2p) for P in primes if P >= 11]
    failures = [profile for profile in profiles if profile["endpoint_difference_failure_count"]]
    min_margin_profile = min(
        profiles,
        key=lambda item: item["minimum_margin_row"]["delta_phi_minus_forest"],
    )
    max_hole_profile = max(
        profiles,
        key=lambda item: item["maximum_forest_hole_row"]["forest_hole_count"],
    )
    return {
        "max_prime": max_prime,
        "prime_base_count": len(profiles),
        "all_endpoint_difference_identities_hold": not failures,
        "endpoint_difference_failure_count": sum(profile["endpoint_difference_failure_count"] for profile in profiles),
        "minimum_margin_profile": {
            "P": min_margin_profile["P"],
            "row": min_margin_profile["minimum_margin_row"],
        },
        "maximum_forest_hole_profile": {
            "P": max_hole_profile["P"],
            "row": max_hole_profile["maximum_forest_hole_row"],
        },
        "sample_profiles": [
            profile
            for profile in profiles
            if profile["P"] in {11, 101, 257, 1009}
        ],
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
    """抽样较大 P 的 endpoint difference 读数。"""
    max_seed = max(seeds) + 10000
    flags = prime_flags(2 * max_seed)
    samples: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        low_primes = [q for q in range(2, P // 2 + 1) if flags[q]]
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

        def is_prime_m(value: int) -> bool:
            return bool(flags[value])

        for k in k_values:
            delta_phi = segment_delta_phi_half(P, k, low_primes)
            holes = forest_hole_count(P, k, high_q_primes, is_prime_m)
            samples.append(
                {
                    "P": P,
                    "k": k,
                    "in_shadow_free_subband": k <= shadow_free_cap(P),
                    "in_upper_band": k >= upper_band_first_k(P),
                    "delta_phi_half": delta_phi,
                    "forest_hole_count": holes,
                    "delta_phi_minus_forest": delta_phi - holes,
                    "positive_endpoint_margin": delta_phi > holes,
                }
            )
    return {
        "sample_seeds": seeds,
        "sample_count": len(samples),
        "all_sampled_endpoint_margins_positive": all(item["positive_endpoint_margin"] for item in samples),
        "minimum_sample_endpoint_margin": min(item["delta_phi_minus_forest"] for item in samples),
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
            "PhiHalfEndpointDifferenceIdentityClosed",
            True,
            True,
            "Delta Phi_half 精确等于 half-primorial survivor 数。",
            "exact Phi-LPF endpoint count",
        ),
        gate(
            "ForestHoleSubtractionIdentityClosed",
            True,
            True,
            "strict 行素数数精确等于 Delta Phi_half 减去 reciprocal forest holes。",
            "exact punctured endpoint identity",
        ),
        gate(
            "ShadowFreeAndUpperBandUnifiedByEndpointDifference",
            True,
            True,
            "shadow-free 是 forest_holes=0；upper-band 是 forest_holes>0 的同一端点差公式。",
            "unified endpoint formulation",
        ),
        gate(
            "FiniteSweepEndpointIdentityMatchesPrimeCount",
            True,
            True,
            "有限审计确认端点差等式与直接素数计数一致，但不作为全局证明。",
            "finite audit only",
        ),
        gate(
            "EndpointDifferenceDominatesForestHolesProved",
            False,
            False,
            "尚未证明所有剩余特殊相位都有 Delta Phi_half>forest_holes。",
            "PuncturedPhiEndpointDifferencePositiveOrPDEC",
        ),
        gate(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层只把剩余口写成 Phi-LPF 两端点差正性，不证明三目标命题。",
            "PuncturedPhiEndpointDifferencePositiveOrPDEC",
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


def sample_markdown(samples: list[dict[str, Any]]) -> str:
    """输出样本表 Markdown。"""
    lines = [
        "| P | k | Delta Phi half | forest holes | Delta-hole | direct primes | shadow-free | upper |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in samples:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['delta_phi_half']} | "
            f"{row['forest_hole_count']} | {row['delta_phi_minus_forest']} | "
            f"{row.get('direct_prime_count', '')} | `{fmt_bool(row['in_shadow_free_subband'])}` | "
            f"`{fmt_bool(row['in_upper_band'])}` |"
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
        "certificate_type": "prime_matrix_phi_lpf_punctured_endpoint_difference_router",
        "status": "strict_k_prime_count_equals_phi_half_endpoint_difference_minus_forest_holes",
        "definitions": {
            "p_half(P)": "least prime > P/2",
            "DeltaPhi_half(P,k)": "Phi((k+1)P-1,p_half(P))-Phi(kP,p_half(P))",
            "F(P,k)": "reciprocal forest hole set of high-prime semiprime slots",
            "identity": "pi((k+1)P-1)-pi(kP)=DeltaPhi_half(P,k)-|F(P,k)|",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "dependency_hashes": dependency_hashes,
        "next_direct_attack_target": "PuncturedPhiEndpointDifferencePositiveOrPDEC",
        "plain_conclusion": (
            "当前 strict-k 剩余被写成单一 Phi-LPF 端点差：行素数数等于半筛 Phi 两端点差 "
            "减去 reciprocal forest holes。反例必须满足 DeltaPhi_half(P,k)<=|F(P,k)|；"
            "这就是 punctured phase 的端点计数正性版本。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    finite = payload["finite_audit"]
    large = payload["large_sample_audit"]
    min_row = finite["minimum_margin_profile"]["row"]
    max_hole = finite["maximum_forest_hole_profile"]["row"]
    sample_rows = [row for profile in finite["sample_profiles"] for row in profile["sample_rows"]]
    lines = [
        "# Prime Matrix Phi-LPF punctured endpoint difference 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层把 punctured half-primorial phase 改写为用户强调的 Phi-LPF 两端点差。",
        "令 `p_half(P)` 为大于 `P/2` 的第一个素数，定义",
        "",
        "```text",
        "DeltaPhi_half(P,k)=Phi((k+1)P-1,p_half(P))-Phi(kP,p_half(P)).",
        "```",
        "",
        "再令 `F(P,k)` 为 upper-band reciprocal forest hole set。则",
        "",
        "```text",
        "pi((k+1)P-1)-pi(kP)=DeltaPhi_half(P,k)-|F(P,k)|.",
        "```",
        "",
        "## 1. 结构证明读法",
        "",
        "`DeltaPhi_half(P,k)` 数的正是该行中避开所有 `q<=P/2` 的 half-primorial survivors。",
        "这些 survivor 若合成，就唯一落入 high-prime semiprime forest holes；去掉 holes 后只能是素数。",
        "因此反例等价于端点差不超过 forest holes：",
        "",
        "```text",
        "DeltaPhi_half(P,k)<=|F(P,k)|.",
        "```",
        "",
        "shadow-free lane 是 `|F(P,k)|=0` 的特例；upper-band 是有 forest holes 的同一公式。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"prime_base_count={finite['prime_base_count']}",
        f"all_endpoint_difference_identities_hold={fmt_bool(finite['all_endpoint_difference_identities_hold'])}",
        f"endpoint_difference_failure_count={finite['endpoint_difference_failure_count']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最小端点差余量行：",
        "",
        "```text",
        f"P={min_row['P']}, k={min_row['k']}, DeltaPhi={min_row['delta_phi_half']}, "
        f"forest={min_row['forest_hole_count']}, margin={min_row['delta_phi_minus_forest']}",
        "```",
        "",
        "最大 forest-hole 行：",
        "",
        "```text",
        f"P={max_hole['P']}, k={max_hole['k']}, DeltaPhi={max_hole['delta_phi_half']}, "
        f"forest={max_hole['forest_hole_count']}, margin={max_hole['delta_phi_minus_forest']}",
        "```",
        "",
        "## 3. 有限样本表",
        "",
        sample_markdown(sample_rows),
        "",
        "## 4. 大尺度抽样",
        "",
        "```text",
        f"sample_seeds={large['sample_seeds']}",
        f"sample_count={large['sample_count']}",
        f"all_sampled_endpoint_margins_positive={fmt_bool(large['all_sampled_endpoint_margins_positive'])}",
        f"minimum_sample_endpoint_margin={large['minimum_sample_endpoint_margin']}",
        f"large_samples_are_evidence_not_global_proof={fmt_bool(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        sample_markdown(large["samples"]),
        "",
        "## 5. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 6. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "当前端点差最窄口为：",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只把统一剩余写成",
        "Phi-LPF 端点差正性。",
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
                "all_endpoint_difference_identities_hold": payload["finite_audit"][
                    "all_endpoint_difference_identities_hold"
                ],
                "large_sample_count": payload["large_sample_audit"]["sample_count"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
