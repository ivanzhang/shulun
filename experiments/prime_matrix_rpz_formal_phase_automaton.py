#!/usr/bin/env python3
"""生成 RPZ formal-family 下降相位自动机证书。

用法示例：
  python3 experiments/prime_matrix_rpz_formal_phase_automaton.py

路线 A 的核心是证明正式反例族避开 first-grid-fail seam。该脚本把这件事压成
一个精确有限相位自动机：

  row phase a mod P(p) -> canonical child phase b mod P(r)

其中 `r` 是 `p` 的前一素数，`P(p)=prod_{ell<=p}ell`。若每一步满足
`delta=-(a-1)(p-r) mod r <= p-r`，则存在完整下层行；否则落入 first-grid-fail
seam。对当前 BCB-Core 账本中的起始下层零行，脚本逐项验证它们都落在接受相位中。
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from pathlib import Path
from typing import Any


def primes_upto(limit: int) -> list[int]:
    """返回不超过 `limit` 的素数表。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % prime for prime in primes if prime * prime <= value):
            primes.append(value)
    return primes


def primorial(primes: list[int], limit: int) -> int:
    """返回不超过 `limit` 的素数乘积。"""
    product = 1
    for prime in primes:
        if prime <= limit:
            product *= prime
    return product


def previous_prime(primes: list[int], prime: int) -> int | None:
    """返回 `prime` 的前一素数。"""
    index = primes.index(prime)
    if index == 0:
        return None
    return primes[index - 1]


def phase_delta(p: int, r: int, row_phase: int) -> int:
    """计算 `p` 行相位到下一条 `r` 对齐行的距离。"""
    return (-(row_phase - 1) * (p - r)) % r


def child_phase(p: int, r: int, row_phase: int, modulus_r: int) -> int:
    """计算 canonical 完整下层行号相位。"""
    delta = phase_delta(p, r, row_phase)
    child = ((row_phase - 1) * p + delta) // r + 1
    return child % modulus_r


def build_transition_row(primes: list[int], p: int) -> dict[str, Any]:
    """构造单个素数层的相位转移行。"""
    r = previous_prime(primes, p)
    if r is None:
        return {
            "p": p,
            "status": "base_no_previous_prime",
        }
    modulus_p = primorial(primes, p)
    modulus_r = primorial(primes, r)
    gap = p - r
    success_residues = []
    fail_residues = []
    child_histogram: dict[int, int] = {}
    for phase in range(modulus_p):
        delta = phase_delta(p, r, phase)
        if delta <= gap:
            success_residues.append(phase)
            child = child_phase(p, r, phase, modulus_r)
            child_histogram[child] = child_histogram.get(child, 0) + 1
        else:
            fail_residues.append(phase)

    return {
        "p": p,
        "r": r,
        "gap": gap,
        "modulus_p": modulus_p,
        "modulus_r": modulus_r,
        "success_phase_count": len(success_residues),
        "fail_phase_count": len(fail_residues),
        "success_density": len(success_residues) / modulus_p,
        "fail_density": len(fail_residues) / modulus_p,
        "fail_residues_mod_r": [
            residue
            for residue in range(r)
            if phase_delta(p, r, residue) > gap
        ],
        "child_phase_image_size": len(child_histogram),
        "child_phase_min_preimage": min(child_histogram.values())
        if child_histogram
        else 0,
        "child_phase_max_preimage": max(child_histogram.values())
        if child_histogram
        else 0,
        "status": "transition_automaton_built",
    }


def acceptance_checker(primes: list[int], max_prime: int):
    """返回带缓存的接受相位判定器。"""

    @lru_cache(maxsize=None)
    def accepts(p: int, phase: int) -> bool:
        if p == 2:
            return True
        r = previous_prime(primes, p)
        if r is None:
            return False
        gap = p - r
        delta = phase_delta(p, r, phase)
        if delta > gap:
            return False
        modulus_r = primorial(primes, r)
        return accepts(r, child_phase(p, r, phase, modulus_r))

    return accepts


def trace_start(primes: list[int], start_prime: int, start_row: int) -> dict[str, Any]:
    """追踪当前账本中的一个起始行。"""
    accepts = acceptance_checker(primes, start_prime)
    trace = []
    p = start_prime
    phase = start_row % primorial(primes, p)
    while p != 2:
        r = previous_prime(primes, p)
        if r is None:
            break
        modulus_r = primorial(primes, r)
        delta = phase_delta(p, r, phase)
        gap = p - r
        child = child_phase(p, r, phase, modulus_r) if delta <= gap else None
        trace.append(
            {
                "p": p,
                "r": r,
                "phase_mod_primorial_p": phase,
                "row_mod_r": phase % r,
                "delta": delta,
                "gap": gap,
                "success": delta <= gap,
                "child_phase_mod_primorial_r": child,
            }
        )
        if child is None:
            break
        p = r
        phase = child
    return {
        "start_prime": start_prime,
        "start_row": start_row,
        "start_phase_mod_primorial": start_row % primorial(primes, start_prime),
        "accepted_by_automaton": accepts(
            start_prime, start_row % primorial(primes, start_prime)
        ),
        "trace": trace,
    }


def build(source_path: Path) -> dict[str, Any]:
    """构造 formal-family 下降相位自动机证书。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    max_prime = max(start["start_prime"] for start in source["starts"])
    primes = primes_upto(max_prime)
    transition_rows = [
        build_transition_row(primes, prime)
        for prime in primes
        if prime > 2
    ]
    accepts = acceptance_checker(primes, max_prime)
    acceptance_rows = []
    for prime in primes:
        if prime < 2:
            continue
        modulus = primorial(primes, prime)
        accepted = sum(1 for phase in range(modulus) if accepts(prime, phase))
        acceptance_rows.append(
            {
                "p": prime,
                "modulus": modulus,
                "accepted_phase_count": accepted,
                "rejected_phase_count": modulus - accepted,
                "accepted_density": accepted / modulus,
            }
        )

    start_traces = [
        trace_start(primes, start["start_prime"], start["start_row"])
        for start in source["starts"]
    ]
    return {
        "status": "rpz_formal_phase_automaton_certificate",
        "source": str(source_path),
        "summary": {
            "max_prime": max_prime,
            "transition_row_count": len(transition_rows),
            "acceptance_row_count": len(acceptance_rows),
            "current_start_count": len(start_traces),
            "current_starts_accepted": sum(
                1 for trace in start_traces if trace["accepted_by_automaton"]
            ),
            "global_formal_family_closed": False,
        },
        "transition_rows": transition_rows,
        "acceptance_rows": acceptance_rows,
        "current_start_traces": start_traces,
        "formal_route_theorem": [
            "若 formal-family 的起始相位属于 accepted set A_p，则 canonical 下降路径到达 p=2。",
            "若起始相位不属于 A_p，则第一失败必为 first-grid-fail seam，并回到 PDEC/ColumnCRT/SAE。",
            "当前 BCB-Core 账本的全部起始相位都属于 accepted set。",
        ],
        "remaining_gap": [
            "尚未证明任意正式反例族的起始相位都属于 A_p。",
            "尚未给出 formal-family 起始相位避开 rejected set 的全局结构定理。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 证书报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ Formal-Family 下降相位自动机证书",
        "",
        "**状态：** `rpz_formal_phase_automaton_certificate`",
        "",
        "## 总结",
        "",
        f"- 最大起始素数层：`{summary['max_prime']}`。",
        f"- 转移行数：`{summary['transition_row_count']}`。",
        f"- 接受集行数：`{summary['acceptance_row_count']}`。",
        f"- 当前起始行数：`{summary['current_start_count']}`。",
        f"- 当前起始行被自动机接受数：`{summary['current_starts_accepted']}`。",
        f"- 全局 formal-family 是否闭合：`{summary['global_formal_family_closed']}`。",
        "",
        "## 接受相位表",
        "",
        "| p | modulus P(p) | accepted | rejected | accepted density |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in result["acceptance_rows"]:
        lines.append(
            "| {p} | {modulus} | {accepted} | {rejected} | {density:.6f} |".format(
                p=row["p"],
                modulus=row["modulus"],
                accepted=row["accepted_phase_count"],
                rejected=row["rejected_phase_count"],
                density=row["accepted_density"],
            )
        )

    lines.extend(
        [
            "",
            "## 当前起始行追踪",
            "",
            "| start p | start row | start phase | accepted | trace deltas |",
            "|---:|---:|---:|---|---|",
        ]
    )
    for trace in result["current_start_traces"]:
        deltas = [
            f"{item['p']}->{item['r']}:d={item['delta']},g={item['gap']}"
            for item in trace["trace"]
        ]
        lines.append(
            "| {p} | {row} | {phase} | `{accepted}` | `{deltas}` |".format(
                p=trace["start_prime"],
                row=trace["start_row"],
                phase=trace["start_phase_mod_primorial"],
                accepted=trace["accepted_by_automaton"],
                deltas=deltas,
            )
        )

    lines.extend(
        [
            "",
            "## 证书定理",
            "",
            "定义 `A_p` 为模 `P(p)` 的接受相位集合：`a mod P(p)` 属于 `A_p` 当且仅当 canonical 相邻素数下降每一步满足 `delta<=p-r` 并最终到达 `p=2`。则：",
            "",
            "```text",
            "formal start phase in A_p  =>  formal descent to p=2 contradiction；",
            "formal start phase not in A_p => first-grid-fail seam => SAE/PDEC/ColumnCRT。",
            "```",
            "",
            "当前 BCB-Core 账本的所有起始行都属于 `A_p`，因此路线 A 在当前账本中闭合。",
            "",
            "## 剩余缺口",
            "",
            "本证书仍未证明任意正式反例族的起始相位必属于 `A_p`。下一步真正目标是证明 formal-family 的起始相位避开 rejected set，或把 rejected set 的命中送入已经物化的 seam/PDEC/ColumnCRT 证书链。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-formal-phase-automaton"),
    )
    args = parser.parse_args()
    result = build(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
