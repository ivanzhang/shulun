#!/usr/bin/env python3
"""续跑 strict 中段 psi 增量节点表的单个区块。

用法示例：
  python3 experiments/prime_matrix_middle_psi_resume_block_runner.py \
    --table data/middle-psi-fine-mesh-node-table.jsonl \
    --block-intervals 5000

脚本只追加一个区块：读取表中最后一个节点，将 C++ runner 从该节点继续，
先写入临时文件并做连续性/余量验收，通过后再追加到正式表。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


X_LEFT = 800_000_000_000
MESH_H = 1_000_000
EXPECTED_NODE_COUNT = 646_258
SOURCE_COMMIT = "21f4f6553851f218801a733f607426c3dba9ba11"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_last_record(path: Path) -> dict[str, Any]:
    """读取 JSONL 表的最后一条非空记录。"""
    last = ""
    with path.open("rb") as handle:
      handle.seek(0, 2)
      size = handle.tell()
      if size == 0:
          raise ValueError("table is empty; seed run must create the first node")
      block = 4096
      data = b""
      position = size
      while position > 0 and b"\n" not in data.rstrip(b"\n"):
          step = min(block, position)
          position -= step
          handle.seek(position)
          data = handle.read(step) + data
      lines = [line for line in data.splitlines() if line.strip()]
      if not lines:
          raise ValueError("table has no JSONL records")
      last = lines[-1].decode("utf-8")
    return json.loads(last)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    """读取临时区块 JSONL。"""
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def expected_x(index: int) -> int:
    """返回百万网格第 index 个节点的 x 值。"""
    return X_LEFT + index * MESH_H


def validate_block(rows: list[dict[str, Any]], previous: dict[str, Any], expected_rows: int) -> dict[str, Any]:
    """验收临时区块的连续性、x_i 和余量。"""
    getcontext().prec = 50
    if len(rows) != expected_rows:
        raise ValueError(f"block row count {len(rows)} != expected {expected_rows}")
    first_i = int(previous["i"]) + 1
    min_slack: Decimal | None = None
    min_slack_i: int | None = None
    for offset, row in enumerate(rows):
        i = int(row["i"])
        if i != first_i + offset:
            raise ValueError(f"non-contiguous block index {i}, expected {first_i + offset}")
        if int(row["x_i"]) != expected_x(i):
            raise ValueError(f"x_i mismatch at i={i}")
        if not row.get("slack_ge_required_floor"):
            raise ValueError(f"slack gate failed at i={i}")
        slack = Decimal(str(row["slack_lower_bound"]))
        if min_slack is None or slack < min_slack:
            min_slack = slack
            min_slack_i = i
    return {
        "first_i": rows[0]["i"],
        "last_i": rows[-1]["i"],
        "first_x_i": rows[0]["x_i"],
        "last_x_i": rows[-1]["x_i"],
        "min_slack": str(min_slack),
        "min_slack_i": min_slack_i,
        "last_psi_estimate": rows[-1]["psi_estimate"],
        "last_cumulative_delta_term_count": rows[-1]["cumulative_delta_term_count"],
    }


def append_file(target: Path, source: Path) -> None:
    """将临时区块追加到正式表。"""
    with target.open("ab") as out, source.open("rb") as inp:
        out.write(inp.read())


def run_block(args: argparse.Namespace) -> dict[str, Any]:
    """运行并追加一个续跑区块。"""
    table = args.table
    previous = read_last_record(table)
    previous_i = int(previous["i"])
    remaining_intervals = EXPECTED_NODE_COUNT - 1 - previous_i
    intervals = min(args.block_intervals, remaining_intervals)
    if intervals <= 0:
        return {
            "status": "already_complete",
            "table": str(table),
            "last_i": previous_i,
            "expected_last_i": EXPECTED_NODE_COUNT - 1,
        }

    tmp = args.tmp_dir / f"middle-psi-resume-block-{previous_i + 1}-{previous_i + intervals}.jsonl"
    if tmp.exists():
        tmp.unlink()

    cmd = [
        str(args.exe),
        str(previous_i),
        str(intervals + 1),
        str(previous["psi_estimate"]),
        SOURCE_COMMIT,
        str(intervals),
        str(previous["cumulative_delta_term_count"]),
        "0",
    ]
    started = time.time()
    with tmp.open("wb") as handle:
        completed = subprocess.run(cmd, stdout=handle, stderr=subprocess.PIPE, text=False, check=False)
    elapsed = time.time() - started
    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace").strip().splitlines()[-5:]
        raise RuntimeError(f"runner failed: {' | '.join(stderr)}")

    rows = load_jsonl(tmp)
    profile = validate_block(rows, previous, intervals)
    append_file(table, tmp)
    total_rows_after = previous_i + 1 + intervals

    return {
        "status": "appended",
        "table": str(table),
        "tmp_block": str(tmp),
        "tmp_block_sha256": sha256(tmp),
        "elapsed_seconds": round(elapsed, 3),
        "previous_last_i": previous_i,
        "appended_rows": intervals,
        "total_rows_after": total_rows_after,
        "completion_fraction": total_rows_after / EXPECTED_NODE_COUNT,
        **profile,
    }


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--table", type=Path, required=True, help="待续跑追加的 JSONL 表")
    parser.add_argument("--block-intervals", type=int, default=5000, help="每次追加的百万区间数")
    parser.add_argument("--exe", type=Path, default=Path("/tmp/middle_psi_segmented_delta"), help="C++ runner 路径")
    parser.add_argument("--tmp-dir", type=Path, default=Path("/tmp"), help="临时区块目录")
    args = parser.parse_args()

    result = run_block(args)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
