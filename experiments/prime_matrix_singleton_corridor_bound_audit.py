#!/usr/bin/env python3
"""Singleton-prime 走廊上界审计。

用法示例：
  python3 experiments/prime_matrix_singleton_corridor_bound_audit.py
  python3 experiments/prime_matrix_singleton_corridor_bound_audit.py --max-p 2000 --alpha 0.43
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

from prime_matrix_mge3_budget_audit import (
    MONOGRAPH,
    ceil_div,
    collect_hard_windows,
    primes_from_flags,
    sieve,
    smallest_prime_factor,
)
from prime_matrix_mge3_tail_envelope_audit import mertens_products
from prime_matrix_tail_spike_localization_audit import singleton_corridor_width

DEFAULT_JSON = MONOGRAPH / "prime-matrix-singleton-corridor-bound-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-singleton-corridor-bound-audit.md"


def corridor_interval(left: int, right: int, tail_value: int) -> tuple[int, int]:
    """返回 singleton 尾值 d 对应的 ab 走廊。"""
    d = tail_value
    lower_from_left = ceil_div(left, d)
    upper_from_right = right // d
    lower_from_right_next = right // (d + 1) + 1
    upper_from_left_prev = ceil_div(left, d - 1) - 1
    return max(lower_from_left, lower_from_right_next), min(upper_from_right, upper_from_left_prev)


def count_corridor_objects(
    low: int,
    high: int,
    z: int,
    tail_value: int,
    prime_flags: bytearray,
    spf: list[int],
) -> dict[str, int]:
    """统计走廊中的 z-rough 数与合法 semiprime 对。"""
    z_rough_count = 0
    semiprime_pair_count = 0
    for value in range(low, high + 1):
        if spf[value] <= z:
            continue
        z_rough_count += 1
        first = spf[value]
        cofactor = value // first
        if first > z and first <= cofactor <= tail_value and prime_flags[cofactor]:
            semiprime_pair_count += 1
    return {"z_rough_count": z_rough_count, "semiprime_pair_count": semiprime_pair_count}


def add_bucket(table: dict[str, dict[str, Any]], key: str, row: dict[str, Any]) -> None:
    """累加走廊上界账本。"""
    bucket = table.setdefault(
        key,
        {
            "corridor_count": 0,
            "width_sum": 0,
            "z_rough_count": 0,
            "semiprime_pair_count": 0,
            "vz_envelope": 0.0,
            "max_pair_width_ratio": 0.0,
            "max_pair_vz_ratio": 0.0,
        },
    )
    bucket["corridor_count"] += 1
    bucket["width_sum"] += row["width"]
    bucket["z_rough_count"] += row["z_rough_count"]
    bucket["semiprime_pair_count"] += row["semiprime_pair_count"]
    bucket["vz_envelope"] += row["vz_envelope"]
    bucket["max_pair_width_ratio"] = max(bucket["max_pair_width_ratio"], row["pair_width_ratio"])
    bucket["max_pair_vz_ratio"] = max(bucket["max_pair_vz_ratio"], row["pair_vz_ratio"])


def finalize_buckets(table: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """渲染分桶。"""
    rows = []
    for key, row in sorted(table.items()):
        envelope = row["vz_envelope"]
        rows.append(
            {
                "bucket": key,
                "corridor_count": row["corridor_count"],
                "width_sum": row["width_sum"],
                "z_rough_count": row["z_rough_count"],
                "semiprime_pair_count": row["semiprime_pair_count"],
                "vz_envelope": envelope,
                "pair_width_ratio": None
                if row["width_sum"] == 0
                else row["semiprime_pair_count"] / row["width_sum"],
                "pair_vz_ratio": None if envelope == 0 else row["semiprime_pair_count"] / envelope,
                "zrough_vz_ratio": None if envelope == 0 else row["z_rough_count"] / envelope,
                "max_pair_width_ratio": row["max_pair_width_ratio"],
                "max_pair_vz_ratio": row["max_pair_vz_ratio"],
            }
        )
    return rows


def audit_corridors(
    hard_windows: list[dict[str, Any]],
    primes: list[int],
    prime_flags: bytearray,
    spf: list[int],
) -> dict[str, Any]:
    """审计 singleton-prime corridor 的低筛上界。"""
    mertens = mertens_products(primes, max(primes))
    corridors: dict[tuple[int, int, int, int, int], dict[str, Any]] = {}
    by_z: dict[str, dict[str, Any]] = {}
    by_width: dict[str, dict[str, Any]] = {}
    by_p_band: dict[str, dict[str, Any]] = {}

    for window in hard_windows:
        p = window["p"]
        z = window["z"]
        left = window["left"]
        right = window["right"]
        max_first_anchor = int(round(right ** (1.0 / 3.0))) + 2
        for first_anchor in primes:
            if first_anchor <= z:
                continue
            if first_anchor > max_first_anchor:
                break
            max_second_anchor = int(math.isqrt(right // first_anchor))
            for second_anchor in primes:
                if second_anchor < first_anchor:
                    continue
                if second_anchor > max_second_anchor:
                    break
                pair = first_anchor * second_anchor
                tail_left = max(second_anchor, ceil_div(left, pair))
                tail_right = right // pair
                if tail_left != tail_right:
                    continue
                tail_value = tail_left
                if not prime_flags[tail_value]:
                    continue
                key = (p, window["q_row"], left, right, tail_value)
                if key not in corridors:
                    low, high = corridor_interval(left, right, tail_value)
                    width = max(0, high - low + 1)
                    counts = count_corridor_objects(low, high, z, tail_value, prime_flags, spf)
                    vz_envelope = width * mertens[z + 1]
                    pair_width_ratio = 0.0 if width == 0 else counts["semiprime_pair_count"] / width
                    pair_vz_ratio = 0.0 if vz_envelope == 0 else counts["semiprime_pair_count"] / vz_envelope
                    corridors[key] = {
                        "p": p,
                        "q": window["q"],
                        "q_row": window["q_row"],
                        "left": left,
                        "right": right,
                        "z": z,
                        "tail_value": tail_value,
                        "corridor_left": low,
                        "corridor_right": high,
                        "width": width,
                        "vz_envelope": vz_envelope,
                        "pair_width_ratio": pair_width_ratio,
                        "pair_vz_ratio": pair_vz_ratio,
                        **counts,
                    }

    for row in corridors.values():
        z_key = f"z={row['z']}"
        if row["width"] <= 1:
            width_key = "1"
        elif row["width"] <= 3:
            width_key = "2-3"
        elif row["width"] <= 6:
            width_key = "4-6"
        else:
            width_key = ">=7"
        if row["p"] < 100:
            p_key = "p<100"
        elif row["p"] < 300:
            p_key = "100<=p<300"
        else:
            p_key = "p>=300"
        add_bucket(by_z, z_key, row)
        add_bucket(by_width, width_key, row)
        add_bucket(by_p_band, p_key, row)

    rows = list(corridors.values())
    width_sum = sum(row["width"] for row in rows)
    z_rough_count = sum(row["z_rough_count"] for row in rows)
    semiprime_pair_count = sum(row["semiprime_pair_count"] for row in rows)
    vz_envelope = sum(row["vz_envelope"] for row in rows)
    width1_rows = [row for row in rows if row["width"] == 1]
    non_width1_rows = [row for row in rows if row["width"] > 1]
    width1_semiprime_pair_count = sum(row["semiprime_pair_count"] for row in width1_rows)
    width1_width_sum = sum(row["width"] for row in width1_rows)
    non_width1_semiprime_pair_count = sum(row["semiprime_pair_count"] for row in non_width1_rows)
    non_width1_z_rough_count = sum(row["z_rough_count"] for row in non_width1_rows)
    non_width1_vz_envelope = sum(row["vz_envelope"] for row in non_width1_rows)
    top_pair_width = sorted(rows, key=lambda row: (row["pair_width_ratio"], row["semiprime_pair_count"]), reverse=True)[:16]
    top_pair_vz = sorted(rows, key=lambda row: (row["pair_vz_ratio"], row["semiprime_pair_count"]), reverse=True)[:16]
    return {
        "corridor_count": len(rows),
        "width_sum": width_sum,
        "z_rough_count": z_rough_count,
        "semiprime_pair_count": semiprime_pair_count,
        "vz_envelope": vz_envelope,
        "pair_width_ratio": None if width_sum == 0 else semiprime_pair_count / width_sum,
        "zrough_width_ratio": None if width_sum == 0 else z_rough_count / width_sum,
        "pair_vz_ratio": None if vz_envelope == 0 else semiprime_pair_count / vz_envelope,
        "zrough_vz_ratio": None if vz_envelope == 0 else z_rough_count / vz_envelope,
        "width1_corridor_count": len(width1_rows),
        "width1_width_sum": width1_width_sum,
        "width1_semiprime_pair_count": width1_semiprime_pair_count,
        "width1_width_bound_slack": width1_width_sum - width1_semiprime_pair_count,
        "non_width1_semiprime_pair_count": non_width1_semiprime_pair_count,
        "non_width1_z_rough_count": non_width1_z_rough_count,
        "non_width1_vz_envelope": non_width1_vz_envelope,
        "non_width1_pair_vz_ratio": None
        if non_width1_vz_envelope == 0
        else non_width1_semiprime_pair_count / non_width1_vz_envelope,
        "non_width1_zrough_vz_ratio": None
        if non_width1_vz_envelope == 0
        else non_width1_z_rough_count / non_width1_vz_envelope,
        "hybrid_width1_plus_vz_envelope": width1_width_sum + non_width1_vz_envelope,
        "hybrid_needed_constant": None
        if (width1_width_sum + non_width1_vz_envelope) == 0
        else semiprime_pair_count / (width1_width_sum + non_width1_vz_envelope),
        "by_z": finalize_buckets(by_z),
        "by_width": finalize_buckets(by_width),
        "by_p_band": finalize_buckets(by_p_band),
        "top_pair_width": top_pair_width,
        "top_pair_vz": top_pair_vz,
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int) -> dict[str, Any]:
    """生成 singleton-prime corridor 上界审计。"""
    small_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(small_flags))
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    primes = primes_from_flags(prime_flags)
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    corridor_bound = audit_corridors(hard_windows, primes, prime_flags, spf)
    return {
        "certificate_type": "prime_matrix_singleton_corridor_bound_audit",
        "status": "singleton_corridor_bound_reduced_to_zrough_sieve_envelope",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction, "keep": keep},
        "corridor_bound": corridor_bound,
        "review_conclusion": (
            "Singleton-prime 走廊有两层无条件上界：唯一分解给出 semiprime 对数不超过走廊宽度，"
            "低筛约束进一步给出 z-rough 筛包络。样本中 semiprime 对仅占走廊总宽度约三分之一，"
            "说明可把剩余证明目标定为 z-rough Selberg 包络，饱和则触发 CRTDefect/Tail-anchor/OSPC。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    bound = audit["corridor_bound"]

    def fmt(value: float | None) -> str:
        """格式化可空浮点数。"""
        return "NA" if value is None else f"{value:.6f}"

    lines = [
        "# Singleton-prime 走廊上界审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告把 singleton-prime corridor 的上界分成两个确定层次：",
        "",
        "1. 唯一分解层：每个整数 `m=ab` 至多给出一个有序素因子对 `a<=b`。",
        "2. 低筛层：`m=ab` 必须避开所有 `ell<=z`，因此还受 `z`-rough 筛包络控制。",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        "",
        "## 2. 全局上界账本",
        "",
        f"- 唯一走廊数：`{bound['corridor_count']}`。",
        f"- 走廊宽度总和：`{bound['width_sum']}`。",
        f"- 走廊中 `z`-rough 整数数：`{bound['z_rough_count']}`。",
        f"- 合法 semiprime 对数：`{bound['semiprime_pair_count']}`。",
        f"- `z`-rough Mertens 包络：`{bound['vz_envelope']:.6f}`。",
        f"- semiprime/宽度：`{fmt(bound['pair_width_ratio'])}`。",
        f"- z-rough/宽度：`{fmt(bound['zrough_width_ratio'])}`。",
        f"- semiprime/z-rough包络：`{fmt(bound['pair_vz_ratio'])}`。",
        f"- z-rough/z-rough包络：`{fmt(bound['zrough_vz_ratio'])}`。",
        f"- 宽度1走廊数：`{bound['width1_corridor_count']}`，宽度界余量：`{bound['width1_width_bound_slack']}`。",
        f"- 宽度>=2 semiprime/Vz：`{fmt(bound['non_width1_pair_vz_ratio'])}`。",
        f"- 宽度>=2 z-rough/Vz：`{fmt(bound['non_width1_zrough_vz_ratio'])}`。",
        f"- 混合包络 `width1 + Vz(width>=2)`：`{bound['hybrid_width1_plus_vz_envelope']:.6f}`。",
        f"- 混合所需常数：`{fmt(bound['hybrid_needed_constant'])}`。",
        "",
        "## 3. 按宽度分桶",
        "",
        "| 宽度层 | 走廊数 | 宽度和 | z-rough | semiprime | Vz包络 | semi/宽度 | semi/Vz | zrough/Vz |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in bound["by_width"]:
        lines.append(
            f"| `{row['bucket']}` | {row['corridor_count']} | {row['width_sum']} | "
            f"{row['z_rough_count']} | {row['semiprime_pair_count']} | {row['vz_envelope']:.6f} | "
            f"{fmt(row['pair_width_ratio'])} | {fmt(row['pair_vz_ratio'])} | {fmt(row['zrough_vz_ratio'])} |"
        )
    lines += [
        "",
        "## 4. 按 p 区间分桶",
        "",
        "| p层 | 走廊数 | 宽度和 | z-rough | semiprime | Vz包络 | semi/宽度 | semi/Vz | zrough/Vz |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in bound["by_p_band"]:
        lines.append(
            f"| `{row['bucket']}` | {row['corridor_count']} | {row['width_sum']} | "
            f"{row['z_rough_count']} | {row['semiprime_pair_count']} | {row['vz_envelope']:.6f} | "
            f"{fmt(row['pair_width_ratio'])} | {fmt(row['pair_vz_ratio'])} | {fmt(row['zrough_vz_ratio'])} |"
        )
    lines += [
        "",
        "## 5. 最紧走廊",
        "",
        "| p | q行 | d | C_d | 宽度 | z | z-rough | semiprime | semi/宽度 | semi/Vz |",
        "| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in bound["top_pair_width"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | {row['tail_value']} | "
            f"`[{row['corridor_left']},{row['corridor_right']}]` | {row['width']} | {row['z']} | "
            f"{row['z_rough_count']} | {row['semiprime_pair_count']} | "
            f"{fmt(row['pair_width_ratio'])} | {fmt(row['pair_vz_ratio'])} |"
        )
    lines += [
        "",
        "## 6. 可证上界框架",
        "",
        "对任意 singleton-prime corridor `C_d(J)`，有确定上界",
        "",
        "\\[",
        "\\#\\{(a,b):ab\\in C_d,\\ z<a\\le b\\le d\\}",
        "\\le \\#\\{m\\in C_d:(m,P(z))=1\\}\\le |C_d|.",
        "\\]",
        "",
        "其中第一步使用唯一分解，第二步使用低筛粗剩余约束。若在一族走廊上 `z`-rough 包络被持续饱和，则这些走廊同时在所有小素模下避开 `0` 类，形成可送入 `CRTDefect/Tail-anchor/OSPC` 的有向缺陷。",
        "",
        "因此当前接口可写为：",
        "",
        "```text",
        "Singleton corridor z-rough Selberg bound",
        "or sustained z-rough saturation => CRTDefect/Tail-anchor/OSPC.",
        "```",
        "",
        "## 7. 审稿结论",
        "",
        audit["review_conclusion"],
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--tail-fraction", type=float, default=0.25)
    parser.add_argument("--keep", type=int, default=40)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_audit(args.max_p, args.alpha, args.tail_fraction, args.keep)
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
