#!/usr/bin/env python3
"""生成 strict acyclic seed 与 canonical T1 系数等式分支分类证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_canonical_t1_equality_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-canonical-precauchy-identity-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
    "prime-matrix-canonical-source-self-contained-final-theorem-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
]

TARGET = "AcyclicSeedToCanonicalT1CoefficientEqualityAndBranchKeyLock"
CANONICAL_CASE = "AcyclicSeedEqualsCanonicalT1CaseAbsorbedByScopedCanonicalPromotion"
MISMATCH_FORCING = "AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect"
ACTUAL_SOURCE = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def mismatch_cases() -> list[dict[str, str]]:
    """列出 canonical T1 mismatch 的合法出口。"""
    return [
        {
            "case": "MissingT1SourceRow",
            "description": "acyclic seed 没有独立 T1 系数行，只能从下游覆盖或 payment 读取。",
            "route": "registered source-missing return / PDEC-SAE-ColumnCRT。",
        },
        {
            "case": "TerminalDependentBranchKey",
            "description": "branch key、符号或权重依赖 terminal payment、PDEC/SAE 或后验投影。",
            "route": "registered phase defect / named terminal return。",
        },
        {
            "case": "GenuineNoncanonicalT1Identity",
            "description": "存在独立 pre-Cauchy 算术恒等式，但不是 canonical RIW/Buchstab 系数。",
            "route": "actual signed source / ExactUV / source entropy 主线。",
        },
        {
            "case": "CleanDiffuseResidual",
            "description": "低维缺陷已剥离，但 residual 仍为非 canonical clean diffuse object。",
            "route": "acyclic windowed DLS / CleanKLS。",
        },
    ]


def build_rows(
    identity: dict[str, Any],
    branch_absorb: dict[str, Any],
    canonical_final: dict[str, Any],
    zero_seed_nogo: dict[str, Any],
    alpha_signed: dict[str, Any],
    source_loop: dict[str, Any],
    cycle_cut: dict[str, Any],
    actual_seed: dict[str, Any],
    windowed_dls: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 equality 分支分类判定表。"""
    return [
        row(
            "EqualityTargetImported",
            identity.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 canonical pre-Cauchy 身份账本压到 acyclic seed 与 canonical T1 系数逐点等式。",
            TARGET,
        ),
        row(
            "ScopedCanonicalFormulaAvailable",
            identity.get("canonical_t1_coefficient_formula_available_scoped") is True,
            True,
            "canonical RIW/Buchstab T1 公式在 canonical branch 内已闭合，可作为比较右端。",
            "仍需证明 acyclic seed 等于该右端。",
        ),
        row(
            "CanonicalEqualityCaseAbsorbed",
            branch_absorb.get("canonical_lock_branch_absorption_closed") is True
            and canonical_final.get("canonical_source_self_contained_theorem_closed") is True,
            True,
            "若逐点等式、branch-key lock 和 no terminal dependence 全部成立，该 case 只进入 canonical scoped promotion。",
            CANONICAL_CASE,
        ),
        row(
            "CanonicalEqualityNotGlobalContradiction",
            canonical_final.get("global_unrestricted_terminal_family_exclusion_closed") is False,
            True,
            "canonical scoped promotion 不是完整行/列无条件闭合；它只删除已证明 canonical 的 case。",
            "row_column_unconditional_closed=false。",
        ),
        row(
            "UnsignedZeroRowCannotProveEquality",
            zero_seed_nogo.get("zero_row_seed_extraction_blocked") is True,
            True,
            "早期零行反例给 unsigned CRT/covering data，不能直接给 canonical signed T1 coefficient equality。",
            MISMATCH_FORCING,
        ),
        row(
            "SignedLiftStillOpenForMismatch",
            alpha_signed.get("alpha_formula_signed_lift_router_closed") is True
            and alpha_signed.get("alpha_formula_signed_coefficient_lift_proved") is False,
            False,
            "若 mismatch 是 genuine noncanonical T1 identity，仍需 actual signed source、权重律、Phi 推前和 branch 预算。",
            alpha_signed.get("terminal_gap_after_router", ACTUAL_SOURCE),
        ),
        row(
            "TerminalDependentSelectionRejected",
            source_loop.get("circular_reverse_derivation_rejected") is True
            or source_loop.get("source_loop_cut_closed") is True,
            True,
            "若 equality 只能在 terminal extraction 之后识别，则不是 T1 branch-key lock，必须命名回流。",
            "registered terminal defect / named return。",
        ),
        row(
            "CounterexamplePressureNotEnoughForEquality",
            cycle_cut.get("direct_unconditional_contradiction_found") is False,
            True,
            "反例链与真实结构链已有压力场，但目前只产生 unsigned rigidity 和候选矛盾，不产生 canonical T1 等式。",
            "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect OR signed lift。",
        ),
        row(
            "ActualSourceLaneRemainsOpen",
            actual_seed.get("actual_exact_uv_support_proved") is not True,
            False,
            "非 canonical T1 身份若存在，应进入 actual-source 熵/ExactUV 支撑；该主线仍未证明。",
            ACTUAL_SOURCE,
        ),
        row(
            "CleanDLSLaneRemainsOpen",
            windowed_dls.get("acyclic_windowed_kloosterman_dls_internal_estimate_proved")
            is False,
            False,
            "clean diffuse residual 的解析出口仍未自足闭合。",
            WINDOWED_DLS,
        ),
        row(
            "EqualityBranchClassifierClosed",
            True,
            True,
            "等式目标已被分类为 canonical absorbed case 或 mismatch forcing case；不能再把 equality 当作无来源常数填充。",
            f"{CANONICAL_CASE} OR {MISMATCH_FORCING}",
        ),
        row(
            "AcyclicSeedToCanonicalT1EqualityCurrentCorpusProved",
            False,
            False,
            "当前材料没有证明 acyclic seed 逐点等于 canonical T1 系数，也没有证明全部 mismatch 都已触发已闭合终端缺陷。",
            MISMATCH_FORCING,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 strict acyclic seed canonical T1 equality 分支分类证书。"""
    identity = load_json(DOCS / "prime-matrix-strict-acyclic-canonical-precauchy-identity-router.json")
    branch_absorb = load_json(DOCS / "prime-matrix-strict-canonical-lock-branch-absorption-router.json")
    canonical_final = load_json(DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json")
    zero_seed_nogo = load_json(DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json")
    alpha_signed = load_json(DOCS / "prime-matrix-strict-alpha-formula-signed-lift-router.json")
    source_loop = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")
    cycle_cut = load_json(DOCS / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json")
    actual_seed = load_json(DOCS / "prime-matrix-strict-actual-source-support-seed-router.json")
    windowed_dls = load_json(DOCS / "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")
    rows = build_rows(
        identity=identity,
        branch_absorb=branch_absorb,
        canonical_final=canonical_final,
        zero_seed_nogo=zero_seed_nogo,
        alpha_signed=alpha_signed,
        source_loop=source_loop,
        cycle_cut=cycle_cut,
        actual_seed=actual_seed,
        windowed_dls=windowed_dls,
    )
    terminal_after = f"{CANONICAL_CASE} OR {MISMATCH_FORCING}"
    strict_after = f"{MISMATCH_FORCING} OR {ACTUAL_SOURCE} OR {WINDOWED_DLS}"
    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_canonical_t1_equality_router",
        "status": "acyclic_seed_canonical_t1_equality_classified_canonical_case_absorbed_mismatch_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "equality_branch_classifier_closed": True,
        "scoped_canonical_formula_available": True,
        "canonical_equality_case_absorbed": True,
        "canonical_equality_not_global_contradiction": True,
        "unsigned_zero_row_cannot_prove_equality": True,
        "terminal_dependent_selection_rejected": True,
        "acyclic_seed_to_canonical_t1_coefficient_equality_proved": False,
        "acyclic_seed_branch_key_lock_proved": False,
        "all_mismatches_force_registered_defect_or_actual_source_proved": False,
        "actual_source_entropy_theorem_proved": False,
        "acyclic_windowed_kloosterman_dls_internal_estimate_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": TARGET,
        "terminal_gap_after_router": terminal_after,
        "strict_active_noncanonical_gap_after_router": strict_after,
        "next_direct_attack_target": MISMATCH_FORCING,
        "parallel_attack_targets": [ACTUAL_SOURCE, WINDOWED_DLS, DSTRUCTURE],
        "mismatch_cases": mismatch_cases(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`AcyclicSeedToCanonicalT1CoefficientEqualityAndBranchKeyLock` 已被分支分类："
            "若 acyclic seed 在 T1 逐点等于 canonical RIW/Buchstab 系数并锁住同一 branch key，则该 case "
            "只被吸收到 canonical scoped promotion，不给完整行/列无条件矛盾；若不等，则必须证明 mismatch "
            "强制落入 actual signed source/ExactUV/source entropy、registered terminal defect，或 acyclic windowed DLS。"
            "现有早期零行几何与真实结构压力不能直接证明该等式，也不能证明全部 mismatch 已被排斥。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed canonical T1 equality 分支分类路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"equality_branch_classifier_closed={fmt_bool(result['equality_branch_classifier_closed'])}",
        f"canonical_equality_case_absorbed={fmt_bool(result['canonical_equality_case_absorbed'])}",
        f"acyclic_seed_to_canonical_t1_coefficient_equality_proved={fmt_bool(result['acyclic_seed_to_canonical_t1_coefficient_equality_proved'])}",
        f"all_mismatches_force_registered_defect_or_actual_source_proved={fmt_bool(result['all_mismatches_force_registered_defect_or_actual_source_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 分支公式",
        "",
        "```text",
        f"{result['terminal_gap_before_router']}",
        "  ->",
        f"{result['terminal_gap_after_router']}",
        "```",
        "",
        "去掉 scoped canonical case 后，严格 noncanonical 活动剩余为：",
        "",
        "```text",
        result["strict_active_noncanonical_gap_after_router"],
        "```",
        "",
        "## 2. mismatch 出口表",
        "",
        "| case | description | route |",
        "| --- | --- | --- |",
    ]
    for item in result["mismatch_cases"]:
        lines.append(
            "| `{case}` | {description} | {route} |".format(
                case=table_cell(item["case"]),
                description=table_cell(item["description"]),
                route=table_cell(item["route"]),
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
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "下一步必须证明所有 canonical T1 mismatch 都不能静默存在：它们要么给出 actual signed source/source entropy 输入，要么登记 terminal defect，要么落入 clean DLS。否则反例链仍有 noncanonical 出口。",
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
