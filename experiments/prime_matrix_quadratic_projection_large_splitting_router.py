#!/usr/bin/env python3
"""把二次投影缺口接口压成低 CRT 不足与大素数分裂质量硬点。

用法示例：
  python3 experiments/prime_matrix_quadratic_projection_large_splitting_router.py
  python3 experiments/prime_matrix_quadratic_projection_large_splitting_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-quadratic-projection-large-splitting-router.json

输出：
  data/prime-matrix-quadratic-projection-large-splitting-ledger.json
  docs/monograph/prime-matrix-quadratic-projection-large-splitting-router.json
  docs/monograph/prime-matrix-quadratic-projection-large-splitting-router.md
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

OUT_LEDGER = DATA / "prime-matrix-quadratic-projection-large-splitting-ledger.json"
OUT_JSON = DOCS / "prime-matrix-quadratic-projection-large-splitting-router.json"
OUT_MD = DOCS / "prime-matrix-quadratic-projection-large-splitting-router.md"

PREVIOUS = "prime-matrix-halfclass-capacity-margin-factorization-router.json"
STATUS_TABLE = "claim-status-table.md"
ACTUAL_LOAD_CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
CRITICAL_LOAD_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

PREVIOUS_TARGET = "QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale"
NEXT_TARGET = "LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale"
PDEC_TARGET = "UltraNearOneQuadraticProjectionDefectToLargeSplittingPDECOrSiegelPacket"
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


def split_record(p: int, primes: list[int]) -> dict[str, Any]:
    """计算二次半类质量及其低/高素数分解。"""
    cutoff = bisect_right(primes, p * p)
    low = {1: 0.0, -1: 0.0}
    high = {1: 0.0, -1: 0.0}
    total = {1: 0.0, -1: 0.0}
    t0 = 0.0
    tchi = 0.0
    for ell in primes[:cutoff]:
        if ell == p:
            continue
        sign = legendre_symbol(ell, p)
        weight = math.log(ell)
        total[sign] += weight
        if ell < p:
            low[sign] += weight
        else:
            high[sign] += weight
        t0 += weight
        tchi += sign * weight

    required_minority = 2.0 * p * math.log(p)
    low_total = low[1] + low[-1]
    high_minority = min(high[1], high[-1])
    total_minority = min(total[1], total[-1])
    projection_gap = (2.0 * total_minority / t0) if t0 else 0.0
    required_projection_gap = (4.0 * p * math.log(p) / t0) if t0 else float("inf")
    return {
        "P": p,
        "T0": t0,
        "Tchi": tchi,
        "theta_plus": total[1],
        "theta_minus": total[-1],
        "low_plus": low[1],
        "low_minus": low[-1],
        "high_plus": high[1],
        "high_minus": high[-1],
        "required_minority_mass": required_minority,
        "total_minority_mass": total_minority,
        "high_minority_mass": high_minority,
        "low_total_mass": low_total,
        "total_minority_to_required_ratio": total_minority / required_minority
        if required_minority
        else float("inf"),
        "high_minority_to_required_ratio": high_minority / required_minority
        if required_minority
        else float("inf"),
        "low_total_to_required_ratio": low_total / required_minority
        if required_minority
        else float("inf"),
        "low_trivial_cap_to_required_ratio": 0.5,
        "actual_projection_gap": projection_gap,
        "required_projection_gap": required_projection_gap,
        "capacity_gate_passes": total_minority > required_minority,
        "large_splitting_gate_passes": high_minority > required_minority,
    }


def finite_split_diagnostic(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """有限扫描只定位分裂质量硬点，不作为无限证明输入。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records = [split_record(p, primes) for p in prime_moduli]
    by_total = sorted(records, key=lambda item: (item["total_minority_to_required_ratio"], item["P"]))
    by_high = sorted(records, key=lambda item: (item["high_minority_to_required_ratio"], item["P"]))
    by_low = sorted(records, key=lambda item: (-item["low_total_to_required_ratio"], item["P"]))
    ge17_records = [item for item in records if item["P"] >= 17]
    return {
        "min_p": min_p,
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "capacity_gate_failure_moduli": [
            item["P"] for item in records if not item["capacity_gate_passes"]
        ],
        "large_splitting_gate_failure_moduli": [
            item["P"] for item in records if not item["large_splitting_gate_passes"]
        ],
        "min_total_minority_to_required_ratio": by_total[0]["total_minority_to_required_ratio"]
        if by_total
        else None,
        "min_total_minority_modulus": by_total[0]["P"] if by_total else None,
        "min_total_minority_to_required_ratio_for_P_ge_17": min(
            (item["total_minority_to_required_ratio"] for item in ge17_records),
            default=None,
        ),
        "min_high_minority_to_required_ratio": by_high[0]["high_minority_to_required_ratio"]
        if by_high
        else None,
        "min_high_minority_modulus": by_high[0]["P"] if by_high else None,
        "min_high_minority_to_required_ratio_for_P_ge_17": min(
            (item["high_minority_to_required_ratio"] for item in ge17_records),
            default=None,
        ),
        "max_low_total_to_required_ratio": by_low[0]["low_total_to_required_ratio"]
        if by_low
        else None,
        "max_low_total_modulus": by_low[0]["P"] if by_low else None,
        "top_low_total_records": by_low[:top],
        "top_low_total_records_note": "low_total is the full ell<P CRT layer; it is structurally capped by P log P = required/2.",
        "top_low_total_records_are_diagnostic_only": True,
        "top_low_total_ratio_records": by_total[:top],
        "top_high_minority_ratio_records": by_high[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录本步公式。"""
    return [
        {
            "item": "minority mass form",
            "formula": "Delta(P)=1-|T_chi|/T0=2 min_s Theta_s(P)/T0(P)",
        },
        {
            "item": "capacity threshold",
            "formula": "Delta(P)>4P log P/T0(P) iff min_s Theta_s(P)>2P log P",
        },
        {
            "item": "low CRT layer",
            "formula": "L_s(P)=sum_{ell<P, chi_P(ell)=s} log ell",
        },
        {
            "item": "large splitting layer",
            "formula": "G_s(P)=sum_{P<ell<=P^2, chi_P(ell)=s} log ell",
        },
        {
            "item": "exact split",
            "formula": "Theta_s(P)=L_s(P)+G_s(P)",
        },
        {
            "item": "elementary low cap",
            "formula": "L_+(P)+L_-(P)=theta(P-1) <= P log P = (2P log P)/2 < 2P log P",
        },
        {
            "item": "failure shape",
            "formula": "if the capacity gate fails then some s has L_s(P)+G_s(P)<=2P log P; the low CRT layer can be fully absorbed by this allowance",
        },
        {
            "item": "new hardpoint",
            "formula": "prove min_s G_s(P)>2P log P, or register the persistent large-splitting desert as PDEC/Siegel packet",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": PREVIOUS_TARGET,
            "route": "minority mass threshold",
            "status": "equivalent reformulation",
            "meaning": "投影缺口击穿阈值等价于少数二次半类 Chebyshev 质量超过 2PlogP。",
        },
        {
            "branch": "low CRT / ell<P phase constraints",
            "route": "capacity-insufficient",
            "status": "closed negative route",
            "meaning": "整个低 CRT 层总质量至多 PlogP，不能单独推出容量门，也不能强制低相位矛盾。",
        },
        {
            "branch": "large prime splitting layer P<ell<=P^2",
            "route": NEXT_TARGET,
            "status": "new direct target",
            "meaning": "剩余有效质量必须来自大素数在二次半类中的分裂；这不是有限低轮 CRT 可直接闭合的对象。",
        },
        {
            "branch": "persistent ultra-near-one projection",
            "route": PDEC_TARGET,
            "status": "named fallback",
            "meaning": "若大素数少数半类长期只有 O(PlogP) 质量，则登记为大分裂荒漠/Siegel 包/ColumnCRT-PDEC 出口。",
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
            "ProjectionGapTargetImported",
            imported,
            imported,
            "上一层已把半类容量门化成 logP/P 级二次投影缺口。",
            PREVIOUS_TARGET,
        ),
        row(
            "MinorityMassEquivalenceClosed",
            True,
            True,
            "二次投影缺口阈值等价于 min_s Theta_s(P)>2PlogP。",
            "none",
        ),
        row(
            "LowCRTCapacityInsufficiencyClosed",
            True,
            True,
            "ell<P 的完整低 CRT 层总质量最多 PlogP，不超过所需少数质量的一半。",
            "none",
        ),
        row(
            "LargeSplittingLayerIdentified",
            True,
            True,
            "反例链若继续存在，真实负载必须表现为大素数二次半类分裂荒漠。",
            NEXT_TARGET,
        ),
        row(
            "LargePrimeQuadraticSplittingMassProved",
            False,
            False,
            "当前语料尚未自足证明 P<ell<=P^2 中两半类各有超过 2PlogP 的素数权重。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步关闭低 CRT 直推误出口，但不证明行/列命题。",
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
        f"OR {NEXT_TARGET} OR {PDEC_TARGET})))) AND {EXACT_UV} AND "
        f"{MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    diagnostic = finite_split_diagnostic(max_p, top)
    return {
        "certificate_type": "prime_matrix_quadratic_projection_large_splitting_router",
        "status": "quadratic_projection_gap_routed_to_large_prime_splitting_mass_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "pdec_fallback_target": PDEC_TARGET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": diagnostic,
        "minority_mass_equivalence_closed": True,
        "low_crt_capacity_insufficiency_closed": True,
        "large_prime_quadratic_splitting_mass_proved": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale`。"
            "二次投影缺口阈值等价于少数二次半类质量 `min_s Theta_s(P)>2P log P`。"
            "把 `Theta_s` 精确拆为低 CRT 层 `ell<P` 与大素数分裂层 `P<ell<=P^2` 后，"
            "低 CRT 层总质量由平凡估计即被压到 `<=P log P`，不超过所需阈值的一半。"
            "因此低轮/有限 CRT 相位不能单独闭合本接口；真正剩余硬点是大素数二次半类分裂质量，"
            "或把 ultra-near-one 投影缺陷登记为大分裂荒漠/Siegel/ColumnCRT-PDEC 出口。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Quadratic Projection Large Splitting Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"minority_mass_equivalence_closed={fmt_bool(result['minority_mass_equivalence_closed'])}",
        f"low_crt_capacity_insufficiency_closed={fmt_bool(result['low_crt_capacity_insufficiency_closed'])}",
        f"large_prime_quadratic_splitting_mass_proved={fmt_bool(result['large_prime_quadratic_splitting_mass_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        f"pdec_fallback_target={result['pdec_fallback_target']}",
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
        "有限扫描只用于定位分裂质量硬点，不作为无限证明输入。",
        "",
        "```text",
        f"min_p={diagnostic['min_p']}",
        f"max_p={diagnostic['max_p']}",
        f"prime_moduli_checked={diagnostic['prime_moduli_checked']}",
        f"capacity_gate_failure_moduli={diagnostic['capacity_gate_failure_moduli']}",
        f"large_splitting_gate_failure_moduli={diagnostic['large_splitting_gate_failure_moduli']}",
        f"min_total_minority_to_required_ratio={diagnostic['min_total_minority_to_required_ratio']}",
        f"min_total_minority_to_required_ratio_for_P_ge_17={diagnostic['min_total_minority_to_required_ratio_for_P_ge_17']}",
        f"min_high_minority_to_required_ratio={diagnostic['min_high_minority_to_required_ratio']}",
        f"min_high_minority_to_required_ratio_for_P_ge_17={diagnostic['min_high_minority_to_required_ratio_for_P_ge_17']}",
        f"max_low_total_to_required_ratio={diagnostic['max_low_total_to_required_ratio']}",
        f"max_low_total_modulus={diagnostic['max_low_total_modulus']}",
        "```",
        "",
        "### 3.1 低 CRT 层容量最高记录",
        "",
        "| P | low total / required | total minority / required | high minority / required |",
        "| --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_low_total_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['low_total_to_required_ratio']:.12f}` | "
            f"`{item['total_minority_to_required_ratio']:.12f}` | "
            f"`{item['high_minority_to_required_ratio']:.12f}` |"
        )

    lines += [
        "",
        "### 3.2 少数半类最接近阈值的记录",
        "",
        "| P | total minority / required | high minority / required | low total / required | capacity pass | large split pass |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_low_total_ratio_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['total_minority_to_required_ratio']:.12f}` | "
            f"`{item['high_minority_to_required_ratio']:.12f}` | "
            f"`{item['low_total_to_required_ratio']:.12f}` | "
            f"`{fmt_bool(item['capacity_gate_passes'])}` | "
            f"`{fmt_bool(item['large_splitting_gate_passes'])}` |"
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
        "审稿边界：本文件证明的是低 CRT 层不足以闭合投影缺口门，并把硬点定位到大素数二次分裂质量；它没有证明该大素数分裂质量下界，因此不声明行/列命题无条件闭合。",
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
    parser.add_argument("--top", type=int, default=12, help="报告前若干条边界记录")
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.max_p, args.top)
    write_outputs(result)
    summary = {
        "status": result["status"],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "pdec_fallback_target": result["pdec_fallback_target"],
        "min_total_minority_to_required_ratio": result["finite_diagnostic"][
            "min_total_minority_to_required_ratio"
        ],
        "min_high_minority_to_required_ratio_for_P_ge_17": result["finite_diagnostic"][
            "min_high_minority_to_required_ratio_for_P_ge_17"
        ],
        "max_low_total_to_required_ratio": result["finite_diagnostic"][
            "max_low_total_to_required_ratio"
        ],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
