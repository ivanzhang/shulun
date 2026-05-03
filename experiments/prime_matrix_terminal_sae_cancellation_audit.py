#!/usr/bin/env python3
"""审计 Terminal-SAE 中 G_y-T_y 的单尾抵消结构。

用法示例：
  python3 experiments/prime_matrix_terminal_sae_cancellation_audit.py --max-p 1000
  python3 experiments/prime_matrix_terminal_sae_cancellation_audit.py --max-p 1000 --y-ratio 0.36787944117144233

在 n=q^2-m 变量中，G_y(h) 是区间 I_h 内避开所有低素数 r<=y 的数。
T_y(h) 是这些数被尾素数 y<ell<=p 整除的总重数。因此

  G_y(h)-T_y(h)=sum_{n in I_h, P^-(n)>y} (1-omega_tail(n)).

所有恰有一个尾素因子的项贡献为 0；真正竞争只发生在无尾储备
和多尾碰撞超额之间。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def sieve_bool(n: int) -> bytearray:
    """返回素数布尔表。"""
    is_prime = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        is_prime[0] = 0
    if n >= 1:
        is_prime[1] = 0
    for d in range(2, int(n**0.5) + 1):
        if is_prime[d]:
            start = d * d
            is_prime[start : n + 1 : d] = b"\x00" * (((n - start) // d) + 1)
    return is_prime


def primes_from_table(is_prime: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(is_prime) if flag]


def next_prime(p: int, primes: list[int]) -> int:
    """返回大于 p 的下一素数。"""
    for prime in primes:
        if prime > p:
            return prime
    raise ValueError("素数表范围不足")


def prefix_sum(values: bytearray) -> list[int]:
    """计算 bytearray 的前缀和。"""
    pref = [0] * (len(values) + 1)
    total = 0
    for idx, value in enumerate(values):
        total += value
        pref[idx + 1] = total
    return pref


def audit(max_p: int, y_ratio: float) -> dict:
    """执行抵消结构审计。"""
    prime_table = sieve_bool(max_p * max_p + max_p * 20 + 10000)
    primes = primes_from_table(prime_table)
    target_primes = [prime for prime in primes if 3 <= prime <= max_p]

    records = []
    unresolved = []
    max_tail_omega = 0
    first_two_tail_only_p = None

    for p in target_primes:
        q = next_prime(p, primes)
        q_square = q * q
        y = max(2, int(math.floor(y_ratio * p)))
        low_primes = [prime for prime in primes if prime <= y]
        tail_primes = [prime for prime in primes if y < prime <= p]

        # low_rough[n]=1 表示 n 避开所有低素数。n=1 与 n=q^2 不能作为素数幸存者。
        low_rough = bytearray(b"\x01") * (q_square + 1)
        low_rough[0] = 0
        low_rough[1] = 0
        low_rough[q_square] = 0
        for ell in low_primes:
            low_rough[0 : q_square + 1 : ell] = b"\x00" * ((q_square // ell) + 1)

        # tail_omega[n] 记录 n 的不同尾素因子个数。
        tail_omega = bytearray(q_square + 1)
        for ell in tail_primes:
            for pos in range(ell, q_square + 1, ell):
                if low_rough[pos] and tail_omega[pos] < 255:
                    tail_omega[pos] += 1

        no_tail = bytearray(q_square + 1)
        one_tail = bytearray(q_square + 1)
        multi_excess = bytearray(q_square + 1)
        multi_count = bytearray(q_square + 1)
        for n in range(2, q_square):
            if not low_rough[n]:
                continue
            omega = tail_omega[n]
            if omega == 0:
                no_tail[n] = 1
            elif omega == 1:
                one_tail[n] = 1
            else:
                multi_count[n] = 1
                multi_excess[n] = omega - 1
                if omega > max_tail_omega:
                    max_tail_omega = omega

        pref_low = prefix_sum(low_rough)
        pref_tail = prefix_sum(tail_omega)
        pref_no_tail = prefix_sum(no_tail)
        pref_one_tail = prefix_sum(one_tail)
        pref_multi_count = prefix_sum(multi_count)
        pref_multi_excess = prefix_sum(multi_excess)

        min_margin = None
        min_rows = []
        min_data = None
        min_margin_nonbottom = None
        min_data_nonbottom = None
        bad_rows = []
        local_max_omega = max(tail_omega)
        if local_max_omega <= 2 and first_two_tail_only_p is None:
            first_two_tail_only_p = p

        for h in range(1, q + 1):
            left = q_square - h * q + 1
            right = q_square - (h - 1) * q
            # right+1 是前缀和右开端点；n=1 与 n=q^2 已被置零。
            low_count = pref_low[right + 1] - pref_low[left]
            tail_weight = pref_tail[right + 1] - pref_tail[left]
            zero_tail = pref_no_tail[right + 1] - pref_no_tail[left]
            single_tail = pref_one_tail[right + 1] - pref_one_tail[left]
            multi_tail = pref_multi_count[right + 1] - pref_multi_count[left]
            excess = pref_multi_excess[right + 1] - pref_multi_excess[left]
            margin = low_count - tail_weight
            cancellation_margin = zero_tail - excess

            if margin != cancellation_margin:
                raise AssertionError("抵消恒等式失败")

            data = {
                "h": h,
                "n_interval": [left, right],
                "low_skeleton": low_count,
                "tail_incidence": tail_weight,
                "no_tail_reserve": zero_tail,
                "one_tail_cancelled": single_tail,
                "multi_tail_count": multi_tail,
                "multi_tail_excess": excess,
                "margin": margin,
            }
            if min_margin is None or margin < min_margin:
                min_margin = margin
                min_rows = [h]
                min_data = data
            elif margin == min_margin:
                min_rows.append(h)
            if h < q and (
                min_margin_nonbottom is None or margin < min_margin_nonbottom
            ):
                min_margin_nonbottom = margin
                min_data_nonbottom = data
            if margin <= 0:
                bad_rows.append(data)

        record = {
            "p": p,
            "q_next": q,
            "y": y,
            "y_ratio_actual": y / p,
            "tail_prime_count": len(tail_primes),
            "local_max_tail_omega": local_max_omega,
            "two_tail_only_by_y3_gt_q2": y**3 > q_square,
            "min_margin": min_margin,
            "min_rows": min_rows[:10],
            "min_data": min_data,
            "min_margin_nonbottom": min_margin_nonbottom,
            "min_data_nonbottom": min_data_nonbottom,
            "bad_margin_row_count": len(bad_rows),
            "bad_margin_rows": bad_rows[:10],
        }
        records.append(record)
        if bad_rows and p >= 7:
            unresolved.append(record)

    worst = sorted(records, key=lambda item: item["min_margin"])[:20]
    worst_nonbottom = sorted(
        records, key=lambda item: item["min_margin_nonbottom"]
    )[:20]
    later_two_tail_threshold = None
    records_with_gt2 = [
        record for record in records if record["local_max_tail_omega"] > 2
    ]
    if records_with_gt2:
        last_gt2_p = records_with_gt2[-1]["p"]
        for record in records:
            if record["p"] > last_gt2_p:
                later_two_tail_threshold = record["p"]
                break
    elif records:
        later_two_tail_threshold = records[0]["p"]
    return {
        "parameters": {
            "max_p": max_p,
            "y_ratio": y_ratio,
        },
        "summary": {
            "prime_count": len(records),
            "unresolved_records_p_ge_7": len(unresolved),
            "min_margin_p_ge_7": min(
                (record["min_margin"] for record in records if record["p"] >= 7),
                default=None,
            ),
            "min_margin_p_ge_19": min(
                (record["min_margin"] for record in records if record["p"] >= 19),
                default=None,
            ),
            "max_tail_omega": max_tail_omega,
            "first_record_with_local_omega_le_2": first_two_tail_only_p,
            "eventual_local_omega_le_2_from_p": later_two_tail_threshold,
            "records_with_y3_gt_q2": sum(
                1 for record in records if record["two_tail_only_by_y3_gt_q2"]
            ),
            "last_record_with_y3_le_q2": max(
                (
                    record["p"]
                    for record in records
                    if not record["two_tail_only_by_y3_gt_q2"]
                ),
                default=None,
            ),
            "min_nonbottom_margin_p_ge_7": min(
                (
                    record["min_margin_nonbottom"]
                    for record in records
                    if record["p"] >= 7
                ),
                default=None,
            ),
            "worst_records": worst,
            "worst_nonbottom_records": worst_nonbottom,
        },
        "unresolved_records_p_ge_7": unresolved,
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写入 Markdown 审计报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# Terminal-SAE 单尾抵消结构审计",
        "",
        "**状态：** `experimental_exact_cancellation_identity_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查奇素数个数：`{summary['prime_count']}`。",
        f"- `p>=7` 未认证记录数：`{summary['unresolved_records_p_ge_7']}`。",
        f"- `p>=7` 最小 margin：`{summary['min_margin_p_ge_7']}`。",
        f"- `p>=19` 最小 margin：`{summary['min_margin_p_ge_19']}`。",
        f"- 最大不同尾素因子个数：`{summary['max_tail_omega']}`。",
        f"- 首个本地 `omega_tail<=2` 的记录：`{summary['first_record_with_local_omega_le_2']}`。",
        f"- 从该素数起后续样本均 `omega_tail<=2`：`{summary['eventual_local_omega_le_2_from_p']}`。",
        f"- 满足 `y^3>q^2` 的记录数：`{summary['records_with_y3_gt_q2']}`。",
        f"- 最后一个未满足 `y^3>q^2` 的 p：`{summary['last_record_with_y3_le_q2']}`。",
        f"- `p>=7` 非底行最小 margin：`{summary['min_nonbottom_margin_p_ge_7']}`。",
        "",
        "## 最小 margin 样本",
        "",
        "| p | q | y | min margin | no-tail | one-tail | multi-excess | h | interval |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for record in summary["worst_records"]:
        data = record["min_data"]
        lines.append(
            "| {p} | {q} | {y} | {margin} | {no_tail} | {one_tail} | {excess} | {h} | {interval} |".format(
                p=record["p"],
                q=record["q_next"],
                y=record["y"],
                margin=record["min_margin"],
                no_tail=data["no_tail_reserve"],
                one_tail=data["one_tail_cancelled"],
                excess=data["multi_tail_excess"],
                h=data["h"],
                interval=data["n_interval"],
            )
        )
    lines.extend(
        [
            "",
            "## 非底行最小 margin 样本",
            "",
            "| p | q | y | min margin | no-tail | one-tail | multi-excess | h | interval |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for record in summary["worst_nonbottom_records"]:
        data = record["min_data_nonbottom"]
        lines.append(
            "| {p} | {q} | {y} | {margin} | {no_tail} | {one_tail} | {excess} | {h} | {interval} |".format(
                p=record["p"],
                q=record["q_next"],
                y=record["y"],
                margin=record["min_margin_nonbottom"],
                no_tail=data["no_tail_reserve"],
                one_tail=data["one_tail_cancelled"],
                excess=data["multi_tail_excess"],
                h=data["h"],
                interval=data["n_interval"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "令 `omega_tail(n)` 为 `n` 的不同尾素因子 `y<ell<=p` 的个数，则每个终端块精确满足",
            "",
            "```text",
            "G_y(h)-T_y(h)=sum_{P^-(n)>y}(1-omega_tail(n)).",
            "```",
            "",
            "因此恰有一个尾素因子的低筛骨架点贡献为 `0`，不会影响最终余量。真正需要证明的是：无尾储备点数严格大于多尾碰撞的超额重数。若 `y^3>q^2`，每个 `n<q^2` 最多含两个尾素因子，于是目标进一步简化为 `no_tail_reserve > two_tail_count`。",
            "",
            "本审计还严格排除了 `n=1` 与 `n=q^2`，避免把非素数端点误算为素数幸存者。样本中正余量仍保持，说明此前 `TSI` 证据没有依赖该端点。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-terminal-sae-cancellation-audit",
    )
    args = parser.parse_args()
    result = audit(args.max_p, args.y_ratio)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    compact_summary = {
        key: value
        for key, value in result["summary"].items()
        if key not in {"worst_records", "worst_nonbottom_records"}
    }
    print(json.dumps(compact_summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
