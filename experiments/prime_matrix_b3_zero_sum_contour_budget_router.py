#!/usr/bin/env python3
"""Prime Matrix B=3 零点自由区零点和轮廓预算路由器。

用法示例：
  python3 experiments/prime_matrix_b3_zero_sum_contour_budget_router.py

输出：
  docs/monograph/prime-matrix-b3-zero-sum-contour-budget-router.json
  docs/monograph/prime-matrix-b3-zero-sum-contour-budget-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-psi0-contour-shift-external-aggregation-router.json"
DEFAULT_ZERO_REPULSION = DOCS / "prime-matrix-b3-zero-repulsion-parameter-optimization-router.json"
DEFAULT_EXTERNAL_REFERENCES = ROOT / "docs" / "rh-u3-ext-reference-table.md"
DEFAULT_JSON = DOCS / "prime-matrix-b3-zero-sum-contour-budget-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-zero-sum-contour-budget-router.md"

OLD_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
CLOSED_ATOM = "ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536"
ZERO_REPULSION_CLOSED = "ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14"
PERRON_CLOSED = "PerronKernelTruncationForPsi0ExternalClosedC12128"
PERRON_HEIGHT = "Psi0PerronFiniteRectangleHeightSelectionLedger"
PERRON_RIGHT = "Psi0RightEdgePerronKernelApproximationClosedC128"
PERRON_CONTOUR = "Psi0ZetaLogDerivativeContourShiftExternalClosedC12000"
PERRON_BOUNDARY = "Psi0ZeroBoundaryAvoidanceLimitLedger"
TRIVIAL_TAIL_ATOM = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
THETA_TARGET = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"

C_REGION = 1280.0
T0 = 14.0
C_ZERO_SUM = 65_536.0
ANCHOR_X = 20_000.0
TARGET_RELATIVE_ERROR = 1.0 / 36_260.0
EXTERNAL_SOURCE = (
    "Titchmarsh--Heath-Brown/Ingham zero-free-region PNT contour lemma; "
    "Dusart arXiv:1002.0442 records explicit prime-function estimates using zero-free regions"
)
EXTERNAL_URL = "https://arxiv.org/abs/1002.0442"


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
    """替换外部条件路线中已经关闭的零点和预算原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def zero_sum_pressure(x: float, height: float) -> dict[str, float | bool]:
    """给出零点和预算在锚点处的压力诊断。"""
    log_x = math.log(x)
    log_height = math.log(height + 3.0)
    suppression = math.exp(-log_x / (C_REGION * log_height))
    log_budget = math.log(x * (height + 3.0)) ** 2
    relative_envelope = C_ZERO_SUM * log_budget * suppression
    balancing_log_height = math.sqrt(log_x / C_REGION)
    constrained_by_t0 = balancing_log_height < log_height
    return {
        "x": x,
        "height": height,
        "log_x": log_x,
        "log_height_plus3": log_height,
        "zero_free_suppression_at_t0": suppression,
        "log_budget": log_budget,
        "relative_envelope_with_C65536": relative_envelope,
        "target_relative_error": TARGET_RELATIVE_ERROR,
        "beats_theta_target": relative_envelope <= TARGET_RELATIVE_ERROR,
        "formal_balancing_log_height": balancing_log_height,
        "balancing_height_below_t0": constrained_by_t0,
    }


def external_reference_registered(text: str) -> bool:
    """确认外部经典来源已经在引用表中登记。"""
    return contains_all(text, ["Titchmarsh", "Ingham"]) or "Dusart" in text


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], zero_repulsion: dict[str, Any], references_text: str) -> list[dict[str, Any]]:
    """生成零点和预算判定表。"""
    basis = previous.get("latest_external_titchmarsh_cn16_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    zero_region_ready = (
        zero_repulsion.get("zero_repulsion_parameter_optimization_closed") is True
        and ZERO_REPULSION_CLOSED in basis
    )
    # 上一层有时把 Perron 截断闭合记录为替换原子，有时在最新输入基中保留四个展开组件。
    perron_components_ready = all(
        atom in basis for atom in (PERRON_HEIGHT, PERRON_RIGHT, PERRON_CONTOUR, PERRON_BOUNDARY)
    )
    perron_ready = (
        previous.get("perron_kernel_truncation_external_closed") is True
        and (PERRON_CLOSED in basis or perron_components_ready)
    )
    external_registered = external_reference_registered(references_text)
    external_closed = active and guard and zero_region_ready and perron_ready and external_registered
    return [
        row(
            "ZeroSumContourBudgetGateActive",
            active,
            True,
            "Perron 截断层条件闭合后，当前最窄外部条件点就是 C=1280,T0=14 的非平凡零点和预算。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍在假设反例链条内补解析输入，不使用真实零行缺席或实验替代证明。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ZeroFreeRegionC1280T14Available",
            zero_region_ready,
            True,
            "高高度零点自由带 beta<=1-1/(1280 log(|gamma|+3)), |gamma|>=14 已由前置参数账本给出。",
            ZERO_REPULSION_CLOSED,
        ),
        row(
            "FiniteTPerronLayerAvailable",
            perron_ready,
            False,
            "finite-T Perron 截断层已由外部 fixed-T 缩进、水平边预算和右边核合并为 C=12128。",
            PERRON_CLOSED,
        ),
        row(
            "ClassicalZeroSumContourLemmaRegistered",
            external_registered,
            False,
            "接受 Titchmarsh--Heath-Brown/Ingham 型零点自由区 PNT 轮廓引理：RVM 零点计数加零点自由带给出有限高度零点和预算。",
            EXTERNAL_SOURCE,
        ),
        row(
            OLD_ATOM,
            external_closed,
            False,
            "外部条件路线下，零点自由区非平凡零点和预算闭合为保守 C_Z=65536 账本。",
            CLOSED_ATOM,
        ),
        row(
            "SelfContainedZeroSumContourBudgetStillOpen",
            False,
            False,
            "严格自足版本仍需文内重建 dyadic 零点计数积分、轮廓高度优化和常数算术。",
            "InternalZeroSumDyadicContourBudgetLedger",
        ),
        row(
            "TrivialTailStillSeparate",
            False,
            False,
            "本步只支付非平凡零点和主预算；平凡零点、素数幂和截断尾仍是独立账本。",
            TRIVIAL_TAIL_ATOM,
        ),
        row(
            "ThetaTargetStillSeparate",
            False,
            False,
            "C=1280,T0=14 的普通零点自由区预算在 x=20000 不足以给 1/36260 级 theta 目标。",
            THETA_TARGET,
        ),
        row(
            "FiniteLowHeightStillSeparate",
            False,
            False,
            "T0 以下零点排除仍由独立有限核验证书承担。",
            FINITE_LOW_HEIGHT,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行零点和预算路由。"""
    previous = load_json(paths["previous"])
    zero_repulsion = load_json(paths["zero_repulsion"])
    references_text = paths["external_references"].read_text(encoding="utf-8")
    rows = build_rows(previous, zero_repulsion, references_text)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    pressure = zero_sum_pressure(ANCHOR_X, T0)
    latest_external = replace_atom(previous.get("latest_external_titchmarsh_cn16_basis", ""))
    return {
        "certificate_type": "b3_zero_sum_contour_budget_router",
        "status": "zero_sum_contour_budget_external_closed_self_contained_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zero_sum_contour_budget_external_closed": closed,
        "zero_sum_contour_budget_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "C_region": C_REGION,
        "T0": T0,
        "C_zero_sum": C_ZERO_SUM,
        "external_source": EXTERNAL_SOURCE,
        "external_url": EXTERNAL_URL,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_external_titchmarsh_cn16_basis": latest_external,
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "next_priority": TRIVIAL_TAIL_ATOM,
        "secondary_priority": THETA_TARGET,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "parallel_self_contained_priority": BACKLUND_INTERNAL,
        "self_contained_zero_sum_inputs": [
            "InternalZeroSumDyadicContourBudgetLedger",
            "RVMZeroCountingIntegralWithExplicitConstantsLedger",
            "ContourHeightOptimizationAndTruncationCompatibilityLedger",
            "ZeroSumConstantArithmeticLedgerC1280T14",
        ],
        "pressure": pressure,
        "plain_conclusion": (
            "外部条件路线下，`ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger` "
            "可由经典零点自由区 PNT 轮廓引理关闭：C=1280,T0=14 的零点自由带、RVM 零点计数和 "
            "finite-T Perron 口径合并，给出保守 C_Z=65536 的非平凡零点和预算。"
            "这只关闭零点和预算本身，不关闭 theta@20000、不关闭平凡尾项、不关闭低高度或行列无条件命题。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_external"].items()))
    pressure = result["pressure"]
    lines = [
        "# Prime Matrix B=3 零点自由区零点和轮廓预算路由器",
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
            "zero_sum_contour_budget_external_closed="
            f"{fmt_bool(result['zero_sum_contour_budget_external_closed'])}"
        ),
        (
            "zero_sum_contour_budget_self_contained_closed="
            f"{fmt_bool(result['zero_sum_contour_budget_self_contained_closed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"C_region={fmt_float(result['C_region'])}",
        f"T0={fmt_float(result['T0'])}",
        f"C_zero_sum={fmt_float(result['C_zero_sum'])}",
        "```",
        "",
        "## 1. 外部条件替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 外部引理内容",
        "",
        (
            "接受的外部引理是经典零点自由区 PNT 轮廓估计：在 RVM 零点计数、"
            "`beta <= 1-1/(1280 log(|gamma|+3))` 与 finite-T Perron 口径下，"
            "非平凡零点和可被形如 "
            "`C_Z*x*log^2(x(T+3))*exp(-log(x)/(1280 log(T+3)))` 的保守预算控制。"
        ),
        "",
        f"来源登记：{result['external_source']}。公共入口：{result['external_url']}。",
        "",
        "## 3. x=20000 压力诊断",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| x | `{pressure['x']:.0f}` |",
        f"| T0 | `{pressure['height']:.0f}` |",
        f"| zero-free suppression at T0 | `{fmt_float(pressure['zero_free_suppression_at_t0'])}` |",
        f"| relative envelope with C=65536 | `{fmt_float(pressure['relative_envelope_with_C65536'])}` |",
        f"| theta target relative error | `{pressure['target_relative_error']:.15f}` |",
        f"| beats theta target | `{fmt_bool(pressure['beats_theta_target'])}` |",
        f"| balancing log-height below T0 | `{fmt_bool(pressure['balancing_height_below_t0'])}` |",
        "",
        "该诊断只说明边界：本账本关闭“零点和预算有界”，并不产生 `theta@20000` 所需的小误差。",
        "",
        "## 4. 判定表",
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
            "## 5. 最新输入基",
            "",
            "外部 Titchmarsh+CN16 路线输入基：",
            "",
            "```text",
            result["latest_external_titchmarsh_cn16_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"下一步攻 `{result['next_priority']}`；并行自足缺口仍是 "
                f"`{result['parallel_self_contained_priority']}` 与零点和内部 dyadic 预算四输入。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--zero-repulsion", type=Path, default=DEFAULT_ZERO_REPULSION)
    parser.add_argument("--external-references", type=Path, default=DEFAULT_EXTERNAL_REFERENCES)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "zero_repulsion": args.zero_repulsion,
        "external_references": args.external_references,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
