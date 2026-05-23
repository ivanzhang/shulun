#!/usr/bin/env python3
"""审计 H_P/Phi-LPF tail 到 Ford--Maynard prime-producing sieve 的嵌入义务。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_ford_maynard_embedding_obligation_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-ford-maynard-embedding-obligation-audit.json

本证书选择三条非循环路线中最可操作的一条：
`SameRowReciprocalWindowTypeIIDispersionForLPFTail`。它精读
Ford--Maynard arXiv:2407.14368 的 Type I/Type II 框架，并把 H_P 行窗口
嵌入该框架，逐项登记哪些只是形式匹配，哪些仍是未证明的同对象估计。

结论刻意保持严格：本层不声称 H_P、外部引理版或内部自足版已经无条件闭合。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-ford-maynard-embedding-obligation"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

LPF_TYPEII_JSON = DOCS / "prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json"
CRT_GATE_JSON = DOCS / "prime-matrix-phi-lpf-crt-signed-residue-projection-gate-audit.json"

DEPENDENCIES = [
    LPF_TYPEII_JSON,
    CRT_GATE_JSON,
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


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空记录，避免证书生成中断。"""
    if not path.exists():
        return {"available": False}
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["available"] = True
    return payload


def lpf_metrics(payload: dict[str, Any]) -> dict[str, Any]:
    """抽取 LPF-tail Type-II 证书的关键读数。"""
    finite = payload.get("finite_audit", {})
    large = payload.get("large_sample_audit", {})
    return {
        "available": payload.get("available", False),
        "status": payload.get("status"),
        "max_prime": finite.get("max_prime"),
        "row_count": finite.get("row_count"),
        "active_residual_row_count": finite.get("active_residual_row_count"),
        "total_R30": finite.get("total_R30"),
        "total_direct_prime_count": finite.get("total_direct_prime_count"),
        "total_prime_count_minus_R30": finite.get("total_prime_count_minus_R30"),
        "thin_q_fiber": finite.get("all_q_m_windows_have_at_most_two_points"),
        "thin_reverse_fiber": finite.get("all_m_q_reverse_fibers_have_at_most_two_points"),
        "one_point_qr_fiber": finite.get("all_qr_a_fibers_have_at_most_one_point"),
        "sparsest_finite_graph": finite.get("sparsest_reciprocal_graph_row"),
        "large_sample_sparsest_graph": large.get("sparsest_reciprocal_graph_row"),
    }


def crt_metrics(payload: dict[str, Any]) -> dict[str, Any]:
    """抽取 CRT signed projection gate 的关键读数。"""
    finite = payload.get("finite_audit", {})
    layers = finite.get("layers", {})
    negative_rows: dict[str, Any] = {}
    for name, layer in layers.items():
        negative_rows[name] = {
            "modulus": layer.get("modulus"),
            "stable_rows_with_negative_unit_cell_surplus": layer.get(
                "stable_rows_with_negative_unit_cell_surplus"
            ),
            "stable_negative_unit_cell_count": layer.get("stable_negative_unit_cell_count"),
            "fixed_crt_classwise_dominance_holds_on_stable_rows": layer.get(
                "fixed_crt_classwise_dominance_holds_on_stable_rows"
            ),
        }
    return {
        "available": payload.get("available", False),
        "status": payload.get("status"),
        "negative_rows_by_layer": negative_rows,
        "fixed_crt_classwise_dominance_proved": payload.get(
            "fixed_crt_classwise_dominance_proved"
        ),
        "character_averaged_dispersion_required": payload.get(
            "character_averaged_dispersion_required"
        ),
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    lpf = lpf_metrics(load_json(LPF_TYPEII_JSON))
    crt = crt_metrics(load_json(CRT_GATE_JSON))
    return {
        "certificate_type": "prime_matrix_phi_lpf_ford_maynard_embedding_obligation_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "hp_embedded_in_ford_maynard_typeii_framework_but_hypotheses_open",
        "selected_non_circular_direction": "SameRowReciprocalWindowTypeIIDispersionForLPFTail",
        "why_selected": [
            "directly attacks the LPF-tail parity obstruction rather than a renamed equivalent form",
            "matches the balanced q*m scale x^(1/2) in the strict top band x≈P^2",
            "Ford--Maynard supplies an explicit theorem-match checklist for Type I/II inputs",
        ],
        "ford_maynard_source": {
            "paper": "Kevin Ford and James Maynard, On the theory of prime-producing sieves",
            "arxiv": "2407.14368v1",
            "date": "2024-07-19",
            "close_read_items": [
                "Type I estimate (I) for w_n=a_n-b_n in divisor-sliced intervals",
                "Type II estimate (II) for arbitrary divisor-bounded bilinear coefficients",
                "constants C^-(gamma,theta,nu), C^+(gamma,theta,nu)",
                "Theorem 2.1: a positive amount of Type II information is necessary",
                "Theorem 2.2: asymptotic region characterized by A1/A2",
                "Theorem 2.4/2.5: the gamma=1/2 boundary is delicate and needs extra boundedness",
            ],
        },
        "hp_embedding": {
            "x_scale": "x≈P^2 in the top strict band k≈P",
            "row_window": "I_{P,k}=(kP,(k+1)P), length H=P=x^(1/2)",
            "normalized_sequence_candidate": "a_{P,k}(n)=(x/H) 1_{kP<n<(k+1)P} times optional wheel/unit filters",
            "comparison_sequence_candidate": "b_{P,k}(n)=smooth local-density model with same row mass and wheel density",
            "prime_sum_target": "sum_p a_{P,k}(p)>0 is equivalent, after normalization, to pi((k+1)P-1)-pi(kP)>0",
            "lpf_tail_typeii_scale": "q,m≈P≈x^(1/2), with q in (P/2,P) and m in I_q(P,k)",
            "reciprocal_graph": "I_q(P,k)=[max(q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))]",
        },
        "prior_certificate_metrics": {
            "lpf_tail_typeii": lpf,
            "crt_signed_projection_gate": crt,
        },
        "theorem_match_table": [
            {
                "field": "Nonnegative target sequence",
                "ford_maynard_requirement": "a_n,b_n nonnegative on x/2<n<=x, average size about 1",
                "hp_embedding_status": "formal after row normalization by x/H≈P",
                "closed": True,
                "proved": True,
                "remaining": "normalization itself gives no prime lower bound",
            },
            {
                "field": "Prime sum target",
                "ford_maynard_requirement": "lower-bound sum_p a_p by C^- sum_p b_p",
                "hp_embedding_status": "sum_p a_{P,k}(p)>0 exactly matches one row of H_P",
                "closed": True,
                "proved": True,
                "remaining": "requires C^->0 and verified hypotheses for every row",
            },
            {
                "field": "Type-I short-row divisor estimate",
                "ford_maynard_requirement": "uniform control of sum w_{mn} for m<=x^gamma and all n-intervals",
                "hp_embedding_status": "not proved for the length sqrt(x) moving row sequence",
                "closed": False,
                "proved": False,
                "remaining": "FMTypeIShortRowDivisorSwitchEstimate",
            },
            {
                "field": "Type-II bilinear estimate",
                "ford_maynard_requirement": "arbitrary divisor-bounded coefficients over x^theta<m<=x^(theta+nu)",
                "hp_embedding_status": "scale matches q,m≈x^(1/2), but support is a thin reciprocal graph, not a rectangular box",
                "closed": False,
                "proved": False,
                "remaining": "FMTypeIISameRowReciprocalGraphBilinearDispersion",
            },
            {
                "field": "Local density model",
                "ford_maynard_requirement": "b_n has a prime-number-theorem-type comparison prime mass",
                "hp_embedding_status": "wheel/local density can be written formally, but row-specific comparison error is unproved",
                "closed": False,
                "proved": False,
                "remaining": "FMLocalDensityForWheelRowComparisonSequence",
            },
            {
                "field": "Pointwise all-row upgrade",
                "ford_maynard_requirement": "framework is dyadic/asymptotic in x for sequences satisfying estimates",
                "hp_embedding_status": "H_P needs every prime P and every strict row k, not an averaged exceptional-set statement",
                "closed": False,
                "proved": False,
                "remaining": "FMPointwiseUniformAllRowsUpgrade",
            },
            {
                "field": "Fixed CRT unit-cell route",
                "ford_maynard_requirement": "signed cancellation may be averaged, not cellwise nonnegative",
                "hp_embedding_status": "existing CRT audit rejects cellwise dominance; character-averaged dispersion remains possible",
                "closed": True,
                "proved": True,
                "remaining": "CharacterAveragedSameRowCRTDispersionForLPFTail",
            },
            {
                "field": "Unconditional H_P closure",
                "ford_maynard_requirement": "all above hypotheses plus positive lower-bound region",
                "hp_embedding_status": "not reached",
                "closed": False,
                "proved": False,
                "remaining": "row_column_unconditional_closed=false",
            },
        ],
        "conditional_external_lemma_schema": {
            "closed_as_schema": True,
            "proved_unconditionally": False,
            "statement": (
                "If for every sufficiently large prime P and every strict row k the normalized "
                "row sequence satisfies Ford--Maynard Type I, Type II, local-density, and "
                "positive-C^- hypotheses uniformly, then H_P follows for those rows."
            ),
            "unproved_inputs": [
                "FMTypeIShortRowDivisorSwitchEstimate",
                "FMTypeIISameRowReciprocalGraphBilinearDispersion",
                "FMLocalDensityForWheelRowComparisonSequence",
                "FMPointwiseUniformAllRowsUpgrade",
            ],
        },
        "new_residual_basis": [
            "FMTypeIShortRowDivisorSwitchEstimate",
            "FMTypeIISameRowReciprocalGraphBilinearDispersion",
            "FMLocalDensityForWheelRowComparisonSequence",
            "FMPointwiseUniformAllRowsUpgrade",
            "CharacterAveragedSameRowCRTDispersionForLPFTail",
            "SquarePhaseEndpointLowerBound",
        ],
        "ford_maynard_embedding_complete": True,
        "ford_maynard_hypotheses_verified_for_hp": False,
        "same_row_reciprocal_typeii_still_main_attack": True,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def table(rows: list[dict[str, Any]], fields: list[str]) -> str:
    """生成 Markdown 表格。"""
    header = "| " + " | ".join(fields) + " |"
    sep = "| " + " | ".join("---" for _ in fields) + " |"
    body = []
    for row in rows:
        cells = []
        for field in fields:
            value = row.get(field, "")
            if isinstance(value, bool):
                value = bool_text(value)
            cells.append(str(value))
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep, *body])


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    lpf = payload["prior_certificate_metrics"]["lpf_tail_typeii"]
    crt = payload["prior_certificate_metrics"]["crt_signed_projection_gate"]
    conditional = payload["conditional_external_lemma_schema"]
    lines = [
        "# Prime Matrix Phi-LPF Ford--Maynard embedding obligation 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 选择方向",
        "",
        f"本轮选择 `{payload['selected_non_circular_direction']}` 作为三条非循环路线中最可操作的主线。",
        "",
        "理由：",
        "",
        *[f"- {item}" for item in payload["why_selected"]],
        "",
        "## 2. Ford--Maynard 精读摘要",
        "",
        f"论文：{payload['ford_maynard_source']['paper']}，arXiv `{payload['ford_maynard_source']['arxiv']}`。",
        "",
        "核心框架不是直接给 H_P 的黑箱定理，而是：对任意非负序列 `a_n`，若",
        "`w_n=a_n-b_n` 满足 Type I 与 Type II 估计，则可用常数",
        "`C^-(gamma,theta,nu)` 给出 prime-producing lower bound。",
        "",
        "精读项：",
        "",
        *[f"- {item}" for item in payload["ford_maynard_source"]["close_read_items"]],
        "",
        "## 3. H_P 嵌入",
        "",
        "```text",
        f"x_scale={payload['hp_embedding']['x_scale']}",
        f"row_window={payload['hp_embedding']['row_window']}",
        f"normalized_sequence_candidate={payload['hp_embedding']['normalized_sequence_candidate']}",
        f"comparison_sequence_candidate={payload['hp_embedding']['comparison_sequence_candidate']}",
        f"prime_sum_target={payload['hp_embedding']['prime_sum_target']}",
        f"lpf_tail_typeii_scale={payload['hp_embedding']['lpf_tail_typeii_scale']}",
        f"reciprocal_graph={payload['hp_embedding']['reciprocal_graph']}",
        "```",
        "",
        "## 4. 既有证书读数",
        "",
        "LPF-tail Type-II：",
        "",
        "```text",
        f"status={lpf.get('status')}",
        f"max_prime={lpf.get('max_prime')}",
        f"row_count={lpf.get('row_count')}",
        f"active_residual_row_count={lpf.get('active_residual_row_count')}",
        f"total_R30={lpf.get('total_R30')}",
        f"total_direct_prime_count={lpf.get('total_direct_prime_count')}",
        f"total_prime_count_minus_R30={lpf.get('total_prime_count_minus_R30')}",
        f"thin_q_fiber={bool_text(lpf.get('thin_q_fiber'))}",
        f"thin_reverse_fiber={bool_text(lpf.get('thin_reverse_fiber'))}",
        f"one_point_qr_fiber={bool_text(lpf.get('one_point_qr_fiber'))}",
        f"sparsest_finite_graph={lpf.get('sparsest_finite_graph')}",
        "```",
        "",
        "CRT signed projection gate：",
        "",
        "```text",
        f"status={crt.get('status')}",
        f"fixed_crt_classwise_dominance_proved={bool_text(crt.get('fixed_crt_classwise_dominance_proved'))}",
        f"character_averaged_dispersion_required={bool_text(crt.get('character_averaged_dispersion_required'))}",
        f"negative_rows_by_layer={crt.get('negative_rows_by_layer')}",
        "```",
        "",
        "## 5. Theorem-match 判定表",
        "",
        table(
            payload["theorem_match_table"],
            ["field", "closed", "proved", "hp_embedding_status", "remaining"],
        ),
        "",
        "## 6. 条件外部引理版",
        "",
        "```text",
        f"closed_as_schema={bool_text(conditional['closed_as_schema'])}",
        f"proved_unconditionally={bool_text(conditional['proved_unconditionally'])}",
        f"statement={conditional['statement']}",
        "```",
        "",
        "未证明输入：",
        "",
        "```text",
        *conditional["unproved_inputs"],
        "```",
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
        f"ford_maynard_embedding_complete={bool_text(payload['ford_maynard_embedding_complete'])}",
        f"ford_maynard_hypotheses_verified_for_hp={bool_text(payload['ford_maynard_hypotheses_verified_for_hp'])}",
        f"same_row_reciprocal_typeii_still_main_attack={bool_text(payload['same_row_reciprocal_typeii_still_main_attack'])}",
        f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
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
    print("ford_maynard_embedding_complete=true")
    print("ford_maynard_hypotheses_verified_for_hp=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
