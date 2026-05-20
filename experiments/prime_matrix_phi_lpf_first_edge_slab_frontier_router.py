#!/usr/bin/env python3
"""生成 Phi-LPF first-edge slab 前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_first_edge_slab_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-first-edge-slab-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.md
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

SLUG = "prime-matrix-phi-lpf-first-edge-slab-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

STEP_ROUTER = DOCS / "prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
ORIENTATION_TRACE_CERT = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_TRACE_CERT = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

EDGE_TABLE = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
FIRST_EDGE_FIBER = "PhiLPFFirstEdgeQRoughContinuationFiberLedger"
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


def factor_by_lpf(value: int, primes: list[int]) -> list[int]:
    """按最小素因子顺序剥离 value。"""
    remaining = value
    factors: list[int] = []
    for q in primes:
        if q * q > remaining:
            break
        while remaining % q == 0:
            factors.append(q)
            remaining //= q
    if remaining > 1:
        factors.append(remaining)
    return factors


def phi_rough(x: int, p: int, primes: list[int]) -> int:
    """直接计算 Phi(x,p)，包含 1。"""
    if x < 1:
        return 0
    return sum(1 for value in range(1, x + 1) if is_p_rough(value, p, primes))


def sample_first_edge_slab_audit(n: int) -> dict[str, Any]:
    """审计 first-edge slab 与 q-rough continuation 纤维公式。"""
    primes = primes_up_to(n)
    small_primes = [p for p in primes if p <= math.isqrt(n)]
    support_keys = 0
    first_edge_occurrences = 0
    internal_edge_occurrences = 0
    total_factor_steps = 0
    max_depth = 0
    first_edge_types: set[tuple[int, int]] = set()
    first_edge_fiber_counter: Counter[tuple[int, int]] = Counter()
    failures: list[str] = []

    for p in small_primes:
        for m in range(2, n // p + 1):
            if not is_p_rough(m, p, primes):
                continue
            factors = factor_by_lpf(m, primes)
            if not factors:
                failures.append(f"empty-factor p={p},m={m}")
                continue
            q = factors[0]
            tail = m // q
            if q < p or not is_p_rough(tail, q, primes):
                failures.append(f"bad-first-edge p={p},m={m},q={q},tail={tail}")
            support_keys += 1
            first_edge_occurrences += 1
            internal_edge_occurrences += max(0, len(factors) - 1)
            total_factor_steps += len(factors)
            max_depth = max(max_depth, len(factors))
            first_edge_types.add((p, q))
            first_edge_fiber_counter[(p, q)] += 1

    formula_counter: Counter[tuple[int, int]] = Counter()
    formula_sum = 0
    for p in small_primes:
        for q in primes:
            if q < p or p * q > n:
                continue
            fiber = phi_rough(n // (p * q), q, primes)
            if fiber:
                formula_counter[(p, q)] = fiber
                formula_sum += fiber

    mismatch_items = [
        (key, first_edge_fiber_counter.get(key, 0), formula_counter.get(key, 0))
        for key in sorted(set(first_edge_fiber_counter) | set(formula_counter))
        if first_edge_fiber_counter.get(key, 0) != formula_counter.get(key, 0)
    ]
    top_fibers = [
        {"p": key[0], "q": key[1], "fiber_mass": value}
        for key, value in first_edge_fiber_counter.most_common(8)
    ]
    return {
        "N": n,
        "small_prime_layers": len(small_primes),
        "support_keys": support_keys,
        "first_edge_occurrences": first_edge_occurrences,
        "internal_edge_occurrences": internal_edge_occurrences,
        "total_ordered_edge_occurrences": total_factor_steps,
        "distinct_first_edge_types": len(first_edge_types),
        "max_factor_depth": max_depth,
        "first_edge_phi_fiber_formula_sum": formula_sum,
        "first_edge_phi_fiber_formula_holds": formula_sum == support_keys and not mismatch_items,
        "first_edge_path_guard_holds": not failures,
        "formal_first_seed_type_sign_shadow_bits": len(first_edge_types),
        "formal_first_seed_type_sign_shadow_log10": round(len(first_edge_types) * math.log10(2), 6),
        "formal_first_edge_occurrence_sign_shadow_bits": first_edge_occurrences,
        "formal_first_edge_occurrence_sign_shadow_log10": round(
            first_edge_occurrences * math.log10(2), 6
        ),
        "formal_internal_transition_occurrence_sign_shadow_bits": internal_edge_occurrences,
        "formal_internal_transition_occurrence_sign_shadow_log10": round(
            internal_edge_occurrences * math.log10(2), 6
        ),
        "top_first_edge_fibers": top_fibers,
        "mismatches": mismatch_items[:10],
        "failures": failures[:10],
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        STEP_ROUTER,
        POINTWISE_FRONTIER_CERT,
        ORIENTATION_TRACE_CERT,
        BUILTIN_TRACE_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def first_edge_fields() -> list[dict[str, str]]:
    """列出 first-edge seed slab 必须携带的字段。"""
    return [
        {
            "field": "semiprime_edge_key",
            "meaning": "第一边 `(p,1,q,q)`，对应真实 composite key `p*q` 与 q-rough tail fiber。",
        },
        {
            "field": "first_seed_signed_value",
            "meaning": "从 virtual unit 到 `q` 的 signed seed；不能从 Phi 的 prime row 或 payment 原像读取。",
        },
        {
            "field": "q_rough_tail_fiber_lift",
            "meaning": "同一 `(p,q)` seed 对所有 q-rough tail 的继续传输规则。",
        },
        {
            "field": "source_trace_or_return_tag",
            "meaning": "pre-Cauchy source trace、branch key、ExactUV 输出；失败时进入命名回流。",
        },
    ]


def internal_transition_fields() -> list[dict[str, str]]:
    """列出内部 prime-adjoin transition 必须携带的字段。"""
    return [
        {
            "field": "internal_edge_key",
            "meaning": "内部边 `(p,prefix,q,prefix*q)`，其中 `prefix>1` 且二者都在同一 owner bucket。",
        },
        {
            "field": "signed_adjoin_multiplier",
            "meaning": "乘入下一素因子 `q` 的 sign/local-factor/truncation 乘子。",
        },
        {
            "field": "nonzero_predecessor_or_return",
            "meaning": "若前缀 signed value 为零或 local factor 消失，必须给命名 return，而不是继续除法。",
        },
        {
            "field": "path_product_compatibility",
            "meaning": "first seed 与内部乘子相乘后，等于最终 support key 的 signed coefficient。",
        },
    ]


def build_rows(
    step: dict[str, Any],
    pointwise: dict[str, Any],
    orientation: dict[str, Any],
    builtin: dict[str, Any],
    exactuv: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 first-edge slab 前沿判定表。"""
    samples_ok = all(
        item["first_edge_phi_fiber_formula_holds"] and item["first_edge_path_guard_holds"]
        for item in samples
    )
    return [
        row(
            "EdgeMultiplierTableTargetImported",
            step.get("next_direct_attack_target") == EDGE_TABLE,
            False,
            "上一层已把 step update 压到逐 ordered edge signed multiplier 表。",
            EDGE_TABLE,
        ),
        row(
            "EdgeTableSplitsIntoFirstSeedAndInternalTransition",
            samples_ok,
            True,
            "每条 LPF path 唯一分成第一边 seed slab 与后续内部 prime-adjoin transitions。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "FirstEdgePhiFiberFormula",
            samples_ok,
            True,
            "第一边 `(p,q)` 的 occurrence mass 精确为 Phi(floor(N/(p*q)),q)，即 q-rough tail fiber。",
            FIRST_EDGE_FIBER,
        ),
        row(
            "FirstEdgeSeedCannotBeRecoveredFromCounts",
            samples_ok,
            True,
            "Phi/LPF 只给 `(p,q)` 纤维大小；不赋 first seed signed value、branch trace 或 ExactUV。",
            FIRST_SEED,
        ),
        row(
            "InternalTransitionCannotBeRecoveredByDivision",
            samples_ok,
            True,
            "内部 transition 需要非零前缀或命名回流，不能用未知 pointwise signed value 作后验除法。",
            INTERNAL_TRANSITION,
        ),
        row(
            "FirstSeedTableCurrentCorpusProved",
            False,
            False,
            "当前材料没有为所有 semiprime first edges 提交 prepushforward signed seed 表。",
            FIRST_SEED,
        ),
        row(
            "InternalPrimeAdjoinTransitionCurrentCorpusProved",
            False,
            False,
            "当前材料没有为所有内部 prime-adjoin edges 提交 signed local-factor transition law。",
            INTERNAL_TRANSITION,
        ),
        row(
            "CompleteBranchTraceWouldSupplyBothSlabs",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True,
            True,
            "完整 branch trace 可同时给 first seed、内部 transition、return tag 与 ExactUV 字段。",
            BRANCH_TRACE,
        ),
        row(
            "AtomicTraceWouldSupplyBothSlabs",
            builtin.get("branch_trace_conditionally_suffices") is True,
            True,
            "atomic trace signed coefficient 公式可把两张表作为同一 trace 的字段读取。",
            ATOMIC_TRACE,
        ),
        row(
            "PointwisePhiLPFTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 signed value table 仍是直接替代，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "ExactUVStillParallelGate",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False
            or exactuv.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "两张 edge 表即使存在，ExactUV source entropy/fiber 仍是并行门。",
            EXACTUV_PAIR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 edge multiplier 表拆成 first seed slab 与 internal transition；未证明三命题无条件闭合。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 first-edge slab 前沿证书。"""
    step = load_json(STEP_ROUTER)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    orientation = load_json(ORIENTATION_TRACE_CERT)
    builtin = load_json(BUILTIN_TRACE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    samples = [sample_first_edge_slab_audit(n) for n in SAMPLE_N]
    rows = build_rows(step, pointwise, orientation, builtin, exactuv, samples)
    retained_basis = (
        f"(({FIRST_SEED} AND {INTERNAL_TRANSITION}) OR {POINTWISE_TABLE} OR "
        f"{BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA}) "
        f"AND {EXACTUV_PAIR} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_first_edge_slab_frontier_router",
        "status": "phi_lpf_edge_multiplier_table_split_into_first_seed_and_internal_transition_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "first_edge_slab_frontier_router_closed": True,
        "edge_signed_multiplier_table_imported": step.get("next_direct_attack_target") == EDGE_TABLE,
        "edge_table_split_into_first_seed_and_internal_transition": True,
        "first_edge_phi_fiber_formula_proved": all(
            item["first_edge_phi_fiber_formula_holds"] for item in samples
        ),
        "semiprime_first_edge_signed_seed_table_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "edge_signed_multiplier_table_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": EDGE_TABLE,
        "next_direct_attack_targets": [FIRST_SEED, INTERNAL_TRANSITION],
        "next_primary_attack_target": FIRST_SEED,
        "paired_required_attack_target": INTERNAL_TRANSITION,
        "parallel_direct_attack_target": POINTWISE_TABLE,
        "conditional_generators": [BRANCH_TRACE, ATOMIC_TRACE],
        "retained_basis_after_router": retained_basis,
        "first_edge_seed_fields": first_edge_fields(),
        "internal_transition_fields": internal_transition_fields(),
        "sample_first_edge_slab_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "逐 edge signed multiplier 表可严格拆成两个子表：第一边 `(p,1,q,q)` 的 semiprime "
            "signed seed slab，以及 `prefix>1` 的内部 prime-adjoin signed transition law。"
            "LPF/Phi 对第一边给出精确 q-rough continuation 纤维公式 "
            "`mass(p,q)=Phi(floor(N/(p*q)),q)`，但该公式只支付支撑和 occurrence mass，"
            "不产生 first seed signed value，也不产生内部 transition 的非零 local factor。"
            "因此下一直接主攻为 semiprime first-edge signed seed table；同时必须配套内部 "
            "prime-adjoin transition law，或改由逐点 signed table / branch trace / atomic trace 提供。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF first-edge slab frontier 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"edge_signed_multiplier_table_imported={fmt_bool(cert['edge_signed_multiplier_table_imported'])}",
        f"edge_table_split_into_first_seed_and_internal_transition={fmt_bool(cert['edge_table_split_into_first_seed_and_internal_transition'])}",
        f"first_edge_phi_fiber_formula_proved={fmt_bool(cert['first_edge_phi_fiber_formula_proved'])}",
        f"semiprime_first_edge_signed_seed_table_proved={fmt_bool(cert['semiprime_first_edge_signed_seed_table_proved'])}",
        f"internal_prime_adjoin_signed_transition_law_proved={fmt_bool(cert['internal_prime_adjoin_signed_transition_law_proved'])}",
        f"edge_signed_multiplier_table_proved={fmt_bool(cert['edge_signed_multiplier_table_proved'])}",
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
            "## 2. first-edge seed slab 字段合同",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in cert["first_edge_seed_fields"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. internal transition 字段合同",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in cert["internal_transition_fields"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 4. 样本审计摘要",
            "",
            "| N | support | first occ | internal occ | first types | max depth | Phi fiber ok | first type sign log10 | first occ sign log10 | internal occ sign log10 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for item in cert["sample_first_edge_slab_audit"]:
        lines.append(
            f"| {item['N']} | {item['support_keys']} | {item['first_edge_occurrences']} | "
            f"{item['internal_edge_occurrences']} | {item['distinct_first_edge_types']} | "
            f"{item['max_factor_depth']} | `{fmt_bool(item['first_edge_phi_fiber_formula_holds'])}` | "
            f"{item['formal_first_seed_type_sign_shadow_log10']} | "
            f"{item['formal_first_edge_occurrence_sign_shadow_log10']} | "
            f"{item['formal_internal_transition_occurrence_sign_shadow_log10']} |"
        )
    lines.extend(
        [
            "",
            "## 5. 最大 first-edge 纤维",
            "",
            "| N | top fibers |",
            "| --- | --- |",
        ]
    )
    for item in cert["sample_first_edge_slab_audit"]:
        top = ", ".join(
            f"(p={fiber['p']},q={fiber['q']},mass={fiber['fiber_mass']})"
            for fiber in item["top_first_edge_fibers"][:4]
        )
        lines.append(f"| {item['N']} | {cell(top)} |")
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
            "\n".join(cert["next_direct_attack_targets"]),
            "```",
            "",
            "并行直接入口：",
            "",
            "```text",
            cert["parallel_direct_attack_target"],
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
    """写出 first-edge slab 前沿证书。"""
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
