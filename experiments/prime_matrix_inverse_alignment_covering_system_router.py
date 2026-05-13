#!/usr/bin/env python3
"""研究 xP+r 小素因子覆盖的逆元对齐系统。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_covering_system_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-covering-system-router.json

输出：
  data/inverse-alignment-covering-system-sample-ledger.json
  docs/monograph/prime-matrix-inverse-alignment-covering-system-router.json
  docs/monograph/prime-matrix-inverse-alignment-covering-system-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-covering-system-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-covering-system-router.md"
OUT_LEDGER = DATA / "inverse-alignment-covering-system-sample-ledger.json"

SEARCH_BOUND = 200_000
LOWER_BOUND_VERIFY_LIMIT = 199


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def primes_upto(n: int) -> list[int]:
    """生成不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for m in range(p * p, n + 1, p):
                sieve[m] = False
    return [i for i, ok in enumerate(sieve) if ok]


def is_prime(n: int) -> bool:
    """确定性试除判素；本脚本只用于小范围证书。"""
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


def primorial_below(P: int) -> int:
    """计算小于 P 的素数乘积。"""
    value = 1
    for q in primes_upto(P - 1):
        value *= q
    return value


def direct_small_factor_hit(P: int, x: int, r: int) -> bool:
    """直接判断 xP+r 是否有小于 P 的素因子。"""
    n = x * P + r
    return any(n % q == 0 for q in primes_upto(P - 1))


def gcd_system_hit(P: int, x: int, r: int) -> bool:
    """判断用户提出的 gcd 系统是否命中。"""
    if math.gcd(x, r) > 1:
        return True
    for a in range(1, P - 1):
        if math.gcd(a * x + r, P - a) > 1:
            return True
    return False


def first_uncovered_r(P: int, x: int) -> int | None:
    """返回行 x 的第一个未被小素数覆盖的 r。"""
    for r in range(1, P):
        if not direct_small_factor_hit(P, x, r):
            return r
    return None


def minimal_alignment_x(P: int, bound: int) -> int | None:
    """在给定边界内扫描最小对齐行。"""
    for x in range(1, bound + 1):
        if first_uncovered_r(P, x) is None:
            return x
    return None


def inverse_classes_for_r(P: int, r: int) -> list[dict[str, int]]:
    """列出每个 q<P 给出的 x 逆元同余类。"""
    rows: list[dict[str, int]] = []
    for q in primes_upto(P - 1):
        residue = (-r * pow(P % q, -1, q)) % q
        rows.append({"q": q, "x_mod_q": residue, "a_P_mod_q": P % q})
    return rows


def witness_row(P: int, x: int) -> list[dict[str, Any]]:
    """列出一个对齐行中每个 r 的首个小素因子。"""
    rows: list[dict[str, Any]] = []
    for r in range(1, P):
        n = x * P + r
        factor = next(q for q in primes_upto(P - 1) if n % q == 0)
        rows.append({"r": r, "n": n, "first_small_factor": factor, "x_mod_q": x % factor})
    return rows


def verify_gcd_equivalence_samples() -> bool:
    """有限样本核验 gcd 系统与小素因子覆盖一致。"""
    for P in primes_upto(43):
        if P < 3:
            continue
        xs = list(range(1, min(200, SEARCH_BOUND) + 1))
        mx = minimal_alignment_x(P, min(SEARCH_BOUND, 5000))
        if mx is not None:
            xs.append(mx)
        for x in xs:
            for r in range(1, P):
                if direct_small_factor_hit(P, x, r) != gcd_system_hit(P, x, r):
                    return False
    return True


def lower_bound_x_gt_p_verified(limit: int) -> dict[str, Any]:
    """有限核验所有 x<=P 均不形成全覆盖。"""
    failures: list[dict[str, int]] = []
    checked_primes = [P for P in primes_upto(limit) if P >= 3]
    for P in checked_primes:
        for x in range(1, P + 1):
            if first_uncovered_r(P, x) is None:
                failures.append({"P": P, "x": x})
                break
    return {
        "limit": limit,
        "checked_prime_count": len(checked_primes),
        "all_checked_have_no_alignment_x_le_P": not failures,
        "failures": failures,
    }


def sample_ledger() -> dict[str, Any]:
    """生成逆元对齐样本账本。"""
    sample_primes = [P for P in primes_upto(47) if P >= 3]
    rows: list[dict[str, Any]] = []
    for P in sample_primes:
        period = primorial_below(P)
        min_x = minimal_alignment_x(P, SEARCH_BOUND)
        exhaustive = period <= SEARCH_BOUND
        rows.append(
            {
                "P": P,
                "prime_count_below_P": len(primes_upto(P - 1)),
                "period_primorial_below_P": period,
                "search_bound": SEARCH_BOUND,
                "period_exhausted": exhaustive,
                "minimal_alignment_x_in_bound": min_x,
                "alignment_exists_in_bound": min_x is not None,
                "minimal_alignment_gt_P_if_found": None if min_x is None else min_x > P,
                "first_uncovered_r_for_x_equal_P": first_uncovered_r(P, P),
            }
        )
    example_P = 23
    example_x = minimal_alignment_x(example_P, SEARCH_BOUND)
    return {
        "ledger_type": "inverse_alignment_covering_system_sample_ledger",
        "search_bound": SEARCH_BOUND,
        "rows": rows,
        "gcd_system_equivalence_sample_verified": verify_gcd_equivalence_samples(),
        "x_le_P_lower_bound_sample": lower_bound_x_gt_p_verified(LOWER_BOUND_VERIFY_LIMIT),
        "example_inverse_classes_P13_r1": inverse_classes_for_r(13, 1),
        "example_alignment_witness_P23": None
        if example_x is None
        else {"P": example_P, "x": example_x, "witness_rows": witness_row(example_P, example_x)},
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本路由的数学结论。"""
    return [
        {
            "name": "gcd_system_equivalence",
            "statement": "q<P prime divides xP+r iff for a=P mod q, q divides both ax+r and P-a.",
            "status": "proved",
        },
        {
            "name": "inverse_residue_cover",
            "statement": "for fixed r and q<P, allowed x is x == -r*P^{-1} mod q.",
            "status": "proved",
        },
        {
            "name": "periodicity",
            "statement": "the all-r coverage predicate is periodic modulo product_{q<P} q.",
            "status": "proved",
        },
        {
            "name": "x_less_P_prime_interval_equivalence",
            "statement": "for x<P, coverage fails iff interval (xP,(x+1)P) contains a prime.",
            "status": "proved_reduction",
        },
        {
            "name": "global_x_min_gt_P",
            "statement": "minimal alignment x is always greater than P.",
            "status": "not_proved_here_reduces_to_prime_gap_below_P2",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "GCDSystemEquivalenceClosed",
            "closed": True,
            "proved": True,
            "meaning": "用户给出的 gcd 组可严格改写为小素因子覆盖条件；gcd(x,r)>1 是冗余但正确的充分子句。",
            "remaining": "none for equivalence",
        },
        {
            "gate": "InverseResidueAlignmentFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "每个 r 的允许 x 类为有限并集 `x=-r P^{-1} mod q`。",
            "remaining": "CRT hitting-set minimization",
        },
        {
            "gate": "MinimalAlignmentFiniteCRTProblemClosed",
            "closed": True,
            "proved": True,
            "meaning": "最小对齐解可在模小素数 primorial 的周期内定义为有限覆盖最小值。",
            "remaining": "efficient/global formula not derived",
        },
        {
            "gate": "SampleMinimalAlignmentsComputed",
            "closed": True,
            "proved": result["sample_ledger"]["gcd_system_equivalence_sample_verified"],
            "meaning": "样本显示最小对齐解高度非单调，不能由单个固定系数公式描述。",
            "remaining": "larger P search optional",
        },
        {
            "gate": "XGreaterThanPGlobalProved",
            "closed": False,
            "proved": False,
            "meaning": "该命题等价/强相关于每个 `(xP,(x+1)P), x<P` 含素数的短区间素数输入。",
            "remaining": "PrimeGapBelowP2ForAllPBlocks",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本路线给出新压缩与计算证据，但尚未排除热窗口/PDEC/SAE 等终端。",
            "remaining": "TerminalCoreHotDivisorWindowPDECorSAE AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        },
    ]


def build_result(ledger: dict[str, Any]) -> dict[str, Any]:
    """构造逆元对齐路由证书。"""
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_covering_system_router",
        "status": "inverse_alignment_gcd_equivalence_closed_min_x_gt_P_reduced_to_prime_gap_input",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_for_proof": True,
        "gcd_system_equivalence_closed": True,
        "gcd_x_r_clause_redundant_but_safe": True,
        "inverse_residue_formula_closed": True,
        "alignment_period_primorial_closed": True,
        "minimal_alignment_defined_as_finite_crt_hitting_problem": True,
        "global_minimal_alignment_x_gt_P_proved": False,
        "x_less_P_reduction_to_prime_in_each_P_block_closed": True,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "sample_ledger": ledger,
        "theorem_rows": theorem_rows(),
        "next_direct_attack_target": "TerminalCoreHotDivisorWindowPDECorSAE",
        "alternative_route_hardpoint": "PrimeGapBelowP2ForAllPBlocks",
        "source_hashes": {
            "experiments/prime_matrix_inverse_alignment_covering_system_router.py": sha256(Path(__file__).resolve()),
            "data/inverse-alignment-covering-system-sample-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "新的逆元对齐想法有一个严格可用的核心：`xP+r` 有小于 `P` 的素因子，"
            "等价于存在 `a` 使 `gcd(ax+r,P-a)>1`；也等价于每个 `r` 被有限并集 "
            "`x=-r P^{-1} (mod q)` 覆盖。因此最小对齐行是一个模小素数 primorial 的有限 CRT "
            "覆盖最小值。若要证明最小对齐行必大于 `P`，在 `x<P` 区间内该问题化为："
            "每个短区间 `(xP,(x+1)P)` 含有一个素数。这个输入很有解释力，但当前不能由 CRT "
            "形式自动推出，所以它是新的可攻硬点，而不是已闭合证明。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    ledger = result["sample_ledger"]
    lines: list[str] = [
        "# Prime Matrix 逆元对齐覆盖系统路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"gcd_system_equivalence_closed={fmt_bool(result['gcd_system_equivalence_closed'])}",
        f"inverse_residue_formula_closed={fmt_bool(result['inverse_residue_formula_closed'])}",
        f"alignment_period_primorial_closed={fmt_bool(result['alignment_period_primorial_closed'])}",
        f"global_minimal_alignment_x_gt_P_proved={fmt_bool(result['global_minimal_alignment_x_gt_P_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 等价式",
        "",
        "对任意小素数 `q<P`，`q | xP+r` 等价于",
        "",
        "```text",
        "x == -r * P^{-1} (mod q).",
        "```",
        "",
        "令 `a=P mod q`，则 `q | P-a` 且 `q | ax+r`，所以它也等价于某个 `a` 满足 `gcd(ax+r,P-a)>1`。",
        "",
        "## 2. 结论表",
        "",
        "| name | statement | status |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['name'])}`",
                    table_cell(item["statement"]),
                    table_cell(item["status"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 最小对齐样本",
            "",
            "| P | period exhausted | min x in bound | min x > P | first uncovered r at x=P |",
            "| ---: | --- | ---: | --- | ---: |",
        ]
    )
    for item in ledger["rows"]:
        min_x = item["minimal_alignment_x_in_bound"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["P"]),
                    f"`{fmt_bool(item['period_exhausted'])}`",
                    "none" if min_x is None else str(min_x),
                    "`unknown`" if min_x is None else f"`{fmt_bool(item['minimal_alignment_gt_P_if_found'])}`",
                    str(item["first_uncovered_r_for_x_equal_P"]),
                ]
            )
            + " |"
        )
    lower = ledger["x_le_P_lower_bound_sample"]
    lines.extend(
        [
            "",
            "## 4. x<P 边界",
            "",
            "若 `x<P`，则 `xP+r<P^2` 且不被 `P` 整除。此时 `xP+r` 有小于 `P` 的素因子当且仅当它是合数。",
            "所以要证明不存在 `x<=P` 的全覆盖，等价于证明每个区间 `(xP,(x+1)P)` 都至少含一个素数。",
            "",
            "```text",
            f"checked_primes_up_to={lower['limit']}",
            f"checked_prime_count={lower['checked_prime_count']}",
            f"all_checked_have_no_alignment_x_le_P={fmt_bool(lower['all_checked_have_no_alignment_x_le_P'])}",
            "```",
            "",
            "## 5. P=13, r=1 的逆元类示例",
            "",
            "| q | P mod q | allowed x mod q |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in ledger["example_inverse_classes_P13_r1"]:
        lines.append(f"| {item['q']} | {item['a_P_mod_q']} | {item['x_mod_q']} |")
    lines.extend(
        [
            "",
            "## 6. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 7. 下一步",
            "",
            "- 主线仍回到 `TerminalCoreHotDivisorWindowPDECorSAE`。",
            "- 这条新路线的可攻硬点是 `PrimeGapBelowP2ForAllPBlocks`，即证明 `x<P` 时每个 `(xP,(x+1)P)` 有素数。",
            "- 边界：本步不声明全局 `min x>P` 已证明，也不声明行/列命题无条件闭合。",
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    ledger = sample_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    result = build_result(ledger)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(json.dumps({"status": result["status"], "next": result["next_direct_attack_target"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
