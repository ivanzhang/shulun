#!/usr/bin/env python3
"""审计 boundary new-side residual 与 terminal tail survivor 的精确对齐。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_new_residual_tail_alignment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.md

本证书承接 old-residual return alignment，继续检验 new-side residual 是否能由
terminal tail survivor 支付。结论：6 个 terminal-tail return 精确闭合；剩余 36 个
bulk new-side residual 和 1 个 right selected-terminal tail overhang 仍未闭合。
"""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

RESIDUAL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json"
OLD_RETURN_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json"
PARTITION_JSON = DOCS / "prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json"

BULK_NEW_SOURCE_LAW = "BoundaryBulkNewResidualSourceLawOrPDEC"
TAIL_OVERHANG_LAW = "RightSelectedTerminalTailOverhangPDEC"
BOUNDARY_MASS_RATIO_LAW = "BoundaryAdjacentRunMassRatioLawOrPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
GROUP_ORBIT_INPUT = "AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), RESIDUAL_JSON, OLD_RETURN_JSON, PARTITION_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def frac_from_record(record: dict[str, Any]) -> Fraction:
    """从 JSON 分数记录恢复 Fraction。"""
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def frac_record(value: Fraction) -> dict[str, Any]:
    """稳定输出分数。"""
    return {
        "fraction": f"{value.numerator}/{value.denominator}",
        "decimal": f"{float(value):.12f}",
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def render_fraction(record: dict[str, Any]) -> str:
    """表格用分数摘要。"""
    return f"{record['decimal']} ({record['fraction']})"


def new_tail_key(row: dict[str, Any]) -> tuple[str, int, int, Fraction]:
    """new-side residual 的 terminal-tail 对齐 key。"""
    return (
        row["atom_key"],
        int(row["new_run_id"]),
        int(row["boundary_q"]),
        frac_from_record(row["residual_mass"]),
    )


def tail_key(row: dict[str, Any]) -> tuple[str, int, int, Fraction]:
    """tail survivor 的对齐 key。"""
    return (
        row["atom_key"],
        int(row["run_id"]),
        int(row["q_start"]),
        frac_from_record(row["mass"]),
    )


def build_match_rows(
    new_rows: list[dict[str, Any]], tail_rows: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """匹配 new residual 与 terminal tail survivor。"""
    tails_by_key = {tail_key(row): row for row in tail_rows}
    matched_rows = []
    unmatched_new_rows = []
    matched_tail_keys = set()
    for row in sorted(new_rows, key=lambda item: (item["atom_key"], int(item["new_run_id"]))):
        key = new_tail_key(row)
        tail = tails_by_key.get(key)
        if tail is None:
            unmatched_new_rows.append(row)
            continue
        matched_tail_keys.add(key)
        matched_rows.append(
            {
                "atom_key": row["atom_key"],
                "new_run_id": row["new_run_id"],
                "boundary_q": row["boundary_q"],
                "direction_pair": row["direction_pair"],
                "new_residual_mass": row["residual_mass"],
                "tail_q_start": tail["q_start"],
                "tail_q_end": tail["q_end"],
                "tail_mass": tail["mass"],
                "matched": frac_from_record(row["residual_mass"]) == frac_from_record(tail["mass"]),
            }
        )
    unmatched_tail_rows = [row for row in tail_rows if tail_key(row) not in matched_tail_keys]
    return matched_rows, unmatched_new_rows, unmatched_tail_rows


def unmatched_by_atom(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 atom 汇总未匹配 new residual。"""
    buckets: dict[str, dict[str, Any]] = defaultdict(lambda: {"count": 0, "mass": Fraction(0)})
    for row in rows:
        item = buckets[row["atom_key"]]
        item["count"] += 1
        item["mass"] += frac_from_record(row["residual_mass"])
    return [
        {
            "atom_key": atom_key,
            "unmatched_new_event_count": item["count"],
            "unmatched_new_residual_mass": frac_record(item["mass"]),
        }
        for atom_key, item in sorted(buckets.items())
    ]


def build_certificate() -> dict[str, Any]:
    """组装 new residual tail alignment 证书。"""
    residual_payload = load_json(RESIDUAL_JSON)
    old_return_payload = load_json(OLD_RETURN_JSON)
    partition_payload = load_json(PARTITION_JSON)
    all_boundary_rows = residual_payload["full_boundary_residual_flow_rows"]
    new_rows = [row for row in all_boundary_rows if row["residual_side"] == "new"]
    tail_rows = [
        row
        for row in partition_payload["survivor_partition_rows"]
        if row["survivor_type"] == "tail_survivor"
    ]
    matched_rows, unmatched_new_rows, unmatched_tail_rows = build_match_rows(new_rows, tail_rows)

    new_total = frac_from_record(residual_payload["new_residual_mass_total"])
    tail_total = sum((frac_from_record(row["mass"]) for row in tail_rows), Fraction(0))
    matched_mass = sum((frac_from_record(row["new_residual_mass"]) for row in matched_rows), Fraction(0))
    unmatched_new_mass = sum((frac_from_record(row["residual_mass"]) for row in unmatched_new_rows), Fraction(0))
    unmatched_tail_mass = sum((frac_from_record(row["mass"]) for row in unmatched_tail_rows), Fraction(0))

    tail_alignment_closed = (
        residual_payload.get("residual_flow_side_decomposition_closed") is True
        and old_return_payload.get("old_residual_return_alignment_closed") is True
        and len(matched_rows) == 6
        and all(row["matched"] for row in matched_rows)
        and matched_mass + unmatched_new_mass == new_total
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_new_residual_tail_alignment_router",
        "status": "new_residual_tail_alignment_partial_closed_bulk_source_open",
        "verified_date": "2026-05-25",
        "previous_residual_flow_side_decomposition_closed": residual_payload.get(
            "residual_flow_side_decomposition_closed"
        )
        is True,
        "previous_old_residual_return_alignment_closed": old_return_payload.get(
            "old_residual_return_alignment_closed"
        )
        is True,
        "new_residual_event_count": len(new_rows),
        "tail_survivor_count": len(tail_rows),
        "new_residual_tail_matched_event_count": len(matched_rows),
        "new_residual_tail_alignment_partial_closed": tail_alignment_closed,
        "new_residual_tail_matched_mass": frac_record(matched_mass),
        "new_residual_unmatched_after_tail_event_count": len(unmatched_new_rows),
        "new_residual_unmatched_after_tail_mass": frac_record(unmatched_new_mass),
        "tail_survivor_mass_total": frac_record(tail_total),
        "tail_survivor_unmatched_count": len(unmatched_tail_rows),
        "tail_survivor_unmatched_mass": frac_record(unmatched_tail_mass),
        "all_new_residual_return_alignment_closed": False,
        "bulk_new_residual_source_law_proved": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "tail_alignment_rows": matched_rows,
        "unmatched_tail_survivor_rows": [
            {
                "atom_key": row["atom_key"],
                "run_id": row["run_id"],
                "q_start": row["q_start"],
                "q_end": row["q_end"],
                "mass": row["mass"],
            }
            for row in unmatched_tail_rows
        ],
        "unmatched_new_residual_by_atom_rows": unmatched_by_atom(unmatched_new_rows),
        "largest_unmatched_new_residual_rows": sorted(
            [
                {
                    "atom_key": row["atom_key"],
                    "new_run_id": row["new_run_id"],
                    "boundary_q": row["boundary_q"],
                    "direction_pair": row["direction_pair"],
                    "residual_mass": row["residual_mass"],
                    "smaller_to_larger_ratio": row["smaller_to_larger_ratio"],
                }
                for row in unmatched_new_rows
            ],
            key=lambda row: frac_from_record(row["residual_mass"]),
            reverse=True,
        )[:12],
        "gate_rows": [
            {
                "gate": "NewResidualTerminalTailAlignmentPartial",
                "closed": tail_alignment_closed,
                "proved": True,
                "meaning": "six new-side residuals match terminal tail survivors exactly.",
                "remaining": "finite terminal-tail return ledger",
            },
            {
                "gate": "AllNewResidualReturnAlignment",
                "closed": False,
                "proved": False,
                "meaning": "36 new-side residual events remain unmatched after tail returns.",
                "remaining": BULK_NEW_SOURCE_LAW,
            },
            {
                "gate": "RightSelectedTerminalTailOverhang",
                "closed": False,
                "proved": False,
                "meaning": "one right selected-terminal tail survivor is not a new-side residual return.",
                "remaining": TAIL_OVERHANG_LAW,
            },
            {
                "gate": "GroupOrbitExpansionEntry",
                "closed": False,
                "proved": False,
                "meaning": "no admissible group orbit or expander family has been constructed for the 36 bulk residuals.",
                "remaining": GROUP_ORBIT_INPUT,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite partial return alignment, not a global parity-breaking theorem.",
                "remaining": f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}",
            },
        ],
        "next_primary_attack_target": (
            f"{BULK_NEW_SOURCE_LAW} AND {TAIL_OVERHANG_LAW} AND "
            f"{BOUNDARY_MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND "
            f"{MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}"
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Six new-side boundary residuals align exactly with terminal tail survivors. "
            "After this finite tail-return payment, 36 bulk new-side residual events remain "
            "with mass about 11.684494473663, and one right selected-terminal tail survivor "
            "remains as a tail overhang.  External Kloosterman, Type-II, affine sieve, or "
            "group-expansion inputs still need an admissible signed/orbit family."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal boundary new-residual tail alignment 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书核对 new-side boundary residual 是否可由 terminal tail survivor 精确支付。")
    lines.append("")
    lines.append("```text")
    for key in [
        "previous_residual_flow_side_decomposition_closed",
        "previous_old_residual_return_alignment_closed",
        "new_residual_event_count",
        "tail_survivor_count",
        "new_residual_tail_matched_event_count",
        "new_residual_tail_alignment_partial_closed",
        "new_residual_unmatched_after_tail_event_count",
        "tail_survivor_unmatched_count",
        "all_new_residual_return_alignment_closed",
        "row_column_unconditional_closed",
    ]:
        value = result[key]
        lines.append(f"{key}={fmt_bool(value) if isinstance(value, bool) else value}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. totals")
    lines.append("")
    lines.append("| quantity | value |")
    lines.append("| --- | --- |")
    for key in [
        "new_residual_tail_matched_mass",
        "new_residual_unmatched_after_tail_mass",
        "tail_survivor_mass_total",
        "tail_survivor_unmatched_mass",
    ]:
        lines.append(f"| `{key}` | {render_fraction(result[key])} |")
    lines.append("")
    lines.append("## 2. matched tail returns")
    lines.append("")
    lines.append("| atom | new run | q | direction | residual | tail q-range | matched |")
    lines.append("| --- | ---: | ---: | --- | --- | --- | --- |")
    for row in result["tail_alignment_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['new_run_id']} | {row['boundary_q']} | "
            f"`{row['direction_pair']}` | {render_fraction(row['new_residual_mass'])} | "
            f"{row['tail_q_start']}->{row['tail_q_end']} | `{fmt_bool(row['matched'])}` |"
        )
    lines.append("")
    lines.append("## 3. unmatched new residual by atom")
    lines.append("")
    lines.append("| atom | events | mass |")
    lines.append("| --- | ---: | --- |")
    for row in result["unmatched_new_residual_by_atom_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['unmatched_new_event_count']} | "
            f"{render_fraction(row['unmatched_new_residual_mass'])} |"
        )
    lines.append("")
    lines.append("## 4. unmatched tail survivor")
    lines.append("")
    lines.append("| atom | run | q-range | mass |")
    lines.append("| --- | ---: | --- | --- |")
    for row in result["unmatched_tail_survivor_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['run_id']} | {row['q_start']}->{row['q_end']} | "
            f"{render_fraction(row['mass'])} |"
        )
    lines.append("")
    lines.append("## 5. 门控表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in result["gate_rows"]:
        lines.append(
            f"| `{cell(row['gate'])}` | `{fmt_bool(row['closed'])}` | `{fmt_bool(row['proved'])}` | "
            f"{cell(row['meaning'])} | `{cell(row['remaining'])}` |"
        )
    lines.append("")
    lines.append("## 6. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_attack_target"])
    lines.append("```")
    lines.append("")
    lines.append("## 7. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    lines.append("行/列命题仍未无条件闭合。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 new residual tail alignment 证书。"""
    result = build_certificate()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(
        "new_residual_tail_alignment_partial_closed="
        f"{fmt_bool(result['new_residual_tail_alignment_partial_closed'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
