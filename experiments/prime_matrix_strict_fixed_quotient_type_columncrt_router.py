#!/usr/bin/env python3
"""生成 strict 固定商型 ColumnCRT/PDEC 路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_fixed_quotient_type_columncrt_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-fixed-quotient-type-columncrt-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-fixed-quotient-type-columncrt-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-fixed-quotient-type-columncrt-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-large-pair-kernel-difference-router.md",
    MONOGRAPH / "prime-matrix-strict-low-multiplier-common-kernel-router.md",
    MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.md",
    MONOGRAPH / "h4-pdec-column-defect-routing-contract.md",
    MONOGRAPH / "h4-pdec-admissible-constraint-table.md",
]

FIXED_TYPE = "FixedQuotientTypeColumnCRTOrPDECExclusion"
SCALED_CORE = "ScaledCoreDivisorDensityDescentOrFixedTypePDEC"
DESCENT_TRANSFER = "FixedQuotientDensityTransferWithoutLoss"
FIXED_PDEC = "FixedQuotientTypePDECColumnCertificateExclusion"
BOUNDED_SAE = "BoundedQuotientTypeSAEAbsorption"
FANIN = "MultiSourceKernelFanInSAEOrPDECExclusion"


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
    """列出固定商型压缩引理。"""
    return [
        {
            "name": "fixed_type_scaled_frequency_identity",
            "formula": "For c=b+a and gcd(b,c)=1, g=kb and g'=kc both divide h iff kbc divides h.",
            "status": "closed",
            "meaning": "固定商型复现精确等价于核心 k 整除缩频 h/(bc)。",
        },
        {
            "name": "core_interval_bounds",
            "formula": "Y/max(b,c)<k<=2Y/min(b,c).",
            "status": "closed",
            "meaning": "原短窗口中的成对除数复现转成核心 k 的有界乘法窗口。",
        },
        {
            "name": "strict_height_descent",
            "formula": "bc>=2, hence |h/(bc)|<=|h|/2 for every legal fixed quotient type.",
            "status": "closed",
            "meaning": "固定商型递归不能无限原地循环；每次都至少折半频率高度。",
        },
        {
            "name": "finite_descent_depth",
            "formula": "Any chain of fixed quotient descents has length <= floor(log_2 |h|).",
            "status": "closed",
            "meaning": "若一直不触发 PDEC/SAE，递归链也必须在有限深度终止。",
        },
        {
            "name": "persistence_to_fixed_pdec",
            "formula": "Persistent same (b,c) core intervals across formal units define a fixed quotient-type ColumnCRT/PDEC certificate.",
            "status": "registered_route_open",
            "meaning": "跨 formal unit 的同型复现是命名坏窗，不可当作自由误差。",
        },
        {
            "name": "single_unit_density_to_scaled_core",
            "formula": "Many same-type pairs inside one formal unit give a short-window divisor-density packet for h/(bc).",
            "status": "closed_reduction",
            "meaning": "单 formal unit 内的同型复现变成缩频核心除数密度问题。",
        },
        {
            "name": "density_transfer_without_loss",
            "formula": "The number and weight loss from pairs (g,g') to cores k must be bounded uniformly through descent.",
            "status": "open_input",
            "meaning": "要闭合固定商型出口，还需证明密度阈值不会在递归中被稀释到不可用。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的固定商型大核分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "FixedTypeScaledFrequencyIdentityClosed",
            "closed": True,
            "proved": True,
            "meaning": "固定 `(b,c)` 的每个复现等价于 `k|h/(bc)`。",
            "remaining": SCALED_CORE,
        },
        {
            "gate": "CoreIntervalBoundsClosed",
            "closed": True,
            "proved": True,
            "meaning": "核心 `k` 落在由 `(b,c)` 决定的有界乘法窗口中。",
            "remaining": "无。",
        },
        {
            "gate": "StrictHeightDescentClosed",
            "closed": True,
            "proved": True,
            "meaning": "`bc>=2`，固定商型递归每步至少折半频率高度。",
            "remaining": "无无限循环。",
        },
        {
            "gate": "FixedTypePDECRouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "跨 formal unit 的同型核心窗口复现应进入固定商型 ColumnCRT/PDEC。",
            "remaining": FIXED_PDEC,
        },
        {
            "gate": "DensityTransferWithoutLossProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明成对复现到核心窗口的密度阈值在递归中保持足够强。",
            "remaining": DESCENT_TRANSFER,
        },
        {
            "gate": "FixedQuotientTypeExcluded",
            "closed": False,
            "proved": False,
            "meaning": "尚未排斥固定商型 PDEC，也未闭合缩频核心密度递归的无损传递。",
            "remaining": f"{FIXED_PDEC} AND {DESCENT_TRANSFER}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_fixed_quotient_type_columncrt_router",
        "status": "fixed_quotient_type_reduced_to_scaled_core_descent_or_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "fixed_type_scaled_frequency_identity_closed": True,
        "core_interval_bounds_closed": True,
        "strict_height_descent_closed": True,
        "finite_descent_depth_closed": True,
        "single_unit_density_to_scaled_core_closed": True,
        "fixed_type_pdec_route_registered": True,
        "density_transfer_without_loss_proved": False,
        "fixed_type_pdec_excluded": False,
        "fixed_quotient_type_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": DESCENT_TRANSFER,
        "secondary_attack_target": FIXED_PDEC,
        "parallel_targets": [BOUNDED_SAE, FANIN],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "固定商型出口已经从相位口号压成精确缩频递归。令 c=b+a。"
            "由于 gcd(b,c)=1，若 g=kb 与 g'=kc 都整除 h，则 lcm(g,g')=kbc 也整除 h；"
            "反过来 kbc|h 即给出同商型 pair。因此同一商型复现等价于核心 k 整除 h/(bc)。"
            "又因为合法商型有 bc>=2，所以每次固定商型递归都会把频率高度至少折半，"
            "不能形成无限循环。剩余缺口是：证明 pair 到 core 的密度/权重传递无损，"
            "或排斥跨 formal unit 的固定商型 ColumnCRT/PDEC 证书。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 固定商型 ColumnCRT/PDEC 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fixed_type_scaled_frequency_identity_closed={fmt_bool(result['fixed_type_scaled_frequency_identity_closed'])}",
        f"core_interval_bounds_closed={fmt_bool(result['core_interval_bounds_closed'])}",
        f"strict_height_descent_closed={fmt_bool(result['strict_height_descent_closed'])}",
        f"finite_descent_depth_closed={fmt_bool(result['finite_descent_depth_closed'])}",
        f"single_unit_density_to_scaled_core_closed={fmt_bool(result['single_unit_density_to_scaled_core_closed'])}",
        f"fixed_type_pdec_route_registered={fmt_bool(result['fixed_type_pdec_route_registered'])}",
        f"density_transfer_without_loss_proved={fmt_bool(result['density_transfer_without_loss_proved'])}",
        f"fixed_type_pdec_excluded={fmt_bool(result['fixed_type_pdec_excluded'])}",
        f"fixed_quotient_type_excluded={fmt_bool(result['fixed_quotient_type_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确缩频",
        "",
        "固定商型 `(b,a)`，记 `c=b+a`。上一层已经保证",
        "",
        "```text",
        "g=kb,  g'=kc,  gcd(b,c)=1.",
        "```",
        "",
        "于是",
        "",
        "```text",
        "g|h and g'|h  <=>  lcm(g,g')=kbc | h  <=>  k | h/(bc).",
        "```",
        "",
        "而原短窗口 `Y<g,g'<=2Y` 给出",
        "",
        "```text",
        "Y/max(b,c) < k <= 2Y/min(b,c).",
        "```",
        "",
        "所以固定商型复现就是缩频 `h/(bc)` 的短窗口核心除数问题。",
        "",
        "## 2. 递归不能绕圈",
        "",
        "合法固定商型有 `b,c>=1` 且 `b!=c`，因此 `bc>=2`。每次进入同类缩频递归都满足",
        "",
        "```text",
        "|h/(bc)| <= |h|/2.",
        "```",
        "",
        "故固定商型链最长为 `floor(log_2 |h|)`。这闭合了循环风险，但不自动闭合密度传递和 PDEC 排斥。",
        "",
        "## 3. 引理表",
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
            "## 4. 判定表",
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
            "## 5. 下一步最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并列需要补齐：",
            "",
            "```text",
            result["secondary_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步只闭合固定商型的缩频恒等式与有限下降；未闭合密度无损传递，也未排斥固定商型 PDEC。",
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
