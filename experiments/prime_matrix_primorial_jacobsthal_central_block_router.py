#!/usr/bin/env python3
"""审计 primorial 标准覆盖块与 Jacobsthal 最大块接口。

用法示例：
  python3 experiments/prime_matrix_primorial_jacobsthal_central_block_router.py --max-k 8
  python3 -m json.tool docs/monograph/prime-matrix-primorial-jacobsthal-central-block-router.json

输出：
  data/primorial-jacobsthal-central-block-ledger.json
  docs/monograph/prime-matrix-primorial-jacobsthal-central-block-router.json
  docs/monograph/prime-matrix-primorial-jacobsthal-central-block-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd, prod
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "primorial-jacobsthal-central-block-ledger.json"
OUT_JSON = DOCS / "prime-matrix-primorial-jacobsthal-central-block-router.json"
OUT_MD = DOCS / "prime-matrix-primorial-jacobsthal-central-block-router.md"

MAIN_TARGET = "TotalPressureSupportPDECExclusion"
NEXT_TARGET = "SpecialSquarePhaseAvoidsLongPrimorialJacobsthalBlocksOrPhasePDEC"


def is_prime(value: int) -> bool:
    """朴素素性测试。"""
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def first_primes(count: int) -> list[int]:
    """返回前 count 个素数。"""
    primes: list[int] = []
    value = 2
    while len(primes) < count:
        if is_prime(value):
            primes.append(value)
        value += 1
    return primes


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def standard_block_identity_holds(primes: list[int], next_prime: int) -> bool:
    """验证 2..p_{k+1}-1 均与 primorial 非互素。"""
    modulus = prod(primes)
    return all(gcd(offset, modulus) > 1 for offset in range(2, next_prime))


def exact_max_covered_run(primes: list[int]) -> dict[str, Any]:
    """精确求模 primorial 周期内最长连续非互素块。

    返回的 `max_covered_run` 是连续整数都被前 k 个素数之一整除的最大长度。
    它等于 Jacobsthal 函数 `j(M)` 减一。
    """
    modulus = prod(primes)
    coprime = bytearray(b"\x01") * modulus
    for prime in primes:
        coprime[0:modulus:prime] = b"\x00" * (((modulus - 1) // prime) + 1)

    first_coprime: int | None = None
    last_coprime: int | None = None
    max_run = -1
    start = 0
    for residue, is_coprime in enumerate(coprime):
        if not is_coprime:
            continue
        if first_coprime is None:
            first_coprime = residue
        if last_coprime is not None:
            run = residue - last_coprime - 1
            if run > max_run:
                max_run = run
                start = last_coprime + 1
        last_coprime = residue

    if first_coprime is None or last_coprime is None:
        raise RuntimeError("primorial should have coprime residues")

    wrap_run = first_coprime + modulus - last_coprime - 1
    if wrap_run > max_run:
        max_run = wrap_run
        start = (last_coprime + 1) % modulus

    start_display = modulus if start == 0 else start
    return {
        "modulus": modulus,
        "max_covered_run": max_run,
        "jacobsthal_value": max_run + 1,
        "first_max_block_start_mod_m": start,
        "first_max_block_start_display": start_display,
        "first_max_block_end_display": start_display + max_run - 1,
        "left_boundary_coprime": gcd(start_display - 1, modulus) == 1,
        "right_boundary_coprime": gcd(start_display + max_run, modulus) == 1,
    }


def audit_k(k_value: int, primes_all: list[int]) -> dict[str, Any]:
    """审计单个 k。"""
    primes = primes_all[:k_value]
    p_k = primes[-1]
    p_next = primes_all[k_value]
    central_length = p_next - 2
    exact = exact_max_covered_run(primes)
    central_is_max = central_length == exact["max_covered_run"]
    square_anchor_prime = p_next
    square_candidate_length = square_anchor_prime - 1
    return {
        "k": k_value,
        "p_k": p_k,
        "p_next": p_next,
        "primorial": exact["modulus"],
        "standard_block": [2, p_next - 1],
        "standard_block_length": central_length,
        "standard_block_identity_holds": standard_block_identity_holds(primes, p_next),
        "exact_max_covered_run": exact["max_covered_run"],
        "jacobsthal_value": exact["jacobsthal_value"],
        "first_max_block_start": exact["first_max_block_start_display"],
        "first_max_block_end": exact["first_max_block_end_display"],
        "max_block_boundary_coprime": exact["left_boundary_coprime"] and exact["right_boundary_coprime"],
        "central_block_is_global_max": central_is_max,
        "max_minus_standard_length": exact["max_covered_run"] - central_length,
        "square_anchor_prime_P": square_anchor_prime,
        "square_window_candidate_length": square_candidate_length,
        "jacobsthal_global_bound_would_close_square_window": exact["max_covered_run"] < square_candidate_length,
        "global_jacobsthal_bound_fails_for_square_length": exact["max_covered_run"] >= square_candidate_length,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "primorial_standard_block_identity",
            "status": "closed",
            "statement": "For M=prod_{i<=k} p_i, every integer M±a with 2<=a<p_{k+1} has a prime factor <=p_k.",
        },
        {
            "name": "standard_block_maximality_refuted",
            "status": "closed_by_counterexample",
            "statement": "The standard block 2..p_{k+1}-1 is not always the longest covered block in the primorial period; k=5 already gives a longer block.",
        },
        {
            "name": "jacobsthal_interface_for_square_anchor",
            "status": "closed",
            "statement": "For P=p_{k+1}, a global bound G(prod_{q<P}q)<P-1 would imply a square-anchor survivor in every phase, hence a prime in P^2±(1..P-1).",
        },
        {
            "name": "global_jacobsthal_bound_too_strong",
            "status": "closed_boundary",
            "statement": "Exact small-k data and known Jacobsthal tables show G(prod_{q<P}q) can exceed P-1, so the target needs special P^2 phase avoidance rather than a uniform period-wide bound.",
        },
        {
            "name": "special_phase_jacobsthal_avoidance",
            "status": "open",
            "statement": "A global proof still needs to show the square phase P^2 is not aligned with any length P-1 covered block, or route such alignment to PDEC/SAE/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "PrimorialStandardBlockIdentityClosed",
            "closed": result["standard_block_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "`M±a` 的标准块确实由 `a` 的小素因子支付。",
            "remaining": "closed",
        },
        {
            "gate": "CentralBlockGlobalMaxClaimRejected",
            "closed": result["first_central_not_max_counterexample"] is not None,
            "proved": True,
            "meaning": "标准块不是全局最大块；不能把该直觉作为无条件闭合输入。",
            "remaining": "closed by k=5 counterexample",
        },
        {
            "gate": "UniformJacobsthalWouldCloseSquareWindow",
            "closed": True,
            "proved": True,
            "meaning": "若能证 `prod_{q<P}q` 周期内所有低筛覆盖块长度都小于 `P-1`，平方锚窗口自动有素数。",
            "remaining": "closed implication only",
        },
        {
            "gate": "UniformJacobsthalBoundAvailable",
            "closed": False,
            "proved": False,
            "meaning": "该强上界与已知/有限 Jacobsthal 数据不兼容，不能作为当前路线。",
            "remaining": "not available",
        },
        {
            "gate": "SpecialSquarePhaseAvoidanceProved",
            "closed": False,
            "proved": False,
            "meaning": "真正可攻点变为 `P^2` 特殊相位避开长覆盖块，或长覆盖块相位回流 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步排除错误最大块假设，并给出 Jacobsthal 接口；不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_k: int) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    primes_all = first_primes(max_k + 1)
    records = [audit_k(k_value, primes_all) for k_value in range(1, max_k + 1)]
    standard_failures = [record for record in records if not record["standard_block_identity_holds"]]
    central_not_max = [record for record in records if not record["central_block_is_global_max"]]
    global_bound_failures = [record for record in records if record["global_jacobsthal_bound_fails_for_square_length"]]
    first_counterexample = central_not_max[0] if central_not_max else None

    aggregate = {
        "record_count": len(records),
        "standard_block_identity_failure_count": len(standard_failures),
        "central_not_global_max_count": len(central_not_max),
        "global_jacobsthal_square_length_failure_count": len(global_bound_failures),
        "max_exact_covered_run": max((record["exact_max_covered_run"] for record in records), default=None),
        "max_standard_gap_excess": max((record["max_minus_standard_length"] for record in records), default=None),
    }
    ledger = {
        "parameters": {"max_k": max_k},
        "aggregate": aggregate,
        "records": records,
        "standard_block_identity_failures": standard_failures,
        "central_not_global_max_records": central_not_max,
        "global_jacobsthal_square_length_failures": global_bound_failures,
        "external_reference_notes": [
            "OEIS A058989 lists the largest number of consecutive integers each divisible by a prime <= the n-th prime.",
            "OEIS A048670 equals A058989+1 and is the Jacobsthal function on the product of the first n primes.",
            "Ziller--Morack arXiv:1611.03310 supplies algorithmic/computational Jacobsthal data used elsewhere in this repository.",
        ],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_primorial_jacobsthal_central_block_router",
        "status": "primorial_standard_block_closed_global_max_false_special_phase_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "records": records,
        "standard_block_identity_failure_count": len(standard_failures),
        "central_not_global_max_count": len(central_not_max),
        "global_jacobsthal_square_length_failure_count": len(global_bound_failures),
        "first_central_not_max_counterexample": first_counterexample,
        "standard_block_identity_closed": len(standard_failures) == 0,
        "standard_block_global_max_claim_refuted": first_counterexample is not None,
        "uniform_jacobsthal_square_bound_proved": False,
        "special_square_phase_avoidance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_primorial_jacobsthal_central_block_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/primorial-jacobsthal-central-block-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步严格吸收 primorial 新思考：`M=prod_{i<=k}p_i` 时，"
            "`M±a` 对 `2<=a<p_{k+1}` 必有 `<=p_k` 的素因子，这是标准中心覆盖块。"
            "但该块不是周期内全局最长覆盖块；精确扫描在 `k=5,p_k=11,M=2310` 已给出"
            "`114..126` 长度 `13` 的覆盖块，超过标准块长度 `11`。"
            "因此不能用“标准块最大”直接闭合平方锚命题。"
            "可保留的正确接口是 Jacobsthal 接口：对 `P=p_{k+1}`，若能证特殊平方相位 `P^2` 不落入 "
            "`prod_{q<P}q` 周期中任何长度 `P-1` 的低筛覆盖块，"
            "或该相位对齐必回流 PDEC/SAE/ColumnCRT，则可继续推进。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    counterexample = result["first_central_not_max_counterexample"]
    lines = [
        "# Prime Matrix primorial Jacobsthal central block router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_k={result['parameters']['max_k']}",
        f"standard_block_identity_failure_count={result['standard_block_identity_failure_count']}",
        f"central_not_global_max_count={result['central_not_global_max_count']}",
        f"global_jacobsthal_square_length_failure_count={result['global_jacobsthal_square_length_failure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 标准中心覆盖块",
        "",
        "设",
        "",
        "```text",
        "M_k = p_1 p_2 ... p_k.",
        "```",
        "",
        "若 `2<=a<p_{k+1}`，则 `a` 的某个素因子必不超过 `p_k`。因此该素因子整除 `M_k` 且整除 `a`，从而整除 `M_k+a` 与 `M_k-a`。所以 `M_k±[2,p_{k+1}-1]` 确实形成标准低筛覆盖块。",
        "",
        "## 2. 不能使用的最大块假设",
        "",
    ]
    if counterexample:
        lines.extend(
            [
                "标准块不总是最大块。最早反例为：",
                "",
                "```text",
                f"k={counterexample['k']}, p_k={counterexample['p_k']}, M={counterexample['primorial']}",
                f"standard block length={counterexample['standard_block_length']}",
                f"exact max covered run={counterexample['exact_max_covered_run']}",
                f"first max block={counterexample['first_max_block_start']}..{counterexample['first_max_block_end']}",
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "因此“中心标准块就是周期最大块”不能作为目标命题的闭合输入。它只能提供一个下界和相位对照。",
            "",
            "## 3. 精确扫描表",
            "",
            "| k | p_k | p_{k+1} | M_k | standard length | exact max run | first max block | central max? | G>=P-1? |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |",
        ]
    )
    for record in result["records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["k"]),
                    str(record["p_k"]),
                    str(record["p_next"]),
                    str(record["primorial"]),
                    str(record["standard_block_length"]),
                    str(record["exact_max_covered_run"]),
                    f"{record['first_max_block_start']}..{record['first_max_block_end']}",
                    f"`{fmt_bool(record['central_block_is_global_max'])}`",
                    f"`{fmt_bool(record['global_jacobsthal_bound_fails_for_square_length'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 与平方锚目标的严格接口",
            "",
            "平方锚窗口 `P^2±r, 1<=r<P` 中，若存在一个数与所有 `q<P` 互素，则该数必为素数：因为若它合成，则所有素因子都大于 `P`，乘积已经超过相应平方邻域。",
            "",
            "所以一个足够强但通常不可用的闭合条件是：",
            "",
            "```text",
            "G(prod_{q<P} q) < P-1.",
            "```",
            "",
            "这里 `G(prod_{q<P} q)` 是模低素数 primorial 周期内最长低筛覆盖块长度。精确小样本已显示该全周期强界很快失败，因此真正剩余必须利用 `P^2` 的特殊相位，而不是要求全周期所有相位都安全。",
            "",
            "## 5. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")

    lines.extend(
        [
            "",
            "## 6. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 7. 下一步",
            "",
            "- 主攻：`SpecialSquarePhaseAvoidsLongPrimorialJacobsthalBlocksOrPhasePDEC`。",
            "- 也就是证明特殊相位 `P^2 mod prod_{q<P}q` 不会落入长度 `P-1` 的低筛覆盖块；若落入，则必须登记为相位 PDEC/SAE/ColumnCRT。",
            "- 这条路可以和当前 `TotalPressureSupportPDECExclusion` 合并：长低筛覆盖块若覆盖平方锚窗口，同时必须解释激活尾支撑 `Q_side(P)` 的异常高素负载。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 8. 外部参照",
            "",
            "- OEIS A058989：最长连续整数段，每个数都被不超过第 n 个素数的某个素数整除。",
            "- OEIS A048670：上述长度加一，即 Jacobsthal 函数作用于前 n 个素数乘积。",
            "- Ziller--Morack, arXiv:1611.03310：Jacobsthal 函数计算算法与附属数据，本仓库已有 RPZ-BCB 接口使用该数据作风险扫描。",
            "",
            "## 9. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-k", type=int, default=8)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    result = build_result(args.max_k)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-primorial-jacobsthal-central-block-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_k": args.max_k,
                "standard_block_identity_failure_count": result["standard_block_identity_failure_count"],
                "central_not_global_max_count": result["central_not_global_max_count"],
                "first_central_not_max_counterexample": result["first_central_not_max_counterexample"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
