#!/usr/bin/env python3
"""Prime Matrix 顶边临界半段单调端点压缩路由器。

用法示例：
  python3 experiments/prime_matrix_top_critical_monotone_endpoint_router.py

输出：
  docs/monograph/prime-matrix-top-critical-monotone-endpoint-router.json
  docs/monograph/prime-matrix-top-critical-monotone-endpoint-router.md
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

DEFAULT_PREVIOUS = MONO / "prime-matrix-top-critical-imaginary-sign-router.json"
DEFAULT_JSON = MONO / "prime-matrix-top-critical-monotone-endpoint-router.json"
DEFAULT_MD = MONO / "prime-matrix-top-critical-monotone-endpoint-router.md"

OLD_ATOM = "TopCriticalSegmentCenterImagNegativeEMReplayLedgerN32P8Mesh2048FloorMinus1Over40"
ENDPOINT_ATOM = "TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40"
DERIVATIVE_POSITIVE_ATOM = "TopCriticalImagDerivativePositiveLedgerT14HalfToOneFloor1Over16"
SEGMENT_CLOSED = "TopCriticalSegmentXiNonzeroClosedByMonotoneEndpointT14HalfToOne"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

HEIGHT = 14.0
ENDPOINT_SIGMA = 1.0
DERIVATIVE_FLOOR = 1.0 / 16.0
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


def eta_derivatives(s: complex, terms: int = 260) -> tuple[complex, complex, complex, complex]:
    """用 Euler 变换近似 zeta 及前三阶导数，仅作侦察审计。"""
    arrays = []
    for order in range(4):
        arrays.append(
            [((-math.log(n + 1)) ** order) * cmath.exp(-s * math.log(n + 1)) for n in range(terms + 1)]
        )
    sums = [0j, 0j, 0j, 0j]
    weight = 2.0
    for k in range(terms):
        for order in range(4):
            sums[order] += arrays[order][0] / weight
        for i in range(terms - k):
            for order in range(4):
                arrays[order][i] = arrays[order][i] - arrays[order][i + 1]
        weight *= 2.0
    log2 = math.log(2)
    two_power = cmath.exp((1 - s) * log2)
    denominator = 1 - two_power
    d1 = log2 * two_power
    d2 = -log2 * log2 * two_power
    d3 = log2**3 * two_power
    zeta = sums[0] / denominator
    zeta1 = (sums[1] - zeta * d1) / denominator
    zeta2 = (sums[2] - zeta * d2 - 2 * zeta1 * d1) / denominator
    zeta3 = (sums[3] - zeta * d3 - 3 * zeta1 * d2 - 3 * zeta2 * d1) / denominator
    return zeta, zeta1, zeta2, zeta3


def audit_monotonicity() -> dict[str, Any]:
    """扫描单调性和端点余量。"""
    endpoint_zeta, endpoint_derivative, endpoint_second, endpoint_third = eta_derivatives(ENDPOINT_SIGMA + HEIGHT * 1j)
    min_derivative_imag = float("inf")
    min_derivative_sigma = 0.0
    max_imag = -10.0
    max_imag_sigma = 0.0
    min_second_imag = float("inf")
    max_second_imag = -float("inf")
    min_third_imag = float("inf")
    for i in range(2001):
        sigma = 0.5 + 0.5 * i / 2000
        zeta, zeta1, zeta2, zeta3 = eta_derivatives(sigma + HEIGHT * 1j)
        if zeta1.imag < min_derivative_imag:
            min_derivative_imag = zeta1.imag
            min_derivative_sigma = sigma
        if zeta.imag > max_imag:
            max_imag = zeta.imag
            max_imag_sigma = sigma
        min_second_imag = min(min_second_imag, zeta2.imag)
        max_second_imag = max(max_second_imag, zeta2.imag)
        min_third_imag = min(min_third_imag, zeta3.imag)
    return {
        "height": HEIGHT,
        "endpoint_sigma": ENDPOINT_SIGMA,
        "imag_floor": IMAG_FLOOR,
        "derivative_floor": DERIVATIVE_FLOOR,
        "endpoint_imag": endpoint_zeta.imag,
        "endpoint_real": endpoint_zeta.real,
        "endpoint_derivative_imag": endpoint_derivative.imag,
        "endpoint_derivative_real": endpoint_derivative.real,
        "endpoint_second_imag": endpoint_second.imag,
        "endpoint_third_imag": endpoint_third.imag,
        "min_derivative_imag": min_derivative_imag,
        "min_derivative_sigma": min_derivative_sigma,
        "max_zeta_imag": max_imag,
        "max_zeta_imag_sigma": max_imag_sigma,
        "min_second_derivative_imag": min_second_imag,
        "max_second_derivative_imag": max_second_imag,
        "min_third_derivative_imag": min_third_imag,
        "endpoint_margin_below_imag_floor": IMAG_FLOOR - endpoint_zeta.imag,
        "derivative_margin_above_floor": min_derivative_imag - DERIVATIVE_FLOOR,
    }


def proof_contract() -> list[str]:
    """写出单调端点压缩证明合同。"""
    return [
        "证明端点不等式 Im zeta(1+14i)<=-1/40。",
        "证明全段导数不等式 Im d/dsigma zeta(sigma+14i)>=1/16。",
        "由导数正号，Im zeta(sigma+14i) 在 1/2<=sigma<=1 上递增，最大值在 sigma=1。",
        "因此整段 Im zeta<=Im zeta(1+14i)<=-1/40<0，顶边临界半段无零。",
        "这样 1024 个中心虚部表可被一个端点值 replay 和一个导数正号 replay 替代。",
    ]


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成单调端点压缩判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    imag_reduction_ready = previous.get("top_critical_center_value_reduced_to_imaginary_sign") is True
    audit_supports = audit["endpoint_imag"] < IMAG_FLOOR and audit["min_derivative_imag"] > DERIVATIVE_FLOOR
    compression_closed = active and guard and imag_reduction_ready
    return [
        row(
            "MonotoneEndpointGateActive",
            active,
            True,
            "上一层唯一剩余是 1024 个中心点虚部负号 replay。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只做解析证书压缩，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "FloatAuditSupportsMonotoneEndpoint",
            audit_supports,
            False,
            (
                f"侦察给端点虚部 {audit['endpoint_imag']:.12f}<-1/40，"
                f"导数虚部最小 {audit['min_derivative_imag']:.12f}>1/16。"
            ),
            "不能作为自足证明，只用于确定压缩方向。",
        ),
        row(
            "MonotoneEndpointLemmaClosed",
            compression_closed,
            True,
            "端点负号加全段导数正号推出整段虚部为负。",
            SEGMENT_CLOSED,
        ),
        row(
            "EndpointImagReplayStillMissing",
            False,
            False,
            "需用有理区间 EM replay 证明 Im zeta(1+14i)<=-1/40。",
            ENDPOINT_ATOM,
        ),
        row(
            "DerivativePositiveReplayStillMissing",
            False,
            False,
            "需用有理区间 EM replay 证明全段 Im zeta_sigma'(sigma+14i)>=1/16。",
            DERIVATIVE_POSITIVE_ATOM,
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "1024 中心负号表已压缩为端点负号和导数正号两个证书。",
            f"{ENDPOINT_ATOM} AND {DERIVATIVE_POSITIVE_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行单调端点压缩路由。"""
    previous = load_json(paths["previous"])
    audit = audit_monotonicity()
    rows = build_rows(previous, audit)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_top_critical_monotone_endpoint_router",
        "status": "top_center_imag_table_reduced_to_endpoint_and_derivative_positive_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "center_imag_table_compressed_to_monotone_endpoint": True,
        "top_critical_segment_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {
            OLD_ATOM: f"{ENDPOINT_ATOM} AND {DERIVATIVE_POSITIVE_ATOM}",
        },
        "audit": audit,
        "proof_contract": proof_contract(),
        "next_priority": DERIVATIVE_POSITIVE_ATOM,
        "secondary_priority": ENDPOINT_ATOM,
        "tertiary_priority": WINDING_ATOM,
        "plain_conclusion": (
            "1024 个中心虚部 replay 表已被压缩为更结构化的两个输入：端点 Im zeta(1+14i)<=-1/40，"
            "以及全段 Im zeta_sigma'(sigma+14i)>=1/16。侦察显示端点虚部约 -0.030678，"
            "导数虚部最小约 0.097214，余量足够；严格自足仍需这两个有理区间 replay 证书。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix 顶边临界半段单调端点压缩路由器",
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
            "center_imag_table_compressed_to_monotone_endpoint="
            f"{fmt_bool(result['center_imag_table_compressed_to_monotone_endpoint'])}"
        ),
        f"top_critical_segment_self_contained_closed={fmt_bool(result['top_critical_segment_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 单调侦察",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| endpoint imag | `{audit['endpoint_imag']:.12f}` |",
        f"| imag floor | `{audit['imag_floor']:.12f}` |",
        f"| endpoint margin below floor | `{audit['endpoint_margin_below_imag_floor']:.12f}` |",
        f"| min derivative imag | `{audit['min_derivative_imag']:.12f}` |",
        f"| derivative floor | `{audit['derivative_floor']:.12f}` |",
        f"| derivative margin above floor | `{audit['derivative_margin_above_floor']:.12f}` |",
        f"| min derivative sigma | `{audit['min_derivative_sigma']:.12f}` |",
        f"| max zeta imag sigma | `{audit['max_zeta_imag_sigma']:.12f}` |",
        f"| second derivative imag range | `[{audit['min_second_derivative_imag']:.12f}, {audit['max_second_derivative_imag']:.12f}]` |",
        f"| endpoint third derivative imag | `{audit['endpoint_third_imag']:.12f}` |",
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
            f"优先攻：`{result['next_priority']}`。",
            f"随后补：`{result['secondary_priority']}`。",
            f"顶边完成后仍需：`{result['tertiary_priority']}`。",
            "",
            "判定：1024 点表已降为单调性证书加一个端点证书。",
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
