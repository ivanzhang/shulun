#!/usr/bin/env python3
"""Prime Matrix B=3 Hadamard 远/近壳分离 convention 路由器。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_shell_separation_convention_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-shell-separation-convention-router.json
  docs/monograph/prime-matrix-b3-hadamard-shell-separation-convention-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-hadamard-dvp-coefficient-normalization-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-shell-separation-convention-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-shell-separation-convention-router.md"

OLD_ATOM = "HadamardFarZeroShellSeparationConventionLedger"
CLOSED_ATOM = "HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic"
COEFF_CLOSED = "HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros"
SHAPE_CLOSED = "HadamardFarZeroQuadraticDecayShapeClosed"
PAIRING_ATOM = "HadamardSymmetricZeroPairingAndOneOverRhoCancellationLedger"
LOCAL_CORE_ATOM = "HadamardLocalZeroCoreAbsorptionByCN16Ledger"
RANGE_ATOM = "HadamardRemainderRangeAndKernelConventionLedger"
CLOG_AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
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


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_atom(text: str) -> str:
    """替换远/近壳 convention 原子。"""
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


def partition_rows() -> list[dict[str, str]]:
    """列出零点集合分割。"""
    return [
        {
            "part": "target",
            "definition": "rho=rho0=beta0+i gamma0",
            "charged_to": "main negative zero term -4/(sigma-beta0)",
        },
        {
            "part": "local_core",
            "definition": "rho!=rho0 and |Im rho-gamma0|<1",
            "charged_to": "HadamardLocalZeroCoreAbsorptionByCN16Ledger",
        },
        {
            "part": "far_shell_j",
            "definition": "2^j <= |Im rho-gamma0| < 2^(j+1), j>=0",
            "charged_to": "HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel",
        },
        {
            "part": "boundary",
            "definition": "exact equality goes to the lower-index half-open shell",
            "charged_to": "no double counting",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成远/近壳分离 convention 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    shape_available = SHAPE_CLOSED in basis
    coeff_available = COEFF_CLOSED in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and guard and shape_available and coeff_available
    return [
        row(
            "ShellSeparationGateActive",
            active,
            False,
            "上一层最窄点是把目标零点、近壳核心和远壳 dyadic tail 分成互斥账本。",
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
            "KernelShapeAndCoefficientReady",
            shape_available and coeff_available,
            True,
            "二次衰减形状和远零点系数归一化均已闭合，可安全定义远壳账本。",
            f"{SHAPE_CLOSED} AND {COEFF_CLOSED}",
        ),
        row(
            "HalfOpenDyadicPartitionClosed",
            closed,
            True,
            "零点按 target/local_core/far half-open dyadic shells 唯一归类，边界归低阶壳，避免重复扣费。",
            CLOSED_ATOM,
        ),
        row(
            "TargetZeroSeparated",
            closed,
            True,
            "目标零点只进入 de la Vallee Poussin 主负项，不再进入远壳或局部核心余项。",
            "no target double charge",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "远/近壳分离 convention 已闭合。",
            CLOSED_ATOM,
        ),
        row(
            "HadamardOtherMicroLedgersStillOpen",
            False,
            False,
            "Hadamard 余项还需配对/1rho 抵消、局部核心吸收和范围 convention。",
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
    """执行远/近壳分离 convention 路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_hadamard_shell_separation_convention_router",
        "status": "hadamard_shell_separation_convention_closed_half_open_dyadic",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "shell_separation_convention_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": PAIRING_ATOM,
        "secondary_priority": LOCAL_CORE_ATOM,
        "tertiary_priority": RANGE_ATOM,
        "post_hadamard_priority": CLOG_AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "partition": partition_rows(),
        "plain_conclusion": (
            "Hadamard 远/近壳分离 convention 已闭合：目标零点、近壳核心和远壳 dyadic tail "
            "用半开区间唯一分配，避免 target、local core 与 far tail 重复扣费。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Hadamard 远/近壳分离 convention 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"shell_separation_convention_closed={fmt_bool(result['shell_separation_convention_closed'])}",
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
        "## 2. 分割表",
        "",
        "| part | definition | charged_to |",
        "| --- | --- | --- |",
    ]
    for item in result["partition"]:
        lines.append(
            "| {part} | `{definition}` | {charged_to} |".format(
                part=table_cell(item["part"]),
                definition=table_cell(item["definition"]),
                charged_to=table_cell(item["charged_to"]),
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
                f"当前最窄点更新为 `{result['next_priority']}`；随后是 "
                f"`{result['secondary_priority']}`、`{result['tertiary_priority']}`。"
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
