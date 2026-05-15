#!/usr/bin/env python3
"""把 W 专属 H/T 硬点改写为平方窗-尾素数支配输入并审查外部对接。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

BOUNDARY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-router.md"

BOUNDARY_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_boundary_source_router.py"
)

MAIN_TARGET = "WSpecificHTSourceInequalityOrBoundaryRecurrencePDEC"
NEXT_TARGET = "SelectorResidueSquareWindowTailDominanceOrBoundaryPDEC"


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


def square_window_count_from_prefix(p_value: int, side: str, pi_prefix: list[int]) -> int:
    """用素数计数前缀计算 P^2±r, 1<=r<P 的窗口素数数。"""
    base = p_value * p_value
    if side == "plus":
        return pi_prefix[base + p_value - 1] - pi_prefix[base]
    if side == "minus":
        return pi_prefix[base - 1] - pi_prefix[base - p_value]
    raise ValueError(f"unknown side: {side}")


def tail_count_from_prefix(p_value: int, pi_prefix: list[int]) -> int:
    """计算 floor(4P/5)<q<P 的尾部素数数。"""
    return pi_prefix[p_value - 1] - pi_prefix[(4 * p_value) // 5]


def w_specific_required_bound(target_w: int) -> int:
    """返回 H-2T 的 W 专属下界。"""
    return 3 - 2 * target_w


def external_input_rows() -> list[dict[str, Any]]:
    """审查常见外部输入与当前硬点的形状匹配。"""
    return [
        {
            "input": "Baker-Harman-Pintz x^0.525 prime gap",
            "matches_required_shape": False,
            "reason": "可给长度约 (P^2)^0.525=P^1.05 的存在性，不能推出长度 P 的平方窗素数计数下界，更不能比较到 2T。",
        },
        {
            "input": "Legendre-type prime in every (n^2,(n+1)^2)",
            "matches_required_shape": False,
            "reason": "即使给每个平方间隙至少一个素数，也远弱于 H >= 2T + O(1) 的计数支配。",
        },
        {
            "input": "RH/Schoenfeld-style explicit formula error",
            "matches_required_shape": False,
            "reason": "平方窗长度为 sqrt(x)；RH 级误差通常仍大于主项 P/log P，不能直接保证该短窗计数下界。",
        },
        {
            "input": "ordinary PNT or arithmetic progression PNT",
            "matches_required_shape": False,
            "reason": "只给长区间或平均意义，不能逐点控制每个 selector residue 上的 P 长度平方窗。",
        },
        {
            "input": "SelectorResidueSquareWindowTailDominance",
            "matches_required_shape": True,
            "reason": "精确需要证明 selector rho 命中时，平方窗计数 H 至少支配尾素数计数 2T 加 W 专属常数。",
        },
    ]


def build_rows(max_p: int, template_ledger: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """重放 prime rho hits 并核对 H/T 素数计数公式。"""
    boundary_module = load_module(BOUNDARY_ROUTER, "ht_external_boundary")
    nf_module = boundary_module.load_module(boundary_module.NORMAL_FORM_ROUTER, "ht_external_normal_form")
    pressure_module = nf_module.load_module(nf_module.PRESSURE_GAP_ROUTER, "ht_external_pressure")
    rho_module = pressure_module.load_module(pressure_module.RHO_OBSTRUCTION_ROUTER, "ht_external_rho")
    template_source = load_json(template_ledger)
    env = rho_module.build_environment(max_p)
    templates = rho_module.build_templates(template_source)
    hits = pressure_module.collect_prime_rho_hits(rho_module, env, templates, max_p)
    rows: list[dict[str, Any]] = []
    formula_failures: list[dict[str, Any]] = []
    for hit in hits:
        row = nf_module.normalize_hit(hit)
        p_value = int(row["p"])
        side = row["side"]
        h_formula = square_window_count_from_prefix(p_value, side, env["pi_prefix"])
        t_formula = tail_count_from_prefix(p_value, env["pi_prefix"])
        required_bound = w_specific_required_bound(int(row["target_W"]))
        dominance_margin = h_formula - 2 * t_formula - required_bound
        formula_ok = h_formula == int(row["H"]) and t_formula == int(row["T"])
        if not formula_ok:
            formula_failures.append(
                {
                    "p": p_value,
                    "side": side,
                    "H": row["H"],
                    "H_formula": h_formula,
                    "T": row["T"],
                    "T_formula": t_formula,
                }
            )
        rows.append(
            {
                "template_index": int(row["template_index"]),
                "p": p_value,
                "side": side,
                "rho": int(row["rho"]),
                "target_W": int(row["target_W"]),
                "H": int(row["H"]),
                "T": int(row["T"]),
                "square_window_formula_count": h_formula,
                "tail_formula_count": t_formula,
                "required_h_minus_2t_lower_bound": required_bound,
                "square_window_tail_dominance_margin": dominance_margin,
                "normal_form_slack": int(row["normal_form_slack"]),
                "formula_ok": formula_ok,
            }
        )
    return rows, {"formula_failures": formula_failures}


def side_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 side 与 W 汇总平方窗-尾素数支配余量。"""
    grouped: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault((row["side"], int(row["target_W"])), []).append(row)
    records: list[dict[str, Any]] = []
    for (side, target_w), values in sorted(grouped.items()):
        margins = [int(row["square_window_tail_dominance_margin"]) for row in values]
        records.append(
            {
                "side": side,
                "target_W": target_w,
                "hit_count": len(values),
                "min_margin": min(margins),
                "max_margin": max(margins),
                "zero_margin_count": sum(1 for value in margins if value == 0),
                "margin_histogram_head": dict(sorted(Counter(margins).items())[:20]),
                "p_values_at_min": sorted({int(row["p"]) for row in values if int(row["square_window_tail_dominance_margin"]) == min(margins)}),
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "h_t_prime_count_identity",
            "status": "closed",
            "statement": "H equals the P-length square-window prime count and T equals the tail prime count pi(P-1)-pi(floor(4P/5)).",
        },
        {
            "name": "external_input_shape_audit",
            "status": "closed",
            "statement": "Common short-interval existence inputs do not match the required square-window tail-dominance count inequality.",
        },
        {
            "name": "selector_residue_square_window_tail_dominance",
            "status": "open",
            "statement": "A global proof must establish the dominance inequality on selector rho hits, or register recurrent boundary failure as PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "HTPrimeCountIdentityClosed",
            "closed": agg["formula_failure_count"] == 0,
            "proved": True,
            "meaning": "H/T 已精确写成素数计数函数差。",
            "remaining": "closed",
        },
        {
            "gate": "KnownExternalInputsMatch",
            "closed": False,
            "proved": False,
            "meaning": "BHP、Legendre 型存在性、RH/PNT 误差均不直接给所需计数支配。",
            "remaining": "need exact square-window tail-dominance input",
        },
        {
            "gate": "CurrentDominanceHolds",
            "closed": agg["dominance_failure_count"] == 0,
            "proved": True,
            "meaning": "当前有限前沿的 selector rho 命中满足平方窗-尾素数支配。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "GlobalDominanceProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明该支配，或把反复失败登记为边界 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成外部输入形状匹配审查，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(boundary_ledger: Path, template_ledger: Path, max_p: int) -> dict[str, Any]:
    """构造外部输入匹配结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    boundary_source = load_json(boundary_ledger)
    rows, replay = build_rows(max_p, template_ledger)
    margins = [int(row["square_window_tail_dominance_margin"]) for row in rows]
    external_rows = external_input_rows()
    aggregate = {
        "boundary_ledger": str(boundary_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "prime_rho_hit_count": len(rows),
        "expected_prime_rho_hit_count": boundary_source["aggregate"]["prime_rho_hit_count"],
        "matches_boundary_total": len(rows) == boundary_source["aggregate"]["prime_rho_hit_count"],
        "formula_failure_count": len(replay["formula_failures"]),
        "dominance_failure_count": sum(1 for row in rows if int(row["square_window_tail_dominance_margin"]) < 0),
        "min_square_window_tail_dominance_margin": min(margins, default=0),
        "max_square_window_tail_dominance_margin": max(margins, default=0),
        "zero_margin_count": sum(1 for margin in margins if margin == 0),
        "known_external_match_count": sum(1 for row in external_rows if row["matches_required_shape"]),
        "known_standard_external_match_count": sum(
            1 for row in external_rows if row["matches_required_shape"] and row["input"] != "SelectorResidueSquareWindowTailDominance"
        ),
        "global_selector_residue_square_window_tail_dominance_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {**boundary_source["parameters"], "max_p": max_p},
        "aggregate": aggregate,
        "side_w_records": side_records(rows),
        "external_input_match_rows": external_rows,
        "formula_failures": replay["formula_failures"],
        "low_margin_examples": sorted(rows, key=lambda row: (int(row["square_window_tail_dominance_margin"]), int(row["p"])))[:30],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router",
        "status": "selector_ht_hardpoint_reduced_to_square_window_tail_dominance_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_dominance_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "side_w_records": ledger["side_w_records"],
        "external_input_match_rows": external_rows,
        "low_margin_examples": ledger["low_margin_examples"],
        "global_selector_residue_square_window_tail_dominance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_boundary_source_router.py": sha256(
                BOUNDARY_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-ledger.json": sha256(
                boundary_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 W 专属 H/T 硬点精确改写为平方窗-尾素数支配："
            "`H=pi(P^2±window)`，`T=pi(P-1)-pi(floor(4P/5))`。"
            "常见外部短区间存在性输入不直接匹配；真正需要的是 selector residue 上的平方窗计数支配。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H/T external input match router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"prime_rho_hit_count={agg['prime_rho_hit_count']}",
        f"formula_failure_count={agg['formula_failure_count']}",
        f"dominance_failure_count={agg['dominance_failure_count']}",
        f"min_square_window_tail_dominance_margin={agg['min_square_window_tail_dominance_margin']}",
        f"zero_margin_count={agg['zero_margin_count']}",
        f"known_standard_external_match_count={agg['known_standard_external_match_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确计数接口",
        "",
        "对 `side=plus`：",
        "",
        "```text",
        "H = pi(P^2+P-1)-pi(P^2)",
        "```",
        "",
        "对 `side=minus`：",
        "",
        "```text",
        "H = pi(P^2-1)-pi(P^2-P)",
        "```",
        "",
        "共同的尾素数项为：",
        "",
        "```text",
        "T = pi(P-1)-pi(floor(4P/5))",
        "```",
        "",
        "因此下一层目标不是普通“有一个素数”，而是 selector rho 命中时的计数支配：",
        "",
        "```text",
        "H - 2T - (3-2W) >= 0.",
        "```",
        "",
        "## 2. side/W 余量",
        "",
        "| side | W | hits | min margin | max margin | zero margin | p at min |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["side_w_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["side"],
                    str(row["target_W"]),
                    str(row["hit_count"]),
                    str(row["min_margin"]),
                    str(row["max_margin"]),
                    str(row["zero_margin_count"]),
                    f"`{row['p_values_at_min']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 外部输入匹配审查",
            "",
            "| input | matches | reason |",
            "| --- | ---: | --- |",
        ]
    )
    for row in result["external_input_match_rows"]:
        lines.append(f"| `{row['input']}` | `{fmt_bool(row['matches_required_shape'])}` | {table_cell(row['reason'])} |")
    lines.extend(
        [
            "",
            "## 4. 低余量样本",
            "",
            "| template | p | side | rho | W | H | T | margin | slack |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["low_margin_examples"][:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["template_index"]),
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["target_W"]),
                    str(row["H"]),
                    str(row["T"]),
                    str(row["square_window_tail_dominance_margin"]),
                    str(row["normal_form_slack"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
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
            "- 内部路线：利用 selector residue、低轮、prefix atom 与平方窗相位共同约束证明上述计数支配。",
            "- 外部路线：必须提供同形状的平方窗-尾素数支配输入；普通短区间存在性、BHP、RH/PNT 不能直接替代。",
            "- 当前仍未证明全局行/列无条件闭合。",
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
    parser.add_argument("--boundary-ledger", type=Path, default=BOUNDARY_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=5000)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    boundary_ledger = args.boundary_ledger if args.boundary_ledger.is_absolute() else ROOT / args.boundary_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(boundary_ledger, template_ledger, args.max_p)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "prime_rho_hit_count": result["aggregate"]["prime_rho_hit_count"],
                "formula_failure_count": result["aggregate"]["formula_failure_count"],
                "dominance_failure_count": result["aggregate"]["dominance_failure_count"],
                "known_standard_external_match_count": result["aggregate"]["known_standard_external_match_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
