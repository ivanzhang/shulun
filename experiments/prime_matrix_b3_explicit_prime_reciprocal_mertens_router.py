#!/usr/bin/env python3
"""Prime Matrix B=3 显式素数倒数 Mertens 包络路由器。

用法示例：
  python3 experiments/prime_matrix_b3_explicit_prime_reciprocal_mertens_router.py

输出：
  docs/monograph/prime-matrix-b3-explicit-prime-reciprocal-mertens-router.json
  docs/monograph/prime-matrix-b3-explicit-prime-reciprocal-mertens-router.md
"""

from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-prime-harmonic-mertens-envelope-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.md"

HIGH_ATOM = "ExplicitPrimeReciprocalMertensEnvelopeXGe286"
FINITE_ATOM = "B3FinitePrimeReciprocalStepLedger286To10371PGe100000"
INTERNAL_TAIL_ATOM = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
EXTERNAL_CLOSED_ATOM = "DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted"
VARIATION_ATOM = "B3BoundaryVariationOnePercentTransferLedger"
STANDARD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
TAIL_START_P = 100_000
FINITE_LOW_X = 286
DUSART_TAIL_START_X = 10_372
DUSART_SOURCE = "https://arxiv.org/abs/1002.0442"
MEISSEL_MERTENS_B1 = 0.2614972128476428


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


def sieve_primes(limit: int) -> list[int]:
    """生成不超过 limit 的素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (
            ((limit - start) // value) + 1
        )
    return [idx for idx, flag in enumerate(flags) if flag]


def prefix_reciprocals(primes: list[int]) -> list[float]:
    """计算素数倒数前缀和。"""
    total = 0.0
    prefix: list[float] = []
    for prime in primes:
        total += 1.0 / prime
        prefix.append(total)
    return prefix


def prime_reciprocal_sum(x: int, primes: list[int], prefix: list[float]) -> float:
    """计算 sum_{p<=x} 1/p。"""
    index = bisect.bisect_right(primes, x) - 1
    if index < 0:
        return 0.0
    return prefix[index]


def dusart_error(log_x: float) -> float:
    """Dusart 型素数倒数和误差项。"""
    return 1.0 / (10.0 * log_x**2) + 4.0 / (15.0 * log_x**3)


def finite_step_ledger(low_x: int, high_x: int) -> dict[str, Any]:
    """生成 low_x<=x<high_x 的有限阶梯账本。"""
    primes = sieve_primes(high_x)
    prefix = prefix_reciprocals(primes)
    segment_primes = [prime for prime in primes if low_x <= prime < high_x]

    # 该误差审计只用于定位小 x 尖峰；B1 的自足区间证明仍属于尾段 Mertens 定理原子。
    worst_abs = {
        "x": None,
        "error": 0.0,
        "abs_error": 0.0,
        "where": None,
    }
    for x in range(low_x, high_x):
        value = prime_reciprocal_sum(x, primes, prefix)
        error = value - math.log(math.log(x)) - MEISSEL_MERTENS_B1
        if abs(error) > worst_abs["abs_error"]:
            worst_abs = {
                "x": x,
                "error": error,
                "abs_error": abs(error),
                "where": "integer_endpoint",
            }

    p_threshold = math.ceil(high_x ** (1.0 / ALPHA))
    z_tail_start = TAIL_START_P**ALPHA
    return {
        "low_x": low_x,
        "high_x_exclusive": high_x,
        "alpha": ALPHA,
        "tail_start_p": TAIL_START_P,
        "z_at_tail_start_p": z_tail_start,
        "p_threshold_for_tail_atoms": p_threshold,
        "prime_count_in_segment": len(segment_primes),
        "first_prime_in_segment": segment_primes[0],
        "last_prime_in_segment": segment_primes[-1],
        "reciprocal_mass_in_segment": sum(1.0 / prime for prime in segment_primes),
        "prefix_mass_below_high_x": prime_reciprocal_sum(high_x - 1, primes, prefix),
        "meissel_mertens_b1_for_audit_only": MEISSEL_MERTENS_B1,
        "worst_abs_error_against_b1_in_finite_segment": worst_abs,
        "finite_step_ledger_closed": True,
    }


def tail_theorem_ledger(start_x: int) -> dict[str, Any]:
    """生成 Dusart 外部尾段定理的参数账本。"""
    log_start = math.log(start_x)
    error_start = dusart_error(log_start)
    return {
        "tail_start_x": start_x,
        "log_tail_start_x": log_start,
        "dusart_error_at_tail_start": error_start,
        "dusart_error_decreases_for_x_ge_start": True,
        "external_source": DUSART_SOURCE,
        "external_theorem_parameter_match_closed": True,
        "self_contained_proof_present_in_repo": False,
    }


def self_replacement() -> str:
    """写出完全自足路线的替换包。"""
    return f"({FINITE_ATOM} AND {INTERNAL_TAIL_ATOM})"


def external_replacement() -> str:
    """写出外部定理路线的替换包。"""
    return EXTERNAL_CLOSED_ATOM


def replace_atom(text: str, replacement: str) -> str:
    """替换显式 Mertens 包络原子。"""
    return text.replace(HIGH_ATOM, replacement)


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


def build_rows(
    previous: dict[str, Any],
    finite: dict[str, Any],
    tail: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成显式 reciprocal-prime Mertens 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == HIGH_ATOM and HIGH_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    previous_split = bool(previous.get("prime_harmonic_mertens_envelope_reduced"))
    finite_closed = bool(finite["finite_step_ledger_closed"])
    tail_external_matched = bool(tail["external_theorem_parameter_match_closed"])
    external_route_closed = active and guard and previous_split and finite_closed and tail_external_matched
    return [
        row(
            "ExplicitPrimeReciprocalMertensGateActive",
            active,
            False,
            "上一层最新最窄点是 x>=286 的显式素数倒数 Mertens 包络。",
            HIGH_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的筛主系数误差，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "PreviousLowHighSplitAvailable",
            previous_split,
            True,
            "prime-harmonic 包络已拆成低素数有限账本与高阈值显式 Mertens 包络。",
            "无上游拆分剩余。",
        ),
        row(
            "FinitePrimeStepLedger286To10371Closed",
            finite_closed,
            True,
            "286<=x<10372 只含有限个素数跳点，作为精确阶梯测度保留，不消耗渐近误差。",
            FINITE_ATOM,
        ),
        row(
            "DusartTailParameterMatchXGe10372Closed",
            tail_external_matched,
            False,
            "x>=10372 与 Dusart reciprocal-prime 显式 Mertens 定理的有效区间匹配；这是外部定理匹配，不是仓库内证明。",
            EXTERNAL_CLOSED_ATOM,
        ),
        row(
            "ExternalRouteForExplicitMertensEnvelopeClosed",
            external_route_closed,
            False,
            "若接受 Dusart/Rosser-Schoenfeld 型外部显式定理，ExplicitPrimeReciprocalMertensEnvelopeXGe286 可关闭。",
            EXTERNAL_CLOSED_ATOM,
        ),
        row(
            "SelfContainedTailProofStillOpen",
            False,
            False,
            "完全自足路线仍必须内联证明 x>=10372 的 reciprocal-prime Mertens 显式误差。",
            INTERNAL_TAIL_ATOM,
        ),
        row(
            VARIATION_ATOM,
            False,
            False,
            "Mertens 包络关闭后，还需证明 B=3 admissible 区域的边界变差传递小于 1% f(s)。",
            VARIATION_ATOM,
        ),
        row(
            STANDARD_IMPORT_ATOM,
            False,
            False,
            "标准 Rosser-Iwaniec beta-sieve 基本引理可外部替代整个 B=3 边界包。",
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
    """执行显式 reciprocal-prime Mertens 包络路由。"""
    previous = load_json(paths["previous"])
    finite = finite_step_ledger(FINITE_LOW_X, DUSART_TAIL_START_X)
    tail = tail_theorem_ledger(DUSART_TAIL_START_X)
    rows = build_rows(previous, finite, tail)
    external_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ExternalRouteForExplicitMertensEnvelopeClosed"
    )
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), self_replacement())
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), external_replacement())
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""), external_replacement())
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_explicit_prime_reciprocal_mertens_router",
        "status": "explicit_reciprocal_mertens_external_closed_self_contained_tail_proof_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "explicit_prime_reciprocal_mertens_external_closed": external_closed,
        "explicit_prime_reciprocal_mertens_self_contained_proved": False,
        "finite_prime_step_ledger_286_to_10371_closed": bool(finite["finite_step_ledger_closed"]),
        "dusart_tail_parameter_match_closed": bool(tail["external_theorem_parameter_match_closed"]),
        "beta_sieve_main_coefficient_99pct_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {HIGH_ATOM: self_replacement()},
        "replacement_external": {HIGH_ATOM: external_replacement()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": INTERNAL_TAIL_ATOM,
        "secondary_priority": VARIATION_ATOM,
        "conditional_next_priority": VARIATION_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "finite_step_ledger": finite,
        "tail_theorem_ledger": tail,
        "standard_source_boundary": (
            "Dusart/Rosser-Schoenfeld type reciprocal-prime Mertens estimates close the "
            "x>=10372 tail as an external theorem. A fully self-contained proof would have "
            "to reproduce that explicit PNT/Mertens machinery inside this project."
        ),
        "plain_conclusion": (
            "显式素数倒数 Mertens 包络被压到最窄边界：286<=x<10372 是有限阶梯账本，"
            "x>=10372 可由 Dusart 型外部定理关闭；但完全自足路线仍缺少该外部定理的内联证明。"
            "因此外部定理版下一点转为 B=3 边界变差传递，自足版下一点则是 reciprocal-prime "
            "Mertens 尾段证明附录。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    self_repl = next(iter(result["replacement_self_contained"].items()))
    ext_repl = next(iter(result["replacement_external"].items()))
    finite = result["finite_step_ledger"]
    tail = result["tail_theorem_ledger"]
    worst = finite["worst_abs_error_against_b1_in_finite_segment"]
    lines = [
        "# Prime Matrix B=3 显式素数倒数 Mertens 包络路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "explicit_prime_reciprocal_mertens_external_closed="
            f"{fmt_bool(result['explicit_prime_reciprocal_mertens_external_closed'])}"
        ),
        (
            "explicit_prime_reciprocal_mertens_self_contained_proved="
            f"{fmt_bool(result['explicit_prime_reciprocal_mertens_self_contained_proved'])}"
        ),
        f"finite_prime_step_ledger_286_to_10371_closed={fmt_bool(result['finite_prime_step_ledger_286_to_10371_closed'])}",
        f"dusart_tail_parameter_match_closed={fmt_bool(result['dusart_tail_parameter_match_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 拆分律",
        "",
        "完全自足路线：",
        "",
        "```text",
        self_repl[0],
        "  =>",
        self_repl[1],
        "```",
        "",
        "外部定理路线：",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        result["standard_source_boundary"],
        "",
        "## 2. 有限阶梯账本",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| low x | {finite['low_x']} |",
        f"| high x exclusive | {finite['high_x_exclusive']} |",
        f"| primes in segment | {finite['prime_count_in_segment']} |",
        f"| first prime in segment | {finite['first_prime_in_segment']} |",
        f"| last prime in segment | {finite['last_prime_in_segment']} |",
        f"| reciprocal mass in segment | {finite['reciprocal_mass_in_segment']:.12f} |",
        f"| prefix mass below high x | {finite['prefix_mass_below_high_x']:.12f} |",
        f"| P threshold where P^alpha reaches 10372 | {finite['p_threshold_for_tail_atoms']} |",
        f"| worst finite B1 audit x | {worst['x']} |",
        f"| worst finite B1 audit error | {worst['error']:.12f} |",
        "",
        "该有限表不是用实验外推无限尾段；它只是把小阈值素数跳点作为精确 Stieltjes 原子保留。",
        "",
        "## 3. Dusart 尾段匹配",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| tail start x | {tail['tail_start_x']} |",
        f"| log tail start | {tail['log_tail_start_x']:.12f} |",
        f"| Dusart error at tail start | {tail['dusart_error_at_tail_start']:.12f} |",
        f"| error decreases for tail | {fmt_bool(tail['dusart_error_decreases_for_x_ge_start'])} |",
        f"| self-contained proof in repo | {fmt_bool(tail['self_contained_proof_present_in_repo'])} |",
        "",
        "外部来源：Dusart, *Estimates of some functions over primes without R.H.*, arXiv:1002.0442。",
        "",
        "## 4. 判定表",
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
            "## 5. 最新输入基",
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
            "## 6. 下一步",
            "",
            (
                f"完全自足路线先攻 `{result['next_priority']}`；"
                f"若接受外部显式 Mertens 定理，则下一点直接转为 `{result['conditional_next_priority']}`。"
            ),
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
