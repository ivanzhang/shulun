#!/usr/bin/env python3
"""为 A1 连续 actual-payment 的有限签名生成 PDEC 输入账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_continuous_pdec_signature_input_ledger.py
  python3 experiments/prime_matrix_triad_a1_continuous_pdec_signature_input_ledger.py --top-signatures 3

输出：
  docs/monograph/prime-matrix-triad-a1-continuous-pdec-signature-input-ledger.json
  docs/monograph/prime-matrix-triad-a1-continuous-pdec-signature-input-ledger.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from prime_matrix_triad_a1_continuous_actual_payment_selection import (
    canonical_phase_payments,
    fmt_float,
    positive_cap_phases,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_ACTUAL = DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
DEFAULT_CONTINUOUS = DOCS / "prime-matrix-triad-a1-continuous-direction-arc-dual.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-continuous-pdec-signature-input-ledger.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-continuous-pdec-signature-input-ledger.md"
TAU = 2.0 * math.pi


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def max_fourier_profile(g_by_phase: dict[int, int], q: int) -> dict[str, Any]:
    """计算有限签名相位剖面的最强非零 Fourier 信号。"""
    total = sum(g_by_phase.values())
    if total == 0:
        return {
            "best_h": None,
            "best_abs": 0.0,
            "best_abs_over_total": None,
            "best_direction_turn": None,
        }
    best_h = 1
    best_value = 0j
    for h in range(1, q):
        value = 0j
        for phase, mass in g_by_phase.items():
            angle = TAU * ((h * phase) % q) / q
            value += mass * complex(math.cos(angle), math.sin(angle))
        if abs(value) > abs(best_value):
            best_h = h
            best_value = value
    return {
        "best_h": best_h,
        "best_abs": abs(best_value),
        "best_abs_over_total": abs(best_value) / total,
        "best_direction_turn": (math.atan2(best_value.imag, best_value.real) % TAU) / TAU,
    }


def phase_profile_for_signature(
    p: int,
    q: int,
    h: int,
    zeta_turn: float,
    signature: str,
    mult_item: dict[str, Any],
) -> dict[str, Any]:
    """重建某个 actual payment 签名的 phase profile。"""
    m_vector = [int(value) for value in mult_item["m_vector"]]
    low_primes = [int(value) for value in mult_item["low_primes"]]
    high_primes = [int(value) for value in mult_item["high_primes"]]
    phases = positive_cap_phases(m_vector, q, h, zeta_turn)
    g_by_phase: dict[int, int] = {}
    phase_hole_hist: Counter[int] = Counter()
    for phase in phases:
        row = canonical_phase_payments(p, q, phase, low_primes, high_primes)
        count = int(row["payment_signature"].get(signature, 0))
        if count <= 0:
            continue
        g_by_phase[phase] = count
        phase_hole_hist[len(row["holes"])] += 1
    fourier = max_fourier_profile(g_by_phase, q)
    total = sum(g_by_phase.values())
    return {
        "signature": signature,
        "signature_parts": signature.split(":"),
        "signature_payment_mass": total,
        "signature_phase_count": len(g_by_phase),
        "signature_phase_mass_sample": [
            {"phase": phase, "mass": mass}
            for phase, mass in sorted(g_by_phase.items())[:20]
        ],
        "phase_hole_hist": dict(sorted(phase_hole_hist.items())),
        "fourier": fourier,
        "pdec_input_route": (
            "FiniteSignaturePDECInputMaterialized"
            if total > 0 and fourier["best_abs_over_total"] not in (None, 0.0)
            else "ZeroOrFlatSignatureNeedsDiffuseRoute"
        ),
    }


def phase_profiles_for_signatures(
    p: int,
    q: int,
    h: int,
    zeta_turn: float,
    signatures: list[str],
    mult_item: dict[str, Any],
) -> list[dict[str, Any]]:
    """一次遍历相位，重建多个 actual payment 签名的 phase profile。"""
    m_vector = [int(value) for value in mult_item["m_vector"]]
    low_primes = [int(value) for value in mult_item["low_primes"]]
    high_primes = [int(value) for value in mult_item["high_primes"]]
    phases = positive_cap_phases(m_vector, q, h, zeta_turn)
    wanted = set(signatures)
    profiles = {
        signature: {"g_by_phase": {}, "phase_hole_hist": Counter()}
        for signature in signatures
    }
    for phase in phases:
        row = canonical_phase_payments(p, q, phase, low_primes, high_primes)
        hole_count = len(row["holes"])
        for signature, count in row["payment_signature"].items():
            if signature not in wanted or count <= 0:
                continue
            profile = profiles[signature]
            profile["g_by_phase"][phase] = int(count)
            profile["phase_hole_hist"][hole_count] += 1

    rows = []
    for signature in signatures:
        g_by_phase = profiles[signature]["g_by_phase"]
        fourier = max_fourier_profile(g_by_phase, q)
        total = sum(g_by_phase.values())
        rows.append(
            {
                "signature": signature,
                "signature_parts": signature.split(":"),
                "signature_payment_mass": total,
                "signature_phase_count": len(g_by_phase),
                "signature_phase_mass_sample": [
                    {"phase": phase, "mass": mass}
                    for phase, mass in sorted(g_by_phase.items())[:20]
                ],
                "phase_hole_hist": dict(
                    sorted(profiles[signature]["phase_hole_hist"].items())
                ),
                "fourier": fourier,
                "pdec_input_route": (
                    "FiniteSignaturePDECInputMaterialized"
                    if total > 0 and fourier["best_abs_over_total"] not in (None, 0.0)
                    else "ZeroOrFlatSignatureNeedsDiffuseRoute"
                ),
            }
        )
    return rows


def analyze_cap(
    actual_row: dict[str, Any],
    mult_item: dict[str, Any],
    top_signatures: int,
) -> dict[str, Any]:
    """分析一个连续 cap 的 top actual payment 签名。"""
    p = int(actual_row["p"])
    q = int(actual_row["q"])
    h = int(actual_row["h"])
    zeta_turn = float(actual_row["zeta_turn"])
    signatures = [
        item["key"] for item in actual_row["top_payment_signature"][:top_signatures]
    ]
    rows = phase_profiles_for_signatures(
            p=p,
            q=q,
            h=h,
            zeta_turn=zeta_turn,
            signatures=signatures,
            mult_item=mult_item,
        )
    route_counts = Counter(row["pdec_input_route"] for row in rows)
    return {
        "p": p,
        "q": q,
        "h": h,
        "zeta_turn": zeta_turn,
        "total_hole_demand": int(actual_row["total_hole_demand"]),
        "top_signature_count": len(rows),
        "all_top_signatures_materialized": all(
            row["pdec_input_route"] == "FiniteSignaturePDECInputMaterialized"
            for row in rows
        )
        if rows
        else False,
        "route_counts": dict(sorted(route_counts.items())),
        "signature_rows": rows,
    }


def run(
    actual_path: Path,
    continuous_path: Path,
    mult_path: Path,
    top_signatures: int,
) -> dict[str, Any]:
    """运行 PDEC 签名输入账本。"""
    actual = load_json(actual_path)
    continuous = load_json(continuous_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    cap_rows = [
        analyze_cap(row, mult_by_p[int(row["p"])], top_signatures)
        for row in actual["cap_reports"]
        if int(row["total_hole_demand"]) > 0
    ]
    route_counts: Counter[str] = Counter()
    all_signature_rows = []
    for cap in cap_rows:
        route_counts.update(cap["route_counts"])
        all_signature_rows.extend(cap["signature_rows"])
    return {
        "certificate_type": "triad_a1_continuous_pdec_signature_input_ledger",
        "status": "continuous_positive_limsup_pdec_inputs_materialized_capacity_open",
        "q": int(continuous["q"]),
        "parameters": {"top_signatures": top_signatures},
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "continuous_actual_payment_selection_json": file_sha256(actual_path),
            "continuous_direction_arc_json": file_sha256(continuous_path),
            "multiplicity_cap_json": file_sha256(mult_path),
        },
        "cap_count": len(cap_rows),
        "signature_row_count": len(all_signature_rows),
        "route_counts": dict(sorted(route_counts.items())),
        "global_min_signature_fourier_abs_over_total": min(
            (
                row["fourier"]["best_abs_over_total"]
                for row in all_signature_rows
                if row["fourier"]["best_abs_over_total"] is not None
            ),
            default=None,
        ),
        "global_max_signature_fourier_abs_over_total": max(
            (
                row["fourier"]["best_abs_over_total"]
                for row in all_signature_rows
                if row["fourier"]["best_abs_over_total"] is not None
            ),
            default=None,
        ),
        "cap_rows": cap_rows,
        "pdec_input_law": (
            "若 canonical actual payment 的有限签名沿反例塔有正 limsup 质量，"
            "则该签名的 phase profile g_b(t) 是合法同集 PDEC 输入：它由真实完成态、真实低洞、"
            "真实 column-tail 支付桶共同定义。非零 Fourier 信号给出 PDEC 测试方向；"
            "剩余未闭合的是该方向上的容量不等式 U_CRT<L_PDEC。"
        ),
        "review_conclusion": (
            "连续 actual-payment 的 positive-limsup 分支已被物化为具体 finite-signature PDEC 输入账本。"
            "这关闭了“正 limsup 签名是否合法”的子问题；仍未关闭 PDEC-CAP 容量比较。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 连续 actual-payment PDEC 签名输入账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 输入律",
        "",
        result["pdec_input_law"],
        "",
        "```text",
        "positive-limsup finite signature b=(prime,residue,column-residue)",
        "=> g_b(t)=# canonical actual payments at phase t using b",
        "=> finite column-tail formal row",
        "=> PDEC capacity comparison U_CRT<L_PDEC still required。",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `cap_count={result['cap_count']}`。",
        f"- `signature_row_count={result['signature_row_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `global_min_signature_fourier_abs_over_total={fmt_float(result['global_min_signature_fourier_abs_over_total'])}`。",
        f"- `global_max_signature_fourier_abs_over_total={fmt_float(result['global_max_signature_fourier_abs_over_total'])}`。",
        "",
        "## 3. Cap 汇总",
        "",
        "| P | top signatures | routes |",
        "| ---: | ---: | --- |",
    ]
    for cap in result["cap_rows"]:
        lines.append(
            f"| {cap['p']} | {cap['top_signature_count']} | `{cap['route_counts']}` |"
        )

    lines.extend(
        [
            "",
            "## 4. 签名行",
            "",
            "| P | signature | mass | phases | best h | Fourier/total | route |",
            "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for cap in result["cap_rows"]:
        for row in cap["signature_rows"]:
            lines.append(
                "| {p} | `{sig}` | {mass} | {phases} | {h} | {ratio} | `{route}` |".format(
                    p=cap["p"],
                    sig=row["signature"],
                    mass=row["signature_payment_mass"],
                    phases=row["signature_phase_count"],
                    h=row["fourier"]["best_h"],
                    ratio=fmt_float(row["fourier"]["best_abs_over_total"]),
                    route=row["pdec_input_route"],
                )
            )

    lines.extend(
        [
            "",
            "## 5. 当前硬点",
            "",
            "本账本完成的是 PDEC 输入合法性与方向物化；它没有证明容量上界。",
            "下一步必须对这些 `g_b(t)` 加入同集容量行并证明：",
            "",
            "```text",
            "U_CRT(g_b; h,zeta) < L_PDEC(g_b)。",
            "```",
            "",
            "若该比较失败，失败对象应输出更窄 DualCap、缺失 column-tail/cofactor 行，或回到 diffuse CleanKLS。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--actual-json", type=Path, default=DEFAULT_ACTUAL)
    parser.add_argument("--continuous-json", type=Path, default=DEFAULT_CONTINUOUS)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--top-signatures", type=int, default=5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        actual_path=args.actual_json,
        continuous_path=args.continuous_json,
        mult_path=args.multiplicity_json,
        top_signatures=args.top_signatures,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "signature_row_count": result["signature_row_count"],
                "route_counts": result["route_counts"],
                "global_min_signature_fourier_abs_over_total": result[
                    "global_min_signature_fourier_abs_over_total"
                ],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
