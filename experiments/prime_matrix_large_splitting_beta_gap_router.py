#!/usr/bin/env python3
"""把大素数二次分裂质量硬点压成 beta-gap 与零包预算。

用法示例：
  python3 experiments/prime_matrix_large_splitting_beta_gap_router.py
  python3 experiments/prime_matrix_large_splitting_beta_gap_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-large-splitting-beta-gap-router.json

输出：
  data/prime-matrix-large-splitting-beta-gap-ledger.json
  docs/monograph/prime-matrix-large-splitting-beta-gap-router.json
  docs/monograph/prime-matrix-large-splitting-beta-gap-router.md
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

OUT_LEDGER = DATA / "prime-matrix-large-splitting-beta-gap-ledger.json"
OUT_JSON = DOCS / "prime-matrix-large-splitting-beta-gap-router.json"
OUT_MD = DOCS / "prime-matrix-large-splitting-beta-gap-router.md"

PREVIOUS = "prime-matrix-quadratic-projection-large-splitting-router.json"
STATUS_TABLE = "claim-status-table.md"
ACTUAL_LOAD_CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
CRITICAL_LOAD_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

PREVIOUS_TARGET = "LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale"
NEXT_TARGET = "SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2"
PDEC_TARGET = "UltraCloseRealZeroOrCoherentZeroPacketLargeSplittingPDEC"
INEFFECTIVE_SIEGEL = "IneffectiveSiegelTheoremFiniteBaseGap"
SELF_CONTAINED_BETA = "SelfContainedEffectivePrimeModulusQuadraticBetaGapAtScaleOneOverP"
ZERO_PACKET = "NonrealZeroPacketResidualBelowLargeSplittingSlackAtP2"

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


def fmt_float(value: float | None, digits: int = 12) -> str:
    """格式化可能缺失的浮点数。"""
    if value is None:
        return "none"
    return f"{value:.{digits}f}"


def legendre_symbol(a: int, p: int) -> int:
    """计算素模 p 下的 Legendre 符号。"""
    value = pow(a % p, (p - 1) // 2, p)
    if value == p - 1:
        return -1
    return value


def real_zero_shadow_ratio(p: int, high_mass: float, delta: float) -> float:
    """连续显式公式模型中的实零高区间归一化影子。

    这里 beta=1-delta，影子项用 (P^(2 beta)-P^beta)/(beta H0) 归一化。
    该量只用于阈值定位；真正证明仍需处理素数幂、端点和非实零包误差。
    """
    beta = 1.0 - delta
    return (math.exp(2.0 * beta * math.log(p)) - math.exp(beta * math.log(p))) / (
        beta * high_mass
    )


def critical_beta_gap(p: int, high_mass: float, tau: float) -> float | None:
    """求无剩余零包时的临界 beta-gap。"""
    target = 1.0 - tau
    if target <= 0:
        return None
    # 只取靠近 1 的实零分支；该区间内 shadow ratio 单调下降。
    upper = min(0.75, max(0.05, 1.0 - 1.0 / (2.0 * math.log(p))))
    while real_zero_shadow_ratio(p, high_mass, upper) > target and upper < 0.95:
        upper = (upper + 0.95) / 2.0
    lo = 0.0
    hi = upper
    for _ in range(96):
        mid = (lo + hi) / 2.0
        if real_zero_shadow_ratio(p, high_mass, mid) > target:
            lo = mid
        else:
            hi = mid
    return hi


def beta_gap_record(p: int, primes: list[int]) -> dict[str, Any]:
    """计算高区间二次分裂门与 beta-gap 临界尺度。"""
    cutoff = bisect_right(primes, p * p)
    high = {1: 0.0, -1: 0.0}
    h0 = 0.0
    hchi = 0.0
    for ell in primes[:cutoff]:
        if ell <= p:
            continue
        sign = legendre_symbol(ell, p)
        weight = math.log(ell)
        high[sign] += weight
        h0 += weight
        hchi += sign * weight

    required = 2.0 * p * math.log(p)
    tau = 4.0 * p * math.log(p) / h0 if h0 else float("inf")
    gap = critical_beta_gap(p, h0, tau) if h0 else None
    high_minority = min(high[1], high[-1])
    return {
        "P": p,
        "H0": h0,
        "Hchi": hchi,
        "Hplus": high[1],
        "Hminus": high[-1],
        "required_minority_mass": required,
        "large_splitting_threshold_tau": tau,
        "allowed_projection_ratio": 1.0 - tau,
        "actual_high_projection_ratio": abs(hchi) / h0 if h0 else 0.0,
        "actual_high_projection_gap": 1.0 - abs(hchi) / h0 if h0 else 0.0,
        "high_minority_mass": high_minority,
        "high_minority_to_required_ratio": high_minority / required if required else float("inf"),
        "large_splitting_gate_passes": high_minority > required,
        "critical_beta_gap_no_residual": gap,
        "critical_beta_gap_times_P": (gap * p) if gap is not None else None,
        "critical_beta_gap_times_P_over_2": (gap * p / 2.0) if gap is not None else None,
        "real_zero_shadow_ratio_at_gap_2_over_P": real_zero_shadow_ratio(p, h0, 2.0 / p),
        "gap_2_over_P_suffices_in_model": real_zero_shadow_ratio(p, h0, 2.0 / p)
        < 1.0 - tau,
    }


def finite_beta_diagnostic(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """有限扫描只定位 beta-gap 临界尺度，不作为无限证明输入。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records = [beta_gap_record(p, primes) for p in prime_moduli]
    gap_records = [item for item in records if item["critical_beta_gap_no_residual"] is not None]
    by_high = sorted(records, key=lambda item: (item["high_minority_to_required_ratio"], item["P"]))
    by_gap = sorted(
        gap_records,
        key=lambda item: (-(item["critical_beta_gap_times_P"] or 0.0), item["P"]),
    )
    ge17 = [item for item in gap_records if item["P"] >= 17]
    ge101 = [item for item in gap_records if item["P"] >= 101]
    return {
        "min_p": min_p,
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "large_splitting_gate_failure_moduli": [
            item["P"] for item in records if not item["large_splitting_gate_passes"]
        ],
        "min_high_minority_to_required_ratio": by_high[0]["high_minority_to_required_ratio"]
        if by_high
        else None,
        "min_high_minority_modulus": by_high[0]["P"] if by_high else None,
        "min_high_minority_to_required_ratio_for_P_ge_17": min(
            (item["high_minority_to_required_ratio"] for item in records if item["P"] >= 17),
            default=None,
        ),
        "max_critical_beta_gap_times_P": by_gap[0]["critical_beta_gap_times_P"]
        if by_gap
        else None,
        "max_critical_beta_gap_modulus": by_gap[0]["P"] if by_gap else None,
        "max_critical_beta_gap_times_P_for_P_ge_17": max(
            (item["critical_beta_gap_times_P"] for item in ge17 if item["critical_beta_gap_times_P"] is not None),
            default=None,
        ),
        "max_critical_beta_gap_times_P_for_P_ge_101": max(
            (item["critical_beta_gap_times_P"] for item in ge101 if item["critical_beta_gap_times_P"] is not None),
            default=None,
        ),
        "min_critical_beta_gap_times_P_for_P_ge_101": min(
            (item["critical_beta_gap_times_P"] for item in ge101 if item["critical_beta_gap_times_P"] is not None),
            default=None,
        ),
        "top_high_minority_ratio_records": by_high[:top],
        "top_critical_beta_gap_records": by_gap[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录本步公式。"""
    return [
        {
            "item": "high interval halfclass",
            "formula": "G_s(P)=sum_{P<ell<=P^2, chi_P(ell)=s} log ell",
        },
        {
            "item": "high projection",
            "formula": "H0=G_++G_-, Hchi=G_+-G_-",
        },
        {
            "item": "large splitting gate",
            "formula": "min_s G_s(P)>2P log P iff 1-|Hchi|/H0 > 4P log P/H0",
        },
        {
            "item": "explicit formula budget shape",
            "formula": "if |Hchi|/H0 <= R_beta(P)+E_zero(P), it suffices that R_beta(P)+E_zero(P)<1-4PlogP/H0",
        },
        {
            "item": "real zero high-interval shadow",
            "formula": "R_beta(P)=(P^(2beta)-P^beta)/(beta H0), beta=1-delta",
        },
        {
            "item": "critical beta gap",
            "formula": "delta_crit solves R_(1-delta)(P)=1-4PlogP/H0; asymptotically delta_crit ~ 2/P when H0~P^2",
        },
        {
            "item": "failure shape",
            "formula": "persistent failure requires beta=1-O(1/P) or a coherent nonreal/endpoint residual consuming the same slack",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": PREVIOUS_TARGET,
            "route": NEXT_TARGET,
            "status": "budget factorization",
            "meaning": "大素数二次分裂门等价于高区间角色投影必须留出 4PlogP/H0 的缺口。",
        },
        {
            "branch": "real quadratic zero shadow",
            "route": SELF_CONTAINED_BETA,
            "status": "quantified threshold",
            "meaning": "若实零影子负责失败，则 beta 必须贴近 1 到约 1/P 级。",
        },
        {
            "branch": "nonreal zeros and endpoint/prime-power corrections",
            "route": ZERO_PACKET,
            "status": "still open",
            "meaning": "即便实零影子不足，非实零同向相干或端点误差仍需有独立预算排斥。",
        },
        {
            "branch": "classical ineffective Siegel theorem",
            "route": INEFFECTIVE_SIEGEL,
            "status": "external asymptotic only",
            "meaning": "任取 epsilon<1 的 Siegel 型 gap 可渐近压过 1/P，但常数无效，不能给出本稿自足全 P 有限基。",
        },
        {
            "branch": "persistent failure",
            "route": PDEC_TARGET,
            "status": "named fallback",
            "meaning": "长期失败必须成为超近实零或非实零包同向相干的显式 PDEC/Siegel 出口。",
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
            "LargeSplittingTargetImported",
            imported,
            imported,
            "上一层已把二次投影缺口压成大素数二次分裂少数质量门。",
            PREVIOUS_TARGET,
        ),
        row(
            "HighProjectionEquivalenceClosed",
            True,
            True,
            "大分裂质量门等价于高区间二次角色投影缺口。",
            "none",
        ),
        row(
            "BetaGapCriticalScaleIdentified",
            True,
            True,
            "实零影子若单独造成失败，必须达到 beta=1-O(1/P) 的临界贴近。",
            "none",
        ),
        row(
            "ClassicalSiegelAsymptoticButIneffective",
            True,
            False,
            "经典 Siegel gap 可给渐近方向，但常数无效，不能替代自足有限基。",
            INEFFECTIVE_SIEGEL,
        ),
        row(
            "BetaGapAndZeroPacketBudgetProved",
            False,
            False,
            "当前语料尚未自足证明有效 beta-gap 与非实零包残差预算。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只量化解析临界尺度，不证明行/列命题。",
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
        f"OR ({SELF_CONTAINED_BETA} AND {ZERO_PACKET}) OR {PDEC_TARGET})))) AND "
        f"{EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    diagnostic = finite_beta_diagnostic(max_p, top)
    return {
        "certificate_type": "prime_matrix_large_splitting_beta_gap_router",
        "status": "large_splitting_mass_routed_to_beta_gap_and_zero_packet_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "pdec_fallback_target": PDEC_TARGET,
        "self_contained_beta_gap_target": SELF_CONTAINED_BETA,
        "zero_packet_residual_target": ZERO_PACKET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": diagnostic,
        "high_projection_equivalence_closed": True,
        "beta_gap_critical_scale_identified": True,
        "beta_gap_and_zero_packet_budget_proved": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale`。"
            "高区间分裂门等价于 `1-|Hchi|/H0 > 4P log P/H0`。"
            "若用显式公式预算 `|Hchi|/H0 <= R_beta(P)+E_zero(P)`，"
            "则需要 `R_beta(P)+E_zero(P)` 小于 `1-4PlogP/H0`。"
            "无剩余零包的实零模型给出临界 `1-beta` 约为 `2/P`。"
            "因此持久失败必须是 beta 贴近 1 到 `1/P` 级，或非实零/端点残差同向相干吃掉同一 slack。"
            "这把剩余硬点压成有效 beta-gap 加零包残差预算；当前仍未自足闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Large Splitting Beta-gap Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"high_projection_equivalence_closed={fmt_bool(result['high_projection_equivalence_closed'])}",
        f"beta_gap_critical_scale_identified={fmt_bool(result['beta_gap_critical_scale_identified'])}",
        f"beta_gap_and_zero_packet_budget_proved={fmt_bool(result['beta_gap_and_zero_packet_budget_proved'])}",
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
        "有限扫描只用于定位 beta-gap 临界尺度，不作为无限证明输入。",
        "",
        "```text",
        f"min_p={diagnostic['min_p']}",
        f"max_p={diagnostic['max_p']}",
        f"prime_moduli_checked={diagnostic['prime_moduli_checked']}",
        f"large_splitting_gate_failure_moduli={diagnostic['large_splitting_gate_failure_moduli']}",
        f"min_high_minority_to_required_ratio={diagnostic['min_high_minority_to_required_ratio']}",
        f"min_high_minority_to_required_ratio_for_P_ge_17={diagnostic['min_high_minority_to_required_ratio_for_P_ge_17']}",
        f"max_critical_beta_gap_times_P={diagnostic['max_critical_beta_gap_times_P']}",
        f"max_critical_beta_gap_times_P_for_P_ge_17={diagnostic['max_critical_beta_gap_times_P_for_P_ge_17']}",
        f"max_critical_beta_gap_times_P_for_P_ge_101={diagnostic['max_critical_beta_gap_times_P_for_P_ge_101']}",
        f"min_critical_beta_gap_times_P_for_P_ge_101={diagnostic['min_critical_beta_gap_times_P_for_P_ge_101']}",
        "```",
        "",
        "### 3.1 高区间少数半类最接近阈值记录",
        "",
        "| P | high minority / required | tau | actual gap | beta gap crit | P*crit |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_high_minority_ratio_records"]:
        gap = item["critical_beta_gap_no_residual"]
        lines.append(
            f"| `{item['P']}` | `{item['high_minority_to_required_ratio']:.12f}` | "
            f"`{item['large_splitting_threshold_tau']:.12f}` | "
            f"`{item['actual_high_projection_gap']:.12f}` | "
            f"`{fmt_float(gap)}` | `{fmt_float(item['critical_beta_gap_times_P'])}` |"
        )

    lines += [
        "",
        "### 3.2 临界 beta-gap 归一化最高记录",
        "",
        "| P | P*crit | crit | tau | R(2/P) | 2/P suffices in model |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_critical_beta_gap_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['critical_beta_gap_times_P']:.12f}` | "
            f"`{item['critical_beta_gap_no_residual']:.12f}` | "
            f"`{item['large_splitting_threshold_tau']:.12f}` | "
            f"`{item['real_zero_shadow_ratio_at_gap_2_over_P']:.12f}` | "
            f"`{fmt_bool(item['gap_2_over_P_suffices_in_model'])}` |"
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
        "审稿边界：本文件没有证明有效无 Siegel 零点、Linnik=2、非实零包抵消或行/列命题；它只把大素数二次分裂失败所需的实零贴近尺度与零包残差预算量化。",
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
        "min_high_minority_to_required_ratio_for_P_ge_17": result["finite_diagnostic"][
            "min_high_minority_to_required_ratio_for_P_ge_17"
        ],
        "max_critical_beta_gap_times_P_for_P_ge_101": result["finite_diagnostic"][
            "max_critical_beta_gap_times_P_for_P_ge_101"
        ],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
