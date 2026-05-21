#!/usr/bin/env python3
"""生成 Phi-LPF 端点区间差分计数证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_endpoint_interval_difference_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-endpoint-interval-difference-router.json

输出：
  data/prime-matrix-phi-lpf-endpoint-interval-difference-ledger.json
  docs/monograph/prime-matrix-phi-lpf-endpoint-interval-difference-router.json
  docs/monograph/prime-matrix-phi-lpf-endpoint-interval-difference-router.md
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

SLUG = "prime-matrix-phi-lpf-endpoint-interval-difference"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def spf_upto(n: int) -> list[int]:
    """返回最小素因子表；spf[1]=1。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def phi_count(x: int, p: int, spf: list[int]) -> int:
    """计算 Phi(x,p)：1<=n<=x 且所有素因子都不小于 p 的 n 个数。"""
    if x <= 0:
        return 0
    return sum(1 for n in range(1, x + 1) if n == 1 or spf[n] >= p)


def prime_count_interval_direct(a: int, b: int, spf: list[int]) -> int:
    """直接数闭区间 [a,b] 内的素数。"""
    return sum(1 for n in range(max(2, a), b + 1) if spf[n] == n)


def lpf_endpoint_interval_count(a: int, b: int) -> dict[str, Any]:
    """用 Phi-LPF 端点差分精确计算闭区间 [a,b] 内素数个数。"""
    if a < 2 or b < a:
        raise ValueError("本证书只审计 2<=a<=b 的闭区间")
    spf = spf_upto(b)
    bucket_rows: list[dict[str, int]] = []
    composite_count = 0
    for p in primes_upto(isqrt(b)):
        right = phi_count(b // p, p, spf)
        left = phi_count((a - 1) // p, p, spf)
        delta = right - left
        if delta:
            bucket_rows.append({"p": p, "right_phi": right, "left_phi": left, "delta": delta})
        composite_count += delta
    length = b - a + 1
    formula_count = length - composite_count
    direct_count = prime_count_interval_direct(a, b, spf)
    return {
        "a": a,
        "b": b,
        "length": length,
        "composite_count_by_lpf_endpoint_difference": composite_count,
        "prime_count_by_endpoint_difference": formula_count,
        "prime_count_direct": direct_count,
        "formula_matches_direct": formula_count == direct_count,
        "nonzero_bucket_deltas": bucket_rows,
    }


def egcd(a: int, b: int) -> tuple[int, int, int]:
    """扩展欧几里得。"""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def inv_mod(a: int, m: int) -> int:
    """求模逆。"""
    g, x, _ = egcd(a % m, m)
    if g != 1:
        raise ValueError("模逆不存在")
    return x % m


def crt_pair(a1: int, m1: int, a2: int, m2: int) -> tuple[int, int]:
    """合并两个互素 CRT 条件。"""
    t = ((a2 - a1) * inv_mod(m1, m2)) % m2
    modulus = m1 * m2
    return (a1 + m1 * t) % modulus, modulus


def crt(congruences: list[tuple[int, int]]) -> tuple[int, int]:
    """合并一组两两互素 CRT 条件。"""
    a, m = congruences[0]
    for a2, m2 in congruences[1:]:
        a, m = crt_pair(a, m, a2, m2)
    return a, m


def aligned_prime_free_block(p_len: int) -> dict[str, Any]:
    """构造一个闭区间 [kP,kP+P] 内全合数的 CRT 样本。"""
    witnesses = primes_upto(200)
    q_list = [q for q in witnesses if q > p_len and q % p_len != 0][: max(0, p_len - 1)]
    congruences = []
    interior: list[dict[str, int]] = []
    for r, q in enumerate(q_list, start=1):
        residue = (-r * inv_mod(p_len, q)) % q
        congruences.append((residue, q))
        interior.append({"r": r, "forced_divisor": q, "k_mod_q": residue})
    k, modulus = crt(congruences) if congruences else (2, 1)
    while k <= 1:
        k += modulus
    a = k * p_len
    b = a + p_len
    audit = lpf_endpoint_interval_count(a, b)
    values = []
    for r in range(0, p_len + 1):
        n = a + r
        divisor = p_len if r in (0, p_len) else interior[r - 1]["forced_divisor"]
        values.append({"r": r, "n": n, "witness_divisor": divisor, "composite": n % divisor == 0})
    return {
        "P": p_len,
        "k": k,
        "crt_modulus": modulus,
        "interval": [a, b],
        "interior_crt_conditions": interior,
        "all_values_composite_by_witness": all(item["composite"] for item in values),
        "values": values,
        "endpoint_difference_audit": audit,
    }


def sample_intervals() -> list[dict[str, Any]]:
    """给出若干 [kP,kP+P] 端点差分样本。"""
    params = [(5, 2), (7, 10), (11, 30), (13, 40)]
    return [
        {
            "P": p_len,
            "k": k,
            "endpoint_difference_audit": lpf_endpoint_interval_count(k * p_len, k * p_len + p_len),
        }
        for p_len, k in params
    ]


def build_rows(crt_block: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "EndpointDifferenceIdentityClosed",
            True,
            True,
            "Pi(B)-Pi(A-1) 可写成长度减去所有 LPF 桶的 Phi 端点差分。",
            "exact identity, not an asymptotic",
        ),
        row(
            "KPToKPPlusPFormulaClosed",
            True,
            True,
            "对闭区间 [kP,kP+P]，长度项为 P+1，合数项为 p<=sqrt(kP+P) 的 Phi 差分和。",
            "P+1 - sum_p Delta_Phi_p",
        ),
        row(
            "MechanicalExactComputationAvailable",
            True,
            True,
            "给定 k,P 后可机械计算精确素数个数，并与直接筛一致。",
            "finite endpoint computation",
        ),
        row(
            "IntervalPositivityFromIdentityAlone",
            False,
            False,
            "恒等式本身不提供 Delta_Phi 总和小于长度的全局不等式。",
            "need upper bound on composite bucket increments",
        ),
        row(
            "UniversalPrimeInEveryAlignedInterval",
            False,
            False,
            "任意固定 P 都可用 CRT 构造某个 k，使 [kP,kP+P] 全为合数；因此该全称命题为假。",
            f"sample P={crt_block['P']} gives prime_count=0",
        ),
        row(
            "UsefulFiniteVerificationBoundary",
            True,
            False,
            "端点差分适合作为有限验证和局部审计工具；若要突破需另加平均、相位或容量不等式。",
            "signed/phase lower bound still required",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只建立区间精确计数与 CRT 阻断；未证明三命题无条件闭合。",
            "offdiagonal signed seed, internal transition, source/side gates, tail package",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    crt_block = aligned_prime_free_block(5)
    samples = sample_intervals()
    rows = build_rows(crt_block)
    return {
        "certificate_type": "prime_matrix_phi_lpf_endpoint_interval_difference_router",
        "status": "phi_lpf_endpoint_interval_difference_identity_closed_but_positivity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "closed_interval_formula": (
            "pi(B)-pi(A-1)=(B-A+1)-sum_{p<=sqrt(B)}"
            "[Phi(floor(B/p),p)-Phi(floor((A-1)/p),p)] for 2<=A<=B"
        ),
        "kp_interval_formula": (
            "pi(kP+P)-pi(kP-1)=P+1-sum_{p<=sqrt(kP+P)}"
            "[Phi(floor((kP+P)/p),p)-Phi(floor((kP-1)/p),p)]"
        ),
        "half_open_kp_interval_formula": (
            "pi(kP+P-1)-pi(kP-1)=P-sum_{p<=sqrt(kP+P-1)}"
            "[Phi(floor((kP+P-1)/p),p)-Phi(floor((kP-1)/p),p)]"
        ),
        "endpoint_difference_identity_proved": True,
        "kp_to_kp_plus_p_formula_proved": True,
        "mechanical_exact_computation_available": True,
        "interval_positivity_from_identity_alone_proved": False,
        "universal_prime_in_every_aligned_interval_proved": False,
        "crt_aligned_prime_free_block_exists": True,
        "row_column_unconditional_closed": False,
        "sample_intervals": samples,
        "crt_prime_free_block_sample": crt_block,
        "gates": rows,
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve())
        },
        "plain_conclusion": (
            "Phi-LPF 精准桶恒等式可以直接用于两个端点求差，得到 [kP,kP+P] 内素数个数的精确公式。"
            "但这只是精确计数表达式；要推出区间内必有素数，还必须证明 LPF 合数桶端点增量之和小于区间长度。"
            "该正性不能由恒等式本身给出，而且任意固定 P 都存在 CRT 对齐的 [kP,kP+P] 全合数区间。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF endpoint interval difference 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 端点差分公式",
        "",
        "闭区间 `2<=A<=B`：",
        "",
        "```text",
        result["closed_interval_formula"],
        "```",
        "",
        "闭区间 `[kP,kP+P]`：",
        "",
        "```text",
        result["kp_interval_formula"],
        "```",
        "",
        "半开区间 `[kP,kP+P)`：",
        "",
        "```text",
        result["half_open_kp_interval_formula"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 样本审计",
            "",
            "| P | k | interval | length | LPF composite delta | endpoint prime count | direct prime count | ok |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for sample in result["sample_intervals"]:
        audit = sample["endpoint_difference_audit"]
        lines.append(
            f"| {sample['P']} | {sample['k']} | [{audit['a']},{audit['b']}] | "
            f"{audit['length']} | {audit['composite_count_by_lpf_endpoint_difference']} | "
            f"{audit['prime_count_by_endpoint_difference']} | {audit['prime_count_direct']} | "
            f"`{fmt_bool(audit['formula_matches_direct'])}` |"
        )
    block = result["crt_prime_free_block_sample"]
    block_audit = block["endpoint_difference_audit"]
    lines.extend(
        [
            "",
            "## 4. CRT 对齐零素数区间样本",
            "",
            f"`P={block['P']}, k={block['k']}, interval={block['interval']}`",
            "",
            "```text",
            f"all_values_composite_by_witness={fmt_bool(block['all_values_composite_by_witness'])}",
            f"endpoint_prime_count={block_audit['prime_count_by_endpoint_difference']}",
            f"direct_prime_count={block_audit['prime_count_direct']}",
            "```",
            "",
            "| r | n=kP+r | witness divisor | composite |",
            "| ---: | ---: | ---: | --- |",
        ]
    )
    for item in block["values"]:
        lines.append(
            f"| {item['r']} | {item['n']} | {item['witness_divisor']} | `{fmt_bool(item['composite'])}` |"
        )
    lines.extend(
        [
            "",
            "## 5. 结论",
            "",
            "端点差分公式可以作为精确局部审计器和有限验证器；它不能单独闭合区间正性。下一步若继续沿此路走，必须新增对",
            "`sum Delta_Phi_p` 的结构性上界，或引入平均相位、signed payload、容量压力等额外信息。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
