#!/usr/bin/env python3
"""不可约数学输入精化路由器。

用法示例：
  python3 experiments/prime_matrix_irreducible_math_input_refinement_router.py

输出：
  docs/monograph/prime-matrix-irreducible-math-input-refinement-router.json
  docs/monograph/prime-matrix-irreducible-math-input-refinement-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_FINAL_ATTEMPT = DOCS / "prime-matrix-unconditional-closure-final-attempt-router.json"
DEFAULT_PRIMARY_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
)
DEFAULT_AP_LIFT_NOGO = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json"
DEFAULT_NEW_FULL_S = DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
DEFAULT_NCBLK_GAP = DOCS / "prime-matrix-triad-a1-ncblk-projection-gap-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-irreducible-math-input-refinement-router.json"
DEFAULT_MD = DOCS / "prime-matrix-irreducible-math-input-refinement-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256，固定证据来源。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    final_attempt: dict[str, Any],
    primary_nogo: dict[str, Any],
    ap_lift_nogo: dict[str, Any],
    new_full_s: dict[str, Any],
    ncblk_gap: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成输入精化判定表。"""
    previous_basis_pinned = (
        final_attempt.get("final_attempt_boundary_closed") is True
        and final_attempt.get("irreducible_math_input")
        == (
            "MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients "
            "OR PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem"
        )
    )
    internal_lane_pinned = (
        ncblk_gap.get("current_internal_ncblk_closed") is False
        and ncblk_gap.get("terminal_gap_after_router")
        == "MovingBlockSpreadNCBLKOrExternalDIBFIOriginalDispersion"
    )
    primary_sources_rejected = (
        primary_nogo.get("primary_source_specialization_closed") is False
        and primary_nogo.get("terminal_gap_after_router")
        == "NewFullSTheoremInputOrAPSourceLift"
        and "DIBFIPrimarySourceSpecializationRejected"
        in primary_nogo.get("closed_nogo_gates", [])
    )
    ap_lift_rejected = (
        ap_lift_nogo.get("ap_source_lift_rejected") is True
        and ap_lift_nogo.get("terminal_gap_after_router") == "NewFullSTheoremInput"
    )
    full_s_atom_pinned = (
        new_full_s.get("new_full_s_theorem_input_closed") is False
        and new_full_s.get("terminal_gap_after_router") == "FullSNonAPWFDKLSTheoremInput"
        and "FullSNonAPWFDKLSTheoremInput" in new_full_s.get("open_input_gates", [])
    )
    promotion_open = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )

    return [
        {
            "gate": "PreviousIrreducibleBasisPinned",
            "closed": previous_basis_pinned,
            "proved_or_accepted": False,
            "meaning": "上一轮已把数学输入压成 moving-block spread 或精确外部 DIBFI/Kuznetsov。",
            "refinement": "继续审查外部标签是否真能由现有 DI/BFI 主来源逐项匹配。",
        },
        {
            "gate": "InternalLaneIsActualMovingBlockSpread",
            "closed": internal_lane_pinned,
            "proved_or_accepted": False,
            "meaning": "内部路不是 fixed-projection diffuse，而是 actual full-S non-AP WFD 系数的 moving same-(u,v) 块扩散。",
            "refinement": "保留为 MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients。",
        },
        {
            "gate": "ExistingPrimaryDIBFISourceMatchRejected",
            "closed": primary_sources_rejected,
            "proved_or_accepted": False,
            "meaning": "现有 BFI AP 定理和 DI/Maynard J-scale 不能推出当前 full-S non-AP KLS-ext。",
            "refinement": "外部路不能再写成已经匹配的现有 DI/BFI/Kuznetsov 推论。",
        },
        {
            "gate": "APSourceLiftRejected",
            "closed": ap_lift_rejected,
            "proved_or_accepted": False,
            "meaning": "non-AP WFD 补集不能无损回提为 AP-source discrepancy。",
            "refinement": "外部路剩余不能借 APSourceLift 逃回 BFI AP 定理。",
        },
        {
            "gate": "FullSNonAPWFDKLSAtomPinned",
            "closed": full_s_atom_pinned,
            "proved_or_accepted": False,
            "meaning": "新增 full-S 定理输入已被精确定义为当前 non-AP、未中心化、无投影 WFD 窗口的 KLS/dispersion 估计。",
            "refinement": "把 PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem 精化为 FullSNonAPWFDKLSTheoremInput。",
        },
        {
            "gate": "IndependentPromotionStillRequired",
            "closed": promotion_open,
            "proved_or_accepted": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 晋级包边界已闭合，但尚未独立接受。",
            "refinement": "完整行/列无条件定理仍需独立晋级验收。",
        },
    ]


def run(
    final_attempt_path: Path,
    primary_nogo_path: Path,
    ap_lift_nogo_path: Path,
    new_full_s_path: Path,
    ncblk_gap_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行不可约输入精化审查。"""
    source_paths = [
        final_attempt_path,
        primary_nogo_path,
        ap_lift_nogo_path,
        new_full_s_path,
        ncblk_gap_path,
        dstructure_path,
    ]
    final_attempt = load_json(final_attempt_path)
    primary_nogo = load_json(primary_nogo_path)
    ap_lift_nogo = load_json(ap_lift_nogo_path)
    new_full_s = load_json(new_full_s_path)
    ncblk_gap = load_json(ncblk_gap_path)
    dstructure = load_json(dstructure_path)

    rows = build_rows(
        final_attempt=final_attempt,
        primary_nogo=primary_nogo,
        ap_lift_nogo=ap_lift_nogo,
        new_full_s=new_full_s,
        ncblk_gap=ncblk_gap,
        dstructure=dstructure,
    )
    row_closed = {row["gate"]: row["closed"] for row in rows}
    refinement_boundary_closed = all(row["closed"] for row in rows)
    all_inputs_proved_or_accepted = all(row["proved_or_accepted"] for row in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_irreducible_math_input_refinement_router",
        "status": "irreducible_math_input_refined_to_full_s_kls_or_moving_block_open",
        "refinement_boundary_closed": refinement_boundary_closed,
        "all_required_inputs_proved_or_accepted": all_inputs_proved_or_accepted,
        "existing_primary_dibfi_match_rejected": row_closed[
            "ExistingPrimaryDIBFISourceMatchRejected"
        ],
        "ap_source_lift_rejected": row_closed["APSourceLiftRejected"],
        "internal_moving_block_proof_found_in_current_corpus": False,
        "new_full_s_kls_theorem_proved_or_cited_in_current_corpus": False,
        "independent_promotion_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_math_input": (
            "MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients "
            "OR PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem"
        ),
        "refined_external_input": "FullSNonAPWFDKLSTheoremInput",
        "refined_math_input": (
            "MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients "
            "OR FullSNonAPWFDKLSTheoremInput"
        ),
        "refined_final_unconditional_basis": (
            "(MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients OR "
            "FullSNonAPWFDKLSTheoremInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "structural_law": (
            "The old external label is too broad after primary-source specialization. "
            "Existing BFI AP discrepancy and DI/Maynard J-scale estimates do not cover the "
            "current full-S non-AP uncentered no-projection WFD object, and APSourceLift is "
            "rejected. Hence the honest external branch is a new or independently cited "
            "FullSNonAPWFDKLSTheoremInput, while the internal branch remains actual moving-block spread."
        ),
        "plain_conclusion": (
            "终局数学输入边界可再精化一层：内部路仍是 actual moving-block spread；外部路不是"
            "已经逐项匹配的现有 DI/BFI/Kuznetsov 推论，而是必须新增、证明或明确引用的 "
            "FullSNonAPWFDKLSTheoremInput。再加上 DStructure/Rankin 独立验收未完成，当前材料仍不能"
            "声明完整行/列无条件定理。"
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
        "# Prime Matrix 不可约数学输入精化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"refinement_boundary_closed={fmt_bool(result['refinement_boundary_closed'])}",
        f"all_required_inputs_proved_or_accepted={fmt_bool(result['all_required_inputs_proved_or_accepted'])}",
        f"existing_primary_dibfi_match_rejected={fmt_bool(result['existing_primary_dibfi_match_rejected'])}",
        f"ap_source_lift_rejected={fmt_bool(result['ap_source_lift_rejected'])}",
        f"internal_moving_block_proof_found_in_current_corpus={fmt_bool(result['internal_moving_block_proof_found_in_current_corpus'])}",
        f"new_full_s_kls_theorem_proved_or_cited_in_current_corpus={fmt_bool(result['new_full_s_kls_theorem_proved_or_cited_in_current_corpus'])}",
        f"independent_promotion_acceptance_completed={fmt_bool(result['independent_promotion_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精化判定表",
        "",
        "| gate | closed | proved_or_accepted | meaning | refinement |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{accepted}` | {meaning} | {refinement} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                accepted=fmt_bool(row["proved_or_accepted"]),
                meaning=table_cell(row["meaning"]),
                refinement=table_cell(row["refinement"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 精化后的输入基",
            "",
            "上一轮输入：",
            "",
            "```text",
            result["previous_math_input"],
            "```",
            "",
            "精化后输入：",
            "",
            "```text",
            result["refined_final_unconditional_basis"],
            "```",
            "",
            "## 3. 当前结论",
            "",
            "这一步关闭的是命名精度缺口，不是证明缺口。",
            "`FullSNonAPWFDKLSTheoremInput` 仍需新增自足证明或独立外部定理引用；",
            "`MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients` 仍未由当前材料推出；",
            "`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 仍需独立验收。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-attempt", type=Path, default=DEFAULT_FINAL_ATTEMPT)
    parser.add_argument("--primary-nogo", type=Path, default=DEFAULT_PRIMARY_NOGO)
    parser.add_argument("--ap-lift-nogo", type=Path, default=DEFAULT_AP_LIFT_NOGO)
    parser.add_argument("--new-full-s", type=Path, default=DEFAULT_NEW_FULL_S)
    parser.add_argument("--ncblk-gap", type=Path, default=DEFAULT_NCBLK_GAP)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        final_attempt_path=args.final_attempt,
        primary_nogo_path=args.primary_nogo,
        ap_lift_nogo_path=args.ap_lift_nogo,
        new_full_s_path=args.new_full_s,
        ncblk_gap_path=args.ncblk_gap,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["refined_final_unconditional_basis"])


if __name__ == "__main__":
    main()
