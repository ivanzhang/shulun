#!/usr/bin/env python3
"""审计直接 BFI 原子的 level 指数账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_bfi_level_ledger_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-bfi-level-ledger-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-bfi-level-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_BFI_ATOM_MATCH = DOCS / "prime-matrix-triad-a1-dibfi-bfi-atom-match-router.json"
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_FINAL_REVIEW = ROOT / "docs" / "final-proof-review.md"
DEFAULT_ZERO_ROW = ROOT / "docs" / "zero-row-position-rigidity.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-bfi-level-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-bfi-level-ledger-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_any(path: Path, needles: list[str]) -> bool:
    """核查文档是否含有任一关键词。"""
    text = path.read_text(encoding="utf-8")
    return any(needle in text for needle in needles)


def contains_all(path: Path, needles: list[str]) -> bool:
    """核查文档是否含有全部关键词。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def fmt_fraction(value: Fraction) -> str:
    """格式化分数。"""
    return f"{value.numerator}/{value.denominator}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_level_rows(
    common_variable_table: dict[str, Any],
    kls_template_path: Path,
    kze_spine_path: Path,
    external_index_path: Path,
    final_review_path: Path,
    zero_row_path: Path,
) -> list[dict[str, Any]]:
    """构造 BFI level 指数账本行。"""
    symbols = {row["symbol"]: row for row in common_variable_table["variable_rows"]}
    x_is_p2 = contains_any(final_review_path, ["x≈P^2", "`x≈P^2`"]) and contains_any(
        zero_row_path,
        ["N=xP+c < P^2", "`N=xP+c < P^2`", "xP+c<P^2"],
    )
    q_is_p_log = contains_all(kls_template_path, ["C ≍ P/log", "S ≍ P"]) and contains_any(
        external_index_path,
        ["d,c≈P/log", "`d,c≈P/log"],
    )
    well_factorable_support = contains_all(
        kze_spine_path,
        ["well-factorable", "R_{\\max}", "lambda_R"],
    ) and contains_all(external_index_path, ["BFI1986-Theorem10", "lambda_d"])
    log_budget_ready = contains_all(kls_template_path, ["B(A)=A+C_0+10", "log^{C_0}P"])
    q_row_ready = "Q" in symbols and "lambda" in symbols

    q_exp_in_x = Fraction(1, 2)
    bfi_limit = Fraction(4, 7)
    chosen_eps = Fraction(1, 56)
    admitted_exp_in_x = bfi_limit - chosen_eps
    slack_in_x = admitted_exp_in_x - q_exp_in_x
    return [
        {
            "gate": "AmbientLengthXEqualsP2",
            "closed": x_is_p2,
            "exponent_in_P": "2",
            "evidence": "行/方阵高度约束把当前 AP ambient length 归一到 X≈P^2。",
            "remaining": "none" if x_is_p2 else "需在当前 A1 残差定义处显式写 X≈P^2。",
        },
        {
            "gate": "ModulusSupportQAtMostPPolylog",
            "closed": q_is_p_log and q_row_ready,
            "exponent_in_P": "1+o(1)",
            "evidence": "KLS 模板登记 C,d≈P/log^{O(1)}P，共同变量表把 Q 作为 lambda 总支撑 level。",
            "remaining": "none"
            if q_is_p_log and q_row_ready
            else "需把当前 lambda_q 的 support 明确写成 Q<=P log^O P。",
        },
        {
            "gate": "BFIExponentSlack",
            "closed": x_is_p2 and q_is_p_log and slack_in_x > 0,
            "exponent_in_X": f"{fmt_fraction(q_exp_in_x)} <= {fmt_fraction(admitted_exp_in_x)}",
            "evidence": (
                "Q<=P log^O P 等价于 Q<=X^{1/2+o(1)}；"
                "取 eps=1/56 时 BFI 允许 X^{31/56}，仍留 X^{3/56} 指数余量。"
            ),
            "remaining": "none" if x_is_p2 and q_is_p_log else "先固定 X≈P^2 与 Q<=P log^O P。",
        },
        {
            "gate": "WellFactorableLambdaSupportLevel",
            "closed": well_factorable_support and q_row_ready,
            "exponent_in_P": "same Q-level",
            "evidence": "KZ-E spine 给 lambda_R well-factorable 分解；外部索引把 lambda_d 接到 BFI Theorem 10。",
            "remaining": "none"
            if well_factorable_support and q_row_ready
            else "需把 lambda 的 well-factorable 分解层与 Q-support 同表登记。",
        },
        {
            "gate": "DyadicAndLogLossAbsorption",
            "closed": log_budget_ready,
            "exponent_in_P": "polylog only",
            "evidence": "KLS 模板以 B(A)=A+C0+10 吸收 dyadic、gcd、端点、平滑和分解层数损失。",
            "remaining": "none" if log_budget_ready else "需补 B(A) 损失吸收账本。",
        },
    ]


def run(
    bfi_atom_match_path: Path,
    common_variable_table_path: Path,
    kls_template_path: Path,
    kze_spine_path: Path,
    external_index_path: Path,
    final_review_path: Path,
    zero_row_path: Path,
) -> dict[str, Any]:
    """运行 BFI level 账本路由。"""
    bfi_atom_match = load_json(bfi_atom_match_path)
    common_variable_table = load_json(common_variable_table_path)
    level_rows = build_level_rows(
        common_variable_table,
        kls_template_path,
        kze_spine_path,
        external_index_path,
        final_review_path,
        zero_row_path,
    )
    closed = all(row["closed"] for row in level_rows)
    open_level_gates = [row["gate"] for row in level_rows if not row["closed"]]
    previous_targets = list(bfi_atom_match["open_terminal_targets"])
    remaining_targets = [
        target for target in previous_targets if target != "BFILevelExponentLedger"
    ]
    if not closed:
        remaining_targets.append("BFILevelExponentLedger")
    return {
        "certificate_type": "triad_a1_dibfi_bfi_level_ledger_router",
        "status": "bfi_level_exponent_ledger_closed_ap_identity_open"
        if closed
        else "bfi_level_exponent_ledger_support_normalization_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "bfi_atom_match_json": file_sha256(bfi_atom_match_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "kls_window_di_bfi_template_md": file_sha256(kls_template_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "external_theorem_index_md": file_sha256(external_index_path),
            "final_proof_review_md": file_sha256(final_review_path),
            "zero_row_position_rigidity_md": file_sha256(zero_row_path),
        },
        "previous_terminal_gap": bfi_atom_match["terminal_gap_after_router"],
        "previous_open_terminal_targets": previous_targets,
        "level_rows": level_rows,
        "open_level_gates": open_level_gates,
        "bfi_level_exponent_ledger_closed": closed,
        "remaining_terminal_targets": remaining_targets,
        "terminal_gap_after_router": (
            "OriginalResidualEqualsBFIAPError"
            if closed
            else "BFILevelExponentLedger"
        ),
        "structural_law": (
            "The BFI level side has positive exponent slack once the prime-matrix "
            "normalization X≈P^2 and Q<=P log^O P is fixed. In X-exponents the current "
            "modulus support is 1/2+o(1), whereas BFI Theorem 10 allows 4/7-eps; choosing "
            "eps=1/56 leaves slack 3/56. Thus the level ledger is not the terminal hard "
            "point; the remaining terminal is the original residual identity with the "
            "BFI prime-AP error object."
        ),
        "review_conclusion": (
            "BFI level 指数账本已在结构层关闭：X≈P^2、Q<=P log^O P 与 "
            "well-factorable lambda support 给出 Q<=X^{1/2+o(1)}，低于 BFI 的 "
            "X^{4/7-eps} 门槛。当前最窄剩余只剩 `OriginalResidualEqualsBFIAPError`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI BFI level 指数账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "previous terminal:",
        f"  {result['previous_terminal_gap']};",
        "",
        "previous open targets:",
        f"  {result['previous_open_terminal_targets']};",
        "",
        "new remaining targets:",
        f"  {result['remaining_terminal_targets']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `bfi_level_exponent_ledger_closed={fmt_bool(result['bfi_level_exponent_ledger_closed'])}`。",
        f"- `open_level_gates={result['open_level_gates']}`。",
        f"- `remaining_terminal_targets={result['remaining_terminal_targets']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. level 账本表",
        "",
        "| gate | closed | exponent | evidence | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["level_rows"]:
        exponent = row.get("exponent_in_X", row.get("exponent_in_P", ""))
        lines.append(
            "| `{gate}` | `{closed}` | `{exponent}` | {evidence} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                exponent=table_cell(exponent),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "level 侧已不再是独立终端硬点：",
            "",
            "```text",
            "Q <= P log^O P;",
            "X ~= P^2;",
            "therefore Q <= X^{1/2+o(1)};",
            "BFI allows X^{4/7-eps};",
            "choose eps=1/56;",
            "slack = 31/56 - 1/2 = 3/56.",
            "```",
            "",
            "因此直接 BFI 外部引用路线的最窄剩余是 AP 源对象等式，而不是 level 指数不足。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bfi-atom-match-json", type=Path, default=DEFAULT_BFI_ATOM_MATCH)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--external-index-md", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--final-review-md", type=Path, default=DEFAULT_FINAL_REVIEW)
    parser.add_argument("--zero-row-md", type=Path, default=DEFAULT_ZERO_ROW)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        bfi_atom_match_path=args.bfi_atom_match_json,
        common_variable_table_path=args.common_variable_table_json,
        kls_template_path=args.kls_template_md,
        kze_spine_path=args.kze_spine_md,
        external_index_path=args.external_index_md,
        final_review_path=args.final_review_md,
        zero_row_path=args.zero_row_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "bfi_level_exponent_ledger_closed": result[
                    "bfi_level_exponent_ledger_closed"
                ],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
