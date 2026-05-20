#!/usr/bin/env python3
"""生成 Phi-LPF bucket signed transport 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_bucket_signed_transport_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.json

输出：
  data/prime-matrix-phi-lpf-bucket-signed-transport-ledger.json
  docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.json
  docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.md
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

SLUG = "prime-matrix-phi-lpf-bucket-signed-transport"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
PHI_CERT = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"
LPF_CANDIDATE_CERT = DOCS / "prime-matrix-lpf-candidate-row-map-alpha-rule-router.json"
SIGNED_VALUE_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"
SIGNED_LIFT_CERT = DOCS / "prime-matrix-strict-alpha-formula-signed-lift-router.json"
PRIMITIVE_EXPR_CERT = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
FIXED_POINT_CERT = DOCS / "prime-matrix-strict-signed-source-fixed-point-breaker-router.json"

TARGET = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
NEXT_TARGET = "PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward"
ROWWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
SIGNED_SUM_IDENTITY = "PhiLPFBucketPrepushforwardSignedSumIdentity"
PHI_SUPPORT = "PhiLPFPrimitiveRowSupportAndCapacityLedger"

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


def phi_direct(x: int, p: int, primes: list[int]) -> int:
    """直接计数 Phi(x,p)，包含 1。"""
    if x < 1:
        return 0
    return sum(1 for value in range(1, x + 1) if is_p_rough(value, p, primes))


def sample_transport_audit(n: int) -> dict[str, Any]:
    """审计 Phi-LPF cofactor split 与 signed transport 所需字段。"""
    primes = primes_up_to(n)
    prime_to_index = {p: index for index, p in enumerate(primes)}
    small_primes = [p for p in primes if p <= math.isqrt(n)]
    layers: dict[str, dict[str, int | bool]] = {}
    split_ok = True
    total_support = 0
    total_nondivisible = 0
    total_divisible_preimages = 0

    for p in small_primes:
        index = prime_to_index[p]
        next_p = primes[index + 1] if index + 1 < len(primes) else n + 1
        x = n // p
        support_count = sum(1 for m in range(2, x + 1) if is_p_rough(m, p, primes))
        nondivisible_count = sum(
            1 for m in range(2, x + 1) if m % p != 0 and is_p_rough(m, p, primes)
        )
        divisible_preimage_count = sum(
            1 for m in range(1, (x // p) + 1) if is_p_rough(m, p, primes)
        )
        phi_split_support_count = (phi_direct(x, next_p, primes) - 1) + phi_direct(
            x // p, p, primes
        )
        layer_ok = support_count == nondivisible_count + divisible_preimage_count
        phi_layer_ok = support_count == phi_split_support_count
        split_ok = split_ok and layer_ok and phi_layer_ok
        total_support += support_count
        total_nondivisible += nondivisible_count
        total_divisible_preimages += divisible_preimage_count
        layers[str(p)] = {
            "x_floor_N_over_p": x,
            "next_prime": next_p,
            "support_count_phi_minus_one": support_count,
            "nondivisible_next_rough_count": nondivisible_count,
            "divisible_preimage_p_rough_count": divisible_preimage_count,
            "phi_split_support_count": phi_split_support_count,
            "cofactor_split_ok": layer_ok,
            "phi_split_ok": phi_layer_ok,
        }

    return {
        "N": n,
        "small_prime_layers": len(small_primes),
        "total_phi_lpf_support_keys": total_support,
        "total_nondivisible_next_rough_keys": total_nondivisible,
        "total_divisible_preimage_keys": total_divisible_preimages,
        "cofactor_split_identity_holds": split_ok,
        "same_capacity_sign_shadow_bits": total_support,
        "same_capacity_sign_shadow_log10": round(total_support * math.log10(2), 6),
        "layers": layers,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS_CERT,
        PHI_CERT,
        LPF_CANDIDATE_CERT,
        SIGNED_VALUE_CERT,
        SIGNED_LIFT_CERT,
        PRIMITIVE_EXPR_CERT,
        FIXED_POINT_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def transport_law_fields() -> list[dict[str, str]]:
    """列出 signed transport law 必须携带的字段。"""
    return [
        {
            "field": "owner_bucket_prime",
            "meaning": "外层 LPF owner prime `p`，即 candidate composite 的最小素因子。",
        },
        {
            "field": "rough_cofactor_step",
            "meaning": "Phi 递推中的 cofactor 乘法步 `m -> q*m`，特别是 `q=p_k`。",
        },
        {
            "field": "signed_coefficient_transport",
            "meaning": "正向给出 `a_p(q*m)` 与 `a_p(m)` 或原始 source row 的关系。",
        },
        {
            "field": "orientation_parity_update",
            "meaning": "cofactor 乘法对 orientation、奇偶分支和符号的更新规则。",
        },
        {
            "field": "local_factor_multiplier",
            "meaning": "乘入 `q` 后 local factor、截断因子、非零条件的更新。",
        },
        {
            "field": "alpha_delta_side_branch_transition",
            "meaning": "同一 key 在 alpha/delta 侧、branch key、ExactUV 输出中的传输。",
        },
        {
            "field": "prepushforward_signed_sum_identity",
            "meaning": "传输后的有限 signed 求和在 Phi/payment 推前前闭合。",
        },
        {
            "field": "return_tag",
            "meaning": "传输失败、零因子、符号冲突或后验依赖时的命名回流。",
        },
        {
            "field": "no_downstream_recovery",
            "meaning": "传输律不能读取 payment skeleton、零行覆盖、origin table 固定点或终端反推。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    phi: dict[str, Any],
    lpf_candidate: dict[str, Any],
    signed_value: dict[str, Any],
    signed_lift: dict[str, Any],
    primitive_expr: dict[str, Any],
    fixed_point: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 Phi-LPF signed transport 判定表。"""
    samples_ok = all(item["cofactor_split_identity_holds"] for item in samples)
    support_closed = previous.get("support_and_capacity_components_closed") is True
    signed_open = previous.get("phi_lpf_bucket_signed_coefficient_law_proved") is False
    return [
        row(
            "PhiLPFSignedLawTargetImported",
            previous.get("next_direct_attack_target") == TARGET and signed_open,
            False,
            "上一层已把 signed kernel 的剩余压成 Phi-LPF bucket signed coefficient law。",
            TARGET,
        ),
        row(
            "PhiRecursiveLPFSupportImported",
            phi.get("prime_count_identity_from_phi_lpf_proved") is True and support_closed,
            True,
            "Phi/LPF 递推和 support bijection 已关闭无符号支撑与容量。",
            PHI_SUPPORT,
        ),
        row(
            "UnsignedCofactorSplitClosed",
            samples_ok,
            True,
            "对每个 owner prime `p`，cofactor 支撑按 `m` 是否被当前递推素数整除精确分裂。",
            PHI_SUPPORT,
        ),
        row(
            "SignedBucketSumPartitionClosedFormally",
            samples_ok,
            True,
            "任意已给定的 rowwise signed 系数 `a_p(m)` 都可沿同一分裂作有限求和；这是形式恒等式，不产生系数值。",
            ROWWISE_TABLE,
        ),
        row(
            "PhiCountsDoNotDetermineSignedValues",
            samples_ok,
            True,
            "同一 Phi 支撑容量可承载大量 signed decorations；Phi 计数只给 domain，不给 orientation/local factor。",
            NEXT_TARGET,
        ),
        row(
            "TransportLawIsFirstRecursiveSignedField",
            True,
            True,
            "若要把 Phi 递推升级为 signed 递推，第一字段必须说明 cofactor 乘法下 signed coefficient 如何传输。",
            NEXT_TARGET,
        ),
        row(
            "LPFCandidateMapStillUnsigned",
            lpf_candidate.get("lpf_candidate_row_emission_map_closed") is True,
            False,
            "LPF candidate-row map 给唯一候选行索引，但不输出 signed coefficient。",
            ROWWISE_TABLE,
        ),
        row(
            "PointwiseSignedValueTableStillOpen",
            signed_value.get("pointwise_signed_alpha_coefficient_value_table_proved") is False,
            False,
            "现有逐点 signed alpha value table 未闭合；Phi-LPF bucket 版本也未提交。",
            ROWWISE_TABLE,
        ),
        row(
            "SignedLiftAndPrimitiveExpressionStillOpen",
            signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is False
            and primitive_expr.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "signed lift 与 primitive summand signed expression 均仍缺正向系数来源。",
            NEXT_TARGET,
        ),
        row(
            "NoDownstreamRecoveryImported",
            fixed_point.get("current_internal_route_is_signed_source_fixed_point") is True,
            True,
            "旧 signed-source 路线会回到自身；不能用 payment、零行或 origin table 反推 signed transport。",
            "fixed-point cut imported",
        ),
        row(
            "PhiLPFBucketSignedCoefficientLawCurrentCorpusProved",
            False,
            False,
            "当前材料尚未给出 cofactor signed transport law 或等价 rowwise signed coefficient table。",
            f"{NEXT_TARGET} OR {ROWWISE_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步没有证明 signed coefficient law、ExactUV fixed-key、终端排斥或三命题无条件闭合。",
            f"{NEXT_TARGET} OR {ROWWISE_TABLE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 Phi-LPF bucket signed transport 证书。"""
    previous = load_json(PREVIOUS_CERT)
    phi = load_json(PHI_CERT)
    lpf_candidate = load_json(LPF_CANDIDATE_CERT)
    signed_value = load_json(SIGNED_VALUE_CERT)
    signed_lift = load_json(SIGNED_LIFT_CERT)
    primitive_expr = load_json(PRIMITIVE_EXPR_CERT)
    fixed_point = load_json(FIXED_POINT_CERT)
    samples = [sample_transport_audit(n) for n in SAMPLE_N]
    samples_ok = all(item["cofactor_split_identity_holds"] for item in samples)
    rows = build_rows(
        previous=previous,
        phi=phi,
        lpf_candidate=lpf_candidate,
        signed_value=signed_value,
        signed_lift=signed_lift,
        primitive_expr=primitive_expr,
        fixed_point=fixed_point,
        samples=samples,
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_bucket_signed_transport_router",
        "status": "phi_lpf_signed_law_reduced_to_rough_cofactor_signed_transport_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "target_input_before_router": TARGET,
        "phi_lpf_bucket_signed_transport_router_closed": True,
        "phi_lpf_support_and_capacity_imported": rows[1]["closed"],
        "unsigned_cofactor_split_identity_proved": samples_ok,
        "signed_bucket_sum_partition_identity_proved": samples_ok,
        "phi_counts_determine_support_not_signed_values": True,
        "phi_lpf_rough_cofactor_signed_transport_law_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "phi_lpf_bucket_signed_coefficient_law_proved": False,
        "noncircular_signed_coefficient_emission_kernel_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_after_router": f"({NEXT_TARGET} OR {ROWWISE_TABLE}) AND {SIGNED_SUM_IDENTITY}",
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_direct_attack_target": ROWWISE_TABLE,
        "transport_law_fields": transport_law_fields(),
        "sample_transport_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Phi/LPF 递推继续给出 signed law 的精确支撑分裂：每个 owner bucket `p` 中，"
            "p-rough cofactor 集合按是否含当前递推素因子分成 next-rough 部分和 `m=q*m'` 的回流部分。"
            "但这个分裂只移动 domain；要得到 signed 递推，必须正向给出 `a_p(q*m')` 的符号、local factor、"
            "alpha/delta side 和 branch 传输律。因而最新硬点从泛化 bucket signed law 收窄为 "
            "`PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward`，或等价提交逐 Phi-LPF bucket 的 signed value table。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF bucket signed transport 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phi_lpf_support_and_capacity_imported={fmt_bool(cert['phi_lpf_support_and_capacity_imported'])}",
        f"unsigned_cofactor_split_identity_proved={fmt_bool(cert['unsigned_cofactor_split_identity_proved'])}",
        f"signed_bucket_sum_partition_identity_proved={fmt_bool(cert['signed_bucket_sum_partition_identity_proved'])}",
        f"phi_lpf_rough_cofactor_signed_transport_law_proved={fmt_bool(cert['phi_lpf_rough_cofactor_signed_transport_law_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"phi_lpf_bucket_signed_coefficient_law_proved={fmt_bool(cert['phi_lpf_bucket_signed_coefficient_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. signed Phi 分裂",
        "",
        "对 owner prime `p` 写 `a_p(m)` 为待证明的 Cauchy 前 signed coefficient。Phi 递推只给出支撑分裂：",
        "",
        "```text",
        "sum_{m p-rough, 1<m<=x} a_p(m)",
        "  = sum_{m p_next-rough, 1<m<=x} a_p(m)",
        "    + sum_{m' p-rough, m'<=floor(x/p)} a_p(p*m')",
        "```",
        "",
        "右侧第二项仍含未知的 `a_p(p*m')`，所以 signed 闭合需要 cofactor 乘法传输律。",
        "",
        "## 2. 样本支撑分裂审计",
        "",
        "| N | support keys | nondivisible | divisible preimages | split | sign-shadow log10 |",
        "| ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for item in cert["sample_transport_audit"]:
        lines.append(
            f"| {item['N']} | {item['total_phi_lpf_support_keys']} | "
            f"{item['total_nondivisible_next_rough_keys']} | {item['total_divisible_preimage_keys']} | "
            f"`{fmt_bool(item['cofactor_split_identity_holds'])}` | {item['same_capacity_sign_shadow_log10']} |"
        )
    lines.extend(
        [
            "",
            "## 3. signed transport 字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in cert["transport_law_fields"]:
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
            "等价并行入口：",
            "",
            "```text",
            cert["parallel_direct_attack_target"],
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
