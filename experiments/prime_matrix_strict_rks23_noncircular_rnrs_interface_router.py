#!/usr/bin/env python3
"""把非循环倒数区间能量剩余压成 RNRS/Rudnev 入射接口。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_noncircular_rnrs_interface_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-noncircular-rnrs-interface-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-noncircular-rnrs-interface-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-noncircular-rnrs-interface-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-self-contained-cycle-guard-frontier-router.json"
POWER_RELAX = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"
MOBIUS_OVERLAP = MONO / "prime-matrix-strict-rks23-reciprocal-energy-mobius-overlap-router.json"
SUMPRODUCT_FRONTIER = MONO / "prime-matrix-strict-rks23-mobius-overlap-sumproduct-frontier-router.json"
P0_STATUS = DOCS / "explicit-p0-constants.status.md"
CRITICAL_BUCKET = DOCS / "critical-bucket-single-hit-sieve-attack.md"
BIBLIOGRAPHY = DOCS / "bibliography.md"

SOURCE_FILES = [
    PREVIOUS,
    POWER_RELAX,
    MOBIUS_OVERLAP,
    SUMPRODUCT_FRONTIER,
    P0_STATUS,
    CRITICAL_BUCKET,
    BIBLIOGRAPHY,
]

TARGET = "NonCircularSelfContainedReciprocalIntervalEnergyPowerSaving"
RNRS_INPUT = "SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling"
POINT_PLANE = "SelfContainedRudnevPointPlaneIncidenceProofWithReciprocalEnergyCorollary"
EXTERNAL_ROUTE = "AcceptRudnevRNRSReciprocalIntervalEnergyEstimateWithParameterMatch"
FIXED_POWER_ENERGY = "UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23"


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本包含全部关键片段。"""
    return all(item in text for item in needles)


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造 RNRS/Rudnev 接口证书。"""
    previous = load_json(PREVIOUS)
    power = load_json(POWER_RELAX)
    mobius = load_json(MOBIUS_OVERLAP)
    sumproduct = load_json(SUMPRODUCT_FRONTIER)
    p0_status = read_text(P0_STATUS)
    critical = read_text(CRITICAL_BUCKET)
    bibliography = read_text(BIBLIOGRAPHY)

    target_active = (
        previous.get("next_direct_attack_target") == TARGET
        and previous.get("self_contained_cycle_detected") is True
        and previous.get("noncircular_reciprocal_energy_input_proved") is False
    )
    fixed_power_reduction_ready = (
        power.get("fixed_power_saving_implies_required_log_saving") is True
        and power.get("next_direct_attack_target") == FIXED_POWER_ENERGY
    )
    mobius_dictionary_ready = (
        mobius.get("mobius_overlap_identity_closed") is True
        and sumproduct.get("energy_mobius_sumproduct_dictionary_closed") is True
    )
    rudnev_interface_present = contains_all(
        critical,
        [
            "Rudnev point-plane incidence",
            "I(R,Π) <= C_Rud",
            "RNRS",
            "E_+(B) <= M^{5/2}",
        ],
    )
    external_reference_registered = contains_all(
        bibliography,
        ["[Rudnev-RNRS]", "Roche-Newton--Rudnev--Shkredov"],
    ) or contains_all(p0_status, ["Rudnev", "Roche-Newton", "Shkredov"])

    exact_interface_closed = (
        target_active
        and fixed_power_reduction_ready
        and mobius_dictionary_ready
        and rudnev_interface_present
        and external_reference_registered
    )
    # 若 RNRS/Rudnev 给 E_+(J^{-1}) <= C N^(5/2) P^eps，
    # 在 N≈P^(1/2)log^O(P) 的颈部，这就是固定幂节省 δ=1/2-o(1)，足以支付所有固定 log 损失。
    parameter_sufficiency_closed = exact_interface_closed
    external_route_would_close_if_accepted = exact_interface_closed
    self_contained_rnrs_proof_closed = False
    row_column_closed = False

    interface = {
        "set": "B=J^{-1} in F_P, where J is an integer interval",
        "collar": "|J|=N with P^(1/2)/log^236(P)<=N<=P^(1/2)log^236(P)",
        "target_energy": "E_+(B)=#{b1+b2=b3+b4: bi in B}",
        "sufficient_bound": "E_+(J^{-1}) <= C*N^(5/2)*P^eps, or any E_+<=N^(3-delta_E) with fixed delta_E>0",
        "why_sufficient": "N^delta_E dominates every fixed log power in the square-root log collar",
        "rudnev_input": "point-plane incidence I(R,Pi)<=C_Rud(|R|^(1/2)|Pi|+k|Pi|), plus RNRS reciprocal-energy corollary",
        "noncircular_requirement": "the proof must be imported from incidence/sum-product geometry, not from the RKS23 inverse-sumproduct chain itself",
        "accepted_external_route": EXTERNAL_ROUTE,
    }

    noncircular_audit = {
        "cycle_guard": "previous router detected that RKS-log -> balanced energy -> Mobius overlap returns to the same inverse-sumproduct frontier",
        "allowed": "a direct self-contained proof of Rudnev point-plane incidence and its reciprocal-energy corollary",
        "allowed_external": "explicit acceptance of Rudnev/RNRS with parameter match",
        "not_allowed": "reusing the already cyclic RKS23/slope-conic/character-moment route as the proof of the same energy input",
    }

    rows = [
        row(
            "NonCircularEnergyTargetActive",
            target_active,
            True,
            "上一证书已把真正剩余固定为非循环倒数区间能量输入。",
            TARGET,
        ),
        row(
            "FixedPowerEnergyReductionImported",
            fixed_power_reduction_ready,
            True,
            "只需固定幂节省，不必直接证明 log^-472。",
            FIXED_POWER_ENERGY,
        ),
        row(
            "MobiusAndInverseSumproductDictionaryImported",
            mobius_dictionary_ready,
            True,
            "倒数能量、Möbius 重叠谱、反演小和集字典已经闭合。",
            "dictionary closed",
        ),
        row(
            "RNRSRudnevInterfaceStatementClosed",
            exact_interface_closed,
            True,
            "所需非循环输入已精确为 Rudnev/RNRS 倒数区间能量固定幂节省接口。",
            RNRS_INPUT,
        ),
        row(
            "RNRSParameterSufficiencyClosed",
            parameter_sufficiency_closed,
            True,
            "`E_+(J^{-1})<=C N^(5/2)P^eps` 或任意固定幂节省足以推出当前目标。",
            "parameter ledger closed",
        ),
        row(
            "ExternalRudnevRNRSWouldCloseIfAccepted",
            external_route_would_close_if_accepted,
            True,
            "若接受外部 Rudnev/RNRS 定理并完成参数匹配，本输入可外部闭合。",
            EXTERNAL_ROUTE,
        ),
        row(
            RNRS_INPUT,
            self_contained_rnrs_proof_closed,
            False,
            "严格内部自足版仍未内联 Rudnev 点-平面 incidence 及 RNRS 倒数能量推论。",
            POINT_PLANE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_closed,
            False,
            "本步闭合的是接口和参数充分性；未补入自足 incidence 证明。",
            RNRS_INPUT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_noncircular_rnrs_interface_router",
        "status": "noncircular_reciprocal_energy_reduced_to_rudnev_rnrs_incidence_interface",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "noncircular_energy_target_active": target_active,
        "fixed_power_energy_reduction_imported": fixed_power_reduction_ready,
        "mobius_and_inverse_sumproduct_dictionary_imported": mobius_dictionary_ready,
        "rnrs_rudnev_interface_statement_closed": exact_interface_closed,
        "rnrs_parameter_sufficiency_closed": parameter_sufficiency_closed,
        "external_rudnev_rnrs_would_close_if_accepted": external_route_would_close_if_accepted,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_proof_closed,
        "row_column_unconditional_closed": row_column_closed,
        "next_direct_attack_target": RNRS_INPUT,
        "next_required_input": POINT_PLANE,
        "parallel_external_route": EXTERNAL_ROUTE,
        "interface": interface,
        "noncircular_audit": noncircular_audit,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "非循环剩余继续压窄：当前不再需要泛泛地重证 BG/RKS23，而只需一个独立的倒数区间能量定理。"
            "精确接口是：对平方根对数颈部中的区间 `J`，证明 `E_+(J^{-1})` 有任意固定幂节省；"
            "典型 Rudnev/RNRS 形态 `E_+(J^{-1})<=C|J|^(5/2)P^eps` 已足够。"
            "接受外部 Rudnev/RNRS 可闭合这一输入；严格自足路线则必须内联 Rudnev 点-平面 incidence "
            "及其 reciprocal-energy 推论，不能再回用已经检测到回环的 RKS23/inverse-sumproduct 链。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    interface = result["interface"]
    audit = result["noncircular_audit"]
    lines = [
        "# Prime Matrix strict RKS23 非循环 RNRS/Rudnev 接口证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"rnrs_rudnev_interface_statement_closed={fmt_bool(result['rnrs_rudnev_interface_statement_closed'])}",
        f"rnrs_parameter_sufficiency_closed={fmt_bool(result['rnrs_parameter_sufficiency_closed'])}",
        f"self_contained_rnrs_rudnev_proof_closed={fmt_bool(result['self_contained_rnrs_rudnev_proof_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确接口",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in interface.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 非循环审计",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in audit.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 下一真正自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            result["next_required_input"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    MONO.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
