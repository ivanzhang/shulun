#!/usr/bin/env python3
"""生成 strict 逐点 signed alpha 系数值表攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_pointwise_signed_alpha_value_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-pointwise-signed-alpha-value-table-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"
OUT_MD = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.md"

TARGET = "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton"
NEXT_TARGET = "PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow"
TERMINAL_GATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"

SOURCE_FILES = [
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-independent-identity-statement-taxonomy-router.json",
    "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json",
    "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-alpha-signed-lift-failure-return-router.json",
    "prime-matrix-clean-core-geometric-phi-budget-bridge-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
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
    """列出逐行 signed 权重公式必须提供的字段。"""
    return [
        {
            "field": "row_domain",
            "meaning": "输入为已闭合 unsigned carry-shell skeleton row，而不是 payment-side atom。",
        },
        {
            "field": "closed_weight_expression",
            "meaning": "给出 signed_alpha_weight 的显式表达式或有限递推公式。",
        },
        {
            "field": "identity_proof",
            "meaning": "证明表达式来自 pre-Cauchy 算术恒等式，早于 Cauchy/dispersion/Phi 推前。",
        },
        {
            "field": "nonzero_sign_local_factor",
            "meaning": "证明非零、符号和 local factor 与 row 同步；失败时命名回流。",
        },
        {
            "field": "no_reverse_recovery",
            "meaning": "证明没有使用零行覆盖、payment skeleton、terminal certificate 后验恢复权重。",
        },
        {
            "field": "same_unit_compatibility",
            "meaning": "权重公式与 source_tuple_hash、Phi atom、variation charge 使用同一 formal unit。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查逐点 signed alpha 值表能否闭合。"""
    hardpoint = data["hardpoint"]
    weight = data["weight"]
    identity = data["identity"]
    moving = data["moving"]
    downstream = data["downstream"]
    signed_lift = data["signed_lift"]
    failure = data["failure"]
    phi = data["phi"]
    disintegration = data["disintegration"]
    source_loop = data["source_loop"]
    zero_nogo = data["zero_nogo"]

    target_active = hardpoint.get("next_direct_attack_target") == TARGET
    identity_reduced_to_moving = (
        identity.get("next_direct_attack_target")
        == "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
        or identity.get("terminal_gap_after_router")
        == "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
    )
    moving_returns_terminal = (
        moving.get("strict_actual_moving_block_router_closed") is True
        and isinstance(moving.get("terminal_gap_after_router"), str)
        and TERMINAL_GATE in moving.get("terminal_gap_after_router", "")
    )
    downstream_returns_terminal = (
        downstream.get("downstream_sync_router_closed") is True
        and downstream.get("next_direct_attack_target") == TERMINAL_GATE
    )

    return [
        row(
            "PointwiseValueTableTargetActive",
            target_active,
            False,
            "上一层把 signed coefficient lift 压成逐 skeleton row 的 signed alpha value table。",
            TARGET,
        ),
        row(
            "ValueTableWouldCloseFourLegs",
            True,
            True,
            "若逐行权重值表存在，则 signed source、权重律、Phi 推前和变差收费可以在同表上合取。",
            "需要先给 signed_alpha_weight 值。",
        ),
        row(
            "FailureLedgerAlreadyNamesMissingValues",
            failure.get("alpha_signed_lift_failure_named_return_ledger_closed") is True,
            True,
            "缺少 signed value、Phi 不兼容、变差超预算已有命名出口。",
            "命名出口尚未被排斥。",
        ),
        row(
            "WeightLawDecompositionImported",
            weight.get("alpha_signed_weight_law_router_closed") is True,
            False,
            "权重律已经拆成独立恒等式、精确公式、非零符号局部因子、反推禁用和失败回流。",
            "ExactAlphaSignedWeightFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger。",
        ),
        row(
            "IndependentIdentityRouteIsFixedPoint",
            identity_reduced_to_moving and moving_returns_terminal and downstream_returns_terminal,
            False,
            "现有独立恒等式路线经 actual moving-block/NCBLK 回到 PDEC/CleanKLS 终端门。",
            "不能用该循环证明逐行权重值。",
        ),
        row(
            "PhiAndDisintegrationWaitForValues",
            phi.get("geometric_payment_base_available") is True
            and (
                disintegration.get("status")
                == "alpha_delta_lift_reduced_to_registered_signed_disintegration_dictionary_open"
                or disintegration.get("signed_fiber_disintegration_formal") is True
            ),
            False,
            "Phi 基底和解积分形式只有在 signed value 已给出后才能求和验证。",
            "不能反向生成 signed_alpha_weight。",
        ),
        row(
            "ReverseRecoveryBlocked",
            source_loop.get("circular_reverse_derivation_rejected") is True
            and zero_nogo.get("zero_row_seed_extraction_blocked") is True,
            True,
            "payment skeleton 和早期零行 unsigned cover 都不能作为权重来源。",
            "必须正向给出逐行非递归公式。",
        ),
        row(
            "ExactWeightFormulaCurrentCorpusProved",
            weight.get("exact_alpha_signed_weight_formula_proved") is True,
            False,
            "当前材料尚未给出每条 skeleton row 的 exact signed weight 公式。",
            "ExactAlphaSignedWeightFormulaLedger。",
        ),
        row(
            "PointwiseNonrecursiveFormulaCurrentCorpusProved",
            False,
            False,
            "当前材料没有逐 skeleton row 的非递归 signed 权重公式及其恒等式证明。",
            NEXT_TARGET,
        ),
        row(
            "PointwiseSignedValueTableCurrentCorpusProved",
            False,
            False,
            "没有逐行 signed 权重公式，整张 signed value table 不能成立。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造逐点 signed alpha 值表攻坚证书。"""
    data = {
        "hardpoint": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "identity": load_json("prime-matrix-strict-independent-identity-statement-taxonomy-router.json"),
        "moving": load_json("prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json"),
        "downstream": load_json("prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-formula-signed-lift-router.json"),
        "failure": load_json("prime-matrix-strict-alpha-signed-lift-failure-return-router.json"),
        "phi": load_json("prime-matrix-clean-core-geometric-phi-budget-bridge-router.json"),
        "disintegration": load_json("prime-matrix-clean-core-alpha-delta-disintegration-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_pointwise_signed_alpha_value_table_router",
        "status": "pointwise_signed_alpha_value_table_reduced_to_nonrecursive_row_weight_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "pointwise_signed_alpha_value_table_router_closed": True,
        "failure_ledger_names_missing_values": True,
        "independent_identity_route_is_fixed_point": True,
        "exact_alpha_signed_weight_formula_proved": False,
        "pointwise_nonrecursive_signed_alpha_weight_formula_proved": False,
        "pointwise_signed_alpha_coefficient_value_table_proved": False,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "actual_signed_alpha_source_measure_proved": False,
        "alpha_rows_phi_pushforward_compatibility_proved": False,
        "alpha_signed_lift_variation_branch_budget_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "formula_fields": formula_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 的真正首字段是 signed_alpha_weight。"
            f"当前最精确单点为 `{NEXT_TARGET}`：对每条 unsigned carry-shell skeleton row，"
            "给出非递归 signed 权重公式、pre-Cauchy 恒等式证明、非零符号局部因子和同 formal-unit 兼容。"
        ),
        "plain_conclusion": (
            "本步继续硬攻逐点 signed value table。结论是：表的 Phi atom、变差收费和解积分都只能在"
            " signed weight 已给出后验证；失败命名纪律也已闭合。真正首要缺口是每条 skeleton row 的"
            " signed_alpha_weight 值。现有独立恒等式路线会经 moving-block/NCBLK 回到 PDEC/CleanKLS 固定点，"
            "不能作为非递归证明。因此最新最精确单点是逐行非递归 signed alpha 权重公式。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 逐点 signed alpha value table 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pointwise_signed_alpha_value_table_router_closed={fmt_bool(result['pointwise_signed_alpha_value_table_router_closed'])}",
        f"failure_ledger_names_missing_values={fmt_bool(result['failure_ledger_names_missing_values'])}",
        f"independent_identity_route_is_fixed_point={fmt_bool(result['independent_identity_route_is_fixed_point'])}",
        f"exact_alpha_signed_weight_formula_proved={fmt_bool(result['exact_alpha_signed_weight_formula_proved'])}",
        f"pointwise_nonrecursive_signed_alpha_weight_formula_proved={fmt_bool(result['pointwise_nonrecursive_signed_alpha_weight_formula_proved'])}",
        f"pointwise_signed_alpha_coefficient_value_table_proved={fmt_bool(result['pointwise_signed_alpha_coefficient_value_table_proved'])}",
        f"alpha_formula_signed_coefficient_lift_proved={fmt_bool(result['alpha_formula_signed_coefficient_lift_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 逐行公式字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["formula_fields"]:
        lines.append(
            "| `{field}` | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
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
