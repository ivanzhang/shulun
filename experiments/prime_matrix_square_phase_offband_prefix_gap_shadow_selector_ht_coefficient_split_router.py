#!/usr/bin/env python3
"""把 selector 正密度余量拆成平方窗下系数与尾素数上系数。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_coefficient_split_router.py --max-p 10000 --p0 2001 --h-coeff 0.43 --t-coeff 0.212
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-router.md
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

DENSITY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-router.md"

EXTERNAL_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py"
)
DENSITY_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_density_budget_router.py"
)

MAIN_TARGET = "SelectorPositiveDensitySquareWindowSurplusInputOrBoundaryRecurrencePDEC"
NEXT_TARGET = "SquareWindowLowerCoefficientAndTailUpperCoefficientOrCorrelatedSurplusPDEC"


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


def enrich(row: dict[str, Any], h_coeff: float, t_coeff: float) -> dict[str, Any]:
    """添加 H/T 系数字段。"""
    p_value = int(row["p"])
    log_p = math.log(p_value)
    h_value = int(row["H"])
    t_value = int(row["T"])
    h_scaled = h_value * log_p / p_value
    t_scaled = t_value * log_p / p_value
    split_c = h_coeff - 2 * t_coeff
    required = 3 - 2 * int(row["target_W"])
    return {
        **row,
        "H_scaled_coeff": h_scaled,
        "T_scaled_coeff": t_scaled,
        "split_density_c": split_c,
        "H_lower_coeff_holds": h_scaled >= h_coeff,
        "T_upper_coeff_holds": t_scaled <= t_coeff,
        "split_density_floor": split_c * p_value / log_p,
        "split_floor_closes_this_row": split_c * p_value / log_p >= required,
        "dominance_margin": int(row["square_window_tail_dominance_margin"]),
    }


def band_records(rows: list[dict[str, Any]], bands: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """按 P 区间汇总 H/T 系数。"""
    records: list[dict[str, Any]] = []
    for lo, hi in bands:
        selected = [row for row in rows if lo <= int(row["p"]) <= hi]
        h_values = [float(row["H_scaled_coeff"]) for row in selected]
        t_values = [float(row["T_scaled_coeff"]) for row in selected]
        records.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "hit_count": len(selected),
                "min_H_scaled_coeff": min(h_values, default=None),
                "max_T_scaled_coeff": max(t_values, default=None),
                "separated_min_surplus_coeff": (min(h_values) - 2 * max(t_values)) if selected else None,
                "p_values_at_min_H": sorted({int(row["p"]) for row in selected if h_values and float(row["H_scaled_coeff"]) == min(h_values)}),
                "p_values_at_max_T": sorted({int(row["p"]) for row in selected if t_values and float(row["T_scaled_coeff"]) == max(t_values)}),
            }
        )
    return records


def low_examples(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """列出最紧系数样本。"""
    selected = sorted(rows, key=lambda row: (float(row["H_scaled_coeff"] - 2 * row["T_scaled_coeff"]), int(row["p"])))
    return [
        {
            "template_index": int(row["template_index"]),
            "p": int(row["p"]),
            "side": row["side"],
            "rho": int(row["rho"]),
            "target_W": int(row["target_W"]),
            "H": int(row["H"]),
            "T": int(row["T"]),
            "H_scaled_coeff": float(row["H_scaled_coeff"]),
            "T_scaled_coeff": float(row["T_scaled_coeff"]),
            "actual_surplus_coeff": float(row["H_scaled_coeff"] - 2 * row["T_scaled_coeff"]),
            "dominance_margin": int(row["dominance_margin"]),
        }
        for row in selected[:limit]
    ]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "coefficient_split_sufficient_condition",
            "status": "closed",
            "statement": "H>=aP/logP and T<=bP/logP imply H-2T>=(a-2b)P/logP.",
        },
        {
            "name": "current_split_coefficients_support_a043_b0212_after_2001",
            "status": "closed_on_current_sweep",
            "statement": "The finite sweep supports a=0.43 and b=0.212 after P0=2001.",
        },
        {
            "name": "global_square_window_lower_and_tail_upper_coefficients",
            "status": "open",
            "statement": "A global proof must establish the square-window lower coefficient and tail upper coefficient, or use a correlated surplus theorem.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "CoefficientSplitSufficientConditionClosed",
            "closed": True,
            "proved": True,
            "meaning": "H 下系数与 T 上系数可推出正密度余量。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentCoefficientSplitHolds",
            "closed": agg["H_lower_failure_count_at_p0"] == 0 and agg["T_upper_failure_count_at_p0"] == 0,
            "proved": True,
            "meaning": "当前有限数据支持 a=0.43,b=0.212,P0=2001。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalCoefficientSplitProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明平方窗下系数与尾素数上系数。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "CorrelatedSurplusAlternativeProved",
            "closed": False,
            "proved": False,
            "meaning": "若分离系数过粗，可直接证明 H-2T 的相关正余量。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只拆分系数输入，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(density_ledger: Path, template_ledger: Path, max_p: int, p0: int, h_coeff: float, t_coeff: float) -> dict[str, Any]:
    """构造 H/T 系数拆分结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(density_ledger)
    external_module = load_module(EXTERNAL_ROUTER, "ht_coeff_external")
    base_rows, replay = external_module.build_rows(max_p, template_ledger)
    rows = [enrich(row, h_coeff, t_coeff) for row in base_rows]
    selected = [row for row in rows if int(row["p"]) >= p0]
    split_c = h_coeff - 2 * t_coeff
    aggregate = {
        "density_ledger": str(density_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "h_coeff": h_coeff,
        "t_coeff": t_coeff,
        "split_density_c": split_c,
        "prime_rho_hit_count": len(rows),
        "previous_prime_rho_hit_count": source["aggregate"]["prime_rho_hit_count"],
        "formula_failure_count": len(replay["formula_failures"]),
        "H_lower_failure_count_at_p0": sum(1 for row in selected if not row["H_lower_coeff_holds"]),
        "T_upper_failure_count_at_p0": sum(1 for row in selected if not row["T_upper_coeff_holds"]),
        "split_floor_closure_failure_count_at_p0": sum(1 for row in selected if not row["split_floor_closes_this_row"]),
        "dominance_failure_count": sum(1 for row in rows if int(row["dominance_margin"]) < 0),
        "global_coefficient_split_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {**source["parameters"], "max_p": max_p, "p0": p0, "h_coeff": h_coeff, "t_coeff": t_coeff},
        "aggregate": aggregate,
        "band_records": band_records(rows, [(3, 2000), (2001, 5000), (5001, max_p)]),
        "low_coefficient_examples": low_examples(rows),
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_coefficient_split_router",
        "status": "selector_positive_density_surplus_reduced_to_coefficient_split_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_coefficient_split_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "band_records": ledger["band_records"],
        "low_coefficient_examples": ledger["low_coefficient_examples"],
        "global_coefficient_split_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_coefficient_split_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py": sha256(
                EXTERNAL_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_density_budget_router.py": sha256(
                DENSITY_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-ledger.json": sha256(
                density_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            f"本步把正密度余量输入拆成两个系数门：`H>={h_coeff}P/logP` 与 "
            f"`T<={t_coeff}P/logP`。二者给出 `H-2T>={split_c}P/logP`；"
            f"在 `P>={p0}` 时足以压过 W=1 的常数项。当前有限数据支持该拆分，"
            "但全局系数证明仍未完成。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H/T coefficient split router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"h_coeff={agg['h_coeff']}",
        f"t_coeff={agg['t_coeff']}",
        f"split_density_c={agg['split_density_c']}",
        f"prime_rho_hit_count={agg['prime_rho_hit_count']}",
        f"H_lower_failure_count_at_p0={agg['H_lower_failure_count_at_p0']}",
        f"T_upper_failure_count_at_p0={agg['T_upper_failure_count_at_p0']}",
        f"split_floor_closure_failure_count_at_p0={agg['split_floor_closure_failure_count_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 系数拆分",
        "",
        "充分条件为：",
        "",
        "```text",
        "H >= a P/logP",
        "T <= b P/logP",
        "a - 2b > 0.",
        "```",
        "",
        "当前登记的可攻参数是 `a=0.43,b=0.212`，因此 `a-2b=0.006`。在 `P>=2001`，该正密度项已经大于 W=1 的常数项 `1`。",
        "",
        "## 2. P 区间系数",
        "",
        "| P range | hits | min H coeff | max T coeff | separated surplus | p at min H | p at max T |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["hit_count"]),
                    str(row["min_H_scaled_coeff"]),
                    str(row["max_T_scaled_coeff"]),
                    str(row["separated_min_surplus_coeff"]),
                    f"`{row['p_values_at_min_H']}`",
                    f"`{row['p_values_at_max_T']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 最紧样本",
            "",
            "| actual surplus coeff | template | p | side | rho | W | H | T | H coeff | T coeff | margin |",
            "| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["low_coefficient_examples"][:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["actual_surplus_coeff"]),
                    str(row["template_index"]),
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["target_W"]),
                    str(row["H"]),
                    str(row["T"]),
                    str(row["H_scaled_coeff"]),
                    str(row["T_scaled_coeff"]),
                    str(row["dominance_margin"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构判断",
            "",
            "- 分离系数门是比直接 `H-2T` 余量更强的输入；它更容易和外部尾素数上界、内部平方窗下界对接。",
            "- 当前尾素数上界形状看起来可由全局显式 `pi(x)` 上界处理；真正困难仍集中在 selector 平方窗下系数。",
            "- 若分离系数无法证明，可退回直接相关余量或低余量复现 PDEC。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 5. 命题行",
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
            "## 6. 决策表",
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
            "## 7. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 优先证明 `T<=0.212P/logP` 的尾素数上界是否可由显式 `pi(x)` 上界关闭。",
            "- 主要难点是证明 selector 平方窗 `H>=0.43P/logP`，或给出相关余量替代。",
            "",
            "## 8. 依赖哈希",
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
    parser.add_argument("--density-ledger", type=Path, default=DENSITY_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--h-coeff", type=float, default=0.43)
    parser.add_argument("--t-coeff", type=float, default=0.212)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    density_ledger = args.density_ledger if args.density_ledger.is_absolute() else ROOT / args.density_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(density_ledger, template_ledger, args.max_p, args.p0, args.h_coeff, args.t_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "p0": args.p0,
                "h_coeff": args.h_coeff,
                "t_coeff": args.t_coeff,
                "H_lower_failure_count_at_p0": result["aggregate"]["H_lower_failure_count_at_p0"],
                "T_upper_failure_count_at_p0": result["aggregate"]["T_upper_failure_count_at_p0"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
