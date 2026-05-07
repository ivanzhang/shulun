#!/usr/bin/env python3
"""压缩非 AP-source 分支的对象侧无投影账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_nonap_object_ledger_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_NONAP_DISPERSION = DOCS / "prime-matrix-triad-a1-dibfi-nonap-dispersion-router.json"
DEFAULT_AP_SOURCE_BRANCH = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-branch-router.json"
DEFAULT_TRANSFER_SCALE = (
    DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_SOURCE_CEN_NO_GO = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_BD_CEN_AUDIT = DOCS / "prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.md"


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


def build_object_rows(
    nonap_dispersion: dict[str, Any],
    ap_source_branch: dict[str, Any],
    transfer_scale: dict[str, Any],
    common_variable_table: dict[str, Any],
    source_cen_no_go_path: Path,
    bd_cen_audit_path: Path,
) -> list[dict[str, Any]]:
    """构造非 AP-source 对象侧账本。"""
    open_transfer = set(transfer_scale["open_transfer_gates"])
    source_cen_blocks_centering = contains_all(
        source_cen_no_go_path,
        [
            "SOURCE-CEN is false as an identity for current WFD-core",
            "external DI/BFI theorem route",
        ],
    )
    bd_cen_blocks_projection = contains_all(
        bd_cen_audit_path,
        [
            "BD-CEN is not proved by the current KZ-E spine",
            "external DI/BFI",
        ],
    )
    nonap_open = "NonAPSourceGenericWFD" in ap_source_branch["open_branches"]
    ap_branch_closed = bool(ap_source_branch["ap_source_branch_closed"])
    transfer_rows = common_variable_table["transfer_rows"]
    table_has_object_rows = any(
        row["step"] == "DispersionCauchy" and not row["target_preserved"]
        for row in transfer_rows
    ) and any(
        row["step"] == "KE13Identification" and not row["target_preserved"]
        for row in transfer_rows
    )
    return [
        {
            "gate": "APErrorRepresentationSeparated",
            "closed": ap_branch_closed and nonap_open,
            "evidence": (
                "AP-source 直接 BFI 分支已闭合；非 AP generic WFD 是其补集，"
                "不能把 APErrorRepresentation 当作非 AP fallback 的对象终端。"
            ),
            "remaining": "none for non-AP object ledger",
            "next_target": "UncenteredWFDToKE13NoProjectionIdentity",
        },
        {
            "gate": "NoSilentProjectionOrCentering",
            "closed": source_cen_blocks_centering and bd_cen_blocks_projection,
            "evidence": (
                "SOURCE-CEN 会改变 WFD 目标对象；BD-CEN 只证明 h=0 主项抵消，"
                "未证明同块中心化扣除。"
            ),
            "remaining": "不能免费插入块中心化、投影或删同块对角。",
            "next_target": "DispersionCauchyNoCenteringIdentity",
        },
        {
            "gate": "DispersionCauchyNoCenteringIdentity",
            "closed": False,
            "evidence": (
                "该门仍在 transfer-scale open_transfer_gates 中；需要从 BFI 原始 "
                "dispersion/Cauchy 展开逐项得到当前未中心化对象。"
            ),
            "remaining": "写出 E_{N,M}->E_disp 的逐项恒等式，确认没有块中心化插入和同块对角删除。",
            "next_target": "UncenteredWFDToKE13NoProjectionIdentity",
        },
        {
            "gate": "KE13DyadicExhaustionNoProjection",
            "closed": False,
            "evidence": (
                "共同变量表已定位 KE13Identification 为 target_preserved=false；"
                "所有 dyadic 主块是否完全覆盖 WFD_core 尚未证明。"
            ),
            "remaining": "证明主非零频块完全等于 WFD_core(C,S,H,lambda,beta,omega)，且无端点遗漏。",
            "next_target": "UncenteredWFDToKE13NoProjectionIdentity",
        },
        {
            "gate": "ObjectTerminalDefined",
            "closed": table_has_object_rows
            and {"DispersionCauchyNoCenteringIdentity", "KE13DyadicExhaustionNoProjection"}
            .issubset(open_transfer),
            "evidence": (
                f"nonap terminal targets={nonap_dispersion['open_terminal_targets']}；"
                "对象侧只保留两个未闭合恒等式。"
            ),
            "remaining": "two object identities remain open",
            "next_target": "UncenteredWFDToKE13NoProjectionIdentity",
        },
    ]


def run(
    nonap_dispersion_path: Path,
    ap_source_branch_path: Path,
    transfer_scale_path: Path,
    common_variable_table_path: Path,
    source_cen_no_go_path: Path,
    bd_cen_audit_path: Path,
) -> dict[str, Any]:
    """运行非 AP-source 对象侧账本路由。"""
    nonap_dispersion = load_json(nonap_dispersion_path)
    ap_source_branch = load_json(ap_source_branch_path)
    transfer_scale = load_json(transfer_scale_path)
    common_variable_table = load_json(common_variable_table_path)
    object_rows = build_object_rows(
        nonap_dispersion,
        ap_source_branch,
        transfer_scale,
        common_variable_table,
        source_cen_no_go_path,
        bd_cen_audit_path,
    )
    open_object_gates = [
        row["gate"]
        for row in object_rows
        if not row["closed"]
        and row["gate"]
        in ["DispersionCauchyNoCenteringIdentity", "KE13DyadicExhaustionNoProjection"]
    ]
    return {
        "certificate_type": "triad_a1_dibfi_nonap_object_ledger_router",
        "status": "nonap_object_ledger_reduced_to_uncentered_wfd_no_projection_identity_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "nonap_dispersion_json": file_sha256(nonap_dispersion_path),
            "ap_source_branch_json": file_sha256(ap_source_branch_path),
            "transfer_scale_json": file_sha256(transfer_scale_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "source_cen_no_go_md": file_sha256(source_cen_no_go_path),
            "bd_cen_audit_md": file_sha256(bd_cen_audit_path),
        },
        "previous_terminal_gap": nonap_dispersion["terminal_gap_after_router"],
        "object_rows": object_rows,
        "removed_nonap_transfer_gates": ["APErrorRepresentation"],
        "open_object_gates": open_object_gates,
        "closed_object_gates": [row["gate"] for row in object_rows if row["closed"]],
        "ap_error_representation_not_nonap_terminal": True,
        "nonap_object_ledger_closed": False,
        "terminal_gap_after_router": "UncenteredWFDToKE13NoProjectionIdentity",
        "terminal_gap_expansion": [
            "DispersionCauchyNoCenteringIdentity",
            "KE13DyadicExhaustionNoProjection",
        ],
        "structural_law": (
            "The non-AP fallback object is not a prime-AP discrepancy. APErrorRepresentation "
            "belongs to the AP-source/direct-BFI branch and is removed from the non-AP terminal. "
            "SOURCE-CEN and BD-CEN block any free centering/projection shortcut. Therefore the "
            "non-AP object side is exactly the uncentered WFD-to-KE13 no-projection identity: "
            "derive the raw dispersion/Cauchy object without centering, then prove KE-13 dyadic "
            "exhaustion without projection or endpoint loss."
        ),
        "review_conclusion": (
            "非 AP-source 对象侧已压成 `UncenteredWFDToKE13NoProjectionIdentity`："
            "`APErrorRepresentation` 已归入 AP-source 直接 BFI 分支；非 AP fallback 只剩 "
            "`DispersionCauchyNoCenteringIdentity` 与 `KE13DyadicExhaustionNoProjection`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI 非 AP-source object ledger 路由器",
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
        "removed from non-AP object terminal:",
        f"  {result['removed_nonap_transfer_gates']};",
        "",
        "new object terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "expansion:",
        f"  {result['terminal_gap_expansion']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `ap_error_representation_not_nonap_terminal={fmt_bool(result['ap_error_representation_not_nonap_terminal'])}`。",
        f"- `nonap_object_ledger_closed={fmt_bool(result['nonap_object_ledger_closed'])}`。",
        f"- `closed_object_gates={result['closed_object_gates']}`。",
        f"- `open_object_gates={result['open_object_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 对象账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["object_rows"]:
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
            "对象侧的最窄剩余为：",
            "",
            "```text",
            "UncenteredWFDToKE13NoProjectionIdentity:",
            "  DispersionCauchyNoCenteringIdentity;",
            "  KE13DyadicExhaustionNoProjection.",
            "```",
            "",
            "这一步只改变终端账本，不声称对象恒等式已经证明；它排除了把 AP-source 身份或块中心化",
            "偷带入非 AP fallback 的路径。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nonap-dispersion-json", type=Path, default=DEFAULT_NONAP_DISPERSION)
    parser.add_argument("--ap-source-branch-json", type=Path, default=DEFAULT_AP_SOURCE_BRANCH)
    parser.add_argument("--transfer-scale-json", type=Path, default=DEFAULT_TRANSFER_SCALE)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--source-cen-no-go-md", type=Path, default=DEFAULT_SOURCE_CEN_NO_GO)
    parser.add_argument("--bd-cen-audit-md", type=Path, default=DEFAULT_BD_CEN_AUDIT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        nonap_dispersion_path=args.nonap_dispersion_json,
        ap_source_branch_path=args.ap_source_branch_json,
        transfer_scale_path=args.transfer_scale_json,
        common_variable_table_path=args.common_variable_table_json,
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
                "open_object_gates": result["open_object_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
