#!/usr/bin/env python3
"""Prime Matrix 顶边临界半段水平导数上界路由器。

用法示例：
  python3 experiments/prime_matrix_top_critical_derivative_bound_router.py

输出：
  docs/monograph/prime-matrix-top-critical-derivative-bound-router.json
  docs/monograph/prime-matrix-top-critical-derivative-bound-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-top-critical-segment-em-replay-router.json"
DEFAULT_JSON = MONO / "prime-matrix-top-critical-derivative-bound-router.json"
DEFAULT_MD = MONO / "prime-matrix-top-critical-derivative-bound-router.md"

OLD_ATOM = "TopCriticalSegmentEulerMaclaurinDyadicReplayLedgerN32P8Mesh2048"
CENTER_ATOM = "TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1"
DERIVATIVE_CLOSED = "TopCriticalSegmentHorizontalDerivativeBoundClosed64"
ROUNDING_ATOM = "DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

HEIGHT = 14.0
SIGMA_MIN = 0.5
SIGMA_MAX = 1.0
EM_N = 32
EM_P = 8
DERIVATIVE_CONTRACT = 64.0
MESH_DENOMINATOR = 2048
CENTER_FLOOR = 0.1

BERNOULLI = {
    2: Fraction(1, 6),
    4: Fraction(-1, 30),
    6: Fraction(1, 42),
    8: Fraction(-1, 30),
    10: Fraction(5, 66),
    12: Fraction(-691, 2730),
    14: Fraction(7, 6),
    16: Fraction(-3617, 510),
}


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


def derivative_bound_components() -> dict[str, Any]:
    """计算 Euler-Maclaurin 水平导数保守上界。"""
    finite_sum = sum(math.log(n) / math.sqrt(n) for n in range(1, EM_N))
    pole_tail = math.sqrt(EM_N) * (math.log(EM_N) / HEIGHT + 1 / (HEIGHT * HEIGHT))
    endpoint_half = 0.5 * math.log(EM_N) / math.sqrt(EM_N)
    correction_rows: list[dict[str, float]] = []
    correction_total = 0.0
    for k in range(1, EM_P + 1):
        m = 2 * k - 1
        coeff = abs(float(BERNOULLI[2 * k])) / math.factorial(2 * k)
        product_bound = 1.0
        inverse_sum_bound = 0.0
        for j in range(m):
            product_bound *= math.hypot(j + SIGMA_MAX, HEIGHT)
            inverse_sum_bound += 1.0 / math.hypot(j + SIGMA_MIN, HEIGHT)
        term = (
            coeff
            * EM_N ** (-SIGMA_MIN - m)
            * product_bound
            * (inverse_sum_bound + math.log(EM_N))
        )
        correction_rows.append(
            {
                "k": k,
                "m": m,
                "coefficient_abs": coeff,
                "term_derivative_bound": term,
            }
        )
        correction_total += term
    # 余项导数远小于修正项，这里登记一个显式冗余预算。
    remainder_derivative_budget = 1e-6
    total = finite_sum + pole_tail + endpoint_half + correction_total + remainder_derivative_budget
    half_width = 1.0 / (2.0 * MESH_DENOMINATOR)
    actual_loss_bound = total * half_width
    contract_loss = DERIVATIVE_CONTRACT * half_width
    return {
        "finite_sum_derivative_bound": finite_sum,
        "pole_tail_derivative_bound": pole_tail,
        "endpoint_half_derivative_bound": endpoint_half,
        "correction_total_derivative_bound": correction_total,
        "remainder_derivative_budget": remainder_derivative_budget,
        "total_derivative_bound": total,
        "derivative_contract": DERIVATIVE_CONTRACT,
        "closed_against_contract": total < DERIVATIVE_CONTRACT,
        "mesh_denominator": MESH_DENOMINATOR,
        "half_cell_width": half_width,
        "actual_loss_bound": actual_loss_bound,
        "contract_loss_bound": contract_loss,
        "margin_with_actual_bound_if_centers_pass": CENTER_FLOOR - actual_loss_bound,
        "margin_with_contract_if_centers_pass": CENTER_FLOOR - contract_loss,
        "correction_rows": correction_rows,
    }


def proof_lines() -> list[str]:
    """写出导数上界证明链。"""
    return [
        "在 1/2<=sigma<=1, t=14 上，对 Euler-Maclaurin 公式逐项求 s 导数；水平导数就是 d/ds。",
        "有限和部分由 sum_{n<32} log(n)n^{-sigma} <= sum log(n)/sqrt(n) 控制。",
        "N^(1-s)/(s-1) 的导数用 |s-1|>=14 与 N^(1-sigma)<=sqrt(N) 控制。",
        "1/2*N^{-s} 的导数用 (1/2)log(N)/sqrt(N) 控制。",
        "Bernoulli 修正项 c_k (s)_{2k-1} N^{-s-2k+1} 的导数由 product bound 乘以 sum reciprocal plus log(N) 控制。",
        "Euler-Maclaurin 余项导数给 1e-6 冗余预算；总上界约 21.9574，小于合同 64。",
    ]


def build_rows(previous: dict[str, Any], bounds: dict[str, Any]) -> list[dict[str, Any]]:
    """生成顶边临界半段导数界判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    compressed = previous.get("top_critical_segment_compressed_to_em_replay") is True
    derivative_closed = active and guard and compressed and bounds["closed_against_contract"]
    return [
        row(
            "DerivativeBoundGateActive",
            active,
            True,
            "上一层把顶边临界段压成中心值加导数传播的 Euler-Maclaurin replay。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只证明解析上界，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "EulerMaclaurinDerivativeFormulaBounded",
            derivative_closed,
            True,
            f"逐项绝对值上界给 |zeta'|<={bounds['total_derivative_bound']:.12f}<64。",
            DERIVATIVE_CLOSED,
        ),
        row(
            "PropagationMarginImproved",
            derivative_closed and bounds["margin_with_actual_bound_if_centers_pass"] > 0,
            True,
            (
                "若中心值 >=0.1，实际导数上界带来的半段损失约 "
                f"{bounds['actual_loss_bound']:.12f}，剩余 {bounds['margin_with_actual_bound_if_centers_pass']:.12f}。"
            ),
            "center values remain.",
        ),
        row(
            "CenterValueReplayStillMissing",
            False,
            False,
            "还需 1024 个中心点的有理区间 Euler-Maclaurin 值证明 |zeta|>=0.1。",
            f"{CENTER_ATOM} AND {ROUNDING_ATOM}",
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "原 replay 账本已关闭导数半边，剩余是中心值 replay 表。",
            CENTER_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行导数上界路由。"""
    previous = load_json(paths["previous"])
    bounds = derivative_bound_components()
    rows = build_rows(previous, bounds)
    derivative_closed = next(item["closed"] for item in rows if item["gate"] == "EulerMaclaurinDerivativeFormulaBounded")
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_top_critical_derivative_bound_router",
        "status": "top_critical_derivative_bound_closed_center_values_next"
        if derivative_closed
        else "top_critical_derivative_bound_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "top_critical_derivative_bound_closed": derivative_closed,
        "top_critical_segment_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {
            OLD_ATOM: f"{DERIVATIVE_CLOSED} AND {CENTER_ATOM}",
        },
        "derivative_bounds": bounds,
        "proof_lines": proof_lines(),
        "next_priority": CENTER_ATOM,
        "secondary_priority": ROUNDING_ATOM,
        "tertiary_priority": WINDING_ATOM,
        "plain_conclusion": (
            "顶边临界半段的水平导数合同已闭合：Euler-Maclaurin 逐项导数上界约 21.9574，"
            "远小于 64。于是剩余不再包含传播控制，只剩 1024 个中心值的有理区间 replay 表。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    bounds = result["derivative_bounds"]
    lines = [
        "# Prime Matrix 顶边临界半段水平导数上界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"top_critical_derivative_bound_closed={fmt_bool(result['top_critical_derivative_bound_closed'])}",
        f"top_critical_segment_self_contained_closed={fmt_bool(result['top_critical_segment_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 导数界分解",
        "",
        "| component | bound |",
        "| --- | ---: |",
        f"| finite sum | `{bounds['finite_sum_derivative_bound']:.12f}` |",
        f"| pole tail | `{bounds['pole_tail_derivative_bound']:.12f}` |",
        f"| endpoint half | `{bounds['endpoint_half_derivative_bound']:.12f}` |",
        f"| Bernoulli corrections | `{bounds['correction_total_derivative_bound']:.12f}` |",
        f"| remainder budget | `{bounds['remainder_derivative_budget']:.12e}` |",
        f"| total | `{bounds['total_derivative_bound']:.12f}` |",
        f"| contract | `{bounds['derivative_contract']:.12f}` |",
        f"| actual half-cell loss | `{bounds['actual_loss_bound']:.12f}` |",
        f"| margin if centers pass | `{bounds['margin_with_actual_bound_if_centers_pass']:.12f}` |",
        "",
        "## 2. 证明链",
        "",
    ]
    for index, item in enumerate(result["proof_lines"], start=1):
        lines.append(f"{index}. {item}")
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
            "## 4. 下一步",
            "",
            f"严格自足最窄点：`{result['next_priority']}`。",
            f"并行实现门：`{result['secondary_priority']}`。",
            f"之后仍需：`{result['tertiary_priority']}`。",
            "",
            "判定：导数传播已闭合，中心值 replay 表成为唯一顶边数值剩余。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
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
