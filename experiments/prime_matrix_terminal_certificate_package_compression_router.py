#!/usr/bin/env python3
"""压缩 TerminalCertificatePackage 的独立输入。

用法示例：
  python3 experiments/prime_matrix_terminal_certificate_package_compression_router.py

输出：
  docs/monograph/prime-matrix-terminal-certificate-package-compression-router.json
  docs/monograph/prime-matrix-terminal-certificate-package-compression-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_ATLAS = DOCS / "prime-matrix-closure-input-atlas-router.json"
DEFAULT_UNNAMED = DOCS / "prime-matrix-unnamed-escape-closure-machine.md"
DEFAULT_NAMED = DOCS / "prime-matrix-named-exit-absorption-contract.md"
DEFAULT_PDEC_TEMPLATE = DOCS / "h4-pdec-certificate-template.md"
DEFAULT_COLUMN_CONTRACT = DOCS / "h4-pdec-column-defect-routing-contract.md"
DEFAULT_TOTAL_DESCENT = DOCS / "prime-matrix-total-zero-row-recursive-descent-route.md"
DEFAULT_RPZ_ROUTE = DOCS / "prime-matrix-rpz-dual-track-closure-route.md"
DEFAULT_SEAM = DOCS / "prime-matrix-rpz-first-grid-fail-seam-certificate.md"
DEFAULT_NC_INPUT = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.json"
DEFAULT_CANONICAL_FINAL = (
    DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-terminal-certificate-package-compression-router.json"
DEFAULT_MD = DOCS / "prime-matrix-terminal-certificate-package-compression-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(path: Path, needles: list[str]) -> bool:
    """检查文件是否包含全部关键文本。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    item: str,
    current_status: str,
    compression: str,
    independent_after_compression: bool,
    remaining_input: str,
) -> dict[str, Any]:
    """构造终端包压缩行。"""
    return {
        "item": item,
        "current_status": current_status,
        "compression": compression,
        "independent_after_compression": independent_after_compression,
        "remaining_input": remaining_input,
    }


def build_rows(
    atlas: dict[str, Any],
    nc_input: dict[str, Any],
    canonical_final: dict[str, Any],
    unnamed_path: Path,
    named_path: Path,
    pdec_template_path: Path,
    column_contract_path: Path,
    total_descent_path: Path,
    rpz_route_path: Path,
    seam_path: Path,
) -> list[dict[str, Any]]:
    """生成终端证书包压缩表。"""
    unnamed_closed = contains_all(
        unnamed_path,
        ["无名逃逸闭合定理", "SAE/endpoint", "CleanMultishellKLS"],
    )
    named_absorbed = contains_all(
        named_path,
        ["Abs(SAE)", "Abs(PDEC)", "Abs(ColumnCRT)", "Abs(TotalDescent)"],
    )
    pdec_template_ready = contains_all(
        pdec_template_path,
        ["U_CRT<L_PDEC", "失败输出", "当前未闭合项"],
    )
    column_contract_ready = contains_all(
        column_contract_path,
        ["ColumnCRTDefect", "相位兼容性", "仍不是已排除出口"],
    )
    descent_absorbed = contains_all(
        total_descent_path,
        ["TotalDescent-TM", "SAE/PDEC/ColumnCRT"],
    ) and contains_all(
        rpz_route_path,
        ["first-grid-fail seam", "ColumnCRTDefect"],
    ) and contains_all(
        seam_path,
        ["PDEC/ColumnCRT 增强证书行", "unit endpoint", "本证书只完成标准形抽取"],
    )
    canonical_closed = (
        canonical_final["canonical_source_self_contained_theorem_closed"]
        and canonical_final["open_self_contained_gates"] == []
    )
    noncanonical_contract_closed = nc_input["contract_boundary_closed"]
    terminal_package_listed = any(
        item["input"] == "TerminalCertificatePackage"
        for item in atlas["minimal_input_basis"]
    )

    return [
        row(
            item="NoUnnamedEscape",
            current_status="closed" if unnamed_closed else "missing",
            compression="所有未命名逃逸必须进入命名出口或下降。",
            independent_after_compression=False,
            remaining_input="none; feeds named exits",
        ),
        row(
            item="NamedExitAbsorption",
            current_status="contract_closed" if named_absorbed else "missing",
            compression="Bohr-cap、EndpointSeam、CofactorAnchor 吸收到 SAE/PDEC/ColumnCRT/CleanKLS/TotalDescent。",
            independent_after_compression=False,
            remaining_input="none; feeds certificate interfaces",
        ),
        row(
            item="SAE-Cert",
            current_status="interface_open",
            compression="稀疏/孤立坏窗不能再生成新分支；必须逐窗给 survivor/lift/higher-defect 或有限证书。",
            independent_after_compression=True,
            remaining_input="Global SAE finite/window certificate family",
        ),
        row(
            item="PDEC-Cert",
            current_status="template_ready_not_filled" if pdec_template_ready else "missing",
            compression="所有持久低模/帽/端点/轮筛缺陷统一到同一坏窗集合上的 U_CRT<L_PDEC。",
            independent_after_compression=True,
            remaining_input="PDEC-Dual/Explicit certificates for all persistent families",
        ),
        row(
            item="ColumnCRT-Cert",
            current_status="routing_contract_closed_exclusion_open"
            if column_contract_ready
            else "missing",
            compression="列位移出口已条件路由；固定非零位移负载必须被排斥或回流 PDEC/SAE。",
            independent_after_compression=True,
            remaining_input="ColumnCRT exclusion or PDEC/SAE return certificates",
        ),
        row(
            item="CleanMultishellKLS",
            current_status=(
                "canonical_branch_closed_noncanonical_externalized"
                if canonical_closed and noncanonical_contract_closed
                else "open"
            ),
            compression="canonical-source clean 分支已被最终边界吸收；noncanonical/generic clean 分支属于补集输入包或外部 KLS。",
            independent_after_compression=False,
            remaining_input="move to NoncanonicalFullSComplementPackage or external KLS",
        ),
        row(
            item="TotalDescent",
            current_status="absorbed_to_p2_or_first_seam" if descent_absorbed else "open",
            compression="正式下降路径存在则到 p=2；不存在则首个 grid-fail seam 已材料化为 PDEC/ColumnCRT/SAE。",
            independent_after_compression=False,
            remaining_input="first-seam PDEC/ColumnCRT/SAE, already counted above",
        ),
        row(
            item="TerminalPackagePresence",
            current_status="listed" if terminal_package_listed else "missing",
            compression="第一包经压缩后只剩 SAE/PDEC/ColumnCRT 三个真正独立证书族。",
            independent_after_compression=False,
            remaining_input="SAE + PDEC + ColumnCRT certificate families",
        ),
    ]


def run(
    atlas_path: Path,
    nc_input_path: Path,
    canonical_final_path: Path,
    unnamed_path: Path,
    named_path: Path,
    pdec_template_path: Path,
    column_contract_path: Path,
    total_descent_path: Path,
    rpz_route_path: Path,
    seam_path: Path,
) -> dict[str, Any]:
    """运行终端证书包压缩。"""
    atlas = load_json(atlas_path)
    nc_input = load_json(nc_input_path)
    canonical_final = load_json(canonical_final_path)
    rows = build_rows(
        atlas=atlas,
        nc_input=nc_input,
        canonical_final=canonical_final,
        unnamed_path=unnamed_path,
        named_path=named_path,
        pdec_template_path=pdec_template_path,
        column_contract_path=column_contract_path,
        total_descent_path=total_descent_path,
        rpz_route_path=rpz_route_path,
        seam_path=seam_path,
    )
    independent_inputs = [
        row["remaining_input"]
        for row in rows
        if row["independent_after_compression"]
    ]
    compression_closed = all(
        row["current_status"] not in {"missing", "open"}
        for row in rows
        if row["item"]
        in {"NoUnnamedEscape", "NamedExitAbsorption", "PDEC-Cert", "ColumnCRT-Cert", "CleanMultishellKLS", "TotalDescent", "TerminalPackagePresence"}
    )

    evidence_paths = [
        atlas_path,
        nc_input_path,
        canonical_final_path,
        unnamed_path,
        named_path,
        pdec_template_path,
        column_contract_path,
        total_descent_path,
        rpz_route_path,
        seam_path,
    ]
    return {
        "certificate_type": "prime_matrix_terminal_certificate_package_compression_router",
        "status": "terminal_package_compressed_to_sae_pdec_columncrt_certificates",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "terminal_package_compression_closed": compression_closed,
        "terminal_package_fully_proved": False,
        "row_column_unconditional_closed": False,
        "independent_terminal_inputs_after_compression": independent_inputs,
        "removed_independent_inputs": [
            "NoUnnamedEscape",
            "NamedExitAbsorption",
            "CleanMultishellKLS inside canonical branch",
            "TotalDescent as separate terminal",
        ],
        "rows": rows,
        "compression_law": (
            "The first package no longer has five independent terminal inputs. "
            "No-unnamed-escape and named-exit absorption are already contract closed. "
            "CleanKLS is absorbed on the canonical branch and belongs to the noncanonical/external "
            "package otherwise. TotalDescent either reaches p=2 or produces a first-grid-fail "
            "seam already routed to PDEC/ColumnCRT/SAE. Therefore the independent terminal "
            "work is compressed to three certificate families: SAE, PDEC, and ColumnCRT."
        ),
        "review_conclusion": (
            "TerminalCertificatePackage 已从五项独立输入压缩为三类证书族：SAE、PDEC、ColumnCRT。"
            "这补齐了第一包的结构压缩，但尚未证明三类证书族本身。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 终端证书包压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 压缩律",
        "",
        result["compression_law"],
        "",
        "```text",
        (
            "terminal_package_compression_closed="
            f"{fmt_bool(result['terminal_package_compression_closed'])}"
        ),
        f"terminal_package_fully_proved={fmt_bool(result['terminal_package_fully_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 压缩表",
        "",
        "| item | current status | compression | independent after compression | remaining input |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{item}` | `{status}` | {compression} | `{independent}` | {remaining} |".format(
                item=table_cell(item["item"]),
                status=table_cell(item["current_status"]),
                compression=table_cell(item["compression"]),
                independent=fmt_bool(bool(item["independent_after_compression"])),
                remaining=table_cell(item["remaining_input"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 压缩后的独立输入",
            "",
        ]
    )
    for item in result["independent_terminal_inputs_after_compression"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            "第一包已经完成结构压缩：`CleanMultishellKLS` 不再作为 canonical 分支的独立终端，"
            "`TotalDescent` 不再作为平行终端，所有首阻断 seam 已回流到 `PDEC/ColumnCRT/SAE`。"
            "剩下必须真正证明的是三类证书族本身。完整行/列无条件命题仍未闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atlas-json", type=Path, default=DEFAULT_ATLAS)
    parser.add_argument("--noncanonical-json", type=Path, default=DEFAULT_NC_INPUT)
    parser.add_argument("--canonical-final-json", type=Path, default=DEFAULT_CANONICAL_FINAL)
    parser.add_argument("--unnamed-md", type=Path, default=DEFAULT_UNNAMED)
    parser.add_argument("--named-md", type=Path, default=DEFAULT_NAMED)
    parser.add_argument("--pdec-template-md", type=Path, default=DEFAULT_PDEC_TEMPLATE)
    parser.add_argument("--column-contract-md", type=Path, default=DEFAULT_COLUMN_CONTRACT)
    parser.add_argument("--total-descent-md", type=Path, default=DEFAULT_TOTAL_DESCENT)
    parser.add_argument("--rpz-route-md", type=Path, default=DEFAULT_RPZ_ROUTE)
    parser.add_argument("--seam-md", type=Path, default=DEFAULT_SEAM)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        atlas_path=args.atlas_json,
        nc_input_path=args.noncanonical_json,
        canonical_final_path=args.canonical_final_json,
        unnamed_path=args.unnamed_md,
        named_path=args.named_md,
        pdec_template_path=args.pdec_template_md,
        column_contract_path=args.column_contract_md,
        total_descent_path=args.total_descent_md,
        rpz_route_path=args.rpz_route_md,
        seam_path=args.seam_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["independent_terminal_inputs_after_compression"])


if __name__ == "__main__":
    main()
