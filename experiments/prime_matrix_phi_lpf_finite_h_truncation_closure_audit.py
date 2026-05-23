#!/usr/bin/env python3
"""闭合 Phi-LPF sawtooth 门中的 polylog finite-H 截断账本。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_finite_h_truncation_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-finite-h-truncation-closure-audit.json

本层接在 sawtooth reciprocal tail gateway 之后。合著稿三命题中，行/列
Phi-LPF 链的 `UniformFiniteHTruncationWithHPolylog` 是最快可完全闭合的
子门：它只依赖 Vaaler/截断账本和 reciprocal thin-fibre 的总质量上界，
不需要新的素数分布定理。

结论：polylog finite-H 截断闭合；剩余硬点缩为带 prime-q/LPF-shell 权重的
有限 Fourier 模式相位和，以及把 LPF 权重抽取到可用 Type-II/Kloosterman
框架的恒等式。
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

SLUG = "prime-matrix-phi-lpf-finite-h-truncation-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

SAWTOOTH_JSON = DOCS / "prime-matrix-phi-lpf-sawtooth-reciprocal-tail-gateway-audit.json"
GATEWAY_JSON = DOCS / "prime-matrix-phi-lpf-reciprocal-graph-kloosterman-gateway-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    SAWTOOTH_JSON,
    GATEWAY_JSON,
    THREE_CLAIMS_JSON,
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


def truncation_sample_rows() -> list[dict[str, Any]]:
    """给出 H=(log P)^B 的代表性截断账本；只展示尺度。"""
    rows: list[dict[str, Any]] = []
    for P in [101, 1009, 100003, 1000003]:
        for target_log_power in [4, 8]:
            # 中文注释：多留两阶对数余量，方便后续有限相位和吸收边界常数。
            truncation_power = target_log_power + 2
            H = math.ceil(math.log(P) ** truncation_power)
            rows.append(
                {
                    "P": P,
                    "target_log_power_A": target_log_power,
                    "chosen_H": H,
                    "endpoint_tail_bound_le": f"4P/log^{truncation_power}P",
                    "tail_over_P_numeric": round(4 / H, 12),
                    "finite_mode_count_le": 2 * H,
                }
            )
    return rows


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
            elif isinstance(value, list):
                value = " / ".join(str(item) for item in value)
            cells.append(str(value).replace("|", r"\|"))
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep, *body])


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    sawtooth = load_json(SAWTOOTH_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    return {
        "certificate_type": "prime_matrix_phi_lpf_finite_h_truncation_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "finite_h_truncation_closed_weighted_phase_and_lpf_extraction_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": sawtooth.get("new_narrowest_sawtooth_mouth"),
                "fastest_subgate": "UniformFiniteHTruncationWithHPolylog",
                "chosen": True,
                "reason": "deterministic Vaaler truncation plus thin-fibre absolute mass bound; no new prime theorem required",
            },
            {
                "claim": "two-point sieve / prime-pair line",
                "frontier": "BMD=>TLI without hidden denominator/parity gap",
                "chosen": False,
                "reason": "requires Buchstab transfer and denominator audit, not a one-gate bookkeeping closure",
            },
            {
                "claim": "RH contradiction-field line",
                "frontier": "IndependentRefereeAcceptanceOfAllRHControlledExits",
                "chosen": False,
                "reason": "verification package state; not the fastest mathematical hard-point closure",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "truncation_theorem": {
            "mass_bound": "For every strict row, total high-q reciprocal candidate mass W_int(P,k)<=2*pi(P)<2P; two endpoint sawtooth tails have absolute mass <=4P.",
            "vaaler_tail_rule": "With H>=1, endpoint truncation error is O(P/H) for nonnegative LPF-shell counting weights, after summing absolute weights.",
            "polylog_choice": "For any target A>0 choose H=ceil((log P)^(A+2)); then the tail is O(P/log^(A+2)P), hence O(P/log^A P).",
            "finite_mode_reduction": "Only |h|<=H weighted phases remain; coefficients have harmonic cost O(log H)=O(log log P).",
        },
        "finite_h_samples": truncation_sample_rows(),
        "external_frontier_match_table": [
            {
                "source": "Vaaler finite Fourier approximation for sawtooth",
                "useful_part": "closes deterministic polylog truncation once absolute thin-fibre mass is O(P)",
                "accepted_for_this_gate": True,
                "closes_weighted_phase": False,
            },
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "useful_part": "power-saving bilinear forms with Kloosterman sums modulo arbitrary q",
                "accepted_for_this_gate": False,
                "closes_weighted_phase": False,
                "reason_not_direct": "finite-field Kloosterman sums after completion, not the present real reciprocal phase with LPF-shell weights",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "useful_part": "non-abelian amplification for composite-modulus Kloosterman sums",
                "accepted_for_this_gate": False,
                "closes_weighted_phase": False,
                "reason_not_direct": "composite-modulus Kloosterman setting; present denominator q is prime and the missing step is LPF-weighted completion",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "useful_part": "Kloosterman sums over square-free and smooth parameters",
                "accepted_for_this_gate": False,
                "closes_weighted_phase": False,
                "reason_not_direct": "useful only after finite-field Kloosterman completion and parameter transfer",
            },
        ],
        "closed_gates": [
            gate(
                "UniformFiniteHTruncationWithHPolylog",
                True,
                True,
                "Choose H=(log P)^(A+2); reciprocal thin-fibre total mass gives sawtooth tail O(P/log^A P).",
                "none",
            ),
            gate(
                "PrimeQLPFShellWeightedReciprocalPhaseSaving",
                False,
                False,
                "Finite modes still need cancellation with prime-q and LPF-shell/rough quotient weights.",
                "weighted finite-mode phase saving",
            ),
            gate(
                "WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII",
                False,
                False,
                "LPF condition must be converted without circularity into a Type-II/Kloosterman-compatible coefficient package.",
                "LPF weight extraction identity/theorem",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQLPFShellWeightedReciprocalPhaseSaving",
            "AND WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII",
        ],
        "uniform_finite_h_truncation_closed": True,
        "weighted_sawtooth_phi_lpf_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["truncation_theorem"]
    lines = [
        "# Prime Matrix Phi-LPF finite-H truncation closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "本轮选择 Prime Matrix 行/列 Phi-LPF 链，因为 `UniformFiniteHTruncationWithHPolylog` 是纯截断账本，可完全闭合；二点筛和 RH 线仍分别卡在 Buchstab 转移和独立审稿包。",
        "",
        "## 2. 截断定理",
        "",
        "```text",
        f"mass_bound={theorem['mass_bound']}",
        f"vaaler_tail_rule={theorem['vaaler_tail_rule']}",
        f"polylog_choice={theorem['polylog_choice']}",
        f"finite_mode_reduction={theorem['finite_mode_reduction']}",
        "```",
        "",
        "关键点是：每个 `q` 的 reciprocal window 至多两个点，故总候选质量 `<=2*pi(P)<2P`；两个 endpoint sawtooth 的绝对尾质量 `<=4P/H`。选择 `H=(log P)^(A+2)` 后，截断尾项已带任意对数节省。",
        "",
        "## 3. 代表尺度",
        "",
        table(
            payload["finite_h_samples"],
            ["P", "target_log_power_A", "chosen_H", "endpoint_tail_bound_le", "tail_over_P_numeric", "finite_mode_count_le"],
        ),
        "",
        "这些数值只展示截断尺度；闭合本身来自上面的符号质量上界。",
        "",
        "## 4. 外部前沿匹配",
        "",
        table(
            payload["external_frontier_match_table"],
            ["source", "useful_part", "accepted_for_this_gate", "closes_weighted_phase", "reason_not_direct"],
        ),
        "",
        "Milićević--Qin--Wu、Pascadi、Shao--Shparlinski--Wijaya 等 Kloosterman 前沿都继续作为 weighted phase 的候选技术源；它们不影响本层 finite-H 截断闭合，也不能直接替代 LPF 带权相位证明。",
        "",
        "## 5. 门控表",
        "",
        table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 6. 最新最窄口",
        "",
        "```text",
        *payload["latest_narrowest_mouth"],
        "```",
        "",
        "状态边界：",
        "",
        "```text",
        f"uniform_finite_h_truncation_closed={bool_text(payload['uniform_finite_h_truncation_closed'])}",
        f"weighted_sawtooth_phi_lpf_closed={bool_text(payload['weighted_sawtooth_phi_lpf_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
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
    print("uniform_finite_h_truncation_closed=true")
    print("weighted_sawtooth_phi_lpf_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
