#!/usr/bin/env python3
"""归档 product-window 独立 signed defect 来源账本。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_independent_signed_defect_source_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-independent-signed-defect-source-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-independent-signed-defect-source-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-independent-signed-defect-source-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-independent-signed-defect-source-router.md

本证书承接 product-window exact-separation equivalence。它把最新硬点
IndependentSignedDefectEmissionBeforeProductWindowPushforward 接回既有
Phi-LPF bucket signed coefficient law 体系：若 defect 不是 survivor 后验定义，
则必须在 pushforward 前对每个 owner key `(p,m)` 给出 signed coefficient、
local factor、orientation、ExactUV/source key 和求和恒等式。无符号 LPF/Phi
support、owner 分桶、rough cofactor split、product-window phase identity 都不能
单独发射该 signed defect。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-independent-signed-defect-source"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

EXACT_EQUIV_JSON = DOCS / "prime-matrix-phi-lpf-product-window-exact-separation-equivalence-router.json"
BUCKET_TRANSPORT_JSON = DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json"
ROW_ORIGIN_BUCKET_JSON = DOCS / "prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-router.json"
BUCKET_STACK_JSON = DOCS / "prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-router.json"
MINIMAL_ROUTE_JSON = DOCS / "prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.json"
SUPPORT_STRIPPED_JSON = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
PRODUCT_PHASE_JSON = DOCS / "prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    EXACT_EQUIV_JSON,
    BUCKET_TRANSPORT_JSON,
    ROW_ORIGIN_BUCKET_JSON,
    BUCKET_STACK_JSON,
    MINIMAL_ROUTE_JSON,
    SUPPORT_STRIPPED_JSON,
    PRODUCT_PHASE_JSON,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]

OLD_PRIMARY_GATE = "IndependentSignedDefectEmissionBeforeProductWindowPushforward"
BUCKET_SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ROUGH_TRANSPORT = "PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward"
TRACE_GATE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients"
PDEC_GATE = "NonTautologicalProductWindowPDEC"
SQRT_GATE = "PointwiseSqrtPrimeInputCOne"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格转义。"""
    return str(value).replace("|", r"\|")


def required_payload_fields() -> list[dict[str, str]]:
    """列出独立 signed defect 的最小字段。"""
    return [
        {
            "field": "owner_key",
            "meaning": "产品窗口中的 LPF owner key `(p,m)`，满足 `pm=kP+r` 且 `m` 为 `p`-rough。",
        },
        {
            "field": "signed_coefficient",
            "meaning": "在读取 survivor 前正向给出的系数 `a_{p,m}`；不能由 `1_S` 或 `1_O-1_*` 后验定义。",
        },
        {
            "field": "local_factor",
            "meaning": "与 LPF/Phi 递推、rough cofactor 乘法、截断端点兼容的局部因子。",
        },
        {
            "field": "orientation_and_branch",
            "meaning": "sign/orientation、alpha-delta side、branch key 的传输规则。",
        },
        {
            "field": "source_identity",
            "meaning": "pre-Cauchy/source-domain 的同 formal unit 求和恒等式，不经过 payment skeleton 反推。",
        },
        {
            "field": "pushforward_identity",
            "meaning": "推前到 product-window row phase 后给出目标 signed defect 的等式。",
        },
        {
            "field": "admissible_norms",
            "meaning": "若走 trace/Type-II 路线，需要系数范数、导子、factorability、区间范围可被外部 theorem 接受。",
        },
        {
            "field": "return_tag",
            "meaning": "若字段缺失、冲突、后验依赖或退化为 survivor 等价式，必须进入 PDEC/SAE/terminal 命名回流。",
        },
    ]


def source_gate_rows(
    exact_equiv: dict[str, Any],
    bucket_transport: dict[str, Any],
    row_origin_bucket: dict[str, Any],
    bucket_stack: dict[str, Any],
    support_stripped: dict[str, Any],
) -> list[dict[str, Any]]:
    """列出独立 signed defect 的候选来源与状态。"""
    return [
        {
            "source": "survivor-defined defect",
            "closed": True,
            "proved": False,
            "status": "rejected as circular",
            "reason": "exact-equivalence 证书已证明 owner-complete defect = -survivor measure。",
            "remaining": OLD_PRIMARY_GATE,
        },
        {
            "source": "unsigned LPF/Phi support and capacity",
            "closed": True,
            "proved": False,
            "status": "cannot emit sign",
            "reason": "support stripping 只关闭无符号支撑/容量；signed coefficient、local factor、orientation 未给出。",
            "remaining": BUCKET_SIGNED_LAW,
        },
        {
            "source": "row-origin fixed-point table",
            "closed": True,
            "proved": False,
            "status": "fixed-point self-certification rejected",
            "reason": "row-origin/bucket-law 同步把 hardpoint 接回 bucket signed law。",
            "remaining": row_origin_bucket.get("next_primary_attack_target", BUCKET_SIGNED_LAW),
        },
        {
            "source": "rough cofactor transport",
            "closed": True,
            "proved": False,
            "status": "formal split closed, signed multiplier open",
            "reason": "bucket transport 已闭合 cofactor split，但没有 `a_p(qm)` 的 signed transport law。",
            "remaining": bucket_transport.get("hardpoint_after_router", ROUGH_TRANSPORT),
        },
        {
            "source": "pointwise Phi-LPF signed table",
            "closed": False,
            "proved": False,
            "status": "sufficient but not submitted",
            "reason": "逐点表若给出可直接作为独立 defect 来源；当前语料标记为 open。",
            "remaining": POINTWISE_TABLE,
        },
        {
            "source": "constructor bucket transport stack",
            "closed": True,
            "proved": False,
            "status": "rebase imported, side gates still open",
            "reason": "bucket stack 需要 edge multiplier/source 三原子、signed survival、row-mass/no-heavy-row 等合取门。",
            "remaining": bucket_stack.get("latest_retained_basis_after_router", ROUGH_TRANSPORT),
        },
        {
            "source": "completed trace / Type-II bridge",
            "closed": False,
            "proved": False,
            "status": "requires signed coefficients first",
            "reason": "没有 independent signed coefficients 时，外部 trace/Kloosterman theorem 无对象可作用。",
            "remaining": TRACE_GATE,
        },
        {
            "source": "non-tautological product-window PDEC",
            "closed": False,
            "proved": False,
            "status": "parallel escape, not materialized",
            "reason": "必须不是两点 Fourier tautology 或 survivor 等价式；需要同 formal unit 缺陷能量阈值。",
            "remaining": PDEC_GATE,
        },
        {
            "source": "pointwise sqrt prime input",
            "closed": False,
            "proved": False,
            "status": "external distribution route",
            "reason": "若能输入 `C=1` sqrt 级点态素数定理，可绕过 signed defect；当前未有。",
            "remaining": SQRT_GATE,
        },
    ]


def finite_ambiguity_rows(exact_equiv: dict[str, Any]) -> list[dict[str, Any]]:
    """从 exact-equivalence 审计抽取无符号支撑的符号歧义规模。"""
    rows = []
    for row in exact_equiv.get("finite_equivalence_audit", []):
        owner_count = int(row["owner_count"])
        survivor_count = int(row["survivor_count"])
        rows.append(
            {
                "P": row["P"],
                "k": row["k"],
                "owner_count": owner_count,
                "survivor_count": survivor_count,
                "unsigned_owner_support_keys": owner_count,
                "same_support_binary_sign_shadow_bits": owner_count,
                "same_support_binary_sign_shadow_log10": round(owner_count * 0.3010299956639812, 6),
                "survivor_defined_defect_available_only_after_partition": survivor_count > 0,
                "unsigned_support_determines_signed_defect": False,
            }
        )
    return rows


def external_rows() -> list[dict[str, Any]]:
    """记录外部 theorem 对本层的必要对象条件。"""
    return [
        {
            "input": "Fouvry--Kowalski--Michel--Sawin trace-function bilinear forms",
            "url": "https://arxiv.org/abs/2511.09459",
            "needed_project_object": "l-adic trace family plus admissible coefficient norms from signed defect coefficients",
            "current_status": "no independent signed coefficient table, so not directly usable",
            "usable_now": False,
        },
        {
            "input": "Pascadi / DI-BFI / Kloosterman Type-II route",
            "url": "https://arxiv.org/abs/2511.08445",
            "needed_project_object": "completed inverse-variable Kloosterman family with factorable signed coefficients",
            "current_status": "current product phase is additive and defect coefficients are not emitted before pushforward",
            "usable_now": False,
        },
        {
            "input": "Pointwise short-interval prime route",
            "url": "https://arxiv.org/abs/2405.20552",
            "needed_project_object": "theta((kP,(k+1)P))>0 at x≈P^2, length P, constant C<=1",
            "current_status": "known frontier remains above the exact sqrt row scale or average-type",
            "usable_now": False,
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    exact_equiv = load_json(EXACT_EQUIV_JSON)
    bucket_transport = load_json(BUCKET_TRANSPORT_JSON)
    row_origin_bucket = load_json(ROW_ORIGIN_BUCKET_JSON)
    bucket_stack = load_json(BUCKET_STACK_JSON)
    minimal_route = load_json(MINIMAL_ROUTE_JSON)
    support_stripped = load_json(SUPPORT_STRIPPED_JSON)
    product_phase = load_json(PRODUCT_PHASE_JSON)

    gate_rows = source_gate_rows(
        exact_equiv,
        bucket_transport,
        row_origin_bucket,
        bucket_stack,
        support_stripped,
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_independent_signed_defect_source_router",
        "status": "independent_signed_defect_rebased_to_phi_lpf_bucket_signed_law",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "product_window_exact_equivalence_imported": exact_equiv.get(
            "standalone_exact_separation_rejected_as_noncircular_primary_gate"
        )
        is True,
        "source_keyed_product_phase_imported": product_phase.get("source_keyed_owner_phase_emission_formula_closed")
        is True,
        "survivor_defined_defect_rejected_as_circular": True,
        "unsigned_lpf_phi_support_cannot_emit_independent_signed_defect": True,
        "independent_signed_defect_source_equivalent_to_phi_lpf_bucket_signed_law": True,
        "pointwise_signed_table_sufficient_but_open": True,
        "rough_cofactor_signed_transport_sufficient_but_open": True,
        "completed_trace_bridge_requires_signed_defect_first": True,
        "non_tautological_product_window_pdec_proved": False,
        "row_column_unconditional_closed": False,
        "required_payload_fields": required_payload_fields(),
        "source_gate_rows": gate_rows,
        "finite_sign_ambiguity_audit": finite_ambiguity_rows(exact_equiv),
        "external_applicability_rows": external_rows(),
        "old_gate_rebased": OLD_PRIMARY_GATE,
        "selected_next_primary_gate": BUCKET_SIGNED_LAW,
        "selected_parallel_pointwise_gate": POINTWISE_TABLE,
        "selected_parallel_transport_gate": ROUGH_TRANSPORT,
        "selected_parallel_trace_gate": TRACE_GATE,
        "selected_parallel_pdec_gate": PDEC_GATE,
        "selected_parallel_distribution_gate": SQRT_GATE,
        "minimal_route_context_status": minimal_route.get("status"),
        "support_stripped_context_status": support_stripped.get("status"),
        "plain_conclusion": (
            "Product-window 的独立 signed defect 不能来自 survivor 后验定义，也不能由无符号 "
            "LPF/Phi support、owner 分桶、rough cofactor split 或 product phase identity 自动产生。"
            "若不输入点态 sqrt 素数定理或非平凡 PDEC，则它等价于提交一个真正的 "
            "Phi-LPF bucket signed coefficient law：在 pushforward 前对每个 `(p,m)` 给出 "
            "signed coefficient、local factor、orientation/source key 与 prepushforward sum identity。"
            "因此最新主攻从抽象 IndependentSignedDefectEmission 精确 rebased 到 "
            "PhiLPFBucketSignedCoefficientLawBeforePushforward，并行替代为逐点 signed table、"
            "rough-cofactor signed transport 或带 signed defect 的 completed trace/Type-II bridge。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window independent signed defect 来源账本",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"product_window_exact_equivalence_imported={fmt_bool(cert['product_window_exact_equivalence_imported'])}",
        f"survivor_defined_defect_rejected_as_circular={fmt_bool(cert['survivor_defined_defect_rejected_as_circular'])}",
        f"unsigned_lpf_phi_support_cannot_emit_independent_signed_defect={fmt_bool(cert['unsigned_lpf_phi_support_cannot_emit_independent_signed_defect'])}",
        f"independent_signed_defect_source_equivalent_to_phi_lpf_bucket_signed_law={fmt_bool(cert['independent_signed_defect_source_equivalent_to_phi_lpf_bucket_signed_law'])}",
        f"completed_trace_bridge_requires_signed_defect_first={fmt_bool(cert['completed_trace_bridge_requires_signed_defect_first'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 必要 payload 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for row in cert["required_payload_fields"]:
        lines.append(f"| `{cell(row['field'])}` | {cell(row['meaning'])} |")

    lines.extend(
        [
            "",
            "## 2. 来源门状态",
            "",
            "| source | closed | proved | status | reason | remaining |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["source_gate_rows"]:
        lines.append(
            f"| {cell(row['source'])} | `{fmt_bool(row['closed'])}` | `{fmt_bool(row['proved'])}` | "
            f"{cell(row['status'])} | {cell(row['reason'])} | `{cell(row['remaining'])}` |"
        )

    lines.extend(
        [
            "",
            "## 3. 有限行 sign ambiguity 审计",
            "",
            "| P | k | owner keys | survivors | sign-shadow bits | log10 sign-shadow | unsigned determines signed defect |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in cert["finite_sign_ambiguity_audit"]:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['owner_count']} | {row['survivor_count']} | "
            f"{row['same_support_binary_sign_shadow_bits']} | {row['same_support_binary_sign_shadow_log10']} | "
            f"`{fmt_bool(row['unsigned_support_determines_signed_defect'])}` |"
        )

    lines.extend(
        [
            "",
            "## 4. 外部 theorem 对象条件",
            "",
            "| input | usable now | needed project object | current status | url |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_applicability_rows"]:
        lines.append(
            f"| {cell(row['input'])} | `{fmt_bool(row['usable_now'])}` | "
            f"{cell(row['needed_project_object'])} | {cell(row['current_status'])} | {row['url']} |"
        )

    lines.extend(
        [
            "",
            "## 5. 下一手",
            "",
            "```text",
            f"old_gate_rebased={cert['old_gate_rebased']}",
            f"selected_next_primary_gate={cert['selected_next_primary_gate']}",
            f"selected_parallel_pointwise_gate={cert['selected_parallel_pointwise_gate']}",
            f"selected_parallel_transport_gate={cert['selected_parallel_transport_gate']}",
            f"selected_parallel_trace_gate={cert['selected_parallel_trace_gate']}",
            f"selected_parallel_pdec_gate={cert['selected_parallel_pdec_gate']}",
            f"selected_parallel_distribution_gate={cert['selected_parallel_distribution_gate']}",
            "```",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(
        "independent_signed_defect_source_equivalent_to_phi_lpf_bucket_signed_law="
        f"{fmt_bool(cert['independent_signed_defect_source_equivalent_to_phi_lpf_bucket_signed_law'])}"
    )
    print(
        "unsigned_lpf_phi_support_cannot_emit_independent_signed_defect="
        f"{fmt_bool(cert['unsigned_lpf_phi_support_cannot_emit_independent_signed_defect'])}"
    )
    print(f"selected_next_primary_gate={cert['selected_next_primary_gate']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
