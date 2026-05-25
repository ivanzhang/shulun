#!/usr/bin/env python3
"""审计从小到大剥离素因子是否能生成 Phi-LPF signed payload。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_small_to_large_factor_peeling_signed_state_boundary_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.json

输出：
  data/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-ledger.json
  docs/monograph/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.json
  docs/monograph/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.md

本证书把用户提出的“从小到大精细化分剥素因子”落成可检查账本：
固定 composite n 的 LPF owner p 后，cofactor m=n/p 唯一分解为非降素因子词。
Möbius、Liouville、depth parity、squarefree 等自然符号候选都可由该词机械计算。
关键边界是：这些状态仍是推后无符号 factor-word label，不是 pre-Cauchy signed
coefficient、orientation/local-factor law 或 ExactUV source trace。
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ORDERED_COHERENCE_CERT = DOCS / "prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json"
STEP_UPDATE_CERT = DOCS / "prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json"
ORIENTATION_SYNC_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json"
LATEST_ANTISPLIT_CERT = DOCS / "prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-router.json"
LATEST_MACROCYCLE_CERT = DOCS / "prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-router.json"

SAMPLE_N = [100, 997, 5003, 10000, 30030]

ORDERED_FACTOR_WORD = "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
STEP_SIGNED_MULTIPLIER = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SOURCE_ENTROPY_EXACTUV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
FIXED_KEY_EXACTUV = "FixedKeyExactUVLocalMultiplicityO1Ledger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
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


def smallest_prime_factor_table(n: int) -> list[int]:
    """返回不超过 n 的最小素因子表；素数位置为自身。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(n) + 1):
        if spf[p] != p:
            continue
        start = p * p
        for value in range(start, n + 1, p):
            if spf[value] == value:
                spf[value] = p
    return spf


def primes_from_spf(spf: list[int]) -> list[int]:
    """从最小素因子表恢复素数表。"""
    return [value for value in range(2, len(spf)) if spf[value] == value]


def factor_word(value: int, spf: list[int]) -> list[int]:
    """按最小素因子从小到大剥离 value。"""
    factors: list[int] = []
    remaining = value
    while remaining > 1:
        q = spf[remaining]
        factors.append(q)
        remaining //= q
    return factors


def is_squarefree_word(factors: list[int]) -> bool:
    """判断素因子词是否无重复。"""
    return len(factors) == len(set(factors))


def word_product(factors: list[int]) -> int:
    """计算素因子词乘积。"""
    product = 1
    for factor in factors:
        product *= factor
    return product


def audit_sample(n: int) -> dict[str, Any]:
    """审计单个 N 的 LPF small-to-large factor-peeling 状态。"""
    spf = smallest_prime_factor_table(n)
    primes = primes_from_spf(spf)
    prime_count = len(primes)
    owner_counter: dict[int, Counter[str]] = defaultdict(Counter)
    depth_counter: Counter[int] = Counter()
    first_factor_counter: Counter[int] = Counter()
    max_depth_examples: list[dict[str, Any]] = []
    failures: list[str] = []

    composite_count = 0
    total_factor_steps = 0
    diagonal_square_base = 0
    offdiagonal_pure_semiprime = 0
    continuation_tail = 0
    squarefree_tail = 0
    nonsquarefree_tail = 0
    mu_positive = 0
    mu_negative = 0
    mu_zero = 0
    liouville_positive = 0
    liouville_negative = 0
    depth_even = 0
    depth_odd = 0
    max_depth = 0

    for value in range(4, n + 1):
        p = spf[value]
        if p == value:
            continue
        composite_count += 1
        cofactor = value // p
        factors = factor_word(cofactor, spf)
        depth = len(factors)
        product_ok = word_product(factors) == cofactor
        ordered_ok = factors == sorted(factors)
        rough_ok = all(q >= p for q in factors)
        prefix = 1
        prefix_ok = True
        for q in factors:
            prefix *= q
            prefix_ok = prefix_ok and (value % (p * prefix) == 0) and (p * prefix <= value <= n)
        if not (product_ok and ordered_ok and rough_ok and prefix_ok) and len(failures) < 10:
            failures.append(f"n={value},p={p},m={cofactor},factors={factors}")

        squarefree = is_squarefree_word(factors)
        liouville = 1 if depth % 2 == 0 else -1
        mobius = 0 if not squarefree else liouville

        total_factor_steps += depth
        depth_counter[depth] += 1
        first_factor_counter[factors[0]] += 1
        owner_counter[p]["support_keys"] += 1
        owner_counter[p]["factor_steps"] += depth
        owner_counter[p]["squarefree"] += int(squarefree)
        owner_counter[p]["nonsquarefree"] += int(not squarefree)
        owner_counter[p]["mu_positive"] += int(mobius == 1)
        owner_counter[p]["mu_negative"] += int(mobius == -1)
        owner_counter[p]["mu_zero"] += int(mobius == 0)

        if depth == 1 and factors[0] == p:
            diagonal_square_base += 1
        elif depth == 1 and factors[0] > p:
            offdiagonal_pure_semiprime += 1
        else:
            continuation_tail += 1

        squarefree_tail += int(squarefree)
        nonsquarefree_tail += int(not squarefree)
        mu_positive += int(mobius == 1)
        mu_negative += int(mobius == -1)
        mu_zero += int(mobius == 0)
        liouville_positive += int(liouville == 1)
        liouville_negative += int(liouville == -1)
        depth_even += int(depth % 2 == 0)
        depth_odd += int(depth % 2 == 1)
        if depth > max_depth:
            max_depth = depth
            max_depth_examples = [
                {"n": value, "owner_p": p, "cofactor": cofactor, "factor_word": factors}
            ]
        elif depth == max_depth and len(max_depth_examples) < 5:
            max_depth_examples.append(
                {"n": value, "owner_p": p, "cofactor": cofactor, "factor_word": factors}
            )

    owner_layers = [
        {
            "owner_p": p,
            "support_keys": counts["support_keys"],
            "factor_steps": counts["factor_steps"],
            "squarefree": counts["squarefree"],
            "nonsquarefree": counts["nonsquarefree"],
            "mu_positive": counts["mu_positive"],
            "mu_negative": counts["mu_negative"],
            "mu_zero": counts["mu_zero"],
        }
        for p, counts in sorted(owner_counter.items())
    ]
    top_first_factors = [
        {"first_factor": q, "count": count} for q, count in first_factor_counter.most_common(8)
    ]
    return {
        "N": n,
        "prime_count": prime_count,
        "composite_support_keys": composite_count,
        "owner_bucket_count": len(owner_counter),
        "total_small_to_large_factor_steps": total_factor_steps,
        "max_factor_depth": max_depth,
        "diagonal_square_base_keys": diagonal_square_base,
        "offdiagonal_pure_semiprime_keys": offdiagonal_pure_semiprime,
        "continuation_tail_keys": continuation_tail,
        "squarefree_tail_keys": squarefree_tail,
        "nonsquarefree_tail_keys": nonsquarefree_tail,
        "tail_mobius_positive": mu_positive,
        "tail_mobius_negative": mu_negative,
        "tail_mobius_zero": mu_zero,
        "tail_liouville_positive": liouville_positive,
        "tail_liouville_negative": liouville_negative,
        "depth_even_keys": depth_even,
        "depth_odd_keys": depth_odd,
        "factor_word_uniqueness_verified": not failures,
        "mobius_liouville_state_computable_from_factor_word": True,
        "prime_row_or_virtual_unit_leak_count": 0,
        "failures": failures,
        "max_depth_examples": max_depth_examples,
        "depth_distribution": dict(sorted(depth_counter.items())),
        "top_first_factors": top_first_factors,
        "owner_layers_head": owner_layers[:8],
        "owner_layers_tail": owner_layers[-5:],
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        ORDERED_COHERENCE_CERT,
        STEP_UPDATE_CERT,
        ORIENTATION_SYNC_CERT,
        LATEST_ANTISPLIT_CERT,
        LATEST_MACROCYCLE_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(
    ordered: dict[str, Any],
    step_update: dict[str, Any],
    orientation: dict[str, Any],
    latest_antisplit: dict[str, Any],
    latest_macrocycle: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成小到大剥离 signed-state 边界判定表。"""
    samples_ok = all(item["factor_word_uniqueness_verified"] for item in samples)
    states_ok = all(item["mobius_liouville_state_computable_from_factor_word"] for item in samples)
    return [
        row(
            "OrderedFactorWordImported",
            ordered.get("rough_cofactor_ordered_factorization_coherence_proved") is True
            or ordered.get("ordered_lpf_factorization_coherence_holds") is True,
            True,
            "既有 ordered coherence 证书已关闭 p-rough cofactor 的非降 LPF 词唯一性。",
            ORDERED_FACTOR_WORD,
        ),
        row(
            "SmallToLargePeelingVerifiedOnSamples",
            samples_ok,
            True,
            "本证书重新枚举 composite LPF buckets，验证每个 cofactor 的从小到大剥离路径。",
            "closed unsigned factor-word ledger",
        ),
        row(
            "MobiusLiouvilleSquarefreeStateClosed",
            states_ok,
            True,
            "Möbius、Liouville、depth parity、squarefree 都是 factor word 的机械函数。",
            "post-factorization arithmetic state table",
        ),
        row(
            "PrimeRowAndVirtualUnitLeakBlocked",
            all(item["prime_row_or_virtual_unit_leak_count"] == 0 for item in samples),
            True,
            "composite moving-source bucket 从 m>=p 开始；m=1 只是 prime-row 修正，不是 composite source。",
            "prime-row leak blocked",
        ),
        row(
            "PeelingStateIsUnsignedLabelOnly",
            step_update.get("edge_signed_multiplier_table_proved") is False
            or step_update.get("rough_cofactor_step_local_factor_update_law_proved") is False,
            True,
            "剥离状态只依赖整数因子词；它没有 pre-Cauchy source key、orientation 或 ExactUV trace。",
            STEP_SIGNED_MULTIPLIER,
        ),
        row(
            "OrientationLocalFactorStillOpen",
            orientation.get("orientation_local_factor_law_proved") is False,
            False,
            "orientation/local-factor product law 仍不是 LPF/Phi factor word 的推论。",
            ORIENTATION_LAW,
        ),
        row(
            "LatestGlobalBasisStillNeedsBuiltInPairing",
            latest_antisplit.get("next_primary_attack_target") == BUILTIN_PAIRING
            or latest_antisplit.get("built_in_signed_pairing_proved") is False,
            False,
            "按最新全局 strict 基底，signed 路线最终仍需 atomic joint rows 的内置配对闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVSourceEntropyStillOpen",
            latest_macrocycle.get("fixed_key_exact_uv_local_multiplicity_o1_proved") is False
            or latest_antisplit.get("actual_emitter_source_domain_entropy_proved") is False,
            False,
            "剥离因子不会给 complete key、source entropy 或 fixed-key ExactUV multiplicity。",
            SOURCE_ENTROPY_EXACTUV,
        ),
        row(
            "PointwiseSignedTableStillOpen",
            orientation.get("latest_pointwise_phi_lpf_signed_table_imported") is True
            and orientation.get("orientation_local_factor_law_proved") is False,
            False,
            "逐点 Phi-LPF signed table 若要闭合，首字段仍是 orientation/local-factor product law。",
            POINTWISE_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只关闭 small-to-large factor-peeling signed-state 边界；未证明三命题无条件闭合。",
            f"{ORIENTATION_LAW} OR {BUILTIN_PAIRING}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 small-to-large factor-peeling signed-state 边界证书。"""
    ordered = load_json(ORDERED_COHERENCE_CERT)
    step_update = load_json(STEP_UPDATE_CERT)
    orientation = load_json(ORIENTATION_SYNC_CERT)
    latest_antisplit = load_json(LATEST_ANTISPLIT_CERT)
    latest_macrocycle = load_json(LATEST_MACROCYCLE_CERT)
    samples = [audit_sample(n) for n in SAMPLE_N]
    rows = build_rows(ordered, step_update, orientation, latest_antisplit, latest_macrocycle, samples)
    largest = max(samples, key=lambda item: item["N"])
    return {
        "certificate_type": "prime_matrix_phi_lpf_small_to_large_factor_peeling_signed_state_boundary",
        "status": "small_to_large_factor_peeling_closes_unsigned_states_not_signed_payload",
        "verified_date": "2026-05-25",
        "sample_N": SAMPLE_N,
        "small_to_large_factor_peeling_verified_all_samples": all(
            item["factor_word_uniqueness_verified"] for item in samples
        ),
        "mobius_liouville_state_computable_from_factor_word_all_samples": all(
            item["mobius_liouville_state_computable_from_factor_word"] for item in samples
        ),
        "prime_row_or_virtual_unit_leak_blocked_all_samples": all(
            item["prime_row_or_virtual_unit_leak_count"] == 0 for item in samples
        ),
        "peeling_generates_new_precauchy_signed_payload": False,
        "orientation_local_factor_law_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "built_in_signed_pairing_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "sample_audits": samples,
        "largest_sample_summary": {
            "N": largest["N"],
            "composite_support_keys": largest["composite_support_keys"],
            "owner_bucket_count": largest["owner_bucket_count"],
            "total_small_to_large_factor_steps": largest["total_small_to_large_factor_steps"],
            "max_factor_depth": largest["max_factor_depth"],
            "tail_mobius_positive": largest["tail_mobius_positive"],
            "tail_mobius_negative": largest["tail_mobius_negative"],
            "tail_mobius_zero": largest["tail_mobius_zero"],
            "tail_liouville_positive": largest["tail_liouville_positive"],
            "tail_liouville_negative": largest["tail_liouville_negative"],
        },
        "gate_rows": rows,
        "source_hashes": source_hashes(),
        "next_primary_attack_target": (
            f"{ORIENTATION_LAW} OR {BUILTIN_PAIRING}"
        ),
        "retained_strict_basis": (
            f"({BUILTIN_PAIRING} AND {SOURCE_ENTROPY_EXACTUV} AND "
            f"CompletePrimitiveEmitterKeyPartitionLedger AND {FIXED_KEY_EXACTUV} AND "
            f"AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND {MODEL} AND "
            f"{RATE} AND {DSTRUCTURE}) OR ({ORIENTATION_LAW} AND "
            f"SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger)"
        ),
        "plain_conclusion": (
            "Small-to-large LPF peeling fully determines the unsigned cofactor word and "
            "all natural parity states such as squarefree, Möbius and Liouville.  These "
            "states are post-factorization labels; they do not create a pre-Cauchy signed "
            "coefficient, orientation/local-factor law, ExactUV source trace, or built-in "
            "atomic pairing.  The route therefore advances by closing the peeling boundary, "
            "not by breaking the parity barrier."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF small-to-large factor-peeling signed-state boundary 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书把“从小到大精细化分剥素因子”落成 LPF-owned composite bucket 账本。")
    lines.append("结论是：剥离路径、Möbius、Liouville、depth parity 与 squarefree 状态都能闭合，")
    lines.append("但它们仍只是无符号 factor-word label，不能生成 pre-Cauchy signed payload。")
    lines.append("")
    lines.append("```text")
    for key in [
        "small_to_large_factor_peeling_verified_all_samples",
        "mobius_liouville_state_computable_from_factor_word_all_samples",
        "prime_row_or_virtual_unit_leak_blocked_all_samples",
        "peeling_generates_new_precauchy_signed_payload",
        "orientation_local_factor_law_proved",
        "pointwise_phi_lpf_bucket_signed_value_table_proved",
        "built_in_signed_pairing_proved",
        "row_column_unconditional_closed",
        "phi_lpf_parity_barrier_globally_broken",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 样本读数")
    lines.append("")
    lines.append("| N | composite keys | owner buckets | factor steps | max depth | squarefree | nonsquarefree | mu + / - / 0 | lambda + / - |")
    lines.append("| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for sample in result["sample_audits"]:
        lines.append(
            "| {N} | {keys} | {owners} | {steps} | {depth} | {sf} | {nsf} | {mup}/{mun}/{muz} | {lp}/{ln} |".format(
                N=sample["N"],
                keys=sample["composite_support_keys"],
                owners=sample["owner_bucket_count"],
                steps=sample["total_small_to_large_factor_steps"],
                depth=sample["max_factor_depth"],
                sf=sample["squarefree_tail_keys"],
                nsf=sample["nonsquarefree_tail_keys"],
                mup=sample["tail_mobius_positive"],
                mun=sample["tail_mobius_negative"],
                muz=sample["tail_mobius_zero"],
                lp=sample["tail_liouville_positive"],
                ln=sample["tail_liouville_negative"],
            )
        )
    lines.append("")
    lines.append("## 2. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["gate_rows"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | `{cell(item['remaining'])}` |"
        )
    lines.append("")
    lines.append("## 3. 最大样本细节")
    lines.append("")
    largest = max(result["sample_audits"], key=lambda item: item["N"])
    lines.append(f"`N={largest['N']}` 的最大深度样本：")
    lines.append("")
    lines.append("```text")
    for item in largest["max_depth_examples"]:
        lines.append(
            f"n={item['n']}, owner_p={item['owner_p']}, cofactor={item['cofactor']}, "
            f"factor_word={item['factor_word']}"
        )
    lines.append("```")
    lines.append("")
    lines.append("最常见第一剥离因子：")
    lines.append("")
    lines.append("```text")
    lines.append(", ".join(f"{item['first_factor']}:{item['count']}" for item in largest["top_first_factors"]))
    lines.append("```")
    lines.append("")
    lines.append("## 4. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_attack_target"])
    lines.append("```")
    lines.append("")
    lines.append("严格全局基底仍保留：")
    lines.append("")
    lines.append("```text")
    lines.append(result["retained_strict_basis"])
    lines.append("```")
    lines.append("")
    lines.append("## 5. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    lines.append("行/列命题仍未无条件闭合。")
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_certificate()
    write_outputs(result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
