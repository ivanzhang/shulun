#!/usr/bin/env python3
"""行列命题无条件闭合终局判定路由器。

用法示例：
  python3 experiments/prime_matrix_unconditional_closure_endpoint_verdict_router.py

输出：
  docs/monograph/prime-matrix-unconditional-closure-endpoint-verdict-router.json
  docs/monograph/prime-matrix-unconditional-closure-endpoint-verdict-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_DUAL_NEXT = DOCS / "prime-matrix-dual-next-narrowest-attack-router.json"
DEFAULT_ANTIATOM_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
)
DEFAULT_TRILEMMA = DOCS / "prime-matrix-noncanonical-complement-trilemma-router.json"
DEFAULT_ATLAS = DOCS / "prime-matrix-closure-input-atlas-router.json"
DEFAULT_PROMOTION = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-unconditional-closure-endpoint-verdict-router.json"
DEFAULT_MD = DOCS / "prime-matrix-unconditional-closure-endpoint-verdict-router.md"

NEW_SOURCE_ANTIATOM = "NewFullSNonAPSourceAntiAtomTheoremInput"
EXTERNAL_CONTRACT = "AcceptFullSKLSExtExternalContract"
NEW_FULL_S_THEOREM = "NewFullSTheoremInput"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希，便于复现审查。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值写为小写文本。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def verdict_row(
    gate: str,
    boundary_closed: bool,
    proved_or_accepted: bool,
    verdict: str,
    evidence: str,
    consequence: str,
    required_action: str,
) -> dict[str, Any]:
    """构造终局判定表行。"""
    return {
        "gate": gate,
        "boundary_closed": boundary_closed,
        "proved_or_accepted": proved_or_accepted,
        "verdict": verdict,
        "evidence": evidence,
        "consequence": consequence,
        "required_action": required_action,
    }


def build_rows(
    dual_next: dict[str, Any],
    antiatom_nogo: dict[str, Any],
    trilemma: dict[str, Any],
    atlas: dict[str, Any],
    promotion: dict[str, Any],
) -> list[dict[str, Any]]:
    """汇总所有终端输入，形成无条件闭合终局判定。"""
    atlas_complete = atlas.get("canonical_source_self_contained_closed") is True
    dual_boundary = dual_next.get("dual_next_narrowest_boundary_closed") is True
    antiatom_refuted = (
        antiatom_nogo.get("self_contained_generic_version_refuted") is True
        and antiatom_nogo.get("self_contained_generic_version_closed_as_proof") is False
    )
    trilemma_closed = trilemma.get("trilemma_boundary_closed") is True
    self_contained_closed = False
    external_accepted = False
    no_blackbox_new_theorem_proved = False
    promotion_boundary = promotion.get("promotion_package_boundary_closed") is True
    promotion_accepted = promotion.get("promotion_package_independently_accepted") is True

    return [
        verdict_row(
            gate="ClosureAtlasImported",
            boundary_closed=atlas_complete,
            proved_or_accepted=atlas_complete,
            verdict="closed_boundary",
            evidence=atlas.get("status", "unknown"),
            consequence="方阵斜线、圆柱覆盖、P列锚、层叠筛和命名出口已被压成有限输入图谱。",
            required_action="继续只攻命名输入，不回到无名分支。",
        ),
        verdict_row(
            gate="DualNextNarrowestBoundaryClosed",
            boundary_closed=dual_boundary,
            proved_or_accepted=False,
            verdict="three_legal_lanes_pinned",
            evidence=dual_next.get("unified_dual_basis", "unknown"),
            consequence="终局只剩自足新源定理、外部合同接受、无黑箱新 full-S 定理三路，加独立晋级门。",
            required_action=(
                f"prove {NEW_SOURCE_ANTIATOM}, accept {EXTERNAL_CONTRACT}, "
                f"or prove {NEW_FULL_S_THEOREM}"
            ),
        ),
        verdict_row(
            gate="GenericSelfContainedLaneRejected",
            boundary_closed=antiatom_refuted,
            proved_or_accepted=antiatom_refuted,
            verdict="refuted_not_open",
            evidence=antiatom_nogo.get("terminal_gap_after_router", "unknown"),
            consequence="现有 formal WFD/Type/Fourier/K4K6/incidence 模板下，generic 自足反原子不是未证，而是被 moving-delta 反模型排除。",
            required_action="只能加强 actual source 假设、限制到 canonical 分支，或走外部定理。",
        ),
        verdict_row(
            gate="NoncanonicalTrilemmaBoundaryClosed",
            boundary_closed=trilemma_closed,
            proved_or_accepted=False,
            verdict="input_still_conditional",
            evidence=trilemma.get("status", "unknown"),
            consequence="扣除 canonical 分支后，noncanonical full-S 补集没有第四条自足逃逸路。",
            required_action=(
                "证明实际源恒等、强化实际源反原子，或接受/证明精确 FullS-KLS-ext。"
            ),
        ),
        verdict_row(
            gate="SelfContainedNewSourceTheoremOpen",
            boundary_closed=True,
            proved_or_accepted=self_contained_closed,
            verdict="open_new_theorem_input",
            evidence=NEW_SOURCE_ANTIATOM,
            consequence="无条件自足闭合必须新增并证明实际 noncanonical full-S 源的强化反原子。",
            required_action=f"prove {NEW_SOURCE_ANTIATOM}",
        ),
        verdict_row(
            gate="ExternalBlackBoxNotAcceptedAsFinalInput",
            boundary_closed=True,
            proved_or_accepted=external_accepted,
            verdict="available_but_not_accepted",
            evidence=EXTERNAL_CONTRACT,
            consequence="外部合同可关闭数学 lane，但当前证书没有把它登记为最终已接受输入。",
            required_action=f"explicitly accept {EXTERNAL_CONTRACT} as an external theorem input",
        ),
        verdict_row(
            gate="ExternalNoBlackBoxNewTheoremOpen",
            boundary_closed=True,
            proved_or_accepted=no_blackbox_new_theorem_proved,
            verdict="open_new_external_theorem",
            evidence=NEW_FULL_S_THEOREM,
            consequence="DI/BFI 主来源特化和 APSourceLift 已被 no-go 排除；无黑箱外部线需要新 full-S 定理证明。",
            required_action=f"prove {NEW_FULL_S_THEOREM}",
        ),
        verdict_row(
            gate="DStructureRankinPromotionOpen",
            boundary_closed=promotion_boundary,
            proved_or_accepted=promotion_accepted,
            verdict="referee_acceptance_open",
            evidence=promotion.get("status", "unknown"),
            consequence="即便某条数学 lane 闭合，完整行/列无条件定理仍需独立晋级验收。",
            required_action=f"obtain {PROMOTION_GATE}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行终局判定。"""
    dual_next = load_json(paths["dual_next"])
    antiatom_nogo = load_json(paths["antiatom_nogo"])
    trilemma = load_json(paths["trilemma"])
    atlas = load_json(paths["atlas"])
    promotion = load_json(paths["promotion"])

    rows = build_rows(
        dual_next=dual_next,
        antiatom_nogo=antiatom_nogo,
        trilemma=trilemma,
        atlas=atlas,
        promotion=promotion,
    )

    boundary_closed = all(row["boundary_closed"] for row in rows)
    any_math_lane_accepted = any(
        row["gate"] in {
            "SelfContainedNewSourceTheoremOpen",
            "ExternalBlackBoxNotAcceptedAsFinalInput",
            "ExternalNoBlackBoxNewTheoremOpen",
        }
        and row["proved_or_accepted"]
        for row in rows
    )
    promotion_accepted = any(
        row["gate"] == "DStructureRankinPromotionOpen"
        and row["proved_or_accepted"]
        for row in rows
    )
    unconditional_closed = any_math_lane_accepted and promotion_accepted

    return {
        "certificate_type": "prime_matrix_unconditional_closure_endpoint_verdict_router",
        "status": "unconditional_closure_endpoint_boundary_closed_inputs_still_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{
                str(path.relative_to(ROOT)): file_sha256(path)
                for path in paths.values()
            },
        },
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "endpoint_boundary_closed": boundary_closed,
        "unconditional_closure_from_current_corpus": False,
        "all_required_inputs_proved_or_accepted": unconditional_closed,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": unconditional_closed,
        "hard_stop_reason": (
            "当前材料已关闭所有无名逃逸和边界分类，但 generic 自足 full-S 反原子被 "
            "moving-delta 模型排除；外部合同尚未登记为最终接受输入；无黑箱外部线需要新 "
            "full-S 定理；DStructure/Rankin 晋级仍未独立接受。因此不能从当前语料库推出"
            "完整无条件闭合。"
        ),
        "valid_closure_schemas": [
            f"{NEW_SOURCE_ANTIATOM} AND {PROMOTION_GATE}",
            f"{EXTERNAL_CONTRACT} AND {PROMOTION_GATE}",
            f"{NEW_FULL_S_THEOREM} AND {PROMOTION_GATE}",
        ],
        "next_atomic_actions": [
            f"Prove {NEW_SOURCE_ANTIATOM}",
            f"Or explicitly accept {EXTERNAL_CONTRACT}",
            f"Or prove {NEW_FULL_S_THEOREM}",
            f"Then obtain {PROMOTION_GATE}",
        ],
        "rows": rows,
        "closed_boundary_gates": [
            row["gate"] for row in rows if row["boundary_closed"]
        ],
        "open_proof_or_acceptance_gates": [
            row["gate"] for row in rows if not row["proved_or_accepted"]
        ],
        "plain_conclusion": (
            "终局硬攻结果是负向闭合加输入基闭合：当前材料不能无条件推出行/列命题。"
            "原因不是还存在无名结构逃逸，而是所有逃逸已被压成命名输入；其中 generic 自足"
            "反原子已被反模型排除，剩余只能由新源定理、外部 FullS-KLS-ext 接受、或新 full-S "
            "无黑箱定理之一闭合，并且还必须通过 DStructure/Rankin 独立验收。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 无条件闭合终局判定路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"endpoint_boundary_closed={fmt_bool(result['endpoint_boundary_closed'])}",
        (
            "unconditional_closure_from_current_corpus="
            f"{fmt_bool(result['unconditional_closure_from_current_corpus'])}"
        ),
        (
            "all_required_inputs_proved_or_accepted="
            f"{fmt_bool(result['all_required_inputs_proved_or_accepted'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 终局硬停原因",
        "",
        result["hard_stop_reason"],
        "",
        "## 2. 可升级闭合模式",
        "",
    ]
    for schema in result["valid_closure_schemas"]:
        lines.append(f"- `{schema}`")
    lines.extend(
        [
            "",
            "## 3. 下一原子动作",
            "",
        ]
    )
    for action in result["next_atomic_actions"]:
        lines.append(f"- {action}")
    lines.extend(
        [
            "",
            "## 4. 终局判定表",
            "",
            "| gate | boundary closed | proved/accepted | verdict | evidence | consequence | required action |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{boundary}` | `{proved}` | `{verdict}` | {evidence} | {consequence} | {required} |".format(
                gate=table_cell(row["gate"]),
                boundary=fmt_bool(row["boundary_closed"]),
                proved=fmt_bool(row["proved_or_accepted"]),
                verdict=table_cell(row["verdict"]),
                evidence=table_cell(row["evidence"]),
                consequence=table_cell(row["consequence"]),
                required=table_cell(row["required_action"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 判定",
            "",
            "当前证书已经把“还能不能直接闭合”判定到底：不能从当前语料库无条件闭合。"
            "这不是停止研究，而是终局路线图的精确化；任何后续闭合必须显式补齐上面的"
            "新定理输入或外部接受输入，并通过独立晋级门。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dual-next-json", type=Path, default=DEFAULT_DUAL_NEXT)
    parser.add_argument("--antiatom-nogo-json", type=Path, default=DEFAULT_ANTIATOM_NOGO)
    parser.add_argument("--trilemma-json", type=Path, default=DEFAULT_TRILEMMA)
    parser.add_argument("--atlas-json", type=Path, default=DEFAULT_ATLAS)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "dual_next": args.dual_next_json,
        "antiatom_nogo": args.antiatom_nogo_json,
        "trilemma": args.trilemma_json,
        "atlas": args.atlas_json,
        "promotion": args.promotion_json,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["hard_stop_reason"])


if __name__ == "__main__":
    main()
