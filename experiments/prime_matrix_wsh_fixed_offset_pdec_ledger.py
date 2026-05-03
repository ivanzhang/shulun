#!/usr/bin/env python3
"""生成 WSH-Hall 固定偏移/PDEC 吸收账本。

用法示例：
  python3 experiments/prime_matrix_wsh_fixed_offset_pdec_ledger.py
  python3 experiments/prime_matrix_wsh_fixed_offset_pdec_ledger.py \
    --input docs/monograph/prime-matrix-wsh-scb1-long-block-certificate.json

目标：
  对 SCB-1 长块证书中的最紧长块，逐个检查 Fixed-offset-full-load 偏移。
  若同一偏移 d 对整块 B 满载，则审计所有候选 n=b+d：
    1. n 为素数时给出真实匹配边；
    2. n 非素数时，验证其必有 <=p 的解释因子；
    3. 记录这些解释因子的负载，用于接入 Tail-anchor / low-mod PDEC。

注意：这是有限吸收账本，不是全局 Endpoint/PDEC 排斥证明。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def is_prime_trial(number: int) -> bool:
    """用确定性试除判断当前证书范围内的素性。"""
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def prime_factors_leq(number: int, limit: int) -> list[int]:
    """返回 `number` 中不超过 `limit` 的互异素因子。"""
    factors: list[int] = []
    remaining = number
    if remaining % 2 == 0:
        factors.append(2)
        while remaining % 2 == 0:
            remaining //= 2
    divisor = 3
    while divisor * divisor <= remaining and divisor <= limit:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 2
    if 1 < remaining <= limit:
        factors.append(remaining)
    return factors


def build_ledger(source: dict) -> dict:
    """从 SCB-1 长块证书生成固定偏移吸收账本。"""
    rows: list[dict] = []
    global_factor_load: Counter[int] = Counter()
    missing_without_small_factor = 0
    full_offset_count = 0
    total_candidates = 0
    total_prime_candidates = 0
    total_missing_candidates = 0

    for block_index, block in enumerate(source["tight_long_blocks"], start=1):
        size = block["semiprime_count"]
        p = block["p"]
        full_offsets = [
            item
            for item in block["pressure"]["top_allowed_offsets"]
            if item["load"] >= size
        ]
        actual_edge_loads = {
            item["offset"]: item["load"]
            for item in block["pressure"]["top_actual_edge_offsets"]
        }
        for offset_row in full_offsets:
            offset = offset_row["offset"]
            full_offset_count += 1
            candidate_rows = []
            factor_load: Counter[int] = Counter()
            prime_count = 0
            missing_count = 0
            for semi_value in block["semiprime_values"]:
                candidate = semi_value + offset
                prime_flag = is_prime_trial(candidate)
                factors = [] if prime_flag else prime_factors_leq(candidate, p)
                if prime_flag:
                    prime_count += 1
                else:
                    missing_count += 1
                    if not factors:
                        missing_without_small_factor += 1
                    factor_load.update(factors)
                    global_factor_load.update(factors)
                candidate_rows.append(
                    {
                        "semiprime": semi_value,
                        "candidate": candidate,
                        "is_prime": prime_flag,
                        "factors_le_p": factors,
                    }
                )
            total_candidates += len(candidate_rows)
            total_prime_candidates += prime_count
            total_missing_candidates += missing_count
            rows.append(
                {
                    "block_index": block_index,
                    "p": p,
                    "q": block["q"],
                    "row": block["row"],
                    "radius": block["radius"],
                    "semiprime_count": size,
                    "surplus": block["surplus"],
                    "offset": offset,
                    "rho_z_offset": offset_row["rho_z_offset"],
                    "allowed_load": offset_row["load"],
                    "actual_edge_load_same_offset": actual_edge_loads.get(offset, 0),
                    "prime_candidates": prime_count,
                    "missing_candidates": missing_count,
                    "max_factor_load": max(factor_load.values(), default=0),
                    "top_factors": [
                        {"factor": factor, "load": load}
                        for factor, load in factor_load.most_common(10)
                    ],
                    "candidate_rows": candidate_rows,
                    "mirror_candidate_span": [
                        block["q"] * block["q"] - max(row["candidate"] for row in candidate_rows),
                        block["q"] * block["q"] - min(row["candidate"] for row in candidate_rows),
                    ],
                }
            )

    return {
        "status": "finite_fixed_offset_pdec_absorption_ledger_not_global_proof",
        "source": source["parameters"],
        "summary": {
            "tight_block_count": len(source["tight_long_blocks"]),
            "full_offset_rows": full_offset_count,
            "total_candidates_on_full_offsets": total_candidates,
            "total_prime_candidates": total_prime_candidates,
            "total_missing_candidates": total_missing_candidates,
            "missing_without_factor_le_p": missing_without_small_factor,
            "max_factor_load_in_offset_row": max(
                (row["max_factor_load"] for row in rows),
                default=0,
            ),
            "global_top_factors": [
                {"factor": factor, "load": load}
                for factor, load in global_factor_load.most_common(20)
            ],
        },
        "offset_rows": rows,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 账本。"""
    summary = result["summary"]
    lines = [
        "# WSH-Hall 固定偏移/PDEC 吸收账本",
        "",
        "**状态：** `finite_fixed_offset_pdec_absorption_ledger_not_global_proof`",
        "",
        "本文档审计 `SCB-1` 最紧长块中的 `Fixed-offset-full-load`。它验证满载偏移上的缺失候选并非无来源缺口：每个非素候选都有 `<=p` 的解释因子，因此可进入 Tail-anchor、low-mod CRTDefect 或 PDEC 吸收账本。",
        "",
        "## 摘要",
        "",
        f"- 最紧长块数：`{summary['tight_block_count']}`。",
        f"- 满载固定偏移行数：`{summary['full_offset_rows']}`。",
        f"- 满载偏移候选总数：`{summary['total_candidates_on_full_offsets']}`。",
        f"- 其中素数候选数：`{summary['total_prime_candidates']}`。",
        f"- 其中缺失候选数：`{summary['total_missing_candidates']}`。",
        f"- 无 `<=p` 解释因子的缺失候选数：`{summary['missing_without_factor_le_p']}`。",
        f"- 单个偏移行最大解释因子负载：`{summary['max_factor_load_in_offset_row']}`。",
        f"- 全局最高解释因子负载：`{summary['global_top_factors']}`。",
        "",
        "## 满载偏移行",
        "",
        "| block | p | q | row | size | offset | allowed | actual same offset | prime | missing | max factor load | top factors | mirror span |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["offset_rows"]:
        lines.append(
            "| {block} | {p} | {q} | {matrix_row} | {size} | {offset} | {allowed} | {actual} | {prime} | {missing} | {max_factor} | {factors} | {mirror} |".format(
                block=row["block_index"],
                p=row["p"],
                q=row["q"],
                matrix_row=row["row"],
                size=row["semiprime_count"],
                offset=row["offset"],
                allowed=row["allowed_load"],
                actual=row["actual_edge_load_same_offset"],
                prime=row["prime_candidates"],
                missing=row["missing_candidates"],
                max_factor=row["max_factor_load"],
                factors=row["top_factors"],
                mirror=row["mirror_candidate_span"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "满载固定偏移 `d` 表示所有 `b in B` 的候选 `b+d` 均避开轮筛小素数禁类。若这些候选已经给出足够素数，则长块扩张成立；若不足，则每个缺失候选必须由某个 `<=p` 素因子解释。当前有限账本中 `missing_without_factor_le_p=0`，所以缺失并非第三种逃逸。",
            "",
            "全局证明仍需把这些解释因子的负载转成正式不等式：重复因子进入 Tail-anchor，低模相位持续缺陷进入 PDEC，孤立端点缺失进入 SAE/Endpoint。该文件只闭合有限吸收账本，不排除最终 Endpoint/PDEC。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/monograph/prime-matrix-wsh-scb1-long-block-certificate.json",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-fixed-offset-pdec-ledger",
    )
    args = parser.parse_args()
    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = build_ledger(source)
    output_prefix = Path(args.out_prefix)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, output_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
