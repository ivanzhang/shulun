#!/usr/bin/env python3
"""生成 strict 终端叶子防火墙当前实例压缩路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_leaf_firewall_current_instance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json"
OUT_MD = DOCS / "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-terminal-descent-firewall-router.md",
    "prime-matrix-final-input-firewall-boundary-router.md",
    "prime-matrix-pdec-family-explicit-input-boundary-router.md",
    "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md",
    "prime-matrix-noncanonical-complement-trilemma-router.md",
    "prime-matrix-strict-acyclic-canonical-lock-router.md",
    "prime-matrix-strict-acyclic-seed-canonical-embedding-router.md",
]


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_result() -> dict[str, Any]:
    """构造当前实例叶子防火墙压缩证书。"""
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    leaf_before = (
        "AcyclicTerminalLeafFirewallInputs["
        "FutureExplicitPrimitivePDECSchema_if_new OR "
        "FutureExplicitSparsePacketExtractorSchema_if_new OR "
        "NoncanonicalFullSComplementLegalClosureMode]"
    )
    leaf_after_current_instance = "NoncanonicalFullSComplementLegalClosureMode"
    canonical_lock = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    terminal_after = f"{canonical_lock} OR {leaf_after_current_instance}"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis = (
        f"({terminal_after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis = (
        f"({terminal_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "TerminalLeafFirewallInputActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把无隐藏循环终端压到 canonical-lock 或叶子防火墙输入。",
            "remaining": f"{canonical_lock} OR {leaf_before}",
        },
        {
            "gate": "CurrentPDECInstanceFrontierZeroImported",
            "closed": True,
            "proved": True,
            "meaning": "当前已物化合法非二点 primitive PDEC 候选为零；这只清理当前语料实例。",
            "remaining": "未来新 PDEC 必须先提交 FutureExplicitPrimitivePDECSchema。",
        },
        {
            "gate": "CurrentSparseInstanceFrontierZeroImported",
            "closed": True,
            "proved": True,
            "meaning": "当前 sparse/LocalSurvivor 前沿没有开放物化义务；这只清理当前语料实例。",
            "remaining": "未来新 sparse route 必须先提交 FutureExplicitSparsePacketExtractorSchema。",
        },
        {
            "gate": "FuturePDECSchemaNotCurrentMathObligation",
            "closed": True,
            "proved": True,
            "meaning": "FutureExplicitPrimitivePDECSchema_if_new 是准入纪律，不是当前已经出现的叶子障碍。",
            "remaining": "若未来新增 PDEC family，则重开显式 schema 审查。",
        },
        {
            "gate": "FutureSparseSchemaNotCurrentMathObligation",
            "closed": True,
            "proved": True,
            "meaning": "FutureExplicitSparsePacketExtractorSchema_if_new 是准入纪律，不是当前已经出现的叶子障碍。",
            "remaining": "若未来新增 sparse family，则重开有限 extractor schema 审查。",
        },
        {
            "gate": "CurrentLeafFirewallActiveBasisReduced",
            "closed": True,
            "proved": True,
            "meaning": "在当前已物化实例内，叶子防火墙活动数学硬点只剩 noncanonical full-S 合法闭合模式。",
            "remaining": leaf_after_current_instance,
        },
        {
            "gate": "NoncanonicalLegalClosureModeCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "noncanonical full-S 补集仍未自足闭合；generic WFD 反原子已经不能使用。",
            "remaining": (
                "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR "
                "FullSNonAPStrengthenedSourceAntiAtomForActualSource OR "
                "accept/prove exact FullS-KLS-ext"
            ),
        },
        {
            "gate": "CanonicalLockStillOpenAlternative",
            "closed": True,
            "proved": False,
            "meaning": "canonical-lock 是并列替代路线，但需要 seed 因子嵌入、同集推前和无 payload 残留。",
            "remaining": canonical_lock,
        },
        {
            "gate": "TerminalLeafFirewallInputsCurrentInstanceProved",
            "closed": True,
            "proved": False,
            "meaning": "当前实例已压缩，但 noncanonical 合法模式未证，所以不能说叶子输入已全部证明或接受。",
            "remaining": f"{canonical_lock} OR {leaf_after_current_instance}",
        },
        {
            "gate": "StrictAcyclicTerminalFamilyCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "终端硬点更窄，但仍未闭合 acyclic terminal family。",
            "remaining": terminal_after,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "仍缺 terminal 二选一、高段 Mertens/PNT 自足尾项或外部接受、DStructure/Rankin 替代包。",
            "remaining": strict_basis,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_terminal_leaf_firewall_current_instance_router",
        "status": "strict_terminal_leaf_firewall_current_instance_reduced_future_schema_disciplined",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "current_materialized_pdec_frontier_closed": True,
        "current_materialized_sparse_frontier_closed": True,
        "future_pdec_schema_admission_discipline_closed": True,
        "future_sparse_schema_admission_discipline_closed": True,
        "current_leaf_firewall_active_basis_reduced": True,
        "future_schema_global_nonexistence_claimed": False,
        "terminal_leaf_firewall_inputs_proved_or_accepted": False,
        "noncanonical_legal_closure_mode_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "strict_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "row_column_unconditional_closed": False,
        "leaf_gap_before_router": leaf_before,
        "leaf_gap_after_current_instance_router": leaf_after_current_instance,
        "terminal_gap_after_current_instance_router": terminal_after,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis,
        "next_attack_contract": {
            "name": "NoncanonicalFullSComplementLegalClosureMode_OR_CanonicalLock",
            "must_prove": [
                "主攻 noncanonical full-S：证明实际源恒等，或证明强化实际源反原子，或明确接受/证明 exact FullS-KLS-ext",
                "并行备用 canonical-lock：证明 acyclic seed 可测有限因子嵌入、终端证书同集推前、无 noncanonical payload 残留",
                "若未来有人提出新 PDEC/sparse 路线，必须先提交对应显式 schema，不得作为隐藏终端使用",
                "保持高段 Mertens/PNT 自足尾项与 DStructure/Rankin 替代包独立验收",
            ],
            "cannot_use_as_proof": [
                "把当前 PDEC/sparse 前沿为零说成未来全局 family 不存在",
                "把 future schema firewall 当作 future schema 内容本身",
                "把 noncanonical 三歧边界闭合当成 noncanonical 分支已证明",
                "把 canonical-source PDEC-CAP 闭合直接导入 acyclic noncanonical 分支",
                "把外部 FullS-KLS 或 Mertens/theta 输入写成 strict 自足证明",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步把 `TerminalLeafFirewallInputs` 做当前实例压缩："
            "已物化 PDEC 前沿与 sparse/LocalSurvivor 前沿均为零，所以 "
            "`FutureExplicitPrimitivePDECSchema_if_new` 与 "
            "`FutureExplicitSparsePacketExtractorSchema_if_new` 在当前证明语料中不是活动数学障碍，"
            "而是未来准入纪律。它们不能被删除为全局不存在，只能从当前活动叶子中移出。"
            "因此当前 strict 自足终端剩余压成 "
            "`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
            "NoncanonicalFullSComplementLegalClosureMode`。"
            "noncanonical 合法闭合模式仍未证明，canonical-lock 也仍未证明；行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 终端叶子防火墙当前实例压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"current_materialized_pdec_frontier_closed={fmt_bool(result['current_materialized_pdec_frontier_closed'])}",
        f"current_materialized_sparse_frontier_closed={fmt_bool(result['current_materialized_sparse_frontier_closed'])}",
        f"future_pdec_schema_admission_discipline_closed={fmt_bool(result['future_pdec_schema_admission_discipline_closed'])}",
        f"future_sparse_schema_admission_discipline_closed={fmt_bool(result['future_sparse_schema_admission_discipline_closed'])}",
        f"current_leaf_firewall_active_basis_reduced={fmt_bool(result['current_leaf_firewall_active_basis_reduced'])}",
        f"future_schema_global_nonexistence_claimed={fmt_bool(result['future_schema_global_nonexistence_claimed'])}",
        f"terminal_leaf_firewall_inputs_proved_or_accepted={fmt_bool(result['terminal_leaf_firewall_inputs_proved_or_accepted'])}",
        f"noncanonical_legal_closure_mode_proved={fmt_bool(result['noncanonical_legal_closure_mode_proved'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"strict_acyclic_terminal_family_proved={fmt_bool(result['strict_acyclic_terminal_family_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_after_current_instance_router={result['terminal_gap_after_current_instance_router']}",
        "```",
        "",
        "## 1. 当前实例压缩链",
        "",
        "```text",
        "AcyclicTerminalLeafFirewallInputs[",
        "  FutureExplicitPrimitivePDECSchema_if_new",
        "  OR FutureExplicitSparsePacketExtractorSchema_if_new",
        "  OR NoncanonicalFullSComplementLegalClosureMode",
        "]",
        "  + current materialized PDEC frontier = 0",
        "  + current materialized sparse frontier = 0",
        "  + future schema clauses are admission discipline only",
        "  -> current active leaf = NoncanonicalFullSComplementLegalClosureMode",
        "```",
        "",
        "注意：这一步只移动当前活动硬点，不声明未来 PDEC/sparse family 全局不存在。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
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
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
