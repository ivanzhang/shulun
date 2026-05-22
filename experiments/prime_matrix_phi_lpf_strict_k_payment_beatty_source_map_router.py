#!/usr/bin/env python3
"""生成 strict 行 low-carrier payment 的 Beatty 近倍数源映射证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_payment_beatty_source_map_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-router.md
"""

from __future__ import annotations

from array import array
from bisect import bisect_right
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-payment-beatty-source-map"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json",
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


def prime_prefix(flags: bytearray) -> array:
    """构造 pi(x) 前缀表。"""
    prefix = array("I", [0]) * len(flags)
    count = 0
    for i, is_prime in enumerate(flags):
        if is_prime:
            count += 1
        prefix[i] = count
    return prefix


def pi_between(prefix: array, lower_exclusive: int, upper_inclusive: int) -> int:
    """计算 lower < prime <= upper 的素数个数。"""
    if upper_inclusive <= lower_exclusive:
        return 0
    return int(prefix[upper_inclusive]) - int(prefix[lower_exclusive])


def h_m_sum(prefix: array, p_len: int, k: int) -> int:
    """按 H_m 定义计算 low-carrier payment 总量。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    total = 0
    for m in range(2, k + 1):
        total += pi_between(prefix, lower // m, upper // m)
    return total


def beatty_sources(primes: list[int], p_len: int, k: int, sample_limit: int = 10) -> dict[str, Any]:
    """按源素数近倍数准则计算 payment 源表。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    source_upper = upper // 2
    count = 0
    samples: list[dict[str, int]] = []
    max_slot = 0
    min_slot: int | None = None
    start = bisect_right(primes, p_len)
    stop = bisect_right(primes, source_upper)
    for r in primes[start:stop]:
        residue = lower % r
        # 因为 r>P>k，r 不整除 kP，residue 非零；slot 是下一倍数距离。
        slot = r - residue
        if 1 <= slot <= p_len - 1:
            m = (lower + slot) // r
            if not (2 <= m <= k and lower < m * r <= upper):
                raise AssertionError("Beatty 源映射产生非法 payment 槽")
            count += 1
            max_slot = max(max_slot, slot)
            min_slot = slot if min_slot is None else min(min_slot, slot)
            if len(samples) < sample_limit:
                samples.append(
                    {
                        "r": r,
                        "source_row": r // p_len,
                        "m": m,
                        "slot": slot,
                        "residue_kP_mod_r": residue,
                        "n": lower + slot,
                    }
                )
    return {
        "beatty_payment_count": count,
        "source_upper": source_upper,
        "sample_sources": samples,
        "min_slot": min_slot,
        "max_slot": max_slot,
    }


def row_summary(primes: list[int], prefix: array, p_len: int, k: int) -> dict[str, Any]:
    """汇总一行的 H_m 与 Beatty 源映射一致性。"""
    hm = h_m_sum(prefix, p_len, k)
    beatty = beatty_sources(primes, p_len, k)
    return {
        "P": p_len,
        "k": k,
        "hm_payment_count": hm,
        "beatty_payment_count": beatty["beatty_payment_count"],
        "counts_match": hm == beatty["beatty_payment_count"],
        "source_upper": beatty["source_upper"],
        "min_slot": beatty["min_slot"],
        "max_slot": beatty["max_slot"],
        "sample_sources": beatty["sample_sources"],
    }


def finite_sweep(max_prime: int = 257) -> dict[str, Any]:
    """有限审计 Beatty 源映射；不作为全局证明。"""
    sample_pairs = [(11, 10), (101, 50), (101, 100), (571, 438), (1009, 1008)]
    sieve_prime = max(max_prime, max(p for p, _k in sample_pairs))
    flags = prime_sieve(sieve_prime * sieve_prime)
    prefix = prime_prefix(flags)
    primes = primes_from_flags(flags)
    strict_primes = [p for p in primes if 5 <= p <= max_prime]
    row_count = 0
    mismatch_rows: list[dict[str, int]] = []
    max_payment = {"value": -1, "cases": []}
    max_slot_ratio = {"value": -1.0, "cases": []}
    sample_rows: list[dict[str, Any]] = []

    for p_len in strict_primes:
        for k in range(2, p_len):
            row_count += 1
            summary = row_summary(primes, prefix, p_len, k)
            if not summary["counts_match"] and len(mismatch_rows) < 32:
                mismatch_rows.append({"P": p_len, "k": k})
            payment = summary["hm_payment_count"]
            case = {
                "P": p_len,
                "k": k,
                "payment": payment,
                "source_upper": summary["source_upper"],
                "max_slot": summary["max_slot"],
            }
            if payment > max_payment["value"]:
                max_payment = {"value": payment, "cases": [case]}
            elif payment == max_payment["value"] and len(max_payment["cases"]) < 8:
                max_payment["cases"].append(case)
            ratio = summary["max_slot"] / (p_len - 1) if p_len > 1 else 0.0
            if ratio > max_slot_ratio["value"]:
                max_slot_ratio = {"value": ratio, "cases": [case]}
            elif ratio == max_slot_ratio["value"] and len(max_slot_ratio["cases"]) < 8:
                max_slot_ratio["cases"].append(case)

    for p_len, k in sample_pairs:
        sample_rows.append(row_summary(primes, prefix, p_len, k))

    return {
        "max_prime": max_prime,
        "sieve_prime_for_large_samples": sieve_prime,
        "prime_count": len(strict_primes),
        "strict_row_count": row_count,
        "all_hm_counts_match_beatty_source_map": not mismatch_rows,
        "mismatch_rows": mismatch_rows,
        "max_payment": max_payment,
        "max_slot_ratio": max_slot_ratio,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "UniqueCarrierForSourcePrimeClosed",
            True,
            True,
            "固定源素数 r>P 时，区间 (kP/r,((k+1)P-1)/r] 长度小于 1，因此至多一个 carrier。",
            "unique carrier",
        ),
        row(
            "BeattyCarrierFormulaClosed",
            True,
            True,
            "若存在 carrier，则必为 m=floor(kP/r)+1。",
            "canonical carrier",
        ),
        row(
            "NearMultipleResidueCriterionClosed",
            True,
            True,
            "payment 槽位为 a=r-(kP mod r)，且 payment 当且仅当 1<=a<P。",
            "near-multiple source criterion",
        ),
        row(
            "HmPaymentEqualsBeattySourceCountClosed",
            True,
            True,
            "sum_{2<=m<=k} H_m(k,P) 等于满足近倍数准则的下半源素数个数。",
            "exact source-table equality",
        ),
        row(
            "ZeroRowReducedToBeattySourcePlusSmoothTiling",
            True,
            True,
            "零行反设等价于 Beatty 近倍数源像与 P-smooth 槽铺满全部行槽。",
            "Beatty-source image + smooth = all slots",
        ),
        row(
            "BeattySmoothAntiTilingProved",
            False,
            False,
            "当前语料尚未证明 Beatty 近倍数源像不能与 P-smooth 槽完美铺满。",
            "Beatty smooth anti-tiling inequality",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层规范化 payment 源表，但不证明 strict 行正性。",
            "anti-tiling, rejection excess, or sqrt-scale input",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    sweep = finite_sweep()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_payment_beatty_source_map_router",
        "status": "strict_k_low_carrier_payment_rewritten_as_unique_beatty_near_multiple_source_map",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "strict_k_range": "1<k<P",
        "canonical_map": {
            "source_range": "P<r<=floor(((k+1)P-1)/2), r prime",
            "carrier": "m=floor(kP/r)+1",
            "slot": "a=m*r-kP=r-(kP mod r)",
            "payment_condition": "1<=a<P",
        },
        "beatty_smooth_anti_tiling_proved": False,
        "row_column_unconditional_closed": False,
        "finite_sweep": sweep,
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "low-carrier payment 的下半源注入可被完全规范成唯一 Beatty 近倍数映射："
            "源素数 r>P 是否支付目标行，只取决于 kP mod r 是否落在 r-P+1 到 r-1 的尾段。"
            "因此零行反例必须由这张近倍数源像与 P-smooth 槽完美铺满；当前层未证明该"
            "Beatty/smooth 反铺满不等式。"
        ),
    }


def compact_case(case: dict[str, Any]) -> str:
    """渲染紧凑样本。"""
    return (
        f"P={case['P']}, k={case['k']}, pay={case['payment']}, "
        f"source_upper={case['source_upper']}, max_slot={case['max_slot']}"
    )


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    sweep = result["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k payment Beatty source-map 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 唯一近倍数源映射",
        "",
        "对 strict 行 `1<k<P`，low-carrier payment 源素数满足：",
        "",
        "```text",
        "P<r<=floor(((k+1)P-1)/2), r prime",
        "m=floor(kP/r)+1",
        "a=m*r-kP=r-(kP mod r)",
        "payment iff 1<=a<P",
        "```",
        "",
        "因为 `P/r<1`，固定 `r` 的 carrier 至多一个；因此 payment 源表不是可自由选择的多值关系，",
        "而是一张由 `kP mod r` 决定的唯一近倍数表。",
        "",
        "## 2. 与 H_m payment 的一致性",
        "",
        "```text",
        "sum_{2<=m<=k} H_m(k,P)",
        "= #{prime r>P: a=r-(kP mod r) lies in [1,P-1]}",
        "```",
        "",
        "零行反设被改写为：",
        "",
        "```text",
        "all slots = image(Beatty near-multiple prime sources) union P-smooth slots",
        "```",
        "",
        "## 3. 有限审计",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"strict_row_count={sweep['strict_row_count']}",
        f"all_hm_counts_match_beatty_source_map={fmt_bool(sweep['all_hm_counts_match_beatty_source_map'])}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(sweep['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最大 payment 样本：",
        "",
        "| value | cases |",
        "| ---: | --- |",
        f"| {sweep['max_payment']['value']} | "
        f"{'; '.join(compact_case(c) for c in sweep['max_payment']['cases'])} |",
        "",
        "样本行：",
        "",
        "| P | k | H_m payment | Beatty count | source upper | sample sources |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in sweep["sample_rows"]:
        sources = "; ".join(
            f"r={src['r']},m={src['m']},a={src['slot']}" for src in item["sample_sources"][:5]
        )
        lines.append(
            f"| {item['P']} | {item['k']} | {item['hm_payment_count']} | "
            f"{item['beatty_payment_count']} | {item['source_upper']} | {sources} |"
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 结论",
            "",
            "本层把 low-carrier payment 的源注入从抽象计数改写为显式近倍数判别。",
            "这进一步排除 payment 选择自由：失败若存在，必须表现为 Beatty 尾段源像与",
            "`P`-smooth 槽的完美铺满。剩余硬点为 `BeattySmoothAntiTilingInequality`，",
            "或回到 raw/rejection strict excess，或提交真正的 sqrt-scale 输入。",
            "",
            "## 6. 依赖哈希",
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
    print(
        json.dumps(
            {"status": result["status"], "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)]},
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
