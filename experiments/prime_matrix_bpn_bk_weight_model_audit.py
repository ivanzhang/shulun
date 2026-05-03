#!/usr/bin/env python3
"""BPN-BK/Selberg 路线权重模型审计。

用法示例：
  python3 experiments/prime_matrix_bpn_bk_weight_model_audit.py

本脚本不宣称证明 BPN(P)。它只做三件事：
- 把可变阶 Bonferroni 的模型阶数算清楚；
- 检查标准 Selberg/Brun 下界筛在长度 P、筛到 P 的边界行中为何不给正下界；
- 把下一步真正硬点压缩为 BK 端点缺陷或 CoreK/Tail-anchor 出口。
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def partial_exp(order: int, value: float) -> float:
    """计算 Bonferroni 模型多项式 sum_{j<=order} (-value)^j/j!。"""
    return sum(((-value) ** index) / math.factorial(index) for index in range(order + 1))


def min_odd_order_for_fraction(value: float, fraction: float) -> int:
    """找使模型下界达到 fraction*exp(-value) 的最小奇阶。"""
    target = fraction * math.exp(-value)
    for order in range(1, 401, 2):
        if partial_exp(order, value) >= target:
            return order
    raise RuntimeError("未在 401 阶内找到可用奇阶")


def min_odd_order_positive(value: float) -> int:
    """找模型下界转正的最小奇阶。"""
    for order in range(1, 401, 2):
        if partial_exp(order, value) > 0:
            return order
    raise RuntimeError("未在 401 阶内找到正奇阶")


def first_primes(limit_count: int) -> list[int]:
    """生成前 limit_count 个素数。"""
    primes: list[int] = []
    candidate = 2
    while len(primes) < limit_count:
        root = int(candidate**0.5)
        if all(candidate % prime for prime in primes if prime <= root):
            primes.append(candidate)
        candidate += 1 if candidate == 2 else 2
    return primes


def max_distinct_prime_factor_count_below_p2(p: int) -> int:
    """用 primorial 下界估算 n<P^2 可拥有的最多不同小素因子个数。"""
    product = 1
    count = 0
    for prime in first_primes(200):
        if prime >= p or product * prime >= p * p:
            break
        product *= prime
        count += 1
    return count


def sample_rows() -> list[dict]:
    """生成 BPN-BK 模型样本表。"""
    samples = [251, 503, 1009, 2003, 5003, 10007, 100_003, 1_000_003]
    rows = []
    for p in samples:
        lamb = math.log(math.log(p * p))
        positive_order = min_odd_order_positive(lamb)
        half_order = min_odd_order_for_fraction(lamb, 0.5)
        rows.append(
            {
                "p": p,
                "lambda_loglog_p2": lamb,
                "expected_sift_density": math.exp(-lamb),
                "expected_survivors_model": p * math.exp(-lamb),
                "min_odd_order_positive_model": positive_order,
                "min_odd_order_half_exp_model": half_order,
                "partial_at_half_order": partial_exp(half_order, lamb),
                "max_omega_bound_n_lt_p2": max_distinct_prime_factor_count_below_p2(p),
                "candidate_core_order": half_order + 1,
            }
        )
    return rows


def sieve_level_rows() -> list[dict]:
    """整理标准下界筛的 level 障碍。"""
    rows = []
    for p in [251, 1009, 10007, 1_000_003]:
        h = p
        z = p
        available_level = h
        positive_lower_level = z * z
        rows.append(
            {
                "p": p,
                "window_length_h": h,
                "sieve_limit_z": z,
                "available_distribution_level": available_level,
                "s_parameter_available": math.log(available_level) / math.log(z),
                "positive_lower_bound_requires_s_gt": 2.0,
                "model_required_level_gt": positive_lower_level,
                "level_gap_factor": positive_lower_level / available_level,
            }
        )
    return rows


def run_audit() -> dict:
    """运行审计。"""
    return {
        "certificate_type": "prime_matrix_bpn_bk_weight_model_audit",
        "status": "bk_selberg_route_reduced_to_endpoint_defect_or_corek_exit",
        "sample_rows": sample_rows(),
        "sieve_level_rows": sieve_level_rows(),
        "structural_conclusion": (
            "可变阶 BK 能避免固定奇阶 Bonferroni 的模型变号，但它本身仍只是"
            "高重尾部控制问题。标准 Selberg/Brun 下界筛在 H=P、z=P 时只有"
            "s<=1，而一维下界筛正性需要 s>2；因此非负筛权不能单独给出"
            "边界行非空。下一步必须证明 BK 端点 sawtooth 缺陷被 CRTDefect/"
            "Tail-anchor 排斥，或证明 CoreK 高重桶过密必触发同类缺陷。"
        ),
        "next_obligations": [
            "严写任意奇阶 K 的逐点恒等式 S_K=prime_count-CoreK_penalty。",
            "把 S_K 展开为主项加端点 sawtooth 误差，定义 BK-DEC 缺陷。",
            "证明 BK-DEC 大于预算时推出 Directed CRTDefect/Tail-anchor。",
            "证明 CoreK 高重桶过密时也推出同一缺陷出口。",
        ],
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    lines = [
        "# BPN-BK/Selberg 权重模型审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 1. 可变阶 BK 模型表",
        "",
        "| P | lambda | exp(-lambda) | model survivors | K>0 | K>=0.5e^-lambda | max omega | core order |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in audit["sample_rows"]:
        lines.append(
            "| {p} | {lam:.6f} | {density:.6f} | {survivors:.3f} | {kpos} | {khalf} | {omega} | {core} |".format(
                p=row["p"],
                lam=row["lambda_loglog_p2"],
                density=row["expected_sift_density"],
                survivors=row["expected_survivors_model"],
                kpos=row["min_odd_order_positive_model"],
                khalf=row["min_odd_order_half_exp_model"],
                omega=row["max_omega_bound_n_lt_p2"],
                core=row["candidate_core_order"],
            )
        )

    lines.extend(
        [
            "",
            "解释：`K>0` 是模型截断第一次转正的奇阶；`K>=0.5e^-lambda` 是模型下界达到真实筛余概率一半的奇阶。有限样本中该 `K` 甚至可超过 `n<P^2` 的最大不同小素因子数，这时 BK 恒等式退化为精确素数计数，不能作为独立证明。",
            "",
            "## 2. 标准 Selberg/Brun 下界障碍",
            "",
            "| P | H | z | available D | available s | required s | required D | gap factor |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in audit["sieve_level_rows"]:
        lines.append(
            "| {p} | {h} | {z} | {level} | {s:.3f} | >{req_s:.1f} | >{req_level} | {gap:.1f} |".format(
                p=row["p"],
                h=row["window_length_h"],
                z=row["sieve_limit_z"],
                level=row["available_distribution_level"],
                s=row["s_parameter_available"],
                req_s=row["positive_lower_bound_requires_s_gt"],
                req_level=row["model_required_level_gt"],
                gap=row["level_gap_factor"],
            )
        )

    lines.extend(
        [
            "",
            "在边界行中窗口长度 `H=P`，筛到 `z=P`。用平凡区间分布 `A_d=H/d+O(1)` 时，总误差限制可用 level 至多约 `D<=H=P`，所以 `s=log D/log z<=1`。一维下界筛的正性区间需要 `s>2`。因此普通 Selberg/Brun 非负筛权只能提供上界或条件预算，不能单独证明行内存在素数。",
            "",
            "## 3. 真正剩余接口",
            "",
            "对任意奇阶 `K`，逐点恒等式为",
            "",
            "\\[",
            "S_K(I)=\\sum_{n\\in I}\\sum_{j=0}^{K}(-1)^j\\binom{\\omega_P(n)}j",
            "=\\pi(I)-\\sum_{\\omega_P(n)\\ge K+1}\\binom{\\omega_P(n)-1}{K}.",
            "\\]",
            "",
            "所以 BK 路线不是绕开短区间素数问题，而是把问题改写为“素数主项是否压过 CoreK 高重尾部”。要变成证明，必须再证明以下二分：",
            "",
            "```text",
            "S_K(I)<=0",
            "=> CoreK 高重桶过密，或 BK 端点 sawtooth 缺陷过大",
            "=> Directed CRTDefect / Tail-anchor",
            "=> 与已证刚性排斥矛盾。",
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
    prefix = DOCS / "prime-matrix-bpn-bk-weight-model-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(json.dumps(audit["sample_rows"][-1], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
