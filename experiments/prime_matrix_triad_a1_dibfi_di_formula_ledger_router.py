#!/usr/bin/env python3
"""把 DI Kloosterman 窗口代入压成 Theorem 12 公式变量账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_di_formula_ledger_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-di-formula-ledger-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-di-formula-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_NONAP_SCALE_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-nonap-scale-ledger-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_THEOREM_LOCATION = DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_DI_FORMULA_NOTE = (
    DOCS / "prime-matrix-triad-a1-dibfi-di-theorem12-formula-note.md"
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-di-formula-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-di-formula-ledger-router.md"


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


def build_formula_rows(
    nonap_scale_ledger: dict[str, Any],
    common_variable_table: dict[str, Any],
    theorem_location: dict[str, Any],
    kls_template_path: Path,
    di_formula_note_path: Path,
) -> list[dict[str, Any]]:
    """构造 DI Theorem 12 公式账本行。"""
    variable_symbols = {row["symbol"] for row in common_variable_table["variable_rows"]}
    formula_extracted = contains_all(
        di_formula_note_path,
        ["J^2", "C*S*(R*S+N)*(C+D*R)", "D^2*N*R"],
    )
    kls_interface_ready = contains_all(
        kls_template_path,
        ["Kloosterman 相位", "模数族", "逆元变量", "频率族"],
    )
    di_location_pinned = any(
        row["source_id"] == "DI1982-Theorem12" and row["located"]
        for row in theorem_location["source_rows"]
    )
    return [
        {
            "gate": "DITheorem12FormulaExtracted",
            "closed": formula_extracted and di_location_pinned,
            "evidence": "Maynard 公开源码中的 DI 引理已记录 J^2 三项；定理位置仍为 DI1982-Theorem12。",
            "remaining": "none at formula-extraction level",
            "next_target": "DITheorem12RDNVariableSubstitutionLedger",
        },
        {
            "gate": "KLSInterfaceRowsReady",
            "closed": kls_interface_ready
            and {"c,C", "s,S", "h,H"}.issubset(variable_symbols),
            "evidence": "KLS 模板与共同变量表已有 C/S/H、相位、gcd、平滑和 log-loss 接口。",
            "remaining": "模板只有 C/S/H 接口，尚未给出 DI 公式中的 R,D,N 分拆。",
            "next_target": "DITheorem12RDNVariableSubstitutionLedger",
        },
        {
            "gate": "DIAdditionalVariablesRDNMapped",
            "closed": False,
            "evidence": "DI Theorem 12 的 J^2 需要 R,D,N；当前共同变量表只有 X,Q,N,M,C,S,H。",
            "remaining": "必须把 r~R、d~D、n~N 从当前 dispersion/WFD 块中逐项抽出并固定。",
            "next_target": "DITheorem12RDNVariableSubstitutionLedger",
        },
        {
            "gate": "KLSModulusWindowQuantified",
            "closed": False,
            "evidence": "C 窗口已命名，但 DI 公式使用 C,D,R 的组合模数结构 C+D*R。",
            "remaining": "证明当前模数族可唯一分解为 DI 的 c~C,d~D,r~R 三个窗口。",
            "next_target": "DITheorem12RDNVariableSubstitutionLedger",
        },
        {
            "gate": "InverseVariableWindowQuantified",
            "closed": False,
            "evidence": "S 窗口已命名，但 DI 公式要求 (r,s)=1 且相位 e(n*bar(dr)/(cs))。",
            "remaining": "证明当前 CRT 合并变量 s、可逆条件和频率/系数 n 与 DI 的 S,N 完全同一。",
            "next_target": "DITheorem12RDNVariableSubstitutionLedger",
        },
        {
            "gate": "DIJScaleDominanceSubstitution",
            "closed": False,
            "evidence": f"旧 open_scale_gates={nonap_scale_ledger['open_scale_gates']}；J^2 三项已记录但未代入。",
            "remaining": "把 J^2 三项逐项比较到 WFD 自然二范数尺度/log^A。",
            "next_target": "DITheorem12RDNVariableSubstitutionLedger",
        },
    ]


def run(
    nonap_scale_ledger_path: Path,
    common_variable_table_path: Path,
    theorem_location_path: Path,
    kls_template_path: Path,
    di_formula_note_path: Path,
) -> dict[str, Any]:
    """运行 DI Theorem 12 公式账本路由。"""
    nonap_scale_ledger = load_json(nonap_scale_ledger_path)
    common_variable_table = load_json(common_variable_table_path)
    theorem_location = load_json(theorem_location_path)
    formula_rows = build_formula_rows(
        nonap_scale_ledger,
        common_variable_table,
        theorem_location,
        kls_template_path,
        di_formula_note_path,
    )
    open_formula_gates = [row["gate"] for row in formula_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_di_formula_ledger_router",
        "status": "di_kloosterman_formula_extracted_rd_n_substitution_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "nonap_scale_ledger_json": file_sha256(nonap_scale_ledger_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "theorem_location_json": file_sha256(theorem_location_path),
            "kls_template_md": file_sha256(kls_template_path),
            "di_formula_note_md": file_sha256(di_formula_note_path),
        },
        "previous_terminal_gap": nonap_scale_ledger["terminal_gap_after_router"],
        "formula_rows": formula_rows,
        "closed_formula_gates": [row["gate"] for row in formula_rows if row["closed"]],
        "open_formula_gates": open_formula_gates,
        "di_formula_ledger_closed": False,
        "terminal_gap_after_router": "DITheorem12RDNVariableSubstitutionLedger",
        "terminal_gap_expansion": [
            "DIAdditionalVariablesRDNMapped",
            "KLSModulusWindowQuantified",
            "InverseVariableWindowQuantified",
            "DIJScaleDominanceSubstitution",
        ],
        "structural_law": (
            "The DI-side scale gap is now formula-level. The old C/S/H wording is insufficient "
            "because DI Theorem 12 uses variables R,S,N,D,C and the three-term J^2 expression. "
            "The remaining task is one substitution ledger: extract R,D,N from the current "
            "dispersion/WFD block, then compare each J^2 term to the WFD natural norm with the "
            "log-saving budget."
        ),
        "review_conclusion": (
            "DI 侧已从描述性 `DIKloostermanWindowSubstitutionLedger` 压成 "
            "`DITheorem12RDNVariableSubstitutionLedger`。公式已固定；未闭合的是 R/D/N "
            "变量抽取和 J^2 三项逐项支配。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI DI formula ledger 路由器",
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
        "new DI-side terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "expansion:",
        f"  {result['terminal_gap_expansion']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `di_formula_ledger_closed={fmt_bool(result['di_formula_ledger_closed'])}`。",
        f"- `closed_formula_gates={result['closed_formula_gates']}`。",
        f"- `open_formula_gates={result['open_formula_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 公式账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["formula_rows"]:
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
            "DITheorem12RDNVariableSubstitutionLedger:",
            "  extract R,D,N from the current WFD block;",
            "  substitute J^2;",
            "  dominate all three J^2 terms by the natural WFD scale/log^A.",
            "```",
            "",
            "这一步关闭了“公式未固定”的退路，但没有关闭 DI 代入本身。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--nonap-scale-ledger-json", type=Path, default=DEFAULT_NONAP_SCALE_LEDGER
    )
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--theorem-location-json", type=Path, default=DEFAULT_THEOREM_LOCATION)
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--di-formula-note-md", type=Path, default=DEFAULT_DI_FORMULA_NOTE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        nonap_scale_ledger_path=args.nonap_scale_ledger_json,
        common_variable_table_path=args.common_variable_table_json,
        theorem_location_path=args.theorem_location_json,
        kls_template_path=args.kls_template_md,
        di_formula_note_path=args.di_formula_note_md,
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
                "open_formula_gates": result["open_formula_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
