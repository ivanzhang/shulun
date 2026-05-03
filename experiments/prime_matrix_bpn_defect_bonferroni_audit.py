#!/usr/bin/env python3
"""BPN-Defect 的 Bonferroni/Möbius 截断审计。

用法示例：
  python3 experiments/prime_matrix_bpn_defect_bonferroni_audit.py

本脚本审计一个可能的非循环出口：
若边界帽行被完全覆盖，则幸存数 S(r)=0。
而 S(r) 可写成有限 Möbius 包含排斥：

  S(r)=sum_{d|N} mu(d) A_d(r),

其中 A_d(r) 是 d 整除该行某列的列数。
奇阶截断给 S(r) 的 Bonferroni 下界。若能在边界帽统一给出正下界，
即可排除边界零行。

审计目的不是宣称证明，而是测试该出口是否有足够数值余量。
"""

from __future__ import annotations

import itertools
import json
from collections import Counter
from math import comb, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            for multiple in range(value * value, limit + 1, value):
                sieve[multiple] = False
    return [value for value, ok in enumerate(sieve) if ok]


def count_divisible_cols(p: int, row: int, modulus: int) -> int:
    """统计列 1..P-1 中满足 modulus | ((row-1)P+c) 的个数。"""
    residue = (-(row - 1) * p) % modulus
    if residue == 0:
        first = modulus
    else:
        first = residue
    if first > p - 1:
        return 0
    return 1 + (p - 1 - first) // modulus


def build_masks(p: int, base_primes: list[int]) -> dict[int, list[int]]:
    """预计算每个小素数的行相位覆盖列掩码。"""
    masks: dict[int, list[int]] = {}
    for prime in base_primes:
        inverse = pow(p, -1, prime)
        residues = [0] * prime
        for col in range(1, p):
            row_residue = (1 - col * inverse) % prime
            residues[row_residue] |= 1 << (col - 1)
        masks[prime] = residues
    return masks


def row_cover_mask(row: int, masks: dict[int, list[int]], full_mask: int) -> int:
    """用位掩码快速计算覆盖列。"""
    mask = 0
    for prime, residues in masks.items():
        mask |= residues[row % prime]
        if mask == full_mask:
            break
    return mask


def exact_survivor_count(p: int, base_primes: list[int], row: int) -> int:
    """直接计算幸存列数。"""
    count = 0
    for col in range(1, p):
        value = (row - 1) * p + col
        if all(value % prime for prime in base_primes):
            count += 1
    return count


def survivor_count_by_mask(
    p: int,
    row: int,
    masks: dict[int, list[int]],
    full_mask: int,
) -> int:
    """用位掩码快速计算幸存列数。"""
    return (p - 1) - row_cover_mask(row, masks, full_mask).bit_count()


def intersection_sums_by_order(p: int, base_primes: list[int], row: int) -> dict[int, int]:
    """计算每个阶数的交集总和。"""
    sums: dict[int, int] = {0: p - 1}
    for order in range(1, len(base_primes) + 1):
        total = 0
        for subset in itertools.combinations(base_primes, order):
            total += count_divisible_cols(p, row, prod(subset))
        sums[order] = total
    return sums


def bonferroni_partials(order_sums: dict[int, int]) -> dict[int, int]:
    """返回 Möbius/Bonferroni 截断部分和。"""
    partials: dict[int, int] = {}
    total = 0
    for order in range(0, max(order_sums) + 1):
        total += (-1) ** order * order_sums[order]
        partials[order] = total
    return partials


def row_audit(p: int, base_primes: list[int], row: int) -> dict:
    """审计单行。"""
    order_sums = intersection_sums_by_order(p, base_primes, row)
    partials = bonferroni_partials(order_sums)
    exact = exact_survivor_count(p, base_primes, row)
    positive_odd_bounds = [
        order for order, value in partials.items() if order % 2 == 1 and value > 0
    ]
    return {
        "row": row,
        "exact_survivors": exact,
        "odd_lower_bounds": {
            order: partials[order]
            for order in sorted(partials)
            if order % 2 == 1
        },
        "even_upper_bounds": {
            order: partials[order]
            for order in sorted(partials)
            if order % 2 == 0
        },
        "first_positive_odd_bound": None
        if not positive_odd_bounds
        else positive_odd_bounds[0],
        "intersection_sums": order_sums,
    }


def zero_rows_for_prime(p: int, base_primes: list[int]) -> list[int]:
    """用位掩码找全部零行。"""
    period = prod(base_primes)
    masks = build_masks(p, base_primes)
    full_mask = (1 << (p - 1)) - 1
    rows = []
    for row in range(1, period + 1):
        if survivor_count_by_mask(p, row, masks, full_mask) == 0:
            rows.append(row)
    return rows


def audit_prime(p: int) -> dict:
    """审计单个 P。"""
    base_primes = primes_upto(p - 1)
    zero_rows = zero_rows_for_prime(p, base_primes)
    front_rows = [row_audit(p, base_primes, row) for row in range(2, p + 1)]
    front_min = min(front_rows, key=lambda item: item["exact_survivors"])
    sample_zero_rows = zero_rows[: min(5, len(zero_rows))]
    zero_audits = [row_audit(p, base_primes, row) for row in sample_zero_rows]
    positive_front = [
        item for item in front_rows if item["first_positive_odd_bound"] is not None
    ]
    return {
        "p": p,
        "base_primes": base_primes,
        "zero_count": len(zero_rows),
        "first_zero": None if not zero_rows else zero_rows[0],
        "front_min_row": front_min,
        "front_positive_odd_bound_count": len(positive_front),
        "front_row_count": len(front_rows),
        "front_first_positive_order_hist": dict(
            sorted(
                Counter(
                    item["first_positive_odd_bound"]
                    for item in positive_front
                ).items()
            )
        ),
        "sample_zero_rows": zero_audits,
    }


def order_sums_limited(
    p: int,
    base_primes: list[int],
    row: int,
    max_order: int,
) -> dict[int, int]:
    """只计算到 max_order 的交集总和。"""
    sums: dict[int, int] = {0: p - 1}
    for order in range(1, max_order + 1):
        total = 0
        for subset in itertools.combinations(base_primes, order):
            total += count_divisible_cols(p, row, prod(subset))
        sums[order] = total
    return sums


def squarefree_products_by_order(
    base_primes: list[int],
    max_order: int,
    cutoff: int,
) -> dict[int, list[int]]:
    """生成 product<cutoff 的 squarefree 乘积，按阶数分组。"""
    products: dict[int, list[int]] = {order: [] for order in range(max_order + 1)}

    def visit(start: int, order: int, product: int) -> None:
        if order > 0:
            products[order].append(product)
        if order == max_order:
            return
        for index in range(start, len(base_primes)):
            next_product = product * base_primes[index]
            if next_product >= cutoff:
                break
            visit(index + 1, order + 1, next_product)

    visit(0, 0, 1)
    return products


def front_odd_scan(max_p: int = 199, max_order: int = 7) -> dict:
    """扫描较大 P 的边界帽奇阶 Bonferroni 下界。

    对边界帽 `row<=P`，所有数都小于 `P^2`，因此 `d>=P^2` 的交集项为 0。
    这允许只枚举 `d<P^2` 的 squarefree 乘积。
    """
    rows = []
    failures = []
    s5_failures = []
    for p in [prime for prime in primes_upto(max_p) if prime >= 13]:
        base_primes = primes_upto(p - 1)
        products = squarefree_products_by_order(base_primes, max_order, p * p)
        min_by_order = {order: None for order in range(1, max_order + 1, 2)}
        min_row_by_order = {order: None for order in range(1, max_order + 1, 2)}
        first_positive_count = 0
        min_row = None
        min_best_odd = None
        for row in range(2, p + 1):
            partial = p - 1
            best_positive_order = None
            for order in range(1, max_order + 1):
                order_sum = sum(
                    count_divisible_cols(p, row, modulus)
                    for modulus in products[order]
                )
                partial += (-1) ** order * order_sum
                if order % 2 == 1:
                    if min_by_order[order] is None or partial < min_by_order[order]:
                        min_by_order[order] = partial
                        min_row_by_order[order] = row
                    if best_positive_order is None and partial > 0:
                        best_positive_order = order
            if best_positive_order is not None:
                first_positive_count += 1
            else:
                min_row = row
            row_best = max(
                min_by_order[order]
                for order in min_by_order
                if min_by_order[order] is not None
            )
            if min_best_odd is None or row_best < min_best_odd:
                min_best_odd = row_best
        record = {
            "p": p,
            "min_by_order": min_by_order,
            "min_row_by_order": min_row_by_order,
            "front_rows_with_some_positive_odd": first_positive_count,
            "front_row_count": p - 1,
            "first_row_without_positive_odd": min_row,
            "product_counts": {
                order: len(values) for order, values in products.items() if order > 0
            },
        }
        rows.append(record)
        if first_positive_count < p - 1:
            failures.append(record)
        if 5 in min_by_order and min_by_order[5] is not None and min_by_order[5] <= 0:
            s5_failures.append(record)
    worst_rows = sorted(
        rows,
        key=lambda item: (
            item["front_rows_with_some_positive_odd"] - item["front_row_count"],
            min(value for value in item["min_by_order"].values() if value is not None),
        ),
    )[:12]
    return {
        "max_p": max_p,
        "max_order": max_order,
        "checked_prime_count": len(rows),
        "failures": failures,
        "s5_failures": s5_failures,
        "worst_rows": worst_rows,
    }


def s5_weight(omega: int) -> int:
    """五阶 Bonferroni 对具有 omega 个小素因子的数的权重。"""
    if omega == 0:
        return 1
    if omega <= 5:
        return 0
    return -comb(omega - 1, 5)


def selected_s5_omega_scan(p_values: list[int] | None = None) -> list[dict]:
    """用小素因子个数恒等式快速扫描较大 P 的 S5。

    对边界帽数 `n<P^2`，`omega=0` 等价于 `n` 为素数。
    五阶下界逐点权重为：
    - 素数：+1；
    - 含 1..5 个 `<P` 小素因子：0；
    - 含至少 6 个 `<P` 小素因子：`-binom(omega-1,5)`。
    """
    if p_values is None:
        p_values = [251, 503, 1009, 2003, 5003]
    results = []
    for p in p_values:
        omega = bytearray(p * p)
        for prime in primes_upto(p - 1):
            for multiple in range(prime, p * p, prime):
                omega[multiple] += 1
        min_s5 = None
        min_row = None
        min_prime_like = None
        min_penalty = None
        failures = []
        for row in range(2, p + 1):
            row_s5 = 0
            prime_like = 0
            penalty = 0
            for value in range((row - 1) * p + 1, row * p):
                weight = s5_weight(omega[value])
                row_s5 += weight
                if omega[value] == 0:
                    prime_like += 1
                elif weight < 0:
                    penalty -= weight
            if min_s5 is None or row_s5 < min_s5:
                min_s5 = row_s5
                min_row = row
                min_prime_like = prime_like
                min_penalty = penalty
            if row_s5 <= 0 and len(failures) < 5:
                failures.append(
                    {
                        "row": row,
                        "s5": row_s5,
                        "prime_like": prime_like,
                        "penalty": penalty,
                    }
                )
        results.append(
            {
                "p": p,
                "min_s5": min_s5,
                "min_row": min_row,
                "prime_like_at_min": min_prime_like,
                "high_omega_penalty_at_min": min_penalty,
                "failures": failures,
            }
        )
    return results


def run_audit() -> dict:
    """运行审计。"""
    results = [audit_prime(p) for p in (13, 17, 19, 23)]
    odd_scan = front_odd_scan()
    omega_scan = selected_s5_omega_scan()
    return {
        "certificate_type": "prime_matrix_bpn_defect_bonferroni_audit",
        "status": "fifth_bonferroni_reduced_to_prime_minus_high_omega_penalty",
        "results": results,
        "front_odd_scan": odd_scan,
        "selected_s5_omega_scan": omega_scan,
        "structural_conclusion": (
            "Bonferroni/Möbius 截断给出了可审查的边界势函数候选，"
            "低阶奇截断在小样本边界帽上给出正下界；扩展扫描显示三阶会失败，"
            "但五阶截断在 P<=199 的边界帽未发现失败，且选点扫描到 P=5003 仍为正。"
            "五阶下界有精确解释：素数数目减去至少六个小素因子的高重惩罚。"
            "因此最新硬点是证明每个边界行的素数数目严格压过高重小因子惩罚。"
        ),
        "next_obligations": [
            "严格证明每个边界行中 prime_like_count > high_omega_penalty。",
            "将高重惩罚分解为含至少 6 个小素因子的整数计数，并用短区间多重因子上界控制。",
            "充分利用边界事实 n<P^2，含至少 6 个小素因子者必须含很小的核心乘积。",
            "若所有低阶奇截断均失败，证明负余量集中到低模端点缺陷或 Tail-anchor 缺陷。",
            "继续保留 BPN-MCR / BPN-Phi / BPN-Defect 三接口，不宣称闭合。",
        ],
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# BPN-Defect 的 Bonferroni 截断审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 1. 截断公式",
        "",
        "令 `N=prod_{ell<P}ell`，第 `r` 行幸存列数为",
        "",
        "\\[",
        "S(r)=\\#\\{1\\le c<P:((r-1)P+c,N)=1\\}.",
        "\\]",
        "",
        "对 `d|N` 定义",
        "",
        "\\[",
        "A_d(r)=\\#\\{1\\le c<P:d\\mid (r-1)P+c\\}.",
        "\\]",
        "",
        "则",
        "",
        "\\[",
        "S(r)=\\sum_{d|N}\\mu(d)A_d(r).",
        "\\]",
        "",
        "奇阶截断 `S_1,S_3,S_5,...` 是 `S(r)` 的 Bonferroni 下界。若某个奇阶截断在所有边界行 `2<=r<=P` 上统一为正，就能证明 `BPN(P)`。",
        "",
        "## 2. 审计总表",
        "",
        "| P | zero count | first zero | front min row | front min exact S | front rows with positive odd bound | first positive order hist |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in audit["results"]:
        front = item["front_min_row"]
        lines.append(
            "| {p} | {zc} | {fz} | {row} | {exact} | {pos}/{total} | `{hist}` |".format(
                p=item["p"],
                zc=item["zero_count"],
                fz=item["first_zero"],
                row=front["row"],
                exact=front["exact_survivors"],
                pos=item["front_positive_odd_bound_count"],
                total=item["front_row_count"],
                hist=item["front_first_positive_order_hist"],
            )
        )
    lines.extend(
        [
            "",
            "### 边界帽低阶奇截断扩展扫描",
            "",
            f"- max_p={audit['front_odd_scan']['max_p']}",
            f"- max_order={audit['front_odd_scan']['max_order']}",
            f"- checked_prime_count={audit['front_odd_scan']['checked_prime_count']}",
            f"- failures=`{audit['front_odd_scan']['failures']}`",
            f"- s5_failures=`{audit['front_odd_scan']['s5_failures']}`",
            f"- worst_rows=`{audit['front_odd_scan']['worst_rows']}`",
            "",
            "### 较大 P 的 S5 恒等式扫描",
            "",
            f"- selected_s5_omega_scan=`{audit['selected_s5_omega_scan']}`",
            "",
            "",
            "## 3. 最薄边界行画像",
            "",
        ]
    )
    for item in audit["results"]:
        front = item["front_min_row"]
        lines.append(f"### P={item['p']}")
        lines.append(f"- row={front['row']}, exact_survivors={front['exact_survivors']}")
        lines.append(f"- odd_lower_bounds=`{front['odd_lower_bounds']}`")
        lines.append(f"- even_upper_bounds=`{front['even_upper_bounds']}`")
        if item["sample_zero_rows"]:
            zero = item["sample_zero_rows"][0]
            lines.append(
                f"- first_zero row={zero['row']}, odd_lower_bounds=`{zero['odd_lower_bounds']}`"
            )
        lines.append("")
    lines.extend(
        [
            "## 4. 结论",
            "",
            "五阶 Bonferroni 截断给出一个非常窄、可证明化的硬点：",
            "",
            "\\[",
            "S_5(r)=(P-1)-I_1(r)+I_2(r)-I_3(r)+I_4(r)-I_5(r)>0\\qquad(2\\le r\\le P).",
            "\\]",
            "",
            "这里 `I_j(r)` 是 j 个根基素数覆盖列交集大小的总和。奇阶 Bonferroni 给出 `S_5(r)<=S(r)`，因此若能逐项证明上式，则直接得到 `S(r)>0`，从而闭合 `BPN(P)`。",
            "",
            "若五阶正性无法统一证明，下一步才应改写为带权筛版本：构造非负权重 `W_d`，证明",
            "",
            "\\[",
            "\\sum_{d|N}\\mu(d)W_d A_d(r)>0\\qquad (2\\le r\\le P),",
            "\\]",
            "",
            "或证明该不等式失败时，高阶交叉集中必然触发低模 CRT 缺陷、Tail-anchor 缺陷或残洞势函数下降矛盾。",
            "",
            "## 5. 五阶逐点恒等式",
            "",
            "设 `omega_P(n)` 为 `n` 的不同 `<P` 素因子个数。对单个数 `n`，五阶 Bonferroni 权重为",
            "",
            "\\[",
            "w_5(n)=\\sum_{j=0}^5(-1)^j\\binom{\\omega_P(n)}j.",
            "\\]",
            "",
            "由组合恒等式可得：",
            "",
            "\\[",
            "w_5(n)=\\begin{cases}",
            "1,&\\omega_P(n)=0,\\\\",
            "0,&1\\le \\omega_P(n)\\le5,\\\\",
            "-\\binom{\\omega_P(n)-1}{5},&\\omega_P(n)\\ge6.",
            "\\end{cases}",
            "\\]",
            "",
            "在边界帽 `n<P^2` 中，`omega_P(n)=0` 等价于 `n` 为素数。因此",
            "",
            "\\[",
            "S_5(r)=\\pi((r-1)P+1,rP-1)-\\sum_{\\substack{(r-1)P<n<rP\\\\ \\omega_P(n)\\ge6}}\\binom{\\omega_P(n)-1}{5}.",
            "\\]",
            "",
            "这把 `BPN-B5` 的真实内容压缩为：每个边界行中的素数数量，严格大于含至少六个小素因子的高重合数惩罚。该形式比抽象交集和更适合下一步引入小核心乘积、短区间多因子容量和 Tail-anchor 缺陷出口。",
            "",
            "## 6. 后续义务",
            "",
        ]
    )
    for obligation in audit["next_obligations"]:
        lines.append(f"- {obligation}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    audit = run_audit()
    prefix = DOCS / "prime-matrix-bpn-defect-bonferroni-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(
        json.dumps(
            {
                item["p"]: {
                    "front_min_row": item["front_min_row"]["row"],
                    "front_min_exact": item["front_min_row"]["exact_survivors"],
                    "positive_odd": item["front_positive_odd_bound_count"],
                    "front_total": item["front_row_count"],
                }
                for item in audit["results"]
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
