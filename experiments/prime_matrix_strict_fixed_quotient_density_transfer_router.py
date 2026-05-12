#!/usr/bin/env python3
"""生成 strict 固定商型密度传递路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_fixed_quotient_density_transfer_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-fixed-quotient-density-transfer-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-fixed-quotient-density-transfer-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-fixed-quotient-density-transfer-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-fixed-quotient-type-columncrt-router.md",
    MONOGRAPH / "prime-matrix-strict-large-pair-kernel-difference-router.md",
    MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.md",
]

DENSITY_TRANSFER = "FixedQuotientDensityTransferWithoutLoss"
ITERATED_DENSITY = "IteratedScaledCoreDensitySurvivalOrPDECEscape"
FIXED_PDEC = "FixedQuotientTypePDECColumnCertificateExclusion"
TYPE_SAE = "BoundedQuotientTypeSAEAbsorption"
HEIGHT_DESCENT = "StrictHeightDescentFiniteDepthLedger"


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
    """列出密度传递引理。"""
    return [
        {
            "name": "fixed_type_core_pair_bijection",
            "formula": "For fixed coprime (b,c), k <-> (kb,kc) is one-to-one.",
            "status": "closed",
            "meaning": "固定商型内部从 pair 到 core 不丢计数。",
        },
        {
            "name": "finite_type_pigeonhole_loss",
            "formula": "With at most A_Lambda<=8Lambda^2 types, T pair locks give some type with >=T/A_Lambda cores.",
            "status": "closed",
            "meaning": "跨商型选择只有登记的有限字母表损失。",
        },
        {
            "name": "core_window_distortion_bound",
            "formula": "Y/max(b,c)<k<=2Y/min(b,c), with 1<=b,c<2Lambda.",
            "status": "closed",
            "meaning": "核心窗口长度和乘法比被 Lambda 显式控制。",
        },
        {
            "name": "registered_density_threshold_transfer",
            "formula": "A pair-lock density rho transfers to core density at least rho/(8Lambda^2) after type selection.",
            "status": "closed",
            "meaning": "密度阈值没有隐性丢失；所有损耗进入显式乘子账本。",
        },
        {
            "name": "no_untracked_weight_loss",
            "formula": "Any orientation or duplicate convention costs at most a factor 2 and is absorbed into A_Lambda.",
            "status": "closed",
            "meaning": "有向/无向 pair 口径不会形成额外未登记误差。",
        },
        {
            "name": "iterated_threshold_survival",
            "formula": "After depth r, threshold loss is controlled by product_r A_{Lambda_r}; it must still beat the PDEC/SAE trigger.",
            "status": "open_input",
            "meaning": "多层缩频递归的阈值账本仍需独立闭合。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的固定商型缩频分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "CorePairBijectionClosed",
            "closed": True,
            "proved": True,
            "meaning": "固定商型内部 `k` 与 `(kb,kc)` 一一对应。",
            "remaining": "无。",
        },
        {
            "gate": "FiniteTypePigeonholeLossClosed",
            "closed": True,
            "proved": True,
            "meaning": "跨商型只损失 `<=8Lambda^2` 的显式因子。",
            "remaining": TYPE_SAE,
        },
        {
            "gate": "DensityTransferWithoutLossClosed",
            "closed": True,
            "proved": True,
            "meaning": "pair-lock 密度到 core-density 的全部损耗已登记。",
            "remaining": ITERATED_DENSITY,
        },
        {
            "gate": "IteratedThresholdSurvivalProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明多层递归后的阈值仍足以触发 PDEC/SAE 或 LCM 高度矛盾。",
            "remaining": ITERATED_DENSITY,
        },
        {
            "gate": "FixedPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "尚未排斥跨 formal unit 的固定商型 PDEC/ColumnCRT 证书。",
            "remaining": FIXED_PDEC,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_fixed_quotient_density_transfer_router",
        "status": "fixed_quotient_density_transfer_closed_iterated_threshold_and_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "core_pair_bijection_closed": True,
        "finite_type_pigeonhole_loss_closed": True,
        "core_window_distortion_bound_closed": True,
        "density_transfer_without_loss_closed": True,
        "no_untracked_weight_loss_closed": True,
        "iterated_threshold_survival_proved": False,
        "fixed_pdec_excluded": False,
        "fixed_quotient_type_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ITERATED_DENSITY,
        "secondary_attack_target": FIXED_PDEC,
        "parallel_targets": [HEIGHT_DESCENT, TYPE_SAE],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "固定商型密度传递已经闭合到显式乘子账本。对固定互素商型 (b,c)，"
            "核心 k 与 pair (kb,kc) 一一对应，因此该商型内部没有计数损失。"
            "跨商型选择至多损失有限字母表因子 A_Lambda<=8Lambda^2；有向/无向口径的常数损失"
            "也并入这个因子。于是 pair-lock 密度进入缩频 core-density 时没有未登记损耗。"
            "新的剩余是多层缩频后阈值是否仍足以触发 LCM/PDEC/SAE，或固定商型 PDEC 是否可排斥。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 固定商型密度传递路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"core_pair_bijection_closed={fmt_bool(result['core_pair_bijection_closed'])}",
        f"finite_type_pigeonhole_loss_closed={fmt_bool(result['finite_type_pigeonhole_loss_closed'])}",
        f"core_window_distortion_bound_closed={fmt_bool(result['core_window_distortion_bound_closed'])}",
        f"density_transfer_without_loss_closed={fmt_bool(result['density_transfer_without_loss_closed'])}",
        f"no_untracked_weight_loss_closed={fmt_bool(result['no_untracked_weight_loss_closed'])}",
        f"iterated_threshold_survival_proved={fmt_bool(result['iterated_threshold_survival_proved'])}",
        f"fixed_pdec_excluded={fmt_bool(result['fixed_pdec_excluded'])}",
        f"fixed_quotient_type_excluded={fmt_bool(result['fixed_quotient_type_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 无隐性损失",
        "",
        "固定 `(b,c)` 后，映射",
        "",
        "```text",
        "k -> (kb,kc)",
        "```",
        "",
        "是一一对应。因此固定商型内部没有 pair 到 core 的计数损失。",
        "",
        "若还没有固定商型，只知道总共有 `T` 个大核 pair-lock，则上一层给出商型数",
        "",
        "```text",
        "A_Lambda <= 8 Lambda^2.",
        "```",
        "",
        "鸽巢后存在某个商型至少贡献",
        "",
        "```text",
        "T/A_Lambda",
        "```",
        "",
        "个核心 `k`。这就是全部损耗；后续证明必须把它写入阈值账本，不能再额外引入未登记常数。",
        "",
        "## 2. 剩余不是循环，而是阈值账本",
        "",
        "固定商型递归每步已有 `|h| -> |h|/(bc) <= |h|/2` 的高度下降。现在真正剩余是：经过有限多层后，`prod A_Lambda` 的损耗是否仍允许触发 LCM 高度矛盾或 PDEC/SAE 出口。",
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
            "审稿边界：本步闭合密度传递的显式损耗账本；未闭合多层阈值生存，也未排斥固定商型 PDEC。",
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
