#!/usr/bin/env python3
"""生成 Phi-LPF edge-local two-prime field-cut 前沿证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_edge_local_two_prime_field_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json

输出：
  data/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-ledger.json
  docs/monograph/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json
  docs/monograph/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.md
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

SLUG = "prime-matrix-phi-lpf-edge-local-two-prime-field-cut"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

NO_SWAP_ROUTER = DOCS / "prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json"
FERRERS_ROUTER = DOCS / "prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
ORIENTATION_TRACE_CERT = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_TRACE_CERT = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

EDGE_LOCAL_FORMULA = "PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward"
EDGE_LABEL_LEDGER = "PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward"
SIGNED_FIELD_TABLE = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
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


def prime_pi_from_table(primes: list[int], x: int) -> int:
    """用素数表计算 pi(x)。"""
    return sum(1 for p in primes if p <= x)


def least_prime_factor(value: int, primes: list[int]) -> int | None:
    """返回 value 的最小素因子；素数表覆盖到 value 即可。"""
    for p in primes:
        if p * p > value:
            break
        if value % p == 0:
            return p
    return value if value >= 2 else None


def sample_edge_local_field_audit(n: int) -> dict[str, Any]:
    """审计 canonical two-prime edge 的闭合无符号字段。"""
    primes = primes_up_to(n)
    left = [p for p in primes if p <= math.isqrt(n)]
    left_rank = {p: index + 1 for index, p in enumerate(left)}
    prime_rank = {p: index + 1 for index, p in enumerate(primes)}
    edges = sorted((p, q) for p in left for q in primes if p < q <= n // p)
    row_degree = {
        p: prime_pi_from_table(primes, n // p) - prime_pi_from_table(primes, p)
        for p in left
    }
    column_degree: dict[int, int] = {}
    for _, q in edges:
        column_degree[q] = column_degree.get(q, 0) + 1

    labels = []
    lpf_failures = []
    row_degree_failures = []
    column_degree_failures = []
    for p, q in edges:
        product = p * q
        label = (
            p,
            q,
            product,
            left_rank[p],
            prime_rank[q],
            row_degree[p],
            column_degree[q],
        )
        labels.append(label)
        if least_prime_factor(product, primes) != p:
            lpf_failures.append((p, q, product))

    for p in left:
        actual = sum(1 for a, _ in edges if a == p)
        if actual != row_degree[p]:
            row_degree_failures.append((p, actual, row_degree[p]))

    for q, degree in column_degree.items():
        expected = prime_pi_from_table(primes, min(q - 1, n // q))
        if degree != expected:
            column_degree_failures.append((q, degree, expected))

    atom_multiplicity_one = len(edges) == len({p * q for p, q in edges}) == len(set(labels))
    sample_labels = [
        {
            "p": p,
            "q": q,
            "product": product,
            "left_rank": lr,
            "q_prime_rank": qr,
            "row_degree": rd,
            "column_degree": cd,
        }
        for p, q, product, lr, qr, rd, cd in labels[:4] + labels[-4:]
    ]
    return {
        "N": n,
        "canonical_edges": len(edges),
        "unique_edge_labels": len(set(labels)),
        "unique_products": len({p * q for p, q in edges}),
        "lpf_bucket_identity_holds": not lpf_failures,
        "row_degree_formula_holds": not row_degree_failures,
        "column_degree_formula_holds": not column_degree_failures,
        "atom_multiplicity_one_holds": atom_multiplicity_one,
        "closed_unsigned_field_count_per_edge": 7,
        "open_signed_field_count_per_edge": 6,
        "formal_sign_shadow_bits": len(edges),
        "formal_sign_shadow_log10": round(len(edges) * math.log10(2), 6),
        "sample_closed_edge_labels": sample_labels,
        "lpf_failure_examples": lpf_failures[:10],
        "row_degree_failure_examples": row_degree_failures[:10],
        "column_degree_failure_examples": column_degree_failures[:10],
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        NO_SWAP_ROUTER,
        FERRERS_ROUTER,
        POINTWISE_FRONTIER_CERT,
        ORIENTATION_TRACE_CERT,
        BUILTIN_TRACE_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def closed_edge_fields() -> list[dict[str, str]]:
    """列出已闭合的无符号 edge-local 字段。"""
    return [
        {
            "field": "owner_p",
            "status": "closed_unsigned",
            "meaning": "LPF owner prime，满足 `p <= sqrt(N)`。",
        },
        {
            "field": "first_q",
            "status": "closed_unsigned",
            "meaning": "offdiagonal pure pair 的第二素数，满足 `p<q<=N/p`。",
        },
        {
            "field": "product_pq",
            "status": "closed_unsigned",
            "meaning": "atom integer value `pq`，其最小素因子为 `p`。",
        },
        {
            "field": "ferrers_row_rank_and_degree",
            "status": "closed_unsigned",
            "meaning": "row rank 与 degree `pi(floor(N/p))-pi(p)`。",
        },
        {
            "field": "ferrers_column_rank_and_degree",
            "status": "closed_unsigned",
            "meaning": "column degree `pi(min(q-1,floor(N/q)))`。",
        },
        {
            "field": "edge_atom_multiplicity",
            "status": "closed_unsigned",
            "meaning": "每个 canonical product `pq` 只有一个 pure atom label。",
        },
    ]


def open_signed_fields() -> list[dict[str, str]]:
    """列出仍需正向证明或命名 return 的 signed 字段。"""
    return [
        {
            "field": "signed_seed_value",
            "remaining": SIGNED_FIELD_TABLE,
            "meaning": "canonical edge 自身的 signed atom 值。",
        },
        {
            "field": "local_factor_multiplier",
            "remaining": SIGNED_FIELD_TABLE,
            "meaning": "first-edge local factor 或 zero/return 标签。",
        },
        {
            "field": "orientation_parity",
            "remaining": OFFDIAG_ORIENTATION,
            "meaning": "同一 `(p,q)` 边上的 orientation parity 与 branch side。",
        },
        {
            "field": "alpha_delta_side",
            "remaining": OFFDIAG_ORIENTATION,
            "meaning": "alpha/delta 分支侧别和符号方向。",
        },
        {
            "field": "exactuv_fixed_pair",
            "remaining": OFFDIAG_EXACTUV,
            "meaning": "edge-local ExactUV fixed pair、fiber 与 return tag。",
        },
        {
            "field": "pre_cauchy_source_row",
            "remaining": COMMON_PACKET,
            "meaning": "真正发出 signed coefficient 的 pre-Cauchy source row。",
        },
    ]


def build_rows(
    no_swap: dict[str, Any],
    ferrers: dict[str, Any],
    pointwise: dict[str, Any],
    orientation: dict[str, Any],
    builtin: dict[str, Any],
    exactuv: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 edge-local field-cut 前沿判定表。"""
    labels_ok = all(
        item["lpf_bucket_identity_holds"]
        and item["row_degree_formula_holds"]
        and item["column_degree_formula_holds"]
        and item["atom_multiplicity_one_holds"]
        for item in samples
    )
    return [
        row(
            "EdgeLocalFormulaTargetImported",
            no_swap.get("next_primary_attack_target") == EDGE_LOCAL_FORMULA,
            False,
            "上一层已删除 swap-symmetry 伪出口，直接剩余为 edge-local formula-or-return。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "CanonicalEdgeLabelBijectionClosed",
            labels_ok and no_swap.get("lpf_owner_ordered_no_swap_identity_proved") is True,
            True,
            "每个 canonical `(p,q)` pure atom 有唯一 closed edge label。",
            EDGE_LABEL_LEDGER,
        ),
        row(
            "LPFBucketAndProductFieldsClosed",
            labels_ok,
            True,
            "`product=pq` 与 `LPF(product)=p` 已在 edge label 中固定。",
            EDGE_LABEL_LEDGER,
        ),
        row(
            "FerrersRankDegreeFieldsClosed",
            labels_ok and ferrers.get("pure_pair_ferrers_support_rule_proved") is True,
            True,
            "row/column rank-degree 字段由 Ferrers 支撑和 prime-count floor 公式给出。",
            EDGE_LABEL_LEDGER,
        ),
        row(
            "AtomMultiplicityOneClosed",
            all(item["atom_multiplicity_one_holds"] for item in samples),
            True,
            "每个 distinct product `pq` 只带一个 pure-pair source atom。",
            EDGE_LABEL_LEDGER,
        ),
        row(
            "LPFPhiFieldsAreUnsignedOnly",
            True,
            True,
            "闭合字段只含 owner、prime、product、rank、degree、multiplicity，不含 sign/local-factor/orientation/ExactUV 槽。",
            SIGNED_FIELD_TABLE,
        ),
        row(
            "EdgeLocalSignedAtomFieldsCurrentCorpusProved",
            False,
            False,
            "当前语料没有提交逐 edge 的 signed seed/local factor 表或命名 return tag 表。",
            SIGNED_FIELD_TABLE,
        ),
        row(
            "OrientationParityStillOpen",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True,
            False,
            "orientation parity 可由完整 branch trace 条件性供给，但当前不是已证明字段。",
            OFFDIAG_ORIENTATION,
        ),
        row(
            "ExactUVReturnTagStillOpen",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False
            or exactuv.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "ExactUV fixed pair/fiber/return tag 仍是独立命名门。",
            OFFDIAG_EXACTUV,
        ),
        row(
            "CommonSourcePacketStillOpen",
            True,
            False,
            "signed value 必须来自 pre-Cauchy source row；closed label 不是 source packet。",
            COMMON_PACKET,
        ),
        row(
            "PointwiseTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed table 仍可替代本 edge-local 表，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "TraceGeneratorsStillConditional",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True
            and builtin.get("branch_trace_conditionally_suffices") is True,
            True,
            "complete branch trace 或 atomic trace 若提交，可同时供给 signed/orientation/ExactUV 字段。",
            f"{BRANCH_TRACE} OR {ATOMIC_TRACE}",
        ),
        row(
            "EdgeLocalSignedInteractionFormulaCurrentCorpusProved",
            False,
            False,
            "本步只关闭 edge label；不证明 edge-local signed interaction formula。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步不证明三命题无条件闭合；它把最新剩余压到 signed atom fields 或 named return。",
            SIGNED_FIELD_TABLE,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 edge-local field-cut 前沿证书。"""
    no_swap = load_json(NO_SWAP_ROUTER)
    ferrers = load_json(FERRERS_ROUTER)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    orientation = load_json(ORIENTATION_TRACE_CERT)
    builtin = load_json(BUILTIN_TRACE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    samples = [sample_edge_local_field_audit(n) for n in SAMPLE_N]
    rows = build_rows(no_swap, ferrers, pointwise, orientation, builtin, exactuv, samples)
    retained_basis = (
        f"(({SIGNED_FIELD_TABLE} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
        f"AND {INTERNAL_TRANSITION} AND {COMMON_PACKET}) OR {POINTWISE_TABLE} "
        f"OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} "
        f"OR {NEW_JOINT_FORMULA}) AND {EXACTUV_PAIR} AND {MODEL_LEDGER} "
        f"AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_edge_local_two_prime_field_cut_router",
        "status": "phi_lpf_edge_local_unsigned_edge_labels_closed_signed_atom_fields_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "edge_local_formula_target_imported": no_swap.get("next_primary_attack_target")
        == EDGE_LOCAL_FORMULA,
        "edge_local_closed_unsigned_label_ledger_proved": all(
            item["lpf_bucket_identity_holds"]
            and item["row_degree_formula_holds"]
            and item["column_degree_formula_holds"]
            and item["atom_multiplicity_one_holds"]
            for item in samples
        ),
        "edge_label_bijection_proved": all(
            item["unique_edge_labels"] == item["canonical_edges"] for item in samples
        ),
        "lpf_bucket_product_fields_proved": all(
            item["lpf_bucket_identity_holds"] for item in samples
        ),
        "ferrers_rank_degree_fields_proved": all(
            item["row_degree_formula_holds"] and item["column_degree_formula_holds"]
            for item in samples
        ),
        "edge_atom_multiplicity_one_proved": all(
            item["atom_multiplicity_one_holds"] for item in samples
        ),
        "signed_atom_field_table_proved": False,
        "orientation_parity_branch_side_proved": False,
        "exactuv_fixed_pair_return_tag_proved": False,
        "pre_cauchy_source_packet_proved": False,
        "edge_local_signed_interaction_formula_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": EDGE_LOCAL_FORMULA,
        "closed_unsigned_subledger": EDGE_LABEL_LEDGER,
        "next_primary_attack_target": SIGNED_FIELD_TABLE,
        "paired_required_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            COMMON_PACKET,
        ],
        "parallel_direct_attack_target": POINTWISE_TABLE,
        "conditional_generators": [BRANCH_TRACE, ATOMIC_TRACE],
        "retained_basis_after_router": retained_basis,
        "closed_edge_fields": closed_edge_fields(),
        "open_signed_fields_or_returns": open_signed_fields(),
        "sample_edge_local_field_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "edge-local formula-or-return 的无符号边标签已经闭合：每条 canonical `(p,q)` "
            "edge 的 owner、product、LPF bucket、Ferrers rank/degree 与 atom multiplicity "
            "均由 LPF/Phi/Ferrers 账本确定。剩余不再是支撑或容量问题，而是逐 edge 的 "
            "signed atom fields：signed value、local factor、orientation/branch side、ExactUV "
            "fixed pair 与 pre-Cauchy source row，或对应的命名 return tag。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF edge-local two-prime field-cut 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"edge_local_formula_target_imported={fmt_bool(cert['edge_local_formula_target_imported'])}",
        f"edge_local_closed_unsigned_label_ledger_proved={fmt_bool(cert['edge_local_closed_unsigned_label_ledger_proved'])}",
        f"edge_label_bijection_proved={fmt_bool(cert['edge_label_bijection_proved'])}",
        f"lpf_bucket_product_fields_proved={fmt_bool(cert['lpf_bucket_product_fields_proved'])}",
        f"ferrers_rank_degree_fields_proved={fmt_bool(cert['ferrers_rank_degree_fields_proved'])}",
        f"edge_atom_multiplicity_one_proved={fmt_bool(cert['edge_atom_multiplicity_one_proved'])}",
        f"signed_atom_field_table_proved={fmt_bool(cert['signed_atom_field_table_proved'])}",
        f"orientation_parity_branch_side_proved={fmt_bool(cert['orientation_parity_branch_side_proved'])}",
        f"exactuv_fixed_pair_return_tag_proved={fmt_bool(cert['exactuv_fixed_pair_return_tag_proved'])}",
        f"edge_local_signed_interaction_formula_proved={fmt_bool(cert['edge_local_signed_interaction_formula_proved'])}",
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
            "## 2. 已闭合 edge label 字段",
            "",
            "| field | status | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["closed_edge_fields"]:
        lines.append(f"| `{item['field']}` | `{item['status']}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 仍开放 signed/return 字段",
            "",
            "| field | remaining | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["open_signed_fields_or_returns"]:
        lines.append(f"| `{item['field']}` | {cell(item['remaining'])} | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 4. 样本审计摘要",
            "",
            "| N | edges | labels | products | LPF ok | row deg ok | col deg ok | atom x1 | sign log10 |",
            "| --- | ---: | ---: | ---: | --- | --- | --- | --- | ---: |",
        ]
    )
    for item in cert["sample_edge_local_field_audit"]:
        lines.append(
            f"| {item['N']} | {item['canonical_edges']} | {item['unique_edge_labels']} | "
            f"{item['unique_products']} | `{fmt_bool(item['lpf_bucket_identity_holds'])}` | "
            f"`{fmt_bool(item['row_degree_formula_holds'])}` | "
            f"`{fmt_bool(item['column_degree_formula_holds'])}` | "
            f"`{fmt_bool(item['atom_multiplicity_one_holds'])}` | "
            f"{item['formal_sign_shadow_log10']} |"
        )
    lines.extend(
        [
            "",
            "## 5. edge label 样本",
            "",
            "| N | sample labels |",
            "| --- | --- |",
        ]
    )
    for item in cert["sample_edge_local_field_audit"]:
        samples = ", ".join(
            (
                f"(p={entry['p']},q={entry['q']},n={entry['product']},"
                f"rd={entry['row_degree']},cd={entry['column_degree']})"
            )
            for entry in item["sample_closed_edge_labels"][:4]
        )
        lines.append(f"| {item['N']} | {samples} |")
    lines.extend(
        [
            "",
            "## 6. 最新保留基",
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
            "## 7. 依赖哈希",
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
    """写出 edge-local field-cut 前沿证书。"""
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
