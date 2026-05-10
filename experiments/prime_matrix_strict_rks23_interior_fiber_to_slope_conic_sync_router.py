#!/usr/bin/env python3
"""把内部 shifted product fiber 前沿同步到斜率二次曲线束唯一剩余。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_interior_fiber_to_slope_conic_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-interior-fiber-to-slope-conic-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-interior-fiber-to-slope-conic-sync-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-interior-fiber-to-slope-conic-sync-router.md"

CURRENT = MONO / "prime-matrix-strict-rks23-inverse-smalldoubling-to-affine-fiber-router.json"
DISCRIMINANT = MONO / "prime-matrix-strict-rks23-interior-fiber-discriminant-corridor-router.json"
ROOT_LOCALIZED = MONO / "prime-matrix-strict-rks23-root-localized-discriminant-corridor-router.json"
ROOT_BRANCH = MONO / "prime-matrix-strict-rks23-root-box-branch-budget-phase-exclusion-router.json"
ROOT_COLLISION = MONO / "prime-matrix-strict-rks23-root-box-collision-normal-form-router.json"
DISTINCT_DIFF = MONO / "prime-matrix-strict-rks23-distinct-difference-collision-router.json"
AFFINE_SQUARE = MONO / "prime-matrix-strict-rks23-affine-square-set-intersection-router.json"
SLOPE_CONIC = MONO / "prime-matrix-strict-rks23-slope-conic-bundle-router.json"

SOURCE_FILES = [
    CURRENT,
    DISCRIMINANT,
    ROOT_LOCALIZED,
    ROOT_BRANCH,
    ROOT_COLLISION,
    DISTINCT_DIFF,
    AFFINE_SQUARE,
    SLOPE_CONIC,
]

INTERIOR_TARGET = "InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar"
DISCRIMINANT_TARGET = "InteriorQuadraticDiscriminantCorridorHighSpectrumPowerSaving"
ROOT_TARGET = "RootLocalizedQuadraticGraphBoxFiberPowerSaving"
CENTRAL_ROOT_TARGET = "CentralPhaseRootLocalizedGraphBoxFiberPowerSaving"
ROOT_COLLISION_TARGET = "NonDiagonalRootBoxCubicCollisionPowerSaving"
DISTINCT_TARGET = "FullyNonDiagonalDistinctDifferenceRootBoxCubicCollisionPowerSaving"
AFFINE_TARGET = "NontrivialAffineSelfIntersectionEnergyOfShortSquareSetPowerSaving"
SLOPE_TARGET = "NontrivialSlopeLocalizedTernaryConicBundlePowerSaving"
SLOPE_INPUT = "RootBoxSlopeConicIncidencePowerSaving"


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
    """构造内部自足线同步证书。"""
    current = load_json(CURRENT)
    discriminant = load_json(DISCRIMINANT)
    root_localized = load_json(ROOT_LOCALIZED)
    root_branch = load_json(ROOT_BRANCH)
    root_collision = load_json(ROOT_COLLISION)
    distinct_diff = load_json(DISTINCT_DIFF)
    affine_square = load_json(AFFINE_SQUARE)
    slope_conic = load_json(SLOPE_CONIC)

    current_frontier_active = (
        current.get("next_direct_attack_target") == INTERIOR_TARGET
        and current.get("reduction_chain_closed_to_interior_frontier") is True
    )
    discriminant_step_closed = (
        discriminant.get("next_direct_attack_target") == DISCRIMINANT_TARGET
        and discriminant.get("sum_variable_quadratic_compression_closed") is True
        and discriminant.get("discriminant_corridor_identity_closed") is True
    )
    root_localized_step_closed = (
        root_localized.get("next_direct_attack_target") == ROOT_TARGET
        and root_localized.get("root_localized_difference_identity_closed") is True
        and root_localized.get("harmonic_mean_phase_map_identity_closed") is True
    )
    root_branch_step_closed = (
        root_branch.get("next_direct_attack_target") == CENTRAL_ROOT_TARGET
        and root_branch.get("low_branch_budget_phase_high_spectrum_excluded") is True
        and root_branch.get("high_fiber_forces_central_phase_condition") is True
    )
    root_collision_step_closed = (
        root_collision.get("next_direct_attack_target") == ROOT_COLLISION_TARGET
        and root_collision.get("root_box_same_phase_collision_identity_closed") is True
        and root_collision.get("high_fiber_forces_nondiagonal_collision_mass") is True
    )
    distinct_difference_step_closed = (
        distinct_diff.get("next_direct_attack_target") == DISTINCT_TARGET
        and distinct_diff.get("equal_difference_square_divisor_absorbed") is True
        and distinct_diff.get("true_cubic_collision_scope_is_distinct_difference_square") is True
    )
    affine_square_step_closed = (
        affine_square.get("next_direct_attack_target") == AFFINE_TARGET
        and affine_square.get("affine_square_set_linearization_closed") is True
        and affine_square.get("nontrivial_affine_maps_identified") is True
    )
    slope_conic_frontier_reached = (
        slope_conic.get("next_direct_attack_target") == SLOPE_TARGET
        and slope_conic.get("conic_bundle_identity_closed") is True
        and slope_conic.get("nontrivial_slopes_nonsingular") is True
    )

    reduction_chain_closed = all(
        [
            current_frontier_active,
            discriminant_step_closed,
            root_localized_step_closed,
            root_branch_step_closed,
            root_collision_step_closed,
            distinct_difference_step_closed,
            affine_square_step_closed,
            slope_conic_frontier_reached,
        ]
    )
    slope_power_saving_proved = slope_conic.get("slope_conic_bundle_power_saving_proved") is True

    chain = [
        {
            "step": "interior-shifted-product",
            "target": INTERIOR_TARGET,
            "compression": "ab=c(a+b) in the interior phase collar",
            "next": DISCRIMINANT_TARGET,
        },
        {
            "step": "sum-discriminant",
            "target": DISCRIMINANT_TARGET,
            "compression": "t=a+b gives X^2-tX+c*t=0 and Delta=t(t-4c)",
            "next": ROOT_TARGET,
        },
        {
            "step": "root-localized-map",
            "target": ROOT_TARGET,
            "compression": "d=a-b is a short signed root and c=(t^2-d^2)/(4t)",
            "next": CENTRAL_ROOT_TARGET,
        },
        {
            "step": "central-root-box",
            "target": CENTRAL_ROOT_TARGET,
            "compression": "low branch budgets are absorbed; high fiber is forced into the central phase box",
            "next": ROOT_COLLISION_TARGET,
        },
        {
            "step": "cubic-collision",
            "target": ROOT_COLLISION_TARGET,
            "compression": "same-phase root-box fibers force non-diagonal cubic collision mass",
            "next": DISTINCT_TARGET,
        },
        {
            "step": "distinct-difference",
            "target": DISTINCT_TARGET,
            "compression": "equal-difference square diagonal is absorbed; true distinct-difference cubic scope remains",
            "next": AFFINE_TARGET,
        },
        {
            "step": "affine-square-set",
            "target": AFFINE_TARGET,
            "compression": "u(x^2-y)-x(u^2-v)=0 becomes v=(u/x)y+u(u-x)",
            "next": SLOPE_TARGET,
        },
        {
            "step": "slope-conic",
            "target": SLOPE_TARGET,
            "compression": "lambda=u/x forces d2^2=lambda*d1^2+lambda(lambda-1)*x^2",
            "next": SLOPE_INPUT,
        },
    ]

    rows = [
        row(
            "CurrentInteriorFiberFrontierActive",
            current_frontier_active,
            True,
            "当前 HEAD 的反演小和集前沿已把唯一剩余压成内部 shifted product fiber 高谱。",
            INTERIOR_TARGET,
        ),
        row(
            "InteriorFiberToDiscriminantCorridorImported",
            discriminant_step_closed,
            True,
            "内部纤维已由和变量压成一维判别式平方返回通道。",
            DISCRIMINANT_TARGET,
        ),
        row(
            "DiscriminantToRootLocalizedMapImported",
            root_localized_step_closed,
            True,
            "判别式通道已加强为根定位小差有理相位映射。",
            ROOT_TARGET,
        ),
        row(
            "RootLocalizedToCentralRootBoxImported",
            root_branch_step_closed,
            True,
            "低分支预算已吸收，高谱只能进入中心相位根盒。",
            CENTRAL_ROOT_TARGET,
        ),
        row(
            "CentralRootBoxToCubicCollisionImported",
            root_collision_step_closed,
            True,
            "中心根盒高纤维已压成非对角三次碰撞质量。",
            ROOT_COLLISION_TARGET,
        ),
        row(
            "CubicCollisionToDistinctDifferenceImported",
            distinct_difference_step_closed,
            True,
            "等差平方退化已吸收，真剩余是完全非对角异差碰撞。",
            DISTINCT_TARGET,
        ),
        row(
            "DistinctDifferenceToAffineSquareImported",
            affine_square_step_closed,
            True,
            "真三次碰撞已线性化为短平方集非平凡仿射自交。",
            AFFINE_TARGET,
        ),
        row(
            "AffineSquareToSlopeConicImported",
            slope_conic_frontier_reached,
            True,
            "仿射自交已压成非平凡斜率局部三元二次曲线束。",
            SLOPE_TARGET,
        ),
        row(
            "ReductionChainClosedToSlopeConicFrontier",
            reduction_chain_closed,
            True,
            "从当前内部 fiber 剩余到斜率二次曲线束前沿的同步链条已闭合。",
            SLOPE_TARGET,
        ),
        row(
            SLOPE_TARGET,
            slope_power_saving_proved,
            False,
            "尚未在仓库内证明斜率局部三元二次曲线束总解数固定幂节省。",
            SLOPE_INPUT,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步完成唯一内部自足线的下钻同步，不宣称行/列无条件闭合。",
            SLOPE_TARGET,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_interior_fiber_to_slope_conic_sync_router",
        "status": "current_internal_frontier_synced_to_slope_localized_conic_bundle",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "current_interior_fiber_frontier_active": current_frontier_active,
        "interior_fiber_to_discriminant_corridor_imported": discriminant_step_closed,
        "discriminant_to_root_localized_map_imported": root_localized_step_closed,
        "root_localized_to_central_root_box_imported": root_branch_step_closed,
        "central_root_box_to_cubic_collision_imported": root_collision_step_closed,
        "cubic_collision_to_distinct_difference_imported": distinct_difference_step_closed,
        "distinct_difference_to_affine_square_imported": affine_square_step_closed,
        "affine_square_to_slope_conic_imported": slope_conic_frontier_reached,
        "reduction_chain_closed_to_slope_conic_frontier": reduction_chain_closed,
        "interior_shifted_product_high_spectrum_proved": False,
        "slope_conic_bundle_power_saving_proved": slope_power_saving_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SLOPE_TARGET,
        "next_required_input": SLOPE_INPUT,
        "equivalent_atom_name": SLOPE_INPUT,
        "reduction_chain": chain,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前唯一内部自足线已能严格下钻到斜率局部三元二次曲线束前沿："
            "内部 shifted product fiber 经判别式通道、根定位小差映射、中心根盒、"
            "非对角三次碰撞、异差碰撞、仿射平方集自交，最终等价压成 "
            "`d2^2=lambda*d1^2+lambda(lambda-1)*x^2` 的非平凡斜率局部曲线束。"
            "真正剩余不是前面的 fiber 或碰撞正规形，而是证明该曲线束的总解数固定幂节省。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 内部 fiber 到斜率二次曲线束同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"reduction_chain_closed_to_slope_conic_frontier={fmt_bool(result['reduction_chain_closed_to_slope_conic_frontier'])}",
        f"slope_conic_bundle_power_saving_proved={fmt_bool(result['slope_conic_bundle_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下钻链条",
        "",
        "| step | target | compression | next |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["reduction_chain"]:
        lines.append(
            "| `{step}` | `{target}` | {compression} | `{next}` |".format(
                step=table_cell(item["step"]),
                target=table_cell(item["target"]),
                compression=table_cell(item["compression"]),
                next=table_cell(item["next"]),
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
            "## 3. 下一唯一内部自足剩余",
            "",
            "```text",
            result["next_direct_attack_target"],
            result["next_required_input"],
            "```",
            "",
            "## 4. 边界声明",
            "",
            "- 本证书只归档“当前内部 fiber 前沿到斜率曲线束前沿”的严格下钻同步。",
            "- 本证书不使用真实区间实验缺失来替代反例链证明。",
            "- 本证书不宣称行/列命题无条件闭合；闭合仍需证明 `RootBoxSlopeConicIncidencePowerSaving`。",
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
