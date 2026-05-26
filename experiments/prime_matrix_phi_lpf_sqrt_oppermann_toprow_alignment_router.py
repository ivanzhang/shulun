#!/usr/bin/env python3
"""审计 sqrt 常数门槛与 top-row Oppermann 左半窗的精确对齐。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_sqrt_oppermann_toprow_alignment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-router.json

输出：
  data/prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-ledger.json
  docs/monograph/prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-router.json
  docs/monograph/prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-router.md
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

SLUG = "prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SAMPLE_PRIMES = [3, 5, 11, 31, 101, 1009, 10007]
CONSTANTS = [
    ("C=1", Fraction(1, 1)),
    ("C=1.0001", Fraction(10001, 10000)),
    ("C=sqrt(2) lower bound", None),
    ("Legendre C=(2P-1)/P", None),
    ("C=2", Fraction(2, 1)),
]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-sqrt-constant-threshold-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json",
    DOCS / "prime-matrix-phi-lpf-sqrt-constant-threshold-router.md",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "PrimeIndexedOppermannLeftTopRowOrSharpCOneSqrtInputStillOpen "
    "AND LegendreWideSquareIntervalDoesNotImplyTopRow "
    "AND AnyFixedSqrtConstantGreaterThanOneHasLowerLeakStrip "
    "AND PointwisePsiAtSharpSqrtScaleOrAdmissibleSignedTypeIIFamilyStillOpen"
)


def is_prime(n: int) -> bool:
    """简单试除素性测试，样本规模很小。"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = math.isqrt(n)
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True


def count_primes(lo_exclusive: int, hi_exclusive: int) -> int:
    """统计开区间内素数数量。"""
    return sum(1 for n in range(lo_exclusive + 1, hi_exclusive) if is_prime(n))


def interval_sample(P: int) -> dict[str, Any]:
    """构造 top-row/Legendre 半窗样本。"""
    lower_left = (P - 1) * (P - 1)
    split = P * P - P
    square = P * P
    lower_leak_count = max(0, split - lower_left)
    top_count = max(0, square - split - 1)
    return {
        "P": P,
        "legendre_open_interval": f"({lower_left},{square})",
        "lower_leak_interval": f"({lower_left},{split}]",
        "top_row_interval": f"({split},{square})",
        "lower_leak_integer_count": lower_leak_count,
        "top_row_integer_count": top_count,
        "equal_half_counts": lower_leak_count == top_count == P - 1,
        "lower_leak_prime_count": count_primes(lower_left, split + 1),
        "top_row_prime_count": count_primes(split, square),
        "top_row_positive_in_sample": count_primes(split, square) > 0,
    }


def leak_length_for_constant(P: int, label: str, C: Fraction | None) -> dict[str, Any]:
    """计算 top row 下方的 C sqrt(P^2) 泄漏长度。"""
    if label == "C=sqrt(2) lower bound":
        # 用 C^2=2，只登记连续长度下界，不需要浮点精确开端。
        leak_floor = math.floor((math.sqrt(2) - 1) * P)
        return {
            "label": label,
            "C": "sqrt(2)",
            "top_row_is_isolated": False,
            "lower_leak_integer_count_at_least": leak_floor,
            "meaning": "positive fixed-proportion leakage below P^2-P",
        }
    if label == "Legendre C=(2P-1)/P":
        return {
            "label": label,
            "C": f"{2 * P - 1}/{P}",
            "top_row_is_isolated": False,
            "lower_leak_integer_count": P - 1,
            "meaning": "Legendre open square interval splits into two equal integer halves",
        }
    assert C is not None
    square = P * P
    split = square - P
    start_floor = math.floor(square - (C.numerator * P) / C.denominator)
    lower_leak_count = max(0, split - start_floor)
    return {
        "label": label,
        "C": f"{C.numerator}/{C.denominator}",
        "top_row_is_isolated": C <= 1,
        "lower_leak_integer_count": lower_leak_count,
        "meaning": "C=1 isolates top row; fixed C>1 creates lower leak strip",
    }


def sample_payload(P: int) -> dict[str, Any]:
    """构造单个 P 的完整样本。"""
    return {
        **interval_sample(P),
        "constant_leaks": [leak_length_for_constant(P, label, C) for label, C in CONSTANTS],
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
        "certificate_type": "prime_matrix_phi_lpf_sqrt_oppermann_toprow_alignment_router",
        "status": "sqrt_C_one_equals_prime_indexed_oppermann_left_toprow",
        "verified_date": "2026-05-26",
        "top_row_identity": "k=P-1 gives I_top=(P^2-P,P^2)",
        "C_one_right_endpoint_identity": "X=P^2 and [X-sqrt(X),X]=[P^2-P,P^2]",
        "prime_endpoint_note": "Both endpoints P^2-P and P^2 are composite, so any prime in the closed C=1 interval lies in the open top row.",
        "legendre_split_identity": "((P-1)^2,P^2)=((P-1)^2,P^2-P] union (P^2-P,P^2), with P-1 integers in each half.",
        "top_row_equals_prime_indexed_oppermann_left_half": True,
        "sqrt_C_one_right_endpoint_equivalent_to_top_row": True,
        "legendre_interval_splits_into_equal_lower_leak_and_target_halves": True,
        "legendre_wide_square_interval_implies_top_row": False,
        "fixed_C_greater_than_one_toprow_isolation": False,
        "known_unconditional_prime_indexed_oppermann_left_available": False,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "samples": [sample_payload(P) for P in SAMPLE_PRIMES],
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The top strict row is exactly the prime-indexed Oppermann left half. "
            "A C=1 right-endpoint square-root theorem at X=P^2 is precisely the needed "
            "top-row input, while Legendre's wider interval splits into a lower leak half "
            "and the target half. Thus Legendre-scale or any fixed C>1 square-root input "
            "cannot by itself close the row/column theorem."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF sqrt-Oppermann top-row alignment 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 精确对齐",
        "",
        "```text",
        payload["top_row_identity"],
        payload["C_one_right_endpoint_identity"],
        payload["prime_endpoint_note"],
        payload["legendre_split_identity"],
        "```",
        "",
        "核心判定：",
        "",
        "```text",
        "top_row_equals_prime_indexed_oppermann_left_half="
        f"{fmt_bool(payload['top_row_equals_prime_indexed_oppermann_left_half'])}",
        "sqrt_C_one_right_endpoint_equivalent_to_top_row="
        f"{fmt_bool(payload['sqrt_C_one_right_endpoint_equivalent_to_top_row'])}",
        "legendre_interval_splits_into_equal_lower_leak_and_target_halves="
        f"{fmt_bool(payload['legendre_interval_splits_into_equal_lower_leak_and_target_halves'])}",
        f"legendre_wide_square_interval_implies_top_row={fmt_bool(payload['legendre_wide_square_interval_implies_top_row'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 样本半窗",
        "",
        "| P | lower leak count | top row count | lower primes | top primes | equal halves |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for sample in payload["samples"]:
        lines.append(
            "| {P} | {lower} | {top} | {lp} | {tp} | {eq} |".format(
                P=sample["P"],
                lower=sample["lower_leak_integer_count"],
                top=sample["top_row_integer_count"],
                lp=sample["lower_leak_prime_count"],
                tp=sample["top_row_prime_count"],
                eq=fmt_bool(sample["equal_half_counts"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 常数泄漏样本",
            "",
            "| P | C label | top row isolated | lower leak count | meaning |",
            "| ---: | --- | --- | ---: | --- |",
        ]
    )
    for sample in payload["samples"]:
        for leak in sample["constant_leaks"]:
            count = leak.get("lower_leak_integer_count", leak.get("lower_leak_integer_count_at_least", 0))
            lines.append(
                "| {P} | {label} | {iso} | {count} | {meaning} |".format(
                    P=sample["P"],
                    label=leak["label"],
                    iso=fmt_bool(leak["top_row_is_isolated"]),
                    count=count,
                    meaning=leak["meaning"],
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
        "sqrt_C_one_right_endpoint_equivalent_to_top_row="
        f"{fmt_bool(payload['sqrt_C_one_right_endpoint_equivalent_to_top_row'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
