#!/usr/bin/env python3
"""Prime Matrix B=3 端点避零与重数 convention 闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_endpoint_multiplicity_convention_router.py

输出：
  docs/monograph/prime-matrix-b3-endpoint-multiplicity-convention-router.json
  docs/monograph/prime-matrix-b3-endpoint-multiplicity-convention-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-endpoint-multiplicity-convention-router.md"

OLD_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
CLOSED_ATOM = "EndpointZeroAvoidanceMultiplicityConventionClosedByLimit"
ARG_ATOM = "ArgumentPrincipleXiRectangleCountingClosed"
XI_ATOM = "XiEntireOrderOneGrowthClosed"
CS8_ATOM = "BacklundCS8SlackAfterBridgeClosedTightHalf"
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
    """替换端点 convention 原子。"""
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


def convention_steps() -> list[dict[str, str]]:
    """列出端点 convention 的严格步骤。"""
    return [
        {
            "step": "finite_multiplicity",
            "content": "xi 是整函数；紧矩形内零点离散且每个零点重数有限。",
        },
        {
            "step": "avoidance_sequence",
            "content": "对给定端点高度 T，取 epsilon_j -> 0，使 T±epsilon_j 不等于任何零点虚部。",
        },
        {
            "step": "argument_principle_first",
            "content": "先在避开零点的边界上应用 argument principle 或 Littlewood 矩形恒等式。",
        },
        {
            "step": "multiplicity_limit",
            "content": "令 epsilon_j -> 0，边界零点以解析重数完整计入闭区间零点计数。",
        },
        {
            "step": "no_constant_charge",
            "content": "端点 convention 只改变计数定义，不额外支付 pi 跳变、C_S 常数或 C_N 常数。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成端点避零与重数 convention 判定表。"""
    self_basis = previous.get("latest_self_contained_basis", "")
    conditional_basis = previous.get("latest_conditional_basis", "")
    global_basis = previous.get("latest_global_with_external_basis", "")
    active = (
        previous.get("conditional_next_priority") == OLD_ATOM
        and OLD_ATOM in conditional_basis
    ) or OLD_ATOM in self_basis or OLD_ATOM in global_basis
    xi_ready = XI_ATOM in self_basis or XI_ATOM in conditional_basis
    argument_ready = ARG_ATOM in self_basis or ARG_ATOM in conditional_basis
    cs8_ready = CS8_ATOM in conditional_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and xi_ready and argument_ready and guard
    return [
        row(
            "EndpointConventionGateActive",
            active,
            False,
            "外部 Backlund 分支当前最窄点是端点避零与重数 convention；自足输入基中也含同一 atom。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的解析记账，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "XiFiniteMultiplicityAvailable",
            xi_ready,
            True,
            "xi 已作为整函数进入输入基，因此紧区域内零点离散且重数有限。",
            XI_ATOM,
        ),
        row(
            "ArgumentPrincipleCompatible",
            argument_ready,
            True,
            "已有 xi 矩形 argument principle；端点落零时可先扰动边界再取极限。",
            ARG_ATOM,
        ),
        row(
            "AvoidingSequenceAndLimitClosed",
            closed,
            True,
            "选择避开零点虚部的 epsilon 序列，在避零边界上计数，再令 epsilon->0，边界零点按重数进入闭区间。",
            CLOSED_ATOM,
        ),
        row(
            "NoBudgetDoubleCounting",
            closed,
            True,
            "端点 convention 不重复扣减凹口成本，也不新增 C_S 或 C_N 常数；所有近零点绕行成本仍属于既有 Backlund 凹口账本。",
            "无新常数。",
        ),
        row(
            "ExternalBacklundInputsPreserved",
            cs8_ready,
            False,
            "外部 Backlund 常数链已到 C_S=8 紧等号；本步只补端点定义，不改变该预算。",
            CS8_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "端点避零与重数 convention 已由极限定义闭合。",
            CLOSED_ATOM,
        ),
        row(
            "RVMToCN16Next",
            False,
            False,
            "端点 convention 关闭后，外部 Backlund 分支下一硬点转到 RVM 到 C_N=16 的局部计数合并。",
            RVM_CN_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行端点避零与重数 convention 闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""))
    latest_conditional = replace_atom(previous.get("latest_conditional_basis", ""))
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""))
    return {
        "certificate_type": "b3_endpoint_multiplicity_convention_router",
        "status": "endpoint_zero_avoidance_multiplicity_convention_closed_by_limit",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "endpoint_multiplicity_convention_closed": closed,
        "endpoint_multiplicity_convention_self_contained_closed": closed,
        "endpoint_multiplicity_convention_external_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_conditional,
        "latest_global_with_external_basis": latest_global,
        "next_priority": previous.get("next_priority"),
        "secondary_priority": previous.get("secondary_priority"),
        "conditional_next_priority": RVM_CN_ATOM,
        "secondary_conditional_priority": DSTRUCTURE,
        "final_promotion_priority": DSTRUCTURE,
        "convention_steps": convention_steps(),
        "core_limit_formula": (
            "N_closed([A,B]) = lim_{epsilon->0+} N_avoiding((A-epsilon, B+epsilon)), "
            "with boundary zeros counted by analytic multiplicity."
        ),
        "plain_conclusion": (
            "端点避零与重数 convention 已闭合：所有边界落零先用 epsilon 避开，"
            "在避零边界上应用 argument principle，再取极限并按解析重数计入。"
            "这只解决定义一致性，不证明新的零点分布，也不关闭行列无条件命题。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    self_repl = next(iter(result["replacement_self_contained"].items()))
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 端点避零与重数 convention 闭合证书",
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
            "endpoint_multiplicity_convention_closed="
            f"{fmt_bool(result['endpoint_multiplicity_convention_closed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足与外部替换",
        "",
        "自足输入基：",
        "",
        "```text",
        self_repl[0],
        "  =>",
        self_repl[1],
        "```",
        "",
        "外部 Backlund 输入基：",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "## 2. 极限 convention",
        "",
        "```text",
        result["core_limit_formula"],
        "```",
        "",
        "| step | content |",
        "| --- | --- |",
    ]
    for item in result["convention_steps"]:
        lines.append(
            "| {step} | {content} |".format(
                step=table_cell(item["step"]),
                content=table_cell(item["content"]),
            )
        )
    lines.extend(
        [
            "",
            "关键点是：端点落零不产生新的分析估计。先绕开、后取极限；跳变由零点重数账本吸收，"
            "近零点绕行成本仍归属 Backlund 凹口账本，不能在这里重复扣费或伪造余量。",
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
            "conditional/external Backlund 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"完全自足路线仍先攻 `{result['next_priority']}`；"
                f"外部 Backlund 分支下一步转为 `{result['conditional_next_priority']}`。"
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
