#!/usr/bin/env python3
"""把 3/5/7 配额门改写为小筛残余 cap 上界。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_residual_cap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

LPF7_QUOTA_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-router.md"

LPF7_QUOTA_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_crt_quota_router.py"
)

MAIN_TARGET = "LPF7CRTQuotaLowerBoundOrBoundaryEqualityAtomPDEC"
NEXT_TARGET = "SmallSieve357ResidualCapBoundOrMinusQuotaAtomPDEC"


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


def enrich_residual_rows(max_p: int, template_ledger: Path, target_h_coeff: float) -> list[dict[str, Any]]:
    """重放 lpf7 配额行并加入 3/5/7 小筛残余字段。"""
    quota = load_module(LPF7_QUOTA_ROUTER, "residual_357_quota")
    rows = quota.enrich_quota_rows(max_p, template_ledger, target_h_coeff)
    enriched = []
    for row in rows:
        residual = int(row["residue_cap_slot_count"]) - int(row["lpf_le_7_loss_count"])
        bound = int(row["failure_loaded_b_breakpoint"]) - 1
        surplus = residual - bound
        enriched.append(
            {
                **row,
                "small_sieve_357_residual_cap_count": residual,
                "small_sieve_357_residual_bound": bound,
                "small_sieve_357_residual_surplus_to_bound": surplus,
                "small_sieve_357_bound_ok": surplus <= 0,
                "equivalent_lpf7_quota_surplus": -surplus,
            }
        )
    return enriched


def side_rho_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 side/rho 汇总残余上界。"""
    grouped: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault((str(row["side"]), int(row["rho"])), []).append(row)
    records = []
    for (side, rho), items in sorted(grouped.items()):
        max_surplus = max(int(row["small_sieve_357_residual_surplus_to_bound"]) for row in items)
        records.append(
            {
                "side": side,
                "rho": rho,
                "hit_count": len(items),
                "failure_count": sum(1 for row in items if int(row["small_sieve_357_residual_surplus_to_bound"]) > 0),
                "exact_count": sum(1 for row in items if int(row["small_sieve_357_residual_surplus_to_bound"]) == 0),
                "max_residual_surplus_to_bound": max_surplus,
                "p_values_at_max_surplus": sorted(
                    {
                        int(row["p"])
                        for row in items
                        if int(row["small_sieve_357_residual_surplus_to_bound"]) == max_surplus
                    }
                ),
            }
        )
    return records


def atom_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """登记残余失败/等号原子。"""
    atoms = [
        row
        for row in rows
        if int(row["small_sieve_357_residual_surplus_to_bound"]) >= 0
    ]
    selected = sorted(
        atoms,
        key=lambda row: (
            -int(row["small_sieve_357_residual_surplus_to_bound"]),
            int(row["p"]),
            row["side"],
            int(row["rho"]),
        ),
    )
    keys = [
        "template_index",
        "p",
        "side",
        "rho",
        "failure_loaded_b_breakpoint",
        "loaded_b_layers",
        "residue_cap_slot_count",
        "lpf_le_7_loss_count",
        "small_sieve_357_residual_cap_count",
        "small_sieve_357_residual_bound",
        "small_sieve_357_residual_surplus_to_bound",
        "lpf3_loss_count",
        "lpf5_loss_count",
        "lpf7_exact_loss_count",
    ]
    return [{key: row[key] for key in keys} for row in selected]


def tight_examples(rows: list[dict[str, Any]], limit: int = 16) -> list[dict[str, Any]]:
    """列出残余最接近或超过上界的样本。"""
    selected = sorted(
        rows,
        key=lambda row: (
            -int(row["small_sieve_357_residual_surplus_to_bound"]),
            int(row["p"]),
            row["side"],
            int(row["rho"]),
        ),
    )
    keys = [
        "template_index",
        "p",
        "side",
        "rho",
        "failure_loaded_b_breakpoint",
        "loaded_b_layers",
        "residue_cap_slot_count",
        "lpf_le_7_loss_count",
        "small_sieve_357_residual_cap_count",
        "small_sieve_357_residual_bound",
        "small_sieve_357_residual_surplus_to_bound",
        "equivalent_lpf7_quota_surplus",
    ]
    return [{key: row[key] for key in keys} for row in selected[:limit]]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "lpf7_quota_residual_equivalence",
            "status": "closed",
            "statement": "The lpf<=7 quota lower bound is equivalent to small_sieve_357_residual_cap_count <= Bcrit-1.",
        },
        {
            "name": "finite_residual_atoms",
            "status": "closed_on_current_sweep",
            "statement": "On the current P>=2001 sweep, the only residual surplus failure is P=2467 minus rho=7; residual equalities occur at P=5297 minus rho=2.",
        },
        {
            "name": "global_357_residual_cap_bound",
            "status": "open",
            "statement": "A global proof must bound the 3/5/7-sieved residual cap slots below Bcrit, or route minus-side boundary/equality atoms to PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "LPF7QuotaResidualEquivalenceClosed",
            "closed": True,
            "proved": True,
            "meaning": "`lpf<=7` 配额已等价改写为 3/5/7 小筛残余 cap 上界。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentResidualFailureIsBoundary",
            "closed": agg["residual_failure_count_at_p0"] == 1,
            "proved": False,
            "meaning": "有限重放中唯一残余超界是 P=2467 贴边原子。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentResidualEqualityAtomsRegistered",
            "closed": agg["residual_exact_count_at_p0"] == 2,
            "proved": False,
            "meaning": "有限重放中残余等号原子为 P=5297 的两条模板记录。",
            "remaining": "finite equality atoms",
        },
        {
            "gate": "Global357ResidualCapBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 3/5/7 小筛残余 cap 上界，或排斥 minus-side 原子持久复现。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把配额门改写成残余上界门。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(quota_ledger: Path, template_ledger: Path, max_p: int, p0: int, target_h_coeff: float) -> dict[str, Any]:
    """构造 3/5/7 小筛残余 cap 结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(quota_ledger)
    rows = enrich_residual_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    aggregate = {
        "quota_ledger": str(quota_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "selected_hit_count_at_p0": len(selected),
        "previous_lpf7_quota_failure_count_at_p0": source["aggregate"]["lpf7_quota_failure_count_at_p0"],
        "residual_failure_count_at_p0": sum(
            1 for row in selected if int(row["small_sieve_357_residual_surplus_to_bound"]) > 0
        ),
        "residual_exact_count_at_p0": sum(
            1 for row in selected if int(row["small_sieve_357_residual_surplus_to_bound"]) == 0
        ),
        "max_residual_surplus_to_bound_at_p0": max(
            int(row["small_sieve_357_residual_surplus_to_bound"]) for row in selected
        ),
        "max_residual_cap_count_at_p0": max(int(row["small_sieve_357_residual_cap_count"]) for row in selected),
        "global_357_residual_cap_bound_proved": False,
        "minus_atom_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "small_sieve_moduli": [3, 5, 7],
        },
        "aggregate": aggregate,
        "side_rho_records": side_rho_records(selected),
        "residual_atom_records": atom_records(selected),
        "tight_examples": tight_examples(selected),
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_residual_cap_router",
        "status": "lpf7_crt_quota_reduced_to_357_residual_cap_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_residual_atoms_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "side_rho_records": ledger["side_rho_records"],
        "residual_atom_records": ledger["residual_atom_records"],
        "tight_examples": ledger["tight_examples"],
        "global_357_residual_cap_bound_proved": False,
        "minus_atom_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_residual_cap_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_crt_quota_router.py": sha256(
                LPF7_QUOTA_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-ledger.json": sha256(
                quota_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 `lpf<=7` 配额下界改写成小筛残余 cap 上界："
            "`cap_count-lpf7_loss <= Bcrit-1`。"
            f"当前 `P>={p0}` 重放中唯一残余超界仍是 `P=2467, minus, rho=7`，"
            "残余等号原子是 `P=5297, minus, rho=2` 的两条模板记录；"
            "所有 plus 侧都有正安全余量。严格闭合还需全局证明 3/5/7 小筛残余 cap 上界，"
            "或排斥 minus-side 边界/等号原子持久复现。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower 357 residual cap router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"selected_hit_count_at_p0={agg['selected_hit_count_at_p0']}",
        f"residual_failure_count_at_p0={agg['residual_failure_count_at_p0']}",
        f"residual_exact_count_at_p0={agg['residual_exact_count_at_p0']}",
        f"max_residual_surplus_to_bound_at_p0={agg['max_residual_surplus_to_bound_at_p0']}",
        f"max_residual_cap_count_at_p0={agg['max_residual_cap_count_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 等价式",
        "",
        "```text",
        "lpf7_loss >= cap_count-Bcrit+1",
        "<=> cap_count-lpf7_loss <= Bcrit-1",
        "```",
        "",
        "左侧是小因子损耗下界，右侧是经过 `3/5/7` 小筛后的 residue-cap 残余槽上界。",
        "",
        "## 2. side/rho 汇总",
        "",
        "| side | rho | hits | failures | exact | max residual surplus | p at max |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["side_rho_records"]:
        lines.append(
            f"| `{row['side']}` | {row['rho']} | {row['hit_count']} | {row['failure_count']} | "
            f"{row['exact_count']} | {row['max_residual_surplus_to_bound']} | `{row['p_values_at_max_surplus']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 残余失败/等号原子",
            "",
            "| p | side | rho | Bcrit | Good | cap | lpf7 loss | residual | bound | surplus |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["residual_atom_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["failure_loaded_b_breakpoint"]),
                    str(row["loaded_b_layers"]),
                    str(row["residue_cap_slot_count"]),
                    str(row["lpf_le_7_loss_count"]),
                    str(row["small_sieve_357_residual_cap_count"]),
                    str(row["small_sieve_357_residual_bound"]),
                    str(row["small_sieve_357_residual_surplus_to_bound"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构判断",
            "",
            "- 现在的主硬点不是“有多少合数”，而是 `3/5/7` 小筛后还剩多少 cap 槽。",
            "- 当前所有硬原子都在 minus 侧；plus 侧有限重放有正余量。",
            "- 这一步直接适配层叠筛：下一步应证明小筛残余无法高于 `Bcrit-1`，或把 minus-side 原子登记为 PDEC。",
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
            "- 具体目标：证明 `3/5/7` 小筛残余 cap 上界；若 minus-side 边界/等号原子复现，则登记为 MinusQuotaAtom-PDEC/SAE 并排斥。",
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
    parser.add_argument("--quota-ledger", type=Path, default=LPF7_QUOTA_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    quota_ledger = args.quota_ledger if args.quota_ledger.is_absolute() else ROOT / args.quota_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(quota_ledger, template_ledger, args.max_p, args.p0, args.target_h_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "residual_failure_count_at_p0": result["aggregate"]["residual_failure_count_at_p0"],
                "residual_exact_count_at_p0": result["aggregate"]["residual_exact_count_at_p0"],
                "max_residual_surplus_to_bound_at_p0": result["aggregate"][
                    "max_residual_surplus_to_bound_at_p0"
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
