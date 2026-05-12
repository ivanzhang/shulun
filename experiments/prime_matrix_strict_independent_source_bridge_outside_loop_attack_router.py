#!/usr/bin/env python3
"""生成 strict 独立 actual-source 桥外环直攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_independent_source_bridge_outside_loop_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-independent-source-bridge-outside-loop-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-independent-source-bridge-outside-loop-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-independent-source-bridge-outside-loop-attack-router.md"

OUTSIDE_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
SOURCE_IDENTITY = "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab"
STRENGTHENED_ANTIATOM = "FullSNonAPStrengthenedSourceAntiAtomForActualSource"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXTERNAL_KLS = "ModulusDependentCompletedFullSKLSInput"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json",
    "prime-matrix-actual-source-antiatom-lane-audit-router.json",
    "prime-matrix-noncanonical-complement-input-contract-router.json",
    "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json",
    "prime-matrix-actual-source-bridge-global-reconciliation-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json",
    "prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """记录本证书使用的上游证据哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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


def bridge_split() -> list[dict[str, str]]:
    """列出外环 source bridge 的合法拆分。"""
    return [
        {
            "from": OUTSIDE_BRIDGE,
            "to": f"{SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM}",
        },
        {
            "from": SOURCE_IDENTITY,
            "to": "actual full-S non-AP source equals canonical RIW/Buchstab decision-tree source before dispersion",
        },
        {
            "from": STRENGTHENED_ANTIATOM,
            "to": "actual noncanonical final capacity measure has no moving same-(u,v) atom",
        },
        {
            "from": "conditional external lane",
            "to": EXTERNAL_KLS,
        },
    ]


def required_fields() -> list[dict[str, str]]:
    """列出两个自足输入的最小字段要求。"""
    return [
        {
            "field": "actual_source_identity",
            "meaning": "在 Cauchy/dispersion/payment 前证明实际 full-S non-AP 源就是 canonical RIW/Buchstab 决策树源。",
        },
        {
            "field": "strengthened_actual_antiatom",
            "meaning": "直接证明实际 noncanonical final capacity measure 满足 moving same-(u,v) 大原子反界。",
        },
        {
            "field": "no_generic_wfd_substitution",
            "meaning": "不得用已被 moving-delta 反证的 generic WFD/Type/Fourier/K4K6 模板替代 actual-source 定理。",
        },
        {
            "field": "no_exactuv_pair_energy_loop",
            "meaning": "不得把 ExactUV/pair-energy/joint constructor 回环作为 independent bridge 的证明。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步 actual-source 桥外环证据。"""
    macro = data["macro"]
    antiatom = data["antiatom"]
    complement = data["complement"]
    taxonomy = data["taxonomy"]
    global_recon = data["global_recon"]
    canonical = data["canonical"]
    entropy_firewall = data["entropy_firewall"]
    joint = data["joint"]
    external = data["external"]

    macro_imported = (
        macro.get("terminal_descent_macrocycle_detected") is True
        and macro.get("independent_actual_source_bridge_outside_pair_energy_loop_proved") is False
    )
    canonical_scoped = (
        canonical.get("canonical_lock_branch_absorption_closed") is True
        and canonical.get("canonical_lock_standalone_global_contradiction") is False
        and global_recon.get("actual_source_bridge_closes_global_unrestricted") is False
    )
    source_identity_open = "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab" in str(complement)
    generic_refuted = (
        antiatom.get("generic_self_contained_antiatom_refuted") is True
        and complement.get("generic_wfd_template_available") is False
        and taxonomy.get("generic_self_contained_version_refuted") is True
    )
    strengthened_pinned = (
        antiatom.get("actual_source_antiatom_lane_boundary_closed") is True
        and STRENGTHENED_ANTIATOM in str(complement)
    )
    entropy_shortcuts_blocked = (
        entropy_firewall.get("fixed_projection_route_blocked") is True
        and entropy_firewall.get("formal_wfd_route_refuted") is True
        and entropy_firewall.get("pair_mass_equivalence_not_proof") is True
    )
    no_existing_antiatom = antiatom.get("actual_source_antiatom_proved") is False
    external_conditional = (
        external.get("terminal_gap_after_router") == EXTERNAL_KLS
        or EXTERNAL_KLS in str(entropy_firewall)
        or EXTERNAL_KLS in str(complement)
    )
    new_joint_open = joint.get("new_explicit_joint_constructor_formula_artifact_present") is False

    return [
        row(
            "MacrocycleImported",
            macro_imported,
            True,
            "上一轮已证明 TERMINAL->SOURCE->PAIR->JOINT->TERMINAL 是宏循环；独立桥必须避开该回环。",
            OUTSIDE_BRIDGE,
        ),
        row(
            "CanonicalBranchOnlyScoped",
            canonical_scoped,
            True,
            "canonical RIW/Buchstab 分支已经闭合为 scoped case，但不能自动覆盖 unrestricted noncanonical 补集。",
            SOURCE_IDENTITY,
        ),
        row(
            "SourceIdentityOptionStillOpen",
            source_identity_open,
            False,
            "若要用 source identity 破环，必须证明实际 full-S non-AP 源等于 canonical 决策树源；当前没有该证明。",
            SOURCE_IDENTITY,
        ),
        row(
            "GenericWFDSelfContainedTemplateRefuted",
            generic_refuted,
            True,
            "unrestricted generic WFD/Type/Fourier 自足模板已被 moving-delta 模型反证。",
            "不能作为自足桥。",
        ),
        row(
            "StrengthenedAntiAtomContractPinned",
            strengthened_pinned,
            True,
            "noncanonical 补集的 actual-source 侧只剩实际源强化反原子，而不是形式筛法推论。",
            STRENGTHENED_ANTIATOM,
        ),
        row(
            "EntropyShortcutFirewallImported",
            entropy_shortcuts_blocked,
            True,
            "fixed projection、formal WFD、K4/K6、早期零行几何和 pair-mass 等价命名都不能证明 actual entropy。",
            STRENGTHENED_ANTIATOM,
        ),
        row(
            "NoExistingStrengthenedAntiAtomProof",
            no_existing_antiatom,
            False,
            "当前材料没有实际 noncanonical full-S 源强化反原子的证明。",
            STRENGTHENED_ANTIATOM,
        ),
        row(
            "ExternalCompletedKLSOnlyConditional",
            external_conditional,
            False,
            "completed/modulus-dependent full-S KLS 可作为条件外部线，但不能写成 strict 自足证明。",
            EXTERNAL_KLS,
        ),
        row(
            "NewJointFormulaParallelStillOpen",
            new_joint_open,
            False,
            "新显式 joint alpha/delta 公式仍是并行破环输入；当前语料没有该工件。",
            NEW_JOINT_FORMULA,
        ),
        row(
            "IndependentSourceBridgeOutsideLoopCurrentCorpusProved",
            False,
            False,
            "外环桥已经压成 source identity 或 strengthened anti-atom；两者当前均未证明。",
            f"{SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只压缩独立桥，不关闭 ExactUV、RatePreservation、DStructure/Rankin 和最终行/列命题。",
            f"({NEW_JOINT_FORMULA} OR {SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM}) AND {EXACT_UV} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造外环桥直攻证书。"""
    data = {
        "macro": load_json("prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json"),
        "antiatom": load_json("prime-matrix-actual-source-antiatom-lane-audit-router.json"),
        "complement": load_json("prime-matrix-noncanonical-complement-input-contract-router.json"),
        "taxonomy": load_json("prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"),
        "global_recon": load_json("prime-matrix-actual-source-bridge-global-reconciliation-router.json"),
        "canonical": load_json("prime-matrix-strict-canonical-lock-branch-absorption-router.json"),
        "entropy_firewall": load_json("prime-matrix-strict-exact-entropy-source-law-firewall-router.json"),
        "joint": load_json("prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"),
        "external": load_json("prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json"),
    }
    rows = build_rows(data)
    active_basis = f"({NEW_JOINT_FORMULA} OR {SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM}) AND {EXACT_UV} AND {RATE} AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_strict_independent_source_bridge_outside_loop_attack_router",
        "status": "independent_source_bridge_outside_loop_reduced_to_source_identity_or_strengthened_antiatom_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "macrocycle_imported": any(r["gate"] == "MacrocycleImported" and r["closed"] for r in rows),
        "canonical_branch_only_scoped": any(r["gate"] == "CanonicalBranchOnlyScoped" and r["closed"] for r in rows),
        "generic_wfd_template_refuted": any(r["gate"] == "GenericWFDSelfContainedTemplateRefuted" and r["closed"] for r in rows),
        "source_identity_proved": False,
        "strengthened_actual_source_antiatom_proved": False,
        "independent_actual_source_bridge_outside_pair_energy_loop_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "external_completed_kls_accepted_as_strict_proof": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": OUTSIDE_BRIDGE,
        "strict_active_basis_after_router": active_basis,
        "conditional_external_basis": f"({NEW_JOINT_FORMULA} OR {SOURCE_IDENTITY} OR {STRENGTHENED_ANTIATOM} OR {EXTERNAL_KLS}) AND {EXACT_UV} AND {RATE} AND {DSTRUCTURE}",
        "bridge_split": bridge_split(),
        "required_fields": required_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本轮直接攻 {OUTSIDE_BRIDGE}。canonical 分支已闭合但只是 scoped case；"
            "generic WFD 自足模板已被 moving-delta 反证；ExactUV/pair-energy/joint 下钻又会回到宏循环。"
            f"因此严格自足外环桥只能是 {SOURCE_IDENTITY} 或 {STRENGTHENED_ANTIATOM}。"
            "当前二者均未证明；外部 completed KLS 只能作为条件线。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict 独立 actual-source 桥外环直攻证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "macrocycle_imported",
        "canonical_branch_only_scoped",
        "generic_wfd_template_refuted",
        "source_identity_proved",
        "strengthened_actual_source_antiatom_proved",
        "independent_actual_source_bridge_outside_pair_energy_loop_proved",
        "new_explicit_joint_constructor_formula_artifact_present",
        "external_completed_kls_accepted_as_strict_proof",
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved",
        "rate_preservation_ledger_proved",
        "dstructure_independent_gate_closed",
        "direct_unconditional_contradiction_found",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 外环桥拆分")
    lines.append("")
    lines.append("| from | to |")
    lines.append("| --- | --- |")
    for item in result["bridge_split"]:
        lines.append(f"| {cell(item['from'])} | {cell(item['to'])} |")
    lines.append("")
    lines.append("## 2. 必要字段")
    lines.append("")
    lines.append("| field | meaning |")
    lines.append("| --- | --- |")
    for item in result["required_fields"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.append("")
    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## 4. 当前严格活动基")
    lines.append("")
    lines.append("```text")
    lines.append(result["strict_active_basis_after_router"])
    lines.append("```")
    lines.append("")
    lines.append("条件外部线：")
    lines.append("")
    lines.append("```text")
    lines.append(result["conditional_external_basis"])
    lines.append("```")
    lines.append("")
    lines.append("审稿边界：本文件只压缩外环 actual-source 桥；没有证明 source identity、强化反原子、ExactUV、RatePreservation 或 DStructure/Rankin。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"independent_actual_source_bridge_outside_pair_energy_loop_proved={fmt_bool(result['independent_actual_source_bridge_outside_pair_energy_loop_proved'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"wrote={OUT_JSON.relative_to(ROOT)}")
    print(f"wrote={OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
