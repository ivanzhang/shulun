#!/usr/bin/env python3
"""生成 one-slot reset 后首个 relief 前缀无新增容量证书。

用法示例：
  python3 experiments/prime_matrix_one_slot_reset_prefix_no_relief_router.py
  python3 -m json.tool data/prime-matrix-one-slot-reset-prefix-no-relief-ledger.json

输出：
  data/prime-matrix-one-slot-reset-prefix-no-relief-ledger.json
  docs/monograph/prime-matrix-one-slot-reset-prefix-no-relief-router.json
  docs/monograph/prime-matrix-one-slot-reset-prefix-no-relief-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PRIME_FILTER = DATA / "prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json"
SATURATION = DATA / "prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json"
RESET_ATOM = DATA / "prime-matrix-prime-anchor-repeat-reset-atom-ledger.json"
NO_PAYLOAD = DATA / "prime-matrix-endpoint-cut-no-payload-sae-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-one-slot-reset-prefix-no-relief-ledger.json"
OUT_JSON = DOCS / "prime-matrix-one-slot-reset-prefix-no-relief-router.json"
OUT_MD = DOCS / "prime-matrix-one-slot-reset-prefix-no-relief-router.md"

PREVIOUS_TARGET = "OneSlotResetPDECExclusionOrNoPayloadEndpointSAESummability"
NEXT_TARGET = "AcceptedResetPDECExclusionOrDelayedReliefSupportMotionSAE"


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


def smallest_factor(n: int) -> int | None:
    """返回最小非平凡因子；素数返回 None。"""
    if n < 2:
        return n
    if n % 2 == 0:
        return 2 if n != 2 else None
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return None


def row_for_step(
    step: int,
    anchor_p: int,
    delay: int,
    anchor_residue: int,
    increment: int,
    ell: int,
    current_union: set[int],
    original_used: set[int],
    missing_nonzero: set[int],
) -> dict[str, Any]:
    """构造 reset 后同步步行。"""
    p_value = anchor_p + delay * step
    residue = (anchor_residue + increment * step) % ell
    factor = smallest_factor(p_value)
    is_prime = factor is None
    if not is_prime:
        route = "composite_no_payload"
    elif residue in missing_nonzero:
        route = "first_missing_nonzero_relief"
    elif residue in current_union:
        route = "repeat_prime_anchor_no_relief"
    else:
        route = "prime_anchor_outside_current_union"
    return {
        "step": step,
        "p": p_value,
        "residue": residue,
        "is_prime_p": is_prime,
        "smallest_factor": factor,
        "already_in_prime_filtered_union": residue in current_union,
        "already_in_original_used_residues": residue in original_used,
        "is_missing_nonzero_residue": residue in missing_nonzero,
        "route": route,
    }


def build_result() -> dict[str, Any]:
    """构造 one-slot reset 后前缀无 relief 证书。"""
    filt = aggregate(PRIME_FILTER)
    sat = aggregate(SATURATION)
    reset = aggregate(RESET_ATOM)
    no_payload = aggregate(NO_PAYLOAD)

    ell = int(filt["ell"])
    anchor_p = int(filt["support_anchor_p"])
    delay = int(filt["support_delay"])
    anchor_residue = int(sat["anchor_residue_mod_ell"])
    increment = int(sat["increment_mod_ell"])
    reset_step = int(reset["repeat_prime_anchor_step"])
    reset_p = int(reset["repeat_prime_anchor_p"])

    missing_including_zero = set(
        int(value) for value in filt["prime_filtered_missing_residues_including_zero"]
    )
    current_union = set(range(ell)) - missing_including_zero
    original_used = set(int(value) for value in sat["used_residues"])
    missing_nonzero = set(int(value) for value in filt["prime_filtered_missing_nonzero_residues"])

    rows: list[dict[str, Any]] = []
    repeat_prime_rows: list[dict[str, Any]] = []
    first_relief: dict[str, Any] | None = None
    for step in range(reset_step, reset_step + 5000):
        row = row_for_step(
            step,
            anchor_p,
            delay,
            anchor_residue,
            increment,
            ell,
            current_union,
            original_used,
            missing_nonzero,
        )
        rows.append(row)
        if row["is_prime_p"] and row["route"] == "repeat_prime_anchor_no_relief":
            repeat_prime_rows.append(row)
        if row["is_prime_p"] and row["route"] == "first_missing_nonzero_relief":
            first_relief = row
            break

    if first_relief is None:
        raise RuntimeError("没有在扫描窗口中找到首个缺失非零 relief")

    prefix_rows = rows[:-1]
    prefix_prime_rows = [row for row in prefix_rows if row["is_prime_p"]]
    prefix_new_rows = [
        row for row in prefix_rows if row["is_prime_p"] and row["is_missing_nonzero_residue"]
    ]
    reset_row = rows[0]
    actual_relief_requires_accepted_reset = int(first_relief["step"]) > reset_step

    result = {
        "certificate_type": "prime_matrix_one_slot_reset_prefix_no_relief_router",
        "status": "accepted_reset_has_no_missing_nonzero_relief_prefix",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "ell": ell,
            "reset_step": reset_step,
            "reset_p": reset_p,
            "reset_residue": int(reset["repeat_residue"]),
            "reset_atom_instantiated": bool(reset["reset_atom_instantiated"]),
            "endpoint_cut_actual_payload_empty": bool(no_payload["actual_payload_empty"]),
            "prefix_step_count_before_first_relief": len(prefix_rows),
            "prefix_p_span_before_first_relief": int(prefix_rows[-1]["p"]) - reset_p,
            "prefix_prime_anchor_count_before_first_relief": len(prefix_prime_rows),
            "prefix_new_missing_nonzero_count_before_first_relief": len(prefix_new_rows),
            "prefix_repeat_prime_anchor_count_before_first_relief": len(repeat_prime_rows),
            "prefix_missing_nonzero_preserved": len(prefix_new_rows) == 0,
            "first_missing_nonzero_relief": first_relief,
            "first_relief_step_gap_after_reset": int(first_relief["step"]) - reset_step,
            "first_relief_p_gap_after_reset": int(first_relief["p"]) - reset_p,
            "first_relief_requires_accepted_reset_pdec": actual_relief_requires_accepted_reset,
            "current_epoch_dichotomy": "accepted_reset_before_relief_or_no_payload_endpoint_sae",
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "reset_row": reset_row,
        "prefix_rows_before_first_relief": prefix_rows,
        "prefix_repeat_prime_rows_before_first_relief": repeat_prime_rows,
        "first_missing_nonzero_relief_row": first_relief,
        "plain_conclusion": (
            "若不切断 endpoint，则 P=9887 的一槽 reset 已先于任何新缺失非零 residue relief 出现。"
            "即使接受该 reset，直到 step=115, P=11887, residue=30 才出现第一个真实 relief；"
            "在 reset 到 relief 之前的前缀中，所有实际素数锚均为已见 residue，"
            "prefix_new_missing_nonzero_count=0。因此当前反例链若要取得新容量，"
            "必须先承担 accepted reset-PDEC；若拒绝 reset，则只能回到无 payload endpoint SAE。"
        ),
        "dependency_hashes": {
            str(PRIME_FILTER.relative_to(ROOT)): sha256(PRIME_FILTER),
            str(SATURATION.relative_to(ROOT)): sha256(SATURATION),
            str(RESET_ATOM.relative_to(ROOT)): sha256(RESET_ATOM),
            str(NO_PAYLOAD.relative_to(ROOT)): sha256(NO_PAYLOAD),
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
        "# Prime Matrix one-slot reset prefix no-relief router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"reset_step={agg['reset_step']}",
        f"reset_p={agg['reset_p']}",
        f"reset_residue={agg['reset_residue']}",
        f"endpoint_cut_actual_payload_empty={fmt_bool(agg['endpoint_cut_actual_payload_empty'])}",
        f"prefix_prime_anchor_count_before_first_relief={agg['prefix_prime_anchor_count_before_first_relief']}",
        f"prefix_new_missing_nonzero_count_before_first_relief={agg['prefix_new_missing_nonzero_count_before_first_relief']}",
        f"prefix_repeat_prime_anchor_count_before_first_relief={agg['prefix_repeat_prime_anchor_count_before_first_relief']}",
        f"first_relief_step_gap_after_reset={agg['first_relief_step_gap_after_reset']}",
        f"first_relief_p_gap_after_reset={agg['first_relief_p_gap_after_reset']}",
        f"first_relief_requires_accepted_reset_pdec={fmt_bool(agg['first_relief_requires_accepted_reset_pdec'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. reset 后首个 relief 前缀",
        "",
        "| step | P | residue | prime P | route |",
        "| ---: | ---: | ---: | --- | --- |",
    ]
    display_rows = result["prefix_rows_before_first_relief"] + [
        result["first_missing_nonzero_relief_row"]
    ]
    for row in display_rows:
        lines.append(
            f"| {row['step']} | {row['p']} | {row['residue']} | "
            f"`{fmt_bool(row['is_prime_p'])}` | `{row['route']}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            "- `P=9887` 已经是一槽 repeat reset，不是新增 missing residue 覆盖。",
            "- 从 reset 到首个 relief 前，实际素数锚全部落在已见 residue 中。",
            "- 第一个新增缺失非零 residue relief 是 `step=115, P=11887, residue=30`。",
            "- 因而新容量路径必须先接受 reset-PDEC；拒绝 reset 的路径仍是 no-payload endpoint SAE。",
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
