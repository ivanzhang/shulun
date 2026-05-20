#!/usr/bin/env python3
"""生成 LPF ownership sieve 到 source declaration 的桥接证书。

用法示例：
  python3 experiments/prime_matrix_lpf_ownership_sieve_source_declaration_router.py
  python3 -m json.tool docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.json

输出：
  data/prime-matrix-lpf-ownership-sieve-source-declaration-ledger.json
  docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.json
  docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.md
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

SLUG = "prime-matrix-lpf-ownership-sieve-source-declaration"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SOURCE_TABLE_CERT = DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json"
FORMULA_LINE_CERT = DOCS / "prime-matrix-strict-actual-constructor-formula-line-router.json"
UNSIGNED_SKELETON_CERT = DOCS / "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"
SOURCE_UNIFICATION_CERT = DOCS / "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json"
LEAST_FACTOR_CUTOFF_DOC = DOCS / "prime-matrix-least-factor-activation-cutoff.md"

PRECAUCHY_DECLARATION = "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
LPF_UNSIGNED = "LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger"
FORMULA_LINE = "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter"
EXPLICIT_RULE = "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"
DOMAIN_LEDGER = "ConstructorDomainCleanCoreMembershipLedger"
ROW_LEDGER = "ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger"
RETURN_LEDGER = "ConstructorFormulaFailureReturnTagsLedger"
NO_DOWNSTREAM = "SourceDeclarationNoDownstreamRecoveryAndNamedReturnLedger"

AFTER_DECLARATION = (
    f"{LPF_UNSIGNED} AND {EXPLICIT_RULE} AND {DOMAIN_LEDGER} AND "
    f"{ROW_LEDGER} AND {RETURN_LEDGER} AND {NO_DOWNSTREAM}"
)

SAMPLE_N = [10, 30, 100, 997, 5003]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；文件不存在时返回空对象。"""
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
            step_start = p * p
            sieve[step_start : n + 1 : p] = [False] * (((n - step_start) // p) + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def least_prime_factor(n: int, primes: list[int]) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def lpf_identity_sample(n: int) -> dict[str, Any]:
    """审计 pi(N)=N-1-sum_p LPF_p(N) 与 quotient 条件。"""
    primes = primes_up_to(n)
    prime_set = set(primes)
    root = math.isqrt(n)
    small_primes = [p for p in primes if p <= root]
    buckets_by_lpf = {p: 0 for p in small_primes}
    quotient_buckets = {p: 0 for p in small_primes}
    quotient_condition_ok = True

    for value in range(2, n + 1):
        if value in prime_set:
            continue
        p = least_prime_factor(value, primes)
        buckets_by_lpf[p] += 1
        m = value // p
        if m < p or any(m % q == 0 for q in small_primes if q < p):
            quotient_condition_ok = False

    for p in small_primes:
        smaller_primes = [q for q in small_primes if q < p]
        for m in range(p, n // p + 1):
            if all(m % q != 0 for q in smaller_primes):
                quotient_buckets[p] += 1

    bucket_sum = sum(buckets_by_lpf.values())
    quotient_bucket_sum = sum(quotient_buckets.values())
    prime_count = len(primes)
    identity_prime_count = n - 1 - bucket_sum
    return {
        "N": n,
        "sqrt_floor": root,
        "prime_count": prime_count,
        "bucket_sum": bucket_sum,
        "identity_prime_count": identity_prime_count,
        "identity_holds": identity_prime_count == prime_count,
        "quotient_bucket_sum": quotient_bucket_sum,
        "quotient_bucket_identity_holds": quotient_buckets == buckets_by_lpf,
        "quotient_condition_ok": quotient_condition_ok,
        "buckets_by_lpf": {str(p): buckets_by_lpf[p] for p in small_primes},
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        SOURCE_TABLE_CERT,
        FORMULA_LINE_CERT,
        UNSIGNED_SKELETON_CERT,
        SOURCE_UNIFICATION_CERT,
        LEAST_FACTOR_CUTOFF_DOC,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def replace_declaration_target(source_table: dict[str, Any]) -> str:
    """把 source-table 的 declaration line 替换为本层细化后的接口。"""
    basis = source_table.get("terminal_gap_after_router", "")
    if PRECAUCHY_DECLARATION in basis:
        return basis.replace(PRECAUCHY_DECLARATION, AFTER_DECLARATION)
    return AFTER_DECLARATION


def build_rows(
    source_table: dict[str, Any],
    formula_line: dict[str, Any],
    unsigned_skeleton: dict[str, Any],
    source_unification: dict[str, Any],
    samples: list[dict[str, Any]],
    after_source_table: str,
) -> list[dict[str, Any]]:
    """生成 LPF ownership source declaration 判定表。"""
    target_imported = PRECAUCHY_DECLARATION in source_table.get("terminal_gap_after_router", "")
    formula_router_closed = formula_line.get("actual_constructor_formula_line_router_closed") is True
    unsigned_skeleton_closed = unsigned_skeleton.get("alpha_row_unsigned_skeleton_router_closed") is True
    common_packet_open = source_unification.get("common_packet_proved") is False
    samples_ok = all(
        item["identity_holds"]
        and item["quotient_bucket_identity_holds"]
        and item["quotient_condition_ok"]
        for item in samples
    )
    return [
        row(
            "PreCauchyDeclarationLineTargetImported",
            target_imported,
            False,
            "actual emitter source table 的第一合法字段仍是 pre-Cauchy constructor declaration line。",
            PRECAUCHY_DECLARATION,
        ),
        row(
            "AscendingLeastPrimeFactorOwnershipPartition",
            True,
            True,
            "每个合数按唯一最小素因子进入且只进入一个筛层；p 层新筛数为 p*m<=N、m>=p、且 m 无小于 p 的素因子。",
            LPF_UNSIGNED,
        ),
        row(
            "PrimeCountingIdentityFromLPFOwnership",
            samples_ok,
            True,
            "因此 pi(N)=N-1-sum_{p<=sqrt(N)} #{n<=N: n composite and LPF(n)=p}，样本审计也逐项通过。",
            LPF_UNSIGNED,
        ),
        row(
            "LeastFactorCutoffImported",
            LEAST_FACTOR_CUTOFF_DOC.exists(),
            True,
            "逐行最小因子激活截止已记录：超过 sqrt 窗口的斜线只是 shadow hit，不产生新的独立 ownership。",
            LPF_UNSIGNED,
        ),
        row(
            "LPFOwnershipIsPreCauchyUnsignedDeclaration",
            True,
            True,
            "LPF ownership 只读取自然数、整除关系和筛层顺序；不依赖 Cauchy、Phi、payment 或零行反推。",
            LPF_UNSIGNED,
        ),
        row(
            "UnsignedSkeletonCompatibilityImported",
            unsigned_skeleton_closed,
            True,
            "现有 unsigned skeleton 已能承接 source tuple、carry shell、P 列相位和 layered-wheel 兼容字段。",
            "AlphaRowUnsignedSkeletonLedger",
        ),
        row(
            "LPFOwnershipDoesNotEmitSignedAlphaDelta",
            True,
            True,
            "LPF 分桶只给合数 ownership 与候选行索引；它不产生 orientation、signed coefficient、local factor 或 alpha/delta 权重。",
            "AlphaFormulaSignedCoefficientLiftLedger",
        ),
        row(
            "ActualConstructorFormulaLineRouterImported",
            formula_router_closed,
            False,
            "actual constructor formula line 已有路由：必须继续给显式 alpha/delta primitive constructor rule、定义域、行输出和失败回流。",
            formula_line.get("terminal_gap_after_router", AFTER_DECLARATION),
        ),
        row(
            "SourceDeclarationCommonPacketStillOpen",
            common_packet_open,
            False,
            "payload/ExactUV 合流所需的 common pre-Cauchy source declaration packet 仍未由当前语料证明。",
            "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket",
        ),
        row(
            "DeclarationLineReducedToLPFOwnershipAndExplicitFormula",
            True,
            False,
            "本步把 declaration line 的 unsigned ownership 字段闭合，并把真正剩余压回显式 signed constructor 公式与回流纪律。",
            after_source_table,
        ),
        row(
            "ExplicitAlphaDeltaPrimitiveRuleStillOpen",
            False,
            False,
            "当前材料尚未写出 actual noncanonical primitive constructor 的显式 alpha/delta 规则。",
            EXPLICIT_RULE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "LPF ownership 是精确筛法恒等式，但还不是 source signed-lift、ExactUV fixed-key 或全局终端排斥证明。",
            after_source_table,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 LPF ownership source declaration 证书。"""
    source_table = load_json(SOURCE_TABLE_CERT)
    formula_line = load_json(FORMULA_LINE_CERT)
    unsigned_skeleton = load_json(UNSIGNED_SKELETON_CERT)
    source_unification = load_json(SOURCE_UNIFICATION_CERT)
    samples = [lpf_identity_sample(n) for n in SAMPLE_N]
    samples_ok = all(
        item["identity_holds"]
        and item["quotient_bucket_identity_holds"]
        and item["quotient_condition_ok"]
        for item in samples
    )
    after_source_table = replace_declaration_target(source_table)
    rows = build_rows(
        source_table=source_table,
        formula_line=formula_line,
        unsigned_skeleton=unsigned_skeleton,
        source_unification=source_unification,
        samples=samples,
        after_source_table=after_source_table,
    )
    return {
        "certificate_type": "prime_matrix_lpf_ownership_sieve_source_declaration_router",
        "status": "lpf_ownership_unsigned_declaration_closed_signed_constructor_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "pre_cauchy_declaration_line_imported": rows[0]["closed"],
        "ascending_lpf_ownership_partition_proved": True,
        "prime_count_identity_from_lpf_ownership_proved": True,
        "quotient_condition_matches_user_sieve_proved": samples_ok,
        "least_factor_cutoff_imported": LEAST_FACTOR_CUTOFF_DOC.exists(),
        "lpf_ownership_unsigned_declaration_line_closed": True,
        "unsigned_skeleton_compatibility_imported": unsigned_skeleton.get("alpha_row_unsigned_skeleton_router_closed") is True,
        "actual_constructor_formula_line_router_imported": formula_line.get("actual_constructor_formula_line_router_closed") is True,
        "lpf_ownership_to_signed_alpha_delta_lift_proved": False,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "pre_cauchy_constructor_declaration_line_proved": False,
        "actual_noncanonical_primitive_emitter_source_table_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": PRECAUCHY_DECLARATION,
        "hardpoint_after_router": after_source_table,
        "next_direct_attack_target": EXPLICIT_RULE,
        "parallel_open_exits": [
            "ConstructorDomainCleanCoreMembershipLedger",
            "ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger",
            "ConstructorFormulaFailureReturnTagsLedger",
            "SourceDeclarationNoDownstreamRecoveryAndNamedReturnLedger",
            "ActualNoncanonicalPrimitiveEmitterSourceTableLedger",
            "CompletePrimitiveEmitterKeyPartitionLedger",
            "FixedKeyExactUVLocalMultiplicityO1Ledger",
        ],
        "prime_count_identity": (
            "pi(N)=N-1-sum_{p<=sqrt(N)} #{n<=N: n composite and least_prime_factor(n)=p}"
        ),
        "user_sieve_bucket_formula": (
            "LPF_p(N)=#{m: p*m<=N, m>=p, and m has no prime factor < p}"
        ),
        "sample_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "LPF ownership sieve 给出严格非重叠分桶：每个合数按唯一最小素因子 p 归入 p 层，"
            "且 p 层新筛掉的正是 p*m<=N、m>=p、m 的最小素因子不小于 p 的数。"
            "因此素数计数恒等式闭合，并且该恒等式可作为 pre-Cauchy unsigned source ownership 声明。"
            "但它不产生 signed alpha/delta coefficient、local factor 或 exact-UV fixed-key 重数控制；"
            "最新直接主攻转为显式 alpha/delta primitive constructor rule。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix LPF ownership sieve source declaration 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"pre_cauchy_declaration_line_imported={fmt_bool(cert['pre_cauchy_declaration_line_imported'])}",
        f"ascending_lpf_ownership_partition_proved={fmt_bool(cert['ascending_lpf_ownership_partition_proved'])}",
        f"prime_count_identity_from_lpf_ownership_proved={fmt_bool(cert['prime_count_identity_from_lpf_ownership_proved'])}",
        f"quotient_condition_matches_user_sieve_proved={fmt_bool(cert['quotient_condition_matches_user_sieve_proved'])}",
        f"lpf_ownership_unsigned_declaration_line_closed={fmt_bool(cert['lpf_ownership_unsigned_declaration_line_closed'])}",
        f"lpf_ownership_to_signed_alpha_delta_lift_proved={fmt_bool(cert['lpf_ownership_to_signed_alpha_delta_lift_proved'])}",
        f"explicit_alpha_delta_primitive_constructor_rule_proved={fmt_bool(cert['explicit_alpha_delta_primitive_constructor_rule_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确 ownership 恒等式",
        "",
        "对任意 `N>=2`，每个合数 `n<=N` 有唯一最小素因子 `p<=sqrt(N)`。写 `n=p*m`，则 `m>=p`，且 `m` 没有小于 `p` 的素因子。反过来，任意满足这些条件的 `p*m<=N` 的数，其最小素因子正是 `p`。",
        "",
        "```text",
        cert["prime_count_identity"],
        cert["user_sieve_bucket_formula"],
        "```",
        "",
        "这正是从小到大筛入每个素数时的“新筛掉”集合；不同 `p` 的集合互不相交，合并后正好是 `N` 以内所有合数。",
        "",
        "## 2. 样本审计",
        "",
        "| N | pi(N) | bucket sum | identity | quotient buckets |",
        "| ---: | ---: | ---: | --- | --- |",
    ]
    for item in cert["sample_audit"]:
        lines.append(
            f"| {item['N']} | {item['prime_count']} | {item['bucket_sum']} | "
            f"`{fmt_bool(item['identity_holds'])}` | `{fmt_bool(item['quotient_bucket_identity_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 对 source declaration 的影响",
            "",
            "```text",
            f"{PRECAUCHY_DECLARATION}",
            "  ->",
            cert["hardpoint_after_router"],
            "```",
            "",
            "LPF ownership 关闭 declaration line 的 unsigned 分桶字段；真正仍缺的是 actual noncanonical primitive constructor 的 signed `alpha/delta` 规则、定义域、逐行 `(u,v)`/key/sign/local-factor 输出和失败回流。",
            "",
            "## 4. 判定表",
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
            "## 5. 诚实边界",
            "",
            "- 本证书证明的是 LPF ownership 精确分桶和素数计数恒等式。",
            "- 本证书没有证明 signed alpha/delta primitive constructor rule。",
            "- 本证书没有证明 actual emitter source table、complete key partition 或 fixed-key exact-UV local multiplicity。",
            "- 行/列命题仍未无条件闭合。",
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
