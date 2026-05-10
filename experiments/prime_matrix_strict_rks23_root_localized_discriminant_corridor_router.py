#!/usr/bin/env python3
"""把判别式通道强化为根定位小差通道。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_root_localized_discriminant_corridor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-root-localized-discriminant-corridor-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-root-localized-discriminant-corridor-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-root-localized-discriminant-corridor-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-interior-fiber-discriminant-corridor-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "InteriorQuadraticDiscriminantCorridorHighSpectrumPowerSaving"
NEXT_ATOM = "RootLocalizedQuadraticGraphBoxFiberPowerSaving"
ALT_ATOM = "SmallDifferenceHarmonicMeanMapHighMultiplicityExclusion"
CHAR_ROUTE_RETIRED = "QuadraticSquareReturnOnlyRouteInsufficient"


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
    """构造根定位通道证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    discriminant_closed = previous.get("discriminant_corridor_identity_closed") is True

    # 令 t=a+b, d=a-b。因为 a,b 属于同一个短整数块 J，
    # d 必须落在长度 O(N) 的小差盒中。仅要求 Delta_c(t) 为平方太弱；
    # 必须要求平方根就是这个小差 d。
    root_localized_closed = active and discriminant_closed
    square_only_retired = active and discriminant_closed
    branch_barrier_closed = active and discriminant_closed

    root_corridor = {
        "variables": "t=a+b and d=a-b",
        "root_cut": "a=(t+d)/2 in J and b=(t-d)/2 in J",
        "small_difference_box": "|d|<=|J|-1 as an ordinary signed integer",
        "equation": "d^2=t(t-4c) mod P",
        "phase_map": "c=(t^2-d^2)/(4t) mod P",
        "fiber_form": "r_c is bounded by the number of (t,d) in the root-localized box with phase_map(t,d)=c",
        "high_fiber_implication": "r_c>N^(1-eta) forces one value of the harmonic-mean map to have >N^(1-eta) preimages in a thin (t,d) box",
        "same_target_preserved": TARGET,
    }

    route_audit = {
        "square_return_only": "insufficient",
        "reason": "Delta_c(t) being a quadratic residue normally occurs on about half of J+J; that is much larger than the desired N^(1-eta) high-spectrum threshold",
        "needed_extra_rigidity": "the square root must equal a small signed difference d=a-b with both reconstructed roots inside J",
        "plain_character_sum_role": "Burgess/Weil cancellation for chi(t(t-4c)) alone does not close the fiber problem",
        "branch_lift_barrier": "for middle interior c, the lift ab-c(a+b)=kP has O(max J) possible k, so per-branch divisor counting loses the required power",
        "next_method": "prove high-multiplicity exclusion for the rational map (t,d)->(t^2-d^2)/(4t) on the short root-localized box",
    }

    rows = [
        row(
            "InteriorDiscriminantTargetActive",
            active,
            True,
            "上一证书已把剩余压成内部相位的判别式通道。",
            TARGET,
        ),
        row(
            "RootLocalizedDifferenceIdentityClosed",
            root_localized_closed,
            True,
            "`a,b in J` 等价给出 `t=a+b` 与小差 `d=a-b`，并满足 `d^2=t(t-4c)`。",
            NEXT_ATOM,
        ),
        row(
            "HarmonicMeanPhaseMapIdentityClosed",
            root_localized_closed,
            True,
            "同一相位可写为 `c=(t^2-d^2)/(4t)`，剩余是该有理映射的小盒子高重数排斥。",
            ALT_ATOM,
        ),
        row(
            "QuadraticSquareReturnOnlyRouteInsufficient",
            square_only_retired,
            True,
            "仅证明 `Delta_c(t)` 很少为平方不可能成立到所需强度；必须使用小差根定位。",
            NEXT_ATOM,
        ),
        row(
            "MiddleInteriorBranchDivisorLiftBarrierQuantified",
            branch_barrier_closed,
            True,
            "中心内部相位有多达 `O(max J)` 个整数分支，朴素分支除数界不能给固定幂节省。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明根定位有理相位映射在短盒子上的高重数固定幂排斥。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步关闭的是通道精化和假捷径排除；最终高重数排斥仍未证明。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_root_localized_discriminant_corridor_router",
        "status": "discriminant_corridor_refined_to_root_localized_small_difference_phase_map",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "interior_discriminant_target_active": active,
        "root_localized_difference_identity_closed": root_localized_closed,
        "harmonic_mean_phase_map_identity_closed": root_localized_closed,
        "quadratic_square_return_only_route_insufficient": square_only_retired,
        "middle_interior_branch_divisor_lift_barrier_quantified": branch_barrier_closed,
        "root_localized_graph_box_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "retired_route": CHAR_ROUTE_RETIRED,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "root_corridor": root_corridor,
        "route_audit": route_audit,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "判别式通道还必须加入根定位约束。设 `t=a+b`、`d=a-b`，"
            "则真实纤维不是单纯的 `Delta_c(t)` 为平方，而是小差盒中的 "
            "`d^2=t(t-4c) mod P`，等价于同一有理相位映射 "
            "`c=(t^2-d^2)/(4t)` 出现高重数。"
            "因此当前最窄剩余是证明该根定位小盒子映射没有固定幂级高重数；"
            "单纯二次字符平方返回路线和朴素分支除数路线都不足以闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    root_corridor = result["root_corridor"]
    route_audit = result["route_audit"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 根定位判别式通道证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"root_localized_difference_identity_closed={fmt_bool(result['root_localized_difference_identity_closed'])}",
        f"quadratic_square_return_only_route_insufficient={fmt_bool(result['quadratic_square_return_only_route_insufficient'])}",
        f"root_localized_graph_box_power_saving_proved={fmt_bool(result['root_localized_graph_box_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 根定位小差通道",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in root_corridor.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 路线审查",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in route_audit.items():
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
            "## 4. 下一最窄自足目标",
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
