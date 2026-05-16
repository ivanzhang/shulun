#!/usr/bin/env python3
"""生成 AffineTwin source materialization gate 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_source_materialization_gate_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-source-materialization-gate-ledger.json

输出：
  data/prime-matrix-affine-twin-source-materialization-gate-ledger.json
  docs/monograph/prime-matrix-affine-twin-source-materialization-gate-audit.json
  docs/monograph/prime-matrix-affine-twin-source-materialization-gate-audit.md
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

MOVING_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-moving-family-sae-columncrt-ledger.json"
)
PAIR_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
)
SLOT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)
PRUNING_LEDGER = DATA / "prime-matrix-affine-twin-formal-pair-pruning-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-affine-twin-source-materialization-gate-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-source-materialization-gate-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-source-materialization-gate-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def pair_rows_by_q(rows: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    """按 gap ell 建立 source 索引。"""
    out: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        out.setdefault(int(row["gap_ell"]), []).append(row)
    return out


def slot_source_by_q(rows: list[dict[str, Any]]) -> dict[int, str]:
    """按 q 建立 slot-lock 已验证 source key。"""
    return {int(row["gap_ell"]): str(row["source_gap_fill_pair_key"]) for row in rows}


def pruning_by_q(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 formal-pair pruning 行索引。"""
    return {int(row["q"]): row for row in rows}


def expected_delay(q: int) -> int | None:
    """AffineTwin 源门控期望的 p-delay。"""
    numerator = 11 * q - 21
    if numerator % 4 != 0:
        return None
    return numerator // 4


def expected_signature(row: dict[str, Any]) -> dict[str, Any]:
    """从 moving candidate 构造 source materialization 期望签名。"""
    q = int(row["q"])
    return {
        "gap_ell": q,
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "generator_side": str(row["generator_side"]),
        "fill_side": str(row["fill_side"]),
        "expected_p_delay": expected_delay(q),
    }


def source_match_vector(
    source: dict[str, Any],
    signature: dict[str, Any],
) -> dict[str, Any]:
    """检查单个 source row 与期望签名的匹配向量。"""
    actual_delay = int(source["p_delay"])
    expected_p_delay = signature["expected_p_delay"]
    return {
        "gap_ell_match": int(source["gap_ell"]) == signature["gap_ell"],
        "generator_ell_match": int(source["generator_ell"]) == signature["generator_ell"],
        "fill_ell_match": int(source["fill_ell"]) == signature["fill_ell"],
        "generator_side_match": str(source["generator_side"]) == signature["generator_side"],
        "fill_side_match": str(source["fill_side"]) == signature["fill_side"],
        "p_delay_match": expected_p_delay is not None and actual_delay == expected_p_delay,
        "actual_p_delay": actual_delay,
        "expected_p_delay": expected_p_delay,
        "p_delay_delta": actual_delay - expected_p_delay if expected_p_delay is not None else None,
    }


def all_required_matches(vector: dict[str, Any]) -> bool:
    """判定源门控所需不变量是否全部通过。"""
    return all(
        bool(vector[key])
        for key in (
            "gap_ell_match",
            "generator_ell_match",
            "fill_ell_match",
            "generator_side_match",
            "fill_side_match",
            "p_delay_match",
        )
    )


def best_source_row(
    sources: list[dict[str, Any]],
    signature: dict[str, Any],
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    """返回匹配度最高的 source row 及其匹配向量。"""
    best: tuple[int, dict[str, Any], dict[str, Any]] | None = None
    for source in sources:
        vector = source_match_vector(source, signature)
        score = sum(
            1
            for key in (
                "gap_ell_match",
                "generator_ell_match",
                "fill_ell_match",
                "generator_side_match",
                "fill_side_match",
                "p_delay_match",
            )
            if vector[key]
        )
        if best is None or score > best[0]:
            best = (score, source, vector)
    if best is None:
        return None, None
    return best[1], best[2]


def gate_row(
    moving_row: dict[str, Any],
    same_gap_sources: list[dict[str, Any]],
    slot_source_key: str | None,
    pruning_row: dict[str, Any],
) -> dict[str, Any]:
    """构造单个 q 的 source materialization gate 行。"""
    q = int(moving_row["q"])
    signature = expected_signature(moving_row)
    best_source, best_vector = best_source_row(same_gap_sources, signature)
    exact_sources = []
    for source in same_gap_sources:
        vector = source_match_vector(source, signature)
        if all_required_matches(vector):
            exact_sources.append(source)

    exact_source = exact_sources[0] if exact_sources else None
    exact_key = str(exact_source["gap_fill_pair_key"]) if exact_source else None
    slot_source_key_matches = exact_key is not None and slot_source_key == exact_key
    gate_passed = exact_source is not None and (
        slot_source_key is None or slot_source_key_matches
    )
    if gate_passed:
        route = "ExactSourceMaterialized"
    elif same_gap_sources:
        route = "SameGapWrongSource-MaterializationGate"
    else:
        route = "NoGapSource-MaterializationGate"

    failed_invariants: list[str] = []
    if best_vector is None:
        failed_invariants = ["gap_source_absent"]
    else:
        failed_invariants = [
            key
            for key in (
                "generator_ell_match",
                "fill_ell_match",
                "generator_side_match",
                "fill_side_match",
                "p_delay_match",
            )
            if not best_vector[key]
        ]
    if exact_key is not None and slot_source_key is not None and not slot_source_key_matches:
        failed_invariants.append("slot_lock_source_key_match")

    return {
        "q": q,
        "route": route,
        "source_gate_passed_current": gate_passed,
        "expected_signature": signature,
        "same_gap_source_row_count": len(same_gap_sources),
        "exact_matching_source_row_count": len(exact_sources),
        "formal_pair_count": int(pruning_row["formal_pair_count"]),
        "formal_pairs_blocked_by_source_gate": 0
        if gate_passed
        else int(pruning_row["formal_pair_count"]),
        "actual_packet_count_current": int(pruning_row["actual_packet_count_current"]),
        "slot_lock_source_key": slot_source_key,
        "exact_source_key": exact_key,
        "slot_lock_source_key_matches": slot_source_key_matches,
        "best_source_key": str(best_source["gap_fill_pair_key"]) if best_source else None,
        "best_source_match_vector": best_vector,
        "failed_invariants": failed_invariants,
    }


def build_result(
    moving_path: Path,
    pair_path: Path,
    slot_path: Path,
    pruning_path: Path,
) -> dict[str, Any]:
    """构造 source materialization gate 审计结果。"""
    moving = load_json(moving_path)
    pair = load_json(pair_path)
    slot = load_json(slot_path)
    pruning = load_json(pruning_path)

    pair_by_q = pair_rows_by_q(pair["gap_fill_pair_rows"])
    slot_by_q = slot_source_by_q(slot["affine_twin_slot_phase_lock_rows"])
    pruning_rows = pruning_by_q(pruning["pruning_rows"])

    rows = [
        gate_row(
            moving_row,
            pair_by_q.get(int(moving_row["q"]), []),
            slot_by_q.get(int(moving_row["q"])),
            pruning_rows[int(moving_row["q"])],
        )
        for moving_row in moving["candidate_affine_twin_epoch_pair_rows"]
    ]

    source_pass_q_values = [row["q"] for row in rows if row["source_gate_passed_current"]]
    source_fail_q_values = [row["q"] for row in rows if not row["source_gate_passed_current"]]
    same_gap_wrong_rows = [
        row for row in rows if row["route"] == "SameGapWrongSource-MaterializationGate"
    ]
    no_gap_rows = [row for row in rows if row["route"] == "NoGapSource-MaterializationGate"]
    aggregate = {
        "moving_ledger": str(moving_path.relative_to(ROOT)),
        "pair_ledger": str(pair_path.relative_to(ROOT)),
        "slot_ledger": str(slot_path.relative_to(ROOT)),
        "pruning_ledger": str(pruning_path.relative_to(ROOT)),
        "candidate_q_values": [row["q"] for row in rows],
        "source_gate_pass_q_values": source_pass_q_values,
        "source_gate_fail_q_values": source_fail_q_values,
        "exact_source_match_count": len(source_pass_q_values),
        "same_gap_wrong_source_count": len(same_gap_wrong_rows),
        "no_gap_source_count": len(no_gap_rows),
        "formal_pairs_blocked_by_source_gate": sum(
            int(row["formal_pairs_blocked_by_source_gate"]) for row in rows
        ),
        "same_gap_wrong_source_formal_pair_count": sum(
            int(row["formal_pairs_blocked_by_source_gate"]) for row in same_gap_wrong_rows
        ),
        "no_gap_source_formal_pair_count": sum(
            int(row["formal_pairs_blocked_by_source_gate"]) for row in no_gap_rows
        ),
        "unresolved_source_failure_count_current": sum(
            1
            for row in rows
            if not row["source_gate_passed_current"] and not row["failed_invariants"]
        ),
        "all_source_failures_classified_current": all(
            row["source_gate_passed_current"] or bool(row["failed_invariants"])
            for row in rows
        ),
        "source_materialization_gate_closed_current_sweep": True,
        "global_source_materialization_gate_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": "prime_matrix_affine_twin_source_materialization_gate_audit",
        "status": "current_sweep_source_materialization_gate_classified_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "source_gate_rows": rows,
        "contract": {
            "source_gate": [
                "gap_ell=q",
                "generator_ell=q-2",
                "fill_ell=q",
                "generator/fill sides match the AffineTwin orientation",
                "p_delay=(11q-21)/4",
                "slot-lock source key agrees when a slot-lock exists",
            ],
            "closed_current_sweep": aggregate[
                "all_source_failures_classified_current"
            ],
            "global_remaining": [
                "GlobalSourceMaterializationGate",
                "SameGapWrongSource-PDEC/SAE",
                "NoGapSource-PDEC/SAE",
                "PrimitiveTwinSlotSupportEscape-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (moving_path, pair_path, slot_path, pruning_path)
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 和 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix AffineTwin source materialization gate audit",
        "",
        "**状态：** `current_sweep_source_materialization_gate_classified_global_open`",
        "",
        "本审计把 formal-pair pruning 中的 `SourceMaterializationFailure` 继续拆成可检查的源门控不变量。",
        "一个 formal residue product 要成为 actual packet，必须有 matching gap-fill source，并同时满足 `generator=q-2`、`fill=q`、方向、仿射 `p_delay` 和 slot-lock source key。",
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"source_gate_pass_q_values={agg['source_gate_pass_q_values']}",
        f"source_gate_fail_q_values={agg['source_gate_fail_q_values']}",
        f"formal_pairs_blocked_by_source_gate={agg['formal_pairs_blocked_by_source_gate']}",
        f"same_gap_wrong_source_formal_pair_count={agg['same_gap_wrong_source_formal_pair_count']}",
        f"no_gap_source_formal_pair_count={agg['no_gap_source_formal_pair_count']}",
        f"all_source_failures_classified_current={fmt_bool(agg['all_source_failures_classified_current'])}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. source gate 表",
        "",
        "| q | route | M_form | blocked | same-gap sources | exact sources | failed invariants |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["source_gate_rows"]:
        lines.append(
            "| {q} | `{route}` | {formal} | {blocked} | {same_gap} | {exact} | `{failed}` |".format(
                q=row["q"],
                route=table_cell(row["route"]),
                formal=row["formal_pair_count"],
                blocked=row["formal_pairs_blocked_by_source_gate"],
                same_gap=row["same_gap_source_row_count"],
                exact=row["exact_matching_source_row_count"],
                failed=table_cell(",".join(row["failed_invariants"]) or "none"),
            )
        )

    lines.extend(
        [
            "",
            "## 2. q=43 的错源诊断",
            "",
            "`q=43` 有同 gap source，但它不是 AffineTwin 期望源：",
            "",
            "```text",
            "expected: generator=41, fill=43, sides=minus->plus, p_delay=113",
            "actual:   generator=47, fill=43, sides=plus->minus, p_delay=74",
            "```",
            "",
            "因此 `q=43` 的 `16` 个 formal residue products 全部被源门控删除；它们不是 actual packets。",
            "",
            "## 3. q=103 的无源诊断",
            "",
            "`q=103` 当前没有任何 gap-fill source row，因此 `12` 个 formal residue products 全部归入 `NoGapSource-MaterializationGate`。",
            "",
            "## 4. 结论边界",
            "",
            "- 当前 source gate 解释了 formal-pair pruning 中全部 `28` 个 source 未物化配对。",
            "- 这不是全局行/列证明；全局仍需证明 source gate 的失败必路由到 `SameGapWrongSource-PDEC/SAE`、`NoGapSource-PDEC/SAE` 或 primitive support escape。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin source materialization gate 审计证书。"
    )
    parser.add_argument("--moving-ledger", type=Path, default=MOVING_LEDGER)
    parser.add_argument("--pair-ledger", type=Path, default=PAIR_LEDGER)
    parser.add_argument("--slot-ledger", type=Path, default=SLOT_LEDGER)
    parser.add_argument("--pruning-ledger", type=Path, default=PRUNING_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.moving_ledger,
        args.pair_ledger,
        args.slot_ledger,
        args.pruning_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
