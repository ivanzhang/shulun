#!/usr/bin/env python3
"""把半类单 residue 容量门分解为总质量下界与二次投影缺口阈值。

用法示例：
  python3 experiments/prime_matrix_halfclass_capacity_margin_factorization_router.py
  python3 experiments/prime_matrix_halfclass_capacity_margin_factorization_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-halfclass-capacity-margin-factorization-router.json

输出：
  data/prime-matrix-halfclass-capacity-margin-factorization-ledger.json
  docs/monograph/prime-matrix-halfclass-capacity-margin-factorization-router.json
  docs/monograph/prime-matrix-halfclass-capacity-margin-factorization-router.md
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

OUT_LEDGER = DATA / "prime-matrix-halfclass-capacity-margin-factorization-ledger.json"
OUT_JSON = DOCS / "prime-matrix-halfclass-capacity-margin-factorization-router.json"
OUT_MD = DOCS / "prime-matrix-halfclass-capacity-margin-factorization-router.md"

PREVIOUS = "prime-matrix-halfclass-single-residue-capacity-router.json"
SIEGEL_MARGIN = "prime-matrix-siegel-quadratic-halfclass-margin-router.json"
STATUS_TABLE = "claim-status-table.md"
ACTUAL_LOAD_CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
CRITICAL_LOAD_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

PREVIOUS_TARGET = "QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2"
NEXT_TARGET = "QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale"
CHEBYSHEV_LOWER_ATOM = "ChebyshevPrincipalMassLowerBoundAtP2"
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
    DOCS / SIEGEL_MARGIN,
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


def projection_margin_record(p: int, primes: list[int]) -> dict[str, Any]:
    """计算容量门等价的二次投影缺口阈值。"""
    cutoff = bisect_right(primes, p * p)
    t0 = 0.0
    tchi = 0.0
    for ell in primes[:cutoff]:
        if ell == p:
            continue
        weight = math.log(ell)
        t0 += weight
        tchi += legendre_symbol(ell, p) * weight
    abs_ratio = abs(tchi) / t0 if t0 else 0.0
    actual_gap = 1.0 - abs_ratio
    required_gap = (4.0 * p * math.log(p)) / t0 if t0 else float("inf")
    gate_ratio = actual_gap / required_gap if required_gap else float("inf")
    chebyshev_scale = t0 / (p * p)
    log_over_p_threshold_with_actual_t0 = required_gap
    return {
        "P": p,
        "T0": t0,
        "Tchi": tchi,
        "principal_mass_scale_T0_over_P2": chebyshev_scale,
        "abs_quadratic_projection_ratio": abs_ratio,
        "actual_projection_gap": actual_gap,
        "required_projection_gap": required_gap,
        "actual_gap_to_required_gap_ratio": gate_ratio,
        "equivalent_min_halfclass_mass": (t0 - abs(tchi)) / 2.0,
        "single_residue_capacity": 2.0 * p * math.log(p),
        "capacity_gate_passes": gate_ratio > 1.0,
        "log_over_p": math.log(p) / p,
        "required_gap_div_log_over_p": log_over_p_threshold_with_actual_t0 / (math.log(p) / p),
    }


def finite_margin_diagnostic(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """有限扫描只定位缺口阈值风险，不作为无限证明输入。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records = [projection_margin_record(p, primes) for p in prime_moduli]
    by_ratio = sorted(records, key=lambda item: (item["actual_gap_to_required_gap_ratio"], item["P"]))
    by_required = sorted(records, key=lambda item: (item["required_projection_gap"], item["P"]), reverse=True)
    failures = [item for item in records if not item["capacity_gate_passes"]]
    ge17_records = [item for item in records if item["P"] >= 17]
    ge17_min = min((item["actual_gap_to_required_gap_ratio"] for item in ge17_records), default=None)
    max_required_ge17 = max((item["required_projection_gap"] for item in ge17_records), default=None)
    return {
        "min_p": min_p,
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "min_actual_gap_to_required_gap_ratio": by_ratio[0]["actual_gap_to_required_gap_ratio"]
        if by_ratio
        else None,
        "min_ratio_modulus": by_ratio[0]["P"] if by_ratio else None,
        "min_actual_gap_to_required_gap_ratio_for_P_ge_17": ge17_min,
        "max_required_projection_gap": by_required[0]["required_projection_gap"] if by_required else None,
        "max_required_projection_gap_modulus": by_required[0]["P"] if by_required else None,
        "max_required_projection_gap_for_P_ge_17": max_required_ge17,
        "capacity_gate_failure_moduli": [item["P"] for item in failures],
        "top_low_gap_ratio_records": by_ratio[:top],
        "top_high_required_gap_records": by_required[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录容量门分解公式。"""
    return [
        {
            "item": "capacity gate",
            "formula": "min_s Theta_s(P)>2P log P",
        },
        {
            "item": "projection gap form",
            "formula": "1-|T_chi(P)|/T0(P) > 4P log P / T0(P)",
        },
        {
            "item": "principal mass factorization",
            "formula": "if T0(P)>=c0(P)P^2 then it suffices that 1-|T_chi|/T0 > 4 log P/(c0(P)P)",
        },
        {
            "item": "failure shape",
            "formula": "capacity failure plus T0 lower bound forces |T_chi|/T0 >= 1-O(log P/P)",
        },
        {
            "item": "stronger existing input",
            "formula": "QuadraticHalfClassSquareScaleBiasMarginTheorem gives this gate if its eta(P) beats 4P log P/T0(P)",
        },
        {
            "item": "new hardpoint",
            "formula": "prove QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale or register ultra-near-one quadratic projection as ColumnCRT/PDEC",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": PREVIOUS_TARGET,
            "route": NEXT_TARGET,
            "status": "equivalent reformulation",
            "meaning": "半类质量击穿单 residue 容量等价于二次投影缺口击穿显式阈值。",
        },
        {
            "branch": CHEBYSHEV_LOWER_ATOM,
            "route": "turn threshold into O(log P/P)",
            "status": "standard but not re-proved in this certificate",
            "meaning": "一旦主质量 T0 有 P^2 级下界，容量门所需二次缺口只有 logP/P 级。",
        },
        {
            "branch": QUADRATIC_MARGIN_TARGET,
            "route": NEXT_TARGET,
            "status": "stronger than needed for this gate if eta(P)>4PlogP/T0(P)",
            "meaning": "原 Siegel 半类余量门可作为更强输入，但本步暴露所需余量其实很小。",
        },
        {
            "branch": "capacity failure",
            "route": "ultra-near-one quadratic projection defect",
            "status": "not excluded in corpus",
            "meaning": "若反例链持久，则二次角色投影必须接近主质量到 logP/P 级别。",
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
            "PreviousCapacityGateImported",
            imported,
            imported,
            "上一层把零支撑退化压成半类总质量超过单 residue 容量。",
            PREVIOUS_TARGET,
        ),
        row(
            "ProjectionGapEquivalenceClosed",
            True,
            True,
            "容量门等价于 1-|T_chi|/T0 > 4PlogP/T0。",
            "none",
        ),
        row(
            "LogOverPThresholdReductionClosed",
            True,
            True,
            "给定任意 T0>=c0(P)P^2，下游阈值就是 4logP/(c0(P)P)。",
            CHEBYSHEV_LOWER_ATOM,
        ),
        row(
            "FixedPositiveQuadraticMarginSufficesEventually",
            True,
            True,
            "任意固定正二次投影缺口都会在大 P 上远强于容量门。",
            "finite base plus " + CHEBYSHEV_LOWER_ATOM,
        ),
        row(
            "QuadraticProjectionGapBeatsThresholdProved",
            False,
            False,
            "当前语料尚未自足证明二次投影缺口击穿 4PlogP/T0。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只做等价分解与阈值缩小，不证明行/列命题。",
            "global final inputs remain open",
        ),
    ]


def build_result(max_p: int, top: int) -> dict[str, Any]:
    """构造证书对象。"""
    previous = load_json(DOCS / PREVIOUS)
    rows = build_rows(previous)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR "
        f"(({CHEBYSHEV_LOWER_ATOM} AND ({QUADRATIC_MARGIN_TARGET} OR {EFFECTIVE_NO_SIEGEL} "
        f"OR {NEXT_TARGET})))) AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    diagnostic = finite_margin_diagnostic(max_p, top)
    return {
        "certificate_type": "prime_matrix_halfclass_capacity_margin_factorization_router",
        "status": "halfclass_capacity_gate_factored_to_log_over_p_quadratic_projection_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "chebyshev_lower_atom": CHEBYSHEV_LOWER_ATOM,
        "quadratic_margin_still_sufficient": QUADRATIC_MARGIN_TARGET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": diagnostic,
        "projection_gap_equivalence_closed": True,
        "log_over_p_threshold_reduction_closed": True,
        "quadratic_projection_gap_beats_threshold_proved": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2`。"
            "半类容量门等价于二次投影缺口 `1-|T_chi|/T0` 大于显式阈值 `4P log P/T0`。"
            "一旦主质量有 `T0>=c0(P)P^2` 的 Chebyshev 级下界，所需缺口只有 "
            "`4 log P/(c0(P)P)`。因此持久失败不再是普通半类偏置，"
            "而是二次投影接近主质量到 `logP/P` 级的极端异常。"
            "最新硬点压成 `QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Half-class Capacity Margin Factorization Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"projection_gap_equivalence_closed={fmt_bool(result['projection_gap_equivalence_closed'])}",
        f"log_over_p_threshold_reduction_closed={fmt_bool(result['log_over_p_threshold_reduction_closed'])}",
        f"quadratic_projection_gap_beats_threshold_proved={fmt_bool(result['quadratic_projection_gap_beats_threshold_proved'])}",
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
        "有限扫描只用于定位投影缺口阈值，不作为无限证明输入。",
        "",
        "```text",
        f"min_p={diagnostic['min_p']}",
        f"max_p={diagnostic['max_p']}",
        f"prime_moduli_checked={diagnostic['prime_moduli_checked']}",
        f"min_actual_gap_to_required_gap_ratio={diagnostic['min_actual_gap_to_required_gap_ratio']}",
        f"min_ratio_modulus={diagnostic['min_ratio_modulus']}",
        f"min_actual_gap_to_required_gap_ratio_for_P_ge_17={diagnostic['min_actual_gap_to_required_gap_ratio_for_P_ge_17']}",
        f"max_required_projection_gap={diagnostic['max_required_projection_gap']}",
        f"max_required_projection_gap_modulus={diagnostic['max_required_projection_gap_modulus']}",
        f"max_required_projection_gap_for_P_ge_17={diagnostic['max_required_projection_gap_for_P_ge_17']}",
        f"capacity_gate_failure_moduli={diagnostic['capacity_gate_failure_moduli']}",
        "```",
        "",
        "### 3.1 投影缺口最接近阈值的记录",
        "",
        "| P | actual gap | required gap | ratio | T0/P^2 | required/(logP/P) | capacity pass |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_low_gap_ratio_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['actual_projection_gap']:.12f}` | "
            f"`{item['required_projection_gap']:.12f}` | "
            f"`{item['actual_gap_to_required_gap_ratio']:.12f}` | "
            f"`{item['principal_mass_scale_T0_over_P2']:.12f}` | "
            f"`{item['required_gap_div_log_over_p']:.12f}` | "
            f"`{fmt_bool(item['capacity_gate_passes'])}` |"
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
        "审稿边界：本文件没有证明二次投影缺口击穿阈值；它只把容量门化为一个 `logP/P` 级投影缺口问题。",
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
    parser.add_argument("--top", type=int, default=12, help="报告前若干条低阈值余量记录")
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.max_p, args.top)
    write_outputs(result)
    summary = {
        "status": result["status"],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "min_actual_gap_to_required_gap_ratio": result["finite_diagnostic"][
            "min_actual_gap_to_required_gap_ratio"
        ],
        "min_actual_gap_to_required_gap_ratio_for_P_ge_17": result["finite_diagnostic"][
            "min_actual_gap_to_required_gap_ratio_for_P_ge_17"
        ],
        "capacity_gate_failure_moduli": result["finite_diagnostic"]["capacity_gate_failure_moduli"],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
