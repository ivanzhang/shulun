#!/usr/bin/env python3
"""Prime Matrix B=3 Gaussian-Poisson theta 恒等式闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_gaussian_poisson_theta_router.py

输出：
  docs/monograph/prime-matrix-b3-gaussian-poisson-theta-router.json
  docs/monograph/prime-matrix-b3-gaussian-poisson-theta-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zeta-xi-hadamard-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-gaussian-poisson-theta-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-gaussian-poisson-theta-router.md"

OLD_ATOM = "GaussianPoissonSummationThetaIdentityLedger"
CLOSED_ATOM = "GaussianPoissonThetaIdentityClosed"
MELLIN_ATOM = "ThetaMellinZetaContinuationFunctionalEquationLedger"
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


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12e}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def theta(t: float, cutoff: int = 120) -> float:
    """计算 theta(t)=sum exp(-pi n^2 t) 的有限截断，用于审计。"""
    total = 1.0
    for n in range(1, cutoff + 1):
        total += 2.0 * math.exp(-math.pi * n * n * t)
    return total


def numerical_theta_audit() -> list[dict[str, float]]:
    """用有限截断核验 theta(t)=t^{-1/2}theta(1/t)。"""
    rows: list[dict[str, float]] = []
    for t in [0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 10.0, 20.0]:
        left = theta(t)
        right = t ** -0.5 * theta(1.0 / t)
        rows.append(
            {
                "t": t,
                "theta_t": left,
                "transformed": right,
                "absolute_error": abs(left - right),
            }
        )
    return rows


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
    """生成 Gaussian-Poisson theta 恒等式判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and guard
    return [
        row(
            "GaussianPoissonThetaGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Gaussian Poisson 求和推出 theta 函数变换。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只是解析基础恒等式，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "PeriodicGaussianFourierCoefficientClosed",
            closed,
            True,
            "周期高斯 F_t(x)=sum_n exp(-pi t(n+x)^2) 的第 m 个 Fourier 系数为 t^{-1/2}exp(-pi m^2/t)。",
            "无剩余；由高斯 Fourier 积分和绝对一致收敛。",
        ),
        row(
            "ThetaModularIdentityClosed",
            closed,
            True,
            "令 x=0 得 theta(t)=t^{-1/2}theta(1/t)，即 Gaussian-Poisson theta 恒等式。",
            CLOSED_ATOM,
        ),
        row(
            "GaussianPoissonSummationThetaIdentityLedger",
            closed,
            True,
            "待证 atom 已由周期高斯 Fourier 级数闭合。",
            CLOSED_ATOM,
        ),
        row(
            "ThetaMellinFunctionalEquationStillNext",
            False,
            False,
            "下一步要把 theta 恒等式送入 Mellin 积分，推出 zeta 延拓和 Lambda 函数方程。",
            MELLIN_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Gaussian-Poisson theta 恒等式闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "GaussianPoissonSummationThetaIdentityLedger"
    )
    audit_rows = numerical_theta_audit()
    return {
        "certificate_type": "b3_gaussian_poisson_theta_router",
        "status": "gaussian_poisson_theta_identity_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "gaussian_poisson_theta_identity_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": MELLIN_ATOM,
        "secondary_priority": XI_ORDER_ATOM,
        "tertiary_priority": HADAMARD_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "theta_numerical_audit": audit_rows,
        "max_theta_audit_error": max(row["absolute_error"] for row in audit_rows),
        "proof_outline": [
            "For t>0 define F_t(x)=sum_{n in Z} exp(-pi*t*(n+x)^2).",
            "The series and its derivatives converge uniformly on compact x intervals, so F_t is smooth and 1-periodic.",
            "The m-th Fourier coefficient equals int_R exp(-pi*t*u^2) exp(-2*pi*i*m*u) du.",
            "The Gaussian Fourier integral gives t^(-1/2) exp(-pi*m^2/t).",
            "Evaluating the absolutely convergent Fourier series at x=0 gives theta(t)=t^(-1/2)theta(1/t).",
        ],
        "plain_conclusion": (
            "Gaussian-Poisson theta 恒等式可以在本文内自足闭合；它只依赖周期高斯的 Fourier "
            "系数计算和高斯积分。闭合后 zeta-xi 包的下一最窄点变为 theta Mellin 延拓与函数方程。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Gaussian-Poisson theta 恒等式闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"gaussian_poisson_theta_identity_closed={fmt_bool(result['gaussian_poisson_theta_identity_closed'])}",
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
        "设 `t>0`，",
        "",
        "```text",
        "F_t(x)=sum_{n in Z} exp(-pi*t*(n+x)^2).",
        "```",
        "",
        (
            "该级数及其逐项导数绝对一致收敛，所以 `F_t` 是光滑 1-周期函数。"
            "它的第 `m` 个 Fourier 系数为"
        ),
        "",
        "```text",
        "a_m=int_0^1 F_t(x) exp(-2*pi*i*m*x) dx",
        "   =int_R exp(-pi*t*u^2) exp(-2*pi*i*m*u) du",
        "   =t^(-1/2) exp(-pi*m^2/t).",
        "```",
        "",
        (
            "第一等号后把 `u=n+x` 展开为整条实线积分；最后一步是高斯 Fourier 积分。"
            "令 `x=0` 并用 Fourier 级数绝对收敛，得到"
        ),
        "",
        "```text",
        "theta(t)=sum_n exp(-pi*n^2*t)=t^(-1/2)sum_m exp(-pi*m^2/t)=t^(-1/2)theta(1/t).",
        "```",
        "",
        "这正是 zeta 函数方程所需的 theta 变换恒等式。",
        "",
        "## 3. 数值审计",
        "",
        "| t | theta(t) | transformed | abs error |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for item in result["theta_numerical_audit"]:
        lines.append(
            "| {t:.6g} | `{left}` | `{right}` | `{err}` |".format(
                t=item["t"],
                left=fmt_float(item["theta_t"]),
                right=fmt_float(item["transformed"]),
                err=fmt_float(item["absolute_error"]),
            )
        )
    lines.extend(
        [
            "",
            f"最大截断核验误差：`{fmt_float(result['max_theta_audit_error'])}`。",
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
                f"随后是 `{result['secondary_priority']}` 与 `{result['tertiary_priority']}`。"
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
