#!/usr/bin/env python3
"""生成 strict 最新自足硬点同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_latest_self_contained_hardpoint_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-latest-self-contained-hardpoint-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-latest-self-contained-hardpoint-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-latest-self-contained-hardpoint-sync-router.md"

CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
NONCANONICAL_MODE = "NoncanonicalFullSComplementLegalClosureMode"
ACTUAL_BRIDGE = "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
EXACT_ENTROPY = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
ACYCLIC_SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
PAIR_ENERGY = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
EXACT_SUPPORT = "ActualNoncanonicalExactUVSupportLowerBound"
SHORT_RETURN = "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect"
PHASE_DEFECT = "SignatureDriftToRegisteredPhaseDefectTheorem"
SIGNED_ROW_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
SIGNED_SOURCE_CYCLE_GUARD = "NoncircularPreCauchySignedCoefficientOriginInputIndependentOfRowLevelGenerationCycle"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json",
    "prime-matrix-strict-noncanonical-legal-closure-mode-router.json",
    "prime-matrix-strict-source-admission-branch-absorption-router.json",
    "prime-matrix-strict-moving-atom-entropy-normal-form-router.json",
    "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json",
    "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
    "prime-matrix-strict-stable-short-return-defect-terminal-schema-sync-router.json",
    "prime-matrix-strict-actual-source-domain-entropy-atom-router.json",
    "prime-matrix-strict-signed-source-cycle-frontier-sync-router.json",
    "prime-matrix-strict-acyclic-signed-value-cycle-sync-router.json",
    "prime-matrix-dstructure-rankin-promotion-acceptance-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记引用证据哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def chain() -> list[dict[str, str]]:
    """展示当前硬点压缩链。"""
    return [
        {"from": f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}", "to": f"{CANONICAL_LOCK} OR {ACTUAL_BRIDGE}"},
        {"from": ACTUAL_BRIDGE, "to": f"A1 branch scoped statement OR {MOVING_ATOM}"},
        {"from": "A1 branch scoped statement", "to": "absorbed; not standalone global contradiction"},
        {"from": MOVING_ATOM, "to": EXACT_ENTROPY},
        {"from": EXACT_ENTROPY, "to": f"{ACYCLIC_SEED} AND {PAIR_ENERGY}"},
        {"from": SHORT_RETURN, "to": "admission schema closed; terminal exclusion still open"},
        {"from": SIGNED_ROW_LAW, "to": "signed-source fixed point unless noncircular input supplied"},
    ]


def build_result() -> dict[str, Any]:
    """同步当前所有主要自足硬点到最新非循环输入。"""
    terminal = load_json("prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json")
    noncanonical = load_json("prime-matrix-strict-noncanonical-legal-closure-mode-router.json")
    source_absorb = load_json("prime-matrix-strict-source-admission-branch-absorption-router.json")
    moving = load_json("prime-matrix-strict-moving-atom-entropy-normal-form-router.json")
    direct_entropy = load_json("prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json")
    nonrecursive_guard = load_json("prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json")
    support_seed = load_json("prime-matrix-strict-actual-source-support-seed-router.json")
    counterexample = load_json("prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json")
    stable_schema = load_json("prime-matrix-strict-stable-short-return-defect-terminal-schema-sync-router.json")
    domain_entropy = load_json("prime-matrix-strict-actual-source-domain-entropy-atom-router.json")
    signed_cycle = load_json("prime-matrix-strict-signed-source-cycle-frontier-sync-router.json")
    signed_value_cycle = load_json("prime-matrix-strict-acyclic-signed-value-cycle-sync-router.json")
    dstructure = load_json("prime-matrix-dstructure-rankin-promotion-acceptance-router.json")

    terminal_synced = (
        terminal.get("sync_closed") is True
        and terminal.get("next_direct_attack_target") == f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}"
    )
    noncanonical_to_bridge = (
        noncanonical.get("noncanonical_legal_closure_boundary_refined") is True
        and noncanonical.get("actual_source_bridge_theorem_closed") is False
    )
    source_admission_absorbed = (
        source_absorb.get("source_admission_absorbed_from_active_or") is True
        and source_absorb.get("moving_atom_unique_noncanonical_strict_leaf") is True
    )
    moving_to_entropy = (
        moving.get("moving_atom_entropy_normal_form_closed") is True
        and moving.get("exact_clean_core_source_entropy_proved") is False
    )
    entropy_to_support = (
        direct_entropy.get("support_to_entropy_conditional_inequality_closed") is True
        and direct_entropy.get("actual_exact_uv_support_proved") is False
    )
    support_to_seed_energy = (
        support_seed.get("new_actual_exact_uv_support_boundary_closed") is True
        and support_seed.get("elementary_mass_support_lemma_closed") is True
        and support_seed.get("actual_exact_uv_support_proved") is False
    )
    nonrecursive_energy_guard = (
        nonrecursive_guard.get("nonrecursive_guard_closed") is True
        and nonrecursive_guard.get("independent_exact_pair_l2_or_max_atom_bound_proved") is False
    )
    stable_direct_schema_only = (
        counterexample.get("short_same_label_recurrence_contradiction_lemma_proved") is True
        and counterexample.get("early_zero_forces_stable_short_return_or_defect_proved") is False
        and stable_schema.get("stable_short_return_or_defect_admission_schema_closed") is True
        and stable_schema.get("terminal_exclusion_proved") is False
    )
    signed_source_recycles = (
        domain_entropy.get("actual_source_domain_entropy_atomization_closed") is True
        and domain_entropy.get("acyclic_seed_primitive_row_signed_coefficient_law_proved") is False
        and signed_cycle.get("signed_source_route_closed_as_diagnostic_cycle") is True
        and signed_value_cycle.get("acyclic_signed_value_subcycle_detected") is True
    )
    dstructure_open = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )
    sync_closed = all(
        [
            terminal_synced,
            noncanonical_to_bridge,
            source_admission_absorbed,
            moving_to_entropy,
            entropy_to_support,
            support_to_seed_energy,
            nonrecursive_energy_guard,
            stable_direct_schema_only,
            signed_source_recycles,
            dstructure_open,
        ]
    )

    rows = [
        row(
            "TerminalLeafImported",
            terminal_synced,
            False,
            "上一层已把非递归核表回流到 canonical-lock 或 noncanonical legal mode。",
            f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
        ),
        row(
            "NoncanonicalModeReducedToActualSourceBridge",
            noncanonical_to_bridge,
            False,
            "noncanonical legal mode 已过滤到实际源锁定或强化反原子。",
            ACTUAL_BRIDGE,
        ),
        row(
            "A1SourceAdmissionAbsorbed",
            source_admission_absorbed,
            True,
            "A1 canonical source admission 是 scoped 分支陈述，不能作为独立全局矛盾。",
            MOVING_ATOM,
        ),
        row(
            "MovingAtomEqualsExactEntropy",
            moving_to_entropy,
            False,
            "actual clean-core moving atom 排斥等价于 exact source entropy 标准形。",
            EXACT_ENTROPY,
        ),
        row(
            "ExactEntropySupportSpineImported",
            entropy_to_support and support_to_seed_energy,
            False,
            "登记乘子与初等支撑能量引理已闭合；剩余是无环 seed 和独立 pair 能量界。",
            f"{ACYCLIC_SEED} AND {PAIR_ENERGY}",
        ),
        row(
            "NonrecursivePairEnergyGuardClosed",
            nonrecursive_energy_guard,
            False,
            "pair 能量界不能用 moving-atom/source-entropy 目标自身证明，必须独立给出。",
            PAIR_ENERGY,
        ),
        row(
            "StableShortReturnDirectLemmaOnly",
            stable_direct_schema_only,
            False,
            "短同标签复现的 CRT 矛盾已闭合，但早期零行强制复现/缺陷只到 schema 准入，终端排斥仍开放。",
            f"{PHASE_DEFECT} OR terminal exclusion",
        ),
        row(
            "SignedSourceDrilldownIsFixedPoint",
            signed_source_recycles,
            False,
            "从 source-domain entropy 攻 signed row law 会回到 signed-source 固定点，不能算独立能量证明。",
            f"{SIGNED_SOURCE_CYCLE_GUARD} OR {PAIR_ENERGY}",
        ),
        row(
            "CanonicalLockStillParallel",
            True,
            False,
            "canonical-lock 仍可作为替代，但必须提交同集推前、有限因子图和无 noncanonical payload 残留。",
            CANONICAL_LOCK,
        ),
        row(
            "RatePreservationStillParallel",
            False,
            False,
            "moving-atom packet 的 log-power 速率保持未由本同步证明。",
            RATE,
        ),
        row(
            "DStructureGateStillOpen",
            dstructure_open,
            False,
            "DStructure/Rankin 晋级门仍未独立接受。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "当前只完成最新硬点同步；尚未证明 canonical-lock 或独立 pair 能量界，也未完成 DStructure/Rate。",
            f"({CANONICAL_LOCK} OR ({ACYCLIC_SEED} AND {PAIR_ENERGY})) AND {RATE} AND {DSTRUCTURE}",
        ),
    ]

    strict_basis = f"({CANONICAL_LOCK} OR ({ACYCLIC_SEED} AND {PAIR_ENERGY})) AND {RATE} AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_strict_latest_self_contained_hardpoint_sync_router",
        "status": "latest_self_contained_hardpoint_synced_pair_energy_or_canonical_lock_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "sync_closed": sync_closed,
        "stable_short_return_admission_schema_closed": stable_schema.get("stable_short_return_or_defect_admission_schema_closed") is True,
        "stable_short_return_terminal_exclusion_proved": False,
        "signed_source_route_is_fixed_point": signed_source_recycles,
        "independent_exact_pair_l2_or_max_atom_bound_proved": False,
        "acyclic_precauchy_seed_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": PAIR_ENERGY,
        "parallel_alternative": CANONICAL_LOCK,
        "strict_active_basis_after_sync": strict_basis,
        "compression_chain": chain(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            "宽终端二选一继续精确化后，noncanonical 分支回到 actual clean-core exact source entropy；"
            f"该熵定理的非递归证明不能走 signed-source 固定点，必须提交 `{ACYCLIC_SEED}` "
            f"和独立的 `{PAIR_ENERGY}`。短复现路线只关闭了 CRT 矛盾引理与相位缺陷准入，"
            "没有排斥终端家族。"
        ),
        "plain_conclusion": (
            "本步同步当前最新自足硬点：能直接触发矛盾的短复现引理已闭合，但强制复现/缺陷仍只到命名准入；"
            "source-domain signed row 下钻会回到 signed-source 固定点。因此当前真正非循环数学输入是"
            f"`{PAIR_ENERGY}`，其对象前提是 `{ACYCLIC_SEED}`；并行替代仍是 canonical-lock。"
            "这些均未证明，行/列命题仍未无条件自足闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 最新自足硬点同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sync_closed={fmt_bool(result['sync_closed'])}",
        f"stable_short_return_admission_schema_closed={fmt_bool(result['stable_short_return_admission_schema_closed'])}",
        f"stable_short_return_terminal_exclusion_proved={fmt_bool(result['stable_short_return_terminal_exclusion_proved'])}",
        f"signed_source_route_is_fixed_point={fmt_bool(result['signed_source_route_is_fixed_point'])}",
        f"independent_exact_pair_l2_or_max_atom_bound_proved={fmt_bool(result['independent_exact_pair_l2_or_max_atom_bound_proved'])}",
        f"acyclic_precauchy_seed_proved={fmt_bool(result['acyclic_precauchy_seed_proved'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"rate_preservation_ledger_proved={fmt_bool(result['rate_preservation_ledger_proved'])}",
        f"dstructure_independent_gate_closed={fmt_bool(result['dstructure_independent_gate_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 压缩链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["compression_chain"]:
        lines.append(
            "| {from_} | {to} |".format(
                from_=table_cell(item["from"]),
                to=table_cell(item["to"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前严格活动基",
            "",
            "```text",
            result["strict_active_basis_after_sync"],
            "```",
            "",
            "下一主攻点：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行替代：",
            "",
            "```text",
            result["parallel_alternative"],
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
