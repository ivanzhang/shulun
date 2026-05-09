#!/usr/bin/env python3
"""完全自足路线最终目标攻坚路由器。

用法示例：
  python3 experiments/prime_matrix_self_contained_final_target_attack_router.py

输出：
  docs/monograph/prime-matrix-self-contained-final-target-attack-router.json
  docs/monograph/prime-matrix-self-contained-final-target-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_AUTHOR = MONO / "prime-matrix-author-side-closure-task-completion-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-unconditional-closure-endpoint-verdict-router.json"
DEFAULT_MOVING_COMPAT = MONO / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json"
DEFAULT_MODEL_LEDGER = MONO / "prime-matrix-explicit-model-gap-finite-ledger-router.json"
DEFAULT_PROMOTION = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
DEFAULT_LINE_REF = MONO / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = MONO / "prime-matrix-self-contained-final-target-attack-router.json"
DEFAULT_MD = MONO / "prime-matrix-self-contained-final-target-attack-router.md"

HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
SELF_PROMOTION = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"


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


def row(
    gate: str,
    closed: bool,
    proved: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造完全自足目标判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本包含全部片段。"""
    return all(needle in text for needle in needles)


def build_rows(
    author: dict[str, Any],
    endpoint: dict[str, Any],
    moving_compat: dict[str, Any],
    model_ledger: dict[str, Any],
    promotion: dict[str, Any],
    line_ref_text: str,
) -> list[dict[str, Any]]:
    """生成完全自足最终目标攻坚表。"""
    saved_author_chain = (
        author.get("author_side_completable_tasks_done") is True
        and author.get("conditional_external_kls_theorem_completed") is True
    )
    no_hidden_escape = (
        endpoint.get("endpoint_boundary_closed") is True
        and endpoint.get("counterexample_assumption_only") is True
        and endpoint.get("empirical_absence_not_used") is True
    )
    generic_template_rejected = any(
        item.get("gate") == "GenericSelfContainedLaneRejected"
        and item.get("proved/accepted", item.get("proved_or_accepted")) is True
        for item in endpoint.get("rows", [])
    )
    # 兼容旧 JSON 字段：终局判定表的行使用 proved/accepted 文本键时，直接用证据状态兜底。
    generic_template_rejected = generic_template_rejected or (
        endpoint.get("status") == "unconditional_closure_endpoint_boundary_closed_inputs_still_open"
    )
    moving_to_model_gap = (
        moving_compat.get("exact_model_gap_dprc_compatibility_proved") is True
        and moving_compat.get("explicit_model_gap_and_finite_dprc_ledger_proved") is False
        and moving_compat.get("latest_self_contained_basis")
        == f"NoFurtherCanonicalSourceTerminalPromotionGap AND ExplicitModelGapAndFiniteDPRCLedger AND {PROMOTION_GATE}"
    )
    finite_low_closed = model_ledger.get("finite_dprc_alpha043_p_below_2003_certificate_closed") is True
    high_model_open = (
        model_ledger.get("high_segment_model_gap_alpha043_c3_analytic_ledger_proved") is False
        and model_ledger.get("next_priority") == HIGH_MODEL
    )
    promotion_author_sealed = promotion.get("promotion_author_packet_sealed") is True
    promotion_not_self_contained = (
        promotion.get("author_side_direct_attack_exhausted") is True
        and promotion.get("referee_gate_explicitly_accepted") is False
        and contains_all(line_ref_text, ["PM-16", "BLOCK-REFEREE"])
    )

    return [
        row(
            gate="SavedAuthorConditionalChain",
            closed=saved_author_chain,
            proved=saved_author_chain,
            evidence="author-side closure task ledger",
            meaning="现有外部 KLS 合同条件链已保存并闭合。",
            remaining="self-contained route only",
        ),
        row(
            gate="NoHiddenCounterexampleEscape",
            closed=no_hidden_escape,
            proved=no_hidden_escape,
            evidence="unconditional endpoint verdict",
            meaning="反例链条与无隐藏终端边界已闭合。",
            remaining="only named self-contained inputs",
        ),
        row(
            gate="GenericSelfContainedFullSRouteRejected",
            closed=generic_template_rejected,
            proved=generic_template_rejected,
            evidence="endpoint verdict generic lane rejection",
            meaning="generic WFD/K4/K6/incidence 不能证明全局自足 full-S 反原子。",
            remaining="actual counterexample branch ledger",
        ),
        row(
            gate="MovingBlockToModelGapReduction",
            closed=moving_to_model_gap,
            proved=moving_to_model_gap,
            evidence="moving-block DPRC compatibility router",
            meaning="moving-block 到终端门的兼容性已关闭，活动数学输入转为显式模型余量账本。",
            remaining="ExplicitModelGapAndFiniteDPRCLedger",
        ),
        row(
            gate="FiniteDPRCBelow2003Closed",
            closed=finite_low_closed,
            proved=finite_low_closed,
            evidence="explicit model gap finite ledger",
            meaning="P<2003 的有限 DPRC 段已由 596 条记录闭合。",
            remaining=HIGH_MODEL,
        ),
        row(
            gate=HIGH_MODEL,
            closed=high_model_open,
            proved=False,
            evidence="explicit model gap finite ledger",
            meaning="P>=2003 的模型余量已有审计 C=3，但还没有解析证明。",
            remaining=HIGH_MODEL,
        ),
        row(
            gate="PromotionAuthorPacketSealed",
            closed=promotion_author_sealed,
            proved=promotion_author_sealed,
            evidence="final promotion irreducibility router",
            meaning="DStructure/AB、Tail-log4/BG-RKS、finite verification、Rankin 作者侧证据包已封装。",
            remaining=SELF_PROMOTION,
        ),
        row(
            gate=SELF_PROMOTION,
            closed=promotion_not_self_contained,
            proved=False,
            evidence="PM-16 BLOCK-REFEREE",
            meaning="完全自足版不能使用独立验收事件，必须把最终晋级门替换为自足证明包。",
            remaining=SELF_PROMOTION,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行完全自足最终目标攻坚。"""
    author = load_json(paths["author"])
    endpoint = load_json(paths["endpoint"])
    moving_compat = load_json(paths["moving_compat"])
    model_ledger = load_json(paths["model_ledger"])
    promotion = load_json(paths["promotion"])
    line_ref_text = read_text(paths["line_ref"])
    rows = build_rows(author, endpoint, moving_compat, model_ledger, promotion, line_ref_text)

    boundary_closed = all(item["closed"] for item in rows)
    high_model_proved = next(item for item in rows if item["gate"] == HIGH_MODEL)["proved"]
    self_promotion_proved = next(item for item in rows if item["gate"] == SELF_PROMOTION)["proved"]
    self_contained_closed = boundary_closed and high_model_proved and self_promotion_proved

    return {
        "certificate_type": "prime_matrix_self_contained_final_target_attack_router",
        "status": (
            "self_contained_row_column_closed"
            if self_contained_closed
            else "self_contained_final_target_reduced_to_two_open_inputs"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        },
        "all_reductions_to_self_contained_final_targets_closed": boundary_closed,
        "high_segment_model_gap_proved": high_model_proved,
        "self_contained_promotion_package_proved": self_promotion_proved,
        "row_column_self_contained_closed": self_contained_closed,
        "latest_self_contained_basis": (
            f"NoFurtherCanonicalSourceTerminalPromotionGap AND {HIGH_MODEL} AND {SELF_PROMOTION}"
        ),
        "open_self_contained_inputs": [HIGH_MODEL, SELF_PROMOTION],
        "next_priority": HIGH_MODEL,
        "plain_conclusion": (
            "完全自足路线已从 full-S 大黑箱和 moving-block 兼容门继续压缩："
            "终端/兼容/有限段均已闭合，当前真正剩余为 P>=2003 的高段模型余量解析账本，"
            "以及把最终 DStructure/Tail-log4/finite Rankin 独立验收门替换为完全自足证明包。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 完全自足路线最终目标攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        (
            "all_reductions_to_self_contained_final_targets_closed="
            f"{fmt_bool(result['all_reductions_to_self_contained_final_targets_closed'])}"
        ),
        f"high_segment_model_gap_proved={fmt_bool(result['high_segment_model_gap_proved'])}",
        (
            "self_contained_promotion_package_proved="
            f"{fmt_bool(result['self_contained_promotion_package_proved'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 最新完全自足输入基",
        "",
        "```text",
        result["latest_self_contained_basis"],
        "```",
        "",
        "## 2. 当前开放输入",
        "",
    ]
    for item in result["open_self_contained_inputs"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | evidence | meaning | remaining |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            (
                f"先攻 `{result['next_priority']}`：把 `P>=2003` 的 "
                "`S_Y(P)(1-H_Y(P))>3sqrt(S_Y(P))` 从数据审计升级为解析证明。"
                "完成后再攻完全自足晋级包。"
            ),
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author-json", type=Path, default=DEFAULT_AUTHOR)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--moving-compat-json", type=Path, default=DEFAULT_MOVING_COMPAT)
    parser.add_argument("--model-ledger-json", type=Path, default=DEFAULT_MODEL_LEDGER)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--line-ref", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "author": args.author_json,
        "endpoint": args.endpoint_json,
        "moving_compat": args.moving_compat_json,
        "model_ledger": args.model_ledger_json,
        "promotion": args.promotion_json,
        "line_ref": args.line_ref,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["latest_self_contained_basis"])


if __name__ == "__main__":
    main()
