#!/usr/bin/env python3
"""Prime Matrix Backlund 近零胶囊密度松弛路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_capsule_density_relaxation_router.py

输出：
  docs/monograph/prime-matrix-backlund-capsule-density-relaxation-router.json
  docs/monograph/prime-matrix-backlund-capsule-density-relaxation-router.md
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

DEFAULT_ATOMIC = MONO / "prime-matrix-backlund-internal-proof-atomic-reduction-router.json"
DEFAULT_NEAR = MONO / "prime-matrix-b3-near-zero-indent-separation-router.json"
DEFAULT_VARIATION = MONO / "prime-matrix-b3-variation-window-scale-router.json"
DEFAULT_SPIKE = MONO / "prime-matrix-b3-backlund-spike-exclusion-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-capsule-density-relaxation-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-capsule-density-relaxation-router.md"

ZERO_COEFF = "BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger"
CAPSULE_DENSITY = "BacklundIndependentCapsuleZeroDensityCoefficientLedger"
NO_RVM = "BacklundSpikeNoRVMCircularityDisciplineClosed"
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


def constants() -> dict[str, float]:
    """胶囊密度常数。"""
    eta = 1.0 / 16.0
    h = 1.0 / 512.0
    capsule_half_height = eta + h
    margin = 5.0 / 64.0
    allowed_zero_coefficient = margin / math.pi
    target_zero_coefficient = capsule_half_height / math.pi
    return {
        "eta": eta,
        "window_length_H": h,
        "capsule_half_height_A": capsule_half_height,
        "stability_margin": margin,
        "allowed_zero_coefficient": allowed_zero_coefficient,
        "capsule_target_zero_coefficient": target_zero_coefficient,
        "jump_cost_at_capsule_target": math.pi * target_zero_coefficient,
        "coefficient_slack": allowed_zero_coefficient - target_zero_coefficient,
        "cost_slack": margin - capsule_half_height,
        "jensen_c16_jump_cost": 16.0 * math.pi,
    }


def candidate_routes() -> list[dict[str, str]]:
    """列出零跳变预算的候选闭合路线。"""
    return [
        {
            "route": ZERO_COEFF,
            "status": "sufficient_but_stronger_than_needed",
            "content": "证明未配对跳变 log(T) 系数为 0；足够闭合，但比实际预算需求更强。",
        },
        {
            "route": CAPSULE_DENSITY,
            "status": "new_best_internal_target",
            "content": "证明近零胶囊内未配对零点数系数不超过 (eta+H)/pi，并且不调用 Backlund/RVM。",
        },
        {
            "route": EXTERNAL_ATOM,
            "status": "external_escape",
            "content": "接受经典 Backlund 缩进引理，直接关闭该预算包；不是严格自足路线。",
        },
    ]


def build_rows(
    atomic: dict[str, Any],
    near: dict[str, Any],
    variation: dict[str, Any],
    spike: dict[str, Any],
    c: dict[str, float],
) -> list[dict[str, Any]]:
    """生成胶囊密度松弛判定表。"""
    active = atomic.get("strict_self_contained_unique_remaining") == ZERO_COEFF
    guard = (
        atomic.get("counterexample_assumption_only") is True
        and atomic.get("empirical_absence_not_used") is True
        and atomic.get("hypothetical_chain_only") is True
    )
    eta_ready = float(near.get("eta", 0.0)) == c["eta"]
    h_ready = float(variation.get("window_length", 0.0)) == c["window_length_H"]
    no_rvm = NO_RVM in spike.get("closed_gates", []) or "NoRVMCircularityDisciplineClosed" in spike.get(
        "closed_gates", []
    )
    capsule_fits = c["jump_cost_at_capsule_target"] < c["stability_margin"]
    return [
        row(
            "ZeroCoefficientGateActive",
            active,
            True,
            "上一层把严格自足唯一剩余压成未配对跳变零系数预算。",
            ZERO_COEFF,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析预算，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "EtaAndWindowImported",
            eta_ready and h_ready,
            True,
            "近零半径 eta=1/16 与短窗口 H=1/512 已固定，因此胶囊半高 A=eta+H=33/512。",
            CAPSULE_DENSITY,
        ),
        row(
            "ZeroCoefficientSufficientButNotNecessary",
            True,
            True,
            "零系数可以闭合预算，但实际只需未配对零点密度低于 5/(64*pi)。",
            CAPSULE_DENSITY,
        ),
        row(
            "CapsuleDensityTargetFitsMargin",
            capsule_fits,
            True,
            "若未配对胶囊零点系数 <=(eta+H)/pi，则跳变成本 <=eta+H=33/512<5/64。",
            CAPSULE_DENSITY,
        ),
        row(
            "JensenC16StillTooCoarse",
            True,
            True,
            "Jensen C16 粗数给出 16*pi 的跳变系数，远超余量；必须证明胶囊高度比例密度。",
            CAPSULE_DENSITY,
        ),
        row(
            "NoRVMCircularityStillRequired",
            no_rvm,
            True,
            "不能直接调用由 Backlund C_S 推出的 RVM/CN16；胶囊密度必须独立证明。",
            CAPSULE_DENSITY,
        ),
        row(
            CAPSULE_DENSITY,
            False,
            False,
            "当前仓库还没有独立证明近零胶囊未配对零点数具有 (eta+H)/pi 级密度系数。",
            f"{CAPSULE_DENSITY} OR {ZERO_COEFF} OR {EXTERNAL_ATOM}",
        ),
        row(
            ZERO_COEFF,
            False,
            False,
            "零系数原子被放宽为更优的胶囊密度原子；二者任一闭合即可推进内部缩进成本。",
            CAPSULE_DENSITY,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行近零胶囊密度松弛审查。"""
    atomic = load_json(paths["atomic"])
    near = load_json(paths["near"])
    variation = load_json(paths["variation"])
    spike = load_json(paths["spike"])
    c = constants()
    rows = build_rows(atomic, near, variation, spike, c)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_capsule_density_relaxation_router",
        "status": "backlund_zero_jump_reduced_to_capsule_density_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zero_coefficient_relaxation_closed": True,
        "capsule_density_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "constants": c,
        "candidate_routes": candidate_routes(),
        "strict_self_contained_unique_remaining": CAPSULE_DENSITY,
        "stronger_sufficient_remaining": ZERO_COEFF,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "未配对跳变零系数不是必要条件。"
            "利用已固定的 eta=1/16 与 H=1/512，近零胶囊半高 A=eta+H=33/512，"
            "若能独立证明未配对胶囊零点密度系数不超过 A/pi，则跳变成本至多 A=33/512，"
            "小于稳定余量 5/64=40/512。"
            "因此当前更优的严格自足目标是 `BacklundIndependentCapsuleZeroDensityCoefficientLedger`；"
            "它必须独立于 Backlund/RVM 证明，不能退回 Jensen C16 粗计数。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    c = result["constants"]
    lines = [
        "# Prime Matrix Backlund 近零胶囊密度松弛路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"zero_coefficient_relaxation_closed={fmt_bool(result['zero_coefficient_relaxation_closed'])}",
        f"capsule_density_self_contained_closed={fmt_bool(result['capsule_density_self_contained_closed'])}",
        f"strict_self_contained_unique_remaining={result['strict_self_contained_unique_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 关键常数",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| eta | `{c['eta']:.12f}` |",
        f"| H | `{c['window_length_H']:.12f}` |",
        f"| A=eta+H | `{c['capsule_half_height_A']:.12f}` |",
        f"| stability margin | `{c['stability_margin']:.12f}` |",
        f"| allowed zero coefficient | `{c['allowed_zero_coefficient']:.12f}` |",
        f"| capsule target zero coefficient | `{c['capsule_target_zero_coefficient']:.12f}` |",
        f"| jump cost at capsule target | `{c['jump_cost_at_capsule_target']:.12f}` |",
        f"| cost slack | `{c['cost_slack']:.12f}` |",
        f"| Jensen C16 jump cost | `{c['jensen_c16_jump_cost']:.12f}` |",
        "",
        "等价看法：`A=33/512`，而稳定余量 `5/64=40/512`，还剩 `7/512` 成本余量。",
        "",
        "## 2. 候选路线",
        "",
        "| route | status | content |",
        "| --- | --- | --- |",
    ]
    for item in result["candidate_routes"]:
        lines.append(
            f"| `{table_cell(item['route'])}` | `{table_cell(item['status'])}` | {table_cell(item['content'])} |"
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
            f"新的严格自足最优剩余：`{result['strict_self_contained_unique_remaining']}`。",
            f"更强充分目标仍可选：`{result['stronger_sufficient_remaining']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：零系数目标已被更优的胶囊密度目标替代；该目标尚未自足闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atomic-json", type=Path, default=DEFAULT_ATOMIC)
    parser.add_argument("--near-json", type=Path, default=DEFAULT_NEAR)
    parser.add_argument("--variation-json", type=Path, default=DEFAULT_VARIATION)
    parser.add_argument("--spike-json", type=Path, default=DEFAULT_SPIKE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "atomic": args.atomic_json,
        "near": args.near_json,
        "variation": args.variation_json,
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
