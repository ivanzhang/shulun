#!/usr/bin/env python3
"""生成 square-phase RFP 过密维数塌缩路由证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_rfp_excess_dimension_collapse_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-rfp-excess-dimension-collapse-router.json

输出：
  docs/monograph/prime-matrix-square-phase-rfp-excess-dimension-collapse-router.json
  docs/monograph/prime-matrix-square-phase-rfp-excess-dimension-collapse-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-rfp-excess-dimension-collapse-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-rfp-excess-dimension-collapse-router.md"

CG = 0.48
CB = 1.50
OFFSET_COUNT = 3

LOW_DEFECT = "LowSkeletonDeficitPDECOrSAE"
RFP_EXCESS = "ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE"
SELBERG_LEDGER = "RFP-SelbergConstantLedger"
FLOOR_PDEC = "ReciprocalFloorCongruencePDECOrSelbergDistributionLedger"

SOURCE_FILES = [
    "prime-matrix-square-phase-nearfull-rough-primevoid-dichotomy-router.json",
    "prime-matrix-square-phase-rfp-upper-direct-attack-router.json",
    "prime-matrix-diagonal-postsquare-rfp-selberg-route.md",
    "prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md",
    "prime-matrix-diagonal-postsquare-ero-low-bprocess-envelope.md",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_rfp_excess_dimension_collapse_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def scale_rows() -> list[dict[str, Any]]:
    """给出反例态下的维数塌缩尺度。"""
    rows = []
    for p in [23, 101, 1009, 10007, 1000003]:
        log_p = math.log(p)
        one_curve_lower = CG * p / (OFFSET_COUNT * log_p)
        rfp_normal = CB * p / (log_p * log_p)
        rows.append(
            {
                "p": p,
                "one_curve_forced_lower": one_curve_lower,
                "normal_rfp_total_budget": rfp_normal,
                "one_curve_lower_over_normal_total": one_curve_lower / rfp_normal,
                "dimension_collapse_factor": CG * log_p / (OFFSET_COUNT * CB),
            }
        )
    return rows


def congruence_rows() -> list[dict[str, str]]:
    """列出 reciprocal-floor congruence 的等价形式。"""
    return [
        {
            "object": "curve_value",
            "formula": "m_s(ell)=floor(P^2/ell)+s, s in {1,2,3}",
            "meaning": "三条倒数地板素对曲线的互补因子。",
        },
        {
            "object": "divisibility",
            "formula": "q | m_s(ell) iff floor(P^2/ell)=q*u-s for some u",
            "meaning": "素性筛的第二坐标坏事件。",
        },
        {
            "object": "reciprocal_interval",
            "formula": "P^2/(q*u-s+1) < ell <= P^2/(q*u-s)",
            "meaning": "每个坏事件是倒数端点短区间，不是任意残基。",
        },
        {
            "object": "range",
            "formula": "y<ell<P and P<m_s(ell)<eP",
            "meaning": "u 只在长度约 P/q 的短区间内取值。",
        },
        {
            "object": "defect",
            "formula": "bad count - expected local density",
            "meaning": "若 Selberg 分布账本失败，即得到 reciprocal-floor PDEC。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "PrimeVoidNoLowDefectForcesRFPDimensionCollapse",
            True,
            True,
            "由 prime-void 二分，若反例不走低骨架亏损，则 B(P)>=0.48P/logP。",
            RFP_EXCESS,
        ),
        row(
            "SingleCurvePositiveScaleForced",
            True,
            True,
            "三条曲线相加为 B(P)，故某个 s 有 B_s(P)>=0.16P/logP。",
            "PositiveDensityPrimeValuesOfReciprocalFloorCurve",
        ),
        row(
            "ReciprocalFloorDivisibilityIntervalFormula",
            True,
            True,
            "q|floor(P^2/ell)+s 精确等价于 ell 落在倒数端点短区间并集中。",
            "none",
        ),
        row(
            "SelbergDistributionWouldContradictCollapse",
            True,
            False,
            "若 reciprocal-floor 坏事件有二维筛正常分布，则 B_s 为 P/log^2P 级，不能达到 P/logP 级。",
            SELBERG_LEDGER,
        ),
        row(
            "RFPExcessRoutedToConcreteDefect",
            True,
            False,
            "RFP 过密不再是无名过密；它等价于某条曲线的素值维数塌缩，或 reciprocal-floor 局部分布缺陷。",
            FLOOR_PDEC,
        ),
        row(
            "RFPExcessExcluded",
            False,
            False,
            "尚未证明 Selberg 分布账本，也未排斥 reciprocal-floor PDEC。",
            f"{SELBERG_LEDGER} OR exclude {FLOOR_PDEC}",
        ),
        row(
            "DirectUnconditionalContradictionFound",
            False,
            False,
            "本步闭合的是 RFP 过密的结构定位，不是最终出口排斥。",
            f"exclude {LOW_DEFECT} and {RFP_EXCESS}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合。",
            f"{LOW_DEFECT} exclusion AND {RFP_EXCESS} exclusion",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造维数塌缩证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_rfp_excess_dimension_collapse_router",
        "status": "rfp_excess_reduced_to_single_curve_dimension_collapse_or_reciprocal_floor_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "prime_void_no_low_defect_forces_rfp_dimension_collapse": True,
        "single_curve_positive_scale_forced": True,
        "reciprocal_floor_divisibility_interval_formula_closed": True,
        "selberg_distribution_would_contradict_collapse": True,
        "rfp_excess_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "constants": {
            "c_g": CG,
            "c_b": CB,
            "offset_count": OFFSET_COUNT,
            "single_curve_constant": CG / OFFSET_COUNT,
        },
        "scale_rows": scale_rows(),
        "congruence_rows": congruence_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": FLOOR_PDEC,
        "plain_conclusion": (
            "在平方端点反例链中，若不发生低骨架亏损，则 `B(P)>=0.48P/logP`。"
            "三条倒数地板曲线中至少一条必须贡献 `0.16P/logP` 级素值，"
            "这比正常二维筛尺度 `P/log^2P` 高一个 `logP` 因子，是维数塌缩。"
            "该塌缩的最具体表达为：对 `m_s(ell)=floor(P^2/ell)+s`，"
            "`q|m_s(ell)` 精确等价于 `ell` 落入一族倒数端点短区间。"
            "因此 RFP 过密必须由 `RFP-SelbergConstantLedger` 失败，"
            "或由 reciprocal-floor 端点相位/PDEC 缺陷承担；尚未完成出口排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    constants = result["constants"]
    lines = [
        "# Prime Matrix square-phase RFP 过密维数塌缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prime_void_no_low_defect_forces_rfp_dimension_collapse={fmt_bool(result['prime_void_no_low_defect_forces_rfp_dimension_collapse'])}",
        f"single_curve_positive_scale_forced={fmt_bool(result['single_curve_positive_scale_forced'])}",
        f"reciprocal_floor_divisibility_interval_formula_closed={fmt_bool(result['reciprocal_floor_divisibility_interval_formula_closed'])}",
        f"rfp_excess_excluded={fmt_bool(result['rfp_excess_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 反例态强度",
        "",
        "在 `P>=23` 的平方端点，如果假设前半窗无素数且没有 LDG 亏损，则",
        "",
        "```text",
        "B(P)=G(P)>=0.48 P/logP.",
        "```",
        "",
        "写 `B(P)=B_1(P)+B_2(P)+B_3(P)`，其中",
        "",
        "```text",
        "B_s(P)=#{ell prime: y<ell<P, floor(P^2/ell)+s prime, 1<=ell*s-(P^2 mod ell)<P}.",
        "```",
        "",
        f"因此某个 `s` 必满足 `B_s(P)>={constants['single_curve_constant']:.2f}P/logP`。",
        "",
        "| P | 单曲线强制下界 | RFP正常总预算 | 单曲线/正常总预算 | 维数塌缩因子 |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["scale_rows"]:
        lines.append(
            f"| {item['p']} | {item['one_curve_forced_lower']:.6f} | "
            f"{item['normal_rfp_total_budget']:.6f} | "
            f"{item['one_curve_lower_over_normal_total']:.6f} | "
            f"{item['dimension_collapse_factor']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 2. reciprocal-floor 整除公式",
            "",
            "| object | formula | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["congruence_rows"]:
        lines.append(
            f"| `{item['object']}` | `{table_cell(item['formula'])}` | {table_cell(item['meaning'])} |"
        )
    lines.extend(
        [
            "",
            "这个公式是本步的实际下钻点：第二坐标素性不再写成抽象的 `m_s(ell) is prime`，而是写成一套随 `q` 变化的倒数短区间避让问题。若这些短区间在素数 `ell` 上有正常局部分布，则二维 Selberg 上筛给 `P/log^2P`；若不正常，异常本身就是 reciprocal-floor PDEC。",
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            "- 直接攻 `ReciprocalFloorCongruencePDECOrSelbergDistributionLedger`：证明倒数短区间坏事件满足二维 Selberg 分布，或把失败登记为端点相位缺陷。",
            "- 若接受外部二维 Selberg/Brun 上筛及该序列的分布账本，则 RFP 过密出口关闭；自足路线仍需内联该账本。",
            "- 该步仍未处理 `LowSkeletonDeficitPDECOrSAE`，所以不能宣称行/列命题无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "rfp_excess_excluded": result["rfp_excess_excluded"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
