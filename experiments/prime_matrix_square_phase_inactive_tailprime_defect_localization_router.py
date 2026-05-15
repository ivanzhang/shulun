#!/usr/bin/env python3
"""定位平方锚 inactive tail-prime 缺陷的两个原子来源。

用法示例：
  python3 experiments/prime_matrix_square_phase_inactive_tailprime_defect_localization_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-inactive-tailprime-defect-localization-router.json

输出：
  data/square-phase-inactive-tailprime-defect-localization-ledger.json
  docs/monograph/prime-matrix-square-phase-inactive-tailprime-defect-localization-router.json
  docs/monograph/prime-matrix-square-phase-inactive-tailprime-defect-localization-router.md
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

OUT_LEDGER = DATA / "square-phase-inactive-tailprime-defect-localization-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-inactive-tailprime-defect-localization-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-inactive-tailprime-defect-localization-router.md"

MAIN_TARGET = "PrimeWindowCountBeatsInactiveTailPrimeCount"
NO_SLOT_TARGET = "NoSlotTailPrimePhaseBandDefectPDECSAE"
COMPOSITE_TARGET = "CompositeSlotCofactorDefectPDECSAE"


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


def smallest_prime_factor(n_value: int, primes: list[int]) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    for q_value in primes:
        if q_value * q_value > n_value:
            return n_value
        if n_value % q_value == 0:
            return q_value
    return n_value


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


def ceil_div(numerator: int, denominator: int) -> int:
    """整数向上取整，允许 numerator 为负。"""
    return -((-numerator) // denominator)


def layer_interval_for_b(p: int, b_value: int, sign: str) -> tuple[int, int]:
    """返回固定 b 时 u 的精确可行区间。"""
    half = (p - 1) // 2
    q_value = p - 2 * b_value
    base = 2 * b_value * b_value
    if sign == "plus":
        return ceil_div(base + 1, q_value), (base + half) // q_value
    if sign == "minus":
        return max(0, ceil_div(base - half, q_value)), (base - 1) // q_value
    raise ValueError(f"unknown sign: {sign}")


def tail_phase_gap(p: int, b_value: int, sign: str) -> int:
    """返回判断无槽的相位 gap，范围为 1..q。"""
    q_value = p - 2 * b_value
    base_mod = (2 * b_value * b_value) % q_value
    if sign == "plus":
        return q_value - base_mod if base_mod else q_value
    if sign == "minus":
        return base_mod if base_mod else q_value
    raise ValueError(f"unknown sign: {sign}")


def raw_slot_values(p: int, q_value: int, sign: str) -> list[dict[str, int]]:
    """返回尾素 q 的原始槽列表。"""
    b_value = (p - q_value) // 2
    u_min, u_max = layer_interval_for_b(p, b_value, sign)
    result = []
    for u_value in range(u_min, u_max + 1):
        m_value = p + 2 * (b_value + u_value)
        result.append({"u": u_value, "m": m_value})
    return result


def cover_residue(p: int, q: int, sign: str) -> int:
    """返回 r 坐标中被 q 覆盖的唯一正残基。"""
    p2_mod = (p * p) % q
    residue = (-p2_mod) % q if sign == "plus" else p2_mod
    return q if residue == 0 else residue


def low_survivor_count(p: int, cutoff: int, sign: str, primes: list[int]) -> int:
    """计算低筛幸存列 H。"""
    covered = bytearray(p)
    for q_value in primes:
        if q_value >= p or q_value > cutoff:
            break
        residue = cover_residue(p, q_value, sign)
        for r_value in range(residue, p, q_value):
            covered[r_value] = 1
    return sum(1 for r_value in range(1, p) if not covered[r_value])


def square_prime_count(p: int, sign: str, prime_flags: bytearray) -> int:
    """计算 P^2 正负半窗内的素数个数。"""
    base = p * p
    total = 0
    for r_value in range(1, p):
        n_value = base + r_value if sign == "plus" else base - r_value
        if prime_flags[n_value]:
            total += 1
    return total


def audit_sign(p: int, sign: str, primes: list[int], prime_flags: bytearray) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    cutoff = cutoff_alpha45(p)
    half = (p - 1) // 2
    tail_primes = [q for q in primes if cutoff < q < p]
    low_count = low_survivor_count(p, cutoff, sign, primes)
    prime_count = square_prime_count(p, sign, prime_flags)

    good_slots = 0
    no_slot = 0
    composite_slot = 0
    phase_band_failures = 0
    multi_slot_failures = 0
    lpf_bound_failures = 0
    max_cofactor = 0
    max_cofactor_ratio = 0.0
    lpf_histogram: dict[str, int] = {}
    no_slot_samples: list[dict[str, int]] = []
    composite_samples: list[dict[str, int]] = []

    for q_value in tail_primes:
        b_value = (p - q_value) // 2
        phase_gap = tail_phase_gap(p, b_value, sign)
        raw_slots = raw_slot_values(p, q_value, sign)
        phase_says_no_slot = phase_gap > half
        actual_no_slot = len(raw_slots) == 0
        if phase_says_no_slot != actual_no_slot:
            phase_band_failures += 1
        if len(raw_slots) > 1:
            multi_slot_failures += 1

        if actual_no_slot:
            no_slot += 1
            if len(no_slot_samples) < 8:
                no_slot_samples.append({"q": q_value, "b": b_value, "phase_gap": phase_gap})
            continue

        # 中文注释：单槽屏障已闭合，若出现多槽也只逐槽计入有限诊断。
        slot_has_prime = False
        for slot in raw_slots:
            m_value = slot["m"]
            max_cofactor = max(max_cofactor, m_value)
            max_cofactor_ratio = max(max_cofactor_ratio, m_value / p)
            if prime_flags[m_value]:
                good_slots += 1
                slot_has_prime = True
            else:
                lpf = smallest_prime_factor(m_value, primes)
                if lpf * lpf > m_value:
                    lpf_bound_failures += 1
                lpf_histogram[str(lpf)] = lpf_histogram.get(str(lpf), 0) + 1
                if len(composite_samples) < 8:
                    composite_samples.append(
                        {
                            "q": q_value,
                            "b": b_value,
                            "u": slot["u"],
                            "m": m_value,
                            "lpf": lpf,
                        }
                    )
        if not slot_has_prime:
            composite_slot += 1

    inactive_tail = no_slot + composite_slot
    partition_delta = len(tail_primes) - good_slots - inactive_tail
    prime_inactive_margin = prime_count - inactive_tail
    defect_threshold = (prime_count + 1) // 2
    no_slot_large_branch = no_slot >= defect_threshold
    composite_large_branch = composite_slot >= defect_threshold
    failure_would_force_branch = True
    if prime_count <= inactive_tail:
        failure_would_force_branch = no_slot_large_branch or composite_large_branch

    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "tail_prime_count": len(tail_primes),
        "low_survivors": low_count,
        "prime_window_count": prime_count,
        "good_slots": good_slots,
        "inactive_tail_primes": inactive_tail,
        "no_slot_tail_primes": no_slot,
        "composite_slot_tail_primes": composite_slot,
        "partition_delta": partition_delta,
        "prime_minus_inactive": prime_inactive_margin,
        "phase_band_failures": phase_band_failures,
        "multi_slot_failures": multi_slot_failures,
        "lpf_bound_failures": lpf_bound_failures,
        "max_cofactor": max_cofactor,
        "max_cofactor_ratio": max_cofactor_ratio,
        "lpf_histogram": dict(sorted(lpf_histogram.items(), key=lambda item: int(item[0]))),
        "defect_threshold_half_primewindow": defect_threshold,
        "no_slot_large_branch": no_slot_large_branch,
        "composite_large_branch": composite_large_branch,
        "failure_would_force_branch": failure_would_force_branch,
        "no_slot_samples": no_slot_samples,
        "composite_samples": composite_samples,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "inactive_partition_identity",
            "status": "closed",
            "statement": "InactiveTailPrime=NoSlotTailPrime+CompositeSlotTailPrime.",
        },
        {
            "name": "no_slot_phase_band",
            "status": "closed",
            "statement": "For q=P-2b, no-slot is exactly the phase condition delta_sign(b)>floor((P-1)/2).",
        },
        {
            "name": "composite_slot_lpf_certificate",
            "status": "closed",
            "statement": "Every composite-slot inactive tail prime has a concrete cofactor m=P+2(b+u) and LPF ell<=sqrt(m).",
        },
        {
            "name": "prime_inactive_failure_dichotomy",
            "status": "closed",
            "statement": "If PrimeWindow<=InactiveTailPrime, then NoSlotTailPrime>=PrimeWindow/2 or CompositeSlotTailPrime>=PrimeWindow/2.",
        },
        {
            "name": "defect_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude the no-slot phase-band branch and the composite cofactor branch.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "InactivePartitionClosed",
            "closed": result["partition_failure_count"] == 0,
            "proved": True,
            "meaning": "未激活尾素被无损拆成无槽尾素与复合余因子尾素。",
            "remaining": "closed",
        },
        {
            "gate": "NoSlotPhaseBandClosed",
            "closed": result["phase_band_failure_count"] == 0,
            "proved": True,
            "meaning": "无槽条件已化为单个二次相位 gap 落入上半带。",
            "remaining": "closed",
        },
        {
            "gate": "CompositeLPFCertificateClosed",
            "closed": result["lpf_bound_failure_count"] == 0,
            "proved": True,
            "meaning": "复合余因子槽都有最小素因子证书。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoPrimeInactiveFailure",
            "closed": result["finite_prime_inactive_failure_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 未出现 PrimeWindow<=InactiveTail。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "NoSlotDefectBranchExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需排斥无槽相位带大到可吞掉半数 PrimeWindow 的分支。",
            "remaining": NO_SLOT_TARGET,
        },
        {
            "gate": "CompositeSlotDefectBranchExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需排斥复合余因子槽大到可吞掉半数 PrimeWindow 的分支。",
            "remaining": COMPOSITE_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只定位缺陷原子，不关闭全局行/列命题。",
            "remaining": f"{NO_SLOT_TARGET} AND {COMPOSITE_TARGET}",
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)

    prime_flags = sieve(max_p * max_p + max_p)
    primes = primes_from_flags(prime_flags, max_p * max_p + max_p)
    small_primes = primes_from_flags(prime_flags, max_p)
    p_values = [p for p in small_primes if 3 <= p <= max_p]
    records: list[dict[str, Any]] = []
    for p in p_values:
        records.append(audit_sign(p, "plus", small_primes, prime_flags))
        records.append(audit_sign(p, "minus", small_primes, prime_flags))

    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    partition_failures = [record for record in records if record["partition_delta"] != 0]
    phase_band_failures = [record for record in records if record["phase_band_failures"]]
    multi_slot_failures = [record for record in records if record["multi_slot_failures"]]
    lpf_bound_failures = [record for record in records if record["lpf_bound_failures"]]
    prime_inactive_failures = [record for record in records if record["prime_minus_inactive"] <= 0]
    branch_failures = [record for record in prime_inactive_failures if not record["failure_would_force_branch"]]
    worst_margin = min(records, key=lambda item: item["prime_minus_inactive"], default=None)
    worst_margin_ge_23 = min(
        [record for record in records if record["p"] >= 23],
        key=lambda item: item["prime_minus_inactive"],
        default=None,
    )

    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    aggregate = {
        "plus_prime_window": sum(record["prime_window_count"] for record in plus_records),
        "plus_inactive_tail_primes": sum(record["inactive_tail_primes"] for record in plus_records),
        "plus_no_slot_tail_primes": sum(record["no_slot_tail_primes"] for record in plus_records),
        "plus_composite_slot_tail_primes": sum(
            record["composite_slot_tail_primes"] for record in plus_records
        ),
        "minus_prime_window": sum(record["prime_window_count"] for record in minus_records),
        "minus_inactive_tail_primes": sum(record["inactive_tail_primes"] for record in minus_records),
        "minus_no_slot_tail_primes": sum(record["no_slot_tail_primes"] for record in minus_records),
        "minus_composite_slot_tail_primes": sum(
            record["composite_slot_tail_primes"] for record in minus_records
        ),
    }
    aggregate["combined_prime_window"] = aggregate["plus_prime_window"] + aggregate["minus_prime_window"]
    aggregate["combined_inactive_tail_primes"] = (
        aggregate["plus_inactive_tail_primes"] + aggregate["minus_inactive_tail_primes"]
    )
    aggregate["combined_no_slot_tail_primes"] = (
        aggregate["plus_no_slot_tail_primes"] + aggregate["minus_no_slot_tail_primes"]
    )
    aggregate["combined_composite_slot_tail_primes"] = (
        aggregate["plus_composite_slot_tail_primes"]
        + aggregate["minus_composite_slot_tail_primes"]
    )

    combined_lpf_histogram: dict[str, int] = {}
    for record in records:
        for key, value in record["lpf_histogram"].items():
            combined_lpf_histogram[key] = combined_lpf_histogram.get(key, 0) + value
    top_lpf_histogram = dict(
        sorted(combined_lpf_histogram.items(), key=lambda item: (-item[1], int(item[0])))[:12]
    )

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "partition_failure_count": len(partition_failures),
        "phase_band_failure_count": len(phase_band_failures),
        "multi_slot_failure_count": len(multi_slot_failures),
        "lpf_bound_failure_count": len(lpf_bound_failures),
        "finite_prime_inactive_failure_count": len(prime_inactive_failures),
        "failure_branch_logic_failure_count": len(branch_failures),
        "worst_prime_minus_inactive_record": worst_margin,
        "worst_prime_minus_inactive_record_ge_23": worst_margin_ge_23,
        "top_lpf_histogram": top_lpf_histogram,
        "sample_records": sample_records,
        "partition_failures": partition_failures[:20],
        "phase_band_failures": phase_band_failures[:20],
        "multi_slot_failures": multi_slot_failures[:20],
        "lpf_bound_failures": lpf_bound_failures[:20],
        "prime_inactive_failures": prime_inactive_failures[:20],
        "branch_failures": branch_failures[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_inactive_tailprime_defect_localization_router",
        "status": "inactive_tailprime_defect_localized_to_no_slot_or_composite_slot_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "partition_failure_count": len(partition_failures),
        "phase_band_failure_count": len(phase_band_failures),
        "multi_slot_failure_count": len(multi_slot_failures),
        "lpf_bound_failure_count": len(lpf_bound_failures),
        "finite_prime_inactive_failure_count": len(prime_inactive_failures),
        "failure_branch_logic_failure_count": len(branch_failures),
        "worst_prime_minus_inactive_record": worst_margin,
        "worst_prime_minus_inactive_record_ge_23": worst_margin_ge_23,
        "top_lpf_histogram": top_lpf_histogram,
        "sample_records": sample_records,
        "inactive_partition_identity_closed": len(partition_failures) == 0,
        "no_slot_phase_band_closed": len(phase_band_failures) == 0,
        "composite_slot_lpf_certificate_closed": len(lpf_bound_failures) == 0,
        "prime_inactive_failure_dichotomy_closed": len(branch_failures) == 0,
        "no_slot_defect_branch_excluded": False,
        "composite_slot_defect_branch_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": f"{NO_SLOT_TARGET} AND {COMPOSITE_TARGET}",
        "next_direct_attack_target": NO_SLOT_TARGET,
        "alternative_attack_target": COMPOSITE_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_inactive_tailprime_defect_localization_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-inactive-tailprime-defect-localization-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 `PrimeWindowCountBeatsInactiveTailPrimeCount` 的反例态进一步定位："
            "未激活尾素不是单一黑箱，而是无槽相位带命中与复合余因子槽两类原子。"
            "对尾素 `q=P-2b`，无槽当且仅当二次相位 gap `delta_sign(b)` 超过半窗；"
            "有槽但未激活则给出 `m=P+2(b+u)` 的复合余因子及 LPF 证书。"
            "因此若 `PrimeWindow<=InactiveTailPrime`，必有无槽相位带或复合余因子槽之一至少达到半个 `PrimeWindow`。"
            "这仍不是全局闭合；下一步必须排斥这两个命名缺陷分支。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    worst = result["worst_prime_minus_inactive_record"]
    worst_ge_23 = result["worst_prime_minus_inactive_record_ge_23"]
    lines = [
        "# Prime Matrix square-phase inactive tail-prime defect localization",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"partition_failure_count={result['partition_failure_count']}",
        f"phase_band_failure_count={result['phase_band_failure_count']}",
        f"multi_slot_failure_count={result['multi_slot_failure_count']}",
        f"lpf_bound_failure_count={result['lpf_bound_failure_count']}",
        f"finite_prime_inactive_failure_count={result['finite_prime_inactive_failure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 两类原子",
        "",
        "对尾素 `q=P-2b`，固定 `b` 的槽至多一个。未激活尾素精确拆成",
        "",
        "```text",
        "InactiveTailPrime = NoSlotTailPrime + CompositeSlotTailPrime.",
        "```",
        "",
        "无槽条件是单个二次相位带条件。令 `h=(P-1)/2`，",
        "",
        "```text",
        "delta_plus(b)  = least positive residue of -2b^2 mod q",
        "delta_minus(b) = least positive residue of  2b^2 mod q",
        "NoSlot iff delta_sign(b)>h.",
        "```",
        "",
        "若有槽但余因子不是素数，则该尾素登记为复合槽缺陷：",
        "",
        "```text",
        "m=P+2(b+u),  ell=P^-(m)<=sqrt(m).",
        "```",
        "",
        "## 2. 反例二分",
        "",
        "若反例态满足",
        "",
        "```text",
        "PrimeWindow <= InactiveTailPrime = NoSlotTailPrime + CompositeSlotTailPrime,",
        "```",
        "",
        "则至少一个分支满足",
        "",
        "```text",
        "NoSlotTailPrime >= PrimeWindow/2",
        "或 CompositeSlotTailPrime >= PrimeWindow/2.",
        "```",
        "",
        "这把终端缺陷固定为两类可审计相位对象。",
        "",
        "## 3. 命题行",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    agg = result["aggregate"]
    lines.extend(
        [
            "",
            "## 4. 有限审计摘要",
            "",
            "| metric | plus | minus | combined |",
            "| --- | ---: | ---: | ---: |",
            f"| PrimeWindow | {agg['plus_prime_window']} | {agg['minus_prime_window']} | {agg['combined_prime_window']} |",
            f"| InactiveTailPrime | {agg['plus_inactive_tail_primes']} | {agg['minus_inactive_tail_primes']} | {agg['combined_inactive_tail_primes']} |",
            f"| NoSlotTailPrime | {agg['plus_no_slot_tail_primes']} | {agg['minus_no_slot_tail_primes']} | {agg['combined_no_slot_tail_primes']} |",
            f"| CompositeSlotTailPrime | {agg['plus_composite_slot_tail_primes']} | {agg['minus_composite_slot_tail_primes']} | {agg['combined_composite_slot_tail_primes']} |",
            "",
            f"全扫描最紧 `PrimeWindow-InactiveTail`：`P={worst['p']}`，`sign={worst['sign']}`，`PrimeWindow={worst['prime_window_count']}`，`InactiveTail={worst['inactive_tail_primes']}`，`margin={worst['prime_minus_inactive']}`。",
            f"`P>=23` 最紧样本：`P={worst_ge_23['p']}`，`sign={worst_ge_23['sign']}`，`PrimeWindow={worst_ge_23['prime_window_count']}`，`InactiveTail={worst_ge_23['inactive_tail_primes']}`，`margin={worst_ge_23['prime_minus_inactive']}`。",
            "",
            "最常见复合槽 LPF：",
            "",
            "| LPF | count |",
            "| ---: | ---: |",
        ]
    )
    for lpf, count in result["top_lpf_histogram"].items():
        lines.append(f"| {lpf} | {count} |")

    lines.extend(
        [
            "",
            "## 5. 样本表",
            "",
            "| P | sign | PrimeWindow | inactive | no-slot | composite | margin | threshold | no-slot>=thr | comp>=thr |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['prime_window_count']} | "
            f"{row['inactive_tail_primes']} | {row['no_slot_tail_primes']} | "
            f"{row['composite_slot_tail_primes']} | {row['prime_minus_inactive']} | "
            f"{row['defect_threshold_half_primewindow']} | `{fmt_bool(row['no_slot_large_branch'])}` | "
            f"`{fmt_bool(row['composite_large_branch'])}` |"
        )

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
            f"- 备选：`{result['alternative_attack_target']}`。",
            "- 当前仍不能宣称全局无条件闭合；必须排斥这两个缺陷分支，或接入足够强的平方端点素数下界。",
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
                "partition_failure_count": result["partition_failure_count"],
                "phase_band_failure_count": result["phase_band_failure_count"],
                "lpf_bound_failure_count": result["lpf_bound_failure_count"],
                "finite_prime_inactive_failure_count": result["finite_prime_inactive_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
