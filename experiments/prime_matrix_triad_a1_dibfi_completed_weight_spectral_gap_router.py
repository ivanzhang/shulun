#!/usr/bin/env python3
"""把完成型 full-S KLS 输入压成 c 依赖 residue 权重谱抵消输入。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_completed_weight_spectral_gap_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_COMPLETION_REDUCTION = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_KLS_SELF_CONTAINED = DOCS / "prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md"
DEFAULT_SOURCE_CEN_NO_GO = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.md"


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


def table_has_fixed_symbol(common_variable_table: dict[str, Any], symbol: str) -> bool:
    """核查共同变量表是否固定指定符号。"""
    return any(
        row["symbol"] == symbol and row["fixed_by_table"]
        for row in common_variable_table["variable_rows"]
    )


def build_rows(
    completion_reduction: dict[str, Any],
    common_variable_table: dict[str, Any],
    kls_template_path: Path,
    kze_spine_path: Path,
    kls_self_contained_path: Path,
    source_cen_no_go_path: Path,
) -> list[dict[str, Any]]:
    """构造完成型权重谱缺口账本。"""
    prior_ready = (
        completion_reduction["terminal_gap_after_router"]
        == "ModulusDependentCompletedFullSKLSInput"
        and completion_reduction["open_completion_gates"]
        == ["ModulusDependentCompletedFullSKLSInput"]
    )
    variables_ready = table_has_fixed_symbol(
        common_variable_table, "c,C"
    ) and table_has_fixed_symbol(common_variable_table, "s,S")
    l2_budget_ready = (
        variables_ready
        and "B_{c,x}" in completion_reduction["completion_formula"]["residue_weight"]
        and contains_all(kls_template_path, ["divisor bound", "B(A)"])
    )
    flat_shortcut_blocked = "FlatResidueMassShortcutUnavailable" in completion_reduction[
        "closed_completion_gates"
    ] and contains_all(
        source_cen_no_go_path,
        ["divisor-bounded", "零均值", "未中心化"],
    )
    pointwise_weil_blocked = contains_all(
        kls_self_contained_path,
        ["为什么点态 Weil 不能闭合", "不能产生任意", "log^{-A}"],
    )
    ordinary_large_sieve_blocked = contains_all(
        kze_spine_path,
        ["点态 Weil 只给单模平方根抵消", "普通大筛", "差一个主尺度"],
    )
    spectral_atom_pinned = all(
        [
            prior_ready,
            l2_budget_ready,
            flat_shortcut_blocked,
            pointwise_weil_blocked,
            ordinary_large_sieve_blocked,
        ]
    )
    return [
        {
            "gate": "PriorCompletedFullSKLSInputAvailable",
            "closed": prior_ready,
            "evidence": (
                f"previous terminal={completion_reduction['terminal_gap_after_router']}; "
                f"open={completion_reduction['open_completion_gates']}."
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "CDependentResidueWeightSpectralCancellationInput",
        },
        {
            "gate": "CompletedResidueL2BudgetAvailable",
            "closed": l2_budget_ready,
            "evidence": (
                "B_{c,x}=sum_k beta_{x+kc}; L_c=S/c=log^O(P); divisor-bounded beta gives "
                "sum_x |B_{c,x}|^2 <= log^O(P) sum_s |beta_s|^2."
            ),
            "remaining": "L2 控制只给自然尺度账本，不给任意 log-saving。",
            "next_target": "CDependentResidueWeightSpectralCancellationInput",
        },
        {
            "gate": "FlatResidueShortcutStillBlocked",
            "closed": flat_shortcut_blocked,
            "evidence": "generic beta_s 没有 residue 平坦/零均值；SOURCE-CEN no-go 禁止免费中心化。",
            "remaining": "不能把 B_{c,x} 当作常数或已中心化权重。",
            "next_target": "CDependentResidueWeightSpectralCancellationInput",
        },
        {
            "gate": "PointwiseWeilL2NoLogSaving",
            "closed": pointwise_weil_blocked,
            "evidence": "KLS 自足脊柱已记录点态 Weil+Cauchy 只能给临界平方根级控制，不能产生任意 log^{-A}。",
            "remaining": "需要模数族与频率族上的谱平均抵消。",
            "next_target": "CDependentResidueWeightSpectralCancellationInput",
        },
        {
            "gate": "OrdinaryLargeSieveNoCDependentWeight",
            "closed": ordinary_large_sieve_blocked,
            "evidence": "KZ-E spine 已记录普通大筛在平衡 Type-II 块差一个主尺度。",
            "remaining": "完成型权重依赖 c，不能由不带 dispersion/Kuznetsov 结构的普通大筛闭合。",
            "next_target": "CDependentResidueWeightSpectralCancellationInput",
        },
        {
            "gate": "CDependentResidueSpectralAtomPinned",
            "closed": spectral_atom_pinned,
            "evidence": "所有朴素出口已排除；剩余必须利用 c,h 族上的谱/dispersion 平均抵消。",
            "remaining": "none at target-definition level",
            "next_target": "CDependentResidueWeightSpectralCancellationInput",
        },
        {
            "gate": "CDependentResidueWeightSpectralCancellationInput",
            "closed": False,
            "evidence": "仓库尚无针对 c 依赖 residue 权重 B_{c,x} 的谱/dispersion 抵消定理或自足证明。",
            "remaining": "证明或引用能处理 B_{c,x} 的完成型 Kuznetsov/DI-BFI 谱平均定理。",
            "next_target": "CDependentResidueWeightSpectralCancellationInput",
        },
    ]


def run(
    completion_reduction_path: Path,
    common_variable_table_path: Path,
    kls_template_path: Path,
    kze_spine_path: Path,
    kls_self_contained_path: Path,
    source_cen_no_go_path: Path,
) -> dict[str, Any]:
    """运行完成型权重谱缺口路由。"""
    completion_reduction = load_json(completion_reduction_path)
    common_variable_table = load_json(common_variable_table_path)
    rows = build_rows(
        completion_reduction,
        common_variable_table,
        kls_template_path,
        kze_spine_path,
        kls_self_contained_path,
        source_cen_no_go_path,
    )
    return {
        "certificate_type": "triad_a1_dibfi_completed_weight_spectral_gap_router",
        "status": "modulus_dependent_completed_kls_reduced_to_c_dependent_residue_spectral_input_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "completion_reduction_json": file_sha256(completion_reduction_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "kls_template_md": file_sha256(kls_template_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "kls_self_contained_md": file_sha256(kls_self_contained_path),
            "source_cen_no_go_md": file_sha256(source_cen_no_go_path),
        },
        "previous_terminal_gap": completion_reduction["terminal_gap_after_router"],
        "spectral_gap_rows": rows,
        "closed_spectral_gap_gates": [row["gate"] for row in rows if row["closed"]],
        "open_spectral_gap_gates": [row["gate"] for row in rows if not row["closed"]],
        "completed_weight_spectral_gap_closed": False,
        "terminal_gap_after_router": "CDependentResidueWeightSpectralCancellationInput",
        "terminal_gap_expansion": ["CDependentResidueWeightSpectralCancellationInput"],
        "scale_diagnosis": [
            "L_c=S/c=log^O(P)",
            "sum_x |B_{c,x}|^2 <= log^O(P) sum_s |beta_s|^2",
            "pointwise Weil + L2 reaches only natural/root scale",
            "arbitrary log-saving requires spectral averaging over c,h",
        ],
        "required_theorem_clauses": [
            "handles c-dependent residue weights B_{c,x}",
            "uses well-factorable lambda_c and smooth omega_h over c,h",
            "goes beyond pointwise Weil and ordinary large sieve",
            "keeps the uncentered no-projection non-AP WFD target",
            "delivers NaturalWFDScale/log^A P for every A>0",
        ],
        "structural_law": (
            "After full-S completion, the remaining obstacle is not the length of the s-window. "
            "The residue weights B_{c,x} have an L2 budget, but they are c-dependent and not "
            "flat or centered. Pointwise Weil with Cauchy reaches only the natural/root scale and "
            "ordinary large sieve lacks the required c,h dispersion structure. Therefore the next "
            "honest atom is a spectral cancellation theorem for c-dependent completed residue "
            "weights."
        ),
        "review_conclusion": (
            "`ModulusDependentCompletedFullSKLSInput` 已被压成 "
            "`CDependentResidueWeightSpectralCancellationInput`：L2/Weil、普通大筛和平坦 residue "
            "捷径都不足，必须证明或引用处理 B_{c,x} 的谱/dispersion 平均抵消。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI completed-weight spectral gap 路由器",
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
        "## 2. 尺度诊断",
        "",
    ]
    for item in result["scale_diagnosis"]:
        lines.append(f"- `{item}`。")
    lines.extend(
        [
            "",
            "## 3. 必要定理条款",
            "",
        ]
    )
    for clause in result["required_theorem_clauses"]:
        lines.append(f"- `{clause}`。")
    lines.extend(
        [
            "",
            "## 4. 汇总",
            "",
            f"- `completed_weight_spectral_gap_closed={fmt_bool(result['completed_weight_spectral_gap_closed'])}`。",
            f"- `closed_spectral_gap_gates={result['closed_spectral_gap_gates']}`。",
            f"- `open_spectral_gap_gates={result['open_spectral_gap_gates']}`。",
            f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
            "",
            "## 5. 谱缺口账本表",
            "",
            "| gate | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["spectral_gap_rows"]:
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
            "## 6. 当前结论",
            "",
            "唯一剩余继续变窄为：",
            "",
            "```text",
            "CDependentResidueWeightSpectralCancellationInput:",
            "  prove/cite spectral DI/BFI/Kuznetsov cancellation",
            "  for completed Kloosterman sums with c-dependent B_{c,x}.",
            "```",
            "",
            "这一步没有证明该谱定理；它排除了点态 Weil、普通大筛和 residue 平坦捷径。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--completion-reduction-json", type=Path, default=DEFAULT_COMPLETION_REDUCTION
    )
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument(
        "--kls-self-contained-md", type=Path, default=DEFAULT_KLS_SELF_CONTAINED
    )
    parser.add_argument("--source-cen-no-go-md", type=Path, default=DEFAULT_SOURCE_CEN_NO_GO)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        completion_reduction_path=args.completion_reduction_json,
        common_variable_table_path=args.common_variable_table_json,
        kls_template_path=args.kls_template_md,
        kze_spine_path=args.kze_spine_md,
        kls_self_contained_path=args.kls_self_contained_md,
        source_cen_no_go_path=args.source_cen_no_go_md,
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
                "open_spectral_gap_gates": result["open_spectral_gap_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
