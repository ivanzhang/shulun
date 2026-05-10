#!/usr/bin/env python3
"""吸收非对角碰撞中的同差平方退化层。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_distinct_difference_collision_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-distinct-difference-collision-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-distinct-difference-collision-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-distinct-difference-collision-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-root-box-collision-normal-form-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "NonDiagonalRootBoxCubicCollisionPowerSaving"
NEXT_ATOM = "FullyNonDiagonalDistinctDifferenceRootBoxCubicCollisionPowerSaving"
EQUAL_DSQ_ATOM = "EqualDifferenceSquareCollisionDivisorAbsorption"


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
    """构造同差平方退化层吸收证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    collision_identity = previous.get("root_box_same_phase_collision_identity_closed") is True

    # 非对角碰撞方程：
    #   t2(t1^2-d1^2)-t1(t2^2-d2^2)=0 mod P。
    # 若 d1^2=d2^2=d^2 且 t1!=t2，则化为
    #   (t1-t2)(t1*t2+d^2)=0 mod P，
    # 因此 t1*t2+d^2=lP。短盒中 l 只有 polylog 个，
    # 固定 d,l 后由除数界控制 t1,t2。
    equal_dsq_absorbed = active and collision_identity
    true_cubic_remaining = active and collision_identity

    equal_dsq = {
        "starting_collision": "t2(t1^2-d1^2)-t1(t2^2-d2^2)=0 mod P",
        "layer_condition": "t1!=t2 and d1^2=d2^2=d^2",
        "reduced_equation": "t1*t2+d^2=0 mod P",
        "integer_lift": "t1*t2+d^2=lP",
        "branch_budget": "l<=O(U^2/P)=log^O(P) in the square-root collar",
        "divisor_count": "for fixed d,l, the number of (t1,t2) is <=tau(lP-d^2)",
        "total_size": "O(N log^O(P) P^o(1))",
        "absorption": "this is far below N^(3-delta) for every fixed delta<2",
    }

    rows = [
        row(
            "NonDiagonalCollisionTargetActive",
            active,
            True,
            "上一证书已把剩余压成根定位盒的非对角三次碰撞。",
            TARGET,
        ),
        row(
            "EqualDifferenceSquareReductionClosed",
            equal_dsq_absorbed,
            True,
            "`d1^2=d2^2` 时非对角碰撞退化为 `t1*t2+d^2=0 mod P`。",
            EQUAL_DSQ_ATOM,
        ),
        row(
            "EqualDifferenceSquareDivisorAbsorbed",
            equal_dsq_absorbed,
            True,
            "整数提升后只有 `log^O(P)` 个分支，固定分支由除数界控制，总规模可吸收。",
            "absorbed",
        ),
        row(
            "TrueCubicCollisionScopeIsDistinctDifferenceSquare",
            true_cubic_remaining,
            True,
            "幸存碰撞必须同时满足 `t1!=t2` 与 `d1^2!=d2^2`。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明完全非对角、差平方不同的三次碰撞固定幂节省。",
            "DistinctDifferenceRootBoxCubicIncidencePowerSaving",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只吸收同差平方退化层，未证明真三次碰撞估计。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_distinct_difference_collision_router",
        "status": "equal_difference_square_collision_absorbed_true_cubic_distinct_difference_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "non_diagonal_collision_target_active": active,
        "equal_difference_square_reduction_closed": equal_dsq_absorbed,
        "equal_difference_square_divisor_absorbed": equal_dsq_absorbed,
        "true_cubic_collision_scope_is_distinct_difference_square": true_cubic_remaining,
        "fully_nondiagonal_distinct_difference_cubic_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "equal_difference_square_layer": equal_dsq,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "非对角碰撞中 `d1^2=d2^2` 的退化层可以自足吸收。"
            "此时碰撞式化为 `t1*t2+d^2=0 mod P`，整数提升为 `t1*t2+d^2=lP`；"
            "在平方根颈部只有 `log^O(P)` 个 `l`，固定 `d,l` 后由除数界控制。"
            "因此真正剩余进一步压成 `t1!=t2` 且 `d1^2!=d2^2` 的完全非对角三次碰撞。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    layer = result["equal_difference_square_layer"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 差平方退化碰撞吸收证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"equal_difference_square_divisor_absorbed={fmt_bool(result['equal_difference_square_divisor_absorbed'])}",
        f"true_cubic_collision_scope_is_distinct_difference_square={fmt_bool(result['true_cubic_collision_scope_is_distinct_difference_square'])}",
        f"fully_nondiagonal_distinct_difference_cubic_power_saving_proved={fmt_bool(result['fully_nondiagonal_distinct_difference_cubic_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同差平方退化层",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in layer.items():
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
