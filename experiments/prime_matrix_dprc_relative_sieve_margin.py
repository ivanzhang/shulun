#!/usr/bin/env python3
"""分析 DPRC 动态提升轮的一阶容量余量分解。

用法示例：
  python3 experiments/prime_matrix_dprc_relative_sieve_margin.py \
    --input docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json \
    --out-prefix docs/dprc_relative_sieve_margin_alpha043_p100000_20260506

恒等式：
  S - T = S*(1-H) - (T-H*S)，其中
    S = 动态粗骨架大小；
    T = 剩余高素总命中；
    H = sum_{Y<q<P} 1/q。

因此只要正偏差 D_+=max(0,T-H*S) 小于模型余量 S*(1-H)，
就得到 T<S。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def enrich(record: dict) -> dict:
    """给单条 DPRC 记录补充相对筛余量字段。"""
    skeleton = record["skeleton_count"]
    total_hits = record["total_hits"]
    harmonic = record["harmonic_high"]
    sqrt_s = math.sqrt(skeleton) if skeleton > 0 else 0.0
    model_gap = skeleton * (1.0 - harmonic)
    discrepancy = total_hits - skeleton * harmonic
    positive_discrepancy = max(0.0, discrepancy)
    return {
        **record,
        "sqrt_skeleton": sqrt_s,
        "model_gap": model_gap,
        "discrepancy": discrepancy,
        "positive_discrepancy": positive_discrepancy,
        "model_gap_over_sqrt": model_gap / sqrt_s if sqrt_s else 0.0,
        "discrepancy_over_sqrt": discrepancy / sqrt_s if sqrt_s else 0.0,
        "positive_discrepancy_over_sqrt": positive_discrepancy / sqrt_s
        if sqrt_s
        else 0.0,
        "slack_over_sqrt": (skeleton - total_hits) / sqrt_s if sqrt_s else 0.0,
    }


def summarize(records: list[dict], threshold_p: int, c_value: float) -> dict:
    """汇总某个 P 下界以上的记录。"""
    rows = [enrich(record) for record in records if record["p"] >= threshold_p]
    if not rows:
        return {"threshold_p": threshold_p, "count": 0}
    c_pass_rows = [
        row
        for row in rows
        if row["positive_discrepancy_over_sqrt"] <= c_value
        and row["model_gap_over_sqrt"] > c_value
    ]
    return {
        "threshold_p": threshold_p,
        "count": len(rows),
        "capacity_fail": sum(not row["capacity_pass"] for row in rows),
        "min_capacity_margin": min(row["capacity_margin"] for row in rows),
        "max_incidence_ratio": max(row["incidence_ratio"] for row in rows),
        "min_model_gap": min(row["model_gap"] for row in rows),
        "max_positive_discrepancy": max(row["positive_discrepancy"] for row in rows),
        "min_model_gap_over_sqrt": min(row["model_gap_over_sqrt"] for row in rows),
        "max_positive_discrepancy_over_sqrt": max(
            row["positive_discrepancy_over_sqrt"] for row in rows
        ),
        "min_slack_over_sqrt": min(row["slack_over_sqrt"] for row in rows),
        "c_value": c_value,
        "c_certificate_pass": len(c_pass_rows) == len(rows),
        "worst_by_margin": sorted(rows, key=lambda row: row["capacity_margin"])[:10],
        "worst_by_model_over_sqrt": sorted(
            rows, key=lambda row: row["model_gap_over_sqrt"]
        )[:10],
        "worst_by_positive_discrepancy_over_sqrt": sorted(
            rows, key=lambda row: -row["positive_discrepancy_over_sqrt"]
        )[:10],
    }


def audit(input_path: Path, c_value: float, thresholds: list[int]) -> dict:
    """读取 DPRC JSON 并生成余量审计。"""
    data = json.loads(input_path.read_text(encoding="utf-8"))
    records = data["records"]
    enriched = [enrich(record) for record in records]
    source_params = data.get("parameters", {})
    source_primes = source_params.get("primes", [])
    source_summary = {
        "prime_count": len(source_primes),
        "prime_min": min(source_primes) if source_primes else None,
        "prime_max": max(source_primes) if source_primes else None,
        "alphas": source_params.get("alphas", []),
    }
    return {
        "parameters": {
            "input": str(input_path),
            "c_value": c_value,
            "thresholds": thresholds,
            "source_summary": source_summary,
        },
        "summaries": [summarize(records, threshold, c_value) for threshold in thresholds],
        "global_worst_by_margin": sorted(
            enriched, key=lambda row: row["capacity_margin"]
        )[:20],
        "global_worst_by_positive_discrepancy": sorted(
            enriched, key=lambda row: -row["positive_discrepancy_over_sqrt"]
        )[:20],
    }


def row_id(row: dict) -> str:
    """格式化记录标识。"""
    return f"P={row['p']}, {row['side']}, cutoff={row['cutoff']}"


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# DPRC 相对筛余量分解",
        "",
        "**状态：** `relative_sieve_margin_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `input`: `{params['input']}`",
        f"- `c_value`: `{params['c_value']}`",
        f"- `thresholds`: `{params['thresholds']}`",
        f"- `source_summary`: `{params['source_summary']}`",
        "",
        "## 恒等式",
        "",
        "\\[",
        "S-T=S(1-H)-(T-HS).",
        "\\]",
        "",
        "其中 `H=sum_{Y<q<P}1/q`。若正偏差 `D_+=max(0,T-HS)` 满足 `D_+<S(1-H)`，则 `T<S`。",
        "",
        "一个可攻充分条件是：",
        "",
        "\\[",
        "D_+\\le C\\sqrt S,\\qquad S(1-H)>C\\sqrt S.",
        "\\]",
        "",
        "## 阈值汇总",
        "",
        "| P threshold | records | cap fail | min margin | max T/S | min model gap | max D+ | min model/sqrt | max D+/sqrt | min slack/sqrt | C-pass |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for summary in result["summaries"]:
        lines.append(
            f"| {summary['threshold_p']} | {summary['count']} | "
            f"{summary.get('capacity_fail', 0)} | "
            f"{summary.get('min_capacity_margin', 0)} | "
            f"{summary.get('max_incidence_ratio', 0):.6f} | "
            f"{summary.get('min_model_gap', 0):.6f} | "
            f"{summary.get('max_positive_discrepancy', 0):.6f} | "
            f"{summary.get('min_model_gap_over_sqrt', 0):.6f} | "
            f"{summary.get('max_positive_discrepancy_over_sqrt', 0):.6f} | "
            f"{summary.get('min_slack_over_sqrt', 0):.6f} | "
            f"{summary.get('c_certificate_pass', False)} |"
        )

    lines.extend(["", "## 全局最小容量余量", ""])
    lines.extend(
        [
            "| record | S | T | margin | H | model gap | D | D+/sqrt |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in result["global_worst_by_margin"][:12]:
        lines.append(
            f"| {row_id(row)} | {row['skeleton_count']} | {row['total_hits']} | "
            f"{row['capacity_margin']} | {row['harmonic_high']:.6f} | "
            f"{row['model_gap']:.6f} | {row['discrepancy']:.6f} | "
            f"{row['positive_discrepancy_over_sqrt']:.6f} |"
        )

    lines.extend(["", "## 最大正偏差记录", ""])
    lines.extend(
        [
            "| record | S | T | margin | H | model gap | D | D+/sqrt |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in result["global_worst_by_positive_discrepancy"][:12]:
        lines.append(
            f"| {row_id(row)} | {row['skeleton_count']} | {row['total_hits']} | "
            f"{row['capacity_margin']} | {row['harmonic_high']:.6f} | "
            f"{row['model_gap']:.6f} | {row['discrepancy']:.6f} | "
            f"{row['positive_discrepancy_over_sqrt']:.6f} |"
        )

    lines.extend(
        [
            "",
            "## 证明接口",
            "",
            "`DPRC(alpha=0.43)` 可拆成两项：先用显式 Mertens/prime harmonic 上界给出 `S(1-H)>C sqrt(S)`；再用同权相对筛或大筛型偏差界证明 `D_+<=C sqrt(S)`。审计显示 `C=3` 对 `P>=2003` 已有余量；`P<2003` 可走有限证书。若任一项失败，失败相位进入 `PDEC/SAE/ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json",
    )
    parser.add_argument("--c-value", type=float, default=3.0)
    parser.add_argument("--thresholds", default="13,2003,10007")
    parser.add_argument(
        "--out-prefix",
        default="docs/dprc_relative_sieve_margin_alpha043_p100000_20260506",
    )
    args = parser.parse_args()
    result = audit(Path(args.input), args.c_value, parse_ints(args.thresholds))
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
