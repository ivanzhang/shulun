#!/usr/bin/env python3
"""同步 strict actual-source 反原子到 ExactUV/终端家族的最窄剩余。

用法示例：
  python3 experiments/prime_matrix_strict_actual_source_antiatom_exactuv_terminal_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json
  docs/monograph/prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.md"

SOURCE_AXIOM = "AddStrengthenedActualSourceAntiAtomTheorem"
EXACT_UV = "ActualNoncanonicalExactUVSupportLowerBound"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
DIRECT_PDEC = "DirectAcyclicSameSetPDECCapDualCertificate"
DIRECT_CLEAN = "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
EXTERNAL_FULLS = "FullSNonAPWFDKLSTheoremInput_OR_DIBFIPrimarySourceSpecializationProof"

SOURCE_FILES = [
    "prime-matrix-strict-strengthened-antiatom-direct-attack-router.json",
    "prime-matrix-final-open-input-direct-attack-router.json",
    "prime-matrix-registered-capacity-multiplier-discipline-router.json",
    "prime-matrix-exact-uv-support-terminal-attack-router.json",
    "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json",
    "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json",
    "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.json",
    "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json",
    "prime-matrix-strict-acyclic-terminal-family-attack-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-acyclic-clean-kls-router.json",
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
    """记录证据哈希。"""
    result = {"script": sha256(Path(__file__).resolve())}
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


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """从上游证据生成同步判定表。"""
    antiatom = data["antiatom"]
    final_direct = data["final_direct"]
    multiplier = data["multiplier"]
    exact_uv = data["exact_uv"]
    entropy_direct = data["entropy_direct"]
    nonrecursive = data["nonrecursive"]
    pair_mass = data["pair_mass"]
    seed_fusion = data["seed_fusion"]
    terminal_attack = data["terminal_attack"]
    direct_pdec = data["direct_pdec"]
    clean_kls = data["clean_kls"]

    antiatom_active = (
        antiatom.get("new_actual_source_axiom_required") is True
        and antiatom.get("strengthened_actual_source_antiatom_proved") is False
    )
    source_to_exactuv = (
        final_direct.get("source_axiom_before_attack") == SOURCE_AXIOM
        and final_direct.get("self_contained_source_input_after_attack") == EXACT_UV
        and final_direct.get("final_open_input_proved_or_accepted") is False
    )
    multiplier_closed = (
        multiplier.get("registered_capacity_multiplier_discipline_closed") is True
        and multiplier.get("remaining_source_microinput") == EXACT_UV
    )
    exactuv_unique_open = (
        exact_uv.get("unique_source_terminal_input") == EXACT_UV
        and exact_uv.get("exact_uv_support_proved") is False
    )
    support_spine_imported = (
        entropy_direct.get("internal_proof_spine_for_new_actual_source_entropy")
        == "RegisteredCapacityMultiplierDiscipline AND ActualNoncanonicalExactUVSupportLowerBound"
    )
    nonrecursive_guard = (
        nonrecursive.get("nonrecursive_guard_closed") is True
        and nonrecursive.get("independent_exact_pair_l2_or_max_atom_bound_proved") is False
    )
    pair_mass_not_terminal = (
        pair_mass.get("pair_mass_dispersion_not_separate_terminal") is True
        and pair_mass.get("clean_core_moving_atom_exclusion_proved") is False
    )
    seed_removed = (
        seed_fusion.get("acyclic_pre_cauchy_seed_independent_input_removed") is True
        and seed_fusion.get("terminal_gap_after_router") == TERMINAL_FAMILY
    )
    terminal_three_atoms = (
        terminal_attack.get("terminal_gap_after_router")
        == f"{CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}"
        and terminal_attack.get("strict_terminal_family_proved") is False
    )
    pdec_scope_open = (
        direct_pdec.get("scope_audit_closed") is True
        and direct_pdec.get("direct_acyclic_same_set_pdec_cap_dual_certificate_proved") is False
    )
    clean_dls_open = (
        clean_kls.get("acyclic_windowed_kloosterman_dls_internal_estimate_proved") is False
        and clean_kls.get("direct_acyclic_clean_kls_dls_proved") is False
    )

    return [
        row(
            "StrengthenedActualSourceAntiAtomActive",
            antiatom_active,
            False,
            "上一轮已确认 actual-source 强化反原子仍是新增源定理，不是已证结论。",
            SOURCE_AXIOM,
        ),
        row(
            "SourceAxiomReducedToExactUVSupport",
            source_to_exactuv and multiplier_closed,
            False,
            "乘子纪律闭合后，actual-source 强化反原子的大部分成本被压到 actual noncanonical ExactUV 支撑下界。",
            EXACT_UV,
        ),
        row(
            "ExactUVUniqueSourceInputStillOpen",
            exactuv_unique_open,
            False,
            "ExactUVSupport 是当前唯一源侧终端输入，但还没有证明。",
            EXACT_UV,
        ),
        row(
            "ExactUVSupportSpineImported",
            support_spine_imported,
            False,
            "新 actual-source 熵定理内部脊柱已对齐为乘子纪律加 ExactUV 支撑。",
            EXACT_UV,
        ),
        row(
            "NonrecursivePairEnergyGuardClosed",
            nonrecursive_guard,
            False,
            "不能用源熵/ moving-atom 结论反过来证明 pair-mass；必须给独立能量界或命名回流。",
            "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed",
        ),
        row(
            "PairMassNotSeparateTerminal",
            pair_mass_not_terminal,
            True,
            "pair-mass 分散失败就是同 formal unit 的 moving atom 失败，不是第三个新终端。",
            "ActualNoncanonicalCleanCoreMovingAtomExclusion",
        ),
        row(
            "AcyclicSeedIndependentInputRemoved",
            seed_removed,
            True,
            "seed 存在/不存在两支均回到 acyclic terminal family，因此 seed 不再作为独立输入。",
            TERMINAL_FAMILY,
        ),
        row(
            "AcyclicTerminalFamilyReducedToThreeAtoms",
            terminal_three_atoms,
            False,
            "源侧下钻已经回到 strict acyclic 终端家族三原子：canonical-lock、direct PDEC、direct CleanKLS。",
            f"{CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}",
        ),
        row(
            "DirectPDECScopeAuditOpen",
            pdec_scope_open,
            False,
            "direct same-set PDEC 的协议可用，但 acyclic/noncanonical 与 canonical 同集作用域匹配未证明。",
            CANONICAL_LOCK,
        ),
        row(
            "DirectCleanDLSAtomOpen",
            clean_dls_open,
            False,
            "clean KLS/DLS 已压到窗口化 Kloosterman/DLS 内部估计，但该估计未证明。",
            WINDOWED_DLS,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本同步只把 actual-source 反原子线压回终端家族；没有证明三原子、ExactUV 或 DStructure/Rankin。",
            f"({CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}) AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "antiatom": load_json("prime-matrix-strict-strengthened-antiatom-direct-attack-router.json"),
        "final_direct": load_json("prime-matrix-final-open-input-direct-attack-router.json"),
        "multiplier": load_json("prime-matrix-registered-capacity-multiplier-discipline-router.json"),
        "exact_uv": load_json("prime-matrix-exact-uv-support-terminal-attack-router.json"),
        "entropy_direct": load_json("prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json"),
        "nonrecursive": load_json("prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json"),
        "pair_mass": load_json("prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.json"),
        "seed_fusion": load_json("prime-matrix-strict-acyclic-seed-terminal-fusion-router.json"),
        "terminal_attack": load_json("prime-matrix-strict-acyclic-terminal-family-attack-router.json"),
        "direct_pdec": load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"),
        "clean_kls": load_json("prime-matrix-strict-acyclic-clean-kls-router.json"),
    }
    rows = build_rows(data)
    boundary_closed = all(item["closed"] for item in rows[:-1])
    latest_basis = (
        f"({CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN} OR {EXTERNAL_FULLS}) "
        f"AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_strict_actual_source_antiatom_exactuv_terminal_sync_router",
        "status": (
            "strict_actual_source_antiatom_synced_to_acyclic_terminal_family_open"
            if boundary_closed
            else "strict_actual_source_antiatom_exactuv_terminal_sync_incomplete"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "actual_source_antiatom_to_terminal_sync_boundary_closed": boundary_closed,
        "strengthened_actual_source_antiatom_proved": False,
        "actual_exact_uv_support_proved": False,
        "strict_terminal_family_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "source_axiom_before_sync": SOURCE_AXIOM,
        "exact_uv_middle_input": EXACT_UV,
        "self_contained_terminal_after_sync": (
            f"{CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}"
        ),
        "latest_conditional_basis_after_sync": latest_basis,
        "next_primary_target": CANONICAL_LOCK,
        "next_parallel_target": WINDOWED_DLS,
        "external_fallback": EXTERNAL_FULLS,
        "rows": rows,
        "source_hashes": source_hashes(),
        "sync_formula": (
            f"{SOURCE_AXIOM} -> {EXACT_UV} -> nonrecursive pair-energy guard "
            f"-> seed branch fusion -> {TERMINAL_FAMILY} -> "
            f"({CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN})."
        ),
        "plain_conclusion": (
            "本轮把 actual-source 强化反原子继续下钻到底层接口：它经已闭合的容量乘子纪律压到 "
            "ActualNoncanonicalExactUVSupportLowerBound；ExactUV 的非递归 pair-energy 证明不能循环使用"
            "源熵目标；pair-mass 失败不是新终端，而是 moving atom；seed 存在/不存在两支又统一回到 "
            "strict acyclic 终端家族。因此当前最窄自足剩余不再是 source anti-atom 大名，而是 "
            "acyclic 终端家族三原子。三原子和 DStructure/Rankin 仍未证明，行/列命题未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict actual-source 反原子到终端家族同步证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "actual_source_antiatom_to_terminal_sync_boundary_closed",
        "strengthened_actual_source_antiatom_proved",
        "actual_exact_uv_support_proved",
        "strict_terminal_family_proved",
        "direct_unconditional_contradiction_found",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 同步公式")
    lines.append("")
    lines.append("```text")
    lines.append(result["sync_formula"])
    lines.append("```")
    lines.append("")
    lines.append("## 2. 判定表")
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
    lines.append("## 3. 最新最窄剩余")
    lines.append("")
    lines.append("```text")
    lines.append(result["self_contained_terminal_after_sync"])
    lines.append("```")
    lines.append("")
    lines.append("首攻点：")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_target"])
    lines.append("```")
    lines.append("")
    lines.append("并行保留：")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_parallel_target"])
    lines.append("```")
    lines.append("")
    lines.append("条件外部基：")
    lines.append("")
    lines.append("```text")
    lines.append(result["latest_conditional_basis_after_sync"])
    lines.append("```")
    lines.append("")
    lines.append("审稿边界：本文件只同步并压缩 actual-source 反原子线；没有证明终端三原子、ExactUV、外部谱输入或 DStructure/Rankin。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"actual_source_antiatom_to_terminal_sync_boundary_closed={fmt_bool(result['actual_source_antiatom_to_terminal_sync_boundary_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"wrote={OUT_JSON.relative_to(ROOT)}")
    print(f"wrote={OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
