#!/usr/bin/env python3
"""生成 strict acyclic 终端回流下降到最终防火墙输入的路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_terminal_descent_firewall_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-terminal-descent-firewall-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-terminal-descent-firewall-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-terminal-cycle-guard-router.md",
    "prime-matrix-pdec-cap-refinement-no-cycle.md",
    "prime-matrix-newlayer-pdec-tower-entropy-contract.md",
    "prime-matrix-composite-cofactor-descent-schema-router.md",
    "prime-matrix-early-band-local-survivor-return-schema-router.md",
    "prime-matrix-dls-shortwindow-sae-return-schema-router.md",
    "prime-matrix-dls-pointload-columncrt-return-schema-router.md",
    "prime-matrix-dls-fixedwheel-pdec-return-schema-router.md",
    "prime-matrix-early-zero-terminal-schema-reconciliation-router.md",
    "prime-matrix-pdec-family-explicit-input-boundary-router.md",
    "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md",
    "prime-matrix-final-input-firewall-boundary-router.md",
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

    before = (
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
        "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
    )
    leaf_inputs = (
        "AcyclicTerminalLeafFirewallInputs"
        "[FutureExplicitPrimitivePDECSchema_if_new OR "
        "FutureExplicitSparsePacketExtractorSchema_if_new OR "
        "NoncanonicalFullSComplementLegalClosureMode]"
    )
    after = f"AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR {leaf_inputs}"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis_after = (
        f"({after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis_after = (
        f"({after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "WellFoundedDescentInputActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 direct 终端自回流压成 canonical-lock 或 well-founded descent 证书。",
            "remaining": before,
        },
        {
            "gate": "FixedPDECRefinementNoCycleClosed",
            "closed": True,
            "proved": True,
            "meaning": "固定有限签名群内 cap 细化由 Boolean algebra 秩严格上升控制，不能无限循环。",
            "remaining": "升层或叶子终端仍需处理。",
        },
        {
            "gate": "NewLayerTowerNoUnnamedEscapeClosed",
            "closed": True,
            "proved": True,
            "meaning": "无限升层有熵发散 PDEC、有限截断 ColumnCRT/PDEC、熵可和 CleanKLS 或 Multiplicity/Stitching 四归宿。",
            "remaining": "这些归宿是命名叶子，不是终端排斥证明。",
        },
        {
            "gate": "CompositeCofactorDescentClosed",
            "closed": True,
            "proved": True,
            "meaning": "复合 cofactor 递归以 m<P 或粗因子深度下降，不能形成无穷无名链。",
            "remaining": "持久进 PDEC，孤立进 sparse/SAE。",
        },
        {
            "gate": "LocalSurvivorAndSAESchemaClosed",
            "closed": True,
            "proved": True,
            "meaning": "early-band、short-window、point-load 与 fixed-wheel 专属出口均已命名为 finite packet、PDEC/ColumnCRT 或 CleanKLS 回流。",
            "remaining": "全局 PDEC/sparse 叶子排斥未完成。",
        },
        {
            "gate": "SourceLoopReimportBlocked",
            "closed": True,
            "proved": True,
            "meaning": "若终端包经 signed/source 路线回到 clean-core 来源，会落入已切断来源环并回到 moving-block/终端包。",
            "remaining": "不能把该环当证明；必须落到终端防火墙输入。",
        },
        {
            "gate": "CurrentMaterializedPDECFrontierZero",
            "closed": True,
            "proved": True,
            "meaning": "当前已物化合法非二点 primitive PDEC 候选为零；未来 PDEC 必须提交显式 primitive schema。",
            "remaining": "FutureExplicitPrimitivePDECSchema_if_new。",
        },
        {
            "gate": "CurrentMaterializedSparseFrontierZero",
            "closed": True,
            "proved": True,
            "meaning": "当前 sparse/LocalSurvivor 前沿没有开放物化义务；未来 sparse 必须提交有限 packet extractor schema。",
            "remaining": "FutureExplicitSparsePacketExtractorSchema_if_new。",
        },
        {
            "gate": "TerminalDescentSchemaClosed",
            "closed": True,
            "proved": True,
            "meaning": "跨 PDEC/SAE/ColumnCRT/CleanKLS 的无名自回流已被下降 schema 与防火墙边界删除。",
            "remaining": leaf_inputs,
        },
        {
            "gate": "TerminalLeafExclusionCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "叶子终端仍未全部排斥；当前结论只是要求它们以显式 schema 或 noncanonical 合法模式进入。",
            "remaining": leaf_inputs,
        },
        {
            "gate": "NoncanonicalLegalClosureModeCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "noncanonical full-S 补集仍需实际源恒等、强化实际源反原子或外部 FullS-KLS/DI-BFI 合同之一。",
            "remaining": "NoncanonicalFullSComplementLegalClosureMode。",
        },
        {
            "gate": "StrictAcyclicTerminalFamilyCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "终端家族不再有隐藏循环，但叶子防火墙输入尚未全部证明或接受。",
            "remaining": after,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "下降防火墙后仍缺终端叶子输入、高段自足尾项或外部接受、DStructure/Rankin 替代包。",
            "remaining": strict_basis_after,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_terminal_descent_firewall_router",
        "status": "strict_acyclic_terminal_descent_schema_closed_leaf_firewall_inputs_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "terminal_return_well_founded_descent_schema_closed": True,
        "hidden_terminal_cycle_removed": True,
        "current_materialized_pdec_frontier_closed": True,
        "current_materialized_sparse_frontier_closed": True,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "terminal_leaf_firewall_inputs_proved_or_accepted": False,
        "noncanonical_legal_closure_mode_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "strict_terminal_family_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": before,
        "terminal_gap_after_router": after,
        "strict_self_contained_math_basis_after_router": strict_basis_after,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis_after,
        "next_attack_contract": {
            "name": "TerminalLeafFirewallInputs_OR_CanonicalLock",
            "must_prove": [
                "若坚持 canonical-lock，证明同集推前、有限因子图和无 noncanonical payload 残留",
                "若出现未来 PDEC 叶子，提交并排斥 FutureExplicitPrimitivePDECSchema",
                "若出现未来 sparse 叶子，提交并排斥 FutureExplicitSparsePacketExtractorSchema",
                "关闭 noncanonical full-S 合法模式：实际源恒等、强化实际源反原子，或明确接受外部 FullS-KLS/DI-BFI",
                "继续独立处理高段 Mertens/PNT 自足尾项与 DStructure/Rankin 替代包",
            ],
            "cannot_use_as_proof": [
                "把无隐藏循环当作叶子终端已经排斥",
                "把当前物化前沿为零当作未来全局 family 不存在",
                "把 future schema firewall 当作 schema 内容本身",
                "把 noncanonical 外部合同写成 strict 自足证明",
                "把 DStructure/Rankin 晋级门混入终端叶子排斥",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步把 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` 的无隐藏循环部分关闭为 schema："
            "固定 PDEC 细化、new-layer 塔、复合 cofactor、LocalSurvivor/SAE、short-window、point-load 和 fixed-wheel "
            "都不能形成无名自回流；它们要么下降，要么进入显式 PDEC/sparse 叶子，要么回到 noncanonical 合法闭合模式。"
            "但这不是终端叶子排斥证明。当前最窄剩余从“循环”压成 `TerminalLeafFirewallInputs` 或 canonical-lock："
            "未来 PDEC/sparse 必须提交显式 schema，noncanonical 分支必须证明实际源恒等/强化反原子或接受外部合同。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic 终端下降到防火墙输入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_return_well_founded_descent_schema_closed={str(result['terminal_return_well_founded_descent_schema_closed']).lower()}",
        f"hidden_terminal_cycle_removed={str(result['hidden_terminal_cycle_removed']).lower()}",
        f"current_materialized_pdec_frontier_closed={str(result['current_materialized_pdec_frontier_closed']).lower()}",
        f"current_materialized_sparse_frontier_closed={str(result['current_materialized_sparse_frontier_closed']).lower()}",
        f"acyclic_terminal_return_well_founded_descent_proved={str(result['acyclic_terminal_return_well_founded_descent_proved']).lower()}",
        f"terminal_leaf_firewall_inputs_proved_or_accepted={str(result['terminal_leaf_firewall_inputs_proved_or_accepted']).lower()}",
        f"noncanonical_legal_closure_mode_proved={str(result['noncanonical_legal_closure_mode_proved']).lower()}",
        f"strict_acyclic_terminal_family_proved={str(result['strict_acyclic_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 下降到叶子",
        "",
        "```text",
        "acyclic terminal self-return",
        "  -> fixed PDEC cap no-cycle",
        "  -> new-layer entropy tower dichotomy",
        "  -> composite cofactor well-founded descent",
        "  -> LocalSurvivor/SAE/short-window/point-load/fixed-wheel named returns",
        "  -> no hidden terminal cycle",
        "  -> explicit leaf firewall inputs",
        "```",
        "",
        "关闭的是无隐藏循环，不是叶子输入本身。",
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
