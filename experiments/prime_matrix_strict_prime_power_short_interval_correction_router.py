#!/usr/bin/env python3
"""生成 strict 短区间 psi 素数幂修正证书。

用法示例：
  python3 experiments/prime_matrix_strict_prime_power_short_interval_correction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-prime-power-short-interval-correction-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-prime-power-short-interval-correction-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-prime-power-short-interval-correction-router.md"

SHORT_INCREMENT = MONOGRAPH / "prime-matrix-strict-short-interval-psi-increment-router.json"
NODE_SLACK = MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-slack-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [SHORT_INCREMENT, NODE_SLACK, CLAIM_STATUS]

TARGET = "PrimePowerShortIntervalCorrectionLedger"
BT_INPUT = "BrunTitchmarshShortIntervalPrimeCountUpperLedger"
NODE_HASH = "MiddlePsiFineMeshNodeSlackFloorAndHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

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


def exponent_rows() -> list[dict[str, Any]]:
    """给出每个指数 k>=2 的保守贡献预算。"""
    y = X_RIGHT + MESH_H
    k_max = math.floor(math.log(y, 2))
    rows = []
    for k in range(2, k_max + 1):
        base_width_at_left = (X_LEFT + MESH_H) ** (1.0 / k) - X_LEFT ** (1.0 / k)
        conservative_base_count = 2
        weight_bound = math.log(y) / k
        rows.append(
            {
                "k": k,
                "base_width_at_left": base_width_at_left,
                "base_width_below_one": base_width_at_left < 1.0,
                "conservative_base_count": conservative_base_count,
                "weight_bound_per_hit": weight_bound,
                "contribution_bound": conservative_base_count * weight_bound,
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造素数幂短区间修正证书。"""
    short = load_json(SHORT_INCREMENT)
    node = load_json(NODE_SLACK)
    rows_by_k = exponent_rows()
    total_bound = sum(float(item["contribution_bound"]) for item in rows_by_k)
    width_all_subunit = all(item["base_width_below_one"] for item in rows_by_k)
    reserve_margin = PRIME_POWER_RESERVE - total_bound
    reserve_sufficient = reserve_margin > 0
    active = TARGET in short.get("open_gates", [])
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            short.get("counterexample_assumption_only") is True
            and short.get("row_column_unconditional_closed") is False,
            True,
            "本步只补 psi 短区间增量中的素数幂误差，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "PrimePowerCorrectionGateActive",
            active,
            True,
            "短区间增量账本把 psi 增量拆成素数项和素数幂修正，本步处理 k>=2 的修正。",
            TARGET,
        ),
        row(
            "ExponentRangeLedger",
            len(rows_by_k) > 0 and rows_by_k[-1]["k"] == math.floor(math.log(X_RIGHT + MESH_H, 2)),
            True,
            "在本区间内只需检查 2<=k<=floor(log_2(x_right+h)) 的素数幂。",
            "none",
        ),
        row(
            "SubunitBaseWidthLedger",
            width_all_subunit,
            True,
            "对每个 k>=2，长度 1e6 的区间投影到 p 变量后的宽度小于 1；保守地每个 k 只预留 2 个命中。",
            "none",
        ),
        row(
            "UniformPrimePowerWeightBudgetLedger",
            reserve_sufficient,
            True,
            "素数幂总权重保守上界约 1.84e2，远小于 20000 预留。",
            "none",
        ),
        row(
            TARGET,
            reserve_sufficient,
            True,
            "百万网格每段的素数幂修正被 20000 预留无条件吸收。",
            "none",
        ),
        row(
            "CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger",
            False,
            False,
            "素数幂包已闭合后，短区间总包还剩 BT 素数计数输入和细网格节点余量/hash。",
            f"{BT_INPUT} AND {NODE_HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "素数幂短区间修正不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_prime_power_short_interval_correction_router",
        "status": "prime_power_short_interval_correction_closed_bt_and_node_hash_still_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "prime_power_short_interval_correction_closed": reserve_sufficient,
        "prime_power_reserve": PRIME_POWER_RESERVE,
        "prime_power_total_bound": total_bound,
        "prime_power_reserve_margin": reserve_margin,
        "subunit_base_width_all_exponents": width_all_subunit,
        "certified_short_interval_psi_increment_upper_closed": False,
        "brun_titchmarsh_short_interval_input_closed": False,
        "middle_psi_fine_mesh_node_slack_floor_hash_closed": node.get(
            "middle_psi_fine_mesh_node_slack_floor_hash_closed"
        )
        is True,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "x_left": X_LEFT,
        "x_right": X_RIGHT,
        "mesh_h": MESH_H,
        "k_min": 2,
        "k_max": rows_by_k[-1]["k"],
        "exponent_rows": rows_by_k,
        "replacement_after_this": {
            "CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger": f"{BT_INPUT} AND {NODE_HASH}",
            TARGET: "closed by elementary prime-power interval budget in this certificate",
        },
        "next_direct_attack_target": BT_INPUT,
        "parallel_attack_targets": [NODE_HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "素数幂修正包可以关闭：在 8e11 到 e^28 的百万短区间中，k>=2 的底数投影宽度都小于 1；"
            "即使用每个指数预留 2 个命中的保守算法，总权重也只有约 1.84e2，远低于短区间账本中的 20000 预留。"
            "因此短区间总包现在实质只剩 Brun-Titchmarsh 素数计数输入和细网格节点余量/hash。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 短区间 psi 素数幂修正路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prime_power_short_interval_correction_closed={fmt_bool(result['prime_power_short_interval_correction_closed'])}",
        f"prime_power_total_bound={fmt_float(float(result['prime_power_total_bound']))}",
        f"prime_power_reserve={fmt_float(float(result['prime_power_reserve']))}",
        f"prime_power_reserve_margin={fmt_float(float(result['prime_power_reserve_margin']))}",
        f"certified_short_interval_psi_increment_upper_closed={fmt_bool(result['certified_short_interval_psi_increment_upper_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 指数预算",
        "",
        "| k | base_width_at_left | contribution_bound | below_one |",
        "| ---: | ---: | ---: | --- |",
    ]
    for item in result["exponent_rows"]:
        lines.append(
            f"| `{item['k']}` | `{fmt_float(float(item['base_width_at_left']))}` | "
            f"`{fmt_float(float(item['contribution_bound']))}` | `{fmt_bool(item['base_width_below_one'])}` |"
        )
    lines.extend(["", "## 2. 剩余替换", "", "```text"])
    for key, value in result["replacement_after_this"].items():
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
