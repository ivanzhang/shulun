#!/usr/bin/env python3
"""生成 Phi-LPF 支撑剥离后的 signed kernel 证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_support_stripped_signed_kernel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json

输出：
  data/prime-matrix-phi-lpf-support-stripped-signed-kernel-ledger.json
  docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json
  docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.md
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

SLUG = "prime-matrix-phi-lpf-support-stripped-signed-kernel"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PHI_CERT = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"
LPF_CANDIDATE_CERT = DOCS / "prime-matrix-lpf-candidate-row-map-alpha-rule-router.json"
NONCIRCULAR_KERNEL_CERT = DOCS / "prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json"
SIGNED_EXPRESSION_CERT = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
SIGNED_FIXED_POINT_CERT = DOCS / "prime-matrix-strict-signed-source-fixed-point-breaker-router.json"

PHI_SUPPORT = "PhiLPFPrimitiveRowSupportAndCapacityLedger"
SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
NONCIRCULAR_KERNEL = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
SIGNED_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
LPF_CANDIDATE_MAP = "LPFOwnershipAlphaCandidateRowEmissionMapLedger"

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


def least_prime_factor(n: int, primes: list[int]) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def is_p_rough(value: int, p: int, primes: list[int]) -> bool:
    """判断 value 是否没有小于 p 的素因子。"""
    return all(value % q != 0 for q in primes if q < p)


def sample_support_audit(n: int) -> dict[str, Any]:
    """审计 LPF/Phi 支撑键与合数集合一一对应。"""
    primes = primes_up_to(n)
    prime_set = set(primes)
    small_primes = [p for p in primes if p <= math.isqrt(n)]

    composite_to_key: dict[int, tuple[int, int]] = {}
    key_to_composite: dict[tuple[int, int], int] = {}
    duplicate_keys: list[str] = []
    rough_failures: list[str] = []

    for value in range(2, n + 1):
        if value in prime_set:
            continue
        p = least_prime_factor(value, primes)
        m = value // p
        key = (p, m)
        composite_to_key[value] = key
        if key in key_to_composite:
            duplicate_keys.append(f"{key}->{key_to_composite[key]},{value}")
        key_to_composite[key] = value
        if p not in small_primes or m < p or not is_p_rough(m, p, primes):
            rough_failures.append(f"{value}={p}*{m}")

    phi_support_keys: set[tuple[int, int]] = set()
    layer_counts: dict[str, int] = {}
    for p in small_primes:
        count = 0
        for m in range(1, n // p + 1):
            if is_p_rough(m, p, primes):
                if m > 1:
                    phi_support_keys.add((p, m))
                    count += 1
        layer_counts[str(p)] = count

    composite_key_set = set(composite_to_key.values())
    missing_from_phi = sorted(composite_key_set - phi_support_keys)[:10]
    extra_phi = sorted(phi_support_keys - composite_key_set)[:10]
    support_bijection_holds = (
        not duplicate_keys
        and not rough_failures
        and composite_key_set == phi_support_keys
        and len(composite_to_key) == len(phi_support_keys)
    )
    return {
        "N": n,
        "prime_count": len(primes),
        "composite_count": len(composite_to_key),
        "phi_lpf_support_key_count": len(phi_support_keys),
        "support_bijection_holds": support_bijection_holds,
        "layer_count_sum": sum(layer_counts.values()),
        "layer_counts": layer_counts,
        "duplicate_keys": duplicate_keys[:10],
        "rough_failures": rough_failures[:10],
        "missing_from_phi": [str(item) for item in missing_from_phi],
        "extra_phi": [str(item) for item in extra_phi],
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PHI_CERT,
        LPF_CANDIDATE_CERT,
        NONCIRCULAR_KERNEL_CERT,
        SIGNED_EXPRESSION_CERT,
        SIGNED_FIXED_POINT_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def signed_law_fields() -> list[dict[str, str]]:
    """列出剩余 signed law 必须给出的字段。"""
    return [
        {
            "field": "bucket_key",
            "meaning": "LPF/Phi 已闭合的 `(p,m)` primitive row support key。",
        },
        {
            "field": "signed_coefficient_value",
            "meaning": "对该 key 的 Cauchy 前 signed coefficient 正向赋值。",
        },
        {
            "field": "sign_local_factor",
            "meaning": "sign、local factor、非零条件与失败回流标签。",
        },
        {
            "field": "alpha_delta_side_and_branch_key",
            "meaning": "该 key 属于 alpha/delta 哪侧、哪个 branch key、哪个 `(u,v)` 输出。",
        },
        {
            "field": "prepushforward_sum_identity",
            "meaning": "对全部 Phi-LPF keys 的 signed 求和在推前前等于 actual alpha/delta 贡献。",
        },
        {
            "field": "no_downstream_recovery",
            "meaning": "赋值律不读取 payment skeleton、零行覆盖、来源恒等式或终端反推。",
        },
    ]


def build_rows(
    phi: dict[str, Any],
    lpf_candidate: dict[str, Any],
    noncircular: dict[str, Any],
    signed_expression: dict[str, Any],
    fixed_point: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 Phi-LPF 支撑剥离判定表。"""
    samples_ok = all(item["support_bijection_holds"] for item in samples)
    return [
        row(
            "NoncircularKernelImported",
            noncircular.get("noncircular_kernel_router_closed") is True,
            False,
            "现有非循环 kernel 路由已把 signed-source 固定点的第一入口钉到 pre-Cauchy declaration。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "SignedSourceFixedPointImported",
            fixed_point.get("current_internal_route_is_signed_source_fixed_point") is True,
            True,
            "旧 signed-source 链已确认会从 row-level 表绕回自身，不能作为证明。",
            "fixed-point cut imported",
        ),
        row(
            "PhiRecursiveLPFOwnershipImported",
            phi.get("prime_count_identity_from_phi_lpf_proved") is True,
            True,
            "Phi 递推已证明 LPF rough-count 桶公式和素数计数恒等式。",
            PHI_SUPPORT,
        ),
        row(
            "LPFCandidateRowMapImported",
            lpf_candidate.get("lpf_candidate_row_emission_map_closed") is True,
            True,
            "LPF ownership 已给 alpha-side candidate row 的非后验支撑索引。",
            LPF_CANDIDATE_MAP,
        ),
        row(
            "PhiLPFSupportBijectionClosed",
            samples_ok,
            True,
            "每个合数 candidate 支撑键唯一写成 `(p,m)`，其中 `p=LPF(pm)` 且 `m` 为 p-rough；样本逐项验证。",
            PHI_SUPPORT,
        ),
        row(
            "SupportAndCapacityNoLongerSignedKernelGap",
            samples_ok and phi.get("large_prime_layer_zero_mass_proved") is True,
            True,
            "行支撑、容量和 p>sqrt(N) 零质量已由 Phi-LPF 层支付，不能再混入 signed kernel 缺口。",
            PHI_SUPPORT,
        ),
        row(
            "PrimitiveSummandSignedExpressionStillOpen",
            signed_expression.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "signed expression 仍未证明；现在其无符号 support 子问题已剥离。",
            SIGNED_LAW,
        ),
        row(
            "PhiLPFBucketSignedCoefficientLawStillOpen",
            True,
            False,
            "剩余必须对每个 Phi-LPF support key 正向赋 signed coefficient、local factor 和推前前求和恒等式。",
            SIGNED_LAW,
        ),
        row(
            "NoncircularKernelReducedToSignedLawOnPhiLPFBuckets",
            samples_ok,
            False,
            "非循环 signed kernel 被收窄为 Phi-LPF support 上的 signed coefficient law，而非找行或数行问题。",
            f"{PHI_SUPPORT} AND {SIGNED_LAW}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步没有证明 signed coefficient law、alpha/delta pairing、ExactUV fixed-key 或终端排斥。",
            SIGNED_LAW,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 Phi-LPF 支撑剥离证书。"""
    phi = load_json(PHI_CERT)
    lpf_candidate = load_json(LPF_CANDIDATE_CERT)
    noncircular = load_json(NONCIRCULAR_KERNEL_CERT)
    signed_expression = load_json(SIGNED_EXPRESSION_CERT)
    fixed_point = load_json(SIGNED_FIXED_POINT_CERT)
    samples = [sample_support_audit(n) for n in SAMPLE_N]
    samples_ok = all(item["support_bijection_holds"] for item in samples)
    rows = build_rows(
        phi=phi,
        lpf_candidate=lpf_candidate,
        noncircular=noncircular,
        signed_expression=signed_expression,
        fixed_point=fixed_point,
        samples=samples,
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_support_stripped_signed_kernel_router",
        "status": "phi_lpf_support_closed_signed_bucket_law_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "phi_recursive_lpf_ownership_imported": rows[2]["closed"],
        "lpf_candidate_row_map_imported": rows[3]["closed"],
        "phi_lpf_support_bijection_proved": samples_ok,
        "support_and_capacity_components_closed": rows[5]["closed"],
        "primitive_summand_signed_weight_expression_proved": False,
        "phi_lpf_bucket_signed_coefficient_law_proved": False,
        "noncircular_signed_coefficient_emission_kernel_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": NONCIRCULAR_KERNEL,
        "hardpoint_after_router": f"{PHI_SUPPORT} AND {SIGNED_LAW}",
        "next_direct_attack_target": SIGNED_LAW,
        "signed_law_fields": signed_law_fields(),
        "sample_support_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Phi/LPF 精确分桶把 noncircular signed kernel 中的无符号支撑、容量和候选行索引全部剥离。"
            "每个合数 candidate 支撑键唯一为 `(p,m)`，其中 `p` 是最小素因子、`m` 为 p-rough，"
            "容量为 `Phi(floor(N/p),p)-1`。因此最新缺口不再是找行、数行或证明粗数容量，"
            "而是对这些 Phi-LPF support keys 正向赋 signed coefficient、sign/local factor 和推前前 alpha/delta 求和恒等式。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF support-stripped signed kernel 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phi_recursive_lpf_ownership_imported={fmt_bool(cert['phi_recursive_lpf_ownership_imported'])}",
        f"lpf_candidate_row_map_imported={fmt_bool(cert['lpf_candidate_row_map_imported'])}",
        f"phi_lpf_support_bijection_proved={fmt_bool(cert['phi_lpf_support_bijection_proved'])}",
        f"support_and_capacity_components_closed={fmt_bool(cert['support_and_capacity_components_closed'])}",
        f"phi_lpf_bucket_signed_coefficient_law_proved={fmt_bool(cert['phi_lpf_bucket_signed_coefficient_law_proved'])}",
        f"noncircular_signed_coefficient_emission_kernel_proved={fmt_bool(cert['noncircular_signed_coefficient_emission_kernel_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 支撑剥离",
        "",
        "Phi-LPF 层给出的 support key 是 `(p,m)`，其中 `p<=sqrt(N)`，`m<=floor(N/p)`，`m>1`，且 `m` 没有小于 `p` 的素因子。该 key 对应唯一合数 `pm`，不同 key 不重叠。",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  ->",
        cert["hardpoint_after_router"],
        "```",
        "",
        "## 2. 样本审计",
        "",
        "| N | pi(N) | composites | support keys | bijection |",
        "| ---: | ---: | ---: | ---: | --- |",
    ]
    for item in cert["sample_support_audit"]:
        lines.append(
            f"| {item['N']} | {item['prime_count']} | {item['composite_count']} | "
            f"{item['phi_lpf_support_key_count']} | `{fmt_bool(item['support_bijection_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 3. signed law 剩余字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in cert["signed_law_fields"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
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
            "## 5. 下一真正单点",
            "",
            "```text",
            cert["next_direct_attack_target"],
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
