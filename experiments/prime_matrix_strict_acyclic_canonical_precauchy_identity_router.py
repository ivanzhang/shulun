#!/usr/bin/env python3
"""生成 strict acyclic canonical pre-Cauchy 系数身份账本路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_canonical_precauchy_identity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-canonical-precauchy-identity-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-canonical-precauchy-identity-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-canonical-precauchy-identity-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-canonical-branch-admission-timeline-router.json",
    "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json",
    "prime-matrix-triad-a1-source-lock-contract-router.json",
    "prime-matrix-triad-a1-canonical-branch-admission-router.json",
    "prime-matrix-strict-acyclic-seed-canonical-embedding-router.json",
    "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
    "prime-matrix-canonical-source-self-contained-final-theorem-router.json",
    "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md",
]

TARGET = "AcyclicCanonicalPreCauchyCoefficientIdentityLedger"
SEED_EQUALITY = "AcyclicSeedToCanonicalT1CoefficientEqualityAndBranchKeyLock"
ACTUAL_SOURCE = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def build_rows(
    timeline: dict[str, Any],
    provenance: dict[str, Any],
    source_lock: dict[str, Any],
    branch_admission: dict[str, Any],
    seed_embedding: dict[str, Any],
    canonical_exit: dict[str, Any],
    branch_absorb: dict[str, Any],
    source_loop: dict[str, Any],
    actual_seed: dict[str, Any],
    windowed_dls: dict[str, Any],
    canonical_final: dict[str, Any],
    kze_text: str,
) -> list[dict[str, Any]]:
    """生成 strict acyclic canonical pre-Cauchy 身份账本判定表。"""
    canonical_formula_declared = "lambda_c := canonical RIW/Buchstab" in kze_text
    return [
        row(
            "TimelineGuardImported",
            timeline.get("canonical_branch_admission_timeline_guard_closed") is True,
            True,
            "上一层已确认 canonical admission 是 T1 时间线门，不能由 terminal/payment/PDEC 倒推。",
            TARGET,
        ),
        row(
            "CanonicalT1CoefficientFormulaAvailableScoped",
            provenance.get("actual_source_provenance_closed") is True
            and canonical_formula_declared,
            True,
            "canonical RIW/Buchstab source branch 内，T1 系数公式和 provenance 已闭合。",
            "这只证明 canonical 分支自身，不证明 acyclic seed 属于该分支。",
        ),
        row(
            "SourceLockClosedOnlyAfterBranchMembership",
            source_lock.get("source_lock_contract_closed_for_canonical_branch") is True,
            True,
            "source lock 对 canonical 分支是定义性闭合；但入口条件是当前对象已被证明是 canonical branch。",
            SEED_EQUALITY,
        ),
        row(
            "A1BranchAdmissionStillContractOpen",
            branch_admission.get("canonical_branch_statement_adopted") is False
            or branch_admission.get("original_clean_object_covered_by_branch_split") is False,
            False,
            "A1 准入材料仍把 generic/noncanonical complement 分出去，未证明 strict acyclic seed 自动进入 canonical 分支。",
            "A1CanonicalSourceBranchStatementAndCoverage。",
        ),
        row(
            "SeedEmbeddingRequiresPointwiseT1Equality",
            seed_embedding.get("acyclic_seed_canonical_branch_admission_proved") is False,
            False,
            "有限因子嵌入不能只靠哈希稳定；必须证明 acyclic seed 的 T1 系数逐点等于 canonical RIW/Buchstab 系数。",
            SEED_EQUALITY,
        ),
        row(
            "NoTerminalDependentSelectionGuard",
            source_loop.get("circular_reverse_derivation_rejected") is True
            or source_loop.get("source_loop_cut_closed") is True,
            True,
            "若 branch key、权重或符号依赖 terminal payment/PDEC 结果，则它不是 T1 canonical 系数，而是循环来源或 noncanonical payload。",
            "需要 branch-key lock 与 terminal-independence。",
        ),
        row(
            "CanonicalFinalTheoremScopedNotGlobal",
            canonical_final.get("canonical_source_self_contained_theorem_closed") is True
            and canonical_final.get("global_unrestricted_terminal_family_exclusion_closed") is False,
            True,
            "canonical-source 自足闭合若可用，也只覆盖已证明进入 canonical-source 边界的对象。",
            "不能替代 acyclic seed-to-canonical equality。",
        ),
        row(
            "CanonicalExactPromotionStillMissingSeedClause",
            canonical_exit.get("acyclic_seed_canonical_branch_admission_proved") is False,
            False,
            "五项 exact same-set promotion 的第一项仍未证；缺 seed equality 时后四项不能启动。",
            canonical_exit.get("canonical_exact_certificate_definition", TARGET),
        ),
        row(
            "BranchAbsorptionDichotomyImported",
            branch_absorb.get("canonical_lock_branch_absorption_closed") is True,
            True,
            "若 seed equality 成立，该 case 被吸收到 canonical scoped promotion；若不成立，canonical-lock 不可用。",
            ACTUAL_SOURCE,
        ),
        row(
            "ActualSeedLaneSeparated",
            actual_seed.get("acyclic_pre_cauchy_noncanonical_primitive_source_seed_proved")
            is not True,
            True,
            "actual/noncanonical source seed 即使以后证明，也不是 canonical equality；它进入源熵或 ExactUV 支撑主线。",
            ACTUAL_SOURCE,
        ),
        row(
            "CleanDLSFallbackRemainsOpen",
            windowed_dls.get("acyclic_windowed_kloosterman_dls_internal_estimate_proved")
            is False,
            False,
            "若 residual 是 clean diffuse 而非 canonical seed，解析出口仍是 acyclic windowed DLS/CleanKLS。",
            WINDOWED_DLS,
        ),
        row(
            "AcyclicCanonicalPreCauchyIdentityLedgerCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交 acyclic seed 与 canonical T1 系数的逐点恒等式及 branch key 锁定。",
            f"{SEED_EQUALITY} OR {ACTUAL_SOURCE} OR {WINDOWED_DLS}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 strict acyclic canonical pre-Cauchy 身份账本路由证书。"""
    timeline = load_json(DOCS / "prime-matrix-strict-canonical-branch-admission-timeline-router.json")
    provenance = load_json(DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json")
    source_lock = load_json(DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json")
    branch_admission = load_json(DOCS / "prime-matrix-triad-a1-canonical-branch-admission-router.json")
    seed_embedding = load_json(DOCS / "prime-matrix-strict-acyclic-seed-canonical-embedding-router.json")
    canonical_exit = load_json(
        DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
    )
    branch_absorb = load_json(DOCS / "prime-matrix-strict-canonical-lock-branch-absorption-router.json")
    source_loop = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")
    actual_seed = load_json(DOCS / "prime-matrix-strict-actual-source-support-seed-router.json")
    windowed_dls = load_json(DOCS / "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")
    canonical_final = load_json(DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json")
    kze_text = read_text(DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md")

    rows = build_rows(
        timeline=timeline,
        provenance=provenance,
        source_lock=source_lock,
        branch_admission=branch_admission,
        seed_embedding=seed_embedding,
        canonical_exit=canonical_exit,
        branch_absorb=branch_absorb,
        source_loop=source_loop,
        actual_seed=actual_seed,
        windowed_dls=windowed_dls,
        canonical_final=canonical_final,
        kze_text=kze_text,
    )
    terminal_after = f"{SEED_EQUALITY} OR {ACTUAL_SOURCE} OR {WINDOWED_DLS}"

    return {
        "certificate_type": "prime_matrix_strict_acyclic_canonical_precauchy_identity_router",
        "status": "acyclic_canonical_precauchy_identity_reduced_to_seed_to_canonical_t1_equality_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "identity_ledger_boundary_refined": True,
        "canonical_t1_coefficient_formula_available_scoped": (
            provenance.get("actual_source_provenance_closed") is True
            and "lambda_c := canonical RIW/Buchstab" in kze_text
        ),
        "source_lock_closed_only_after_branch_membership": True,
        "downstream_terminal_selection_rejected": True,
        "acyclic_seed_to_canonical_t1_coefficient_equality_proved": False,
        "acyclic_seed_branch_key_lock_proved": False,
        "acyclic_seed_terminal_independence_proved": False,
        "acyclic_canonical_precauchy_coefficient_identity_ledger_proved": False,
        "acyclic_seed_canonical_branch_admission_before_cauchy_proved": False,
        "acyclic_canonical_exact_same_set_promotion_certificate_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "acyclic_windowed_kloosterman_dls_internal_estimate_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": TARGET,
        "terminal_gap_after_router": terminal_after,
        "next_direct_attack_target": SEED_EQUALITY,
        "parallel_attack_targets": [ACTUAL_SOURCE, WINDOWED_DLS, DSTRUCTURE],
        "closed_scoped_canonical_part": (
            "Canonical RIW/Buchstab T1 coefficient formula and provenance are closed inside the canonical branch."
        ),
        "open_acyclic_membership_part": (
            "The strict acyclic seed generated by the early-zero counterexample chain has not been proved "
            "pointwise equal to that canonical T1 coefficient with the same branch key and no terminal-dependent selection."
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`AcyclicCanonicalPreCauchyCoefficientIdentityLedger` 不是完全空白：canonical RIW/Buchstab 分支内的 "
            "T1 系数公式和 provenance 已有 scoped 闭合。真正缺口是 strict acyclic seed 的成员身份："
            "必须证明它在 T1 逐点等于 canonical 系数，并锁定同一 branch key，且不依赖 terminal payment、PDEC/SAE "
            "或后验投影。当前语料没有该恒等式，因此 canonical-lock 不能作为无条件闭合出口；若该恒等式成立，"
            "只得到 canonical scoped promotion；若不成立，必须回到 actual-source 熵定理或 acyclic windowed DLS。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic canonical pre-Cauchy 身份账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"identity_ledger_boundary_refined={fmt_bool(result['identity_ledger_boundary_refined'])}",
        f"canonical_t1_coefficient_formula_available_scoped={fmt_bool(result['canonical_t1_coefficient_formula_available_scoped'])}",
        f"acyclic_seed_to_canonical_t1_coefficient_equality_proved={fmt_bool(result['acyclic_seed_to_canonical_t1_coefficient_equality_proved'])}",
        f"acyclic_seed_branch_key_lock_proved={fmt_bool(result['acyclic_seed_branch_key_lock_proved'])}",
        f"acyclic_canonical_precauchy_coefficient_identity_ledger_proved={fmt_bool(result['acyclic_canonical_precauchy_coefficient_identity_ledger_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 账本拆分",
        "",
        "已闭合的 scoped canonical 部分：",
        "",
        "```text",
        result["closed_scoped_canonical_part"],
        "```",
        "",
        "仍开放的 strict acyclic 成员身份部分：",
        "",
        "```text",
        result["open_acyclic_membership_part"],
        "```",
        "",
        "因此攻击前后为：",
        "",
        "```text",
        f"{result['terminal_gap_before_router']}",
        "  ->",
        f"{result['terminal_gap_after_router']}",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "该目标必须给出逐点 T1 系数恒等式与 branch-key 锁。若只能从下游 payment 或 terminal defect 识别 branch，则不满足 pre-Cauchy 身份账本。",
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
