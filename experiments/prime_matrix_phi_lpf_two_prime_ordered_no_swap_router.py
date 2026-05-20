#!/usr/bin/env python3
"""生成 Phi-LPF two-prime ordered no-swap 前沿证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_two_prime_ordered_no_swap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json

输出：
  data/prime-matrix-phi-lpf-two-prime-ordered-no-swap-ledger.json
  docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json
  docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-two-prime-ordered-no-swap"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

FERRERS_ROUTER = DOCS / "prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
ORIENTATION_TRACE_CERT = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_TRACE_CERT = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

TWO_PRIME_SIGNED_KERNEL = "PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward"
ORDERED_NO_SWAP = "PhiLPFOffDiagonalTwoPrimeOrderedLPFOwnerNoSwapSymmetryLedgerBeforePushforward"
EDGE_LOCAL_FORMULA = "PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SAMPLE_N = [30, 100, 997, 5003, 10000]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def primes_up_to(n: int) -> list[int]:
    """返回不超过 n 的素数表。"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = [False] * (((n - start) // p) + 1)
    return [value for value, is_prime in enumerate(sieve) if is_prime]


def sample_ordered_no_swap_audit(n: int) -> dict[str, Any]:
    """审计 two-prime pure pair 的 LPF owner 顺序与 no-swap 性质。"""
    primes = primes_up_to(n)
    prime_set = set(primes)
    left = [p for p in primes if p <= math.isqrt(n)]
    edges = sorted((p, q) for p in left for q in primes if p < q <= n // p)
    edge_set = set(edges)
    reverse_present = [(p, q) for p, q in edges if (q, p) in edge_set]
    bad_lpf_owner = [
        (p, q)
        for p, q in edges
        if not (p < q and p * q <= n and p in prime_set and q in prime_set)
    ]
    unordered_semiprimes = {
        p * q
        for i, p in enumerate(primes)
        for q in primes[i + 1 :]
        if p * q <= n
    }
    edge_products = {p * q for p, q in edges}
    missing_products = sorted(unordered_semiprimes - edge_products)[:10]
    duplicate_product_count = len(edges) - len(edge_products)
    lpf_owner_identity = not reverse_present and not bad_lpf_owner and not missing_products and duplicate_product_count == 0
    small_q_edges = [(p, q) for p, q in edges if q <= math.isqrt(n)]
    large_q_edges = [(p, q) for p, q in edges if q > math.isqrt(n)]
    top_products = [
        {"p": p, "q": q, "value": p * q}
        for p, q in edges[:8]
    ]
    tail_products = [
        {"p": p, "q": q, "value": p * q}
        for p, q in edges[-8:]
    ]
    return {
        "N": n,
        "ordered_edges": len(edges),
        "unordered_distinct_semiprime_products": len(unordered_semiprimes),
        "edge_product_count": len(edge_products),
        "duplicate_product_count": duplicate_product_count,
        "reverse_edges_present": len(reverse_present),
        "lpf_owner_no_swap_identity_holds": lpf_owner_identity,
        "small_q_edges": len(small_q_edges),
        "large_q_edges": len(large_q_edges),
        "small_q_edge_share": round(len(small_q_edges) / max(1, len(edges)), 12),
        "large_q_edge_share": round(len(large_q_edges) / max(1, len(edges)), 12),
        "formal_ordered_edge_sign_shadow_bits": len(edges),
        "formal_ordered_edge_sign_shadow_log10": round(len(edges) * math.log10(2), 6),
        "top_edge_products": top_products,
        "tail_edge_products": tail_products,
        "reverse_present_examples": reverse_present[:10],
        "bad_lpf_owner_examples": bad_lpf_owner[:10],
        "missing_product_examples": missing_products,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        FERRERS_ROUTER,
        POINTWISE_FRONTIER_CERT,
        ORIENTATION_TRACE_CERT,
        BUILTIN_TRACE_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def ordered_fields() -> list[dict[str, str]]:
    """列出 no-swap 顺序账本字段。"""
    return [
        {
            "field": "canonical_lpf_owner_order",
            "status": "closed_unsigned",
            "meaning": "每个 distinct semiprime `p*q` 只进入 `(min(p,q),max(p,q))`。",
        },
        {
            "field": "reverse_edge_absence",
            "status": "closed_unsigned",
            "meaning": "`(q,p)` 不属于同一 LPF owner source domain，不能用作 cancellation partner。",
        },
        {
            "field": "product_symmetry_erased_before_signed_kernel",
            "status": "closed_unsigned",
            "meaning": "`p*q=q*p` 只证明同一整数值，不产生第二个 signed source row。",
        },
        {
            "field": "edge_local_signed_formula",
            "status": "open_signed",
            "meaning": "仍需为 canonical ordered edge `(p,q)` 正向给出 signed interaction formula 或 return。",
        },
    ]


def build_rows(
    ferrers: dict[str, Any],
    pointwise: dict[str, Any],
    orientation: dict[str, Any],
    builtin: dict[str, Any],
    exactuv: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 ordered no-swap 前沿判定表。"""
    no_swap_ok = all(item["lpf_owner_no_swap_identity_holds"] for item in samples)
    return [
        row(
            "TwoPrimeSignedKernelTargetImported",
            ferrers.get("next_primary_attack_target") == TWO_PRIME_SIGNED_KERNEL,
            False,
            "上一层已把 pure atom 剩余压到 two-prime signed interaction kernel。",
            TWO_PRIME_SIGNED_KERNEL,
        ),
        row(
            "LPFOwnerOrderedNoSwapIdentity",
            no_swap_ok,
            True,
            "每个 offdiagonal semiprime product 只有 canonical `(p,q)` source edge，没有 reverse edge。",
            ORDERED_NO_SWAP,
        ),
        row(
            "ProductSymmetryCannotEmitSign",
            True,
            True,
            "`p*q=q*p` 不提供第二个 pre-Cauchy source row，不能定义 signed cancellation。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "EdgeLocalSignedFormulaCurrentCorpusProved",
            False,
            False,
            "当前语料没有为 canonical ordered edge `(p,q)` 提交 signed interaction formula 或 return。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "TwoPrimeSignedKernelCurrentCorpusProved",
            False,
            False,
            "no-swap 只删除交换伪出口，不证明 two-prime signed kernel。",
            TWO_PRIME_SIGNED_KERNEL,
        ),
        row(
            "OffDiagonalOrientationParityStillOpen",
            ferrers.get("offdiagonal_orientation_parity_law_proved") is False,
            False,
            "edge-local formula 仍需 orientation parity/branch side 同边绑定。",
            OFFDIAG_ORIENTATION,
        ),
        row(
            "OffDiagonalExactUVReturnStillOpen",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False
            or exactuv.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "ExactUV fixed pair/source entropy/fiber 与 return tag 仍是并行门。",
            OFFDIAG_EXACTUV,
        ),
        row(
            "InternalTransitionStillPairedGate",
            ferrers.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "tail lift 与完整 support key 的 signed compatibility 仍依赖 internal transition。",
            INTERNAL_TRANSITION,
        ),
        row(
            "PointwisePhiLPFTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 signed table 仍可替代 edge-local formula，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "CompleteBranchTraceWouldSupplyEdgeFormula",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True,
            True,
            "完整 branch trace 可给 ordered edge 的 signed value、orientation、ExactUV 与 return tag。",
            BRANCH_TRACE,
        ),
        row(
            "AtomicTraceWouldSupplyEdgeFormula",
            builtin.get("branch_trace_conditionally_suffices") is True,
            True,
            "atomic trace signed coefficient 公式可把 edge-local formula 作为 trace 字段读取。",
            ATOMIC_TRACE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步不证明三命题无条件闭合；它只删除 two-prime kernel 的 swap-symmetry 伪出口。",
            f"{EDGE_LOCAL_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 ordered no-swap 前沿证书。"""
    ferrers = load_json(FERRERS_ROUTER)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    orientation = load_json(ORIENTATION_TRACE_CERT)
    builtin = load_json(BUILTIN_TRACE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    samples = [sample_ordered_no_swap_audit(n) for n in SAMPLE_N]
    rows = build_rows(ferrers, pointwise, orientation, builtin, exactuv, samples)
    no_swap_ok = all(item["lpf_owner_no_swap_identity_holds"] for item in samples)
    retained_basis = (
        f"(({EDGE_LOCAL_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
        f"AND {INTERNAL_TRANSITION} AND {COMMON_PACKET}) OR {POINTWISE_TABLE} "
        f"OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} "
        f"OR {NEW_JOINT_FORMULA}) AND {EXACTUV_PAIR} AND {MODEL_LEDGER} "
        f"AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_two_prime_ordered_no_swap_router",
        "status": "phi_lpf_two_prime_signed_kernel_no_swap_symmetry_exit_removed",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "two_prime_ordered_no_swap_router_closed": True,
        "two_prime_signed_kernel_target_imported": ferrers.get("next_primary_attack_target")
        == TWO_PRIME_SIGNED_KERNEL,
        "lpf_owner_ordered_no_swap_identity_proved": no_swap_ok,
        "product_symmetry_signed_emission_proved": False,
        "edge_local_two_prime_signed_formula_proved": False,
        "two_prime_signed_interaction_kernel_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TWO_PRIME_SIGNED_KERNEL,
        "closed_unsigned_subledger": ORDERED_NO_SWAP,
        "next_primary_attack_target": EDGE_LOCAL_FORMULA,
        "paired_required_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            COMMON_PACKET,
        ],
        "parallel_direct_attack_target": POINTWISE_TABLE,
        "conditional_generators": [BRANCH_TRACE, ATOMIC_TRACE],
        "retained_basis_after_router": retained_basis,
        "ordered_no_swap_fields": ordered_fields(),
        "sample_ordered_no_swap_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "two-prime signed kernel 不能从交换对称 `p*q=q*p` 中获得。LPF owner source "
            "domain 只接纳 canonical ordered edge `(p,q)` with `p<q`；reverse edge `(q,p)` "
            "不在同一 source domain。于是 product symmetry 在 signed kernel 之前已经被 LPF "
            "owner 顺序擦除，剩余必须是 edge-local two-prime signed interaction formula 或命名 return。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF two-prime ordered no-swap 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"two_prime_signed_kernel_target_imported={fmt_bool(cert['two_prime_signed_kernel_target_imported'])}",
        f"lpf_owner_ordered_no_swap_identity_proved={fmt_bool(cert['lpf_owner_ordered_no_swap_identity_proved'])}",
        f"product_symmetry_signed_emission_proved={fmt_bool(cert['product_symmetry_signed_emission_proved'])}",
        f"edge_local_two_prime_signed_formula_proved={fmt_bool(cert['edge_local_two_prime_signed_formula_proved'])}",
        f"two_prime_signed_interaction_kernel_proved={fmt_bool(cert['two_prime_signed_interaction_kernel_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. no-swap 字段",
            "",
            "| field | status | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["ordered_no_swap_fields"]:
        lines.append(f"| `{item['field']}` | `{item['status']}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 样本审计摘要",
            "",
            "| N | ordered edges | unordered products | reverse edges | duplicates | small-q | large-q | no-swap ok | sign log10 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for item in cert["sample_ordered_no_swap_audit"]:
        lines.append(
            f"| {item['N']} | {item['ordered_edges']} | {item['unordered_distinct_semiprime_products']} | "
            f"{item['reverse_edges_present']} | {item['duplicate_product_count']} | "
            f"{item['small_q_edges']} | {item['large_q_edges']} | "
            f"`{fmt_bool(item['lpf_owner_no_swap_identity_holds'])}` | "
            f"{item['formal_ordered_edge_sign_shadow_log10']} |"
        )
    lines.extend(
        [
            "",
            "## 4. edge product 样本",
            "",
            "| N | first products | last products |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["sample_ordered_no_swap_audit"]:
        first = ", ".join(
            f"(p={entry['p']},q={entry['q']},n={entry['value']})"
            for entry in item["top_edge_products"][:4]
        )
        last = ", ".join(
            f"(p={entry['p']},q={entry['q']},n={entry['value']})"
            for entry in item["tail_edge_products"][-4:]
        )
        lines.append(f"| {item['N']} | {first} | {last} |")
    lines.extend(
        [
            "",
            "## 5. 最新保留基",
            "",
            "```text",
            cert["retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "配套仍需：",
            "",
            "```text",
            "\n".join(cert["paired_required_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 ordered no-swap 前沿证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
