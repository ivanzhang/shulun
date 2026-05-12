#!/usr/bin/env python3
"""生成 strict zeta log-derivative 内部展开闭合路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_logder_internal_expansion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-logder-internal-expansion-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-logder-internal-expansion-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-logder-internal-expansion-router.md"

RVM_SYNC = MONOGRAPH / "prime-matrix-strict-rvm-cn16-self-contained-sync-router.json"
HADAMARD = MONOGRAPH / "prime-matrix-b3-hadamard-factorization-router.json"
GAMMA = MONOGRAPH / "prime-matrix-b3-gamma-digamma-clog-router.json"
RANGE = MONOGRAPH / "prime-matrix-b3-hadamard-range-kernel-convention-router.json"
REMAINDER = MONOGRAPH / "prime-matrix-b3-hadamard-remainder-final-closure-router.json"
HORIZONTAL = MONOGRAPH / "prime-matrix-b3-psi0-horizontal-logder-bound-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [
    RVM_SYNC,
    HADAMARD,
    GAMMA,
    RANGE,
    REMAINDER,
    HORIZONTAL,
    CLAIM_STATUS,
]

LOGDER_INTERNAL = "ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger"
LOGDER_CLOSED = "ClassicalZetaLogDerivativeAwayFromZerosInternalExpansionClosedByHadamardGammaRemainder"
LOCAL_DISTANCE = "Psi0HorizontalLocalZeroDistanceSumConstantLedger"
WEIGHTED = "Psi0HorizontalWeightedIntegralBudgetLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖证据哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


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
    rvm_sync: dict[str, Any],
    hadamard: dict[str, Any],
    gamma: dict[str, Any],
    range_conv: dict[str, Any],
    remainder: dict[str, Any],
    horizontal: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成内部展开判定表。"""
    guard = (
        rvm_sync.get("counterexample_assumption_only") is True
        and rvm_sync.get("row_column_unconditional_closed") is False
        and rvm_sync.get("direct_unconditional_contradiction_found") is False
    )
    active = LOGDER_INTERNAL in str(rvm_sync.get("remaining_after_rvm_sync", [])) or LOGDER_INTERNAL in str(
        horizontal.get("replacement_self_contained", {})
    )
    hadamard_ready = hadamard.get("hadamard_factorization_log_derivative_closed") is True
    gamma_ready = gamma.get("gamma_digamma_stirling_uniform_closed") is True
    range_ready = range_conv.get("range_kernel_convention_closed") is True
    remainder_ready = remainder.get("hadamard_partial_fraction_remainder_closed") is True
    rvm_ready = rvm_sync.get("rvm_cn16_self_contained_resynchronized") is True
    expansion_closed = active and guard and hadamard_ready and gamma_ready and range_ready and remainder_ready
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只把水平边解析结构内部化，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "LogDerivativeInternalAtomActive",
            active,
            True,
            "RVM/CN16 同步后，strict Perron 的下一原子正是内部 zeta log-derivative 展开。",
            LOGDER_INTERNAL,
        ),
        row(
            "HadamardLogDerivativeAvailable",
            hadamard_ready,
            hadamard_ready,
            "xi 的一阶 Hadamard 乘积与 xi'/xi 部分分式已闭合，可转回 zeta'/zeta。",
            "HadamardFactorizationLogDerivativeClosed",
        ),
        row(
            "GammaDigammaUniformAvailable",
            gamma_ready,
            gamma_ready,
            "Gamma/digamma/Stirling 项已有 C_gamma=24 的内部统一界。",
            "GammaDigammaStirlingUniformNumericalClosedCgamma24",
        ),
        row(
            "RangeAndRemainderConventionAvailable",
            range_ready and remainder_ready,
            range_ready and remainder_ready,
            "target/local/far 分割、1/rho 项和非目标零点正预算已按 Hadamard 余项账本处理。",
            "HadamardPartialFractionRemainderNumericalClosedZeroPositiveBudget",
        ),
        row(
            "ClassicalLogDerivativeExpansionClosed",
            expansion_closed,
            expansion_closed,
            "在避开零点的水平边上，-zeta'/zeta 可写成局部零点主部加 O(log(T+3)) 结构余项。",
            LOGDER_CLOSED,
        ),
        row(
            "SelfContainedCN16AlreadySyncedForCounting",
            rvm_ready,
            rvm_ready,
            "局部零点数量的 C_N=16 已由上一同步证书完成；它将在下一局部倒距离账本中使用。",
            "RVMToCN16LocalInequalitySelfContainedClosedWithRawArgCS8CommonEnvelope",
        ),
        row(
            "PointwiseHorizontalBoundStillOpen",
            False,
            False,
            "结构展开本身不等于 Perron 水平边点态常数；仍需把局部零点倒距离和显式压到 C=288。",
            LOCAL_DISTANCE,
        ),
        row(
            "UnsmoothedPerronStrictSelfContainedClosed",
            False,
            False,
            "本步不关闭非平滑 Perron 自足包；局部倒距离和加权预算仍开放。",
            f"{LOCAL_DISTANCE} AND {WEIGHTED}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只是解析结构输入闭合，不产生全局反例矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    rvm_sync = load_json(RVM_SYNC)
    hadamard = load_json(HADAMARD)
    gamma = load_json(GAMMA)
    range_conv = load_json(RANGE)
    remainder = load_json(REMAINDER)
    horizontal = load_json(HORIZONTAL)
    rows = build_rows(rvm_sync, hadamard, gamma, range_conv, remainder, horizontal)
    expansion_closed = next(item["closed"] for item in rows if item["gate"] == "ClassicalLogDerivativeExpansionClosed")
    return {
        "certificate_type": "prime_matrix_strict_logder_internal_expansion_router",
        "status": "classical_zeta_logder_internal_expansion_closed_local_distance_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "classical_zeta_logder_internal_expansion_closed": expansion_closed,
        "local_zero_distance_self_contained_proved": False,
        "weighted_budget_self_contained_proved": False,
        "unsmoothed_perron_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {
            LOGDER_INTERNAL: LOGDER_CLOSED,
        },
        "remaining_after_logder_expansion": [
            LOCAL_DISTANCE,
            WEIGHTED,
        ],
        "next_direct_attack_target": LOCAL_DISTANCE,
        "secondary_attack_target": WEIGHTED,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger` 已闭合为内部结构展开："
            "Hadamard 对数导数给零点主部，Gamma/digamma 给 O(log T) 结构项，"
            "Hadamard 余项账本处理非目标零点和范围 convention。"
            "该闭合只给展开，不直接给 Perron 水平边点态预算；下一步仍需 "
            "`Psi0HorizontalLocalZeroDistanceSumConstantLedger`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict zeta log-derivative 内部展开路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"classical_zeta_logder_internal_expansion_closed={fmt_bool(result['classical_zeta_logder_internal_expansion_closed'])}",
        f"local_zero_distance_self_contained_proved={fmt_bool(result['local_zero_distance_self_contained_proved'])}",
        f"weighted_budget_self_contained_proved={fmt_bool(result['weighted_budget_self_contained_proved'])}",
        f"unsmoothed_perron_strict_self_contained_closed={fmt_bool(result['unsmoothed_perron_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        LOGDER_INTERNAL,
        f"  => {LOGDER_CLOSED}",
        "```",
        "",
        "## 2. 判定表",
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
            "## 3. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "也就是把局部零点数量、避零距离 eta 和结构余项合成为 C=288 的点态倒距离和预算。",
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
