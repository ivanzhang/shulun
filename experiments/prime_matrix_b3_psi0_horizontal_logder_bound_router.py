#!/usr/bin/env python3
"""Prime Matrix B=3 psi_0 水平边 log-derivative 上界路由器。

用法示例：
  python3 experiments/prime_matrix_b3_psi0_horizontal_logder_bound_router.py

输出：
  docs/monograph/prime-matrix-b3-psi0-horizontal-logder-bound-router.json
  docs/monograph/prime-matrix-b3-psi0-horizontal-logder-bound-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-psi0-fixed-height-indentation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-psi0-horizontal-logder-bound-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-psi0-horizontal-logder-bound-router.md"

OLD_ATOM = "Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger"
INTERNAL_LOGDER = "ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger"
EXTERNAL_LOGDER = "ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted"
RIGHT_CAP_EXTERNAL = "ExplicitNearOneZetaLogDerivativeExternalRegistered"
TITCHMARSH_STRUCTURAL = "TitchmarshLocalZeroExpansionExternalRegistered"
LOCAL_ZERO_DISTANCE = "Psi0HorizontalLocalZeroDistanceSumConstantLedger"
WEIGHTED_BUDGET = "Psi0HorizontalWeightedIntegralBudgetLedger"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
BACKLUND_EXTERNAL = "ClassicalBacklundZeroIndentationCostExternalAccepted"
GOOD_HEIGHT = "Psi0GoodHeightTStarAveragingContourShiftLedger"
CONTOUR_ATOM = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"

ANCHOR_X = 20_000.0
ANCHOR_T_VALUES = [14.0, 45.0, 1_000.0, 20_000.0]
DIAGNOSTIC_C_AWAY = 87.0

EXTERNAL_SOURCES = [
    {
        "name": "Titchmarsh, The Theory of the Riemann Zeta-function, Theorem 9.6(A)",
        "url": "https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf",
        "used_for": (
            "结构性来源：zeta'/zeta 可写成附近零点主部和 O(log t) 余项；"
            "该来源不是项目级显式常数闭合。"
        ),
    },
    {
        "name": "Nicol Leong, arXiv:2405.04869",
        "url": "https://arxiv.org/abs/2405.04869",
        "used_for": (
            "显式外部候选：给出接近 1 线的 log-derivative 显式估计；"
            "仍需检查是否覆盖本项目 whole-strip Perron 水平边。"
        ),
    },
    {
        "name": "Tim Trudgian, explicit logarithmic derivative bounds",
        "url": "https://doi.org/10.7169/facm/2015.52.2.5",
        "used_for": (
            "显式外部候选：接近 1 线时有 |zeta'/zeta| <= 87 log t 类型界；"
            "但原条件 t>=45 且 sigma 接近 1，不能单独覆盖全水平边。"
        ),
    },
]


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


def self_contained_replacement() -> str:
    """写出自足路线替换包。"""
    return f"({INTERNAL_LOGDER} AND {LOCAL_ZERO_DISTANCE} AND {WEIGHTED_BUDGET})"


def external_replacement() -> str:
    """写出外部路线替换包。"""
    return f"({EXTERNAL_LOGDER} AND {WEIGHTED_BUDGET})"


def structural_replacement() -> str:
    """写出当前已确认的结构分解包。"""
    return (
        f"({TITCHMARSH_STRUCTURAL} AND {RIGHT_CAP_EXTERNAL} AND "
        f"{LOCAL_ZERO_DISTANCE} AND {WEIGHTED_BUDGET})"
    )


def replace_atom(text: str, replacement: str) -> str:
    """替换水平边 log-derivative 原子。"""
    return text.replace(OLD_ATOM, replacement)


def weighted_diagnostics() -> list[dict[str, float]]:
    """生成加权水平边压力诊断；这是量纲检查，不是闭合证明。"""
    rows: list[dict[str, float]] = []
    for height in ANCHOR_T_VALUES:
        log_x_t = math.log(ANCHOR_X * height)
        # 若 pointwise bound 是 C log^2(xT)，两条水平边粗略吸收为 2eC x log^2(xT)/T。
        bound = 2.0 * math.e * DIAGNOSTIC_C_AWAY * ANCHOR_X * log_x_t * log_x_t / height
        rows.append(
            {
                "x": ANCHOR_X,
                "T": height,
                "C_away": DIAGNOSTIC_C_AWAY,
                "log_xT": log_x_t,
                "diagnostic_two_horizontal_bound": bound,
                "relative_to_x": bound / ANCHOR_X,
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
    """生成水平边 log-derivative 判定表。"""
    self_basis = previous.get("latest_self_contained_basis", "")
    external_basis = previous.get("latest_external_fixed_t_basis", "")
    active = (
        previous.get("conditional_next_priority") == OLD_ATOM
        or OLD_ATOM in self_basis
        or OLD_ATOM in external_basis
    )
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    fixed_t_external = previous.get("psi0_fixed_t_indentation_external_closed") is True
    fixed_t_self_open = previous.get("psi0_fixed_t_indentation_self_contained_closed") is False
    structural_ready = active and guard
    # Titchmarsh 给结构，Leong/Trudgian 给接近 1 线候选；whole-strip 显式常数还未匹配。
    right_cap_registered = structural_ready
    whole_strip_external_matched = False
    local_zero_distance_closed = False
    weighted_budget_closed = False
    self_closed = False
    external_closed = whole_strip_external_matched and weighted_budget_closed
    return [
        row(
            "Psi0HorizontalLogDerivativeGateActive",
            active,
            True,
            "上一层 fixed-T 缩进归并后，条件路线下一点是水平边 away-from-zero 的 -zeta'/zeta 上界。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条解析输入，不使用真实零行缺席或数值实验替代证明。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FixedTIndentExternalAvailable",
            fixed_t_external,
            False,
            "接受外部 Backlund 缩进后，近零穿越成本可条件支付；这只解决极近零点，不给 away-from-zero 全边界常数。",
            BACKLUND_EXTERNAL,
        ),
        row(
            "FixedTIndentSelfContainedStillOpen",
            fixed_t_self_open,
            True,
            "严格自足路线仍同时保留 Backlund 缩进内部证明义务。",
            BACKLUND_INTERNAL,
        ),
        row(
            "TitchmarshLocalZeroExpansionRegistered",
            structural_ready,
            False,
            "经典结构公式可把 zeta'/zeta 分成附近零点主部和 O(log T) 余项。",
            TITCHMARSH_STRUCTURAL,
        ),
        row(
            "NearOneExplicitExternalRegistered",
            right_cap_registered,
            False,
            "Leong/Trudgian 类型显式结果可作为右端接近 1 线的外部候选。",
            RIGHT_CAP_EXTERNAL,
        ),
        row(
            "WholeStripExplicitExternalMatchMissing",
            whole_strip_external_matched,
            False,
            "项目水平边从左边界到右边界，需 whole-strip、避零距离、端点 convention 同时匹配的显式常数；当前外部候选尚未严格覆盖。",
            EXTERNAL_LOGDER,
        ),
        row(
            "LocalZeroDistanceSumConstantMissing",
            local_zero_distance_closed,
            False,
            "Titchmarsh 结构仍需把 sum 1/|s-rho| 在凹口后用局部零点计数和最小距离显式化。",
            LOCAL_ZERO_DISTANCE,
        ),
        row(
            "HorizontalWeightedIntegralBudgetMissing",
            weighted_budget_closed,
            False,
            "即使有 pointwise log-derivative 上界，还需把 x^sigma/|s| 权重积分压进 Perron/PNT 常数预算。",
            WEIGHTED_BUDGET,
        ),
        row(
            "HorizontalLogDerivativeStructuralReduction",
            structural_ready,
            False,
            "本步完成结构分解：外部结构公式和右端显式候选已定位，但项目级 whole-strip 常数和加权预算仍开放。",
            structural_replacement(),
        ),
        row(
            OLD_ATOM,
            self_closed or external_closed,
            False,
            "自足路线和外部严格匹配路线都尚未完全关闭该水平边原子。",
            f"self: {self_contained_replacement()} ; external: {external_replacement()}",
        ),
        row(
            "Psi0ZetaLogDerivativeContourShiftStillOpen",
            False,
            False,
            "fixed-T 缩进已归并，但水平边上界未闭合，所以完整轮廓移线仍未闭合。",
            CONTOUR_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行水平边 log-derivative 路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "HorizontalLogDerivativeStructuralReduction"
    )
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_psi0_horizontal_logder_bound_router",
        "status": "psi0_horizontal_logder_structural_reduction_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "psi0_horizontal_logder_structural_reduction": reduced,
        "psi0_horizontal_logder_self_contained_closed": False,
        "psi0_horizontal_logder_external_strict_match_closed": False,
        "psi0_horizontal_weighted_integral_budget_closed": False,
        "zeta_logder_contour_shift_closed": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: self_contained_replacement()},
        "replacement_external": {OLD_ATOM: external_replacement()},
        "replacement_structural": {OLD_ATOM: structural_replacement()},
        "latest_self_contained_basis": replace_atom(
            previous.get("latest_self_contained_basis", ""),
            self_contained_replacement(),
        ),
        "latest_external_backlund_basis": replace_atom(
            previous.get("latest_external_fixed_t_basis", ""),
            external_replacement(),
        ),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": LOCAL_ZERO_DISTANCE,
        "secondary_priority": WEIGHTED_BUDGET,
        "external_match_priority": EXTERNAL_LOGDER,
        "parallel_self_contained_priority": BACKLUND_INTERNAL,
        "alternative_priority": GOOD_HEIGHT,
        "post_horizontal_priority": ZERO_SUM_ATOM,
        "diagnostic_C_away": DIAGNOSTIC_C_AWAY,
        "weighted_diagnostics": weighted_diagnostics(),
        "external_sources": EXTERNAL_SOURCES,
        "plain_conclusion": (
            "`Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger` 已完成结构性压缩，但未闭合。"
            "Titchmarsh 公式给出附近零点主部加 O(log T) 的结构，Leong/Trudgian 给出接近 1 线的显式外部候选；"
            "然而项目需要覆盖整个 Perron 水平边的显式常数，并把避零距离后的局部零点和 "
            "`x^s/s` 加权积分纳入 PNT 常数预算。"
            "因此外部路线的下一步不是再谈 fixed-T 缩进，而是严格匹配 `ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted`，"
            "并完成 `Psi0HorizontalWeightedIntegralBudgetLedger`；严格自足路线还需内部证明局部零点距离和。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    self_repl = next(iter(result["replacement_self_contained"].items()))
    ext_repl = next(iter(result["replacement_external"].items()))
    structural_repl = next(iter(result["replacement_structural"].items()))
    lines = [
        "# Prime Matrix B=3 psi_0 水平边 log-derivative 上界路由器",
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
            "psi0_horizontal_logder_structural_reduction="
            f"{fmt_bool(result['psi0_horizontal_logder_structural_reduction'])}"
        ),
        (
            "psi0_horizontal_logder_self_contained_closed="
            f"{fmt_bool(result['psi0_horizontal_logder_self_contained_closed'])}"
        ),
        (
            "psi0_horizontal_logder_external_strict_match_closed="
            f"{fmt_bool(result['psi0_horizontal_logder_external_strict_match_closed'])}"
        ),
        (
            "psi0_horizontal_weighted_integral_budget_closed="
            f"{fmt_bool(result['psi0_horizontal_weighted_integral_budget_closed'])}"
        ),
        f"zeta_logder_contour_shift_closed={fmt_bool(result['zeta_logder_contour_shift_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 原子替换",
        "",
        "结构性分解：",
        "",
        "```text",
        structural_repl[0],
        "  =>",
        structural_repl[1],
        "```",
        "",
        "严格自足路线：",
        "",
        "```text",
        self_repl[0],
        "  =>",
        self_repl[1],
        "```",
        "",
        "外部严格匹配路线：",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "## 2. 外部来源",
        "",
        "| source | url | used for |",
        "| --- | --- | --- |",
    ]
    for source in result["external_sources"]:
        lines.append(
            "| {name} | {url} | {used_for} |".format(
                name=table_cell(source["name"]),
                url=table_cell(source["url"]),
                used_for=table_cell(source["used_for"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 加权压力诊断",
            "",
            "| x | T | C_away | log(xT) | diagnostic two-horizontal bound | relative to x |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["weighted_diagnostics"]:
        lines.append(
            "| {x} | {T} | {C} | {L} | {bound} | {rel} |".format(
                x=fmt_float(float(item["x"])),
                T=fmt_float(float(item["T"])),
                C=fmt_float(float(item["C_away"])),
                L=fmt_float(float(item["log_xT"])),
                bound=fmt_float(float(item["diagnostic_two_horizontal_bound"])),
                rel=fmt_float(float(item["relative_to_x"])),
            )
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
            "严格自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "接受外部 Backlund 缩进后的输入基：",
            "",
            "```text",
            result["latest_external_backlund_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"内部路线先攻 `{result['next_priority']}`，并行保留 "
                f"`{result['parallel_self_contained_priority']}`；"
                f"外部路线先匹配 `{result['external_match_priority']}`，随后攻 "
                f"`{result['secondary_priority']}`。"
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
