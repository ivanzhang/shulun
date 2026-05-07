#!/usr/bin/env python3
"""审计 FO-PDEC 的 fractional Weighted Hall dual 是否能保留嵌套重复。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_weighted_hall_dual_audit.py

输出：
  docs/monograph/prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.json
  docs/monograph/prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.md
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_LOWMOD = DOCS / "prime-matrix-wsh-fo-pdec-lowmod-audit.json"
DEFAULT_TIGHT = DOCS / "prime-matrix-wsh-scb1-long-block-certificate.json"
DEFAULT_NESTED = DOCS / "prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.json"
DEFAULT_JSON = DOCS / "prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.md"


Equation = dict[str, Any]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def best_fourier(rows: Iterable[Equation]) -> dict[str, Any] | None:
    """计算一组方程的最佳单因子 Fourier 投影。"""
    by_factor: defaultdict[int, Counter[int]] = defaultdict(Counter)
    for row in rows:
        by_factor[int(row["explaining_factor"])][int(row["target_residue"])] += 1
    best: dict[str, Any] | None = None
    for factor, counts in by_factor.items():
        best_value = 0.0
        best_frequency = 0
        for frequency in range(1, factor):
            total = 0j
            for residue, load in counts.items():
                total += load * cmath.exp(2j * math.pi * frequency * residue / factor)
            value = abs(total)
            if value > best_value:
                best_value = value
                best_frequency = frequency
        row = {
            "factor": factor,
            "frequency": best_frequency,
            "fourier": best_value,
            "mass": sum(counts.values()),
            "support": len(counts),
            "top_residues": [
                {"residue": residue, "load": load}
                for residue, load in counts.most_common()
            ],
        }
        if best is None or (row["fourier"], row["mass"]) > (
            best["fourier"],
            best["mass"],
        ):
            best = row
    return best


def dedupe(rows: Iterable[Equation], key_fields: tuple[str, ...]) -> list[Equation]:
    """按给定字段去重，保留第一条代表。"""
    seen: set[tuple[Any, ...]] = set()
    result: list[Equation] = []
    for row in rows:
        key = tuple(row[field] for field in key_fields)
        if key in seen:
            continue
        seen.add(key)
        result.append(row)
    return result


def group_best(
    rows: Iterable[Equation],
    group_fields: tuple[str, ...],
    dedupe_fields: tuple[str, ...] | None = None,
) -> dict[str, Any]:
    """按 formal unit 分组并返回最佳组。"""
    groups: defaultdict[tuple[Any, ...], list[Equation]] = defaultdict(list)
    for row in rows:
        groups[tuple(row[field] for field in group_fields)].append(row)
    units = []
    for key, values in sorted(groups.items()):
        effective = dedupe(values, dedupe_fields) if dedupe_fields else list(values)
        units.append(
            {
                "key": list(key),
                "raw_count": len(values),
                "effective_count": len(effective),
                "best": best_fourier(effective),
            }
        )
    best = max(
        (unit for unit in units if unit["best"]),
        key=lambda unit: (unit["best"]["fourier"], unit["best"]["mass"]),
        default=None,
    )
    return {"unit_count": len(units), "best_unit": best, "units": units}


def tight_block_map(tight: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """生成 tight block 索引表。"""
    return {
        index: row
        for index, row in enumerate(tight["tight_long_blocks"], start=1)
    }


def block_pair_increment(
    block_ids: list[int],
    blocks: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    """计算嵌套块差层是否提供新压力。"""
    if len(block_ids) != 2:
        return {
            "status": "not_pair",
            "independent_increment_available": None,
        }
    first = blocks[block_ids[0]]
    second = blocks[block_ids[1]]
    first_support = set(map(int, first["semiprime_values"]))
    second_support = set(map(int, second["semiprime_values"]))
    if first_support >= second_support:
        large_id, small_id = block_ids[0], block_ids[1]
        large, small = first, second
        large_support, small_support = first_support, second_support
    elif second_support >= first_support:
        large_id, small_id = block_ids[1], block_ids[0]
        large, small = second, first
        large_support, small_support = second_support, first_support
    else:
        return {
            "status": "not_laminar",
            "independent_increment_available": True,
        }
    delta_semiprime = len(large_support - small_support)
    delta_prime = int(large["prime_count"]) - int(small["prime_count"])
    delta_surplus = int(large["surplus"]) - int(small["surplus"])
    return {
        "status": "laminar_pair",
        "large_block": large_id,
        "small_block": small_id,
        "large_semiprime_count": int(large["semiprime_count"]),
        "small_semiprime_count": int(small["semiprime_count"]),
        "large_prime_count": int(large["prime_count"]),
        "small_prime_count": int(small["prime_count"]),
        "large_surplus": int(large["surplus"]),
        "small_surplus": int(small["surplus"]),
        "delta_semiprime": delta_semiprime,
        "delta_prime": delta_prime,
        "delta_surplus": delta_surplus,
        "new_semiprimes": sorted(large_support - small_support),
        "independent_increment_available": delta_surplus < 0,
        "dominance_reason": (
            "difference_layer_has_no_new_hall_pressure"
            if delta_surplus >= 0
            else "difference_layer_has_negative_surplus_pressure"
        ),
    }


def nested_weight_rows(
    nested: dict[str, Any],
    tight: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成嵌套重复的加权对偶审计行。"""
    blocks = tight_block_map(tight)
    rows = []
    for row in nested["audited_duplicates"]:
        increment = block_pair_increment(row["block_ids"], blocks)
        full_extra_blocked = (
            row["unit_weight_independence_status"]
            == "blocked_by_same_coordinate_nested_support"
            and increment["status"] == "laminar_pair"
            and not increment["independent_increment_available"]
        )
        rows.append(
            {
                "key": row["key"],
                "block_ids": row["block_ids"],
                "factor": int(row["key"][6]),
                "target_residue": int(row["key"][7]),
                "increment": increment,
                "max_extra_unit_weight_from_laminar_difference": (
                    0.0 if full_extra_blocked else None
                ),
                "full_duplicate_weight_status": (
                    "blocked_by_laminar_zero_pressure_increment"
                    if full_extra_blocked
                    else "requires_external_weighted_dual_proof"
                ),
            }
        )
    return rows


def build_audit(
    lowmod: dict[str, Any],
    tight: dict[str, Any],
    nested: dict[str, Any],
    lowmod_path: Path,
    tight_path: Path,
    nested_path: Path,
) -> dict[str, Any]:
    """构造 weighted Hall dual 审计。"""
    equations: list[Equation] = lowmod["equations"]
    coordinate_fields = (
        "q",
        "source_row",
        "candidate_row",
        "column",
        "offset",
        "candidate",
        "explaining_factor",
        "target_residue",
    )
    physical_fields = ("candidate", "explaining_factor")

    raw_rows = list(equations)
    coordinate_cap_rows = dedupe(equations, coordinate_fields)
    physical_cap_rows = dedupe(equations, physical_fields)
    q_row_best = group_best(equations, ("q", "source_row"), coordinate_fields)
    block_best = group_best(equations, ("block_index",), None)
    nested_rows = nested_weight_rows(nested, tight)

    raw_best = best_fourier(raw_rows)
    coordinate_best = best_fourier(coordinate_cap_rows)
    physical_best = best_fourier(physical_cap_rows)
    all_nested_extra_blocked = all(
        row["full_duplicate_weight_status"]
        == "blocked_by_laminar_zero_pressure_increment"
        for row in nested_rows
    )
    factor_199_rows = [row for row in nested_rows if row["factor"] == 199]
    factor_199_extra_blocked = bool(factor_199_rows) and all(
        row["full_duplicate_weight_status"]
        == "blocked_by_laminar_zero_pressure_increment"
        for row in factor_199_rows
    )
    return {
        "certificate_type": "fo_pdec_weighted_hall_dual_audit",
        "status": "weighted_hall_dual_full_duplicate_weight_blocked_not_global_proof",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "lowmod_audit": file_sha256(lowmod_path),
            "tight_long_block_certificate": file_sha256(tight_path),
            "nested_duplicate_dominance": file_sha256(nested_path),
        },
        "mode_comparison": [
            {
                "mode": "global_library_raw",
                "formal_status": "diagnostic_only",
                "rows": len(raw_rows),
                "best": raw_best,
            },
            {
                "mode": "nested_coordinate_cap",
                "formal_status": "allows_cross_q_but_rejects_same_coordinate_duplicate_unit_weight",
                "rows": len(coordinate_cap_rows),
                "best": coordinate_best,
            },
            {
                "mode": "physical_candidate_cap",
                "formal_status": "dedupes_cross_q_same_physical_candidate",
                "rows": len(physical_cap_rows),
                "best": physical_best,
            },
            {
                "mode": "single_q_row_coordinate_cap",
                "formal_status": "single_formal_branch",
                "rows": q_row_best["best_unit"]["effective_count"] if q_row_best["best_unit"] else 0,
                "best": q_row_best["best_unit"]["best"] if q_row_best["best_unit"] else None,
                "unit": q_row_best["best_unit"]["key"] if q_row_best["best_unit"] else None,
            },
            {
                "mode": "single_block",
                "formal_status": "single_hall_block",
                "rows": block_best["best_unit"]["effective_count"] if block_best["best_unit"] else 0,
                "best": block_best["best_unit"]["best"] if block_best["best_unit"] else None,
                "unit": block_best["best_unit"]["key"] if block_best["best_unit"] else None,
            },
        ],
        "nested_weight_rows": nested_rows,
        "all_nested_full_extra_unit_weight_blocked": all_nested_extra_blocked,
        "factor_199_full_extra_unit_weight_blocked": factor_199_extra_blocked,
        "closed_subgate": (
            "FractionalWeightedHallCannotRecoverFullNestedDuplicateMass"
            if all_nested_extra_blocked
            else "FractionalWeightedHallStillNeedsExternalIndependenceCase"
        ),
        "remaining_after_subgate": [
            "coordinate-cap PDEC threshold using the 2.9698366905785227-level signal if cross-q persistence is proved",
            "physical-cap / primitive PDEC threshold using the 1.9997507790353146-level signal",
            "single-branch PDEC or SAE/Endpoint absorption when cross-q persistence is rejected",
            "independent non-laminar weighted dual proof, if a future branch supplies one",
        ],
        "review_conclusion": (
            "当前 FO-PDEC 嵌套重复的分数加权对偶不能恢复完整第二单位质量。"
            "每个重复来自同一正式坐标，且大小 Hall 块是 laminar 嵌套；差层只增加同数目的半素数和素数，"
            "surplus 增量为 0，没有新的 Hall 压力。因此 raw 3.959... 必须降到坐标 cap 口径；"
            "若 cross-q persistence 不成立，还要继续降到 primitive/单分支口径。"
        ),
    }


def fmt_best(best: dict[str, Any] | None) -> str:
    """格式化最佳 Fourier 数据。"""
    if not best:
        return "-"
    return (
        f"ell={best['factor']}, h={best['frequency']}, "
        f"Fourier={best['fourier']:.12f}, mass={best['mass']}, support={best['support']}"
    )


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    lines = [
        "# FO-PDEC fractional Weighted Hall dual 审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 子门裁定",
        "",
        "```text",
        f"closed_subgate: {result['closed_subgate']}",
        (
            "all_nested_full_extra_unit_weight_blocked: "
            f"{str(result['all_nested_full_extra_unit_weight_blocked']).lower()}"
        ),
        (
            "factor_199_full_extra_unit_weight_blocked: "
            f"{str(result['factor_199_full_extra_unit_weight_blocked']).lower()}"
        ),
        "```",
        "",
        "## 2. 口径比较",
        "",
        "| mode | formal status | rows | best Fourier projection |",
        "| --- | --- | ---: | --- |",
    ]
    for row in result["mode_comparison"]:
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    row["mode"],
                    row["formal_status"],
                    row["rows"],
                    fmt_best(row["best"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 嵌套差层审计",
            "",
            "| key | blocks | delta semiprime | delta prime | delta surplus | conclusion |",
            "| --- | --- | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["nested_weight_rows"]:
        inc = row["increment"]
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    row["key"],
                    row["block_ids"],
                    inc.get("delta_semiprime"),
                    inc.get("delta_prime"),
                    inc.get("delta_surplus"),
                    row["full_duplicate_weight_status"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明读法",
            "",
            "加权 Hall 对偶若要把同一坐标重复计两次，必须证明第二个权重来自独立差层。"
            "但本审计中的嵌套差层不含这个重复坐标，并且只增加一个新半素数和一个新素数，"
            "Hall surplus 不下降。因此差层没有新的缺陷压力可支付重复坐标的第二单位质量。",
            "",
            "这不是全局 PDEC 排斥。它只排除了当前最强 `global_library_raw` 信号中"
            "“嵌套重复靠分数加权恢复完整第二单位质量”的路线。",
            "",
            "## 5. 剩余",
            "",
        ]
    )
    for item in result["remaining_after_subgate"]:
        lines.append(f"- `{item}`")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lowmod", type=Path, default=DEFAULT_LOWMOD)
    parser.add_argument("--tight", type=Path, default=DEFAULT_TIGHT)
    parser.add_argument("--nested", type=Path, default=DEFAULT_NESTED)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    lowmod = load_json(args.lowmod)
    tight = load_json(args.tight)
    nested = load_json(args.nested)
    result = build_audit(lowmod, tight, nested, args.lowmod, args.tight, args.nested)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["closed_subgate"])


if __name__ == "__main__":
    main()
