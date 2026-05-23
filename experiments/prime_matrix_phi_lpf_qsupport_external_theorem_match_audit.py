#!/usr/bin/env python3
"""审计 q-support reciprocal phase 与最新外部 Kloosterman/Type-II 定理的匹配。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_external_theorem_match_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-external-theorem-match-audit.json

上一层已经证明完整叶子相位塌缩为

  e(-hD/q)=e(h*kP/q),

所以当前对象是 prime-q 支撑集合上的 reciprocal phase：

  sum_{q in S(P,k)} e(h*kP/q).

本层只做 theorem-match，不宣称相位节省。它把 2025--2026 的外部
Kloosterman/Type-II 前沿逐项对照到当前对象，关闭“按名称引用外部定理”
这个伪出口，并把缺口缩小为：必须先构造 q-support 到 completed
bilinear/trilinear convolution 的同对象桥，并验证外部定理要求的
equidistributed/Siegel-Walfisz 因子与 dyadic ranges。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-qsupport-external-theorem-match"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

PHASE_COLLAPSE_JSON = DOCS / "prime-matrix-phi-lpf-complete-leaf-phase-collapse-audit.json"
COMPLETE_TREE_JSON = DOCS / "prime-matrix-phi-lpf-complete-rough-factor-tree-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    PHASE_COLLAPSE_JSON,
    COMPLETE_TREE_JSON,
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


def prime_sieve(n: int) -> list[int]:
    """生成不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def lpf(n: int, primes: list[int]) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return p
    return n


def q_window(P: int, k: int, q: int) -> tuple[int, int]:
    """返回 q 侧 clipped cofactor 窗口。"""
    low = max(q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


def actual_q_support(P: int, k: int, primes: list[int]) -> set[int]:
    """直接扫描 q-window，得到 R30 residual q 支撑。"""
    support: set[int] = set()
    for q in (p for p in primes if P // 2 < p < P):
        low, high = q_window(P, k, q)
        if low > high:
            continue
        for m in range(low, high + 1):
            r = lpf(m, primes)
            if r >= 7 and r != m:
                support.add(q)
    return support


def row_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行 q-support theorem-match 诊断。"""
    q_values = [p for p in primes if P // 2 < p < P]
    support = actual_q_support(P, k, primes)
    q_min = min(support) if support else None
    q_max = max(support) if support else None
    hk_mod_samples: list[str] = []
    for q in sorted(support)[:6]:
        # 中文注释：记录 reciprocal phase 的分母与分子模 q 形态。
        hk_mod_samples.append(f"q={q},kPmodq={(k * P) % q},phase=e(h*kP/q)")
    return {
        "P": P,
        "k": k,
        "prime_q_count": len(q_values),
        "support_q_count": len(support),
        "support_density_numer": len(support),
        "support_density_denom": len(q_values),
        "support_q_min": q_min,
        "support_q_max": q_max,
        "all_support_q_in_prime_dyadic_P_over_2_to_P": all(P // 2 < q < P for q in support),
        "phase_denominator_family": "prime q in (P/2,P)",
        "phase_numerator_family": "h*k*P modulo q",
        "has_completed_mn_congruence_representation": False,
        "has_siegel_walfisz_factor_certificate": False,
        "has_type_ii_dyadic_ranges_certificate": False,
        "hk_mod_samples": "; ".join(hk_mod_samples) if hk_mod_samples else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_prime_q = 0
    total_support_q = 0
    max_support_q_count = 0
    max_prime_q_count = 0
    missing_bridge_totals: Counter[str] = Counter()
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_payload(P, k, primes)
            active_rows += int(row["support_q_count"] > 0)
            total_prime_q += row["prime_q_count"]
            total_support_q += row["support_q_count"]
            max_support_q_count = max(max_support_q_count, row["support_q_count"])
            max_prime_q_count = max(max_prime_q_count, row["prime_q_count"])
            for key in (
                "has_completed_mn_congruence_representation",
                "has_siegel_walfisz_factor_certificate",
                "has_type_ii_dyadic_ranges_certificate",
            ):
                missing_bridge_totals[key] += int(not row[key])
            if (P, k) in interesting:
                samples.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_qsupport_row_count": active_rows,
        "total_prime_q_instances": total_prime_q,
        "total_qsupport_instances": total_support_q,
        "max_prime_q_count": max_prime_q_count,
        "max_support_q_count": max_support_q_count,
        "support_is_prime_denominator_dyadic_family": True,
        "completed_mn_congruence_representation_available": False,
        "siegel_walfisz_factor_certificate_available": False,
        "type_ii_dyadic_ranges_certificate_available": False,
        "missing_completed_mn_congruence_rows": missing_bridge_totals[
            "has_completed_mn_congruence_representation"
        ],
        "missing_siegel_walfisz_factor_rows": missing_bridge_totals[
            "has_siegel_walfisz_factor_certificate"
        ],
        "missing_type_ii_dyadic_range_rows": missing_bridge_totals[
            "has_type_ii_dyadic_ranges_certificate"
        ],
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": samples,
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
            elif isinstance(value, dict):
                value = ", ".join(f"{k}:{value[k]}" for k in sorted(value, key=str))
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


def external_sources() -> list[dict[str, Any]]:
    """列出当前最有用外部源及 theorem-match 结论。"""
    return [
        {
            "source": "Wright 2026 arXiv:2604.25177",
            "source_url": "https://arxiv.org/abs/2604.25177",
            "input_shape": "trilinear Kloosterman fractions / unbalanced convolution, including partially fixed moduli",
            "requires": "completed mn≡a mod q convolution, dyadic M,N,Q ranges, and an equidistributed/Siegel-Walfisz factor",
            "current_object": "prime-q support reciprocal phase sum_{q in S(P,k)} e(h*kP/q)",
            "directly_closes": False,
            "missing_bridge": "QSupportToCompletedTrilinearKloostermanFractionWithSWFactor",
        },
        {
            "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
            "source_url": "https://arxiv.org/abs/2511.07550",
            "input_shape": "general bilinear forms with Kloosterman sums modulo arbitrary q",
            "requires": "bilinear Kloosterman form with admissible coefficient norms",
            "current_object": "0/1 q-support predicate times e(h*kP/q)",
            "directly_closes": False,
            "missing_bridge": "QSupportToBilinearKloostermanFormWithAdmissibleCoefficients",
        },
        {
            "source": "Pascadi 2025 arXiv:2511.08445",
            "source_url": "https://arxiv.org/abs/2511.08445",
            "input_shape": "Type-II Kloosterman sums with composite moduli",
            "requires": "Type-II organisation over composite moduli and non-abelian amplification input",
            "current_object": "prime denominator q with object-specific support predicate",
            "directly_closes": False,
            "missing_bridge": "PrimeQSupportToCompositeModulusTypeIIOrganisation",
        },
        {
            "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
            "source_url": "https://arxiv.org/abs/2411.12113",
            "input_shape": "Kloosterman sums parametrised by square-free and smooth integers",
            "requires": "completed square-free/smooth parameter family",
            "current_object": "floor-defined LPF q-support, not a completed smooth/square-free parameter sum",
            "directly_closes": False,
            "missing_bridge": "QSupportLPFPredicateToCompletedSmoothSquarefreeParameterFamily",
        },
        {
            "source": "Ford--Maynard 2024 arXiv:2407.14368",
            "source_url": "https://arxiv.org/abs/2407.14368",
            "input_shape": "prime-producing sieve framework with Type-I/II hypotheses",
            "requires": "object-specific Type-I and Type-II information before the sieve conclusion",
            "current_object": "q-support phase after parity-class linear sieve reductions",
            "directly_closes": False,
            "missing_bridge": "ObjectSpecificQSupportTypeITypeIIInputLedger",
        },
    ]


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    phase_collapse = load_json(PHASE_COLLAPSE_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_external_theorem_match_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "external_theorem_match_completed_direct_closure_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": phase_collapse.get("latest_narrowest_mouth"),
                "fastest_subgate": "QSupportExternalTheoremMatchAndBridgeObligation",
                "chosen": True,
                "reason": "after leaf phase collapse, the only realistic non-cyclic advance is to theorem-match the q-support phase against current Kloosterman/Type-II inputs",
            },
            {
                "claim": "two-point sieve / prime-pair line",
                "frontier": "BMD=>TLI without hidden denominator/parity gap",
                "chosen": False,
                "reason": "no faster external theorem-match than the current q-support phase interface",
            },
            {
                "claim": "RH contradiction-field line",
                "frontier": "IndependentRefereeAcceptanceOfAllRHControlledExits",
                "chosen": False,
                "reason": "not a Kloosterman/Type-II q-support interface",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "current_object": {
            "phase_sum": "sum_{q in S(P,k)} e(h*kP/q)",
            "denominator": "prime q in (P/2,P)",
            "support": "S(P,k) is the actual Phi-LPF residual q-support after complete leaf phase collapse",
            "not_a_completed_external_form": "No current ledger gives mn≡a mod q bilinear/trilinear convolution with a Siegel-Walfisz factor.",
        },
        "finite_audit": finite_audit,
        "external_theorem_match_table": external_sources(),
        "closed_gates": [
            gate(
                "QSupportExternalFrontierInventoryUpdatedThroughWright2026",
                True,
                True,
                "The current external candidates now include Wright 2026 partially fixed-modulus trilinear Kloosterman fractions.",
                "none",
            ),
            gate(
                "DirectNameCitationToKloostermanTypeIIRejected",
                True,
                True,
                "None of the external names directly estimates the present q-support reciprocal phase.",
                "none",
            ),
            gate(
                "CompletionObligationSharpenedToConvolutionBridge",
                True,
                True,
                "The vague completion gate is refined to a bilinear/trilinear convolution bridge with external hypotheses.",
                "none",
            ),
            gate(
                "QSupportToCompletedBilinearOrTrilinearKloostermanConvolutionWithSWFactor",
                False,
                False,
                "Construct the same-object convolution representation and verify the equidistribution/Siegel-Walfisz factor.",
                "new bridge theorem",
            ),
            gate(
                "PointwisePKUniformTransferFromExternalAverageEstimate",
                False,
                False,
                "Transfer an external averaged Kloosterman/Type-II theorem to every fixed P,k row without zero-exception leakage.",
                "uniform transfer ledger",
            ),
        ],
        "latest_narrowest_mouth": [
            "QSupportToCompletedBilinearOrTrilinearKloostermanConvolutionWithSWFactor",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "external_theorem_match_completed": True,
        "direct_external_closure_available": False,
        "q_support_convolution_bridge_closed": False,
        "pointwise_pk_transfer_closed": False,
        "q_support_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit = payload["finite_audit"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-support external theorem match 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "本轮继续选择行/列 Phi-LPF。叶子相位塌缩后，继续分解 LPF 已无相位收益；最快非循环推进是把当前 q-support phase 与最新外部 Kloosterman/Type-II 定理逐项 theorem-match。",
        "",
        "## 2. 当前对象",
        "",
        "```text",
        f"phase_sum={current['phase_sum']}",
        f"denominator={current['denominator']}",
        f"support={current['support']}",
        f"not_a_completed_external_form={current['not_a_completed_external_form']}",
        "```",
        "",
        "## 3. 有限接口审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_qsupport_row_count={audit['active_qsupport_row_count']}",
        f"total_prime_q_instances={audit['total_prime_q_instances']}",
        f"total_qsupport_instances={audit['total_qsupport_instances']}",
        f"max_prime_q_count={audit['max_prime_q_count']}",
        f"max_support_q_count={audit['max_support_q_count']}",
        f"support_is_prime_denominator_dyadic_family={bool_text(audit['support_is_prime_denominator_dyadic_family'])}",
        f"completed_mn_congruence_representation_available={bool_text(audit['completed_mn_congruence_representation_available'])}",
        f"siegel_walfisz_factor_certificate_available={bool_text(audit['siegel_walfisz_factor_certificate_available'])}",
        f"type_ii_dyadic_ranges_certificate_available={bool_text(audit['type_ii_dyadic_ranges_certificate_available'])}",
        f"missing_completed_mn_congruence_rows={audit['missing_completed_mn_congruence_rows']}",
        f"missing_siegel_walfisz_factor_rows={audit['missing_siegel_walfisz_factor_rows']}",
        f"missing_type_ii_dyadic_range_rows={audit['missing_type_ii_dyadic_range_rows']}",
        "```",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "prime_q_count",
                "support_q_count",
                "support_q_min",
                "support_q_max",
                "phase_denominator_family",
                "hk_mod_samples",
            ],
        ),
        "",
        "## 4. 外部 theorem-match 表",
        "",
        table(
            payload["external_theorem_match_table"],
            ["source", "source_url", "input_shape", "requires", "current_object", "directly_closes", "missing_bridge"],
        ),
        "",
        "结论：这些定理都是有用候选，但没有一个可以按名称直接闭合当前 q-support phase。必须先提交同对象 completion bridge。",
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
        f"external_theorem_match_completed={bool_text(payload['external_theorem_match_completed'])}",
        f"direct_external_closure_available={bool_text(payload['direct_external_closure_available'])}",
        f"q_support_convolution_bridge_closed={bool_text(payload['q_support_convolution_bridge_closed'])}",
        f"pointwise_pk_transfer_closed={bool_text(payload['pointwise_pk_transfer_closed'])}",
        f"q_support_phase_saving_closed={bool_text(payload['q_support_phase_saving_closed'])}",
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
    print("external_theorem_match_completed=true")
    print("q_support_convolution_bridge_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
