#!/usr/bin/env python3
"""生成 strict 顶行 Phi-LPF perfect-tiling 剩余硬点证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_top_row_perfect_tiling_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.md
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json",
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


def prime_sieve(n: int) -> bytearray:
    """返回素数标记表。"""
    if n < 2:
        return bytearray(n + 1)
    flags = bytearray(b"\x01") * (n + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def primes_from_flags(flags: bytearray) -> list[int]:
    """从标记表抽取素数。"""
    return [i for i, is_prime in enumerate(flags) if is_prime]


def least_prime_factor(n: int, primes: list[int], flags: bytearray) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    if flags[n]:
        return n
    limit = isqrt(n)
    for p in primes:
        if p > limit:
            break
        if n % p == 0:
            return p
    return n


def top_row_interval(p_len: int) -> tuple[int, int]:
    """返回顶行内部整数区间端点。"""
    return p_len * p_len - p_len + 1, p_len * p_len - 1


def top_row_prime_count(flags: bytearray, p_len: int) -> int:
    """计算顶行内部素数个数。"""
    start, stop = top_row_interval(p_len)
    return sum(flags[start : stop + 1])


def sample_tiling(flags: bytearray, primes: list[int], p_len: int) -> dict[str, Any]:
    """生成一个顶行 LPF 铺满样本。"""
    start, stop = top_row_interval(p_len)
    bucket_counts: Counter[int] = Counter()
    prime_slots: list[int] = []
    low_carrier_examples: list[dict[str, int]] = []
    for n in range(start, stop + 1):
        lpf = least_prime_factor(n, primes, flags)
        if lpf == n:
            prime_slots.append(n)
        else:
            bucket_counts[lpf] += 1
            if len(low_carrier_examples) < 8:
                low_carrier_examples.append(
                    {
                        "slot": n,
                        "least_prime_factor": lpf,
                        "cofactor": n // lpf,
                    }
                )
    slot_count = stop - start + 1
    composite_load = sum(bucket_counts.values())
    bucket_table = [
        {"lpf_bucket": q, "count": count}
        for q, count in sorted(bucket_counts.items(), key=lambda item: item[0])
    ]
    return {
        "P": p_len,
        "top_row_internal_interval": [start, stop],
        "slot_count": slot_count,
        "prime_count": len(prime_slots),
        "composite_lpf_tiling_load": composite_load,
        "identity_slot_count_equals_prime_plus_composite": (
            slot_count == len(prime_slots) + composite_load
        ),
        "perfect_lpf_tiling": len(prime_slots) == 0,
        "prime_slots_sample": prime_slots[:12],
        "bucket_table": bucket_table,
        "low_carrier_examples": low_carrier_examples,
    }


def finite_sweep(max_prime: int = 5003) -> dict[str, Any]:
    """有限审计 LPF 完美铺满；不作全局证明。"""
    flags = prime_sieve(max_prime * max_prime)
    base_primes = primes_from_flags(flags[: max_prime + 1])
    strict_primes = [p for p in base_primes if p >= 3]
    zero_top_rows: list[dict[str, int]] = []
    min_prime_count: int | None = None
    min_cases: list[dict[str, int]] = []
    max_composite_ratio = 0.0
    max_composite_ratio_cases: list[dict[str, Any]] = []
    for p_len in strict_primes:
        prime_count = top_row_prime_count(flags, p_len)
        slot_count = p_len - 1
        composite_load = slot_count - prime_count
        ratio = composite_load / slot_count
        if prime_count == 0:
            zero_top_rows.append({"P": p_len})
        if min_prime_count is None or prime_count < min_prime_count:
            min_prime_count = prime_count
            min_cases = [{"P": p_len, "prime_count": prime_count}]
        elif prime_count == min_prime_count and len(min_cases) < 16:
            min_cases.append({"P": p_len, "prime_count": prime_count})
        if ratio > max_composite_ratio:
            max_composite_ratio = ratio
            max_composite_ratio_cases = [
                {
                    "P": p_len,
                    "prime_count": prime_count,
                    "composite_lpf_tiling_load": composite_load,
                    "slot_count": slot_count,
                    "composite_ratio": ratio,
                }
            ]
        elif ratio == max_composite_ratio and len(max_composite_ratio_cases) < 16:
            max_composite_ratio_cases.append(
                {
                    "P": p_len,
                    "prime_count": prime_count,
                    "composite_lpf_tiling_load": composite_load,
                    "slot_count": slot_count,
                    "composite_ratio": ratio,
                }
            )
    sample_ps = [5, 11, 17, 101]
    return {
        "max_prime": max_prime,
        "case_count": len(strict_primes),
        "zero_top_rows_found": zero_top_rows,
        "perfect_lpf_tiling_found_in_finite_sweep": bool(zero_top_rows),
        "all_top_rows_have_untiled_prime_slot_in_finite_sweep": not zero_top_rows,
        "minimum_untiled_prime_slots": min_prime_count,
        "minimum_cases": min_cases,
        "maximum_composite_tiling_ratio": max_composite_ratio,
        "maximum_composite_ratio_cases": max_composite_ratio_cases,
        "sample_tilings": [sample_tiling(flags, base_primes, p) for p in sample_ps],
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "TopRowPerfectTilingEquivalenceClosed",
            True,
            True,
            "N_top(P)=0 等价于所有 P-1 个顶行内部槽位被 LPF 合数桶精确铺满。",
            "exclude perfect LPF tiling",
        ),
        row(
            "DeltaPhiLocalRecursionClosed",
            True,
            True,
            "端点差分版 Phi 递推只把每个桶继续拆成较深的有序粗因子树。",
            "recursion enumerates load, does not create sign",
        ),
        row(
            "SylvesterSchurOnlyRoutesToLowCarrierPayment",
            True,
            True,
            "连续乘积定理只强制出现大素因子；若顶行无素数，该大素因子必被小载体承载。",
            "low-carrier high-prime payment injection",
        ),
        row(
            "PerfectTilingExcludedGlobally",
            False,
            False,
            "当前语料没有无条件排除所有素数 P 的顶行 LPF 完美铺满。",
            "PrimeSquareUpperCollarPrimeInput or PositiveRejectionExcess",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把正性硬点改写成 perfect-tiling 排除问题。",
            "strict row positivity still open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    sweep = finite_sweep()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_top_row_perfect_tiling_router",
        "status": "strict_k_top_row_positive_reduced_to_excluding_perfect_lpf_tiling",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "top_row_slots": "T_P={P^2-P+a:1<=a<P}",
        "top_row_prime_count": "N_top(P)=pi(P^2-1)-pi(P^2-P)",
        "lpf_bucket_count": (
            "B_q(P)=Phi(floor((P^2-1)/q),q)-Phi(floor((P^2-P)/q),q)"
        ),
        "perfect_tiling_equivalence": "N_top(P)=0 iff sum_{q<P} B_q(P)=P-1",
        "positivity_equivalence": "N_top(P)>=1 iff sum_{q<P} B_q(P)<=P-2",
        "delta_phi_recursion": (
            "Delta_j(A,B)=Delta_{j+1}(A,B)+"
            "[Phi(floor(B/p_j),p_j)-Phi(floor(A/p_j),p_j)]"
        ),
        "sylvester_schur_reading": (
            "对 P-1 个连续顶行槽位，Sylvester-Schur 定理给出一个素因子 r>P。"
            "如果顶行没有素数槽，那么 r 必被某个 2<=m<P 的小载体承载，"
            "于是该输入变成 low-carrier payment，而不是直接矛盾。"
        ),
        "perfect_tiling_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "finite_sweep": sweep,
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "Phi-LPF 端点差分给出的顶行正性不是一个新的免费正项；它等价于排除"
            " LPF 合数桶对 P-1 个顶行槽位的完美铺满。递推式只把铺满负载继续拆成"
            "有序粗因子树。经典连续乘积输入最多强制大素因子出现；在无素数顶行"
            "假设下，该大素因子会被 2<=m<P 的小载体承载，正好回到低载体 payment"
            " injection/positive rejection excess 接口。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    sweep = result["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k top row perfect tiling 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 精确铺满等价",
        "",
        "```text",
        result["top_row_slots"],
        result["top_row_prime_count"],
        result["lpf_bucket_count"],
        result["perfect_tiling_equivalence"],
        result["positivity_equivalence"],
        "```",
        "",
        "因此，顶行正性 `N_top(P)>=1` 的最窄形式不是继续展开 Phi 递推，",
        "而是证明 LPF 合数桶负载不可能达到完整槽位数 `P-1`。",
        "",
        "## 2. 端点差分递推读法",
        "",
        "```text",
        result["delta_phi_recursion"],
        "```",
        "",
        "这只是把同一批合数槽位继续按下一个粗因子层拆开；它保持精确，",
        "但自身不产生正性余量。若要推出正性，必须在某层证明至少一个槽位未被合数桶覆盖。",
        "",
        "## 3. Sylvester-Schur 输入的实际落点",
        "",
        result["sylvester_schur_reading"],
        "",
        "也就是说，经典连续乘积定理能证明大素因子泄出，但不能证明顶行中有一个槽位本身为素数。",
        "它把问题转回低载体高素数 payment injection，而不是直接给出矛盾。",
        "",
        "## 4. 有限审计边界",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"case_count={sweep['case_count']}",
        "perfect_lpf_tiling_found_in_finite_sweep="
        f"{fmt_bool(sweep['perfect_lpf_tiling_found_in_finite_sweep'])}",
        "all_top_rows_have_untiled_prime_slot_in_finite_sweep="
        f"{fmt_bool(sweep['all_top_rows_have_untiled_prime_slot_in_finite_sweep'])}",
        f"minimum_untiled_prime_slots={sweep['minimum_untiled_prime_slots']}",
        f"maximum_composite_tiling_ratio={sweep['maximum_composite_tiling_ratio']:.6f}",
        "finite_evidence_not_used_as_global_proof=true",
        "```",
        "",
        "最小未铺满素数槽样本：",
        "",
        "| P | prime count |",
        "| ---: | ---: |",
    ]
    for item in sweep["minimum_cases"]:
        lines.append(f"| {item['P']} | {item['prime_count']} |")
    lines.extend(
        [
            "",
            "最高合数铺满比例样本：",
            "",
            "| P | composite load | slot count | ratio | prime count |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in sweep["maximum_composite_ratio_cases"]:
        lines.append(
            "| {P} | {composite_lpf_tiling_load} | {slot_count} | {ratio:.6f} | {prime_count} |".format(
                P=item["P"],
                composite_lpf_tiling_load=item["composite_lpf_tiling_load"],
                slot_count=item["slot_count"],
                ratio=item["composite_ratio"],
                prime_count=item["prime_count"],
            )
        )
    lines.extend(["", "## 5. 样本铺满表", ""])
    for sample in sweep["sample_tilings"]:
        lines.extend(
            [
                f"### P={sample['P']}",
                "",
                "```text",
                f"interval={sample['top_row_internal_interval']}",
                f"slot_count={sample['slot_count']}",
                f"prime_count={sample['prime_count']}",
                f"composite_lpf_tiling_load={sample['composite_lpf_tiling_load']}",
                f"perfect_lpf_tiling={fmt_bool(sample['perfect_lpf_tiling'])}",
                "identity_slot_count_equals_prime_plus_composite="
                f"{fmt_bool(sample['identity_slot_count_equals_prime_plus_composite'])}",
                f"prime_slots_sample={sample['prime_slots_sample']}",
                "```",
                "",
                "| LPF bucket | count |",
                "| ---: | ---: |",
            ]
        )
        for bucket in sample["bucket_table"][:16]:
            lines.append(f"| {bucket['lpf_bucket']} | {bucket['count']} |")
        if len(sample["bucket_table"]) > 16:
            lines.append(f"| ... | {len(sample['bucket_table']) - 16} more buckets |")
        lines.append("")
    lines.extend(
        [
            "## 6. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 7. 结论",
            "",
            "顶行 square-collar 的正性现在被压成一个非常明确的全局排除命题：",
            "`sum_{q<P} B_q(P)=P-1` 的 perfect LPF tiling 不能发生。",
            "当前语料尚无该排除的无条件证明；剩余出口仍是",
            "`PrimeSquareUpperCollarPrimeInput`、`SqrtGapInputAfterX` 或",
            "`PositiveRejectionExcessForStrictKRawLPFIncidence`。",
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps({"status": result["status"], "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
