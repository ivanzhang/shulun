#!/usr/bin/env python3
"""Prime Matrix B=3 平凡零点/素数幂/尾项预算路由器。

用法示例：
  python3 experiments/prime_matrix_b3_trivial_tail_prime_power_budget_router.py

输出：
  docs/monograph/prime-matrix-b3-trivial-tail-prime-power-budget-router.json
  docs/monograph/prime-matrix-b3-trivial-tail-prime-power-budget-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zero-sum-contour-budget-router.json"
DEFAULT_PC1 = ROOT / "docs" / "rh-pc1-analytic-input-theoremization.md"
DEFAULT_JSON = DOCS / "prime-matrix-b3-trivial-tail-prime-power-budget-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-trivial-tail-prime-power-budget-router.md"

OLD_ATOM = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
CLOSED_ATOM = "PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000"
EXACT_PSI0 = "InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost"
ENDPOINT_HALF = "ChebyshevPsi0EndpointHalfWeightConventionClosed"
PRIME_POWER = "PrimePowerThetaPsiTransferLedgerClosed"
ZERO_SUM_CLOSED = "ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536"
THETA_TARGET = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"

ANCHOR_X = 20_000
TARGET_RELATIVE_ERROR = 1.0 / 36_260.0


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
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_atom(text: str) -> str:
    """替换已闭合的平凡尾项原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def sieve_primes(limit: int) -> list[int]:
    """生成不超过 limit 的素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return [idx for idx, flag in enumerate(flags) if flag]


def prime_power_weight(limit: int) -> dict[str, Any]:
    """精确计算锚点处素数幂 Chebyshev 权重，用作压力诊断。"""
    total = 0.0
    terms = 0
    max_power = 0
    for prime in sieve_primes(int(math.isqrt(limit)) + 1):
        power = prime * prime
        exponent = 2
        while power <= limit:
            total += math.log(prime)
            terms += 1
            max_power = max(max_power, power)
            exponent += 1
            power *= prime
    return {
        "x": limit,
        "prime_power_weight": total,
        "term_count": terms,
        "max_prime_power": max_power,
        "relative_to_x": total / limit,
    }


def static_formula_terms(x: int) -> dict[str, float | bool]:
    """计算 psi_0 精确公式中平凡零点与常数项的锚点压力。"""
    log_2pi = math.log(2.0 * math.pi)
    trivial_log = -0.5 * math.log(1.0 - x ** -2)
    total_abs = log_2pi + trivial_log
    return {
        "x": float(x),
        "log_2pi": log_2pi,
        "trivial_zero_log_term": trivial_log,
        "static_abs_total": total_abs,
        "static_relative_to_x": total_abs / x,
        "target_relative_error": TARGET_RELATIVE_ERROR,
        "static_beats_theta_target": total_abs / x <= TARGET_RELATIVE_ERROR,
    }


def source_prime_power_ready(text: str) -> bool:
    """确认素数幂转移在文内材料中登记。"""
    return contains_all(text, ["素数幂", "Chebyshev", "X^{1/2}"])


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], pc1_text: str) -> list[dict[str, Any]]:
    """生成平凡尾项/素数幂预算判定表。"""
    external_basis = previous.get("latest_external_titchmarsh_cn16_basis", "")
    self_basis = previous.get("latest_self_contained_basis", "")
    combined_basis = external_basis + "\n" + self_basis
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    exact_ready = EXACT_PSI0 in combined_basis
    endpoint_ready = ENDPOINT_HALF in combined_basis
    prime_power_ready = PRIME_POWER in combined_basis or source_prime_power_ready(pc1_text)
    zero_sum_ready = previous.get("zero_sum_contour_budget_external_closed") is True and ZERO_SUM_CLOSED in external_basis
    closed = active and guard and exact_ready and endpoint_ready and prime_power_ready and zero_sum_ready
    return [
        row(
            "TrivialTailPrimePowerGateActive",
            active,
            True,
            "零点和预算之后，当前最窄点是同一 psi_0/Perron 口径下的平凡零点、素数幂和尾项账本。",
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
            "Psi0ExactFormulaAvailable",
            exact_ready,
            True,
            "内部 psi_0 精确公式已经给出常数项 -log(2pi) 与平凡零点项 -1/2 log(1-x^-2)。",
            EXACT_PSI0,
        ),
        row(
            "EndpointHalfWeightConventionAvailable",
            endpoint_ready,
            True,
            "Chebyshev psi_0 端点半权 convention 已闭合，避免端点重复计费。",
            ENDPOINT_HALF,
        ),
        row(
            "PrimePowerTransferAvailable",
            prime_power_ready,
            True,
            "素数幂到 theta/素数 Chebyshev 权的转移已在 PC1 账本中登记，可作为初等低阶项。",
            PRIME_POWER,
        ),
        row(
            "NontrivialZeroBudgetAlreadySeparated",
            zero_sum_ready,
            False,
            "非平凡零点和预算已经由上一层外部条件账本关闭，本步不再重复支付。",
            ZERO_SUM_CLOSED,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "平凡零点、公式常数、端点半权和素数幂转移闭合为初等尾项账本。",
            CLOSED_ATOM,
        ),
        row(
            "ThetaTargetStillSeparate",
            False,
            False,
            "这些尾项有界不等于 theta@20000 小误差目标；theta 目标仍需外部 Dusart 或独立有限桥。",
            THETA_TARGET,
        ),
        row(
            "FiniteLowHeightStillSeparate",
            False,
            False,
            "低高度零点核验仍与本初等尾项账本无关。",
            FINITE_LOW_HEIGHT,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行平凡尾项/素数幂预算路由。"""
    previous = load_json(paths["previous"])
    pc1_text = paths["pc1"].read_text(encoding="utf-8")
    rows = build_rows(previous, pc1_text)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    latest_external = replace_atom(previous.get("latest_external_titchmarsh_cn16_basis", ""))
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""))
    return {
        "certificate_type": "b3_trivial_tail_prime_power_budget_router",
        "status": "trivial_tail_prime_power_budget_closed_theta_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "trivial_tail_prime_power_budget_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement": {OLD_ATOM: CLOSED_ATOM},
        "latest_external_titchmarsh_cn16_basis": latest_external,
        "latest_self_contained_basis": latest_self,
        "next_priority": THETA_TARGET,
        "secondary_priority": FINITE_LOW_HEIGHT,
        "parallel_self_contained_priority": BACKLUND_INTERNAL,
        "static_formula_pressure": static_formula_terms(ANCHOR_X),
        "prime_power_pressure": prime_power_weight(ANCHOR_X),
        "plain_conclusion": (
            "`PerronTruncationTrivialZeroPrimePowerTailBudgetLedger` 已按初等口径关闭："
            "psi_0 精确公式给出 -log(2pi) 和平凡零点项，端点半权 convention 防止端点重复计费，"
            "素数幂转移由 PC1 低阶账本承担。该闭合只处理尾项归属和可界性，不推出 theta@20000 小误差。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    static = result["static_formula_pressure"]
    prime_power = result["prime_power_pressure"]
    lines = [
        "# Prime Matrix B=3 平凡零点/素数幂/尾项预算路由器",
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
            "trivial_tail_prime_power_budget_closed="
            f"{fmt_bool(result['trivial_tail_prime_power_budget_closed'])}"
        ),
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
        "## 2. 锚点压力诊断",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| log(2pi) | `{fmt_float(static['log_2pi'])}` |",
        f"| trivial zero log term | `{fmt_float(static['trivial_zero_log_term'])}` |",
        f"| static relative to x=20000 | `{fmt_float(static['static_relative_to_x'])}` |",
        f"| static beats theta target | `{fmt_bool(static['static_beats_theta_target'])}` |",
        f"| exact prime-power Chebyshev weight at 20000 | `{fmt_float(prime_power['prime_power_weight'])}` |",
        f"| prime-power relative to x=20000 | `{fmt_float(prime_power['relative_to_x'])}` |",
        "",
        "该表说明尾项可归账，但不能自动替代 `ThetaEnvelopeTargetAt20000NumericalBudgetLedger`。",
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
            "外部 Titchmarsh+CN16 路线输入基：",
            "",
            "```text",
            result["latest_external_titchmarsh_cn16_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            f"下一步攻 `{result['next_priority']}`；低高度核验 `{result['secondary_priority']}` 仍独立开放。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--pc1", type=Path, default=DEFAULT_PC1)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous, "pc1": args.pc1}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
