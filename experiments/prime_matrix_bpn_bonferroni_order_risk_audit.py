#!/usr/bin/env python3
"""BPN Bonferroni 固定阶风险审计。

用法示例：
  python3 experiments/prime_matrix_bpn_bonferroni_order_risk_audit.py

结论：
- 固定五阶 `S5` 在当前数值样本中仍为正；
- 但任意固定奇阶 Bonferroni 截断都存在渐近风险，因为边界数的
  小素因子个数均值约为 `log log(P^2)`，会无界增长；
- 因此主线应从固定 `BPN-B5` 升级到可变阶 `BPN-BK` 或 Selberg/Brun 带权筛。
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def partial_exp(order: int, value: float) -> float:
    """计算 sum_{j=0}^order (-value)^j/j!。"""
    return sum(((-value) ** index) / math.factorial(index) for index in range(order + 1))


def first_positive_root(order: int) -> float:
    """求奇阶截断第一次变号位置。"""
    left = 0.0
    right = 1.0
    while partial_exp(order, right) > 0:
        right *= 2.0
    for _ in range(80):
        mid = (left + right) / 2
        if partial_exp(order, mid) > 0:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def model_rows() -> list[dict]:
    """生成固定阶风险模型表。"""
    orders = [3, 5, 7, 9, 11, 15, 21]
    rows = []
    for order in orders:
        root = first_positive_root(order)
        threshold_log_p = math.exp(root) / 2
        rows.append(
            {
                "odd_order": order,
                "first_root_lambda": root,
                "model_threshold_log_P": threshold_log_p,
                "model_threshold_log10_P": threshold_log_p / math.log(10),
            }
        )
    return rows


def sample_rows() -> list[dict]:
    """整理已跑的 S5 选点扫描。"""
    data = [
        (251, 17, 18, 1),
        (503, 28, 29, 1),
        (1009, 49, 52, 3),
        (2003, 96, 113, 17),
        (5003, 177, 272, 95),
        (10007, 236, 505, 269),
    ]
    rows = []
    for p, s5, prime_like, penalty in data:
        lamb = math.log(math.log(p * p))
        rows.append(
            {
                "p": p,
                "min_s5": s5,
                "prime_like": prime_like,
                "high_omega_penalty": penalty,
                "penalty_over_prime_like": penalty / prime_like,
                "lambda_loglog_p2": lamb,
                "s5_model_partial": partial_exp(5, lamb),
            }
        )
    return rows


def run_audit() -> dict:
    """运行审计。"""
    return {
        "certificate_type": "prime_matrix_bpn_bonferroni_order_risk_audit",
        "status": "fixed_order_bonferroni_has_asymptotic_risk",
        "sample_rows": sample_rows(),
        "model_rows": model_rows(),
        "structural_conclusion": (
            "固定五阶 S5 在样本中仍为正，但固定阶 Bonferroni 不是稳健终局。"
            "小素因子个数的自然尺度 log log(P^2) 无界增长；任意固定奇阶截断"
            "的指数多项式模型都会在足够大参数处变号。"
            "因此下一步应升级为可变阶 BK 或 Selberg/Brun 带权筛。"
        ),
        "next_obligations": [
            "将 BPN-B5 改写为 BPN-BK：K 随 log log P 缓慢增长。",
            "或构造 Selberg/Brun 非负筛权，避免固定阶截断的渐近变号。",
            "Core6-Density-or-TailAnchor 仍可作为低阶失败时的缺陷出口。",
        ],
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# BPN Bonferroni 固定阶风险审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 1. 样本扫描",
        "",
        "| P | min S5 | prime_like | penalty | penalty/prime | loglog(P^2) | S5 model partial |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in audit["sample_rows"]:
        lines.append(
            "| {p} | {s5} | {prime_like} | {penalty} | {ratio:.6f} | {lam:.6f} | {partial:.6f} |".format(
                p=row["p"],
                s5=row["min_s5"],
                prime_like=row["prime_like"],
                penalty=row["high_omega_penalty"],
                ratio=row["penalty_over_prime_like"],
                lam=row["lambda_loglog_p2"],
                partial=row["s5_model_partial"],
            )
        )
    lines.extend(
        [
            "",
            "## 2. 固定阶模型风险",
            "",
            "奇阶 Bonferroni 截断在 Poisson/独立模型下对应",
            "",
            "\\[",
            "E[S_K]\\approx e^{-\\lambda}\\sum_{j=0}^K\\frac{(-\\lambda)^j}{j!}.",
            "\\]",
            "",
            "其中 `lambda≈log log(P^2)`。任意固定奇阶 `K` 的多项式部分都会在某个有限 `lambda` 后变负；而 `log log(P^2)` 无界增长。因此固定阶 `BPN-BK` 不能作为最终无条件路线。",
            "",
            "| odd K | first root lambda | model log P threshold | model log10 P threshold |",
            "| ---: | ---: | ---: | ---: |",
        ]
    )
    for row in audit["model_rows"]:
        lines.append(
            "| {order} | {root:.6f} | {logp:.6f} | {log10p:.6f} |".format(
                order=row["odd_order"],
                root=row["first_root_lambda"],
                logp=row["model_threshold_log_P"],
                log10p=row["model_threshold_log10_P"],
            )
        )
    lines.extend(
        [
            "",
            "## 3. 路线调整",
            "",
            "固定 `S5` 是低范围强证据和缺陷定位工具，不应作为全局终局证明。主线应升级为：",
            "",
            "```text",
            "BPN-BK: 取 K≈c log log P 的奇阶 Bonferroni/Brun 截断，",
            "或 Selberg/Brun 非负权重，证明筛余正性；",
            "若局部失败，则进入 Core6/CoreK 密度或 Tail-anchor/CRTDefect 出口。",
            "```",
            "",
            "## 4. 后续义务",
            "",
        ]
    )
    for obligation in audit["next_obligations"]:
        lines.append(f"- {obligation}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    audit = run_audit()
    prefix = DOCS / "prime-matrix-bpn-bonferroni-order-risk-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(json.dumps(audit["sample_rows"][-1], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
