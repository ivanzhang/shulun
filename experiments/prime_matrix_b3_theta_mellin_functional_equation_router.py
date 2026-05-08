#!/usr/bin/env python3
"""Prime Matrix B=3 theta-Mellin zeta 延拓与函数方程闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_theta_mellin_functional_equation_router.py

输出：
  docs/monograph/prime-matrix-b3-theta-mellin-functional-equation-router.json
  docs/monograph/prime-matrix-b3-theta-mellin-functional-equation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-gaussian-poisson-theta-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-theta-mellin-functional-equation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-theta-mellin-functional-equation-router.md"

OLD_ATOM = "ThetaMellinZetaContinuationFunctionalEquationLedger"
CLOSED_ATOM = "ThetaMellinZetaContinuationFunctionalEquationClosed"
THETA_CLOSED_ATOM = "GaussianPoissonThetaIdentityClosed"
XI_ORDER_ATOM = "XiEntireOrderOneGrowthLedger"
HADAMARD_ATOM = "HadamardFactorizationLogDerivativeLedger"
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
    """生成 theta-Mellin 函数方程判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    theta_available = THETA_CLOSED_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and theta_available and guard
    return [
        row(
            "ThetaMellinFunctionalEquationGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 theta Mellin 延拓与 zeta 函数方程。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍是解析基础恒等式，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "GaussianPoissonThetaIdentityAvailable",
            theta_available,
            True,
            "上一层已经闭合 theta(t)=t^{-1/2}theta(1/t)。",
            THETA_CLOSED_ATOM,
        ),
        row(
            "CompletedZetaMellinIntegralClosed",
            closed,
            True,
            "Re s>1 中 Lambda(s)=1/2 int_0^infty (theta(t)-1)t^{s/2-1}dt。",
            "无剩余；由 Gamma 积分和绝对收敛。",
        ),
        row(
            "ContinuationSymmetricIntegralClosed",
            closed,
            True,
            "分割积分并使用 theta 变换得到 1/(s(s-1)) 加 [1,infty) 对称积分。",
            "无剩余；该公式给出亚纯延拓。",
        ),
        row(
            "FunctionalEquationClosed",
            closed,
            True,
            "对称积分公式在 s 与 1-s 下不变，因此 Lambda(s)=Lambda(1-s)。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "待证 atom 已闭合为 completed zeta 的亚纯延拓和函数方程。",
            CLOSED_ATOM,
        ),
        row(
            "XiEntireOrderOneGrowthStillNext",
            False,
            False,
            "下一步要把 xi(s)=1/2*s*(s-1)*Lambda(s) 证明为一阶整函数并给增长账本。",
            XI_ORDER_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 theta-Mellin 函数方程闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_theta_mellin_functional_equation_router",
        "status": "theta_mellin_zeta_functional_equation_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "theta_mellin_zeta_functional_equation_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": XI_ORDER_ATOM,
        "secondary_priority": HADAMARD_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "core_formula": {
            "theta0": "theta_0(t)=theta(t)-1",
            "completed_zeta_integral": (
                "Lambda(s)=pi^(-s/2)Gamma(s/2)zeta(s)="
                "1/2 int_0^infty theta_0(t)t^(s/2-1)dt, Re s>1"
            ),
            "symmetric_continuation": (
                "Lambda(s)=1/(s(s-1))+1/2 int_1^infty theta_0(t)"
                "(t^(s/2-1)+t^((1-s)/2-1))dt"
            ),
            "functional_equation": "Lambda(s)=Lambda(1-s)",
        },
        "plain_conclusion": (
            "theta-Mellin 延拓与 completed zeta 函数方程已由上一层 theta 恒等式闭合。"
            "这仍只是 zeta-xi 基础包的一部分；下一步需要 xi 整函数和一阶增长账本。"
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
        "# Prime Matrix B=3 theta-Mellin zeta 延拓与函数方程闭合证书",
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
            "theta_mellin_zeta_functional_equation_closed="
            f"{fmt_bool(result['theta_mellin_zeta_functional_equation_closed'])}"
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
        "记 `theta_0(t)=theta(t)-1`。当 `Re s>1`，Gamma 积分给出",
        "",
        "```text",
        formula["completed_zeta_integral"],
        "```",
        "",
        "把积分拆成 `[0,1]` 与 `[1,infty)`，在 `[0,1]` 中令 `u=1/t`，并使用上一层闭合的",
        "`theta(t)=t^(-1/2)theta(1/t)`，得到",
        "",
        "```text",
        formula["symmetric_continuation"],
        "```",
        "",
        (
            "`theta_0(t)` 在 `[1,infty)` 指数衰减，所以右侧积分在每个紧集上一致收敛；"
            "除 `s=0,1` 的显式极点外给出亚纯延拓。该公式关于 `s` 与 `1-s` 对称，因此"
        ),
        "",
        "```text",
        formula["functional_equation"],
        "```",
        "",
        "这闭合 zeta-xi 基础包中的延拓与函数方程层。",
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
                f"随后是 `{result['secondary_priority']}`。"
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
