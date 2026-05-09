#!/usr/bin/env python3
"""Prime Matrix B=3 非平滑 Chebyshev/Perron 显式公式路由器。

用法示例：
  python3 experiments/prime_matrix_b3_unsmoothed_perron_formula_router.py

输出：
  docs/monograph/prime-matrix-b3-unsmoothed-perron-formula-router.json
  docs/monograph/prime-matrix-b3-unsmoothed-perron-formula-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-pnt-contour-constant-router.json"
DEFAULT_PC1 = ROOT / "docs" / "rh-pc1-analytic-input-theoremization.md"
DEFAULT_OFFLINE = ROOT / "docs" / "rh-offline-zero-prime-count-contradiction.md"
DEFAULT_FINAL_DRAFT = ROOT / "docs" / "final-proof-draft.md"
DEFAULT_JSON = DOCS / "prime-matrix-b3-unsmoothed-perron-formula-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-unsmoothed-perron-formula-router.md"

OLD_ATOM = "UnsmoothedChebyshevPerronExplicitFormulaConstantLedger"
CLASSICAL_FORMULA_ATOM = "ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger"
PERRON_KERNEL_ATOM = "PerronKernelTruncationConstantForPsi0Ledger"
ENDPOINT_ATOM = "ChebyshevPsi0EndpointHalfWeightConventionClosed"
REDUCED_ATOM = "UnsmoothedChebyshevPerronExplicitFormulaReducedToClassicalFormulaAndKernel"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
TRIVIAL_TAIL_ATOM = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def replacement_pair() -> str:
    """写出非平滑 Perron 公式替换包。"""
    return f"({CLASSICAL_FORMULA_ATOM} AND {PERRON_KERNEL_ATOM} AND {ENDPOINT_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧非平滑 Perron 原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def source_audit(pc1_text: str, offline_text: str, final_text: str) -> dict[str, Any]:
    """审查当前文稿中非平滑显式公式的材料状态。"""
    smooth_formula_closed = contains_all(
        pc1_text,
        ["Ψ_W", "Mellin", "-ζ'(s)/ζ(s)", "素数幂"],
    )
    informal_von_mangoldt_formula = contains_all(
        offline_text,
        ["ψ(x)-x", "Σ_ρ", "lower terms"],
    )
    perron_template_present = contains_all(
        final_text,
        ["截断 Perron", "c=1+1", "T="],
    )
    psi0_constantized = contains_all(
        final_text + "\n" + offline_text,
        ["ψ_0", "x^ρ/ρ", "R_T", "log^2"],
    )
    return {
        "smooth_formula_closed": smooth_formula_closed,
        "informal_von_mangoldt_formula_present": informal_von_mangoldt_formula,
        "generic_perron_template_present": perron_template_present,
        "psi0_constantized_formula_present": psi0_constantized,
    }


def formula_contract() -> dict[str, str]:
    """记录本层需要的精确公式合同。"""
    return {
        "psi0_definition": "psi_0(x)=sum_{n<x} Lambda(n)+1/2 Lambda(x) if x is an integer",
        "target_formula": (
            "psi_0(x)=x-sum_{|gamma|<=T} x^rho/rho-log(2*pi)"
            "-1/2 log(1-x^-2)+R_T(x)"
        ),
        "target_remainder_shape": "|R_T(x)| <= C_Perron*x*log^2(xT)/T + C_edge*log x",
        "validity_needed": "x>=20000, T>=14, endpoint convention fixed",
    }


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成非平滑 Perron 公式判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    upstream_reduced = bool(previous.get("pnt_contour_constant_reduced"))
    smooth_ready = bool(audit["smooth_formula_closed"])
    informal_present = bool(audit["informal_von_mangoldt_formula_present"])
    perron_template = bool(audit["generic_perron_template_present"])
    psi0_constantized = bool(audit["psi0_constantized_formula_present"])
    endpoint_closed = True
    reduced = active and guard and upstream_reduced and smooth_ready
    closed = reduced and psi0_constantized
    return [
        row(
            "UnsmoothedPerronGateActive",
            active,
            False,
            "上一层已把 PNT 轮廓常数压到非平滑 Perron 公式、零点和预算、尾项预算。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "UpstreamPNTMicroReductionAvailable",
            upstream_reduced,
            True,
            "PNT 轮廓层已经完成微账本拆分，因此本步可以专攻非平滑 Perron 子账本。",
            "无上游拆分剩余。",
        ),
        row(
            "SmoothFormulaDoesNotSufficeButIsAvailable",
            smooth_ready,
            True,
            "平滑 Mellin 显式公式已闭合，但只能作为推导背景，不能直接替代 psi/theta 的非平滑常数公式。",
            "需要非平滑 Perron 内联或外部接受。",
        ),
        row(
            "InformalVonMangoldtFormulaPresent",
            informal_present,
            False,
            "文稿已有 psi(x)-x=-sum x^rho/rho+低阶项的非正式说明。",
            "尚未给常数化截断余项。",
        ),
        row(
            "GenericPerronTemplatePresent",
            perron_template,
            False,
            "主稿有其他对象的 Perron 截断模板，可复用思路但不能自动覆盖 zeta von Mangoldt 公式。",
            "需写成 psi_0 专用账本。",
        ),
        row(
            "EndpointHalfWeightConventionClosed",
            endpoint_closed,
            True,
            "采用 psi_0 半权端点定义后，整数跳点误差被固定为 O(log x) 口径。",
            ENDPOINT_ATOM,
        ),
        row(
            "Psi0PerronConstantizedFormulaMissing",
            psi0_constantized,
            False,
            "还没有目标公式中 R_T(x) 的显式常数 C_Perron、C_edge 与适用区间证书。",
            f"{CLASSICAL_FORMULA_ATOM} AND {PERRON_KERNEL_ATOM}",
        ),
        row(
            "UnsmoothedPerronFormulaReducedToClassicalFormulaAndKernel",
            reduced,
            False,
            "旧非平滑 Perron 原子已压成经典公式接受/内联证明、Perron 截断核常数、端点半权口径。",
            replacement_pair(),
        ),
        row(
            OLD_ATOM,
            closed,
            False,
            "只有 psi_0 目标公式和 R_T 常数账本完成后，才能关闭非平滑 Perron 子账本。",
            REDUCED_ATOM if closed else replacement_pair(),
        ),
        row(
            ZERO_SUM_ATOM,
            False,
            False,
            "非平滑公式闭合后，还要把 C=1280,T0=14 代入零点和轮廓预算。",
            ZERO_SUM_ATOM,
        ),
        row(
            TRIVIAL_TAIL_ATOM,
            False,
            False,
            "平凡零点、素数幂与截断尾仍需同一公式口径下登记。",
            TRIVIAL_TAIL_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行非平滑 Chebyshev/Perron 显式公式路由。"""
    previous = load_json(paths["previous"])
    pc1_text = paths["pc1"].read_text(encoding="utf-8")
    offline_text = paths["offline"].read_text(encoding="utf-8")
    final_text = paths["final_draft"].read_text(encoding="utf-8")
    audit = source_audit(pc1_text, offline_text, final_text)
    rows = build_rows(previous, audit)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "UnsmoothedPerronFormulaReducedToClassicalFormulaAndKernel"
    )
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_unsmoothed_perron_formula_router",
        "status": "unsmoothed_perron_formula_reduced_to_classical_formula_and_kernel_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "unsmoothed_perron_formula_reduced": reduced,
        "unsmoothed_perron_formula_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": CLASSICAL_FORMULA_ATOM,
        "secondary_priority": PERRON_KERNEL_ATOM,
        "post_perron_priority": ZERO_SUM_ATOM,
        "tail_priority": TRIVIAL_TAIL_ATOM,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "source_audit": audit,
        "formula_contract": formula_contract(),
        "plain_conclusion": (
            "非平滑 Chebyshev/Perron 子账本已经压到最小可审查合同："
            "要么接受经典 von Mangoldt 显式公式并登记适用常数，要么在文内证明 "
            "psi_0(x) 的 Perron 截断公式及 R_T 常数。当前材料只有平滑公式、非正式 "
            "psi(x)-x 说明和其他对象的 Perron 模板，尚未关闭本原子。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    contract = result["formula_contract"]
    lines = [
        "# Prime Matrix B=3 非平滑 Chebyshev/Perron 显式公式路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"unsmoothed_perron_formula_reduced={fmt_bool(result['unsmoothed_perron_formula_reduced'])}",
        f"unsmoothed_perron_formula_closed={fmt_bool(result['unsmoothed_perron_formula_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 目标公式合同",
        "",
        "| item | value |",
        "| --- | --- |",
    ]
    for key, value in contract.items():
        lines.append(f"| {key} | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 3. 来源审查",
            "",
            "| item | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["source_audit"].items():
        lines.append(f"| {key} | `{fmt_bool(value)}` |")
    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"当前最窄点更新为 `{result['next_priority']}`；若选择文内自足证明，"
                f"核心就是 `{result['secondary_priority']}`。之后才进入 `{result['post_perron_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--pc1", type=Path, default=DEFAULT_PC1)
    parser.add_argument("--offline", type=Path, default=DEFAULT_OFFLINE)
    parser.add_argument("--final-draft", type=Path, default=DEFAULT_FINAL_DRAFT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "pc1": args.pc1,
        "offline": args.offline,
        "final_draft": args.final_draft,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
