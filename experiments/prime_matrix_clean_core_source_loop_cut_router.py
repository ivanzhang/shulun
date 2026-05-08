#!/usr/bin/env python3
"""Prime Matrix clean-core 来源环切断路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_source_loop_cut_router.py

输出：
  docs/monograph/prime-matrix-clean-core-source-loop-cut-router.json
  docs/monograph/prime-matrix-clean-core-source-loop-cut-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-prepushforward-emitter-origin-ledger-router.json"
DEFAULT_ORIGIN = DOCS / "prime-matrix-clean-core-origin-source-admission-router.md"
DEFAULT_FIREWALL = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.md"
DEFAULT_REVERSE = DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.md"
DEFAULT_PREPUSH = DOCS / "prime-matrix-prepushforward-emitter-origin-ledger-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-source-loop-cut-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-source-loop-cut-router.md"

OLD_ATOM = "CleanCoreOriginalCoefficientGenerationLedgerAndReturn"
NEW_ATOM = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的来源账本原子。"""
    return text.replace(old, new)


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
    origin_text: str,
    firewall_text: str,
    reverse_text: str,
    prepush_text: str,
) -> list[dict[str, Any]]:
    """检测来源环，并把循环证明路径压成无环源种子输入。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    origin_to_constructor = (
        "OriginLedgerNeedsSourceConstructorAdmission" in origin_text
        and "ConstructorAdmissionImpliesOriginLedger" in origin_text
        and "CleanCorePrimitiveSourceConstructorAdmissionAndReturn" in origin_text
    )
    constructor_to_actual = (
        "ConstructorAdmissionSplitsBySourceClass" in firewall_text
        and "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn" in firewall_text
        and "UnregisteredOrMixedFormalUnitReturnAbsorbed" in firewall_text
    )
    actual_to_emitter = (
        "ConstructorFormulaEquivalentToRegisteredFiberEmitter" in reverse_text
        and "ReversePushforwardUniquenessRejected" in reverse_text
        and "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn" in reverse_text
    )
    emitter_to_origin = (
        "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn" in prepush_text
        and "CleanCoreOriginalCoefficientGenerationLedgerAndReturn" in prepush_text
        and "prepushforward_emitter_reduction_closed=true" in prepush_text
    )
    cycle_detected = all(
        [
            active,
            origin_to_constructor,
            constructor_to_actual,
            actual_to_emitter,
            emitter_to_origin,
        ]
    )
    return [
        row(
            "OriginLedgerGateActive",
            active,
            False,
            "最新假设链最窄点已回到 CleanCoreOriginalCoefficientGenerationLedgerAndReturn。",
            "检查它是否能靠既有路由自我闭合。",
        ),
        row(
            "OriginLedgerToConstructorAdmission",
            origin_to_constructor,
            True,
            "原始账本必须先给 pre-Cauchy primitive source constructor 准入。",
            "该方向不生成构造器，只说明账本入口。",
        ),
        row(
            "ConstructorAdmissionToActualNoncanonicalFormula",
            constructor_to_actual,
            True,
            "来源分类防火墙把 canonical/generic/unregistered/external 分流后，只剩 actual noncanonical 公式。",
            "仍需 actual noncanonical primitive formula。",
        ),
        row(
            "ActualFormulaToRegisteredEmitter",
            actual_to_emitter,
            True,
            "反向来源函子只给等价改写：actual formula 等价为 registered pre-pushforward emitter。",
            "不能从 payment 图反推来源。",
        ),
        row(
            "RegisteredEmitterBackToOriginLedger",
            emitter_to_origin,
            True,
            "pre-pushforward emitter 已压回 actual alpha/delta 原始生成账本。",
            "闭合成来源环，但没有生成源种子。",
        ),
        row(
            "CleanCoreSourceLoopDetected",
            cycle_detected,
            True,
            "现有源侧路由形成 origin ledger -> constructor -> formula -> emitter -> origin ledger 的循环。",
            "循环本身不是证明，必须切断。",
        ),
        row(
            "CircularReverseDerivationRejected",
            cycle_detected,
            True,
            "假设反例链不能把自身 payment skeleton 或有限投影当作 primitive source 的来源证明。",
            "需要无环 pre-Cauchy 源种子或命名回流。",
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "当前材料尚未提交不依赖 downstream payment 图的 actual noncanonical primitive source seed。",
            NEW_ATOM,
        ),
        row(
            "ExplicitModelGapAndFiniteDPRCLedger",
            "ExplicitModelGapAndFiniteDPRCLedger" in basis,
            False,
            "模型余量/有限 DPRC 账本仍在输入基中，未由来源环切断处理。",
            "ExplicitModelGapAndFiniteDPRCLedger。",
        ),
        row(
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(
    previous_path: Path,
    origin_path: Path,
    firewall_path: Path,
    reverse_path: Path,
    prepush_path: Path,
) -> dict[str, Any]:
    """执行来源环切断路由。"""
    source_paths = [previous_path, origin_path, firewall_path, reverse_path, prepush_path]
    previous = load_json(previous_path)
    origin_text = origin_path.read_text(encoding="utf-8")
    firewall_text = firewall_path.read_text(encoding="utf-8")
    reverse_text = reverse_path.read_text(encoding="utf-8")
    prepush_text = prepush_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        origin_text=origin_text,
        firewall_text=firewall_text,
        reverse_text=reverse_text,
        prepush_text=prepush_text,
    )
    cycle_cut = next(bool(item["closed"]) for item in rows if item["gate"] == "CircularReverseDerivationRejected")
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "clean_core_source_loop_cut_router",
        "status": "clean_core_source_loop_cut_to_acyclic_seed_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "source_loop_detected": cycle_cut,
        "circular_reverse_derivation_rejected": cycle_cut,
        "source_loop_cut_closed": cycle_cut,
        "acyclic_pre_cauchy_source_seed_proved": False,
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
            "本步把 CleanCoreOriginalCoefficientGenerationLedgerAndReturn 的循环来源证明路径切断。"
            "现有路由只形成 origin ledger -> constructor admission -> actual noncanonical formula -> "
            "registered emitter -> origin ledger 的等价环；假设早期零行反例若要保留 clean-core 分支，"
            "必须提交不依赖 downstream payment skeleton 的无环 pre-Cauchy noncanonical primitive source seed。"
            "若提交不了，该分支不能作为 clean-core 终端，必须回流到 PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix clean-core 来源环切断路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"source_loop_detected={fmt_bool(result['source_loop_detected'])}",
        f"circular_reverse_derivation_rejected={fmt_bool(result['circular_reverse_derivation_rejected'])}",
        f"source_loop_cut_closed={fmt_bool(result['source_loop_cut_closed'])}",
        f"acyclic_pre_cauchy_source_seed_proved={fmt_bool(result['acyclic_pre_cauchy_source_seed_proved'])}",
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
        "## 1. 来源环",
        "",
        "```text",
        "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
        "  -> CleanCorePrimitiveSourceConstructorAdmissionAndReturn",
        "  -> ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn",
        "  -> RegisteredPrimitivePrePushforwardFiberEmitterAndReturn",
        "  -> CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
        "```",
        "",
        "这个环只说明若一个字段已经合法给出，其他字段可以互相展开或分组；它不能从 downstream payment "
        "skeleton 反向生成 primitive source。",
        "",
        "## 2. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "该替换把“循环来源证明”改写为无环源种子义务。",
        "",
        "## 3. 判定表",
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
            "## 5. 下一步",
            "",
            f"下一步最窄目标为 `{result['next_priority']}`：给出不依赖真实 payment 图、有限投影塔或样本缺席的"
            " pre-Cauchy actual noncanonical primitive source seed；否则必须输出命名回流标签。",
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
    parser.add_argument("--origin", type=Path, default=DEFAULT_ORIGIN)
    parser.add_argument("--firewall", type=Path, default=DEFAULT_FIREWALL)
    parser.add_argument("--reverse", type=Path, default=DEFAULT_REVERSE)
    parser.add_argument("--prepush", type=Path, default=DEFAULT_PREPUSH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        origin_path=args.origin,
        firewall_path=args.firewall,
        reverse_path=args.reverse,
        prepush_path=args.prepush,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
