#!/usr/bin/env python3
"""Prime Matrix 顶边临界半段二阶导数负号压缩路由器。

用法示例：
  python3 experiments/prime_matrix_top_critical_second_derivative_reduction_router.py

输出：
  docs/monograph/prime-matrix-top-critical-second-derivative-reduction-router.json
  docs/monograph/prime-matrix-top-critical-second-derivative-reduction-router.md
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

DEFAULT_PREVIOUS = MONO / "prime-matrix-top-critical-derivative-positive-reduction-router.json"
DEFAULT_JSON = MONO / "prime-matrix-top-critical-second-derivative-reduction-router.json"
DEFAULT_MD = MONO / "prime-matrix-top-critical-second-derivative-reduction-router.md"

OLD_ATOM = "TopCriticalImagSecondDerivativeNegativeLedgerT14HalfToOneFloorMinus1Over8"
ENDPOINT_SECOND_ATOM = "TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8"
THIRD_POSITIVE_ATOM = "TopCriticalImagThirdDerivativePositiveLedgerT14HalfToOneFloor1Over8"
ENDPOINT_DERIVATIVE_ATOM = "TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16"
ENDPOINT_IMAG_ATOM = "TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

HEIGHT = 14.0
SECOND_CEILING = -1.0 / 8.0
THIRD_FLOOR = 1.0 / 8.0


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


def zeta_derivatives(s: complex, terms: int = 260) -> tuple[complex, complex, complex, complex]:
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


def audit_second_reduction() -> dict[str, Any]:
    """扫描二阶负号压缩余量。"""
    endpoint = zeta_derivatives(1.0 + HEIGHT * 1j)
    min_second = float("inf")
    min_second_sigma = 0.0
    max_second = -float("inf")
    max_second_sigma = 0.0
    min_third = float("inf")
    min_third_sigma = 0.0
    max_third = -float("inf")
    max_third_sigma = 0.0
    for i in range(2001):
        sigma = 0.5 + 0.5 * i / 2000
        _, _, zeta2, zeta3 = zeta_derivatives(sigma + HEIGHT * 1j)
        if zeta2.imag < min_second:
            min_second = zeta2.imag
            min_second_sigma = sigma
        if zeta2.imag > max_second:
            max_second = zeta2.imag
            max_second_sigma = sigma
        if zeta3.imag < min_third:
            min_third = zeta3.imag
            min_third_sigma = sigma
        if zeta3.imag > max_third:
            max_third = zeta3.imag
            max_third_sigma = sigma
    return {
        "height": HEIGHT,
        "second_ceiling": SECOND_CEILING,
        "third_floor": THIRD_FLOOR,
        "endpoint_second_imag": endpoint[2].imag,
        "endpoint_third_imag": endpoint[3].imag,
        "min_second_derivative_imag": min_second,
        "min_second_derivative_sigma": min_second_sigma,
        "max_second_derivative_imag": max_second,
        "max_second_derivative_sigma": max_second_sigma,
        "min_third_derivative_imag": min_third,
        "min_third_derivative_sigma": min_third_sigma,
        "max_third_derivative_imag": max_third,
        "max_third_derivative_sigma": max_third_sigma,
        "endpoint_second_margin": SECOND_CEILING - endpoint[2].imag,
        "third_positive_margin": min_third - THIRD_FLOOR,
    }


def proof_contract() -> list[str]:
    """写出二阶负号压缩证明合同。"""
    return [
        "证明端点二阶不等式 Im zeta''(1+14i)<=-1/8。",
        "证明全段三阶导数不等式 Im zeta'''(sigma+14i)>=1/8。",
        "由三阶导数正号，Im zeta''(sigma+14i) 随 sigma 递增，最大值在 sigma=1。",
        "因此全段 Im zeta''(sigma+14i)<=Im zeta''(1+14i)<=-1/8。",
    ]


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成二阶负号压缩判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    derivative_ready = previous.get("derivative_positive_reduced_to_endpoint_and_second_negative") is True
    audit_supports = audit["endpoint_second_imag"] < SECOND_CEILING and audit["min_third_derivative_imag"] > THIRD_FLOOR
    compression_closed = active and guard and derivative_ready
    return [
        row(
            "SecondDerivativeGateActive",
            active,
            True,
            "上一层把导数正号压成端点导数正号和全段二阶负号。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只压缩低高度解析证书，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "FloatAuditSupportsThirdDerivativeRoute",
            audit_supports,
            False,
            (
                f"侦察端点二阶虚部 {audit['endpoint_second_imag']:.12f}<-1/8，"
                f"三阶导数虚部最小 {audit['min_third_derivative_imag']:.12f}>1/8。"
            ),
            "不能作为自足证明，只用于确定压缩方向。",
        ),
        row(
            "SecondNegativeFromEndpointAndThirdPositive",
            compression_closed,
            True,
            "端点二阶负号加三阶正号推出全段二阶负号。",
            OLD_ATOM,
        ),
        row(
            "EndpointSecondReplayStillMissing",
            False,
            False,
            "需用有理区间 EM replay 证明 Im zeta''(1+14i)<=-1/8。",
            ENDPOINT_SECOND_ATOM,
        ),
        row(
            "ThirdDerivativePositiveStillMissing",
            False,
            False,
            "需用有理区间 EM replay 或 Taylor 符号梯证明全段 Im zeta'''>=1/8。",
            THIRD_POSITIVE_ATOM,
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "二阶负号账本已压缩为端点二阶负号和三阶导数正号。",
            f"{ENDPOINT_SECOND_ATOM} AND {THIRD_POSITIVE_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行二阶负号压缩路由。"""
    previous = load_json(paths["previous"])
    audit = audit_second_reduction()
    rows = build_rows(previous, audit)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_top_critical_second_derivative_reduction_router",
        "status": "top_second_derivative_negative_reduced_to_endpoint_second_and_third_positive_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "second_derivative_negative_reduced_to_endpoint_and_third_positive": True,
        "top_critical_segment_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {
            OLD_ATOM: f"{ENDPOINT_SECOND_ATOM} AND {THIRD_POSITIVE_ATOM}",
        },
        "audit": audit,
        "proof_contract": proof_contract(),
        "next_priority": THIRD_POSITIVE_ATOM,
        "secondary_priority": ENDPOINT_SECOND_ATOM,
        "tertiary_priority": ENDPOINT_DERIVATIVE_ATOM,
        "quaternary_priority": ENDPOINT_IMAG_ATOM,
        "downstream_priority": WINDING_ATOM,
        "plain_conclusion": (
            "二阶负号输入已进一步压缩：只需端点 Im zeta''(1+14i)<=-1/8 和全段 "
            "Im zeta'''(sigma+14i)>=1/8。侦察显示端点二阶约 -0.152777，三阶导数最小约 0.200258。"
            "严格自足仍需这两个 replay/符号证书。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix 顶边临界半段二阶导数负号压缩路由器",
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
            "second_derivative_negative_reduced_to_endpoint_and_third_positive="
            f"{fmt_bool(result['second_derivative_negative_reduced_to_endpoint_and_third_positive'])}"
        ),
        f"top_critical_segment_self_contained_closed={fmt_bool(result['top_critical_segment_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 侦察余量",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| endpoint second derivative imag | `{audit['endpoint_second_imag']:.12f}` |",
        f"| second ceiling | `{audit['second_ceiling']:.12f}` |",
        f"| endpoint second margin | `{audit['endpoint_second_margin']:.12f}` |",
        f"| max second derivative imag | `{audit['max_second_derivative_imag']:.12f}` |",
        f"| max second derivative sigma | `{audit['max_second_derivative_sigma']:.12f}` |",
        f"| min third derivative imag | `{audit['min_third_derivative_imag']:.12f}` |",
        f"| third floor | `{audit['third_floor']:.12f}` |",
        f"| third positive margin | `{audit['third_positive_margin']:.12f}` |",
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
            f"再补端点导数：`{result['tertiary_priority']}`。",
            f"再补端点虚部：`{result['quaternary_priority']}`。",
            f"顶边完成后仍需：`{result['downstream_priority']}`。",
            "",
            "判定：二阶负号已降为三阶正号和端点二阶负号。",
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
