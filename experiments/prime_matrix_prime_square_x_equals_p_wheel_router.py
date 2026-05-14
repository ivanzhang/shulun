#!/usr/bin/env python3
"""生成 x=P 特化轮序 gcd 方程组审查证书。

用法示例：
  python3 experiments/prime_matrix_prime_square_x_equals_p_wheel_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-prime-square-x-equals-p-wheel-router.json

输出：
  data/prime-square-x-equals-p-wheel-sample-ledger.json
  docs/monograph/prime-matrix-prime-square-x-equals-p-wheel-router.json
  docs/monograph/prime-matrix-prime-square-x-equals-p-wheel-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
OUT_LEDGER = DATA / "prime-square-x-equals-p-wheel-sample-ledger.json"
OUT_JSON = DOCS / "prime-matrix-prime-square-x-equals-p-wheel-router.json"
OUT_MD = DOCS / "prime-matrix-prime-square-x-equals-p-wheel-router.md"

FIRST_HALF = "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP"
SQUARE_PHASE = "SquarePhaseRoughSurvivorUniformLowerBound"
NONFINAL = "NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction"


def sieve(limit: int) -> bytearray:
    """筛出 limit 以内素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int | None = None) -> list[int]:
    """从素数表提取素数。"""
    end = len(flags) if limit is None else min(limit + 1, len(flags))
    return [idx for idx in range(2, end) if flags[idx]]


def is_prime_trial(n: int, primes: list[int]) -> bool:
    """用已有素数表试除判定样本素性。"""
    if n < 2:
        return False
    for q in primes:
        if q * q > n:
            return True
        if n % q == 0:
            return n == q
    return True


def wheel_survivors(p: int, primes: list[int]) -> tuple[list[int], dict[int, int]]:
    """计算 r in [1,p) 中未被 q<p 的平方相位禁类覆盖的列。"""
    covered = bytearray(p)
    hit_counts: dict[int, int] = {}
    p2 = p * p
    for q in primes:
        if q >= p:
            break
        residue = (-p2) % q
        if residue == 0:
            residue = q
        count = 0
        for r in range(residue, p, q):
            covered[r] = 1
            count += 1
        hit_counts[q] = count
    survivors = [r for r in range(1, p) if not covered[r]]
    return survivors, hit_counts


def canonical_gcd_covers(p: int, r: int, primes: list[int]) -> bool:
    """检查 canonical k=P-q 的 gcd 方程是否覆盖 r。"""
    for q in primes:
        if q >= p:
            break
        if gcd((p - q) * p + r, q) == q:
            return True
    return False


def full_wheel_covers(p: int, r: int) -> bool:
    """检查用户轮序 k=0..P-2 中是否存在非平凡 gcd。"""
    return any(gcd(k * p + r, p - k) > 1 for k in range(0, p - 1))


def audit_p(p: int, primes: list[int], check_full_wheel: bool) -> dict[str, Any]:
    """审计单个素数 P 的 x=P 轮序覆盖。"""
    survivors, hit_counts = wheel_survivors(p, primes)
    survivor_prime_flags = {str(r): is_prime_trial(p * p + r, primes) for r in survivors}
    canonical_mismatches = [
        r
        for r in range(1, p)
        if canonical_gcd_covers(p, r, primes) == (r in survivors)
    ]
    full_wheel_mismatches = []
    if check_full_wheel:
        full_wheel_mismatches = [
            r
            for r in range(1, p)
            if full_wheel_covers(p, r) == (r in survivors)
        ]
    least_survivor = survivors[0] if survivors else None
    return {
        "p": p,
        "survivor_count": len(survivors),
        "least_survivor_r": least_survivor,
        "least_survivor_value": None if least_survivor is None else p * p + least_survivor,
        "least_survivor_is_prime": None if least_survivor is None else survivor_prime_flags[str(least_survivor)],
        "first_survivors": survivors[:20],
        "survivor_prime_flags": survivor_prime_flags,
        "canonical_gcd_equivalence_mismatch_count": len(canonical_mismatches),
        "canonical_gcd_equivalence_mismatches": canonical_mismatches[:20],
        "full_wheel_equivalence_mismatch_count": len(full_wheel_mismatches),
        "full_wheel_equivalence_mismatches": full_wheel_mismatches[:20],
        "full_wheel_checked": check_full_wheel,
        "coverage_by_small_q": {str(q): hit_counts[q] for q in sorted(hit_counts)[:12]},
        "tail_coverage_by_large_q": {str(q): hit_counts[q] for q in sorted(hit_counts)[-8:]},
    }


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def theorem_rows() -> list[dict[str, str]]:
    """列出 x=P 特化后的等价链。"""
    return [
        {
            "name": "canonical_wheel_equivalence",
            "status": "closed",
            "statement": "对 q<P，q | P^2+r 当且仅当 gcd((P-q)P+r,q)=q。",
        },
        {
            "name": "full_wheel_redundancy",
            "status": "closed",
            "statement": "用户轮序 gcd(kP+r,P-k)>1 与小素因子覆盖等价；canonical k=P-q 是最小无冗余子系统。",
        },
        {
            "name": "exact_gcd_q_scope",
            "status": "closed",
            "statement": "若在复合模 P-k 上写 gcd(...)=q 会漏掉 gcd 为复合数的覆盖；精确等号 q 应锚定在 canonical 模数 P-k=q。",
        },
        {
            "name": "uncovered_is_prime",
            "status": "closed",
            "statement": "若 1<=r<P 未被任何 q<P 覆盖，则 P^2+r 不能合成；否则其最小素因子必须小于 P。",
        },
        {
            "name": "x_equals_P_no_solution_equivalence",
            "status": "target_equivalent_open",
            "statement": "证明 x=P 时轮序系统不能覆盖所有 r，正等价于证明 (P^2,P^2+P) 内有素数。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "XEqualsPCanonicalWheelEquivalenceChecked",
            "closed": result["canonical_equivalence_checked"],
            "proved": True,
            "meaning": "canonical 方程 gcd((P-q)P+r,q)=q 与 q|P^2+r 完全一致。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteXEqualsPWheelNoFullCoverChecked",
            "closed": result["finite_failure_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 未出现 x=P 全覆盖。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "XEqualsPNoSolutionGlobalProved",
            "closed": False,
            "proved": False,
            "meaning": "x=P 无解就是平方后前半窗素数命题本身；当前未给出全局证明。",
            "remaining": FIRST_HALF,
        },
        {
            "gate": "SquarePhaseAttackPointIsolated",
            "closed": True,
            "proved": False,
            "meaning": "真正新信息不是任意 x，而是 P^2 在所有小模上的负平方相位刚性。",
            "remaining": SQUARE_PHASE,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步完成等价链和有限证据，不闭合最终命题。",
            "remaining": f"{SQUARE_PHASE} OR {NONFINAL}",
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造 x=P 轮序证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    prime_flags = sieve(max_p * max_p + max_p)
    primes = primes_from_flags(prime_flags, max_p * max_p + max_p)
    small_primes = [p for p in primes if p <= max_p]
    target_ps = [p for p in small_primes if p >= 3]
    sample_set = set(sample_ps)
    records = [audit_p(p, primes, p in sample_set) for p in target_ps]
    sample_records = [record for record in records if record["p"] in sample_set]
    failures = [record for record in records if record["survivor_count"] == 0]
    canonical_bad = [record for record in records if record["canonical_gcd_equivalence_mismatch_count"]]
    full_bad = [
        record
        for record in records
        if record["full_wheel_checked"] and record["full_wheel_equivalence_mismatch_count"]
    ]
    worst_survivor = min(records, key=lambda item: item["survivor_count"], default=None)
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(target_ps),
        "finite_failure_count": len(failures),
        "canonical_bad_count": len(canonical_bad),
        "full_wheel_checked_count": sum(1 for record in records if record["full_wheel_checked"]),
        "full_wheel_bad_count": len(full_bad),
        "worst_survivor_record": worst_survivor,
        "sample_records": sample_records,
        "failure_records": failures,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_prime_square_x_equals_p_wheel_router",
        "status": "x_equals_p_wheel_equivalence_closed_global_no_cover_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "canonical_equivalence_checked": len(canonical_bad) == 0,
        "full_wheel_equivalence_checked": len(full_bad) == 0,
        "full_wheel_checked_count": ledger["full_wheel_checked_count"],
        "finite_failure_count": len(failures),
        "x_equals_p_no_solution_global_proved": False,
        "square_phase_rigidity_attack_target_identified": True,
        "first_half_prime_square_input_current_corpus_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": FIRST_HALF,
        "hardpoint_after_router": f"{SQUARE_PHASE} OR {NONFINAL}",
        "next_direct_attack_target": SQUARE_PHASE,
        "parallel_attack_targets": [NONFINAL],
        "parameters": ledger["parameters"],
        "finite_prime_count": ledger["prime_count"],
        "worst_survivor_record": worst_survivor,
        "sample_records": sample_records,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_prime_square_x_equals_p_wheel_router.py": sha256(Path(__file__).resolve()),
            "data/prime-square-x-equals-p-wheel-sample-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "`x=P` 特化后，用户给出的轮序 gcd 系统有一个无冗余 canonical 子系统："
            "`gcd((P-q)P+r,q)=q`。它与 `q|P^2+r` 完全等价；"
            "若使用复合模 `P-k`，安全条件应写成 `gcd(kP+r,P-k)>1`，"
            "而精确等号 `=q` 要落在 canonical 模数 `P-k=q` 上。"
            "若某个 `r` 未被所有 `q<P` 覆盖，则 `P^2+r` 必为素数。"
            "因此“`x=P` 时方程组无全覆盖解”不是额外弱命题，而正是平方后前半窗素数命题。"
            "本步把等价链和有限样本固定下来；全局突破仍需 square-phase 粗幸存下界或 PDEC/SAE 矛盾。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix x=P 特化轮序 gcd 方程组路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"finite_failure_count={result['finite_failure_count']}",
        f"canonical_equivalence_checked={fmt_bool(result['canonical_equivalence_checked'])}",
        f"full_wheel_checked_count={result['full_wheel_checked_count']}",
        f"x_equals_p_no_solution_global_proved={fmt_bool(result['x_equals_p_no_solution_global_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 等价链",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")
    lines.extend(
        [
            "",
            "## 2. 样本记录",
            "",
            "| P | survivors | least r | P^2+r | prime | canonical mismatch | full wheel mismatch |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["sample_records"]:
        lines.append(
            f"| {item['p']} | {item['survivor_count']} | {item['least_survivor_r']} | "
            f"{item['least_survivor_value']} | `{fmt_bool(item['least_survivor_is_prime'])}` | "
            f"{item['canonical_gcd_equivalence_mismatch_count']} | {item['full_wheel_equivalence_mismatch_count']} |"
        )
    worst = result["worst_survivor_record"]
    lines.extend(
        [
            "",
            "## 3. 最小幸存样本",
            "",
            f"- `P={worst['p']}`，未覆盖列数 `{worst['survivor_count']}`，最小未覆盖 `r={worst['least_survivor_r']}`，对应素数 `{worst['least_survivor_value']}`。",
            "",
            "## 4. 判定表",
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
            "## 5. 下一步",
            "",
            f"- 主攻 `{SQUARE_PHASE}`：利用 `r=-P^2 mod q` 的负平方相位，证明长度 `P` 内存在未覆盖列。",
            f"- 若 square-phase 全覆盖被假设成立，则必须把覆盖相位异常登记到 `{NONFINAL}`，寻找 PDEC/SAE/预算矛盾。",
            "",
            "## 6. 依赖哈希",
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument(
        "--sample-ps",
        default="13,17,19,23,29,31,101,499,1009,2003,4999",
    )
    args = parser.parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": result["parameters"]["max_p"],
                "finite_failure_count": result["finite_failure_count"],
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
