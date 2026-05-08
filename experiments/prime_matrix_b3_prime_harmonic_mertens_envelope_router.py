#!/usr/bin/env python3
"""Prime Matrix B=3 prime-harmonic Mertens 包络路由器。

用法示例：
  python3 experiments/prime_matrix_b3_prime_harmonic_mertens_envelope_router.py

输出：
  docs/monograph/prime-matrix-b3-prime-harmonic-mertens-envelope-router.json
  docs/monograph/prime-matrix-b3-prime-harmonic-mertens-envelope-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-alternating-boundary-terminal-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-prime-harmonic-mertens-envelope-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-prime-harmonic-mertens-envelope-router.md"

MERTENS_ATOM = "B3PrimeHarmonicMertensUniformEnvelopePGe100000"
LOW_ATOM = "B3LowPrimeStepFiniteLedgerXLt286PGe100000"
HIGH_ATOM = "ExplicitPrimeReciprocalMertensEnvelopeXGe286"
VARIATION_ATOM = "B3BoundaryVariationOnePercentTransferLedger"
STANDARD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TAIL_START = 100_000
ALPHA = 0.43
LOW_X_CUTOFF = 286


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def prime_list_below(limit: int) -> list[int]:
    """列出小于 limit 的素数。"""
    primes: list[int] = []
    for candidate in range(2, limit):
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
    return primes


def replacement_pair() -> str:
    """写出 Mertens 包络替换包。"""
    return f"({LOW_ATOM} AND {HIGH_ATOM})"


def replace_mertens_atom(text: str) -> str:
    """替换 prime-harmonic Mertens 包络原子。"""
    return text.replace(MERTENS_ATOM, replacement_pair())


def low_prime_ledger() -> dict[str, Any]:
    """生成低素数有限阶梯账本。"""
    primes = prime_list_below(LOW_X_CUTOFF)
    z0 = TAIL_START**ALPHA
    active_low_primes_at_tail_start = [prime for prime in primes if prime < z0]
    return {
        "cutoff_x": LOW_X_CUTOFF,
        "tail_start": TAIL_START,
        "alpha": ALPHA,
        "z_at_tail_start": z0,
        "prime_count_below_cutoff": len(primes),
        "largest_prime_below_cutoff": primes[-1],
        "prime_count_active_at_tail_start": len(active_low_primes_at_tail_start),
        "largest_active_prime_at_tail_start": active_low_primes_at_tail_start[-1],
        "low_step_mass_total_below_cutoff": sum(1.0 / prime for prime in primes),
        "low_step_mass_active_at_tail_start": sum(1.0 / prime for prime in active_low_primes_at_tail_start),
        "finite_table_closed": True,
    }


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], low_ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 prime-harmonic Mertens 包络判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == MERTENS_ATOM and MERTENS_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    boundary_split_available = bool(previous.get("alternating_boundary_remainder_atom_reduced"))
    scale_transfer_closed = True
    low_closed = bool(low_ledger["finite_table_closed"])
    high_closed = False
    reduced = active and guard and boundary_split_available and scale_transfer_closed and low_closed
    return [
        row(
            "PrimeHarmonicMertensGateActive",
            active,
            False,
            "上一层最新最窄点是 prime-harmonic/Mertens 统一包络。",
            MERTENS_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的筛主系数误差，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "BoundarySplitAvailable",
            boundary_split_available,
            True,
            "交错边界余项已经拆成一维 Mertens 包络与 B=3 边界变差传递。",
            "无上游拆分剩余。",
        ),
        row(
            "LogScaleTransferClosed",
            scale_transfer_closed,
            True,
            "变量 x=P^u 把 H_P(u)=sum_{p<P^u}1/p 精确转为素数倒数部分和，u 只改变阈值。",
            "无尺度变换剩余。",
        ),
        row(
            "LowPrimeStepFiniteLedgerClosed",
            low_closed,
            True,
            "P^u<286 的阶梯部分只涉及有限素数表，可逐点精确保留，不进入渐近误差。",
            LOW_ATOM,
        ),
        row(
            "HighXExplicitMertensEnvelopeStillNeeded",
            high_closed,
            False,
            "P^u>=286 的统一包络需要显式素数倒数 Mertens 定理或自足证明。",
            HIGH_ATOM,
        ),
        row(
            "MertensEnvelopeSplitToLowFiniteAndHighExplicit",
            reduced,
            False,
            "Mertens 包络原子被压成低素数有限阶梯账本和高阈值显式 reciprocal-prime Mertens 包络。",
            f"{LOW_ATOM} AND {HIGH_ATOM}",
        ),
        row(
            HIGH_ATOM,
            False,
            False,
            "需要引用或证明 sum_{p<=x}1/p=log log x+B1+E(x) 的显式统一误差，至少覆盖 x>=286。",
            HIGH_ATOM,
        ),
        row(
            VARIATION_ATOM,
            False,
            False,
            "高阈值 Mertens 包络还必须与 B=3 边界变差传递合成，才能关闭 1% 余项。",
            VARIATION_ATOM,
        ),
        row(
            STANDARD_IMPORT_ATOM,
            False,
            False,
            "标准 Rosser-Iwaniec beta-sieve 基本引理可外部替代高阈值 Mertens 与变差合成。",
            STANDARD_IMPORT_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。",
            EXTERNAL_ROUGH_ATOM,
        ),
        row(
            EXTERNAL_DIBFI_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_DIBFI_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 B=3 prime-harmonic Mertens 包络路由。"""
    previous = load_json(paths["previous"])
    low_ledger = low_prime_ledger()
    rows = build_rows(previous, low_ledger)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "MertensEnvelopeSplitToLowFiniteAndHighExplicit"
    )
    latest_self = replace_mertens_atom(previous.get("latest_self_contained_basis", ""))
    latest_cond = replace_mertens_atom(previous.get("latest_conditional_basis", ""))
    latest_global = replace_mertens_atom(previous.get("latest_global_with_external_basis", ""))
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_prime_harmonic_mertens_envelope_router",
        "status": "mertens_envelope_split_low_finite_high_explicit_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "prime_harmonic_mertens_envelope_reduced": reduced,
        "low_prime_step_finite_ledger_closed": True,
        "explicit_prime_reciprocal_mertens_envelope_proved": False,
        "boundary_variation_transfer_proved": False,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "standard_beta_sieve_import_accepted": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {MERTENS_ATOM: replacement_pair()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": HIGH_ATOM,
        "secondary_priority": VARIATION_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "low_prime_ledger": low_ledger,
        "standard_source_boundary": (
            "Rosser-Schoenfeld/Dusart type explicit bounds for reciprocal prime sums would close "
            "the high-x envelope as an external standard input; an internal self-contained proof is not yet present."
        ),
        "plain_conclusion": (
            "prime-harmonic/Mertens 包络又被压窄一层：低阈值 P^u<286 是有限素数阶梯表，可精确保留；"
            "真正剩余是 x>=286 的显式素数倒数 Mertens 统一误差，以及它与 B=3 边界变差的合成。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    low = result["low_prime_ledger"]
    lines = [
        "# Prime Matrix B=3 prime-harmonic Mertens 包络路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"prime_harmonic_mertens_envelope_reduced={fmt_bool(result['prime_harmonic_mertens_envelope_reduced'])}",
        f"low_prime_step_finite_ledger_closed={fmt_bool(result['low_prime_step_finite_ledger_closed'])}",
        (
            "explicit_prime_reciprocal_mertens_envelope_proved="
            f"{fmt_bool(result['explicit_prime_reciprocal_mertens_envelope_proved'])}"
        ),
        f"boundary_variation_transfer_proved={fmt_bool(result['boundary_variation_transfer_proved'])}",
        f"beta_sieve_main_coefficient_99pct_proved={fmt_bool(result['beta_sieve_main_coefficient_99pct_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 低阈值有限账本",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| cutoff x | {low['cutoff_x']} |",
        f"| z at P=100000 | {low['z_at_tail_start']:.6f} |",
        f"| primes below cutoff | {low['prime_count_below_cutoff']} |",
        f"| largest prime below cutoff | {low['largest_prime_below_cutoff']} |",
        f"| active primes at tail start | {low['prime_count_active_at_tail_start']} |",
        f"| largest active prime at tail start | {low['largest_active_prime_at_tail_start']} |",
        f"| low step mass below cutoff | {low['low_step_mass_total_below_cutoff']:.12f} |",
        f"| active low step mass at tail start | {low['low_step_mass_active_at_tail_start']:.12f} |",
        "",
        "## 2. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        result["standard_source_boundary"],
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "global/external 宽口径输入基：",
            "",
            "```text",
            result["latest_global_with_external_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            f"先攻 `{result['next_priority']}`，再攻 `{result['secondary_priority']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
