#!/usr/bin/env python3
"""从 Terminal-RCI 抵消审计中剥离 h=q 镜像边界块。

用法示例：
  python3 experiments/prime_matrix_terminal_rci_boundary_split_audit.py \
    --input docs/terminal_sae_cancellation_audit_p2000_20260505.json

h=q 时 n 区间为 [1,q]。在 y^2>q 后，低筛骨架只剩尾素数和 q；
尾素数单尾抵消，q 提供唯一无尾储备，所以该块余量恒为 1。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def summarize(path: Path, thresholds: list[int]) -> dict:
    """读取审计 JSON 并生成边界/非底块摘要。"""
    package = json.loads(path.read_text(encoding="utf-8"))
    records = package["records"]
    threshold_rows = []
    for threshold in thresholds:
        scoped = [record for record in records if record["p"] >= threshold]
        if not scoped:
            continue
        min_all = min(record["min_margin"] for record in scoped)
        min_nonbottom = min(record["min_margin_nonbottom"] for record in scoped)
        worst_all = next(record for record in scoped if record["min_margin"] == min_all)
        worst_nonbottom = next(
            record
            for record in scoped
            if record["min_margin_nonbottom"] == min_nonbottom
        )
        threshold_rows.append(
            {
                "p_threshold": threshold,
                "min_all": min_all,
                "min_all_at": {
                    "p": worst_all["p"],
                    "q": worst_all["q_next"],
                    "h": worst_all["min_data"]["h"],
                    "interval": worst_all["min_data"]["n_interval"],
                    "no_tail": worst_all["min_data"]["no_tail_reserve"],
                    "multi_excess": worst_all["min_data"]["multi_tail_excess"],
                },
                "min_nonbottom": min_nonbottom,
                "min_nonbottom_at": {
                    "p": worst_nonbottom["p"],
                    "q": worst_nonbottom["q_next"],
                    "h": worst_nonbottom["min_data_nonbottom"]["h"],
                    "interval": worst_nonbottom["min_data_nonbottom"]["n_interval"],
                    "no_tail": worst_nonbottom["min_data_nonbottom"][
                        "no_tail_reserve"
                    ],
                    "multi_excess": worst_nonbottom["min_data_nonbottom"][
                        "multi_tail_excess"
                    ],
                },
            }
        )
    boundary_min_records = [
        record
        for record in records
        if record["min_data"]["h"] == record["q_next"]
    ]
    return {
        "input": str(path),
        "status": "terminal_rci_boundary_block_split_not_a_proof",
        "record_count": len(records),
        "boundary_min_record_count": len(boundary_min_records),
        "boundary_min_fraction": (
            len(boundary_min_records) / len(records) if records else None
        ),
        "threshold_rows": threshold_rows,
    }


def print_table(package: dict) -> None:
    """输出简表。"""
    print(
        "records boundary_min boundary_fraction threshold min_all all_at "
        "min_nonbottom nonbottom_at",
        flush=True,
    )
    for row in package["threshold_rows"]:
        print(
            f"{package['record_count']} {package['boundary_min_record_count']} "
            f"{package['boundary_min_fraction']:.6f} {row['p_threshold']} "
            f"{row['min_all']} {row['min_all_at']} "
            f"{row['min_nonbottom']} {row['min_nonbottom_at']}",
            flush=True,
        )


def parse_thresholds(raw: str) -> list[int]:
    """解析阈值列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/terminal_sae_cancellation_audit_p2000_20260505.json",
    )
    parser.add_argument(
        "--thresholds",
        default="7,11,23,29,47,101,251,501,1009,1500",
    )
    parser.add_argument("--format", choices=("json", "table"), default="table")
    args = parser.parse_args()
    package = summarize(Path(args.input), parse_thresholds(args.thresholds))
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    print_table(package)


if __name__ == "__main__":
    main()
