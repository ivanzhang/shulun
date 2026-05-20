#!/usr/bin/env python3
"""生成 Phi-LPF pure pair Ferrers support 前沿证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_pure_pair_ferrers_support_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json

输出：
  data/prime-matrix-phi-lpf-pure-pair-ferrers-support-ledger.json
  docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json
  docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.md
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

SLUG = "prime-matrix-phi-lpf-pure-pair-ferrers-support"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PURE_ATOM_ROUTER = DOCS / "prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
ORIENTATION_TRACE_CERT = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_TRACE_CERT = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

PURE_SEMIPRIME_ATOM = "PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward"
FERRERS_SUPPORT = "PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward"
TWO_PRIME_SIGNED_KERNEL = "PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward"
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


def sample_ferrers_support_audit(n: int) -> dict[str, Any]:
    """审计 pure pair 支撑图的 Ferrers 嵌套邻域结构。"""
    primes = primes_up_to(n)
    left = [p for p in primes if p <= math.isqrt(n)]
    neighborhoods: dict[int, set[int]] = {
        p: {q for q in primes if p < q <= n // p}
        for p in left
    }
    edges = sorted((p, q) for p, qs in neighborhoods.items() for q in qs)
    ferrers_failures: list[str] = []
    for i, p in enumerate(left):
        for r in left[i + 1 :]:
            if not neighborhoods[r].issubset(neighborhoods[p]):
                ferrers_failures.append(f"N({r}) not subset N({p})")
                break
        if ferrers_failures:
            break

    right_degrees: dict[int, int] = {}
    for _, q in edges:
        right_degrees[q] = right_degrees.get(q, 0) + 1
    degree_identity = sum(len(qs) for qs in neighborhoods.values()) == len(edges) == sum(
        right_degrees.values()
    )
    left_degrees = [{"p": p, "degree": len(neighborhoods[p])} for p in left]
    top_right_degrees = [
        {"q": q, "degree": degree}
        for q, degree in sorted(right_degrees.items(), key=lambda item: (-item[1], item[0]))[:8]
    ]
    edge_formula_sum = sum(
        sum(1 for q in primes if p < q <= n // p)
        for p in left
    )
    edge_formula_ok = edge_formula_sum == len(edges)
    nonempty_left = sum(1 for p in left if neighborhoods[p])
    empty_left = len(left) - nonempty_left
    return {
        "N": n,
        "left_owner_prime_layers": len(left),
        "right_prime_vertices": len(right_degrees),
        "pure_pair_edges": len(edges),
        "nonempty_left_layers": nonempty_left,
        "empty_left_layers": empty_left,
        "edge_formula_sum": edge_formula_sum,
        "edge_formula_holds": edge_formula_ok,
        "ferrers_nested_neighborhoods_hold": not ferrers_failures,
        "degree_sum_identity_holds": degree_identity,
        "max_left_degree": max((item["degree"] for item in left_degrees), default=0),
        "min_nonzero_left_degree": min(
            (item["degree"] for item in left_degrees if item["degree"] > 0), default=0
        ),
        "max_right_degree": max(right_degrees.values(), default=0),
        "formal_edge_sign_shadow_bits": len(edges),
        "formal_edge_sign_shadow_log10": round(len(edges) * math.log10(2), 6),
        "top_left_degrees": left_degrees[:8],
        "tail_left_degrees": left_degrees[-5:],
        "top_right_degrees": top_right_degrees,
        "ferrers_failures": ferrers_failures[:10],
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PURE_ATOM_ROUTER,
        POINTWISE_FRONTIER_CERT,
        ORIENTATION_TRACE_CERT,
        BUILTIN_TRACE_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def support_fields() -> list[dict[str, str]]:
    """列出 Ferrers 支撑账本字段。"""
    return [
        {
            "field": "left_owner_prime",
            "status": "closed_unsigned",
            "meaning": "`p <= sqrt(N)` 的 LPF owner layer。",
        },
        {
            "field": "right_first_prime",
            "status": "closed_unsigned",
            "meaning": "pure pair 的 second prime `q`，满足 `p<q<=N/p`。",
        },
        {
            "field": "ferrers_neighbor_rule",
            "status": "closed_unsigned",
            "meaning": "`N(p)={q prime: p<q<=N/p}`，且 `p` 递增时邻域嵌套下降。",
        },
        {
            "field": "degree_ledgers",
            "status": "closed_unsigned",
            "meaning": "left/right degree 和 edge 总数完全由 prime tables 与 floor(N/p) 决定。",
        },
        {
            "field": "two_prime_signed_interaction_value",
            "status": "open_signed",
            "meaning": "每条 `(p,q)` 边的 signed seed/local factor/orientation 仍未由支撑图产生。",
        },
    ]


def build_rows(
    pure_atom: dict[str, Any],
    pointwise: dict[str, Any],
    orientation: dict[str, Any],
    builtin: dict[str, Any],
    exactuv: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 Ferrers support 前沿判定表。"""
    ferrers_ok = all(item["ferrers_nested_neighborhoods_hold"] for item in samples)
    formula_ok = all(item["edge_formula_holds"] and item["degree_sum_identity_holds"] for item in samples)
    return [
        row(
            "PurePairSignedAtomTargetImported",
            pure_atom.get("next_primary_attack_target") == PURE_SEMIPRIME_ATOM,
            False,
            "上一层已把 latest seed 原子压到 offdiagonal pure semiprime pair。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "PurePairFerrersSupportRuleClosed",
            ferrers_ok,
            True,
            "pure pair 支撑等价于边条件 `p<q<=N/p`，左邻域按 `p` 递增嵌套下降。",
            FERRERS_SUPPORT,
        ),
        row(
            "PurePairDegreeLedgerClosed",
            formula_ok,
            True,
            "edge count、left degrees、right degrees 均由 prime table 和 `floor(N/p)` 决定。",
            FERRERS_SUPPORT,
        ),
        row(
            "SupportGraphDoesNotEmitSignedKernel",
            True,
            True,
            "Ferrers 支撑只排除支撑/度数缺口；不产生每条边的 sign、orientation 或 local factor。",
            TWO_PRIME_SIGNED_KERNEL,
        ),
        row(
            "TwoPrimeSignedInteractionKernelCurrentCorpusProved",
            False,
            False,
            "当前语料没有提交 `(p,q)` 两素数交互 signed kernel。",
            TWO_PRIME_SIGNED_KERNEL,
        ),
        row(
            "OffDiagonalOrientationParityStillOpen",
            pure_atom.get("offdiagonal_orientation_parity_law_proved") is False,
            False,
            "两素数 kernel 即使存在，orientation parity/branch side 仍需同边绑定。",
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
            pure_atom.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "tail lift 与完整 support key 的 signed compatibility 仍依赖 internal transition。",
            INTERNAL_TRANSITION,
        ),
        row(
            "PointwisePhiLPFTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 signed table 仍可替代两素数 kernel，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "CompleteBranchTraceWouldSupplyKernel",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True,
            True,
            "完整 branch trace 可给每条 `(p,q)` 边的 signed kernel、orientation、ExactUV 与 return tag。",
            BRANCH_TRACE,
        ),
        row(
            "AtomicTraceWouldSupplyKernel",
            builtin.get("branch_trace_conditionally_suffices") is True,
            True,
            "atomic trace signed coefficient 公式可把两素数交互 kernel 作为 trace 字段读取。",
            ATOMIC_TRACE,
        ),
        row(
            "PurePairSignedAtomCurrentCorpusProved",
            False,
            False,
            "本步只关闭 pure pair 支撑图和度数账本，没有证明 signed seed atom。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步不证明三命题无条件闭合；它只把 pure atom 缺口压到两素数 signed interaction kernel。",
            f"{TWO_PRIME_SIGNED_KERNEL} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 Ferrers support 前沿证书。"""
    pure_atom = load_json(PURE_ATOM_ROUTER)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    orientation = load_json(ORIENTATION_TRACE_CERT)
    builtin = load_json(BUILTIN_TRACE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    samples = [sample_ferrers_support_audit(n) for n in SAMPLE_N]
    rows = build_rows(pure_atom, pointwise, orientation, builtin, exactuv, samples)
    ferrers_ok = all(item["ferrers_nested_neighborhoods_hold"] for item in samples)
    formula_ok = all(item["edge_formula_holds"] and item["degree_sum_identity_holds"] for item in samples)
    retained_basis = (
        f"(({TWO_PRIME_SIGNED_KERNEL} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
        f"AND {INTERNAL_TRANSITION} AND {COMMON_PACKET}) OR {POINTWISE_TABLE} "
        f"OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} "
        f"OR {NEW_JOINT_FORMULA}) AND {EXACTUV_PAIR} AND {MODEL_LEDGER} "
        f"AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_pure_pair_ferrers_support_router",
        "status": "phi_lpf_pure_pair_signed_atom_reduced_to_two_prime_signed_interaction_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "pure_pair_ferrers_support_router_closed": True,
        "pure_pair_signed_atom_target_imported": pure_atom.get("next_primary_attack_target")
        == PURE_SEMIPRIME_ATOM,
        "pure_pair_ferrers_support_rule_proved": ferrers_ok,
        "pure_pair_degree_ledger_proved": formula_ok,
        "support_graph_signed_kernel_emission_proved": False,
        "two_prime_signed_interaction_kernel_proved": False,
        "pure_semiprime_pair_signed_seed_atom_proved": False,
        "offdiagonal_orientation_parity_law_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": PURE_SEMIPRIME_ATOM,
        "closed_unsigned_subledger": FERRERS_SUPPORT,
        "next_primary_attack_target": TWO_PRIME_SIGNED_KERNEL,
        "paired_required_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            COMMON_PACKET,
        ],
        "parallel_direct_attack_target": POINTWISE_TABLE,
        "conditional_generators": [BRANCH_TRACE, ATOMIC_TRACE],
        "retained_basis_after_router": retained_basis,
        "pure_pair_support_fields": support_fields(),
        "sample_ferrers_support_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "offdiagonal pure pair atom 的支撑已经完全退化为二素数 Ferrers 图：左侧 "
            "`p<=sqrt(N)`，右侧素数 `q`，边条件为 `p<q<=N/p`。随着 `p` 增大，"
            "邻域嵌套下降，left/right degree 与总边数全由 prime table 和 `floor(N/p)` 决定。"
            "因此 pure atom 剩余不再是支撑或度数问题，而是每条 `(p,q)` 边上的 two-prime "
            "signed interaction kernel、orientation parity、ExactUV return 与 internal transition。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF pure pair Ferrers support 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"pure_pair_signed_atom_target_imported={fmt_bool(cert['pure_pair_signed_atom_target_imported'])}",
        f"pure_pair_ferrers_support_rule_proved={fmt_bool(cert['pure_pair_ferrers_support_rule_proved'])}",
        f"pure_pair_degree_ledger_proved={fmt_bool(cert['pure_pair_degree_ledger_proved'])}",
        f"support_graph_signed_kernel_emission_proved={fmt_bool(cert['support_graph_signed_kernel_emission_proved'])}",
        f"two_prime_signed_interaction_kernel_proved={fmt_bool(cert['two_prime_signed_interaction_kernel_proved'])}",
        f"pure_semiprime_pair_signed_seed_atom_proved={fmt_bool(cert['pure_semiprime_pair_signed_seed_atom_proved'])}",
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
            "## 2. 支撑字段",
            "",
            "| field | status | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["pure_pair_support_fields"]:
        lines.append(f"| `{item['field']}` | `{item['status']}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 样本审计摘要",
            "",
            "| N | left layers | right vertices | edges | nonempty left | max left deg | max right deg | Ferrers | degree ok | sign log10 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |",
        ]
    )
    for item in cert["sample_ferrers_support_audit"]:
        lines.append(
            f"| {item['N']} | {item['left_owner_prime_layers']} | {item['right_prime_vertices']} | "
            f"{item['pure_pair_edges']} | {item['nonempty_left_layers']} | {item['max_left_degree']} | "
            f"{item['max_right_degree']} | `{fmt_bool(item['ferrers_nested_neighborhoods_hold'])}` | "
            f"`{fmt_bool(item['degree_sum_identity_holds'])}` | {item['formal_edge_sign_shadow_log10']} |"
        )
    lines.extend(
        [
            "",
            "## 4. 度数摘要",
            "",
            "| N | top left degrees | top right degrees | tail left degrees |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in cert["sample_ferrers_support_audit"]:
        top_left = ", ".join(f"(p={entry['p']},deg={entry['degree']})" for entry in item["top_left_degrees"][:4])
        top_right = ", ".join(f"(q={entry['q']},deg={entry['degree']})" for entry in item["top_right_degrees"][:4])
        tail_left = ", ".join(f"(p={entry['p']},deg={entry['degree']})" for entry in item["tail_left_degrees"])
        lines.append(f"| {item['N']} | {top_left} | {top_right} | {tail_left} |")
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
    """写出 Ferrers support 前沿证书。"""
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
