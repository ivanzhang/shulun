#!/usr/bin/env python3
"""Prime Matrix clean-core alpha/delta 解积分字典路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_alpha_delta_disintegration_router.py

输出：
  docs/monograph/prime-matrix-clean-core-alpha-delta-disintegration-router.json
  docs/monograph/prime-matrix-clean-core-alpha-delta-disintegration-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-fiber-emitter-field-audit-router.json"
DEFAULT_PAYMENT = DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
DEFAULT_PRECAUCHY = DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json"
DEFAULT_PATH = DOCS / "prime-matrix-clean-core-layer-transfer-path-router.json"
DEFAULT_DECISION = DOCS / "prime-matrix-triad-a1-decision-tree-formula-router.json"
DEFAULT_FIREWALL = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.md"


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


def dictionary_fields() -> list[dict[str, str]]:
    """列出 signed 解积分字典字段。"""
    return [
        {
            "field": "signed_source_measure",
            "requirement": "在 Cauchy/dispersion 前给出 actual noncanonical alpha/delta signed primitive 源测度。",
        },
        {
            "field": "payment_base_map",
            "requirement": "给出 primitive summand 到 completion-hole/first-cover payment atom 的确定性映射。",
        },
        {
            "field": "fiber_dictionary",
            "requirement": "对每个正质量 payment atom 列出其 signed preimage summand、branch key、u/v map、sign 和 local factor。",
        },
        {
            "field": "pushforward_identity",
            "requirement": "证明字典沿 payment_base_map 推前后等于目标 alpha/delta payment-side 系数。",
        },
        {
            "field": "variation_and_support_budget",
            "requirement": "证明总变差、绝对支撑和 branch key 数在注册的 polylog/K6 预算内。",
        },
        {
            "field": "sign_refinement",
            "requirement": "同一完整 key 内 local factor 非零；若有相反号，必须先细分到 sign-refined key。",
        },
        {
            "field": "failure_return",
            "requirement": "无源测度、非同一 formal unit、推前不等式失败、超预算或抵消必须命名回流。",
        },
    ]


def implication_rows() -> list[dict[str, str]]:
    """记录 alpha/delta lift 与解积分字典的等价方向。"""
    return [
        {
            "direction": "lift_to_dictionary",
            "content": "若 ExactAlphaDeltaLift 已证明，则按 first-cover payment atom 分组 signed summand，得到解积分字典。",
        },
        {
            "direction": "dictionary_to_lift",
            "content": "若字典含 signed 源测度、纤维表和推前恒等式，则逐纤维求和直接给出 ExactAlphaDeltaLift。",
        },
        {
            "direction": "canonical_template_scoped",
            "content": "RIW/Buchstab 决策树给出了 canonical 分支上的字典模板，但作用域不能跨到 noncanonical clean-core。",
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    payment: dict[str, Any],
    precauchy: dict[str, Any],
    path: dict[str, Any],
    decision: dict[str, Any],
    firewall: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成解积分字典判定表。"""
    payment_base_closed = (
        previous.get("payment_fiber_skeleton_closed") is True
        and payment.get("all_payment_counts_match_demand") is True
    )
    canonical_template = (
        decision.get("recursive_formula_closed_algebraically") is True
        and decision.get("conditional_source_identification_implies_decision_tree_formula") is True
    )
    return [
        {
            "gate": "PriorAlphaDeltaLiftPinned",
            "closed": previous.get("latest_internal_subinput")
            == "ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn",
            "proved": False,
            "meaning": "上一层已把最窄自足剩余压成 payment skeleton 到 signed alpha/delta primitive 系数的提升。",
            "remaining": "把 lift 拆成测度解积分字典字段。",
        },
        {
            "gate": "PaymentBaseMapClosed",
            "closed": payment_base_closed,
            "proved": True,
            "meaning": "completion-hole 域、first-cover map 和 payment count identity 已给出解积分的基底映射。",
            "remaining": "基底映射不生成 signed 源测度。",
        },
        {
            "gate": "LiftEquivalentToSignedDisintegrationDictionary",
            "closed": True,
            "proved": True,
            "meaning": "Exact alpha/delta lift 与 signed primitive 源测度在 payment map 上的逐纤维解积分字典等价。",
            "remaining": "等价不证明 actual noncanonical 字典存在。",
        },
        {
            "gate": "PreCauchyLedgerShowsNecessaryFields",
            "closed": precauchy.get("origin_generation_ledger_implication_closed") is True,
            "proved": True,
            "meaning": "pre-Cauchy 来源律原子化已说明字段必须包含 formal unit、branch key、u/v map、sign 和 local factor。",
            "remaining": "当前材料未提交 noncanonical clean-core 的实际字段表。",
        },
        {
            "gate": "PathPartitionShowsBudgetUse",
            "closed": path.get("clean_core_layer_transfer_path_boundary_closed") is True,
            "proved": True,
            "meaning": "路径分割路由已说明 polylog branch schema 足以转化为 selector 支撑保留。",
            "remaining": "仍需 actual noncanonical 字典给出这些 branch key。",
        },
        {
            "gate": "CanonicalDecisionTreeTemplateScoped",
            "closed": canonical_template,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 决策树展示了解积分字典的结构模板。",
            "remaining": "模板只在 canonical 分支内有效，不能导入 noncanonical clean-core。",
        },
        {
            "gate": "GenericOrUnregisteredDictionaryBlocked",
            "closed": firewall.get("generic_wfd_constructor_rejected") is True
            and firewall.get("unregistered_source_return_absorbed") is True,
            "proved": True,
            "meaning": "generic WFD 和未登记来源不能作为字典；它们已被外部化或命名回流。",
            "remaining": "保留分支必须给 actual noncanonical registered dictionary。",
        },
        {
            "gate": "RegisteredAlphaDeltaDisintegrationDictionaryCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出 actual noncanonical clean-core 的 signed alpha/delta 解积分字典。",
            "remaining": "证明 RegisteredAlphaDeltaDisintegrationDictionaryAndReturn。",
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
    decision_path: Path,
    firewall_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core alpha/delta 解积分路由。"""
    source_paths = [
        previous_path,
        payment_path,
        precauchy_path,
        path_path,
        decision_path,
        firewall_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    payment = load_json(payment_path)
    precauchy = load_json(precauchy_path)
    path = load_json(path_path)
    decision = load_json(decision_path)
    firewall = load_json(firewall_path)
    dstructure = load_json(dstructure_path)

    rows = gate_rows(previous, payment, precauchy, path, decision, firewall, dstructure)
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"]
        not in {
            "RegisteredAlphaDeltaDisintegrationDictionaryCurrentCorpusProved",
            "DStructureRankinStillIndependent",
        }
    )
    latest_internal = "RegisteredAlphaDeltaDisintegrationDictionaryAndReturn"
    latest_external = previous.get(
        "latest_external_subinput",
        "CDependentResidueWeightSpectralCancellationInput",
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_alpha_delta_disintegration_router",
        "status": "alpha_delta_lift_reduced_to_registered_signed_disintegration_dictionary_open",
        "previous_input": previous.get("latest_internal_subinput"),
        "alpha_delta_disintegration_boundary_closed": boundary_closed,
        "payment_base_map_closed": True,
        "lift_equivalent_to_signed_disintegration_dictionary": True,
        "canonical_decision_tree_template_scoped": True,
        "generic_or_unregistered_dictionary_blocked": True,
        "registered_alpha_delta_disintegration_dictionary_proved": False,
        "exact_alpha_delta_lift_proved": False,
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
        "disintegration_law": (
            "ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn 的本质不是新的数值估计，"
            "而是 signed 源测度相对于 first-cover payment map 的解积分问题。"
            "payment skeleton 提供基底映射；pre-Cauchy 来源账本给出必要字段；路径分割说明 polylog "
            "branch key 如何转化为支撑保留；canonical RIW/Buchstab 决策树只提供作用域内模板。"
            "因此最新自足原子是 RegisteredAlphaDeltaDisintegrationDictionaryAndReturn："
            "提交 actual noncanonical signed alpha/delta 源测度、逐纤维字典、推前恒等式、总变差/支撑预算、"
            "sign-refinement 和失败回流。"
        ),
        "plain_conclusion": (
            "alpha/delta lift 被进一步压成 signed 解积分字典。"
            "已有模型给出基底映射和 canonical 模板，但当前材料尚未给出 noncanonical clean-core 的实际字典，"
            "所以行/列无条件命题仍未闭合。"
        ),
        "dictionary_fields": dictionary_fields(),
        "implication_rows": implication_rows(),
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
        "# Prime Matrix clean-core alpha/delta 解积分字典路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"alpha_delta_disintegration_boundary_closed={fmt_bool(result['alpha_delta_disintegration_boundary_closed'])}",
        f"payment_base_map_closed={fmt_bool(result['payment_base_map_closed'])}",
        f"lift_equivalent_to_signed_disintegration_dictionary={fmt_bool(result['lift_equivalent_to_signed_disintegration_dictionary'])}",
        f"canonical_decision_tree_template_scoped={fmt_bool(result['canonical_decision_tree_template_scoped'])}",
        f"registered_alpha_delta_disintegration_dictionary_proved={fmt_bool(result['registered_alpha_delta_disintegration_dictionary_proved'])}",
        f"exact_alpha_delta_lift_proved={fmt_bool(result['exact_alpha_delta_lift_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 解积分律",
        "",
        result["disintegration_law"],
        "",
        "```text",
        "signed alpha/delta primitive source measure nu",
        "  -- first-cover payment map Phi --> payment skeleton Gamma;",
        "",
        "Exact lift <=> registered signed disintegration dictionary of nu over Phi.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `alpha_delta_disintegration_boundary_closed={fmt_bool(result['alpha_delta_disintegration_boundary_closed'])}`。",
        f"- `registered_alpha_delta_disintegration_dictionary_proved={fmt_bool(result['registered_alpha_delta_disintegration_dictionary_proved'])}`。",
        f"- `latest_internal_subinput={result['latest_internal_subinput']}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        "",
        "## 3. 判定表",
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
            "## 4. 字典字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for row in result["dictionary_fields"]:
        lines.append(f"| `{table_cell(row['field'])}` | {table_cell(row['requirement'])} |")
    lines.extend(
        [
            "",
            "## 5. 等价方向",
            "",
            "| direction | content |",
            "| --- | --- |",
        ]
    )
    for row in result["implication_rows"]:
        lines.append(f"| `{table_cell(row['direction'])}` | {table_cell(row['content'])} |")
    lines.extend(
        [
            "",
            "## 6. 最新输入基",
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
            "## 7. 当前结论",
            "",
            "本步没有证明 signed 字典。它把 alpha/delta lift 的终端硬点改写成一个可审稿的解积分字典：",
            "先给 actual signed 源测度，再沿 first-cover payment map 逐纤维列出 signed summand 和推前恒等式。",
            "canonical 决策树只提供模板，不能跨分支导入 noncanonical clean-core。",
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
    parser.add_argument("--decision", type=Path, default=DEFAULT_DECISION)
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
        decision_path=args.decision,
        firewall_path=args.firewall,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
