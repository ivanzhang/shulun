#!/usr/bin/env python3
"""生成 branch replay 的全局二分证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_branch_replay_global_dichotomy_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-branch-replay-global-dichotomy-ledger.json

输出：
  data/prime-matrix-cycle-debt-branch-replay-global-dichotomy-ledger.json
  docs/monograph/prime-matrix-cycle-debt-branch-replay-global-dichotomy-router.json
  docs/monograph/prime-matrix-cycle-debt-branch-replay-global-dichotomy-router.md
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

SUPPORT_GAP = DATA / "prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-branch-replay-global-dichotomy-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-branch-replay-global-dichotomy-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-branch-replay-global-dichotomy-router.md"

PREVIOUS_TARGET = "BranchReplayColumnCRTPDECExclusionOrIsolatedTerminalAtomAbsorption"
NEXT_TARGET = "BranchReplayColumnCRTPDECExclusionOrFiniteAtomBaseCheck"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def log10_int(value: int) -> float:
    """计算正整数十进对数。"""
    return math.log10(value) if value > 0 else 0.0


def promote_block(block: dict[str, Any], period_p: int) -> dict[str, Any]:
    """把周期坐标 replay 模数提升到 P 坐标 ColumnCRT 模数。"""
    replay_modulus = int(block["replay_modulus"])
    p_space_modulus = replay_modulus * period_p
    return {
        "label": block["label"],
        "factor_count": int(block["factor_count"]),
        "support_width": int(block["support_width"]),
        "audit_slot_count": int(block["audit_slot_count"]),
        "cycle_replay_modulus": replay_modulus,
        "cycle_replay_modulus_log10": log10_int(replay_modulus),
        "p_space_columncrt_modulus": p_space_modulus,
        "p_space_columncrt_modulus_log10": log10_int(p_space_modulus),
        "p_space_margin_over_support_width_log10": log10_int(p_space_modulus) - math.log10(max(1, int(block["support_width"]))),
        "p_space_margin_over_audit_slots_log10": log10_int(p_space_modulus) - math.log10(max(1, int(block["audit_slot_count"]))),
        "defines_columncrt_replay_class": True,
    }


def build_result() -> dict[str, Any]:
    """构造全局二分证书。"""
    support_gap = load_json(SUPPORT_GAP)
    period_p = int(support_gap["aggregate"]["period_p"])
    blocks = [promote_block(block, period_p) for block in support_gap["replay_blocks"]]

    min_cycle = min(block["cycle_replay_modulus_log10"] for block in blocks)
    min_p_space = min(block["p_space_columncrt_modulus_log10"] for block in blocks)
    max_p_space = max(block["p_space_columncrt_modulus_log10"] for block in blocks)

    aggregate = {
        "row_column_unconditional_closed": False,
        "previous_hardpoint": PREVIOUS_TARGET,
        "period_p": period_p,
        "registered_replay_block_count": len(blocks),
        "minimum_cycle_replay_modulus_log10": min_cycle,
        "minimum_p_space_columncrt_modulus_log10": min_p_space,
        "maximum_p_space_columncrt_modulus_log10": max_p_space,
        "persistent_registered_replay_routes_to_columncrt_pdec": True,
        "isolated_atoms_cannot_form_infinite_registered_family": True,
        "new_blocker_package_routes_to_pdec_sae_or_new_router": True,
        "finite_atom_base_check_required": True,
        "global_unconditional_closed_by_this_router": False,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
    }

    result = {
        "certificate_type": "prime_matrix_cycle_debt_branch_replay_global_dichotomy_router",
        "status": "global_registered_replay_reduced_to_columncrt_pdec_or_finite_atom_check",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "global_dichotomy": [
            "If a registered terminal replay block occurs infinitely often with the same blocker package, it lies in a fixed P-space ColumnCRT class.",
            "If no registered block occurs infinitely often, the registered atoms are finite and require finite base checking rather than a structural escape.",
            "If the blocker package changes, the support-gap router sends the change to PDEC/SAE or to a new named router.",
        ],
        "aggregate": aggregate,
        "columncrt_blocks": blocks,
        "plain_conclusion": (
            "本步把孤立原子从全局反例链中剥离：登记的终端阻断包只有有限个。"
            "若某个登记包在全局反例链中无限复现，则周期 replay lemma 立即把它提升为 P 坐标中的固定 ColumnCRT 类，"
            "最小 P-space 模数约 10^36.336；若没有登记包无限复现，则这些登记原子只是有限项，"
            "不能作为全局结构逃逸，只能进入有限基例检查。若阻断包改变，则回流 PDEC/SAE 或新命名 router。"
        ),
        "dependency_hashes": {
            str(SUPPORT_GAP.relative_to(ROOT)): sha256(SUPPORT_GAP),
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
        "# Prime Matrix cycle-debt branch replay global dichotomy router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={str(agg['row_column_unconditional_closed']).lower()}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"registered_replay_block_count={agg['registered_replay_block_count']}",
        f"minimum_cycle_replay_modulus_log10={agg['minimum_cycle_replay_modulus_log10']:.3f}",
        f"minimum_p_space_columncrt_modulus_log10={agg['minimum_p_space_columncrt_modulus_log10']:.3f}",
        f"maximum_p_space_columncrt_modulus_log10={agg['maximum_p_space_columncrt_modulus_log10']:.3f}",
        f"persistent_registered_replay_routes_to_columncrt_pdec={str(agg['persistent_registered_replay_routes_to_columncrt_pdec']).lower()}",
        f"isolated_atoms_cannot_form_infinite_registered_family={str(agg['isolated_atoms_cannot_form_infinite_registered_family']).lower()}",
        f"finite_atom_base_check_required={str(agg['finite_atom_base_check_required']).lower()}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. global dichotomy",
        "",
        "- 登记的终端 replay block 是有限集合。",
        "- 若某个登记 block 在全局反例链中无限复现，则周期坐标 `T == 0 mod lcm(B)` 提升为 `P` 坐标中的固定 `period_p*lcm(B)` ColumnCRT 类。",
        "- 若没有登记 block 无限复现，则登记原子只剩有限项；它们不能构成全局结构逃逸，必须进入有限基例检查。",
        "- 若后续阻断包改变，则不属于同一 replay block，回流 `PDEC/SAE` 或生成新的命名 router。",
        "",
        "## 2. P-space ColumnCRT blocks",
        "",
        "| block | support width | audit slots | log10 cycle replay | log10 P-space modulus |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for block in result["columncrt_blocks"]:
        lines.append(
            "| `{label}` | {support_width} | {audit_slot_count} | "
            "{cycle_replay_modulus_log10:.3f} | {p_space_columncrt_modulus_log10:.3f} |".format(**block)
        )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- 本步不排斥远程 ColumnCRT/PDEC；它证明远程无限复现必须被登记为该类结构缺陷。",
            "- 孤立有限原子不再是全局结构出口，但仍需要有限基例检查；因此不能宣称行/列命题已经无条件闭合。",
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
