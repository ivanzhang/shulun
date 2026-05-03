#!/usr/bin/env python3
"""生成 FO-PDEC 的低模缺陷方程审计。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_lowmod_audit.py
  python3 experiments/prime_matrix_wsh_fo_pdec_lowmod_audit.py \
    --input docs/monograph/prime-matrix-wsh-fixed-offset-pdec-ledger.json

目标：
  把每个固定偏移缺失候选 n=b+d 的解释因子 ell 写成精确 CRT 行方程：

      n=(r-1)q+c, ell|n
      => r == 1 - c*q^{-1} (mod ell)

  同时验证双尾半素数 b=u*v 满足 bilinear 方程：

      u*v + d == 0 (mod ell)

注意：这是低模缺陷方程账本，不是 FO-PDEC 全局排斥证明。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def factor_semiprime(number: int, limit: int) -> list[int]:
    """在 `<=limit` 内分解半素数，返回互异或重复素因子列表。"""
    factors: list[int] = []
    remaining = number
    divisor = 2
    while divisor * divisor <= remaining and divisor <= limit:
        while remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        factors.append(remaining)
    return factors


def row_and_column(number: int, width: int) -> tuple[int, int]:
    """把整数写成 `width` 方阵坐标。"""
    row = (number - 1) // width + 1
    column = (number - 1) % width + 1
    return row, column


def build_audit(source: dict) -> dict:
    """生成低模方程审计结果。"""
    equations: list[dict] = []
    factor_counter: Counter[int] = Counter()
    residue_counter: Counter[tuple[int, int]] = Counter()
    row_factor_counter: Counter[tuple[int, int, int]] = Counter()
    block_factor_counter: Counter[tuple[int, int]] = Counter()
    crt_failures = 0
    bilinear_failures = 0
    semiprime_factor_failures = 0

    for offset_row_index, offset_row in enumerate(source["offset_rows"], start=1):
        p = offset_row["p"]
        q = offset_row["q"]
        matrix_row = offset_row["row"]
        offset = offset_row["offset"]
        for candidate_row in offset_row["candidate_rows"]:
            if candidate_row["is_prime"]:
                continue
            semiprime = candidate_row["semiprime"]
            candidate = candidate_row["candidate"]
            tail_factors = factor_semiprime(semiprime, p)
            if len(tail_factors) != 2 or tail_factors[0] * tail_factors[1] != semiprime:
                semiprime_factor_failures += 1
            candidate_matrix_row, column = row_and_column(candidate, q)
            for explaining_factor in candidate_row["factors_le_p"]:
                inverse_q = pow(q % explaining_factor, -1, explaining_factor)
                target_residue = (1 - column * inverse_q) % explaining_factor
                row_residue = candidate_matrix_row % explaining_factor
                crt_ok = row_residue == target_residue
                bilinear_ok = (semiprime + offset) % explaining_factor == 0
                if not crt_ok:
                    crt_failures += 1
                if not bilinear_ok:
                    bilinear_failures += 1
                factor_counter.update([explaining_factor])
                residue_counter.update([(explaining_factor, target_residue)])
                row_factor_counter.update([(q, matrix_row, explaining_factor)])
                block_factor_counter.update([(offset_row["block_index"], explaining_factor)])
                equations.append(
                    {
                        "offset_row_index": offset_row_index,
                        "block_index": offset_row["block_index"],
                        "p": p,
                        "q": q,
                        "source_row": matrix_row,
                        "candidate_row": candidate_matrix_row,
                        "column": column,
                        "offset": offset,
                        "semiprime": semiprime,
                        "tail_factors": tail_factors,
                        "candidate": candidate,
                        "explaining_factor": explaining_factor,
                        "row_residue": row_residue,
                        "target_residue": target_residue,
                        "crt_equation_ok": crt_ok,
                        "bilinear_equation_ok": bilinear_ok,
                    }
                )

    return {
        "status": "finite_fo_pdec_lowmod_equation_audit_not_global_proof",
        "summary": {
            "offset_rows": len(source["offset_rows"]),
            "lowmod_equations": len(equations),
            "distinct_explaining_factors": len(factor_counter),
            "crt_equation_failures": crt_failures,
            "bilinear_equation_failures": bilinear_failures,
            "semiprime_factor_failures": semiprime_factor_failures,
            "max_global_factor_load": max(factor_counter.values(), default=0),
            "max_residue_equation_load": max(residue_counter.values(), default=0),
            "max_same_row_factor_load": max(row_factor_counter.values(), default=0),
            "max_same_block_factor_load": max(block_factor_counter.values(), default=0),
            "top_factors": [
                {"factor": factor, "load": load}
                for factor, load in factor_counter.most_common(20)
            ],
            "top_factor_residues": [
                {"factor": factor, "residue": residue, "load": load}
                for (factor, residue), load in residue_counter.most_common(20)
            ],
            "top_row_factors": [
                {"q": q, "row": row, "factor": factor, "load": load}
                for (q, row, factor), load in row_factor_counter.most_common(20)
            ],
        },
        "equations": equations,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    lines = [
        "# FO-PDEC 低模缺陷方程审计",
        "",
        "**状态：** `finite_fo_pdec_lowmod_equation_audit_not_global_proof`",
        "",
        "本文档把固定偏移缺失候选逐项转写为 CRT 低模方程和双尾双线性方程。它证明的是方程化与有限核验，不是 `FO-PDEC` 的全局排斥。",
        "",
        "## 摘要",
        "",
        f"- 满载偏移行数：`{summary['offset_rows']}`。",
        f"- 低模方程数：`{summary['lowmod_equations']}`。",
        f"- 互异解释因子数：`{summary['distinct_explaining_factors']}`。",
        f"- CRT 方程失败数：`{summary['crt_equation_failures']}`。",
        f"- 双线性方程失败数：`{summary['bilinear_equation_failures']}`。",
        f"- 半素数分解失败数：`{summary['semiprime_factor_failures']}`。",
        f"- 全局最大解释因子负载：`{summary['max_global_factor_load']}`。",
        f"- 最大同因子同残基方程负载：`{summary['max_residue_equation_load']}`。",
        f"- 最大同 `(q,row,factor)` 负载：`{summary['max_same_row_factor_load']}`。",
        f"- 最大同 `(block,factor)` 负载：`{summary['max_same_block_factor_load']}`。",
        f"- 最高解释因子：`{summary['top_factors']}`。",
        f"- 最高因子-残基：`{summary['top_factor_residues']}`。",
        "",
        "## 方程模板",
        "",
        "若 `n=b+d=(r-1)q+c` 且 `ell|n`，则",
        "",
        "\\[",
        "  r \\equiv 1-cq^{-1}\\pmod \\ell。",
        "\\]",
        "",
        "若 `b=u v` 是双尾半素数，则同一条缺失还满足",
        "",
        "\\[",
        "  u v+d\\equiv0\\pmod \\ell。",
        "\\]",
        "",
        "因此每个缺失候选都不是孤立事实，而是一条低模行相位约束和一条双线性同余约束。",
        "",
        "## 方程样本",
        "",
        "| q | row | col | offset | semiprime | tails | candidate | ell | row mod ell | target | ok |",
        "| ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for equation in result["equations"][:80]:
        lines.append(
            "| {q} | {row} | {column} | {offset} | {semiprime} | {tails} | {candidate} | {factor} | {row_residue} | {target} | {ok} |".format(
                q=equation["q"],
                row=equation["candidate_row"],
                column=equation["column"],
                offset=equation["offset"],
                semiprime=equation["semiprime"],
                tails=equation["tail_factors"],
                candidate=equation["candidate"],
                factor=equation["explaining_factor"],
                row_residue=equation["row_residue"],
                target=equation["target_residue"],
                ok=equation["crt_equation_ok"] and equation["bilinear_equation_ok"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "本账本把 `FO-PDEC` 的剩余从口头描述压成一个明确不等式目标：若这些低模方程在相邻行、镜像块或递归壳层中持续出现，则它们给出 persistent PDEC；若不持续，则必须进入 SAE/Endpoint 的稀疏逃逸账本。",
            "",
            "当前有限样本中所有 CRT 方程与双线性方程均通过，且最大同 `(q,row,factor)` 负载为有限可见值。全局证明仍需一个统一的持久化下界或稀疏逃逸排斥，不得把该有限方程账本直接升级为无条件闭合。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/monograph/prime-matrix-wsh-fixed-offset-pdec-ledger.json",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit",
    )
    args = parser.parse_args()
    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = build_audit(source)
    output_prefix = Path(args.out_prefix)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, output_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
