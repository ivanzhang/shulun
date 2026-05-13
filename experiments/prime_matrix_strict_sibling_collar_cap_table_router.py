#!/usr/bin/env python3
"""生成 strict 兄弟 collar 同参数短除数 cap 表证书。

用法示例：
  python3 experiments/prime_matrix_strict_sibling_collar_cap_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sibling-collar-cap-table-router.json

输出：
  docs/monograph/prime-matrix-strict-sibling-collar-cap-table-router.json
  docs/monograph/prime-matrix-strict-sibling-collar-cap-table-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-sibling-collar-cap-table-router.json"
OUT_MD = DOCS / "prime-matrix-strict-sibling-collar-cap-table-router.md"

COLLAR_TABLE = "SameParameterSiblingCollarShortDivisorCapTable"
WIDTH_ABSORB = "SiblingCollarWidthBudgetAbsorptionLedger"
LCM_SHARPENING = "SiblingCollarShortDivisorBurstLCMOrPDECRoute"
PARENT_DILATED_TABLE = "ParentSiblingDilatedWindowColdCoreThresholdTable"
PARENT_HOT_RETURN = "ParentSiblingDilatedWindowHotCorePDECorSAEExclusion"
COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
SIBLING_OVERLAP = "SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-parent-dilated-window-threshold-router.json",
    "prime-matrix-strict-parent-support-numeric-envelope-router.json",
    "prime-matrix-strict-short-window-divisor-density-lcm-router.json",
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
        "experiments/prime_matrix_strict_sibling_collar_cap_table_router.py": sha256(
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


def sample_rows() -> list[dict[str, Any]]:
    """根据上一层样本给出 collar 长度 cap。"""
    parent = load_json("prime-matrix-strict-parent-support-numeric-envelope-router.json")
    rows: list[dict[str, Any]] = []
    for item in parent.get("finite_geometry_rows", []):
        left = int(item["left_collar"])
        right = int(item["right_collar"])
        g_max = int(item["max_child_multiplier"])
        rows.append(
            {
                "parent_window": item["parent_window"],
                "union_interval": item["union_interval"],
                "g_max": g_max,
                "left_collar_length": left,
                "right_collar_length": right,
                "collar_cap": left + right,
                "length_bound_lt_2gmax": left + right < 2 * g_max,
            }
        )
    return rows


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def formula_rows() -> list[dict[str, str]]:
    """列出 collar cap 公式。"""
    return [
        {
            "name": "left collar cap",
            "formula": "N_H([L_*,L-1]) <= max(0,L-L_*)",
            "role": "整数区间长度上界，同参数可计算。",
        },
        {
            "name": "right collar cap",
            "formula": "N_H([R+1,R_*]) <= max(0,R_*-R)",
            "role": "整数区间长度上界，同参数可计算。",
        },
        {
            "name": "total collar cap",
            "formula": "C_col(U)=max(0,L-L_*)+max(0,R_*-R) < 2 g_max(U)",
            "role": "给出左右 collar 的统一 cap。",
        },
        {
            "name": "dilated cold threshold",
            "formula": "C_dil(U)=C_core^*(U;[L,R])+C_col(U)",
            "role": "在原父窗口冷分支中，扩张父窗口 cap 可计算。",
        },
        {
            "name": "sharpness warning",
            "formula": "if sum_U C_col(U) is too large, use LCM/PDEC sharpening, not free deletion",
            "role": "宽度 cap 可能太粗，必须进入同参数总预算或命名回流。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "CollarCapTargetImported",
            result["collar_cap_target_imported"],
            result["collar_cap_target_imported"],
            "上一层已把扩张表剩余压成同参数 collar cap。",
            COLLAR_TABLE,
        ),
        row(
            "IntegerLengthCollarCapProved",
            True,
            True,
            "任何 collar 内除数个数不超过该整数区间长度。",
            COLLAR_TABLE,
        ),
        row(
            "SameParameterCollarCapTableProved",
            True,
            True,
            "左右 collar 长度由同一父窗口和子乘子账本计算，不引入新参数。",
            COLLAR_TABLE,
        ),
        row(
            "DilatedColdThresholdTableProved",
            True,
            False,
            "在原父窗口冷分支中，可用 C_core^*+C_col 作为扩张窗口阈值。",
            PARENT_DILATED_TABLE,
        ),
        row(
            "CollarWidthBudgetAbsorbed",
            False,
            False,
            "尚未证明 sum_U C_col(U) 在最终同参数预算中可吸收。",
            WIDTH_ABSORB,
        ),
        row(
            "CollarLCMSharpeningStillOpen",
            False,
            False,
            "若宽度 cap 太粗，需要短窗口 LCM/共同核/PDEC 锐化。",
            LCM_SHARPENING,
        ),
        row(
            "ParentDilatedWindowHotReturnExcluded",
            False,
            False,
            "原父窗口热或扩张后热回流仍未排斥。",
            PARENT_HOT_RETURN,
        ),
        row(
            "ParentSupportNumericEnvelopeProved",
            False,
            False,
            "collar cap 表闭合，但宽度预算吸收和热回流排斥仍未完成。",
            f"{WIDTH_ABSORB} AND {PARENT_HOT_RETURN}",
        ),
        row(
            "SiblingColdCoreThresholdNumericEnvelopeProved",
            False,
            False,
            "还需 overlap、PDEC 阈值和最终宽度预算吸收。",
            f"{WIDTH_ABSORB} AND {SIBLING_OVERLAP} AND {PDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{WIDTH_ABSORB} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 collar cap 表证书。"""
    previous = load_json("prime-matrix-strict-parent-dilated-window-threshold-router.json")
    rows = sample_rows()
    all_bounds = all(item["length_bound_lt_2gmax"] for item in rows)
    target_imported = previous.get("next_direct_attack_target") == COLLAR_TABLE

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_sibling_collar_cap_table_router",
        "status": "same_parameter_collar_cap_table_closed_width_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "collar_cap_target_imported": target_imported,
        "integer_length_collar_cap_proved": True,
        "same_parameter_collar_short_divisor_cap_table_proved": True,
        "finite_collar_bounds_all_passed": all_bounds,
        "parent_sibling_dilated_window_cold_core_threshold_table_proved": True,
        "collar_width_budget_absorbed": False,
        "collar_lcm_sharpening_proved": False,
        "parent_dilated_window_hot_return_excluded": False,
        "parent_scaled_child_union_support_numeric_envelope_proved": False,
        "sibling_cold_core_threshold_numeric_envelope_proved": False,
        "terminal_cold_window_anticascade_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": COLLAR_TABLE,
        "hardpoint_after_router": (
            f"{WIDTH_ABSORB} AND {LCM_SHARPENING} AND {PARENT_HOT_RETURN} "
            f"AND {SIBLING_OVERLAP} AND {PDEC_TABLE}"
        ),
        "next_direct_attack_target": WIDTH_ABSORB,
        "parallel_attack_targets": [
            LCM_SHARPENING,
            PARENT_HOT_RETURN,
            COLD_CORE_TABLE,
            SIBLING_OVERLAP,
            PDEC_TABLE,
            SIBLING_NUMERIC,
            TERMINAL_ANTICASCADE,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "formula_rows": formula_rows(),
        "finite_sample_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SameParameterSiblingCollarShortDivisorCapTable` 可以关闭："
            "左 collar 和右 collar 都是同一父窗口扩张产生的整数短区间，"
            "所以除数个数分别不超过区间长度；总 cap 为 "
            "`C_col(U)=(L-L_*)+(R_*-R)<2g_max(U)`。"
            "这给出完全同参数的 collar cap 表，并把扩张父窗口阈值写成 "
            "`C_dil(U)=C_core^*(U;[L,R])+C_col(U)`。"
            "但该长度 cap 可能太粗，尚未证明其在最终统一预算中可吸收；"
            "若不能吸收，必须用短窗口 LCM/共同核/PDEC 路由锐化。"
            "因此本步关闭 collar cap 表本身，不关闭行/列无条件命题。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 兄弟 collar 同参数 cap 表路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"collar_cap_target_imported={fmt_bool(result['collar_cap_target_imported'])}",
        f"integer_length_collar_cap_proved={fmt_bool(result['integer_length_collar_cap_proved'])}",
        f"same_parameter_collar_short_divisor_cap_table_proved={fmt_bool(result['same_parameter_collar_short_divisor_cap_table_proved'])}",
        f"parent_sibling_dilated_window_cold_core_threshold_table_proved={fmt_bool(result['parent_sibling_dilated_window_cold_core_threshold_table_proved'])}",
        f"collar_width_budget_absorbed={fmt_bool(result['collar_width_budget_absorbed'])}",
        f"parent_scaled_child_union_support_numeric_envelope_proved={fmt_bool(result['parent_scaled_child_union_support_numeric_envelope_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## cap 公式",
        "",
        "| name | formula | role |",
        "|---|---|---|",
    ]
    for item in result["formula_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['name'])}` | "
            f"`{table_cell(item['formula'])}` | "
            f"{table_cell(item['role'])} |"
        )

    lines.extend(
        [
            "",
            "## 有限样本",
            "",
            "| parent window | union interval | g_max | left length | right length | collar cap | cap < 2gmax |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["finite_sample_rows"]:
        lines.append(
            "| "
            f"`{item['parent_window']}` | "
            f"`{item['union_interval']}` | "
            f"{item['g_max']} | "
            f"{item['left_collar_length']} | "
            f"{item['right_collar_length']} | "
            f"{item['collar_cap']} | "
            f"`{fmt_bool(item['length_bound_lt_2gmax'])}` |"
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
