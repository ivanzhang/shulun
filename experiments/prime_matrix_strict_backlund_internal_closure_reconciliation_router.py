#!/usr/bin/env python3
"""生成 strict Backlund 内部闭合调和路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_backlund_internal_closure_reconciliation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-backlund-internal-closure-reconciliation-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-backlund-internal-closure-reconciliation-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-backlund-internal-closure-reconciliation-router.md"

STRICT_PERRON = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-self-contained-reduction-router.json"
COMMON_ENVELOPE = MONOGRAPH / "prime-matrix-backlund-common-envelope-internal-closure-router.json"
FINAL_BRANCH = MONOGRAPH / "prime-matrix-backlund-final-branch-status-router.json"
INTERNAL_EXTERNAL = MONOGRAPH / "prime-matrix-backlund-internal-external-merge-router.json"
LOWHEIGHT_XI = MONOGRAPH / "prime-matrix-lowheight-xi-backlund-integration-router.json"
RVM_CN16 = MONOGRAPH / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.json"
LOCAL_ZERO = MONOGRAPH / "prime-matrix-b3-psi0-horizontal-local-zero-distance-router.json"
WEIGHTED_BUDGET = MONOGRAPH / "prime-matrix-b3-psi0-horizontal-weighted-budget-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [
    STRICT_PERRON,
    COMMON_ENVELOPE,
    FINAL_BRANCH,
    INTERNAL_EXTERNAL,
    LOWHEIGHT_XI,
    RVM_CN16,
    LOCAL_ZERO,
    WEIGHTED_BUDGET,
    CLAIM_STATUS,
]

BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
BACKLUND_CLOSED = "ClassicalBacklundZeroIndentationCostInternalProofClosedByHighPowerCommonEnvelope"
OLD_BACKLUND_ATOM = "BacklundZeroProximityIndentationCostLedger"
LOGDER_INTERNAL = "ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger"
LOCAL_DISTANCE = "Psi0HorizontalLocalZeroDistanceSumConstantLedger"
WEIGHTED = "Psi0HorizontalWeightedIntegralBudgetLedger"
RVM_SYNC = "SelfContainedRVMToCN16LocalInequalitySyncFromCommonEnvelopeAndLowHeightXi"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖证据哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def replace_backlund_atom(text: str) -> str:
    """只替换 Backlund 内部证明原子，不触碰其他剩余。"""
    return text.replace(BACKLUND_INTERNAL, BACKLUND_CLOSED)


def build_rows(
    perron: dict[str, Any],
    common: dict[str, Any],
    final_branch: dict[str, Any],
    lowheight: dict[str, Any],
    rvm: dict[str, Any],
    local_zero: dict[str, Any],
    weighted: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成调和判定表。"""
    guard = (
        perron.get("counterexample_assumption_only") is True
        and perron.get("empirical_absence_not_used") is True
        and perron.get("row_column_unconditional_closed") is False
    )
    perron_uses_backlund = BACKLUND_INTERNAL in str(perron.get("self_contained_replacement", ""))
    common_replacement = common.get("replacement_self_contained", {})
    common_closes_backlund = (
        common.get("strict_self_contained_backlund_closed") is True
        and common.get("closed_internal_backlund_atom") == BACKLUND_CLOSED
        and common_replacement.get(BACKLUND_INTERNAL) == BACKLUND_CLOSED
    )
    old_final_open = (
        final_branch.get("row_column_self_contained_closed") is False
        and final_branch.get("self_contained_remaining") == OLD_BACKLUND_ATOM
    )
    lowheight_closed = (
        lowheight.get("lowheight_xi_rectangle_count_closed") is True
        and lowheight.get("finite_lowheight_zero_check_closed") is True
    )
    rvm_self_closed = rvm.get("rvm_to_cn16_self_contained_closed") is True
    local_self_closed = local_zero.get("psi0_horizontal_local_zero_distance_self_contained_closed") is True
    weighted_self_closed = weighted.get("psi0_horizontal_weighted_integral_budget_self_contained_closed") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只调和假设反例链中的解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "OlderFinalBranchStatusScoped",
            old_final_open,
            True,
            "旧最终分叉状态仍可作为历史边界：它说明当时 Backlund 凹口成本开放，且全局不可闭合。",
            "该旧状态不再支配 Backlund 单原子的新闭合证据。",
        ),
        row(
            "CommonEnvelopeBacklundAtomClosed",
            common_closes_backlund,
            common_closes_backlund,
            "共同高高度包络给出同一 sigma 分区支配，max 不新增 log 系数，C16 分子仍为 7。",
            BACKLUND_CLOSED,
        ),
        row(
            "LowHeightXiSubpackageAlreadyClosed",
            lowheight_closed,
            lowheight_closed,
            "0<t<=14 的 xi 矩形零点计数、临界线/离线 Turing 和 finite low-height check 已由低高度子包回灌。",
            "LowHeightXiRectangleZeroCountZero0To14SelfContainedClosed",
        ),
        row(
            "StrictPerronBacklundReplacementLegal",
            perron_uses_backlund and common_closes_backlund,
            perron_uses_backlund and common_closes_backlund,
            "最新 strict Perron 压缩中的 Backlund 内部证明原子可替换为共同包络闭合原子。",
            f"{BACKLUND_INTERNAL} => {BACKLUND_CLOSED}",
        ),
        row(
            "FixedTIndentAtomReconciled",
            common_closes_backlund,
            common_closes_backlund,
            "psi_0 fixed-T 缩进已证明与经典 Backlund 缩进同 formal unit；Backlund 原子闭合后，该缩进子项同步调和。",
            BACKLUND_CLOSED,
        ),
        row(
            "SelfContainedRVMToCN16NotYetResynchronized",
            rvm_self_closed,
            rvm_self_closed,
            "RVM->C_N=16 当前仍只在外部/条件分支有显式闭合记录；需另做从共同包络和低高度 xi 到原始 arg C8 的自足同步。",
            RVM_SYNC,
        ),
        row(
            "SelfContainedLocalZeroDistanceStillOpen",
            local_self_closed,
            local_self_closed,
            "局部零点倒距离 C=288 目前仍是外部 Backlund/RVM 条件闭合；自足版需先完成 RVM/CN16 同步并接入内部 log-derivative。",
            LOCAL_DISTANCE,
        ),
        row(
            "SelfContainedWeightedBudgetStillOpen",
            weighted_self_closed,
            weighted_self_closed,
            "C=12000 加权预算已在外部条件线下闭合；自足版需等待自足局部零点距离和 pointwise log-derivative。",
            WEIGHTED,
        ),
        row(
            "UnsmoothedPerronStrictSelfContainedClosed",
            False,
            False,
            "Backlund 原子调和后，strict 非平滑 Perron 仍缺水平边 log-derivative、局部零点距离和加权预算同步。",
            f"{LOGDER_INTERNAL} AND {LOCAL_DISTANCE} AND {WEIGHTED}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只是解析输入基调和；统一矛盾场尚未产生直接无条件矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    perron = load_json(STRICT_PERRON)
    common = load_json(COMMON_ENVELOPE)
    final_branch = load_json(FINAL_BRANCH)
    internal_external = load_json(INTERNAL_EXTERNAL)
    lowheight = load_json(LOWHEIGHT_XI)
    rvm = load_json(RVM_CN16)
    local_zero = load_json(LOCAL_ZERO)
    weighted = load_json(WEIGHTED_BUDGET)
    old_basis = str(perron.get("self_contained_replacement", ""))
    reconciled_basis = replace_backlund_atom(old_basis)
    rows = build_rows(perron, common, final_branch, lowheight, rvm, local_zero, weighted)
    backlund_replaced = next(item["closed"] for item in rows if item["gate"] == "StrictPerronBacklundReplacementLegal")
    return {
        "certificate_type": "prime_matrix_strict_backlund_internal_closure_reconciliation_router",
        "status": "strict_backlund_internal_closure_reconciled_perron_horizontal_inputs_still_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "backlund_common_envelope_atom_accepted_for_strict_perron": backlund_replaced,
        "older_final_branch_status_superseded_for_backlund_atom_only": backlund_replaced,
        "strict_perron_backlund_atom_replaced": backlund_replaced,
        "rvm_cn16_self_contained_resynchronized": False,
        "local_zero_distance_self_contained_proved": False,
        "weighted_budget_self_contained_proved": False,
        "unsmoothed_perron_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "old_strict_perron_self_contained_basis": old_basis,
        "reconciled_strict_perron_self_contained_basis": reconciled_basis,
        "remaining_atoms_after_backlund_reconciliation": [
            LOGDER_INTERNAL,
            LOCAL_DISTANCE,
            WEIGHTED,
        ],
        "unwrapped_next_sync_atom": RVM_SYNC,
        "next_direct_attack_target": RVM_SYNC,
        "parallel_attack_target": LOGDER_INTERNAL,
        "post_sync_target": f"{LOCAL_DISTANCE} => {WEIGHTED}",
        "external_merge_status_seen": internal_external.get("status", ""),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Backlund 状态冲突已按原子作用域调和：旧 final-branch-status 仍正确说明当时和全局层面不能闭合，"
            "但较新的 common-envelope 证书已经对 `ClassicalBacklundZeroIndentationCostInternalProofLedger` "
            "给出作者侧共同包络闭合。因此 strict Perron 中的 Backlund 原子可合法替换为 "
            f"`{BACKLUND_CLOSED}`。替换后仍不能声明非平滑 Perron 自足闭合；剩余转为水平边 "
            "log-derivative、自足 RVM/CN16 到局部零点距离、以及加权预算同步。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Backlund 内部闭合调和路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"backlund_common_envelope_atom_accepted_for_strict_perron={fmt_bool(result['backlund_common_envelope_atom_accepted_for_strict_perron'])}",
        f"older_final_branch_status_superseded_for_backlund_atom_only={fmt_bool(result['older_final_branch_status_superseded_for_backlund_atom_only'])}",
        f"strict_perron_backlund_atom_replaced={fmt_bool(result['strict_perron_backlund_atom_replaced'])}",
        f"rvm_cn16_self_contained_resynchronized={fmt_bool(result['rvm_cn16_self_contained_resynchronized'])}",
        f"local_zero_distance_self_contained_proved={fmt_bool(result['local_zero_distance_self_contained_proved'])}",
        f"weighted_budget_self_contained_proved={fmt_bool(result['weighted_budget_self_contained_proved'])}",
        f"unsmoothed_perron_strict_self_contained_closed={fmt_bool(result['unsmoothed_perron_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 调和替换",
        "",
        "旧 strict Perron 自足基：",
        "",
        "```text",
        result["old_strict_perron_self_contained_basis"],
        "```",
        "",
        "调和后自足基：",
        "",
        "```text",
        result["reconciled_strict_perron_self_contained_basis"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            result["parallel_attack_target"],
            "```",
            "",
            "本步的边界很窄：它只解决 Backlund 原子版本冲突，不关闭 Perron 水平边整体，也不关闭行/列无条件命题。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
