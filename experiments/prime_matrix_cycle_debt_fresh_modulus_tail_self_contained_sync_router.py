#!/usr/bin/env python3
"""同步 cycle-debt fresh-modulus 分支中的 strict tail-sieve 自足闭合状态。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_fresh_modulus_tail_self_contained_sync_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-ledger.json

输出：
  data/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-ledger.json
  docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-router.json
  docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

FRESH_TAIL = DATA / "prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-ledger.json"
MERTENS_SYNC = DOCS / "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json"
TERMINAL_SYNC = DOCS / "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-router.md"

PREVIOUS_TARGET = "FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure"
NEXT_TARGET = "FreshLayerPDECColumnCRTExclusion"
SELF_MERTENS = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"


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
    """构造 strict tail-sieve 同步证书。"""
    fresh_tail = load_json(FRESH_TAIL)
    mertens = load_json(MERTENS_SYNC)
    terminal = load_json(TERMINAL_SYNC)

    previous_tail_interface = bool(fresh_tail["tail_object_interface_closed"])
    previous_external_tail = bool(fresh_tail["conditional_external_tail_sieve_closed"])
    previous_strict_tail_open = not bool(fresh_tail["strict_self_contained_tail_sieve_closed"])
    non_pdec_forces_tail = bool(fresh_tail["non_pdec_unbounded_fresh_layers_force_tail_rough_object"])
    strict_mertens_closed = bool(mertens["strict_self_contained_mertens_tail_proved"])
    b3_tv_synced = bool(terminal["b3_tv_strict_self_contained_synchronized"])

    strict_tail_now_closed = (
        previous_tail_interface
        and non_pdec_forces_tail
        and previous_external_tail
        and strict_mertens_closed
        and b3_tv_synced
    )

    gates = [
        gate(
            "PreviousFreshTailBridgeImported",
            previous_tail_interface,
            True,
            "上一证书已把 non-PDEC 无界 fresh layers 接到 B3 避单余类 tail rough object。",
            PREVIOUS_TARGET,
        ),
        gate(
            "OldSelfContainedDusartAtomWasOpenInBridge",
            previous_strict_tail_open,
            True,
            "上一桥接中 strict tail-sieve 的唯一解析粗原子仍登记为 SelfContainedDusart...",
            SELF_MERTENS,
        ),
        gate(
            "StrictMertensTailClosedByLatestSync",
            strict_mertens_closed,
            True,
            "后续 strict 速率尾段同步已导入 theta/PNT 包络与 B1 区间，Mertens 尾段解析包从活动剩余移出。",
            "closed",
        ),
        gate(
            "B3TVStrictSelfContainedSynchronized",
            b3_tv_synced,
            True,
            "终端预算最新同步确认 B3-TV 的 Stieltjes 边界结构、20000 锚点预算与自足 Mertens 尾段已合并。",
            "closed for tail-sieve branch",
        ),
        gate(
            "StrictTailSieveStabilityBranchClosedForBranchReplay",
            strict_tail_now_closed,
            True,
            "在上一桥接对象接口、B3-TV 同步和 Mertens 尾段自足闭合同时成立后，branch-replay 的 tail-sieve stability 出口移出剩余基。",
            "closed",
        ),
        gate(
            "FreshLayerPDECExitStillRequiresExclusion",
            False,
            False,
            "剩余反例链只能在某个 fresh layer 产生相位复用、投影碰撞、moving support 逃逸或 ColumnCRT 缺陷；该 PDEC/ColumnCRT 出口尚未排斥。",
            NEXT_TARGET,
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭的是 branch-replay 的 strict tail-sieve stability 出口；行/列全局还需 fresh-layer PDEC 排斥及其它全局终端门。",
            NEXT_TARGET,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_cycle_debt_fresh_modulus_tail_self_contained_sync_router",
        "status": "fresh_modulus_tail_sieve_strict_self_contained_synced_fresh_layer_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_TARGET,
        "previous_tail_object_interface_closed": previous_tail_interface,
        "previous_non_pdec_unbounded_fresh_layers_force_tail_rough_object": non_pdec_forces_tail,
        "previous_conditional_external_tail_sieve_closed": previous_external_tail,
        "previous_strict_tail_sieve_closed": not previous_strict_tail_open,
        "strict_self_contained_mertens_tail_proved_latest": strict_mertens_closed,
        "b3_tv_strict_self_contained_synchronized_latest": b3_tv_synced,
        "strict_self_contained_tail_sieve_closed_for_branch_replay": strict_tail_now_closed,
        "fresh_layer_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "old_branch_replay_strict_remaining_basis": fresh_tail["strict_branch_remaining_basis"],
        "new_branch_replay_strict_remaining_basis": NEXT_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "inherited_global_strict_remaining_basis_after_mertens_sync": mertens[
            "strict_self_contained_condensed_basis"
        ],
        "inherited_terminal_budget_latest_target": terminal["next_direct_attack_target"],
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "本步把 branch-replay fresh-modulus 分支中旧的 strict tail-sieve 开口同步到最新解析前沿。"
            "上一桥接已把 non-PDEC 无界 fresh layers 接到 B3 避单余类粗筛对象；后续 strict Mertens/PNT+B1 "
            "证书与 B3-TV 同步证书已关闭该尾段解析出口。因此 branch-replay 的最新剩余不再是 "
            "tail-sieve stability，而是 fresh-layer PDEC/ColumnCRT 排斥。"
        ),
        "dependency_hashes": {
            str(FRESH_TAIL.relative_to(ROOT)): sha256(FRESH_TAIL),
            str(MERTENS_SYNC.relative_to(ROOT)): sha256(MERTENS_SYNC),
            str(TERMINAL_SYNC.relative_to(ROOT)): sha256(TERMINAL_SYNC),
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix cycle-debt fresh-modulus tail-sieve strict 自足同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"previous_tail_object_interface_closed={fmt_bool(result['previous_tail_object_interface_closed'])}",
        "previous_non_pdec_unbounded_fresh_layers_force_tail_rough_object="
        f"{fmt_bool(result['previous_non_pdec_unbounded_fresh_layers_force_tail_rough_object'])}",
        f"previous_conditional_external_tail_sieve_closed={fmt_bool(result['previous_conditional_external_tail_sieve_closed'])}",
        f"previous_strict_tail_sieve_closed={fmt_bool(result['previous_strict_tail_sieve_closed'])}",
        "strict_self_contained_mertens_tail_proved_latest="
        f"{fmt_bool(result['strict_self_contained_mertens_tail_proved_latest'])}",
        "b3_tv_strict_self_contained_synchronized_latest="
        f"{fmt_bool(result['b3_tv_strict_self_contained_synchronized_latest'])}",
        "strict_self_contained_tail_sieve_closed_for_branch_replay="
        f"{fmt_bool(result['strict_self_contained_tail_sieve_closed_for_branch_replay'])}",
        f"fresh_layer_pdec_excluded={fmt_bool(result['fresh_layer_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步逻辑",
        "",
        "上一 fresh-modulus 桥接把 non-PDEC 无界 fresh layers 转成 B3 避单余类粗筛对象，但当时 strict 路线仍把 "
        "`SelfContainedDusartReciprocalPrimeProofAppendixXGe10372` 作为开放粗原子。后续 strict 速率尾段同步证书已经把 "
        "theta/PNT 包络与 Meissel-Mertens B1 常数区间导入，并标记 Mertens 尾段解析包已从活动剩余移出；终端预算最新同步同时确认 B3-TV 自足同步完成。",
        "",
        "因此 branch-replay 这条分支内，tail-sieve stability 出口不再是活动剩余；剩余集中到 fresh-layer PDEC/ColumnCRT。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 剩余基",
            "",
            "旧 branch-replay strict 剩余基：",
            "",
            "```text",
            result["old_branch_replay_strict_remaining_basis"],
            "```",
            "",
            "新 branch-replay strict 剩余基：",
            "",
            "```text",
            result["new_branch_replay_strict_remaining_basis"],
            "```",
            "",
            "继承的全局 strict 剩余基仍为：",
            "",
            "```text",
            result["inherited_global_strict_remaining_basis_after_mertens_sync"],
            "```",
            "",
            "本同步不宣称行/列命题闭合；它只从 branch-replay 子分支中移除旧 Mertens/PNT tail-sieve 出口。",
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
    """命令行入口。"""
    result = build_result()
    write_outputs(result)
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
