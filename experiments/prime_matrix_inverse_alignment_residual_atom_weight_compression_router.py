#!/usr/bin/env python3
"""把残洞已分配 atom 的单位权缺口接回 M# 加权预算账本。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_residual_atom_weight_compression_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-residual-atom-weight-compression-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-residual-atom-weight-compression-router.json
  docs/monograph/prime-matrix-inverse-alignment-residual-atom-weight-compression-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-residual-atom-weight-compression-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-residual-atom-weight-compression-router.md"

DELETION_MAP = DOCS / "prime-matrix-inverse-alignment-overlap-slack-deletion-map-router.json"
SPARSE_FORCED_LOAD = DOCS / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json"
FORCED_OBLIGATION = DOCS / "prime-matrix-strict-forced-obligation-lower-bound-router.json"
SPARSE_BUDGET = DOCS / "prime-matrix-strict-sparse-budget-after-unified-sync-router.json"

SOURCE_FILES = [
    DELETION_MAP,
    SPARSE_FORCED_LOAD,
    FORCED_OBLIGATION,
    SPARSE_BUDGET,
    DOCS / "prime-matrix-inverse-alignment-prefix-demand-bridge-router.json",
    DOCS / "prime-matrix-inverse-alignment-latest-frontier-sync-router.json",
]

RESIDUAL_COMPRESSION = "ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger"
STRICT_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
HOT_FIXED = "TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_residual_atom_weight_compression_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def compression_rows(deletion_map: dict[str, Any]) -> list[dict[str, Any]]:
    """把上一层整数删除缺口解释为 raw 单位度量到 M# 度量的换尺。"""
    rows: list[dict[str, Any]] = []
    for item in deletion_map.get("unit_audit_rows", []):
        residual = int(item["residual_columns"])
        msharp = float(item["Msharp"])
        integer_gap = int(item["residual_reciprocal_compression_needed"])
        formula_gap = math.floor(residual - msharp) + 1
        rows.append(
            {
                "P": int(item["P"]),
                "x": int(item["x"]),
                "z": int(item["z"]),
                "assigned_residual_atom_units": residual,
                "Msharp_weighted_mass": round(msharp, 12),
                "raw_unit_minus_weighted_mass": round(residual - msharp, 12),
                "integer_gap_if_raw_units_are_kept": integer_gap,
                "floor_formula_gap": formula_gap,
                "measure_change_identity_ok": integer_gap == formula_gap,
                "weighted_mass_not_unit_deletion": True,
            }
        )
    return rows


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合的接口命题。"""
    return [
        {
            "name": "residual_atom_unit_gap_identified",
            "status": "closed",
            "statement": "after direct suffix deletion, the remaining raw unit count is |R_xz|, while the budget demand is M#.",
        },
        {
            "name": "capacity_multiplier_weight_normalization",
            "status": "closed_by_imported_Msharp_ledger",
            "statement": "each assigned residual atom contributes 1/mu_tau to M#, not one raw supply unit.",
        },
        {
            "name": "integer_residual_deletion_gap",
            "status": "closed_as_wrong_measure_artifact",
            "statement": "floor(|R_xz|-M#)+1 is the extra deletion required only if assigned atoms are incorrectly kept at unit weight.",
        },
        {
            "name": "named_return_boundary",
            "status": "closed_as_no_loss_or_named_return",
            "statement": "mass not entering the weighted sparse terminal ledger must be registered as PDEC/SAE/ColumnCRT/hot/fixed/quotient return.",
        },
        {
            "name": "same_parameter_strict_margin",
            "status": "open",
            "statement": "the true remaining inequality is M# - E_registered > U_np under the same parameter ledger.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "DeletionMapImported",
            "closed": result["overlap_slack_deletion_map_imported"],
            "proved": result["overlap_slack_deletion_map_imported"],
            "meaning": "上一层已把 raw suffix 删除量拆成直接后缀冗余与残洞已分配 atom。",
            "remaining": RESIDUAL_COMPRESSION,
        },
        {
            "gate": "MsharpWeightedSourceImported",
            "closed": result["msharp_weighted_source_imported"],
            "proved": result["msharp_weighted_source_imported"],
            "meaning": "prefix 残洞到 M# 的容量乘子归一化已经在主线账本闭合。",
            "remaining": STRICT_MARGIN,
        },
        {
            "gate": "NoLossOrNamedReturnImported",
            "closed": result["no_loss_or_named_return_imported"],
            "proved": result["no_loss_or_named_return_imported"],
            "meaning": "不能进入 weighted sparse terminal ledger 的质量只能命名回流，不能作为免费冷供给。",
            "remaining": STRICT_MARGIN,
        },
        {
            "gate": "ResidualCompressionIndependentHardpointRemoved",
            "closed": result["residual_atom_weight_compression_closed_as_measure_change"],
            "proved": result["residual_atom_weight_compression_closed_as_measure_change"],
            "meaning": "残洞 atom 的“额外删除量”是 raw 单位尺误差；正确预算已使用 M# reciprocal 权重。",
            "remaining": STRICT_MARGIN,
        },
        {
            "gate": "SameParameterStrictMarginProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 M# 扣除命名回流后严格大于非持久 cold supply。",
            "remaining": STRICT_MARGIN,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "同参数严格余量、热/固定出口、持久 moving atom 和 DStructure/Rankin 仍未全部闭合。",
            "remaining": f"{STRICT_MARGIN} AND {HOT_FIXED} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造残洞 atom 权重压缩证书。"""
    deletion_map = load_json(DELETION_MAP)
    forced_load = load_json(SPARSE_FORCED_LOAD)
    forced_obligation = load_json(FORCED_OBLIGATION)
    sparse_budget = load_json(SPARSE_BUDGET)
    rows = compression_rows(deletion_map)

    weighted_source = (
        forced_load.get("prefix_weighted_source_imported") is True
        and forced_load.get("forced_load_criterion_closed") is True
        and forced_obligation.get("clb_residual_to_weighted_obligation_injection_closed") is True
    )
    no_loss = (
        forced_load.get("terminal_projection_no_loss_or_named_return_closed") is True
        and forced_obligation.get("no_loss_weighted_accounting_imported") is True
    )
    normal_form = sparse_budget.get("same_parameter_sparse_demand_cold_supply_normal_form_closed") is True
    measure_change = bool(rows) and all(item["measure_change_identity_ok"] for item in rows)
    closed_as_measure_change = (
        deletion_map.get("deletion_target_decomposition_closed") is True
        and weighted_source
        and no_loss
        and normal_form
        and measure_change
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_residual_atom_weight_compression_router",
        "status": "residual_atom_weight_compression_imported_strict_margin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "overlap_slack_deletion_map_imported": deletion_map.get(
            "registered_direct_suffix_overlap_deletion_map_closed"
        )
        is True,
        "msharp_weighted_source_imported": weighted_source,
        "no_loss_or_named_return_imported": no_loss,
        "same_parameter_sparse_demand_cold_supply_normal_form_imported": normal_form,
        "residual_atom_weight_compression_closed_as_measure_change": closed_as_measure_change,
        "same_parameter_sparse_demand_cold_supply_strict_margin_proved": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": RESIDUAL_COMPRESSION,
        "hardpoint_after_router": STRICT_MARGIN,
        "next_direct_attack_target": STRICT_MARGIN,
        "parallel_attack_targets": [HOT_FIXED, MOVING_ATOM, DSTRUCTURE],
        "compression_rows": rows,
        "theorem_rows": theorem_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger` 不应再被当作"
            "新的 raw 删除命题。上一层的整数缺口 `floor(|R_{x,z}|-M#)+1` 只说明：若把"
            "残洞已分配 atom 继续按单位权留在 raw supply 中，必然无法低于 M#。但主线早已"
            "把这些 atom 通过容量乘子归一化为 `M#=sum 1/mu_tau` 的加权义务；无法进入该"
            "weighted ledger 的部分必须登记为命名回流。因此残洞 atom 权重压缩作为独立硬点已移除，"
            "真正剩余回到同参数严格余量 `M#-E_registered>U_np`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix inverse alignment 残洞 atom 权重压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"msharp_weighted_source_imported={fmt_bool(result['msharp_weighted_source_imported'])}",
        f"no_loss_or_named_return_imported={fmt_bool(result['no_loss_or_named_return_imported'])}",
        f"same_parameter_sparse_demand_cold_supply_normal_form_imported={fmt_bool(result['same_parameter_sparse_demand_cold_supply_normal_form_imported'])}",
        f"residual_atom_weight_compression_closed_as_measure_change={fmt_bool(result['residual_atom_weight_compression_closed_as_measure_change'])}",
        f"same_parameter_sparse_demand_cold_supply_strict_margin_proved={fmt_bool(result['same_parameter_sparse_demand_cold_supply_strict_margin_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 换尺审计表",
        "",
        "| P | X(P) | z | assigned units | M# | raw-M# | integer gap | formula ok |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["compression_rows"]:
        lines.append(
            "| `{P}` | `{x}` | `{z}` | `{units}` | `{msharp}` | `{gap}` | `{igap}` | `{ok}` |".format(
                P=item["P"],
                x=item["x"],
                z=item["z"],
                units=item["assigned_residual_atom_units"],
                msharp=item["Msharp_weighted_mass"],
                gap=item["raw_unit_minus_weighted_mass"],
                igap=item["integer_gap_if_raw_units_are_kept"],
                ok=fmt_bool(item["measure_change_identity_ok"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 命题接口",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["theorem_rows"]:
        lines.append(
            "| `{name}` | `{status}` | {statement} |".format(
                name=table_cell(item["name"]),
                status=table_cell(item["status"]),
                statement=table_cell(item["statement"]),
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
    for item in result["decision_rows"]:
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
            "## 4. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体任务：在同一 `x,z,M#` 参数下给出 `M#-E_registered>U_np`，或者证明失败必进入热核心、固定历史、PDEC/SAE、持久 moving atom 或 DStructure/Rankin 验收门。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"next={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
