#!/usr/bin/env python3
"""审计 EndpointReciprocal-OSC 的 B-process 主项模型。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_bprocess_model_audit.py \
    --input-json docs/diagonal_postsquare_carry_reciprocal_frequency_audit_p50000_20260505.json \
    --freq 64 \
    --out-prefix docs/diagonal_postsquare_bprocess_model_audit_r64_20260505

该脚本比较真实低频贡献
  -Im sum_r S_r(P)/(pi r sqrt(P))
与驻相主项模型
  -Im sum_{r,n} c_{r,n}(1-e(sqrt(rn)))e(2P sqrt(rn)+kappa)/(pi r)。

输出只用于定位 ERO-Low 的剩余误差，不构成证明。
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

TAU = 2.0 * math.pi


def exp1(value: float) -> complex:
    """计算 e(value)=exp(2*pi*i*value)。"""
    return cmath.exp(1j * TAU * value)


def exact_contribution_over_sqrt(p: int, r: int, y: int) -> float:
    """计算单个频率的真实贡献并除以 sqrt(P)。"""
    weighted_sum = 0j
    for a in range(y + 1, p):
        phase = exp1((r * (p * p % a)) / a)
        weight = 1.0 - exp1((r * p) / a)
        weighted_sum += phase * weight
    return -weighted_sum.imag / (math.pi * r * math.sqrt(p))


def stationary_contribution_over_sqrt(
    p: int,
    r: int,
    y: int,
    kappa: float,
) -> tuple[float, int]:
    """计算 B-process 驻相主项贡献并除以 sqrt(P)。"""
    lower_a = y + 1
    upper_a = p - 1
    lower_n = max(1, math.ceil(r * p * p / (upper_a * upper_a)))
    upper_n = math.floor(r * p * p / (lower_a * lower_a))
    model_sum = 0j
    term_count = 0

    for n in range(lower_n, upper_n + 1):
        x = p * math.sqrt(r / n)
        if x < lower_a or x > upper_a:
            continue
        root = math.sqrt(r * n)
        # 归一化后 1/sqrt(f'') 给出 r^(1/4)/(sqrt(2)n^(3/4))。
        coeff = (r ** 0.25) / (math.sqrt(2.0) * (n ** 0.75))
        weight = 1.0 - exp1(root)
        phase = exp1(2.0 * p * root + kappa)
        model_sum += coeff * weight * phase
        term_count += 1

    return -model_sum.imag / (math.pi * r), term_count


def discrepancy_over_sqrt(p: int, y: int) -> float:
    """计算真实 D(P)/sqrt(P)。"""
    carry = 0
    weight = 0.0
    for a in range(y + 1, p):
        q = p // a
        h = p - q * a
        carry += 1 if (h * h) % a + h > a else 0
        weight += h / a
    return (carry - weight) / math.sqrt(p)


def load_samples(path: Path, limit: int | None) -> list[int]:
    """从频率审计 JSON 读取样本 P。"""
    data = json.loads(path.read_text(encoding="utf-8"))
    samples = [record["p"] for record in data["records"]]
    if limit is not None:
        samples = samples[:limit]
    return samples


def audit(input_json: Path, freq: int, limit: int | None) -> dict:
    """执行 B-process 模型审计。"""
    samples = load_samples(input_json, limit)
    kappas = [-0.375, -0.25, -0.125, 0.0, 0.125, 0.25, 0.375]
    records = []

    for p in samples:
        y = max(2, int(math.floor(p / math.e)))
        exact_terms = []
        model_terms = {str(kappa): [] for kappa in kappas}
        stationary_terms = 0

        for r in range(1, freq + 1):
            exact_terms.append(exact_contribution_over_sqrt(p, r, y))
            for kappa in kappas:
                value, count = stationary_contribution_over_sqrt(p, r, y, kappa)
                model_terms[str(kappa)].append(value)
                if kappa == kappas[0]:
                    stationary_terms += count

        exact_partial = sum(exact_terms)
        models = {
            str(kappa): {
                "partial_over_sqrt": sum(model_terms[str(kappa)]),
                "error_over_sqrt": exact_partial - sum(model_terms[str(kappa)]),
            }
            for kappa in kappas
        }
        records.append(
            {
                "p": p,
                "y": y,
                "freq": freq,
                "stationary_terms": stationary_terms,
                "discrepancy_over_sqrt_p": discrepancy_over_sqrt(p, y),
                "exact_partial_over_sqrt_p": exact_partial,
                "models": models,
            }
        )

    kappa_stats = {}
    for kappa in kappas:
        key = str(kappa)
        errors = [record["models"][key]["error_over_sqrt"] for record in records]
        rmse = math.sqrt(sum(error * error for error in errors) / len(errors))
        max_abs = max(abs(error) for error in errors)
        mean_error = sum(errors) / len(errors)
        kappa_stats[key] = {
            "rmse": rmse,
            "max_abs_error": max_abs,
            "mean_error": mean_error,
        }

    best_key = min(kappa_stats, key=lambda key: kappa_stats[key]["rmse"])
    for record in records:
        record["best_model"] = {
            "kappa": float(best_key),
            **record["models"][best_key],
        }

    worst = max(
        records,
        key=lambda item: abs(item["best_model"]["error_over_sqrt"]),
        default=None,
    )
    return {
        "parameters": {
            "input_json": str(input_json),
            "freq": freq,
            "limit": limit,
            "kappas": kappas,
        },
        "summary": {
            "sample_count": len(records),
            "best_kappa": float(best_key),
            "best_kappa_stats": kappa_stats[best_key],
            "kappa_stats": kappa_stats,
            "worst_best_model_record": worst,
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# EndpointReciprocal-OSC B-process 模型审计",
        "",
        "**状态：** `bprocess_model_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `input_json`: `{params['input_json']}`",
        f"- `freq`: `{params['freq']}`",
        f"- `sample_count`: `{summary['sample_count']}`",
        "",
        "## 相位常数扫描",
        "",
        "| kappa | rmse | max abs error | mean error |",
        "|---:|---:|---:|---:|",
    ]
    for key, stats in summary["kappa_stats"].items():
        lines.append(
            f"| {float(key):.3f} | {stats['rmse']:.6f} | "
            f"{stats['max_abs_error']:.6f} | {stats['mean_error']:.6f} |"
        )
    best = summary["best_kappa_stats"]
    lines.extend(
        [
            "",
            "## 最优常数",
            "",
            f"- `best_kappa`: `{summary['best_kappa']}`。",
            f"- `rmse`: `{best['rmse']:.6f}`。",
            f"- `max_abs_error`: `{best['max_abs_error']:.6f}`。",
            "",
            "## 样本表",
            "",
            "| p | D/sqrtP | exact partial/sqrtP | model/sqrtP | error/sqrtP | terms |",
            "|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for record in result["records"]:
        best_model = record["best_model"]
        lines.append(
            f"| {record['p']} | {record['discrepancy_over_sqrt_p']:.6f} | "
            f"{record['exact_partial_over_sqrt_p']:.6f} | "
            f"{best_model['partial_over_sqrt']:.6f} | "
            f"{best_model['error_over_sqrt']:.6f} | "
            f"{record['stationary_terms']} |"
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "该审计只比较粗 B-process 主项与真实低频有符号贡献。若误差稳定为 O(1) 且不随 P 增长，则 `ERO-Low` 可拆成有限非平方频率主项账本加 `ERO-Edge` 端点余项。若误差集中在少数 P 或频率上，则进入 endpoint PDEC/SAE 路由。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-json",
        default="docs/diagonal_postsquare_carry_reciprocal_frequency_audit_p50000_20260505.json",
    )
    parser.add_argument("--freq", type=int, default=64)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_bprocess_model_audit_r64_20260505",
    )
    args = parser.parse_args()
    result = audit(Path(args.input_json), args.freq, args.limit)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
