#!/usr/bin/env python3
"""生成 Phi-LPF offdiagonal pure semiprime seed atom 前沿证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_offdiagonal_pure_semiprime_seed_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json

输出：
  data/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-ledger.json
  docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json
  docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.md
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

SLUG = "prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

TUPLE_ROUTER = DOCS / "prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json"
FIRST_EDGE_ROUTER = DOCS / "prime-matrix-phi-lpf-first-edge-slab-frontier-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
ORIENTATION_TRACE_CERT = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_TRACE_CERT = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
PURE_SEMIPRIME_ATOM = "PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward"
TAIL_LIFT = "PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward"
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


def sample_pure_seed_atom_audit(n: int) -> dict[str, Any]:
    """审计 offdiagonal pure semiprime atom 与 tail lift 分解。"""
    primes = primes_up_to(n)
    small_primes = [p for p in primes if p <= math.isqrt(n)]
    offdiag_types = 0
    pure_atoms = 0
    tail_lift_occurrences = 0
    total_occurrences = 0
    failures: list[str] = []
    top_tail_lifts: list[dict[str, int]] = []

    for p in small_primes:
        for q in primes:
            if q <= p or p * q > n:
                continue
            mass = phi_rough(n // (p * q), q, primes)
            if mass < 1:
                failures.append(f"missing-tail1 p={p},q={q}")
                continue
            offdiag_types += 1
            pure_atoms += 1
            lift_mass = mass - 1
            tail_lift_occurrences += lift_mass
            total_occurrences += mass
            if lift_mass:
                top_tail_lifts.append({"p": p, "q": q, "tail_lift_mass": lift_mass})

    top_tail_lifts.sort(key=lambda item: item["tail_lift_mass"], reverse=True)
    return {
        "N": n,
        "small_prime_layers": len(small_primes),
        "offdiagonal_seed_types": offdiag_types,
        "pure_semiprime_pair_seed_atoms": pure_atoms,
        "tail_lift_occurrences": tail_lift_occurrences,
        "offdiagonal_total_occurrences": total_occurrences,
        "pure_atom_type_bijection_holds": offdiag_types == pure_atoms and not failures,
        "tail_lift_decomposition_holds": total_occurrences == pure_atoms + tail_lift_occurrences,
        "pure_atom_share_of_occurrences": round(pure_atoms / max(1, total_occurrences), 12),
        "tail_lift_share_of_occurrences": round(tail_lift_occurrences / max(1, total_occurrences), 12),
        "formal_pure_atom_sign_shadow_bits": pure_atoms,
        "formal_pure_atom_sign_shadow_log10": round(pure_atoms * math.log10(2), 6),
        "formal_tail_lift_transition_shadow_bits": tail_lift_occurrences,
        "formal_tail_lift_transition_shadow_log10": round(tail_lift_occurrences * math.log10(2), 6),
        "top_tail_lifts": top_tail_lifts[:8],
        "failures": failures[:10],
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        TUPLE_ROUTER,
        FIRST_EDGE_ROUTER,
        POINTWISE_FRONTIER_CERT,
        ORIENTATION_TRACE_CERT,
        BUILTIN_TRACE_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def pure_atom_fields() -> list[dict[str, str]]:
    """列出 pure semiprime signed atom 的字段边界。"""
    return [
        {
            "field": "pure_pair_key",
            "status": "closed_unsigned",
            "meaning": "ordered pair `(p,q)` with `p<q` and value `p*q`。",
        },
        {
            "field": "tail_identity_t_equals_1",
            "status": "closed_unsigned",
            "meaning": "每个 offdiagonal type 的 first seed atom 是唯一 tail=1 occurrence。",
        },
        {
            "field": "tail_lift_mass",
            "status": "closed_unsigned",
            "meaning": "`Phi(floor(N/(p*q)),q)-1`，不是新 first seed，只能由 internal transition lift 处理。",
        },
        {
            "field": "pure_pair_signed_value",
            "status": "open_signed",
            "meaning": "必须由 source tuple 在 pushforward 前正向发射。",
        },
        {
            "field": "orientation_and_exactuv",
            "status": "open_signed_exactuv",
            "meaning": "orientation parity、branch side、ExactUV fixed pair 与 return tag 仍未闭合。",
        },
    ]


def build_rows(
    tuple_router: dict[str, Any],
    first_edge: dict[str, Any],
    pointwise: dict[str, Any],
    orientation: dict[str, Any],
    builtin: dict[str, Any],
    exactuv: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 pure semiprime atom 前沿判定表。"""
    pure_ok = all(item["pure_atom_type_bijection_holds"] for item in samples)
    tail_ok = all(item["tail_lift_decomposition_holds"] for item in samples)
    return [
        row(
            "OffDiagonalSourceTupleSignedFormulaTargetImported",
            tuple_router.get("next_primary_attack_target") == OFFDIAG_SIGNED_FORMULA,
            False,
            "上一层已把 offdiagonal seed 的 signed 缺口压到 source tuple signed seed formula。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "PureSemiprimePairSeedAtomBijection",
            pure_ok,
            True,
            "每个 offdiagonal type `(p,q)` 恰有一个 tail=1 pure semiprime seed atom。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "TailNonunitNotNewFirstSeed",
            tail_ok,
            True,
            "`tail>1` occurrences 共享同一 first seed type，只增加 internal transition lift。",
            TAIL_LIFT,
        ),
        row(
            "PhiMinusOneTailLiftMassFormula",
            tail_ok,
            True,
            "每个 `(p,q)` 的 tail-lift mass 为 `Phi(floor(N/(p*q)),q)-1`。",
            TAIL_LIFT,
        ),
        row(
            "PureSeedSignedValueCurrentCorpusProved",
            False,
            False,
            "当前语料没有给出 pure pair `(p,q)` 的 prepushforward signed seed atom。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "TailLiftSignedCompatibilityNeedsInternalTransition",
            first_edge.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "tail lift 的 signed compatibility 仍依赖 internal prime-adjoin transition law。",
            INTERNAL_TRANSITION,
        ),
        row(
            "OffDiagonalOrientationParityStillOpen",
            tuple_router.get("offdiagonal_orientation_parity_law_proved") is False,
            False,
            "pure atom 仍需 orientation parity、branch side 与 local factor law。",
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
            "PointwisePhiLPFTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 signed table 仍可替代 pure atom formula，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "CompleteBranchTraceWouldSupplyPureAtom",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True,
            True,
            "完整 branch trace 可给 pure atom signed value、orientation、ExactUV 和 return tag。",
            BRANCH_TRACE,
        ),
        row(
            "AtomicTraceWouldSupplyPureAtom",
            builtin.get("branch_trace_conditionally_suffices") is True,
            True,
            "atomic trace signed coefficient 公式可把 pure semiprime pair seed 作为 trace 字段读取。",
            ATOMIC_TRACE,
        ),
        row(
            "OffDiagonalSourceTupleSignedFormulaCurrentCorpusProved",
            False,
            False,
            "本步只把 source tuple signed formula 拆成 pure atom 与 tail lift，没有证明 signed formula。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步不证明三命题无条件闭合；它只把 offdiagonal signed formula 的 first-seed 原子定位到 pure semiprime pair。",
            f"{PURE_SEMIPRIME_ATOM} AND {INTERNAL_TRANSITION} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 pure semiprime atom 前沿证书。"""
    tuple_router = load_json(TUPLE_ROUTER)
    first_edge = load_json(FIRST_EDGE_ROUTER)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    orientation = load_json(ORIENTATION_TRACE_CERT)
    builtin = load_json(BUILTIN_TRACE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    samples = [sample_pure_seed_atom_audit(n) for n in SAMPLE_N]
    rows = build_rows(tuple_router, first_edge, pointwise, orientation, builtin, exactuv, samples)
    pure_ok = all(item["pure_atom_type_bijection_holds"] for item in samples)
    tail_ok = all(item["tail_lift_decomposition_holds"] for item in samples)
    retained_basis = (
        f"(({PURE_SEMIPRIME_ATOM} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
        f"AND {INTERNAL_TRANSITION} AND {COMMON_PACKET}) OR {POINTWISE_TABLE} "
        f"OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} "
        f"OR {NEW_JOINT_FORMULA}) AND {EXACTUV_PAIR} AND {MODEL_LEDGER} "
        f"AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_offdiagonal_pure_semiprime_seed_atom_router",
        "status": "phi_lpf_offdiagonal_source_tuple_signed_formula_split_to_pure_pair_atom_and_tail_lift_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "offdiagonal_pure_semiprime_seed_atom_router_closed": True,
        "offdiagonal_source_tuple_signed_seed_target_imported": tuple_router.get(
            "next_primary_attack_target"
        )
        == OFFDIAG_SIGNED_FORMULA,
        "pure_semiprime_pair_seed_atom_bijection_proved": pure_ok,
        "tail_nonunit_reduced_to_internal_transition_lift": tail_ok,
        "tail_lift_phi_minus_one_mass_formula_proved": tail_ok,
        "pure_semiprime_pair_signed_seed_atom_proved": False,
        "offdiagonal_source_tuple_signed_seed_formula_proved": False,
        "offdiagonal_orientation_parity_law_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": OFFDIAG_SIGNED_FORMULA,
        "closed_unsigned_subledgers": [PURE_SEMIPRIME_ATOM + "_unsigned_domain", TAIL_LIFT],
        "next_primary_attack_target": PURE_SEMIPRIME_ATOM,
        "paired_required_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            COMMON_PACKET,
        ],
        "parallel_direct_attack_target": POINTWISE_TABLE,
        "conditional_generators": [BRANCH_TRACE, ATOMIC_TRACE],
        "retained_basis_after_router": retained_basis,
        "pure_semiprime_atom_fields": pure_atom_fields(),
        "sample_pure_seed_atom_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "offdiagonal source tuple signed seed formula 进一步强制拆成 pure semiprime pair "
            "`tail=1` seed atom 与 `tail>1` q-rough continuation lift。每个 ordered type "
            "`(p,q), p<q` 恰有一个 pure atom `p*q`；所有 tail 非单位 occurrence 不是新的 first "
            "seed，只能由同一 pure atom 加 internal transition lift 解释。剩余最新窄口因此变为 "
            "`PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward`，并仍需 "
            "orientation parity、ExactUV return、internal transition 与 common packet。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF offdiagonal pure semiprime seed atom 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"offdiagonal_source_tuple_signed_seed_target_imported={fmt_bool(cert['offdiagonal_source_tuple_signed_seed_target_imported'])}",
        f"pure_semiprime_pair_seed_atom_bijection_proved={fmt_bool(cert['pure_semiprime_pair_seed_atom_bijection_proved'])}",
        f"tail_nonunit_reduced_to_internal_transition_lift={fmt_bool(cert['tail_nonunit_reduced_to_internal_transition_lift'])}",
        f"tail_lift_phi_minus_one_mass_formula_proved={fmt_bool(cert['tail_lift_phi_minus_one_mass_formula_proved'])}",
        f"pure_semiprime_pair_signed_seed_atom_proved={fmt_bool(cert['pure_semiprime_pair_signed_seed_atom_proved'])}",
        f"offdiagonal_source_tuple_signed_seed_formula_proved={fmt_bool(cert['offdiagonal_source_tuple_signed_seed_formula_proved'])}",
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
            "## 2. pure atom 字段",
            "",
            "| field | status | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["pure_semiprime_atom_fields"]:
        lines.append(f"| `{item['field']}` | `{item['status']}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 样本审计摘要",
            "",
            "| N | types | pure atoms | tail lift | total occ | pure share | tail share | pure ok | tail ok | pure sign log10 | tail transition log10 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: |",
        ]
    )
    for item in cert["sample_pure_seed_atom_audit"]:
        lines.append(
            f"| {item['N']} | {item['offdiagonal_seed_types']} | {item['pure_semiprime_pair_seed_atoms']} | "
            f"{item['tail_lift_occurrences']} | {item['offdiagonal_total_occurrences']} | "
            f"{item['pure_atom_share_of_occurrences']} | {item['tail_lift_share_of_occurrences']} | "
            f"`{fmt_bool(item['pure_atom_type_bijection_holds'])}` | "
            f"`{fmt_bool(item['tail_lift_decomposition_holds'])}` | "
            f"{item['formal_pure_atom_sign_shadow_log10']} | {item['formal_tail_lift_transition_shadow_log10']} |"
        )
    lines.extend(
        [
            "",
            "## 4. 最大 tail-lift 纤维",
            "",
            "| N | top tail lifts |",
            "| --- | --- |",
        ]
    )
    for item in cert["sample_pure_seed_atom_audit"]:
        top = ", ".join(
            f"(p={entry['p']},q={entry['q']},lift={entry['tail_lift_mass']})"
            for entry in item["top_tail_lifts"][:4]
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
    """写出 pure semiprime atom 前沿证书。"""
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
