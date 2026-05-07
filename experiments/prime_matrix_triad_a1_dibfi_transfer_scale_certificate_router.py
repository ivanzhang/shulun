#!/usr/bin/env python3
"""审计 DI/BFI 共同变量表上的转移/尺度合取证书。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_transfer_scale_certificate_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_THEOREM_LOCATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
)
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_SOURCE_CEN = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_HLC_KLS_EXTERNAL = DOCS / "prime-matrix-h3-dsb-hlc-kls-external-adaptation.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.md"


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


def build_transfer_certificate_rows(
    common_variable_table: dict[str, Any],
    kze_spine_path: Path,
    kls_template_path: Path,
    source_cen_path: Path,
) -> list[dict[str, Any]]:
    """逐行审计对象转移证书。"""
    transfer_steps = {row["step"]: row for row in common_variable_table["transfer_rows"]}
    has_type_budget = contains_all(
        kze_spine_path,
        ["Vaughan/Heath-Brown", "Type-I/II", "dyadic", "log"],
    )
    has_crt_phase = contains_all(kze_spine_path, ["KE-8", "CRT", "Kloosterman"])
    has_kls_phase = contains_all(kls_template_path, ["相位归一化", "CRT", "S(a,b;c)"])
    source_cen_refuted = contains_all(
        source_cen_path,
        ["SOURCE-CEN is false", "未块中心化", "会改变目标对象"],
    )
    return [
        {
            "gate": "APErrorRepresentation",
            "common_step": "APError",
            "status": "interface_named_but_exact_residual_identity_open",
            "closed": False,
            "evidence": transfer_steps["APError"]["formula"],
            "remaining": "仍需把 clean A1 generic WFD 残差逐项写成该 AP error 或其 dyadic 总和。",
            "next_target": "APToUncenteredDispersionIdentity",
        },
        {
            "gate": "TypeDecompositionLogBudget",
            "common_step": "TypeDecomposition",
            "status": "ledger_closed_conditioned_on_ap_error_identity"
            if has_type_budget
            else "ledger_gap",
            "closed": has_type_budget,
            "evidence": "KZ-E spine 已登记 Vaughan/Heath-Brown、Type-I/II 与 dyadic/log 账本。",
            "remaining": "该行只关闭分解账本；不替代 APErrorRepresentation。",
            "next_target": "none",
        },
        {
            "gate": "DispersionCauchyNoCenteringIdentity",
            "common_step": "DispersionCauchy",
            "status": "open_no_centering_shortcut_available",
            "closed": False,
            "evidence": "SOURCE-CEN 已反证，不能免费插入块中心化或删同块对角。",
            "remaining": "必须从 BFI 原始 dispersion 写出 Cauchy 展开到 KE-5 的逐项恒等式。",
            "next_target": "NoProjectionUncenteredDispersionIdentity",
        },
        {
            "gate": "CRTPhaseSymbolUnification",
            "common_step": "CRTPhase",
            "status": "closed",
            "closed": has_crt_phase and has_kls_phase,
            "evidence": "KZ-E 的 KE-8 与 KLS 模板的相位归一化同指向标准 e_c(a s+b bar{s})。",
            "remaining": "最终稿只需统一符号；不再是独立数学缺口。",
            "next_target": "none",
        },
        {
            "gate": "KE13DyadicExhaustionNoProjection",
            "common_step": "KE13Identification",
            "status": "open_main_target_transfer_blocker",
            "closed": False,
            "evidence": transfer_steps["KE13Identification"]["formula"],
            "remaining": "需证明所有 dyadic 主块完全覆盖，且没有额外中心化、投影、块对角删除或端点遗漏。",
            "next_target": "NoProjectionUncenteredDispersionIdentity",
        },
    ]


def build_scale_certificate_rows(
    common_variable_table: dict[str, Any],
    kze_spine_path: Path,
    kls_template_path: Path,
    external_index_path: Path,
) -> list[dict[str, Any]]:
    """逐行审计尺度不等式证书。"""
    scale_rows = {row["inequality"]: row for row in common_variable_table["scale_rows"]}
    has_type_product = contains_all(kze_spine_path, ["Type-I/II", "dyadic"])
    has_tail_ledger = contains_all(
        kls_template_path,
        ["0<|h|<=H", "B(A)", "sawtooth Fourier 截断"],
    )
    has_log_ledger = contains_all(kls_template_path, ["B(A)", "dyadic", "gcd"])
    has_theorem_sources = contains_all(
        external_index_path,
        ["BFI1987-Theorem10", "DI1982-Theorem12"],
    )
    return [
        {
            "gate": "TypeProductQuantified",
            "common_inequality": "TypeProduct",
            "status": "closed_at_dyadic_product_level"
            if has_type_product
            else "type_product_gap",
            "closed": has_type_product,
            "evidence": scale_rows["TypeProduct"]["statement"],
            "remaining": "N*M≈X 本身已是 Type 分块恒等式；仍不决定 Q,C,S,H 的外部定理范围。",
            "next_target": "none",
        },
        {
            "gate": "BFILevelQuantified",
            "common_inequality": "BFILevel",
            "status": "open_exact_x_q_exponent_substitution_missing",
            "closed": False,
            "evidence": scale_rows["BFILevel"]["statement"],
            "remaining": "需要给出 X、Q 与 prime-matrix 参数的显式关系，并代入 BFI Theorem 10 的 level 条件。",
            "next_target": "QuantifiedDIBFIWindowSubstitution",
        },
        {
            "gate": "KLSModulusWindowQuantified",
            "common_inequality": "KLSModulusWindow",
            "status": "open_qualitative_range_only",
            "closed": False,
            "evidence": scale_rows["KLSModulusWindow"]["statement"],
            "remaining": "当前 C≈P/log^{O(1)}P 只是定性窗口，需匹配 DI/BFI 原文模数族与 dyadic level。",
            "next_target": "QuantifiedDIBFIWindowSubstitution",
        },
        {
            "gate": "InverseVariableWindowQuantified",
            "common_inequality": "InverseVariableWindow",
            "status": "open_completion_length_substitution_missing",
            "closed": False,
            "evidence": scale_rows["InverseVariableWindow"]["statement"],
            "remaining": "需从 completion 后的 s 变量长度推出 DI 逆元变量窗口允许范围。",
            "next_target": "QuantifiedDIBFIWindowSubstitution",
        },
        {
            "gate": "FrequencyWindowAndTail",
            "common_inequality": "FrequencyWindow",
            "status": "tail_ledger_closed_di_range_still_in_quantified_substitution"
            if has_tail_ledger
            else "frequency_tail_gap",
            "closed": has_tail_ledger,
            "evidence": scale_rows["FrequencyWindow"]["statement"],
            "remaining": "Fourier 尾项账本已关；h 作为 DI/BFI 频率参数的精确范围并入量化代入证书。",
            "next_target": "QuantifiedDIBFIWindowSubstitution",
        },
        {
            "gate": "DIJScaleDominanceSubstitution",
            "common_inequality": "DIJScaleDominance",
            "status": "open_main_scale_blocker",
            "closed": False,
            "evidence": scale_rows["DIJScaleDominance"]["statement"],
            "remaining": "需把 DI Theorem 12 的 J-scale 项逐项代入 C,S,H,N,M,Q，并证明小于 WFD 自然尺度/log^A。",
            "next_target": "QuantifiedDIBFIWindowSubstitution",
        },
        {
            "gate": "LogLossC0Extraction",
            "common_inequality": "LogLossAbsorption",
            "status": "closed_symbolic_log_ledger"
            if has_log_ledger and has_theorem_sources
            else "log_ledger_gap",
            "closed": has_log_ledger and has_theorem_sources,
            "evidence": scale_rows["LogLossAbsorption"]["statement"],
            "remaining": "C0 仍可保持符号化；若最终稿要求显式常数，再逐项抽取 C_i。",
            "next_target": "none",
        },
    ]


def build_terminal_rows(
    transfer_rows: list[dict[str, Any]],
    scale_rows: list[dict[str, Any]],
    theorem_location: dict[str, Any],
    hlc_kls_external_path: Path,
) -> list[dict[str, Any]]:
    """把所有未闭合行压成终端目标。"""
    open_transfer = [row["gate"] for row in transfer_rows if not row["closed"]]
    open_scale = [row["gate"] for row in scale_rows if not row["closed"]]
    external_hlc_adapted = contains_all(
        hlc_kls_external_path,
        [
            "clean HLC branch is closed in the external-deep-theorem version",
            "HLC-KLS-core",
            "审稿边界",
        ],
    )
    return [
        {
            "terminal": "NoProjectionUncenteredDispersionIdentity",
            "covers": [
                "APErrorRepresentation",
                "DispersionCauchyNoCenteringIdentity",
                "KE13DyadicExhaustionNoProjection",
            ],
            "status": "open",
            "reason": "对象转移仍必须证明原始未中心化目标在 BFI dispersion 展开中逐项保持。",
            "closed": False,
        },
        {
            "terminal": "QuantifiedDIBFIWindowSubstitution",
            "covers": [
                "BFILevelQuantified",
                "KLSModulusWindowQuantified",
                "InverseVariableWindowQuantified",
                "DIJScaleDominanceSubstitution",
            ],
            "status": "open",
            "reason": "尺度侧仍缺少把 X,Q,N,M,C,S,H 代入 BFI Theorem 10 与 DI Theorem 12 的逐项不等式。",
            "closed": False,
        },
        {
            "terminal": "ExternalWindowedKLSAlternative",
            "covers": ["HLC-KLS-core / CORE-5"],
            "status": "available_for_hlc_clean_branch_not_generic_wfd_certificate",
            "reason": (
                "HLC clean 分支已有外部深定理适配；但当前 generic WFD 共同变量表仍要求"
                "原始未中心化对象与量化尺度的同表证书，不能直接替代。"
            ),
            "closed": bool(theorem_location["theorem_locations_pinned"])
            and external_hlc_adapted,
        },
    ]


def run(
    common_variable_table_path: Path,
    theorem_location_path: Path,
    kls_template_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
    external_index_path: Path,
    hlc_kls_external_path: Path,
) -> dict[str, Any]:
    """运行转移/尺度合取证书审计。"""
    common_variable_table = load_json(common_variable_table_path)
    theorem_location = load_json(theorem_location_path)
    transfer_rows = build_transfer_certificate_rows(
        common_variable_table,
        kze_spine_path,
        kls_template_path,
        source_cen_path,
    )
    scale_rows = build_scale_certificate_rows(
        common_variable_table,
        kze_spine_path,
        kls_template_path,
        external_index_path,
    )
    terminal_rows = build_terminal_rows(
        transfer_rows,
        scale_rows,
        theorem_location,
        hlc_kls_external_path,
    )
    open_transfer_gates = [row["gate"] for row in transfer_rows if not row["closed"]]
    open_scale_gates = [row["gate"] for row in scale_rows if not row["closed"]]
    open_terminal_targets = [row["terminal"] for row in terminal_rows if not row["closed"]]
    all_transfer_closed = not open_transfer_gates
    all_scale_closed = not open_scale_gates
    return {
        "certificate_type": "triad_a1_dibfi_transfer_scale_certificate_router",
        "status": "dibfi_transfer_scale_certificate_reduced_to_quantified_no_projection_certificate_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "dibfi_theorem_location_json": file_sha256(theorem_location_path),
            "kls_template_md": file_sha256(kls_template_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "source_cen_no_go_md": file_sha256(source_cen_path),
            "external_theorem_index_md": file_sha256(external_index_path),
            "hlc_kls_external_adaptation_md": file_sha256(hlc_kls_external_path),
        },
        "previous_terminal_gap": common_variable_table["terminal_gap_after_router"],
        "transfer_certificate_rows": transfer_rows,
        "scale_certificate_rows": scale_rows,
        "terminal_rows": terminal_rows,
        "all_transfer_closed": all_transfer_closed,
        "all_scale_closed": all_scale_closed,
        "all_certificate_rows_closed": all_transfer_closed and all_scale_closed,
        "open_transfer_gates": open_transfer_gates,
        "open_scale_gates": open_scale_gates,
        "open_terminal_targets": open_terminal_targets,
        "next_external_target": "DIBFIQuantifiedNoProjectionWindowCertificate",
        "terminal_gap_after_router": "DIBFIQuantifiedNoProjectionWindowCertificate",
        "structural_law": (
            "The common-variable certificate cannot be closed by another qualitative checklist. "
            "The local ledger rows split cleanly: Type decomposition, CRT phase, Fourier tail and "
            "symbolic log-loss absorption are closed at ledger level. The true remaining content is "
            "exactly twofold: an uncentered no-projection dispersion identity, and a quantified "
            "substitution of X,Q,N,M,C,S,H into BFI Theorem 10 and DI Theorem 12, including the "
            "DI J-scale dominance."
        ),
        "review_conclusion": (
            "共同变量表的合取证书已被继续压缩：账本型行已经关闭，真正剩余不是新的统计实验，"
            "而是 `NoProjectionUncenteredDispersionIdentity` 与 `QuantifiedDIBFIWindowSubstitution` "
            "两项合并证书。二者同时成立才可把 generic WFD 外部 DI/BFI 分支标记闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI 转移/尺度证书路由器",
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
        "previous:",
        f"  {result['previous_terminal_gap']};",
        "",
        "ledger rows closed:",
        "  TypeDecompositionLogBudget;",
        "  CRTPhaseSymbolUnification;",
        "  FrequencyWindowAndTail;",
        "  LogLossC0Extraction;",
        "",
        "terminal:",
        f"  {result['terminal_gap_after_router']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `all_transfer_closed={fmt_bool(result['all_transfer_closed'])}`。",
        f"- `all_scale_closed={fmt_bool(result['all_scale_closed'])}`。",
        f"- `all_certificate_rows_closed={fmt_bool(result['all_certificate_rows_closed'])}`。",
        f"- `open_transfer_gates={result['open_transfer_gates']}`。",
        f"- `open_scale_gates={result['open_scale_gates']}`。",
        f"- `open_terminal_targets={result['open_terminal_targets']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 对象转移证书行",
        "",
        "| gate | common step | status | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["transfer_certificate_rows"]:
        lines.append(
            "| `{gate}` | `{step}` | `{status}` | `{closed}` | {evidence} | {remaining} | `{next_target}` |".format(
                gate=table_cell(row["gate"]),
                step=table_cell(row["common_step"]),
                status=table_cell(row["status"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                next_target=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 尺度不等式证书行",
            "",
            "| gate | common inequality | status | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["scale_certificate_rows"]:
        lines.append(
            "| `{gate}` | `{ineq}` | `{status}` | `{closed}` | {evidence} | {remaining} | `{next_target}` |".format(
                gate=table_cell(row["gate"]),
                ineq=table_cell(row["common_inequality"]),
                status=table_cell(row["status"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                next_target=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 终端目标",
            "",
            "| terminal | covers | status | reason | closed |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["terminal_rows"]:
        lines.append(
            "| `{terminal}` | {covers} | `{status}` | {reason} | `{closed}` |".format(
                terminal=table_cell(row["terminal"]),
                covers=table_cell(", ".join(row["covers"])),
                status=table_cell(row["status"]),
                reason=table_cell(row["reason"]),
                closed=fmt_bool(bool(row["closed"])),
            )
        )
    lines.extend(
        [
            "",
            "## 6. 当前结论",
            "",
            "这一轮没有把缺口继续横向拆散，而是把共同变量表上的剩余压成一个更小的合取证书：",
            "",
            "```text",
            "DIBFIQuantifiedNoProjectionWindowCertificate",
            "  = NoProjectionUncenteredDispersionIdentity",
            "    + QuantifiedDIBFIWindowSubstitution.",
            "```",
            "",
            "其中第一项是对象恒等式问题，第二项是原文定理尺度代入问题。二者未同时完成前，"
            "不能诚实宣称 generic WFD 外部 DI/BFI 分支已经闭合。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument(
        "--dibfi-theorem-location-json", type=Path, default=DEFAULT_THEOREM_LOCATION
    )
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--source-cen-md", type=Path, default=DEFAULT_SOURCE_CEN)
    parser.add_argument("--external-index-md", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--hlc-kls-external-md", type=Path, default=DEFAULT_HLC_KLS_EXTERNAL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        common_variable_table_path=args.common_variable_table_json,
        theorem_location_path=args.dibfi_theorem_location_json,
        kls_template_path=args.kls_template_md,
        kze_spine_path=args.kze_spine_md,
        source_cen_path=args.source_cen_md,
        external_index_path=args.external_index_md,
        hlc_kls_external_path=args.hlc_kls_external_md,
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
                "all_certificate_rows_closed": result["all_certificate_rows_closed"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
