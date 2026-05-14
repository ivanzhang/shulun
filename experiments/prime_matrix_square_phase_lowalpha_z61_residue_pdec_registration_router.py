#!/usr/bin/env python3
"""登记 z=61 singleton residue gate 的 Residue-PDEC 证书对象。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_residue_pdec_registration_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-residue-pdec-registration-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-residue-pdec-registration-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-residue-pdec-registration-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
RESIDUE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-singleton-residue-gate-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-residue-pdec-registration-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-residue-pdec-registration-router.md"

NEXT_TARGET = "ResiduePDECExclusionOrSingletonResidueSignedCountBalance"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-singleton-residue-gate-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_residue_pdec_registration_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """登记 Residue-PDEC 对象。"""
    data = json.loads(RESIDUE_JSON.read_text(encoding="utf-8"))
    records = []
    for row in data["rows"]:
        records.append(
            {
                "formal_unit_key": (
                    "z61|singleton-residue|"
                    f"sign={row['target_cell_sign']}|p={row['p']}|q={row['q']}|"
                    f"b={row['b']}|mod={row['modulus_bq']}|res={row['residue_p2_mod_bq']}"
                ),
                "target_cell_sign": row["target_cell_sign"],
                "phase_quotient": row["phase_quotient"],
                "p": row["p"],
                "q": row["q"],
                "a": row["a"],
                "b": row["b"],
                "modulus": row["modulus_bq"],
                "residue": row["residue_p2_mod_bq"],
                "delta": row["delta_abq_minus_p2"],
                "short_delta_condition": f"0 < {row['delta_abq_minus_p2']} < {row['p']}",
                "residue_condition": row["residue_gate_statement"],
            }
        )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_residue_pdec_registration_router",
        "status": "z61_singleton_residue_pdec_registered_not_excluded",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": data["certificate_type"],
        "residue_pdec_records": records,
        "negative_record_count": sum(1 for row in records if row["target_cell_sign"] == "negative"),
        "positive_record_count": sum(1 for row in records if row["target_cell_sign"] == "positive"),
        "residue_pdec_registration_closed": (
            data["all_residue_gates_closed"]
            and data["all_short_delta_bounds_closed"]
            and len(records) == 3
        ),
        "residue_pdec_excluded": False,
        "singleton_residue_signed_count_balance_proved": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Singleton residue gate 分支已登记成三个短残基 PDEC 对象："
            "一条负记录、两条正记录。登记闭合的是失败对象的形式化；"
            "仍需排斥 Residue-PDEC，或证明 singleton residue signed count balance。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 Residue-PDEC 登记",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"residue_pdec_registration_closed={fmt_bool(result['residue_pdec_registration_closed'])}",
        f"negative_record_count={result['negative_record_count']}",
        f"positive_record_count={result['positive_record_count']}",
        f"residue_pdec_excluded={fmt_bool(result['residue_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Residue-PDEC Records",
        "",
        "| sign | quotient | p | q | a | b | modulus | residue | delta |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["residue_pdec_records"]:
        lines.append(
            f"| `{row['target_cell_sign']}` | {row['phase_quotient']} | {row['p']} | "
            f"{row['q']} | {row['a']} | {row['b']} | {row['modulus']} | "
            f"{row['residue']} | {row['delta']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：短残基失败对象的正式登记。",
            "- 未闭合：Residue-PDEC 排斥，或 singleton residue signed count balance。",
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
                "residue_pdec_registration_closed": result["residue_pdec_registration_closed"],
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
