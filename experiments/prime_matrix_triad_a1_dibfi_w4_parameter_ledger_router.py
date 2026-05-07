#!/usr/bin/env python3
"""把当前 WFD -> Maynard-W4 参数账本压成三条显式 W4 条件。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_w4_parameter_ledger_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-w4-parameter-ledger-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-w4-parameter-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DI_RDN_SUBSTITUTION = DOCS / "prime-matrix-triad-a1-dibfi-di-rdn-substitution-router.json"
DEFAULT_W4_PARAMETER_NOTE = DOCS / "prime-matrix-triad-a1-dibfi-maynard-w4-parameter-note.md"
DEFAULT_COMMON_VARIABLE_TABLE = DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-w4-parameter-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-w4-parameter-ledger-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(path: Path, needles: list[str]) -> bool:
    """核查文档是否含有全部关键词。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_w4_rows(
    di_rdn_substitution: dict[str, Any],
    w4_parameter_note_path: Path,
    common_variable_table: dict[str, Any],
    kze_spine_path: Path,
) -> list[dict[str, Any]]:
    """构造 W4 参数账本行。"""
    note_has_template = contains_all(
        w4_parameter_note_path,
        [
            "B << N R",
            "C << N R S",
            "Z ≍ S^2",
            "N_May R_May^2 S_May^5 Q_May < x^(2-14 eps)",
        ],
    )
    note_has_j_simplification = contains_all(
        w4_parameter_note_path,
        [
            "J^2 << x^eps",
            "N_May^2 R_May^2 S_May^5",
            "N_May^3 R_May^3 S_May^4",
        ],
    )
    common_has_source_symbols = {"X", "Q", "N,M", "c,C", "s,S", "h,H"}.issubset(
        {row["symbol"] for row in common_variable_table["variable_rows"]}
    )
    kze_has_dispersion_inputs = contains_all(
        kze_spine_path,
        ["Vaughan/Heath-Brown", "Type-I/II", "s_1,s_2", "0<|h|\\le H"],
    )
    return [
        {
            "gate": "MaynardW4TemplateExtracted",
            "closed": note_has_template,
            "evidence": "W4 的 B,C,F,Z,Y 参数和三条最终条件已抽成记录。",
            "remaining": "none at Maynard-template level",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
        {
            "gate": "W4JBoundSimplified",
            "closed": note_has_j_simplification,
            "evidence": "在 Maynard factor 条件下，J^2 简化为两项主界。",
            "remaining": "none before current-window substitution",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
        {
            "gate": "SourceSymbolsReadyForTranslation",
            "closed": common_has_source_symbols and kze_has_dispersion_inputs,
            "evidence": "共同变量表与 KZ-E spine 已有 X,Q,N,M,C,S,H、Type-I/II 和 s1/s2/h 接口。",
            "remaining": "符号可翻译，但尚未给出非冲突的 N_May/R_May/S_May/M_May/Q_May 表。",
            "next_target": "CurrentWFDMaynardVariableTranslation",
        },
        {
            "gate": "CurrentWFDMatchesW4OffDiagonalForm",
            "closed": False,
            "evidence": "上游 RDN router 已把 DI 变量代入 W4，但当前 E_disp 到 W4 off-diagonal 变量的逐项等式未写出。",
            "remaining": "证明 z=s1*s2、y=a*f*(h1*s1-h2*s2)、b,c 窗口正是当前 WFD 的非对角展开。",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
        {
            "gate": "CurrentWFDMaynardVariableTranslation",
            "closed": False,
            "evidence": "当前变量表有 X,Q,N,M,C,S,H；Maynard 条件使用 N_May,R_May,S_May,M_May,Q_May。",
            "remaining": "建立非冲突翻译表，避免把本项目 S 与 DI/Maynard 的不同 S 混同。",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
        {
            "gate": "MaynardDiagonalCondition",
            "closed": False,
            "evidence": "需证明 N_May^2 R_May^2 S_May << x^(1-7eps)。",
            "remaining": "从当前窗口上界推出该对角条件。",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
        {
            "gate": "MaynardOffDiagonalCondition1",
            "closed": False,
            "evidence": "需证明 N_May R_May^2 S_May^5 Q_May < x^(2-14eps)。",
            "remaining": "从当前窗口上界推出第一条非对角条件。",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
        {
            "gate": "MaynardOffDiagonalCondition2",
            "closed": False,
            "evidence": "需证明 N_May^2 R_May^3 S_May^4 Q_May < x^(2-14eps)。",
            "remaining": "从当前窗口上界推出第二条非对角条件。",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
        {
            "gate": "JBoundDominanceAfterW4Substitution",
            "closed": False,
            "evidence": f"上游 open_substitution_gates={di_rdn_substitution['open_substitution_gates']}；W4 条件已显式化但未由当前窗口推出。",
            "remaining": "三条 Maynard 条件全部成立后，该项才可关闭。",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
    ]


def run(
    di_rdn_substitution_path: Path,
    w4_parameter_note_path: Path,
    common_variable_table_path: Path,
    kze_spine_path: Path,
) -> dict[str, Any]:
    """运行 W4 参数账本路由。"""
    di_rdn_substitution = load_json(di_rdn_substitution_path)
    common_variable_table = load_json(common_variable_table_path)
    w4_rows = build_w4_rows(
        di_rdn_substitution,
        w4_parameter_note_path,
        common_variable_table,
        kze_spine_path,
    )
    open_w4_gates = [row["gate"] for row in w4_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_w4_parameter_ledger_router",
        "status": "w4_parameter_ledger_reduced_to_current_wfd_maynard_conditions_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "di_rdn_substitution_json": file_sha256(di_rdn_substitution_path),
            "w4_parameter_note_md": file_sha256(w4_parameter_note_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "kze_spine_md": file_sha256(kze_spine_path),
        },
        "previous_terminal_gap": di_rdn_substitution["terminal_gap_after_router"],
        "w4_rows": w4_rows,
        "closed_w4_gates": [row["gate"] for row in w4_rows if row["closed"]],
        "open_w4_gates": open_w4_gates,
        "w4_parameter_ledger_closed": False,
        "terminal_gap_after_router": "CurrentWFDSatisfiesMaynardW4Conditions",
        "terminal_gap_expansion": [
            "CurrentWFDMatchesW4OffDiagonalForm",
            "CurrentWFDMaynardVariableTranslation",
            "MaynardDiagonalCondition",
            "MaynardOffDiagonalCondition1",
            "MaynardOffDiagonalCondition2",
        ],
        "structural_law": (
            "The Maynard-W4 parameter template is now explicit. The final DI scale work is no "
            "longer to search for a theorem or formula, but to prove that the present uncentered "
            "WFD block generates the W4 off-diagonal variables and satisfies three concrete "
            "Maynard inequalities after a non-conflicting variable translation."
        ),
        "review_conclusion": (
            "W4 参数模板与 J-bound 简化已固定；剩余为当前 WFD 到 W4 的对象等式、变量翻译表，"
            "以及一条对角条件和两条非对角条件。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI W4 parameter ledger 路由器",
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
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "expansion:",
        f"  {result['terminal_gap_expansion']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `w4_parameter_ledger_closed={fmt_bool(result['w4_parameter_ledger_closed'])}`。",
        f"- `closed_w4_gates={result['closed_w4_gates']}`。",
        f"- `open_w4_gates={result['open_w4_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. W4 账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["w4_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {remaining} | `{next}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                next=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "尺度侧的最窄剩余为：",
            "",
            "```text",
            "CurrentWFDSatisfiesMaynardW4Conditions:",
            "  CurrentWFDMatchesW4OffDiagonalForm;",
            "  CurrentWFDMaynardVariableTranslation;",
            "  MaynardDiagonalCondition;",
            "  MaynardOffDiagonalCondition1;",
            "  MaynardOffDiagonalCondition2.",
            "```",
            "",
            "这一步关闭了 W4 模板未知和 J-bound 未简化的退路，但未证明当前 WFD 满足三条 Maynard 条件。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--di-rdn-substitution-json", type=Path, default=DEFAULT_DI_RDN_SUBSTITUTION
    )
    parser.add_argument("--w4-parameter-note-md", type=Path, default=DEFAULT_W4_PARAMETER_NOTE)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        di_rdn_substitution_path=args.di_rdn_substitution_json,
        w4_parameter_note_path=args.w4_parameter_note_md,
        common_variable_table_path=args.common_variable_table_json,
        kze_spine_path=args.kze_spine_md,
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
                "open_w4_gates": result["open_w4_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
