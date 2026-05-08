#!/usr/bin/env python3
"""Prime Matrix actual signed/Phi 兼容预算到 pre-pushforward emitter 的压缩路由器。

用法示例：
  python3 experiments/prime_matrix_actual_signed_phi_budget_emitter_reduction_router.py

输出：
  docs/monograph/prime-matrix-actual-signed-phi-budget-emitter-reduction-router.json
  docs/monograph/prime-matrix-actual-signed-phi-budget-emitter-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-signed-geometric-variation-compatibility-merger.json"
DEFAULT_DISINTEGRATION = DOCS / "prime-matrix-clean-core-disintegration-automaticity-router.md"
DEFAULT_ALPHA = DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.md"
DEFAULT_REVERSE = DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.md"
DEFAULT_FIBER = DOCS / "prime-matrix-clean-core-fiber-emitter-field-audit-router.md"
DEFAULT_PRECAUCHY = DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-actual-signed-phi-budget-emitter-reduction-router.json"
DEFAULT_MD = DOCS / "prime-matrix-actual-signed-phi-budget-emitter-reduction-router.md"

OLD_ATOM = "ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn"
NEW_ATOM = "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn"
MODEL_ATOM = "ExplicitModelGapAndFiniteDPRCLedger"


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


def replace_once(text: str, old: str, new: str) -> str:
    """只替换一次输入基原子。"""
    if old not in text:
        return text
    return text.replace(old, new, 1)


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
    disintegration_text: str,
    alpha_text: str,
    reverse_text: str,
    fiber_text: str,
    precauchy_text: str,
) -> list[dict[str, Any]]:
    """生成兼容预算压缩到 emitter 的判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    assumption_guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    disintegration_formal = (
        "disintegration_automaticity_boundary_closed=true" in disintegration_text
        and "SignedFiberDisintegrationFormal" in disintegration_text
        and "PushforwardIdentityIsTheRealCompatibilityGate" in disintegration_text
    )
    dictionary_fields = (
        "signed_source_measure" in alpha_text
        and "pushforward_identity" in alpha_text
        and "variation_and_support_budget" in alpha_text
        and "sign_refinement" in alpha_text
    )
    reverse_functor = (
        "reverse_provenance_functor_boundary_closed=true" in reverse_text
        and "pushforward_reverse_uniqueness_rejected=true" in reverse_text
        and NEW_ATOM in reverse_text
    )
    payment_skeleton = (
        "payment_fiber_skeleton_closed=true" in fiber_text
        and "first_cover_payment_map_closed=true" in fiber_text
        and "payment_count_identity_closed=true" in fiber_text
    )
    precauchy_fields = (
        "CleanCoreOriginalCoefficientGenerationLedgerAndReturn" in precauchy_text
        and "PrimitivePathKey" in precauchy_text
        and "NamedReturnDiscipline" in precauchy_text
    )
    reduction_closed = all(
        [
            active,
            assumption_guard,
            disintegration_formal,
            dictionary_fields,
            reverse_functor,
            payment_skeleton,
            precauchy_fields,
        ]
    )
    return [
        row(
            "ActualSignedPhiBudgetGateActive",
            active,
            True,
            "当前输入基仍含 ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn。",
            "本步判断它的真正原子字段。",
        ),
        row(
            "HypotheticalCounterexampleChainGuard",
            assumption_guard,
            True,
            "本路由只在假设早期零行反例所需的证书链中工作，不用真实样本缺席。",
            "保持假设链条与真实链条分离。",
        ),
        row(
            "DisintegrationFormalPartClosed",
            disintegration_formal,
            True,
            "给定 signed source 与 Phi 后，逐纤维解积分形式闭合；真实门是 pushforward identity 与预算。",
            "需要 pre-pushforward signed source。",
        ),
        row(
            "AlphaDeltaDictionaryFieldsPinned",
            dictionary_fields,
            True,
            "字典字段已经固定为 signed source、pushforward、variation/support 和 sign refinement。",
            "字段尚未填。",
        ),
        row(
            "PaymentSkeletonAlreadyClosed",
            payment_skeleton,
            True,
            "completion-hole 域、first-cover map 和 payment count identity 已闭合。",
            "剩余不是 payment 图，而是 signed primitive lift。",
        ),
        row(
            "ReversePushforwardNoGoImported",
            reverse_functor,
            True,
            "不能从 Gamma 反推唯一 primitive source；必须额外提交 pre-pushforward fiber emitter。",
            NEW_ATOM,
        ),
        row(
            "PreCauchyLedgerFieldsImported",
            precauchy_fields,
            True,
            "pre-Cauchy 来源律要求 primitive path key、同 formal unit、非零/符号细分和命名回流。",
            "这些正是 emitter 字段。",
        ),
        row(
            "CompatibilityBudgetReducedToFiberEmitter",
            reduction_closed,
            True,
            "兼容预算包的未闭合内容等价压成同 formal unit 的 pre-pushforward fiber emitter。",
            NEW_ATOM,
        ),
        row(
            OLD_ATOM,
            reduction_closed,
            True,
            "该硬点作为复合黑箱已压缩到 RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。",
            "压缩不证明 emitter 存在。",
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "当前材料尚未给出 actual noncanonical primitive pre-pushforward fiber emitter。",
            NEW_ATOM,
        ),
        row(
            "ExplicitModelGapAndFiniteDPRCLedger",
            MODEL_ATOM in previous.get("latest_self_contained_basis", ""),
            False,
            "模型余量/有限 DPRC 账本仍在输入基中，未由本步处理。",
            MODEL_ATOM,
        ),
        row(
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            False,
            False,
            "源侧 emitter 与模型余量完成后仍需 DStructure/Tail-log4/finite Rankin 独立验收。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(
    previous_path: Path,
    disintegration_path: Path,
    alpha_path: Path,
    reverse_path: Path,
    fiber_path: Path,
    precauchy_path: Path,
) -> dict[str, Any]:
    """执行兼容预算压缩路由。"""
    source_paths = [
        previous_path,
        disintegration_path,
        alpha_path,
        reverse_path,
        fiber_path,
        precauchy_path,
    ]
    previous = load_json(previous_path)
    disintegration_text = disintegration_path.read_text(encoding="utf-8")
    alpha_text = alpha_path.read_text(encoding="utf-8")
    reverse_text = reverse_path.read_text(encoding="utf-8")
    fiber_text = fiber_path.read_text(encoding="utf-8")
    precauchy_text = precauchy_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        disintegration_text=disintegration_text,
        alpha_text=alpha_text,
        reverse_text=reverse_text,
        fiber_text=fiber_text,
        precauchy_text=precauchy_text,
    )
    reduction_closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    latest_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "actual_signed_phi_budget_emitter_reduction_router",
        "status": "actual_signed_phi_budget_reduced_to_prepushforward_emitter_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "actual_signed_phi_budget_reduction_closed": reduction_closed,
        "actual_signed_source_phi_compatibility_budget_proved": False,
        "registered_primitive_prepushforward_fiber_emitter_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": NEW_ATOM,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步不证明 actual signed/Phi 兼容预算；它把该复合黑箱压成更原子的 "
            "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。假设早期零行反例若要保留 clean-core "
            "支付链，就必须在 Cauchy/dispersion 前给出同 formal unit 的 primitive signed preimage summand、"
            "branch key、u/v、sign/local factor 与推前系数恒等式；否则该对象不能留在假设链条中，"
            "必须按未登记来源、口径冲突、thin block、PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入回流。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix actual signed/Phi 兼容预算到 pre-pushforward emitter 压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "actual_signed_phi_budget_reduction_closed="
            f"{fmt_bool(result['actual_signed_phi_budget_reduction_closed'])}"
        ),
        (
            "actual_signed_source_phi_compatibility_budget_proved="
            f"{fmt_bool(result['actual_signed_source_phi_compatibility_budget_proved'])}"
        ),
        (
            "registered_primitive_prepushforward_fiber_emitter_proved="
            f"{fmt_bool(result['registered_primitive_prepushforward_fiber_emitter_proved'])}"
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
        "这里分清两条链：假设链条强制反例必须提供该 emitter；真实链条不能从 payment 图或样本缺席反推出 emitter。",
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
            f"下一步最窄目标为 `{result['next_priority']}`：在推前前逐纤维列出 primitive summand、"
            "系数恒等式、branch key、u/v map、符号和 local factor；无法登记或超预算者必须命名回流。",
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
    parser.add_argument("--disintegration", type=Path, default=DEFAULT_DISINTEGRATION)
    parser.add_argument("--alpha", type=Path, default=DEFAULT_ALPHA)
    parser.add_argument("--reverse", type=Path, default=DEFAULT_REVERSE)
    parser.add_argument("--fiber", type=Path, default=DEFAULT_FIBER)
    parser.add_argument("--precauchy", type=Path, default=DEFAULT_PRECAUCHY)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        disintegration_path=args.disintegration,
        alpha_path=args.alpha,
        reverse_path=args.reverse,
        fiber_path=args.fiber,
        precauchy_path=args.precauchy,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
