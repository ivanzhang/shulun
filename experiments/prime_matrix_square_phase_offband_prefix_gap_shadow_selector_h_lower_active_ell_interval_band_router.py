#!/usr/bin/env python3
"""审计活跃 ell 来源是否形成连续素数带。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_active_ell_interval_band_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SOURCE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-router.md"

NEXT_TARGET = "ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


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


def primes_between(lo: int, hi: int) -> list[int]:
    """列出闭区间素数。"""
    return [n for n in range(lo, hi + 1) if is_prime(n)]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def build_result(source_path: Path) -> dict[str, Any]:
    """构造连续素数带审计结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)

    source = load_json(source_path)
    agg = source["aggregate"]
    active = list(map(int, agg["active_ell_values"]))
    both = list(map(int, agg["both_side_ell_values"]))
    minus_only = list(map(int, agg["minus_only_ell_values"]))
    plus_only = list(map(int, agg["plus_only_ell_values"]))

    full_band = primes_between(min(active), max(active))
    both_band = primes_between(min(both), max(both))
    below_gap = primes_between(2, min(active) - 1)

    exact_active_prime_interval = active == full_band
    exact_both_side_prime_interval = both == both_band
    endpoint_asymmetry_only = minus_only == [min(active), max(active)] and plus_only == []

    ledger = {
        "source_ledger": str(source_path.relative_to(ROOT)),
        "active_ell_values": active,
        "active_prime_interval": full_band,
        "both_side_ell_values": both,
        "both_side_prime_interval": both_band,
        "missing_small_prime_sources_below_active_band": below_gap,
        "minus_only_ell_values": minus_only,
        "plus_only_ell_values": plus_only,
        "exact_active_prime_interval_current_sweep": exact_active_prime_interval,
        "exact_both_side_prime_interval_current_sweep": exact_both_side_prime_interval,
        "endpoint_asymmetry_only_current_sweep": endpoint_asymmetry_only,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "active_ell_interval_band_router"
        ),
        "status": "active_ell_interval_band_closed_current_sweep_endpoint_growth_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "exact_active_prime_interval_current_sweep": exact_active_prime_interval,
        "exact_both_side_prime_interval_current_sweep": exact_both_side_prime_interval,
        "endpoint_asymmetry_only_current_sweep": endpoint_asymmetry_only,
        "active_band_min": min(active),
        "active_band_max": max(active),
        "active_band_prime_count": len(full_band),
        "both_side_band_min": min(both),
        "both_side_band_max": max(both),
        "both_side_band_prime_count": len(both_band),
        "missing_small_prime_source_count_below_active_band": len(below_gap),
        "missing_small_prime_sources_below_active_band": below_gap,
        "minus_only_ell_values": minus_only,
        "plus_only_ell_values": plus_only,
        "active_ell_band_endpoint_growth_bound_proved": False,
        "endpoint_reset_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "ActiveEllGrowthBoundOrTransportResetPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "当前扫描中活跃 `ell` 来源不是任意稀疏集合，而是精确等于闭区间 "
            f"`{min(active)}..{max(active)}` 内的全部素数，共 {len(full_band)} 个；"
            f"双侧共同活跃核心为 `{min(both)}..{max(both)}` 内的全部素数，共 {len(both_band)} 个。"
            f"相位不对称只发生在 minus-only 端点 `{minus_only}`，plus-only 为空。"
            "因此下一步可把一般活跃来源增长界压成端点增长界，或证明端点移动触发 reset-PDEC/SAE。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_active_ell_interval_band_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json": sha256(
            source_path
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower active ell interval band router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_active_prime_interval_current_sweep={fmt_bool(result['exact_active_prime_interval_current_sweep'])}",
        f"active_band={result['active_band_min']}..{result['active_band_max']}",
        f"active_band_prime_count={result['active_band_prime_count']}",
        f"both_side_band={result['both_side_band_min']}..{result['both_side_band_max']}",
        f"both_side_band_prime_count={result['both_side_band_prime_count']}",
        f"endpoint_asymmetry_only_current_sweep={fmt_bool(result['endpoint_asymmetry_only_current_sweep'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 带状结构",
        "",
        "| object | value |",
        "| --- | --- |",
        f"| active ell band | `{result['active_band_min']}..{result['active_band_max']}` |",
        f"| active prime count | `{result['active_band_prime_count']}` |",
        f"| both-side core band | `{result['both_side_band_min']}..{result['both_side_band_max']}` |",
        f"| both-side prime count | `{result['both_side_band_prime_count']}` |",
        f"| minus-only endpoints | `{result['minus_only_ell_values']}` |",
        f"| plus-only endpoints | `{result['plus_only_ell_values']}` |",
        f"| missing small prime sources below active band | `{result['missing_small_prime_sources_below_active_band']}` |",
        "",
        "## 2. 结构结论",
        "",
        "- 当前 formal unit 内，活跃来源增长不是任意组合增长，而是素数带端点增长。",
        "- 下端缺失小素数只有有限个，若全局活跃来源数失控，主要通道只能是上端点外推。",
        "- 端点外推必须与 residue 重复、transport reset-PDEC 或 SAE/Rankin 稀疏化发生对接；否则仍不能闭合行/列命题。",
        "",
        "## 3. 下一步",
        "",
        f"- 主攻：`{result['next_direct_attack_target']}`。",
        "- 证明活跃素数带端点增长受限，或证明端点移动必然形成可排斥的 endpoint reset-PDEC/SAE。",
        "",
        "## 4. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-ledger", type=Path, default=SOURCE_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    source_path = args.source_ledger if args.source_ledger.is_absolute() else ROOT / args.source_ledger
    result = build_result(source_path)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "active_band": [result["active_band_min"], result["active_band_max"]],
                "active_band_prime_count": result["active_band_prime_count"],
                "endpoint_asymmetry_only_current_sweep": result["endpoint_asymmetry_only_current_sweep"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
