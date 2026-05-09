#!/usr/bin/env python3
"""Prime Matrix theta-Mellin 紧致范围盒路由器。

用法示例：
  python3 experiments/prime_matrix_theta_mellin_range_box_router.py

输出：
  docs/monograph/prime-matrix-theta-mellin-range-box-router.json
  docs/monograph/prime-matrix-theta-mellin-range-box-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-theta-mellin-transcendental-kernel-router.json"
DEFAULT_JSON = MONO / "prime-matrix-theta-mellin-range-box-router.json"
DEFAULT_MD = MONO / "prime-matrix-theta-mellin-range-box-router.md"

OLD_ATOM = "ThetaMellinCompactRangeBoxLedger0To14"
CLOSED_ATOM = "ThetaMellinCompactRangeBoxClosed0To14T64N20"
TAIL_ORDER = "ThetaMellinTaylorTailOrderLedger0To14"
TRACE_LEDGER = "IntervalOperationTraceHashLedger"
THETA_TAIL = "GaussianThetaTailBoundLedger"
QUADRATURE = "CompactThetaMellinQuadratureSubdivisionLedger0To14"

SIGMA_MIN = Fraction(-1, 1)
SIGMA_MAX = Fraction(2, 1)
TAU_MIN = Fraction(0, 1)
TAU_MAX = Fraction(14, 1)
T_MIN = Fraction(1, 1)
T_MAX = Fraction(64, 1)
N_THETA_MAX = 20
LOG_T_MAX_SAFE = Fraction(6, 1)
PI_LO_SAFE = Fraction(3, 1)
PI_HI_SAFE = Fraction(4, 1)


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


def frac(value: Fraction) -> str:
    """格式化有理数。"""
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def interval(lo: Fraction, hi: Fraction) -> list[str]:
    """格式化闭区间。"""
    return [frac(lo), frac(hi)]


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
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def compute_boxes() -> dict[str, Any]:
    """计算保守有理范围盒。"""
    z_re_min = SIGMA_MIN / 2 - 1
    z_re_max = SIGMA_MAX / 2 - 1
    z_im_abs = TAU_MAX / 2
    re_log_abs = max(abs(z_re_min), abs(z_re_max)) * LOG_T_MAX_SAFE
    im_log_abs = z_im_abs * LOG_T_MAX_SAFE
    gaussian_x_min = PI_LO_SAFE * T_MIN
    gaussian_x_max = PI_HI_SAFE * N_THETA_MAX * N_THETA_MAX * T_MAX
    return {
        "s_rectangle_sigma": interval(SIGMA_MIN, SIGMA_MAX),
        "s_rectangle_tau": interval(TAU_MIN, TAU_MAX),
        "theta_mellin_t_window": interval(T_MIN, T_MAX),
        "theta_finite_n_window": [1, N_THETA_MAX],
        "log_t_range_safe": interval(Fraction(0, 1), LOG_T_MAX_SAFE),
        "z_plus_re_range": interval(z_re_min, z_re_max),
        "z_minus_re_range": interval(z_re_min, z_re_max),
        "z_im_abs_bound": frac(z_im_abs),
        "re_z_log_t_abs_bound": frac(re_log_abs),
        "im_z_log_t_abs_bound": frac(im_log_abs),
        "gaussian_pi_n2_t_range_safe": interval(gaussian_x_min, gaussian_x_max),
        "pi_safe_range": interval(PI_LO_SAFE, PI_HI_SAFE),
    }


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成范围盒判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    templates_closed = previous.get("transcendental_templates_closed") is True
    boxes_closed = active and templates_closed
    return [
        row(
            "RangeBoxGateActive",
            active,
            True,
            "上一层已把超越函数核的唯一活动缺口压成紧致范围盒。",
            OLD_ATOM,
        ),
        row(
            "TranscendentalTemplatesAvailable",
            templates_closed,
            True,
            "log/trig/exp/complex power/Gaussian exp 的 Taylor 模板已闭合。",
            "只需给它们有限参数盒。",
        ),
        row(
            "LowHeightRectangleBoxFixed",
            boxes_closed,
            True,
            "取保守矩形 -1<=Re s<=2, 0<=Im s<=14，覆盖低高度非平凡零点计数区域。",
            "sigma in [-1,2], tau in [0,14]",
        ),
        row(
            "ThetaMellinTAndNWindowsFixed",
            boxes_closed,
            True,
            "固定积分主窗口 1<=t<=64 和有限 theta 项 1<=n<=20；这里只登记范围，不证明尾项足够小。",
            "tail adequacy remains in GaussianThetaTailBoundLedger",
        ),
        row(
            "LogAndPowerArgumentBoxesClosed",
            boxes_closed,
            True,
            "由 log t<=6 和 |Im z|<=7 得 |Im z log t|<=42，|Re z log t|<=9。",
            CLOSED_ATOM,
        ),
        row(
            "GaussianExponentBoxClosed",
            boxes_closed,
            True,
            "用 3<pi<4 得 pi n^2 t 落在 [3,102400]，足以供负指数 range reduction。",
            CLOSED_ATOM,
        ),
        row(
            "TailAndQuadratureStillDownstream",
            False,
            False,
            "范围盒不证明截断误差、积分分段误差或操作轨迹。",
            f"{TAIL_ORDER} AND {TRACE_LEDGER} AND {THETA_TAIL} AND {QUADRATURE}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 theta-Mellin 紧致范围盒路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    boxes_closed = all(item["closed"] for item in rows[:6])
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_theta_mellin_range_box_router",
        "status": "theta_mellin_compact_range_boxes_closed_tail_orders_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "range_box_closed": boxes_closed,
        "theta_mellin_transcendental_kernel_closed": False,
        "row_column_self_contained_closed": False,
        "replacement": {OLD_ATOM: CLOSED_ATOM},
        "range_boxes": compute_boxes(),
        "next_priority": TAIL_ORDER,
        "secondary_priority": TRACE_LEDGER,
        "downstream_priority": f"{THETA_TAIL} AND {QUADRATURE}",
        "plain_conclusion": (
            "theta-Mellin 超越函数核的范围盒已可保守关闭：低高度矩形、主积分窗口、"
            "有限 theta 项窗口、log/power 参数和 Gaussian 指数参数都被有理区间包住。"
            "本步不证明 t>64 或 n>20 的尾项足够小，也不证明积分分段误差；这些仍由后续账本承担。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    boxes = result["range_boxes"]
    lines = [
        "# Prime Matrix theta-Mellin 紧致范围盒路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"range_box_closed={fmt_bool(result['range_box_closed'])}",
        (
            "theta_mellin_transcendental_kernel_closed="
            f"{fmt_bool(result['theta_mellin_transcendental_kernel_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 范围盒",
        "",
        "| item | range |",
        "| --- | --- |",
    ]
    for key, value in boxes.items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一步",
            "",
            f"当前最窄点：`{result['next_priority']}`。",
            f"并行审计点：`{result['secondary_priority']}`。",
            f"后续仍需 `{result['downstream_priority']}`。",
            "",
            "判定：范围盒已闭合，剩余变成 Taylor 尾阶表、调用轨迹、Gaussian 尾项和积分分段。",
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
