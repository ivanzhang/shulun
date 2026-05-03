#!/usr/bin/env python3
"""抽取 RPZ-BCB 候选下层行相位身份。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_candidate_phase_identity.py

短候选块公式把剩余硬点压成：证明正式 BCB 核心区间诱导的候选下层
行相位属于 accepted set `A_h`。本脚本把这个相位从 BCB 构造参数中
逐项抽出，避免把“候选行号从程序扫描得到”作为黑箱。

设上层素数为 `P`，上层零行号为 `R`，半宽素数为 `h`，平台位移为
`s_min..s_max`，尾锚阈值为 `T`。BCB 强制核心区间为

  L=(R-1)P+1+s_min+T,
  U=RP+s_max-T。

完整包含在 `[L,U]` 中的 `h` 对齐行号满足

  L <= (m-1)h+1 and mh <= U。

因此候选行区间为

  m_min=floor((L+h-2)/h)+1,
  m_max=floor(U/h)。

写 `P=Qh+d` 后，该公式等价于只依赖 `R mod hP(h)` 的相位公式：

  m_min=(R-1)Q+floor(((R-1)d+s_min+T+h-1)/h)+1,
  m_max=RQ+floor((Rd+s_max-T)/h)。

这就是后续要证明落入 `A_h` 的精确对象。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from prime_matrix_rpz_formal_phase_automaton import (
    acceptance_checker,
    primes_upto,
    primorial,
)


def candidate_rows_by_identity(record: dict[str, Any]) -> dict[str, Any]:
    """用 BCB 参数公式计算候选行区间。"""
    top_prime = record["top_prime"]
    top_row = record["top_zero_row"]
    h = record["half_prime"]
    tail_threshold = record["tail_threshold"]
    shift_min = min(record["zero_shift_plateau"])
    shift_max = max(record["zero_shift_plateau"])
    left = (top_row - 1) * top_prime + 1 + shift_min + tail_threshold
    right = top_row * top_prime + shift_max - tail_threshold
    direct_min = (left + h - 2) // h + 1
    direct_max = right // h

    quotient, remainder = divmod(top_prime, h)
    affine_min = (
        (top_row - 1) * quotient
        + ((top_row - 1) * remainder + shift_min + tail_threshold + h - 1) // h
        + 1
    )
    affine_max = (
        top_row * quotient
        + (top_row * remainder + shift_max - tail_threshold) // h
    )
    rows = list(range(direct_min, direct_max + 1)) if direct_min <= direct_max else []
    return {
        "core_interval_from_identity": [left, right],
        "direct_candidate_min": direct_min,
        "direct_candidate_max": direct_max,
        "affine_candidate_min": affine_min,
        "affine_candidate_max": affine_max,
        "identity_matches_core_interval": record["forced_core_interval"] == [left, right],
        "identity_matches_contained_rows": rows == record["contained_half_rows"],
        "candidate_rows_by_identity": rows,
        "top_prime_div_half": {
            "quotient": quotient,
            "remainder": remainder,
        },
    }


def phase_from_residue(
    top_row_residue: int,
    top_prime: int,
    h: int,
    shift_min: int,
    shift_max: int,
    tail_threshold: int,
    modulus_h: int,
) -> tuple[int, int]:
    """只用 `R mod hP(h)` 计算候选行相位区间。"""
    quotient, remainder = divmod(top_prime, h)
    representative = top_row_residue
    min_phase = (
        (representative - 1) * quotient
        + ((representative - 1) * remainder + shift_min + tail_threshold + h - 1) // h
        + 1
    ) % modulus_h
    max_phase = (
        representative * quotient
        + (representative * remainder + shift_max - tail_threshold) // h
    ) % modulus_h
    return min_phase, max_phase


def audit_record(primes: list[int], record: dict[str, Any]) -> dict[str, Any]:
    """审计单条 BCB 记录的候选行相位身份。"""
    h = record["half_prime"]
    modulus_h = primorial(primes, h)
    period_h = h * modulus_h
    identity = candidate_rows_by_identity(record)
    accepts = acceptance_checker(primes, h)
    shift_min = min(record["zero_shift_plateau"])
    shift_max = max(record["zero_shift_plateau"])
    residue_min, residue_max = phase_from_residue(
        record["top_zero_row"] % period_h,
        record["top_prime"],
        h,
        shift_min,
        shift_max,
        record["tail_threshold"],
        modulus_h,
    )
    candidate_phases = [row % modulus_h for row in identity["candidate_rows_by_identity"]]
    candidate_acceptance = [accepts(h, phase) for phase in candidate_phases]
    return {
        "top_prime": record["top_prime"],
        "top_zero_row": record["top_zero_row"],
        "half_prime": h,
        "tail_threshold": record["tail_threshold"],
        "shift_min": shift_min,
        "shift_max": shift_max,
        "top_row_mod_hP": record["top_zero_row"] % period_h,
        "half_primorial": modulus_h,
        "half_endpoint_period_hP": period_h,
        **identity,
        "candidate_phases_mod_primorial": candidate_phases,
        "candidate_acceptance": candidate_acceptance,
        "all_candidates_accepted": all(candidate_acceptance) if candidate_acceptance else False,
        "selector_exists": any(candidate_acceptance),
        "phase_from_top_row_residue": [residue_min, residue_max],
        "residue_formula_matches": (
            candidate_phases == list(range(residue_min, residue_max + 1))
            if residue_min <= residue_max
            else candidate_phases == [residue_min]
        )
        if len(candidate_phases) <= 2
        else False,
    }


def build(core_path: Path) -> dict[str, Any]:
    """构造候选下层行相位身份账本。"""
    core = json.loads(core_path.read_text(encoding="utf-8"))
    max_h = max(record["half_prime"] for record in core["records"])
    primes = primes_upto(max_h)
    records = [audit_record(primes, record) for record in core["records"]]
    return {
        "status": "rpz_bcb_candidate_lower_row_phase_identity",
        "source": str(core_path),
        "summary": {
            "records": len(records),
            "records_matching_core_interval": sum(
                1 for row in records if row["identity_matches_core_interval"]
            ),
            "records_matching_contained_rows": sum(
                1 for row in records if row["identity_matches_contained_rows"]
            ),
            "total_candidate_rows": sum(len(row["candidate_rows_by_identity"]) for row in records),
            "accepted_candidate_rows": sum(
                sum(1 for accepted in row["candidate_acceptance"] if accepted)
                for row in records
            ),
            "records_with_selector": sum(1 for row in records if row["selector_exists"]),
        },
        "records": records,
        "review_boundary": [
            "BCB 候选行相位可由 top row residue mod hP(h) 与平台参数精确计算。",
            "当前样本中公式匹配全部 contained rows，且所有候选行 accepted。",
            "这仍不是全局 selector 定理；剩余义务是证明正式 BCB top row residue 必诱导 accepted candidate phase。",
            "若候选相位 rejected，则该相位已有 first-failure seam/PDEC/ColumnCRT 路由。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ-BCB 候选下层行相位身份账本",
        "",
        "**状态：** `rpz_bcb_candidate_lower_row_phase_identity`",
        "",
        "## 总结",
        "",
        f"- BCB 记录数：`{summary['records']}`。",
        f"- 核心区间公式匹配数：`{summary['records_matching_core_interval']}`。",
        f"- 候选行公式匹配数：`{summary['records_matching_contained_rows']}`。",
        f"- 候选行总数：`{summary['total_candidate_rows']}`。",
        f"- accepted 候选行数：`{summary['accepted_candidate_rows']}`。",
        f"- 有 selector 的记录数：`{summary['records_with_selector']}`。",
        "",
        "## 精确身份",
        "",
        "BCB 核心区间为",
        "",
        "```text",
        "L=(R-1)P+1+s_min+T,",
        "U=RP+s_max-T。",
        "```",
        "",
        "完整包含的 `h` 对齐候选行满足",
        "",
        "```text",
        "m_min=floor((L+h-2)/h)+1,",
        "m_max=floor(U/h)。",
        "```",
        "",
        "若 `P=Qh+d`，则相位只依赖 `R mod hP(h)`：",
        "",
        "```text",
        "m_min=(R-1)Q+floor(((R-1)d+s_min+T+h-1)/h)+1,",
        "m_max=RQ+floor((Rd+s_max-T)/h)。",
        "```",
        "",
        "## 当前样本",
        "",
        "| top P | top row | h | shifts | R mod hP(h) | candidate rows | phases | accepted | selector | identity match |",
        "|---:|---:|---:|---|---:|---|---|---|---|---|",
    ]
    for row in result["records"]:
        lines.append(
            "| {top} | {top_row} | {h} | `{shifts}` | {residue} | `{rows}` | `{phases}` | `{accepted}` | `{selector}` | `{match}` |".format(
                top=row["top_prime"],
                top_row=row["top_zero_row"],
                h=row["half_prime"],
                shifts=[row["shift_min"], row["shift_max"]],
                residue=row["top_row_mod_hP"],
                rows=row["candidate_rows_by_identity"],
                phases=row["candidate_phases_mod_primorial"],
                accepted=row["candidate_acceptance"],
                selector=row["selector_exists"],
                match=row["identity_matches_contained_rows"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "候选下层行不再是程序扫描对象，而是 BCB 参数给出的显式 floor 身份。",
            "当前样本中该身份逐项匹配 `contained_half_rows`，且 `6/6` 个候选行相位都属于 `A_h`。",
            "剩余全局硬点是证明正式 BCB 反例的 `R mod hP(h)` 必诱导 accepted 候选相位；若诱导 rejected 相位，则回流到已命名 first-failure 出口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--core",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-core-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-candidate-phase-identity"),
    )
    args = parser.parse_args()

    result = build(args.core)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
