#!/usr/bin/env python3
"""把 AffineTwin 平方根乘积门改写为两侧 residue 压力乘积门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_paired_side_pressure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SQRT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-router.md"

NEXT_TARGET = "AffineTwinPairedSidePressureBoundOrPressureProductPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def fraction_json(value: Fraction) -> dict[str, Any]:
    """把分数写成 JSON 友好格式。"""
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": float(value),
    }


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def pressure_row(row: dict[str, Any]) -> dict[str, Any]:
    """构造单个 q 的两侧压力乘积行。"""
    q = int(row["q"])
    g = int(row["generator_ell"])
    f = int(row["fill_ell"])
    gu = int(row["generator_used_residue_count"])
    fu = int(row["fill_used_residue_count"])
    generator_pressure = Fraction(gu * gu, g)
    fill_pressure = Fraction(fu * fu, f)
    paired_pressure = generator_pressure * fill_pressure
    gate_passed = paired_pressure <= 1
    bottleneck = "generator" if generator_pressure < fill_pressure else "fill"
    if generator_pressure == fill_pressure:
        bottleneck = "balanced"
    return {
        "q": q,
        "generator_ell": g,
        "fill_ell": f,
        "generator_used_residue_count": gu,
        "fill_used_residue_count": fu,
        "generator_side_pressure": fraction_json(generator_pressure),
        "fill_side_pressure": fraction_json(fill_pressure),
        "paired_side_pressure_product": fraction_json(paired_pressure),
        "paired_pressure_gate_passed_current_sweep": gate_passed,
        "pressure_product_pdec_trigger_current_sweep": not gate_passed,
        "generator_side_pressure_above_one": generator_pressure > 1,
        "fill_side_pressure_above_one": fill_pressure > 1,
        "one_sided_pressure_without_pair_collision": (
            (generator_pressure > 1 or fill_pressure > 1) and gate_passed
        ),
        "paired_pressure_bottleneck": bottleneck,
        "sqrt_product_gate_equivalent": gate_passed == bool(row["sqrt_product_gate_passed_current_sweep"]),
        "source_sqrt_product_ratio": float(row["product_over_sqrt_capacity"]),
        "realized_current_sweep": bool(row["realized_current_sweep"]),
        "realized_pair_count": int(row["realized_pair_count"]),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "sqrt_gate_equals_paired_side_pressure_gate",
            "status": "closed",
            "statement": "M_q^2<=q(q-2) is exactly (g_used^2/(q-2))*(f_used^2/q)<=1, so the hardpoint is a two-side synchronized residue-pressure product, not a raw atom count.",
        },
        {
            "name": "current_one_sided_pressure_does_not_collide",
            "status": "closed_current_sweep",
            "statement": "The current sweep has generator-side pressure above one for q=43 and q=103, but the paired fill-side pressure is small enough that no q violates the product gate.",
        },
        {
            "name": "pressure_product_pdec_routing",
            "status": "closed_routing",
            "statement": "If the paired product exceeds one, the failure is a named PressureProduct-PDEC/ColumnCRT object: adjacent twin epochs simultaneously carry too much compatible residue pressure.",
        },
        {
            "name": "global_paired_pressure_bound",
            "status": "open",
            "statement": "A self-contained proof still must show this paired pressure product is always <=1 for persistent AffineTwin atoms, or exclude the named PDEC family.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "SqrtGatePressureEquivalenceClosed",
            "closed": agg["all_sqrt_product_pressure_equivalences_closed"],
            "proved": True,
            "meaning": "平方根乘积门已精确改写为两侧 residue 压力乘积不超过 1。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentPressureProductGateClosed",
            "closed": agg["all_current_rows_pass_paired_pressure_gate"],
            "proved": False,
            "meaning": "当前候选 q 没有两侧压力同步碰撞；最大压力乘积低于 1。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "OneSidedPressureExplained",
            "closed": agg["one_sided_pressure_without_pair_collision_count"] > 0,
            "proved": False,
            "meaning": "样本中的高 generator 压力不是终端矛盾，因相邻 fill 压力不足以同步。",
            "remaining": "finite structural diagnosis",
        },
        {
            "gate": "PressureProductPDECRouted",
            "closed": True,
            "proved": True,
            "meaning": "若两侧压力乘积超过 1，失败形态已命名为相邻 twin epoch 的同步 residue 压力碰撞。",
            "remaining": "exclusion still separate",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把平方根门压成压力乘积门，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(sqrt_ledger: Path) -> dict[str, Any]:
    """构造两侧压力乘积门结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    sqrt_data = load_json(sqrt_ledger)
    rows = [pressure_row(row) for row in sqrt_data["sqrt_product_q_rows"]]
    pdec_rows = [row for row in rows if row["pressure_product_pdec_trigger_current_sweep"]]
    one_sided_rows = [row for row in rows if row["one_sided_pressure_without_pair_collision"]]
    max_pressure = max(
        (Fraction(row["paired_side_pressure_product"]["numerator"], row["paired_side_pressure_product"]["denominator"]) for row in rows),
        default=Fraction(0, 1),
    )
    aggregate = {
        "sqrt_product_ledger": str(sqrt_ledger.relative_to(ROOT)),
        "candidate_q_values": [row["q"] for row in rows],
        "realized_q_values": [row["q"] for row in rows if row["realized_current_sweep"]],
        "all_sqrt_product_pressure_equivalences_closed": all(
            row["sqrt_product_gate_equivalent"] for row in rows
        ),
        "all_current_rows_pass_paired_pressure_gate": len(pdec_rows) == 0,
        "pressure_product_pdec_count_current_sweep": len(pdec_rows),
        "one_sided_pressure_without_pair_collision_count": len(one_sided_rows),
        "one_sided_pressure_q_values": [row["q"] for row in one_sided_rows],
        "max_paired_side_pressure_product": fraction_json(max_pressure),
        "min_pressure_product_slack": fraction_json(Fraction(1, 1) - max_pressure),
        "paired_pressure_product_bound_proved_globally": False,
        "pressure_product_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "paired_side_pressure_rows": rows,
        "pressure_product_pdec_rows_current_sweep": pdec_rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_paired_side_pressure_router"
        ),
        "status": "affine_twin_sqrt_gate_rewritten_as_paired_side_pressure_product_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "paired_side_pressure_rows": rows,
        "pressure_product_pdec_rows_current_sweep": pdec_rows,
        "paired_pressure_product_bound_proved_globally": False,
        "pressure_product_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "AffineTwinSqrtProductBoundOrSuperSqrtEpochPairPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把平方根乘积门进一步内化为两侧 residue 压力乘积：令 "
            "`g=q-2`、`f=q`，`A_g,A_f` 为两侧已用 residue 数，则 "
            "`M_q^2<=q(q-2)` 等价于 `(A_g^2/g)*(A_f^2/f)<=1`。"
            f"当前最大压力乘积为 {float(max_pressure):.12f}，"
            f"单侧高压但未同步碰撞的 q 为 {aggregate['one_sided_pressure_q_values']}。"
            "因此新的最窄硬点不是单侧 residue 多，而是相邻 twin epochs 两侧压力同步超过 1；"
            "若出现则登记为 `PressureProduct-PDEC/ColumnCRT`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_paired_side_pressure_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json": sha256(
            sqrt_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    max_pressure = agg["max_paired_side_pressure_product"]
    slack = agg["min_pressure_product_slack"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin paired side pressure router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"realized_q_values={agg['realized_q_values']}",
        f"all_sqrt_product_pressure_equivalences_closed={fmt_bool(agg['all_sqrt_product_pressure_equivalences_closed'])}",
        f"all_current_rows_pass_paired_pressure_gate={fmt_bool(agg['all_current_rows_pass_paired_pressure_gate'])}",
        f"max_paired_side_pressure_product={max_pressure['numerator']}/{max_pressure['denominator']} ~= {max_pressure['decimal']:.12f}",
        f"min_pressure_product_slack={slack['numerator']}/{slack['denominator']} ~= {slack['decimal']:.12f}",
        f"one_sided_pressure_q_values={agg['one_sided_pressure_q_values']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压力乘积表",
        "",
        "| q | gen pressure | fill pressure | product | bottleneck | one-sided high | pass |",
        "| ---: | ---: | ---: | ---: | --- | ---: | ---: |",
    ]
    for row in result["paired_side_pressure_rows"]:
        gen = row["generator_side_pressure"]
        fill = row["fill_side_pressure"]
        product = row["paired_side_pressure_product"]
        lines.append(
            f"| {row['q']} | `{gen['numerator']}/{gen['denominator']}` ~= {gen['decimal']:.6f} | "
            f"`{fill['numerator']}/{fill['denominator']}` ~= {fill['decimal']:.6f} | "
            f"`{product['numerator']}/{product['denominator']}` ~= {product['decimal']:.6f} | "
            f"`{row['paired_pressure_bottleneck']}` | "
            f"`{fmt_bool(row['one_sided_pressure_without_pair_collision'])}` | "
            f"`{fmt_bool(row['paired_pressure_gate_passed_current_sweep'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 精确等价",
            "",
            "```text",
            "M_q = A_g A_f, g=q-2, f=q.",
            "M_q^2 <= gf",
            "iff (A_g^2/g) * (A_f^2/f) <= 1.",
            "```",
            "",
            "这说明单侧 residue 压力偏高还不足以产生反例链；必须与相邻 twin epoch 的另一侧压力同步，才会破坏平方根乘积门。",
            "",
            "## 3. 命题行",
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
            "- 具体目标：证明相邻 twin epochs 的两侧 residue 压力不能同步超过 1。",
            "- 失败形态：若同步超过 1，则输出 `PressureProduct-PDEC/ColumnCRT`，再用相位/列 CRT 约束排斥。",
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
    parser.add_argument("--sqrt-ledger", type=Path, default=SQRT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sqrt_ledger = args.sqrt_ledger if args.sqrt_ledger.is_absolute() else ROOT / args.sqrt_ledger
    result = build_result(sqrt_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    max_pressure = result["aggregate"]["max_paired_side_pressure_product"]
    print(
        json.dumps(
            {
                "status": result["status"],
                "candidate_q_values": result["aggregate"]["candidate_q_values"],
                "max_paired_side_pressure_product_decimal": max_pressure["decimal"],
                "one_sided_pressure_q_values": result["aggregate"]["one_sided_pressure_q_values"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
