#!/usr/bin/env python3
"""审计 Phi-LPF primorial-wheel 容量阶梯与极限。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_primorial_wheel_limit_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-primorial-wheel-limit-audit.json

本证书回答：从 6-wheel、30-wheel 继续到 210、2310、...、动态 primorial
是否能在极限中自动证明目标命题。结论是：wheel 阶梯确实单调收紧；
但当 wheel 覆盖到 sqrt(2P) 后，容量上界已经等于真实 forest-hole 数。
此时正性条件正好等价于目标行内素数存在，不能作为独立证明。
"""

from __future__ import annotations

import hashlib
import json
from math import isqrt, prod
from pathlib import Path
from typing import Any, Callable

from prime_matrix_phi_lpf_punctured_endpoint_wheel30_capacity_router import (
    DATA,
    DOCS,
    LARGE_SAMPLE_SEEDS,
    MAX_PRIME_AUDIT,
    ROOT,
    finite_delta_phi_half,
    finite_direct_prime_count,
    high_band_lower_k,
    next_prime_after_half,
    next_prime_at_least,
    prime_flags,
    primes_from_flags,
    primes_from_spf,
    reciprocal_window_for_q,
    segment_delta_phi_half,
    shadow_free_cap,
    spf_table,
    upper_band_first_k,
)


SLUG = "prime-matrix-phi-lpf-primorial-wheel-limit"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
FIXED_WHEEL_LAYERS = [
    ("2-wheel", [2]),
    ("6-wheel", [2, 3]),
    ("30-wheel", [2, 3, 5]),
    ("210-wheel", [2, 3, 5, 7]),
    ("2310-wheel", [2, 3, 5, 7, 11]),
    ("30030-wheel", [2, 3, 5, 7, 11, 13]),
]

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-wheel6-capacity-router.json",
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-router.json",
    DOCS / "prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bool_text(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def wheel_modulus(primes: list[int]) -> int:
    """返回 wheel primorial。"""
    return prod(primes) if primes else 1


def forced_by_wheel(m: int, wheel_primes: list[int]) -> bool:
    """判断 m 是否被给定 wheel 强迫为合数。"""
    return any(m > ell and m % ell == 0 for ell in wheel_primes)


def candidate_m_values(P: int, k: int, high_q_primes: list[int]) -> list[int]:
    """列出 reciprocal windows 中的 m 候选，保留 q 重数。"""
    values: list[int] = []
    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        values.extend(range(lower, upper + 1))
    return values


def capacity_from_candidates(candidates: list[int], wheel_primes: list[int]) -> int:
    """计算给定 wheel 下仍可能为 prime cofactor 的候选重数。"""
    return sum(1 for m in candidates if not forced_by_wheel(m, wheel_primes))


def hole_count_from_candidates(candidates: list[int], is_prime: Callable[[int], bool]) -> int:
    """计算真实 prime-cofactor forest-hole 重数。"""
    return sum(1 for m in candidates if is_prime(m))


def sqrt_wheel_primes(P: int, primes_2p: list[int]) -> list[int]:
    """返回足以筛掉所有 m<2P 合数的动态 wheel primes。"""
    limit = isqrt(2 * P - 1)
    return [ell for ell in primes_2p if ell <= limit]


def row_profile(
    P: int,
    k: int,
    primes_2p: list[int],
    is_prime: Callable[[int], bool],
    delta_phi: int,
    direct_prime_count: int | None = None,
) -> dict[str, Any]:
    """构造单行 primorial-wheel 阶梯读数。"""
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    candidates = candidate_m_values(P, k, high_q_primes)
    holes = hole_count_from_candidates(candidates, is_prime)
    capacities: dict[str, dict[str, Any]] = {}
    previous_capacity: int | None = None
    for name, wheel_primes in FIXED_WHEEL_LAYERS:
        capacity = capacity_from_candidates(candidates, wheel_primes)
        capacities[name] = {
            "wheel_primes": wheel_primes,
            "wheel_modulus": wheel_modulus(wheel_primes),
            "capacity": capacity,
            "delta_minus_capacity": delta_phi - capacity,
            "positive_by_capacity": delta_phi > capacity,
            "deletion_from_previous": None if previous_capacity is None else previous_capacity - capacity,
        }
        previous_capacity = capacity

    dynamic_primes = sqrt_wheel_primes(P, primes_2p)
    exact_capacity = capacity_from_candidates(candidates, dynamic_primes)
    capacities["sqrt(2P)-wheel"] = {
        "wheel_primes": dynamic_primes,
        "wheel_prime_count": len(dynamic_primes),
        "largest_wheel_prime": dynamic_primes[-1] if dynamic_primes else None,
        "capacity": exact_capacity,
        "delta_minus_capacity": delta_phi - exact_capacity,
        "positive_by_capacity": delta_phi > exact_capacity,
        "deletion_from_previous": previous_capacity - exact_capacity if previous_capacity is not None else None,
    }

    profile = {
        "P": P,
        "k": k,
        "p_half": next_prime_after_half(P, primes_2p),
        "in_shadow_free_subband": k <= shadow_free_cap(P),
        "in_upper_band": k >= upper_band_first_k(P),
        "in_bhp_remaining_high_band": k >= high_band_lower_k(P),
        "integer_window_capacity": len(candidates),
        "forest_hole_count": holes,
        "direct_prime_count": direct_prime_count,
        "delta_phi_half": delta_phi,
        "exact_capacity_equals_holes": exact_capacity == holes,
        "exact_margin_equals_direct_prime_count": (
            direct_prime_count is None or delta_phi - exact_capacity == direct_prime_count
        ),
        "capacity_layers": capacities,
    }
    return profile


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
            delta_phi = finite_delta_phi_half(P, k, spf, next_prime_after_half(P, primes_2p))
            direct = finite_direct_prime_count(P, k, spf)
            rows.append(row_profile(P, k, primes_2p, lambda value: spf[value] == value, delta_phi, direct))

    layer_summary: dict[str, dict[str, Any]] = {}
    layer_names = [name for name, _ in FIXED_WHEEL_LAYERS] + ["sqrt(2P)-wheel"]
    for name in layer_names:
        layer_rows = [row["capacity_layers"][name] for row in rows]
        min_index, min_layer = min(
            enumerate(layer_rows),
            key=lambda item: item[1]["delta_minus_capacity"],
        )
        layer_summary[name] = {
            "closed_count": sum(item["positive_by_capacity"] for item in layer_rows),
            "not_closed_count": sum(not item["positive_by_capacity"] for item in layer_rows),
            "minimum_delta_minus_capacity": min_layer["delta_minus_capacity"],
            "minimum_row": {
                "P": rows[min_index]["P"],
                "k": rows[min_index]["k"],
                "delta_phi_half": rows[min_index]["delta_phi_half"],
                "capacity": min_layer["capacity"],
                "forest_hole_count": rows[min_index]["forest_hole_count"],
                "direct_prime_count": rows[min_index]["direct_prime_count"],
            },
        }

    sample_keys = {(11, 10), (19, 15), (101, 100), (257, 256), (1009, 1008)}
    sample_rows = [row for row in rows if (row["P"], row["k"]) in sample_keys]
    return {
        "max_prime": max_prime,
        "row_count": len(rows),
        "layer_summary": layer_summary,
        "all_exact_capacity_equals_holes": all(row["exact_capacity_equals_holes"] for row in rows),
        "all_exact_margin_equals_direct_prime_count": all(
            row["exact_margin_equals_direct_prime_count"] for row in rows
        ),
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 primorial-wheel 阶梯读数。"""
    max_seed = max(seeds) + 10000
    flags = prime_flags(2 * max_seed)
    samples: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        low_primes = primes_from_flags(flags, P // 2)
        primes_2p = primes_from_flags(flags, 2 * P)
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
            delta_phi = segment_delta_phi_half(P, k, low_primes)
            samples.append(row_profile(P, k, primes_2p, lambda value: bool(flags[value]), delta_phi, None))

    layer_names = [name for name, _ in FIXED_WHEEL_LAYERS] + ["sqrt(2P)-wheel"]
    layer_summary: dict[str, dict[str, Any]] = {}
    for name in layer_names:
        layer_rows = [row["capacity_layers"][name] for row in samples]
        layer_summary[name] = {
            "minimum_delta_minus_capacity": min(item["delta_minus_capacity"] for item in layer_rows),
            "all_sampled_positive": all(item["positive_by_capacity"] for item in layer_rows),
        }
    return {
        "sample_seeds": seeds,
        "sample_count": len(samples),
        "layer_summary": layer_summary,
        "all_sample_exact_capacity_equals_holes": all(row["exact_capacity_equals_holes"] for row in samples),
        "sample_rows": samples,
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
            "FinitePrimorialWheelLadderMonotoneTightening",
            True,
            True,
            "2,6,30,210,2310,... wheel 只会删除 forced-composite cofactor 候选，容量单调不增。",
            "capacity ladder registered",
        ),
        gate(
            "SqrtCofactorWheelEqualsActualForestHoles",
            True,
            True,
            "当 wheel primes 覆盖到 sqrt(2P) 时，每个 m<2P 的合数都有已覆盖小因子，故容量等于真实 prime-cofactor forest holes。",
            "exact hole count",
        ),
        gate(
            "InfinitePrimorialLimitIsIndependentProof",
            False,
            False,
            "极限容量等于 |F(P,k)| 后，DeltaPhi_half>C_limit 正是行内素数存在本身。",
            "positivity still required",
        ),
        gate(
            "PhiLPFParityBarrierBrokenGlobally",
            False,
            False,
            "primorial wheel 极限是精确化，不是 signed dispersion、sqrt-scale 短区间或新自守端点证明。",
            "signed/dispersion or structural lower bound required",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层不证明 H_P、外部引理版或内部自足版无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sample_table(rows: list[dict[str, Any]]) -> str:
    """输出样本行 Markdown 表。"""
    lines = [
        "| P | k | Delta | W_int | C_30 | C_210 | C_2310 | C_sqrt | holes | primes |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        layers = row["capacity_layers"]
        lines.append(
            f"| {row['P']} | {row['k']} | {row['delta_phi_half']} | {row['integer_window_capacity']} | "
            f"{layers['30-wheel']['capacity']} | {layers['210-wheel']['capacity']} | "
            f"{layers['2310-wheel']['capacity']} | {layers['sqrt(2P)-wheel']['capacity']} | "
            f"{row['forest_hole_count']} | {row.get('direct_prime_count') or ''} |"
        )
    return "\n".join(lines)


def layer_summary_table(summary: dict[str, dict[str, Any]]) -> str:
    """输出 layer summary Markdown 表。"""
    lines = [
        "| layer | closed | not closed | min Delta-C | min row |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for name in [name for name, _ in FIXED_WHEEL_LAYERS] + ["sqrt(2P)-wheel"]:
        item = summary[name]
        row = item["minimum_row"]
        lines.append(
            f"| {name} | {item['closed_count']} | {item['not_closed_count']} | "
            f"{item['minimum_delta_minus_capacity']} | P={row['P']}, k={row['k']} |"
        )
    return "\n".join(lines)


def gates_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=bool_text(item["closed"]),
                proved=bool_text(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    finite = finite_audit()
    large = large_sample_audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_primorial_wheel_limit_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "primorial_wheel_ladder_tightens_but_limit_is_exact_tautology",
        "fixed_wheel_layers": [
            {"name": name, "wheel_primes": primes, "wheel_modulus": wheel_modulus(primes)}
            for name, primes in FIXED_WHEEL_LAYERS
        ],
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "limit_statement": {
            "sqrt_wheel_exact_hole_count": True,
            "reason": "every composite m<2P has a prime factor <=sqrt(2P-1)",
            "limit_capacity": "|F(P,k)|",
            "limit_positivity_condition": "DeltaPhi_half(P,k)>|F(P,k)|",
            "equivalent_to": "pi((k+1)P-1)-pi(kP)>0",
            "independent_closure": False,
        },
        "next_direct_attack_target": (
            "PuncturedSqrtWheelExactForestHolePositivityOrSignedDispersion"
            "OrSpecialSquarePhaseLowerBound"
        ),
        "primorial_wheel_ladder_tightened": True,
        "sqrt_wheel_limit_exact": True,
        "primorial_limit_independent_proof": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    finite = payload["finite_audit"]
    large = payload["large_sample_audit"]
    lines = [
        "# Prime Matrix Phi-LPF primorial-wheel limit 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 直接回答",
        "",
        "可以继续从 `30` 推进到 `210, 2310, ...`，而且容量会单调收紧。",
        "但这条路线的极限不是自动证明；当 wheel primes 覆盖到 `sqrt(2P)` 后，",
        "`C_wheel(P,k)` 已经等于真实 forest-hole 数 `|F(P,k)|`。",
        "于是 `DeltaPhi_half(P,k)>C_wheel(P,k)` 正好等价于行内素数存在。",
        "",
        "## 2. 有限层审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"row_count={finite['row_count']}",
        f"all_exact_capacity_equals_holes={bool_text(finite['all_exact_capacity_equals_holes'])}",
        f"all_exact_margin_equals_direct_prime_count={bool_text(finite['all_exact_margin_equals_direct_prime_count'])}",
        f"finite_evidence_not_used_as_global_proof={bool_text(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        layer_summary_table(finite["layer_summary"]),
        "",
        "代表样本：",
        "",
        sample_table(finite["sample_rows"]),
        "",
        "## 3. 大尺度抽样",
        "",
        "```text",
        f"sample_seeds={large['sample_seeds']}",
        f"sample_count={large['sample_count']}",
        f"all_sample_exact_capacity_equals_holes={bool_text(large['all_sample_exact_capacity_equals_holes'])}",
        f"large_samples_are_evidence_not_global_proof={bool_text(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        "大样本 layer 最小余量：",
        "",
        "```text",
        *[
            f"{name}: min Delta-C={item['minimum_delta_minus_capacity']}, all_positive={bool_text(item['all_sampled_positive'])}"
            for name, item in large["layer_summary"].items()
        ],
        "```",
        "",
        "## 4. 极限判定",
        "",
        "若 wheel primes 覆盖到 `sqrt(2P-1)`，则每个合数 `m<2P` 都有一个已覆盖素因子。",
        "因此 reciprocal cofactor 窗中未被删除的 `m` 恰好是素数，容量上界变成精确等式：",
        "",
        "```text",
        "C_sqrt(P,k)=|F(P,k)|",
        "DeltaPhi_half(P,k)-C_sqrt(P,k)=pi((k+1)P-1)-pi(kP)",
        "```",
        "",
        "这说明 primorial ladder 的极限是目标命题的等价重述，不是独立闭合证明。",
        "",
        "## 5. 判定表",
        "",
        gates_markdown(payload["gates"]),
        "",
        "## 6. 当前最窄口",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "```text",
        f"primorial_wheel_ladder_tightened={bool_text(payload['primorial_wheel_ladder_tightened'])}",
        f"sqrt_wheel_limit_exact={bool_text(payload['sqrt_wheel_limit_exact'])}",
        f"primorial_limit_independent_proof={bool_text(payload['primorial_limit_independent_proof'])}",
        f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("sqrt_wheel_limit_exact=true")
    print("primorial_limit_independent_proof=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
