#!/usr/bin/env python3
"""生成 strict 短窗口倒数除数密度路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_windowed_reciprocal_divisor_density_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-windowed-reciprocal-divisor-density-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.md",
    MONOGRAPH / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.md",
    MONOGRAPH / "h5-4-ospc-weighted-crtdefect-absorption.md",
]

WINDOW_DIVISOR = "WindowedReciprocalDivisorEnvelopeForFrequencyH"
SHORT_DENSITY = "ShortWindowDivisorDensityEnvelopeForFrequencyH"
HOT_DENSITY = "HotFrequencyDivisorDensityPDECorSAE"
PDEC_COMPARE = "WeightedPositiveEndpointPDECLowerBoundComparison"
LOW_QUOTIENT = "LowQuotientColumnCRTOrPDECRoute"


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


def lemmas() -> list[dict[str, str]]:
    """列出窗口除数密度引理。"""
    return [
        {
            "name": "reciprocal_to_count",
            "formula": "For Y<g<=2Y, sum_{g|h}1/g <= N_h(Y,2Y]/Y.",
            "status": "closed",
            "meaning": "倒数封套由短窗口除数个数控制。",
        },
        {
            "name": "count_threshold",
            "formula": "If sum_{g|h,Y<g<=2Y}1/g >= eta, then N_h(Y,2Y] >= eta Y.",
            "status": "closed",
            "meaning": "倒数和过大强制频率 h 在该短窗口内有线性多除数。",
        },
        {
            "name": "multi_s_threshold",
            "formula": "LowEff_R(h)>Xi implies some s has N_h(B/s,2B/s] >= (2Xi/(R-1))(B/s).",
            "status": "closed_implication",
            "meaning": "低有效失败等价于某条小商线上的短窗口除数密度异常。",
        },
        {
            "name": "density_to_structural_defect",
            "formula": "Many divisors g of h in one short multiplicative window give a hot frequency divisor-density certificate.",
            "status": "registered_route",
            "meaning": "该证书持久出现是 PDEC/ColumnCRT，孤立出现是 SAE。",
        },
        {
            "name": "no_free_global_divisor_bound",
            "formula": "A generic tau(h) bound alone is insufficient unless compared with the actual PDEC lower threshold.",
            "status": "discipline_closed",
            "meaning": "防止用无参数除数函数估计偷关当前缺口。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的低有效模封套内部。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "ReciprocalToDivisorCountClosed",
            "closed": True,
            "proved": True,
            "meaning": "窗口倒数和已经转成短窗口除数个数。",
            "remaining": SHORT_DENSITY,
        },
        {
            "gate": "HotDensityCertificateClosed",
            "closed": True,
            "proved": False,
            "meaning": "除数密度若超过阈值，得到热频率除数密度证书。",
            "remaining": HOT_DENSITY,
        },
        {
            "gate": "GenericTauClosureRejected",
            "closed": True,
            "proved": True,
            "meaning": "没有实际阈值比较时，不能用普通 tau(h) 估计宣称闭合。",
            "remaining": PDEC_COMPARE,
        },
        {
            "gate": "WindowedDivisorEnvelopeCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明所有正式频率的短窗口除数密度低于 PDEC 阈值。",
            "remaining": f"{SHORT_DENSITY} AND {PDEC_COMPARE}",
        },
        {
            "gate": "HotDensityExcludedCurrentCorpus",
            "closed": False,
            "proved": False,
            "meaning": "尚未排斥热除数密度的 PDEC/ColumnCRT/SAE 出口。",
            "remaining": f"{HOT_DENSITY} AND {LOW_QUOTIENT}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_windowed_reciprocal_divisor_density_router",
        "status": "windowed_reciprocal_divisor_envelope_reduced_to_short_window_density_pdec_sae_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "reciprocal_to_divisor_count_closed": True,
        "hot_density_certificate_closed": True,
        "generic_tau_closure_rejected": True,
        "windowed_divisor_envelope_proved": False,
        "hot_density_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SHORT_DENSITY,
        "parallel_targets": [PDEC_COMPARE, HOT_DENSITY, LOW_QUOTIENT],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "短窗口倒数除数封套进一步压成除数密度阈值。对 Y<g<=2Y，"
            "倒数和至多为 N_h(Y,2Y]/Y；若它超过 eta，则 h 在这个短乘法窗口中至少有 eta Y "
            "个除数。因而低有效模若无法由倒数封套吸收，就物化为热频率除数密度证书。"
            "这个证书必须进入 PDEC/ColumnCRT 或 SAE，不能作为普通 tau(h) 粗估计自由处理。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 短窗口倒数除数密度路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"reciprocal_to_divisor_count_closed={fmt_bool(result['reciprocal_to_divisor_count_closed'])}",
        f"hot_density_certificate_closed={fmt_bool(result['hot_density_certificate_closed'])}",
        f"generic_tau_closure_rejected={fmt_bool(result['generic_tau_closure_rejected'])}",
        f"windowed_divisor_envelope_proved={fmt_bool(result['windowed_divisor_envelope_proved'])}",
        f"hot_density_excluded={fmt_bool(result['hot_density_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 短窗口密度阈值",
        "",
        "对任意窗口 `Y<g<=2Y`，有",
        "",
        "```text",
        "sum_{g|h, Y<g<=2Y} 1/g <= N_h(Y,2Y]/Y.",
        "```",
        "",
        "所以若该倒数和大于 `eta`，就强制",
        "",
        "```text",
        "N_h(Y,2Y] >= eta Y.",
        "```",
        "",
        "这把低有效模失败变成短窗口除数密度证书。",
        "",
        "## 2. 引理表",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["lemmas"]:
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
            "审稿边界：本步只把窗口倒数封套转成除数密度证书；尚未证明正式频率族没有热除数窗口。",
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
