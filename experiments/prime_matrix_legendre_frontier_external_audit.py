#!/usr/bin/env python3
"""Legendre-frontier external theorem audit.

用法示例：
  python3 experiments/prime_matrix_legendre_frontier_external_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-legendre-frontier-external-audit.json

本证书审计 2026 年与 Legendre/平方间隔最相关的新外部结果：
RH 条件下的 consecutive larger powers、每个平方间有 P3 almost-prime、
以及 Guth--Maynard 的 17/30 短区间 PNT。目标是把它们精确映射到
Prime Matrix 的 P^2±P 半窗，防止把“弱化 Legendre”或 almost-prime
误写成本文所需的素数半窗定理。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-legendre-frontier-external"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-prime-square-halfscale-specialization-audit.json",
    DOCS / "prime-matrix-prime-square-pm1-sandwich-audit.json",
    DOCS / "prime-matrix-external-frontier-theorem-stress-router.json",
    DOCS / "prime-matrix-parity-breaking-obstruction-audit.json",
    DOCS / "prime-matrix-composite-p2-support-saturation-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bool_text(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def power_interval_exponent(delta: float) -> float:
    """把 (x^(2+delta),(x+1)^(2+delta)) 的长度换成 X 指数。"""
    return (1.0 + delta) / (2.0 + delta)


def build_payload() -> dict[str, Any]:
    """构造外部前沿审计 payload。"""
    delta_records = []
    for delta in [0.25, 0.10, 0.01, 0.001]:
        delta_records.append(
            {
                "delta": delta,
                "interval_power": f"2+{delta:g}",
                "length_exponent_in_X": round(power_interval_exponent(delta), 12),
                "excess_over_half": round(power_interval_exponent(delta) - 0.5, 12),
                "matches_delta_zero_legendre": False,
            }
        )
    return {
        "certificate_type": "prime_matrix_legendre_frontier_external_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "legendre_frontier_external_inputs_are_near_gates_not_prime_square_halfscale_closure",
        "external_sources": [
            {
                "name": "Chamberland-Straub, Weakening the Legendre Conjecture",
                "url": "https://arxiv.org/abs/2602.22502",
                "verified_version": "v1, submitted 2026-02-26",
                "claim_type": "RH-conditional primes between consecutive larger powers x^(2+delta)",
                "acceptance_status": "arxiv_preprint_and_RH_conditional",
                "project_role": "conditional near-gate; not delta=0 Legendre and not unconditional",
            },
            {
                "name": "Campbell, On the Existence of Integers with at Most 3 Prime Factors Between Every Pair of Consecutive Squares",
                "url": "https://arxiv.org/abs/2603.10356",
                "verified_version": "v2, 2026-05-19",
                "claim_type": "unconditional P3 almost-prime in every square interval",
                "acceptance_status": "arxiv_preprint",
                "project_role": "parity diagnostic; correct location but wrong prime object",
            },
            {
                "name": "Bordignon-Johnston-Starichkova, explicit Chen theorem and linear sieve",
                "url": "https://arxiv.org/abs/2207.09452",
                "verified_version": "v6, 2025-06-25",
                "claim_type": "explicit linear sieve / P2 additive Chen-type input",
                "acceptance_status": "to_appear",
                "project_role": "technology behind almost-prime results; linear-sieve parity remains",
            },
            {
                "name": "Guth-Maynard, New large value estimates for Dirichlet polynomials",
                "url": "https://annals.math.princeton.edu/2026/203-2/p06",
                "verified_version": "Annals 203(2), 2026",
                "claim_type": "zero-density estimate and short-interval PNT at length x^(17/30+o(1))",
                "acceptance_status": "published",
                "project_role": "deep pointwise PNT technology; exponent still above 1/2",
            },
            {
                "name": "Lee, Minimal zero-free regions for results on primes between consecutive perfect kth powers",
                "url": "https://arxiv.org/abs/2602.14340",
                "verified_version": "arXiv:2602.14340v2, 2026",
                "claim_type": "zero-free-region requirements for primes between consecutive kth powers",
                "acceptance_status": "arxiv_preprint",
                "project_role": "quantifies high-power progress toward Legendre; does not reach k=2",
            },
        ],
        "larger_powers_scale_audit": {
            "source": "Chamberland-Straub under RH",
            "statement_shape": "primes between x^(2+delta) and (x+1)^(2+delta)",
            "delta_zero_target": "Legendre/PrimeSquareHalfscale with length exponent 1/2",
            "delta_records": delta_records,
            "why_not_close": "for every fixed delta>0 the length exponent is 1/2 + delta/(2(2+delta)); delta=0 is exactly the open square case and is not supplied",
            "unconditional": False,
            "closes_prime_square_halfscale": False,
        },
        "p3_between_squares_audit": {
            "source": "Campbell 2026 v2",
            "statement_shape": "every (n^2,(n+1)^2) contains an integer with at most 3 prime factors counted with multiplicity",
            "location_matches_square_interval": True,
            "object_is_prime": False,
            "parity_barrier_diagnostic": "linear sieve can force almost-prime objects in square intervals but not a prime object",
            "closes_prime_square_halfscale": False,
        },
        "guth_maynard_scale_audit": {
            "theta": "17/30",
            "theta_decimal": round(17 / 30, 12),
            "after_x_equals_p_square": "P^(17/15)",
            "row_thickness_exponent": round(2 * (17 / 30) - 1, 12),
            "target_row_thickness": 0,
            "closes_each_p_row": False,
        },
        "decision_gates": [
            {
                "gate": "RHLargerPowersDeltaPositiveImported",
                "closed": True,
                "proved": False,
                "meaning": "registered as RH-conditional near-gate; delta=0 remains missing",
                "remaining": "DeltaZeroLegendreOrPrimeSquareHalfscale",
            },
            {
                "gate": "P3AlmostPrimeBetweenSquaresImported",
                "closed": True,
                "proved": False,
                "meaning": "registered as arXiv preprint diagnostic: P3 object in square intervals, not a prime object",
                "remaining": "P3ToPrimeParityBreakingTransfer",
            },
            {
                "gate": "LinearSieveParityBrokenByP3Result",
                "closed": False,
                "proved": False,
                "meaning": "P3 confirms location but not prime parity; it is a parity diagnostic, not a parity break",
                "remaining": "PrimeObjectExtractionFromP3OrSignedDispersion",
            },
            {
                "gate": "GuthMaynard17Over30AtHalfscale",
                "closed": False,
                "proved": False,
                "meaning": "17/30 gives P^(2/15) row thickening after X=P^2, not one row",
                "remaining": "ThetaLeHalfOrGridTransferAtHalfscale",
            },
            {
                "gate": "HighPowerZeroFreeRegionProgressImported",
                "closed": True,
                "proved": False,
                "meaning": "latest kth-power zero-free-region work quantifies progress for large k, but not k=2",
                "remaining": "SquarePowerKEqualsTwoCase",
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "neither H_P nor the external/internal versions are unconditionally closed",
                "remaining": "row_column_unconditional_closed=false",
            },
        ],
        "new_residual_basis": [
            "DeltaZeroLegendreOrPrimeSquareHalfscaleTheorem",
            "P3ToPrimeParityBreakingTransferOrObjectSensitiveSignedSieve",
            "ThetaLeHalfPointwiseShortIntervalPrimeTheorem",
            "GridTransferredThetaHalfSecondMoment",
            "PrimeSquareSpecialPhaseNoOuterTailTheorem",
            "NewSameObjectSignedDispersionOrAutomorphicProof",
        ],
        "legendre_frontier_external_inputs_imported": True,
        "rh_larger_powers_delta_zero_closed": False,
        "p3_to_prime_transfer_closed": False,
        "prime_square_halfscale_closed": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def table(rows: list[dict[str, Any]], columns: list[str]) -> str:
    """生成 Markdown 表。"""
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for row in rows:
        values = []
        for col in columns:
            value = row.get(col, "")
            if isinstance(value, bool):
                value = bool_text(value)
            values.append(str(value).replace("|", r"\|"))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    lp = payload["larger_powers_scale_audit"]
    p3 = payload["p3_between_squares_audit"]
    gm = payload["guth_maynard_scale_audit"]
    lines = [
        "# Legendre Frontier External Theorem Audit",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 直接回答",
        "",
        "2026 年 Legendre 相关外部结果确实有帮助，但都不是本文的无条件素数半窗闭合。",
        "RH 条件 larger-powers 结果避开了 `delta=0`；P3 almost-prime 结果落在正确平方区间但对象不是素数；Guth--Maynard 的 `17/30` 仍高于 `1/2`。",
        "",
        "## 2. 外部源",
        "",
        table(payload["external_sources"], ["name", "verified_version", "acceptance_status", "claim_type", "project_role", "url"]),
        "",
        "## 3. RH larger-powers 尺度",
        "",
        "```text",
        f"source={lp['source']}",
        f"statement_shape={lp['statement_shape']}",
        f"delta_zero_target={lp['delta_zero_target']}",
        f"unconditional={bool_text(lp['unconditional'])}",
        f"closes_prime_square_halfscale={bool_text(lp['closes_prime_square_halfscale'])}",
        "```",
        "",
        table(lp["delta_records"], ["delta", "interval_power", "length_exponent_in_X", "excess_over_half", "matches_delta_zero_legendre"]),
        "",
        lp["why_not_close"],
        "",
        "## 4. P3 almost-prime 诊断",
        "",
        "```text",
        f"source={p3['source']}",
        f"statement_shape={p3['statement_shape']}",
        f"location_matches_square_interval={bool_text(p3['location_matches_square_interval'])}",
        f"object_is_prime={bool_text(p3['object_is_prime'])}",
        f"closes_prime_square_halfscale={bool_text(p3['closes_prime_square_halfscale'])}",
        "```",
        "",
        p3["parity_barrier_diagnostic"],
        "",
        "## 5. Guth--Maynard 17/30 尺度",
        "",
        "```text",
        f"theta={gm['theta']}",
        f"theta_decimal={gm['theta_decimal']}",
        f"after_x_equals_p_square={gm['after_x_equals_p_square']}",
        f"row_thickness_exponent={gm['row_thickness_exponent']}",
        f"closes_each_p_row={bool_text(gm['closes_each_p_row'])}",
        "```",
        "",
        "## 6. 判定表",
        "",
        table(payload["decision_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 7. 新剩余基",
        "",
        "```text",
        *payload["new_residual_basis"],
        "```",
        "",
        "## 8. 边界声明",
        "",
        "```text",
        f"legendre_frontier_external_inputs_imported={bool_text(payload['legendre_frontier_external_inputs_imported'])}",
        f"rh_larger_powers_delta_zero_closed={bool_text(payload['rh_larger_powers_delta_zero_closed'])}",
        f"p3_to_prime_transfer_closed={bool_text(payload['p3_to_prime_transfer_closed'])}",
        f"prime_square_halfscale_closed={bool_text(payload['prime_square_halfscale_closed'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("legendre_frontier_external_inputs_imported=true")
    print("prime_square_halfscale_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
