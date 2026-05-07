#!/usr/bin/env python3
"""审计 DIBFIPrimarySourceSpecializationProof 是否能由现有主来源闭合。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_primary_source_specialization_nogo_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.md
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
DEFAULT_FULL_S_KLS_SPECIALIZATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
)
DEFAULT_S_BARRIER = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-barrier-router.json"
)
DEFAULT_S_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.json"
)
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_NOTE = DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-note.md"
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.md"
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


def build_rows(
    full_s_kls_specialization: dict[str, Any],
    s_barrier: dict[str, Any],
    s_nogo: dict[str, Any],
    external_index_path: Path,
    note_path: Path,
) -> list[dict[str, Any]]:
    """构造 primary-source no-go 审计行。"""
    note_ready = contains_all(
        note_path,
        [
            "BFI1986-Theorem10",
            "DIBFIPrimarySourceSpecializationProof rejected",
            "NewFullSTheoremInput",
            "APSourceLift",
        ],
    )
    index_corrected = contains_all(
        external_index_path,
        [
            "BFI1986-Theorem10",
            "historical compatibility alias",
            "DI1982-Theorem12",
        ],
    )
    prior_ready = (
        full_s_kls_specialization["terminal_gap_after_router"]
        == "DIBFIPrimarySourceSpecializationProof"
    )
    q = Fraction(1, 2)
    s = Fraction(1, 2)
    minimal_w4_left = 5 * s + q
    w4_bound = Fraction(2, 1)
    full_s_exceeds_di_cone = minimal_w4_left > w4_bound
    return [
        {
            "gate": "PriorPrimarySourceGapAvailable",
            "closed": prior_ready,
            "evidence": "上一层已把外部合同版闭合后剩余单点定为 DIBFIPrimarySourceSpecializationProof。",
            "remaining": "none at prior-frontier level",
            "next_target": "BFIPrimarySourceCorrected",
        },
        {
            "gate": "BFIPrimarySourceCorrected",
            "closed": index_corrected and note_ready,
            "evidence": "Maynard 交叉来源显示 BFI Theorem 10 主来源是 1986 Acta Math；外部索引已修正。",
            "remaining": "需逐步替换历史 BFI1987 别名；但主定理定位不再含糊。",
            "next_target": "BFIAPAtomOnly",
        },
        {
            "gate": "BFIAPAtomOnly",
            "closed": note_ready,
            "evidence": "BFI Theorem 10 直接估计 well-factorable prime-AP discrepancy，不直接估计 non-AP KE-13/WFD full-S kernel。",
            "remaining": "若能证明 APSourceLift，则可回到直接 BFI；否则不能用 AP 定理关闭 non-AP kernel。",
            "next_target": "APSourceLiftOrNewFullSTheoremInput",
        },
        {
            "gate": "DIJScaleFullSObstruction",
            "closed": (
                note_ready
                and s_barrier["maynard_s_upper_bound_when_q_half"] == "3/10-o(1)"
                and s_nogo["forced_full_z_exponent"] == "1+o(1)"
                and full_s_exceeds_di_cone
            ),
            "evidence": (
                "DI/Maynard W4 condition n+2r+5s+q<=2 fails for q=s=1/2: "
                f"minimal left side={fmt_fraction(minimal_w4_left)}>{fmt_fraction(w4_bound)}。"
            ),
            "remaining": "现有 DI/Maynard J-scale 不能推出 full-S KLS-ext。",
            "next_target": "NewFullSTheoremInput",
        },
        {
            "gate": "DIBFIPrimarySourceSpecializationRejected",
            "closed": note_ready and full_s_exceeds_di_cone,
            "evidence": "现有 BFI AP theorem 与 DI J-scale 不推出本文自定义 full-S KLS-ext。",
            "remaining": "必须新增更强 full-S 外部定理，或证明当前 non-AP 对象可提升回 AP-source。",
            "next_target": "NewFullSTheoremInputOrAPSourceLift",
        },
        {
            "gate": "NewFullSTheoremInput",
            "closed": False,
            "evidence": "仓库尚无强于现有 DI/BFI J-scale、直接覆盖 S≈X^(1/2) full-S kernel 的定理。",
            "remaining": "需要独立外部深定理或新证明。",
            "next_target": "NewFullSTheoremInputOrAPSourceLift",
        },
        {
            "gate": "APSourceLift",
            "closed": False,
            "evidence": "此前 AP-source 分支已闭合，但 non-AP generic WFD fallback 没有无损提升回 AP discrepancy。",
            "remaining": "若证明该提升，可使用 BFI1986-Theorem10 直接闭合。",
            "next_target": "NewFullSTheoremInputOrAPSourceLift",
        },
    ]


def run(
    full_s_kls_specialization_path: Path,
    s_barrier_path: Path,
    s_nogo_path: Path,
    external_index_path: Path,
    note_path: Path,
) -> dict[str, Any]:
    """运行 primary-source no-go 路由。"""
    full_s_kls_specialization = load_json(full_s_kls_specialization_path)
    s_barrier = load_json(s_barrier_path)
    s_nogo = load_json(s_nogo_path)
    rows = build_rows(
        full_s_kls_specialization,
        s_barrier,
        s_nogo,
        external_index_path,
        note_path,
    )
    open_gates = [row["gate"] for row in rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_primary_source_specialization_nogo_router",
        "status": "dibfi_primary_source_specialization_rejected_new_theorem_or_ap_lift_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "full_s_kls_specialization_json": file_sha256(full_s_kls_specialization_path),
            "s_barrier_json": file_sha256(s_barrier_path),
            "s_nogo_json": file_sha256(s_nogo_path),
            "external_index_md": file_sha256(external_index_path),
            "note_md": file_sha256(note_path),
        },
        "previous_terminal_gap": full_s_kls_specialization["terminal_gap_after_router"],
        "nogo_rows": rows,
        "closed_nogo_gates": [row["gate"] for row in rows if row["closed"]],
        "open_nogo_gates": open_gates,
        "primary_source_specialization_closed": False,
        "terminal_gap_after_router": "NewFullSTheoremInputOrAPSourceLift",
        "terminal_gap_expansion": ["NewFullSTheoremInput", "APSourceLift"],
        "structural_law": (
            "The final primary-source check is not a missing citation. BFI Theorem 10, correctly "
            "located in the 1986 Acta Math paper, closes AP-source discrepancies with positive "
            "level slack, but the current remaining branch is non-AP WFD. The DI/Maynard "
            "Kloosterman J-scale cannot supply the custom full-S KLS-ext theorem when s=q=1/2, "
            "since n+2r+5s+q<=2 already fails before adding n and r. Therefore deriving "
            "FullS-KLS-ext from existing DI/BFI primary sources is rejected."
        ),
        "review_conclusion": (
            "`DIBFIPrimarySourceSpecializationProof` 被主来源尺度条件阻断：现有 BFI/DI 可闭合 "
            "AP-source 分支，但不能推出当前 full-S non-AP KLS-ext。最后剩余改写为 "
            "`NewFullSTheoremInputOrAPSourceLift`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI primary-source specialization no-go 路由器",
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
        f"- `primary_source_specialization_closed={fmt_bool(result['primary_source_specialization_closed'])}`。",
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
            "不能把 `DIBFIPrimarySourceSpecializationProof` 标记为已证。当前真实剩余为：",
            "",
            "```text",
            "NewFullSTheoremInputOrAPSourceLift:",
            "  NewFullSTheoremInput;",
            "  APSourceLift.",
            "```",
            "",
            "这一步排除的是“现有 DI/BFI 主来源可直接推出 full-S KLS-ext”的最后隐含跳步。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--full-s-kls-specialization-json",
        type=Path,
        default=DEFAULT_FULL_S_KLS_SPECIALIZATION,
    )
    parser.add_argument("--s-barrier-json", type=Path, default=DEFAULT_S_BARRIER)
    parser.add_argument("--s-nogo-json", type=Path, default=DEFAULT_S_NOGO)
    parser.add_argument("--external-index-md", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--note-md", type=Path, default=DEFAULT_NOTE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        full_s_kls_specialization_path=args.full_s_kls_specialization_json,
        s_barrier_path=args.s_barrier_json,
        s_nogo_path=args.s_nogo_json,
        external_index_path=args.external_index_md,
        note_path=args.note_md,
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
