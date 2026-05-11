#!/usr/bin/env python3
"""生成 strict acyclic canonical-admission / direct-PDEC 二选一路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_branch_or_direct_pdec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-branch-or-direct-pdec-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-branch-or-direct-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-branch-or-direct-pdec-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-canonical-embedding-router.md",
    "prime-matrix-strict-acyclic-canonical-lock-router.md",
    "prime-matrix-strict-acyclic-terminal-family-attack-router.md",
    "prime-matrix-strict-self-contained-dual-lane-final-router.md",
    "prime-matrix-pdec-cap-same-set-global-dual-router.md",
    "prime-matrix-self-contained-pdec-cap-boundary-lift-router.md",
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

    canonical_package = (
        "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy "
        "AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity "
        "AND AcyclicSeedNoSourceReplacementOrPayloadCreation "
        "AND TerminalCertificateSameSetPushforwardIdentity "
        "AND NoNoncanonicalPayloadSurvivesCanonicalProjection"
    )
    direct_pdec_before = "DirectAcyclicSameSetPDECCapDualCertificate"
    direct_pdec_after = (
        "AcyclicSameSetPDECInputMaterializationAndMassLedger "
        "AND AcyclicPDECDualCapLocalizationAndNoFourthExit "
        "AND AcyclicFiniteArcCapMassBoundsOrNamedReturn"
    )
    clean_fallback = "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    terminal_gap_after = (
        f"({canonical_package}) OR ({direct_pdec_after}) OR {clean_fallback}"
    )
    strict_basis_with_external_mertens = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"({terminal_gap_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "TwoLaneGateActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层留下二选一：证明 canonical-lock 的 seed 准入包，或转 direct acyclic same-set PDEC。",
            "remaining": "canonical package OR DirectAcyclicSameSetPDECCapDualCertificate。",
        },
        {
            "gate": "CanonicalBranchConditionalImplicationPinned",
            "closed": True,
            "proved": True,
            "meaning": "若 seed 因子图、同集推前和无 payload 残留全部成立，则可条件导入 canonical-source 终端闭合。",
            "remaining": "该项只是条件蕴含，不证明前提。",
        },
        {
            "gate": "CanonicalAdmissionCurrentCorpusStillOpen",
            "closed": True,
            "proved": False,
            "meaning": "当前材料未证明 acyclic seed 在 pre-Cauchy 层就是 canonical RIW/Buchstab source branch。",
            "remaining": "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy。",
        },
        {
            "gate": "CanonicalFactorMapCurrentCorpusStillOpen",
            "closed": True,
            "proved": False,
            "meaning": "当前材料未提交 pi_* mu_c = mu_a 的同测度有限因子图。",
            "remaining": "AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity。",
        },
        {
            "gate": "NoPayloadProjectionCurrentCorpusStillOpen",
            "closed": True,
            "proved": False,
            "meaning": "当前材料未证明 noncanonical payload 在 canonical 投影后无残留。",
            "remaining": "AcyclicSeedNoSourceReplacementOrPayloadCreation AND NoNoncanonicalPayloadSurvivesCanonicalProjection。",
        },
        {
            "gate": "DirectPDECSelectedAsLiveStrictBranch",
            "closed": True,
            "proved": True,
            "meaning": "在不偷渡 canonical 前提的 strict acyclic/noncanonical 分支中，下一主攻口必须是 direct same-set PDEC 或 direct CleanKLS；优先攻 PDEC。",
            "remaining": direct_pdec_before,
        },
        {
            "gate": "RegisteredCapacityMultiplierImported",
            "closed": True,
            "proved": True,
            "meaning": "容量乘子纪律已在严格二线终局过滤中登记，direct PDEC 必须使用同一阈值和同一坏窗口径。",
            "remaining": "仍需物化 acyclic PDEC 输入。",
        },
        {
            "gate": "SameSetPDECProtocolImportedWithScope",
            "closed": True,
            "proved": True,
            "meaning": "PDEC 比较的形式协议是同一坏窗计数向量上计算 U_CRT 与 L_PDEC；若失败必须输出 dual cap。",
            "remaining": "该协议不自动证明 acyclic 终端家族满足输入物化和 cap 上界。",
        },
        {
            "gate": "AcyclicPDECInputMaterializationPinned",
            "closed": True,
            "proved": False,
            "meaning": "必须从 acyclic terminal certificate 生成同一 formal unit、同一坏窗集合、同一质量 M 的 PDEC count vector。",
            "remaining": "AcyclicSameSetPDECInputMaterializationAndMassLedger。",
        },
        {
            "gate": "DualCapLocalizationPinned",
            "closed": True,
            "proved": False,
            "meaning": "若 acyclic PDEC 不等式失败，必须定位到有限方向帽 dual cap，并证明它只能命名回流而不能作为第四出口。",
            "remaining": "AcyclicPDECDualCapLocalizationAndNoFourthExit。",
        },
        {
            "gate": "FiniteArcMassBoundsPinned",
            "closed": True,
            "proved": False,
            "meaning": "direct acyclic PDEC 的真正估计硬点是所有有限循环弧 cap 质量上界，或输出 PDEC/SAE/ColumnCRT/CleanKLS 命名回流。",
            "remaining": "AcyclicFiniteArcCapMassBoundsOrNamedReturn。",
        },
        {
            "gate": "DirectAcyclicPDECCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料闭合了 canonical-source PDEC 边界，但没有闭合 acyclic/noncanonical 同集 PDEC 证书。",
            "remaining": direct_pdec_after,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_branch_or_direct_pdec_router",
        "status": "canonical_admission_open_direct_acyclic_pdec_selected_and_atomized",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "canonical_branch_conditional_implication_pinned": True,
        "acyclic_seed_canonical_branch_admission_proved": False,
        "acyclic_seed_finite_factor_map_weight_identity_proved": False,
        "acyclic_seed_no_source_replacement_proved": False,
        "terminal_certificate_same_set_pushforward_proved": False,
        "no_noncanonical_payload_survives_projection_proved": False,
        "direct_acyclic_same_set_pdec_selected": True,
        "registered_capacity_multiplier_discipline_imported": True,
        "same_set_pdec_protocol_imported_with_scope": True,
        "acyclic_same_set_pdec_input_materialized": False,
        "acyclic_pdec_dual_cap_localization_no_fourth_exit_proved": False,
        "acyclic_finite_arc_cap_mass_bounds_proved": False,
        "direct_acyclic_same_set_pdec_dual_proved": False,
        "direct_acyclic_clean_kls_dls_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "canonical_package": canonical_package,
        "direct_pdec_before_router": direct_pdec_before,
        "direct_pdec_after_router": direct_pdec_after,
        "terminal_gap_after_router": terminal_gap_after,
        "strict_self_contained_math_basis_after_router": strict_basis_with_external_mertens,
        "next_attack_contract": {
            "name": "AcyclicSameSetPDECInputMaterializationAndMassLedger",
            "must_prove": [
                "从假设早期零行反例链的 acyclic terminal certificate 中定义唯一坏窗集合 B 和有限 formal unit G",
                "构造同一 count vector g_B(t)，使 U_CRT、L_PDEC、M、capacity multiplier 全部作用在同一个 g_B 上",
                "证明删除、投影、回流、quotient 不改变坏窗集合口径；改变则必须命名为 PDEC/SAE/ColumnCRT/CleanKLS return",
                "若 U_CRT >= L_PDEC，则输出有限方向帽 dual cap，并进入 finite-arc cap mass bounds 或命名回流",
            ],
            "cannot_use_as_proof": [
                "把 canonical-source PDEC-CAP 闭合直接用于 acyclic/noncanonical 分支",
                "把 source 哈希稳定当成同集 count vector 物化",
                "在 U_CRT 与 L_PDEC 中使用不同坏窗集合或不同推前质量",
                "把 dual cap 的存在当成矛盾；必须继续证明 cap 上界或命名回流",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步把二选一硬点做成严格分叉：canonical 路线只有在 seed 因子图、同集推前、无 payload 残留全部证明后才可导入；"
            "当前语料没有证明这些前提。因此 strict acyclic/noncanonical 活动分支优先转入 DirectAcyclicSameSetPDECCapDualCertificate。"
            "该证书又被压成三项：先物化同一坏窗集合上的 PDEC 输入和质量账本；再证明 dual-cap 定位无第四出口；"
            "最后证明有限循环弧 cap 质量上界或命名回流。命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic canonical/direct-PDEC 二选一路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"empirical_absence_not_used={str(result['empirical_absence_not_used']).lower()}",
        f"canonical_branch_conditional_implication_pinned={str(result['canonical_branch_conditional_implication_pinned']).lower()}",
        f"acyclic_seed_canonical_branch_admission_proved={str(result['acyclic_seed_canonical_branch_admission_proved']).lower()}",
        f"acyclic_seed_finite_factor_map_weight_identity_proved={str(result['acyclic_seed_finite_factor_map_weight_identity_proved']).lower()}",
        f"direct_acyclic_same_set_pdec_selected={str(result['direct_acyclic_same_set_pdec_selected']).lower()}",
        f"acyclic_same_set_pdec_input_materialized={str(result['acyclic_same_set_pdec_input_materialized']).lower()}",
        f"direct_acyclic_same_set_pdec_dual_proved={str(result['direct_acyclic_same_set_pdec_dual_proved']).lower()}",
        f"direct_acyclic_clean_kls_dls_proved={str(result['direct_acyclic_clean_kls_dls_proved']).lower()}",
        f"strict_terminal_family_proved={str(result['strict_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. 二选一分叉",
        "",
        "canonical 条件包：",
        "",
        "```text",
        result["canonical_package"],
        "```",
        "",
        "direct PDEC 原子化前：",
        "",
        "```text",
        result["direct_pdec_before_router"],
        "```",
        "",
        "direct PDEC 原子化后：",
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
