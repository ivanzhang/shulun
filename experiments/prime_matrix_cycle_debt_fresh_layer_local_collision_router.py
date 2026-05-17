#!/usr/bin/env python3
"""排除 registered branch replay 的 fresh-layer 本地投影碰撞。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_fresh_layer_local_collision_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-fresh-layer-local-collision-ledger.json

输出：
  data/prime-matrix-cycle-debt-fresh-layer-local-collision-ledger.json
  docs/monograph/prime-matrix-cycle-debt-fresh-layer-local-collision-router.json
  docs/monograph/prime-matrix-cycle-debt-fresh-layer-local-collision-router.md
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
FRESH_MODULUS = DATA / "prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json"
TAIL_SYNC = DATA / "prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-fresh-layer-local-collision-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-fresh-layer-local-collision-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-fresh-layer-local-collision-router.md"

PREVIOUS_TARGET = "FreshLayerPDECColumnCRTExclusion"
NEXT_TARGET = "FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def block_map(items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """按 label 建立索引。"""
    return {item["label"]: item for item in items}


def merge_block(period_p: int, support: dict[str, Any], fresh: dict[str, Any]) -> dict[str, Any]:
    """合并一个 replay block 的 fresh-layer 本地碰撞审计。"""
    sample = [int(q) for q in fresh["fresh_prime_sample"]]
    support_width = int(support["support_width"])
    audit_slots = int(support["audit_slot_count"])
    first = sample[0]
    max_window = max(support_width, audit_slots)
    return {
        "label": support["label"],
        "support_width": support_width,
        "audit_slot_count": audit_slots,
        "first_fresh_prime": first,
        "fresh_prime_sample": sample,
        "all_sample_coprime_to_period_p": all(math.gcd(period_p, q) == 1 for q in sample),
        "first_fresh_exceeds_support_width": first > support_width,
        "first_fresh_exceeds_audit_slots": first > audit_slots,
        "all_sample_exceed_support_width": all(q > support_width for q in sample),
        "all_sample_exceed_audit_slots": all(q > audit_slots for q in sample),
        "first_fresh_minus_support_width": first - support_width,
        "first_fresh_minus_audit_slots": first - audit_slots,
        "first_fresh_minus_max_window": first - max_window,
        "local_affine_projection_injective_for_sample": all(
            math.gcd(period_p, q) == 1 and max_window < q for q in sample
        ),
    }


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定门。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造本地 fresh-layer 碰撞排斥证书。"""
    support_gap = load_json(SUPPORT_GAP)
    fresh_modulus = load_json(FRESH_MODULUS)
    tail_sync = load_json(TAIL_SYNC)
    period_p = int(support_gap["aggregate"]["period_p"])
    supports = block_map(support_gap["replay_blocks"])
    fresh_layers = block_map(fresh_modulus["fresh_layers"])

    labels = sorted(set(supports) & set(fresh_layers))
    blocks = [merge_block(period_p, supports[label], fresh_layers[label]) for label in labels]

    all_coprime = all(block["all_sample_coprime_to_period_p"] for block in blocks)
    all_first_exceed_support = all(block["first_fresh_exceeds_support_width"] for block in blocks)
    all_first_exceed_audit = all(block["first_fresh_exceeds_audit_slots"] for block in blocks)
    all_sample_injective = all(block["local_affine_projection_injective_for_sample"] for block in blocks)
    min_first_minus_support = min(block["first_fresh_minus_support_width"] for block in blocks)
    min_first_minus_audit = min(block["first_fresh_minus_audit_slots"] for block in blocks)
    min_first_minus_max_window = min(block["first_fresh_minus_max_window"] for block in blocks)

    gates = [
        gate(
            "FreshLayerPDECImportedAsOnlyBranchReplayExit",
            tail_sync["hardpoint_after_router"] == PREVIOUS_TARGET,
            True,
            "上一同步已移除 tail-sieve 出口，branch-replay 子分支只剩 fresh-layer PDEC/ColumnCRT。",
            PREVIOUS_TARGET,
        ),
        gate(
            "FreshPrimesCoprimeToLocalPeriod",
            all_coprime,
            True,
            "全部登记 fresh prime sample 均与本地周期 5680 互素，因此局部槽坐标按周期步长在模 fresh prime 上可逆。",
            "closed for registered samples",
        ),
        gate(
            "FreshPrimeExceedsLocalSupport",
            all_first_exceed_support and all_first_exceed_audit,
            True,
            "每个登记 block 的首个 fresh prime 已大于对应 primitive support 宽度和审计槽数；样本 fresh primes 更大。",
            "closed for registered blocks",
        ),
        gate(
            "LocalFreshLayerProjectionCollisionExcluded",
            all_sample_injective,
            True,
            "若槽坐标为 a+jM，gcd(M,ell)=1 且窗口长度小于 ell，则 j->a+jM mod ell 在该窗口内单射，不能产生本地投影碰撞。",
            "closed for registered support windows",
        ),
        gate(
            "SupportMotionOrRemoteColumnCRTStillOpen",
            False,
            False,
            "fresh-layer PDEC 若仍持续，只能来自支撑运动逃逸、远程 P-space ColumnCRT 复现或未登记的新 block family。",
            NEXT_TARGET,
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只排除 registered fresh layers 的本地投影碰撞，不排除远程 ColumnCRT/PDEC 或新 moving-family。",
            NEXT_TARGET,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_cycle_debt_fresh_layer_local_collision_router",
        "status": "registered_fresh_layer_local_projection_collision_excluded_remote_columncrt_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_TARGET,
        "period_p": period_p,
        "registered_block_count": len(blocks),
        "fresh_prime_sample_count_per_block": fresh_modulus["aggregate"]["fresh_prime_sample_count_per_block"],
        "all_sample_fresh_primes_coprime_to_period_p": all_coprime,
        "all_first_fresh_primes_exceed_support_width": all_first_exceed_support,
        "all_first_fresh_primes_exceed_audit_slots": all_first_exceed_audit,
        "all_registered_samples_injective_on_local_windows": all_sample_injective,
        "minimum_first_fresh_minus_support_width": min_first_minus_support,
        "minimum_first_fresh_minus_audit_slots": min_first_minus_audit,
        "minimum_first_fresh_minus_max_window": min_first_minus_max_window,
        "local_fresh_layer_projection_collision_excluded": all_sample_injective,
        "support_motion_or_remote_columncrt_still_open": True,
        "fresh_layer_pdec_fully_excluded": False,
        "row_column_unconditional_closed": False,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "blocks": blocks,
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "registered branch replay 的 fresh-layer 本地投影碰撞已排除：全部 fresh prime sample "
            "与本地周期 5680 互素，且首个 fresh prime 已大于对应支撑宽度和审计槽数；因此局部窗口内 "
            "a+j*5680 mod ell 是单射。剩余 fresh-layer PDEC 只能是支撑运动逃逸、远程 ColumnCRT/PDEC "
            "或未登记 moving family。"
        ),
        "dependency_hashes": {
            str(SUPPORT_GAP.relative_to(ROOT)): sha256(SUPPORT_GAP),
            str(FRESH_MODULUS.relative_to(ROOT)): sha256(FRESH_MODULUS),
            str(TAIL_SYNC.relative_to(ROOT)): sha256(TAIL_SYNC),
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix cycle-debt fresh-layer 本地投影碰撞路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"period_p={result['period_p']}",
        f"registered_block_count={result['registered_block_count']}",
        "all_sample_fresh_primes_coprime_to_period_p="
        f"{fmt_bool(result['all_sample_fresh_primes_coprime_to_period_p'])}",
        "all_first_fresh_primes_exceed_support_width="
        f"{fmt_bool(result['all_first_fresh_primes_exceed_support_width'])}",
        "all_first_fresh_primes_exceed_audit_slots="
        f"{fmt_bool(result['all_first_fresh_primes_exceed_audit_slots'])}",
        "all_registered_samples_injective_on_local_windows="
        f"{fmt_bool(result['all_registered_samples_injective_on_local_windows'])}",
        f"minimum_first_fresh_minus_support_width={result['minimum_first_fresh_minus_support_width']}",
        f"minimum_first_fresh_minus_audit_slots={result['minimum_first_fresh_minus_audit_slots']}",
        f"local_fresh_layer_projection_collision_excluded={fmt_bool(result['local_fresh_layer_projection_collision_excluded'])}",
        f"fresh_layer_pdec_fully_excluded={fmt_bool(result['fresh_layer_pdec_fully_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 单射引理",
        "",
        "设本地周期步长为 `M=5680`，fresh prime 为 `ell`。若 `gcd(M,ell)=1` 且局部窗口长度 `W<ell`，"
        "则槽坐标 `j -> a+jM (mod ell)` 在 `0<=j<W` 上单射。否则若两个槽同余，则 `ell | (j1-j2)M`，"
        "由互素性得 `ell | (j1-j2)`；但 `|j1-j2|<W<ell`，只能 `j1=j2`。",
        "",
        "## 2. block 读数",
        "",
        "| block | support | audit slots | first fresh | first-support | first-audit | sample injective |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for block in result["blocks"]:
        lines.append(
            f"| `{block['label']}` | {block['support_width']} | {block['audit_slot_count']} | "
            f"{block['first_fresh_prime']} | {block['first_fresh_minus_support_width']} | "
            f"{block['first_fresh_minus_audit_slots']} | `{fmt_bool(block['local_affine_projection_injective_for_sample'])}` |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. 剩余接口",
            "",
            "```text",
            result["hardpoint_after_router"],
            "```",
            "",
            "本证书只排除 registered blocks 的本地 fresh-layer 投影碰撞。若 fresh-layer PDEC 仍持续，必须表现为支撑运动逃逸、远程 P-space ColumnCRT 复现或未登记 moving family。",
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


def main() -> None:
    """命令行入口。"""
    result = build_result()
    write_outputs(result)
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
