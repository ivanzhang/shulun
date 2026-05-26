#!/usr/bin/env python3
"""LPF 修正后，把三命题突破路线重新路由到 signed trace/Type-II 门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_corrected_lpf_signed_trace_breakthrough_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.json

输出：
  data/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-ledger.json
  docs/monograph/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.json
  docs/monograph/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json",
    DOCS / "prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json",
    DOCS / "prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json",
    DOCS / "prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.json",
    DOCS / "prime-matrix-phi-lpf-theta-short-interval-zero-density-band-router.json",
    DOCS / "prime-matrix-phi-lpf-sqrt-constant-threshold-router.json",
    DOCS / "prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-router.json",
    DOCS / "prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "CorrectedLPFExactCountsAndPeriodicErrorsDoNotGivePrimeEmission "
    "AND PureShortIntervalOrTopRowInputsDoNotCloseAllRows "
    "AND FastestPrimeMatrixRouteRequiresSignedTraceOrTypeIIFamily "
    "AND UniformAdjacentRunCancellationOrNamedPDECSAEStillOpen"
)


EXTERNAL_INPUTS = [
    {
        "name": "Runbo Li short intervals",
        "url": "https://arxiv.org/abs/2308.04458",
        "input_signature": "ordinary prime in [x-x^theta,x], theta=13/25",
        "usable_after": "strict row containment with k+1<P^(12/13)",
        "current_blocker": "zero-density low rows only; top band still needs sqrt-scale pointwise input",
        "direct_close": False,
    },
    {
        "name": "Runbo Li large-modulus AP / Harman sieve",
        "url": "https://arxiv.org/abs/2602.20917",
        "input_signature": "average large-modulus/AP distribution input",
        "usable_after": "project weights are promoted to an admissible averaged AP family",
        "current_blocker": "row-column target is pointwise at P^2, not merely averaged",
        "direct_close": False,
    },
    {
        "name": "Milicevic-Qin-Wu Kloosterman bilinear sums",
        "url": "https://arxiv.org/abs/2511.07550",
        "input_signature": "bilinear Kloosterman-type family",
        "usable_after": "moving Beatty numerator becomes a genuine two-variable Kloosterman family",
        "current_blocker": "no admissible two-variable trace family has been constructed from LPF buckets",
        "direct_close": False,
    },
    {
        "name": "Pascadi composite-modulus Type-II",
        "url": "https://arxiv.org/abs/2511.08445",
        "input_signature": "composite-modulus Type-II sums with admissible coefficients",
        "usable_after": "terminal/LPF weights are converted into well-factorable signed coefficients",
        "current_blocker": "unsigned LPF ownership counts are not Type-II coefficients",
        "direct_close": False,
    },
    {
        "name": "Wright trilinear Kloosterman fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "input_signature": "trilinear Kloosterman-fraction convolution",
        "usable_after": "terminal payload is upgraded to a trilinear convolution with equidistributed beta sequence",
        "current_blocker": "current payload is finite and one-dimensional, not a trilinear family",
        "direct_close": False,
    },
    {
        "name": "spectral gap / finite-group expansion inputs",
        "url": "https://arxiv.org/abs/2512.15364",
        "input_signature": "finite-group orbit expansion or anti-concentration",
        "usable_after": "a genuine group orbit model is constructed from phase residues",
        "current_blocker": "no orbit expansion family has been proved for the row-column payload",
        "direct_close": False,
    },
]


ROUTES = [
    {
        "route": "corrected LPF/Phi exact count",
        "closed_assets": [
            "C_p(N)=Phi(floor(N/p);q<p)-1",
            "C_p(N)=Phi(floor(N/p);q<p)-Phi(p-1;q<p)",
            "Phi(p-1;q<p)=1",
            "periodic primorial boundary error identified",
        ],
        "remaining_blocker": "unsigned counts do not distinguish prime emission from composite tails",
        "direct_unconditional_closure": False,
        "next_required_object": "global Mobius/von-Mangoldt signed divisor payload",
        "priority": "supporting",
    },
    {
        "route": "ordinary short intervals and Oppermann top row",
        "closed_assets": [
            "theta>1/2 closes only zero-density low rows",
            "sqrt C<=1 is the sharp row containment threshold",
            "top row equals prime-indexed Oppermann-left",
            "top row is necessary but not sufficient for all rows",
        ],
        "remaining_blocker": "need h(kP)<P for every 1<=k<P, not just k=P-1",
        "direct_unconditional_closure": False,
        "next_required_object": "pointwise sqrt-scale row psi input or internal signed substitute",
        "priority": "boundary",
    },
    {
        "route": "terminal signed monotone-run payload",
        "closed_assets": [
            "finite terminal run ledger closed",
            "atom adjacent-cancellation decomposition closed",
            "selected negative excess beats finite extra atom survivor",
        ],
        "remaining_blocker": "uniform adjacent-run cancellation family or named PDEC/SAE return",
        "direct_unconditional_closure": False,
        "next_required_object": "admissible signed trace/Type-II family or LocalSurvivor/PDEC theorem",
        "priority": "fastest",
    },
    {
        "route": "two-point sieve / quadratic secondary sieve",
        "closed_assets": [
            "DI/BFI/KLS direction identified",
            "same-convention numerator/denominator contract stated",
        ],
        "remaining_blocker": "denominator floor and numerator load must be proved in the same singular-series convention",
        "direct_unconditional_closure": False,
        "next_required_object": "BMD=>TLI without hidden denominator/parity gap",
        "priority": "second",
    },
    {
        "route": "RH contradiction-field controlled exits",
        "closed_assets": [
            "controlled exits and D-structure/Rankin boundaries recorded",
        ],
        "remaining_blocker": "independent referee acceptance of all controlled exits",
        "direct_unconditional_closure": False,
        "next_required_object": "verification package, not first-break route",
        "priority": "verification",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def route_summary() -> dict[str, Any]:
    """生成路线裁定摘要。"""
    fastest = next(route for route in ROUTES if route["priority"] == "fastest")
    return {
        "fastest_route": fastest["route"],
        "fastest_next_required_object": fastest["next_required_object"],
        "pure_lpf_lane_closes_claim": False,
        "pure_short_interval_lane_closes_claim": False,
        "top_row_oppermann_lane_closes_claim": False,
        "external_theorems_directly_close_without_internal_signed_family": False,
        "three_claim_unconditional_closure_reached": False,
        "honest_instruction": (
            "Do not present corrected LPF counts, periodic Euler errors, top-row Oppermann-left, "
            "or external Kloosterman/Type-II estimates as a completed proof until an admissible "
            "signed family or a named PDEC/SAE/LocalSurvivor theorem is supplied."
        ),
    }


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    return {
        "certificate_type": "prime_matrix_phi_lpf_corrected_lpf_signed_trace_breakthrough_router",
        "status": "corrected_lpf_routes_to_signed_trace_not_unsigned_closure",
        "verified_date": "2026-05-26",
        "lpf_exact_count_fixed": True,
        "lpf_exact_count_formula": "C_p(N)=Phi(floor(N/p);q<p)-1=Phi(floor(N/p);q<p)-Phi(p-1;q<p)",
        "phi_endpoint_singleton": "Phi(p-1;q<p)=1",
        "finite_euler_truncation_error_type": "primorial periodic boundary term, not half-main saving",
        "von_mangoldt_lift_requires_global_signed_payload": True,
        "prime_power_tail_sublinear_closed": True,
        "top_row_oppermann_necessary_not_sufficient": True,
        "all_external_inputs_require_internal_admissible_family": True,
        "fastest_first_break_candidate": "Prime Matrix terminal signed monotone-run payload",
        "fastest_first_break_gate": (
            "UniformAdjacentRunCancellationFamilyOrPDEC "
            "AND AtomLocalSurvivorPaymentOrPDEC "
            "AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
        ),
        "row_column_unconditional_closed": False,
        "two_point_unconditional_closed": False,
        "rh_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "routes": ROUTES,
        "external_inputs": EXTERNAL_INPUTS,
        "summary": route_summary(),
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "After correcting the LPF bucket formula and the finite Euler truncation error, "
            "the LPF/Phi lane supplies exact ownership and boundary accounting but not prime "
            "emission. Ordinary short intervals and the top-row Oppermann-left subcore also "
            "do not close all strict rows. The fastest non-cyclic route is therefore the "
            "Prime Matrix terminal signed monotone-run payload: either construct a uniform "
            "adjacent-run cancellation / Type-II trace family, or return a named PDEC/SAE/"
            "LocalSurvivor theorem."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF corrected-LPF signed-trace breakthrough 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 总裁定",
        "",
        "```text",
        f"lpf_exact_count_fixed={fmt_bool(payload['lpf_exact_count_fixed'])}",
        f"lpf_exact_count_formula={payload['lpf_exact_count_formula']}",
        f"phi_endpoint_singleton={payload['phi_endpoint_singleton']}",
        f"finite_euler_truncation_error_type={payload['finite_euler_truncation_error_type']}",
        "von_mangoldt_lift_requires_global_signed_payload="
        f"{fmt_bool(payload['von_mangoldt_lift_requires_global_signed_payload'])}",
        "top_row_oppermann_necessary_not_sufficient="
        f"{fmt_bool(payload['top_row_oppermann_necessary_not_sufficient'])}",
        "all_external_inputs_require_internal_admissible_family="
        f"{fmt_bool(payload['all_external_inputs_require_internal_admissible_family'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        "```",
        "",
        "## 2. 路线裁定表",
        "",
        "| route | priority | closed assets | remaining blocker | next required object | direct close |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for route in payload["routes"]:
        lines.append(
            "| {route} | {priority} | {assets} | {blocker} | {next_obj} | {direct} |".format(
                route=route["route"],
                priority=route["priority"],
                assets="<br>".join(route["closed_assets"]),
                blocker=route["remaining_blocker"],
                next_obj=route["next_required_object"],
                direct=fmt_bool(route["direct_unconditional_closure"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 外部前沿适配",
            "",
            "| input | input signature | usable after | current blocker | direct close | url |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in payload["external_inputs"]:
        lines.append(
            "| {name} | {sig} | {after} | {blocker} | {direct} | {url} |".format(
                name=item["name"],
                sig=item["input_signature"],
                after=item["usable_after"],
                blocker=item["current_blocker"],
                direct=fmt_bool(item["direct_close"]),
                url=item["url"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 最快非循环突破口",
            "",
            "```text",
            f"fastest_first_break_candidate={payload['fastest_first_break_candidate']}",
            f"fastest_first_break_gate={payload['fastest_first_break_gate']}",
            "```",
            "",
            "## 5. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 6. 依赖哈希",
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
    print(f"fastest_first_break_candidate={payload['fastest_first_break_candidate']}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
