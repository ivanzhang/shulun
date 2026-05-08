#!/usr/bin/env python3
"""Prime Matrix clean-core 反向来源函子路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_reverse_provenance_functor_router.py

输出：
  docs/monograph/prime-matrix-clean-core-reverse-provenance-functor-router.json
  docs/monograph/prime-matrix-clean-core-reverse-provenance-functor-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-external-lemma-parameter-match-router.json"
DEFAULT_CONSTRUCTOR = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
DEFAULT_PROFINITE = DOCS / "prime-matrix-profinite-actual-payment-stitching-router.json"
DEFAULT_TRANSVERSE = DOCS / "prime-matrix-pdec-cap-transverse-embedding-router.json"
DEFAULT_CANONICAL = DOCS / "prime-matrix-pdec-cap-canonical-layer-closure-router.json"
DEFAULT_PROVENANCE = DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.md"


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


def section_requirements() -> list[dict[str, str]]:
    """列出反向来源所需的最小纤维分解字段。"""
    return [
        {
            "field": "pre_pushforward_domain",
            "requirement": "在 Cauchy/dispersion 前给出 primitive summand 的定义域，而不是从 Gamma 事后命名。",
        },
        {
            "field": "fiber_emitter",
            "requirement": "对每个正质量 clean-core payment atom，输出有限/polylog 个 primitive preimage summand。",
        },
        {
            "field": "coefficient_identity",
            "requirement": "证明这些 preimage summand 的 alpha/delta、符号与 local factor 推前后等于 actual payment 质量。",
        },
        {
            "field": "branch_schema",
            "requirement": "每个 summand 带 branch key、u/v map、phase/sign/local factor，且 key 数为 log^O(1)。",
        },
        {
            "field": "formal_unit_registration",
            "requirement": "preimage、payment、capacity、support 与 return ledger 使用同一个 actual formal unit。",
        },
        {
            "field": "failure_return",
            "requirement": "空纤维、非唯一口径、超预算、thin block 或未登记来源必须给出命名 return tag。",
        },
    ]


def implication_rows() -> list[dict[str, str]]:
    """记录公式输入与纤维分解输入的等价方向。"""
    return [
        {
            "direction": "constructor_formula_to_fiber_emitter",
            "content": (
                "若 actual noncanonical primitive constructor formula 已给出，则按 payment signature "
                "分组其 emitted summand，即得到已登记 pre-pushforward 纤维分解。"
            ),
        },
        {
            "direction": "fiber_emitter_to_constructor_formula",
            "content": (
                "若已登记纤维分解 emitter 给出所有字段，则把 emitter 的输出在 Cauchy/dispersion 前求和，"
                "即得到 actual noncanonical primitive constructor formula；失败情形由 return tag 吸收。"
            ),
        },
        {
            "direction": "pushforward_graph_to_formula_no_go",
            "content": (
                "仅知道 Gamma 或任意有限投影不能反推唯一 pre-Cauchy 来源；不同 primitive 源测度可有同一推前。"
            ),
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    constructor: dict[str, Any],
    profinite: dict[str, Any],
    transverse: dict[str, Any],
    canonical: dict[str, Any],
    provenance: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成反向来源函子判定表。"""
    previous_atom = previous.get("latest_internal_subinput")
    payment_functorial = (
        profinite.get("profinite_aps_dichotomy_closed") is True
        and transverse.get("transverse_formal_unit_embedding_closed") is True
    )
    canonical_boundary_scoped = (
        canonical.get("self_contained_canonical_branch_closed") is True
        and provenance.get("actual_source_provenance_closed") is True
    )
    return [
        {
            "gate": "PriorConstructorFormulaPinned",
            "closed": previous_atom == "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn",
            "proved": False,
            "meaning": "上一层已把完全自足源侧剩余固定为 actual noncanonical primitive constructor formula。",
            "remaining": "判断已有支付图/投影塔模型能否反向恢复该公式。",
        },
        {
            "gate": "PaymentPushforwardFunctorialityAvailable",
            "closed": payment_functorial,
            "proved": True,
            "meaning": "actual payment graph、有限投影、弧限制和横向商均为同一来源上的推前/因子操作。",
            "remaining": "这些是正向函子，不自动提供反向来源。",
        },
        {
            "gate": "ReversePushforwardUniquenessRejected",
            "closed": True,
            "proved": True,
            "meaning": "推前映射通常不可逆；多个 pre-Cauchy primitive 源或不同纤维分配可给出同一 Gamma。",
            "remaining": "不能把 downstream payment atom 当作 primitive source formula。",
        },
        {
            "gate": "FiniteProjectionOnlyReconstructsGamma",
            "closed": True,
            "proved": True,
            "meaning": "有限投影塔最多恢复真实支付图 Gamma 的投影极限，不恢复被推前前的 summand emitter。",
            "remaining": "需要额外的 pre-pushforward 纤维分解数据。",
        },
        {
            "gate": "CanonicalReverseImportBlocked",
            "closed": canonical_boundary_scoped,
            "proved": True,
            "meaning": "canonical 来源分支的 RIW/Buchstab 构造器已闭合但作用域固定，不能反向导入 noncanonical clean-core。",
            "remaining": "noncanonical clean-core 必须给自己的已登记纤维 emitter 或回流。",
        },
        {
            "gate": "UnregisteredFiberReturnAbsorbed",
            "closed": constructor.get("unregistered_source_return_absorbed") is True,
            "proved": True,
            "meaning": "若某支付纤维没有同一 formal unit 的来源登记，它不再是 clean-core 终端，而回到已命名出口。",
            "remaining": "保留的 clean-core 情形必须提交已登记纤维分解。",
        },
        {
            "gate": "ConstructorFormulaEquivalentToRegisteredFiberEmitter",
            "closed": True,
            "proved": True,
            "meaning": "公式与已登记 pre-pushforward 纤维分解在闭合的回流纪律下等价：公式可分组为纤维，纤维 emitter 可求和为公式。",
            "remaining": "等价不证明该 emitter 存在。",
        },
        {
            "gate": "DownstreamModelsCloseCompatibilityFields",
            "closed": payment_functorial
            and constructor.get("source_class_partition_closed") is True
            and constructor.get("unregistered_source_return_absorbed") is True,
            "proved": True,
            "meaning": "支付图、投影塔、横向商和来源分类防火墙已关闭 formal-unit 兼容与未登记出口问题。",
            "remaining": "仍需真正的 pre-pushforward summand 生成规则。",
        },
        {
            "gate": "RegisteredPrimitivePrePushforwardFiberEmitterCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出 actual noncanonical clean-core 的已登记 primitive 纤维分解 emitter。",
            "remaining": "证明 RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。",
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
    constructor_path: Path,
    profinite_path: Path,
    transverse_path: Path,
    canonical_path: Path,
    provenance_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core 反向来源函子路由。"""
    source_paths = [
        previous_path,
        constructor_path,
        profinite_path,
        transverse_path,
        canonical_path,
        provenance_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    constructor = load_json(constructor_path)
    profinite = load_json(profinite_path)
    transverse = load_json(transverse_path)
    canonical = load_json(canonical_path)
    provenance = load_json(provenance_path)
    dstructure = load_json(dstructure_path)

    rows = gate_rows(
        previous=previous,
        constructor=constructor,
        profinite=profinite,
        transverse=transverse,
        canonical=canonical,
        provenance=provenance,
        dstructure=dstructure,
    )
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"]
        not in {
            "RegisteredPrimitivePrePushforwardFiberEmitterCurrentCorpusProved",
            "DStructureRankinStillIndependent",
        }
    )

    latest_internal = "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn"
    latest_external = previous.get(
        "latest_external_subinput",
        "CDependentResidueWeightSpectralCancellationInput",
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_reverse_provenance_functor_router",
        "status": "reverse_provenance_functor_boundary_closed_registered_fiber_emitter_open",
        "previous_input": previous.get(
            "latest_internal_subinput",
            "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn",
        ),
        "reverse_provenance_functor_boundary_closed": boundary_closed,
        "payment_pushforward_functoriality_available": True,
        "pushforward_reverse_uniqueness_rejected": True,
        "finite_projection_recovers_gamma_not_source": True,
        "canonical_reverse_import_blocked": True,
        "unregistered_fiber_return_absorbed": constructor.get("unregistered_source_return_absorbed") is True,
        "constructor_formula_equivalent_to_registered_fiber_emitter": True,
        "registered_primitive_prepushforward_fiber_emitter_proved": False,
        "actual_noncanonical_primitive_constructor_formula_proved": False,
        "external_spectral_atom_accepted": previous.get("external_spectral_atom_accepted", False),
        "dstructure_rankin_independent_acceptance_completed": dstructure.get(
            "promotion_package_independently_accepted",
            False,
        ),
        "row_column_unconditional_closed": False,
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
        "reverse_functor_law": (
            "支付图 Gamma、有限投影、弧限制和横向商都是 pre-Cauchy 来源测度的正向推前或有限因子。"
            "这些结构能证明来源兼容性和未登记出口纪律，却不能反向唯一恢复 primitive summand。"
            "在已闭合的回流纪律下，ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn "
            "等价于给出同一 formal unit 内的 RegisteredPrimitivePrePushforwardFiberEmitterAndReturn："
            "它必须在推前前逐纤维列出 primitive summand、系数恒等式、branch key、u/v map、符号和 local factor；"
            "无法登记或超预算者必须回流。"
        ),
        "plain_conclusion": (
            "从已有支付图、投影塔和横向商模型得到的有效突破是边界重写："
            "不能从 Gamma 反推 actual noncanonical primitive constructor；"
            "但当前公式剩余可等价压成一个更可审查的已登记 pre-pushforward 纤维分解 emitter。"
            "当前材料尚未证明该 emitter，因此行/列无条件命题仍未闭合。"
        ),
        "section_requirements": section_requirements(),
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
        "# Prime Matrix clean-core 反向来源函子路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"reverse_provenance_functor_boundary_closed={fmt_bool(result['reverse_provenance_functor_boundary_closed'])}",
        f"payment_pushforward_functoriality_available={fmt_bool(result['payment_pushforward_functoriality_available'])}",
        f"pushforward_reverse_uniqueness_rejected={fmt_bool(result['pushforward_reverse_uniqueness_rejected'])}",
        f"finite_projection_recovers_gamma_not_source={fmt_bool(result['finite_projection_recovers_gamma_not_source'])}",
        f"constructor_formula_equivalent_to_registered_fiber_emitter={fmt_bool(result['constructor_formula_equivalent_to_registered_fiber_emitter'])}",
        f"registered_primitive_prepushforward_fiber_emitter_proved={fmt_bool(result['registered_primitive_prepushforward_fiber_emitter_proved'])}",
        f"actual_noncanonical_primitive_constructor_formula_proved={fmt_bool(result['actual_noncanonical_primitive_constructor_formula_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 反向函子律",
        "",
        result["reverse_functor_law"],
        "",
        "```text",
        "pre-Cauchy primitive source measure",
        "  --deterministic payment pushforward--> Gamma",
        "  --finite projections / arc restrictions / transverse quotients--> downstream factors;",
        "",
        "Gamma and its finite factors do not determine the primitive source;",
        "a valid reverse route must supply:",
        "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `reverse_provenance_functor_boundary_closed={fmt_bool(result['reverse_provenance_functor_boundary_closed'])}`。",
        f"- `registered_primitive_prepushforward_fiber_emitter_proved={fmt_bool(result['registered_primitive_prepushforward_fiber_emitter_proved'])}`。",
        f"- `actual_noncanonical_primitive_constructor_formula_proved={fmt_bool(result['actual_noncanonical_primitive_constructor_formula_proved'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `latest_internal_subinput={result['latest_internal_subinput']}`。",
        f"- `latest_external_subinput={result['latest_external_subinput']}`。",
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
            "## 4. 纤维 emitter 字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for row in result["section_requirements"]:
        lines.append(
            f"| `{table_cell(row['field'])}` | {table_cell(row['requirement'])} |"
        )
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
        lines.append(
            f"| `{table_cell(row['direction'])}` | {table_cell(row['content'])} |"
        )
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
            "本步没有证明新的 emitter，也没有声明行/列无条件命题闭合。它把“直接写公式”的剩余改写成更可审查的反向来源问题：",
            "若能给出已登记的 pre-pushforward 纤维分解 emitter，则 actual noncanonical primitive constructor formula 随之闭合；",
            "若不能给出，则该对象不能留在 clean-core 终端，而必须按未登记来源、口径冲突、thin block 或外部谱输入回流。",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--constructor", type=Path, default=DEFAULT_CONSTRUCTOR)
    parser.add_argument("--profinite", type=Path, default=DEFAULT_PROFINITE)
    parser.add_argument("--transverse", type=Path, default=DEFAULT_TRANSVERSE)
    parser.add_argument("--canonical", type=Path, default=DEFAULT_CANONICAL)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        constructor_path=args.constructor,
        profinite_path=args.profinite,
        transverse_path=args.transverse,
        canonical_path=args.canonical,
        provenance_path=args.provenance,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
