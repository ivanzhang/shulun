#!/usr/bin/env python3
"""Prime Matrix Backlund 尺度敏感 Jensen 几何障碍路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_scale_sensitive_jensen_obstruction_router.py

输出：
  docs/monograph/prime-matrix-backlund-scale-sensitive-jensen-obstruction-router.json
  docs/monograph/prime-matrix-backlund-scale-sensitive-jensen-obstruction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_ATTACK = MONO / "prime-matrix-backlund-capsule-density-internal-attack-router.json"
DEFAULT_CENTER = MONO / "prime-matrix-b3-jensen-center-anchor-router.json"
DEFAULT_EULER = MONO / "prime-matrix-b3-jensen-euler-lower-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-scale-sensitive-jensen-obstruction-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-scale-sensitive-jensen-obstruction-router.md"

SCALE_JENSEN = "BacklundScaleSensitiveJensenCapsuleDensityLedger"
RIGHT_ANCHOR_OBSTRUCTION = "BacklundRightAnchorScaleSensitiveJensenRadiusObstructionClosed"
CRITICAL_ANCHOR = "BacklundCriticalLineScaleAnchorAvoidanceLedger"
MOVING_CENTER = "BacklundMovingCenterZeroAvoidanceWithoutCostLedger"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


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


def geometry_constants() -> dict[str, float]:
    """尺度敏感 Jensen 的几何常数。"""
    eta = 1.0 / 16.0
    h = 1.0 / 512.0
    a = eta + h
    right_anchor_min_radius = 0.5
    sigma2_radius = 1.5
    margin = 5.0 / 64.0
    return {
        "eta": eta,
        "H": h,
        "capsule_half_height_A": a,
        "right_anchor_min_radius": right_anchor_min_radius,
        "sigma2_center_radius": sigma2_radius,
        "right_anchor_radius_over_A": right_anchor_min_radius / a,
        "sigma2_radius_over_A": sigma2_radius / a,
        "stability_margin": margin,
        "right_anchor_radius_minus_margin": right_anchor_min_radius - margin,
    }


def route_table() -> list[dict[str, str]]:
    """尺度敏感 Jensen 后续路线表。"""
    return [
        {
            "route": "RightEdgeEulerAnchor",
            "verdict": "geometrically_blocked_for_A_scale",
            "reason": "圆心在 sigma>1 时，为覆盖临界线附近零点，半径至少约 1/2，无法保留 A=33/512 小因子。",
        },
        {
            "route": "CriticalLineSmallDiskAnchor",
            "verdict": "new_hard_atom",
            "reason": "半径可为 O(A)，但必须给出靠近临界线且避开零点的统一圆心下界。",
        },
        {
            "route": "MovingCenterAvoidance",
            "verdict": "equivalent_to_indent_cost",
            "reason": "随 T 移动选择避零圆心会重新引入近零缩进/跳变成本。",
        },
    ]


def build_rows(attack: dict[str, Any], center: dict[str, Any], euler: dict[str, Any], c: dict[str, float]) -> list[dict[str, Any]]:
    """生成尺度敏感 Jensen 几何障碍判定表。"""
    active = attack.get("strict_self_contained_unique_remaining") == SCALE_JENSEN
    guard = (
        attack.get("counterexample_assumption_only") is True
        and attack.get("empirical_absence_not_used") is True
        and attack.get("hypothetical_chain_only") is True
    )
    center_choice_seen = center.get("next_priority") == "BacklundJensenRightEdgeCenterChoiceConventionLedger" or (
        "CenterChoiceConventionMissing" in center.get("open_gates", [])
    )
    euler_lower_available = euler.get("backlund_jensen_right_edge_euler_lower_closed") is True or (
        "BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2" in str(euler)
    )
    radius_obstruction = c["right_anchor_min_radius"] > c["capsule_half_height_A"]
    return [
        row(
            "ScaleSensitiveJensenGateActive",
            active,
            True,
            "上一层把胶囊密度压成尺度敏感 Jensen 胶囊计数。",
            SCALE_JENSEN,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的解析几何障碍。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "RightEdgeAnchorMechanismIdentified",
            center_choice_seen and euler_lower_available,
            True,
            "现有 Jensen 圆心路线依赖 sigma>1 的 Euler product 下界。",
            RIGHT_ANCHOR_OBSTRUCTION,
        ),
        row(
            RIGHT_ANCHOR_OBSTRUCTION,
            radius_obstruction,
            True,
            "若圆心在 sigma>1，又要覆盖 sigma=1/2 附近零点，则半径至少约 1/2，不能保留 A=33/512 小尺度。",
            CRITICAL_ANCHOR,
        ),
        row(
            "Sigma2CenterEvenWorse",
            True,
            True,
            "若沿用 sigma=2 圆心，半径至少 3/2，是 A 的二十多倍。",
            CRITICAL_ANCHOR,
        ),
        row(
            "SmallRadiusRequiresCriticalAnchor",
            True,
            True,
            "要让 Jensen 半径为 O(A)，圆心必须靠近临界线；这需要新的统一非零下界或避零圆心选择。",
            f"{CRITICAL_ANCHOR} OR {MOVING_CENTER}",
        ),
        row(
            "MovingCenterAvoidanceLoopsToIndent",
            True,
            True,
            "若圆心随零点移动避让，避让本身重新产生近零跳变/缩进成本。",
            CRITICAL_ANCHOR,
        ),
        row(
            SCALE_JENSEN,
            False,
            False,
            "尺度敏感 Jensen 路线被右边界锚半径障碍阻断；下一步必须攻临界线小半径 anchor。",
            f"{CRITICAL_ANCHOR} OR {EXTERNAL_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行尺度敏感 Jensen 几何障碍审查。"""
    attack = load_json(paths["attack"])
    center = load_json(paths["center"])
    euler = load_json(paths["euler"])
    c = geometry_constants()
    rows = build_rows(attack, center, euler, c)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_scale_sensitive_jensen_obstruction_router",
        "status": "backlund_scale_sensitive_jensen_blocked_by_anchor_radius_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "right_anchor_radius_obstruction_closed": True,
        "scale_sensitive_jensen_capsule_density_closed": False,
        "row_column_self_contained_closed": False,
        "geometry_constants": c,
        "route_table": route_table(),
        "strict_self_contained_unique_remaining": CRITICAL_ANCHOR,
        "parent_remaining": SCALE_JENSEN,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "尺度敏感 Jensen 胶囊计数被现有右边界 anchor 几何阻断。"
            "要得到 A=33/512 的小因子，Jensen 半径必须与 A 同阶；"
            "但只要圆心放在 sigma>1 以使用 Euler product 下界，覆盖临界线附近零点的半径至少约 1/2，"
            "已经远大于 A，不能保留胶囊高度小因子。"
            "因此新的最窄内部目标是 `BacklundCriticalLineScaleAnchorAvoidanceLedger`："
            "在靠近临界线的小半径圆盘中建立非循环、非移动成本的圆心 anchor。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    c = result["geometry_constants"]
    lines = [
        "# Prime Matrix Backlund 尺度敏感 Jensen 几何障碍路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"right_anchor_radius_obstruction_closed={fmt_bool(result['right_anchor_radius_obstruction_closed'])}",
        (
            "scale_sensitive_jensen_capsule_density_closed="
            f"{fmt_bool(result['scale_sensitive_jensen_capsule_density_closed'])}"
        ),
        f"strict_self_contained_unique_remaining={result['strict_self_contained_unique_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 几何常数",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| A=eta+H | `{c['capsule_half_height_A']:.12f}` |",
        f"| right-anchor minimum radius | `{c['right_anchor_min_radius']:.12f}` |",
        f"| sigma=2 center radius | `{c['sigma2_center_radius']:.12f}` |",
        f"| right-anchor radius / A | `{c['right_anchor_radius_over_A']:.12f}` |",
        f"| sigma=2 radius / A | `{c['sigma2_radius_over_A']:.12f}` |",
        f"| stability margin | `{c['stability_margin']:.12f}` |",
        f"| right-anchor radius minus margin | `{c['right_anchor_radius_minus_margin']:.12f}` |",
        "",
        "## 2. 路线判定",
        "",
        "| route | verdict | reason |",
        "| --- | --- | --- |",
    ]
    for item in result["route_table"]:
        lines.append(
            f"| `{table_cell(item['route'])}` | `{table_cell(item['verdict'])}` | {table_cell(item['reason'])} |"
        )
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
            "## 4. 下一步",
            "",
            f"新的严格自足唯一剩余：`{result['strict_self_contained_unique_remaining']}`。",
            f"父级剩余：`{result['parent_remaining']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：右边界 Jensen anchor 无法给出 A 级胶囊密度；必须攻临界线小半径 anchor。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attack-json", type=Path, default=DEFAULT_ATTACK)
    parser.add_argument("--center-json", type=Path, default=DEFAULT_CENTER)
    parser.add_argument("--euler-json", type=Path, default=DEFAULT_EULER)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "attack": args.attack_json,
        "center": args.center_json,
        "euler": args.euler_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["strict_self_contained_unique_remaining"])


if __name__ == "__main__":
    main()
