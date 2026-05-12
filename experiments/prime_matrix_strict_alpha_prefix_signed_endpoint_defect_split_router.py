#!/usr/bin/env python3
"""生成 strict alpha-prefix 有符号端点缺陷分裂路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_prefix_signed_endpoint_defect_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-prefix-signed-endpoint-defect-split-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-alpha-prefix-signed-endpoint-defect-split-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-alpha-prefix-signed-endpoint-defect-split-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-alpha-prefix-load-deficit-pdec-router.md",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-dyadic-pdec-certificate.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-highdyadic-endpoint-lock.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-hdl-coreload-identity.md",
]

SIGNED_DEFECT = "AlphaPrefixSignedEndpointDefect"
DYADIC_PDEC = "DyadicLowerWeightEndpointPDECExclusion"
FAR_TAIL = "LowerWeightFarTailCoreOrSAEExclusion"
LOW_MOD = "LowModSignedEndpointDefectExclusion"
MAIN_GAP = "AlphaLowerWeightMainGapPositiveAgainstHighLabelCapacity"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def implications() -> list[dict[str, str]]:
    """列出闭合的有符号缺陷蕴含。"""
    return [
        {
            "name": "lower_weight_exact_endpoint_sum",
            "formula": "L_alpha(x)=sum_d lambda_d^- A_d(x)=(P-1)W_alpha^-+E_alpha(x), E_alpha=sum_d lambda_d^- epsilon_d(x).",
            "status": "closed",
            "meaning": "把粗筛 lower sum 精确拆成主项和有符号端点误差。",
        },
        {
            "name": "capacity_forces_negative_endpoint",
            "formula": "If EarlyZeroRow and G_alpha=(P-1)W_alpha^- - C_alpha(P)>0, then E_alpha(x)<=-G_alpha.",
            "status": "closed_implication",
            "meaning": "这是比 TV 大更强的同向负端点缺陷。",
        },
        {
            "name": "low_middle_far_split",
            "formula": "E_alpha=E_low(D0)+sum_j E_{I_j}+E_far(D1).",
            "status": "closed_identity",
            "meaning": "缺陷可以按低模、中间 dyadic 块、远尾 core 精确分裂。",
        },
        {
            "name": "dyadic_pigeonhole",
            "formula": "If E_alpha<=-G, E_low>-eta0 G, E_far>-eta1 G, then some middle block E_I<=-(1-eta0-eta1)G/J.",
            "status": "closed_implication",
            "meaning": "强缺陷不能无形分散；不是低模/远尾承担，就必有 dyadic PDEC 证书。",
        },
        {
            "name": "high_dyadic_lock_import",
            "formula": "When the defect block has d>P-1, each modulus has at most one endpoint hit.",
            "status": "imported_closed",
            "meaning": "高块缺陷进一步变成 HDL-9/HDL-10 型端点命中偏斜。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行假设下推出有符号缺陷。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "SignedEndpointDefectForced",
            "closed": True,
            "proved": True,
            "meaning": "若 lower-weight 主项超过高标签容量，早期零行强制 E_alpha<=-G_alpha。",
            "remaining": MAIN_GAP,
        },
        {
            "gate": "DyadicSplitClosed",
            "closed": True,
            "proved": True,
            "meaning": "强负缺陷若不由低模或远尾承担，必落入某个中间 dyadic 块。",
            "remaining": f"{LOW_MOD} OR {DYADIC_PDEC} OR {FAR_TAIL}",
        },
        {
            "gate": "HighDyadicEndpointLockImported",
            "closed": True,
            "proved": True,
            "meaning": "高块 `d>P-1` 时端点误差是单命中 CRT 偏斜，可接 HDL/CoreLoad。",
            "remaining": "HDL-9/HDL-10 energy exclusion",
        },
        {
            "gate": "SignedEndpointDefectExcludedCurrentCorpus",
            "closed": False,
            "proved": False,
            "meaning": "低模、dyadic PDEC、远尾 core 三出口尚未全部排斥。",
            "remaining": f"{LOW_MOD} AND {DYADIC_PDEC} AND {FAR_TAIL}",
        },
        {
            "gate": "RowColumnClosed",
            "closed": False,
            "proved": False,
            "meaning": "当前只得到精确缺陷显化，不得到无条件闭合。",
            "remaining": f"{MAIN_GAP} plus exclusion of {LOW_MOD}/{DYADIC_PDEC}/{FAR_TAIL}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_alpha_prefix_signed_endpoint_defect_split_router",
        "status": "signed_endpoint_defect_forced_and_split_low_dyadic_far_tail_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "signed_endpoint_defect_forced": True,
        "low_middle_far_split_closed": True,
        "dyadic_pigeonhole_closed": True,
        "high_dyadic_endpoint_lock_imported": True,
        "signed_endpoint_defect_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": DYADIC_PDEC,
        "parallel_targets": [LOW_MOD, FAR_TAIL, MAIN_GAP],
        "implications": implications(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "上一层的 TV 缺陷可以加强为有符号端点缺陷：lower-weight 和 "
            "L_alpha=(P-1)W^-_alpha+E_alpha 精确成立；若早期零行又要求 "
            "R_alpha 不超过高标签容量 C_alpha，而主项间隙 G_alpha=(P-1)W^-_alpha-C_alpha 为正，"
            "则必须有 E_alpha<=-G_alpha。随后按低模、中间 dyadic、远尾 core 分裂，"
            "若低模和远尾不能承担固定比例负缺陷，就得到某个 dyadic 块上的 PDEC 证书。"
            "这仍是缺陷显化，不是缺陷排斥。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict alpha-prefix 有符号端点缺陷分裂路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_endpoint_defect_forced={fmt_bool(result['signed_endpoint_defect_forced'])}",
        f"low_middle_far_split_closed={fmt_bool(result['low_middle_far_split_closed'])}",
        f"dyadic_pigeonhole_closed={fmt_bool(result['dyadic_pigeonhole_closed'])}",
        f"high_dyadic_endpoint_lock_imported={fmt_bool(result['high_dyadic_endpoint_lock_imported'])}",
        f"signed_endpoint_defect_excluded={fmt_bool(result['signed_endpoint_defect_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有符号缺陷公式",
        "",
        "令",
        "",
        "```text",
        "L_alpha(x)=sum_d lambda_d^- A_d(x),",
        "A_d(x)=(P-1)/d + epsilon_d(x).",
        "```",
        "",
        "则",
        "",
        "```text",
        "L_alpha(x)=(P-1)W_alpha^- + E_alpha(x),",
        "E_alpha(x)=sum_d lambda_d^- epsilon_d(x).",
        "```",
        "",
        "若早期零行成立，则 `L_alpha(x)<=R_alpha(x)<=C_alpha(P)`。因此一旦",
        "",
        "```text",
        "G_alpha=(P-1)W_alpha^- - C_alpha(P)>0,",
        "```",
        "",
        "就强制",
        "",
        "```text",
        "E_alpha(x)<=-G_alpha.",
        "```",
        "",
        "这不是普通误差上界问题，而是有方向的端点 CRT 缺陷。",
        "",
        "## 2. 闭合蕴含",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["implications"]:
        lines.append(
            "| `{name}` | {formula} | `{status}` | {meaning} |".format(
                name=table_cell(row["name"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新最窄输入",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步只把强缺陷从抽象 TV 压成有符号端点 PDEC/远尾 core 出口；尚未排斥这些出口。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
