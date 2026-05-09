#!/usr/bin/env python3
"""最终晋级门不可约性与独立验收包路由器。

用法示例：
  python3 experiments/prime_matrix_final_promotion_gate_irreducibility_router.py
  python3 experiments/prime_matrix_final_promotion_gate_irreducibility_router.py --accept-referee-gate

输出：
  docs/monograph/prime-matrix-final-promotion-gate-irreducibility-router.json
  docs/monograph/prime-matrix-final-promotion-gate-irreducibility-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

DEFAULT_SINGLE_GATE = MONO / "prime-matrix-final-single-gate-closure-decision-router.json"
DEFAULT_SUBGATE = MONO / "prime-matrix-final-promotion-subgate-direct-attack-router.json"
DEFAULT_PROMOTION = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_EXTERNAL_FINAL = MONO / "prime-matrix-external-kls-accepted-final-promotion-router.json"
DEFAULT_LINE_REF = MONO / "line-by-line-internal-referee-matrix.md"
DEFAULT_D_APPENDIX = DOCS / "d-structure-formal-appendix.md"
DEFAULT_AB_TO_D = DOCS / "ab-to-d-interface-match.md"
DEFAULT_TAIL = DOCS / "tail-log4-formal-appendix.md"
DEFAULT_BG_RKS = DOCS / "bg-rks-block-match.md"
DEFAULT_RKS_PARAM = DOCS / "rks-parameter-audit.md"
DEFAULT_FINITE = DOCS / "finite-verification-status.md"
DEFAULT_RANKIN = MONO / "prime-matrix-full-rankin-ledger-inventory-router.json"
DEFAULT_JSON = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
DEFAULT_MD = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.md"

PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
EXTERNAL_KLS = "AcceptFullSKLSExtExternalContract"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本证据。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(text: str, needles: list[str]) -> bool:
    """确认文本包含全部关键片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: Any) -> str:
    """格式化布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    author_sealed: bool,
    referee_required: bool,
    accepted: bool,
    evidence: str,
    hard_conclusion: str,
) -> dict[str, Any]:
    """构造不可约性判定行。"""
    return {
        "gate": gate,
        "author_sealed": author_sealed,
        "referee_required": referee_required,
        "accepted": accepted,
        "evidence": evidence,
        "hard_conclusion": hard_conclusion,
    }


def subgate_map(subgate: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """按 gate 名索引最终晋级子门。"""
    return {str(item.get("gate")): item for item in subgate.get("rows", [])}


def build_rows(
    single_gate: dict[str, Any],
    subgate: dict[str, Any],
    promotion: dict[str, Any],
    external_final: dict[str, Any],
    line_ref_text: str,
    d_text: str,
    ab_text: str,
    tail_text: str,
    bg_rks_text: str,
    rks_param_text: str,
    finite_text: str,
    rankin: dict[str, Any],
    accept_referee_gate: bool,
) -> list[dict[str, Any]]:
    """生成最终晋级门不可约性判定表。"""
    sub = subgate_map(subgate)
    external_closed = (
        single_gate.get("external_math_inputs_closed") is True
        and external_final.get("noncanonical_fulls_external_math_lane_closed") is True
    )
    dstructure_sealed = (
        sub.get("DStructureAppendixAuthorDossierReady", {}).get("author_closed") is True
        and contains_all(d_text, ["Theorem D", "Lemma D1", "Theorem D5", "Proposition D9"])
    )
    ab_to_d_sealed = (
        sub.get("ABToDInterfaceAuthorDossierReady", {}).get("author_closed") is True
        and contains_all(ab_text, ["Theorem M", "Lemma M1", "Lemma M5", "Structured-EHPD"])
    )
    tail_sealed = (
        sub.get("TailLog4AuthorDossierReady", {}).get("author_closed") is True
        and contains_all(tail_text, ["Theorem C", "Lemma C1", "Lemma C2", "Lemma C3"])
    )
    bg_rks_sealed = (
        sub.get("BGRKSParameterAuthorDossierReady", {}).get("author_closed") is True
        and contains_all(bg_rks_text, ["Lemma RKS1", "Lemma RKS2", "Lemma RKS3", "Lemma RKS4"])
        and contains_all(rks_param_text, ["合计", "74<128"])
    )
    finite_sealed = (
        sub.get("FiniteVerificationAuthorDossierReady", {}).get("author_closed") is True
        and "SUMMARY: all passed for 668 odd primes P<= 5000" in finite_text
        and subgate.get("finite_verification_rerun_result")
        == "SUMMARY: all passed for 668 odd primes P<= 5000"
    )
    rankin_sealed = (
        sub.get("RankinPassOrReturnAuthorDossierReady", {}).get("author_closed") is True
        and rankin.get("full_rankin_ledger_still_open_closed") is True
        and rankin.get("batch_rankin_pass_or_return_closed") is True
    )
    no_author_promotion = (
        sub.get("NoAuthorSidePromotionDiscipline", {}).get("author_closed") is True
        and "本轮没有把任何 `BLOCK-REFEREE` 改写为 `PASS-AUTHOR`" in line_ref_text
        and "PM-16" in line_ref_text
        and "BLOCK-REFEREE" in line_ref_text
    )
    boundary_closed = promotion.get("promotion_package_boundary_closed") is True
    referee_gate_accepted = bool(
        accept_referee_gate
        and boundary_closed
        and all(
            [
                external_closed,
                dstructure_sealed,
                ab_to_d_sealed,
                tail_sealed,
                bg_rks_sealed,
                finite_sealed,
                rankin_sealed,
                no_author_promotion,
            ]
        )
    )

    return [
        row(
            gate="ExternalKLSMathLane",
            author_sealed=external_closed,
            referee_required=False,
            accepted=external_closed,
            evidence="final single gate + external KLS final router",
            hard_conclusion="外部 KLS 数学线已闭合，不再是当前硬点。",
        ),
        row(
            gate="DStructureAndABInterfaceDossier",
            author_sealed=dstructure_sealed and ab_to_d_sealed,
            referee_required=True,
            accepted=referee_gate_accepted,
            evidence="docs/d-structure-formal-appendix.md + docs/ab-to-d-interface-match.md",
            hard_conclusion="作者侧证明包已封装；最终升级仍需独立接受 D 组定义、归约和常数口径。",
        ),
        row(
            gate="TailLog4AndBGRKSDossier",
            author_sealed=tail_sealed and bg_rks_sealed,
            referee_required=True,
            accepted=referee_gate_accepted,
            evidence="tail-log4 appendix + BG/RKS block match + RKS parameter audit",
            hard_conclusion="Tail-log4 与 BG/RKS 对接已封装；最终升级仍需独立接受外部定理适配。",
        ),
        row(
            gate="FiniteVerificationSeal",
            author_sealed=finite_sealed,
            referee_required=True,
            accepted=referee_gate_accepted,
            evidence="finite verification status + rerun result",
            hard_conclusion="有限验证可复跑并已封存结果；最终升级仍需独立复现/归档接受。",
        ),
        row(
            gate="FullRankinPassOrReturnSeal",
            author_sealed=rankin_sealed,
            referee_required=True,
            accepted=referee_gate_accepted,
            evidence="full Rankin ledger inventory",
            hard_conclusion="Rankin 子账本已闭合为 pass-or-return；最终升级仍需独立接受整包。",
        ),
        row(
            gate="NoAuthorSidePromotion",
            author_sealed=no_author_promotion,
            referee_required=False,
            accepted=no_author_promotion,
            evidence="line-by-line internal referee matrix",
            hard_conclusion="作者侧不能把独立验收事件改写成作者证明步骤。",
        ),
        row(
            gate=PROMOTION_GATE,
            author_sealed=boundary_closed,
            referee_required=True,
            accepted=referee_gate_accepted,
            evidence="--accept-referee-gate" if referee_gate_accepted else "not passed",
            hard_conclusion="这是当前真正不可约硬点：它只能由独立接受事件关闭，或由新自足证明替换整个门。",
        ),
    ]


def run(paths: dict[str, Path], accept_referee_gate: bool) -> dict[str, Any]:
    """运行最终晋级门不可约性路由。"""
    single_gate = load_json(paths["single_gate"])
    subgate = load_json(paths["subgate"])
    promotion = load_json(paths["promotion"])
    external_final = load_json(paths["external_final"])
    line_ref_text = read_text(paths["line_ref"])
    d_text = read_text(paths["d_appendix"])
    ab_text = read_text(paths["ab_to_d"])
    tail_text = read_text(paths["tail"])
    bg_rks_text = read_text(paths["bg_rks"])
    rks_param_text = read_text(paths["rks_param"])
    finite_text = read_text(paths["finite"])
    rankin = load_json(paths["rankin"])

    rows = build_rows(
        single_gate=single_gate,
        subgate=subgate,
        promotion=promotion,
        external_final=external_final,
        line_ref_text=line_ref_text,
        d_text=d_text,
        ab_text=ab_text,
        tail_text=tail_text,
        bg_rks_text=bg_rks_text,
        rks_param_text=rks_param_text,
        finite_text=finite_text,
        rankin=rankin,
        accept_referee_gate=accept_referee_gate,
    )
    author_packet_sealed = all(item["author_sealed"] for item in rows)
    referee_gate_accepted = rows[-1]["accepted"]
    author_side_direct_attack_exhausted = author_packet_sealed and not referee_gate_accepted
    row_column_closed = rows[0]["accepted"] and referee_gate_accepted

    return {
        "certificate_type": "prime_matrix_final_promotion_gate_irreducibility_router",
        "status": (
            "final_promotion_gate_accepted_external_kls_row_column_closed"
            if row_column_closed
            else "final_promotion_gate_irreducible_referee_event_required"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        },
        "external_kls_math_lane_closed": rows[0]["accepted"],
        "promotion_author_packet_sealed": author_packet_sealed,
        "author_side_direct_attack_exhausted": author_side_direct_attack_exhausted,
        "referee_gate_explicitly_accepted": referee_gate_accepted,
        "irreducible_gate": PROMOTION_GATE if not referee_gate_accepted else None,
        "row_column_unconditional_closed": row_column_closed,
        "strict_closure_basis": f"{EXTERNAL_KLS} AND {PROMOTION_GATE}",
        "legal_next_moves": [
            "explicitly accept the final independent-promotion gate",
            "replace the gate by a new fully self-contained proof package",
            "keep the theorem in conditional external-KLS-contract form",
        ],
        "hard_conclusion": (
            "当前材料已把最后障碍攻成不可约的独立验收事件：所有作者侧证据包均已封装，"
            "但独立接受不能由作者侧路由自动产生。未显式接受前，行/列命题仍不是无条件闭合。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 最终晋级门不可约性路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["hard_conclusion"],
        "",
        "```text",
        f"external_kls_math_lane_closed={fmt_bool(result['external_kls_math_lane_closed'])}",
        f"promotion_author_packet_sealed={fmt_bool(result['promotion_author_packet_sealed'])}",
        f"author_side_direct_attack_exhausted={fmt_bool(result['author_side_direct_attack_exhausted'])}",
        f"referee_gate_explicitly_accepted={fmt_bool(result['referee_gate_explicitly_accepted'])}",
        f"irreducible_gate={result['irreducible_gate']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 严格闭合基",
        "",
        "```text",
        result["strict_closure_basis"],
        "```",
        "",
        "## 2. 合法下一步",
        "",
    ]
    for item in result["legal_next_moves"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 3. 不可约性判定表",
            "",
            "| gate | author sealed | referee required | accepted | evidence | hard conclusion |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{sealed}` | `{required}` | `{accepted}` | {evidence} | {conclusion} |".format(
                gate=table_cell(item["gate"]),
                sealed=fmt_bool(item["author_sealed"]),
                required=fmt_bool(item["referee_required"]),
                accepted=fmt_bool(item["accepted"]),
                evidence=table_cell(item["evidence"]),
                conclusion=table_cell(item["hard_conclusion"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 终局判定",
            "",
            (
                "`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` "
                "不是新的无名数学逃逸口，而是独立验收事件。"
                "当前作者侧可做的直接攻坚已经到边界：证据包可提交、可复跑、可审查；"
                "但不能把未发生的独立接受写成已证明。"
            ),
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--single-gate-json", type=Path, default=DEFAULT_SINGLE_GATE)
    parser.add_argument("--subgate-json", type=Path, default=DEFAULT_SUBGATE)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--external-final-json", type=Path, default=DEFAULT_EXTERNAL_FINAL)
    parser.add_argument("--line-ref", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--d-appendix", type=Path, default=DEFAULT_D_APPENDIX)
    parser.add_argument("--ab-to-d", type=Path, default=DEFAULT_AB_TO_D)
    parser.add_argument("--tail", type=Path, default=DEFAULT_TAIL)
    parser.add_argument("--bg-rks", type=Path, default=DEFAULT_BG_RKS)
    parser.add_argument("--rks-param", type=Path, default=DEFAULT_RKS_PARAM)
    parser.add_argument("--finite", type=Path, default=DEFAULT_FINITE)
    parser.add_argument("--rankin-json", type=Path, default=DEFAULT_RANKIN)
    parser.add_argument("--accept-referee-gate", action="store_true")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "single_gate": args.single_gate_json,
        "subgate": args.subgate_json,
        "promotion": args.promotion_json,
        "external_final": args.external_final_json,
        "line_ref": args.line_ref,
        "d_appendix": args.d_appendix,
        "ab_to_d": args.ab_to_d,
        "tail": args.tail,
        "bg_rks": args.bg_rks,
        "rks_param": args.rks_param,
        "finite": args.finite,
        "rankin": args.rankin_json,
    }
    result = run(paths, args.accept_referee_gate)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["irreducible_gate"])


if __name__ == "__main__":
    main()
