#!/usr/bin/env python3
"""审计 APSourceLift 是否可由当前 non-AP generic WFD 分支无损推出。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_ap_source_lift_nogo_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_PRIMARY_SOURCE_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
)
DEFAULT_AP_SOURCE_BRANCH = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-branch-router.json"
DEFAULT_AP_RESIDUAL_IDENTITY = (
    DOCS / "prime-matrix-triad-a1-dibfi-ap-residual-identity-router.json"
)
DEFAULT_NONAP_OBJECT_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.json"
)
DEFAULT_TRANSFER_SCALE = (
    DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
)
DEFAULT_SOURCE_CEN_NO_GO = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_BD_CEN_AUDIT = DOCS / "prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.md"


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


def row_closed(rows: list[dict[str, Any]], gate: str) -> bool:
    """读取既有门控行是否关闭。"""
    for row in rows:
        if row.get("gate") == gate:
            return bool(row.get("closed"))
    return False


def build_rows(
    primary_source_nogo: dict[str, Any],
    ap_source_branch: dict[str, Any],
    ap_residual_identity: dict[str, Any],
    nonap_object_ledger: dict[str, Any],
    transfer_scale: dict[str, Any],
    source_cen_no_go_path: Path,
    bd_cen_audit_path: Path,
) -> list[dict[str, Any]]:
    """构造 APSourceLift no-go 审计行。"""
    prior_dual_gap = (
        primary_source_nogo["terminal_gap_after_router"]
        == "NewFullSTheoremInputOrAPSourceLift"
        and "APSourceLift" in primary_source_nogo["open_nogo_gates"]
    )
    branch_dichotomy_ready = (
        bool(ap_source_branch["ap_source_branch_closed"])
        and "NonAPSourceGenericWFD" in ap_source_branch["open_branches"]
    )
    source_identity_required = ap_residual_identity["open_gates"] == [
        "UpstreamCleanA1ResidualDefinition",
        "MainTermAndCoefficientMatch",
    ]
    no_downstream_backprojection = row_closed(
        ap_residual_identity["identity_rows"], "NoDownstreamBackProjectionShortcut"
    )
    transfer_marks_ap_open = "APErrorRepresentation" in transfer_scale["open_transfer_gates"]
    nonap_removes_ap = (
        bool(nonap_object_ledger["ap_error_representation_not_nonap_terminal"])
        and nonap_object_ledger["removed_nonap_transfer_gates"] == ["APErrorRepresentation"]
    )
    nonap_object_terminal_locked = nonap_object_ledger["open_object_gates"] == [
        "DispersionCauchyNoCenteringIdentity",
        "KE13DyadicExhaustionNoProjection",
    ]
    source_cen_blocks = contains_all(
        source_cen_no_go_path,
        [
            "SOURCE-CEN is false as an identity for current WFD-core",
            "external DI/BFI theorem route",
        ],
    )
    bd_cen_blocks = contains_all(
        bd_cen_audit_path,
        [
            "BD-CEN is not proved by the current KZ-E spine",
            "external DI/BFI",
        ],
    )
    projection_shortcut_blocked = source_cen_blocks and bd_cen_blocks
    lift_rejected = all(
        [
            prior_dual_gap,
            branch_dichotomy_ready,
            source_identity_required,
            no_downstream_backprojection,
            transfer_marks_ap_open,
            nonap_removes_ap,
            nonap_object_terminal_locked,
            projection_shortcut_blocked,
        ]
    )
    return [
        {
            "gate": "PriorDualGapContainsAPSourceLift",
            "closed": prior_dual_gap,
            "evidence": (
                f"previous={primary_source_nogo['terminal_gap_after_router']}; "
                f"open={primary_source_nogo['open_nogo_gates']}"
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "APSourceLift",
        },
        {
            "gate": "ExplicitAPNonAPDichotomy",
            "closed": branch_dichotomy_ready,
            "evidence": (
                "AP-source branch is closed only when source identity is declared upstream; "
                f"open_branches={ap_source_branch['open_branches']}."
            ),
            "remaining": "non-AP branch is the complement, not an implicit AP branch.",
            "next_target": "NoSilentAPUpgrade",
        },
        {
            "gate": "SourceIdentityRequiredAndStillMissing",
            "closed": source_identity_required and no_downstream_backprojection,
            "evidence": (
                f"AP identity open_gates={ap_residual_identity['open_gates']}; "
                "NoDownstreamBackProjectionShortcut is closed."
            ),
            "remaining": "APSourceLift would have to add a new upstream source identity.",
            "next_target": "NewSourceIdentityOrNewFullSTheoremInput",
        },
        {
            "gate": "TransferScaleDoesNotProvideAPRepresentation",
            "closed": transfer_marks_ap_open,
            "evidence": f"open_transfer_gates={transfer_scale['open_transfer_gates']}",
            "remaining": "APErrorRepresentation remains an open transfer gate, not a proved lift.",
            "next_target": "NewSourceIdentityOrNewFullSTheoremInput",
        },
        {
            "gate": "NonAPObjectLedgerRemovesAPError",
            "closed": nonap_removes_ap and nonap_object_terminal_locked,
            "evidence": (
                f"removed={nonap_object_ledger['removed_nonap_transfer_gates']}; "
                f"terminal={nonap_object_ledger['terminal_gap_after_router']}"
            ),
            "remaining": "non-AP object side is uncentered WFD-to-KE13 no-projection identity.",
            "next_target": "NewFullSTheoremInput",
        },
        {
            "gate": "ProjectionCenteringShortcutBlocked",
            "closed": projection_shortcut_blocked,
            "evidence": "SOURCE-CEN and BD-CEN block free centering/projection/back-projection.",
            "remaining": "no silent route from non-AP WFD object to prime-AP discrepancy.",
            "next_target": "NewFullSTheoremInput",
        },
        {
            "gate": "APSourceLiftRejected",
            "closed": lift_rejected,
            "evidence": (
                "A lift from the declared non-AP generic WFD complement to AP-source would "
                "contradict the current branch split unless a new source identity theorem is added."
            ),
            "remaining": "APSourceLift is rejected under the current contracts.",
            "next_target": "NewFullSTheoremInput",
        },
        {
            "gate": "NewFullSTheoremInput",
            "closed": False,
            "evidence": "No current DI/BFI primary-source theorem covers the full-S non-AP WFD kernel.",
            "remaining": "需要新增 full-S 外部深定理或新解析证明。",
            "next_target": "NewFullSTheoremInput",
        },
    ]


def run(
    primary_source_nogo_path: Path,
    ap_source_branch_path: Path,
    ap_residual_identity_path: Path,
    nonap_object_ledger_path: Path,
    transfer_scale_path: Path,
    source_cen_no_go_path: Path,
    bd_cen_audit_path: Path,
) -> dict[str, Any]:
    """运行 APSourceLift no-go 路由。"""
    primary_source_nogo = load_json(primary_source_nogo_path)
    ap_source_branch = load_json(ap_source_branch_path)
    ap_residual_identity = load_json(ap_residual_identity_path)
    nonap_object_ledger = load_json(nonap_object_ledger_path)
    transfer_scale = load_json(transfer_scale_path)
    rows = build_rows(
        primary_source_nogo,
        ap_source_branch,
        ap_residual_identity,
        nonap_object_ledger,
        transfer_scale,
        source_cen_no_go_path,
        bd_cen_audit_path,
    )
    ap_source_lift_rejected = any(
        row["gate"] == "APSourceLiftRejected" and row["closed"] for row in rows
    )
    open_terminal_gates = [
        row["gate"]
        for row in rows
        if not row["closed"] and row["gate"] == "NewFullSTheoremInput"
    ]
    return {
        "certificate_type": "triad_a1_dibfi_ap_source_lift_nogo_router",
        "status": "ap_source_lift_rejected_new_full_s_theorem_input_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "primary_source_nogo_json": file_sha256(primary_source_nogo_path),
            "ap_source_branch_json": file_sha256(ap_source_branch_path),
            "ap_residual_identity_json": file_sha256(ap_residual_identity_path),
            "nonap_object_ledger_json": file_sha256(nonap_object_ledger_path),
            "transfer_scale_json": file_sha256(transfer_scale_path),
            "source_cen_no_go_md": file_sha256(source_cen_no_go_path),
            "bd_cen_audit_md": file_sha256(bd_cen_audit_path),
        },
        "previous_terminal_gap": primary_source_nogo["terminal_gap_after_router"],
        "nogo_rows": rows,
        "closed_nogo_gates": [row["gate"] for row in rows if row["closed"]],
        "open_terminal_gates": open_terminal_gates,
        "rejected_gates": ["APSourceLift"] if ap_source_lift_rejected else [],
        "ap_source_lift_available": False,
        "ap_source_lift_rejected": ap_source_lift_rejected,
        "terminal_gap_after_router": "NewFullSTheoremInput",
        "terminal_gap_expansion": ["NewFullSTheoremInput"],
        "structural_law": (
            "APSourceLift is not an estimate; it is a source-level reclassification. The AP branch "
            "is legal only when the clean residual is declared before Cauchy/dispersion as a BFI "
            "prime-AP discrepancy with matching main term and coefficients. The non-AP generic WFD "
            "branch is the complement: its object ledger removes APErrorRepresentation and leaves "
            "only uncentered WFD-to-KE13 no-projection identities. SOURCE-CEN and BD-CEN block the "
            "free centering/projection shortcut. Therefore the current contracts reject a silent "
            "lift from non-AP WFD back to AP-source."
        ),
        "review_conclusion": (
            "`APSourceLift` 被当前分支定义和对象账本阻断：AP-source 只能作为上游源等式分支使用，"
            "non-AP generic WFD 补集不能无损回提为 BFI prime-AP discrepancy。剩余单点压成 "
            "`NewFullSTheoremInput`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI APSourceLift no-go 路由器",
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
        "rejected:",
        f"  {result['rejected_gates']};",
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
        f"- `ap_source_lift_available={fmt_bool(result['ap_source_lift_available'])}`。",
        f"- `ap_source_lift_rejected={fmt_bool(result['ap_source_lift_rejected'])}`。",
        f"- `closed_nogo_gates={result['closed_nogo_gates']}`。",
        f"- `open_terminal_gates={result['open_terminal_gates']}`。",
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
            "双点剩余已被压成单点：",
            "",
            "```text",
            "rejected:",
            "  APSourceLift;",
            "",
            "still open:",
            "  NewFullSTheoremInput.",
            "```",
            "",
            "这不是行命题完全闭合；它说明若不接受 FullS-KLS-ext 外部合同版，"
            "完全自足/主来源逐项版仍需要新的 full-S 定理输入或新证明。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--primary-source-nogo-json", type=Path, default=DEFAULT_PRIMARY_SOURCE_NOGO
    )
    parser.add_argument(
        "--ap-source-branch-json", type=Path, default=DEFAULT_AP_SOURCE_BRANCH
    )
    parser.add_argument(
        "--ap-residual-identity-json", type=Path, default=DEFAULT_AP_RESIDUAL_IDENTITY
    )
    parser.add_argument(
        "--nonap-object-ledger-json", type=Path, default=DEFAULT_NONAP_OBJECT_LEDGER
    )
    parser.add_argument("--transfer-scale-json", type=Path, default=DEFAULT_TRANSFER_SCALE)
    parser.add_argument("--source-cen-no-go-md", type=Path, default=DEFAULT_SOURCE_CEN_NO_GO)
    parser.add_argument("--bd-cen-audit-md", type=Path, default=DEFAULT_BD_CEN_AUDIT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        primary_source_nogo_path=args.primary_source_nogo_json,
        ap_source_branch_path=args.ap_source_branch_json,
        ap_residual_identity_path=args.ap_residual_identity_json,
        nonap_object_ledger_path=args.nonap_object_ledger_json,
        transfer_scale_path=args.transfer_scale_json,
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
                "ap_source_lift_rejected": result["ap_source_lift_rejected"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
