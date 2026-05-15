#!/usr/bin/env python3
"""审计平方锚无槽尾素的二次相位层结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_noslot_phase_layer_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-noslot-phase-layer-router.json

输出：
  data/square-phase-noslot-phase-layer-ledger.json
  docs/monograph/prime-matrix-square-phase-noslot-phase-layer-router.json
  docs/monograph/prime-matrix-square-phase-noslot-phase-layer-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "square-phase-noslot-phase-layer-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-noslot-phase-layer-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-noslot-phase-layer-router.md"

MAIN_TARGET = "NoSlotTailPrimePhaseBandDefectPDECSAE"
NEXT_TARGET = "NoSlotFloorLayerBandBoundOrLayerPDEC"


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


def primes_from_flags(flags: bytearray, limit: int) -> list[int]:
    """从筛表提取不超过 limit 的素数。"""
    return [idx for idx in range(2, min(limit + 1, len(flags))) if flags[idx]]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def cutoff_alpha45(p: int) -> int:
    """返回 floor(4P/5)。"""
    return (4 * p) // 5


def square_prime_count(p: int, sign: str, prime_flags: bytearray) -> int:
    """计算 P^2 正负半窗内的素数个数。"""
    base = p * p
    total = 0
    for r_value in range(1, p):
        n_value = base + r_value if sign == "plus" else base - r_value
        if prime_flags[n_value]:
            total += 1
    return total


def layer_record(p: int, q_value: int) -> dict[str, Any]:
    """生成单个尾素的二次相位层记录。"""
    b_value = (p - q_value) // 2
    half = (p - 1) // 2
    left_width = q_value - half
    doubled_square = 2 * b_value * b_value
    k_value, residue = divmod(doubled_square, q_value)
    # 中文注释：2b^2 == P^2/2 (mod q)，用于把无槽条件接回平方锚相位。
    inv2 = pow(2, -1, q_value)
    p2_half_residue = (p * p * inv2) % q_value
    plus_no_slot = residue < left_width
    minus_no_slot = residue > half
    both_raw = not plus_no_slot and not minus_no_slot
    return {
        "q": q_value,
        "b": b_value,
        "k": k_value,
        "residue": residue,
        "p2_half_residue": p2_half_residue,
        "left_width": left_width,
        "half": half,
        "plus_no_slot": plus_no_slot,
        "minus_no_slot": minus_no_slot,
        "both_raw": both_raw,
        "phase_congruence_ok": residue == p2_half_residue,
        "exclusive_ok": sum([plus_no_slot, minus_no_slot, both_raw]) == 1,
    }


def audit_p(p: int, primes: list[int], prime_flags: bytearray) -> dict[str, Any]:
    """审计单个 P 的双侧无槽层结构。"""
    cutoff = cutoff_alpha45(p)
    tail_primes = [q for q in primes if cutoff < q < p]
    rows = [layer_record(p, q_value) for q_value in tail_primes]
    plus_no = [row for row in rows if row["plus_no_slot"]]
    minus_no = [row for row in rows if row["minus_no_slot"]]
    both_raw = [row for row in rows if row["both_raw"]]
    phase_failures = [row for row in rows if not row["phase_congruence_ok"]]
    exclusive_failures = [row for row in rows if not row["exclusive_ok"]]
    identity_delta = len(tail_primes) - len(plus_no) - len(minus_no) - len(both_raw)

    plus_prime = square_prime_count(p, "plus", prime_flags)
    minus_prime = square_prime_count(p, "minus", prime_flags)

    plus_layer_hist: dict[str, int] = {}
    minus_layer_hist: dict[str, int] = {}
    both_layer_hist: dict[str, int] = {}
    for row in plus_no:
        key = str(row["k"])
        plus_layer_hist[key] = plus_layer_hist.get(key, 0) + 1
    for row in minus_no:
        key = str(row["k"])
        minus_layer_hist[key] = minus_layer_hist.get(key, 0) + 1
    for row in both_raw:
        key = str(row["k"])
        both_layer_hist[key] = both_layer_hist.get(key, 0) + 1

    max_layer = max((row["k"] for row in rows), default=0)
    layer_count = max_layer + 1 if rows else 0
    plus_threshold = (plus_prime + 1) // 2
    minus_threshold = (minus_prime + 1) // 2
    plus_large = len(plus_no) >= plus_threshold
    minus_large = len(minus_no) >= minus_threshold
    plus_pigeonhole_layer_lower = 0 if layer_count == 0 else (plus_threshold + layer_count - 1) // layer_count
    minus_pigeonhole_layer_lower = 0 if layer_count == 0 else (minus_threshold + layer_count - 1) // layer_count

    return {
        "p": p,
        "cutoff": cutoff,
        "tail_prime_count": len(tail_primes),
        "plus_prime_window": plus_prime,
        "minus_prime_window": minus_prime,
        "plus_no_slot": len(plus_no),
        "minus_no_slot": len(minus_no),
        "both_raw": len(both_raw),
        "identity_delta": identity_delta,
        "phase_congruence_failure_count": len(phase_failures),
        "exclusive_failure_count": len(exclusive_failures),
        "max_layer_k": max_layer,
        "layer_count": layer_count,
        "plus_no_slot_large_branch": plus_large,
        "minus_no_slot_large_branch": minus_large,
        "plus_large_branch_forces_layer_count_at_least": plus_pigeonhole_layer_lower,
        "minus_large_branch_forces_layer_count_at_least": minus_pigeonhole_layer_lower,
        "plus_layer_histogram": dict(sorted(plus_layer_hist.items(), key=lambda item: int(item[0]))),
        "minus_layer_histogram": dict(sorted(minus_layer_hist.items(), key=lambda item: int(item[0]))),
        "both_raw_layer_histogram": dict(sorted(both_layer_hist.items(), key=lambda item: int(item[0]))),
        "plus_no_slot_samples": plus_no[:6],
        "minus_no_slot_samples": minus_no[:6],
        "both_raw_samples": both_raw[:6],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "tail_phase_congruence",
            "status": "closed",
            "statement": "For q=P-2b, 2b^2 is congruent to P^2/2 modulo q.",
        },
        {
            "name": "two_sided_noslot_trichotomy",
            "status": "closed",
            "statement": "Every tail prime belongs to exactly one of plus-no-slot, minus-no-slot, or both-sides-raw.",
        },
        {
            "name": "floor_layer_normal_form",
            "status": "closed",
            "statement": "Writing 2b^2=kq+s, plus-no-slot is s<q-(P-1)/2 and minus-no-slot is s>(P-1)/2.",
        },
        {
            "name": "large_noslot_branch_layer_return",
            "status": "closed",
            "statement": "A no-slot branch large enough to threaten PrimeWindow forces a floor layer with proportional phase-band mass.",
        },
        {
            "name": "layer_band_bound_or_pdec",
            "status": "open",
            "statement": "A global proof still needs a bound for every floor-layer phase band, or a PDEC/SAE exclusion of persistent layers.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "TailPhaseCongruenceClosed",
            "closed": result["phase_congruence_failure_count"] == 0,
            "proved": True,
            "meaning": "`2b^2 mod q` 已严格接回 `P^2/2 mod q`。",
            "remaining": "closed",
        },
        {
            "gate": "TwoSidedNoSlotTrichotomyClosed",
            "closed": result["trichotomy_failure_count"] == 0,
            "proved": True,
            "meaning": "每个尾素恰落入 plus 无槽、minus 无槽、双侧有槽三类之一。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoLargeNoSlotBranch",
            "closed": result["finite_large_noslot_branch_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 没有无槽分支达到 PrimeWindow/2。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalLayerBandBound",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局控制所有 floor layer 的二次相位端带命中。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只压缩无槽分支，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def merge_histograms(records: list[dict[str, Any]], key: str) -> dict[str, int]:
    """合并层直方图。"""
    merged: dict[str, int] = {}
    for record in records:
        for layer, count in record[key].items():
            merged[layer] = merged.get(layer, 0) + count
    return dict(sorted(merged.items(), key=lambda item: int(item[0])))


def top_histogram(histogram: dict[str, int], limit: int = 12) -> dict[str, int]:
    """取最重层。"""
    return dict(sorted(histogram.items(), key=lambda item: (-item[1], int(item[0])))[:limit])


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    prime_flags = sieve(max_p * max_p + max_p)
    primes = primes_from_flags(prime_flags, max_p)
    p_values = [p for p in primes if 3 <= p <= max_p]
    records = [audit_p(p, primes, prime_flags) for p in p_values]

    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    phase_failures = [record for record in records if record["phase_congruence_failure_count"]]
    exclusive_failures = [record for record in records if record["exclusive_failure_count"]]
    identity_failures = [record for record in records if record["identity_delta"] != 0]
    large_noslot = [
        record
        for record in records
        if record["plus_no_slot_large_branch"] or record["minus_no_slot_large_branch"]
    ]

    plus_hist = merge_histograms(records, "plus_layer_histogram")
    minus_hist = merge_histograms(records, "minus_layer_histogram")
    both_hist = merge_histograms(records, "both_raw_layer_histogram")

    aggregate = {
        "tail_prime_count": sum(record["tail_prime_count"] for record in records),
        "plus_prime_window": sum(record["plus_prime_window"] for record in records),
        "minus_prime_window": sum(record["minus_prime_window"] for record in records),
        "plus_no_slot": sum(record["plus_no_slot"] for record in records),
        "minus_no_slot": sum(record["minus_no_slot"] for record in records),
        "both_raw": sum(record["both_raw"] for record in records),
        "max_layer_k": max((record["max_layer_k"] for record in records), default=0),
    }
    aggregate["combined_prime_window"] = aggregate["plus_prime_window"] + aggregate["minus_prime_window"]
    aggregate["combined_no_slot"] = aggregate["plus_no_slot"] + aggregate["minus_no_slot"]

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "phase_congruence_failure_count": len(phase_failures),
        "exclusive_failure_count": len(exclusive_failures),
        "identity_failure_count": len(identity_failures),
        "finite_large_noslot_branch_count": len(large_noslot),
        "top_plus_layers": top_histogram(plus_hist),
        "top_minus_layers": top_histogram(minus_hist),
        "top_both_raw_layers": top_histogram(both_hist),
        "sample_records": sample_records,
        "phase_failures": phase_failures[:20],
        "exclusive_failures": exclusive_failures[:20],
        "identity_failures": identity_failures[:20],
        "large_noslot_branch_records": large_noslot[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_noslot_phase_layer_router",
        "status": "noslot_phase_band_reduced_to_floor_layer_bound_or_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "phase_congruence_failure_count": len(phase_failures),
        "exclusive_failure_count": len(exclusive_failures),
        "identity_failure_count": len(identity_failures),
        "trichotomy_failure_count": len(exclusive_failures) + len(identity_failures),
        "finite_large_noslot_branch_count": len(large_noslot),
        "top_plus_layers": ledger["top_plus_layers"],
        "top_minus_layers": ledger["top_minus_layers"],
        "top_both_raw_layers": ledger["top_both_raw_layers"],
        "sample_records": sample_records,
        "tail_phase_congruence_closed": len(phase_failures) == 0,
        "two_sided_noslot_trichotomy_closed": len(exclusive_failures) + len(identity_failures) == 0,
        "floor_layer_normal_form_closed": True,
        "global_layer_band_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_noslot_phase_layer_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-noslot-phase-layer-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把无槽尾素分支压成同一个二次相位的 floor-layer 问题。"
            "对 `q=P-2b` 有 `2b^2≡P^2/2 (mod q)`；写 `2b^2=kq+s` 后，"
            "plus 无槽等价于 `s<q-(P-1)/2`，minus 无槽等价于 `s>(P-1)/2`。"
            "因此每个尾素恰好落入 plus 无槽、minus 无槽、双侧有槽三类之一。"
            "若无槽分支大到威胁 `PrimeWindow`，必有某个 floor layer 承担相位端带质量。"
            "全局仍需证明层端带上界，或将持久层异常排斥为 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase no-slot phase layer router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"phase_congruence_failure_count={result['phase_congruence_failure_count']}",
        f"trichotomy_failure_count={result['trichotomy_failure_count']}",
        f"finite_large_noslot_branch_count={result['finite_large_noslot_branch_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 相位层正规形",
        "",
        "尾素写成 `q=P-2b`。因为",
        "",
        "```text",
        "2b^2 = (P-q)^2/2 == P^2/2 (mod q),",
        "```",
        "",
        "令 `h=(P-1)/2`，并写",
        "",
        "```text",
        "2b^2 = kq+s,  0<=s<q.",
        "```",
        "",
        "则三分法为",
        "",
        "```text",
        "plus no-slot  iff s < q-h",
        "minus no-slot iff s > h",
        "both raw       iff q-h <= s <= h.",
        "```",
        "",
        "因为 `q<P`，左右端带互斥。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| tail prime count | {agg['tail_prime_count']} |",
        f"| plus PrimeWindow | {agg['plus_prime_window']} |",
        f"| minus PrimeWindow | {agg['minus_prime_window']} |",
        f"| plus no-slot | {agg['plus_no_slot']} |",
        f"| minus no-slot | {agg['minus_no_slot']} |",
        f"| both raw | {agg['both_raw']} |",
        f"| max floor layer k | {agg['max_layer_k']} |",
        "",
        "## 3. 最重层",
        "",
        "| side | layer k | count |",
        "| --- | ---: | ---: |",
    ]
    for side, histogram in [
        ("plus", result["top_plus_layers"]),
        ("minus", result["top_minus_layers"]),
        ("both_raw", result["top_both_raw_layers"]),
    ]:
        for layer, count in histogram.items():
            lines.append(f"| `{side}` | {layer} | {count} |")

    lines.extend(
        [
            "",
            "## 4. 样本表",
            "",
            "| P | tail | plus prime | plus no-slot | minus prime | minus no-slot | both raw | max k | plus large | minus large |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | {row['tail_prime_count']} | {row['plus_prime_window']} | "
            f"{row['plus_no_slot']} | {row['minus_prime_window']} | {row['minus_no_slot']} | "
            f"{row['both_raw']} | {row['max_layer_k']} | "
            f"`{fmt_bool(row['plus_no_slot_large_branch'])}` | "
            f"`{fmt_bool(row['minus_no_slot_large_branch'])}` |"
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
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    lines.extend(
        [
            "",
            "## 6. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 7. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 这一步没有证明层端带全局上界；它只是把无槽异常压成固定 floor layer 的相位带异常。",
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析整数列表。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--sample-ps", default="13,17,19,23,29,31,101,499,1009,2003,4999")
    args = parser.parse_args()

    result = build_result(max_p=args.max_p, sample_ps=parse_ints(args.sample_ps))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": result["parameters"]["max_p"],
                "phase_congruence_failure_count": result["phase_congruence_failure_count"],
                "trichotomy_failure_count": result["trichotomy_failure_count"],
                "finite_large_noslot_branch_count": result["finite_large_noslot_branch_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
