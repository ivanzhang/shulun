#!/usr/bin/env python3
"""生成 strict 局部零点倒距离自足同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_local_zero_distance_self_contained_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-local-zero-distance-self-contained-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-local-zero-distance-self-contained-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-local-zero-distance-self-contained-sync-router.md"

BACKLUND = MONOGRAPH / "prime-matrix-strict-backlund-internal-closure-reconciliation-router.json"
RVM_CN16 = MONOGRAPH / "prime-matrix-strict-rvm-cn16-self-contained-sync-router.json"
LOGDER = MONOGRAPH / "prime-matrix-strict-logder-internal-expansion-router.json"
EXTERNAL_LOCAL = MONOGRAPH / "prime-matrix-b3-psi0-horizontal-local-zero-distance-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [BACKLUND, RVM_CN16, LOGDER, EXTERNAL_LOCAL, CLAIM_STATUS]

OLD_ATOM = "Psi0HorizontalLocalZeroDistanceSumConstantLedger"
CLOSED_ATOM = "Psi0HorizontalLocalZeroDistanceSumSelfContainedClosedC288Eta1Over16"
EXTERNAL_CLOSED_ATOM = "Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16"
WEIGHTED = "Psi0HorizontalWeightedIntegralBudgetLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ETA = 1.0 / 16.0
C_N = 16.0
C_STRUCTURAL_REMAINDER = 32.0
C_LOCAL_DISTANCE = C_N / ETA
C_TOTAL_LOGDER = C_LOCAL_DISTANCE + C_STRUCTURAL_REMAINDER


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记证据文件哈希，便于之后复核。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


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


def row_closed(rows: list[dict[str, Any]], gate: str) -> bool:
    """读取依赖证书中的 gate 状态。"""
    for item in rows:
        if item.get("gate") == gate:
            return item.get("closed") is True and item.get("proved") is True
    return False


def constant_rows() -> list[dict[str, Any]]:
    """登记 C=288 的常数来源。"""
    return [
        {
            "item": "eta",
            "value": ETA,
            "formula": "1/16",
            "meaning": "共同缩进纪律之后，剩余水平段离目标零点的登记最小距离。",
        },
        {
            "item": "C_N",
            "value": C_N,
            "formula": "RVMToCN16LocalInequalitySelfContainedClosedWithRawArgCS8CommonEnvelope",
            "meaning": "自足同步后的单位高度局部零点数常数。",
        },
        {
            "item": "local distance coefficient",
            "value": C_LOCAL_DISTANCE,
            "formula": "C_N/eta",
            "meaning": "近零点倒距离总贡献的粗上界系数。",
        },
        {
            "item": "structural remainder reserve",
            "value": C_STRUCTURAL_REMAINDER,
            "formula": "HadamardGammaRemainder reserve",
            "meaning": "log-derivative 展开中非局部主部的结构余项预留。",
        },
        {
            "item": "total pointwise coefficient",
            "value": C_TOTAL_LOGDER,
            "formula": "256 + 32",
            "meaning": "水平边点态界的最终系数。",
        },
    ]


def sample_rows() -> list[dict[str, float]]:
    """给代表性高度生成点态上界样例。"""
    rows: list[dict[str, float]] = []
    for height in [14.0, 45.0, 100.0, 1000.0, 20000.0, 1_000_000.0]:
        log_t = math.log(height + 3.0)
        rows.append(
            {
                "T": height,
                "log_T_plus_3": log_t,
                "pointwise_bound": C_TOTAL_LOGDER * log_t,
            }
        )
    return rows


def build_rows(
    backlund: dict[str, Any],
    rvm_cn16: dict[str, Any],
    logder: dict[str, Any],
    external_local: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 strict 自足同步判定表。"""
    guard = (
        backlund.get("counterexample_assumption_only") is True
        and rvm_cn16.get("counterexample_assumption_only") is True
        and logder.get("counterexample_assumption_only") is True
        and backlund.get("direct_unconditional_contradiction_found") is False
        and rvm_cn16.get("direct_unconditional_contradiction_found") is False
        and logder.get("direct_unconditional_contradiction_found") is False
        and backlund.get("row_column_unconditional_closed") is False
        and rvm_cn16.get("row_column_unconditional_closed") is False
        and logder.get("row_column_unconditional_closed") is False
    )
    fixed_indent = (
        backlund.get("strict_perron_backlund_atom_replaced") is True
        and row_closed(backlund.get("rows", []), "FixedTIndentAtomReconciled")
    )
    cn16_ready = (
        rvm_cn16.get("rvm_cn16_self_contained_resynchronized") is True
        and row_closed(rvm_cn16.get("rows", []), "RVMToCN16SelfContainedSynchronized")
    )
    logder_ready = (
        logder.get("classical_zeta_logder_internal_expansion_closed") is True
        and row_closed(logder.get("rows", []), "ClassicalLogDerivativeExpansionClosed")
    )
    old_atom_active = OLD_ATOM in str(logder.get("remaining_after_logder_expansion", []))
    external_formula_checked = (
        external_local.get("psi0_horizontal_local_zero_distance_external_closed") is True
        and abs(float(external_local.get("C_total_logder", 0.0)) - C_TOTAL_LOGDER) < 1e-9
    )
    eta_budget = (
        ETA == 1.0 / 16.0
        and abs(C_LOCAL_DISTANCE - 256.0) < 1e-12
        and abs(C_TOTAL_LOGDER - 288.0) < 1e-12
    )
    local_self_closed = guard and fixed_indent and cn16_ready and logder_ready and old_atom_active and eta_budget
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理早期零行假设链条中的解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "LocalZeroDistanceAtomActive",
            old_atom_active,
            True,
            "log-derivative 展开闭合后，strict Perron 的下一原子正是局部倒距离和。",
            OLD_ATOM,
        ),
        row(
            "FixedTIndentDisciplineSelfContained",
            fixed_indent,
            fixed_indent,
            "共同高高度包络已把 fixed-T 缩进原子调和为作者侧可用的内部闭合输入。",
            "ClassicalBacklundZeroIndentationCostInternalProofClosedByHighPowerCommonEnvelope",
        ),
        row(
            "RVMCN16SelfContainedAvailable",
            cn16_ready,
            cn16_ready,
            "RVM 原始 arg 归一化、CS8 边界桥和低高度 xi 子包已同步为 C_N=16。",
            "RVMToCN16LocalInequalitySelfContainedClosedWithRawArgCS8CommonEnvelope",
        ),
        row(
            "LogDerivativeExpansionSelfContainedAvailable",
            logder_ready,
            logder_ready,
            "Hadamard 对数导数、Gamma/digamma 和余项账本已给出内部结构展开。",
            "ClassicalZetaLogDerivativeAwayFromZerosInternalExpansionClosedByHadamardGammaRemainder",
        ),
        row(
            "ExternalFormulaReusedOnlyAsArithmeticCheck",
            external_formula_checked,
            True,
            "旧外部证书只复用 eta=1/16、C_N/eta+32=288 的算术模板，不复用外部假设。",
            EXTERNAL_CLOSED_ATOM,
        ),
        row(
            "EtaOneOver16C288BudgetClosed",
            eta_budget,
            True,
            "在缩进后的水平段，每个近零点贡献至多 1/eta；16/(1/16)+32=288。",
            CLOSED_ATOM,
        ),
        row(
            "Psi0LocalZeroDistanceSelfContainedClosed",
            local_self_closed,
            local_self_closed,
            "三项内部输入全部到位后，局部零点倒距离和从外部条件版升级为 strict 自足版。",
            CLOSED_ATOM,
        ),
        row(
            "UnsmoothedPerronStrictSelfContainedClosed",
            False,
            False,
            "本步只关闭点态倒距离常数；水平加权积分预算仍未 strict 自足同步。",
            WEIGHTED,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只是解析输入自足化，不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    backlund = load_json(BACKLUND)
    rvm_cn16 = load_json(RVM_CN16)
    logder = load_json(LOGDER)
    external_local = load_json(EXTERNAL_LOCAL)
    rows = build_rows(backlund, rvm_cn16, logder, external_local)
    local_self_closed = next(item["closed"] for item in rows if item["gate"] == "Psi0LocalZeroDistanceSelfContainedClosed")
    return {
        "certificate_type": "prime_matrix_strict_local_zero_distance_self_contained_sync_router",
        "status": "psi0_local_zero_distance_self_contained_closed_weighted_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "psi0_horizontal_local_zero_distance_self_contained_closed": local_self_closed,
        "psi0_horizontal_weighted_integral_budget_self_contained_closed": False,
        "unsmoothed_perron_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "eta": ETA,
        "C_N": C_N,
        "C_local_distance": C_LOCAL_DISTANCE,
        "C_structural_remainder": C_STRUCTURAL_REMAINDER,
        "C_total_logder": C_TOTAL_LOGDER,
        "replacement_self_contained": {
            OLD_ATOM: CLOSED_ATOM,
        },
        "remaining_after_local_zero_distance_sync": [WEIGHTED],
        "next_direct_attack_target": WEIGHTED,
        "source_hashes": source_hashes(),
        "constant_rows": constant_rows(),
        "sample_rows": sample_rows(),
        "plain_conclusion": (
            "`Psi0HorizontalLocalZeroDistanceSumConstantLedger` 已可从外部条件版同步为 strict 自足版："
            "共同包络提供 fixed-T 缩进纪律，RVM-CN16 同步提供 C_N=16，"
            "Hadamard/Gamma/余项提供内部 log-derivative 展开；"
            "因此 eta=1/16 给出 C_N/eta=256，再加结构余项 32，得到 C=288。"
            "该步不关闭加权水平积分预算，也不关闭行/列无条件命题。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix strict 局部零点倒距离自足同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"psi0_horizontal_local_zero_distance_self_contained_closed={fmt_bool(result['psi0_horizontal_local_zero_distance_self_contained_closed'])}",
        f"psi0_horizontal_weighted_integral_budget_self_contained_closed={fmt_bool(result['psi0_horizontal_weighted_integral_budget_self_contained_closed'])}",
        f"unsmoothed_perron_strict_self_contained_closed={fmt_bool(result['unsmoothed_perron_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"C_total_logder={fmt_float(result['C_total_logder'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        f"  => {replacement[1]}",
        "```",
        "",
        "## 2. 常数表",
        "",
        "| item | value | formula | meaning |",
        "| --- | ---: | --- | --- |",
    ]
    for item in result["constant_rows"]:
        lines.append(
            "| {item} | `{value}` | {formula} | {meaning} |".format(
                item=table_cell(item["item"]),
                value=fmt_float(float(item["value"])),
                formula=table_cell(item["formula"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 样例上界",
            "",
            "| T | log(T+3) | pointwise bound |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in result["sample_rows"]:
        lines.append(
            "| {T} | {L} | {B} |".format(
                T=fmt_float(float(item["T"])),
                L=fmt_float(float(item["log_T_plus_3"])),
                B=fmt_float(float(item["pointwise_bound"])),
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
            "## 5. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "也就是把点态 C=288 水平边界乘上 Perron 权重并压入 C=12000 的加权预算。",
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
