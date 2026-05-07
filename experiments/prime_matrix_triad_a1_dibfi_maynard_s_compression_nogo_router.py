#!/usr/bin/env python3
"""审计 MaynardSCompressionMap 与完整共同 S 窗口的冲突。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_maynard_s_compression_nogo_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.md
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
DEFAULT_REROUTE_AUDIT = (
    DOCS / "prime-matrix-triad-a1-dibfi-alternate-w4-reroute-audit-router.json"
)
DEFAULT_S_BARRIER = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-barrier-router.json"
)
DEFAULT_DI_RDN_SUBSTITUTION = (
    DOCS / "prime-matrix-triad-a1-dibfi-di-rdn-substitution-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_NOGO_NOTE = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-note.md"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.md"
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


def fmt_fraction(value: Fraction) -> str:
    """格式化分数。"""
    return f"{value.numerator}/{value.denominator}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_nogo_rows(
    reroute_audit: dict[str, Any],
    s_barrier: dict[str, Any],
    di_rdn_substitution: dict[str, Any],
    common_variable_table: dict[str, Any],
    nogo_note_path: Path,
) -> list[dict[str, Any]]:
    """构造 S-compression no-go 账本行。"""
    note_ready = contains_all(
        nogo_note_path,
        [
            "z=s1*s2",
            "S_common≈P=X^(1/2",
            "S_May <= X^(3/10",
            "ShortSSubwindowDecomposition",
            "NewFullSDispersionAtom",
        ],
    )
    prior_ready = reroute_audit["terminal_gap_after_router"] == "MaynardSCompressionMap"
    common_s_ready = any(
        row["symbol"] == "s,S" and row["fixed_by_table"]
        for row in common_variable_table["variable_rows"]
    )
    w4_z_ready = any(
        row["gate"] == "CurrentWFDMatchesW4OffDiagonalForm"
        and "z=s1*s2" in row["evidence"]
        for row in di_rdn_substitution["substitution_rows"]
    )
    s_barrier_ready = (
        s_barrier["maynard_s_upper_bound_when_q_half"] == "3/10-o(1)"
    )
    full_s_exponent = Fraction(1, 2)
    maynard_s_bound = Fraction(3, 10)
    full_z_exponent = full_s_exponent * 2
    maynard_z_bound = maynard_s_bound * 2
    return [
        {
            "gate": "PriorSingleMaynardSCompressionTerminalAvailable",
            "closed": prior_ready,
            "evidence": "上游已排除已登记替代 W4 路由，尺度侧单点化为 MaynardSCompressionMap。",
            "remaining": "none at prior-frontier level",
            "next_target": "FullCommonSProductForcesLargeZ",
        },
        {
            "gate": "FullCommonSWindowPinned",
            "closed": common_s_ready,
            "evidence": "共同变量表固定 KE-13 逆元窗口 s,S；当前 non-AP 账本记录 S_common≈P=X^(1/2+o(1))。",
            "remaining": "若要压缩，必须证明合法短子窗口分解，而非直接使用完整 S_common。",
            "next_target": "ShortSSubwindowDecomposition",
        },
        {
            "gate": "W4ZEqualsS1S2ObjectRequirement",
            "closed": w4_z_ready,
            "evidence": "DI RDN/W4 账本要求当前 WFD 对象逐项生成 z=s1*s2。",
            "remaining": "该对象等式尚未证明，但一旦坚持它，就固定 Z 的尺度。",
            "next_target": "FullCommonSProductForcesLargeZ",
        },
        {
            "gate": "MaynardConeForcesSmallSAndZ",
            "closed": s_barrier_ready,
            "evidence": (
                f"q=1/2 时 S_May<={fmt_fraction(maynard_s_bound)}，"
                f"故 Z≈S_May^2<={fmt_fraction(maynard_z_bound)}。"
            ),
            "remaining": "none at cone consequence level",
            "next_target": "FullCommonSProductContradictsMaynardZBound",
        },
        {
            "gate": "FullCommonSProductForcesLargeZ",
            "closed": common_s_ready and w4_z_ready and note_ready,
            "evidence": (
                f"s1,s2~X^{fmt_fraction(full_s_exponent)} and z=s1*s2 force "
                f"Z~X^{fmt_fraction(full_z_exponent)} and S_May~X^{fmt_fraction(full_s_exponent)}。"
            ),
            "remaining": "none if full S window is preserved",
            "next_target": "FullCommonSProductContradictsMaynardZBound",
        },
        {
            "gate": "FullCommonSProductContradictsMaynardZBound",
            "closed": note_ready and full_z_exponent > maynard_z_bound,
            "evidence": (
                f"full-S object gives Z exponent {fmt_fraction(full_z_exponent)}；"
                f"Maynard cone allows at most {fmt_fraction(maynard_z_bound)}。"
            ),
            "remaining": "MaynardSCompressionMap cannot preserve the full common S window and the W4 z=s1*s2 object simultaneously.",
            "next_target": "ShortSSubwindowOrNewFullSDispersionAtom",
        },
        {
            "gate": "ShortSSubwindowDecomposition",
            "closed": False,
            "evidence": "需要证明 KE-13/WFD 的 s1,s2 窗口可合法切成 S_short<=X^(3/10-o(1)) 并不丢目标质量。",
            "remaining": "尚未建立；这是新的具体硬点。",
            "next_target": "ShortSSubwindowOrNewFullSDispersionAtom",
        },
        {
            "gate": "NewFullSDispersionAtom",
            "closed": False,
            "evidence": "若不能短窗分解，必须新增适配 S_common≈X^(1/2) 的 full-S 原始 dispersion 原子。",
            "remaining": "当前仓库没有该已登记闭合原子。",
            "next_target": "ShortSSubwindowOrNewFullSDispersionAtom",
        },
    ]


def run(
    reroute_audit_path: Path,
    s_barrier_path: Path,
    di_rdn_substitution_path: Path,
    common_variable_table_path: Path,
    nogo_note_path: Path,
) -> dict[str, Any]:
    """运行 S-compression no-go 路由。"""
    reroute_audit = load_json(reroute_audit_path)
    s_barrier = load_json(s_barrier_path)
    di_rdn_substitution = load_json(di_rdn_substitution_path)
    common_variable_table = load_json(common_variable_table_path)
    nogo_rows = build_nogo_rows(
        reroute_audit,
        s_barrier,
        di_rdn_substitution,
        common_variable_table,
        nogo_note_path,
    )
    open_nogo_gates = [row["gate"] for row in nogo_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_maynard_s_compression_nogo_router",
        "status": "maynard_s_compression_map_rejected_full_s_window_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "reroute_audit_json": file_sha256(reroute_audit_path),
            "s_barrier_json": file_sha256(s_barrier_path),
            "di_rdn_substitution_json": file_sha256(di_rdn_substitution_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "nogo_note_md": file_sha256(nogo_note_path),
        },
        "previous_terminal_gap": reroute_audit["terminal_gap_after_router"],
        "full_common_s_exponent": "1/2+o(1)",
        "forced_full_z_exponent": "1+o(1)",
        "maynard_s_upper_bound_when_q_half": "3/10-o(1)",
        "maynard_z_upper_bound_when_q_half": "3/5-o(1)",
        "nogo_rows": nogo_rows,
        "closed_nogo_gates": [row["gate"] for row in nogo_rows if row["closed"]],
        "open_nogo_gates": open_nogo_gates,
        "maynard_s_compression_map_closed": False,
        "terminal_gap_after_router": "ShortSSubwindowOrNewFullSDispersionAtom",
        "terminal_gap_expansion": [
            "ShortSSubwindowDecomposition",
            "NewFullSDispersionAtom",
        ],
        "structural_law": (
            "If the current WFD keeps the full common inverse window S_common≈X^(1/2) and "
            "also matches the Maynard W4 object z=s1*s2, then Z≈X and S_May≈X^(1/2). "
            "The Maynard cone with q=1/2 permits only S_May<=X^(3/10-o(1)). Therefore "
            "MaynardSCompressionMap is impossible without a genuine short-S subwindow "
            "decomposition, or else a new full-S dispersion atom."
        ),
        "review_conclusion": (
            "Maynard-S 压缩映射在完整共同 S 窗口和 W4 对象等式同时保留时被排除；"
            "剩余转为短 S 子窗口分解，或新增 full-S 原始 dispersion 原子。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI Maynard S-compression no-go 路由器",
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
        "forced scales:",
        f"  full_common_s={result['full_common_s_exponent']};",
        f"  full_z={result['forced_full_z_exponent']};",
        f"  maynard_s_bound={result['maynard_s_upper_bound_when_q_half']};",
        f"  maynard_z_bound={result['maynard_z_upper_bound_when_q_half']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `maynard_s_compression_map_closed={fmt_bool(result['maynard_s_compression_map_closed'])}`。",
        f"- `closed_nogo_gates={result['closed_nogo_gates']}`。",
        f"- `open_nogo_gates={result['open_nogo_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. No-go 账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["nogo_rows"]:
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
            "ShortSSubwindowOrNewFullSDispersionAtom:",
            "  ShortSSubwindowDecomposition;",
            "  NewFullSDispersionAtom.",
            "```",
            "",
            "这一步排除的是完整 S 窗口下的 Maynard-S 压缩映射，不是行命题闭合。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reroute-audit-json", type=Path, default=DEFAULT_REROUTE_AUDIT)
    parser.add_argument("--s-barrier-json", type=Path, default=DEFAULT_S_BARRIER)
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
    parser.add_argument("--nogo-note-md", type=Path, default=DEFAULT_NOGO_NOTE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        reroute_audit_path=args.reroute_audit_json,
        s_barrier_path=args.s_barrier_json,
        di_rdn_substitution_path=args.di_rdn_substitution_json,
        common_variable_table_path=args.common_variable_table_json,
        nogo_note_path=args.nogo_note_md,
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
                "open_nogo_gates": result["open_nogo_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
