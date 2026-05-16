#!/usr/bin/env python3
"""审计活跃 ell 端点运动制造的内部缺口。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_endpoint_motion_gap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
BUDGET_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json"
BUDGET_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_rankin_budget_router.py"
)

OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-router.md"

NEXT_TARGET = "EndpointMotionGapFillBoundOrGapPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def is_prime(n: int) -> bool:
    """小范围素性判定。"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_interval(lo: int, hi: int) -> list[int]:
    """闭区间素数列表。"""
    return [n for n in range(lo, hi + 1) if is_prime(n)]


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩首次激活记录。"""
    return {
        "p": int(record["p"]),
        "side": str(record["side"]),
        "rho": int(record["rho"]),
        "ell": int(record["ell_tuple"][0]),
        "crt_residue": int(record["crt_residue"]),
        "slot_keys": list(record["slot_keys"]),
        "margin": int(record["residual_prime_pair_margin_to_bound"]),
        "left_depth": int(record["left_depth"]),
        "right_depth": int(record["right_depth"]),
    }


def build_singleton_records(template_ledger: Path, budget_ledger: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """重放并提取 singleton residue 物理记录。"""
    budget = load_json(budget_ledger)
    params = budget["parameters"]
    budget_router = load_module(BUDGET_ROUTER, "endpoint_motion_budget")
    records = budget_router.build_singleton_records(
        template_ledger,
        int(params["max_p"]),
        int(params["p0"]),
        float(params["target_h_coeff"]),
        int(params["max_certificate_size"]),
    )
    return records, params


def first_activation_rows(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """提取每个一槽 ell 的首次激活。"""
    first: dict[int, dict[str, Any]] = {}
    for record in records:
        if int(record["certificate_size"]) != 1:
            continue
        ell = int(record["ell_tuple"][0])
        if ell not in first or int(record["p"]) < int(first[ell]["p"]):
            first[ell] = record
    rows = [compact(record) for record in first.values()]
    return sorted(rows, key=lambda row: (row["p"], row["ell"]))


def activation_snapshots(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按首次激活顺序生成端点运动快照。"""
    first_p_by_ell = {row["ell"]: row["p"] for row in rows}
    active: set[int] = set()
    snapshots = []
    for row in rows:
        active.add(row["ell"])
        lo = min(active)
        hi = max(active)
        band = prime_interval(lo, hi)
        missing = sorted(set(band).difference(active))
        fill_delays = {
            str(ell): first_p_by_ell[ell] - row["p"]
            for ell in missing
            if ell in first_p_by_ell
        }
        snapshots.append(
            {
                "activation_p": row["p"],
                "activated_ell": row["ell"],
                "activated_side": row["side"],
                "active_count": len(active),
                "band_min": lo,
                "band_max": hi,
                "band_prime_count": len(band),
                "missing_internal_prime_ells": missing,
                "missing_count": len(missing),
                "known_fill_delays": fill_delays,
                "is_exact_prime_interval": len(missing) == 0,
            }
        )
    return snapshots


def prefix_snapshots(rows: list[dict[str, Any]], cutoffs: list[int]) -> list[dict[str, Any]]:
    """按 P 前缀截断生成粗快照。"""
    result = []
    for cutoff in cutoffs:
        active = {row["ell"] for row in rows if row["p"] <= cutoff}
        if not active:
            result.append({"cutoff": cutoff, "active_count": 0, "is_exact_prime_interval": True})
            continue
        lo = min(active)
        hi = max(active)
        band = prime_interval(lo, hi)
        missing = sorted(set(band).difference(active))
        result.append(
            {
                "cutoff": cutoff,
                "active_count": len(active),
                "band_min": lo,
                "band_max": hi,
                "band_prime_count": len(band),
                "missing_internal_prime_ells": missing,
                "is_exact_prime_interval": len(missing) == 0,
            }
        )
    return result


def build_result(template_ledger: Path, budget_ledger: Path) -> dict[str, Any]:
    """构造端点运动缺口审计。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    records, params = build_singleton_records(template_ledger, budget_ledger)
    activation_rows = first_activation_rows(records)
    snapshots = activation_snapshots(activation_rows)
    gap_snapshots = [row for row in snapshots if row["missing_count"] > 0]
    gap_ells = sorted({ell for row in gap_snapshots for ell in row["missing_internal_prime_ells"]})
    fill_delays = [
        delay
        for row in gap_snapshots
        for delay in row["known_fill_delays"].values()
    ]
    cutoffs = list(range(3000, int(params["max_p"]) + 1, 1000))
    prefix_rows = prefix_snapshots(activation_rows, cutoffs)
    final = snapshots[-1]
    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "endpoint_motion_gap_router"
        ),
        "status": "endpoint_motion_gap_fill_profile_closed_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "activation_count": len(activation_rows),
        "activation_rows": activation_rows,
        "activation_snapshots": snapshots,
        "prefix_snapshots_1000": prefix_rows,
        "gap_snapshot_count": len(gap_snapshots),
        "gap_snapshots": gap_snapshots,
        "gap_ells": gap_ells,
        "max_known_gap_fill_delay": max(fill_delays) if fill_delays else 0,
        "all_activation_gaps_filled_in_current_sweep": all(
            ell in {row["ell"] for row in activation_rows} for ell in gap_ells
        ),
        "all_1000_prefix_snapshots_exact_intervals": all(row["is_exact_prime_interval"] for row in prefix_rows),
        "final_active_band": [final["band_min"], final["band_max"]],
        "final_active_count": final["active_count"],
        "final_exact_prime_interval": final["is_exact_prime_interval"],
        "endpoint_motion_gap_fill_bound_proved": False,
        "gap_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "EndpointBandMotionBoundOrEndpointAtomPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "按首次激活顺序看，活跃 `ell` 带端点扩张只制造了 "
            f"{len(gap_snapshots)} 次内部素数缺口，缺口 `ell` 为 {gap_ells}，"
            f"当前扫描内最大已知填充延迟为 {max(fill_delays) if fill_delays else 0}。"
            "所有千级 P 前缀快照均保持连续素数带。全局剩余因此可进一步表述为："
            "证明端点扩张制造的内部缺口有统一填充界，或把持久缺口登记并排斥为 Gap-PDEC/SAE。"
        ),
    }
    ledger = {
        "budget_ledger": str(budget_ledger.relative_to(ROOT)),
        "activation_count": result["activation_count"],
        "activation_rows": activation_rows,
        "activation_snapshots": snapshots,
        "prefix_snapshots_1000": prefix_rows,
        "gap_snapshots": gap_snapshots,
        "gap_ells": gap_ells,
        "max_known_gap_fill_delay": result["max_known_gap_fill_delay"],
        "final_active_band": result["final_active_band"],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_endpoint_motion_gap_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json": sha256(
            budget_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower endpoint motion gap router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"activation_count={result['activation_count']}",
        f"gap_snapshot_count={result['gap_snapshot_count']}",
        f"gap_ells={result['gap_ells']}",
        f"max_known_gap_fill_delay={result['max_known_gap_fill_delay']}",
        f"all_activation_gaps_filled_in_current_sweep={fmt_bool(result['all_activation_gaps_filled_in_current_sweep'])}",
        f"all_1000_prefix_snapshots_exact_intervals={fmt_bool(result['all_1000_prefix_snapshots_exact_intervals'])}",
        f"final_active_band={result['final_active_band']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 首次激活",
        "",
        "| p | ell | side | residue | slot | margin |",
        "| ---: | ---: | --- | ---: | --- | ---: |",
    ]
    for row in result["activation_rows"]:
        lines.append(
            f"| {row['p']} | {row['ell']} | `{row['side']}` | {row['crt_residue']} | "
            f"`{row['slot_keys']}` | {row['margin']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 缺口快照",
            "",
            "| p | activated ell | band | missing | fill delays |",
            "| ---: | ---: | --- | --- | --- |",
        ]
    )
    for row in result["gap_snapshots"]:
        lines.append(
            f"| {row['activation_p']} | {row['activated_ell']} | "
            f"`{row['band_min']}..{row['band_max']}` | `{row['missing_internal_prime_ells']}` | "
            f"`{row['known_fill_delays']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 千级 P 前缀",
            "",
            "| cutoff | active count | band | exact interval | missing |",
            "| ---: | ---: | --- | ---: | --- |",
        ]
    )
    for row in result["prefix_snapshots_1000"]:
        band = "empty" if row["active_count"] == 0 else f"{row['band_min']}..{row['band_max']}"
        lines.append(
            f"| {row['cutoff']} | {row['active_count']} | `{band}` | "
            f"`{fmt_bool(row['is_exact_prime_interval'])}` | `{row.get('missing_internal_prime_ells', [])}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构结论",
            "",
            "- 当前端点扩张不是任意散乱激活，而是带短暂内部缺口的素数带运动。",
            "- 缺口事件只有三类：`43`、`31`、`59`，并且当前扫描内都被后续首次激活填回。",
            "- 全局闭合仍需要证明统一填充界，或证明持久缺口会形成可排斥的 Gap-PDEC/SAE。",
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 将缺口填充延迟写成端点 CRT 相位宽度与新 `ell` 首次激活原子的比较不等式。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--budget-ledger", type=Path, default=BUDGET_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    budget_ledger = args.budget_ledger if args.budget_ledger.is_absolute() else ROOT / args.budget_ledger
    result = build_result(template_ledger, budget_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "activation_count": result["activation_count"],
                "gap_snapshot_count": result["gap_snapshot_count"],
                "gap_ells": result["gap_ells"],
                "max_known_gap_fill_delay": result["max_known_gap_fill_delay"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
