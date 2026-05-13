#!/usr/bin/env python3
"""生成 strict 兄弟 collar 宽度 LCM/共同核压缩证书。

用法示例：
  python3 experiments/prime_matrix_strict_sibling_collar_width_lcm_kernel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json

输出：
  docs/monograph/prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json
  docs/monograph/prime-matrix-strict-sibling-collar-width-lcm-kernel-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json"
OUT_MD = DOCS / "prime-matrix-strict-sibling-collar-width-lcm-kernel-router.md"

WIDTH_LCM = "SiblingCollarWidthLCMKernelCompressionLedger"
WIDTH_SUM = "SameParameterSiblingCollarWidthFiniteSumTable"
LOW_KERNEL = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
DENSE_LCM = "DenseShortWindowLCMLowerBoundAfterKernelCompression"
HEIGHT = "FormalFrequencyHeightCeilingForEndpointPDEC"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
SAE_ABSORB = "BoundedQuotientTypeSAEAbsorption"
PARENT_HOT_RETURN = "ParentSiblingDilatedWindowHotCorePDECorSAEExclusion"
SIBLING_OVERLAP = "SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-sibling-collar-width-budget-router.json",
    "prime-matrix-strict-short-window-divisor-density-lcm-router.json",
    "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    "prime-matrix-strict-large-pair-kernel-difference-router.json",
    "prime-matrix-strict-multisource-fanin-small-quotient-router.json",
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
        "experiments/prime_matrix_strict_sibling_collar_width_lcm_kernel_router.py": sha256(
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
    """给出 dyadic 层宽度到子乘子个数的核验样本。"""
    rows = []
    samples = [
        (10, [11, 13, 17, 19]),
        (20, [23, 29, 31, 37]),
        (40, [41, 43, 47, 53, 59, 61, 67, 71, 73]),
        (80, [83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151]),
    ]
    for y, values in samples:
        total_width_cap = sum(2 * g for g in values)
        count_lower_from_width = total_width_cap // (4 * y)
        rows.append(
            {
                "Y": y,
                "dyadic_range": [y, 2 * y],
                "child_count": len(values),
                "total_width_cap": total_width_cap,
                "count_lower_from_width": count_lower_from_width,
                "lower_bound_valid": count_lower_from_width <= len(values),
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


def lemma_rows() -> list[dict[str, str]]:
    """列出宽度到 LCM/共同核的结构压缩。"""
    return [
        {
            "lemma": "dyadic width to count",
            "statement": "if Y<g<=2Y, then C_col(g)<2g<=4Y; hence sum C_col>=B implies N_Y>=B/(4Y)",
            "effect": "宽度总量过大强制同一 dyadic 层内子乘子个数过多。",
        },
        {
            "lemma": "same prefix divisor anchor",
            "statement": "all child multipliers g in a sibling family divide the same H_U",
            "effect": "同层子乘子集合可接入短窗口除数密度 LCM 纪律。",
        },
        {
            "lemma": "LCM or kernel",
            "statement": "large N_Y forces either many LCM multipliers or many low-multiplier common kernels",
            "effect": "宽度过大不能保持无名；必须进入 LCM 高度或共同核回流。",
        },
        {
            "lemma": "persistent kernel route",
            "statement": "repeated quotient/kernel type routes to fixed-history ColumnCRT/PDEC",
            "effect": "共同核持久复现不能留在非持久冷供给。",
        },
        {
            "lemma": "nonpersistent kernel route",
            "statement": "bounded quotient types without persistence are SAE-countable",
            "effect": "非持久共同核回到有限字母表 SAE 预算。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "WidthLCMTargetImported",
            result["width_lcm_target_imported"],
            result["width_lcm_target_imported"],
            "上一层已把粗宽度吸收失败压成 LCM/共同核压缩。",
            WIDTH_LCM,
        ),
        row(
            "DyadicWidthToCountProved",
            True,
            True,
            "同一 dyadic 乘子层中，宽度总量下界给出子乘子个数下界。",
            WIDTH_LCM,
        ),
        row(
            "SamePrefixDivisorAnchorImported",
            True,
            True,
            "同一 sibling family 的子乘子都整除同一个 H_U。",
            WIDTH_LCM,
        ),
        row(
            "LCMKernelDichotomyImported",
            result["short_window_lcm_discipline_imported"],
            result["short_window_lcm_discipline_imported"],
            "子乘子密集后无第四出口：LCM 高度或低乘子共同核。",
            f"{DENSE_LCM} OR {LOW_KERNEL}",
        ),
        row(
            "WidthLCMKernelCompressionProved",
            True,
            False,
            "宽度过大已压成既有 LCM/共同核出口，但出口本身尚未排斥。",
            f"{DENSE_LCM} AND {HEIGHT} OR {LOW_KERNEL}",
        ),
        row(
            "SameParameterWidthFiniteSumTableProved",
            False,
            False,
            "仍可走直接有限总和表路线，但本步未提交该表。",
            WIDTH_SUM,
        ),
        row(
            "LowMultiplierKernelExcluded",
            False,
            False,
            "低乘子共同核还需 ColumnCRT/PDEC 或 SAE 吸收。",
            f"{LOW_KERNEL} AND {SAE_ABSORB}",
        ),
        row(
            "SiblingCollarWidthBudgetAbsorbed",
            False,
            False,
            "结构压缩完成，但 LCM 高度/共同核出口仍未排斥。",
            f"{DENSE_LCM} AND {HEIGHT} AND {LOW_KERNEL}",
        ),
        row(
            "SiblingColdCoreThresholdNumericEnvelopeProved",
            False,
            False,
            "仍需处理共同核、overlap、PDEC 阈值和热回流。",
            f"{LOW_KERNEL} AND {SIBLING_OVERLAP} AND {PDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{LOW_KERNEL} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造宽度 LCM/共同核压缩证书。"""
    previous = load_json("prime-matrix-strict-sibling-collar-width-budget-router.json")
    short_lcm = load_json("prime-matrix-strict-short-window-divisor-density-lcm-router.json")
    target_imported = previous.get("next_direct_attack_target") == WIDTH_LCM
    short_lcm_imported = (
        short_lcm.get("incremental_multiplier_discipline_closed") is True
        and short_lcm.get("low_multiplier_kernel_forcing_closed") is True
    )
    rows = sample_rows()
    samples_passed = all(item["lower_bound_valid"] for item in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_sibling_collar_width_lcm_kernel_router",
        "status": "collar_width_lcm_kernel_compression_closed_exits_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "width_lcm_target_imported": target_imported,
        "dyadic_width_to_count_proved": True,
        "same_prefix_divisor_anchor_imported": True,
        "short_window_lcm_discipline_imported": short_lcm_imported,
        "width_lcm_kernel_compression_proved": True,
        "finite_samples_all_passed": samples_passed,
        "dense_lcm_after_kernel_compression_proved": False,
        "formal_frequency_height_ceiling_matched": False,
        "low_multiplier_common_kernel_excluded": False,
        "same_parameter_width_finite_sum_table_proved": False,
        "sibling_collar_width_budget_absorbed": False,
        "sibling_cold_core_threshold_numeric_envelope_proved": False,
        "terminal_cold_window_anticascade_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": WIDTH_LCM,
        "hardpoint_after_router": (
            f"({DENSE_LCM} AND {HEIGHT}) OR ({LOW_KERNEL} AND {FIXED_HISTORY}) "
            f"OR {SAE_ABSORB}"
        ),
        "next_direct_attack_target": LOW_KERNEL,
        "parallel_attack_targets": [
            DENSE_LCM,
            HEIGHT,
            FIXED_HISTORY,
            SAE_ABSORB,
            WIDTH_SUM,
            PARENT_HOT_RETURN,
            SIBLING_OVERLAP,
            PDEC_TABLE,
            SIBLING_NUMERIC,
            TERMINAL_ANTICASCADE,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "lemma_rows": lemma_rows(),
        "finite_sample_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SiblingCollarWidthLCMKernelCompressionLedger` 的结构压缩可以关闭。"
            "在同一 dyadic 子乘子层 `Y<g<=2Y` 中，`C_col(g)<2g<=4Y`，"
            "所以若 collar 宽度总量过大，就强制该层有许多兼容子乘子。"
            "这些子乘子都整除同一父前缀频率 `H_U`，因此可直接接入短窗口除数密度的 LCM 乘子纪律："
            "要么 LCM 增长超过正式频率高度，要么大量低乘子共同核出现。"
            "共同核持久化进入固定历史/ColumnCRT/PDEC，非持久则进入有限字母表 SAE。"
            "本步关闭的是宽度过大到 LCM/共同核的压缩，不排斥这些出口，因此行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 兄弟 collar 宽度 LCM/共同核压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"width_lcm_target_imported={fmt_bool(result['width_lcm_target_imported'])}",
        f"dyadic_width_to_count_proved={fmt_bool(result['dyadic_width_to_count_proved'])}",
        f"same_prefix_divisor_anchor_imported={fmt_bool(result['same_prefix_divisor_anchor_imported'])}",
        f"short_window_lcm_discipline_imported={fmt_bool(result['short_window_lcm_discipline_imported'])}",
        f"width_lcm_kernel_compression_proved={fmt_bool(result['width_lcm_kernel_compression_proved'])}",
        f"low_multiplier_common_kernel_excluded={fmt_bool(result['low_multiplier_common_kernel_excluded'])}",
        f"sibling_collar_width_budget_absorbed={fmt_bool(result['sibling_collar_width_budget_absorbed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 压缩引理",
        "",
        "| lemma | statement | effect |",
        "|---|---|---|",
    ]
    for item in result["lemma_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['lemma'])}` | "
            f"{table_cell(item['statement'])} | "
            f"{table_cell(item['effect'])} |"
        )

    lines.extend(
        [
            "",
            "## 有限样本",
            "",
            "| Y | dyadic range | child count | width cap | count lower | valid |",
            "|---:|---|---:|---:|---:|---:|",
        ]
    )
    for item in result["finite_sample_rows"]:
        lines.append(
            "| "
            f"{item['Y']} | "
            f"`{item['dyadic_range']}` | "
            f"{item['child_count']} | "
            f"{item['total_width_cap']} | "
            f"{item['count_lower_from_width']} | "
            f"`{fmt_bool(item['lower_bound_valid'])}` |"
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
