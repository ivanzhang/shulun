#!/usr/bin/env python3
"""生成二级/triple LPF 压力的迭代 LPF 秩预算证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_iterated_lpf_rank_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json",
]

PREVIOUS_TARGET = "SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC"
TRIPLE_IMPORT = "SecondLPFTriplePressureImportedLedger"
ORDERED_CHAIN = "IteratedLPFOrderedRoughResidualChainLedger"
SUPPORT_PRODUCT = "LPFSupportProductReciprocityInvariantLedger"
RANK_BUDGET = "LPFDepthRankBudgetLedger"
CRT_WORD = "IteratedLPFCRTWordCellLedger"
PRODUCT_WIDTH = "IteratedLPFProductWidthColumnCRTExitLedger"
TERMINAL_ATOM = "TerminalResidualFiniteAtomLedger"
NO_CYCLE = "IteratedLPFWellFoundedNoCycleLedger"
NEW_TARGET = "RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC"

REDUCED_TARGET = (
    f"{TRIPLE_IMPORT} AND {ORDERED_CHAIN} AND {SUPPORT_PRODUCT} "
    f"AND {RANK_BUDGET} AND {CRT_WORD} AND {PRODUCT_WIDTH} "
    f"AND {TERMINAL_ATOM} AND {NO_CYCLE} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve()] + SOURCE_FILES
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的二级/triple 压力替换成秩预算分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造迭代 LPF 秩预算判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "SecondLPFTriplePressureImported",
            imported,
            False,
            "上一层把 fixed-pair rough-m pressure 的剩余压到二级 LPF/triple rough-t pressure。",
            PREVIOUS_TARGET,
        ),
        row(
            "IteratedLPFOrderedResidualChainClosed",
            True,
            True,
            "从 residual n_0 开始，若 n_i>1 令 a_i=lpf(n_i)，n_i=a_i n_{i+1}；由 rough 条件得 a_i 非降且 a_i>=r。",
            ORDERED_CHAIN,
        ),
        row(
            "LPFSupportProductReciprocityClosed",
            True,
            True,
            "经过含初始 s 的因子词 A_h=s*prod a_i 后，残余支撑宽度至多 ceil(width_m/A_h)；CRT 周期乘积增大时支撑同步收缩。",
            SUPPORT_PRODUCT,
        ),
        row(
            "LPFDepthRankBudgetClosed",
            True,
            True,
            "非有限分支 r>=2。令 d 为含 s 的总因子深度；若 A_h<=width_m，则 d<=floor(log_r(width_m))；超过该预算即落入单点/有限原子。",
            RANK_BUDGET,
        ),
        row(
            "IteratedLPFCRTWordCellClosed",
            True,
            True,
            "每个有限因子词给出一个确定的 MCRT phase word；相位复现只能沿该词的合成模数周期发生。",
            CRT_WORD,
        ),
        row(
            "IteratedProductWidthExitClosed",
            True,
            True,
            "若活动因子词的合成模数乘积超过原 m 支撑宽度，则同一相位字至多命中孤立原子，并登记 ColumnCRT/PDEC。",
            PRODUCT_WIDTH,
        ),
        row(
            "TerminalResidualFiniteAtomClosed",
            True,
            True,
            "当 residual 支撑宽度降到 1 或 residual=1 时，分支变成固定 q 的有限原子。",
            TERMINAL_ATOM,
        ),
        row(
            "IteratedLPFNoCycleClosed",
            True,
            True,
            "秩函数 (support width, residual product) 在每次真实 LPF 展开中良序下降，排除同尺度循环。",
            NO_CYCLE,
        ),
        row(
            "RankBudgetedMovingFamilyStillOpen",
            False,
            False,
            "仍未排除随 P 移动的低秩 LPF 因子词族；本步只把 triple pressure 压成有显式秩预算的 moving-family/ColumnCRT 出口。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥秩预算化 moving-family，或证明其必回流为 ColumnCRT/PDEC/SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造迭代 LPF 秩预算证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json")
    latest_basis = replace_latest_basis(previous)
    rows = build_rows(previous)
    plain = (
        "二级/triple rough-t pressure 被改写成迭代 LPF 因子词。"
        "每加入一个 least-prime-factor，合成 CRT 周期乘积同步扩大，而 residual 支撑宽度按该乘积收缩。"
        "因此同一尺度上不可能无限循环；若周期乘积超过支撑宽度，只剩 ColumnCRT/PDEC 或有限原子。"
        "剩余不是自由 triple pressure，而是有显式深度预算的 moving-family。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_iterated_lpf_rank_budget_router",
        "status": "second_lpf_triple_pressure_reduced_to_rank_budgeted_iterated_lpf_family_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "second_lpf_triple_pressure_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "ordered_residual_chain_closed": True,
        "support_product_reciprocity_closed": True,
        "depth_rank_budget_closed": True,
        "iterated_crt_word_cell_closed": True,
        "product_width_exit_closed": True,
        "terminal_residual_finite_atom_closed": True,
        "well_founded_no_cycle_closed": True,
        "rank_budgeted_moving_family_excluded": False,
        "row_column_unconditional_closed": False,
        "iterated_lpf_formulas": {
            "initial_cell": "q=ell*r*m, m=s*t, s=lpf(m)>=r, gcd(t,W_<s)=1",
            "recursive_step": "n_i>1 => a_i=lpf(n_i), n_i=a_i*n_{i+1}, gcd(n_{i+1},W_<a_i)=1",
            "ordered_factors": "r<=s<=a_1<=a_2<=... with repetitions allowed",
            "factor_word_product": "A_h=s*prod_{i<=h} a_i",
            "support_reciprocity": "width(n_h-support)<=ceil(width_m/A_h)",
            "rank_budget": "A_h<=width_m and all factors >=r>=2 => total_depth d<=floor(log_r(width_m))",
            "crt_word": "phase period divides/contains product of active LPF word moduli",
            "product_width_exit": "active word modulus product > width_m => ColumnCRT/PDEC or finite atom",
            "new_failure": "rank-budgeted iterated LPF moving family or ColumnCRT/PDEC",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix iterated-LPF rank-budget 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"second_lpf_triple_pressure_imported={fmt_bool(cert['second_lpf_triple_pressure_imported'])}",
        f"ordered_residual_chain_closed={fmt_bool(cert['ordered_residual_chain_closed'])}",
        f"support_product_reciprocity_closed={fmt_bool(cert['support_product_reciprocity_closed'])}",
        f"depth_rank_budget_closed={fmt_bool(cert['depth_rank_budget_closed'])}",
        f"iterated_crt_word_cell_closed={fmt_bool(cert['iterated_crt_word_cell_closed'])}",
        f"product_width_exit_closed={fmt_bool(cert['product_width_exit_closed'])}",
        f"terminal_residual_finite_atom_closed={fmt_bool(cert['terminal_residual_finite_atom_closed'])}",
        f"well_founded_no_cycle_closed={fmt_bool(cert['well_founded_no_cycle_closed'])}",
        f"rank_budgeted_moving_family_excluded={fmt_bool(cert['rank_budgeted_moving_family_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 从 triple cell 到因子词",
        "",
        "上一层剩余为二级 LPF/triple rough-t pressure。固定 `(r,ell,s)` 后：",
        "",
        "```text",
        "q=ell*r*m,",
        "m=s*t,",
        "s=lpf(m)>=r,",
        "gcd(t,W_<s)=1.",
        "```",
        "",
        "若 residual `n_i>1`，递归取：",
        "",
        "```text",
        "a_i=lpf(n_i),",
        "n_i=a_i*n_{i+1},",
        "gcd(n_{i+1},W_<a_i)=1.",
        "```",
        "",
        "于是 LPF 因子词满足：",
        "",
        "```text",
        "r<=s<=a_1<=a_2<=...",
        "```",
        "",
        "允许重复；重复只表示同一素因子的幂次继续消耗 residual。",
        "",
        "## 2. 支撑-周期互反不变量",
        "",
        "令：",
        "",
        "```text",
        "A_h=s*prod_{i<=h}a_i.",
        "```",
        "",
        "原 m 支撑宽度为 `width_m`。经过因子词 `A_h` 后，残余支撑满足：",
        "",
        "```text",
        "width(n_h-support)<=ceil(width_m/A_h).",
        "```",
        "",
        "这就是当前最关键的非循环结构：CRT 周期乘积越大，能承载同一相位字的 residual 支撑越小。",
        "",
        "## 3. 秩预算",
        "",
        "非有限分支中 `r>=2`，且每个新增因子都至少为 `r`。因此若仍未进入 product-width 出口，必须有：",
        "",
        "```text",
        "A_h<=width_m.",
        "```",
        "",
        "从而：",
        "",
        "```text",
        "d<=floor(log_r(width_m)).",
        "```",
        "",
        "这里 `d` 是包含初始二级因子 `s` 的总因子深度。所以 triple pressure 不能隐藏成无限 LPF 塔；它只能是有限秩、有限深的因子词 moving-family。",
        "",
        "## 4. product-width 出口",
        "",
        "若某一活动因子词的合成模数乘积超过原支撑宽度：",
        "",
        "```text",
        "M_word>width_m,",
        "```",
        "",
        "则同一相位字在该支撑内至多命中孤立有限原子，必须登记为 ColumnCRT/PDEC 或有限原子。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        PREVIOUS_TARGET,
        "  -> " + TRIPLE_IMPORT,
        "  AND " + ORDERED_CHAIN,
        "  AND " + SUPPORT_PRODUCT,
        "  AND " + RANK_BUDGET,
        "  AND " + CRT_WORD,
        "  AND " + PRODUCT_WIDTH,
        "  AND " + TERMINAL_ATOM,
        "  AND " + NO_CYCLE,
        "  AND " + NEW_TARGET,
        "```",
        "",
        "剩余从自由 triple pressure 变成秩预算化迭代 LPF moving-family，或 ColumnCRT/PDEC。",
        "",
        "## 6. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(item["gate"]),
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 7. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 8. 诚实边界",
            "",
            "- 本证书没有证明秩预算化 moving-family 不可能。",
            "- 本证书只证明二级/triple pressure 必须服从支撑-周期互反不变量与有限秩预算。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 9. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """生成全部证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
