#!/usr/bin/env python3
"""把 Maynard-W4 三条条件压成统一指数锥。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_maynard_exponent_cone_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-maynard-exponent-cone-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-maynard-exponent-cone-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_W4_PARAMETER_LEDGER = DOCS / "prime-matrix-triad-a1-dibfi-w4-parameter-ledger-router.json"
DEFAULT_EXPONENT_CONE_NOTE = DOCS / "prime-matrix-triad-a1-dibfi-maynard-exponent-cone-note.md"
DEFAULT_W4_PARAMETER_NOTE = DOCS / "prime-matrix-triad-a1-dibfi-maynard-w4-parameter-note.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-maynard-exponent-cone-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-maynard-exponent-cone-router.md"


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


def build_cone_rows(
    w4_parameter_ledger: dict[str, Any],
    exponent_cone_note_path: Path,
    w4_parameter_note_path: Path,
) -> list[dict[str, Any]]:
    """构造指数锥账本行。"""
    cone_note_ready = contains_all(
        exponent_cone_note_path,
        [
            "2n + 2r + s <= 1 - eta",
            "n + 2r + 5s + q <= 2 - eta",
            "2n + 3r + 4s + q <= 2 - eta",
        ],
    )
    w4_note_ready = contains_all(
        w4_parameter_note_path,
        [
            "N_May^2 R_May^2 S_May << x^(1-7 eps)",
            "N_May R_May^2 S_May^5 Q_May < x^(2-14 eps)",
            "N_May^2 R_May^3 S_May^4 Q_May < x^(2-14 eps)",
        ],
    )
    return [
        {
            "gate": "W4ConditionsConvertedToExponentCone",
            "closed": cone_note_ready and w4_note_ready,
            "evidence": "三条 Maynard 乘法条件已改写为 n,r,s,q 的线性不等式。",
            "remaining": "none at algebraic conversion level",
            "next_target": "CurrentWFDFitsMaynardExponentCone",
        },
        {
            "gate": "DiagonalEqualsFactorCondition",
            "closed": cone_note_ready,
            "evidence": "n+m=1 时，M_May>R_May^2 S_May N_May 等价于 2n+2r+s<1。",
            "remaining": "仍需当前 WFD 给出 n,m,r,s 翻译和正余量 eta。",
            "next_target": "CurrentWFDFitsMaynardExponentCone",
        },
        {
            "gate": "CurrentWFDMatchesW4OffDiagonalForm",
            "closed": False,
            "evidence": "上游 W4 ledger 仍将该项列为 open；指数锥只处理尺度，不处理对象等式。",
            "remaining": "证明 z=s1*s2、y=a*f*(h1*s1-h2*s2)、b,c 窗口来自当前 WFD 非对角展开。",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
        {
            "gate": "CurrentWFDMaynardVariableTranslation",
            "closed": False,
            "evidence": "必须给出 N_May,R_May,S_May,M_May,Q_May 与当前 X,Q,N,M,C,S,H 的非冲突翻译。",
            "remaining": "没有该翻译，指数锥不能代入。",
            "next_target": "CurrentWFDFitsMaynardExponentCone",
        },
        {
            "gate": "CurrentWFDFitsMaynardExponentCone",
            "closed": False,
            "evidence": (
                "需要同时满足 n+m=1、2n+2r+s<=1-eta、"
                "n+2r+5s+q<=2-eta、2n+3r+4s+q<=2-eta。"
            ),
            "remaining": "当前 WFD 的 n,r,s,m,q 尚未提交，因此不能关闭该 cone admission。",
            "next_target": "CurrentWFDSatisfiesMaynardW4Conditions",
        },
        {
            "gate": "JBoundDominanceAfterW4Substitution",
            "closed": False,
            "evidence": f"上游 open_w4_gates={w4_parameter_ledger['open_w4_gates']}；三条件已合并为 exponent cone。",
            "remaining": "只有 CurrentWFDFitsMaynardExponentCone 关闭后，J-bound dominance 才关闭。",
            "next_target": "CurrentWFDFitsMaynardExponentCone",
        },
    ]


def run(
    w4_parameter_ledger_path: Path,
    exponent_cone_note_path: Path,
    w4_parameter_note_path: Path,
) -> dict[str, Any]:
    """运行 Maynard-W4 指数锥路由。"""
    w4_parameter_ledger = load_json(w4_parameter_ledger_path)
    cone_rows = build_cone_rows(
        w4_parameter_ledger,
        exponent_cone_note_path,
        w4_parameter_note_path,
    )
    open_cone_gates = [row["gate"] for row in cone_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_maynard_exponent_cone_router",
        "status": "maynard_w4_conditions_reduced_to_current_wfd_exponent_cone_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "w4_parameter_ledger_json": file_sha256(w4_parameter_ledger_path),
            "exponent_cone_note_md": file_sha256(exponent_cone_note_path),
            "w4_parameter_note_md": file_sha256(w4_parameter_note_path),
        },
        "previous_terminal_gap": w4_parameter_ledger["terminal_gap_after_router"],
        "cone_rows": cone_rows,
        "closed_cone_gates": [row["gate"] for row in cone_rows if row["closed"]],
        "open_cone_gates": open_cone_gates,
        "maynard_exponent_cone_closed": False,
        "terminal_gap_after_router": "CurrentWFDMaynardExponentConeAdmission",
        "terminal_gap_expansion": [
            "CurrentWFDMatchesW4OffDiagonalForm",
            "CurrentWFDMaynardVariableTranslation",
            "CurrentWFDFitsMaynardExponentCone",
        ],
        "exponent_cone": [
            "n+m=1",
            "2n+2r+s <= 1-eta",
            "n+2r+5s+q <= 2-eta",
            "2n+3r+4s+q <= 2-eta",
        ],
        "structural_law": (
            "The three Maynard W4 multiplicative conditions are one linear exponent-cone "
            "admission after writing N=x^n, R=x^r, S=x^s, M=x^m, Q=x^q. The diagonal "
            "condition is exactly the factor condition under n+m=1. The remaining task is to "
            "supply the current WFD variable translation and prove the translated exponents lie "
            "inside this cone with positive slack."
        ),
        "review_conclusion": (
            "Maynard-W4 的三条条件已统一压成指数锥；剩余为当前 WFD 的 W4 非对角对象等式、"
            "变量翻译表，以及指数锥准入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI Maynard exponent cone 路由器",
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
        "exponent cone:",
        f"  {result['exponent_cone']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `maynard_exponent_cone_closed={fmt_bool(result['maynard_exponent_cone_closed'])}`。",
        f"- `closed_cone_gates={result['closed_cone_gates']}`。",
        f"- `open_cone_gates={result['open_cone_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 指数锥账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["cone_rows"]:
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
            "尺度侧最窄剩余为：",
            "",
            "```text",
            "CurrentWFDMaynardExponentConeAdmission:",
            "  CurrentWFDMatchesW4OffDiagonalForm;",
            "  CurrentWFDMaynardVariableTranslation;",
            "  CurrentWFDFitsMaynardExponentCone.",
            "```",
            "",
            "这一步关闭了三条 Maynard 条件分散表达的退路，但未证明当前 WFD 的指数落入该锥。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--w4-parameter-ledger-json", type=Path, default=DEFAULT_W4_PARAMETER_LEDGER)
    parser.add_argument("--exponent-cone-note-md", type=Path, default=DEFAULT_EXPONENT_CONE_NOTE)
    parser.add_argument("--w4-parameter-note-md", type=Path, default=DEFAULT_W4_PARAMETER_NOTE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        w4_parameter_ledger_path=args.w4_parameter_ledger_json,
        exponent_cone_note_path=args.exponent_cone_note_md,
        w4_parameter_note_path=args.w4_parameter_note_md,
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
                "open_cone_gates": result["open_cone_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
