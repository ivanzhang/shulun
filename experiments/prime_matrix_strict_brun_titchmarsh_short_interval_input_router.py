#!/usr/bin/env python3
"""生成 strict 短区间 Brun-Titchmarsh 输入登记证书。

用法示例：
  python3 experiments/prime_matrix_strict_brun_titchmarsh_short_interval_input_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-brun-titchmarsh-short-interval-input-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-brun-titchmarsh-short-interval-input-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-brun-titchmarsh-short-interval-input-router.md"

SHORT_INCREMENT = MONOGRAPH / "prime-matrix-strict-short-interval-psi-increment-router.json"
PRIME_POWER = MONOGRAPH / "prime-matrix-strict-prime-power-short-interval-correction-router.json"
NODE_SLACK = MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-slack-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [SHORT_INCREMENT, PRIME_POWER, NODE_SLACK, CLAIM_STATUS]

TARGET = "BrunTitchmarshShortIntervalPrimeCountUpperLedger"
NODE_HASH = "MiddlePsiFineMeshNodeSlackFloorAndHashLedger"
NODE_DATA = "DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

X_LEFT = 8.0e11
X_RIGHT = math.exp(28)
MESH_H = 1_000_000.0

EXTERNAL_SOURCES = [
    {
        "name": "Montgomery-Vaughan large sieve / explicit Brun-Titchmarsh interval form",
        "doi": "10.1112/S0025579300004708",
        "url": "https://doi.org/10.1112/S0025579300004708",
        "statement_used": "pi(x+y)-pi(x) <= 2y/log(y) for the q=1 short interval form",
    },
    {
        "name": "MathOverflow pointer to the Montgomery-Vaughan explicit interval form",
        "url": "https://mathoverflow.net/a/370956",
        "statement_used": "secondary pointer only; not a replacement for the theorem source",
    },
]


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


def bt_profile() -> dict[str, float | bool]:
    """计算 q=1 Brun-Titchmarsh 输入给出的 theta 型增量上界。"""
    prime_count_bound = 2.0 * MESH_H / math.log(MESH_H)
    log_weight_bound = math.log(X_RIGHT + MESH_H)
    theta_increment_bound = prime_count_bound * log_weight_bound
    return {
        "x_left": X_LEFT,
        "x_right": X_RIGHT,
        "mesh_h": MESH_H,
        "h_gt_one": MESH_H > 1.0,
        "short_interval_inside_positive_range": X_LEFT > MESH_H,
        "bt_prime_count_bound": prime_count_bound,
        "log_weight_bound": log_weight_bound,
        "theta_prime_increment_bound": theta_increment_bound,
    }


def build_result() -> dict[str, Any]:
    """构造 BT 短区间输入登记证书。"""
    short = load_json(SHORT_INCREMENT)
    prime_power = load_json(PRIME_POWER)
    node = load_json(NODE_SLACK)
    profile = bt_profile()
    prior_bound = float(short["arithmetic_profile"]["bt_prime_increment_bound"])
    matches_prior = abs(float(profile["theta_prime_increment_bound"]) - prior_bound) < 1e-6
    external_closed = bool(profile["h_gt_one"]) and bool(profile["short_interval_inside_positive_range"]) and matches_prior
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            short.get("counterexample_assumption_only") is True
            and short.get("row_column_unconditional_closed") is False,
            True,
            "本步只登记短区间素数计数外部输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ExternalBrunTitchmarshTheoremRegistered",
            external_closed,
            True,
            "采用 Montgomery-Vaughan 显式 Brun-Titchmarsh 的 q=1 区间形式作为外部黑箱。",
            "not self-contained",
        ),
        row(
            "ParameterMatchToMillionMesh",
            external_closed,
            True,
            "h=1e6>1，且所有起始点均在正区间内；每段素数个数用 2h/log h 控制。",
            "none",
        ),
        row(
            "ThetaWeightConversionArithmetic",
            matches_prior,
            True,
            "再乘以 log(x_right+h) 得到与短区间账本一致的素数部分 theta 权重上界。",
            "none",
        ),
        row(
            "BrunTitchmarshSelfContainedProof",
            False,
            False,
            "本文没有重证 Montgomery-Vaughan 大筛/Brun-Titchmarsh 定理；严格自足版仍需内部证明或可接受的定理引用政策。",
            "internal large sieve proof or accepted external theorem status",
        ),
        row(
            TARGET,
            external_closed,
            True,
            "在外部黑箱路线中，短区间素数计数输入已完成登记和参数匹配。",
            "self-contained proof remains open",
        ),
        row(
            "CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger",
            False,
            False,
            "BT 外部输入和素数幂修正已经处理后，短区间总包仍卡在细网格节点余量/hash。",
            NODE_HASH,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "BT 输入登记不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_brun_titchmarsh_short_interval_input_router",
        "status": "brun_titchmarsh_external_input_registered_self_contained_proof_open_node_hash_still_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "brun_titchmarsh_short_interval_input_external_closed": external_closed,
        "brun_titchmarsh_short_interval_input_self_contained_closed": False,
        "brun_titchmarsh_short_interval_input_closed_for_external_lane": external_closed,
        "prime_power_short_interval_correction_closed": prime_power.get("prime_power_short_interval_correction_closed") is True,
        "middle_psi_fine_mesh_node_slack_floor_hash_closed": node.get(
            "middle_psi_fine_mesh_node_slack_floor_hash_closed"
        )
        is True,
        "certified_short_interval_psi_increment_upper_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "bt_profile": profile,
        "prior_short_interval_bt_bound": prior_bound,
        "matches_prior_short_interval_bound": matches_prior,
        "external_sources": EXTERNAL_SOURCES,
        "replacement_after_this": {
            "CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger": NODE_HASH,
            TARGET: "closed on the external theorem lane; self-contained proof remains open",
            NODE_HASH: f"{NODE_DATA} AND NodeSlackFloorAuditLedger AND MeshCompletenessAndIndexHashLedger AND MiddlePsiUpperDirectedRoundingLedger",
        },
        "next_direct_attack_target": NODE_HASH,
        "parallel_attack_targets": ["BrunTitchmarshSelfContainedProof", NODE_DATA],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Brun-Titchmarsh 短区间素数计数输入可以在外部黑箱路线中登记："
            "用 pi(x+h)-pi(x)<=2h/log h，并乘以 log(e^28+h)，得到与原短区间账本相同的"
            "素数 theta 增量上界。严格自足版仍未重证该定理；在外部路线中，短区间总包现在只剩"
            "细网格节点余量/hash。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    profile = result["bt_profile"]
    lines = [
        "# Prime Matrix strict 短区间 Brun-Titchmarsh 输入登记器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"brun_titchmarsh_short_interval_input_external_closed={fmt_bool(result['brun_titchmarsh_short_interval_input_external_closed'])}",
        f"brun_titchmarsh_short_interval_input_self_contained_closed={fmt_bool(result['brun_titchmarsh_short_interval_input_self_contained_closed'])}",
        f"prime_power_short_interval_correction_closed={fmt_bool(result['prime_power_short_interval_correction_closed'])}",
        f"middle_psi_fine_mesh_node_slack_floor_hash_closed={fmt_bool(result['middle_psi_fine_mesh_node_slack_floor_hash_closed'])}",
        f"certified_short_interval_psi_increment_upper_closed={fmt_bool(result['certified_short_interval_psi_increment_upper_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 参数匹配",
        "",
        "```text",
    ]
    for key, value in profile.items():
        if isinstance(value, bool):
            lines.append(f"{key}={fmt_bool(value)}")
        else:
            lines.append(f"{key}={fmt_float(float(value))}")
    lines.extend(["```", "", "## 2. 外部来源", "", "| name | url | statement_used |", "| --- | --- | --- |"])
    for item in result["external_sources"]:
        lines.append(
            f"| {table_cell(item['name'])} | {table_cell(item['url'])} | {table_cell(item['statement_used'])} |"
        )
    lines.extend(["", "## 3. 剩余替换", "", "```text"])
    for key, value in result["replacement_after_this"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 4. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 5. 下一最窄点",
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
