#!/usr/bin/env python3
"""把 RKS2/RKS3 微薄边剩余压成精确 Whitney/端点 strip 带权质量账本。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_microscopic_thin_side_mass_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-microscopic-thin-side-mass-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-microscopic-thin-side-mass-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-microscopic-thin-side-mass-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-thin-packet-plancherel-floor-router.json"
RECTANGULARIZATION = MONO / "prime-matrix-strict-rks23-product-ratio-rectangular-convolution-router.json"
SOURCE_FILES = [PREVIOUS, RECTANGULARIZATION]

TARGET = "MicroscopicThinSidePacketMassAbsorptionAtCauchyScale"
LEDGER_ATOM = "MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale"
ENDPOINT_ATOM = "EndpointStripMultiplicityBoundForMicroscopicProductPackets"
BURGESS_ATOM = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"


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
    """构造微薄边质量路由证书。"""
    previous = load_json(PREVIOUS)
    rectangular = load_json(RECTANGULARIZATION)

    active = (
        previous.get("next_direct_attack_target") == TARGET
        and previous.get("microscopic_thin_packets_isolated") is True
        and previous.get("nonmicroscopic_thin_packets_absorbed") is True
    )
    geometry_imported = (
        rectangular.get("rotated_root_box_support_geometry_closed") is True
        and rectangular.get("dyadic_rectangularization_closed_up_to_polylog") is True
    )

    packetwise_reduction_closed = active
    four_side_union_closed = active
    endpoint_source_identified = active and geometry_imported
    bounded_overlap_insufficient = active

    # 关键结论：微薄边的解析估计已经不再是新的角色和问题。
    # 剩余必须证明一个几何 packing/端点 strip 重数账本。
    microscopic_side_ledger_proved = False
    endpoint_multiplicity_proved = False
    microscopic_absorbed = microscopic_side_ledger_proved and endpoint_multiplicity_proved
    thin_branch_absorbed = previous.get("nonmicroscopic_thin_packets_absorbed") is True and microscopic_absorbed
    burgess_still_open = previous.get("burgess_pointwise_input_still_open") is True

    definitions = {
        "packet": "Q=(I1,I2,I3,I4) with side lengths H_j=|I_j|",
        "micro_cutoff": "T=P^kappa, with fixed kappa>0 chosen below the needed packing margin",
        "microscopic_condition": "H_min(Q)=min_j H_j<T",
        "packet_l2": "L(Q)=(1/(P-1))*sum_{chi!=chi0} prod_j |S_Ij(chi)|^2",
        "cauchy_scale": "the centered product-ratio L2 scale required by the earlier Cauchy reduction",
        "allowed_losses": "dyadic and endpoint labels may cost only P^o(1), already registered as polylog losses",
    }

    analytic_reduction = {
        "shortest_side_plancherel": "if H_s=H_min(Q), then L(Q)<=H_s*prod_{j!=s} H_j^2",
        "micro_union_bound": "sum_{Q:H_min<T} L(Q) <= sum_{s=1}^4 sum_{Q:H_s<T} H_s*prod_{j!=s} H_j^2",
        "exact_remaining_ledger": (
            "prove sum_s sum_{Q:H_s<T} H_s*prod_{j!=s}H_j^2 "
            "<= CauchyScale*P^(-eta) after polylog losses"
        ),
        "conditional_closure": "this weighted side ledger immediately absorbs all microscopic thin packets",
        "why_this_is_narrow": "no character cancellation remains in the micro branch after this reduction",
    }

    obstruction = {
        "naive_small_length_fails": "H_s<T alone does not give fixed power saving when H_s is O(1)",
        "bounded_overlap_fails": "bounded overlap controls packet membership, not the one-power weighted sum H_s*prod_{j!=s}H_j^2",
        "natural_mass_mismatch": "natural packet mass has H_s^2, while the Plancherel bound has only H_s",
        "possible_bad_case": "many unit-width side packets repeated across endpoint phases can saturate the Cauchy scale unless strip multiplicity is bounded",
        "therefore_needed": ENDPOINT_ATOM,
    }

    geometric_target = {
        "source": "the previous rectangularization splits by signs, parity, and distances to strip boundaries",
        "required_structure": "every H_s<T packet must be charged to an endpoint/boundary strip of comparable width with bounded signed multiplicity",
        "sufficient_bound": (
            "for each side s and T=P^kappa, the total weighted strip mass is "
            "<= CauchyScale*P^(-eta) for some eta>0"
        ),
        "model_margin": "if the ambient side scale is P^theta and endpoint strips have total width O(T*P^o(1)), then any theta>kappa gives fixed power room",
        "unproved_part": "the current corpus has not registered the endpoint-strip multiplicity and ambient-scale margin with exact constants",
    }

    rows = [
        row(
            "MicroscopicThinSideAtomActive",
            active,
            True,
            "上一证书已把薄包唯一剩余隔离为 `H_min<P^kappa` 的微薄边包。",
            TARGET,
        ),
        row(
            "NonmicroscopicComplementAlreadyAbsorbed",
            previous.get("nonmicroscopic_thin_packets_absorbed") is True,
            True,
            "非微观薄包已由最短边 Plancherel 地板吸收。",
            "absorbed",
        ),
        row(
            "PacketwiseAnalyticReductionToWeightedSideLedgerClosed",
            packetwise_reduction_closed,
            True,
            "对最短边做 Plancherel 后，微薄包总贡献被精确压到 `H_s*prod_{j!=s}H_j^2` 的带权短边账本。",
            LEDGER_ATOM,
        ),
        row(
            "FourSideUnionBoundClosed",
            four_side_union_closed,
            True,
            "`H_min<T` 被四个事件 `H_s<T` 覆盖，只损失常数 4。",
            LEDGER_ATOM,
        ),
        row(
            "EndpointStripSourceIdentifiedFromRectangularization",
            endpoint_source_identified,
            True,
            "已有矩形化说明短边来自符号、奇偶和边界距离拆包；真正需要的是端点 strip 重数账本。",
            ENDPOINT_ATOM,
        ),
        row(
            "RawBoundedOverlapInsufficient",
            bounded_overlap_insufficient,
            True,
            "已有 bounded-overlap/polylog 只控制拆包数，不能替代 `H_s` 单幂带权质量下界。",
            ENDPOINT_ATOM,
        ),
        row(
            LEDGER_ATOM,
            microscopic_side_ledger_proved,
            microscopic_side_ledger_proved,
            "仓库内尚未证明微薄边带权 Whitney packing 质量相对 Cauchy 尺度有固定幂余量。",
            ENDPOINT_ATOM,
        ),
        row(
            ENDPOINT_ATOM,
            endpoint_multiplicity_proved,
            endpoint_multiplicity_proved,
            "仓库内尚未给出每个微薄边端点/边界 strip 的严格重数和环境尺度余量。",
            ENDPOINT_ATOM,
        ),
        row(
            "ThinDyadicPacketMassAbsorptionProved",
            thin_branch_absorbed,
            thin_branch_absorbed,
            "薄包分支需要非微观吸收与微薄边账本同时成立；当前只完成前者和解析归约。",
            LEDGER_ATOM,
        ),
        row(
            "BurgessPointwiseInputStillOpen",
            burgess_still_open,
            False,
            "大包分支的 Burgess 点态角色和输入仍是并行开放项。",
            BURGESS_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步是内部自足线的微薄边压缩证书，不宣称行/列命题无条件闭合。",
            f"{ENDPOINT_ATOM} AND {BURGESS_ATOM}",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_microscopic_thin_side_mass_router",
        "status": "microscopic_thin_side_reduced_to_endpoint_strip_weighted_packing_ledger",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "microscopic_thin_side_atom_active": active,
        "packetwise_analytic_reduction_to_weighted_side_ledger_closed": packetwise_reduction_closed,
        "four_side_union_bound_closed": four_side_union_closed,
        "endpoint_strip_source_identified_from_rectangularization": endpoint_source_identified,
        "raw_bounded_overlap_insufficient": bounded_overlap_insufficient,
        "microscopic_side_whitney_packing_mass_ledger_proved": microscopic_side_ledger_proved,
        "endpoint_strip_multiplicity_bound_proved": endpoint_multiplicity_proved,
        "microscopic_thin_side_packet_mass_absorption_proved": microscopic_absorbed,
        "thin_dyadic_packet_mass_absorption_proved": thin_branch_absorbed,
        "burgess_pointwise_input_still_open": burgess_still_open,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ENDPOINT_ATOM,
        "reduced_internal_atom": LEDGER_ATOM,
        "parallel_required_target": BURGESS_ATOM,
        "definitions": definitions,
        "analytic_reduction": analytic_reduction,
        "obstruction": obstruction,
        "geometric_target": geometric_target,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "微薄边分支的解析部分已被压到底：对最短边做 Plancherel 后，"
            "`H_min<P^kappa` 的所有包贡献由四个带权短边和控制，形式为 "
            "`sum_{H_s<T} H_s*prod_{j!=s}H_j^2`。因此剩余不再是角色和估计，"
            "而是一个精确的 Whitney/端点 strip packing 账本：必须证明微薄边 strip "
            "的带权总质量相对 Cauchy 尺度有固定幂余量。已有 bounded-overlap 不能替代它，"
            "因为 Plancherel 后短边只剩一个 `H_s` 幂。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 微薄边质量路由证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"packetwise_analytic_reduction_to_weighted_side_ledger_closed={fmt_bool(result['packetwise_analytic_reduction_to_weighted_side_ledger_closed'])}",
        f"endpoint_strip_source_identified_from_rectangularization={fmt_bool(result['endpoint_strip_source_identified_from_rectangularization'])}",
        f"raw_bounded_overlap_insufficient={fmt_bool(result['raw_bounded_overlap_insufficient'])}",
        f"microscopic_side_whitney_packing_mass_ledger_proved={fmt_bool(result['microscopic_side_whitney_packing_mass_ledger_proved'])}",
        f"endpoint_strip_multiplicity_bound_proved={fmt_bool(result['endpoint_strip_multiplicity_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 定义",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["definitions"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. 解析归约",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["analytic_reduction"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 3. 不能闭合的原因",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["obstruction"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 4. 下一个最窄几何输入",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["geometric_target"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "审稿边界：本证书只关闭微薄边的解析归约和精确账本定位；没有证明端点 strip 重数账本，",
            "没有内部化 Burgess 点态输入，也不声明行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 和 Markdown 证书。"""
    MONO.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
