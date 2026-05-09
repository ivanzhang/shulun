#!/usr/bin/env python3
"""接受 FullS-KLS-ext 后的最终晋级状态路由器。

用法示例：
  python3 experiments/prime_matrix_external_kls_accepted_final_promotion_router.py

输出：
  docs/monograph/prime-matrix-external-kls-accepted-final-promotion-router.json
  docs/monograph/prime-matrix-external-kls-accepted-final-promotion-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_KLS_ACCEPTANCE = DOCS / "prime-matrix-fulls-kls-ext-acceptance-match-audit.json"
DEFAULT_PROMOTION = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_FRONTIER = DOCS / "prime-matrix-row-column-unconditional-frontier-router.json"
DEFAULT_ENDPOINT = DOCS / "prime-matrix-unconditional-closure-endpoint-verdict-router.json"
DEFAULT_FULL_RANKIN = DOCS / "prime-matrix-full-rankin-ledger-inventory-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-external-kls-accepted-final-promotion-router.json"
DEFAULT_MD = DOCS / "prime-matrix-external-kls-accepted-final-promotion-router.md"

EXTERNAL_CONTRACT = "AcceptFullSKLSExtExternalContract"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值写为小写文本。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def state_row(
    gate: str,
    closed: bool,
    accepted: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造最终晋级状态行。"""
    return {
        "gate": gate,
        "closed": closed,
        "accepted": accepted,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    kls: dict[str, Any],
    promotion: dict[str, Any],
    frontier: dict[str, Any],
    endpoint: dict[str, Any],
    full_rankin: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成接受外部 KLS 后的最终状态表。"""
    kls_accepted = (
        kls.get("strict_contract_match") is True
        and kls.get("accepted_as_external_blackbox_input") is True
        and kls.get("external_math_lane_closed_after_acceptance") is True
    )
    promotion_boundary = promotion.get("promotion_package_boundary_closed") is True
    promotion_accepted = promotion.get("promotion_package_independently_accepted") is True
    rankin_closed = (
        full_rankin.get("full_rankin_ledger_still_open_closed") is True
        and full_rankin.get("batch_rankin_pass_or_return_closed") is True
    )
    no_hidden_math_lane = (
        endpoint.get("endpoint_boundary_closed") is True
        and endpoint.get("row_column_unconditional_closed") is False
    )
    frontier_not_closed = frontier.get("row_column_unconditional_closed") is False

    return [
        state_row(
            gate="ExternalFullSKLSExtAccepted",
            closed=kls_accepted,
            accepted=kls_accepted,
            evidence=kls.get("status", "unknown"),
            meaning="FullS-KLS-ext 已按黑箱外部定理合同接受，且逐项匹配当前 non-AP full-S WFD 目标。",
            remaining="none on noncanonical full-S external math lane",
        ),
        state_row(
            gate="NoncanonicalFullSMathLaneClosed",
            closed=kls_accepted,
            accepted=kls_accepted,
            evidence=kls.get("accepted_external_basis", "unknown"),
            meaning="接受外部 KLS 后，noncanonical full-S 数学输入不再是开放硬点。",
            remaining=PROMOTION_GATE,
        ),
        state_row(
            gate="EndpointNoHiddenMathLane",
            closed=no_hidden_math_lane,
            accepted=no_hidden_math_lane,
            evidence=endpoint.get("status", "unknown"),
            meaning="终局边界已证明没有第四条未命名数学路线；剩余只能是已命名晋级门。",
            remaining=PROMOTION_GATE,
        ),
        state_row(
            gate="RankinSubledgerPassOrReturnClosed",
            closed=rankin_closed,
            accepted=rankin_closed,
            evidence=full_rankin.get("status", "unknown"),
            meaning="Rankin 子账本已闭合为全集清单与 pass-or-return 纪律。",
            remaining="independent acceptance of the whole promotion package",
        ),
        state_row(
            gate="DStructureTailLog4FiniteRankinBoundaryClosed",
            closed=promotion_boundary,
            accepted=promotion_accepted,
            evidence=promotion.get("status", "unknown"),
            meaning="DStructure/Tail-log4/finite verification/Rankin 晋级包边界已闭合。",
            remaining=(
                "none" if promotion_accepted else "independent acceptance, not author-side promotion"
            ),
        ),
        state_row(
            gate="NoAuthorSideUnconditionalUpgrade",
            closed=frontier_not_closed and not promotion_accepted,
            accepted=not promotion_accepted,
            evidence=frontier.get("status", "unknown"),
            meaning="当前材料明确禁止用作者侧路由替代独立晋级验收。",
            remaining=PROMOTION_GATE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行最终晋级状态路由。"""
    kls = load_json(paths["kls_acceptance"])
    promotion = load_json(paths["promotion"])
    frontier = load_json(paths["frontier"])
    endpoint = load_json(paths["endpoint"])
    full_rankin = load_json(paths["full_rankin"])
    rows = build_rows(kls, promotion, frontier, endpoint, full_rankin)

    external_math_closed = rows[1]["closed"] and rows[2]["closed"]
    promotion_accepted = promotion.get("promotion_package_independently_accepted") is True
    row_column_closed = external_math_closed and promotion_accepted

    return {
        "certificate_type": "prime_matrix_external_kls_accepted_final_promotion_router",
        "status": (
            "external_kls_math_lane_closed_final_promotion_gate_only_open"
            if external_math_closed and not promotion_accepted
            else "external_kls_and_promotion_accepted_row_column_closed"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{
                str(path.relative_to(ROOT)): file_sha256(path)
                for path in paths.values()
            },
        },
        "external_fulls_kls_accepted": rows[0]["accepted"],
        "noncanonical_fulls_external_math_lane_closed": external_math_closed,
        "rankin_subledger_pass_or_return_closed": rows[3]["closed"],
        "promotion_package_boundary_closed": promotion.get("promotion_package_boundary_closed") is True,
        "promotion_package_independently_accepted": promotion_accepted,
        "all_math_inputs_closed_after_external_acceptance": external_math_closed,
        "remaining_single_gate_after_external_acceptance": (
            None if promotion_accepted else PROMOTION_GATE
        ),
        "conditional_final_basis": f"{EXTERNAL_CONTRACT} AND {PROMOTION_GATE}",
        "row_column_unconditional_closed": row_column_closed,
        "rows": rows,
        "plain_conclusion": (
            "接受 FullS-KLS-ext 后，noncanonical full-S 外部数学线已经闭合；"
            "Rankin 子账本也已闭合为 pass-or-return。当前唯一剩余是 "
            "DStructure/Tail-log4/finite verification/Rankin 整体晋级包的独立接受。"
            "该门未接受前，不能诚实声明完整行/列无条件定理；若该门被独立接受，"
            "则在外部 KLS 合同版中命题闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 接受外部 KLS 后的最终晋级路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"external_fulls_kls_accepted={fmt_bool(result['external_fulls_kls_accepted'])}",
        (
            "noncanonical_fulls_external_math_lane_closed="
            f"{fmt_bool(result['noncanonical_fulls_external_math_lane_closed'])}"
        ),
        (
            "rankin_subledger_pass_or_return_closed="
            f"{fmt_bool(result['rankin_subledger_pass_or_return_closed'])}"
        ),
        (
            "promotion_package_boundary_closed="
            f"{fmt_bool(result['promotion_package_boundary_closed'])}"
        ),
        (
            "promotion_package_independently_accepted="
            f"{fmt_bool(result['promotion_package_independently_accepted'])}"
        ),
        (
            "all_math_inputs_closed_after_external_acceptance="
            f"{fmt_bool(result['all_math_inputs_closed_after_external_acceptance'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 条件终局输入基",
        "",
        "```text",
        result["conditional_final_basis"],
        "```",
        "",
        "## 2. 接受后唯一剩余",
        "",
    ]
    if result["remaining_single_gate_after_external_acceptance"]:
        lines.append(f"- `{result['remaining_single_gate_after_external_acceptance']}`")
    else:
        lines.append("- 无。")
    lines.extend(
        [
            "",
            "## 3. 最终状态表",
            "",
            "| gate | closed | accepted | evidence | meaning | remaining |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{accepted}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                accepted=fmt_bool(row["accepted"]),
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
            "外部 KLS 合同版的数学输入已经闭合。当前不能再把目标在数学输入之间来回转换；"
            "唯一剩余是最终晋级验收门。若该门被独立接受，外部 KLS 版本即可升级为完整行/列命题闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kls-acceptance-json", type=Path, default=DEFAULT_KLS_ACCEPTANCE)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--frontier-json", type=Path, default=DEFAULT_FRONTIER)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--full-rankin-json", type=Path, default=DEFAULT_FULL_RANKIN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "kls_acceptance": args.kls_acceptance_json,
        "promotion": args.promotion_json,
        "frontier": args.frontier_json,
        "endpoint": args.endpoint_json,
        "full_rankin": args.full_rankin_json,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["remaining_single_gate_after_external_acceptance"])


if __name__ == "__main__":
    main()
