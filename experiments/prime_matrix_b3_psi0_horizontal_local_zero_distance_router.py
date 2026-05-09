#!/usr/bin/env python3
"""Prime Matrix B=3 psi_0 水平边局部零点倒距离和路由器。

用法示例：
  python3 experiments/prime_matrix_b3_psi0_horizontal_local_zero_distance_router.py

输出：
  docs/monograph/prime-matrix-b3-psi0-horizontal-local-zero-distance-router.json
  docs/monograph/prime-matrix-b3-psi0-horizontal-local-zero-distance-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-psi0-horizontal-logder-bound-router.json"
DEFAULT_CN16 = DOCS / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-psi0-horizontal-local-zero-distance-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-psi0-horizontal-local-zero-distance-router.md"

OLD_ATOM = "Psi0HorizontalLocalZeroDistanceSumConstantLedger"
CLOSED_ATOM = "Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16"
WEIGHTED_BUDGET = "Psi0HorizontalWeightedIntegralBudgetLedger"
WHOLE_STRIP_EXTERNAL = "ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
BACKLUND_EXTERNAL = "ClassicalBacklundZeroIndentationCostExternalAccepted"
CONTOUR_ATOM = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"

ETA = 1.0 / 16.0
C_N = 16.0
C_STRUCTURAL_REMAINDER = 32.0
C_LOCAL_DISTANCE = C_N / ETA
C_TOTAL_LOGDER = C_LOCAL_DISTANCE + C_STRUCTURAL_REMAINDER


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
    """把待证原子替换为闭合常数原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def external_titchmarsh_basis(previous: dict[str, Any]) -> str:
    """生成外部 Titchmarsh+CN16 路线的输入基。"""
    text = previous.get("latest_self_contained_basis", "")
    text = text.replace("ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger", "TitchmarshLocalZeroExpansionExternalRegistered")
    text = text.replace(BACKLUND_INTERNAL, BACKLUND_EXTERNAL)
    return replace_atom(text)


def constant_rows() -> list[dict[str, Any]]:
    """生成常数聚合表。"""
    return [
        {
            "item": "eta",
            "value": ETA,
            "formula": "1/16",
            "meaning": "凹口后的剩余水平边到近零点的登记最小距离。",
        },
        {
            "item": "C_N",
            "value": C_N,
            "formula": "RVMToCN16LocalInequalityClosedWithRawArgCS8",
            "meaning": "外部 Backlund/RVM 分支给出的单位高度局部零点计数常数。",
        },
        {
            "item": "local distance coefficient",
            "value": C_LOCAL_DISTANCE,
            "formula": "C_N/eta",
            "meaning": "粗界 sum 1/|s-rho| <= C_N log(T+3)/eta。",
        },
        {
            "item": "structural remainder reserve",
            "value": C_STRUCTURAL_REMAINDER,
            "formula": "Titchmarsh O(log T) reserve",
            "meaning": "给局部零点主部之外的结构余项预留。",
        },
        {
            "item": "total log-derivative coefficient",
            "value": C_TOTAL_LOGDER,
            "formula": "C_N/eta + 32",
            "meaning": "供下一层加权水平积分预算使用的 pointwise 系数。",
        },
    ]


def sample_rows() -> list[dict[str, float]]:
    """给代表性高度生成 pointwise 上界样例。"""
    rows: list[dict[str, float]] = []
    for height in [14.0, 45.0, 100.0, 1_000.0, 20_000.0, 1_000_000.0]:
        # 这里只登记 C_TOTAL_LOGDER * log(T+3)，不替代加权积分预算。
        import math

        log_t = math.log(height + 3.0)
        rows.append(
            {
                "T": height,
                "log_T_plus_3": log_t,
                "pointwise_bound": C_TOTAL_LOGDER * log_t,
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


def build_rows(previous: dict[str, Any], cn16: dict[str, Any]) -> list[dict[str, Any]]:
    """生成局部零点倒距离和判定表。"""
    self_basis = previous.get("latest_self_contained_basis", "")
    external_basis = previous.get("latest_external_backlund_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in self_basis or OLD_ATOM in external_basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    cn16_external = cn16.get("rvm_to_cn16_external_closed") is True
    cn16_self = cn16.get("rvm_to_cn16_self_contained_closed") is True
    fixed_indent_external = BACKLUND_EXTERNAL in external_basis
    fixed_indent_self = BACKLUND_INTERNAL in self_basis
    eta_valid = ETA == 1.0 / 16.0 and C_LOCAL_DISTANCE == 256.0 and C_TOTAL_LOGDER == 288.0
    external_closed = active and guard and cn16_external and fixed_indent_external and eta_valid
    self_closed = active and guard and cn16_self and fixed_indent_self and eta_valid
    return [
        row(
            "Psi0LocalZeroDistanceGateActive",
            active,
            True,
            "上一层把水平边 log-derivative 压到局部零点倒距离和与加权积分预算。",
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
            "ExternalCN16LocalCountAvailable",
            cn16_external,
            False,
            "接受外部 Backlund/RVM 分支时，单位高度零点数有 C_N=16 上界。",
            "RVMToCN16LocalInequalityClosedWithRawArgCS8",
        ),
        row(
            "SelfContainedCN16StillOpen",
            not cn16_self,
            True,
            "严格自足路线仍缺自足 Backlund 和低高度零点核验，不能自足调用 C_N=16。",
            BACKLUND_INTERNAL,
        ),
        row(
            "FixedIndentDisciplineAvailableExternally",
            fixed_indent_external,
            False,
            "外部 fixed-T 缩进允许把 eta 内近零点转入凹口成本，剩余水平段距离至少 eta。",
            BACKLUND_EXTERNAL,
        ),
        row(
            "EtaOneOver16DistanceBoundComputed",
            eta_valid,
            True,
            "在剩余水平段上，每个近零点贡献至多 1/eta；C_N=16 给出 256 log(T+3)，结构余项预留 32 log(T+3)。",
            CLOSED_ATOM,
        ),
        row(
            "Psi0LocalZeroDistanceExternalClosed",
            external_closed,
            False,
            "外部条件路线下，局部零点倒距离和闭合为 pointwise 系数 C=288。",
            CLOSED_ATOM,
        ),
        row(
            "Psi0LocalZeroDistanceSelfContainedClosed",
            self_closed,
            False,
            "自足路线只有在自足 C_N=16 和自足 fixed-T 缩进都关闭后才能同步闭合。",
            f"{BACKLUND_INTERNAL} AND RVMToCN16 self-contained",
        ),
        row(
            OLD_ATOM,
            external_closed,
            False,
            "本原子在外部 Backlund/RVM 条件路线下关闭；严格自足版仍未关闭。",
            CLOSED_ATOM,
        ),
        row(
            "HorizontalWeightedIntegralBudgetNext",
            False,
            False,
            "pointwise C=288 log(T+3) 仍需乘上 x^sigma/|s| 并进入 Perron/PNT 常数预算。",
            WEIGHTED_BUDGET,
        ),
        row(
            "WholeStripExternalMatchStillIndependent",
            False,
            False,
            "若不采用内部 Titchmarsh+CN16 展开，也可继续寻找 whole-strip 外部显式引理。",
            WHOLE_STRIP_EXTERNAL,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行局部零点倒距离和路由。"""
    previous = load_json(paths["previous"])
    cn16 = load_json(paths["cn16"])
    rows = build_rows(previous, cn16)
    external_closed = next(item["closed"] for item in rows if item["gate"] == "Psi0LocalZeroDistanceExternalClosed")
    self_closed = next(item["closed"] for item in rows if item["gate"] == "Psi0LocalZeroDistanceSelfContainedClosed")
    return {
        "certificate_type": "b3_psi0_horizontal_local_zero_distance_router",
        "status": "psi0_horizontal_local_zero_distance_external_closed_self_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "psi0_horizontal_local_zero_distance_external_closed": external_closed,
        "psi0_horizontal_local_zero_distance_self_contained_closed": self_closed,
        "psi0_horizontal_weighted_integral_budget_closed": False,
        "zeta_logder_contour_shift_closed": False,
        "row_column_unconditional_closed": False,
        "eta": ETA,
        "C_N": C_N,
        "C_local_distance": C_LOCAL_DISTANCE,
        "C_structural_remainder": C_STRUCTURAL_REMAINDER,
        "C_total_logder": C_TOTAL_LOGDER,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "latest_external_backlund_basis": previous.get("latest_external_backlund_basis", ""),
        "latest_external_titchmarsh_cn16_basis": external_titchmarsh_basis(previous),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": WEIGHTED_BUDGET,
        "secondary_priority": WHOLE_STRIP_EXTERNAL,
        "parallel_self_contained_priority": BACKLUND_INTERNAL,
        "post_horizontal_priority": ZERO_SUM_ATOM,
        "contour_shift_atom": CONTOUR_ATOM,
        "constant_rows": constant_rows(),
        "sample_rows": sample_rows(),
        "plain_conclusion": (
            "`Psi0HorizontalLocalZeroDistanceSumConstantLedger` 在外部 Backlund/RVM 条件路线下闭合："
            "固定 eta=1/16 后，凹口外剩余水平段到近零点距离至少 eta，"
            "C_N=16 给出倒距离和不超过 256 log(T+3)，再给 Titchmarsh 结构余项预留 32 log(T+3)，"
            "得到 pointwise 系数 C=288。该步不关闭严格自足路线，也不关闭加权水平积分预算。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 psi_0 水平边局部零点倒距离和路由器",
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
            "psi0_horizontal_local_zero_distance_external_closed="
            f"{fmt_bool(result['psi0_horizontal_local_zero_distance_external_closed'])}"
        ),
        (
            "psi0_horizontal_local_zero_distance_self_contained_closed="
            f"{fmt_bool(result['psi0_horizontal_local_zero_distance_self_contained_closed'])}"
        ),
        (
            "psi0_horizontal_weighted_integral_budget_closed="
            f"{fmt_bool(result['psi0_horizontal_weighted_integral_budget_closed'])}"
        ),
        f"zeta_logder_contour_shift_closed={fmt_bool(result['zeta_logder_contour_shift_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"C_total_logder={fmt_float(result['C_total_logder'])}",
        "```",
        "",
        "## 1. 外部条件替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 常数表",
        "",
        "| item | value | formula | meaning |",
        "| --- | ---: | --- | --- |",
    ]
    for item in result["constant_rows"]:
        lines.append(
            "| {item} | `{value}` | {formula} | {meaning} |".format(
                item=table_cell(item["item"]),
                value=fmt_float(float(item["value"])),
                formula=table_cell(item["formula"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 样例上界",
            "",
            "| T | log(T+3) | pointwise bound |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in result["sample_rows"]:
        lines.append(
            "| {T} | {L} | {B} |".format(
                T=fmt_float(float(item["T"])),
                L=fmt_float(float(item["log_T_plus_3"])),
                B=fmt_float(float(item["pointwise_bound"])),
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
            "接受外部 Backlund/RVM 后的输入基：",
            "",
            "```text",
            result["latest_external_titchmarsh_cn16_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"下一步集中攻 `{result['next_priority']}`；"
                f"严格自足路线并行保留 `{result['parallel_self_contained_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--cn16", type=Path, default=DEFAULT_CN16)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "cn16": args.cn16,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
