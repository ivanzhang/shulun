#!/usr/bin/env python3
"""Prime square half-scale specialization audit.

用法示例：
  python3 experiments/prime_matrix_prime_square_halfscale_specialization_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-prime-square-halfscale-specialization-audit.json

本证书回答一个精确问题：通用短区间素数定理的当前最强指数
theta=0.52，在特殊端点 X=P^2 且 P 为素数时，是否可由端点因子结构
自动降到 theta=1/2。本证书只登记可证明的结构收益与仍开放的缺口，
不把有限验证或平均外部定理改名为全局证明。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-prime-square-halfscale-specialization"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

FINITE_BOUNDARY_JSON = DOCS / "prime-matrix-postsquare-first-half-finite-boundary-router.json"

DEPENDENCIES = [
    DOCS / "prime-matrix-prime-base-exponent-half-barrier-router.json",
    FINITE_BOUNDARY_JSON,
    DOCS / "prime-matrix-terminal-row-square-phase-bridge-router.json",
    DOCS / "prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json",
    DOCS / "prime-matrix-inverse-alignment-two-frontier-direct-attack-router.json",
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-wheel6-capacity-router.json",
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


def load_finite_boundary() -> dict[str, Any]:
    """读取既有平方后前半窗有限审计。"""
    if not FINITE_BOUNDARY_JSON.exists():
        return {
            "available": False,
            "max_p": None,
            "prime_count": None,
            "failure_count": None,
            "max_ratio_record": None,
        }
    payload = json.loads(FINITE_BOUNDARY_JSON.read_text(encoding="utf-8"))
    scan = payload.get("finite_scan", {})
    params = scan.get("parameters", {})
    return {
        "available": True,
        "max_p": params.get("max_p"),
        "prime_count": scan.get("prime_count"),
        "failure_count": scan.get("failure_count"),
        "max_ratio_record": scan.get("max_ratio_record"),
        "first_failure": scan.get("first_failure"),
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite = load_finite_boundary()
    return {
        "certificate_type": "prime_matrix_prime_square_halfscale_specialization_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "prime_square_endpoint_structure_is_attack_surface_not_halfscale_theorem",
        "user_question": "Can X=P^2 with prime P lower the 0.52 short-interval exponent to 1/2?",
        "short_answer": "not by currently known unconditional theorems; prime-square structure gives a special square-phase route but no automatic exponent drop",
        "theta_conversion": [
            {
                "input": "Baker-Harman-Pintz 0.525",
                "x_scale": "X",
                "after_x_equals_p_square": "P^1.05",
                "target_length": "P",
                "directly_sufficient": False,
            },
            {
                "input": "Runbo Li arXiv:2308.04458 v8 0.52",
                "x_scale": "X",
                "after_x_equals_p_square": "P^1.04",
                "target_length": "P",
                "directly_sufficient": False,
            },
            {
                "input": "needed prime-square half-scale theorem",
                "x_scale": "X^(1/2) on X=P^2",
                "after_x_equals_p_square": "P",
                "target_length": "P",
                "directly_sufficient": True,
            },
        ],
        "right_window_target": {
            "name": "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP",
            "statement": "for every sufficiently large prime P, pi(P^2+P)-pi(P^2)>0, equivalently a prime in (P^2,P^2+P)",
            "current_corpus_proved": False,
            "finite_boundary": finite,
        },
        "left_window_target": {
            "name": "PrimeIndexedOppermannLeftTopRow",
            "statement": "prime in (P^2-P,P^2) for every prime P",
            "role": "Phi-LPF strict top row; parallel square-root half-window",
            "current_corpus_proved": False,
        },
        "provable_prime_square_structure": [
            {
                "structure": "q=P is harmless",
                "meaning": "for 1<=r<P, P does not divide P^2+r or P^2-r",
                "effect": "removes one trivial local obstruction only",
            },
            {
                "structure": "square-phase CRT vector",
                "meaning": "for q<P, the forbidden residue is r≡-P^2 mod q on the right and r≡P^2 mod q on the left",
                "effect": "turns the problem into a special square-phase long-block avoidance problem",
            },
            {
                "structure": "survivor-to-prime gate",
                "meaning": "if P^2±r avoids all prime divisors q<P for 1<=r<P, then it is prime",
                "effect": "converts a full low-prime-cover exclusion into a prime existence theorem",
            },
            {
                "structure": "local wheel deletions",
                "meaning": "parity and 6-wheel factors delete some candidate cofactors",
                "effect": "gives real finite/capacity tightening but not a global lower bound",
            },
        ],
        "decision_gates": [
            {
                "gate": "ExternalTheta052SpecializedToPrimeSquare",
                "closed": True,
                "proved": True,
                "meaning": "substitution X=P^2 gives length P^1.04, still longer than P",
                "remaining": "theta<=1/2 or prime-square-specific theorem",
            },
            {
                "gate": "PrimeFactorStructureAutomaticallyDropsExponent",
                "closed": False,
                "proved": False,
                "meaning": "the endpoint being a prime square gives CRT phase rigidity, not a known density theorem",
                "remaining": "SquarePhaseSpecialPhaseLongBlockPDECExclusion OR PrimeSquareEndpointNoExceptionalPhaseTheorem",
            },
            {
                "gate": "RightFirstHalfPrimeSquareFiniteBoundary",
                "closed": bool(finite.get("available")) and finite.get("failure_count") == 0,
                "proved": False,
                "meaning": "finite scan has no failure but is not a proof",
                "remaining": "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP",
            },
            {
                "gate": "PhiLPFHalfScaleGlobalBreakthrough",
                "closed": False,
                "proved": False,
                "meaning": "6-wheel and Phi-LPF identities tighten the residual but still need global square-phase positivity or signed dispersion",
                "remaining": "PuncturedWheel6EndpointCapacityInequality OR signed/dispersion input",
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "neither H_P nor the external/internal versions are unconditionally closed",
                "remaining": "row_column_unconditional_closed=false",
            },
        ],
        "external_source_notes": [
            {
                "name": "Runbo Li short intervals",
                "url": "https://arxiv.org/abs/2308.04458",
                "role": "gives x^0.52 intervals for sufficiently large x; after X=P^2 this is P^1.04",
            },
            {
                "name": "Ford-Maynard prime-producing sieve framework",
                "url": "https://arxiv.org/abs/2407.14368",
                "role": "requires Type I/II style object-sensitive input; does not itself supply the prime-square half-window theorem",
            },
            {
                "name": "Runbo Li large-moduli AP",
                "url": "https://arxiv.org/abs/2602.20917",
                "role": "mean-value AP technology; not a pointwise prime-square endpoint theorem",
            },
        ],
        "new_residual_basis": [
            "SquarePhaseSpecialPhaseLongBlockPDECExclusion",
            "TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound",
            "PrimeSquareEndpointNoExceptionalPhaseTheorem",
            "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP",
            "PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC",
            "ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch",
            "NewAutomorphicDispersionProof",
        ],
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
    finite = payload["right_window_target"]["finite_boundary"]
    lines = [
        "# Prime Square Half-Scale Specialization Audit",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 直接回答",
        "",
        "把 `X=P^2` 代入通用短区间定理不会自动把指数从 `0.52` 降到 `1/2`。",
        "`P` 为素数确实给出平方相位刚性，但当前已知外部定理没有把这种刚性转成每个素数平方端点的长度 `P` 素数存在定理。",
        "",
        "## 2. 尺度换算",
        "",
        table(payload["theta_conversion"], ["input", "after_x_equals_p_square", "target_length", "directly_sufficient"]),
        "",
        "## 3. 右侧窗口与左侧窗口",
        "",
        "```text",
        f"right_window_target={payload['right_window_target']['name']}",
        f"right_window_current_corpus_proved={bool_text(payload['right_window_target']['current_corpus_proved'])}",
        f"left_window_target={payload['left_window_target']['name']}",
        f"left_window_current_corpus_proved={bool_text(payload['left_window_target']['current_corpus_proved'])}",
        "```",
        "",
        "既有有限边界：",
        "",
        "```text",
        f"finite_boundary_available={bool_text(finite.get('available'))}",
        f"max_p={finite.get('max_p')}",
        f"prime_count={finite.get('prime_count')}",
        f"failure_count={finite.get('failure_count')}",
        f"max_ratio_record={finite.get('max_ratio_record')}",
        "```",
        "",
        "## 4. 可证明结构收益",
        "",
        table(payload["provable_prime_square_structure"], ["structure", "meaning", "effect"]),
        "",
        "## 5. 判定表",
        "",
        table(payload["decision_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 6. 新剩余基",
        "",
        "```text",
        *payload["new_residual_basis"],
        "```",
        "",
        "## 7. 边界声明",
        "",
        "```text",
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
    print("prime_square_halfscale_auto_drop_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
