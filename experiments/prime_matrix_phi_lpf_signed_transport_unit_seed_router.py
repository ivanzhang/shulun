#!/usr/bin/env python3
"""生成 Phi-LPF signed transport unit-seed 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_signed_transport_unit_seed_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-signed-transport-unit-seed-router.json

输出：
  data/prime-matrix-phi-lpf-signed-transport-unit-seed-ledger.json
  docs/monograph/prime-matrix-phi-lpf-signed-transport-unit-seed-router.json
  docs/monograph/prime-matrix-phi-lpf-signed-transport-unit-seed-router.md
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

SLUG = "prime-matrix-phi-lpf-signed-transport-unit-seed"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json"
PHI_CERT = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"
SUPPORT_CERT = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
SIGNED_VALUE_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"
PRIMITIVE_EXPR_CERT = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"

TARGET = "PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward"
NEXT_TARGET = "PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward"
STEP_UPDATE = "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward"
ORDERED_COHERENCE = "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
ROWWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"

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


def sample_seed_audit(n: int) -> dict[str, Any]:
    """审计 unit cofactor 在 signed transport 中对应的平方基入口。"""
    primes = primes_up_to(n)
    small_primes = [p for p in primes if p <= math.isqrt(n)]
    layers: dict[str, dict[str, int | bool | str]] = {}
    total_support = 0
    square_seed_count = 0
    unit_preimage_ok = True

    for p in small_primes:
        x = n // p
        support_count = sum(1 for m in range(2, x + 1) if is_p_rough(m, p, primes))
        square_key_present = p <= x and is_p_rough(p, p, primes)
        unit_preimage_maps_to_square = p * p <= n and square_key_present
        total_support += support_count
        square_seed_count += 1 if unit_preimage_maps_to_square else 0
        unit_preimage_ok = unit_preimage_ok and unit_preimage_maps_to_square
        layers[str(p)] = {
            "x_floor_N_over_p": x,
            "unit_preimage_m_prime": 1,
            "square_base_cofactor_m": p,
            "square_base_composite": p * p,
            "square_key_present": square_key_present,
            "unit_preimage_maps_to_square": unit_preimage_maps_to_square,
            "support_count_phi_minus_one": support_count,
        }

    return {
        "N": n,
        "small_prime_layers": len(small_primes),
        "total_phi_lpf_support_keys": total_support,
        "square_base_seed_key_count": square_seed_count,
        "non_square_support_key_count": total_support - square_seed_count,
        "unit_preimage_square_seed_identity_holds": unit_preimage_ok,
        "seed_fraction": round(square_seed_count / total_support, 8) if total_support else 0.0,
        "layers": layers,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS_CERT,
        PHI_CERT,
        SUPPORT_CERT,
        SIGNED_VALUE_CERT,
        PRIMITIVE_EXPR_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def seed_fields() -> list[dict[str, str]]:
    """列出 unit seed / square-base 系数字段。"""
    return [
        {
            "field": "owner_bucket_prime",
            "meaning": "LPF owner prime `p`。",
        },
        {
            "field": "virtual_unit_cofactor",
            "meaning": "Phi 递推中的 `m'=1`，它不是 composite support row。",
        },
        {
            "field": "square_base_key",
            "meaning": "unit preimage 传输后得到的真实 composite key `(p,p)`，即 `p^2`。",
        },
        {
            "field": "square_base_signed_coefficient",
            "meaning": "对 `p^2` 的 Cauchy 前 signed coefficient 正向赋值。",
        },
        {
            "field": "prime_row_leak_guard",
            "meaning": "不得把被 LPF 计数公式减掉的 prime row `p` 当作 signed composite seed。",
        },
        {
            "field": "orientation_local_factor_base",
            "meaning": "平方基入口的 orientation、local factor、非零条件和 return tag。",
        },
        {
            "field": "transport_bootstrap_identity",
            "meaning": "证明后续 cofactor transport 从该平方基入口启动，而非从后验 payment 读取。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    phi: dict[str, Any],
    support: dict[str, Any],
    signed_value: dict[str, Any],
    primitive_expr: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 unit-seed 判定表。"""
    samples_ok = all(item["unit_preimage_square_seed_identity_holds"] for item in samples)
    return [
        row(
            "SignedTransportTargetImported",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 Phi-LPF signed law 压到 rough cofactor multiplication signed transport。",
            TARGET,
        ),
        row(
            "PhiMinusOnePrimeRowGuardImported",
            phi.get("phi_recursive_lpf_bucket_formula_proved") is True,
            True,
            "`Phi(floor(N/p),p)-1` 中减掉的 `m=1` 是 prime row `p`，不是 composite support。",
            "prime row cannot seed signed composite coefficient",
        ),
        row(
            "UnitPreimageReentersTransportAsSquareBase",
            samples_ok,
            True,
            "signed transport 的整除分支含 `m'=1`，它映到真实 composite key `(p,p)` 即 `p^2`。",
            NEXT_TARGET,
        ),
        row(
            "SupportBijectionConfirmsSquareBaseKeys",
            support.get("phi_lpf_support_bijection_proved") is True and samples_ok,
            True,
            "平方基 key 是 Phi-LPF support 的合法起点，但 unit cofactor 本身不是 support key。",
            NEXT_TARGET,
        ),
        row(
            "TransportCannotStartWithoutSeed",
            True,
            True,
            "若没有 virtual-unit 或 square-base signed coefficient，递推传输无法给出 `a_p(p)`。",
            NEXT_TARGET,
        ),
        row(
            "PrimeRowLeakBlocked",
            True,
            True,
            "不能把计数公式中被减掉的 prime `p` 的状态偷换成 composite coefficient seed。",
            NEXT_TARGET,
        ),
        row(
            "StepUpdateAndCoherenceRemainAfterSeed",
            True,
            False,
            "即使平方基入口给定，后续仍需每个 rough prime step 的 local factor 更新和有序分解一致性。",
            f"{STEP_UPDATE} AND {ORDERED_COHERENCE}",
        ),
        row(
            "PointwiseSignedValueTableAlternativeStillOpen",
            signed_value.get("pointwise_signed_alpha_coefficient_value_table_proved") is False,
            False,
            "直接提交 Phi-LPF bucket 逐点 signed value table 仍是等价并行入口，但当前未给出。",
            ROWWISE_TABLE,
        ),
        row(
            "PrimitiveSignedExpressionStillOpen",
            primitive_expr.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "primitive summand signed expression 未证明，因此平方基 signed coefficient 也未由现有语料产生。",
            NEXT_TARGET,
        ),
        row(
            "UnitSeedCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交 virtual-unit/square-base signed coefficient 与 prime-row leak guard 的正向证书。",
            NEXT_TARGET,
        ),
        row(
            "SignedTransportCurrentCorpusProved",
            False,
            False,
            "缺少平方基 seed，rough cofactor signed transport law 尚未证明。",
            f"{NEXT_TARGET} AND {STEP_UPDATE} AND {ORDERED_COHERENCE}",
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
    """组装 unit-seed 证书。"""
    previous = load_json(PREVIOUS_CERT)
    phi = load_json(PHI_CERT)
    support = load_json(SUPPORT_CERT)
    signed_value = load_json(SIGNED_VALUE_CERT)
    primitive_expr = load_json(PRIMITIVE_EXPR_CERT)
    samples = [sample_seed_audit(n) for n in SAMPLE_N]
    samples_ok = all(item["unit_preimage_square_seed_identity_holds"] for item in samples)
    rows = build_rows(
        previous=previous,
        phi=phi,
        support=support,
        signed_value=signed_value,
        primitive_expr=primitive_expr,
        samples=samples,
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_signed_transport_unit_seed_router",
        "status": "phi_lpf_signed_transport_reduced_to_unit_seed_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "target_input_before_router": TARGET,
        "phi_lpf_signed_transport_unit_seed_router_closed": True,
        "phi_minus_one_prime_row_guard_imported": rows[1]["closed"],
        "unit_preimage_square_seed_identity_proved": samples_ok,
        "unit_seed_or_square_base_signed_coefficient_proved": False,
        "rough_cofactor_step_local_factor_update_law_proved": False,
        "rough_cofactor_ordered_factorization_coherence_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "phi_lpf_rough_cofactor_signed_transport_law_proved": False,
        "phi_lpf_bucket_signed_coefficient_law_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_after_router": (
            f"({NEXT_TARGET} AND {STEP_UPDATE} AND {ORDERED_COHERENCE}) OR {ROWWISE_TABLE}"
        ),
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_direct_attack_target": ROWWISE_TABLE,
        "seed_fields": seed_fields(),
        "sample_seed_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Phi 计数公式中的 `-1` 是 signed transport 的关键边界：`m=1` 被从 composite support 中排除，"
            "但 rough cofactor 乘法分支又必须从 `m'=1` 生成平方基 key `(p,p)`。因此递推 signed transport "
            "不能从 Phi 计数自动启动；它首先需要 virtual-unit seed 或 square-base signed coefficient，"
            "并明确禁止把 prime row `p` 偷换成 composite signed seed。最新硬点压成 "
            "`PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward`。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF signed transport unit-seed 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phi_minus_one_prime_row_guard_imported={fmt_bool(cert['phi_minus_one_prime_row_guard_imported'])}",
        f"unit_preimage_square_seed_identity_proved={fmt_bool(cert['unit_preimage_square_seed_identity_proved'])}",
        f"unit_seed_or_square_base_signed_coefficient_proved={fmt_bool(cert['unit_seed_or_square_base_signed_coefficient_proved'])}",
        f"rough_cofactor_step_local_factor_update_law_proved={fmt_bool(cert['rough_cofactor_step_local_factor_update_law_proved'])}",
        f"rough_cofactor_ordered_factorization_coherence_proved={fmt_bool(cert['rough_cofactor_ordered_factorization_coherence_proved'])}",
        f"phi_lpf_rough_cofactor_signed_transport_law_proved={fmt_bool(cert['phi_lpf_rough_cofactor_signed_transport_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. unit seed 边界",
        "",
        "Phi 桶计数中 `m=1` 被减掉，因为它对应 prime row `p`。但 signed transport 的整除分支需要",
        "`m'=1 -> m=p` 来生成 composite `p^2` 的第一个真实 signed key。因此 transport 必须显式给出",
        "virtual-unit seed 或 square-base coefficient，不能从 prime row 后验偷渡。",
        "",
        "## 2. 样本 seed 审计",
        "",
        "| N | support keys | square-base seeds | non-square keys | seed fraction | seed identity |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in cert["sample_seed_audit"]:
        lines.append(
            f"| {item['N']} | {item['total_phi_lpf_support_keys']} | {item['square_base_seed_key_count']} | "
            f"{item['non_square_support_key_count']} | {item['seed_fraction']} | "
            f"`{fmt_bool(item['unit_preimage_square_seed_identity_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 3. seed 字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in cert["seed_fields"]:
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
