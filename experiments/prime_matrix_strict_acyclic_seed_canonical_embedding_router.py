#!/usr/bin/env python3
"""生成 strict acyclic seed -> canonical source 有限因子嵌入路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_canonical_embedding_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-canonical-embedding-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-canonical-embedding-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-canonical-embedding-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-canonical-lock-router.md",
    "prime-matrix-clean-core-source-loop-cut-router.md",
    "prime-matrix-triad-a1-source-lock-contract-router.md",
    "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.md",
    "prime-matrix-pdec-cap-transverse-embedding-router.md",
    "prime-matrix-canonical-formal-unit-hash-stability-router.md",
    "prime-matrix-strict-actual-source-support-seed-router.md",
    "prime-matrix-canonical-terminal-promotion-closure-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    gate_before = "AcyclicSeedCanonicalSourceFiniteFactorEmbedding"
    gate_after = (
        "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy "
        "AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity "
        "AND AcyclicSeedNoSourceReplacementOrPayloadCreation"
    )
    fallback = (
        "DirectAcyclicSameSetPDECCapDualCertificate "
        "OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    )
    terminal_gap_after = (
        f"(({gate_after}) "
        "AND TerminalCertificateSameSetPushforwardIdentity "
        "AND NoNoncanonicalPayloadSurvivesCanonicalProjection) "
        f"OR {fallback}"
    )
    strict_basis_with_external_mertens = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"({terminal_gap_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "AcyclicSeedEmbeddingGateActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 canonical-lock 的第一原子定为 acyclic seed 是 canonical A1/KZ-E 源的有限测度因子。",
            "remaining": gate_before,
        },
        {
            "gate": "FiniteFactorMeaningPinned",
            "closed": True,
            "proved": True,
            "meaning": "有限因子只能由 canonical 源经事件限制、确定性推前、有限投影、有限商或条件化得到。",
            "remaining": "必须提交具体因子图和权重推前恒等式。",
        },
        {
            "gate": "CanonicalSourceAvailableOnlyByPreCauchyDeclaration",
            "closed": True,
            "proved": True,
            "meaning": "canonical 来源账本只在 lambda_c 于 Cauchy/dispersion 之前被声明为 RIW/Buchstab 决策树系数时闭合。",
            "remaining": "acyclic seed 也必须在同一时间线和同一 formal unit 下满足该来源声明。",
        },
        {
            "gate": "SourceLoopCutBlocksDownstreamRecovery",
            "closed": True,
            "proved": True,
            "meaning": "不能从早期零行覆盖图、payment skeleton、terminal certificate 或有限投影反推出 primitive source。",
            "remaining": "若 seed 只在下游终端选择后出现，则不能作为 canonical pre-Cauchy 因子。",
        },
        {
            "gate": "HashStabilityNotMeasureFactor",
            "closed": True,
            "proved": True,
            "meaning": "formal unit 哈希稳定只证明记录命名稳定，不证明测度、权重和 sigma 代数可由 canonical 源推前。",
            "remaining": "仍需 pi_* mu_c = mu_a 的测度等式。",
        },
        {
            "gate": "TransverseEmbeddingScopeGuard",
            "closed": True,
            "proved": True,
            "meaning": "既有横向嵌入只覆盖由 canonical payment 图取弧预像和有限商得到的特定对象。",
            "remaining": "当前 acyclic noncanonical seed 未证明属于该横向商对象族。",
        },
        {
            "gate": "AcyclicCanonicalAdmissionPinned",
            "closed": True,
            "proved": False,
            "meaning": "必须证明假设反例链生成的 acyclic seed 在 pre-Cauchy 层就是 canonical RIW/Buchstab source branch。",
            "remaining": "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy。",
        },
        {
            "gate": "MeasurableFactorMapPinned",
            "closed": True,
            "proved": False,
            "meaning": "必须给出从 canonical 源样本空间到 acyclic seed 样本空间的有限可测因子图 pi，并证明权重质量逐纤维守恒。",
            "remaining": "AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity。",
        },
        {
            "gate": "NoSourceReplacementPinned",
            "closed": True,
            "proved": False,
            "meaning": "任何 branch-dependent 新权重、terminal-dependent payload 或 non-AP/WFD 补集不得在投影后作为 canonical 源残留。",
            "remaining": "AcyclicSeedNoSourceReplacementOrPayloadCreation。",
        },
        {
            "gate": "FactorObstructionCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "若 acyclic seed 含有不由 canonical source 字段决定的系数或 payload，则按有限因子定义不能走 canonical-lock。",
            "remaining": "该情形必须转 direct PDEC dual 或 direct CleanKLS/DLS。",
        },
        {
            "gate": "CurrentCorpusEmbeddingProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料给出 canonical 来源、横向嵌入和哈希稳定，但尚未给出 acyclic seed 的 pre-Cauchy canonical 准入与因子图。",
            "remaining": f"{gate_after} OR {fallback}",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_canonical_embedding_router",
        "status": "acyclic_seed_canonical_embedding_reduced_to_precauchy_admission_and_factor_map_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "finite_factor_definition_pinned": True,
        "canonical_source_material_imported_with_scope": True,
        "source_loop_cut_imported": True,
        "transverse_embedding_imported_with_scope": True,
        "acyclic_seed_canonical_branch_admission_proved": False,
        "acyclic_seed_finite_factor_map_weight_identity_proved": False,
        "acyclic_seed_no_source_replacement_proved": False,
        "acyclic_seed_canonical_source_embedding_proved": False,
        "terminal_certificate_same_set_pushforward_proved": False,
        "no_noncanonical_payload_survives_projection_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": gate_before,
        "seed_embedding_gap_after_router": gate_after,
        "terminal_gap_after_router": terminal_gap_after,
        "strict_self_contained_math_basis_after_router": strict_basis_with_external_mertens,
        "next_attack_contract": {
            "name": "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy_OR_DirectDualFallback",
            "must_prove_for_canonical_lock": [
                "acyclic seed 的 lambda 在 Cauchy/dispersion/terminal extraction 之前已被定义为 canonical RIW/Buchstab 决策树系数",
                "存在有限可测因子图 pi: Omega_c -> Omega_a，且 acyclic 权重等于 canonical 权重的限制、条件化或确定性推前",
                "formal_unit、branch key、bad-window set、U_CRT、L_PDEC 口径在该因子图下不改变",
                "所有 noncanonical payload 均被证明只是 canonical 字段的有限商信息，不能新增系数源",
            ],
            "fallback_if_any_clause_fails": [
                "若来源时间线依赖下游 payment/terminal 数据，则进入 DirectAcyclicSameSetPDECCapDualCertificate",
                "若 residual 已无低维 PDEC 签名但仍为 clean diffuse 对象，则进入 DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
                "若出现 unregistered payload，则先命名回流到 PDEC/SAE/ColumnCRT，再重新判定同集终端门",
            ],
            "cannot_use_as_proof": [
                "只引用 canonical-source 终端闭合",
                "只引用 formal_unit 哈希稳定",
                "只引用横向 PDEC-CAP 嵌入而不给当前 seed 的因子图",
                "从假设早期零行覆盖或 payment skeleton 反推出 pre-Cauchy source",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步没有证明 AcyclicSeedCanonicalSourceFiniteFactorEmbedding；它把该原子压成三个更硬但可审查的必要条件："
            "acyclic seed 必须在 pre-Cauchy 时间线上准入 canonical RIW/Buchstab source branch；必须给出有限可测因子图与权重推前恒等式；"
            "必须排除任何 source replacement 或新增 noncanonical payload。当前语料不足以关闭这三项，因此 canonical-lock 路线暂不能导入；"
            "若下一步不能证明这些条件，正确路线是直接攻 acyclic 同集 PDEC 对偶或 acyclic CleanKLS/DLS。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic seed canonical embedding 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"empirical_absence_not_used={str(result['empirical_absence_not_used']).lower()}",
        f"finite_factor_definition_pinned={str(result['finite_factor_definition_pinned']).lower()}",
        f"canonical_source_material_imported_with_scope={str(result['canonical_source_material_imported_with_scope']).lower()}",
        f"source_loop_cut_imported={str(result['source_loop_cut_imported']).lower()}",
        f"transverse_embedding_imported_with_scope={str(result['transverse_embedding_imported_with_scope']).lower()}",
        f"acyclic_seed_canonical_branch_admission_proved={str(result['acyclic_seed_canonical_branch_admission_proved']).lower()}",
        f"acyclic_seed_finite_factor_map_weight_identity_proved={str(result['acyclic_seed_finite_factor_map_weight_identity_proved']).lower()}",
        f"acyclic_seed_no_source_replacement_proved={str(result['acyclic_seed_no_source_replacement_proved']).lower()}",
        f"acyclic_seed_canonical_source_embedding_proved={str(result['acyclic_seed_canonical_source_embedding_proved']).lower()}",
        f"acyclic_terminal_canonical_lock_proved={str(result['acyclic_terminal_canonical_lock_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. 有限因子口径",
        "",
        "要把 acyclic seed 锁入 canonical source，必须存在同一 formal unit 下的有限可测因子图：",
        "",
        "```text",
        "(Omega_c, mu_c, lambda_c^RIW/Buchstab)",
        "  -- restriction / conditioning / deterministic pushforward / finite quotient -->",
        "(Omega_a, mu_a, lambda_a)",
        "",
        "required: mu_a = pi_* mu_c, and lambda_a is the pushed-forward canonical coefficient.",
        "```",
        "",
        "这一定义立即排除一类偷渡：若 acyclic seed 的权重依赖下游 payment 图、terminal certificate、moving payload 或 generic WFD 补集，而这些字段不是 canonical 源字段的有限商，则它不是 canonical source 的有限因子。",
        "",
        "## 2. seed 原子拆分",
        "",
        "拆分前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["seed_embedding_gap_after_router"],
        "```",
        "",
        "并回填到终端 canonical-lock 总门：",
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
            "canonical-lock 路线必须证明：",
        ]
    )
    for item in contract["must_prove_for_canonical_lock"]:
        lines.append(f"- {item}。")
    lines.append("")
    lines.append("任一条失败时的回退：")
    for item in contract["fallback_if_any_clause_fails"]:
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
