#!/usr/bin/env python3
"""Prime Matrix signed 几何变差锁兼容预算合并路由器。

用法示例：
  python3 experiments/prime_matrix_signed_geometric_variation_compatibility_merger.py

输出：
  docs/monograph/prime-matrix-signed-geometric-variation-compatibility-merger.json
  docs/monograph/prime-matrix-signed-geometric-variation-compatibility-merger.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-dls-fixedwheel-pdec-return-schema-router.json"
DEFAULT_GEOM = DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.md"
DEFAULT_DISINTEGRATION = DOCS / "prime-matrix-clean-core-disintegration-automaticity-router.md"
DEFAULT_ALPHA = DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.md"
DEFAULT_CONSTRUCTOR = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-signed-geometric-variation-compatibility-merger.json"
DEFAULT_MD = DOCS / "prime-matrix-signed-geometric-variation-compatibility-merger.md"

SOURCE_ATOM = "ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn"
OLD_ATOM = "SignedGeometricLedgerVariationBranchLiftAndReturn"
NEW_ATOM = "ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn"
MODEL_ATOM = "ExplicitModelGapAndFiniteDPRCLedger"
NEXT_ATOM = NEW_ATOM


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


def merge_source_and_signed_atoms(text: str) -> str:
    """把 source identity 与 signed variation 合并为同一兼容预算原子。"""
    patterns = [
        (
            f"{SOURCE_ATOM} AND {MODEL_ATOM} AND {OLD_ATOM}",
            f"{NEW_ATOM} AND {MODEL_ATOM}",
        ),
        (
            f"{SOURCE_ATOM} AND {OLD_ATOM} AND {MODEL_ATOM}",
            f"{NEW_ATOM} AND {MODEL_ATOM}",
        ),
        (
            f"{SOURCE_ATOM} AND {OLD_ATOM}",
            NEW_ATOM,
        ),
    ]
    result = text
    for old, new in patterns:
        result = result.replace(old, new)
    if SOURCE_ATOM in result or OLD_ATOM in result:
        result = result.replace(SOURCE_ATOM, NEW_ATOM)
        for pattern in [f" AND {OLD_ATOM}", f"{OLD_ATOM} AND ", OLD_ATOM]:
            result = result.replace(pattern, "")
    return result


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
    previous: dict[str, Any],
    geom_text: str,
    disintegration_text: str,
    alpha_text: str,
    constructor_text: str,
) -> list[dict[str, Any]]:
    """生成 signed 几何变差锁合并判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    source_identity_present = SOURCE_ATOM in basis
    geom_split = (
        "SignedGeometricLedgerVariationBranchLiftAndReturn" in geom_text
        and "actual signed source 的总变差和 branch key 复杂度" in geom_text
        and "不能由 unsigned 几何自动推出" in geom_text
    )
    disintegration_boundary = (
        "disintegration_automaticity_boundary_closed=true" in disintegration_text
        and "actual signed 源测度与 Phi 兼容恒等式、总变差和 branch 预算" in disintegration_text
        and NEW_ATOM in disintegration_text
    )
    alpha_dictionary_fields = (
        "variation_and_support_budget" in alpha_text
        and "pushforward_identity" in alpha_text
        and "signed_source_measure" in alpha_text
    )
    constructor_fields = (
        "actual_noncanonical_primitive_constructor_formula_proved=false" in constructor_text
        and "branch key" in constructor_text
        and "sign" in constructor_text
        and "local factor" in constructor_text
    )
    merger_closed = all(
        [
            active,
            source_identity_present,
            geom_split,
            disintegration_boundary,
            alpha_dictionary_fields,
            constructor_fields,
        ]
    )
    return [
        row(
            "SignedVariationGateActive",
            active,
            True,
            "当前输入基仍含 SignedGeometricLedgerVariationBranchLiftAndReturn。",
            "检查它是否应独立保留。",
        ),
        row(
            "SourceIdentityPairedInSameBasis",
            source_identity_present,
            True,
            "同一输入基中已经有 ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn。",
            "signed 变差不能脱离 source/Phi 恒等式单独证明。",
        ),
        row(
            "GeometricBudgetSplitImported",
            geom_split,
            True,
            "几何层只给 unsigned payment 账本；signed 总变差与 branch key 是 source 层字段。",
            "不能由斜线/轮筛几何自动推出。",
        ),
        row(
            "DisintegrationAutomaticityPinsCombinedGate",
            disintegration_boundary,
            True,
            "逐纤维解积分形式上闭合，真实硬点是 actual signed source、Phi 推前、总变差和 branch 预算合包。",
            NEW_ATOM,
        ),
        row(
            "AlphaDeltaDictionaryFieldsCoverVariation",
            alpha_dictionary_fields,
            True,
            "alpha/delta 解积分字典已经把 pushforward、variation/support、sign refinement 列为同一字段组。",
            "字段尚未填，不是已经证明。",
        ),
        row(
            "ConstructorSourceFieldsCoverBranchKeys",
            constructor_fields,
            True,
            "actual noncanonical 构造器公式必须发出 branch key、u/v、sign 和 local factor。",
            "构造器公式仍未证明。",
        ),
        row(
            "NoIndependentSignedVariationAtom",
            merger_closed,
            True,
            "signed variation lift 不应作为独立原子；它是 actual signed source/Phi compatibility budget 的字段。",
            NEW_ATOM,
        ),
        row(
            OLD_ATOM,
            merger_closed,
            True,
            "该硬点作为独立输入已合并到 ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn。",
            "合并不证明兼容预算。",
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "当前材料尚未给出 actual signed source、Phi 推前恒等式、总变差和 branch key 预算。",
            NEW_ATOM,
        ),
        row(
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            False,
            False,
            "源侧预算完成后仍需 DStructure/Tail-log4/finite Rankin 独立验收。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(
    previous_path: Path,
    geom_path: Path,
    disintegration_path: Path,
    alpha_path: Path,
    constructor_path: Path,
) -> dict[str, Any]:
    """执行 signed 几何变差锁合并路由。"""
    source_paths = [
        previous_path,
        geom_path,
        disintegration_path,
        alpha_path,
        constructor_path,
    ]
    previous = load_json(previous_path)
    geom_text = geom_path.read_text(encoding="utf-8")
    disintegration_text = disintegration_path.read_text(encoding="utf-8")
    alpha_text = alpha_path.read_text(encoding="utf-8")
    constructor_text = constructor_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        geom_text=geom_text,
        disintegration_text=disintegration_text,
        alpha_text=alpha_text,
        constructor_text=constructor_text,
    )
    merger_closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    latest_self = merge_source_and_signed_atoms(previous.get("latest_self_contained_basis", ""))
    latest_cond = merge_source_and_signed_atoms(previous.get("latest_conditional_basis", ""))
    return {
        "certificate_type": "signed_geometric_variation_compatibility_merger",
        "status": "signed_variation_independent_atom_merged_compatibility_budget_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "signed_variation_independent_atom_removed": merger_closed,
        "actual_signed_source_phi_compatibility_budget_proved": False,
        "actual_noncanonical_constructor_formula_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": f"{SOURCE_ATOM} AND {OLD_ATOM}",
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {f"{SOURCE_ATOM} AND {OLD_ATOM}": NEW_ATOM},
        "next_priority": NEXT_ATOM,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步没有证明 signed source 兼容预算；它关闭的是一个边界误差："
            "SignedGeometricLedgerVariationBranchLiftAndReturn 不是独立原子，而是 actual signed source、"
            "Phi 推前恒等式、总变差/支撑预算和 branch key 预算同一个兼容包的字段。"
            "因此 source identity 与 signed variation 合并为 ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix signed 几何变差锁兼容预算合并路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        (
            "signed_variation_independent_atom_removed="
            f"{fmt_bool(result['signed_variation_independent_atom_removed'])}"
        ),
        (
            "actual_signed_source_phi_compatibility_budget_proved="
            f"{fmt_bool(result['actual_signed_source_phi_compatibility_budget_proved'])}"
        ),
        (
            "actual_noncanonical_constructor_formula_proved="
            f"{fmt_bool(result['actual_noncanonical_constructor_formula_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "这一步合并的是输入边界，不使用真实样本缺席，也不证明兼容预算本身。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 最新输入基",
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
            "## 4. 下一步",
            "",
            f"下一步最窄目标为 `{result['next_priority']}`：给出 actual noncanonical signed source、"
            "Phi 推前恒等式、总变差/支撑预算和 branch key 预算，或把失败者命名回流。",
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
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--geom", type=Path, default=DEFAULT_GEOM)
    parser.add_argument("--disintegration", type=Path, default=DEFAULT_DISINTEGRATION)
    parser.add_argument("--alpha", type=Path, default=DEFAULT_ALPHA)
    parser.add_argument("--constructor", type=Path, default=DEFAULT_CONSTRUCTOR)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        geom_path=args.geom,
        disintegration_path=args.disintegration,
        alpha_path=args.alpha,
        constructor_path=args.constructor,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
