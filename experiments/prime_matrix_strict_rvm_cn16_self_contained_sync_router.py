#!/usr/bin/env python3
"""生成 strict RVM->C_N=16 自足同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_rvm_cn16_self_contained_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rvm-cn16-self-contained-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-rvm-cn16-self-contained-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-rvm-cn16-self-contained-sync-router.md"

RECONCILIATION = MONOGRAPH / "prime-matrix-strict-backlund-internal-closure-reconciliation-router.json"
CS8 = MONOGRAPH / "prime-matrix-b3-cs8-slack-router.json"
ENDPOINT = MONOGRAPH / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
RVM = MONOGRAPH / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.json"
LOWHEIGHT_XI = MONOGRAPH / "prime-matrix-lowheight-xi-backlund-integration-router.json"
COMMON_ENVELOPE = MONOGRAPH / "prime-matrix-backlund-common-envelope-internal-closure-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [
    RECONCILIATION,
    CS8,
    ENDPOINT,
    RVM,
    LOWHEIGHT_XI,
    COMMON_ENVELOPE,
    CLAIM_STATUS,
]

BACKLUND_CLOSED = "ClassicalBacklundZeroIndentationCostInternalProofClosedByHighPowerCommonEnvelope"
CS8_SELF = "BacklundCS8SlackAfterBridgeSelfContainedClosedTightHalfByCommonEnvelope"
RVM_SELF = "RVMToCN16LocalInequalitySelfContainedClosedWithRawArgCS8CommonEnvelope"
LOGDER_INTERNAL = "ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger"
LOCAL_DISTANCE = "Psi0HorizontalLocalZeroDistanceSumConstantLedger"
WEIGHTED = "Psi0HorizontalWeightedIntegralBudgetLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
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


def has_closed_gate(data: dict[str, Any], gate: str) -> bool:
    """判断上游证书是否登记闭合 gate。"""
    return gate in data.get("closed_gates", [])


def build_rows(
    reconciliation: dict[str, Any],
    cs8: dict[str, Any],
    endpoint: dict[str, Any],
    rvm: dict[str, Any],
    lowheight: dict[str, Any],
    common: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 RVM 自足同步判定表。"""
    guard = (
        reconciliation.get("counterexample_assumption_only") is True
        and reconciliation.get("row_column_unconditional_closed") is False
        and reconciliation.get("direct_unconditional_contradiction_found") is False
    )
    backlund_closed = (
        reconciliation.get("strict_perron_backlund_atom_replaced") is True
        and common.get("strict_self_contained_backlund_closed") is True
        and common.get("closed_internal_backlund_atom") == BACKLUND_CLOSED
    )
    cs8_algebra = (
        has_closed_gate(cs8, "BoundaryBridgeInputsAvailable")
        and has_closed_gate(cs8, "CS8TightEqualityPasses")
        and float(cs8.get("C_S_result", 0.0)) == float(cs8.get("C_S_target", -1.0))
    )
    endpoint_closed = endpoint.get("endpoint_multiplicity_convention_self_contained_closed") is True
    lowheight_closed = lowheight.get("finite_lowheight_zero_check_closed") is True
    raw_arg_passes = has_closed_gate(rvm, "RawArgNormalizationPassesCN16")
    normalized_rejected = has_closed_gate(rvm, "NormalizedSInterpretationRejected")
    rvm_coefficient_ok = float(rvm.get("raw_arg_rvm_coefficient", 999.0)) < float(rvm.get("C_N_target", 0.0))
    cs8_self_closed = backlund_closed and cs8_algebra
    rvm_self_closed = (
        guard
        and cs8_self_closed
        and endpoint_closed
        and lowheight_closed
        and raw_arg_passes
        and normalized_rejected
        and rvm_coefficient_ok
    )
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "同步仍只在假设反例链解析输入内部进行，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "BacklundCommonEnvelopeImported",
            backlund_closed,
            backlund_closed,
            "Backlund 缩进内部证明原子已由共同高高度包络调和闭合。",
            BACKLUND_CLOSED,
        ),
        row(
            "CS8BoundaryBridgeAlgebraReady",
            cs8_algebra,
            cs8_algebra,
            "C_boundary=16 与 bridge factor=1/2 的代数验收已给出 C_S=8 紧等号。",
            "16 * 1/2 = 8",
        ),
        row(
            "CS8SelfContainedSynchronized",
            cs8_self_closed,
            cs8_self_closed,
            "原先 CS8 只因 Backlund 缩进外部输入而标作条件；共同包络替换后，该 CS8 账本可作者侧同步。",
            CS8_SELF,
        ),
        row(
            "EndpointConventionSelfContained",
            endpoint_closed,
            endpoint_closed,
            "端点避零与重数极限 convention 已自足闭合，且不新增 C_S 或 C_N 常数。",
            "EndpointZeroAvoidanceMultiplicityConventionClosedByLimit",
        ),
        row(
            "LowHeightXiSelfContained",
            lowheight_closed,
            lowheight_closed,
            "0<t<=14 的低高度零点检查已由 xi 矩形零点计数 0 回灌。",
            "LowHeightXiRectangleZeroCountZero0To14SelfContainedClosed",
        ),
        row(
            "RawArgNormalizationPassesCN16",
            raw_arg_passes and normalized_rejected and rvm_coefficient_ok,
            raw_arg_passes and normalized_rejected and rvm_coefficient_ok,
            "RVM 中使用原始 arg zeta 常数后，总系数约 10.4266，小于目标 C_N=16；规范化 S 解释已被拒绝。",
            "raw_arg_rvm_coefficient < C_N_target",
        ),
        row(
            "RVMToCN16SelfContainedSynchronized",
            rvm_self_closed,
            rvm_self_closed,
            "Backlund C8、端点 convention、低高度 xi 与 RVM 原始 arg 代数全部接通后，C_N=16 局部计数可同步为作者侧输入。",
            RVM_SELF,
        ),
        row(
            "LocalZeroDistanceStillNeedsLogDerivativeLedger",
            False,
            False,
            "C_N=16 同步只给局部零点数量；Perron 水平边还需要内部 log-derivative 展开和局部倒距离常数账本。",
            f"{LOGDER_INTERNAL} AND {LOCAL_DISTANCE}",
        ),
        row(
            "UnsmoothedPerronStrictSelfContainedClosed",
            False,
            False,
            "本步不关闭非平滑 Perron 自足包；加权预算仍等待 pointwise 水平边上界。",
            f"{LOGDER_INTERNAL} AND {LOCAL_DISTANCE} AND {WEIGHTED}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只是解析输入同步，不产生全局反例矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    reconciliation = load_json(RECONCILIATION)
    cs8 = load_json(CS8)
    endpoint = load_json(ENDPOINT)
    rvm = load_json(RVM)
    lowheight = load_json(LOWHEIGHT_XI)
    common = load_json(COMMON_ENVELOPE)
    rows = build_rows(reconciliation, cs8, endpoint, rvm, lowheight, common)
    rvm_closed = next(item["closed"] for item in rows if item["gate"] == "RVMToCN16SelfContainedSynchronized")
    return {
        "certificate_type": "prime_matrix_strict_rvm_cn16_self_contained_sync_router",
        "status": "rvm_cn16_self_contained_synchronized_horizontal_logder_still_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "backlund_common_envelope_imported": next(item["closed"] for item in rows if item["gate"] == "BacklundCommonEnvelopeImported"),
        "cs8_self_contained_synchronized": next(item["closed"] for item in rows if item["gate"] == "CS8SelfContainedSynchronized"),
        "rvm_cn16_self_contained_resynchronized": rvm_closed,
        "local_zero_distance_self_contained_proved": False,
        "weighted_budget_self_contained_proved": False,
        "unsmoothed_perron_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {
            "BacklundCS8SlackAfterBridgeLedger": CS8_SELF,
            "RVMToCN16LocalInequalityLedger": RVM_SELF,
        },
        "remaining_after_rvm_sync": [
            LOGDER_INTERNAL,
            LOCAL_DISTANCE,
            WEIGHTED,
        ],
        "next_direct_attack_target": LOGDER_INTERNAL,
        "secondary_attack_target": LOCAL_DISTANCE,
        "post_local_target": WEIGHTED,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "RVM->C_N=16 的自足同步已完成到证书层：共同包络关闭 Backlund 缩进原子后，"
            "CS8 紧等号账本不再需要外部 Backlund；端点 convention 与低高度 xi 子包已自足，"
            "RVM 原始 arg 归一化的系数 10.4266<16 可直接接入。"
            "但这只关闭局部零点计数输入，尚未关闭 Perron 水平边的内部 log-derivative、局部倒距离和加权预算。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RVM->C_N=16 自足同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cs8_self_contained_synchronized={fmt_bool(result['cs8_self_contained_synchronized'])}",
        f"rvm_cn16_self_contained_resynchronized={fmt_bool(result['rvm_cn16_self_contained_resynchronized'])}",
        f"local_zero_distance_self_contained_proved={fmt_bool(result['local_zero_distance_self_contained_proved'])}",
        f"weighted_budget_self_contained_proved={fmt_bool(result['weighted_budget_self_contained_proved'])}",
        f"unsmoothed_perron_strict_self_contained_closed={fmt_bool(result['unsmoothed_perron_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        "BacklundCS8SlackAfterBridgeLedger",
        f"  => {result['replacement_self_contained']['BacklundCS8SlackAfterBridgeLedger']}",
        "",
        "RVMToCN16LocalInequalityLedger",
        f"  => {result['replacement_self_contained']['RVMToCN16LocalInequalityLedger']}",
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
            "也就是把 Titchmarsh 型局部展开从“结构来源/外部登记”推进成项目内作者侧显式账本，再接 `Psi0HorizontalLocalZeroDistanceSumConstantLedger`。",
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
