#!/usr/bin/env python3
"""审计 Maynard S_May 与共同逆元窗口 S 的直接同一化障碍。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_maynard_s_compression_barrier_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-maynard-s-compression-barrier-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-maynard-s-compression-barrier-router.md
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
DEFAULT_VARIABLE_TRANSLATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-variable-translation-router.json"
)
DEFAULT_NONAP_SCALE_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-nonap-scale-ledger-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_BARRIER_NOTE = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-barrier-note.md"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-barrier-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-barrier-router.md"
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


def maynard_s_upper_bound(q_exponent: Fraction) -> Fraction:
    """由 n+2r+5s+q<=2 和 n,r>=0 推出 s 上界。"""
    return (Fraction(2, 1) - q_exponent) / 5


def build_barrier_rows(
    variable_translation: dict[str, Any],
    nonap_scale_ledger: dict[str, Any],
    common_variable_table: dict[str, Any],
    barrier_note_path: Path,
) -> list[dict[str, Any]]:
    """构造 S-compression barrier 账本行。"""
    q_exponent = Fraction(1, 2)
    s_common_exponent = Fraction(1, 2)
    s_may_upper = maynard_s_upper_bound(q_exponent)
    note_ready = contains_all(
        barrier_note_path,
        [
            "s <= (2-q)/5",
            "s <= 3/10",
            "S_common != S_May",
            "MaynardSCompressionMap",
        ],
    )
    has_q_level = any(
        row["gate"] == "BFILevelQuantified" and row["closed"]
        for row in nonap_scale_ledger["scale_rows"]
    )
    has_common_s = any(
        row["symbol"] == "s,S" and row["fixed_by_table"]
        for row in common_variable_table["variable_rows"]
    )
    prior_terminal_ready = (
        variable_translation["terminal_gap_after_router"]
        == "CurrentWFDW4ObjectTranslationMatrixAdmission"
    )
    direct_s_collision = s_common_exponent > s_may_upper
    return [
        {
            "gate": "PriorTranslationMatrixFrontierAvailable",
            "closed": prior_terminal_ready,
            "evidence": "上游已经把 Maynard 翻译压成 WFD 对象等式、WFD 指数向量和线性矩阵。",
            "remaining": "none at prior-frontier level",
            "next_target": "NaiveCommonSToMaynardSRejected",
        },
        {
            "gate": "QExponentPinnedAtHalf",
            "closed": has_q_level,
            "evidence": "X≈P^2 且 Q<=P log^O P，故 q=x_Q=1/2+o(1)。",
            "remaining": "若后续改用更小 Q_May，需要另建 q<1/2 的翻译行。",
            "next_target": "MaynardSUpperBoundFromCone",
        },
        {
            "gate": "CommonInverseSExponentPinnedAtHalf",
            "closed": has_common_s,
            "evidence": "共同变量表/KE-13 逆元窗口为 S_common≈P=X^(1/2+o(1))。",
            "remaining": "该 S_common 不能未经压缩直接当作 S_May。",
            "next_target": "NaiveCommonSToMaynardSRejected",
        },
        {
            "gate": "MaynardSUpperBoundFromCone",
            "closed": note_ready,
            "evidence": (
                "由 n+2r+5s+q<=2 和 n,r>=0 得 "
                f"s<={fmt_fraction(s_may_upper)}+o(1) when q={fmt_fraction(q_exponent)}。"
            ),
            "remaining": "none at cone-inequality level",
            "next_target": "NaiveCommonSToMaynardSRejected",
        },
        {
            "gate": "NaiveCommonSToMaynardSRejected",
            "closed": direct_s_collision and note_ready,
            "evidence": (
                f"S_common exponent={fmt_fraction(s_common_exponent)} exceeds "
                f"Maynard cone bound {fmt_fraction(s_may_upper)}；直接同一化矛盾。"
            ),
            "remaining": "必须给出 S 压缩映射或改走另一对象路由。",
            "next_target": "MaynardSCompressionMapOrAlternateW4Rerouting",
        },
        {
            "gate": "MaynardSCompressionMap",
            "closed": False,
            "evidence": "需要从当前 s1,s2/h/completion 结构中抽出真实 S_May<=X^(3/10-o(1))。",
            "remaining": "尚无压缩映射；这是真实新硬点。",
            "next_target": "MaynardSCompressionMapOrAlternateW4Rerouting",
        },
        {
            "gate": "AlternateW4ObjectRerouting",
            "closed": False,
            "evidence": "若无法压缩 S_May，则必须证明当前 WFD 非对角对象进入另一已登记可闭合 dispersion 原子。",
            "remaining": "尚未给出替代对象路由。",
            "next_target": "MaynardSCompressionMapOrAlternateW4Rerouting",
        },
    ]


def run(
    variable_translation_path: Path,
    nonap_scale_ledger_path: Path,
    common_variable_table_path: Path,
    barrier_note_path: Path,
) -> dict[str, Any]:
    """运行 S-compression barrier 路由。"""
    variable_translation = load_json(variable_translation_path)
    nonap_scale_ledger = load_json(nonap_scale_ledger_path)
    common_variable_table = load_json(common_variable_table_path)
    barrier_rows = build_barrier_rows(
        variable_translation,
        nonap_scale_ledger,
        common_variable_table,
        barrier_note_path,
    )
    open_barrier_gates = [row["gate"] for row in barrier_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_maynard_s_compression_barrier_router",
        "status": "maynard_s_common_inverse_direct_identification_rejected_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "variable_translation_json": file_sha256(variable_translation_path),
            "nonap_scale_ledger_json": file_sha256(nonap_scale_ledger_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "barrier_note_md": file_sha256(barrier_note_path),
        },
        "previous_terminal_gap": variable_translation["terminal_gap_after_router"],
        "q_exponent": "1/2+o(1)",
        "common_inverse_s_exponent": "1/2+o(1)",
        "maynard_s_upper_bound_when_q_half": "3/10-o(1)",
        "barrier_rows": barrier_rows,
        "closed_barrier_gates": [row["gate"] for row in barrier_rows if row["closed"]],
        "open_barrier_gates": open_barrier_gates,
        "s_compression_barrier_closed": False,
        "terminal_gap_after_router": "MaynardSCompressionMapOrAlternateW4Rerouting",
        "terminal_gap_expansion": [
            "MaynardSCompressionMap",
            "AlternateW4ObjectRerouting",
        ],
        "structural_law": (
            "The Maynard exponent cone forces s <= (2-q)/5. With the current level "
            "q=1/2+o(1), S_May must have exponent at most 3/10-o(1). Therefore the "
            "common inverse window S_common≈P=X^(1/2) cannot be identified with S_May. "
            "A genuine S-compression map or an alternate W4 object route is required."
        ),
        "review_conclusion": (
            "朴素把共同逆元窗口 S 当作 Maynard 的 S_May 已被指数锥排除；当前硬点变为证明"
            " Maynard-S 压缩映射，或给出替代 W4 对象路由。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI Maynard S-compression barrier 路由器",
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
        "forced exponents:",
        f"  q={result['q_exponent']};",
        f"  S_common={result['common_inverse_s_exponent']};",
        f"  S_May<={result['maynard_s_upper_bound_when_q_half']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `s_compression_barrier_closed={fmt_bool(result['s_compression_barrier_closed'])}`。",
        f"- `closed_barrier_gates={result['closed_barrier_gates']}`。",
        f"- `open_barrier_gates={result['open_barrier_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 障碍账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["barrier_rows"]:
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
            "当前最窄尺度侧剩余变为：",
            "",
            "```text",
            "MaynardSCompressionMapOrAlternateW4Rerouting:",
            "  MaynardSCompressionMap;",
            "  AlternateW4ObjectRerouting.",
            "```",
            "",
            "这一步关闭的是朴素变量同一化退路，不是最终命题闭合。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--variable-translation-json",
        type=Path,
        default=DEFAULT_VARIABLE_TRANSLATION,
    )
    parser.add_argument(
        "--nonap-scale-ledger-json",
        type=Path,
        default=DEFAULT_NONAP_SCALE_LEDGER,
    )
    parser.add_argument(
        "--common-variable-table-json",
        type=Path,
        default=DEFAULT_COMMON_VARIABLE_TABLE,
    )
    parser.add_argument("--barrier-note-md", type=Path, default=DEFAULT_BARRIER_NOTE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        variable_translation_path=args.variable_translation_json,
        nonap_scale_ledger_path=args.nonap_scale_ledger_json,
        common_variable_table_path=args.common_variable_table_json,
        barrier_note_path=args.barrier_note_md,
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
                "open_barrier_gates": result["open_barrier_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
