#!/usr/bin/env python3
"""把 ratio-Fourier 锁压成 Dirichlet 二次扭曲配对角色轨道锁。

用法示例：
  python3 experiments/prime_matrix_halfclass_twist_pair_character_lock_router.py
  python3 experiments/prime_matrix_halfclass_twist_pair_character_lock_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-halfclass-twist-pair-character-lock-router.json

输出：
  data/prime-matrix-halfclass-twist-pair-character-lock-ledger.json
  docs/monograph/prime-matrix-halfclass-twist-pair-character-lock-router.json
  docs/monograph/prime-matrix-halfclass-twist-pair-character-lock-router.md
"""

from __future__ import annotations

import argparse
import cmath
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

OUT_LEDGER = DATA / "prime-matrix-halfclass-twist-pair-character-lock-ledger.json"
OUT_JSON = DOCS / "prime-matrix-halfclass-twist-pair-character-lock-router.json"
OUT_MD = DOCS / "prime-matrix-halfclass-twist-pair-character-lock-router.md"

PREVIOUS = "prime-matrix-halfclass-ratio-fourier-lock-router.json"
COMPENSATION = "prime-matrix-nonreal-halfclass-compensation-variance-router.json"
SIMPLEX = "prime-matrix-nonreal-halfclass-simplex-phase-router.json"
HALFCLASS_MARGIN = "prime-matrix-siegel-quadratic-halfclass-margin-router.json"
STATUS_TABLE = "claim-status-table.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_VIII = ROOT / "docs" / "prime-density-waves-VIII.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"
ACTUAL_LOAD_CONTRACTS = ROOT / "docs" / "monograph" / "three-claims-actual-load-closure-contracts.md"
CRITICAL_LOAD_FRONTIER = ROOT / "docs" / "monograph" / "three-claims-formal-to-actual-critical-load-frontier.md"

PREVIOUS_TARGET = "HalfClassRatioFourierLockExclusionOrColumnCRTPDEC"
NEXT_TARGET = "QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC"
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
    DOCS / COMPENSATION,
    DOCS / SIMPLEX,
    DOCS / HALFCLASS_MARGIN,
    DOCS / STATUS_TABLE,
    FINAL_PROOF_DRAFT,
    PRIME_DENSITY_WAVES_VIII,
    PRIME_DENSITY_WAVES_X,
    ACTUAL_LOAD_CONTRACTS,
    CRITICAL_LOAD_FRONTIER,
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


def primitive_root(p: int) -> int:
    """求素数 p 的一个原根。"""
    factors: list[int] = []
    n = p - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise ValueError(f"no primitive root found for {p}")


def theta_vector_for_modulus(p: int, primes: list[int]) -> list[float]:
    """计算 theta(P^2;P,a) 向量。"""
    theta = [0.0] * p
    cutoff = bisect_right(primes, p * p)
    for ell in primes[:cutoff]:
        if ell == p:
            continue
        theta[ell % p] += math.log(ell)
    return theta


def halfclass_min_puncture_records(p: int, primes: list[int]) -> list[dict[str, Any]]:
    """对两个半类的最小 residue puncture 计算扭曲角色配对锁诊断。"""
    theta = theta_vector_for_modulus(p, primes)
    h = (p - 1) // 2
    g = primitive_root(p)
    # q_positions[t]=g^(2t)，枚举二次剩余子群 Q。
    q_positions = [pow(g, 2 * t, p) for t in range(h)]
    log_index = {pow(g, k, p): k for k in range(p - 1)}
    records: list[dict[str, Any]] = []
    for sign, name in ((1, "quadratic_residue"), (-1, "quadratic_nonresidue")):
        members = [a for a in range(1, p) if legendre_symbol(a, p) == sign]
        a0 = min(members, key=lambda a: (theta[a], a))
        z = theta[a0]
        f_values = [theta[(a0 * u) % p] for u in q_positions]
        total = math.fsum(f_values)
        c = (total - z) / (h - 1)
        target = z - c
        dev2 = math.fsum((value - c) ** 2 for idx, value in enumerate(f_values) if idx != 0)
        # DFT on Q: F_j=sum_t f(g^(2t))*exp(-2*pi*i*j*t/h)。
        lock_defect = 0.0
        max_pair_error = 0.0
        max_pair_error_j = 1
        max_pair_abs = 0.0
        max_pair_abs_j = 1
        for j in range(1, h):
            omega = cmath.exp(-2j * math.pi * j / h)
            power = 1.0 + 0.0j
            coeff = 0.0 + 0.0j
            for value in f_values:
                coeff += value * power
                power *= omega
            defect = abs(coeff - target)
            lock_defect += defect * defect
            if defect > max_pair_error:
                max_pair_error = defect
                max_pair_error_j = j
            if abs(coeff) > max_pair_abs:
                max_pair_abs = abs(coeff)
                max_pair_abs_j = j

        # 用 F* 上的角色配对公式复核：F_j=chi_j(a0)/2*(T_chi_j+s*T_chi_j*chi2)。
        max_pair_formula_error = 0.0
        for j in range(1, h):
            t_chi = 0.0 + 0.0j
            t_twist = 0.0 + 0.0j
            for a in range(1, p):
                exponent = log_index[a]
                chi_bar = cmath.exp(-2j * math.pi * j * exponent / (p - 1))
                t_chi += theta[a] * chi_bar
                t_twist += theta[a] * legendre_symbol(a, p) * chi_bar
            chi_a0 = cmath.exp(2j * math.pi * j * log_index[a0] / (p - 1))
            paired = chi_a0 * (t_chi + sign * t_twist) / 2.0

            omega = cmath.exp(-2j * math.pi * j / h)
            power = 1.0 + 0.0j
            coeff = 0.0 + 0.0j
            for value in f_values:
                coeff += value * power
                power *= omega
            max_pair_formula_error = max(max_pair_formula_error, abs(coeff - paired))

        parseval_error = lock_defect - h * dev2
        scale = max(abs(lock_defect), abs(h * dev2), 1.0)
        records.append(
            {
                "P": p,
                "halfclass": name,
                "legendre_sign": sign,
                "halfclass_size": h,
                "primitive_root": g,
                "puncture_residue": a0,
                "puncture_theta": z,
                "flat_compensator_level": c,
                "lock_target": target,
                "lock_target_abs": abs(target),
                "punctured_flatness_square": dev2,
                "parseval_lock_defect": lock_defect,
                "parseval_identity_abs_error": abs(parseval_error),
                "parseval_identity_relative_error": abs(parseval_error) / scale,
                "max_twist_pair_orbit_error": max_pair_error,
                "max_twist_pair_orbit_error_j": max_pair_error_j,
                "max_twist_pair_abs_projection": max_pair_abs,
                "max_twist_pair_abs_projection_j": max_pair_abs_j,
                "max_twist_pair_formula_abs_error": max_pair_formula_error,
                "relative_lock_defect_to_target_energy": lock_defect / ((h - 1) * target * target)
                if target
                else None,
            }
        )
    return records


def finite_diagnostic(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """有限扫描只定位配对角色锁误差，不作为无限证明输入。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records: list[dict[str, Any]] = []
    for p in prime_moduli:
        records.extend(halfclass_min_puncture_records(p, primes))

    by_relative_lock = sorted(
        records,
        key=lambda item: (item["relative_lock_defect_to_target_energy"] or float("inf"), item["P"]),
    )
    by_target = sorted(records, key=lambda item: (item["lock_target_abs"], item["P"]), reverse=True)
    return {
        "min_p": min_p,
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "min_residue_halfclass_records_checked": len(records),
        "max_parseval_identity_relative_error": max(
            (item["parseval_identity_relative_error"] for item in records), default=0.0
        ),
        "max_twist_pair_formula_abs_error": max(
            (item["max_twist_pair_formula_abs_error"] for item in records), default=0.0
        ),
        "min_relative_lock_defect_to_target_energy": (
            by_relative_lock[0]["relative_lock_defect_to_target_energy"] if by_relative_lock else None
        ),
        "min_relative_lock_defect_modulus": by_relative_lock[0]["P"] if by_relative_lock else None,
        "max_lock_target_abs": by_target[0]["lock_target_abs"] if by_target else None,
        "max_lock_target_abs_modulus": by_target[0]["P"] if by_target else None,
        "top_near_orbit_lock_records": by_relative_lock[:top],
        "top_lock_target_records": by_target[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录扭曲配对角色轨道锁公式。"""
    return [
        {
            "item": "subgroup character extension",
            "formula": "every nontrivial psi on Q has two extensions chi and chi*chi_2 to F_P^*",
        },
        {
            "item": "paired projection",
            "formula": "F_psi(a0)=chi(a0)*(T_chi+s*T_{chi chi_2})/2 for a0 in H_s",
        },
        {
            "item": "orbit lock",
            "formula": "flat compensation forces chi(a0)*(T_chi+s*T_{chi chi_2})/2 = theta_{a0}-c_{a0} for every psi!=1",
        },
        {
            "item": "explicit zero-packet form",
            "formula": "each T_chi is a signed explicit-formula zero packet plus controlled finite terms",
        },
        {
            "item": "Parseval lock defect",
            "formula": "sum_{psi!=1}|chi(a0)*(T_chi+s*T_{chi chi_2})/2-(theta_{a0}-c_{a0})|^2 = h*punctured_flatness",
        },
        {
            "item": "new hardpoint",
            "formula": "exclude persistent quadratic-twist pair orbit lock, or register ColumnCRT/PDEC/moving-family",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": PREVIOUS_TARGET,
            "route": NEXT_TARGET,
            "status": "sharpened but open",
            "meaning": "ratio-Fourier 全频率锁被改写为每一对二次扭曲 Dirichlet 角色的同一轨道锁。",
        },
        {
            "branch": "Q-Fourier coefficients",
            "route": "paired character projections T_chi+s*T_{chi chi_2}",
            "status": "closed as algebraic identity",
            "meaning": "Q 子群频率没有引入新黑箱；它们正是模 P 角色按二次扭曲配对后的投影。",
        },
        {
            "branch": "persistent orbit lock",
            "route": "explicit zero-packet phase coherence across all twist-pairs",
            "status": "not proved in corpus",
            "meaning": "若反例持久，则不是单个角色异常，而是全部配对角色同步相位。",
        },
        {
            "branch": NEXT_TARGET,
            "route": "exclude all-pair orbit lock or route to ColumnCRT/PDEC/moving-family",
            "status": "not proved in corpus",
            "meaning": "这是当前非实 AP 分支的最新最窄接口。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "PreviousRatioFourierTargetImported",
            imported,
            False,
            "上一层把补偿平铺压成二次剩余子群上的全频率锁。",
            PREVIOUS_TARGET,
        ),
        row(
            "SubgroupCharacterExtensionClosed",
            True,
            True,
            "Q 上每个非平凡频率都有两条 Dirichlet 扩张，彼此相差二次角色。",
            "none",
        ),
        row(
            "TwistPairProjectionIdentityClosed",
            True,
            True,
            "Q-Fourier 系数精确等于 T_chi 与 T_chi chi2 的半类配对投影。",
            "none",
        ),
        row(
            "OrbitLockReformulationClosed",
            True,
            True,
            "平铺补偿等价于全部二次扭曲角色对落在同一 a0 相位轨道。",
            "none",
        ),
        row(
            "SingleCharacterOrCapacitySufficiencyRejected",
            True,
            True,
            "一个角色异常或总能量不够；持久反例需要全配对角色同步锁。",
            NEXT_TARGET,
        ),
        row(
            "PersistentTwistPairOrbitLockExcluded",
            False,
            False,
            "当前语料尚未排斥全部二次扭曲角色对的持久同步轨道锁。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只完成角色配对化，不证明行/列命题。",
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
        "certificate_type": "prime_matrix_halfclass_twist_pair_character_lock_router",
        "status": "ratio_fourier_lock_routed_to_quadratic_twist_pair_character_orbit_lock_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "quadratic_margin_still_required": QUADRATIC_MARGIN_TARGET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": diagnostic,
        "subgroup_character_extension_closed": True,
        "twist_pair_projection_identity_closed": True,
        "orbit_lock_reformulation_closed": True,
        "single_character_or_capacity_sufficiency_rejected": True,
        "persistent_twist_pair_orbit_lock_excluded": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `HalfClassRatioFourierLockExclusionOrColumnCRTPDEC`。"
            "二次剩余子群 Q 上的每个非平凡频率都对应模 P 的一对二次扭曲 Dirichlet 角色 "
            "`chi, chi*chi_2`。平铺补偿要求 `chi(a0)*(T_chi+s*T_{chi chi_2})/2` "
            "对所有配对角色同时等于同一个实目标 `theta_a0-c_a0`。"
            "因此最新硬点压成 `QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Half-class Twist-pair Character Lock Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"subgroup_character_extension_closed={fmt_bool(result['subgroup_character_extension_closed'])}",
        f"twist_pair_projection_identity_closed={fmt_bool(result['twist_pair_projection_identity_closed'])}",
        f"orbit_lock_reformulation_closed={fmt_bool(result['orbit_lock_reformulation_closed'])}",
        f"single_character_or_capacity_sufficiency_rejected={fmt_bool(result['single_character_or_capacity_sufficiency_rejected'])}",
        f"persistent_twist_pair_orbit_lock_excluded={fmt_bool(result['persistent_twist_pair_orbit_lock_excluded'])}",
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
        "有限扫描只用于定位配对角色锁误差，不作为无限证明输入。",
        "",
        "```text",
        f"min_p={diagnostic['min_p']}",
        f"max_p={diagnostic['max_p']}",
        f"prime_moduli_checked={diagnostic['prime_moduli_checked']}",
        f"min_residue_halfclass_records_checked={diagnostic['min_residue_halfclass_records_checked']}",
        f"max_parseval_identity_relative_error={diagnostic['max_parseval_identity_relative_error']}",
        f"max_twist_pair_formula_abs_error={diagnostic['max_twist_pair_formula_abs_error']}",
        f"min_relative_lock_defect_to_target_energy={diagnostic['min_relative_lock_defect_to_target_energy']}",
        f"min_relative_lock_defect_modulus={diagnostic['min_relative_lock_defect_modulus']}",
        f"max_lock_target_abs={diagnostic['max_lock_target_abs']}",
        f"max_lock_target_abs_modulus={diagnostic['max_lock_target_abs_modulus']}",
        "```",
        "",
        "### 3.1 最接近配对轨道锁的最小 residue 记录",
        "",
        "| P | halfclass | puncture | target | rel lock defect | max pair error | max pair j | formula err |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_near_orbit_lock_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['halfclass']}` | `{item['puncture_residue']}` | "
            f"`{item['lock_target']:.12f}` | "
            f"`{item['relative_lock_defect_to_target_energy']:.12f}` | "
            f"`{item['max_twist_pair_orbit_error']:.12f}` | "
            f"`{item['max_twist_pair_orbit_error_j']}` | "
            f"`{item['max_twist_pair_formula_abs_error']:.3e}` |"
        )

    lines += [
        "",
        "### 3.2 锁目标绝对值最高记录",
        "",
        "| P | halfclass | puncture | |target| | target | max pair abs | max pair abs j |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_lock_target_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['halfclass']}` | `{item['puncture_residue']}` | "
            f"`{item['lock_target_abs']:.12f}` | `{item['lock_target']:.12f}` | "
            f"`{item['max_twist_pair_abs_projection']:.12f}` | `{item['max_twist_pair_abs_projection_j']}` |"
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
        "审稿边界：本文件没有证明持久二次扭曲配对角色轨道锁不可能，也没有排斥相应 ColumnCRT/PDEC/moving-family 出口；它只把 ratio-Fourier 锁接回标准 Dirichlet 角色投影语言。",
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
                "min_relative_lock_defect_to_target_energy": result["finite_diagnostic"][
                    "min_relative_lock_defect_to_target_energy"
                ],
                "max_twist_pair_formula_abs_error": result["finite_diagnostic"][
                    "max_twist_pair_formula_abs_error"
                ],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
