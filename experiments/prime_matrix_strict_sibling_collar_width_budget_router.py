#!/usr/bin/env python3
"""生成 strict 兄弟 collar 宽度预算吸收攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_sibling_collar_width_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sibling-collar-width-budget-router.json

输出：
  docs/monograph/prime-matrix-strict-sibling-collar-width-budget-router.json
  docs/monograph/prime-matrix-strict-sibling-collar-width-budget-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-sibling-collar-width-budget-router.json"
OUT_MD = DOCS / "prime-matrix-strict-sibling-collar-width-budget-router.md"

WIDTH_ABSORB = "SiblingCollarWidthBudgetAbsorptionLedger"
WIDTH_LCM = "SiblingCollarWidthLCMKernelCompressionLedger"
WIDTH_SUM = "SameParameterSiblingCollarWidthFiniteSumTable"
LCM_SHARPENING = "SiblingCollarShortDivisorBurstLCMOrPDECRoute"
PARENT_HOT_RETURN = "ParentSiblingDilatedWindowHotCorePDECorSAEExclusion"
COLLAR_TABLE = "SameParameterSiblingCollarShortDivisorCapTable"
PARENT_DILATED_TABLE = "ParentSiblingDilatedWindowColdCoreThresholdTable"
SIBLING_OVERLAP = "SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-sibling-collar-cap-table-router.json",
    "prime-matrix-strict-parent-dilated-window-threshold-router.json",
    "prime-matrix-strict-short-window-divisor-density-lcm-router.json",
    "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    "prime-matrix-strict-large-pair-kernel-difference-router.json",
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
        "experiments/prime_matrix_strict_sibling_collar_width_budget_router.py": sha256(
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


def obstruction_rows() -> list[dict[str, Any]]:
    """给出粗宽度预算不能直接吸收的指数模型。"""
    alpha = 0.43
    rows = []
    for family_exp, g_exp in [(0.10, 0.10), (0.20, 0.20), (0.30, 0.20), (0.43, 0.43)]:
        width_exp = family_exp + g_exp
        rows.append(
            {
                "family_count_exponent": family_exp,
                "gmax_exponent": g_exp,
                "crude_width_sum_exponent": width_exp,
                "demand_exponent_alpha": alpha,
                "crude_absorbed_by_alpha": width_exp < alpha,
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


def dichotomy_rows() -> list[dict[str, str]]:
    """列出宽度预算二分。"""
    return [
        {
            "case": "finite width sum table",
            "criterion": "sum_U (T_U-1) C_col(U) <= U_col,0(P,z,Lambda)",
            "route": "若 U_col,0 与既有 U_cold 合并后仍小于需求余量，则宽度预算吸收。",
        },
        {
            "case": "many large g_max",
            "criterion": "同一前缀下大 g_max 频繁出现",
            "route": "LCM 乘子纪律迫使频率高度爆炸，或产生低乘子共同核。",
        },
        {
            "case": "low-multiplier kernel",
            "criterion": "g_t 与既有 lcm 共享大共同核",
            "route": "进入大成对差值锁、多源 fan-in、固定历史 PDEC 或 SAE。",
        },
        {
            "case": "persistent width packet",
            "criterion": "同一 collar shape/formal unit 重复超阈值",
            "route": "进入固定历史/ColumnCRT/PDEC，不留在非持久冷供给。",
        },
        {
            "case": "nonpersistent sparse width",
            "criterion": "所有宽度包均不持久",
            "route": "进入有限历史 SAE 求和，回到同参数 U_cold 正余量。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "WidthAbsorptionTargetImported",
            result["width_absorption_target_imported"],
            result["width_absorption_target_imported"],
            "上一层已把 collar cap 后的剩余压成宽度预算吸收。",
            WIDTH_ABSORB,
        ),
        row(
            "CrudeWidthCapImported",
            True,
            True,
            "每个 collar 宽度满足 C_col(U)<2g_max(U)。",
            COLLAR_TABLE,
        ),
        row(
            "NaiveWidthAbsorptionRejected",
            True,
            True,
            "仅靠 sum 2g_max 的粗估可超过 alpha=0.43 需求阶。",
            WIDTH_LCM,
        ),
        row(
            "WidthDichotomyRegistered",
            True,
            False,
            "宽度预算失败只能来自大 g_max、共同核、持久包或非持久 SAE。",
            WIDTH_LCM,
        ),
        row(
            "SameParameterWidthFiniteSumTableProved",
            False,
            False,
            "尚未给出 sum_U (T_U-1)C_col(U) 的同参数有限总和表。",
            WIDTH_SUM,
        ),
        row(
            "WidthLCMKernelCompressionProved",
            False,
            False,
            "尚未证明宽度过大必触发 LCM 高度矛盾或共同核回流。",
            WIDTH_LCM,
        ),
        row(
            "SiblingCollarWidthBudgetAbsorbed",
            False,
            False,
            "宽度 cap 表闭合，但总预算吸收/锐化仍未完成。",
            f"{WIDTH_SUM} OR {WIDTH_LCM}",
        ),
        row(
            "ParentSupportNumericEnvelopeProved",
            False,
            False,
            "父支撑仍需宽度吸收和热回流排斥。",
            f"{WIDTH_ABSORB} AND {PARENT_HOT_RETURN}",
        ),
        row(
            "SiblingColdCoreThresholdNumericEnvelopeProved",
            False,
            False,
            "还需 overlap、PDEC 阈值、宽度预算与热回流。",
            f"{WIDTH_ABSORB} AND {SIBLING_OVERLAP} AND {PDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{WIDTH_LCM} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 collar 宽度预算吸收攻坚证书。"""
    previous = load_json("prime-matrix-strict-sibling-collar-cap-table-router.json")
    target_imported = previous.get("next_direct_attack_target") == WIDTH_ABSORB
    rows = obstruction_rows()
    naive_failure_exists = any(not row_item["crude_absorbed_by_alpha"] for row_item in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_sibling_collar_width_budget_router",
        "status": "collar_width_budget_naive_absorption_rejected_lcm_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "width_absorption_target_imported": target_imported,
        "crude_width_cap_imported": previous.get("same_parameter_collar_short_divisor_cap_table_proved") is True,
        "naive_width_absorption_rejected": naive_failure_exists,
        "width_dichotomy_registered": True,
        "same_parameter_width_finite_sum_table_proved": False,
        "width_lcm_kernel_compression_proved": False,
        "sibling_collar_width_budget_absorbed": False,
        "parent_scaled_child_union_support_numeric_envelope_proved": False,
        "sibling_cold_core_threshold_numeric_envelope_proved": False,
        "terminal_cold_window_anticascade_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": WIDTH_ABSORB,
        "hardpoint_after_router": (
            f"({WIDTH_SUM} OR {WIDTH_LCM}) AND {LCM_SHARPENING} "
            f"AND {PARENT_HOT_RETURN} AND {SIBLING_OVERLAP} AND {PDEC_TABLE}"
        ),
        "next_direct_attack_target": WIDTH_LCM,
        "parallel_attack_targets": [
            WIDTH_SUM,
            LCM_SHARPENING,
            PARENT_HOT_RETURN,
            FIXED_HISTORY,
            SIBLING_OVERLAP,
            PDEC_TABLE,
            SIBLING_NUMERIC,
            TERMINAL_ANTICASCADE,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "obstruction_rows": rows,
        "dichotomy_rows": dichotomy_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SiblingCollarWidthBudgetAbsorptionLedger` 不能由粗宽度 cap 直接关闭。"
            "虽然每个 collar 有 `C_col(U)<2g_max(U)`，但若没有进一步限制 sibling family 数量和 "
            "`g_max` 的总和，形式上 `sum_U C_col(U)` 可达到超过 `P^0.43` 的阶，"
            "不能保证被最终需求余量吸收。合法下一步是二分：要么提交同参数宽度有限总和表，"
            "要么证明宽度过大强制同前缀大乘子密集，从而由 LCM 乘子纪律产生频率高度矛盾，"
            "或进入低乘子共同核、固定历史/PDEC/SAE 回流。"
            "本步关闭的是粗吸收不可用和宽度失败二分，不关闭最终命题。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 兄弟 collar 宽度预算吸收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"width_absorption_target_imported={fmt_bool(result['width_absorption_target_imported'])}",
        f"crude_width_cap_imported={fmt_bool(result['crude_width_cap_imported'])}",
        f"naive_width_absorption_rejected={fmt_bool(result['naive_width_absorption_rejected'])}",
        f"width_dichotomy_registered={fmt_bool(result['width_dichotomy_registered'])}",
        f"same_parameter_width_finite_sum_table_proved={fmt_bool(result['same_parameter_width_finite_sum_table_proved'])}",
        f"width_lcm_kernel_compression_proved={fmt_bool(result['width_lcm_kernel_compression_proved'])}",
        f"sibling_collar_width_budget_absorbed={fmt_bool(result['sibling_collar_width_budget_absorbed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 粗吸收阻塞模型",
        "",
        "| family exponent | gmax exponent | width exponent | alpha | absorbed |",
        "|---:|---:|---:|---:|---:|",
    ]
    for item in result["obstruction_rows"]:
        lines.append(
            "| "
            f"{item['family_count_exponent']:.2f} | "
            f"{item['gmax_exponent']:.2f} | "
            f"{item['crude_width_sum_exponent']:.2f} | "
            f"{item['demand_exponent_alpha']:.2f} | "
            f"`{fmt_bool(item['crude_absorbed_by_alpha'])}` |"
        )

    lines.extend(
        [
            "",
            "## 宽度失败二分",
            "",
            "| case | criterion | route |",
            "|---|---|---|",
        ]
    )
    for item in result["dichotomy_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['case'])}` | "
            f"{table_cell(item['criterion'])} | "
            f"{table_cell(item['route'])} |"
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
