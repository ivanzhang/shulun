#!/usr/bin/env python3
"""把 NewFullSTheoremInput 压成唯一的 full-S non-AP WFD KLS 定理输入。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_new_full_s_theorem_input_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_AP_SOURCE_LIFT_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json"
)
DEFAULT_PRIMARY_SOURCE_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
)
DEFAULT_FULL_S_KLS_SPECIALIZATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
)
DEFAULT_FULL_S_KLS_NOTE = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization.md"
)
DEFAULT_SHORT_S_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-short-s-subwindow-nogo-router.json"
)
DEFAULT_MAYNARD_S_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.json"
)
DEFAULT_NONAP_OBJECT_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.json"
)
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_SOURCE_CEN_NO_GO = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_BD_CEN_AUDIT = DOCS / "prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.md"


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


def build_rows(
    ap_source_lift_nogo: dict[str, Any],
    primary_source_nogo: dict[str, Any],
    full_s_kls_specialization: dict[str, Any],
    full_s_kls_note_path: Path,
    short_s_nogo: dict[str, Any],
    maynard_s_nogo: dict[str, Any],
    nonap_object_ledger: dict[str, Any],
    kze_spine_path: Path,
    source_cen_no_go_path: Path,
    bd_cen_audit_path: Path,
) -> list[dict[str, Any]]:
    """构造新 full-S 定理输入账本。"""
    prior_single_gap = (
        ap_source_lift_nogo["terminal_gap_after_router"] == "NewFullSTheoremInput"
        and ap_source_lift_nogo["ap_source_lift_rejected"]
    )
    primary_sources_rejected = (
        primary_source_nogo["terminal_gap_after_router"]
        == "NewFullSTheoremInputOrAPSourceLift"
        and "NewFullSTheoremInput" in primary_source_nogo["open_nogo_gates"]
    )
    external_contract_ready = (
        full_s_kls_specialization["external_theorem_contract_closed"]
        and contains_all(
            full_s_kls_note_path,
            [
                "Theorem FullS-KLS-ext",
                "S≈P=X^(1/2+o(1))",
                "未中心化、无投影",
                "NaturalWFDScale",
            ],
        )
    )
    maynard_route_blocked = (
        maynard_s_nogo["terminal_gap_after_router"]
        == "ShortSSubwindowOrNewFullSDispersionAtom"
        and maynard_s_nogo["maynard_s_compression_map_closed"] is False
    )
    short_s_route_blocked = (
        short_s_nogo["terminal_gap_after_router"] == "NewFullSDispersionAtom"
        and short_s_nogo["short_s_subwindow_closed"] is False
    )
    nonap_object_is_target = (
        nonap_object_ledger["ap_error_representation_not_nonap_terminal"]
        and nonap_object_ledger["terminal_gap_after_router"]
        == "UncenteredWFDToKE13NoProjectionIdentity"
    )
    kze_core_named_open = contains_all(
        kze_spine_path,
        [
            "WFD-core",
            "(KE-13)",
            "尚未证明",
        ],
    )
    projection_routes_blocked = contains_all(
        source_cen_no_go_path,
        [
            "SOURCE-CEN is false as an identity for current WFD-core",
            "external DI/BFI theorem route",
        ],
    ) and contains_all(
        bd_cen_audit_path,
        [
            "BD-CEN is not proved by the current KZ-E spine",
            "external DI/BFI",
        ],
    )
    theorem_atom_pinned = all(
        [
            prior_single_gap,
            primary_sources_rejected,
            external_contract_ready,
            maynard_route_blocked,
            short_s_route_blocked,
            nonap_object_is_target,
            kze_core_named_open,
            projection_routes_blocked,
        ]
    )
    return [
        {
            "gate": "PriorSingleGapIsNewFullSTheoremInput",
            "closed": prior_single_gap,
            "evidence": (
                f"APSourceLift rejected={ap_source_lift_nogo['ap_source_lift_rejected']}; "
                f"terminal={ap_source_lift_nogo['terminal_gap_after_router']}."
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "FullSNonAPWFDKLSTheoremInput",
        },
        {
            "gate": "ExistingDIBFIPrimarySourcesRejected",
            "closed": primary_sources_rejected,
            "evidence": "BFI AP theorem and DI/Maynard J-scale do not imply the full-S non-AP WFD kernel.",
            "remaining": "不能把 NewFullSTheoremInput 写成现有 DI/BFI 主来源逐项推论。",
            "next_target": "FullSNonAPWFDKLSTheoremInput",
        },
        {
            "gate": "ExternalFullSContractAlreadyPinsStatement",
            "closed": external_contract_ready,
            "evidence": "FullS-KLS-ext 已写明 C≈P/log^O P, S≈P, H<=P/log^O P 和未中心化无投影对象。",
            "remaining": "外部合同版可引用；完全自足版仍需要新证明。",
            "next_target": "FullSNonAPWFDKLSTheoremInput",
        },
        {
            "gate": "MaynardAndShortSRoutesBlocked",
            "closed": maynard_route_blocked and short_s_route_blocked,
            "evidence": (
                "Maynard-S compression conflicts with full S; short-width subwindows do not reduce "
                "the Maynard magnitude."
            ),
            "remaining": "不能回到 W4 cone 或短 S 子窗口分解。",
            "next_target": "FullSNonAPWFDKLSTheoremInput",
        },
        {
            "gate": "NonAPUncenteredNoProjectionObjectPinned",
            "closed": nonap_object_is_target,
            "evidence": (
                "non-AP object ledger removes APErrorRepresentation and leaves "
                f"{nonap_object_ledger['terminal_gap_after_router']}."
            ),
            "remaining": "新定理必须直接估计当前 non-AP WFD 对象，不得换对象。",
            "next_target": "FullSNonAPWFDKLSTheoremInput",
        },
        {
            "gate": "SelfContainedCompletionKernelStillOpen",
            "closed": kze_core_named_open and projection_routes_blocked,
            "evidence": "KZ-E 已把内联账本压到 WFD-core；SOURCE-CEN/BD-CEN 阻断免费中心化投影。",
            "remaining": "完成型/Kuznetsov 自足证明仍等价于新增 full-S 深定理。",
            "next_target": "FullSNonAPWFDKLSTheoremInput",
        },
        {
            "gate": "FullSNonAPWFDKLSTheoremInputPinned",
            "closed": theorem_atom_pinned,
            "evidence": "所有旧出口已分类；唯一剩余是一个直接作用于 full-S non-AP WFD 的 KLS 定理输入。",
            "remaining": "none at target-definition level",
            "next_target": "FullSNonAPWFDKLSTheoremInput",
        },
        {
            "gate": "FullSNonAPWFDKLSTheoremInput",
            "closed": False,
            "evidence": "仓库尚无该新定理的外部主来源引用或自足解析证明。",
            "remaining": "提交外部深定理引用，或证明完整 full-S non-AP WFD KLS 估计。",
            "next_target": "FullSNonAPWFDKLSTheoremInput",
        },
    ]


def run(
    ap_source_lift_nogo_path: Path,
    primary_source_nogo_path: Path,
    full_s_kls_specialization_path: Path,
    full_s_kls_note_path: Path,
    short_s_nogo_path: Path,
    maynard_s_nogo_path: Path,
    nonap_object_ledger_path: Path,
    kze_spine_path: Path,
    source_cen_no_go_path: Path,
    bd_cen_audit_path: Path,
) -> dict[str, Any]:
    """运行新 full-S 定理输入路由。"""
    ap_source_lift_nogo = load_json(ap_source_lift_nogo_path)
    primary_source_nogo = load_json(primary_source_nogo_path)
    full_s_kls_specialization = load_json(full_s_kls_specialization_path)
    short_s_nogo = load_json(short_s_nogo_path)
    maynard_s_nogo = load_json(maynard_s_nogo_path)
    nonap_object_ledger = load_json(nonap_object_ledger_path)
    rows = build_rows(
        ap_source_lift_nogo,
        primary_source_nogo,
        full_s_kls_specialization,
        full_s_kls_note_path,
        short_s_nogo,
        maynard_s_nogo,
        nonap_object_ledger,
        kze_spine_path,
        source_cen_no_go_path,
        bd_cen_audit_path,
    )
    return {
        "certificate_type": "triad_a1_dibfi_new_full_s_theorem_input_router",
        "status": "new_full_s_theorem_input_reduced_to_full_s_nonap_wfd_kls_input_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "ap_source_lift_nogo_json": file_sha256(ap_source_lift_nogo_path),
            "primary_source_nogo_json": file_sha256(primary_source_nogo_path),
            "full_s_kls_specialization_json": file_sha256(full_s_kls_specialization_path),
            "full_s_kls_note_md": file_sha256(full_s_kls_note_path),
            "short_s_nogo_json": file_sha256(short_s_nogo_path),
            "maynard_s_nogo_json": file_sha256(maynard_s_nogo_path),
            "nonap_object_ledger_json": file_sha256(nonap_object_ledger_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "source_cen_no_go_md": file_sha256(source_cen_no_go_path),
            "bd_cen_audit_md": file_sha256(bd_cen_audit_path),
        },
        "previous_terminal_gap": ap_source_lift_nogo["terminal_gap_after_router"],
        "theorem_input_rows": rows,
        "closed_input_gates": [row["gate"] for row in rows if row["closed"]],
        "open_input_gates": [row["gate"] for row in rows if not row["closed"]],
        "new_full_s_theorem_input_closed": False,
        "terminal_gap_after_router": "FullSNonAPWFDKLSTheoremInput",
        "terminal_gap_expansion": ["FullSNonAPWFDKLSTheoremInput"],
        "required_theorem_clauses": [
            "object: current non-AP uncentered no-projection WFD window",
            "range: X≈P^2, C≈P/log^O P, S≈P, 0<|h|<=H<=P/log^O P",
            "weights: lambda well-factorable, beta divisor-bounded, omega smooth",
            "loss: dyadic/gcd/smoothing endpoints absorbed into B(A)",
            "strength: NaturalWFDScale/log^A P for every A>0",
            "boundary: no AP-source lift, no Maynard-W4 compression, no hidden centering/projection",
        ],
        "structural_law": (
            "NewFullSTheoremInput is not another combinatorial branch. All old exits are blocked: "
            "existing DI/BFI primary sources do not imply the full-S non-AP WFD kernel; APSourceLift "
            "is rejected; Maynard-W4 and short-S routes are rejected; SOURCE-CEN/BD-CEN block hidden "
            "projection. The remaining atom is therefore a single theorem input: a Kloosterman large "
            "sieve/dispersion estimate for the current full-S, uncentered, non-projected non-AP WFD "
            "window with arbitrary log saving."
        ),
        "review_conclusion": (
            "`NewFullSTheoremInput` 已被压成唯一可审稿原子 "
            "`FullSNonAPWFDKLSTheoremInput`。这一步没有证明新定理；它完成了目标定义层闭合，"
            "把剩余变成一个必须引用或新证的 full-S non-AP WFD KLS 定理。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI NewFullSTheoremInput 路由器",
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
        f"- `new_full_s_theorem_input_closed={fmt_bool(result['new_full_s_theorem_input_closed'])}`。",
        f"- `closed_input_gates={result['closed_input_gates']}`。",
        f"- `open_input_gates={result['open_input_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 必要定理条款",
        "",
    ]
    for clause in result["required_theorem_clauses"]:
        lines.append(f"- `{clause}`。")
    lines.extend(
        [
            "",
            "## 4. 定理输入账本表",
            "",
            "| gate | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["theorem_input_rows"]:
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
            "唯一剩余已从泛称压成具体原子：",
            "",
            "```text",
            "FullSNonAPWFDKLSTheoremInput:",
            "  prove or cite a full-S Kloosterman large-sieve/dispersion theorem",
            "  for the current non-AP uncentered no-projection WFD window.",
            "```",
            "",
            "因此外部合同版可以接受 FullS-KLS-ext 作为输入；完全自足版仍未闭合，"
            "因为该 full-S 定理本身尚未在仓库内证明。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ap-source-lift-nogo-json", type=Path, default=DEFAULT_AP_SOURCE_LIFT_NOGO
    )
    parser.add_argument(
        "--primary-source-nogo-json", type=Path, default=DEFAULT_PRIMARY_SOURCE_NOGO
    )
    parser.add_argument(
        "--full-s-kls-specialization-json",
        type=Path,
        default=DEFAULT_FULL_S_KLS_SPECIALIZATION,
    )
    parser.add_argument("--full-s-kls-note-md", type=Path, default=DEFAULT_FULL_S_KLS_NOTE)
    parser.add_argument("--short-s-nogo-json", type=Path, default=DEFAULT_SHORT_S_NOGO)
    parser.add_argument("--maynard-s-nogo-json", type=Path, default=DEFAULT_MAYNARD_S_NOGO)
    parser.add_argument(
        "--nonap-object-ledger-json", type=Path, default=DEFAULT_NONAP_OBJECT_LEDGER
    )
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--source-cen-no-go-md", type=Path, default=DEFAULT_SOURCE_CEN_NO_GO)
    parser.add_argument("--bd-cen-audit-md", type=Path, default=DEFAULT_BD_CEN_AUDIT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        ap_source_lift_nogo_path=args.ap_source_lift_nogo_json,
        primary_source_nogo_path=args.primary_source_nogo_json,
        full_s_kls_specialization_path=args.full_s_kls_specialization_json,
        full_s_kls_note_path=args.full_s_kls_note_md,
        short_s_nogo_path=args.short_s_nogo_json,
        maynard_s_nogo_path=args.maynard_s_nogo_json,
        nonap_object_ledger_path=args.nonap_object_ledger_json,
        kze_spine_path=args.kze_spine_md,
        source_cen_no_go_path=args.source_cen_no_go_md,
        bd_cen_audit_path=args.bd_cen_audit_md,
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
                "terminal_gap_after_router": result["terminal_gap_after_router"],
                "open_input_gates": result["open_input_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
