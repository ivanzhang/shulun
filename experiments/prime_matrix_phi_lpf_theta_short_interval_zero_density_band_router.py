#!/usr/bin/env python3
"""审计任意固定 theta>1/2 短区间输入在 strict rows 中只闭合零密度低行带。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_theta_short_interval_zero_density_band_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-theta-short-interval-zero-density-band-router.json

输出：
  data/prime-matrix-phi-lpf-theta-short-interval-zero-density-band-ledger.json
  docs/monograph/prime-matrix-phi-lpf-theta-short-interval-zero-density-band-router.json
  docs/monograph/prime-matrix-phi-lpf-theta-short-interval-zero-density-band-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-theta-short-interval-zero-density-band"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SAMPLE_POWERS = [10**6, 10**12, 10**24]
THETA_INPUTS = [
    {
        "name": "Baker-Harman-Pintz 2001",
        "theta": Fraction(21, 40),
        "source": "classical pointwise short-interval exponent 0.525",
    },
    {
        "name": "Runbo Li arXiv:2308.04458 v8",
        "theta": Fraction(13, 25),
        "source": "https://arxiv.org/abs/2308.04458",
    },
    {
        "name": "Guth-Maynard/Hieu scale representative",
        "theta": Fraction(17, 30),
        "source": "zero-density/AP short-interval PNT scale, still above 1/2",
    },
    {
        "name": "Hypothetical theta=0.5001",
        "theta": Fraction(5001, 10000),
        "source": "near-half fixed exponent stress test",
    },
]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-audit.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "AllFixedThetaGreaterThanHalfShortIntervalInputsCloseOnlyZeroDensityLowRows "
    "AND DensityOneTopBandStillRequiresThetaHalfPointwisePsiOrStructuralParityBreak "
    "AND PrimePowerTailSublinearThresholdClosed "
    "AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen"
)


def covered_exponent(theta: Fraction) -> Fraction:
    """返回 alpha=(1-theta)/theta。"""
    return Fraction(theta.denominator - theta.numerator, theta.numerator)


def covered_rows_approx(P: int, theta: Fraction) -> float:
    """短区间右端点嵌入可覆盖的低行数量近似。"""
    alpha = covered_exponent(theta)
    return P ** (alpha.numerator / alpha.denominator)


def theta_payload(item: dict[str, Any]) -> dict[str, Any]:
    """构造单个 theta 的审计数据。"""
    theta = item["theta"]
    alpha = covered_exponent(theta)
    samples = []
    for P in SAMPLE_POWERS:
        closed = covered_rows_approx(P, theta)
        fraction = closed / P
        samples.append(
            {
                "P": P,
                "covered_rows_approx": closed,
                "covered_fraction": fraction,
                "top_band_fraction": 1.0 - fraction,
            }
        )
    return {
        "name": item["name"],
        "theta": f"{theta.numerator}/{theta.denominator}",
        "theta_decimal": theta.numerator / theta.denominator,
        "covered_row_exponent": f"{alpha.numerator}/{alpha.denominator}",
        "covered_row_exponent_decimal": alpha.numerator / alpha.denominator,
        "closed_rows_density_tends_zero": alpha < 1,
        "top_band_density_tends_one": alpha < 1,
        "source": item["source"],
        "samples": samples,
    }


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    payloads = [theta_payload(item) for item in THETA_INPUTS]
    return {
        "certificate_type": "prime_matrix_phi_lpf_theta_short_interval_zero_density_band_router",
        "status": "fixed_theta_gt_half_short_intervals_close_only_zero_density_low_rows",
        "verified_date": "2026-05-26",
        "row_interval": "I_{P,k}=(kP,(k+1)P), integers kP<n<(k+1)P",
        "right_endpoint_embedding": "X=(k+1)P and X^theta<P",
        "general_condition": "k+1 < P^((1-theta)/theta), constants only change prefactors",
        "density_law": "for every fixed theta>1/2, P^((1-theta)/theta)/(P-1)->0",
        "all_fixed_theta_gt_half_close_only_zero_density_low_rows": True,
        "theta_half_identified_as_short_interval_lane_threshold": True,
        "density_one_top_band_remains_for_all_fixed_theta_gt_half": True,
        "closes_row_column_unconditionally": False,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "theta_inputs": payloads,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The Runbo Li bridge is the best current pointwise short-interval "
            "low-row input, but the phenomenon is general: any fixed exponent "
            "theta>1/2 embeds into only P^((1-theta)/theta) low rows, a zero-density "
            "set of the P strict rows. Thus ordinary fixed-exponent short-interval "
            "progress cannot close the row/column theorem unless it reaches the "
            "theta=1/2 scale or is supplemented by a structural top-band parity break."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF theta short-interval zero-density band 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 一般嵌入律",
        "",
        "对 strict row 取右端点短区间：",
        "",
        "```text",
        payload["row_interval"],
        payload["right_endpoint_embedding"],
        payload["general_condition"],
        payload["density_law"],
        "```",
        "",
        "核心判定：",
        "",
        "```text",
        "all_fixed_theta_gt_half_close_only_zero_density_low_rows="
        f"{fmt_bool(payload['all_fixed_theta_gt_half_close_only_zero_density_low_rows'])}",
        "theta_half_identified_as_short_interval_lane_threshold="
        f"{fmt_bool(payload['theta_half_identified_as_short_interval_lane_threshold'])}",
        "density_one_top_band_remains_for_all_fixed_theta_gt_half="
        f"{fmt_bool(payload['density_one_top_band_remains_for_all_fixed_theta_gt_half'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        "```",
        "",
        "## 2. theta 对照表",
        "",
        "| input | theta | covered exponent | zero-density low rows | source |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    for item in payload["theta_inputs"]:
        lines.append(
            "| {name} | {theta} | {alpha} | {zero} | {source} |".format(
                name=item["name"],
                theta=item["theta"],
                alpha=item["covered_row_exponent"],
                zero=fmt_bool(item["closed_rows_density_tends_zero"]),
                source=item["source"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 尺度样本",
            "",
            "| input | P | covered rows approx | covered fraction | top-band fraction |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in payload["theta_inputs"]:
        for sample in item["samples"]:
            lines.append(
                "| {name} | {P} | {rows:.3f} | {covered:.9f} | {top:.9f} |".format(
                    name=item["name"],
                    P=sample["P"],
                    rows=sample["covered_rows_approx"],
                    covered=sample["covered_fraction"],
                    top=sample["top_band_fraction"],
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
        "all_fixed_theta_gt_half_close_only_zero_density_low_rows="
        f"{fmt_bool(payload['all_fixed_theta_gt_half_close_only_zero_density_low_rows'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
