#!/usr/bin/env python3
"""ASB-RHC 的 alpha 参数扫描。

用法示例：
  python3 experiments/prime_matrix_asb_rhc_alpha_sweep.py
  python3 experiments/prime_matrix_asb_rhc_alpha_sweep.py --max-p 2000 --tail-fraction 0.25
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-asb-rhc-alpha-sweep.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-asb-rhc-alpha-sweep.md"
DEFAULT_ALPHAS = (0.37, 0.40, 0.43, 0.46, 0.49)


def sieve(n: int) -> bytearray:
    """返回不超过 n 的素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    p = 2
    while p * p <= n:
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return flags


def smallest_prime_factor(n: int) -> list[int]:
    """构造最小素因子表。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    p = 2
    while p * p <= n:
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
        p += 1
    return spf


def primes_from_flags(flags: bytearray) -> list[int]:
    """从素数标记表抽取素数。"""
    return [i for i in range(2, len(flags)) if flags[i]]


def row_interval(width: int, row: int) -> tuple[int, int]:
    """返回方阵第 row 行对应的闭区间。"""
    return (row - 1) * width + 1, row * width


def contains_full_p_row(p: int, left: int, right: int) -> bool:
    """判断区间是否含完整旧 p 行。"""
    first_t = (left - 1 + p - 1) // p
    block_left = first_t * p + 1
    block_right = (first_t + 1) * p
    return block_left >= left and block_right <= right


def sampled_windows(p: int, q: int, tail_fraction: float) -> list[tuple[int, int, int, int]]:
    """列出后排 ASB 采样窗口。"""
    g = q - p
    old_square = p * p
    last_full_q_row = old_square // q
    tail_start = max(1, int((1.0 - tail_fraction) * last_full_q_row))
    windows = []
    for s in range(tail_start, last_full_q_row + 1):
        left, right = row_interval(q, s)
        if contains_full_p_row(p, left, right):
            continue
        r = (left - 1) % p
        if r <= g:
            continue
        windows.append((s, left, right, r))
    return windows


def analyze_window(left: int, right: int, z: int, prime_flags: bytearray, spf: list[int]) -> dict[str, Any]:
    """分析一个窗口中的 RHC 点覆盖率。"""
    rough_count = 0
    rough_prime_count = 0
    for n in range(left, right + 1):
        if spf[n] <= z:
            continue
        rough_count += 1
        if prime_flags[n]:
            rough_prime_count += 1
    if rough_count == 0:
        return {
            "rough_count": 0,
            "rough_prime_count": 0,
            "rough_prime_ratio": None,
            "point_coverage_ratio": None,
        }
    rough_prime_ratio = rough_prime_count / rough_count
    return {
        "rough_count": rough_count,
        "rough_prime_count": rough_prime_count,
        "rough_prime_ratio": rough_prime_ratio,
        "point_coverage_ratio": 1.0 - rough_prime_ratio,
    }


def analyze_alpha(
    alpha: float,
    prime_pairs: list[tuple[int, int]],
    tail_fraction: float,
    prime_flags: bytearray,
    spf: list[int],
) -> dict[str, Any]:
    """分析单个 alpha。"""
    total_windows = 0
    total_rough = 0
    total_rough_primes = 0
    worst_prime_ratio: dict[str, Any] | None = None
    worst_coverage_ratio: dict[str, Any] | None = None
    zero_rough_prime_windows = 0
    for p, q in prime_pairs:
        z = max(2, int(p**alpha))
        for q_row, left, right, r in sampled_windows(p, q, tail_fraction):
            total_windows += 1
            stats = analyze_window(left, right, z, prime_flags, spf)
            if stats["rough_count"] == 0:
                continue
            total_rough += stats["rough_count"]
            total_rough_primes += stats["rough_prime_count"]
            if stats["rough_prime_count"] == 0:
                zero_rough_prime_windows += 1
            row = {
                "p": p,
                "q": q,
                "z": z,
                "q_row": q_row,
                "left": left,
                "right": right,
                "r": r,
                **stats,
            }
            if worst_prime_ratio is None or stats["rough_prime_ratio"] < worst_prime_ratio["rough_prime_ratio"]:
                worst_prime_ratio = row
            if worst_coverage_ratio is None or stats["point_coverage_ratio"] > worst_coverage_ratio["point_coverage_ratio"]:
                worst_coverage_ratio = row
    global_prime_ratio = None if total_rough == 0 else total_rough_primes / total_rough
    return {
        "alpha": alpha,
        "total_windows": total_windows,
        "total_rough": total_rough,
        "total_rough_primes": total_rough_primes,
        "global_rough_prime_ratio": global_prime_ratio,
        "global_point_coverage_ratio": None if global_prime_ratio is None else 1.0 - global_prime_ratio,
        "zero_rough_prime_windows": zero_rough_prime_windows,
        "worst_prime_ratio_window": worst_prime_ratio,
        "worst_point_coverage_window": worst_coverage_ratio,
    }


def build_audit(max_p: int, alphas: list[float], tail_fraction: float) -> dict[str, Any]:
    """生成 alpha 扫描审计。"""
    prime_flags_small = sieve(max_p + 200)
    base_primes = [p for p in primes_from_flags(prime_flags_small) if p >= 3]
    prime_pairs = [(p, q) for p, q in zip(base_primes, base_primes[1:]) if p <= max_p]
    max_q = prime_pairs[-1][1]
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    alpha_results = [analyze_alpha(alpha, prime_pairs, tail_fraction, prime_flags, spf) for alpha in alphas]
    best_by_worst_ratio = max(
        alpha_results,
        key=lambda row: -1.0
        if row["worst_prime_ratio_window"] is None
        else row["worst_prime_ratio_window"]["rough_prime_ratio"],
    )
    return {
        "certificate_type": "prime_matrix_asb_rhc_alpha_sweep",
        "status": "rhc_equivalent_to_positive_rough_prime_density",
        "parameters": {"max_p": max_p, "alphas": alphas, "tail_fraction": tail_fraction},
        "case_count": len(prime_pairs),
        "alpha_results": alpha_results,
        "best_by_worst_ratio": best_by_worst_ratio,
        "review_conclusion": (
            "ASB-RHC 的点覆盖版本等价于所有采样窗口中 R_z(J) 的素数比例有统一正下界。"
            "样本支持该比例为正，但这已经是短窗口粗剩余素数下界，不能由普通覆盖容量自动推出。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    lines = [
        "# ASB-RHC 的 alpha 扫描与等价硬点",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告继续压缩 `ASB-RHC`。由于 `D_z(J)` 正好是低筛粗剩余中的合数点集，",
        "",
        "\\[",
        "|D_z(J)|=|R_z(J)|-|R_z(J)\\cap\\mathbb P|.",
        "\\]",
        "",
        "因此",
        "",
        "\\[",
        "|D_z(J)|\\le(1-\\eta)|R_z(J)|",
        "\\]",
        "",
        "等价于",
        "",
        "\\[",
        "|R_z(J)\\cap\\mathbb P|\\ge\\eta |R_z(J)|.",
        "\\tag{RPD}",
        "\\]",
        "",
        "所以当前真正硬点不是几何遮挡，也不是裸总 incidence，而是采样短窗口内低筛粗剩余的素数正比例下界 `RPD`。",
        "",
        "## 1. 参数扫描",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 相邻素数对数量：`{audit['case_count']}`。",
        "",
        "| alpha | 窗口数 | 全局粗剩余素数比 | 最坏窗口素数比 | 零粗素数窗口 |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in audit["alpha_results"]:
        worst = row["worst_prime_ratio_window"]
        worst_ratio = "-" if worst is None else f"{worst['rough_prime_ratio']:.6f}"
        global_ratio = "-" if row["global_rough_prime_ratio"] is None else f"{row['global_rough_prime_ratio']:.6f}"
        lines.append(
            f"| {row['alpha']:.2f} | {row['total_windows']} | {global_ratio} | "
            f"{worst_ratio} | {row['zero_rough_prime_windows']} |"
        )
    best = audit["best_by_worst_ratio"]
    worst = best["worst_prime_ratio_window"]
    lines += [
        "",
        "## 2. 当前最优 alpha",
        "",
        f"- 按最坏窗口素数比，样本最优 `alpha={best['alpha']:.2f}`。",
    ]
    if worst:
        lines += [
            f"- 最坏窗口：`p={worst['p']}, q={worst['q']}, z={worst['z']}`。",
            f"- 区间 `[{worst['left']},{worst['right']}]`，`q_row={worst['q_row']}`，残基 `r={worst['r']}`。",
            f"- `rough_count={worst['rough_count']}`，`rough_prime_count={worst['rough_prime_count']}`。",
            f"- 最坏粗剩余素数比 `{worst['rough_prime_ratio']:.6f}`。",
            "",
        ]
    lines += [
        "## 3. 审稿解释",
        "",
        "这一步暴露了 `ASB-RHC` 的真实难度：它不是一般的高素覆盖容量上界，而是要求每个采样短窗口中的低筛粗剩余含有固定比例素数。若能证明 `RPD`，则 `ASB-Fail` 立即矛盾；若不能，递推路线仍停在短窗口素数下界障碍。",
        "",
        "和全局 `SEB` 相比，`RPD` 仍更精确，因为它只作用在 ASB 采样窗口和低筛粗剩余上；但它仍需要解析数论输入或强 CRT 漂移异常排斥，不能由当前行存在命题自动推出。",
        "",
        "## 4. 下一步最小目标",
        "",
        "把 `RPD` 写成二分出口：",
        "",
        "```text",
        "要么每个 ASB 采样窗口满足 |R_z(J)∩P| >= eta |R_z(J)|;",
        "要么存在某个窗口的低筛粗剩余显著避开素数，",
        "     这触发 CRTDefect / Tail-anchor / OSPC 型异常出口。",
        "```",
        "",
        audit["review_conclusion"],
        "",
    ]
    return "\n".join(lines)


def parse_alphas(raw: str) -> list[float]:
    """解析 alpha 列表。"""
    return [float(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--alphas", type=str, default=",".join(str(x) for x in DEFAULT_ALPHAS))
    parser.add_argument("--tail-fraction", type=float, default=0.25)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_audit(args.max_p, parse_alphas(args.alphas), args.tail_fraction)
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
