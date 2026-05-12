#!/usr/bin/env python3
"""生成 strict pair-energy 非循环对齐证书。

用法示例：
  python3 experiments/prime_matrix_strict_pair_energy_noncycle_reconciliation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-pair-energy-noncycle-reconciliation-router.md"

PAIR_ENERGY = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
RATE_PACKET = "RateBearingLargePairAtomPacketExclusion"
TERMINAL_GATE = (
    "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
    "DirectAcyclicSameSetPDECCapDualCertificate OR "
    "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
)
SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
INDEPENDENT_NONTERMINAL = (
    "IndependentNonterminalProofOfNewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
)
KERNEL_IDENTITY = "SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion"
POINTWISE_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
JOINT_CONSTRUCTOR = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
EXACT_UV_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-latest-self-contained-hardpoint-sync-router.json",
    "prime-matrix-strict-independent-pair-energy-attack-router.json",
    "prime-matrix-strict-rate-bearing-large-pair-packet-router.json",
    "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json",
    "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json",
    "prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json",
    "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json",
    "prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json",
    "prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象，便于旧工作树复核。"""
    path = MONOGRAPH / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本证书引用的上游文件哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = MONOGRAPH / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


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


def chain() -> list[dict[str, str]]:
    """列出 pair-energy 路线与非循环替代路线。"""
    return [
        {"from": PAIR_ENERGY, "to": RATE_PACKET},
        {"from": RATE_PACKET, "to": TERMINAL_GATE},
        {"from": TERMINAL_GATE, "to": f"AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR {SOURCE_ENTROPY}"},
        {"from": SOURCE_ENTROPY, "to": INDEPENDENT_NONTERMINAL},
        {"from": INDEPENDENT_NONTERMINAL, "to": KERNEL_IDENTITY},
        {"from": KERNEL_IDENTITY, "to": POINTWISE_TABLE},
        {"from": POINTWISE_TABLE, "to": f"{JOINT_CONSTRUCTOR} AND {EXACT_UV_INCIDENCE} AND {RATE}"},
    ]


def build_rows(
    latest: dict[str, Any],
    pair: dict[str, Any],
    packet: dict[str, Any],
    terminal: dict[str, Any],
    fixed: dict[str, Any],
    nonterminal: dict[str, Any],
    kernel: dict[str, Any],
    table: dict[str, Any],
    leaf: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成非循环对齐判定表。"""
    latest_pair_active = latest.get("next_direct_attack_target") == PAIR_ENERGY
    pair_to_packet = pair.get("internal_obligation_after_router") == RATE_PACKET
    packet_to_terminal = packet.get("rate_bearing_packet_split_closed") is True
    terminal_returns = terminal.get("terminal_route_returns_to_source_entropy_target") is True
    fixed_point_closed = fixed.get("new_actual_source_entropy_fixed_point_firewall_closed") is True
    nonterminal_atomized = (
        nonterminal.get("independent_nonterminal_atomization_closed") is True
        and nonterminal.get("preterminal_actual_fulls_factor_support_capacity_proved") is False
    )
    kernel_to_table = (
        kernel.get("kernel_identity_attack_router_closed") is True
        and kernel.get("pointwise_primitive_kernel_table_proved") is False
    )
    field_boundary = (
        table.get("field_contract_boundary_closed") is True
        and table.get("explicit_joint_alpha_delta_constructor_rule_proved") is False
    )
    joint_loops = leaf.get("joint_constructor_path_is_fixed_point_without_new_formula") is True
    return [
        row(
            "LatestPairEnergyInputActive",
            latest_pair_active,
            False,
            "最新同步把抽象 pair-energy 输入列为 direct attack target。",
            PAIR_ENERGY,
        ),
        row(
            "PairEnergyExistingAttackReducesToPacket",
            pair_to_packet,
            False,
            "既有直攻已证明 seed-only 与定性投影不够，pair-energy 失败等价于 rate-bearing 大 pair packet。",
            RATE_PACKET,
        ),
        row(
            "RatePacketTerminalSplitClosedOnlyAsRouting",
            packet_to_terminal,
            False,
            "大 pair packet 已分到 canonical、PDEC、sparse/ColumnCRT、clean residual 四类，但这些只是终端入口。",
            TERMINAL_GATE,
        ),
        row(
            "TerminalRouteReturnsToSourceEntropy",
            terminal_returns,
            True,
            "direct PDEC/CleanKLS 终端路线经防火墙回到 canonical-lock 或原 source-entropy 目标。",
            f"AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR {SOURCE_ENTROPY}",
        ),
        row(
            "CurrentPairEnergySpineRejectedAsProof",
            fixed_point_closed,
            True,
            "ExactUV/pair-energy/rate-packet/terminal/canonical 旧脊柱形成 T->...->T 固定点，不能作为 T 的证明。",
            INDEPENDENT_NONTERMINAL,
        ),
        row(
            "IndependentNonterminalAtomizationImported",
            nonterminal_atomized,
            False,
            "非循环 source-entropy 证明已压成 pre-terminal 支撑/容量，再回到同 formal-unit kernel/table 需求。",
            KERNEL_IDENTITY,
        ),
        row(
            "KernelIdentityReducedToPointwiseTable",
            kernel_to_table,
            False,
            "同 formal-unit 核恒等式不能由记录守恒或几何 Phi 自动推出，必须提交逐 primitive 核表。",
            POINTWISE_TABLE,
        ),
        row(
            "PointwiseTableFieldBoundaryClosed",
            field_boundary,
            False,
            "逐点核表字段边界已闭合；首个生产性字段是 actual joint alpha/delta constructor rule。",
            f"{JOINT_CONSTRUCTOR} AND {EXACT_UV_INCIDENCE}",
        ),
        row(
            "JointConstructorKnownRouteLoopsWithoutNewFormula",
            joint_loops,
            True,
            "若没有新的显式 joint constructor 公式工件，现有 joint-alpha 链会回到 signed-source 固定点。",
            JOINT_CONSTRUCTOR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只切断 pair-energy 旧脊柱的循环用法，并确定非循环首个生产性工件；尚未给出该工件。",
            f"({JOINT_CONSTRUCTOR} AND {EXACT_UV_INCIDENCE}) AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 pair-energy 非循环对齐证书。"""
    latest = load_json("prime-matrix-strict-latest-self-contained-hardpoint-sync-router.json")
    pair = load_json("prime-matrix-strict-independent-pair-energy-attack-router.json")
    packet = load_json("prime-matrix-strict-rate-bearing-large-pair-packet-router.json")
    terminal = load_json("prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json")
    fixed = load_json("prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json")
    nonterminal = load_json("prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json")
    kernel = load_json("prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json")
    table = load_json("prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json")
    leaf = load_json("prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json")
    rows = build_rows(latest, pair, packet, terminal, fixed, nonterminal, kernel, table, leaf)
    strict_basis = f"({JOINT_CONSTRUCTOR} AND {EXACT_UV_INCIDENCE}) AND {RATE} AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_strict_pair_energy_noncycle_reconciliation_router",
        "status": "pair_energy_latest_target_reconciled_to_noncycle_pointwise_constructor_inputs_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "pair_energy_abstract_input_active": latest.get("next_direct_attack_target") == PAIR_ENERGY,
        "current_pair_energy_attack_spine_is_recursive": True,
        "terminal_route_returns_to_source_entropy_target": terminal.get("terminal_route_returns_to_source_entropy_target") is True,
        "new_actual_source_entropy_fixed_point_firewall_closed": fixed.get("new_actual_source_entropy_fixed_point_firewall_closed") is True,
        "noncycle_pointwise_table_required": True,
        "explicit_joint_constructor_rule_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": PAIR_ENERGY,
        "noncycle_reconciled_target": POINTWISE_TABLE,
        "first_productive_input_after_router": JOINT_CONSTRUCTOR,
        "parallel_input_after_router": EXACT_UV_INCIDENCE,
        "strict_active_basis_after_router": strict_basis,
        "compression_chain": chain(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed` 仍是最新同步中的合法抽象输入，"
            "但沿当前已建 pair-energy/rate-packet/terminal 路线推进会回到 "
            "`NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` 固定点，不能作为非递归证明。"
            "因此本步把它与固定点防火墙重新对齐：strict 自足线若要继续闭合，必须提交同一 formal unit "
            "的逐 primitive alpha/delta 核表；在字段层，首个生产性输入是 "
            "`ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple`，"
            "并行还必须给出 `ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem`、RatePreservation 与 DStructure 门。"
            "这些仍未证明，所以行/列命题不能升级为无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict pair-energy 非循环对齐证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pair_energy_abstract_input_active={fmt_bool(result['pair_energy_abstract_input_active'])}",
        f"current_pair_energy_attack_spine_is_recursive={fmt_bool(result['current_pair_energy_attack_spine_is_recursive'])}",
        f"noncycle_pointwise_table_required={fmt_bool(result['noncycle_pointwise_table_required'])}",
        f"explicit_joint_constructor_rule_proved={fmt_bool(result['explicit_joint_constructor_rule_proved'])}",
        f"actual_emitter_exact_uv_bounded_multiplicity_incidence_proved={fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}",
        f"rate_preservation_ledger_proved={fmt_bool(result['rate_preservation_ledger_proved'])}",
        f"dstructure_independent_gate_closed={fmt_bool(result['dstructure_independent_gate_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 非循环对齐链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["compression_chain"]:
        lines.append(
            "| {from_} | {to} |".format(
                from_=table_cell(item["from"]),
                to=table_cell(item["to"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 当前严格活动基",
            "",
            "```text",
            result["strict_active_basis_after_router"],
            "```",
            "",
            "下一真正生产性输入：",
            "",
            "```text",
            result["first_productive_input_after_router"],
            "```",
            "",
            "并行必须保留：",
            "",
            "```text",
            result["parallel_input_after_router"],
            "RatePreservationLedger_FOR_moving_atom_packet",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            "```",
            "",
            "审稿边界：本证书只切断 pair-energy 旧脊柱的循环用法并固定非循环输入，不声称已证明这些输入。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
