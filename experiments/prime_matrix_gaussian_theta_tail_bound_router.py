#!/usr/bin/env python3
"""Prime Matrix Gaussian theta 尾界账本路由器。

用法示例：
  python3 experiments/prime_matrix_gaussian_theta_tail_bound_router.py

输出：
  docs/monograph/prime-matrix-gaussian-theta-tail-bound-router.json
  docs/monograph/prime-matrix-gaussian-theta-tail-bound-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_TRACE = MONO / "prime-matrix-interval-operation-trace-hash-ledger-router.json"
DEFAULT_RANGE = MONO / "prime-matrix-theta-mellin-range-box-router.json"
DEFAULT_THETA_MELLIN = MONO / "prime-matrix-b3-theta-mellin-functional-equation-router.json"
DEFAULT_JSON = MONO / "prime-matrix-gaussian-theta-tail-bound-router.json"
DEFAULT_MD = MONO / "prime-matrix-gaussian-theta-tail-bound-router.md"

OLD_ATOM = "GaussianThetaTailBoundLedger"
CLOSED_ATOM = "GaussianThetaTailBoundClosedN20T64Xi1eMinus80"
QUADRATURE = "CompactThetaMellinQuadratureSubdivisionLedger0To14"

N_CUTOFF = 20
T_CUTOFF = 64
XI_TAIL_TARGET = Decimal("1e-80")


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


def sci(value: Decimal) -> str:
    """Decimal 科学计数法展示。"""
    return f"{value:.6E}"


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


def tail_bounds() -> dict[str, Any]:
    """计算保守 Gaussian theta 尾界。"""
    getcontext().prec = 100
    n1 = Decimal(N_CUTOFF + 1)
    t0 = Decimal(T_CUTOFF)
    # 只用 pi>3 与几何比 <1/2，避免依赖浮点圆周率。
    n_tail_lambda = (Decimal(4) / (Decimal(3) * n1 * n1)) * (-(Decimal(3) * n1 * n1)).exp()
    t_tail_lambda = (Decimal(4) / Decimal(3)) * (-(Decimal(3) * t0)).exp()
    lambda_tail = n_tail_lambda + t_tail_lambda
    xi_multiplier = Decimal(225) / Decimal(2)
    xi_tail = xi_multiplier * lambda_tail
    return {
        "n_cutoff": N_CUTOFF,
        "t_cutoff": T_CUTOFF,
        "power_weight_bound": "2",
        "pi_lower_bound_used": "3",
        "series_ratio_bound": "< 1/2",
        "n_tail_lambda_bound": sci(n_tail_lambda),
        "t_tail_lambda_bound": sci(t_tail_lambda),
        "lambda_tail_total_bound": sci(lambda_tail),
        "xi_multiplier_bound": sci(xi_multiplier),
        "xi_tail_total_bound": sci(xi_tail),
        "xi_tail_target": sci(XI_TAIL_TARGET),
        "xi_tail_margin_factor": sci(XI_TAIL_TARGET / xi_tail),
        "xi_tail_closed": xi_tail < XI_TAIL_TARGET,
    }


def proof_lines() -> list[str]:
    """给出文内可读证明链。"""
    return [
        "theta_0(t)=2*sum_{n>=1} exp(-pi*n^2*t).",
        "在 -1<=sigma<=2 且 t>=1 上，|t^(s/2-1)|<=1 且 |t^((1-s)/2-1)|<=1。",
        "因此 Lambda 对称积分的尾误差不超过被删去 theta_0(t) 的积分。",
        "n>N 的级数尾：int_1^infty 2*sum_{n>=N+1} exp(-pi*n^2*t) dt <= 4/(3*(N+1)^2)*exp(-3*(N+1)^2)。",
        "t>T 的积分尾：int_T^infty 2*sum_{n>=1} exp(-pi*n^2*t) dt <= 4/3*exp(-3*T)。",
        "|s|<=15 且 |s-1|<=15，所以 xi(s)=1/2*s*(s-1)*Lambda(s) 的尾误差乘子 <=225/2。",
    ]


def build_rows(trace: dict[str, Any], range_box: dict[str, Any], theta_mellin: dict[str, Any], bounds: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Gaussian theta 尾界判定表。"""
    active = trace.get("next_priority") == OLD_ATOM
    guard = (
        trace.get("counterexample_assumption_only") is True
        and trace.get("empirical_absence_not_used") is True
        and trace.get("hypothetical_chain_only") is True
    )
    trace_ready = trace.get("certified_complex_ball_kernel_closed") is True
    range_ready = (
        range_box.get("range_box_closed") is True
        and range_box["range_boxes"]["theta_finite_n_window"] == [1, N_CUTOFF]
        and range_box["range_boxes"]["theta_mellin_t_window"] == ["1", str(T_CUTOFF)]
    )
    theta_mellin_ready = theta_mellin.get("theta_mellin_zeta_functional_equation_closed") is True
    tail_tiny = bounds["xi_tail_closed"] is True
    closed = all([active, guard, trace_ready, range_ready, theta_mellin_ready, tail_tiny])
    return [
        row(
            "GaussianThetaTailGateActive",
            active,
            True,
            "trace/hash 闭合后，当前最窄点是 theta 级数和 t 积分截断尾界。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只是解析尾界，不使用真实零行缺席或数值采样代替证明。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "ThetaMellinFormulaImported",
            theta_mellin_ready,
            True,
            "已闭合 Lambda(s) 的 [1,infty) 对称 theta-Mellin 积分公式。",
            "Lambda symmetric integral available.",
        ),
        row(
            "FiniteWindowImported",
            range_ready,
            True,
            "范围盒固定主窗口 1<=t<=64 与有限 theta 项 1<=n<=20。",
            "n>20 and t>64 are exactly the tails paid here.",
        ),
        row(
            "PowerWeightsDoNotAmplifyTail",
            True,
            True,
            "在 -1<=Re(s)<=2, t>=1 上两个 Mellin 幂权模长均不超过 1，总权重不超过 2。",
            "tail reduces to Gaussian theta_0 integral.",
        ),
        row(
            "SeriesTailNGreater20Closed",
            True,
            True,
            f"用 pi>3 与几何比<1/2 得 n>20 对 Lambda 的贡献 <= {bounds['n_tail_lambda_bound']}。",
            CLOSED_ATOM,
        ),
        row(
            "IntegralTailTGreater64Closed",
            True,
            True,
            f"用 pi>3 与几何比<1/2 得 t>64 对 Lambda 的贡献 <= {bounds['t_tail_lambda_bound']}。",
            CLOSED_ATOM,
        ),
        row(
            "XiMultiplierTailStillTiny",
            tail_tiny,
            True,
            f"乘上 |s(s-1)|/2<=225/2 后 xi 总尾界 <= {bounds['xi_tail_total_bound']} < {bounds['xi_tail_target']}。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            closed,
            "Gaussian theta 截断尾项账本已闭合，有限引擎可只处理 n<=20 与 1<=t<=64。",
            CLOSED_ATOM if closed else OLD_ATOM,
        ),
        row(
            "QuadratureStillDownstream",
            False,
            False,
            "本步不支付 [1,64] 紧致区间上的积分分段/求积误差。",
            QUADRATURE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Gaussian theta 尾界账本路由。"""
    trace = load_json(paths["trace"])
    range_box = load_json(paths["range"])
    theta_mellin = load_json(paths["theta_mellin"])
    bounds = tail_bounds()
    rows = build_rows(trace, range_box, theta_mellin, bounds)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_gaussian_theta_tail_bound_router",
        "status": "gaussian_theta_tail_bound_closed_quadrature_next"
        if closed
        else "gaussian_theta_tail_bound_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "gaussian_theta_tail_bound_closed": closed,
        "theta_mellin_interval_engine_closed": False,
        "row_column_self_contained_closed": False,
        "replacement": {OLD_ATOM: CLOSED_ATOM},
        "tail_bounds": bounds,
        "proof_lines": proof_lines(),
        "next_priority": QUADRATURE,
        "downstream_priority": "XiBoundaryIntervalNonzeroCertificate0To14 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14",
        "plain_conclusion": (
            "GaussianThetaTailBoundLedger 已闭合：在 theta-Mellin 对称积分中，低高度矩形不会放大 "
            "Gaussian 尾；n>20 和 t>64 的 xi 级总尾界小于 1e-80。剩余集中到 [1,64] "
            "紧致窗口的积分分段/求积账本。"
            if closed
            else "GaussianThetaTailBoundLedger 尚未闭合；需要补齐上游 theta-Mellin 公式、范围盒或尾界。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    bounds = result["tail_bounds"]
    lines = [
        "# Prime Matrix Gaussian theta 尾界账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"gaussian_theta_tail_bound_closed={fmt_bool(result['gaussian_theta_tail_bound_closed'])}",
        f"theta_mellin_interval_engine_closed={fmt_bool(result['theta_mellin_interval_engine_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 尾界参数",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| n cutoff | `{bounds['n_cutoff']}` |",
        f"| t cutoff | `{bounds['t_cutoff']}` |",
        f"| n-tail Lambda bound | `{bounds['n_tail_lambda_bound']}` |",
        f"| t-tail Lambda bound | `{bounds['t_tail_lambda_bound']}` |",
        f"| total Lambda tail | `{bounds['lambda_tail_total_bound']}` |",
        f"| xi multiplier | `{bounds['xi_multiplier_bound']}` |",
        f"| total xi tail | `{bounds['xi_tail_total_bound']}` |",
        f"| target | `{bounds['xi_tail_target']}` |",
        f"| margin factor | `{bounds['xi_tail_margin_factor']}` |",
        "",
        "## 2. 证明链",
        "",
    ]
    for index, line in enumerate(result["proof_lines"], start=1):
        lines.append(f"{index}. {line}")
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
            f"当前最窄点：`{result['next_priority']}`。",
            f"后续进入：`{result['downstream_priority']}`。",
            "",
            "判定：theta 尾项已支付；仍需紧致积分分段账本，不能据此直接宣称低高度矩形证书闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace-json", type=Path, default=DEFAULT_TRACE)
    parser.add_argument("--range-json", type=Path, default=DEFAULT_RANGE)
    parser.add_argument("--theta-mellin-json", type=Path, default=DEFAULT_THETA_MELLIN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "trace": args.trace_json,
        "range": args.range_json,
        "theta_mellin": args.theta_mellin_json,
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
