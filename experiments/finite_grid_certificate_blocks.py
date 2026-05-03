#!/usr/bin/env python3
"""分块生成/校验 P×P 方阵行列素数见证证书。

相比 finite_grid_certificate.py，本脚本按 P 区间输出多个 JSONL 记录，便于续跑、
分块存储和未来扩大到 P<=10^5/10^6。

用法示例：
  python3 experiments/finite_grid_certificate_blocks.py generate --min-p 3 --max-p 1000 --block-size 200 --output-dir /tmp/grid-blocks
  python3 experiments/finite_grid_certificate_blocks.py check --input-dir /tmp/grid-blocks
"""
from __future__ import annotations

import argparse
import gzip
import json
from math import isqrt
from pathlib import Path
from typing import Any, Iterable


def sieve(n: int) -> bytearray:
    """返回 0..n 的素性表；用 bytearray 降低大范围验证内存。"""
    if n < 2:
        return bytearray(n + 1)
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0] = is_prime[1] = 0
    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return is_prime


def primes_up_to(n: int) -> list[int]:
    """列出不超过 n 的素数。"""
    table = sieve(n)
    return [i for i, ok in enumerate(table) if ok]


def segmented_prime_flags(values: list[int], base_primes: list[int], segment_size: int) -> dict[int, bool]:
    """对给定见证值做分段筛素性判定。

    只为包含见证值的窗口建筛表，内存约为 segment_size 字节，适合大 P 证书校验。
    """
    if not values:
        return {}
    unique_values = sorted(set(values))
    result: dict[int, bool] = {}
    index = 0
    while index < len(unique_values):
        low = (unique_values[index] // segment_size) * segment_size
        high = low + segment_size - 1
        window_start = index
        while index < len(unique_values) and unique_values[index] <= high:
            index += 1
        segment_values = unique_values[window_start:index]

        segment = bytearray(b"\x01") * (high - low + 1)
        if low == 0:
            segment[0:2] = b"\x00\x00"
        elif low == 1:
            segment[0] = 0
        for prime in base_primes:
            square = prime * prime
            if square > high:
                break
            first = max(square, ((low + prime - 1) // prime) * prime)
            segment[first - low : high - low + 1 : prime] = b"\x00" * (((high - first) // prime) + 1)
        for value in segment_values:
            result[value] = bool(segment[value - low])
    return result


def validate_record_shape(record: dict[str, Any]) -> tuple[bool, str, int, list[int], list[int]]:
    """只校验证书形状与行列位置，同时返回实际见证值。"""
    P, rows, cols = record_values(record)
    if len(rows) != P:
        return False, f"P={P} 行见证数量错误", P, rows, cols
    if len(cols) != P - 1:
        return False, f"P={P} 列见证数量错误", P, rows, cols
    for row, value in enumerate(rows, start=1):
        if not ((row - 1) * P + 1 <= value <= row * P):
            return False, f"P={P} 第 {row} 行见证越界: {value}", P, rows, cols
    for col, value in enumerate(cols, start=1):
        if value % P != col % P or not (1 <= value <= P * P):
            return False, f"P={P} 第 {col} 列见证越界: {value}", P, rows, cols
    return True, f"P={P} OK", P, rows, cols


def block_ranges(min_p: int, max_p: int, block_size: int) -> Iterable[tuple[int, int]]:
    """生成闭区间分块。"""
    start = min_p
    while start <= max_p:
        end = min(max_p, start + block_size - 1)
        yield start, end
        start = end + 1


def row_witness_offset(P: int, row: int, prime_table: bytearray) -> int | None:
    """返回第 row 行的首个素数偏移，范围 0..P-1。"""
    start = (row - 1) * P + 1
    for offset in range(P):
        if prime_table[start + offset]:
            return offset
    return None


def col_witness_row(P: int, col: int, prime_table: bytearray) -> int | None:
    """返回第 col 列的首个素数所在行号，范围 1..P。"""
    for row in range(1, P + 1):
        value = (row - 1) * P + col
        if prime_table[value]:
            return row
    return None


def segmented_sieve_interval(low: int, high: int, base_primes: list[int]) -> bytearray:
    """返回闭区间 [low, high] 的分段素性表。"""
    segment = bytearray(b"\x01") * (high - low + 1)
    if low == 0:
        segment[0:2] = b"\x00\x00"
    elif low == 1:
        segment[0] = 0
    for prime in base_primes:
        square = prime * prime
        if square > high:
            break
        first = max(square, ((low + prime - 1) // prime) * prime)
        segment[first - low : high - low + 1 : prime] = b"\x00" * (((high - first) // prime) + 1)
    return segment


def generate_record_segmented(P: int, compact: bool, segment_size: int) -> dict[str, Any]:
    """用分段筛生成单个 P 的见证记录，避免整表筛到 P^2。"""
    base_primes = primes_up_to(P)
    row_offsets: list[int | None] = [None] * P
    col_rows: list[int | None] = [None] * (P - 1)
    for low in range(1, P * P + 1, segment_size):
        high = min(P * P, low + segment_size - 1)
        segment = segmented_sieve_interval(low, high, base_primes)
        for index, flag in enumerate(segment):
            if not flag:
                continue
            value = low + index
            row = (value - 1) // P + 1
            col = (value - 1) % P + 1
            if row_offsets[row - 1] is None:
                row_offsets[row - 1] = col - 1
            if col < P and col_rows[col - 1] is None:
                col_rows[col - 1] = row
        if all(offset is not None for offset in row_offsets) and all(row is not None for row in col_rows):
            break
    missing_row = next((i + 1 for i, offset in enumerate(row_offsets) if offset is None), None)
    if missing_row is not None:
        raise RuntimeError(f"P={P} 第 {missing_row} 行无素数")
    missing_col = next((i + 1 for i, row in enumerate(col_rows) if row is None), None)
    if missing_col is not None:
        raise RuntimeError(f"P={P} 第 {missing_col} 列无素数")
    if compact:
        return {"P": P, "format": "offset-v1", "row_offsets": row_offsets, "col_rows": col_rows}
    rows = [(row - 1) * P + 1 + int(offset) for row, offset in enumerate(row_offsets, start=1)]
    cols = [(int(witness_row) - 1) * P + col for col, witness_row in enumerate(col_rows, start=1)]
    return {"P": P, "row_witnesses": rows, "col_witnesses": cols}


def generate_record(P: int, prime_table: bytearray, compact: bool) -> dict[str, Any]:
    """生成单个 P 的行列见证记录；compact=True 时存偏移/行号。"""
    rows = []
    cols = []
    for row in range(1, P + 1):
        offset = row_witness_offset(P, row, prime_table)
        if offset is None:
            raise RuntimeError(f"P={P} 第 {row} 行无素数")
        rows.append(offset if compact else (row - 1) * P + 1 + offset)
    for col in range(1, P):
        row = col_witness_row(P, col, prime_table)
        if row is None:
            raise RuntimeError(f"P={P} 第 {col} 列无素数")
        cols.append(row if compact else (row - 1) * P + col)
    if compact:
        return {"P": P, "format": "offset-v1", "row_offsets": rows, "col_rows": cols}
    return {"P": P, "row_witnesses": rows, "col_witnesses": cols}


def is_prime_trial(n: int) -> bool:
    """用试除校验证书中的见证素性。"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    d = 3
    limit = isqrt(n)
    while d <= limit:
        if n % d == 0:
            return False
        d += 2
    return True


def check_record(record: dict[str, Any]) -> tuple[bool, str]:
    """校验单条 P 记录；兼容完整见证和 offset-v1 紧凑格式。"""
    P = int(record["P"])
    if record.get("format") == "offset-v1":
        rows = record.get("row_offsets", [])
        cols = record.get("col_rows", [])
        if len(rows) != P:
            return False, f"P={P} 行偏移数量错误"
        if len(cols) != P - 1:
            return False, f"P={P} 列行号数量错误"
        for row, offset in enumerate(rows, start=1):
            if not (0 <= int(offset) < P):
                return False, f"P={P} 第 {row} 行偏移越界: {offset}"
            value = (row - 1) * P + 1 + int(offset)
            if not is_prime_trial(value):
                return False, f"P={P} 第 {row} 行见证非素数: {value}"
        for col, witness_row in enumerate(cols, start=1):
            if not (1 <= int(witness_row) <= P):
                return False, f"P={P} 第 {col} 列行号越界: {witness_row}"
            value = (int(witness_row) - 1) * P + col
            if not is_prime_trial(value):
                return False, f"P={P} 第 {col} 列见证非素数: {value}"
        return True, f"P={P} OK"

    rows = record.get("row_witnesses", [])
    cols = record.get("col_witnesses", [])
    if len(rows) != P:
        return False, f"P={P} 行见证数量错误"
    if len(cols) != P - 1:
        return False, f"P={P} 列见证数量错误"
    for row, value in enumerate(rows, start=1):
        if not ((row - 1) * P + 1 <= value <= row * P):
            return False, f"P={P} 第 {row} 行见证越界: {value}"
        if not is_prime_trial(value):
            return False, f"P={P} 第 {row} 行见证非素数: {value}"
    for col, value in enumerate(cols, start=1):
        if value % P != col % P or not (1 <= value <= P * P):
            return False, f"P={P} 第 {col} 列见证越界: {value}"
        if not is_prime_trial(value):
            return False, f"P={P} 第 {col} 列见证非素数: {value}"
    return True, f"P={P} OK"


def open_text(path: Path, mode: str):
    """按后缀打开普通文本或 gzip 文本。"""
    if path.suffix == ".gz":
        return gzip.open(path, mode + "t", encoding="utf-8")
    return path.open(mode, encoding="utf-8")


def generate_blocks(min_p: int, max_p: int, block_size: int, output_dir: Path, overwrite: bool, compact: bool, gzip_output: bool, prime_mode: str, segment_size: int) -> None:
    """按区间生成 JSONL 证书块。"""
    output_dir.mkdir(parents=True, exist_ok=True)
    all_primes = [p for p in primes_up_to(max_p) if p % 2 == 1 and p >= min_p]
    for start, end in block_ranges(min_p, max_p, block_size):
        suffix = ".jsonl.gz" if gzip_output else ".jsonl"
        block_path = output_dir / f"grid_cert_P{start}_{end}{suffix}"
        if block_path.exists() and not overwrite:
            print(f"跳过已存在块: {block_path}")
            continue
        ps = [p for p in all_primes if start <= p <= end]
        if not ps:
            block_path.write_text("")
            print(f"空块: {block_path}")
            continue
        prime_table = sieve(ps[-1] * ps[-1]) if prime_mode == "sieve" else None
        with open_text(block_path, "w") as handle:
            header = {"type": "finite_grid_prime_witness_block", "min_p": start, "max_p": end, "prime_count": len(ps), "format": "offset-v1" if compact else "full-v1", "prime_mode": prime_mode}
            handle.write(json.dumps(header, ensure_ascii=False) + "\n")
            for P in ps:
                if prime_mode == "segmented":
                    record = generate_record_segmented(P, compact, segment_size)
                else:
                    record = generate_record(P, prime_table, compact)
                handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
        print(f"生成块: {block_path}，P 数量={len(ps)}")


def record_values(record: dict[str, Any]) -> tuple[int, list[int], list[int]]:
    """把证书记录转为实际行/列见证值，供块级筛表快速校验。"""
    P = int(record["P"])
    if record.get("format") == "offset-v1":
        rows = [(row - 1) * P + 1 + int(offset) for row, offset in enumerate(record.get("row_offsets", []), start=1)]
        cols = [(int(witness_row) - 1) * P + col for col, witness_row in enumerate(record.get("col_rows", []), start=1)]
    else:
        rows = [int(v) for v in record.get("row_witnesses", [])]
        cols = [int(v) for v in record.get("col_witnesses", [])]
    return P, rows, cols


def check_record_fast(record: dict[str, Any], prime_table: bytearray) -> tuple[bool, str]:
    """用块级筛表快速校验单条记录。"""
    P, rows, cols = record_values(record)
    if len(rows) != P:
        return False, f"P={P} 行见证数量错误"
    if len(cols) != P - 1:
        return False, f"P={P} 列见证数量错误"
    for row, value in enumerate(rows, start=1):
        if not ((row - 1) * P + 1 <= value <= row * P):
            return False, f"P={P} 第 {row} 行见证越界: {value}"
        if not prime_table[value]:
            return False, f"P={P} 第 {row} 行见证非素数: {value}"
    for col, value in enumerate(cols, start=1):
        if value % P != col % P or not (1 <= value <= P * P):
            return False, f"P={P} 第 {col} 列见证越界: {value}"
        if not prime_table[value]:
            return False, f"P={P} 第 {col} 列见证非素数: {value}"
    return True, f"P={P} OK"


def check_blocks(input_dir: Path, mode: str, segment_size: int) -> None:
    """校验目录内所有 JSONL 证书块。"""
    files = sorted(input_dir.glob("grid_cert_P*_*.jsonl")) + sorted(input_dir.glob("grid_cert_P*_*.jsonl.gz"))
    if not files:
        raise SystemExit(f"未找到证书块: {input_dir}")
    total = 0
    for path in files:
        with open_text(path, "r") as handle:
            header_line = handle.readline()
            if not header_line:
                print(f"空块通过: {path}")
                continue
            header = json.loads(header_line)
            if header.get("type") != "finite_grid_prime_witness_block":
                raise SystemExit(f"块头错误: {path}")
            records = [json.loads(line) for line in handle]
        if not records:
            print(f"空块通过: {path}")
            continue
        prime_table = None
        if mode == "sieve":
            max_p = max(int(item["P"]) for item in records)
            prime_table = sieve(max_p * max_p)
            for record in records:
                ok, message = check_record_fast(record, prime_table)
                if not ok:
                    raise SystemExit(f"{path}: {message}")
        elif mode == "trial":
            for record in records:
                # 试除模式更慢，但不需要为每块筛到 max(P)^2，适合大 P 低内存抽检。
                ok, message = check_record(record)
                if not ok:
                    raise SystemExit(f"{path}: {message}")
        else:
            witness_values: set[int] = set()
            max_p = max(int(item["P"]) for item in records)
            for record in records:
                ok, message, _P, rows, cols = validate_record_shape(record)
                if not ok:
                    raise SystemExit(f"{path}: {message}")
                witness_values.update(rows)
                witness_values.update(cols)
            base_primes = primes_up_to(max_p)
            prime_flags = segmented_prime_flags(list(witness_values), base_primes, segment_size)
            for record in records:
                P, rows, cols = record_values(record)
                for row, value in enumerate(rows, start=1):
                    if not prime_flags.get(value, False):
                        raise SystemExit(f"{path}: P={P} 第 {row} 行见证非素数: {value}")
                for col, value in enumerate(cols, start=1):
                    if not prime_flags.get(value, False):
                        raise SystemExit(f"{path}: P={P} 第 {col} 列见证非素数: {value}")
        count = len(records)
        if count != int(header.get("prime_count", count)):
            raise SystemExit(f"{path}: 记录数与头部不一致")
        total += count
        print(f"校验通过: {path}，P 数量={count}")
    print(f"SUMMARY: 证书块全部通过，奇素数 P 总数={total}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    gen = sub.add_parser("generate")
    gen.add_argument("--min-p", type=int, default=3)
    gen.add_argument("--max-p", type=int, required=True)
    gen.add_argument("--block-size", type=int, default=1000)
    gen.add_argument("--output-dir", type=Path, required=True)
    gen.add_argument("--overwrite", action="store_true")
    gen.add_argument("--compact", action="store_true", help="使用 offset-v1 紧凑格式保存见证")
    gen.add_argument("--gzip", action="store_true", help="输出 .jsonl.gz 压缩证书块")
    gen.add_argument("--prime-mode", choices=("sieve", "segmented"), default="sieve", help="生成模式：sieve 快但占内存，segmented 低内存")
    gen.add_argument("--segment-size", type=int, default=8_000_000, help="segmented 模式的筛窗口长度")
    chk = sub.add_parser("check")
    chk.add_argument("--input-dir", type=Path, required=True)
    chk.add_argument("--mode", choices=("sieve", "segmented", "trial"), default="sieve", help="校验模式：sieve 快但占内存，segmented 平衡速度和内存，trial 慢但低内存")
    chk.add_argument("--segment-size", type=int, default=8_000_000, help="segmented 模式的筛窗口长度")
    args = parser.parse_args()

    if args.cmd == "generate":
        generate_blocks(args.min_p, args.max_p, args.block_size, args.output_dir, args.overwrite, args.compact, args.gzip, args.prime_mode, args.segment_size)
    else:
        check_blocks(args.input_dir, args.mode, args.segment_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
