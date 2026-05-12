#!/usr/bin/env python3
"""生成 strict 终端下降宏循环调和证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_descent_macrocycle_reconciliation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json"
OUT_MD = DOCS / "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.md"

TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughAlphaReturn"
ACTUAL_BRIDGE = "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
SOURCE_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
EXACT_ENTROPY = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
PAIR_ENERGY = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
JOINT_CONSTRUCTOR = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
NEW_BRIDGE_ARTIFACT = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json",
    "prime-matrix-strict-descent-leaf-firewall-alpha-return-sync-router.json",
    "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json",
    "prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取证书；缺失时返回空对象，避免把缺文件误判为证明。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本证书引用的上游文件哈希。"""
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


def macrocycle_chain() -> list[dict[str, str]]:
    """列出当前材料中终端下降继续下钻形成的宏循环。"""
    return [
        {"from": TERMINAL_DESCENT, "to": "TerminalLeafFirewallInputs_OR_CanonicalLock"},
        {"from": "TerminalLeafFirewallInputs_OR_CanonicalLock", "to": f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}"},
        {"from": INDEPENDENT_BRIDGE, "to": f"{SOURCE_ADMISSION} OR {EXACT_ENTROPY}"},
        {"from": EXACT_ENTROPY, "to": SOURCE_ENTROPY},
        {"from": SOURCE_ENTROPY, "to": PAIR_ENERGY},
        {"from": PAIR_ENERGY, "to": "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"},
        {"from": "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate", "to": JOINT_CONSTRUCTOR},
        {"from": JOINT_CONSTRUCTOR, "to": "signed-source fixed point"},
        {"from": "signed-source fixed point", "to": TERMINAL_DESCENT},
    ]


def noncycle_fields() -> list[dict[str, str]]:
    """当前可破环输入的最小字段要求。"""
    return [
        {
            "field": "canonical_lock_full_certificate",
            "meaning": "证明 acyclic 终端同集推前、有限因子图、branch key 锁定和无 noncanonical payload 残留。",
        },
        {
            "field": "new_joint_formula",
            "meaning": "提交 actual joint alpha/delta 正向公式；同一行给出 basis word、signed coefficient、u/v、branch、sign/local factor。",
        },
        {
            "field": "independent_actual_source_bridge",
            "meaning": "在进入 ExactUV/pair-energy/alpha 回边前证明 actual source 恒等或强化反原子。",
        },
        {
            "field": "parallel_exactuv_rate_dstructure",
            "meaning": "即使破环成功，仍需 ExactUV bounded multiplicity、RatePreservation 和 DStructure/Rankin 独立门。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步终端下降、actual-source、pair-energy 与 joint 构造器路线。"""
    explicit_joint = data["explicit_joint"]
    alpha_return = data["alpha_return"]
    bridge = data["bridge"]
    entropy_firewall = data["entropy_firewall"]
    entropy_guard = data["entropy_guard"]
    pair = data["pair"]
    leaf = data["leaf"]
    canonical = data["canonical"]

    terminal_candidate = explicit_joint.get("noncycle_alternative_after_router") == TERMINAL_DESCENT
    descent_to_bridge = (
        alpha_return.get("terminal_gap_after_router") == f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}"
        and alpha_return.get("pointwise_alpha_route_counts_as_well_founded_descent") is False
    )
    bridge_to_entropy = (
        bridge.get("terminal_gap_after_router")
        == f"{CANONICAL_LOCK} OR {SOURCE_ADMISSION} OR {EXACT_ENTROPY}"
        and bridge.get("exact_clean_core_source_entropy_proved") is False
    )
    entropy_to_pair = (
        entropy_firewall.get("new_actual_source_entropy_theorem_proved") is False
        and entropy_guard.get("pair_mass_return_loop_detected") is True
        and entropy_guard.get("independent_exact_pair_l2_or_max_atom_bound_proved") is False
    )
    pair_to_joint = (
        pair.get("current_pair_energy_attack_spine_is_recursive") is True
        and pair.get("first_productive_input_after_router") == JOINT_CONSTRUCTOR
    )
    joint_to_terminal = (
        explicit_joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True
        and explicit_joint.get("new_explicit_joint_constructor_formula_artifact_present") is False
        and explicit_joint.get("noncycle_alternative_after_router") == TERMINAL_DESCENT
    )
    canonical_open = (
        canonical.get("acyclic_terminal_canonical_lock_proved") is False
        or leaf.get("acyclic_terminal_canonical_lock_proved") is False
    )
    macrocycle = all([terminal_candidate, descent_to_bridge, bridge_to_entropy, entropy_to_pair, pair_to_joint, joint_to_terminal])

    return [
        row(
            "TerminalDescentStillActiveAsAlternative",
            terminal_candidate,
            False,
            "显式 joint 构造器直接攻坚后，非循环替代仍指向终端下降证书。",
            TERMINAL_DESCENT,
        ),
        row(
            "DescentLeafAlphaRouteIsBackedge",
            descent_to_bridge,
            True,
            "终端下降的旧 pointwise/alpha 下钻已被登记为回边，不能计为 well-founded 进展量。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}",
        ),
        row(
            "IndependentBridgeReducedToSourceAdmissionOrEntropy",
            bridge_to_entropy,
            False,
            "independent actual-source 桥已具体化为 A1 source admission 或 exact entropy，但二者均未证明。",
            f"{SOURCE_ADMISSION} OR {EXACT_ENTROPY}",
        ),
        row(
            "ExactEntropyRouteReturnsToPairEnergyInput",
            entropy_to_pair,
            True,
            "exact entropy 经非递归守门后不能用自身回证 pair-mass，只剩独立 pair L2/max-atom 能量输入。",
            PAIR_ENERGY,
        ),
        row(
            "PairEnergyCurrentSpineReturnsToJointConstructor",
            pair_to_joint,
            True,
            "现有 pair-energy/rate-packet/terminal 脊柱为递归脊柱，已重钉到 joint constructor 工件。",
            JOINT_CONSTRUCTOR,
        ),
        row(
            "JointConstructorReturnsToTerminalDescent",
            joint_to_terminal,
            True,
            "没有新的显式 joint 公式时，joint-alpha/signed-source 路线回到终端下降替代门。",
            TERMINAL_DESCENT,
        ),
        row(
            "TerminalDescentMacrocycleDetected",
            macrocycle,
            True,
            "当前终端下降直攻链形成 TERMINAL -> SOURCE -> PAIR -> JOINT -> TERMINAL 宏循环。",
            f"{CANONICAL_LOCK} OR {NEW_JOINT_FORMULA} OR {NEW_BRIDGE_ARTIFACT}",
        ),
        row(
            "CurrentTerminalDescentAttackSpineRejectedAsProof",
            macrocycle,
            True,
            "该宏循环只能作为路线审查结论，不能作为终端矛盾或 well-founded descent 证明。",
            "必须提交破环输入。",
        ),
        row(
            "CanonicalLockStillOpenParallel",
            canonical_open,
            False,
            "canonical-lock 仍是并行破环路线，但其同集推前、有限因子图和无 payload 残留未证。",
            CANONICAL_LOCK,
        ),
        row(
            "NewJointFormulaStillOpen",
            explicit_joint.get("new_explicit_joint_constructor_formula_artifact_present") is False,
            False,
            "显式 joint 构造器需要新的正向公式工件；当前语料没有该工件。",
            NEW_JOINT_FORMULA,
        ),
        row(
            "IndependentBridgeOutsidePairEnergyLoopStillOpen",
            True,
            False,
            "若继续走 actual-source 桥，必须在 ExactUV/pair-energy/joint 回环前独立证明源恒等或强化反原子。",
            NEW_BRIDGE_ARTIFACT,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "宏循环已暴露但未产生矛盾；ExactUV、RatePreservation 与 DStructure/Rankin 门仍未全部闭合。",
            f"({CANONICAL_LOCK} OR {NEW_JOINT_FORMULA} OR {NEW_BRIDGE_ARTIFACT}) AND {EXACT_UV} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造终端下降宏循环调和结果。"""
    data = {
        "explicit_joint": load_json("prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"),
        "alpha_return": load_json("prime-matrix-strict-descent-leaf-firewall-alpha-return-sync-router.json"),
        "bridge": load_json("prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json"),
        "entropy_firewall": load_json("prime-matrix-strict-exact-entropy-source-law-firewall-router.json"),
        "entropy_guard": load_json("prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json"),
        "pair": load_json("prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json"),
        "leaf": load_json("prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json"),
        "canonical": load_json("prime-matrix-strict-canonical-lock-branch-absorption-router.json"),
    }
    rows = build_rows(data)
    active_basis = f"({CANONICAL_LOCK} OR {NEW_JOINT_FORMULA} OR {NEW_BRIDGE_ARTIFACT}) AND {EXACT_UV} AND {RATE} AND {DSTRUCTURE}"
    macrocycle = any(r["gate"] == "TerminalDescentMacrocycleDetected" and r["closed"] for r in rows)
    return {
        "certificate_type": "prime_matrix_strict_terminal_descent_macrocycle_reconciliation_router",
        "status": "terminal_descent_current_attack_spine_reconciled_as_macrocycle_new_break_inputs_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "terminal_descent_macrocycle_detected": macrocycle,
        "current_terminal_descent_attack_spine_is_recursive": macrocycle,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "independent_actual_source_bridge_outside_pair_energy_loop_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": TERMINAL_DESCENT,
        "macrocycle_chain": macrocycle_chain(),
        "required_noncycle_fields": noncycle_fields(),
        "strict_active_basis_after_router": active_basis,
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮直接攻 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` 的当前最窄链条。"
            "同步后发现，沿终端叶子、actual-source、exact entropy、pair-energy 和 joint constructor 继续下钻，"
            "会形成 TERMINAL -> SOURCE -> PAIR -> JOINT -> TERMINAL 宏循环。"
            "因此当前脊柱不能作为 well-founded descent 证明；非循环破环必须来自 canonical-lock 全证书、"
            "新的显式 actual joint alpha/delta 公式工件，或不经过 ExactUV/pair-energy/joint 回环的独立 actual-source 桥。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict 终端下降宏循环调和证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "terminal_descent_macrocycle_detected",
        "current_terminal_descent_attack_spine_is_recursive",
        "acyclic_terminal_return_well_founded_descent_proved",
        "acyclic_terminal_canonical_lock_proved",
        "new_explicit_joint_constructor_formula_artifact_present",
        "independent_actual_source_bridge_outside_pair_energy_loop_proved",
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved",
        "rate_preservation_ledger_proved",
        "dstructure_independent_gate_closed",
        "direct_unconditional_contradiction_found",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 宏循环链")
    lines.append("")
    lines.append("| from | to |")
    lines.append("| --- | --- |")
    for item in result["macrocycle_chain"]:
        lines.append(f"| {cell(item['from'])} | {cell(item['to'])} |")
    lines.append("")
    lines.append("## 2. 非循环破环字段")
    lines.append("")
    lines.append("| field | meaning |")
    lines.append("| --- | --- |")
    for item in result["required_noncycle_fields"]:
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
    lines.append("审稿边界：本文件只证明当前终端下降直攻脊柱是宏循环，不能把宏循环本身当作矛盾或闭合证明。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"terminal_descent_macrocycle_detected={fmt_bool(result['terminal_descent_macrocycle_detected'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"wrote={OUT_JSON.relative_to(ROOT)}")
    print(f"wrote={OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
