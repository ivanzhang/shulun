#!/usr/bin/env python3
"""审计原始 clean A1 残差是否已等于 BFI prime-AP 误差。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_ap_residual_identity_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-ap-residual-identity-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-ap-residual-identity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_BFI_LEVEL_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-bfi-level-ledger-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_TRANSFER_SCALE = (
    DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
)
DEFAULT_GENERIC_WFD_DIBFI = DOCS / "prime-matrix-triad-a1-generic-wfd-dibfi-router.json"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_SOURCE_CEN = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-ap-residual-identity-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-ap-residual-identity-router.md"


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


def ap_formula(common_variable_table: dict[str, Any]) -> str:
    """提取 APError 公式。"""
    for row in common_variable_table["transfer_rows"]:
        if row["step"] == "APError":
            return str(row["formula"])
    return ""


def build_identity_rows(
    common_variable_table: dict[str, Any],
    transfer_scale: dict[str, Any],
    generic_wfd_dibfi: dict[str, Any],
    kze_spine_path: Path,
    source_cen_path: Path,
) -> list[dict[str, Any]]:
    """构造 AP 源对象等式门控。"""
    formula = ap_formula(common_variable_table)
    kze_is_downstream = contains_all(kze_spine_path, ["WFD-core", "KE-13", "Cauchy"])
    source_cen_refuted = contains_all(
        source_cen_path,
        ["SOURCE-CEN is false", "当前 WFD-core", "未块中心化"],
    )
    ap_gate_open = "APErrorRepresentation" in transfer_scale["open_transfer_gates"]
    uncentered_target_locked = bool(generic_wfd_dibfi["external_dibfi_contract_materialized"])
    return [
        {
            "gate": "APErrorFormulaAvailable",
            "closed": bool(formula),
            "status": "closed_formula_only" if formula else "missing_formula",
            "evidence": formula or "none",
            "remaining": "公式已命名，但不等于源对象等式。",
            "next_target": "none",
        },
        {
            "gate": "DownstreamWFDObjectIdentified",
            "closed": kze_is_downstream and uncentered_target_locked,
            "status": "closed_as_diagnostic_not_identity",
            "evidence": "KZ-E spine 与 generic WFD 合同锁定当前下游对象为未中心化 WFD/KE-13 核。",
            "remaining": "这只能说明下游对象是什么，不能从下游反推出 AP 源等式。",
            "next_target": "UpstreamCleanA1APSourceDefinition",
        },
        {
            "gate": "NoDownstreamBackProjectionShortcut",
            "closed": source_cen_refuted,
            "status": "closed_negative_shortcut_blocked",
            "evidence": "SOURCE-CEN no-go 排除免费中心化/投影替换；下游 KE-13 不能自动替代原始 AP 残差。",
            "remaining": "必须从 Cauchy/dispersion 之前的原始残差定义写等式。",
            "next_target": "UpstreamCleanA1APSourceDefinition",
        },
        {
            "gate": "TransferScaleAlreadyMarksAPRepresentationOpen",
            "closed": ap_gate_open,
            "status": "open_confirmed_by_previous_certificate",
            "evidence": f"open_transfer_gates={transfer_scale['open_transfer_gates']}",
            "remaining": "上游证书明确把 APErrorRepresentation 作为未闭合项。",
            "next_target": "UpstreamCleanA1APSourceDefinition",
        },
        {
            "gate": "UpstreamCleanA1ResidualDefinition",
            "closed": False,
            "status": "open_source_definition_missing",
            "evidence": "尚未找到 clean A1 原始残差在进入 Cauchy/dispersion 前等于 AP discrepancy 的逐项定义。",
            "remaining": "需给出 R_clean = dyadic sum of E_AP(X,Q) + acceptable endpoints 的源头等式。",
            "next_target": "UpstreamCleanA1APSourceDefinition",
        },
        {
            "gate": "MainTermAndCoefficientMatch",
            "closed": False,
            "status": "open_delta_q_main_term_match_missing",
            "evidence": "AP 公式中的 Delta_q(nm) 已命名，但主项扣除、残基类 a(q) 与 lambda_q 符号尚未逐项接到 clean A1 残差。",
            "remaining": "需核对主项、端点、dyadic 权、lambda_q 与 alpha/beta 系数完全同源。",
            "next_target": "UpstreamCleanA1APSourceDefinition",
        },
    ]


def run(
    bfi_level_ledger_path: Path,
    common_variable_table_path: Path,
    transfer_scale_path: Path,
    generic_wfd_dibfi_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
) -> dict[str, Any]:
    """运行 AP 残差对象等式路由。"""
    bfi_level_ledger = load_json(bfi_level_ledger_path)
    common_variable_table = load_json(common_variable_table_path)
    transfer_scale = load_json(transfer_scale_path)
    generic_wfd_dibfi = load_json(generic_wfd_dibfi_path)
    identity_rows = build_identity_rows(
        common_variable_table,
        transfer_scale,
        generic_wfd_dibfi,
        kze_spine_path,
        source_cen_path,
    )
    open_gates = [row["gate"] for row in identity_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_ap_residual_identity_router",
        "status": "ap_residual_identity_reduced_to_upstream_source_definition_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "bfi_level_ledger_json": file_sha256(bfi_level_ledger_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "transfer_scale_json": file_sha256(transfer_scale_path),
            "generic_wfd_dibfi_json": file_sha256(generic_wfd_dibfi_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "source_cen_no_go_md": file_sha256(source_cen_path),
        },
        "previous_terminal_gap": bfi_level_ledger["terminal_gap_after_router"],
        "previous_remaining_targets": bfi_level_ledger["remaining_terminal_targets"],
        "identity_rows": identity_rows,
        "open_gates": open_gates,
        "ap_residual_identity_closed": False,
        "terminal_gap_after_router": "UpstreamCleanA1APSourceDefinition",
        "ke13_fallback_condition": (
            "If UpstreamCleanA1APSourceDefinition cannot be proved, direct BFI AP atom "
            "cannot close this branch; the legal route returns to KE-13 no-projection fallback "
            "or a separately stated external original-dispersion theorem."
        ),
        "structural_law": (
            "OriginalResidualEqualsBFIAPError is a source-level identity, not a downstream "
            "Kloosterman-window estimate. The AP formula, WFD-core, phase normalization and "
            "level ledger are all available, but they do not prove that the clean A1 residual "
            "before Cauchy/dispersion is exactly the BFI prime-AP discrepancy. That equality "
            "must be written at the upstream definition layer, including Delta_q main term, "
            "lambda_q, dyadic weights, endpoint losses and coefficient provenance."
        ),
        "review_conclusion": (
            "唯一剩余 AP 对象等式被压成源头定义合同：必须证明原始 clean A1 残差在进入 "
            "Cauchy/dispersion 前就是 BFI prime-AP discrepancy 的 dyadic 总和。"
            "不能从 KE-13/WFD 下游窗口倒推该等式；若源头等式失败，直接 BFI 路线必须退回 fallback。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI AP 残差源等式路由器",
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
        "open gates:",
        f"  {result['open_gates']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `ap_residual_identity_closed={fmt_bool(result['ap_residual_identity_closed'])}`。",
        f"- `open_gates={result['open_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 对象等式门控表",
        "",
        "| gate | status | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["identity_rows"]:
        lines.append(
            "| `{gate}` | `{status}` | `{closed}` | {evidence} | {remaining} | `{next}` |".format(
                gate=table_cell(row["gate"]),
                status=table_cell(row["status"]),
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
            "现在的终端硬点已经不能再写成泛泛的 BFI 适配问题，而是一个源头定义等式：",
            "",
            "```text",
            "UpstreamCleanA1APSourceDefinition:",
            "  R_clean",
            "  = sum_dyadic E_AP(X,Q; lambda_q, alpha, beta, Delta_q)",
            "    + endpoint/log-budget errors.",
            "```",
            "",
            "这条等式必须出现在 Cauchy、dispersion、KE-13 和任何中心化/投影操作之前。",
            "否则直接 BFI prime-AP 原子不可用，只能走 KE-13 无投影 fallback 或另写外部原始 dispersion 定理。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bfi-level-ledger-json", type=Path, default=DEFAULT_BFI_LEVEL_LEDGER)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--transfer-scale-json", type=Path, default=DEFAULT_TRANSFER_SCALE)
    parser.add_argument(
        "--generic-wfd-dibfi-json", type=Path, default=DEFAULT_GENERIC_WFD_DIBFI
    )
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--source-cen-md", type=Path, default=DEFAULT_SOURCE_CEN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        bfi_level_ledger_path=args.bfi_level_ledger_json,
        common_variable_table_path=args.common_variable_table_json,
        transfer_scale_path=args.transfer_scale_json,
        generic_wfd_dibfi_path=args.generic_wfd_dibfi_json,
        kze_spine_path=args.kze_spine_md,
        source_cen_path=args.source_cen_md,
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
                "ap_residual_identity_closed": result["ap_residual_identity_closed"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
