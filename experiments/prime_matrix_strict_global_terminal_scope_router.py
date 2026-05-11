#!/usr/bin/env python3
"""生成严格全局终端门作用域校准路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_global_terminal_scope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-global-terminal-scope-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-global-terminal-scope-router.json"
OUT_MD = DOCS / "prime-matrix-strict-global-terminal-scope-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-moving-atom-to-global-terminal-router.md",
    "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.md",
    "prime-matrix-self-contained-terminal-bottleneck-router.md",
    "prime-matrix-self-contained-pdec-cap-boundary-lift-router.md",
    "prime-matrix-canonical-terminal-promotion-closure-router.md",
    "prime-matrix-explicit-model-gap-finite-ledger-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    rows = [
        {
            "gate": "StrictGlobalTerminalInputActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层严格基含 GlobalPDECorSparseTerminalExclusion 与 ExplicitModelGapAndFiniteDPRCLedger。",
            "remaining": "继续拆全局终端门，并拆模型/DPRC 账本。",
        },
        {
            "gate": "GlobalTerminalSplitImported",
            "closed": True,
            "proved": True,
            "meaning": "GlobalPDECorSparseTerminalExclusion 已由既有拆分压成 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve。",
            "remaining": "PDEC-CAP 或内部 CleanKLS 大筛吸收。",
        },
        {
            "gate": "MaterializedFrontierExhaustedImported",
            "closed": True,
            "proved": True,
            "meaning": "当前已物化 PDEC 与 sparse/LocalSurvivor 前沿清零；不能继续靠局部样本消元。",
            "remaining": "必须处理全局家族证书，而非现成样本。",
        },
        {
            "gate": "CanonicalTerminalPromotionScopeChecked",
            "closed": True,
            "proved": True,
            "meaning": "NoFurtherCanonicalSourceTerminalPromotionGap 只在 canonical-source 形式系统内闭合。",
            "remaining": "不能直接关闭 acyclic noncanonical/global 终端家族。",
        },
        {
            "gate": "CanonicalImportBlockedForStrictNoncanonicalSeed",
            "closed": True,
            "proved": True,
            "meaning": "当前严格链仍含 AcyclicPreCauchyNoncanonicalPrimitiveSourceSeed；没有证明该 seed 的终端证书全都 canonical-lock。",
            "remaining": "若要使用 canonical 闭合，必须新增 terminal canonical-lock theorem。",
        },
        {
            "gate": "CleanKLSBottleneckScopeChecked",
            "closed": True,
            "proved": True,
            "meaning": "Internal CleanKLS 在 canonical-source 边界内已非独立瓶颈；但 unrestricted/generic 自足 KLS 已被隔离而非证明。",
            "remaining": "strict noncanonical 仍需 PDEC_CAP_OR_INTERNAL_CleanKLS 的同对象证明或回流。",
        },
        {
            "gate": "ExplicitModelGapFiniteSplitImported",
            "closed": True,
            "proved": True,
            "meaning": "ExplicitModelGapAndFiniteDPRCLedger 已拆分：P<2003 有限段闭合，高段解析模型余量仍开放。",
            "remaining": "HighSegmentModelGapAlpha043C3AnalyticLedger。",
        },
        {
            "gate": "StrictGlobalTerminalScopeReduced",
            "closed": True,
            "proved": True,
            "meaning": "严格全局终端门不能用 canonical 闭合偷渡；它被校准为 acyclic-seed 口径下的 PDEC_CAP/CleanKLS 终端证明。",
            "remaining": "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily。",
        },
        {
            "gate": "AcyclicSeedCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料仍未提交无环 pre-Cauchy actual noncanonical primitive source seed。",
            "remaining": "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn。",
        },
        {
            "gate": "StrictTerminalFamilyCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料没有证明 acyclic noncanonical terminal family 的 PDEC-CAP/CleanKLS 全局排斥。",
            "remaining": "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily。",
        },
        {
            "gate": "HighSegmentModelGapCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "P>=2003 的 S_Y(P)(1-H_Y(P))>3sqrt(S_Y(P)) 仍只有审计账本，缺解析证明。",
            "remaining": "HighSegmentModelGapAlpha043C3AnalyticLedger。",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_global_terminal_scope_router",
        "status": "strict_global_terminal_reduced_to_acyclic_terminal_family_and_high_model_gap_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_global_terminal_scope_boundary_closed": True,
        "global_terminal_split_imported": True,
        "canonical_terminal_promotion_not_importable_for_strict_noncanonical": True,
        "finite_dprc_segment_closed": True,
        "acyclic_pre_cauchy_seed_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "GlobalPDECorSparseTerminalExclusion AND "
            "ExplicitModelGapAndFiniteDPRCLedger"
        ),
        "terminal_gap_after_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND "
            "HighSegmentModelGapAlpha043C3AnalyticLedger"
        ),
        "strict_self_contained_math_basis_after_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND "
            "HighSegmentModelGapAlpha043C3AnalyticLedger AND "
            "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
        ),
        "next_attack_contract": {
            "name": "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
            "must_prove": [
                "对 acyclic noncanonical source 产生的全部 PDEC family 证明同一坏窗集合上的 U_CRT<L_PDEC 全局对偶证书",
                "或证明其 diffuse residual 满足内部 CleanKLS/DLS 大筛吸收并把失败回流 PDEC/SAE/ColumnCRT",
                "若要引用 canonical 终端闭合，必须证明终端证书 canonical-lock 到 RIW/Buchstab source branch",
                "同时闭合 HighSegmentModelGapAlpha043C3AnalyticLedger 的高段解析不等式",
                "继续保留自足 DStructure/Rankin 替代包",
            ],
            "cannot_use_as_proof": [
                "把 NoFurtherCanonicalSourceTerminalPromotionGap 直接导入 noncanonical acyclic seed",
                "把当前物化前沿清零当作全局家族排斥",
                "把 unrestricted/generic KLS 自足版当作已证",
                "把 P<2003 有限 DPRC 闭合当作高段模型余量证明",
                "把外部 DI/BFI/KLS 作为严格自足闭合",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "严格全局终端门继续压缩，但必须守住作用域：GlobalPDECorSparseTerminalExclusion 可接入既有拆分，"
            "变成 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve；ExplicitModelGapAndFiniteDPRCLedger 可拆成已闭合的 "
            "P<2003 有限段与仍开放的 HighSegmentModelGapAlpha043C3AnalyticLedger。可是 canonical 终端晋级闭合"
            "只限 canonical-source 形式系统，不能直接导入当前 acyclic noncanonical seed。故严格自足剩余更新为："
            "无环 source seed、acyclic noncanonical 终端家族的 PDEC-CAP/CleanKLS 证明、高段模型余量，以及自足 "
            "DStructure/Rankin 替代包。当前仍没有无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix 严格全局终端门作用域校准路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_global_terminal_scope_boundary_closed={str(result['strict_global_terminal_scope_boundary_closed']).lower()}",
        f"canonical_terminal_promotion_not_importable_for_strict_noncanonical={str(result['canonical_terminal_promotion_not_importable_for_strict_noncanonical']).lower()}",
        f"finite_dprc_segment_closed={str(result['finite_dprc_segment_closed']).lower()}",
        f"acyclic_pre_cauchy_seed_proved={str(result['acyclic_pre_cauchy_seed_proved']).lower()}",
        f"strict_acyclic_terminal_family_proved={str(result['strict_acyclic_terminal_family_proved']).lower()}",
        f"high_segment_model_gap_alpha043_c3_analytic_ledger_proved={str(result['high_segment_model_gap_alpha043_c3_analytic_ledger_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 作用域校准链",
        "",
        "```text",
        "GlobalPDECorSparseTerminalExclusion",
        "  -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
        "  -> canonical promotion closes only canonical-source branch",
        "  -> strict acyclic noncanonical branch still needs its own terminal-family proof",
        "",
        "ExplicitModelGapAndFiniteDPRCLedger",
        "  -> FiniteDPRCAlpha043PBelow2003Certificate(closed)",
        "  -> HighSegmentModelGapAlpha043C3AnalyticLedger(open)",
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
            "## 3. 下一主攻合同",
            "",
            f"下一数学主攻点：`{contract['name']}`。",
            "",
            "必须证明：",
        ]
    )
    for item in contract["must_prove"]:
        lines.append(f"- {item}。")

    lines.extend(["", "不能作为证明使用："])
    for item in contract["cannot_use_as_proof"]:
        lines.append(f"- {item}。")

    lines.extend(
        [
            "",
            "严格自足数学基更新为：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
