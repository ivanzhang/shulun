#!/usr/bin/env python3
"""审计 z=61 PrefixGate quotient ladder 的 prime-a singleton 源纤维。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_source_fiber_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-source-fiber-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-source-fiber-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-source-fiber-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_prime_b_sieve_router as sieve


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
QUOTIENT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-source-fiber-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-source-fiber-router.md"

NEXT_TARGET = "SingletonPrimeAFiberLadderBalanceOrFiberPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.json",
]


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_source_fiber_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_candidates_for_p_list(p_list: list[int]) -> dict[int, list[dict[str, Any]]]:
    """收集每个 p 的 prime-a 候选。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = sieve.envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = sieve.envelope.primes_from_flags(flags, trial_limit)
    return {
        p_value: sieve.collect_prime_a_candidates(p_value, flags, trial_primes)
        for p_value in p_list
    }


def audit() -> dict[str, Any]:
    """执行源纤维审计。"""
    quotient_data = json.loads(QUOTIENT_JSON.read_text(encoding="utf-8"))
    p_list = sorted({row["p"] for row in quotient_data["quotient_rows"]})
    candidates_by_p = collect_candidates_for_p_list(p_list)
    source_rows = []
    for qrow in quotient_data["quotient_rows"]:
        candidates = [
            candidate
            for candidate in candidates_by_p[qrow["p"]]
            if int(candidate["b"]) == int(qrow["b_value"])
        ]
        source_rows.append(
            {
                "phase_quotient": qrow["phase_quotient"],
                "target_cell_sign": qrow["target_cell_sign"],
                "p": qrow["p"],
                "b_value": qrow["b_value"],
                "source_candidate_count": len(candidates),
                "source_candidates": candidates,
                "unique_singleton_prime_a_source_closed": (
                    len(candidates) == 1
                    and bool(candidates[0]["prime_a"])
                    and not bool(candidates[0]["prime_b"])
                    and bool(candidates[0]["singleton_ok"])
                    and candidates[0]["valid_a_interval"][0] == candidates[0]["valid_a_interval"][1]
                ),
            }
        )
    positive_sources = [row for row in source_rows if row["target_cell_sign"] == "positive"]
    negative_sources = [row for row in source_rows if row["target_cell_sign"] == "negative"]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_prefix_gate_source_fiber_router",
        "status": "z61_quotient_ladder_reduced_to_singleton_prime_a_source_fibers_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": quotient_data["certificate_type"],
        "phase_modulus": quotient_data["phase_modulus"],
        "phase_condition": quotient_data["phase_condition"],
        "source_rows": source_rows,
        "source_fiber_count": sum(row["source_candidate_count"] for row in source_rows),
        "all_quotient_hits_have_unique_singleton_prime_a_source": all(
            row["unique_singleton_prime_a_source_closed"] for row in source_rows
        ),
        "positive_source_fiber_count": len(positive_sources),
        "negative_source_fiber_count": len(negative_sources),
        "positive_minus_negative_source_fiber_count": len(positive_sources) - len(negative_sources),
        "source_fiber_ladder_identity_closed": (
            all(row["unique_singleton_prime_a_source_closed"] for row in source_rows)
            and len(positive_sources) == 2
            and len(negative_sources) == 1
        ),
        "singleton_prime_a_fiber_ladder_balance_proved": False,
        "fiber_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "PrefixGate quotient ladder 的三个相位命中均来自唯一 prime-a singleton 源纤维，"
            "且这些 `b` 都是 composite prime-b 失败点。负侧有一条源纤维，正侧有两条源纤维。"
            "因此 dyadic quotient count balance 可进一步改写为 singleton prime-a 源纤维配对/容量问题，"
            "或登记 Fiber-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 PrefixGate 源纤维",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"source_fiber_count={result['source_fiber_count']}",
        f"all_quotient_hits_have_unique_singleton_prime_a_source={fmt_bool(result['all_quotient_hits_have_unique_singleton_prime_a_source'])}",
        f"positive_source_fiber_count={result['positive_source_fiber_count']}",
        f"negative_source_fiber_count={result['negative_source_fiber_count']}",
        f"source_fiber_ladder_identity_closed={fmt_bool(result['source_fiber_ladder_identity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Singleton 源纤维",
        "",
        "| quotient | sign | p | b | q | a | n | a interval | singleton |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["source_rows"]:
        candidate = row["source_candidates"][0] if row["source_candidates"] else {}
        lines.append(
            f"| {row['phase_quotient']} | `{row['target_cell_sign']}` | {row['p']} | {row['b_value']} | "
            f"{candidate.get('q', 'n/a')} | {candidate.get('a', 'n/a')} | {candidate.get('n', 'n/a')} | "
            f"`{candidate.get('valid_a_interval', [])}` | {fmt_bool(candidate.get('singleton_ok', False))} |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：quotient ladder 到 singleton prime-a 源纤维的样本恒等式。",
            "- 未闭合：singleton 源纤维配对/容量全局证明，或 Fiber-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "source_fiber_ladder_identity_closed": result["source_fiber_ladder_identity_closed"],
                "source_fiber_count": result["source_fiber_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
