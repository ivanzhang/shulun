#!/usr/bin/env python3
"""Prime-square P^2±1 sandwich audit.

用法示例：
  python3 experiments/prime_matrix_prime_square_pm1_sandwich_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-prime-square-pm1-sandwich-audit.json

本证书审计一个更细的想法：既然通用短区间定理可用于 X=P^2-1
和 X=P^2+1，能否由两侧夹击把 X^0.52 自动降到 P=X^0.5。
结论是不能。±1 平移只改变常数级相位，不改变 P^1.04 的窗口长度；
夹击得到的是厚外壳，不是长度 P 的左右半窗定位。
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

SLUG = "prime-matrix-prime-square-pm1-sandwich"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
THETA = 0.52

DEPENDENCIES = [
    DOCS / "prime-matrix-prime-square-halfscale-specialization-audit.json",
    DOCS / "prime-matrix-prime-square-halfscale-specialization-audit.md",
    DOCS / "prime-matrix-external-frontier-theorem-stress-router.json",
    DOCS / "prime-matrix-hp-cramer-local-route-reset-router.md",
    DOCS / "prime-matrix-prime-square-pm-layered-wheel-alignment-router.md",
    DOCS / "prime-matrix-square-phase-jacobsthal-special-phase-router.md",
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
    """登记依赖哈希，便于审计证书是否随主文档同步刷新。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def scale_samples() -> list[dict[str, Any]]:
    """给出 ±1 平移下的窗口长度样本。"""
    rows: list[dict[str, Any]] = []
    for p in [101, 1009, 100003, 1000003]:
        plus_len = (p * p + 1) ** THETA
        minus_len = (p * p - 1) ** THETA
        rows.append(
            {
                "P": p,
                "(P^2+1)^0.52/P": round(plus_len / p, 6),
                "(P^2-1)^0.52/P": round(minus_len / p, 6),
                "right_outer_tail_estimate": int(round(max(0.0, plus_len - p))),
                "left_outer_tail_estimate": int(round(max(0.0, minus_len - p))),
            }
        )
    return rows


def build_payload() -> dict[str, Any]:
    """构造 P^2±1 夹击审计 payload。"""
    return {
        "certificate_type": "prime_matrix_prime_square_pm1_sandwich_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "pm1_sandwich_does_not_localize_theta052_to_halfscale",
        "user_question": "Can applying the x^0.52 theorem at X=P^2-1 and X=P^2+1 sandwich a prime into distance P from P^2?",
        "short_answer": "no; the ±1 endpoints give P^1.04-thick containers and do not force the guaranteed primes into the inner P-windows",
        "external_theorem_snapshot": [
            {
                "name": "Runbo Li arXiv:2308.04458v8",
                "form": "prime in [x-x^0.52,x] for all sufficiently large x",
                "status": "frontier preprint as verified on 2026-05-23",
                "url": "https://arxiv.org/abs/2308.04458",
            },
            {
                "name": "Baker-Harman-Pintz 2001",
                "form": "published pointwise short-interval exponent 0.525",
                "status": "published baseline",
            },
        ],
        "pm1_shift_analysis": {
            "formula": "(P^2±1)^theta = P^(2theta) * (1 + O(P^-2))",
            "theta": THETA,
            "after_specialization": "P^1.04 * (1 + O(P^-2))",
            "target_halfscale": "P",
            "pm1_shift_absolute_change": "O(P^(2theta-2)) = O(P^-0.96)",
            "pm1_shift_changes_exponent": False,
        },
        "scale_samples": scale_samples(),
        "sandwich_windows": [
            {
                "model": "right endpoint from P^2+1",
                "guaranteed_container": "(P^2+1, P^2+1+(P^2+1)^0.52]",
                "target_inner_window": "(P^2, P^2+P)",
                "open_outer_tail": "[P^2+P, P^2+P^1.04+O(1)]",
                "localizes_to_inner_window": False,
            },
            {
                "model": "left endpoint from P^2-1",
                "guaranteed_container": "[P^2-1-(P^2-1)^0.52, P^2-1)",
                "target_inner_window": "(P^2-P, P^2)",
                "open_outer_tail": "[P^2-P^1.04+O(1), P^2-P]",
                "localizes_to_inner_window": False,
            },
            {
                "model": "forward theorem at P^2-1",
                "guaranteed_container": "(P^2-1, P^2-1+(P^2-1)^0.52]",
                "target_inner_window": "(P^2, P^2+P)",
                "open_outer_tail": "[P^2+P, P^2+P^1.04+O(1)]",
                "localizes_to_inner_window": False,
            },
            {
                "model": "backward theorem at P^2+1",
                "guaranteed_container": "[P^2+1-(P^2+1)^0.52, P^2+1)",
                "target_inner_window": "(P^2-P, P^2)",
                "open_outer_tail": "[P^2-P^1.04+O(1), P^2-P]",
                "localizes_to_inner_window": False,
            },
        ],
        "count_obstruction": {
            "large_container_lower_bound_from_short_interval": "at_least_one_prime",
            "outer_tail_length": "P^1.04-P",
            "brun_titchmarsh_tail_capacity_order": "P^1.04/log P",
            "why_counting_does_not_close": "one guaranteed prime in the thick container can all lie in the outer tail; available upper bounds do not make the outer tail empty",
            "needed_count_dominance": "container prime lower bound > outer-tail prime upper bound",
            "available_now": False,
        },
        "factor_structure_diagnostic": [
            {
                "structure": "P^2-1=(P-1)(P+1)",
                "effect": "endpoint factorization does not constrain where the next or previous prime inside a P^1.04 container lies",
                "closes_halfscale": False,
            },
            {
                "structure": "P^2+1 square-adjacent phase",
                "effect": "gives fixed quadratic/square phase residues already captured by the square-phase routers",
                "closes_halfscale": False,
            },
            {
                "structure": "P is coprime to P^2±r for 1<=r<P",
                "effect": "removes the q=P local obstruction but leaves all q<P square-phase cover residues",
                "closes_halfscale": False,
            },
        ],
        "decision_gates": [
            {
                "gate": "PM1ShiftChangesTheta052Scale",
                "closed": True,
                "proved": True,
                "meaning": "±1 changes (P^2)^0.52 only by O(P^-0.96), not by a power of P",
                "remaining": "none",
            },
            {
                "gate": "EndpointSandwichLocalizesPrimeIntoPWindow",
                "closed": False,
                "proved": False,
                "meaning": "the endpoint theorem gives thick containers, not inner P-window localization",
                "remaining": "PM1OuterTailExclusion OR count dominance",
            },
            {
                "gate": "EndpointFactorStructureForcesHalfscale",
                "closed": False,
                "proved": False,
                "meaning": "factorization of P^2-1 and square adjacency of P^2+1 do not imply a prime in the first P slots",
                "remaining": "PrimeSquareSpecialPhaseNoOuterTailTheorem",
            },
            {
                "gate": "FiniteBoundaryPromotedToProof",
                "closed": False,
                "proved": False,
                "meaning": "finite scans remain evidence only",
                "remaining": "global proof for all sufficiently large prime P",
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
            "PM1OuterTailExclusionForTheta052Containers",
            "PrimeSquareNearestPrimeWithinPOnAtLeastOneSide",
            "TwoSidedSquarePhaseInnerWindowLocalization",
            "SquarePhaseSpecialPhaseLongBlockPDECExclusion",
            "PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC",
            "ExactExternalSqrtScaleOrGridTransferredThetaHalfSecondMoment",
            "NewSameObjectSignedDispersionOrAutomorphicProof",
        ],
        "pm1_sandwich_halfscale_closed": False,
        "pm1_sandwich_no_go_closed": True,
        "prime_square_halfscale_auto_drop_closed": False,
        "square_phase_attack_surface_identified": True,
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
    shift = payload["pm1_shift_analysis"]
    count = payload["count_obstruction"]
    lines = [
        "# Prime Square P^2±1 Sandwich Audit",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 直接回答",
        "",
        "`P^2-1` 与 `P^2+1` 的两侧夹击不能把 `0.52` 自动降到 `1/2`。",
        "原因是短区间定理给出的仍是厚度 `P^1.04` 的容器；目标只允许厚度 `P`。",
        "夹击若要成功，必须额外证明保证素数不落在外尾段，或证明容器内素数数目压过外尾段容量。",
        "",
        "## 2. ±1 平移尺度",
        "",
        "```text",
        f"formula={shift['formula']}",
        f"theta={shift['theta']}",
        f"after_specialization={shift['after_specialization']}",
        f"target_halfscale={shift['target_halfscale']}",
        f"pm1_shift_absolute_change={shift['pm1_shift_absolute_change']}",
        f"pm1_shift_changes_exponent={bool_text(shift['pm1_shift_changes_exponent'])}",
        "```",
        "",
        table(
            payload["scale_samples"],
            ["P", "(P^2+1)^0.52/P", "(P^2-1)^0.52/P", "right_outer_tail_estimate", "left_outer_tail_estimate"],
        ),
        "",
        "## 3. 夹击窗口审计",
        "",
        table(
            payload["sandwich_windows"],
            ["model", "guaranteed_container", "target_inner_window", "open_outer_tail", "localizes_to_inner_window"],
        ),
        "",
        "## 4. 计数障碍",
        "",
        "```text",
        f"large_container_lower_bound_from_short_interval={count['large_container_lower_bound_from_short_interval']}",
        f"outer_tail_length={count['outer_tail_length']}",
        f"brun_titchmarsh_tail_capacity_order={count['brun_titchmarsh_tail_capacity_order']}",
        f"needed_count_dominance={count['needed_count_dominance']}",
        f"available_now={bool_text(count['available_now'])}",
        "```",
        "",
        count["why_counting_does_not_close"],
        "",
        "## 5. 因子结构诊断",
        "",
        table(payload["factor_structure_diagnostic"], ["structure", "effect", "closes_halfscale"]),
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
        f"pm1_sandwich_halfscale_closed={bool_text(payload['pm1_sandwich_halfscale_closed'])}",
        f"pm1_sandwich_no_go_closed={bool_text(payload['pm1_sandwich_no_go_closed'])}",
        f"prime_square_halfscale_auto_drop_closed={bool_text(payload['prime_square_halfscale_auto_drop_closed'])}",
        f"square_phase_attack_surface_identified={bool_text(payload['square_phase_attack_surface_identified'])}",
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
    print("pm1_sandwich_halfscale_closed=false")
    print("pm1_sandwich_no_go_closed=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
