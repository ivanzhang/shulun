#!/usr/bin/env python3
"""相邻素数方阵 Seam(p,q) 端点缝合审计。

用法示例：
  python3 experiments/prime_matrix_seam_endpoint_audit.py
  python3 experiments/prime_matrix_seam_endpoint_audit.py --max-p 2000
"""
from __future__ import annotations

import argparse
from bisect import bisect_left, bisect_right
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-seam-endpoint-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-seam-endpoint-audit.md"


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


def primes_upto(n: int) -> list[int]:
    """列出不超过 n 的素数。"""
    flags = sieve(n)
    return [i for i in range(2, n + 1) if flags[i]]


def row_interval(width: int, row: int) -> tuple[int, int]:
    """返回方阵第 row 行对应的闭区间。"""
    return (row - 1) * width + 1, row * width


def first_last_prime_positions(prime_list: list[int], p: int, row: int) -> tuple[int | None, int | None]:
    """返回 p 行内首末素数的行内位置。"""
    left, right = row_interval(p, row)
    start = bisect_left(prime_list, max(2, left))
    end = bisect_right(prime_list, right)
    if start == end:
        return None, None
    first = prime_list[start] - left + 1
    last = prime_list[end - 1] - left + 1
    return first, last


def contains_full_p_row(p: int, left: int, right: int) -> bool:
    """判断区间是否包含一个完整 p 行块。"""
    first_t = (left - 1 + p - 1) // p
    block_left = first_t * p + 1
    block_right = (first_t + 1) * p
    return block_left >= left and block_right <= right


def has_prime(prime_list: list[int], left: int, right: int) -> bool:
    """判断闭区间是否含素数。"""
    left = max(left, 2)
    return bisect_left(prime_list, left) < bisect_right(prime_list, right)


def row_profiles(prime_list: list[int], p: int) -> list[dict[str, int | None]]:
    """生成 p×p 旧行的端点素数剖面。"""
    rows = []
    for row in range(1, p + 1):
        first, last = first_last_prime_positions(prime_list, p, row)
        prefix_gap = None if first is None else first - 1
        suffix_gap = None if last is None else p - last
        rows.append(
            {
                "row": row,
                "first_pos": first,
                "last_pos": last,
                "prefix_gap": prefix_gap,
                "suffix_gap": suffix_gap,
            }
        )
    return rows


def analyze_pair(p: int, q: int, prime_list: list[int]) -> dict[str, Any]:
    """分析 p 到 q 的旧核心缝合端点压力。"""
    gap = q - p
    profiles = row_profiles(prime_list, p)
    old_square = p * p

    seam_rows = []
    full_rows = 0
    actual_failures = 0
    min_exact_margin: int | None = None
    worst_exact_row: dict[str, Any] | None = None

    last_full_q_row = old_square // q
    for q_row in range(1, last_full_q_row + 1):
        left, right = row_interval(q, q_row)
        if contains_full_p_row(p, left, right):
            full_rows += 1
            continue

        start_offset = left - 1
        residue = start_offset % p
        current_p_row = start_offset // p + 1
        next_p_row = current_p_row + 1
        if next_p_row > p:
            continue

        suffix_length = p - residue
        prefix_length = residue + gap
        current = profiles[current_p_row - 1]
        nxt = profiles[next_p_row - 1]
        suffix_gap = current["suffix_gap"]
        prefix_gap = nxt["prefix_gap"]
        suffix_margin = None if suffix_gap is None else suffix_length - int(suffix_gap)
        prefix_margin = None if prefix_gap is None else prefix_length - int(prefix_gap)
        exact_margin_candidates = [m for m in (suffix_margin, prefix_margin) if m is not None]
        exact_margin = max(exact_margin_candidates) if exact_margin_candidates else None
        endpoint_sum = None if suffix_gap is None or prefix_gap is None else int(suffix_gap) + int(prefix_gap)
        endpoint_certificate = endpoint_sum is not None and endpoint_sum < q
        actual_has_prime = has_prime(prime_list, left, right)
        if not actual_has_prime:
            actual_failures += 1

        row = {
            "q_row": q_row,
            "left": left,
            "right": right,
            "residue_r": residue,
            "current_p_row": current_p_row,
            "next_p_row": next_p_row,
            "suffix_length": suffix_length,
            "prefix_length": prefix_length,
            "current_last_pos": current["last_pos"],
            "next_first_pos": nxt["first_pos"],
            "suffix_gap": suffix_gap,
            "prefix_gap": prefix_gap,
            "suffix_margin": suffix_margin,
            "prefix_margin": prefix_margin,
            "exact_margin": exact_margin,
            "endpoint_gap_sum": endpoint_sum,
            "endpoint_certificate": endpoint_certificate,
            "actual_has_prime": actual_has_prime,
        }
        seam_rows.append(row)
        if exact_margin is not None and (min_exact_margin is None or exact_margin < min_exact_margin):
            min_exact_margin = exact_margin
            worst_exact_row = row

    adjacent_pairs = []
    max_endpoint_sum: int | None = None
    worst_pair: dict[str, Any] | None = None
    pair_certificate_failures = 0
    for row in range(1, p):
        current = profiles[row - 1]
        nxt = profiles[row]
        suffix_gap = current["suffix_gap"]
        prefix_gap = nxt["prefix_gap"]
        endpoint_sum = None if suffix_gap is None or prefix_gap is None else int(suffix_gap) + int(prefix_gap)
        certificate = endpoint_sum is not None and endpoint_sum < q
        if not certificate:
            pair_certificate_failures += 1
        pair = {
            "boundary_after_p_row": row,
            "suffix_gap": suffix_gap,
            "prefix_gap_next": prefix_gap,
            "endpoint_gap_sum": endpoint_sum,
            "endpoint_certificate_sum_lt_q": certificate,
            "ratio_to_q": None if endpoint_sum is None else endpoint_sum / q,
        }
        adjacent_pairs.append(pair)
        if endpoint_sum is not None and (max_endpoint_sum is None or endpoint_sum > max_endpoint_sum):
            max_endpoint_sum = endpoint_sum
            worst_pair = pair

    rows_without_prime = sum(1 for row in profiles if row["first_pos"] is None)
    max_prefix_gap = max((int(row["prefix_gap"]) for row in profiles if row["prefix_gap"] is not None), default=None)
    max_suffix_gap = max((int(row["suffix_gap"]) for row in profiles if row["suffix_gap"] is not None), default=None)

    return {
        "p": p,
        "q": q,
        "gap": gap,
        "old_square": old_square,
        "full_old_q_rows": last_full_q_row,
        "q_rows_containing_full_p_row": full_rows,
        "seam_q_rows_without_full_p_row": len(seam_rows),
        "actual_seam_failures": actual_failures,
        "old_p_rows_without_prime": rows_without_prime,
        "min_exact_seam_margin": min_exact_margin,
        "worst_exact_seam_row": worst_exact_row,
        "max_prefix_gap": max_prefix_gap,
        "max_suffix_gap": max_suffix_gap,
        "max_endpoint_gap_sum": max_endpoint_sum,
        "max_endpoint_gap_sum_ratio_to_q": None if max_endpoint_sum is None else max_endpoint_sum / q,
        "worst_endpoint_pair": worst_pair,
        "endpoint_pair_certificate_failures": pair_certificate_failures,
        "endpoint_pair_certificate_holds_globally": pair_certificate_failures == 0,
        "sample_hard_seam_rows": sorted(
            seam_rows,
            key=lambda row: (
                10**9 if row["exact_margin"] is None else int(row["exact_margin"]),
                -1 if row["endpoint_gap_sum"] is None else -int(row["endpoint_gap_sum"]),
            ),
        )[:8],
    }


def build_audit(max_p: int) -> dict[str, Any]:
    """生成 Seam 端点审计证书。"""
    primes = [p for p in primes_upto(max_p + 200) if p >= 3]
    max_q = primes[-1]
    prime_list = primes_upto(max_q * max_q)
    cases = []
    for p, q in zip(primes, primes[1:]):
        if p > max_p:
            break
        cases.append(analyze_pair(p, q, prime_list))

    worst_margin = min(
        (case for case in cases if case["min_exact_seam_margin"] is not None),
        key=lambda case: case["min_exact_seam_margin"],
        default=None,
    )
    worst_endpoint_ratio = max(
        (case for case in cases if case["max_endpoint_gap_sum_ratio_to_q"] is not None),
        key=lambda case: case["max_endpoint_gap_sum_ratio_to_q"],
        default=None,
    )
    total_actual_failures = sum(case["actual_seam_failures"] for case in cases)
    total_certificate_failures = sum(case["endpoint_pair_certificate_failures"] for case in cases)
    return {
        "certificate_type": "prime_matrix_seam_endpoint_audit",
        "status": "seam_reduced_to_endpoint_gap_barrier_not_a_proof",
        "parameters": {"max_p": max_p},
        "case_count": len(cases),
        "total_actual_seam_failures": total_actual_failures,
        "total_endpoint_pair_certificate_failures": total_certificate_failures,
        "worst_exact_margin_case": worst_margin,
        "worst_endpoint_ratio_case": worst_endpoint_ratio,
        "cases": cases,
        "formal_reduction": {
            "seam_window": "J_s(q)=[(s-1)q+1,sq], q=p+g",
            "no_full_p_row_condition": "r=((s-1)q mod p)>g, then J_s is suffix length p-r plus prefix length r+g",
            "failure_condition": "last_prime_pos(row_t)<=r and first_prime_pos(row_{t+1})>r+g",
            "gap_form": "failure implies suffix_gap(row_t)+prefix_gap(row_{t+1})>=q",
            "sufficient_barrier": "for every adjacent p-row pair, suffix_gap(row_t)+prefix_gap(row_{t+1})<q",
        },
        "review_conclusion": (
            "Seam(p,q) 的新最小硬点可压缩为相邻旧 p 行端点空段互补排斥。"
            "Row(p) 本身不足；若能证明每个相邻边界的 suffix_gap+prefix_gap_next<q，"
            "则旧核心所有 q 行缝合窗口自动含素数。该端点屏障本质上仍是局部素数间隙控制，"
            "目前只能作为更窄的待证接口，不能作为无条件证明。"
        ),
    }


def render_case_row(case: dict[str, Any]) -> str:
    """渲染表格行。"""
    margin = case["min_exact_seam_margin"]
    ratio = case["max_endpoint_gap_sum_ratio_to_q"]
    return (
        f"| {case['p']} | {case['q']} | {case['gap']} | "
        f"{case['seam_q_rows_without_full_p_row']} | {case['actual_seam_failures']} | "
        f"{margin if margin is not None else '-'} | "
        f"{case['max_endpoint_gap_sum'] if case['max_endpoint_gap_sum'] is not None else '-'} | "
        f"{ratio:.3f} |"
    )


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Seam(p,q) 端点缝合硬点审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告细化相邻素数方阵递推路线中的新最小硬点 `Seam(p,q)`。结论是：旧核心传递不应再表述为“完整旧行继承”，而应表述为相邻旧行端点空段不能互补覆盖一个新 `q` 行缝合窗口。",
        "",
        "## 1. 精确端点模型",
        "",
        "设 `q=p+g`，旧 `p` 行为",
        "",
        "\\[",
        "I_t^{(p)}=[(t-1)p+1,tp],",
        "\\]",
        "",
        "新 `q` 行为",
        "",
        "\\[",
        "J_s^{(q)}=[(s-1)q+1,sq].",
        "\\]",
        "",
        "令",
        "",
        "\\[",
        "r=(s-1)q\\pmod p.",
        "\\]",
        "",
        "若 `J_s^{(q)}` 不含完整旧 `p` 行，则 `r>g`，且该窗口正好分解为",
        "",
        "\\[",
        "J_s^{(q)}=",
        "\\{I_t\\text{ 的尾段长度 }p-r\\}",
        "\\cup",
        "\\{I_{t+1}\\text{ 的头段长度 }r+g\\}.",
        "\\]",
        "",
        "记旧行 `I_t` 的末个素数行内位置为 `L_t`，下一行 `I_{t+1}` 的首个素数位置为 `F_{t+1}`。则缝合窗口无素数当且仅当",
        "",
        "\\[",
        "L_t\\le r,\\qquad F_{t+1}>r+g.",
        "\\tag{Seam-Fail}",
        "\\]",
        "",
        "等价地，设",
        "",
        "\\[",
        "\\sigma_t=p-L_t,\\qquad \\pi_{t+1}=F_{t+1}-1,",
        "\\]",
        "",
        "则失败必然推出",
        "",
        "\\[",
        "\\sigma_t\\ge p-r,\\qquad \\pi_{t+1}\\ge r+g,",
        "\\]",
        "",
        "从而",
        "",
        "\\[",
        "\\sigma_t+\\pi_{t+1}\\ge q.",
        "\\tag{Endpoint-Barrier}",
        "\\]",
        "",
        "因此一个足够的严格接口是",
        "",
        "\\[",
        "\\boxed{\\max_{1\\le t<p}(\\sigma_t+\\pi_{t+1})<q.}",
        "\\tag{SEB}",
        "\\]",
        "",
        "若 `SEB` 成立，则所有完全位于旧核心 `[1,p^2]` 的新 `q` 行缝合窗口都含旧素数。",
        "",
        "## 2. 为什么这是新最小硬点",
        "",
        "- `Row(p)` 只给出每个旧行至少一个素数；它不控制该素数靠近左端还是右端。",
        "- 对不含完整旧行的新窗口，只要当前旧行素数都在左侧、下一旧行素数都在右侧，就可能出现缝合空窗。",
        "- `SEB` 正好排斥这种端点互补：相邻两行跨边界的终端无素数段总长不能达到 `q`。",
        "- 这比重新证明整个 `q×q` 行命题更局部，但本质仍是局部素数间隙控制，不能由 `Row(p)` 自动推出。",
        "",
        "## 3. 样本审计",
        "",
        f"- 参数：`max_p={audit['parameters']['max_p']}`。",
        f"- 相邻素数对数量：`{audit['case_count']}`。",
        f"- 实测旧核心 seam 空窗数：`{audit['total_actual_seam_failures']}`。",
        f"- `SEB` 证书失败的相邻端点对总数：`{audit['total_endpoint_pair_certificate_failures']}`。",
        "",
        "| p | q | gap | seam行数 | 实测seam空窗 | 最小精确余量 | 最大端点空段和 | 比值/ q |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for case in audit["cases"][:20]:
        lines.append(render_case_row(case))

    worst_margin = audit["worst_exact_margin_case"]
    if worst_margin:
        row = worst_margin["worst_exact_seam_row"]
        lines += [
            "",
            "最薄精确余量样本：",
            "",
            f"- `p={worst_margin['p']}, q={worst_margin['q']}, gap={worst_margin['gap']}`。",
            f"- 最小 seam 精确余量：`{worst_margin['min_exact_seam_margin']}`。",
            f"- 对应 `q` 行：`{row['q_row']}`，残基 `r={row['residue_r']}`。",
            f"- 尾段长度 `{row['suffix_length']}`，头段长度 `{row['prefix_length']}`。",
            f"- 当前行 `suffix_gap={row['suffix_gap']}`，下一行 `prefix_gap={row['prefix_gap']}`。",
        ]

    worst_ratio = audit["worst_endpoint_ratio_case"]
    if worst_ratio:
        pair = worst_ratio["worst_endpoint_pair"]
        lines += [
            "",
            "最强端点压力样本：",
            "",
            f"- `p={worst_ratio['p']}, q={worst_ratio['q']}`。",
            f"- 最大端点空段和：`{worst_ratio['max_endpoint_gap_sum']}`。",
            f"- 比值：`{worst_ratio['max_endpoint_gap_sum_ratio_to_q']:.6f}`。",
            f"- 发生在旧 `p` 行边界 `{pair['boundary_after_p_row']}` 之后。",
        ]

    lines += [
        "",
        "## 4. 递推链条的正确改写",
        "",
        "递推路线应写为",
        "",
        "```text",
        "Row(p) + SEB(p,q) + Annulus(p,q) => Row(q).",
        "```",
        "",
        "其中：",
        "",
        "- `Row(p)` 只负责旧 `p` 行内存在素数。",
        "- `SEB(p,q)` 负责旧核心内的新行边界漂移，即端点缝合。",
        "- `Annulus(p,q)` 负责 `(p^2,q^2]` 新增壳层。",
        "",
        "这比原先的 `Seam(p,q)` 更窄：`Seam` 是窗口存在性命题，`SEB` 是足以推出 `Seam` 的端点空段不等式。",
        "",
        "## 5. 诚实审稿结论",
        "",
        audit["review_conclusion"],
        "",
        "下一步最优攻坚不是继续枚举模板，而是尝试证明 `SEB(p,q)`：相邻旧行跨边界的末端无素数段与首端无素数段之和始终小于下一素数 `q`。若该式不能直接无条件证明，则需要把它进一步接入已建立的方阵/CRT 矛盾场，证明端点空段同时过长会触发斜线覆盖容量、互质刚性或 CRT 周期均衡矛盾。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_audit(args.max_p)
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
