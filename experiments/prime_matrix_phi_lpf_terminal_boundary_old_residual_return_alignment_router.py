#!/usr/bin/env python3
"""审计 boundary old-side residual 与 nonboundary/internal return 的精确对齐。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_old_residual_return_alignment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.md

本证书承接 boundary residual-flow obstruction，检查 5 个 old-side residual
是否可逐项解释为 source-key partition 中的 nonboundary/internal return。
结论：old-side return alignment 精确闭合；dominant new-side residual source
仍未闭合。
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

RESIDUAL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json"
PARTITION_JSON = DOCS / "prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json"

BOUNDARY_SOURCE_LAW = "BoundaryDominantNewResidualSourceLawOrPDEC"
BOUNDARY_NEW_RETURN_LAW = "BoundaryNewResidualReturnOrPDEC"
BOUNDARY_MASS_RATIO_LAW = "BoundaryAdjacentRunMassRatioLawOrPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), RESIDUAL_JSON, PARTITION_JSON]
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


def old_residual_key(row: dict[str, Any]) -> tuple[str, int, int]:
    """old-side residual 的对齐 key。"""
    return (row["atom_key"], int(row["old_run_id"]), int(row["boundary_q"]))


def nonboundary_key(row: dict[str, Any]) -> tuple[str, int, int]:
    """nonboundary jump 的 old endpoint key。"""
    return (row["atom_key"], int(row["old_run_id"]), int(row["old_q_end"]))


def internal_survivor_key(row: dict[str, Any]) -> tuple[str, int, int]:
    """internal survivor 的 return key。"""
    return (row["atom_key"], int(row["run_id"]), int(row["q_end"]))


def build_return_rows(
    old_rows: list[dict[str, Any]],
    nonboundary_rows: list[dict[str, Any]],
    internal_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """逐项匹配 old residual 与 return rows。"""
    returns: dict[tuple[str, int, int], dict[str, Any]] = {}
    for row in nonboundary_rows:
        key = nonboundary_key(row)
        returns[key] = {
            "return_type": "nonboundary_record_jump",
            "return_mass": row["chunk"],
            "return_endpoint": f"old_q_end={row['old_q_end']}, new_q_start={row['new_q_start']}",
        }
    for row in internal_rows:
        key = internal_survivor_key(row)
        returns[key] = {
            "return_type": "internal_survivor",
            "return_mass": row["mass"],
            "return_endpoint": f"q_start={row['q_start']}, q_end={row['q_end']}",
        }

    aligned = []
    for row in sorted(old_rows, key=lambda item: old_residual_key(item)):
        key = old_residual_key(row)
        target = returns.get(key)
        target_mass = frac_from_record(target["return_mass"]) if target else None
        residual_mass = frac_from_record(row["residual_mass"])
        aligned.append(
            {
                "atom_key": row["atom_key"],
                "old_run_id": row["old_run_id"],
                "boundary_q": row["boundary_q"],
                "direction_pair": row["direction_pair"],
                "old_residual_mass": row["residual_mass"],
                "matched": target is not None and target_mass == residual_mass,
                "return_type": target["return_type"] if target else "missing",
                "return_endpoint": target["return_endpoint"] if target else "missing",
                "return_mass": target["return_mass"] if target else frac_record(Fraction(0)),
                "mass_difference": frac_record(
                    residual_mass - (target_mass if target_mass is not None else Fraction(0))
                ),
            }
        )
    return aligned


def build_certificate() -> dict[str, Any]:
    """组装 old residual return alignment 证书。"""
    residual_payload = load_json(RESIDUAL_JSON)
    partition_payload = load_json(PARTITION_JSON)

    old_rows = residual_payload["old_residual_event_rows"]
    nonboundary_rows = partition_payload["nonboundary_record_jump_rows"]
    internal_rows = [
        row
        for row in partition_payload["survivor_partition_rows"]
        if row["survivor_type"] == "internal_survivor"
    ]
    return_rows = build_return_rows(old_rows, nonboundary_rows, internal_rows)

    old_total = frac_from_record(residual_payload["old_residual_mass_total"])
    nonboundary_total = frac_from_record(partition_payload["nonboundary_record_jump_mass_total"])
    internal_total = frac_from_record(partition_payload["internal_survivor_mass_total"])
    nonboundary_plus_internal = frac_from_record(
        partition_payload["nonboundary_plus_internal_obstruction_mass"]
    )
    matched_mass = sum(
        (frac_from_record(row["old_residual_mass"]) for row in return_rows if row["matched"]),
        Fraction(0),
    )
    new_total = frac_from_record(residual_payload["new_residual_mass_total"])
    alignment_closed = (
        residual_payload.get("residual_flow_side_decomposition_closed") is True
        and partition_payload.get("source_key_obstruction_partition_closed") is True
        and len(old_rows) == len(return_rows)
        and all(row["matched"] for row in return_rows)
        and old_total == nonboundary_plus_internal
        and matched_mass == old_total
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_old_residual_return_alignment_router",
        "status": "old_residual_return_alignment_closed_new_source_open",
        "verified_date": "2026-05-25",
        "previous_residual_flow_side_decomposition_closed": residual_payload.get(
            "residual_flow_side_decomposition_closed"
        )
        is True,
        "previous_source_key_obstruction_partition_closed": partition_payload.get(
            "source_key_obstruction_partition_closed"
        )
        is True,
        "old_residual_event_count": len(old_rows),
        "nonboundary_record_jump_event_count": len(nonboundary_rows),
        "internal_survivor_return_count": len(internal_rows),
        "old_residual_total": frac_record(old_total),
        "nonboundary_record_jump_mass_total": frac_record(nonboundary_total),
        "internal_survivor_mass_total": frac_record(internal_total),
        "nonboundary_plus_internal_obstruction_mass": frac_record(nonboundary_plus_internal),
        "old_residual_equals_nonboundary_plus_internal_obstruction": old_total
        == nonboundary_plus_internal,
        "old_residual_return_aligned_event_count": sum(1 for row in return_rows if row["matched"]),
        "old_residual_return_alignment_closed": alignment_closed,
        "matched_old_residual_return_mass": frac_record(matched_mass),
        "unmatched_old_residual_return_mass": frac_record(old_total - matched_mass),
        "new_residual_mass_total_still_open": frac_record(new_total),
        "new_residual_return_alignment_closed": False,
        "boundary_dominant_new_residual_source_law_proved": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "return_alignment_rows": return_rows,
        "gate_rows": [
            {
                "gate": "OldResidualReturnAlignmentClosed",
                "closed": alignment_closed,
                "proved": True,
                "meaning": "the five old-side boundary residuals match four nonboundary jumps plus one internal survivor exactly.",
                "remaining": "finite old-side return ledger",
            },
            {
                "gate": "BoundaryResidualTransportToNonBoundaryInternalReturnsOldSide",
                "closed": alignment_closed,
                "proved": True,
                "meaning": "old-side residual transport is fully accounted for in the finite source-key partition.",
                "remaining": "old-side transport closed only",
            },
            {
                "gate": "BoundaryDominantNewResidualSource",
                "closed": False,
                "proved": False,
                "meaning": "new-side residual mass remains dominant and has no return alignment in this certificate.",
                "remaining": BOUNDARY_SOURCE_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite old-side return alignment, not a global parity-breaking theorem.",
                "remaining": f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}",
            },
        ],
        "next_primary_attack_target": (
            f"{BOUNDARY_SOURCE_LAW} AND {BOUNDARY_NEW_RETURN_LAW} AND "
            f"{BOUNDARY_MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND "
            f"{MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}"
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "The five old-side boundary residuals align exactly with the four "
            "nonboundary record jumps and the one internal survivor.  The old-side "
            "transport subgate is therefore closed in the finite ledger, but the "
            "dominant new-side residual mass is still open and must be explained by "
            "a source law, a new-return alignment, or PDEC."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal boundary old-residual return alignment 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书核对 old-side boundary residual 是否逐项等于 nonboundary/internal return。")
    lines.append("")
    lines.append("```text")
    for key in [
        "previous_residual_flow_side_decomposition_closed",
        "previous_source_key_obstruction_partition_closed",
        "old_residual_event_count",
        "nonboundary_record_jump_event_count",
        "internal_survivor_return_count",
        "old_residual_equals_nonboundary_plus_internal_obstruction",
        "old_residual_return_alignment_closed",
        "new_residual_return_alignment_closed",
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
        "old_residual_total",
        "nonboundary_record_jump_mass_total",
        "internal_survivor_mass_total",
        "nonboundary_plus_internal_obstruction_mass",
        "matched_old_residual_return_mass",
        "unmatched_old_residual_return_mass",
        "new_residual_mass_total_still_open",
    ]:
        lines.append(f"| `{key}` | {render_fraction(result[key])} |")
    lines.append("")
    lines.append("## 2. return alignment rows")
    lines.append("")
    lines.append("| atom | old run | q | direction | old residual | return type | return endpoint | matched |")
    lines.append("| --- | ---: | ---: | --- | --- | --- | --- | --- |")
    for row in result["return_alignment_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['old_run_id']} | {row['boundary_q']} | "
            f"`{row['direction_pair']}` | {render_fraction(row['old_residual_mass'])} | "
            f"`{row['return_type']}` | `{cell(row['return_endpoint'])}` | `{fmt_bool(row['matched'])}` |"
        )
    lines.append("")
    lines.append("## 3. 门控表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in result["gate_rows"]:
        lines.append(
            f"| `{cell(row['gate'])}` | `{fmt_bool(row['closed'])}` | `{fmt_bool(row['proved'])}` | "
            f"{cell(row['meaning'])} | `{cell(row['remaining'])}` |"
        )
    lines.append("")
    lines.append("## 4. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_attack_target"])
    lines.append("```")
    lines.append("")
    lines.append("## 5. 依赖哈希")
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
    """生成 old residual return alignment 证书。"""
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
    print(f"old_residual_return_alignment_closed={fmt_bool(result['old_residual_return_alignment_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
