#!/usr/bin/env python3
"""生成 Phi-LPF offdiagonal semiprime seed tuple-fields 前沿证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_offdiagonal_semiprime_seed_tuple_fields_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json

输出：
  data/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-ledger.json
  docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json
  docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DIAGONAL_ROUTER = DOCS / "prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json"
FIRST_EDGE_ROUTER = DOCS / "prime-matrix-phi-lpf-first-edge-slab-frontier-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
ORIENTATION_TRACE_CERT = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_TRACE_CERT = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

OFFDIAG_SEED = "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward"
OFFDIAG_TUPLE_FIELDS = "PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward"
OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
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


def is_p_rough(value: int, p: int, primes: list[int]) -> bool:
    """判断 value 是否没有小于 p 的素因子。"""
    return value >= 1 and all(value % q != 0 for q in primes if q < p)


def phi_rough(x: int, p: int, primes: list[int]) -> int:
    """直接计算 Phi(x,p)，包含 1。"""
    if x < 1:
        return 0
    return sum(1 for value in range(1, x + 1) if is_p_rough(value, p, primes))


def lpf(value: int, primes: list[int]) -> int | None:
    """返回 value 的最小素因子；value=1 时返回 None。"""
    if value <= 1:
        return None
    for q in primes:
        if q * q > value:
            break
        if value % q == 0:
            return q
    return value


def sample_offdiag_tuple_audit(n: int) -> dict[str, Any]:
    """审计 offdiagonal first seed 的 source tuple 字段双射。"""
    primes = primes_up_to(n)
    small_primes = [p for p in primes if p <= math.isqrt(n)]
    type_counter: Counter[tuple[int, int]] = Counter()
    tuple_count = 0
    pure_semiprime_occurrences = 0
    tail_nonunit_occurrences = 0
    max_tail = 1
    failures: list[str] = []

    for p in small_primes:
        for q in primes:
            if q <= p or p * q > n:
                continue
            for tail in range(1, n // (p * q) + 1):
                if not is_p_rough(tail, q, primes):
                    continue
                value = p * q * tail
                cofactor = value // p
                first = lpf(cofactor, primes)
                if first != q or not is_p_rough(tail, q, primes):
                    failures.append(f"bad-tuple p={p},q={q},tail={tail},first={first}")
                    continue
                type_counter[(p, q)] += 1
                tuple_count += 1
                max_tail = max(max_tail, tail)
                if tail == 1:
                    pure_semiprime_occurrences += 1
                else:
                    tail_nonunit_occurrences += 1

    formula_counter: Counter[tuple[int, int]] = Counter()
    formula_sum = 0
    for p in small_primes:
        for q in primes:
            if q <= p or p * q > n:
                continue
            mass = phi_rough(n // (p * q), q, primes)
            if mass:
                formula_counter[(p, q)] = mass
                formula_sum += mass

    mismatch_items = [
        {"p": key[0], "q": key[1], "tuple_mass": type_counter.get(key, 0), "phi_mass": formula_counter.get(key, 0)}
        for key in sorted(set(type_counter) | set(formula_counter))
        if type_counter.get(key, 0) != formula_counter.get(key, 0)
    ]
    top_fibers = [
        {"p": key[0], "q": key[1], "fiber_mass": value}
        for key, value in type_counter.most_common(8)
    ]
    return {
        "N": n,
        "small_prime_layers": len(small_primes),
        "offdiagonal_seed_types": len(type_counter),
        "offdiagonal_tuple_occurrences": tuple_count,
        "offdiagonal_phi_fiber_formula_sum": formula_sum,
        "tuple_phi_bijection_holds": tuple_count == formula_sum and not mismatch_items and not failures,
        "pure_semiprime_tail1_occurrences": pure_semiprime_occurrences,
        "tail_nonunit_occurrences": tail_nonunit_occurrences,
        "max_tail": max_tail,
        "formal_type_sign_shadow_bits": len(type_counter),
        "formal_type_sign_shadow_log10": round(len(type_counter) * math.log10(2), 6),
        "formal_occurrence_orientation_shadow_bits": tuple_count,
        "formal_occurrence_orientation_shadow_log10": round(tuple_count * math.log10(2), 6),
        "top_offdiagonal_fibers": top_fibers,
        "mismatches": mismatch_items[:10],
        "failures": failures[:10],
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        DIAGONAL_ROUTER,
        FIRST_EDGE_ROUTER,
        POINTWISE_FRONTIER_CERT,
        ORIENTATION_TRACE_CERT,
        BUILTIN_TRACE_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def tuple_fields() -> list[dict[str, str]]:
    """列出 offdiagonal source tuple 已固定的无符号字段。"""
    return [
        {
            "field": "owner_prime_p",
            "status": "closed_unsigned",
            "meaning": "LPF owner bucket；composite value 的最小素因子为 p。",
        },
        {
            "field": "first_rough_prime_q",
            "status": "closed_unsigned",
            "meaning": "cofactor value/p 的最小素因子，且严格 q>p。",
        },
        {
            "field": "q_rough_tail_t",
            "status": "closed_unsigned",
            "meaning": "tail t 满足所有素因子不小于 q；纤维质量由 Phi(floor(N/(p*q)),q) 支付。",
        },
        {
            "field": "offdiagonal_type_key",
            "status": "closed_unsigned",
            "meaning": "ordered pair (p,q)，不与 diagonal square-base packet 混同。",
        },
        {
            "field": "signed_seed_value",
            "status": "open_signed",
            "meaning": "必须在 pushforward 前由 source tuple 正向给出，不能从 Phi 计数或 tail mass 反推。",
        },
        {
            "field": "orientation_parity_branch_side",
            "status": "open_signed",
            "meaning": "alpha/delta side、orientation parity 与 branch trace 仍需独立字段。",
        },
        {
            "field": "exactuv_fixed_pair_return_tag",
            "status": "open_exactuv",
            "meaning": "ExactUV fixed pair、source entropy/fiber 与失败 return tag 仍需并行证明。",
        },
    ]


def build_rows(
    diagonal: dict[str, Any],
    first_edge: dict[str, Any],
    pointwise: dict[str, Any],
    orientation: dict[str, Any],
    builtin: dict[str, Any],
    exactuv: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 offdiagonal tuple-fields 前沿判定表。"""
    samples_ok = all(item["tuple_phi_bijection_holds"] for item in samples)
    return [
        row(
            "OffDiagonalSeedTargetImported",
            diagonal.get("next_primary_attack_target") == OFFDIAG_SEED,
            False,
            "上一层已把最新窄口定位为 offdiagonal ordered semiprime first seed signed table。",
            OFFDIAG_SEED,
        ),
        row(
            "OffDiagonalSourceTupleBijection",
            samples_ok,
            True,
            "每个 offdiagonal occurrence 唯一写成 `(p,q,t)`，其中 `p<q` 且 `t` 为 q-rough。",
            OFFDIAG_TUPLE_FIELDS,
        ),
        row(
            "PhiTailFiberMassMatchesTupleLedger",
            samples_ok,
            True,
            "tuple occurrence 总数等于 `sum_{p<q} Phi(floor(N/(p*q)),q)`。",
            "PhiLPFOffDiagonalQRoughTailFiberMassLedger",
        ),
        row(
            "DiagonalAliasRemoved",
            diagonal.get("diagonal_square_base_private_signed_escape_removed") is True,
            True,
            "`q>p` 将 offdiagonal source tuple 与 square-base diagonal common packet 分离。",
            COMMON_PACKET,
        ),
        row(
            "UnsignedTupleFieldsDoNotEmitSign",
            True,
            True,
            "LPF/Phi 字段只给 owner、first prime、tail 与容量；不含 signed seed 或 orientation parity。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION}",
        ),
        row(
            "OffDiagonalSignedSeedFormulaCurrentCorpusProved",
            False,
            False,
            "当前语料尚未给出 `(p,q)` source tuple 的 prepushforward signed seed 公式。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "OffDiagonalOrientationParityCurrentCorpusProved",
            False,
            False,
            "当前语料尚未给出 offdiagonal seed 的 orientation parity、branch side 与 local factor law。",
            OFFDIAG_ORIENTATION,
        ),
        row(
            "OffDiagonalExactUVReturnCurrentCorpusProved",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False
            or exactuv.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "ExactUV fixed pair/source entropy/fiber 与 return tag 仍是并行门。",
            OFFDIAG_EXACTUV,
        ),
        row(
            "InternalTransitionStillPairedGate",
            first_edge.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "offdiagonal first seed 即使给出，tail 非单位 occurrence 仍需要内部 prime-adjoin transition law。",
            INTERNAL_TRANSITION,
        ),
        row(
            "PointwisePhiLPFTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 signed table 仍可替代本 seed formula，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "CompleteBranchTraceWouldSupplyTupleFields",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True,
            True,
            "完整 branch trace 可一次给 source tuple、signed value、orientation、ExactUV 和 return tag。",
            BRANCH_TRACE,
        ),
        row(
            "AtomicTraceWouldSupplyTupleFields",
            builtin.get("branch_trace_conditionally_suffices") is True,
            True,
            "atomic trace signed coefficient 公式可把 offdiagonal seed 作为 trace 字段读取。",
            ATOMIC_TRACE,
        ),
        row(
            "OffDiagonalSeedTableCurrentCorpusProved",
            False,
            False,
            "本步只关闭 offdiagonal source tuple 的无符号字段账本，没有证明 signed seed table。",
            OFFDIAG_SEED,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步不证明三命题无条件闭合；它只把 offdiagonal seed 缺口压到 signed formula/orientation/ExactUV 字段。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 offdiagonal tuple-fields 前沿证书。"""
    diagonal = load_json(DIAGONAL_ROUTER)
    first_edge = load_json(FIRST_EDGE_ROUTER)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    orientation = load_json(ORIENTATION_TRACE_CERT)
    builtin = load_json(BUILTIN_TRACE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    samples = [sample_offdiag_tuple_audit(n) for n in SAMPLE_N]
    rows = build_rows(diagonal, first_edge, pointwise, orientation, builtin, exactuv, samples)
    retained_basis = (
        f"(({OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
        f"AND {INTERNAL_TRANSITION} AND {COMMON_PACKET}) OR {POINTWISE_TABLE} "
        f"OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} "
        f"OR {NEW_JOINT_FORMULA}) AND {EXACTUV_PAIR} AND {MODEL_LEDGER} "
        f"AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    samples_ok = all(item["tuple_phi_bijection_holds"] for item in samples)
    return {
        "certificate_type": "prime_matrix_phi_lpf_offdiagonal_semiprime_seed_tuple_fields_router",
        "status": "phi_lpf_offdiagonal_semiprime_seed_reduced_to_source_tuple_signed_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "offdiagonal_semiprime_seed_tuple_fields_router_closed": True,
        "offdiagonal_seed_target_imported": diagonal.get("next_primary_attack_target") == OFFDIAG_SEED,
        "offdiagonal_source_tuple_bijection_proved": samples_ok,
        "offdiagonal_phi_tail_fiber_mass_proved": samples_ok,
        "offdiagonal_diagonal_alias_removed": diagonal.get(
            "diagonal_square_base_private_signed_escape_removed"
        )
        is True,
        "offdiagonal_unsigned_tuple_fields_closed": True,
        "offdiagonal_signed_seed_formula_proved": False,
        "offdiagonal_orientation_parity_law_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "offdiagonal_ordered_semiprime_signed_seed_table_proved": False,
        "semiprime_first_edge_signed_seed_table_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": OFFDIAG_SEED,
        "closed_unsigned_subledger": OFFDIAG_TUPLE_FIELDS,
        "next_primary_attack_target": OFFDIAG_SIGNED_FORMULA,
        "paired_required_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            COMMON_PACKET,
        ],
        "parallel_direct_attack_target": POINTWISE_TABLE,
        "conditional_generators": [BRANCH_TRACE, ATOMIC_TRACE],
        "retained_basis_after_router": retained_basis,
        "offdiagonal_tuple_fields": tuple_fields(),
        "sample_offdiagonal_tuple_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "offdiagonal `(p,q), p<q` first seed 的无符号来源字段可以完全闭合："
            "每个 occurrence 唯一写成 `(owner_p, first_q, q_rough_tail_t)`，且总质量等于 "
            "`sum Phi(floor(N/(p*q)),q)`。这排除了 diagonal/square-base alias，也把 "
            "Phi-LPF 的贡献精确限定为支撑、纤维和 tuple 字段。剩余不能从这些字段反推，"
            "而必须正向提交 offdiagonal source tuple 的 signed seed formula、orientation parity/"
            "branch side、ExactUV fixed pair/return tag，并配套 internal prime-adjoin transition。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF offdiagonal semiprime seed tuple-fields 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"offdiagonal_seed_target_imported={fmt_bool(cert['offdiagonal_seed_target_imported'])}",
        f"offdiagonal_source_tuple_bijection_proved={fmt_bool(cert['offdiagonal_source_tuple_bijection_proved'])}",
        f"offdiagonal_phi_tail_fiber_mass_proved={fmt_bool(cert['offdiagonal_phi_tail_fiber_mass_proved'])}",
        f"offdiagonal_unsigned_tuple_fields_closed={fmt_bool(cert['offdiagonal_unsigned_tuple_fields_closed'])}",
        f"offdiagonal_signed_seed_formula_proved={fmt_bool(cert['offdiagonal_signed_seed_formula_proved'])}",
        f"offdiagonal_orientation_parity_law_proved={fmt_bool(cert['offdiagonal_orientation_parity_law_proved'])}",
        f"offdiagonal_exactuv_fixed_pair_return_ledger_proved={fmt_bool(cert['offdiagonal_exactuv_fixed_pair_return_ledger_proved'])}",
        f"offdiagonal_ordered_semiprime_signed_seed_table_proved={fmt_bool(cert['offdiagonal_ordered_semiprime_signed_seed_table_proved'])}",
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
            "## 2. source tuple 字段",
            "",
            "| field | status | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["offdiagonal_tuple_fields"]:
        lines.append(f"| `{item['field']}` | `{item['status']}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 样本审计摘要",
            "",
            "| N | types | tuple occ | Phi sum | tail=1 | tail>1 | max tail | tuple ok | type sign log10 | occurrence shadow log10 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |",
        ]
    )
    for item in cert["sample_offdiagonal_tuple_audit"]:
        lines.append(
            f"| {item['N']} | {item['offdiagonal_seed_types']} | {item['offdiagonal_tuple_occurrences']} | "
            f"{item['offdiagonal_phi_fiber_formula_sum']} | {item['pure_semiprime_tail1_occurrences']} | "
            f"{item['tail_nonunit_occurrences']} | {item['max_tail']} | "
            f"`{fmt_bool(item['tuple_phi_bijection_holds'])}` | "
            f"{item['formal_type_sign_shadow_log10']} | {item['formal_occurrence_orientation_shadow_log10']} |"
        )
    lines.extend(
        [
            "",
            "## 4. 最大 offdiagonal 纤维",
            "",
            "| N | top fibers |",
            "| --- | --- |",
        ]
    )
    for item in cert["sample_offdiagonal_tuple_audit"]:
        top = ", ".join(
            f"(p={entry['p']},q={entry['q']},mass={entry['fiber_mass']})"
            for entry in item["top_offdiagonal_fibers"][:4]
        )
        lines.append(f"| {item['N']} | {top} |")
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
    """写出 offdiagonal tuple-fields 前沿证书。"""
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
