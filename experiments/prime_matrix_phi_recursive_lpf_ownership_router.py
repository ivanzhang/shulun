#!/usr/bin/env python3
"""生成 Phi 递推版 LPF ownership 证书。

用法示例：
  python3 experiments/prime_matrix_phi_recursive_lpf_ownership_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json

输出：
  data/prime-matrix-phi-recursive-lpf-ownership-ledger.json
  docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json
  docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from functools import cache
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-recursive-lpf-ownership"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LPF_OWNERSHIP_CERT = DOCS / "prime-matrix-lpf-ownership-sieve-source-declaration-router.json"
LPF_CANDIDATE_CERT = DOCS / "prime-matrix-lpf-candidate-row-map-alpha-rule-router.json"
SIGNED_WEIGHT_FORMULA_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"

PHI_LEDGER = "PhiRecursiveLPFOwnershipRoughCountLedger"
LPF_UNSIGNED = "LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger"
LPF_CANDIDATE_MAP = "LPFOwnershipAlphaCandidateRowEmissionMapLedger"
SIGNED_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"

SAMPLE_N = [10, 30, 100, 997, 5003, 10000]


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


def least_prime_factor(n: int, primes: list[int]) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def rough_count_direct(x: int, p: int, primes: list[int]) -> int:
    """直接计数 Phi(x,p)：没有小于 p 的素因子的正整数个数。"""
    if x < 1:
        return 0
    smaller_primes = [q for q in primes if q < p]
    return sum(1 for value in range(1, x + 1) if all(value % q != 0 for q in smaller_primes))


class PhiComputer:
    """用递推式计算 Phi(x,p_k)。"""

    def __init__(self, primes: list[int]) -> None:
        self.primes = primes

    @cache
    def phi(self, x: int, prime_index: int) -> int:
        """递归计算 Phi(x,p_k)，并以 p_k>x 时只有 1 为基。"""
        if x < 1:
            return 0
        if prime_index >= len(self.primes) or self.primes[prime_index] > x:
            return 1
        p = self.primes[prime_index]
        return self.phi(x, prime_index + 1) + self.phi(x // p, prime_index)


def lpf_bucket_direct(n: int, p: int, primes: list[int], prime_set: set[int]) -> int:
    """直接按最小素因子 p 计数合数桶。"""
    return sum(
        1
        for value in range(2, n + 1)
        if value not in prime_set and least_prime_factor(value, primes) == p
    )


def sample_audit(n: int) -> dict[str, Any]:
    """审计 Phi 递推、LPF 分桶与 pi(N) 恒等式。"""
    primes = primes_up_to(n)
    prime_set = set(primes)
    prime_to_index = {p: index for index, p in enumerate(primes)}
    phi_computer = PhiComputer(primes)
    small_primes = [p for p in primes if p <= math.isqrt(n)]

    buckets: dict[str, dict[str, int | bool]] = {}
    phi_recursion_ok = True
    phi_direct_ok = True
    for p in small_primes:
        index = prime_to_index[p]
        x = n // p
        phi_value = phi_computer.phi(x, index)
        direct_phi = rough_count_direct(x, p, primes)
        c_phi = phi_value - 1
        c_direct = lpf_bucket_direct(n, p, primes, prime_set)
        recurrence_rhs = phi_computer.phi(x, index + 1) + phi_computer.phi(x // p, index)
        recurrence_ok = phi_value == recurrence_rhs
        direct_ok = phi_value == direct_phi and c_phi == c_direct
        phi_recursion_ok = phi_recursion_ok and recurrence_ok
        phi_direct_ok = phi_direct_ok and direct_ok
        buckets[str(p)] = {
            "x_floor_N_over_p": x,
            "phi_recursive": phi_value,
            "phi_direct": direct_phi,
            "c_phi_minus_one": c_phi,
            "lpf_bucket_direct": c_direct,
            "recurrence_ok": recurrence_ok,
            "direct_bucket_ok": direct_ok,
        }

    composite_count = n - 1 - len(primes)
    bucket_sum = sum(int(item["c_phi_minus_one"]) for item in buckets.values())
    pi_from_phi = n - 1 - bucket_sum
    return {
        "N": n,
        "sqrt_floor": math.isqrt(n),
        "prime_count": len(primes),
        "composite_count": composite_count,
        "bucket_sum_from_phi": bucket_sum,
        "pi_from_phi": pi_from_phi,
        "phi_recursion_identity_holds_on_buckets": phi_recursion_ok,
        "phi_recursive_matches_direct_rough_count": phi_direct_ok,
        "lpf_bucket_sum_identity_holds": bucket_sum == composite_count,
        "prime_count_identity_holds": pi_from_phi == len(primes),
        "buckets": buckets,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LPF_OWNERSHIP_CERT,
        LPF_CANDIDATE_CERT,
        SIGNED_WEIGHT_FORMULA_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(
    lpf_ownership: dict[str, Any],
    lpf_candidate: dict[str, Any],
    signed_formula: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 Phi 递推 LPF ownership 判定表。"""
    samples_ok = all(
        item["phi_recursion_identity_holds_on_buckets"]
        and item["phi_recursive_matches_direct_rough_count"]
        and item["lpf_bucket_sum_identity_holds"]
        and item["prime_count_identity_holds"]
        for item in samples
    )
    return [
        row(
            "LPFOwnershipImported",
            lpf_ownership.get("lpf_ownership_unsigned_declaration_line_closed") is True,
            True,
            "上一层已把合数按唯一最小素因子分桶，并关闭 pre-Cauchy unsigned ownership 字段。",
            LPF_UNSIGNED,
        ),
        row(
            "PhiRoughCountDefinitionClosed",
            True,
            True,
            "Phi(x,p) 定义为 1<=m<=x 且无小于 p 的素因子的 rough 计数，包含 m=1。",
            PHI_LEDGER,
        ),
        row(
            "PhiRecursionIdentityClosed",
            samples_ok,
            True,
            "按是否被 p_k 整除分拆，得到 Phi(x,p_k)=Phi(x,p_{k+1})+Phi(floor(x/p_k),p_k)。",
            PHI_LEDGER,
        ),
        row(
            "LPFBucketEqualsPhiMinusOneClosed",
            samples_ok,
            True,
            "p 层新筛合数数 c(p)=Phi(floor(N/p),p)-1；减去的 1 是 cofactor m=1 对应的素数 p。",
            PHI_LEDGER,
        ),
        row(
            "PrimeCountingIdentityFromPhiLPFClosed",
            samples_ok,
            True,
            "求和 p<=sqrt(N) 的 Phi 桶后得到 pi(N)=N-1-sum_p(Phi(floor(N/p),p)-1)。",
            PHI_LEDGER,
        ),
        row(
            "LargePrimeLayerZeroMassClosed",
            True,
            True,
            "当 p>sqrt(N) 时 floor(N/p)<p，Phi(floor(N/p),p)=1，故 c(p)=0。",
            PHI_LEDGER,
        ),
        row(
            "CandidateRowMapImported",
            lpf_candidate.get("lpf_candidate_row_emission_map_closed") is True,
            True,
            "Phi 递推加强 LPF candidate-row map 的源计数，但不改变其 unsigned 性质。",
            LPF_CANDIDATE_MAP,
        ),
        row(
            "PhiOwnershipDoesNotEmitSignedWeight",
            True,
            True,
            "Phi 递推只计算 rough ownership 容量；它不赋 orientation、signed coefficient、local factor 或 primitive summand。",
            SIGNED_EXPR,
        ),
        row(
            "PrimitiveSummandSignedExpressionStillOpen",
            signed_formula.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "逐行 signed primitive summand 表达式仍是 LPF/Phi 无符号层之后的真正硬点。",
            SIGNED_EXPR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步没有证明 signed alpha/delta、pairing、ExactUV fixed-key、DStructure/Rankin 或 endpoint 排斥。",
            SIGNED_EXPR,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 Phi 递推 LPF ownership 证书。"""
    lpf_ownership = load_json(LPF_OWNERSHIP_CERT)
    lpf_candidate = load_json(LPF_CANDIDATE_CERT)
    signed_formula = load_json(SIGNED_WEIGHT_FORMULA_CERT)
    samples = [sample_audit(n) for n in SAMPLE_N]
    samples_ok = all(
        item["phi_recursion_identity_holds_on_buckets"]
        and item["phi_recursive_matches_direct_rough_count"]
        and item["lpf_bucket_sum_identity_holds"]
        and item["prime_count_identity_holds"]
        for item in samples
    )
    rows = build_rows(
        lpf_ownership=lpf_ownership,
        lpf_candidate=lpf_candidate,
        signed_formula=signed_formula,
        samples=samples,
    )
    return {
        "certificate_type": "prime_matrix_phi_recursive_lpf_ownership_router",
        "status": "phi_recursive_lpf_ownership_closed_signed_summand_expression_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "lpf_ownership_imported": rows[0]["closed"],
        "phi_rough_count_definition_proved": True,
        "phi_recursion_identity_proved": True,
        "phi_recursive_lpf_bucket_formula_proved": True,
        "prime_count_identity_from_phi_lpf_proved": True,
        "large_prime_layer_zero_mass_proved": True,
        "sample_audit_all_passed": samples_ok,
        "lpf_candidate_row_map_imported": rows[6]["closed"],
        "phi_recursive_ownership_to_signed_alpha_delta_lift_proved": False,
        "primitive_summand_signed_weight_expression_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": LPF_UNSIGNED,
        "hardpoint_after_router": f"{PHI_LEDGER} AND {SIGNED_EXPR}",
        "next_direct_attack_target": SIGNED_EXPR,
        "parallel_open_exits": [
            "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger",
            "AlphaPrimitiveCoefficientWeightFormulaLedger",
            "AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger",
            "AlphaPrimitiveRuleFailureNamedReturnLedger",
            "ActualNoncanonicalDeltaSidePrimitiveRuleLedger",
            "AlphaDeltaPrimitivePairingCompatibilityLedger",
            "FixedKeyExactUVLocalMultiplicityO1Ledger",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "phi_definition": "Phi(x,p)=#{1<=m<=x: every prime factor of m is >=p}, with m=1 included",
        "phi_recursion_identity": "Phi(x,p_k)=Phi(x,p_{k+1})+Phi(floor(x/p_k),p_k)",
        "phi_lpf_bucket_formula": "c_N(p)=Phi(floor(N/p),p)-1",
        "prime_count_identity": "pi(N)=N-1-sum_{p<=sqrt(N)}(Phi(floor(N/p),p)-1)",
        "sample_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Phi 递推把 LPF ownership 从集合分桶提升为可机械计算的 rough-count 账本。"
            "每个 p 层容量正是 Phi(floor(N/p),p)-1，p>sqrt(N) 自动为零，"
            "所以用户给出的 pi(N) 精确公式闭合。该层仍是无符号 ownership/容量层；"
            "它不生成 actual noncanonical primitive summand 的 signed 权重表达式。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-recursive LPF ownership 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"lpf_ownership_imported={fmt_bool(cert['lpf_ownership_imported'])}",
        f"phi_rough_count_definition_proved={fmt_bool(cert['phi_rough_count_definition_proved'])}",
        f"phi_recursion_identity_proved={fmt_bool(cert['phi_recursion_identity_proved'])}",
        f"phi_recursive_lpf_bucket_formula_proved={fmt_bool(cert['phi_recursive_lpf_bucket_formula_proved'])}",
        f"prime_count_identity_from_phi_lpf_proved={fmt_bool(cert['prime_count_identity_from_phi_lpf_proved'])}",
        f"large_prime_layer_zero_mass_proved={fmt_bool(cert['large_prime_layer_zero_mass_proved'])}",
        f"sample_audit_all_passed={fmt_bool(cert['sample_audit_all_passed'])}",
        f"phi_recursive_ownership_to_signed_alpha_delta_lift_proved={fmt_bool(cert['phi_recursive_ownership_to_signed_alpha_delta_lift_proved'])}",
        f"primitive_summand_signed_weight_expression_proved={fmt_bool(cert['primitive_summand_signed_weight_expression_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Phi 递推",
        "",
        "`Phi(x,p)` 计数 `1<=m<=x` 且所有素因子都不小于 `p` 的整数，并包含 `m=1`。对相邻素数 `p_k,p_{k+1}`，把 `p_k`-rough 数按是否被 `p_k` 整除分为两类：",
        "",
        "```text",
        cert["phi_recursion_identity"],
        "```",
        "",
        "若 `p_k>x`，则只剩 `m=1`，所以 `Phi(x,p_k)=1`。这给出有限递归基。",
        "",
        "## 2. LPF 桶公式",
        "",
        "对 `p<=sqrt(N)`，`p` 层新筛掉的合数为 `p*m<=N` 且 `m` 为 `p`-rough 的项；`m=1` 对应素数 `p` 自身，必须扣除：",
        "",
        "```text",
        cert["phi_lpf_bucket_formula"],
        cert["prime_count_identity"],
        "```",
        "",
        "当 `p>sqrt(N)` 时 `floor(N/p)<p`，递归基给出 `Phi(floor(N/p),p)=1`，所以该层没有新合数质量。",
        "",
        "## 3. 样本审计",
        "",
        "| N | pi(N) | composite count | bucket sum | pi from Phi | recursion | identity |",
        "| ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for item in cert["sample_audit"]:
        lines.append(
            f"| {item['N']} | {item['prime_count']} | {item['composite_count']} | "
            f"{item['bucket_sum_from_phi']} | {item['pi_from_phi']} | "
            f"`{fmt_bool(item['phi_recursion_identity_holds_on_buckets'])}` | "
            f"`{fmt_bool(item['prime_count_identity_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 对最新硬点的影响",
            "",
            "```text",
            f"{LPF_UNSIGNED}",
            "  ->",
            cert["hardpoint_after_router"],
            "```",
            "",
            "Phi 递推给出的是 LPF ownership 的容量读数和机械递归计算。它可以加强 `LPFOwnershipAlphaCandidateRowEmissionMapLedger` 的源容量基础，但不能把 candidate row 升格为 actual signed alpha primitive row。",
            "",
            "最新直接硬点保持为：",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 6. 诚实边界",
            "",
            "- 本证书证明 Phi 递推、LPF 桶公式与素数计数恒等式。",
            "- 本证书没有证明 signed alpha/delta primitive constructor rule。",
            "- 本证书没有证明 local factor、ExactUV fixed-key multiplicity 或 endpoint 终端排斥。",
            "- 行/列命题仍未无条件闭合。",
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
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
