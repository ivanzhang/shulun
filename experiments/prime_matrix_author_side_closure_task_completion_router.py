#!/usr/bin/env python3
"""作者侧闭合任务完成状态总账路由器。

用法示例：
  python3 experiments/prime_matrix_author_side_closure_task_completion_router.py
  python3 experiments/prime_matrix_author_side_closure_task_completion_router.py --accept-referee-gate

输出：
  docs/monograph/prime-matrix-author-side-closure-task-completion-router.json
  docs/monograph/prime-matrix-author-side-closure-task-completion-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_LOGIC = MONO / "prime-matrix-final-proof-logic-chain-status-router.json"
DEFAULT_IRREDUCIBLE = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
DEFAULT_SINGLE_GATE = MONO / "prime-matrix-final-single-gate-closure-decision-router.json"
DEFAULT_SUBGATE = MONO / "prime-matrix-final-promotion-subgate-direct-attack-router.json"
DEFAULT_LINE_REF = MONO / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = MONO / "prime-matrix-author-side-closure-task-completion-router.json"
DEFAULT_MD = MONO / "prime-matrix-author-side-closure-task-completion-router.md"

EXTERNAL_KLS = "AcceptFullSKLSExtExternalContract"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本证据。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """格式化布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def task(
    name: str,
    required_for: str,
    author_completed: bool,
    theorem_promotion_completed: bool,
    author_can_complete: bool,
    status: str,
    evidence: str,
    final_action: str,
) -> dict[str, Any]:
    """构造作者侧任务行。"""
    return {
        "name": name,
        "required_for": required_for,
        "author_completed": author_completed,
        "theorem_promotion_completed": theorem_promotion_completed,
        "author_can_complete": author_can_complete,
        "status": status,
        "evidence": evidence,
        "final_action": final_action,
    }


def step_status(logic: dict[str, Any], name: str) -> bool:
    """按名称读取最终证明链步骤状态。"""
    for item in logic.get("actual_proof_chain", []):
        if item.get("name") == name:
            return item.get("proved_or_accepted") is True
    return False


def subgate_author_complete(subgate: dict[str, Any]) -> bool:
    """确认晋级门作者侧子包全完成。"""
    rows = subgate.get("rows", [])
    return bool(rows) and all(item.get("author_closed") is True for item in rows)


def build_tasks(
    logic: dict[str, Any],
    irreducible: dict[str, Any],
    single_gate: dict[str, Any],
    subgate: dict[str, Any],
    line_ref_text: str,
    accept_referee_gate: bool,
) -> list[dict[str, Any]]:
    """整理全部剩余目标任务与完成状态。"""
    referee_accepted = bool(
        accept_referee_gate
        and irreducible.get("promotion_author_packet_sealed") is True
        and irreducible.get("irreducible_gate") == PROMOTION_GATE
    )
    no_author_promotion = (
        step_status(logic, "NoAuthorSidePromotion")
        and "本轮没有把任何 `BLOCK-REFEREE` 改写为 `PASS-AUTHOR`" in line_ref_text
    )

    return [
        task(
            name="反例链纪律",
            required_for="条件闭合与自足闭合共同前提",
            author_completed=step_status(logic, "CounterexampleChainDiscipline"),
            theorem_promotion_completed=step_status(logic, "CounterexampleChainDiscipline"),
            author_can_complete=True,
            status="completed",
            evidence="final proof logic chain step 1",
            final_action="保持只在假设反例链条内推理，不用真实样本缺席。",
        ),
        task(
            name="无隐藏终端图谱",
            required_for="条件闭合与自足闭合共同前提",
            author_completed=step_status(logic, "NoHiddenTerminalEscape"),
            theorem_promotion_completed=step_status(logic, "NoHiddenTerminalEscape"),
            author_can_complete=True,
            status="completed",
            evidence="closure atlas + endpoint boundary",
            final_action="不再回到无名分支，只攻命名输入。",
        ),
        task(
            name="外部 FullS-KLS 数学线",
            required_for="外部合同版闭合",
            author_completed=step_status(logic, "ExternalFullSKLSMathLaneClosure"),
            theorem_promotion_completed=step_status(logic, "ExternalFullSKLSMathLaneClosure"),
            author_can_complete=True,
            status="completed_as_external_contract",
            evidence=EXTERNAL_KLS,
            final_action="若接受外部合同，本线已闭合；若要求完全自足，则必须另证 full-S 定理。",
        ),
        task(
            name="完全自足 full-S 替代证明",
            required_for="完全自足无黑箱闭合",
            author_completed=False,
            theorem_promotion_completed=False,
            author_can_complete=True,
            status="optional_open_for_self_contained_version",
            evidence="endpoint verdict: NewFullSTheoremInput or NewFullSNonAPSourceAntiAtomTheoremInput",
            final_action="不属于外部 KLS 合同版剩余；若坚持自足版，需新增深定理证明替代外部 KLS。",
        ),
        task(
            name="DStructure/Tail-log4/finite Rankin 作者侧证据包",
            required_for="最终晋级门验收",
            author_completed=(
                irreducible.get("promotion_author_packet_sealed") is True
                and single_gate.get("promotion_author_dossier_complete") is True
                and subgate_author_complete(subgate)
            ),
            theorem_promotion_completed=False,
            author_can_complete=True,
            status="author_packet_sealed_referee_acceptance_open",
            evidence="final promotion subgate + irreducibility router",
            final_action="作者侧已完成可审查证据包；仍需独立接受才可晋级定理。",
        ),
        task(
            name="不偷换纪律",
            required_for="防止条件闭合误报为无条件闭合",
            author_completed=no_author_promotion,
            theorem_promotion_completed=no_author_promotion,
            author_can_complete=True,
            status="completed",
            evidence="line-by-line internal referee matrix",
            final_action="保持 PM-16 为 BLOCK-REFEREE，除非独立接受真实发生。",
        ),
        task(
            name="条件行/列定理",
            required_for="当前可合法声明的最高版本",
            author_completed=step_status(logic, "ConditionalRowColumnTheorem"),
            theorem_promotion_completed=step_status(logic, "ConditionalRowColumnTheorem"),
            author_can_complete=True,
            status="completed_conditional_theorem",
            evidence=f"{EXTERNAL_KLS} AND {PROMOTION_GATE}",
            final_action="可声明条件定理；不能删去条件。",
        ),
        task(
            name="最终独立晋级门接受",
            required_for="外部 KLS 合同版无条件闭合",
            author_completed=False,
            theorem_promotion_completed=referee_accepted,
            author_can_complete=False,
            status="not_author_completable_referee_event_open",
            evidence=PROMOTION_GATE if not referee_accepted else "--accept-referee-gate",
            final_action="只能由显式独立接受关闭，或由全新自足证明包替换该门。",
        ),
        task(
            name="作者侧完全自足替代晋级证明",
            required_for="不依赖独立验收事件的自足闭合",
            author_completed=False,
            theorem_promotion_completed=False,
            author_can_complete=True,
            status="open_new_proof_package_required",
            evidence="irreducibility router legal next move: replace the gate by a new fully self-contained proof package",
            final_action="需把 DStructure/AB、Tail-log4/BG-RKS、finite verification、Rankin 全部升级为无需外审门的自足定理包。",
        ),
        task(
            name="最终无条件命题晋级",
            required_for="完整行/列命题无条件闭合",
            author_completed=False,
            theorem_promotion_completed=referee_accepted,
            author_can_complete=False,
            status="blocked_by_final_independent_gate",
            evidence="final proof logic chain step 7",
            final_action="在独立晋级门未接受或未被新自足证明替换前，必须保持 false。",
        ),
    ]


def run(paths: dict[str, Path], accept_referee_gate: bool) -> dict[str, Any]:
    """运行作者侧闭合任务总账。"""
    logic = load_json(paths["logic"])
    irreducible = load_json(paths["irreducible"])
    single_gate = load_json(paths["single_gate"])
    subgate = load_json(paths["subgate"])
    line_ref_text = read_text(paths["line_ref"])
    tasks = build_tasks(
        logic=logic,
        irreducible=irreducible,
        single_gate=single_gate,
        subgate=subgate,
        line_ref_text=line_ref_text,
        accept_referee_gate=accept_referee_gate,
    )
    author_side_completable_tasks_done = all(
        item["author_completed"] for item in tasks if item["author_can_complete"]
        and not item["name"].startswith("完全自足")
        and not item["name"].startswith("作者侧完全自足")
    )
    conditional_theorem_completed = any(
        item["name"] == "条件行/列定理" and item["author_completed"] for item in tasks
    )
    final_referee_gate_open = any(
        item["name"] == "最终独立晋级门接受"
        and not item["theorem_promotion_completed"]
        for item in tasks
    )
    self_contained_open = any(
        item["name"] in {"完全自足 full-S 替代证明", "作者侧完全自足替代晋级证明"}
        and not item["author_completed"]
        for item in tasks
    )
    row_column_closed = conditional_theorem_completed and not final_referee_gate_open

    return {
        "certificate_type": "prime_matrix_author_side_closure_task_completion_router",
        "status": (
            "author_side_conditional_chain_complete_final_referee_gate_open"
            if final_referee_gate_open
            else "author_side_plus_referee_gate_row_column_closed"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        },
        "author_side_completable_tasks_done": author_side_completable_tasks_done,
        "conditional_external_kls_theorem_completed": conditional_theorem_completed,
        "final_referee_gate_open": final_referee_gate_open,
        "self_contained_replacement_tasks_open": self_contained_open,
        "row_column_unconditional_closed": row_column_closed,
        "highest_valid_author_side_claim": (
            f"{EXTERNAL_KLS} AND {PROMOTION_GATE} => row/column theorem"
        ),
        "non_author_remaining_obligation": (
            PROMOTION_GATE if final_referee_gate_open else None
        ),
        "remaining_author_side_targets_not_fully_completed": [
            item for item in tasks if item["author_can_complete"] and not item["author_completed"]
        ],
        "remaining_non_author_targets": [
            item for item in tasks if not item["author_can_complete"] and not item["theorem_promotion_completed"]
        ],
        "tasks": tasks,
        "plain_conclusion": (
            "作者侧可合法完成的条件闭合链已经完成；仍未完成的是最终独立晋级门接受，"
            "它不是作者侧可生成的证明步骤。若坚持完全自足，还另需新增 full-S 替代证明"
            "和自足替代晋级证明包。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 作者侧闭合任务完成状态总账",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"author_side_completable_tasks_done={fmt_bool(result['author_side_completable_tasks_done'])}",
        f"conditional_external_kls_theorem_completed={fmt_bool(result['conditional_external_kls_theorem_completed'])}",
        f"final_referee_gate_open={fmt_bool(result['final_referee_gate_open'])}",
        f"self_contained_replacement_tasks_open={fmt_bool(result['self_contained_replacement_tasks_open'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 作者侧最高可声明版本",
        "",
        "```text",
        result["highest_valid_author_side_claim"],
        "```",
        "",
        "## 2. 任务总账",
        "",
        "| task | required for | author completed | theorem promotion completed | author can complete | status | final action |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["tasks"]:
        lines.append(
            "| {name} | {required} | `{author}` | `{theorem}` | `{can}` | `{status}` | {action} |".format(
                name=table_cell(item["name"]),
                required=table_cell(item["required_for"]),
                author=fmt_bool(item["author_completed"]),
                theorem=fmt_bool(item["theorem_promotion_completed"]),
                can=fmt_bool(item["author_can_complete"]),
                status=table_cell(item["status"]),
                action=table_cell(item["final_action"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 未充分完成项",
            "",
        ]
    )
    author_open = result["remaining_author_side_targets_not_fully_completed"]
    non_author_open = result["remaining_non_author_targets"]
    if author_open:
        lines.append("### 作者侧若坚持完全自足仍需新增证明")
        lines.append("")
        for item in author_open:
            lines.append(f"- `{item['name']}`：{item['final_action']}")
        lines.append("")
    else:
        lines.append("作者侧在外部 KLS 合同路线内可完成的任务已经全部完成。")
        lines.append("")
    if non_author_open:
        lines.append("### 非作者侧可生成的剩余义务")
        lines.append("")
        for item in non_author_open:
            lines.append(f"- `{item['name']}`：{item['final_action']}")
        lines.append("")
    lines.extend(
        [
            "## 4. 最终完成状态",
            "",
            (
                "在不伪造独立验收的前提下，作者侧已经完整完成条件证明逻辑链。"
                "完整无条件命题闭合仍为 `false`，因为最后独立晋级门未被接受；"
                "完全自足版也仍为 `false`，因为需要新增替代外部 KLS 与替代晋级门的证明包。"
            ),
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--logic-json", type=Path, default=DEFAULT_LOGIC)
    parser.add_argument("--irreducible-json", type=Path, default=DEFAULT_IRREDUCIBLE)
    parser.add_argument("--single-gate-json", type=Path, default=DEFAULT_SINGLE_GATE)
    parser.add_argument("--subgate-json", type=Path, default=DEFAULT_SUBGATE)
    parser.add_argument("--line-ref", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--accept-referee-gate", action="store_true")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "logic": args.logic_json,
        "irreducible": args.irreducible_json,
        "single_gate": args.single_gate_json,
        "subgate": args.subgate_json,
        "line_ref": args.line_ref,
    }
    result = run(paths, args.accept_referee_gate)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["plain_conclusion"])


if __name__ == "__main__":
    main()
