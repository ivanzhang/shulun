#!/usr/bin/env python3
"""生成 Dusart 2010 显式区间输入在 strict 1<k<P 行上的桥接证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_dusart_interval_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-dusart-interval-bridge-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-dusart-interval-bridge-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-dusart-interval-bridge-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-dusart-interval-bridge-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-dusart-interval-bridge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

X0_DUSART_INTERVAL = 396_738
DUSART_INTERVAL_C = 25.0
FINITE_BRIDGE_MAX_N = X0_DUSART_INTERVAL + X0_DUSART_INTERVAL // 2
AUDIT_MAX_PRIME = 10007

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json",
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
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def primes_from_flags(flags: bytearray) -> list[int]:
    """从标记表抽取素数。"""
    return [i for i, is_prime in enumerate(flags) if is_prime]


def has_prime_in_internal_row(flags: bytearray, p_len: int, k: int) -> bool:
    """检查 kP<n<(k+1)P 内是否有素数。"""
    start = k * p_len + 1
    stop = (k + 1) * p_len - 1
    return any(flags[start : stop + 1])


def dusart_interval_closes(p_len: int, k: int) -> bool:
    """Dusart 区间定理是否把 x=kP 后的素数塞进行长 P。"""
    x = k * p_len
    if x < X0_DUSART_INTERVAL:
        return False
    return k <= DUSART_INTERVAL_C * math.log(x) ** 2


def dusart_interval_margin(p_len: int, k: int) -> float:
    """返回 P - x/(25 log^2 x)。"""
    x = k * p_len
    if x <= 1:
        return float("-inf")
    return p_len - x / (DUSART_INTERVAL_C * math.log(x) ** 2)


def pi_upper_dusart_abstract(x: float) -> float:
    """Dusart 摘要中的保守 pi 上界模板。"""
    log_x = math.log(x)
    return x / log_x * (1.0 + 1.2762 / log_x)


def pi_lower_dusart_abstract(x: float) -> float:
    """Dusart 摘要中的保守 pi 下界模板。"""
    log_x = math.log(x)
    return x / log_x * (1.0 + 1.0 / log_x)


def direct_pi_endpoint_closes(p_len: int, k: int) -> bool:
    """用 Dusart 摘要 pi 双侧界直接端点相减是否已给 >=1。"""
    x = k * p_len
    y = (k + 1) * p_len - 1
    if y < 599:
        return False
    return pi_lower_dusart_abstract(y) - pi_upper_dusart_abstract(x) >= 1.0


def direct_pi_endpoint_margin(p_len: int, k: int) -> float:
    """返回 Dusart pi 双侧界给出的端点差下界减 1。"""
    x = k * p_len
    y = (k + 1) * p_len - 1
    if y < 599:
        return float("-inf")
    return pi_lower_dusart_abstract(y) - pi_upper_dusart_abstract(x) - 1.0


def finite_bridge_audit() -> dict[str, Any]:
    """验证 kP<X0 的有限桥；不作无限证明。"""
    flags = prime_sieve(FINITE_BRIDGE_MAX_N)
    primes = [p for p in primes_from_flags(flags[: X0_DUSART_INTERVAL // 2 + 2]) if p >= 3]
    checked = 0
    failures: list[dict[str, int]] = []
    max_p = 0
    max_k = 0
    for p_len in primes:
        k_max = min(p_len - 1, (X0_DUSART_INTERVAL - 1) // p_len)
        if k_max < 2:
            continue
        max_p = max(max_p, p_len)
        max_k = max(max_k, k_max)
        for k in range(2, k_max + 1):
            checked += 1
            if not has_prime_in_internal_row(flags, p_len, k):
                failures.append({"P": p_len, "k": k})
                if len(failures) >= 32:
                    break
        if len(failures) >= 32:
            break
    return {
        "finite_threshold_x0": X0_DUSART_INTERVAL,
        "sieve_max_n": FINITE_BRIDGE_MAX_N,
        "checked_rows": checked,
        "max_prime_in_bridge": max_p,
        "max_k_in_bridge": max_k,
        "failures": failures,
        "finite_bridge_verified": not failures,
        "finite_evidence_scope": "all strict rows with kP<396738",
    }


def coverage_audit(max_prime: int = AUDIT_MAX_PRIME) -> dict[str, Any]:
    """审计 Dusart 外部定理覆盖哪些 finite sample 行。"""
    flags = prime_sieve(max_prime * max_prime)
    primes = [p for p in primes_from_flags(flags[: max_prime + 1]) if p >= 5]
    total = 0
    finite_closed = 0
    direct_pi_closed = 0
    interval_closed = 0
    union_closed = 0
    uncovered: list[dict[str, Any]] = []
    sample_closed: list[dict[str, Any]] = []
    first_prime_with_uncovered: int | None = None
    last_prime_all_rows_closed: int | None = None
    for p_len in primes:
        p_total = p_len - 2
        p_union = 0
        for k in range(2, p_len):
            total += 1
            x = k * p_len
            finite = x < X0_DUSART_INTERVAL
            direct = direct_pi_endpoint_closes(p_len, k)
            interval = dusart_interval_closes(p_len, k)
            finite_closed += int(finite)
            direct_pi_closed += int(direct)
            interval_closed += int(interval)
            closed = finite or direct or interval
            if closed:
                union_closed += 1
                p_union += 1
                if len(sample_closed) < 8 and interval:
                    sample_closed.append(
                        {
                            "P": p_len,
                            "k": k,
                            "x": x,
                            "dusart_margin": dusart_interval_margin(p_len, k),
                            "direct_pi_margin": direct_pi_endpoint_margin(p_len, k),
                        }
                    )
            elif len(uncovered) < 16:
                uncovered.append(
                    {
                        "P": p_len,
                        "k": k,
                        "x": x,
                        "dusart_margin": dusart_interval_margin(p_len, k),
                        "direct_pi_margin": direct_pi_endpoint_margin(p_len, k),
                    }
                )
        if p_union == p_total:
            last_prime_all_rows_closed = p_len
        elif first_prime_with_uncovered is None:
            first_prime_with_uncovered = p_len
    return {
        "max_prime": max_prime,
        "prime_count": len(primes),
        "strict_row_count": total,
        "finite_threshold_closed_rows": finite_closed,
        "direct_pi_endpoint_bound_closed_rows": direct_pi_closed,
        "dusart_interval_closed_rows": interval_closed,
        "union_closed_rows": union_closed,
        "union_closed_ratio": union_closed / total if total else 1.0,
        "uncovered_rows_in_sample": total - union_closed,
        "first_prime_with_uncovered_row": first_prime_with_uncovered,
        "last_prime_all_rows_closed_in_sample": last_prime_all_rows_closed,
        "sample_interval_closed_rows": sample_closed,
        "sample_uncovered_rows": uncovered,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "Dusart2010IntervalInputImported",
            True,
            True,
            "外部 Dusart 2010 给出 x>=396738 后长度 x/(25 log^2 x) 的素数存在输入。",
            "external theorem accepted, not self-contained",
        ),
        row(
            "StrictRowDusartLowKBridgeClosed",
            True,
            True,
            "若 kP>=396738 且 k<=25 log^2(kP)，则 Dusart 素数落在 strict 行内。",
            "low-k logarithmic band",
        ),
        row(
            "FiniteBelowThresholdBridgeVerified",
            True,
            True,
            "kP<396738 的 strict 行已作有限桥验证。",
            "finite computation only",
        ),
        row(
            "DusartCoversAllStrictRows",
            False,
            False,
            "Dusart 长度为 x/log^2 x；在 k 接近 P 时远大于行长 P，不能覆盖全部 strict 行。",
            "sqrt-scale or anti-co-saturation still needed",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只用外部显式 PNT 闭合低 k/有限桥，不关闭全局行命题。",
            "high-k rows remain",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    finite = finite_bridge_audit()
    coverage = coverage_audit()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_dusart_interval_bridge_router",
        "status": "dusart_2010_closes_log_square_low_k_band_not_all_strict_rows",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "external_source": {
            "name": "Pierre Dusart, Estimates of some functions over primes without R.H.",
            "arxiv": "1002.0442",
            "url": "https://arxiv.org/abs/1002.0442",
            "used_statement": (
                "for x>=396738, [x, x+x/(25 log^2 x)] contains at least one prime"
            ),
            "pi_bound_templates_from_abstract": [
                "pi(x)>=x/log x*(1+1/log x) for x>=599",
                "pi(x)<=x/log x*(1+1.2762/log x) for x>1",
            ],
        },
        "strict_row_application": (
            "x=kP; if x>=396738 and k<=25 log^2(kP), then "
            "x/(25 log^2 x)<=P and the Dusart prime lies inside (kP,(k+1)P)"
        ),
        "dusart_low_k_condition": "k <= 25 log^2(kP)",
        "dusart_covers_all_strict_rows": False,
        "finite_bridge": finite,
        "coverage_audit": coverage,
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "Dusart 2010 的显式区间定理可以严格闭合 kP>=396738 且 "
            "k<=25 log^2(kP) 的 strict 行；kP<396738 由有限桥验证。"
            "但是该外部输入的长度尺度是 x/log^2 x，在 k 接近 P 时约为 "
            "P^2/log^2(P^2)，大于行长 P，因此不能替代 sqrt-scale 输入，"
            "也不能单独推出全部 1<k<P 行正性。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    finite = result["finite_bridge"]
    coverage = result["coverage_audit"]
    lines = [
        "# Prime Matrix Phi-LPF strict k Dusart interval bridge 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 外部输入",
        "",
        "```text",
        "Dusart 2010 / arXiv:1002.0442",
        result["external_source"]["used_statement"],
        *result["external_source"]["pi_bound_templates_from_abstract"],
        "```",
        "",
        "该输入作为外部定理使用；本证书不声称已经在仓库内重证 Dusart 的零点自由区和显式表。",
        "",
        "## 2. strict 行桥接",
        "",
        "```text",
        result["strict_row_application"],
        f"dusart_low_k_condition: {result['dusart_low_k_condition']}",
        "```",
        "",
        "因此 Dusart 输入闭合的是低 k 对数平方带，而不是整个 `1<k<P`。",
        "",
        "## 3. 阈值以下有限桥",
        "",
        "```text",
        f"finite_threshold_x0={finite['finite_threshold_x0']}",
        f"sieve_max_n={finite['sieve_max_n']}",
        f"checked_rows={finite['checked_rows']}",
        f"max_prime_in_bridge={finite['max_prime_in_bridge']}",
        f"max_k_in_bridge={finite['max_k_in_bridge']}",
        f"finite_bridge_verified={fmt_bool(finite['finite_bridge_verified'])}",
        "```",
        "",
        "## 4. 覆盖审计",
        "",
        "```text",
        f"max_prime={coverage['max_prime']}",
        f"strict_row_count={coverage['strict_row_count']}",
        f"finite_threshold_closed_rows={coverage['finite_threshold_closed_rows']}",
        f"direct_pi_endpoint_bound_closed_rows={coverage['direct_pi_endpoint_bound_closed_rows']}",
        f"dusart_interval_closed_rows={coverage['dusart_interval_closed_rows']}",
        f"union_closed_rows={coverage['union_closed_rows']}",
        f"union_closed_ratio={coverage['union_closed_ratio']:.6f}",
        f"uncovered_rows_in_sample={coverage['uncovered_rows_in_sample']}",
        f"first_prime_with_uncovered_row={coverage['first_prime_with_uncovered_row']}",
        f"last_prime_all_rows_closed_in_sample={coverage['last_prime_all_rows_closed_in_sample']}",
        "finite_evidence_not_used_as_global_proof=true",
        "```",
        "",
        "样本未覆盖行：",
        "",
        "| P | k | x=kP | Dusart margin P-x/(25log^2x) | direct pi margin |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in coverage["sample_uncovered_rows"]:
        lines.append(
            "| {P} | {k} | {x} | {dm:.6f} | {pm:.6f} |".format(
                P=item["P"],
                k=item["k"],
                x=item["x"],
                dm=item["dusart_margin"],
                pm=item["direct_pi_margin"],
            )
        )
    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 结论",
            "",
            "Dusart 2010 给出了有用的外部显式低 k 桥，但尺度仍是 `x/log^2 x`。",
            "对顶端 `k~P`，这比行长 `P` 大一个约 `P/log^2 P` 的因子。",
            "所以最新剩余仍是 `GlobalPaymentSmoothAntiCoSaturationInequality`、",
            "`PositiveRejectionExcessForStrictKRawLPFIncidence` 或真正的 `SqrtGapInputAfterX`。",
            "",
            "## 7. 依赖哈希",
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
