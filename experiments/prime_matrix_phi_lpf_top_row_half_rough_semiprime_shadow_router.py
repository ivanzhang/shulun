#!/usr/bin/env python3
"""生成顶行 half-rough survivor 与 reciprocal semiprime shadow 证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_top_row_half_rough_semiprime_shadow_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.json

输出：
  data/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-ledger.json
  docs/monograph/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.json
  docs/monograph/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.md
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

SLUG = "prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json",
    DOCS / "prime-matrix-terminal-row-square-phase-bridge-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def prime_flags(n: int) -> bytearray:
    """生成素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def half_rough_profile(P: int, flags_square: bytearray, flags_2p: bytearray, primes: list[int]) -> dict[str, Any]:
    """计算单个素数底的 half-rough 分解。"""
    low_primes = [q for q in primes if q <= P // 2]
    high_primes = [q for q in primes if P // 2 < q < P]

    covered = bytearray(P)
    for q in low_primes:
        residue = (P * P) % q
        start = residue if residue != 0 else q
        for r in range(start, P, q):
            covered[r] = 1

    rough_rs = [r for r in range(1, P) if not covered[r]]
    semiprime_shadow: list[dict[str, int]] = []
    max_candidates_per_q = 0
    two_candidate_q_count = 0
    for q in high_primes:
        lower = (P * P - P) // q + 1
        upper = (P * P - 1) // q
        candidate_count = max(0, upper - lower + 1)
        max_candidates_per_q = max(max_candidates_per_q, candidate_count)
        if candidate_count == 2:
            two_candidate_q_count += 1
        for m in range(lower, upper + 1):
            if m < len(flags_2p) and flags_2p[m]:
                semiprime_shadow.append({"q": q, "m": m, "r": P * P - q * m})

    direct_top_primes = [P * P - r for r in range(1, P) if flags_square[P * P - r]]
    rough_count = len(rough_rs)
    shadow_count = len(semiprime_shadow)
    direct_prime_count = len(direct_top_primes)
    return {
        "P": P,
        "slot_count": P - 1,
        "low_prime_cutoff": P // 2,
        "low_prime_count": len(low_primes),
        "high_prime_count": len(high_primes),
        "half_rough_survivor_count": rough_count,
        "semiprime_shadow_count": shadow_count,
        "half_rough_minus_shadow": rough_count - shadow_count,
        "direct_top_prime_count": direct_prime_count,
        "identity_holds": rough_count - shadow_count == direct_prime_count,
        "shadow_entries_have_prime_factors": all(flags_2p[item["q"]] and flags_2p[item["m"]] for item in semiprime_shadow),
        "shadow_entries_in_top_row": all(1 <= item["r"] < P for item in semiprime_shadow),
        "max_candidates_per_high_q": max_candidates_per_q,
        "two_candidate_high_q_count": two_candidate_q_count,
        "rough_r_prefix": rough_rs[:16],
        "shadow_prefix": semiprime_shadow[:16],
        "top_prime_prefix": direct_top_primes[:16],
    }


def finite_sweep(max_prime: int = 5003) -> dict[str, Any]:
    """有限审计 half-rough 等式；不作为全局证明。"""
    flags_square = prime_flags(max_prime * max_prime)
    flags_2p = prime_flags(2 * max_prime)
    primes = [n for n in range(2, max_prime + 1) if flags_square[n]]
    prime_bases = [p for p in primes if p >= 5]
    rows = [half_rough_profile(P, flags_square, flags_2p, primes) for P in prime_bases]
    failures = [row for row in rows if not row["identity_holds"]]
    min_margin = min(row["half_rough_minus_shadow"] for row in rows)
    min_margin_rows = [row for row in rows if row["half_rough_minus_shadow"] == min_margin][:12]
    max_shadow_ratio_row = max(
        rows,
        key=lambda row: row["semiprime_shadow_count"] / max(1, row["half_rough_survivor_count"]),
    )
    sample_ps = [5, 7, 11, 17, 101, 257, 1009, 5003]
    sample_rows = [row for row in rows if row["P"] in sample_ps]
    return {
        "max_prime": max_prime,
        "prime_base_count": len(rows),
        "all_half_rough_identities_hold": not failures,
        "identity_failure_count": len(failures),
        "minimum_half_rough_minus_shadow": min_margin,
        "minimum_margin_rows": min_margin_rows,
        "max_shadow_ratio_row": max_shadow_ratio_row,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "HalfRoughSplitIdentityClosed",
            "closed": True,
            "proved": True,
            "meaning": "顶行素数数精确等于避开 q<=P/2 的平方相位幸存量减去 reciprocal prime-semiprime shadow。",
            "remaining": "exact identity",
        },
        {
            "gate": "CompositeHalfRoughForcesTwoPrimeShadow",
            "closed": True,
            "proved": True,
            "meaning": "若 P^2-r 避开所有 q<=P/2 且仍合成，则其 LPF q 在 (P/2,P)，商 m 在 (P,2P) 且为素数。",
            "remaining": "none for structural split",
        },
        {
            "gate": "EachHighQHasAtMostTwoReciprocalCandidates",
            "closed": True,
            "proved": True,
            "meaning": "对 q in (P/2,P)，m 的 reciprocal window 长度为 P/q<2，因此每个 q 至多给两个候选 m。",
            "remaining": "candidate count only; prime filtering remains",
        },
        {
            "gate": "FiniteSweepIdentityMatchesDirectPrimeCount",
            "closed": True,
            "proved": True,
            "meaning": "有限审计确认 R_{1/2}-T_{1/2} 与直接顶行素数计数一致，但不作为全局证明。",
            "remaining": "finite audit only",
        },
        {
            "gate": "HalfRoughExcessProvedUniformly",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明所有尾段素数 P 都满足 R_{1/2}(P)>T_{1/2}(P)。",
            "remaining": "HalfRoughSurvivorExcessOverReciprocalSemiprimeShadow",
        },
        {
            "gate": "UnifiedPositiveCoreProved",
            "closed": False,
            "proved": False,
            "meaning": "本层只把顶行尾段硬点压成 half-rough excess；没有证明 strict 全行正性。",
            "remaining": "SquarePhaseTailLongBlockPDECExclusion OR HalfRoughExcess",
        },
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
    """输出样本表 Markdown。"""
    lines = [
        "| P | R_half | T_shadow | R-T | direct primes | high q | max cand/q |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in samples:
        lines.append(
            f"| {row['P']} | {row['half_rough_survivor_count']} | {row['semiprime_shadow_count']} | "
            f"{row['half_rough_minus_shadow']} | {row['direct_top_prime_count']} | "
            f"{row['high_prime_count']} | {row['max_candidates_per_high_q']} |"
        )
    return "\n".join(lines)


def compact_cases(cases: list[dict[str, Any]]) -> str:
    """压缩输出极小余量样本。"""
    if not cases:
        return "无"
    return "; ".join(
        "P={P}, R={R}, T={T}, direct={D}".format(
            P=row["P"],
            R=row["half_rough_survivor_count"],
            T=row["semiprime_shadow_count"],
            D=row["direct_top_prime_count"],
        )
        for row in cases
    )


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    sweep = finite_sweep()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_top_row_half_rough_semiprime_shadow_router",
        "status": "top_row_prime_count_equals_half_rough_survivor_excess_over_reciprocal_semiprime_shadow",
        "definitions": {
            "R_half": "#{1<=r<P: gcd(P^2-r, product_{q<=P/2} q)=1}",
            "T_shadow": "sum_{P/2<q<P, q prime} #{m prime: floor((P^2-P)/q)<m<=floor((P^2-1)/q)}",
            "identity": "pi(P^2-1)-pi(P^2-P)=R_half(P)-T_shadow(P)",
        },
        "structural_reason": {
            "low_sieve_cut": "q<=P/2",
            "composite_residual_lpf": "P/2<q<P",
            "quotient_range": "P<m<2P",
            "quotient_prime_for_P_ge_11": "if m were composite, all its prime factors would be >=q>P/2, forcing m>=q^2>2P",
            "small_primes_checked_directly": [5, 7],
            "per_high_q_candidate_bound": "floor window length < 2, so at most two m candidates per q",
        },
        "finite_sweep": sweep,
        "decision_rows": build_rows(),
        "unified_positive_core_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": "HalfRoughSurvivorExcessOverReciprocalSemiprimeShadow OR SquarePhaseTailLongBlockPDECExclusion",
        "dependency_hashes": dependency_hashes,
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    sweep = payload["finite_sweep"]
    hashes = payload["dependency_hashes"]
    hash_lines = ["| file | sha256 |", "| --- | --- |"]
    for file_name, digest in hashes.items():
        hash_lines.append(f"| `{file_name}` | `{digest}` |")

    max_ratio = sweep["max_shadow_ratio_row"]
    return f"""# Prime Matrix Phi-LPF top-row half-rough semiprime shadow 证书

**状态：** `{payload['status']}`

本层把 prime-indexed Oppermann-left 顶行尾段再压缩一层。定义

```text
R_1/2(P)=#{{1<=r<P: gcd(P^2-r, product_{{q<=P/2}} q)=1}}
T_1/2(P)=sum_{{P/2<q<P, q prime}}
  #{{m prime: floor((P^2-P)/q)<m<=floor((P^2-1)/q)}}.
```

则有精确恒等式：

```text
pi(P^2-1)-pi(P^2-P)=R_1/2(P)-T_1/2(P).
```

因此顶行正性不再需要处理完整 LPF 树；它等价于 half-rough survivor
严格多于 reciprocal prime-semiprime shadow。

## 1. 结构证明读法

若 `P^2-r` 避开所有 `q<=P/2` 而仍合成，则它的最小素因子 `q` 必满足：

```text
P/2<q<P.
```

写 `P^2-r=qm`。由于 `P^2-P<P^2-r<P^2`，得到：

```text
P<m<2P.
```

且 `m` 必为素数；否则 `m` 的素因子都不小于 `q>P/2`，从而 `m>=q^2>2P`
（`P>=11`；小素数底在有限审计中直接覆盖）。对每个固定 `q in (P/2,P)`，
`m` 的可行窗口长度为 `P/q<2`，所以每个 `q` 至多贡献两个 reciprocal 候选。

## 2. 有限审计

```text
max_prime={sweep['max_prime']}
prime_base_count={sweep['prime_base_count']}
all_half_rough_identities_hold={fmt_bool(sweep['all_half_rough_identities_hold'])}
identity_failure_count={sweep['identity_failure_count']}
minimum_half_rough_minus_shadow={sweep['minimum_half_rough_minus_shadow']}
finite_evidence_not_used_as_global_proof={fmt_bool(sweep['finite_evidence_not_used_as_global_proof'])}
```

极小余量样本：

```text
{compact_cases(sweep['minimum_margin_rows'])}
```

最高 shadow 比例样本：

```text
P={max_ratio['P']}, R={max_ratio['half_rough_survivor_count']},
T={max_ratio['semiprime_shadow_count']},
ratio={max_ratio['semiprime_shadow_count'] / max(1, max_ratio['half_rough_survivor_count']):.6f}
```

## 3. 样本表

{sample_markdown(sweep['sample_rows'])}

## 4. 判定表

{rows_markdown(payload['decision_rows'])}

## 5. 结论

当前顶行尾段的真剩余已经从“低筛全覆盖”进一步变为单一不等式：

```text
HalfRoughSurvivorExcessOverReciprocalSemiprimeShadow:
  R_1/2(P)>T_1/2(P) for every remaining prime P.
```

若这个不等式成立，则 `PrimeIndexedOppermannLeftHalf(P)` 成立；若失败，则失败不是
匿名容量问题，而是 `(P/2,P)` 与 `(P,2P)` 的 reciprocal prime-semiprime shadow
铺满了全部 half-rough survivor，应登记为 square-phase/semiprime-shadow PDEC。

本层仍不证明 `UnifiedPositiveCore` 或行/列命题；它只把无限尾段硬点压到更窄的
half-rough excess 接口。

## 6. 依赖哈希

{chr(10).join(hash_lines)}
"""


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(json.dumps({"status": payload["status"], "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
