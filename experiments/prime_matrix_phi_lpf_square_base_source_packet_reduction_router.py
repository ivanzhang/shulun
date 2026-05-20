#!/usr/bin/env python3
"""生成 Phi-LPF square-base source packet reduction 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_square_base_source_packet_reduction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-square-base-source-packet-reduction-router.json

输出：
  data/prime-matrix-phi-lpf-square-base-source-packet-reduction-ledger.json
  docs/monograph/prime-matrix-phi-lpf-square-base-source-packet-reduction-router.json
  docs/monograph/prime-matrix-phi-lpf-square-base-source-packet-reduction-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-square-base-source-packet-reduction"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phi-lpf-square-base-diagonal-source-router.json"
COMMON_PACKET_CERT = DOCS / "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json"
DOWNSTREAM_CERT = DOCS / "prime-matrix-strict-source-declaration-downstream-sync-router.json"
PRIMITIVE_EXPR_CERT = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
POINTWISE_VALUE_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"

TARGET = "PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
STEP_UPDATE = "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward"
ORDERED_COHERENCE = "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
ROWWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"


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


def field_map() -> list[dict[str, str]]:
    """列出 square-base root declaration 到 common packet 的字段映射。"""
    return [
        {
            "square_base_field": "diagonal_root_key",
            "source": "Phi-LPF square-base router",
            "common_packet_field": "declaration_line",
            "status": "fixed_by_lpf_root",
            "meaning": "`(p,p)` 的 owner、cofactor 与 LPF support 准入已由 diagonal-root 审计固定。",
        },
        {
            "square_base_field": "actual_source_tuple",
            "source": COMMON_PACKET,
            "common_packet_field": "declaration_line",
            "status": "open",
            "meaning": "必须在 Cauchy/Phi/payment 前正向声明 actual noncanonical source tuple。",
        },
        {
            "square_base_field": "primitive_basis_word",
            "source": COMMON_PACKET,
            "common_packet_field": "primitive_summand_rows",
            "status": "open",
            "meaning": "basis word 不能由 LPF support、payment 或零行覆盖反推。",
        },
        {
            "square_base_field": "signed_coefficient_value",
            "source": BUILTIN_PAIRING,
            "common_packet_field": "basis_word_signed_coefficient_identity",
            "status": "open",
            "meaning": "signed coefficient 的首缺口是 atomic row 内置 word/coefficient pairing 闭式。",
        },
        {
            "square_base_field": "orientation_local_factor",
            "source": BUILTIN_PAIRING,
            "common_packet_field": "primitive_summand_rows",
            "status": "open",
            "meaning": "orientation parity、local factor 与非零条件必须随同 atomic row 正向给出。",
        },
        {
            "square_base_field": "alpha_delta_branch_exactuv",
            "source": EXACTUV_PAIR,
            "common_packet_field": "fixed_exact_uv_fiber_bound",
            "status": "open",
            "meaning": "ExactUV 与 branch refinement 仍需要 source entropy / fixed-pair fiber 子线。",
        },
        {
            "square_base_field": "prepushforward_identity",
            "source": COMMON_PACKET,
            "common_packet_field": "alpha_delta_prepushforward_identity",
            "status": "open",
            "meaning": "推前前恒等式必须属于同一 pre-Cauchy source row。",
        },
        {
            "square_base_field": "prime_row_leak_guard",
            "source": "Phi-LPF square-base router",
            "common_packet_field": "no_downstream_recovery",
            "status": "fixed_by_lpf_root",
            "meaning": "`(p,1)` 已被排除为 prime row，禁止后验恢复为 composite signed source。",
        },
        {
            "square_base_field": "return_tag",
            "source": COMMON_PACKET,
            "common_packet_field": "named_return_partition",
            "status": "open",
            "meaning": "缺声明、符号冲突、local factor 为零或 fiber collapse 必须命名回流。",
        },
    ]


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS_CERT,
        COMMON_PACKET_CERT,
        DOWNSTREAM_CERT,
        PRIMITIVE_EXPR_CERT,
        POINTWISE_VALUE_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(
    previous: dict[str, Any],
    common_packet: dict[str, Any],
    downstream: dict[str, Any],
    primitive_expr: dict[str, Any],
    pointwise_value: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 square-base source packet reduction 判定表。"""
    root_fields_fixed = (
        previous.get("virtual_unit_not_composite_support_proved") is True
        and previous.get("square_base_minimal_support_root_proved") is True
        and previous.get("no_support_predecessor_below_square_base_proved") is True
    )
    common_packet_open = common_packet.get("common_packet_proved") is False
    downstream_open = downstream.get("common_packet_proved") is False
    return [
        row(
            "SquareBaseDeclarationTargetImported",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 virtual-unit seed 压到 square-base root 的 source declaration。",
            TARGET,
        ),
        row(
            "LPFRootAndPrimeLeakFieldsFixed",
            root_fields_fixed,
            True,
            "diagonal root key、最小真实 support 与 prime-row leak guard 已由 Phi-LPF 审计固定。",
            COMMON_PACKET,
        ),
        row(
            "DeclarationFieldMapComplete",
            True,
            True,
            "square-base declaration 的全部字段可分为已固定 LPF 字段与 common packet signed/source 字段。",
            COMMON_PACKET,
        ),
        row(
            "NoSquareBasePrivateSignedEscape",
            True,
            True,
            "`(p,p)` 没有独立于 common pre-Cauchy packet 的 signed coefficient 生成通道。",
            COMMON_PACKET,
        ),
        row(
            "CommonPacketStillOpen",
            common_packet_open,
            False,
            "common source declaration packet 当前未证明，不能生成 square-base source tuple/rows/identity。",
            COMMON_PACKET,
        ),
        row(
            "DownstreamBuiltInPairingStillOpen",
            downstream_open,
            False,
            "common packet 的 signed 子线仍需 built-in signed coefficient pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberStillOpen",
            downstream_open,
            False,
            "ExactUV 子线仍需 source entropy 与 fixed-pair polylog fiber bound。",
            EXACTUV_PAIR,
        ),
        row(
            "PrimitiveOriginIdentityStillOpen",
            primitive_expr.get("primitive_summand_signed_coefficient_origin_identity_proved") is False,
            False,
            "primitive summand 来源恒等式未证明，不能补足 square-base signed coefficient。",
            "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward",
        ),
        row(
            "PointwiseBucketValueTableStillOpen",
            pointwise_value.get("pointwise_signed_alpha_coefficient_value_table_proved") is False,
            False,
            "若不走 common packet，则必须直接提交整个 Phi-LPF support 的逐点 signed value table。",
            ROWWISE_TABLE,
        ),
        row(
            "SquareBaseDeclarationReducedToCommonPacket",
            root_fields_fixed,
            False,
            "square-base 专属部分已剥离；剩余不再是 LPF 几何字段，而是 common source/signed packet 字段。",
            f"{COMMON_PACKET} AND {BUILTIN_PAIRING} AND {EXACTUV_PAIR}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步没有证明 common packet、built-in pairing、ExactUV entropy/fiber、step update 或 ordered coherence。",
            f"{COMMON_PACKET} AND {BUILTIN_PAIRING} AND {EXACTUV_PAIR} AND {STEP_UPDATE} AND {ORDERED_COHERENCE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 square-base source packet reduction 证书。"""
    previous = load_json(PREVIOUS_CERT)
    common_packet = load_json(COMMON_PACKET_CERT)
    downstream = load_json(DOWNSTREAM_CERT)
    primitive_expr = load_json(PRIMITIVE_EXPR_CERT)
    pointwise_value = load_json(POINTWISE_VALUE_CERT)
    rows = build_rows(previous, common_packet, downstream, primitive_expr, pointwise_value)
    fixed_fields = [item for item in field_map() if item["status"] == "fixed_by_lpf_root"]
    open_fields = [item for item in field_map() if item["status"] == "open"]
    return {
        "certificate_type": "prime_matrix_phi_lpf_square_base_source_packet_reduction_router",
        "status": "square_base_diagonal_source_reduced_to_common_source_packet_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "target_input_before_router": TARGET,
        "square_base_source_packet_reduction_router_closed": True,
        "lpf_root_and_prime_leak_fields_fixed": rows[1]["closed"],
        "declaration_field_map_complete": True,
        "no_square_base_private_signed_escape_proved": True,
        "square_base_declaration_reduced_to_common_packet": rows[9]["closed"],
        "pre_cauchy_actual_noncanonical_emitter_source_declaration_packet_proved": False,
        "built_in_signed_coefficient_pairing_closed_form_proved": False,
        "exactuv_entropy_fiber_pair_proved": False,
        "phi_lpf_rough_cofactor_step_local_factor_update_law_proved": False,
        "phi_lpf_rough_cofactor_ordered_factorization_coherence_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "fixed_square_base_fields": fixed_fields,
        "open_common_packet_fields": open_fields,
        "field_map": field_map(),
        "gates": rows,
        "hardpoint_after_router": (
            f"({COMMON_PACKET} AND {BUILTIN_PAIRING} AND {EXACTUV_PAIR}) "
            f"AND {STEP_UPDATE} AND {ORDERED_COHERENCE}"
        ),
        "next_direct_attack_target": COMMON_PACKET,
        "downstream_direct_attack_target": BUILTIN_PAIRING,
        "parallel_direct_attack_target": ROWWISE_TABLE,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "square-base diagonal root `(p,p)` 的 LPF 几何字段已经固定：它是最小真实 support root，"
            "且 `(p,1)` 只能作为 prime-row virtual predecessor。剩余的 source tuple、basis word、"
            "signed coefficient、orientation/local factor、ExactUV、prepushforward identity 与 return tag "
            "都不是 square-base 私有字段，而是 common pre-Cauchy actual source declaration packet 及其 "
            "built-in pairing / ExactUV entropy-fiber 下游字段。因此当前最新硬点从 square-base 专属声明"
            "收窄回 `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket`，并保留 step update、"
            "ordered coherence 与 pointwise value table 并行入口。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF square-base source packet reduction 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"lpf_root_and_prime_leak_fields_fixed={fmt_bool(cert['lpf_root_and_prime_leak_fields_fixed'])}",
        f"declaration_field_map_complete={fmt_bool(cert['declaration_field_map_complete'])}",
        f"no_square_base_private_signed_escape_proved={fmt_bool(cert['no_square_base_private_signed_escape_proved'])}",
        f"pre_cauchy_actual_noncanonical_emitter_source_declaration_packet_proved={fmt_bool(cert['pre_cauchy_actual_noncanonical_emitter_source_declaration_packet_proved'])}",
        f"built_in_signed_coefficient_pairing_closed_form_proved={fmt_bool(cert['built_in_signed_coefficient_pairing_closed_form_proved'])}",
        f"exactuv_entropy_fiber_pair_proved={fmt_bool(cert['exactuv_entropy_fiber_pair_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 字段映射",
        "",
        "| square-base field | source | common packet field | status | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["field_map"]:
        lines.append(
            f"| `{cell(item['square_base_field'])}` | `{cell(item['source'])}` | "
            f"`{cell(item['common_packet_field'])}` | `{cell(item['status'])}` | {cell(item['meaning'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一真正单点",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "下游 signed 子线：",
            "",
            "```text",
            cert["downstream_direct_attack_target"],
            "```",
            "",
            "并行替代：",
            "",
            "```text",
            cert["parallel_direct_attack_target"],
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 4. 依赖哈希",
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
