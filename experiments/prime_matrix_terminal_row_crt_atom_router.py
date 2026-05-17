#!/usr/bin/env python3
"""归档终端行/下一行 CRT 原子与平方根素性证书。

用法示例：
  python3 experiments/prime_matrix_terminal_row_crt_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-terminal-row-crt-atom-router.json

输出：
  data/prime-matrix-terminal-row-crt-atom-ledger.json
  docs/monograph/prime-matrix-terminal-row-crt-atom-router.json
  docs/monograph/prime-matrix-terminal-row-crt-atom-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

OUT_LEDGER = DATA / "prime-matrix-terminal-row-crt-atom-ledger.json"
OUT_JSON = DOCS / "prime-matrix-terminal-row-crt-atom-router.json"
OUT_MD = DOCS / "prime-matrix-terminal-row-crt-atom-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-predecessor-gap-pcrt-uniformity-router.json",
    DOCS / "prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json",
    DOCS / "prime-matrix-early-zero-gap-crt-asymmetry-router.json",
    DOCS / "prime-matrix-beta-gap-page-sparsity-router.json",
    DOCS / "claim-status-table.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    PAPER,
]

NEXT_TARGET = "TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer"
FALLBACK_TARGET = "PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier"
PAGE_TARGET = "PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget"


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    primes: list[int] = []
    for x in range(2, n + 1):
        composite = False
        for p in primes:
            if p * p > x:
                break
            if x % p == 0:
                composite = True
                break
        if not composite:
            primes.append(x)
    return primes


def is_prime(n: int) -> bool:
    """朴素素性测试，样本很小。"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def next_prime_after(p: int) -> int:
    """求 p 后的下一个素数。"""
    n = p + 1
    while not is_prime(n):
        n += 1
    return n


def prod(values: list[int]) -> int:
    """整数乘积。"""
    result = 1
    for value in values:
        result *= value
    return result


def small_factor(n: int, primes: list[int]) -> int | None:
    """返回 n 的第一个小素因子；没有则返回 None。"""
    for p in primes:
        if n % p == 0:
            return p
    return None


def crt_vector(n: int, primes: list[int]) -> dict[str, int]:
    """登记 n 在小素数模下的余数向量。"""
    return {str(p): n % p for p in primes}


def unit_residues(modulus: int, primes: list[int]) -> list[int]:
    """完整 CRT 周期中的小素单位残基。"""
    residues = []
    for n in range(1, modulus + 1):
        if all(n % p for p in primes):
            residues.append(n if n < modulus else 0)
    return residues


def analyze_p(P: int, targets: list[int]) -> dict[str, Any]:
    """分析用户指定的 P=5,7 终端原子。"""
    base_primes = primes_upto(P)
    modulus = prod(base_primes)
    next_p = next_prime_after(P)
    last_row = list(range(P * P - P + 1, P * P + 1))
    next_row = list(range(P * P + 1, P * P + P + 1))
    last_nonp = [n for n in last_row if n % P != 0]
    next_nonp = [n for n in next_row if n % P != 0]
    last_units = [n for n in last_nonp if small_factor(n, base_primes) is None]
    next_units = [n for n in next_nonp if small_factor(n, base_primes) is None]
    residues = unit_residues(modulus, base_primes)

    target_rows = []
    for n in targets:
        factor = small_factor(n, base_primes)
        target_rows.append(
            {
                "n": n,
                "position": (
                    "last_row"
                    if n in last_row
                    else "next_row"
                    if n in next_row
                    else "outside_two_terminal_rows"
                ),
                "crt_vector_mod_primes_le_P": crt_vector(n, base_primes),
                "small_factor_le_P": factor,
                "is_unit_mod_M_le_P": factor is None,
                "forced_prime_by_terminal_sqrt_gate": factor is None
                and (1 < n < next_p * next_p),
                "mirror_mod_M": (-n) % modulus,
            }
        )

    return {
        "P": P,
        "base_primes": base_primes,
        "M_le_P": modulus,
        "phi_M_le_P": len(residues),
        "next_prime": next_p,
        "last_row": last_row,
        "next_row": next_row,
        "last_row_nonP_columns": last_nonp,
        "next_row_nonP_columns": next_nonp,
        "last_row_units": last_units,
        "next_row_units": next_units,
        "unit_residues_in_one_period": residues,
        "target_atom_checks": target_rows,
        "complete_wheel_reflection_pairs_for_targets": [
            [item["n"], item["mirror_mod_M"]] for item in target_rows
        ],
        "all_targets_small_factor_absorption_impossible": all(
            item["small_factor_le_P"] is None for item in target_rows
        ),
    }


def sha256(path: Path) -> str:
    """计算依赖哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    hashes: dict[str, str] = {}
    for path in SOURCE_FILES:
        if path.exists():
            hashes[str(path.relative_to(ROOT))] = sha256(path)
    return hashes


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def build_rows() -> list[dict[str, Any]]:
    """构造判定表。"""
    return [
        {
            "gate": "SpecifiedTerminalAtomsSmallFactorAbsorptionImpossible",
            "closed": True,
            "proved": True,
            "meaning": "23,29,43,47,53 等指定原子在对应小素 CRT 向量中没有零坐标，不能被 <=P 小素数整除。",
            "remaining": "none for specified atoms",
        },
        {
            "gate": "TerminalSqrtGate",
            "closed": True,
            "proved": True,
            "meaning": "若 n<p_next^2 且 n 对所有 q<=P 非零，则 n 不能为合数，故为素数。",
            "remaining": "none for existing reduced atoms",
        },
        {
            "gate": "CompleteWheelSymmetryIdentity",
            "closed": True,
            "proved": True,
            "meaning": "完整 M_{<=P} 周期中单位残基按 CRT 周期重复，并在 n->-n 下反射配对。",
            "remaining": "full-period identity only",
        },
        {
            "gate": "FullWheelSymmetryLocalizesToTerminalRows",
            "closed": False,
            "proved": False,
            "meaning": "完整周期单位残基均匀性不能自动保证任意给定短行中有单位残基。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "GlobalTerminalRowNoMissingPrimeProved",
            "closed": False,
            "proved": False,
            "meaning": "要推广到全体奇素数，仍需证明末行或下一行总有 reduced atom，等价于短区间/点态 AP 输入。",
            "remaining": FALLBACK_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosed",
            "closed": False,
            "proved": False,
            "meaning": "本步只把用户给定终端例子变成严格 CRT 原子证书，不闭合全局行/列命题。",
            "remaining": PAGE_TARGET,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    examples = [
        analyze_p(5, [23, 29]),
        analyze_p(7, [43, 47, 53]),
    ]
    latest_basis = (
        "(TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer OR "
        "PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2 OR "
        "PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget OR "
        "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR "
        "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND "
        "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND "
        "ExplicitModelGapAndFiniteDPRCLedger AND "
        "RatePreservationLedger_FOR_moving_atom_packet AND "
        "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
    )
    return {
        "certificate_type": "prime_matrix_terminal_row_crt_atom_router",
        "status": "specified_terminal_atoms_closed_but_global_localization_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "next_direct_attack_target": NEXT_TARGET,
        "fallback_target": FALLBACK_TARGET,
        "page_frontier_target": PAGE_TARGET,
        "examples": examples,
        "lemmas": [
            {
                "name": "specified atom CRT contradiction",
                "statement": "若指定 n 在所有 q<=P 下均非零，则假设 n 可被 q<=P 整除立即与其 CRT 坐标矛盾。",
            },
            {
                "name": "terminal sqrt gate",
                "statement": "若 1<n<p_next^2 且 gcd(n,M_{<=P})=1，则 n 为素数；否则最小素因子至少 p_next，合数至少 p_next^2。",
            },
            {
                "name": "complete wheel non-localization",
                "statement": "完整 CRT 周期中单位残基的均匀和反射只给全周期身份，不给初始 P x P 或末端短行的点态存在性。",
            },
        ],
        "rows": build_rows(),
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "P=5 的 23,29 与 P=7 的 43,47,53 都是对应 M_{<=P} 周期中的单位原子；"
            "假设它们能被 <=P 小素数整除，与 CRT 余数向量直接矛盾。并且它们都小于下一素数平方，"
            "所以单位原子一旦存在就被平方根门强制为真实素数。可推广的严格部分是这个原子级引理；"
            "不可跳过的开放部分是证明任意大 P 的目标短行中必存在这样的单位原子。完整 CRT 周期对称性"
            "本身只给全周期均匀，不给短行局部化，因此全局路线仍回到局部化 P-CRT/Linnik=2、AP 零点包、"
            "Page 稀疏 moving singleton/非实零包残差或 signed payload/PDEC 前沿。"
        ),
        "latest_strict_activity_basis": latest_basis,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix 终端行 CRT 原子路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        f"fallback_target={result['fallback_target']}",
        f"page_frontier_target={result['page_frontier_target']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 用户例子核查",
        "",
    ]
    for example in result["examples"]:
        lines += [
            f"### P={example['P']}",
            "",
            "```text",
            f"M_le_P={example['M_le_P']}",
            f"base_primes={example['base_primes']}",
            f"next_prime={example['next_prime']}",
            f"last_row={example['last_row']}",
            f"next_row={example['next_row']}",
            f"last_row_units={example['last_row_units']}",
            f"next_row_units={example['next_row_units']}",
            "```",
            "",
            "| n | position | CRT vector mod q<=P | small factor <=P | unit | forced prime | mirror mod M |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for item in example["target_atom_checks"]:
            lines.append(
                f"| `{item['n']}` | `{item['position']}` | "
                f"`{table_cell(item['crt_vector_mod_primes_le_P'])}` | "
                f"`{item['small_factor_le_P']}` | `{fmt_bool(item['is_unit_mod_M_le_P'])}` | "
                f"`{fmt_bool(item['forced_prime_by_terminal_sqrt_gate'])}` | "
                f"`{item['mirror_mod_M']}` |"
            )
        lines.append("")

    lines += [
        "## 2. 可推广的严格引理",
        "",
        "| name | statement |",
        "| --- | --- |",
    ]
    for lemma in result["lemmas"]:
        lines.append(f"| `{table_cell(lemma['name'])}` | {table_cell(lemma['statement'])} |")

    lines += [
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| `{table_cell(row['gate'])}` | `{fmt_bool(row['closed'])}` | "
            f"`{fmt_bool(row['proved'])}` | {table_cell(row['meaning'])} | "
            f"{table_cell(row['remaining'])} |"
        )

    lines += [
        "",
        "## 4. 最新活动基",
        "",
        "```text",
        result["latest_strict_activity_basis"],
        "```",
        "",
        "审稿边界：本文件没有证明短行单位原子存在性、Linnik=2 型点态 AP、Page moving singleton 排斥、非实零包残差预算、signed payload、PDEC scope 或 DStructure/Rankin 晋级门。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "fallback_target": result["fallback_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
