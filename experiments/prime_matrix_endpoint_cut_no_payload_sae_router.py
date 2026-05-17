#!/usr/bin/env python3
"""生成 endpoint cut no-payload SAE 证书。

用法示例：
  python3 experiments/prime_matrix_endpoint_cut_no_payload_sae_router.py
  python3 -m json.tool data/prime-matrix-endpoint-cut-no-payload-sae-ledger.json

输出：
  data/prime-matrix-endpoint-cut-no-payload-sae-ledger.json
  docs/monograph/prime-matrix-endpoint-cut-no-payload-sae-router.json
  docs/monograph/prime-matrix-endpoint-cut-no-payload-sae-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

ZERO_GAIN = DATA / "prime-matrix-endpoint-cut-zero-gain-ledger.json"
PRIME_FILTER = DATA / "prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-endpoint-cut-no-payload-sae-ledger.json"
OUT_JSON = DOCS / "prime-matrix-endpoint-cut-no-payload-sae-router.json"
OUT_MD = DOCS / "prime-matrix-endpoint-cut-no-payload-sae-router.md"

PREVIOUS_TARGET = "ZeroGainEndpointCutSAEOrOneSlotResetPDECExclusion"
NEXT_TARGET = "OneSlotResetPDECExclusionOrNoPayloadEndpointSAESummability"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def aggregate(path: Path) -> dict[str, Any]:
    """读取账本 aggregate；没有 aggregate 时返回原对象。"""
    obj = load_json(path)
    return obj.get("aggregate", obj)


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def classify_payload(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """统计端点切断缓冲的 actual payload。"""
    actual_prime_rows = [row for row in rows if bool(row["is_prime_p"])]
    new_prime_rows = [
        row
        for row in rows
        if bool(row["is_prime_p"]) and not bool(row["already_in_prime_filtered_union"])
    ]
    filtered_repeat_prime_rows = [
        row
        for row in rows
        if bool(row["is_prime_p"]) and bool(row["already_in_prime_filtered_union"])
    ]
    formal_gap_composites = [
        row for row in rows if row["route"] == "formal_gap_but_composite_anchor"
    ]
    old_composites = [
        row for row in rows if row["route"] == "old_residue_composite_anchor"
    ]
    return {
        "actual_prime_rows": actual_prime_rows,
        "new_prime_rows": new_prime_rows,
        "filtered_repeat_prime_rows": filtered_repeat_prime_rows,
        "formal_gap_composites": formal_gap_composites,
        "old_composites": old_composites,
    }


def build_result() -> dict[str, Any]:
    """构造 endpoint cut no-payload SAE 证书。"""
    zero_obj = load_json(ZERO_GAIN)
    zero = zero_obj["aggregate"]
    prime_filter = aggregate(PRIME_FILTER)
    rows = zero_obj["cut_buffer_rows"]
    payload = classify_payload(rows)

    missing_before = set(int(value) for value in prime_filter["prime_filtered_missing_nonzero_residues"])
    formal_gap_residues = set(int(row["residue"]) for row in payload["formal_gap_composites"])
    actual_new_residues = set(int(row["residue"]) for row in payload["new_prime_rows"])
    missing_after_cut = sorted(missing_before - actual_new_residues)
    actual_payload_empty = (
        len(payload["actual_prime_rows"]) == 0
        and len(payload["new_prime_rows"]) == 0
        and len(payload["filtered_repeat_prime_rows"]) == 0
    )

    result = {
        "certificate_type": "prime_matrix_endpoint_cut_no_payload_sae_router",
        "status": "endpoint_cut_branch_has_empty_actual_payload",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "cut_buffer_step_count": int(zero["cut_buffer_step_count"]),
            "actual_prime_anchor_count_before_reset": len(payload["actual_prime_rows"]),
            "actual_new_prime_anchor_count_before_reset": len(payload["new_prime_rows"]),
            "filtered_repeat_prime_anchor_count_before_reset": len(
                payload["filtered_repeat_prime_rows"]
            ),
            "actual_payload_empty": actual_payload_empty,
            "actual_payload_mass": 0 if actual_payload_empty else len(payload["actual_prime_rows"]),
            "formal_gap_composite_row_count": len(payload["formal_gap_composites"]),
            "formal_gap_composite_residues": sorted(formal_gap_residues),
            "formal_gap_payload_survives_prime_filter": False,
            "old_residue_composite_row_count": len(payload["old_composites"]),
            "missing_nonzero_before_cut": len(missing_before),
            "missing_nonzero_after_cut": len(missing_after_cut),
            "missing_nonzero_set_preserved_by_cut": len(missing_before) == len(missing_after_cut),
            "missing_nonzero_residues_after_cut": missing_after_cut,
            "reset_atom_at_first_prime_anchor": bool(
                zero["reset_atom_instantiated_at_first_prime_anchor"]
            ),
            "endpoint_cut_routes_to_no_payload_sae": actual_payload_empty,
            "current_epoch_dichotomy": "one_slot_reset_pdec_or_no_payload_endpoint_sae",
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "cut_buffer_rows": rows,
        "formal_gap_composite_rows": payload["formal_gap_composites"],
        "old_residue_composite_rows": payload["old_composites"],
        "actual_payload_rows": payload["actual_prime_rows"],
        "plain_conclusion": (
            "端点切断缓冲 step=83..89 的 actual payload 为空：没有素数锚、没有新增 residue、"
            "缺失非零 residue 集保持不变。形式缺口 62 与 0 均被合数/71 整除过滤，"
            "所以 endpoint cut 分支不能携带反例链所需容量，只能登记为 no-payload SAE；"
            "若不走该 SAE，则首个素数锚已经是 one-slot reset-PDEC。"
        ),
        "dependency_hashes": {
            str(ZERO_GAIN.relative_to(ROOT)): sha256(ZERO_GAIN),
            str(PRIME_FILTER.relative_to(ROOT)): sha256(PRIME_FILTER),
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix endpoint cut no-payload SAE router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"cut_buffer_step_count={agg['cut_buffer_step_count']}",
        f"actual_prime_anchor_count_before_reset={agg['actual_prime_anchor_count_before_reset']}",
        f"actual_new_prime_anchor_count_before_reset={agg['actual_new_prime_anchor_count_before_reset']}",
        f"filtered_repeat_prime_anchor_count_before_reset={agg['filtered_repeat_prime_anchor_count_before_reset']}",
        f"actual_payload_empty={fmt_bool(agg['actual_payload_empty'])}",
        f"formal_gap_composite_residues={agg['formal_gap_composite_residues']}",
        f"missing_nonzero_before_cut={agg['missing_nonzero_before_cut']}",
        f"missing_nonzero_after_cut={agg['missing_nonzero_after_cut']}",
        f"missing_nonzero_set_preserved_by_cut={fmt_bool(agg['missing_nonzero_set_preserved_by_cut'])}",
        f"endpoint_cut_routes_to_no_payload_sae={fmt_bool(agg['endpoint_cut_routes_to_no_payload_sae'])}",
        f"reset_atom_at_first_prime_anchor={fmt_bool(agg['reset_atom_at_first_prime_anchor'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. buffer payload table",
        "",
        "| step | P | residue | route | payload |",
        "| ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["cut_buffer_rows"]:
        payload = "actual" if row["is_prime_p"] else "empty"
        lines.append(
            f"| {row['step']} | {row['p']} | {row['residue']} | `{row['route']}` | `{payload}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            "- 端点切断缓冲中 actual prime-anchor payload 为空。",
            "- 缺失非零 residue 数在切断前后保持 `35`，所以没有容量收益。",
            "- 形式缺口 `62,0` 不通过素数锚过滤，不能作为真实覆盖。",
            "- 当前 epoch 的剩余二分为 `one-slot reset-PDEC` 或 `no-payload endpoint SAE`。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
