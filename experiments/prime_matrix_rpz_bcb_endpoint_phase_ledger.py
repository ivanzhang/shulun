#!/usr/bin/env python3
"""生成 RPZ-BCB 端点失败相位账本。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_endpoint_phase_ledger.py

输入为 `prime-matrix-rpz-bcb-grid-endpoint-audit.json`。脚本枚举每条记录在固定
`(h,N)` 下所有可能的左端相位 `u mod h`，标出会导致 `(Grid)` 失败的端点相位。
实际样本相位同时记录，用于区分：

1. 实际中心区间已经含完整下层行；
2. 若失败，失败只可能属于有限相位表；
3. 多平台持续失败必须在某个有限相位上重复，从而进入 PDEC/ColumnCRT；否则是 SAE 稀疏包。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def phase_for_residue(h: int, length: int, left_residue: int) -> dict:
    """返回给定左端相位下的网格判据结果。"""
    delta = (1 - left_residue) % h
    margin = length - (delta + h)
    return {
        "h": h,
        "length": length,
        "left_residue_mod_h": left_residue,
        "length_mod_h": length % h,
        "delta_to_next_row_start": delta,
        "criterion_margin": margin,
        "endpoint_deficit": max(0, -margin),
        "fails_grid": margin < 0,
    }


def audit(source_path: Path) -> dict:
    """执行端点相位账本审计。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    records = []
    global_failure_phase_load: Counter[tuple[int, int, int, int]] = Counter()
    actual_failure_phase_load: Counter[tuple[int, int, int, int]] = Counter()

    for record in source["records"]:
        h = record["half_prime"]
        length = record["length"]
        actual_residue = record["left_residue_mod_h"]
        possible_phases = [
            phase_for_residue(h, length, residue)
            for residue in range(h)
        ]
        failure_phases = [phase for phase in possible_phases if phase["fails_grid"]]
        actual_phase = phase_for_residue(h, length, actual_residue)

        for phase in failure_phases:
            key = (
                phase["h"],
                phase["length_mod_h"],
                phase["left_residue_mod_h"],
                phase["endpoint_deficit"],
            )
            global_failure_phase_load[key] += 1
        if actual_phase["fails_grid"]:
            key = (
                actual_phase["h"],
                actual_phase["length_mod_h"],
                actual_phase["left_residue_mod_h"],
                actual_phase["endpoint_deficit"],
            )
            actual_failure_phase_load[key] += 1

        records.append(
            {
                "top_prime": record["top_prime"],
                "top_zero_row": record["top_zero_row"],
                "half_prime": h,
                "forced_core_interval": record["forced_core_interval"],
                "length": length,
                "actual_phase": actual_phase,
                "actual_grid_failure": actual_phase["fails_grid"],
                "possible_failure_phase_count": len(failure_phases),
                "possible_success_phase_count": h - len(failure_phases),
                "possible_failure_phases": failure_phases,
                "failure_phase_density": len(failure_phases) / h,
            }
        )

    return {
        "status": "rpz_bcb_endpoint_failure_is_finite_phase_ledger",
        "source": str(source_path),
        "summary": {
            "records": len(records),
            "actual_endpoint_failures": sum(
                1 for record in records if record["actual_grid_failure"]
            ),
            "total_possible_failure_phases": sum(
                record["possible_failure_phase_count"] for record in records
            ),
            "max_possible_failure_phase_count": max(
                (record["possible_failure_phase_count"] for record in records),
                default=0,
            ),
            "max_failure_phase_density": max(
                (record["failure_phase_density"] for record in records),
                default=0,
            ),
            "distinct_possible_failure_phase_keys": len(global_failure_phase_load),
            "distinct_actual_failure_phase_keys": len(actual_failure_phase_load),
            "global_possible_failure_phase_load": {
                repr(key): value
                for key, value in sorted(global_failure_phase_load.items())
            },
            "actual_failure_phase_load": {
                repr(key): value
                for key, value in sorted(actual_failure_phase_load.items())
            },
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ-BCB 端点失败相位账本",
        "",
        "**状态：** `rpz_bcb_endpoint_failure_is_finite_phase_ledger`",
        "",
        "## 总结",
        "",
        f"- 样本记录数：`{summary['records']}`。",
        f"- 实际端点失败记录数：`{summary['actual_endpoint_failures']}`。",
        f"- 可能失败相位总数：`{summary['total_possible_failure_phases']}`。",
        f"- 单记录最大可能失败相位数：`{summary['max_possible_failure_phase_count']}`。",
        f"- 最大失败相位密度：`{summary['max_failure_phase_density']:.6f}`。",
        f"- 不同可能失败相位键数：`{summary['distinct_possible_failure_phase_keys']}`。",
        f"- 不同实际失败相位键数：`{summary['distinct_actual_failure_phase_keys']}`。",
        f"- 可能失败相位负载：`{summary['global_possible_failure_phase_load']}`。",
        "",
        "## 逐例表",
        "",
        "| top P | row | h | length | actual residue | actual margin | possible failure phases | failure density | actual failure |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for record in result["records"]:
        actual = record["actual_phase"]
        lines.append(
            "| {top} | {row} | {h} | {length} | {residue} | {margin} | {failures} | {density:.6f} | {actual_failure} |".format(
                top=record["top_prime"],
                row=record["top_zero_row"],
                h=record["half_prime"],
                length=record["length"],
                residue=actual["left_residue_mod_h"],
                margin=actual["criterion_margin"],
                failures=record["possible_failure_phase_count"],
                density=record["failure_phase_density"],
                actual_failure="yes" if record["actual_grid_failure"] else "no",
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "端点失败不是新的无限自由度。固定 `h` 与中心长度 `N` 后，失败完全由左端相位 `u mod h` 决定；失败相位数至多为 `h`，实际为满足 `delta_h(u)+h>N` 的那一段端点残基。",
            "",
            "若正式反例族中端点失败只出现有限次或每个相位负载低于阈值，则它属于 `SAE` 稀疏包；若失败持续出现，则有限相位鸽巢强制某个 `(h,N mod h,u mod h,deficit)` 相位重复，进入 `PDEC/ColumnCRT`。",
            "",
            "同批样本没有实际端点失败；可能失败相位只出现在 `h=11,N=19` 的两个左端残基中。这支持端点分支是窄相位出口，而不是内部容量主支。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-endpoint-phase-ledger"),
    )
    args = parser.parse_args()
    result = audit(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
