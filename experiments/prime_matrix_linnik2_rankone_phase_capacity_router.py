#!/usr/bin/env python3
"""把 Linnik=2 非主投影障碍分解为容量与 rank-one 相位极化。

用法示例：
  python3 experiments/prime_matrix_linnik2_rankone_phase_capacity_router.py
  python3 experiments/prime_matrix_linnik2_rankone_phase_capacity_router.py --max-p 3000 --top 12
  python3 -m json.tool docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json

输出：
  data/prime-matrix-linnik2-rankone-phase-capacity-ledger.json
  docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json
  docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.md
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

OUT_LEDGER = DATA / "prime-matrix-linnik2-rankone-phase-capacity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-linnik2-rankone-phase-capacity-router.json"
OUT_MD = DOCS / "prime-matrix-linnik2-rankone-phase-capacity-router.md"

NONPRINCIPAL_OBSTRUCTION = "prime-matrix-linnik2-nonprincipal-character-obstruction-router.json"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_V = ROOT / "docs" / "prime-density-waves-V.md"
PRIME_DENSITY_WAVES_VIII = ROOT / "docs" / "prime-density-waves-VIII.md"

PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
POINTWISE_PROJECTION_BOUND = "PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2"
RANKONE_PHASE = "RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / NONPRINCIPAL_OBSTRUCTION,
    FINAL_PROOF_DRAFT,
    PRIME_DENSITY_WAVES_V,
    PRIME_DENSITY_WAVES_VIII,
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
    """计算 theta 向量的容量指标和 rank-one 投影指标。"""
    limit = p * p
    cutoff = bisect_right(primes, limit)
    theta = [0.0] * p
    for ell in primes[:cutoff]:
        if ell == p:
            continue
        theta[ell % p] += math.log(ell)

    values = theta[1:]
    t0 = sum(values)
    average = t0 / (p - 1)
    min_residue = min(range(1, p), key=lambda a: theta[a])
    min_theta = theta[min_residue]
    max_deficit = average - min_theta
    negative_projection_ratio = max_deficit / average if average else 0.0
    phase_margin_to_zero = 1.0 - negative_projection_ratio
    zero_residues = [a for a in range(1, p) if theta[a] == 0.0]

    centered_l2 = sum((value - average) ** 2 for value in values)
    nonprincipal_energy = (p - 1) * centered_l2
    zero_floor = (t0 * t0) / (p - 2) if p > 2 else None
    energy_ratio = nonprincipal_energy / zero_floor if zero_floor else None

    # 对最危险 residue 的 evaluation 向量 v_a，投影能量占总能量的比例。
    # 这是相位极化程度；零列需要投影幅度达到 T0，而不是只需要总能量大。
    projection_energy_fraction = None
    if nonprincipal_energy > 0 and p > 2:
        projection_energy_fraction = ((p - 1) * max_deficit) ** 2 / ((p - 2) * nonprincipal_energy)

    capacity_only_can_exclude = bool(energy_ratio is not None and energy_ratio < 1.0)
    capacity_false_positive_shape = bool(energy_ratio is not None and energy_ratio >= 1.0 and not zero_residues)

    return {
        "P": p,
        "theta0": t0,
        "average_theta": average,
        "min_theta_residue": min_residue,
        "min_theta": min_theta,
        "zero_theta_residue_count": len(zero_residues),
        "negative_projection_ratio": negative_projection_ratio,
        "phase_margin_to_zero": phase_margin_to_zero,
        "nonprincipal_energy": nonprincipal_energy,
        "zero_defect_energy_floor": zero_floor,
        "energy_to_zero_floor_ratio": energy_ratio,
        "projection_energy_fraction_for_worst_residue": projection_energy_fraction,
        "capacity_only_can_exclude_zero": capacity_only_can_exclude,
        "capacity_false_positive_shape": capacity_false_positive_shape,
    }


def sample_rankone_phase(max_p: int, top: int) -> dict[str, Any]:
    """扫描有限样本，找出容量路线与投影路线的分离。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if 3 <= p <= max_p]
    records = [theta_profile_for_modulus(p, primes) for p in prime_moduli]
    by_projection = sorted(records, key=lambda item: (item["negative_projection_ratio"], item["P"]), reverse=True)
    by_energy = sorted(records, key=lambda item: (item["energy_to_zero_floor_ratio"] or -1.0, item["P"]), reverse=True)
    capacity_false_positive = [item for item in records if item["capacity_false_positive_shape"]]
    capacity_exclusion = [item for item in records if item["capacity_only_can_exclude_zero"]]

    return {
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "zero_theta_residue_total": sum(item["zero_theta_residue_count"] for item in records),
        "capacity_false_positive_count": len(capacity_false_positive),
        "capacity_exclusion_count": len(capacity_exclusion),
        "worst_projection_ratio": by_projection[0]["negative_projection_ratio"] if by_projection else None,
        "worst_projection_modulus": by_projection[0]["P"] if by_projection else None,
        "max_energy_ratio": by_energy[0]["energy_to_zero_floor_ratio"] if by_energy else None,
        "max_energy_ratio_modulus": by_energy[0]["P"] if by_energy else None,
        "top_projection_records": by_projection[:top],
        "top_energy_records": by_energy[:top],
    }


def exact_capacity_phase_chain() -> list[dict[str, str]]:
    """列出从投影界到 rank-one 相位极化界的精确链。"""
    return [
        {
            "from": POINTWISE_PROJECTION_BOUND,
            "to": "for every a, -N_a(P)/T_0(P)<1",
        },
        {
            "from": "zero column at a",
            "to": "-N_a(P)/T_0(P)=1",
        },
        {
            "from": "energy-only exclusion",
            "to": "requires sum_{chi!=chi0}|T_chi|^2<T_0(P)^2/(P-2)",
        },
        {
            "from": "energy above the floor",
            "to": "not a contradiction; one still needs rank-one projection phase control",
        },
        {
            "from": "evaluation vectors v_a",
            "to": "<v_a,v_b>=P-2 if a=b, otherwise -1; residue tests are simplex directions",
        },
        {
            "from": "remaining proof target",
            "to": RANKONE_PHASE,
        },
    ]


def formula_ledger() -> dict[str, str]:
    """登记容量/相位的判别公式。"""
    return {
        "projection_ratio": "rho_a(P)=-N_a(P)/T_0(P)=1-theta_a(P)/average_theta(P)",
        "zero_column": "theta_a(P)=0 iff rho_a(P)=1",
        "energy_floor": "zero column implies ||T_nonprincipal||_2^2 >= T_0(P)^2/(P-2)",
        "energy_only_sufficient_exclusion": "||T_nonprincipal||_2^2 < T_0(P)^2/(P-2) excludes zero columns",
        "energy_only_limitation": "if ||T_nonprincipal||_2^2 >= T_0(P)^2/(P-2), capacity alone gives no contradiction",
        "rankone_projection": "N_a(P)=<T_nonprincipal,v_a>, ||v_a||_2^2=P-2",
        "simplex_inner_product": "<v_a,v_b>=P-2 for a=b and -1 for a!=b",
    }


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    previous_imported = (
        previous.get("next_direct_attack_target") == POINTWISE_PROJECTION_BOUND
        and previous.get("pointwise_projection_bound_proved") is False
    )
    return [
        row(
            "PointwiseProjectionBarrierImported",
            previous_imported,
            False,
            "上一层已把 Linnik=2 零列缺陷压成逐 residue 的非主负投影界。",
            POINTWISE_PROJECTION_BOUND,
        ),
        row(
            "EnergyFloorNecessaryConditionClosed",
            True,
            True,
            "零列必然使非主总能量超过 T0^2/(P-2)，这是 Cauchy 的必要条件。",
            "none",
        ),
        row(
            "EnergyCapacityAloneSufficientOnlyBelowFloor",
            True,
            True,
            "若能证明总能量严格低于该地板，则可排除零列；这是容量路线的唯一直接出口。",
            "global L2 bound below zero floor",
        ),
        row(
            "EnergyCapacityRouteNotEnoughInCurrentFrontier",
            True,
            True,
            "当前对象需要排斥 rank-one 负投影；总能量在地板以上并不构成矛盾。",
            RANKONE_PHASE,
        ),
        row(
            "EvaluationVectorSimplexGeometryClosed",
            True,
            True,
            "各 residue 的非主 evaluation 向量形成正则 simplex，零列是其中一个方向的极端负投影。",
            RANKONE_PHASE,
        ),
        row(
            "RankOnePhaseCoherenceExclusionProved",
            False,
            False,
            "当前语料没有证明 rho_a(P)<1 的统一余量；这正是点态 AP 问题的相位形式。",
            RANKONE_PHASE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭容量-only 误出口，把剩余压成 rank-one 负投影相位极化排斥。",
            f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR {RANKONE_PHASE}) AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result(max_p: int, top: int) -> dict[str, Any]:
    """构造 rank-one 相位容量路由证书。"""
    previous = load_json(DOCS / NONPRINCIPAL_OBSTRUCTION)
    sample = sample_rankone_phase(max_p, top)
    rows = build_rows(previous)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR {RANKONE_PHASE}) "
        f"AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )

    return {
        "certificate_type": "prime_matrix_linnik2_rankone_phase_capacity_router",
        "status": "pointwise_nonprincipal_projection_reduced_to_rankone_phase_coherence_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "energy_floor_necessary_condition_closed": True,
        "energy_capacity_only_route_not_enough": True,
        "evaluation_vector_simplex_geometry_closed": True,
        "rankone_phase_coherence_exclusion_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": POINTWISE_PROJECTION_BOUND,
        "next_direct_attack_target": RANKONE_PHASE,
        "latest_strict_activity_basis": latest_basis,
        "formula_ledger": formula_ledger(),
        "exact_capacity_phase_chain": exact_capacity_phase_chain(),
        "sample_rankone_phase": sample,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "点态非主投影界不能只靠总能量容量闭合。零列确实强制 "
            "`||T_nonprincipal||_2^2>=T_0^2/(P-2)`，但总能量超过该地板只是必要条件，"
            "不是矛盾；真正需要排斥的是某一个 residue evaluation simplex 方向上的 "
            "rank-one 负投影达到 `-T_0`。因此最新剩余接口收缩为 "
            "`RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    sample = result["sample_rankone_phase"]
    lines = [
        "# Prime Matrix Linnik=2 rank-one 相位容量路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"energy_floor_necessary_condition_closed={fmt_bool(result['energy_floor_necessary_condition_closed'])}",
        f"energy_capacity_only_route_not_enough={fmt_bool(result['energy_capacity_only_route_not_enough'])}",
        f"evaluation_vector_simplex_geometry_closed={fmt_bool(result['evaluation_vector_simplex_geometry_closed'])}",
        f"rankone_phase_coherence_exclusion_proved={fmt_bool(result['rankone_phase_coherence_exclusion_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 公式账本",
        "",
        "| item | formula |",
        "| --- | --- |",
    ]
    for key, value in result["formula_ledger"].items():
        lines.append(f"| `{key}` | `{table_cell(value)}` |")

    lines += [
        "",
        "## 2. 容量/相位路由链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["exact_capacity_phase_chain"]:
        lines.append(f"| `{table_cell(item['from'])}` | `{table_cell(item['to'])}` |")

    lines += [
        "",
        f"## 3. 有限样本（P <= {sample['max_p']}）",
        "",
        f"- 检查素数模数：`{sample['prime_moduli_checked']}`。",
        f"- theta 零剩余类总数：`{sample['zero_theta_residue_total']}`。",
        f"- 容量-only 不能排除的样本数：`{sample['capacity_false_positive_count']}`。",
        f"- 容量-only 可直接排除的样本数：`{sample['capacity_exclusion_count']}`。",
        f"- 最大负投影比例：`{sample['worst_projection_ratio']:.6f}`，出现于 `P={sample['worst_projection_modulus']}`。",
        f"- 最大总能量/零列地板比例：`{sample['max_energy_ratio']:.6f}`，出现于 `P={sample['max_energy_ratio_modulus']}`。",
        "",
        "### 3.1 负投影最危险样本",
        "",
        "| P | min residue | min theta | rho=max(-N/T0) | phase margin | energy/floor | projection energy fraction |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in sample["top_projection_records"]:
        lines.append(
            "| {P} | {min_theta_residue} | {min_theta:.6f} | {negative_projection_ratio:.6f} | {phase_margin_to_zero:.6f} | {energy_to_zero_floor_ratio:.6f} | {projection_energy_fraction_for_worst_residue:.6f} |".format(
                **item
            )
        )

    lines += [
        "",
        "### 3.2 总能量最大样本",
        "",
        "| P | rho=max(-N/T0) | energy/floor | phase margin | capacity false positive |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in sample["top_energy_records"]:
        lines.append(
            "| {P} | {negative_projection_ratio:.6f} | {energy_to_zero_floor_ratio:.6f} | {phase_margin_to_zero:.6f} | `{capacity_false_positive_shape}` |".format(
                **item
            )
        )

    lines += [
        "",
        "这些样本只用于定位误出口：很多实例总能量已经超过零列必要地板，但仍没有零列。因此容量地板不能替代 rank-one 相位排斥。",
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
        "审稿边界：本文件没有证明 rank-one 负投影相位极化排斥；它只证明容量-only 线路不能作为当前无条件闭合，并把剩余精确定位到 evaluation simplex 的点态方向。",
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
                "capacity_false_positive_count": result["sample_rankone_phase"]["capacity_false_positive_count"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
