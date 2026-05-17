#!/usr/bin/env python3
"""生成 accepted reset 后完整 relief horizon 证书。

用法示例：
  python3 experiments/prime_matrix_accepted_reset_full_relief_horizon_router.py
  python3 -m json.tool data/prime-matrix-accepted-reset-full-relief-horizon-ledger.json

输出：
  data/prime-matrix-accepted-reset-full-relief-horizon-ledger.json
  docs/monograph/prime-matrix-accepted-reset-full-relief-horizon-router.json
  docs/monograph/prime-matrix-accepted-reset-full-relief-horizon-router.md
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
RESET_PREFIX = DATA / "prime-matrix-one-slot-reset-prefix-no-relief-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-accepted-reset-full-relief-horizon-ledger.json"
OUT_JSON = DOCS / "prime-matrix-accepted-reset-full-relief-horizon-router.json"
OUT_MD = DOCS / "prime-matrix-accepted-reset-full-relief-horizon-router.md"

PREVIOUS_TARGET = "AcceptedResetPDECExclusionOrDelayedReliefSupportMotionSAE"
NEXT_TARGET = "AcceptedResetPDECExclusionOrLongReliefHorizonSupportMotionSAE"


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


def build_result() -> dict[str, Any]:
    """构造完整 relief horizon 证书。"""
    filt = aggregate(PRIME_FILTER)
    sat = aggregate(SATURATION)
    prefix = aggregate(RESET_PREFIX)

    ell = int(filt["ell"])
    anchor_p = int(filt["support_anchor_p"])
    delay = int(filt["support_delay"])
    anchor_residue = int(sat["anchor_residue_mod_ell"])
    increment = int(sat["increment_mod_ell"])
    reset_step = int(prefix["reset_step"])
    reset_p = int(prefix["reset_p"])
    p_min, p_max = [int(value) for value in filt["current_epoch_p_range"]]

    missing_including_zero = set(
        int(value) for value in filt["prime_filtered_missing_residues_including_zero"]
    )
    seen = set(range(ell)) - missing_including_zero
    missing_nonzero = set(int(value) for value in filt["prime_filtered_missing_nonzero_residues"])
    original_used = set(int(value) for value in sat["used_residues"])

    new_relief_rows: list[dict[str, Any]] = []
    repeat_prime_rows: list[dict[str, Any]] = []
    composite_missing_rows: list[dict[str, Any]] = []
    prime_anchor_count = 0

    for step in range(reset_step, reset_step + 10000):
        p_value = anchor_p + delay * step
        residue = (anchor_residue + increment * step) % ell
        factor = smallest_factor(p_value)
        is_missing_open = residue in missing_nonzero and residue not in seen
        if factor is None:
            prime_anchor_count += 1
            row = {
                "step": step,
                "p": p_value,
                "residue": residue,
                "already_in_original_used_residues": residue in original_used,
            }
            if is_missing_open:
                row["route"] = "new_missing_nonzero_relief"
                new_relief_rows.append(row)
                seen.add(residue)
                if len(new_relief_rows) == len(missing_nonzero):
                    break
            else:
                row["route"] = "repeat_prime_anchor_no_new_relief"
                repeat_prime_rows.append(row)
        elif is_missing_open:
            composite_missing_rows.append(
                {
                    "step": step,
                    "p": p_value,
                    "residue": residue,
                    "smallest_factor": factor,
                    "route": "formal_missing_hit_but_composite",
                }
            )
    else:
        raise RuntimeError("没有在扫描窗口中补完全部缺失非零 residue")

    first_relief = new_relief_rows[0]
    final_relief = new_relief_rows[-1]
    epoch_width = p_max - p_min + 1
    result = {
        "certificate_type": "prime_matrix_accepted_reset_full_relief_horizon_router",
        "status": "full_missing_nonzero_relief_requires_long_post_reset_horizon",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "ell": ell,
            "missing_nonzero_count_at_reset": len(missing_nonzero),
            "reset_step": reset_step,
            "reset_p": reset_p,
            "first_relief_step": int(first_relief["step"]),
            "first_relief_p": int(first_relief["p"]),
            "first_relief_residue": int(first_relief["residue"]),
            "full_relief_step": int(final_relief["step"]),
            "full_relief_p": int(final_relief["p"]),
            "full_relief_residue": int(final_relief["residue"]),
            "full_relief_step_gap_after_reset": int(final_relief["step"]) - reset_step,
            "full_relief_p_gap_after_reset": int(final_relief["p"]) - reset_p,
            "full_relief_p_extension_beyond_epoch_p_max": int(final_relief["p"]) - p_max,
            "full_relief_extension_over_epoch_width": (int(final_relief["p"]) - p_max)
            / epoch_width,
            "prime_anchor_count_until_full_relief": prime_anchor_count,
            "new_relief_prime_anchor_count_until_full_relief": len(new_relief_rows),
            "repeat_prime_anchor_count_until_full_relief": len(repeat_prime_rows),
            "composite_missing_candidate_count_until_full_relief": len(composite_missing_rows),
            "repeat_to_new_relief_ratio_until_full_relief": len(repeat_prime_rows)
            / len(new_relief_rows),
            "all_missing_nonzero_residues_relieved": len(new_relief_rows) == len(missing_nonzero),
            "full_relief_requires_long_support_motion": True,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "new_relief_rows": new_relief_rows,
        "repeat_prime_rows_sample": repeat_prime_rows[:20],
        "composite_missing_rows_sample": composite_missing_rows[:20],
        "plain_conclusion": (
            "接受 P=9887 的一槽 reset 后，补完全部 35 个缺失非零 residue 直到 "
            "step=1192, P=98047, residue=67 才完成；这距离 reset 有 1102 个同步步、"
            "88160 的 P 距离，并且期间出现 225 个 repeat prime anchor。"
            "因此完整 relief 不是局部容量修补，而是长程 support-motion 义务；"
            "若该长程运动不可吸收，则回到 accepted reset-PDEC 排斥。"
        ),
        "dependency_hashes": {
            str(PRIME_FILTER.relative_to(ROOT)): sha256(PRIME_FILTER),
            str(SATURATION.relative_to(ROOT)): sha256(SATURATION),
            str(RESET_PREFIX.relative_to(ROOT)): sha256(RESET_PREFIX),
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
        "# Prime Matrix accepted reset full relief horizon router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"missing_nonzero_count_at_reset={agg['missing_nonzero_count_at_reset']}",
        f"reset_step={agg['reset_step']}",
        f"reset_p={agg['reset_p']}",
        f"first_relief=(step={agg['first_relief_step']},P={agg['first_relief_p']},residue={agg['first_relief_residue']})",
        f"full_relief=(step={agg['full_relief_step']},P={agg['full_relief_p']},residue={agg['full_relief_residue']})",
        f"full_relief_step_gap_after_reset={agg['full_relief_step_gap_after_reset']}",
        f"full_relief_p_gap_after_reset={agg['full_relief_p_gap_after_reset']}",
        f"repeat_prime_anchor_count_until_full_relief={agg['repeat_prime_anchor_count_until_full_relief']}",
        f"new_relief_prime_anchor_count_until_full_relief={agg['new_relief_prime_anchor_count_until_full_relief']}",
        f"composite_missing_candidate_count_until_full_relief={agg['composite_missing_candidate_count_until_full_relief']}",
        f"full_relief_extension_over_epoch_width={agg['full_relief_extension_over_epoch_width']:.12f}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. new relief rows",
        "",
        "| # | step | P | residue |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for index, row in enumerate(result["new_relief_rows"], start=1):
        lines.append(f"| {index} | {row['step']} | {row['p']} | {row['residue']} |")

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            "- 首个 relief 已经在 reset 之后，完整 relief 更远到 `P=98047`。",
            "- 到完整 relief 前共有 `225` 个 repeat prime-anchor，不提供新增缺失 residue 容量。",
            "- 形式上命中缺失 residue 但为合数的候选也有 `101` 个，不能计入 actual load。",
            "- 因此当前剩余转为 accepted reset-PDEC 排斥，或长程 support-motion SAE 吸收。",
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
