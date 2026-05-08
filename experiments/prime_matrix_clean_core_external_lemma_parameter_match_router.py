#!/usr/bin/env python3
"""Prime Matrix clean-core 外部引理参数匹配路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_external_lemma_parameter_match_router.py

输出：
  docs/monograph/prime-matrix-clean-core-external-lemma-parameter-match-router.json
  docs/monograph/prime-matrix-clean-core-external-lemma-parameter-match-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_CURRENT = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
DEFAULT_SPECTRAL = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_PRIMARY_NOGO = DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_CLEAN_KLS = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-external-lemma-parameter-match-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-external-lemma-parameter-match-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def external_sources() -> list[dict[str, str]]:
    """记录本轮核对的一手外部来源。"""
    return [
        {
            "source": "Deshouillers-Iwaniec 1982/83",
            "object": "Kloosterman sums and Fourier coefficients of cusp forms",
            "usable_for": "谱 Kloosterman 大筛、Kuznetsov/trace formula 后的平均抵消。",
            "not_usable_for": "pre-Cauchy source constructor 或 actual summand emitter。",
            "url": "https://eudml.org/doc/142975",
        },
        {
            "source": "Bombieri-Friedlander-Iwaniec 1986",
            "object": "Primes in arithmetic progressions to large moduli, Theorem 10",
            "usable_for": "well-factorable AP discrepancy / dispersion framework。",
            "not_usable_for": "non-AP clean-core primitive constructor formula。",
            "url": "https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6385-11511_2006_Article_BF02399204.pdf",
        },
        {
            "source": "Maynard 2020",
            "object": "well-factorable AP estimates to larger moduli",
            "usable_for": "更强 AP/well-factorable 分布背景。",
            "not_usable_for": "c-dependent completed residue weights 或 pre-Cauchy source emitter。",
            "url": "https://arxiv.org/abs/2006.07088",
        },
    ]


def match_rows(
    spectral: dict[str, Any],
    primary_nogo: dict[str, Any],
    clean_kls: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成外部引理与当前原子的参数匹配表。"""
    return [
        {
            "lemma_family": "DI_Kuznetsov_KLS",
            "structure_match": "post_completion_inverse_phase_average",
            "parameter_match": "partial",
            "matches_constructor_formula": False,
            "reason": (
                "DI/Kuznetsov 处理的是已给定系数向量后的 Kloosterman 模数/频率平均；"
                "当前自足原子要求 Cauchy 前生成 alpha/delta summand。"
            ),
            "route": "只能进入 external_spectral 或 KLS-window 分支。",
        },
        {
            "lemma_family": "BFI1986_Theorem10",
            "structure_match": "well_factorable_AP_discrepancy",
            "parameter_match": "AP_source_only",
            "matches_constructor_formula": False,
            "reason": (
                "BFI Theorem 10 的对象是 AP discrepancy 与 well-factorable 模权；"
                "当前对象是 non-AP clean-core primitive source constructor。"
            ),
            "route": "若能证明 APSourceLift 才可回接；当前 APSourceLift 未证。",
        },
        {
            "lemma_family": "Maynard_WellFactorable_AP",
            "structure_match": "stronger_AP_level_background",
            "parameter_match": "not_c_dependent_completed_weight",
            "matches_constructor_formula": False,
            "reason": (
                "Maynard 扩展 AP/well-factorable 平均范围，但仍不是 actual noncanonical "
                "summand emitter，也不处理当前 B_{c,x} 依赖。"
            ),
            "route": "可作外部谱路线背景，不能替代自足公式。",
        },
        {
            "lemma_family": "KLS_Window_Template",
            "structure_match": "phase_modulus_frequency_match_after_CRT",
            "parameter_match": "matched_for_two_point_or_clean_KLS_template",
            "matches_constructor_formula": False,
            "reason": (
                "仓库 KLS-window 模板已把相位、模数、频率和 well-factorable 权重对齐到外部 KLS，"
                "但它从已给定系数开始，不生成 noncanonical clean-core 系数。"
            ),
            "route": clean_kls.get("terminal_gap_after_router", "KuznetsovLSAtomSC9OrExternalCitation"),
        },
        {
            "lemma_family": "Completed_CDependentResidueSpectral",
            "structure_match": "closest_external_target",
            "parameter_match": "open",
            "matches_constructor_formula": False,
            "reason": spectral.get(
                "structural_law",
                "完成型 residue 权重依赖 c，仍需专门谱/dispersion 抵消。",
            ),
            "route": spectral.get("terminal_gap_after_router", "CDependentResidueWeightSpectralCancellationInput"),
        },
        {
            "lemma_family": "Existing_DI_BFI_Primary_Source_Specialization",
            "structure_match": "rejected_for_full_S_non_AP",
            "parameter_match": "blocked_by_scale_or_object",
            "matches_constructor_formula": False,
            "reason": primary_nogo.get(
                "structural_law",
                "现有 DI/BFI 主来源不能直接推出 full-S non-AP KLS-ext。",
            ),
            "route": primary_nogo.get("terminal_gap_after_router", "NewFullSTheoremInputOrAPSourceLift"),
        },
    ]


def gate_rows(
    current: dict[str, Any],
    spectral: dict[str, Any],
    primary_nogo: dict[str, Any],
    external_index_text: str,
    kls_template_text: str,
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成外部引理参数匹配判定表。"""
    has_di = "Deshouillers" in external_index_text and "Kloosterman" in external_index_text
    has_bfi = "Bombieri" in external_index_text and "Theorem 10" in external_index_text
    has_kls_template = "DI spectral Kloosterman large sieve" in kls_template_text
    return [
        {
            "gate": "CurrentSelfContainedAtomPinned",
            "closed": current.get("latest_internal_subinput")
            == "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn",
            "proved": False,
            "meaning": "上一层已把完全自足源侧剩余压成 actual noncanonical constructor formula。",
            "remaining": "核对外部引理是否可替代该公式。",
        },
        {
            "gate": "ExternalPrimarySourcesIdentified",
            "closed": has_di and has_bfi,
            "proved": True,
            "meaning": "外部索引已定位 DI Kloosterman 与 BFI well-factorable AP 主来源。",
            "remaining": "这些来源的对象是否匹配当前原子。",
        },
        {
            "gate": "KLSWindowAdaptationAvailable",
            "closed": has_kls_template,
            "proved": True,
            "meaning": "KLS-window 已有相位、模数、频率、权重和损失适配模板。",
            "remaining": "模板属于 completion 后谱平均，不是 source constructor。",
        },
        {
            "gate": "ExternalLemmasDoNotEmitPreCauchySummands",
            "closed": True,
            "proved": True,
            "meaning": "DI/BFI/Kuznetsov 输入都从已给定系数或完成型权重开始，不能生成 alpha/delta summand emitter。",
            "remaining": "自足 constructor formula 仍需内部证明。",
        },
        {
            "gate": "PrimarySourceSpecializationNoGoRetained",
            "closed": primary_nogo.get("terminal_gap_after_router")
            == "NewFullSTheoremInputOrAPSourceLift",
            "proved": True,
            "meaning": "现有 DI/BFI 主来源不能直接推出 full-S non-AP KLS-ext。",
            "remaining": "若走外部路线，仍需新 Full-S 定理或 APSourceLift。",
        },
        {
            "gate": "CDependentResidueExternalTargetStillOpen",
            "closed": spectral.get("terminal_gap_after_router")
            == "CDependentResidueWeightSpectralCancellationInput",
            "proved": False,
            "meaning": "最接近的外部谱目标仍是 c-dependent residue weight cancellation。",
            "remaining": "证明或接受该外部谱输入。",
        },
        {
            "gate": "ActualNoncanonicalConstructorFormulaStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "外部引理匹配不能替代 actual noncanonical primitive source constructor formula。",
            "remaining": "证明 ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧完成后仍需独立验收。",
        },
    ]


def run(
    current_path: Path,
    spectral_path: Path,
    primary_nogo_path: Path,
    external_index_path: Path,
    kls_template_path: Path,
    clean_kls_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行外部引理参数匹配路由。"""
    source_paths = [
        current_path,
        spectral_path,
        primary_nogo_path,
        external_index_path,
        kls_template_path,
        clean_kls_path,
        dstructure_path,
    ]
    current = load_json(current_path)
    spectral = load_json(spectral_path)
    primary_nogo = load_json(primary_nogo_path)
    external_index_text = external_index_path.read_text(encoding="utf-8")
    kls_template_text = kls_template_path.read_text(encoding="utf-8")
    clean_kls = load_json(clean_kls_path)
    dstructure = load_json(dstructure_path)

    rows = gate_rows(
        current=current,
        spectral=spectral,
        primary_nogo=primary_nogo,
        external_index_text=external_index_text,
        kls_template_text=kls_template_text,
        dstructure=dstructure,
    )
    matches = match_rows(
        spectral=spectral,
        primary_nogo=primary_nogo,
        clean_kls=clean_kls,
    )
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"]
        not in {
            "CDependentResidueExternalTargetStillOpen",
            "ActualNoncanonicalConstructorFormulaStillOpen",
            "DStructureRankinStillIndependent",
        }
    )
    any_constructor_match = any(row["matches_constructor_formula"] for row in matches)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_external_lemma_parameter_match_router",
        "status": "external_lemmas_do_not_close_self_contained_constructor_formula",
        "external_lemma_parameter_match_boundary_closed": boundary_closed,
        "external_primary_sources_identified": True,
        "external_lemmas_match_constructor_formula": any_constructor_match,
        "external_lemmas_close_self_contained_remainder": False,
        "external_spectral_atom_accepted": False,
        "actual_noncanonical_primitive_constructor_formula_proved": False,
        "row_column_unconditional_closed": False,
        "previous_input": "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn",
        "latest_internal_subinput": "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn",
        "latest_external_subinput": "CDependentResidueWeightSpectralCancellationInput",
        "latest_conditional_basis": (
            "(ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn OR "
            "CDependentResidueWeightSpectralCancellationInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "comparison_law": (
            "外部 DI/BFI/Kuznetsov 引理与当前自足原子处在不同层级：外部引理处理 completion "
            "之后的 Kloosterman/AP/谱平均，要求系数或 residue 权重已经给定；当前自足原子要求在 "
            "Cauchy/dispersion 前写出 actual noncanonical alpha/delta 的 primitive constructor。"
            "因此外部引理不能替代该公式，只能作为 external_spectral 分支的候选。"
        ),
        "plain_conclusion": (
            "与外部引理逐项对比后，最新完全自足剩余没有被外部定理消掉：DI/BFI/Kuznetsov "
            "只能处理完成后的谱平均或 AP/well-factorable 分布，不能生成 pre-Cauchy actual "
            "noncanonical summand emitter。完全自足剩余仍是 "
            "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn。"
        ),
        "external_sources": external_sources(),
        "match_rows": matches,
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
    """写出 Markdown 研究证书。"""
    lines: list[str] = [
        "# Prime Matrix clean-core 外部引理参数匹配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"external_lemma_parameter_match_boundary_closed={fmt_bool(result['external_lemma_parameter_match_boundary_closed'])}",
        f"external_lemmas_match_constructor_formula={fmt_bool(result['external_lemmas_match_constructor_formula'])}",
        f"external_lemmas_close_self_contained_remainder={fmt_bool(result['external_lemmas_close_self_contained_remainder'])}",
        f"external_spectral_atom_accepted={fmt_bool(result['external_spectral_atom_accepted'])}",
        f"actual_noncanonical_primitive_constructor_formula_proved={fmt_bool(result['actual_noncanonical_primitive_constructor_formula_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
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
            "## 2. 对比律",
            "",
            result["comparison_law"],
            "",
            "## 3. 外部来源",
            "",
            "| source | object | usable for | not usable for | url |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["external_sources"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(row["source"]),
                    table_cell(row["object"]),
                    table_cell(row["usable_for"]),
                    table_cell(row["not_usable_for"]),
                    table_cell(row["url"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 参数匹配表",
            "",
            "| lemma family | structure match | parameter match | constructor match | reason | route |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["match_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['lemma_family'])}`",
                    table_cell(row["structure_match"]),
                    table_cell(row["parameter_match"]),
                    f"`{fmt_bool(row['matches_constructor_formula'])}`",
                    table_cell(row["reason"]),
                    table_cell(row["route"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 当前结论",
            "",
            "外部引理参数匹配没有推进为完全自足闭合；它只确认外部谱路线的边界位置。",
            "当前自足证明仍必须直接写出 actual noncanonical primitive constructor formula，",
            "并且 DStructure/Rankin 独立验收门仍未完成。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(
        description="Compare external lemmas with the clean-core constructor formula atom."
    )
    parser.add_argument("--current", type=Path, default=DEFAULT_CURRENT)
    parser.add_argument("--spectral", type=Path, default=DEFAULT_SPECTRAL)
    parser.add_argument("--primary-nogo", type=Path, default=DEFAULT_PRIMARY_NOGO)
    parser.add_argument("--external-index", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--kls-template", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--clean-kls", type=Path, default=DEFAULT_CLEAN_KLS)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        current_path=args.current,
        spectral_path=args.spectral,
        primary_nogo_path=args.primary_nogo,
        external_index_path=args.external_index,
        kls_template_path=args.kls_template,
        clean_kls_path=args.clean_kls,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_internal_subinput"])


if __name__ == "__main__":
    main()
