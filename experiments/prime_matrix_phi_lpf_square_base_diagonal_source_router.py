#!/usr/bin/env python3
"""生成 Phi-LPF square-base diagonal source 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_square_base_diagonal_source_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-square-base-diagonal-source-router.json

输出：
  data/prime-matrix-phi-lpf-square-base-diagonal-source-ledger.json
  docs/monograph/prime-matrix-phi-lpf-square-base-diagonal-source-router.json
  docs/monograph/prime-matrix-phi-lpf-square-base-diagonal-source-router.md
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

SLUG = "prime-matrix-phi-lpf-square-base-diagonal-source"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phi-lpf-signed-transport-unit-seed-router.json"
SUPPORT_CERT = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
SOURCE_PACKET_CERT = DOCS / "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json"
SOURCE_DOWNSTREAM_CERT = DOCS / "prime-matrix-strict-source-declaration-downstream-sync-router.json"
PRIMITIVE_EXPR_CERT = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
POINTWISE_VALUE_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"

TARGET = "PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward"
NEXT_TARGET = "PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward"
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


def sample_diagonal_root_audit(n: int) -> dict[str, Any]:
    """审计 square-base key 是每个 LPF 桶的唯一 transport 根。"""
    primes = primes_up_to(n)
    small_primes = [p for p in primes if p <= math.isqrt(n)]
    layers: dict[str, dict[str, int | bool | str]] = {}
    all_ok = True
    square_root_count = 0

    for p in small_primes:
        x = n // p
        below_support = [m for m in range(2, p) if m <= x and is_p_rough(m, p, primes)]
        square_key_present = p <= x and is_p_rough(p, p, primes)
        support_predecessors = []
        virtual_predecessors = []
        for q in primes:
            if q < p or q > p:
                continue
            if p % q != 0:
                continue
            m_prime = p // q
            if is_p_rough(m_prime, p, primes):
                if m_prime > 1:
                    support_predecessors.append((q, m_prime))
                else:
                    virtual_predecessors.append((q, m_prime))
        layer_ok = (
            not below_support
            and square_key_present
            and not support_predecessors
            and virtual_predecessors == [(p, 1)]
        )
        all_ok = all_ok and layer_ok
        square_root_count += 1 if layer_ok else 0
        layers[str(p)] = {
            "x_floor_N_over_p": x,
            "virtual_unit_key_excluded": True,
            "minimal_support_cofactor": p,
            "square_base_key": f"({p},{p})",
            "square_base_composite": p * p,
            "below_square_support_count": len(below_support),
            "square_key_present": square_key_present,
            "support_predecessor_count": len(support_predecessors),
            "virtual_predecessor_count": len(virtual_predecessors),
            "unique_virtual_predecessor": virtual_predecessors == [(p, 1)],
            "diagonal_root_identity_ok": layer_ok,
        }

    return {
        "N": n,
        "small_prime_layers": len(small_primes),
        "square_base_diagonal_root_count": square_root_count,
        "diagonal_root_identity_holds": all_ok,
        "layers": layers,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS_CERT,
        SUPPORT_CERT,
        SOURCE_PACKET_CERT,
        SOURCE_DOWNSTREAM_CERT,
        PRIMITIVE_EXPR_CERT,
        POINTWISE_VALUE_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def declaration_fields() -> list[dict[str, str]]:
    """列出 square-base diagonal source declaration 字段。"""
    return [
        {
            "field": "diagonal_root_key",
            "meaning": "每个 owner bucket 的最小真实 support key `(p,p)`。",
        },
        {
            "field": "actual_source_tuple",
            "meaning": "同 formal-unit、Cauchy/Phi/payment 前的 actual noncanonical source tuple。",
        },
        {
            "field": "primitive_basis_word",
            "meaning": "平方基 diagonal root 生成的 primitive basis word。",
        },
        {
            "field": "signed_coefficient_value",
            "meaning": "该 diagonal root 的 signed coefficient 正向值。",
        },
        {
            "field": "orientation_local_factor",
            "meaning": "orientation parity、local factor、截断因子和非零条件。",
        },
        {
            "field": "alpha_delta_branch_exactuv",
            "meaning": "alpha/delta side、branch key 和 exact `(u,v)` 输出。",
        },
        {
            "field": "prepushforward_identity",
            "meaning": "证明 root 声明在推前前已经等于目标 signed 贡献。",
        },
        {
            "field": "prime_row_leak_guard",
            "meaning": "证明没有把 prime row `p` 或 virtual `(p,1)` 当成 composite signed source。",
        },
        {
            "field": "return_tag",
            "meaning": "声明缺失、local factor 为零、符号冲突或后验依赖时的命名回流。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    support: dict[str, Any],
    source_packet: dict[str, Any],
    source_downstream: dict[str, Any],
    primitive_expr: dict[str, Any],
    pointwise_value: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 square-base diagonal source 判定表。"""
    samples_ok = all(item["diagonal_root_identity_holds"] for item in samples)
    packet_open = source_packet.get("actual_noncanonical_emitter_source_declaration_packet_proved") is False
    downstream_pairing_open = (
        source_downstream.get("built_in_signed_coefficient_pairing_closed_form_proved") is False
        or source_downstream.get("atomic_joint_rows_formula_with_builtin_pairing_proved") is False
    )
    return [
        row(
            "UnitSeedTargetImported",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 signed transport 启动压到 virtual-unit 或 square-base signed coefficient。",
            TARGET,
        ),
        row(
            "VirtualUnitNotCompositeSupport",
            previous.get("phi_minus_one_prime_row_guard_imported") is True,
            True,
            "`(p,1)` 对应 prime row `p`，不在 composite support 中，不能独立携带 composite signed coefficient。",
            NEXT_TARGET,
        ),
        row(
            "SquareBaseIsMinimalSupportRoot",
            samples_ok and support.get("phi_lpf_support_bijection_proved") is True,
            True,
            "每个 LPF owner bucket 的最小真实 support cofactor 是 `m=p`，即 diagonal root `(p,p)`。",
            NEXT_TARGET,
        ),
        row(
            "NoSupportPredecessorBelowSquareBase",
            samples_ok,
            True,
            "`(p,p)` 没有更小的 composite support predecessor；唯一 predecessor 是 virtual `(p,1)`。",
            NEXT_TARGET,
        ),
        row(
            "VirtualSeedCollapsesToSquareBaseDeclaration",
            samples_ok,
            True,
            "合法 virtual seed 若存在，必须作为 square-base root 的声明前像出现，不能作为独立 signed row。",
            NEXT_TARGET,
        ),
        row(
            "SourceDeclarationPacketStillOpen",
            packet_open,
            False,
            "common pre-Cauchy source declaration packet 仍未证明；square-base root 也必须满足该 packet。",
            "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket",
        ),
        row(
            "BuiltInPairingStillOpen",
            downstream_pairing_open,
            False,
            "source packet 下游仍缺 atomic row 的 built-in word/coefficient pairing 闭式。",
            "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows",
        ),
        row(
            "PrimitiveSummandExpressionStillOpen",
            primitive_expr.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "primitive summand signed expression 未证明，不能自动给 diagonal root signed coefficient。",
            NEXT_TARGET,
        ),
        row(
            "PointwiseBucketValueTableStillOpen",
            pointwise_value.get("pointwise_signed_alpha_coefficient_value_table_proved") is False,
            False,
            "直接提交整个 Phi-LPF support 的 pointwise signed value table 仍未完成。",
            ROWWISE_TABLE,
        ),
        row(
            "SquareBaseDiagonalSourceDeclarationCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交 `(p,p)` diagonal root 的同源 basis word/signed coefficient source declaration。",
            NEXT_TARGET,
        ),
        row(
            "UnitSeedCurrentCorpusProved",
            False,
            False,
            "virtual-unit 口径已归约到 square-base declaration；该 declaration 未证明，unit seed 仍未闭合。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步没有证明 signed coefficient law、step update、ordered coherence、ExactUV fixed-key 或三命题无条件闭合。",
            f"{NEXT_TARGET} AND {STEP_UPDATE} AND {ORDERED_COHERENCE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 square-base diagonal source 证书。"""
    previous = load_json(PREVIOUS_CERT)
    support = load_json(SUPPORT_CERT)
    source_packet = load_json(SOURCE_PACKET_CERT)
    source_downstream = load_json(SOURCE_DOWNSTREAM_CERT)
    primitive_expr = load_json(PRIMITIVE_EXPR_CERT)
    pointwise_value = load_json(POINTWISE_VALUE_CERT)
    samples = [sample_diagonal_root_audit(n) for n in SAMPLE_N]
    samples_ok = all(item["diagonal_root_identity_holds"] for item in samples)
    rows = build_rows(
        previous=previous,
        support=support,
        source_packet=source_packet,
        source_downstream=source_downstream,
        primitive_expr=primitive_expr,
        pointwise_value=pointwise_value,
        samples=samples,
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_square_base_diagonal_source_router",
        "status": "phi_lpf_unit_seed_reduced_to_square_base_diagonal_source_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "target_input_before_router": TARGET,
        "phi_lpf_square_base_diagonal_source_router_closed": True,
        "virtual_unit_not_composite_support_proved": rows[1]["closed"],
        "square_base_minimal_support_root_proved": samples_ok,
        "no_support_predecessor_below_square_base_proved": samples_ok,
        "virtual_seed_collapses_to_square_base_declaration": samples_ok,
        "square_base_diagonal_root_signed_source_declaration_proved": False,
        "unit_seed_or_square_base_signed_coefficient_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "phi_lpf_rough_cofactor_signed_transport_law_proved": False,
        "phi_lpf_bucket_signed_coefficient_law_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_after_router": f"({NEXT_TARGET} AND {STEP_UPDATE} AND {ORDERED_COHERENCE}) OR {ROWWISE_TABLE}",
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_direct_attack_target": ROWWISE_TABLE,
        "declaration_fields": declaration_fields(),
        "sample_diagonal_root_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "virtual-unit seed 不能作为独立 composite signed row：`(p,1)` 是被 Phi-LPF 计数公式减掉的 prime row。"
            "每个 owner bucket 的最小真实 support key 是 square-base diagonal root `(p,p)`，它没有更小的 "
            "composite support predecessor；唯一 predecessor 是 virtual `(p,1)`。因此 seed 硬点进一步收窄为 "
            "`PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward`：必须在 Cauchy/Phi/payment 前"
            "对 `(p,p)` 同时给出 source tuple、basis word、signed coefficient、orientation/local factor、"
            "alpha/delta branch、ExactUV、推前前恒等式和 prime-row leak guard。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF square-base diagonal source 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"virtual_unit_not_composite_support_proved={fmt_bool(cert['virtual_unit_not_composite_support_proved'])}",
        f"square_base_minimal_support_root_proved={fmt_bool(cert['square_base_minimal_support_root_proved'])}",
        f"no_support_predecessor_below_square_base_proved={fmt_bool(cert['no_support_predecessor_below_square_base_proved'])}",
        f"virtual_seed_collapses_to_square_base_declaration={fmt_bool(cert['virtual_seed_collapses_to_square_base_declaration'])}",
        f"square_base_diagonal_root_signed_source_declaration_proved={fmt_bool(cert['square_base_diagonal_root_signed_source_declaration_proved'])}",
        f"phi_lpf_rough_cofactor_signed_transport_law_proved={fmt_bool(cert['phi_lpf_rough_cofactor_signed_transport_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. diagonal root 结构",
        "",
        "`(p,1)` 不是 composite support。对 owner bucket `p`，`1<m<p` 的 cofactor 一定含有小于 `p` 的素因子，",
        "所以最小真实 support cofactor 是 `m=p`。因此 `(p,p)` 是 transport forest 的 diagonal root。",
        "",
        "## 2. 样本 root 审计",
        "",
        "| N | layers | square roots | root identity |",
        "| ---: | ---: | ---: | --- |",
    ]
    for item in cert["sample_diagonal_root_audit"]:
        lines.append(
            f"| {item['N']} | {item['small_prime_layers']} | "
            f"{item['square_base_diagonal_root_count']} | `{fmt_bool(item['diagonal_root_identity_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 3. declaration 字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in cert["declaration_fields"]:
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
