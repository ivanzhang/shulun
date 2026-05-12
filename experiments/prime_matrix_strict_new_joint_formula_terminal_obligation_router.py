#!/usr/bin/env python3
"""生成 strict 新显式 joint 公式终端义务证书。

用法示例：
  python3 experiments/prime_matrix_strict_new_joint_formula_terminal_obligation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-new-joint-formula-terminal-obligation-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-new-joint-formula-terminal-obligation-router.json"
OUT_MD = DOCS / "prime-matrix-strict-new-joint-formula-terminal-obligation-router.md"

NEW_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
TARGET_RULE = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
JOINT_ALPHA = "JointAlphaSidePrimitiveWordCoefficientRuleLedger"
JOINT_SAME_ROW = "JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SIGNED_EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json",
    "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json",
    "prime-matrix-strict-joint-declaration-constructor-sync-router.json",
    "prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json",
    "prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json",
    "prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-signed-source-fixed-point-breaker-router.json",
    "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json",
    "prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json",
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


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不能当成证明。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def formula_fields() -> list[dict[str, str]]:
    """新显式公式工件必须携带的最小字段。"""
    return [
        {
            "field": "actual_noncanonical_source_tuple_domain",
            "requirement": "在 Cauchy、dispersion、terminal extraction、payment 推前前定义；不得由零行或 payment 数据反推。",
        },
        {
            "field": "joint_row_index_and_formal_unit",
            "requirement": "每个 primitive row 属于同一 formal unit，并给出 alpha/delta 两侧共同索引。",
        },
        {
            "field": "basis_word_formula",
            "requirement": "从 source tuple 正向输出 primitive basis word 坐标，而非后验选择。",
        },
        {
            "field": "signed_coefficient_formula",
            "requirement": "同一行同时输出 signed coefficient、sign、local factor 和非零条件。",
        },
        {
            "field": "uv_phi_pairing",
            "requirement": "同步给出 exact (u,v)、Phi atom，并证明推前前 alpha/delta pairing 恒等式。",
        },
        {
            "field": "budget_and_failure_return",
            "requirement": "给出总变差、branch key、rank/multiplicity 预算；失败必须落入命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步新 joint 公式的终端义务。"""
    frontier = data["frontier"]
    direct = data["direct"]
    joint_decl = data["joint_decl"]
    joint_explicit = data["joint_explicit"]
    joint_alpha = data["joint_alpha"]
    same_row = data["same_row"]
    row_level = data["row_level"]
    signed_fixed = data["signed_fixed"]
    terminal = data["terminal"]
    pair = data["pair"]

    return [
        row(
            "CurrentStrictInternalNoncycleTarget",
            frontier.get("next_direct_attack_target") == NEW_FORMULA,
            False,
            "seed-cycle-cut 与 PDEC 作用域分支饱和后，唯一内部非循环主攻点是新显式 joint 公式。",
            NEW_FORMULA,
        ),
        row(
            "ExistingDirectAttackImported",
            direct.get("explicit_joint_constructor_target_active") is True
            and direct.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True,
            direct.get("explicit_joint_constructor_rule_proved") is True,
            "已有 direct attack 证明：继续展开旧 TARGET 会回到 signed-source 固定点。",
            NEW_FORMULA,
        ),
        row(
            "DeclarationIsNotFormula",
            joint_decl.get("joint_declaration_constructor_sync_router_closed") is True
            or joint_decl.get("same_source_tuple_container_closed") is True,
            False,
            "source tuple 容器、字段边界、payload 名称都不是正向 coefficient 公式。",
            "需要 actual formula。",
        ),
        row(
            "OldJointRuleReducesToAlphaSide",
            joint_explicit.get("next_direct_attack_target") == JOINT_ALPHA,
            False,
            "旧 joint rule 的首字段仍是 alpha-side primitive word/coefficient ledger。",
            JOINT_ALPHA,
        ),
        row(
            "AlphaSideReducesToSameRow",
            joint_alpha.get("next_direct_attack_target") == JOINT_SAME_ROW,
            False,
            "alpha-side 需要同一 pre-Cauchy row 上 basis word 与 signed coefficient 同源。",
            JOINT_SAME_ROW,
        ),
        row(
            "SameRowReducesToRowLevel",
            same_row.get("next_direct_attack_target") == ROW_TABLE,
            False,
            "same-row 同源恒等式仍要求逐行原始生成表。",
            ROW_TABLE,
        ),
        row(
            "RowLevelReturnsToSignedEmitter",
            row_level.get("next_direct_attack_target") == SIGNED_EMITTER,
            False,
            "row-level 表继续要求 signed row emitter。",
            SIGNED_EMITTER,
        ),
        row(
            "SignedEmitterRouteIsFixedPoint",
            signed_fixed.get("current_internal_route_is_signed_source_fixed_point") is True,
            True,
            "signed row emitter 的内部展开已经登记为 signed-source 固定点。",
            "不能用固定点替代新公式。",
        ),
        row(
            "TerminalDescentAlternativeIsMacrocycle",
            terminal.get("terminal_descent_macrocycle_detected") is True
            and terminal.get("current_terminal_descent_attack_spine_is_recursive") is True,
            False,
            "没有新公式时的终端下降替代已是 terminal-source-pair-joint 宏循环。",
            TERMINAL_DESCENT,
        ),
        row(
            "PairEnergyDoesNotSupplyFormula",
            pair.get("current_pair_energy_attack_spine_is_recursive") is True
            or pair.get("explicit_joint_constructor_rule_proved") is False,
            False,
            "pair-energy 抽象输入不能生产逐行 joint formula；它也回到 source entropy/joint constructor 固定点。",
            NEW_FORMULA,
        ),
        row(
            "NewFormulaArtifactPresent",
            False,
            False,
            "当前仓库没有提交满足六字段合同的显式新公式工件。",
            NEW_FORMULA,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "缺少新公式以及 ExactUV/模型余量/Rate/DStructure 验收门，作者侧无条件闭合尚未完成。",
            f"{NEW_FORMULA} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造新 joint 公式终端义务证书。"""
    data = {
        "frontier": load_json("prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"),
        "direct": load_json("prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"),
        "joint_decl": load_json("prime-matrix-strict-joint-declaration-constructor-sync-router.json"),
        "joint_explicit": load_json("prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json"),
        "joint_alpha": load_json("prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json"),
        "same_row": load_json("prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json"),
        "row_level": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "signed_fixed": load_json("prime-matrix-strict-signed-source-fixed-point-breaker-router.json"),
        "terminal": load_json("prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json"),
        "pair": load_json("prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    fixedpoint_imported = any(
        item["gate"] == "SignedEmitterRouteIsFixedPoint" and item["closed"] is True for item in rows
    )
    formula_artifact_present = False
    strict_basis = f"{NEW_FORMULA} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_strict_new_joint_formula_terminal_obligation_router",
        "status": "new_joint_formula_terminal_obligation_open_no_current_internal_formula_artifact",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "new_joint_formula_is_current_internal_noncycle_target": data["frontier"].get(
            "next_direct_attack_target"
        )
        == NEW_FORMULA,
        "old_joint_constructor_route_returns_to_signed_source_fixed_point": fixedpoint_imported,
        "new_explicit_joint_constructor_formula_artifact_present": formula_artifact_present,
        "explicit_joint_constructor_rule_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": data["terminal"].get(
            "acyclic_terminal_return_well_founded_descent_proved"
        )
        is True,
        "terminal_descent_alternative_is_macrocycle": data["terminal"].get(
            "terminal_descent_macrocycle_detected"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_FORMULA,
        "strict_author_side_remaining_basis": strict_basis,
        "formula_fields": formula_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "当前 strict 内部路线已压到真正终端公式义务：必须提交一个新的显式 actual joint alpha/delta "
            "primitive word/coefficient 构造公式。已有 declaration、alpha-side、same-row、row-level、signed-emitter "
            "材料只能形成固定点，不能生产该公式；terminal descent 替代路线也已是宏循环。因此目标命题作者侧"
            "无条件闭合尚未完成，最后数学输入就是 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`，"
            "并需同时通过 ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 守门项。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 新显式 joint 公式终端义务",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        (
            "new_joint_formula_is_current_internal_noncycle_target="
            f"{fmt_bool(result['new_joint_formula_is_current_internal_noncycle_target'])}"
        ),
        (
            "old_joint_constructor_route_returns_to_signed_source_fixed_point="
            f"{fmt_bool(result['old_joint_constructor_route_returns_to_signed_source_fixed_point'])}"
        ),
        (
            "new_explicit_joint_constructor_formula_artifact_present="
            f"{fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}"
        ),
        f"explicit_joint_constructor_rule_proved={fmt_bool(result['explicit_joint_constructor_rule_proved'])}",
        (
            "terminal_descent_alternative_is_macrocycle="
            f"{fmt_bool(result['terminal_descent_alternative_is_macrocycle'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
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
            "## 2. 公式字段合同",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for item in result["formula_fields"]:
        lines.append(
            "| `{field}` | {requirement} |".format(
                field=table_cell(item["field"]),
                requirement=table_cell(item["requirement"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 作者侧剩余基",
            "",
            "```text",
            result["strict_author_side_remaining_basis"],
            "```",
            "",
            "下一直接主攻仍是：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    if result["missing_sources"]:
        lines.extend(["", "## 4. 缺失依赖", ""])
        for item in result["missing_sources"]:
            lines.append(f"- `{item}`")
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
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
