#!/usr/bin/env python3
"""把 Linnik=2 零列缺陷路由到非主角色相位障碍。

用法示例：
  python3 experiments/prime_matrix_linnik2_nonprincipal_character_obstruction_router.py
  python3 experiments/prime_matrix_linnik2_nonprincipal_character_obstruction_router.py --max-p 3000 --top 12
  python3 -m json.tool docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.json

输出：
  data/prime-matrix-linnik2-nonprincipal-character-obstruction-ledger.json
  docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.json
  docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.md
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

OUT_LEDGER = DATA / "prime-matrix-linnik2-nonprincipal-character-obstruction-ledger.json"
OUT_JSON = DOCS / "prime-matrix-linnik2-nonprincipal-character-obstruction-router.json"
OUT_MD = DOCS / "prime-matrix-linnik2-nonprincipal-character-obstruction-router.md"

LINNIK2_BARRIER = "prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_V = ROOT / "docs" / "prime-density-waves-V.md"
PRIME_DENSITY_WAVES_VIII = ROOT / "docs" / "prime-density-waves-VIII.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
L2_AP = "PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2"
ZERO_COLUMN = "Linnik2ZeroColumnDefect"
NONPRINCIPAL_SPIKE = "NonprincipalCharacterEnergySpikeForLinnik2Defect"
POINTWISE_PROJECTION_BOUND = "PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / LINNIK2_BARRIER,
    FINAL_PROOF_DRAFT,
    PRIME_DENSITY_WAVES_V,
    PRIME_DENSITY_WAVES_VIII,
    PRIME_DENSITY_WAVES_X,
]


def sieve(limit: int) -> tuple[bytearray, list[int]]:
    """返回素数布尔表和素数表。"""
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


def theta_profile_for_modulus(p: int, primes: list[int]) -> dict[str, Any]:
    """计算 theta 权的 residue profile 与非主能量指标。"""
    limit = p * p
    cutoff = bisect_right(primes, limit)
    theta = [0.0] * p
    for ell in primes[:cutoff]:
        if ell == p:
            continue
        theta[ell % p] += math.log(ell)

    nonzero = theta[1:]
    theta0 = sum(nonzero)
    average = theta0 / (p - 1)
    min_residue = min(range(1, p), key=lambda a: theta[a])
    min_theta = theta[min_residue]
    deficit = average - min_theta
    deficit_ratio = deficit / average if average else 0.0
    zero_residues = [a for a in range(1, p) if theta[a] == 0.0]

    centered_l2 = sum((value - average) ** 2 for value in nonzero)
    nonprincipal_energy = (p - 1) * centered_l2
    zero_defect_energy_floor = (theta0 * theta0) / (p - 2) if p > 2 else None
    max_character_floor = theta0 / (p - 2) if p > 2 else None
    energy_floor_ratio = (
        nonprincipal_energy / zero_defect_energy_floor
        if zero_defect_energy_floor and zero_defect_energy_floor > 0
        else None
    )

    return {
        "P": p,
        "theta0": theta0,
        "average_theta_per_nonzero_class": average,
        "min_theta_residue": min_residue,
        "min_theta": min_theta,
        "max_negative_deficit": deficit,
        "max_negative_deficit_ratio_to_average": deficit_ratio,
        "zero_theta_residue_count": len(zero_residues),
        "zero_theta_residue_sample": zero_residues[:12],
        "nonprincipal_character_energy": nonprincipal_energy,
        "zero_defect_nonprincipal_energy_floor": zero_defect_energy_floor,
        "energy_to_zero_defect_floor_ratio": energy_floor_ratio,
        "zero_defect_max_character_floor": max_character_floor,
    }


def sample_character_obstruction(max_p: int, top: int) -> dict[str, Any]:
    """扫描有限样本中的最大负 theta 缺口。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if 3 <= p <= max_p]
    records = [theta_profile_for_modulus(p, primes) for p in prime_moduli]
    records.sort(
        key=lambda item: (
            item["zero_theta_residue_count"],
            item["max_negative_deficit_ratio_to_average"],
            item["P"],
        ),
        reverse=True,
    )
    worst = records[0] if records else {}
    return {
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "zero_theta_residue_total": sum(item["zero_theta_residue_count"] for item in records),
        "worst_deficit_ratio": worst.get("max_negative_deficit_ratio_to_average"),
        "worst_deficit_modulus": worst.get("P"),
        "top_records": records[:top],
    }


def exact_character_chain() -> list[dict[str, str]]:
    """列出 Linnik=2 缺陷到非主角色障碍的精确链。"""
    return [
        {
            "from": L2_AP,
            "to": f"not {ZERO_COLUMN}",
        },
        {
            "from": ZERO_COLUMN,
            "to": "theta_a(P)=0 for some a in F_P^*",
        },
        {
            "from": "theta_a=(T_0+N_a)/(P-1)",
            "to": "N_a=(P-1)theta_a-T_0",
        },
        {
            "from": "theta_a=0",
            "to": "N_a=-T_0 exact negative nonprincipal projection",
        },
        {
            "from": "N_a=-T_0",
            "to": "sum_{chi!=chi0}|T_chi|^2 >= T_0^2/(P-2)",
        },
        {
            "from": "exclude zero column",
            "to": POINTWISE_PROJECTION_BOUND,
        },
    ]


def formula_ledger() -> dict[str, str]:
    """登记精确公式，避免把启发式写成证明。"""
    return {
        "theta_class": "theta_a(P)=sum_{ell<=P^2, ell prime, ell=a mod P} log ell",
        "character_sum": "T_chi(P)=sum_{a in F_P^*} chi(a) theta_a(P)=sum_{ell<=P^2, ell!=P} chi(ell) log ell",
        "orthogonality": "theta_a(P)=(1/(P-1))*sum_chi conjugate(chi(a))*T_chi(P)",
        "principal_mass": "T_0(P)=sum_{a in F_P^*} theta_a(P)",
        "nonprincipal_projection": "N_a(P)=sum_{chi!=chi0} conjugate(chi(a))*T_chi(P)=(P-1)theta_a(P)-T_0(P)",
        "zero_column_implication": "theta_a(P)=0 => N_a(P)=-T_0(P)",
        "energy_floor": "theta_a(P)=0 => sum_{chi!=chi0}|T_chi(P)|^2 >= T_0(P)^2/(P-2)",
        "pointwise_sufficient_exclusion": "if N_a(P)>-T_0(P) for every a, then every nonzero column has a prime <=P^2",
    }


def build_rows(linnik2_barrier: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    l2_imported = (
        linnik2_barrier.get("next_direct_attack_target") == L2_AP
        and linnik2_barrier.get("pointwise_linnik2_ap_theorem_proved") is False
    )
    return [
        row(
            "Linnik2BarrierImported",
            l2_imported,
            False,
            "上一层已把局部化 P-CRT 列转移压成 prime-modulus 点态 AP/Linnik=2 屏障。",
            L2_AP,
        ),
        row(
            "ThetaCharacterExpansionExact",
            True,
            True,
            "对 F_P^* 上的 theta residue vector 使用 Dirichlet 角色正交展开，公式完全有限且不依赖渐近。",
            "none",
        ),
        row(
            "ZeroColumnForcesNegativeProjection",
            True,
            True,
            "若某非零列在 P^2 前无素数，则该列非主角色投影必须精确等于 -T_0。",
            NONPRINCIPAL_SPIKE,
        ),
        row(
            "ZeroColumnForcesEnergySpike",
            True,
            True,
            "由 Cauchy，零列缺陷迫使非主角色总能量至少达到 T_0^2/(P-2)，且至少一个非主角色大小达到 T_0/(P-2)。",
            NONPRINCIPAL_SPIKE,
        ),
        row(
            "AverageCRTStillInsufficient",
            True,
            True,
            "完整 CRT 均匀性对应 principal mass；零列排斥需要控制每个 a 的非主投影负相位。",
            POINTWISE_PROJECTION_BOUND,
        ),
        row(
            "NonprincipalSpikeContradictionFound",
            False,
            False,
            "当前语料没有证明所有非主投影都严格高于 -T_0，也没有给出排斥 Siegel/大偏差相位的无条件点态界。",
            POINTWISE_PROJECTION_BOUND,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 Linnik=2 缺陷转写为精确角色相位/能量障碍，尚未排斥该障碍。",
            f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR {POINTWISE_PROJECTION_BOUND}) AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result(max_p: int, top: int) -> dict[str, Any]:
    """构造非主角色障碍证书。"""
    linnik2_barrier = load_json(DOCS / LINNIK2_BARRIER)
    sample = sample_character_obstruction(max_p, top)
    rows = build_rows(linnik2_barrier)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR {POINTWISE_PROJECTION_BOUND}) "
        f"AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )

    return {
        "certificate_type": "prime_matrix_linnik2_nonprincipal_character_obstruction_router",
        "status": "linnik2_zero_column_reduced_to_nonprincipal_character_projection_barrier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "theta_character_expansion_exact": True,
        "zero_column_forces_negative_projection": True,
        "zero_column_forces_energy_spike": True,
        "nonprincipal_spike_contradiction_found": False,
        "pointwise_projection_bound_proved": False,
        "pointwise_linnik2_ap_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": L2_AP,
        "next_direct_attack_target": POINTWISE_PROJECTION_BOUND,
        "structural_fallback_target": f"{PDEC_SCOPE_ATOM}_OR_{SIGNED_PAYLOAD_ATOM}",
        "latest_strict_activity_basis": latest_basis,
        "formula_ledger": formula_ledger(),
        "exact_character_chain": exact_character_chain(),
        "sample_character_obstruction": sample,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Linnik=2 零列缺陷可以精确改写为非主 Dirichlet 角色的负相位投影障碍："
            "若某个非零 residue class `a mod P` 在 `P^2` 前没有素数，则 theta 权 `theta_a(P)=0`，"
            "从而非主投影 `N_a(P)` 必须等于 `-T_0(P)`。这迫使非主角色能量达到显式下界，"
            "但该能量/相位尖峰本身并未在当前语料中被排斥。因此本步把点态 AP 屏障压成 "
            "`PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2`，不是行/列命题的无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    sample = result["sample_character_obstruction"]
    lines = [
        "# Prime Matrix Linnik=2 非主角色障碍路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"theta_character_expansion_exact={fmt_bool(result['theta_character_expansion_exact'])}",
        f"zero_column_forces_negative_projection={fmt_bool(result['zero_column_forces_negative_projection'])}",
        f"zero_column_forces_energy_spike={fmt_bool(result['zero_column_forces_energy_spike'])}",
        f"pointwise_projection_bound_proved={fmt_bool(result['pointwise_projection_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 精确公式账本",
        "",
        "| item | formula |",
        "| --- | --- |",
    ]
    for key, value in result["formula_ledger"].items():
        lines.append(f"| `{key}` | `{table_cell(value)}` |")

    lines += [
        "",
        "## 2. 精确路由链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["exact_character_chain"]:
        lines.append(f"| `{table_cell(item['from'])}` | `{table_cell(item['to'])}` |")

    lines += [
        "",
        f"## 3. 有限 theta 样本（P <= {sample['max_p']}）",
        "",
        f"- 检查素数模数：`{sample['prime_moduli_checked']}`。",
        f"- theta 零剩余类总数：`{sample['zero_theta_residue_total']}`。",
        f"- 最大负缺口比例：`{sample['worst_deficit_ratio']:.6f}`，出现于 `P={sample['worst_deficit_modulus']}`。",
        "",
        "| P | min residue | min theta | avg theta | deficit/avg | nonprincipal energy / zero floor | zero classes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in sample["top_records"]:
        energy_ratio = item["energy_to_zero_defect_floor_ratio"]
        lines.append(
            "| {P} | {min_theta_residue} | {min_theta:.6f} | {average_theta_per_nonzero_class:.6f} | {max_negative_deficit_ratio_to_average:.6f} | {energy_ratio:.6f} | {zero_theta_residue_count} |".format(
                energy_ratio=energy_ratio if energy_ratio is not None else float("nan"),
                **item,
            )
        )

    lines += [
        "",
        "样本只说明当前有限范围内没有 theta 零列；证明不依赖经验无反例。",
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
        "审稿边界：本文件没有证明点态 AP/Linnik=2 定理，也没有证明排斥所有非主角色负相位投影的无条件界；它只给出有限群角色正交下的精确障碍形式。",
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
    parser.add_argument("--max-p", type=int, default=3000, help="扫描最大 P，默认 3000")
    parser.add_argument("--top", type=int, default=12, help="输出最坏样本数，默认 12")
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
                "zero_theta_residue_total": result["sample_character_obstruction"]["zero_theta_residue_total"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
