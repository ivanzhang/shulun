#!/usr/bin/env python3
"""把精确半类轨道锁压成对数独立支撑退化出口。

用法示例：
  python3 experiments/prime_matrix_halfclass_log_independence_degeneracy_router.py
  python3 experiments/prime_matrix_halfclass_log_independence_degeneracy_router.py --max-p 1500 --top 16
  python3 -m json.tool docs/monograph/prime-matrix-halfclass-log-independence-degeneracy-router.json

输出：
  data/prime-matrix-halfclass-log-independence-degeneracy-ledger.json
  docs/monograph/prime-matrix-halfclass-log-independence-degeneracy-router.json
  docs/monograph/prime-matrix-halfclass-log-independence-degeneracy-router.md
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

OUT_LEDGER = DATA / "prime-matrix-halfclass-log-independence-degeneracy-ledger.json"
OUT_JSON = DOCS / "prime-matrix-halfclass-log-independence-degeneracy-router.json"
OUT_MD = DOCS / "prime-matrix-halfclass-log-independence-degeneracy-router.md"

PREVIOUS = "prime-matrix-halfclass-twist-pair-character-lock-router.json"
RATIO = "prime-matrix-halfclass-ratio-fourier-lock-router.json"
STATUS_TABLE = "claim-status-table.md"
ACTUAL_LOAD_CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
CRITICAL_LOAD_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

PREVIOUS_TARGET = "QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC"
NEXT_TARGET = "PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC"
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
    DOCS / RATIO,
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


def theta_support_counts(p: int, primes: list[int]) -> list[int]:
    """计算每个非零 residue 中小于等于 P^2 的素数个数。"""
    counts = [0] * p
    cutoff = bisect_right(primes, p * p)
    for ell in primes[:cutoff]:
        if ell != p:
            counts[ell % p] += 1
    return counts


def finite_support_diagnostic(max_p: int, top: int, min_p: int = 7) -> dict[str, Any]:
    """有限扫描只定位零支撑退化，不作为无限证明输入。"""
    _, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if min_p <= p <= max_p]
    records: list[dict[str, Any]] = []
    degeneracy_records: list[dict[str, Any]] = []
    for p in prime_moduli:
        counts = theta_support_counts(p, primes)
        for sign, name in ((1, "quadratic_residue"), (-1, "quadratic_nonresidue")):
            members = [a for a in range(1, p) if legendre_symbol(a, p) == sign]
            h = len(members)
            active_members = [a for a in members if counts[a] > 0]
            for a0 in members:
                punctured = [a for a in members if a != a0]
                active_punctured = [a for a in punctured if counts[a] > 0]
                zero_punctured = [a for a in punctured if counts[a] == 0]
                record = {
                    "P": p,
                    "halfclass": name,
                    "legendre_sign": sign,
                    "halfclass_size": h,
                    "puncture_residue": a0,
                    "puncture_support_count": counts[a0],
                    "active_halfclass_support_count": len(active_members),
                    "active_punctured_support_count": len(active_punctured),
                    "zero_punctured_support_count": len(zero_punctured),
                    "punctured_zero_support_degeneracy": len(active_punctured) == 0,
                    "first_active_punctured_residues": active_punctured[:8],
                    "first_zero_punctured_residues": zero_punctured[:8],
                }
                records.append(record)
                if record["punctured_zero_support_degeneracy"]:
                    degeneracy_records.append(record)

    by_low_activity = sorted(
        records,
        key=lambda item: (
            item["active_punctured_support_count"],
            item["zero_punctured_support_count"],
            item["P"],
            item["puncture_residue"],
        ),
    )
    min_active = by_low_activity[0]["active_punctured_support_count"] if by_low_activity else None
    return {
        "min_p": min_p,
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "punctured_halfclass_instances_checked": len(records),
        "min_active_punctured_support_count": min_active,
        "degenerate_instances_found": len(degeneracy_records),
        "degenerate_instances": degeneracy_records[:top],
        "top_low_activity_records": by_low_activity[:top],
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录对数独立退化公式。"""
    return [
        {
            "item": "residue prime support",
            "formula": "S_a(P)={ell prime: ell<=P^2, ell!=P, ell=a mod P}",
        },
        {
            "item": "theta support product",
            "formula": "theta_a=log(prod_{ell in S_a(P)} ell)",
        },
        {
            "item": "log-prime independence",
            "formula": "theta_a=theta_b and a!=b imply S_a(P)=S_b(P)=empty",
        },
        {
            "item": "exact punctured flatness degeneration",
            "formula": "P>=7 and theta_{a0u}=c for all u!=1 in Q imply c=0 and S_{a0u}=empty for every u!=1",
        },
        {
            "item": "new hardpoint",
            "formula": "exclude punctured half-class zero-support degeneracy or register ColumnCRT/PDEC/moving-family",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": PREVIOUS_TARGET,
            "route": NEXT_TARGET,
            "status": "sharpened but open",
            "meaning": "全配对角色轨道锁若是精确平铺，则正平铺由素数对数独立性排除，只剩 punctured 半类全零支撑退化。",
        },
        {
            "branch": "positive exact half-class flatness",
            "route": "log-prime product independence",
            "status": "closed as algebraic identity",
            "meaning": "不同 residue 的素数支撑互不相交，两个正 theta 值不可能完全相等。",
        },
        {
            "branch": "all-pair orbit lock",
            "route": "punctured zero-support degeneracy",
            "status": "not excluded in corpus",
            "meaning": "剩余出口要求同半类除缺孔外没有任何 P^2 内素数到达。",
        },
        {
            "branch": NEXT_TARGET,
            "route": "exclude zero-support degeneracy or route to ColumnCRT/PDEC/moving-family",
            "status": "not proved in corpus",
            "meaning": "这是当前非实 AP 分支的最新最窄接口。",
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
            "PreviousTwistPairTargetImported",
            imported,
            imported,
            "上一层把 ratio-Fourier 锁压成二次扭曲角色配对轨道锁。",
            PREVIOUS_TARGET,
        ),
        row(
            "LogPrimeProductIndependenceClosed",
            True,
            True,
            "不同 residue 的 theta 精确相等只能同时为空支撑。",
            "none",
        ),
        row(
            "PositiveExactPuncturedFlatnessExcluded",
            True,
            True,
            "P>=7 时，punctured 半类的正精确平铺与唯一分解矛盾。",
            "none",
        ),
        row(
            "OrbitLockRoutedToZeroSupportDegeneracy",
            True,
            True,
            "精确轨道锁若持久，只能退化为 punctured 半类全零支撑。",
            NEXT_TARGET,
        ),
        row(
            "PuncturedHalfClassZeroSupportDegeneracyExcluded",
            False,
            False,
            "当前语料尚未自足排斥同半类除缺孔外全无 P^2 内素数到达。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只排除正精确平铺，不证明行/列命题。",
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
    diagnostic = finite_support_diagnostic(max_p, top)
    return {
        "certificate_type": "prime_matrix_halfclass_log_independence_degeneracy_router",
        "status": "twist_pair_orbit_lock_routed_to_log_independence_zero_support_degeneracy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "quadratic_margin_still_required": QUADRATIC_MARGIN_TARGET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "finite_diagnostic": diagnostic,
        "log_prime_product_independence_closed": True,
        "positive_exact_punctured_flatness_excluded": True,
        "orbit_lock_routed_to_zero_support_degeneracy": True,
        "punctured_halfclass_zero_support_degeneracy_excluded": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC`。"
            "若 punctured 半类出现精确平铺，则任意两个不同 residue 的 theta 值相等。"
            "但 theta 是对应素数集合乘积的对数；唯一分解给出不同 residue 的正 theta 值不可能精确相等。"
            "因此精确轨道锁只能退化为 `c=0` 且同半类除缺孔外全部 residue 在 `P^2` 内无素数到达。"
            "最新硬点压成 `PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["finite_diagnostic"]
    lines = [
        "# Prime Matrix Half-class Log Independence Degeneracy Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"log_prime_product_independence_closed={fmt_bool(result['log_prime_product_independence_closed'])}",
        f"positive_exact_punctured_flatness_excluded={fmt_bool(result['positive_exact_punctured_flatness_excluded'])}",
        f"orbit_lock_routed_to_zero_support_degeneracy={fmt_bool(result['orbit_lock_routed_to_zero_support_degeneracy'])}",
        f"punctured_halfclass_zero_support_degeneracy_excluded={fmt_bool(result['punctured_halfclass_zero_support_degeneracy_excluded'])}",
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
        "有限扫描只用于定位零支撑退化，不作为无限证明输入。",
        "",
        "```text",
        f"min_p={diagnostic['min_p']}",
        f"max_p={diagnostic['max_p']}",
        f"prime_moduli_checked={diagnostic['prime_moduli_checked']}",
        f"punctured_halfclass_instances_checked={diagnostic['punctured_halfclass_instances_checked']}",
        f"min_active_punctured_support_count={diagnostic['min_active_punctured_support_count']}",
        f"degenerate_instances_found={diagnostic['degenerate_instances_found']}",
        "```",
        "",
        "### 3.1 最接近零支撑退化的记录",
        "",
        "| P | halfclass | puncture | puncture support | active punctured | zero punctured | first active punctured residues |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in diagnostic["top_low_activity_records"]:
        lines.append(
            f"| `{item['P']}` | `{item['halfclass']}` | `{item['puncture_residue']}` | "
            f"`{item['puncture_support_count']}` | "
            f"`{item['active_punctured_support_count']}` | "
            f"`{item['zero_punctured_support_count']}` | "
            f"`{item['first_active_punctured_residues']}` |"
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
        "审稿边界：本文件排除的是精确正平铺。它没有证明 punctured 半类全零支撑退化不可能，也没有排斥相应 ColumnCRT/PDEC/moving-family 出口。",
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
    parser.add_argument("--top", type=int, default=12, help="报告前若干条低活动记录")
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.max_p, args.top)
    write_outputs(result)
    summary = {
        "status": result["status"],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "min_active_punctured_support_count": result["finite_diagnostic"]["min_active_punctured_support_count"],
        "degenerate_instances_found": result["finite_diagnostic"]["degenerate_instances_found"],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
