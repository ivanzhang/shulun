#!/usr/bin/env python3
"""生成 strict acyclic 终端家族自回流循环守卫路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_terminal_cycle_guard_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-terminal-cycle-guard-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-terminal-cycle-guard-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-terminal-cycle-guard-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-terminal-fusion-router.md",
    "prime-matrix-strict-acyclic-terminal-family-attack-router.md",
    "prime-matrix-strict-acyclic-pdec-input-materialization-router.md",
    "prime-matrix-strict-acyclic-finite-arc-cap-router.md",
    "prime-matrix-strict-acyclic-clean-kls-router.md",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.md",
    "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.md",
    "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.md",
    "prime-matrix-strict-global-terminal-scope-router.md",
    "prime-matrix-pdec-cap-refinement-no-cycle.md",
    "prime-matrix-pdec-cap-same-set-global-dual-router.md",
    "prime-matrix-self-contained-pdec-cap-boundary-lift-router.md",
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

    terminal_family = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
    terminal_three_atom = (
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
        "DirectAcyclicSameSetPDECCapDualCertificate OR "
        "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    )
    guarded_terminal = (
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
        "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
    )
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis_after = (
        f"({guarded_terminal}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis_after = (
        f"({guarded_terminal}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "AcyclicTerminalFamilyActiveAfterSeedFusion",
            "closed": True,
            "proved": False,
            "meaning": "seed 融合后，当前唯一数学终端门是 acyclic noncanonical PDEC-CAP 或内部 CleanKLS。",
            "remaining": terminal_family,
        },
        {
            "gate": "ThreeAtomSplitImported",
            "closed": True,
            "proved": True,
            "meaning": "终端家族已拆成 canonical-lock、direct PDEC、direct clean KLS 三个入口。",
            "remaining": terminal_three_atom,
        },
        {
            "gate": "DirectPDECRouteSelfReturnDetected",
            "closed": True,
            "proved": True,
            "meaning": "direct PDEC 的同集输入和 dual-cap 定位闭合后，有限弧高质量若不命名回流就进入 direct clean KLS。",
            "remaining": "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn。",
        },
        {
            "gate": "DirectCleanRouteSelfReturnDetected",
            "closed": True,
            "proved": True,
            "meaning": "direct clean KLS 经 windowed DLS、KZ-E、NC-BLK/moving-atom 后又接回 global terminal family。",
            "remaining": terminal_family,
        },
        {
            "gate": "RawDirectEstimatesNotProgressMeasure",
            "closed": True,
            "proved": True,
            "meaning": "裸 direct PDEC 或裸 direct clean KLS 标签会形成 F -> ... -> F 的证明循环，不能作为闭合证明。",
            "remaining": "必须给出严格下降量或 canonical-lock。",
        },
        {
            "gate": "FixedLevelPDECNoCycleImported",
            "closed": True,
            "proved": True,
            "meaning": "固定有限签名群内的 PDEC cap 细化无循环已可用。",
            "remaining": "该事实只防止同一有限层无限细分。",
        },
        {
            "gate": "FixedLevelNoCycleInsufficientGlobally",
            "closed": True,
            "proved": True,
            "meaning": "strict 终端家族回流允许换层、new-layer、CleanKLS 和 global terminal scope；固定层无循环不足以排斥全局自回流。",
            "remaining": "需要跨回流的 well-founded descent certificate。",
        },
        {
            "gate": "CanonicalLockStillLegalExit",
            "closed": True,
            "proved": False,
            "meaning": "若能证明全部 acyclic terminal certificates canonical-lock 到 canonical-source 边界，则可复用 canonical 闭合。",
            "remaining": "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary。",
        },
        {
            "gate": "WellFoundedDescentGuardPinned",
            "closed": True,
            "proved": False,
            "meaning": "不走 canonical-lock 时，必须给每次 PDEC/SAE/ColumnCRT/CleanKLS 回流赋予严格下降的有限复杂度。",
            "remaining": "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate。",
        },
        {
            "gate": "TerminalCycleGuardReduced",
            "closed": True,
            "proved": False,
            "meaning": "三原子终端门已压成 canonical-lock 或非循环下降证书；裸 direct PDEC/CleanKLS 不再单独计为闭合路线。",
            "remaining": guarded_terminal,
        },
        {
            "gate": "StrictAcyclicTerminalFamilyCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前仓库尚未证明 canonical-lock，也未提交跨回流的严格下降量。",
            "remaining": guarded_terminal,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "终端循环守卫后仍缺 canonical-lock/下降证书、高段自足尾项或外部接受、DStructure/Rankin 替代包。",
            "remaining": strict_basis_after,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_terminal_cycle_guard_router",
        "status": "strict_acyclic_terminal_family_reduced_to_canonical_lock_or_well_founded_descent_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "terminal_family_self_return_detected": True,
        "direct_pdec_raw_route_self_return_detected": True,
        "direct_clean_raw_route_self_return_detected": True,
        "fixed_level_pdec_no_cycle_imported": True,
        "fixed_level_no_cycle_sufficient_for_global_terminal_family": False,
        "raw_direct_pdec_clean_routes_count_as_closure": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": terminal_three_atom,
        "terminal_gap_after_router": guarded_terminal,
        "strict_self_contained_math_basis_after_router": strict_basis_after,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis_after,
        "next_attack_contract": {
            "name": "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate_OR_CanonicalLock",
            "must_prove": [
                "定义每个 acyclic terminal record 的有限复杂度向量，例如 formal-unit level、未结坏窗数、签名秩、payload 维度、回流深度",
                "证明 PDEC/SAE/ColumnCRT/CleanKLS 每次命名回流在字典序上严格下降，或进入已封闭 canonical boundary",
                "证明 new-layer/refined PDEC 不能无限增广复杂度；若增广，则必须以更低未结质量或更小坏窗义务支付",
                "证明下降到底时只能到达已闭合的有限 packet、已排斥二点 tautology、或 canonical-source 边界",
                "若不能给下降量，则改证 AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
            ],
            "cannot_use_as_proof": [
                "重复 direct PDEC -> finite arc -> clean KLS -> NC-BLK -> terminal family 的自回流链",
                "把固定有限签名群 no-cycle 当作跨层全局 no-cycle",
                "把当前已物化有限塔证据当作全局有限塔证明",
                "把 canonical-source PDEC-CAP 闭合直接导入 acyclic noncanonical 终端",
                "把外部 DI/BFI/Kuznetsov 写成严格自足终端家族证明",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步发现并固定 strict acyclic 终端家族的真正循环障碍：裸 direct PDEC 分支已经被路由到有限弧，"
            "再到 direct clean KLS；裸 direct clean KLS 又经 windowed DLS、Kuznetsov/KZ-E、NC-BLK/moving-atom "
            "回到 global terminal family。因此不能再把 direct PDEC 或 direct CleanKLS 的标签本身当作进展。"
            "固定有限签名群内的 PDEC no-cycle 只防止同层无限细分，不足以排斥跨层回流。最新最窄剩余压成："
            "证明 acyclic terminal canonical-lock，或提交跨 PDEC/SAE/ColumnCRT/CleanKLS 回流的 well-founded "
            "严格下降证书。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic 终端家族循环守卫路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={str(result['counterexample_assumption_only']).lower()}",
        f"terminal_family_self_return_detected={str(result['terminal_family_self_return_detected']).lower()}",
        f"direct_pdec_raw_route_self_return_detected={str(result['direct_pdec_raw_route_self_return_detected']).lower()}",
        f"direct_clean_raw_route_self_return_detected={str(result['direct_clean_raw_route_self_return_detected']).lower()}",
        f"fixed_level_pdec_no_cycle_imported={str(result['fixed_level_pdec_no_cycle_imported']).lower()}",
        f"fixed_level_no_cycle_sufficient_for_global_terminal_family={str(result['fixed_level_no_cycle_sufficient_for_global_terminal_family']).lower()}",
        f"raw_direct_pdec_clean_routes_count_as_closure={str(result['raw_direct_pdec_clean_routes_count_as_closure']).lower()}",
        f"acyclic_terminal_canonical_lock_proved={str(result['acyclic_terminal_canonical_lock_proved']).lower()}",
        f"acyclic_terminal_return_well_founded_descent_proved={str(result['acyclic_terminal_return_well_founded_descent_proved']).lower()}",
        f"strict_acyclic_terminal_family_proved={str(result['strict_acyclic_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 自回流链",
        "",
        "```text",
        "F := PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        "",
        "F",
        "  -> DirectAcyclicSameSetPDECCapDualCertificate",
        "  -> AcyclicFiniteArcCapMassBoundsOrNamedReturn",
        "  -> DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
        "  -> AcyclicWindowedKloostermanDLSInternalEstimate",
        "  -> SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks",
        "  -> AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom",
        "  -> GlobalPDECorSparseTerminalExclusion",
        "  -> F",
        "```",
        "",
        "该链条只有在附带严格下降量时才是证明；否则只是循环路由。",
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
