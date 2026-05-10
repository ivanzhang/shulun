#!/usr/bin/env python3
"""生成 strict 非递归 constructor/signed-lift 破环输入审查证书。

用法示例：
  python3 experiments/prime_matrix_strict_nonrecursive_constructor_signed_lift_breaker_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json"
OUT_MD = DOCS / "prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.md"

TARGET = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
NUCLEAR_INPUT = "SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion"

SOURCE_FILES = [
    "prime-matrix-strict-self-contained-cycle-obstruction-router.json",
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-alpha-signed-lift-failure-return-router.json",
    "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json",
    "prime-matrix-strict-absolute-fiber-mass-dispersion-router.json",
    "prime-matrix-clean-core-geometric-phi-budget-bridge-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象，便于暴露证据缺口。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def row(
    atom: str,
    evidence_closed: bool,
    proved: bool,
    current_evidence: str,
    obstruction: str,
    needed: str,
) -> dict[str, Any]:
    """构造内部基审查行。"""
    return {
        "atom": atom,
        "evidence_closed": evidence_closed,
        "proved": proved,
        "current_evidence": current_evidence,
        "obstruction": obstruction,
        "needed": needed,
    }


def build_basis_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """检查六个破环内部基在当前语料中的闭合状态。"""
    explicit = data["explicit"]
    signed_lift = data["signed_lift"]
    failure_return = data["failure_return"]
    downstream = data["downstream"]
    absolute = data["absolute"]
    phi_bridge = data["phi_bridge"]
    precauchy = data["precauchy"]
    disintegration = data["disintegration"]
    source_loop = data["source_loop"]
    zero_nogo = data["zero_nogo"]

    return [
        row(
            "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter",
            explicit.get("explicit_alpha_delta_rule_router_closed") is True
            or explicit.get("status") == "strict_explicit_alpha_delta_rule_reduced_to_two_side_rules_pairing_nonzero_open",
            explicit.get("explicit_alpha_delta_primitive_constructor_rule_proved") is True,
            "alpha/delta 规则已压成两侧 primitive rule 与 pairing nonzero 检查。",
            "该规则仍依赖 actual noncanonical source tuple；没有非递归来源表时不能独立生成 constructor。",
            "同一 formal unit 的 primitive summand 公式、u/v map、sign/local factor 与非零/回流表。",
        ),
        row(
            "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger",
            signed_lift.get("zero_row_signed_seed_extraction_blocked_imported") is True
            or zero_nogo.get("zero_row_seed_extraction_blocked") is True,
            signed_lift.get("actual_signed_alpha_source_measure_proved") is True
            or failure_return.get("actual_signed_alpha_source_measure_proved") is True,
            "早期零行和几何链已被审查为 unsigned covering/payment 数据。",
            "unsigned carry-shell、斜线覆盖、P列锚和层叠轮不定义 signed alpha source measure。",
            "pre-Cauchy 阶段直接定义 signed measure nu_alpha，并列出每个 carry-shell row 的来源。",
        ),
        row(
            "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger",
            downstream.get("alpha_weight_law_reduced_to_independent_identity") is True
            or failure_return.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is False,
            failure_return.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is True,
            "权重律已同步到 IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger。",
            "现有下游路线把权重律送回 moving block、NCBLK 与 PDEC/CleanKLS 终端门，形成固定点。",
            "一个不调用终端门的算术核恒等式，直接给出 alpha 权重、符号和 local factor。",
        ),
        row(
            "AlphaRowsPhiPushforwardCompatibilityLedger",
            phi_bridge.get("geometry_does_not_prove_phi_pushforward_identity") is True
            or signed_lift.get("alpha_rows_phi_pushforward_compatibility_proved") is False,
            signed_lift.get("alpha_rows_phi_pushforward_compatibility_proved") is True,
            "几何 Phi/payment base 可用；解积分形式上说明给定 signed source 后可逐纤维推前。",
            "Phi_*nu 等于 payment-side alpha 系数不是几何覆盖自动推出的等式。",
            "同一核恒等式必须同时给出 source 侧和 payment 侧，并证明逐纤维求和相等。",
        ),
        row(
            "AlphaSignedLiftVariationBranchBudgetLedger",
            signed_lift.get("geometric_ledger_unsigned_only_imported") is True
            or phi_bridge.get("geometric_payment_base_available") is True,
            signed_lift.get("alpha_signed_lift_variation_branch_budget_proved") is True
            or failure_return.get("alpha_signed_lift_variation_branch_budget_proved") is True,
            "圆柱斜线、P列锚和层叠轮给出支撑/相位/branch 字母表与预算候选形状。",
            "绝对支撑预算不能替代 signed 总变差预算；branch key 爆炸也不能靠 unsigned 模型消除。",
            "同一 formal unit 下的总变差、绝对支撑、branch key 数和失败命名回流预算。",
        ),
        row(
            "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem",
            absolute.get("absolute_fiber_mass_dispersion_router_closed") is True
            or disintegration.get("signed_fiber_disintegration_formal") is True,
            absolute.get("preterminal_exact_uv_fiber_absolute_mass_dispersion_proved") is True,
            "fiber 非集中已压成 pre-pushforward primitive emitter 的绝对质量/multiplicity 分散。",
            "该分散仍未独立证明；向下会进入 emitter/source table/constructor，最终回到同一 signed source 包。",
            "核恒等式需同时给出 exact-UV fiber 的绝对质量分散或 bounded multiplicity 证明。",
        ),
        row(
            "NonrecursiveSourceOriginCondition",
            precauchy.get("origin_generation_ledger_implication_closed") is True
            and source_loop.get("circular_reverse_derivation_rejected") is True,
            precauchy.get("clean_core_original_coefficient_generation_ledger_proved") is True
            or source_loop.get("nonrecursive_source_constructor_proved") is True,
            "pre-Cauchy 来源律显示需要原始生成账本；来源环切断拒绝 downstream 反推。",
            "payment skeleton、终端证书、有限投影或早期零行覆盖都不能作为 primitive source 的来源证明。",
            "证明必须在 Cauchy、dispersion、terminal extraction 之前提交原始来源。",
        ),
    ]


def build_kernel_fields() -> list[dict[str, str]]:
    """给出真正破环输入必须一次性携带的字段。"""
    return [
        {
            "field": "formal_unit",
            "requirement": "固定同一 formal unit；不得在 source、Phi、fiber 或 terminal 侧更换 witness 集合。",
        },
        {
            "field": "primitive_constructor",
            "requirement": "列出 alpha/delta primitive summand 的 u/v map、branch key、sign、local factor 和非零条件。",
        },
        {
            "field": "signed_source_measure",
            "requirement": "在 carry-shell rows 上定义 actual signed alpha source measure，而不是 unsigned cover。",
        },
        {
            "field": "arithmetic_weight_identity",
            "requirement": "用 pre-Cauchy 算术恒等式给出权重律，不能回调 PDEC/CleanKLS 或 source entropy 目标。",
        },
        {
            "field": "phi_pushforward",
            "requirement": "证明 Phi_*nu_alpha 等于 payment-side alpha 系数，含端点、重数和符号。",
        },
        {
            "field": "variation_branch_budget",
            "requirement": "同时控制 signed 总变差、绝对支撑、branch key 数，超预算时命名回流。",
        },
        {
            "field": "exact_uv_fiber_dispersion",
            "requirement": "给出 exact-UV fiber 绝对质量分散或 bounded multiplicity，且与同一 source measure 兼容。",
        },
        {
            "field": "failure_return",
            "requirement": "任何字段缺失、Phi 不兼容、变差超预算、canonical 泄漏或 terminal-dependent key 都登记到同一命名出口。",
        },
    ]


def build_rows_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总内部基审查结果。"""
    return {
        "all_basis_evidence_routes_closed": all(item["evidence_closed"] for item in rows),
        "all_basis_proved": all(item["proved"] for item in rows),
        "proved_atoms": [item["atom"] for item in rows if item["proved"]],
        "open_atoms": [item["atom"] for item in rows if not item["proved"]],
    }


def build_result() -> dict[str, Any]:
    """构造非递归 constructor/signed-lift 破环输入审查证书。"""
    data = {
        "cycle": load_json("prime-matrix-strict-self-contained-cycle-obstruction-router.json"),
        "explicit": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-formula-signed-lift-router.json"),
        "failure_return": load_json("prime-matrix-strict-alpha-signed-lift-failure-return-router.json"),
        "downstream": load_json("prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"),
        "absolute": load_json("prime-matrix-strict-absolute-fiber-mass-dispersion-router.json"),
        "phi_bridge": load_json("prime-matrix-clean-core-geometric-phi-budget-bridge-router.json"),
        "precauchy": load_json("prime-matrix-clean-core-precauchy-source-law-atom-router.json"),
        "disintegration": load_json("prime-matrix-clean-core-alpha-delta-disintegration-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "counterexample_true": load_json("prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json"),
    }
    rows = build_basis_rows(data)
    summary = build_rows_summary(rows)
    cycle_active = (
        data["cycle"].get("next_direct_attack_target") == TARGET
        and data["cycle"].get("current_internal_route_is_fixed_point") is True
    )
    any_direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    nonrecursive_package_proved = summary["all_basis_proved"] and not any_direct_contradiction
    kernel_fields = build_kernel_fields()
    return {
        "certificate_type": "prime_matrix_strict_nonrecursive_constructor_signed_lift_breaker_router",
        "status": "nonrecursive_constructor_signed_lift_breaker_atomized_kernel_identity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "terminal_cycle_breaker_target_active": cycle_active,
        "current_internal_route_is_fixed_point": data["cycle"].get("current_internal_route_is_fixed_point") is True,
        "nonrecursive_constructor_signed_lift_breaker_router_closed": True,
        "all_basis_evidence_routes_closed": summary["all_basis_evidence_routes_closed"],
        "nonrecursive_breaker_package_proved": nonrecursive_package_proved,
        "same_formal_unit_kernel_identity_proved": False,
        "current_route_still_fixed_point_without_new_kernel_identity": cycle_active and not nonrecursive_package_proved,
        "fragmented_six_leg_proof_rejected": True,
        "direct_unconditional_contradiction_found": any_direct_contradiction,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TARGET,
        "next_direct_attack_target": NUCLEAR_INPUT,
        "kernel_identity_statement": (
            f"{NUCLEAR_INPUT}: 在同一 formal unit、Cauchy/dispersion/terminal extraction 之前，"
            "一次性给出 actual noncanonical alpha/delta primitive constructor、signed alpha source measure、"
            "pre-Cauchy 权重律、Phi 推前恒等式、signed 变差/branch 预算和 exact-UV fiber 分散；"
            "证明过程不得回调 PDEC/CleanKLS 终端门、canonical scoped import、source entropy 目标自身，"
            "也不得从早期零行 unsigned covering data 反向生成 source。"
        ),
        "if_kernel_identity_proved_then": (
            "六个内部基可在同一 witness 集上合取，NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage "
            "才成为真正破环输入；随后可重新进入 exact-UV/source entropy 链，检查是否推出终端矛盾。"
        ),
        "if_kernel_identity_not_proved_then": (
            "现有内部路线只能回到 PDEC/CleanKLS 固定点；不能声明行/列命题作者侧无条件闭合。"
        ),
        "basis_rows": rows,
        "kernel_fields": kernel_fields,
        "open_atoms": summary["open_atoms"],
        "proved_atoms": summary["proved_atoms"],
        "parallel_acceptance_lanes_retained": data["cycle"].get("parallel_acceptance_lanes", []),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步直接审查真正破环输入。结论是：六个内部基的证据路线大多已定位，"
            "但都没有在当前材料中被非递归证明；若逐腿推进，它们会回流到 source table、emitter、"
            "PDEC/CleanKLS 或命名回流固定点。因此当前最窄点不是再拆六项，而是提交一个同一 formal unit "
            "下的 pre-Cauchy alpha/delta 核恒等式，同时携带 signed source、Phi 推前、变差预算和 exact-UV 分散。"
            "在该核恒等式给出前，目标命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 非递归 constructor/signed-lift 破环输入审查",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_cycle_breaker_target_active={fmt_bool(result['terminal_cycle_breaker_target_active'])}",
        f"current_internal_route_is_fixed_point={fmt_bool(result['current_internal_route_is_fixed_point'])}",
        f"all_basis_evidence_routes_closed={fmt_bool(result['all_basis_evidence_routes_closed'])}",
        f"nonrecursive_breaker_package_proved={fmt_bool(result['nonrecursive_breaker_package_proved'])}",
        f"same_formal_unit_kernel_identity_proved={fmt_bool(result['same_formal_unit_kernel_identity_proved'])}",
        f"current_route_still_fixed_point_without_new_kernel_identity={fmt_bool(result['current_route_still_fixed_point_without_new_kernel_identity'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 内部基审查",
        "",
        "| atom | evidence_closed | proved | current evidence | obstruction | needed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["basis_rows"]:
        lines.append(
            "| `{atom}` | `{evidence_closed}` | `{proved}` | {current_evidence} | {obstruction} | {needed} |".format(
                atom=table_cell(item["atom"]),
                evidence_closed=fmt_bool(item["evidence_closed"]),
                proved=fmt_bool(item["proved"]),
                current_evidence=table_cell(item["current_evidence"]),
                obstruction=table_cell(item["obstruction"]),
                needed=table_cell(item["needed"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 新最窄破环输入",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            result["kernel_identity_statement"],
            "",
            "## 3. 核恒等式字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for item in result["kernel_fields"]:
        lines.append(
            "| `{field}` | {requirement} |".format(
                field=table_cell(item["field"]),
                requirement=table_cell(item["requirement"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            result["if_kernel_identity_proved_then"],
            "",
            result["if_kernel_identity_not_proved_then"],
            "",
            "并行保留验收线：",
            "",
            "```text",
            *result["parallel_acceptance_lanes_retained"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
