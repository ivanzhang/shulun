#!/usr/bin/env python3
"""Prime Matrix B=3 Hadamard/DVP kernel 二次包络路由器。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_dvp_kernel_envelope_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-dvp-kernel-envelope-router.json
  docs/monograph/prime-matrix-b3-hadamard-dvp-kernel-envelope-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-hadamard-dyadic-shell-tail-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-dvp-kernel-envelope-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-dvp-kernel-envelope-router.md"

OLD_ATOM = "HadamardDVPQuadraticKernelEnvelopeLedger"
SHAPE_CLOSED = "HadamardFarZeroQuadraticDecayShapeClosed"
COEFF_ATOM = "HadamardDVPKernelCoefficientNormalizationC2Ledger"
SHELL_SEPARATION_ATOM = "HadamardFarZeroShellSeparationConventionLedger"
PAIRING_ATOM = "HadamardSymmetricZeroPairingAndOneOverRhoCancellationLedger"
LOCAL_CORE_ATOM = "HadamardLocalZeroCoreAbsorptionByCN16Ledger"
RANGE_ATOM = "HadamardRemainderRangeAndKernelConventionLedger"
CLOG_AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

REQUIRED_C_KERNEL = 2.0
RAW_DVP_COEFF_SUM = 8.0


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
    """写出 kernel 包络的替换包。"""
    return f"({SHAPE_CLOSED} AND {COEFF_ATOM} AND {SHELL_SEPARATION_ATOM})"


def replace_atom(text: str) -> str:
    """替换 kernel 包络原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def inequality_audit() -> list[dict[str, str]]:
    """列出二次衰减形状证明的关键不等式。"""
    return [
        {
            "claim": "far_zero_real_part",
            "formula": "Re 1/(sigma+it-rho)=(sigma-beta)/((sigma-beta)^2+(t-gamma)^2)",
            "status": "closed for |t-gamma|>=1 and 0<=beta<=1, 1<sigma<=2",
        },
        {
            "claim": "quadratic_bound_shape",
            "formula": "0 <= Re 1/(sigma+it-rho) <= 2/(t-gamma)^2",
            "status": "shape closed before DVP coefficient normalization",
        },
        {
            "claim": "coefficient_pressure",
            "formula": "raw DVP coefficient sum 3+4+1=8, required effective kernel constant <=2",
            "status": "not closed without cancellation/sign discipline",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Hadamard/DVP kernel 包络判定表。"""
    basis = "\n".join(
        [
            previous.get("latest_self_contained_basis", ""),
            previous.get("latest_conditional_basis", ""),
            previous.get("latest_global_with_external_basis", ""),
        ]
    )
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    shape_closed = True
    coefficient_closed = COEFF_ATOM in basis
    shell_separation_closed = SHELL_SEPARATION_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and guard and shape_closed
    fully_closed = reduced and coefficient_closed and shell_separation_closed
    return [
        row(
            "DVPKernelEnvelopeGateActive",
            active,
            False,
            "上一层剩余集中到 Hadamard/DVP 组合的远零点 kernel 包络。",
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
            "FarZeroQuadraticDecayShapeClosed",
            shape_closed,
            True,
            "对 |t-gamma|>=1，strip 内零点给 Re 1/(sigma+it-rho)<=2/(t-gamma)^2。",
            SHAPE_CLOSED,
        ),
        row(
            "DVPCoefficientNormalizationStillMissing",
            coefficient_closed,
            False,
            "dyadic C=192 账本使用有效 C_kernel=2；但 DVP 原始权重 3,4,1 的绝对和为 8，必须证明符号/配对后有效常数降到 2 或重算预算。",
            COEFF_ATOM,
        ),
        row(
            "FarShellSeparationConventionStillMissing",
            shell_separation_closed,
            False,
            "还需固定 |t-gamma|<1 的局部核心剥离、远壳起点和 sigma 范围，使二次包络不与局部核心重复扣费。",
            SHELL_SEPARATION_ATOM,
        ),
        row(
            "DVPKernelEnvelopeReduced",
            reduced,
            False,
            "kernel 包络已分解：二次衰减形状闭合；剩余为 DVP 系数归一化和远/近壳分离 convention。",
            replacement_pair(),
        ),
        row(
            OLD_ATOM,
            fully_closed,
            False,
            "只有系数归一化与远壳分离同时完成时，才能把 kernel 包络接回 dyadic tail。",
            replacement_pair(),
        ),
        row(
            "HadamardOtherMicroLedgersStillOpen",
            False,
            False,
            "kernel 包络后仍需配对/1rho 抵消、局部核心吸收和范围 convention。",
            f"{PAIRING_ATOM} AND {LOCAL_CORE_ATOM} AND {RANGE_ATOM}",
        ),
        row(
            "CLogAggregationStillDownstream",
            False,
            False,
            "Hadamard 四账本全闭合后，才能进入 C_log 总常数聚合。",
            CLOG_AGGREGATION_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Hadamard/DVP kernel 包络路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "DVPKernelEnvelopeReduced")
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_hadamard_dvp_kernel_envelope_router",
        "status": "hadamard_dvp_kernel_shape_closed_coefficient_normalization_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "dvp_kernel_envelope_reduced": reduced,
        "dvp_kernel_shape_closed": True,
        "dvp_kernel_envelope_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": COEFF_ATOM,
        "secondary_priority": SHELL_SEPARATION_ATOM,
        "tertiary_priority": PAIRING_ATOM,
        "quaternary_priority": LOCAL_CORE_ATOM,
        "post_hadamard_priority": CLOG_AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "constant_audit": {
            "required_C_kernel_from_dyadic_budget": REQUIRED_C_KERNEL,
            "raw_DVP_absolute_coefficient_sum": RAW_DVP_COEFF_SUM,
            "coefficient_gap": RAW_DVP_COEFF_SUM - REQUIRED_C_KERNEL,
        },
        "inequality_audit": inequality_audit(),
        "plain_conclusion": (
            "Hadamard/DVP kernel 的二次衰减形状已经闭合，但这还不足以接回 dyadic C=192 预算。"
            "关键剩余是系数归一化：DVP 原始绝对系数和为 8，而前一账本使用的有效 kernel 常数为 2。"
            "必须证明符号/配对/主项剥离把有效常数降到 2，或返回上游重算更大的 C_log。"
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
        "# Prime Matrix B=3 Hadamard/DVP kernel 二次包络路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"dvp_kernel_envelope_reduced={fmt_bool(result['dvp_kernel_envelope_reduced'])}",
        f"dvp_kernel_shape_closed={fmt_bool(result['dvp_kernel_shape_closed'])}",
        f"dvp_kernel_envelope_closed={fmt_bool(result['dvp_kernel_envelope_closed'])}",
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
        "## 2. 不等式审计",
        "",
        "| claim | formula | status |",
        "| --- | --- | --- |",
    ]
    for item in result["inequality_audit"]:
        lines.append(
            "| {claim} | `{formula}` | {status} |".format(
                claim=table_cell(item["claim"]),
                formula=table_cell(item["formula"]),
                status=table_cell(item["status"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 常数压力",
            "",
            "| item | value |",
            "| --- | ---: |",
        ]
    )
    for key, value in audit.items():
        lines.append(f"| {key} | `{fmt_float(float(value))}` |")
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
                f"当前最窄点为 `{result['next_priority']}`；若不能证明有效 C_kernel<=2，"
                "必须回到 C_log 聚合账本重算更大的常数。"
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
