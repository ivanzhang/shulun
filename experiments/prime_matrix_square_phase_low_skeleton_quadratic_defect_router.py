#!/usr/bin/env python3
"""生成 square-phase 低骨架负平方相位缺陷路由证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_low_skeleton_quadratic_defect_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json

输出：
  docs/monograph/prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json
  docs/monograph/prime-matrix-square-phase-low-skeleton-quadratic-defect-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-low-skeleton-quadratic-defect-router.md"

CG = 0.48
E_GAMMA_INV = math.exp(-0.5772156649015328606)

LOW_DEFECT = "LowSkeletonDeficitPDECOrSAE"
QUAD_DEFECT = "NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC"
MERTENS_LEDGER = "ExplicitMertensProductLedgerForYEqualsFloorPOverE"

SOURCE_FILES = [
    "prime-matrix-square-phase-nearfull-rough-primevoid-dichotomy-router.json",
    "prime-matrix-square-phase-ldg-lower-direct-attack-router.json",
    "prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md",
    "prime-matrix-eda-diagonal-quadratic-phase-lock.md",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_low_skeleton_quadratic_defect_router.py": sha256(
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


def margin_rows() -> list[dict[str, Any]]:
    """给出 Mertens 主项相对 0.48 目标的启发余量。"""
    rows = []
    for p in [2003, 10007, 100000, 1000003, 10000019]:
        y = math.floor(p / math.e)
        main_shape = E_GAMMA_INV * p / math.log(y)
        target = CG * p / math.log(p)
        rows.append(
            {
                "p": p,
                "y": y,
                "mertens_shape": main_shape,
                "target": target,
                "shape_surplus": main_shape - target,
                "relative_surplus": (main_shape - target) / main_shape,
            }
        )
    return rows


def defect_rows() -> list[dict[str, str]]:
    """列出低骨架缺陷的精确结构。"""
    return [
        {
            "name": "negative_square_residue",
            "formula": "q | P^2+k iff k == -P^2 mod q",
            "meaning": "每个小素数只删除一个由 P 锁定的负平方相位。",
        },
        {
            "name": "legendre_lock",
            "formula": "q | P^2+k and q not| k => chi_q(k)=chi_q(-1)",
            "meaning": "被覆盖列在每个命中模上满足固定二次字符方向。",
        },
        {
            "name": "low_skeleton",
            "formula": "G(P)=sum_{1<=k<P} prod_{q<=P/e} 1_{k!=-P^2 mod q}",
            "meaning": "低骨架是负平方相位单残基覆盖的精确补集。",
        },
        {
            "name": "deficit",
            "formula": "G(P)<0.48P/logP",
            "meaning": "负平方相位覆盖比完整周期密度多吞掉固定比例余量。",
        },
        {
            "name": "pdec_route",
            "formula": "persistent deficit => nonzero Fourier/character defect",
            "meaning": "若亏损持续且非有限 SAE，则必须产生可登记的相位偏置。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "LowSkeletonExactNegativeSquarePhase",
            True,
            True,
            "LDG 低骨架已精确写成 k 避开全部 -P^2 mod q 的单残基补集。",
            "none",
        ),
        row(
            "QuadraticCharacterLockImported",
            True,
            True,
            "若 q 覆盖 k 且 q 不整除 k，则 k 的 Legendre 方向被锁为 chi_q(-1)。",
            "none",
        ),
        row(
            "LDGFailureForcesQuadraticCoveringDefect",
            True,
            True,
            "若 G(P)<0.48P/logP，则负平方相位覆盖必须超过 Mertens 主项安全余量。",
            QUAD_DEFECT,
        ),
        row(
            "ExplicitMertensProductLedgerClosedForThisGate",
            False,
            False,
            "需要把 V(floor(P/e)) 与 0.48P/logP 的显式余量写成全阈值账本；当前只登记主项形状。",
            MERTENS_LEDGER,
        ),
        row(
            "NegativeSquarePhaseDefectExcluded",
            False,
            False,
            "尚未证明持续负平方相位覆盖过量不可能，也未排斥对应 PDEC/SAE。",
            QUAD_DEFECT,
        ),
        row(
            "LowSkeletonDeficitExcluded",
            False,
            False,
            "低骨架亏损出口仍未关闭。",
            f"{MERTENS_LEDGER} AND exclude {QUAD_DEFECT}",
        ),
        row(
            "DirectUnconditionalContradictionFound",
            False,
            False,
            "本步只把 LDG 亏损精确化为二次相位覆盖缺陷。",
            f"exclude {LOW_DEFECT}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合。",
            "LowSkeletonDeficit exclusion AND RFPExcess exclusion",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造低骨架二次缺陷证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_low_skeleton_quadratic_defect_router",
        "status": "low_skeleton_deficit_reduced_to_negative_square_phase_covering_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "low_skeleton_exact_negative_square_phase_closed": True,
        "quadratic_character_lock_imported": True,
        "ldg_failure_forces_quadratic_covering_defect": True,
        "explicit_mertens_product_ledger_closed_for_this_gate": False,
        "negative_square_phase_defect_excluded": False,
        "low_skeleton_deficit_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "margin_rows": margin_rows(),
        "defect_rows": defect_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": QUAD_DEFECT,
        "plain_conclusion": (
            "`LowSkeletonDeficit` 的最窄形式已经不是普通短区间筛下界，"
            "而是负平方相位单残基覆盖过量：每个 `q<=P/e` 只允许删除 `k=-P^2 mod q`。"
            "同时，任意被覆盖的非零列满足 Legendre 锁 `chi_q(k)=chi_q(-1)`。"
            "因此若 `G(P)<0.48P/logP` 在反例链中持续发生，必须表现为负平方相位覆盖的"
            "非零 Fourier/二次字符偏置，或进入有限 SAE。该出口尚未排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase 低骨架二次相位缺陷路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"low_skeleton_exact_negative_square_phase_closed={fmt_bool(result['low_skeleton_exact_negative_square_phase_closed'])}",
        f"quadratic_character_lock_imported={fmt_bool(result['quadratic_character_lock_imported'])}",
        f"negative_square_phase_defect_excluded={fmt_bool(result['negative_square_phase_defect_excluded'])}",
        f"low_skeleton_deficit_excluded={fmt_bool(result['low_skeleton_deficit_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 结构行",
        "",
        "| name | formula | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["defect_rows"]:
        lines.append(f"| `{item['name']}` | `{table_cell(item['formula'])}` | {table_cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 主项余量形状",
            "",
            "下表只登记 `e^{-gamma}P/log(floor(P/e))` 相对 `0.48P/logP` 的主项形状，不是显式 Mertens 证明。",
            "",
            "| P | y | Mertens shape | target | surplus | relative surplus |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["margin_rows"]:
        lines.append(
            f"| {item['p']} | {item['y']} | {item['mertens_shape']:.6f} | "
            f"{item['target']:.6f} | {item['shape_surplus']:.6f} | "
            f"{item['relative_surplus']:.6f} |"
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
            "- 直接攻 `NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC`：证明负平方相位覆盖过量会产生可排斥的 Fourier/Legendre 缺陷。",
            "- 补齐 `ExplicitMertensProductLedgerForYEqualsFloorPOverE`，把完整周期主项余量做成显式常数账本。",
            "- 该出口与 RFP 过密出口必须同时排除，才能闭合 square-phase 反例。",
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
                "low_skeleton_deficit_excluded": result["low_skeleton_deficit_excluded"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
