#!/usr/bin/env python3
"""生成 strict-k half-rough shadow 与高 k 平方边界带拆分证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_half_rough_shadow_band_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.md
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

SLUG = "prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

MAX_PRIME_AUDIT = 1009

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-router.json",
    DOCS / "prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.json",
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
    """生成最小素因子表；素数的最小素因子等于自身。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            start = p * p
            for value in range(start, n + 1, p):
                if spf[value] == value:
                    spf[value] = p
    return spf


def prime_list_from_spf(spf: list[int], n: int) -> list[int]:
    """从最小素因子表读取素数列表。"""
    return [value for value in range(2, n + 1) if spf[value] == value]


def high_band_lower_k(P: int) -> int:
    """返回 BHP bulk 之后的第一个整数 k；仅作分区标签。"""
    # 浮点只用于有限审计标签，不作为证明输入。
    return max(2, int(P ** (19.0 / 21.0)) + 1)


def shadow_free_cap(P: int) -> int:
    """返回保证 q,m>P/2 的双素数 shadow 不可能出现的最大 k。

    若 4*((k+1)P-1)<=P^2，则整行位于 P^2/4 以下，而任意 q,m>P/2
    的乘积都严格大于 P^2/4。
    """
    cap = 1
    for k in range(2, P):
        if 4 * ((k + 1) * P - 1) <= P * P:
            cap = k
        else:
            break
    return cap


def audit_prime_base(P: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """审计单个素数底 P 的 strict-k half-rough shadow 恒等式。"""
    rough = [0] * P
    direct = [0] * P
    shadow = [0] * P

    for k in range(2, P):
        base = k * P
        for t in range(1, P):
            n = base + t
            if spf[n] > P // 2:
                rough[k] += 1
            if spf[n] == n:
                direct[k] += 1

    high_q = [q for q in primes_2p if P // 2 < q < P]
    high_m = [m for m in primes_2p if P // 2 < m < 2 * P]
    shadow_prefix: list[dict[str, int]] = []
    for q in high_q:
        for m in high_m:
            if m < q:
                continue
            n = q * m
            if n >= P * P:
                break
            k, t = divmod(n, P)
            if 2 <= k < P and 1 <= t < P:
                shadow[k] += 1
                if len(shadow_prefix) < 16:
                    shadow_prefix.append({"k": k, "t": t, "q": q, "m": m, "n": n})

    rows: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    high_lower = high_band_lower_k(P)
    free_cap = shadow_free_cap(P)
    for k in range(2, P):
        margin = rough[k] - shadow[k]
        item = {
            "P": P,
            "k": k,
            "rough_survivor_count": rough[k],
            "semiprime_shadow_count": shadow[k],
            "rough_minus_shadow": margin,
            "direct_prime_count": direct[k],
            "identity_holds": margin == direct[k],
            "in_bhp_remaining_high_band": k >= high_lower,
            "in_shadow_free_subband": k <= free_cap,
        }
        rows.append(item)
        if not item["identity_holds"]:
            failures.append(item)

    min_margin = min(row["rough_minus_shadow"] for row in rows)
    min_high_margin = min(
        (row["rough_minus_shadow"] for row in rows if row["in_bhp_remaining_high_band"]),
        default=None,
    )
    sample_ks = sorted({2, min(P - 1, high_lower), min(P - 1, max(high_lower, P // 4)), P - 1})
    samples = [row for row in rows if row["k"] in sample_ks]
    return {
        "P": P,
        "strict_row_count": len(rows),
        "identity_failure_count": len(failures),
        "all_identities_hold": not failures,
        "minimum_margin_all_strict_rows": min_margin,
        "minimum_margin_rows": [row for row in rows if row["rough_minus_shadow"] == min_margin][:8],
        "bhp_remaining_high_band_first_k": high_lower,
        "shadow_free_cap_k": free_cap,
        "minimum_margin_in_bhp_remaining_high_band": min_high_margin,
        "high_band_row_count": sum(1 for row in rows if row["in_bhp_remaining_high_band"]),
        "shadow_free_row_count": sum(1 for row in rows if row["in_shadow_free_subband"]),
        "sample_rows": samples,
        "shadow_prefix": shadow_prefix,
    }


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计 exact identity；只作一致性检查，不作全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = prime_list_from_spf(spf, max_prime)
    primes_2p = prime_list_from_spf(spf, 2 * max_prime)
    prime_bases = [p for p in primes if p >= 11]
    profiles = [audit_prime_base(P, spf, primes_2p) for P in prime_bases]
    failures = [profile for profile in profiles if profile["identity_failure_count"]]
    all_rows = [row for profile in profiles for row in profile["sample_rows"]]
    min_profile = min(profiles, key=lambda item: item["minimum_margin_all_strict_rows"])
    high_profiles = [profile for profile in profiles if profile["high_band_row_count"]]
    min_high_profile = min(
        high_profiles,
        key=lambda item: item["minimum_margin_in_bhp_remaining_high_band"]
        if item["minimum_margin_in_bhp_remaining_high_band"] is not None
        else 10**9,
    )
    return {
        "max_prime": max_prime,
        "prime_base_count": len(profiles),
        "all_half_rough_shadow_identities_hold": not failures,
        "identity_failure_count": len(failures),
        "minimum_margin_profile": {
            "P": min_profile["P"],
            "minimum_margin_all_strict_rows": min_profile["minimum_margin_all_strict_rows"],
            "minimum_margin_rows": min_profile["minimum_margin_rows"],
        },
        "minimum_high_band_margin_profile": {
            "P": min_high_profile["P"],
            "bhp_remaining_high_band_first_k": min_high_profile["bhp_remaining_high_band_first_k"],
            "minimum_margin_in_bhp_remaining_high_band": min_high_profile["minimum_margin_in_bhp_remaining_high_band"],
        },
        "sample_profiles": [
            profile
            for profile in profiles
            if profile["P"] in {11, 101, 257, 1009}
        ],
        "sample_rows_compact": all_rows[:24],
        "finite_evidence_not_used_as_global_proof": True,
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
            "StrictKHalfRoughShadowIdentityClosed",
            True,
            True,
            "对每个 1<k<P，N_P(k) 精确等于 q<=P/2 后的 half-rough survivor 减去 q,m>P/2 的双素数 shadow。",
            "exact identity",
        ),
        row(
            "CompositeHalfRoughSurvivorForcesTwoPrimeShadow",
            True,
            True,
            "若 kP+t 避开所有 q<=P/2 且仍合成，则其 LPF q 在 (P/2,P)，商 m<2P 且必须为素数。",
            "none for structural split",
        ),
        row(
            "BHPRemainingHighBandShadowFreeSubbandSeparated",
            True,
            True,
            "当整行位于 P^2/4 以下时，q,m>P/2 的 shadow 不可能出现；该子带只剩 half-rough survivor 非空性。",
            "HalfRoughSurvivorExistenceInShadowFreeHighBand",
        ),
        row(
            "UpperSquareBandReducedToSemiprimeShadowExcess",
            True,
            True,
            "在 P^2/4 以上的高 k 带，失败必须表现为双素数 shadow 吃掉全部 half-rough survivor excess。",
            "HighKHalfRoughSurvivorExcessOverTwoPrimeShadow",
        ),
        row(
            "FiniteSweepIdentityMatchesDirectPrimeCount",
            True,
            True,
            "有限审计确认 exact identity 与直接素数计数一致，但不作为全局证明。",
            "finite audit only",
        ),
        row(
            "HighKSquareBandPositivityProved",
            False,
            False,
            "本层没有证明 half-rough survivor 非空性或 shadow excess 的全局下界。",
            "HalfRoughSurvivorExistenceInShadowFreeHighBand OR HighKHalfRoughSurvivorExcessOverTwoPrimeShadow",
        ),
        row(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层继续压缩非循环剩余，但不证明三目标命题无条件闭合。",
            "sqrt-scale theorem or structural high-k half-rough excess",
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
        "| P | k | R_half | T_shadow | R-T | direct primes | high band | shadow-free |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row_item in samples:
        lines.append(
            f"| {row_item['P']} | {row_item['k']} | {row_item['rough_survivor_count']} | "
            f"{row_item['semiprime_shadow_count']} | {row_item['rough_minus_shadow']} | "
            f"{row_item['direct_prime_count']} | `{fmt_bool(row_item['in_bhp_remaining_high_band'])}` | "
            f"`{fmt_bool(row_item['in_shadow_free_subband'])}` |"
        )
    return "\n".join(lines)


def compact_min_rows(rows: list[dict[str, Any]]) -> str:
    """压缩最小余量行读数。"""
    return "; ".join(
        "P={P}, k={k}, R={R}, T={T}, direct={D}".format(
            P=item["P"],
            k=item["k"],
            R=item["rough_survivor_count"],
            T=item["semiprime_shadow_count"],
            D=item["direct_prime_count"],
        )
        for item in rows
    )


def build_payload() -> dict[str, Any]:
    """生成证书 payload。"""
    audit = finite_audit()
    rows = build_rows()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "status": "strict_k_prime_count_equals_half_rough_survivor_excess_over_two_prime_shadow",
        "definitions": {
            "R_half(P,k)": "#{1<=t<P: gcd(kP+t, product_{q<=P/2} q)=1}",
            "T_half(P,k)": "#{q,m prime: P/2<q<=m<2P, kP<qm<(k+1)P}",
            "identity": "pi((k+1)P-1)-pi(kP)=R_half(P,k)-T_half(P,k)",
            "shadow_free_condition": "4*((k+1)P-1)<=P^2 implies T_half(P,k)=0",
        },
        "finite_audit": audit,
        "gates": rows,
        "dependency_hashes": dependency_hashes,
        "next_direct_attack_target": (
            "HalfRoughSurvivorExistenceInShadowFreeHighBand OR "
            "HighKHalfRoughSurvivorExcessOverTwoPrimeShadow"
        ),
        "plain_conclusion": (
            "高 k 平方边界带现在不再需要完整 LPF 树。每一行的素数数等于 half-rough survivor "
            "减去唯一的 q,m>P/2 双素数 shadow。低于 P^2/4 的剩余子带 shadow 为零，只需证明 "
            "half-rough survivor 非空；高于 P^2/4 的子带则变成 survivor 严格多于 two-prime shadow。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit = payload["finite_audit"]
    min_profile = audit["minimum_margin_profile"]
    min_high = audit["minimum_high_band_margin_profile"]
    sample_rows = [row for profile in audit["sample_profiles"] for row in profile["sample_rows"]]
    lines = [
        "# Prime Matrix Phi-LPF strict-k half-rough shadow band split 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层把上一层留下的高 `k` 平方边界带继续 half-rough 化。对素数底 `P` 和 `1<k<P`，定义",
        "",
        "```text",
        "R_half(P,k)=#{1<=t<P: gcd(kP+t, product_{q<=P/2} q)=1}",
        "T_half(P,k)=#{q,m prime: P/2<q<=m<2P, kP<qm<(k+1)P}.",
        "```",
        "",
        "则有精确恒等式：",
        "",
        "```text",
        "pi((k+1)P-1)-pi(kP)=R_half(P,k)-T_half(P,k).",
        "```",
        "",
        "## 1. 结构证明读法",
        "",
        "若 `kP+t` 避开所有 `q<=P/2` 而仍合成，则其最小素因子 `q` 必满足 `P/2<q<P`。",
        "写 `kP+t=qm`，由 `k<P` 得 `m<2P`。当 `P>=11` 时，`m` 不可能合成；",
        "否则 `m` 的素因子都至少为 `q>P/2`，从而 `m>=q^2>P^2/4>2P`。",
        "为避免双计数，shadow 只取 `q<=m`。于是每个 composite half-rough survivor",
        "与一个唯一的双素数 shadow 对应。",
        "",
        "同时，如果",
        "",
        "```text",
        "4*((k+1)P-1)<=P^2,",
        "```",
        "",
        "则整行低于 `P^2/4`，而任意 `q,m>P/2` 的乘积都大于 `P^2/4`，所以 `T_half(P,k)=0`。",
        "这把 BHP bulk 之后的高 `k` 带再分成 shadow-free survivor 非空问题和 upper-band",
        "semiprime-shadow excess 问题。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"prime_base_count={audit['prime_base_count']}",
        f"all_half_rough_shadow_identities_hold={fmt_bool(audit['all_half_rough_shadow_identities_hold'])}",
        f"identity_failure_count={audit['identity_failure_count']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(audit['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最小余量样本：",
        "",
        "```text",
        compact_min_rows(min_profile["minimum_margin_rows"]),
        "```",
        "",
        "高带最小余量读数：",
        "",
        "```text",
        f"P={min_high['P']}, first_high_k={min_high['bhp_remaining_high_band_first_k']}, "
        f"min_high_margin={min_high['minimum_margin_in_bhp_remaining_high_band']}",
        "```",
        "",
        "## 3. 样本表",
        "",
        sample_markdown(sample_rows),
        "",
        "## 4. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 5. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "当前最窄直接主攻口更新为：",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只把高 `k` 真剩余",
        "压成更短的 survivor 非空和 two-prime shadow excess 两个接口。",
        "",
        "## 6. 依赖哈希",
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
    print(
        json.dumps(
            {
                "status": payload["status"],
                "max_prime": payload["finite_audit"]["max_prime"],
                "all_identities_hold": payload["finite_audit"]["all_half_rough_shadow_identities_hold"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
