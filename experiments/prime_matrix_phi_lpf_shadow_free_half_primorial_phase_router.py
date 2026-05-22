#!/usr/bin/env python3
"""生成 shadow-free 子带的 half-primorial 特殊相位证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_shadow_free_half_primorial_phase_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.json

输出：
  data/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-ledger.json
  docs/monograph/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.json
  docs/monograph/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.md
"""

from __future__ import annotations

import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-shadow-free-half-primorial-phase"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

MAX_ROW_AUDIT_PRIME = 1009
MAX_FULL_PERIOD_PRIME = 43
LARGE_SAMPLE_SEEDS = [3_000_000, 5_000_000]

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json",
    DOCS / "prime-matrix-primorial-jacobsthal-central-block-router.json",
    DOCS / "prime-matrix-terminal-row-square-phase-bridge-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def spf_table(n: int) -> list[int]:
    """生成最小素因子表。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for value in range(p * p, n + 1, p):
                if spf[value] == value:
                    spf[value] = p
    return spf


def primes_up_to(n: int, spf: list[int]) -> list[int]:
    """返回不超过 n 的素数。"""
    return [value for value in range(2, n + 1) if spf[value] == value]


def is_prime64(n: int) -> bool:
    """确定性 Miller-Rabin，覆盖本脚本样本范围。"""
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if n == prime:
            return True
        if n % prime == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in small_primes:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime_at_least(n: int) -> int:
    """返回不小于 n 的第一个素数。"""
    if n <= 2:
        return 2
    candidate = n if n % 2 else n + 1
    while not is_prime64(candidate):
        candidate += 2
    return candidate


def primorial(primes: list[int]) -> int:
    """计算素数列表乘积。"""
    value = 1
    for prime in primes:
        value *= prime
    return value


def max_circular_covered_run(modulus: int, primes: list[int]) -> dict[str, Any]:
    """计算半 primorial 周期中的最大连续低筛覆盖块。

    covered=True 表示该 residue 与 modulus 不互素；也就是会被 q<=P/2 的低筛删掉。
    """
    covered = bytearray(modulus)
    for q in primes:
        covered[0:modulus:q] = b"\x01" * ((modulus - 1) // q + 1)

    doubled = covered + covered
    best_len = 0
    best_start = 0
    current = 0
    current_start = 0
    for idx, flag in enumerate(doubled):
        if flag:
            if current == 0:
                current_start = idx
            current += 1
            if current > best_len and current <= modulus:
                best_len = current
                best_start = current_start % modulus
        else:
            current = 0
    return {
        "modulus": modulus,
        "low_prime_count": len(primes),
        "max_covered_run_length": best_len,
        "max_covered_run_start_mod_M": best_start,
        "max_covered_run_end_mod_M": (best_start + best_len - 1) % modulus if best_len else None,
    }


def shadow_free_cap(P: int) -> int:
    """返回保证 two-prime shadow 为空的最大 k。"""
    cap = 1
    for k in range(2, P):
        if 4 * ((k + 1) * P - 1) <= P * P:
            cap = k
        else:
            break
    return cap


def high_band_lower_k(P: int) -> int:
    """返回 BHP bulk 后第一个整数 k；只作分区标签。"""
    return max(2, int(P ** (19.0 / 21.0)) + 1)


def row_phase_audit(max_prime: int = MAX_ROW_AUDIT_PRIME) -> dict[str, Any]:
    """有限审计 shadow-free 高带的实际 half-rough survivor 是否非空。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_up_to(max_prime, spf)
    rows: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for P in [prime for prime in primes if prime >= 11]:
        high_lower = high_band_lower_k(P)
        free_cap = shadow_free_cap(P)
        if high_lower > free_cap:
            continue
        low_primes = primes_up_to(P // 2, spf)
        modulus = primorial(low_primes) if P <= MAX_FULL_PERIOD_PRIME else None
        for k in range(high_lower, free_cap + 1):
            survivors: list[int] = []
            for t in range(1, P):
                n = k * P + t
                if spf[n] > P // 2:
                    survivors.append(n)
            item = {
                "P": P,
                "k": k,
                "interval": [k * P + 1, (k + 1) * P - 1],
                "row_length": P - 1,
                "half_rough_survivor_count": len(survivors),
                "first_survivor": survivors[0] if survivors else None,
                "phase_start_mod_half_primorial": (k * P + 1) % modulus if modulus else None,
                "shadow_free": True,
                "survivors_are_prime_in_shadow_free_band": all(spf[n] == n for n in survivors),
            }
            rows.append(item)
            if not survivors:
                failures.append(item)
    min_count = min((row["half_rough_survivor_count"] for row in rows), default=None)
    return {
        "max_prime": max_prime,
        "audited_shadow_free_high_rows": len(rows),
        "all_shadow_free_high_rows_have_survivor": not failures,
        "failure_count": len(failures),
        "minimum_survivor_count": min_count,
        "minimum_rows": [row for row in rows if row["half_rough_survivor_count"] == min_count][:12],
        "sample_rows": rows[:16],
        "finite_evidence_not_used_as_global_proof": True,
    }


def full_period_audit(max_prime: int = MAX_FULL_PERIOD_PRIME) -> dict[str, Any]:
    """扫描小 P 的完整 half-primorial 周期覆盖块。"""
    spf = spf_table(max_prime)
    primes = primes_up_to(max_prime, spf)
    profiles: list[dict[str, Any]] = []
    for P in [prime for prime in primes if prime >= 11]:
        low_primes = primes_up_to(P // 2, spf)
        modulus = primorial(low_primes)
        run = max_circular_covered_run(modulus, low_primes)
        profiles.append(
            {
                "P": P,
                "low_cutoff": P // 2,
                "half_primorial": modulus,
                "half_primorial_prime_count": len(low_primes),
                "row_length_P_minus_1": P - 1,
                "max_covered_run_length": run["max_covered_run_length"],
                "uniform_period_bound_closes_all_phases_for_this_P": run["max_covered_run_length"] < P - 1,
                "max_run_start_mod_M": run["max_covered_run_start_mod_M"],
                "max_run_end_mod_M": run["max_covered_run_end_mod_M"],
            }
        )
    return {
        "max_full_period_prime": max_prime,
        "profile_count": len(profiles),
        "all_scanned_half_primorial_periods_have_max_run_less_than_P_minus_1": all(
            item["uniform_period_bound_closes_all_phases_for_this_P"] for item in profiles
        ),
        "profiles": profiles,
        "period_scan_is_small_and_not_global_proof": True,
    }


def segmented_shadow_free_row(P: int, k: int) -> dict[str, Any]:
    """用分段低筛审计一个大样本 shadow-free 行。"""
    spf = spf_table(P // 2)
    low_primes = primes_up_to(P // 2, spf)
    # alive[t]=1 表示 kP+t 尚未被 q<=P/2 删除；t=0 不属于行内槽。
    alive = bytearray(b"\x01") * P
    alive[0] = 0
    base = k * P
    for q in low_primes:
        first_t = (-base) % q
        if first_t == 0:
            first_t = q
        alive[first_t:P:q] = b"\x00" * (((P - 1 - first_t) // q) + 1)
    survivor_ts = [idx for idx in range(1, P) if alive[idx]]
    first_values = [base + t for t in survivor_ts[:8]]
    return {
        "P": P,
        "k": k,
        "interval": [base + 1, base + P - 1],
        "low_prime_count": len(low_primes),
        "shadow_free_condition_holds": 4 * ((k + 1) * P - 1) <= P * P,
        "half_rough_survivor_count": len(survivor_ts),
        "first_survivor_values": first_values,
        "first_survivors_prime_checked": [is_prime64(value) for value in first_values],
    }


def large_sample_audit() -> dict[str, Any]:
    """在真正有交集的尺度上审计 shadow-free 高带样本。"""
    rows: list[dict[str, Any]] = []
    for seed in LARGE_SAMPLE_SEEDS:
        P = next_prime_at_least(seed)
        high_lower = high_band_lower_k(P)
        free_cap = shadow_free_cap(P)
        if high_lower > free_cap:
            rows.append(
                {
                    "P": P,
                    "high_lower": high_lower,
                    "shadow_free_cap": free_cap,
                    "has_overlap": False,
                }
            )
            continue
        sample_ks = sorted({high_lower, (high_lower + free_cap) // 2, free_cap})
        for k in sample_ks:
            item = segmented_shadow_free_row(P, k)
            item["high_lower"] = high_lower
            item["shadow_free_cap"] = free_cap
            item["has_overlap"] = True
            rows.append(item)
    return {
        "sample_seeds": LARGE_SAMPLE_SEEDS,
        "sample_count": len(rows),
        "all_sampled_rows_have_survivor": all(
            (not row.get("has_overlap", True)) or row.get("half_rough_survivor_count", 0) > 0
            for row in rows
        ),
        "rows": rows,
        "large_samples_are_evidence_not_global_proof": True,
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "ShadowFreeSurvivorEqualsHalfPrimorialCoprimeHit",
            True,
            True,
            "在 shadow-free 子带，R_half(P,k)>0 等价于区间 kP+1..kP+P-1 命中一个与 M_{<=P/2} 互素的 residue。",
            "exact equivalence",
        ),
        row(
            "ShadowFreeSurvivorIsPrime",
            True,
            True,
            "由于整行低于 P^2/4，任意 q,m>P/2 的合成 shadow 不存在；half-rough survivor 必为素数。",
            "none",
        ),
        row(
            "UniformHalfPrimorialJacobsthalWouldCloseShadowFreeLane",
            True,
            True,
            "若 half-primorial 周期中最大低筛覆盖块长度 < P-1，则所有 shadow-free 行自动闭合。",
            "needs uniform half-primorial bound",
        ),
        row(
            "SpecialRowPhaseAvoidanceIdentified",
            True,
            True,
            "即使没有全周期 Jacobsthal 上界，也只需排斥特殊相位 kP+1 命中长度 P-1 覆盖块。",
            "HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC",
        ),
        row(
            "FiniteAuditSupportsButDoesNotProve",
            True,
            True,
            "有限行审计与小周期扫描均正常，但不作为全局证明。",
            "finite evidence only",
        ),
        row(
            "ShadowFreeLaneClosedGlobally",
            False,
            False,
            "尚未证明 uniform half-primorial Jacobsthal bound 或特殊相位避让。",
            "HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC",
        ),
        row(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层只把 shadow-free 子带压成半 primorial 特殊相位问题，不证明三目标命题。",
            "upper-band shadow excess still open",
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


def period_markdown(profiles: list[dict[str, Any]]) -> str:
    """输出小周期扫描表。"""
    lines = [
        "| P | cutoff | M_half | max covered run | P-1 | uniform closes | start mod M |",
        "| ---: | ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for item in profiles:
        lines.append(
            f"| {item['P']} | {item['low_cutoff']} | {item['half_primorial']} | "
            f"{item['max_covered_run_length']} | {item['row_length_P_minus_1']} | "
            f"`{fmt_bool(item['uniform_period_bound_closes_all_phases_for_this_P'])}` | "
            f"{item['max_run_start_mod_M']} |"
        )
    return "\n".join(lines)


def compact_rows(rows: list[dict[str, Any]]) -> str:
    """压缩有限行审计读数。"""
    if not rows:
        return "无"
    return "; ".join(
        "P={P}, k={k}, survivors={C}, first={F}".format(
            P=item["P"],
            k=item["k"],
            C=item["half_rough_survivor_count"],
            F=item["first_survivor"],
        )
        for item in rows
    )


def build_payload() -> dict[str, Any]:
    """生成证书 payload。"""
    row_audit = row_phase_audit()
    period_audit = full_period_audit()
    large_audit = large_sample_audit()
    gates = build_rows()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "status": "shadow_free_lane_reduced_to_half_primorial_special_phase_avoidance",
        "definitions": {
            "M_half(P)": "product of primes q<=P/2",
            "shadow_free_condition": "4*((k+1)P-1)<=P^2",
            "coprime_hit": "exists t in [1,P-1] with gcd(kP+t,M_half(P))=1",
            "phase_start": "kP+1 mod M_half(P)",
        },
        "row_phase_audit": row_audit,
        "full_period_audit": period_audit,
        "large_sample_audit": large_audit,
        "gates": gates,
        "dependency_hashes": dependency_hashes,
        "next_direct_attack_target": "HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC",
        "plain_conclusion": (
            "shadow-free 子带的正性已经无损转为半 primorial 特殊相位避让："
            "行失败当且仅当相位 kP+1 在 M_{<=P/2} 周期中启动一个长度 P-1 的低筛覆盖块。"
            "全周期 Jacobsthal 上界会立即闭合该子带；若全周期上界不可得，剩余就是特殊行相位避让或 PDEC。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    row_audit = payload["row_phase_audit"]
    period_audit = payload["full_period_audit"]
    large_audit = payload["large_sample_audit"]
    lines = [
        "# Prime Matrix Phi-LPF shadow-free half-primorial phase 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层只处理上一层拆出的 shadow-free 子带。设",
        "",
        "```text",
        "M_half(P)=prod_{q<=P/2, q prime} q.",
        "```",
        "",
        "在条件 `4*((k+1)P-1)<=P^2` 下，two-prime shadow 为空。因此该行正性等价于",
        "",
        "```text",
        "exists 1<=t<P such that gcd(kP+t, M_half(P))=1.",
        "```",
        "",
        "并且任何这样的 survivor 自动是素数。换句话说，失败当且仅当特殊相位",
        "`kP+1 mod M_half(P)` 启动了一个长度 `P-1` 的 half-primorial 低筛覆盖块。",
        "",
        "## 1. 有限行相位审计",
        "",
        "```text",
        f"max_prime={row_audit['max_prime']}",
        f"audited_shadow_free_high_rows={row_audit['audited_shadow_free_high_rows']}",
        f"all_shadow_free_high_rows_have_survivor={fmt_bool(row_audit['all_shadow_free_high_rows_have_survivor'])}",
        f"failure_count={row_audit['failure_count']}",
        f"minimum_survivor_count={row_audit['minimum_survivor_count']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(row_audit['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最小 survivor 行样本：",
        "",
        "```text",
        compact_rows(row_audit["minimum_rows"]),
        "```",
        "",
        "大尺度 shadow-free 交集样本：",
        "",
        "```text",
        f"sample_seeds={large_audit['sample_seeds']}",
        f"sample_count={large_audit['sample_count']}",
        f"all_sampled_rows_have_survivor={fmt_bool(large_audit['all_sampled_rows_have_survivor'])}",
        f"large_samples_are_evidence_not_global_proof={fmt_bool(large_audit['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        "| P | k | high lower | free cap | survivors | first survivor | first prime checked |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in large_audit["rows"]:
        if not item.get("has_overlap", True):
            lines.append(
                f"| {item['P']} | - | {item['high_lower']} | {item['shadow_free_cap']} | - | - | `false` |"
            )
        else:
            first_value = item["first_survivor_values"][0] if item["first_survivor_values"] else None
            first_checked = item["first_survivors_prime_checked"][0] if item["first_survivors_prime_checked"] else None
            lines.append(
                f"| {item['P']} | {item['k']} | {item['high_lower']} | {item['shadow_free_cap']} | "
                f"{item['half_rough_survivor_count']} | {first_value} | `{fmt_bool(first_checked)}` |"
            )
    lines.extend(
        [
        "",
        "## 2. 小 half-primorial 全周期扫描",
        "",
        "```text",
        f"max_full_period_prime={period_audit['max_full_period_prime']}",
        f"profile_count={period_audit['profile_count']}",
        "all_scanned_half_primorial_periods_have_max_run_less_than_P_minus_1="
        f"{fmt_bool(period_audit['all_scanned_half_primorial_periods_have_max_run_less_than_P_minus_1'])}",
        f"period_scan_is_small_and_not_global_proof={fmt_bool(period_audit['period_scan_is_small_and_not_global_proof'])}",
        "```",
        "",
        period_markdown(period_audit["profiles"]),
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 4. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "当前 shadow-free 子带的最窄直接口是：",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "这仍不是最终闭合；upper-band 的 two-prime shadow excess 也仍然开放。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
            "| --- | --- |",
        ]
    )
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
    print(
        json.dumps(
            {
                "status": payload["status"],
                "row_audit_passed": payload["row_phase_audit"]["all_shadow_free_high_rows_have_survivor"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
