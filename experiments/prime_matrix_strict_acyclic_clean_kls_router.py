#!/usr/bin/env python3
"""生成 strict acyclic clean KLS/DLS 终端原子化路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_clean_kls_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-clean-kls-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-clean-kls-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-clean-kls-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-finite-arc-cap-router.md",
    "prime-matrix-triad-a1-clean-kls-external-input-router.md",
    "prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.md",
    "prime-matrix-clean-core-newlayer-external-lemma-match-router.md",
    "prime-matrix-clean-core-bes-dls-named-return-router.md",
    "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.md",
    "prime-matrix-ncblk-boundary-reconciliation-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    before = "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    after = (
        "AcyclicWindowedKloostermanDLSInternalEstimate "
        "OR AcceptExternalDIBFIKuznetsovNoProjectionWindowCertificate"
    )
    strict_after = "AcyclicWindowedKloostermanDLSInternalEstimate"
    canonical_package = (
        "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy "
        "AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity "
        "AND AcyclicSeedNoSourceReplacementOrPayloadCreation "
        "AND TerminalCertificateSameSetPushforwardIdentity "
        "AND NoNoncanonicalPayloadSurvivesCanonicalProjection"
    )
    terminal_gap_after = f"({canonical_package}) OR {strict_after}"
    strict_basis_with_external_mertens = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"({terminal_gap_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "DirectAcyclicCleanKLSActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 finite-arc 平坦剩余转为 strict acyclic clean KLS/DLS 终端。",
            "remaining": before,
        },
        {
            "gate": "NamedDefectsAlreadyPeeled",
            "closed": True,
            "proved": True,
            "meaning": "PDEC/SAE/ColumnCRT/Multiplicity/new-layer 低维缺陷已由 finite-arc 与 no-loss return 体系剥离。",
            "remaining": "只剩 clean residual。",
        },
        {
            "gate": "K1K9AdmissionClosedByConstruction",
            "closed": True,
            "proved": True,
            "meaning": "clean residual 的 K1--K9 准入条件成立；任一失败都按定义回流到已命名出口。",
            "remaining": "准入不是大筛估计。",
        },
        {
            "gate": "L2FlatCoefficientLedgerClosed",
            "closed": True,
            "proved": True,
            "meaning": "所有固定有限投影的高原子、短窗、低相位和新增层集中已剥离，剩余给出 L2-flat 系数账本。",
            "remaining": "需要把系数映射到标准窗口化 Kloosterman/DLS 模板。",
        },
        {
            "gate": "WindowedKloostermanTemplateRegistered",
            "closed": True,
            "proved": True,
            "meaning": "A1 clean KLS 模板已登记：clean dyadic formal unit 映射到 m, ell, d, R, h 与平滑权重窗口。",
            "remaining": "提交内部大筛估计或外部证书。",
        },
        {
            "gate": "CanonicalNCBLKImportBlocked",
            "closed": True,
            "proved": True,
            "meaning": "canonical-source NC-BLK 吸收只在 canonical RIW/Buchstab 来源分支内有效，不能导入 acyclic/noncanonical clean residual。",
            "remaining": "必须证明 acyclic 窗口化估计或走外部条件线。",
        },
        {
            "gate": "ExternalDIBFISeparated",
            "closed": True,
            "proved": True,
            "meaning": "外部 DI/BFI/Kuznetsov 可形成条件版本，但严格自足路线不能用外部黑箱关闭。",
            "remaining": "AcceptExternalDIBFIKuznetsovNoProjectionWindowCertificate 只属于外部线。",
        },
        {
            "gate": "DirectCleanKLSReducedToWindowedDLSAtom",
            "closed": True,
            "proved": False,
            "meaning": "direct clean KLS/DLS 的结构准入已闭合，剩余是窗口化 Kloosterman/DLS 内部估计。",
            "remaining": strict_after,
        },
        {
            "gate": "DirectAcyclicCleanKLSDLSEstimateProved",
            "closed": True,
            "proved": False,
            "meaning": "当前语料尚未提交 acyclic windowed Kloosterman/DLS 自足大筛估计。",
            "remaining": strict_after,
        },
        {
            "gate": "StrictTerminalFamilyProved",
            "closed": True,
            "proved": False,
            "meaning": "strict 终端家族仍未闭合；它现在卡在 canonical package 或 acyclic windowed DLS atom。",
            "remaining": terminal_gap_after,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_clean_kls_router",
        "status": "direct_acyclic_clean_kls_reduced_to_windowed_dls_atom_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "named_defects_peeled": True,
        "k1_k9_clean_admission_closed": True,
        "l2_flat_coefficient_ledger_closed": True,
        "windowed_kloosterman_template_registered": True,
        "canonical_ncblk_import_blocked": True,
        "external_dibfi_separated_for_condition_line": True,
        "acyclic_windowed_kloosterman_dls_internal_estimate_proved": False,
        "direct_acyclic_clean_kls_dls_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": before,
        "conditional_gap_after_router": after,
        "strict_gap_after_router": strict_after,
        "terminal_gap_after_router": terminal_gap_after,
        "strict_self_contained_math_basis_after_router": strict_basis_with_external_mertens,
        "next_attack_contract": {
            "name": "AcyclicWindowedKloostermanDLSInternalEstimate",
            "must_prove": [
                "把 acyclic clean residual 的 L2-flat 系数精确写入窗口化 Kloosterman/dispersion 双线性型",
                "给出同一 formal unit 下的模数、长度、光滑权、互素条件和坏窗质量规范化",
                "证明内部 DLS/Kuznetsov 型大筛界足以吸收 clean residual",
                "若估计失败，必须输出 point-load、short-window、low-phase 或 new-layer PDEC/SAE/ColumnCRT 命名回流",
            ],
            "cannot_use_as_proof": [
                "只说 K1--K9 已通过",
                "直接引用 canonical-source NC-BLK 吸收",
                "把外部 DI/BFI/Kuznetsov 黑箱写成严格自足证明",
                "把有限数值审计当作窗口化 DLS 全局估计",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步把 `DirectAcyclicCleanKLSDLSEstimateWithNamedReturn` 原子化。PDEC/SAE/ColumnCRT/Multiplicity 等低维缺陷已在上游剥离，"
            "所以 K1--K9 clean admission 与 L2-flat 系数账本可作为结构准入关闭；但这仍不是大筛证明。"
            "严格自足剩余压成 `AcyclicWindowedKloostermanDLSInternalEstimate`。外部 DI/BFI/Kuznetsov 可作为条件线，"
            "不能替代严格自足闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic clean KLS/DLS 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"empirical_absence_not_used={str(result['empirical_absence_not_used']).lower()}",
        f"named_defects_peeled={str(result['named_defects_peeled']).lower()}",
        f"k1_k9_clean_admission_closed={str(result['k1_k9_clean_admission_closed']).lower()}",
        f"l2_flat_coefficient_ledger_closed={str(result['l2_flat_coefficient_ledger_closed']).lower()}",
        f"windowed_kloosterman_template_registered={str(result['windowed_kloosterman_template_registered']).lower()}",
        f"acyclic_windowed_kloosterman_dls_internal_estimate_proved={str(result['acyclic_windowed_kloosterman_dls_internal_estimate_proved']).lower()}",
        f"direct_acyclic_clean_kls_dls_proved={str(result['direct_acyclic_clean_kls_dls_proved']).lower()}",
        f"strict_terminal_family_proved={str(result['strict_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. clean KLS 收缩",
        "",
        "```text",
        "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
        "  named low-dimensional defects already peeled",
        "  K1--K9 admission closes structurally",
        "  L2-flat coefficient ledger closes structurally",
        "  remaining strict atom:",
        "    AcyclicWindowedKloostermanDLSInternalEstimate",
        "```",
        "",
        "条件外部线为：",
        "",
        "```text",
        result["conditional_gap_after_router"],
        "```",
        "",
        "严格自足线只保留：",
        "",
        "```text",
        result["strict_gap_after_router"],
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
                gate=row["gate"],
                closed=str(row["closed"]).lower(),
                proved=str(row["proved"]).lower(),
                meaning=row["meaning"],
                remaining=row["remaining"],
            )
        )

    contract = result["next_attack_contract"]
    lines.extend(
        [
            "",
            "## 3. 最新严格基",
            "",
            "若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "## 4. 下一主攻合同",
            "",
            f"主攻名：`{contract['name']}`。",
            "",
            "必须证明：",
        ]
    )
    for item in contract["must_prove"]:
        lines.append(f"- {item}。")
    lines.append("")
    lines.append("不能作为证明使用：")
    for item in contract["cannot_use_as_proof"]:
        lines.append(f"- {item}。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
