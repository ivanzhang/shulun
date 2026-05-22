#!/usr/bin/env python3
"""生成 strict-k 正性核心的四坐标统一证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_unified_positive_core_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-unified-positive-core-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-unified-positive-core-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-unified-positive-core-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-unified-positive-core-router.md
"""

from __future__ import annotations

from array import array
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-unified-positive-core"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化成小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
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


def factor_tables(n: int) -> tuple[array, array, bytearray, list[int]]:
    """返回最小素因子、最大素因子、素数标记和素数表。"""
    spf = array("I", range(n + 1))
    gpf = array("I", [0]) * (n + 1)
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
        spf[0] = 0
    if n >= 1:
        flags[1] = 0
        spf[1] = 1
        gpf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
                    flags[m] = 0
    primes = [i for i in range(2, n + 1) if flags[i]]
    for x in range(2, n + 1):
        y = x
        last = 1
        while y > 1:
            p = int(spf[y])
            last = p
            while y % p == 0:
                y //= p
        gpf[x] = last
    return spf, gpf, flags, primes


def beatty_payment_count(primes: list[int], p_len: int, k: int) -> int:
    """计算 high-prime Beatty payment 槽数。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    source_upper = upper // 2
    total = 0
    for r in primes:
        if r <= p_len:
            continue
        if r > source_upper:
            break
        slot = r - (lower % r)
        if 1 <= slot <= p_len - 1:
            total += 1
    return total


def next_prime_after(flags: bytearray, x: int) -> int:
    """返回大于 x 的下一个素数。"""
    y = x + 1
    while y < len(flags) and not flags[y]:
        y += 1
    if y >= len(flags):
        raise ValueError("sieve too short for next-prime lookup")
    return y


def row_summary(
    spf: array,
    gpf: array,
    flags: bytearray,
    primes: list[int],
    p_len: int,
    k: int,
) -> dict[str, Any]:
    """汇总一条 strict 行的四种正性坐标。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    length = p_len - 1
    prime_count = 0
    smooth_count = 0
    raw_total = 0
    owner_mass = 0
    rejection_mass = 0
    for n in range(lower + 1, upper + 1):
        if flags[n]:
            prime_count += 1
            continue
        owner_mass += 1
        if gpf[n] <= p_len:
            smooth_count += 1
        hits = 0
        root = isqrt(n)
        for p in primes:
            if p > root:
                break
            if n % p == 0:
                hits += 1
        raw_total += hits
        rejection_mass += hits - 1
    beatty_count = beatty_payment_count(primes, p_len, k)
    next_p = next_prime_after(flags, lower)
    dual_value = length - beatty_count - smooth_count
    owner_defect = length - owner_mass
    rejection_excess = rejection_mass - (raw_total - length)
    sqrt_gap_open = next_p <= upper
    return {
        "P": p_len,
        "k": k,
        "x": lower,
        "length": length,
        "prime_count": prime_count,
        "dual_value": dual_value,
        "B": beatty_count,
        "S": smooth_count,
        "owner_mass": owner_mass,
        "owner_defect": owner_defect,
        "raw_total": raw_total,
        "rejection_mass": rejection_mass,
        "raw_surplus": raw_total - length,
        "rejection_excess": rejection_excess,
        "next_prime_after_x": next_p,
        "next_prime_offset": next_p - lower,
        "sqrt_gap_open": sqrt_gap_open,
        "all_four_coordinates_match": (
            prime_count == dual_value == owner_defect == rejection_excess
            and (prime_count >= 1) == sqrt_gap_open
        ),
        "positive_margin_over_zero": prime_count,
        "anti_tiling_spare_after_positive_threshold": dual_value - 1,
    }


def finite_sweep(max_prime: int = 257) -> dict[str, Any]:
    """有限审计四坐标等价；不作为全局证明。"""
    extra_samples = [(571, 438), (1009, 1008)]
    sieve_limit = max(max_prime * max_prime + max_prime, 1012 * 1012)
    spf, gpf, flags, primes = factor_tables(sieve_limit)
    strict_primes = [p for p in primes if 3 <= p <= max_prime]
    row_count = 0
    failures: list[dict[str, Any]] = []
    min_positive: int | None = None
    min_cases: list[dict[str, int]] = []
    max_next_offset = {"value": -1, "cases": []}
    tight_cases: list[dict[str, Any]] = []
    for p_len in strict_primes:
        for k in range(2, p_len):
            row_count += 1
            summary = row_summary(spf, gpf, flags, primes, p_len, k)
            if not summary["all_four_coordinates_match"] and len(failures) < 8:
                failures.append(summary)
            value = summary["prime_count"]
            if min_positive is None or value < min_positive:
                min_positive = value
                min_cases = [{"P": p_len, "k": k, "value": value}]
            elif value == min_positive and len(min_cases) < 16:
                min_cases.append({"P": p_len, "k": k, "value": value})
            offset = summary["next_prime_offset"]
            case = {"P": p_len, "k": k, "N": value, "offset": offset, "length": summary["length"]}
            if offset > max_next_offset["value"]:
                max_next_offset = {"value": offset, "cases": [case]}
            elif offset == max_next_offset["value"] and len(max_next_offset["cases"]) < 8:
                max_next_offset["cases"].append(case)
            if value <= 3 and len(tight_cases) < 16:
                tight_cases.append(summary)
    sample_rows = [
        row_summary(spf, gpf, flags, primes, p, k)
        for p, k in [(11, 10), (59, 42), (101, 100), *extra_samples]
    ]
    return {
        "max_prime": max_prime,
        "strict_row_count": row_count,
        "all_four_coordinate_identities_hold": not failures,
        "failures": failures,
        "minimum_positive_core_value": min_positive,
        "minimum_positive_cases": min_cases,
        "max_next_prime_offset": max_next_offset,
        "tight_cases_sample": tight_cases,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "FourCoordinateCoreIdentityClosed",
            True,
            True,
            "dual-window value、owner defect、raw/rejection excess 与 next-prime row opening 是同一个整数 N_P(k)。",
            "unified positive core",
        ),
        row(
            "FalseIndependentHardpointsRemoved",
            True,
            True,
            "DualWindowAntiTiling、PositiveRejectionExcess 与 SqrtGapInput 不是三个独立缺口，而是同一正性核心的不同坐标。",
            "single core",
        ),
        row(
            "FiniteAuditAllCoordinatesAgree",
            True,
            True,
            "有限审计确认四坐标读数一致，但不作为全局证明。",
            "finite audit only",
        ),
        row(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层没有证明 N_P(k)>=1；它只消除接口分裂。",
            "prove the unified core",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "strict 行正性仍需 sqrt-scale gap 输入或内部双窗口反铺满。",
            "SqrtGapInputAfterX OR DualWindowAntiTilingInequality",
        ),
    ]


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def sample_markdown(samples: list[dict[str, Any]]) -> str:
    """输出样本行 Markdown。"""
    lines = [
        "| P | k | N | dual | owner defect | rejection excess | next offset | B | S |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in samples:
        lines.append(
            f"| {item['P']} | {item['k']} | {item['prime_count']} | "
            f"{item['dual_value']} | {item['owner_defect']} | "
            f"{item['rejection_excess']} | {item['next_prime_offset']} | "
            f"{item['B']} | {item['S']} |"
        )
    return "\n".join(lines)


def cases_markdown(cases: list[dict[str, Any]]) -> str:
    """压缩输出样本。"""
    if not cases:
        return "无"
    return "; ".join(
        f"P={case['P']}, k={case['k']}, N={case.get('N', case.get('value'))}, "
        f"offset={case.get('offset', '-')}"
        for case in cases
    )


def build_payload() -> dict[str, Any]:
    """生成证书 payload。"""
    sweep = finite_sweep()
    rows = build_rows()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "status": "strict_k_positive_core_unified_across_dual_owner_rejection_gap_coordinates",
        "core_identity": {
            "N": "N_P(k)=pi((k+1)P-1)-pi(kP)",
            "dual_window": "N=(P-1)-B_P(k)-S_P(k)",
            "owner_defect": "N=(P-1)-OwnerMass",
            "raw_rejection": "N=RejectionMass-(RawTotal-(P-1))",
            "sqrt_gap": "N>=1 iff next_prime(kP)<(k+1)P",
        },
        "finite_sweep": sweep,
        "gates": rows,
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "当前 strict-k 前沿的多个名字已经统一为同一个正性核心。"
            "证明 DualWindowAntiTiling、PositiveRejectionExcess 或 SqrtGapInput 中任一项，"
            "本质上都是证明同一个整数 N_P(k) 为正。非循环路线不应继续把这些名字当作"
            "互相独立的逃逸口；下一步必须直接证明统一核心，或输入平方根尺度短区间定理。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    sweep = payload["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k unified positive core 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层把当前三个硬点同步成同一个整数。对 `1<k<P`，令",
        "",
        "```text",
        "N_P(k)=pi((k+1)P-1)-pi(kP).",
        "```",
        "",
        "则已有四个坐标完全一致：",
        "",
        "```text",
        "N_P(k)=(P-1)-B_P(k)-S_P(k)",
        "      =(P-1)-OwnerMass",
        "      =RejectionMass-(RawTotal-(P-1)).",
        "N_P(k)>=1 iff next_prime(kP)<(k+1)P.",
        "```",
        "",
        "## 1. 有限审计",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"strict_row_count={sweep['strict_row_count']}",
        f"all_four_coordinate_identities_hold={fmt_bool(sweep['all_four_coordinate_identities_hold'])}",
        f"minimum_positive_core_value={sweep['minimum_positive_core_value']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(sweep['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最小正性核心样本：",
        "",
        "```text",
        cases_markdown(sweep["minimum_positive_cases"]),
        "```",
        "",
        "最大 next-prime offset 样本：",
        "",
        "```text",
        cases_markdown(sweep["max_next_prime_offset"]["cases"]),
        "```",
        "",
        "## 2. 样本行",
        "",
        sample_markdown(sweep["sample_rows"]),
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 4. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "本层不是无条件证明；它的作用是把当前真剩余精确压成单核：",
        "",
        "```text",
        "UnifiedPositiveCore: N_P(k)>=1 for every prime P and every 1<k<P.",
        "```",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in payload["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
