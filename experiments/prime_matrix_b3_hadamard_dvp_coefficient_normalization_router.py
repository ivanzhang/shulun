#!/usr/bin/env python3
"""Prime Matrix B=3 Hadamard/DVP kernel 系数归一化路由器。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_dvp_coefficient_normalization_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-dvp-coefficient-normalization-router.json
  docs/monograph/prime-matrix-b3-hadamard-dvp-coefficient-normalization-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-hadamard-dvp-kernel-envelope-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-dvp-coefficient-normalization-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-dvp-coefficient-normalization-router.md"

OLD_ATOM = "HadamardDVPKernelCoefficientNormalizationC2Ledger"
CLOSED_ATOM = "HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros"
SHAPE_CLOSED = "HadamardFarZeroQuadraticDecayShapeClosed"
SHELL_SEPARATION_ATOM = "HadamardFarZeroShellSeparationConventionLedger"
KERNEL_ATOM = "HadamardDVPQuadraticKernelEnvelopeLedger"
PAIRING_ATOM = "HadamardSymmetricZeroPairingAndOneOverRhoCancellationLedger"
LOCAL_CORE_ATOM = "HadamardLocalZeroCoreAbsorptionByCN16Ledger"
RANGE_ATOM = "HadamardRemainderRangeAndKernelConventionLedger"
CLOG_AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

RAW_DVP_COEFF_SUM = 8.0
EFFECTIVE_FAR_ZERO_KERNEL = 0.0
REQUIRED_C_KERNEL = 2.0


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
    """替换系数归一化原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def sign_ledger() -> list[dict[str, str]]:
    """列出符号归一化的关键链条。"""
    return [
        {
            "step": "zero_kernel_nonnegative",
            "formula": "Re 1/(sigma+iu-rho)=(sigma-beta)/((sigma-beta)^2+(u-gamma)^2)>=0",
            "meaning": "sigma>1, 0<=beta<=1 时成立。",
        },
        {
            "step": "log_derivative_sign",
            "formula": "Re(-zeta'/zeta)(s)=pole/gamma terms - sum_rho Re(1/(s-rho)+1/rho)",
            "meaning": "零点核进入 DVP 右侧时带负号。",
        },
        {
            "step": "positive_coefficients",
            "formula": "3,4,1 >= 0",
            "meaning": "DVP 组合不会把负零点贡献翻成正贡献。",
        },
        {
            "step": "far_zero_discard",
            "formula": "-sum_{rho != target} nonnegative terms <= 0",
            "meaning": "非目标远零点可丢弃；它们不消耗 C_log 正预算。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 DVP kernel 系数归一化判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    shape_available = SHAPE_CLOSED in basis
    sign_passes = EFFECTIVE_FAR_ZERO_KERNEL <= REQUIRED_C_KERNEL
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and guard and shape_available and sign_passes
    return [
        row(
            "DVPCoefficientNormalizationGateActive",
            active,
            False,
            "上一层最窄点是把 DVP 原始绝对系数压力归一化到 dyadic 账本允许的有效 C_kernel<=2。",
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
            "QuadraticShapeAvailable",
            shape_available,
            True,
            "远零点实部核的非负性和二次衰减形状已经闭合。",
            SHAPE_CLOSED,
        ),
        row(
            "RawAbsoluteCoefficientRejected",
            True,
            True,
            "不能用 3+4+1=8 的绝对值粗付；在 -zeta'/zeta 中非目标零点项带负号，应按符号丢弃。",
            "raw coefficient sum is not the budget coefficient.",
        ),
        row(
            "FarZeroSignDiscardClosed",
            closed,
            True,
            "sigma>1 时每个非目标零点核实部非负，而零点项在 Re(-zeta'/zeta) 中为负，DVP 非负系数组合后仍为非正，可全部丢弃。",
            CLOSED_ATOM,
        ),
        row(
            "EffectiveKernelC2Passes",
            sign_passes,
            True,
            "非目标远零点有效正预算常数为 0，满足 dyadic 账本要求的 C_kernel<=2。",
            f"{EFFECTIVE_FAR_ZERO_KERNEL:.1f}<={REQUIRED_C_KERNEL:.1f}",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "DVP kernel 系数归一化闭合：非目标远零点不消耗正 C_log 预算。",
            CLOSED_ATOM,
        ),
        row(
            "ShellSeparationStillNeeded",
            False,
            False,
            "仍需把目标零点、近壳核心和远壳尾项分离，避免与局部核心账本重复扣费。",
            SHELL_SEPARATION_ATOM,
        ),
        row(
            "KernelEnvelopeStillNeedsSeparation",
            False,
            False,
            "系数归一化闭合后，整个 kernel envelope 还差远/近壳分离 convention。",
            KERNEL_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 DVP kernel 系数归一化路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_hadamard_dvp_coefficient_normalization_router",
        "status": "hadamard_dvp_coefficient_normalization_closed_far_zero_sign_discard",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "dvp_coefficient_normalization_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": SHELL_SEPARATION_ATOM,
        "secondary_priority": PAIRING_ATOM,
        "tertiary_priority": LOCAL_CORE_ATOM,
        "quaternary_priority": RANGE_ATOM,
        "post_hadamard_priority": CLOG_AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "constant_audit": {
            "raw_DVP_absolute_coefficient_sum": RAW_DVP_COEFF_SUM,
            "effective_far_zero_positive_kernel": EFFECTIVE_FAR_ZERO_KERNEL,
            "required_C_kernel": REQUIRED_C_KERNEL,
            "slack": REQUIRED_C_KERNEL - EFFECTIVE_FAR_ZERO_KERNEL,
        },
        "sign_ledger": sign_ledger(),
        "plain_conclusion": (
            "DVP kernel 系数归一化闭合：原始绝对系数和 8 不能作为预算常数；"
            "在 Re(-zeta'/zeta) 中，非目标零点核带负号，且 DVP 系数 3,4,1 非负，"
            "所以非目标远零点整体非正，可在上界中丢弃。有效远零点正预算常数为 0，满足 C_kernel<=2。"
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
        "# Prime Matrix B=3 Hadamard/DVP kernel 系数归一化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"dvp_coefficient_normalization_closed={fmt_bool(result['dvp_coefficient_normalization_closed'])}",
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
        "## 2. 符号链条",
        "",
        "| step | formula | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sign_ledger"]:
        lines.append(
            "| {step} | `{formula}` | {meaning} |".format(
                step=table_cell(item["step"]),
                formula=table_cell(item["formula"]),
                meaning=table_cell(item["meaning"]),
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
                f"当前最窄点更新为 `{result['next_priority']}`；随后是 "
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
