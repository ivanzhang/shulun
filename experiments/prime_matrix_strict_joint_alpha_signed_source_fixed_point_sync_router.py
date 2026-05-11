#!/usr/bin/env python3
"""生成 strict joint-alpha / signed-source 固定点同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_joint_alpha_signed_source_fixed_point_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.md"

SIGNED_SOURCE_INPUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
JOINT_EMITTER = "AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy"
JOINT_DECLARATION = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
JOINT_CONSTRUCTOR = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
JOINT_ALPHA_SIDE = "JointAlphaSidePrimitiveWordCoefficientRuleLedger"
JOINT_SAME_ROW = "JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SIGNED_ROW_EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-signed-source-cycle-frontier-sync-router.json",
    "prime-matrix-strict-cycle-cut-joint-basis-coefficient-emitter-router.json",
    "prime-matrix-strict-joint-emitter-formula-field-atom-router.json",
    "prime-matrix-strict-joint-declaration-constructor-sync-router.json",
    "prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json",
    "prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json",
    "prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-signed-source-fixed-point-breaker-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-acyclic-terminal-cycle-guard-router.json",
    "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取证书；缺失时返回空对象以保留审计边界。"""
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
    """记录本证书实际读取到的证据文件。"""
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


def synchronized_route() -> list[dict[str, str]]:
    """列出本轮同步后的完整固定点路线。"""
    return [
        {"from": SIGNED_SOURCE_INPUT, "to": JOINT_EMITTER},
        {"from": JOINT_EMITTER, "to": JOINT_DECLARATION},
        {"from": JOINT_DECLARATION, "to": JOINT_CONSTRUCTOR},
        {"from": JOINT_CONSTRUCTOR, "to": JOINT_ALPHA_SIDE},
        {"from": JOINT_ALPHA_SIDE, "to": JOINT_SAME_ROW},
        {"from": JOINT_SAME_ROW, "to": ROW_TABLE},
        {"from": ROW_TABLE, "to": SIGNED_ROW_EMITTER},
        {"from": SIGNED_ROW_EMITTER, "to": "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"},
        {"from": "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward", "to": "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows"},
        {"from": "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows", "to": "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy"},
        {"from": "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy", "to": "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger"},
        {"from": "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger", "to": "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment"},
        {"from": "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment", "to": "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility"},
        {"from": "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility", "to": "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility"},
        {"from": "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility", "to": "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters"},
        {"from": "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters", "to": "AcyclicSeedSignedWeightCoordinateSlotLedger"},
        {"from": "AcyclicSeedSignedWeightCoordinateSlotLedger", "to": "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords"},
        {"from": "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords", "to": "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger"},
        {"from": "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger", "to": "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula"},
        {"from": "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula", "to": "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward"},
        {"from": "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward", "to": ROW_TABLE},
    ]


def descent_input_contract() -> list[dict[str, str]]:
    """列出下一非循环下降证书必须补齐的字段。"""
    return [
        {
            "field": "complexity_vector",
            "meaning": "给每个 terminal return record 定义有限字典序量，例如 formal unit 层级、未结叶子数、签名秩、payload 维度和回流深度。",
        },
        {
            "field": "return_transition_table",
            "meaning": "逐类登记 PDEC、SAE、ColumnCRT、CleanKLS、new-layer、sparse packet 和 noncanonical payload 的回流边。",
        },
        {
            "field": "strict_drop_or_leaf",
            "meaning": "证明每条合法回流边要么复杂度严格下降，要么进入已命名叶子防火墙输入。",
        },
        {
            "field": "leaf_firewall_discharge",
            "meaning": "对 FutureExplicitPrimitivePDECSchema、FutureExplicitSparsePacketExtractorSchema 与 NoncanonicalFullSComplementLegalClosureMode 给出排斥或接受边界。",
        },
        {
            "field": "no_source_reimport",
            "meaning": "禁止从 terminal leaf 再后验读回 row-level/signed-source 表来制造自证。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步 joint-alpha 与 signed-source 两条路线，判断是否仍有非循环源输入。"""
    frontier = data["frontier"]
    cycle_cut = data["cycle_cut"]
    joint_emitter = data["joint_emitter"]
    joint_declaration = data["joint_declaration"]
    joint_constructor = data["joint_constructor"]
    joint_alpha = data["joint_alpha"]
    same_row = data["same_row"]
    row_level = data["row_level"]
    fixed_point = data["fixed_point"]
    coordinate_cycle = data["coordinate_cycle"]
    terminal_cycle = data["terminal_cycle"]
    terminal_descent = data["terminal_descent"]

    joint_route_to_row_level = all(
        [
            frontier.get("next_direct_attack_target") == SIGNED_SOURCE_INPUT,
            cycle_cut.get("next_direct_attack_target") == JOINT_EMITTER,
            joint_emitter.get("next_direct_attack_target") == JOINT_DECLARATION,
            joint_declaration.get("next_direct_attack_target") == JOINT_CONSTRUCTOR,
            joint_constructor.get("next_direct_attack_target") == JOINT_ALPHA_SIDE,
            joint_alpha.get("next_direct_attack_target") == JOINT_SAME_ROW,
            same_row.get("next_direct_attack_target") == ROW_TABLE,
        ]
    )
    signed_source_fixed_point = (
        fixed_point.get("current_internal_route_is_signed_source_fixed_point") is True
        and fixed_point.get("row_level_clean_core_origin_generation_table_proved") is False
    )
    cycle_guard_imported = (
        coordinate_cycle.get("seed_coordinate_source_cycle_detected") is True
        or coordinate_cycle.get("acyclic_seed_coordinate_source_cycle_guard_router_closed") is True
    )
    terminal_descent_schema_closed = (
        terminal_descent.get("terminal_return_well_founded_descent_schema_closed") is True
        and terminal_descent.get("acyclic_terminal_return_well_founded_descent_proved") is False
    )

    return [
        row(
            "CounterexampleBranchPreserved",
            True,
            True,
            "本同步仍在早期零行反例链内部工作，不使用真实零行缺席作前提。",
            "direct_unconditional_contradiction_found=false",
        ),
        row(
            "CycleCutRouteStartsAtSignedSourceInput",
            frontier.get("next_direct_attack_target") == SIGNED_SOURCE_INPUT,
            False,
            "上一前沿把非循环新增输入钉为 primitive basis/coefficient 前置源输入。",
            SIGNED_SOURCE_INPUT,
        ),
        row(
            "CycleCutRouteReducedToJointEmitter",
            cycle_cut.get("next_direct_attack_target") == JOINT_EMITTER,
            False,
            "cycle-cut 输入已排除顺序拆分，压成 Cauchy 前联合发射器。",
            JOINT_EMITTER,
        ),
        row(
            "JointEmitterRouteReducedToJointDeclaration",
            joint_emitter.get("next_direct_attack_target") == JOINT_DECLARATION,
            False,
            "联合发射器字段级下钻后，第一生产性原子是 joint declaration line。",
            JOINT_DECLARATION,
        ),
        row(
            "JointDeclarationRouteReducedToJointConstructor",
            joint_declaration.get("next_direct_attack_target") == JOINT_CONSTRUCTOR,
            False,
            "joint declaration 与 actual constructor 同步后，硬点变成显式 joint alpha/delta constructor rule。",
            JOINT_CONSTRUCTOR,
        ),
        row(
            "JointConstructorRouteReducedToAlphaSide",
            joint_constructor.get("next_direct_attack_target") == JOINT_ALPHA_SIDE,
            False,
            "显式 joint rule 的首个生产性字段是 joint alpha-side primitive word/coefficient rule。",
            JOINT_ALPHA_SIDE,
        ),
        row(
            "JointAlphaSideReducedToSameRowIdentity",
            joint_alpha.get("next_direct_attack_target") == JOINT_SAME_ROW,
            False,
            "joint alpha-side 的未闭合处是 unsigned word skeleton 与 signed coefficient origin identity 同行同源。",
            JOINT_SAME_ROW,
        ),
        row(
            "SameRowIdentityReducedToRowLevelTable",
            same_row.get("next_direct_attack_target") == ROW_TABLE,
            False,
            "same-row 桥接已回收到逐行 clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "RowLevelTableStillOpen",
            row_level.get("row_level_clean_core_origin_generation_table_proved") is False,
            False,
            "逐行原始生成表仍未证明，继续内部下钻会进入 seed signed row emitter。",
            SIGNED_ROW_EMITTER,
        ),
        row(
            "SignedSourceFixedPointImported",
            signed_source_fixed_point,
            True,
            "signed-source 下钻链已登记为 RowLevel -> ... -> RowLevel 固定点。",
            "不能用固定点自证 row-level 表。",
        ),
        row(
            "CoordinateSourceCycleGuardImported",
            cycle_guard_imported,
            True,
            "坐标、source tuple、basis word、assignment、origin identity 的来源环已被守卫识别。",
            f"{SIGNED_SOURCE_INPUT} OR {TERMINAL_DESCENT}",
        ),
        row(
            "JointAlphaSignedSourceRouteIsFixedPoint",
            joint_route_to_row_level and signed_source_fixed_point,
            True,
            "cycle-cut/joint-alpha 线与 signed-source 线同步后回到同一个 RowLevel 固定点。",
            TERMINAL_DESCENT,
        ),
        row(
            "TerminalCycleGuardAlreadyPinsDescentNeed",
            terminal_cycle.get("terminal_gap_after_router", "").find(TERMINAL_DESCENT) >= 0,
            False,
            "终端家族循环守卫已说明 direct PDEC/CleanKLS 裸路线会自回流，必须给 well-founded descent 或 canonical-lock。",
            TERMINAL_DESCENT,
        ),
        row(
            "TerminalDescentSchemaClosedButLeafOpen",
            terminal_descent_schema_closed,
            False,
            "无隐藏循环 schema 已闭合，但叶子防火墙与 noncanonical full-S 合法模式仍未排斥。",
            terminal_descent.get("terminal_gap_after_router", "TerminalLeafFirewallInputs_OR_CanonicalLock"),
        ),
        row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "当前只完成固定点同步和下一非循环硬点定位，尚未得到终端矛盾。",
            TERMINAL_DESCENT,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "frontier": load_json("prime-matrix-strict-signed-source-cycle-frontier-sync-router.json"),
        "cycle_cut": load_json("prime-matrix-strict-cycle-cut-joint-basis-coefficient-emitter-router.json"),
        "joint_emitter": load_json("prime-matrix-strict-joint-emitter-formula-field-atom-router.json"),
        "joint_declaration": load_json("prime-matrix-strict-joint-declaration-constructor-sync-router.json"),
        "joint_constructor": load_json("prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json"),
        "joint_alpha": load_json("prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json"),
        "same_row": load_json("prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json"),
        "row_level": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "fixed_point": load_json("prime-matrix-strict-signed-source-fixed-point-breaker-router.json"),
        "coordinate_cycle": load_json("prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"),
        "terminal_cycle": load_json("prime-matrix-strict-acyclic-terminal-cycle-guard-router.json"),
        "terminal_descent": load_json("prime-matrix-strict-acyclic-terminal-descent-firewall-router.json"),
    }
    rows = build_rows(data)
    fixed_point_synced = next(item["closed"] for item in rows if item["gate"] == "JointAlphaSignedSourceRouteIsFixedPoint")
    terminal_schema_closed = next(item["closed"] for item in rows if item["gate"] == "TerminalDescentSchemaClosedButLeafOpen")
    return {
        "certificate_type": "prime_matrix_strict_joint_alpha_signed_source_fixed_point_sync_router",
        "status": "joint_alpha_cycle_cut_route_synced_to_signed_source_fixed_point_terminal_descent_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "joint_alpha_signed_source_fixed_point_sync_router_closed": True,
        "cycle_cut_joint_route_returns_to_row_level_fixed_point": fixed_point_synced,
        "acyclic_seed_cycle_cut_source_input_proved": False,
        "joint_basis_word_coefficient_emitter_proved": False,
        "row_level_clean_core_origin_generation_table_proved": False,
        "acyclic_terminal_return_well_founded_descent_schema_closed": terminal_schema_closed,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": TERMINAL_DESCENT,
        "terminal_gap_after_router": f"{TERMINAL_DESCENT} AND {DSTRUCTURE}",
        "descent_input_contract": descent_input_contract(),
        "synchronized_route": synchronized_route(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{SIGNED_SOURCE_INPUT}` 经 joint emitter、joint declaration、joint constructor、"
            f"joint alpha-side 与 same-row identity 后回到 `{ROW_TABLE}`；"
            "而该表的 signed-source 内部展开又回到自身。"
        ),
        "plain_conclusion": (
            "本步没有转换命题，而是把最新 cycle-cut/joint-alpha 下钻链与 signed-source 固定点链同步。"
            "结果是：所谓 cycle-cut 前置源输入若按内部字段继续展开，会经 joint 发射器、joint 声明、"
            "显式 joint alpha/delta 规则、joint alpha-side、same-row 桥接回到逐行原始生成表；"
            "该表又落入已登记的 signed-source 固定点。因此当前内部自足线不能再把 cycle-cut 源输入当作"
            "新的非循环出口。下一真正非循环硬点是终端回流 well-founded 严格下降证书；"
            "下降 schema 已部分整理，但叶子防火墙和 noncanonical full-S 合法模式仍未排斥。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict joint-alpha / signed-source 固定点同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"joint_alpha_signed_source_fixed_point_sync_router_closed={fmt_bool(result['joint_alpha_signed_source_fixed_point_sync_router_closed'])}",
        f"cycle_cut_joint_route_returns_to_row_level_fixed_point={fmt_bool(result['cycle_cut_joint_route_returns_to_row_level_fixed_point'])}",
        f"acyclic_seed_cycle_cut_source_input_proved={fmt_bool(result['acyclic_seed_cycle_cut_source_input_proved'])}",
        f"joint_basis_word_coefficient_emitter_proved={fmt_bool(result['joint_basis_word_coefficient_emitter_proved'])}",
        f"row_level_clean_core_origin_generation_table_proved={fmt_bool(result['row_level_clean_core_origin_generation_table_proved'])}",
        f"acyclic_terminal_return_well_founded_descent_schema_closed={fmt_bool(result['acyclic_terminal_return_well_founded_descent_schema_closed'])}",
        f"acyclic_terminal_return_well_founded_descent_proved={fmt_bool(result['acyclic_terminal_return_well_founded_descent_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步路线",
        "",
        result["frontier_reduction"],
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["synchronized_route"]:
        lines.append(f"| {table_cell(item['from'])} | {table_cell(item['to'])} |")

    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 下一非循环硬点合同",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["descent_input_contract"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "## 4. 下一真正单点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "当前活动基：",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "```",
            "",
            "审稿边界：本文件只关闭 joint-alpha/cycle-cut 与 signed-source 固定点的同步定位；"
            "它没有证明终端下降证书，也没有证明行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        "cycle_cut_joint_route_returns_to_row_level_fixed_point="
        f"{fmt_bool(result['cycle_cut_joint_route_returns_to_row_level_fixed_point'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
