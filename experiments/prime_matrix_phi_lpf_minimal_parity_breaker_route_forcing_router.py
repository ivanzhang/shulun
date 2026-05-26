#!/usr/bin/env python3
"""归档 Phi-LPF 奇偶性障碍的最小破障路线强制合同。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_minimal_parity_breaker_route_forcing_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.json

输出：
  data/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-ledger.json
  docs/monograph/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.json
  docs/monograph/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.md

本证书承接 parity-barrier prime-distribution contract。目的不是重复说明
LPF/Phi 是无符号计数，而是把“若要真正闭合，最小还缺什么”压成路线
强制表：外部点态 theta/psi、内部 signed cofactor transport、trace/Type-II
family、PDEC/SAE 回流四类路线互相区分，并给出当前最快非循环下一手。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PARITY_CONTRACT_JSON = DOCS / "prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json"
CORRECTED_LPF_JSON = DOCS / "prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.json"
BUCKET_TRANSPORT_JSON = DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json"
TRACE_KERNEL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.json"
SQRT_THRESHOLD_JSON = DOCS / "prime-matrix-phi-lpf-sqrt-constant-threshold-router.json"
OPPERMANN_SUBCORE_JSON = DOCS / "prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-router.json"
PRIME_POWER_TAIL_JSON = DOCS / "prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.json"
SHARED_HINGE_JSON = DOCS / "prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-router.json"
EXTERNAL_STRESS_JSON = DOCS / "prime-matrix-external-frontier-theorem-stress-router.json"

SOURCE_FILES = [
    Path(__file__).resolve(),
    PARITY_CONTRACT_JSON,
    CORRECTED_LPF_JSON,
    BUCKET_TRANSPORT_JSON,
    TRACE_KERNEL_JSON,
    SQRT_THRESHOLD_JSON,
    OPPERMANN_SUBCORE_JSON,
    PRIME_POWER_TAIL_JSON,
    SHARED_HINGE_JSON,
    EXTERNAL_STRESS_JSON,
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    DOCS / "external-theorem-index.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

LATEST_OPEN_GATE = (
    "MinimalParityBreakerRouteForcingClosed "
    "AND NeedEitherPointwiseThetaPsiCOneInputOrSignedCofactorTransport "
    "AND PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward "
    "AND BoundaryRatioSourceKeyLawOrPDEC "
    "AND TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC "
    "AND PrimitiveOrientationLocalFactorProductLawBeforePushforward "
    "AND AdmissibleSignedTraceTypeIIFamilyStillOpen"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def short_interval_rows() -> list[dict[str, Any]]:
    """外部点态短区间路线的精确门槛。"""
    return [
        {
            "formula": "theta((kP,(k+1)P))>0 for every 1<=k<P",
            "equivalent_form": "h(kP)<P for every 1<=k<P",
            "minimum_strength": "pointwise sqrt-scale input with constant C<=1",
            "current_status": "not available unconditionally in current corpus",
            "why_not_enough_now": "known theta>1/2 inputs close only low-row or zero-density bands; C>1 leaves positive-density top band",
        },
        {
            "formula": "psi((kP,(k+1)P)) > PrimePowerTail((kP,(k+1)P))",
            "equivalent_form": "theta((kP,(k+1)P))>0 after removing pure prime powers",
            "minimum_strength": "pointwise lower bound exceeding an o(P) tail",
            "current_status": "tail bound closed; pointwise psi lower bound not proved",
            "why_not_enough_now": "sublinear tail is bookkeeping unless a positive rowwise psi main term is supplied",
        },
    ]


def route_forcing_rows(
    parity_contract: dict[str, Any],
    bucket_transport: dict[str, Any],
    trace_kernel: dict[str, Any],
    sqrt_threshold: dict[str, Any],
    prime_power_tail: dict[str, Any],
    shared_hinge: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造最小破障路线表。"""
    return [
        {
            "route": "Pointwise theta / gap route",
            "minimal_object": "theta((kP,(k+1)P))>0, equivalently h(kP)<P for all strict rows",
            "already_closed_assets": "C<=1 sqrt-scale threshold contract; top-row/Oppermann subcore separated",
            "open_atom": "unconditional pointwise C<=1 sqrt-scale theorem or row-specific substitute",
            "directly_breaks_parity": True,
            "available_now": False,
            "chosen_next": False,
            "evidence": f"sqrt_threshold_status={sqrt_threshold.get('status')}",
        },
        {
            "route": "Pointwise psi beyond prime-power tail",
            "minimal_object": "psi(I_{P,k})>PrimePowerTail(I_{P,k}) rowwise",
            "already_closed_assets": prime_power_tail.get("asymptotic_tail_statement"),
            "open_atom": "pointwise psi lower bound at exact row scale",
            "directly_breaks_parity": True,
            "available_now": False,
            "chosen_next": False,
            "evidence": (
                "prime_power_tail_sublinear_threshold_closed="
                f"{prime_power_tail.get('prime_power_tail_sublinear_threshold_closed')}"
            ),
        },
        {
            "route": "Internal LPF signed cofactor transport",
            "minimal_object": "a_p(q*m) transport law with orientation/local-factor/branch updates before pushforward",
            "already_closed_assets": "unsigned cofactor split and formal signed partition identity",
            "open_atom": "PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward",
            "directly_breaks_parity": True,
            "available_now": False,
            "chosen_next": True,
            "evidence": bucket_transport.get("hardpoint_after_router"),
        },
        {
            "route": "Trace / Kloosterman / Type-II route",
            "minimal_object": "completed source-keyed signed trace family with factorable coefficients and conductor control",
            "already_closed_assets": "formal Jordan kernel, prefix-record reflection, finite q-spine kernel",
            "open_atom": "source-key lift plus Type-II factorability and conductor range",
            "directly_breaks_parity": True,
            "available_now": False,
            "chosen_next": False,
            "evidence": trace_kernel.get("latest_open_gate"),
        },
        {
            "route": "Shared-pivot PDEC/SAE return",
            "minimal_object": "uniform hinge/payment law failure returns to controlled contradiction",
            "already_closed_assets": "shared-pivot hinge contract and endpoint slack ledger",
            "open_atom": "BridgeRootSharedPivotHingeLawOrPDEC plus terminal sibling q-spine payment",
            "directly_breaks_parity": True,
            "available_now": False,
            "chosen_next": False,
            "evidence": shared_hinge.get("latest_open_gate"),
        },
        {
            "route": "More LPF/Phi/wheel refinement",
            "minimal_object": "none; this class only refines unsigned support",
            "already_closed_assets": parity_contract.get("lpf_bucket_exact_formula"),
            "open_atom": "not a parity-breaking atom",
            "directly_breaks_parity": False,
            "available_now": True,
            "chosen_next": False,
            "evidence": "unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false",
        },
    ]


def external_rows() -> list[dict[str, Any]]:
    """列出当前最新外部输入与本项目所缺接口的关系。"""
    return [
        {
            "input": "Guth--Maynard zero-density / short intervals",
            "url": "https://arxiv.org/abs/2405.20552",
            "supplies": "pointwise PNT in intervals x^{17/30+o(1)}",
            "project_blocker": "17/30>1/2, so top P^2 rows still need sqrt-scale strength",
            "direct_close_now": False,
        },
        {
            "input": "Runbo Li short intervals",
            "url": "https://arxiv.org/abs/2308.04458",
            "supplies": "prime existence in [x-x^0.52,x] for large x",
            "project_blocker": "0.52>1/2; closes only low-row band after row containment",
            "direct_close_now": False,
        },
        {
            "input": "Runbo Li large-modulus AP / Harman sieve",
            "url": "https://arxiv.org/abs/2602.20917",
            "supplies": "mean value theorems beyond x^{1/2} for selected modulus families",
            "project_blocker": "Prime Matrix target is pointwise fixed row/column positivity at x=P^2",
            "direct_close_now": False,
        },
        {
            "input": "Fouvry--Kowalski--Michel--Sawin trace functions",
            "url": "https://arxiv.org/abs/2511.09459",
            "supplies": "bilinear trace-function cancellation below Polya-Vinogradov range",
            "project_blocker": "no completed source-keyed trace sheaf/family yet",
            "direct_close_now": False,
        },
        {
            "input": "Milicevic--Qin--Wu Kloosterman bilinear forms",
            "url": "https://arxiv.org/abs/2511.07550",
            "supplies": "power-saving bilinear Kloosterman estimates modulo arbitrary q",
            "project_blocker": "no admissible two-variable Kloosterman family from LPF payload yet",
            "direct_close_now": False,
        },
        {
            "input": "Wright trilinear Kloosterman fractions",
            "url": "https://arxiv.org/abs/2604.25177",
            "supplies": "trilinear/unbalanced convolution estimates with partially fixed moduli",
            "project_blocker": "no trilinear convolution or equidistributed beta sequence constructed",
            "direct_close_now": False,
        },
        {
            "input": "Pascadi distribution / non-abelian Type-II inputs",
            "url": "https://arxiv.org/abs/2505.00653 and https://arxiv.org/abs/2511.08445",
            "supplies": "well-factorable prime/smooth distribution and composite-modulus Kloosterman Type-II bounds",
            "project_blocker": "current LPF ownership is not a well-factorable signed coefficient family",
            "direct_close_now": False,
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装最小破障路线强制证书。"""
    parity_contract = load_json(PARITY_CONTRACT_JSON)
    corrected_lpf = load_json(CORRECTED_LPF_JSON)
    bucket_transport = load_json(BUCKET_TRANSPORT_JSON)
    trace_kernel = load_json(TRACE_KERNEL_JSON)
    sqrt_threshold = load_json(SQRT_THRESHOLD_JSON)
    oppermann_subcore = load_json(OPPERMANN_SUBCORE_JSON)
    prime_power_tail = load_json(PRIME_POWER_TAIL_JSON)
    shared_hinge = load_json(SHARED_HINGE_JSON)
    external_stress = load_json(EXTERNAL_STRESS_JSON)

    route_rows = route_forcing_rows(
        parity_contract,
        bucket_transport,
        trace_kernel,
        sqrt_threshold,
        prime_power_tail,
        shared_hinge,
    )
    chosen_rows = [row for row in route_rows if row["chosen_next"]]
    false_direct_close_rows = [
        row for row in external_rows() if row["direct_close_now"] is False
    ]

    minimal_route_forcing_closed = all(
        [
            parity_contract.get("parity_barrier_diagnosis_closed") is True,
            parity_contract.get("lpf_correction_closed") is True,
            parity_contract.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction") is False,
            bucket_transport.get("phi_lpf_bucket_signed_transport_router_closed") is True,
            bucket_transport.get("phi_lpf_rough_cofactor_signed_transport_law_proved") is False,
            trace_kernel.get("trace_or_typeii_family_admissible_now") is False,
            len(chosen_rows) == 1,
            len(false_direct_close_rows) == len(external_rows()),
        ]
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_minimal_parity_breaker_route_forcing_router",
        "status": "minimal_parity_breaker_route_forcing_pinned_signed_transport_open",
        "verified_date": "2026-05-26",
        "parity_barrier_essence": parity_contract.get("parity_barrier_essence"),
        "minimal_route_forcing_closed": minimal_route_forcing_closed,
        "lpf_exact_count_formula": parity_contract.get("lpf_bucket_exact_formula"),
        "legendre_periodic_boundary_not_half_main": parity_contract.get("legendre_periodic_boundary_not_half_main"),
        "more_wheel_or_lpf_refinement_rejected_as_first_break": True,
        "pointwise_theta_gap_formula_required": "theta((kP,(k+1)P))>0 iff h(kP)<P for all 1<=k<P",
        "pointwise_psi_tail_formula_required": "psi(I_{P,k})>PrimePowerTail(I_{P,k})",
        "signed_transport_formula_required": (
            "a_p(q*m) must be transported from source data with orientation, local factor, "
            "alpha/delta side, branch transition, and named failure return before pushforward"
        ),
        "short_interval_rows": short_interval_rows(),
        "route_forcing_rows": route_rows,
        "external_frontier_rows": external_rows(),
        "chosen_next_primary_attack_target": "PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward",
        "chosen_parallel_attack_target": "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward",
        "why_chosen_next": (
            "这是从小到大 LPF 剥离第一次可能升级为 signed 递推的位置。"
            "外部 trace/Type-II 工具必须先拿到这类系数才能接入；"
            "外部 theta/psi 路线则需要当前不可用的点态平方根尺度定理。"
        ),
        "corrected_lpf_status": corrected_lpf.get("status"),
        "bucket_transport_status": bucket_transport.get("status"),
        "trace_kernel_status": trace_kernel.get("status"),
        "sqrt_threshold_status": sqrt_threshold.get("status"),
        "oppermann_subcore_status": oppermann_subcore.get("status"),
        "prime_power_tail_status": prime_power_tail.get("status"),
        "external_stress_status": external_stress.get("status"),
        "row_column_unconditional_closed": False,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "奇偶性障碍现在被压成最小路线选择：完整证明必须给出精确平方根行上的 "
            "pointwise theta/psi 正性，或产生 signed coefficient family。"
            "在内部非循环路线中，下一最小对象是 pushforward 前的 LPF rough-cofactor "
            "multiplication signed transport law；当前所有外部谱/Type-II 输入仍要等这个 "
            "signed family 或等价 trace object 构造出来后才能真正接入。"
        ),
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix Phi-LPF minimal parity-breaker route-forcing 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        "## 1. 最小破障裁定",
        "",
        cert["parity_barrier_essence"],
        "",
        "```text",
        f"minimal_route_forcing_closed={fmt_bool(cert['minimal_route_forcing_closed'])}",
        f"lpf_exact_count_formula={cert['lpf_exact_count_formula']}",
        f"legendre_periodic_boundary_not_half_main={fmt_bool(cert['legendre_periodic_boundary_not_half_main'])}",
        f"more_wheel_or_lpf_refinement_rejected_as_first_break={fmt_bool(cert['more_wheel_or_lpf_refinement_rejected_as_first_break'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 必须攻克的精确公式",
        "",
        "| formula | equivalent form | minimum strength | current status | why not enough now |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in cert["short_interval_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(row["formula"]),
                    cell(row["equivalent_form"]),
                    cell(row["minimum_strength"]),
                    cell(row["current_status"]),
                    cell(row["why_not_enough_now"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 路线强制表",
            "",
            "| route | minimal object | closed assets | open atom | breaks parity | chosen next |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["route_forcing_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(row["route"]),
                    cell(row["minimal_object"]),
                    cell(row["already_closed_assets"]),
                    cell(row["open_atom"]),
                    f"`{fmt_bool(row['directly_breaks_parity'])}`",
                    f"`{fmt_bool(row['chosen_next'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 当前最快非循环下一手",
            "",
            "```text",
            f"chosen_next_primary_attack_target={cert['chosen_next_primary_attack_target']}",
            f"chosen_parallel_attack_target={cert['chosen_parallel_attack_target']}",
            "```",
            "",
            cert["why_chosen_next"],
            "",
            "## 5. 外部前沿输入边界",
            "",
            "| input | supplies | project blocker | direct close now | url |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_frontier_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(row["input"]),
                    cell(row["supplies"]),
                    cell(row["project_blocker"]),
                    f"`{fmt_bool(row['direct_close_now'])}`",
                    cell(row["url"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 6. 最新开放口",
            "",
            "```text",
            cert["latest_open_gate"],
            "```",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")

    lines.append("")
    lines.append("三命题仍未无条件闭合。")
    return "\n".join(lines) + "\n"


def main() -> None:
    """生成证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, indent=2, ensure_ascii=False, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(cert), encoding="utf-8")
    print(f"minimal_route_forcing_closed={fmt_bool(cert['minimal_route_forcing_closed'])}")
    print(f"chosen_next_primary_attack_target={cert['chosen_next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
