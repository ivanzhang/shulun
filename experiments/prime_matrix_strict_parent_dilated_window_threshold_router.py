#!/usr/bin/env python3
"""生成 strict 父扩张窗口冷核心阈值表攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_parent_dilated_window_threshold_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-parent-dilated-window-threshold-router.json

输出：
  docs/monograph/prime-matrix-strict-parent-dilated-window-threshold-router.json
  docs/monograph/prime-matrix-strict-parent-dilated-window-threshold-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-parent-dilated-window-threshold-router.json"
OUT_MD = DOCS / "prime-matrix-strict-parent-dilated-window-threshold-router.md"

PARENT_DILATED_TABLE = "ParentSiblingDilatedWindowColdCoreThresholdTable"
COLLAR_BURST = "SiblingCollarShortDivisorBurstLCMOrPDECRoute"
COLLAR_TABLE = "SameParameterSiblingCollarShortDivisorCapTable"
PARENT_HOT_RETURN = "ParentSiblingDilatedWindowHotCorePDECorSAEExclusion"
COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
SHORT_LCM = "ShortWindowDivisorDensityLCMMultiplierDiscipline"
LOW_KERNEL = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
SIBLING_OVERLAP = "SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-parent-support-numeric-envelope-router.json",
    "prime-matrix-strict-sibling-numeric-envelope-attack-router.json",
    "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
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
        "experiments/prime_matrix_strict_parent_dilated_window_threshold_router.py": sha256(
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


def divisors(n: int) -> list[int]:
    """列出正因子，用于有限模型核验。"""
    out: list[int] = []
    root = math.isqrt(n)
    for d in range(1, root + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def count_in_interval(values: list[int], left: int, right: int) -> int:
    """计数闭区间内的元素。"""
    return sum(1 for value in values if left <= value <= right)


def threshold_sample(h: int, base_left: int, base_right: int, dil_left: int, dil_right: int) -> dict[str, Any]:
    """核验扩张窗口分解。"""
    ds = divisors(h)
    base_count = count_in_interval(ds, base_left, base_right)
    left_collar_count = count_in_interval(ds, dil_left, base_left - 1)
    right_collar_count = count_in_interval(ds, base_right + 1, dil_right)
    dilated_count = count_in_interval(ds, dil_left, dil_right)
    decomposition_count = base_count + left_collar_count + right_collar_count
    return {
        "H": h,
        "base_window": [base_left, base_right],
        "dilated_window": [dil_left, dil_right],
        "base_count": base_count,
        "left_collar_count": left_collar_count,
        "right_collar_count": right_collar_count,
        "dilated_count": dilated_count,
        "decomposition_count": decomposition_count,
        "identity_holds": dilated_count == decomposition_count,
        "collar_total": left_collar_count + right_collar_count,
    }


def sample_rows() -> list[dict[str, Any]]:
    """生成有限核验样本。"""
    return [
        threshold_sample(360, 20, 180, 18, 180),
        threshold_sample(840, 30, 240, 28, 245),
        threshold_sample(1260, 50, 420, 45, 423),
        threshold_sample(2520, 60, 720, 54, 721),
        threshold_sample(720720, 401, 4001, 390, 4012),
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


def formula_rows() -> list[dict[str, str]]:
    """列出扩张阈值表的合法公式。"""
    return [
        {
            "piece": "base cold count",
            "formula": "N_H([L,R])<=C_core^*(U;[L,R]) or hot return",
            "status": "imported conditional",
        },
        {
            "piece": "left collar",
            "formula": "N_H([L_*,L-1])<=C_col,left(U)",
            "status": "open numeric cap",
        },
        {
            "piece": "right collar",
            "formula": "N_H([R+1,R_*])<=C_col,right(U)",
            "status": "open numeric cap",
        },
        {
            "piece": "dilated table",
            "formula": "C_dil(U)=C_core^*(U;[L,R])+C_col,left(U)+C_col,right(U)",
            "status": "schema closed, numeric caps open",
        },
        {
            "piece": "collar burst",
            "formula": "if a collar cap fails, short-window divisor density triggers LCM/common-kernel/PDEC",
            "status": "registered route open",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "ParentDilatedTableTargetImported",
            result["parent_dilated_table_target_imported"],
            result["parent_dilated_table_target_imported"],
            "上一层已把父支撑数值界压成扩张父窗口冷核心表。",
            PARENT_DILATED_TABLE,
        ),
        row(
            "DilatedWindowThreePieceDecompositionProved",
            True,
            True,
            "扩张窗口计数精确分解为原父窗口加左右 collar。",
            PARENT_DILATED_TABLE,
        ),
        row(
            "FreeCollarAbsorptionRejected",
            True,
            True,
            "collar 不能免费并入旧 C_core；必须有同参数 collar cap 或命名回流。",
            COLLAR_TABLE,
        ),
        row(
            "DilatedThresholdSchemaClosed",
            True,
            False,
            "合法阈值表形态为 C_base+C_left+C_right。",
            f"{COLLAR_TABLE} AND {COLD_CORE_TABLE}",
        ),
        row(
            "CollarBurstRouteRegistered",
            result["short_window_lcm_discipline_imported"],
            False,
            "collar 短窗口高密度可接入 LCM 乘子纪律/共同核/PDEC 路由。",
            COLLAR_BURST,
        ),
        row(
            "SameParameterCollarCapTableProved",
            False,
            False,
            "尚未给出左右 collar 在同一参数账本下的可求和数值上界。",
            COLLAR_TABLE,
        ),
        row(
            "ParentDilatedWindowHotReturnExcluded",
            False,
            False,
            "若原父窗口或 collar 爆发为热窗口，仍需排斥热核心回流。",
            PARENT_HOT_RETURN,
        ),
        row(
            "ParentSiblingDilatedWindowColdCoreThresholdTableProved",
            False,
            False,
            "表结构已闭合，但 collar cap 和热回流排斥尚未完成。",
            f"{COLLAR_TABLE} AND {COLLAR_BURST} AND {PARENT_HOT_RETURN}",
        ),
        row(
            "SiblingColdCoreThresholdNumericEnvelopeProved",
            False,
            False,
            "扩张父窗口表、overlap 和 PDEC 阈值仍未全部闭合。",
            f"{PARENT_DILATED_TABLE} AND {SIBLING_OVERLAP} AND {PDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{COLLAR_TABLE} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造父扩张窗口冷核心阈值表攻坚证书。"""
    previous = load_json("prime-matrix-strict-parent-support-numeric-envelope-router.json")
    short_lcm = load_json("prime-matrix-strict-short-window-divisor-density-lcm-router.json")
    rows = sample_rows()
    identity_all = all(item["identity_holds"] for item in rows)
    short_lcm_imported = (
        short_lcm.get("incremental_multiplier_discipline_closed") is True
        and short_lcm.get("low_multiplier_kernel_forcing_closed") is True
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_parent_dilated_window_threshold_router",
        "status": "parent_dilated_threshold_schema_closed_collar_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "parent_dilated_table_target_imported": previous.get("next_direct_attack_target") == PARENT_DILATED_TABLE,
        "dilated_window_three_piece_decomposition_proved": True,
        "finite_decomposition_all_passed": identity_all,
        "free_collar_absorption_rejected": True,
        "dilated_threshold_schema_closed": True,
        "short_window_lcm_discipline_imported": short_lcm_imported,
        "collar_burst_route_registered": short_lcm_imported,
        "same_parameter_collar_short_divisor_cap_table_proved": False,
        "parent_dilated_window_hot_return_excluded": False,
        "parent_sibling_dilated_window_cold_core_threshold_table_proved": False,
        "parent_scaled_child_union_support_numeric_envelope_proved": False,
        "sibling_cold_core_threshold_numeric_envelope_proved": False,
        "terminal_cold_window_anticascade_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": PARENT_DILATED_TABLE,
        "hardpoint_after_router": (
            f"{COLLAR_TABLE} AND {COLLAR_BURST} AND {PARENT_HOT_RETURN} "
            f"AND {SIBLING_OVERLAP} AND {PDEC_TABLE}"
        ),
        "next_direct_attack_target": COLLAR_TABLE,
        "parallel_attack_targets": [
            COLLAR_BURST,
            PARENT_HOT_RETURN,
            SHORT_LCM,
            LOW_KERNEL,
            FIXED_HISTORY,
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
            "`ParentSiblingDilatedWindowColdCoreThresholdTable` 不能通过把扩张 collar "
            "免费塞进旧 `C_core^*` 来关闭。合法分解是："
            "`N_H([L_*,R_*]) = N_H([L,R]) + N_H([L_*,L-1]) + N_H([R+1,R_*])`。"
            "因此扩张阈值表的唯一合法形态是 `C_base + C_left_collar + C_right_collar`，"
            "三项必须使用同一参数账本。若 collar 短区间除数数超过其 cap，"
            "该爆发不是冷容量，而必须进入短窗口 LCM 乘子纪律、低乘子共同核、固定历史/PDEC/SAE 或热核心回流。"
            "本步关闭表结构与免费吸收禁令；尚未给出 collar cap 数值表，也未排斥热回流，"
            "所以行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 父扩张窗口冷核心阈值表路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"parent_dilated_table_target_imported={fmt_bool(result['parent_dilated_table_target_imported'])}",
        f"dilated_window_three_piece_decomposition_proved={fmt_bool(result['dilated_window_three_piece_decomposition_proved'])}",
        f"free_collar_absorption_rejected={fmt_bool(result['free_collar_absorption_rejected'])}",
        f"dilated_threshold_schema_closed={fmt_bool(result['dilated_threshold_schema_closed'])}",
        f"same_parameter_collar_short_divisor_cap_table_proved={fmt_bool(result['same_parameter_collar_short_divisor_cap_table_proved'])}",
        f"parent_dilated_window_hot_return_excluded={fmt_bool(result['parent_dilated_window_hot_return_excluded'])}",
        f"parent_sibling_dilated_window_cold_core_threshold_table_proved={fmt_bool(result['parent_sibling_dilated_window_cold_core_threshold_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 合法阈值表",
        "",
        "| piece | formula | status |",
        "|---|---|---|",
    ]
    for item in result["formula_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['piece'])}` | "
            f"`{table_cell(item['formula'])}` | "
            f"`{table_cell(item['status'])}` |"
        )

    lines.extend(
        [
            "",
            "## 有限分解核验",
            "",
            "| H | base window | dilated window | base | left collar | right collar | dilated | identity |",
            "|---:|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["finite_sample_rows"]:
        lines.append(
            "| "
            f"{item['H']} | "
            f"`{item['base_window']}` | "
            f"`{item['dilated_window']}` | "
            f"{item['base_count']} | "
            f"{item['left_collar_count']} | "
            f"{item['right_collar_count']} | "
            f"{item['dilated_count']} | "
            f"`{fmt_bool(item['identity_holds'])}` |"
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
