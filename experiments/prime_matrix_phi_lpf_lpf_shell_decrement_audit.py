#!/usr/bin/env python3
"""审计 Phi-LPF fixed-wheel residual 的 LPF shell 递归剥离律。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_lpf_shell_decrement_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-lpf-shell-decrement-audit.json

本层把 fixed-wheel residual R_S(P,k) 继续拆成最小素因子互斥桶。若
m 是未被当前 wheel 删除的合成 cofactor，令 r=LPF(m)，则
m=r*a，a>=r，且 a 没有小于 r 的素因子。于是每次 primorial wheel
从 y 推进到下一个素数 r，容量下降恰好等于 LPF=r 的 shell。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, Callable

from prime_matrix_phi_lpf_fixed_wheel_residual_rough_composite_audit import (
    finite_delta_and_prime_count,
    is_prime_from_spf,
    lpf_from_spf,
)
from prime_matrix_phi_lpf_primorial_wheel_limit_audit import (
    DATA,
    DOCS,
    FIXED_WHEEL_LAYERS,
    LARGE_SAMPLE_SEEDS,
    MAX_PRIME_AUDIT,
    ROOT,
    bool_text,
    candidate_m_values,
    capacity_from_candidates,
    cell,
    high_band_lower_k,
    next_prime_after_half,
    next_prime_at_least,
    prime_flags,
    primes_from_spf,
    segment_delta_phi_half,
    shadow_free_cap,
    spf_table,
    sqrt_wheel_primes,
    upper_band_first_k,
    wheel_modulus,
)


SLUG = "prime-matrix-phi-lpf-lpf-shell-decrement"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
SHELL_DISPLAY_PRIMES = [2, 3, 5, 7, 11, 13]

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-fixed-wheel-residual-rough-composite-audit.json",
    DOCS / "prime-matrix-phi-lpf-primorial-wheel-limit-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def bool_count(rows: list[dict[str, Any]], key: str) -> int:
    """统计布尔字段为真的行数。"""
    return sum(1 for row in rows if row[key])


def layer_sequence(P: int, primes_2p: list[int]) -> list[dict[str, Any]]:
    """列出 integer、固定 primorial wheel 与动态 sqrt wheel。"""
    sequence: list[dict[str, Any]] = [
        {"name": "integer-window", "wheel_primes": [], "wheel_modulus": 1}
    ]
    for name, primes in FIXED_WHEEL_LAYERS:
        sequence.append({"name": name, "wheel_primes": primes, "wheel_modulus": wheel_modulus(primes)})
    dynamic = sqrt_wheel_primes(P, primes_2p)
    sequence.append(
        {
            "name": "sqrt(2P)-wheel",
            "wheel_primes": dynamic,
            "wheel_prime_count": len(dynamic),
            "largest_wheel_prime": dynamic[-1] if dynamic else None,
            "wheel_modulus": None,
        }
    )
    return sequence


def cutoff_prime(layer: dict[str, Any]) -> int:
    """返回初段 wheel 的最大素数。"""
    primes = layer["wheel_primes"]
    return primes[-1] if primes else 1


def lpf_shells(
    candidates: list[int],
    is_prime: Callable[[int], bool],
    least_prime_factor: Callable[[int], int | None],
) -> dict[str, Any]:
    """把候选 cofactor 拆成 prime holes 与 composite LPF shells。"""
    holes = 0
    shells: Counter[int] = Counter()
    factorization_failures: list[dict[str, int]] = []
    for m in candidates:
        if is_prime(m):
            holes += 1
            continue
        r = least_prime_factor(m)
        if r is None:
            continue
        a = m // r
        a_lpf = least_prime_factor(a)
        if a < r or (a_lpf is not None and a_lpf < r):
            factorization_failures.append({"m": m, "r": r, "a": a, "a_lpf": a_lpf or a})
        shells[r] += 1
    return {
        "holes": holes,
        "shells": dict(sorted(shells.items())),
        "factorization_failures": factorization_failures,
    }


def residual_after_cutoff(shells: dict[int, int], cutoff: int) -> int:
    """计算 LPF 大于 cutoff 的 residual。"""
    return sum(count for prime, count in shells.items() if prime > cutoff)


def shell_sum_between(shells: dict[int, int], low: int, high: int) -> int:
    """计算 low < LPF <= high 的 shell 总量。"""
    return sum(count for prime, count in shells.items() if low < prime <= high)


def display_shells(shells: dict[int, int], sqrt_cutoff: int) -> dict[str, int]:
    """生成压缩 shell 展示。"""
    result: dict[str, int] = {}
    for prime in SHELL_DISPLAY_PRIMES:
        result[str(prime)] = shells.get(prime, 0)
    result["tail_ge_17"] = sum(count for prime, count in shells.items() if prime >= 17)
    result["tail_to_sqrt"] = sum(count for prime, count in shells.items() if prime <= sqrt_cutoff and prime >= 17)
    return result


def row_profile(
    P: int,
    k: int,
    primes_2p: list[int],
    is_prime: Callable[[int], bool],
    least_prime_factor: Callable[[int], int | None],
    delta_phi: int,
    direct_prime_count: int | None = None,
) -> dict[str, Any]:
    """构造单行 LPF shell 递归剥离读数。"""
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    candidates = candidate_m_values(P, k, high_q_primes)
    shell_data = lpf_shells(candidates, is_prime, least_prime_factor)
    shells = {int(prime): count for prime, count in shell_data["shells"].items()}
    holes = shell_data["holes"]
    row_prime_count = direct_prime_count if direct_prime_count is not None else delta_phi - holes
    sequence = layer_sequence(P, primes_2p)

    layers: dict[str, dict[str, Any]] = {}
    capacity_reconstruction_failures: list[str] = []
    for layer in sequence:
        name = layer["name"]
        cutoff = cutoff_prime(layer)
        residual = residual_after_cutoff(shells, cutoff)
        reconstructed_capacity = holes + residual
        direct_capacity = capacity_from_candidates(candidates, layer["wheel_primes"])
        if reconstructed_capacity != direct_capacity:
            capacity_reconstruction_failures.append(name)
        layers[name] = {
            "cutoff_prime": cutoff,
            "capacity": direct_capacity,
            "reconstructed_capacity_from_lpf_shells": reconstructed_capacity,
            "rough_composite_residual": residual,
            "delta_minus_capacity": delta_phi - direct_capacity,
            "prime_count_minus_residual": row_prime_count - residual,
        }

    decrements: list[dict[str, Any]] = []
    for left, right in zip(sequence, sequence[1:]):
        left_name = left["name"]
        right_name = right["name"]
        left_cutoff = cutoff_prime(left)
        right_cutoff = cutoff_prime(right)
        capacity_drop = layers[left_name]["capacity"] - layers[right_name]["capacity"]
        shell_drop = shell_sum_between(shells, left_cutoff, right_cutoff)
        decrements.append(
            {
                "from": left_name,
                "to": right_name,
                "added_lpf_interval": f"({left_cutoff},{right_cutoff}]",
                "capacity_drop": capacity_drop,
                "lpf_shell_drop": shell_drop,
                "decrement_identity_holds": capacity_drop == shell_drop,
            }
        )

    sqrt_cutoff = cutoff_prime(sequence[-1])
    return {
        "P": P,
        "k": k,
        "p_half": next_prime_after_half(P, primes_2p),
        "in_shadow_free_subband": k <= shadow_free_cap(P),
        "in_upper_band": k >= upper_band_first_k(P),
        "in_bhp_remaining_high_band": k >= high_band_lower_k(P),
        "integer_window_capacity": len(candidates),
        "delta_phi_half": delta_phi,
        "forest_hole_count": holes,
        "row_prime_count_from_identity": row_prime_count,
        "direct_prime_count": direct_prime_count,
        "lpf_shells": display_shells(shells, sqrt_cutoff),
        "all_lpf_factorizations_ordered": not shell_data["factorization_failures"],
        "factorization_failure_count": len(shell_data["factorization_failures"]),
        "capacity_reconstruction_failures": capacity_reconstruction_failures,
        "all_capacity_reconstructed_from_lpf_shells": not capacity_reconstruction_failures,
        "decrements": decrements,
        "all_adjacent_decrements_equal_lpf_shells": all(
            item["decrement_identity_holds"] for item in decrements
        ),
        "layers": layers,
    }


def compact_row(row: dict[str, Any]) -> dict[str, Any]:
    """压缩行读数。"""
    return {
        "P": row["P"],
        "k": row["k"],
        "Delta": row["delta_phi_half"],
        "N": row["row_prime_count_from_identity"],
        "holes": row["forest_hole_count"],
        "W_int": row["layers"]["integer-window"]["capacity"],
        "C_30": row["layers"]["30-wheel"]["capacity"],
        "R_30": row["layers"]["30-wheel"]["rough_composite_residual"],
        "R_210": row["layers"]["210-wheel"]["rough_composite_residual"],
        "R_2310": row["layers"]["2310-wheel"]["rough_composite_residual"],
        "R_sqrt": row["layers"]["sqrt(2P)-wheel"]["rough_composite_residual"],
        "shells": row["lpf_shells"],
    }


def summarize_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """生成审计汇总。"""
    aggregate_shells: Counter[str] = Counter()
    for row in rows:
        aggregate_shells.update(row["lpf_shells"])
    min_r30_row = min(rows, key=lambda row: row["layers"]["30-wheel"]["prime_count_minus_residual"])
    max_tail_row = max(rows, key=lambda row: row["lpf_shells"]["tail_ge_17"])
    sample_keys = {(11, 10), (19, 15), (101, 100), (257, 256), (1009, 1008)}
    return {
        "row_count": len(rows),
        "all_lpf_factorizations_ordered": bool_count(rows, "all_lpf_factorizations_ordered") == len(rows),
        "all_capacity_reconstructed_from_lpf_shells": bool_count(
            rows, "all_capacity_reconstructed_from_lpf_shells"
        )
        == len(rows),
        "all_adjacent_decrements_equal_lpf_shells": bool_count(
            rows, "all_adjacent_decrements_equal_lpf_shells"
        )
        == len(rows),
        "aggregate_lpf_shells": dict(aggregate_shells),
        "minimum_prime_minus_R30_row": compact_row(min_r30_row),
        "maximum_tail_ge_17_row": compact_row(max_tail_row),
        "sample_rows": [compact_row(row) for row in rows if (row["P"], row["k"]) in sample_keys],
    }


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计；只作一致性检查，不作全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    rows: list[dict[str, Any]] = []
    for P in primes:
        if P < 11:
            continue
        p_half = next_prime_after_half(P, primes_2p)
        for k in range(2, P):
            delta_phi, direct = finite_delta_and_prime_count(P, k, spf, p_half)
            rows.append(
                row_profile(
                    P,
                    k,
                    primes_2p,
                    lambda value, table=spf: is_prime_from_spf(table, value),
                    lambda value, table=spf: lpf_from_spf(table, value),
                    delta_phi,
                    direct,
                )
            )
    summary = summarize_rows(rows)
    summary["max_prime"] = max_prime
    summary["finite_evidence_not_used_as_global_proof"] = True
    return summary


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 LPF shell 读数。"""
    max_seed = max(seeds) + 10000
    spf = spf_table(2 * max_seed)
    flags = prime_flags(2 * max_seed)
    samples: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        low_primes = primes_from_spf(spf, P // 2)
        primes_2p = primes_from_spf(spf, 2 * P)
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
            samples.append(
                row_profile(
                    P,
                    k,
                    primes_2p,
                    lambda value, table=spf: is_prime_from_spf(table, value),
                    lambda value, table=spf: lpf_from_spf(table, value),
                    delta_phi,
                    None,
                )
            )
    summary = summarize_rows(samples)
    summary["sample_seeds"] = seeds
    summary["sample_count"] = len(samples)
    summary["large_samples_are_evidence_not_global_proof"] = True
    return summary


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
            "LPFShellOrderedFactorization",
            True,
            True,
            "每个合成 cofactor 唯一写成 m=r*a，其中 r=LPF(m)，a>=r 且 a 为 r-rough。",
            "ordered LPF shell ledger",
        ),
        gate(
            "AdjacentWheelDropEqualsNewLPFShell",
            True,
            True,
            "primorial wheel 从 y 加到 y' 时，容量下降等于 y<LPF(m)<=y' 的 shell。",
            "C_y-C_yprime=shell(y,yprime]",
        ),
        gate(
            "ResidualEqualsTailLPFShellSum",
            True,
            True,
            "固定 wheel residual 等于 LPF 大于 wheel cutoff 的 shell 尾和。",
            "R_y=sum_{r>y} Shell_r",
        ),
        gate(
            "PrimeDominatesEveryTailGlobally",
            False,
            False,
            "有限审计中 N>R_30，但尚未证明所有 P,k 的同对象素数数支配 LPF 尾和。",
            "PrimeCountDominatesLPFTailShellSum",
        ),
        gate(
            "ExternalRoughNumberTheoremClosesPointwiseRows",
            False,
            False,
            "现有 rough-number 短区间/方差结果控制普通 rough 集合，尚不匹配本文 reciprocal-window 加权同对象 residual。",
            "same-row signed residual theorem required",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层不证明 H_P、外部引理版或内部自足版无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def row_table(rows: list[dict[str, Any]]) -> str:
    """输出样本行表。"""
    lines = [
        "| P | k | Delta | N | holes | W_int | C_30 | R_30 | R_210 | R_2310 | R_sqrt | shells |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        shells = ", ".join(f"{key}:{value}" for key, value in row["shells"].items() if value)
        lines.append(
            f"| {row['P']} | {row['k']} | {row['Delta']} | {row['N']} | {row['holes']} | "
            f"{row['W_int']} | {row['C_30']} | {row['R_30']} | {row['R_210']} | "
            f"{row['R_2310']} | {row['R_sqrt']} | {cell(shells)} |"
        )
    return "\n".join(lines)


def shell_summary_text(shells: dict[str, int]) -> str:
    """输出 shell 汇总。"""
    keys = [str(prime) for prime in SHELL_DISPLAY_PRIMES] + ["tail_ge_17"]
    return "\n".join(f"{key}={shells.get(key, 0)}" for key in keys)


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
        "certificate_type": "prime_matrix_phi_lpf_lpf_shell_decrement_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "fixed_wheel_residual_split_into_lpf_shell_decrement_law",
        "definitions": {
            "Shell_r(P,k)": "candidate cofactor multiplicity with LPF(m)=r",
            "ordered_factorization": "m=r*a, r=LPF(m), a>=r, and a is r-rough",
            "wheel_decrement": "C_y(P,k)-C_yprime(P,k)=sum_{y<r<=yprime} Shell_r(P,k)",
            "residual_tail": "R_y(P,k)=sum_{r>y} Shell_r(P,k)",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "external_frontier_note": (
            "Recent rough-number short-interval variance results are relevant as diagnostics, "
            "but they do not give the required pointwise same-row weighted residual dominance."
        ),
        "next_direct_attack_target": (
            "PrimeCountDominatesLPFTailShellSum OR signed shell cancellation "
            "OR square-phase endpoint lower bound"
        ),
        "lpf_shell_decrement_law_closed": True,
        "fixed_wheel_residual_dominance_global_closed": False,
        "external_rough_number_theorem_closes_pointwise_rows": False,
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
        "# Prime Matrix Phi-LPF LPF shell decrement 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子分解",
        "",
        "对每个合成 cofactor `m`，令 `r=LPF(m)`。唯一分解为：",
        "",
        "```text",
        "m=r*a,  a>=r,  every prime divisor of a is >=r",
        "```",
        "",
        "因此 fixed-wheel residual 是 LPF shell 尾和：",
        "",
        "```text",
        "R_y(P,k)=sum_{r>y} Shell_r(P,k)",
        "C_y(P,k)-C_y'(P,k)=sum_{y<r<=y'} Shell_r(P,k)",
        "```",
        "",
        "这把 residual 从黑箱尾项拆成互斥 LPF 桶；继续加 primorial wheel 的每一步",
        "都只是剥离一个或一段 LPF shell。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"row_count={finite['row_count']}",
        f"all_lpf_factorizations_ordered={bool_text(finite['all_lpf_factorizations_ordered'])}",
        f"all_capacity_reconstructed_from_lpf_shells={bool_text(finite['all_capacity_reconstructed_from_lpf_shells'])}",
        f"all_adjacent_decrements_equal_lpf_shells={bool_text(finite['all_adjacent_decrements_equal_lpf_shells'])}",
        f"finite_evidence_not_used_as_global_proof={bool_text(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "有限 LPF shell 汇总：",
        "",
        "```text",
        shell_summary_text(finite["aggregate_lpf_shells"]),
        "```",
        "",
        "代表样本：",
        "",
        row_table(finite["sample_rows"]),
        "",
        "最小 `N-R_30` 行：",
        "",
        row_table([finite["minimum_prime_minus_R30_row"]]),
        "",
        "最大 `tail_ge_17` 行：",
        "",
        row_table([finite["maximum_tail_ge_17_row"]]),
        "",
        "## 3. 大尺度抽样",
        "",
        "```text",
        f"sample_seeds={large['sample_seeds']}",
        f"sample_count={large['sample_count']}",
        f"all_lpf_factorizations_ordered={bool_text(large['all_lpf_factorizations_ordered'])}",
        f"all_capacity_reconstructed_from_lpf_shells={bool_text(large['all_capacity_reconstructed_from_lpf_shells'])}",
        f"all_adjacent_decrements_equal_lpf_shells={bool_text(large['all_adjacent_decrements_equal_lpf_shells'])}",
        f"large_samples_are_evidence_not_global_proof={bool_text(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        "大样本 LPF shell 汇总：",
        "",
        "```text",
        shell_summary_text(large["aggregate_lpf_shells"]),
        "```",
        "",
        "## 4. 外部定理验收边界",
        "",
        "Rough-number 短区间与方差理论可作为密度诊断，但本文需要的是",
        "`reciprocal-window` 加权、逐行点态、同对象的 prime-minus-shell-tail 支配。",
        "因此现有 rough-number 方差输入不能直接替代：",
        "",
        "```text",
        "PrimeCountDominatesLPFTailShellSum",
        "```",
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
        f"lpf_shell_decrement_law_closed={bool_text(payload['lpf_shell_decrement_law_closed'])}",
        f"fixed_wheel_residual_dominance_global_closed={bool_text(payload['fixed_wheel_residual_dominance_global_closed'])}",
        f"external_rough_number_theorem_closes_pointwise_rows={bool_text(payload['external_rough_number_theorem_closes_pointwise_rows'])}",
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
    print("lpf_shell_decrement_law_closed=true")
    print("fixed_wheel_residual_dominance_global_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
