#!/usr/bin/env python3
"""生成 target-affine source-keyed product phase 发射证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_target_affine_source_keyed_product_phase_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.json

输出：
  data/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-ledger.json
  docs/monograph/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.json
  docs/monograph/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.md
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

SLUG = "prime-matrix-phi-lpf-target-affine-source-keyed-product-phase"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SIGNED_PHASE = DOCS / "prime-matrix-phi-lpf-target-affine-signed-phase-contract-router.json"
GAP_EQUIV = DOCS / "prime-matrix-phi-lpf-target-affine-gap-equivalence-router.json"
POINTWISE_TABLE = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
RUN_TRACE = DOCS / "prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    SIGNED_PHASE,
    GAP_EQUIV,
    POINTWISE_TABLE,
    RUN_TRACE,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]

PRODUCT_PHASE = "SourceKeyedProductWindowPhaseEmissionIdentity"
PRODUCT_SAVING = "ProductWindowBilinearAdditivePhaseSavingOrPDEC"
KLOOSTERMAN_BRIDGE = "ProductWindowToCompletedKloostermanOrTraceBridge"
TYPEII_COEFF = "LPFOwnerRoughCofactorWeightsToTypeIICoefficients"
SQRT_INPUT = "PointwiseSqrtPrimeInputCOne"


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
    """返回合数的最小素因子；素数返回 None。"""
    limit = math.isqrt(value)
    for p in primes:
        if p > limit:
            return None
        if value % p == 0:
            return p
    return None


def is_p_rough(value: int, p: int, primes: list[int]) -> bool:
    """判断 value 是否没有小于 p 的素因子。"""
    return all(value % q != 0 for q in primes if q < p)


def selected_frequencies(P: int) -> list[int]:
    """选取少量代表频率做数值相位和核验。"""
    raw = [1, 2, 3, (P - 1) // 2, P - 1]
    return sorted({h for h in raw if 1 <= h <= P - 1})


def row_product_phase_audit(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """核验 owner offset phase 等于 source-keyed product phase。"""
    keys: list[dict[str, int]] = []
    survivor_count = 0
    for r in range(1, P):
        n = k * P + r
        p = least_prime_factor(n, primes)
        if p is None:
            survivor_count += 1
            continue
        m = n // p
        keys.append({"r": r, "n": n, "p": p, "m": m})

    congruence_ok = all((key["r"] - key["p"] * key["m"]) % P == 0 for key in keys)
    owner_residue_ok = all((key["r"] + k * P) % key["p"] == 0 for key in keys)
    rough_ok = all(is_p_rough(key["m"], key["p"], primes) for key in keys)
    window_ok = all(k * P < key["p"] * key["m"] < (k + 1) * P for key in keys)
    lpf_bound_ok = all(key["p"] <= math.isqrt(key["n"]) for key in keys)
    residue_collision_free = len({key["p"] * key["m"] % P for key in keys}) == len(keys)

    freq_rows = []
    for h in selected_frequencies(P):
        owner_real = owner_imag = product_real = product_imag = 0.0
        for key in keys:
            angle_owner = 2.0 * math.pi * h * key["r"] / P
            angle_product = 2.0 * math.pi * h * (key["p"] * key["m"] % P) / P
            owner_real += math.cos(angle_owner)
            owner_imag += math.sin(angle_owner)
            product_real += math.cos(angle_product)
            product_imag += math.sin(angle_product)
        error = math.hypot(owner_real - product_real, owner_imag - product_imag)
        freq_rows.append(
            {
                "h": h,
                "owner_abs": round(math.hypot(owner_real, owner_imag), 9),
                "product_abs": round(math.hypot(product_real, product_imag), 9),
                "phase_error": round(error, 12),
            }
        )

    p_counts: dict[int, int] = {}
    for key in keys:
        p_counts[key["p"]] = p_counts.get(key["p"], 0) + 1
    top_owner_counts = sorted(p_counts.items(), key=lambda item: (-item[1], item[0]))[:8]

    return {
        "P": P,
        "k": k,
        "row_length": P - 1,
        "owner_key_count": len(keys),
        "survivor_count": survivor_count,
        "partition_count_ok": len(keys) + survivor_count == P - 1,
        "source_keyed_product_phase_congruence_ok": congruence_ok,
        "owner_residue_condition_ok": owner_residue_ok,
        "rough_cofactor_condition_ok": rough_ok,
        "product_window_condition_ok": window_ok,
        "lpf_bound_condition_ok": lpf_bound_ok,
        "product_residue_collision_free_on_owner_keys": residue_collision_free,
        "selected_frequency_phase_rows": freq_rows,
        "top_owner_bucket_counts": [{"p": p, "count": count} for p, count in top_owner_counts],
    }


def finite_audit_rows(signed_cert: dict[str, Any], gap_cert: dict[str, Any]) -> list[dict[str, Any]]:
    """从上一层有限行抽样生成 product phase 审计。"""
    rows = signed_cert.get("finite_row_phase_audit") or gap_cert.get("finite_scan_summary") or []
    normalized: list[dict[str, int]] = []
    for row in rows:
        P = int(row["P"])
        k = int(row.get("k", row.get("min_k")))
        normalized.append({"P": P, "k": k})
    max_value = max((row["k"] + 1) * row["P"] for row in normalized)
    primes = primes_up_to(math.isqrt(max_value) + 2)
    return [row_product_phase_audit(row["P"], row["k"], primes) for row in normalized]


def contract_rows() -> list[dict[str, Any]]:
    """列出本层收缩后的合同门。"""
    return [
        {
            "gate": PRODUCT_PHASE,
            "closed": True,
            "proved": True,
            "meaning": "对每个 owner key n=pm=kP+r，offset phase e_P(hr) 精确等于 product phase e_P(hpm)。",
            "remaining": "identity only",
        },
        {
            "gate": "FullCoverProductPhaseEquation",
            "closed": True,
            "proved": False,
            "meaning": "若 full cover 成立，则 owner product residues 是 F_P^* 的排列，所有非零频率和为 -1。",
            "remaining": PRODUCT_SAVING,
        },
        {
            "gate": PRODUCT_SAVING,
            "closed": False,
            "proved": False,
            "meaning": "需要证明目标 product-window rough-owner 集不可能模拟全体非零 residue，或给出符号节省。",
            "remaining": f"{PRODUCT_SAVING} OR named PDEC/SAE/LocalSurvivor",
        },
        {
            "gate": KLOOSTERMAN_BRIDGE,
            "closed": False,
            "proved": False,
            "meaning": "当前相位是 e_P(hpm) 与双曲窗口；不是已完成的 inverse-variable Kloosterman family。",
            "remaining": KLOOSTERMAN_BRIDGE,
        },
        {
            "gate": TYPEII_COEFF,
            "closed": False,
            "proved": False,
            "meaning": "p-rough cofactor weights 还没有转成外部 Type-II theorem 可接受的 well-factorable 系数。",
            "remaining": TYPEII_COEFF,
        },
        {
            "gate": "TargetAffineRowClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本层关闭 source-keyed emission identity，但不证明行级正性。",
            "remaining": f"{PRODUCT_SAVING} OR {KLOOSTERMAN_BRIDGE} OR {SQRT_INPUT}",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    signed_cert = load_json(SIGNED_PHASE)
    gap_cert = load_json(GAP_EQUIV)
    finite_rows = finite_audit_rows(signed_cert, gap_cert)
    all_identity_ok = bool(finite_rows) and all(
        row["source_keyed_product_phase_congruence_ok"]
        and row["owner_residue_condition_ok"]
        and row["rough_cofactor_condition_ok"]
        and row["product_window_condition_ok"]
        and row["lpf_bound_condition_ok"]
        for row in finite_rows
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_target_affine_source_keyed_product_phase_router",
        "status": "source_keyed_owner_phase_emission_closed_to_product_window_phase",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "target_affine_source_keyed_product_phase_synced": signed_cert.get(
            "target_affine_signed_phase_contract_synced"
        )
        is True,
        "source_keyed_owner_phase_emission_formula_closed": True,
        "source_keyed_product_phase_identity": "n=pm=kP+r => r≡pm (mod P), hence e_P(h r)=e_P(h p m)",
        "finite_product_phase_identity_all_ok": all_identity_ok,
        "full_cover_product_phase_equation_closed": True,
        "product_window_bilinear_additive_phase_saving_proved": False,
        "product_window_to_completed_kloosterman_bridge_proved": False,
        "lpf_owner_rough_cofactor_weights_to_typeii_coefficients_proved": False,
        "row_column_unconditional_closed": False,
        "finite_product_phase_audit": finite_rows,
        "contract_rows": contract_rows(),
        "selected_next_primary_gate": PRODUCT_SAVING,
        "selected_parallel_trace_gate": KLOOSTERMAN_BRIDGE,
        "selected_parallel_typeii_gate": TYPEII_COEFF,
        "selected_parallel_distribution_gate": SQRT_INPUT,
        "plain_conclusion": (
            "Source-keyed owner phase 的代数发射式已经闭合：每个 LPF owner 元素 "
            "n=pm=kP+r 都满足 r≡pm mod P，因此 offset Fourier phase 可无损改写为 "
            "source-keyed product-window phase e_P(hpm)。这是真推进，因为抽象 source key "
            "已变成显式 (p,m) product phase；但它仍只是恒等式。full-cover 时该 product "
            "residue 集会成为 F_P^* 的排列，非零频率和等于 -1。要非循环突破，下一步必须证明 "
            "ProductWindowBilinearAdditivePhaseSaving/PDEC，或把这个双曲 product-window 完成到"
            "外部 trace/Kloosterman/Type-II 可接受的系数族，或输入 C=1 sqrt 级点态素数定理。"
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
        "# Prime Matrix Phi-LPF target-affine source-keyed product phase 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"target_affine_source_keyed_product_phase_synced={fmt_bool(cert['target_affine_source_keyed_product_phase_synced'])}",
        f"source_keyed_owner_phase_emission_formula_closed={fmt_bool(cert['source_keyed_owner_phase_emission_formula_closed'])}",
        f"finite_product_phase_identity_all_ok={fmt_bool(cert['finite_product_phase_identity_all_ok'])}",
        f"product_window_bilinear_additive_phase_saving_proved={fmt_bool(cert['product_window_bilinear_additive_phase_saving_proved'])}",
        f"product_window_to_completed_kloosterman_bridge_proved={fmt_bool(cert['product_window_to_completed_kloosterman_bridge_proved'])}",
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
            "## 2. 有限行 product phase 审计",
            "",
            "| P | k | owner keys | survivors | identity | rough | window | max phase error |",
            "| ---: | ---: | ---: | ---: | --- | --- | --- | ---: |",
        ]
    )
    for row in cert["finite_product_phase_audit"]:
        max_error = max(item["phase_error"] for item in row["selected_frequency_phase_rows"])
        lines.append(
            f"| {row['P']} | {row['k']} | {row['owner_key_count']} | {row['survivor_count']} | "
            f"`{fmt_bool(row['source_keyed_product_phase_congruence_ok'])}` | "
            f"`{fmt_bool(row['rough_cofactor_condition_ok'])}` | "
            f"`{fmt_bool(row['product_window_condition_ok'])}` | {max_error} |"
        )

    lines.extend(
        [
            "",
            "## 3. 下一手",
            "",
            "```text",
            f"selected_next_primary_gate={cert['selected_next_primary_gate']}",
            f"selected_parallel_trace_gate={cert['selected_parallel_trace_gate']}",
            f"selected_parallel_typeii_gate={cert['selected_parallel_typeii_gate']}",
            f"selected_parallel_distribution_gate={cert['selected_parallel_distribution_gate']}",
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
    print(
        "target_affine_source_keyed_product_phase_synced="
        f"{fmt_bool(cert['target_affine_source_keyed_product_phase_synced'])}"
    )
    print(
        "source_keyed_owner_phase_emission_formula_closed="
        f"{fmt_bool(cert['source_keyed_owner_phase_emission_formula_closed'])}"
    )
    print(f"selected_next_primary_gate={cert['selected_next_primary_gate']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
