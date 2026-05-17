#!/usr/bin/env python3
"""把非实半类 simplex 硬点继续压成补偿质量与方差恒等式。

用法示例：
  python3 experiments/prime_matrix_nonreal_halfclass_compensation_variance_router.py
  python3 experiments/prime_matrix_nonreal_halfclass_compensation_variance_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-nonreal-halfclass-compensation-variance-router.json

输出：
  data/prime-matrix-nonreal-halfclass-compensation-variance-ledger.json
  docs/monograph/prime-matrix-nonreal-halfclass-compensation-variance-router.json
  docs/monograph/prime-matrix-nonreal-halfclass-compensation-variance-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from bisect import bisect_right
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

OUT_LEDGER = DATA / "prime-matrix-nonreal-halfclass-compensation-variance-ledger.json"
OUT_JSON = DOCS / "prime-matrix-nonreal-halfclass-compensation-variance-router.json"
OUT_MD = DOCS / "prime-matrix-nonreal-halfclass-compensation-variance-router.md"

PREVIOUS = "prime-matrix-nonreal-halfclass-simplex-phase-router.json"
HALFCLASS_MARGIN = "prime-matrix-siegel-quadratic-halfclass-margin-router.json"
SIEGEL_SPLIT = "prime-matrix-explicit-ap-zero-packet-siegel-split-router.json"
RANKONE = "prime-matrix-linnik2-rankone-phase-capacity-router.json"
STATUS_TABLE = "claim-status-table.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_VIII = ROOT / "docs" / "prime-density-waves-VIII.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

PREVIOUS_TARGET = "NonrealHalfClassSimplexRankOneProjectionExclusionAtP2"
NEXT_TARGET = "HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC"
QUADRATIC_MARGIN_TARGET = "QuadraticHalfClassSquareScaleBiasMarginTheorem"
EFFECTIVE_NO_SIEGEL = "EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale"
PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / PREVIOUS,
    DOCS / HALFCLASS_MARGIN,
    DOCS / SIEGEL_SPLIT,
    DOCS / RANKONE,
    DOCS / STATUS_TABLE,
    FINAL_PROOF_DRAFT,
    PRIME_DENSITY_WAVES_VIII,
    PRIME_DENSITY_WAVES_X,
    PAPER,
]


def sieve(limit: int) -> tuple[bytearray, list[int]]:
    """返回素数布尔表和素数列表。"""
    if limit < 2:
        return bytearray(limit + 1), []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    root = math.isqrt(limit)
    for n in range(2, root + 1):
        if flags[n]:
            start = n * n
            flags[start : limit + 1 : n] = b"\x00" * (((limit - start) // n) + 1)
    return flags, [i for i in range(2, limit + 1) if flags[i]]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    result: dict[str, str] = {}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def legendre_symbol(a: int, p: int) -> int:
    """计算素模 p 下的 Legendre 符号。"""
    value = pow(a % p, (p - 1) // 2, p)
    if value == p - 1:
        return -1
    return value


def theta_vector_for_modulus(p: int, primes: list[int]) -> list[float]:
    """计算 theta(P^2;P,a) 向量。"""
    theta = [0.0] * p
    cutoff = bisect_right(primes, p * p)
    for ell in primes[:cutoff]:
        if ell == p:
            continue
        theta[ell % p] += math.log(ell)
    return theta


def halfclass_records_for_modulus(p: int, primes: list[int]) -> list[dict[str, Any]]:
    """计算两个二次半类的中心化补偿与方差诊断。"""
    theta = theta_vector_for_modulus(p, primes)
    t0 = math.fsum(theta[1:])
    t_quad = math.fsum(legendre_symbol(a, p) * theta[a] for a in range(1, p))
    h = (p - 1) // 2
    records: list[dict[str, Any]] = []
    for sign, name in ((1, "quadratic_residue"), (-1, "quadratic_nonresidue")):
        members = [a for a in range(1, p) if legendre_symbol(a, p) == sign]
        half_mass = math.fsum(theta[a] for a in members)
        expected_half_mass = 0.5 * (t0 + sign * t_quad)
        mu = half_mass / h
        required_zero_projection = (p - 1) * mu
        residuals = [(p - 1) * (theta[a] - mu) for a in members]
        min_index, min_residual = min(enumerate(residuals), key=lambda item: (item[1], members[item[0]]))
        min_residue = members[min_index]
        actual_negative_projection = max(0.0, -min_residual)
        half_square = math.fsum(value * value for value in residuals)
        one_hole_floor = (
            required_zero_projection * required_zero_projection * h / (h - 1) if h > 1 else float("inf")
        )
        actual_min_floor = (
            actual_negative_projection * actual_negative_projection * h / (h - 1) if h > 1 else float("inf")
        )
        flat_zero_lift_ratio = h / (h - 1) if h > 1 else float("inf")
        records.append(
            {
                "P": p,
                "halfclass": name,
                "legendre_sign": sign,
                "halfclass_size": h,
                "T0": t0,
                "T_quadratic": t_quad,
                "half_mass": half_mass,
                "expected_half_mass_from_T0_T2": expected_half_mass,
                "half_mass_identity_error": half_mass - expected_half_mass,
                "halfclass_mean_theta": mu,
                "required_zero_projection": required_zero_projection,
                "same_half_compensation_average_if_zero": required_zero_projection / (h - 1),
                "flat_zero_compensator_theta_level": mu * flat_zero_lift_ratio,
                "flat_zero_lift_ratio": flat_zero_lift_ratio,
                "min_residue": min_residue,
                "min_theta": theta[min_residue],
                "min_residual": min_residual,
                "actual_negative_projection": actual_negative_projection,
                "actual_negative_to_zero_projection_ratio": (
                    actual_negative_projection / required_zero_projection if required_zero_projection else 0.0
                ),
                "halfclass_centering_abs_error": abs(math.fsum(residuals)),
                "halfclass_residual_square": half_square,
                "sharp_one_hole_variance_floor": one_hole_floor,
                "actual_min_residue_variance_floor": actual_min_floor,
                "halfclass_square_to_zero_floor_ratio": half_square / one_hole_floor if one_hole_floor else None,
                "halfclass_square_to_actual_min_floor_ratio": (
                    half_square / actual_min_floor if actual_min_floor else None
                ),
                "capacity_false_positive_for_zero_floor": bool(half_square >= one_hole_floor),
            }
        )
    return records


def finite_diagnostic(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """有限扫描只定位补偿/容量误差形态，不作为无限证明输入。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records: list[dict[str, Any]] = []
    for p in prime_moduli:
        records.extend(halfclass_records_for_modulus(p, primes))

    by_deficit = sorted(
        records,
        key=lambda item: (item["actual_negative_to_zero_projection_ratio"], item["P"]),
        reverse=True,
    )
    by_variance = sorted(
        records,
        key=lambda item: (item["halfclass_square_to_zero_floor_ratio"] or -1.0, item["P"]),
        reverse=True,
    )
    false_positives = [item for item in records if item["capacity_false_positive_for_zero_floor"]]
    max_centering_error = max((item["halfclass_centering_abs_error"] for item in records), default=0.0)
    max_half_mass_error = max((abs(item["half_mass_identity_error"]) for item in records), default=0.0)
    return {
        "min_p": min_p,
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "halfclass_records_checked": len(records),
        "max_halfclass_centering_abs_error": max_centering_error,
        "max_half_mass_identity_abs_error": max_half_mass_error,
        "capacity_false_positive_for_zero_floor_count": len(false_positives),
        "max_actual_negative_to_zero_projection_ratio": (
            by_deficit[0]["actual_negative_to_zero_projection_ratio"] if by_deficit else None
        ),
        "max_deficit_ratio_modulus": by_deficit[0]["P"] if by_deficit else None,
        "max_deficit_ratio_halfclass": by_deficit[0]["halfclass"] if by_deficit else None,
        "max_halfclass_square_to_zero_floor_ratio": (
            by_variance[0]["halfclass_square_to_zero_floor_ratio"] if by_variance else None
        ),
        "max_variance_ratio_modulus": by_variance[0]["P"] if by_variance else None,
        "min_flat_zero_lift_ratio": min((item["flat_zero_lift_ratio"] for item in records), default=None),
        "max_flat_zero_lift_ratio": max((item["flat_zero_lift_ratio"] for item in records), default=None),
        "top_deficit_records": by_deficit[:top],
        "top_variance_records": by_variance[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录半类补偿恒等式。"""
    return [
        {
            "item": "halfclass mean after removing principal/quadratic",
            "formula": "mu_s=(T0+sT2)/(P-1), s in {+1,-1}",
        },
        {
            "item": "centered nonreal residual",
            "formula": "R_a=(P-1)(theta_a-mu_s) for chi_2(a)=s",
        },
        {
            "item": "halfclass centering",
            "formula": "sum_{chi_2(a)=s} R_a=0",
        },
        {
            "item": "zero column compensation mass",
            "formula": "theta_a=0 implies R_a=-(P-1)mu_s and sum_{b!=a, chi_2(b)=s} R_b=(P-1)mu_s",
        },
        {
            "item": "sharp one-hole variance floor",
            "formula": "sum_{chi_2(b)=s} R_b^2 >= ((P-1)mu_s)^2*h/(h-1), h=(P-1)/2",
        },
        {
            "item": "flat extremizer",
            "formula": "equality occurs when all non-hole residues in the same halfclass have theta_b=mu_s*h/(h-1)",
        },
        {
            "item": "new hardpoint",
            "formula": "exclude the flat/near-flat compensation profile by actual prime phase, or register ColumnCRT/PDEC",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": PREVIOUS_TARGET,
            "route": NEXT_TARGET,
            "status": "sharpened but open",
            "meaning": "rank-one 负投影被改写为同半类一个缺孔与其余列的等量正补偿。",
        },
        {
            "branch": "capacity-only variance argument",
            "route": "sharp one-hole floor is necessary and convexly sharp",
            "status": "closed as insufficient",
            "meaning": "方差地板达到或超过并不排除零列；平铺补偿向量本身非负且满足半类中心化。",
        },
        {
            "branch": NEXT_TARGET,
            "route": "prove true prime-induced compensation cannot remain flat without persistent CRT phase defect",
            "status": "not proved in corpus",
            "meaning": "这是非实 AP 分支的最新最窄自足接口。",
        },
        {
            "branch": "persistent flat compensation",
            "route": "ColumnCRT/PDEC or moving-family SAE/Rankin return",
            "status": "registered return, not excluded",
            "meaning": "若真实反例链复现同一补偿相位，应形成可审查的持久相位缺陷。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "PreviousNonrealSimplexTargetImported",
            imported,
            False,
            "上一层把非实零点包压成半类 simplex 的单方向负投影排斥。",
            PREVIOUS_TARGET,
        ),
        row(
            "HalfclassCenteringIdentityClosed",
            True,
            True,
            "每个二次半类内的非实残差严格中心化，和为零。",
            "none",
        ),
        row(
            "ZeroColumnCompensationMassClosed",
            True,
            True,
            "零列强制同半类其它 residue 总正补偿质量等于缺失的主/二次质量。",
            "none",
        ),
        row(
            "SharpOneHoleVarianceFloorClosed",
            True,
            True,
            "尖孔方差地板由 Cauchy 给出且有平铺补偿等号态，因此只是必要条件。",
            "none",
        ),
        row(
            "CapacityOnlySufficiencyRejected",
            True,
            True,
            "纯方差/容量不能排除零列；必须加入真实素数相位或 CRT 持久缺陷机制。",
            NEXT_TARGET,
        ),
        row(
            "ActualPrimeCompensationNonconcentrationProved",
            False,
            False,
            "当前语料还没有证明真实素数诱导的补偿不能近似平铺在同一半类。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只关闭非实分支的补偿恒等式和误出口，不证明行/列命题。",
            "global final inputs remain open",
        ),
    ]


def build_result(max_p: int, top: int) -> dict[str, Any]:
    """构造证书对象。"""
    previous = load_json(DOCS / PREVIOUS)
    rows = build_rows(previous)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR "
        f"(({QUADRATIC_MARGIN_TARGET} OR {EFFECTIVE_NO_SIEGEL}) AND {NEXT_TARGET})) "
        f"AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    diagnostic = finite_diagnostic(max_p, top)
    return {
        "certificate_type": "prime_matrix_nonreal_halfclass_compensation_variance_router",
        "status": "nonreal_halfclass_simplex_sharpened_to_compensation_variance_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "quadratic_margin_still_required": QUADRATIC_MARGIN_TARGET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": diagnostic,
        "halfclass_centering_identity_closed": True,
        "zero_column_compensation_mass_closed": True,
        "sharp_one_hole_variance_floor_closed": True,
        "capacity_only_sufficiency_rejected": True,
        "actual_prime_compensation_nonconcentration_proved": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `NonrealHalfClassSimplexRankOneProjectionExclusionAtP2`。"
            "在每个二次半类内，非实残差恰为 `R_a=(P-1)(theta_a-mu_s)`，所以自动中心化。"
            "零列若出现，不仅要求一个 residue 给出 rank-one 负投影，还要求同半类其余 residue "
            "承担等量正补偿。Cauchy 方差地板是尖锐必要条件，平铺补偿等号态说明纯容量论证不能闭合；"
            "最新硬点压成 `HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Nonreal Half-class Compensation Variance Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"halfclass_centering_identity_closed={fmt_bool(result['halfclass_centering_identity_closed'])}",
        f"zero_column_compensation_mass_closed={fmt_bool(result['zero_column_compensation_mass_closed'])}",
        f"sharp_one_hole_variance_floor_closed={fmt_bool(result['sharp_one_hole_variance_floor_closed'])}",
        f"capacity_only_sufficiency_rejected={fmt_bool(result['capacity_only_sufficiency_rejected'])}",
        f"actual_prime_compensation_nonconcentration_proved={fmt_bool(result['actual_prime_compensation_nonconcentration_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 公式账本",
        "",
        "| item | formula |",
        "| --- | --- |",
    ]
    for item in result["formula_ledger"]:
        lines.append(f"| `{table_cell(item['item'])}` | `{table_cell(item['formula'])}` |")

    lines += [
        "",
        "## 2. 分支压缩",
        "",
        "| branch | route | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["branch_ledger"]:
        lines.append(
            f"| `{table_cell(item['branch'])}` | {table_cell(item['route'])} | "
            f"{table_cell(item['status'])} | {table_cell(item['meaning'])} |"
        )

    lines += [
        "",
        "## 3. 有限诊断",
        "",
        "有限扫描只用于定位补偿/容量误差形态，不作为无限证明输入。",
        "",
        "```text",
        f"min_p={diagnostic['min_p']}",
        f"max_p={diagnostic['max_p']}",
        f"prime_moduli_checked={diagnostic['prime_moduli_checked']}",
        f"halfclass_records_checked={diagnostic['halfclass_records_checked']}",
        f"max_halfclass_centering_abs_error={diagnostic['max_halfclass_centering_abs_error']}",
        f"max_half_mass_identity_abs_error={diagnostic['max_half_mass_identity_abs_error']}",
        f"capacity_false_positive_for_zero_floor_count={diagnostic['capacity_false_positive_for_zero_floor_count']}",
        f"max_actual_negative_to_zero_projection_ratio={diagnostic['max_actual_negative_to_zero_projection_ratio']}",
        f"max_deficit_ratio_modulus={diagnostic['max_deficit_ratio_modulus']}",
        f"max_deficit_ratio_halfclass={diagnostic['max_deficit_ratio_halfclass']}",
        f"max_halfclass_square_to_zero_floor_ratio={diagnostic['max_halfclass_square_to_zero_floor_ratio']}",
        f"max_variance_ratio_modulus={diagnostic['max_variance_ratio_modulus']}",
        f"flat_zero_lift_ratio_range=[{diagnostic['min_flat_zero_lift_ratio']}, {diagnostic['max_flat_zero_lift_ratio']}]",
        "```",
        "",
        "### 3.1 缺孔比例最高记录",
        "",
        "| P | halfclass | min residue | actual/zero | min theta | zero projection | square/floor |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_deficit_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['halfclass']}` | `{item['min_residue']}` | "
            f"`{item['actual_negative_to_zero_projection_ratio']:.12f}` | "
            f"`{item['min_theta']:.12f}` | `{item['required_zero_projection']:.12f}` | "
            f"`{item['halfclass_square_to_zero_floor_ratio']:.12f}` |"
        )

    lines += [
        "",
        "### 3.2 半类方差地板最高记录",
        "",
        "| P | halfclass | square/floor | actual/zero | flat lift | capacity false positive |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_variance_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['halfclass']}` | "
            f"`{item['halfclass_square_to_zero_floor_ratio']:.12f}` | "
            f"`{item['actual_negative_to_zero_projection_ratio']:.12f}` | "
            f"`{item['flat_zero_lift_ratio']:.12f}` | "
            f"`{item['capacity_false_positive_for_zero_floor']}` |"
        )

    lines += [
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )

    lines += [
        "",
        "## 5. 最新活动基",
        "",
        "```text",
        result["latest_strict_activity_basis"],
        "```",
        "",
        "审稿边界：本文件没有证明真实素数补偿质量的非平铺定理、二次半类余量定理或行/列命题；它只关闭非实半类分支中的中心化、补偿、尖锐方差地板和容量误出口。",
        "",
        "## 6. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=1000, help="有限诊断扫描的最大素模数")
    parser.add_argument("--top", type=int, default=12, help="Markdown 中保留的最高风险记录数")
    return parser.parse_args()


def main() -> None:
    """写出路由证书。"""
    args = parse_args()
    result = build_result(args.max_p, args.top)
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "max_actual_negative_to_zero_projection_ratio": result["finite_diagnostic"][
                    "max_actual_negative_to_zero_projection_ratio"
                ],
                "capacity_false_positive_for_zero_floor_count": result["finite_diagnostic"][
                    "capacity_false_positive_for_zero_floor_count"
                ],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
