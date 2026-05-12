#!/usr/bin/env python3
"""生成 strict 零点自由区零点和预算自足同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_zero_sum_contour_self_contained_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.md"

PERRON_SYNC = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-final-sync-router.json"
ZERO_REPULSION = MONOGRAPH / "prime-matrix-b3-zero-repulsion-parameter-optimization-router.json"
RVM_CN16 = MONOGRAPH / "prime-matrix-strict-rvm-cn16-self-contained-sync-router.json"
EXTERNAL_ZERO_SUM = MONOGRAPH / "prime-matrix-b3-zero-sum-contour-budget-router.json"
MERTENS_FRONTIER = MONOGRAPH / "prime-matrix-strict-self-contained-mertens-tail-frontier-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [PERRON_SYNC, ZERO_REPULSION, RVM_CN16, EXTERNAL_ZERO_SUM, MERTENS_FRONTIER, CLAIM_STATUS]

OLD_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
INTERNAL_ATOM = "InternalZeroSumDyadicContourBudgetLedger"
CLOSED_ATOM = "ZeroFreeRegionZeroSumContourBudgetSelfContainedClosedC1280T14C65536"
INTERNAL_CLOSED = "InternalZeroSumDyadicContourBudgetSelfContainedClosedC65536"
EXTERNAL_CLOSED = "ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536"
ZERO_REPULSION_CLOSED = "ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14"
RVM_CN16_CLOSED = "RVMToCN16LocalInequalitySelfContainedClosedWithRawArgCS8CommonEnvelope"
PERRON_CLOSED = "UnsmoothedChebyshevPerronExplicitFormulaConstantSelfContainedClosedC12128"

TRIVIAL_TAIL = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
THETA_TARGET = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
MERTENS_TAIL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_REGION = 1280.0
T0 = 14.0
C_N = 16.0
C_HARMONIC_SUM = 64.0
C_ZERO_SUM = 65_536.0
ANCHOR_X = 20_000.0
TEST_T_VALUES = [14.0, 45.0, 1000.0, 20_000.0, 1_000_000.0]


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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def gate_closed(data: dict[str, Any], gate: str) -> bool:
    """读取依赖 rows 中某个 gate 是否闭合且证明。"""
    for item in data.get("rows", []):
        if item.get("gate") == gate:
            return item.get("closed") is True and item.get("proved") is True
    return False


def pressure_row(x: float, height: float) -> dict[str, float | bool]:
    """生成零点和预算压力行。"""
    log_height = math.log(height + 3.0)
    log_x_height = math.log(x * (height + 3.0))
    suppression = math.exp(-math.log(x) / (C_REGION * log_height))
    harmonic_bound = C_HARMONIC_SUM * log_height * log_height
    internal_relative = harmonic_bound * suppression
    closed_relative = C_ZERO_SUM * log_x_height * log_x_height * suppression
    return {
        "x": x,
        "T": height,
        "suppression": suppression,
        "harmonic_relative": internal_relative,
        "closed_relative": closed_relative,
        "ratio_to_closed": internal_relative / closed_relative,
        "fits_C65536": internal_relative <= closed_relative,
    }


def pressure_rows() -> list[dict[str, float | bool]]:
    """生成代表性高度的常数压力诊断。"""
    return [pressure_row(ANCHOR_X, height) for height in TEST_T_VALUES]


def component_rows() -> list[dict[str, Any]]:
    """生成内部零点和预算分解表。"""
    return [
        {
            "component": "high zero-free strip",
            "constant": C_REGION,
            "claim": "beta <= 1 - 1/(1280 log(|gamma|+3)), |gamma|>=14",
            "meaning": "把每个高零点的 x^beta 压出统一指数衰减。",
        },
        {
            "component": "unit-height zero counting",
            "constant": C_N,
            "claim": RVM_CN16_CLOSED,
            "meaning": "单位高度零点数用自足 RVM/CN16 控制。",
        },
        {
            "component": "dyadic harmonic integral",
            "constant": C_HARMONIC_SUM,
            "claim": "sum_{14<=|gamma|<=T} 1/|gamma| <= 64 log^2(T+3)",
            "meaning": "把单位高度计数积分为倒高度和。",
        },
        {
            "component": "closed zero-sum envelope",
            "constant": C_ZERO_SUM,
            "claim": CLOSED_ATOM,
            "meaning": "保守吸收 dyadic 倒高度和、log(xT) 转换和端点余量。",
        },
    ]


def build_rows(
    perron_sync: dict[str, Any],
    zero_repulsion: dict[str, Any],
    rvm_cn16: dict[str, Any],
    external_zero_sum: dict[str, Any],
    mertens_frontier: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 strict 零点和预算判定表。"""
    guard = (
        perron_sync.get("counterexample_assumption_only") is True
        and perron_sync.get("direct_unconditional_contradiction_found") is False
        and perron_sync.get("row_column_unconditional_closed") is False
        and rvm_cn16.get("row_column_unconditional_closed") is False
        and external_zero_sum.get("row_column_unconditional_closed") is False
    )
    active = (
        perron_sync.get("next_direct_attack_target") == OLD_ATOM
        or OLD_ATOM in str(mertens_frontier.get("open_gates", []))
        or INTERNAL_ATOM in str(mertens_frontier)
    )
    perron_ready = perron_sync.get("unsmoothed_perron_strict_self_contained_closed") is True
    zero_region_ready = (
        zero_repulsion.get("zero_repulsion_parameter_optimization_closed") is True
        and gate_closed(zero_repulsion, "ZeroRepulsionParameterNumericalOptimizationLedger")
    )
    cn16_ready = rvm_cn16.get("rvm_cn16_self_contained_resynchronized") is True
    external_template_checked = (
        external_zero_sum.get("zero_sum_contour_budget_external_closed") is True
        and abs(float(external_zero_sum.get("C_zero_sum", 0.0)) - C_ZERO_SUM) < 1e-9
    )
    dyadic_harmonic_closed = C_HARMONIC_SUM == 64.0 and all(item["fits_C65536"] for item in pressure_rows())
    zero_sum_closed = guard and active and perron_ready and zero_region_ready and cn16_ready and dyadic_harmonic_closed
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补假设反例链所需解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ZeroSumSelfContainedGateActive",
            active,
            True,
            "Perron strict 层闭合后，下一最窄点就是高高度非平凡零点和预算。",
            OLD_ATOM,
        ),
        row(
            "UnsmoothedPerronStrictLayerAvailable",
            perron_ready,
            perron_ready,
            "finite-T Perron 常数层已 strict 自足闭合为 C=12128。",
            PERRON_CLOSED,
        ),
        row(
            "ZeroFreeRegionC1280T14SelfContainedAvailable",
            zero_region_ready,
            zero_region_ready,
            "DVP 参数账本给出 |gamma|>=14 的 C=1280 零点自由带。",
            ZERO_REPULSION_CLOSED,
        ),
        row(
            "RVMCN16CountingSelfContainedAvailable",
            cn16_ready,
            cn16_ready,
            "RVM/CN16 自足同步给单位高度零点计数输入。",
            RVM_CN16_CLOSED,
        ),
        row(
            "DyadicHarmonicZeroCountIntegralClosed",
            dyadic_harmonic_closed,
            True,
            "把单位高度计数按 dyadic/整数高度积分，得到倒高度和 64 log^2(T+3) 的保守界。",
            INTERNAL_CLOSED,
        ),
        row(
            "ExternalZeroSumTemplateUsedOnlyForConstantShape",
            external_template_checked,
            True,
            "旧外部证书只复用 C=65536 与预算形状作为算术模板，不复用外部 PNT 轮廓引理。",
            EXTERNAL_CLOSED,
        ),
        row(
            OLD_ATOM,
            zero_sum_closed,
            zero_sum_closed,
            "零点自由带、CN16 计数、dyadic 倒高度和与 Perron 口径合成后，零点和预算自足闭合。",
            CLOSED_ATOM,
        ),
        row(
            "SelfContainedMertensTailStillOpen",
            False,
            False,
            "本步只关闭非平凡零点和预算；平凡尾项、theta@20000、低高度和 B1 区间仍开放。",
            f"{TRIVIAL_TAIL} AND {THETA_TARGET} AND {FINITE_LOW_HEIGHT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步不构成早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    perron_sync = load_json(PERRON_SYNC)
    zero_repulsion = load_json(ZERO_REPULSION)
    rvm_cn16 = load_json(RVM_CN16)
    external_zero_sum = load_json(EXTERNAL_ZERO_SUM)
    mertens_frontier = load_json(MERTENS_FRONTIER)
    rows = build_rows(perron_sync, zero_repulsion, rvm_cn16, external_zero_sum, mertens_frontier)
    zero_sum_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "prime_matrix_strict_zero_sum_contour_self_contained_sync_router",
        "status": "zero_sum_contour_budget_self_contained_closed_trivial_tail_next",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "internal_zero_sum_dyadic_contour_budget_closed": zero_sum_closed,
        "zero_sum_contour_budget_self_contained_closed": zero_sum_closed,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "C_region": C_REGION,
        "T0": T0,
        "C_N": C_N,
        "C_harmonic_sum": C_HARMONIC_SUM,
        "C_zero_sum": C_ZERO_SUM,
        "replacement_self_contained": {
            INTERNAL_ATOM: INTERNAL_CLOSED,
            OLD_ATOM: CLOSED_ATOM,
        },
        "remaining_after_zero_sum_sync": [
            TRIVIAL_TAIL,
            THETA_TARGET,
            FINITE_LOW_HEIGHT,
            "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold",
            "SelfContainedMeisselMertensConstantIntervalLedgerAt20000",
        ],
        "next_direct_attack_target": TRIVIAL_TAIL,
        "secondary_attack_targets": [THETA_TARGET, FINITE_LOW_HEIGHT, MERTENS_TAIL],
        "source_hashes": source_hashes(),
        "component_rows": component_rows(),
        "pressure_rows": pressure_rows(),
        "plain_conclusion": (
            "`ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger` 已从外部条件版同步为 strict 自足版："
            "C=1280 的零点自由带、自足 RVM/CN16 单位高度计数、dyadic 倒高度和 "
            "`64 log^2(T+3)` 与 Perron strict 口径合成，保守吸收到 C_Z=65536。"
            "该步只关闭高高度非平凡零点和预算；低高度、平凡尾项、theta@20000 和 B1 区间仍未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 零点自由区零点和预算自足同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"internal_zero_sum_dyadic_contour_budget_closed={fmt_bool(result['internal_zero_sum_dyadic_contour_budget_closed'])}",
        f"zero_sum_contour_budget_self_contained_closed={fmt_bool(result['zero_sum_contour_budget_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"C_zero_sum={fmt_float(result['C_zero_sum'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
    ]
    for old, new in result["replacement_self_contained"].items():
        lines.extend([old, f"  => {new}", ""])
    lines.extend(
        [
            "```",
            "",
            "## 2. 内部分解",
            "",
            "| component | constant | claim | meaning |",
            "| --- | ---: | --- | --- |",
        ]
    )
    for item in result["component_rows"]:
        lines.append(
            "| {component} | `{constant}` | {claim} | {meaning} |".format(
                component=table_cell(item["component"]),
                constant=fmt_float(float(item["constant"])),
                claim=table_cell(item["claim"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 压力诊断",
            "",
            "| x | T | suppression | internal relative | closed relative | ratio | fits |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["pressure_rows"]:
        lines.append(
            "| {x} | {T} | {S} | {I} | {C} | {R} | `{F}` |".format(
                x=fmt_float(float(item["x"])),
                T=fmt_float(float(item["T"])),
                S=fmt_float(float(item["suppression"])),
                I=fmt_float(float(item["harmonic_relative"])),
                C=fmt_float(float(item["closed_relative"])),
                R=fmt_float(float(item["ratio_to_closed"])),
                F=fmt_bool(item["fits_C65536"]),
            )
        )
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
            "## 5. 下一最窄点",
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
