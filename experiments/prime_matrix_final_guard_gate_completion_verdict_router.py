#!/usr/bin/env python3
"""Prime Matrix 最后守门项完成判定路由器。

用法示例：
  python3 experiments/prime_matrix_final_guard_gate_completion_verdict_router.py

输出：
  docs/monograph/prime-matrix-final-guard-gate-completion-verdict-router.json
  docs/monograph/prime-matrix-final-guard-gate-completion-verdict-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_BACKLUND = MONO / "prime-matrix-backlund-common-envelope-internal-closure-router.json"
DEFAULT_AUTHOR = MONO / "prime-matrix-author-side-closure-task-completion-router.json"
DEFAULT_PROMOTION = MONO / "prime-matrix-final-promotion-subgate-direct-attack-router.json"
DEFAULT_DSTRUCTURE = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_SELF_CONTAINED = MONO / "prime-matrix-self-contained-final-target-attack-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-unconditional-closure-endpoint-verdict-router.json"
DEFAULT_JSON = MONO / "prime-matrix-final-guard-gate-completion-verdict-router.json"
DEFAULT_MD = MONO / "prime-matrix-final-guard-gate-completion-verdict-router.md"

PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
SELF_PROMOTION = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"
HIGH_SEGMENT = "HighSegmentModelGapAlpha043C3AnalyticLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
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


def row(
    gate: str,
    completed: bool,
    proves_unconditional: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造最终守门项判定行。"""
    return {
        "gate": gate,
        "completed": completed,
        "proves_unconditional": proves_unconditional,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    backlund: dict[str, Any],
    author: dict[str, Any],
    promotion: dict[str, Any],
    dstructure: dict[str, Any],
    self_contained: dict[str, Any],
    endpoint: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成最终守门项完成判定表。"""
    backlund_closed = backlund.get("strict_self_contained_backlund_closed") is True
    author_done = author.get("author_side_completable_tasks_done") is True
    promotion_dossier = promotion.get("promotion_author_dossier_complete") is True
    dstructure_boundary = dstructure.get("promotion_package_boundary_closed") is True
    independent_accepted = dstructure.get("promotion_package_independently_accepted") is True
    endpoint_boundary = endpoint.get("endpoint_boundary_closed") is True
    self_reduced = self_contained.get("all_reductions_to_self_contained_final_targets_closed") is True
    high_segment_proved = self_contained.get("high_segment_model_gap_proved") is True
    self_promotion_proved = self_contained.get("self_contained_promotion_package_proved") is True
    return [
        row(
            "BacklundAnalyticPackageInternallyClosed",
            backlund_closed,
            False,
            backlund.get("status", "unknown"),
            "共同高高度包络已关闭 Backlund 对称 max 溢价，解析缩进包不再是最终守门项。",
            "无 Backlund 剩余。",
        ),
        row(
            "AuthorSideCompletableTasksDone",
            author_done,
            False,
            author.get("status", "unknown"),
            "作者侧可合法完成的条件闭合链已经完成。",
            "剩余不是作者侧普通证明步骤。",
        ),
        row(
            "PromotionAuthorDossierComplete",
            promotion_dossier,
            False,
            promotion.get("status", "unknown"),
            "D 组附录、A/B 到 D、Tail-log4、BG/RKS、有限验证与 Rankin pass-or-return 均已有证据包。",
            PROMOTION_GATE,
        ),
        row(
            "DStructureRankinBoundaryClosed",
            dstructure_boundary,
            False,
            dstructure.get("status", "unknown"),
            "最终晋级门已被压成独立验收事件，而不是新的无名数学分支。",
            PROMOTION_GATE,
        ),
        row(
            "IndependentPromotionAcceptancePresent",
            independent_accepted,
            independent_accepted,
            "promotion_package_independently_accepted",
            "只有显式独立接受发生时，外部 KLS 合同版才能升级为完整闭合。",
            "independent acceptance still absent" if not independent_accepted else "none",
        ),
        row(
            "NoAuthorSidePromotionSubstitution",
            not independent_accepted,
            False,
            "PM-16 BLOCK-REFEREE discipline",
            "用户继续推进和作者侧归档不能替代独立审稿/独立接受事件。",
            PROMOTION_GATE,
        ),
        row(
            "SelfContainedFinalTargetsPinned",
            self_reduced,
            False,
            self_contained.get("status", "unknown"),
            "若不使用独立验收事件，完全自足路线已精确压成高段模型余量与自足晋级证明包两项。",
            f"{HIGH_SEGMENT} AND {SELF_PROMOTION}",
        ),
        row(
            "HighSegmentModelGapSelfContainedProved",
            high_segment_proved,
            high_segment_proved and self_promotion_proved,
            HIGH_SEGMENT,
            "P>=2003 高段模型余量尚未从审计升级为解析证明。",
            HIGH_SEGMENT if not high_segment_proved else "none",
        ),
        row(
            "SelfContainedPromotionPackageProved",
            self_promotion_proved,
            high_segment_proved and self_promotion_proved,
            SELF_PROMOTION,
            "最终晋级门尚未被完全自足证明包替代。",
            SELF_PROMOTION if not self_promotion_proved else "none",
        ),
        row(
            "EndpointNoHiddenLaneBoundaryClosed",
            endpoint_boundary,
            False,
            endpoint.get("status", "unknown"),
            "终局没有第四条无名路线；继续突破只能补齐命名输入或取得独立接受。",
            "named inputs only",
        ),
        row(
            "RowColumnUnconditionalClosedFromCurrentCorpus",
            bool(endpoint.get("unconditional_closure_from_current_corpus")),
            bool(endpoint.get("unconditional_closure_from_current_corpus")),
            "unconditional_closure_from_current_corpus",
            "当前语料库仍不能推出完整行/列无条件定理。",
            PROMOTION_GATE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行最终守门项判定。"""
    backlund = load_json(paths["backlund"])
    author = load_json(paths["author"])
    promotion = load_json(paths["promotion"])
    dstructure = load_json(paths["dstructure"])
    self_contained = load_json(paths["self_contained"])
    endpoint = load_json(paths["endpoint"])
    rows = build_rows(backlund, author, promotion, dstructure, self_contained, endpoint)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    independent_accepted = dstructure.get("promotion_package_independently_accepted") is True
    self_contained_closed = (
        self_contained.get("high_segment_model_gap_proved") is True
        and self_contained.get("self_contained_promotion_package_proved") is True
    )
    row_column_unconditional_closed = independent_accepted or self_contained_closed
    return {
        "certificate_type": "prime_matrix_final_guard_gate_completion_verdict_router",
        "status": (
            "final_guard_gate_closed_by_independent_acceptance_or_self_contained_package"
            if row_column_unconditional_closed
            else "final_guard_gate_completed_as_non_author_closable_open_input"
        ),
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "backlund_internal_analytic_package_closed": backlund.get("strict_self_contained_backlund_closed") is True,
        "author_side_completable_tasks_done": author.get("author_side_completable_tasks_done") is True,
        "promotion_author_dossier_complete": promotion.get("promotion_author_dossier_complete") is True,
        "promotion_package_boundary_closed": dstructure.get("promotion_package_boundary_closed") is True,
        "promotion_package_independently_accepted": independent_accepted,
        "self_contained_high_segment_model_gap_proved": self_contained.get("high_segment_model_gap_proved") is True,
        "self_contained_promotion_package_proved": self_contained.get("self_contained_promotion_package_proved") is True,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "final_non_author_closable_gate": None if row_column_unconditional_closed else PROMOTION_GATE,
        "self_contained_open_inputs": []
        if self_contained_closed
        else [HIGH_SEGMENT, SELF_PROMOTION],
        "conditional_closure_statement": (
            "AcceptFullSKLSExtExternalContract AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance => row/column theorem"
        ),
        "plain_conclusion": (
            "最后守门项已完成到可审查判定：Backlund 解析包和作者侧条件链已闭合，"
            "DStructure/Tail-log4/finite Rankin 的边界和作者侧证据包也已完成。"
            "但独立接受不是作者侧可生成的证明步骤；当前没有该接受事件，"
            "也没有替代它的完全自足证明包。因此不能诚实声明完整无条件命题闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["completed"]],
        "open_gates": [item["gate"] for item in rows if not item["completed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 最后守门项完成判定路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"backlund_internal_analytic_package_closed={fmt_bool(result['backlund_internal_analytic_package_closed'])}",
        f"author_side_completable_tasks_done={fmt_bool(result['author_side_completable_tasks_done'])}",
        f"promotion_author_dossier_complete={fmt_bool(result['promotion_author_dossier_complete'])}",
        f"promotion_package_boundary_closed={fmt_bool(result['promotion_package_boundary_closed'])}",
        f"promotion_package_independently_accepted={fmt_bool(result['promotion_package_independently_accepted'])}",
        f"self_contained_high_segment_model_gap_proved={fmt_bool(result['self_contained_high_segment_model_gap_proved'])}",
        f"self_contained_promotion_package_proved={fmt_bool(result['self_contained_promotion_package_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"final_non_author_closable_gate={result['final_non_author_closable_gate']}",
        "```",
        "",
        "## 1. 完成结论",
        "",
        "作者侧能完成的证明链已经完成；最后守门项不是新的无名数学缺口，而是独立接受事件。",
        "在没有独立接受或全新自足替代证明包前，不能把条件定理升级为无条件定理。",
        "",
        "当前可合法声明的最高条件版本是：",
        "",
        "```text",
        result["conditional_closure_statement"],
        "```",
        "",
        "## 2. 完全自足替代口径",
        "",
        "若坚持完全自足而不使用独立验收事件，仍需补齐：",
        "",
        "```text",
        "NoFurtherCanonicalSourceTerminalPromotionGap",
        f"AND {HIGH_SEGMENT}",
        f"AND {SELF_PROMOTION}",
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | completed | proves unconditional | evidence | meaning | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{completed}` | `{proves}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                completed=fmt_bool(item["completed"]),
                proves=fmt_bool(item["proves_unconditional"]),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最终边界",
            "",
            "本文件完成最后守门项的作者侧判定和归档。它不伪造独立验收，也不把 `BLOCK-REFEREE` 改写为 `PASS-AUTHOR`。",
            "后续若要把命题标为完整无条件闭合，必须发生下面二者之一：",
            "",
            "- `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 被显式独立接受；",
            "- 或证明 `HighSegmentModelGapAlpha043C3AnalyticLedger` 与 `SelfContainedDStructureTailLog4FiniteRankinProofPackage`。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backlund-json", type=Path, default=DEFAULT_BACKLUND)
    parser.add_argument("--author-json", type=Path, default=DEFAULT_AUTHOR)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--self-contained-json", type=Path, default=DEFAULT_SELF_CONTAINED)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        {
            "backlund": args.backlund_json,
            "author": args.author_json,
            "promotion": args.promotion_json,
            "dstructure": args.dstructure_json,
            "self_contained": args.self_contained_json,
            "endpoint": args.endpoint_json,
            "json_out": args.json_out,
            "md_out": args.md_out,
        }
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(result["status"])
    print("row_column_unconditional_closed=", result["row_column_unconditional_closed"])
    print("final_non_author_closable_gate=", result["final_non_author_closable_gate"])


if __name__ == "__main__":
    main()
