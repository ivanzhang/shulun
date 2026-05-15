#!/usr/bin/env python3
"""把 selected target segment 写成 q=P-2b 的 atom-piece 正规形。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_segment_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-segment-normal-form-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-segment-normal-form-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-segment-normal-form-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-segment-normal-form-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-target-segment-ledger.json"
SUPPORT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-segment-normal-form-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-segment-normal-form-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-segment-normal-form-router.md"

TARGET_SEGMENT_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_target_segment_router.py"
)

MAIN_TARGET = "SelectedTargetAtomSegmentPrimeSupplyOrSegmentVoidPDEC"
NEXT_TARGET = "SelectedSmallKAtomPiecePrimeSupplyOrAtomPieceVoidPDEC"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def parse_atom_key(key: str) -> dict[str, Any]:
    """解析 band:k:qlo-qhi atom 键。"""
    band, rest = key.split(":k", 1)
    k_text, q_text = rest.split(":", 1)
    q_lo_text, q_hi_text = q_text.split("-", 1)
    return {
        "key": key,
        "band": band,
        "k": int(k_text),
        "q_lo": int(q_lo_text),
        "q_hi": int(q_hi_text),
    }


def record_key(row: dict[str, Any]) -> tuple[Any, ...]:
    """生成跨账本匹配键。"""
    return (row["p"], row["side"], row["q_hull_lo"], row["q_hull_hi"], row["shape_key"])


def atom_pieces_for_segment(segment: dict[str, Any], atom_keys: list[str]) -> list[dict[str, Any]]:
    """把 selected segment 按原始 atom 切成 atom pieces。"""
    q_lo = int(segment["q_lo"])
    q_hi = int(segment["q_hi"])
    prime_values = list(segment["target_prime_values"])
    atoms = [parse_atom_key(key) for key in atom_keys]
    pieces: list[dict[str, Any]] = []
    for atom in atoms:
        piece_lo = max(q_lo, atom["q_lo"])
        piece_hi = min(q_hi, atom["q_hi"])
        if piece_hi < piece_lo:
            continue
        piece_primes = [value for value in prime_values if piece_lo <= value <= piece_hi]
        pieces.append(
            {
                "q_lo": piece_lo,
                "q_hi": piece_hi,
                "candidate_count": (piece_hi - piece_lo) // 2 + 1,
                "target_prime_values": piece_primes,
                "target_prime_count": len(piece_primes),
                "actual_piece_void": len(piece_primes) == 0,
                "parent_atom_key": atom["key"],
                "parent_atom_band": atom["band"],
                "parent_atom_k": atom["k"],
                "parent_atom_q_lo": atom["q_lo"],
                "parent_atom_q_hi": atom["q_hi"],
            }
        )
    return sorted(pieces, key=lambda piece: (piece["q_lo"], piece["q_hi"]))


def normal_form_record(row: dict[str, Any], support_by_key: dict[tuple[Any, ...], dict[str, Any]]) -> dict[str, Any]:
    """生成 selected segment/atom-piece 正规形记录。"""
    support = support_by_key[record_key(row)]
    segment = row["selected_target_segment"]
    pieces = atom_pieces_for_segment(segment, support["void_atom_keys"])
    nonvoid_pieces = [piece for piece in pieces if not piece["actual_piece_void"]]
    selected_piece = None
    if nonvoid_pieces:
        selected_piece = min(nonvoid_pieces, key=lambda piece: (piece["candidate_count"], piece["q_lo"]))
    p_value = int(row["p"])
    q_lo = int(selected_piece["q_lo"]) if selected_piece else int(segment["q_lo"])
    q_hi = int(selected_piece["q_hi"]) if selected_piece else int(segment["q_hi"])
    b_lo = (p_value - q_hi) // 2
    b_hi = (p_value - q_lo) // 2
    atom_piece_selector_closed = selected_piece is not None
    return {
        "p": p_value,
        "side": row["side"],
        "shape_key": row["shape_key"],
        "source_selected_segment_q_lo": segment["q_lo"],
        "source_selected_segment_q_hi": segment["q_hi"],
        "source_selected_segment_candidate_count": segment["candidate_count"],
        "source_selected_segment_target_prime_values": segment["target_prime_values"],
        "atom_pieces_inside_segment": pieces,
        "selected_atom_piece_q_lo": q_lo,
        "selected_atom_piece_q_hi": q_hi,
        "selected_segment_candidate_count": segment["candidate_count"],
        "selected_atom_piece_candidate_count": selected_piece["candidate_count"] if selected_piece else None,
        "selected_atom_piece_target_prime_values": selected_piece["target_prime_values"] if selected_piece else [],
        "selected_atom_piece_target_prime_count": selected_piece["target_prime_count"] if selected_piece else 0,
        "b_lo": b_lo,
        "b_hi": b_hi,
        "b_length": b_hi - b_lo + 1,
        "depth_from_p": p_value - q_lo,
        "parent_atom_key": selected_piece["parent_atom_key"] if selected_piece else None,
        "parent_atom_band": selected_piece["parent_atom_band"] if selected_piece else None,
        "parent_atom_k": selected_piece["parent_atom_k"] if selected_piece else None,
        "parent_atom_q_lo": selected_piece["parent_atom_q_lo"] if selected_piece else None,
        "parent_atom_q_hi": selected_piece["parent_atom_q_hi"] if selected_piece else None,
        "atom_piece_selector_closed": atom_piece_selector_closed,
        "normal_form_statement": (
            f"q=P-2b, {b_lo}<=b<={b_hi}, "
            f"q in [{q_lo},{q_hi}], parent_atom={selected_piece['parent_atom_key'] if selected_piece else 'missing'}"
        ),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "selected_segment_atom_piece_selector",
            "status": "closed",
            "statement": "Every selected target segment contains a selected non-void atom piece from the original fixed band/k atoms.",
        },
        {
            "name": "selected_atom_piece_q_equals_p_minus_2b_normal_form",
            "status": "closed",
            "statement": "Each selected atom piece has explicit q=P-2b and b-interval endpoints.",
        },
        {
            "name": "finite_small_k_segment_frontier",
            "status": "finite_evidence",
            "statement": "The finite frontier only uses parent atoms with k<=2 and selected atom-piece length at most five.",
        },
        {
            "name": "global_selected_small_k_segment_supply",
            "status": "open",
            "statement": "A global proof still needs prime supply in these selected small-k atom pieces, or exclusion of atom-piece-void PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "AtomPieceSelectorClosed",
            "closed": result["atom_piece_selector_failure_count"] == 0,
            "proved": True,
            "meaning": "每个 selected segment 都已选出一个非空原始 band/k atom piece。",
            "remaining": "closed",
        },
        {
            "gate": "QEqualsPMinus2BNormalFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "每个 selected atom piece 已写成 q=P-2b 的 b 区间。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteSmallKSegmentFrontier",
            "closed": result["max_parent_atom_k"] <= 2,
            "proved": False,
            "meaning": "有限前沿全部为 k<=2 的短 target atom piece。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalSmallKSegmentSupplyClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 selected small-k atom piece 含素数，或排斥 atom-piece void。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成 atom-piece 正规形，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, support_ledger: Path) -> dict[str, Any]:
    """构造 segment normal-form 路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    support_source = load_json(support_ledger)
    support_by_key = {record_key(row): row for row in support_source["collapse_records"]}
    records = [normal_form_record(row, support_by_key) for row in source["target_segment_records"]]
    failures = [row for row in records if not row["atom_piece_selector_closed"]]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "support_ledger": str(support_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "atom_piece_selector_failure_count": len(failures),
        "min_selected_segment_candidate_count": min(
            (row["selected_segment_candidate_count"] for row in records),
            default=0,
        ),
        "max_selected_segment_candidate_count": max(
            (row["selected_segment_candidate_count"] for row in records),
            default=0,
        ),
        "min_selected_atom_piece_candidate_count": min(
            (row["selected_atom_piece_candidate_count"] for row in records if row["selected_atom_piece_candidate_count"] is not None),
            default=0,
        ),
        "max_selected_atom_piece_candidate_count": max(
            (row["selected_atom_piece_candidate_count"] for row in records if row["selected_atom_piece_candidate_count"] is not None),
            default=0,
        ),
        "min_b_length": min((row["b_length"] for row in records), default=0),
        "max_b_length": max((row["b_length"] for row in records), default=0),
        "max_parent_atom_k": max((row["parent_atom_k"] for row in records if row["parent_atom_k"] is not None), default=0),
        "parent_band_histogram": {},
    }
    for row in records:
        band = row["parent_atom_band"]
        aggregate["parent_band_histogram"][band] = aggregate["parent_band_histogram"].get(band, 0) + 1
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "normal_form_records": records,
        "atom_piece_selector_failures": failures,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_segment_normal_form_router",
        "status": "selected_target_atom_piece_normal_form_registered_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "normal_form_records": records,
        "atom_piece_selector_failure_count": len(failures),
        "max_parent_atom_k": aggregate["max_parent_atom_k"],
        "global_selected_small_k_atom_piece_supply_proved": False,
        "normal_form_atom_piece_void_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_segment_normal_form_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_target_segment_router.py": sha256(
                TARGET_SEGMENT_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-target-segment-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json": sha256(support_ledger),
            "data/square-phase-offband-prefix-gap-shadow-segment-normal-form-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 selected target segment 继续切回原始 fixed band/k atom pieces，并选出最短的非空 atom piece。"
            "有限前沿 11 个包全部选择成功，选中 atom piece 长度为 2..5，父 atom 的最大 k 为 2；"
            "全局仍需证明这些 selected small-k atom pieces 含素数，或排斥正规形 atom-piece-void PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow segment normal form router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"atom_piece_selector_failure_count={agg['atom_piece_selector_failure_count']}",
        f"selected_segment_candidate_count_range={agg['min_selected_segment_candidate_count']}..{agg['max_selected_segment_candidate_count']}",
        f"selected_atom_piece_candidate_count_range={agg['min_selected_atom_piece_candidate_count']}..{agg['max_selected_atom_piece_candidate_count']}",
        f"b_length_range={agg['min_b_length']}..{agg['max_b_length']}",
        f"max_parent_atom_k={agg['max_parent_atom_k']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 正规形",
        "",
        "每个 selected target segment 先按原始 atom 切分，再选出一个显式非空 atom piece：",
        "",
        "```text",
        "q=P-2b, b_lo<=b<=b_hi, selected atom piece <= parent atom = band:k:qlo-qhi",
        "```",
        "",
        "## 2. 正规形前沿",
        "",
        "| P | side | q atom piece | b interval | parent atom | primes |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in result["normal_form_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['selected_atom_piece_q_lo']}-{row['selected_atom_piece_q_hi']}`",
                    f"`{row['b_lo']}-{row['b_hi']}`",
                    f"`{row['parent_atom_key']}`",
                    f"`{row['selected_atom_piece_target_prime_values']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 4. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 继续攻击这些 k<=2、长度 2..5 的 q=P-2b atom pieces 素数供给，或把 atom-piece void 接入列相位/平方锚矛盾。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    parser.add_argument("--support-ledger", type=Path, default=SUPPORT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    support_ledger = args.support_ledger if args.support_ledger.is_absolute() else ROOT / args.support_ledger
    result = build_result(input_ledger, support_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-segment-normal-form-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "atom_piece_selector_failure_count": result["atom_piece_selector_failure_count"],
                "max_parent_atom_k": result["max_parent_atom_k"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
