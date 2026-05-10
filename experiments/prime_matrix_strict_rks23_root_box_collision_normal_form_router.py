#!/usr/bin/env python3
"""把中央根定位盒高重数改写为同相位碰撞正规形。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_root_box_collision_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-root-box-collision-normal-form-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-root-box-collision-normal-form-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-root-box-collision-normal-form-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-root-box-branch-budget-phase-exclusion-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "CentralPhaseRootLocalizedGraphBoxFiberPowerSaving"
NEXT_ATOM = "NonDiagonalRootBoxCubicCollisionPowerSaving"
COLLISION_ATOM = "RootBoxSamePhaseCollisionEnergyNormalForm"


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
    """构造碰撞正规形证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    central_forced = previous.get("high_fiber_forces_central_phase_condition") is True

    # 根定位变量为 t=a+b, d=a-b。相位映射为
    #   Phi(t,d)=(t^2-d^2)/(4t) mod P。
    # 两点同相位等价于清分母后的三次碰撞：
    #   t2(t1^2-d1^2)-t1(t2^2-d2^2)=0 mod P。
    # t1=t2 的退化只给 d1=±d2，可由符号对称吸收。
    collision_identity_closed = active and central_forced
    diagonal_absorbed = active and central_forced
    high_fiber_to_collision_closed = active and central_forced

    normal_form = {
        "root_box_variables": "t=a+b in J+J, d=a-b with |d|<|J| and matching parity",
        "phase_map": "Phi(t,d)=(t^2-d^2)/(4t) mod P",
        "same_phase_collision": "Phi(t1,d1)=Phi(t2,d2)",
        "cleared_denominator_form": "t2(t1^2-d1^2)-t1(t2^2-d2^2)=0 mod P",
        "diagonal_t_collision": "if t1=t2 then d1^2=d2^2, hence d1=±d2 in F_P",
        "diagonal_absorption": "same-t and sign-symmetry collisions contribute only O(N^2), below every N^(3-delta) target",
        "high_fiber_implication": "a fiber of size H produces >=H(H-2) non-diagonal same-phase collisions unless it is absorbed by the diagonal layer",
        "remaining_shape": "prove power saving for non-diagonal cubic collisions in the root-localized box",
    }

    rows = [
        row(
            "CentralRootBoxTargetActive",
            active,
            True,
            "上一证书已把幸存反例压入中央相位根定位盒。",
            TARGET,
        ),
        row(
            "RootBoxSamePhaseCollisionIdentityClosed",
            collision_identity_closed,
            True,
            "同相位条件精确等价于清分母三次碰撞式。",
            COLLISION_ATOM,
        ),
        row(
            "SameTAndSignDiagonalAbsorbed",
            diagonal_absorbed,
            True,
            "`t1=t2` 只允许 `d1=±d2`，该退化层规模 `O(N^2)`。",
            "absorbed",
        ),
        row(
            "HighFiberForcesNonDiagonalCollisionMass",
            high_fiber_to_collision_closed,
            True,
            "若中央相位仍有高纤维，则必须产生大量 `t1!=t2` 的同相位碰撞。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明根定位盒中非对角三次碰撞具有固定幂节省。",
            "RootBoxCubicIncidenceOrSumProductPowerSaving",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只把剩余改写为非对角碰撞输入，没有证明该碰撞估计。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_root_box_collision_normal_form_router",
        "status": "central_root_box_high_fiber_reduced_to_nondiagonal_cubic_collision_power_saving",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "central_root_box_target_active": active,
        "root_box_same_phase_collision_identity_closed": collision_identity_closed,
        "same_t_and_sign_diagonal_absorbed": diagonal_absorbed,
        "high_fiber_forces_nondiagonal_collision_mass": high_fiber_to_collision_closed,
        "nondiagonal_root_box_cubic_collision_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "normal_form": normal_form,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "中央根定位盒的高重数可改写为同相位碰撞问题。"
            "对 `Phi(t,d)=(t^2-d^2)/(4t)`，两点同相位当且仅当 "
            "`t2(t1^2-d1^2)-t1(t2^2-d2^2)=0 mod P`。"
            "同 `t` 的退化只给 `d1=±d2`，规模为 `O(N^2)`，已低于固定幂能量目标。"
            "因此当前最窄剩余变成非对角根定位盒三次碰撞的固定幂节省。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    normal = result["normal_form"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 根定位盒碰撞正规形证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"root_box_same_phase_collision_identity_closed={fmt_bool(result['root_box_same_phase_collision_identity_closed'])}",
        f"same_t_and_sign_diagonal_absorbed={fmt_bool(result['same_t_and_sign_diagonal_absorbed'])}",
        f"nondiagonal_root_box_cubic_collision_power_saving_proved={fmt_bool(result['nondiagonal_root_box_cubic_collision_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 碰撞正规形",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in normal.items():
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
