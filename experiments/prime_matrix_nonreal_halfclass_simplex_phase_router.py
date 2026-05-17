#!/usr/bin/env python3
"""把非实零点包压成二次半类正交 simplex 的 rank-one 相位门。

用法示例：
  python3 experiments/prime_matrix_nonreal_halfclass_simplex_phase_router.py
  python3 experiments/prime_matrix_nonreal_halfclass_simplex_phase_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.json

输出：
  data/prime-matrix-nonreal-halfclass-simplex-phase-ledger.json
  docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.json
  docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.md
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

OUT_LEDGER = DATA / "prime-matrix-nonreal-halfclass-simplex-phase-ledger.json"
OUT_JSON = DOCS / "prime-matrix-nonreal-halfclass-simplex-phase-router.json"
OUT_MD = DOCS / "prime-matrix-nonreal-halfclass-simplex-phase-router.md"

HALFCLASS_MARGIN = "prime-matrix-siegel-quadratic-halfclass-margin-router.json"
SIEGEL_SPLIT = "prime-matrix-explicit-ap-zero-packet-siegel-split-router.json"
RANKONE = "prime-matrix-linnik2-rankone-phase-capacity-router.json"
STATUS_TABLE = "claim-status-table.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_VIII = ROOT / "docs" / "prime-density-waves-VIII.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

QUADRATIC_MARGIN_TARGET = "QuadraticHalfClassSquareScaleBiasMarginTheorem"
EFFECTIVE_NO_SIEGEL = "EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale"
NONREAL_BRANCH = "NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2"
NONREAL_SIMPLEX_TARGET = "NonrealHalfClassSimplexRankOneProjectionExclusionAtP2"
PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
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


def nonreal_record(p: int, primes: list[int]) -> dict[str, Any]:
    """计算去掉主角色和二次角色后的非实残差诊断。"""
    theta = theta_vector_for_modulus(p, primes)
    n = p - 1
    t0 = sum(theta[1:])
    t_quad = sum(legendre_symbol(a, p) * theta[a] for a in range(1, p))
    tau = t_quad / t0 if t0 else 0.0
    r_quad = abs(tau)

    residuals: list[float] = []
    required_ratios: list[float] = []
    slack_ratios: list[float] = []
    max_negative_ratio = 0.0
    worst_residue = 1
    for a in range(1, p):
        chi = legendre_symbol(a, p)
        # R_a 是删除主角色与二次角色后的非实角色包在 residue a 上的评价。
        residual = n * theta[a] - t0 - chi * t_quad
        residuals.append(residual)
        negative_ratio = max(0.0, -residual / t0) if t0 else 0.0
        required_ratio = 1.0 + chi * tau
        slack_ratio = required_ratio + residual / t0 if t0 else 0.0
        required_ratios.append(required_ratio)
        slack_ratios.append(slack_ratio)
        if negative_ratio > max_negative_ratio:
            max_negative_ratio = negative_ratio
            worst_residue = a

    nonreal_energy = sum(value * value for value in residuals) / n if n else 0.0
    min_required = min(required_ratios)
    zero_floor = (t0 * t0 * min_required * min_required) / (p - 3)
    energy_ratio = nonreal_energy / zero_floor if zero_floor else None

    return {
        "P": p,
        "T0": t0,
        "T_quadratic": t_quad,
        "quadratic_ratio": r_quad,
        "min_required_nonreal_projection_ratio_to_zero": min_required,
        "max_actual_negative_nonreal_projection_ratio": max_negative_ratio,
        "worst_residue": worst_residue,
        "worst_residue_legendre": legendre_symbol(worst_residue, p),
        "min_actual_slack_ratio": min(slack_ratios),
        "nonreal_energy": nonreal_energy,
        "nonreal_zero_floor": zero_floor,
        "nonreal_energy_to_zero_floor_ratio": energy_ratio,
        "capacity_false_positive_after_quadratic_removal": bool(energy_ratio is not None and energy_ratio >= 1.0),
    }


def finite_diagnostic(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """扫描有限样本，定位非实残差容量/相位分离。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records = [nonreal_record(p, primes) for p in prime_moduli]
    by_negative = sorted(
        records,
        key=lambda item: (item["max_actual_negative_nonreal_projection_ratio"], item["P"]),
        reverse=True,
    )
    by_energy = sorted(
        records,
        key=lambda item: (item["nonreal_energy_to_zero_floor_ratio"] or -1.0, item["P"]),
        reverse=True,
    )
    capacity_false_positive = [item for item in records if item["capacity_false_positive_after_quadratic_removal"]]
    return {
        "min_p": min_p,
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "capacity_false_positive_after_quadratic_removal_count": len(capacity_false_positive),
        "max_actual_negative_nonreal_projection_ratio": (
            by_negative[0]["max_actual_negative_nonreal_projection_ratio"] if by_negative else None
        ),
        "max_negative_ratio_modulus": by_negative[0]["P"] if by_negative else None,
        "max_nonreal_energy_to_zero_floor_ratio": (
            by_energy[0]["nonreal_energy_to_zero_floor_ratio"] if by_energy else None
        ),
        "max_energy_ratio_modulus": by_energy[0]["P"] if by_energy else None,
        "top_negative_projection_records": by_negative[:top],
        "top_energy_records": by_energy[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录非实半类 simplex 公式。"""
    return [
        {
            "item": "nonreal residual packet",
            "formula": "R_a=(P-1)theta_a(P)-T0(P)-chi_2(a)T_2(P)",
        },
        {
            "item": "zero-column requirement after quadratic removal",
            "formula": "theta_a=0 implies R_a=-T0(P)-chi_2(a)T_2(P)",
        },
        {
            "item": "minimum required nonreal projection",
            "formula": "min_a |T0+chi_2(a)T_2|/T0 = 1-|T_2|/T0",
        },
        {
            "item": "nonreal evaluation norm",
            "formula": "||w_a||^2=P-3 after removing principal and quadratic characters",
        },
        {
            "item": "halfclass simplex inner product",
            "formula": "<w_a,w_b>=P-3 if a=b; -2 if a!=b and chi_2(a)=chi_2(b); 0 if chi_2(a)!=chi_2(b)",
        },
        {
            "item": "capacity floor after quadratic removal",
            "formula": "zero column forces E_nonreal >= T0^2*(1-|T_2|/T0)^2/(P-3)",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录非实分支压缩。"""
    return [
        {
            "branch": NONREAL_BRANCH,
            "route": NONREAL_SIMPLEX_TARGET,
            "status": "open",
            "meaning": "非实零包不是无结构残差；它是两个正交二次半类 simplex 上的 rank-one 投影问题。",
        },
        {
            "branch": "capacity-only after quadratic removal",
            "route": "nonreal energy below floor would exclude zero columns",
            "status": "insufficient in current frontier",
            "meaning": "能量超过地板仍不迫使能量集中到某个 residue evaluation 方向。",
        },
        {
            "branch": NONREAL_SIMPLEX_TARGET,
            "route": "exclude rank-one negative projection of size at least (1-r_quad)T0 in both halfclass simplexes",
            "status": "not proved in corpus",
            "meaning": "这是当前解析 AP 路线的非实相位硬点。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    imported = previous.get("nonreal_branch_still_required") == NONREAL_BRANCH
    return [
        row(
            "NonrealBranchImported",
            imported,
            False,
            "上一层确认二次半类余量之后仍必须处理非实零包相位。",
            NONREAL_BRANCH,
        ),
        row(
            "HalfclassSimplexGeometryClosed",
            True,
            True,
            "删除主角色和二次角色后，evaluation 向量分裂为两个正交半类 simplex。",
            "none",
        ),
        row(
            "ZeroRequirementAfterQuadraticRemovalClosed",
            True,
            True,
            "零列要求非实残差在对应半类方向提供至少 (1-r_quad)T0 的负投影。",
            NONREAL_SIMPLEX_TARGET,
        ),
        row(
            "NonrealEnergyFloorNecessaryConditionClosed",
            True,
            True,
            "Cauchy 给出删除二次角色后的非实能量必要地板。",
            "none",
        ),
        row(
            "NonrealCapacityAloneSufficient",
            False,
            False,
            "当前语料没有证明非实能量低于地板；能量高于地板也不是相位矛盾。",
            NONREAL_SIMPLEX_TARGET,
        ),
        row(
            "NonrealRankOneProjectionExclusionProved",
            False,
            False,
            "当前语料没有排斥两个半类 simplex 中的单方向同相负投影。",
            NONREAL_SIMPLEX_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只闭合非实残差的几何和容量地板，不证明行/列命题。",
            "global final inputs remain open",
        ),
    ]


def build_result(max_p: int, top: int) -> dict[str, Any]:
    """构造证书对象。"""
    previous = load_json(DOCS / HALFCLASS_MARGIN)
    rows = build_rows(previous)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR "
        f"(({QUADRATIC_MARGIN_TARGET} OR {EFFECTIVE_NO_SIEGEL}) AND {NONREAL_SIMPLEX_TARGET})) "
        f"AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    diagnostic = finite_diagnostic(max_p, top)
    return {
        "certificate_type": "prime_matrix_nonreal_halfclass_simplex_phase_router",
        "status": "nonreal_zero_packet_routed_to_halfclass_simplex_rankone_phase_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_nonreal_branch": NONREAL_BRANCH,
        "next_direct_attack_target": NONREAL_SIMPLEX_TARGET,
        "quadratic_margin_still_required": QUADRATIC_MARGIN_TARGET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": diagnostic,
        "halfclass_simplex_geometry_closed": True,
        "zero_requirement_after_quadratic_removal_closed": True,
        "nonreal_energy_floor_closed": True,
        "nonreal_rankone_projection_exclusion_proved": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2`。"
            "删除主角色和二次角色后，非实 evaluation 向量不再是一个未解析残差，"
            "而是分裂为两个正交的二次半类 simplex。零列若存在，非实包必须在对应半类的单个 "
            "rank-one 方向提供至少 `(1-r_quad)T0` 的负投影。Cauchy 能量地板只是必要条件；"
            "真正剩余是 `NonrealHalfClassSimplexRankOneProjectionExclusionAtP2`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Nonreal Half-class Simplex Phase Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"halfclass_simplex_geometry_closed={fmt_bool(result['halfclass_simplex_geometry_closed'])}",
        f"zero_requirement_after_quadratic_removal_closed={fmt_bool(result['zero_requirement_after_quadratic_removal_closed'])}",
        f"nonreal_energy_floor_closed={fmt_bool(result['nonreal_energy_floor_closed'])}",
        f"nonreal_rankone_projection_exclusion_proved={fmt_bool(result['nonreal_rankone_projection_exclusion_proved'])}",
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
        "有限扫描只用于定位容量/相位分离，不作为无限证明输入。",
        "",
        "```text",
        f"min_p={diagnostic['min_p']}",
        f"max_p={diagnostic['max_p']}",
        f"prime_moduli_checked={diagnostic['prime_moduli_checked']}",
        f"capacity_false_positive_after_quadratic_removal_count={diagnostic['capacity_false_positive_after_quadratic_removal_count']}",
        f"max_actual_negative_nonreal_projection_ratio={diagnostic['max_actual_negative_nonreal_projection_ratio']}",
        f"max_negative_ratio_modulus={diagnostic['max_negative_ratio_modulus']}",
        f"max_nonreal_energy_to_zero_floor_ratio={diagnostic['max_nonreal_energy_to_zero_floor_ratio']}",
        f"max_energy_ratio_modulus={diagnostic['max_energy_ratio_modulus']}",
        "```",
        "",
        "### 3.1 非实负投影最高记录",
        "",
        "| P | required min | actual negative | slack | energy/floor | worst residue | chi |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_negative_projection_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['min_required_nonreal_projection_ratio_to_zero']:.12f}` | "
            f"`{item['max_actual_negative_nonreal_projection_ratio']:.12f}` | "
            f"`{item['min_actual_slack_ratio']:.12f}` | "
            f"`{item['nonreal_energy_to_zero_floor_ratio']:.12f}` | "
            f"`{item['worst_residue']}` | `{item['worst_residue_legendre']}` |"
        )

    lines += [
        "",
        "### 3.2 非实能量地板最高记录",
        "",
        "| P | energy/floor | required min | actual negative | capacity false positive |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_energy_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['nonreal_energy_to_zero_floor_ratio']:.12f}` | "
            f"`{item['min_required_nonreal_projection_ratio_to_zero']:.12f}` | "
            f"`{item['max_actual_negative_nonreal_projection_ratio']:.12f}` | "
            f"`{item['capacity_false_positive_after_quadratic_removal']}` |"
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
        "审稿边界：本文件没有证明非实 rank-one 投影排斥、二次半类余量定理或行/列命题；它只把非实残差的几何结构和容量地板严格化。",
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
                "max_actual_negative_nonreal_projection_ratio": result["finite_diagnostic"][
                    "max_actual_negative_nonreal_projection_ratio"
                ],
                "capacity_false_positive_after_quadratic_removal_count": result["finite_diagnostic"][
                    "capacity_false_positive_after_quadratic_removal_count"
                ],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
