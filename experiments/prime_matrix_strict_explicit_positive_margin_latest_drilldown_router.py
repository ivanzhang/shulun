#!/usr/bin/env python3
"""生成 strict 显式正终端余量最新下钻同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_explicit_positive_margin_latest_drilldown_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json

输出：
  docs/monograph/prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json
  docs/monograph/prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json"
OUT_MD = DOCS / "prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.md"

POSITIVE_MARGIN = "ExplicitPositiveTerminalBudgetMarginInequality"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
NAMED_TABLE = "NamedReturnSameParameterDeductionTable"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
DIVISOR_CAP = "ScaledTerminalCoreDivisorWindowCountCap"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json",
    "prime-matrix-strict-positive-terminal-budget-margin-attack-router.json",
    "prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json",
    "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json",
    "prime-matrix-strict-rosser-floor-terminal-charge-router.json",
    "prime-matrix-strict-named-return-same-parameter-deduction-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json",
    "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json",
    "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json",
    "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json",
    "prime-matrix-strict-atomic-origin-identity-cycle-cut-sync-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取证书 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """记录依赖文件哈希，便于审稿复核。"""
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
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成显式正余量下钻判定表。"""
    latest = data["latest"]
    coupled = data["coupled"]
    concrete = data["concrete"]
    rosser = data["rosser"]
    named = data["named"]
    cold = data["cold"]
    sparse = data["sparse"]
    mult = data["multiplicity"]
    terminal = data["terminal"]
    pdec_scope = data["pdec_scope"]
    atomic = data["atomic"]

    positive_imported = latest.get("next_direct_attack_target") == POSITIVE_MARGIN
    coupled_schema = coupled.get("coupled_margin_schema_closed") is True
    candidate_row = concrete.get("candidate_parameter_row_generated") is True
    rosser_charged = rosser.get("sawtooth_failure_no_free_d0_loss_closed") is True
    named_schema = named.get("named_return_same_parameter_schema_closed") is True
    cold_discipline = (
        cold.get("cold_supply_upper_envelope_closed") is True
        and cold.get("same_parameter_lambda_schedule_closed") is True
    )
    sparse_formula = sparse.get("nonpersistent_sae_budget_formula_closed") is True
    divisor_reduced = mult.get("multiplicity_to_divisor_count_closed") is True
    terminal_saturated = terminal.get("strict_acyclic_terminal_family_proved") is False and (
        terminal.get("direct_clean_kls_returns_to_terminal") is True
    )
    pdec_saturated = pdec_scope.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
    moving_atom_next = atomic.get("next_direct_attack_target") == MOVING_ATOM

    return [
        row(
            "PositiveMarginFrontierImported",
            positive_imported,
            False,
            "最新前沿已把保标签商熵亏损同步为同参数正余量 D_prefix-E_named-U_cold>0。",
            POSITIVE_MARGIN,
        ),
        row(
            "CoupledMarginSchemaClosed",
            coupled_schema,
            coupled_schema,
            "D0、E0、U0、margin_delta 与 finite hash 的字段合同已列全。",
            "ConcreteSameParameterMarginTableCertificate",
        ),
        row(
            "ConcreteCandidateRowGenerated",
            candidate_row,
            False,
            "alpha=0.43, P>=100000 的同参数候选行已生成，但 D0/E0/U0 仍不是数值证书。",
            "fill D0/E0/U0 under same parameter_id",
        ),
        row(
            "RosserSawtoothFailureCharged",
            rosser_charged,
            False,
            "Rosser floor/sawtooth 失败不再是无名 D0 损失，已强制登记为同 formal unit 命名终端收费。",
            f"{FINITE_PREFIX} AND ({NAMED_TABLE} OR {TERMINAL_FAMILY})",
        ),
        row(
            "D0FinitePrefixHashStillAbsent",
            concrete.get("finite_boundary_hash_available") is False,
            False,
            "渐近或外部尾段不能替代有限边界 prefix 证书；没有 hash 就不能给全局 D0。",
            FINITE_PREFIX,
        ),
        row(
            "NamedReturnSameParameterSchemaClosed",
            named_schema,
            False,
            "E_named 只剩持久终端家族排斥与非持久预算吸收两类来源；schema 闭合但数值扣除未证。",
            f"{TERMINAL_FAMILY} AND {SPARSE_BUDGET}",
        ),
        row(
            "PersistentReturnReducedToTerminalFamily",
            named.get("persistent_return_reduced_to_terminal_family") is True,
            False,
            "持久命名回流只有 strict acyclic 终端家族被排斥后才能在 E0 中记为 0。",
            TERMINAL_FAMILY,
        ),
        row(
            "ColdSameParameterDisciplineClosed",
            cold_discipline,
            False,
            "冷供给与 Lambda 调参纪律已锁入同一参数账本，但还没有 U0 数值反超。",
            COLD_NUMERIC,
        ),
        row(
            "SparseBudgetFormulaClosed",
            sparse_formula,
            False,
            "非持久稀疏历史供给公式闭合；剩下是强制负载是否严格超过非持久供给。",
            SPARSE_BUDGET,
        ),
        row(
            "SparseMultiplicityReducedToDivisorCap",
            divisor_reduced,
            False,
            "单历史重数已压成缩频终端核心除数窗口计数，热窗口必须命名回流。",
            f"{DIVISOR_CAP} OR {HOT_CORE}",
        ),
        row(
            "TerminalFamilySaturatedInCurrentInternalCorpus",
            terminal_saturated and pdec_saturated,
            False,
            "canonical-lock、direct PDEC、clean KLS/DLS 三手臂在当前内部语料下已饱和为循环，不是已证排斥。",
            f"{MOVING_ATOM} OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact",
        ),
        row(
            "MovingAtomNonterminalExclusionPinned",
            moving_atom_next,
            False,
            "signed-source/atomic 来源展开回到终端三原子后，最贴近反例终端矛盾的非终端目标是 moving atom 排斥。",
            MOVING_ATOM,
        ),
        row(
            "ExplicitPositiveMarginCurrentCorpusProved",
            False,
            False,
            "D0 finite hash、E0 终端排斥、U0 非持久预算反超和 DStructure 尚未同时闭合。",
            f"{FINITE_PREFIX} AND {DIVISOR_CAP} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把最新正余量目标压成同参数子门；还没有得到反例链与真实结构链的无条件终端矛盾。",
            f"{FINITE_PREFIX} AND {DIVISOR_CAP} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造最新显式正余量下钻证书。"""
    data = {
        "latest": load_json("prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json"),
        "positive": load_json("prime-matrix-strict-positive-terminal-budget-margin-attack-router.json"),
        "coupled": load_json("prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json"),
        "concrete": load_json("prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json"),
        "rosser": load_json("prime-matrix-strict-rosser-floor-terminal-charge-router.json"),
        "named": load_json("prime-matrix-strict-named-return-same-parameter-deduction-router.json"),
        "cold": load_json("prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json"),
        "sparse": load_json("prime-matrix-strict-sparse-terminal-history-sae-budget-router.json"),
        "multiplicity": load_json("prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json"),
        "terminal": load_json("prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json"),
        "pdec_scope": load_json("prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"),
        "atomic": load_json("prime-matrix-strict-atomic-origin-identity-cycle-cut-sync-router.json"),
    }
    rows = build_rows(data)
    parameter_id = data["concrete"].get(
        "parameter_id",
        data["named"].get("parameter_id", "alpha043_pge100000_external_b3_pending_finite_prefix_named_return"),
    )
    hardpoint_after = (
        f"{FINITE_PREFIX} AND ({DIVISOR_CAP} OR {HOT_CORE}) AND "
        f"({MOVING_ATOM} OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate "
        "OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND "
        f"{DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_strict_explicit_positive_margin_latest_drilldown_router",
        "status": "explicit_positive_margin_drilled_to_finite_prefix_sparse_divisor_and_terminal_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "parameter_id": parameter_id,
        "explicit_positive_terminal_budget_margin_imported": data["latest"].get("next_direct_attack_target") == POSITIVE_MARGIN,
        "coupled_margin_schema_closed": data["coupled"].get("coupled_margin_schema_closed") is True,
        "candidate_parameter_row_generated": data["concrete"].get("candidate_parameter_row_generated") is True,
        "rosser_sawtooth_failure_charged": data["rosser"].get("sawtooth_failure_no_free_d0_loss_closed") is True,
        "named_return_same_parameter_schema_closed": data["named"].get("named_return_same_parameter_schema_closed") is True,
        "cold_same_parameter_discipline_closed": data["cold"].get("same_parameter_lambda_schedule_closed") is True,
        "sparse_budget_formula_closed": data["sparse"].get("nonpersistent_sae_budget_formula_closed") is True,
        "sparse_multiplicity_reduced_to_divisor_cap": data["multiplicity"].get("multiplicity_to_divisor_count_closed") is True,
        "terminal_family_saturated_not_proved": data["terminal"].get("strict_acyclic_terminal_family_proved") is False,
        "moving_atom_nonterminal_exclusion_pinned": data["atomic"].get("next_direct_attack_target") == MOVING_ATOM,
        "finite_boundary_prefix_certificate_proved": data["concrete"].get("finite_boundary_prefix_certificate_proved") is True,
        "scaled_terminal_core_divisor_window_count_cap_proved": data["multiplicity"].get("scaled_terminal_core_divisor_window_count_cap_proved") is True,
        "moving_atom_exclusion_proved": False,
        "dstructure_rankin_independently_accepted": False,
        "explicit_positive_terminal_budget_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": POSITIVE_MARGIN,
        "hardpoint_after_router": hardpoint_after,
        "next_direct_attack_target": DIVISOR_CAP,
        "next_parallel_targets": [
            FINITE_PREFIX,
            HOT_CORE,
            MOVING_ATOM,
            "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate",
            "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact",
            DSTRUCTURE,
        ],
        "margin_formula": "D_prefix - E_named - U_cold > 0",
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步直接下钻 `{POSITIVE_MARGIN}`，并同步旧的同参数表、Rosser 收费、命名回流、"
            "冷供给纪律、稀疏历史预算和终端三原子结果。结论是：正余量目标没有闭合；"
            f"D0 仍缺 `{FINITE_PREFIX}`，非持久 U0 已压到 `{DIVISOR_CAP}` 或热核心回流，"
            f"持久 E0 已回到终端三原子，其中当前最贴近反例终端矛盾的内部点是 `{MOVING_ATOM}`。"
            f"下一单点先攻 `{DIVISOR_CAP}`，同时保留 finite prefix、moving atom 和 DStructure 门。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 显式正终端余量最新下钻同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"parameter_id={result['parameter_id']}",
        f"explicit_positive_terminal_budget_margin_imported={fmt_bool(result['explicit_positive_terminal_budget_margin_imported'])}",
        f"coupled_margin_schema_closed={fmt_bool(result['coupled_margin_schema_closed'])}",
        f"candidate_parameter_row_generated={fmt_bool(result['candidate_parameter_row_generated'])}",
        f"rosser_sawtooth_failure_charged={fmt_bool(result['rosser_sawtooth_failure_charged'])}",
        f"named_return_same_parameter_schema_closed={fmt_bool(result['named_return_same_parameter_schema_closed'])}",
        f"sparse_multiplicity_reduced_to_divisor_cap={fmt_bool(result['sparse_multiplicity_reduced_to_divisor_cap'])}",
        f"finite_boundary_prefix_certificate_proved={fmt_bool(result['finite_boundary_prefix_certificate_proved'])}",
        f"scaled_terminal_core_divisor_window_count_cap_proved={fmt_bool(result['scaled_terminal_core_divisor_window_count_cap_proved'])}",
        f"explicit_positive_terminal_budget_margin_proved={fmt_bool(result['explicit_positive_terminal_budget_margin_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下钻收缩",
        "",
        "```text",
        result["hardpoint_before_router"],
        "  =>",
        result["hardpoint_after_router"],
        "```",
        "",
        "同参数余量仍是唯一终端口：",
        "",
        "```text",
        result["margin_formula"],
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
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 当前最窄单点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["next_parallel_targets"]),
            "```",
            "",
            "审稿边界：本证书不把候选参数行、Rosser 失败收费、稀疏预算公式或终端循环饱和写成无条件闭合；它只把最新正余量目标同步到更窄的同参数子门。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
