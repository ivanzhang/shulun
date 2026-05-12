#!/usr/bin/env python3
"""生成 strict 表尾项显式零点自由区路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_explicit_zero_free_table_tail_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-explicit-zero-free-table-tail-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-explicit-zero-free-table-tail-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-explicit-zero-free-table-tail-router.md"

LARGE_RH = MONOGRAPH / "prime-matrix-strict-large-finite-rh-verification-router.json"
ZERO_FREE_CONSTANTS = MONOGRAPH / "prime-matrix-b3-explicit-zero-free-constants-router.json"
ZERO_SUM = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [LARGE_RH, ZERO_FREE_CONSTANTS, ZERO_SUM, CLAIM_STATUS]

TARGET = "ExplicitZeroFreeRegionForTableTailLedger"
KADIRI_EXTERNAL = "Kadiri2004ExplicitZeroFreeRegionExternalAcceptedForTableTail"
CONSTANTS = "TableTailZeroFreeConstantsLedger"
HEIGHT_RANGE = "ZeroFreeTailHeightRangeAndTransitionLedger"
TAIL_BUDGET = "PsiEpsilonTailRemainderBudgetLedger"
CONTOUR_MATCH = "ZeroFreeTailToPsiEpsilonTableContourMatchLedger"
BRIDGE = "FiniteVerifiedZerosToZeroFreeTailTransitionLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

KADIRI_URL = "https://arxiv.org/abs/math/0401238"


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


def build_result() -> dict[str, Any]:
    """构造表尾项显式零点自由区证书。"""
    large_rh = load_json(LARGE_RH)
    zero_free = load_json(ZERO_FREE_CONSTANTS)
    zero_sum = load_json(ZERO_SUM)
    active = large_rh.get("next_direct_attack_target") == TARGET
    symbolic_or_internal_chain_present = zero_free.get("explicit_zero_free_constants_reduced") is True
    coarse_zero_sum_closed = zero_sum.get("zero_sum_contour_budget_self_contained_closed") is True
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            large_rh.get("counterexample_assumption_only") is True
            and large_rh.get("row_column_unconditional_closed") is False,
            True,
            "本步只审计 epsilon 表尾项零点自由区输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ExplicitZeroFreeTableTailGateActive",
            active,
            True,
            "大高度有限 RH 输入外部通道登记后，下一并列硬点是表尾项显式零点自由区。",
            TARGET,
        ),
        row(
            "KadiriExternalSourceIdentified",
            True,
            False,
            "Dusart 文献登记 Kadiri 显式零点自由区；可作为外部条件来源。",
            KADIRI_EXTERNAL,
        ),
        row(
            "ExistingInternalZeroFreeChainIsCoarse",
            symbolic_or_internal_chain_present,
            True,
            "仓库已有零点自由常数拆包和 C=1280 粗预算，但它不是 Dusart epsilon 表尾项的精确常数账本。",
            f"{CONSTANTS} AND {CONTOUR_MATCH}",
        ),
        row(
            "ExistingZeroSumContourBudgetNotEnoughForTable",
            coarse_zero_sum_closed,
            True,
            "C=1280,C_Z=65536 粗零点和预算已自足，但前面压力诊断显示它距离 eps_psi 表值约 10^12 倍。",
            TAIL_BUDGET,
        ),
        row(
            CONSTANTS,
            False,
            False,
            "需要明确表尾项使用的零点自由区公式、常数、适用高度和舍入方向。",
            KADIRI_EXTERNAL,
        ),
        row(
            HEIGHT_RANGE,
            False,
            False,
            "需要把大高度有限 RH 验证的终点与零点自由区尾项起点精确拼接。",
            BRIDGE,
        ),
        row(
            TAIL_BUDGET,
            False,
            False,
            "需要把零点自由区尾项、零点密度/和、平凡尾项分配到 eps_psi(28) 与中段表值预算。",
            CONTOUR_MATCH,
        ),
        row(
            CONTOUR_MATCH,
            False,
            False,
            "需要证明该尾项常数与 epsilon 表生成器的显式公式同口径，而不是另一个粗 contour 模板。",
            "PsiEpsilonTableComputationAlgorithmLedger",
        ),
        row(
            TARGET,
            False,
            False,
            "当前只登记 Kadiri 外部来源和粗内部链不足；表尾项零点自由区尚未作者侧闭合。",
            f"{CONSTANTS} AND {HEIGHT_RANGE} AND {TAIL_BUDGET} AND {CONTOUR_MATCH}",
        ),
        row(
            "ExternalConditionalLaneAvailable",
            True,
            False,
            "若接受 Kadiri/Dusart 外部常数和表算法，可条件推进到 finite-zero/tail 桥接审查。",
            KADIRI_EXTERNAL,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "表尾项零点自由区审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_explicit_zero_free_table_tail_router",
        "status": "explicit_zero_free_table_tail_external_kadiri_available_internal_table_constants_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "kadiri_external_source_identified": True,
        "explicit_zero_free_table_tail_closed": False,
        "table_tail_zero_free_constants_closed": False,
        "tail_height_transition_closed": False,
        "psi_epsilon_tail_remainder_budget_closed": False,
        "zero_free_tail_to_table_contour_match_closed": False,
        "existing_internal_zero_free_chain_present_but_coarse": symbolic_or_internal_chain_present,
        "existing_zero_sum_contour_budget_not_enough_for_table": coarse_zero_sum_closed,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "external_reference": {
            "id": "Kadiri 2004",
            "url": KADIRI_URL,
            "role": "external zero-free region source for table tail, not repository self-contained table-tail budget",
        },
        "replacement_self_contained": {
            TARGET: f"{CONSTANTS} AND {HEIGHT_RANGE} AND {TAIL_BUDGET} AND {CONTOUR_MATCH}",
            BRIDGE: "LargeFiniteRHVerificationForPsiEpsilonTableLedger AND ExplicitZeroFreeRegionForTableTailLedger AND SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger",
        },
        "next_direct_attack_target": BRIDGE,
        "parallel_attack_targets": [CONSTANTS, TAIL_BUDGET, CONTOUR_MATCH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "表尾项零点自由区路线已拆清：Kadiri 外部来源可登记，但作者侧还需表尾项所用常数、"
            "有限 RH 验证终点到零点自由尾项的高度拼接、尾项预算，以及与 epsilon 表生成器同口径的 contour 匹配。"
            "现有 C=1280,C_Z=65536 粗预算虽已自足，但此前压力诊断显示远不足以给出 Dusart 表值。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 表尾项显式零点自由区路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"kadiri_external_source_identified={fmt_bool(result['kadiri_external_source_identified'])}",
        f"explicit_zero_free_table_tail_closed={fmt_bool(result['explicit_zero_free_table_tail_closed'])}",
        f"table_tail_zero_free_constants_closed={fmt_bool(result['table_tail_zero_free_constants_closed'])}",
        f"tail_height_transition_closed={fmt_bool(result['tail_height_transition_closed'])}",
        f"psi_epsilon_tail_remainder_budget_closed={fmt_bool(result['psi_epsilon_tail_remainder_budget_closed'])}",
        f"zero_free_tail_to_table_contour_match_closed={fmt_bool(result['zero_free_tail_to_table_contour_match_closed'])}",
        f"existing_internal_zero_free_chain_present_but_coarse={fmt_bool(result['existing_internal_zero_free_chain_present_but_coarse'])}",
        f"existing_zero_sum_contour_budget_not_enough_for_table={fmt_bool(result['existing_zero_sum_contour_budget_not_enough_for_table'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部边界",
        "",
        f"- `{result['external_reference']['id']}`：{result['external_reference']['url']}",
        f"- role：{result['external_reference']['role']}",
        "",
        "## 2. 自足替换",
        "",
        "```text",
    ]
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 3. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 4. 下一最窄点",
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
