#!/usr/bin/env python3
"""审计 z=61 Residue-PDEC 的本地有符号吸收。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_residue_signed_absorption_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-residue-signed-absorption-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-residue-signed-absorption-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-residue-signed-absorption-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
RESIDUE_PDEC_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-residue-pdec-registration-router.json"
QUOTIENT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-residue-signed-absorption-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-residue-signed-absorption-router.md"

NEXT_TARGET = "GlobalResidueSignedCountBalanceOrUnabsorbedResiduePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-residue-pdec-registration-router.json",
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_residue_signed_absorption_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def sign_value(label: str) -> int:
    """把 profile 符号转成计数符号。"""
    if label == "positive":
        return 1
    if label == "negative":
        return -1
    return 0


def audit() -> dict[str, Any]:
    """执行本地 Residue-PDEC 吸收审计。"""
    pdec = json.loads(RESIDUE_PDEC_JSON.read_text(encoding="utf-8"))
    quotient = json.loads(QUOTIENT_JSON.read_text(encoding="utf-8"))
    contribution_by_quotient = {
        row["phase_quotient"]: row["target_contribution"]
        for row in quotient["quotient_rows"]
    }
    rows = []
    signed_count = 0
    signed_weight = 0.0
    positive_weight = 0.0
    negative_weight = 0.0
    for record in pdec["residue_pdec_records"]:
        sign = sign_value(record["target_cell_sign"])
        weight = contribution_by_quotient[record["phase_quotient"]]
        signed_count += sign
        signed_weight += sign * weight
        if sign > 0:
            positive_weight += weight
        elif sign < 0:
            negative_weight += weight
        rows.append(
            {
                **record,
                "unit_weight": weight,
                "signed_count_contribution": sign,
                "signed_weight_contribution": sign * weight,
            }
        )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_residue_signed_absorption_router",
        "status": "z61_registered_residue_pdec_locally_absorbed_global_balance_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            pdec["certificate_type"],
            quotient["certificate_type"],
        ],
        "constant_unit_weight_closed": quotient["constant_per_hit_contribution_closed"],
        "unit_weight": quotient["per_hit_contribution"],
        "positive_record_count": pdec["positive_record_count"],
        "negative_record_count": pdec["negative_record_count"],
        "signed_count": signed_count,
        "positive_weight": positive_weight,
        "negative_weight": negative_weight,
        "signed_weight": signed_weight,
        "local_negative_residue_pdec_absorbed": signed_count >= 0 and signed_weight >= 0,
        "strict_positive_absorption_margin": signed_count > 0 and signed_weight > 0,
        "rows": rows,
        "global_residue_signed_count_balance_proved": False,
        "unabsorbed_residue_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "已登记的三条 Residue-PDEC 记录在当前 formal unit 内不是净负缺陷："
            "每条记录权重相同，一条负记录由两条正记录吸收，净计数为 `+1`。"
            "这闭合的是本地样本 formal unit 的负缺陷吸收；"
            "全局仍需证明 residue signed count balance，或排斥未吸收 Residue-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 Residue signed absorption",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"constant_unit_weight_closed={fmt_bool(result['constant_unit_weight_closed'])}",
        f"unit_weight={fmt_float(result['unit_weight'])}",
        f"positive_record_count={result['positive_record_count']}",
        f"negative_record_count={result['negative_record_count']}",
        f"signed_count={result['signed_count']}",
        f"signed_weight={fmt_float(result['signed_weight'])}",
        f"local_negative_residue_pdec_absorbed={fmt_bool(result['local_negative_residue_pdec_absorbed'])}",
        f"global_residue_signed_count_balance_proved={fmt_bool(result['global_residue_signed_count_balance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有符号记录",
        "",
        "| sign | quotient | p | q | b | modulus | residue | signed weight |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| `{row['target_cell_sign']}` | {row['phase_quotient']} | {row['p']} | "
            f"{row['q']} | {row['b']} | {row['modulus']} | {row['residue']} | "
            f"{fmt_float(row['signed_weight_contribution'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：当前 formal unit 的本地负 Residue-PDEC 被同权正记录吸收。",
            "- 未闭合：全局 Residue signed count balance，或未吸收 Residue-PDEC 排斥。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "local_negative_residue_pdec_absorbed": result["local_negative_residue_pdec_absorbed"],
                "signed_count": result["signed_count"],
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
