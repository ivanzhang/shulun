#!/usr/bin/env python3
"""Prime Matrix Backlund 点态近零核心转移障碍路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_pointwise_core_transfer_obstruction_router.py

输出：
  docs/monograph/prime-matrix-backlund-pointwise-core-transfer-obstruction-router.json
  docs/monograph/prime-matrix-backlund-pointwise-core-transfer-obstruction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_STATUS = MONO / "prime-matrix-backlund-final-branch-status-router.json"
DEFAULT_ABSORB = MONO / "prime-matrix-backlund-indent-weight-absorption-router.json"
DEFAULT_LITTLEWOOD = MONO / "prime-matrix-b3-backlund-littlewood-rectangle-router.json"
DEFAULT_NEAR = MONO / "prime-matrix-b3-near-zero-indent-separation-router.json"
DEFAULT_VARIATION = MONO / "prime-matrix-b3-variation-window-scale-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-pointwise-core-transfer-obstruction-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-pointwise-core-transfer-obstruction-router.md"

INDENT_COST = "BacklundZeroProximityIndentationCostLedger"
POINTWISE_TRANSFER = "BacklundPointwiseNearZeroCoreTransferLedger"
SUPPORT_MISMATCH = "BacklundPointwiseCoreSupportMismatchLemmaClosed"
STIELTJES_JUMP = "BacklundBoundaryStieltjesJumpTransferLedger"
NO_DOUBLE = "BacklundZeroWeightNoDoubleCountingLedger"
CONSTANT_REAGG = "BacklundC8BudgetPreservingIndentReaggregationLedger"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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


def local_model_samples() -> list[dict[str, float]]:
    """生成左边界贴近零点模型的支撑乘子样本。"""
    h = 1.0 / 512.0
    samples: list[dict[str, float]] = []
    for eps in (1 / 16, 1 / 64, 1 / 256, 1 / 1024, 1 / 4096):
        # 局部模型：零点 rho=a+eps+iT，沿左边界 a+i(T+u) 取 |u|<=h。
        # arg(a+i(T+u)-rho) 的高度变差绝对值为 2 arctan(h/eps)。
        pointwise_jump = 2.0 * math.atan(h / eps)
        littlewood_weight = 2.0 * math.pi * eps
        needed_multiplier = pointwise_jump / littlewood_weight if littlewood_weight else math.inf
        samples.append(
            {
                "epsilon": eps,
                "window_length": h,
                "pointwise_jump_lower_model": pointwise_jump,
                "littlewood_zero_weight": littlewood_weight,
                "needed_capacity_multiplier": needed_multiplier,
            }
        )
    return samples


def obstruction_lemmas() -> list[dict[str, str]]:
    """列出本步得到的结构性障碍。"""
    return [
        {
            "lemma": "HorizontalWeightVsVerticalJumpMismatch",
            "content": (
                "Littlewood 矩形零点项按横向权重 beta-a 计；点态近零核心按高度方向的 arg 跳变计。"
                "当 beta-a=epsilon 趋近 0 时，前者趋近 0，后者在固定窗口内可保持正量。"
            ),
        },
        {
            "lemma": "NoUniformCapacityMultiplier",
            "content": (
                "若试图用 K * 2*pi*(beta-a) 支付点态跳变，则 K 至少随 1/epsilon 发散；"
                "因此 RegisteredCapacityMultiplierDiscipline 禁止直接转移。"
            ),
        },
        {
            "lemma": "BoundaryZeroSupportLowerBoundWouldBeTooStrong",
            "content": (
                "除非额外证明所有近零核心满足 beta-a>=delta>0，否则权重吸收不能推出点态核心预算；"
                "这等于排除贴边界零点，不是当前输入基已有事实。"
            ),
        },
        {
            "lemma": "StieltjesJumpTransferIsTheRealAtom",
            "content": (
                "剩余不能再是普通零点权重吸收，而必须是局部 Stieltjes 跳变/缩进引理："
                "把边界贴近零点的点态跳变作为同一轮廓极限项登记，并证明不重复扣 Jensen/RVM 预算。"
            ),
        },
    ]


def transfer_options() -> list[dict[str, str]]:
    """列出从当前障碍继续闭合的逻辑选项。"""
    return [
        {
            "option": "support_lower_bound",
            "atom": "BacklundBoundaryZeroSupportLowerBoundLedger",
            "status": "not_available",
            "reason": "需要 beta-a>=delta 的统一左边界支撑下界；这会排除或强约束临界线/贴线零点。",
        },
        {
            "option": "local_stieltjes_jump_transfer",
            "atom": STIELTJES_JUMP,
            "status": "next_internal_atom",
            "reason": "用局部轮廓同伦和 Stieltjes 跳变账本替代权重乘子，可能与经典 Backlund 缩进引理等价。",
        },
        {
            "option": "external_backlund_indent",
            "atom": EXTERNAL_ATOM,
            "status": "external_escape",
            "reason": "接受经典 Backlund 缩进处理即可关闭本分析缺口，但不是严格自足证明。",
        },
    ]


def build_rows(
    status: dict[str, Any],
    absorb: dict[str, Any],
    littlewood: dict[str, Any],
    near: dict[str, Any],
    variation: dict[str, Any],
    endpoint: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成点态核心转移障碍判定表。"""
    active = (
        status.get("self_contained_remaining") == INDENT_COST
        and absorb.get("next_priority") == POINTWISE_TRANSFER
    )
    guard = (
        absorb.get("counterexample_assumption_only") is True
        and absorb.get("empirical_absence_not_used") is True
        and absorb.get("hypothetical_chain_only") is True
    )
    rectangle_closed = littlewood.get("backlund_littlewood_rectangle_argument_closed") is True
    near_core_assigned = near.get("near_zero_indent_separation_external_closed") is True
    endpoint_limit_closed = endpoint.get("endpoint_multiplicity_convention_closed") is True
    tight_margin = float(variation.get("stability_margin", 0.0)) == 0.078125
    return [
        row(
            "PointwiseCoreTransferGateActive",
            active,
            True,
            "凹口成本内部化后的最窄点正是把矩形零点权重吸收转到点态近零核心。",
            POINTWISE_TRANSFER,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的解析障碍，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "LittlewoodRectangleWeightAvailable",
            rectangle_closed,
            True,
            "Littlewood 矩形层已有零点横向权重项。",
            "仅可作为矩形平均层输入。",
        ),
        row(
            "NearZeroCoreStillAssignedToIndent",
            near_core_assigned,
            True,
            "eta=1/16 内零点没有被倒距离和吸收，仍属于凹口/点态核心。",
            INDENT_COST,
        ),
        row(
            "EndpointLimitConventionAvailable",
            endpoint_limit_closed,
            True,
            "端点落零可由极限 convention 定义，但该 convention 不提供点态预算。",
            STIELTJES_JUMP,
        ),
        row(
            SUPPORT_MISMATCH,
            True,
            True,
            "横向权重 beta-a 可趋近 0，而点态高度跳变在同一固定窗口内仍为正量。",
            STIELTJES_JUMP,
        ),
        row(
            "DirectLittlewoodToPointwiseMultiplierBlocked",
            True,
            True,
            "任何固定容量乘子都无法把 2*pi*(beta-a) 统一转成点态近零跳变预算。",
            STIELTJES_JUMP,
        ),
        row(
            "C8BudgetCannotAbsorbResidualMultiplier",
            tight_margin,
            True,
            "C_S=8 后续为紧等号，5/64 余量也只属于窗口稳定性；不能容纳发散乘子或正比例残差。",
            CONSTANT_REAGG,
        ),
        row(
            POINTWISE_TRANSFER,
            False,
            False,
            "直接权重吸收转移已被结构性阻断；必须改证局部 Stieltjes 跳变/缩进账本。",
            f"{STIELTJES_JUMP} AND {NO_DOUBLE} AND {CONSTANT_REAGG}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行点态核心转移障碍审查。"""
    status = load_json(paths["status"])
    absorb = load_json(paths["absorb"])
    littlewood = load_json(paths["littlewood"])
    near = load_json(paths["near"])
    variation = load_json(paths["variation"])
    endpoint = load_json(paths["endpoint"])
    rows = build_rows(status, absorb, littlewood, near, variation, endpoint)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    samples = local_model_samples()
    max_needed = max(item["needed_capacity_multiplier"] for item in samples)
    return {
        "certificate_type": "prime_matrix_backlund_pointwise_core_transfer_obstruction_router",
        "status": "backlund_pointwise_core_transfer_blocked_by_support_mismatch_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "pointwise_core_transfer_closed": False,
        "support_mismatch_obstruction_closed": True,
        "indent_cost_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "left_boundary_model": {
            "setup": "zero rho=a+epsilon+iT, pointwise line sigma=a, window |u|<=H",
            "window_length": 1.0 / 512.0,
            "pointwise_jump_formula": "2*atan(H/epsilon)",
            "littlewood_weight_formula": "2*pi*epsilon",
            "needed_multiplier_formula": "atan(H/epsilon)/(pi*epsilon)",
            "unbounded_as_epsilon_to_zero": True,
            "max_sampled_multiplier": max_needed,
        },
        "samples": samples,
        "obstruction_lemmas": obstruction_lemmas(),
        "transfer_options": transfer_options(),
        "replacement_next": {
            POINTWISE_TRANSFER: STIELTJES_JUMP,
        },
        "next_priority": STIELTJES_JUMP,
        "support_priority": "BacklundBoundaryZeroSupportLowerBoundLedger",
        "discipline_priority": NO_DOUBLE,
        "constant_priority": CONSTANT_REAGG,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "点态近零核心不能由 Littlewood 矩形零点权重直接吸收。"
            "结构原因是支撑不匹配：矩形权重是横向的 beta-a，贴左边界时可任意小；"
            "而点态高度跳变在固定短窗口内仍保持正量。"
            "所以当前最窄点从普通权重转移改写为局部 Stieltjes 跳变/缩进账本；"
            "这仍未关闭严格自足路线，但排除了一个关键伪闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_next"].items()))
    model = result["left_boundary_model"]
    lines = [
        "# Prime Matrix Backlund 点态近零核心转移障碍路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"pointwise_core_transfer_closed={fmt_bool(result['pointwise_core_transfer_closed'])}",
        f"support_mismatch_obstruction_closed={fmt_bool(result['support_mismatch_obstruction_closed'])}",
        f"indent_cost_self_contained_closed={fmt_bool(result['indent_cost_self_contained_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 局部模型",
        "",
        "```text",
        f"setup: {model['setup']}",
        f"H={model['window_length']:.12f}",
        f"pointwise_jump={model['pointwise_jump_formula']}",
        f"littlewood_weight={model['littlewood_weight_formula']}",
        f"needed_multiplier={model['needed_multiplier_formula']}",
        "```",
        "",
        "| epsilon | pointwise jump | Littlewood weight | needed multiplier |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for item in result["samples"]:
        lines.append(
            "| {epsilon:.12f} | {jump:.12f} | {weight:.12f} | {mult:.12f} |".format(
                epsilon=item["epsilon"],
                jump=item["pointwise_jump_lower_model"],
                weight=item["littlewood_zero_weight"],
                mult=item["needed_capacity_multiplier"],
            )
        )
    lines.extend(
        [
            "",
            "结论：`epsilon -> 0` 时，Littlewood 横向权重趋近 `0`，但点态跳变不随同趋近 `0`；",
            "因此不存在独立于零点贴边界距离的固定容量乘子。",
            "",
            "## 2. 障碍引理",
            "",
            "| lemma | content |",
            "| --- | --- |",
        ]
    )
    for item in result["obstruction_lemmas"]:
        lines.append(f"| `{table_cell(item['lemma'])}` | {table_cell(item['content'])} |")
    lines.extend(
        [
            "",
            "## 3. 自足替换",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "| option | atom | status | reason |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["transfer_options"]:
        lines.append(
            f"| `{table_cell(item['option'])}` | `{table_cell(item['atom'])}` | "
            f"`{table_cell(item['status'])}` | {table_cell(item['reason'])} |"
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
            "## 5. 下一步",
            "",
            f"当前真正最窄点：`{result['next_priority']}`。",
            f"支撑下界备选：`{result['support_priority']}`，但该路线会要求贴边界零点支撑下界。",
            f"无重复扣费纪律：`{result['discipline_priority']}`。",
            f"常数重聚合：`{result['constant_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：直接 Littlewood 权重转移被结构性阻断；下一步只能攻局部 Stieltjes 跳变/缩进账本。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status-json", type=Path, default=DEFAULT_STATUS)
    parser.add_argument("--absorb-json", type=Path, default=DEFAULT_ABSORB)
    parser.add_argument("--littlewood-json", type=Path, default=DEFAULT_LITTLEWOOD)
    parser.add_argument("--near-json", type=Path, default=DEFAULT_NEAR)
    parser.add_argument("--variation-json", type=Path, default=DEFAULT_VARIATION)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "status": args.status_json,
        "absorb": args.absorb_json,
        "littlewood": args.littlewood_json,
        "near": args.near_json,
        "variation": args.variation_json,
        "endpoint": args.endpoint_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["next_priority"])


if __name__ == "__main__":
    main()
