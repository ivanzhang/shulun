#!/usr/bin/env python3
"""归档 product-window additive saving 的适用性防火墙。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_additive_saving_firewall_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-additive-saving-firewall-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-additive-saving-firewall-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-additive-saving-firewall-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-additive-saving-firewall-router.md

本证书承接 target-affine source-keyed product phase。核心目的：
普通非零频率上界节省不能排除 full-cover，因为 full-cover 的完整非零
剩余类 Fourier 和本来就是 -1。要继续非循环推进，必须要求精确系数
分离、subunit Fourier contradiction、带符号缺陷传输，或回到点态素数输入。
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

SLUG = "prime-matrix-phi-lpf-product-window-additive-saving-firewall"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PRODUCT_PHASE_JSON = DOCS / "prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.json"
SIGNED_PHASE_JSON = DOCS / "prime-matrix-phi-lpf-target-affine-signed-phase-contract-router.json"
GAP_EQUIV_JSON = DOCS / "prime-matrix-phi-lpf-target-affine-gap-equivalence-router.json"
EXTERNAL_STRESS_JSON = DOCS / "prime-matrix-external-frontier-theorem-stress-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    PRODUCT_PHASE_JSON,
    SIGNED_PHASE_JSON,
    GAP_EQUIV_JSON,
    EXTERNAL_STRESS_JSON,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]

OLD_SAVING_GATE = "ProductWindowBilinearAdditivePhaseSavingOrPDEC"
NEW_PRIMARY_GATE = "ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC"
TRACE_GATE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefect"
SQRT_GATE = "PointwiseSqrtPrimeInputCOne"
NUMERIC_TOLERANCE = 1e-8


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def primes_up_to(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = [False] * (((n - start) // p) + 1)
    return [value for value, flag in enumerate(sieve) if flag]


def least_prime_factor(value: int, primes: list[int]) -> int | None:
    """合数返回最小素因子，素数返回 None。"""
    limit = math.isqrt(value)
    for p in primes:
        if p > limit:
            return None
        if value % p == 0:
            return p
    return None


def selected_frequencies(P: int) -> list[int]:
    """选取代表性非零频率。"""
    raw = [1, 2, 3, (P - 1) // 2, P - 1]
    return sorted({h for h in raw if 1 <= h <= P - 1})


def cis(P: int, h: int, r: int) -> complex:
    """返回 e_P(hr)。"""
    angle = 2.0 * math.pi * h * (r % P) / P
    return complex(math.cos(angle), math.sin(angle))


def row_firewall_audit(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """核验 owner、survivor、完整非零剩余类的 Fourier 关系。"""
    owner_residues: list[int] = []
    survivor_residues: list[int] = []
    for r in range(1, P):
        n = k * P + r
        if least_prime_factor(n, primes) is None:
            survivor_residues.append(r)
        else:
            owner_residues.append(r)

    freq_rows: list[dict[str, Any]] = []
    for h in selected_frequencies(P):
        complete_sum = sum(cis(P, h, r) for r in range(1, P))
        owner_sum = sum(cis(P, h, r) for r in owner_residues)
        survivor_sum = sum(cis(P, h, r) for r in survivor_residues)
        partition_error = abs((owner_sum + survivor_sum) - complete_sum)
        complete_minus_minus_one_error = abs(complete_sum + 1.0)
        defect_error = abs((owner_sum + 1.0) + survivor_sum)
        full_cover_abs = abs(complete_sum)
        ordinary_bounds = {
            "sqrt_P": math.sqrt(P),
            "P_to_3_over_4": P ** 0.75,
            "P_over_logP_squared": P / (math.log(P) ** 2),
        }
        freq_rows.append(
            {
                "h": h,
                "complete_sum_real": round(complete_sum.real, 12),
                "complete_sum_imag": round(complete_sum.imag, 12),
                "full_cover_abs": round(full_cover_abs, 12),
                "owner_plus_survivor_partition_error": round(partition_error, 12),
                "complete_equals_minus_one_error": round(complete_minus_minus_one_error, 12),
                "owner_defect_equals_negative_survivor_error": round(defect_error, 12),
                "ordinary_upper_bounds_all_allow_full_cover": all(
                    full_cover_abs <= bound for bound in ordinary_bounds.values()
                ),
                "ordinary_upper_bounds": {key: round(value, 9) for key, value in ordinary_bounds.items()},
                "subunit_bound_needed_to_exclude_full_cover": True,
            }
        )

    return {
        "P": P,
        "k": k,
        "row_length": P - 1,
        "owner_count": len(owner_residues),
        "survivor_count": len(survivor_residues),
        "partition_count_ok": len(owner_residues) + len(survivor_residues) == P - 1,
        "full_cover_fourier_profile_if_survivor_count_zero": "S_h=-1 for every h=1,...,P-1",
        "sampled_frequency_rows": freq_rows,
        "ordinary_additive_saving_excludes_full_cover": False,
    }


def finite_firewall_rows(product_cert: dict[str, Any]) -> list[dict[str, Any]]:
    """从上一层抽样行生成 Fourier 防火墙审计。"""
    rows = product_cert.get("finite_product_phase_audit", [])
    normalized = [{"P": int(row["P"]), "k": int(row["k"])} for row in rows]
    max_value = max((row["k"] + 1) * row["P"] for row in normalized)
    primes = primes_up_to(math.isqrt(max_value) + 2)
    return [row_firewall_audit(row["P"], row["k"], primes) for row in normalized]


def external_applicability_rows() -> list[dict[str, Any]]:
    """登记本层用到的外部前沿压力测试。"""
    return [
        {
            "source": "Guth--Maynard, arXiv:2405.20552v2, New large value estimates for Dirichlet polynomials",
            "date_checked": "2026-05-26",
            "reported_strength": "zero-density estimate implying primes in intervals of length x^(17/30+o(1))",
            "applicability_to_target_row": "not enough for a pointwise row of length P at x≈P^2, since x^(17/30)=P^(17/15)>P",
            "usable_as_closure": False,
            "url": "https://arxiv.org/abs/2405.20552",
        },
        {
            "source": "Le Duc Hieu, arXiv:2509.04883, APs of primes in short intervals beyond 17/30",
            "date_checked": "2026-05-26",
            "reported_strength": "uses uniform short-interval PNT at exponents theta>17/30",
            "applicability_to_target_row": "inherits theta>17/30; still above the required theta=1/2 scale",
            "usable_as_closure": False,
            "url": "https://arxiv.org/abs/2509.04883",
        },
        {
            "source": "Pascadi, arXiv:2511.08445, Non-abelian amplification and bilinear forms with Kloosterman sums",
            "date_checked": "2026-05-26",
            "reported_strength": "Type-II Kloosterman savings for composite moduli, with near-prime exceptions and prior prime-modulus inputs",
            "applicability_to_target_row": "our modulus is prime P and current phase is additive e_P(hpm), not a completed inverse-variable Kloosterman family",
            "usable_as_closure": False,
            "url": "https://arxiv.org/abs/2511.08445",
        },
        {
            "source": "Shao--Shparlinski--Wijaya, 2025, Sums of Kloosterman sums over square-free and smooth integers",
            "date_checked": "2026-05-26",
            "reported_strength": "bounds Kloosterman trace sums over square-free/smooth parameters and multiplicative-function twists",
            "applicability_to_target_row": "helpful only after a bridge to Kloosterman trace parameters; p-rough cofactor owner weights are not yet an admissible completed coefficient family",
            "usable_as_closure": False,
            "url": "https://doi.org/10.1017/S0004972725100609",
        },
    ]


def contract_rows() -> list[dict[str, Any]]:
    """列出本层收缩后的合同门。"""
    return [
        {
            "gate": "CompleteNonzeroResidueFourierFingerprint",
            "closed": True,
            "proved": True,
            "meaning": "full-cover 时 owner residues=F_P^*，故每个非零频率 Fourier 和都等于 -1。",
            "remaining": "identity only",
        },
        {
            "gate": "OrdinaryProductWindowAdditiveSavingAsPrimaryGate",
            "closed": True,
            "proved": False,
            "meaning": "任何只给 |S_h|<=B(P) 且 B(P)>=1 的普通节省都与 full-cover 完全兼容。",
            "remaining": NEW_PRIMARY_GATE,
        },
        {
            "gate": NEW_PRIMARY_GATE,
            "closed": False,
            "proved": False,
            "meaning": "需要证明 owner product-window 测度不能等于完整非零剩余类测度，或给出 subunit Fourier 矛盾/PDEC。",
            "remaining": f"{NEW_PRIMARY_GATE} OR signed defect transport",
        },
        {
            "gate": TRACE_GATE,
            "closed": False,
            "proved": False,
            "meaning": "外部 Kloosterman/Type-II 输入只能在完成 trace family 且携带 signed defect 后使用。",
            "remaining": TRACE_GATE,
        },
        {
            "gate": "TargetAffineRowClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本层剪掉普通 additive saving 假出口，但不证明行级正性。",
            "remaining": f"{NEW_PRIMARY_GATE} OR {TRACE_GATE} OR {SQRT_GATE}",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    product_cert = load_json(PRODUCT_PHASE_JSON)
    finite_rows = finite_firewall_rows(product_cert)
    all_identity_ok = bool(finite_rows) and all(
        row["partition_count_ok"]
        and all(
            freq["complete_equals_minus_one_error"] <= NUMERIC_TOLERANCE
            and freq["owner_plus_survivor_partition_error"] <= NUMERIC_TOLERANCE
            and freq["owner_defect_equals_negative_survivor_error"] <= NUMERIC_TOLERANCE
            for freq in row["sampled_frequency_rows"]
        )
        for row in finite_rows
    )
    all_bounds_allow = bool(finite_rows) and all(
        all(freq["ordinary_upper_bounds_all_allow_full_cover"] for freq in row["sampled_frequency_rows"])
        for row in finite_rows
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_additive_saving_firewall_router",
        "status": "ordinary_product_window_additive_saving_rejected_as_primary_closure_gate",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "source_product_phase_imported": product_cert.get("source_keyed_owner_phase_emission_formula_closed") is True,
        "complete_nonzero_residue_fourier_fingerprint_closed": True,
        "finite_complete_measure_identity_all_ok": all_identity_ok,
        "numeric_tolerance": NUMERIC_TOLERANCE,
        "ordinary_product_window_additive_saving_rejected_as_primary_gate": True,
        "ordinary_upper_bounds_all_allow_full_cover_on_audit_rows": all_bounds_allow,
        "product_window_exact_coefficient_separation_proved": False,
        "product_window_to_completed_kloosterman_bridge_with_signed_defect_proved": False,
        "row_column_unconditional_closed": False,
        "old_gate_demoted": OLD_SAVING_GATE,
        "selected_next_primary_gate": NEW_PRIMARY_GATE,
        "selected_parallel_trace_gate": TRACE_GATE,
        "selected_parallel_distribution_gate": SQRT_GATE,
        "finite_firewall_audit": finite_rows,
        "external_applicability_rows": external_applicability_rows(),
        "contract_rows": contract_rows(),
        "plain_conclusion": (
            "Product-window 相位 e_P(hpm) 的普通非零频率节省不能作为主闭合门。"
            "若 full-cover 成立，owner product residues 正好是 F_P^*，所以每个非零频率"
            "的完整和就是 -1；任何上界 |S_h|<=B(P) 且 B(P)>=1 都不会产生矛盾。"
            "因此下一步必须改成精确系数分离、subunit Fourier contradiction、带符号"
            "缺陷的 trace/Kloosterman 桥，或点态 C=1 sqrt 素数输入。"
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格转义。"""
    return str(value).replace("|", r"\|")


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window additive saving 防火墙",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"source_product_phase_imported={fmt_bool(cert['source_product_phase_imported'])}",
        f"complete_nonzero_residue_fourier_fingerprint_closed={fmt_bool(cert['complete_nonzero_residue_fourier_fingerprint_closed'])}",
        f"finite_complete_measure_identity_all_ok={fmt_bool(cert['finite_complete_measure_identity_all_ok'])}",
        f"ordinary_product_window_additive_saving_rejected_as_primary_gate={fmt_bool(cert['ordinary_product_window_additive_saving_rejected_as_primary_gate'])}",
        f"product_window_exact_coefficient_separation_proved={fmt_bool(cert['product_window_exact_coefficient_separation_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 合同门",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in cert["contract_rows"]:
        lines.append(
            f"| `{cell(row['gate'])}` | `{fmt_bool(row['closed'])}` | `{fmt_bool(row['proved'])}` | "
            f"{cell(row['meaning'])} | {cell(row['remaining'])} |"
        )

    lines.extend(
        [
            "",
            "## 2. 有限行 Fourier 防火墙审计",
            "",
            "| P | k | owners | survivors | complete=-1 | ordinary bounds allow full-cover |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in cert["finite_firewall_audit"]:
        complete_ok = all(
            freq["complete_equals_minus_one_error"] <= cert["numeric_tolerance"]
            for freq in row["sampled_frequency_rows"]
        )
        bounds_allow = all(freq["ordinary_upper_bounds_all_allow_full_cover"] for freq in row["sampled_frequency_rows"])
        lines.append(
            f"| {row['P']} | {row['k']} | {row['owner_count']} | {row['survivor_count']} | "
            f"`{fmt_bool(complete_ok)}` | `{fmt_bool(bounds_allow)}` |"
        )

    lines.extend(
        [
            "",
            "## 3. 外部前沿适用性压力测试",
            "",
            "| source | usable as closure | applicability note | url |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_applicability_rows"]:
        lines.append(
            f"| {cell(row['source'])} | `{fmt_bool(row['usable_as_closure'])}` | "
            f"{cell(row['applicability_to_target_row'])} | {row['url']} |"
        )

    lines.extend(
        [
            "",
            "## 4. 下一手",
            "",
            "```text",
            f"old_gate_demoted={cert['old_gate_demoted']}",
            f"selected_next_primary_gate={cert['selected_next_primary_gate']}",
            f"selected_parallel_trace_gate={cert['selected_parallel_trace_gate']}",
            f"selected_parallel_distribution_gate={cert['selected_parallel_distribution_gate']}",
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"source_product_phase_imported={fmt_bool(cert['source_product_phase_imported'])}")
    print(
        "ordinary_product_window_additive_saving_rejected_as_primary_gate="
        f"{fmt_bool(cert['ordinary_product_window_additive_saving_rejected_as_primary_gate'])}"
    )
    print(f"selected_next_primary_gate={cert['selected_next_primary_gate']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
