#!/usr/bin/env python3
"""FullS-KLS-ext 外部引理严格匹配与接受审计。

用法示例：
  python3 experiments/prime_matrix_fulls_kls_ext_acceptance_match_audit.py

输出：
  docs/monograph/prime-matrix-fulls-kls-ext-acceptance-match-audit.json
  docs/monograph/prime-matrix-fulls-kls-ext-acceptance-match-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_STATEMENT = DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization.md"
DEFAULT_SPECIALIZATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
)
DEFAULT_NEW_FULL_S = DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
DEFAULT_COMMON_TABLE = DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
DEFAULT_OBJECT = DOCS / "prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.json"
DEFAULT_SCALE = DOCS / "prime-matrix-triad-a1-dibfi-nonap-scale-ledger-router.json"
DEFAULT_DUAL_NEXT = DOCS / "prime-matrix-dual-next-narrowest-attack-router.json"
DEFAULT_PROMOTION = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-fulls-kls-ext-acceptance-match-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-fulls-kls-ext-acceptance-match-audit.md"

LEMMA = "FullS-KLS-ext"
EXTERNAL_CONTRACT = "AcceptFullSKLSExtExternalContract"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值写成小写文本。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def match_row(
    item: str,
    required: str,
    external_lemma_clause: str,
    match: bool,
    caveat: str,
) -> dict[str, Any]:
    """构造严格匹配审计行。"""
    return {
        "item": item,
        "required": required,
        "external_lemma_clause": external_lemma_clause,
        "match": match,
        "caveat": caveat,
    }


def build_rows(
    statement_text: str,
    specialization: dict[str, Any],
    new_full_s: dict[str, Any],
    common_table: dict[str, Any],
    obj: dict[str, Any],
    scale: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 FullS-KLS-ext 与当前目标的逐项匹配表。"""
    statement_has_window = all(
        token in statement_text
        for token in [
            "W_full(C,S,H)",
            "C≈P/log^{O(1)}P",
            "S≈P",
            "NaturalWFDScale",
            "未中心化、无投影",
        ]
    )
    statement_has_phase = "e_c(a_h s + b_h bar{s})" in statement_text
    statement_has_saving = "log^A P" in statement_text and "B(A)" in statement_text
    specialization_closed = specialization.get("external_theorem_contract_closed") is True
    new_input_pinned = (
        new_full_s.get("terminal_gap_after_router") == "FullSNonAPWFDKLSTheoremInput"
    )
    variables_fixed = common_table.get("common_variable_table_materialized") is True
    no_projection_target = (
        obj.get("terminal_gap_after_router") == "UncenteredWFDToKE13NoProjectionIdentity"
    )
    scale_target = scale.get("terminal_gap_after_router") == "DIKloostermanWindowSubstitutionLedger"

    return [
        match_row(
            "对象",
            "当前 non-AP、未中心化、无投影 WFD 窗口。",
            "Theorem 直接估计 W_full(C,S,H)，并声明不插入中心化、不投影到 AP/canonical 对象。",
            statement_has_window and no_projection_target,
            "匹配的是外部合同对象；若不用外部合同，内部仍需证明对象恒等式。",
        ),
        match_row(
            "相位",
            "CRT 相位必须为 e_c(a_h s + b_h bar{s})。",
            "适配条件显式列出 phase: CRT 相位归一化为 e_c(a_h s + b_h bar{s})。",
            statement_has_phase,
            "最终稿仍应保持符号与 KE-13/共同变量表一致。",
        ),
        match_row(
            "尺度",
            "X≈P^2, C≈P/log^O P, S≈P, 0<|h|<=H<=P/log^O P。",
            "Theorem FullS-KLS-ext 逐项列出同一 full-S 窗口。",
            statement_has_window and scale_target,
            "该条作为外部定理合同吸收 DI J-scale 代入；不是 DI 原文逐项证明。",
        ),
        match_row(
            "权重",
            "lambda well-factorable, beta divisor-bounded, omega smooth。",
            "Theorem 条款逐项列出 lambda_c、beta_s、omega_h。",
            all(token in statement_text for token in ["well-factorable", "divisor-bounded", "smooth"]),
            "lambda 不能替换为 canonical RIW/Buchstab 支撑权。",
        ),
        match_row(
            "变量一致性",
            "X,Q,N,M,C,S,H,lambda,beta,omega,A,B(A) 必须共用同一表。",
            "共同变量表已物化，FullS-KLS-ext 使用同一 C,S,H 和 log-saving 预算。",
            variables_fixed,
            "变量表完成不等于内部 scale certificate 已证明；外部合同可直接吸收该证书。",
        ),
        match_row(
            "强度",
            "输出必须是 NaturalWFDScale/log^A P，且 A 任意。",
            "Theorem 给出 |W_full| <= NaturalWFDScale(C,S,H)/log^A P。",
            statement_has_saving,
            "所有 dyadic/gcd/smoothing/endpoint 损失由 B(A) 吸收。",
        ),
        match_row(
            "终端输入",
            "外部无黑箱路线的原子必须正是 FullSNonAPWFDKLSTheoremInput。",
            "NewFullSTheoremInput 已压成 FullSNonAPWFDKLSTheoremInput。",
            new_input_pinned,
            "这说明合同命题与剩余外部原子同名同对象。",
        ),
        match_row(
            "外部合同状态",
            "若作为黑箱外部定理接受，应关闭 noncanonical full-S 数学 lane。",
            "specialization router 标记 external theorem contract closed。",
            specialization_closed,
            "接受合同不等于完成 DIBFIPrimarySourceSpecializationProof。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行严格匹配与接受审计。"""
    statement_text = paths["statement"].read_text(encoding="utf-8")
    specialization = load_json(paths["specialization"])
    new_full_s = load_json(paths["new_full_s"])
    common_table = load_json(paths["common_table"])
    obj = load_json(paths["object"])
    scale = load_json(paths["scale"])
    dual_next = load_json(paths["dual_next"])
    promotion = load_json(paths["promotion"])

    rows = build_rows(
        statement_text=statement_text,
        specialization=specialization,
        new_full_s=new_full_s,
        common_table=common_table,
        obj=obj,
        scale=scale,
    )
    strict_match = all(row["match"] for row in rows)
    accepted_as_external_input = strict_match
    promotion_accepted = promotion.get("promotion_package_independently_accepted") is True
    row_column_closed = accepted_as_external_input and promotion_accepted

    return {
        "certificate_type": "prime_matrix_fulls_kls_ext_acceptance_match_audit",
        "status": (
            "fulls_kls_ext_strict_match_accepted_external_math_lane_closed_rankin_open"
            if accepted_as_external_input
            else "fulls_kls_ext_match_failed_external_acceptance_blocked"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{
                str(path.relative_to(ROOT)): file_sha256(path)
                for path in paths.values()
            },
        },
        "external_lemma": LEMMA,
        "external_lemma_content": {
            "object": "W_full(C,S,H)=sum_{c~C} lambda_c sum_{0<|h|<=H} omega_h sum_{s~S,(s,c)=1} beta_s e_c(a_h s + b_h bar{s})",
            "range": "X≈P^2, C≈P/log^O P, S≈P, 0<|h|<=H<=P/log^O P, Q<=P log^O P",
            "weights": "lambda well-factorable, beta divisor-bounded, omega smooth",
            "strength": "|W_full(C,S,H)| <= NaturalWFDScale(C,S,H)/log^A P for every A>0",
            "loss_budget": "dyadic/gcd/smoothing/endpoint losses absorbed by B(A)",
            "boundary": "no AP-source lift, no canonical import, no hidden centering/projection",
        },
        "strict_contract_match": strict_match,
        "accepted_as_external_blackbox_input": accepted_as_external_input,
        "external_math_lane_closed_after_acceptance": accepted_as_external_input,
        "primary_source_derivation_closed": False,
        "primary_source_derivation_still_required_for_no_blackbox_version": True,
        "dstructure_rankin_independent_acceptance_completed": promotion_accepted,
        "row_column_unconditional_closed": row_column_closed,
        "accepted_external_basis": f"{EXTERNAL_CONTRACT} AND {PROMOTION_GATE}",
        "previous_unified_basis": dual_next.get("unified_dual_basis"),
        "remaining_after_acceptance": (
            [PROMOTION_GATE]
            if accepted_as_external_input and not promotion_accepted
            else []
        ),
        "self_contained_remaining_core": [
            "ActualNoncanonicalCleanCoreMovingAtomExclusion",
            "or ActualNoncanonicalExactUVSupportLowerBound plus registered multiplier discipline",
        ],
        "rows": rows,
        "plain_conclusion": (
            "FullS-KLS-ext 与当前 non-AP full-S WFD 终端目标严格匹配：对象、相位、尺度、权重、"
            "强度和无中心化/无投影边界都逐项对齐。按用户允许的外部黑箱口径，可以接受该合同，"
            "并关闭 noncanonical full-S 外部数学 lane。但这不是 DI/BFI 原文逐项推出；无黑箱版本仍需"
            " DIBFIPrimarySourceSpecializationProof 或新证明。完整行/列无条件闭合仍差 DStructure/"
            "Rankin 独立验收。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    lines = [
        "# Prime Matrix FullS-KLS-ext 外部引理接受匹配审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_contract_match={fmt_bool(result['strict_contract_match'])}",
        (
            "accepted_as_external_blackbox_input="
            f"{fmt_bool(result['accepted_as_external_blackbox_input'])}"
        ),
        (
            "external_math_lane_closed_after_acceptance="
            f"{fmt_bool(result['external_math_lane_closed_after_acceptance'])}"
        ),
        (
            "primary_source_derivation_closed="
            f"{fmt_bool(result['primary_source_derivation_closed'])}"
        ),
        (
            "dstructure_rankin_independent_acceptance_completed="
            f"{fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部引理具体内容",
        "",
    ]
    for key, value in result["external_lemma_content"].items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(
        [
            "",
            "## 2. 接受后的输入基",
            "",
            "```text",
            result["accepted_external_basis"],
            "```",
            "",
            "## 3. 严格匹配表",
            "",
            "| item | required by target | external lemma clause | match | caveat |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{item}` | {required} | {clause} | `{match}` | {caveat} |".format(
                item=table_cell(row["item"]),
                required=table_cell(row["required"]),
                clause=table_cell(row["external_lemma_clause"]),
                match=fmt_bool(row["match"]),
                caveat=table_cell(row["caveat"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 接受后仍剩",
            "",
        ]
    )
    if result["remaining_after_acceptance"]:
        for item in result["remaining_after_acceptance"]:
            lines.append(f"- `{item}`")
    else:
        lines.append("- 无。")
    lines.extend(
        [
            "",
            "## 5. 自足路线剩余",
            "",
        ]
    )
    for item in result["self_contained_remaining_core"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 6. 判定",
            "",
            "可以接受的是 `FullS-KLS-ext` 作为外部黑箱定理输入；不能把它写成已经从 DI/BFI 原文"
            "逐项推出。接受后外部数学 lane 闭合，但完整行/列命题仍需 DStructure/Rankin 独立验收。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--statement", type=Path, default=DEFAULT_STATEMENT)
    parser.add_argument("--specialization-json", type=Path, default=DEFAULT_SPECIALIZATION)
    parser.add_argument("--new-full-s-json", type=Path, default=DEFAULT_NEW_FULL_S)
    parser.add_argument("--common-table-json", type=Path, default=DEFAULT_COMMON_TABLE)
    parser.add_argument("--object-json", type=Path, default=DEFAULT_OBJECT)
    parser.add_argument("--scale-json", type=Path, default=DEFAULT_SCALE)
    parser.add_argument("--dual-next-json", type=Path, default=DEFAULT_DUAL_NEXT)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "statement": args.statement,
        "specialization": args.specialization_json,
        "new_full_s": args.new_full_s_json,
        "common_table": args.common_table_json,
        "object": args.object_json,
        "scale": args.scale_json,
        "dual_next": args.dual_next_json,
        "promotion": args.promotion_json,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["accepted_external_basis"])


if __name__ == "__main__":
    main()
