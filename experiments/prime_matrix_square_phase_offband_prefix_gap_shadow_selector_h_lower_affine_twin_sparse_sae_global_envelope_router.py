#!/usr/bin/env python3
"""把 AffineTwin SparseSAE 拆成单原子可求和包络与 multiplicity 剩余门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_sparse_sae_global_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-router.md
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

MULTIPLICITY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-router.md"

NEXT_TARGET = "AffineTwinPerQMultiplicityBoundOrHighDensityEpochPairPDECExclusion"


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


def odd_floor(value: int) -> int:
    """返回不小于 value 的奇数下界。"""
    return value if value % 2 == 1 else value + 1


def odd_tail_sum(first_odd_q: int) -> Fraction:
    """计算 sum_{odd q>=first} 1/(q(q-2)) 的望远镜上界。"""
    q0 = odd_floor(first_odd_q)
    if q0 < 5:
        q0 = 5
    return Fraction(1, 2 * (q0 - 2))


def row_envelope(row: dict[str, Any]) -> dict[str, Any]:
    """构造单行 SAE 包络。"""
    q = int(row["q"])
    single = Fraction(1, q * (q - 2))
    return {
        "q": q,
        "realized_current_sweep": bool(row["realized_current_sweep"]),
        "realized_pair_count": int(row["realized_pair_count"]),
        "single_pair_sae_mass": fraction_json(single),
        "matches_recorded_single_pair_mass": abs(float(single) - float(row["single_pair_sae_mass"])) < 1e-18,
        "occupancy_upper_ratio": float(row["occupancy_upper_ratio"]),
        "eta": float(row["eta"]),
        "sparse_eta_gate_passed_current_sweep": bool(row["occupancy_below_eta"]),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "affine_twin_single_atom_sae_tail_envelope",
            "status": "closed",
            "statement": "For odd q>=Q, sum 1/(q(q-2)) is bounded by the telescoping tail 1/(2(Q-2)); affine-twin q values form a subset of these odd q.",
        },
        {
            "name": "eta_sparse_alone_not_global_summability",
            "status": "closed_diagnostic",
            "statement": "The eta sparse gate alone permits O(eta q(q-2)) atoms at each q; without a per-q multiplicity/decay bound this does not yield a summable global SAE family.",
        },
        {
            "name": "per_q_multiplicity_or_high_density_pdec",
            "status": "open",
            "statement": "A global proof must show O(1) or decaying affine-twin atoms per q, or route excess multiplicity to HighDensityEpochPair-PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "SingleAtomSAETailEnvelopeClosed",
            "closed": True,
            "proved": True,
            "meaning": "单固定双槽原子的 SAE 质量全局可求和，且不依赖孪生素数输入。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentRealizedSAEWithinFrontierTail",
            "closed": agg["current_realized_sae_mass_below_frontier_tail"],
            "proved": False,
            "meaning": "当前实现质量低于 q>=当前前沿的望远镜尾和。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "EtaSparseAloneSufficientForGlobalSummability",
            "closed": False,
            "proved": False,
            "meaning": "eta 稀疏本身不足以推出全局可求和；还需要每 q multiplicity 控制。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "HighDensityEpochPairPDECRouted",
            "closed": True,
            "proved": True,
            "meaning": "multiplicity 过大时仍回流 HighDensityEpochPair-PDEC/ColumnCRT。",
            "remaining": "exclusion still separate",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭单原子求和包络，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(multiplicity_ledger: Path) -> dict[str, Any]:
    """构造 SparseSAE 全局包络结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    multiplicity = load_json(multiplicity_ledger)
    rows = [row_envelope(row) for row in multiplicity["affine_twin_epoch_pair_multiplicity_rows"]]
    q_values = [row["q"] for row in rows]
    realized_q_values = [row["q"] for row in rows if row["realized_current_sweep"]]
    q_floor_current = min(q_values) if q_values else 31
    universal_tail = odd_tail_sum(5)
    frontier_tail = odd_tail_sum(q_floor_current)
    realized_mass = sum(
        Fraction(row["realized_pair_count"], row["q"] * (row["q"] - 2))
        for row in rows
    )
    candidate_single_mass = sum(
        Fraction(1, row["q"] * (row["q"] - 2))
        for row in rows
    )
    aggregate = {
        "multiplicity_ledger": str(multiplicity_ledger.relative_to(ROOT)),
        "candidate_q_values": q_values,
        "realized_q_values": realized_q_values,
        "current_frontier_q_floor": q_floor_current,
        "universal_single_atom_tail_from_q_ge_5": fraction_json(universal_tail),
        "frontier_single_atom_tail_from_min_candidate_q": fraction_json(frontier_tail),
        "candidate_single_pair_sae_mass_sum": fraction_json(candidate_single_mass),
        "current_realized_sae_mass": fraction_json(realized_mass),
        "current_realized_sae_mass_below_frontier_tail": realized_mass <= frontier_tail,
        "candidate_single_mass_below_frontier_tail": candidate_single_mass <= frontier_tail,
        "single_atom_sae_tail_envelope_proved": True,
        "eta_sparse_alone_summability_proved": False,
        "per_q_multiplicity_bound_proved": False,
        "high_density_epoch_pair_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "single_atom_sae_envelope_rows": rows,
        "diagnostic": {
            "why_eta_sparse_alone_is_not_enough": (
                "eta sparse allows up to eta*q*(q-2) atoms at a fixed q; each atom has "
                "mass 1/(q*(q-2)), so a saturated sparse q contributes about eta. "
                "Summing eta over infinitely many q is not summable without a per-q "
                "multiplicity decay, finite activation theorem, or HighDensity/PDEC exclusion."
            ),
            "telescoping_identity": "1/(q(q-2)) = (1/2)*(1/(q-2)-1/q) over odd q.",
        },
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_sparse_sae_global_envelope_router"
        ),
        "status": "single_atom_sae_tail_envelope_closed_per_q_multiplicity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "single_atom_sae_envelope_rows": rows,
        "single_atom_sae_tail_envelope_proved": True,
        "eta_sparse_alone_summability_proved": False,
        "per_q_multiplicity_bound_proved": False,
        "high_density_epoch_pair_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "AffineTwinSparseSAEGlobalBoundOrHighDensityEpochPairPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 SparseSAE 的真正可求和部分剥离出来：单个固定 AffineTwin 双槽原子的质量为 "
            "`1/(q(q-2))`，而奇数尾和满足望远镜恒等式，故所有 `q>=Q` 的单原子包络 "
            "`<=1/(2(Q-2))`。当前前沿 `Q=31` 时尾和为 "
            f"{float(frontier_tail):.12f}，当前实现质量为 {float(realized_mass):.12f}。"
            "但 `eta` 稀疏门本身不够推出全局可求和：若每个 q 都允许正比例多原子，总贡献可发散。"
            "因此最新硬点被精确压成每 q multiplicity 的 O(1)/衰减界，或 HighDensityEpochPair-PDEC 排斥。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_sparse_sae_global_envelope_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json": sha256(
            multiplicity_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    frontier_tail = agg["frontier_single_atom_tail_from_min_candidate_q"]
    universal_tail = agg["universal_single_atom_tail_from_q_ge_5"]
    realized = agg["current_realized_sae_mass"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin SparseSAE global envelope router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"realized_q_values={agg['realized_q_values']}",
        f"universal_single_atom_tail_from_q_ge_5={universal_tail['numerator']}/{universal_tail['denominator']} ~= {universal_tail['decimal']:.12f}",
        f"frontier_single_atom_tail_from_q_ge_{agg['current_frontier_q_floor']}={frontier_tail['numerator']}/{frontier_tail['denominator']} ~= {frontier_tail['decimal']:.12f}",
        f"current_realized_sae_mass={realized['numerator']}/{realized['denominator']} ~= {realized['decimal']:.12f}",
        f"single_atom_sae_tail_envelope_proved={fmt_bool(agg['single_atom_sae_tail_envelope_proved'])}",
        f"eta_sparse_alone_summability_proved={fmt_bool(agg['eta_sparse_alone_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 望远镜包络",
        "",
        "```text",
        "1/(q(q-2)) = (1/2) * (1/(q-2) - 1/q)",
        "sum over odd q >= Q is <= 1/(2(Q-2)).",
        "AffineTwin q values are a subset of these odd q.",
        "```",
        "",
        "## 2. 单原子质量",
        "",
        "| q | realized | single SAE mass | recorded match | sparse gate |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["single_atom_sae_envelope_rows"]:
        mass = row["single_pair_sae_mass"]
        lines.append(
            f"| {row['q']} | `{fmt_bool(row['realized_current_sweep'])}` | "
            f"`{mass['numerator']}/{mass['denominator']}` ~= {mass['decimal']:.9f} | "
            f"`{fmt_bool(row['matches_recorded_single_pair_mass'])}` | "
            f"`{fmt_bool(row['sparse_eta_gate_passed_current_sweep'])}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 关键边界",
            "",
            "- 单原子 SAE 可求和已经闭合；这是全局恒等式，不依赖有限扫描或孪生素数猜想。",
            "- `eta` 稀疏门不能单独闭合全局求和，因为每个 q 的正比例多原子会给出约 `eta` 的贡献。",
            "- 因此真正剩余不是再换命题，而是证明每 q 的 AffineTwin 原子数为 O(1)/有额外衰减，或把超额送入 HighDensityEpochPair-PDEC/ColumnCRT。",
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
            "- 具体目标：证明每个 q 的 AffineTwin 原子 multiplicity 为 O(1)/衰减；若失败，输出 HighDensityEpochPair-PDEC/ColumnCRT。",
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
    parser.add_argument("--multiplicity-ledger", type=Path, default=MULTIPLICITY_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    multiplicity_ledger = (
        args.multiplicity_ledger if args.multiplicity_ledger.is_absolute() else ROOT / args.multiplicity_ledger
    )
    result = build_result(multiplicity_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "frontier_tail_decimal": result["aggregate"][
                    "frontier_single_atom_tail_from_min_candidate_q"
                ]["decimal"],
                "current_realized_sae_mass_decimal": result["aggregate"]["current_realized_sae_mass"]["decimal"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
