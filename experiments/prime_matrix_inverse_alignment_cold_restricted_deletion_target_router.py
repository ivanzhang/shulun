#!/usr/bin/env python3
"""生成 exact-x cold-restricted 所需删除量目标表。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_cold_restricted_deletion_target_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-cold-restricted-deletion-target-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-cold-restricted-deletion-target-router.json
  docs/monograph/prime-matrix-inverse-alignment-cold-restricted-deletion-target-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-cold-restricted-deletion-target-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-cold-restricted-deletion-target-router.md"

EXACT_OBSTRUCTION = DOCS / "prime-matrix-inverse-alignment-exact-x-runner-obstruction-router.json"
SOURCE_FILES = [
    EXACT_OBSTRUCTION,
    DOCS / "prime-matrix-inverse-alignment-exact-x-budget-interface-router.json",
    DOCS / "prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json",
    DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json",
    DOCS / "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
]

COLD_DELETION = "ColdRestrictedExactXSupplyDeletionLedger"
DELETION_LOWER = "ColdRestrictionDeletionLowerBoundAgainstExactXTable"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
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
        "experiments/prime_matrix_inverse_alignment_cold_restricted_deletion_target_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def deletion_target_rows(obstruction: dict[str, Any]) -> list[dict[str, Any]]:
    """由 raw suffix capacity 与 exact M# 计算严格余量所需删除量。"""
    rows: list[dict[str, Any]] = []
    for item in obstruction.get("obstruction_rows", []):
        raw_capacity = int(item["raw_suffix_capacity"])
        msharp = float(item["Msharp"])
        raw_gap = raw_capacity - msharp
        required = max(0, math.floor(raw_gap) + 1)
        rows.append(
            {
                "P": int(item["P"]),
                "x": int(item["x"]),
                "z": int(item["z"]),
                "Msharp": round(msharp, 12),
                "raw_suffix_capacity": raw_capacity,
                "raw_gap": round(raw_gap, 12),
                "minimum_integer_deletion_for_strict_margin": required,
                "remaining_capacity_after_required_deletion": raw_capacity - required,
                "strict_margin_after_required_deletion": (raw_capacity - required) < msharp,
                "required_deletion_fraction_of_raw_suffix": round(required / raw_capacity, 9)
                if raw_capacity
                else 0.0,
            }
        )
    return rows


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ExactXRawCapacityObstructionImported",
            "closed": result["exact_x_raw_capacity_obstruction_imported"],
            "proved": result["exact_x_raw_capacity_obstruction_imported"],
            "meaning": "上一层已证明 raw suffix 容量路线不足。",
            "remaining": COLD_DELETION,
        },
        {
            "gate": "RequiredDeletionFormulaClosed",
            "closed": result["required_deletion_formula_closed"],
            "proved": result["required_deletion_formula_closed"],
            "meaning": "若 raw capacity 为整数 C，严格余量需要删除至少 floor(C-M#)+1 个单位。",
            "remaining": DELETION_LOWER,
        },
        {
            "gate": "ExactXDeletionTargetTableClosed",
            "closed": result["exact_x_deletion_target_table_closed"],
            "proved": result["exact_x_deletion_target_table_closed"],
            "meaning": "样本 exact x 的所需 cold 删除量已生成。",
            "remaining": DELETION_LOWER,
        },
        {
            "gate": "ColdReturnRoutesImported",
            "closed": result["cold_return_routes_imported"],
            "proved": result["cold_return_routes_imported"],
            "meaning": "可用删除来源只能是 cold/no-return guard、热/固定回流、共同核无免费循环与 PDEC/SAE。",
            "remaining": COLD_NUMERIC,
        },
        {
            "gate": "ColdRestrictedExactXSupplyDeletionLedgerClosed",
            "closed": result["cold_restricted_exact_x_supply_deletion_ledger_closed"],
            "proved": result["cold_restricted_exact_x_supply_deletion_ledger_closed"],
            "meaning": "删除量目标表闭合，但删除量下界尚未证明。",
            "remaining": DELETION_LOWER,
        },
        {
            "gate": "ColdRestrictionDeletionLowerBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明真实 cold 限制至少删除目标表所需单位。",
            "remaining": DELETION_LOWER,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "非持久删除量下界、持久 moving atom 与 DStructure/Rankin 仍未全部闭合。",
            "remaining": f"{DELETION_LOWER} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 cold-restricted 删除目标证书。"""
    obstruction = load_json(EXACT_OBSTRUCTION)
    cold_return = load_json(DOCS / "prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json")
    cold_after = load_json(DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json")
    anticascade = load_json(DOCS / "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json")
    cycle = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    rows = deletion_target_rows(obstruction)
    formula_closed = bool(rows) and all(item["strict_margin_after_required_deletion"] for item in rows)
    routes = (
        cold_return.get("cold_restricted_inverse_alignment_envelope_synced_to_return_frontier") is True
        and cold_after.get("effective_pruning_closed_for_nonpersistent_budget") is True
        and anticascade.get("canonical_cold_window_sibling_charging_isolated") is True
        and cycle.get("common_kernel_return_cycle_descent_or_pdec_proved") is True
    )
    ledger_closed = (
        obstruction.get("exact_x_runner_obstruction_closed") is True and formula_closed and routes
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_cold_restricted_deletion_target_router",
        "status": "cold_restricted_exact_x_deletion_target_table_closed_lower_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "exact_x_raw_capacity_obstruction_imported": obstruction.get("exact_x_runner_obstruction_closed") is True,
        "required_deletion_formula_closed": formula_closed,
        "exact_x_deletion_target_table_closed": formula_closed,
        "cold_return_routes_imported": routes,
        "cold_restricted_exact_x_supply_deletion_ledger_closed": ledger_closed,
        "cold_restriction_deletion_lower_bound_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "same_parameter_sparse_demand_cold_supply_strict_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": COLD_DELETION,
        "hardpoint_after_router": f"{DELETION_LOWER} AND {COLD_NUMERIC}",
        "next_direct_attack_target": DELETION_LOWER,
        "parallel_attack_targets": [COLD_NUMERIC, MOVING_ATOM, DSTRUCTURE],
        "deletion_target_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Cold-restricted exact-x 目标已经被量化：对每个 exact x 样本，若原始后缀容量为整数 C，"
            "要得到严格 `U_np<M#`，至少要删除 `floor(C-M#)+1` 个后缀容量单位。"
            "这把抽象的 cold deletion 需求变成可验目标表。当前仍未证明真实 cold/no-return/回流纪律"
            "一定达到该删除下界；下一最窄点是 `ColdRestrictionDeletionLowerBoundAgainstExactXTable`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix inverse alignment cold-restricted 删除目标路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_x_raw_capacity_obstruction_imported={fmt_bool(result['exact_x_raw_capacity_obstruction_imported'])}",
        f"required_deletion_formula_closed={fmt_bool(result['required_deletion_formula_closed'])}",
        f"exact_x_deletion_target_table_closed={fmt_bool(result['exact_x_deletion_target_table_closed'])}",
        f"cold_return_routes_imported={fmt_bool(result['cold_return_routes_imported'])}",
        f"cold_restricted_exact_x_supply_deletion_ledger_closed={fmt_bool(result['cold_restricted_exact_x_supply_deletion_ledger_closed'])}",
        f"cold_restriction_deletion_lower_bound_proved={fmt_bool(result['cold_restriction_deletion_lower_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 所需删除量表",
        "",
        "| P | X(P) | z | M# | raw C | required deletion | remaining C | deletion fraction |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["deletion_target_rows"]:
        lines.append(
            "| `{P}` | `{x}` | `{z}` | `{msharp}` | `{raw}` | `{required}` | `{remaining}` | `{fraction}` |".format(
                P=item["P"],
                x=item["x"],
                z=item["z"],
                msharp=item["Msharp"],
                raw=item["raw_suffix_capacity"],
                required=item["minimum_integer_deletion_for_strict_margin"],
                remaining=item["remaining_capacity_after_required_deletion"],
                fraction=item["required_deletion_fraction_of_raw_suffix"],
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
            "- 任务：证明真实 cold 限制、命名回流与无免费共同核循环至少删掉目标表所需容量。",
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
