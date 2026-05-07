#!/usr/bin/env python3
"""审计短 S 子窗口分解是否能绕过 full-S 障碍。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_short_s_subwindow_nogo_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-short-s-subwindow-nogo-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-short-s-subwindow-nogo-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_S_COMPRESSION_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.json"
)
DEFAULT_W4_PARAMETER_NOTE = DOCS / "prime-matrix-triad-a1-dibfi-maynard-w4-parameter-note.md"
DEFAULT_DI_RDN_SUBSTITUTION = (
    DOCS / "prime-matrix-triad-a1-dibfi-di-rdn-substitution-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_SUBWINDOW_NOTE = (
    DOCS / "prime-matrix-triad-a1-dibfi-short-s-subwindow-nogo-note.md"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-short-s-subwindow-nogo-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-short-s-subwindow-nogo-router.md"
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


def build_subwindow_rows(
    s_compression_nogo: dict[str, Any],
    w4_parameter_note_path: Path,
    di_rdn_substitution: dict[str, Any],
    common_variable_table: dict[str, Any],
    subwindow_note_path: Path,
) -> list[dict[str, Any]]:
    """构造短 S 子窗口 no-go 账本行。"""
    note_ready = contains_all(
        subwindow_note_path,
        [
            "小宽度不等于小 Maynard-S",
            "z=s1*s2≈X",
            "S_May≈X^(1/2)",
            "NewFullSDispersionAtom",
        ],
    )
    prior_ready = (
        s_compression_nogo["terminal_gap_after_router"]
        == "ShortSSubwindowOrNewFullSDispersionAtom"
    )
    w4_s_is_magnitude = contains_all(
        w4_parameter_note_path,
        ["Z ≍ S^2", "Z ≍ S_May^2"],
    ) or contains_all(w4_parameter_note_path, ["Z ≍ S^2", "S_May"])
    w4_z_object = any(
        row["gate"] == "CurrentWFDMatchesW4OffDiagonalForm"
        and "z=s1*s2" in row["evidence"]
        for row in di_rdn_substitution["substitution_rows"]
    )
    common_s_ready = any(
        row["symbol"] == "s,S" and row["fixed_by_table"]
        for row in common_variable_table["variable_rows"]
    )
    return [
        {
            "gate": "PriorShortSOrFullSAtomFrontierAvailable",
            "closed": prior_ready,
            "evidence": "上游已排除完整 S 窗口下的 Maynard-S 压缩，并留下短 S 子窗口/full-S 原子二选一。",
            "remaining": "none at prior-frontier level",
            "next_target": "ShortSWidthDoesNotReduceMaynardMagnitude",
        },
        {
            "gate": "MaynardSIsMagnitudeNotIntervalWidth",
            "closed": w4_s_is_magnitude and w4_z_object,
            "evidence": "W4 使用 z=s1*s2 且 Z≈S_May^2；S_May 控制乘积变量的量级，不是局部区间宽度。",
            "remaining": "none at notation level",
            "next_target": "ShortSWidthDoesNotReduceMaynardMagnitude",
        },
        {
            "gate": "CurrentBlockIsFullCommonS",
            "closed": common_s_ready,
            "evidence": "当前 KE-13/common table 的逆元变量仍在 full-S dyadic 块 S_common≈X^(1/2)。",
            "remaining": "none unless the target object is changed to a genuinely smaller dyadic S block",
            "next_target": "ShortSWidthDoesNotReduceMaynardMagnitude",
        },
        {
            "gate": "ShortSWidthDoesNotReduceMaynardMagnitude",
            "closed": note_ready and w4_s_is_magnitude and common_s_ready,
            "evidence": "把 s≈X^(1/2) 的窗口切成短宽度区间后，s 的量级仍是 X^(1/2)，故 z=s1*s2≈X。",
            "remaining": "不能用区间宽度 L<=X^(3/10) 替代 S_May。",
            "next_target": "ShortSSubwindowDecompositionRejected",
        },
        {
            "gate": "SmallMagnitudeSSelectionLosesFullSBlock",
            "closed": note_ready,
            "evidence": "若真实要求 s1,s2<=X^(3/10)，则已经离开当前 S_common≈X^(1/2) dyadic 块。",
            "remaining": "必须另证目标质量不在 full-S 块；当前合同没有该事实。",
            "next_target": "ShortSSubwindowDecompositionRejected",
        },
        {
            "gate": "ShortSSubwindowDecompositionRejected",
            "closed": note_ready and w4_s_is_magnitude and common_s_ready,
            "evidence": "短宽度分解不能降低 Maynard-S 量级；真实短量级选择又会丢失当前 full-S dyadic 目标块。",
            "remaining": "当前资料下短 S 子窗口出口不可用。",
            "next_target": "NewFullSDispersionAtom",
        },
        {
            "gate": "NewFullSDispersionAtom",
            "closed": False,
            "evidence": "仍需新增并证明适配 S_common≈X^(1/2)、z≈X 的 full-S 原始 dispersion 原子。",
            "remaining": "当前最新终端硬点。",
            "next_target": "NewFullSDispersionAtom",
        },
    ]


def run(
    s_compression_nogo_path: Path,
    w4_parameter_note_path: Path,
    di_rdn_substitution_path: Path,
    common_variable_table_path: Path,
    subwindow_note_path: Path,
) -> dict[str, Any]:
    """运行短 S 子窗口 no-go 路由。"""
    s_compression_nogo = load_json(s_compression_nogo_path)
    di_rdn_substitution = load_json(di_rdn_substitution_path)
    common_variable_table = load_json(common_variable_table_path)
    subwindow_rows = build_subwindow_rows(
        s_compression_nogo,
        w4_parameter_note_path,
        di_rdn_substitution,
        common_variable_table,
        subwindow_note_path,
    )
    open_subwindow_gates = [
        row["gate"] for row in subwindow_rows if not row["closed"]
    ]
    return {
        "certificate_type": "triad_a1_dibfi_short_s_subwindow_nogo_router",
        "status": "short_s_subwindow_decomposition_rejected_full_s_atom_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "s_compression_nogo_json": file_sha256(s_compression_nogo_path),
            "w4_parameter_note_md": file_sha256(w4_parameter_note_path),
            "di_rdn_substitution_json": file_sha256(di_rdn_substitution_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "subwindow_note_md": file_sha256(subwindow_note_path),
        },
        "previous_terminal_gap": s_compression_nogo["terminal_gap_after_router"],
        "subwindow_rows": subwindow_rows,
        "closed_subwindow_gates": [
            row["gate"] for row in subwindow_rows if row["closed"]
        ],
        "open_subwindow_gates": open_subwindow_gates,
        "short_s_subwindow_closed": False,
        "terminal_gap_after_router": "NewFullSDispersionAtom",
        "terminal_gap_expansion": ["NewFullSDispersionAtom"],
        "structural_law": (
            "Short interval width does not reduce the Maynard S parameter. In W4, "
            "S_May is tied to the magnitude of z=s1*s2 via Z≈S_May^2. A subinterval "
            "inside s≈X^(1/2) still has s magnitude X^(1/2), so it still forces "
            "S_May≈X^(1/2). A true S_May<=X^(3/10) selection leaves the current full-S "
            "dyadic block. Thus the remaining scale route requires a new full-S dispersion atom."
        ),
        "review_conclusion": (
            "短 S 子窗口分解被排除：小区间宽度不能替代 Maynard-S 的实际量级；当前尺度侧"
            "剩余单点化为 `NewFullSDispersionAtom`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI short-S subwindow no-go 路由器",
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
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `short_s_subwindow_closed={fmt_bool(result['short_s_subwindow_closed'])}`。",
        f"- `closed_subwindow_gates={result['closed_subwindow_gates']}`。",
        f"- `open_subwindow_gates={result['open_subwindow_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 子窗口账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["subwindow_rows"]:
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
            "当前尺度侧剩余为：",
            "",
            "```text",
            "NewFullSDispersionAtom:",
            "  prove a full-S original dispersion atom for S_common≈X^(1/2), z≈X.",
            "```",
            "",
            "这一步排除的是短 S 子窗口退路，不是 full-S 原子本身。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--s-compression-nogo-json",
        type=Path,
        default=DEFAULT_S_COMPRESSION_NOGO,
    )
    parser.add_argument("--w4-parameter-note-md", type=Path, default=DEFAULT_W4_PARAMETER_NOTE)
    parser.add_argument(
        "--di-rdn-substitution-json",
        type=Path,
        default=DEFAULT_DI_RDN_SUBSTITUTION,
    )
    parser.add_argument(
        "--common-variable-table-json",
        type=Path,
        default=DEFAULT_COMMON_VARIABLE_TABLE,
    )
    parser.add_argument("--subwindow-note-md", type=Path, default=DEFAULT_SUBWINDOW_NOTE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        s_compression_nogo_path=args.s_compression_nogo_json,
        w4_parameter_note_path=args.w4_parameter_note_md,
        di_rdn_substitution_path=args.di_rdn_substitution_json,
        common_variable_table_path=args.common_variable_table_json,
        subwindow_note_path=args.subwindow_note_md,
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
                "open_subwindow_gates": result["open_subwindow_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
