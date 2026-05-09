#!/usr/bin/env python3
"""Prime Matrix 按序推进剩余任务路由器。

用法示例：
  python3 experiments/prime_matrix_ordered_remaining_task_execution_router.py

输出：
  docs/monograph/prime-matrix-ordered-remaining-task-execution-router.json
  docs/monograph/prime-matrix-ordered-remaining-task-execution-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

SIGNED_DELAY = DOCS / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json"
MERTENS_TAIL = DOCS / "prime-matrix-b3-self-contained-mertens-tail-router.json"
FINAL_GATE = DOCS / "prime-matrix-final-guard-gate-completion-verdict-router.json"

DEFAULT_JSON = DOCS / "prime-matrix-ordered-remaining-task-execution-router.json"
DEFAULT_MD = DOCS / "prime-matrix-ordered-remaining-task-execution-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
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


def task(
    order: int,
    name: str,
    status: str,
    completed: bool,
    proves_unconditional: bool,
    evidence: str,
    next_action: str,
) -> dict[str, Any]:
    """构造顺序任务行。"""
    return {
        "order": order,
        "name": name,
        "status": status,
        "completed": completed,
        "proves_unconditional": proves_unconditional,
        "evidence": evidence,
        "next_action": next_action,
    }


def build_tasks(
    signed_delay: dict[str, Any],
    mertens_tail: dict[str, Any],
    final_gate: dict[str, Any],
) -> list[dict[str, Any]]:
    """按当前推荐顺序列出剩余任务。"""
    boundary_closed = bool(
        signed_delay.get("b3_boundary_variation_one_percent_conditional_closed")
    )
    self_tail_open = not bool(mertens_tail.get("self_contained_mertens_tail_proved"))
    final_gate_open = not bool(final_gate.get("promotion_package_independently_accepted"))

    return [
        task(
            1,
            "B3BoundaryVariationOnePercentTransferLedger",
            "conditional_external_mertens_route_closed",
            boundary_closed,
            False,
            "B3Anchor20000BoundaryVariationBudgetClosedAlpha043",
            "严格自足版继续进入 SelfContainedDusartReciprocalPrimeProofAppendixXGe10372。",
        ),
        task(
            2,
            "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372",
            "reduced_to_explicit_pnt_package_open",
            not self_tail_open,
            False,
            "prime-matrix-b3-self-contained-mertens-tail-router",
            "先证明 SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000，再补 SelfContainedMeisselMertensConstantIntervalLedgerAt20000。",
        ),
        task(
            3,
            "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000",
            "open",
            False,
            False,
            "zero-free theta envelope route",
            "按子顺序推进 SelfContainedDeLaValleePoussinZeroFreeRegionConstantsLedger、ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion、FiniteThetaEnvelopeBridgeBelowAnalyticThreshold。",
        ),
        task(
            4,
            "SelfContainedMeisselMertensConstantIntervalLedgerAt20000",
            "open",
            False,
            False,
            "self-contained Mertens tail route",
            "给出 B1 常数区间和 x=20000 基点核验，接回 reciprocal-prime Mertens 尾段。",
        ),
        task(
            5,
            "SelfContainedDStructureTailLog4FiniteRankinProofPackage",
            "open_or_referee_gate",
            not final_gate_open,
            False,
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            "若走外部合同版，需独立接受；若走作者自足版，需替换该独立验收门。",
        ),
        task(
            6,
            "RowColumnUnconditionalPromotion",
            "blocked_by_named_inputs",
            False,
            False,
            "row_column_unconditional_closed=false",
            "只有前述自足包全部证明，或外部合同与最终晋级门均被接受后，才能改为 true。",
        ),
    ]


def run() -> dict[str, Any]:
    """执行顺序推进状态汇总。"""
    signed_delay = load_json(SIGNED_DELAY)
    mertens_tail = load_json(MERTENS_TAIL)
    final_gate = load_json(FINAL_GATE)
    tasks = build_tasks(signed_delay, mertens_tail, final_gate)
    boundary_done = tasks[0]["completed"]
    open_tasks = [item["name"] for item in tasks if not item["completed"]]
    result = {
        "certificate_type": "prime_matrix_ordered_remaining_task_execution_router",
        "status": "first_order_task_closed_next_self_contained_pnt_package_open",
        "counterexample_assumption_only": bool(
            signed_delay.get("counterexample_assumption_only")
        )
        and bool(mertens_tail.get("counterexample_assumption_only")),
        "empirical_absence_not_used": bool(signed_delay.get("empirical_absence_not_used"))
        and bool(mertens_tail.get("empirical_absence_not_used")),
        "first_order_b3_boundary_variation_completed": boundary_done,
        "external_mertens_route_closed": bool(mertens_tail.get("external_mertens_route_closed")),
        "self_contained_mertens_tail_proved": bool(
            mertens_tail.get("self_contained_mertens_tail_proved")
        ),
        "promotion_package_independently_accepted": bool(
            final_gate.get("promotion_package_independently_accepted")
        ),
        "row_column_unconditional_closed": False,
        "next_priority": mertens_tail.get("next_priority"),
        "secondary_priority": mertens_tail.get("secondary_priority"),
        "latest_self_contained_basis": mertens_tail.get("latest_self_contained_basis"),
        "latest_conditional_basis": mertens_tail.get("latest_conditional_basis"),
        "open_tasks_in_order": open_tasks,
        "tasks": tasks,
        "evidence_hashes": {
            str(SIGNED_DELAY.relative_to(ROOT)): file_sha256(SIGNED_DELAY),
            str(MERTENS_TAIL.relative_to(ROOT)): file_sha256(MERTENS_TAIL),
            str(FINAL_GATE.relative_to(ROOT)): file_sha256(FINAL_GATE),
        },
        "plain_conclusion": (
            "第一顺位 B3 边界变差已在外部 Mertens 路线下由 20000 锚点预算关闭；"
            "严格自足路线没有完成无条件闭合，下一步必须内联 reciprocal-prime Mertens "
            "尾段所需的显式 PNT 包，然后再处理最终 DStructure/Rankin 晋级包。"
        ),
    }
    return result


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写出 Markdown 报告。"""
    lines: list[str] = []
    lines.append("# Prime Matrix 按序推进剩余任务路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "first_order_b3_boundary_variation_completed",
        "external_mertens_route_closed",
        "self_contained_mertens_tail_proved",
        "promotion_package_independently_accepted",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append(f"next_priority={result['next_priority']}")
    lines.append(f"secondary_priority={result['secondary_priority']}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 本轮完成")
    lines.append("")
    lines.append(
        "`B3BoundaryVariationOnePercentTransferLedger` 的外部 Mertens 路线已经由 "
        "`B3Anchor20000BoundaryVariationBudgetClosedAlpha043` 关闭。旧的 "
        "`<2.865` 乘子硬证不再是必要路线；20000 锚点给出足够预算余量。"
    )
    lines.append("")
    lines.append("这不等于完整行/列无条件闭合，因为完全自足 Mertens 尾段和最终晋级门仍未关闭。")
    lines.append("")
    lines.append("## 2. 顺序任务表")
    lines.append("")
    lines.append(
        "| order | task | status | completed | proves unconditional | next action |"
    )
    lines.append("| ---: | --- | --- | --- | --- | --- |")
    for item in result["tasks"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["order"]),
                    f"`{table_cell(item['name'])}`",
                    table_cell(item["status"]),
                    fmt_bool(item["completed"]),
                    fmt_bool(item["proves_unconditional"]),
                    table_cell(item["next_action"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## 3. 当前最窄下一步")
    lines.append("")
    lines.append(f"```text\n{result['next_priority']}\n```")
    lines.append("")
    lines.append("具体顺序：")
    lines.append("")
    lines.append("1. `SelfContainedDeLaValleePoussinZeroFreeRegionConstantsLedger`")
    lines.append("2. `ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion`")
    lines.append("3. `FiniteThetaEnvelopeBridgeBelowAnalyticThreshold`")
    lines.append("4. `SelfContainedMeisselMertensConstantIntervalLedgerAt20000`")
    lines.append("5. `SelfContainedDStructureTailLog4FiniteRankinProofPackage` 或独立接受对应晋级门")
    lines.append("")
    lines.append("## 4. 最新输入基")
    lines.append("")
    lines.append("严格自足输入基：")
    lines.append("")
    lines.append("```text")
    lines.append(result["latest_self_contained_basis"])
    lines.append("```")
    lines.append("")
    lines.append("外部 Mertens 条件输入基：")
    lines.append("")
    lines.append("```text")
    lines.append(result["latest_conditional_basis"])
    lines.append("```")
    lines.append("")
    lines.append("## 5. 证据哈希")
    lines.append("")
    for evidence, digest in result["evidence_hashes"].items():
        lines.append(f"- `{evidence}`: `{digest}`")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    result = run()
    DEFAULT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, DEFAULT_MD)
    print(result["status"])
    print(result["next_priority"])


if __name__ == "__main__":
    main()
