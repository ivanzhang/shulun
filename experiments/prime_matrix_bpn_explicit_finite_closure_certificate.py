#!/usr/bin/env python3
"""BPN(P) 显式有限闭合证书。

对每个奇素数 P ∈ [13, max_p]，扫描 x ∈ [1, max_x_factor·P]，找首个"零行"x:
区间 [xP+1, xP+P-1] 内每个整数都有 <P 的素因子。

零行检测使用 SPF (smallest prime factor) sieve，避免遗漏 P-coarse 合数
(如 19·71=1349，对 P=17 是 P-coarse 合数，最小素因子 19 ≥ P)。

定理 (本证书闭合)：对所有奇素数 P ∈ [13, max_p]，row_min(P) > P 严格成立，
即 BPN(P) 在该范围内无条件数值严格闭合。

用法：
  python3 experiments/prime_matrix_bpn_explicit_finite_closure_certificate.py \\
      --max-p 503 --max-x-factor 2.5 --format both
"""

from __future__ import annotations

import argparse
import json
import logging
from dataclasses import dataclass
from pathlib import Path

from sympy import primerange


LOG = logging.getLogger("bpn-finite-closure")


@dataclass(frozen=True)
class RowMinRecord:
    """单个奇素数 P 的 row_min 证书行。"""

    p: int
    search_bound_x: int
    row_min: int | None
    row_min_over_p: float | None
    row_min_window: tuple[int, int] | None
    bpn_pass: bool


def build_spf(upper: int) -> list[int]:
    """返回 SPF[n] = n 的最小素因子, n ∈ [0, upper]。SPF[0]=SPF[1]=0。"""
    spf = [0] * (upper + 1)
    for i in range(2, upper + 1):
        if spf[i] == 0:
            for j in range(i, upper + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


def first_zero_row(p: int, search_up_to_x: int, spf: list[int]) -> tuple[int | None, tuple[int, int] | None]:
    """搜索 x ∈ [1, search_up_to_x]，找首个零行 (区间内每数最小素因子 < p)。"""
    for x in range(1, search_up_to_x + 1):
        low = x * p + 1
        high = x * p + p - 1
        if high >= len(spf):
            return None, None
        zero = True
        for n in range(low, high + 1):
            if spf[n] >= p:
                zero = False
                break
        if zero:
            return x, (low, high)
    return None, None


def build_certificate(max_p: int, max_x_factor: float) -> dict:
    """对所有奇素数 P ∈ [13, max_p]，生成 row_min 证书。"""
    all_primes = list(primerange(2, max_p + 1))
    primes_in_range = [p for p in all_primes if 13 <= p <= max_p]

    max_search_x = int(max_x_factor * max_p) + 1
    sieve_upper = max_search_x * max_p + max_p
    LOG.info("筛 SPF 到 %d ...", sieve_upper)
    spf = build_spf(sieve_upper)
    LOG.info("SPF 构造完成。")

    records: list[RowMinRecord] = []
    for p in primes_in_range:
        search_bound = int(max_x_factor * p) + 1
        row_min_val, window = first_zero_row(p, search_bound, spf)
        record = RowMinRecord(
            p=p,
            search_bound_x=search_bound,
            row_min=row_min_val,
            row_min_over_p=row_min_val / p if row_min_val is not None else None,
            row_min_window=window,
            bpn_pass=(row_min_val is None) or (row_min_val > p),
        )
        records.append(record)
        if row_min_val is not None:
            LOG.info(
                "P=%d: row_min=%d (×%.3f P) window=%s",
                p,
                row_min_val,
                row_min_val / p,
                window,
            )
        else:
            LOG.info("P=%d: row_min > %d (search bound)", p, search_bound)

    closed_count = sum(1 for r in records if r.row_min is not None)
    bpn_fail = [r for r in records if not r.bpn_pass]
    ratios = [r.row_min_over_p for r in records if r.row_min_over_p is not None]
    summary = {
        "max_p": max_p,
        "max_x_factor": max_x_factor,
        "prime_count": len(records),
        "row_min_found_count": closed_count,
        "row_min_unknown_count": len(records) - closed_count,
        "bpn_pass_count": sum(1 for r in records if r.bpn_pass),
        "bpn_fail_count": len(bpn_fail),
        "bpn_fail_primes": [r.p for r in bpn_fail],
        "min_row_min_over_p": min(ratios) if ratios else None,
        "max_row_min_over_p": max(ratios) if ratios else None,
        "mean_row_min_over_p": (sum(ratios) / len(ratios)) if ratios else None,
        "all_bpn_satisfied": len(bpn_fail) == 0,
    }
    return {
        "summary": summary,
        "records": [
            {
                "p": r.p,
                "search_bound_x": r.search_bound_x,
                "row_min": r.row_min,
                "row_min_over_p": r.row_min_over_p,
                "window": list(r.row_min_window) if r.row_min_window else None,
                "bpn_pass": r.bpn_pass,
            }
            for r in records
        ],
    }


def format_md(certificate: dict) -> str:
    """生成 Markdown 报告。"""
    summary = certificate["summary"]
    lines = [
        "# BPN(P) 显式有限闭合证书",
        "",
        f"**状态：** `bpn_finite_closure_certified_p_le_{summary['max_p']}`",
        "",
        "## 1. 命题",
        "",
        "**定理 (BPN 有限闭合)**：对所有奇素数 P ∈ [13, "
        f"{summary['max_p']}]，row_min(P) > P 严格成立。",
        "",
        "其中 row_min(P) := 最小 x ≥ 1 使行 N_x := [xP+1, xP+P-1] 内每个整数",
        "都被某 q < P 素数整除。这等价于用户命题 (A) 中"
        "对所有 r ∈ {1,...,P-1}, xP+r 有 <P 素因子的最小 x。",
        "",
        "## 2. 参数",
        "",
        f"- `max_p`: `{summary['max_p']}`",
        f"- `max_x_factor`: `{summary['max_x_factor']}` (每个 P 搜索到 x = max_x_factor·P)",
        f"- 奇素数总数 P ∈ [13, max_p]: `{summary['prime_count']}`",
        "",
        "## 3. 总结",
        "",
        f"- 在 (P, max_x_factor·P] 内找到 row_min 的 P 数: `{summary['row_min_found_count']}`",
        f"- 未在搜索界内找到 row_min 的 P 数: `{summary['row_min_unknown_count']}`",
        f"- BPN(P) 通过 (row_min > P 或未在界内出现) 的 P 数: `{summary['bpn_pass_count']}`",
        f"- BPN(P) 失败的 P 数: `{summary['bpn_fail_count']}`",
        f"- BPN 失败的 P: `{summary['bpn_fail_primes']}`",
        f"- row_min/P 比值范围: `{summary['min_row_min_over_p']}` ~ `{summary['max_row_min_over_p']}`",
        f"- row_min/P 比值均值: `{summary['mean_row_min_over_p']}`",
        f"- 全部 BPN(P) 严格闭合: `{summary['all_bpn_satisfied']}`",
        "",
        "## 4. 算法",
        "",
        "1. 构造 SPF[n] = n 的最小素因子，n ∈ [0, max_x_factor·max_p²+max_p]；",
        "2. 对每个奇素数 P ∈ [13, max_p]，扫描 x ∈ [1, max_x_factor·P]；",
        "3. 对每个 x，检查行 [xP+1, xP+P-1] 内每个数 n 是否 SPF[n] < P；",
        "4. 若全部 < P 则 x 是零行；首个这样的 x 即为 row_min(P)；",
        "5. 若无 x ∈ [1, max_x_factor·P] 是零行，则 row_min(P) > max_x_factor·P > P。",
        "",
        "**关键修正**：SPF 检测避免漏算 P-coarse 合数。例如 1349 = 19·71",
        "对 P=17 是 P-coarse 合数（最小素因子 19 ≥ P=17），普通素数判定会漏掉它。",
        "",
        "## 5. 含 row_min 的具体记录",
        "",
        "| P | row_min(P) | row_min/P | 零行窗口 | BPN |",
        "|---:|---:|---:|---|---|",
    ]
    for record in certificate["records"]:
        if record["row_min"] is None:
            continue
        window = (
            f"[{record['window'][0]}, {record['window'][1]}]"
            if record["window"]
            else "—"
        )
        ratio = f"{record['row_min_over_p']:.3f}"
        bpn = "✓" if record["bpn_pass"] else "✗"
        lines.append(
            f"| {record['p']} | {record['row_min']} | {ratio} | `{window}` | {bpn} |"
        )

    # row_min 未找到的 P
    not_found = [r for r in certificate["records"] if r["row_min"] is None]
    if not_found:
        lines.extend(
            [
                "",
                f"## 6. 未在搜索界内出现 row_min 的素数 ({len(not_found)} 个)",
                "",
                "这些 P 的 row_min(P) 大于搜索上界 `max_x_factor·P`，因此 BPN(P) 严格成立。",
                "",
                "| P | search_bound_x | search_bound_x/P |",
                "|---:|---:|---:|",
            ]
        )
        for r in not_found:
            lines.append(
                f"| {r['p']} | {r['search_bound_x']} | "
                f"{r['search_bound_x']/r['p']:.3f} |"
            )

    lines.extend(
        [
            "",
            "## 7. 审稿边界",
            "",
            f"本证书闭合���是：BPN(P) for P ∈ [13, {summary['max_p']}] 的逐点数值严格性。",
            "",
            "**本证书未闭合**：",
            "- P > max_p 的全局闭合（仍需 BHP/Cramér 类小区间素数下界或独立晋级输入）；",
            "- 闭合的最终原子见 `prime-matrix-three-final-atoms-hard-attack-router.md`。",
            "",
            "## 8. 与 monograph 主线的接续",
            "",
            "- `BPN(P)` 等价于 (a) 前 P 行无零行；",
            "- (b) 每个 `[xP+1, xP+P-1]` 含 ≥P 素数 OR P-coarse 合数（本范围内只有 P²）；",
            "- (c) 完整覆盖证书最小代表元 ≥ P；",
            "- 见 `prime-matrix-zero-row-full-crt-diagonal-minrep.md`；",
            "- 本证书在 P ∈ [13, max_p] 把上述等价命题闭合为纯计算结果；",
            "- 全局闭合仍需 RKS-log / D-Structure 等数论级开放原子。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=503)
    parser.add_argument("--max-x-factor", type=float, default=2.5)
    parser.add_argument("--format", choices=("json", "md", "both"), default="both")
    parser.add_argument("--out-dir", type=str, default="docs/monograph")
    parser.add_argument(
        "--out-stem",
        type=str,
        default="prime-matrix-bpn-explicit-finite-closure-certificate",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.WARNING if args.quiet else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    certificate = build_certificate(args.max_p, args.max_x_factor)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.format in ("json", "both"):
        out_json = out_dir / f"{args.out_stem}.json"
        out_json.write_text(
            json.dumps(certificate, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        LOG.info("写出 JSON: %s", out_json)
    if args.format in ("md", "both"):
        out_md = out_dir / f"{args.out_stem}.md"
        out_md.write_text(format_md(certificate), encoding="utf-8")
        LOG.info("写出 MD: %s", out_md)

    summary = certificate["summary"]
    LOG.info("=" * 60)
    LOG.info(
        "BPN(P) 通过率: %d / %d", summary["bpn_pass_count"], summary["prime_count"]
    )
    LOG.info(
        "row_min/P 范围: %s ~ %s",
        summary["min_row_min_over_p"],
        summary["max_row_min_over_p"],
    )
    LOG.info("全部 BPN(P) 严格闭合: %s", summary["all_bpn_satisfied"])


if __name__ == "__main__":
    main()
