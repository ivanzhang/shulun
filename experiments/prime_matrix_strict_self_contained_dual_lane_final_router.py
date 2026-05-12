#!/usr/bin/env python3
"""生成 Prime Matrix 严格自足二线终局路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_self_contained_dual_lane_final_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-self-contained-dual-lane-final-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-self-contained-dual-lane-final-router.json"
OUT_MD = DOCS / "prime-matrix-strict-self-contained-dual-lane-final-router.md"


SOURCE_FILES = [
    "prime-matrix-active-final-inputs-router.md",
    "prime-matrix-self-contained-narrowest-core-router.md",
    "prime-matrix-noncanonical-source-core-atomization-router.md",
    "prime-matrix-registered-capacity-multiplier-discipline-router.md",
    "prime-matrix-exact-uv-support-terminal-attack-router.md",
    "prime-matrix-final-promotion-gate-irreducibility-router.md",
    "prime-matrix-author-side-closure-task-completion-router.md",
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
            "gate": "ActiveFinalTwoLaneImported",
            "boundary_closed": True,
            "proved_or_accepted": False,
            "meaning": "当前最终数学输入是 noncanonical 二线：实际源反原子或 c-dependent 完成型谱抵消。",
            "remaining": "判定严格自足口径下哪条线仍合法。",
        },
        {
            "gate": "ExternalSpectralLaneNotStrictSelfContained",
            "boundary_closed": True,
            "proved_or_accepted": True,
            "meaning": "CDependentResidueWeightSpectralCancellationInput / FullS-KLS-ext 可以作为外部或条件数学线，但不是严格自足证明。",
            "remaining": "若坚持自足，不能用该线关闭命题。",
        },
        {
            "gate": "ActualSourceCoreReducedToExactUVSupport",
            "boundary_closed": True,
            "proved_or_accepted": True,
            "meaning": "balanced range 与 registered capacity multiplier discipline 已吸收；实际源反原子剩余压成 ActualNoncanonicalExactUVSupportLowerBound。",
            "remaining": "证明 actual noncanonical exact u/v 支撑下界。",
        },
        {
            "gate": "ShortcutNoGoRetained",
            "boundary_closed": True,
            "proved_or_accepted": True,
            "meaning": "formal WFD、K4/K6、朴素 incidence、raw Buchstab 计数和 canonical 支撑偷渡均不能推出该 exact 支撑。",
            "remaining": "只能给 actual-source 支撑定理，或给直接 final anti-atom 定理。",
        },
        {
            "gate": "ExactUVSupportCurrentCorpusProved",
            "boundary_closed": True,
            "proved_or_accepted": False,
            "meaning": "当前材料尚未证明 ActualNoncanonicalExactUVSupportLowerBound。",
            "remaining": "CleanCoreTerminalSupportIncidenceTheorem 或等价 exact support theorem。",
        },
        {
            "gate": "IndependentPromotionNotStrictSelfContained",
            "boundary_closed": True,
            "proved_or_accepted": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 当前是独立验收门；若要求严格自足，必须用新的自足替代证明包替换该门。",
            "remaining": "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage。",
        },
        {
            "gate": "StrictSelfContainedClosureCurrentCorpusProved",
            "boundary_closed": True,
            "proved_or_accepted": False,
            "meaning": "严格自足闭合不能由当前语料库推出。",
            "remaining": "ExactUV 支撑下界 + 自足 DStructure/Rankin 替代证明包。",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_self_contained_dual_lane_final_router",
        "status": "strict_self_contained_dual_lane_reduced_to_exact_uv_and_self_contained_promotion_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "strict_self_contained_boundary_closed": True,
        "external_lane_excluded_for_strict_self_contained": True,
        "registered_capacity_multiplier_discipline_closed": True,
        "actual_exact_uv_support_proved": False,
        "self_contained_promotion_replacement_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "math_two_lane_before_strict_filter": (
            "ActualNoncanonicalExactUVSupportLowerBound OR "
            "CDependentResidueWeightSpectralCancellationInput"
        ),
        "strict_self_contained_math_lane_after_filter": "ActualNoncanonicalExactUVSupportLowerBound",
        "strict_self_contained_completion_basis": (
            "ActualNoncanonicalExactUVSupportLowerBound AND "
            "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
        ),
        "conditional_external_completion_basis": (
            "AcceptFullSKLSExtExternalContract AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "next_math_attack": "CleanCoreTerminalSupportIncidenceTheorem_FOR_ActualNoncanonicalExactUVSupportLowerBound",
        "next_promotion_attack": "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage",
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "严格自足口径下，最终二选一不再是可任选的 OR：外部谱抵消/FullS-KLS 只能给条件外部线。"
            "自足数学线必须证明 ActualNoncanonicalExactUVSupportLowerBound；同时最终独立晋级门若不接受，"
            "还必须由 SelfContainedDStructureTailLog4FiniteRankinReplacementPackage 替换。"
            "当前材料没有证明这两个输入，因此不能声明行/列命题严格自足闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix 严格自足二线终局路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_self_contained_boundary_closed={str(result['strict_self_contained_boundary_closed']).lower()}",
        f"external_lane_excluded_for_strict_self_contained={str(result['external_lane_excluded_for_strict_self_contained']).lower()}",
        f"registered_capacity_multiplier_discipline_closed={str(result['registered_capacity_multiplier_discipline_closed']).lower()}",
        f"actual_exact_uv_support_proved={str(result['actual_exact_uv_support_proved']).lower()}",
        f"self_contained_promotion_replacement_proved={str(result['self_contained_promotion_replacement_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. 严格自足过滤律",
        "",
        "普通条件版的数学二线为：",
        "",
        "```text",
        result["math_two_lane_before_strict_filter"],
        "```",
        "",
        "严格自足版不能使用外部谱抵消或 FullS-KLS 黑箱，因此过滤后只剩：",
        "",
        "```text",
        result["strict_self_contained_math_lane_after_filter"],
        "```",
        "",
        "再加上最终晋级门的自足替代义务，严格自足闭合基为：",
        "",
        "```text",
        result["strict_self_contained_completion_basis"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | boundary closed | proved/accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]

    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{boundary}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                boundary=str(row["boundary_closed"]).lower(),
                proved=str(row["proved_or_accepted"]).lower(),
                meaning=row["meaning"],
                remaining=row["remaining"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"数学主攻点：`{result['next_math_attack']}`。",
            f"自足晋级替代点：`{result['next_promotion_attack']}`。",
            "",
            "条件外部版仍可写成：",
            "",
            "```text",
            result["conditional_external_completion_basis"],
            "```",
            "",
            "但这不是严格自足闭合。当前不能把条件外部闭合或作者侧证据包封装改写为无条件自足证明。",
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
