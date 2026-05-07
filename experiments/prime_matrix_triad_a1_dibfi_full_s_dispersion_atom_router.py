#!/usr/bin/env python3
"""审计 full-S 原始 dispersion 原子的真实剩余。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_full_s_dispersion_atom_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-dispersion-atom-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-dispersion-atom-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_SHORT_S_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-short-s-subwindow-nogo-router.json"
)
DEFAULT_THEOREM_LOCATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
)
DEFAULT_DIRECT_BFI_ATOM = (
    DOCS / "prime-matrix-triad-a1-dibfi-direct-bfi-atom-router.json"
)
DEFAULT_AP_SOURCE_BRANCH = (
    DOCS / "prime-matrix-triad-a1-dibfi-ap-source-branch-router.json"
)
DEFAULT_NONAP_OBJECT_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.json"
)
DEFAULT_NCBLK_PROJECTION = (
    DOCS / "prime-matrix-triad-a1-ncblk-projection-gap-router.json"
)
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_NOTE = DOCS / "prime-matrix-triad-a1-dibfi-full-s-dispersion-atom-note.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-full-s-dispersion-atom-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-full-s-dispersion-atom-router.md"


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


def build_atom_rows(
    short_s_nogo: dict[str, Any],
    theorem_location: dict[str, Any],
    direct_bfi_atom: dict[str, Any],
    ap_source_branch: dict[str, Any],
    nonap_object_ledger: dict[str, Any],
    ncblk_projection: dict[str, Any],
    kze_spine_path: Path,
    note_path: Path,
) -> list[dict[str, Any]]:
    """构造 full-S 原子审计行。"""
    note_ready = contains_all(
        note_path,
        [
            "FullSOriginalDIBFIAtom",
            "S_common≈X^(1/2)",
            "z≈X",
            "ExternalFullSDIBFIAtomMatch",
            "UncenteredWFDToKE13NoProjectionIdentity",
        ],
    )
    kze_core_present_but_open = contains_all(
        kze_spine_path,
        [
            "WFD-core",
            "(KE-13)",
            "尚未证明",
        ],
    )
    theorem_locations_pinned = bool(theorem_location["theorem_locations_pinned"])
    ap_direct_closed_nonap_open = (
        bool(ap_source_branch["ap_source_branch_closed"])
        and "NonAPSourceGenericWFD" in ap_source_branch["open_branches"]
    )
    nonap_object_open = (
        nonap_object_ledger["terminal_gap_after_router"]
        == "UncenteredWFDToKE13NoProjectionIdentity"
        and bool(nonap_object_ledger["open_object_gates"])
    )
    external_dibfi_open = (
        ncblk_projection["external_route_status"]
        == "open_needs_precise_di_bfi_original_dispersion_citation"
    )
    return [
        {
            "gate": "PriorNewFullSAtomFrontierAvailable",
            "closed": short_s_nogo["terminal_gap_after_router"] == "NewFullSDispersionAtom",
            "evidence": "短 S 子窗口退路已排除，上游终端单点化为 NewFullSDispersionAtom。",
            "remaining": "none at prior-frontier level",
            "next_target": "FullSAtomStatementPinned",
        },
        {
            "gate": "FullSAtomStatementPinned",
            "closed": note_ready,
            "evidence": "full-S 原子被固定为 S_common≈X^(1/2)、z≈X 的原始 DI/BFI dispersion 输入。",
            "remaining": "none at statement-naming level",
            "next_target": "ExternalFullSDIBFIAtomMatch",
        },
        {
            "gate": "MaynardW4RouteAlreadyRejected",
            "closed": short_s_nogo["open_subwindow_gates"] == ["NewFullSDispersionAtom"],
            "evidence": "Maynard W4 路线需要 S_May<=X^(3/10-o(1))；full-S 保留会强制 S_May≈X^(1/2)。",
            "remaining": "不能再从 Maynard-W4 锥内取得 full-S 结论。",
            "next_target": "ExternalFullSDIBFIAtomMatch",
        },
        {
            "gate": "ExistingKZEWFDCoreIsSameShapeButOpen",
            "closed": kze_core_present_but_open,
            "evidence": "KZ-E spine 已有 KE-13/WFD-core 形状，但文档明确标注该核尚未自足证明。",
            "remaining": "不能把 KE-13/WFD-core 当作已闭合 full-S 原子。",
            "next_target": "ExternalFullSDIBFIAtomMatch",
        },
        {
            "gate": "DirectBFIAPBranchDoesNotCloseNonAPFullS",
            "closed": ap_direct_closed_nonap_open and bool(direct_bfi_atom["direct_bfi_atom_available"]),
            "evidence": "AP-source 直接 BFI 分支已闭合；当前剩余是 non-AP generic WFD fallback。",
            "remaining": "必须给出 non-AP full-S 原始 dispersion 假设匹配，或回到无投影对象恒等式。",
            "next_target": "ExternalFullSDIBFIAtomMatch",
        },
        {
            "gate": "OriginalDIBFITheoremLocationsPinned",
            "closed": theorem_locations_pinned,
            "evidence": "外部 DI/BFI 定理位置已固定为 BFI Theorem 10 与 DI Theorem 12。",
            "remaining": "定理位置不是问题；问题是 full-S 当前窗口假设逐项匹配。",
            "next_target": "ExternalFullSDIBFIAtomMatch",
        },
        {
            "gate": "UncenteredNoProjectionCompatibilityStillOpen",
            "closed": False,
            "evidence": (
                "non-AP 对象账本仍开放："
                f"{nonap_object_ledger['open_object_gates']}。"
            ),
            "remaining": "证明 full-S 外部原子应用时没有隐藏中心化、投影或 dyadic 主块遗漏。",
            "next_target": "UncenteredWFDToKE13NoProjectionIdentity",
        },
        {
            "gate": "ExternalFullSDIBFIAtomMatch",
            "closed": False,
            "evidence": (
                "NC-BLK 外部路由也要求 precise DI/BFI original dispersion citation；"
                f"external_dibfi_open={external_dibfi_open}。"
            ),
            "remaining": (
                "需要写出 full-S 原始 dispersion 定理/引用合同，并逐项验证当前 "
                "S_common≈X^(1/2)、z≈X 窗口满足其假设。"
            ),
            "next_target": "ExternalFullSDIBFIAtomMatch",
        },
    ]


def run(
    short_s_nogo_path: Path,
    theorem_location_path: Path,
    direct_bfi_atom_path: Path,
    ap_source_branch_path: Path,
    nonap_object_ledger_path: Path,
    ncblk_projection_path: Path,
    kze_spine_path: Path,
    note_path: Path,
) -> dict[str, Any]:
    """运行 full-S 原子路由。"""
    short_s_nogo = load_json(short_s_nogo_path)
    theorem_location = load_json(theorem_location_path)
    direct_bfi_atom = load_json(direct_bfi_atom_path)
    ap_source_branch = load_json(ap_source_branch_path)
    nonap_object_ledger = load_json(nonap_object_ledger_path)
    ncblk_projection = load_json(ncblk_projection_path)
    atom_rows = build_atom_rows(
        short_s_nogo,
        theorem_location,
        direct_bfi_atom,
        ap_source_branch,
        nonap_object_ledger,
        ncblk_projection,
        kze_spine_path,
        note_path,
    )
    open_atom_gates = [row["gate"] for row in atom_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_full_s_dispersion_atom_router",
        "status": "full_s_dispersion_atom_reduced_to_external_dibfi_match_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "short_s_nogo_json": file_sha256(short_s_nogo_path),
            "theorem_location_json": file_sha256(theorem_location_path),
            "direct_bfi_atom_json": file_sha256(direct_bfi_atom_path),
            "ap_source_branch_json": file_sha256(ap_source_branch_path),
            "nonap_object_ledger_json": file_sha256(nonap_object_ledger_path),
            "ncblk_projection_json": file_sha256(ncblk_projection_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "note_md": file_sha256(note_path),
        },
        "previous_terminal_gap": short_s_nogo["terminal_gap_after_router"],
        "atom_rows": atom_rows,
        "closed_atom_gates": [row["gate"] for row in atom_rows if row["closed"]],
        "open_atom_gates": open_atom_gates,
        "full_s_dispersion_atom_closed": False,
        "terminal_gap_after_router": "ExternalFullSDIBFIAtomMatch",
        "terminal_gap_expansion": [
            "ExternalFullSDIBFIAtomMatch",
            "UncenteredWFDToKE13NoProjectionIdentity",
        ],
        "structural_law": (
            "The latest scale gap is no longer a parameter optimization problem. Maynard-W4 "
            "cannot accept S≈X^(1/2) when q≈1/2, short-S subwindows do not change the magnitude "
            "of z=s1*s2, and the existing KE-13/WFD-core text is an open deep kernel rather than "
            "a closed proof. Thus the honest full-S route is a precise original DI/BFI dispersion "
            "atom for the current full-S window, with no hidden centering/projection."
        ),
        "review_conclusion": (
            "`NewFullSDispersionAtom` 已被精确改写为 `ExternalFullSDIBFIAtomMatch`："
            "要么提交适配 S_common≈X^(1/2)、z≈X 的原始 DI/BFI full-S 定理合同，"
            "要么继续攻 non-AP 对象侧的未中心化无投影恒等式。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI full-S dispersion atom 路由器",
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
        f"- `full_s_dispersion_atom_closed={fmt_bool(result['full_s_dispersion_atom_closed'])}`。",
        f"- `closed_atom_gates={result['closed_atom_gates']}`。",
        f"- `open_atom_gates={result['open_atom_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 原子账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["atom_rows"]:
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
            "最新最窄剩余为：",
            "",
            "```text",
            "ExternalFullSDIBFIAtomMatch:",
            "  full-S original DI/BFI theorem/citation for S_common≈X^(1/2), z≈X;",
            "  current-window hypothesis match;",
            "  no hidden centering/projection in the non-AP WFD application.",
            "```",
            "",
            "这一步没有宣称行命题闭合；它把 full-S 缺口从笼统新原子改成可审计外部定理合同。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--short-s-nogo-json", type=Path, default=DEFAULT_SHORT_S_NOGO)
    parser.add_argument("--theorem-location-json", type=Path, default=DEFAULT_THEOREM_LOCATION)
    parser.add_argument("--direct-bfi-atom-json", type=Path, default=DEFAULT_DIRECT_BFI_ATOM)
    parser.add_argument("--ap-source-branch-json", type=Path, default=DEFAULT_AP_SOURCE_BRANCH)
    parser.add_argument(
        "--nonap-object-ledger-json", type=Path, default=DEFAULT_NONAP_OBJECT_LEDGER
    )
    parser.add_argument("--ncblk-projection-json", type=Path, default=DEFAULT_NCBLK_PROJECTION)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--note-md", type=Path, default=DEFAULT_NOTE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        short_s_nogo_path=args.short_s_nogo_json,
        theorem_location_path=args.theorem_location_json,
        direct_bfi_atom_path=args.direct_bfi_atom_json,
        ap_source_branch_path=args.ap_source_branch_json,
        nonap_object_ledger_path=args.nonap_object_ledger_json,
        ncblk_projection_path=args.ncblk_projection_json,
        kze_spine_path=args.kze_spine_md,
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
                "open_atom_gates": result["open_atom_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
