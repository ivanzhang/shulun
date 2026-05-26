#!/usr/bin/env python3
"""审计 Oppermann top-row 子核不能单独推出全部 strict rows。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_oppermann_subcore_not_full_closure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-router.json

输出：
  data/prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-ledger.json
  docs/monograph/prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-router.json
  docs/monograph/prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-oppermann-subcore-not-full-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SAMPLE_PRIMES = [3, 5, 11, 31, 101, 1009]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-router.json",
    DOCS / "prime-matrix-phi-lpf-sqrt-constant-threshold-router.json",
    DOCS / "prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json",
    DOCS / "prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "TopRowOppermannLeftIsNecessarySubcoreNotFullClosure "
    "AND FullRowsRequireGapBoundHkPLessThanPForEveryK "
    "AND LPFPhiExactCountsRemainUnsignedParityBlind "
    "AND PointwisePsiAtSharpSqrtScaleOrAdmissibleSignedTypeIIFamilyStillOpen"
)


def sieve(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    p = 2
    while p * p <= limit:
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
        p += 1
    return flags


def prefix_counts(flags: bytearray) -> list[int]:
    """构造 pi(n) 前缀表。"""
    prefix: list[int] = [0] * len(flags)
    total = 0
    for i, is_prime in enumerate(flags):
        total += int(is_prime)
        prefix[i] = total
    return prefix


def prime_count(prefix: list[int], lo_exclusive: int, hi_exclusive: int) -> int:
    """统计开区间内素数个数。"""
    if hi_exclusive <= lo_exclusive + 1:
        return 0
    return prefix[hi_exclusive - 1] - prefix[lo_exclusive]


def sample_payload(P: int) -> dict[str, Any]:
    """构造单个 P 的 strict-row/top-row 对照样本。"""
    flags = sieve(P * P + P)
    prefix = prefix_counts(flags)

    row_prime_counts = [
        prime_count(prefix, k * P, (k + 1) * P) for k in range(1, P)
    ]
    rows_with_prime = sum(1 for count in row_prime_counts if count > 0)
    first_zero_row = next((k for k, count in enumerate(row_prime_counts, start=1) if count == 0), None)

    # 中文注释：h(kP) 是从左端点 kP 到下一个素数的距离；行正性等价于 h(kP)<P。
    gap_distances: list[int] = []
    for k in range(1, P):
        x = k * P
        y = x + 1
        while y < len(flags) and not flags[y]:
            y += 1
        gap_distances.append(y - x)

    return {
        "P": P,
        "strict_row_count": P - 1,
        "top_row_index": P - 1,
        "top_row_interval": f"({P * P - P},{P * P})",
        "top_row_prime_count": row_prime_counts[-1],
        "top_row_oppermann_left_positive_in_sample": row_prime_counts[-1] > 0,
        "top_input_rows_covered_by_containment": 1,
        "top_input_coverage_fraction": 1.0 / (P - 1),
        "rows_with_prime_in_sample": rows_with_prime,
        "all_rows_positive_in_sample": rows_with_prime == P - 1,
        "first_zero_row_in_sample": first_zero_row,
        "max_h_kP_in_sample": max(gap_distances),
        "all_h_kP_less_than_P_in_sample": max(gap_distances) < P,
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
        "certificate_type": "prime_matrix_phi_lpf_oppermann_subcore_not_full_closure_router",
        "status": "top_row_oppermann_left_is_necessary_but_not_sufficient",
        "verified_date": "2026-05-26",
        "strict_row_statement": "For each prime P, strict-row positivity asks pi((k+1)P-1)-pi(kP)>=1 for every 1<=k<P.",
        "top_row_statement": "The top row k=P-1 is pi(P^2-1)-pi(P^2-P)>=1, i.e. prime-indexed Oppermann-left.",
        "gap_equivalence": "All strict rows are positive iff h(kP)<P for every 1<=k<P, where h(x)=next_prime_after(x)-x.",
        "top_row_gap_equivalence": "The top row alone is h(P^2-P)<P.",
        "row_column_strict_positivity_implies_toprow": True,
        "top_row_input_alone_closes_all_strict_rows": False,
        "top_row_input_is_necessary_not_sufficient": True,
        "all_rows_equivalent_to_prime_gap_bound_h_kP_less_than_P": True,
        "top_row_only_equivalent_to_prime_gap_bound_h_P2_minus_P_less_than_P": True,
        "legendre_or_C_gt_one_still_not_full_closure": True,
        "lpf_phi_exact_bucket_formula_corrected_but_unsigned": True,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "samples": [sample_payload(P) for P in SAMPLE_PRIMES],
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The prime-indexed Oppermann-left top row is a necessary subcore of "
            "full row-column strict positivity, because it is exactly the k=P-1 row. "
            "It is not a full closure route by itself: under the containment embedding "
            "it covers only that single row, whereas the full theorem requires "
            "h(kP)<P for every 1<=k<P or a structural signed Type-II/trace family. "
            "Corrected LPF/Phi bucket identities remain exact unsigned counts and do "
            "not supply that signed prime-emission mechanism."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF Oppermann subcore not-full-closure 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 逻辑边界",
        "",
        "```text",
        payload["strict_row_statement"],
        payload["top_row_statement"],
        payload["gap_equivalence"],
        payload["top_row_gap_equivalence"],
        "```",
        "",
        "核心判定：",
        "",
        "```text",
        "row_column_strict_positivity_implies_toprow="
        f"{fmt_bool(payload['row_column_strict_positivity_implies_toprow'])}",
        "top_row_input_alone_closes_all_strict_rows="
        f"{fmt_bool(payload['top_row_input_alone_closes_all_strict_rows'])}",
        "top_row_input_is_necessary_not_sufficient="
        f"{fmt_bool(payload['top_row_input_is_necessary_not_sufficient'])}",
        "all_rows_equivalent_to_prime_gap_bound_h_kP_less_than_P="
        f"{fmt_bool(payload['all_rows_equivalent_to_prime_gap_bound_h_kP_less_than_P'])}",
        "row_column_unconditional_closed="
        f"{fmt_bool(payload['row_column_unconditional_closed'])}",
        "phi_lpf_parity_barrier_globally_broken="
        f"{fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        "```",
        "",
        "## 2. 有限样本",
        "",
        "| P | strict rows | rows covered by top input | coverage fraction | sample rows with prime | top primes | max h(kP) | all h(kP)<P |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for sample in payload["samples"]:
        lines.append(
            "| {P} | {rows} | {covered} | {frac:.9f} | {with_prime} | {top} | {gap} | {all_gap} |".format(
                P=sample["P"],
                rows=sample["strict_row_count"],
                covered=sample["top_input_rows_covered_by_containment"],
                frac=sample["top_input_coverage_fraction"],
                with_prime=sample["rows_with_prime_in_sample"],
                top=sample["top_row_prime_count"],
                gap=sample["max_h_kP_in_sample"],
                all_gap=fmt_bool(sample["all_h_kP_less_than_P_in_sample"]),
            )
        )

    lines.extend(
        [
            "",
            "样本列只检验实现与等价关系；全局闭合仍需要逐行 `h(kP)<P`，不能由单个 top row 输入替代。",
            "",
            "## 3. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 4. 依赖哈希",
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
        "top_row_input_alone_closes_all_strict_rows="
        f"{fmt_bool(payload['top_row_input_alone_closes_all_strict_rows'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
