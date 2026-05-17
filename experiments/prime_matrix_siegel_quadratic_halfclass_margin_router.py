#!/usr/bin/env python3
"""把 Siegel 实零偏置分支压成二次角色半类投影余量门。

用法示例：
  python3 experiments/prime_matrix_siegel_quadratic_halfclass_margin_router.py
  python3 experiments/prime_matrix_siegel_quadratic_halfclass_margin_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json

输出：
  data/prime-matrix-siegel-quadratic-halfclass-margin-ledger.json
  docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json
  docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.md
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

OUT_LEDGER = DATA / "prime-matrix-siegel-quadratic-halfclass-margin-ledger.json"
OUT_JSON = DOCS / "prime-matrix-siegel-quadratic-halfclass-margin-router.json"
OUT_MD = DOCS / "prime-matrix-siegel-quadratic-halfclass-margin-router.md"

SIEGEL_SPLIT = "prime-matrix-explicit-ap-zero-packet-siegel-split-router.json"
NONPRINCIPAL = "prime-matrix-linnik2-nonprincipal-character-obstruction-router.json"
RANKONE = "prime-matrix-linnik2-rankone-phase-capacity-router.json"
STATUS_TABLE = "claim-status-table.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_VIII = ROOT / "docs" / "prime-density-waves-VIII.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

SIEGEL_BRANCH = "SiegelExceptionalBiasExclusionAtSquareScale"
HALFCLASS_MARGIN = "QuadraticHalfClassSquareScaleBiasMarginTheorem"
EFFECTIVE_NO_SIEGEL = "EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale"
NONREAL_BRANCH = "NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2"
PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / SIEGEL_SPLIT,
    DOCS / NONPRINCIPAL,
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


def quadratic_projection_record(p: int, primes: list[int]) -> dict[str, Any]:
    """计算二次角色投影 T_chi/T0 与半类余量。"""
    limit = p * p
    cutoff = bisect_right(primes, limit)
    t0 = 0.0
    tchi = 0.0
    qr_weight = 0.0
    nqr_weight = 0.0
    qr_count = 0
    nqr_count = 0
    for ell in primes[:cutoff]:
        if ell == p:
            continue
        weight = math.log(ell)
        symbol = legendre_symbol(ell, p)
        t0 += weight
        tchi += symbol * weight
        if symbol == 1:
            qr_weight += weight
            qr_count += 1
        elif symbol == -1:
            nqr_weight += weight
            nqr_count += 1

    ratio = abs(tchi) / t0 if t0 else 0.0
    signed_ratio = tchi / t0 if t0 else 0.0
    dangerous_half = "quadratic_residue" if tchi < 0 else "quadratic_nonresidue"
    halfclass_margin = 1.0 - ratio
    # 只保留有限精度，避免 JSON 中出现过长浮点噪声。
    return {
        "P": p,
        "T0": t0,
        "Tchi": tchi,
        "signed_quadratic_projection_ratio": signed_ratio,
        "abs_quadratic_projection_ratio": ratio,
        "halfclass_margin_ratio": halfclass_margin,
        "dangerous_halfclass_if_only_real_projection": dangerous_half,
        "qr_weight": qr_weight,
        "nqr_weight": nqr_weight,
        "qr_prime_count": qr_count,
        "nqr_prime_count": nqr_count,
    }


def sample_quadratic_projection(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """扫描有限样本，定位二次投影比例的风险轮廓。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records = [quadratic_projection_record(p, primes) for p in prime_moduli]
    by_ratio = sorted(records, key=lambda item: (item["abs_quadratic_projection_ratio"], item["P"]), reverse=True)
    max_record = by_ratio[0] if by_ratio else None
    return {
        "max_p": max_p,
        "min_p": min_p,
        "prime_moduli_checked": len(prime_moduli),
        "max_abs_quadratic_projection_ratio": max_record["abs_quadratic_projection_ratio"] if max_record else None,
        "max_abs_ratio_modulus": max_record["P"] if max_record else None,
        "min_halfclass_margin_ratio": max_record["halfclass_margin_ratio"] if max_record else None,
        "top_quadratic_projection_records": by_ratio[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录 Siegel 分支的等价量。"""
    return [
        {
            "item": "quadratic character projection",
            "formula": "T_chi(P)=sum_{ell<=P^2, ell prime, ell!=P} chi_P(ell) log ell",
        },
        {
            "item": "principal mass",
            "formula": "T0(P)=sum_{ell<=P^2, ell prime, ell!=P} log ell",
        },
        {
            "item": "real-projection ratio",
            "formula": "r_quad(P)=|T_chi(P)|/T0(P)",
        },
        {
            "item": "half-class main margin",
            "formula": "dangerous half-class average weight is proportional to 1-r_quad(P)",
        },
        {
            "item": "exceptional-zero heuristic",
            "formula": "if beta=1-lambda/log P, then r_quad(P) has square-scale size about exp(-2 lambda)/beta",
        },
        {
            "item": "needed theorem",
            "formula": "prove r_quad(P)<=1-eta(P) with enough eta(P) to dominate nonreal and finite packets",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": SIEGEL_BRANCH,
            "route": f"{HALFCLASS_MARGIN} OR {EFFECTIVE_NO_SIEGEL}",
            "status": "open",
            "meaning": "实零偏置被精确改写为二次角色投影比例接近 1 的风险。",
        },
        {
            "branch": HALFCLASS_MARGIN,
            "route": "prove |T_chi|/T0 is bounded away from 1 at square scale with explicit margin",
            "status": "not proved in corpus",
            "meaning": "这是自足线需要的新点态实角色余量，不是平均 AP 定理。",
        },
        {
            "branch": EFFECTIVE_NO_SIEGEL,
            "route": "accept an independently certified no-Siegel-zero or beta-gap theorem strong enough at x=P^2",
            "status": "not available as unconditional peer-certified input here",
            "meaning": "经典零点排斥可作为结构组织，但不能替代该输入。",
        },
        {
            "branch": NONREAL_BRANCH,
            "route": "still required after real half-class margin",
            "status": "open",
            "meaning": "即使二次半类保留主项余量，非实零包仍可能在单个 residue 方向上造成点态缺口。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    imported = previous.get("siegel_branch_target") == SIEGEL_BRANCH
    return [
        row(
            "SiegelBranchImported",
            imported,
            False,
            "上一层已把 AP 零点包拆出 Siegel 实零偏置分支。",
            SIEGEL_BRANCH,
        ),
        row(
            "QuadraticProjectionIdentityClosed",
            True,
            True,
            "实二次角色贡献等于 QR/NQR 半类权重差，危险半类余量由 1-|T_chi|/T0 控制。",
            HALFCLASS_MARGIN,
        ),
        row(
            "FiniteDiagnosticLedgerGenerated",
            True,
            True,
            "有限扫描只作风险定位；它不作为无限证明输入。",
            "none",
        ),
        row(
            "HalfClassMarginTheoremProved",
            False,
            False,
            "当前语料没有证明 square-scale 二次投影比例全局远离 1。",
            HALFCLASS_MARGIN,
        ),
        row(
            "EffectiveNoSiegelInputAccepted",
            False,
            False,
            "当前没有可作为合著稿无条件输入的全局无 Siegel 零点或足够强 beta-gap 定理。",
            EFFECTIVE_NO_SIEGEL,
        ),
        row(
            "SiegelBranchClosed",
            False,
            False,
            "本步只把 Siegel 分支压缩为半类余量门或外部 beta-gap 门。",
            f"{HALFCLASS_MARGIN} OR {EFFECTIVE_NO_SIEGEL}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "非实零包、结构 PDEC/signed payload、ExactUV、RatePreservation 与 DStructure 仍未全部闭合。",
            "global final inputs remain open",
        ),
    ]


def build_result(max_p: int, top: int) -> dict[str, Any]:
    """构造证书对象。"""
    previous = load_json(DOCS / SIEGEL_SPLIT)
    rows = build_rows(previous)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR "
        f"(({HALFCLASS_MARGIN} OR {EFFECTIVE_NO_SIEGEL}) AND {NONREAL_BRANCH})) "
        f"AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    sample = sample_quadratic_projection(max_p, top)
    return {
        "certificate_type": "prime_matrix_siegel_quadratic_halfclass_margin_router",
        "status": "siegel_branch_routed_to_quadratic_halfclass_margin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_branch": SIEGEL_BRANCH,
        "next_direct_attack_target": HALFCLASS_MARGIN,
        "external_escape_target": EFFECTIVE_NO_SIEGEL,
        "nonreal_branch_still_required": NONREAL_BRANCH,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": sample,
        "quadratic_projection_identity_closed": True,
        "halfclass_margin_theorem_proved": False,
        "effective_no_siegel_input_accepted": False,
        "siegel_branch_closed": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `SiegelExceptionalBiasExclusionAtSquareScale`："
            "实二次零点偏置在 prime modulus 下被压成二次角色投影比例 "
            "`r_quad(P)=|T_chi(P)|/T0(P)`。危险半类的平均主项余量正比于 `1-r_quad(P)`。"
            "因此 Siegel 分支若要闭合，必须自足证明 `QuadraticHalfClassSquareScaleBiasMarginTheorem`，"
            "或接受足够强且独立认证的无 Siegel 零点/beta-gap 输入。当前二者均未完成，"
            "非实零包相位抵消也仍需另证。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    sample = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Siegel Quadratic Half-class Margin Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"quadratic_projection_identity_closed={fmt_bool(result['quadratic_projection_identity_closed'])}",
        f"halfclass_margin_theorem_proved={fmt_bool(result['halfclass_margin_theorem_proved'])}",
        f"effective_no_siegel_input_accepted={fmt_bool(result['effective_no_siegel_input_accepted'])}",
        f"siegel_branch_closed={fmt_bool(result['siegel_branch_closed'])}",
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
        "有限扫描只用于定位风险，不作为无限证明输入。",
        "",
        "```text",
        f"max_p={sample['max_p']}",
        f"min_p={sample['min_p']}",
        f"prime_moduli_checked={sample['prime_moduli_checked']}",
        f"max_abs_quadratic_projection_ratio={sample['max_abs_quadratic_projection_ratio']}",
        f"max_abs_ratio_modulus={sample['max_abs_ratio_modulus']}",
        f"min_halfclass_margin_ratio={sample['min_halfclass_margin_ratio']}",
        "```",
        "",
        "| P | abs ratio | signed ratio | halfclass margin | dangerous halfclass |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in sample["top_quadratic_projection_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['abs_quadratic_projection_ratio']:.12f}` | "
            f"`{item['signed_quadratic_projection_ratio']:.12f}` | "
            f"`{item['halfclass_margin_ratio']:.12f}` | "
            f"`{item['dangerous_halfclass_if_only_real_projection']}` |"
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
        "审稿边界：本文件没有证明无 Siegel 零点、二次半类余量定理、非实零包相位抵消或行/列命题；它只把 Siegel 实零分支压成可复核的二次角色投影余量门。",
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
                "max_abs_quadratic_projection_ratio": result["finite_diagnostic"]["max_abs_quadratic_projection_ratio"],
                "siegel_branch_closed": result["siegel_branch_closed"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
