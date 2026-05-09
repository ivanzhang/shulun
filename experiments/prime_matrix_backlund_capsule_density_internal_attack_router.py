#!/usr/bin/env python3
"""Prime Matrix Backlund 胶囊密度内部攻坚路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_capsule_density_internal_attack_router.py

输出：
  docs/monograph/prime-matrix-backlund-capsule-density-internal-attack-router.json
  docs/monograph/prime-matrix-backlund-capsule-density-internal-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_CAPSULE = MONO / "prime-matrix-backlund-capsule-density-relaxation-router.json"
DEFAULT_JENSEN = MONO / "prime-matrix-b3-backlund-independent-jensen-router.json"
DEFAULT_C16 = MONO / "prime-matrix-b3-jensen-c16-aggregation-router.json"
DEFAULT_CENTER = MONO / "prime-matrix-b3-jensen-center-anchor-aggregation-router.json"
DEFAULT_SPIKE = MONO / "prime-matrix-b3-backlund-spike-exclusion-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-capsule-density-internal-attack-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-capsule-density-internal-attack-router.md"

CAPSULE_DENSITY = "BacklundIndependentCapsuleZeroDensityCoefficientLedger"
SCALE_JENSEN = "BacklundScaleSensitiveJensenCapsuleDensityLedger"
CAPSULE_COVER = "BacklundNearZeroCapsuleCoverGeometryClosed"
NO_RVM_SCALE = "BacklundNoRVMScaleSensitiveDensityDisciplineClosed"
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


def comparison(constants: dict[str, float]) -> dict[str, float]:
    """比较胶囊目标和现有 C16 粗计数。"""
    target = constants["capsule_target_zero_coefficient"]
    c16 = 16.0
    return {
        "target_zero_coefficient": target,
        "c16_zero_coefficient": c16,
        "coefficient_overshoot_factor": c16 / target,
        "target_jump_cost": constants["jump_cost_at_capsule_target"],
        "c16_jump_cost": constants["jensen_c16_jump_cost"],
        "cost_overshoot_factor": constants["jensen_c16_jump_cost"] / constants["jump_cost_at_capsule_target"],
        "cost_slack": constants["cost_slack"],
    }


def route_table() -> list[dict[str, str]]:
    """胶囊密度的候选内部路线。"""
    return [
        {
            "route": "RVMLocalDensity",
            "verdict": "blocked_by_circularity",
            "reason": "RVM 局部计数需要 Backlund/arg zeta 端点控制；当前正是在证明该控制。",
        },
        {
            "route": "FixedRadiusJensenC16",
            "verdict": "too_coarse",
            "reason": "C16 没有胶囊高度 A 的小因子，跳变成本约 50.265，远超 5/64。",
        },
        {
            "route": "ScaleSensitiveJensenCapsule",
            "verdict": "next_internal_atom",
            "reason": "需要 Jensen/xi 圆周平均保留尺度 A 的 Gamma 主项相消和 zeta 平均控制。",
        },
    ]


def build_rows(
    capsule: dict[str, Any],
    jensen: dict[str, Any],
    c16_doc: dict[str, Any],
    center: dict[str, Any],
    spike: dict[str, Any],
    comp: dict[str, float],
) -> list[dict[str, Any]]:
    """生成胶囊密度内部攻坚判定表。"""
    active = capsule.get("strict_self_contained_unique_remaining") == CAPSULE_DENSITY
    guard = (
        capsule.get("counterexample_assumption_only") is True
        and capsule.get("empirical_absence_not_used") is True
        and capsule.get("hypothetical_chain_only") is True
    )
    jensen_formula = "JensenDiskFormulaClosed" in jensen.get("closed_gates", [])
    center_symbolic = "IndependentJensenCenterAnchorClosedSymbolic" in center.get("closed_gates", [])
    c16_reduced = c16_doc.get("backlund_independent_jensen_c16_aggregation_reduced") is True
    no_rvm = "NoRVMCircularityDisciplineClosed" in spike.get("closed_gates", [])
    c16_too_coarse = comp["c16_jump_cost"] > capsule.get("constants", {}).get("stability_margin", 0.0)
    return [
        row(
            "CapsuleDensityGateActive",
            active,
            True,
            "上一层已把零系数目标松弛为独立胶囊密度目标。",
            CAPSULE_DENSITY,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的解析计数，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            CAPSULE_COVER,
            True,
            True,
            "eta 邻域沿 H 窗口扫出半高 A=eta+H 的胶囊；几何覆盖本身无剩余。",
            SCALE_JENSEN,
        ),
        row(
            NO_RVM_SCALE,
            no_rvm,
            True,
            "胶囊密度不能直接调用待证 Backlund 后推出的 RVM/CN16。",
            SCALE_JENSEN,
        ),
        row(
            "JensenFormalLayerAvailable",
            jensen_formula,
            True,
            "Jensen 公式形式层可用，可作为尺度敏感计数的唯一非循环候选工具。",
            SCALE_JENSEN,
        ),
        row(
            "CenterAnchorSymbolicAvailable",
            center_symbolic,
            True,
            "xi 圆心 anchor 已有符号有限常数，但还没有尺度 A 的数值密度聚合。",
            SCALE_JENSEN,
        ),
        row(
            "FixedC16RouteRejectedForCapsule",
            c16_reduced and c16_too_coarse,
            True,
            "固定半径 C16 计数比胶囊目标粗约 780 倍，不能支付跳变预算。",
            SCALE_JENSEN,
        ),
        row(
            SCALE_JENSEN,
            False,
            False,
            "仍需证明 Jensen 胶囊计数保留 A=33/512 的尺度小因子，且不借用 Backlund/RVM。",
            f"{SCALE_JENSEN} OR {EXTERNAL_ATOM}",
        ),
        row(
            CAPSULE_DENSITY,
            False,
            False,
            "胶囊密度目标已压成尺度敏感 Jensen 胶囊计数。",
            SCALE_JENSEN,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行胶囊密度内部攻坚。"""
    capsule = load_json(paths["capsule"])
    jensen = load_json(paths["jensen"])
    c16_doc = load_json(paths["c16"])
    center = load_json(paths["center"])
    spike = load_json(paths["spike"])
    comp = comparison(capsule["constants"])
    rows = build_rows(capsule, jensen, c16_doc, center, spike, comp)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_capsule_density_internal_attack_router",
        "status": "backlund_capsule_density_reduced_to_scale_sensitive_jensen_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "capsule_density_reduction_closed": True,
        "scale_sensitive_jensen_capsule_density_closed": False,
        "row_column_self_contained_closed": False,
        "comparison": comp,
        "route_table": route_table(),
        "strict_self_contained_unique_remaining": SCALE_JENSEN,
        "parent_remaining": CAPSULE_DENSITY,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "胶囊密度目标不能由现有固定半径 Jensen C16 粗计数关闭，也不能直接调用 RVM。"
            "C16 跳变成本约为胶囊目标成本的 780 倍。"
            "因此当前真正最窄的内部目标是 `BacklundScaleSensitiveJensenCapsuleDensityLedger`："
            "必须在 Jensen/xi 平均中保留胶囊高度 A=33/512 的尺度小因子，同时保持 Gamma 主项相消与 zeta 平均控制。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    comp = result["comparison"]
    lines = [
        "# Prime Matrix Backlund 胶囊密度内部攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"capsule_density_reduction_closed={fmt_bool(result['capsule_density_reduction_closed'])}",
        (
            "scale_sensitive_jensen_capsule_density_closed="
            f"{fmt_bool(result['scale_sensitive_jensen_capsule_density_closed'])}"
        ),
        f"strict_self_contained_unique_remaining={result['strict_self_contained_unique_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. C16 与胶囊目标对比",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| capsule target zero coefficient | `{comp['target_zero_coefficient']:.12f}` |",
        f"| fixed Jensen C16 coefficient | `{comp['c16_zero_coefficient']:.12f}` |",
        f"| coefficient overshoot factor | `{comp['coefficient_overshoot_factor']:.12f}` |",
        f"| capsule target jump cost | `{comp['target_jump_cost']:.12f}` |",
        f"| fixed C16 jump cost | `{comp['c16_jump_cost']:.12f}` |",
        f"| cost overshoot factor | `{comp['cost_overshoot_factor']:.12f}` |",
        f"| remaining cost slack at capsule target | `{comp['cost_slack']:.12f}` |",
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
            "判定：胶囊密度目标已压成尺度敏感 Jensen 计数；尚未闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capsule-json", type=Path, default=DEFAULT_CAPSULE)
    parser.add_argument("--jensen-json", type=Path, default=DEFAULT_JENSEN)
    parser.add_argument("--c16-json", type=Path, default=DEFAULT_C16)
    parser.add_argument("--center-json", type=Path, default=DEFAULT_CENTER)
    parser.add_argument("--spike-json", type=Path, default=DEFAULT_SPIKE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "capsule": args.capsule_json,
        "jensen": args.jensen_json,
        "c16": args.c16_json,
        "center": args.center_json,
        "spike": args.spike_json,
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
