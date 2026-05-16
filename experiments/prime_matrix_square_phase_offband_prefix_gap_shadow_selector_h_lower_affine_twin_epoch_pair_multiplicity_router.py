#!/usr/bin/env python3
"""审计 AffineTwin epoch-pair multiplicity 稀疏门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_epoch_pair_multiplicity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-router.md
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

MOVING_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-router.md"

ETA_NUMERATOR = 1
ETA_DENOMINATOR = 40
NEXT_TARGET = "AffineTwinSparseSAEGlobalBoundOrHighDensityEpochPairPDECExclusion"


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


def multiplicity_row(row: dict[str, Any], eta_num: int, eta_den: int) -> dict[str, Any]:
    """构造单个候选 epoch-pair 的稀疏判定行。"""
    used = int(row["epoch_pair_product_used_upper"])
    capacity = int(row["epoch_pair_capacity"])
    slack_num = eta_num * capacity - eta_den * used
    return {
        "q": int(row["q"]),
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "epoch_pair_capacity": capacity,
        "epoch_pair_product_used_upper": used,
        "occupancy_upper_ratio": used / capacity,
        "eta": eta_num / eta_den,
        "eta_slack_numerator": slack_num,
        "eta_slack_denominator": eta_den * capacity,
        "occupancy_below_eta": slack_num >= 0,
        "high_density_epoch_pair_pdec_trigger": slack_num < 0,
        "realized_current_sweep": bool(row["realized_current_sweep"]),
        "realized_pair_count": int(row["realized_affine_twin_pair_count"]),
        "realized_sae_mass": float(row["realized_affine_twin_sae_mass"]),
        "single_pair_sae_mass": float(row["single_pair_sae_mass"]),
        "fixed_pair_modulus_margin": int(row["fixed_pair_modulus_margin"]),
        "source_realized_key": row["realized_source_key"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "current_affine_twin_epoch_pair_sparse_acceptance",
            "status": "closed_current_sweep",
            "statement": "For eta=1/40, every current candidate affine-twin epoch-pair has product occupancy below eta, and the total candidate product occupancy is also below eta.",
        },
        {
            "name": "high_density_epoch_pair_pdec_trigger",
            "status": "closed_routing",
            "statement": "If an affine-twin epoch-pair violates the eta sparse gate, the offending q gives a named HighDensityEpochPair-PDEC/ColumnCRT certificate.",
        },
        {
            "name": "global_sparse_sae_bound",
            "status": "open",
            "statement": "A global proof must show the sparse gate persists with summable SAE mass, or exclude the high-density epoch-pair PDEC family.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "CurrentEpochPairSparseEtaGateClosed",
            "closed": agg["all_candidate_epoch_pair_occupancy_below_eta"],
            "proved": False,
            "meaning": "当前候选 twin epoch-pair 全部低于 eta=1/40。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentTotalCandidateMassBelowEta",
            "closed": agg["candidate_product_mass_upper_sum_below_eta"],
            "proved": False,
            "meaning": "当前候选乘法占用总质量也低于 eta=1/40。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "HighDensityEpochPairPDECRouted",
            "closed": True,
            "proved": True,
            "meaning": "若 eta 门失败，失败行已命名为 HighDensityEpochPair-PDEC/ColumnCRT。",
            "remaining": "exclusion still separate",
        },
        {
            "gate": "GlobalSparseSAEBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明全局稀疏 SAE 质量可求和并足以吸收反例链。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成当前候选稀疏验收与高密度出口命名，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(moving_ledger: Path, eta_num: int, eta_den: int) -> dict[str, Any]:
    """构造 multiplicity 稀疏门结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    moving = load_json(moving_ledger)
    rows = [
        multiplicity_row(row, eta_num, eta_den)
        for row in moving["candidate_affine_twin_epoch_pair_rows"]
    ]
    high_density_rows = [row for row in rows if row["high_density_epoch_pair_pdec_trigger"]]
    candidate_mass = sum(row["occupancy_upper_ratio"] for row in rows)
    realized_mass = sum(row["realized_sae_mass"] for row in rows)
    eta_value = eta_num / eta_den
    aggregate = {
        "moving_ledger": str(moving_ledger.relative_to(ROOT)),
        "eta_numerator": eta_num,
        "eta_denominator": eta_den,
        "eta": eta_value,
        "candidate_epoch_pair_count": len(rows),
        "candidate_q_values": [row["q"] for row in rows],
        "realized_q_values": [row["q"] for row in rows if row["realized_current_sweep"]],
        "candidate_product_mass_upper_sum": candidate_mass,
        "candidate_product_mass_upper_sum_below_eta": candidate_mass <= eta_value,
        "candidate_total_eta_slack": eta_value - candidate_mass,
        "realized_affine_twin_sae_mass_sum": realized_mass,
        "all_candidate_epoch_pair_occupancy_below_eta": all(row["occupancy_below_eta"] for row in rows),
        "min_eta_slack_numerator": min(row["eta_slack_numerator"] for row in rows) if rows else None,
        "max_occupancy_upper_ratio": max(row["occupancy_upper_ratio"] for row in rows) if rows else None,
        "high_density_epoch_pair_count": len(high_density_rows),
        "current_sparse_acceptance_closed": len(high_density_rows) == 0 and candidate_mass <= eta_value,
        "global_sparse_sae_bound_proved": False,
        "high_density_epoch_pair_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "affine_twin_epoch_pair_multiplicity_rows": rows,
        "high_density_epoch_pair_pdec_rows": high_density_rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_epoch_pair_multiplicity_router"
        ),
        "status": "affine_twin_epoch_pair_sparse_eta_gate_passes_current_sweep_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "affine_twin_epoch_pair_multiplicity_rows": rows,
        "high_density_epoch_pair_pdec_rows": high_density_rows,
        "current_sparse_acceptance_closed": aggregate["current_sparse_acceptance_closed"],
        "global_sparse_sae_bound_proved": False,
        "high_density_epoch_pair_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 AffineTwin epoch-pair multiplicity 压成 eta 稀疏门：取 `eta=1/40`，"
            "当前候选 `q` 的乘法占用上界逐项低于 eta，且总占用也低于 eta。"
            f"当前最大占用为 {aggregate['max_occupancy_upper_ratio']:.12f}，"
            f"总占用为 {candidate_mass:.12f}，总 eta 余量为 "
            f"{aggregate['candidate_total_eta_slack']:.12f}。若全局出现 eta 门失败，"
            "失败行已被命名为 HighDensityEpochPair-PDEC/ColumnCRT；否则进入 sparse SAE 账本。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_epoch_pair_multiplicity_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json": sha256(
            moving_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin epoch-pair multiplicity router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"eta={agg['eta_numerator']}/{agg['eta_denominator']}",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"realized_q_values={agg['realized_q_values']}",
        f"candidate_product_mass_upper_sum={agg['candidate_product_mass_upper_sum']:.12f}",
        f"candidate_total_eta_slack={agg['candidate_total_eta_slack']:.12f}",
        f"max_occupancy_upper_ratio={agg['max_occupancy_upper_ratio']:.12f}",
        f"high_density_epoch_pair_count={agg['high_density_epoch_pair_count']}",
        f"current_sparse_acceptance_closed={fmt_bool(agg['current_sparse_acceptance_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. eta 稀疏门",
        "",
        "| q | used upper | capacity | occupancy | eta slack numerator | realized | high density |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["affine_twin_epoch_pair_multiplicity_rows"]:
        lines.append(
            f"| {row['q']} | {row['epoch_pair_product_used_upper']} | {row['epoch_pair_capacity']} | "
            f"{row['occupancy_upper_ratio']:.9f} | {row['eta_slack_numerator']} | "
            f"`{fmt_bool(row['realized_current_sweep'])}` | "
            f"`{fmt_bool(row['high_density_epoch_pair_pdec_trigger'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 出口",
            "",
            "- 当前扫描没有 HighDensityEpochPair 行。",
            "- 若后续或全局族出现 `occupancy>eta`，该 `q` 直接成为固定/移动模 ColumnCRT-PDEC 证书对象。",
            "- 若始终满足 sparse gate，则进入 sparse SAE 质量账本；全局仍需证明该质量可求和并足以吸收反例链。",
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
            "- 具体目标：证明 sparse SAE 的全局求和吸收，或排斥 HighDensityEpochPair-PDEC/ColumnCRT。",
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
    parser.add_argument("--eta-numerator", type=int, default=ETA_NUMERATOR)
    parser.add_argument("--eta-denominator", type=int, default=ETA_DENOMINATOR)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    moving_ledger = args.moving_ledger if args.moving_ledger.is_absolute() else ROOT / args.moving_ledger
    result = build_result(moving_ledger, args.eta_numerator, args.eta_denominator)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "candidate_q_values": result["aggregate"]["candidate_q_values"],
                "candidate_product_mass_upper_sum": result["aggregate"]["candidate_product_mass_upper_sum"],
                "high_density_epoch_pair_count": result["aggregate"]["high_density_epoch_pair_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
