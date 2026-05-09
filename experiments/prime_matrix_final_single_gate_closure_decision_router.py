#!/usr/bin/env python3
"""最终单门闭合判定路由器。

用法示例：
  python3 experiments/prime_matrix_final_single_gate_closure_decision_router.py
  python3 experiments/prime_matrix_final_single_gate_closure_decision_router.py --accept-final-promotion-input

输出：
  docs/monograph/prime-matrix-final-single-gate-closure-decision-router.json
  docs/monograph/prime-matrix-final-single-gate-closure-decision-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_EXTERNAL_FINAL = MONO / "prime-matrix-external-kls-accepted-final-promotion-router.json"
DEFAULT_SUBGATE = MONO / "prime-matrix-final-promotion-subgate-direct-attack-router.json"
DEFAULT_PROMOTION = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-unconditional-closure-endpoint-verdict-router.json"
DEFAULT_LINE_REF = MONO / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = MONO / "prime-matrix-final-single-gate-closure-decision-router.json"
DEFAULT_MD = MONO / "prime-matrix-final-single-gate-closure-decision-router.md"

EXTERNAL_CONTRACT = "AcceptFullSKLSExtExternalContract"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本证据。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    boundary_closed: bool,
    accepted_or_proved: bool,
    evidence: str,
    meaning: str,
    consequence: str,
) -> dict[str, Any]:
    """构造最终判定表行。"""
    return {
        "gate": gate,
        "boundary_closed": boundary_closed,
        "accepted_or_proved": accepted_or_proved,
        "evidence": evidence,
        "meaning": meaning,
        "consequence": consequence,
    }


def subgate_author_rows_closed(subgate: dict[str, Any]) -> bool:
    """确认最终晋级门的作者侧子门都已完成。"""
    rows = subgate.get("rows", [])
    return bool(rows) and all(item.get("author_closed") is True for item in rows)


def subgate_names(subgate: dict[str, Any]) -> list[str]:
    """提取子门名称。"""
    return [str(item.get("gate", "")) for item in subgate.get("rows", [])]


def build_rows(
    external_final: dict[str, Any],
    subgate: dict[str, Any],
    promotion: dict[str, Any],
    endpoint: dict[str, Any],
    line_ref_text: str,
    accept_final_promotion_input: bool,
) -> list[dict[str, Any]]:
    """构造最终单门闭合判定表。"""
    external_math_closed = (
        external_final.get("external_fulls_kls_accepted") is True
        and external_final.get("all_math_inputs_closed_after_external_acceptance") is True
        and external_final.get("remaining_single_gate_after_external_acceptance") == PROMOTION_GATE
    )
    endpoint_boundary_closed = (
        endpoint.get("endpoint_boundary_closed") is True
        and endpoint.get("row_column_unconditional_closed") is False
    )
    promotion_boundary_closed = promotion.get("promotion_package_boundary_closed") is True
    author_dossier_complete = (
        subgate.get("promotion_author_dossier_complete") is True
        and subgate_author_rows_closed(subgate)
    )
    no_author_side_promotion = (
        "本轮没有把任何 `BLOCK-REFEREE` 改写为 `PASS-AUTHOR`" in line_ref_text
        and "PM-16" in line_ref_text
        and "BLOCK-REFEREE" in line_ref_text
    )
    final_promotion_accepted = bool(accept_final_promotion_input and author_dossier_complete)

    return [
        row(
            gate="ExternalKLSMathLaneClosed",
            boundary_closed=external_math_closed,
            accepted_or_proved=external_math_closed,
            evidence=external_final.get("status", "unknown"),
            meaning="FullS-KLS-ext 已作为严格匹配的外部黑箱输入接受，noncanonical full-S 数学线闭合。",
            consequence="数学线不再分叉；只剩最终晋级门。",
        ),
        row(
            gate="EndpointNoHiddenMathRoute",
            boundary_closed=endpoint_boundary_closed,
            accepted_or_proved=endpoint_boundary_closed,
            evidence=endpoint.get("status", "unknown"),
            meaning="终局路由已经排除未命名第四路线，当前不能继续转换目标。",
            consequence="剩余必须落在命名输入或验收门上。",
        ),
        row(
            gate="PromotionPackageBoundaryClosed",
            boundary_closed=promotion_boundary_closed,
            accepted_or_proved=False,
            evidence=promotion.get("status", "unknown"),
            meaning="DStructure/Tail-log4/finite verification/Rankin 晋级包边界已闭合。",
            consequence="边界闭合不等于独立接受。",
        ),
        row(
            gate="PromotionAuthorDossierComplete",
            boundary_closed=author_dossier_complete,
            accepted_or_proved=author_dossier_complete,
            evidence=", ".join(subgate_names(subgate)),
            meaning="D 组、A/B 到 D、Tail-log4、BG/RKS、有限验证、Rankin 子账本均有作者侧可复核材料。",
            consequence="可提交独立验收；作者侧不能自行晋级。",
        ),
        row(
            gate="NoAuthorSidePromotionDiscipline",
            boundary_closed=no_author_side_promotion,
            accepted_or_proved=no_author_side_promotion,
            evidence="line-by-line internal referee matrix",
            meaning="逐行矩阵明确禁止把 BLOCK-REFEREE 改写成 PASS-AUTHOR。",
            consequence="避免把条件闭合伪装为无条件自足闭合。",
        ),
        row(
            gate="FinalPromotionInputAccepted",
            boundary_closed=author_dossier_complete,
            accepted_or_proved=final_promotion_accepted,
            evidence="--accept-final-promotion-input" if final_promotion_accepted else "not passed",
            meaning="只有显式接受最终晋级输入，才能把外部 KLS 合同版升级为完整行/列闭合。",
            consequence="accepted => row_column_unconditional_closed=true; otherwise false。",
        ),
    ]


def run(paths: dict[str, Path], accept_final_promotion_input: bool) -> dict[str, Any]:
    """运行最终单门闭合判定。"""
    external_final = load_json(paths["external_final"])
    subgate = load_json(paths["subgate"])
    promotion = load_json(paths["promotion"])
    endpoint = load_json(paths["endpoint"])
    line_ref_text = read_text(paths["line_ref"])

    rows = build_rows(
        external_final=external_final,
        subgate=subgate,
        promotion=promotion,
        endpoint=endpoint,
        line_ref_text=line_ref_text,
        accept_final_promotion_input=accept_final_promotion_input,
    )

    external_math_closed = rows[0]["accepted_or_proved"] and rows[1]["accepted_or_proved"]
    author_dossier_complete = rows[3]["accepted_or_proved"]
    final_promotion_accepted = rows[5]["accepted_or_proved"]
    row_column_closed = external_math_closed and final_promotion_accepted
    only_remaining_gate = (
        external_math_closed
        and rows[2]["boundary_closed"]
        and author_dossier_complete
        and rows[4]["accepted_or_proved"]
        and not final_promotion_accepted
    )

    return {
        "certificate_type": "prime_matrix_final_single_gate_closure_decision_router",
        "status": (
            "external_kls_contract_row_column_closed_by_accepted_final_promotion"
            if row_column_closed
            else "final_single_gate_promotable_but_final_promotion_acceptance_required"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        },
        "external_contract": EXTERNAL_CONTRACT,
        "final_promotion_gate": PROMOTION_GATE,
        "external_math_inputs_closed": external_math_closed,
        "endpoint_no_hidden_math_route": rows[1]["accepted_or_proved"],
        "promotion_package_boundary_closed": rows[2]["boundary_closed"],
        "promotion_author_dossier_complete": author_dossier_complete,
        "final_promotion_input_explicitly_accepted": final_promotion_accepted,
        "only_remaining_gate": PROMOTION_GATE if only_remaining_gate else None,
        "row_column_unconditional_closed": row_column_closed,
        "strict_closure_basis": f"{EXTERNAL_CONTRACT} AND {PROMOTION_GATE}",
        "current_theorem_status": (
            "外部 KLS 合同版已在最终晋级门被接受后闭合。该闭合仍不是完全自足证明。"
            if row_column_closed
            else "当前材料已经把命题压到唯一最终晋级门；未显式接受该门前，仍只能声明条件闭合。"
        ),
        "conditional_theorem": (
            "若 AcceptFullSKLSExtExternalContract 与 "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance 均成立，"
            "则当前无隐藏终端图谱推出行/列命题闭合。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 最终单门闭合判定路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["current_theorem_status"],
        "",
        "```text",
        f"external_math_inputs_closed={fmt_bool(result['external_math_inputs_closed'])}",
        f"endpoint_no_hidden_math_route={fmt_bool(result['endpoint_no_hidden_math_route'])}",
        f"promotion_package_boundary_closed={fmt_bool(result['promotion_package_boundary_closed'])}",
        f"promotion_author_dossier_complete={fmt_bool(result['promotion_author_dossier_complete'])}",
        (
            "final_promotion_input_explicitly_accepted="
            f"{fmt_bool(result['final_promotion_input_explicitly_accepted'])}"
        ),
        f"only_remaining_gate={result['only_remaining_gate']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 严格闭合基",
        "",
        "```text",
        result["strict_closure_basis"],
        "```",
        "",
        "## 2. 当前可声明定理",
        "",
        result["conditional_theorem"],
        "",
        "## 3. 判定表",
        "",
        "| gate | boundary closed | accepted/proved | evidence | meaning | consequence |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{boundary}` | `{accepted}` | {evidence} | {meaning} | {consequence} |".format(
                gate=table_cell(item["gate"]),
                boundary=fmt_bool(item["boundary_closed"]),
                accepted=fmt_bool(item["accepted_or_proved"]),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                consequence=table_cell(item["consequence"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 结论",
            "",
            (
                "本路由已经把最后障碍压成一个不可再由作者侧路由消去的晋级门。"
                "若显式接受该晋级输入，则外部 KLS 合同版闭合；若要求完全自足，"
                "还必须把该晋级输入本身改写为独立审查级完整证明。"
            ),
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external-final-json", type=Path, default=DEFAULT_EXTERNAL_FINAL)
    parser.add_argument("--subgate-json", type=Path, default=DEFAULT_SUBGATE)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--line-ref", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--accept-final-promotion-input", action="store_true")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "external_final": args.external_final_json,
        "subgate": args.subgate_json,
        "promotion": args.promotion_json,
        "endpoint": args.endpoint_json,
        "line_ref": args.line_ref,
    }
    result = run(paths, args.accept_final_promotion_input)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["only_remaining_gate"])


if __name__ == "__main__":
    main()
