#!/usr/bin/env python3
"""生成 strict Schoenfeld/Dusart psi 误差表内化路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_schoenfeld_dusart_psi_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-schoenfeld-dusart-psi-table-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-schoenfeld-dusart-psi-table-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-schoenfeld-dusart-psi-table-router.md"

RH_GUARD = MONOGRAPH / "prime-matrix-strict-sqrt-kernel-rh-guard-router.json"
ANALYTIC_SPLICE = MONOGRAPH / "prime-matrix-strict-dusart-analytic-kernel-threshold-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [RH_GUARD, ANALYTIC_SPLICE, CLAIM_STATUS]

TARGET = "SchoenfeldDusartPsiEpsilonTableInternalizationLedger"
HIGH_TABLE = "PsiEpsilonHighTailB28TableCertificate"
MIDDLE_TABLE = "PsiUpperMiddle8e11ToE28TableCertificate"
PSI_THETA = "PsiMinusThetaLowerGap09999SqrtSelfContainedLedger"
THETA_FINITE = "ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger"
TABLE_GENERATOR = "SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger"
ZERO_INPUT = "VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger"
ROUNDING_AUDIT = "DusartP51TableRoundingMarginAuditLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

DUSART_URL = "https://arxiv.org/abs/1002.0442"
SCHOENFELD_URL = "https://www.ams.org/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf"

TARGET_RELATIVE = 1.0 / 36260.0
EPS_HIGH = 0.00002224
EPS_MIDDLE = 0.00002841
GAP_RELATIVE = 0.9999 * math.exp(-14.0)
MIDDLE_RESULT = EPS_MIDDLE - GAP_RELATIVE
HIGH_MARGIN = TARGET_RELATIVE - EPS_HIGH
MIDDLE_MARGIN = TARGET_RELATIVE - MIDDLE_RESULT


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


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


def table_value_rows() -> list[dict[str, Any]]:
    """列出 P5.1 需要的表值和余量。"""
    return [
        {
            "input": HIGH_TABLE,
            "claim": "psi(x)-x <= 0.00002224 x for x>=e^28",
            "used_for": "high tail",
            "margin": HIGH_MARGIN,
            "closed": False,
        },
        {
            "input": MIDDLE_TABLE,
            "claim": "psi(x) < 1.00002841 x for 8e11<=x<=e^28",
            "used_for": "middle strip before subtracting psi-theta",
            "margin": MIDDLE_MARGIN,
            "closed": False,
        },
        {
            "input": PSI_THETA,
            "claim": "psi(x)-theta(x)>0.9999 sqrt(x) on the middle strip",
            "used_for": "middle strip subtraction",
            "margin": MIDDLE_MARGIN,
            "closed": False,
        },
        {
            "input": THETA_FINITE,
            "claim": "theta(x)<x for x<=8e11",
            "used_for": "finite left range",
            "margin": float("nan"),
            "closed": False,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 Schoenfeld/Dusart psi 表内化路由证书。"""
    guard = load_json(RH_GUARD)
    splice = load_json(ANALYTIC_SPLICE)
    active = guard.get("next_direct_attack_target") == TARGET
    arithmetic_splice_ready = splice.get("dusart_analytic_kernel_threshold_arithmetic_splice_closed") is True
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            guard.get("counterexample_assumption_only") is True and guard.get("row_column_unconditional_closed") is False,
            True,
            "本步只内化无条件 psi 表输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "UnconditionalPsiTableGateActive",
            active,
            True,
            "平方根核已被标记为 RH-level，故无条件主线回到 Schoenfeld/Dusart 显式 psi 表。",
            TARGET,
        ),
        row(
            "P51ArithmeticSpliceAlreadyReady",
            arithmetic_splice_ready,
            True,
            "Dusart P5.1 的拼接算术已经完成，剩余是表值本身和证明来源。",
            ROUNDING_AUDIT,
        ),
        row(
            "HighTailTableValueNeeded",
            False,
            False,
            "需要作者侧证明或可复算证书给出 eps_psi(28)<=0.00002224。",
            f"{TABLE_GENERATOR} AND {ZERO_INPUT}",
        ),
        row(
            "MiddlePsiUpperTableNeeded",
            False,
            False,
            "需要证明 8e11<=x<=e^28 上 psi(x)<1.00002841x；该常数因中段余量很薄，不能粗化。",
            f"{TABLE_GENERATOR} AND {ZERO_INPUT}",
        ),
        row(
            "PsiThetaGapNeeded",
            False,
            False,
            "中段还必须内化 psi-theta>0.9999sqrt(x)，否则 0.00002841 不能降到 1/36260 以下。",
            PSI_THETA,
        ),
        row(
            "ThetaFiniteTableTo8e11Needed",
            False,
            False,
            "仓库只有 x<=20000 的有限 theta 桥；Dusart P5.1 左段需要 theta(x)<x 到 8e11。",
            THETA_FINITE,
        ),
        row(
            "RoundingMarginAuditActive",
            MIDDLE_MARGIN > 0 and HIGH_MARGIN > 0,
            True,
            "高尾余量约 5.34e-6，中段余量仅约 4.46e-11；表值必须保留足够有效数字和舍入方向。",
            ROUNDING_AUDIT,
        ),
        row(
            TARGET,
            False,
            False,
            "Schoenfeld/Dusart psi 表尚未作者侧自足内化；当前只完成了责任拆包与余量审查。",
            f"{HIGH_TABLE} AND {MIDDLE_TABLE} AND {PSI_THETA} AND {THETA_FINITE} AND {ROUNDING_AUDIT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "psi 表内化拆包不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_schoenfeld_dusart_psi_table_router",
        "status": "schoenfeld_dusart_psi_table_internalization_split_into_four_table_inputs",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "schoenfeld_dusart_psi_table_self_contained_closed": False,
        "p51_arithmetic_splice_ready": arithmetic_splice_ready,
        "table_rounding_margin_audit_closed": MIDDLE_MARGIN > 0 and HIGH_MARGIN > 0,
        "high_tail_eps_table_closed": False,
        "middle_psi_upper_table_closed": False,
        "psi_theta_gap_self_contained_closed": False,
        "theta_less_than_identity_to_8e11_closed": False,
        "direct_internal_dusart_theta_pnt_envelope_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "table_values": table_value_rows(),
        "diagnostics": {
            "target_relative_1_over_36260": TARGET_RELATIVE,
            "eps_high_28": EPS_HIGH,
            "high_margin": HIGH_MARGIN,
            "eps_middle_raw": EPS_MIDDLE,
            "psi_theta_gap_at_e28": GAP_RELATIVE,
            "middle_result_relative": MIDDLE_RESULT,
            "middle_margin": MIDDLE_MARGIN,
        },
        "external_references": [
            {
                "id": "Dusart arXiv:1002.0442",
                "url": DUSART_URL,
                "role": "source boundary for Proposition 5.1 and the epsilon/table values",
            },
            {
                "id": "Schoenfeld 1976 Math. Comput. 30(134)",
                "url": SCHOENFELD_URL,
                "role": "source boundary for classical Chebyshev-function estimates used by the table lineage",
            },
        ],
        "replacement_self_contained": {
            TARGET: f"{HIGH_TABLE} AND {MIDDLE_TABLE} AND {PSI_THETA} AND {THETA_FINITE} AND {ROUNDING_AUDIT}",
            HIGH_TABLE: f"{TABLE_GENERATOR} AND {ZERO_INPUT}",
            MIDDLE_TABLE: f"{TABLE_GENERATOR} AND {ZERO_INPUT}",
        },
        "next_direct_attack_target": TABLE_GENERATOR,
        "parallel_attack_targets": [ZERO_INPUT, PSI_THETA, THETA_FINITE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "无条件高尾路线已回到 Schoenfeld/Dusart 显式 psi 表。P5.1 需要四类作者侧输入："
            "`eps_psi(28)<=0.00002224`、`8e11<=x<=e^28` 的 `psi<1.00002841x`、"
            "`psi-theta>0.9999sqrt(x)`、以及 `theta(x)<x` 到 `8e11` 的有限表。"
            "其中中段拼接余量只有约 `4.46e-11`，因此表值生成器和舍入方向必须单独验收。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    d = result["diagnostics"]
    lines = [
        "# Prime Matrix strict Schoenfeld/Dusart psi 表内化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"schoenfeld_dusart_psi_table_self_contained_closed={fmt_bool(result['schoenfeld_dusart_psi_table_self_contained_closed'])}",
        f"p51_arithmetic_splice_ready={fmt_bool(result['p51_arithmetic_splice_ready'])}",
        f"table_rounding_margin_audit_closed={fmt_bool(result['table_rounding_margin_audit_closed'])}",
        f"high_tail_eps_table_closed={fmt_bool(result['high_tail_eps_table_closed'])}",
        f"middle_psi_upper_table_closed={fmt_bool(result['middle_psi_upper_table_closed'])}",
        f"psi_theta_gap_self_contained_closed={fmt_bool(result['psi_theta_gap_self_contained_closed'])}",
        f"theta_less_than_identity_to_8e11_closed={fmt_bool(result['theta_less_than_identity_to_8e11_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 表值责任",
        "",
        "| input | claim | used for | margin | closed |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for item in result["table_values"]:
        margin = "n/a" if math.isnan(item["margin"]) else f"{item['margin']:.12e}"
        lines.append(
            f"| `{table_cell(item['input'])}` | {table_cell(item['claim'])} | "
            f"{table_cell(item['used_for'])} | `{margin}` | `{fmt_bool(item['closed'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 拼接余量",
            "",
            "| item | value |",
            "| --- | ---: |",
            f"| target relative `1/36260` | `{d['target_relative_1_over_36260']:.12e}` |",
            f"| eps high b=28 | `{d['eps_high_28']:.12e}` |",
            f"| high margin | `{d['high_margin']:.12e}` |",
            f"| middle raw psi upper | `{d['eps_middle_raw']:.12e}` |",
            f"| middle psi-theta gap at e^28 | `{d['psi_theta_gap_at_e28']:.12e}` |",
            f"| middle result relative | `{d['middle_result_relative']:.12e}` |",
            f"| middle margin | `{d['middle_margin']:.12e}` |",
            "",
            "## 3. 外部边界",
            "",
        ]
    )
    for ref in result["external_references"]:
        lines.append(f"- `{ref['id']}`：{ref['url']}；{ref['role']}")
    lines.extend(["", "## 4. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 5. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 6. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
