#!/usr/bin/env python3
"""审计 Phi-LPF same-row reciprocal graph 到外部 Kloosterman 定理的入口。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_reciprocal_graph_kloosterman_gateway_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-reciprocal-graph-kloosterman-gateway-audit.json

本层接在 Ford--Maynard embedding obligation 后，继续下钻
`FMTypeIISameRowReciprocalGraphBilinearDispersion`。目标是把同一行
reciprocal graph 的 Type-II 义务与 DFI/Bettin--Chandee/Wright 等外部
Kloosterman-fraction 定理逐项匹配，明确哪些条件已匹配，哪些仍缺失。

结论：外部定理是相关技术源，但当前对象还缺一个无损的
reciprocal-graph-to-Kloosterman completion identity；因此不能直接引用外部
Kloosterman 定理闭合 H_P。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-reciprocal-graph-kloosterman-gateway"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

FM_EMBED_JSON = DOCS / "prime-matrix-phi-lpf-ford-maynard-embedding-obligation-audit.json"
LPF_TYPEII_JSON = DOCS / "prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json"
CRT_GATE_JSON = DOCS / "prime-matrix-phi-lpf-crt-signed-residue-projection-gate-audit.json"

DEPENDENCIES = [
    FM_EMBED_JSON,
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
    """读取 JSON；缺失时返回空记录。"""
    if not path.exists():
        return {"available": False}
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["available"] = True
    return payload


def compact_prior_metrics() -> dict[str, Any]:
    """抽取上一层证书的关键读数。"""
    fm = load_json(FM_EMBED_JSON)
    lpf = load_json(LPF_TYPEII_JSON)
    crt = load_json(CRT_GATE_JSON)
    finite = lpf.get("finite_audit", {})
    return {
        "ford_maynard_status": fm.get("status"),
        "selected_non_circular_direction": fm.get("selected_non_circular_direction"),
        "ford_maynard_hypotheses_verified_for_hp": fm.get(
            "ford_maynard_hypotheses_verified_for_hp"
        ),
        "lpf_tail_status": lpf.get("status"),
        "max_prime": finite.get("max_prime"),
        "row_count": finite.get("row_count"),
        "active_residual_row_count": finite.get("active_residual_row_count"),
        "total_R30": finite.get("total_R30"),
        "thin_q_fiber": finite.get("all_q_m_windows_have_at_most_two_points"),
        "thin_reverse_fiber": finite.get("all_m_q_reverse_fibers_have_at_most_two_points"),
        "one_point_qr_fiber": finite.get("all_qr_a_fibers_have_at_most_one_point"),
        "crt_status": crt.get("status"),
        "fixed_crt_classwise_dominance_proved": crt.get(
            "fixed_crt_classwise_dominance_proved"
        ),
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    return {
        "certificate_type": "prime_matrix_phi_lpf_reciprocal_graph_kloosterman_gateway_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "reciprocal_graph_kloosterman_gateway_identified_not_closed",
        "prior_metrics": compact_prior_metrics(),
        "selected_attack_line": "FMTypeIISameRowReciprocalGraphBilinearDispersion",
        "same_row_object": {
            "residual": "R_30(P,k)=# {(q,r,a): P/2<q<P, q prime, m=r*a in I_q(P,k), r=LPF(m)>=7, a r-rough}",
            "graph": "I_q(P,k)=[max(q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))]",
            "fiber_bounds": [
                "#I_q(P,k)<=2",
                "#{q:m in I_q(P,k)}<=2",
                "#{a:kP<q*r*a<(k+1)P}<=1",
            ],
        },
        "frequency_decomposition_gate": [
            {
                "route": "floor_sawtooth_endpoint_route",
                "formal_phase": "psi(kP/u), psi(((k+1)P-1)/u) -> finite sums of e(h*kP/u)",
                "benefit": "keeps exact same-row reciprocal endpoint geometry",
                "defect": "produces reciprocal phases e(A/u), not modular-inverse Kloosterman fractions e(A*bar m/n)",
                "closed": True,
                "proved": True,
                "remaining": "ReciprocalSawtoothTailLogSavingForLPFShellWeights",
            },
            {
                "route": "product_window_fourier_route",
                "formal_phase": "smooth 1_{kP<uv<(k+1)P} -> additive bilinear phases e(t*u*v/Y)",
                "benefit": "keeps bilinear product variable before solving for one-point fibres",
                "defect": "not yet transformed into a DI/DFI/BC inverse-fraction phase without Cauchy/Poisson loss",
                "closed": True,
                "proved": True,
                "remaining": "ProductWindowToInverseKloostermanCompletionIdentity",
            },
            {
                "route": "crt_character_average_route",
                "formal_phase": "sum_a mu_S(a) chi(a) across unit classes",
                "benefit": "compatible with fixed-wheel signed projection",
                "defect": "fixed cellwise dominance is false; character averaging still needs same-row dispersion",
                "closed": True,
                "proved": True,
                "remaining": "CharacterAveragedSameRowCRTDispersionForLPFTail",
            },
        ],
        "external_theorem_match_table": [
            {
                "source": "Duke-Friedlander-Iwaniec 1997",
                "theorem_type": "bilinear forms with Kloosterman fractions e(a*bar m/n)",
                "useful_part": "arbitrary coefficients; balanced dyadic ranges have nontrivial cancellation",
                "matched_to_current_object": False,
                "reason_not_direct": "current graph emits floor/reciprocal or product-window phases before any inverse-modulus completion",
                "remaining": "ProductWindowToInverseKloostermanCompletionIdentity",
                "accepted_as_external_input": False,
            },
            {
                "source": "Bettin-Chandee 2015/2018",
                "theorem_type": "trilinear Kloosterman fractions e(theta*a*bar m/n)",
                "useful_part": "adds an averaged numerator variable and improves DFI-type bounds",
                "matched_to_current_object": False,
                "reason_not_direct": "LPF tail has q prime and one-point m/a fibres, not an existing averaged numerator denominator package",
                "remaining": "LPFShellWeightsToBCKloostermanVariablesWithoutProjectionLoss",
                "accepted_as_external_input": False,
            },
            {
                "source": "Wright 2026 arXiv:2604.25177",
                "theorem_type": "partially fixed moduli and unbalanced convolution AP discrepancy",
                "useful_part": "improves Bettin-Chandee input when the denominator has a fixed factor",
                "matched_to_current_object": False,
                "reason_not_direct": "estimates average AP convolution over q~Q with Siegel-Walfisz beta; H_P is a pointwise product-window row",
                "remaining": "SameRowProductWindowToAPConvolutionAverageTransfer",
                "accepted_as_external_input": False,
            },
            {
                "source": "Dong-Robles-Zeindler 2026 arXiv:2601.00292",
                "theorem_type": "claimed improved bilinear Kloosterman fractions",
                "useful_part": "none for citation discipline",
                "matched_to_current_object": False,
                "reason_not_direct": "paper is withdrawn and cannot be used as an accepted theorem",
                "remaining": "not_an_accepted_source",
                "accepted_as_external_input": False,
            },
        ],
        "new_atomic_gates": [
            {
                "gate": "ReciprocalGraphToKloostermanCompletionIdentity",
                "closed": False,
                "proved": False,
                "meaning": "derive, without losing the pointwise row and LPF-shell weights, a DI/DFI/BC-compatible inverse-fraction bilinear or trilinear form",
                "remaining": "first missing gate before external Kloosterman theorems can be applied",
            },
            {
                "gate": "CompletedKloostermanMeanForPrimeQAndLPFShellWeights",
                "closed": False,
                "proved": False,
                "meaning": "after completion, prove or cite a mean theorem with q prime, r=LPF(m), a r-rough and one-point fibres",
                "remaining": "object-sensitive spectral/dispersion theorem",
            },
            {
                "gate": "SawtoothTailLogSavingForThinReciprocalFibres",
                "closed": False,
                "proved": False,
                "meaning": "control the Fourier truncation/tail from the floor endpoint representation with arbitrary log saving",
                "remaining": "thin reciprocal graph Fourier tail bound",
            },
            {
                "gate": "ExternalKloostermanTheoremsApplyDirectly",
                "closed": False,
                "proved": False,
                "meaning": "DFI/BC/Wright do not directly match the present fixed-row reciprocal graph",
                "remaining": "must first close the completion identity",
            },
        ],
        "latest_narrowest_mouth": [
            "ReciprocalGraphToKloostermanCompletionIdentity",
            "AND CompletedKloostermanMeanForPrimeQAndLPFShellWeights",
            "AND SawtoothTailLogSavingForThinReciprocalFibres",
        ],
        "direct_external_closure_reached": False,
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
    prior = payload["prior_metrics"]
    lines = [
        "# Prime Matrix Phi-LPF reciprocal graph Kloosterman gateway 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 目标",
        "",
        f"本层继续下钻 `{payload['selected_attack_line']}`，目标是判断 DFI、Bettin--Chandee、Wright 等外部 Kloosterman 定理是否能直接接入 Phi-LPF same-row reciprocal graph。",
        "",
        "## 2. 上游读数",
        "",
        "```text",
        f"ford_maynard_status={prior.get('ford_maynard_status')}",
        f"selected_non_circular_direction={prior.get('selected_non_circular_direction')}",
        f"ford_maynard_hypotheses_verified_for_hp={bool_text(prior.get('ford_maynard_hypotheses_verified_for_hp'))}",
        f"lpf_tail_status={prior.get('lpf_tail_status')}",
        f"max_prime={prior.get('max_prime')}",
        f"row_count={prior.get('row_count')}",
        f"active_residual_row_count={prior.get('active_residual_row_count')}",
        f"total_R30={prior.get('total_R30')}",
        f"thin_q_fiber={bool_text(prior.get('thin_q_fiber'))}",
        f"thin_reverse_fiber={bool_text(prior.get('thin_reverse_fiber'))}",
        f"one_point_qr_fiber={bool_text(prior.get('one_point_qr_fiber'))}",
        f"fixed_crt_classwise_dominance_proved={bool_text(prior.get('fixed_crt_classwise_dominance_proved'))}",
        "```",
        "",
        "## 3. 同一行对象",
        "",
        "```text",
        f"residual={payload['same_row_object']['residual']}",
        f"graph={payload['same_row_object']['graph']}",
        *payload["same_row_object"]["fiber_bounds"],
        "```",
        "",
        "## 4. 频率分解入口",
        "",
        table(
            payload["frequency_decomposition_gate"],
            ["route", "closed", "proved", "formal_phase", "defect", "remaining"],
        ),
        "",
        "## 5. 外部定理 theorem-match",
        "",
        table(
            payload["external_theorem_match_table"],
            [
                "source",
                "theorem_type",
                "matched_to_current_object",
                "reason_not_direct",
                "remaining",
                "accepted_as_external_input",
            ],
        ),
        "",
        "## 6. 新原子门",
        "",
        table(payload["new_atomic_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 7. 最新最窄口",
        "",
        "```text",
        *payload["latest_narrowest_mouth"],
        "```",
        "",
        "## 8. 边界声明",
        "",
        "```text",
        f"direct_external_closure_reached={bool_text(payload['direct_external_closure_reached'])}",
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
    print("reciprocal_graph_kloosterman_gateway_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
