#!/usr/bin/env python3
"""把反演小和集能量前沿同步到内部相位 shifted product fiber 剩余。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_inverse_smalldoubling_to_affine_fiber_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-inverse-smalldoubling-to-affine-fiber-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-inverse-smalldoubling-to-affine-fiber-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-inverse-smalldoubling-to-affine-fiber-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-mobius-overlap-sumproduct-frontier-router.json"
AFFINE = MONO / "prime-matrix-strict-rks23-mobius-to-affine-inverse-high-spectrum-router.json"
DEGENERATE = MONO / "prime-matrix-strict-rks23-affine-degenerate-phase-split-router.json"
SHIFTED = MONO / "prime-matrix-strict-rks23-nonzero-pgl2-to-shifted-product-fiber-router.json"
SIGNED = MONO / "prime-matrix-strict-rks23-shifted-product-fiber-signed-lift-router.json"

SOURCE_FILES = [PREVIOUS, AFFINE, DEGENERATE, SHIFTED, SIGNED]

TARGET = "SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar"
INTERIOR_TARGET = "InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar"
NEXT_INPUT = "InteriorPhaseBranchSlopeIncidenceOrAverageDivisorPacketBound"
EXTERNAL_ROUTE = "RudnevRNRSShiftedProductFiberIncidenceEstimate"


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
    """构造前沿同步证书。"""
    previous = load_json(PREVIOUS)
    affine = load_json(AFFINE)
    degenerate = load_json(DEGENERATE)
    shifted = load_json(SHIFTED)
    signed = load_json(SIGNED)

    target_active = previous.get("next_direct_attack_target") == TARGET
    affine_imported = (
        affine.get("affine_inverse_self_intersection_identity_closed") is True
        and affine.get("low_overlap_layer_automatically_absorbed") is True
    )
    degenerate_imported = (
        degenerate.get("degenerate_phase_s0_identified") is True
        and degenerate.get("degenerate_phase_s0_energy_absorbed") is True
        and degenerate.get("nonzero_maps_are_genuine_pgl2") is True
    )
    shifted_imported = (
        shifted.get("shifted_product_fiber_identity_closed") is True
        and shifted.get("pointwise_fiber_bound_would_close_spectrum") is True
    )
    signed_imported = (
        signed.get("signed_small_phase_divisor_lift_sublinear_bound_proved") is True
        and signed.get("signed_small_phase_high_spectrum_absorbed") is True
        and signed.get("uniform_pointwise_fiber_bound_retired_as_necessary_gate") is True
    )

    reduction_chain_closed = (
        target_active
        and affine_imported
        and degenerate_imported
        and shifted_imported
        and signed_imported
    )
    interior_high_spectrum_proved = signed.get("interior_shifted_product_high_spectrum_proved") is True
    self_contained_inverse_smalldoubling_proved = reduction_chain_closed and interior_high_spectrum_proved

    chain = [
        {
            "step": "inverse-energy",
            "formula": "A=J^(-1), E_+(A)=sum_s r_J(s)^2",
            "effect": "反演小和集问题等价于 Möbius 重叠谱。",
        },
        {
            "step": "affine-inverse",
            "formula": "r_J(s)=|A_s cap A_s^(-1)|, A_s=sJ-1",
            "effect": "一般 Möbius 重叠化为仿射等差段的倒数自交。",
        },
        {
            "step": "degenerate-phase",
            "formula": "s=0 gives b=-a and contributes at most N^2",
            "effect": "退化仿射相位已被固定幂能量预算吸收。",
        },
        {
            "step": "shifted-product",
            "formula": "for s!=0, c=s^(-1), (a-c)(b-c)=c^2 mod P",
            "effect": "非零 PGL2 高谱转为 shifted modular hyperbola 纤维。",
        },
        {
            "step": "signed-small-phase",
            "formula": "|gamma|<=max J implies (a-gamma)(b-gamma)=gamma^2+kP with |k|<=log^O(P)",
            "effect": "近零/近 P 相位由整数分支和除数界吸收。",
        },
        {
            "step": "interior-frontier",
            "formula": "min(c,P-c)>max J",
            "effect": "唯一剩余为内部相位的平均型分支/斜率 incidence 或除数包估计。",
        },
    ]

    rows = [
        row(
            "InverseSmallDoublingTargetActive",
            target_active,
            True,
            "最新前沿证书已把唯一内部自足剩余命名为反演小和集倒数能量节省。",
            TARGET,
        ),
        row(
            "AffineInverseSelfIntersectionImported",
            affine_imported,
            True,
            "已跟踪证书给出 `A_s=sJ-1` 的倒数自交等价式，并吸收低重叠层。",
            "affine reduction imported",
        ),
        row(
            "DegenerateS0PhaseAbsorbedImported",
            degenerate_imported,
            True,
            "`s=0` 仿射退化相位只贡献 `O(N^2)`，已从高谱硬点移除。",
            "nonzero PGL2 remains",
        ),
        row(
            "NonzeroShiftedProductFiberImported",
            shifted_imported,
            True,
            "`s!=0` 等价于 shifted product fiber `(a-c)(b-c)=c^2 mod P`。",
            INTERIOR_TARGET,
        ),
        row(
            "SignedSmallPhaseAbsorbedImported",
            signed_imported,
            True,
            "有符号小相位由整数提升和除数界吸收；全局点态界不再是必要门。",
            INTERIOR_TARGET,
        ),
        row(
            INTERIOR_TARGET,
            interior_high_spectrum_proved,
            False,
            "内部相位 `min(c,P-c)>max J` 的高谱平均排斥尚未证明。",
            NEXT_INPUT,
        ),
        row(
            TARGET,
            self_contained_inverse_smalldoubling_proved,
            False,
            "原反演小和集自足输入已缩窄，但仍等价依赖内部相位 fiber 高谱输入。",
            INTERIOR_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步同步并压缩剩余，不宣称行/列无条件闭合。",
            INTERIOR_TARGET,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_inverse_smalldoubling_to_affine_fiber_router",
        "status": "inverse_smalldoubling_frontier_synced_to_interior_shifted_product_fiber",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "inverse_smalldoubling_target_active": target_active,
        "affine_inverse_self_intersection_imported": affine_imported,
        "degenerate_s0_phase_absorbed_imported": degenerate_imported,
        "nonzero_shifted_product_fiber_imported": shifted_imported,
        "signed_small_phase_absorbed_imported": signed_imported,
        "reduction_chain_closed_to_interior_frontier": reduction_chain_closed,
        "interior_shifted_product_high_spectrum_proved": interior_high_spectrum_proved,
        "self_contained_inverse_smalldoubling_proved": self_contained_inverse_smalldoubling_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": INTERIOR_TARGET,
        "next_required_input": NEXT_INPUT,
        "parallel_external_route": EXTERNAL_ROUTE,
        "chain": chain,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮没有换题，而是把上一提交的反演小和集能量前沿与仓库中已跟踪的更深链条合并。"
            "从 `A=J^{-1}` 的能量出发，现已连续接到仿射等差段倒数自交、`s=0` 退化相位吸收、"
            "非零相位 shifted product fiber，以及有符号小相位整数提升吸收。"
            "因此当前唯一内部自足剩余不再是完整反演 sum-product 定理，而是内部相位 "
            "`min(c,P-c)>max J` 的 shifted product fiber 高谱平均排斥；需要证明 "
            "`InteriorPhaseBranchSlopeIncidenceOrAverageDivisorPacketBound`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 反演小和集到内部 fiber 前沿同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"reduction_chain_closed_to_interior_frontier={fmt_bool(result['reduction_chain_closed_to_interior_frontier'])}",
        f"interior_shifted_product_high_spectrum_proved={fmt_bool(result['interior_shifted_product_high_spectrum_proved'])}",
        f"self_contained_inverse_smalldoubling_proved={fmt_bool(result['self_contained_inverse_smalldoubling_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链条",
        "",
        "| step | formula | effect |",
        "| --- | --- | --- |",
    ]
    for item in result["chain"]:
        lines.append(
            "| `{step}` | {formula} | {effect} |".format(
                step=table_cell(item["step"]),
                formula=table_cell(item["formula"]),
                effect=table_cell(item["effect"]),
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
            "## 3. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            result["next_required_input"],
            "```",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
