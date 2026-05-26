#!/usr/bin/env python3
"""审计 strict row 中平方根尺度短区间输入的常数门槛。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_sqrt_constant_threshold_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.json

输出：
  data/prime-matrix-phi-lpf-sqrt-constant-threshold-ledger.json
  docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.json
  docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.md
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-sqrt-constant-threshold"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SAMPLE_P_VALUES = [10**6 + 3, 10**12 + 39, 10**24 + 39]
CONSTANT_INPUTS = [
    {
        "name": "C=1/2",
        "C_squared": Fraction(1, 4),
        "meaning": "stronger than the sharp square-root row length",
    },
    {
        "name": "C=1",
        "C_squared": Fraction(1, 1),
        "meaning": "sharp aligned square-root threshold",
    },
    {
        "name": "C=1.0001",
        "C_squared": Fraction(10001 * 10001, 10000 * 10000),
        "meaning": "near-sharp but still larger than one",
    },
    {
        "name": "C=sqrt(2)",
        "C_squared": Fraction(2, 1),
        "meaning": "fixed constant above one",
    },
    {
        "name": "C=2",
        "C_squared": Fraction(4, 1),
        "meaning": "wide square-root input with constant loss",
    },
]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-theta-short-interval-zero-density-band-router.json",
    DOCS / "prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-audit.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "SqrtScaleConstantAtMostOnePointwiseInputWouldCloseStrictRows "
    "AND AnyFixedSqrtConstantGreaterThanOneLeavesPositiveDensityTopBand "
    "AND PrimePowerTailSublinearThresholdClosed "
    "AND PointwisePsiAtSharpSqrtScaleOrAdmissibleSignedTypeIIFamilyStillOpen"
)


def floor_fraction_div(P: int, denominator: Fraction) -> int:
    """返回 floor(P / denominator)。"""
    return (P * denominator.denominator) // denominator.numerator


def row_counts(P: int, C_squared: Fraction) -> dict[str, Any]:
    """计算左端点和右端点嵌入可闭合的 strict row 数量。"""
    strict_count = P - 1

    # 左端点前进输入：(kP, kP + C sqrt(kP)] 落入 row 需要 C^2 k <= P。
    left_max_k = floor_fraction_div(P, C_squared)
    left_closed = max(0, min(strict_count, left_max_k))

    # 右端点后退输入：[(k+1)P - C sqrt((k+1)P), (k+1)P] 落入 row
    # 需要 C^2 (k+1) <= P。等号时端点是合数，仍可用于开 row。
    right_max_k_plus_one = floor_fraction_div(P, C_squared)
    right_closed = max(0, min(strict_count, right_max_k_plus_one - 1))

    return {
        "P": P,
        "strict_row_count": strict_count,
        "left_endpoint_closed_rows": left_closed,
        "left_endpoint_closed_fraction": left_closed / strict_count,
        "left_endpoint_top_band_fraction": 1.0 - left_closed / strict_count,
        "right_endpoint_closed_rows": right_closed,
        "right_endpoint_closed_fraction": right_closed / strict_count,
        "right_endpoint_top_band_fraction": 1.0 - right_closed / strict_count,
    }


def constant_payload(item: dict[str, Any]) -> dict[str, Any]:
    """构造单个常数的审计数据。"""
    C_squared = item["C_squared"]
    closes_all_asymptotically = C_squared <= 1
    top_band_density_if_gt_one = (
        0.0 if closes_all_asymptotically else 1.0 - float(Fraction(1, 1) / C_squared)
    )
    return {
        "name": item["name"],
        "C_squared": f"{C_squared.numerator}/{C_squared.denominator}",
        "C_squared_decimal": C_squared.numerator / C_squared.denominator,
        "meaning": item["meaning"],
        "closes_all_strict_rows_if_pointwise_input_available": closes_all_asymptotically,
        "leaves_positive_density_top_band": not closes_all_asymptotically,
        "asymptotic_closed_density_if_gt_one": (
            1.0 if closes_all_asymptotically else float(Fraction(1, 1) / C_squared)
        ),
        "asymptotic_top_band_density_if_gt_one": top_band_density_if_gt_one,
        "samples": [row_counts(P, C_squared) for P in SAMPLE_P_VALUES],
    }


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    return {
        "certificate_type": "prime_matrix_phi_lpf_sqrt_constant_threshold_router",
        "status": "sqrt_scale_constant_one_is_sharp_for_strict_rows",
        "verified_date": "2026-05-26",
        "strict_row": "I_{P,k}=(kP,(k+1)P), 1<=k<P",
        "left_endpoint_embedding": "x=kP and (x, x+C*sqrt(x)] lies in row if C^2*k<=P",
        "right_endpoint_embedding": "X=(k+1)P and [X-C*sqrt(X), X] lies in row if C^2*(k+1)<=P",
        "endpoint_composite_note": "Equality at C=1 is harmless because kP and (k+1)P are composite row endpoints.",
        "constant_threshold_law": "C<=1 would close all sufficiently large strict rows; every fixed C>1 leaves top-band density 1-1/C^2.",
        "sqrt_constant_one_pointwise_input_would_close_all_strict_rows": True,
        "fixed_constant_greater_than_one_leaves_positive_density_top_band": True,
        "known_unconditional_C_at_most_one_pointwise_input_available": False,
        "theta_half_constant_gate_identified": True,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "constant_inputs": [constant_payload(item) for item in CONSTANT_INPUTS],
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "After fixed theta>1/2 inputs have been routed to zero-density low rows, "
            "the pure short-interval lane has a sharp remaining constant gate at theta=1/2. "
            "A pointwise C*sqrt(x) theorem with C<=1 would close all large strict rows, "
            "but any fixed C>1 still leaves a positive-density top band. No known "
            "unconditional input in the current corpus supplies the C<=1 pointwise theorem."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF sqrt constant threshold 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 平方根常数门槛",
        "",
        "```text",
        payload["strict_row"],
        payload["left_endpoint_embedding"],
        payload["right_endpoint_embedding"],
        payload["endpoint_composite_note"],
        payload["constant_threshold_law"],
        "```",
        "",
        "核心判定：",
        "",
        "```text",
        "sqrt_constant_one_pointwise_input_would_close_all_strict_rows="
        f"{fmt_bool(payload['sqrt_constant_one_pointwise_input_would_close_all_strict_rows'])}",
        "fixed_constant_greater_than_one_leaves_positive_density_top_band="
        f"{fmt_bool(payload['fixed_constant_greater_than_one_leaves_positive_density_top_band'])}",
        "known_unconditional_C_at_most_one_pointwise_input_available="
        f"{fmt_bool(payload['known_unconditional_C_at_most_one_pointwise_input_available'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        "```",
        "",
        "## 2. 常数对照表",
        "",
        "| input | C^2 | closes all if input available | top-band density | meaning |",
        "| --- | ---: | --- | ---: | --- |",
    ]
    for item in payload["constant_inputs"]:
        lines.append(
            "| {name} | {c2} | {closed} | {top:.9f} | {meaning} |".format(
                name=item["name"],
                c2=item["C_squared"],
                closed=fmt_bool(item["closes_all_strict_rows_if_pointwise_input_available"]),
                top=item["asymptotic_top_band_density_if_gt_one"],
                meaning=item["meaning"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 尺度样本",
            "",
            "| input | P | left closed fraction | right closed fraction | right top-band fraction |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in payload["constant_inputs"]:
        for sample in item["samples"]:
            lines.append(
                "| {name} | {P} | {left:.9f} | {right:.9f} | {top:.9f} |".format(
                    name=item["name"],
                    P=sample["P"],
                    left=sample["left_endpoint_closed_fraction"],
                    right=sample["right_endpoint_closed_fraction"],
                    top=sample["right_endpoint_top_band_fraction"],
                )
            )

    lines.extend(
        [
            "",
            "## 4. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in payload["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(
        "sqrt_constant_one_pointwise_input_would_close_all_strict_rows="
        f"{fmt_bool(payload['sqrt_constant_one_pointwise_input_would_close_all_strict_rows'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
