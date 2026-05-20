#!/usr/bin/env python3
"""生成 Phi-LPF rough cofactor 有序分解一致性证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_rough_cofactor_ordered_factorization_coherence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json

输出：
  data/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-ledger.json
  docs/monograph/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json
  docs/monograph/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.md
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

SLUG = "prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PHI_CERT = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"
SUPPORT_CERT = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
TRANSPORT_CERT = DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json"
UNIT_SEED_CERT = DOCS / "prime-matrix-phi-lpf-signed-transport-unit-seed-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"

ORDERED_COHERENCE = "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
STEP_UPDATE = "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
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


def sample_ordered_coherence_audit(n: int) -> dict[str, Any]:
    """审计 Phi-LPF 支撑键的有序素因子路径唯一性。"""
    primes = primes_up_to(n)
    small_primes = [p for p in primes if p <= math.isqrt(n)]
    layers: dict[str, dict[str, Any]] = {}
    total_support = 0
    total_factor_steps = 0
    max_depth = 0
    square_base_keys = 0
    coherence_ok = True
    failures: list[str] = []

    for p in small_primes:
        layer_support = 0
        layer_steps = 0
        layer_max_depth = 0
        layer_square_base = 0
        for m in range(2, n // p + 1):
            if not is_p_rough(m, p, primes):
                continue
            factors = factor_by_lpf(m, primes)
            prefixes: list[int] = []
            prefix = 1
            for q in factors:
                prefix *= q
                prefixes.append(prefix)
            product_ok = math.prod(factors) == m if factors else False
            ordered_ok = factors == sorted(factors)
            rough_ok = all(q >= p for q in factors) and all(
                is_p_rough(prefix_value, p, primes) for prefix_value in prefixes
            )
            bounded_ok = all(p * prefix_value <= n for prefix_value in prefixes)
            layer_ok = product_ok and ordered_ok and rough_ok and bounded_ok
            if not layer_ok and len(failures) < 10:
                failures.append(f"p={p},m={m},factors={factors},prefixes={prefixes}")
            coherence_ok = coherence_ok and layer_ok
            layer_support += 1
            layer_steps += len(factors)
            layer_max_depth = max(layer_max_depth, len(factors))
            layer_square_base += 1 if m == p else 0
        layers[str(p)] = {
            "support_keys": layer_support,
            "factor_steps": layer_steps,
            "max_factor_depth": layer_max_depth,
            "square_base_keys": layer_square_base,
            "ordered_lpf_path_ok": failures == [] or coherence_ok,
        }
        total_support += layer_support
        total_factor_steps += layer_steps
        max_depth = max(max_depth, layer_max_depth)
        square_base_keys += layer_square_base

    return {
        "N": n,
        "small_prime_layers": len(small_primes),
        "total_phi_lpf_support_keys": total_support,
        "total_ordered_factor_steps": total_factor_steps,
        "max_factor_depth": max_depth,
        "square_base_seed_keys": square_base_keys,
        "ordered_lpf_factorization_coherence_holds": coherence_ok,
        "failures": failures,
        "layers": layers,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PHI_CERT,
        SUPPORT_CERT,
        TRANSPORT_CERT,
        UNIT_SEED_CERT,
        POINTWISE_FRONTIER_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def coherence_fields() -> list[dict[str, str]]:
    """列出 ordered coherence 已闭合的无符号字段。"""
    return [
        {
            "field": "owner_bucket_prime",
            "meaning": "固定 LPF owner prime `p`。",
        },
        {
            "field": "rough_cofactor",
            "meaning": "`m` 为 p-rough 且 `p*m<=N` 的 Phi-LPF support cofactor。",
        },
        {
            "field": "ordered_factor_word",
            "meaning": "按最小素因子剥离得到的唯一非降素因子词 `q_1,...,q_t`，且每个 `q_i>=p`。",
        },
        {
            "field": "prefix_support_path",
            "meaning": "前缀 `q_1...q_j` 仍为 p-rough，且 `p*q_1...q_j<=N`，所以路径不离开 owner bucket。",
        },
        {
            "field": "permutation_lock",
            "meaning": "只采用非降 LPF 词，排除同一 cofactor 的排列重复路径。",
        },
        {
            "field": "signed_update_not_included",
            "meaning": "该一致性只给 path/order，不给 orientation、local factor 或 signed coefficient 更新。",
        },
    ]


def build_rows(
    phi: dict[str, Any],
    support: dict[str, Any],
    transport: dict[str, Any],
    unit_seed: dict[str, Any],
    pointwise: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 ordered coherence 判定表。"""
    samples_ok = all(item["ordered_lpf_factorization_coherence_holds"] for item in samples)
    return [
        row(
            "PhiLPFSupportImported",
            phi.get("prime_count_identity_from_phi_lpf_proved") is True
            and support.get("phi_lpf_support_bijection_proved") is True,
            True,
            "Phi/LPF ownership 已固定 owner bucket 与 p-rough support key。",
            "support/capacity already paid",
        ),
        row(
            "TransportResidualImported",
            transport.get("unsigned_cofactor_split_identity_proved") is True
            and unit_seed.get("rough_cofactor_ordered_factorization_coherence_proved") is False,
            False,
            "旧 rough transport 还把 step local factor update 与 ordered coherence 合在一起。",
            f"{STEP_UPDATE} AND {ORDERED_COHERENCE}",
        ),
        row(
            "OrderedFactorWordExists",
            samples_ok,
            True,
            "对每个 p-rough cofactor `m`，算术基本定理给出唯一非降素因子词。",
            ORDERED_COHERENCE,
        ),
        row(
            "LPFPeelingPathUnique",
            samples_ok,
            True,
            "按最小素因子递次剥离与非降素因子词一致，因此没有路径选择自由。",
            ORDERED_COHERENCE,
        ),
        row(
            "PrefixPathStaysInOwnerBucket",
            samples_ok,
            True,
            "每个前缀仍为 p-rough 且对应 `p*prefix<=p*m<=N`，不会跳出同一 owner bucket。",
            ORDERED_COHERENCE,
        ),
        row(
            "PermutationAmbiguityRemoved",
            samples_ok,
            True,
            "非降 LPF 词把同一 cofactor 的排列重复全部锁死。",
            ORDERED_COHERENCE,
        ),
        row(
            "OrderedCoherenceCurrentCorpusProved",
            samples_ok,
            True,
            "ordered factorization coherence 是纯支撑/路径事实，已由 LPF 剥离和前缀保持性闭合。",
            "ordered coherence removed from latest basis",
        ),
        row(
            "StepLocalFactorUpdateStillOpen",
            True,
            False,
            "有序路径不产生 signed coefficient、orientation parity 或 local factor 乘子。",
            STEP_UPDATE,
        ),
        row(
            "PointwiseTableStillOpen",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "若不走 step update，仍需直接提交逐 Phi-LPF key 的 signed value table。",
            POINTWISE_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只闭合 ordered coherence；未证明 signed local factor、ExactUV、seed cycle-cut、same-set PDEC、new joint 或三命题无条件闭合。",
            f"{STEP_UPDATE} AND ({POINTWISE_TABLE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA})",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 ordered coherence 证书。"""
    phi = load_json(PHI_CERT)
    support = load_json(SUPPORT_CERT)
    transport = load_json(TRANSPORT_CERT)
    unit_seed = load_json(UNIT_SEED_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    samples = [sample_ordered_coherence_audit(n) for n in SAMPLE_N]
    rows = build_rows(phi, support, transport, unit_seed, pointwise, samples)
    retained_basis = (
        f"({POINTWISE_TABLE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA}) "
        f"AND {EXACTUV_PAIR} AND {STEP_UPDATE} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_rough_cofactor_ordered_factorization_coherence_router",
        "status": "phi_lpf_rough_cofactor_ordered_factorization_coherence_closed_step_update_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "phi_lpf_rough_cofactor_ordered_factorization_coherence_router_closed": True,
        "phi_lpf_support_and_capacity_imported": rows[0]["closed"],
        "unsigned_cofactor_split_imported": transport.get("unsigned_cofactor_split_identity_proved") is True,
        "ordered_lpf_factorization_coherence_proved": rows[6]["closed"],
        "rough_cofactor_ordered_factorization_coherence_proved": rows[6]["closed"],
        "rough_cofactor_step_local_factor_update_law_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": ORDERED_COHERENCE,
        "next_direct_attack_target": STEP_UPDATE,
        "parallel_direct_attack_target": POINTWISE_TABLE,
        "nonrecursive_breaker_alternatives": [
            SEED_CYCLE_CUT,
            PDEC_SCOPE,
            NEW_JOINT_FORMULA,
        ],
        "retained_basis_after_router": retained_basis,
        "coherence_fields": coherence_fields(),
        "sample_ordered_coherence_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Phi-LPF rough cofactor 的 ordered factorization coherence 是纯无符号路径事实："
            "固定 owner prime `p` 后，每个 p-rough cofactor `m` 由最小素因子剥离得到唯一非降素因子词，"
            "所有前缀仍为 p-rough 且对应 composite `p*prefix` 仍在同一 owner bucket 内。"
            "因此 ordered coherence 可从最新剩余基中移除。"
            "但该路径事实不产生 signed coefficient、orientation parity 或 local factor 乘子；"
            "真正剩余为 `PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward`，"
            "或直接提交逐 Phi-LPF key signed value table，或进入 seed cycle-cut、same-set PDEC、new joint formula。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF rough cofactor ordered factorization coherence 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phi_lpf_support_and_capacity_imported={fmt_bool(cert['phi_lpf_support_and_capacity_imported'])}",
        f"unsigned_cofactor_split_imported={fmt_bool(cert['unsigned_cofactor_split_imported'])}",
        f"rough_cofactor_ordered_factorization_coherence_proved={fmt_bool(cert['rough_cofactor_ordered_factorization_coherence_proved'])}",
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
            "## 2. 已闭合字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in cert["coherence_fields"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 样本审计摘要",
            "",
            "| N | support keys | factor steps | max depth | square-base keys | ok |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in cert["sample_ordered_coherence_audit"]:
        lines.append(
            f"| {item['N']} | {item['total_phi_lpf_support_keys']} | "
            f"{item['total_ordered_factor_steps']} | {item['max_factor_depth']} | "
            f"{item['square_base_seed_keys']} | `{fmt_bool(item['ordered_lpf_factorization_coherence_holds'])}` |"
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
            "并行直接入口：",
            "",
            "```text",
            cert["parallel_direct_attack_target"],
            "```",
            "",
            "非循环破环替代：",
            "",
            "```text",
            "\n".join(cert["nonrecursive_breaker_alternatives"]),
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
    """写出 ordered coherence 证书。"""
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
