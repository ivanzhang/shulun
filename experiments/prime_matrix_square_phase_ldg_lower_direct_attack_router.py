#!/usr/bin/env python3
"""生成 square-phase 的 LDG-Lower 直接下钻证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_ldg_lower_direct_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-ldg-lower-direct-attack-router.json

输出：
  docs/monograph/prime-matrix-square-phase-ldg-lower-direct-attack-router.json
  docs/monograph/prime-matrix-square-phase-ldg-lower-direct-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-ldg-lower-direct-attack-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-ldg-lower-direct-attack-router.md"

LDG = "LDG-Lower"
RFP = "RFP-Upper"
DIMENSION_GAP = "PostSquareEndpointDimensionGapGMinusBPositive"
LOW_DEFECT = "LowSkeletonDeficitPDECOrSAE"
BETA_REMAINDER = "SquarePhaseBetaSieveRemainderBound"
FINITE_CRT = "FiniteSquarePhaseCRTContradiction"
NONFINAL = "NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction"

SOURCE_FILES = [
    "prime-matrix-square-phase-dimension-gap-attack-router.json",
    "prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md",
    "prime-matrix-prime-square-x-equals-p-wheel-router.json",
    "prime-matrix-prime-base-exponent-half-barrier-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_ldg_lower_direct_attack_router.py": sha256(
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
    """列出 LDG 下筛公式。"""
    return [
        {
            "name": "low_skeleton",
            "formula": "G(P)=#{1<=r<P: r != -P^2 mod q for every prime q<=y}",
            "status": "closed_definition",
        },
        {
            "name": "crt_residue_for_d",
            "formula": "for squarefree d|Q_y, a_d == -P^2 mod d is the unique forbidden CRT class",
            "status": "closed",
        },
        {
            "name": "exact_inclusion_exclusion",
            "formula": "G(P)=sum_{d|Q_y} mu(d) N_d(P), N_d(P)=#{1<=r<P: r==a_d mod d}",
            "status": "closed_identity",
        },
        {
            "name": "mertens_main",
            "formula": "P*prod_{q<=y}(1-1/q) ~ e^{-gamma} P/log y",
            "status": "closed_main_term_shape",
        },
        {
            "name": "ldg_target",
            "formula": "G(P)>=0.48 P/log P",
            "status": "open_lower_bound",
        },
    ]


def obstruction_rows() -> list[dict[str, str]]:
    """列出不能闭合的路径和剩余。"""
    return [
        {
            "obstruction": "full inclusion-exclusion too wide",
            "detail": "d|Q_y 有 2^pi(y) 个项；单纯逐项误差 O(1) 无法求和。",
            "route": "use lower beta-sieve weights supported on d<=D",
        },
        {
            "obstruction": "finite CRT phase no contradiction",
            "detail": "任意有限平方相位可由素数 P 实现，不能靠有限模排除坏相位。",
            "route": "must prove growing sieve remainder bound",
        },
        {
            "obstruction": "interval length equals P",
            "detail": "窗口长度与筛到 y~P/e 同阶，余项纪律是核心而非常数微调。",
            "route": BETA_REMAINDER,
        },
        {
            "obstruction": "if LDG fails",
            "detail": "G(P) 低于主项安全常数，等价于固定负平方相位的低模骨架持续负偏。",
            "route": LOW_DEFECT,
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "LDGTargetImportedFromDimensionGap",
            True,
            True,
            "维数差闭合需要 LDG-Lower 与 RFP-Upper；本步专攻 LDG。",
            LDG,
        ),
        row(
            "ExactSquarePhaseInclusionExclusionClosed",
            True,
            True,
            "G(P) 已写成固定负平方相位的精确 CRT inclusion-exclusion。",
            BETA_REMAINDER,
        ),
        row(
            "FiniteLocalCRTContradictionRejected",
            True,
            True,
            "有限相位模式可由素数 P 实现，不能作为 LDG 的终端矛盾。",
            f"not {FINITE_CRT}",
        ),
        row(
            "BetaSieveRemainderBoundProved",
            False,
            False,
            "尚未证明下筛权余项足够小，从而保留 0.48P/logP 的低骨架。",
            BETA_REMAINDER,
        ),
        row(
            "LDGLowerCurrentCorpusProved",
            False,
            False,
            "LDG 的主项形态和失败路由清楚，但尾段全局不等式未闭合。",
            f"{BETA_REMAINDER} OR {LOW_DEFECT}",
        ),
        row(
            "SquarePhaseDimensionGapClosed",
            False,
            False,
            "即便 LDG 闭合，仍需并行 RFP-Upper；本步不声明最终命题。",
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
    """构造 LDG-Lower 下钻证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_ldg_lower_direct_attack_router",
        "status": "ldg_lower_reduced_to_square_phase_beta_sieve_remainder_or_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "ldg_target_imported": True,
        "exact_square_phase_inclusion_exclusion_closed": True,
        "finite_local_crt_contradiction_rejected": True,
        "beta_sieve_remainder_bound_proved": False,
        "ldg_lower_current_corpus_proved": False,
        "square_phase_dimension_gap_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": LDG,
        "hardpoint_after_router": f"{BETA_REMAINDER} OR {LOW_DEFECT}",
        "next_direct_attack_target": BETA_REMAINDER,
        "parallel_attack_targets": [LOW_DEFECT, RFP, NONFINAL],
        "formula_rows": formula_rows(),
        "obstruction_rows": obstruction_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`LDG-Lower` 已下钻为一个明确的下筛余项问题："
            "`G(P)` 是避开所有 `q<=P/e` 的负平方相位禁类的列数，"
            "可精确写成 `sum mu(d)N_d(P)`。Mertens 主项自然给 "
            "`e^{-gamma}P/logP`，而目标常数 `0.48` 留出安全余量。"
            "但全 inclusion-exclusion 过宽，有限 CRT 相位也不能给矛盾；"
            "真正剩余是证明 square-phase beta-sieve 余项受控，"
            "或把 `G(P)<0.48P/logP` 的持续负偏抽取为 LowSkeletonDeficit/PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase LDG-Lower 直接下钻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_square_phase_inclusion_exclusion_closed={fmt_bool(result['exact_square_phase_inclusion_exclusion_closed'])}",
        f"finite_local_crt_contradiction_rejected={fmt_bool(result['finite_local_crt_contradiction_rejected'])}",
        f"beta_sieve_remainder_bound_proved={fmt_bool(result['beta_sieve_remainder_bound_proved'])}",
        f"ldg_lower_current_corpus_proved={fmt_bool(result['ldg_lower_current_corpus_proved'])}",
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
            f"- 主攻 `{BETA_REMAINDER}`：构造下筛权并证明固定负平方相位的加权余项不吞掉 `0.48P/logP` 余量。",
            f"- 若余项异常偏负，则抽取 `{LOW_DEFECT}` 并接回 PDEC/SAE。",
            f"- 并行保留 `{RFP}`；维数差最终需要 LDG 与 RFP 同时闭合。",
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
                "ldg_lower_current_corpus_proved": result["ldg_lower_current_corpus_proved"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
