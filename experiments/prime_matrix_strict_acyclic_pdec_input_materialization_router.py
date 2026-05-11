#!/usr/bin/env python3
"""生成 strict acyclic same-set PDEC 输入物化路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_pdec_input_materialization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-pdec-input-materialization-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-pdec-input-materialization-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-pdec-input-materialization-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-branch-or-direct-pdec-router.md",
    "prime-matrix-universal-formal-unit-extractor-router.md",
    "prime-matrix-formal-unit-source-record-router.md",
    "prime-matrix-formal-unit-partition-coverage-router.md",
    "prime-matrix-canonical-formal-unit-hash-stability-router.md",
    "prime-matrix-terminal-certificate-package-compression-router.md",
    "prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.md",
    "prime-matrix-pdec-cap-uniform-cap-finite-basis-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    before = (
        "AcyclicSameSetPDECInputMaterializationAndMassLedger "
        "AND AcyclicPDECDualCapLocalizationAndNoFourthExit "
        "AND AcyclicFiniteArcCapMassBoundsOrNamedReturn"
    )
    after = "AcyclicFiniteArcCapMassBoundsOrNamedReturn"
    terminal_gap_after = (
        "(AcyclicSeedCanonicalBranchAdmissionBeforeCauchy "
        "AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity "
        "AND AcyclicSeedNoSourceReplacementOrPayloadCreation "
        "AND TerminalCertificateSameSetPushforwardIdentity "
        "AND NoNoncanonicalPayloadSurvivesCanonicalProjection) "
        f"OR {after} "
        "OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    )
    strict_basis_with_external_mertens = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"({terminal_gap_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "AcyclicPDECInputMaterializationActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 direct acyclic PDEC 的首个原子定为同集输入物化与质量账本。",
            "remaining": "AcyclicSameSetPDECInputMaterializationAndMassLedger。",
        },
        {
            "gate": "UniversalExtractorImported",
            "closed": True,
            "proved": True,
            "meaning": "任意假设早期零行 witness 都可产出有限、无漏、可哈希的 formal unit records。",
            "remaining": "把这些 records 专门读取为 PDEC count vector。",
        },
        {
            "gate": "FormalUnitRecordSchemaImported",
            "closed": True,
            "proved": True,
            "meaning": "每个 formal unit record 含 witness、family、window、phase、branch 和 no-loss return 字段。",
            "remaining": "在 PDEC 分支中指定坏窗集合 B 与有限签名群 G。",
        },
        {
            "gate": "BadWindowSetDefined",
            "closed": True,
            "proved": True,
            "meaning": "对进入 direct PDEC 的 acyclic terminal certificate，取 B 为同一 formal unit 中未命名回流的坏窗义务集合。",
            "remaining": "无；改变 B 的操作必须变成 return record。",
        },
        {
            "gate": "FiniteSignatureGroupDefined",
            "closed": True,
            "proved": True,
            "meaning": "取 G 为 formal unit key 中的有限相位/签名商；hash stability 保证分割和回流不改名。",
            "remaining": "无；跨 G 的项必须重新登记或回流。",
        },
        {
            "gate": "SameCountVectorConstructed",
            "closed": True,
            "proved": True,
            "meaning": "定义 g_B(t)=同一 B 内落在签名 t 的坏窗质量总和；U_CRT、L_PDEC、M 均只作用在此 g_B 上。",
            "remaining": "无；不同 g 的比较被禁止。",
        },
        {
            "gate": "CapacityMultiplierSameSetDisciplinePreserved",
            "closed": True,
            "proved": True,
            "meaning": "容量乘子只登记在同一 g_B、同一 M、同一 formal unit 上；阈值迁移需命名回流。",
            "remaining": "无；只剩容量估计。",
        },
        {
            "gate": "NoLossReturnProtectsMassLedger",
            "closed": True,
            "proved": True,
            "meaning": "删除、投影、quotient、重复合并若不保留 g_B，必须显式进入 PDEC/SAE/ColumnCRT/CleanKLS return。",
            "remaining": "无；这给出 PDEC 输入账本的同集性。",
        },
        {
            "gate": "AcyclicSameSetPDECInputMaterialized",
            "closed": True,
            "proved": True,
            "meaning": "direct acyclic PDEC 的同集输入物化闭合：B、G、g_B、M、U_CRT、L_PDEC 口径固定。",
            "remaining": "AcyclicPDECDualCapLocalizationAndNoFourthExit。",
        },
        {
            "gate": "DualCapLocalizationNoFourthExitClosed",
            "closed": True,
            "proved": True,
            "meaning": "有限 LP/帽定位给出 dual cap；终端证书压缩保证它只能回流 PDEC/SAE/ColumnCRT/CleanKLS，不能成为第四出口。",
            "remaining": "仍需证明有限弧 cap 质量上界，或执行这些命名回流。",
        },
        {
            "gate": "FiniteArcCapEstimateStillOpen",
            "closed": True,
            "proved": False,
            "meaning": "真正剩余是对每个 acyclic formal unit、非平凡字符和有限循环弧证明 cap 质量低于阈值，或输出命名回流。",
            "remaining": after,
        },
        {
            "gate": "DirectAcyclicPDECCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "direct acyclic PDEC 已越过输入物化和 dual-cap 定位，但未完成有限弧 cap 质量估计。",
            "remaining": after,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_pdec_input_materialization_router",
        "status": "acyclic_same_set_pdec_input_materialized_finite_arc_cap_bounds_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "universal_formal_unit_extractor_imported": True,
        "formal_unit_source_record_imported": True,
        "hash_stability_imported": True,
        "terminal_package_compression_imported": True,
        "registered_capacity_multiplier_discipline_imported": True,
        "bad_window_set_defined": True,
        "finite_signature_group_defined": True,
        "same_count_vector_constructed": True,
        "acyclic_same_set_pdec_input_materialized": True,
        "acyclic_pdec_dual_cap_localization_no_fourth_exit_proved": True,
        "acyclic_finite_arc_cap_mass_bounds_proved": False,
        "direct_acyclic_same_set_pdec_dual_proved": False,
        "direct_acyclic_clean_kls_dls_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "direct_pdec_before_router": before,
        "direct_pdec_after_router": after,
        "terminal_gap_after_router": terminal_gap_after,
        "strict_self_contained_math_basis_after_router": strict_basis_with_external_mertens,
        "next_attack_contract": {
            "name": "AcyclicFiniteArcCapMassBoundsOrNamedReturn",
            "must_prove": [
                "固定 acyclic formal unit G 与同集 count vector g_B 后，列出所有非平凡字符 chi 与有限循环弧 I",
                "证明 g_B(chi^{-1}(I)) 低于 PDEC 帽定位阈值 (L_PDEC-alpha M)/(1-alpha)",
                "若某弧超过阈值，必须把该弧物化为 SAE、refined PDEC、ColumnCRT 或 CleanKLS return",
                "证明有限弧细化不会产生同层无限循环；升层必须进入 new-layer PDEC/CleanKLS 命名路线",
            ],
            "cannot_use_as_proof": [
                "只说 dual cap 存在；dual cap 是失败证书，不是排斥证书",
                "使用 canonical-source cap 上界覆盖 acyclic/noncanonical formal unit",
                "在弧质量估计中更换 B、G、g_B 或 M",
                "把有限实验样本中没有高质量弧当作全局证明",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步关闭 direct acyclic PDEC 的首个输入物化硬点：由普遍 formal unit 抽取、source record schema、"
            "hash stability、no-loss return 和容量乘子纪律，可在假设早期零行分支中定义同一坏窗集合 B、有限签名群 G、"
            "同一 count vector g_B 与同一质量 M。有限 LP/帽定位和终端证书压缩也关闭了 dual-cap 无第四出口。"
            "direct PDEC 的真正剩余因此压成一个原子：AcyclicFiniteArcCapMassBoundsOrNamedReturn。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic PDEC 输入物化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"empirical_absence_not_used={str(result['empirical_absence_not_used']).lower()}",
        f"universal_formal_unit_extractor_imported={str(result['universal_formal_unit_extractor_imported']).lower()}",
        f"same_count_vector_constructed={str(result['same_count_vector_constructed']).lower()}",
        f"acyclic_same_set_pdec_input_materialized={str(result['acyclic_same_set_pdec_input_materialized']).lower()}",
        f"acyclic_pdec_dual_cap_localization_no_fourth_exit_proved={str(result['acyclic_pdec_dual_cap_localization_no_fourth_exit_proved']).lower()}",
        f"acyclic_finite_arc_cap_mass_bounds_proved={str(result['acyclic_finite_arc_cap_mass_bounds_proved']).lower()}",
        f"direct_acyclic_same_set_pdec_dual_proved={str(result['direct_acyclic_same_set_pdec_dual_proved']).lower()}",
        f"strict_terminal_family_proved={str(result['strict_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. 输入物化公式",
        "",
        "```text",
        "witness W -> finite formal unit records -> select direct-PDEC unit (B,G)",
        "g_B(t) := total bad-window mass in B with signature t in G",
        "U_CRT = U_CRT(g_B),  L_PDEC = L_PDEC(g_B),  M = sum_t g_B(t)",
        "```",
        "",
        "所有比较都在同一个 `g_B` 上进行。若删除、投影、quotient 或回流改变 `B/G/g_B/M`，它不能继续留在本 PDEC 输入内，必须成为命名 return。",
        "",
        "## 2. PDEC 线更新",
        "",
        "更新前：",
        "",
        "```text",
        result["direct_pdec_before_router"],
        "```",
        "",
        "更新后：",
        "",
        "```text",
        result["direct_pdec_after_router"],
        "```",
        "",
        "总终端门更新为：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "## 3. 判定表",
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
            "## 4. 最新严格基",
            "",
            "若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "## 5. 下一主攻合同",
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
