#!/usr/bin/env python3
"""CRT 零行解集分布审计。

用法示例：
  python3 experiments/prime_matrix_crt_zero_solution_distribution_audit.py

本脚本只研究 `<P` 根基素数同余筛层：
- 行 r 的列 c 被覆盖，当且仅当存在素数 ell<P 使
  (r-1)P+c == 0 (mod ell)；
- 零行是所有 c=1..P-1 都被覆盖的 CRT 解；
- 幸存列是全非零同余解。

目标是把“镜像零行”“边界帽”“中区粗合数密集”分层：
镜像是严格 CRT 事实；中区粗合数密集是数值层事实；
边界零行不存在仍需独立边界势函数或等价素数间隙输入。
"""

from __future__ import annotations

import json
from collections import Counter
from math import prod
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


def is_prime(value: int) -> bool:
    """朴素素性测试，用于边界幸存者核验。"""
    if value < 2:
        return False
    if value in (2, 3):
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def build_masks(p: int, base_primes: list[int]) -> dict[int, list[int]]:
    """预计算每个根基素数的行相位覆盖列掩码。"""
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
    """返回行 row 被 `<P` 根基素数覆盖的列掩码。"""
    mask = 0
    for prime, residues in masks.items():
        mask |= residues[row % prime]
        if mask == full_mask:
            break
    return mask


def survivor_cols(p: int, cover_mask: int) -> list[int]:
    """由覆盖掩码得到幸存列。"""
    return [
        col + 1 for col in range(p - 1) if ((cover_mask >> col) & 1) == 0
    ]


def least_covering_prime(p: int, base_primes: list[int], row: int, col: int) -> int | None:
    """返回覆盖指定格点的最小根基素数；若未覆盖则返回 None。"""
    value = (row - 1) * p + col
    for prime in base_primes:
        if value % prime == 0:
            return prime
    return None


def row_profile(
    p: int,
    base_primes: list[int],
    row: int,
    masks: dict[int, list[int]],
) -> dict:
    """生成一行的短画像。"""
    full_mask = (1 << (p - 1)) - 1
    cover_mask = row_cover_mask(row, masks, full_mask)
    survivors = survivor_cols(p, cover_mask)
    survivor_values = [(row - 1) * p + col for col in survivors]
    return {
        "row": row,
        "survivor_count": len(survivors),
        "survivor_cols": survivors,
        "survivor_values": survivor_values,
        "all_boundary_survivors_prime": all(is_prime(value) for value in survivor_values)
        if row <= p
        else None,
    }


def zero_certificate(
    p: int,
    base_primes: list[int],
    row: int,
) -> dict:
    """用每列最小覆盖素数表示一个零行证书。"""
    labels: list[int] = []
    assignments = []
    for col in range(1, p):
        label = least_covering_prime(p, base_primes, row, col)
        if label is None:
            raise ValueError(f"row {row} is not a zero row at col {col}")
        labels.append(label)
        assignments.append({"col": col, "least_label": label})
    return {
        "row": row,
        "least_label_hist": dict(sorted(Counter(labels).items())),
        "distinct_label_count": len(set(labels)),
        "assignments": assignments,
    }


def cyclic_gap_stats(rows: list[int], period: int) -> dict:
    """统计零行循环间隔。"""
    if not rows:
        return {"min_gap": None, "max_gap": None, "small_gaps": []}
    gaps = []
    for left, right in zip(rows, rows[1:]):
        gaps.append(right - left)
    gaps.append(period - rows[-1] + rows[0])
    return {
        "min_gap": min(gaps),
        "max_gap": max(gaps),
        "small_gaps": sorted(gap for gap in gaps if gap <= 2 * rows[0])[:20],
    }


def scan_prime(p: int) -> dict:
    """完整扫描一个可承受的 CRT 行周期。"""
    base_primes = primes_upto(p - 1)
    period = prod(base_primes)
    masks = build_masks(p, base_primes)
    full_mask = (1 << (p - 1)) - 1
    counts = Counter()
    zero_rows: list[int] = []
    zero_deciles = [0] * 10
    survivor_decile_sums = [0] * 10
    decile_sizes = [0] * 10
    front_profiles = []
    middle_profiles = []

    middle_start = max(1, period // 2 - p)
    middle_end = min(period, period // 2 + p)

    for row in range(1, period + 1):
        cover_mask = row_cover_mask(row, masks, full_mask)
        survivor_count = (p - 1) - cover_mask.bit_count()
        counts[survivor_count] += 1
        decile = min(9, (10 * (row - 1)) // period)
        survivor_decile_sums[decile] += survivor_count
        decile_sizes[decile] += 1
        if survivor_count == 0:
            zero_rows.append(row)
            zero_deciles[decile] += 1
        if 2 <= row <= p:
            front_profiles.append(row_profile(p, base_primes, row, masks))
        if middle_start <= row <= middle_end:
            middle_profiles.append(row_profile(p, base_primes, row, masks))

    zero_set = set(zero_rows)
    mirror_zero_ok = all(period - row + 1 in zero_set for row in zero_rows)
    count_mirror_ok = True
    for row in range(1, min(period, 10000) + 1):
        left_mask = row_cover_mask(row, masks, full_mask)
        right_mask = row_cover_mask(period - row + 1, masks, full_mask)
        if left_mask.bit_count() != right_mask.bit_count():
            count_mirror_ok = False
            break

    first_zero = zero_rows[0] if zero_rows else None
    last_zero = zero_rows[-1] if zero_rows else None
    thinnest_front = min(front_profiles, key=lambda item: item["survivor_count"])
    thinnest_middle = min(middle_profiles, key=lambda item: item["survivor_count"])
    certificates = []
    for row in zero_rows[:3]:
        certificates.append(zero_certificate(p, base_primes, row))
    if first_zero is not None and period - first_zero + 1 not in zero_rows[:3]:
        certificates.append(zero_certificate(p, base_primes, period - first_zero + 1))

    return {
        "p": p,
        "period": period,
        "hist": dict(sorted(counts.items())),
        "zero_count": len(zero_rows),
        "first_zero": first_zero,
        "last_zero": last_zero,
        "first_zero_over_p": None if first_zero is None else first_zero / p,
        "edge_cap_zero_count": sum(1 for row in zero_rows if row <= p or row >= period - p + 1),
        "zero_deciles": zero_deciles,
        "avg_survivor_count_by_decile": [
            survivor_decile_sums[index] / decile_sizes[index] for index in range(10)
        ],
        "front_thinnest": thinnest_front,
        "middle_thinnest": thinnest_middle,
        "mirror_zero_ok": mirror_zero_ok,
        "sample_count_mirror_ok": count_mirror_ok,
        "gap_stats": cyclic_gap_stats(zero_rows, period),
        "zero_certificates": certificates,
    }


def run_audit() -> dict:
    """运行审计。"""
    results = [scan_prime(p) for p in (13, 17, 19, 23)]
    return {
        "certificate_type": "prime_matrix_crt_zero_solution_distribution_audit",
        "status": "crt_solution_geometry_supports_edge_cap_reduction_not_edge_proof",
        "results": results,
        "structural_conclusion": (
            "零行是列覆盖集合交的 CRT 解，镜像来自取负映射，严格成立。"
            "实验中边界帽 rows 2..P 无零行，且边界幸存者自动为素数；"
            "但中区粗合数密集不能推出边界帽非零，因为前者是数值层粗合数画像，"
            "后者是 CRT 筛层边界最小代表下界。"
        ),
        "next_obligations": [
            "将边界零行不存在表述为 CRT 覆盖证书最小代表 >=P 的下界。",
            "构造独立边界势函数 Phi_P(R)，而不是依赖中区密度单调性。",
            "若使用中区粗合数密集，必须证明其通过同一证书族压迫边界代表；当前尚未闭合。",
        ],
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# CRT 零行解集分布与边界帽审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 1. CRT 方程组",
        "",
        "固定奇素数 `P`，令 `N=prod_{ell<P} ell`。第 `r` 行第 `c` 列的数为",
        "",
        "\\[",
        "n_{r,c}=(r-1)P+c,\\qquad 1\\le c<P.",
        "\\]",
        "",
        "列 `c` 被根基素数 `ell<P` 覆盖当且仅当",
        "",
        "\\[",
        "r\\equiv 1-cP^{-1}\\pmod {ell}.",
        "\\]",
        "",
        "因此零行集合是",
        "",
        "\\[",
        "Z_P=\\bigcap_{1\\le c<P}\\bigcup_{ell<P}\\{r:r\\equiv 1-cP^{-1}\\pmod {ell}\\}.",
        "\\]",
        "",
        "幸存列集合是",
        "",
        "\\[",
        "R_P(r)=\\{1\\le c<P:(n_{r,c},N)=1\\}.",
        "\\]",
        "",
        "取负映射给出精确镜像",
        "",
        "\\[",
        "R_P(N-r+1)=\\{P-c:c\\in R_P(r)\\}.",
        "\\]",
        "",
        "所以 `r` 为零行当且仅当 `N-r+1` 为零行。",
        "",
        "## 2. 分布审计表",
        "",
        "| P | N | zero count | first zero | first/P | edge zeros | zero deciles | front thinnest | middle thinnest | mirror ok |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |",
    ]
    for item in audit["results"]:
        front = item["front_thinnest"]
        middle = item["middle_thinnest"]
        lines.append(
            "| {p} | {period} | {zc} | {fz} | {ratio:.3f} | {edge} | `{deciles}` | row {fr}, holes {fc}, vals `{fv}` | row {mr}, holes {mc} | {mirror} |".format(
                p=item["p"],
                period=item["period"],
                zc=item["zero_count"],
                fz=item["first_zero"],
                ratio=item["first_zero_over_p"],
                edge=item["edge_cap_zero_count"],
                deciles=item["zero_deciles"],
                fr=front["row"],
                fc=front["survivor_count"],
                fv=front["survivor_values"],
                mr=middle["row"],
                mc=middle["survivor_count"],
                mirror=item["mirror_zero_ok"] and item["sample_count_mirror_ok"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 可严格使用的结论",
            "",
            "- **镜像刚性：** 零行集合关于 `r -> N-r+1` 严格对称；这给出首端/尾端同时异常的两端帽约束。",
            "- **边界自动素数：** 若 `2<=r<=P` 且 `c` 幸存，则 `n_{r,c}<P^2`，没有 `<P` 素因子，所以 `n_{r,c}` 必为素数。",
            "- **边界帽等价：** 前 `P` 行无零行等价于每个 `[xP+1,xP+P-1]`, `1<=x<P`, 含素数。",
            "- **证书最小代表：** 任意零行证书给出一个 CRT 代表；边界排除等价于证明所有完整覆盖证书的最小正代表 `>=P`。",
            "",
            "## 4. 不能直接使用的跳步",
            "",
            "- 中区幸存者可能是素数或 `P`-rough 合数；它们密集不是 CRT 筛层单调势能。",
            "- 零行镜像不是短周期；它不推出零行需以 `r`、`2r` 或 `2r-1` 为复现周期。",
            "- 因此“中区两侧光滑合数密集，所以边界无零行”目前只是启发，不是证明。",
            "",
            "## 5. 下一步硬攻形式",
            "",
            "要把本路线变成边界零行不存在证明，需要补充一个独立势函数：",
            "",
            "\\[",
            "\\Phi_P(R_P(r))\\ge 1\\quad (2\\le r\\le P),\\qquad \\Phi_P(\\varnothing)=0.",
            "\\]",
            "",
            "它必须只依赖 CRT 覆盖证书、镜像两端帽、残洞迁移和低模投影，而不能把目标结论本身放入定义。可攻版本是：若某个边界行满足 `R_P(r)=empty`，则其镜像尾端也为空；两端证书的最小标签分配合并后产生固定小模投影缺陷或残洞迁移势能为负，从而矛盾。",
            "",
            "## 6. 零行证书样本",
            "",
        ]
    )
    for item in audit["results"]:
        lines.append(f"### P={item['p']}")
        for cert in item["zero_certificates"][:4]:
            lines.append(
                f"- row={cert['row']} distinct_labels={cert['distinct_label_count']} least_label_hist=`{cert['least_label_hist']}`"
            )
        lines.append(
            f"- gap_stats=`{item['gap_stats']}`; avg_survivor_count_by_decile=`{[round(x, 4) for x in item['avg_survivor_count_by_decile']]}`"
        )
        lines.append("")

    lines.extend(["## 7. 后续证明义务", ""])
    for obligation in audit["next_obligations"]:
        lines.append(f"- {obligation}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    audit = run_audit()
    prefix = DOCS / "prime-matrix-crt-zero-solution-distribution-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(
        json.dumps(
            {
                item["p"]: {
                    "zero_count": item["zero_count"],
                    "first_zero": item["first_zero"],
                    "edge_zeros": item["edge_cap_zero_count"],
                }
                for item in audit["results"]
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
