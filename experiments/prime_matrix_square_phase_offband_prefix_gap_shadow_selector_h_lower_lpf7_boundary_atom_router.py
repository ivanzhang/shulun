#!/usr/bin/env python3
"""把小因子损耗阶梯压成 lpf<=7 主层加唯一边界补项原子。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_boundary_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SMALL_FACTOR_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-router.md"

MAIN_TARGET = "SelectorResidueCapSmallFactorLossFloorOrLargePrimeCompanionPersistencePDEC"
NEXT_TARGET = "LPF7MainLossFloorPlusBoundarySupplementOrBoundaryAtomPDEC"


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


def int_key_dict(raw: dict[str, Any]) -> dict[int, int]:
    """把 JSON 字符串键转为整数键。"""
    return {int(key): int(value) for key, value in raw.items()}


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "finite_lpf7_main_layer_all_but_one",
            "status": "closed_on_current_sweep",
            "statement": "On the current P>=2001 sweep, lpf(m)<=7 pays the required composite-loss floor for every selector row except the single boundary atom P=2467, minus, rho=7.",
        },
        {
            "name": "boundary_supplement_exact_payment",
            "status": "closed_on_current_sweep",
            "statement": "For the boundary atom, the lpf 11,13,17,23,43 supplement contributes exactly eight extra composite losses and closes the floor with zero surplus.",
        },
        {
            "name": "global_lpf7_main_plus_boundary_nonpersistence",
            "status": "open",
            "statement": "A global proof must establish the lpf<=7 main loss floor away from boundary atoms and prove boundary supplements cannot persist without PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "CurrentLPF7MainLayerIsolated",
            "closed": agg["lpf7_failure_count_at_p0"] == 1,
            "proved": False,
            "meaning": "有限重放中 lpf<=7 只剩一个边界原子。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentBoundarySupplementExact",
            "closed": agg["boundary_supplement_exact_payment"],
            "proved": False,
            "meaning": "唯一边界原子的 11..43 补项刚好补齐 8 个缺口。",
            "remaining": "finite boundary atom",
        },
        {
            "gate": "GlobalLPF7MainFloorProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 lpf<=7 主层损耗下界。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "BoundaryAtomPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明类似贴边补项不能无限复现，或登记并排斥为 PDEC/SAE。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把小因子阶梯压成主层加唯一边界原子。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(small_factor_ledger: Path) -> dict[str, Any]:
    """构造 lpf<=7 主层和边界补项结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(small_factor_ledger)
    agg = source["aggregate"]
    lpf7_record = next(item for item in source["threshold_summary"] if int(item["threshold"]) == 7)
    lpf43_record = next(item for item in source["threshold_summary"] if int(item["threshold"]) == 43)
    boundary = source["tight_examples"][0]
    histogram = int_key_dict(boundary["least_prime_factor_histogram"])
    main_lpf7_payment = sum(count for prime, count in histogram.items() if prime <= 7)
    supplement_histogram = {prime: count for prime, count in histogram.items() if 7 < prime <= 43}
    supplement_payment = sum(supplement_histogram.values())
    required_loss = int(boundary["required_composite_loss_for_breakpoint_safety"])
    boundary_deficit_after_lpf7 = required_loss - main_lpf7_payment
    boundary_supplement_exact = supplement_payment == boundary_deficit_after_lpf7
    unique_boundary_atom = {
        "p": boundary["p"],
        "side": boundary["side"],
        "rho": boundary["rho"],
        "template_index": boundary["template_index"],
        "Bcrit": boundary["failure_loaded_b_breakpoint"],
        "GoodShell": boundary["loaded_b_layers"],
        "cap_count": boundary["residue_cap_slot_count"],
        "required_loss": required_loss,
        "actual_loss": boundary["companion_composite_loss_count"],
        "loss_surplus": boundary["composite_loss_surplus_to_floor"],
        "main_lpf7_payment": main_lpf7_payment,
        "boundary_deficit_after_lpf7": boundary_deficit_after_lpf7,
        "supplement_histogram_11_to_43": supplement_histogram,
        "supplement_payment_11_to_43": supplement_payment,
        "boundary_supplement_exact_payment": boundary_supplement_exact,
    }
    result_aggregate = {
        "small_factor_ledger": str(small_factor_ledger.relative_to(ROOT)),
        "p0": agg["p0"],
        "max_p": agg["max_p"],
        "selected_hit_count_at_p0": agg["selected_hit_count_at_p0"],
        "lpf7_failure_count_at_p0": lpf7_record["failure_count_at_p0"],
        "lpf7_failure_p_values_sample": lpf7_record["failure_p_values_sample"],
        "lpf43_failure_count_at_p0": lpf43_record["failure_count_at_p0"],
        "zero_composite_loss_surplus_count_at_p0": agg["zero_composite_loss_surplus_count_at_p0"],
        "boundary_supplement_exact_payment": boundary_supplement_exact,
        "global_lpf7_main_floor_proved": False,
        "boundary_atom_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "source_ledger": str(small_factor_ledger.relative_to(ROOT)),
            "p0": agg["p0"],
            "max_p": agg["max_p"],
        },
        "aggregate": result_aggregate,
        "unique_boundary_atom": unique_boundary_atom,
        "source_threshold_summary": source["threshold_summary"],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_boundary_atom_router",
        "status": "small_factor_loss_ladder_reduced_to_lpf7_main_layer_plus_boundary_atom_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_boundary_atom_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": result_aggregate,
        "unique_boundary_atom": unique_boundary_atom,
        "global_lpf7_main_floor_proved": False,
        "boundary_atom_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_boundary_atom_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-ledger.json": sha256(
                small_factor_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把小因子损耗阶梯压成 `lpf(m)<=7` 主层加唯一边界补项。"
            "当前有限重放中，`lpf<=7` 只在 `P=2467, minus, rho=7` 一个贴边行不足；"
            "该行需要 28 个合数损耗，`lpf<=7` 支付 20 个，缺口 8 个，"
            "而 `11,13,17,23,43` 补项精确支付 8 个，最终余量仍为 0。"
            "这不是全局证明；严格闭合还需证明 lpf<=7 主层全局下界并排斥边界补项持久复现。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    atom = result["unique_boundary_atom"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower lpf7 boundary atom router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"selected_hit_count_at_p0={agg['selected_hit_count_at_p0']}",
        f"lpf7_failure_count_at_p0={agg['lpf7_failure_count_at_p0']}",
        f"lpf7_failure_p_values_sample={agg['lpf7_failure_p_values_sample']}",
        f"lpf43_failure_count_at_p0={agg['lpf43_failure_count_at_p0']}",
        f"boundary_supplement_exact_payment={fmt_bool(atom['boundary_supplement_exact_payment'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 唯一边界原子",
        "",
        "| p | side | rho | Bcrit | Good | cap | required loss | actual loss | lpf<=7 pay | deficit | supplement | loss surplus |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        f"| {atom['p']} | `{atom['side']}` | {atom['rho']} | {atom['Bcrit']} | {atom['GoodShell']} | "
        f"{atom['cap_count']} | {atom['required_loss']} | {atom['actual_loss']} | {atom['main_lpf7_payment']} | "
        f"{atom['boundary_deficit_after_lpf7']} | {atom['supplement_payment_11_to_43']} | {atom['loss_surplus']} |",
        "",
        "补项直方图：",
        "",
        "```json",
        json.dumps(atom["supplement_histogram_11_to_43"], ensure_ascii=False, sort_keys=True),
        "```",
        "",
        "## 2. 结构判断",
        "",
        "- 当前高段主层几乎完全由 `3,5,7` 三个小模支付。",
        "- 唯一不足处是贴边行，且补项没有余量；这正是需要排斥持久复现的边界原子。",
        "- 下一步不能把 `43` 当固定全局常数，而应证明 `lpf<=7` 主层的自适应 CRT 覆盖，并把边界补项作为 PDEC/SAE 守门项。",
        "",
        "## 3. 命题行",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 4. 决策表",
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
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体目标：证明 `lpf<=7` 主层小模 CRT 覆盖下界；若存在贴边补项复现，则登记为 BoundaryAtom-PDEC/SAE 并排斥。",
            "",
            "## 6. 依赖哈希",
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
    parser.add_argument("--small-factor-ledger", type=Path, default=SMALL_FACTOR_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    small_factor_ledger = (
        args.small_factor_ledger if args.small_factor_ledger.is_absolute() else ROOT / args.small_factor_ledger
    )
    result = build_result(small_factor_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "lpf7_failure_count_at_p0": result["aggregate"]["lpf7_failure_count_at_p0"],
                "boundary_atom": result["unique_boundary_atom"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
