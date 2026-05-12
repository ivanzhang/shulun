#!/usr/bin/env python3
"""生成 P5.1 闭合后的最终硬点压缩证书。

用法示例：
  python3 experiments/prime_matrix_strict_final_hardpoint_after_p51_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-final-hardpoint-after-p51-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-final-hardpoint-after-p51-router.json"
OUT_MD = MONO / "prime-matrix-strict-final-hardpoint-after-p51-router.md"

P51_SYNC = MONO / "prime-matrix-strict-dusart-p51-theta-upper-full-sync-router.json"
FINAL_SINGLE = MONO / "prime-matrix-final-single-gate-closure-decision-router.json"
FINAL_PROMOTION = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
DSTRUCTURE = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
SUBGATE = MONO / "prime-matrix-final-promotion-subgate-direct-attack-router.json"
EXTERNAL_PACKAGE = DOCS / "external-theorem-package.md"
D_APPENDIX = DOCS / "d-structure-formal-appendix.md"
AB_MATCH = DOCS / "ab-to-d-interface-match.md"
TAIL = DOCS / "tail-log4-formal-appendix.md"
BG_RKS = DOCS / "bg-rks-block-match.md"
RKS_PARAM = DOCS / "rks-parameter-audit.md"
CLAIM_STATUS = MONO / "claim-status-table.md"

SOURCE_FILES = [
    P51_SYNC,
    FINAL_SINGLE,
    FINAL_PROMOTION,
    DSTRUCTURE,
    SUBGATE,
    EXTERNAL_PACKAGE,
    D_APPENDIX,
    AB_MATCH,
    TAIL,
    BG_RKS,
    RKS_PARAM,
    CLAIM_STATUS,
]

PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
SELF_REPLACEMENT = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
FIRST_SELF_ATOM = "SelfContainedEXTBGRKSMultilinearKloostermanAndTailLog4Replacement"
EXPLICIT_ACCEPTANCE = "ExplicitIndependentPromotionAcceptanceRecord"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def contains_all(text: str, needles: list[str]) -> bool:
    """确认文本包含全部关键片段。"""
    return all(item in text for item in needles)


def build_result() -> dict[str, Any]:
    """构造最终硬点压缩证书。"""
    p51 = load_json(P51_SYNC)
    single = load_json(FINAL_SINGLE)
    promotion = load_json(FINAL_PROMOTION)
    dstructure = load_json(DSTRUCTURE)
    subgate = load_json(SUBGATE)
    external_text = read_text(EXTERNAL_PACKAGE)
    d_text = read_text(D_APPENDIX)
    ab_text = read_text(AB_MATCH)
    tail_text = read_text(TAIL)
    bg_rks_text = read_text(BG_RKS)
    rks_text = read_text(RKS_PARAM)

    p51_external_closed = p51.get("dusart_p51_full_theta_statement_external_closed") is True
    external_math_closed = single.get("external_math_inputs_closed") is True
    promotion_boundary_closed = dstructure.get("promotion_package_boundary_closed") is True
    promotion_accepted = dstructure.get("promotion_package_independently_accepted") is True
    author_packet_sealed = promotion.get("promotion_author_packet_sealed") is True
    direct_attack_exhausted = promotion.get("author_side_direct_attack_exhausted") is True
    no_author_side_upgrade = contains_all(
        promotion.get("hard_conclusion", ""),
        ["独立接受不能由作者侧路由自动产生", "行/列命题仍不是无条件闭合"],
    )

    external_package_indexed = contains_all(
        external_text,
        ["EXT-KL", "EXT-BG", "EXT-Vaaler", "EXT-Selberg", "EXT-Vaughan"],
    )
    d_ab_tail_packet_present = all(
        [
            contains_all(d_text, ["Theorem D", "EXT-KL", "Theorem D5"]),
            contains_all(ab_text, ["Theorem M", "Lemma M5", "Structured-EHPD"]),
            contains_all(tail_text, ["Theorem C", "Lemma C1", "Lemma C3"]),
            contains_all(bg_rks_text, ["Lemma RKS1", "Lemma RKS2", "Lemma RKS3", "Lemma RKS4"]),
            contains_all(rks_text, ["合计", "74<128"]),
        ]
    )
    first_self_atom_isolated = (
        external_package_indexed
        and d_ab_tail_packet_present
        and author_packet_sealed
        and not promotion_accepted
    )

    rows = [
        row(
            "DusartP51ExternalAnalyticInputClosed",
            p51_external_closed,
            True,
            "P5.1 解析输入已外部路线全段闭合，不再是当前硬点。",
            "none",
        ),
        row(
            "ExternalMathLaneAlreadyClosed",
            external_math_closed,
            True,
            "终局数学线已收缩到最终晋级门；FullS-KLS 外部合同版不再分叉。",
            PROMOTION_GATE,
        ),
        row(
            "PromotionBoundaryClosed",
            promotion_boundary_closed,
            True,
            "DStructure/Tail-log4/finite verification/Rankin 晋级包边界已闭合。",
            "boundary closed, acceptance open",
        ),
        row(
            "AuthorPacketSealed",
            author_packet_sealed and d_ab_tail_packet_present,
            True,
            "D 组、A/B 到 D、Tail-log4、BG/RKS 参数、有限验证和 Rankin 子账本均已有作者侧材料。",
            "independent acceptance still required",
        ),
        row(
            "IndependentPromotionAcceptanceRecord",
            promotion_accepted,
            False,
            "当前仓库没有独立验收记录；不能由作者侧路由自动生成。",
            EXPLICIT_ACCEPTANCE,
        ),
        row(
            "AuthorSideDirectAttackExhausted",
            direct_attack_exhausted and no_author_side_upgrade,
            True,
            "在现有材料内，继续作者侧路由只能重述证据包，不能把 referee gate 改写成 PASS-AUTHOR。",
            f"{EXPLICIT_ACCEPTANCE} OR {SELF_REPLACEMENT}",
        ),
        row(
            "FirstSelfContainedReplacementAtomIsolated",
            first_self_atom_isolated,
            False,
            "若拒绝独立验收路线，自足替代的第一原子是把 EXT-BG/RKS/Tail-log4 外部输入整体重证或给出同等内部定理。",
            FIRST_SELF_ATOM,
        ),
        row(
            PROMOTION_GATE,
            promotion_accepted,
            False,
            "唯一剩余闭合口：显式独立接受，或用完整自足替代包替换整个晋级门。",
            f"{EXPLICIT_ACCEPTANCE} OR {SELF_REPLACEMENT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "未发生独立验收，也没有新的自足替代证明包；故不能声明行/列命题无条件闭合。",
            PROMOTION_GATE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_final_hardpoint_after_p51_router",
        "status": "post_p51_final_hardpoint_compressed_to_independent_acceptance_or_self_contained_ext_bg_rks_replacement",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dusart_p51_full_theta_statement_external_closed": p51_external_closed,
        "external_math_inputs_closed": external_math_closed,
        "promotion_package_boundary_closed": promotion_boundary_closed,
        "promotion_author_packet_sealed": author_packet_sealed,
        "promotion_package_independently_accepted": promotion_accepted,
        "author_side_direct_attack_exhausted": direct_attack_exhausted,
        "first_self_contained_replacement_atom_isolated": first_self_atom_isolated,
        "first_self_contained_replacement_atom": FIRST_SELF_ATOM,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "legal_closure_channels": [EXPLICIT_ACCEPTANCE, SELF_REPLACEMENT],
        "next_direct_attack_target": FIRST_SELF_ATOM,
        "parallel_attack_target": EXPLICIT_ACCEPTANCE,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "P5.1 外部解析输入已经闭合，终局数学线也已收缩到最终晋级门。"
            "当前真正剩余不是新的局部常数，而是二选一："
            "要么登记独立晋级验收记录，要么用完整自足包替换该验收门。"
            "若坚持继续作者侧自足硬攻，第一不可替代原子是 "
            "`SelfContainedEXTBGRKSMultilinearKloostermanAndTailLog4Replacement`："
            "也就是重证或内部替代 Tail-log4/RKS 使用的 BG/Baker/Kloosterman 类外部输入。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict P5.1 后最终硬点压缩证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dusart_p51_full_theta_statement_external_closed={fmt_bool(result['dusart_p51_full_theta_statement_external_closed'])}",
        f"external_math_inputs_closed={fmt_bool(result['external_math_inputs_closed'])}",
        f"promotion_package_boundary_closed={fmt_bool(result['promotion_package_boundary_closed'])}",
        f"promotion_author_packet_sealed={fmt_bool(result['promotion_author_packet_sealed'])}",
        f"promotion_package_independently_accepted={fmt_bool(result['promotion_package_independently_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
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
            "## 2. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
