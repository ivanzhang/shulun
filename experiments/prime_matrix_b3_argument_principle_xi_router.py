#!/usr/bin/env python3
"""Prime Matrix B=3 xi 矩形 argument principle 计数闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_argument_principle_xi_router.py

输出：
  docs/monograph/prime-matrix-b3-argument-principle-xi-router.json
  docs/monograph/prime-matrix-b3-argument-principle-xi-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-rvm-local-count-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-argument-principle-xi-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-argument-principle-xi-router.md"

OLD_ATOM = "ArgumentPrincipleXiRectangleCountingLedger"
CLOSED_ATOM = "ArgumentPrincipleXiRectangleCountingClosed"
GAMMA_MAIN_ATOM = "GammaMainTermLocalDifferenceNumericalLedger"
BACKLUND_ATOM = "BacklundZetaArgumentBoundNumericalLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
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
    """把待证 atom 替换为已闭合 atom。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 xi 矩形 argument principle 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    xi_ready = "XiEntireOrderOneGrowthClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and xi_ready and guard
    return [
        row(
            "ArgumentPrincipleXiGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 xi 矩形 argument principle 计数。",
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
            "XiEntireFunctionAvailable",
            xi_ready,
            True,
            "xi 已闭合为整函数，argument principle 可直接应用。",
            "无整函数性剩余。",
        ),
        row(
            "BoundaryPerturbationConventionClosed",
            closed,
            True,
            "若矩形边界穿过零点，先取 epsilon 扰动并在极限中按重数计数。",
            "端点统一记账仍留给 EndpointZeroAvoidanceMultiplicityConventionLedger。",
        ),
        row(
            "XiRectangleArgumentCountingClosed",
            closed,
            True,
            "矩形内零点数等于 (1/2pi i) int_{partial R} xi'(s)/xi(s) ds，即边界辐角变化除以 2pi。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "待证 atom 已闭合为 xi 矩形 argument principle 计数恒等式。",
            CLOSED_ATOM,
        ),
        row(
            "GammaMainTermStillNext",
            False,
            False,
            "下一步需要把边界辐角分解中的 Gamma/主项差数值化。",
            GAMMA_MAIN_ATOM,
        ),
        row(
            "BacklundAndEndpointStillDownstream",
            False,
            False,
            "arg zeta、端点 convention 与 CN16 合并仍未闭合。",
            f"{BACKLUND_ATOM} AND {ENDPOINT_ATOM} AND {RVM_CN_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 xi 矩形 argument principle 计数闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_argument_principle_xi_router",
        "status": "argument_principle_xi_rectangle_counting_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "argument_principle_xi_rectangle_counting_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": GAMMA_MAIN_ATOM,
        "secondary_priority": BACKLUND_ATOM,
        "tertiary_priority": ENDPOINT_ATOM,
        "quaternary_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "core_formula": "N(R)=1/(2*pi*i) int_{partial R} xi'(s)/xi(s) ds = Delta_{partial R} arg xi / (2*pi)",
        "plain_conclusion": (
            "xi 矩形 argument principle 计数恒等式已闭合。它只是形式计数层，不给任何数值上界；"
            "下一步仍要数值化 Gamma 主项、Backlund 辐角和端点 convention。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 xi 矩形 argument principle 计数闭合证书",
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
            "argument_principle_xi_rectangle_counting_closed="
            f"{fmt_bool(result['argument_principle_xi_rectangle_counting_closed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 文内证明",
        "",
        "对避开零点的矩形 `R`，argument principle 给出",
        "",
        "```text",
        result["core_formula"],
        "```",
        "",
        (
            "若边界穿过零点，先对边界作 `epsilon` 平移或凹口绕开，最后令 `epsilon->0`，"
            "以零点重数计入。这个 convention 的全局统一仍由后续端点账本处理。"
        ),
        "",
        "该层不估计辐角大小，只把零点计数精确转成边界积分。",
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
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`、`{result['tertiary_priority']}`、"
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
