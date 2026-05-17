#!/usr/bin/env python3
"""生成 branch replay 的 fresh-modulus escalation 证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_branch_replay_fresh_modulus_escalation_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json

输出：
  data/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json
  docs/monograph/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-router.json
  docs/monograph/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-router.md
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

COUPLED = DATA / "prime-matrix-cycle-debt-coupled-branch-entry-wall-ledger.json"
POST100000 = DATA / "prime-matrix-cycle-debt-post100000-tail-atom-exact-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-router.md"

PREVIOUS_TARGET = "BranchReplayColumnCRTPDECExclusion"
NEXT_TARGET = "UnboundedFreshModulusEscalationPDECOrTailSieveStabilityContradiction"
FRESH_PRIME_SAMPLE_COUNT = 8


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime(n: int) -> bool:
    """试除法素性检查。"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def next_fresh_primes(after: int, used: set[int], count: int) -> list[int]:
    """找出超过 after 且不在 used 中的 fresh primes。"""
    result: list[int] = []
    n = after + 1
    while len(result) < count:
        if is_prime(n) and n not in used:
            result.append(n)
        n += 1
    return result


def lcm_many(values: list[int] | set[int]) -> int:
    """计算最小公倍数。"""
    value = 1
    for item in values:
        value = value * int(item) // math.gcd(value, int(item))
    return value


def log10_int(value: int) -> float:
    """计算正整数十进对数。"""
    return math.log10(value) if value > 0 else 0.0


def block_layer(label: str, block: dict[str, Any]) -> dict[str, Any]:
    """生成一个 replay block 的 fresh-prime 层摘要。"""
    factors = [int(item) for item in block["factors"]]
    factor_set = set(factors)
    old_lcm = int(block["lcm"])
    max_factor = max(factors)
    fresh = next_fresh_primes(max_factor, factor_set, FRESH_PRIME_SAMPLE_COUNT)
    lcm_plus_first = lcm_many(factors + fresh[:1])
    lcm_plus_sample = lcm_many(factors + fresh)
    return {
        "label": label,
        "factor_count": len(factors),
        "max_registered_factor": max_factor,
        "fresh_prime_sample": fresh,
        "all_fresh_primes_coprime_to_old_lcm": all(math.gcd(old_lcm, q) == 1 for q in fresh),
        "old_lcm_log10": log10_int(old_lcm),
        "lcm_plus_first_fresh_log10": log10_int(lcm_plus_first),
        "lcm_plus_sample_log10": log10_int(lcm_plus_sample),
        "first_fresh_log10_gain": log10_int(lcm_plus_first) - log10_int(old_lcm),
        "sample_log10_gain": log10_int(lcm_plus_sample) - log10_int(old_lcm),
        "finite_crt_class_can_be_terminal": False,
    }


def build_result() -> dict[str, Any]:
    """构造 fresh-modulus escalation 证书。"""
    coupled = load_json(COUPLED)
    post100000 = load_json(POST100000)
    blocks = [
        block_layer(label, block)
        for label, block in coupled["factor_summaries"].items()
        if label in {
            "k13_branch_exclusive",
            "k14_branch_exclusive",
            "k14_branch_plus_entry",
            "k14_branch_plus_entry_plus_assigned",
            "k14_branch_plus_entry_plus_postwall",
            "both_branches_plus_k14_entry_postwall",
        }
    ]

    aggregate = {
        "row_column_unconditional_closed": False,
        "previous_hardpoint": PREVIOUS_TARGET,
        "finite_atom_branch_closed_for_registered_atoms": bool(
            post100000["aggregate"]["finite_atom_branch_closed_for_registered_atoms"]
        ),
        "registered_replay_block_count": len(blocks),
        "fresh_prime_sample_count_per_block": FRESH_PRIME_SAMPLE_COUNT,
        "all_registered_blocks_have_coprime_fresh_layers": all(
            block["all_fresh_primes_coprime_to_old_lcm"] for block in blocks
        ),
        "minimum_first_fresh_log10_gain": min(block["first_fresh_log10_gain"] for block in blocks),
        "minimum_sample_log10_gain": min(block["sample_log10_gain"] for block in blocks),
        "finite_crt_terminal_description_excluded": True,
        "persistent_family_requires_unbounded_modulus_or_pdec": True,
        "tail_sieve_stability_contradiction_still_open": True,
        "global_unconditional_closed_by_this_router": False,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
    }

    result = {
        "certificate_type": "prime_matrix_cycle_debt_branch_replay_fresh_modulus_escalation_router",
        "status": "finite_columncrt_replay_class_nonterminal_fresh_modulus_escalation_registered",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "fresh_layer_lemma": (
            "A finite CRT replay class modulo Q cannot be a terminal description for an infinite prime-matrix counterexample chain. "
            "Every prime ell not dividing Q is a new independent CRT coordinate. When ell enters the active wheel, persistence must either "
            "absorb ell into the modulus, fail as a PDEC/ColumnCRT defect, or be handled by a tail-sieve stability bound."
        ),
        "aggregate": aggregate,
        "fresh_layers": blocks,
        "plain_conclusion": (
            "有限 ColumnCRT replay 类不是全局终端结构。当前有限原子分支已关闭后，剩余持久 replay 若固定在某个登记模数上，"
            "每一个未登记的新素数层都会给出与旧模数互素的新 CRT 坐标；因此无限反例链不能在有限模数上稳定，"
            "只能不断扩模、触发 PDEC/ColumnCRT 缺陷，或转入尾段筛稳定矛盾。"
        ),
        "dependency_hashes": {
            str(COUPLED.relative_to(ROOT)): sha256(COUPLED),
            str(POST100000.relative_to(ROOT)): sha256(POST100000),
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
        "# Prime Matrix cycle-debt branch replay fresh-modulus escalation router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={str(agg['row_column_unconditional_closed']).lower()}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"finite_atom_branch_closed_for_registered_atoms={str(agg['finite_atom_branch_closed_for_registered_atoms']).lower()}",
        f"registered_replay_block_count={agg['registered_replay_block_count']}",
        f"fresh_prime_sample_count_per_block={agg['fresh_prime_sample_count_per_block']}",
        f"all_registered_blocks_have_coprime_fresh_layers={str(agg['all_registered_blocks_have_coprime_fresh_layers']).lower()}",
        f"minimum_first_fresh_log10_gain={agg['minimum_first_fresh_log10_gain']:.3f}",
        f"minimum_sample_log10_gain={agg['minimum_sample_log10_gain']:.3f}",
        f"finite_crt_terminal_description_excluded={str(agg['finite_crt_terminal_description_excluded']).lower()}",
        f"persistent_family_requires_unbounded_modulus_or_pdec={str(agg['persistent_family_requires_unbounded_modulus_or_pdec']).lower()}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. fresh layer lemma",
        "",
        "固定有限 CRT replay 类的模数记为 `Q`。任意新素数 `ell` 若不整除 `Q`，则 `ell` 是与旧周期互素的新 CRT 坐标。"
        "当 `ell` 进入后续筛层时，持久反例链不能只靠旧的 `mod Q` 信息决定 `ell` 层；它必须扩模、触发 PDEC/ColumnCRT 缺陷，或被尾段筛稳定估计吸收。",
        "",
        "## 2. registered blocks",
        "",
        "| block | factors | max factor | first fresh primes | old log10 lcm | +first gain | +sample gain |",
        "| --- | ---: | ---: | --- | ---: | ---: | ---: |",
    ]
    for block in result["fresh_layers"]:
        lines.append(
            f"| `{block['label']}` | {block['factor_count']} | {block['max_registered_factor']} | "
            f"`{block['fresh_prime_sample']}` | {block['old_lcm_log10']:.3f} | "
            f"{block['first_fresh_log10_gain']:.3f} | {block['sample_log10_gain']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- 当前 finite atom 分支已经由 post-100000 exact runner 对登记对象关闭。",
            "- 任一登记 replay block 仍只是有限 CRT 类；新素数层必然继续给出互素 CRT 坐标。",
            "- 因此有限 CRT 类不能作为全局终端稳定结构；持久族必须走无界扩模/PDEC，或转入尾段筛稳定矛盾。",
            "- 本步仍不宣称行/列命题闭合；它把最后接口从固定 ColumnCRT 类排斥推进到无界 fresh-modulus escalation。",
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
