#!/usr/bin/env python3
"""把平方锚特殊相位压成偶数半网格覆盖字。

用法示例：
  python3 experiments/prime_matrix_square_phase_halfgrid_boundary_word_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-halfgrid-boundary-word-router.json

输出：
  data/square-phase-halfgrid-boundary-word-ledger.json
  docs/monograph/prime-matrix-square-phase-halfgrid-boundary-word-router.json
  docs/monograph/prime-matrix-square-phase-halfgrid-boundary-word-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SPLIT_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py"

OUT_LEDGER = DATA / "square-phase-halfgrid-boundary-word-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-halfgrid-boundary-word-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-halfgrid-boundary-word-router.md"

MAIN_TARGET = "SquarePhaseSpecialPhaseLongBlockPDECExclusion"
NEXT_TARGET = "HalfGridSurvivorBeatsActivatedTailSupportOrBoundaryWordPDEC"


def load_split_router() -> Any:
    """加载已有 no-slot 分裂路由器。"""
    spec = importlib.util.spec_from_file_location("noslot_k0_split_router", SPLIT_ROUTER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SPLIT_ROUTER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sieve(limit: int) -> bytearray:
    """筛出 limit 以内素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int | None = None) -> list[int]:
    """从筛表提取素数。"""
    end = len(flags) if limit is None else min(limit + 1, len(flags))
    return [idx for idx in range(2, end) if flags[idx]]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def responsible_prime_for_half_slot(p: int, s_value: int, side: str, odd_primes: list[int]) -> int | None:
    """返回半网格槽 s 的最小奇责任素数；无覆盖则返回 None。"""
    r_value = 2 * s_value
    value = p * p + r_value if side == "plus" else p * p - r_value
    for q_value in odd_primes:
        if q_value >= p:
            break
        if value % q_value == 0:
            return q_value
    return None


def halfgrid_record(p: int, side: str, primes: list[int]) -> dict[str, Any]:
    """审计一个 P,side 的偶数半网格覆盖。"""
    half = (p - 1) // 2
    odd_primes = [prime for prime in primes if prime != 2 and prime < p]
    survivors: list[int] = []
    covered_count = 0
    responsibility_histogram: dict[int, int] = {}
    boundary_word: list[int] = []

    if side == "plus":
        boundary_slots = range(1, half + 1)
    elif side == "minus":
        boundary_slots = range(half, 0, -1)
    else:
        raise ValueError(f"unknown side: {side}")

    boundary_open = False
    first_boundary_survivor: int | None = None
    for s_value in boundary_slots:
        q_value = responsible_prime_for_half_slot(p, s_value, side, odd_primes)
        if q_value is None:
            first_boundary_survivor = s_value
            boundary_open = True
            break
        boundary_word.append(q_value)

    for s_value in range(1, half + 1):
        q_value = responsible_prime_for_half_slot(p, s_value, side, odd_primes)
        if q_value is None:
            survivors.append(s_value)
            continue
        covered_count += 1
        responsibility_histogram[q_value] = responsibility_histogram.get(q_value, 0) + 1

    if first_boundary_survivor is None and not boundary_open:
        boundary_run = p - 1
        first_survivor_r = None
    elif side == "plus":
        boundary_run = 2 * int(first_boundary_survivor) - 1
        first_survivor_r = 2 * int(first_boundary_survivor)
    else:
        boundary_run = 2 * (half - int(first_boundary_survivor))
        first_survivor_r = 2 * int(first_boundary_survivor)

    top_responsibility = sorted(
        [{"q": q_value, "slots": slots} for q_value, slots in responsibility_histogram.items()],
        key=lambda row: (row["slots"], row["q"]),
        reverse=True,
    )[:8]
    return {
        "half_grid_size": half,
        "covered_half_slots": covered_count,
        "half_grid_survivor_count": len(survivors),
        "first_survivor_s": survivors[0] if side == "plus" and survivors else (survivors[-1] if survivors else None),
        "first_survivor_r_from_boundary": first_survivor_r,
        "boundary_covered_run_length_in_original_window": boundary_run,
        "boundary_word_prefix": boundary_word[:40],
        "boundary_word_length": len(boundary_word),
        "top_responsibility": top_responsibility,
        "survivor_s_prefix": survivors[:20],
        "survivor_r_prefix": [2 * s_value for s_value in survivors[:20]],
        "full_cover": len(survivors) == 0,
    }


def audit_side(split: Any, p: int, side: str, primes: list[int], prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """审计单侧半网格与总压力支撑。"""
    split_record = split.audit_p(p, prime_flags, pi_prefix)
    half = halfgrid_record(p, side, primes)
    prime_window = split_record[f"{side}_prime_window"]
    no_slot_load = split_record[f"{side}_no_slot_load"]
    half_survivors = half["half_grid_survivor_count"]
    return {
        "p": p,
        "side": side,
        "prime_window": prime_window,
        "half_grid_survivor_count": half_survivors,
        "half_grid_size": half["half_grid_size"],
        "halfgrid_prime_identity_ok": prime_window == half_survivors,
        "no_slot_load": no_slot_load,
        "total_pressure_margin": half_survivors - 2 * no_slot_load,
        "total_pressure_defect": half_survivors <= 2 * no_slot_load,
        "full_cover": half["full_cover"],
        "boundary_covered_run_length_in_original_window": half["boundary_covered_run_length_in_original_window"],
        "first_survivor_r_from_boundary": half["first_survivor_r_from_boundary"],
        "boundary_word_length": half["boundary_word_length"],
        "boundary_word_prefix": half["boundary_word_prefix"],
        "top_responsibility": half["top_responsibility"],
        "survivor_r_prefix": half["survivor_r_prefix"],
    }


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩审计记录。"""
    return {
        "p": record["p"],
        "side": record["side"],
        "prime_window": record["prime_window"],
        "half_grid_survivor_count": record["half_grid_survivor_count"],
        "half_grid_size": record["half_grid_size"],
        "no_slot_load": record["no_slot_load"],
        "total_pressure_margin": record["total_pressure_margin"],
        "boundary_run": record["boundary_covered_run_length_in_original_window"],
        "first_survivor_r": record["first_survivor_r_from_boundary"],
        "boundary_word_prefix": record["boundary_word_prefix"],
        "top_responsibility": record["top_responsibility"],
        "survivor_r_prefix": record["survivor_r_prefix"],
        "full_cover": record["full_cover"],
        "total_pressure_defect": record["total_pressure_defect"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "odd_columns_removed_by_two",
            "status": "closed",
            "statement": "For odd P, every odd r in P^2±r is even, hence automatically covered by q=2.",
        },
        {
            "name": "halfgrid_primewindow_identity",
            "status": "closed",
            "statement": "PrimeWindow_side(P) equals the number of uncovered even slots r=2s after sieving by odd q<P.",
        },
        {
            "name": "special_long_block_halfgrid_form",
            "status": "closed",
            "statement": "A square-phase full cover is equivalent to zero survivors on the signed even half-grid.",
        },
        {
            "name": "total_pressure_halfgrid_form",
            "status": "closed",
            "statement": "The latest total pressure defect is exactly HalfGridSurvivors_side(P)<=2*NoSlotLoad_side(P).",
        },
        {
            "name": "finite_no_halfgrid_full_cover_or_pressure_defect",
            "status": "finite_evidence",
            "statement": "The finite audit finds no half-grid full cover and no total pressure defect up to the tested bound.",
        },
        {
            "name": "halfgrid_survivor_lower_bound",
            "status": "open",
            "statement": "A global proof still needs HalfGridSurvivors_side(P)>2*NoSlotLoad_side(P), or a BoundaryWord-PDEC/SAE/ColumnCRT exclusion.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "OddColumnsRemovedByTwoClosed",
            "closed": True,
            "proved": True,
            "meaning": "平方锚窗口的奇数列由 `q=2` 自动覆盖，真实自由度只在偶数半网格。",
            "remaining": "closed",
        },
        {
            "gate": "HalfGridPrimeWindowIdentityClosed",
            "closed": result["halfgrid_prime_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "`PrimeWindow` 已精确等于偶数半网格幸存数。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoHalfGridFullCover",
            "closed": result["full_cover_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中没有半网格全覆盖。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "FiniteNoTotalPressureDefect",
            "closed": result["total_pressure_defect_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中没有 `HalfGridSurvivors<=2*NoSlotLoad`。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "HalfGridSurvivorLowerBoundProvedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明半网格幸存数压过激活尾支撑负载的两倍。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把特殊相位硬点压到半网格覆盖字，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    split = load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = sieve(max_p)
    primes = primes_from_flags(small_flags, max_p)
    p_values = [p for p in primes if p >= 3]
    records = [
        audit_side(split, p, side, primes, prime_flags, pi_prefix)
        for p in p_values
        for side in ("plus", "minus")
    ]
    identity_failures = [record for record in records if not record["halfgrid_prime_identity_ok"]]
    full_cover_records = [record for record in records if record["full_cover"]]
    pressure_defect_records = [record for record in records if record["total_pressure_defect"]]
    frontier = sorted(records, key=lambda record: (record["total_pressure_margin"], record["p"], record["side"]))
    max_boundary_run = max(records, key=lambda record: record["boundary_covered_run_length_in_original_window"], default=None)
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    aggregate = {
        "record_count": len(records),
        "combined_prime_window": sum(record["prime_window"] for record in records),
        "combined_halfgrid_survivors": sum(record["half_grid_survivor_count"] for record in records),
        "combined_no_slot_load": sum(record["no_slot_load"] for record in records),
        "halfgrid_prime_identity_failure_count": len(identity_failures),
        "full_cover_count": len(full_cover_records),
        "total_pressure_defect_count": len(pressure_defect_records),
        "min_total_pressure_margin": frontier[0]["total_pressure_margin"] if frontier else None,
        "max_boundary_run": (
            max_boundary_run["boundary_covered_run_length_in_original_window"] if max_boundary_run else None
        ),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "frontier_records": [compact(record) for record in frontier[:80]],
        "max_boundary_run_record": compact(max_boundary_run) if max_boundary_run else None,
        "sample_records": [compact(record) for record in sample_records],
        "halfgrid_prime_identity_failures": [compact(record) for record in identity_failures[:20]],
        "full_cover_records": [compact(record) for record in full_cover_records[:20]],
        "total_pressure_defect_records": [compact(record) for record in pressure_defect_records[:20]],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_halfgrid_boundary_word_router",
        "status": "square_phase_special_longblock_reduced_to_even_halfgrid_boundary_word_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "halfgrid_prime_identity_failure_count": len(identity_failures),
        "full_cover_count": len(full_cover_records),
        "total_pressure_defect_count": len(pressure_defect_records),
        "frontier_records": ledger["frontier_records"][:20],
        "max_boundary_run_record": ledger["max_boundary_run_record"],
        "sample_records": ledger["sample_records"],
        "halfgrid_primewindow_identity_closed": len(identity_failures) == 0,
        "finite_no_halfgrid_full_cover": len(full_cover_records) == 0,
        "finite_no_total_pressure_defect": len(pressure_defect_records) == 0,
        "halfgrid_survivor_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_halfgrid_boundary_word_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(SPLIT_ROUTER),
            "data/square-phase-halfgrid-boundary-word-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把平方锚特殊相位长块命中压成偶数半网格覆盖字。"
            "因为 `P` 为奇素数，`P^2±r` 在所有奇数 `r` 上都被 `q=2` 覆盖；"
            "因此真正决定平方锚素数的只有 `r=2s`。"
            "逐项审计证明 `PrimeWindow_side(P)` 精确等于 signed half-grid 中未被奇素数 `q<P` 覆盖的槽数。"
            "于是最新总压力硬点化为 `HalfGridSurvivors_side(P)>2*NoSlotLoad_side(P)`。"
            "有限扫描没有半网格全覆盖或总压力缺陷；全局仍需证明该半网格幸存下界，或登记边界覆盖字 PDEC/SAE/ColumnCRT。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase half-grid boundary word router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"halfgrid_prime_identity_failure_count={result['halfgrid_prime_identity_failure_count']}",
        f"full_cover_count={result['full_cover_count']}",
        f"total_pressure_defect_count={result['total_pressure_defect_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 半网格正规形",
        "",
        "由于 `P` 为奇素数，奇数 `r` 使 `P^2±r` 为偶数，所以全部由 `q=2` 覆盖。令 `r=2s`，`1<=s<=(P-1)/2`。对奇素数 `q<P`：",
        "",
        "```text",
        "plus:  q | P^2+2s  iff  s == -P^2 * 2^{-1} (mod q),",
        "minus: q | P^2-2s  iff  s ==  P^2 * 2^{-1} (mod q).",
        "```",
        "",
        "因此平方锚全覆盖等价于 signed half-grid 没有任何幸存槽。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| record count | {agg['record_count']} |",
        f"| combined PrimeWindow | {agg['combined_prime_window']} |",
        f"| combined half-grid survivors | {agg['combined_halfgrid_survivors']} |",
        f"| combined NoSlotLoad | {agg['combined_no_slot_load']} |",
        f"| identity failures | {agg['halfgrid_prime_identity_failure_count']} |",
        f"| full cover count | {agg['full_cover_count']} |",
        f"| total pressure defect count | {agg['total_pressure_defect_count']} |",
        f"| min total pressure margin | {agg['min_total_pressure_margin']} |",
        f"| max boundary run | {agg['max_boundary_run']} |",
        "",
        "## 3. 边界记录",
        "",
        "| label | P | side | W | half survivors | NoSlot | W-2N | boundary run | first survivor r |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    boundary_rows = [("worst margin", result["frontier_records"][0] if result["frontier_records"] else None)]
    boundary_rows.append(("max boundary run", result["max_boundary_run_record"]))
    for label, record in boundary_rows:
        if not record:
            continue
        lines.append(
            "| "
            + " | ".join(
                [
                    label,
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["prime_window"]),
                    str(record["half_grid_survivor_count"]),
                    str(record["no_slot_load"]),
                    str(record["total_pressure_margin"]),
                    str(record["boundary_run"]),
                    str(record["first_survivor_r"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 样本边界覆盖字",
            "",
            "| P | side | boundary run | first survivor r | word prefix | survivor prefix |",
            "| ---: | --- | ---: | ---: | --- | --- |",
        ]
    )
    for record in result["sample_records"][:24]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["boundary_run"]),
                    str(record["first_survivor_r"]),
                    "`" + ",".join(str(item) for item in record["boundary_word_prefix"][:16]) + "`",
                    "`" + ",".join(str(item) for item in record["survivor_r_prefix"][:10]) + "`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 6. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 7. 下一步",
            "",
            "- 主攻：`HalfGridSurvivorBeatsActivatedTailSupportOrBoundaryWordPDEC`。",
            "- 也就是证明 signed half-grid 的幸存槽数始终大于 `2*NoSlotLoad`。",
            "- 若失败，反例必须给出一个极长边界覆盖字；该覆盖字的责任素数序列可登记为 BoundaryWord-PDEC、端点 SAE 或 ColumnCRT。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument(
        "--sample-ps",
        type=str,
        default="13,17,19,23,29,31,101,499,1009,2003,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-halfgrid-boundary-word-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "halfgrid_prime_identity_failure_count": result["halfgrid_prime_identity_failure_count"],
                "full_cover_count": result["full_cover_count"],
                "total_pressure_defect_count": result["total_pressure_defect_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
