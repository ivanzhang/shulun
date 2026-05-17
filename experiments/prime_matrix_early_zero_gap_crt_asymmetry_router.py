#!/usr/bin/env python3
"""生成早期零行相邻素数载体与 CRT 非对称路由证书。

用法示例：
  python3 experiments/prime_matrix_early_zero_gap_crt_asymmetry_router.py
  python3 experiments/prime_matrix_early_zero_gap_crt_asymmetry_router.py --max-p 5000
  python3 -m json.tool data/prime-matrix-early-zero-gap-crt-asymmetry-ledger.json

输出：
  data/prime-matrix-early-zero-gap-crt-asymmetry-ledger.json
  docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.json
  docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.md
"""

from __future__ import annotations

import argparse
import bisect
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

CURRENT_FRONTIER = DOCS / "prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.json"
H3_UNIFIED = DOCS / "prime-matrix-h3-unified-defect-criterion.md"
NC_BLK = DOCS / "prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md"

OUT_LEDGER = DATA / "prime-matrix-early-zero-gap-crt-asymmetry-ledger.json"
OUT_JSON = DOCS / "prime-matrix-early-zero-gap-crt-asymmetry-router.json"
OUT_MD = DOCS / "prime-matrix-early-zero-gap-crt-asymmetry-router.md"

PREVIOUS_HARDPOINT = (
    "CycleDebtBranchReplayCurrentMaterializedFrontierZeroWithFutureSchemaFirewall;"
    "GlobalFinalInputsStillOpen"
)
NEXT_HARDPOINT = (
    "EarlyZeroGapCarrierAsymmetryRoutedToH3DSBNCBLKOrExternalDIBFI;"
    "GlobalFinalInputsStillOpen"
)


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def sieve_flags(limit: int) -> bytearray:
    """返回素数标记表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    d = 2
    while d * d <= limit:
        if flags[d]:
            start = d * d
            flags[start : limit + 1 : d] = b"\x00" * (((limit - start) // d) + 1)
        d += 1
    return flags


def primes_from_flags(flags: bytearray) -> list[int]:
    """从标记表提取素数。"""
    return [n for n in range(2, len(flags)) if flags[n]]


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定门。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def audit_early_rows(max_p: int) -> dict[str, Any]:
    """有限核查早期行，并提取若出现零行时的相邻素数载体。"""
    max_prime_for_square = max_p + 100
    max_n = max_prime_for_square * max_prime_for_square
    flags = sieve_flags(max_n)
    primes = primes_from_flags(flags)
    p_values = [p for p in primes if 3 <= p <= max_p]

    zero_rows: list[dict[str, Any]] = []
    min_prime_count: int | None = None
    min_prime_count_samples: list[dict[str, Any]] = []
    rows_checked = 0

    for p in p_values:
        # 行号 r=1 含有平凡列 p；早期反例只审计 2<=r<=p。
        for row in range(2, p + 1):
            left = (row - 1) * p + 1
            right = row * p
            lo = bisect.bisect_left(primes, left)
            hi = bisect.bisect_right(primes, right)
            prime_count = hi - lo
            rows_checked += 1

            if min_prime_count is None or prime_count < min_prime_count:
                min_prime_count = prime_count
                min_prime_count_samples = []
            if prime_count == min_prime_count and len(min_prime_count_samples) < 20:
                min_prime_count_samples.append(
                    {
                        "p": p,
                        "row": row,
                        "interval": [left, right],
                        "prime_count": prime_count,
                        "primes_in_row": primes[lo:hi],
                    }
                )

            if prime_count == 0:
                prev_prime = primes[lo - 1] if lo > 0 else None
                next_prime = primes[hi] if hi < len(primes) else None
                zero_rows.append(
                    {
                        "p": p,
                        "row": row,
                        "k": row,
                        "interval": [left, right],
                        "prev_prime": prev_prime,
                        "next_prime": next_prime,
                        "carrier_gap": None
                        if prev_prime is None or next_prime is None
                        else next_prime - prev_prime,
                        "left_slack": None if prev_prime is None else left - prev_prime,
                        "right_slack": None if next_prime is None else next_prime - right,
                    }
                )

    adjacent_gaps = [
        b - a
        for a, b in zip(primes, primes[1:])
        if b <= max_p * max_p
    ]
    max_adjacent_gap_below_square = max(adjacent_gaps, default=None)

    return {
        "max_p": max_p,
        "sieve_limit": max_n,
        "prime_layers_checked": len(p_values),
        "row_windows_checked": rows_checked,
        "early_zero_rows_found": len(zero_rows),
        "early_zero_rows": zero_rows[:20],
        "min_prime_count_in_checked_rows": min_prime_count,
        "min_prime_count_samples": min_prime_count_samples,
        "max_adjacent_prime_gap_below_max_p_square": max_adjacent_gap_below_square,
    }


def build_result(max_p: int) -> dict[str, Any]:
    """构造路由证书。"""
    audit = audit_early_rows(max_p)
    current = json.loads(CURRENT_FRONTIER.read_text(encoding="utf-8"))

    gates = [
        gate(
            "EarlyZeroToStraddlingAdjacentPrimeGap",
            True,
            True,
            "若第 k 行 [(k-1)P+1,kP] 无素数，则其左右最近素数构成跨越该行的相邻素数对，间隙严格大于 P。",
            "closed",
        ),
        gate(
            "GapCarrierBelowSquareForEarlyRows",
            True,
            True,
            "若 1<k<P，则被跨越的行窗口完全位于 P^2 之前；若右侧素数越过 P^2，则反而进入更强的平方锚/对角分支。",
            "closed with square-anchor escape",
        ),
        gate(
            "CRTPeriodicityOnlyForSmallFactorCover",
            True,
            True,
            "小素因子覆盖按 M_P 周期重复，但相邻素数端点本身不是 CRT 周期对象。",
            "closed",
        ),
        gate(
            "StandaloneGapAsymmetryContradiction",
            False,
            False,
            "单个相邻素数大间隙只重述平方根长度短区间素数问题，不能单独推出全局矛盾。",
            "routes to H3/DSB or named exits",
        ),
        gate(
            "PersistentCarrierPhaseRoutesToPDECColumnCRT",
            True,
            True,
            "若相邻素数载体的端点相位在 CRT 周期中持久复现，则形成固定相位/列位移缺陷，进入 PDEC/ColumnCRT。",
            "closed as router",
        ),
        gate(
            "SparseCarrierPhaseRoutesToSAE",
            True,
            True,
            "若载体相位只孤立出现，则它是单窗逃逸而非无限结构，进入 SAE。",
            "closed as router",
        ),
        gate(
            "NonperiodicPrimeEndpointRoutesToH3DSBKLS",
            True,
            True,
            "若端点素性不能周期化，只能回到 H3 六轮尾补洞、DSB/KLS 与 NC-BLK 或外部 DI/BFI 分支。",
            "H3-DSB-NCBLK-or-external-DIBFI",
        ),
        gate(
            "NCBLKOrExternalDIBFIClosed",
            False,
            False,
            "当前仓库最新完全自足硬核仍是 NC-BLK；若不内证，只能调用外部 DI/BFI dispersion。",
            "NC-BLK or external DI/BFI",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步把用户的相邻素数/CRT 非对称提示接入现有最终硬核，不关闭全局行/列命题。",
            NEXT_HARDPOINT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_early_zero_gap_crt_asymmetry_router",
        "status": "early_zero_gap_carrier_asymmetry_routed_not_global_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_HARDPOINT,
        "current_frontier_status": current.get("status"),
        "finite_audit": audit,
        "early_zero_gap_lemma_proved": True,
        "crt_gap_asymmetry_standalone_contradiction_proved": False,
        "persistent_phase_routes_to_pdec_columncrt": True,
        "sparse_phase_routes_to_sae": True,
        "nonperiodic_endpoint_routes_to_h3_dsb_kls": True,
        "nc_blk_or_external_dibfi_closed": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_HARDPOINT,
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "早期零行确实会强制一个跨越该行的相邻素数大间隙载体；但 CRT 周期只复制小素因子覆盖，"
            "不复制素数端点。因此该非对称提示本身不是完整矛盾，而是一个路由器：持久相位进入 "
            "PDEC/ColumnCRT，孤立相位进入 SAE，非周期素端点回到 H3-DSB/KLS 的 NC-BLK 或外部 "
            "DI/BFI 最终硬核。"
        ),
        "dependency_hashes": {
            str(CURRENT_FRONTIER.relative_to(ROOT)): sha256(CURRENT_FRONTIER),
            str(H3_UNIFIED.relative_to(ROOT)): sha256(H3_UNIFIED),
            str(NC_BLK.relative_to(ROOT)): sha256(NC_BLK),
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    audit = result["finite_audit"]
    lines = [
        "# 早期零行相邻素数载体与 CRT 非对称路由",
        "",
        "**状态：** `early_zero_gap_carrier_asymmetry_routed_not_global_proof`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"early_zero_gap_lemma_proved={fmt_bool(result['early_zero_gap_lemma_proved'])}",
        "crt_gap_asymmetry_standalone_contradiction_proved="
        f"{fmt_bool(result['crt_gap_asymmetry_standalone_contradiction_proved'])}",
        "persistent_phase_routes_to_pdec_columncrt="
        f"{fmt_bool(result['persistent_phase_routes_to_pdec_columncrt'])}",
        f"sparse_phase_routes_to_sae={fmt_bool(result['sparse_phase_routes_to_sae'])}",
        "nonperiodic_endpoint_routes_to_h3_dsb_kls="
        f"{fmt_bool(result['nonperiodic_endpoint_routes_to_h3_dsb_kls'])}",
        f"nc_blk_or_external_dibfi_closed={fmt_bool(result['nc_blk_or_external_dibfi_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 相邻素数载体引理",
        "",
        "设 `P` 为奇素数，第 `k` 行为",
        "",
        "\\[",
        "I_{P,k}=[(k-1)P+1,kP].",
        "\\]",
        "",
        "若 `I_{P,k}` 中没有素数，令 `a` 为小于左端点的最大素数，`b` 为大于右端点的最小素数。则 `a,b` 之间没有其它素数，所以它们是相邻素数，且",
        "",
        "\\[",
        "b-a \\ge (kP+1)-((k-1)P)=P+1>P.",
        "\\]",
        "",
        "这严格化了“早期零行强制跨行相邻素数大间隙”的提示。",
        "",
        "## 2. CRT 非对称的精确边界",
        "",
        "小素因子覆盖集合只依赖 `mod M_P`，因此零行覆盖图案可以按 CRT 周期重复。但相邻素数端点不是小因子覆盖对象；`a+M_P` 与 `b+M_P` 没有理由仍为素数。这就是非对称的核心：周期复制的是反例覆盖链，不是素数真实链。",
        "",
        "因此单个 gap carrier 不能直接推出矛盾。要产生全局结构矛盾，必须证明这些 carrier 相位在无限链中持久复现，或证明非复现时无法支付尾补洞需求。",
        "",
        "## 3. 三分流",
        "",
        "| case | route | meaning |",
        "| --- | --- | --- |",
        "| 持久同相 gap carrier | `PDEC/ColumnCRT` | 固定端点相位或列位移重复，成为 CRT/Fourier 缺陷。 |",
        "| 孤立 gap carrier | `SAE` | 单窗逃逸，不构成无限反例结构。 |",
        "| 素端点不能周期化但覆盖仍持续 | `H3-DSB/KLS -> NC-BLK or external DI/BFI` | 回到六轮尾补洞与短窗口 Kloosterman/dispersion 硬核。 |",
        "",
        "## 4. 有限核查",
        "",
        f"- `max_p`: `{audit['max_p']}`。",
        f"- `prime_layers_checked`: `{audit['prime_layers_checked']}`。",
        f"- `row_windows_checked`: `{audit['row_windows_checked']}`。",
        f"- `early_zero_rows_found`: `{audit['early_zero_rows_found']}`。",
        f"- `min_prime_count_in_checked_rows`: `{audit['min_prime_count_in_checked_rows']}`。",
        f"- `max_adjacent_prime_gap_below_max_p_square`: `{audit['max_adjacent_prime_gap_below_max_p_square']}`。",
        "",
        "最小素数数样本：",
        "",
        "| P | row | interval | prime_count | primes_in_row |",
        "| ---: | ---: | --- | ---: | --- |",
    ]
    for sample in audit["min_prime_count_samples"][:12]:
        lines.append(
            "| {p} | {row} | `{interval}` | {count} | `{primes}` |".format(
                p=sample["p"],
                row=sample["row"],
                interval=sample["interval"],
                count=sample["prime_count"],
                primes=sample["primes_in_row"],
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
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 6. 最新剩余",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "本证书不关闭全局行/列命题；它只把“早期零行相邻素数载体”提示严格接入现有最终硬核，并排除把单个 CRT 非对称现象误当作完整证明的跳步。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    args = parser.parse_args()
    result = build_result(max_p=args.max_p)
    write_outputs(result)
    print(json.dumps({
        "status": result["status"],
        "max_p": result["finite_audit"]["max_p"],
        "row_windows_checked": result["finite_audit"]["row_windows_checked"],
        "early_zero_rows_found": result["finite_audit"]["early_zero_rows_found"],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
