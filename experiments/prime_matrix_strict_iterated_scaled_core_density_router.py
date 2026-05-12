#!/usr/bin/env python3
"""生成 strict 迭代缩频核心密度账本路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_iterated_scaled_core_density_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-iterated-scaled-core-density-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-iterated-scaled-core-density-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-iterated-scaled-core-density-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-fixed-quotient-density-transfer-router.md",
    MONOGRAPH / "prime-matrix-strict-fixed-quotient-type-columncrt-router.md",
    MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.md",
]

ITERATED = "IteratedScaledCoreDensitySurvivalOrPDECEscape"
THRESHOLD_COLLAPSE = "IteratedThresholdCollapseExclusionLedger"
DEPTH_LCM = "DepthwiseLCMExplosionAgainstScaledFrequencyHeight"
FIXED_PDEC = "FixedQuotientTypePDECColumnCertificateExclusion"
SAE_ABSORB = "BoundedQuotientTypeSAEAbsorption"


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
    """列出迭代账本引理。"""
    return [
        {
            "name": "scaled_frequency_product_law",
            "formula": "h_r=h_0/prod_{i<=r} b_i c_i.",
            "status": "closed",
            "meaning": "每层固定商型都精确剥离一个商型乘积。",
        },
        {
            "name": "strict_height_decay_law",
            "formula": "|h_r|<=|h_0|/2^r.",
            "status": "closed",
            "meaning": "因每层 b_i c_i>=2，递归深度有限。",
        },
        {
            "name": "density_loss_product_law",
            "formula": "rho_r>=rho_0/prod_{i<=r} A_{Lambda_i}, with A_{Lambda_i}<=8Lambda_i^2.",
            "status": "closed",
            "meaning": "密度损耗完全由有限字母表乘子登记。",
        },
        {
            "name": "window_scale_product_law",
            "formula": "Y_r is bounded by Y_0/prod_i max(b_i,c_i) and Y_0/prod_i min(b_i,c_i).",
            "status": "closed",
            "meaning": "核心窗口尺度随商型链显式变化。",
        },
        {
            "name": "three_exit_ledger",
            "formula": "At each depth: LCM explosion, fixed-type PDEC escape, or threshold collapse.",
            "status": "closed_dichotomy",
            "meaning": "迭代不再有第四种无名出口。",
        },
        {
            "name": "threshold_collapse_exclusion",
            "formula": "Show rho_r |I_r| stays above the trigger before height descent makes LCM impossible.",
            "status": "open_input",
            "meaning": "剩余硬点是排斥阈值过早坍缩。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的固定商型缩频迭代分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "ScaledFrequencyProductLawClosed",
            "closed": True,
            "proved": True,
            "meaning": "缩频频率等于初始频率除以全部商型乘积。",
            "remaining": "无。",
        },
        {
            "gate": "StrictHeightDecayClosed",
            "closed": True,
            "proved": True,
            "meaning": "每层至少折半，递归不能无限循环。",
            "remaining": "无。",
        },
        {
            "gate": "DensityLossProductLedgerClosed",
            "closed": True,
            "proved": True,
            "meaning": "全部密度损耗由 `prod A_Lambda` 显式登记。",
            "remaining": THRESHOLD_COLLAPSE,
        },
        {
            "gate": "ThreeExitLedgerClosed",
            "closed": True,
            "proved": True,
            "meaning": "每层只剩 LCM 高度矛盾、固定商型 PDEC、阈值坍缩三出口。",
            "remaining": f"{DEPTH_LCM} OR {FIXED_PDEC} OR {THRESHOLD_COLLAPSE}",
        },
        {
            "gate": "IteratedThresholdCollapseExcluded",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明阈值不会在触发 LCM/PDEC/SAE 前过早低于 1 个有效核心。",
            "remaining": THRESHOLD_COLLAPSE,
        },
        {
            "gate": "IteratedScaledCoreDensitySurvivalProved",
            "closed": False,
            "proved": False,
            "meaning": "账本已闭合，但尚未排斥阈值坍缩，也未排斥固定商型 PDEC。",
            "remaining": f"{THRESHOLD_COLLAPSE} AND {FIXED_PDEC}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_iterated_scaled_core_density_router",
        "status": "iterated_scaled_core_density_ledger_closed_threshold_collapse_and_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "scaled_frequency_product_law_closed": True,
        "strict_height_decay_closed": True,
        "density_loss_product_ledger_closed": True,
        "window_scale_product_law_closed": True,
        "three_exit_ledger_closed": True,
        "iterated_threshold_collapse_excluded": False,
        "depthwise_lcm_explosion_proved": False,
        "fixed_type_pdec_excluded": False,
        "iterated_scaled_core_density_survival_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": THRESHOLD_COLLAPSE,
        "secondary_attack_target": FIXED_PDEC,
        "parallel_targets": [DEPTH_LCM, SAE_ABSORB],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "迭代缩频核心密度账本已经闭合。若固定商型链为 (b_i,c_i)，则 "
            "h_r=h_0/prod b_i c_i，且因 b_i c_i>=2 有 |h_r|<=|h_0|/2^r。"
            "密度损耗也完全登记为 rho_r>=rho_0/prod A_{Lambda_i}，其中 "
            "A_{Lambda_i}<=8Lambda_i^2。于是递归层不再有循环或无名出口："
            "每一层必须是 LCM 高度矛盾、固定商型 PDEC 逃逸，或阈值坍缩。"
            "当前唯一新的数学缺口是排斥阈值过早坍缩，另保留固定商型 PDEC 排斥。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 迭代缩频核心密度账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"scaled_frequency_product_law_closed={fmt_bool(result['scaled_frequency_product_law_closed'])}",
        f"strict_height_decay_closed={fmt_bool(result['strict_height_decay_closed'])}",
        f"density_loss_product_ledger_closed={fmt_bool(result['density_loss_product_ledger_closed'])}",
        f"window_scale_product_law_closed={fmt_bool(result['window_scale_product_law_closed'])}",
        f"three_exit_ledger_closed={fmt_bool(result['three_exit_ledger_closed'])}",
        f"iterated_threshold_collapse_excluded={fmt_bool(result['iterated_threshold_collapse_excluded'])}",
        f"depthwise_lcm_explosion_proved={fmt_bool(result['depthwise_lcm_explosion_proved'])}",
        f"fixed_type_pdec_excluded={fmt_bool(result['fixed_type_pdec_excluded'])}",
        f"iterated_scaled_core_density_survival_proved={fmt_bool(result['iterated_scaled_core_density_survival_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 统一账本",
        "",
        "一条固定商型缩频链满足",
        "",
        "```text",
        "h_r = h_0 / prod_{i<=r} b_i c_i,",
        "|h_r| <= |h_0| / 2^r.",
        "```",
        "",
        "对应密度阈值满足",
        "",
        "```text",
        "rho_r >= rho_0 / prod_{i<=r} A_{Lambda_i},",
        "A_{Lambda_i} <= 8 Lambda_i^2.",
        "```",
        "",
        "所以固定商型路线已从“可能无限缠绕”变成有限深度的显式阈值账本。",
        "",
        "## 2. 三出口",
        "",
        "每一层只剩三种情况：",
        "",
        "```text",
        "1. LCM explosion against |h_r|;",
        "2. fixed quotient-type ColumnCRT/PDEC escape;",
        "3. threshold collapse before either trigger fires.",
        "```",
        "",
        "前两类是命名矛盾/证书出口；第三类是当前最新最窄硬点。",
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
            "审稿边界：本步闭合迭代账本和三出口分解；未证明阈值坍缩不发生，也未排斥固定商型 PDEC。",
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
