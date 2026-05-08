#!/usr/bin/env python3
"""Prime Matrix pre-pushforward emitter 到原始生成账本的压缩路由器。

用法示例：
  python3 experiments/prime_matrix_prepushforward_emitter_origin_ledger_router.py

输出：
  docs/monograph/prime-matrix-prepushforward-emitter-origin-ledger-router.json
  docs/monograph/prime-matrix-prepushforward-emitter-origin-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-actual-signed-phi-budget-emitter-reduction-router.json"
DEFAULT_REVERSE = DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.md"
DEFAULT_FIBER = DOCS / "prime-matrix-clean-core-fiber-emitter-field-audit-router.md"
DEFAULT_PRECAUCHY = DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.md"
DEFAULT_ORIGIN = DOCS / "prime-matrix-clean-core-origin-source-admission-router.md"
DEFAULT_FIREWALL = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-prepushforward-emitter-origin-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-prepushforward-emitter-origin-ledger-router.md"

OLD_ATOM = "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn"
NEW_ATOM = "CleanCoreOriginalCoefficientGenerationLedgerAndReturn"


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
    reverse_text: str,
    fiber_text: str,
    precauchy_text: str,
    origin_text: str,
    firewall_text: str,
) -> list[dict[str, Any]]:
    """生成 emitter 到原始生成账本压缩判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    no_reverse = (
        "pushforward_reverse_uniqueness_rejected=true" in reverse_text
        and "不能反向唯一恢复 primitive summand" in reverse_text
    )
    payment_skeleton_closed = (
        "payment_fiber_skeleton_closed=true" in fiber_text
        and "payment_count_identity_closed=true" in fiber_text
        and "alpha_delta_coefficient_lift_proved=false" in fiber_text
    )
    origin_ledger_atom = (
        "CleanCoreOriginalCoefficientGenerationLedgerAndReturn" in precauchy_text
        and "PrimitivePathKey" in precauchy_text
        and "NamedReturnDiscipline" in precauchy_text
    )
    constructor_entry = (
        "OriginLedgerNeedsSourceConstructorAdmission" in origin_text
        and "ConstructorAdmissionImpliesOriginLedger" in origin_text
    )
    source_firewall = (
        "constructor_source_class_firewall_boundary_closed=true" in firewall_text
        and "actual_noncanonical_primitive_constructor_formula_proved=false" in firewall_text
    )
    reduction_closed = all(
        [
            active,
            no_reverse,
            payment_skeleton_closed,
            origin_ledger_atom,
            constructor_entry,
            source_firewall,
        ]
    )
    return [
        row(
            "PrePushforwardEmitterGateActive",
            active,
            True,
            "当前输入基仍含 RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。",
            "检查它的最小来源证据。",
        ),
        row(
            "ReversePhiRouteBlocked",
            no_reverse,
            True,
            "不能从 payment 图或有限投影反推 primitive summand；反推路径不是证明。",
            "必须给 pre-Cauchy 原始来源。",
        ),
        row(
            "PaymentSkeletonClosedButSignedLiftOpen",
            payment_skeleton_closed,
            True,
            "payment fiber skeleton 与计数恒等式已闭合；未闭合的是 alpha/delta primitive 系数提升。",
            "需要原始生成账本。",
        ),
        row(
            "PreCauchyOriginLedgerAtomPinned",
            origin_ledger_atom,
            True,
            "pre-Cauchy 来源律的最小证据是同 formal unit 的原始生成账本。",
            NEW_ATOM,
        ),
        row(
            "ConstructorAdmissionIsLedgerEntry",
            constructor_entry,
            True,
            "原始生成账本必须来自 Cauchy 前 primitive source constructor 准入。",
            "后续可继续压到 constructor admission。",
        ),
        row(
            "SourceClassFirewallPreventsCanonicalLeak",
            source_firewall,
            True,
            "canonical、generic、unregistered 和 external 来源已分流；noncanonical 不能偷用 canonical 表。",
            "仍需 actual noncanonical 账本。",
        ),
        row(
            "EmitterReducedToOriginGenerationLedger",
            reduction_closed,
            True,
            "已登记 pre-pushforward emitter 的实质就是相关纤维上的 clean-core 原始系数生成账本。",
            NEW_ATOM,
        ),
        row(
            OLD_ATOM,
            reduction_closed,
            True,
            "该硬点作为复合字段已压缩到 CleanCoreOriginalCoefficientGenerationLedgerAndReturn。",
            "压缩不证明账本存在。",
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "当前材料尚未列出 actual clean-core alpha/delta 的完整 pre-Cauchy 原始生成表。",
            NEW_ATOM,
        ),
        row(
            "ExplicitModelGapAndFiniteDPRCLedger",
            "ExplicitModelGapAndFiniteDPRCLedger" in basis,
            False,
            "模型余量/有限 DPRC 账本仍在输入基中，未由本步处理。",
            "ExplicitModelGapAndFiniteDPRCLedger。",
        ),
        row(
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            False,
            False,
            "来源账本与模型余量完成后仍需 DStructure/Tail-log4/finite Rankin 独立验收。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(
    previous_path: Path,
    reverse_path: Path,
    fiber_path: Path,
    precauchy_path: Path,
    origin_path: Path,
    firewall_path: Path,
) -> dict[str, Any]:
    """执行 emitter 到原始生成账本压缩路由。"""
    source_paths = [
        previous_path,
        reverse_path,
        fiber_path,
        precauchy_path,
        origin_path,
        firewall_path,
    ]
    previous = load_json(previous_path)
    reverse_text = reverse_path.read_text(encoding="utf-8")
    fiber_text = fiber_path.read_text(encoding="utf-8")
    precauchy_text = precauchy_path.read_text(encoding="utf-8")
    origin_text = origin_path.read_text(encoding="utf-8")
    firewall_text = firewall_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        reverse_text=reverse_text,
        fiber_text=fiber_text,
        precauchy_text=precauchy_text,
        origin_text=origin_text,
        firewall_text=firewall_text,
    )
    reduction_closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    latest_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "prepushforward_emitter_origin_ledger_router",
        "status": "prepushforward_emitter_reduced_to_origin_generation_ledger_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "prepushforward_emitter_reduction_closed": reduction_closed,
        "registered_primitive_prepushforward_fiber_emitter_proved": False,
        "clean_core_original_generation_ledger_proved": False,
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
            "本步把 RegisteredPrimitivePrePushforwardFiberEmitterAndReturn 压成 "
            "CleanCoreOriginalCoefficientGenerationLedgerAndReturn。核心矛盾搜索边界是：假设反例链条不能"
            "从真实 payment 图或样本缺席反向制造来源；它必须提交 Cauchy/dispersion 前的 actual clean-core "
            "alpha/delta 原始生成表。若没有这张表，clean-core 来源不合法，必须命名回流。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix pre-pushforward emitter 到原始生成账本压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"prepushforward_emitter_reduction_closed={fmt_bool(result['prepushforward_emitter_reduction_closed'])}",
        (
            "registered_primitive_prepushforward_fiber_emitter_proved="
            f"{fmt_bool(result['registered_primitive_prepushforward_fiber_emitter_proved'])}"
        ),
        (
            "clean_core_original_generation_ledger_proved="
            f"{fmt_bool(result['clean_core_original_generation_ledger_proved'])}"
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
        "该替换防止从真实 payment 图反向偷渡来源；保留的假设反例必须提交 pre-Cauchy 原始账本。",
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
            f"下一步最窄目标为 `{result['next_priority']}`：列出 actual clean-core alpha/delta 的"
            "完整 pre-Cauchy 原始生成表；缺失来源、路径超预算、thin block 或抵消必须命名回流。",
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
    parser.add_argument("--reverse", type=Path, default=DEFAULT_REVERSE)
    parser.add_argument("--fiber", type=Path, default=DEFAULT_FIBER)
    parser.add_argument("--precauchy", type=Path, default=DEFAULT_PRECAUCHY)
    parser.add_argument("--origin", type=Path, default=DEFAULT_ORIGIN)
    parser.add_argument("--firewall", type=Path, default=DEFAULT_FIREWALL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        reverse_path=args.reverse,
        fiber_path=args.fiber,
        precauchy_path=args.precauchy,
        origin_path=args.origin,
        firewall_path=args.firewall,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
