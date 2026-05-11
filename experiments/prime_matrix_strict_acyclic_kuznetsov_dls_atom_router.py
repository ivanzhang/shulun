#!/usr/bin/env python3
"""生成 strict acyclic Kuznetsov/DLS 自足大筛原子路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_kuznetsov_dls_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.md",
    "prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.md",
    "prime-matrix-h3-dsb-hlc-kuznetsov-ls-atom-expansion.md",
    "prime-matrix-h3-dsb-hlc-kz-b-kuznetsov-trace-specialization.md",
    "prime-matrix-h3-dsb-hlc-kz-d-spectral-large-sieve-spine.md",
    "prime-matrix-ncblk-boundary-reconciliation-router.md",
    "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.md",
    "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    before = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
    after = "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"
    conditional_after = (
        "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom "
        "OR AcceptExternalFullSKLSExtWithNoProjectionCompatibility"
    )
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
            "gate": "KuznetsovDLSAtomActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 acyclic windowed DLS 估计压成自足 Kuznetsov/DLS 大筛原子。",
            "remaining": before,
        },
        {
            "gate": "KZAClosed",
            "closed": True,
            "proved": True,
            "meaning": "Kloosterman 模数平滑和 L2 bookkeeping 已由 H3/KZ-A 普通账本关闭。",
            "remaining": "无。",
        },
        {
            "gate": "KZBClosed",
            "closed": True,
            "proved": True,
            "meaning": "Kuznetsov trace formula 专门化已由 Poincare unfolding 与谱 Plancherel 内联推导。",
            "remaining": "无。",
        },
        {
            "gate": "KZCClosed",
            "closed": True,
            "proved": True,
            "meaning": "Bessel transform 窗口衰减已由 H3/KZ-C 账本关闭。",
            "remaining": "无。",
        },
        {
            "gate": "KZDClosed",
            "closed": True,
            "proved": True,
            "meaning": "谱大筛 KZ-D 已由 pretrace/LPC/GHLC Schur 链关闭，oldform/Eisenstein 只进入多对数账本。",
            "remaining": "无。",
        },
        {
            "gate": "KZEReducesToNCBLK",
            "closed": True,
            "proved": True,
            "meaning": "KZ-E/well-factorable dispersion 对数节省不能由裸谱大筛给出；既有 SC-9 前沿已压到 NC-BLK 或外部 DI/BFI。",
            "remaining": after,
        },
        {
            "gate": "CanonicalNCBLKAbsorptionBlockedForAcyclic",
            "closed": True,
            "proved": True,
            "meaning": "canonical-source NC-BLK 已被同集边界吸收，但 strict acyclic/noncanonical 分支不能偷渡该吸收。",
            "remaining": "需证明 acyclic actual block nonconcentration 或源反原子。",
        },
        {
            "gate": "GenericAntiAtomNoGoImported",
            "closed": True,
            "proved": True,
            "meaning": "generic full-S 自足反原子在 moving-delta 模型下为假；仅靠形式 WFD/Type/Fourier 模板不能推出 NC-BLK。",
            "remaining": "acyclic seed 必须提供更强的实际来源反原子，或接受外部 FullS-KLS-ext。",
        },
        {
            "gate": "ExternalContractSeparated",
            "closed": True,
            "proved": True,
            "meaning": "FullS-KLS-ext 或 DI/BFI/Kuznetsov 可作为外部合同线，但严格自足线需要内部来源反原子。",
            "remaining": "AcceptExternalFullSKLSExtWithNoProjectionCompatibility 属于条件线。",
        },
        {
            "gate": "SelfContainedKuznetsovDLSAtomReduced",
            "closed": True,
            "proved": False,
            "meaning": "自足 Kuznetsov/DLS 原子已沿 KZ-A--KZ-E 压到 acyclic NC-BLK/源反原子。",
            "remaining": after,
        },
        {
            "gate": "StrictTerminalFamilyProved",
            "closed": True,
            "proved": False,
            "meaning": "strict 终端家族仍未闭合；活动非 canonical 线卡在 acyclic NC-BLK/源反原子。",
            "remaining": terminal_gap_after,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_kuznetsov_dls_atom_router",
        "status": "self_contained_kuznetsov_dls_atom_reduced_to_acyclic_ncblk_source_antiatom_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "kz_a_smoothing_closed": True,
        "kz_b_trace_specialization_closed": True,
        "kz_c_bessel_decay_closed": True,
        "kz_d_spectral_large_sieve_closed": True,
        "kz_e_reduced_to_ncblk_or_external": True,
        "canonical_ncblk_import_blocked_for_acyclic": True,
        "generic_antiatom_nogo_imported": True,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "acyclic_ncblk_actual_block_nonconcentration_proved": False,
        "acyclic_strengthened_source_antiatom_proved": False,
        "direct_acyclic_clean_kls_dls_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": before,
        "strict_gap_after_router": after,
        "conditional_gap_after_router": conditional_after,
        "terminal_gap_after_router": terminal_gap_after,
        "strict_self_contained_math_basis_after_router": strict_basis_with_external_mertens,
        "next_attack_contract": {
            "name": "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom",
            "must_prove": [
                "对 acyclic clean residual 的实际系数证明同 moving-block 的最大块质量满足任意 log-power 反原子界",
                "证明该反原子来自假设早期零行链的实际 pre-Cauchy source，而不是形式 WFD 模板",
                "排除 moving-delta 单块集中模型，或说明它必回流 PDEC/SAE/ColumnCRT",
                "若使用外部 FullS-KLS-ext，必须保留条件线并证明无投影兼容",
            ],
            "cannot_use_as_proof": [
                "重复 KZ-A--KZ-D 谱理论闭合",
                "把 canonical-source NC-BLK 吸收导入 acyclic/noncanonical 分支",
                "声称形式 well-factorable/Type/Fourier 模板自动给反原子",
                "把外部 FullS-KLS-ext 写成严格自足证明",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步继续攻 `SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`。"
            "KZ-A 平滑、KZ-B trace formula、KZ-C Bessel 衰减、KZ-D spectral large sieve 已有内部脊柱；"
            "真正阻断是 KZ-E 的 well-factorable dispersion log-saving。既有 SC-9 前沿和 NC-BLK 核查显示，"
            "该阻断等价于证明 acyclic actual block nonconcentration/source anti-atom，或走外部 FullS-KLS-ext 条件线。"
            "因此当前最窄自足剩余更新为 `AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom`。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic Kuznetsov/DLS 原子路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"empirical_absence_not_used={str(result['empirical_absence_not_used']).lower()}",
        f"kz_a_smoothing_closed={str(result['kz_a_smoothing_closed']).lower()}",
        f"kz_b_trace_specialization_closed={str(result['kz_b_trace_specialization_closed']).lower()}",
        f"kz_c_bessel_decay_closed={str(result['kz_c_bessel_decay_closed']).lower()}",
        f"kz_d_spectral_large_sieve_closed={str(result['kz_d_spectral_large_sieve_closed']).lower()}",
        f"kz_e_reduced_to_ncblk_or_external={str(result['kz_e_reduced_to_ncblk_or_external']).lower()}",
        f"self_contained_kuznetsov_dls_large_sieve_inequality_proved={str(result['self_contained_kuznetsov_dls_large_sieve_inequality_proved']).lower()}",
        f"acyclic_ncblk_actual_block_nonconcentration_proved={str(result['acyclic_ncblk_actual_block_nonconcentration_proved']).lower()}",
        f"acyclic_strengthened_source_antiatom_proved={str(result['acyclic_strengthened_source_antiatom_proved']).lower()}",
        f"strict_terminal_family_proved={str(result['strict_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. KZ 展开",
        "",
        "```text",
        "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks",
        "  -> KZ-A smoothing/L2 bookkeeping closed",
        "  -> KZ-B Kuznetsov trace specialization closed",
        "  -> KZ-C Bessel transform decay closed",
        "  -> KZ-D spectral large sieve/pretrace chain closed",
        "  -> KZ-E well-factorable dispersion log-saving",
        "  -> AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom",
        "```",
        "",
        "条件外部线：",
        "",
        "```text",
        result["conditional_gap_after_router"],
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
