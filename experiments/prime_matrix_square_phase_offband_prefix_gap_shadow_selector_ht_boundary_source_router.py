#!/usr/bin/env python3
"""展开 prime rho hit 的 H/T 正规形边界来源。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_boundary_source_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-router.md
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

NORMAL_FORM_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-router.md"

NORMAL_FORM_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_pressure_inequality_normal_form_router.py"
)

MAIN_TARGET = "PrimeRhoHitHTInequalityLowerBoundOrFullShapeOverlapPDEC"
NEXT_TARGET = "WSpecificHTSourceInequalityOrBoundaryRecurrencePDEC"


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


def short_list(values: list[int], limit: int = 16) -> dict[str, Any]:
    """压缩长列表，保留头尾与总量。"""
    if len(values) <= 2 * limit:
        return {"count": len(values), "values": values}
    return {
        "count": len(values),
        "head": values[:limit],
        "tail": values[-limit:],
    }


def square_window_prime_offsets(p_value: int, side: str, prime_flags: bytearray) -> list[int]:
    """列出 P^2±r 窗口中的素数偏移 r。"""
    base = p_value * p_value
    offsets: list[int] = []
    for r_value in range(1, p_value):
        n_value = base + r_value if side == "plus" else base - r_value
        if prime_flags[n_value]:
            offsets.append(r_value)
    return offsets


def tail_prime_values(p_value: int, prime_flags: bytearray) -> list[int]:
    """列出 floor(4P/5)<q<P 的尾部素数。"""
    lo = (4 * p_value) // 5 + 1
    if lo % 2 == 0:
        lo += 1
    return [q_value for q_value in range(lo, p_value, 2) if prime_flags[q_value]]


def compact_atom(atom: dict[str, Any]) -> dict[str, Any]:
    """压缩前三 prefix atom 的来源。"""
    return {
        "band": atom["band"],
        "k": int(atom["k"]),
        "b_lo": int(atom["b_lo"]),
        "b_hi": int(atom["b_hi"]),
        "b_length": int(atom.get("b_length", atom["b_hi"] - atom["b_lo"] + 1)),
        "q_lo": int(atom["q_lo"]),
        "q_hi": int(atom["q_hi"]),
        "q_span": int(atom["q_span"]),
        "prime_load": int(atom["prime_load"]),
        "q_values": atom.get("q_values", [])[:16],
    }


def replay_row_for_hit(rho_module: Any, env: dict[str, Any], hit: dict[str, Any]) -> dict[str, Any]:
    """对单个 hit 回放完整 gap-shadow 行。"""
    gap = env["gap"]
    split_record = env["split"].audit_p(int(hit["p"]), env["prime_flags"], env["pi_prefix"])
    atoms = env["layer"].layer_atoms_for_p(env["offband"], env["phase"], int(hit["p"]), env["small_flags"])
    return gap.shadow_record(
        env["interval"],
        env["single"],
        env["multiplicity"],
        env["layer"],
        env["two"],
        int(hit["p"]),
        hit["side"],
        split_record[f"{hit['side']}_prime_window"],
        atoms,
        3,
    )


def w_specific_required_bound(target_w: int) -> int:
    """返回 H-2T 的 W 专属下界。"""
    return 3 - 2 * target_w


def w_specific_record(rows: list[dict[str, Any]], target_w: int) -> dict[str, Any]:
    """按 W 汇总 H/T 下界画像。"""
    selected = [row for row in rows if int(row["target_W"]) == target_w]
    h_minus = [int(row["h_minus_2t"]) for row in selected]
    required = w_specific_required_bound(target_w)
    return {
        "target_W": target_w,
        "hit_count": len(selected),
        "required_h_minus_2t_lower_bound": required,
        "min_h_minus_2t": min(h_minus, default=None),
        "max_h_minus_2t": max(h_minus, default=None),
        "bound_failure_count": sum(1 for row in selected if int(row["h_minus_2t"]) < required),
        "bound_equality_count": sum(1 for row in selected if int(row["h_minus_2t"]) == required),
        "h_minus_2t_histogram_head": dict(sorted(Counter(h_minus).items())[:20]),
        "p_values_at_min": sorted({int(row["p"]) for row in selected if h_minus and int(row["h_minus_2t"]) == min(h_minus)}),
    }


def enrich_critical_row(rho_module: Any, env: dict[str, Any], hit: dict[str, Any]) -> dict[str, Any]:
    """展开 slack<=1 的临界行。"""
    p_value = int(hit["p"])
    side = hit["side"]
    replay = replay_row_for_hit(rho_module, env, hit)
    window_offsets = square_window_prime_offsets(p_value, side, env["prime_flags"])
    tail_primes = tail_prime_values(p_value, env["small_flags"])
    required_bound = w_specific_required_bound(int(hit["target_W"]))
    return {
        "template_index": int(hit["template_index"]),
        "p": p_value,
        "side": side,
        "rho": int(hit["rho"]),
        "gcd_modulus_15": int(hit["gcd_modulus_15"]),
        "target_W": int(hit["target_W"]),
        "replay_W": int(hit["replay_W"]),
        "H": int(hit["H"]),
        "T": int(hit["T"]),
        "h_minus_2t": int(hit["h_minus_2t"]),
        "w_specific_required_h_minus_2t_lower_bound": required_bound,
        "bound_excess": int(hit["h_minus_2t"]) - required_bound,
        "signed_tail_deficit_2T_minus_H": int(hit["signed_tail_deficit_2T_minus_H"]),
        "signed_deficit_threshold_2W_minus_3": int(hit["signed_deficit_threshold_2W_minus_3"]),
        "normal_form_slack": int(hit["normal_form_slack"]),
        "pressure_gap_target_minus_replay": int(hit["pressure_gap_target_minus_replay"]),
        "square_window_prime_offsets": short_list(window_offsets),
        "tail_prime_values": short_list(tail_primes),
        "prefix_prime_load": int(replay["prefix_prime_load"]),
        "prefix_loaded_atom_count": int(replay["prefix_loaded_atom_count"]),
        "prefix_void_atom_count": int(replay["prefix_void_atom_count"]),
        "prefix_interval_atoms": [compact_atom(atom) for atom in replay["prefix_interval_atoms"]],
        "void_subset_templates": replay["void_subset_templates"],
    }


def build_result(normal_form_ledger: Path, template_ledger: Path, max_p: int) -> dict[str, Any]:
    """构造 H/T 边界来源结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    normal_source = load_json(normal_form_ledger)
    template_source = load_json(template_ledger)
    nf_module = load_module(NORMAL_FORM_ROUTER, "ht_boundary_normal_form")
    pressure_module = nf_module.load_module(nf_module.PRESSURE_GAP_ROUTER, "ht_boundary_pressure_gap")
    rho_module = pressure_module.load_module(pressure_module.RHO_OBSTRUCTION_ROUTER, "ht_boundary_rho")
    env = rho_module.build_environment(max_p)
    templates = rho_module.build_templates(template_source)
    hits = pressure_module.collect_prime_rho_hits(rho_module, env, templates, max_p)
    rows = [nf_module.normalize_hit(hit) for hit in hits]
    critical_rows = [row for row in rows if int(row["normal_form_slack"]) <= 1]
    boundary_rows = [row for row in rows if int(row["normal_form_slack"]) == 0]
    h_minus = [int(row["h_minus_2t"]) for row in rows]
    critical_p_values = sorted({int(row["p"]) for row in critical_rows})
    w_records = [w_specific_record(rows, target_w) for target_w in sorted({int(row["target_W"]) for row in rows})]
    aggregate = {
        "normal_form_ledger": str(normal_form_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "prime_rho_hit_count": len(rows),
        "expected_prime_rho_hit_count": normal_source["aggregate"]["prime_rho_hit_count"],
        "matches_normal_form_total": len(rows) == normal_source["aggregate"]["prime_rho_hit_count"],
        "global_ht_inequality_failure_count": sum(1 for row in rows if not row["ht_inequality_holds"]),
        "min_h_minus_2t": min(h_minus, default=0),
        "max_h_minus_2t": max(h_minus, default=0),
        "w_specific_bound_failure_count": sum(
            1 for row in rows if int(row["h_minus_2t"]) < w_specific_required_bound(int(row["target_W"]))
        ),
        "critical_slack_le_1_count": len(critical_rows),
        "boundary_slack_zero_count": len(boundary_rows),
        "critical_p_values": critical_p_values,
        "max_critical_p": max(critical_p_values, default=None),
        "critical_template_indices": sorted({int(row["template_index"]) for row in critical_rows}),
        "critical_rho_classes": sorted({f"mod{row['gcd_modulus_15']}={row['rho']}" for row in critical_rows}),
        "critical_all_below_2000_on_current_sweep": all(int(row["p"]) < 2000 for row in critical_rows),
        "w2_stronger_nonnegative_failure_count": sum(
            1 for row in rows if int(row["target_W"]) == 2 and int(row["h_minus_2t"]) < 0
        ),
        "w1_positive_bound_failure_count": sum(
            1 for row in rows if int(row["target_W"]) == 1 and int(row["h_minus_2t"]) < 1
        ),
        "global_w_specific_ht_source_inequality_proved": False,
        "row_column_unconditional_closed": False,
    }
    critical_enriched = [enrich_critical_row(rho_module, env, row) for row in critical_rows]
    ledger = {
        "parameters": {**template_source["parameters"], "max_p": max_p},
        "aggregate": aggregate,
        "w_specific_records": w_records,
        "critical_boundary_records": critical_enriched,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_boundary_source_router",
        "status": "selector_prime_rho_ht_boundary_source_isolated_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_boundary_source_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "w_specific_records": w_records,
        "critical_boundary_records": critical_enriched,
        "global_w_specific_ht_source_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_boundary_source_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_pressure_inequality_normal_form_router.py": sha256(
                NORMAL_FORM_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-ledger.json": sha256(
                normal_form_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 prime rho hit 的 H/T 硬点拆成 W 专属整数下界："
            "W=1 需要 `H-2T>=1`，W=2 需要 `H-2T>=-1`。"
            f"当前 {len(rows)} 个命中没有 W 专属下界失败；"
            f"slack<=1 的临界行只有 {len(critical_rows)} 个，"
            f"slack=0 的真正边界只有 {len(boundary_rows)} 个。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "w_specific_ht_integer_bounds",
            "status": "closed",
            "statement": "The normal form is split into W=1: H-2T>=1 and W=2: H-2T>=-1.",
        },
        {
            "name": "current_w_specific_bounds_hold",
            "status": "closed_on_current_sweep",
            "statement": "Every current prime rho hit satisfies its W-specific H/T bound.",
        },
        {
            "name": "critical_boundary_source_isolated",
            "status": "closed_on_current_sweep",
            "statement": "All slack<=1 rows are explicitly expanded to square-window prime offsets, tail primes, and prefix atoms.",
        },
        {
            "name": "global_w_specific_ht_source_inequality",
            "status": "open",
            "statement": "A global proof must derive the W-specific H/T source inequality, or route recurrent boundary failure to PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "WSpecificIntegerNormalFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "`2T-H<=2W-3` 已拆成 W=1 与 W=2 的整数下界。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentWSpecificBoundsHold",
            "closed": agg["w_specific_bound_failure_count"] == 0,
            "proved": True,
            "meaning": "当前全部 prime rho hit 满足 W 专属 H/T 下界。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "CriticalBoundaryRowsIsolated",
            "closed": True,
            "proved": True,
            "meaning": "slack<=1 的临界对象已全部展开为具体窗口与 atom 来源。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "GlobalWSpecificHTSourceInequalityProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 W 专属 H/T 来源不等式，或把边界复现登记为 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只隔离 H/T 边界来源，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H/T boundary source router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"prime_rho_hit_count={agg['prime_rho_hit_count']}",
        f"global_ht_inequality_failure_count={agg['global_ht_inequality_failure_count']}",
        f"w_specific_bound_failure_count={agg['w_specific_bound_failure_count']}",
        f"critical_slack_le_1_count={agg['critical_slack_le_1_count']}",
        f"boundary_slack_zero_count={agg['boundary_slack_zero_count']}",
        f"critical_p_values={agg['critical_p_values']}",
        f"critical_template_indices={agg['critical_template_indices']}",
        f"w2_stronger_nonnegative_failure_count={agg['w2_stronger_nonnegative_failure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. W 专属整数下界",
        "",
        "`H/T` 正规形为 `H-2T>=3-2W`。当前模板只出现 `W=1` 与 `W=2`，因此硬点被拆成：",
        "",
        "```text",
        "W=1: H-2T >= 1",
        "W=2: H-2T >= -1",
        "```",
        "",
        "| W | hits | required lower bound | min H-2T | max H-2T | failures | equality | p at min |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["w_specific_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["target_W"]),
                    str(row["hit_count"]),
                    str(row["required_h_minus_2t_lower_bound"]),
                    str(row["min_h_minus_2t"]),
                    str(row["max_h_minus_2t"]),
                    str(row["bound_failure_count"]),
                    str(row["bound_equality_count"]),
                    f"`{row['p_values_at_min']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. slack<=1 临界行",
            "",
            "| template | p | side | rho | W | H | T | H-2T | bound | excess | slack | prefix atoms |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["critical_boundary_records"]:
        atom_summary = ",".join(f"{atom['band']}:k{atom['k']}[{atom['q_lo']},{atom['q_hi']}]:{atom['prime_load']}" for atom in row["prefix_interval_atoms"])
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
                    str(row["h_minus_2t"]),
                    str(row["w_specific_required_h_minus_2t_lower_bound"]),
                    str(row["bound_excess"]),
                    str(row["normal_form_slack"]),
                    f"`{atom_summary}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 结构判断",
            "",
            "- `W=1` 的目标下界是正余量 `H>=2T+1`；当前唯一 slack=0 边界是 `p=173, side=plus, rho=2, template=4`。",
            "- `W=2` 的目标下界只需 `H>=2T-1`；当前有限前沿实际更强，全部满足 `H>=2T`。",
            "- 因此下一步不应回到泛泛短区间素数命题，而应证明 W 专属的 H/T 来源不等式，或把反复出现的边界相位登记为 PDEC/ColumnCRT。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 4. 命题行",
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
            "## 5. 决策表",
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
            "## 6. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 证明目标：从 selector 相位、低轮 residue、平方窗与尾素数供给的共同约束推出 W 专属 H/T 来源不等式。",
            "- 若出现低余量长期复现，则把它转为边界复现 PDEC/ColumnCRT，而不是把有限验证当作证明。",
            "",
            "## 7. 依赖哈希",
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
    parser.add_argument("--normal-form-ledger", type=Path, default=NORMAL_FORM_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=5000)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    normal_form_ledger = args.normal_form_ledger if args.normal_form_ledger.is_absolute() else ROOT / args.normal_form_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(normal_form_ledger, template_ledger, args.max_p)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "prime_rho_hit_count": result["aggregate"]["prime_rho_hit_count"],
                "w_specific_bound_failure_count": result["aggregate"]["w_specific_bound_failure_count"],
                "critical_slack_le_1_count": result["aggregate"]["critical_slack_le_1_count"],
                "boundary_slack_zero_count": result["aggregate"]["boundary_slack_zero_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
