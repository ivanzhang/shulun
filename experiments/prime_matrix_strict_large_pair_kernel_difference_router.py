#!/usr/bin/env python3
"""生成 strict 大成对共同核差值锁路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_large_pair_kernel_difference_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-large-pair-kernel-difference-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-large-pair-kernel-difference-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-large-pair-kernel-difference-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-low-multiplier-common-kernel-router.md",
    MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.md",
    MONOGRAPH / "h4-pdec-column-defect-routing-contract.md",
    MONOGRAPH / "h4-pdec-admissible-constraint-table.md",
]

PAIR_KERNEL = "LargePairKernelDifferenceColumnCRTExclusion"
FINITE_QUOTIENT = "FiniteQuotientAlphabetForLargePairKernelLocks"
FIXED_TYPE_PDEC = "FixedQuotientTypeColumnCRTOrPDECExclusion"
BOUNDED_TYPE_SAE = "BoundedQuotientTypeSAEAbsorption"
FANIN_KERNEL = "MultiSourceKernelFanInSAEOrPDECExclusion"


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
    """列出差值锁压缩引理。"""
    return [
        {
            "name": "exact_pair_gcd_normal_form",
            "formula": "For k=gcd(g,g'), write g=kb, g'=k(b+a), with gcd(b,b+a)=1.",
            "status": "closed",
            "meaning": "成对共同核可规范化为精确核乘互素商对。",
        },
        {
            "name": "bounded_quotient_gap",
            "formula": "If Y<g,g'<=2Y and k>Y/Lambda, then 1<=b,b+a<2Lambda and 0<|a|<Lambda.",
            "status": "closed",
            "meaning": "大核差值锁把商变量压进有限字母表。",
        },
        {
            "name": "finite_quotient_alphabet",
            "formula": "#{(b,a): 1<=b,b+a<2Lambda, a!=0, gcd(b,b+a)=1} <= 8 Lambda^2.",
            "status": "closed",
            "meaning": "大成对核异常不能产生无限新类型，只能在 O(Lambda^2) 个商型中移动。",
        },
        {
            "name": "fixed_type_persistence_route",
            "formula": "Repeated same (b,a) locks force a fixed quotient-type ColumnCRT/PDEC certificate.",
            "status": "registered_route_open",
            "meaning": "同一商型复现时，相位自由度只剩核心 k，进入固定类型 CRT 证书。",
        },
        {
            "name": "bounded_type_sae_route",
            "formula": "If no quotient type persists beyond its threshold, total large-pair locks are SAE-countable.",
            "status": "registered_route_open",
            "meaning": "不持久的有限字母表异常应由 SAE 容量账本吸收。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的低乘子共同核分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "ExactPairGCDNormalFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "大成对核可写成精确核 k 与互素商对 b,b+a。",
            "remaining": "无。",
        },
        {
            "gate": "FiniteQuotientAlphabetClosed",
            "closed": True,
            "proved": True,
            "meaning": "若 k>Y/Lambda，则商型数量至多 O(Lambda^2)。",
            "remaining": FINITE_QUOTIENT,
        },
        {
            "gate": "FixedTypePDECRouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "同一商型持久复现应进入固定商型 ColumnCRT/PDEC。",
            "remaining": FIXED_TYPE_PDEC,
        },
        {
            "gate": "BoundedTypeSAERouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "商型不持久时应按有限字母表 SAE 计数吸收。",
            "remaining": BOUNDED_TYPE_SAE,
        },
        {
            "gate": "LargePairKernelDifferenceExcluded",
            "closed": False,
            "proved": False,
            "meaning": "尚未排斥固定商型 PDEC，也未完成不持久商型 SAE 总量账本。",
            "remaining": f"{FIXED_TYPE_PDEC} AND {BOUNDED_TYPE_SAE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_large_pair_kernel_difference_router",
        "status": "large_pair_kernel_difference_reduced_to_finite_quotient_type_pdec_or_sae_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "exact_pair_gcd_normal_form_closed": True,
        "bounded_quotient_gap_closed": True,
        "finite_quotient_alphabet_closed": True,
        "fixed_type_pdec_route_registered": True,
        "bounded_type_sae_route_registered": True,
        "fixed_type_pdec_excluded": False,
        "bounded_type_sae_absorbed": False,
        "large_pair_kernel_difference_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": FIXED_TYPE_PDEC,
        "secondary_attack_target": BOUNDED_TYPE_SAE,
        "parallel_targets": [PAIR_KERNEL, FANIN_KERNEL],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "大成对共同核差值锁进一步压成有限商字母表。对一对短窗口除数 g,g'，"
            "取精确核 k=gcd(g,g')，写 g=kb、g'=k(b+a)，则 gcd(b,b+a)=1。"
            "若该核属于低乘子分支的阈值 k>Y/Lambda，因为 g,g' 都在 (Y,2Y]，"
            "必有 1<=b,b+a<2Lambda 且 0<|a|<Lambda。故所有这类异常只落在 "
            "O(Lambda^2) 个商型 (b,a) 中。持久同型复现应形成固定商型 ColumnCRT/PDEC；"
            "非持久同型则进入有限字母表 SAE 容量账本。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 大成对共同核差值锁路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_pair_gcd_normal_form_closed={fmt_bool(result['exact_pair_gcd_normal_form_closed'])}",
        f"bounded_quotient_gap_closed={fmt_bool(result['bounded_quotient_gap_closed'])}",
        f"finite_quotient_alphabet_closed={fmt_bool(result['finite_quotient_alphabet_closed'])}",
        f"fixed_type_pdec_route_registered={fmt_bool(result['fixed_type_pdec_route_registered'])}",
        f"bounded_type_sae_route_registered={fmt_bool(result['bounded_type_sae_route_registered'])}",
        f"fixed_type_pdec_excluded={fmt_bool(result['fixed_type_pdec_excluded'])}",
        f"bounded_type_sae_absorbed={fmt_bool(result['bounded_type_sae_absorbed'])}",
        f"large_pair_kernel_difference_excluded={fmt_bool(result['large_pair_kernel_difference_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有限商字母表",
        "",
        "对大成对核事件，取精确共同核",
        "",
        "```text",
        "k=gcd(g,g'),  g=kb,  g'=k(b+a),  gcd(b,b+a)=1.",
        "```",
        "",
        "若 `k>Y/Lambda` 且 `Y<g,g'<=2Y`，则",
        "",
        "```text",
        "1<=b,b+a<2Lambda,  0<|a|<Lambda.",
        "```",
        "",
        "因此所有商型 `(b,a)` 至多为 `O(Lambda^2)` 个。这个压缩是结构性的：它不依赖真实样本缺席，也不使用统计逼近。",
        "",
        "## 2. 出口",
        "",
        "同一 `(b,a)` 反复出现时，变量只剩共同核 `k` 的相位移动，形成固定商型 `ColumnCRT/PDEC`。若所有 `(b,a)` 都不持久，则有限字母表给出可求和的 `SAE` 账本入口。",
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
            "审稿边界：本步闭合有限商型压缩，不闭合固定商型 PDEC 排斥，也不闭合 SAE 总量账本。",
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
