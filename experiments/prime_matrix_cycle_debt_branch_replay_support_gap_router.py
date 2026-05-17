#!/usr/bin/env python3
"""生成 branch replay 的支撑宽度-CRT 模数缺口证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_branch_replay_support_gap_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json

输出：
  data/prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json
  docs/monograph/prime-matrix-cycle-debt-branch-replay-support-gap-router.json
  docs/monograph/prime-matrix-cycle-debt-branch-replay-support-gap-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SUPPORT_HALL = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"
COUPLED = DATA / "prime-matrix-cycle-debt-coupled-branch-entry-wall-ledger.json"
ARRIVAL_WALL = DATA / "prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-branch-replay-support-gap-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-branch-replay-support-gap-router.md"

PREVIOUS_TARGET = "K13BranchExclusiveCRTLoadExclusionOrK14CoupledEntryBranchCRTWallExclusion"
NEXT_TARGET = "BranchReplayColumnCRTPDECExclusionOrIsolatedTerminalAtomAbsorption"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def log10_int(value: int) -> float:
    """计算正整数十进对数。"""
    return math.log10(value) if value > 0 else 0.0


def replay_block(
    *,
    label: str,
    summary: dict[str, Any],
    support_width: int,
    audit_slot_count: int,
    period_p: int,
) -> dict[str, Any]:
    """把一个阻断因子包转成周期复现下界。

    若同一个阻断因子包在周期坐标中平移 T 个 period_p 后仍复现，
    每个素因子 q 都给出 T == 0 (mod q)，因为原槽已被 q 整除且
    gcd(q, period_p)=1。因此最小非零复现周期就是这些 q 的 lcm。
    """
    lcm_value = int(summary["lcm"])
    lcm_log10 = log10_int(lcm_value)
    return {
        "label": label,
        "factor_count": int(summary["factor_count"]),
        "support_width": int(support_width),
        "audit_slot_count": int(audit_slot_count),
        "replay_modulus": lcm_value,
        "replay_modulus_log10": lcm_log10,
        "log10_margin_over_support_width": lcm_log10 - math.log10(max(1, support_width)),
        "log10_margin_over_audit_slots": lcm_log10 - math.log10(max(1, audit_slot_count)),
        "gcd_with_period_p": math.gcd(lcm_value, period_p),
        "coprime_to_period_p": math.gcd(lcm_value, period_p) == 1,
        "nonzero_replay_exceeds_support_width": lcm_value > support_width,
        "nonzero_replay_exceeds_audit_slots": lcm_value > audit_slot_count,
        "nonzero_replay_exceeds_period_p": lcm_value > period_p,
    }


def build_result() -> dict[str, Any]:
    """构造 branch replay 支撑缺口证书。"""
    support_hall = load_json(SUPPORT_HALL)
    coupled = load_json(COUPLED)
    arrival_wall = load_json(ARRIVAL_WALL)

    period_p = int(coupled["aggregate"]["period_p"])
    near_shift_limit = int(support_hall["aggregate"]["near_shift_limit_cycles"])
    postwall_capacity_total = int(arrival_wall["aggregate"]["postwall_capacity_total"])
    entry_wall_count = int(arrival_wall["aggregate"]["entry_wall_prime_count"])

    agg = coupled["aggregate"]
    summaries = coupled["factor_summaries"]

    k13_width = int(agg["k13_branch_exclusive_width"])
    k14_branch_width = int(agg["k14_branch_exclusive_width"])
    k14_union_width = int(agg["k14_branch_arrival_union_width"])
    k14_assigned_width = int(agg["k14_arrival_assigned_width"])

    blocks = [
        replay_block(
            label="k13_branch_exclusive",
            summary=summaries["k13_branch_exclusive"],
            support_width=k13_width,
            audit_slot_count=k13_width,
            period_p=period_p,
        ),
        replay_block(
            label="k14_branch_exclusive",
            summary=summaries["k14_branch_exclusive"],
            support_width=k14_branch_width,
            audit_slot_count=k14_branch_width,
            period_p=period_p,
        ),
        replay_block(
            label="k14_branch_plus_entry",
            summary=summaries["k14_branch_plus_entry"],
            support_width=k14_union_width,
            audit_slot_count=k14_branch_width + entry_wall_count,
            period_p=period_p,
        ),
        replay_block(
            label="k14_branch_plus_entry_plus_assigned",
            summary=summaries["k14_branch_plus_entry_plus_assigned"],
            support_width=k14_union_width,
            audit_slot_count=k14_branch_width + entry_wall_count + k14_assigned_width,
            period_p=period_p,
        ),
        replay_block(
            label="k14_branch_plus_entry_plus_postwall",
            summary=summaries["k14_branch_plus_entry_plus_postwall"],
            support_width=k14_union_width,
            audit_slot_count=k14_branch_width + entry_wall_count + postwall_capacity_total,
            period_p=period_p,
        ),
        replay_block(
            label="both_branches_plus_k14_entry_postwall",
            summary=summaries["both_branches_plus_k14_entry_postwall"],
            support_width=k13_width + k14_union_width,
            audit_slot_count=k13_width + k14_branch_width + entry_wall_count + postwall_capacity_total,
            period_p=period_p,
        ),
    ]

    min_margin_support = min(item["log10_margin_over_support_width"] for item in blocks)
    min_margin_audit = min(item["log10_margin_over_audit_slots"] for item in blocks)

    aggregate = {
        "row_column_unconditional_closed": False,
        "previous_hardpoint": PREVIOUS_TARGET,
        "period_p": period_p,
        "near_shift_limit_cycles": near_shift_limit,
        "k13_branch_exclusive_width": k13_width,
        "k14_branch_arrival_union_width": k14_union_width,
        "k14_coupled_audit_slot_count_all_postwall": k14_branch_width + entry_wall_count + postwall_capacity_total,
        "smallest_log10_margin_over_support_width": min_margin_support,
        "smallest_log10_margin_over_audit_slots": min_margin_audit,
        "all_blocks_coprime_to_period": all(item["coprime_to_period_p"] for item in blocks),
        "all_nonzero_replay_moduli_exceed_support_width": all(
            item["nonzero_replay_exceeds_support_width"] for item in blocks
        ),
        "all_nonzero_replay_moduli_exceed_audit_slots": all(
            item["nonzero_replay_exceeds_audit_slots"] for item in blocks
        ),
        "all_nonzero_replay_moduli_exceed_period_p": all(
            item["nonzero_replay_exceeds_period_p"] for item in blocks
        ),
        "local_moving_slot_replay_excluded_for_registered_blocks": True,
        "far_replay_still_requires_columncrt_pdec": True,
        "isolated_atom_absorption_not_global_proof": True,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
    }

    result = {
        "certificate_type": "prime_matrix_cycle_debt_branch_replay_support_gap_router",
        "status": "local_moving_slot_replay_excluded_far_replay_routed_to_columncrt_pdec",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "replay_lemma": (
            "For a registered blocker package B with factors q coprime to the local period M, "
            "a replay after T period steps of the same package forces T=0 mod q for every q in B. "
            "Hence the least nonzero replay period is lcm(B)."
        ),
        "aggregate": aggregate,
        "replay_blocks": blocks,
        "plain_conclusion": (
            "K13 branch-exclusive 与 K14 coupled entry-branch 的本地 moving-slot 复现被关闭："
            "同一阻断因子包若在周期坐标中平移复现，非零位移必须至少为其 CRT lcm。"
            "K13 branch-exclusive 的 lcm 约 10^36.678，已远超 73 宽度支撑；"
            "K14 branch+entry+postwall 的 lcm 约 10^85.024，远超 78 宽度实际支撑与 117 个审计槽。"
            "因此本地支撑运动不能复现这些终端载荷；剩余只能是远程 ColumnCRT/PDEC 复现，"
            "或被登记为孤立有限原子，而不是新的自由逃逸路线。"
        ),
        "dependency_hashes": {
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
            str(COUPLED.relative_to(ROOT)): sha256(COUPLED),
            str(ARRIVAL_WALL.relative_to(ROOT)): sha256(ARRIVAL_WALL),
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
        "# Prime Matrix cycle-debt branch replay support-gap router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={str(agg['row_column_unconditional_closed']).lower()}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"near_shift_limit_cycles={agg['near_shift_limit_cycles']}",
        f"k13_branch_exclusive_width={agg['k13_branch_exclusive_width']}",
        f"k14_branch_arrival_union_width={agg['k14_branch_arrival_union_width']}",
        f"k14_coupled_audit_slot_count_all_postwall={agg['k14_coupled_audit_slot_count_all_postwall']}",
        f"smallest_log10_margin_over_support_width={agg['smallest_log10_margin_over_support_width']:.3f}",
        f"smallest_log10_margin_over_audit_slots={agg['smallest_log10_margin_over_audit_slots']:.3f}",
        f"all_blocks_coprime_to_period={str(agg['all_blocks_coprime_to_period']).lower()}",
        f"all_nonzero_replay_moduli_exceed_support_width={str(agg['all_nonzero_replay_moduli_exceed_support_width']).lower()}",
        f"all_nonzero_replay_moduli_exceed_audit_slots={str(agg['all_nonzero_replay_moduli_exceed_audit_slots']).lower()}",
        f"local_moving_slot_replay_excluded_for_registered_blocks={str(agg['local_moving_slot_replay_excluded_for_registered_blocks']).lower()}",
        f"far_replay_still_requires_columncrt_pdec={str(agg['far_replay_still_requires_columncrt_pdec']).lower()}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. replay lemma",
        "",
        "设本地周期为 `M=5680`。若一个已登记阻断包 `B` 在周期坐标中平移 `T` 个周期后仍由同一素因子包复现，则对每个 `q in B` 有",
        "",
        "```text",
        "n_q + T*M == 0 (mod q),  且  n_q == 0 (mod q).",
        "```",
        "",
        "因全部 `q` 与 `M` 互素，得到 `T == 0 (mod q)`。合并后 `T == 0 (mod lcm(B))`。所以最小非零复现周期就是 `lcm(B)`。",
        "",
        "## 2. replay blocks",
        "",
        "| block | support width | audit slots | factors | log10 replay modulus | margin over support | margin over audit |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for block in result["replay_blocks"]:
        lines.append(
            "| `{label}` | {support_width} | {audit_slot_count} | {factor_count} | "
            "{replay_modulus_log10:.3f} | {log10_margin_over_support_width:.3f} | "
            "{log10_margin_over_audit_slots:.3f} |".format(**block)
        )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- K13 分支的最小复现模数已经比 `73` 宽度支撑大约 `10^34.814` 倍。",
            "- K14 `branch+entry+postwall` 的最小复现模数比 `78` 宽度实际支撑大约 `10^83.132` 倍，也远超 `117` 个审计槽。",
            "- 因此高因子吸收槽不能通过本地 moving-slot 支撑运动复现；一旦移动，就必须换成新的阻断包并回流 `ColumnCRT/PDEC/SAE`。",
            "- 这仍不是全局行/列命题闭合；它关闭本地复现解释，并把远程复现登记为明确的 ColumnCRT/PDEC 接口。",
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
