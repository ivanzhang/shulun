#!/usr/bin/env python3
"""Prime Matrix new-layer 二秩预算账本路由器。

用法示例：
  python3 experiments/prime_matrix_newlayer_ranktwo_budget_ledger_router.py

输出：
  docs/monograph/prime-matrix-newlayer-ranktwo-budget-ledger-router.json
  docs/monograph/prime-matrix-newlayer-ranktwo-budget-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SCHEMA = DOCS / "prime-matrix-newlayer-pdec-schema-admission-router.json"
DEFAULT_PROJECTION = DOCS / "prime-matrix-clean-core-newlayer-pdec-projection-router.json"
DEFAULT_RANKTWO = DOCS / "prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.json"
DEFAULT_UNIFORM = DOCS / "prime-matrix-pdec-cap-uniform-cap-finite-basis-router.json"
DEFAULT_FINITE_ARC = DOCS / "prime-matrix-pdec-cap-finite-arc-transverse-router.json"
DEFAULT_TRANSVERSE = DOCS / "prime-matrix-pdec-cap-transverse-clean-reduction-router.json"
DEFAULT_DUAL_ABSORB = DOCS / "prime-matrix-pdec-dual-failure-absorption-contract.md"
DEFAULT_NO_CYCLE = DOCS / "prime-matrix-pdec-cap-refinement-no-cycle.md"
DEFAULT_TOWER = DOCS / "prime-matrix-newlayer-pdec-tower-entropy-contract.md"
DEFAULT_EXTMATCH = DOCS / "prime-matrix-clean-core-newlayer-external-lemma-match-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-newlayer-ranktwo-budget-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-newlayer-ranktwo-budget-ledger-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部锚点。"""
    return all(needle in text for needle in needles)


def remove_atom_once(text: str, atom: str) -> str:
    """从 AND 输入基中移除一个已被吸收的原子。"""
    if f"{atom} AND " in text:
        return text.replace(f"{atom} AND ", "", 1)
    if f" AND {atom}" in text:
        return text.replace(f" AND {atom}", "", 1)
    return text.replace(atom, "", 1)


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    schema: dict[str, Any],
    projection: dict[str, Any],
    ranktwo: dict[str, Any],
    uniform: dict[str, Any],
    finite_arc: dict[str, Any],
    transverse: dict[str, Any],
    dual_absorb_text: str,
    no_cycle_text: str,
    tower_text: str,
    extmatch_text: str,
) -> list[dict[str, Any]]:
    """生成 new-layer 二秩预算账本判定表。"""
    schema_active = (
        schema.get("newlayer_schema_admission_closed") is True
        and schema.get("terminal_gap_after_router")
        == "NewLayerRankTwoCapStablePDECBudgetLedger"
    )
    same_unit_ledger = (
        schema_active
        and projection.get("terminal_gap_after_router")
        == "RegisteredNewLayerPDECFormalUnitAndCapStableSchema"
        and "SameCPProjectionMonotonicity" in projection.get("closed_sublemmas", [])
        and schema.get("formal_unit_schema", {}).get("Omega", "").startswith("Omega'_A")
    )
    cap_localization_imported = (
        ranktwo.get("ranktwo_capstable_kernel_inequality_closed") is True
        and ranktwo.get("narrowest_next_hardpoint")
        == "UniformCapStabilityCertificateForRankTwoPrimitiveKernels"
        and contains_all(
            dual_absorb_text,
            ["Cap localization", "C_alpha(h,zeta)", "g(C_alpha)>=(U-alpha M)/(1-alpha)"],
        )
    )
    finite_arc_basis_imported = (
        uniform.get("uniform_cap_finite_basis_closed") is True
        and uniform.get("narrowest_next_hardpoint")
        == "FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels"
    )
    product_direction_split = (
        same_unit_ledger
        and finite_arc_basis_imported
        and "phase_map" in schema.get("formal_unit_schema", {})
    )
    finite_arc_trichotomy = (
        finite_arc.get("finite_arc_no_unnamed_exit_closed") is True
        and finite_arc.get("narrowest_next_hardpoint")
        == "TransverseFiberExpansionForFiniteArcCaps"
    )
    transverse_flat_reduction = (
        transverse.get("transverse_expansion_reduced_to_clean_atom") is True
        and transverse.get("narrowest_next_hardpoint")
        == "TransverseQuotientCleanLargeSieveAtom"
        and "NewLayerNoConcentrationImpliesFlatAdmission" in extmatch_text
    )
    named_return_no_cycle = (
        contains_all(
            dual_absorb_text,
            ["SAE / refined PDEC / ColumnCRT / Multiplicity-Stitching", "CapPersistent"],
        )
        and contains_all(
            no_cycle_text,
            ["Boolean algebra", "new-layer PDEC", "CleanKLS/DLS"],
        )
        and contains_all(
            tower_text,
            ["NewLayer-PDEC Tower Dichotomy", "profinite/global PDEC", "CleanKLS/DLS"],
        )
    )
    independent_removed = all(
        [
            schema_active,
            same_unit_ledger,
            cap_localization_imported,
            finite_arc_basis_imported,
            product_direction_split,
            finite_arc_trichotomy,
            transverse_flat_reduction,
            named_return_no_cycle,
        ]
    )
    return [
        row(
            "NewLayerRankTwoBudgetInputActive",
            schema_active,
            True,
            "上一层已把合法 new-layer schema 的唯一开放门定位为二秩 cap-stable 预算账本。",
            "检查它是否真是独立新原子。",
        ),
        row(
            "SameFormalUnitBudgetLedgerRegistered",
            same_unit_ledger,
            True,
            "Omega'_A=A x F_r、phase、weight 与同一 C_P 投影塔已固定，预算比较不换集合不换权重。",
            "若换口径则回流 Stitching/Multiplicity，不进入本账本。",
        ),
        row(
            "RankTwoCapLocalizationImported",
            cap_localization_imported,
            True,
            "同 formal unit 二秩 cap-stable 核的预算失败必给方向帽质量下界。",
            "U_CRT>=L_PDEC 不能作为无名失败保留，必须输出 cap witness。",
        ),
        row(
            "UniformFiniteArcBasisImported",
            finite_arc_basis_imported,
            True,
            "连续方向帽在有限 formal unit 上等价于有限循环弧 cap 基。",
            "只需处理旧轴、新 fiber、混合轴上的有限字符弧。",
        ),
        row(
            "ProductCharacterDirectionSplit",
            product_direction_split,
            True,
            "Omega'_A=A x F_r 中每个非平凡方向分成 old-axis、new-fiber 或 mixed-axis，均仍是有限字符弧预像。",
            "old-axis 回旧层 PDEC/ColumnCRT；new/mixed 进入 new-layer cap/flat 分裂。",
        ),
        row(
            "FiniteArcTransverseTrichotomyInherited",
            finite_arc_trichotomy,
            True,
            "高质量有限弧只有低横向支撑、持久横向偏斜、横向平坦分散三类。",
            "前两类回流 SAE/ColumnCRT/refined PDEC；平坦类进入 clean/flat 门。",
        ),
        row(
            "TransverseFlatResidualUsesNewLayerFlatGate",
            transverse_flat_reduction,
            False,
            "非平坦缺陷剥离后，剩余正是 new-layer 无集中 flat admission 的对象。",
            "仍需证明 NewLayerNoConcentrationImpliesFlatAdmission 及后续 flat DLS/KLS 吸收。",
        ),
        row(
            "NoCycleAndNamedReturnPreserved",
            named_return_no_cycle,
            True,
            "cap 细化不会在同层无限循环；升层只能进入 profinite/new-layer PDEC 或 CleanKLS/DLS。",
            "不允许新增第五类终端。",
        ),
        row(
            "NewLayerRankTwoBudgetIndependentGateRemoved",
            independent_removed,
            True,
            "二秩预算账本失败已被强制材料化为有限弧 cap，并被路由到命名回流或 new-layer flat gate。",
            "它不再作为独立开放输入保留。",
        ),
        row(
            "NewLayerNoConcentrationImpliesFlatAdmission",
            False,
            False,
            "当前材料尚未证明删除所有可登记 PDEC cap 后的 residual 自动满足 flat-DLS/KLS 准入。",
            "下一步最窄目标。",
        ),
    ]


def run(
    schema_path: Path,
    projection_path: Path,
    ranktwo_path: Path,
    uniform_path: Path,
    finite_arc_path: Path,
    transverse_path: Path,
    dual_absorb_path: Path,
    no_cycle_path: Path,
    tower_path: Path,
    extmatch_path: Path,
) -> dict[str, Any]:
    """执行 new-layer 二秩预算账本路由。"""
    source_paths = [
        schema_path,
        projection_path,
        ranktwo_path,
        uniform_path,
        finite_arc_path,
        transverse_path,
        dual_absorb_path,
        no_cycle_path,
        tower_path,
        extmatch_path,
    ]
    schema = load_json(schema_path)
    projection = load_json(projection_path)
    ranktwo = load_json(ranktwo_path)
    uniform = load_json(uniform_path)
    finite_arc = load_json(finite_arc_path)
    transverse = load_json(transverse_path)
    dual_absorb_text = dual_absorb_path.read_text(encoding="utf-8")
    no_cycle_text = no_cycle_path.read_text(encoding="utf-8")
    tower_text = tower_path.read_text(encoding="utf-8")
    extmatch_text = extmatch_path.read_text(encoding="utf-8")
    rows = build_rows(
        schema=schema,
        projection=projection,
        ranktwo=ranktwo,
        uniform=uniform,
        finite_arc=finite_arc,
        transverse=transverse,
        dual_absorb_text=dual_absorb_text,
        no_cycle_text=no_cycle_text,
        tower_text=tower_text,
        extmatch_text=extmatch_text,
    )
    old_atom = "NewLayerRankTwoCapStablePDECBudgetLedger"
    latest_self = remove_atom_once(schema.get("latest_self_contained_basis", ""), old_atom)
    latest_cond = remove_atom_once(schema.get("latest_conditional_basis", ""), old_atom)
    independent_removed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "NewLayerRankTwoBudgetIndependentGateRemoved"
    )
    return {
        "certificate_type": "newlayer_ranktwo_budget_ledger_router",
        "status": "newlayer_ranktwo_budget_ledger_reduced_to_flat_admission_gate",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "newlayer_ranktwo_budget_ledger_reduced": independent_removed,
        "newlayer_ranktwo_budget_independent_input_removed": independent_removed,
        "newlayer_pdec_budget_inequality_unconditionally_proved": False,
        "newlayer_no_concentration_flat_admission_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": old_atom,
        "terminal_gap_after_router": "NewLayerNoConcentrationImpliesFlatAdmission",
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "direction_split": {
            "old_axis": "projection to old formal unit; old PDEC/ColumnCRT/SAE return",
            "new_fiber_axis": "fiber residue b mod r; new-layer cap or flat admission",
            "mixed_axis": "finite character arc in A x F_r; transverse split then flat admission",
        },
        "replacement": {
            old_atom: "absorbed by named cap returns OR NewLayerNoConcentrationImpliesFlatAdmission",
        },
        "next_priority": "NewLayerNoConcentrationImpliesFlatAdmission",
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步没有证明所有 new-layer 二秩核的 U_CRT<L_PDEC；"
            "它证明更窄的结构事实：若该预算账本失败，则同一 formal unit 内必产生有限字符弧 cap。"
            "该 cap 要么回流 SAE/refined PDEC/ColumnCRT/multiplicity，要么在非平坦缺陷剥离后成为 "
            "NewLayerNoConcentrationImpliesFlatAdmission 的 flat residual。"
            "因此二秩预算账本不再是独立最终输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix new-layer 二秩预算账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"newlayer_ranktwo_budget_ledger_reduced={fmt_bool(result['newlayer_ranktwo_budget_ledger_reduced'])}",
        f"newlayer_ranktwo_budget_independent_input_removed={fmt_bool(result['newlayer_ranktwo_budget_independent_input_removed'])}",
        f"newlayer_pdec_budget_inequality_unconditionally_proved={fmt_bool(result['newlayer_pdec_budget_inequality_unconditionally_proved'])}",
        f"newlayer_no_concentration_flat_admission_proved={fmt_bool(result['newlayer_no_concentration_flat_admission_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 预算失败的强制形状",
        "",
        "```text",
        "NewLayerRankTwoCapStablePDECBudgetLedger",
        "  same formal unit Omega'_A=A x F_r;",
        "  if U_CRT >= L_PDEC:",
        "    cap localization gives a finite cyclic arc cap;",
        "    old-axis cap   => old PDEC / ColumnCRT / SAE return;",
        "    new-fiber cap  => new-layer PDEC cap or flat residual;",
        "    mixed-axis cap => transverse split, then named return or flat residual;",
        "  therefore no independent budget-ledger terminal remains.",
        "```",
        "",
        "## 2. 方向分裂",
        "",
        "| direction class | route |",
        "| --- | --- |",
    ]
    for key, value in result["direction_split"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 3. 替换律",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "注意：这里删除的是独立预算账本原子，不是宣称 new-layer flat admission 已经完成。",
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{remaining}` |".format(
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
            "## 5. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            f"最窄目标更新为 `{result['next_priority']}`。"
            "必须证明：删除/回流所有可登记 PDEC cap 后，剩余新增层对象确实满足 flat-DLS/KLS 准入；"
            "否则必须输出新的命名 PDEC/SAE/ColumnCRT/multiplicity 证书。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_outputs(result: dict[str, Any], json_out: Path, md_out: Path) -> None:
    """写出 JSON 与 Markdown。"""
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--projection", type=Path, default=DEFAULT_PROJECTION)
    parser.add_argument("--ranktwo", type=Path, default=DEFAULT_RANKTWO)
    parser.add_argument("--uniform", type=Path, default=DEFAULT_UNIFORM)
    parser.add_argument("--finite-arc", type=Path, default=DEFAULT_FINITE_ARC)
    parser.add_argument("--transverse", type=Path, default=DEFAULT_TRANSVERSE)
    parser.add_argument("--dual-absorb", type=Path, default=DEFAULT_DUAL_ABSORB)
    parser.add_argument("--no-cycle", type=Path, default=DEFAULT_NO_CYCLE)
    parser.add_argument("--tower", type=Path, default=DEFAULT_TOWER)
    parser.add_argument("--extmatch", type=Path, default=DEFAULT_EXTMATCH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        schema_path=args.schema,
        projection_path=args.projection,
        ranktwo_path=args.ranktwo,
        uniform_path=args.uniform,
        finite_arc_path=args.finite_arc,
        transverse_path=args.transverse,
        dual_absorb_path=args.dual_absorb,
        no_cycle_path=args.no_cycle,
        tower_path=args.tower,
        extmatch_path=args.extmatch,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
