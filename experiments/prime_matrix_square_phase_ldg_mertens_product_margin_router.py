#!/usr/bin/env python3
"""生成 square-phase LDG 显式 Mertens 乘积余量路由证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_ldg_mertens_product_margin_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-ldg-mertens-product-margin-router.json

输出：
  docs/monograph/prime-matrix-square-phase-ldg-mertens-product-margin-router.json
  docs/monograph/prime-matrix-square-phase-ldg-mertens-product-margin-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-ldg-mertens-product-margin-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-ldg-mertens-product-margin-router.md"

EULER_GAMMA = 0.5772156649015328606
E_GAMMA = math.exp(EULER_GAMMA)
RS_C = 2.50637
CG = 0.48
P0 = 2003

MERTENS_LEDGER = "ExplicitMertensProductLedgerForYEqualsFloorPOverE"
PHASE_DEFECT = "NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC"

SOURCE_FILES = [
    "prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json",
    "prime-matrix-square-phase-ldg-beta-level-barrier-router.json",
    "prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md",
    "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.md",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_ldg_mertens_product_margin_router.py": sha256(
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


def rs_product_lower_bound(x: float) -> float:
    """Rosser-Schoenfeld 型外部乘积下界。"""
    log_x = math.log(x)
    return 1.0 / (E_GAMMA * log_x + RS_C / log_x)


def target_lower_bound(p: int) -> float:
    """LDG 常数目标中的乘积密度。"""
    return CG / math.log(p)


def sample_rows() -> list[dict[str, Any]]:
    """给出样本余量读数。"""
    rows = []
    for p in [2003, 5003, 10007, 20011, 100000, 1000000, 10000000]:
        y = math.floor(p / math.e)
        lower = rs_product_lower_bound(y)
        target = target_lower_bound(p)
        rows.append(
            {
                "p": p,
                "y": y,
                "rs_lower": lower,
                "target": target,
                "surplus": lower - target,
                "ratio": lower / target,
            }
        )
    return rows


def proof_inequality_rows() -> list[dict[str, Any]]:
    """登记单调不等式所需数值。"""
    l0 = math.log(P0)
    t0 = l0 - 1.0
    f0 = l0 - CG * (E_GAMMA * t0 + RS_C / t0)
    derivative_lower = 1.0 - CG * E_GAMMA
    derivative_exact_at_l0 = 1.0 - CG * (E_GAMMA - RS_C / (t0 * t0))
    return [
        {
            "name": "L0",
            "value": l0,
            "meaning": "L=log P at P0=2003",
        },
        {
            "name": "t0",
            "value": t0,
            "meaning": "t=L-1 upper bound for log floor(P/e)",
        },
        {
            "name": "F(L0)",
            "value": f0,
            "meaning": "F(L)=L-0.48(e^gamma(L-1)+2.50637/(L-1))",
        },
        {
            "name": "coarse_derivative_lower",
            "value": derivative_lower,
            "meaning": "1-0.48e^gamma; positive lower bound for F'(L) after dropping the positive term",
        },
        {
            "name": "exact_derivative_at_L0",
            "value": derivative_exact_at_l0,
            "meaning": "F'(L0), also positive",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "RosserSchoenfeldProductInequalityMatched",
            "closed": True,
            "proved": False,
            "meaning": "若接受外部乘积不等式 prod_{q<=x}(1-1/q)>1/(e^gamma log x+2.50637/log x)，则可接入本门。",
            "remaining": "external theorem accepted OR self-contained proof",
        },
        {
            "gate": "AlgebraicMarginForPGe2003Closed",
            "closed": True,
            "proved": True,
            "meaning": "用 y=floor(P/e)<=P/e 与单调性，P>=2003 时外部乘积下界严格大于 0.48/logP。",
            "remaining": "none",
        },
        {
            "gate": "ExplicitMertensProductLedgerExternalClosed",
            "closed": True,
            "proved": False,
            "meaning": "在接受 Rosser-Schoenfeld 外部输入时，LDG 主项常数余量关闭。",
            "remaining": "self-contained Rosser-Schoenfeld/Dusart proof appendix if strict route",
        },
        {
            "gate": "LDGLowerStillNeedsPhaseDiscrepancy",
            "closed": False,
            "proved": False,
            "meaning": "完整周期主项余量不等于短区间实际 G(P) 下界；还需排斥负平方相位覆盖过量。",
            "remaining": PHASE_DEFECT,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "没有排除相位亏损和 RFP 过密出口，不能声明行/列命题无条件闭合。",
            "remaining": "NegativeSquarePhase defect AND ReciprocalFloor defect exclusions",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 Mertens 乘积余量证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_ldg_mertens_product_margin_router",
        "status": "ldg_mertens_product_margin_external_closed_phase_discrepancy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "rosser_schoenfeld_product_inequality_matched": True,
        "algebraic_margin_for_p_ge_2003_closed": True,
        "explicit_mertens_product_ledger_external_closed": True,
        "explicit_mertens_product_ledger_self_contained_proved": False,
        "ldg_lower_current_corpus_proved": False,
        "negative_square_phase_defect_excluded": False,
        "row_column_unconditional_closed": False,
        "constants": {
            "euler_gamma": EULER_GAMMA,
            "e_gamma": E_GAMMA,
            "rs_c": RS_C,
            "c_g": CG,
            "p0": P0,
        },
        "sample_rows": sample_rows(),
        "proof_inequality_rows": proof_inequality_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": PHASE_DEFECT,
        "plain_conclusion": (
            "接受 Rosser-Schoenfeld 型外部 Mertens 乘积不等式时，"
            "`y=floor(P/e)` 的完整周期密度从 `P>=2003` 起严格高于 `0.48/logP`。"
            "代数余量本身很宽，因此 LDG 剩余不再是主项常数，而是短区间负平方相位"
            "实际计数 `G(P)` 相对完整周期主项的亏损。严格自足路线仍需内联该外部乘积不等式的证明。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase LDG Mertens 乘积余量路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"rosser_schoenfeld_product_inequality_matched={fmt_bool(result['rosser_schoenfeld_product_inequality_matched'])}",
        f"algebraic_margin_for_p_ge_2003_closed={fmt_bool(result['algebraic_margin_for_p_ge_2003_closed'])}",
        f"explicit_mertens_product_ledger_external_closed={fmt_bool(result['explicit_mertens_product_ledger_external_closed'])}",
        f"explicit_mertens_product_ledger_self_contained_proved={fmt_bool(result['explicit_mertens_product_ledger_self_contained_proved'])}",
        f"ldg_lower_current_corpus_proved={fmt_bool(result['ldg_lower_current_corpus_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部输入",
        "",
        "使用的外部口径为 Rosser-Schoenfeld/Dusart 型显式 Mertens 乘积下界：",
        "",
        "```text",
        "prod_{q<=x}(1-1/q) > 1/(e^gamma log x + 2.50637/log x).",
        "```",
        "",
        "本文件只完成该输入与 LDG 常数的参数匹配；若走严格自足路线，还必须内联证明该外部不等式。",
        "",
        "## 2. 余量样本",
        "",
        "| P | y=floor(P/e) | RS lower | 0.48/logP | surplus | ratio |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["sample_rows"]:
        lines.append(
            f"| {item['p']} | {item['y']} | {item['rs_lower']:.12f} | "
            f"{item['target']:.12f} | {item['surplus']:.12f} | {item['ratio']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 3. 单调代数",
            "",
            "令 `L=logP`。因 `floor(P/e)<=P/e` 且乘积下界分母在本区间单调递增，只需验证",
            "",
            "```text",
            "F(L)=L-0.48(e^gamma(L-1)+2.50637/(L-1)) > 0.",
            "```",
            "",
            "`P>=2003` 时 `L>=log2003`，且 `F(log2003)>0`、`F'(L)>0`，故全尾段成立。",
            "",
            "| item | value | meaning |",
            "| --- | ---: | --- |",
        ]
    )
    for item in result["proof_inequality_rows"]:
        lines.append(f"| `{item['name']}` | {item['value']:.12f} | {table_cell(item['meaning'])} |")
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
            f"- 主项常数余量在外部 Mertens 输入下已经不是硬点；继续攻 `{PHASE_DEFECT}`。",
            "- 严格自足路线若不接受外部输入，则需补 `SelfContainedRosserSchoenfeldMertensProductProofAppendix`。",
            "- 即使 Mertens 主项关闭，LDG 仍需证明短区间负平方相位实际亏损不会吞掉该余量。",
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
                "algebraic_margin_for_p_ge_2003_closed": result["algebraic_margin_for_p_ge_2003_closed"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
