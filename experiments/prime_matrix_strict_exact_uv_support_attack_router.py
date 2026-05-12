#!/usr/bin/env python3
"""生成严格自足 ExactUV 支撑主攻点路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_exact_uv_support_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-exact-uv-support-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-exact-uv-support-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-exact-uv-support-attack-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-self-contained-dual-lane-final-router.md",
    "prime-matrix-clean-core-exact-entropy-atom-router.md",
    "prime-matrix-clean-core-support-incidence-attack-router.md",
    "prime-matrix-clean-core-layer-transfer-path-router.md",
    "prime-matrix-clean-core-path-source-firewall-router.md",
    "prime-matrix-clean-core-source-loop-cut-router.md",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.md",
    "prime-matrix-independent-precauchy-identity-taxonomy-router.md",
    "prime-matrix-counterexample-moving-block-terminal-router.md",
    "prime-matrix-early-zero-terminal-schema-reconciliation-router.md",
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
            "gate": "StrictExactUVGateActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层严格自足过滤后，数学主攻点只剩 ActualNoncanonicalExactUVSupportLowerBound。",
            "remaining": "直接攻击该支撑下界。",
        },
        {
            "gate": "SupportIncidenceReductionImported",
            "closed": True,
            "proved": True,
            "meaning": "ExactUV 支撑下界可由 CleanCoreTerminalSupportIncidenceTheorem 支付。",
            "remaining": "证明 clean-core terminal support incidence。",
        },
        {
            "gate": "ExactLayerTransferReductionImported",
            "closed": True,
            "proved": True,
            "meaning": "支撑关联已压到 clean-core exact 层承认、非零转移和 thin return。",
            "remaining": "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn。",
        },
        {
            "gate": "PathPartitionReductionImported",
            "closed": True,
            "proved": True,
            "meaning": "层承认可由 actual clean-core 系数的 polylog 路径分割、同路径非零/无抵消推出。",
            "remaining": "CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn。",
        },
        {
            "gate": "PreCauchySourceLawRequired",
            "closed": True,
            "proved": True,
            "meaning": "路径分割必须建立在 Cauchy/dispersion 前的 actual signed alpha/delta 来源恒等式上。",
            "remaining": "CleanCorePreCauchyCoefficientSourceLawAndReturn。",
        },
        {
            "gate": "SourceLoopCutAndZeroRowSeedNoGo",
            "closed": True,
            "proved": True,
            "meaning": "不能从 downstream payment skeleton、有限投影、早期零行覆盖图或几何 Phi 反向生成 pre-Cauchy 源。",
            "remaining": "IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn。",
        },
        {
            "gate": "IndependentIdentityTaxonomyClosed",
            "closed": True,
            "proved": True,
            "meaning": "canonical、generic WFD、AP/external 来源都不能作为严格自足 noncanonical clean-core 来源恒等式。",
            "remaining": "actual noncanonical moving-block spread / source theorem。",
        },
        {
            "gate": "MovingBlockReturnLoopDetected",
            "closed": True,
            "proved": True,
            "meaning": "actual moving-block 若有低维签名则回流 PDEC/SAE/ColumnCRT；若无签名则回到早期零行终端包。",
            "remaining": "这不是 ExactUV 的新证明，而是回到终端门/外部谱分支。",
        },
        {
            "gate": "NoExistingInternalProofOfExactUV",
            "closed": True,
            "proved": False,
            "meaning": "现有内部链已经压完伪出口，但没有产生 actual exact u/v 支撑下界。",
            "remaining": "NewActualNoncanonicalExactUVSupportTheoremInput。",
        },
        {
            "gate": "StrictExactUVSupportClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前语料库不能证明严格自足 ExactUV 支撑输入。",
            "remaining": "新增并证明 actual noncanonical exact-support 定理，或改变目标为条件外部线。",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_exact_uv_support_attack_router",
        "status": "strict_exact_uv_support_reduced_to_new_actual_source_support_theorem_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "strict_exact_uv_attack_boundary_closed": True,
        "support_incidence_reduction_closed": True,
        "path_partition_source_reduction_closed": True,
        "zero_row_seed_extraction_blocked": True,
        "moving_block_return_loop_detected": True,
        "actual_exact_uv_support_proved": False,
        "new_actual_source_support_theorem_required": True,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": (
            "CleanCoreTerminalSupportIncidenceTheorem_FOR_"
            "ActualNoncanonicalExactUVSupportLowerBound"
        ),
        "terminal_gap_after_router": "NewActualNoncanonicalExactUVSupportTheoremInput",
        "strict_self_contained_math_basis_after_router": (
            "NewActualNoncanonicalExactUVSupportTheoremInput AND "
            "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
        ),
        "next_attack_contract": {
            "name": "NewActualNoncanonicalExactUVSupportTheoremInput",
            "must_prove": [
                "在 Cauchy/dispersion 前给出 actual noncanonical clean-core signed source identity",
                "从该 identity 得到 polylog exact path partition",
                "证明同路径非零/无抵消或给出 sign-refined partition",
                "证明 thin/rejected/path-overbudget block 全部命名回流",
                "推出 S_u*S_v >= L^(2A+4C+E) 的 exact u/v 支撑下界",
            ],
            "cannot_use_as_proof": [
                "canonical RIW/Buchstab 来源表跨分支导入",
                "formal WFD/Type/Fourier/K4/K6 平坦性",
                "真实样本未见早期零行",
                "从 payment skeleton 或 CRT 覆盖图反推 signed source",
                "外部 FullS-KLS 黑箱",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "直接硬攻 ExactUV 后，现有内部路线已经把伪出口全部压掉：支撑关联需要 exact 层转移，"
            "exact 层转移需要 actual 路径分割，路径分割需要 pre-Cauchy signed 来源恒等式；"
            "而该来源恒等式不能由早期零行覆盖图、几何 Phi、canonical 模板或 generic WFD 反推出。"
            "因此严格自足数学主攻点被进一步定名为 NewActualNoncanonicalExactUVSupportTheoremInput。"
            "当前没有无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix 严格自足 ExactUV 支撑主攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_exact_uv_attack_boundary_closed={str(result['strict_exact_uv_attack_boundary_closed']).lower()}",
        f"support_incidence_reduction_closed={str(result['support_incidence_reduction_closed']).lower()}",
        f"path_partition_source_reduction_closed={str(result['path_partition_source_reduction_closed']).lower()}",
        f"zero_row_seed_extraction_blocked={str(result['zero_row_seed_extraction_blocked']).lower()}",
        f"actual_exact_uv_support_proved={str(result['actual_exact_uv_support_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 压缩链",
        "",
        "```text",
        "ActualNoncanonicalExactUVSupportLowerBound",
        "  -> CleanCoreTerminalSupportIncidenceTheorem",
        "  -> CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn",
        "  -> CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn",
        "  -> CleanCorePreCauchyCoefficientSourceLawAndReturn",
        "  -> IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn",
        "  -> NewActualNoncanonicalExactUVSupportTheoremInput",
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
            "## 3. 新主攻合同",
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
