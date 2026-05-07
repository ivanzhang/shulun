#!/usr/bin/env python3
"""把 DI Theorem 12 的 R/D/N 变量代入压成 Maynard-W4 参数账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_di_rdn_substitution_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-di-rdn-substitution-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-di-rdn-substitution-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DI_FORMULA_LEDGER = DOCS / "prime-matrix-triad-a1-dibfi-di-formula-ledger-router.json"
DEFAULT_DI_FORMULA_NOTE = DOCS / "prime-matrix-triad-a1-dibfi-di-theorem12-formula-note.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_COMMON_VARIABLE_TABLE = DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-di-rdn-substitution-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-di-rdn-substitution-router.md"


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


def build_substitution_rows(
    di_formula_ledger: dict[str, Any],
    di_formula_note_path: Path,
    kze_spine_path: Path,
    common_variable_table: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造 R/D/N 到 Maynard-W4 的代入表。"""
    formula_ready = contains_all(
        di_formula_note_path,
        ["J^2", "C*S*(R*S+N)*(C+D*R)", "D^2*N*R"],
    )
    kze_has_square_stage = contains_all(
        kze_spine_path,
        ["s_1,s_2", "0<|h|\\le H", "e_{r_1r_2}(a(h)s+b(h)\\bar s)"],
    )
    common_has_core_symbols = {"c,C", "s,S", "h,H", "alpha,beta,omega"}.issubset(
        {row["symbol"] for row in common_variable_table["variable_rows"]}
    )
    return [
        {
            "gate": "DIToMaynardW4Alias",
            "closed": formula_ready,
            "evidence": "DI Theorem 12 取 r=z, s=1, n=y, d=b, c=c，得到 Maynard W4 的 J-bound。",
            "remaining": "none at pure formula-alias level",
            "next_target": "MaynardW4ParameterBoundsForCurrentWFD",
        },
        {
            "gate": "JBoundAfterAlias",
            "closed": formula_ready,
            "evidence": "J^2 被代入为 C(Z+Y)(C+B Z)+C^2 B sqrt((Z+Y)Z)+B^2 Y Z。",
            "remaining": "none before current-window substitution",
            "next_target": "MaynardW4ParameterBoundsForCurrentWFD",
        },
        {
            "gate": "DIAdditionalVariablesRDNMapped",
            "closed": formula_ready,
            "evidence": "R_DI,D_DI,N_DI 已分别映到 Z,B,Y；S_DI 为平凡窗口 1。",
            "remaining": "仍需把当前 WFD 的内部 S/H/frequency 变量压到 Z,Y,B,C。",
            "next_target": "CurrentWFDToMaynardW4ParameterLedger",
        },
        {
            "gate": "KZEHasW4ShapeInputs",
            "closed": kze_has_square_stage and common_has_core_symbols,
            "evidence": "KZ-E spine 与共同变量表含 s1/s2、h、C/S/H 和 Kloosterman 逆元相位接口。",
            "remaining": "形状接口可用，但尚未证明当前块等于 Maynard W4 的 off-diagonal 结构。",
            "next_target": "CurrentWFDToMaynardW4ParameterLedger",
        },
        {
            "gate": "CurrentWFDMatchesW4OffDiagonalForm",
            "closed": False,
            "evidence": "Maynard W4 使用 z=s1*s2、y=a*f*(h1*s1-h2*s2)、b,c 两个模数窗口；当前账本尚未逐项生成这些变量。",
            "remaining": "从当前 E_disp/WFD_core 写出 z,y,b,c 的 dyadic 分解和 off-diagonal ell!=0 归约。",
            "next_target": "CurrentWFDToMaynardW4ParameterLedger",
        },
        {
            "gate": "MaynardW4ParameterBoundsForCurrentWFD",
            "closed": False,
            "evidence": "Maynard 应用需要 B<=NR、C<=NRS、Z≈S^2、Y<=N R^2 S^3/M 等参数界。",
            "remaining": "把这些 Maynard 参数界翻译为当前 X,Q,N,M,C,S,H 的非冲突变量表。",
            "next_target": "CurrentWFDToMaynardW4ParameterLedger",
        },
        {
            "gate": "JBoundDominanceAfterW4Substitution",
            "closed": False,
            "evidence": f"上游 open_formula_gates={di_formula_ledger['open_formula_gates']}；J-bound 公式已降维但还未比较目标尺度。",
            "remaining": "证明 C(Z+Y)(C+BZ)、C^2B sqrt((Z+Y)Z)、B^2YZ 均被 WFD 自然尺度/log^A 吸收。",
            "next_target": "CurrentWFDToMaynardW4ParameterLedger",
        },
    ]


def run(
    di_formula_ledger_path: Path,
    di_formula_note_path: Path,
    kze_spine_path: Path,
    common_variable_table_path: Path,
) -> dict[str, Any]:
    """运行 DI R/D/N 代入路由。"""
    di_formula_ledger = load_json(di_formula_ledger_path)
    common_variable_table = load_json(common_variable_table_path)
    substitution_rows = build_substitution_rows(
        di_formula_ledger,
        di_formula_note_path,
        kze_spine_path,
        common_variable_table,
    )
    open_substitution_gates = [row["gate"] for row in substitution_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_di_rdn_substitution_router",
        "status": "di_rdn_substitution_reduced_to_current_wfd_maynard_w4_parameter_ledger_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "di_formula_ledger_json": file_sha256(di_formula_ledger_path),
            "di_formula_note_md": file_sha256(di_formula_note_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
        },
        "previous_terminal_gap": di_formula_ledger["terminal_gap_after_router"],
        "substitution_rows": substitution_rows,
        "closed_substitution_gates": [
            row["gate"] for row in substitution_rows if row["closed"]
        ],
        "open_substitution_gates": open_substitution_gates,
        "di_rdn_substitution_closed": False,
        "di_to_w4_alias": {
            "R_DI": "Z",
            "S_DI": "1",
            "N_DI": "Y",
            "D_DI": "B",
            "C_DI": "C",
        },
        "w4_j_bound": "J^2 <= C(Z+Y)(C+B Z)+C^2 B sqrt((Z+Y)Z)+B^2 Y Z",
        "terminal_gap_after_router": "CurrentWFDToMaynardW4ParameterLedger",
        "terminal_gap_expansion": [
            "CurrentWFDMatchesW4OffDiagonalForm",
            "MaynardW4ParameterBoundsForCurrentWFD",
            "JBoundDominanceAfterW4Substitution",
        ],
        "structural_law": (
            "The extra DI variables R,D,N are no longer abstract: under the standard Maynard "
            "application of DI Theorem 12, they alias to Z,B,Y with S_DI=1. The remaining scale "
            "work is not theorem-formula work but current-object work: prove that the present "
            "uncentered WFD block has the W4 off-diagonal variables z=s1*s2, y=a*f*(h1*s1-h2*s2), "
            "with the required dyadic bounds, and then dominate the three W4 J-bound terms."
        ),
        "review_conclusion": (
            "DI 的 R/D/N 变量已在公式层代入到 Maynard-W4 正规形；剩余不再是 DI 定理变量不明，"
            "而是当前 WFD 块到 W4 参数表的逐项生成与 J-bound 三项支配。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI DI RDN substitution 路由器",
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
        "DI -> W4 alias:",
        f"  {result['di_to_w4_alias']};",
        "",
        "W4 J-bound:",
        f"  {result['w4_j_bound']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `di_rdn_substitution_closed={fmt_bool(result['di_rdn_substitution_closed'])}`。",
        f"- `closed_substitution_gates={result['closed_substitution_gates']}`。",
        f"- `open_substitution_gates={result['open_substitution_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 代入账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["substitution_rows"]:
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
            "尺度侧的最窄剩余已经变为：",
            "",
            "```text",
            "CurrentWFDToMaynardW4ParameterLedger:",
            "  CurrentWFDMatchesW4OffDiagonalForm;",
            "  MaynardW4ParameterBoundsForCurrentWFD;",
            "  JBoundDominanceAfterW4Substitution.",
            "```",
            "",
            "这一步关闭了 `R/D/N` 抽象变量缺口，但没有证明当前 WFD 块已经满足 W4 参数界。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--di-formula-ledger-json", type=Path, default=DEFAULT_DI_FORMULA_LEDGER)
    parser.add_argument("--di-formula-note-md", type=Path, default=DEFAULT_DI_FORMULA_NOTE)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        di_formula_ledger_path=args.di_formula_ledger_json,
        di_formula_note_path=args.di_formula_note_md,
        kze_spine_path=args.kze_spine_md,
        common_variable_table_path=args.common_variable_table_json,
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
                "open_substitution_gates": result["open_substitution_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
