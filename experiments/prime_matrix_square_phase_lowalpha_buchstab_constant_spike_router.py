#!/usr/bin/env python3
"""生成 Buchstab 模型常数账本或局部密度尖峰二分证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_buchstab_constant_spike_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-constant-spike-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-constant-spike-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-constant-spike-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-model-density-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-constant-spike-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-constant-spike-router.md"

DEFAULT_CONSTANTS = [1.5, 2.0, 2.5, 3.0]
NEXT_TARGET = "UniformBuchstabConstantProofOrDensitySpikePDECExclusion"


def parse_float_list(text: str) -> list[float]:
    """解析浮点数列表。"""
    return [float(part) for part in text.split(",") if part.strip()]


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source() -> dict[str, Any]:
    """读取上一步 Buchstab 模型账本。"""
    return json.loads(SOURCE_JSON.read_text(encoding="utf-8"))


def collect_block_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """提取 block 级账本行。"""
    rows = []
    for profile in source["profiles"]:
        for row in profile["rows"]:
            rows.append(
                {
                    "p": row["p"],
                    "previous_cutoff": row["previous_cutoff"],
                    "cutoff": row["cutoff"],
                    "hits": row["cofactor_hits"],
                    "model": row["buchstab_model_sum"],
                    "actual_over_model": row["actual_over_buchstab_model"],
                    "top_hit_predecessor": row["top_hit_predecessor"],
                    "top_model_excess_predecessor": row["top_model_excess_predecessor"],
                    "h_bucket_rows": row["h_bucket_rows"],
                }
            )
    return rows


def collect_bucket_rows(block_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """提取尺度桶级账本行。"""
    rows = []
    for block in block_rows:
        for bucket, values in block["h_bucket_rows"].items():
            model = values["model"]
            ratio = None if model == 0 else values["hits"] / model
            rows.append(
                {
                    "p": block["p"],
                    "previous_cutoff": block["previous_cutoff"],
                    "cutoff": block["cutoff"],
                    "bucket": bucket,
                    "hits": values["hits"],
                    "model": model,
                    "actual_over_model": ratio,
                    "weighted_density": values["weighted_density"],
                }
            )
    return rows


def worst_ratio(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    """返回最高 actual/model 行。"""
    valid = [row for row in rows if row["actual_over_model"] is not None]
    return max(valid, key=lambda row: row["actual_over_model"], default=None)


def threshold_table(constants: list[float], block_rows: list[dict[str, Any]], bucket_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """生成常数二分表。"""
    table = []
    for constant in constants:
        block_failures = [row for row in block_rows if row["actual_over_model"] is not None and row["actual_over_model"] > constant]
        bucket_failures = [row for row in bucket_rows if row["actual_over_model"] is not None and row["actual_over_model"] > constant]
        table.append(
            {
                "constant": constant,
                "block_constant_passes_sample": not block_failures,
                "bucket_constant_passes_sample": not bucket_failures,
                "block_failure_count": len(block_failures),
                "bucket_failure_count": len(bucket_failures),
                "top_block_failure": worst_ratio(block_failures),
                "top_bucket_failure": worst_ratio(bucket_failures),
            }
        )
    return table


def audit(constants: list[float]) -> dict[str, Any]:
    """执行常数/尖峰二分审计。"""
    source = load_source()
    block_rows = collect_block_rows(source)
    bucket_rows = collect_bucket_rows(block_rows)
    block_worst = worst_ratio(block_rows)
    bucket_worst = worst_ratio(bucket_rows)
    table = threshold_table(constants, block_rows, bucket_rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_buchstab_constant_spike_router",
        "status": "buchstab_constant_or_local_density_spike_dichotomy_materialized_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "constant_spike_dichotomy_closed": True,
        "uniform_buchstab_constant_proved": False,
        "local_density_spike_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "total_actual_over_buchstab_model": source["total_actual_over_buchstab_model"],
        "worst_block_actual_over_model": block_worst,
        "worst_bucket_actual_over_model": bucket_worst,
        "threshold_table": table,
        "source_hashes": {
            "docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-model-density-router.json": file_sha256(SOURCE_JSON),
            "experiments/prime_matrix_square_phase_lowalpha_buchstab_constant_spike_router.py": file_sha256(
                Path(__file__).resolve()
            ),
        },
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Buchstab 模型常数问题已严格二分：给定任意常数 `C_B`，"
            "若所有 block/尺度桶满足 `actual <= C_B*model`，则 low-alpha 模型负载由该常数支付；"
            "否则自动抽取最高超标 block 或尺度桶作为局部密度尖峰 PDEC 候选。"
            "本步闭合的是二分逻辑，不是常数证明或 PDEC 排斥。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha Buchstab 常数/尖峰二分",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"constant_spike_dichotomy_closed={fmt_bool(result['constant_spike_dichotomy_closed'])}",
        f"uniform_buchstab_constant_proved={fmt_bool(result['uniform_buchstab_constant_proved'])}",
        f"local_density_spike_pdec_excluded={fmt_bool(result['local_density_spike_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 样本最坏比例",
        "",
        "| scope | worst actual/model | witness |",
        "| --- | ---: | --- |",
        f"| global | {result['total_actual_over_buchstab_model']:.6f} | all low-alpha rows |",
        f"| block | {result['worst_block_actual_over_model']['actual_over_model']:.6f} | `{result['worst_block_actual_over_model']}` |",
        f"| H-bucket | {result['worst_bucket_actual_over_model']['actual_over_model']:.6f} | `{result['worst_bucket_actual_over_model']}` |",
        "",
        "## 2. 常数门表",
        "",
        "| C_B | block sample pass | block failures | bucket sample pass | bucket failures | top bucket failure |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["threshold_table"]:
        lines.append(
            f"| {row['constant']:.3f} | {fmt_bool(row['block_constant_passes_sample'])} | "
            f"{row['block_failure_count']} | {fmt_bool(row['bucket_constant_passes_sample'])} | "
            f"{row['bucket_failure_count']} | `{row['top_bucket_failure']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：任意常数 `C_B` 下的模型常数/局部尖峰二分。",
            "- 未闭合：证明一个足够小的统一 Buchstab 常数。",
            "- 未闭合：若统一常数失败，排除对应局部密度尖峰 PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--constants", default=",".join(str(item) for item in DEFAULT_CONSTANTS))
    args = parser.parse_args()
    result = audit(parse_float_list(args.constants))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "constant_spike_dichotomy_closed": result["constant_spike_dichotomy_closed"],
                "total_actual_over_buchstab_model": result["total_actual_over_buchstab_model"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
