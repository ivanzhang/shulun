#!/usr/bin/env python3
"""生成 strict 除数兼容冷历史树打包界攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_divisor_compatible_tree_packing_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json
  docs/monograph/prime-matrix-strict-divisor-compatible-tree-packing-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-effective-cold-history-pruning-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    "prime-matrix-strict-fixed-quotient-type-columncrt-router.json",
    "prime-matrix-strict-short-window-divisor-density-lcm-router.json",
]

TREE_PACKING = "DivisorCompatibleColdHistoryTreePackingBound"
PREFIX_BRANCHING = "ColdHistoryPrefixBranchingHotOrFixedReturnLemma"
PRIME_POWER = "PrimePowerCascadeColdWindowExclusionOrCapacityTable"
COLD_WINDOW = "TerminalColdWindowCompatibilityAntiCascadeLemma"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
LCM_KERNEL = "DenseLCMOrLowMultiplierCommonKernelReturn"
CORE_CAP_TABLE = "ColdCoreThresholdFunctionNumericTable"
PERSISTENCE_TABLE = "SameParameterPDECThresholdNumericTable"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
LOG2_PHI = math.log((1 + math.sqrt(5)) / 2, 2)


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
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
        "experiments/prime_matrix_strict_divisor_compatible_tree_packing_attack_router.py": sha256(
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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def obstruction_rows() -> list[dict[str, Any]]:
    """给出仅靠除数兼容时的阻塞模型。"""
    return [
        {
            "model": "all powers of 2 as grouped factors",
            "history_count_lower_shape": "2^(a-1) for h_0=2^a",
            "p_exponent_if_2a_about_p": 1.0,
            "demand_exponent_alpha": ALPHA,
            "beats_alpha_043": True,
            "meaning": "若冷条件不进一步剪枝，仅靠 D(W)|h_0 无法阻止有序分组爆炸。",
        },
        {
            "model": "factors restricted to 2 and 4",
            "history_count_lower_shape": "Fibonacci(a)",
            "p_exponent_if_2a_about_p": LOG2_PHI,
            "demand_exponent_alpha": ALPHA,
            "beats_alpha_043": LOG2_PHI > ALPHA,
            "meaning": "即使只允许两种小乘子，增长阶约 P^0.694，也大于需求阶 P^0.43。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成除数兼容树打包判定表。"""
    pruning = data["pruning"]
    scaled = data["scaled"]
    fixed_type = data["fixed_type"]
    lcm = data["lcm"]

    target_imported = pruning.get("next_direct_attack_target") == TREE_PACKING
    divisor_interface = pruning.get("divisor_compatibility_interface_closed") is True
    cold_hot = scaled.get("cold_hot_split_closed") is True
    fixed_route = fixed_type.get("fixed_type_pdec_route_registered") is True
    lcm_route = (
        lcm.get("lcm_anchor_closed") is True
        and lcm.get("low_multiplier_kernel_forcing_closed") is True
    )

    return [
        row(
            "TreePackingTargetImported",
            target_imported,
            False,
            "上一层已把有效剪枝压成除数兼容冷历史树打包界。",
            TREE_PACKING,
        ),
        row(
            "DivisorCompatibilityInterfaceImported",
            divisor_interface,
            True,
            "D(W)|h_0 与 H_W=h_0/D(W) 的接口已闭合。",
            TREE_PACKING,
        ),
        row(
            "DivisorCompatibilityAloneRejected",
            True,
            True,
            "素数幂频率模型显示仅靠 D(W)|h_0 仍可产生过大的有序历史树。",
            PREFIX_BRANCHING,
        ),
        row(
            "ColdWindowConstraintMustBeUsed",
            cold_hot,
            False,
            "必须利用冷窗口 N_{H_W}(I_W)<=C_core(W)；否则无法剪掉素数幂级联。",
            COLD_WINDOW,
        ),
        row(
            "PrefixBranchingReturnRoutesRegistered",
            fixed_route and lcm_route,
            False,
            "过多同前缀分叉若不是冷兼容，必须回流热核心、固定历史或 LCM 共同核。",
            PREFIX_BRANCHING,
        ),
        row(
            "PrimePowerCascadeCaseClosed",
            False,
            False,
            "尚未排斥最危险的小乘子/素数幂级联冷窗口。",
            PRIME_POWER,
        ),
        row(
            "DivisorCompatibleColdHistoryTreePackingBoundProved",
            False,
            False,
            "树打包界必须同时使用冷窗口反级联和前缀分叉回流；当前未证明。",
            f"{PREFIX_BRANCHING} AND {PRIME_POWER} AND {COLD_WINDOW}",
        ),
        row(
            "ColdSupplyNumericEnvelopeProved",
            False,
            False,
            "树打包界之外，仍需 C_core 与 T_PDEC 同参数数值表。",
            f"{TREE_PACKING} AND {CORE_CAP_TABLE} AND {PERSISTENCE_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{PREFIX_BRANCHING} AND {HOT_CORE} AND {FIXED_HISTORY} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造除数兼容树打包攻坚证书。"""
    data = {
        "pruning": load_json("prime-matrix-strict-effective-cold-history-pruning-router.json"),
        "scaled": load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"),
        "fixed_type": load_json("prime-matrix-strict-fixed-quotient-type-columncrt-router.json"),
        "lcm": load_json("prime-matrix-strict-short-window-divisor-density-lcm-router.json"),
    }
    rows = build_rows(data)

    return {
        "certificate_type": "prime_matrix_strict_divisor_compatible_tree_packing_attack_router",
        "status": "divisor_compatible_tree_packing_requires_cold_window_prefix_branching_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "divisor_compatibility_interface_imported": True,
        "divisor_compatibility_alone_rejected_as_sufficient": True,
        "cold_window_constraint_needed": True,
        "prime_power_cascade_case_closed": False,
        "cold_history_prefix_branching_hot_or_fixed_return_proved": False,
        "divisor_compatible_cold_history_tree_packing_bound_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": TREE_PACKING,
        "hardpoint_after_router": f"{PREFIX_BRANCHING} AND {PRIME_POWER} AND {COLD_WINDOW}",
        "next_direct_attack_target": PREFIX_BRANCHING,
        "parallel_attack_targets": [
            PRIME_POWER,
            COLD_WINDOW,
            HOT_CORE,
            FIXED_HISTORY,
            LCM_KERNEL,
            CORE_CAP_TABLE,
            PERSISTENCE_TABLE,
            DSTRUCTURE,
        ],
        "obstruction_rows": obstruction_rows(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`DivisorCompatibleColdHistoryTreePackingBound` 不能只靠 `D(W)|h_0` 闭合。"
            "素数幂频率给出结构性阻塞：若 `h_0=2^a`，有序乘积分组本身就可产生约 `2^(a-1)` "
            "条形式历史；即使把因子限制为 2 和 4，数量也按 Fibonacci(a) 增长，约为 "
            "`P^0.694`，仍大于 `alpha=0.43` 的需求阶。"
            "因此树打包界必须使用冷窗口约束和前缀分叉回流：过多分叉必须触发热核心、固定历史或 LCM 共同核。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 除数兼容冷历史树打包界攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"divisor_compatibility_alone_rejected_as_sufficient={fmt_bool(result['divisor_compatibility_alone_rejected_as_sufficient'])}",
        f"prime_power_cascade_case_closed={fmt_bool(result['prime_power_cascade_case_closed'])}",
        f"cold_history_prefix_branching_hot_or_fixed_return_proved={fmt_bool(result['cold_history_prefix_branching_hot_or_fixed_return_proved'])}",
        f"divisor_compatible_cold_history_tree_packing_bound_proved={fmt_bool(result['divisor_compatible_cold_history_tree_packing_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 阻塞模型",
        "",
        "| model | history_count_lower_shape | p_exponent_if_2a_about_p | demand_exponent_alpha | beats_alpha_043 | meaning |",
        "|---|---|---:|---:|---:|---|",
    ]
    for item in result["obstruction_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['model'])}` | "
            f"`{table_cell(item['history_count_lower_shape'])}` | "
            f"{item['p_exponent_if_2a_about_p']:.6f} | "
            f"{item['demand_exponent_alpha']:.6f} | "
            f"`{fmt_bool(item['beats_alpha_043'])}` | "
            f"{table_cell(item['meaning'])} |"
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
    for item in result["rows"]:
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
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
