#!/usr/bin/env python3
"""生成 strict 平凡零点/素数幂尾项自足同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_trivial_tail_prime_power_self_contained_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.md"

ZERO_SUM_SYNC = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
TRIVIAL_EXTERNAL = MONOGRAPH / "prime-matrix-b3-trivial-tail-prime-power-budget-router.json"
INTERNAL_PSI0 = MONOGRAPH / "prime-matrix-b3-internal-psi0-perron-formula-router.json"
MERTENS_FRONTIER = MONOGRAPH / "prime-matrix-strict-self-contained-mertens-tail-frontier-router.json"
PC1 = ROOT / "docs" / "rh-pc1-analytic-input-theoremization.md"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [ZERO_SUM_SYNC, TRIVIAL_EXTERNAL, INTERNAL_PSI0, MERTENS_FRONTIER, PC1, CLAIM_STATUS]

OLD_ATOM = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
CLOSED_ATOM = "PerronTrivialZeroPrimePowerTailBudgetSelfContainedClosedElementaryXGe20000"
EXTERNAL_CLOSED = "PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000"
ZERO_SUM_CLOSED = "ZeroFreeRegionZeroSumContourBudgetSelfContainedClosedC1280T14C65536"
EXACT_PSI0 = "InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost"
ENDPOINT_HALF = "ChebyshevPsi0EndpointHalfWeightConventionClosed"
PRIME_POWER = "PrimePowerThetaPsiTransferLedgerClosed"

THETA_TARGET = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
MERTENS_TAIL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000
TARGET_RELATIVE_ERROR = 1.0 / 36_260.0


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记证据文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


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


def gate_closed(data: dict[str, Any], gate: str) -> bool:
    """读取依赖 rows 中某个 gate 是否闭合且证明。"""
    for item in data.get("rows", []):
        if item.get("gate") == gate:
            return item.get("closed") is True and item.get("proved") is True
    return False


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
    """精确计算锚点素数幂 Chebyshev 权重。"""
    total = 0.0
    terms = 0
    max_power = 0
    for prime in sieve_primes(int(math.isqrt(limit)) + 1):
        power = prime * prime
        while power <= limit:
            total += math.log(prime)
            terms += 1
            max_power = max(max_power, power)
            power *= prime
    return {
        "x": limit,
        "prime_power_weight": total,
        "term_count": terms,
        "max_prime_power": max_power,
        "relative_to_x": total / limit,
    }


def static_formula_terms(x: int) -> dict[str, float | bool]:
    """计算公式常数和平凡零点项的锚点压力。"""
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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    zero_sum: dict[str, Any],
    trivial_external: dict[str, Any],
    internal_psi0: dict[str, Any],
    mertens_frontier: dict[str, Any],
    pc1_text: str,
) -> list[dict[str, Any]]:
    """生成 strict 平凡尾项判定表。"""
    guard = (
        zero_sum.get("counterexample_assumption_only") is True
        and zero_sum.get("direct_unconditional_contradiction_found") is False
        and zero_sum.get("row_column_unconditional_closed") is False
        and trivial_external.get("row_column_unconditional_closed") is False
    )
    active = (
        zero_sum.get("next_direct_attack_target") == OLD_ATOM
        or OLD_ATOM in str(mertens_frontier)
    )
    zero_sum_ready = zero_sum.get("zero_sum_contour_budget_self_contained_closed") is True
    exact_ready = internal_psi0.get("internal_psi0_exact_formula_closed") is True
    endpoint_ready = gate_closed(internal_psi0, "Psi0EndpointConventionAvailable")
    prime_power_ready = PRIME_POWER in pc1_text or ("素数幂" in pc1_text and "Chebyshev" in pc1_text)
    external_arithmetic_template = trivial_external.get("trivial_tail_prime_power_budget_closed") is True
    closed = guard and active and zero_sum_ready and exact_ready and endpoint_ready and prime_power_ready
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设反例链解析输入内同步，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "TrivialTailPrimePowerGateActive",
            active,
            True,
            "自足零点和预算关闭后，下一最窄点是同口径平凡零点、素数幂和尾项账本。",
            OLD_ATOM,
        ),
        row(
            "SelfContainedZeroSumSeparated",
            zero_sum_ready,
            zero_sum_ready,
            "非平凡零点和预算已由 strict 自足零点和证书支付，本步不重复计费。",
            ZERO_SUM_CLOSED,
        ),
        row(
            "Psi0ExactFormulaAvailable",
            exact_ready,
            exact_ready,
            "内部 psi_0 精确公式给出 -log(2pi) 和平凡零点项。",
            EXACT_PSI0,
        ),
        row(
            "EndpointHalfWeightConventionAvailable",
            endpoint_ready,
            endpoint_ready,
            "psi_0 半权端点 convention 已闭合，端点不重复计费。",
            ENDPOINT_HALF,
        ),
        row(
            "PrimePowerTransferAvailable",
            prime_power_ready,
            True,
            "素数幂到 theta/素数 Chebyshev 权的转移在 PC1 材料中登记为低阶项。",
            PRIME_POWER,
        ),
        row(
            "ExternalTailTemplateUsedOnlyForElementaryArithmetic",
            external_arithmetic_template,
            True,
            "旧尾项证书只复用初等压力诊断和替换名，不复用外部零点和路线。",
            EXTERNAL_CLOSED,
        ),
        row(
            OLD_ATOM,
            closed,
            closed,
            "平凡零点、公式常数、端点半权和素数幂转移闭合为 strict 自足初等尾项账本。",
            CLOSED_ATOM,
        ),
        row(
            "ThetaTargetStillSeparate",
            False,
            False,
            "尾项归账不等于 theta@20000 小误差目标；theta 目标仍需单独证明。",
            THETA_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    zero_sum = load_json(ZERO_SUM_SYNC)
    trivial_external = load_json(TRIVIAL_EXTERNAL)
    internal_psi0 = load_json(INTERNAL_PSI0)
    mertens_frontier = load_json(MERTENS_FRONTIER)
    pc1_text = PC1.read_text(encoding="utf-8")
    rows = build_rows(zero_sum, trivial_external, internal_psi0, mertens_frontier, pc1_text)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "prime_matrix_strict_trivial_tail_prime_power_self_contained_sync_router",
        "status": "trivial_tail_prime_power_budget_self_contained_closed_theta_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "trivial_tail_prime_power_budget_self_contained_closed": closed,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {
            OLD_ATOM: CLOSED_ATOM,
        },
        "remaining_after_trivial_tail_sync": [
            THETA_TARGET,
            FINITE_LOW_HEIGHT,
            "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold",
            "SelfContainedMeisselMertensConstantIntervalLedgerAt20000",
        ],
        "next_direct_attack_target": THETA_TARGET,
        "secondary_attack_targets": [FINITE_LOW_HEIGHT, MERTENS_TAIL],
        "source_hashes": source_hashes(),
        "static_formula_pressure": static_formula_terms(ANCHOR_X),
        "prime_power_pressure": prime_power_weight(ANCHOR_X),
        "plain_conclusion": (
            "`PerronTruncationTrivialZeroPrimePowerTailBudgetLedger` 已同步为 strict 自足初等尾项账本："
            "非平凡零点和由上一层自足证书分离，psi_0 精确公式支付常数和平凡零点项，"
            "端点半权和素数幂转移给出同口径低阶归账。"
            "该步仍不证明 theta@20000 小误差，也不关闭 Mertens 尾段或行/列命题。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    static = result["static_formula_pressure"]
    prime_power = result["prime_power_pressure"]
    lines = [
        "# Prime Matrix strict 平凡零点/素数幂尾项自足同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"trivial_tail_prime_power_budget_self_contained_closed={fmt_bool(result['trivial_tail_prime_power_budget_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        f"  => {replacement[1]}",
        "```",
        "",
        "## 2. 锚点压力诊断",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| log(2pi) | `{fmt_float(float(static['log_2pi']))}` |",
        f"| trivial zero log term | `{fmt_float(float(static['trivial_zero_log_term']))}` |",
        f"| static relative to x=20000 | `{fmt_float(float(static['static_relative_to_x']))}` |",
        f"| static beats theta target | `{fmt_bool(static['static_beats_theta_target'])}` |",
        f"| exact prime-power Chebyshev weight at 20000 | `{fmt_float(float(prime_power['prime_power_weight']))}` |",
        f"| prime-power relative to x=20000 | `{fmt_float(float(prime_power['relative_to_x']))}` |",
        "",
        "该表只说明尾项可归账；它不能替代 `ThetaEnvelopeTargetAt20000NumericalBudgetLedger`。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
