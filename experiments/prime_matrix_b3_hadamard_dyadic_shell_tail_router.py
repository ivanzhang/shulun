#!/usr/bin/env python3
"""Prime Matrix B=3 Hadamard dyadic 零点壳尾项路由器。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_dyadic_shell_tail_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-dyadic-shell-tail-router.json
  docs/monograph/prime-matrix-b3-hadamard-dyadic-shell-tail-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-hadamard-partial-fraction-remainder-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-dyadic-shell-tail-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-dyadic-shell-tail-router.md"

OLD_ATOM = "HadamardDyadicZeroShellTailNumericalLedger"
CLOSED_SUM_ATOM = "HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel"
KERNEL_ATOM = "HadamardDVPQuadraticKernelEnvelopeLedger"
SHELL_COUNT_ATOM = "HadamardCN16UnitIntervalToDyadicShellCountClosed"
PAIRING_ATOM = "HadamardSymmetricZeroPairingAndOneOverRhoCancellationLedger"
LOCAL_CORE_ATOM = "HadamardLocalZeroCoreAbsorptionByCN16Ledger"
RANGE_ATOM = "HadamardRemainderRangeAndKernelConventionLedger"
CLOG_AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
ZERO_COUNT_EXTERNAL = "RVMToCN16LocalInequalityClosedWithRawArgCS8"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_N = 16.0
C_KERNEL = 2.0
C_LOG_SHIFT = 2.0
C_DYADIC_TARGET = 192.0
SHELLS_TO_AUDIT = 16


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


def replacement_pair() -> str:
    """写出 dyadic tail 的替换包。"""
    return f"({KERNEL_ATOM} AND {SHELL_COUNT_ATOM} AND {CLOSED_SUM_ATOM})"


def replace_atom(text: str) -> str:
    """替换 dyadic tail 原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def dyadic_sum_constant(shells: int = SHELLS_TO_AUDIT) -> tuple[list[dict[str, float]], float, float]:
    """计算抽象二次 kernel 下的 dyadic 求和常数。"""
    rows: list[dict[str, float]] = []
    cumulative = 0.0
    for j in range(shells):
        # 壳 [2^j,2^{j+1}] 的单位区间数为 O(2^j)，二次 kernel 给 O(2^{-2j})。
        shell_intervals = 2.0 ** j
        kernel_weight = C_KERNEL / (2.0 ** (2 * j))
        log_shift_weight = 1.0 + C_LOG_SHIFT * (j + 1.0) / (2.0 ** j)
        contribution = C_N * shell_intervals * kernel_weight * log_shift_weight
        cumulative += contribution
        rows.append(
            {
                "shell": float(j),
                "unit_intervals": shell_intervals,
                "kernel_weight": kernel_weight,
                "log_shift_weight": log_shift_weight,
                "contribution": contribution,
                "cumulative": cumulative,
            }
        )
    # 剩余尾部用 sum 2^{-j} 和 sum j2^{-j} 的粗上界。
    tail_bound = 8.0 * C_N * C_KERNEL / (2.0 ** shells)
    return rows, cumulative, cumulative + tail_bound


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], final_bound: float) -> list[dict[str, Any]]:
    """生成 dyadic shell tail 判定表。"""
    basis = "\n".join(
        [
            previous.get("latest_self_contained_basis", ""),
            previous.get("latest_conditional_basis", ""),
            previous.get("latest_global_with_external_basis", ""),
        ]
    )
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in previous.get(
        "replacement_self_contained", {}
    ).get("HadamardPartialFractionRemainderNumericalLedger", "")
    zero_count_available = ZERO_COUNT_EXTERNAL in basis or "ExternalCN16ZeroCountAvailable" in previous.get(
        "closed_gates", []
    )
    sum_passes = final_bound <= C_DYADIC_TARGET
    kernel_closed = KERNEL_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and guard and zero_count_available and sum_passes
    return [
        row(
            "DyadicShellTailGateActive",
            active,
            False,
            "上一层当前最窄点是 Hadamard 零点远壳尾项的 dyadic 数值账本。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "CN16UnitIntervalShellCountAvailable",
            zero_count_available,
            False,
            "外部 RVM-C_N=16 局部计数可逐单位区间累加成 dyadic shell 计数。",
            ZERO_COUNT_EXTERNAL,
        ),
        row(
            "DyadicSeriesSummationClosed",
            sum_passes,
            True,
            "一旦 kernel 在第 j 壳有二次衰减 O(2^{-2j})，单位区间数 O(2^j) 后的级数可进入 C=192 的保守尾项预算。",
            CLOSED_SUM_ATOM,
        ),
        row(
            "QuadraticKernelEnvelopeStillMissing",
            kernel_closed,
            False,
            "还需从 Hadamard/DVP 组合的精确 kernel 推出远壳二次衰减，并固定 sigma、主零点剥离和配对 convention。",
            KERNEL_ATOM,
        ),
        row(
            "DyadicShellTailReducedToKernelEnvelope",
            reduced,
            False,
            "dyadic 求和与 C_N=16 shell 计数已压实；剩余集中到 DVP-Hadamard kernel 二次包络。",
            replacement_pair(),
        ),
        row(
            "HadamardOtherMicroLedgersStillOpen",
            False,
            False,
            "之后仍需配对/1rho 抵消、局部核心吸收和范围 convention。",
            f"{PAIRING_ATOM} AND {LOCAL_CORE_ATOM} AND {RANGE_ATOM}",
        ),
        row(
            "CLogAggregationStillDownstream",
            False,
            False,
            "Hadamard 四账本全闭合后，才能进行 C_log 总常数聚合。",
            CLOG_AGGREGATION_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 dyadic shell tail 路由。"""
    previous = load_json(paths["previous"])
    shell_rows, partial_sum, final_bound = dyadic_sum_constant()
    rows = build_rows(previous, final_bound)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "DyadicShellTailReducedToKernelEnvelope")
    return {
        "certificate_type": "b3_hadamard_dyadic_shell_tail_router",
        "status": "hadamard_dyadic_shell_tail_reduced_to_kernel_envelope_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "dyadic_shell_tail_reduced": reduced,
        "dyadic_series_summation_closed": final_bound <= C_DYADIC_TARGET,
        "hadamard_dyadic_shell_tail_proved": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": KERNEL_ATOM,
        "secondary_priority": PAIRING_ATOM,
        "tertiary_priority": LOCAL_CORE_ATOM,
        "quaternary_priority": RANGE_ATOM,
        "post_hadamard_priority": CLOG_AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "constant_audit": {
            "C_N": C_N,
            "C_kernel": C_KERNEL,
            "C_log_shift": C_LOG_SHIFT,
            "target": C_DYADIC_TARGET,
            "partial_sum": partial_sum,
            "final_bound_with_tail": final_bound,
            "slack": C_DYADIC_TARGET - final_bound,
        },
        "shell_budget_table": shell_rows,
        "plain_conclusion": (
            "dyadic shell 求和本身已经闭合到 C=192：若 Hadamard/DVP kernel 在远壳具有二次衰减，"
            "C_N=16 的单位区间零点计数足以支付尾项。C=64 目标在当前粗 kernel 下不够；"
            "真正剩余是证明 DVP-Hadamard kernel envelope，并在后续 C_log 聚合中重新核算总常数。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    audit = result["constant_audit"]
    lines = [
        "# Prime Matrix B=3 Hadamard dyadic 零点壳尾项路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"dyadic_shell_tail_reduced={fmt_bool(result['dyadic_shell_tail_reduced'])}",
        f"dyadic_series_summation_closed={fmt_bool(result['dyadic_series_summation_closed'])}",
        f"hadamard_dyadic_shell_tail_proved={fmt_bool(result['hadamard_dyadic_shell_tail_proved'])}",
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
        "## 2. 常数审计",
        "",
        "| item | value |",
        "| --- | ---: |",
    ]
    for key, value in audit.items():
        lines.append(f"| {key} | `{fmt_float(float(value))}` |")
    lines.extend(
        [
            "",
            "| shell | intervals | kernel weight | log-shift | contribution | cumulative |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["shell_budget_table"]:
        lines.append(
            "| {shell:.0f} | `{intervals}` | `{kernel}` | `{shift}` | `{contribution}` | `{cumulative}` |".format(
                shell=item["shell"],
                intervals=fmt_float(item["unit_intervals"]),
                kernel=fmt_float(item["kernel_weight"]),
                shift=fmt_float(item["log_shift_weight"]),
                contribution=fmt_float(item["contribution"]),
                cumulative=fmt_float(item["cumulative"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
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
                f"当前最窄点为 `{result['next_priority']}`；随后是 "
                f"`{result['secondary_priority']}`、`{result['tertiary_priority']}`、"
                f"`{result['quaternary_priority']}`。"
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
