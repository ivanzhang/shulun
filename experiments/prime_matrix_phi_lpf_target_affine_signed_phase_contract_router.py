#!/usr/bin/env python3
"""生成 target-affine signed phase payload 合同证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_target_affine_signed_phase_contract_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-target-affine-signed-phase-contract-router.json

输出：
  data/prime-matrix-phi-lpf-target-affine-signed-phase-contract-ledger.json
  docs/monograph/prime-matrix-phi-lpf-target-affine-signed-phase-contract-router.json
  docs/monograph/prime-matrix-phi-lpf-target-affine-signed-phase-contract-router.md
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

SLUG = "prime-matrix-phi-lpf-target-affine-signed-phase-contract"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

TARGET_AFFINE_GAP = DOCS / "prime-matrix-phi-lpf-target-affine-gap-equivalence-router.json"
POINTWISE_TABLE = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
RUN_TRACE = DOCS / "prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json"
CORRECTED_TRACE = DOCS / "prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    TARGET_AFFINE_GAP,
    POINTWISE_TABLE,
    RUN_TRACE,
    CORRECTED_TRACE,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]

SOURCE_KEYED_OWNER_PHASE = "SourceKeyedOwnerPhaseEmissionFormula"
COMPLETED_TRACE_FAMILY = "CompletedTraceKloostermanFamilyFromOwnerFibers"
POINTWISE_SQRT_INPUT = "PointwiseSqrtPrimeInputCOne"
ROW_FOURIER_DEFECT = "RowFourierDefectPositiveLowerBound"
PREPUSH_SIGNED_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"


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
    return [value for value, is_prime in enumerate(sieve) if is_prime]


def least_prime_factor(value: int, primes: list[int]) -> int | None:
    """返回 value 的最小素因子；素数返回 None。"""
    limit = math.isqrt(value)
    for p in primes:
        if p > limit:
            return None
        if value % p == 0:
            return p
    return None


def survivor_phase_stats(P: int, survivor_offsets: list[int]) -> dict[str, Any]:
    """计算目标行 prime survivor 的非零 Fourier 能量。"""
    count = len(survivor_offsets)
    max_abs = 0.0
    max_h = 0
    l2_nonzero = 0.0
    for h in range(1, P):
        real = 0.0
        imag = 0.0
        for r in survivor_offsets:
            angle = 2.0 * math.pi * h * r / P
            real += math.cos(angle)
            imag += math.sin(angle)
        mag2 = real * real + imag * imag
        l2_nonzero += mag2
        mag = math.sqrt(mag2)
        if mag > max_abs:
            max_abs = mag
            max_h = h
    formula = P * count - count * count
    return {
        "survivor_count": count,
        "zero_frequency_defect": count,
        "nonzero_l2_numeric": round(l2_nonzero, 9),
        "nonzero_l2_formula": formula,
        "parseval_error": round(abs(l2_nonzero - formula), 9),
        "max_nonzero_abs": round(max_abs, 9),
        "max_nonzero_h": max_h,
        "nonzero_phase_detects_survivors_if_count_positive": bool(count > 0 and formula > 0),
        "detection_is_equivalent_not_lower_bound": True,
    }


def finite_row_audit_rows(gap_cert: dict[str, Any]) -> list[dict[str, Any]]:
    """对上一层有限目标行做 signed phase 恒等式审计。"""
    scan_rows = gap_cert.get("finite_scan_summary", [])
    if not scan_rows:
        return []
    max_value = max((row["min_k"] + 1) * row["P"] for row in scan_rows if row.get("P") and row.get("min_k"))
    primes = primes_up_to(math.isqrt(max_value) + 2)
    audited = []
    for row in scan_rows:
        P = int(row["P"])
        k = int(row["min_k"])
        survivor_offsets: list[int] = []
        owner_counts: dict[int, int] = {}
        for r in range(1, P):
            value = k * P + r
            lpf = least_prime_factor(value, primes)
            if lpf is None:
                survivor_offsets.append(r)
            else:
                owner_counts[lpf] = owner_counts.get(lpf, 0) + 1
        phase = survivor_phase_stats(P, survivor_offsets)
        owner_total = sum(owner_counts.values())
        audited.append(
            {
                "P": P,
                "k": k,
                "row_interval": f"({k}*{P},{k + 1}*{P})",
                "row_length": P - 1,
                "owner_bucket_count": len(owner_counts),
                "owner_total": owner_total,
                "survivor_total": len(survivor_offsets),
                "partition_covers_row": owner_total + len(survivor_offsets) == P - 1,
                "imported_min_prime_count": row.get("min_prime_count"),
                "phase_stats": phase,
            }
        )
    return audited


def contract_rows() -> list[dict[str, Any]]:
    """列出 target-affine signed phase 的非循环合同。"""
    return [
        {
            "gate": "TargetAffineRowFourierDefectIdentity",
            "closed": True,
            "proved": True,
            "meaning": "对任意 h mod P，row indicator = owner composite indicator + prime survivor indicator。",
            "remaining": "identity only",
        },
        {
            "gate": ROW_FOURIER_DEFECT,
            "closed": True,
            "proved": False,
            "meaning": "非零 Fourier 能量等价检测 survivor；但给正下界仍等价于证明行内有素数。",
            "remaining": POINTWISE_SQRT_INPUT,
        },
        {
            "gate": "OwnerResiduePhaseOnlyPayload",
            "closed": True,
            "proved": False,
            "meaning": "只给 a_p=-kP mod p 或 offset Fourier 相位会回到 full-cover/prime-gap 等价式。",
            "remaining": SOURCE_KEYED_OWNER_PHASE,
        },
        {
            "gate": "LambdaMobiusRowPayload",
            "closed": True,
            "proved": False,
            "meaning": "若直接使用 Lambda 或 Mobius-Von-Mangoldt 行权重，就是 theta/psi 行输入，不是 LPF 内生证明。",
            "remaining": POINTWISE_SQRT_INPUT,
        },
        {
            "gate": SOURCE_KEYED_OWNER_PHASE,
            "closed": False,
            "proved": False,
            "meaning": "必须正向给出依赖 owner key、source key、orientation、ExactUV 的相位发射公式。",
            "remaining": f"{SOURCE_KEYED_OWNER_PHASE} OR named PDEC/SAE/LocalSurvivor",
        },
        {
            "gate": COMPLETED_TRACE_FAMILY,
            "closed": False,
            "proved": False,
            "meaning": "必须把 owner fibers 完成到真正 bilinear/trilinear trace 或 Kloosterman family。",
            "remaining": COMPLETED_TRACE_FAMILY,
        },
        {
            "gate": "ExternalKloostermanTraceInputsAdmissibleNow",
            "closed": True,
            "proved": False,
            "meaning": "FKMS/MQW/Pascadi/Wright 等输入是候选，但当前对象还没有完成成它们需要的系数族。",
            "remaining": f"{SOURCE_KEYED_OWNER_PHASE} AND {COMPLETED_TRACE_FAMILY}",
        },
        {
            "gate": "TargetAffineSignedPhasePayloadProved",
            "closed": False,
            "proved": False,
            "meaning": "本步只固定 signed phase 的最小合同，不证明全局行级不等式。",
            "remaining": f"{SOURCE_KEYED_OWNER_PHASE} OR {POINTWISE_SQRT_INPUT} OR {COMPLETED_TRACE_FAMILY}",
        },
    ]


def external_trace_rows() -> list[dict[str, Any]]:
    """列出本层外部前沿定理的精确接入口。"""
    return [
        {
            "input": "Fouvry-Kowalski-Michel-Sawin bilinear trace functions",
            "source": "https://arxiv.org/abs/2511.09459",
            "usable_after": "ell-adic trace family with monodromy/conductor data is constructed",
            "directly_admissible_now": False,
        },
        {
            "input": "Milicevic-Qin-Wu bilinear Kloosterman sums",
            "source": "https://arxiv.org/abs/2511.07550",
            "usable_after": "owner fibers become a two-variable Kloosterman sum modulo moving q",
            "directly_admissible_now": False,
        },
        {
            "input": "Pascadi non-abelian amplification / composite Type-II",
            "source": "https://arxiv.org/abs/2511.08445",
            "usable_after": "well-factorable composite-modulus Type-II coefficients are exposed",
            "directly_admissible_now": False,
        },
        {
            "input": "Wright trilinear Kloosterman fractions",
            "source": "https://arxiv.org/abs/2604.25177",
            "usable_after": "terminal payload becomes a trilinear convolution with equidistributed beta sequence",
            "directly_admissible_now": False,
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    gap_cert = load_json(TARGET_AFFINE_GAP)
    pointwise = load_json(POINTWISE_TABLE)
    run_trace = load_json(RUN_TRACE)
    corrected = load_json(CORRECTED_TRACE)
    synced = gap_cert.get("target_affine_gap_equivalence_synced") is True
    finite_rows = finite_row_audit_rows(gap_cert)
    return {
        "certificate_type": "prime_matrix_phi_lpf_target_affine_signed_phase_contract_router",
        "status": "target_affine_signed_phase_reduced_to_source_keyed_phase_or_sqrt_input",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "target_affine_signed_phase_contract_synced": synced,
        "target_affine_gap_equivalence_imported": synced,
        "pointwise_signed_table_frontier_imported": bool(pointwise),
        "terminal_run_trace_contract_imported": bool(run_trace),
        "corrected_lpf_signed_trace_frontier_imported": bool(corrected),
        "row_fourier_defect_identity_closed": True,
        "row_fourier_positive_lower_bound_proved": False,
        "owner_residue_phase_only_closes": False,
        "lambda_mobius_payload_is_external_prime_input": True,
        "source_keyed_owner_phase_emission_formula_proved": False,
        "completed_trace_kloosterman_family_from_owner_fibers_proved": False,
        "external_trace_inputs_directly_admissible_now": False,
        "target_affine_signed_phase_payload_proved": False,
        "row_column_unconditional_closed": False,
        "finite_row_phase_audit": finite_rows,
        "contract_rows": contract_rows(),
        "external_trace_rows": external_trace_rows(),
        "selected_next_primary_gate": SOURCE_KEYED_OWNER_PHASE,
        "selected_parallel_distribution_gate": POINTWISE_SQRT_INPUT,
        "selected_parallel_trace_gate": COMPLETED_TRACE_FAMILY,
        "selected_direct_table_gate": PREPUSH_SIGNED_TABLE,
        "plain_conclusion": (
            "target-affine signed phase 的第一层相位恒等式已经闭合：row Fourier defect "
            "精确等于 prime survivor Fourier transform。但这只是等价检测；给出正下界仍等价于"
            "证明行内有素数。只使用 owner residue phase 会回到 prime-gap 等价式，直接使用 "
            "Lambda/Mobius 又变成 theta/psi 行输入。非循环突破必须正向构造 source-keyed "
            "owner phase emission formula，或把 owner fibers 完成到可用 trace/Kloosterman family，"
            "或输入真正 C=1 sqrt-scale 点态素数定理。"
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
        "# Prime Matrix Phi-LPF target-affine signed phase contract 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"target_affine_signed_phase_contract_synced={fmt_bool(cert['target_affine_signed_phase_contract_synced'])}",
        f"row_fourier_defect_identity_closed={fmt_bool(cert['row_fourier_defect_identity_closed'])}",
        f"row_fourier_positive_lower_bound_proved={fmt_bool(cert['row_fourier_positive_lower_bound_proved'])}",
        f"source_keyed_owner_phase_emission_formula_proved={fmt_bool(cert['source_keyed_owner_phase_emission_formula_proved'])}",
        f"completed_trace_kloosterman_family_from_owner_fibers_proved={fmt_bool(cert['completed_trace_kloosterman_family_from_owner_fibers_proved'])}",
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
            "## 2. 有限行 phase 审计",
            "",
            "| P | k | primes | owner total | cover | max nonzero Fourier | parseval error |",
            "| ---: | ---: | ---: | ---: | --- | ---: | ---: |",
        ]
    )
    for row in cert["finite_row_phase_audit"]:
        phase = row["phase_stats"]
        lines.append(
            f"| {row['P']} | {row['k']} | {row['survivor_total']} | {row['owner_total']} | "
            f"`{fmt_bool(row['partition_covers_row'])}` | {phase['max_nonzero_abs']} | "
            f"{phase['parseval_error']} |"
        )

    lines.extend(
        [
            "",
            "## 3. 外部 trace/Kloosterman 输入接入口",
            "",
            "| input | directly admissible now | usable after | source |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_trace_rows"]:
        lines.append(
            f"| {cell(row['input'])} | `{fmt_bool(row['directly_admissible_now'])}` | "
            f"{cell(row['usable_after'])} | {cell(row['source'])} |"
        )

    lines.extend(
        [
            "",
            "```text",
            f"selected_next_primary_gate={cert['selected_next_primary_gate']}",
            f"selected_parallel_distribution_gate={cert['selected_parallel_distribution_gate']}",
            f"selected_parallel_trace_gate={cert['selected_parallel_trace_gate']}",
            f"selected_direct_table_gate={cert['selected_direct_table_gate']}",
            "```",
            "",
            "## 4. 依赖哈希",
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
    print(f"target_affine_signed_phase_contract_synced={fmt_bool(cert['target_affine_signed_phase_contract_synced'])}")
    print(f"row_fourier_defect_identity_closed={fmt_bool(cert['row_fourier_defect_identity_closed'])}")
    print(f"selected_next_primary_gate={cert['selected_next_primary_gate']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
