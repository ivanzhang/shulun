#!/usr/bin/env python3
"""生成 square-phase 的 RFP-Upper 直接下钻证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_rfp_upper_direct_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-rfp-upper-direct-attack-router.json

输出：
  docs/monograph/prime-matrix-square-phase-rfp-upper-direct-attack-router.json
  docs/monograph/prime-matrix-square-phase-rfp-upper-direct-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-rfp-upper-direct-attack-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-rfp-upper-direct-attack-router.md"

RFP = "RFP-Upper"
LDG = "LDG-Lower"
RFP_AREA = "RFP-AreaCarryBound"
RFP_SELBERG = "RFP-SelbergConstantLedger"
CARRY = "CarryDiscrepancyEndpointReciprocalPhaseBound"
TAIL_DEFECT = "ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE"
HYP_DISC = "HyperbolicDiscFailurePDEC"
DIMENSION_GAP = "PostSquareEndpointDimensionGapGMinusBPositive"
NONFINAL = "NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction"

SOURCE_FILES = [
    "prime-matrix-square-phase-dimension-gap-attack-router.json",
    "prime-matrix-diagonal-postsquare-rfp-selberg-route.md",
    "prime-matrix-diagonal-postsquare-carry-discrepancy-pdec-route.md",
    "prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md",
    "prime-matrix-diagonal-postsquare-endpoint-reciprocal-osc-hard-attack.md",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_rfp_upper_direct_attack_router.py": sha256(
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


def formula_rows() -> list[dict[str, str]]:
    """列出 RFP 上界公式。"""
    return [
        {
            "name": "prime_pair_cover",
            "formula": "B(P)=#{(ell,m): y<ell<P<m, ell,m prime, P^2<ell*m<P^2+P}",
            "status": "closed_definition",
        },
        {
            "name": "three_curves",
            "formula": "m=floor(P^2/ell)+s, s in {1,2,3}",
            "status": "closed_reduction",
        },
        {
            "name": "hyperbolic_strip",
            "formula": "R_P={(a,b): y<a<P, P<b, P^2<ab<P^2+P}",
            "status": "closed_embedding",
        },
        {
            "name": "rfp_target",
            "formula": "B(P)<=1.50 P/log^2 P",
            "status": "open_upper_bound",
        },
        {
            "name": "area_target",
            "formula": "X(P)=|R_P|<=1.02P for P>=2003",
            "status": "open_tail_or_pdec",
        },
        {
            "name": "carry_discrepancy_target",
            "formula": "D(P)<=1.98 sqrt(P) for P>=10007",
            "status": "open_endpoint_reciprocal_phase",
        },
    ]


def obstruction_rows() -> list[dict[str, str]]:
    """列出 RFP 阻塞。"""
    return [
        {
            "obstruction": "two-dimensional sieve constant",
            "detail": "需要二维 Selberg/Brun 权常数加边界误差压到 1.50。",
            "route": RFP_SELBERG,
        },
        {
            "obstruction": "hyperbolic floor area",
            "detail": "窄带面积 X(P) 的 1.02P 尾段界等价于进位计数控制。",
            "route": RFP_AREA,
        },
        {
            "obstruction": "carry discrepancy",
            "detail": "进位偏差 D(P) 是端点倒数相位低频和；过大即 HyperbolicDisc/PDEC。",
            "route": CARRY,
        },
        {
            "obstruction": "tail prime-pair spike",
            "detail": "若三曲线素-素点超过二维筛预算，必须表现为短窗素数或尾锚异常集中。",
            "route": TAIL_DEFECT,
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "RFPTargetImportedFromDimensionGap",
            True,
            True,
            "维数差闭合需要 RFP-Upper 控制一尾素-素覆盖数。",
            RFP,
        ),
        row(
            "ThreeCurvePrimePairReductionClosed",
            True,
            True,
            "一尾覆盖已压成三条倒数地板素-素曲线。",
            RFP_SELBERG,
        ),
        row(
            "HyperbolicStripEmbeddingClosed",
            True,
            True,
            "B(P) 是双曲窄带 R_P 中两个坐标同为素数的点数。",
            RFP_SELBERG,
        ),
        row(
            "RFPAreaCarryBoundProved",
            False,
            False,
            "P>=2003 的 X(P)<=1.02P 尚未作者侧证明；过密需路由到 HyperbolicDisc/PDEC。",
            f"{RFP_AREA} OR {HYP_DISC}",
        ),
        row(
            "CarryDiscrepancyEndpointReciprocalPhaseProved",
            False,
            False,
            "D(P)<=1.98sqrt(P) 尚未证明；过大即端点倒数相位低频集中。",
            f"{CARRY} OR {HYP_DISC}",
        ),
        row(
            "RFPSelbergConstantProved",
            False,
            False,
            "二维上筛主常数、边界误差和离散误差尚未压入 1.50。",
            f"{RFP_SELBERG} OR {TAIL_DEFECT}",
        ),
        row(
            "RFPUpperCurrentCorpusProved",
            False,
            False,
            "RFP 已精确拆分，但面积、倒数相位和 Selberg 常数未同时闭合。",
            f"{RFP_AREA} AND {CARRY} AND {RFP_SELBERG}",
        ),
        row(
            "SquarePhaseDimensionGapClosed",
            False,
            False,
            "即便 RFP 闭合，仍需并行 LDG-Lower。",
            f"{LDG} AND {RFP}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "没有得到全局无条件终端矛盾。",
            f"({LDG} AND {RFP}) OR {NONFINAL}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 RFP-Upper 下钻证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_rfp_upper_direct_attack_router",
        "status": "rfp_upper_reduced_to_area_carry_selberg_reciprocal_phase_or_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "rfp_target_imported": True,
        "three_curve_prime_pair_reduction_closed": True,
        "hyperbolic_strip_embedding_closed": True,
        "rfp_area_carry_bound_proved": False,
        "carry_discrepancy_endpoint_reciprocal_phase_proved": False,
        "rfp_selberg_constant_proved": False,
        "rfp_upper_current_corpus_proved": False,
        "square_phase_dimension_gap_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": RFP,
        "hardpoint_after_router": f"{RFP_AREA} AND {CARRY} AND {RFP_SELBERG} OR PDEC/SAE defects",
        "next_direct_attack_target": CARRY,
        "parallel_attack_targets": [RFP_AREA, RFP_SELBERG, TAIL_DEFECT, HYP_DISC, LDG],
        "formula_rows": formula_rows(),
        "obstruction_rows": obstruction_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`RFP-Upper` 已下钻为三块具体任务："
            "双曲窄带面积/进位计数、端点倒数相位 CarryDiscrepancy、二维 Selberg 上筛常数。"
            "三条倒数地板素-素曲线的几何表示已闭合；若 `B(P)` 超过 "
            "`1.50P/log^2P`，失败不能是无名现象，只能表现为面积进位过密、"
            "端点倒数相位低频集中，或尾锚素对异常峰值，并进入 PDEC/SAE。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase RFP-Upper 直接下钻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"three_curve_prime_pair_reduction_closed={fmt_bool(result['three_curve_prime_pair_reduction_closed'])}",
        f"hyperbolic_strip_embedding_closed={fmt_bool(result['hyperbolic_strip_embedding_closed'])}",
        f"rfp_area_carry_bound_proved={fmt_bool(result['rfp_area_carry_bound_proved'])}",
        f"carry_discrepancy_endpoint_reciprocal_phase_proved={fmt_bool(result['carry_discrepancy_endpoint_reciprocal_phase_proved'])}",
        f"rfp_selberg_constant_proved={fmt_bool(result['rfp_selberg_constant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 公式",
        "",
        "| name | formula | status |",
        "| --- | --- | --- |",
    ]
    for item in result["formula_rows"]:
        lines.append(f"| `{item['name']}` | `{table_cell(item['formula'])}` | `{item['status']}` |")
    lines.extend(
        [
            "",
            "## 2. 阻塞与路由",
            "",
            "| obstruction | detail | route |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["obstruction_rows"]:
        lines.append(
            f"| `{item['obstruction']}` | {table_cell(item['detail'])} | `{item['route']}` |"
        )
    lines.extend(
        [
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
            f"- 主攻 `{CARRY}`：证明端点倒数相位偏差 `D(P)<=1.98sqrt(P)`，或产出 `{HYP_DISC}`。",
            f"- 并行攻 `{RFP_SELBERG}`：给出二维上筛常数账本，压入 `1.50`。",
            f"- 保留 `{RFP_AREA}` 的面积进位边界和 `{TAIL_DEFECT}` 的尾锚异常路由。",
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
                "rfp_upper_current_corpus_proved": result["rfp_upper_current_corpus_proved"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
