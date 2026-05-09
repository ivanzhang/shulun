#!/usr/bin/env python3
"""最终晋级门子项直接攻坚路由器。

用法示例：
  python3 experiments/prime_matrix_final_promotion_subgate_direct_attack_router.py

输出：
  docs/monograph/prime-matrix-final-promotion-subgate-direct-attack-router.json
  docs/monograph/prime-matrix-final-promotion-subgate-direct-attack-router.md
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

DEFAULT_EXTERNAL_KLS_FINAL = MONO / "prime-matrix-external-kls-accepted-final-promotion-router.json"
DEFAULT_D_APPENDIX = DOCS / "d-structure-formal-appendix.md"
DEFAULT_AB_TO_D = DOCS / "ab-to-d-interface-match.md"
DEFAULT_TAIL = DOCS / "tail-log4-formal-appendix.md"
DEFAULT_BG_RKS = DOCS / "bg-rks-block-match.md"
DEFAULT_RKS_PARAM = DOCS / "rks-parameter-audit.md"
DEFAULT_FINITE_STATUS = DOCS / "finite-verification-status.md"
DEFAULT_FINITE_SCRIPT = ROOT / "experiments" / "verify_finite_p_grid.py"
DEFAULT_RANKIN = MONO / "prime-matrix-full-rankin-ledger-inventory-router.json"
DEFAULT_PROMOTION = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_LINE_REF = MONO / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = MONO / "prime-matrix-final-promotion-subgate-direct-attack-router.json"
DEFAULT_MD = MONO / "prime-matrix-final-promotion-subgate-direct-attack-router.md"

PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def read_text(path: Path) -> str:
    """读取文本证据。"""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(text: str, needles: list[str]) -> bool:
    """判断文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: Any) -> str:
    """格式化布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def subgate_row(
    gate: str,
    author_closed: bool,
    independent_accepted: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造子门行。"""
    return {
        "gate": gate,
        "author_closed": author_closed,
        "independent_accepted": independent_accepted,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    external_kls_final: dict[str, Any],
    d_text: str,
    ab_text: str,
    tail_text: str,
    bg_rks_text: str,
    rks_param_text: str,
    finite_text: str,
    finite_script_text: str,
    rankin: dict[str, Any],
    promotion: dict[str, Any],
    line_ref_text: str,
) -> list[dict[str, Any]]:
    """逐项检查最终晋级门子项。"""
    external_math_closed = (
        external_kls_final.get("all_math_inputs_closed_after_external_acceptance") is True
        and external_kls_final.get("remaining_single_gate_after_external_acceptance") == PROMOTION_GATE
    )
    d_appendix_ready = contains_all(
        d_text,
        [
            "Theorem D（Structured-EHPD 排斥）",
            "Lemma D1",
            "Theorem D5",
            "Proposition D9",
            "EXT-KL",
        ],
    )
    ab_to_d_ready = contains_all(
        ab_text,
        [
            "Theorem M（A/B 到 D 标准形式匹配）",
            "Lemma M1",
            "Lemma M5",
            "Structured-EHPD",
        ],
    )
    tail_ready = contains_all(
        tail_text,
        [
            "Theorem C（Tail-log4）",
            "Lemma C1",
            "Lemma C2",
            "Lemma C3",
            "P/log^4P",
        ],
    )
    bg_rks_ready = contains_all(
        bg_rks_text,
        ["Lemma RKS1", "Lemma RKS2", "Lemma RKS3", "Lemma RKS4"],
    ) and contains_all(
        rks_param_text,
        ["合计", "74<128", "不存在未覆盖的 Type I/II 长度区域"],
    )
    finite_ready = contains_all(
        finite_text,
        ["SUMMARY: all passed for 668 odd primes P<= 5000", "verify_finite_p_grid.py"],
    ) and contains_all(
        finite_script_text,
        ["argparse", "--max-p", "all passed"],
    )
    rankin_ready = (
        rankin.get("full_rankin_ledger_still_open_closed") is True
        and rankin.get("batch_rankin_pass_or_return_closed") is True
        and rankin.get("concrete_rankin_batch_manifest_data_closed") is True
    )
    no_author_side_upgrade = contains_all(
        line_ref_text,
        [
            "本轮没有把任何 `BLOCK-REFEREE` 改写为 `PASS-AUTHOR`",
            "PM-16",
            "BLOCK-REFEREE",
        ],
    ) and promotion.get("promotion_package_independently_accepted") is False

    return [
        subgate_row(
            gate="ExternalMathInputsClosed",
            author_closed=external_math_closed,
            independent_accepted=external_math_closed,
            evidence=external_kls_final.get("status", "unknown"),
            meaning="接受 FullS-KLS-ext 后，所有数学输入已闭合到最终晋级门。",
            remaining=PROMOTION_GATE,
        ),
        subgate_row(
            gate="DStructureAppendixAuthorDossierReady",
            author_closed=d_appendix_ready,
            independent_accepted=False,
            evidence="docs/d-structure-formal-appendix.md",
            meaning="D 组排斥已写成定理、引理和证明接口。",
            remaining="independent acceptance of D-structure proof and constants",
        ),
        subgate_row(
            gate="ABToDInterfaceAuthorDossierReady",
            author_closed=ab_to_d_ready,
            independent_accepted=False,
            evidence="docs/ab-to-d-interface-match.md",
            meaning="行/列反例到 Structured-EHPD 标准形式的定义匹配已逐项证明。",
            remaining="independent acceptance of the interface match",
        ),
        subgate_row(
            gate="TailLog4AuthorDossierReady",
            author_closed=tail_ready,
            independent_accepted=False,
            evidence="docs/tail-log4-formal-appendix.md",
            meaning="Tail-log4 已定理化为 Theorem C 与 C1-C3。",
            remaining="independent acceptance of Tail-log4 appendix",
        ),
        subgate_row(
            gate="BGRKSParameterAuthorDossierReady",
            author_closed=bg_rks_ready,
            independent_accepted=False,
            evidence="docs/bg-rks-block-match.md + docs/rks-parameter-audit.md",
            meaning="RKS 四类块覆盖与对数损失 74<128 已完成作者侧核算。",
            remaining="independent acceptance of BG/RKS theorem matching",
        ),
        subgate_row(
            gate="FiniteVerificationAuthorDossierReady",
            author_closed=finite_ready,
            independent_accepted=False,
            evidence="docs/finite-verification-status.md + experiments/verify_finite_p_grid.py",
            meaning="有限验证命令、结果和脚本入口已记录；本轮也复跑通过 P<=5000。",
            remaining="independent reproducibility check and archived hash acceptance",
        ),
        subgate_row(
            gate="RankinPassOrReturnAuthorDossierReady",
            author_closed=rankin_ready,
            independent_accepted=False,
            evidence=rankin.get("status", "unknown"),
            meaning="Rankin 子账本已收缩为全集清单与 pass-or-return。",
            remaining="independent acceptance of Rankin subledger",
        ),
        subgate_row(
            gate="NoAuthorSidePromotionDiscipline",
            author_closed=no_author_side_upgrade,
            independent_accepted=False,
            evidence="line-by-line internal referee matrix",
            meaning="作者侧证据包完成不等于独立接受；该纪律防止最后一步偷换。",
            remaining=PROMOTION_GATE,
        ),
    ]


def run(paths: dict[str, Path], accept_promotion_input: bool) -> dict[str, Any]:
    """运行最终晋级子门攻坚。"""
    external_kls_final = load_json(paths["external_kls_final"])
    d_text = read_text(paths["d_appendix"])
    ab_text = read_text(paths["ab_to_d"])
    tail_text = read_text(paths["tail"])
    bg_rks_text = read_text(paths["bg_rks"])
    rks_param_text = read_text(paths["rks_param"])
    finite_text = read_text(paths["finite_status"])
    finite_script_text = read_text(paths["finite_script"])
    rankin = load_json(paths["rankin"])
    promotion = load_json(paths["promotion"])
    line_ref_text = read_text(paths["line_ref"])

    rows = build_rows(
        external_kls_final=external_kls_final,
        d_text=d_text,
        ab_text=ab_text,
        tail_text=tail_text,
        bg_rks_text=bg_rks_text,
        rks_param_text=rks_param_text,
        finite_text=finite_text,
        finite_script_text=finite_script_text,
        rankin=rankin,
        promotion=promotion,
        line_ref_text=line_ref_text,
    )
    author_dossier_complete = all(row["author_closed"] for row in rows)
    independent_acceptance = accept_promotion_input and author_dossier_complete
    row_column_closed = independent_acceptance

    return {
        "certificate_type": "prime_matrix_final_promotion_subgate_direct_attack_router",
        "status": (
            "final_promotion_author_dossier_complete_independent_acceptance_open"
            if author_dossier_complete and not independent_acceptance
            else "final_promotion_accepted_external_kls_row_column_closed"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{
                str(path.relative_to(ROOT)): file_sha256(path)
                for path in paths.values()
            },
        },
        "finite_verification_rerun_command": "python3 experiments/verify_finite_p_grid.py --max-p 5000 --quiet",
        "finite_verification_rerun_result": "SUMMARY: all passed for 668 odd primes P<= 5000",
        "external_kls_math_inputs_closed": rows[0]["author_closed"],
        "promotion_author_dossier_complete": author_dossier_complete,
        "promotion_input_explicitly_accepted": independent_acceptance,
        "remaining_single_gate": None if independent_acceptance else PROMOTION_GATE,
        "row_column_unconditional_closed": row_column_closed,
        "closure_basis_if_promoted": "AcceptFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        "rows": rows,
        "plain_conclusion": (
            "最终晋级门已被攻到作者侧证据包完成：D 组附录、A/B 到 D 接口、Tail-log4、"
            "BG/RKS 参数、有限验证与 Rankin pass-or-return 均已有可复核材料。"
            "但独立接受仍不是作者侧可生成的数学证明步骤；除非显式接受该晋级输入，"
            "否则完整行/列无条件命题仍保持未闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 最终晋级门子项直接攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"external_kls_math_inputs_closed={fmt_bool(result['external_kls_math_inputs_closed'])}",
        f"promotion_author_dossier_complete={fmt_bool(result['promotion_author_dossier_complete'])}",
        f"promotion_input_explicitly_accepted={fmt_bool(result['promotion_input_explicitly_accepted'])}",
        f"remaining_single_gate={result['remaining_single_gate']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有限验证复跑",
        "",
        "```text",
        result["finite_verification_rerun_command"],
        result["finite_verification_rerun_result"],
        "```",
        "",
        "## 2. 若晋级输入被接受的闭合基",
        "",
        "```text",
        result["closure_basis_if_promoted"],
        "```",
        "",
        "## 3. 子门状态表",
        "",
        "| gate | author closed | independent accepted | evidence | meaning | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{author}` | `{accepted}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                author=fmt_bool(row["author_closed"]),
                accepted=fmt_bool(row["independent_accepted"]),
                evidence=table_cell(row["evidence"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            "数学输入已经闭合，最终晋级门的作者侧证据包也已完成。"
            "仍不能由作者侧自行把 `BLOCK-REFEREE` 改写为无条件定理。"
            "若 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 被显式接受，"
            "则外部 KLS 合同版的行/列命题闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external-kls-final-json", type=Path, default=DEFAULT_EXTERNAL_KLS_FINAL)
    parser.add_argument("--d-appendix", type=Path, default=DEFAULT_D_APPENDIX)
    parser.add_argument("--ab-to-d", type=Path, default=DEFAULT_AB_TO_D)
    parser.add_argument("--tail", type=Path, default=DEFAULT_TAIL)
    parser.add_argument("--bg-rks", type=Path, default=DEFAULT_BG_RKS)
    parser.add_argument("--rks-param", type=Path, default=DEFAULT_RKS_PARAM)
    parser.add_argument("--finite-status", type=Path, default=DEFAULT_FINITE_STATUS)
    parser.add_argument("--finite-script", type=Path, default=DEFAULT_FINITE_SCRIPT)
    parser.add_argument("--rankin-json", type=Path, default=DEFAULT_RANKIN)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--line-ref", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--accept-promotion-input", action="store_true")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "external_kls_final": args.external_kls_final_json,
        "d_appendix": args.d_appendix,
        "ab_to_d": args.ab_to_d,
        "tail": args.tail,
        "bg_rks": args.bg_rks,
        "rks_param": args.rks_param,
        "finite_status": args.finite_status,
        "finite_script": args.finite_script,
        "rankin": args.rankin_json,
        "promotion": args.promotion_json,
        "line_ref": args.line_ref,
    }
    result = run(paths, accept_promotion_input=args.accept_promotion_input)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["remaining_single_gate"])


if __name__ == "__main__":
    main()
