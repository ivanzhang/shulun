#!/usr/bin/env python3
"""硬攻行列命题三个最后原子，并输出不可替代输入边界。

用法示例：
  python3 experiments/prime_matrix_three_final_atoms_hard_attack_router.py

输出：
  docs/monograph/prime-matrix-three-final-atoms-hard-attack-router.json
  docs/monograph/prime-matrix-three-final-atoms-hard-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_LAST_ATOMS = DOCS / "prime-matrix-last-remaining-atoms-router.json"
DEFAULT_SOURCE_ANTIATOM = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
DEFAULT_COMPLETED_WEIGHT = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_EXACT_FACTOR_SUPPORT = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_FACTOR_INCIDENCE = DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-three-final-atoms-hard-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-three-final-atoms-hard-attack-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_attack_rows(
    last_atoms: dict[str, Any],
    source_antiatom: dict[str, Any],
    completed_weight: dict[str, Any],
    dstructure: dict[str, Any],
    exact_factor_support: dict[str, Any],
    factor_incidence: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成三个最终原子的硬攻结果行。"""
    last_names = set(last_atoms.get("unconditional_closure_equivalent_to_atoms", []))
    source_open = source_antiatom.get("open_antiatom_gates", [])
    spectral_open = completed_weight.get("open_spectral_gap_gates", [])

    actual_atom_boundary = (
        "ActualFullSNonAPExactSupportAtom" in last_names
        and "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"
        in source_open
        and exact_factor_support.get("current_internal_exact_factor_support_closed") is False
        and factor_incidence.get("naive_incidence_bridge_valid") is False
    )
    completed_atom_boundary = (
        "ModulusDependentCompletedFullSKLSInput" in last_names
        and completed_weight.get("completed_weight_spectral_gap_closed") is False
        and "CDependentResidueWeightSpectralCancellationInput" in spectral_open
    )
    promotion_atom_boundary = (
        "DStructureRankinIndependentAcceptance" in last_names
        and dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )
    full_rankin_closed = (
        dstructure.get("full_rankin_ledger_still_open_closed") is True
        and dstructure.get("batch_rankin_pass_or_return_closed") is True
    )

    return [
        {
            "original_atom": "ActualFullSNonAPExactSupportAtom",
            "attack_status": "reduced_not_proved",
            "boundary_closed": actual_atom_boundary,
            "proved_or_accepted": False,
            "refined_atom": "ActualFullSNonAPSourceCapacityAntiAtomForActualSource",
            "blocked_shortcuts": source_antiatom.get("blocked_shortcuts", []),
            "structural_reason": (
                "精确因子支撑与 Type/Fourier 容量兼容不是两个独立估计；它们等价于实际 "
                "full-S non-AP 源容量测度没有 moving same-(u,v) 原子。generic 版本已被 "
                "moving-delta 模型反证，K4/K6 与朴素 incidence 也不能推出该结论。"
            ),
            "minimum_completion": (
                "证明 actual source 的无 moving atom 反原子定理；或者把 actual source 锁回 "
                "canonical RIW/Buchstab 已闭合分支；否则必须改走外部谱/dispersion 输入。"
            ),
        },
        {
            "original_atom": "ModulusDependentCompletedFullSKLSInput",
            "attack_status": "reduced_not_proved",
            "boundary_closed": completed_atom_boundary,
            "proved_or_accepted": False,
            "refined_atom": "CDependentResidueWeightSpectralCancellationInput",
            "blocked_shortcuts": [
                "pointwise Weil + L2",
                "ordinary large sieve",
                "flat or centered residue shortcut",
            ],
            "structural_reason": (
                "full-S 长度已可按模 c 完成；剩余不是窗口长度，而是 B_{c,x}=sum_k beta_{x+kc} "
                "这种依赖 c 的未中心化 residue 权重。L2 只到自然尺度，普通大筛没有 c,h "
                "dispersion 结构。"
            ),
            "minimum_completion": (
                "证明或引用 completed、c-dependent residue weight 的 Kuznetsov/DI-BFI 谱平均抵消，"
                "并保持 full-S、non-AP、无投影、未中心化目标。"
            ),
        },
        {
            "original_atom": "DStructureRankinIndependentAcceptance",
            "attack_status": "boundary_closed_referee_acceptance_open",
            "boundary_closed": promotion_atom_boundary,
            "proved_or_accepted": False,
            "refined_atom": "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            "blocked_shortcuts": ["author-side self-promotion"],
            "structural_reason": (
                "第三原子不是隐藏数学终端，而是定理晋级验收门。Rankin pass-or-return 子账本"
                f"{'已内部闭合' if full_rankin_closed else '仍未内部闭合'}；但 D-structure 归约、"
                "Tail-log4 外部适配、有限验证 hash 与独立接受仍未完成。"
            ),
            "minimum_completion": (
                "取得 D-structure/Structured-EHPD 归约、Tail-log4 BG/RKS 适配、有限验证归档 hash、"
                "以及 Rankin pass-or-return 子账本的独立接受；作者侧不能自审升级。"
            ),
        },
    ]


def run(
    last_atoms_path: Path,
    source_antiatom_path: Path,
    completed_weight_path: Path,
    dstructure_path: Path,
    exact_factor_support_path: Path,
    factor_incidence_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行三个最终原子的硬攻路由。"""
    source_paths = [
        last_atoms_path,
        source_antiatom_path,
        completed_weight_path,
        dstructure_path,
        exact_factor_support_path,
        factor_incidence_path,
    ]
    last_atoms = load_json(last_atoms_path)
    source_antiatom = load_json(source_antiatom_path)
    completed_weight = load_json(completed_weight_path)
    dstructure = load_json(dstructure_path)
    exact_factor_support = load_json(exact_factor_support_path)
    factor_incidence = load_json(factor_incidence_path)

    rows = build_attack_rows(
        last_atoms=last_atoms,
        source_antiatom=source_antiatom,
        completed_weight=completed_weight,
        dstructure=dstructure,
        exact_factor_support=exact_factor_support,
        factor_incidence=factor_incidence,
    )
    all_boundaries_closed = all(row["boundary_closed"] for row in rows)
    all_atoms_closed = all(row["proved_or_accepted"] for row in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_three_final_atoms_hard_attack_router",
        "status": "three_final_atoms_reduced_to_two_lane_math_input_plus_independent_promotion_open",
        "three_atom_attack_boundary_closed": all_boundaries_closed,
        "all_three_atoms_proved_or_accepted": all_atoms_closed,
        "author_side_new_unconditional_closure_found": False,
        "conditional_logic_chain_complete": all_boundaries_closed,
        "row_column_unconditional_closed": False,
        "mathematical_final_choice": [
            "ActualFullSNonAPSourceCapacityAntiAtomForActualSource",
            "CDependentResidueWeightSpectralCancellationInput",
        ],
        "promotion_final_atom": "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        "minimum_unconditional_basis": (
            "(ActualFullSNonAPSourceCapacityAntiAtomForActualSource OR "
            "CDependentResidueWeightSpectralCancellationInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "irreducibility_law": (
            "三个最后原子继续硬攻后，PDEC/sparse 与 APSourceLift/generic anti-atom 等旧路仍无效。"
            "noncanonical 方向只剩两个二选一可用数学输入：actual source 无 moving atom 反原子，"
            "或 c-dependent completed residue weight 谱抵消。最终晋级仍需独立 DStructure/Rankin "
            "验收。当前材料没有给出这些新增定理或独立验收，因此完整无条件闭合仍未成立。"
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
        "# Prime Matrix 三个最终原子硬攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["irreducibility_law"],
        "",
        "```text",
        f"three_atom_attack_boundary_closed={fmt_bool(result['three_atom_attack_boundary_closed'])}",
        f"all_three_atoms_proved_or_accepted={fmt_bool(result['all_three_atoms_proved_or_accepted'])}",
        f"author_side_new_unconditional_closure_found={fmt_bool(result['author_side_new_unconditional_closure_found'])}",
        f"conditional_logic_chain_complete={fmt_bool(result['conditional_logic_chain_complete'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 硬攻结果表",
        "",
        "| original_atom | attack_status | boundary_closed | proved_or_accepted | refined_atom | structural_reason | minimum_completion |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{original}` | `{status}` | `{boundary}` | `{accepted}` | `{refined}` | {reason} | {minimum} |".format(
                original=table_cell(row["original_atom"]),
                status=table_cell(row["attack_status"]),
                boundary=fmt_bool(row["boundary_closed"]),
                accepted=fmt_bool(row["proved_or_accepted"]),
                refined=table_cell(row["refined_atom"]),
                reason=table_cell(row["structural_reason"]),
                minimum=table_cell(row["minimum_completion"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 最小无条件输入基",
            "",
            f"`{result['minimum_unconditional_basis']}`",
            "",
            "## 3. 数学二选一输入",
            "",
        ]
    )
    lines.extend(f"- `{item}`" for item in result["mathematical_final_choice"])
    lines.extend(
        [
            "",
            "## 4. 晋级验收输入",
            "",
            f"- `{result['promotion_final_atom']}`",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--last-atoms", type=Path, default=DEFAULT_LAST_ATOMS)
    parser.add_argument("--source-antiatom", type=Path, default=DEFAULT_SOURCE_ANTIATOM)
    parser.add_argument("--completed-weight", type=Path, default=DEFAULT_COMPLETED_WEIGHT)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--exact-factor-support", type=Path, default=DEFAULT_EXACT_FACTOR_SUPPORT)
    parser.add_argument("--factor-incidence", type=Path, default=DEFAULT_FACTOR_INCIDENCE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        last_atoms_path=args.last_atoms,
        source_antiatom_path=args.source_antiatom,
        completed_weight_path=args.completed_weight,
        dstructure_path=args.dstructure,
        exact_factor_support_path=args.exact_factor_support,
        factor_incidence_path=args.factor_incidence,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["minimum_unconditional_basis"])


if __name__ == "__main__":
    main()
