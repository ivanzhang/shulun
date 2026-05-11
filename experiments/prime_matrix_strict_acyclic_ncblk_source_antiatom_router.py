#!/usr/bin/env python3
"""生成 strict acyclic NC-BLK/source anti-atom 去重路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_ncblk_source_antiatom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.md",
    "prime-matrix-strict-actual-source-support-seed-router.md",
    "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.md",
    "prime-matrix-strict-moving-atom-to-global-terminal-router.md",
    "prime-matrix-strict-global-terminal-scope-router.md",
    "prime-matrix-strict-high-tail-corpus-reconciliation-router.md",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.md",
    "prime-matrix-independent-precauchy-identity-taxonomy-router.md",
    "prime-matrix-counterexample-moving-block-terminal-router.md",
    "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.md",
    "prime-matrix-clean-core-moving-atom-sharp-input-router.md",
]


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    ncblk_atom = "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"
    moving_atom = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
    global_terminal = (
        "GlobalPDECorSparseTerminalExclusion AND "
        "ExplicitModelGapAndFiniteDPRCLedger"
    )
    strict_terminal = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"{strict_terminal} AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"{strict_terminal} AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "AcyclicNCBLKSourceAntiAtomInputActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层 strict acyclic Kuznetsov/DLS 原子已压到实际块非集中或强化源反原子。",
            "remaining": ncblk_atom,
        },
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本步只在假设早期零行反例链内做对象替换和回流；不使用真实零行缺席。",
            "remaining": "所有失败态必须进入命名终端或保留为开放输入。",
        },
        {
            "gate": "GenericWFDNoGoImported",
            "closed": True,
            "proved": True,
            "meaning": "generic full-S/WFD 形式反原子已被 moving-delta 模型阻断，不能作为 strict 自足证明。",
            "remaining": "必须使用 actual acyclic source 结构，或转条件外部谱线。",
        },
        {
            "gate": "ExactPairLargeAtomEquivalenceImported",
            "closed": True,
            "proved": True,
            "meaning": "actual NC-BLK/反原子失败等价于同一 formal unit 中出现 sign-refined exact (u,v) 大原子。",
            "remaining": "该大原子就是 clean-core moving atom。",
        },
        {
            "gate": "MovingAtomNormalFormImported",
            "closed": True,
            "proved": True,
            "meaning": "registered capacity multiplier discipline 与 failure-packet 字母表把大原子标准化为 clean-core moving atom。",
            "remaining": moving_atom,
        },
        {
            "gate": "MovingAtomReturnImported",
            "closed": True,
            "proved": True,
            "meaning": "strict moving-atom 路由已把 clean-core moving atom 接回全局 PDEC/sparse 终端与模型/DPRC 账本。",
            "remaining": global_terminal,
        },
        {
            "gate": "SeedNoGoScopeImported",
            "closed": True,
            "proved": True,
            "meaning": "早期零行假设只给 unsigned 覆盖数据，不能反向生成 pre-Cauchy signed source seed。",
            "remaining": "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn 仍是独立输入。",
        },
        {
            "gate": "IndependentIdentityTaxonomyImported",
            "closed": True,
            "proved": True,
            "meaning": "独立 pre-Cauchy 来源恒等式的合法来源类已穷尽；非 canonical 自足路线最终汇合到 moving-block/NC-BLK。",
            "remaining": "不能把来源恒等式当作隐藏第四出口。",
        },
        {
            "gate": "AcyclicNCBLKNotSeparateTerminal",
            "closed": True,
            "proved": True,
            "meaning": "在当前 strict 语料中，NC-BLK/source anti-atom 失败不是新终端；它去重为 moving atom，再接回全局终端门。",
            "remaining": global_terminal,
        },
        {
            "gate": "AcyclicNCBLKActualBlockNonconcentrationCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "本步没有证明 NC-BLK 块非集中；只是证明其失败对象已有命名回流位置。",
            "remaining": global_terminal,
        },
        {
            "gate": "StrictGlobalTerminalScopeImported",
            "closed": True,
            "proved": True,
            "meaning": "全局终端门在 strict noncanonical 口径下继续校准为 acyclic PDEC-CAP/CleanKLS 家族。",
            "remaining": strict_terminal,
        },
        {
            "gate": "HighTailCorpusImported",
            "closed": True,
            "proved": False,
            "meaning": "若不接受外部 Mertens/theta 定理，高段尾项仍需自足 PNT/Mertens 内联证明。",
            "remaining": high_tail,
        },
        {
            "gate": "StrictTerminalFamilyCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "strict acyclic 终端家族仍未证明；canonical-source 闭合不能直接导入 noncanonical seed。",
            "remaining": strict_terminal,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "NC-BLK 去重后仍缺 acyclic source seed、strict 终端家族、高段自足尾项或外部输入、DStructure/Rankin 替代包。",
            "remaining": strict_basis,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_ncblk_source_antiatom_router",
        "status": "strict_acyclic_ncblk_source_antiatom_deduplicated_to_global_terminal_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "generic_wfd_antiatom_no_go_imported": True,
        "exact_pair_large_atom_equivalence_imported": True,
        "moving_atom_return_imported": True,
        "acyclic_ncblk_not_separate_terminal": True,
        "acyclic_ncblk_actual_block_nonconcentration_proved": False,
        "acyclic_strengthened_source_antiatom_proved": False,
        "acyclic_pre_cauchy_seed_proved": False,
        "global_pdec_sparse_terminal_exclusion_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": ncblk_atom,
        "terminal_gap_after_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            f"{global_terminal}"
        ),
        "strict_terminal_gap_after_scope_import": strict_terminal,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis,
        "next_attack_contract": {
            "name": "AcyclicPreCauchySeed_AND_AcyclicTerminalFamily",
            "must_prove": [
                "提交不依赖 downstream 覆盖图的 acyclic pre-Cauchy actual noncanonical source seed",
                "证明 acyclic noncanonical 终端家族的 PDEC-CAP/CleanKLS 全局排斥，或把失败全部命名回流",
                "若坚持严格自足，还要内联 Mertens/theta 高段尾项证明",
                "提交 SelfContainedDStructureTailLog4FiniteRankinReplacementPackage 或明确接受独立验收门",
                "全过程保持假设链条与真实链条分离",
            ],
            "cannot_use_as_proof": [
                "把 generic WFD/formal Type/Fourier 反原子当作已证",
                "把 NC-BLK 名称反复作为新黑箱引用",
                "把 canonical-source 终端闭合直接导入 acyclic noncanonical seed",
                "从早期零行 unsigned 覆盖图反推出 signed pre-Cauchy source",
                "把外部 DI/BFI/FullS-KLS 或 Mertens 定理冒充为 strict 自足证明",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "`AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom` 被继续硬攻后，"
            "不能作为已经证明的反原子使用；但它也不再是独立无名终端。generic WFD 版反原子已被 "
            "moving-delta 阻断；actual acyclic 版若失败，就等价于同一 formal unit 的 exact (u,v) "
            "大原子，即 clean-core moving atom。既有 moving-atom 路由把该对象接回全局 PDEC/sparse "
            "终端和模型/DPRC 账本。因此当前 strict 自足链的真正剩余是 acyclic pre-Cauchy source seed、"
            "acyclic noncanonical 终端家族、高段 Mertens/PNT 自足尾项和 DStructure/Rankin 替代包。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic NC-BLK/source anti-atom 去重路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"empirical_absence_not_used={str(result['empirical_absence_not_used']).lower()}",
        f"acyclic_ncblk_not_separate_terminal={str(result['acyclic_ncblk_not_separate_terminal']).lower()}",
        f"acyclic_ncblk_actual_block_nonconcentration_proved={str(result['acyclic_ncblk_actual_block_nonconcentration_proved']).lower()}",
        f"acyclic_strengthened_source_antiatom_proved={str(result['acyclic_strengthened_source_antiatom_proved']).lower()}",
        f"acyclic_pre_cauchy_seed_proved={str(result['acyclic_pre_cauchy_seed_proved']).lower()}",
        f"strict_acyclic_terminal_family_proved={str(result['strict_acyclic_terminal_family_proved']).lower()}",
        f"self_contained_mertens_tail_proved={str(result['self_contained_mertens_tail_proved']).lower()}",
        f"self_contained_dstructure_rankin_replacement_proved={str(result['self_contained_dstructure_rankin_replacement_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 去重链",
        "",
        "```text",
        "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom fails",
        "  -> generic WFD anti-atom route blocked by moving-delta no-go",
        "  -> actual acyclic route produces sign-refined exact (u,v) large atom",
        "  -> ActualNoncanonicalCleanCoreMovingAtomExclusion",
        "  -> GlobalPDECorSparseTerminalExclusion",
        "  -> ExplicitModelGapAndFiniteDPRCLedger",
        "  -> strict scope: PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        "```",
        "",
        "这说明 NC-BLK/source anti-atom 不是已经闭合的定理，也不是新的第四终端；它被去重到已有全局终端门。",
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
            "若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：",
            "",
            "```text",
            result["with_external_mertens_high_tail_removed_basis"],
            "```",
            "",
            "## 4. 下一主攻合同",
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
