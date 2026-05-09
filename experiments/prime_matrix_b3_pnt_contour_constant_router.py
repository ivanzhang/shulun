#!/usr/bin/env python3
"""Prime Matrix B=3 零点自由区到 PNT 轮廓常数路由器。

用法示例：
  python3 experiments/prime_matrix_b3_pnt_contour_constant_router.py

输出：
  docs/monograph/prime-matrix-b3-pnt-contour-constant-router.json
  docs/monograph/prime-matrix-b3-pnt-contour-constant-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zero-repulsion-parameter-optimization-router.json"
DEFAULT_EXPLICIT_FORMULA = ROOT / "docs" / "rh-pc1-analytic-input-theoremization.md"
DEFAULT_FINAL_DRAFT = ROOT / "docs" / "final-proof-draft.md"
DEFAULT_JSON = DOCS / "prime-matrix-b3-pnt-contour-constant-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-pnt-contour-constant-router.md"

OLD_ATOM = "ZeroFreeRegionToExplicitPNTContourConstantLedger"
SMOOTH_EF_ATOM = "SmoothChebyshevExplicitFormulaAppendixClosed"
UNSMOOTHED_PERRON_ATOM = "UnsmoothedChebyshevPerronExplicitFormulaConstantLedger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
TRIVIAL_TAIL_ATOM = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
CLOSED_REDUCTION_ATOM = "ZeroFreeRegionToExplicitPNTContourConstantReducedToPerronAndZeroSumLedgers"
THETA_TARGET_ATOM = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ZERO_REPULSION_C = 1280.0
ZERO_REPULSION_C_INV = 1.0 / ZERO_REPULSION_C
T0 = 14.0
ANCHOR_X = 20_000.0
TARGET_RELATIVE_ERROR = 1.0 / 36_260.0


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def replacement_pair() -> str:
    """写出 PNT 轮廓常数微账本替换包。"""
    return (
        f"({UNSMOOTHED_PERRON_ATOM} AND {ZERO_SUM_ATOM} "
        f"AND {TRIVIAL_TAIL_ATOM})"
    )


def replace_atom(text: str) -> str:
    """替换旧 PNT 轮廓常数原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def contour_pressure() -> dict[str, Any]:
    """给出 x=20000 目标对普通零点自由区 PNT 误差的压力诊断。"""
    log_x = math.log(ANCHOR_X)
    sqrt_log_x = math.sqrt(log_x)
    base_exponent = math.sqrt(ZERO_REPULSION_C_INV)
    conservative_exponent = base_exponent / 4.0
    diagnostic_factor = math.exp(-conservative_exponent * sqrt_log_x)
    log_needed_for_target_k1 = (
        math.log(1.0 / TARGET_RELATIVE_ERROR) / conservative_exponent
    ) ** 2
    return {
        "anchor_x": ANCHOR_X,
        "log_anchor_x": log_x,
        "sqrt_log_anchor_x": sqrt_log_x,
        "target_relative_error": TARGET_RELATIVE_ERROR,
        "zero_free_region_c": ZERO_REPULSION_C_INV,
        "base_exp_sqrt_c": base_exponent,
        "diagnostic_conservative_exponent": conservative_exponent,
        "diagnostic_factor_at_20000": diagnostic_factor,
        "log_x_needed_for_target_if_K1": log_needed_for_target_k1,
    }


def source_audit(explicit_formula_text: str, final_draft_text: str) -> dict[str, Any]:
    """审查当前材料能否直接给出非平滑 PNT 常数账本。"""
    smooth_explicit_formula = contains_all(
        explicit_formula_text,
        ["Ψ_W", "-ζ'(s)/ζ(s)", "非平凡零点", "素数幂"],
    )
    unsmoothed_perron_formula = contains_all(
        final_draft_text,
        ["psi(x)=x", "sum_{rho}", "Perron", "Chebyshev"],
    )
    theta_target_registered = contains_all(
        final_draft_text,
        ["vartheta(x)-x", "36260", "Dusart"],
    )
    explicit_contour_budget = contains_all(
        final_draft_text,
        ["ZeroFreeRegionToExplicitPNTContourConstantLedger", "zero sum", "truncation"],
    )
    return {
        "smooth_explicit_formula_available": smooth_explicit_formula,
        "unsmoothed_perron_formula_constantized": unsmoothed_perron_formula,
        "dusart_theta_target_registered": theta_target_registered,
        "explicit_zero_sum_truncation_budget_present": explicit_contour_budget,
    }


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 PNT 轮廓常数判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    zero_repulsion_ready = bool(
        previous.get("zero_repulsion_parameter_optimization_closed")
    )
    smooth_ready = bool(audit["smooth_explicit_formula_available"])
    unsmoothed_ready = bool(audit["unsmoothed_perron_formula_constantized"])
    zero_sum_budget_ready = bool(audit["explicit_zero_sum_truncation_budget_present"])
    reduced = active and guard and zero_repulsion_ready and smooth_ready
    closed = reduced and unsmoothed_ready and zero_sum_budget_ready
    return [
        row(
            "PNTContourGateActive",
            active,
            False,
            "上一层已把 C_log 与零点排斥参数闭合，当前最窄点转为 PNT 轮廓常数。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ZeroRepulsionC1280T14Ready",
            zero_repulsion_ready,
            True,
            "已取得高高度零点自由带 beta<=1-1/(1280 log(|gamma|+3)), |gamma|>=14。",
            "低高度仍由独立有限账本处理。",
        ),
        row(
            "SmoothExplicitFormulaAvailable",
            smooth_ready,
            True,
            "仓库已有平滑 Chebyshev 显式公式和素数幂低阶吸收接口。",
            SMOOTH_EF_ATOM,
        ),
        row(
            "UnsmoothedPerronConstantLedgerMissing",
            unsmoothed_ready,
            False,
            "还没有把非平滑 psi/theta 的 Perron 截断、端点误差和常数写成可复核账本。",
            UNSMOOTHED_PERRON_ATOM,
        ),
        row(
            "ZeroSumContourNumericalBudgetMissing",
            zero_sum_budget_ready,
            False,
            "还没有把 C=1280,T0=14 零点自由带代入零点和、截断高度、平凡零点尾项的数值预算。",
            ZERO_SUM_ATOM,
        ),
        row(
            "TrivialTailAndPrimePowerBudgetStillNeeded",
            False,
            False,
            "平凡零点、素数幂和截断尾必须与非平滑 Perron 同口径登记，不能由平滑公式自动替代。",
            TRIVIAL_TAIL_ATOM,
        ),
        row(
            "PNTContourConstantReducedToMicroLedgers",
            reduced,
            False,
            "旧 PNT 轮廓常数原子已压成非平滑 Perron 常数、零点和预算、平凡/截断尾预算三个微账本。",
            replacement_pair(),
        ),
        row(
            OLD_ATOM,
            closed,
            False,
            "只有三个微账本全部完成后，才能说零点自由区到显式 PNT 轮廓常数闭合。",
            CLOSED_REDUCTION_ATOM if closed else replacement_pair(),
        ),
        row(
            "ThetaTargetAt20000StillSeparate",
            False,
            False,
            "即使 PNT 轮廓常数完成，x=20000 的 1/36260 级目标仍需单独预算或外部 Dusart/有限桥。",
            THETA_TARGET_ATOM,
        ),
        row(
            "FiniteLowHeightStillSeparate",
            False,
            False,
            "T0 以下零点排除仍是独立有限证书，不能并入高高度轮廓预算。",
            FINITE_LOW_HEIGHT,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行零点自由区到 PNT 轮廓常数路由。"""
    previous = load_json(paths["previous"])
    explicit_formula_text = paths["explicit_formula"].read_text(encoding="utf-8")
    final_draft_text = paths["final_draft"].read_text(encoding="utf-8")
    audit = source_audit(explicit_formula_text, final_draft_text)
    rows = build_rows(previous, audit)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "PNTContourConstantReducedToMicroLedgers"
    )
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_pnt_contour_constant_router",
        "status": "pnt_contour_constant_reduced_to_microledgers_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "pnt_contour_constant_reduced": reduced,
        "pnt_contour_constant_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": UNSMOOTHED_PERRON_ATOM,
        "secondary_priority": ZERO_SUM_ATOM,
        "tertiary_priority": TRIVIAL_TAIL_ATOM,
        "post_contour_priority": THETA_TARGET_ATOM,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "source_audit": audit,
        "pressure": contour_pressure(),
        "plain_conclusion": (
            "PNT 轮廓常数层已被压到三个更窄微账本：非平滑 Chebyshev/Perron 常数账本、"
            "C=1280,T0=14 的零点和轮廓数值预算、以及平凡零点/素数幂/截断尾同口径预算。"
            "当前材料不能直接关闭该层，更不能自动推出 x=20000 的 1/36260 级 theta 目标。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    pressure = result["pressure"]
    lines = [
        "# Prime Matrix B=3 零点自由区到 PNT 轮廓常数路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"pnt_contour_constant_reduced={fmt_bool(result['pnt_contour_constant_reduced'])}",
        f"pnt_contour_constant_closed={fmt_bool(result['pnt_contour_constant_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 微账本替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 来源审查",
        "",
        "| item | value |",
        "| --- | --- |",
    ]
    for key, value in result["source_audit"].items():
        lines.append(f"| {key} | `{fmt_bool(value)}` |")
    lines.extend(
        [
            "",
            "## 3. x=20000 压力诊断",
            "",
            "| item | value |",
            "| --- | ---: |",
            f"| anchor x | `{pressure['anchor_x']:.0f}` |",
            f"| log(anchor x) | `{fmt_float(pressure['log_anchor_x'])}` |",
            f"| target relative error | `{pressure['target_relative_error']:.15f}` |",
            f"| zero-free c | `{pressure['zero_free_region_c']:.15f}` |",
            f"| diagnostic exponent sqrt(c)/4 | `{pressure['diagnostic_conservative_exponent']:.15f}` |",
            f"| diagnostic factor at 20000 | `{pressure['diagnostic_factor_at_20000']:.12f}` |",
            f"| log x needed for target if K=1 | `{pressure['log_x_needed_for_target_if_K1']:.6e}` |",
            "",
            "该表只用于说明常数压力：普通零点自由区型 PNT 误差远不足以在 `x=20000` 直接达到 Dusart 级目标。",
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 5. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"当前最窄点更新为 `{result['next_priority']}`；随后是 "
                f"`{result['secondary_priority']}` 与 `{result['tertiary_priority']}`。"
                f"`{result['post_contour_priority']}` 和 `{result['finite_low_height_priority']}` 保持独立。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--explicit-formula", type=Path, default=DEFAULT_EXPLICIT_FORMULA)
    parser.add_argument("--final-draft", type=Path, default=DEFAULT_FINAL_DRAFT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "explicit_formula": args.explicit_formula,
        "final_draft": args.final_draft,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
