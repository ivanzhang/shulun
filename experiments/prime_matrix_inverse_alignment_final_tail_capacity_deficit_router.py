#!/usr/bin/env python3
"""生成逆元 final-tail 容量缺口下钻证书。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_final_tail_capacity_deficit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-final-tail-capacity-deficit-router.json

输出：
  data/inverse-alignment-final-tail-capacity-probe-ledger.json
  docs/monograph/prime-matrix-inverse-alignment-final-tail-capacity-deficit-router.json
  docs/monograph/prime-matrix-inverse-alignment-final-tail-capacity-deficit-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_LEDGER = DATA / "inverse-alignment-final-tail-capacity-probe-ledger.json"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-final-tail-capacity-deficit-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-final-tail-capacity-deficit-router.md"

SCAN_LIMIT = 251
REQUESTED_P = [13, 17, 19, 23, 29, 31]

SOURCE_FILES = [
    DOCS / "prime-matrix-inverse-alignment-min-x-phase-scan-router.json",
    DOCS / "prime-matrix-zero-row-minrep-route-review.md",
    DATA / "inverse-alignment-min-x-phase-scan-ledger.json",
]

NEXT_TARGET = "UniformFinalTailRoughSurvivorLowerBoundOrRegisteredPhaseDefect"
JACOBSTHAL_TARGET = "PrimorialCutoffJacobsthalRoughSurvivorLowerBoundForPBlocks"
PHASE_TARGET = "RegisteredFinalTailPhaseDefectPDECSAERoute"
SHORT_INTERVAL = "PrimeInEveryAlignedPBlockBelowP2"


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def primes_lt(n: int) -> list[int]:
    """生成小于 n 的素数。"""
    if n <= 2:
        return []
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for p in range(2, int((n - 1) ** 0.5) + 1):
        if sieve[p]:
            for m in range(p * p, n, p):
                sieve[m] = False
    return [i for i in range(2, n) if sieve[i]]


def phase(P: int, x: int, q: int) -> int:
    """计算 q 对行 x 的覆盖相位 rho_q(x)。"""
    return (-x * P) % q


def mu_for_phase(P: int, rho: int, q: int) -> int:
    """计算 1<=r<P 中 r=rho mod q 的列数。"""
    first = q if rho == 0 else rho
    if first > P - 1:
        return 0
    return 1 + (P - 1 - first) // q


def final_tail_context(P: int) -> dict[str, int]:
    """返回 final-tail cutoff 的第二大素数和最大尾素数。"""
    qs = primes_lt(P)
    return {
        "cutoff_second_largest_prime": qs[-2],
        "tail_largest_prime": qs[-1],
        "tail_gap_to_P": P - qs[-1],
    }


def residual_after_cutoff(P: int, x: int, cutoff: int) -> list[int]:
    """返回未被 q<=cutoff 覆盖的列。"""
    low_primes = [q for q in primes_lt(P) if q <= cutoff]
    return [
        r
        for r in range(1, P)
        if not any(r % q == phase(P, x, q) for q in low_primes)
    ]


def tail_columns(P: int, x: int, ell: int) -> list[int]:
    """返回最大尾素数 ell 命中的列。"""
    rho = phase(P, x, ell)
    return [r for r in range(1, P) if r % ell == rho]


def is_prime(n: int) -> bool:
    """小整数素性测试。"""
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


def final_tail_row(P: int, x: int) -> dict[str, Any]:
    """计算单个 x 的 final-tail 残洞、尾容量和幸存素数。"""
    ctx = final_tail_context(P)
    cutoff = ctx["cutoff_second_largest_prime"]
    ell = ctx["tail_largest_prime"]
    residual = residual_after_cutoff(P, x, cutoff)
    tail = tail_columns(P, x, ell)
    tail_inside = sorted(set(residual) & set(tail))
    prime_survivors = [r for r in residual if r not in tail and is_prime(x * P + r)]
    nonprime_nontail = [r for r in residual if r not in tail and not is_prime(x * P + r)]
    return {
        "x": x,
        "residual_size": len(residual),
        "tail_capacity_mu": len(tail),
        "tail_effective_hits_inside_residual": len(tail_inside),
        "residual_minus_tail_capacity_gap": len(residual) - len(tail),
        "residual_minus_tail_effective_gap": len(residual) - len(tail_inside),
        "residual_columns": residual,
        "tail_columns": tail,
        "tail_inside_residual": tail_inside,
        "prime_survivor_columns": prime_survivors,
        "nonprime_nontail_residual_columns": nonprime_nontail,
        "decomposition_ok": not nonprime_nontail,
    }


def scan_prime(P: int) -> dict[str, Any]:
    """扫描固定 P 的 1<=x<=P final-tail 缺口。"""
    ctx = final_tail_context(P)
    rows = [final_tail_row(P, x) for x in range(1, P + 1)]
    nonpositive = [row for row in rows if row["residual_minus_tail_capacity_gap"] <= 0]
    no_survivor = [row for row in rows if not row["prime_survivor_columns"]]
    return {
        "P": P,
        **ctx,
        "x_range_checked": f"1<=x<={P}",
        "min_residual_minus_tail_capacity_gap": min(
            row["residual_minus_tail_capacity_gap"] for row in rows
        ),
        "min_residual_minus_tail_effective_gap": min(
            row["residual_minus_tail_effective_gap"] for row in rows
        ),
        "strict_capacity_deficit_for_all_x": not nonpositive,
        "prime_survivor_for_all_x": not no_survivor,
        "decomposition_ok_for_all_x": all(row["decomposition_ok"] for row in rows),
        "nonpositive_capacity_gap_witnesses": [
            {
                "x": row["x"],
                "residual_size": row["residual_size"],
                "tail_capacity_mu": row["tail_capacity_mu"],
                "tail_effective_hits_inside_residual": row["tail_effective_hits_inside_residual"],
                "prime_survivor_columns": row["prime_survivor_columns"],
            }
            for row in nonpositive
        ],
    }


def build_probe_rows() -> list[dict[str, Any]]:
    """生成 P<=SCAN_LIMIT 的 final-tail 探针。"""
    return [scan_prime(P) for P in primes_lt(SCAN_LIMIT + 1) if P >= 13]


def requested_detail_rows(probe_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """给请求的 P 保留代表性最弱行细节。"""
    details = []
    for summary in probe_rows:
        P = summary["P"]
        if P not in REQUESTED_P:
            continue
        rows = [final_tail_row(P, x) for x in range(1, P + 1)]
        weakest = min(rows, key=lambda row: row["residual_minus_tail_capacity_gap"])
        details.append({"P": P, **final_tail_context(P), "weakest_row": weakest})
    return details


def theorem_rows() -> list[dict[str, str]]:
    """列出本证书闭合的结构事实和未闭合输入。"""
    return [
        {
            "name": "final_tail_decomposition",
            "status": "closed",
            "statement": "After sieving by all primes below ell, where ell is the largest prime <P, every residual column is either an ell-multiple or a genuine prime >P in the early range 1<=x<=P.",
        },
        {
            "name": "tail_capacity_at_most_two",
            "status": "closed",
            "statement": "Because ell>P/2, the largest tail prime phase hits at most two columns in 1<=r<P.",
        },
        {
            "name": "capacity_or_phase_defect_implication",
            "status": "closed",
            "statement": "If |R|>mu_ell then a prime survivor exists; if |R|<=mu_ell but R is not contained in the ell phase, the missing alignment is a registered phase defect and also leaves a prime survivor.",
        },
        {
            "name": "finite_probe",
            "status": "diagnostic_closed",
            "statement": "For tested primes 13<=P<=251 every early row has a final-tail prime survivor; for all tested P>=29 the stronger strict capacity deficit |R|>mu_ell holds.",
        },
        {
            "name": "uniform_lower_bound",
            "status": "open",
            "statement": "The remaining global task is to prove a non-tautological rough survivor lower bound for the primorial cutoff, or route equality cases to a registered phase defect.",
        },
    ]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_final_tail_capacity_deficit_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in [OUT_LEDGER, *SOURCE_FILES]:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def build_result(probe_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """构造 final-tail 容量缺口证书。"""
    requested_rows = requested_detail_rows(probe_rows)
    all_decomposition = all(row["decomposition_ok_for_all_x"] for row in probe_rows)
    all_prime_survivor = all(row["prime_survivor_for_all_x"] for row in probe_rows)
    strict_from_29 = all(row["P"] < 29 or row["strict_capacity_deficit_for_all_x"] for row in probe_rows)
    return {
        "certificate_type": "prime_matrix_inverse_alignment_final_tail_capacity_deficit_router",
        "status": "final_tail_decomposition_closed_uniform_rough_survivor_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_for_global_proof": True,
        "scan_limit": SCAN_LIMIT,
        "final_tail_residual_decomposition_closed": all_decomposition,
        "largest_tail_prime_capacity_at_most_two_closed": True,
        "capacity_or_phase_defect_implication_closed": True,
        "finite_probe_prime_survivor_for_all_rows": all_prime_survivor,
        "finite_probe_strict_capacity_deficit_for_all_P_ge_29": strict_from_29,
        "uniform_final_tail_capacity_deficit_or_phase_defect_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "UniformCapacityDeficitOrRegisteredPhaseDefectLowerBoundForAllEarlyX",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [JACOBSTHAL_TARGET, PHASE_TARGET, SHORT_INTERVAL],
        "theorem_rows": theorem_rows(),
        "probe_rows": probe_rows,
        "requested_detail_rows": requested_rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "final-tail 下钻给出一个严格结构分解：设 ell 为 P 以下最大素数、z 为其前一素数。"
            "在 `1<=x<=P` 中，过了 `q<=z` 的残洞若不是 ell 相位倍数，就只能是真正的素数；"
            "不可能是其它合数，因为其它允许素因子只能是 `>P`，两因子乘积已超过 `P^2+P`，而 P 本身不整除 `xP+r`。"
            "因此 final-tail 缺口不再是抽象容量账本，而是精确的“ell 倍数或素数幸存”二分。"
            "有限探针到 `P<=251` 全部有素数幸存，且 `P>=29` 全部满足更强的 `|R_z(x)|>mu_ell(x)`。"
            "但全局仍需证明 primorial cutoff 的粗幸存下界，或把等号态登记为相位缺陷；行/列命题尚未无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix inverse alignment final-tail 容量缺口路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"final_tail_residual_decomposition_closed={fmt_bool(result['final_tail_residual_decomposition_closed'])}",
        f"finite_probe_prime_survivor_for_all_rows={fmt_bool(result['finite_probe_prime_survivor_for_all_rows'])}",
        f"finite_probe_strict_capacity_deficit_for_all_P_ge_29={fmt_bool(result['finite_probe_strict_capacity_deficit_for_all_P_ge_29'])}",
        f"uniform_final_tail_capacity_deficit_or_phase_defect_lower_bound_proved={fmt_bool(result['uniform_final_tail_capacity_deficit_or_phase_defect_lower_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 结构分解",
        "",
        "令 `ell` 为小于 `P` 的最大素数，`z` 为 `ell` 前一个素数。对 `1<=x<=P`，定义",
        "",
        "```text",
        "R_z(x)={1<=r<P: xP+r 不被任何 q<=z 整除}.",
        "A_ell(x)={1<=r<P: ell | xP+r}.",
        "```",
        "",
        "若 `r in R_z(x) \\ A_ell(x)` 且 `xP+r` 合数，则其最小素因子不能小于 `ell`，不能等于 `ell`，也不能等于 `P`。因此最小素因子必须大于 `P`，两个因子乘积超过 `P^2+P`，与 `xP+r<=P^2+P-1` 矛盾。所以这类列必为素数。",
        "",
        "## 2. 有限探针",
        "",
        f"扫描范围：素数 `13<=P<={result['scan_limit']}`，每个 `1<=x<=P`。",
        "",
        "| P | z | ell | min R_minus_mu_ell | min R_minus_effective | strict capacity all x | prime survivor all x | nonpositive witnesses |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in result["probe_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['P']}`",
                    f"`{row['cutoff_second_largest_prime']}`",
                    f"`{row['tail_largest_prime']}`",
                    f"`{row['min_residual_minus_tail_capacity_gap']}`",
                    f"`{row['min_residual_minus_tail_effective_gap']}`",
                    f"`{fmt_bool(row['strict_capacity_deficit_for_all_x'])}`",
                    f"`{fmt_bool(row['prime_survivor_for_all_x'])}`",
                    f"`{table_cell(row['nonpositive_capacity_gap_witnesses'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 请求 P 的最弱行",
            "",
            "| P | z | ell | weakest x | R_size | mu_ell | effective hits | prime survivor columns |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["requested_detail_rows"]:
        weak = row["weakest_row"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['P']}`",
                    f"`{row['cutoff_second_largest_prime']}`",
                    f"`{row['tail_largest_prime']}`",
                    f"`{weak['x']}`",
                    f"`{weak['residual_size']}`",
                    f"`{weak['tail_capacity_mu']}`",
                    f"`{weak['tail_effective_hits_inside_residual']}`",
                    f"`{weak['prime_survivor_columns']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 判定边界",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")
    lines.extend(
        [
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 具体化为：证明 `P>=29` 时 `|R_z(x)|>mu_ell(x)` 对所有 `1<=x<=P` 成立；或证明所有等号态必须进入 `{PHASE_TARGET}`。",
            f"- 这等价需要一个 `{JACOBSTHAL_TARGET}` 型粗幸存下界，不能把有限探针当作全局证明。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """生成 JSON、数据账本与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    probe_rows = build_probe_rows()
    OUT_LEDGER.write_text(
        json.dumps(
            {
                "ledger_type": "inverse_alignment_final_tail_capacity_probe_ledger",
                "scan_limit": SCAN_LIMIT,
                "probe_rows": probe_rows,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    result = build_result(probe_rows)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(
        "finite_probe_strict_capacity_deficit_for_all_P_ge_29="
        + fmt_bool(result["finite_probe_strict_capacity_deficit_for_all_P_ge_29"])
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
