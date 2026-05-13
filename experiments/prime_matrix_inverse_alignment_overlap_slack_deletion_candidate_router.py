#!/usr/bin/env python3
"""生成 overlap/slack 作为 exact-x cold 删除源的候选证书。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_overlap_slack_deletion_candidate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-overlap-slack-deletion-candidate-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-overlap-slack-deletion-candidate-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-overlap-slack-deletion-candidate-router.md"

TARGET = DOCS / "prime-matrix-inverse-alignment-cold-restricted-deletion-target-router.json"
BUDGET_LEDGER = DATA / "inverse-alignment-exact-x-budget-interface-ledger.json"
SOURCE_FILES = [
    TARGET,
    BUDGET_LEDGER,
    DOCS / "prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.json",
    DOCS / "prime-matrix-strict-cold-window-sibling-charging-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
]

OVERLAP_MAP = "RegisteredOverlapSlackToColdSupplyDeletionMap"
DELETION_LOWER = "ColdRestrictionDeletionLowerBoundAgainstExactXTable"
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
        "experiments/prime_matrix_inverse_alignment_overlap_slack_deletion_candidate_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def candidate_rows() -> list[dict[str, Any]]:
    """合并所需删除量与 overlap/slack 候选源。"""
    target = load_json(TARGET)
    budget = load_json(BUDGET_LEDGER)
    by_p = {int(item["P"]): item for item in budget.get("budget_rows", [])}
    rows: list[dict[str, Any]] = []
    for item in target.get("deletion_target_rows", []):
        p_value = int(item["P"])
        b = by_p[p_value]
        required = int(item["minimum_integer_deletion_for_strict_margin"])
        proxy = int(b["overlap_debt"]) + int(b["charged_slack_for_appeared_tau"])
        rows.append(
            {
                "P": p_value,
                "x": int(item["x"]),
                "z": int(item["z"]),
                "required_deletion": required,
                "overlap_debt": int(b["overlap_debt"]),
                "tau_charged_slack": int(b["charged_slack_for_appeared_tau"]),
                "overlap_plus_slack_proxy": proxy,
                "proxy_margin": proxy - required,
                "proxy_covers_required_deletion": proxy >= required,
            }
        )
    return rows


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "DeletionTargetImported",
            "closed": result["deletion_target_imported"],
            "proved": result["deletion_target_imported"],
            "meaning": "上一层已给出 exact-x 严格余量所需删除量。",
            "remaining": DELETION_LOWER,
        },
        {
            "gate": "OverlapSlackCandidateDominatesSamples",
            "closed": result["overlap_slack_candidate_dominates_samples"],
            "proved": False,
            "meaning": "样本中 overlap debt + tau slack 均覆盖所需删除量，但这还不是全局证明。",
            "remaining": OVERLAP_MAP,
        },
        {
            "gate": "RegisteredOverlapSlackDeletionMapProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需把 hit-level overlap/slack 无损注入 cold supply 删除单位。",
            "remaining": OVERLAP_MAP,
        },
        {
            "gate": "ColdRestrictionDeletionLowerBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "候选源足量的样本信号存在，但缺全局注册映射和无重复扣减纪律。",
            "remaining": f"{OVERLAP_MAP} AND {DELETION_LOWER}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "删除映射、持久 moving atom 与 DStructure/Rankin 仍未全部闭合。",
            "remaining": f"{OVERLAP_MAP} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造候选删除源证书。"""
    target = load_json(TARGET)
    rows = candidate_rows()
    target_imported = target.get("cold_restricted_exact_x_supply_deletion_ledger_closed") is True
    dominates = bool(rows) and all(item["proxy_covers_required_deletion"] for item in rows)
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_overlap_slack_deletion_candidate_router",
        "status": "overlap_slack_deletion_candidate_dominates_samples_registered_map_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "deletion_target_imported": target_imported,
        "overlap_slack_candidate_dominates_samples": dominates,
        "registered_overlap_slack_deletion_map_proved": False,
        "cold_restriction_deletion_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": DELETION_LOWER,
        "hardpoint_after_router": OVERLAP_MAP,
        "next_direct_attack_target": OVERLAP_MAP,
        "parallel_attack_targets": [MOVING_ATOM, DSTRUCTURE],
        "candidate_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Exact-x 删除目标表暴露出一个候选机制：样本中 `overlap_debt + tau charged_slack` "
            "全部大于等于严格余量所需删除量。这说明重叠债与 tau 桶松弛可能正是 cold-restricted "
            "删除量的来源。当前还不能宣布闭合，因为 overlap/slack 是命中层字段，必须证明它们能被"
            "无重复、保标签地注册为 cold supply 删除单位。下一最窄点是 "
            "`RegisteredOverlapSlackToColdSupplyDeletionMap`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix inverse alignment overlap/slack 删除候选路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"deletion_target_imported={fmt_bool(result['deletion_target_imported'])}",
        f"overlap_slack_candidate_dominates_samples={fmt_bool(result['overlap_slack_candidate_dominates_samples'])}",
        f"registered_overlap_slack_deletion_map_proved={fmt_bool(result['registered_overlap_slack_deletion_map_proved'])}",
        f"cold_restriction_deletion_lower_bound_proved={fmt_bool(result['cold_restriction_deletion_lower_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 候选源表",
        "",
        "| P | X(P) | z | required | overlap | tau slack | proxy | proxy margin |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["candidate_rows"]:
        lines.append(
            "| `{P}` | `{x}` | `{z}` | `{required}` | `{overlap}` | `{slack}` | `{proxy}` | `{margin}` |".format(
                P=item["P"],
                x=item["x"],
                z=item["z"],
                required=item["required_deletion"],
                overlap=item["overlap_debt"],
                slack=item["tau_charged_slack"],
                proxy=item["overlap_plus_slack_proxy"],
                margin=item["proxy_margin"],
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
            "- 任务：构造 overlap/slack 到 cold supply 删除单位的保标签注入，防止重复扣减。",
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
