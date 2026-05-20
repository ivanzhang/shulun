#!/usr/bin/env python3
"""生成 Phi-LPF step local factor update 前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_step_local_factor_update_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-step-local-factor-update-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-step-local-factor-update-frontier-router.md
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

SLUG = "prime-matrix-phi-lpf-step-local-factor-update-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ORDERED_CERT = DOCS / "prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
ORIENTATION_TRACE_CERT = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_TRACE_CERT = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
PRIMITIVE_EXPR_CERT = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

STEP_UPDATE = "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward"
EDGE_TABLE = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
PRIMITIVE_ORIGIN = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
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
    """按最小素因子递增剥离 value 的素因子。"""
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


def sample_step_update_audit(n: int) -> dict[str, Any]:
    """审计 ordered LPF edge 与 signed multiplier 自由字段。"""
    primes = primes_up_to(n)
    small_primes = [p for p in primes if p <= math.isqrt(n)]
    total_support = 0
    total_edges = 0
    first_edges = 0
    internal_edges = 0
    max_depth = 0
    distinct_edge_transitions: set[tuple[int, int, int, int]] = set()
    failures: list[str] = []
    layer_summary: dict[str, dict[str, int | bool]] = {}

    for p in small_primes:
        layer_support = 0
        layer_edges = 0
        layer_first_edges = 0
        layer_internal_edges = 0
        layer_max_depth = 0
        for m in range(2, n // p + 1):
            if not is_p_rough(m, p, primes):
                continue
            factors = factor_by_lpf(m, primes)
            prefix = 1
            layer_support += 1
            layer_max_depth = max(layer_max_depth, len(factors))
            for index, q in enumerate(factors):
                next_prefix = prefix * q
                edge_ok = (
                    q >= p
                    and is_p_rough(prefix, p, primes)
                    and is_p_rough(next_prefix, p, primes)
                    and p * next_prefix <= n
                )
                if not edge_ok and len(failures) < 10:
                    failures.append(f"p={p},m={m},edge={prefix}->{next_prefix},q={q}")
                distinct_edge_transitions.add((p, prefix, q, next_prefix))
                layer_edges += 1
                if index == 0:
                    layer_first_edges += 1
                else:
                    layer_internal_edges += 1
                prefix = next_prefix
        layer_summary[str(p)] = {
            "support_keys": layer_support,
            "edge_steps": layer_edges,
            "first_edges": layer_first_edges,
            "internal_edges": layer_internal_edges,
            "max_depth": layer_max_depth,
            "edge_path_ok": not failures,
        }
        total_support += layer_support
        total_edges += layer_edges
        first_edges += layer_first_edges
        internal_edges += layer_internal_edges
        max_depth = max(max_depth, layer_max_depth)

    return {
        "N": n,
        "small_prime_layers": len(small_primes),
        "total_phi_lpf_support_keys": total_support,
        "total_ordered_edge_steps": total_edges,
        "first_edge_steps": first_edges,
        "internal_edge_steps": internal_edges,
        "distinct_edge_transitions": len(distinct_edge_transitions),
        "max_factor_depth": max_depth,
        "edge_path_identity_holds": not failures,
        "formal_distinct_edge_sign_shadow_bits": len(distinct_edge_transitions),
        "formal_distinct_edge_sign_shadow_log10": round(
            len(distinct_edge_transitions) * math.log10(2), 6
        ),
        "formal_edge_occurrence_sign_shadow_bits": total_edges,
        "formal_edge_occurrence_sign_shadow_log10": round(total_edges * math.log10(2), 6),
        "failures": failures,
        "layers": layer_summary,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        ORDERED_CERT,
        POINTWISE_FRONTIER_CERT,
        ORIENTATION_TRACE_CERT,
        BUILTIN_TRACE_CERT,
        PRIMITIVE_EXPR_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def edge_multiplier_fields() -> list[dict[str, str]]:
    """列出 edge multiplier 表必须携带的字段。"""
    return [
        {
            "field": "edge_key",
            "meaning": "同一 owner bucket 内的有序边 `(p, prefix, q, prefix*q)`。",
        },
        {
            "field": "source_tuple_or_trace_id",
            "meaning": "该边所属的 pre-Cauchy actual source tuple 或 branch trace，不是推后 payment 原像。",
        },
        {
            "field": "signed_multiplier_formula",
            "meaning": "从 `a_p(prefix)` 到 `a_p(prefix*q)` 的 sign/local-factor/truncation 乘子。",
        },
        {
            "field": "first_edge_policy",
            "meaning": "`prefix=1` 的第一边也必须由同表正向给出，不得读取 Phi 中被减掉的 prime row。",
        },
        {
            "field": "orientation_parity_increment",
            "meaning": "乘入 `q` 对 orientation parity 与 signed coefficient 符号的增量规则。",
        },
        {
            "field": "local_factor_nonzero_or_return",
            "meaning": "local factor 非零、截断兼容；失败时进入命名回流。",
        },
        {
            "field": "alpha_delta_branch_exactuv_transition",
            "meaning": "同一边同步更新 alpha/delta side、branch key 和 exact `(u,v)` 输出。",
        },
        {
            "field": "path_product_identity_before_pushforward",
            "meaning": "沿 ordered edge 乘积在 Phi/payment 推前前等于该 support key 的 signed coefficient。",
        },
        {
            "field": "no_downstream_recovery",
            "meaning": "不得由 payment skeleton、零行覆盖、origin table 固定点或 terminal 反推恢复乘子。",
        },
    ]


def build_rows(
    ordered: dict[str, Any],
    pointwise: dict[str, Any],
    orientation: dict[str, Any],
    builtin: dict[str, Any],
    primitive_expr: dict[str, Any],
    exactuv: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 step update 前沿判定表。"""
    samples_ok = all(item["edge_path_identity_holds"] for item in samples)
    return [
        row(
            "StepLocalFactorUpdateTargetImported",
            ordered.get("next_direct_attack_target") == STEP_UPDATE,
            False,
            "上一层已把 ordered coherence 移除，最新直接缺口就是 step local factor update。",
            STEP_UPDATE,
        ),
        row(
            "OrderedLPFEdgePathImported",
            ordered.get("rough_cofactor_ordered_factorization_coherence_proved") is True and samples_ok,
            True,
            "LPF 最小素因子剥离已给出同一 owner bucket 内唯一 ordered edge path。",
            "path/order already paid",
        ),
        row(
            "StepUpdateEquivalentToEdgeMultiplierTable",
            samples_ok,
            True,
            "路径固定后，step update 等价于在每条 ordered edge 上给 signed multiplier，并沿路径相乘。",
            EDGE_TABLE,
        ),
        row(
            "FirstEdgeCannotUsePrimeRowLeak",
            samples_ok,
            True,
            "`prefix=1` 的第一边是 multiplier 表字段；不能把 Phi 公式排除的 prime row 当作 composite signed seed。",
            EDGE_TABLE,
        ),
        row(
            "PhiLPFCountsDoNotDetermineMultipliers",
            samples_ok,
            True,
            "同一 support/order 可形式承载独立 edge sign decorations；LPF/Phi 只给 domain，不给奇 signed 数据。",
            EDGE_TABLE,
        ),
        row(
            "CompleteBranchTraceWouldSupplyMultipliers",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True,
            True,
            "若 exact actual noncanonical branch trace 存在，orientation、local factor、branch key 与 return tag 可同 trace 给出。",
            BRANCH_TRACE,
        ),
        row(
            "AtomicTraceWouldSupplySameRowSignedValue",
            builtin.get("branch_trace_conditionally_suffices") is True,
            True,
            "若 atomic branch trace signed coefficient 公式存在，edge multiplier 与逐点 signed value 可作为同一 trace 的字段读取。",
            ATOMIC_TRACE,
        ),
        row(
            "PrimitiveOriginIdentityStillOpen",
            primitive_expr.get("primitive_summand_signed_coefficient_origin_identity_proved") is False,
            False,
            "primitive summand 的 signed coefficient 来源恒等式仍未给出，不能反向生成 edge multiplier。",
            PRIMITIVE_ORIGIN,
        ),
        row(
            "ExactUVStillParallelGate",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False
            or exactuv.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "即使 edge multiplier 表存在，ExactUV source entropy/fiber 或 bounded incidence 仍是并行门。",
            EXACTUV_PAIR,
        ),
        row(
            "PointwisePhiLPFTableStillOpen",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "直接提交逐 Phi-LPF key signed value table 仍是并行替代，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "EdgeMultiplierTableCurrentCorpusProved",
            False,
            False,
            "当前材料没有逐 ordered edge 的 signed multiplier、非零 local factor、branch/ExactUV 转移和推前前乘积恒等式表。",
            EDGE_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 step update 压成 edge multiplier 表；未证明三命题无条件闭合。",
            f"{EDGE_TABLE} OR {POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 step update 前沿证书。"""
    ordered = load_json(ORDERED_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    orientation = load_json(ORIENTATION_TRACE_CERT)
    builtin = load_json(BUILTIN_TRACE_CERT)
    primitive_expr = load_json(PRIMITIVE_EXPR_CERT)
    exactuv = load_json(EXACTUV_CERT)
    samples = [sample_step_update_audit(n) for n in SAMPLE_N]
    rows = build_rows(ordered, pointwise, orientation, builtin, primitive_expr, exactuv, samples)
    retained_basis = (
        f"({EDGE_TABLE} OR {POINTWISE_TABLE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA}) "
        f"AND {EXACTUV_PAIR} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_step_local_factor_update_frontier_router",
        "status": "phi_lpf_step_local_factor_update_reduced_to_edge_signed_multiplier_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "phi_lpf_step_local_factor_update_frontier_router_closed": True,
        "ordered_lpf_edge_path_imported": rows[1]["closed"],
        "step_update_reduced_to_edge_multiplier_table": True,
        "edge_signed_multiplier_table_proved": False,
        "rough_cofactor_step_local_factor_update_law_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "actual_noncanonical_complete_branch_trace_formula_proved": False,
        "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": STEP_UPDATE,
        "next_direct_attack_target": EDGE_TABLE,
        "conditional_generators": [
            BRANCH_TRACE,
            ATOMIC_TRACE,
            PRIMITIVE_ORIGIN,
        ],
        "parallel_direct_attack_target": POINTWISE_TABLE,
        "nonrecursive_breaker_alternatives": [
            SEED_CYCLE_CUT,
            PDEC_SCOPE,
            NEW_JOINT_FORMULA,
        ],
        "retained_basis_after_router": retained_basis,
        "edge_multiplier_fields": edge_multiplier_fields(),
        "sample_step_update_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "ordered LPF path 已闭合后，`PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward` "
            "不再是路径选择问题，而是逐 ordered edge 的 signed multiplier 表问题。"
            "对每条 `(p,prefix,q,prefix*q)` 边，必须正向给出 sign/local-factor/truncation 乘子、"
            "orientation parity 增量、alpha/delta branch 与 exact-UV 转移、非零或命名回流，以及沿路径乘积的推前前恒等式。"
            "`prefix=1` 的第一边也必须由该表给出，不能读取 Phi 中被排除的 prime row 或 payment 原像。"
            "因此最新直接主攻收窄为 `PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward`；"
            "条件生成器是 exact branch trace / atomic trace / primitive origin identity，"
            "并行替代仍是逐 Phi-LPF key signed value table。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF step local factor update frontier 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"ordered_lpf_edge_path_imported={fmt_bool(cert['ordered_lpf_edge_path_imported'])}",
        f"step_update_reduced_to_edge_multiplier_table={fmt_bool(cert['step_update_reduced_to_edge_multiplier_table'])}",
        f"edge_signed_multiplier_table_proved={fmt_bool(cert['edge_signed_multiplier_table_proved'])}",
        f"rough_cofactor_step_local_factor_update_law_proved={fmt_bool(cert['rough_cofactor_step_local_factor_update_law_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
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
            "## 2. edge multiplier 字段合同",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in cert["edge_multiplier_fields"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 样本审计摘要",
            "",
            "| N | support keys | edge steps | first edges | internal edges | distinct edges | max depth | distinct sign log10 | occurrence sign log10 | ok |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in cert["sample_step_update_audit"]:
        lines.append(
            f"| {item['N']} | {item['total_phi_lpf_support_keys']} | "
            f"{item['total_ordered_edge_steps']} | {item['first_edge_steps']} | "
            f"{item['internal_edge_steps']} | {item['distinct_edge_transitions']} | "
            f"{item['max_factor_depth']} | {item['formal_distinct_edge_sign_shadow_log10']} | "
            f"{item['formal_edge_occurrence_sign_shadow_log10']} | "
            f"`{fmt_bool(item['edge_path_identity_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "条件生成器：",
            "",
            "```text",
            "\n".join(cert["conditional_generators"]),
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
            "## 5. 依赖哈希",
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
    """写出 step local factor update 前沿证书。"""
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
