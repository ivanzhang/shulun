#!/usr/bin/env python3
"""归档 product-window 精确系数分离的等价边界。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_exact_separation_equivalence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-exact-separation-equivalence-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-exact-separation-equivalence-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-exact-separation-equivalence-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-exact-separation-equivalence-router.md

本证书承接 product-window additive-saving firewall。它把
ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC
继续拆开：若“精确分离”只是说 owner product-window 测度不等于完整非零
剩余类测度，那么它与 prime survivor 非空完全等价；若“subunit Fourier
contradiction”没有独立 signed defect 来源，也只是同一等价命题的 Fourier
重写。非循环主攻必须转向独立 signed defect emission、带 defect 的 completed
trace/Kloosterman family、点态 sqrt 素数输入，或非平凡 PDEC。
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

SLUG = "prime-matrix-phi-lpf-product-window-exact-separation-equivalence"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

FIREWALL_JSON = DOCS / "prime-matrix-phi-lpf-product-window-additive-saving-firewall-router.json"
PRODUCT_PHASE_JSON = DOCS / "prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.json"
MINIMAL_ROUTE_JSON = DOCS / "prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    FIREWALL_JSON,
    PRODUCT_PHASE_JSON,
    MINIMAL_ROUTE_JSON,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]

OLD_PRIMARY_GATE = "ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC"
NEW_PRIMARY_GATE = "IndependentSignedDefectEmissionBeforeProductWindowPushforward"
TRACE_GATE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients"
SQRT_GATE = "PointwiseSqrtPrimeInputCOne"
PDEC_GATE = "NonTautologicalProductWindowPDEC"
NUMERIC_TOLERANCE = 1e-6


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


def cis(P: int, h: int, r: int) -> complex:
    """返回 e_P(hr)。"""
    angle = 2.0 * math.pi * h * (r % P) / P
    return complex(math.cos(angle), math.sin(angle))


def row_equivalence_audit(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """核验 defect Fourier 能量与 survivor 数量的等价关系。"""
    owner = [0] * P
    survivor = [0] * P
    for r in range(1, P):
        n = k * P + r
        if least_prime_factor(n, primes) is None:
            survivor[r] = 1
        else:
            owner[r] = 1

    survivor_count = sum(survivor)
    owner_count = sum(owner)
    nonzero_defect_energy = 0.0
    max_defect_partition_error = 0.0
    nonzero_defect_count = 0
    min_owner_minus_complete_abs = None
    for h in range(1, P):
        owner_sum = sum(owner[r] * cis(P, h, r) for r in range(P))
        survivor_sum = sum(survivor[r] * cis(P, h, r) for r in range(P))
        complete_sum = sum(cis(P, h, r) for r in range(1, P))
        defect = owner_sum - complete_sum
        max_defect_partition_error = max(max_defect_partition_error, abs(defect + survivor_sum))
        nonzero_defect_energy += abs(defect) ** 2
        if abs(defect) > NUMERIC_TOLERANCE:
            nonzero_defect_count += 1
        current_abs = abs(owner_sum - complete_sum)
        min_owner_minus_complete_abs = (
            current_abs
            if min_owner_minus_complete_abs is None
            else min(min_owner_minus_complete_abs, current_abs)
        )

    expected_energy = P * survivor_count - survivor_count * survivor_count
    energy_error = abs(nonzero_defect_energy - expected_energy)
    exact_separation = survivor_count > 0
    fourier_separation = nonzero_defect_count > 0
    return {
        "P": P,
        "k": k,
        "row_length": P - 1,
        "owner_count": owner_count,
        "survivor_count": survivor_count,
        "owner_plus_survivor_equals_complete_count": owner_count + survivor_count == P - 1,
        "exact_measure_separation_holds": exact_separation,
        "fourier_nonminusone_contradiction_holds": fourier_separation,
        "separation_equivalent_to_survivor_nonempty_on_row": exact_separation == fourier_separation,
        "nonzero_defect_frequency_count": nonzero_defect_count,
        "defect_parseval_energy": round(nonzero_defect_energy, 9),
        "expected_parseval_energy_Ps_minus_s2": round(expected_energy, 9),
        "defect_parseval_energy_error": round(energy_error, 9),
        "max_defect_partition_error": round(max_defect_partition_error, 12),
        "min_abs_owner_minus_complete_over_nonzero_frequencies": round(min_owner_minus_complete_abs or 0.0, 12),
    }


def finite_equivalence_rows(firewall_cert: dict[str, Any]) -> list[dict[str, Any]]:
    """从上一层有限行生成等价审计。"""
    rows = firewall_cert.get("finite_firewall_audit", [])
    normalized = [{"P": int(row["P"]), "k": int(row["k"])} for row in rows]
    max_value = max((row["k"] + 1) * row["P"] for row in normalized)
    primes = primes_up_to(math.isqrt(max_value) + 2)
    return [row_equivalence_audit(row["P"], row["k"], primes) for row in normalized]


def external_trace_rows() -> list[dict[str, Any]]:
    """登记当前外部 trace 前沿对本层的精确适用条件。"""
    return [
        {
            "source": "Fouvry--Kowalski--Michel--Sawin, arXiv:2511.09459, Bilinear forms with trace functions",
            "frontier_value": "general bilinear trace-function bounds below the Polya--Vinogradov range under geometric monodromy hypotheses",
            "missing_bridge": "our current defect is an owner-minus-complete coefficient on product-window residues, not yet an l-adic trace sheaf family with admissible coefficient norms",
            "usable_now": False,
            "url": "https://arxiv.org/abs/2511.09459",
        },
        {
            "source": "Pascadi, arXiv:2511.08445, Non-abelian amplification and bilinear forms with Kloosterman sums",
            "frontier_value": "Type-II Kloosterman savings, especially for composite moduli with prime-modulus inputs imported",
            "missing_bridge": "our modulus is prime P and the phase is additive product-window defect, not completed inverse-variable Kloosterman data",
            "usable_now": False,
            "url": "https://arxiv.org/abs/2511.08445",
        },
        {
            "source": "Guth--Maynard and Hieu short-interval inputs",
            "frontier_value": "pointwise short intervals only beyond theta>17/30 in the current corpus",
            "missing_bridge": "target row at x≈P^2 requires theta=1/2 with constant C<=1",
            "usable_now": False,
            "url": "https://arxiv.org/abs/2405.20552",
        },
    ]


def contract_rows() -> list[dict[str, Any]]:
    """列出本层收缩后的合同门。"""
    return [
        {
            "gate": "OwnerCompleteDefectFourierInversionIdentity",
            "closed": True,
            "proved": True,
            "meaning": "owner-complete defect equals negative survivor measure; Parseval energy is P*s-s^2.",
            "remaining": "identity only",
        },
        {
            "gate": "ExactCoefficientSeparationAsStandaloneClosure",
            "closed": True,
            "proved": False,
            "meaning": "standalone exact separation is equivalent to survivor nonempty and cannot be used as independent proof.",
            "remaining": NEW_PRIMARY_GATE,
        },
        {
            "gate": "SubunitFourierContradictionAsStandaloneClosure",
            "closed": True,
            "proved": False,
            "meaning": "without an independent source for the defect, Fourier non-minus-one/subunit contradiction is the same row prime statement.",
            "remaining": NEW_PRIMARY_GATE,
        },
        {
            "gate": NEW_PRIMARY_GATE,
            "closed": False,
            "proved": False,
            "meaning": "需要在 Fourier pushforward 前产生独立 signed defect，不是事后用 survivor 定义 defect。",
            "remaining": f"{NEW_PRIMARY_GATE} OR {PDEC_GATE}",
        },
        {
            "gate": TRACE_GATE,
            "closed": False,
            "proved": False,
            "meaning": "需要把 signed defect 完成到可套用 FKMS/DI/BFI/Pascadi 类 theorem 的 coefficient/trace family。",
            "remaining": TRACE_GATE,
        },
        {
            "gate": "TargetAffineRowClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本层只排除 exact separation 的循环用法，不证明行级正性。",
            "remaining": f"{NEW_PRIMARY_GATE} OR {TRACE_GATE} OR {SQRT_GATE} OR {PDEC_GATE}",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    firewall_cert = load_json(FIREWALL_JSON)
    minimal_route = load_json(MINIMAL_ROUTE_JSON)
    finite_rows = finite_equivalence_rows(firewall_cert)
    all_identity_ok = bool(finite_rows) and all(
        row["owner_plus_survivor_equals_complete_count"]
        and row["separation_equivalent_to_survivor_nonempty_on_row"]
        and row["defect_parseval_energy_error"] <= NUMERIC_TOLERANCE
        and row["max_defect_partition_error"] <= NUMERIC_TOLERANCE
        for row in finite_rows
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_exact_separation_equivalence_router",
        "status": "exact_coefficient_separation_demoted_to_survivor_equivalence",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "source_firewall_imported": firewall_cert.get(
            "ordinary_product_window_additive_saving_rejected_as_primary_gate"
        )
        is True,
        "fourier_inversion_defect_identity_closed": True,
        "exact_coefficient_separation_equivalent_to_survivor_nonempty": True,
        "subunit_or_nonminusone_fourier_contradiction_equivalent_to_survivor_nonempty_without_independent_defect": True,
        "standalone_exact_separation_rejected_as_noncircular_primary_gate": True,
        "independent_signed_defect_emission_proved": False,
        "completed_trace_bridge_with_signed_defect_proved": False,
        "row_column_unconditional_closed": False,
        "old_gate_demoted": OLD_PRIMARY_GATE,
        "selected_next_primary_gate": NEW_PRIMARY_GATE,
        "selected_parallel_trace_gate": TRACE_GATE,
        "selected_parallel_distribution_gate": SQRT_GATE,
        "selected_parallel_pdec_gate": PDEC_GATE,
        "minimal_route_context_status": minimal_route.get("status"),
        "finite_equivalence_audit": finite_rows,
        "external_trace_applicability_rows": external_trace_rows(),
        "contract_rows": contract_rows(),
        "plain_conclusion": (
            "Product-window 的 exact coefficient separation 若只是说 owner measure "
            "不等于完整非零剩余类 measure，则它与 prime survivor 非空完全等价。"
            "Fourier 形式同样如此：owner-complete defect 等于负 survivor measure，"
            "非零频率 Parseval 能量为 P*s-s^2，正性当且仅当 survivor 数 s>0。"
            "因此本层把 standalone exact separation/subunit Fourier contradiction 降级为循环门；"
            "下一步必须在 pushforward 前构造独立 signed defect，或完成带 defect 的 trace/Type-II "
            "family，或输入 C=1 sqrt 级点态素数定理，或给出非平凡 PDEC。"
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
        "# Prime Matrix Phi-LPF product-window exact separation 等价边界",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"source_firewall_imported={fmt_bool(cert['source_firewall_imported'])}",
        f"fourier_inversion_defect_identity_closed={fmt_bool(cert['fourier_inversion_defect_identity_closed'])}",
        f"exact_coefficient_separation_equivalent_to_survivor_nonempty={fmt_bool(cert['exact_coefficient_separation_equivalent_to_survivor_nonempty'])}",
        "subunit_or_nonminusone_fourier_contradiction_equivalent_to_survivor_nonempty_without_independent_defect="
        f"{fmt_bool(cert['subunit_or_nonminusone_fourier_contradiction_equivalent_to_survivor_nonempty_without_independent_defect'])}",
        f"standalone_exact_separation_rejected_as_noncircular_primary_gate={fmt_bool(cert['standalone_exact_separation_rejected_as_noncircular_primary_gate'])}",
        f"independent_signed_defect_emission_proved={fmt_bool(cert['independent_signed_defect_emission_proved'])}",
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
            "## 2. 有限行等价审计",
            "",
            "| P | k | owners | survivors | energy identity | separation iff survivor | nonzero defect freqs |",
            "| ---: | ---: | ---: | ---: | --- | --- | ---: |",
        ]
    )
    for row in cert["finite_equivalence_audit"]:
        energy_ok = row["defect_parseval_energy_error"] <= NUMERIC_TOLERANCE
        lines.append(
            f"| {row['P']} | {row['k']} | {row['owner_count']} | {row['survivor_count']} | "
            f"`{fmt_bool(energy_ok)}` | `{fmt_bool(row['separation_equivalent_to_survivor_nonempty_on_row'])}` | "
            f"{row['nonzero_defect_frequency_count']} |"
        )

    lines.extend(
        [
            "",
            "## 3. 外部 trace 前沿适用性",
            "",
            "| source | usable now | missing bridge | url |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_trace_applicability_rows"]:
        lines.append(
            f"| {cell(row['source'])} | `{fmt_bool(row['usable_now'])}` | "
            f"{cell(row['missing_bridge'])} | {row['url']} |"
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
            f"selected_parallel_pdec_gate={cert['selected_parallel_pdec_gate']}",
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
    print(f"source_firewall_imported={fmt_bool(cert['source_firewall_imported'])}")
    print(
        "standalone_exact_separation_rejected_as_noncircular_primary_gate="
        f"{fmt_bool(cert['standalone_exact_separation_rejected_as_noncircular_primary_gate'])}"
    )
    print(f"selected_next_primary_gate={cert['selected_next_primary_gate']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
