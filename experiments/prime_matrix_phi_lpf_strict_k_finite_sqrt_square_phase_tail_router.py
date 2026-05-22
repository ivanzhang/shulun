#!/usr/bin/env python3
"""生成 strict-k 有限 sqrt-gap 桥与平方相位尾段证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_finite_sqrt_square_phase_tail_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.md
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

SLUG = "prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

FINITE_SQRT_X_MIN = 117
FINITE_SQRT_X_MAX = 10**18

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-unified-positive-core-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-router.json",
    DOCS / "prime-matrix-terminal-row-square-phase-bridge-router.json",
    DOCS / "prime-matrix-primorial-jacobsthal-central-block-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json",
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


def is_prime64(n: int) -> bool:
    """确定性 Miller-Rabin，覆盖 64 位范围。"""
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

    # 这组小素数底数对本脚本涉及的 64 位整数范围是确定性的。
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
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


def previous_prime(n: int) -> int:
    """返回不超过 n 的最大素数。"""
    if n < 2:
        raise ValueError("n must be at least 2")
    candidate = n if n % 2 else n - 1
    if n >= 2 and candidate < 2:
        return 2
    while candidate >= 2:
        if is_prime64(candidate):
            return candidate
        candidate -= 2
    return 2


def primes_below(n: int) -> list[int]:
    """返回小于 n 的素数列表。"""
    return [value for value in range(2, n) if is_prime64(value)]


def next_prime_after(n: int) -> int:
    """返回 n 后的下一个素数。"""
    candidate = n + 1
    if candidate <= 2:
        return 2
    if candidate % 2 == 0:
        candidate += 1
    while not is_prime64(candidate):
        candidate += 2
    return candidate


def top_row_threshold() -> dict[str, Any]:
    """计算外部有限 sqrt-gap 引理能覆盖到的顶行素数底。"""
    # 顶行起点 x=P^2-P。求 P^2-P <= 10^18 的最大整数 P。
    integer_bound = (1 + isqrt(1 + 4 * FINITE_SQRT_X_MAX)) // 2
    while integer_bound * integer_bound - integer_bound > FINITE_SQRT_X_MAX:
        integer_bound -= 1
    largest_prime_base = previous_prime(integer_bound)
    return {
        "x_max": FINITE_SQRT_X_MAX,
        "top_row_integer_base_bound": integer_bound,
        "largest_prime_base_with_top_row_start_le_x_max": largest_prime_base,
        "top_row_start_at_largest_prime_base": largest_prime_base * largest_prime_base - largest_prime_base,
        "top_row_end_at_largest_prime_base": largest_prime_base * largest_prime_base - 1,
        "finite_sqrt_gap_length": isqrt(largest_prime_base * largest_prime_base - largest_prime_base),
        "strict_row_length_P": largest_prime_base,
    }


def small_direct_rows(limit_x: int = FINITE_SQRT_X_MIN - 1) -> dict[str, Any]:
    """直接核查有限 sqrt-gap 引理阈值以下的 strict 行。"""
    checked: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for P in primes_below(limit_x + 3):
        if P <= 3:
            continue
        for k in range(2, P):
            x = k * P
            if x > limit_x:
                continue
            row_primes = [n for n in range(x + 1, (k + 1) * P) if is_prime64(n)]
            item = {"P": P, "k": k, "x": x, "prime_count": len(row_primes), "first_prime": row_primes[0] if row_primes else None}
            checked.append(item)
            if not row_primes:
                failures.append(item)
    return {
        "small_x_limit": limit_x,
        "checked_row_count": len(checked),
        "all_small_rows_positive": not failures,
        "small_row_failures": failures,
        "minimum_small_row_prime_count": min((row["prime_count"] for row in checked), default=0),
        "sample_small_rows": checked[:12],
    }


def top_row_cover_sample(P: int) -> dict[str, Any]:
    """给出顶行 minus-square 相位低筛覆盖样本。"""
    low_primes = primes_below(P)
    owner_counts: dict[int, int] = {}
    survivors: list[dict[str, int]] = []
    owner_word: list[dict[str, int]] = []
    for r in range(1, P):
        n = P * P - r
        owner = None
        for q in low_primes:
            if n % q == 0:
                owner = q
                break
        if owner is None:
            survivors.append({"r": r, "n": n})
        else:
            owner_counts[owner] = owner_counts.get(owner, 0) + 1
            if len(owner_word) < 16:
                owner_word.append({"r": r, "n": n, "owner": owner})
    return {
        "P": P,
        "interval": [P * P - P + 1, P * P - 1],
        "slot_count": P - 1,
        "prime_count": len(survivors),
        "first_prime": survivors[0]["n"] if survivors else None,
        "full_low_sieve_cover": len(survivors) == 0,
        "square_phase_cover_statement": "r in [1,P-1] is covered iff r == P^2 mod q for some q<P",
        "owner_counts": {str(key): owner_counts[key] for key in sorted(owner_counts)},
        "owner_word_prefix": owner_word,
        "survivor_prefix": survivors[:12],
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "FiniteSqrtGapBridgeCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "对 x=kP 且 1<k<P，有 sqrt(x)<P；因此 [x,x+sqrt(x)] 内有素数会推出 strict 行正性。",
            "remaining": "criterion only",
        },
        {
            "gate": "PublishedFiniteSqrtGapClosesInitialSegment",
            "closed": True,
            "proved": True,
            "meaning": "外部 Lemma 2.7 给出 117<=x<=10^18 时 [x,x+sqrt(x)] 有素数，阈值以下 strict 行由直接有限核查覆盖。",
            "remaining": "x>10^18 tail",
        },
        {
            "gate": "PrimeIndexedTopRowFiniteReachIdentified",
            "closed": True,
            "proved": True,
            "meaning": "顶行 x=P^2-P 的外部有限覆盖达到 P<=999999937；这清掉巨大有限初段但不触及无限尾段。",
            "remaining": "prime bases P>999999937",
        },
        {
            "gate": "TopRowFailureEquivalentToMinusSquarePhaseFullCover",
            "closed": True,
            "proved": True,
            "meaning": "N_top(P)=0 等价于每个 r=1..P-1 都满足 P^2-r 被某个 q<P 整除，即 r==P^2 mod q 的低筛禁类全覆盖。",
            "remaining": "exclude special-phase full cover",
        },
        {
            "gate": "FiniteBridgePlusGenericGapTheoremsCloseInfiniteTail",
            "closed": False,
            "proved": False,
            "meaning": "Dusart/BHP 等通用输入在 x>10^18 的 sqrt-edge 仍长于 P 或只覆盖低 k 子带。",
            "remaining": "sqrt-scale theorem or structural square-phase proof",
        },
        {
            "gate": "UnifiedPositiveCoreProved",
            "closed": False,
            "proved": False,
            "meaning": "本层只清理有限初段并把尾段反例锁到平方相位长覆盖块；没有证明所有 P,k 的正性。",
            "remaining": "SquarePhaseTailLongBlockPDECExclusion OR SquarePhaseRoughSurvivorUniformLowerBound",
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
    """输出顶行样本表。"""
    lines = [
        "| P | interval | slots | prime count | first prime | full cover | owner counts |",
        "| ---: | --- | ---: | ---: | ---: | --- | --- |",
    ]
    for item in samples:
        owner_counts = ", ".join(f"{q}:{c}" for q, c in item["owner_counts"].items())
        lines.append(
            f"| {item['P']} | {item['interval'][0]}..{item['interval'][1]} | "
            f"{item['slot_count']} | {item['prime_count']} | {item['first_prime']} | "
            f"`{fmt_bool(item['full_low_sieve_cover'])}` | {owner_counts} |"
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    small = small_direct_rows()
    threshold = top_row_threshold()
    samples = [top_row_cover_sample(P) for P in (5, 11, 17, 101, 257)]
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_finite_sqrt_square_phase_tail_router",
        "status": "finite_sqrt_gap_initial_segment_closed_tail_routed_to_square_phase_full_cover",
        "finite_sqrt_external_input": {
            "source": "Erdos-Harcos-Kharel-Maga-Mezei-Toroczkai, Math. Ann. 388 (2024), Lemma 2.7",
            "statement_used": "for every x in [117, 10^18], [x, x+sqrt(x)] contains a prime",
            "computational_source": "Oliveira e Silva-Herzog-Pardi prime-gap computation up to 4*10^18",
            "url": "https://link.springer.com/article/10.1007/s00208-023-02574-1",
            "finite_evidence_not_used_beyond_declared_range": True,
        },
        "bridge": {
            "strict_x": "x=kP",
            "strict_range": "1<k<P",
            "sqrt_x_less_than_P": True,
            "consequence": "prime in [x,x+sqrt(x)] implies pi((k+1)P-1)-pi(kP)>=1",
        },
        "small_direct_audit": small,
        "top_row_threshold": threshold,
        "top_row_square_phase_equivalence": {
            "N_top_zero": "pi(P^2-1)-pi(P^2-P)=0",
            "equivalent_full_cover": "for every 1<=r<P, gcd(P^2-r, product_{q<P} q)>1",
            "residue_word": "r == P^2 mod q for some prime q<P",
            "named_tail": "SquarePhaseTailLongBlockPDECExclusion",
        },
        "top_row_cover_samples": samples,
        "decision_rows": build_rows(),
        "unified_positive_core_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": (
            "SquarePhaseTailLongBlockPDECExclusion OR "
            "SquarePhaseRoughSurvivorUniformLowerBound OR "
            "genuine sqrt-scale theorem beyond 10^18"
        ),
        "dependency_hashes": dependency_hashes,
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    threshold = payload["top_row_threshold"]
    small = payload["small_direct_audit"]
    samples = payload["top_row_cover_samples"]
    rows = payload["decision_rows"]
    hashes = payload["dependency_hashes"]

    hash_lines = ["| file | sha256 |", "| --- | --- |"]
    for file_name, digest in hashes.items():
        hash_lines.append(f"| `{file_name}` | `{digest}` |")

    return f"""# Prime Matrix Phi-LPF strict-k finite sqrt square-phase tail 证书

**状态：** `{payload['status']}`

本层把 Phi-LPF strict 行的端点差分接入一个已发表的有限 sqrt-gap 输入：
若 `x=kP` 且 `1<k<P`，则 `sqrt(x)<P`。所以只要 `[x,x+sqrt(x)]`
内有素数，便自动得到

```text
N_P(k)=pi((k+1)P-1)-pi(kP)>=1.
```

Erdos--Harcos--Kharel--Maga--Mezei--Toroczkai 的 Lemma 2.7 给出
`117<=x<=10^18` 时 `[x,x+sqrt(x)]` 有素数；阈值以下的 strict 行由
直接有限核查覆盖。因此可能的 strict 反例必须进入 `x>10^18` 的无限尾段。

## 1. 有限 sqrt-gap 桥

```text
external_range=[{FINITE_SQRT_X_MIN}, {FINITE_SQRT_X_MAX}]
small_direct_x_limit={small['small_x_limit']}
small_checked_row_count={small['checked_row_count']}
all_small_rows_positive={fmt_bool(small['all_small_rows_positive'])}
minimum_small_row_prime_count={small['minimum_small_row_prime_count']}
```

顶行 `x=P^2-P` 的有限覆盖达到：

```text
top_row_integer_base_bound={threshold['top_row_integer_base_bound']}
largest_prime_base_with_top_row_start_le_x_max={threshold['largest_prime_base_with_top_row_start_le_x_max']}
top_row_start_at_largest_prime_base={threshold['top_row_start_at_largest_prime_base']}
```

这只清掉巨大有限初段；`P>{threshold['largest_prime_base_with_top_row_start_le_x_max']}`
的顶行尾段仍未由外部有限计算处理。

## 2. 平方相位尾段等价

顶行失败等价于：

```text
N_top(P)=0
iff for every 1<=r<P, gcd(P^2-r, product_{{q<P}} q)>1
iff [1,P-1] is covered by residue classes r == P^2 mod q, q<P.
```

也就是说，prime-indexed Oppermann-left 的尾段失败不是新的计数误差，而是
`P^2` 特殊相位启动的长度 `P-1` 低筛全覆盖块。它应进入：

```text
SquarePhaseTailLongBlockPDECExclusion
OR SquarePhaseRoughSurvivorUniformLowerBound
OR genuine sqrt-scale theorem beyond 10^18.
```

## 3. 顶行低筛覆盖样本

{sample_markdown(samples)}

## 4. 判定表

{rows_markdown(rows)}

## 5. 结论

Phi-LPF 端点差分现在与一个审稿级有限 sqrt-gap 输入接牢：所有 `kP<=10^18`
的 strict 行正性可由外部有限定理加极小初段核查覆盖。剩余不是有限验证缺口，
而是无限尾段的结构问题。最坏顶行尾段精确化为：

```text
P>999999937 and [1,P-1] fully covered by r == P^2 mod q for primes q<P.
```

这一步仍不证明 `UnifiedPositiveCore`。它把当前真剩余收缩为平方相位特殊长块的
PDEC/rough-survivor 排斥，或一个真正的 `sqrt(x)` 尺度无条件短区间定理。

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
