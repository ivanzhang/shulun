#!/usr/bin/env python3
"""生成 strict actual emitter incidence 熵/纤维拆分证书。

用法示例：
  python3 experiments/prime_matrix_strict_actual_emitter_incidence_entropy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-actual-emitter-incidence-entropy-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"
OUT_MD = DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
    "prime-matrix-clean-core-fiber-emitter-field-audit-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
    "prime-matrix-clean-core-geometric-variation-branch-budget-router.json",
    "prime-matrix-triad-a1-exact-factor-support-router.json",
    "prime-matrix-registered-capacity-multiplier-discipline-router.json",
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
    incidence_router: dict[str, Any],
    field_audit: dict[str, Any],
    disintegration: dict[str, Any],
    branch_budget: dict[str, Any],
    exact_factor: dict[str, Any],
    multiplier: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 actual emitter incidence 熵/纤维拆分判定表。"""
    target = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
    next_basis = (
        "ActualEmitterSourceDomainEntropyLedger AND "
        "ExactUVMapFixedPairPolylogFiberBoundLedger"
    )
    return [
        {
            "gate": "ActualEmitterIncidenceTargetActive",
            "closed": incidence_router.get("terminal_gap_after_router") == target,
            "proved": False,
            "meaning": "上一层已把 exact-UV map rank 压成 actual emitter 的有界重数 incidence。",
            "remaining": target,
        },
        {
            "gate": "BoundedMultiplicitySplitPinned",
            "closed": True,
            "proved": False,
            "meaning": "有界重数 incidence 等价于源域足够大且每个 fixed pair 的原像纤维足够小。",
            "remaining": next_basis,
        },
        {
            "gate": "PaymentSkeletonDoesNotGiveSourceDomainEntropy",
            "closed": field_audit.get("payment_fiber_skeleton_closed") is True,
            "proved": True,
            "meaning": "payment count identity 只统计下游需求，不证明 pre-Cauchy emitted primitive summand 域的 absolute entropy。",
            "remaining": "ActualEmitterSourceDomainEntropyLedger。",
        },
        {
            "gate": "DisintegrationDictionaryDoesNotGiveFiberBound",
            "closed": disintegration.get("registered_alpha_delta_disintegration_dictionary_proved")
            is False,
            "proved": True,
            "meaning": "即使 signed 字典存在，还必须另证 fixed `(u,v)` 下 branch/sign/local-factor 原像数受控。",
            "remaining": "ExactUVMapFixedPairPolylogFiberBoundLedger。",
        },
        {
            "gate": "BranchBudgetNotEnoughForEntropy",
            "closed": branch_budget.get("branch_key_multiplicity_budget_proved") is False,
            "proved": True,
            "meaning": "branch key 复杂度预算尚未证明；即便证明 polylog key 数，也只给 fixed-pair 纤维上界的一部分，不给 image entropy。",
            "remaining": next_basis,
        },
        {
            "gate": "NaiveFactorSupportCountermodelImported",
            "closed": exact_factor.get("k4_k6_imply_exact_factor_support") is False,
            "proved": True,
            "meaning": "旧 factor-support 反模型显示内部 atom 可在一个 moving pair 内展开；不能用 residue-flat 代替源域 entropy。",
            "remaining": next_basis,
        },
        {
            "gate": "WeightComparabilityImported",
            "closed": multiplier.get("registered_capacity_multiplier_discipline_closed")
            is True,
            "proved": True,
            "meaning": "单 summand 权重和容量损失已登记，所以本步只处理 counting/entropy，不再处理权重偷换。",
            "remaining": next_basis,
        },
        {
            "gate": "CurrentCorpusIncidenceEntropyBasisProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料尚未证明源域 entropy 和 fixed-pair polylog fiber bound 的合取。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict actual emitter incidence 熵/纤维拆分证书。"""
    incidence_router = load_json(
        DOCS / "prime-matrix-strict-exact-uv-map-rank-incidence-router.json"
    )
    field_audit = load_json(DOCS / "prime-matrix-clean-core-fiber-emitter-field-audit-router.json")
    disintegration = load_json(DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.json")
    branch_budget = load_json(
        DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.json"
    )
    exact_factor = load_json(DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json")
    multiplier = load_json(DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json")

    target = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
    next_basis = (
        "ActualEmitterSourceDomainEntropyLedger AND "
        "ExactUVMapFixedPairPolylogFiberBoundLedger"
    )
    rows = build_rows(
        incidence_router=incidence_router,
        field_audit=field_audit,
        disintegration=disintegration,
        branch_budget=branch_budget,
        exact_factor=exact_factor,
        multiplier=multiplier,
    )
    return {
        "certificate_type": "prime_matrix_strict_actual_emitter_incidence_entropy_router",
        "status": "strict_actual_emitter_bounded_incidence_reduced_to_source_entropy_and_fixed_pair_fiber_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "actual_emitter_incidence_entropy_router_closed": True,
        "bounded_multiplicity_split_pinned": True,
        "payment_skeleton_not_source_entropy": True,
        "fixed_pair_fiber_bound_not_from_dictionary": True,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": next_basis,
        "split_contract": (
            "To prove bounded multiplicity for the actual emitter, prove both: "
            "(1) the pre-Cauchy emitted source domain has log-power absolute entropy/support, "
            "and (2) after branch/sign/local-factor refinement, each fixed exact (u,v) pair "
            "has only polylog many primitive preimages."
        ),
        "hard_law": (
            "有界重数 incidence 不是一个单字段性质。源域总支撑不足时，即使 fixed-pair 纤维小也无用；"
            "fixed-pair 纤维可很大时，即使 payment count 大也可能全部坍缩到一个 `(u,v)`。"
            "因此下一步必须同时证明 source-domain entropy 与 fixed-pair polylog fiber bound。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem` 被拆成两个不可混淆的账本："
            "`ActualEmitterSourceDomainEntropyLedger` 与 `ExactUVMapFixedPairPolylogFiberBoundLedger`。"
            "这仍是同一源熵目标内部的 incidence 证明，不是换命题。当前语料尚未证明这两个账本，"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict actual emitter incidence 熵/纤维拆分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"actual_emitter_incidence_entropy_router_closed={fmt_bool(result['actual_emitter_incidence_entropy_router_closed'])}",
        f"bounded_multiplicity_split_pinned={fmt_bool(result['bounded_multiplicity_split_pinned'])}",
        f"actual_emitter_source_domain_entropy_proved={fmt_bool(result['actual_emitter_source_domain_entropy_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"actual_emitter_exact_uv_bounded_multiplicity_incidence_proved={fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 拆分",
        "",
        "拆分前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "拆分合同：",
        "",
        "```text",
        result["split_contract"],
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
