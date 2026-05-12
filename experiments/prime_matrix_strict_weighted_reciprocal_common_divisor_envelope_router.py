#!/usr/bin/env python3
"""生成 strict 加权共同因子倒数封套路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_weighted_reciprocal_common_divisor_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.md",
    MONOGRAPH / "prime-matrix-beta-sieve-self-contained-frontier-router.md",
    MONOGRAPH / "prime-matrix-beta-sieve-lower-weight-recursion-router.md",
    MONOGRAPH / "prime-matrix-strict-high-tail-corpus-reconciliation-router.md",
]

RECIP_ENV = "WeightedReciprocalCommonDivisorEnvelopeForLowEffectiveSpectrum"
WINDOW_DIVISOR = "WindowedReciprocalDivisorEnvelopeForFrequencyH"
HOT_WINDOW = "HotFrequencyDivisorWindowAnomalyPDECorSAE"
LOW_QUOTIENT = "LowQuotientColumnCRTOrPDECRoute"
PDEC_LOWER = "WeightedPositiveEndpointPDECLowerBoundComparison"


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


def envelopes() -> list[dict[str, str]]:
    """列出倒数封套。"""
    return [
        {
            "name": "positive_weight_pointwise_bound",
            "formula": "0<=w_d^+<=1 for finite lower weights lambda_d^{low} in {-1,0,1}.",
            "status": "imported_closed",
            "meaning": "正权部分不能超过 1；这是有限 lower-weight 递归的点态结果。",
        },
        {
            "name": "exact_windowed_reciprocal_envelope",
            "formula": "LowEff_R(h)<=1/2 sum_{2<=s<=R} sum_{g|h, B/s<g<=2B/s} 1/g.",
            "status": "closed",
            "meaning": "dyadic 条件 d in (B,2B] 把 g 限在短乘法窗口。",
        },
        {
            "name": "divisor_count_envelope",
            "formula": "sum_{g|h, B/s<g<=2B/s} 1/g <= (s/B) N_h(B/s,2B/s].",
            "status": "closed",
            "meaning": "若只知道 divisor 个数，也得到窗口计数封套。",
        },
        {
            "name": "sigma_minus_one_global_envelope",
            "formula": "LowEff_R(h)<=((R-1)/2) sigma_{-1}(h).",
            "status": "closed_but_weak",
            "meaning": "全局倒数因子和是安全粗上界；通常太弱，只作兜底。",
        },
        {
            "name": "hot_window_pigeonhole",
            "formula": "If LowEff_R(h)>Xi, then some s has sum_{g|h, B/s<g<=2B/s}1/g >= 2Xi/(R-1).",
            "status": "closed_implication",
            "meaning": "低有效模失败会物化为某条小商线上的热频率因子窗口。",
        },
        {
            "name": "hot_window_route",
            "formula": "Persistent hot windows are PDEC/ColumnCRT; isolated hot windows are SAE.",
            "status": "registered_route",
            "meaning": "倒数封套失败不是自由出口。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的低有效模出口内部。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "PointwiseWeightBoundImported",
            "closed": True,
            "proved": True,
            "meaning": "lower-weight 正部满足点态 <=1。",
            "remaining": "无。",
        },
        {
            "gate": "WindowedReciprocalEnvelopeClosed",
            "closed": True,
            "proved": True,
            "meaning": "共同因子倒数和已压成 h 的短窗口除数倒数和。",
            "remaining": WINDOW_DIVISOR,
        },
        {
            "gate": "HotWindowPigeonholeClosed",
            "closed": True,
            "proved": True,
            "meaning": "封套若仍过大，某个小商 s 的热窗口必须显化。",
            "remaining": HOT_WINDOW,
        },
        {
            "gate": "ReciprocalEnvelopeBeatsPDECLowerBoundCurrentCorpus",
            "closed": False,
            "proved": False,
            "meaning": "尚未把窗口除数封套与 PDEC 下界完成常数比较。",
            "remaining": f"{WINDOW_DIVISOR} AND {PDEC_LOWER}",
        },
        {
            "gate": "HotWindowExcludedCurrentCorpus",
            "closed": False,
            "proved": False,
            "meaning": "尚未排斥持久热窗口 PDEC/ColumnCRT 或孤立 SAE。",
            "remaining": f"{HOT_WINDOW} AND {LOW_QUOTIENT}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_weighted_reciprocal_common_divisor_envelope_router",
        "status": "weighted_reciprocal_common_divisor_envelope_reduced_to_windowed_divisor_hot_window_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "pointwise_weight_bound_imported": True,
        "windowed_reciprocal_envelope_closed": True,
        "hot_window_pigeonhole_closed": True,
        "reciprocal_envelope_beats_pdec_lower_bound": False,
        "hot_window_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": WINDOW_DIVISOR,
        "parallel_targets": [PDEC_LOWER, HOT_WINDOW, LOW_QUOTIENT],
        "envelopes": envelopes(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "共同因子倒数和已被压成完全初等的短窗口除数封套。由于 positive lower-weight "
            "点态不超过 1，低有效模贡献至多为 "
            "1/2 * sum_{2<=s<=R} sum_{g|h, B/s<g<=2B/s} 1/g。"
            "若该封套小于 PDEC 下界，低有效模出口被排除；若不小，鸽巢原理强制某个小商 s "
            "出现热频率因子窗口，持久时进入 PDEC/ColumnCRT，孤立时进入 SAE。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 加权共同因子倒数封套路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pointwise_weight_bound_imported={fmt_bool(result['pointwise_weight_bound_imported'])}",
        f"windowed_reciprocal_envelope_closed={fmt_bool(result['windowed_reciprocal_envelope_closed'])}",
        f"hot_window_pigeonhole_closed={fmt_bool(result['hot_window_pigeonhole_closed'])}",
        f"reciprocal_envelope_beats_pdec_lower_bound={fmt_bool(result['reciprocal_envelope_beats_pdec_lower_bound'])}",
        f"hot_window_excluded={fmt_bool(result['hot_window_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 窗口除数封套",
        "",
        "在 dyadic 块 `d in (B,2B]` 中，低有效模已经写成 `d=s g`、`g|h`、`2<=s<=R`。因此",
        "",
        "```text",
        "B/s < g <= 2B/s.",
        "```",
        "",
        "又因正权点态不超过 1，得到",
        "",
        "```text",
        "LowEff_R(h) <= 1/2 sum_{2<=s<=R} sum_{g|h, B/s<g<=2B/s} 1/g.",
        "```",
        "",
        "所以当前问题已变成频率 `h` 的短乘法窗口除数倒数和问题。",
        "",
        "## 2. 封套表",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["envelopes"]:
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
            "审稿边界：本步闭合短窗口除数封套与热窗口显化；尚未证明封套常数足够小，也未排斥热窗口出口。",
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
