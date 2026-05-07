#!/usr/bin/env python3
"""审计是否存在绕开 Maynard-S 压缩的已登记 W4 替代路由。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_alternate_w4_reroute_audit_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-alternate-w4-reroute-audit-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-alternate-w4-reroute-audit-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_S_COMPRESSION_BARRIER = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-barrier-router.json"
)
DEFAULT_DIRECT_BFI_ATOM = (
    DOCS / "prime-matrix-triad-a1-dibfi-direct-bfi-atom-router.json"
)
DEFAULT_AP_SOURCE_BRANCH = (
    DOCS / "prime-matrix-triad-a1-dibfi-ap-source-branch-router.json"
)
DEFAULT_NONAP_DISPERSION = (
    DOCS / "prime-matrix-triad-a1-dibfi-nonap-dispersion-router.json"
)
DEFAULT_AUDIT_NOTE = (
    DOCS / "prime-matrix-triad-a1-dibfi-alternate-w4-reroute-audit-note.md"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-alternate-w4-reroute-audit-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-alternate-w4-reroute-audit-router.md"
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


def build_reroute_rows(
    s_compression_barrier: dict[str, Any],
    direct_bfi_atom: dict[str, Any],
    ap_source_branch: dict[str, Any],
    nonap_dispersion: dict[str, Any],
    audit_note_path: Path,
) -> list[dict[str, Any]]:
    """构造替代路由审计账本行。"""
    note_ready = contains_all(
        audit_note_path,
        [
            "APSourceDirectBFI",
            "NonAPSourceGenericWFD",
            "HLCWindowedKLSAtom",
            "MaynardSCompressionMap",
        ],
    )
    prior_ready = (
        s_compression_barrier["terminal_gap_after_router"]
        == "MaynardSCompressionMapOrAlternateW4Rerouting"
    )
    direct_bfi_has_ap_scope = direct_bfi_atom["terminal_gap_after_router"] == (
        "DIBFIDirectBFIAPAtomMatchOrKE13NoProjection"
    )
    ap_closed_nonap_open = (
        ap_source_branch["ap_source_branch_closed"]
        and not ap_source_branch["generic_nonap_fallback_closed"]
    )
    nonap_returns_same_fallback = nonap_dispersion["terminal_gap_after_router"] == (
        "DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource"
    )
    return [
        {
            "gate": "PriorSCompressionBarrierAvailable",
            "closed": prior_ready,
            "evidence": "上游已把朴素 S_common=S_May 同一化排除，并留下压缩/替代二选一。",
            "remaining": "none at prior-barrier level",
            "next_target": "NoRegisteredClosedAlternateW4Route",
        },
        {
            "gate": "DirectBFIAtomScopeAPOnly",
            "closed": direct_bfi_has_ap_scope and ap_closed_nonap_open,
            "evidence": "直接 BFI 原子只在 AP-source 分支闭合；非 AP generic WFD 不能静默升级。",
            "remaining": "若要用直接 BFI，必须重新证明源头 AP residual identity。",
            "next_target": "NoRegisteredClosedAlternateW4Route",
        },
        {
            "gate": "HLCWindowedKLSAtomScopeCleanOnly",
            "closed": note_ready,
            "evidence": "HLCWindowedKLSAtom 只覆盖 clean HLC 分支，不替代 generic WFD 共同变量表。",
            "remaining": "none for current non-AP generic WFD route",
            "next_target": "NoRegisteredClosedAlternateW4Route",
        },
        {
            "gate": "NonAPFallbackReturnsToSameKE13Route",
            "closed": nonap_returns_same_fallback,
            "evidence": "非 AP fallback 回到无投影 KE-13/量化窗口代入；这正是当前 Maynard-W4 链条。",
            "remaining": "不是独立闭合出口。",
            "next_target": "NoRegisteredClosedAlternateW4Route",
        },
        {
            "gate": "NoRegisteredClosedAlternateW4Route",
            "closed": note_ready
            and direct_bfi_has_ap_scope
            and ap_closed_nonap_open
            and nonap_returns_same_fallback,
            "evidence": "当前已登记原子中没有可绕开 Maynard-S 压缩并闭合非 AP generic WFD 的替代路由。",
            "remaining": "只有新增外部原始 dispersion 原子才会重开该出口。",
            "next_target": "MaynardSCompressionMap",
        },
        {
            "gate": "MaynardSCompressionMap",
            "closed": False,
            "evidence": "仍需从 s1,s2,h,completion 结构中构造 S_May<=X^(3/10-o(1))。",
            "remaining": "当前最终尺度硬点。",
            "next_target": "MaynardSCompressionMap",
        },
    ]


def run(
    s_compression_barrier_path: Path,
    direct_bfi_atom_path: Path,
    ap_source_branch_path: Path,
    nonap_dispersion_path: Path,
    audit_note_path: Path,
) -> dict[str, Any]:
    """运行替代 W4 路由审计。"""
    s_compression_barrier = load_json(s_compression_barrier_path)
    direct_bfi_atom = load_json(direct_bfi_atom_path)
    ap_source_branch = load_json(ap_source_branch_path)
    nonap_dispersion = load_json(nonap_dispersion_path)
    reroute_rows = build_reroute_rows(
        s_compression_barrier,
        direct_bfi_atom,
        ap_source_branch,
        nonap_dispersion,
        audit_note_path,
    )
    open_reroute_gates = [row["gate"] for row in reroute_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_alternate_w4_reroute_audit_router",
        "status": "alternate_w4_reroute_rejected_maynard_s_compression_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "s_compression_barrier_json": file_sha256(s_compression_barrier_path),
            "direct_bfi_atom_json": file_sha256(direct_bfi_atom_path),
            "ap_source_branch_json": file_sha256(ap_source_branch_path),
            "nonap_dispersion_json": file_sha256(nonap_dispersion_path),
            "audit_note_md": file_sha256(audit_note_path),
        },
        "previous_terminal_gap": s_compression_barrier["terminal_gap_after_router"],
        "reroute_rows": reroute_rows,
        "closed_reroute_gates": [
            row["gate"] for row in reroute_rows if row["closed"]
        ],
        "open_reroute_gates": open_reroute_gates,
        "alternate_w4_reroute_closed": False,
        "terminal_gap_after_router": "MaynardSCompressionMap",
        "terminal_gap_expansion": ["MaynardSCompressionMap"],
        "structural_law": (
            "No registered closed alternate W4 object route is available for the non-AP generic "
            "WFD branch. Direct BFI is AP-source only, HLCWindowedKLS is clean-HLC only, and the "
            "non-AP fallback returns to the same KE-13/DI-Maynard chain. The remaining scale "
            "hard point is MaynardSCompressionMap."
        ),
        "review_conclusion": (
            "替代 W4 对象路由在当前合同下被排除；非 AP generic WFD 的尺度侧剩余单点化为"
            " `MaynardSCompressionMap`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI alternate W4 reroute audit 路由器",
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
        f"- `alternate_w4_reroute_closed={fmt_bool(result['alternate_w4_reroute_closed'])}`。",
        f"- `closed_reroute_gates={result['closed_reroute_gates']}`。",
        f"- `open_reroute_gates={result['open_reroute_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 替代路由账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["reroute_rows"]:
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
            "当前尺度侧最终硬点为：",
            "",
            "```text",
            "MaynardSCompressionMap:",
            "  construct S_May from s1,s2,h,completion;",
            "  prove S_May <= X^(3/10-o(1)).",
            "```",
            "",
            "这一步排除的是已登记替代出口；它没有证明 S 压缩映射本身。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--s-compression-barrier-json",
        type=Path,
        default=DEFAULT_S_COMPRESSION_BARRIER,
    )
    parser.add_argument("--direct-bfi-atom-json", type=Path, default=DEFAULT_DIRECT_BFI_ATOM)
    parser.add_argument("--ap-source-branch-json", type=Path, default=DEFAULT_AP_SOURCE_BRANCH)
    parser.add_argument("--nonap-dispersion-json", type=Path, default=DEFAULT_NONAP_DISPERSION)
    parser.add_argument("--audit-note-md", type=Path, default=DEFAULT_AUDIT_NOTE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        s_compression_barrier_path=args.s_compression_barrier_json,
        direct_bfi_atom_path=args.direct_bfi_atom_json,
        ap_source_branch_path=args.ap_source_branch_json,
        nonap_dispersion_path=args.nonap_dispersion_json,
        audit_note_path=args.audit_note_md,
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
                "open_reroute_gates": result["open_reroute_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
