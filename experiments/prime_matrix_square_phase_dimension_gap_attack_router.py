#!/usr/bin/env python3
"""生成 square-phase 粗幸存下界的维数差攻坚证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_dimension_gap_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-dimension-gap-attack-router.json

输出：
  docs/monograph/prime-matrix-square-phase-dimension-gap-attack-router.json
  docs/monograph/prime-matrix-square-phase-dimension-gap-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-dimension-gap-attack-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-dimension-gap-attack-router.md"

SQUARE_PHASE = "SquarePhaseRoughSurvivorUniformLowerBound"
DIMENSION_GAP = "PostSquareEndpointDimensionGapGMinusBPositive"
LDG = "LDG-Lower"
RFP = "RFP-Upper"
LOW_DEFECT = "LowSkeletonDeficitPDECOrSAE"
TAIL_DEFECT = "ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE"
FINITE_CRT = "FiniteSquarePhaseCRTContradiction"
NONFINAL = "NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction"
FIRST_HALF = "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP"

SOURCE_FILES = [
    "prime-matrix-prime-square-x-equals-p-wheel-router.json",
    "prime-matrix-prime-base-exponent-half-barrier-router.json",
    "prime-matrix-diagonal-postsquare-tail-collision-vanishing.md",
    "prime-matrix-diagonal-postsquare-tail-cofactor-identity.md",
    "prime-matrix-diagonal-postsquare-primepair-dimension-gap.md",
    "prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md",
    "prime-matrix-diagonal-postsquare-rfp-selberg-route.md",
    "prime-matrix-diagonal-postsquare-carry-discrepancy-pdec-route.md",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_dimension_gap_attack_router.py": sha256(
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


def reduction_rows() -> list[dict[str, str]]:
    """列出 square-phase 到维数差的严格压缩链。"""
    return [
        {
            "name": "x_equals_p_wheel",
            "status": "closed",
            "statement": "x=P 全覆盖等价于每个 1<=r<P 的 P^2+r 都有某个小素因子 q<P。",
        },
        {
            "name": "low_skeleton_split",
            "status": "closed",
            "statement": "先筛掉 q<=y=floor(P/e) 后，剩余低筛骨架 G(P) 只可能是素数或一尾项。",
        },
        {
            "name": "no_multi_tail_collision",
            "status": "closed_for_P_ge_23",
            "statement": "P>=23 时低筛骨架中不存在两个尾素因子的多尾碰撞。",
        },
        {
            "name": "prime_cofactor_identity",
            "status": "closed_for_P_ge_23",
            "statement": "P>=23 时一尾项唯一形如 P^2+r=ell*m, y<ell<P<m，且 m 为素数。",
        },
        {
            "name": "three_reciprocal_floor_curves",
            "status": "closed",
            "statement": "每个一尾项落在三条曲线 m=floor(P^2/ell)+s, s=1,2,3 上。",
        },
        {
            "name": "dimension_gap_equivalence",
            "status": "closed_as_reduction",
            "statement": "若 G(P)>B(P)，则存在低筛骨架点逃出所有尾素数，因位于 (P^2,(P+1)^2) 内而为素数。",
        },
    ]


def barrier_rows() -> list[dict[str, str]]:
    """列出有限 CRT 平方相位不能闭合的理由。"""
    return [
        {
            "name": "finite_square_phase_flexibility",
            "status": "closed_barrier",
            "statement": "对任意有限小素数集合 S 和任意非零平方相位选择，CRT 给出 P 的同余类实现这些 P^2 mod q。",
        },
        {
            "name": "dirichlet_prime_realization",
            "status": "closed_barrier",
            "statement": "只要 CRT 类与模数互素，Dirichlet 定理给出无限多个素数 P 落在该类中。",
        },
        {
            "name": "no_finite_local_contradiction",
            "status": "closed_barrier",
            "statement": "因此任何只检查有限小模平方相位的论证都不能推出全局矛盾；必须使用随 P 增长的筛余量或 PDEC 异常。",
        },
    ]


def attack_rows() -> list[dict[str, str]]:
    """列出剩余可攻目标。"""
    return [
        {
            "target": DIMENSION_GAP,
            "formula": "G(P)-B(P)>0",
            "route": "直接维数差；若成立则平方后短窗有素数。",
            "status": "open",
        },
        {
            "target": LDG,
            "formula": "G(P)>=0.48 P/log P",
            "route": "低模骨架下界；失败进入 LowSkeletonDeficit/PDEC。",
            "status": "open",
        },
        {
            "target": RFP,
            "formula": "B(P)<=1.50 P/log^2 P",
            "route": "三条倒数地板素-素曲线上界；失败进入 TailAnchor/PDEC。",
            "status": "open",
        },
        {
            "target": "finite_low_band",
            "formula": "P<=2003 checked",
            "route": "低段已有有限端点素数与 G-B 正余量证书。",
            "status": "closed_finite",
        },
        {
            "target": "dimension_constants",
            "formula": "1.50/0.48=3.125<log(23)",
            "route": "若 LDG/RFP 常数从 P>=23 成立，则全局闭合。",
            "status": "closed_conditional",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "SquarePhaseReducedToDimensionGap",
            True,
            True,
            "x=P 全覆盖已压成低筛骨架被三条素-素互补曲线完美吃掉；G(P)>B(P) 即闭合。",
            DIMENSION_GAP,
        ),
        row(
            "FiniteCRTPhaseContradictionExcluded",
            True,
            True,
            "有限平方相位模式可由素数 P 的 CRT 类实现，不能作为终端矛盾来源。",
            f"not {FINITE_CRT}",
        ),
        row(
            "LowBandFiniteCertificateImported",
            True,
            False,
            "P<=2003 的有限端点素数和 G-B 正余量证书可用，但不替代尾段解析证明。",
            "tail P>=2003",
        ),
        row(
            "LDGLowerCurrentCorpusProved",
            False,
            False,
            "低筛骨架下界仍未从作者侧全局证明。",
            f"{LDG} OR {LOW_DEFECT}",
        ),
        row(
            "RFPUpperCurrentCorpusProved",
            False,
            False,
            "三条倒数地板素对上界仍未以 1.50 常数闭合。",
            f"{RFP} OR {TAIL_DEFECT}",
        ),
        row(
            "SquarePhaseRoughSurvivorUniformLowerBoundProved",
            False,
            False,
            "维数差条件已清楚，但 LDG 与 RFP 两个常数输入尚未同时闭合。",
            f"({LDG} AND {RFP}) OR ({LOW_DEFECT} AND {TAIL_DEFECT})",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "尚未得到全局无条件终端矛盾。",
            f"{DIMENSION_GAP} OR {NONFINAL}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 square-phase 维数差攻坚证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_dimension_gap_attack_router",
        "status": "square_phase_reduced_to_dimension_gap_ldg_rfp_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "square_phase_reduced_to_dimension_gap": True,
        "finite_crt_square_phase_contradiction_excluded": True,
        "low_band_finite_certificate_imported": True,
        "ldg_lower_current_corpus_proved": False,
        "rfp_upper_current_corpus_proved": False,
        "square_phase_rough_survivor_uniform_lower_bound_proved": False,
        "first_half_prime_square_input_current_corpus_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SQUARE_PHASE,
        "hardpoint_after_router": f"{DIMENSION_GAP}: ({LDG} AND {RFP}) OR PDEC/SAE defects",
        "next_direct_attack_target": LDG,
        "parallel_attack_targets": [RFP, LOW_DEFECT, TAIL_DEFECT, NONFINAL],
        "reduction_rows": reduction_rows(),
        "barrier_rows": barrier_rows(),
        "attack_rows": attack_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SquarePhaseRoughSurvivorUniformLowerBound` 已被进一步压缩："
            "x=P 的小素数全覆盖等价于低筛骨架 `G(P)` 被一尾素-素互补曲线完美覆盖。"
            "对 `P>=23`，多尾碰撞消失，互补因子必为素数，且只落在三条倒数地板曲线。"
            "因此若能证明 `G(P)>B(P)`，平方后前半窗立即有素数。"
            "同时，有限 CRT 平方相位不能产生矛盾，因为任意有限平方相位模式可由无限多个素数 P 实现。"
            "真正剩余不是局部同余，而是 `LDG-Lower` 与 `RFP-Upper` 的尾段常数证明，"
            "或证明任一失败会生成 PDEC/SAE/预算缺陷。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase 维数差攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"square_phase_reduced_to_dimension_gap={fmt_bool(result['square_phase_reduced_to_dimension_gap'])}",
        f"finite_crt_square_phase_contradiction_excluded={fmt_bool(result['finite_crt_square_phase_contradiction_excluded'])}",
        f"ldg_lower_current_corpus_proved={fmt_bool(result['ldg_lower_current_corpus_proved'])}",
        f"rfp_upper_current_corpus_proved={fmt_bool(result['rfp_upper_current_corpus_proved'])}",
        f"square_phase_rough_survivor_uniform_lower_bound_proved={fmt_bool(result['square_phase_rough_survivor_uniform_lower_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压缩链",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["reduction_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")
    lines.extend(
        [
            "",
            "## 2. 有限 CRT 障碍",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["barrier_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")
    lines.extend(
        [
            "",
            "## 3. 剩余攻坚目标",
            "",
            "| target | formula | route | status |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["attack_rows"]:
        lines.append(
            f"| `{item['target']}` | `{table_cell(item['formula'])}` | "
            f"{table_cell(item['route'])} | `{item['status']}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一步",
            "",
            f"- 主攻 `{LDG}`：证明 `G(P)>=0.48P/logP`，或把低模骨架亏损路由到 `{LOW_DEFECT}`。",
            f"- 并行攻 `{RFP}`：证明 `B(P)<=1.50P/log^2P`，或把素对过密路由到 `{TAIL_DEFECT}`。",
            "- 不再寻找有限小模 CRT 直接矛盾；该路由已被素数 CRT 灵活性排除。",
            "",
            "## 6. 依赖哈希",
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
                "square_phase_reduced_to_dimension_gap": result["square_phase_reduced_to_dimension_gap"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
