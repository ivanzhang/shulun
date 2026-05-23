#!/usr/bin/env python3
"""Short-interval transference parity audit.

用法示例：
  python3 experiments/prime_matrix_short_interval_transference_parity_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-short-interval-transference-parity-audit.json

本证书审计短区间 AP/转移法/BDH 均方输入能否突破 Prime Matrix
Phi-LPF 奇偶障碍。核心检验是：这些定理给的是厚短区间中的素数模式
或平均控制，还是每个素数平方端点 `P^2` 的长度 `P` 单行半窗素数。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-short-interval-transference-parity"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-legendre-frontier-external-audit.json",
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
    """登记本证书依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def p_scale_window(theta: float) -> str:
    """把 X^theta 在 X=P^2 下换成 P 尺度。"""
    exponent = 2.0 * theta
    return f"P^{exponent:.12g}"


def row_thickness(theta: float) -> float:
    """计算相对单行 P 的额外行厚度指数。"""
    return 2.0 * theta - 1.0


def scale_records() -> list[dict[str, Any]]:
    """登记代表性短区间指数的半窗换算。"""
    records: list[dict[str, Any]] = []
    for label, theta in [
        ("target_half_scale", 0.5),
        ("hieu_beyond_17_over_30_plus_0.001", 17 / 30 + 0.001),
        ("guth_maynard_17_over_30", 17 / 30),
        ("legacy_0.52_prime_gap_input", 0.52),
        ("l_function_free_39_over_40", 39 / 40),
    ]:
        records.append(
            {
                "label": label,
                "theta": round(theta, 12),
                "length_after_x_equals_p_square": p_scale_window(theta),
                "row_thickness_exponent": round(row_thickness(theta), 12),
                "single_row_halfscale": theta <= 0.5,
            }
        )
    return records


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    records = scale_records()
    return {
        "certificate_type": "prime_matrix_short_interval_transference_parity_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "transference_and_prime_pattern_inputs_are_not_single_row_phi_lpf_parity_closure",
        "external_sources": [
            {
                "name": "Le Duc Hieu, Arithmetic progressions of primes in short intervals beyond the 17/30 barrier",
                "url": "https://arxiv.org/abs/2509.04883",
                "verified_version": "arXiv:2509.04883v1, 2025",
                "claim_type": "k-term prime APs in intervals [x,x+x^theta] for theta>17/30",
                "acceptance_status": "arxiv_preprint",
                "project_role": "prime-pattern abundance in thick short intervals; not endpoint-localized halfscale",
            },
            {
                "name": "Guth--Maynard, New large value estimates for Dirichlet polynomials",
                "url": "https://annals.math.princeton.edu/2026/203-2/p06",
                "verified_version": "Annals 203(2), 2026",
                "claim_type": "short-interval PNT at length x^(17/30+o(1))",
                "acceptance_status": "published",
                "project_role": "analytic input behind the 17/30 frontier; still gives thick rows at X=P^2",
            },
            {
                "name": "Matomaki--Shao, Vinogradov's theorem with almost equal summands",
                "url": "https://arxiv.org/abs/1405.6592",
                "verified_version": "arXiv:1405.6592",
                "claim_type": "primes in short intervals/arithmetic progressions for most moduli or averaged settings",
                "acceptance_status": "published_related_preprint",
                "project_role": "useful AP distribution technology; not all prime-square endpoints",
            },
            {
                "name": "Matomaki--Merikoski--Teravainen, Primes in arithmetic progressions and short intervals without L-functions",
                "url": "https://arxiv.org/abs/2401.17570",
                "verified_version": "arXiv:2401.17570v1, 2024",
                "claim_type": "L-function-free short-interval/AP technology at much longer scales",
                "acceptance_status": "arxiv_preprint",
                "project_role": "methodological input; scale far above Prime Matrix halfscale",
            },
            {
                "name": "Green--Tao, The primes contain arbitrarily long arithmetic progressions",
                "url": "https://arxiv.org/abs/math/0404188",
                "verified_version": "Annals 167(2), 2008",
                "claim_type": "global transference theorem for prime AP patterns",
                "acceptance_status": "published",
                "project_role": "transference architecture; not local pointwise prime existence",
            },
        ],
        "scale_audit": {
            "input_variable": "X",
            "prime_square_specialization": "X=P^2",
            "target_interval": "(P^2, P^2+P] or [P^2-P, P^2)",
            "target_theta": 0.5,
            "records": records,
            "why_theta_gt_half_does_not_localize": "for theta>1/2 the container (P^2,P^2+P^(2theta)] has an outer tail of length P^(2theta)-P, asymptotically almost the whole container",
        },
        "transference_obstruction": {
            "green_tao_or_w_trick_role": "removes small prime biases and transfers dense-model pattern counts",
            "missing_prime_matrix_property": "anchoring every prime-square endpoint and every Phi-LPF row/column fiber",
            "full_phi_lpf_sieve_needed": "avoid all q<P residue covers, not only W with q up to logarithmic size",
            "parity_breaking": False,
            "closes_single_row_halfscale": False,
        },
        "pattern_count_localization_obstruction": {
            "whole_container_statement": "there are prime APs or many primes in a short interval of length X^theta",
            "required_statement": "there is a prime inside the initial/final length-P subinterval for every prime P",
            "outer_tail_can_absorb_patterns": True,
            "reason": "when theta>1/2, the outer tail length is comparable to the whole thick container, so pattern abundance need not intersect the first row",
            "closes_prime_square_halfscale": False,
        },
        "mean_square_obstruction": {
            "bdh_or_average_role": "controls many moduli/intervals on average",
            "missing_pointwise_gate": "no exceptional prime-square phase for all P and all relevant fibers",
            "known_failure_mode": "a sparse exceptional set can still contain all prime-square rows unless an object-sensitive endpoint theorem is added",
            "closes_row_column_unconditional": False,
        },
        "decision_gates": [
            {
                "gate": "ShortIntervalAPTransferenceImported",
                "closed": True,
                "proved": False,
                "meaning": "registered Hieu/Green--Tao style prime-pattern transference as external input",
                "remaining": "EndpointLocalizationInsidePrimeSquareHalfWindow",
            },
            {
                "gate": "ThetaGreater17Over30AtPrimeSquareScale",
                "closed": False,
                "proved": False,
                "meaning": "theta>17/30 gives P^(2/15+epsilon) row thickening after X=P^2",
                "remaining": "ThetaLeHalfUniformShortIntervalPrimeTheorem",
            },
            {
                "gate": "PrimePatternAbundanceForcesFirstRowPrime",
                "closed": False,
                "proved": False,
                "meaning": "outer tail can absorb the whole-pattern count at theta>1/2",
                "remaining": "APPatternLocalizationInsidePrimeSquareHalfWindow",
            },
            {
                "gate": "WTrickBreaksPhiLPFParity",
                "closed": False,
                "proved": False,
                "meaning": "W-trick handles small logarithmic primes and dense models, not all q<P Phi-LPF covers",
                "remaining": "WTrickToFullPhiLPFObjectSensitiveSieve",
            },
            {
                "gate": "BDHMeanSquareGivesAllRows",
                "closed": False,
                "proved": False,
                "meaning": "mean-square/AP averages do not remove every prime-square endpoint exception",
                "remaining": "BDHNoExceptionalPrimeSquarePhaseTheorem",
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
            "ThetaLeHalfUniformShortIntervalPrimeTheorem",
            "APPatternLocalizationInsidePrimeSquareHalfWindow",
            "BDHNoExceptionalPrimeSquarePhaseTheorem",
            "WTrickToFullPhiLPFObjectSensitiveSieve",
            "MaynardClusterAnchoredAtEveryPrimeSquare",
            "SameObjectSignedDispersionOrAutomorphicEndpointProof",
        ],
        "short_interval_transference_inputs_imported": True,
        "prime_pattern_to_first_row_transfer_closed": False,
        "w_trick_phi_lpf_parity_closed": False,
        "bdh_pointwise_all_rows_closed": False,
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
    trans = payload["transference_obstruction"]
    pattern = payload["pattern_count_localization_obstruction"]
    mean_square = payload["mean_square_obstruction"]
    lines = [
        "# Short-Interval Transference Parity Audit",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 直接回答",
        "",
        "短区间 AP/Green--Tao 转移和 BDH 均方输入是真实有用的外部技术，",
        "但它们给的是厚短区间中的素数模式或平均控制，不给每个 `P^2` 端点的长度 `P` 单行半窗素数。",
        "因此它们不闭合 Phi-LPF 奇偶障碍。",
        "",
        "## 2. 外部源",
        "",
        table(payload["external_sources"], ["name", "verified_version", "acceptance_status", "claim_type", "project_role", "url"]),
        "",
        "## 3. `X=P^2` 尺度换算",
        "",
        "```text",
        f"input_variable={scale['input_variable']}",
        f"prime_square_specialization={scale['prime_square_specialization']}",
        f"target_interval={scale['target_interval']}",
        f"target_theta={scale['target_theta']}",
        "```",
        "",
        table(scale["records"], ["label", "theta", "length_after_x_equals_p_square", "row_thickness_exponent", "single_row_halfscale"]),
        "",
        scale["why_theta_gt_half_does_not_localize"],
        "",
        "## 4. 转移法缺口",
        "",
        "```text",
        f"green_tao_or_w_trick_role={trans['green_tao_or_w_trick_role']}",
        f"missing_prime_matrix_property={trans['missing_prime_matrix_property']}",
        f"full_phi_lpf_sieve_needed={trans['full_phi_lpf_sieve_needed']}",
        f"parity_breaking={bool_text(trans['parity_breaking'])}",
        f"closes_single_row_halfscale={bool_text(trans['closes_single_row_halfscale'])}",
        "```",
        "",
        "## 5. 模式计数定位缺口",
        "",
        "```text",
        f"whole_container_statement={pattern['whole_container_statement']}",
        f"required_statement={pattern['required_statement']}",
        f"outer_tail_can_absorb_patterns={bool_text(pattern['outer_tail_can_absorb_patterns'])}",
        f"closes_prime_square_halfscale={bool_text(pattern['closes_prime_square_halfscale'])}",
        "```",
        "",
        pattern["reason"],
        "",
        "## 6. 均方到点态缺口",
        "",
        "```text",
        f"bdh_or_average_role={mean_square['bdh_or_average_role']}",
        f"missing_pointwise_gate={mean_square['missing_pointwise_gate']}",
        f"known_failure_mode={mean_square['known_failure_mode']}",
        f"closes_row_column_unconditional={bool_text(mean_square['closes_row_column_unconditional'])}",
        "```",
        "",
        "## 7. 判定表",
        "",
        table(payload["decision_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 8. 新剩余基",
        "",
        "```text",
        *payload["new_residual_basis"],
        "```",
        "",
        "## 9. 边界声明",
        "",
        "```text",
        f"short_interval_transference_inputs_imported={bool_text(payload['short_interval_transference_inputs_imported'])}",
        f"prime_pattern_to_first_row_transfer_closed={bool_text(payload['prime_pattern_to_first_row_transfer_closed'])}",
        f"w_trick_phi_lpf_parity_closed={bool_text(payload['w_trick_phi_lpf_parity_closed'])}",
        f"bdh_pointwise_all_rows_closed={bool_text(payload['bdh_pointwise_all_rows_closed'])}",
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
    print("short_interval_transference_inputs_imported=true")
    print("prime_pattern_to_first_row_transfer_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
