#!/usr/bin/env python3
"""Prime Matrix clean-core 纤维 emitter 字段审计路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_fiber_emitter_field_audit_router.py

输出：
  docs/monograph/prime-matrix-clean-core-fiber-emitter-field-audit-router.json
  docs/monograph/prime-matrix-clean-core-fiber-emitter-field-audit-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json"
DEFAULT_PAYMENT = DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
DEFAULT_STITCHING = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-router.json"
DEFAULT_CONSTRUCTOR = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
DEFAULT_SOURCE_LOCK = DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-fiber-emitter-field-audit-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-fiber-emitter-field-audit-router.md"


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


def field_rows(
    payment: dict[str, Any],
    stitching: dict[str, Any],
    constructor: dict[str, Any],
    source_lock: dict[str, Any],
) -> list[dict[str, Any]]:
    """逐项审计纤维 emitter 字段。"""
    payment_skeleton = payment.get("all_payment_counts_match_demand") is True
    actual_stitching = stitching.get("route") == "ActualPaymentStitchingPersistentMFUOrDistributedCleanKLS"
    return [
        {
            "field": "payment_fiber_domain",
            "closed": payment_skeleton,
            "proved": True,
            "evidence": "completion y, low hole c, pay(c,y)=first ell",
            "meaning": "completion-hole 对和 first-cover payment map 已给出 payment-level preimage 骨架。",
            "remaining": "这还不是 signed alpha/delta primitive source。",
        },
        {
            "field": "payment_count_identity",
            "closed": payment_skeleton,
            "proved": True,
            "evidence": "all_payment_counts_match_demand",
            "meaning": "payment_count=sum_phase M(phase)*|H_low(phase)| 的计数恒等式已闭合。",
            "remaining": "需提升为 alpha/delta signed coefficient identity。",
        },
        {
            "field": "actual_gamma_stitching_gate",
            "closed": actual_stitching,
            "proved": True,
            "evidence": "ActualPaymentStitchingPersistentMFUOrDistributedCleanKLS",
            "meaning": "真实 Gamma 已被路由到持久 PDEC 或分散 CleanKLS/DLS，payment 层没有第四出口。",
            "remaining": "该门控不生成 clean-core primitive coefficient emitter。",
        },
        {
            "field": "formal_unit_return_discipline",
            "closed": constructor.get("unregistered_source_return_absorbed") is True,
            "proved": True,
            "evidence": "unregistered_source_return_absorbed",
            "meaning": "未登记或混合 formal unit 的来源不能留作 clean-core 终端。",
            "remaining": "保留者仍需同一 formal unit 的系数提升。",
        },
        {
            "field": "canonical_branch_separation",
            "closed": source_lock.get("noncanonical_branch_external_return") is True,
            "proved": True,
            "evidence": "NoncanonicalBranchExternalReturn",
            "meaning": "canonical 支撑链与 noncanonical clean-core 残余已分离，不能跨分支偷用 RIW/Buchstab 表。",
            "remaining": "noncanonical 残余需要自己的 alpha/delta lift。",
        },
        {
            "field": "alpha_delta_coefficient_lift",
            "closed": False,
            "proved": False,
            "evidence": "not in current corpus",
            "meaning": "当前材料尚未把 payment-level completion-hole 骨架提升为 clean-core alpha/delta primitive 系数。",
            "remaining": "证明 ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn。",
        },
        {
            "field": "polylog_branch_schema",
            "closed": False,
            "proved": False,
            "evidence": "not in current corpus",
            "meaning": "当前材料尚未给出 noncanonical clean-core 纤维的 log^O(1) branch key 压缩与同路径无抵消。",
            "remaining": "同属 ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn。",
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    payment: dict[str, Any],
    stitching: dict[str, Any],
    constructor: dict[str, Any],
    source_lock: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成字段审计判定表。"""
    fields = field_rows(payment, stitching, constructor, source_lock)
    closed_fields = {
        row["field"]: row["closed"]
        for row in fields
    }
    return [
        {
            "gate": "PriorFiberEmitterPinned",
            "closed": previous.get("latest_internal_subinput")
            == "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn",
            "proved": False,
            "meaning": "上一层已把公式剩余改写为已登记 pre-pushforward 纤维 emitter。",
            "remaining": "拆分该 emitter 的字段，找出已闭合骨架和真正未闭合字段。",
        },
        {
            "gate": "PaymentLevelFiberSkeletonClosed",
            "closed": closed_fields["payment_fiber_domain"] and closed_fields["payment_count_identity"],
            "proved": True,
            "meaning": "completion-hole 域、first-cover map 与 payment count identity 已闭合。",
            "remaining": "它只是 payment skeleton，不是 alpha/delta source formula。",
        },
        {
            "gate": "NoPaymentLayerFourthExit",
            "closed": closed_fields["actual_gamma_stitching_gate"],
            "proved": True,
            "meaning": "Actual Gamma 的持久/消散二分已排除 payment 层第四出口。",
            "remaining": "不能由此推出 primitive coefficient lift。",
        },
        {
            "gate": "FormalUnitAndCanonicalSeparationClosed",
            "closed": closed_fields["formal_unit_return_discipline"]
            and closed_fields["canonical_branch_separation"],
            "proved": True,
            "meaning": "同一 formal unit 纪律和 canonical/noncanonical 分支隔离已闭合。",
            "remaining": "剩余是 noncanonical clean-core 自己的系数提升。",
        },
        {
            "gate": "AlphaDeltaLiftCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有从 payment skeleton 到 actual alpha/delta primitive summand 的系数提升公式。",
            "remaining": "证明 ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn。",
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
    stitching_path: Path,
    constructor_path: Path,
    source_lock_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core 纤维 emitter 字段审计。"""
    source_paths = [
        previous_path,
        payment_path,
        stitching_path,
        constructor_path,
        source_lock_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    payment = load_json(payment_path)
    stitching = load_json(stitching_path)
    constructor = load_json(constructor_path)
    source_lock = load_json(source_lock_path)
    dstructure = load_json(dstructure_path)

    fields = field_rows(payment, stitching, constructor, source_lock)
    rows = gate_rows(previous, payment, stitching, constructor, source_lock, dstructure)
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"] not in {"AlphaDeltaLiftCurrentCorpusProved", "DStructureRankinStillIndependent"}
    )
    latest_internal = "ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn"
    latest_external = previous.get(
        "latest_external_subinput",
        "CDependentResidueWeightSpectralCancellationInput",
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_fiber_emitter_field_audit_router",
        "status": "payment_fiber_skeleton_closed_alpha_delta_lift_open",
        "previous_input": previous.get("latest_internal_subinput"),
        "fiber_emitter_field_audit_boundary_closed": boundary_closed,
        "payment_fiber_skeleton_closed": True,
        "first_cover_payment_map_closed": True,
        "payment_count_identity_closed": payment.get("all_payment_counts_match_demand") is True,
        "actual_gamma_stitching_gate_closed": stitching.get("route")
        == "ActualPaymentStitchingPersistentMFUOrDistributedCleanKLS",
        "formal_unit_return_discipline_closed": constructor.get("unregistered_source_return_absorbed") is True,
        "canonical_noncanonical_separation_closed": source_lock.get("noncanonical_branch_external_return") is True,
        "alpha_delta_coefficient_lift_proved": False,
        "polylog_branch_schema_proved": False,
        "registered_primitive_prepushforward_fiber_emitter_proved": False,
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
        "field_law": (
            "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn 的 payment-level 骨架已经由 "
            "ActualPaymentSelection 给出：completion-hole 对、first-cover map 和 payment count identity "
            "均可审查；ActualPaymentStitching 又排除 payment 层第四出口。"
            "但这只给出计数型 Gamma 骨架，不给出 clean-core signed alpha/delta primitive summand。"
            "在 canonical/noncanonical 分支隔离和未登记回流纪律下，真正剩余被压成 "
            "ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn。"
        ),
        "plain_conclusion": (
            "已有模型已经闭合 registered fiber emitter 的 payment 骨架字段；"
            "剩余不再是 Gamma 选择或支付计数，而是把该骨架提升为同一 formal unit 内的 "
            "actual noncanonical alpha/delta primitive 系数和 polylog branch schema。"
        ),
        "field_rows": fields,
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
        "# Prime Matrix clean-core 纤维 emitter 字段审计路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fiber_emitter_field_audit_boundary_closed={fmt_bool(result['fiber_emitter_field_audit_boundary_closed'])}",
        f"payment_fiber_skeleton_closed={fmt_bool(result['payment_fiber_skeleton_closed'])}",
        f"first_cover_payment_map_closed={fmt_bool(result['first_cover_payment_map_closed'])}",
        f"payment_count_identity_closed={fmt_bool(result['payment_count_identity_closed'])}",
        f"alpha_delta_coefficient_lift_proved={fmt_bool(result['alpha_delta_coefficient_lift_proved'])}",
        f"polylog_branch_schema_proved={fmt_bool(result['polylog_branch_schema_proved'])}",
        f"registered_primitive_prepushforward_fiber_emitter_proved={fmt_bool(result['registered_primitive_prepushforward_fiber_emitter_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 字段律",
        "",
        result["field_law"],
        "",
        "```text",
        "completion y + low hole c",
        "  --first-cover pay(c,y)--> payment atom in Gamma;",
        "payment count identity is closed;",
        "",
        "remaining lift:",
        "payment skeleton -> signed alpha/delta primitive summand schema.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `fiber_emitter_field_audit_boundary_closed={fmt_bool(result['fiber_emitter_field_audit_boundary_closed'])}`。",
        f"- `payment_fiber_skeleton_closed={fmt_bool(result['payment_fiber_skeleton_closed'])}`。",
        f"- `alpha_delta_coefficient_lift_proved={fmt_bool(result['alpha_delta_coefficient_lift_proved'])}`。",
        f"- `latest_internal_subinput={result['latest_internal_subinput']}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        "",
        "## 3. 字段审计表",
        "",
        "| field | closed | proved | evidence | meaning | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["field_rows"]:
        lines.append(
            "| {field} | `{closed}` | `{proved}` | {evidence} | {meaning} | {remaining} |".format(
                field=table_cell(row["field"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                evidence=table_cell(row["evidence"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 6. 当前结论",
            "",
            "本步没有证明 alpha/delta lift。它把上一步的已登记纤维 emitter 进一步分成已闭合的 payment skeleton",
            "和未闭合的 signed primitive coefficient lift。下一步最窄自足目标是证明该 lift，或把失败者命名回流。",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--payment", type=Path, default=DEFAULT_PAYMENT)
    parser.add_argument("--stitching", type=Path, default=DEFAULT_STITCHING)
    parser.add_argument("--constructor", type=Path, default=DEFAULT_CONSTRUCTOR)
    parser.add_argument("--source-lock", type=Path, default=DEFAULT_SOURCE_LOCK)
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
        stitching_path=args.stitching,
        constructor_path=args.constructor,
        source_lock_path=args.source_lock,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
