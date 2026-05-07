#!/usr/bin/env python3
"""把当前 WFD -> Maynard 变量翻译压成线性矩阵证书。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_maynard_variable_translation_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-maynard-variable-translation-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-maynard-variable-translation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_EXPONENT_CONE = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-exponent-cone-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_TRANSLATION_NOTE = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-variable-translation-note.md"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-variable-translation-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-variable-translation-router.md"
)


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


def build_translation_constraints() -> list[str]:
    """给出必须检查的线性约束。"""
    return [
        "n+m=1",
        "q=x_Q",
        "x_B <= n+r",
        "x_C <= n+r+s",
        "x_F <= n-q",
        "x_Z = 2s",
        "x_Y <= n+2r+3s-m",
        "2n+2r+s <= 1-eta",
        "n+2r+5s+q <= 2-eta",
        "2n+3r+4s+q <= 2-eta",
    ]


def build_translation_rows(
    exponent_cone: dict[str, Any],
    common_variable_table: dict[str, Any],
    translation_note_path: Path,
) -> list[dict[str, Any]]:
    """构造变量翻译矩阵账本行。"""
    common_symbols = {row["symbol"] for row in common_variable_table["variable_rows"]}
    common_table_ready = {"X", "Q", "N,M", "c,C", "s,S", "h,H"}.issubset(
        common_symbols
    )
    cone_ready = (
        exponent_cone["terminal_gap_after_router"]
        == "CurrentWFDMaynardExponentConeAdmission"
    )
    note_has_matrix = contains_all(
        translation_note_path,
        [
            "x_B <= n+r",
            "x_C <= n+r+s",
            "x_F <= n-q",
            "x_Z = 2s",
            "x_Y <= n+2r+3s-m",
            "CurrentWFDW4ObjectTranslationMatrixAdmission",
        ],
    )
    return [
        {
            "gate": "CommonVariableTableAvailable",
            "closed": common_table_ready,
            "evidence": "共同变量表已有 X,Q,N,M,C,S,H 与 Type-I/II、模数、逆元、频率接口。",
            "remaining": "none at table-availability level",
            "next_target": "WFDWindowExponentVectorSubmitted",
        },
        {
            "gate": "MaynardExponentConeAvailable",
            "closed": cone_ready,
            "evidence": (
                "上游已把三条 Maynard 条件压成 "
                f"{exponent_cone['terminal_gap_after_router']}。"
            ),
            "remaining": "none at cone-algebra level",
            "next_target": "CurrentWFDMaynardTranslationMatrixFeasibleWithSlack",
        },
        {
            "gate": "NoSymbolCollisionDiscipline",
            "closed": note_has_matrix,
            "evidence": "记录明确分离共同变量表的 N,M,C,S,H 与 Maynard 的 N_May,R_May,S_May,M_May,Q_May。",
            "remaining": "none at notation-discipline level",
            "next_target": "WFDWindowExponentVectorSubmitted",
        },
        {
            "gate": "W4ParameterAnchorsLinearized",
            "closed": note_has_matrix,
            "evidence": "B,C,F,Z,Y 的 W4 参数锚点已写成 x_B,x_C,x_F,x_Z,x_Y 的线性约束。",
            "remaining": "none until current WFD exponent vector is supplied",
            "next_target": "CurrentWFDMaynardTranslationMatrixFeasibleWithSlack",
        },
        {
            "gate": "CurrentWFDMatchesW4OffDiagonalForm",
            "closed": False,
            "evidence": "仍需证明当前 WFD 非对角块逐项生成 z=s1*s2、y=a*f*(h1*s1-h2*s2)、b,c 窗口。",
            "remaining": "对象等式未提交；该项独立于线性尺度矩阵。",
            "next_target": "CurrentWFDW4ObjectTranslationMatrixAdmission",
        },
        {
            "gate": "WFDWindowExponentVectorSubmitted",
            "closed": False,
            "evidence": "矩阵需要输入 v_WFD=(x_B,x_C,x_F,x_Z,x_Y,x_Q)，当前尚无逐项 dyadic 指数向量。",
            "remaining": "从当前 WFD 窗口定义抽取 B,C,F,Z,Y,Q 的指数上界。",
            "next_target": "CurrentWFDMaynardTranslationMatrixFeasibleWithSlack",
        },
        {
            "gate": "CurrentWFDMaynardTranslationMatrixFeasibleWithSlack",
            "closed": False,
            "evidence": "必须存在 n,r,s,m,q,eta>0 同时满足 W4 参数锚点与 Maynard 指数锥。",
            "remaining": "待 v_WFD 提交后检查线性可行性和正余量 eta。",
            "next_target": "CurrentWFDW4ObjectTranslationMatrixAdmission",
        },
    ]


def run(
    exponent_cone_path: Path,
    common_variable_table_path: Path,
    translation_note_path: Path,
) -> dict[str, Any]:
    """运行 Maynard 变量翻译矩阵路由。"""
    exponent_cone = load_json(exponent_cone_path)
    common_variable_table = load_json(common_variable_table_path)
    translation_rows = build_translation_rows(
        exponent_cone,
        common_variable_table,
        translation_note_path,
    )
    open_translation_gates = [
        row["gate"] for row in translation_rows if not row["closed"]
    ]
    return {
        "certificate_type": "triad_a1_dibfi_maynard_variable_translation_router",
        "status": "maynard_exponent_cone_reduced_to_wfd_translation_matrix_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "exponent_cone_json": file_sha256(exponent_cone_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "translation_note_md": file_sha256(translation_note_path),
        },
        "previous_terminal_gap": exponent_cone["terminal_gap_after_router"],
        "translation_rows": translation_rows,
        "closed_translation_gates": [
            row["gate"] for row in translation_rows if row["closed"]
        ],
        "open_translation_gates": open_translation_gates,
        "translation_matrix_closed": False,
        "translation_constraints": build_translation_constraints(),
        "terminal_gap_after_router": "CurrentWFDW4ObjectTranslationMatrixAdmission",
        "terminal_gap_expansion": [
            "CurrentWFDMatchesW4OffDiagonalForm",
            "WFDWindowExponentVectorSubmitted",
            "CurrentWFDMaynardTranslationMatrixFeasibleWithSlack",
        ],
        "structural_law": (
            "CurrentWFDMaynardVariableTranslation is now a finite linear feasibility "
            "certificate. Once the WFD dyadic exponent vector is supplied, the Maynard "
            "translation and exponent-cone admission are checked by one matrix with positive "
            "slack; the separate object identity CurrentWFDMatchesW4OffDiagonalForm remains "
            "independent."
        ),
        "review_conclusion": (
            "Maynard 指数锥准入已继续压成 WFD 非对角对象等式、WFD 指数向量提交、"
            "以及一张带正余量的线性翻译矩阵。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI Maynard variable translation 路由器",
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
        f"- `translation_matrix_closed={fmt_bool(result['translation_matrix_closed'])}`。",
        f"- `closed_translation_gates={result['closed_translation_gates']}`。",
        f"- `open_translation_gates={result['open_translation_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 翻译约束",
        "",
        "```text",
    ]
    lines.extend(result["translation_constraints"])
    lines.extend(
        [
            "```",
            "",
            "## 4. 翻译账本表",
            "",
            "| gate | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["translation_rows"]:
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
            "## 5. 当前结论",
            "",
            "当前最窄尺度侧剩余为：",
            "",
            "```text",
            "CurrentWFDW4ObjectTranslationMatrixAdmission:",
            "  CurrentWFDMatchesW4OffDiagonalForm;",
            "  WFDWindowExponentVectorSubmitted;",
            "  CurrentWFDMaynardTranslationMatrixFeasibleWithSlack.",
            "```",
            "",
            "这一步没有证明 WFD 指数落入锥内；它把待证事实固定成一个对象等式和一个线性矩阵可行性证书。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--exponent-cone-json",
        type=Path,
        default=DEFAULT_EXPONENT_CONE,
    )
    parser.add_argument(
        "--common-variable-table-json",
        type=Path,
        default=DEFAULT_COMMON_VARIABLE_TABLE,
    )
    parser.add_argument(
        "--translation-note-md",
        type=Path,
        default=DEFAULT_TRANSLATION_NOTE,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        exponent_cone_path=args.exponent_cone_json,
        common_variable_table_path=args.common_variable_table_json,
        translation_note_path=args.translation_note_md,
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
                "open_translation_gates": result["open_translation_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
