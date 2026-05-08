#!/usr/bin/env python3
"""Prime Matrix B=3 zeta-xi-Hadamard 基础包路由器。

用法示例：
  python3 experiments/prime_matrix_b3_zeta_xi_hadamard_router.py

输出：
  docs/monograph/prime-matrix-b3-zeta-xi-hadamard-router.json
  docs/monograph/prime-matrix-b3-zeta-xi-hadamard-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zero-free-constants-router.json"
DEFAULT_EXPLICIT_FORMULA = ROOT / "docs" / "rh-pc1-explicit-formula-proof-appendix.md"
DEFAULT_PC1_THEOREMIZATION = ROOT / "docs" / "rh-pc1-analytic-input-theoremization.md"
DEFAULT_JSON = DOCS / "prime-matrix-b3-zeta-xi-hadamard-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-zeta-xi-hadamard-router.md"

OLD_ATOM = "CompletedZetaXiFunctionalEquationAndHadamardProductLedger"
POISSON_ATOM = "GaussianPoissonSummationThetaIdentityLedger"
MELLIN_ATOM = "ThetaMellinZetaContinuationFunctionalEquationLedger"
XI_ORDER_ATOM = "XiEntireOrderOneGrowthLedger"
HADAMARD_ATOM = "HadamardFactorizationLogDerivativeLedger"
EULER_ATOM = "EulerProductLogDerivativePositiveRealPartLedger"
REPULSION_ATOM = "DeLaValleePoussinZeroRepulsionInequalityLedger"
CONSTANT_ATOM = "ExplicitZeroFreeRegionConstantNumericalLedger"
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


def contains_any(text: str, needles: list[str]) -> bool:
    """检查文本是否包含任一片段。"""
    return any(needle in text for needle in needles)


def source_audit(texts: dict[str, str]) -> dict[str, Any]:
    """审查当前文档是否已包含 zeta-xi-Hadamard 基础包。"""
    combined = "\n".join(texts.values())
    explicit_formula_uses_zeta = all(
        needle in texts["explicit_formula"]
        for needle in ["Mellin", "-ζ'(s)/ζ(s)", "非平凡零点"]
    )
    gaussian_poisson_present = contains_any(
        combined,
        ["Poisson summation", "Poisson求和", "theta(t)=t^{-1/2}theta(1/t)"],
    )
    theta_mellin_present = contains_any(
        combined,
        [
            "pi^{-s/2} Gamma(s/2) zeta(s)",
            "π^{-s/2}Γ(s/2)ζ(s)",
            "theta Mellin",
        ],
    )
    xi_entire_order_present = contains_any(
        combined,
        ["xi entire order one", "xi 是整函数", "ξ 是整函数", "order one"],
    )
    hadamard_product_present = contains_any(
        combined,
        ["Hadamard product", "Hadamard 乘积", "xi'/xi", "ξ'/ξ"],
    )
    return {
        "explicit_formula_uses_zeta_log_derivative": explicit_formula_uses_zeta,
        "gaussian_poisson_theta_identity_present": gaussian_poisson_present,
        "theta_mellin_continuation_functional_equation_present": theta_mellin_present,
        "xi_entire_order_one_growth_present": xi_entire_order_present,
        "hadamard_factorization_log_derivative_present": hadamard_product_present,
    }


def replacement_pair() -> str:
    """写出 zeta-xi-Hadamard 账本的自足替换包。"""
    return f"({POISSON_ATOM} AND {MELLIN_ATOM} AND {XI_ORDER_ATOM} AND {HADAMARD_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧 zeta-xi-Hadamard 原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


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
    """生成 zeta-xi-Hadamard 基础包判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    poisson_closed = bool(audit["gaussian_poisson_theta_identity_present"])
    mellin_closed = bool(audit["theta_mellin_continuation_functional_equation_present"])
    xi_order_closed = bool(audit["xi_entire_order_one_growth_present"])
    hadamard_closed = bool(audit["hadamard_factorization_log_derivative_present"])
    reduced = active and guard and bool(audit["explicit_formula_uses_zeta_log_derivative"])
    return [
        row(
            "ZetaXiHadamardGateActive",
            active,
            False,
            "上一层唯一内部最窄点是完整 zeta-xi 函数方程与 Hadamard 乘积账本。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补假设链条的解析基础，不用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ExplicitFormulaUsesButDoesNotProveZeta",
            bool(audit["explicit_formula_uses_zeta_log_derivative"]),
            True,
            "已有显式公式使用 -zeta'/zeta 和零点，但它把 zeta 解析基础作为背景。",
            "需要下沉到 theta-Poisson 证明包。",
        ),
        row(
            "GaussianPoissonThetaIdentityMissing",
            poisson_closed,
            False,
            "需要证明 Gaussian Poisson 求和并推出 theta(t)=t^{-1/2}theta(1/t)。",
            POISSON_ATOM,
        ),
        row(
            "ThetaMellinFunctionalEquationMissing",
            mellin_closed,
            False,
            "需要由 theta Mellin 积分给出 zeta 延拓与 Lambda(s)=Lambda(1-s)。",
            MELLIN_ATOM,
        ),
        row(
            "XiEntireOrderOneGrowthMissing",
            xi_order_closed,
            False,
            "需要用 Gamma/Stirling 与 theta 积分控制 xi 为一阶整函数。",
            XI_ORDER_ATOM,
        ),
        row(
            "HadamardFactorizationLogDerivativeMissing",
            hadamard_closed,
            False,
            "需要把一阶整函数分解成 Hadamard 乘积并给出 xi'/xi 的可用部分分式。",
            HADAMARD_ATOM,
        ),
        row(
            "ZetaXiHadamardReducedToThetaPoissonPackage",
            reduced,
            False,
            "旧 zeta-xi-Hadamard 原子被压成 theta-Poisson、Mellin 延拓、xi 增长阶、Hadamard 对数导数四包。",
            replacement_pair(),
        ),
        row(
            "EulerProductPositiveKernelStillNext",
            False,
            False,
            "zeta-xi 包完成后，仍需 Euler product 对数导数正性接入零点排斥。",
            EULER_ATOM,
        ),
        row(
            "ZeroRepulsionAndConstantsStillDownstream",
            False,
            False,
            "随后才是 de la Vallee Poussin 排斥不等式和显式常数账本。",
            f"{REPULSION_ATOM} AND {CONSTANT_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 zeta-xi-Hadamard 基础包路由。"""
    previous = load_json(paths["previous"])
    texts = {name: path.read_text(encoding="utf-8") for name, path in paths.items() if name != "previous"}
    audit = source_audit(texts)
    rows = build_rows(previous, audit)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ZetaXiHadamardReducedToThetaPoissonPackage"
    )
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_zeta_xi_hadamard_router",
        "status": "zeta_xi_hadamard_reduced_to_theta_poisson_package_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zeta_xi_hadamard_reduced": reduced,
        "zeta_xi_hadamard_self_contained_proved": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": POISSON_ATOM,
        "secondary_priority": MELLIN_ATOM,
        "tertiary_priority": XI_ORDER_ATOM,
        "quaternary_priority": HADAMARD_ATOM,
        "downstream_priority": EULER_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "source_audit": audit,
        "core_formula": {
            "theta_identity": "theta(t)=t^(-1/2) theta(1/t)",
            "completed_zeta": "Lambda(s)=pi^(-s/2) Gamma(s/2) zeta(s)",
            "mellin_continuation": (
                "Lambda(s)=1/(s(s-1)) + 1/2 int_1^infty "
                "(theta(t)-1)(t^(s/2-1)+t^((1-s)/2-1)) dt"
            ),
            "xi_definition": "xi(s)=1/2*s*(s-1)*Lambda(s), xi(s)=xi(1-s)",
            "hadamard_log_derivative": "xi'/xi(s)=B + sum_rho (1/(s-rho)+1/rho)",
        },
        "plain_conclusion": (
            "当前仓库的显式公式已经使用 zeta 零点语言，但没有把 zeta 的函数方程、"
            "xi 整函数阶与 Hadamard 乘积逐行内联。该基础包不能直接给零点自由区；"
            "它只是 de la Vallee Poussin 排斥不等式的底座。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    formula = result["core_formula"]
    lines = [
        "# Prime Matrix B=3 zeta-xi-Hadamard 基础包路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"zeta_xi_hadamard_reduced={fmt_bool(result['zeta_xi_hadamard_reduced'])}",
        f"zeta_xi_hadamard_self_contained_proved={fmt_bool(result['zeta_xi_hadamard_self_contained_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 核心公式目标",
        "",
        "```text",
        formula["theta_identity"],
        formula["completed_zeta"],
        formula["mellin_continuation"],
        formula["xi_definition"],
        formula["hadamard_log_derivative"],
        "```",
        "",
        "这些公式闭合后只得到零点排斥所需的解析骨架；还没有给出零点自由区常数。",
        "",
        "## 3. 来源审查",
        "",
        "| item | value |",
        "| --- | --- |",
    ]
    for key, value in result["source_audit"].items():
        lines.append(f"| {table_cell(key)} | `{fmt_bool(value)}` |")
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
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后依次是 `{result['secondary_priority']}`、`{result['tertiary_priority']}`、"
                f"`{result['quaternary_priority']}`，再回到 `{result['downstream_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--explicit-formula", type=Path, default=DEFAULT_EXPLICIT_FORMULA)
    parser.add_argument("--pc1", type=Path, default=DEFAULT_PC1_THEOREMIZATION)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "explicit_formula": args.explicit_formula,
        "pc1": args.pc1,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
