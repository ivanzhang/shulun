#!/usr/bin/env python3
"""把 punctured 半类全零支撑退化压成半类质量超过单 residue 容量门。

用法示例：
  python3 experiments/prime_matrix_halfclass_single_residue_capacity_router.py
  python3 experiments/prime_matrix_halfclass_single_residue_capacity_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-halfclass-single-residue-capacity-router.json

输出：
  data/prime-matrix-halfclass-single-residue-capacity-ledger.json
  docs/monograph/prime-matrix-halfclass-single-residue-capacity-router.json
  docs/monograph/prime-matrix-halfclass-single-residue-capacity-router.md
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

OUT_LEDGER = DATA / "prime-matrix-halfclass-single-residue-capacity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-halfclass-single-residue-capacity-router.json"
OUT_MD = DOCS / "prime-matrix-halfclass-single-residue-capacity-router.md"

PREVIOUS = "prime-matrix-halfclass-log-independence-degeneracy-router.json"
HALFCLASS_MARGIN = "prime-matrix-siegel-quadratic-halfclass-margin-router.json"
STATUS_TABLE = "claim-status-table.md"
ACTUAL_LOAD_CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
CRITICAL_LOAD_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

PREVIOUS_TARGET = "PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC"
NEXT_TARGET = "QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2"
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
    DOCS / STATUS_TABLE,
    ACTUAL_LOAD_CONTRACTS,
    CRITICAL_LOAD_FRONTIER,
    FINAL_PROOF_DRAFT,
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
        if ell != p:
            theta[ell % p] += math.log(ell)
    return theta


def capacity_record(p: int, primes: list[int]) -> dict[str, Any]:
    """计算半类质量和单 residue 容量读数。"""
    theta = theta_vector_for_modulus(p, primes)
    t0 = math.fsum(theta[1:])
    tchi = math.fsum(legendre_symbol(a, p) * theta[a] for a in range(1, p))
    deterministic_capacity = 2.0 * p * math.log(p)
    half_records = []
    for sign, name in ((1, "quadratic_residue"), (-1, "quadratic_nonresidue")):
        members = [a for a in range(1, p) if legendre_symbol(a, p) == sign]
        mass = math.fsum(theta[a] for a in members)
        active = [a for a in members if theta[a] > 0]
        max_residue = max((theta[a] for a in members), default=0.0)
        half_records.append(
            {
                "halfclass": name,
                "legendre_sign": sign,
                "halfclass_mass": mass,
                "active_residue_count": len(active),
                "max_actual_single_residue_weight": max_residue,
                "actual_support_surplus": mass - max_residue,
                "deterministic_single_residue_capacity": deterministic_capacity,
                "capacity_surplus": mass - deterministic_capacity,
                "mass_to_capacity_ratio": mass / deterministic_capacity if deterministic_capacity else None,
                "first_active_residues": active[:8],
            }
        )
    dangerous = min(half_records, key=lambda item: item["halfclass_mass"])
    actual_margin_ratio = 1.0 - abs(tchi) / t0 if t0 else 0.0
    required_margin_ratio = (4.0 * p * math.log(p)) / t0 if t0 else float("inf")
    return {
        "P": p,
        "T0": t0,
        "Tchi": tchi,
        "abs_quadratic_projection_ratio": abs(tchi) / t0 if t0 else 0.0,
        "actual_halfclass_margin_ratio": actual_margin_ratio,
        "required_margin_ratio_for_single_residue_capacity": required_margin_ratio,
        "margin_ratio_surplus": actual_margin_ratio - required_margin_ratio,
        "deterministic_single_residue_capacity": deterministic_capacity,
        "dangerous_halfclass": dangerous["halfclass"],
        "min_halfclass_mass": dangerous["halfclass_mass"],
        "min_mass_to_capacity_ratio": dangerous["mass_to_capacity_ratio"],
        "min_capacity_surplus": dangerous["capacity_surplus"],
        "min_actual_support_surplus": dangerous["actual_support_surplus"],
        "capacity_gate_passes": dangerous["capacity_surplus"] > 0,
        "actual_support_degeneracy_absent": dangerous["actual_support_surplus"] > 0,
        "halfclass_records": half_records,
    }


def finite_capacity_diagnostic(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """有限扫描只定位容量门风险，不作为无限证明输入。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records = [capacity_record(p, primes) for p in prime_moduli]
    by_capacity_ratio = sorted(records, key=lambda item: (item["min_mass_to_capacity_ratio"], item["P"]))
    by_margin_surplus = sorted(records, key=lambda item: (item["margin_ratio_surplus"], item["P"]))
    capacity_failures = [item for item in records if not item["capacity_gate_passes"]]
    support_degeneracies = [item for item in records if not item["actual_support_degeneracy_absent"]]
    ge17_records = [item for item in records if item["P"] >= 17]
    min_ge17 = min((item["min_mass_to_capacity_ratio"] for item in ge17_records), default=None)
    return {
        "min_p": min_p,
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "min_mass_to_capacity_ratio": by_capacity_ratio[0]["min_mass_to_capacity_ratio"] if by_capacity_ratio else None,
        "min_mass_to_capacity_modulus": by_capacity_ratio[0]["P"] if by_capacity_ratio else None,
        "min_mass_to_capacity_ratio_for_P_ge_17": min_ge17,
        "deterministic_capacity_failures_found": len(capacity_failures),
        "deterministic_capacity_failure_moduli": [item["P"] for item in capacity_failures],
        "actual_support_degeneracies_found": len(support_degeneracies),
        "top_low_capacity_records": by_capacity_ratio[:top],
        "top_low_margin_surplus_records": by_margin_surplus[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录半类质量容量门公式。"""
    return [
        {
            "item": "half-class mass",
            "formula": "Theta_s(P)=sum_{chi_P(a)=s} theta(P^2;P,a)=(T0+s*T_chi)/2",
        },
        {
            "item": "single residue deterministic capacity",
            "formula": "theta(P^2;P,a)<=P*log(P^2)=2P log P",
        },
        {
            "item": "zero-support degeneracy implication",
            "formula": "punctured half-class zero support implies Theta_s(P)=theta(P^2;P,a0)<=2P log P",
        },
        {
            "item": "capacity exclusion gate",
            "formula": "min_s Theta_s(P)>2P log P excludes punctured half-class zero-support degeneracy",
        },
        {
            "item": "quadratic projection form",
            "formula": "T0(P)*(1-|T_chi(P)|/T0(P))>4P log P",
        },
        {
            "item": "new hardpoint",
            "formula": "prove QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2 or route capacity failure to ColumnCRT/PDEC",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": PREVIOUS_TARGET,
            "route": NEXT_TARGET,
            "status": "sharpened but open",
            "meaning": "半类全零支撑若存在，则对应半类质量不能超过单 residue 的确定性容量。",
        },
        {
            "branch": "single-residue capacity",
            "route": "theta(P^2;P,a)<=2P log P",
            "status": "closed as counting bound",
            "meaning": "一个 residue 在 P^2 前至多有 P 个候选位置，每个素数权重至多 2 log P。",
        },
        {
            "branch": NEXT_TARGET,
            "route": "T0(P)*(1-|T_chi|/T0)>4P log P",
            "status": "not proved in corpus",
            "meaning": "剩余是二次半类总 Chebyshev 质量必须击穿单 residue 容量。",
        },
        {
            "branch": "capacity failure",
            "route": "ColumnCRT/PDEC/moving-family registration",
            "status": "not proved in corpus",
            "meaning": "若容量门失败，则反例链已被压成半类总质量过低的显式二次角色缺陷。",
        },
    ]


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "PreviousZeroSupportDegeneracyImported",
            imported,
            imported,
            "上一层把精确轨道锁压成 punctured 半类全零支撑退化。",
            PREVIOUS_TARGET,
        ),
        row(
            "SingleResidueDeterministicCapacityClosed",
            True,
            True,
            "固定 residue 在 P^2 前的 theta 权重至多 2P log P。",
            "none",
        ),
        row(
            "ZeroSupportDegeneracyImpliesCapacityFailureClosed",
            True,
            True,
            "若同半类除缺孔外全零，则该半类总质量必须不超过单 residue 容量。",
            "none",
        ),
        row(
            "FiniteBaseSupportDegeneracyAbsentInDiagnostic",
            True,
            False,
            "有限诊断中 P<=13 的确定性容量门不全通过，但实际支撑退化为零；有限读数不替代无限证明。",
            "none",
        ),
        row(
            "QuadraticHalfClassMassBeatsSingleResidueCapacityProved",
            False,
            False,
            "当前语料尚未自足证明每个二次半类总质量都超过 2P log P。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只把零支撑退化压成半类质量容量门，不证明行/列命题。",
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
    diagnostic = finite_capacity_diagnostic(max_p, top)
    return {
        "certificate_type": "prime_matrix_halfclass_single_residue_capacity_router",
        "status": "zero_support_degeneracy_routed_to_halfclass_single_residue_capacity_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "quadratic_margin_still_required": QUADRATIC_MARGIN_TARGET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": diagnostic,
        "single_residue_deterministic_capacity_closed": True,
        "zero_support_degeneracy_implies_capacity_failure_closed": True,
        "quadratic_halfclass_mass_beats_single_residue_capacity_proved": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC`。"
            "若同一二次半类除缺孔外全无 `P^2` 内素数到达，则该半类全部 Chebyshev 质量只能落在一个 residue。"
            "而单个 residue 在 `P^2` 前至多有 `P` 个候选位置，因此权重不超过 `2P log P`。"
            "所以只要证明 `min_s Theta_s(P)>2P log P`，即 "
            "`T0(P)*(1-|T_chi(P)|/T0(P))>4P log P`，就排除该退化。"
            "最新硬点压成 `QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Half-class Single-residue Capacity Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"single_residue_deterministic_capacity_closed={fmt_bool(result['single_residue_deterministic_capacity_closed'])}",
        f"zero_support_degeneracy_implies_capacity_failure_closed={fmt_bool(result['zero_support_degeneracy_implies_capacity_failure_closed'])}",
        f"quadratic_halfclass_mass_beats_single_residue_capacity_proved={fmt_bool(result['quadratic_halfclass_mass_beats_single_residue_capacity_proved'])}",
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
        "有限扫描只用于定位容量门风险，不作为无限证明输入。",
        "",
        "```text",
        f"min_p={diagnostic['min_p']}",
        f"max_p={diagnostic['max_p']}",
        f"prime_moduli_checked={diagnostic['prime_moduli_checked']}",
        f"min_mass_to_capacity_ratio={diagnostic['min_mass_to_capacity_ratio']}",
        f"min_mass_to_capacity_modulus={diagnostic['min_mass_to_capacity_modulus']}",
        f"min_mass_to_capacity_ratio_for_P_ge_17={diagnostic['min_mass_to_capacity_ratio_for_P_ge_17']}",
        f"deterministic_capacity_failures_found={diagnostic['deterministic_capacity_failures_found']}",
        f"deterministic_capacity_failure_moduli={diagnostic['deterministic_capacity_failure_moduli']}",
        f"actual_support_degeneracies_found={diagnostic['actual_support_degeneracies_found']}",
        "```",
        "",
        "### 3.1 半类质量最接近单 residue 容量的记录",
        "",
        "| P | dangerous halfclass | min mass | capacity | ratio | surplus | actual support surplus | margin surplus |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_low_capacity_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['dangerous_halfclass']}` | "
            f"`{item['min_halfclass_mass']:.12f}` | "
            f"`{item['deterministic_single_residue_capacity']:.12f}` | "
            f"`{item['min_mass_to_capacity_ratio']:.12f}` | "
            f"`{item['min_capacity_surplus']:.12f}` | "
            f"`{item['min_actual_support_surplus']:.12f}` | "
            f"`{item['margin_ratio_surplus']:.12f}` |"
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
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | "
            f"{table_cell(item['remaining'])} |"
        )

    lines += [
        "",
        "## 5. 最新活动基",
        "",
        "```text",
        result["latest_strict_activity_basis"],
        "```",
        "",
        "审稿边界：本文件没有证明二次半类总质量必然超过单 residue 容量；它只给出从零支撑退化到该容量门的严格蕴含。",
        "",
        "## 6. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=False)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=1000, help="有限诊断的最大素模 P")
    parser.add_argument("--top", type=int, default=12, help="报告前若干条低容量记录")
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.max_p, args.top)
    write_outputs(result)
    summary = {
        "status": result["status"],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "min_mass_to_capacity_ratio": result["finite_diagnostic"]["min_mass_to_capacity_ratio"],
        "min_mass_to_capacity_ratio_for_P_ge_17": result["finite_diagnostic"][
            "min_mass_to_capacity_ratio_for_P_ge_17"
        ],
        "deterministic_capacity_failure_moduli": result["finite_diagnostic"][
            "deterministic_capacity_failure_moduli"
        ],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
