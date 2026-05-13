#!/usr/bin/env python3
"""生成 strict 父支撑数值 envelope 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_parent_support_numeric_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-parent-support-numeric-envelope-router.json

输出：
  docs/monograph/prime-matrix-strict-parent-support-numeric-envelope-router.json
  docs/monograph/prime-matrix-strict-parent-support-numeric-envelope-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-parent-support-numeric-envelope-router.json"
OUT_MD = DOCS / "prime-matrix-strict-parent-support-numeric-envelope-router.md"

PARENT_SUPPORT = "ParentScaledChildUnionSupportNumericEnvelope"
PARENT_DILATED_TABLE = "ParentSiblingDilatedWindowColdCoreThresholdTable"
PARENT_HOT_RETURN = "ParentSiblingDilatedWindowHotCorePDECorSAEExclusion"
COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
SIBLING_OVERLAP = "SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-sibling-numeric-envelope-attack-router.json",
    "prime-matrix-strict-cold-window-sibling-charging-router.json",
    "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json",
    "prime-matrix-strict-product-window-endpoint-generator-appendix-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_parent_support_numeric_envelope_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def scaled_child_interval(parent_left: int, parent_right: int, g: int) -> tuple[int, int]:
    """把子窗口按 g 重新投回父频率尺度。"""
    child_left = parent_left // g
    child_right = math.ceil(parent_right / g)
    return g * child_left, g * child_right


def union_geometry(parent_left: int, parent_right: int, children: list[int]) -> dict[str, Any]:
    """核验 scaled-child union 是单个 collar 扩张区间。"""
    intervals = [scaled_child_interval(parent_left, parent_right, g) for g in children]
    union_left = min(left for left, _right in intervals)
    union_right = max(right for _left, right in intervals)
    max_g = max(children)
    left_collar = parent_left - union_left
    right_collar = union_right - parent_right
    all_contain_parent = all(left <= parent_left and parent_right <= right for left, right in intervals)
    collar_bound_holds = 0 <= left_collar < max_g and 0 <= right_collar < max_g
    return {
        "parent_window": [parent_left, parent_right],
        "children": children,
        "scaled_child_intervals": [[left, right] for left, right in intervals],
        "union_interval": [union_left, union_right],
        "max_child_multiplier": max_g,
        "left_collar": left_collar,
        "right_collar": right_collar,
        "all_scaled_children_contain_parent": all_contain_parent,
        "collar_width_lt_max_child": collar_bound_holds,
        "union_is_single_interval": all_contain_parent,
    }


def geometry_rows() -> list[dict[str, Any]]:
    """生成有限几何核验样本。"""
    return [
        union_geometry(20, 180, [2, 3, 5, 6]),
        union_geometry(30, 240, [2, 3, 4, 5, 7]),
        union_geometry(50, 420, [3, 4, 5, 6, 7, 9]),
        union_geometry(60, 720, [4, 5, 6, 7, 8, 9, 10]),
        union_geometry(401, 4001, [11, 13, 17, 19, 23]),
    ]


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def lemma_rows() -> list[dict[str, str]]:
    """列出父支撑 envelope 的压缩引理。"""
    return [
        {
            "lemma": "scaled child interval contains parent interval",
            "statement": "g*floor(L/g)<=L<=R<=g*ceil(R/g)",
            "effect": "所有兄弟投影窗口都覆盖同一个父窗口。",
        },
        {
            "lemma": "single collar interval",
            "statement": "union_g [g floor(L/g),g ceil(R/g)] = [L_*,R_*]",
            "effect": "scaled-child union 不是多段并集，而是单个 collar 扩张。",
        },
        {
            "lemma": "collar width",
            "statement": "0<=L-L_*<g_max and 0<=R_*-R<g_max",
            "effect": "边界外扩只由最大子乘子控制。",
        },
        {
            "lemma": "parent divisor support",
            "statement": "pi(F_U) subset {d:d|H_U, d in [L_*,R_*]}",
            "effect": "父支撑数值界可接入规范冷核心窗口表。",
        },
        {
            "lemma": "cold or hot parent window",
            "statement": "N_{H_U}([L_*,R_*])<=C_core^*(parent key) or hot return",
            "effect": "若父扩张窗口不冷，失败必须命名为热核心/PDEC/SAE。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "ParentSupportTargetImported",
            result["parent_support_target_imported"],
            result["parent_support_target_imported"],
            "上一层已把 sibling numeric envelope 压成父投影支撑。",
            PARENT_SUPPORT,
        ),
        row(
            "ScaledChildUnionSingleIntervalProved",
            True,
            True,
            "同一父窗口外向缩放回来的兄弟投影并集是单个 collar 扩张区间。",
            PARENT_DILATED_TABLE,
        ),
        row(
            "CollarWidthBoundProved",
            True,
            True,
            "左右 collar 宽度均小于最大子乘子。",
            PARENT_DILATED_TABLE,
        ),
        row(
            "ProjectedSupportToDilatedWindowProved",
            True,
            True,
            "父投影支撑被单个扩张父窗口上的除数计数控制。",
            PARENT_DILATED_TABLE,
        ),
        row(
            "ConditionalColdCoreInsertionClosed",
            True,
            False,
            "若扩张父窗口冷，则支撑项可由 C_core^* 表控制。",
            COLD_CORE_TABLE,
        ),
        row(
            "ParentDilatedWindowHotReturnExcluded",
            False,
            False,
            "若扩张父窗口热，仍需排斥热核心/PDEC/SAE 回流。",
            PARENT_HOT_RETURN,
        ),
        row(
            "ParentSupportNumericEnvelopeProved",
            False,
            False,
            "几何压缩已闭合，但冷核心数值表或热回流排斥尚未完成。",
            f"{PARENT_DILATED_TABLE} AND {PARENT_HOT_RETURN}",
        ),
        row(
            "SiblingColdCoreThresholdNumericEnvelopeProved",
            False,
            False,
            "父支撑数值界、overlap 和 PDEC 阈值仍未全部闭合。",
            f"{PARENT_DILATED_TABLE} AND {SIBLING_OVERLAP} AND {PDEC_TABLE}",
        ),
        row(
            "TerminalColdWindowAntiCascadeProved",
            False,
            False,
            "反级联仍需父扩张窗口数值表和热/固定历史排斥。",
            f"{SIBLING_NUMERIC} AND {HOT_CORE} AND {FIXED_HISTORY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{PARENT_DILATED_TABLE} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造父支撑数值 envelope 攻坚证书。"""
    previous = load_json("prime-matrix-strict-sibling-numeric-envelope-attack-router.json")
    threshold = load_json("prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json")
    rows = geometry_rows()
    geometry_passed = all(
        row_item["union_is_single_interval"] and row_item["collar_width_lt_max_child"]
        for row_item in rows
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_parent_support_numeric_envelope_router",
        "status": "parent_support_envelope_reduced_to_dilated_parent_window_cold_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "parent_support_target_imported": previous.get("next_direct_attack_target") == PARENT_SUPPORT,
        "sibling_projection_identity_imported": previous.get("sibling_multiset_projection_identity_proved") is True,
        "canonical_cold_core_registry_imported": (
            threshold.get("canonical_cold_core_threshold_registry_defined") is True
        ),
        "scaled_child_union_single_interval_geometry_proved": True,
        "finite_geometry_all_passed": geometry_passed,
        "collar_width_lt_max_child_proved": True,
        "projected_support_to_dilated_parent_window_proved": True,
        "parent_dilated_window_cold_core_table_proved": False,
        "parent_dilated_window_hot_return_excluded": False,
        "parent_scaled_child_union_support_numeric_envelope_proved": False,
        "sibling_cold_core_threshold_numeric_envelope_proved": False,
        "terminal_cold_window_anticascade_proved": False,
        "effective_cold_history_pruning_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": PARENT_SUPPORT,
        "hardpoint_after_router": (
            f"{PARENT_DILATED_TABLE} AND {PARENT_HOT_RETURN} "
            f"AND {SIBLING_OVERLAP} AND {PDEC_TABLE}"
        ),
        "next_direct_attack_target": PARENT_DILATED_TABLE,
        "parallel_attack_targets": [
            PARENT_HOT_RETURN,
            SIBLING_OVERLAP,
            COLD_CORE_TABLE,
            PDEC_TABLE,
            HOT_CORE,
            FIXED_HISTORY,
            TERMINAL_ANTICASCADE,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "lemma_rows": lemma_rows(),
        "finite_geometry_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ParentScaledChildUnionSupportNumericEnvelope` 的几何核心可以关闭："
            "若父窗口为 `[L,R]`，子乘子为 `g`，外向生成器给出子窗口 "
            "`[floor(L/g),ceil(R/g)]`，投回父尺度后为 "
            "`[g floor(L/g),g ceil(R/g)]`。每个这样的区间都包含 `[L,R]`，"
            "所以所有兄弟投影窗口的并集不是复杂多段集合，而是单个扩张父窗口 `[L_*,R_*]`；"
            "左右扩张宽度都小于最大子乘子。于是父投影支撑被 "
            "`N_{H_U}([L_*,R_*])` 控制，可接入规范 `C_core^*` 冷核心表。"
            "但要得到数值 envelope，还必须证明该扩张父窗口冷，或排斥热核心/PDEC/SAE 回流；"
            "因此行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 父支撑数值 envelope 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"parent_support_target_imported={fmt_bool(result['parent_support_target_imported'])}",
        f"sibling_projection_identity_imported={fmt_bool(result['sibling_projection_identity_imported'])}",
        f"scaled_child_union_single_interval_geometry_proved={fmt_bool(result['scaled_child_union_single_interval_geometry_proved'])}",
        f"collar_width_lt_max_child_proved={fmt_bool(result['collar_width_lt_max_child_proved'])}",
        f"projected_support_to_dilated_parent_window_proved={fmt_bool(result['projected_support_to_dilated_parent_window_proved'])}",
        f"parent_dilated_window_cold_core_table_proved={fmt_bool(result['parent_dilated_window_cold_core_table_proved'])}",
        f"parent_dilated_window_hot_return_excluded={fmt_bool(result['parent_dilated_window_hot_return_excluded'])}",
        f"parent_scaled_child_union_support_numeric_envelope_proved={fmt_bool(result['parent_scaled_child_union_support_numeric_envelope_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 几何引理",
        "",
        "| lemma | statement | effect |",
        "|---|---|---|",
    ]
    for item in result["lemma_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['lemma'])}` | "
            f"`{table_cell(item['statement'])}` | "
            f"{table_cell(item['effect'])} |"
        )

    lines.extend(
        [
            "",
            "## 有限几何核验",
            "",
            "| parent window | children | union interval | g_max | left collar | right collar | single interval | collar bound |",
            "|---|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["finite_geometry_rows"]:
        lines.append(
            "| "
            f"`{item['parent_window']}` | "
            f"`{item['children']}` | "
            f"`{item['union_interval']}` | "
            f"{item['max_child_multiplier']} | "
            f"{item['left_collar']} | "
            f"{item['right_collar']} | "
            f"`{fmt_bool(item['union_is_single_interval'])}` | "
            f"`{fmt_bool(item['collar_width_lt_max_child'])}` |"
        )

    lines.extend(
        [
            "",
            "## 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['gate'])}` | "
            f"`{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | "
            f"{table_cell(item['meaning'])} | "
            f"`{table_cell(item['remaining'])}` |"
        )

    lines.extend(
        [
            "",
            "## 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 并行保留：",
        ]
    )
    for target in result["parallel_attack_targets"]:
        lines.append(f"  - `{target}`")

    lines.extend(
        [
            "",
            "## 证据哈希",
            "",
            "| file | sha256 |",
            "|---|---|",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """主入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
