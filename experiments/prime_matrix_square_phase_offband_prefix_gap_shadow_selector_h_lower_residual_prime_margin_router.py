#!/usr/bin/env python3
"""把 residual prime-pair 上界压成单等号原子与 12 跳跃余量。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-router.md
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

ABSORBER_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-router.md"

ABSORBER_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_highfactor_absorber_router.py"
)

MAIN_TARGET = "ResidualPrimePairBoundOrHighFactorAbsorberPDEC"
NEXT_TARGET = "ResidualPrimePairSingleEqualityAtomOrMarginJumpPDEC"


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


def enrich_margin_rows(max_p: int, template_ledger: Path, target_h_coeff: float) -> list[dict[str, Any]]:
    """重放高因子吸收行并加入 residual prime margin。"""
    absorber = load_module(ABSORBER_ROUTER, "residual_prime_margin_absorber")
    rows = absorber.enrich_absorber_rows(max_p, template_ledger, target_h_coeff)
    enriched = []
    for row in rows:
        margin = int(row["small_sieve_357_residual_bound"]) - int(row["residual_prime_pair_count"])
        enriched.append(
            {
                **row,
                "residual_prime_pair_margin_to_bound": margin,
                "residual_prime_pair_margin_exact": margin == 0,
                "residual_prime_pair_margin_failure": margin < 0,
            }
        )
    return enriched


def side_rho_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 side/rho 汇总 residual prime margin。"""
    grouped: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault((str(row["side"]), int(row["rho"])), []).append(row)
    records = []
    for (side, rho), items in sorted(grouped.items()):
        min_margin = min(int(row["residual_prime_pair_margin_to_bound"]) for row in items)
        records.append(
            {
                "side": side,
                "rho": rho,
                "hit_count": len(items),
                "failure_count": sum(1 for row in items if int(row["residual_prime_pair_margin_to_bound"]) < 0),
                "exact_count": sum(1 for row in items if int(row["residual_prime_pair_margin_to_bound"]) == 0),
                "min_margin": min_margin,
                "p_values_at_min_margin": sorted(
                    {int(row["p"]) for row in items if int(row["residual_prime_pair_margin_to_bound"]) == min_margin}
                ),
            }
        )
    return records


def margin_histogram(rows: list[dict[str, Any]]) -> dict[str, int]:
    """余量直方图。"""
    counts = Counter(int(row["residual_prime_pair_margin_to_bound"]) for row in rows)
    return {str(key): counts[key] for key in sorted(counts)}


def tight_examples(rows: list[dict[str, Any]], limit: int = 24) -> list[dict[str, Any]]:
    """列出 residual prime margin 最紧样本。"""
    selected = sorted(
        rows,
        key=lambda row: (
            int(row["residual_prime_pair_margin_to_bound"]),
            int(row["p"]),
            row["side"],
            int(row["rho"]),
            int(row["template_index"]),
        ),
    )
    keys = [
        "template_index",
        "p",
        "side",
        "rho",
        "failure_loaded_b_breakpoint",
        "loaded_b_layers",
        "small_sieve_357_residual_bound",
        "residual_prime_pair_count",
        "residual_prime_pair_margin_to_bound",
        "small_sieve_357_residual_cap_count",
        "highfactor_composite_absorber_count",
        "small_sieve_357_residual_surplus_to_bound",
    ]
    return [{key: row[key] for key in keys} for row in selected[:limit]]


def equality_atom_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """登记等号原子。"""
    exact = [row for row in rows if int(row["residual_prime_pair_margin_to_bound"]) == 0]
    return tight_examples(exact, limit=len(exact))


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "residual_prime_pair_margin_form",
            "status": "closed",
            "statement": "The residual prime-pair safety condition is equivalent to margin=Bcrit-1-residual_prime_pair_count >=0.",
        },
        {
            "name": "finite_single_equality_atom_and_margin_jump",
            "status": "closed_on_current_sweep",
            "statement": "On the current P>=2001 sweep there is exactly one equality atom, P=2467 minus rho=7; after removing it, the minimum margin jumps to 12.",
        },
        {
            "name": "global_single_equality_atom_exclusion",
            "status": "open",
            "statement": "A global proof must show residual prime-pair margin remains positive away from nonpersistent equality atoms, or route equality persistence to PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "ResidualPrimePairMarginFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "真素对残余上界已改写为 margin>=0。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentResidualPrimeBoundHasNoFailure",
            "closed": agg["residual_prime_pair_margin_failure_count_at_p0"] == 0,
            "proved": False,
            "meaning": "有限重放中没有真素对残余超界。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentSingleEqualityAtomRegistered",
            "closed": agg["residual_prime_pair_margin_exact_count_at_p0"] == 1,
            "proved": False,
            "meaning": "有限重放中唯一等号原子已登记。",
            "remaining": "finite equality atom",
        },
        {
            "gate": "CurrentNonEqualityMarginJumpObserved",
            "closed": agg["min_margin_after_removing_exact_atoms_at_p0"] >= 12,
            "proved": False,
            "meaning": "排除等号原子后，有限重放最小余量跳到 12。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalEqualityAtomPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排斥等号原子持久复现，或给出 margin 正下界。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把真素对残余上界压成单等号原子与余量跳跃。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(absorber_ledger: Path, template_ledger: Path, max_p: int, p0: int, target_h_coeff: float) -> dict[str, Any]:
    """构造 residual prime margin 结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(absorber_ledger)
    rows = enrich_margin_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    exact_rows = [row for row in selected if int(row["residual_prime_pair_margin_to_bound"]) == 0]
    nonexact = [row for row in selected if int(row["residual_prime_pair_margin_to_bound"]) != 0]
    aggregate = {
        "absorber_ledger": str(absorber_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "selected_hit_count_at_p0": len(selected),
        "previous_residual_prime_pair_bound_failure_count_at_p0": source["aggregate"][
            "residual_prime_pair_bound_failure_count_at_p0"
        ],
        "residual_prime_pair_margin_failure_count_at_p0": sum(
            1 for row in selected if int(row["residual_prime_pair_margin_to_bound"]) < 0
        ),
        "residual_prime_pair_margin_exact_count_at_p0": len(exact_rows),
        "min_residual_prime_pair_margin_at_p0": min(
            int(row["residual_prime_pair_margin_to_bound"]) for row in selected
        ),
        "min_margin_after_removing_exact_atoms_at_p0": min(
            int(row["residual_prime_pair_margin_to_bound"]) for row in nonexact
        ),
        "single_equality_atom_p_values_at_p0": sorted({int(row["p"]) for row in exact_rows}),
        "global_residual_prime_pair_margin_proved": False,
        "equality_atom_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
        },
        "aggregate": aggregate,
        "side_rho_records": side_rho_records(selected),
        "equality_atom_records": equality_atom_records(selected),
        "tight_examples": tight_examples(selected),
        "margin_histogram": margin_histogram(selected),
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router",
        "status": "residual_prime_pair_bound_reduced_to_single_equality_atom_margin_jump_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_margin_jump_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "side_rho_records": ledger["side_rho_records"],
        "equality_atom_records": ledger["equality_atom_records"],
        "tight_examples": ledger["tight_examples"],
        "margin_histogram": ledger["margin_histogram"],
        "global_residual_prime_pair_margin_proved": False,
        "equality_atom_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_highfactor_absorber_router.py": sha256(
                ABSORBER_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-ledger.json": sha256(
                absorber_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 residual prime-pair 上界压成余量形式："
            "`margin=Bcrit-1-residual_prime_pair_count`。"
            f"当前 `P>={p0}` 重放中失败数为 {aggregate['residual_prime_pair_margin_failure_count_at_p0']}，"
            f"等号原子数为 {aggregate['residual_prime_pair_margin_exact_count_at_p0']}；"
            f"唯一等号原子是 `P={aggregate['single_equality_atom_p_values_at_p0'][0]}`，"
            f"排除等号后最小余量跳到 {aggregate['min_margin_after_removing_exact_atoms_at_p0']}。"
            "严格闭合还需证明等号原子不能持久复现，或建立全局正余量下界。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower residual prime margin router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"residual_prime_pair_margin_failure_count_at_p0={agg['residual_prime_pair_margin_failure_count_at_p0']}",
        f"residual_prime_pair_margin_exact_count_at_p0={agg['residual_prime_pair_margin_exact_count_at_p0']}",
        f"min_residual_prime_pair_margin_at_p0={agg['min_residual_prime_pair_margin_at_p0']}",
        f"min_margin_after_removing_exact_atoms_at_p0={agg['min_margin_after_removing_exact_atoms_at_p0']}",
        f"single_equality_atom_p_values_at_p0={agg['single_equality_atom_p_values_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 余量形式",
        "",
        "```text",
        "margin = Bcrit - 1 - residual_prime_pair_count",
        "safe <=> margin >= 0",
        "exact atom <=> margin = 0",
        "```",
        "",
        "## 2. side/rho 汇总",
        "",
        "| side | rho | hits | failures | exact | min margin | p at min |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["side_rho_records"]:
        lines.append(
            f"| `{row['side']}` | {row['rho']} | {row['hit_count']} | {row['failure_count']} | "
            f"{row['exact_count']} | {row['min_margin']} | `{row['p_values_at_min_margin']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 等号原子",
            "",
            "| p | side | rho | Bcrit | Good | bound | prime pairs | margin | residual | highfactor |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["equality_atom_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["failure_loaded_b_breakpoint"]),
                    str(row["loaded_b_layers"]),
                    str(row["small_sieve_357_residual_bound"]),
                    str(row["residual_prime_pair_count"]),
                    str(row["residual_prime_pair_margin_to_bound"]),
                    str(row["small_sieve_357_residual_cap_count"]),
                    str(row["highfactor_composite_absorber_count"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 最紧样本",
            "",
            "| margin | p | side | rho | template | bound | prime pairs | residual | highfactor |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["tight_examples"][:14]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["residual_prime_pair_margin_to_bound"]),
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["template_index"]),
                    str(row["small_sieve_357_residual_bound"]),
                    str(row["residual_prime_pair_count"]),
                    str(row["small_sieve_357_residual_cap_count"]),
                    str(row["highfactor_composite_absorber_count"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 结构判断",
            "",
            "- 当前有限段没有 residual prime-pair 超界。",
            "- 唯一等号原子为 `P=2467, minus, rho=7`；排除它后最小余量为 `12`，没有 1 到 11 的近失效层。",
            "- 这把剩余硬点压成：证明等号原子不持久，或给出全局 margin 正下界。",
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
            "- 具体目标：排斥 `P=2467` 型 residual-prime 等号相位持久复现，或建立全局正 margin 下界。",
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
    parser.add_argument("--absorber-ledger", type=Path, default=ABSORBER_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    absorber_ledger = args.absorber_ledger if args.absorber_ledger.is_absolute() else ROOT / args.absorber_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(absorber_ledger, template_ledger, args.max_p, args.p0, args.target_h_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "residual_prime_pair_margin_failure_count_at_p0": result["aggregate"][
                    "residual_prime_pair_margin_failure_count_at_p0"
                ],
                "residual_prime_pair_margin_exact_count_at_p0": result["aggregate"][
                    "residual_prime_pair_margin_exact_count_at_p0"
                ],
                "min_margin_after_removing_exact_atoms_at_p0": result["aggregate"][
                    "min_margin_after_removing_exact_atoms_at_p0"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
