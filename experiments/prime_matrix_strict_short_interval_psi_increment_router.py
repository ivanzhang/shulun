#!/usr/bin/env python3
"""生成 strict 中段短区间 psi 增量上界路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_short_interval_psi_increment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-short-interval-psi-increment-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-short-interval-psi-increment-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-short-interval-psi-increment-router.md"

MIDDLE_COVER = MONOGRAPH / "prime-matrix-strict-middle-finite-interval-psi-cover-router.json"
MIDDLE_SOURCE = MONOGRAPH / "prime-matrix-strict-middle-psi-upper-source-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [MIDDLE_COVER, MIDDLE_SOURCE, CLAIM_STATUS]

TARGET = "CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger"
BT_INPUT = "BrunTitchmarshShortIntervalPrimeCountUpperLedger"
PRIME_POWER = "PrimePowerShortIntervalCorrectionLedger"
MESH_ARITH = "MillionMeshBrunTitchmarshIncrementArithmeticLedger"
NODE_SLACK = "MiddlePsiFineMeshNodeSlackFloorAndHashLedger"
FINE_MESH = "MiddlePsiFineMeshComputationAndHashLedger"
JUMP_CONTROL = "PrimePowerJumpLocalizationOrUpperEnvelopeLedger"
ROUNDING = "MiddlePsiUpperDirectedRoundingLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TARGET_RATIO = 1.00002841
X_LEFT = 8.0e11
X_RIGHT = math.exp(28)
MESH_H = 1_000_000.0
PRIME_POWER_RESERVE = 20_000.0


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """稳定输出浮点。"""
    return f"{value:.15e}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def bt_prime_increment_bound(h: float, y: float) -> float:
    """Brun-Titchmarsh 型素数增量转为 theta 权的保守上界。"""
    return 2.0 * h * math.log(y) / math.log(h)


def arithmetic_profile() -> dict[str, float | bool]:
    """给出百万网格下的短区间增量预算。"""
    y = X_RIGHT + MESH_H
    prime_bound = bt_prime_increment_bound(MESH_H, y)
    total_bound = prime_bound + PRIME_POWER_RESERVE
    target_linear_allowance = TARGET_RATIO * MESH_H
    required_node_slack = max(0.0, total_bound - target_linear_allowance)
    interval_count = math.ceil((X_RIGHT - X_LEFT) / MESH_H)
    return {
        "mesh_h": MESH_H,
        "x_left": X_LEFT,
        "x_right": X_RIGHT,
        "interval_count": interval_count,
        "bt_prime_increment_bound": prime_bound,
        "prime_power_reserve": PRIME_POWER_RESERVE,
        "total_increment_bound": total_bound,
        "target_linear_allowance": target_linear_allowance,
        "required_node_slack_floor": required_node_slack,
        "arithmetic_feasible_if_node_slack_floor_available": required_node_slack < 4_000_000.0,
    }


def build_result() -> dict[str, Any]:
    """构造短区间 psi 增量上界证书。"""
    cover = load_json(MIDDLE_COVER)
    middle_source = load_json(MIDDLE_SOURCE)
    active = cover.get("next_direct_attack_target") == TARGET
    source_ready = middle_source.get("middle_psi_upper_use_site_closed") is True
    profile = arithmetic_profile()
    arithmetic_feasible = bool(profile["arithmetic_feasible_if_node_slack_floor_available"])
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            cover.get("counterexample_assumption_only") is True
            and cover.get("row_column_unconditional_closed") is False,
            True,
            "本步只审计假设反例链可调用的中段短区间增量，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ShortIntervalPsiIncrementGateActive",
            active and source_ready,
            True,
            "中段覆盖证书已把点间逃逸压成短区间 psi 增量上界。",
            TARGET,
        ),
        row(
            MESH_ARITH,
            arithmetic_feasible,
            True,
            "取百万级网格时，Brun-Titchmarsh 型素数增量加素数幂预留后，只需每个节点保留约 3.07e6 绝对余量。",
            NODE_SLACK,
        ),
        row(
            BT_INPUT,
            False,
            False,
            "需要登记或自足证明适用于本区间和网格长度的 Brun-Titchmarsh 短区间素数计数上界。",
            "classical Brun-Titchmarsh input or internal proof",
        ),
        row(
            PRIME_POWER,
            False,
            False,
            "需要证明百万网格内素数幂贡献小于预留 20000，或给出更紧可复算包络。",
            JUMP_CONTROL,
        ),
        row(
            NODE_SLACK,
            False,
            False,
            "需要约 646258 个百万网格节点的 psi 值或上界，并证明每个节点有足够目标余量。",
            FINE_MESH,
        ),
        row(
            TARGET,
            False,
            False,
            "增量算术路径可行，但短区间上界输入、素数幂修正和节点余量/hash 尚未闭合。",
            f"{BT_INPUT} AND {PRIME_POWER} AND {NODE_SLACK}",
        ),
        row(
            "FineMeshAlternativeStillOpen",
            False,
            False,
            "若不采用 Brun-Titchmarsh 增量包，则需要直接给出全段精细网格、跳点定位和外向舍入证书。",
            f"{FINE_MESH} AND {JUMP_CONTROL} AND {ROUNDING}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "短区间增量审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_short_interval_psi_increment_router",
        "status": "short_interval_increment_arithmetic_feasible_node_slack_and_bt_inputs_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "million_mesh_increment_arithmetic_closed": arithmetic_feasible,
        "certified_short_interval_psi_increment_upper_closed": False,
        "brun_titchmarsh_short_interval_input_closed": False,
        "prime_power_short_interval_correction_closed": False,
        "middle_psi_fine_mesh_node_slack_floor_hash_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "arithmetic_profile": profile,
        "replacement_self_contained": {
            TARGET: f"{BT_INPUT} AND {PRIME_POWER} AND {NODE_SLACK}",
            NODE_SLACK: "machine-readable node table on mesh h=1e6 with psi-node slack >= required_node_slack_floor",
        },
        "next_direct_attack_target": NODE_SLACK,
        "parallel_attack_targets": [BT_INPUT, PRIME_POWER, FINE_MESH, JUMP_CONTROL, ROUNDING],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "短区间增量路线出现了可行的数值骨架：用长度 1e6 的网格，Brun-Titchmarsh 型素数增量上界"
            "加 20000 的素数幂预留后，每个节点只需约 3.07e6 的绝对余量即可防止点间逃逸。"
            "但这还不是闭合证明；仍需 Brun-Titchmarsh 输入、素数幂修正，以及约 646258 个节点的 psi 余量/hash。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    profile = result["arithmetic_profile"]
    lines = [
        "# Prime Matrix strict 中段短区间 psi 增量上界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"million_mesh_increment_arithmetic_closed={fmt_bool(result['million_mesh_increment_arithmetic_closed'])}",
        f"certified_short_interval_psi_increment_upper_closed={fmt_bool(result['certified_short_interval_psi_increment_upper_closed'])}",
        f"brun_titchmarsh_short_interval_input_closed={fmt_bool(result['brun_titchmarsh_short_interval_input_closed'])}",
        f"prime_power_short_interval_correction_closed={fmt_bool(result['prime_power_short_interval_correction_closed'])}",
        f"middle_psi_fine_mesh_node_slack_floor_hash_closed={fmt_bool(result['middle_psi_fine_mesh_node_slack_floor_hash_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 百万网格算术画像",
        "",
        "```text",
    ]
    for key, value in profile.items():
        if isinstance(value, bool):
            lines.append(f"{key}={fmt_bool(value)}")
        else:
            lines.append(f"{key}={fmt_float(float(value))}")
    lines.extend(["```", "", "## 2. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 3. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
