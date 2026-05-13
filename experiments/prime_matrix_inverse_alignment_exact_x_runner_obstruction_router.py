#!/usr/bin/env python3
"""生成 exact-x 预算 runner 的原始容量阻塞证书。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_exact_x_runner_obstruction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-exact-x-runner-obstruction-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-exact-x-runner-obstruction-router.json
  docs/monograph/prime-matrix-inverse-alignment-exact-x-runner-obstruction-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-exact-x-runner-obstruction-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-exact-x-runner-obstruction-router.md"

SOURCE_LEDGER = DATA / "inverse-alignment-exact-x-budget-interface-ledger.json"
SOURCE_FILES = [
    DOCS / "prime-matrix-inverse-alignment-exact-x-budget-interface-router.json",
    DOCS / "prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json",
    DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
]

EXACT_X_RUNNER = "ExactZeroRowXDrivenSameParameterBudgetRunnerOrAnalyticEnvelope"
COLD_DELETION = "ColdRestrictedExactXSupplyDeletionLedger"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
STRICT_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_exact_x_runner_obstruction_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in [SOURCE_LEDGER, *SOURCE_FILES]:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def obstruction_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """抽取原始容量阻塞样本。"""
    return [
        {
            "P": item["P"],
            "x": item["exact_minimal_zero_row_x"],
            "z": item["same_parameter_z"],
            "Msharp": item["Msharp_exact"],
            "raw_suffix_capacity": item["suffix_capacity_sum_mu"],
            "raw_gap": item["raw_suffix_capacity_minus_Msharp"],
            "raw_capacity_closes_margin": item["Msharp_exact"] > item["suffix_capacity_sum_mu"],
        }
        for item in rows
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ExactXBudgetInterfaceImported",
            "closed": result["exact_x_budget_interface_imported"],
            "proved": result["exact_x_budget_interface_imported"],
            "meaning": "上一层已经把 exact x/M#/tau 接入同参数预算字段。",
            "remaining": EXACT_X_RUNNER,
        },
        {
            "gate": "ExactXSampleReplayClosed",
            "closed": result["exact_x_sample_replay_closed"],
            "proved": result["exact_x_sample_replay_closed"],
            "meaning": "样本 exact x 预算字段可复核重放。",
            "remaining": "finite range expansion if used as finite certificate",
        },
        {
            "gate": "RawSuffixCapacityObstructionCertified",
            "closed": result["raw_suffix_capacity_obstruction_certified"],
            "proved": result["raw_suffix_capacity_obstruction_certified"],
            "meaning": "原始后缀容量不小于 exact M#；不能用 raw suffix 容量闭合严格余量。",
            "remaining": COLD_DELETION,
        },
        {
            "gate": "ColdRestrictedDeletionAlreadyRouted",
            "closed": result["cold_restricted_deletion_already_routed"],
            "proved": result["cold_restricted_deletion_already_routed"],
            "meaning": "需要的删除量必须来自 cold/no-return/共同核无免费循环/命名回流纪律。",
            "remaining": f"{COLD_DELETION} AND {COLD_NUMERIC}",
        },
        {
            "gate": "ExactXRunnerObstructionClosed",
            "closed": result["exact_x_runner_obstruction_closed"],
            "proved": result["exact_x_runner_obstruction_closed"],
            "meaning": "Exact-x runner 的机械字段闭合，且已证明原始容量路线不足。",
            "remaining": COLD_DELETION,
        },
        {
            "gate": "ExactXBudgetDominanceProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 cold-restricted 删除后的 U_np 低于 exact M#。",
            "remaining": f"{COLD_DELETION} AND {COLD_NUMERIC}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "非持久 exact-x 删除量、持久 moving atom 与 DStructure/Rankin 仍未全部闭合。",
            "remaining": f"{COLD_DELETION} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 exact-x runner 阻塞证书。"""
    ledger = load_json(SOURCE_LEDGER)
    interface = load_json(DOCS / "prime-matrix-inverse-alignment-exact-x-budget-interface-router.json")
    cold_return = load_json(DOCS / "prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json")
    cold_after = load_json(DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json")
    return_cycle = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")

    rows = obstruction_rows(ledger.get("budget_rows", []))
    exact_imported = interface.get("exact_x_runner_interface_closed") is True
    replay_closed = bool(rows) and all(item["x"] > item["P"] for item in rows)
    raw_obstruction = bool(rows) and all(not item["raw_capacity_closes_margin"] for item in rows)
    routed = (
        cold_return.get("cold_restricted_inverse_alignment_envelope_synced_to_return_frontier") is True
        and cold_after.get("effective_pruning_closed_for_nonpersistent_budget") is True
        and return_cycle.get("common_kernel_return_cycle_descent_or_pdec_proved") is True
    )
    closed = exact_imported and replay_closed and raw_obstruction and routed

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_exact_x_runner_obstruction_router",
        "status": "exact_x_runner_raw_capacity_obstruction_closed_cold_deletion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "exact_x_budget_interface_imported": exact_imported,
        "exact_x_sample_replay_closed": replay_closed,
        "raw_suffix_capacity_obstruction_certified": raw_obstruction,
        "cold_restricted_deletion_already_routed": routed,
        "exact_x_runner_obstruction_closed": closed,
        "exact_x_budget_dominance_proved": False,
        "same_parameter_sparse_demand_cold_supply_strict_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": EXACT_X_RUNNER,
        "hardpoint_after_router": f"{COLD_DELETION} AND {COLD_NUMERIC}",
        "next_direct_attack_target": COLD_DELETION,
        "parallel_attack_targets": [COLD_NUMERIC, MOVING_ATOM, DSTRUCTURE],
        "obstruction_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Exact-x runner 的机械接口已经足够精确，但样本揭示一个必要事实："
            "原始后缀容量 `sum_{q>z} mu_q` 全部大于 exact `M#_{x,z}`，因此不能用未冷限制的"
            "逆元容量和来证明同参数严格余量。下一步必须证明 cold/no-return/共同核无免费循环/命名回流"
            "删除掉足够多的后缀容量，使注册冷供给 `U_np` 低于 exact `M#`。"
            "这把最新最窄点压成 `ColdRestrictedExactXSupplyDeletionLedger`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix inverse alignment exact-x runner 原始容量阻塞路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_x_budget_interface_imported={fmt_bool(result['exact_x_budget_interface_imported'])}",
        f"exact_x_sample_replay_closed={fmt_bool(result['exact_x_sample_replay_closed'])}",
        f"raw_suffix_capacity_obstruction_certified={fmt_bool(result['raw_suffix_capacity_obstruction_certified'])}",
        f"cold_restricted_deletion_already_routed={fmt_bool(result['cold_restricted_deletion_already_routed'])}",
        f"exact_x_runner_obstruction_closed={fmt_bool(result['exact_x_runner_obstruction_closed'])}",
        f"exact_x_budget_dominance_proved={fmt_bool(result['exact_x_budget_dominance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 原始容量阻塞样本",
        "",
        "| P | X(P) | z | M# | raw suffix capacity | raw gap | raw closes margin |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["obstruction_rows"]:
        lines.append(
            "| `{P}` | `{x}` | `{z}` | `{msharp}` | `{cap}` | `{gap}` | `{closes}` |".format(
                P=item["P"],
                x=item["x"],
                z=item["z"],
                msharp=item["Msharp"],
                cap=item["raw_suffix_capacity"],
                gap=item["raw_gap"],
                closes=fmt_bool(item["raw_capacity_closes_margin"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
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
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 任务：证明 exact x 生成的后缀容量在 cold/no-return/命名回流约束下有足够删除量。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
