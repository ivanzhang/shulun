#!/usr/bin/env python3
"""生成 Prime Matrix strict 数学主线最新前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_mainline_latest_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-mainline-latest-frontier-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-mainline-latest-frontier-sync-router.json
  docs/monograph/prime-matrix-strict-mainline-latest-frontier-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-mainline-latest-frontier-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-mainline-latest-frontier-sync-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json",
    DOCS / "prime-matrix-current-terminal-promotion-reconciliation-router.json",
    DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json",
    DOCS / "prime-matrix-explicit-model-gap-finite-ledger-router.json",
    DOCS / "prime-matrix-self-contained-final-frontier-consolidation-router.json",
    DOCS / "prime-matrix-ordered-remaining-task-execution-router.json",
    DOCS / "prime-matrix-final-guard-gate-completion-verdict-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.json",
]

ZERO_FREE = "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000"
MERTENS_INTERVAL = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
DSTRUCTURE_ACCEPT = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
DSTRUCTURE_SELF = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"
GENERIC_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
CANONICAL_TERMINAL = "NoFurtherCanonicalSourceTerminalPromotionGap"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，便于前沿同步降级运行。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖证据哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造最新主线前沿同步对象。"""
    canonical = load_json(DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json")
    compat = load_json(DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json")
    explicit_gap = load_json(DOCS / "prime-matrix-explicit-model-gap-finite-ledger-router.json")
    frontier = load_json(DOCS / "prime-matrix-self-contained-final-frontier-consolidation-router.json")
    ordered = load_json(DOCS / "prime-matrix-ordered-remaining-task-execution-router.json")
    guard = load_json(DOCS / "prime-matrix-final-guard-gate-completion-verdict-router.json")
    final_closure = load_json(DOCS / "prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.json")

    canonical_closed = canonical.get("canonical_source_self_contained_theorem_closed") is True
    generic_refuted = final_closure.get("unrestricted_generic_self_contained_refuted") is True
    compat_closed = compat.get("exact_model_gap_dprc_compatibility_proved") is True
    finite_split = explicit_gap.get("explicit_model_gap_and_finite_dprc_ledger_split_closed") is True
    finite_dprc_closed = explicit_gap.get("finite_dprc_alpha043_p_below_2003_certificate_closed") is True
    author_tasks_done = ordered.get("author_side_completable_tasks_done") is True
    external_chain_closed = ordered.get("conditional_external_kls_proof_chain_closed") is True
    promotion_accepted = guard.get("promotion_package_independently_accepted") is True

    rows = [
        row(
            "CanonicalSourceSelfContainedBoundaryClosed",
            canonical_closed,
            canonical_closed,
            "canonical RIW/Buchstab source branch 的自足命题边界已闭合。",
            "无 canonical-source 自足终端缺口。",
        ),
        row(
            "UnrestrictedGenericSelfContainedRefuted",
            generic_refuted,
            generic_refuted,
            "unrestricted generic WFD 自足强化已由 moving-delta 模型阻断，不能作为可闭合目标声明。",
            "不得把 generic WFD 写成自足闭合命题。",
        ),
        row(
            "MovingBlockDPRCCompatibilityRemoved",
            compat_closed,
            compat_closed,
            "moving-block 到终端门的替换没有改变 DPRC 模型账本对象。",
            "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock 已从活动输入基删除。",
        ),
        row(
            "ExplicitModelGapFiniteSplitClosed",
            finite_split and finite_dprc_closed,
            finite_split and finite_dprc_closed,
            "ExplicitModelGapAndFiniteDPRCLedger 已拆成闭合有限段与高段模型余量。",
            "高段解析替代仍在严格自足路线中保留。",
        ),
        row(
            "ExternalMertensAndConditionalChainAuthorClosed",
            author_tasks_done and external_chain_closed,
            author_tasks_done and external_chain_closed,
            "作者侧条件链与外部 Mertens 锚点路线已完成。",
            "条件链不能替代最终独立晋级门。",
        ),
        row(
            "StrictSelfContainedPNTReplacementOpen",
            False,
            False,
            "若要求完全自足替代外部 Mertens/Dusart，下一步必须补内部显式 PNT/零点自由区包。",
            f"{ZERO_FREE} AND {MERTENS_INTERVAL}",
        ),
        row(
            "SelfContainedPromotionReplacementOpen",
            False,
            False,
            "若不接受独立晋级事件，必须用完整自足证明包替代 DStructure/Tail-log4/finite Rankin 门。",
            DSTRUCTURE_SELF,
        ),
        row(
            "IndependentPromotionAcceptanceAbsent",
            promotion_accepted,
            promotion_accepted,
            "外部 KLS 合同版要升级为完整行/列命题，仍需独立接受最终晋级包。",
            DSTRUCTURE_ACCEPT,
        ),
        row(
            "RowColumnUnconditionalClosedFromCurrentCorpus",
            False,
            False,
            "当前语料只能给 canonical-source 自足边界闭合和条件外部链；完整行/列无条件仍未闭合。",
            f"({ZERO_FREE} AND {MERTENS_INTERVAL} AND {DSTRUCTURE_SELF}) OR {DSTRUCTURE_ACCEPT}",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_mainline_latest_frontier_sync_router",
        "status": "strict_mainline_latest_frontier_synced_canonical_closed_global_unconditional_open",
        "same_theorem_target_preserved": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "canonical_source_self_contained_theorem_closed": canonical_closed,
        "unrestricted_generic_self_contained_refuted": generic_refuted,
        "moving_block_dprc_compatibility_closed": compat_closed,
        "explicit_model_gap_finite_split_closed": finite_split,
        "finite_dprc_alpha043_p_below_2003_closed": finite_dprc_closed,
        "author_side_conditional_chain_closed": author_tasks_done and external_chain_closed,
        "strict_self_contained_pnt_replacement_closed": False,
        "self_contained_promotion_replacement_closed": False,
        "promotion_package_independently_accepted": promotion_accepted,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ZERO_FREE,
        "secondary_attack_targets": [MERTENS_INTERVAL, DSTRUCTURE_SELF, DSTRUCTURE_ACCEPT],
        "canonical_self_contained_basis": CANONICAL_TERMINAL,
        "strict_self_contained_remaining_basis": (
            f"{CANONICAL_TERMINAL} AND {ZERO_FREE} AND {MERTENS_INTERVAL} AND {DSTRUCTURE_SELF}"
        ),
        "conditional_external_remaining_basis": (
            f"({CANONICAL_TERMINAL} OR AcceptFullSKLSExtExternalContract) AND {DSTRUCTURE_ACCEPT}"
        ),
        "generic_external_side_basis": f"{GENERIC_DIBFI} AND {DSTRUCTURE_ACCEPT}",
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本同步把当前数学主线固定为三层：第一，canonical RIW/Buchstab source branch "
            "的自足命题边界已经闭合；第二，unrestricted generic WFD 自足版不是开放缺口，"
            "而是被 moving-delta 模型反证，不能声明；第三，完整行/列无条件命题仍需 "
            "严格自足 PNT/Mertens 替代包与 DStructure/Rankin 自足晋级包，或外部合同加最终独立接受。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix strict 数学主线最新前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"canonical_source_self_contained_theorem_closed={fmt_bool(result['canonical_source_self_contained_theorem_closed'])}",
        f"unrestricted_generic_self_contained_refuted={fmt_bool(result['unrestricted_generic_self_contained_refuted'])}",
        f"moving_block_dprc_compatibility_closed={fmt_bool(result['moving_block_dprc_compatibility_closed'])}",
        f"author_side_conditional_chain_closed={fmt_bool(result['author_side_conditional_chain_closed'])}",
        f"strict_self_contained_pnt_replacement_closed={fmt_bool(result['strict_self_contained_pnt_replacement_closed'])}",
        f"self_contained_promotion_replacement_closed={fmt_bool(result['self_contained_promotion_replacement_closed'])}",
        f"promotion_package_independently_accepted={fmt_bool(result['promotion_package_independently_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最新判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 当前输入基",
            "",
            "canonical-source 自足边界：",
            "",
            "```text",
            result["canonical_self_contained_basis"],
            "```",
            "",
            "严格自足替代完整输入基：",
            "",
            "```text",
            result["strict_self_contained_remaining_basis"],
            "```",
            "",
            "外部合同条件输入基：",
            "",
            "```text",
            result["conditional_external_remaining_basis"],
            "```",
            "",
            "generic/external 分支输入基：",
            "",
            "```text",
            result["generic_external_side_basis"],
            "```",
            "",
            "## 3. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            "\n".join(result["secondary_attack_targets"]),
            "```",
            "",
            "审稿边界：本证书关闭的是最新前沿同步，不把 canonical-source 自足边界升级为完整行/列无条件定理。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
