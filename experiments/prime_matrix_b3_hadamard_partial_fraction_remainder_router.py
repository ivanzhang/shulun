#!/usr/bin/env python3
"""Prime Matrix B=3 Hadamard 部分分式余项账本路由器。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_partial_fraction_remainder_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-partial-fraction-remainder-router.json
  docs/monograph/prime-matrix-b3-hadamard-partial-fraction-remainder-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-explicit-clog-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-partial-fraction-remainder-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-partial-fraction-remainder-router.md"

OLD_ATOM = "HadamardPartialFractionRemainderNumericalLedger"
HADAMARD_FORMULA = "HadamardFactorizationLogDerivativeClosed"
COMPLETED_HADAMARD_PACKAGE = "CompletedZetaXiFunctionalEquationAndHadamardProductClosed"
ZERO_COUNT_EXTERNAL = "RVMToCN16LocalInequalityClosedWithRawArgCS8"
SYMMETRIC_PAIR_ATOM = "HadamardSymmetricZeroPairingAndOneOverRhoCancellationLedger"
SHELL_TAIL_ATOM = "HadamardDyadicZeroShellTailNumericalLedger"
LOCAL_CORE_ATOM = "HadamardLocalZeroCoreAbsorptionByCN16Ledger"
RANGE_ATOM = "HadamardRemainderRangeAndKernelConventionLedger"
CLOG_AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
OPT_ATOM = "ZeroRepulsionParameterNumericalOptimizationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_N = 16.0
PAIRING_CANDIDATE = 8.0
LOCAL_CORE_CANDIDATE = 32.0
SHELL_TAIL_CANDIDATE = 64.0
RANGE_CONVENTION_CANDIDATE = 8.0
TOTAL_CANDIDATE = PAIRING_CANDIDATE + LOCAL_CORE_CANDIDATE + SHELL_TAIL_CANDIDATE + RANGE_CONVENTION_CANDIDATE


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
    """写出 Hadamard 余项的最小数值替换包。"""
    return f"({SYMMETRIC_PAIR_ATOM} AND {SHELL_TAIL_ATOM} AND {LOCAL_CORE_ATOM} AND {RANGE_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧 Hadamard 余项原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def shell_budget_table() -> list[dict[str, float]]:
    """给 dyadic shell 尾项做数值压力审计。"""
    rows: list[dict[str, float]] = []
    cumulative = 0.0
    for j in range(8):
        width_weight = 2.0 ** (-j)
        # 这是候选核的审计，不是闭合证明；真正证明需固定 kernel convention。
        contribution = C_N * math.log(2.0) * width_weight
        cumulative += contribution
        rows.append(
            {
                "shell": float(j),
                "relative_kernel_weight": width_weight,
                "candidate_contribution": contribution,
                "cumulative": cumulative,
            }
        )
    return rows


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Hadamard 部分分式余项判定表。"""
    self_basis = previous.get("latest_self_contained_basis", "")
    external_basis = "\n".join(
        [
            previous.get("latest_conditional_basis", ""),
            previous.get("latest_global_with_external_basis", ""),
            json.dumps(previous.get("current_replacement_external", {}), ensure_ascii=False),
        ]
    )
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in previous.get(
        "current_replacement_external", {}
    ).get("ExplicitCLogHadamardStirlingJensenNumericalLedger", "")
    hadamard_available = HADAMARD_FORMULA in self_basis or COMPLETED_HADAMARD_PACKAGE in self_basis
    external_zero_count_available = ZERO_COUNT_EXTERNAL in external_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and guard and hadamard_available and external_zero_count_available
    return [
        row(
            "HadamardRemainderGateActive",
            active,
            False,
            "C_log 外部条件分支当前最窄点是 Hadamard 部分分式中的远零点和 1/rho 余项数值化。",
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
            "HadamardLogDerivativeFormulaAvailable",
            hadamard_available,
            True,
            "xi Hadamard 乘积和对数导数公式已在基础解析链中闭合，可给出零点部分分式。",
            f"{HADAMARD_FORMULA} OR {COMPLETED_HADAMARD_PACKAGE}",
        ),
        row(
            "ExternalCN16ZeroCountAvailable",
            external_zero_count_available,
            False,
            "接受外部 Backlund/低高度输入时，局部零点计数 C_N=16 可供 dyadic shell 预算使用。",
            ZERO_COUNT_EXTERNAL,
        ),
        row(
            "SymmetricPairingIdentityStillMissing",
            False,
            False,
            "还需固定 rho 与 1-rho、conjugate pairing 后 1/rho 常数项如何抵消或进入绝对预算。",
            SYMMETRIC_PAIR_ATOM,
        ),
        row(
            "DyadicShellTailNumericalLedgerMissing",
            False,
            False,
            "还需按 |Im rho-t| 的 dyadic shell 用 C_N=16 逐壳求和，给出可复算常数。",
            SHELL_TAIL_ATOM,
        ),
        row(
            "LocalCoreAbsorptionMissing",
            False,
            False,
            "还需处理 |Im rho-t|<=1 的局部核心，证明它已由 RVM-C_N=16 或主零点排斥项支付。",
            LOCAL_CORE_ATOM,
        ),
        row(
            "RangeAndKernelConventionMissing",
            False,
            False,
            "还需固定 sigma-1、t 低高度交界、kernel 归一化和 C_log 加法口径。",
            RANGE_ATOM,
        ),
        row(
            "HadamardRemainderReducedToFourMicroLedgers",
            reduced,
            False,
            "旧 Hadamard 余项原子已压成配对抵消、dyadic tail、局部核心、范围 convention 四个数值账本。",
            replacement_pair(),
        ),
        row(
            "CLogAggregationStillNext",
            False,
            False,
            "Hadamard 余项数值账本完成后，才可聚合总 C_log 并进入零点自由常数优化。",
            CLOG_AGGREGATION_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Hadamard 部分分式余项路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(
        bool(item["closed"]) for item in rows if item["gate"] == "HadamardRemainderReducedToFourMicroLedgers"
    )
    return {
        "certificate_type": "b3_hadamard_partial_fraction_remainder_router",
        "status": "hadamard_partial_fraction_remainder_reduced_to_four_micro_ledgers_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "hadamard_partial_fraction_remainder_reduced": reduced,
        "hadamard_partial_fraction_remainder_self_contained_proved": False,
        "hadamard_partial_fraction_remainder_external_proved": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": SHELL_TAIL_ATOM,
        "secondary_priority": SYMMETRIC_PAIR_ATOM,
        "tertiary_priority": LOCAL_CORE_ATOM,
        "quaternary_priority": RANGE_ATOM,
        "post_hadamard_priority": CLOG_AGGREGATION_ATOM,
        "post_clog_priority": OPT_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "candidate_budget_constants": {
            "C_N": C_N,
            "pairing_candidate": PAIRING_CANDIDATE,
            "local_core_candidate": LOCAL_CORE_CANDIDATE,
            "shell_tail_candidate": SHELL_TAIL_CANDIDATE,
            "range_convention_candidate": RANGE_CONVENTION_CANDIDATE,
            "total_candidate": TOTAL_CANDIDATE,
        },
        "shell_budget_table": shell_budget_table(),
        "plain_conclusion": (
            "Hadamard 部分分式余项不能直接从符号 Hadamard 公式升级为数值账本。"
            "在外部 C_N=16 局部零点计数可用时，它已被压成四个最小账本：零点对称配对/1rho 抵消、"
            "dyadic shell 尾项求和、局部核心吸收和范围/kernel convention。当前真正最窄点是 dyadic shell 尾项数值账本。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    constants = result["candidate_budget_constants"]
    lines = [
        "# Prime Matrix B=3 Hadamard 部分分式余项账本路由器",
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
            "hadamard_partial_fraction_remainder_reduced="
            f"{fmt_bool(result['hadamard_partial_fraction_remainder_reduced'])}"
        ),
        (
            "hadamard_partial_fraction_remainder_external_proved="
            f"{fmt_bool(result['hadamard_partial_fraction_remainder_external_proved'])}"
        ),
        (
            "hadamard_partial_fraction_remainder_self_contained_proved="
            f"{fmt_bool(result['hadamard_partial_fraction_remainder_self_contained_proved'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 数值替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 候选常数审计",
        "",
        "| item | value |",
        "| --- | ---: |",
    ]
    for key, value in constants.items():
        lines.append(f"| {key} | `{fmt_float(float(value))}` |")
    lines.extend(
        [
            "",
            "dyadic shell 压力样表：",
            "",
            "| shell | relative kernel weight | candidate contribution | cumulative |",
            "| ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["shell_budget_table"]:
        lines.append(
            "| {shell:.0f} | `{weight}` | `{contribution}` | `{cumulative}` |".format(
                shell=item["shell"],
                weight=fmt_float(item["relative_kernel_weight"]),
                contribution=fmt_float(item["candidate_contribution"]),
                cumulative=fmt_float(item["cumulative"]),
            )
        )
    lines.extend(
        [
            "",
            "这些常数只是账本压力审计；闭合还必须固定 kernel 口径并给出逐壳不等式。",
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
