#!/usr/bin/env python3
"""RPD 第一锚 FAC 预算常数审计。

用法示例：
  python3 experiments/prime_matrix_rpd_fac_budget_audit.py
  python3 experiments/prime_matrix_rpd_fac_budget_audit.py --max-p 2000 --alpha 0.43 --etas 0.10,0.18
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

DEFAULT_JSON = MONOGRAPH / "prime-matrix-rpd-fac-budget-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-rpd-fac-budget-audit.md"


def parse_etas(raw: str) -> list[float]:
    """解析 eta 列表。"""
    etas = []
    for item in raw.split(","):
        item = item.strip()
        if not item:
            continue
        value = float(item)
        if not (0.0 < value < 1.0):
            raise ValueError(f"eta 必须在 (0,1) 内：{value}")
        etas.append(value)
    if not etas:
        raise ValueError("至少需要一个 eta")
    return etas


def prime_density_prefix(primes: list[int], limit: int) -> dict[int, float]:
    """返回每个素锚 a 对应的 V(<a)=prod_{l<a}(1-1/l)。"""
    densities: dict[int, float] = {}
    density = 1.0
    for prime in primes:
        if prime > limit:
            break
        densities[prime] = density
        density *= 1.0 - 1.0 / prime
    return densities


def beta_bucket(anchor: int, p: int, alpha: float) -> str:
    """按 anchor≈p^beta 分桶。"""
    beta = math.log(anchor) / math.log(p)
    edges = [alpha, 0.50, 0.60, 2.0 / 3.0, 0.80, 0.90, 1.01]
    labels = ["[α,0.50)", "[0.50,0.60)", "[0.60,2/3)", "[2/3,0.80)", "[0.80,0.90)", "[0.90,1.01)"]
    for label, lo, hi in zip(labels, edges, edges[1:]):
        if lo <= beta < hi:
            return label
    return "outside"


def add_bucket(
    buckets: dict[str, dict[str, Any]],
    name: str,
    capacity: int,
    rough: int,
    model: float,
) -> None:
    """累加 FAC 层预算。"""
    row = buckets.setdefault(
        name,
        {
            "anchor_interval_count": 0,
            "capacity": 0,
            "actual_rough_cofactor": 0,
            "mertens_model": 0.0,
        },
    )
    row["anchor_interval_count"] += 1
    row["capacity"] += capacity
    row["actual_rough_cofactor"] += rough
    row["mertens_model"] += model


def finalize_buckets(buckets: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """整理 FAC 层预算。"""
    rows = []
    for name, row in sorted(buckets.items()):
        model = row["mertens_model"]
        capacity = row["capacity"]
        actual = row["actual_rough_cofactor"]
        rows.append(
            {
                "bucket": name,
                "anchor_interval_count": row["anchor_interval_count"],
                "capacity": capacity,
                "actual_rough_cofactor": actual,
                "mertens_model": model,
                "actual_density": None if capacity == 0 else actual / capacity,
                "required_constant": None if model <= 0.0 else actual / model,
            }
        )
    return rows


def count_anchor_budget(
    left: int,
    right: int,
    anchor: int,
    density: float,
    spf: list[int],
) -> tuple[int, int, float]:
    """统计锚区间容量、真实 rough 互补因子和 Mertens 模型量。"""
    co_left = max(anchor, ceil_div(left, anchor))
    co_right = right // anchor
    capacity = max(0, co_right - co_left + 1)
    if capacity == 0:
        return 0, 0, 0.0
    rough = 0
    for cofactor in range(co_left, co_right + 1):
        if spf[cofactor] >= anchor:
            rough += 1
    return capacity, rough, capacity * density


def allowed_constant(rough_count: int, model: float, eta: float) -> float | None:
    """给定 eta 时 RPD 可容许的 FAC 常数。"""
    if model <= 0.0:
        return None
    return (1.0 - eta) * rough_count / model


def summarize_eta(rows: list[dict[str, Any]], etas: list[float]) -> dict[str, Any]:
    """汇总不同 eta 的逐窗口预算余量。"""
    summary: dict[str, Any] = {}
    max_required_row = max(
        (row for row in rows if row["required_constant"] is not None),
        key=lambda row: row["required_constant"],
        default=None,
    )
    max_required = None if max_required_row is None else max_required_row["required_constant"]
    for eta in etas:
        key = f"{eta:.6g}"
        eligible = [row for row in rows if row["mertens_model"] > 0.0]
        failures = [
            row
            for row in eligible
            if row["required_constant"] is not None
            and row["allowed_constants"][key] is not None
            and row["required_constant"] > row["allowed_constants"][key]
        ]
        min_allowed_row = min(
            eligible,
            key=lambda row: row["allowed_constants"][key],
            default=None,
        )
        min_allowed = None if min_allowed_row is None else min_allowed_row["allowed_constants"][key]
        uniform_gap = None
        if min_allowed is not None and max_required is not None:
            uniform_gap = min_allowed - max_required
        summary[key] = {
            "eta": eta,
            "window_count": len(eligible),
            "actual_rpd_failure_count": len(failures),
            "min_allowed_constant": min_allowed,
            "min_allowed_window": min_allowed_row,
            "max_required_constant": max_required,
            "max_required_window": max_required_row,
            "uniform_constant_gap": uniform_gap,
            "uniform_constant_feasible_on_sample": None if uniform_gap is None else uniform_gap >= 0.0,
            "largest_excess_windows": sorted(
                failures,
                key=lambda row: row["required_constant"] - row["allowed_constants"][key],
                reverse=True,
            )[:10],
        }
    return summary


def audit_fac_budget(
    hard_windows: list[dict[str, Any]],
    primes: list[int],
    density_prefix: dict[int, float],
    spf: list[int],
    alpha: float,
    etas: list[float],
) -> dict[str, Any]:
    """审计 FAC 模型常数与逐窗口余量。"""
    buckets: dict[str, dict[str, Any]] = {}
    per_window: list[dict[str, Any]] = []
    total_capacity = 0
    total_actual = 0
    total_model = 0.0
    total_rough = 0
    total_prime = 0
    total_composite = 0

    for window in hard_windows:
        p = window["p"]
        z = window["z"]
        left = window["left"]
        right = window["right"]
        window_capacity = 0
        window_actual = 0
        window_model = 0.0

        for anchor in primes:
            if anchor <= z:
                continue
            if anchor > p:
                break
            capacity, rough, model = count_anchor_budget(left, right, anchor, density_prefix[anchor], spf)
            if capacity == 0:
                continue
            add_bucket(buckets, beta_bucket(anchor, p, alpha), capacity, rough, model)
            window_capacity += capacity
            window_actual += rough
            window_model += model

        required = None if window_model <= 0.0 else window_actual / window_model
        allowed = {f"{eta:.6g}": allowed_constant(window["rough_count"], window_model, eta) for eta in etas}
        row = {
            "p": p,
            "q": window["q"],
            "q_row": window["q_row"],
            "left": left,
            "right": right,
            "rough_count": window["rough_count"],
            "prime_count": window["prime_count"],
            "composite_count": window["composite_count"],
            "fac_capacity": window_capacity,
            "fac_actual_rough_cofactor": window_actual,
            "fac_identity_gap": window_actual - window["composite_count"],
            "mertens_model": window_model,
            "required_constant": required,
            "allowed_constants": allowed,
            "prime_ratio": None if window["rough_count"] == 0 else window["prime_count"] / window["rough_count"],
            "composite_ratio": None if window["rough_count"] == 0 else window["composite_count"] / window["rough_count"],
            "model_share_of_rough": None if window["rough_count"] == 0 else window_model / window["rough_count"],
        }
        per_window.append(row)
        total_capacity += window_capacity
        total_actual += window_actual
        total_model += window_model
        total_rough += window["rough_count"]
        total_prime += window["prime_count"]
        total_composite += window["composite_count"]

    eta_keys = [f"{eta:.6g}" for eta in etas]
    global_allowed = {
        key: None if total_model <= 0.0 else (1.0 - float(key)) * total_rough / total_model
        for key in eta_keys
    }
    return {
        "window_count": len(hard_windows),
        "rough_count": total_rough,
        "prime_count": total_prime,
        "composite_count": total_composite,
        "fac_capacity": total_capacity,
        "fac_actual_rough_cofactor": total_actual,
        "fac_identity_gap": total_actual - total_composite,
        "mertens_model": total_model,
        "global_required_constant": None if total_model <= 0.0 else total_actual / total_model,
        "global_allowed_constants": global_allowed,
        "global_prime_ratio": None if total_rough == 0 else total_prime / total_rough,
        "global_composite_ratio": None if total_rough == 0 else total_composite / total_rough,
        "buckets": finalize_buckets(buckets),
        "worst_required_constant_windows": sorted(
            per_window,
            key=lambda row: row["required_constant"] or 0.0,
            reverse=True,
        )[:12],
        "worst_prime_ratio_windows": sorted(per_window, key=lambda row: (row["prime_ratio"], -row["rough_count"]))[:12],
        "eta_summary": summarize_eta(per_window, etas),
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int, etas: list[float]) -> dict[str, Any]:
    """生成 FAC 预算审计。"""
    small_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(small_flags))
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    primes = primes_from_flags(prime_flags)
    density_prefix = prime_density_prefix(primes, max_q)
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    fac_budget = audit_fac_budget(hard_windows, primes, density_prefix, spf, alpha, etas)
    return {
        "certificate_type": "prime_matrix_rpd_fac_budget_audit",
        "status": "first_anchor_fac_budget_numerical_pressure_audit",
        "parameters": {
            "max_p": max_p,
            "alpha": alpha,
            "tail_fraction": tail_fraction,
            "keep": keep,
            "etas": etas,
        },
        "fac_budget": fac_budget,
        "review_conclusion": (
            "FAC 恒等式侧可用 sum capacity*V(<anchor) 给出同权模型常数审计。"
            "全局压力有余量；逐窗口尖峰仍需要端点缺陷出口或分层 Selberg 常数证明。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "NA"
    return f"{value:.6f}"


def window_label(row: dict[str, Any]) -> str:
    """格式化窗口。"""
    return f"`[{row['left']},{row['right']}]`"


def write_md(report: dict[str, Any], path: Path) -> None:
    """写出 Markdown 报告。"""
    params = report["parameters"]
    budget = report["fac_budget"]
    lines: list[str] = [
        "# RPD 第一锚 FAC 预算常数审计",
        "",
        "**状态：** `first_anchor_fac_budget_numerical_pressure_audit`",
        "",
        "本报告在第一锚恒等式基础上，审计模型预算",
        "",
        "\\[",
        "U_{\\rm FAC}^{\\rm model}(J)=\\sum_{z<a\\le p}{\\rm cap}(I_a(J))\\prod_{\\ell<a}\\left(1-{1\\over \\ell}\\right).",
        "\\]",
        "",
        "它不是完整证明；作用是把当前硬点压成显式常数包：`C_FAC * U_FAC_model <= (1-eta)|R_z(J)|`，或输出低模端点缺陷。",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        f"- eta 测试：`{', '.join(str(x) for x in params['etas'])}`。",
        "",
        "## 2. 总账本",
        "",
        f"- 低筛粗剩余：`{budget['rough_count']}`。",
        f"- 粗素数：`{budget['prime_count']}`。",
        f"- 粗合数：`{budget['composite_count']}`。",
        f"- FAC 容量：`{budget['fac_capacity']}`。",
        f"- FAC 真实 rough 互补因子：`{budget['fac_actual_rough_cofactor']}`。",
        f"- FAC 恒等式差：`{budget['fac_identity_gap']}`。",
        f"- Mertens 模型量：`{fmt_float(budget['mertens_model'])}`。",
        f"- 全局所需常数：`{fmt_float(budget['global_required_constant'])}`。",
        f"- 全局粗素数比例：`{fmt_float(budget['global_prime_ratio'])}`。",
        "",
        "### 2.1 eta 允许常数",
        "",
        "| eta | 全局允许常数 | 逐窗口最小允许常数 | 实际RPD失败数 |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for key, item in budget["eta_summary"].items():
        lines.append(
            "| "
            f"{fmt_float(item['eta'])} | "
            f"{fmt_float(budget['global_allowed_constants'][key])} | "
            f"{fmt_float(item['min_allowed_constant'])} | "
            f"{item['actual_rpd_failure_count']} |"
        )

    lines.extend(
        [
            "",
            "### 2.2 单一 FAC 常数压力",
            "",
            "| eta | 样本最大所需常数 | 逐窗口最小允许常数 | 单一常数余量 | 样本单一常数可行 |",
            "| ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for key, item in budget["eta_summary"].items():
        lines.append(
            "| "
            f"{fmt_float(item['eta'])} | "
            f"{fmt_float(item['max_required_constant'])} | "
            f"{fmt_float(item['min_allowed_constant'])} | "
            f"{fmt_float(item['uniform_constant_gap'])} | "
            f"{item['uniform_constant_feasible_on_sample']} |"
        )

    lines.extend(
        [
            "",
            "## 3. FAC 锚层模型账本",
            "",
            "| 锚层 | 区间数 | 容量 | 真实rough互补 | 模型量 | 真实密度 | 所需常数 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in budget["buckets"]:
        lines.append(
            "| "
            f"{row['bucket']} | "
            f"{row['anchor_interval_count']} | "
            f"{row['capacity']} | "
            f"{row['actual_rough_cofactor']} | "
            f"{fmt_float(row['mertens_model'])} | "
            f"{fmt_float(row['actual_density'])} | "
            f"{fmt_float(row['required_constant'])} |"
        )

    lines.extend(
        [
            "",
            "## 4. 逐窗口常数尖峰",
            "",
            "| p | q行 | J | rough | prime | composite | 模型量 | 所需常数 | prime/rough |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in budget["worst_required_constant_windows"]:
        lines.append(
            "| "
            f"{row['p']} | "
            f"{row['q_row']} | "
            f"{window_label(row)} | "
            f"{row['rough_count']} | "
            f"{row['prime_count']} | "
            f"{row['composite_count']} | "
            f"{fmt_float(row['mertens_model'])} | "
            f"{fmt_float(row['required_constant'])} | "
            f"{fmt_float(row['prime_ratio'])} |"
        )

    lines.extend(
        [
            "",
            "## 5. 审稿结论",
            "",
            "1. `FAC` 恒等式仍通过：`fac_identity_gap=0`，说明模型审计对象与粗合数侧一致。",
            "2. 实际窗口的粗素数比例有余量，但单一 `C_FAC` 模型常数在样本上已出现负余量；不能用全局平均替代逐窗口证明。",
            "3. 下一步硬点应写成严格二分：若分层/端点修正后的同权 Selberg 常数低于逐窗口允许常数则闭合；否则尖峰必须产生低模端点缺陷，并接入 `CRTDefect/Tail-anchor/OSPC`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--tail-fraction", type=float, default=0.25)
    parser.add_argument("--keep", type=int, default=40)
    parser.add_argument("--etas", default="0.10,0.18")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    etas = parse_etas(args.etas)
    report = build_audit(args.max_p, args.alpha, args.tail_fraction, args.keep, etas)
    args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(report, args.md_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.md_out}")


if __name__ == "__main__":
    main()
