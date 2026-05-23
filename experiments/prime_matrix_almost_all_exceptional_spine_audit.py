#!/usr/bin/env python3
"""Almost-all short interval exceptional-spine audit.

用法示例：
  python3 experiments/prime_matrix_almost_all_exceptional_spine_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-almost-all-exceptional-spine-audit.json

本证书审计 almost-all 短区间素数、exceptional interval bounds 与高阶一致性
结果能否突破 Prime Matrix 的 Phi-LPF 奇偶障碍。核心检验是：这些结果虽然
在尺度上远强于 `P^2` 的长度 `P` 半窗，但它们允许稀疏例外；素数平方端点
本身就是密度为零的稀疏脊线，因此必须另证例外集不含这条脊线。
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-almost-all-exceptional-spine"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-short-interval-transference-parity-audit.json",
    DOCS / "prime-matrix-legendre-frontier-external-audit.json",
    DOCS / "prime-matrix-prime-square-halfscale-specialization-audit.json",
    DOCS / "prime-matrix-prime-square-pm1-sandwich-audit.json",
    DOCS / "prime-matrix-external-frontier-theorem-stress-router.json",
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
    """登记依赖哈希，便于审稿时复核证书输入。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def exponent_record(label: str, theta: Fraction, status: str) -> dict[str, Any]:
    """把 X^theta 在 X=P^2 下换成 P 尺度。"""
    p_exp = 2 * theta
    return {
        "label": label,
        "theta_as_fraction": f"{theta.numerator}/{theta.denominator}",
        "theta_decimal": round(float(theta), 12),
        "length_after_x_equals_p_square": f"P^({p_exp.numerator}/{p_exp.denominator})",
        "p_exponent_decimal": round(float(p_exp), 12),
        "shorter_than_halfscale_P": p_exp < 1,
        "status": status,
    }


def build_payload() -> dict[str, Any]:
    """构造 almost-all 例外脊线审计 payload。"""
    scale_records = [
        exponent_record("runbo_li_almost_all_1_over_21_5", Fraction(2, 43), "almost_all"),
        exponent_record("runbo_li_ii_working_paper_1_over_22", Fraction(1, 22), "almost_all_working_paper"),
        exponent_record("gafni_tao_almost_all_2_over_15", Fraction(2, 15), "almost_all_pnt"),
        exponent_record("higher_uniformity_lambda_1_over_3", Fraction(1, 3), "almost_all_uniformity"),
        exponent_record("target_halfscale", Fraction(1, 2), "pointwise_target"),
    ]
    return {
        "certificate_type": "prime_matrix_almost_all_exceptional_spine_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "almost_all_short_interval_inputs_are_scale_strong_but_spine_pointwise_open",
        "external_sources": [
            {
                "name": "Runbo Li, Primes in almost all short intervals",
                "url": "https://arxiv.org/abs/2407.05651",
                "verified_version": "arXiv:2407.05651v6, 2025-09-25",
                "claim_type": "almost all intervals [n,n+n^(1/21.5+epsilon)] contain primes",
                "acceptance_status": "arxiv_preprint",
                "project_role": "scale-overkill if pointwise; still almost-all only",
            },
            {
                "name": "Runbo Li, Primes in almost all short intervals II",
                "url": "https://www.cambridge.org/engage/coe/article-details/68f12b20bc2ac3a0e0635f11",
                "verified_version": "Cambridge Open Engage working paper v1, 2025-10-17",
                "claim_type": "almost all intervals [n-n^(1/22+epsilon),n] contain primes",
                "acceptance_status": "working_paper_not_peer_reviewed_at_posting",
                "project_role": "newest almost-all scale indicator; not a citable unconditional pointwise closure",
            },
            {
                "name": "Gafni--Tao, On the number of exceptional intervals to the PNT in short intervals",
                "url": "https://arxiv.org/abs/2505.24017",
                "verified_version": "arXiv:2505.24017v1, 2025-05-29",
                "claim_type": "exceptional-set bounds; PNT in short intervals all x for theta>17/30 and almost all x for theta>2/15",
                "acceptance_status": "arxiv_preprint",
                "project_role": "best exceptional-set framework; still permits structured sparse spines without extra exclusion",
            },
            {
                "name": "Matomaki--Radziwill--Shao--Tao--Teravainen, Higher uniformity II",
                "url": "https://arxiv.org/abs/2411.05770",
                "verified_version": "arXiv:2411.05770v2, 2026; Invent. Math. 2026",
                "claim_type": "almost all short intervals higher uniformity for Lambda, mu and divisor functions",
                "acceptance_status": "published_inventiones_2026",
                "project_role": "deep almost-all transference/uniformity input; not pointwise on prime-square spine",
            },
        ],
        "scale_audit": {
            "prime_matrix_specialization": "X=P^2",
            "target_halfwindow": "length P = X^(1/2)",
            "records": scale_records,
            "scale_conclusion": "the almost-all inputs are shorter than P after X=P^2; if they were pointwise they would be stronger than needed",
        },
        "prime_square_spine_audit": {
            "dyadic_block": "X <= n <= 2X",
            "prime_square_spine": "{P^2: P prime, sqrt(X) <= P <= sqrt(2X)}",
            "spine_size_asymptotic": "asymp X^(1/2)/log X",
            "spine_density": "asymp 1/(X^(1/2) log X)",
            "why_almost_all_does_not_close": "an o(X) exceptional set, or even a sparse structured exceptional set, may still contain every prime-square endpoint unless a spine-disjointness theorem is proved",
            "required_upgrade": "ExceptionalSetIntersectPrimeSquareSpineIsEmptyEventually",
        },
        "decision_gates": [
            {
                "gate": "AlmostAllPrimeInputImported",
                "closed": True,
                "proved": False,
                "meaning": "registered newest almost-all prime interval scales",
                "remaining": "PrimeSquareSpinePointwiseExclusion",
            },
            {
                "gate": "ScaleWouldBeatHalfWindowIfPointwise",
                "closed": True,
                "proved": True,
                "meaning": "all listed almost-all exponents are below 1/2 in X, hence below P at X=P^2",
                "remaining": "not a pointwise theorem",
            },
            {
                "gate": "ExceptionalSetCannotContainPrimeSquares",
                "closed": False,
                "proved": False,
                "meaning": "almost-all statements do not identify the exceptional set arithmetically",
                "remaining": "ExceptionalPrimeSquareSpineDisjointness",
            },
            {
                "gate": "HigherUniformityImpliesEndpointPrime",
                "closed": False,
                "proved": False,
                "meaning": "almost-all Lambda uniformity gives powerful averages but permits exceptional intervals",
                "remaining": "PointwiseEndpointUniformityAtEveryP2",
            },
            {
                "gate": "PhiLPFParityBrokenByAlmostAll",
                "closed": False,
                "proved": False,
                "meaning": "Phi-LPF needs every row/column fiber, not density-one rows",
                "remaining": "AllRowsNoExceptionOrObjectSensitiveSignedSieve",
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "external lemma and internal self-contained versions remain open",
                "remaining": "row_column_unconditional_closed=false",
            },
        ],
        "new_residual_basis": [
            "ExceptionalPrimeSquareSpineDisjointness",
            "PointwiseEndpointUniformityAtEveryPrimeSquare",
            "AlmostAllToAllRowsUpgradeWithArithmeticSpineRepulsion",
            "NoPrimeSquareExceptionalPhaseForGafniTaoBounds",
            "PhiLPFObjectSensitiveSignedSieveOnSparseSpine",
            "ThetaLeHalfPointwiseShortIntervalPrimeTheorem",
        ],
        "almost_all_short_interval_inputs_imported": True,
        "scale_stronger_than_halfwindow_if_pointwise": True,
        "exceptional_prime_square_spine_excluded": False,
        "pointwise_every_prime_square_endpoint_closed": False,
        "phi_lpf_parity_closed": False,
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
    """生成 Markdown 审计文档。"""
    scale = payload["scale_audit"]
    spine = payload["prime_square_spine_audit"]
    lines = [
        "# Almost-All Short Interval Exceptional-Spine Audit",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 直接回答",
        "",
        "almost-all 短区间素数和高阶一致性结果在尺度上非常强；代入 `X=P^2` 后，",
        "它们的窗口长度都短于目标半窗 `P`。但这些结果允许例外集，而素数平方端点",
        "`{P^2}` 本身就是密度为零的稀疏脊线。因此它们不能自动闭合每个 `P^2` 半窗。",
        "",
        "## 2. 外部源",
        "",
        table(payload["external_sources"], ["name", "verified_version", "acceptance_status", "claim_type", "project_role", "url"]),
        "",
        "## 3. `X=P^2` 尺度换算",
        "",
        "```text",
        f"prime_matrix_specialization={scale['prime_matrix_specialization']}",
        f"target_halfwindow={scale['target_halfwindow']}",
        "```",
        "",
        table(scale["records"], ["label", "theta_as_fraction", "theta_decimal", "length_after_x_equals_p_square", "p_exponent_decimal", "shorter_than_halfscale_P", "status"]),
        "",
        scale["scale_conclusion"],
        "",
        "## 4. 例外脊线缺口",
        "",
        "```text",
        f"dyadic_block={spine['dyadic_block']}",
        f"prime_square_spine={spine['prime_square_spine']}",
        f"spine_size_asymptotic={spine['spine_size_asymptotic']}",
        f"spine_density={spine['spine_density']}",
        f"required_upgrade={spine['required_upgrade']}",
        "```",
        "",
        spine["why_almost_all_does_not_close"],
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
        f"almost_all_short_interval_inputs_imported={bool_text(payload['almost_all_short_interval_inputs_imported'])}",
        f"scale_stronger_than_halfwindow_if_pointwise={bool_text(payload['scale_stronger_than_halfwindow_if_pointwise'])}",
        f"exceptional_prime_square_spine_excluded={bool_text(payload['exceptional_prime_square_spine_excluded'])}",
        f"pointwise_every_prime_square_endpoint_closed={bool_text(payload['pointwise_every_prime_square_endpoint_closed'])}",
        f"phi_lpf_parity_closed={bool_text(payload['phi_lpf_parity_closed'])}",
        f"prime_square_halfscale_closed={bool_text(payload['prime_square_halfscale_closed'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    """写出证书、账本和 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("almost_all_short_interval_inputs_imported=true")
    print("exceptional_prime_square_spine_excluded=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
