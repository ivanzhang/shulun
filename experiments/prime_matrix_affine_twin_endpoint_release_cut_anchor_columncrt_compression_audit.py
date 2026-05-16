#!/usr/bin/env python3
"""生成 AffineTwin cut-anchor ColumnCRT compression 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_cut_anchor_columncrt_compression_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-audit.md
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

CUT_ANCHOR_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-ledger.json"
)
SLOT_LOCK_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)
MOVING_FAMILY_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-moving-family-sae-columncrt-ledger.json"
)
SPARSE_SAE_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-sparse-sae-global-envelope-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-cut-anchor-"
    "columncrt-compression-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-cut-anchor-"
    "columncrt-compression-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-cut-anchor-"
    "columncrt-compression-audit.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def fmt_decimal(value: float) -> str:
    """稳定输出小数。"""
    return f"{value:.12g}"


def fraction_row(value: Fraction) -> dict[str, Any]:
    """把 Fraction 变成稳定 JSON 行。"""
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": float(value),
    }


def build_result(
    cut_anchor_path: Path,
    slot_lock_path: Path,
    moving_family_path: Path,
    sparse_sae_path: Path,
) -> dict[str, Any]:
    """构造 cut-anchor ColumnCRT compression 审计结果。"""
    cut_anchor = load_json(cut_anchor_path)
    slot_lock = load_json(slot_lock_path)
    moving_family = load_json(moving_family_path)
    sparse_sae = load_json(sparse_sae_path)

    cut_rows = cut_anchor["cut_anchor_rows"]
    cut_agg = cut_anchor["aggregate"]
    slot_row = slot_lock["affine_twin_slot_phase_lock_rows"][0]
    moving_agg = moving_family["aggregate"]
    sparse_agg = sparse_sae["aggregate"]

    modulus = int(cut_agg["combined_crt_modulus"])
    cut_count = int(cut_agg["cut_count"])
    actual_residues = sorted(
        {
            int(row["actual_anchor_representative"]) % modulus
            for row in cut_rows
        }
    )
    if len(actual_residues) != 1:
        raise RuntimeError(f"expected one actual CRT residue, got {actual_residues}")
    actual_residue = actual_residues[0]
    fixed_mass = Fraction(1, modulus)
    naive_cut_mass = Fraction(cut_count, modulus)
    saved_mass = naive_cut_mass - fixed_mass

    actual_representatives = sorted(
        {int(row["actual_anchor_representative"]) for row in cut_rows}
    )
    cut_labels = [
        f"{row['cut_from_pair']}->{row['cut_to_pair']}"
        for row in cut_rows
    ]

    pdec_object = {
        "schema": "CutAnchorColumnCRT-PDEC",
        "X": "current q=31 actual-retained cut-anchor formal cut set",
        "tau": {
            "P_congruence": f"P == {actual_residue} mod {modulus}",
            "generator_slot": (
                f"P == {int(slot_row['generator_residue'])} "
                f"mod {int(slot_row['generator_modulus'])}"
            ),
            "shifted_fill_slot": (
                f"P == {int(slot_row['shifted_fill_residue_for_generator_p'])} "
                f"mod {int(slot_row['fill_modulus'])}"
            ),
            "q": int(slot_row["gap_ell"]),
            "q_minus_2": int(slot_row["generator_ell"]),
        },
        "S": (
            "prime P in tau whose counterexample chain tries to persist after "
            "same-orientation cut-anchor absorption is closed"
        ),
        "registered_mass": fraction_row(fixed_mass),
        "cut_labels": cut_labels,
    }

    compression_rows = []
    for row in cut_rows:
        compression_rows.append(
            {
                "cut": f"{row['cut_from_pair']}->{row['cut_to_pair']}",
                "actual_anchor_representative": int(
                    row["actual_anchor_representative"]
                ),
                "actual_crt_residue": int(row["actual_anchor_representative"])
                % modulus,
                "actual_anchor_position": str(row["actual_anchor_position"]),
                "arc_width": int(row["arc_width"]),
                "total_endpoint_release_required": int(
                    row["total_endpoint_release_required"]
                ),
                "same_orientation_absorption_closed": bool(
                    row["same_orientation_absorption_closed"]
                ),
            }
        )

    escape_rows = [
        {
            "escape": "same_orientation_actual_retained_cut_anchor",
            "status": "closed_current_sweep",
            "capacity_object": "none",
            "reason": "all cuts fail left D=8 or right D=1 formula gates",
        },
        {
            "escape": "fixed_q_fixed_actual_residue_orientation_changing",
            "status": "registered_columncrt_pdec",
            "capacity_object": f"P == {actual_residue} mod {modulus}",
            "reason": "changing orientation cannot create new cut mass while q and the actual slot residue stay fixed",
        },
        {
            "escape": "moving_q_or_moving_residue",
            "status": "routed_existing_moving_family_sae_columncrt",
            "capacity_object": str(moving_agg["candidate_q_values"]),
            "reason": "moving q leaves the fixed cut ledger and enters the existing AffineTwin moving-family ledger",
        },
        {
            "escape": "cut_multiplicity_as_capacity_source",
            "status": "closed_current_sweep",
            "capacity_object": f"1/{modulus} not {cut_count}/{modulus}",
            "reason": "all cuts share the same actual CRT residue",
        },
    ]

    aggregate = {
        "cut_anchor_sweep_ledger": str(cut_anchor_path.relative_to(ROOT)),
        "slot_lock_ledger": str(slot_lock_path.relative_to(ROOT)),
        "moving_family_ledger": str(moving_family_path.relative_to(ROOT)),
        "sparse_sae_ledger": str(sparse_sae_path.relative_to(ROOT)),
        "combined_crt_modulus": modulus,
        "actual_anchor_pair": str(cut_agg["actual_anchor_pair"]),
        "actual_representatives_used_by_cuts": actual_representatives,
        "actual_crt_residue": actual_residue,
        "cut_count": cut_count,
        "unique_actual_crt_residue_count": len(actual_residues),
        "cut_to_actual_residue_compression_factor": cut_count
        / len(actual_residues),
        "fixed_actual_columncrt_mass": fraction_row(fixed_mass),
        "naive_cut_counting_mass": fraction_row(naive_cut_mass),
        "mass_saved_by_cut_compression": fraction_row(saved_mass),
        "cut_multiplicity_capacity_overcount_factor": cut_count,
        "cut_multiplicity_capacity_source_closed_current_sweep": len(actual_residues)
        == 1
        and bool(cut_agg["cut_anchor_sweep_closed_current_sweep"]),
        "fixed_q_fixed_residue_columncrt_registered": True,
        "same_orientation_cut_anchor_closed_current_sweep": bool(
            cut_agg["cut_anchor_sweep_closed_current_sweep"]
        ),
        "moving_family_candidate_q_values": moving_agg["candidate_q_values"],
        "moving_family_realized_q_values": moving_agg["realized_q_values"],
        "fixed_residue_slot_drift_pair_count": int(
            moving_agg["fixed_residue_slot_drift_pair_count"]
        ),
        "fixed_q_fixed_residue_columncrt_routing_closed": bool(
            moving_agg["fixed_q_fixed_residue_columncrt_routing_closed"]
        ),
        "current_realized_sae_mass": sparse_agg["current_realized_sae_mass"],
        "candidate_single_pair_sae_mass_sum": sparse_agg[
            "candidate_single_pair_sae_mass_sum"
        ],
        "frontier_single_atom_tail_from_min_candidate_q": sparse_agg[
            "frontier_single_atom_tail_from_min_candidate_q"
        ],
        "cut_anchor_columncrt_compression_closed_current_sweep": len(
            actual_residues
        )
        == 1
        and bool(cut_agg["cut_anchor_sweep_closed_current_sweep"])
        and bool(moving_agg["fixed_q_fixed_residue_columncrt_routing_closed"]),
        "global_cut_anchor_columncrt_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "cut_anchor_columncrt_compression_audit"
        ),
        "status": (
            "current_sweep_cut_anchor_columncrt_compression_"
            "closed_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "pdec_object": pdec_object,
        "compression_rows": compression_rows,
        "escape_rows": escape_rows,
        "contract": {
            "cut_anchor_columncrt_compression_gate": [
                "do not count circular cuts as independent actual-P residue classes",
                "compress every actual-retained cut to the same fixed CRT atom",
                "register orientation-changing persistence as CutAnchorColumnCRT-PDEC",
                "route moving q or moving residues to the existing AffineTwin moving-family SAE/ColumnCRT ledger",
            ],
            "closed_current_sweep": aggregate[
                "cut_anchor_columncrt_compression_closed_current_sweep"
            ],
            "global_remaining": [
                "CutAnchorColumnCRTPDECExclusion",
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion",
                "CutAnchorSweepGlobalFamilyNoGo",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                cut_anchor_path,
                slot_lock_path,
                moving_family_path,
                sparse_sae_path,
            )
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    fixed_mass = agg["fixed_actual_columncrt_mass"]
    naive_mass = agg["naive_cut_counting_mass"]
    saved_mass = agg["mass_saved_by_cut_compression"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release cut-anchor ColumnCRT compression audit",
        "",
        "**状态：** `current_sweep_cut_anchor_columncrt_compression_closed_global_open`",
        "",
        "本审计继续下钻 cut-anchor sweep 的剩余出口：圆周 cut 是分析切口，不是新的 actual residue 自由度。若保留同一个 actual packet，全部 cut 都压回同一个 `P mod q(q-2)` 的 ColumnCRT 原子。",
        "",
        "```text",
        f"cut_count={agg['cut_count']}",
        f"combined_crt_modulus={agg['combined_crt_modulus']}",
        f"actual_anchor_pair={agg['actual_anchor_pair']}",
        f"actual_representatives_used_by_cuts={agg['actual_representatives_used_by_cuts']}",
        f"actual_crt_residue={agg['actual_crt_residue']}",
        f"unique_actual_crt_residue_count={agg['unique_actual_crt_residue_count']}",
        f"cut_to_actual_residue_compression_factor={fmt_decimal(agg['cut_to_actual_residue_compression_factor'])}",
        f"fixed_actual_columncrt_mass={fixed_mass['numerator']}/{fixed_mass['denominator']}",
        f"naive_cut_counting_mass={naive_mass['numerator']}/{naive_mass['denominator']}",
        f"mass_saved_by_cut_compression={saved_mass['numerator']}/{saved_mass['denominator']}",
        f"same_orientation_cut_anchor_closed_current_sweep={fmt_bool(agg['same_orientation_cut_anchor_closed_current_sweep'])}",
        f"fixed_q_fixed_residue_columncrt_registered={fmt_bool(agg['fixed_q_fixed_residue_columncrt_registered'])}",
        f"moving_family_candidate_q_values={agg['moving_family_candidate_q_values']}",
        f"cut_anchor_columncrt_compression_closed_current_sweep={fmt_bool(agg['cut_anchor_columncrt_compression_closed_current_sweep'])}",
        "```",
        "",
        "## 1. cut 到 actual residue 的压缩",
        "",
        "| cut | actual rep | actual residue | position | arc width | release | same-orientation closed |",
        "| --- | ---: | ---: | --- | ---: | ---: | --- |",
    ]
    for row in result["compression_rows"]:
        lines.append(
            "| `{cut}` | {rep} | {residue} | `{pos}` | {width} | {release} | `{closed}` |".format(
                cut=row["cut"],
                rep=row["actual_anchor_representative"],
                residue=row["actual_crt_residue"],
                pos=row["actual_anchor_position"],
                width=row["arc_width"],
                release=row["total_endpoint_release_required"],
                closed=fmt_bool(row["same_orientation_absorption_closed"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. PDEC/ColumnCRT 输入对象",
            "",
            "```text",
            f"schema={result['pdec_object']['schema']}",
            f"X={result['pdec_object']['X']}",
            f"tau.P={result['pdec_object']['tau']['P_congruence']}",
            f"tau.generator={result['pdec_object']['tau']['generator_slot']}",
            f"tau.shifted_fill={result['pdec_object']['tau']['shifted_fill_slot']}",
            f"registered_mass={fixed_mass['numerator']}/{fixed_mass['denominator']}",
            "```",
            "",
            "## 3. 逃逸路线压缩",
            "",
            "| escape | status | capacity object | reason |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["escape_rows"]:
        lines.append(
            "| `{}` | `{}` | `{}` | {} |".format(
                row["escape"],
                row["status"],
                row["capacity_object"],
                row["reason"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 显式容量矛盾点",
            "",
            f"若错误地把 `{agg['cut_count']}` 个 cut 当成独立 actual 相位，质量会被记成 `{naive_mass['numerator']}/{naive_mass['denominator']}`。但所有 cut 的 actual representative 都同余于 `{agg['actual_crt_residue']} mod {agg['combined_crt_modulus']}`，因此固定 `q=31`、固定 actual 槽的真实 ColumnCRT 质量只有 `{fixed_mass['numerator']}/{fixed_mass['denominator']}`，多出来的 `{saved_mass['numerator']}/{saved_mass['denominator']}` 是切口重数假象。",
            "",
            "因此，same-orientation 已被 cut-anchor sweep 关闭后，固定 `q` 固定残基的方向改变逃逸不能获得新的容量；它只能作为 `CutAnchorColumnCRT-PDEC` 输入对象被登记。若 `q` 或残基移动，则已经离开本固定 cut 账本，回到既有 AffineTwin moving-family SAE/ColumnCRT 账本。",
            "",
            "## 5. 结论边界",
            "",
            "- 本步关闭当前 sweep 中“切口多重性作为容量来源”的解释。",
            "- 本步仍不排斥全局 `CutAnchorColumnCRT-PDEC`，也不关闭行/列无条件命题。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cut-anchor-ledger",
        type=Path,
        default=CUT_ANCHOR_LEDGER,
        help="cut-anchor sweep ledger path",
    )
    parser.add_argument(
        "--slot-lock-ledger",
        type=Path,
        default=SLOT_LOCK_LEDGER,
        help="AffineTwin slot-lock ledger path",
    )
    parser.add_argument(
        "--moving-family-ledger",
        type=Path,
        default=MOVING_FAMILY_LEDGER,
        help="AffineTwin moving-family SAE/ColumnCRT ledger path",
    )
    parser.add_argument(
        "--sparse-sae-ledger",
        type=Path,
        default=SPARSE_SAE_LEDGER,
        help="AffineTwin sparse SAE envelope ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.cut_anchor_ledger,
        args.slot_lock_ledger,
        args.moving_family_ledger,
        args.sparse_sae_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
