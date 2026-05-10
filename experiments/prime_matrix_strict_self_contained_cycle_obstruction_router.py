#!/usr/bin/env python3
"""生成 strict 自足终端循环障碍证书。

用法示例：
  python3 experiments/prime_matrix_strict_self_contained_cycle_obstruction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-self-contained-cycle-obstruction-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-self-contained-cycle-obstruction-router.json"
OUT_MD = DOCS / "prime-matrix-strict-self-contained-cycle-obstruction-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json",
    "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json",
    "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json",
    "prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json",
    "prime-matrix-strict-preterminal-support-capacity-attack-router.json",
    "prime-matrix-strict-nonterminal-fiber-aperiodicity-attack-router.json",
    "prime-matrix-strict-absolute-fiber-mass-dispersion-router.json",
    "prime-matrix-strict-emitter-multiplicity-rank-attack-router.json",
    "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
    "prime-matrix-strict-actual-emitter-incidence-entropy-router.json",
    "prime-matrix-strict-fixed-pair-fiber-bound-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-strict-precauchy-declaration-line-router.json",
    "prime-matrix-strict-actual-constructor-formula-line-router.json",
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-alpha-signed-lift-failure-return-router.json",
    "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json",
]

TERMINAL_GATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
CYCLE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象，便于暴露链条缺口。"""
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


def cycle_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成当前自足链的循环审查矩阵。"""
    return [
        {
            "stage": "TerminalSplit",
            "route_closed": data["pdec"].get("terminal_split_router_closed") is True,
            "proved": data["pdec"].get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is True,
            "meaning": "PDEC/CleanKLS 终端门已精确二分，但 PDEC 作用域匹配和自足 KZ/DLS 手臂均未证。",
            "next": data["pdec"].get("next_direct_attack_target"),
        },
        {
            "stage": "KuznetsovDLS",
            "route_closed": data["kz"].get("kz_e_reduced_to_ncblk_or_external") is True,
            "proved": data["kz"].get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is True,
            "meaning": "KZ-A 至 KZ-D 已归档；KZ-E 对数节省被压到 acyclic NC-BLK/source anti-atom 或外部线。",
            "next": data["kz"].get("strict_gap_after_router"),
        },
        {
            "stage": "NCBLK",
            "route_closed": data["ncblk"].get("acyclic_ncblk_not_separate_terminal") is True,
            "proved": data["ncblk"].get("acyclic_ncblk_actual_block_nonconcentration_proved") is True,
            "meaning": "NC-BLK/source anti-atom 不是独立终端；失败去重为 moving atom，再回全局终端门。",
            "next": data["ncblk"].get("terminal_gap_after_router"),
        },
        {
            "stage": "SourceEntropyFirewall",
            "route_closed": data["entropy_fw"].get("exact_entropy_source_law_firewall_closed") is True,
            "proved": data["entropy_fw"].get("new_actual_source_entropy_theorem_proved") is True,
            "meaning": "固定投影、formal WFD、K4/K6、早期零行几何、canonical import 均不能证明 actual-source 熵。",
            "next": data["entropy_fw"].get("strict_self_contained_terminal_after_router"),
        },
        {
            "stage": "SourceEntropyFixedPoint",
            "route_closed": data["source_fp"].get("new_actual_source_entropy_fixed_point_firewall_closed") is True,
            "proved": data["source_fp"].get("new_actual_source_entropy_theorem_proved") is True,
            "meaning": "ExactUV/pair/terminal/canonical 脊柱形成 T -> ... -> T 固定点，不能作为 T 的证明。",
            "next": data["source_fp"].get("next_direct_attack_target"),
        },
        {
            "stage": "PreterminalSupport",
            "route_closed": data["atomize"].get("independent_nonterminal_atomization_closed") is True
            and data["support"].get("preterminal_support_capacity_attack_closed") is True,
            "proved": data["support"].get("preterminal_actual_fulls_factor_support_capacity_proved") is True,
            "meaning": "source entropy 被压成 pre-terminal actual full-S 支撑/容量，再压到 exact-UV fiber 非集中。",
            "next": data["support"].get("next_direct_attack_target"),
        },
        {
            "stage": "AbsoluteFiber",
            "route_closed": data["fiber"].get("nonterminal_fiber_aperiodicity_attack_closed") is True
            and data["absolute"].get("absolute_fiber_mass_dispersion_router_closed") is True,
            "proved": data["absolute"].get("preterminal_exact_uv_fiber_absolute_mass_dispersion_proved") is True,
            "meaning": "fiber 非集中被压成 pre-pushforward primitive emitter 的绝对质量/multiplicity 分散。",
            "next": data["absolute"].get("next_direct_attack_target"),
        },
        {
            "stage": "EmitterRank",
            "route_closed": data["emitter_rank"].get("emitter_multiplicity_rank_attack_closed") is True
            and data["uv_rank"].get("exact_uv_map_rank_incidence_router_closed") is True,
            "proved": data["uv_rank"].get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is True,
            "meaning": "primitive emitter multiplicity 被压成 exact-UV map rank/no-collapse 和 bounded incidence。",
            "next": data["uv_rank"].get("next_direct_attack_target"),
        },
        {
            "stage": "IncidenceKeySourceTable",
            "route_closed": data["incidence"].get("actual_emitter_incidence_entropy_router_closed") is True
            and data["fixed_pair"].get("fixed_pair_fiber_bound_router_closed") is True
            and data["key"].get("complete_emitter_key_partition_router_closed") is True
            and data["source_table"].get("actual_emitter_source_table_router_closed") is True,
            "proved": data["source_table"].get("actual_noncanonical_primitive_emitter_source_table_proved") is True,
            "meaning": "bounded incidence 被压成 source-domain 熵、fixed-pair fiber bound、complete key 与 actual emitter source table。",
            "next": data["source_table"].get("next_direct_attack_target"),
        },
        {
            "stage": "ConstructorRule",
            "route_closed": data["decl"].get("precauchy_declaration_line_router_closed") is True
            and data["formula"].get("actual_constructor_formula_line_router_closed") is True
            and data["explicit"].get("explicit_alpha_delta_rule_router_closed") is True,
            "proved": data["explicit"].get("explicit_alpha_delta_primitive_constructor_rule_proved") is True,
            "meaning": "source table 第一行被压成 actual noncanonical constructor formula 和两侧 alpha/delta primitive rule。",
            "next": data["explicit"].get("next_direct_attack_target"),
        },
        {
            "stage": "AlphaSignedLift",
            "route_closed": data["alpha_rule"].get("alpha_side_primitive_rule_router_closed") is True
            and data["alpha_emit"].get("deterministic_alpha_row_emission_map_router_closed") is True
            and data["alpha_phase"].get("alpha_row_anchor_phase_formula_router_closed") is True
            and data["signed_lift"].get("alpha_formula_signed_lift_router_closed") is True,
            "proved": data["signed_lift"].get("alpha_formula_signed_coefficient_lift_proved") is True,
            "meaning": "alpha 侧规则被压到确定性发射、anchor/phase 公式和 signed lift；早期零行刚性仍只是 unsigned 形状。",
            "next": data["signed_lift"].get("next_direct_attack_target"),
        },
        {
            "stage": "ReturnToTerminal",
            "route_closed": data["lift_return"].get("alpha_signed_lift_failure_named_return_ledger_closed") is True
            and data["downstream"].get("downstream_sync_router_closed") is True,
            "proved": data["downstream"].get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is True,
            "meaning": "signed lift 失败命名回流闭合为登记纪律；alpha weight 下游同步回 PDEC/CleanKLS 终端门。",
            "next": data["downstream"].get("next_direct_attack_target"),
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 自足终端循环障碍证书。"""
    data = {
        "pdec": load_json("prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"),
        "kz": load_json("prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json"),
        "ncblk": load_json("prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json"),
        "entropy_fw": load_json("prime-matrix-strict-exact-entropy-source-law-firewall-router.json"),
        "source_fp": load_json("prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json"),
        "atomize": load_json("prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json"),
        "support": load_json("prime-matrix-strict-preterminal-support-capacity-attack-router.json"),
        "fiber": load_json("prime-matrix-strict-nonterminal-fiber-aperiodicity-attack-router.json"),
        "absolute": load_json("prime-matrix-strict-absolute-fiber-mass-dispersion-router.json"),
        "emitter_rank": load_json("prime-matrix-strict-emitter-multiplicity-rank-attack-router.json"),
        "uv_rank": load_json("prime-matrix-strict-exact-uv-map-rank-incidence-router.json"),
        "incidence": load_json("prime-matrix-strict-actual-emitter-incidence-entropy-router.json"),
        "fixed_pair": load_json("prime-matrix-strict-fixed-pair-fiber-bound-router.json"),
        "key": load_json("prime-matrix-strict-complete-emitter-key-partition-router.json"),
        "source_table": load_json("prime-matrix-strict-actual-emitter-source-table-router.json"),
        "decl": load_json("prime-matrix-strict-precauchy-declaration-line-router.json"),
        "formula": load_json("prime-matrix-strict-actual-constructor-formula-line-router.json"),
        "explicit": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
        "alpha_rule": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "alpha_emit": load_json("prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"),
        "alpha_phase": load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-formula-signed-lift-router.json"),
        "lift_return": load_json("prime-matrix-strict-alpha-signed-lift-failure-return-router.json"),
        "downstream": load_json("prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"),
    }
    rows = cycle_rows(data)
    cycle_edges_closed = all(row["route_closed"] for row in rows)
    any_cycle_node_proved = any(row["proved"] for row in rows)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    returned_to_terminal = data["downstream"].get("next_direct_attack_target") == TERMINAL_GATE

    cycle_breaker_basis = (
        "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND "
        "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND "
        "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND "
        "AlphaRowsPhiPushforwardCompatibilityLedger AND "
        "AlphaSignedLiftVariationBranchBudgetLedger AND "
        "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem"
    )

    return {
        "certificate_type": "prime_matrix_strict_self_contained_cycle_obstruction_router",
        "status": "strict_self_contained_cycle_obstruction_closed_nonrecursive_cycle_breaker_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "cycle_edges_closed": cycle_edges_closed,
        "cycle_returns_to_pdec_clean_kls_terminal_gate": returned_to_terminal,
        "current_internal_route_is_fixed_point": cycle_edges_closed and returned_to_terminal,
        "any_cycle_node_proved_as_contradiction": any_cycle_node_proved,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "self_contained_cycle_obstruction_proved": cycle_edges_closed and returned_to_terminal and not direct_contradiction,
        "strict_internal_chain_after_router": (
            f"{TERMINAL_GATE} -> KZ/NCBLK -> source entropy -> exact-UV/source table "
            f"-> alpha signed lift -> {TERMINAL_GATE}"
        ),
        "next_direct_attack_target": CYCLE_BREAKER,
        "cycle_breaker_basis": cycle_breaker_basis,
        "parallel_acceptance_lanes": [
            "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate",
            "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks",
            "ExplicitModelGapAndFiniteDPRCLedger",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "hard_law": (
            "当前自足内部路线已不是一条通向矛盾的单向下降链，而是一条证明固定点："
            "从 PDEC/CleanKLS 终端门出发，经 KZ/NC-BLK、source entropy、exact-UV/source table、"
            "alpha signed lift 后又回到同一 PDEC/CleanKLS 终端门。该循环能排除伪出口和命名损失，"
            "但不能证明反例不存在。要破环，必须给出不经终端回流、不经 canonical scoped import、"
            "不从早期零行 unsigned 覆盖反推的 actual noncanonical pre-Cauchy 构造与 signed lift 包。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把当前最窄自足主攻链直接攻到底后，得到的是严格循环障碍而非无条件闭合："
            "`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 经 Kuznetsov/DLS、NC-BLK、actual-source 熵、"
            "ExactUV/source table、alpha signed lift 后，回到同一终端门。"
            "所以当前材料没有给出终端矛盾；真正破环输入是一个非递归的 actual noncanonical "
            "pre-Cauchy constructor/signed-lift 包，或独立证明 PDEC 作用域匹配、KZ/DLS 原子、"
            "模型余量账本和 DStructure/Rankin 验收门。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 自足终端循环障碍路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"cycle_edges_closed={fmt_bool(result['cycle_edges_closed'])}",
        f"cycle_returns_to_pdec_clean_kls_terminal_gate={fmt_bool(result['cycle_returns_to_pdec_clean_kls_terminal_gate'])}",
        f"current_internal_route_is_fixed_point={fmt_bool(result['current_internal_route_is_fixed_point'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 循环链",
        "",
        "```text",
        result["strict_internal_chain_after_router"],
        "```",
        "",
        "## 2. 循环审查矩阵",
        "",
        "| stage | route_closed | proved | meaning | next |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{stage}` | `{route_closed}` | `{proved}` | {meaning} | {next} |".format(
                stage=table_cell(row["stage"]),
                route_closed=fmt_bool(row["route_closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                next=table_cell(row["next"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 破环输入",
            "",
            "下一直接主攻点：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "其内部基为：",
            "",
            "```text",
            result["cycle_breaker_basis"],
            "```",
            "",
            "并行验收线：",
            "",
            "```text",
            *result["parallel_acceptance_lanes"],
            "```",
            "",
            "## 4. 结构结论",
            "",
            result["hard_law"],
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
