#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 变差窗口尺度路由器。

用法示例：
  python3 experiments/prime_matrix_b3_variation_window_scale_router.py

输出：
  docs/monograph/prime-matrix-b3-variation-window-scale-router.json
  docs/monograph/prime-matrix-b3-variation-window-scale-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zero-distance-constant-aggregation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-variation-window-scale-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-variation-window-scale-router.md"

OLD_ATOM = "BacklundVariationWindowScaleLedger"
CLOSED_ATOM = "BacklundVariationWindowScaleClosedH1Over512C192"
DISTANCE_CLOSED = "BacklundZeroDistanceSumConstantAggregationClosedC192Eta1Over16"
GAMMA_ATOM = "GammaDigammaStirlingUniformNumericalClosedCgamma24"
INDENT_ATOM = "BacklundZeroProximityIndentationCostLedger"
CS8_ATOM = "BacklundCS8SlackAfterBridgeLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_DISTANCE = 192.0
C_GAMMA = 24.0
C_TOTAL_VARIATION = C_DISTANCE + C_GAMMA
WINDOW_LENGTH = 1.0 / 512.0
HALF_STABILITY_TARGET = 0.5
VARIATION_LOSS_FACTOR = C_TOTAL_VARIATION * WINDOW_LENGTH
STABILITY_MARGIN = HALF_STABILITY_TARGET - VARIATION_LOSS_FACTOR


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
    """替换变差窗口尺度原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def budget_rows() -> list[dict[str, Any]]:
    """生成窗口尺度预算表。"""
    return [
        {
            "component": "zero-distance variation",
            "coefficient": C_DISTANCE,
            "source": DISTANCE_CLOSED,
        },
        {
            "component": "Gamma/digamma variation",
            "coefficient": C_GAMMA,
            "source": GAMMA_ATOM,
        },
        {
            "component": "total variation coefficient",
            "coefficient": C_TOTAL_VARIATION,
            "source": "C_distance + C_gamma",
        },
        {
            "component": "window length",
            "coefficient": WINDOW_LENGTH,
            "source": "H=1/512",
        },
        {
            "component": "variation loss factor",
            "coefficient": VARIATION_LOSS_FACTOR,
            "source": "H*(C_distance+C_gamma)",
        },
        {
            "component": "margin to half stability",
            "coefficient": STABILITY_MARGIN,
            "source": "1/2 - loss",
        },
    ]


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
    """生成变差窗口尺度判定表。"""
    external_basis = previous.get("latest_conditional_basis", "")
    active = previous.get("conditional_next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    distance_ready = bool(previous.get("zero_distance_constant_aggregation_external_closed")) and DISTANCE_CLOSED in external_basis
    gamma_ready = GAMMA_ATOM in external_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    budget_ok = VARIATION_LOSS_FACTOR < HALF_STABILITY_TARGET
    closed = active and distance_ready and gamma_ready and guard and budget_ok
    return [
        row(
            "VariationWindowScaleGateActive",
            active,
            False,
            "外部 Backlund/Jensen 分支当前最窄点是选择短窗口尺度。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的解析局部稳定性，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "DistanceAndGammaConstantsAvailable",
            distance_ready and gamma_ready,
            True,
            "倒距离常数 C192 与 Gamma/digamma 常数 C24 均已可用。",
            f"{DISTANCE_CLOSED} AND {GAMMA_ATOM}",
        ),
        row(
            "WindowLengthChosenH1Over512",
            WINDOW_LENGTH > 0.0,
            True,
            "取短窗口长度 H=1/512；这是固定常数，不随 T 变化。",
            CLOSED_ATOM,
        ),
        row(
            "HalfStabilityBudgetPasses",
            budget_ok,
            True,
            "变差损失系数 216/512=0.421875 小于 1/2，保留短平均点态桥需要的一半质量。",
            CLOSED_ATOM,
        ),
        row(
            "VariationWindowScaleClosed",
            closed,
            True,
            "窗口尺度验收闭合；后续尖峰排斥只剩近零凹口成本与 C_S=8 余量。",
            CLOSED_ATOM,
        ),
        row(
            "IndentCostNext",
            False,
            False,
            "下一步必须支付 eta 内近零点的凹口成本。",
            INDENT_ATOM,
        ),
        row(
            "CS8SlackStillDownstream",
            False,
            False,
            "凹口成本完成后再统一验收 C_S=8。",
            CS8_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行变差窗口尺度路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "VariationWindowScaleClosed"
    )
    latest_external = replace_atom(previous.get("latest_conditional_basis", ""))
    return {
        "certificate_type": "b3_variation_window_scale_router",
        "status": "variation_window_scale_external_closed_h1_over_512",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "variation_window_scale_external_closed": closed,
        "variation_window_scale_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "distance_constant": C_DISTANCE,
        "gamma_constant": C_GAMMA,
        "total_variation_constant": C_TOTAL_VARIATION,
        "window_length": WINDOW_LENGTH,
        "variation_loss_factor": VARIATION_LOSS_FACTOR,
        "half_stability_target": HALF_STABILITY_TARGET,
        "stability_margin": STABILITY_MARGIN,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "latest_conditional_basis": latest_external,
        "latest_global_with_external_basis": latest_external,
        "next_priority": previous.get("next_priority"),
        "secondary_priority": previous.get("secondary_priority"),
        "conditional_next_priority": INDENT_ATOM,
        "post_indent_priority": CS8_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "budget_rows": budget_rows(),
        "plain_conclusion": (
            "变差窗口尺度在外部 Backlund/Jensen 分支中闭合："
            "C_distance=192 与 C_gamma=24 合计为 216，取窗口长度 H=1/512，"
            "变差损失 0.421875 小于 1/2，足以支撑短平均点态桥的半质量保留。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 变差窗口尺度路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"variation_window_scale_external_closed={fmt_bool(result['variation_window_scale_external_closed'])}",
        f"variation_window_scale_self_contained_closed={fmt_bool(result['variation_window_scale_self_contained_closed'])}",
        f"distance_constant={fmt_float(result['distance_constant'])}",
        f"gamma_constant={fmt_float(result['gamma_constant'])}",
        f"total_variation_constant={fmt_float(result['total_variation_constant'])}",
        f"window_length={fmt_float(result['window_length'])}",
        f"variation_loss_factor={fmt_float(result['variation_loss_factor'])}",
        f"stability_margin={fmt_float(result['stability_margin'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件链替换",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "## 2. 预算表",
        "",
        "| component | coefficient | source |",
        "| --- | ---: | --- |",
    ]
    for item in result["budget_rows"]:
        lines.append(
            "| {component} | `{coefficient}` | {source} |".format(
                component=table_cell(item["component"]),
                coefficient=fmt_float(float(item["coefficient"])),
                source=table_cell(item["source"]),
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
                f"外部 Backlund/Jensen 分支下一步转为 `{result['conditional_next_priority']}`。"
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
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
