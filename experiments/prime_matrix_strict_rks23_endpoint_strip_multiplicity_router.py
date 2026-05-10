#!/usr/bin/env python3
"""登记 RKS2/RKS3 微薄边端点 strip 重数，并压出剩余尺度比较原子。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_endpoint_strip_multiplicity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-endpoint-strip-multiplicity-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-endpoint-strip-multiplicity-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-endpoint-strip-multiplicity-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-microscopic-thin-side-mass-router.json"
RECTANGULARIZATION = MONO / "prime-matrix-strict-rks23-product-ratio-rectangular-convolution-router.json"
SOURCE_FILES = [PREVIOUS, RECTANGULARIZATION]

TARGET = "EndpointStripMultiplicityBoundForMicroscopicProductPackets"
NEXT_ATOM = "MicroscopicEndpointStripCauchyScaleComparisonForWeightedSideMass"
LEDGER_ATOM = "MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale"
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
    """构造端点 strip 重数证书。"""
    previous = load_json(PREVIOUS)
    rectangular = load_json(RECTANGULARIZATION)

    active = (
        previous.get("next_direct_attack_target") == TARGET
        and previous.get("packetwise_analytic_reduction_to_weighted_side_ledger_closed") is True
    )
    geometry_ready = (
        rectangular.get("rotated_root_box_support_geometry_closed") is True
        and rectangular.get("dyadic_rectangularization_closed_up_to_polylog") is True
    )
    bounded_overlap_ready = rectangular.get("geometry", {}).get("bounded_overlap") is not None

    # 本步只关闭纯几何/组合重数：微薄边来自 Whitney 边界距离小，
    # 端点 strip 族有限，物理点进入 packet 的次数为 polylog。
    # 它不自动给最终质量吸收，因为还要比较三侧平方质量与 Cauchy 尺度。
    whitney_charge_closed = active and geometry_ready
    finite_strip_family_closed = active and geometry_ready
    polylog_point_multiplicity_closed = active and bounded_overlap_ready
    one_dimensional_thin_sum_closed = active and geometry_ready

    pure_multiplicity_closed = (
        whitney_charge_closed
        and finite_strip_family_closed
        and polylog_point_multiplicity_closed
        and one_dimensional_thin_sum_closed
    )

    scale_comparison_proved = False
    microscopic_side_ledger_proved = pure_multiplicity_closed and scale_comparison_proved
    thin_branch_absorbed = (
        previous.get("thin_dyadic_packet_mass_absorption_proved") is True
        or microscopic_side_ledger_proved
    )
    burgess_still_open = previous.get("burgess_pointwise_input_still_open") is True

    strip_model = {
        "ambient_cover": "rectangularization splits by signs, parity, and distance to finitely many linear strip boundaries",
        "micro_width": "T=P^kappa",
        "micro_side_event": "H_s<T for one of s=1,2,3,4",
        "charge_rule": "charge the packet to a boundary/endpoint strip of width O(T) in side s",
        "strip_family_size": "O(1) boundary families times 4 sides, with only polylog dyadic labels",
        "point_multiplicity": "imported bounded-overlap gives O(log^C P) physical packet multiplicity",
    }

    one_dimensional_sum = {
        "dyadic_scales": "H=1,2,4,...,<T",
        "cells_in_width_T_strip_at_scale_H": "O(T/H+1)",
        "weighted_sum_per_scale": "O(T+H)",
        "summed_over_scales": "O(T log P)",
        "interpretation": "Plancherel leaves one H_s power; summing short-side cells inside endpoint strips costs T*polylog, not T^2",
    }

    weighted_mass_bound = {
        "previous_packet_bound": "L(Q)<=H_s*prod_{j!=s}H_j^2",
        "after_strip_multiplicity": (
            "sum_{Q:H_s<T} L(Q) <= P^o(1) * T * "
            "TripleSideSquareMass_s(endpoint-compatible packets)"
        ),
        "triple_side_square_mass": "sum over compatible packets of prod_{j!=s}H_j^2 after side-s strip charge",
        "required_final_comparison": "P^o(1)*T*TripleSideSquareMass_s <= CauchyScale*P^(-eta)",
        "why_not_automatic": "the existing corpus has not bounded the endpoint-compatible triple-side square mass against the Cauchy scale",
    }

    next_atom = {
        "name": NEXT_ATOM,
        "input_statement": (
            "for every side s and micro width T=P^kappa, the endpoint-compatible triple-side square mass "
            "satisfies T*TripleSideSquareMass_s <= CauchyScale*P^(-eta-o(1))"
        ),
        "what_would_close": "combined with this file, it closes MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale",
        "remaining_danger": "a dense family of endpoint-compatible packets with large three-side square mass can still saturate the Cauchy scale",
        "not_a_theorem_switch": "same RKS2/RKS3 thin-packet mass absorption target is preserved",
    }

    rows = [
        row(
            "EndpointStripMultiplicityAtomActive",
            active,
            True,
            "上一证书已把微薄边剩余压到端点/边界 strip 重数与尺度余量。",
            TARGET,
        ),
        row(
            "WhitneyMicroSideChargeClosed",
            whitney_charge_closed,
            True,
            "在按边界距离拆分的 Whitney 矩形化中，`H_s<T` 的短边 packet 可充到宽 `O(T)` 的端点/边界 strip。",
            "pure multiplicity",
        ),
        row(
            "FiniteEndpointStripFamilyClosed",
            finite_strip_family_closed,
            True,
            "根盒边界族、符号和奇偶类数量为固定常数；dyadic 标签只给 polylog 损失。",
            "pure multiplicity",
        ),
        row(
            "PolylogPacketPointMultiplicityClosed",
            polylog_point_multiplicity_closed,
            True,
            "已有矩形化 bounded-overlap 登记每个物理点只进入 `O(log^C P)` 个 packet。",
            "pure multiplicity",
        ),
        row(
            "OneDimensionalThinSideWeightedSumClosed",
            one_dimensional_thin_sum_closed,
            True,
            "宽 `T` strip 内按 dyadic 长度求和，`sum_{H<T} H*(T/H+1)=O(T log P)`。",
            NEXT_ATOM,
        ),
        row(
            "EndpointStripPureMultiplicityClosed",
            pure_multiplicity_closed,
            pure_multiplicity_closed,
            "纯重数账本闭合：微薄边总量只剩 `T` 乘三侧平方质量的 Cauchy 尺度比较。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            scale_comparison_proved,
            scale_comparison_proved,
            "仓库内尚未证明端点兼容三侧平方质量乘 `T` 后仍比 Cauchy 尺度小固定幂。",
            NEXT_ATOM,
        ),
        row(
            LEDGER_ATOM,
            microscopic_side_ledger_proved,
            microscopic_side_ledger_proved,
            "微薄边总质量吸收需要纯重数账本和最终尺度比较同时成立。",
            NEXT_ATOM,
        ),
        row(
            "ThinDyadicPacketMassAbsorptionProved",
            thin_branch_absorbed,
            thin_branch_absorbed,
            "薄包分支仍缺微薄边尺度比较，因此不能声明薄包总吸收。",
            NEXT_ATOM,
        ),
        row(
            "BurgessPointwiseInputStillOpen",
            burgess_still_open,
            False,
            "大包分支的 Burgess 点态输入仍是独立开放项。",
            BURGESS_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只关闭微薄边端点 strip 纯重数账本，不关闭行/列无条件定理。",
            f"{NEXT_ATOM} AND {BURGESS_ATOM}",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_endpoint_strip_multiplicity_router",
        "status": "endpoint_strip_pure_multiplicity_closed_cauchy_scale_comparison_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "endpoint_strip_multiplicity_atom_active": active,
        "whitney_micro_side_charge_closed": whitney_charge_closed,
        "finite_endpoint_strip_family_closed": finite_strip_family_closed,
        "polylog_packet_point_multiplicity_closed": polylog_point_multiplicity_closed,
        "one_dimensional_thin_side_weighted_sum_closed": one_dimensional_thin_sum_closed,
        "endpoint_strip_pure_multiplicity_closed": pure_multiplicity_closed,
        "microscopic_endpoint_strip_cauchy_scale_comparison_proved": scale_comparison_proved,
        "microscopic_side_whitney_packing_mass_ledger_proved": microscopic_side_ledger_proved,
        "thin_dyadic_packet_mass_absorption_proved": thin_branch_absorbed,
        "burgess_pointwise_input_still_open": burgess_still_open,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "reduced_internal_atom": LEDGER_ATOM,
        "parallel_required_target": BURGESS_ATOM,
        "strip_model": strip_model,
        "one_dimensional_sum": one_dimensional_sum,
        "weighted_mass_bound": weighted_mass_bound,
        "next_atom": next_atom,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "端点 strip 的纯重数部分已被分离并登记：在已有 Whitney/矩形化拆包中，"
            "`H_s<T` 的微薄边 packet 可充到宽 `O(T)` 的有限端点/边界 strip；"
            "每个物理点只有 polylog 重数，且一维短边带权和只花 `O(T log P)`。"
            "因此微薄边剩余进一步压成一个更窄的尺度比较："
            "`P^o(1)*T*TripleSideSquareMass_s <= CauchyScale*P^-eta`。"
            "当前材料尚未证明该三侧平方质量比较，所以仍不能声明薄包或行/列命题闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 端点 strip 重数证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"endpoint_strip_pure_multiplicity_closed={fmt_bool(result['endpoint_strip_pure_multiplicity_closed'])}",
        f"one_dimensional_thin_side_weighted_sum_closed={fmt_bool(result['one_dimensional_thin_side_weighted_sum_closed'])}",
        f"microscopic_endpoint_strip_cauchy_scale_comparison_proved={fmt_bool(result['microscopic_endpoint_strip_cauchy_scale_comparison_proved'])}",
        f"microscopic_side_whitney_packing_mass_ledger_proved={fmt_bool(result['microscopic_side_whitney_packing_mass_ledger_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Strip 模型",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["strip_model"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. 一维短边求和",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["one_dimensional_sum"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 3. 带权质量界",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["weighted_mass_bound"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 4. 新最窄输入",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["next_atom"].items():
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
            "审稿边界：本证书只关闭端点 strip 纯重数和一维短边带权求和；",
            "没有证明三侧平方质量的 Cauchy 尺度比较，没有内部化 Burgess 输入，也不声明行/列命题无条件闭合。",
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
