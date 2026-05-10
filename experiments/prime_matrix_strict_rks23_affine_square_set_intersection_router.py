#!/usr/bin/env python3
"""把完全非对角三次碰撞线性化为短平方集的仿射自交。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_affine_square_set_intersection_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-affine-square-set-intersection-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-affine-square-set-intersection-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-affine-square-set-intersection-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-distinct-difference-collision-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "FullyNonDiagonalDistinctDifferenceRootBoxCubicCollisionPowerSaving"
NEXT_ATOM = "NontrivialAffineSelfIntersectionEnergyOfShortSquareSetPowerSaving"
ALT_ATOM = "RootBoxTParameterAffineSquareSetIncidencePowerSaving"


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
    """构造仿射平方集自交证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    true_scope = previous.get("true_cubic_collision_scope_is_distinct_difference_square") is True

    # 真三次碰撞：
    #   u(x^2-y)-x(u^2-v)=0，其中 x=t1,u=t2,y=d1^2,v=d2^2。
    # 对 x,u 非零且 x!=u，可写成
    #   v=(u/x)y+u(u-x) mod P。
    # 因此剩余只是短平方集 D 在一族非恒等仿射映射下的自交。
    affine_reduction_closed = active and true_scope
    multiplicity_control_closed = active and true_scope

    affine_form = {
        "variables": "x=t1, u=t2, y=d1^2, v=d2^2",
        "true_scope": "x!=u and y!=v",
        "cubic_collision": "u(x^2-y)-x(u^2-v)=0 mod P",
        "affine_square_equation": "v=(u/x)y+u(u-x) mod P",
        "slope": "lambda=u/x, and lambda!=1 in the non-diagonal t-layer",
        "translation": "mu=u(u-x)",
        "short_square_set": "D={d^2: d is an allowed root-box difference}",
        "multiplicity": "each y in D has at most two signed d-preimages, so d-multiplicity costs only an absolute factor",
        "collision_count_bound": "true cubic collisions <=4*sum_{x!=u} |D cap A_{x,u}^{-1}(D)|",
    }

    rows = [
        row(
            "FullyNonDiagonalCollisionTargetActive",
            active,
            True,
            "上一证书已把剩余压成 `t1!=t2` 且 `d1^2!=d2^2` 的真三次碰撞。",
            TARGET,
        ),
        row(
            "AffineSquareSetLinearizationClosed",
            affine_reduction_closed,
            True,
            "代入 `y=d1^2,v=d2^2` 后，碰撞式对 `y,v` 是一条非恒等仿射关系。",
            NEXT_ATOM,
        ),
        row(
            "SignedDifferenceMultiplicityControlled",
            multiplicity_control_closed,
            True,
            "`d->d^2` 在根定位盒中至多二重，转成平方值集合只损失常数。",
            "constant factor",
        ),
        row(
            "NontrivialAffineMapsIdentified",
            affine_reduction_closed,
            True,
            "`t1!=t2` 等价于斜率 `u/x!=1`，所以剩余排除了恒等仿射退化。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明短平方集在这族非平凡仿射映射下的总自交有固定幂节省。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只线性化真三次碰撞，未证明仿射平方集自交估计。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_affine_square_set_intersection_router",
        "status": "true_cubic_collision_linearized_to_nontrivial_affine_self_intersections_of_short_square_set",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "fully_nondiagonal_collision_target_active": active,
        "affine_square_set_linearization_closed": affine_reduction_closed,
        "signed_difference_multiplicity_controlled": multiplicity_control_closed,
        "nontrivial_affine_maps_identified": affine_reduction_closed,
        "nontrivial_affine_square_set_energy_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "affine_form": affine_form,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "完全非对角三次碰撞可以进一步线性化。令 `x=t1,u=t2,y=d1^2,v=d2^2`，"
            "碰撞式 `u(x^2-y)-x(u^2-v)=0` 等价于 "
            "`v=(u/x)y+u(u-x) mod P`。"
            "由于 `x!=u`，斜率非 1；由于 `d->d^2` 至多二重，差变量只造成常数损失。"
            "因此当前唯一剩余变成短平方集 `D` 在参数化非平凡仿射映射族下的总自交固定幂节省。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    affine = result["affine_form"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 仿射平方集自交前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"affine_square_set_linearization_closed={fmt_bool(result['affine_square_set_linearization_closed'])}",
        f"nontrivial_affine_square_set_energy_power_saving_proved={fmt_bool(result['nontrivial_affine_square_set_energy_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 仿射平方集正规形",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in affine.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
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
