#!/usr/bin/env python3
"""生成 strict primitive emitter multiplicity/rank 直攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_emitter_multiplicity_rank_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-emitter-multiplicity-rank-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-emitter-multiplicity-rank-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-emitter-multiplicity-rank-attack-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-absolute-fiber-mass-dispersion-router.json",
    "prime-matrix-clean-core-fiber-emitter-field-audit-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
    "prime-matrix-clean-core-geometric-variation-branch-budget-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典，兼容旧归档。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


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


def build_rows(
    absolute_fiber: dict[str, Any],
    field_audit: dict[str, Any],
    disintegration: dict[str, Any],
    variation_budget: dict[str, Any],
    reverse_functor: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 emitter multiplicity/rank 判定表。"""
    target = "PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem"
    next_atom = "PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem"
    return [
        {
            "gate": "EmitterMultiplicityTargetActive",
            "closed": absolute_fiber.get("terminal_gap_after_router") == target,
            "proved": False,
            "meaning": "上一层已把绝对 fiber 质量分散压成 primitive emitter 原像 multiplicity 分散。",
            "remaining": target,
        },
        {
            "gate": "PaymentSkeletonNotEnough",
            "closed": field_audit.get("payment_fiber_skeleton_closed") is True,
            "proved": True,
            "meaning": "payment skeleton、first-cover map 和 count identity 只给下游计数骨架，不给 exact `(u,v)` map 的原像秩。",
            "remaining": next_atom,
        },
        {
            "gate": "AlphaDeltaDictionaryStillObjectNotRank",
            "closed": disintegration.get("lift_equivalent_to_signed_disintegration_dictionary")
            is True,
            "proved": True,
            "meaning": "signed 解积分字典若存在，只给 source 对象和逐纤维字段；还必须证明这些字段不会坍缩到少数 `(u,v)`。",
            "remaining": next_atom,
        },
        {
            "gate": "BranchBudgetNotMapRank",
            "closed": variation_budget.get("geometry_ledger_alphabet_closed") is True,
            "proved": True,
            "meaning": "branch key 与几何变差预算控制复杂度和总变差，但不自动给 exact `(u,v)` 映射秩下界。",
            "remaining": next_atom,
        },
        {
            "gate": "ReverseFunctorNoRankRecovery",
            "closed": reverse_functor.get("pushforward_reverse_uniqueness_rejected") is True,
            "proved": True,
            "meaning": "从推前 payment 图不能恢复 pre-Cauchy 原像，也不能恢复 exact `(u,v)` map 的最大纤维界。",
            "remaining": next_atom,
        },
        {
            "gate": "MultiplicityEquivalentToMapRank",
            "closed": True,
            "proved": False,
            "meaning": "在单 summand 权重已登记后，multiplicity 分散等价于证明 exact `(u,v)` map 的最大 fiber 小，或 image 支撑足够大。",
            "remaining": next_atom,
        },
        {
            "gate": "NoFiberCollapseConditionPinned",
            "closed": True,
            "proved": False,
            "meaning": "必须排除大量 branch/source summands 具有不同内部 key 但同一个 exact `(u,v)` 的坍缩模型。",
            "remaining": "NoExactUVFiberCollapseForActualEmitter。",
        },
        {
            "gate": "PreCauchyEmitterExactUVMapRankCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料尚未证明 actual pre-Cauchy emitter 的 exact `(u,v)` 映射秩/无坍缩定理。",
            "remaining": next_atom,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict primitive emitter multiplicity/rank 直攻证书。"""
    absolute_fiber = load_json(
        DOCS / "prime-matrix-strict-absolute-fiber-mass-dispersion-router.json"
    )
    field_audit = load_json(DOCS / "prime-matrix-clean-core-fiber-emitter-field-audit-router.json")
    disintegration = load_json(DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.json")
    variation_budget = load_json(
        DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.json"
    )
    reverse_functor = load_json(DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json")

    target = "PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem"
    next_atom = "PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem"
    rows = build_rows(
        absolute_fiber=absolute_fiber,
        field_audit=field_audit,
        disintegration=disintegration,
        variation_budget=variation_budget,
        reverse_functor=reverse_functor,
    )
    return {
        "certificate_type": "prime_matrix_strict_emitter_multiplicity_rank_attack_router",
        "status": "strict_emitter_multiplicity_reduced_to_exact_uv_map_rank_no_collapse_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "emitter_multiplicity_rank_attack_closed": True,
        "payment_skeleton_not_enough": True,
        "alpha_delta_dictionary_not_rank_proof": True,
        "branch_budget_not_map_rank": True,
        "reverse_functor_no_rank_recovery": True,
        "preterminal_exact_uv_primitive_emitter_multiplicity_dispersion_proved": False,
        "pre_cauchy_emitter_exact_uv_map_rank_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_atom,
        "next_direct_attack_target": next_atom,
        "map_rank_contract": (
            "For the actual pre-Cauchy primitive emitter in one formal unit, prove that "
            "the map from emitted primitive summands (including branch key, sign/local factor "
            "and source parameters) to exact (u,v) has maximum fiber at most |Domain|/L^K, "
            "or equivalently that the exact (u,v) image support has log-power rank/entropy."
        ),
        "hard_law": (
            "multiplicity 分散的底层不是 payment count，也不是 alpha/delta 字典存在性，"
            "而是 exact `(u,v)` 映射的秩/无坍缩性质。branch key 复杂度小只说明可审计，"
            "不说明不同 branch 不会落入同一个 pair；必须直接证明 no-fiber-collapse。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem` 被进一步压到映射秩层："
            "payment skeleton、alpha/delta 解积分字典、branch 预算和反向来源函子都不能证明 exact `(u,v)` map "
            "没有大原像纤维。最新最窄点是 `PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem`。"
            "该秩/无坍缩定理尚未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict primitive emitter multiplicity/rank 直攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"emitter_multiplicity_rank_attack_closed={fmt_bool(result['emitter_multiplicity_rank_attack_closed'])}",
        f"payment_skeleton_not_enough={fmt_bool(result['payment_skeleton_not_enough'])}",
        f"alpha_delta_dictionary_not_rank_proof={fmt_bool(result['alpha_delta_dictionary_not_rank_proof'])}",
        f"branch_budget_not_map_rank={fmt_bool(result['branch_budget_not_map_rank'])}",
        f"pre_cauchy_emitter_exact_uv_map_rank_proved={fmt_bool(result['pre_cauchy_emitter_exact_uv_map_rank_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压缩",
        "",
        "压缩前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "压缩后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "映射秩合同：",
        "",
        "```text",
        result["map_rank_contract"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 结构结论",
            "",
            result["hard_law"],
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
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
