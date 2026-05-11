#!/usr/bin/env python3
"""生成 strict acyclic windowed Kloosterman/DLS 内部估计路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_windowed_dls_estimate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-windowed-dls-estimate-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-windowed-dls-estimate-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-clean-kls-router.md",
    "prime-matrix-triad-a1-clean-kls-external-input-router.md",
    "prime-matrix-triad-a1-dibfi-common-variable-table-router.md",
    "prime-matrix-triad-a1-dibfi-di-formula-ledger-router.md",
    "prime-matrix-triad-a1-dibfi-window-match-router.md",
    "prime-matrix-triad-a1-dibfi-external-full-s-match-router.md",
    "prime-matrix-clean-core-external-lemma-parameter-match-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    before = "AcyclicWindowedKloostermanDLSInternalEstimate"
    after = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
    conditional_after = (
        "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks "
        "OR (ExactExternalKLSSpecialization AND UncenteredNoProjectionCompatibilityForAcyclicCleanBlock)"
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
            "gate": "WindowedDLSInternalEstimateActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 strict acyclic clean KLS/DLS 压成窗口化 Kloosterman/DLS 内部估计。",
            "remaining": before,
        },
        {
            "gate": "CleanResidualObjectFixed",
            "closed": True,
            "proved": True,
            "meaning": "同一 formal unit 中的 PDEC/SAE/ColumnCRT/new-layer 低维缺陷已剥离，只剩 L2-flat clean residual。",
            "remaining": "无；对象已固定。",
        },
        {
            "gate": "BilinearNormalFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "clean residual 可写入窗口化 Kloosterman/dispersion 双线性型，变量为 m, ell, d, R, h 与平滑 W。",
            "remaining": "大筛不等式本身。",
        },
        {
            "gate": "PhaseAndInvertibleVariableLedgerClosed",
            "closed": True,
            "proved": True,
            "meaning": "CRT 相位、可逆变量、gcd/unit 层和非零 Fourier 频率已经由 A1 clean KLS 模板登记。",
            "remaining": "内部谱估计。",
        },
        {
            "gate": "CoefficientNormLedgerClosed",
            "closed": True,
            "proved": True,
            "meaning": "L2-flat 系数、dyadic 分块、平滑导数损失和 polylog 预算均在 clean admission/模板账本内登记。",
            "remaining": "证明这些范数输入下的 KLS/DLS log-saving。",
        },
        {
            "gate": "FailureReturnAlphabetClosed",
            "closed": True,
            "proved": True,
            "meaning": "若失败来自 point-load、short-window、low-phase、new-layer 或列/壳集中，已经命名回流。",
            "remaining": "纯谱大筛不等式无法再靠命名回流删除。",
        },
        {
            "gate": "ExternalLineSeparated",
            "closed": True,
            "proved": True,
            "meaning": "外部 DI/BFI/Kuznetsov 线需要精确专门化和无投影兼容；它可给条件闭合，不给严格自足闭合。",
            "remaining": "ExactExternalKLSSpecialization AND UncenteredNoProjectionCompatibilityForAcyclicCleanBlock。",
        },
        {
            "gate": "InternalKuznetsovDLSInequalityAtomPinned",
            "closed": True,
            "proved": False,
            "meaning": "真正自足剩余是证明 acyclic clean blocks 的窗口化 Kuznetsov/DLS 大筛不等式。",
            "remaining": after,
        },
        {
            "gate": "AcyclicWindowedDLSInternalEstimateProved",
            "closed": True,
            "proved": False,
            "meaning": "当前语料没有提交该自足谱大筛证明。",
            "remaining": after,
        },
        {
            "gate": "StrictTerminalFamilyProved",
            "closed": True,
            "proved": False,
            "meaning": "strict 终端家族仍未闭合；活动非 canonical 线卡在自足 Kuznetsov/DLS 不等式。",
            "remaining": terminal_gap_after,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_windowed_dls_estimate_router",
        "status": "acyclic_windowed_dls_reduced_to_self_contained_kuznetsov_large_sieve_atom_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "clean_residual_object_fixed": True,
        "acyclic_windowed_bilinear_normal_form_closed": True,
        "phase_invertible_variable_ledger_closed": True,
        "coefficient_norm_ledger_closed": True,
        "failure_return_alphabet_closed": True,
        "external_line_separated": True,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "acyclic_windowed_kloosterman_dls_internal_estimate_proved": False,
        "direct_acyclic_clean_kls_dls_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": before,
        "strict_gap_after_router": after,
        "conditional_gap_after_router": conditional_after,
        "terminal_gap_after_router": terminal_gap_after,
        "strict_self_contained_math_basis_after_router": strict_basis_with_external_mertens,
        "next_attack_contract": {
            "name": "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks",
            "must_prove": [
                "对所有 acyclic clean dyadic blocks 给出统一窗口化 Kloosterman/DLS 双线性型上界",
                "上界必须只依赖 L2 范数、模数窗口、频率窗口、平滑导数损失和 polylog 预算",
                "所得节省必须足以吸收 strict 终端门中剩余 clean residual 质量",
                "若试图使用外部 DI/BFI/Kuznetsov，必须另证精确专门化和无投影兼容，并标记为条件线",
            ],
            "cannot_use_as_proof": [
                "重复 K1--K9 clean admission 或 L2-flat 账本",
                "只给 DI/BFI 变量表而不证明 J-scale/谱大筛上界",
                "把外部定理当成严格自足证明",
                "把有限数值审计或低维回流字母表当成纯谱不等式",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步继续攻 `AcyclicWindowedKloostermanDLSInternalEstimate`。形式层已压尽："
            "acyclic clean residual 的对象、窗口化双线性型、相位/可逆变量、L2 系数范数和失败回流字母表均可由现有账本关闭。"
            "剩下的不是变量命名或 clean 准入，而是一个真正解析原子："
            "`SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`。"
            "外部 DI/BFI/Kuznetsov 只能作为条件线，仍需精确专门化与无投影兼容。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic windowed DLS 估计路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"empirical_absence_not_used={str(result['empirical_absence_not_used']).lower()}",
        f"acyclic_windowed_bilinear_normal_form_closed={str(result['acyclic_windowed_bilinear_normal_form_closed']).lower()}",
        f"phase_invertible_variable_ledger_closed={str(result['phase_invertible_variable_ledger_closed']).lower()}",
        f"coefficient_norm_ledger_closed={str(result['coefficient_norm_ledger_closed']).lower()}",
        f"failure_return_alphabet_closed={str(result['failure_return_alphabet_closed']).lower()}",
        f"self_contained_kuznetsov_dls_large_sieve_inequality_proved={str(result['self_contained_kuznetsov_dls_large_sieve_inequality_proved']).lower()}",
        f"acyclic_windowed_kloosterman_dls_internal_estimate_proved={str(result['acyclic_windowed_kloosterman_dls_internal_estimate_proved']).lower()}",
        f"direct_acyclic_clean_kls_dls_proved={str(result['direct_acyclic_clean_kls_dls_proved']).lower()}",
        f"strict_terminal_family_proved={str(result['strict_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "严格自足线：",
        "",
        "```text",
        f"{result['terminal_gap_before_router']}",
        "  -> clean residual object fixed",
        "  -> windowed bilinear normal form",
        "  -> phase/invertible-variable ledger",
        "  -> coefficient norm ledger",
        f"  -> {result['strict_gap_after_router']}",
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
