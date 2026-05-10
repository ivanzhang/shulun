#!/usr/bin/env python3
"""用分支预算排除低预算相位，只留下中央根定位盒高重数。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_root_box_branch_budget_phase_exclusion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-root-box-branch-budget-phase-exclusion-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-root-box-branch-budget-phase-exclusion-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-root-box-branch-budget-phase-exclusion-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-root-localized-discriminant-corridor-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "RootLocalizedQuadraticGraphBoxFiberPowerSaving"
NEXT_ATOM = "CentralPhaseRootLocalizedGraphBoxFiberPowerSaving"
LOW_BUDGET_ATOM = "LowBranchBudgetPhaseHighSpectrumExclusion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造低分支预算排除证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    root_box_closed = previous.get("root_localized_difference_identity_closed") is True

    # 对相位 c 取有符号代表 gamma，并记 U=max J。
    # 从 ab-gamma(a+b)=kP 有
    #   |k| <= (U^2+2|gamma|U)/P + O(1)。
    # 固定 k 时 (a-gamma)(b-gamma)=gamma^2+kP，
    # 因而由除数界得到每相位 r_gamma <= branch_budget * P^o(1)。
    branch_budget_closed = active and root_box_closed
    low_budget_absorbed = active and root_box_closed
    central_necessary = active and root_box_closed

    branch_ledger = {
        "signed_phase": "gamma is the signed representative of c",
        "box_height": "U=max J with U<=P^(1/2)log^236(P)",
        "integer_lift": "ab-gamma(a+b)=kP",
        "branch_budget": "B(gamma)<=1+(U^2+2|gamma|U)/P",
        "per_branch_factorization": "(a-gamma)(b-gamma)=gamma^2+kP",
        "divisor_envelope": "r_gamma<=B(gamma)*P^o(1)",
        "high_threshold": "r_gamma>N^(1-eta) for some fixed eta>0",
        "necessary_central_condition": "|gamma| >= (P/U)*N^(1-eta-o(1)) unless the phase is already absorbed",
    }

    compression = {
        "absorbed_phases": "all phases with B(gamma)<=N^(1-eta-o(1))",
        "remaining_phases": "central signed phases whose branch budget itself is high enough to support a high fiber",
        "why_this_is_narrower": "the proof no longer has to handle every interior phase; only central phases with large lift-branch supply remain",
        "still_missing": "large branch supply does not by itself create many root-localized hits; it only keeps the counterexample alive",
        "next_direct_attack": NEXT_ATOM,
    }

    rows = [
        row(
            "RootLocalizedGraphBoxTargetActive",
            active,
            True,
            "上一证书已把剩余固定为根定位小差盒的有理相位映射高重数排斥。",
            TARGET,
        ),
        row(
            "BranchBudgetEnvelopeClosed",
            branch_budget_closed,
            True,
            "`ab-gamma(a+b)=kP` 给出 `B(gamma)<=1+(U^2+2|gamma|U)/P`。",
            LOW_BUDGET_ATOM,
        ),
        row(
            "PerBranchDivisorEnvelopeClosed",
            branch_budget_closed,
            True,
            "固定分支化为一条整数乘积方程，所以每分支由除数界控制。",
            LOW_BUDGET_ATOM,
        ),
        row(
            "LowBranchBudgetPhaseHighSpectrumExcluded",
            low_budget_absorbed,
            True,
            "若分支预算低于高谱阈值，则 `r_gamma<=B(gamma)P^o(1)` 直接排除高重数。",
            "absorbed",
        ),
        row(
            "HighFiberForcesCentralPhaseCondition",
            central_necessary,
            True,
            "任何幸存高纤维必须满足 `|gamma| >= (P/U)N^(1-eta-o(1))` 的中央相位必要条件。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "中央相位仍可能有足够分支预算；还需证明这些分支不能同步命中根定位小差盒。",
            "CentralBranchRootBoxIncidencePowerSaving",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只排除低分支预算相位，没有证明中央相位排斥。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_root_box_branch_budget_phase_exclusion_router",
        "status": "low_branch_budget_phases_absorbed_central_root_box_high_spectrum_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "root_localized_graph_box_target_active": active,
        "branch_budget_envelope_closed": branch_budget_closed,
        "per_branch_divisor_envelope_closed": branch_budget_closed,
        "low_branch_budget_phase_high_spectrum_excluded": low_budget_absorbed,
        "high_fiber_forces_central_phase_condition": central_necessary,
        "central_phase_root_localized_graph_box_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "branch_ledger": branch_ledger,
        "compression": compression,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "根定位小差盒继续被分支预算压缩。对有符号相位 `gamma`，"
            "`ab-gamma(a+b)=kP` 的分支数满足 `B(gamma)<=1+(U^2+2|gamma|U)/P`；"
            "固定分支再由除数界控制。因此低分支预算相位不能进入固定幂高谱。"
            "任何假设高纤维都被迫满足中央相位必要条件 "
            "`|gamma| >= (P/U)N^(1-eta-o(1))`，剩余只剩中央相位的大分支供给是否能同步命中根定位盒。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    branch = result["branch_ledger"]
    compression = result["compression"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 根定位盒分支预算排除证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"low_branch_budget_phase_high_spectrum_excluded={fmt_bool(result['low_branch_budget_phase_high_spectrum_excluded'])}",
        f"high_fiber_forces_central_phase_condition={fmt_bool(result['high_fiber_forces_central_phase_condition'])}",
        f"central_phase_root_localized_graph_box_power_saving_proved={fmt_bool(result['central_phase_root_localized_graph_box_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 分支预算",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in branch.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 压缩结果",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in compression.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 4. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
