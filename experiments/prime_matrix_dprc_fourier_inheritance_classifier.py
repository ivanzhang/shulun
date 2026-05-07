#!/usr/bin/env python3
"""分类 DPRC 层叠轮 Fourier 频率的继承/新层显化。

用法示例：
  python3 experiments/prime_matrix_dprc_fourier_inheritance_classifier.py \
    --input docs/dprc_layered_wheel_fourier_audit_20260506.json \
    --out-prefix docs/dprc_fourier_inheritance_classifier_20260506

目标：
  读取 layered wheel Fourier 审计结果，判断每个最强频率的 period
  是否已经从上一层轮继承；若没有继承，则记录新增素因子层。
  这用于区分“低模旧相位残留”和“新轮层 PDEC 证书候选”。
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path


L1_DANGER = 12.0 / 5.0
L2_CAUCHY = 3.0 / math.sqrt(6.0)


def prime_factors(value: int) -> list[int]:
    """返回 value 的不同素因子。"""
    factors: list[int] = []
    divisor = 2
    current = value
    while divisor * divisor <= current:
        if current % divisor == 0:
            factors.append(divisor)
            while current % divisor == 0:
                current //= divisor
        divisor += 1 if divisor == 2 else 2
    if current > 1:
        factors.append(current)
    return factors


def classify_frequency(period: int, previous_wheel: int | None) -> dict:
    """判断 period 是否从 previous_wheel 继承。"""
    if previous_wheel is None:
        return {
            "class": "base",
            "previous_wheel": None,
            "new_part": period,
            "new_prime_factors": prime_factors(period),
            "inherited": False,
        }

    inherited = previous_wheel % period == 0
    common = math.gcd(period, previous_wheel)
    new_part = period // common
    return {
        "class": "inherited" if inherited else "new-layer",
        "previous_wheel": previous_wheel,
        "new_part": new_part,
        "new_prime_factors": prime_factors(new_part),
        "inherited": inherited,
    }


def classify_record(record: dict, wheel_order: list[int]) -> dict:
    """分类单条 P/side 记录。"""
    row_by_wheel = {row["wheel"]: row for row in record["wheels"]}
    classified = []
    previous_wheel: int | None = None
    for wheel in wheel_order:
        row = row_by_wheel[wheel]
        top = row["max_fourier_frequency"]
        classification = classify_frequency(top["period"], previous_wheel)
        classified.append(
            {
                "wheel": wheel,
                "period": top["period"],
                "h": top["h"],
                "gcd_h_w": top["gcd_h_w"],
                "max_fourier_abs_over_sqrt": row[
                    "max_fourier_abs_over_sqrt"
                ],
                "centered_top_over_sqrt": row["centered_top_over_sqrt"],
                "centered_l2_over_sqrt": row["centered_l2_over_sqrt"],
                **classification,
            }
        )
        previous_wheel = wheel
    return {
        "p": record["p"],
        "side": record["side"],
        "skeleton_count": record["skeleton_count"],
        "positive_bucket_l1_over_sqrt": record[
            "positive_bucket_l1_over_sqrt"
        ],
        "positive_bucket_l2_over_sqrt": record[
            "positive_bucket_l2_over_sqrt"
        ],
        "high_l1": record["positive_bucket_l1_over_sqrt"] >= L1_DANGER,
        "high_l2_cauchy": record["positive_bucket_l2_over_sqrt"] > L2_CAUCHY,
        "wheels": classified,
    }


def summarize(classified_records: list[dict], wheel_order: list[int]) -> dict:
    """汇总继承/新层显化比例。"""
    wheel_summaries = []
    for wheel in wheel_order:
        rows = [
            wheel_row
            for record in classified_records
            for wheel_row in record["wheels"]
            if wheel_row["wheel"] == wheel
        ]
        class_hist = Counter(row["class"] for row in rows)
        period_hist = Counter(row["period"] for row in rows)
        new_factor_hist = Counter(
            tuple(row["new_prime_factors"])
            for row in rows
            if row["class"] == "new-layer"
        )
        wheel_summaries.append(
            {
                "wheel": wheel,
                "class_histogram": dict(class_hist),
                "period_histogram": dict(sorted(period_hist.items())),
                "new_factor_histogram": {
                    ",".join(map(str, key)) if key else "none": value
                    for key, value in sorted(new_factor_hist.items())
                },
                "max_fourier_abs_over_sqrt": max(
                    row["max_fourier_abs_over_sqrt"] for row in rows
                ),
                "max_centered_top_over_sqrt": max(
                    row["centered_top_over_sqrt"] for row in rows
                ),
            }
        )

    high_l1 = [row for row in classified_records if row["high_l1"]]
    high_l2 = [row for row in classified_records if row["high_l2_cauchy"]]
    return {
        "record_count": len(classified_records),
        "high_l1_count": len(high_l1),
        "high_l2_cauchy_count": len(high_l2),
        "danger_intersection_count": len(
            [row for row in classified_records if row["high_l1"] and row["high_l2_cauchy"]]
        ),
        "wheel_summaries": wheel_summaries,
    }


def build_result(input_path: Path, wheel_order: list[int]) -> dict:
    """读取原始审计并生成分类结果。"""
    source = json.loads(input_path.read_text(encoding="utf-8"))
    if not wheel_order:
        wheel_order = source["parameters"]["wheels"]
    records = [classify_record(record, wheel_order) for record in source["records"]]
    return {
        "parameters": {
            "input": str(input_path),
            "wheel_order": wheel_order,
            "l1_danger": L1_DANGER,
            "l2_cauchy": L2_CAUCHY,
        },
        "summary": summarize(records, wheel_order),
        "records": records,
    }


def fmt(value: float) -> str:
    """格式化浮点数。"""
    return f"{value:.6f}"


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# DPRC Fourier 频率继承分类审计",
        "",
        "**状态：** `classification_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `input`: `{params['input']}`",
        f"- `wheel_order`: `{params['wheel_order']}`",
        f"- `L1 danger`: `{params['l1_danger']:.6f}`",
        f"- `L2 Cauchy`: `{params['l2_cauchy']:.6f}`",
        "",
        "## 总览",
        "",
        f"- `records`: `{summary['record_count']}`",
        f"- `high L1 records`: `{summary['high_l1_count']}`",
        f"- `high L2(Cauchy) records`: `{summary['high_l2_cauchy_count']}`",
        f"- `danger intersection`: `{summary['danger_intersection_count']}`",
        "",
        "| W | class histogram | period histogram | new factors | max Fourier/sqrt | max centered peak/sqrt |",
        "|---:|---|---|---|---:|---:|",
    ]
    for row in summary["wheel_summaries"]:
        lines.append(
            f"| {row['wheel']} | `{row['class_histogram']}` | "
            f"`{row['period_histogram']}` | `{row['new_factor_histogram']}` | "
            f"{fmt(row['max_fourier_abs_over_sqrt'])} | "
            f"{fmt(row['max_centered_top_over_sqrt'])} |"
        )

    lines.extend(
        [
            "",
            "## 逐记录分类",
            "",
            "| P | side | BES L1 | BES L2 | W | period | class | new part | new factors | max Fourier/sqrt | centered peak/sqrt |",
            "|---:|---|---:|---:|---:|---:|---|---:|---|---:|---:|",
        ]
    )
    for record in result["records"]:
        for row in record["wheels"]:
            lines.append(
                f"| {record['p']} | {record['side']} | "
                f"{fmt(record['positive_bucket_l1_over_sqrt'])} | "
                f"{fmt(record['positive_bucket_l2_over_sqrt'])} | "
                f"{row['wheel']} | {row['period']} | `{row['class']}` | "
                f"{row['new_part']} | `{row['new_prime_factors']}` | "
                f"{fmt(row['max_fourier_abs_over_sqrt'])} | "
                f"{fmt(row['centered_top_over_sqrt'])} |"
            )

    lines.extend(
        [
            "",
            "## 结构读法",
            "",
            "若 `period` 整除上一层轮，则当前最强频率只是旧层相位的提升；否则它必须使用新增素因子层，属于 `new-layer`。因此 `new-layer` 不是随机噪声标签，而是一个可物化的低模 PDEC 候选方向。",
            "",
            "本次代表样本显示：`W=2310` 的最强频率全部不从 `W=210` 继承，而是都带有新增因子 `11`。这说明升到 `2310` 后，单单位类峰已被稀释，但 Fourier 能量转入新层振荡方向。",
            "",
            "对高 `BES L1` 样本，`W=2310` 的 centered peak 很小而 max Fourier 较大；这支持当前二分：若这种新层振荡持续同步，则进入 `W-unit PDEC`；若不同步，则剩余能量只能走高模分散大筛出口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_wheels(raw: str) -> list[int]:
    """解析轮层列表。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/dprc_layered_wheel_fourier_audit_20260506.json",
    )
    parser.add_argument("--wheel-order", default="")
    parser.add_argument(
        "--out-prefix",
        default="docs/dprc_fourier_inheritance_classifier_20260506",
    )
    args = parser.parse_args()

    result = build_result(Path(args.input), parse_wheels(args.wheel_order))
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
