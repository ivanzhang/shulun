#!/usr/bin/env python3
"""把 localized signed-ratio cap 等价改写为正负两色质量平衡。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_localized_block_twocolor_balance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-localized-block-twocolor-balance-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-localized-block-twocolor-balance-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-localized-block-twocolor-balance-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SIGNED_TABLE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-signed-ratio-budget-table-router.json"
BILINEAR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-localized-block-twocolor-balance-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-localized-block-twocolor-balance-router.md"

NEXT_TARGET = "Z61TwoColorMassBalanceRatio1569OrLocalizedBlockPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-signed-ratio-budget-table-router.json",
    "prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json",
]


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_localized_block_twocolor_balance_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def route_for_bucket(bucket: str) -> str:
    """复原局部块路线。"""
    if bucket in {"balanced<=2", "mid<=4"}:
        return "BilinearDispersion"
    return "EndpointPDEC"


def audit() -> dict[str, Any]:
    """生成两色质量平衡合同。"""
    signed_table = json.loads(SIGNED_TABLE_JSON.read_text(encoding="utf-8"))
    bilinear = json.loads(BILINEAR_JSON.read_text(encoding="utf-8"))
    cap_by_atom = {
        (int(row["z"]), row["bucket"]): row
        for row in signed_table["atom_rows"]
        if not row["closed_by_trivial_bound"]
    }
    rows = []
    for z_row in bilinear["rows"]:
        z = int(z_row["z"])
        for block in z_row["balance_buckets"]:
            key = (z, block["bucket"])
            if key not in cap_by_atom:
                continue
            cap_row = cap_by_atom[key]
            cap = float(cap_row["required_signed_ratio_cap"])
            signed = float(block["signed_contribution"])
            abs_sum = float(block["abs_contribution"])
            positive_abs = (abs_sum + signed) / 2.0
            negative_abs = (abs_sum - signed) / 2.0
            observed_ratio = max(positive_abs, negative_abs) / min(positive_abs, negative_abs)
            required_ratio = (1.0 + cap) / (1.0 - cap)
            rows.append(
                {
                    "atom_label": cap_row["atom_label"],
                    "z": z,
                    "bucket": block["bucket"],
                    "route": route_for_bucket(block["bucket"]),
                    "signed_ratio_cap": cap,
                    "required_two_color_ratio": required_ratio,
                    "positive_abs": positive_abs,
                    "negative_abs": negative_abs,
                    "observed_two_color_ratio": observed_ratio,
                    "ratio_slack": required_ratio - observed_ratio,
                    "sample_passes_ratio": observed_ratio <= required_ratio,
                }
            )
    z31 = [row for row in rows if row["z"] == 31]
    z61 = [row for row in rows if row["z"] == 61]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_localized_block_twocolor_balance_router",
        "status": "localized_block_signed_caps_reduced_to_twocolor_balance_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "signed_ratio_to_twocolor_equivalence_closed": True,
        "z31_wide_ratio_contract_materialized": True,
        "z61_tight_ratio_contract_materialized": True,
        "z31_twocolor_balance_proved": False,
        "z61_twocolor_balance_proved": False,
        "localized_block_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "nontrivial_atom_count": len(rows),
        "z31_required_ratio": z31[0]["required_two_color_ratio"] if z31 else None,
        "z61_required_ratio": z61[0]["required_two_color_ratio"] if z61 else None,
        "max_observed_ratio_z31": max((row["observed_two_color_ratio"] for row in z31), default=None),
        "max_observed_ratio_z61": max((row["observed_two_color_ratio"] for row in z61), default=None),
        "sample_failure_count": sum(1 for row in rows if not row["sample_passes_ratio"]),
        "rows": rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "`signed/abs<=theta` 已等价改写为正负两色质量比 "
            "`max(P,N)/min(P,N)<=(1+theta)/(1-theta)`。"
            "`z=31` 的 cap 只需排除约 `3.895:1` 的正负质量偏斜，"
            "`z=61` 的 cap 需要排除约 `1.569:1` 的偏斜。"
            "因此最终局部块硬点变为两色质量平衡，若失败则直接给出 LocalizedBlock-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha 局部块两色质量平衡",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_ratio_to_twocolor_equivalence_closed={fmt_bool(result['signed_ratio_to_twocolor_equivalence_closed'])}",
        f"z31_wide_ratio_contract_materialized={fmt_bool(result['z31_wide_ratio_contract_materialized'])}",
        f"z61_tight_ratio_contract_materialized={fmt_bool(result['z61_tight_ratio_contract_materialized'])}",
        f"z31_twocolor_balance_proved={fmt_bool(result['z31_twocolor_balance_proved'])}",
        f"z61_twocolor_balance_proved={fmt_bool(result['z61_twocolor_balance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 两色合同",
        "",
        "| atom | route | required ratio | observed ratio | slack | positive abs | negative abs |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| `{row['atom_label']}` | `{row['route']}` | "
            f"{fmt_float(row['required_two_color_ratio'])} | {fmt_float(row['observed_two_color_ratio'])} | "
            f"{fmt_float(row['ratio_slack'])} | {fmt_float(row['positive_abs'])} | "
            f"{fmt_float(row['negative_abs'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：signed-ratio cap 与两色质量比合同的等价转换。",
            f"- `z=31` 需要正负质量比不超过 `{fmt_float(result['z31_required_ratio'])}`。",
            f"- `z=61` 需要正负质量比不超过 `{fmt_float(result['z61_required_ratio'])}`。",
            "- 未闭合：`z=31` 宽比例合同。",
            "- 未闭合：`z=61` 紧比例合同，这是当前最窄点。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
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
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "z31_required_ratio": result["z31_required_ratio"],
                "z61_required_ratio": result["z61_required_ratio"],
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
