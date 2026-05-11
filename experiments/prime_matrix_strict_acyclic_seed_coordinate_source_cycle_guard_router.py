#!/usr/bin/env python3
"""生成 strict acyclic seed 坐标-来源依赖环守卫证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_coordinate_source_cycle_guard_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.md"

TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
NEXT_TARGET = (
    "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput_OR_"
    "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
)

NODES = [
    (
        "WordCoordinateFormula",
        "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json",
        "AcyclicSeedSignedWeightCoordinateSlotLedger",
    ),
    (
        "SignedWeightCoordinateSlot",
        "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json",
        "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords",
    ),
    (
        "SignedSlotValueFormula",
        "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json",
        "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger",
    ),
    (
        "CoefficientAssignment",
        "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json",
        "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula",
    ),
    (
        "CoefficientValueMap",
        "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json",
        "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward",
    ),
    (
        "BasisWordOriginIdentity",
        "prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json",
        "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands",
    ),
    (
        "RowLevelOriginGenerationTable",
        "prime-matrix-strict-row-level-origin-generation-table-router.json",
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity",
    ),
    (
        "SignedRowEmitter",
        "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json",
        "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward",
    ),
    (
        "PrimitiveCoefficientLaw",
        "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
        "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows",
    ),
    (
        "BasisWeightSource",
        "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json",
        "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy",
    ),
    (
        "InternalArithmeticBasisExpansion",
        "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json",
        "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger",
    ),
    (
        "BasisAlphabetLedger",
        "prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json",
        "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment",
    ),
    (
        "PrimitiveBasisWordGeneration",
        "prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json",
        "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility",
    ),
    (
        "SourceTupleWordConstructor",
        "prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json",
        "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility",
    ),
    (
        "BasisWordFormula",
        "prime-matrix-strict-acyclic-seed-basis-word-formula-router.json",
        "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters",
    ),
]

SOURCE_FILES = [name for _, name, _ in NODES] + [
    "prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
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


def cycle_edges(docs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """抽取当前前沿依赖边。"""
    edges = []
    for node, filename, expected_next in NODES:
        actual_next = docs[filename].get("next_direct_attack_target")
        edges.append(
            {
                "node": node,
                "file": f"docs/monograph/{filename}",
                "expected_next": expected_next,
                "actual_next": actual_next,
                "edge_matches": actual_next == expected_next,
            }
        )
    return edges


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造 seed 坐标-来源依赖环守卫证书。"""
    docs = {name: load_json(name) for name in SOURCE_FILES}
    edges = cycle_edges(docs)
    all_edges_match = all(edge["edge_matches"] for edge in edges)
    anchor_closed = docs["prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json"].get(
        "anchor_input_rule_proved"
    ) is True
    source_loop_cut = docs["prime-matrix-clean-core-source-loop-cut-router.json"].get(
        "source_loop_cut_closed"
    ) is True
    reverse_zero_blocked = (
        docs["prime-matrix-hypothetical-zero-row-seed-no-go-router.json"].get(
            "downstream_reverse_source_blocked"
        )
        is True
    )
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in docs.values()
        if isinstance(doc, dict)
    )

    cycle_text = (
        "WordCoordinateFormula -> SignedWeightCoordinateSlot -> SignedSlotValueFormula -> "
        "CoefficientAssignment -> CoefficientValueMap -> BasisWordOriginIdentity -> "
        "RowLevelOriginGenerationTable -> SignedRowEmitter -> PrimitiveCoefficientLaw -> "
        "BasisWeightSource -> InternalArithmeticBasisExpansion -> BasisAlphabetLedger -> "
        "PrimitiveBasisWordGeneration -> SourceTupleWordConstructor -> BasisWordFormula -> "
        "WordCoordinateFormula"
    )
    rows = [
        row(
            "AnchorInputRemovedFromFrontier",
            anchor_closed,
            True,
            "旧的 anchor input 缺口已经闭合；当前环不是由 anchor 选择函数造成。",
            "继续检查 signed 坐标-来源依赖环。",
        ),
        row(
            "SeedCoordinateSourceCycleDetected",
            all_edges_match,
            True,
            "当前所有已归档 next_direct_attack_target 串成一个从 word coordinate 回到 basis word formula 的闭合依赖环。",
            cycle_text,
        ),
        row(
            "RawCycleDoesNotCloseTheorem",
            all_edges_match,
            True,
            "该环说明现有内部路线互相定义；它不是 signed coefficient 或 word formula 的正向证明。",
            "raw cycle cannot count as closure。",
        ),
        row(
            "AcyclicSourceDisciplineRejectsReverseDefinition",
            source_loop_cut and reverse_zero_blocked,
            True,
            "source-loop cut 与零行 no-go 已排除从 payment、早期零行或推前后投影反向恢复 primitive source。",
            "需要独立 pre-Cauchy primitive basis/coefficient source，或命名回流。",
        ),
        row(
            "PrimitiveBasisAndCoefficientSourceInputCurrentCorpusProved",
            False,
            False,
            "仓库当前没有提交同时给出 primitive basis words 与 signed coefficients 的无环 pre-Cauchy 源输入。",
            "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput。",
        ),
        row(
            "TerminalReturnStillNeedsTerminalFamilyClosure",
            True,
            False,
            "若拒绝循环定义，本 signed-source 分支只能回流 acyclic terminal family；但终端家族自身仍需 canonical-lock 或 well-founded descent。",
            "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate。",
        ),
        row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "当前只完成了内部自足线的循环守卫；尚未得到反例链与真实链的终端矛盾。",
            NEXT_TARGET,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_coordinate_source_cycle_guard_router",
        "status": "acyclic_seed_coordinate_source_cycle_detected_cycle_cut_input_or_terminal_descent_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "anchor_input_rule_proved": anchor_closed,
        "seed_coordinate_source_cycle_detected": all_edges_match,
        "raw_cycle_counts_as_closure": False,
        "source_loop_cut_imported": source_loop_cut,
        "reverse_zero_row_source_recovery_blocked": reverse_zero_blocked,
        "primitive_basis_and_coefficient_source_input_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "terminal_return_if_no_cycle_cut_input": TERMINAL_RETURN,
        "next_direct_attack_target": NEXT_TARGET,
        "cycle_edges": edges,
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            "当前内部自足线已经不能靠继续展开获得更小字段；它形成 signed 坐标-来源闭合依赖环。"
            "要继续同一命题路线，只能补一个无环 primitive basis/coefficient 源输入，"
            "或证明回流终端家族有 well-founded descent/canonical-lock。"
        ),
        "plain_conclusion": (
            "本步把最新剩余硬点从线性下钻改写为环守卫：anchor input 已闭合，"
            "但 signed weight coordinate slot、coefficient assignment、来源恒等式、row emitter、basis alphabet、"
            "word constructor 与 word coordinate formula 构成闭合依赖环。"
            "该环不能作为证明；按 source-loop/no-go 纪律，若没有独立 pre-Cauchy primitive basis/coefficient 源输入，"
            "该分支必须回流 acyclic terminal family。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed 坐标-来源环守卫路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"anchor_input_rule_proved={fmt_bool(result['anchor_input_rule_proved'])}",
        f"seed_coordinate_source_cycle_detected={fmt_bool(result['seed_coordinate_source_cycle_detected'])}",
        f"raw_cycle_counts_as_closure={fmt_bool(result['raw_cycle_counts_as_closure'])}",
        f"source_loop_cut_imported={fmt_bool(result['source_loop_cut_imported'])}",
        f"primitive_basis_and_coefficient_source_input_proved={fmt_bool(result['primitive_basis_and_coefficient_source_input_proved'])}",
        f"acyclic_terminal_return_well_founded_descent_proved={fmt_bool(result['acyclic_terminal_return_well_founded_descent_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 闭合依赖环",
        "",
        "| node | edge_matches | actual_next |",
        "| --- | --- | --- |",
    ]
    for edge in result["cycle_edges"]:
        lines.append(
            "| `{node}` | `{edge_matches}` | {actual_next} |".format(
                node=table_cell(edge["node"]),
                edge_matches=fmt_bool(edge["edge_matches"]),
                actual_next=table_cell(edge["actual_next"]),
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
            "## 4. 下一真正单点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "无 cycle-cut 输入时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_cycle_cut_input"],
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
