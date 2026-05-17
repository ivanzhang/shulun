#!/usr/bin/env python3
"""生成 prime-anchor repeat reset atom 证书。

用法示例：
  python3 experiments/prime_matrix_prime_anchor_repeat_reset_atom_router.py
  python3 -m json.tool data/prime-matrix-prime-anchor-repeat-reset-atom-ledger.json

输出：
  data/prime-matrix-prime-anchor-repeat-reset-atom-ledger.json
  docs/monograph/prime-matrix-prime-anchor-repeat-reset-atom-router.json
  docs/monograph/prime-matrix-prime-anchor-repeat-reset-atom-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

IMMEDIATE_REPEAT = DATA / "prime-matrix-prime-anchor-postband-immediate-repeat-ledger.json"
SATURATION = DATA / "prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-prime-anchor-repeat-reset-atom-ledger.json"
OUT_JSON = DOCS / "prime-matrix-prime-anchor-repeat-reset-atom-router.json"
OUT_MD = DOCS / "prime-matrix-prime-anchor-repeat-reset-atom-router.md"

PREVIOUS_TARGET = "ImmediatePrimeAnchorRepeatTransportResetPDECOrEndpointMotionSAE"
NEXT_TARGET = "OneSlotPrimeAnchorRepeatResetPDECExclusionOrEndpointMotionSAE"


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


def find_record(records: list[dict[str, Any]], residue: int) -> dict[str, Any]:
    """查找指定 residue 的原始 singleton 记录。"""
    matches = [record for record in records if int(record["crt_residue"]) == residue]
    if len(matches) != 1:
        raise RuntimeError(f"expected one record for residue {residue}, got {len(matches)}")
    return matches[0]


def build_result() -> dict[str, Any]:
    """构造 repeat reset atom 证书。"""
    immediate = aggregate(IMMEDIATE_REPEAT)
    saturation_obj = load_json(SATURATION)
    saturation = saturation_obj["aggregate"]
    records = saturation_obj["minus71_existing_records"]

    ell = int(immediate["ell"])
    repeat = immediate["first_repeat_prime_anchor"]
    repeat_p = int(repeat["p"])
    repeat_step = int(repeat["step"])
    repeat_residue = int(repeat["residue"])
    original = find_record(records, repeat_residue)
    original_p = int(original["p"])
    delta_p = repeat_p - original_p
    lift_delta, lift_remainder = divmod(delta_p, ell)
    original_lift, original_residue = divmod(original_p, ell)
    repeat_lift, repeat_mod_residue = divmod(repeat_p, ell)
    composite_buffer = [
        row
        for row in load_json(IMMEDIATE_REPEAT)["post_band_rows_until_first_prime_window"]
        if not row["is_prime_p"]
    ]

    reset_atom = {
        "side": str(saturation["side"]),
        "ell": ell,
        "residue": repeat_residue,
        "original_p": original_p,
        "repeat_p": repeat_p,
        "original_lift": original_lift,
        "repeat_lift": repeat_lift,
        "lift_delta": lift_delta,
        "p_delta": delta_p,
        "slot_keys": original["slot_keys"],
        "residue_packet_key": f"size=1|side={saturation['side']}|ells={ell}|mod={ell}|residue={repeat_residue}",
        "formal_unit": (
            f"one-slot-repeat-reset|side={saturation['side']}|ell={ell}|"
            f"residue={repeat_residue}|lift_delta={lift_delta}|"
            f"p={original_p}->{repeat_p}"
        ),
    }
    exact_translate = (
        lift_remainder == 0
        and original_residue == repeat_residue
        and repeat_mod_residue == repeat_residue
        and lift_delta > 0
    )
    endpoint_cut = {
        "must_cut_before_step": repeat_step,
        "must_cut_before_p": repeat_p,
        "last_admitted_step": int(immediate["admitted_step_range"][1]),
        "last_epoch_p_max": int(immediate["current_epoch_p_range"][1]),
        "step_gap_after_admitted_band": int(immediate["repeat_step_gap_after_admitted_band"]),
        "p_extension_beyond_epoch_p_max": int(immediate["repeat_p_extension_beyond_epoch_p_max"]),
        "p_extension_beyond_admitted_lattice_p_max": int(
            immediate["repeat_p_extension_beyond_admitted_lattice_p_max"]
        ),
        "composite_buffer_step_count": len(composite_buffer),
        "composite_buffer_steps": [int(row["step"]) for row in composite_buffer],
        "composite_buffer_p_values": [int(row["p"]) for row in composite_buffer],
    }

    result = {
        "certificate_type": "prime_matrix_prime_anchor_repeat_reset_atom_router",
        "status": "one_slot_prime_anchor_repeat_reset_atom_instantiated",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "ell": ell,
            "repeat_residue": repeat_residue,
            "original_record_p": original_p,
            "repeat_prime_anchor_p": repeat_p,
            "repeat_prime_anchor_step": repeat_step,
            "p_delta": delta_p,
            "p_delta_over_ell": lift_delta,
            "p_delta_remainder_mod_ell": lift_remainder,
            "exact_same_residue_ell_translate": exact_translate,
            "reset_atom_instantiated": exact_translate and bool(
                immediate["first_postband_prime_is_original_used_repeat"]
            ),
            "new_prime_anchor_count_before_first_repeat": int(
                immediate["new_prime_anchor_count_before_first_repeat"]
            ),
            "missing_nonzero_remaining_at_reset_atom": int(
                immediate["missing_nonzero_remaining_at_first_repeat"]
            ),
            "endpoint_cut_required_to_avoid_reset": True,
            "endpoint_cut": endpoint_cut,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "reset_atom": reset_atom,
        "original_record": original,
        "composite_buffer_before_reset": composite_buffer,
        "plain_conclusion": (
            "首个 post-band 素数锚 P=9887 与原始 singleton 记录 P=7757 "
            "具有同一 minus:71 residue=18，且差值为 2130=30*71。"
            "这不是新的 residue 覆盖，而是一个已实例化的一槽 repeat-reset 原子。"
            "若同一 epoch 延伸到该点，必须进入 reset-PDEC；若反例链拒绝 reset，"
            "端点必须在首个 post-band 素数锚之前切断，转入 endpoint motion/SAE。"
        ),
        "dependency_hashes": {
            str(IMMEDIATE_REPEAT.relative_to(ROOT)): sha256(IMMEDIATE_REPEAT),
            str(SATURATION.relative_to(ROOT)): sha256(SATURATION),
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
    reset = result["reset_atom"]
    endpoint = agg["endpoint_cut"]
    lines = [
        "# Prime Matrix prime-anchor repeat reset atom router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"original_record_p={agg['original_record_p']}",
        f"repeat_prime_anchor_p={agg['repeat_prime_anchor_p']}",
        f"repeat_residue={agg['repeat_residue']}",
        f"p_delta={agg['p_delta']}",
        f"p_delta_over_ell={agg['p_delta_over_ell']}",
        f"exact_same_residue_ell_translate={fmt_bool(agg['exact_same_residue_ell_translate'])}",
        f"reset_atom_instantiated={fmt_bool(agg['reset_atom_instantiated'])}",
        f"new_prime_anchor_count_before_first_repeat={agg['new_prime_anchor_count_before_first_repeat']}",
        f"missing_nonzero_remaining_at_reset_atom={agg['missing_nonzero_remaining_at_reset_atom']}",
        f"endpoint_cut_required_to_avoid_reset={fmt_bool(agg['endpoint_cut_required_to_avoid_reset'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. reset atom",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key in [
        "side",
        "ell",
        "residue",
        "original_p",
        "repeat_p",
        "original_lift",
        "repeat_lift",
        "lift_delta",
        "p_delta",
        "slot_keys",
        "formal_unit",
    ]:
        lines.append(f"| `{key}` | `{reset[key]}` |")

    lines.extend(
        [
            "",
            "## 2. endpoint cut alternative",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in endpoint.items():
        lines.append(f"| `{key}` | `{value}` |")

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- `9887-7757=2130=30*71`，所以这是同一 residue packet 的整周期平移。",
            "- 在该 repeat 前没有任何新素数锚补入缺失非零 residue。",
            "- 若保持同一无 reset epoch，则 reset-PDEC atom 已经实例化。",
            "- 若避免 reset，则必须在首个 post-band 素数锚前切断，进入 endpoint motion/SAE。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
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
