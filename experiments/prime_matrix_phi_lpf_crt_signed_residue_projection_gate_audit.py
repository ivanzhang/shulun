#!/usr/bin/env python3
"""审计 Phi-LPF LPF tail 的 CRT signed residue projection gate。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_crt_signed_residue_projection_gate_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-crt-signed-residue-projection-gate-audit.json

本层接在 LPF tail Type-II obligation 之后。对固定 wheel S，定义同一行
signed residue measure：

  mu_S(a;P,k) =
      #{row primes n: n mod W_S = a}
    - #{S-wheel residual composites n=q*m: n mod W_S = a}.

总和恒等式为 sum_a mu_S(a)=N(P,k)-R_S(P,k)。审计问题是：
能否用固定 CRT 单位剩余类的逐类非负性来支付 LPF tail？

有限审计显示答案为否。总和在样本范围内为正，但许多单位剩余类已经出现
mu_S(a)<0；当 wheel 细化到 2310/30030 时，负格子基本跟 residual 原子一一对应。
因此 CRT 投影仍需跨剩余类/跨 character 的 signed dispersion，不能停在逐格匹配。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from math import gcd, isqrt, prod
from pathlib import Path
from typing import Any

from prime_matrix_phi_lpf_fixed_wheel_residual_rough_composite_audit import (
    finite_delta_and_prime_count,
    is_prime_from_spf,
)
from prime_matrix_phi_lpf_primorial_wheel_limit_audit import (
    DATA,
    DOCS,
    LARGE_SAMPLE_SEEDS,
    MAX_PRIME_AUDIT,
    ROOT,
    bool_text,
    cell,
    high_band_lower_k,
    next_prime_after_half,
    next_prime_at_least,
    prime_flags,
    primes_from_spf,
    reciprocal_window_for_q,
    shadow_free_cap,
    spf_table,
    upper_band_first_k,
    wheel_modulus,
)


SLUG = "prime-matrix-phi-lpf-crt-signed-residue-projection-gate"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
SIGNED_RESIDUE_LAYERS = [
    ("30-wheel", [2, 3, 5]),
    ("210-wheel", [2, 3, 5, 7]),
    ("2310-wheel", [2, 3, 5, 7, 11]),
    ("30030-wheel", [2, 3, 5, 7, 11, 13]),
]

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json",
    DOCS / "prime-matrix-phi-lpf-lpf-shell-decrement-audit.json",
    DOCS / "prime-matrix-phi-lpf-adjacent-coprime-parity-trap-audit.json",
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


def forced_by_wheel(m: int, wheel_primes: list[int]) -> bool:
    """判断 cofactor m 是否被指定 wheel 强迫为合数。"""
    return any(m > ell and m % ell == 0 for ell in wheel_primes)


def stable_for_layer(P: int, wheel_primes: list[int]) -> bool:
    """确保高素因子 q 不属于当前 wheel。"""
    return P > 2 * max(wheel_primes)


def row_prime_values_from_spf(P: int, k: int, spf: list[int]) -> list[int]:
    """直接从 SPF 表取出一行素数。"""
    values: list[int] = []
    for t in range(1, P):
        n = k * P + t
        if spf[n] == n:
            values.append(n)
    return values


def segmented_prime_values(P: int, k: int, base_primes: list[int]) -> list[int]:
    """对大样本行做分段筛，返回行内素数。"""
    start = k * P + 1
    end = (k + 1) * P - 1
    length = max(0, end - start + 1)
    if length == 0:
        return []
    composite = bytearray(length)
    limit = isqrt(end)
    for p in base_primes:
        if p > limit:
            break
        first = max(p * p, ((start + p - 1) // p) * p)
        for value in range(first, end + 1, p):
            composite[value - start] = 1
    return [start + index for index, marked in enumerate(composite) if not marked and start + index >= 2]


def residual_composite_values(
    P: int,
    k: int,
    spf: list[int],
    primes_2p: list[int],
    wheel_primes: list[int],
) -> list[int]:
    """列出指定 wheel 后仍存活的 rough-composite row values n=q*m。"""
    values: list[int] = []
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        for m in range(lower, upper + 1):
            if forced_by_wheel(m, wheel_primes):
                continue
            if is_prime_from_spf(spf, m):
                continue
            values.append(q * m)
    return values


def negative_cells(pos: Counter[int], neg: Counter[int], modulus: int) -> list[dict[str, int]]:
    """返回单位剩余类中 signed surplus 为负的格子。"""
    cells: list[dict[str, int]] = []
    for residue, residual_count in neg.items():
        if gcd(residue, modulus) != 1:
            continue
        prime_count = pos.get(residue, 0)
        surplus = prime_count - residual_count
        if surplus < 0:
            cells.append(
                {
                    "residue": residue,
                    "prime_count": prime_count,
                    "residual_count": residual_count,
                    "surplus": surplus,
                }
            )
    return sorted(cells, key=lambda item: (item["surplus"], item["residue"]))


def row_layer_profile(
    P: int,
    k: int,
    prime_values: list[int],
    residual_values: list[int],
    wheel_primes: list[int],
) -> dict[str, Any]:
    """构造某行某 wheel 的 signed residue projection 读数。"""
    modulus = wheel_modulus(wheel_primes)
    pos = Counter(value % modulus for value in prime_values)
    neg = Counter(value % modulus for value in residual_values)
    nonunit_prime_atoms = sum(count for residue, count in pos.items() if gcd(residue, modulus) != 1)
    nonunit_residual_atoms = sum(count for residue, count in neg.items() if gcd(residue, modulus) != 1)
    bad_cells = negative_cells(pos, neg, modulus)
    total_prime_count = len(prime_values)
    total_residual_count = len(residual_values)
    unit_signed_sum = sum(
        count for residue, count in pos.items() if gcd(residue, modulus) == 1
    ) - sum(count for residue, count in neg.items() if gcd(residue, modulus) == 1)
    return {
        "P": P,
        "k": k,
        "modulus": modulus,
        "stable_for_layer": stable_for_layer(P, wheel_primes),
        "prime_count": total_prime_count,
        "residual_count": total_residual_count,
        "total_surplus": total_prime_count - total_residual_count,
        "unit_signed_sum": unit_signed_sum,
        "nonunit_prime_atoms": nonunit_prime_atoms,
        "nonunit_residual_atoms": nonunit_residual_atoms,
        "active_residual": total_residual_count > 0,
        "negative_unit_cell_count": len(bad_cells),
        "has_negative_unit_cell": bool(bad_cells),
        "worst_negative_unit_cell": bad_cells[0] if bad_cells else None,
        "sample_negative_unit_cells": bad_cells[:5],
        "unit_projection_identity_holds": (
            total_prime_count - total_residual_count
            == unit_signed_sum + nonunit_prime_atoms - nonunit_residual_atoms
        ),
    }


def compact_row(row: dict[str, Any]) -> dict[str, Any]:
    """压缩行读数。"""
    return {
        "P": row["P"],
        "k": row["k"],
        "N": row["prime_count"],
        "R": row["residual_count"],
        "N_minus_R": row["total_surplus"],
        "negative_unit_cell_count": row["negative_unit_cell_count"],
        "worst_negative_unit_cell": row["worst_negative_unit_cell"],
    }


def summarize_layer(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总一个 wheel 层的 signed projection。"""
    stable_rows = [row for row in rows if row["stable_for_layer"]]
    active_rows = [row for row in stable_rows if row["active_residual"]]
    negative_rows = [row for row in stable_rows if row["has_negative_unit_cell"]]
    worst_negative_row = (
        min(
            negative_rows,
            key=lambda row: (
                row["worst_negative_unit_cell"]["surplus"],
                row["P"],
                row["k"],
            ),
        )
        if negative_rows
        else None
    )
    max_residual_row = max(active_rows, key=lambda row: row["residual_count"]) if active_rows else None
    min_total_surplus_row = min(active_rows, key=lambda row: row["total_surplus"]) if active_rows else None
    return {
        "modulus": rows[0]["modulus"] if rows else None,
        "row_count": len(rows),
        "stable_row_count": len(stable_rows),
        "stable_active_residual_row_count": len(active_rows),
        "stable_total_prime_count": sum(row["prime_count"] for row in stable_rows),
        "stable_total_residual_count": sum(row["residual_count"] for row in stable_rows),
        "stable_total_surplus": sum(row["total_surplus"] for row in stable_rows),
        "stable_rows_with_negative_unit_cell_surplus": len(negative_rows),
        "stable_negative_unit_cell_count": sum(row["negative_unit_cell_count"] for row in stable_rows),
        "stable_nonunit_prime_atoms": sum(row["nonunit_prime_atoms"] for row in stable_rows),
        "stable_nonunit_residual_atoms": sum(row["nonunit_residual_atoms"] for row in stable_rows),
        "all_stable_atoms_in_unit_classes": all(
            row["nonunit_prime_atoms"] == 0 and row["nonunit_residual_atoms"] == 0 for row in stable_rows
        ),
        "all_unit_projection_identities_hold": all(row["unit_projection_identity_holds"] for row in rows),
        "fixed_crt_classwise_dominance_holds_on_stable_rows": not negative_rows,
        "worst_negative_unit_cell_row": compact_row(worst_negative_row) if worst_negative_row else None,
        "maximum_residual_row": compact_row(max_residual_row) if max_residual_row else None,
        "minimum_total_surplus_active_row": compact_row(min_total_surplus_row) if min_total_surplus_row else None,
    }


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计；只作一致性检查，不作全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    layer_rows: dict[str, list[dict[str, Any]]] = {name: [] for name, _ in SIGNED_RESIDUE_LAYERS}
    sample_keys = {(37, 30), (97, 92), (313, 183), (463, 448), (971, 936), (1009, 1008)}
    samples: dict[str, list[dict[str, Any]]] = {name: [] for name, _ in SIGNED_RESIDUE_LAYERS}

    for P in primes:
        if P < 11:
            continue
        p_half = next_prime_after_half(P, primes_2p)
        for k in range(2, P):
            _, direct = finite_delta_and_prime_count(P, k, spf, p_half)
            prime_values = row_prime_values_from_spf(P, k, spf)
            if direct != len(prime_values):
                raise AssertionError((P, k, direct, len(prime_values)))
            for name, wheel_primes in SIGNED_RESIDUE_LAYERS:
                residual_values = residual_composite_values(P, k, spf, primes_2p, wheel_primes)
                row = row_layer_profile(P, k, prime_values, residual_values, wheel_primes)
                layer_rows[name].append(row)
                if (P, k) in sample_keys:
                    samples[name].append(compact_row(row))

    return {
        "max_prime": max_prime,
        "layers": {name: summarize_layer(rows) for name, rows in layer_rows.items()},
        "sample_rows": samples,
        "finite_evidence_not_used_as_global_proof": True,
    }


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 signed residue projection 读数。"""
    max_seed = max(seeds) + 10000
    spf = spf_table(2 * max_seed)
    flags = prime_flags(2 * max_seed)
    base_primes = primes_from_spf(spf, 2 * max_seed)
    layer_rows: dict[str, list[dict[str, Any]]] = {name: [] for name, _ in SIGNED_RESIDUE_LAYERS}

    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        primes_2p = primes_from_spf(spf, 2 * P)
        k_values = sorted({2, P // 4, P // 2, max(2, P - P // 21), P - 1})
        for k in k_values:
            prime_values = segmented_prime_values(P, k, base_primes)
            for name, wheel_primes in SIGNED_RESIDUE_LAYERS:
                residual_values = residual_composite_values(P, k, spf, primes_2p, wheel_primes)
                layer_rows[name].append(row_layer_profile(P, k, prime_values, residual_values, wheel_primes))

    return {
        "sample_seeds": seeds,
        "sample_count": sum(len(rows) for rows in layer_rows.values()) // len(SIGNED_RESIDUE_LAYERS),
        "layers": {name: summarize_layer(rows) for name, rows in layer_rows.items()},
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
            "SignedResidueProjectionIdentity",
            True,
            True,
            "固定 wheel 下 sum_a mu_S(a;P,k)=N(P,k)-R_S(P,k)。",
            "signed residue ledger",
        ),
        gate(
            "StableUnitClassSupportAfterWheel",
            True,
            True,
            "当 P>2 max(S) 时，row primes 与 S-wheel residual atoms 都落在 W_S 的单位类。",
            "stable finite exceptions removed",
        ),
        gate(
            "FixedCRTClasswiseDominance",
            False,
            False,
            "有限审计已出现 mu_S(a)<0 的单位类，逐类非负支付路线失败。",
            "global signed/character dispersion required",
        ),
        gate(
            "CRTProjectionBreaksParityBarrier",
            False,
            False,
            "固定 CRT 投影只重排 signed mass，不提供 prime-minus-tail 全局下界。",
            "SameRowReciprocalWindowTypeIIDispersionForLPFTail",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层不证明 H_P、外部引理版或内部自足版无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def layer_summary_lines(layers: dict[str, dict[str, Any]]) -> list[str]:
    """输出层摘要文本。"""
    lines: list[str] = []
    for name, item in layers.items():
        lines.extend(
            [
                f"[{name}]",
                f"modulus={item['modulus']}",
                f"stable_row_count={item['stable_row_count']}",
                f"stable_active_residual_row_count={item['stable_active_residual_row_count']}",
                f"stable_total_prime_count={item['stable_total_prime_count']}",
                f"stable_total_residual_count={item['stable_total_residual_count']}",
                f"stable_total_surplus={item['stable_total_surplus']}",
                f"stable_rows_with_negative_unit_cell_surplus={item['stable_rows_with_negative_unit_cell_surplus']}",
                f"stable_negative_unit_cell_count={item['stable_negative_unit_cell_count']}",
                f"all_stable_atoms_in_unit_classes={bool_text(item['all_stable_atoms_in_unit_classes'])}",
                f"fixed_crt_classwise_dominance_holds_on_stable_rows={bool_text(item['fixed_crt_classwise_dominance_holds_on_stable_rows'])}",
            ]
        )
    return lines


def row_table(rows: list[dict[str, Any]]) -> str:
    """输出样本行 Markdown 表。"""
    lines = [
        "| P | k | N | R | N-R | negative unit cells | worst negative cell |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['N']} | {row['R']} | "
            f"{row['N_minus_R']} | {row['negative_unit_cell_count']} | "
            f"{cell(row['worst_negative_unit_cell'])} |"
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
        "certificate_type": "prime_matrix_phi_lpf_crt_signed_residue_projection_gate_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "fixed_crt_unit_class_dominance_rejected_signed_character_dispersion_required",
        "definitions": {
            "signed_measure": "mu_S(a;P,k)=prime_count_in_residue_a - S-wheel_residual_count_in_residue_a",
            "total_identity": "sum_a mu_S(a;P,k)=N(P,k)-R_S(P,k)",
            "stable_unit_condition": "P>2 max(S), so high q and row primes are not wheel primes",
            "failed_route": "prove mu_S(a;P,k)>=0 for every unit residue a",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "external_frontier_note": (
            "Ford--Maynard prime-producing sieve requires Type-I/II input for the actual sequence; "
            "this CRT projection audit shows fixed residue-cell matching is not that input."
        ),
        "next_direct_attack_target": (
            "CharacterAveragedSameRowCRTDispersionForLPFTail "
            "OR SameRowReciprocalWindowTypeIIDispersionForLPFTail "
            "OR SquarePhaseEndpointLowerBound"
        ),
        "signed_residue_projection_identity_closed": True,
        "stable_unit_class_support_closed": True,
        "fixed_crt_classwise_dominance_proved": False,
        "character_averaged_dispersion_required": True,
        "prime_count_dominates_lpf_tail_shell_sum_proved": False,
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
        "# Prime Matrix Phi-LPF CRT signed residue projection gate 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "对固定 wheel `S` 与 `W_S=prod(S)`，定义同一行 signed residue measure：",
        "",
        "```text",
        "mu_S(a;P,k) = #{row primes n: n≡a mod W_S}",
        "              - #{S-wheel residual composites n=q*m: n≡a mod W_S}",
        "sum_a mu_S(a;P,k)=N(P,k)-R_S(P,k)",
        "```",
        "",
        "若 `P>2 max(S)`，row primes 与 residual atoms 全部落在 `W_S` 的单位剩余类。",
        "因此固定 CRT 逐类支付路线会要求所有单位类 `mu_S(a;P,k)>=0`。",
        "有限审计显示该逐类要求为假：总和为正，但许多单位剩余类为负。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        *layer_summary_lines(finite["layers"]),
        f"finite_evidence_not_used_as_global_proof={bool_text(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "各层最坏负单位格：",
        "",
    ]
    for name, item in finite["layers"].items():
        lines.extend(
            [
                f"### {name}",
                "",
                row_table([item["worst_negative_unit_cell_row"]]),
                "",
                "最大 residual 行：",
                "",
                row_table([item["maximum_residual_row"]]),
                "",
            ]
        )
    lines.extend(
        [
            "## 3. 大尺度抽样",
            "",
            "```text",
            f"sample_seeds={large['sample_seeds']}",
            f"sample_count={large['sample_count']}",
            *layer_summary_lines(large["layers"]),
            f"large_samples_are_evidence_not_global_proof={bool_text(large['large_samples_are_evidence_not_global_proof'])}",
            "```",
            "",
            "## 4. 外部定理验收边界",
            "",
            "Ford--Maynard prime-producing sieve 的价值在于说明需要目标序列自己的",
            "Type-I/Type-II 信息。本文这一层证明，固定 CRT 单位格逐类匹配不是这种信息：",
            "它只把 `N-R_S` 分解成剩余类 signed mass，而 signed mass 可在局部为负。",
            "因此下一步必须进入 character 平均、跨剩余类的同对象 dispersion，或回到",
            "square-phase endpoint lower bound。",
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
            f"signed_residue_projection_identity_closed={bool_text(payload['signed_residue_projection_identity_closed'])}",
            f"stable_unit_class_support_closed={bool_text(payload['stable_unit_class_support_closed'])}",
            f"fixed_crt_classwise_dominance_proved={bool_text(payload['fixed_crt_classwise_dominance_proved'])}",
            f"character_averaged_dispersion_required={bool_text(payload['character_averaged_dispersion_required'])}",
            f"prime_count_dominates_lpf_tail_shell_sum_proved={bool_text(payload['prime_count_dominates_lpf_tail_shell_sum_proved'])}",
            f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
            f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
            f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
            f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
            "```",
        ]
    )
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
    print("signed_residue_projection_identity_closed=true")
    print("fixed_crt_classwise_dominance_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
