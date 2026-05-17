#!/usr/bin/env python3
"""把半类补偿平铺硬点压成二次剩余 ratio-Fourier 锁定。

用法示例：
  python3 experiments/prime_matrix_halfclass_ratio_fourier_lock_router.py
  python3 experiments/prime_matrix_halfclass_ratio_fourier_lock_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-halfclass-ratio-fourier-lock-router.json

输出：
  data/prime-matrix-halfclass-ratio-fourier-lock-ledger.json
  docs/monograph/prime-matrix-halfclass-ratio-fourier-lock-router.json
  docs/monograph/prime-matrix-halfclass-ratio-fourier-lock-router.md
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

OUT_LEDGER = DATA / "prime-matrix-halfclass-ratio-fourier-lock-ledger.json"
OUT_JSON = DOCS / "prime-matrix-halfclass-ratio-fourier-lock-router.json"
OUT_MD = DOCS / "prime-matrix-halfclass-ratio-fourier-lock-router.md"

PREVIOUS = "prime-matrix-nonreal-halfclass-compensation-variance-router.json"
SIMPLEX = "prime-matrix-nonreal-halfclass-simplex-phase-router.json"
HALFCLASS_MARGIN = "prime-matrix-siegel-quadratic-halfclass-margin-router.json"
STATUS_TABLE = "claim-status-table.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_VIII = ROOT / "docs" / "prime-density-waves-VIII.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

PREVIOUS_TARGET = "HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC"
NEXT_TARGET = "HalfClassRatioFourierLockExclusionOrColumnCRTPDEC"
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
    DOCS / SIMPLEX,
    DOCS / HALFCLASS_MARGIN,
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


def halfclass_puncture_records(p: int, primes: list[int]) -> list[dict[str, Any]]:
    """扫描每个半类每个可能缺孔，计算 punctured flatness 与恒等式误差。"""
    theta = theta_vector_for_modulus(p, primes)
    h = (p - 1) // 2
    records: list[dict[str, Any]] = []
    for sign, name in ((1, "quadratic_residue"), (-1, "quadratic_nonresidue")):
        members = [a for a in range(1, p) if legendre_symbol(a, p) == sign]
        total = math.fsum(theta[a] for a in members)
        sumsq = math.fsum(theta[a] * theta[a] for a in members)
        mu = total / h
        min_residue = min(members, key=lambda a: (theta[a], a))
        for puncture in members:
            z = theta[puncture]
            c = (total - z) / (h - 1)
            # dev2 是去掉 puncture 后，剩余列相对最优平铺补偿常数 c 的二次偏离。
            dev2 = (sumsq - z * z) - ((total - z) * (total - z)) / (h - 1)
            if dev2 < 0 and abs(dev2) < 1e-8:
                dev2 = 0.0
            max_abs_dev = max(abs(theta[a] - c) for a in members if a != puncture)
            denominator_energy = max(sumsq - z * z, 1e-300)
            denominator_flat = max(c * c * (h - 1), 1e-300)
            relative_energy = dev2 / denominator_energy
            relative_flat = dev2 / denominator_flat
            residual_square = (p - 1) * (p - 1) * math.fsum((theta[a] - mu) ** 2 for a in members)
            one_point_floor = (p - 1) * (p - 1) * (z - mu) * (z - mu) * h / (h - 1)
            identity_error = residual_square - one_point_floor - (p - 1) * (p - 1) * dev2
            identity_scale = max(abs(residual_square), abs(one_point_floor), abs((p - 1) * (p - 1) * dev2), 1.0)
            records.append(
                {
                    "P": p,
                    "halfclass": name,
                    "legendre_sign": sign,
                    "halfclass_size": h,
                    "puncture_residue": puncture,
                    "puncture_theta": z,
                    "puncture_is_min_residue": puncture == min_residue,
                    "halfclass_total_theta": total,
                    "halfclass_mean_theta": mu,
                    "punctured_flat_compensator_level": c,
                    "punctured_flatness_square": dev2,
                    "punctured_flatness_relative_to_energy": relative_energy,
                    "punctured_flatness_relative_to_flat_level": relative_flat,
                    "max_abs_deviation_from_flat_compensator": max_abs_dev,
                    "max_abs_deviation_to_flat_level_ratio": max_abs_dev / abs(c) if c else None,
                    "one_point_variance_floor": one_point_floor,
                    "halfclass_residual_square": residual_square,
                    "one_point_variance_excess_identity_error": identity_error,
                    "one_point_variance_excess_identity_relative_error": abs(identity_error) / identity_scale,
                    "fourier_lock_parseval_square": h * dev2,
                    "nontrivial_frequency_lock_target": z - c,
                }
            )
    return records


def finite_diagnostic(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """有限扫描只定位 ratio-Fourier 锁误差，不作为无限证明输入。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records: list[dict[str, Any]] = []
    for p in prime_moduli:
        records.extend(halfclass_puncture_records(p, primes))

    by_energy_flatness = sorted(
        records,
        key=lambda item: (item["punctured_flatness_relative_to_energy"], item["P"]),
    )
    by_flat_level = sorted(
        records,
        key=lambda item: (item["punctured_flatness_relative_to_flat_level"], item["P"]),
    )
    min_residue_records = [item for item in records if item["puncture_is_min_residue"]]
    by_min_residue_flatness = sorted(
        min_residue_records,
        key=lambda item: (item["punctured_flatness_relative_to_energy"], item["P"]),
    )
    thresholds = [1e-3, 1e-2, 5e-2, 1e-1]
    max_identity_error = max((abs(item["one_point_variance_excess_identity_error"]) for item in records), default=0.0)
    max_identity_relative_error = max(
        (item["one_point_variance_excess_identity_relative_error"] for item in records), default=0.0
    )
    return {
        "min_p": min_p,
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "puncture_records_checked": len(records),
        "min_residue_puncture_records_checked": len(min_residue_records),
        "max_one_point_variance_excess_identity_abs_error": max_identity_error,
        "near_flat_counts_relative_to_energy": {
            str(threshold): sum(
                1 for item in records if item["punctured_flatness_relative_to_energy"] <= threshold
            )
            for threshold in thresholds
        },
        "near_flat_min_residue_counts_relative_to_energy": {
            str(threshold): sum(
                1 for item in min_residue_records if item["punctured_flatness_relative_to_energy"] <= threshold
            )
            for threshold in thresholds
        },
        "min_punctured_flatness_relative_to_energy": (
            by_energy_flatness[0]["punctured_flatness_relative_to_energy"] if by_energy_flatness else None
        ),
        "max_one_point_variance_excess_identity_relative_error": max_identity_relative_error,
        "min_punctured_flatness_relative_to_energy_modulus": (
            by_energy_flatness[0]["P"] if by_energy_flatness else None
        ),
        "min_punctured_flatness_relative_to_flat_level": (
            by_flat_level[0]["punctured_flatness_relative_to_flat_level"] if by_flat_level else None
        ),
        "min_flat_level_modulus": by_flat_level[0]["P"] if by_flat_level else None,
        "min_residue_best_flatness_relative_to_energy": (
            by_min_residue_flatness[0]["punctured_flatness_relative_to_energy"]
            if by_min_residue_flatness
            else None
        ),
        "min_residue_best_flatness_modulus": by_min_residue_flatness[0]["P"] if by_min_residue_flatness else None,
        "top_near_flat_records": by_energy_flatness[:top],
        "top_near_flat_min_residue_records": by_min_residue_flatness[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录 ratio-Fourier 锁定公式。"""
    return [
        {
            "item": "ratio normalization",
            "formula": "Q=quadratic residues mod P; f_{a0}(u)=theta(P^2;P,a0*u), u in Q",
        },
        {
            "item": "punctured flat compensator",
            "formula": "c_{a0}=(sum_{u!=1} f_{a0}(u))/(h-1), h=(P-1)/2",
        },
        {
            "item": "one-point variance excess identity",
            "formula": "sum R_a^2 - (P-1)^2(theta_{a0}-mu)^2*h/(h-1) = (P-1)^2*sum_{u!=1}(f_{a0}(u)-c_{a0})^2",
        },
        {
            "item": "flat zero compensator",
            "formula": "theta_{a0}=0 and zero excess iff f_{a0}(u)=c_{a0} for every u!=1",
        },
        {
            "item": "subgroup Fourier lock",
            "formula": "flat profile iff every nontrivial Fourier coefficient on Q equals theta_{a0}-c_{a0}",
        },
        {
            "item": "Parseval lock defect",
            "formula": "sum_{psi!=1} |F_psi-(theta_{a0}-c_{a0})|^2 = h*sum_{u!=1}(f_{a0}(u)-c_{a0})^2",
        },
        {
            "item": "new hardpoint",
            "formula": "exclude persistent all-frequency ratio lock, or register it as ColumnCRT/PDEC/moving-family",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": PREVIOUS_TARGET,
            "route": NEXT_TARGET,
            "status": "sharpened but open",
            "meaning": "补偿质量非平铺被改写为二次剩余 ratio 坐标上的全非平凡频率同相锁定排斥。",
        },
        {
            "branch": "near-flat compensation",
            "route": "all nontrivial Fourier coefficients on the QR subgroup nearly equal",
            "status": "closed as equivalent structure",
            "meaning": "这不是随机噪声，而是高度刚性的乘法相位锁。",
        },
        {
            "branch": "non-flat compensation",
            "route": "positive Parseval lock defect / named compensation dispersion packet",
            "status": "registered return, not excluded",
            "meaning": "非平铺本身也不是矛盾；它必须接入 PDEC/SAE/Rankin 或实际源熵预算。",
        },
        {
            "branch": NEXT_TARGET,
            "route": "exclude persistent ratio-Fourier lock or route every persistent lock to ColumnCRT/PDEC",
            "status": "not proved in corpus",
            "meaning": "这是半类补偿分支的最新最窄自足接口。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "PreviousCompensationTargetImported",
            imported,
            False,
            "上一层把非实分支压成真实补偿质量非平铺或 ColumnCRT/PDEC。",
            PREVIOUS_TARGET,
        ),
        row(
            "RatioNormalizationClosed",
            True,
            True,
            "固定假想缺孔 a0 后，同半类被 a0^{-1} 归一化为二次剩余子群 Q。",
            "none",
        ),
        row(
            "OnePointVarianceExcessIdentityClosed",
            True,
            True,
            "半类方差超过单点地板的部分，精确等于 punctured flatness 二次量。",
            "none",
        ),
        row(
            "FlatCompensatorFourierLockEquivalenceClosed",
            True,
            True,
            "平铺补偿等价于 Q 上所有非平凡 Fourier 系数同时锁到同一值。",
            "none",
        ),
        row(
            "CapacityOrVarianceOnlySufficiencyRejected",
            True,
            True,
            "方差超额只测量非平铺；零超额只给 Fourier 锁，都不是自动矛盾。",
            NEXT_TARGET,
        ),
        row(
            "PersistentRatioFourierLockExcluded",
            False,
            False,
            "当前语料尚未排斥真实素数向量的持久 ratio-Fourier 锁。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只关闭补偿平铺的 Fourier 等价与误出口，不证明行/列命题。",
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
        "certificate_type": "prime_matrix_halfclass_ratio_fourier_lock_router",
        "status": "halfclass_compensation_routed_to_ratio_fourier_lock_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "quadratic_margin_still_required": QUADRATIC_MARGIN_TARGET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": diagnostic,
        "ratio_normalization_closed": True,
        "one_point_variance_excess_identity_closed": True,
        "flat_compensator_fourier_lock_equivalence_closed": True,
        "capacity_or_variance_only_sufficiency_rejected": True,
        "persistent_ratio_fourier_lock_excluded": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC`。"
            "固定假想缺孔 `a0` 后，同半类列可由二次剩余子群 ratio `u=a0^{-1}a` 统一参数化。"
            "半类方差超过单点地板的部分，精确等于非孔 ratio 列偏离最佳平铺补偿的二次量；"
            "而平铺补偿又等价于二次剩余子群上所有非平凡 Fourier 系数同时锁到同一值。"
            "因此最新硬点压成 `HalfClassRatioFourierLockExclusionOrColumnCRTPDEC`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Half-class Ratio Fourier Lock Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"ratio_normalization_closed={fmt_bool(result['ratio_normalization_closed'])}",
        f"one_point_variance_excess_identity_closed={fmt_bool(result['one_point_variance_excess_identity_closed'])}",
        f"flat_compensator_fourier_lock_equivalence_closed={fmt_bool(result['flat_compensator_fourier_lock_equivalence_closed'])}",
        f"capacity_or_variance_only_sufficiency_rejected={fmt_bool(result['capacity_or_variance_only_sufficiency_rejected'])}",
        f"persistent_ratio_fourier_lock_excluded={fmt_bool(result['persistent_ratio_fourier_lock_excluded'])}",
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
        "有限扫描只用于定位 ratio-Fourier 锁误差，不作为无限证明输入。",
        "",
        "```text",
        f"min_p={diagnostic['min_p']}",
        f"max_p={diagnostic['max_p']}",
        f"prime_moduli_checked={diagnostic['prime_moduli_checked']}",
        f"puncture_records_checked={diagnostic['puncture_records_checked']}",
        f"min_residue_puncture_records_checked={diagnostic['min_residue_puncture_records_checked']}",
        f"max_one_point_variance_excess_identity_abs_error={diagnostic['max_one_point_variance_excess_identity_abs_error']}",
        f"max_one_point_variance_excess_identity_relative_error={diagnostic['max_one_point_variance_excess_identity_relative_error']}",
        f"near_flat_counts_relative_to_energy={diagnostic['near_flat_counts_relative_to_energy']}",
        f"near_flat_min_residue_counts_relative_to_energy={diagnostic['near_flat_min_residue_counts_relative_to_energy']}",
        f"min_punctured_flatness_relative_to_energy={diagnostic['min_punctured_flatness_relative_to_energy']}",
        f"min_punctured_flatness_relative_to_energy_modulus={diagnostic['min_punctured_flatness_relative_to_energy_modulus']}",
        f"min_residue_best_flatness_relative_to_energy={diagnostic['min_residue_best_flatness_relative_to_energy']}",
        f"min_residue_best_flatness_modulus={diagnostic['min_residue_best_flatness_modulus']}",
        "```",
        "",
        "### 3.1 全部 puncture 中最接近平铺的记录",
        "",
        "| P | halfclass | puncture | is min | rel energy | rel flat | theta puncture | flat level | max dev/flat |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_near_flat_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['halfclass']}` | `{item['puncture_residue']}` | "
            f"`{item['puncture_is_min_residue']}` | "
            f"`{item['punctured_flatness_relative_to_energy']:.12f}` | "
            f"`{item['punctured_flatness_relative_to_flat_level']:.12f}` | "
            f"`{item['puncture_theta']:.12f}` | "
            f"`{item['punctured_flat_compensator_level']:.12f}` | "
            f"`{item['max_abs_deviation_to_flat_level_ratio']:.12f}` |"
        )

    lines += [
        "",
        "### 3.2 最小 residue puncture 中最接近平铺的记录",
        "",
        "| P | halfclass | puncture | rel energy | rel flat | theta puncture | flat level | max dev/flat |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_near_flat_min_residue_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['halfclass']}` | `{item['puncture_residue']}` | "
            f"`{item['punctured_flatness_relative_to_energy']:.12f}` | "
            f"`{item['punctured_flatness_relative_to_flat_level']:.12f}` | "
            f"`{item['puncture_theta']:.12f}` | "
            f"`{item['punctured_flat_compensator_level']:.12f}` | "
            f"`{item['max_abs_deviation_to_flat_level_ratio']:.12f}` |"
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
        "审稿边界：本文件没有证明持久 ratio-Fourier 锁不可能，也没有排斥相应 ColumnCRT/PDEC/moving-family 出口；它只把半类补偿平铺和非平铺的结构边界严格化。",
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
                "min_punctured_flatness_relative_to_energy": result["finite_diagnostic"][
                    "min_punctured_flatness_relative_to_energy"
                ],
                "min_residue_best_flatness_relative_to_energy": result["finite_diagnostic"][
                    "min_residue_best_flatness_relative_to_energy"
                ],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
