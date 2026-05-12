#!/usr/bin/env python3
"""生成 strict 加权 dyadic endpoint PDEC 到 HDL/CoreLoad 的路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_weighted_dyadic_endpoint_pdec_hdl_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-weighted-dyadic-endpoint-pdec-hdl-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-weighted-dyadic-endpoint-pdec-hdl-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-weighted-dyadic-endpoint-pdec-hdl-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-alpha-prefix-signed-endpoint-defect-split-router.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-highdyadic-endpoint-lock.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-hdl-coreload-identity.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-hcl-cofactor-inversion.md",
]

WEIGHTED_HDL = "WeightedDyadicEndpointHDLCoreLoadExclusion"
WEIGHTED_PLUS_DEFICIT = "WeightedPositiveEndpointHitDeficitPDEC"
WEIGHTED_MINUS_SURPLUS = "WeightedNegativeEndpointHitSurplusCoreLoad"
WEIGHTED_COFACTOR = "WeightedCofactorLoadCapacityOrColumnCRT"
LOW_MIDDLE = "LowOrMiddleDyadicEndpointPDECExclusion"
FAR_TAIL = "LowerWeightFarTailCoreOrSAEExclusion"
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
    """列出加权 HDL 接桥蕴含。"""
    return [
        {
            "name": "weighted_endpoint_block",
            "formula": "E_I(x)=sum_{d in I} lambda_d^- epsilon_d(x), epsilon_d=A_d-(P-1)/d.",
            "status": "closed_definition",
            "meaning": "当前链使用 lower-weight，而不是 Möbius 裸权重。",
        },
        {
            "name": "positive_negative_weight_split",
            "formula": "lambda_d^{low}=w_d^+ - w_d^-, with w_d^+,w_d^- >=0; E_I=(A_I^+-H R_I^+) - (A_I^--H R_I^-).",
            "status": "closed_identity",
            "meaning": "任何负缺陷都可拆成正权端点亏损或负权端点过剩。",
        },
        {
            "name": "weighted_hdl_dichotomy",
            "formula": "If E_I<=-tau, then A_I^+<=H R_I^+-tau/2 or A_I^->=H R_I^-+tau/2.",
            "status": "closed_implication",
            "meaning": "这是 HDL-9/HDL-10 的 lower-weight 加权版本。",
        },
        {
            "name": "high_block_single_hit",
            "formula": "If d>H=P-1, then A_d(x)=1_{rho_d(x)<=H}.",
            "status": "closed_imported",
            "meaning": "高 dyadic 块中每个模数最多命中一次，端点缺陷变成单命中偏斜。",
        },
        {
            "name": "weighted_coreload_identity",
            "formula": "A_I^sigma=sum_{k<=H} sum_{d in I,d|G_z(k)} w_d^sigma.",
            "status": "closed_identity",
            "meaning": "加权端点命中偏斜等价于逐列低素 squarefree 核的加权负载异常。",
        },
        {
            "name": "weighted_cofactor_inversion",
            "formula": "For d>H, d|xP+c and m=(xP+c)/d imply m<P+2; weighted load projects to low cofactor band.",
            "status": "closed_implication",
            "meaning": "奇/负权过剩若不集中为列锚，就必须在低互补因子带分布。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链中处理 dyadic 负端点缺陷。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "WeightedHDLBridgeClosed",
            "closed": True,
            "proved": True,
            "meaning": "Möbius HDL 已升级为 lower-weight 加权 HDL，避免权重口径偷换。",
            "remaining": WEIGHTED_HDL,
        },
        {
            "gate": "HighBlockSingleHitCoreLoadClosed",
            "closed": True,
            "proved": True,
            "meaning": "高块缺陷可精确改写为加权逐列 coreload 异常。",
            "remaining": f"{WEIGHTED_PLUS_DEFICIT} OR {WEIGHTED_MINUS_SURPLUS}",
        },
        {
            "gate": "WeightedCofactorBandProjectionClosed",
            "closed": True,
            "proved": True,
            "meaning": "过剩分支投影到 m<P+2 的互补因子带；单 m 容量仍受一个剩余类限制。",
            "remaining": WEIGHTED_COFACTOR,
        },
        {
            "gate": "DyadicEndpointPDECExcludedCurrentCorpus",
            "closed": False,
            "proved": False,
            "meaning": "加权 HDL/CoreLoad 接桥闭合，但正权亏损、负权过剩和低/中块 PDEC 尚未排斥。",
            "remaining": f"{LOW_MIDDLE} AND {WEIGHTED_PLUS_DEFICIT} AND {WEIGHTED_MINUS_SURPLUS}",
        },
        {
            "gate": "RowColumnClosed",
            "closed": False,
            "proved": False,
            "meaning": "当前只把 dyadic PDEC 压到加权 HDL/CoreLoad/互补因子出口。",
            "remaining": f"{MAIN_GAP} AND {LOW_MIDDLE} AND {WEIGHTED_HDL} AND {FAR_TAIL}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_weighted_dyadic_endpoint_pdec_hdl_router",
        "status": "weighted_dyadic_endpoint_pdec_reduced_to_hdl_coreload_cofactor_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "weighted_hdl_bridge_closed": True,
        "high_block_single_hit_coreload_closed": True,
        "weighted_cofactor_band_projection_closed": True,
        "dyadic_endpoint_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": WEIGHTED_PLUS_DEFICIT,
        "parallel_targets": [WEIGHTED_MINUS_SURPLUS, WEIGHTED_COFACTOR, LOW_MIDDLE, FAR_TAIL, MAIN_GAP],
        "implications": implications(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前 alpha-prefix 链的 dyadic 端点缺陷带有 Rosser-Iwaniec lower-weight 权重，"
            "不能直接套用旧的 Möbius HDL。本文把 HDL-9/HDL-10 升级为加权形式："
            "若某个 dyadic 块有 E_I<=-tau，则要么正权端点命中亏损，"
            "要么负权端点命中过剩。若该块在 d>P-1 的高区间，端点命中是单命中 CRT 事件，"
            "并精确等价于逐列低素核的加权 coreload 异常；过剩分支还可反演到 m<P+2 的低互补因子带。"
            "本步关闭权重口径和结构接桥，但尚未排斥这些加权异常。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 加权 dyadic endpoint PDEC 到 HDL/CoreLoad 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"weighted_hdl_bridge_closed={fmt_bool(result['weighted_hdl_bridge_closed'])}",
        f"high_block_single_hit_coreload_closed={fmt_bool(result['high_block_single_hit_coreload_closed'])}",
        f"weighted_cofactor_band_projection_closed={fmt_bool(result['weighted_cofactor_band_projection_closed'])}",
        f"dyadic_endpoint_pdec_excluded={fmt_bool(result['dyadic_endpoint_pdec_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 加权 HDL 口径",
        "",
        "对 dyadic 块 `I`，当前端点误差是",
        "",
        "```text",
        "E_I(x)=sum_{d in I} lambda_d^- epsilon_d(x),",
        "epsilon_d(x)=A_d(x)-(P-1)/d.",
        "```",
        "",
        "把权重拆成正负部分后，若 `E_I<=-tau`，则必有",
        "",
        "```text",
        "A_I^+ <= H R_I^+ - tau/2",
        "或",
        "A_I^- >= H R_I^- + tau/2.",
        "```",
        "",
        "这就是 HDL 端点亏损/过剩的 lower-weight 加权版本。",
        "",
        "## 2. 闭合接桥",
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
            "审稿边界：本步闭合的是 weighted endpoint PDEC 到 HDL/CoreLoad/cofactor 的结构接桥；没有证明这些加权异常不可能。",
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
