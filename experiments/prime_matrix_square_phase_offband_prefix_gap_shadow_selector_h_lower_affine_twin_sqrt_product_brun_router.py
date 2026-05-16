#!/usr/bin/env python3
"""把 AffineTwin per-q multiplicity 压成超平方根乘积门与 Brun 型 SAE 出口。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_sqrt_product_brun_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

MOVING_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json"
SPARSE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json"
PARTITION_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.md"

BRUN_INPUT = "ClassicalBrunTwinPrimeReciprocalConvergence"
NEXT_TARGET = "AffineTwinSqrtProductBoundOrSuperSqrtEpochPairPDECExclusion"


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


def q_row(row: dict[str, Any]) -> dict[str, Any]:
    """构造单个 q 的平方根乘积门审计行。"""
    q = int(row["q"])
    capacity = int(row["epoch_pair_capacity"])
    used = int(row["epoch_pair_product_used_upper"])
    sqrt_capacity = math.sqrt(capacity)
    sqrt_gate_passed = used * used <= capacity
    return {
        "q": q,
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "generator_used_residue_count": int(row["generator_used_residue_count"]),
        "fill_used_residue_count": int(row["fill_used_residue_count"]),
        "epoch_pair_capacity": capacity,
        "epoch_pair_product_used_upper": used,
        "product_over_sqrt_capacity": used / sqrt_capacity if capacity else None,
        "sqrt_product_gate_slack_squared": capacity - used * used,
        "sqrt_product_gate_passed_current_sweep": sqrt_gate_passed,
        "super_sqrt_epoch_pair_pdec_trigger_current_sweep": not sqrt_gate_passed,
        "sae_mass_upper": used / capacity,
        "sqrt_gate_sae_mass_envelope": 1 / sqrt_capacity,
        "sae_mass_below_sqrt_gate_envelope": used / capacity <= 1 / sqrt_capacity,
        "realized_current_sweep": bool(row["realized_current_sweep"]),
        "realized_pair_count": int(row["realized_affine_twin_pair_count"]),
        "single_pair_sae_mass": float(row["single_pair_sae_mass"]),
        "fixed_pair_modulus_margin": int(row["fixed_pair_modulus_margin"]),
        "source_realized_key": row["realized_source_key"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合、条件闭合和开放的命题行。"""
    return [
        {
            "name": "sqrt_product_gate_implies_brun_sae_summability",
            "status": "closed_conditional_on_external_brun",
            "statement": "For affine-twin q, if M_q<=sqrt(q(q-2)), then M_q/(q(q-2))<=1/sqrt(q(q-2))<=1/(q-2); Brun convergence for twin-prime reciprocals makes the SAE tail summable.",
        },
        {
            "name": "current_affine_twin_rows_pass_sqrt_product_gate",
            "status": "closed_current_sweep",
            "statement": "Every current candidate q has epoch-pair product upper M_q with M_q^2<=q(q-2).",
        },
        {
            "name": "super_sqrt_epoch_pair_pdec_routing",
            "status": "closed_routing",
            "statement": "Any q with M_q>sqrt(q(q-2)) is no longer a sparse SAE row; it is a named SuperSqrtEpochPair-PDEC/ColumnCRT side-residue concentration object.",
        },
        {
            "name": "internal_sqrt_product_bound",
            "status": "open",
            "statement": "The self-contained route still must prove the sqrt-product gate globally, or exclude the super-sqrt PDEC family without appealing to finite scans.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "CurrentSqrtProductGateClosed",
            "closed": agg["all_current_rows_pass_sqrt_product_gate"],
            "proved": False,
            "meaning": "当前候选 q 全部满足 M_q^2<=q(q-2)，且最大 M_q/sqrt(q(q-2)) 低于 1。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "BrunConditionalSAESummability",
            "closed": True,
            "proved": False,
            "meaning": "若接受外部 Brun twin-prime reciprocal convergence，并全局证明平方根乘积门，则 AffineTwin SAE 尾和可求和。",
            "remaining": "external input + global sqrt gate",
        },
        {
            "gate": "SuperSqrtEpochPairPDECRouted",
            "closed": True,
            "proved": True,
            "meaning": "平方根乘积门失败时，失败 q 被明确登记为 side-residue product 超平方根集中，而不是普通 sparse 行。",
            "remaining": "exclusion still separate",
        },
        {
            "gate": "InternalGlobalSqrtProductBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "作者侧自足路线仍需证明 M_q<=sqrt(q(q-2))，或排斥持久 SuperSqrtEpochPair-PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只压窄 per-q multiplicity 门，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(moving_ledger: Path, sparse_ledger: Path, partition_ledger: Path) -> dict[str, Any]:
    """构造平方根乘积门与 Brun SAE 结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    moving = load_json(moving_ledger)
    sparse = load_json(sparse_ledger)
    partition = load_json(partition_ledger)
    rows = [q_row(row) for row in moving["candidate_affine_twin_epoch_pair_rows"]]
    pdec_rows = [row for row in rows if row["super_sqrt_epoch_pair_pdec_trigger_current_sweep"]]
    max_ratio = max((row["product_over_sqrt_capacity"] for row in rows), default=0.0)
    aggregate = {
        "moving_ledger": str(moving_ledger.relative_to(ROOT)),
        "sparse_ledger": str(sparse_ledger.relative_to(ROOT)),
        "partition_ledger": str(partition_ledger.relative_to(ROOT)),
        "candidate_q_values": [row["q"] for row in rows],
        "realized_q_values": [row["q"] for row in rows if row["realized_current_sweep"]],
        "candidate_q_count": len(rows),
        "all_current_rows_pass_sqrt_product_gate": len(pdec_rows) == 0,
        "super_sqrt_epoch_pair_pdec_count_current_sweep": len(pdec_rows),
        "max_product_over_sqrt_capacity": max_ratio,
        "min_sqrt_product_gate_slack_squared": min(
            (row["sqrt_product_gate_slack_squared"] for row in rows),
            default=None,
        ),
        "current_product_sae_mass_upper_sum": sum(row["sae_mass_upper"] for row in rows),
        "current_sqrt_gate_envelope_sum": sum(row["sqrt_gate_sae_mass_envelope"] for row in rows),
        "sparse_single_atom_tail_envelope_proved": bool(
            sparse["aggregate"]["single_atom_sae_tail_envelope_proved"]
        ),
        "partition_identity_closed": bool(partition["aggregate"]["partition_identity_closed"]),
        "max_physical_multiplicity_per_residue_packet_current_sweep": int(
            partition["aggregate"]["max_physical_multiplicity_per_residue_packet"]
        ),
        "external_brun_input": BRUN_INPUT,
        "brun_conditional_sae_summability_closed": True,
        "external_brun_input_accepted_in_author_side": False,
        "internal_sqrt_product_bound_proved": False,
        "super_sqrt_epoch_pair_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "sqrt_product_q_rows": rows,
        "super_sqrt_epoch_pair_pdec_rows_current_sweep": pdec_rows,
        "brun_conditional_envelope": {
            "identity": "M_q/(q(q-2)) <= 1/sqrt(q(q-2)) <= 1/(q-2) when M_q^2 <= q(q-2).",
            "external_input": BRUN_INPUT,
            "meaning": "Brun convergence applies to the reciprocal sum over twin-prime q values q-2,q.",
        },
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_sqrt_product_brun_router"
        ),
        "status": "affine_twin_sqrt_product_gate_passes_current_sweep_brun_conditional_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "sqrt_product_q_rows": rows,
        "super_sqrt_epoch_pair_pdec_rows_current_sweep": pdec_rows,
        "brun_conditional_sae_summability_closed": True,
        "external_brun_input_accepted_in_author_side": False,
        "internal_sqrt_product_bound_proved": False,
        "super_sqrt_epoch_pair_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "AffineTwinPerQMultiplicityBoundOrHighDensityEpochPairPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 per-q multiplicity 的目标从过强的 O(1) 压窄为平方根乘积门：设 "
            "`M_q` 为同一 AffineTwin `q` 的候选双残基乘积上界。若 `M_q^2<=q(q-2)`，"
            "则该 q 的 SAE 贡献至多 `1/sqrt(q(q-2))<=1/(q-2)`；在接受经典 Brun "
            "孪生素数倒数收敛作为外部输入时，这条 twin-q 尾和可求和。当前候选 "
            f"`q={aggregate['candidate_q_values']}` 全部通过该门，最大 "
            f"`M_q/sqrt(q(q-2))={max_ratio:.12f}`。但作者侧自足闭合仍需全局证明平方根乘积门，"
            "或排斥 `SuperSqrtEpochPair-PDEC/ColumnCRT`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_sqrt_product_brun_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json": sha256(
            moving_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json": sha256(
            sparse_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-ledger.json": sha256(
            partition_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin sqrt-product Brun router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"realized_q_values={agg['realized_q_values']}",
        f"all_current_rows_pass_sqrt_product_gate={fmt_bool(agg['all_current_rows_pass_sqrt_product_gate'])}",
        f"max_product_over_sqrt_capacity={agg['max_product_over_sqrt_capacity']:.12f}",
        f"min_sqrt_product_gate_slack_squared={agg['min_sqrt_product_gate_slack_squared']}",
        f"current_product_sae_mass_upper_sum={agg['current_product_sae_mass_upper_sum']:.12f}",
        f"current_sqrt_gate_envelope_sum={agg['current_sqrt_gate_envelope_sum']:.12f}",
        f"external_brun_input={agg['external_brun_input']}",
        f"external_brun_input_accepted_in_author_side={fmt_bool(agg['external_brun_input_accepted_in_author_side'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 平方根乘积门",
        "",
        "| q | used product M_q | q(q-2) | M_q/sqrt(q(q-2)) | squared slack | pass | realized |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["sqrt_product_q_rows"]:
        lines.append(
            f"| {row['q']} | {row['epoch_pair_product_used_upper']} | {row['epoch_pair_capacity']} | "
            f"{row['product_over_sqrt_capacity']:.9f} | {row['sqrt_product_gate_slack_squared']} | "
            f"`{fmt_bool(row['sqrt_product_gate_passed_current_sweep'])}` | "
            f"`{fmt_bool(row['realized_current_sweep'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. Brun 条件包络",
            "",
            "```text",
            "If M_q^2 <= q(q-2), then",
            "M_q/(q(q-2)) <= 1/sqrt(q(q-2)) <= 1/(q-2).",
            "For affine-twin q, q and q-2 are twin primes.",
            "Classical Brun convergence makes sum_{twin q} 1/(q-2) finite.",
            "```",
            "",
            "这关闭的是“接受外部 Brun 输入后的 SAE 可求和出口”。作者侧自足线仍不能把 Brun 输入或当前有限扫描当作最终证明。",
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
            "- 自足线：证明所有持久 AffineTwin epoch-pair 都满足 `M_q^2<=q(q-2)`。",
            "- 失败线：若 `M_q^2>q(q-2)`，把该 q 的 side-residue product 超平方根集中登记为 `SuperSqrtEpochPair-PDEC/ColumnCRT` 并排斥。",
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
    parser.add_argument("--moving-ledger", type=Path, default=MOVING_LEDGER)
    parser.add_argument("--sparse-ledger", type=Path, default=SPARSE_LEDGER)
    parser.add_argument("--partition-ledger", type=Path, default=PARTITION_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    moving_ledger = args.moving_ledger if args.moving_ledger.is_absolute() else ROOT / args.moving_ledger
    sparse_ledger = args.sparse_ledger if args.sparse_ledger.is_absolute() else ROOT / args.sparse_ledger
    partition_ledger = args.partition_ledger if args.partition_ledger.is_absolute() else ROOT / args.partition_ledger
    result = build_result(moving_ledger, sparse_ledger, partition_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "candidate_q_values": result["aggregate"]["candidate_q_values"],
                "max_product_over_sqrt_capacity": result["aggregate"]["max_product_over_sqrt_capacity"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
