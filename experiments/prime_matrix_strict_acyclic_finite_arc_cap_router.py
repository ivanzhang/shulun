#!/usr/bin/env python3
"""生成 strict acyclic 有限弧 cap 质量界/命名回流路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_finite_arc_cap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-finite-arc-cap-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-finite-arc-cap-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-finite-arc-cap-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-pdec-input-materialization-router.md",
    "prime-matrix-pdec-cap-finite-arc-transverse-router.md",
    "prime-matrix-pdec-cap-transverse-clean-reduction-router.md",
    "prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.md",
    "prime-matrix-lowmod-finite-arc-cap-reduction-router.md",
    "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.md",
    "prime-matrix-triad-a1-clean-kls-external-input-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    before = "AcyclicFiniteArcCapMassBoundsOrNamedReturn"
    after = "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    canonical_package = (
        "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy "
        "AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity "
        "AND AcyclicSeedNoSourceReplacementOrPayloadCreation "
        "AND TerminalCertificateSameSetPushforwardIdentity "
        "AND NoNoncanonicalPayloadSurvivesCanonicalProjection"
    )
    terminal_gap_after = f"({canonical_package}) OR {after}"
    strict_basis_with_external_mertens = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"({terminal_gap_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "AcyclicFiniteArcCapActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层 direct PDEC 剩余为同一 g_B 上的有限循环弧 cap 质量上界或命名回流。",
            "remaining": before,
        },
        {
            "gate": "SameSetCountVectorImported",
            "closed": True,
            "proved": True,
            "meaning": "已固定 acyclic formal unit G、坏窗集合 B、同一 count vector g_B 与质量 M。",
            "remaining": "只允许在同一 g_B 上做弧 cap 判定。",
        },
        {
            "gate": "FiniteArcRankOneSliceImported",
            "closed": True,
            "proved": True,
            "meaning": "任意方向帽都是非平凡字符有限像上的循环弧预像，即秩一切片。",
            "remaining": "检查弧内横向变量。",
        },
        {
            "gate": "LowTransverseSupportNamedReturn",
            "closed": True,
            "proved": True,
            "meaning": "高质量弧若由低横向支撑、孤立短窗、列位移或固定壳承担，则生成 SAE/ColumnCRT/fixed-shell PDEC return。",
            "remaining": "无；它不保留为 cap-stable PDEC 核。",
        },
        {
            "gate": "PersistentTransverseBiasNamedReturn",
            "closed": True,
            "proved": True,
            "meaning": "高质量弧若有持久横向偏斜，则弧指标并入签名，得到 refined/new-layer PDEC；有限层细化无循环。",
            "remaining": "无；它回到 PDEC 命名路线。",
        },
        {
            "gate": "LowModArcClassificationImported",
            "closed": True,
            "proved": True,
            "meaning": "固定轮弧、新增层弧、高模平坦弧分别进入 W-unit PDEC、new-layer PDEC、flat DLS/KLS。",
            "remaining": "高模平坦弧进入 clean DLS，不再是 PDEC 弧 cap 独立输入。",
        },
        {
            "gate": "TransverseFlatResidualCleanAdmission",
            "closed": True,
            "proved": True,
            "meaning": "若弧内没有低支撑、持久偏斜或列/壳集中，则剩余是横向 L2-flat clean residual，准入 DirectAcyclicCleanKLS/DLS。",
            "remaining": after,
        },
        {
            "gate": "FiniteArcNoUnnamedExitClosed",
            "closed": True,
            "proved": True,
            "meaning": "有限弧 cap 不能作为第四类无名出口；它要么命名回流，要么成为 clean DLS/KLS residual。",
            "remaining": "证明 clean DLS/KLS 吸收。",
        },
        {
            "gate": "AcyclicFiniteArcIndependentInputRemoved",
            "closed": True,
            "proved": True,
            "meaning": "AcyclicFiniteArcCapMassBoundsOrNamedReturn 作为独立 PDEC 剩余已删除；未闭合部分转到 direct clean KLS/DLS。",
            "remaining": after,
        },
        {
            "gate": "DirectAcyclicPDECDualProved",
            "closed": True,
            "proved": False,
            "meaning": "PDEC 分支已无独立有限弧逃逸，但没有证明所有弧质量均低于阈值；平坦弧转入 clean 分支。",
            "remaining": after,
        },
        {
            "gate": "DirectCleanKLSStillOpen",
            "closed": True,
            "proved": False,
            "meaning": "当前真正最窄终端硬点变成 strict acyclic clean residual 的内部 KLS/DLS 大筛估计或命名回流。",
            "remaining": after,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_finite_arc_cap_router",
        "status": "acyclic_finite_arc_cap_independent_input_removed_clean_kls_remaining",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "same_set_count_vector_imported": True,
        "finite_arc_rank_one_slice_imported": True,
        "low_transverse_support_named_return_closed": True,
        "persistent_transverse_bias_named_return_closed": True,
        "lowmod_arc_classification_imported": True,
        "transverse_flat_residual_clean_admission_closed": True,
        "acyclic_finite_arc_no_unnamed_exit_closed": True,
        "acyclic_finite_arc_independent_input_removed": True,
        "acyclic_finite_arc_cap_mass_bounds_proved": False,
        "direct_acyclic_same_set_pdec_dual_proved": False,
        "direct_acyclic_clean_kls_dls_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": before,
        "terminal_gap_after_router": terminal_gap_after,
        "strict_self_contained_math_basis_after_router": strict_basis_with_external_mertens,
        "next_attack_contract": {
            "name": "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
            "must_prove": [
                "对已剥离 PDEC/SAE/ColumnCRT 的 acyclic clean residual 验证 K1--K9 clean admission",
                "给出同一 formal unit 上的 L2-flat 系数账本和窗口化 Kloosterman/dispersion 参数映射",
                "证明内部 DLS/KLS 大筛吸收，或把失败命名回流到 PDEC/SAE/ColumnCRT/Multiplicity",
                "若使用外部 DI/BFI/Kuznetsov 定理，必须明确标记为外部条件路线，不能声明严格自足闭合",
            ],
            "cannot_use_as_proof": [
                "把有限弧无第四出口当成 clean 大筛估计",
                "把 canonical-source NC-BLK 吸收直接导入 acyclic/noncanonical clean residual",
                "把 K1--K9 准入当成大筛证明；准入后仍需 KLS/DLS 界",
                "用有限实验中弧 cap 消失替代全局横向平坦估计",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步直接攻 `AcyclicFiniteArcCapMassBoundsOrNamedReturn`。有限弧是同一 finite formal unit 中的秩一字符弧；"
            "高质量弧若有低横向支撑、持久横向偏斜、列/壳集中或新增层偏斜，都会命名回流到 SAE、ColumnCRT 或 refined/new-layer PDEC；"
            "若这些缺陷全部剥离，剩余就是横向 L2-flat clean residual，必须进入 `DirectAcyclicCleanKLSDLSEstimateWithNamedReturn`。"
            "因此有限弧 cap 不再是独立剩余，但 clean KLS/DLS 估计仍未证明，完整命题仍未闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic 有限弧 cap 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"empirical_absence_not_used={str(result['empirical_absence_not_used']).lower()}",
        f"same_set_count_vector_imported={str(result['same_set_count_vector_imported']).lower()}",
        f"finite_arc_rank_one_slice_imported={str(result['finite_arc_rank_one_slice_imported']).lower()}",
        f"low_transverse_support_named_return_closed={str(result['low_transverse_support_named_return_closed']).lower()}",
        f"persistent_transverse_bias_named_return_closed={str(result['persistent_transverse_bias_named_return_closed']).lower()}",
        f"transverse_flat_residual_clean_admission_closed={str(result['transverse_flat_residual_clean_admission_closed']).lower()}",
        f"acyclic_finite_arc_no_unnamed_exit_closed={str(result['acyclic_finite_arc_no_unnamed_exit_closed']).lower()}",
        f"acyclic_finite_arc_independent_input_removed={str(result['acyclic_finite_arc_independent_input_removed']).lower()}",
        f"acyclic_finite_arc_cap_mass_bounds_proved={str(result['acyclic_finite_arc_cap_mass_bounds_proved']).lower()}",
        f"direct_acyclic_same_set_pdec_dual_proved={str(result['direct_acyclic_same_set_pdec_dual_proved']).lower()}",
        f"direct_acyclic_clean_kls_dls_proved={str(result['direct_acyclic_clean_kls_dls_proved']).lower()}",
        f"strict_terminal_family_proved={str(result['strict_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. 有限弧三分",
        "",
        "```text",
        "finite arc cap chi^{-1}(I) inside same g_B",
        "  low transverse support / short sparse / column-shell concentration",
        "    => SAE / ColumnCRT / fixed-shell PDEC return",
        "  persistent transverse or new-layer bias",
        "    => refined PDEC / new-layer PDEC return",
        "  otherwise",
        "    => transverse L2-flat clean residual",
        "    => DirectAcyclicCleanKLS/DLS",
        "```",
        "",
        "## 2. 终端门更新",
        "",
        "更新前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "更新后：",
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
