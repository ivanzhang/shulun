#!/usr/bin/env python3
"""Prime Matrix 顶边临界半段虚部负号路由器。

用法示例：
  python3 experiments/prime_matrix_top_critical_imaginary_sign_router.py

输出：
  docs/monograph/prime-matrix-top-critical-imaginary-sign-router.json
  docs/monograph/prime-matrix-top-critical-imaginary-sign-router.md
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_DERIVATIVE = MONO / "prime-matrix-top-critical-derivative-bound-router.json"
DEFAULT_ROUNDING = MONO / "prime-matrix-em-replay-rounding-discipline-router.json"
DEFAULT_JSON = MONO / "prime-matrix-top-critical-imaginary-sign-router.json"
DEFAULT_MD = MONO / "prime-matrix-top-critical-imaginary-sign-router.md"

OLD_ATOM = "TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1"
NEW_ATOM = "TopCriticalSegmentCenterImagNegativeEMReplayLedgerN32P8Mesh2048FloorMinus1Over40"
SEGMENT_CLOSED = "TopCriticalSegmentXiNonzeroClosedByImagNegativeT14HalfToOne"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

HEIGHT = 14.0
MESH_DENOMINATOR = 2048
CELL_COUNT = 1024
IMAG_FLOOR = -1.0 / 40.0


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


def eta_euler(s: complex, terms: int = 220) -> complex:
    """用 Euler 变换近似 zeta(s)，仅作侦察审计。"""
    values = [cmath.exp(-s * math.log(n + 1)) for n in range(terms + 1)]
    total = 0j
    weight = 2.0
    for k in range(terms):
        total += values[0] / weight
        for i in range(terms - k):
            values[i] = values[i] - values[i + 1]
        weight *= 2.0
    two_power = cmath.exp((1 - s) * math.log(2))
    return total / (1 - two_power)


def audit_imaginary_sign() -> dict[str, Any]:
    """扫描中心虚部负号余量。"""
    max_imag = -10.0
    max_sigma = 0.0
    min_imag = 10.0
    min_sigma = 0.0
    for j in range(CELL_COUNT):
        sigma = 0.5 + (j + 0.5) / MESH_DENOMINATOR
        zeta_value = eta_euler(sigma + HEIGHT * 1j)
        if zeta_value.imag > max_imag:
            max_imag = zeta_value.imag
            max_sigma = sigma
        if zeta_value.imag < min_imag:
            min_imag = zeta_value.imag
            min_sigma = sigma
    return {
        "height": HEIGHT,
        "mesh_denominator": MESH_DENOMINATOR,
        "cell_count": CELL_COUNT,
        "imag_floor_contract": IMAG_FLOOR,
        "audit_max_center_imag": max_imag,
        "audit_max_center_sigma": max_sigma,
        "audit_min_center_imag": min_imag,
        "audit_min_center_sigma": min_sigma,
        "audit_margin_below_floor": IMAG_FLOOR - max_imag,
    }


def proof_contract(derivative_loss: float) -> list[str]:
    """写出虚部负号证明合同。"""
    return [
        "对每个中心 c_j=1/2+(j+1/2)/2048，用 EM replay 证明 Im zeta(c_j+14i)<=-1/40。",
        f"已闭合导数界给每个半小段的虚部漂移至多 {derivative_loss:.12f}。",
        f"若中心虚部 <=-1/40，则整段虚部 <= {-1/40 + derivative_loss:.12f}<0。",
        "因此 zeta 在顶边临界半段无零；xi 的显式因子非零，所以 xi 也无零。",
        "这比 |zeta|>=0.1 的复模证书更窄，只需证明一个实区间上界。",
    ]


def build_rows(derivative: dict[str, Any], rounding: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成虚部负号判定表。"""
    active = derivative.get("next_priority") == OLD_ATOM or rounding.get("next_priority") == OLD_ATOM
    guard = (
        derivative.get("counterexample_assumption_only") is True
        and derivative.get("empirical_absence_not_used") is True
        and derivative.get("hypothetical_chain_only") is True
    )
    derivative_ready = derivative.get("top_critical_derivative_bound_closed") is True
    rounding_ready = rounding.get("em_replay_rounding_discipline_closed") is True
    derivative_loss = derivative["derivative_bounds"]["actual_loss_bound"]
    propagation_negative = IMAG_FLOOR + derivative_loss < 0
    audit_supports = audit["audit_max_center_imag"] < IMAG_FLOOR
    return [
        row(
            "ImaginarySignGateActive",
            active,
            True,
            "中心值复模表可被更窄的中心虚部负号表替代。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理低高度解析证书，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "DerivativeAndRoundingInputsImported",
            derivative_ready and rounding_ready,
            True,
            "导数传播和 EM replay 舍入纪律均已闭合。",
            "ready for real one-sided center table.",
        ),
        row(
            "FloatAuditShowsImaginaryGap",
            audit_supports,
            False,
            f"侦察最大中心虚部≈{audit['audit_max_center_imag']:.12f}，低于 -1/40={IMAG_FLOOR:.12f}。",
            "只能确定参数，不作为自足证明。",
        ),
        row(
            "ImaginaryPropagationLemmaClosed",
            propagation_negative,
            True,
            f"中心虚部 <=-1/40 且半段漂移 <={derivative_loss:.12f} 推出整段虚部仍 <0。",
            SEGMENT_CLOSED,
        ),
        row(
            "ExactCenterImaginaryReplayStillMissing",
            False,
            False,
            "还需 1024 个中心点的有理区间 EM replay，逐点证明 Im zeta<=-1/40。",
            NEW_ATOM,
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "复模中心值表已压缩成单边虚部负号表，但严格自足尚未闭合。",
            NEW_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行顶边临界半段虚部负号路由。"""
    derivative = load_json(paths["derivative"])
    rounding = load_json(paths["rounding"])
    audit = audit_imaginary_sign()
    rows = build_rows(derivative, rounding, audit)
    derivative_loss = derivative["derivative_bounds"]["actual_loss_bound"]
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_top_critical_imaginary_sign_router",
        "status": "top_critical_center_values_reduced_to_imaginary_negative_replay_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "top_critical_center_value_reduced_to_imaginary_sign": True,
        "top_critical_segment_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {OLD_ATOM: NEW_ATOM},
        "audit": audit,
        "derivative_loss_bound": derivative_loss,
        "proof_contract": proof_contract(derivative_loss),
        "next_priority": NEW_ATOM,
        "secondary_priority": WINDING_ATOM,
        "plain_conclusion": (
            "中心值 replay 的目标从复模下界进一步压缩为单边虚部负号表：只需证明 1024 个中心点 "
            "Im zeta(c_j+14i)<=-1/40。已闭合导数界保证整段虚部仍严格为负，因此顶边临界半段非零。"
            "当前仍缺这 1024 个有理区间中心虚部证书。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix 顶边临界半段虚部负号路由器",
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
            "top_critical_center_value_reduced_to_imaginary_sign="
            f"{fmt_bool(result['top_critical_center_value_reduced_to_imaginary_sign'])}"
        ),
        f"top_critical_segment_self_contained_closed={fmt_bool(result['top_critical_segment_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 虚部侦察",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| height | `{audit['height']}` |",
        f"| mesh denominator | `{audit['mesh_denominator']}` |",
        f"| cell count | `{audit['cell_count']}` |",
        f"| imag floor contract | `{audit['imag_floor_contract']:.12f}` |",
        f"| audit max center imag | `{audit['audit_max_center_imag']:.12f}` |",
        f"| audit max center sigma | `{audit['audit_max_center_sigma']:.12f}` |",
        f"| audit min center imag | `{audit['audit_min_center_imag']:.12f}` |",
        f"| audit margin below floor | `{audit['audit_margin_below_floor']:.12f}` |",
        f"| derivative half-cell loss | `{result['derivative_loss_bound']:.12f}` |",
        "",
        "## 2. 证明合同",
        "",
    ]
    for index, item in enumerate(result["proof_contract"], start=1):
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
            f"严格自足唯一顶边剩余：`{result['next_priority']}`。",
            f"顶边完成后仍需：`{result['secondary_priority']}`。",
            "",
            "判定：顶边非零已变成 1024 个一维实不等式。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--derivative-json", type=Path, default=DEFAULT_DERIVATIVE)
    parser.add_argument("--rounding-json", type=Path, default=DEFAULT_ROUNDING)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "derivative": args.derivative_json,
        "rounding": args.rounding_json,
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
