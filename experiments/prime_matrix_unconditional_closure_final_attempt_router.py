#!/usr/bin/env python3
"""最终无条件闭合尝试：合并数学二选一输入与独立晋级验收。

用法示例：
  python3 experiments/prime_matrix_unconditional_closure_final_attempt_router.py

输出：
  docs/monograph/prime-matrix-unconditional-closure-final-attempt-router.json
  docs/monograph/prime-matrix-unconditional-closure-final-attempt-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_THREE_ATOMS = DOCS / "prime-matrix-three-final-atoms-hard-attack-router.json"
DEFAULT_C_DEPENDENT = (
    DOCS / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json"
)
DEFAULT_SOURCE_ENTROPY = DOCS / "prime-matrix-triad-a1-source-block-entropy-router.json"
DEFAULT_ANTIATOM_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
)
DEFAULT_NCBLK_GAP = DOCS / "prime-matrix-triad-a1-ncblk-projection-gap-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-unconditional-closure-final-attempt-router.json"
DEFAULT_MD = DOCS / "prime-matrix-unconditional-closure-final-attempt-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    three_atoms: dict[str, Any],
    c_dependent: dict[str, Any],
    source_entropy: dict[str, Any],
    antiatom_nogo: dict[str, Any],
    ncblk_gap: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成最终闭合尝试的判定行。"""
    math_basis_pinned = (
        three_atoms.get("minimum_unconditional_basis")
        == "(ActualFullSNonAPSourceCapacityAntiAtomForActualSource OR "
        "CDependentResidueWeightSpectralCancellationInput) AND "
        "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
    )
    c_dep_to_ncblk = (
        c_dependent.get("terminal_gap_after_router")
        == "NCBLKActualBlockNonConcentrationOrExternalDIBFI"
        and "NCBLKActualBlockNonConcentrationOrExternalDIBFI"
        in c_dependent.get("open_reduction_gates", [])
    )
    internal_entropy_open = (
        source_entropy.get("conditional_source_entropy_implies_ncblk") is True
        and source_entropy.get("current_internal_source_entropy_closed") is False
        and source_entropy.get("source_entropy_gap_exists") is True
    )
    generic_antiatom_refuted = (
        antiatom_nogo.get("self_contained_generic_version_refuted") is True
        and antiatom_nogo.get("self_contained_generic_version_closed_as_proof") is False
    )
    moving_block_gap = (
        ncblk_gap.get("fixed_projection_gap_exists") is True
        and ncblk_gap.get("current_internal_ncblk_closed") is False
        and ncblk_gap.get("terminal_gap_after_router")
        == "MovingBlockSpreadNCBLKOrExternalDIBFIOriginalDispersion"
    )
    independent_acceptance_open = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )

    return [
        {
            "gate": "ThreeAtomBasisPinned",
            "closed_at_boundary": math_basis_pinned,
            "proved_or_accepted": False,
            "meaning": "三个最终原子已经压成数学二选一输入加独立晋级验收。",
            "remaining": "继续判断二选一数学输入是否能由当前材料推出。",
        },
        {
            "gate": "CDependentLaneReturnsToNCBLK",
            "closed_at_boundary": c_dep_to_ncblk,
            "proved_or_accepted": False,
            "meaning": "c-dependent completed residue 权重经有限 Fourier/BWFD/BSC/KFLS 回到 actual NC-BLK 或外部定理。",
            "remaining": "证明 actual same-(u,v) block non-concentration，或精确匹配外部 DI/BFI/Kuznetsov。",
        },
        {
            "gate": "ActualSourceAntiAtomEqualsMovingBlockSpread",
            "closed_at_boundary": internal_entropy_open and generic_antiatom_refuted,
            "proved_or_accepted": False,
            "meaning": "actual-source 反原子本质上是 moving-block spread/source entropy；generic 版本已被反证。",
            "remaining": "必须证明 actual 系数源自身的 moving-block spread，不能用形式 WFD/Type/Fourier 代替。",
        },
        {
            "gate": "FixedProjectionCannotCloseMovingBlock",
            "closed_at_boundary": moving_block_gap,
            "proved_or_accepted": False,
            "meaning": "A1 fixed-projection diffuse 不控制随尺度移动的 same-(u,v) 块。",
            "remaining": "新增 MovingBlockSpreadNCBLK 定理，或走精确外部 dispersion。",
        },
        {
            "gate": "ExternalTheoremMatchStillAbsentInCorpus",
            "closed_at_boundary": moving_block_gap and c_dep_to_ncblk,
            "proved_or_accepted": False,
            "meaning": "外部路线已被精确命名，但仓库没有逐项匹配到当前 full-S、non-AP、未中心化、无投影对象的定理。",
            "remaining": "提交 primary-source theorem match：变量表、尺度、权重、无投影对象、局部方差扣除全部同一化。",
        },
        {
            "gate": "IndependentPromotionStillOpen",
            "closed_at_boundary": independent_acceptance_open,
            "proved_or_accepted": False,
            "meaning": "DStructure/Rankin 晋级包边界已闭合，但不能作者侧自验收。",
            "remaining": "正式全集 Rankin 证书、Tail-log4 外部适配、有限验证 hash 与独立审稿接受。",
        },
    ]


def run(
    three_atoms_path: Path,
    c_dependent_path: Path,
    source_entropy_path: Path,
    antiatom_nogo_path: Path,
    ncblk_gap_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行最终无条件闭合尝试。"""
    source_paths = [
        three_atoms_path,
        c_dependent_path,
        source_entropy_path,
        antiatom_nogo_path,
        ncblk_gap_path,
        dstructure_path,
    ]
    three_atoms = load_json(three_atoms_path)
    c_dependent = load_json(c_dependent_path)
    source_entropy = load_json(source_entropy_path)
    antiatom_nogo = load_json(antiatom_nogo_path)
    ncblk_gap = load_json(ncblk_gap_path)
    dstructure = load_json(dstructure_path)

    rows = build_rows(
        three_atoms=three_atoms,
        c_dependent=c_dependent,
        source_entropy=source_entropy,
        antiatom_nogo=antiatom_nogo,
        ncblk_gap=ncblk_gap,
        dstructure=dstructure,
    )
    boundary_closed = all(row["closed_at_boundary"] for row in rows)
    all_accepted = all(row["proved_or_accepted"] for row in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_unconditional_closure_final_attempt_router",
        "status": "unconditional_closure_final_attempt_reduced_to_irreducible_new_inputs_open",
        "final_attempt_boundary_closed": boundary_closed,
        "all_required_inputs_proved_or_accepted": all_accepted,
        "math_lanes_collapsed_to_common_core": True,
        "internal_math_proof_found_in_current_corpus": False,
        "external_math_match_found_in_current_corpus": False,
        "independent_promotion_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "irreducible_math_input": (
            "MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients "
            "OR PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem"
        ),
        "irreducible_promotion_input": (
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "final_unconditional_basis": (
            "(MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients OR "
            "PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "no_unconditional_closure_theorem": (
            "在当前材料中，二选一数学输入已经汇合到 actual moving-block spread/NC-BLK "
            "或精确外部 dispersion；generic 反原子被反证，fixed-projection 不能控制 moving label，"
            "外部定理尚未逐项匹配，独立晋级验收也未完成。因此当前材料不能无条件闭合行/列命题。"
        ),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 审查报告。"""
    lines: list[str] = [
        "# Prime Matrix 最终无条件闭合尝试路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["no_unconditional_closure_theorem"],
        "",
        "```text",
        f"final_attempt_boundary_closed={fmt_bool(result['final_attempt_boundary_closed'])}",
        f"all_required_inputs_proved_or_accepted={fmt_bool(result['all_required_inputs_proved_or_accepted'])}",
        f"math_lanes_collapsed_to_common_core={fmt_bool(result['math_lanes_collapsed_to_common_core'])}",
        f"internal_math_proof_found_in_current_corpus={fmt_bool(result['internal_math_proof_found_in_current_corpus'])}",
        f"external_math_match_found_in_current_corpus={fmt_bool(result['external_math_match_found_in_current_corpus'])}",
        f"independent_promotion_acceptance_completed={fmt_bool(result['independent_promotion_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最终判定表",
        "",
        "| gate | boundary_closed | proved_or_accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{boundary}` | `{accepted}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                boundary=fmt_bool(row["closed_at_boundary"]),
                accepted=fmt_bool(row["proved_or_accepted"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 不可再压缩输入基",
            "",
            "```text",
            result["final_unconditional_basis"],
            "```",
            "",
            "## 3. 当前结论",
            "",
            "当前完成的是终局输入边界闭合，不是无条件定理闭合。",
            "要升级为完整无条件定理，必须新增或独立接受上面的数学输入和晋级验收输入。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--three-atoms", type=Path, default=DEFAULT_THREE_ATOMS)
    parser.add_argument("--c-dependent", type=Path, default=DEFAULT_C_DEPENDENT)
    parser.add_argument("--source-entropy", type=Path, default=DEFAULT_SOURCE_ENTROPY)
    parser.add_argument("--antiatom-nogo", type=Path, default=DEFAULT_ANTIATOM_NOGO)
    parser.add_argument("--ncblk-gap", type=Path, default=DEFAULT_NCBLK_GAP)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        three_atoms_path=args.three_atoms,
        c_dependent_path=args.c_dependent,
        source_entropy_path=args.source_entropy,
        antiatom_nogo_path=args.antiatom_nogo,
        ncblk_gap_path=args.ncblk_gap,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["final_unconditional_basis"])


if __name__ == "__main__":
    main()
