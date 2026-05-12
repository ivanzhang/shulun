#!/usr/bin/env python3
"""生成 strict 统一矛盾场当前前沿同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_unified_contradiction_field_current_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-unified-contradiction-field-current-frontier-router.json

输出：
  docs/monograph/prime-matrix-strict-unified-contradiction-field-current-frontier-router.json
  docs/monograph/prime-matrix-strict-unified-contradiction-field-current-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-unified-contradiction-field-current-frontier-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-unified-contradiction-field-current-frontier-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.md",
    MONOGRAPH / "prime-matrix-strict-block-coprime-dynamics-capacity-surplus-router.md",
    MONOGRAPH / "prime-matrix-strict-alpha-prefix-load-deficit-pdec-router.md",
    MONOGRAPH / "prime-matrix-strict-alpha-prefix-signed-endpoint-defect-split-router.md",
    MONOGRAPH / "prime-matrix-strict-weighted-dyadic-endpoint-pdec-hdl-router.md",
    MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-fourier-upper-router.md",
    MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.md",
    MONOGRAPH / "prime-matrix-strict-iterated-threshold-collapse-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.md",
    MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-self-contained-mertens-tail-frontier-router.md",
    MONOGRAPH / "prime-matrix-b3-external-chain-to-dstructure-gate-router.md",
]

B3_TV = "B3RemainderTotalVariationBudgetForLengthP"
UNSMOOTHED = "UnsmoothedChebyshevPerronExplicitFormulaConstantLedger"
INTERNAL_ZERO_SUM = "InternalZeroSumDyadicContourBudgetLedger"
THETA_TARGET = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
B1_INTERVAL = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
UNIFIED_INEQUALITY = "UnifiedTerminalBudgetStrictInequality"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，避免同步证书因旧文件缺失中断。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def factor_rows() -> list[dict[str, str]]:
    """列出统一矛盾场已积累的结构因子。"""
    return [
        {
            "layer": "相邻/商互质",
            "closed_factor": "连续列因子支撑互质；同一大素标签短距复用要求 q|d。",
            "pressure": "把早期零行的连续合数解释压成有限供给容量问题。",
            "remaining": "已接入容量场；不再是独立硬点。",
        },
        {
            "layer": "块容量反超",
            "closed_factor": "|R_{B,z}|>C_{B,z} 即直接矛盾；alpha>1/2 时全行高标签容量 <=2(pi(P)-pi(alpha P))。",
            "pressure": "若负载不反超，则必产生总变差/端点缺陷。",
            "remaining": "AlphaPrefixTotalVariationOrEndpointPDECDefectExclusion 已继续下钻。",
        },
        {
            "layer": "有符号端点缺陷",
            "closed_factor": "容量失败强制 E_alpha<=-G_alpha，并分裂为低模、中间 dyadic、远尾 core 三出口。",
            "pressure": "正权端点亏损形成零均值 Fourier/PDEC 证书。",
            "remaining": "低有效模、倒数共同因子和短窗口除数密度已继续下钻。",
        },
        {
            "layer": "除数密度/LCM",
            "closed_factor": "热短窗口除数密度强制 LCM 爆炸或低乘子共同核复现。",
            "pressure": "共同核复现进一步压成有限商型、缩频核心和稀疏历史。",
            "remaining": "热核心/固定历史 PDEC 与稀疏历史预算仍是命名出口。",
        },
        {
            "layer": "稀疏终端历史",
            "closed_factor": "历史词、深度、字母表和非持久供给预算公式均已登记。",
            "pressure": "若 L_forced 超过冷核心供给，则早期零行直接供需矛盾。",
            "remaining": "强制负载下界、终端抗塌缩和命名回流排斥仍需输入。",
        },
        {
            "layer": "统一终端预算",
            "closed_factor": "((P-1)W^--TV)/ceil(P/z)-E_named > sum_W(T_PDEC(W)-1)C_core(W) 可直接闭合矛盾。",
            "pressure": "所有结构压力被压到 B3 总变差、终端抗塌缩和冷供给三组输入。",
            "remaining": B3_TV,
        },
        {
            "layer": "B3/解析输入",
            "closed_factor": "B3 TV 在接受外部显式 Mertens/Dusart 时条件关闭；外部 B3 解析链已到 DStructure/Rankin 门。",
            "pressure": "严格自足路线需补 Mertens 尾段内部证明。",
            "remaining": f"{UNSMOOTHED} AND {INTERNAL_ZERO_SUM} AND {THETA_TARGET} AND {B1_INTERVAL}",
        },
    ]


def frontier_rows(b3_tv: dict[str, Any], mertens: dict[str, Any], external: dict[str, Any]) -> list[dict[str, Any]]:
    """生成当前前沿判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "同步证书只整理假设早期零行反例链与真实结构链的当前交点。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "UnifiedContradictionFactorsAccumulated",
            "closed": True,
            "proved": False,
            "meaning": "相邻互质、容量反超、端点 Fourier、LCM、稀疏历史、冷核心供需和 B3/TV 已进入同一矛盾场。",
            "remaining": "尚未找到单个无条件反超交点。",
        },
        {
            "gate": "B3TVConditionalExternalClosed",
            "closed": b3_tv.get("b3_tv_budget_conditional_external_closed") is True,
            "proved": False,
            "meaning": "接受外部显式 Mertens/Dusart 输入时，B3 总变差预算可条件关闭。",
            "remaining": "不是严格自足闭合。",
        },
        {
            "gate": "B3TVStrictSelfContainedClosed",
            "closed": b3_tv.get("b3_tv_budget_strict_self_contained_proved") is True,
            "proved": b3_tv.get("b3_tv_budget_strict_self_contained_proved") is True,
            "meaning": "严格自足 B3 TV 仍取决于自足 reciprocal-prime Mertens 尾段。",
            "remaining": "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372",
        },
        {
            "gate": "SelfContainedMertensTailClosed",
            "closed": mertens.get("self_contained_mertens_tail_proved") is True,
            "proved": mertens.get("self_contained_mertens_tail_proved") is True,
            "meaning": "自足 Mertens 尾段尚未闭合；最新自足解析最窄点是非平滑 Perron 常数。",
            "remaining": mertens.get("next_direct_attack_target", UNSMOOTHED),
        },
        {
            "gate": "ExternalB3AnalyticChainReachesDStructureGate",
            "closed": external.get("b3_external_analytic_chain_closed_to_dstructure_gate") is True,
            "proved": False,
            "meaning": "外部条件链已经推进到 DStructure/Rankin 独立验收门。",
            "remaining": DSTRUCTURE_GATE,
        },
        {
            "gate": "DStructureIndependentAcceptancePresent",
            "closed": external.get("promotion_package_independently_accepted") is True,
            "proved": external.get("promotion_package_independently_accepted") is True,
            "meaning": "未出现独立接受事件时，外部链不能升级为无条件闭合。",
            "remaining": DSTRUCTURE_GATE,
        },
        {
            "gate": "DirectUnconditionalContradictionFound",
            "closed": False,
            "proved": False,
            "meaning": "当前语料仍未给出反例链与真实结构链之间的最终单点矛盾。",
            "remaining": f"{UNSMOOTHED} OR internal zero-sum/theta/B1 OR terminal named-return exclusions",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书对象。"""
    b3_tv = load_json(MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json")
    mertens = load_json(MONOGRAPH / "prime-matrix-strict-self-contained-mertens-tail-frontier-router.json")
    external = load_json(MONOGRAPH / "prime-matrix-b3-external-chain-to-dstructure-gate-router.json")
    next_self = mertens.get("next_direct_attack_target", UNSMOOTHED)
    external_at_gate = external.get("b3_external_analytic_chain_closed_to_dstructure_gate") is True
    dstructure_accepted = external.get("promotion_package_independently_accepted") is True
    return {
        "certificate_type": "prime_matrix_strict_unified_contradiction_field_current_frontier_router",
        "status": "unified_contradiction_field_current_frontier_synced_self_contained_mertens_open_external_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "unified_factors_accumulated": True,
        "b3_tv_conditional_external_closed": b3_tv.get("b3_tv_budget_conditional_external_closed") is True,
        "b3_tv_strict_self_contained_closed": b3_tv.get("b3_tv_budget_strict_self_contained_proved") is True,
        "self_contained_mertens_tail_closed": mertens.get("self_contained_mertens_tail_proved") is True,
        "external_b3_chain_reaches_dstructure_gate": external_at_gate,
        "dstructure_independent_acceptance_present": dstructure_accepted,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": next_self,
        "parallel_attack_targets": [INTERNAL_ZERO_SUM, THETA_TARGET, B1_INTERVAL, DSTRUCTURE_GATE],
        "strict_self_contained_boundary": (
            f"{next_self} AND {INTERNAL_ZERO_SUM} AND {THETA_TARGET} AND "
            f"FiniteThetaEnvelopeBridgeBelowAnalyticThreshold AND {B1_INTERVAL}"
        ),
        "external_conditional_boundary": (
            "B3 external analytic chain + "
            f"{DSTRUCTURE_GATE}"
        ),
        "factor_rows": factor_rows(),
        "frontier_rows": frontier_rows(b3_tv, mertens, external),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "统一矛盾场当前已不是单一的相邻互质或容量判据，而是一条已分层登记的压力链："
            "相邻/商互质给容量场，容量失败给有符号端点缺陷，端点缺陷给 Fourier/PDEC，"
            "低有效模给除数窗口，除数窗口给 LCM/固定商型/稀疏历史，最后统一成冷核心供需预算。"
            "外部显式 Mertens/Dusart 路线可把 B3 TV 条件关闭并推进到 DStructure/Rankin 门；"
            "严格自足路线的当前最窄解析入口仍是自足 Mertens 尾段中的非平滑 Perron 常数。"
            "因此目前不能声明行/列无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 统一矛盾场当前前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unified_factors_accumulated={fmt_bool(result['unified_factors_accumulated'])}",
        f"b3_tv_conditional_external_closed={fmt_bool(result['b3_tv_conditional_external_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"external_b3_chain_reaches_dstructure_gate={fmt_bool(result['external_b3_chain_reaches_dstructure_gate'])}",
        f"dstructure_independent_acceptance_present={fmt_bool(result['dstructure_independent_acceptance_present'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 已积累矛盾因子",
        "",
        "| layer | closed factor | pressure | remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["factor_rows"]:
        lines.append(
            "| {layer} | {closed} | {pressure} | {remaining} |".format(
                layer=table_cell(row["layer"]),
                closed=table_cell(row["closed_factor"]),
                pressure=table_cell(row["pressure"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 当前前沿判定",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["frontier_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 3. 当前最窄点",
            "",
            "严格自足主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "严格自足边界包：",
            "",
            "```text",
            result["strict_self_contained_boundary"],
            "```",
            "",
            "外部条件边界：",
            "",
            "```text",
            result["external_conditional_boundary"],
            "```",
            "",
            "审稿边界：外部条件链不能替代严格自足证明；未出现 DStructure/Rankin 独立接受前，也不能宣称行/列无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
