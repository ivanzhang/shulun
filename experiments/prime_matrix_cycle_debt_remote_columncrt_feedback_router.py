#!/usr/bin/env python3
"""生成 remote P-space ColumnCRT 的反馈回流证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_remote_columncrt_feedback_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-remote-columncrt-feedback-ledger.json

输出：
  data/prime-matrix-cycle-debt-remote-columncrt-feedback-ledger.json
  docs/monograph/prime-matrix-cycle-debt-remote-columncrt-feedback-router.json
  docs/monograph/prime-matrix-cycle-debt-remote-columncrt-feedback-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SUPPORT_GLOBAL = DATA / "prime-matrix-cycle-debt-fresh-support-motion-global-ledger.json"
POST100000 = DATA / "prime-matrix-cycle-debt-post100000-tail-atom-exact-ledger.json"
FRESH_ESCALATION = DATA / "prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json"
TAIL_SYNC = DATA / "prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-remote-columncrt-feedback-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-remote-columncrt-feedback-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-remote-columncrt-feedback-router.md"

PREVIOUS_TARGET = "RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter"
NEXT_TARGET = "MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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
    """构造 remote ColumnCRT 反馈路由证书。"""
    support = load_json(SUPPORT_GLOBAL)
    post = load_json(POST100000)
    fresh = load_json(FRESH_ESCALATION)
    tail = load_json(TAIL_SYNC)

    remote_blocks = []
    fresh_by_label = {item["label"]: item for item in fresh["fresh_layers"]}
    for block in support["blocks"]:
        fresh_layer = fresh_by_label[block["label"]]
        remote_blocks.append(
            {
                "label": block["label"],
                "support_width": block["support_width"],
                "audit_slot_count": block["audit_slot_count"],
                "p_space_columncrt_modulus_log10": block["p_space_columncrt_modulus_log10"],
                "log10_p_space_margin_over_support_width": block[
                    "log10_p_space_margin_over_support_width"
                ],
                "first_fresh_prime": fresh_layer["fresh_prime_sample"][0],
                "first_fresh_log10_gain": fresh_layer["first_fresh_log10_gain"],
                "sample_fresh_log10_gain": fresh_layer["sample_log10_gain"],
                "remote_plus_first_fresh_log10": (
                    block["p_space_columncrt_modulus_log10"]
                    + fresh_layer["first_fresh_log10_gain"]
                ),
                "remote_plus_sample_fresh_log10": (
                    block["p_space_columncrt_modulus_log10"]
                    + fresh_layer["sample_log10_gain"]
                ),
            }
        )

    finite_atoms_closed = bool(post["aggregate"]["finite_atom_branch_closed_for_registered_atoms"])
    fixed_finite_closed = bool(fresh["aggregate"]["finite_crt_terminal_description_excluded"])
    persistent_requires_fresh = bool(fresh["aggregate"]["persistent_family_requires_unbounded_modulus_or_pdec"])
    tail_closed = bool(tail["strict_self_contained_tail_sieve_closed_for_branch_replay"])
    local_support_closed = bool(support["registered_support_motion_escape_closed"])
    remote_route_imported = bool(support["persistent_registered_replay_routes_to_columncrt_pdec"])

    bare_remote_terminal_closed = (
        remote_route_imported
        and finite_atoms_closed
        and fixed_finite_closed
        and persistent_requires_fresh
        and tail_closed
        and local_support_closed
    )

    gates = [
        gate(
            "RemotePspaceColumnCRTImported",
            remote_route_imported,
            True,
            "上一证书已证明 registered block 若无限复现，只能提升为远程 P-space ColumnCRT/PDEC 类。",
            "remote registered P-space ColumnCRT",
        ),
        gate(
            "RegisteredFiniteAtomsAlreadyAbsorbed",
            finite_atoms_closed,
            True,
            "post-100000 exact runner 已关闭当前登记有限原子分支；孤立远程原子不能作为全局逃逸。",
            "closed for registered finite atoms",
        ),
        gate(
            "FixedFiniteRemoteCRTNotTerminal",
            fixed_finite_closed,
            True,
            "fresh-modulus escalation 证书已证明固定有限 CRT replay 类不是无限反例链的终端稳定结构。",
            "unbounded fresh modulus or PDEC",
        ),
        gate(
            "NonPDECFreshTailSieveClosed",
            tail_closed,
            True,
            "若无 fresh-layer PDEC/ColumnCRT，则无界 fresh layers 已接入 B3 tail-sieve 对象并由 strict 同步关闭。",
            "closed unless fresh-layer PDEC materializes",
        ),
        gate(
            "LocalSupportMotionAlreadyClosed",
            local_support_closed,
            True,
            "本地投影碰撞和本地 support-motion 逃逸均已关闭；剩余不再是本地漂移。",
            "closed",
        ),
        gate(
            "BareRemotePspaceColumnCRTTerminalClosed",
            bare_remote_terminal_closed,
            True,
            "远程 P-space ColumnCRT 若只是裸固定周期类，则被有限原子、固定有限 CRT 非终端和 non-PDEC tail-sieve 闭合链吸收。",
            "materialized fresh-layer PDEC/ColumnCRT or unregistered moving family",
        ),
        gate(
            "MaterializedFreshLayerPDECColumnCRTStillOpen",
            False,
            False,
            "若远程类在某个新素数层实际产生相位复用/碰撞/PDEC 载荷，本证书尚未排斥该材料化 PDEC/ColumnCRT。",
            "MaterializedFreshLayerPDECColumnCRTExclusion",
        ),
        gate(
            "UnregisteredMovingFamilyStillOpen",
            False,
            False,
            "若阻断包、shape 或来源签名改变，则它不是 registered remote ColumnCRT，而是未登记 moving family。",
            "UnregisteredMovingFamilyRouter",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭裸远程周期终端解释，但不排斥材料化 fresh-layer PDEC 或未登记 moving family。",
            NEXT_TARGET,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_cycle_debt_remote_columncrt_feedback_router",
        "status": "bare_remote_pspace_columncrt_terminal_closed_materialized_fresh_layer_pdec_or_unregistered_moving_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_TARGET,
        "registered_remote_block_count": len(remote_blocks),
        "minimum_remote_pspace_columncrt_modulus_log10": min(
            block["p_space_columncrt_modulus_log10"] for block in remote_blocks
        ),
        "maximum_remote_pspace_columncrt_modulus_log10": max(
            block["p_space_columncrt_modulus_log10"] for block in remote_blocks
        ),
        "minimum_first_fresh_log10_gain": min(
            block["first_fresh_log10_gain"] for block in remote_blocks
        ),
        "minimum_sample_fresh_log10_gain": min(
            block["sample_fresh_log10_gain"] for block in remote_blocks
        ),
        "remote_pspace_columncrt_imported": remote_route_imported,
        "registered_finite_atoms_absorbed": finite_atoms_closed,
        "fixed_finite_remote_crt_not_terminal": fixed_finite_closed,
        "persistent_remote_requires_unbounded_fresh_modulus_or_pdec": persistent_requires_fresh,
        "non_pdec_fresh_tail_sieve_closed": tail_closed,
        "local_support_motion_closed": local_support_closed,
        "bare_remote_pspace_columncrt_terminal_closed": bare_remote_terminal_closed,
        "materialized_fresh_layer_pdec_columncrt_excluded": False,
        "unregistered_moving_family_excluded": False,
        "row_column_unconditional_closed": False,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "remote_blocks": remote_blocks,
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "remote P-space ColumnCRT 不能再作为裸固定周期终端保留：孤立有限原子已由 exact runner 吸收，"
            "固定有限 CRT 类已由 fresh-modulus escalation 证明为非终端，且 non-PDEC 无界 fresh layers 已由 tail-sieve "
            "strict 同步关闭。因此剩余必须是某个新素数层已经材料化的 PDEC/ColumnCRT，或阻断包改变后的未登记 moving family。"
        ),
        "dependency_hashes": {
            str(SUPPORT_GLOBAL.relative_to(ROOT)): sha256(SUPPORT_GLOBAL),
            str(POST100000.relative_to(ROOT)): sha256(POST100000),
            str(FRESH_ESCALATION.relative_to(ROOT)): sha256(FRESH_ESCALATION),
            str(TAIL_SYNC.relative_to(ROOT)): sha256(TAIL_SYNC),
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
        "# Prime Matrix cycle-debt remote ColumnCRT feedback router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"registered_remote_block_count={result['registered_remote_block_count']}",
        "minimum_remote_pspace_columncrt_modulus_log10="
        f"{result['minimum_remote_pspace_columncrt_modulus_log10']:.3f}",
        "maximum_remote_pspace_columncrt_modulus_log10="
        f"{result['maximum_remote_pspace_columncrt_modulus_log10']:.3f}",
        f"minimum_first_fresh_log10_gain={result['minimum_first_fresh_log10_gain']:.3f}",
        f"minimum_sample_fresh_log10_gain={result['minimum_sample_fresh_log10_gain']:.3f}",
        f"registered_finite_atoms_absorbed={fmt_bool(result['registered_finite_atoms_absorbed'])}",
        "fixed_finite_remote_crt_not_terminal="
        f"{fmt_bool(result['fixed_finite_remote_crt_not_terminal'])}",
        "non_pdec_fresh_tail_sieve_closed="
        f"{fmt_bool(result['non_pdec_fresh_tail_sieve_closed'])}",
        "bare_remote_pspace_columncrt_terminal_closed="
        f"{fmt_bool(result['bare_remote_pspace_columncrt_terminal_closed'])}",
        "materialized_fresh_layer_pdec_columncrt_excluded="
        f"{fmt_bool(result['materialized_fresh_layer_pdec_columncrt_excluded'])}",
        f"unregistered_moving_family_excluded={fmt_bool(result['unregistered_moving_family_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 反馈闭合逻辑",
        "",
        "上一接口中的 `RemotePspaceColumnCRT` 有两种含义必须分开：",
        "",
        "- 如果它只是裸固定远程周期类，则它已经落回旧 `BranchReplayColumnCRTPDECExclusion` 链；有限原子、固定有限 CRT 终端和 non-PDEC tail-sieve 出口均已被已有证书吸收。",
        "- 如果它在某个新素数层真实产生相位复用、投影碰撞或载荷集中，则它不再是裸远程周期类，而是材料化的 fresh-layer PDEC/ColumnCRT。",
        "",
        "因此当前接口不应继续写成宽泛的 remote ColumnCRT，而应改写为材料化 fresh-layer PDEC/ColumnCRT 或未登记 moving family。",
        "",
        "## 2. remote blocks",
        "",
        "| block | support | audit | log10 P-space CRT | +first fresh | +sample fresh |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for block in result["remote_blocks"]:
        lines.append(
            "| `{label}` | {support_width} | {audit_slot_count} | "
            "{p_space_columncrt_modulus_log10:.3f} | {remote_plus_first_fresh_log10:.3f} | "
            "{remote_plus_sample_fresh_log10:.3f} |".format(**block)
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
            result["next_direct_attack_target"],
            "```",
            "",
            "本证书不排斥材料化 fresh-layer PDEC/ColumnCRT，也不排斥未登记 moving family；它只把裸 remote P-space ColumnCRT 终端解释从剩余接口中删除。",
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
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps({
        "status": result["status"],
        "bare_remote_pspace_columncrt_terminal_closed": result[
            "bare_remote_pspace_columncrt_terminal_closed"
        ],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
