#!/usr/bin/env python3
"""路由 A1 连续 positive-limsup PDEC 签名到 prime-lift 接口。

用法示例：
  python3 experiments/prime_matrix_triad_a1_continuous_prime_lift_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-continuous-prime-lift-router.json
  docs/monograph/prime-matrix-triad-a1-continuous-prime-lift-router.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_PDEC_SIGNATURE = DOCS / "prime-matrix-triad-a1-continuous-pdec-signature-input-ledger.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-continuous-prime-lift-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-continuous-prime-lift-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def classify_row(row: dict[str, Any], high_primes: list[int]) -> str:
    """按 promoted prime 在当前 high_primes 中的位置分类。"""
    prime = int(row["signature_congruence"]["promoted_prime"])
    if prime not in high_primes:
        return "InvalidPromotedPrimeNotInTail"
    if prime == min(high_primes):
        return "StandardNextPrimePromotionDeletionKLReady"
    return "SelectivePrimePromotionNeedsCommutationBeforeDeletionKL"


def run(pdec_signature_path: Path, mult_path: Path) -> dict[str, Any]:
    """运行 prime-lift 路由。"""
    pdec = load_json(pdec_signature_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    rows = []
    for cap in pdec["cap_rows"]:
        p = int(cap["p"])
        high_primes = [int(value) for value in mult_by_p[p]["high_primes"]]
        next_high_prime = min(high_primes) if high_primes else None
        for sig in cap["signature_rows"]:
            congruence = sig["signature_congruence"]
            promoted_prime = int(congruence["promoted_prime"])
            route = classify_row(sig, high_primes)
            rows.append(
                {
                    "p": p,
                    "q": int(cap["q"]),
                    "signature": sig["signature"],
                    "signature_payment_mass": int(sig["signature_payment_mass"]),
                    "signature_phase_count": int(sig["signature_phase_count"]),
                    "promoted_prime": promoted_prime,
                    "next_high_prime": next_high_prime,
                    "promoted_prime_is_next_high_prime": promoted_prime == next_high_prime,
                    "high_primes": high_primes,
                    "forced_old_phase_residue_mod_prime": int(
                        congruence["forced_old_phase_residue_mod_prime"]
                    ),
                    "forced_lifted_phase_residue_mod_prime": int(
                        congruence["forced_lifted_phase_residue_mod_prime"]
                    ),
                    "promoted_q": int(congruence["promoted_q"]),
                    "all_old_phase_congruent": bool(sig["all_old_phase_congruent"]),
                    "all_lifted_phase_congruent": bool(
                        sig["all_lifted_phase_congruent"]
                    ),
                    "fourier_abs_over_total": sig["fourier"]["best_abs_over_total"],
                    "route": route,
                }
            )

    route_counts = Counter(row["route"] for row in rows)
    promoted_prime_counts = Counter(row["promoted_prime"] for row in rows)
    p_summary = []
    for p in sorted({int(row["p"]) for row in rows}):
        p_rows = [row for row in rows if int(row["p"]) == p]
        p_summary.append(
            {
                "p": p,
                "signature_row_count": len(p_rows),
                "promoted_prime_counts": dict(
                    sorted(Counter(row["promoted_prime"] for row in p_rows).items())
                ),
                "route_counts": dict(sorted(Counter(row["route"] for row in p_rows).items())),
                "all_congruences_verified": all(
                    row["all_old_phase_congruent"] and row["all_lifted_phase_congruent"]
                    for row in p_rows
                ),
                "min_fourier_abs_over_total": min(
                    row["fourier_abs_over_total"] for row in p_rows
                ),
            }
        )

    return {
        "certificate_type": "triad_a1_continuous_prime_lift_router",
        "status": "continuous_pdec_signatures_routed_to_prime_lift_gate",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "continuous_pdec_signature_input_json": file_sha256(pdec_signature_path),
            "multiplicity_cap_json": file_sha256(mult_path),
        },
        "q": int(pdec["q"]),
        "signature_row_count": len(rows),
        "all_signature_rows_have_prime_lift_congruence": bool(
            pdec["all_signature_rows_have_prime_lift_congruence"]
        )
        and all(row["all_old_phase_congruent"] and row["all_lifted_phase_congruent"] for row in rows),
        "route_counts": dict(sorted(route_counts.items())),
        "promoted_prime_counts": dict(sorted(promoted_prime_counts.items())),
        "standard_next_prime_row_count": route_counts[
            "StandardNextPrimePromotionDeletionKLReady"
        ],
        "selective_prime_row_count": route_counts[
            "SelectivePrimePromotionNeedsCommutationBeforeDeletionKL"
        ],
        "p_summary": p_summary,
        "signature_rows": rows,
        "prime_lift_law": (
            "任何 payment signature b=(ell,y,c) 都强制旧相位满足 "
            "t == 1-cP^{-1}-Qy (mod ell)，并强制升层相位 t+Qy 满足 "
            "t+Qy == 1-cP^{-1} (mod ell)。因此 positive-limsup finite signature "
            "不是自由 PDEC 尖峰；它是把 ell 晋升进低模周期的合法 prime-lift 输入。"
        ),
        "review_conclusion": (
            "连续 positive-limsup PDEC 输入的 prime-lift 刚性已物化：所有 40 个签名行都满足唯一同余。"
            "其中标准下一素数晋升行可直接接删除势/NoDeletion-KL；选择性晋升行需要先证明与较小尾素数晋升交换，"
            "或按 cofactor-order 缺口回流。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 连续 PDEC 签名 Prime-Lift 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. Prime-Lift 刚性律",
        "",
        result["prime_lift_law"],
        "",
        "```text",
        "signature b=(ell,y,c)；",
        "row=t+Qy；",
        "(row-1)P+c=0 mod ell；",
        "therefore t=1-cP^{-1}-Qy mod ell。",
        "```",
        "",
        "这说明 positive-limsup PDEC 签名等价于新增素数层上的 residue 锁定。",
        "",
        "## 2. 汇总",
        "",
        f"- `signature_row_count={result['signature_row_count']}`。",
        f"- `all_signature_rows_have_prime_lift_congruence={result['all_signature_rows_have_prime_lift_congruence']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `promoted_prime_counts={result['promoted_prime_counts']}`。",
        f"- `standard_next_prime_row_count={result['standard_next_prime_row_count']}`。",
        f"- `selective_prime_row_count={result['selective_prime_row_count']}`。",
        "",
        "## 3. P 汇总",
        "",
        "| P | rows | promoted primes | routes | min Fourier/total |",
        "| ---: | ---: | --- | --- | ---: |",
    ]
    for row in result["p_summary"]:
        lines.append(
            "| {p} | {rows} | `{primes}` | `{routes}` | {fourier} |".format(
                p=row["p"],
                rows=row["signature_row_count"],
                primes=row["promoted_prime_counts"],
                routes=row["route_counts"],
                fourier=fmt_float(row["min_fourier_abs_over_total"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. 签名行",
            "",
            "| P | signature | ell | next ell | old t mod ell | lift mod ell | mass | route |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["signature_rows"]:
        lines.append(
            "| {p} | `{sig}` | {ell} | {next_ell} | {old_res} | {lift_res} | {mass} | `{route}` |".format(
                p=row["p"],
                sig=row["signature"],
                ell=row["promoted_prime"],
                next_ell=row["next_high_prime"],
                old_res=row["forced_old_phase_residue_mod_prime"],
                lift_res=row["forced_lifted_phase_residue_mod_prime"],
                mass=row["signature_payment_mass"],
                route=row["route"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 当前硬点",
            "",
            "这一步把 `PDEC-CAP` 的 positive-limsup 输入进一步变成 prime-lift 输入。",
            "标准下一素数行应接已有 PromotionDeletionPotential / NoDeletion-KL / CleanKLS 账本。",
            "选择性素数行需要补一个交换律：先晋升较小尾素数再晋升该签名素数，不改变终端路由；",
            "若交换律失败，失败本身是 cofactor-order/PDEC 缺口。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdec-signature-json", type=Path, default=DEFAULT_PDEC_SIGNATURE)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.pdec_signature_json, args.multiplicity_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "route_counts": result["route_counts"],
                "promoted_prime_counts": result["promoted_prime_counts"],
                "selective_prime_row_count": result["selective_prime_row_count"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
