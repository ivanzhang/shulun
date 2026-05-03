#!/usr/bin/env python3
"""生成 RPZ-BCB 短平台 Jacobsthal 端点相位证书。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_short_platform_embedding_certificate.py
  python3 experiments/prime_matrix_rpz_bcb_short_platform_embedding_certificate.py --max-h 53

本脚本读取 Ziller--Morack 附属 `moduli.txt` 中最长 Jacobsthal 覆盖块的
模表示，重建每个最长块的左端相位，并对短平台参数

  N = P + m - 1 - 2T <= G(h)

生成 max-block endpoint phase family：

  E^max_{h,N} = {a+t mod P(h): a 为最长覆盖块左端, 0<=t<=G(h)-N}。

注意：这是“最长块端点证书”。它能材料化短平台出口的主要风险相位，但
不等同于完整的 `E_{h,N}`，因为完整集合还需要覆盖所有长度 >=N 的极大
低筛覆盖块。该边界必须保留在论文审稿说明中。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import urllib.request
from pathlib import Path
from typing import Any


MODULI_URL = "https://arxiv.org/src/1611.03310v2/anc/moduli.txt"


def is_prime(value: int) -> bool:
    """朴素素性测试；本脚本只处理附属表中的小素数。"""
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def primes_upto(value: int) -> list[int]:
    """返回不超过 `value` 的全部素数。"""
    return [candidate for candidate in range(2, value + 1) if is_prime(candidate)]


def next_prime_greater_than(value: int) -> int:
    """返回严格大于 `value` 的最小素数。"""
    candidate = value + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def load_text(url: str, cache_path: Path | None) -> str:
    """读取附属数据；若提供缓存路径则优先使用本地缓存。"""
    if cache_path and cache_path.exists():
        return cache_path.read_text(encoding="utf-8")
    with urllib.request.urlopen(url, timeout=30) as response:
        text = response.read().decode("utf-8", errors="replace")
    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(text, encoding="utf-8")
    return text


def crt_pair(left_residue: int, left_modulus: int, right_residue: int, right_modulus: int) -> tuple[int, int]:
    """合并两个相容同余，允许模数有公共因子。"""
    gcd_value = math.gcd(left_modulus, right_modulus)
    if (right_residue - left_residue) % gcd_value != 0:
        raise ValueError("不相容的 CRT 约束")
    reduced_left = left_modulus // gcd_value
    reduced_right = right_modulus // gcd_value
    inverse = pow(reduced_left, -1, reduced_right)
    multiplier = ((right_residue - left_residue) // gcd_value * inverse) % reduced_right
    modulus = left_modulus * reduced_right
    return (left_residue + left_modulus * multiplier) % modulus, modulus


def parse_moduli_blocks(text: str) -> dict[int, dict[str, Any]]:
    """解析 `moduli.txt` 的每个 n/p_n 数据块。"""
    pattern = re.compile(
        r"n=(\d+), p_n=(\d+), omega\(n\)=(\d+), n_seq=(\d+)\n(.*?)(?=\n-{75,}|\Z)",
        re.S,
    )
    blocks: dict[int, dict[str, Any]] = {}
    for match in pattern.finditer(text):
        prime_index, h_value, omega, sequence_count = map(int, match.groups()[:4])
        body = match.group(5)
        sequences = []
        for line in body.splitlines():
            if "*" not in line:
                continue
            sequence = [int(token) for token in line.split("*", 1)[1].split()]
            if len(sequence) != omega:
                raise ValueError(f"h={h_value} 的序列长度不等于 omega")
            sequences.append(sequence)
        if len(sequences) != sequence_count:
            raise ValueError(f"h={h_value} 的序列条数不等于 n_seq")
        blocks[h_value] = {
            "prime_index": prime_index,
            "h": h_value,
            "omega": omega,
            "G_h": 2 * omega + 1,
            "n_seq": sequence_count,
            "sequences": sequences,
        }
    return blocks


def left_endpoint_residue(sequence: list[int]) -> tuple[int, int]:
    """由奇位置最小模序列重建完整覆盖块的偶左端相位。"""
    residue = 0
    modulus = 2
    for index, prime in enumerate(sequence):
        # 覆盖块左端为 A；奇位置 A+1+2j 被 sequence[j] 整除。
        congruence = -(1 + 2 * index) % prime
        residue, modulus = crt_pair(residue, modulus, congruence, prime)
    return residue, modulus


def verify_full_block(left_endpoint: int, modulus: int, length: int) -> dict[str, Any]:
    """验证重建块确为覆盖块，且两侧边界未被低筛覆盖。"""
    covered = all(math.gcd((left_endpoint + offset) % modulus, modulus) > 1 for offset in range(length))
    left_boundary_covered = math.gcd((left_endpoint - 1) % modulus, modulus) > 1
    right_boundary_covered = math.gcd((left_endpoint + length) % modulus, modulus) > 1
    return {
        "covered": covered,
        "left_boundary_uncovered": not left_boundary_covered,
        "right_boundary_uncovered": not right_boundary_covered,
        "maximal_in_this_phase": covered and not left_boundary_covered and not right_boundary_covered,
    }


def endpoint_digest(values: list[int]) -> str:
    """对相位集合生成稳定哈希，避免在主报告中塞入过多大整数。"""
    hasher = hashlib.sha256()
    for value in values:
        hasher.update(str(value).encode("ascii"))
        hasher.update(b"\n")
    return hasher.hexdigest()


def summarize_row(row: dict[str, Any] | None) -> dict[str, Any] | None:
    """提取适合放入摘要区的短行，避免重复塞入完整相位表。"""
    if row is None:
        return None
    keys = [
        "h",
        "prime_index",
        "G_h",
        "minimal_top_prime_gt_2h",
        "short_core_length_N",
        "deficit_D_G_minus_N",
        "max_block_count",
        "unique_endpoint_count",
        "endpoint_sha256",
    ]
    return {key: row[key] for key in keys}


def build_certificate(
    blocks: dict[int, dict[str, Any]],
    min_h: int,
    max_h: int,
    platform_length: int,
    tail_threshold: int,
    sample_limit: int,
    full_endpoint_limit: int,
) -> dict[str, Any]:
    """构造短平台最长块端点证书。"""
    rows = []
    verified_blocks = 0
    failed_verifications = []
    for h_value in sorted(blocks):
        if h_value < min_h or h_value > max_h:
            continue
        block = blocks[h_value]
        primes = primes_upto(h_value)
        primorial = math.prod(primes)
        top_prime = next_prime_greater_than(2 * h_value)
        core_length = top_prime + platform_length - 1 - 2 * tail_threshold
        deficit = block["G_h"] - core_length
        if deficit < 0:
            continue

        left_endpoints = []
        for sequence_index, sequence in enumerate(block["sequences"], start=1):
            left_endpoint, modulus = left_endpoint_residue(sequence)
            if modulus != primorial:
                raise ValueError(f"h={h_value} 的 CRT 模数未覆盖完整 primorial")
            verification = verify_full_block(left_endpoint, primorial, block["G_h"])
            if verification["maximal_in_this_phase"]:
                verified_blocks += 1
            else:
                failed_verifications.append(
                    {
                        "h": h_value,
                        "sequence_index": sequence_index,
                        "left_endpoint": left_endpoint,
                        "verification": verification,
                    }
                )
            left_endpoints.append(left_endpoint)

        endpoint_values = sorted(
            {
                (left_endpoint + shift) % primorial
                for left_endpoint in left_endpoints
                for shift in range(deficit + 1)
            }
        )
        row = {
            "h": h_value,
            "prime_index": block["prime_index"],
            "primorial_digits": len(str(primorial)),
            "G_h": block["G_h"],
            "minimal_top_prime_gt_2h": top_prime,
            "platform_length": platform_length,
            "tail_threshold": tail_threshold,
            "short_core_length_N": core_length,
            "deficit_D_G_minus_N": deficit,
            "max_block_count": len(left_endpoints),
            "raw_endpoint_bound": len(left_endpoints) * (deficit + 1),
            "unique_endpoint_count": len(endpoint_values),
            "endpoint_sha256": endpoint_digest(endpoint_values),
            "left_endpoint_sample": left_endpoints[:sample_limit],
            "endpoint_sample": endpoint_values[:sample_limit],
            "full_endpoints": endpoint_values if len(endpoint_values) <= full_endpoint_limit else None,
        }
        rows.append(row)

    first_nontrivial = next((row for row in rows if row["h"] >= 5), None)
    return {
        "status": "rpz_bcb_short_platform_embedding_certificate",
        "source": {
            "url": MODULI_URL,
            "paper": "Mario Ziller and John F. Morack, Algorithmic concepts for the computation of Jacobsthal's function, arXiv:1611.03310",
            "data_role": "max-block endpoint certificate, not complete E_{h,N} proof",
        },
        "parameters": {
            "min_h": min_h,
            "max_h": max_h,
            "platform_length": platform_length,
            "tail_threshold": tail_threshold,
            "short_core_length_formula": "N=P+m-1-2T with P=nextprime(2h)",
            "endpoint_family": "Emax_{h,N}={a+t mod P(h): a max-block left endpoint, 0<=t<=G(h)-N}",
        },
        "summary": {
            "short_rows": len(rows),
            "first_nontrivial_short_row": summarize_row(first_nontrivial),
            "verified_max_blocks": verified_blocks,
            "failed_max_block_verifications": len(failed_verifications),
            "largest_unique_endpoint_count": max((row["unique_endpoint_count"] for row in rows), default=0),
        },
        "rows": rows,
        "failed_verifications": failed_verifications,
        "review_boundary": [
            "每条最长块相位均由 CRT 从 Ziller--Morack 的模表示重建，并验证覆盖及两侧边界非覆盖。",
            "该证书只覆盖最长 Jacobsthal 块产生的短平台 endpoint 相位。",
            "完整闭合仍需证明所有长度 >=N 的低筛覆盖块都可归约到该最长块相位族，或另行枚举完整 E_{h,N}。",
            "因此本证书是 PDEC/ColumnCRT 的材料化输入，不是 Prime Matrix 行命题的最终无条件证明。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审稿报告。"""
    summary = result["summary"]
    first_row = summary["first_nontrivial_short_row"]
    lines = [
        "# RPZ-BCB 短平台最长块端点证书",
        "",
        "**状态：** `rpz_bcb_short_platform_embedding_certificate`",
        "",
        "## 总结",
        "",
        f"- 短平台行数：`{summary['short_rows']}`。",
        (
            "- 首个 `h>=5` 短平台行："
            f"`h={first_row['h']}, P={first_row['minimal_top_prime_gt_2h']}, "
            f"N={first_row['short_core_length_N']}, D={first_row['deficit_D_G_minus_N']}, "
            f"endpoints={first_row['unique_endpoint_count']}`。"
            if first_row
            else "- 首个 `h>=5` 短平台行：无。"
        ),
        f"- 已验证最长块数：`{summary['verified_max_blocks']}`。",
        f"- 验证失败块数：`{summary['failed_max_block_verifications']}`。",
        f"- 最大唯一 endpoint 数：`{summary['largest_unique_endpoint_count']}`。",
        "",
        "## 证书含义",
        "",
        "给定 `N=P+m-1-2T`，若 `N<=G(h)`，最长块相位给出有限集合",
        "",
        "```text",
        "Emax_{h,N}={a+t mod P(h): a 为最长覆盖块左端, 0<=t<=G(h)-N}。",
        "```",
        "",
        "`Emax_{h,N}` 是短平台出口的可计算材料化对象。它可以喂给 PDEC/ColumnCRT 或 SAE 接口。",
        "",
        "## 行摘录",
        "",
        "| h | G(h) | P | N | D | max blocks | unique endpoints | primorial digits | sha256 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["rows"][:30]:
        lines.append(
            "| {h} | {G} | {P} | {N} | {D} | {blocks} | {endpoints} | {digits} | `{sha}` |".format(
                h=row["h"],
                G=row["G_h"],
                P=row["minimal_top_prime_gt_2h"],
                N=row["short_core_length_N"],
                D=row["deficit_D_G_minus_N"],
                blocks=row["max_block_count"],
                endpoints=row["unique_endpoint_count"],
                digits=row["primorial_digits"],
                sha=row["endpoint_sha256"][:16],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿边界",
            "",
            "本证书没有宣称完整 `E_{h,N}` 已枚举。它只枚举最长 Jacobsthal 块给出的 `Emax_{h,N}`。",
            "要把短平台分支最终闭合，还需证明任意长度 `>=N` 的覆盖块可归入最长块相位，或生成完整覆盖块证书。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=MODULI_URL)
    parser.add_argument("--cache-path", type=Path, default=None)
    parser.add_argument("--min-h", type=int, default=3)
    parser.add_argument("--max-h", type=int, default=251)
    parser.add_argument("--platform-length", type=int, default=5)
    parser.add_argument("--tail-threshold", type=int, default=4)
    parser.add_argument("--sample-limit", type=int, default=8)
    parser.add_argument("--full-endpoint-limit", type=int, default=0)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-short-platform-embedding-certificate"),
    )
    args = parser.parse_args()

    text = load_text(args.url, args.cache_path)
    blocks = parse_moduli_blocks(text)
    result = build_certificate(
        blocks=blocks,
        min_h=args.min_h,
        max_h=args.max_h,
        platform_length=args.platform_length,
        tail_threshold=args.tail_threshold,
        sample_limit=args.sample_limit,
        full_endpoint_limit=args.full_endpoint_limit,
    )
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
