#!/usr/bin/env python3
"""生成 RPZ unit endpoint 的 ColumnCRT 门控证书。

用法示例：
  python3 experiments/prime_matrix_rpz_unit_endpoint_columncrt_gate.py

该脚本读取 first-grid-fail seam 证书。对每条 unit endpoint 分支证明一个更窄的
结构事实：端点 `ap` 在下层 `r` 网格中落在固定非平凡列

  c == ap mod r == r + (p-r) - delta,

并且对任意同列素数见证 `pi=h*r+c`，端点行与见证行的位移模 `p` 与行号 `a`
无关且非零。这把持久 unit endpoint seam 从泛泛的 `PDEC/ColumnCRT` 入口压缩为
一个固定非零位移余类的 ColumnCRT 门控对象。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def is_prime(value: int) -> bool:
    """朴素素性测试；当前证书只需处理很小的列见证候选。"""
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def inverse_mod(value: int, modulus: int) -> int:
    """返回 `value` 在模 `modulus` 下的逆元。"""
    return pow(value % modulus, -1, modulus)


def least_column_prime_witness(r: int, column: int) -> dict[str, int] | None:
    """寻找 `h*r+column` 形式的最小素数见证。"""
    for witness_row in range(r + 1):
        witness_prime = witness_row * r + column
        if is_prime(witness_prime):
            return {
                "witness_prime": witness_prime,
                "witness_row_zero_based": witness_row,
            }
    return None


def build_gate_row(seam_row: dict[str, Any]) -> dict[str, Any]:
    """把一条 seam 行转成 unit endpoint ColumnCRT 门控行。"""
    p = seam_row["p"]
    r = seam_row["r"]
    gap = seam_row["gap"]
    delta = seam_row["delta"]
    row_residue = seam_row["row_residue_mod_r"]
    unit_size = seam_row["endpoint_split_packet"]["lower_sieve_status"][
        "rough_support_size"
    ]
    lower_column = (p * row_residue) % r
    expected_column = r + gap - delta
    witness = least_column_prime_witness(r, lower_column)

    endpoint_row_mod_p = (-lower_column * inverse_mod(r, p)) % p
    if witness is None:
        witness_prime = None
        witness_row = None
        displacement_mod_p = None
        nonzero_displacement = None
    else:
        witness_prime = witness["witness_prime"]
        witness_row = witness["witness_row_zero_based"]
        displacement_mod_p = (witness_row - endpoint_row_mod_p) % p
        nonzero_displacement = displacement_mod_p != 0 and witness_prime != p

    unit_residues = seam_row["endpoint_split_packet"]["lower_sieve_status"][
        "rough_support_residues_mod_Q"
    ]
    residue_checks = []
    for residue in unit_residues:
        endpoint_value_mod_r = (p * residue) % r
        endpoint_lower_row_mod_p = (
            ((p * residue - lower_column) // r) % p
        )
        residue_checks.append(
            {
                "a_mod_Q": residue,
                "endpoint_mod_r": endpoint_value_mod_r,
                "endpoint_lower_row_mod_p": endpoint_lower_row_mod_p,
                "column_ok": endpoint_value_mod_r == lower_column,
                "row_mod_p_ok": endpoint_lower_row_mod_p == endpoint_row_mod_p,
            }
        )

    return {
        "p": p,
        "r": r,
        "gap": gap,
        "delta": delta,
        "row_residue_mod_r": row_residue,
        "unit_endpoint_support_size": unit_size,
        "lower_column_mod_r": lower_column,
        "lower_column_expected_from_right_cap": expected_column,
        "column_identity_ok": lower_column == expected_column,
        "column_is_nontrivial": 1 <= lower_column < r,
        "same_column_witness": witness,
        "endpoint_lower_row_mod_p": endpoint_row_mod_p,
        "columncrt_label": p,
        "columncrt_displacement_mod_p": displacement_mod_p,
        "columncrt_displacement_nonzero": nonzero_displacement,
        "unit_residue_checks": residue_checks,
        "all_unit_residues_have_fixed_column": all(
            item["column_ok"] for item in residue_checks
        ),
        "all_unit_residues_have_fixed_row_mod_p": all(
            item["row_mod_p_ok"] for item in residue_checks
        ),
        "gate_verdict": (
            "routes_to_fixed_nonzero_columncrt_residue"
            if nonzero_displacement
            else "missing_same_column_witness"
        ),
        "remaining_for_exclusion": [
            "把正式反例族映射到这些 unit endpoint rows",
            "给出全局同列素数见证或列命题输入",
            "证明 ColumnCRTDefect 阈值 L_D 不可被超过，或将超过视为已排除出口",
        ],
    }


def build(source_path: Path) -> dict[str, Any]:
    """构造 unit endpoint ColumnCRT 门控证书。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    gate_rows = [
        build_gate_row(row)
        for row in source["seam_phase_rows"]
        if row["endpoint_split_packet"]["lower_sieve_status"]["rough_support_size"] > 0
    ]
    return {
        "status": "rpz_unit_endpoint_columncrt_gate_certificate",
        "source": str(source_path),
        "summary": {
            "gate_row_count": len(gate_rows),
            "unit_endpoint_phase_count": sum(
                row["unit_endpoint_support_size"] for row in gate_rows
            ),
            "rows_with_column_identity_ok": sum(
                1 for row in gate_rows if row["column_identity_ok"]
            ),
            "rows_with_explicit_same_column_witness": sum(
                1 for row in gate_rows if row["same_column_witness"] is not None
            ),
            "rows_with_nonzero_displacement": sum(
                1 for row in gate_rows if row["columncrt_displacement_nonzero"]
            ),
            "rows_with_fixed_unit_residue_column": sum(
                1 for row in gate_rows if row["all_unit_residues_have_fixed_column"]
            ),
            "rows_with_fixed_unit_row_mod_p": sum(
                1 for row in gate_rows if row["all_unit_residues_have_fixed_row_mod_p"]
            ),
        },
        "gate_rows": gate_rows,
        "review_boundary": [
            "本证书证明 unit endpoint seam 的列位移入口已标准化",
            "本证书不排除 ColumnCRTDefect",
            "全局闭合仍需 ColumnCRT 阈值或正式反例族避开证明",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 证书报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ Unit Endpoint ColumnCRT 门控证书",
        "",
        "**状态：** `rpz_unit_endpoint_columncrt_gate_certificate`",
        "",
        "## 关键恒等式",
        "",
        "设相邻下降 `p->r`、`g=p-r`、`delta=-(a-1)g mod r`，并处在 first-grid-fail seam：`g<delta<r`。若 `a≡rho mod r`，则 unit endpoint `ap` 在下层 `r` 网格中的列为",
        "",
        "```text",
        "c ≡ p*rho mod r = r+g-delta。",
        "```",
        "",
        "因此 `c` 是固定的非平凡列 `1<=c<r`。若同列素数见证为 `pi=h*r+c`，则端点下层行号满足",
        "",
        "```text",
        "H*r+c = a*p,  so  H ≡ -c*r^{-1} mod p。",
        "```",
        "",
        "于是位移 `d=h-H mod p` 与 `a` 无关；且若 `pi` 是素数并且 `pi!=p`，则 `d` 不能为 `0 mod p`。这正是 `ColumnCRT` 的固定非零位移余类入口。",
        "",
        "## 总结",
        "",
        f"- 门控行数：`{summary['gate_row_count']}`。",
        f"- unit endpoint 相位总数：`{summary['unit_endpoint_phase_count']}`。",
        f"- 列恒等式通过行数：`{summary['rows_with_column_identity_ok']}`。",
        f"- 有显式同列素数见证行数：`{summary['rows_with_explicit_same_column_witness']}`。",
        f"- 非零位移通过行数：`{summary['rows_with_nonzero_displacement']}`。",
        f"- unit residues 固定列通过行数：`{summary['rows_with_fixed_unit_residue_column']}`。",
        f"- unit residues 固定 `H mod p` 通过行数：`{summary['rows_with_fixed_unit_row_mod_p']}`。",
        "",
        "## 门控表",
        "",
        "| p | r | delta | rho | c | unit | witness pi | witness row | H mod p | d mod p | verdict |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["gate_rows"]:
        witness = row["same_column_witness"] or {}
        lines.append(
            "| {p} | {r} | {delta} | {rho} | {c} | {unit} | {pi} | {h} | {H} | {d} | `{verdict}` |".format(
                p=row["p"],
                r=row["r"],
                delta=row["delta"],
                rho=row["row_residue_mod_r"],
                c=row["lower_column_mod_r"],
                unit=row["unit_endpoint_support_size"],
                pi=witness.get("witness_prime", "NA"),
                h=witness.get("witness_row_zero_based", "NA"),
                H=row["endpoint_lower_row_mod_p"],
                d=row["columncrt_displacement_mod_p"],
                verdict=row["gate_verdict"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿意义",
            "",
            "本证书把 `404` 个 unit endpoint seam 相位进一步压缩：一旦同一 unit seam 相位持久出现，端点标签固定为 `p`，下层列固定为 `c=r+g-delta`，同列见证位移固定为一个非零 `mod p` 余类。因此它不是任意 PDEC 坏窗，而是标准 `ColumnCRTDefect(p,d)` 候选。",
            "",
            "这一步仍不是全局命题闭合。剩余硬义务是证明正式反例族确实映入这些门控行，并排除对应 `ColumnCRTDefect` 阈值 `L_D`，或证明正式反例族避开 unit endpoint seam。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(
            "docs/monograph/prime-matrix-rpz-first-grid-fail-seam-certificate.json"
        ),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-unit-endpoint-columncrt-gate"),
    )
    args = parser.parse_args()
    result = build(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
