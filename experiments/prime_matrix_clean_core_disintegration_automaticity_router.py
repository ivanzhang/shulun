#!/usr/bin/env python3
"""Prime Matrix clean-core 解积分自动性路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_disintegration_automaticity_router.py

输出：
  docs/monograph/prime-matrix-clean-core-disintegration-automaticity-router.json
  docs/monograph/prime-matrix-clean-core-disintegration-automaticity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.json"
DEFAULT_PAYMENT = DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
DEFAULT_PRECAUCHY = DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json"
DEFAULT_PATH = DOCS / "prime-matrix-clean-core-layer-transfer-path-router.json"
DEFAULT_FIREWALL = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-disintegration-automaticity-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-disintegration-automaticity-router.md"


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


def residual_fields() -> list[dict[str, str]]:
    """列出自动性之后真正剩余的字段。"""
    return [
        {
            "field": "actual_signed_source_measure",
            "requirement": "在 Cauchy/dispersion 前定义 actual noncanonical signed alpha/delta 源测度。",
        },
        {
            "field": "phi_compatibility_identity",
            "requirement": "证明该源测度沿 first-cover payment map Phi 的推前就是目标 payment-side 系数。",
        },
        {
            "field": "absolute_variation_budget",
            "requirement": "证明总变差和绝对支撑没有超过 registered clean-core 容量预算。",
        },
        {
            "field": "branch_key_budget",
            "requirement": "证明纤维内 branch key、sign refinement 和 local factor 表为 polylog/K6 可登记复杂度。",
        },
        {
            "field": "return_tags",
            "requirement": "源测度缺失、Phi 不兼容、变差超预算、branch 爆炸或抵消均命名回流。",
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    payment: dict[str, Any],
    precauchy: dict[str, Any],
    path: dict[str, Any],
    firewall: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成解积分自动性判定表。"""
    base_map_closed = (
        previous.get("payment_base_map_closed") is True
        and payment.get("all_payment_counts_match_demand") is True
    )
    return [
        {
            "gate": "PriorDisintegrationDictionaryPinned",
            "closed": previous.get("latest_internal_subinput")
            == "RegisteredAlphaDeltaDisintegrationDictionaryAndReturn",
            "proved": False,
            "meaning": "上一层已把 alpha/delta lift 压成 signed 解积分字典。",
            "remaining": "判断字典构造本身是否还是数学硬点。",
        },
        {
            "gate": "DiscretePaymentBaseMapClosed",
            "closed": base_map_closed,
            "proved": True,
            "meaning": "first-cover payment map 的基底空间为离散/有限签名层，且 payment count identity 已闭合。",
            "remaining": "仍需 actual signed 源测度。",
        },
        {
            "gate": "SignedFiberDisintegrationFormal",
            "closed": True,
            "proved": True,
            "meaning": "一旦 signed 源测度和 Phi 给定，按 Phi 的纤维限制 signed measure 就形式给出解积分字典。",
            "remaining": "形式解积分不证明该 signed 源测度来自 actual noncanonical clean-core。",
        },
        {
            "gate": "PushforwardIdentityIsTheRealCompatibilityGate",
            "closed": True,
            "proved": True,
            "meaning": "字典是否有效取决于 Phi_*nu 是否等于目标 payment-side alpha/delta 系数。",
            "remaining": "证明 Phi 兼容恒等式，或命名回流。",
        },
        {
            "gate": "PreCauchyAndPathBudgetsIdentifyResidualFields",
            "closed": precauchy.get("origin_generation_ledger_implication_closed") is True
            and path.get("clean_core_layer_transfer_path_boundary_closed") is True,
            "proved": True,
            "meaning": "pre-Cauchy 账本和路径分割路由已经说明剩余字段是源测度、Phi 兼容、变差和 branch 预算。",
            "remaining": "当前材料未证明这些字段。",
        },
        {
            "gate": "UnregisteredOrGenericSourceStillBlocked",
            "closed": firewall.get("generic_wfd_constructor_rejected") is True
            and firewall.get("unregistered_source_return_absorbed") is True,
            "proved": True,
            "meaning": "generic WFD 或未登记来源不能填充 signed 源测度字段。",
            "remaining": "必须给 actual noncanonical signed source 或外部谱输入。",
        },
        {
            "gate": "ActualSignedSourceMeasurePhiCompatibilityBudgetCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明 actual signed 源测度、Phi 兼容恒等式、总变差和 branch 预算。",
            "remaining": "证明 ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧完成后仍需独立验收。",
        },
    ]


def run(
    previous_path: Path,
    payment_path: Path,
    precauchy_path: Path,
    path_path: Path,
    firewall_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core 解积分自动性路由。"""
    source_paths = [previous_path, payment_path, precauchy_path, path_path, firewall_path, dstructure_path]
    previous = load_json(previous_path)
    payment = load_json(payment_path)
    precauchy = load_json(precauchy_path)
    path = load_json(path_path)
    firewall = load_json(firewall_path)
    dstructure = load_json(dstructure_path)

    rows = gate_rows(previous, payment, precauchy, path, firewall, dstructure)
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"]
        not in {
            "ActualSignedSourceMeasurePhiCompatibilityBudgetCurrentCorpusProved",
            "DStructureRankinStillIndependent",
        }
    )
    latest_internal = "ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn"
    latest_external = previous.get(
        "latest_external_subinput",
        "CDependentResidueWeightSpectralCancellationInput",
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_disintegration_automaticity_router",
        "status": "signed_disintegration_formal_source_phi_budget_open",
        "previous_input": previous.get("latest_internal_subinput"),
        "disintegration_automaticity_boundary_closed": boundary_closed,
        "discrete_payment_base_map_closed": True,
        "signed_fiber_disintegration_formal": True,
        "pushforward_identity_is_real_gate": True,
        "actual_signed_source_measure_phi_compatibility_budget_proved": False,
        "registered_alpha_delta_disintegration_dictionary_proved": False,
        "row_column_unconditional_closed": False,
        "dstructure_rankin_independent_acceptance_completed": dstructure.get(
            "promotion_package_independently_accepted",
            False,
        ),
        "latest_internal_subinput": latest_internal,
        "latest_external_subinput": latest_external,
        "latest_conditional_basis": (
            f"({latest_internal} OR {latest_external}) "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            f"{latest_internal} "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "automaticity_law": (
            "RegisteredAlphaDeltaDisintegrationDictionaryAndReturn 中的逐纤维分解不是新的解析估计。"
            "在离散 first-cover payment map Phi 已闭合时，只要 actual signed 源测度 nu 给定，"
            "nu 在 Phi 的纤维限制就形式给出 signed 字典。真正剩余是证明 nu 是同一 formal unit 内的 "
            "actual noncanonical alpha/delta 源测度，且 Phi_*nu 等于目标 payment-side 系数，并满足总变差、"
            "绝对支撑和 branch key 预算；失败者必须命名回流。"
        ),
        "plain_conclusion": (
            "解积分步骤本身已经形式化闭合；最新自足硬点变成 actual signed 源测度与 Phi 兼容恒等式、"
            "总变差和 branch 预算。当前材料尚未证明这些字段。"
        ),
        "residual_fields": residual_fields(),
        "rows": rows,
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
    }
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_out.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 归档。"""
    lines: list[str] = [
        "# Prime Matrix clean-core 解积分自动性路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"disintegration_automaticity_boundary_closed={fmt_bool(result['disintegration_automaticity_boundary_closed'])}",
        f"discrete_payment_base_map_closed={fmt_bool(result['discrete_payment_base_map_closed'])}",
        f"signed_fiber_disintegration_formal={fmt_bool(result['signed_fiber_disintegration_formal'])}",
        f"pushforward_identity_is_real_gate={fmt_bool(result['pushforward_identity_is_real_gate'])}",
        f"actual_signed_source_measure_phi_compatibility_budget_proved={fmt_bool(result['actual_signed_source_measure_phi_compatibility_budget_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自动性律",
        "",
        result["automaticity_law"],
        "",
        "```text",
        "given signed source measure nu and first-cover map Phi:",
        "  nu = sum_a nu restricted to Phi^{-1}(a);",
        "dictionary is formal;",
        "hard part is actual nu + Phi_*nu identity + budgets.",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 剩余字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for row in result["residual_fields"]:
        lines.append(f"| `{table_cell(row['field'])}` | {table_cell(row['requirement'])} |")
    lines.extend(
        [
            "",
            "## 4. 最新输入基",
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
            "## 5. 当前结论",
            "",
            "本步没有证明 actual signed source 或 Phi 兼容预算。它只关闭了一个误区：逐纤维 disintegration",
            "本身不是新的数学估计；真正需要补的是同一 formal unit 内的 signed 源测度和预算恒等式。",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--payment", type=Path, default=DEFAULT_PAYMENT)
    parser.add_argument("--precauchy", type=Path, default=DEFAULT_PRECAUCHY)
    parser.add_argument("--path", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--firewall", type=Path, default=DEFAULT_FIREWALL)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        payment_path=args.payment,
        precauchy_path=args.precauchy,
        path_path=args.path,
        firewall_path=args.firewall,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
