#!/usr/bin/env python3
"""生成严格高段尾项语料校准路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_high_tail_corpus_reconciliation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-high-tail-corpus-reconciliation-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-high-tail-corpus-reconciliation-router.json"
OUT_MD = DOCS / "prime-matrix-strict-high-tail-corpus-reconciliation-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-high-model-tail-update-router.md",
    "prime-matrix-beta-sieve-self-contained-frontier-router.md",
    "prime-matrix-beta-sieve-lower-weight-recursion-router.md",
    "prime-matrix-beta-sieve-lower-bound-dominance-router.md",
    "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.md",
    "prime-matrix-b3-continuous-beta-sieve-surplus-router.md",
    "prime-matrix-b3-prime-word-stieltjes-integral-router.md",
    "prime-matrix-b3-alternating-boundary-terminal-router.md",
    "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.md",
    "prime-matrix-b3-signed-delay-multiplier-anchor-router.md",
    "prime-matrix-b3-self-contained-mertens-tail-router.md",
    "prime-matrix-exact-residue-sawtooth-normal-form-router.md",
    "prime-matrix-quadratic-arc-nearsquare-spread-router.md",
    "prime-matrix-nearsquare-strip-defect-certificate-router.md",
    "prime-matrix-nearsquare-strip-terminal-admission-router.md",
    "prime-matrix-strict-global-terminal-scope-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    old_tail_gap = (
        "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND "
        "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 AND "
        "ExactResidueWeightedFloorSawtoothTenPercentBound"
    )
    self_contained_mertens_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND "
        f"({self_contained_mertens_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_high_tail_basis = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "StrictHighTailCorpusReconciliationActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层 strict 高段尾项仍把 beta 构造、99% 主系数和 exact sawtooth 写成三个并列开放输入。",
            "remaining": "导入已经完成的 beta/B3/sawtooth 语料，并重新校准严格作用域。",
        },
        {
            "gate": "LowerWeightConstructionAndDominanceImported",
            "closed": True,
            "proved": True,
            "meaning": "B=3 lower word rule、有限递归、支撑、符号、level 与逐点 lower-bound 支配均已由内部组合证明关闭。",
            "remaining": "不再把 SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix 作为未拆黑箱。",
        },
        {
            "gate": "ContinuousAndStieltjesLayersImported",
            "closed": True,
            "proved": True,
            "meaning": "连续 f(1/0.43) 余量与 prime-word Stieltjes 精确表示已闭合，离散误差集中到 B=3 边界余项。",
            "remaining": "B3 交错边界余项的一维 Mertens 尾段。",
        },
        {
            "gate": "BoundaryVariationAnchor20000Imported",
            "closed": True,
            "proved": True,
            "meaning": "10372 到 20000 的有限锚点提升、face 字典和 delay-kernel BV 乘子账本已闭合。",
            "remaining": "若不用外部 Dusart/Rosser-Schoenfeld，则仍需自足证明 reciprocal-prime Mertens 尾段。",
        },
        {
            "gate": "ExternalMertensHighTailRouteAvailable",
            "closed": True,
            "proved": False,
            "meaning": "接受 Dusart/Rosser-Schoenfeld 型外部显式 Mertens/theta 输入时，B3 高段解析链可接到 DStructure/Rankin 门。",
            "remaining": "这是外部条件接入，不是严格自足内联证明。",
        },
        {
            "gate": "SelfContainedMertensTailStillOpen",
            "closed": True,
            "proved": False,
            "meaning": "完全自足版必须内联显式 PNT 机器：x>=20000 的 theta/psi 包络和 Meissel-Mertens 常数区间。",
            "remaining": self_contained_mertens_tail,
        },
        {
            "gate": "ExactSawtoothNormalFormImported",
            "closed": True,
            "proved": True,
            "meaning": "Exact floor/sawtooth 已精确化为二次圆弧，再化为近平方条带 formal unit。",
            "remaining": "条带失败态是否形成可排除的全局终端家族。",
        },
        {
            "gate": "NearSquareTerminalAdmittedToStrictTerminalFamily",
            "closed": True,
            "proved": False,
            "meaning": "近平方条带失败会生成同一 formal unit 的 PDEC/SAE 证书；在 strict noncanonical 口径中只能并入已开放的 acyclic terminal-family 门，不能用 canonical 吸收偷渡。",
            "remaining": "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily。",
        },
        {
            "gate": "ExactSawtoothIndependentInputRemovedByCharging",
            "closed": True,
            "proved": False,
            "meaning": "Exact sawtooth 不再作为第三个高段独立输入保留；其失败态被收费到 strict 全局终端门。",
            "remaining": "strict 终端门本身仍未证明。",
        },
        {
            "gate": "StrictHighTailSelfContainedCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "旧三项已经重新压缩，但严格自足高段尾项还缺 Mertens/PNT 内联证明。",
            "remaining": self_contained_mertens_tail,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "即便高段外部解析线可用，完整行/列命题仍受 acyclic seed、strict PDEC/CleanKLS 与 DStructure/Rankin 替代门限制。",
            "remaining": strict_basis,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_high_tail_corpus_reconciliation_router",
        "status": "strict_high_tail_reconciled_to_mertens_tail_and_strict_terminal_family_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_high_tail_corpus_reconciliation_closed": True,
        "lower_weight_construction_and_dominance_imported": True,
        "continuous_and_stieltjes_layers_imported": True,
        "b3_boundary_variation_anchor20000_imported": True,
        "external_mertens_high_tail_route_available": True,
        "self_contained_mertens_tail_proved": False,
        "exact_sawtooth_normal_form_imported": True,
        "exact_sawtooth_independent_input_removed": True,
        "strict_terminal_family_proved": False,
        "acyclic_pre_cauchy_seed_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": old_tail_gap,
        "strict_self_contained_high_tail_gap_after_router": self_contained_mertens_tail,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "with_external_mertens_high_tail_removed_basis": external_high_tail_basis,
        "next_attack_contract": {
            "name": "SelfContainedMertensTail_OR_AcyclicTerminalFamily",
            "strict_self_contained_high_tail_priority": self_contained_mertens_tail,
            "global_strict_priority": "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
            "cannot_use_as_proof": [
                "把 canonical-source 的 NoFurtherCanonicalSourceTerminalPromotionGap 直接导入 acyclic noncanonical 分支",
                "把 Dusart/Rosser-Schoenfeld 外部 Mertens 定理冒充为仓库内自足证明",
                "把 finite checkpoint 余量外推成 P>=100000 全尾段证明",
                "把 exact sawtooth 标准形本身当作负损失界",
                "把 DStructure/Rankin 独立验收门改写为已证自足替代包",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步把 strict 高段尾项与已经完成的 beta/B3/sawtooth 语料重新对齐。"
            "lower weights 构造、逐点支配、连续主项、Stieltjes 表示和 B=3 delay 乘子账本可导入；"
            "exact sawtooth 失败态也不再是独立第三输入，而是并入 strict acyclic noncanonical 终端家族。"
            "严格自足高段剩余因此压成 Mertens/PNT 内联证明；若接受外部 Dusart/Rosser-Schoenfeld 输入，"
            "高段解析线可移出活动缺口。完整行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix 严格高段尾项语料校准路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_high_tail_corpus_reconciliation_closed={str(result['strict_high_tail_corpus_reconciliation_closed']).lower()}",
        f"lower_weight_construction_and_dominance_imported={str(result['lower_weight_construction_and_dominance_imported']).lower()}",
        f"continuous_and_stieltjes_layers_imported={str(result['continuous_and_stieltjes_layers_imported']).lower()}",
        f"b3_boundary_variation_anchor20000_imported={str(result['b3_boundary_variation_anchor20000_imported']).lower()}",
        f"self_contained_mertens_tail_proved={str(result['self_contained_mertens_tail_proved']).lower()}",
        f"exact_sawtooth_independent_input_removed={str(result['exact_sawtooth_independent_input_removed']).lower()}",
        f"strict_terminal_family_proved={str(result['strict_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"strict_self_contained_high_tail_gap_after_router={result['strict_self_contained_high_tail_gap_after_router']}",
        "```",
        "",
        "## 1. 校准前后",
        "",
        "校准前 strict 高段尾项写成：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "导入现有语料后，严格自足高段尾项剩余压成：",
        "",
        "```text",
        result["strict_self_contained_high_tail_gap_after_router"],
        "```",
        "",
        "同时 exact sawtooth 失败态收费到 strict 终端家族，而不是用 canonical 吸收偷渡。",
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
            "严格自足基更新为：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "若接受外部 Mertens/theta 显式定理，高段解析缺口可移出，剩：",
            "",
            "```text",
            result["with_external_mertens_high_tail_removed_basis"],
            "```",
            "",
            "## 4. 下一主攻合同",
            "",
            f"主攻名：`{contract['name']}`。",
            "",
            "- 高段严格自足优先：`{}`。".format(contract["strict_self_contained_high_tail_priority"]),
            "- 全局 strict 优先：`{}`。".format(contract["global_strict_priority"]),
            "",
            "不能作为证明使用：",
        ]
    )
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
