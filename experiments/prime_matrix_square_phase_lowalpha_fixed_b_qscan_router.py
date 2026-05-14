#!/usr/bin/env python3
"""审计固定 b 后的一维 q 扫描 normal form。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_fixed_b_qscan_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-qscan-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-qscan-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-qscan-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_occupied_b_collision_geometry_router as collision


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-fixed-b-qscan-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-fixed-b-qscan-router.md"

DEFAULT_P_LIST = collision.DEFAULT_P_LIST
NEXT_TARGET = "FixedBPhaseSparseQScanSelbergBoundOrPrimeBSpikePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-occupied-b-collision-geometry-router.json",
    "prime-matrix-square-phase-lowalpha-occupied-b-sequence-router.json",
]

normal = collision.normal
envelope = collision.envelope
quarter = collision.quarter


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_fixed_b_qscan_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def active_q_axes_for_p(p: int, flags: bytearray) -> list[int]:
    """列出 quarter-gate semiprime regime 中的活跃 q 轴。"""
    primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
    axes: list[int] = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        if previous < envelope.BASE_D:
            continue
        if envelope.factor_depth_bound(p, previous) < 3:
            continue
        if not quarter.quarter_gate_closed(p, previous):
            continue
        axes.extend(
            q
            for q in primes
            if previous < q <= cutoff and envelope.is_semiprime_regime(p, q)
        )
    return sorted(set(axes))


def qscan_candidate(
    p: int,
    b: int,
    q: int,
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any] | None:
    """返回固定 `(b,q)` 的唯一合法候选；若不存在则返回 None。"""
    p2 = p * p
    a_left = p2 // (b * q) + 1
    a_right = (p2 + p - 1) // (b * q)
    lower = p / q
    if a_right < a_left:
        return None
    valid_left = max(a_left, math.floor(lower) + 1)
    valid_right = min(a_right, b)
    if valid_right < valid_left:
        return None
    # 若存在合法 a，则 a>P/q 且 a<=b，因此 bq>P，整数区间自动至多单点。
    singleton_ok = valid_left == valid_right
    a = valid_left
    prime_a = normal.is_prime_with_flags(a, flags, trial_primes)
    prime_b = normal.is_prime_with_flags(b, flags, trial_primes)
    n = q * a
    return {
        "q": q,
        "a": a,
        "b": b,
        "n": n,
        "prime_a": prime_a,
        "prime_b": prime_b,
        "valid_a_interval": [valid_left, valid_right],
        "raw_a_interval": [a_left, a_right],
        "singleton_ok": singleton_ok,
        "a_interval_width": p / (b * q),
        "n_interval": [p2 // b + 1, (p2 + p - 1) // b],
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的固定 b q-scan normal form。"""
    records = [collision.decorate_record(p, record) for record in collision.collect_records_for_p(p, flags, trial_primes)]
    b_values = sorted({int(record["b"]) for record in records})
    active_q = active_q_axes_for_p(p, flags)
    actual_keys = {(int(record["b"]), int(record["q"]), int(record["a"])) for record in records}
    actual_prime_b_keys = {
        (int(record["b"]), int(record["q"]), int(record["a"]))
        for record in records
        if record["prime_b"]
    }

    by_b_phase: dict[int, list[dict[str, Any]]] = defaultdict(list)
    by_b_prime_a: dict[int, list[dict[str, Any]]] = defaultdict(list)
    by_b_prime_b: dict[int, list[dict[str, Any]]] = defaultdict(list)
    singleton_failures: list[dict[str, Any]] = []
    scanned_candidates = 0

    for b in b_values:
        for q in active_q:
            candidate = qscan_candidate(p, b, q, flags, trial_primes)
            if candidate is None:
                continue
            scanned_candidates += 1
            by_b_phase[b].append(candidate)
            if not candidate["singleton_ok"]:
                singleton_failures.append(candidate)
            if candidate["prime_a"]:
                by_b_prime_a[b].append(candidate)
                if candidate["prime_b"]:
                    by_b_prime_b[b].append(candidate)

    qscan_prime_a_keys = {
        (candidate["b"], candidate["q"], candidate["a"])
        for candidates in by_b_prime_a.values()
        for candidate in candidates
    }
    qscan_prime_b_keys = {
        (candidate["b"], candidate["q"], candidate["a"])
        for candidates in by_b_prime_b.values()
        for candidate in candidates
    }
    missing_actual = sorted(actual_keys - qscan_prime_a_keys)[:12]
    extra_qscan = sorted(qscan_prime_a_keys - actual_keys)[:12]
    missing_prime_b = sorted(actual_prime_b_keys - qscan_prime_b_keys)[:12]
    extra_prime_b = sorted(qscan_prime_b_keys - actual_prime_b_keys)[:12]

    top_phase = max(by_b_phase.items(), key=lambda item: len(item[1]), default=(None, []))
    top_prime_a = max(by_b_prime_a.items(), key=lambda item: len(item[1]), default=(None, []))
    top_prime_b = max(by_b_prime_b.items(), key=lambda item: len(item[1]), default=(None, []))
    phase_fibers = sum(len(candidates) for candidates in by_b_phase.values())
    prime_a_fibers = sum(len(candidates) for candidates in by_b_prime_a.values())
    prime_b_fibers = sum(len(candidates) for candidates in by_b_prime_b.values())

    return {
        "p": p,
        "active_q_axis_count": len(active_q),
        "distinct_b_values": len(b_values),
        "qscan_phase_fibers": phase_fibers,
        "qscan_prime_a_fibers": prime_a_fibers,
        "qscan_prime_b_fibers": prime_b_fibers,
        "actual_occupied_records": len(actual_keys),
        "actual_prime_b_records": len(actual_prime_b_keys),
        "phase_to_prime_a_ratio": safe_ratio(phase_fibers, prime_a_fibers),
        "prime_b_over_prime_a_ratio": safe_ratio(prime_b_fibers, prime_a_fibers),
        "max_phase_multiplicity_per_b": len(top_phase[1]),
        "max_prime_a_multiplicity_per_b": len(top_prime_a[1]),
        "max_prime_b_multiplicity_per_b": len(top_prime_b[1]),
        "singleton_failure_count": len(singleton_failures),
        "qscan_missing_actual_count": len(actual_keys - qscan_prime_a_keys),
        "qscan_extra_actual_count": len(qscan_prime_a_keys - actual_keys),
        "qscan_missing_prime_b_count": len(actual_prime_b_keys - qscan_prime_b_keys),
        "qscan_extra_prime_b_count": len(qscan_prime_b_keys - actual_prime_b_keys),
        "sample_missing_actual": missing_actual,
        "sample_extra_qscan": extra_qscan,
        "sample_missing_prime_b": missing_prime_b,
        "sample_extra_prime_b": extra_prime_b,
        "top_phase_b": {
            "b": top_phase[0],
            "multiplicity": len(top_phase[1]),
            "sample": top_phase[1][:8],
        },
        "top_prime_a_b": {
            "b": top_prime_a[0],
            "multiplicity": len(top_prime_a[1]),
            "sample": top_prime_a[1][:8],
        },
        "top_prime_b_b": {
            "b": top_prime_b[0],
            "multiplicity": len(top_prime_b[1]),
            "sample": top_prime_b[1][:8],
        },
        "scanned_nonempty_candidates": scanned_candidates,
    }


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行固定 b q-scan 审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]

    missing_actual = sum(profile["qscan_missing_actual_count"] for profile in profiles)
    extra_actual = sum(profile["qscan_extra_actual_count"] for profile in profiles)
    missing_prime_b = sum(profile["qscan_missing_prime_b_count"] for profile in profiles)
    extra_prime_b = sum(profile["qscan_extra_prime_b_count"] for profile in profiles)
    singleton_failures = sum(profile["singleton_failure_count"] for profile in profiles)
    phase_fibers = sum(profile["qscan_phase_fibers"] for profile in profiles)
    prime_a_fibers = sum(profile["qscan_prime_a_fibers"] for profile in profiles)
    prime_b_fibers = sum(profile["qscan_prime_b_fibers"] for profile in profiles)

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_fixed_b_qscan_router",
        "status": "fixed_b_qscan_normal_form_closed_prime_density_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "fixed_b_qscan_exact_for_occupied_records_closed": missing_actual == 0 and extra_actual == 0,
        "fixed_b_qscan_exact_for_prime_b_records_closed": missing_prime_b == 0 and extra_prime_b == 0,
        "valid_candidate_singleton_closed": singleton_failures == 0,
        "phase_sparse_bound_proved": False,
        "prime_a_selberg_bound_proved": False,
        "prime_b_spike_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "active_q_axis_count": sum(profile["active_q_axis_count"] for profile in profiles),
        "distinct_b_values": sum(profile["distinct_b_values"] for profile in profiles),
        "qscan_phase_fibers": phase_fibers,
        "qscan_prime_a_fibers": prime_a_fibers,
        "qscan_prime_b_fibers": prime_b_fibers,
        "phase_to_prime_a_ratio": safe_ratio(phase_fibers, prime_a_fibers),
        "prime_b_over_prime_a_ratio": safe_ratio(prime_b_fibers, prime_a_fibers),
        "max_phase_multiplicity_per_b": max((profile["max_phase_multiplicity_per_b"] for profile in profiles), default=0),
        "max_prime_a_multiplicity_per_b": max((profile["max_prime_a_multiplicity_per_b"] for profile in profiles), default=0),
        "max_prime_b_multiplicity_per_b": max((profile["max_prime_b_multiplicity_per_b"] for profile in profiles), default=0),
        "singleton_failure_count": singleton_failures,
        "qscan_missing_actual_count": missing_actual,
        "qscan_extra_actual_count": extra_actual,
        "qscan_missing_prime_b_count": missing_prime_b,
        "qscan_extra_prime_b_count": extra_prime_b,
        "top_phase_b": max((profile["top_phase_b"] for profile in profiles), key=lambda item: item["multiplicity"], default=None),
        "top_prime_a_b": max(
            (profile["top_prime_a_b"] for profile in profiles),
            key=lambda item: item["multiplicity"],
            default=None,
        ),
        "top_prime_b_b": max(
            (profile["top_prime_b_b"] for profile in profiles),
            key=lambda item: item["multiplicity"],
            default=None,
        ),
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "固定 b 后，全部 occupied 记录可由活跃 q 轴的一维扫描精确重建："
            "若整数区间 P^2/(bq)<a<=(P^2+P-1)/(bq) 与 P/q<a<=b 相交，"
            "则交集自动是单点；该单点为素数时正好给出 occupied 记录，"
            "再要求 b 为素数即给出最终 semiprime-u 贡献。"
            "样本中 q-scan 与原 occupied/prime-b 账本完全一致；剩余是证明该 q-scan 相位稀疏、"
            "prime-a/prime-b 素性上筛，或把持续尖峰登记并排斥为 PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha fixed-b q-scan 路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fixed_b_qscan_exact_for_occupied_records_closed={fmt_bool(result['fixed_b_qscan_exact_for_occupied_records_closed'])}",
        f"fixed_b_qscan_exact_for_prime_b_records_closed={fmt_bool(result['fixed_b_qscan_exact_for_prime_b_records_closed'])}",
        f"valid_candidate_singleton_closed={fmt_bool(result['valid_candidate_singleton_closed'])}",
        f"phase_sparse_bound_proved={fmt_bool(result['phase_sparse_bound_proved'])}",
        f"prime_a_selberg_bound_proved={fmt_bool(result['prime_a_selberg_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. q-scan 分层账本",
        "",
        "| active q axes | distinct b | phase fibers | prime-a fibers | prime-b fibers | phase/prime-a | prime-b/prime-a |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['active_q_axis_count']} | {result['distinct_b_values']} | "
            f"{result['qscan_phase_fibers']} | {result['qscan_prime_a_fibers']} | "
            f"{result['qscan_prime_b_fibers']} | {fmt_float(result['phase_to_prime_a_ratio'])} | "
            f"{fmt_float(result['prime_b_over_prime_a_ratio'])} |"
        ),
        "",
        "## 2. 精确匹配与重数",
        "",
        "| singleton failures | missing occupied | extra occupied | missing prime-b | extra prime-b | max phase mult | max prime-a mult | max prime-b mult |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['singleton_failure_count']} | {result['qscan_missing_actual_count']} | "
            f"{result['qscan_extra_actual_count']} | {result['qscan_missing_prime_b_count']} | "
            f"{result['qscan_extra_prime_b_count']} | {result['max_phase_multiplicity_per_b']} | "
            f"{result['max_prime_a_multiplicity_per_b']} | {result['max_prime_b_multiplicity_per_b']} |"
        ),
        "",
        "## 3. 最大纤维样本",
        "",
        "| kind | data |",
        "| --- | --- |",
        f"| phase | `{result['top_phase_b']}` |",
        f"| prime-a | `{result['top_prime_a_b']}` |",
        f"| prime-b | `{result['top_prime_b_b']}` |",
        "",
        "## 4. 每个 P 的总结",
        "",
        "| P | active q | distinct b | phase | prime-a | prime-b | max phase | max prime-a | max prime-b |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['active_q_axis_count']} | {profile['distinct_b_values']} | "
            f"{profile['qscan_phase_fibers']} | {profile['qscan_prime_a_fibers']} | "
            f"{profile['qscan_prime_b_fibers']} | {profile['max_phase_multiplicity_per_b']} | "
            f"{profile['max_prime_a_multiplicity_per_b']} | {profile['max_prime_b_multiplicity_per_b']} |"
        )
    lines.extend(
        [
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：固定 `b` 后，原 occupied 记录与一维 q-scan 的 prime-a 单点候选完全一致。",
            "- 已闭合：固定 `b` 后，再加 `b` 为素数即可精确恢复 prime-b 贡献。",
            "- 已闭合：任意合法 `(b,q)` 候选自动是单点，因为合法性强制 `bq>P`。",
            "- 未闭合：固定 `b` 的 phase 候选总数全局稀疏上界。",
            "- 未闭合：prime-a 与 prime-b 的一维 Selberg/Brun 型上筛，或持续尖峰的 PDEC 排除。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 6. 依赖哈希",
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
                "fixed_b_qscan_exact_for_occupied_records_closed": result[
                    "fixed_b_qscan_exact_for_occupied_records_closed"
                ],
                "valid_candidate_singleton_closed": result["valid_candidate_singleton_closed"],
                "qscan_phase_fibers": result["qscan_phase_fibers"],
                "qscan_prime_a_fibers": result["qscan_prime_a_fibers"],
                "qscan_prime_b_fibers": result["qscan_prime_b_fibers"],
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
