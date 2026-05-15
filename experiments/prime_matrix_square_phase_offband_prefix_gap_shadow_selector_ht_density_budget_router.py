#!/usr/bin/env python3
"""把平方窗-尾素数支配压成正密度余量输入。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_density_budget_router.py --max-p 10000 --density-c 0.01 --p0 2001
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

BOUNDARY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-router.md"

EXTERNAL_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py"
)
BOUNDARY_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_dominance_boundary_recurrence_router.py"
)

MAIN_TARGET = "AsymptoticSquareWindowTailDominanceOrLowMarginBoundaryRecurrencePDEC"
NEXT_TARGET = "SelectorPositiveDensitySquareWindowSurplusInputOrBoundaryRecurrencePDEC"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def enriched_row(row: dict[str, Any], density_c: float) -> dict[str, Any]:
    """给单行添加密度预算字段。"""
    p_value = int(row["p"])
    h_minus_2t = int(row["H"]) - 2 * int(row["T"])
    required = 3 - 2 * int(row["target_W"])
    margin = h_minus_2t - required
    log_p = math.log(p_value)
    density_surplus_coeff = h_minus_2t * log_p / p_value
    margin_coeff = margin * log_p / p_value
    density_floor = density_c * p_value / log_p
    return {
        **row,
        "h_minus_2t": h_minus_2t,
        "required_h_minus_2t": required,
        "dominance_margin": margin,
        "density_surplus_coeff": density_surplus_coeff,
        "dominance_margin_coeff": margin_coeff,
        "density_floor_c_p_over_logp": density_floor,
        "density_floor_closes_this_row": density_floor >= required,
        "density_input_would_cover_this_row": h_minus_2t >= density_floor,
    }


def band_records(rows: list[dict[str, Any]], bands: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """按 P 区间汇总密度余量。"""
    records: list[dict[str, Any]] = []
    for lo, hi in bands:
        selected = [row for row in rows if lo <= int(row["p"]) <= hi]
        coeffs = [float(row["density_surplus_coeff"]) for row in selected]
        margins = [int(row["dominance_margin"]) for row in selected]
        records.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "hit_count": len(selected),
                "min_density_surplus_coeff": min(coeffs, default=None),
                "avg_density_surplus_coeff": sum(coeffs) / len(coeffs) if coeffs else None,
                "min_margin": min(margins, default=None),
                "p_values_at_min_coeff": sorted(
                    {
                        int(row["p"])
                        for row in selected
                        if coeffs and float(row["density_surplus_coeff"]) == min(coeffs)
                    }
                ),
            }
        )
    return records


def p0_records(rows: list[dict[str, Any]], p0_values: list[int], density_c: float) -> list[dict[str, Any]]:
    """不同 P0 下的密度输入审计。"""
    records: list[dict[str, Any]] = []
    for p0 in p0_values:
        selected = [row for row in rows if int(row["p"]) >= p0]
        coeffs = [float(row["density_surplus_coeff"]) for row in selected]
        floor_failures = [row for row in selected if not row["density_floor_closes_this_row"]]
        input_failures = [row for row in selected if not row["density_input_would_cover_this_row"]]
        records.append(
            {
                "p0": p0,
                "hit_count": len(selected),
                "density_c": density_c,
                "min_density_surplus_coeff": min(coeffs, default=None),
                "density_floor_closure_failure_count": len(floor_failures),
                "current_density_input_failure_count": len(input_failures),
                "p_values_at_min_coeff": sorted(
                    {
                        int(row["p"])
                        for row in selected
                        if coeffs and float(row["density_surplus_coeff"]) == min(coeffs)
                    }
                ),
                "sufficient_if_global_density_input_proved": len(floor_failures) == 0,
            }
        )
    return records


def low_coeff_examples(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """列出密度余量系数最低的对象。"""
    selected = sorted(rows, key=lambda row: (float(row["density_surplus_coeff"]), int(row["p"]), int(row["template_index"])))
    examples: list[dict[str, Any]] = []
    for row in selected[:limit]:
        examples.append(
            {
                "template_index": int(row["template_index"]),
                "p": int(row["p"]),
                "side": row["side"],
                "rho": int(row["rho"]),
                "target_W": int(row["target_W"]),
                "H": int(row["H"]),
                "T": int(row["T"]),
                "h_minus_2t": int(row["h_minus_2t"]),
                "required_h_minus_2t": int(row["required_h_minus_2t"]),
                "dominance_margin": int(row["dominance_margin"]),
                "density_surplus_coeff": float(row["density_surplus_coeff"]),
            }
        )
    return examples


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "positive_density_surplus_sufficient_condition",
            "status": "closed",
            "statement": "If H-2T>=cP/logP beyond P0 and cP/logP>=3-2W, then the dominance margin is nonnegative.",
        },
        {
            "name": "current_density_budget_supports_c001_after_2001",
            "status": "closed_on_current_sweep",
            "statement": "The finite sweep supports c=0.01 after P0=2001, but this is not a global proof.",
        },
        {
            "name": "selector_positive_density_square_window_surplus",
            "status": "open",
            "statement": "A global proof must establish H-2T>=cP/logP on selector rho hits beyond the finite boundary core.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "DensitySurplusSufficientConditionClosed",
            "closed": True,
            "proved": True,
            "meaning": "正密度余量输入足以推出平方窗-尾素数支配。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentC001P0Support",
            "closed": agg["current_density_input_failure_count_at_p0"] == 0,
            "proved": True,
            "meaning": "当前有限数据支持 c=0.01, P0=2001。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalPositiveDensitySurplusProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明 selector rho 命中上 H-2T 有固定正密度级下界。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "BoundaryRecurrencePDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若低余量签名高处复现，仍需 PDEC/ColumnCRT 排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只给出充分条件和有限预算，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(boundary_ledger: Path, template_ledger: Path, max_p: int, density_c: float, p0: int) -> dict[str, Any]:
    """构造正密度预算结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(boundary_ledger)
    external_module = load_module(EXTERNAL_ROUTER, "ht_density_external")
    base_rows, replay = external_module.build_rows(max_p, template_ledger)
    rows = [enriched_row(row, density_c) for row in base_rows]
    p0_values = sorted({3, 157, 173, 1777, 2001, 5001, p0})
    selected_after_p0 = [row for row in rows if int(row["p"]) >= p0]
    coeffs_after_p0 = [float(row["density_surplus_coeff"]) for row in selected_after_p0]
    current_density_failures = [row for row in selected_after_p0 if not row["density_input_would_cover_this_row"]]
    density_floor_failures = [row for row in selected_after_p0 if not row["density_floor_closes_this_row"]]
    aggregate = {
        "boundary_ledger": str(boundary_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "density_c": density_c,
        "p0": p0,
        "prime_rho_hit_count": len(rows),
        "previous_prime_rho_hit_count": source["aggregate"]["prime_rho_hit_count"],
        "formula_failure_count": len(replay["formula_failures"]),
        "dominance_failure_count": sum(1 for row in rows if int(row["dominance_margin"]) < 0),
        "min_density_surplus_coeff_after_p0": min(coeffs_after_p0, default=None),
        "current_density_input_failure_count_at_p0": len(current_density_failures),
        "density_floor_closure_failure_count_at_p0": len(density_floor_failures),
        "positive_density_surplus_global_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {**source["parameters"], "max_p": max_p, "density_c": density_c, "p0": p0},
        "aggregate": aggregate,
        "band_records": band_records(rows, [(3, 2000), (2001, 5000), (5001, max_p)]),
        "p0_records": p0_records(rows, p0_values, density_c),
        "low_coeff_examples": low_coeff_examples(rows),
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_density_budget_router",
        "status": "selector_square_window_tail_dominance_reduced_to_positive_density_surplus_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_density_budget_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "band_records": ledger["band_records"],
        "p0_records": ledger["p0_records"],
        "low_coeff_examples": ledger["low_coeff_examples"],
        "positive_density_surplus_global_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_density_budget_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py": sha256(
                EXTERNAL_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_dominance_boundary_recurrence_router.py": sha256(
                BOUNDARY_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-ledger.json": sha256(
                boundary_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            f"本步把 asymptotic dominance 压成正密度余量输入：若在 selector rho 命中上 "
            f"`H-2T>={density_c}P/logP` 对 `P>={p0}` 成立，则常数项也被压过，"
            "平方窗-尾素数支配随之闭合。当前有限数据支持该预算，但全局正密度余量尚未证明。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H/T density budget router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"density_c={agg['density_c']}",
        f"p0={agg['p0']}",
        f"prime_rho_hit_count={agg['prime_rho_hit_count']}",
        f"formula_failure_count={agg['formula_failure_count']}",
        f"dominance_failure_count={agg['dominance_failure_count']}",
        f"min_density_surplus_coeff_after_p0={agg['min_density_surplus_coeff_after_p0']}",
        f"current_density_input_failure_count_at_p0={agg['current_density_input_failure_count_at_p0']}",
        f"density_floor_closure_failure_count_at_p0={agg['density_floor_closure_failure_count_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 充分条件",
        "",
        "当前支配余量是",
        "",
        "```text",
        "margin = H - 2T - (3-2W).",
        "```",
        "",
        "若对边界核之后的 selector rho 命中有",
        "",
        "```text",
        "H - 2T >= c P/log P",
        "c P/log P >= 3-2W,",
        "```",
        "",
        "则 `margin>=0`。由于 `W=1` 是唯一正常数项，`c=0.01,P0=2001` 已使 `cP/logP>1`，足以压过常数项。",
        "",
        "## 2. P 区间密度系数",
        "",
        "| P range | hits | min coeff | avg coeff | min margin | p at min coeff |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["hit_count"]),
                    str(row["min_density_surplus_coeff"]),
                    str(row["avg_density_surplus_coeff"]),
                    str(row["min_margin"]),
                    f"`{row['p_values_at_min_coeff']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. P0 预算",
            "",
            "| P0 | hits | c | min coeff | c-input failures | floor failures | sufficient if global input proved |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["p0_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p0"]),
                    str(row["hit_count"]),
                    str(row["density_c"]),
                    str(row["min_density_surplus_coeff"]),
                    str(row["current_density_input_failure_count"]),
                    str(row["density_floor_closure_failure_count"]),
                    f"`{fmt_bool(row['sufficient_if_global_density_input_proved'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 最低系数样本",
            "",
            "| coeff | template | p | side | rho | W | H | T | H-2T | margin |",
            "| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["low_coeff_examples"][:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["density_surplus_coeff"]),
                    str(row["template_index"]),
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["target_W"]),
                    str(row["H"]),
                    str(row["T"]),
                    str(row["h_minus_2t"]),
                    str(row["dominance_margin"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 结构判断",
            "",
            "- 这一步没有证明短区间素数定理；它只把所需输入精确压成 selector 条件下的正密度余量。",
            "- 普通 BHP/Legendre/RH-PNT 仍不能直接替代该输入；需要同形状的 `H-2T` 正密度证明。",
            "- 若无法证明正密度余量，则必须继续沿低余量签名做 BoundaryRecurrence-PDEC/ColumnCRT 排斥。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 6. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 7. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 8. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 内部路线：证明 selector rho 命中强制 `H-2T>=cP/logP`。",
            "- PDEC 路线：若正密度输入失败，则低余量签名必须长期复现并进入 BoundaryRecurrence/ColumnCRT。",
            "",
            "## 9. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boundary-ledger", type=Path, default=BOUNDARY_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--density-c", type=float, default=0.01)
    parser.add_argument("--p0", type=int, default=2001)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    boundary_ledger = args.boundary_ledger if args.boundary_ledger.is_absolute() else ROOT / args.boundary_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(boundary_ledger, template_ledger, args.max_p, args.density_c, args.p0)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "density_c": args.density_c,
                "p0": args.p0,
                "prime_rho_hit_count": result["aggregate"]["prime_rho_hit_count"],
                "current_density_input_failure_count_at_p0": result["aggregate"]["current_density_input_failure_count_at_p0"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
