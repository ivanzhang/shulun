#!/usr/bin/env python3
"""同步 fresh-layer 剩余接口中的支撑运动与远程 ColumnCRT 二分。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_fresh_support_motion_global_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-fresh-support-motion-global-ledger.json

输出：
  data/prime-matrix-cycle-debt-fresh-support-motion-global-ledger.json
  docs/monograph/prime-matrix-cycle-debt-fresh-support-motion-global-router.json
  docs/monograph/prime-matrix-cycle-debt-fresh-support-motion-global-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

LOCAL_COLLISION = DATA / "prime-matrix-cycle-debt-fresh-layer-local-collision-ledger.json"
SUPPORT_GAP = DATA / "prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json"
GLOBAL_DICHOTOMY = DATA / "prime-matrix-cycle-debt-branch-replay-global-dichotomy-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-fresh-support-motion-global-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-fresh-support-motion-global-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-fresh-support-motion-global-router.md"

PREVIOUS_TARGET = "FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion"
NEXT_TARGET = "RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter"


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
    """构造支撑运动全局路由证书。"""
    local = load_json(LOCAL_COLLISION)
    support = load_json(SUPPORT_GAP)
    global_router = load_json(GLOBAL_DICHOTOMY)

    support_agg = support["aggregate"]
    global_agg = global_router["aggregate"]

    local_collision_closed = bool(local["local_fresh_layer_projection_collision_excluded"])
    support_motion_closed = bool(support_agg["local_moving_slot_replay_excluded_for_registered_blocks"])
    far_replay_columncrt = bool(support_agg["far_replay_still_requires_columncrt_pdec"])
    persistent_routes_to_columncrt = bool(global_agg["persistent_registered_replay_routes_to_columncrt_pdec"])
    new_package_routes = bool(global_agg["new_blocker_package_routes_to_pdec_sae_or_new_router"])
    isolated_not_global = bool(global_agg["isolated_atoms_cannot_form_infinite_registered_family"])

    min_support_margin = min(
        block["log10_margin_over_support_width"] for block in support["replay_blocks"]
    )
    min_audit_margin = min(block["log10_margin_over_audit_slots"] for block in support["replay_blocks"])

    blocks = []
    columncrt_by_label = {item["label"]: item for item in global_router["columncrt_blocks"]}
    for item in support["replay_blocks"]:
        col = columncrt_by_label[item["label"]]
        blocks.append(
            {
                "label": item["label"],
                "support_width": item["support_width"],
                "audit_slot_count": item["audit_slot_count"],
                "cycle_replay_modulus_log10": item["replay_modulus_log10"],
                "p_space_columncrt_modulus_log10": col["p_space_columncrt_modulus_log10"],
                "log10_margin_over_support_width": item["log10_margin_over_support_width"],
                "log10_p_space_margin_over_support_width": col["p_space_margin_over_support_width_log10"],
                "local_support_motion_excluded": item["nonzero_replay_exceeds_support_width"],
                "persistent_remote_routes_to_columncrt": col["defines_columncrt_replay_class"],
            }
        )

    registered_support_motion_escape_closed = (
        local_collision_closed
        and support_motion_closed
        and far_replay_columncrt
        and persistent_routes_to_columncrt
        and isolated_not_global
    )

    gates = [
        gate(
            "FreshLocalCollisionAlreadyExcluded",
            local_collision_closed,
            True,
            "上一证书已排除 registered fresh layer 在本地 primitive support 内的投影碰撞。",
            "closed",
        ),
        gate(
            "RegisteredLocalSupportMotionExcluded",
            support_motion_closed,
            True,
            "support-gap replay lemma 已证明同一阻断包本地非零复现周期至少为 lcm(B)，且远超支撑宽度。",
            "closed for registered blocks",
        ),
        gate(
            "PersistentRegisteredRemoteReplayRoutesToPspaceColumnCRT",
            persistent_routes_to_columncrt,
            True,
            "全局二分已证明若某个 registered block 无限复现，则提升为固定 P-space ColumnCRT 类。",
            "RemotePspaceColumnCRTExclusion",
        ),
        gate(
            "IsolatedRegisteredAtomsNotGlobalEscape",
            isolated_not_global,
            True,
            "若没有 registered block 无限复现，则登记原子只是有限项，不能构成全局结构逃逸。",
            "closed as global escape",
        ),
        gate(
            "NewBlockerPackageRoutesToMovingFamily",
            new_package_routes,
            False,
            "若阻断包改变，则不再是 registered support motion，而是未登记 moving family，须另建 PDEC/SAE/ColumnCRT 路由。",
            "UnregisteredMovingFamilyRouter",
        ),
        gate(
            "RegisteredSupportMotionEscapeClosed",
            registered_support_motion_escape_closed,
            True,
            "本地碰撞和本地支撑漂移均已排除；registered 无限复现只能是远程 P-space ColumnCRT。",
            "closed except remote ColumnCRT",
        ),
        gate(
            "RemoteColumnCRTOrUnregisteredMovingFamilyStillOpen",
            False,
            False,
            "剩余不是本地支撑运动，而是远程 P-space ColumnCRT 排斥或未登记 moving family 的新路由。",
            NEXT_TARGET,
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只关闭 registered support-motion escape，不排斥远程 ColumnCRT 或未登记 moving-family。",
            NEXT_TARGET,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_cycle_debt_fresh_support_motion_global_router",
        "status": "registered_support_motion_escape_closed_remote_columncrt_or_unregistered_moving_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_TARGET,
        "period_p": support_agg["period_p"],
        "registered_block_count": len(blocks),
        "local_fresh_layer_projection_collision_excluded": local_collision_closed,
        "registered_local_support_motion_excluded": support_motion_closed,
        "far_replay_still_requires_columncrt_pdec": far_replay_columncrt,
        "persistent_registered_replay_routes_to_columncrt_pdec": persistent_routes_to_columncrt,
        "isolated_registered_atoms_cannot_form_global_escape": isolated_not_global,
        "new_blocker_package_routes_to_pdec_sae_or_new_router": new_package_routes,
        "registered_support_motion_escape_closed": registered_support_motion_escape_closed,
        "minimum_cycle_log10_margin_over_support_width": min_support_margin,
        "minimum_cycle_log10_margin_over_audit_slots": min_audit_margin,
        "minimum_p_space_columncrt_modulus_log10": global_agg["minimum_p_space_columncrt_modulus_log10"],
        "maximum_p_space_columncrt_modulus_log10": global_agg["maximum_p_space_columncrt_modulus_log10"],
        "remote_pspace_columncrt_excluded": False,
        "unregistered_moving_family_excluded": False,
        "row_column_unconditional_closed": False,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "blocks": blocks,
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "registered branch-replay 的 support-motion escape 已被同步关闭：本地 fresh-layer 投影碰撞已排除，"
            "同一阻断包本地非零支撑漂移又被 support-gap lcm 屏障排除；若 registered block 仍在全局无限复现，"
            "只能提升为远程 P-space ColumnCRT 类。剩余为 RemotePspaceColumnCRT 排斥或未登记 moving family 路由。"
        ),
        "dependency_hashes": {
            str(LOCAL_COLLISION.relative_to(ROOT)): sha256(LOCAL_COLLISION),
            str(SUPPORT_GAP.relative_to(ROOT)): sha256(SUPPORT_GAP),
            str(GLOBAL_DICHOTOMY.relative_to(ROOT)): sha256(GLOBAL_DICHOTOMY),
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix cycle-debt fresh support-motion 全局路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"period_p={result['period_p']}",
        f"registered_block_count={result['registered_block_count']}",
        "local_fresh_layer_projection_collision_excluded="
        f"{fmt_bool(result['local_fresh_layer_projection_collision_excluded'])}",
        f"registered_local_support_motion_excluded={fmt_bool(result['registered_local_support_motion_excluded'])}",
        "persistent_registered_replay_routes_to_columncrt_pdec="
        f"{fmt_bool(result['persistent_registered_replay_routes_to_columncrt_pdec'])}",
        "isolated_registered_atoms_cannot_form_global_escape="
        f"{fmt_bool(result['isolated_registered_atoms_cannot_form_global_escape'])}",
        f"registered_support_motion_escape_closed={fmt_bool(result['registered_support_motion_escape_closed'])}",
        f"minimum_cycle_log10_margin_over_support_width={result['minimum_cycle_log10_margin_over_support_width']:.3f}",
        f"minimum_p_space_columncrt_modulus_log10={result['minimum_p_space_columncrt_modulus_log10']:.3f}",
        f"remote_pspace_columncrt_excluded={fmt_bool(result['remote_pspace_columncrt_excluded'])}",
        f"unregistered_moving_family_excluded={fmt_bool(result['unregistered_moving_family_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步引理",
        "",
        "registered fresh-layer 剩余包含三种表面形态：本地投影碰撞、本地支撑漂移、远程复现。"
        "本地投影碰撞已由 fresh-layer 单射引理排除；本地支撑漂移已由同一阻断包的 `lcm(B)` 复现屏障排除。"
        "因此若 registered block 仍在全局反例链中无限复现，它不再是本地支撑运动，而必须是固定 P-space ColumnCRT 类。",
        "",
        "若阻断包改变，则它不属于 registered support-motion escape，而是未登记 moving family，需要新的 PDEC/SAE/ColumnCRT 路由。",
        "",
        "## 2. block 读数",
        "",
        "| block | support | audit | log10 cycle replay | log10 P-space CRT | local motion closed |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for block in result["blocks"]:
        lines.append(
            f"| `{block['label']}` | {block['support_width']} | {block['audit_slot_count']} | "
            f"{block['cycle_replay_modulus_log10']:.3f} | {block['p_space_columncrt_modulus_log10']:.3f} | "
            f"`{fmt_bool(block['local_support_motion_excluded'])}` |"
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
            "本证书不排斥远程 P-space ColumnCRT，也不排斥未登记 moving family；它只删除 registered support-motion escape 这个本地出口。",
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
