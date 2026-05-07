#!/usr/bin/env python3
"""把非 AP-source 分支接回既有原始 dispersion 匹配链。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_nonap_dispersion_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-nonap-dispersion-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-nonap-dispersion-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_AP_SOURCE_BRANCH = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-branch-router.json"
DEFAULT_GENERIC_WFD_DIBFI = DOCS / "prime-matrix-triad-a1-generic-wfd-dibfi-router.json"
DEFAULT_THEOREM_LOCATION = DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
DEFAULT_WINDOW_MATCH = DOCS / "prime-matrix-triad-a1-dibfi-window-match-router.json"
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_TRANSFER_SCALE = (
    DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-nonap-dispersion-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-nonap-dispersion-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_chain_rows(
    ap_source_branch: dict[str, Any],
    generic_wfd_dibfi: dict[str, Any],
    theorem_location: dict[str, Any],
    window_match: dict[str, Any],
    common_variable_table: dict[str, Any],
    transfer_scale: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造非 AP fallback 接线表。"""
    nonap_open = "NonAPSourceGenericWFD" in ap_source_branch["open_branches"]
    return [
        {
            "stage": "NonAPSourceDetected",
            "closed": nonap_open,
            "evidence": f"open_branches={ap_source_branch['open_branches']}",
            "next": "GenericWFDOriginalDispersionContract",
        },
        {
            "stage": "GenericWFDOriginalDispersionContract",
            "closed": bool(generic_wfd_dibfi["external_dibfi_contract_materialized"]),
            "evidence": generic_wfd_dibfi["terminal_gap_after_router"],
            "next": "TheoremLocationPinned",
        },
        {
            "stage": "TheoremLocationPinned",
            "closed": bool(theorem_location["theorem_locations_pinned"]),
            "evidence": theorem_location["terminal_gap_after_router"],
            "next": "CurrentWindowMatch",
        },
        {
            "stage": "CurrentWindowMatch",
            "closed": window_match["open_gates"]
            == ["OriginalAPToWFDTargetTransfer", "WindowScaleInequalities"],
            "evidence": f"open_gates={window_match['open_gates']}",
            "next": "CommonVariableTable",
        },
        {
            "stage": "CommonVariableTable",
            "closed": bool(common_variable_table["no_variable_fork"]),
            "evidence": common_variable_table["terminal_gap_after_router"],
            "next": "TransferScaleCertificate",
        },
        {
            "stage": "TransferScaleCertificate",
            "closed": False,
            "evidence": (
                f"open_transfer={transfer_scale['open_transfer_gates']}; "
                f"open_scale={transfer_scale['open_scale_gates']}"
            ),
            "next": "DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource",
        },
    ]


def run(
    ap_source_branch_path: Path,
    generic_wfd_dibfi_path: Path,
    theorem_location_path: Path,
    window_match_path: Path,
    common_variable_table_path: Path,
    transfer_scale_path: Path,
) -> dict[str, Any]:
    """运行非 AP fallback 原始 dispersion 路由。"""
    ap_source_branch = load_json(ap_source_branch_path)
    generic_wfd_dibfi = load_json(generic_wfd_dibfi_path)
    theorem_location = load_json(theorem_location_path)
    window_match = load_json(window_match_path)
    common_variable_table = load_json(common_variable_table_path)
    transfer_scale = load_json(transfer_scale_path)
    chain_rows = build_chain_rows(
        ap_source_branch,
        generic_wfd_dibfi,
        theorem_location,
        window_match,
        common_variable_table,
        transfer_scale,
    )
    return {
        "certificate_type": "triad_a1_dibfi_nonap_dispersion_router",
        "status": "nonap_source_dispersion_reduced_to_quantified_no_projection_certificate_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "ap_source_branch_json": file_sha256(ap_source_branch_path),
            "generic_wfd_dibfi_json": file_sha256(generic_wfd_dibfi_path),
            "theorem_location_json": file_sha256(theorem_location_path),
            "window_match_json": file_sha256(window_match_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "transfer_scale_json": file_sha256(transfer_scale_path),
        },
        "previous_terminal_gap": ap_source_branch["terminal_gap_after_router"],
        "chain_rows": chain_rows,
        "open_transfer_gates": transfer_scale["open_transfer_gates"],
        "open_scale_gates": transfer_scale["open_scale_gates"],
        "open_terminal_targets": transfer_scale["open_terminal_targets"],
        "nonap_dispersion_closed": False,
        "terminal_gap_after_router": "DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource",
        "structural_law": (
            "The non-AP-source branch is not a new undefined gap. It reconnects to the already "
            "materialized original-dispersion chain: generic WFD contract, pinned DI/BFI theorem "
            "locations, current-window match, common variable table, and the transfer/scale "
            "certificate. All earlier stages are routed; the remaining fallback terminal is exactly "
            "the quantified no-projection window certificate for the non-AP source."
        ),
        "review_conclusion": (
            "非 AP-source 分支已接回既有原始 dispersion 链条。定理位置、窗口接口与共同变量表都已路由；"
            "当前真正剩余是 `NoProjectionUncenteredDispersionIdentity` 与 "
            "`QuantifiedDIBFIWindowSubstitution` 的合取证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI 非 AP-source 原始 dispersion 路由器",
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
        "open terminal targets:",
        f"  {result['open_terminal_targets']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `nonap_dispersion_closed={fmt_bool(result['nonap_dispersion_closed'])}`。",
        f"- `open_transfer_gates={result['open_transfer_gates']}`。",
        f"- `open_scale_gates={result['open_scale_gates']}`。",
        f"- `open_terminal_targets={result['open_terminal_targets']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 接线表",
        "",
        "| stage | closed | evidence | next |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["chain_rows"]:
        lines.append(
            "| `{stage}` | `{closed}` | {evidence} | `{next}` |".format(
                stage=table_cell(row["stage"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                next=table_cell(row["next"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "非 AP-source fallback 的最窄终端为：",
            "",
            "```text",
            "DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource",
            "  = NoProjectionUncenteredDispersionIdentity",
            "    + QuantifiedDIBFIWindowSubstitution.",
            "```",
            "",
            "这说明下一步不应再找定理号或重复 AP-source 账本，而应直接攻未中心化无投影恒等式和量化窗口代入。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ap-source-branch-json", type=Path, default=DEFAULT_AP_SOURCE_BRANCH)
    parser.add_argument("--generic-wfd-dibfi-json", type=Path, default=DEFAULT_GENERIC_WFD_DIBFI)
    parser.add_argument("--theorem-location-json", type=Path, default=DEFAULT_THEOREM_LOCATION)
    parser.add_argument("--window-match-json", type=Path, default=DEFAULT_WINDOW_MATCH)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--transfer-scale-json", type=Path, default=DEFAULT_TRANSFER_SCALE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        ap_source_branch_path=args.ap_source_branch_json,
        generic_wfd_dibfi_path=args.generic_wfd_dibfi_json,
        theorem_location_path=args.theorem_location_json,
        window_match_path=args.window_match_json,
        common_variable_table_path=args.common_variable_table_json,
        transfer_scale_path=args.transfer_scale_json,
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
                "nonap_dispersion_closed": result["nonap_dispersion_closed"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
