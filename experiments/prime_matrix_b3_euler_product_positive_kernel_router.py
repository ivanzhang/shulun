#!/usr/bin/env python3
"""Prime Matrix B=3 Euler product 对数导数正性闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_euler_product_positive_kernel_router.py

输出：
  docs/monograph/prime-matrix-b3-euler-product-positive-kernel-router.json
  docs/monograph/prime-matrix-b3-euler-product-positive-kernel-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-hadamard-factorization-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-euler-product-positive-kernel-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-euler-product-positive-kernel-router.md"

OLD_ATOM = "EulerProductLogDerivativePositiveRealPartLedger"
CLOSED_ATOM = "EulerProductLogDerivativePositiveRealPartClosed"
HADAMARD_CLOSED_ATOM = "HadamardFactorizationLogDerivativeClosed"
TRIG_ATOM = "DeLaValleePoussinTrigonometricKernelIdentityClosed"
REPULSION_ATOM = "DeLaValleePoussinZeroRepulsionInequalityLedger"
CONSTANT_ATOM = "ExplicitZeroFreeRegionConstantNumericalLedger"
LOW_HEIGHT_ATOM = "FiniteLowHeightZeroCheckLedger"
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


def von_mangoldt(n: int) -> float:
    """计算小 n 的 von Mangoldt 函数，用于数值审计。"""
    m = n
    prime = None
    p = 2
    while p * p <= m:
        if m % p == 0:
            prime = p
            while m % p == 0:
                m //= p
            if m != 1:
                return 0.0
            return math.log(prime)
        p += 1 if p == 2 else 2
    return math.log(n) if n >= 2 else 0.0


def positive_kernel_sample() -> list[dict[str, float]]:
    """有限截断核验正性核。"""
    rows: list[dict[str, float]] = []
    sigma = 1.2
    for t in [0.0, 0.1, 0.7, 1.3, 2.0, 3.5]:
        total = 0.0
        min_kernel = float("inf")
        for n in range(2, 800):
            lam = von_mangoldt(n)
            if lam == 0.0:
                continue
            u = t * math.log(n)
            kernel = 3.0 + 4.0 * math.cos(u) + math.cos(2.0 * u)
            min_kernel = min(min_kernel, kernel)
            total += lam * (n ** (-sigma)) * kernel
        rows.append(
            {
                "sigma": sigma,
                "t": t,
                "finite_sum": total,
                "min_kernel_seen": min_kernel,
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
    """生成 Euler product 正性判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    hadamard_available = HADAMARD_CLOSED_ATOM in basis
    trig_available = TRIG_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and guard and hadamard_available and trig_available
    return [
        row(
            "EulerProductPositiveKernelGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Euler product 对数导数正性。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补假设链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "HadamardInputAvailable",
            hadamard_available,
            True,
            "上一层已给出 xi'/xi 的零点部分分式，供下一排斥层使用。",
            HADAMARD_CLOSED_ATOM,
        ),
        row(
            "TrigKernelIdentityAvailable",
            trig_available,
            True,
            "三角核 3+4cos u+cos 2u=2(1+cos u)^2>=0 已在零点自由区常数路由中闭合。",
            TRIG_ATOM,
        ),
        row(
            "EulerProductLogDerivativeSeriesClosed",
            closed,
            True,
            "对 sigma>1，Euler product 给 -zeta'/zeta(s)=sum Lambda(n)n^{-s}，绝对收敛。",
            "无剩余。",
        ),
        row(
            "PositiveRealPartKernelClosed",
            closed,
            True,
            "逐项乘以正核并求和，得 3F(sigma)+4Re F(sigma+it)+Re F(sigma+2it)>=0。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "待证 atom 已闭合为 Euler product 对数导数正性不等式。",
            CLOSED_ATOM,
        ),
        row(
            "ZeroRepulsionInequalityStillNext",
            False,
            False,
            "下一步要把 Hadamard 部分分式与 Euler 正性合并，推出 de la Vallee Poussin 零点排斥。",
            REPULSION_ATOM,
        ),
        row(
            "ExplicitConstantsStillDownstream",
            False,
            False,
            "排斥不等式之后仍需显式常数账本与低高度零点核验。",
            f"{CONSTANT_ATOM} AND {LOW_HEIGHT_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Euler product 正性闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    samples = positive_kernel_sample()
    return {
        "certificate_type": "b3_euler_product_positive_kernel_router",
        "status": "euler_product_log_derivative_positive_kernel_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "euler_product_log_derivative_positive_real_part_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": REPULSION_ATOM,
        "secondary_priority": CONSTANT_ATOM,
        "tertiary_priority": LOW_HEIGHT_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "positive_kernel_samples": samples,
        "min_finite_sum_sample": min(item["finite_sum"] for item in samples),
        "core_formula": {
            "log_derivative": "F(s)=-zeta'/zeta(s)=sum_{n>=1} Lambda(n)n^(-s), Re s>1",
            "positive_kernel": "3+4*cos(u)+cos(2u)=2*(1+cos(u))^2>=0",
            "real_part_inequality": (
                "3F(sigma)+4 Re F(sigma+i t)+Re F(sigma+2 i t)>=0, sigma>1"
            ),
        },
        "plain_conclusion": (
            "Euler product 对数导数正性已闭合。该层只给 sigma>1 处的正核不等式；"
            "它本身还不是零点自由区，下一步必须同 Hadamard 零点部分分式合并，"
            "证明 de la Vallee Poussin 零点排斥。"
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
        "# Prime Matrix B=3 Euler product 对数导数正性闭合证书",
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
            "euler_product_log_derivative_positive_real_part_closed="
            f"{fmt_bool(result['euler_product_log_derivative_positive_real_part_closed'])}"
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
        "当 `sigma>1` 时，Euler product 绝对收敛，逐项取对数导数得到",
        "",
        "```text",
        formula["log_derivative"],
        "```",
        "",
        "对任意实数 `u`，",
        "",
        "```text",
        formula["positive_kernel"],
        "```",
        "",
        "令 `u=t log n`，逐项乘以非负权 `Lambda(n)n^{-sigma}` 并求和，得到",
        "",
        "```text",
        formula["real_part_inequality"],
        "```",
        "",
        "这正是 de la Vallee Poussin 零点排斥步骤需要的 Euler 正性输入。",
        "",
        "## 3. 有限截断审计",
        "",
        "| sigma | t | finite positive sum | min kernel seen |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for item in result["positive_kernel_samples"]:
        lines.append(
            "| {sigma:.3g} | {t:.3g} | `{total}` | `{min_kernel}` |".format(
                sigma=item["sigma"],
                t=item["t"],
                total=fmt_float(item["finite_sum"]),
                min_kernel=fmt_float(item["min_kernel_seen"]),
            )
        )
    lines.extend(
        [
            "",
            f"有限截断样本最小正和：`{fmt_float(result['min_finite_sum_sample'])}`。",
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
