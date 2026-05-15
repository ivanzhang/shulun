#!/usr/bin/env python3
"""审计 z=61 low-alpha 固定核心回流闭环账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_fixed_core_cycle_ledger_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-ledger-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-ledger-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-ledger-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-ledger-router.md"

CHAIN = [
    {
        "name": "positive_lift_carry_to_signed_sum",
        "file": "prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-to-signed-sum-bridge-router.json",
        "closed_key": "positive_lift_carry_to_signed_sum_bridge_closed_for_sample",
        "next": "FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC",
    },
    {
        "name": "signed_sum_residue_gate",
        "file": "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json",
        "closed_key": "all_signed_sum_residue_gates_closed",
        "next": "FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC",
    },
    {
        "name": "dominant_peel",
        "file": "prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json",
        "closed_key": "all_dominant_peels_closed",
        "next": "DominantPeelSignedSumGlobalBoundOrPeelPDEC",
    },
    {
        "name": "terminal_sign_forcing",
        "file": "prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.json",
        "closed_key": "all_terminal_sign_forcings_closed",
        "next": "TerminalSignForcingGlobalBoundOrTerminalPDEC",
    },
    {
        "name": "branch_decision_ledger",
        "file": "prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json",
        "closed_key": "branch_decision_ledger_closed",
        "next": "GlobalBranchDecisionPatternBoundOrBranchDecisionPDEC",
    },
    {
        "name": "branch_decision_margin",
        "file": "prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.json",
        "closed_key": "branch_decision_margin_stability_proved_for_formal_unit",
        "next": "BranchDecisionMarginStabilityGlobalBoundOrMarginPDEC",
    },
    {
        "name": "margin_pdec_registration",
        "file": "prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.json",
        "closed_key": "margin_pdec_registration_closed",
        "next": "GlobalNoMarginCollapseOrMarginPDECExclusion",
    },
    {
        "name": "nearest_margin_collision",
        "file": "prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.json",
        "closed_key": "offset55_collision_pattern_closed_for_formal_unit",
        "next": "Offset55MarginCollisionExclusionOrOffsetPDEC",
    },
    {
        "name": "offset55_halfmod_flip",
        "file": "prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.json",
        "closed_key": "offset55_halfmod_flip_closed_for_formal_unit",
        "next": "HalfModulusFlipSeparationGlobalBoundOrHalfFlipPDEC",
    },
    {
        "name": "halfmod_factor_separation",
        "file": "prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.json",
        "closed_key": "halfmod_factor_separation_closed_for_formal_unit",
        "next": "HalfModulusFlipFactorSeparationGlobalBoundOrFactorPDEC",
    },
    {
        "name": "gap3_crt_structure",
        "file": "prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.json",
        "closed_key": "gap3_crt_structure_closed_for_formal_unit",
        "next": "GapThreeCRTStructureGlobalBoundOrGapPDEC",
    },
    {
        "name": "half_residue_gap_source",
        "file": "prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.json",
        "closed_key": "gap_source_closed_for_formal_unit",
        "next": "HalfResidueGapSourceGlobalBoundOrGapSourcePDEC",
    },
    {
        "name": "core_factor_residue_identity",
        "file": "prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.json",
        "closed_key": "core_factor_residue_identity_closed_for_formal_unit",
        "next": "CoreFactorResidueIdentityGlobalBoundOrCoreFactorPDEC",
    },
    {
        "name": "core_quotient_lock",
        "file": "prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.json",
        "closed_key": "quotient_lock_unique_positive_integer_solution_proved",
        "next": "CoreQuotientLockGlobalExclusionOrQuotientLockPDEC",
    },
    {
        "name": "quotient_lock_pdec_registration",
        "file": "prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.json",
        "closed_key": "quotient_lock_pdec_registration_closed",
        "next": "QuotientLockPDECExclusionByFixedCoreCheckOrGlobalTemplateBound",
    },
    {
        "name": "quotient_lock_fixed_core_bridge",
        "file": "prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.json",
        "closed_key": "quotient_lock_fixed_core_bridge_closed_for_sample",
        "next": "FixedCoreDyadicAbsorberGlobalizationOrPersistentPhasePDEC",
    },
    {
        "name": "fixed_core_dyadic_balance",
        "file": "prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json",
        "closed_key": "fixed_core_dyadic_balance_lemma_closed_for_sample",
        "next": "PositiveDyadicLiftExistenceForFixedCoreOrMissingLiftPDEC",
    },
    {
        "name": "positive_lift_shifted_pair",
        "file": "prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json",
        "closed_key": "positive_lift_shifted_pair_bridge_closed_for_sample",
        "next": "ShiftedSquareWindowGlobalBoundOrMissingLiftPDEC",
    },
    {
        "name": "positive_lift_root_selector",
        "file": "prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.json",
        "closed_key": "positive_lift_root_selector_bridge_closed_for_sample",
        "next": "CRTRootIntegralSelectorGlobalBoundOrMissingLiftPDEC",
    },
    {
        "name": "positive_lift_factor_gate",
        "file": "prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.json",
        "closed_key": "positive_lift_factor_gate_bridge_closed_for_sample",
        "next": "PrimeFactorLiftGateGlobalBoundOrMissingLiftPDEC",
    },
    {
        "name": "positive_lift_projection_gate",
        "file": "prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.json",
        "closed_key": "positive_lift_projection_gate_bridge_closed_for_sample",
        "next": "RootProjectionGateGlobalBoundOrMissingLiftPDEC",
    },
    {
        "name": "positive_lift_signed_projection",
        "file": "prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.json",
        "closed_key": "positive_lift_signed_projection_bridge_closed_for_sample",
        "next": "SignedCRTSupportCarryBoundOrMissingLiftPDEC",
    },
    {
        "name": "positive_lift_carry_layer",
        "file": "prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.json",
        "closed_key": "positive_lift_carry_layer_bridge_closed_for_sample",
        "next": "CarryLayerTargetFiberGlobalBoundOrMissingLiftPDEC",
    },
]

NEXT_TARGET = "FixedCoreCycleNonPersistenceOrPersistentPhasePDEC"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str) -> dict[str, Any]:
    """读取命名 JSON。"""
    return json.loads((DOCS / name).read_text(encoding="utf-8"))


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_fixed_core_cycle_ledger_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for item in CHAIN:
        path = DOCS / item["file"]
        result[f"docs/monograph/{item['file']}"] = file_sha256(path)
    return result


def chain_rows(certificates: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """整理闭环链上每个证书的闭合状态。"""
    rows = []
    for index, item in enumerate(CHAIN, start=1):
        cert = certificates[item["name"]]
        rows.append(
            {
                "step": index,
                "name": item["name"],
                "certificate_type": cert["certificate_type"],
                "status": cert["status"],
                "closed_key": item["closed_key"],
                "closed": bool(cert.get(item["closed_key"])),
                "same_theorem_target_preserved": bool(cert.get("same_theorem_target_preserved")),
                "no_theorem_switch": bool(cert.get("no_theorem_switch")),
                "row_column_unconditional_closed": bool(cert.get("row_column_unconditional_closed")),
                "next_direct_attack_target": cert.get("next_direct_attack_target"),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行固定核心回流闭环审计。"""
    certificates = {item["name"]: load(item["file"]) for item in CHAIN}
    rows = chain_rows(certificates)

    signed_sum = certificates["signed_sum_residue_gate"]["signed_sum_rows"][0]
    branch = certificates["branch_decision_ledger"]
    offset = certificates["offset55_halfmod_flip"]
    quotient_lock = certificates["core_quotient_lock"]
    quotient_registration = certificates["quotient_lock_pdec_registration"]
    fixed_core_bridge = certificates["quotient_lock_fixed_core_bridge"]
    dyadic = certificates["fixed_core_dyadic_balance"]
    carry = certificates["positive_lift_carry_layer"]
    carry_to_sum = certificates["positive_lift_carry_to_signed_sum"]

    target_triples = {
        (
            cert.get("target_bucket"),
            cert.get("target_omega"),
            cert.get("target_shell"),
        )
        for cert in certificates.values()
        if cert.get("target_bucket") is not None
    }
    local_chain_closed = all(row["closed"] for row in rows)
    no_theorem_switch = all(row["same_theorem_target_preserved"] and row["no_theorem_switch"] for row in rows)
    no_accidental_global_claim = not any(row["row_column_unconditional_closed"] for row in rows)

    # 核心回流同一性：signed-sum 唯一命中，经 quotient-lock 固定核心和 dyadic lift 后，
    # 返回同一个 carry/root/sign 三元组。
    fixed_core_identity_closed = (
        len(target_triples) == 1
        and signed_sum["modulus"] == carry["modulus"] == carry_to_sum["modulus"] == 57684
        and signed_sum["q2"] == carry["q2"] == carry_to_sum["q2"] == 71
        and signed_sum["q4"] == carry["q4"] == carry_to_sum["q4"] == 37
        and signed_sum["selected_residue"] == carry["selected_residue"] == carry_to_sum["selected_residue"] == 26951
        and signed_sum["selected_carry"] == carry["selected_carry"] == carry_to_sum["selected_carry"] == 6
        and signed_sum["selected_sign_word"]
        == carry["selected_sign_word"]
        == carry_to_sum["selected_sign_word"]
        == branch["selected_original_sign_word"]
        == "--++-"
        and branch["selected_peel_sign_word"] == offset["selected_peel_sign_word"] == "++---"
        and offset["flip_delta_equals_half_modulus"]
        and quotient_lock["quotient_lock_unique_positive_integer_solution_proved"]
        and quotient_registration["fixed_core_candidate_unique"]
        and fixed_core_bridge["quotient_lock_modulus_is_positive_lift_2B"]
        and dyadic["dyadic_positive_quotients"] == [2, 4]
        and carry["positive_lift_carry_layer_bridge_closed_for_sample"]
        and carry_to_sum["positive_lift_carry_to_signed_sum_bridge_closed_for_sample"]
    )

    cycle_materialized = local_chain_closed and no_theorem_switch and fixed_core_identity_closed

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_fixed_core_cycle_ledger_router",
        "status": "z61_positive_lift_signed_sum_reenters_fixed_core_dyadic_cycle_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_bucket": "unbalanced<=8",
        "target_omega": 4,
        "target_shell": "(8D,16D]",
        "chain_step_count": len(rows),
        "chain_rows": rows,
        "all_local_bridges_closed": local_chain_closed,
        "all_steps_preserve_same_theorem_target": no_theorem_switch,
        "no_accidental_global_closure_claim": no_accidental_global_claim,
        "target_triples": sorted(map(str, target_triples)),
        "modulus": 57684,
        "core": 4807,
        "core_factors": [11, 19, 23],
        "q2": 71,
        "q4": 37,
        "selected_residue": 26951,
        "selected_carry": 6,
        "selected_original_sign_word": "--++-",
        "selected_peel_sign_word": "++---",
        "selected_signed_sum": signed_sum["selected_signed_sum"],
        "halfmod_flip_delta": offset["flip_delta"],
        "halfmod_signed_separation": offset["signed_separation_mod_target"],
        "quotient_lock_unique_positive_integer_solution_proved": quotient_lock[
            "quotient_lock_unique_positive_integer_solution_proved"
        ],
        "fixed_core_candidate_unique": quotient_registration["fixed_core_candidate_unique"],
        "quotient_lock_modulus_is_positive_lift_2B": fixed_core_bridge[
            "quotient_lock_modulus_is_positive_lift_2B"
        ],
        "dyadic_positive_quotients": dyadic["dyadic_positive_quotients"],
        "cycle_returns_to_same_carry_signed_sum_gate": fixed_core_identity_closed,
        "z61_fixed_core_cycle_ledger_closed_for_formal_unit": cycle_materialized,
        "fixed_core_cycle_global_nonpersistence_proved": False,
        "persistent_phase_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "当前 z=61 low-alpha 剩余不是新的自由局部参数：positive-lift carry 纤维接入 "
            "five-term signed-sum 后，经 dominant peel、terminal forcing、branch margin、"
            "offset-55 halfmod、core quotient lock、固定核心 dyadic balance，又回到同一个 "
            "`--++- / carry=6 / r=26951` positive-lift carry 门。该账本闭合的是 formal-unit "
            "同一性；全局仍需证明固定核心回流不能持久，或排斥 PersistentPhase-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 fixed-core cycle ledger",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"chain_step_count={result['chain_step_count']}",
        f"all_local_bridges_closed={fmt_bool(result['all_local_bridges_closed'])}",
        f"cycle_returns_to_same_carry_signed_sum_gate={fmt_bool(result['cycle_returns_to_same_carry_signed_sum_gate'])}",
        f"z61_fixed_core_cycle_ledger_closed_for_formal_unit={fmt_bool(result['z61_fixed_core_cycle_ledger_closed_for_formal_unit'])}",
        f"fixed_core_cycle_global_nonpersistence_proved={fmt_bool(result['fixed_core_cycle_global_nonpersistence_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 闭环锚点",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| target | `{result['target_bucket']}, omega={result['target_omega']}, shell={result['target_shell']}` |",
        f"| core | `{result['core']}={result['core_factors']}` |",
        f"| M, q4, q2 | `{result['modulus']}, {result['q4']}, {result['q2']}` |",
        f"| selected root | `{result['selected_residue']}` |",
        f"| selected carry/sign | `{result['selected_carry']} / {result['selected_original_sign_word']}` |",
        f"| peel sign | `{result['selected_peel_sign_word']}` |",
        f"| selected signed sum | `{result['selected_signed_sum']}` |",
        f"| halfmod flip | `{result['halfmod_flip_delta']}`, separation `{result['halfmod_signed_separation']}` |",
        f"| dyadic positive quotients | `{result['dyadic_positive_quotients']}` |",
        "",
        "## 2. 链条账本",
        "",
        "| step | certificate | closed key | closed | next target |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for row in result["chain_rows"]:
        lines.append(
            f"| {row['step']} | `{row['name']}` | `{row['closed_key']}` | "
            f"{fmt_bool(row['closed'])} | `{row['next_direct_attack_target']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：当前 formal unit 的回流链条同一性，且没有引入新自由参数。",
            "- 未闭合：固定核心回流的全局非持久性，或 PersistentPhase-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_local_bridges_closed": result["all_local_bridges_closed"],
                "cycle_returns_to_same_carry_signed_sum_gate": result[
                    "cycle_returns_to_same_carry_signed_sum_gate"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
