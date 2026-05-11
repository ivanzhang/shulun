#!/usr/bin/env python3
"""生成 strict acyclic source seed 与终端家族门融合路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_terminal_fusion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-terminal-fusion-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-terminal-fusion-router.md"


SOURCE_FILES = [
    "prime-matrix-clean-core-source-loop-cut-router.md",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.md",
    "prime-matrix-independent-precauchy-identity-taxonomy-router.md",
    "prime-matrix-counterexample-moving-block-terminal-router.md",
    "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.md",
    "prime-matrix-strict-acyclic-terminal-family-attack-router.md",
    "prime-matrix-strict-global-terminal-scope-router.md",
    "prime-matrix-strict-high-tail-corpus-reconciliation-router.md",
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

    seed = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
    terminal_family = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis_before = (
        f"{seed} AND {terminal_family} AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    strict_basis_after = (
        f"{terminal_family} AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis_after = (
        f"{terminal_family} AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    terminal_three_atom = (
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
        "DirectAcyclicSameSetPDECCapDualCertificate OR "
        "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    )

    rows = [
        {
            "gate": "SeedAndTerminalBothActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层 strict 基同时含 acyclic pre-Cauchy seed 与 acyclic terminal family。",
            "remaining": f"{seed} AND {terminal_family}",
        },
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本步仍只在假设早期零行反例链内做分支覆盖，不使用真实零行缺席。",
            "remaining": "所有 seed 缺失或 seed 下游失败必须进入命名终端家族。",
        },
        {
            "gate": "SeedExistsBranchCovered",
            "closed": True,
            "proved": True,
            "meaning": "若反例链确有合法 acyclic pre-Cauchy seed，则 ExactUV/pair-mass/NC-BLK 路由已把失败对象接回终端家族。",
            "remaining": terminal_family,
        },
        {
            "gate": "SeedAbsentBranchReturned",
            "closed": True,
            "proved": True,
            "meaning": "若反例链不能给出 seed，来源环切断与早期零行 seed no-go 已禁止 clean-core 偷渡，强制回流 PDEC/SAE/ColumnCRT/CleanKLS。",
            "remaining": terminal_family,
        },
        {
            "gate": "IndependentIdentityNotFourthExit",
            "closed": True,
            "proved": True,
            "meaning": "独立 pre-Cauchy 来源恒等式已被分类：canonical scoped、generic rejected、external not-self-contained，actual 分支回到 moving-block/NC-BLK。",
            "remaining": terminal_family,
        },
        {
            "gate": "MovingBlockReturnImported",
            "closed": True,
            "proved": True,
            "meaning": "actual moving-block/NC-BLK 若出现大原子，已由 moving-block 与 strict NC-BLK 路由接回早期零行/全局终端门。",
            "remaining": terminal_family,
        },
        {
            "gate": "SeedNoLongerIndependentConjunct",
            "closed": True,
            "proved": True,
            "meaning": "seed 不是被证明存在，而是通过存在/不存在两支都落入同一终端家族，故可从最终并列输入基中删除。",
            "remaining": terminal_family,
        },
        {
            "gate": "AcyclicPreCauchySeedCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前仍没有构造 acyclic pre-Cauchy seed；本步不声称 seed 定理成立。",
            "remaining": "seed 已变成分支准入门，不再是独立闭合输入。",
        },
        {
            "gate": "StrictAcyclicTerminalFamilyCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "终端家族本身仍未排斥；这是 seed 融合后的真正数学主攻点。",
            "remaining": terminal_three_atom,
        },
        {
            "gate": "HighTailCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "若不接受外部 Mertens/theta 定理，高段 PNT/Mertens 自足尾项仍开放。",
            "remaining": high_tail,
        },
        {
            "gate": "DStructureRankinCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 替代包仍未自足证明。",
            "remaining": "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage。",
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "seed 融合后仍缺终端家族、高段自足尾项或外部接受、DStructure/Rankin 替代包。",
            "remaining": strict_basis_after,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_terminal_fusion_router",
        "status": "strict_acyclic_seed_independent_input_removed_terminal_family_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "seed_exists_branch_covered_by_terminal_family": True,
        "seed_absent_branch_returned_to_terminal_family": True,
        "independent_identity_not_fourth_exit": True,
        "acyclic_pre_cauchy_seed_independent_input_removed": True,
        "acyclic_pre_cauchy_seed_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": f"{seed} AND {terminal_family}",
        "terminal_gap_after_router": terminal_family,
        "strict_self_contained_math_basis_before_router": strict_basis_before,
        "strict_self_contained_math_basis_after_router": strict_basis_after,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis_after,
        "next_attack_contract": {
            "name": "AcyclicTerminalFamilyThreeAtomDirectAttack",
            "terminal_three_atom": terminal_three_atom,
            "priority_order": [
                "DirectAcyclicSameSetPDECCapDualCertificate",
                "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
                "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
            ],
            "must_prove": [
                "在同一坏窗集合和同一 formal unit 下证明 direct acyclic PDEC 对偶容量证书",
                "或证明 diffuse clean residual 的 direct acyclic KLS/DLS 吸收并把失败命名回流",
                "若改用 canonical-lock，必须证明同集推前、无 payload 残留和有限因子图",
                "继续保持 seed 存在/不存在两支都覆盖",
                "保留高段尾项与 DStructure/Rankin 替代包的独立状态",
            ],
            "cannot_use_as_proof": [
                "把 seed 融合误写成 seed 已证明存在",
                "从 unsigned 早期零行覆盖图反推出 signed source seed",
                "把 canonical-source 终端闭合直接导入 acyclic noncanonical 分支",
                "把当前已物化样本清零当作全局终端家族排斥",
                "把外部谱定理或外部 Mertens/theta 当作 strict 自足证明",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步把 `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn` 从最终并列输入基中删除，"
            "但不是证明 seed 存在。理由是严格二分：若假设早期零行反例链能给出合法 seed，则后续 ExactUV、"
            "pair-mass、moving-atom 与 NC-BLK 路由已经把失败态接回 acyclic terminal family；若给不出 seed，"
            "来源环切断、早期零行 seed no-go 和独立来源恒等式分类又强制它回流同一 PDEC/SAE/ColumnCRT/CleanKLS "
            "终端家族。因此 seed 不再是独立闭合输入，真正剩余收缩为 acyclic terminal family，另加高段 "
            "Mertens/PNT 自足尾项与 DStructure/Rankin 替代包。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic seed 与终端家族门融合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"empirical_absence_not_used={str(result['empirical_absence_not_used']).lower()}",
        f"seed_exists_branch_covered_by_terminal_family={str(result['seed_exists_branch_covered_by_terminal_family']).lower()}",
        f"seed_absent_branch_returned_to_terminal_family={str(result['seed_absent_branch_returned_to_terminal_family']).lower()}",
        f"acyclic_pre_cauchy_seed_independent_input_removed={str(result['acyclic_pre_cauchy_seed_independent_input_removed']).lower()}",
        f"acyclic_pre_cauchy_seed_proved={str(result['acyclic_pre_cauchy_seed_proved']).lower()}",
        f"strict_acyclic_terminal_family_proved={str(result['strict_acyclic_terminal_family_proved']).lower()}",
        f"self_contained_mertens_tail_proved={str(result['self_contained_mertens_tail_proved']).lower()}",
        f"self_contained_dstructure_rankin_replacement_proved={str(result['self_contained_dstructure_rankin_replacement_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 融合二分",
        "",
        "```text",
        "Assume EarlyZeroRowWithinP",
        "  -> valid acyclic pre-Cauchy source seed exists",
        "       -> ExactUV / pair-mass / moving-atom / NC-BLK returns",
        "       -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        "  -> no valid seed exists",
        "       -> source-loop cut + zero-row seed no-go + identity taxonomy",
        "       -> PDEC / SAE / ColumnCRT / CleanKLS return",
        "       -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        "```",
        "",
        "所以本步只删除 seed 的独立输入地位；不声明 seed 定理成立。",
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
            "融合前：",
            "",
            "```text",
            result["strict_self_contained_math_basis_before_router"],
            "```",
            "",
            "融合后：",
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
            "三原子终端门：",
            "",
            "```text",
            contract["terminal_three_atom"],
            "```",
            "",
            "建议优先顺序：",
        ]
    )
    for item in contract["priority_order"]:
        lines.append(f"- `{item}`。")

    lines.extend(["", "必须证明："])
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
