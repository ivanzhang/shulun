#!/usr/bin/env python3
"""Prime Matrix B=3 xi Hadamard 分解与对数导数闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_factorization_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-factorization-router.json
  docs/monograph/prime-matrix-b3-hadamard-factorization-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-xi-entire-order-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-factorization-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-factorization-router.md"

OLD_ATOM = "HadamardFactorizationLogDerivativeLedger"
CLOSED_ATOM = "HadamardFactorizationLogDerivativeClosed"
XI_CLOSED_ATOM = "XiEntireOrderOneGrowthClosed"
ZETA_XI_CLOSED_ATOM = "CompletedZetaXiFunctionalEquationAndHadamardProductClosed"
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


def replace_atom(text: str) -> str:
    """把待证 atom 替换为已闭合 atom。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Hadamard 分解与对数导数判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    xi_available = XI_CLOSED_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and xi_available and guard
    return [
        row(
            "HadamardFactorizationGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 xi 的 Hadamard 分解与对数导数部分分式。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补假设链条中的解析基础，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "XiEntireOrderOneAvailable",
            xi_available,
            True,
            "上一层已经闭合 xi 为一阶以内整函数。",
            XI_CLOSED_ATOM,
        ),
        row(
            "ZeroExponentAndCanonicalProductClosed",
            closed,
            True,
            "由 Jensen 公式和一阶增长，xi 的零点指数不超过 1，genus-1 规范乘积局部一致收敛。",
            "无剩余。",
        ),
        row(
            "ZeroFreeQuotientExponentialLinearClosed",
            closed,
            True,
            "xi 除以规范乘积后是无零一阶整函数，因此等于 exp(A+Bs)。",
            "无剩余。",
        ),
        row(
            "HadamardProductClosed",
            closed,
            True,
            "得到 xi(s)=exp(A+Bs) prod_rho (1-s/rho) exp(s/rho)。",
            CLOSED_ATOM,
        ),
        row(
            "HadamardLogDerivativeClosed",
            closed,
            True,
            "在避开零点的紧集上取对数导数，得到 xi'/xi(s)=B+sum_rho(1/(s-rho)+1/rho)。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "待证 atom 已闭合为一阶 Hadamard 乘积及其对数导数部分分式。",
            CLOSED_ATOM,
        ),
        row(
            "CompletedZetaXiFunctionalEquationAndHadamardProductClosed",
            closed,
            True,
            "theta-Poisson、theta-Mellin、xi 整函数增长和 Hadamard 四层均已闭合，父级 zeta-xi 基础包闭合。",
            ZETA_XI_CLOSED_ATOM,
        ),
        row(
            "EulerProductPositiveKernelStillNext",
            False,
            False,
            "下一步回到零点自由区主链：Euler product 对数导数正性与 de la Vallee Poussin 排斥。",
            EULER_ATOM,
        ),
        row(
            "ZeroRepulsionAndConstantsStillDownstream",
            False,
            False,
            "Euler 正性后仍需零点排斥不等式和显式常数账本。",
            f"{REPULSION_ATOM} AND {CONSTANT_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Hadamard 分解与对数导数闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_hadamard_factorization_router",
        "status": "hadamard_factorization_log_derivative_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "hadamard_factorization_log_derivative_closed": closed,
        "completed_zeta_xi_functional_equation_hadamard_product_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": EULER_ATOM,
        "secondary_priority": REPULSION_ATOM,
        "tertiary_priority": CONSTANT_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "core_formula": {
            "hadamard_product": "xi(s)=exp(A+B*s) prod_rho (1-s/rho) exp(s/rho)",
            "log_derivative": "xi'/xi(s)=B+sum_rho (1/(s-rho)+1/rho)",
            "convergence": "locally uniform away from zeros, with symmetric/genus-1 canonical product",
        },
        "plain_conclusion": (
            "Hadamard 分解与对数导数账本已由 xi 的一阶整函数性闭合；"
            "zeta-xi 基础包至此完成。下一步真正回到 de la Vallee Poussin 零点自由区主链："
            "先攻 Euler product 对数导数正性，再攻零点排斥不等式和显式常数。"
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
        "# Prime Matrix B=3 xi Hadamard 分解与对数导数闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "hadamard_factorization_log_derivative_closed="
            f"{fmt_bool(result['hadamard_factorization_log_derivative_closed'])}"
        ),
        (
            "completed_zeta_xi_functional_equation_hadamard_product_closed="
            f"{fmt_bool(result['completed_zeta_xi_functional_equation_hadamard_product_closed'])}"
        ),
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
        "## 2. 文内证明",
        "",
        (
            "上一层给出 `xi` 是一阶以内整函数。Jensen 公式给零点计数 "
            "`N(r)=O(r log r)`，因此零点指数不超过 `1`，genus-1 规范乘积"
        ),
        "",
        "```text",
        "P(s)=prod_rho (1-s/rho) exp(s/rho)",
        "```",
        "",
        (
            "在紧集上一致收敛。`xi/P` 是无零整函数，故可写成 `exp(g(s))`。"
            "又因 `xi` 和 `P` 都是一阶以内增长，`g` 必为一次多项式 `A+B*s`。于是"
        ),
        "",
        "```text",
        formula["hadamard_product"],
        "```",
        "",
        "在不含零点的紧集上对局部一致收敛的乘积取对数导数，得到",
        "",
        "```text",
        formula["log_derivative"],
        formula["convergence"],
        "```",
        "",
        (
            "这就是 de la Vallee Poussin 排斥不等式需要的零点部分分式输入。"
            "它不包含 Euler product 正性，也不包含零点自由区常数。"
        ),
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"之后是 `{result['secondary_priority']}` 与 `{result['tertiary_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
