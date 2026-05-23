#!/usr/bin/env python3
"""审计固定 wheel 与精确 sqrt-wheel 之间的 rough-composite residual。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_fixed_wheel_residual_rough_composite_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-fixed-wheel-residual-rough-composite-audit.json

本层接在 primorial-wheel limit 之后。前一层已经证明动态 sqrt-wheel
容量等于真实 forest holes。本层把任意固定 wheel 的多余容量显式拆成
y-rough composite cofactor residual：

  C_S(P,k)=|F(P,k)|+R_S(P,k)
  DeltaPhi_half(P,k)-C_S(P,k)=N(P,k)-R_S(P,k)

因此固定 wheel 的正性证明比目标更强：它必须证明行内素数数 N(P,k)
严格支配尚未被小素数删掉的 rough-composite residual R_S(P,k)。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, Callable

from prime_matrix_phi_lpf_primorial_wheel_limit_audit import (
    DATA,
    DOCS,
    FIXED_WHEEL_LAYERS,
    LARGE_SAMPLE_SEEDS,
    MAX_PRIME_AUDIT,
    ROOT,
    bool_text,
    candidate_m_values,
    cell,
    capacity_from_candidates,
    forced_by_wheel,
    high_band_lower_k,
    next_prime_after_half,
    next_prime_at_least,
    prime_flags,
    primes_from_flags,
    primes_from_spf,
    segment_delta_phi_half,
    shadow_free_cap,
    spf_table,
    sqrt_wheel_primes,
    upper_band_first_k,
    wheel_modulus,
)


SLUG = "prime-matrix-phi-lpf-fixed-wheel-residual-rough-composite"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-router.json",
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


def is_prime_from_spf(spf: list[int], value: int) -> bool:
    """用 SPF 表判断素数。"""
    return value >= 2 and spf[value] == value


def lpf_from_spf(spf: list[int], value: int) -> int | None:
    """返回合数的最小素因子；素数返回 None。"""
    if value < 2 or spf[value] == value:
        return None
    return spf[value]


def residual_lpf_histogram(
    candidates: list[int],
    wheel_primes: list[int],
    is_prime: Callable[[int], bool],
    least_prime_factor: Callable[[int], int | None],
) -> dict[str, int]:
    """统计固定 wheel 下未删除的合成 cofactor 的 LPF 分布。"""
    counts: Counter[str] = Counter()
    for m in candidates:
        if forced_by_wheel(m, wheel_primes) or is_prime(m):
            continue
        lpf = least_prime_factor(m)
        counts[str(lpf if lpf is not None else "unknown")] += 1
    return dict(sorted(counts.items(), key=lambda item: int(item[0]) if item[0].isdigit() else 10**9))


def compact_histogram(histogram: dict[str, int], limit: int = 8) -> dict[str, int]:
    """压缩 LPF 直方图，避免证书过大。"""
    ordered = sorted(histogram.items(), key=lambda item: (-item[1], int(item[0]) if item[0].isdigit() else 10**9))
    top = dict(ordered[:limit])
    remaining = sum(value for _, value in ordered[limit:])
    if remaining:
        top["other"] = remaining
    return top


def layer_names() -> list[str]:
    """返回固定层加动态精确层。"""
    return [name for name, _ in FIXED_WHEEL_LAYERS] + ["sqrt(2P)-wheel"]


def finite_delta_and_prime_count(P: int, k: int, spf: list[int], p_half: int) -> tuple[int, int]:
    """一次扫描同时计算 DeltaPhi_half 与行内素数数。"""
    delta_phi = 0
    prime_count = 0
    base = k * P
    for t in range(1, P):
        value = base + t
        if spf[value] >= p_half:
            delta_phi += 1
        if spf[value] == value:
            prime_count += 1
    return delta_phi, prime_count


def layer_primes(name: str, P: int, primes_2p: list[int]) -> list[int]:
    """返回指定容量层使用的 wheel primes。"""
    if name == "sqrt(2P)-wheel":
        return sqrt_wheel_primes(P, primes_2p)
    for layer_name, primes in FIXED_WHEEL_LAYERS:
        if layer_name == name:
            return primes
    raise KeyError(name)


def row_residual_profile(
    P: int,
    k: int,
    primes_2p: list[int],
    is_prime: Callable[[int], bool],
    least_prime_factor: Callable[[int], int | None],
    delta_phi: int,
    direct_prime_count: int | None = None,
) -> dict[str, Any]:
    """构造一行的 residual 分解读数。"""
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    candidates = candidate_m_values(P, k, high_q_primes)
    holes = sum(1 for m in candidates if is_prime(m))
    row_prime_count = direct_prime_count if direct_prime_count is not None else delta_phi - holes
    layers: dict[str, dict[str, Any]] = {}
    for name in layer_names():
        primes = layer_primes(name, P, primes_2p)
        capacity = capacity_from_candidates(candidates, primes)
        residual = sum(1 for m in candidates if (not forced_by_wheel(m, primes)) and (not is_prime(m)))
        layers[name] = {
            "wheel_primes": primes,
            "wheel_modulus": None if name == "sqrt(2P)-wheel" else wheel_modulus(primes),
            "capacity": capacity,
            "rough_composite_residual": residual,
            "capacity_minus_holes": capacity - holes,
            "prime_count_minus_residual": row_prime_count - residual,
            "delta_minus_capacity": delta_phi - capacity,
            "residual_zero": residual == 0,
            "capacity_equals_holes_plus_residual": capacity == holes + residual,
            "lpf_histogram": compact_histogram(
                residual_lpf_histogram(candidates, primes, is_prime, least_prime_factor)
            ),
        }

    return {
        "P": P,
        "k": k,
        "p_half": next_prime_after_half(P, primes_2p),
        "in_shadow_free_subband": k <= shadow_free_cap(P),
        "in_upper_band": k >= upper_band_first_k(P),
        "in_bhp_remaining_high_band": k >= high_band_lower_k(P),
        "integer_window_capacity": len(candidates),
        "forest_hole_count": holes,
        "delta_phi_half": delta_phi,
        "direct_prime_count": direct_prime_count,
        "row_prime_count_from_identity": row_prime_count,
        "endpoint_identity_prime_count_used": direct_prime_count is None,
        "layers": layers,
    }


def compact_row(row: dict[str, Any], layer: str) -> dict[str, Any]:
    """压缩一行，供 summary/frontier 使用。"""
    item = row["layers"][layer]
    return {
        "P": row["P"],
        "k": row["k"],
        "Delta": row["delta_phi_half"],
        "holes": row["forest_hole_count"],
        "prime_count": row["row_prime_count_from_identity"],
        "capacity": item["capacity"],
        "residual": item["rough_composite_residual"],
        "prime_minus_residual": item["prime_count_minus_residual"],
        "delta_minus_capacity": item["delta_minus_capacity"],
        "lpf_histogram": item["lpf_histogram"],
    }


def summarize_layers(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """生成各层 residual 摘要。"""
    summaries: dict[str, dict[str, Any]] = {}
    for name in layer_names():
        layer_rows = [row["layers"][name] for row in rows]
        min_margin_index, min_margin = min(
            enumerate(layer_rows),
            key=lambda item: item[1]["prime_count_minus_residual"],
        )
        max_residual_index, max_residual = max(
            enumerate(layer_rows),
            key=lambda item: item[1]["rough_composite_residual"],
        )
        total_residual = sum(item["rough_composite_residual"] for item in layer_rows)
        total_prime_count = sum(row["row_prime_count_from_identity"] for row in rows)
        lpf_counter: Counter[str] = Counter()
        for item in layer_rows:
            lpf_counter.update(item["lpf_histogram"])
        summaries[name] = {
            "row_count": len(rows),
            "residual_zero_count": sum(item["residual_zero"] for item in layer_rows),
            "residual_positive_count": sum(not item["residual_zero"] for item in layer_rows),
            "all_capacity_equals_holes_plus_residual": all(
                item["capacity_equals_holes_plus_residual"] for item in layer_rows
            ),
            "all_prime_count_dominates_residual": all(
                item["prime_count_minus_residual"] > 0 for item in layer_rows
            ),
            "minimum_prime_count_minus_residual": min_margin["prime_count_minus_residual"],
            "maximum_rough_composite_residual": max_residual["rough_composite_residual"],
            "total_rough_composite_residual": total_residual,
            "total_prime_count_from_identity": total_prime_count,
            "total_residual_to_prime_ratio": total_residual / total_prime_count if total_prime_count else None,
            "minimum_margin_row": compact_row(rows[min_margin_index], name),
            "maximum_residual_row": compact_row(rows[max_residual_index], name),
            "aggregate_lpf_histogram": compact_histogram(dict(lpf_counter), limit=12),
        }
    return summaries


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
            delta_phi, direct = finite_delta_and_prime_count(
                P, k, spf, next_prime_after_half(P, primes_2p)
            )
            rows.append(
                row_residual_profile(
                    P,
                    k,
                    primes_2p,
                    lambda value, table=spf: is_prime_from_spf(table, value),
                    lambda value, table=spf: lpf_from_spf(table, value),
                    delta_phi,
                    direct,
                )
            )

    sample_keys = {(11, 10), (19, 15), (101, 100), (257, 256), (1009, 1008)}
    return {
        "max_prime": max_prime,
        "row_count": len(rows),
        "layer_summary": summarize_layers(rows),
        "all_sqrt_residual_zero": all(row["layers"]["sqrt(2P)-wheel"]["rough_composite_residual"] == 0 for row in rows),
        "all_fixed_capacity_decomposition_holds": all(
            row["layers"][name]["capacity_equals_holes_plus_residual"]
            for row in rows
            for name in layer_names()
        ),
        "all_delta_minus_capacity_equals_prime_minus_residual": all(
            row["layers"][name]["delta_minus_capacity"]
            == row["layers"][name]["prime_count_minus_residual"]
            for row in rows
            for name in layer_names()
        ),
        "sample_rows": [row for row in rows if (row["P"], row["k"]) in sample_keys],
        "finite_evidence_not_used_as_global_proof": True,
    }


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 residual 分解读数。"""
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
                row_residual_profile(
                    P,
                    k,
                    primes_2p,
                    lambda value, table=spf: is_prime_from_spf(table, value),
                    lambda value, table=spf: lpf_from_spf(table, value),
                    delta_phi,
                    None,
                )
            )

    return {
        "sample_seeds": seeds,
        "sample_count": len(samples),
        "layer_summary": summarize_layers(samples),
        "all_sample_sqrt_residual_zero": all(
            row["layers"]["sqrt(2P)-wheel"]["rough_composite_residual"] == 0 for row in samples
        ),
        "samples": samples,
        "large_samples_are_evidence_not_global_proof": True,
    }


def least_prime_factor_by_trial(value: int, primes: list[int], flags: bytearray) -> int | None:
    """备用试除工具；主流程使用 SPF 表。"""
    if value < 2 or flags[value]:
        return None
    for prime in primes:
        if prime * prime > value:
            break
        if value % prime == 0:
            return prime
    return None


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
            "FixedWheelResidualDecomposition",
            True,
            True,
            "任意固定 wheel 的容量精确拆成 prime-cofactor holes 加 rough-composite residual。",
            "C_S(P,k)=|F(P,k)|+R_S(P,k)",
        ),
        gate(
            "FixedWheelPositivityRequiresPrimeDominatesResidual",
            True,
            True,
            "DeltaPhi_half>C_S 等价于行内素数数 N(P,k) 严格大于 R_S(P,k)。",
            "PrimeCountDominatesFixedWheelRoughCompositeResidual",
        ),
        gate(
            "SqrtWheelResidualVanishes",
            True,
            True,
            "wheel primes 覆盖所有 ell<=sqrt(2P-1) 时，每个合成 m<2P 被删除，R_S=0。",
            "dynamic exact wheel",
        ),
        gate(
            "FixedWheelResidualDominanceProvedGlobally",
            False,
            False,
            "有限审计显示固定 wheel residual 被素数数支配，但尚无全局证明。",
            "signed dispersion or special square-phase lower bound required",
        ),
        gate(
            "PhiLPFParityBarrierBrokenGlobally",
            False,
            False,
            "本层只是把奇偶障碍剩余项显式物化；没有证明全局半窗素数存在。",
            "same-object prime-minus-rough-composite separation required",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层不证明 H_P、外部引理版或内部自足版无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def sample_table(rows: list[dict[str, Any]]) -> str:
    """输出样本行 Markdown 表。"""
    lines = [
        "| P | k | Delta | primes | holes | R_30 | R_210 | R_2310 | R_sqrt | primes-R_30 |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        layers = row["layers"]
        lines.append(
            f"| {row['P']} | {row['k']} | {row['delta_phi_half']} | "
            f"{row['row_prime_count_from_identity']} | {row['forest_hole_count']} | "
            f"{layers['30-wheel']['rough_composite_residual']} | "
            f"{layers['210-wheel']['rough_composite_residual']} | "
            f"{layers['2310-wheel']['rough_composite_residual']} | "
            f"{layers['sqrt(2P)-wheel']['rough_composite_residual']} | "
            f"{layers['30-wheel']['prime_count_minus_residual']} |"
        )
    return "\n".join(lines)


def layer_summary_table(summary: dict[str, dict[str, Any]]) -> str:
    """输出 layer summary Markdown 表。"""
    lines = [
        "| layer | residual>0 rows | max R | min primes-R | total R | R/primes | max-R row |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for name in layer_names():
        item = summary[name]
        row = item["maximum_residual_row"]
        ratio = item["total_residual_to_prime_ratio"]
        ratio_text = "" if ratio is None else f"{ratio:.6f}"
        lines.append(
            f"| {name} | {item['residual_positive_count']} | "
            f"{item['maximum_rough_composite_residual']} | "
            f"{item['minimum_prime_count_minus_residual']} | "
            f"{item['total_rough_composite_residual']} | {ratio_text} | "
            f"P={row['P']}, k={row['k']} |"
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
        "certificate_type": "prime_matrix_phi_lpf_fixed_wheel_residual_rough_composite_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "fixed_wheel_capacity_gap_equals_rough_composite_residual",
        "definitions": {
            "C_S(P,k)": "fixed-wheel reciprocal-window capacity after deleting S-forced composite cofactors",
            "F(P,k)": "prime-cofactor forest-hole multiset counted with q-window multiplicity",
            "R_S(P,k)": "composite cofactors not deleted by S, counted with the same multiplicity",
            "N(P,k)": "pi((k+1)P-1)-pi(kP)",
            "exact_decomposition": "C_S(P,k)=|F(P,k)|+R_S(P,k)",
            "fixed_wheel_margin": "DeltaPhi_half(P,k)-C_S(P,k)=N(P,k)-R_S(P,k)",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "next_direct_attack_target": (
            "PrimeCountDominatesFixedWheelRoughCompositeResidual "
            "OR same-object signed dispersion "
            "OR special square-phase lower bound"
        ),
        "fixed_wheel_residual_decomposition_closed": True,
        "sqrt_wheel_residual_zero_closed": True,
        "fixed_wheel_residual_dominance_global_closed": False,
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
        "# Prime Matrix Phi-LPF fixed-wheel rough-composite residual 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子分解",
        "",
        "设 `S` 为固定 wheel primes，`C_S(P,k)` 为删去 `S` 强迫合成 cofactor 后的容量。",
        "把剩余候选分成两类：prime cofactor forest holes 与仍未被删掉的合成 cofactor。",
        "记后者为 `R_S(P,k)`，则有精确恒等式：",
        "",
        "```text",
        "C_S(P,k)=|F(P,k)|+R_S(P,k)",
        "DeltaPhi_half(P,k)-C_S(P,k)=N(P,k)-R_S(P,k)",
        "N(P,k)=pi((k+1)P-1)-pi(kP)",
        "```",
        "",
        "因此固定 wheel 的 `DeltaPhi_half>C_S` 不是目标本身，而是更强的",
        "`N(P,k)>R_S(P,k)`。这就是当前可见的 rough-composite residual 硬点。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"row_count={finite['row_count']}",
        f"all_sqrt_residual_zero={bool_text(finite['all_sqrt_residual_zero'])}",
        f"all_fixed_capacity_decomposition_holds={bool_text(finite['all_fixed_capacity_decomposition_holds'])}",
        f"all_delta_minus_capacity_equals_prime_minus_residual={bool_text(finite['all_delta_minus_capacity_equals_prime_minus_residual'])}",
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
        f"all_sample_sqrt_residual_zero={bool_text(large['all_sample_sqrt_residual_zero'])}",
        f"large_samples_are_evidence_not_global_proof={bool_text(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        layer_summary_table(large["layer_summary"]),
        "",
        "## 4. 极限含义",
        "",
        "当 wheel primes 覆盖所有 `ell<=sqrt(2P-1)` 时，每个合成 `m<2P` 都被删去，",
        "所以 `R_S(P,k)=0`，容量退化为 `C_S=|F|`。这给出精确目标等价式，",
        "但不提供新的正性来源。",
        "",
        "对任何固定 wheel，剩下的 `R_S` 是 LPF 大于 wheel 边界的 rough composite。",
        "继续加有限 wheel 只是在缩小 `R_S`；全局闭合必须证明同一行的素数数",
        "支配这些 residual，或引入真正的 signed/dispersion/平方相位结构输入。",
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
        f"fixed_wheel_residual_decomposition_closed={bool_text(payload['fixed_wheel_residual_decomposition_closed'])}",
        f"sqrt_wheel_residual_zero_closed={bool_text(payload['sqrt_wheel_residual_zero_closed'])}",
        f"fixed_wheel_residual_dominance_global_closed={bool_text(payload['fixed_wheel_residual_dominance_global_closed'])}",
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
    print("fixed_wheel_residual_decomposition_closed=true")
    print("fixed_wheel_residual_dominance_global_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
