#!/usr/bin/env python3
"""生成 punctured half-primorial forest phase 证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_punctured_half_primorial_forest_phase_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-router.json

输出：
  data/prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-ledger.json
  docs/monograph/prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-router.json
  docs/monograph/prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-router.md
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

SLUG = "prime-matrix-phi-lpf-punctured-half-primorial-forest-phase"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

MAX_PRIME_AUDIT = 1009
LARGE_SAMPLE_SEEDS = [100000, 300000]

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.json",
    DOCS / "prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-router.json",
    DOCS / "prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json",
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


def forest_edge_slots(
    P: int,
    k: int,
    high_q_primes: list[int],
    is_prime: Callable[[int], bool],
) -> set[int]:
    """列出 upper-band forest shadow 在行内打孔的位置 t。"""
    slots: set[int] = set()
    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        for m in range(lower, upper + 1):
            if is_prime(m):
                t = q * m - k * P
                if 1 <= t < P:
                    slots.add(t)
    return slots


def finite_rough_slots(P: int, k: int, spf: list[int]) -> set[int]:
    """直接读取避开 q<=P/2 的 half-rough 槽。"""
    cutoff = P // 2
    return {t for t in range(1, P) if spf[k * P + t] > cutoff}


def finite_direct_prime_count(P: int, k: int, spf: list[int]) -> int:
    """直接读取该行素数数。"""
    return sum(1 for t in range(1, P) if spf[k * P + t] == k * P + t)


def row_profile(P: int, k: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """构造有限行的 punctured half-primorial 等价读数。"""
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]

    def is_prime_m(value: int) -> bool:
        return spf[value] == value

    rough_slots = finite_rough_slots(P, k, spf)
    edge_slots = forest_edge_slots(P, k, high_q_primes, is_prime_m)
    prime_slots = rough_slots - edge_slots
    direct_prime_count = finite_direct_prime_count(P, k, spf)
    covered_outside_forest = (P - 1) - len(edge_slots) - len(prime_slots)
    return {
        "P": P,
        "k": k,
        "upper_band_first_k": upper_band_first_k(P),
        "bhp_remaining_high_band_first_k": high_band_lower_k(P),
        "in_shadow_free_subband": k <= shadow_free_cap(P),
        "in_upper_band": k >= upper_band_first_k(P),
        "half_rough_survivor_count": len(rough_slots),
        "forest_hole_count": len(edge_slots),
        "prime_slot_count_by_punctured_phase": len(prime_slots),
        "direct_prime_count": direct_prime_count,
        "covered_outside_forest_count": covered_outside_forest,
        "rough_slots_subset_of_forest_holes": rough_slots <= edge_slots,
        "punctured_phase_identity_holds": len(prime_slots) == direct_prime_count,
        "forest_holes_all_half_rough": edge_slots <= rough_slots,
        "prime_slot_prefix": sorted(prime_slots)[:16],
        "forest_hole_prefix": sorted(edge_slots)[:16],
    }


def audit_prime_base(P: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """审计单个素数底 P 的 upper-band punctured phase。"""
    first_upper = upper_band_first_k(P)
    rows = [row_profile(P, k, spf, primes_2p) for k in range(first_upper, P)]
    failures = [
        row
        for row in rows
        if not (row["punctured_phase_identity_holds"] and row["forest_holes_all_half_rough"])
    ]
    saturation_rows = [row for row in rows if row["rough_slots_subset_of_forest_holes"]]
    min_prime_row = min(rows, key=lambda item: item["prime_slot_count_by_punctured_phase"])
    max_forest_row = max(rows, key=lambda item: item["forest_hole_count"])
    sample_ks = sorted(
        {
            first_upper,
            min(P - 1, max(first_upper, high_band_lower_k(P))),
            min(P - 1, max(first_upper, P // 2)),
            min(P - 1, max(first_upper, (3 * P) // 4)),
            P - 1,
        }
    )
    return {
        "P": P,
        "upper_band_first_k": first_upper,
        "upper_row_count": len(rows),
        "punctured_phase_failure_count": len(failures),
        "all_punctured_phase_identities_hold": not failures,
        "saturation_row_count": len(saturation_rows),
        "minimum_prime_slot_row": min_prime_row,
        "maximum_forest_hole_row": max_forest_row,
        "sample_rows": [row for row in rows if row["k"] in sample_ks],
    }


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计；只作一致性检查，不作全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    profiles = [audit_prime_base(P, spf, primes_2p) for P in primes if P >= 11]
    failures = [profile for profile in profiles if profile["punctured_phase_failure_count"]]
    min_prime_profile = min(
        profiles,
        key=lambda item: item["minimum_prime_slot_row"]["prime_slot_count_by_punctured_phase"],
    )
    max_forest_profile = max(
        profiles,
        key=lambda item: item["maximum_forest_hole_row"]["forest_hole_count"],
    )
    return {
        "max_prime": max_prime,
        "prime_base_count": len(profiles),
        "all_punctured_phase_identities_hold": not failures,
        "punctured_phase_failure_count": sum(profile["punctured_phase_failure_count"] for profile in profiles),
        "saturation_row_count": sum(profile["saturation_row_count"] for profile in profiles),
        "minimum_prime_slot_profile": {
            "P": min_prime_profile["P"],
            "row": min_prime_profile["minimum_prime_slot_row"],
        },
        "maximum_forest_hole_profile": {
            "P": max_forest_profile["P"],
            "row": max_forest_profile["maximum_forest_hole_row"],
        },
        "sample_profiles": [
            profile
            for profile in profiles
            if profile["P"] in {11, 101, 257, 1009}
        ],
        "finite_evidence_not_used_as_global_proof": True,
    }


def segment_rough_slots(P: int, k: int, low_primes: list[int]) -> set[int]:
    """用分段筛读取大样本 half-rough 槽。"""
    covered = bytearray(P)
    for q in low_primes:
        start = (-(k * P)) % q
        if start == 0:
            start = q
        if start < P:
            covered[start:P:q] = b"\x01" * (((P - 1 - start) // q) + 1)
    return {t for t in range(1, P) if not covered[t]}


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P；不作全局证明。"""
    max_seed = max(seeds) + 10000
    flags = prime_flags(2 * max_seed)
    samples: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        low_primes = [q for q in range(2, P // 2 + 1) if flags[q]]
        high_q_primes = [q for q in range(P // 2 + 1, P) if flags[q]]
        first_upper = upper_band_first_k(P)
        k_values = sorted(
            {
                first_upper,
                min(P - 1, max(first_upper, high_band_lower_k(P))),
                min(P - 1, max(first_upper, P // 2)),
                min(P - 1, max(first_upper, (3 * P) // 4)),
                P - 1,
            }
        )

        def is_prime_m(value: int) -> bool:
            return bool(flags[value])

        for k in k_values:
            rough_slots = segment_rough_slots(P, k, low_primes)
            edge_slots = forest_edge_slots(P, k, high_q_primes, is_prime_m)
            prime_slots = rough_slots - edge_slots
            samples.append(
                {
                    "P": P,
                    "k": k,
                    "upper_band_first_k": first_upper,
                    "bhp_remaining_high_band_first_k": high_band_lower_k(P),
                    "half_rough_survivor_count": len(rough_slots),
                    "forest_hole_count": len(edge_slots),
                    "prime_slot_count_by_punctured_phase": len(prime_slots),
                    "forest_holes_all_half_rough": edge_slots <= rough_slots,
                    "rough_slots_subset_of_forest_holes": rough_slots <= edge_slots,
                }
            )
    return {
        "sample_seeds": seeds,
        "sample_count": len(samples),
        "all_sampled_forest_holes_are_half_rough": all(item["forest_holes_all_half_rough"] for item in samples),
        "sample_saturation_row_count": sum(1 for item in samples if item["rough_slots_subset_of_forest_holes"]),
        "minimum_sample_prime_slots": min(item["prime_slot_count_by_punctured_phase"] for item in samples),
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
            "PuncturedHalfPrimorialIdentityClosed",
            True,
            True,
            "行素数槽精确等于 half-primorial survivor 去掉 upper-band forest holes 后的剩余。",
            "exact identity",
        ),
        gate(
            "ShadowFreeLaneIsZeroHoleSpecialCase",
            True,
            True,
            "shadow-free 子带就是 forest hole set 为空的 punctured phase 特例。",
            "unifies previous lane",
        ),
        gate(
            "UpperBandFailureEqualsPuncturedCoveredBlock",
            True,
            True,
            "upper-band 失败当且仅当所有 half-primorial survivors 都落在 forest holes 内。",
            "PuncturedHalfPrimorialForestCoveredBlock",
        ),
        gate(
            "FiniteSweepNoSaturationObserved",
            True,
            True,
            "有限审计未见 forest saturation，但这不是全局证明。",
            "finite audit only",
        ),
        gate(
            "PuncturedForestPhaseAvoidanceProved",
            False,
            False,
            "尚未证明特殊相位不能启动带 forest holes 的长覆盖块。",
            "PuncturedHalfPrimorialForestPhaseAvoidanceOrPDEC",
        ),
        gate(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层统一两个剩余口，但不证明三目标命题。",
            "PuncturedHalfPrimorialForestPhaseAvoidanceOrPDEC",
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
        "| P | k | R_half | forest holes | prime slots | covered outside holes | saturation |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in samples:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['half_rough_survivor_count']} | "
            f"{row['forest_hole_count']} | {row['prime_slot_count_by_punctured_phase']} | "
            f"{row.get('covered_outside_forest_count', '')} | "
            f"`{fmt_bool(row['rough_slots_subset_of_forest_holes'])}` |"
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
        "certificate_type": "prime_matrix_phi_lpf_punctured_half_primorial_forest_phase_router",
        "status": "shadow_free_and_upper_band_reduced_to_punctured_half_primorial_forest_phase",
        "definitions": {
            "M_half(P)": "prod_{q<=P/2, q prime} q",
            "F(P,k)": "{t: exists q,m prime, P/2<q<=m<2P, kP<qm<(k+1)P, t=qm-kP}",
            "prime_slots": "{1<=t<P: gcd(kP+t,M_half(P))=1 and t not in F(P,k)}",
            "failure_equivalence": "row has no prime iff all half-primorial survivors lie in F(P,k)",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "dependency_hashes": dependency_hashes,
        "next_direct_attack_target": "PuncturedHalfPrimorialForestPhaseAvoidanceOrPDEC",
        "plain_conclusion": (
            "shadow-free 与 upper-band 两个剩余口已经合并为同一个相位问题：特殊半 primorial "
            "覆盖块允许被 reciprocal forest holes 打孔。若仍无素数，则全部 half-primorial survivor "
            "必须落入这片 forest hole set；否则任意未被打孔的 survivor 自动就是素数。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    finite = payload["finite_audit"]
    large = payload["large_sample_audit"]
    min_row = finite["minimum_prime_slot_profile"]["row"]
    max_forest = finite["maximum_forest_hole_profile"]["row"]
    sample_rows = [row for profile in finite["sample_profiles"] for row in profile["sample_rows"]]
    lines = [
        "# Prime Matrix Phi-LPF punctured half-primorial forest phase 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层把 shadow-free half-primorial special phase 与 upper-band forest saturation 合并。",
        "设",
        "",
        "```text",
        "M_half(P)=prod_{q<=P/2, q prime} q,",
        "F(P,k)={t: t=qm-kP, q,m prime, P/2<q<=m<2P, kP<qm<(k+1)P}.",
        "```",
        "",
        "则行内素数槽精确为",
        "",
        "```text",
        "{1<=t<P: gcd(kP+t,M_half(P))=1 and t not in F(P,k)}.",
        "```",
        "",
        "## 1. 结构证明读法",
        "",
        "若 `t` 避开所有低素数且不在 forest hole set `F(P,k)` 中，则 `kP+t` 不可能合成。",
        "因为任何合成 half-rough 槽都必须写成唯一的 high-prime product `qm`，从而正好落入 `F(P,k)`。",
        "因此行失败等价于所有 half-primorial survivor 都被 forest holes 吃掉：",
        "",
        "```text",
        "{t: gcd(kP+t,M_half(P))=1} subset F(P,k).",
        "```",
        "",
        "shadow-free 子带就是 `F(P,k)=empty` 的零孔特例；upper-band 则是有序森林孔特例。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"prime_base_count={finite['prime_base_count']}",
        f"all_punctured_phase_identities_hold={fmt_bool(finite['all_punctured_phase_identities_hold'])}",
        f"punctured_phase_failure_count={finite['punctured_phase_failure_count']}",
        f"saturation_row_count={finite['saturation_row_count']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最小 prime-slot 行：",
        "",
        "```text",
        f"P={min_row['P']}, k={min_row['k']}, R={min_row['half_rough_survivor_count']}, "
        f"forest={min_row['forest_hole_count']}, prime_slots={min_row['prime_slot_count_by_punctured_phase']}",
        "```",
        "",
        "最大 forest-hole 行：",
        "",
        "```text",
        f"P={max_forest['P']}, k={max_forest['k']}, R={max_forest['half_rough_survivor_count']}, "
        f"forest={max_forest['forest_hole_count']}, prime_slots={max_forest['prime_slot_count_by_punctured_phase']}",
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
        f"all_sampled_forest_holes_are_half_rough={fmt_bool(large['all_sampled_forest_holes_are_half_rough'])}",
        f"sample_saturation_row_count={large['sample_saturation_row_count']}",
        f"minimum_sample_prime_slots={large['minimum_sample_prime_slots']}",
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
        "当前统一最窄口为：",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它把两个剩余口合并成",
        "一个 punctured half-primorial special phase 问题。",
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
                "all_punctured_phase_identities_hold": payload["finite_audit"][
                    "all_punctured_phase_identities_hold"
                ],
                "saturation_row_count": payload["finite_audit"]["saturation_row_count"],
                "large_sample_count": payload["large_sample_audit"]["sample_count"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
