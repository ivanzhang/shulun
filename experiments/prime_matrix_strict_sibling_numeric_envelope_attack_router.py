#!/usr/bin/env python3
"""生成 strict 兄弟冷核心数值 envelope 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_sibling_numeric_envelope_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sibling-numeric-envelope-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-sibling-numeric-envelope-attack-router.json
  docs/monograph/prime-matrix-strict-sibling-numeric-envelope-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-sibling-numeric-envelope-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-sibling-numeric-envelope-attack-router.md"

SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
PARENT_SUPPORT = "ParentScaledChildUnionSupportNumericEnvelope"
OVERLAP_RETURN = "SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion"
COLLAR_ENVELOPE = "SiblingScaledWindowCollarNumericEnvelope"
COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-cold-window-sibling-charging-router.json",
    "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json",
    "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
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
        "experiments/prime_matrix_strict_sibling_numeric_envelope_attack_router.py": sha256(
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


def child_window(parent_left: int, parent_right: int, g: int) -> tuple[int, int]:
    """按外向缩放生成子窗口端点。"""
    return parent_left // g, math.ceil(parent_right / g)


def audit_family(parent_h: int, parent_left: int, parent_right: int, children: list[int]) -> dict[str, Any]:
    """核验兄弟总收费到父支撑加重叠债的恒等式。"""
    projected: list[int] = []
    child_rows: list[dict[str, Any]] = []
    for g in children:
        if parent_h % g != 0:
            child_rows.append(
                {
                    "g": g,
                    "compatible": False,
                    "child_window": None,
                    "child_core_count": 0,
                    "projected_count": 0,
                }
            )
            continue
        left, right = child_window(parent_left, parent_right, g)
        cores = [k for k in divisors(parent_h // g) if left <= k <= right]
        images = [g * k for k in cores]
        projected.extend(images)
        child_rows.append(
            {
                "g": g,
                "compatible": True,
                "child_window": [left, right],
                "child_core_count": len(cores),
                "projected_count": len(images),
            }
        )

    multiplicities: dict[int, int] = {}
    for d in projected:
        multiplicities[d] = multiplicities.get(d, 0) + 1

    total_charge = len(projected)
    support_count = len(multiplicities)
    overlap_excess = sum(max(0, count - 1) for count in multiplicities.values())
    collar_support = sum(1 for d in multiplicities if d < parent_left or d > parent_right)

    return {
        "parent_h": parent_h,
        "parent_window": [parent_left, parent_right],
        "children": children,
        "compatible_children": sum(1 for row in child_rows if row["compatible"]),
        "child_rows": child_rows,
        "total_child_charge": total_charge,
        "parent_projected_support": support_count,
        "overlap_excess": overlap_excess,
        "collar_support_outside_parent_window": collar_support,
        "identity_holds": total_charge == support_count + overlap_excess,
    }


def model_rows() -> list[dict[str, Any]]:
    """生成有限模型行，说明精确恒等式不是经验假设。"""
    return [
        audit_family(360, 20, 180, [2, 3, 5, 6]),
        audit_family(840, 30, 240, [2, 3, 4, 5, 7]),
        audit_family(1260, 50, 420, [3, 4, 5, 6, 7, 9]),
        audit_family(2520, 60, 720, [4, 5, 6, 7, 8, 9, 10]),
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


def decomposition_rows() -> list[dict[str, str]]:
    """列出兄弟 envelope 的精确拆分。"""
    return [
        {
            "piece": "child multiset",
            "formula": "F_U={(g,k): g in G_U, k|H_U/g, k in I_{U,g}}",
            "meaning": "所有兄弟冷窗口原始收费对象。",
        },
        {
            "piece": "parent projection",
            "formula": "pi(g,k)=gk, so pi(F_U) subset {d:d|H_U}",
            "meaning": "把子核心推回父频率除数支撑。",
        },
        {
            "piece": "exact identity",
            "formula": "|F_U|=|pi(F_U)|+sum_d(max(mu_U(d)-1,0))",
            "meaning": "兄弟总收费等于父支撑数加重复收费债。",
        },
        {
            "piece": "support budget",
            "formula": "C_sib,supp(U)=|pi(F_U)|",
            "meaning": "可留在冷供给中的整族支撑项。",
        },
        {
            "piece": "overlap return",
            "formula": "E_overlap(U)=sum_d(max(mu_U(d)-1,0))",
            "meaning": "同一父除数被多个孩子重复收费时必须回流固定历史或 ColumnCRT。",
        },
        {
            "piece": "collar discipline",
            "formula": "pi(F_U) uses union_g g I_{U,g}, not a naive single parent interval",
            "meaning": "外向取整产生的边界 collar 必须被数值 envelope 覆盖或命名回流。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "SiblingChargingLedgerImported",
            result["sibling_charging_ledger_imported"],
            result["sibling_charging_ledger_imported"],
            "上一层已关闭兄弟收费/热回流账本规则。",
            SIBLING_NUMERIC,
        ),
        row(
            "MultisetProjectionIdentityProved",
            True,
            True,
            "同父前缀兄弟收费可精确分解为父支撑计数和重叠债。",
            PARENT_SUPPORT,
        ),
        row(
            "FreeConstantCsibRejected",
            True,
            True,
            "C_sib(U) 不能作为固定常数猜测；必须由同参数父支撑表生成。",
            PARENT_SUPPORT,
        ),
        row(
            "ExactCsibSupportDefinitionClosed",
            True,
            True,
            "可留在冷供给的 C_sib,supp(U) 定义为 projected support 的实际大小。",
            PARENT_SUPPORT,
        ),
        row(
            "OverlapDebtRegisteredButNotExcluded",
            result["overlap_return_registered"],
            False,
            "重复收费已可命名为固定历史/ColumnCRT 债，但尚未全局排斥。",
            OVERLAP_RETURN,
        ),
        row(
            "BoundaryCollarNumericEnvelopeProved",
            False,
            False,
            "外向缩放后的 union_g gI_{U,g} 需要同参数 collar 数值界。",
            COLLAR_ENVELOPE,
        ),
        row(
            "ParentSupportNumericEnvelopeProved",
            False,
            False,
            "尚未证明 projected support 在父级 union/collar 中满足可求和数值上界。",
            f"{PARENT_SUPPORT} AND {COLD_CORE_TABLE}",
        ),
        row(
            "SiblingColdCoreThresholdNumericEnvelopeProved",
            False,
            False,
            "结构恒等式已闭合，但父支撑、collar 和 overlap 三项尚未全部关闭。",
            f"{PARENT_SUPPORT} AND {OVERLAP_RETURN} AND {COLLAR_ENVELOPE}",
        ),
        row(
            "TerminalColdWindowAntiCascadeProved",
            False,
            False,
            "兄弟数值 envelope 仍未完成，反级联不能升级为定理。",
            f"{SIBLING_NUMERIC} AND {HOT_CORE} AND {FIXED_HISTORY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{PARENT_SUPPORT} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造兄弟数值 envelope 攻坚证书。"""
    sibling = load_json("prime-matrix-strict-cold-window-sibling-charging-router.json")
    rows = model_rows()
    identity_all = all(item["identity_holds"] for item in rows)
    sibling_imported = sibling.get("canonical_cold_window_sibling_charging_ledger_closed") is True

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_sibling_numeric_envelope_attack_router",
        "status": "sibling_numeric_envelope_reduced_to_support_overlap_and_collar_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "sibling_charging_ledger_imported": sibling_imported,
        "sibling_multiset_projection_identity_proved": True,
        "finite_model_identity_all_passed": identity_all,
        "free_constant_c_sib_rejected": True,
        "exact_c_sib_support_definition_closed": True,
        "overlap_return_registered": sibling.get("overlap_return_registered") is True,
        "parent_scaled_child_union_support_numeric_envelope_proved": False,
        "sibling_overlap_multiplicity_return_excluded": False,
        "sibling_scaled_window_collar_numeric_envelope_proved": False,
        "sibling_cold_core_threshold_numeric_envelope_proved": False,
        "terminal_cold_window_anticascade_proved": False,
        "effective_cold_history_pruning_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SIBLING_NUMERIC,
        "hardpoint_after_router": (
            f"{PARENT_SUPPORT} AND {OVERLAP_RETURN} AND {COLLAR_ENVELOPE} "
            f"AND {COLD_CORE_TABLE} AND {PDEC_TABLE}"
        ),
        "next_direct_attack_target": PARENT_SUPPORT,
        "parallel_attack_targets": [
            OVERLAP_RETURN,
            COLLAR_ENVELOPE,
            COLD_CORE_TABLE,
            PDEC_TABLE,
            HOT_CORE,
            FIXED_HISTORY,
            TERMINAL_ANTICASCADE,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "decomposition_rows": decomposition_rows(),
        "finite_model_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SiblingColdCoreThresholdNumericEnvelopeTable` 已被进一步下钻。"
            "同一父前缀 `U` 的兄弟冷收费不能靠独立常数 `C_sib(U)` 猜测闭合；"
            "它有精确投影恒等式：所有子收费对象 `(g,k)` 经 `d=gk` 投到父频率除数支撑，"
            "于是兄弟总收费等于父投影支撑大小加同一父除数的重复收费债。"
            "因此可留在冷供给里的 sibling envelope 只能是父级 scaled-child union support，"
            "重复收费必须登记为固定历史或 ColumnCRT 回流，外向缩放产生的边界 collar 也必须进入同参数数值界。"
            "本步关闭的是结构恒等式和 `C_sib` 的合法定义，尚未证明父支撑数值上界、overlap 排斥或 collar 上界；"
            "行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 兄弟冷核心数值 envelope 攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sibling_charging_ledger_imported={fmt_bool(result['sibling_charging_ledger_imported'])}",
        f"sibling_multiset_projection_identity_proved={fmt_bool(result['sibling_multiset_projection_identity_proved'])}",
        f"free_constant_c_sib_rejected={fmt_bool(result['free_constant_c_sib_rejected'])}",
        f"exact_c_sib_support_definition_closed={fmt_bool(result['exact_c_sib_support_definition_closed'])}",
        f"parent_scaled_child_union_support_numeric_envelope_proved={fmt_bool(result['parent_scaled_child_union_support_numeric_envelope_proved'])}",
        f"sibling_overlap_multiplicity_return_excluded={fmt_bool(result['sibling_overlap_multiplicity_return_excluded'])}",
        f"sibling_scaled_window_collar_numeric_envelope_proved={fmt_bool(result['sibling_scaled_window_collar_numeric_envelope_proved'])}",
        f"sibling_cold_core_threshold_numeric_envelope_proved={fmt_bool(result['sibling_cold_core_threshold_numeric_envelope_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 精确拆分",
        "",
        "| piece | formula | meaning |",
        "|---|---|---|",
    ]
    for item in result["decomposition_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['piece'])}` | "
            f"`{table_cell(item['formula'])}` | "
            f"{table_cell(item['meaning'])} |"
        )

    lines.extend(
        [
            "",
            "## 有限模型核验",
            "",
            "| H_U | parent window | children | child charge | projected support | overlap excess | collar support | identity |",
            "|---:|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["finite_model_rows"]:
        lines.append(
            "| "
            f"{item['parent_h']} | "
            f"`{item['parent_window']}` | "
            f"`{item['children']}` | "
            f"{item['total_child_charge']} | "
            f"{item['parent_projected_support']} | "
            f"{item['overlap_excess']} | "
            f"{item['collar_support_outside_parent_window']} | "
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
