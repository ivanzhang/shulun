#!/usr/bin/env python3
"""把 full-S non-AP WFD KLS 输入压成完成型 residue 权重 KLS 输入。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_full_s_completion_reduction_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_NEW_FULL_S_INPUT = (
    DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
)
DEFAULT_FULL_S_KLS_NOTE = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization.md"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_SOURCE_CEN_NO_GO = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.md"


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
    new_full_s_input: dict[str, Any],
    full_s_kls_note_path: Path,
    common_variable_table: dict[str, Any],
    kls_template_path: Path,
    kze_spine_path: Path,
    source_cen_no_go_path: Path,
) -> list[dict[str, Any]]:
    """构造 full-S 完成型压缩账本。"""
    prior_ready = (
        new_full_s_input["terminal_gap_after_router"]
        == "FullSNonAPWFDKLSTheoremInput"
        and new_full_s_input["open_input_gates"] == ["FullSNonAPWFDKLSTheoremInput"]
    )
    full_s_window_ready = contains_all(
        full_s_kls_note_path,
        [
            "C≈P/log",
            "S≈P=X^(1/2+o(1))",
            "0<|h|<=H<=P/log",
            "NaturalWFDScale",
        ],
    ) and contains_all(
        kls_template_path,
        [
            "C ≍ P/log",
            "S ≍ P",
            "0<|h|<=H<=P/log",
        ],
    )
    variables_ready = table_has_fixed_symbol(
        common_variable_table, "c,C"
    ) and table_has_fixed_symbol(common_variable_table, "s,S")
    completion_algebra_ready = contains_all(
        kze_spine_path,
        [
            "CRT 合并变量",
            "标准 Kloosterman 逆元相位",
            "WFD-core",
        ],
    )
    loss_budget_ready = contains_all(
        full_s_kls_note_path,
        ["dyadic/gcd/smoothing/endpoint", "B(A)"],
    ) or contains_all(kls_template_path, ["dyadic 分块", "gcd strata", "B(A)"])
    residue_flatness_not_available = contains_all(
        source_cen_no_go_path,
        ["divisor-bounded", "零均值", "未中心化"],
    )
    completed_atom_pinned = all(
        [
            prior_ready,
            full_s_window_ready,
            variables_ready,
            completion_algebra_ready,
            loss_budget_ready,
            residue_flatness_not_available,
        ]
    )
    return [
        {
            "gate": "PriorFullSNonAPWFDKLSInputAvailable",
            "closed": prior_ready,
            "evidence": (
                f"previous terminal={new_full_s_input['terminal_gap_after_router']}; "
                f"open={new_full_s_input['open_input_gates']}."
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "FullSCompletionDecomposition",
        },
        {
            "gate": "FullSOverModulusRatioIsPolylog",
            "closed": full_s_window_ready,
            "evidence": "Full-S contract and KLS template give S≈P and C≈P/log^O P, hence S/C=log^O P.",
            "remaining": "none at scale-ratio level",
            "next_target": "FullSCompletionDecomposition",
        },
        {
            "gate": "CommonVariablesSupportCompletion",
            "closed": variables_ready,
            "evidence": "共同变量表固定 c,C 与 s,S；完成分解不引入新变量叉路。",
            "remaining": "none at variable-table level",
            "next_target": "FullSCompletionDecomposition",
        },
        {
            "gate": "FullSCompletionDecomposition",
            "closed": full_s_window_ready and variables_ready and completion_algebra_ready,
            "evidence": (
                "对每个 c~C，把 s~S 写成 x+k c；完整块数 L_c≈S/c=log^O P，"
                "相位变成完整 residue Kloosterman 相位 e_c(a_h x+b_h bar{x})。"
            ),
            "remaining": "端点、非互素层和平滑只进入多对数损失账本。",
            "next_target": "ModulusDependentCompletedFullSKLSInput",
        },
        {
            "gate": "EndpointAndGcdLossAbsorbed",
            "closed": loss_budget_ready,
            "evidence": "FullS-KLS-ext 与 KLS 模板已有 dyadic/gcd/smoothing/endpoint 的 B(A) 损失账本。",
            "remaining": "none after choosing B(A) larger",
            "next_target": "ModulusDependentCompletedFullSKLSInput",
        },
        {
            "gate": "FlatResidueMassShortcutUnavailable",
            "closed": residue_flatness_not_available,
            "evidence": (
                "当前 generic beta_s 只要求 divisor-bounded；SOURCE-CEN no-go 已记录未中心化对象"
                "没有块内零均值/平坦性。"
            ),
            "remaining": "不能把 residue 权重当作常数后只用完整 Weil 和。",
            "next_target": "ModulusDependentCompletedFullSKLSInput",
        },
        {
            "gate": "ModulusDependentCompletedAtomPinned",
            "closed": completed_atom_pinned,
            "evidence": (
                "完成后 residue 权重 B_{c,x}=sum_k beta_{x+kc} 依赖模数 c；"
                "这正是 full-S 输入的不可再逃避核心。"
            ),
            "remaining": "none at target-definition level",
            "next_target": "ModulusDependentCompletedFullSKLSInput",
        },
        {
            "gate": "ModulusDependentCompletedFullSKLSInput",
            "closed": False,
            "evidence": "仓库尚无针对 B_{c,x} 模数依赖 residue 权重的完成型 KLS/dispersion 定理。",
            "remaining": "证明或引用完成型、模数依赖 residue 权重的 full-S Kloosterman 平均估计。",
            "next_target": "ModulusDependentCompletedFullSKLSInput",
        },
    ]


def run(
    new_full_s_input_path: Path,
    full_s_kls_note_path: Path,
    common_variable_table_path: Path,
    kls_template_path: Path,
    kze_spine_path: Path,
    source_cen_no_go_path: Path,
) -> dict[str, Any]:
    """运行 full-S 完成型压缩路由。"""
    new_full_s_input = load_json(new_full_s_input_path)
    common_variable_table = load_json(common_variable_table_path)
    rows = build_rows(
        new_full_s_input,
        full_s_kls_note_path,
        common_variable_table,
        kls_template_path,
        kze_spine_path,
        source_cen_no_go_path,
    )
    return {
        "certificate_type": "triad_a1_dibfi_full_s_completion_reduction_router",
        "status": "full_s_nonap_wfd_kls_input_reduced_to_modulus_dependent_completed_kls_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "new_full_s_input_json": file_sha256(new_full_s_input_path),
            "full_s_kls_note_md": file_sha256(full_s_kls_note_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "kls_template_md": file_sha256(kls_template_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "source_cen_no_go_md": file_sha256(source_cen_no_go_path),
        },
        "previous_terminal_gap": new_full_s_input["terminal_gap_after_router"],
        "completion_rows": rows,
        "closed_completion_gates": [row["gate"] for row in rows if row["closed"]],
        "open_completion_gates": [row["gate"] for row in rows if not row["closed"]],
        "full_s_completion_reduction_closed": False,
        "terminal_gap_after_router": "ModulusDependentCompletedFullSKLSInput",
        "terminal_gap_expansion": ["ModulusDependentCompletedFullSKLSInput"],
        "completion_formula": {
            "residue_weight": "B_{c,x}=sum_{k: x+k*c in S-block} beta_{x+k*c} W((x+k*c)/S)",
            "completed_sum": "sum_{c~C} lambda_c sum_{0<|h|<=H} omega_h sum_{x mod c}^* B_{c,x} e_c(a_h*x+b_h*bar{x})",
            "block_count": "L_c=S/c=log^O(P)",
        },
        "required_theorem_clauses": [
            "handles c-dependent residue weights B_{c,x}",
            "keeps the current uncentered no-projection non-AP object",
            "uses C≈P/log^O P, S≈P and H<=P/log^O P",
            "absorbs endpoint, gcd, dyadic and smoothing losses into B(A)",
            "delivers NaturalWFDScale/log^A P for every A>0",
        ],
        "structural_law": (
            "Because S≈P while C≈P/log^O P, the full-S inverse window contains only polylog many "
            "complete residue blocks modulo each c. Thus the incomplete s-window itself is no "
            "longer the sharp obstruction: it can be completed algebraically. The obstruction "
            "moves to the completed residue weights B_{c,x}, which depend on c and are not flat "
            "for generic divisor-bounded beta_s. Therefore the remaining theorem input is a "
            "modulus-dependent completed Kloosterman average, not a vague full-S estimate."
        ),
        "review_conclusion": (
            "`FullSNonAPWFDKLSTheoremInput` 已被完成分解压成 "
            "`ModulusDependentCompletedFullSKLSInput`：full-S 长度可按模 c 完成，"
            "真正剩余是处理依赖 c 的 residue 权重 B_{c,x} 的完整 Kloosterman 平均定理。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI full-S completion reduction 路由器",
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
        "## 2. 完成公式",
        "",
        f"- `residue_weight={result['completion_formula']['residue_weight']}`。",
        f"- `completed_sum={result['completion_formula']['completed_sum']}`。",
        f"- `block_count={result['completion_formula']['block_count']}`。",
        "",
        "## 3. 汇总",
        "",
        f"- `full_s_completion_reduction_closed={fmt_bool(result['full_s_completion_reduction_closed'])}`。",
        f"- `closed_completion_gates={result['closed_completion_gates']}`。",
        f"- `open_completion_gates={result['open_completion_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 4. 必要定理条款",
        "",
    ]
    for clause in result["required_theorem_clauses"]:
        lines.append(f"- `{clause}`。")
    lines.extend(
        [
            "",
            "## 5. 完成型账本表",
            "",
            "| gate | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["completion_rows"]:
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
            "ModulusDependentCompletedFullSKLSInput:",
            "  prove/cite a completed Kloosterman average with c-dependent residue weights B_{c,x}.",
            "```",
            "",
            "这一步没有证明该完成型定理；它利用 full-S 长度把非完整窗口硬点剥离掉，"
            "暴露出真正剩余的模数依赖权重问题。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--new-full-s-input-json", type=Path, default=DEFAULT_NEW_FULL_S_INPUT
    )
    parser.add_argument("--full-s-kls-note-md", type=Path, default=DEFAULT_FULL_S_KLS_NOTE)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--source-cen-no-go-md", type=Path, default=DEFAULT_SOURCE_CEN_NO_GO)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        new_full_s_input_path=args.new_full_s_input_json,
        full_s_kls_note_path=args.full_s_kls_note_md,
        common_variable_table_path=args.common_variable_table_json,
        kls_template_path=args.kls_template_md,
        kze_spine_path=args.kze_spine_md,
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
                "open_completion_gates": result["open_completion_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
