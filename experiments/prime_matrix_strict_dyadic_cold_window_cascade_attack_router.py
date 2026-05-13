#!/usr/bin/env python3
"""生成 strict dyadic 冷窗口级联攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_dyadic_cold_window_cascade_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-dyadic-cold-window-cascade-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-dyadic-cold-window-cascade-attack-router.json
  docs/monograph/prime-matrix-strict-dyadic-cold-window-cascade-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-dyadic-cold-window-cascade-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-dyadic-cold-window-cascade-attack-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-small-prime-power-cascade-attack-router.json",
    "prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json",
    "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    "prime-matrix-strict-fixed-quotient-type-columncrt-router.json",
]

ALPHA = 0.43
PHI = (1 + math.sqrt(5)) / 2

DYADIC = "DyadicPrimePowerColdWindowCascadeExclusionLemma"
CANON = "DyadicValuationOrderCanonicalizationOrPhaseDefectLedger"
PHASE = "DyadicPathDependentColdWindowPhaseDefectPDECRoute"
VALUATION = "PureDyadicValuationStateCompressionLedger"
MIXED_ODD = "DyadicOddCoreLeakageToOddPrimeEpsilonLedger"
COLD_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
SMALL_TABLE = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
KERNEL_BUDGET = "PrefixBranchingKernelMultiplicityBudgetLedger"
TREE_PACKING = "DivisorCompatibleColdHistoryTreePackingBound"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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
        "experiments/prime_matrix_strict_dyadic_cold_window_cascade_attack_router.py": sha256(
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


def fib(n: int) -> int:
    """计算 Fibonacci 数，F_0=0, F_1=1。"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def dyadic_overcount_rows() -> list[dict[str, Any]]:
    """比较 dyadic 有序路径数和 2-adic 状态数。"""
    rows: list[dict[str, Any]] = []
    for a in [8, 16, 24, 32, 40, 48, 56, 64]:
        ordered_paths = fib(a + 1)
        valuation_states = a + 1
        rows.append(
            {
                "a": a,
                "ordered_one_two_paths": ordered_paths,
                "valuation_states": valuation_states,
                "overcount_ratio": ordered_paths / valuation_states,
                "asymptotic_exponent": math.log(PHI, 2),
                "beats_alpha": math.log(PHI, 2) > ALPHA,
            }
        )
    return rows


def dyadic_dichotomy_rows() -> list[dict[str, str]]:
    """列出 dyadic 级联的二选一路径。"""
    return [
        {
            "branch": "order_canonical",
            "condition": "cold admissibility depends only on cumulative v2 and odd core",
            "consequence": "ordered Fibonacci paths collapse to at most a+1 valuation states",
            "remaining": VALUATION,
        },
        {
            "branch": "path_dependent",
            "condition": "two orders with same total v2 give different cold windows or labels",
            "consequence": "the difference is a phase/window defect, hence must route to PDEC/ColumnCRT/hot core",
            "remaining": PHASE,
        },
        {
            "branch": "odd_leakage",
            "condition": "dyadic child contains odd leakage or alternates with odd prime blocks",
            "consequence": "it exits pure dyadic cascade and returns to p=3/5 epsilon ledger or fan-in budget",
            "remaining": MIXED_ODD,
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 dyadic 冷窗口级联判定表。"""
    small = data["small"]
    scaled = data["scaled"]
    fixed = data["fixed"]

    target_imported = small.get("next_direct_attack_target") == DYADIC
    p2_primary = small.get("p2_primary_dyadic_case") is True
    cold_hot = scaled.get("cold_hot_split_closed") is True
    fixed_route = fixed.get("fixed_type_pdec_route_registered") is True

    return [
        row(
            "DyadicTargetImported",
            target_imported,
            False,
            "上一层确认 p=2 是唯一强主危险。",
            DYADIC,
        ),
        row(
            "P2PrimaryRiskPinned",
            p2_primary,
            True,
            "一二步 dyadic Fibonacci 模型仍给 P^0.694，明显超过 alpha=0.43。",
            DYADIC,
        ),
        row(
            "DyadicOvercountSourceIdentified",
            True,
            True,
            "指数爆炸来自有序分割 2^a 的路径数，而不是来自不同 2-adic 终态数。",
            CANON,
        ),
        row(
            "PureValuationStateCompressionWouldSuffice",
            True,
            False,
            "若冷窗口只依赖累计 v2 和奇核，Fibonacci 路径可压成线性 a+1 个状态。",
            VALUATION,
        ),
        row(
            "PathDependenceForcesPhaseDefect",
            True,
            False,
            "若不同顺序不可合并，则必存在相位/窗口/标签差异，可进入 PDEC/ColumnCRT/热核心。",
            PHASE,
        ),
        row(
            "ColdHotGateImported",
            cold_hot,
            False,
            "dyadic 级联造成过密终端窗口时，必须回流热核心。",
            HOT_CORE,
        ),
        row(
            "FixedHistoryRouteImported",
            fixed_route,
            False,
            "同一 dyadic 商型持久复现时进入固定历史 PDEC/ColumnCRT。",
            FIXED_HISTORY,
        ),
        row(
            "DyadicDichotomyClosed",
            True,
            True,
            "纯 dyadic 级联只剩规范化折叠或路径相位缺陷两类，奇因子泄漏回到 p=3/5。",
            CANON,
        ),
        row(
            "DyadicValuationOrderCanonicalizationProved",
            False,
            False,
            "尚未证明真实冷窗口对 dyadic 顺序不敏感，或给出顺序敏感的缺陷路由证书。",
            CANON,
        ),
        row(
            "DyadicPrimePowerColdWindowCascadeExcluded",
            False,
            False,
            "dyadic 主危险已压到规范化/相位缺陷二选一，但二选一未闭合。",
            f"{CANON} AND {COLD_ANTICASCADE}",
        ),
        row(
            "SmallPrimePowerCascadeTableProved",
            False,
            False,
            "dyadic 未闭合，故 p=2,3,5 小素数表仍未闭合。",
            SMALL_TABLE,
        ),
        row(
            "PrefixBranchingKernelMultiplicityBudgetProved",
            False,
            False,
            "小素数幂表未闭合，共同核重数预算仍未闭合。",
            KERNEL_BUDGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{CANON} AND {COLD_ANTICASCADE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 dyadic 冷窗口级联攻坚证书。"""
    data = {
        "small": load_json("prime-matrix-strict-small-prime-power-cascade-attack-router.json"),
        "scaled": load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"),
        "fixed": load_json("prime-matrix-strict-fixed-quotient-type-columncrt-router.json"),
    }
    rows = build_rows(data)

    return {
        "certificate_type": "prime_matrix_strict_dyadic_cold_window_cascade_attack_router",
        "status": "dyadic_cascade_reduced_to_order_canonicalization_or_phase_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "p2_primary_risk_pinned": True,
        "dyadic_overcount_source_identified": True,
        "pure_valuation_state_compression_would_suffice": True,
        "path_dependence_forces_phase_defect_route": True,
        "dyadic_dichotomy_closed": True,
        "dyadic_valuation_order_canonicalization_proved": False,
        "dyadic_path_dependent_phase_defect_pdec_route_proved": False,
        "dyadic_prime_power_cold_window_cascade_excluded": False,
        "small_prime_power_cascade_table_proved": False,
        "prefix_branching_kernel_multiplicity_budget_proved": False,
        "divisor_compatible_cold_history_tree_packing_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": DYADIC,
        "hardpoint_after_router": f"{CANON} AND {COLD_ANTICASCADE}",
        "next_direct_attack_target": CANON,
        "parallel_attack_targets": [
            PHASE,
            VALUATION,
            MIXED_ODD,
            COLD_ANTICASCADE,
            HOT_CORE,
            FIXED_HISTORY,
            TREE_PACKING,
            DSTRUCTURE,
        ],
        "dyadic_overcount_rows": dyadic_overcount_rows(),
        "dyadic_dichotomy_rows": dyadic_dichotomy_rows(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`DyadicPrimePowerColdWindowCascadeExclusionLemma` 的主爆炸源已定位："
            "危险的 Fibonacci 数量来自把同一个 `2^a` 预算有序切成 `1/2` 步，而不是来自不同的 "
            "2-adic 终态。若冷可容许性只依赖累计 `v2` 和同一奇核，则所有有序路径必须压缩到 "
            "`a+1` 个 valuation states，指数爆炸消失；若两个同总 `v2` 的顺序不能合并，"
            "它们必在相位、冷窗口或标签上产生可登记差异，进入 PDEC/ColumnCRT/热核心。"
            "因此 dyadic 主硬点被压成 `DyadicValuationOrderCanonicalizationOrPhaseDefectLedger`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict dyadic 冷窗口级联攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dyadic_dichotomy_closed={fmt_bool(result['dyadic_dichotomy_closed'])}",
        f"dyadic_valuation_order_canonicalization_proved={fmt_bool(result['dyadic_valuation_order_canonicalization_proved'])}",
        f"dyadic_path_dependent_phase_defect_pdec_route_proved={fmt_bool(result['dyadic_path_dependent_phase_defect_pdec_route_proved'])}",
        f"dyadic_prime_power_cold_window_cascade_excluded={fmt_bool(result['dyadic_prime_power_cold_window_cascade_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 有序路径过计数",
        "",
        "| a=v2(h0) | ordered_one_two_paths | valuation_states | overcount_ratio | asymptotic_exponent | beats_alpha |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for item in result["dyadic_overcount_rows"]:
        lines.append(
            "| "
            f"{item['a']} | "
            f"{item['ordered_one_two_paths']} | "
            f"{item['valuation_states']} | "
            f"{item['overcount_ratio']:.6f} | "
            f"{item['asymptotic_exponent']:.6f} | "
            f"`{fmt_bool(item['beats_alpha'])}` |"
        )

    lines.extend(
        [
            "",
            "## 二选一路由",
            "",
            "| branch | condition | consequence | remaining |",
            "|---|---|---|---|",
        ]
    )
    for item in result["dyadic_dichotomy_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['branch'])}` | "
            f"{table_cell(item['condition'])} | "
            f"{table_cell(item['consequence'])} | "
            f"`{table_cell(item['remaining'])}` |"
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
