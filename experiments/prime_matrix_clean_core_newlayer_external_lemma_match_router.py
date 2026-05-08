#!/usr/bin/env python3
"""Prime Matrix clean-core new-layer 与外部闭合引理参数匹配路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_newlayer_external_lemma_match_router.py

输出：
  docs/monograph/prime-matrix-clean-core-newlayer-external-lemma-match-router.json
  docs/monograph/prime-matrix-clean-core-newlayer-external-lemma-match-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_LOWPHASE = DOCS / "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.json"
DEFAULT_FULLS_EXT = DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
DEFAULT_CLEAN_KLS = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_PRIMARY_NOGO = DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
DEFAULT_NEWLAYER_MD = DOCS / "prime-matrix-dprc-newlayer-energy-dispersion.md"
DEFAULT_FOURIER_MD = DOCS / "prime-matrix-dprc-fourier-inheritance-classifier.md"
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-newlayer-external-lemma-match-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-newlayer-external-lemma-match-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希，便于归档复核。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_once(text: str, old: str, new: str) -> str:
    """只替换一次输入基中的原子名。"""
    if old not in text:
        return text
    return text.replace(old, new, 1)


def match_rows(
    fulls_ext: dict[str, Any],
    clean_kls: dict[str, Any],
    primary_nogo: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成外部闭合引理与 new-layer 原子的逐项匹配表。"""
    return [
        {
            "item": "proof_stage",
            "external_closed_lemma_side": "post_completion_flat_kloosterman_or_nonap_wfd_block",
            "current_newlayer_side": "pre_flat_admission_unit_fiber_fourier_concentration",
            "match": "stage_mismatch",
            "closed_by_external": False,
            "remaining": "ExactNewLayerFiberPDECProjectionMorphism",
            "reason": (
                "外部 KLS/FullS 引理从已完成、已给定系数、已通过 clean admission 的块开始；"
                "当前 new-layer 原子还要证明新增素因子 fiber 上的低维集中必给 PDEC。"
            ),
        },
        {
            "item": "frequency_support",
            "external_closed_lemma_side": "Kloosterman frequency h and inverse variable after CRT",
            "current_newlayer_side": "new-layer additive frequencies r not dividing h on W=rW0",
            "match": "partial_after_projection",
            "closed_by_external": False,
            "remaining": "NewLayerFrequencyToKLSVariableMap",
            "reason": (
                "KLS 模板能处理 CRT 后的逆元相位；但 r∤h 的新增层频率先要被证明能投影到同一 formal unit，"
                "否则它只是低模 fiber 偏斜而不是 KLS 输入。"
            ),
        },
        {
            "item": "coefficient_flatness",
            "external_closed_lemma_side": clean_kls.get(
                "self_contained_version_status",
                "open_at_kuznetsov_ls_atom_sc9",
            ),
            "current_newlayer_side": "unit-class conditioned residue weights before deleting PDEC spikes",
            "match": "requires_deletion_ledger",
            "closed_by_external": False,
            "remaining": "NewLayerNoConcentrationImpliesFlatAdmission",
            "reason": (
                "外部引理只吸收 L2-flat/diffuse 系数；新增层如果有低维尖峰，必须先登记为 new-layer PDEC，"
                "删除后才能声称剩余满足 flat admission。"
            ),
        },
        {
            "item": "projection_and_centering",
            "external_closed_lemma_side": (
                "FullS-KLS-ext absorbs uncentered non-projected non-AP WFD object"
                if fulls_ext.get("external_theorem_contract_closed")
                else "FullS-KLS-ext not accepted"
            ),
            "current_newlayer_side": "new-layer low-mod unit projection with BES danger thresholds",
            "match": "not_the_same_no_projection_statement",
            "closed_by_external": False,
            "remaining": "NewLayerFormalUnitIdentity",
            "reason": (
                "FullS 合同的 no-projection 是对 non-AP WFD 完成块说的；"
                "new-layer 仍需证明低模单位 fiber、BES 桶和 payment formal unit 是同一对象。"
            ),
        },
        {
            "item": "danger_thresholds",
            "external_closed_lemma_side": "mean-square or log-saving bound after admission",
            "current_newlayer_side": "BES high-L1 and high-L2 simultaneous positive pressure",
            "match": "requires_return_compatibility",
            "closed_by_external": False,
            "remaining": "BESDangerToPDECReturnOrFlatAdmission",
            "reason": (
                "外部谱平均不给出 BES 危险交集的命名回流；内部命题要求危险同步失败必须回到 PDEC/SAE/ColumnCRT/DLS。"
            ),
        },
        {
            "item": "primary_source_derivation",
            "external_closed_lemma_side": primary_nogo.get(
                "terminal_gap_after_router",
                "NewFullSTheoremInputOrAPSourceLift",
            ),
            "current_newlayer_side": "fully self-contained no-black-box route",
            "match": "not_closed_self_contained",
            "closed_by_external": False,
            "remaining": "SC9OrInternalNewLayerFlatDLSProof",
            "reason": (
                "现有 DI/BFI 主来源不能直接推出 full-S non-AP KLS-ext；"
                "即使外部合同版可用，完全自足版仍需内部谱大筛或等价新层分散证明。"
            ),
        },
    ]


def gate_rows(
    lowphase: dict[str, Any],
    fulls_ext: dict[str, Any],
    clean_kls: dict[str, Any],
    primary_nogo: dict[str, Any],
    newlayer_md: str,
    fourier_md: str,
    kls_template_md: str,
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成本轮边界判定表。"""
    lowphase_has_newlayer = "DLSNewLayerFourierConcentrationPDECReturn" in lowphase.get(
        "latest_internal_subinputs",
        [],
    )
    newlayer_energy_ready = "NewLayer Dispersion Clamp" in newlayer_md
    fourier_inheritance_ready = "Fourier Inheritance Clamp" in fourier_md
    kls_template_ready = "Theorem H7-KLS-ext" in kls_template_md
    return [
        {
            "gate": "CurrentNewLayerAtomPinned",
            "closed": lowphase_has_newlayer,
            "proved": False,
            "meaning": "LowPhase 已把最贴近结构材料的子口命名为新增轮层 Fourier 集中/PDEC 回流。",
            "remaining": "核对外部闭合引理能否替代该子口。",
        },
        {
            "gate": "ExternalFullSKLSContractClosedIfAccepted",
            "closed": fulls_ext.get("external_theorem_contract_closed") is True,
            "proved": False,
            "meaning": "FullS-KLS-ext 外部合同版可闭合完成后的 non-AP WFD full-S 块。",
            "remaining": "这只是外部定理版，不是完全自足版。",
        },
        {
            "gate": "CleanKLSAdmissionTemplateRegistered",
            "closed": clean_kls.get("external_kls_input_registered") is True
            and clean_kls.get("all_admission_verified_or_routed") is True,
            "proved": False,
            "meaning": "K1--K9 已说明失败项如何回流，全部通过时才可调用 KLS/DLS。",
            "remaining": "new-layer 分支必须证明自己满足这些准入条件或返回 PDEC。",
        },
        {
            "gate": "NewLayerEnergyIdentityAvailable",
            "closed": newlayer_energy_ready,
            "proved": False,
            "meaning": "新增层能量已由继承频率和 r 不整除 h 的新频率精确拆分。",
            "remaining": "能量恒等式还不是低维集中推出 PDEC 的证明。",
        },
        {
            "gate": "FourierInheritanceClampAvailable",
            "closed": fourier_inheritance_ready,
            "proved": False,
            "meaning": "强频率可判定为旧层继承或新增素因子层。",
            "remaining": "需证明新增层强频率的持久集中给出合法 new-layer PDEC 证书。",
        },
        {
            "gate": "ExternalKLSPhaseTemplateAvailable",
            "closed": kls_template_ready,
            "proved": False,
            "meaning": "外部 KLS 模板能处理 CRT 后标准逆元相位。",
            "remaining": "需证明 new-layer 低模频率删除后可变成该模板的平坦输入。",
        },
        {
            "gate": "PrimarySourceSelfContainedNoGoRetained",
            "closed": primary_nogo.get("terminal_gap_after_router")
            == "NewFullSTheoremInputOrAPSourceLift",
            "proved": True,
            "meaning": "现有 DI/BFI 主来源不能直接给出本文所需 full-S non-AP KLS-ext。",
            "remaining": "自足版仍需内部证明，或另立新外部定理输入。",
        },
        {
            "gate": "DirectExternalLemmaClosesNewLayer",
            "closed": False,
            "proved": False,
            "meaning": "外部闭合引理不能直接替代 DLSNewLayerFourierConcentrationPDECReturn。",
            "remaining": "ExactNewLayerFiberPDECProjectionMorphism AND NewLayerNoConcentrationImpliesFlatAdmission。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是完整晋级的独立验收门。",
            "remaining": "new-layer/flat DLS/signed 源锁完成后仍需独立验收。",
        },
    ]


def run(
    lowphase_path: Path,
    fulls_ext_path: Path,
    clean_kls_path: Path,
    primary_nogo_path: Path,
    newlayer_md_path: Path,
    fourier_md_path: Path,
    kls_template_path: Path,
    dstructure_path: Path,
) -> dict[str, Any]:
    """执行 new-layer 与外部引理匹配审计。"""
    paths = [
        lowphase_path,
        fulls_ext_path,
        clean_kls_path,
        primary_nogo_path,
        newlayer_md_path,
        fourier_md_path,
        kls_template_path,
        dstructure_path,
    ]
    lowphase = load_json(lowphase_path)
    fulls_ext = load_json(fulls_ext_path)
    clean_kls = load_json(clean_kls_path)
    primary_nogo = load_json(primary_nogo_path)
    newlayer_md = newlayer_md_path.read_text(encoding="utf-8")
    fourier_md = fourier_md_path.read_text(encoding="utf-8")
    kls_template_md = kls_template_path.read_text(encoding="utf-8")
    dstructure = load_json(dstructure_path)
    rows = gate_rows(
        lowphase=lowphase,
        fulls_ext=fulls_ext,
        clean_kls=clean_kls,
        primary_nogo=primary_nogo,
        newlayer_md=newlayer_md,
        fourier_md=fourier_md,
        kls_template_md=kls_template_md,
        dstructure=dstructure,
    )
    matches = match_rows(
        fulls_ext=fulls_ext,
        clean_kls=clean_kls,
        primary_nogo=primary_nogo,
    )
    old_atom = "DLSNewLayerFourierConcentrationPDECReturn"
    new_atoms = (
        "ExactNewLayerFiberPDECProjectionMorphism "
        "AND NewLayerNoConcentrationImpliesFlatAdmission"
    )
    latest_self_contained_basis = replace_once(
        lowphase.get("latest_self_contained_basis", ""),
        old_atom,
        new_atoms,
    )
    latest_conditional_basis = replace_once(
        lowphase.get("latest_conditional_basis", ""),
        old_atom,
        new_atoms,
    )
    return {
        "certificate_type": "clean_core_newlayer_external_lemma_match_router",
        "status": "newlayer_external_match_reduced_to_projection_morphism_and_flat_admission",
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path)
            for path in paths
        },
        "previous_newlayer_atom": old_atom,
        "terminal_gap_after_router": "ExactNewLayerFiberPDECProjectionMorphismAndFlatAdmission",
        "terminal_gap_expansion": [
            "ExactNewLayerFiberPDECProjectionMorphism",
            "NewLayerNoConcentrationImpliesFlatAdmission",
        ],
        "external_closed_lemma_accepted_branch": fulls_ext.get(
            "external_theorem_contract_closed",
            False,
        ),
        "direct_external_lemma_closes_newlayer": False,
        "self_contained_newlayer_closed": False,
        "row_column_unconditional_closed": False,
        "rows": rows,
        "match_rows": matches,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "latest_conditional_basis": latest_conditional_basis,
        "latest_self_contained_basis": latest_self_contained_basis,
        "structural_law": (
            "External KLS/FullS lemmas close only a prepared flat spectral block. "
            "The current new-layer atom sits one level earlier: it must first prove that "
            "low-dimensional concentration on the added wheel fiber is an actual PDEC "
            "certificate, or that after deleting all such fibers the residual satisfies "
            "the clean flat-admission hypotheses. Therefore external closure can attach "
            "only after an exact new-layer projection/admission morphism, not directly at "
            "DLSNewLayerFourierConcentrationPDECReturn."
        ),
        "plain_conclusion": (
            "外部闭合引理是一台只吃“已准入平坦谱块”的机器；当前 new-layer 硬点还在把新增轮层 "
            "Fourier 低维集中转成 PDEC 证书、或把删除后的残余转成 flat-KLS 准入块。"
            "所以本轮没有宣称行/列命题闭合，而是把 new-layer 子口压成两个精确微输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写出 Markdown 报告。"""
    lines = [
        "# Prime Matrix clean-core new-layer 外部引理匹配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"direct_external_lemma_closes_newlayer={fmt_bool(result['direct_external_lemma_closes_newlayer'])}",
        f"self_contained_newlayer_closed={fmt_bool(result['self_contained_newlayer_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "因此当前子口更新为：",
        "",
        "```text",
        f"{result['previous_newlayer_atom']}",
        "  => ExactNewLayerFiberPDECProjectionMorphism",
        "     AND NewLayerNoConcentrationImpliesFlatAdmission.",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                proved=fmt_bool(bool(row["proved"])),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 参数匹配表",
            "",
            "| item | external closed lemma side | current new-layer side | match | closed by external | remaining | reason |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["match_rows"]:
        lines.append(
            "| `{item}` | {external} | {current} | `{match}` | `{closed}` | `{remaining}` | {reason} |".format(
                item=table_cell(row["item"]),
                external=table_cell(row["external_closed_lemma_side"]),
                current=table_cell(row["current_newlayer_side"]),
                match=table_cell(row["match"]),
                closed=fmt_bool(bool(row["closed_by_external"])),
                remaining=table_cell(row["remaining"]),
                reason=table_cell(row["reason"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新输入基",
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
            "## 5. 当前结论",
            "",
            "外部闭合引理与当前子口的参数比较给出一个硬边界：",
            "只要还没有 `ExactNewLayerFiberPDECProjectionMorphism`，就不能把新增轮层低维集中直接送入外部 KLS；",
            "只要还没有 `NewLayerNoConcentrationImpliesFlatAdmission`，就不能把“无集中”直接等同于 flat-DLS 可吸收。",
            "因此下一步最窄自足目标不是再找新的外部引用，而是证明这两个投影/准入微输入，之后 flat 分支才可与 KLS/DLS 终端对接。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lowphase-json", type=Path, default=DEFAULT_LOWPHASE)
    parser.add_argument("--fulls-ext-json", type=Path, default=DEFAULT_FULLS_EXT)
    parser.add_argument("--clean-kls-json", type=Path, default=DEFAULT_CLEAN_KLS)
    parser.add_argument("--primary-nogo-json", type=Path, default=DEFAULT_PRIMARY_NOGO)
    parser.add_argument("--newlayer-md", type=Path, default=DEFAULT_NEWLAYER_MD)
    parser.add_argument("--fourier-md", type=Path, default=DEFAULT_FOURIER_MD)
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        lowphase_path=args.lowphase_json,
        fulls_ext_path=args.fulls_ext_json,
        clean_kls_path=args.clean_kls_json,
        primary_nogo_path=args.primary_nogo_json,
        newlayer_md_path=args.newlayer_md,
        fourier_md_path=args.fourier_md,
        kls_template_path=args.kls_template_md,
        dstructure_path=args.dstructure_json,
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)


if __name__ == "__main__":
    main()
