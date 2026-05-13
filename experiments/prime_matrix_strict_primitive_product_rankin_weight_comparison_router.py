#!/usr/bin/env python3
"""生成 strict primitive product Rankin 权重比较路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_primitive_product_rankin_weight_comparison_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json

输出：
  data/primitive-product-rankin-weight-sample-ledger.json
  docs/monograph/prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json
  docs/monograph/prime-matrix-strict-primitive-product-rankin-weight-comparison-router.md
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
OUT_JSON = DOCS / "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json"
OUT_MD = DOCS / "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.md"
OUT_LEDGER = DATA / "primitive-product-rankin-weight-sample-ledger.json"

HARDPOINT = "PrimitiveProductRankinWeightP018Comparison"
PROJECTION = "PrimitiveProductProjectionRuleExecutableHash"
LOCAL_FORMULA = "PrimitiveProductLocalRankinWeightFormula"
EULER_BOUND = "PrimitiveProductEulerProfileSumBound"
P018_TABLE = "PrimitiveProductRankinP018InequalityTable"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
CANDIDATE_BOUND = "ColdProductBlockCandidateCountOrSymbolicBound"
SUPPORT_RANKIN = "PrimitiveProductSupportRankinLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json",
    DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json",
    DOCS / "prime-matrix-strict-primitive-product-rankin-manifest-router.json",
    DATA / "primitive-product-projection-sample-ledger.json",
]

SIGMA_GRID = [round(x / 10, 1) for x in range(1, 31)]


def load_json(path: Path) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_primitive_product_rankin_weight_comparison_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/primitive-product-rankin-weight-sample-ledger.json": sha256(OUT_LEDGER),
    }
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


def factor(n: int) -> dict[int, int]:
    """用确定性试除分解正整数；用于样本和公式校验。"""
    if n <= 0:
        raise ValueError("n must be positive")
    x = n
    result: dict[int, int] = {}
    p = 2
    while p * p <= x:
        while x % p == 0:
            result[p] = result.get(p, 0) + 1
            x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        result[x] = result.get(x, 0) + 1
    return result


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    """由素因子指数生成全部除数；仅用于小样本诊断。"""
    divisors = [1]
    for prime, exp in sorted(factors.items()):
        powers = [prime**e for e in range(exp + 1)]
        divisors = [d * power for d in divisors for power in powers]
    return sorted(divisors)


def gcd(a: int, b: int) -> int:
    """计算最大公因数。"""
    while b:
        a, b = b, a % b
    return abs(a)


def allowed_factorization(h0: int, registered_common_kernel: int) -> dict[int, int]:
    """删除已登记共同核素因子后的允许 primitive 因子域。"""
    h_fac = factor(h0)
    if registered_common_kernel <= 1:
        return h_fac
    kernel_primes = set(factor(registered_common_kernel))
    return {prime: exp for prime, exp in h_fac.items() if prime not in kernel_primes}


def local_sum(prime: int, exp: int, sigma: float, sign: int) -> float:
    """计算局部 Rankin 因子 sum_{e=0}^a p^{sign*sigma*e}。"""
    return sum(prime ** (sign * sigma * e) for e in range(exp + 1))


def euler_product(factors: dict[int, int], sigma: float, sign: int) -> float:
    """计算 primitive profile 的 Euler product 权重。"""
    product = 1.0
    for prime, exp in sorted(factors.items()):
        product *= local_sum(prime, exp, sigma, sign)
    return product


def rankin_bound(P: int, h0: int, Y: int, registered_common_kernel: int, sigma: float) -> dict[str, float]:
    """计算双侧 dyadic Rankin 上界。"""
    factors = allowed_factorization(h0, registered_common_kernel)
    z_plus = euler_product(factors, sigma, +1)
    z_minus = euler_product(factors, sigma, -1)
    upper_from_left = z_plus / (Y**sigma)
    upper_from_right = ((2 * Y) ** sigma) * z_minus
    best = min(upper_from_left, upper_from_right)
    return {
        "sigma": sigma,
        "z_plus": z_plus,
        "z_minus": z_minus,
        "upper_from_left": upper_from_left,
        "upper_from_right": upper_from_right,
        "best_bound": best,
        "best_exponent_base_P": math.log(max(best, 1e-300), P),
        "p018_budget": P**0.18,
        "passes_p018_sample": best <= P**0.18,
    }


def actual_sample_count(h0: int, Y: int, registered_common_kernel: int) -> int:
    """枚举样本块中的真实允许除数个数；只作为诊断，不作为证明。"""
    return sum(
        1
        for d in divisors_from_factorization(factor(h0))
        if Y < d <= 2 * Y and gcd(d, registered_common_kernel) == 1
    )


def best_rankin_row(P: int, h0: int, Y: int, registered_common_kernel: int) -> dict[str, Any]:
    """在固定 sigma 网格上寻找样本最小 Rankin 上界。"""
    candidates = [rankin_bound(P, h0, Y, registered_common_kernel, sigma) for sigma in SIGMA_GRID]
    best = min(candidates, key=lambda item: item["best_bound"])
    return {
        "P": P,
        "h0": h0,
        "Y": Y,
        "block": f"({Y},{2 * Y}]",
        "registered_common_kernel": registered_common_kernel,
        "actual_count_diagnostic_only": actual_sample_count(h0, Y, registered_common_kernel),
        "best_sigma_grid": best["sigma"],
        "best_bound_grid": best["best_bound"],
        "best_exponent_base_P_grid": best["best_exponent_base_P"],
        "p018_budget": best["p018_budget"],
        "passes_p018_on_sample_grid": best["passes_p018_sample"],
        "all_sigma_rows": candidates,
    }


def sample_ledger() -> dict[str, Any]:
    """生成权重公式的样本账本。"""
    rows = [
        best_rankin_row(P=100_000, h0=2310, Y=16, registered_common_kernel=1),
        best_rankin_row(P=100_000, h0=2310, Y=64, registered_common_kernel=1),
        best_rankin_row(P=100_000, h0=4320, Y=64, registered_common_kernel=1),
        best_rankin_row(P=100_000, h0=840, Y=32, registered_common_kernel=6),
    ]
    return {
        "ledger_type": "primitive_product_rankin_weight_sample_ledger",
        "diagnostic_only": True,
        "sigma_grid": SIGMA_GRID,
        "rankin_bound_formula": "N(Y<d<=2Y) <= min(Y^-s Z_+(s), (2Y)^s Z_-(s))",
        "rows": rows,
        "all_sample_rows_pass_grid_p018": all(row["passes_p018_on_sample_grid"] for row in rows),
    }


def imported_flags() -> dict[str, bool]:
    """读取权重比较需要的导入。"""
    projection = load_json(DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json")
    candidate = load_json(DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json")
    manifest = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-manifest-router.json")
    return {
        "primitive_projection_imported": bool(
            projection.get("primitive_product_projection_rule_executable_hash_closed")
        ),
        "candidate_count_symbolic_schema_imported": bool(
            candidate.get("primitive_symbolic_envelope_schema_closed")
        ),
        "rankin_manifest_schema_imported": bool(
            manifest.get("primitive_product_rankin_embedding_manifest_schema_closed")
        ),
    }


def formula_rows() -> list[dict[str, str]]:
    """列出本步闭合的 Rankin 公式。"""
    return [
        {
            "name": "left_tail_rankin",
            "formula": "1_{d>Y} <= (d/Y)^s, so N_B <= Y^{-s} sum_{d|h0,allowed} d^s",
            "status": "closed",
        },
        {
            "name": "right_tail_rankin",
            "formula": "1_{d<=2Y} <= (2Y/d)^s, so N_B <= (2Y)^s sum_{d|h0,allowed} d^{-s}",
            "status": "closed",
        },
        {
            "name": "euler_factorization",
            "formula": "sum_{d|h0,allowed} d^{±s}=prod_{p^a||h0,allowed}(1+p^{±s}+...+p^{±as})",
            "status": "closed",
        },
        {
            "name": "two_sided_dyadic_bound",
            "formula": "N_B <= min(Y^{-s}Z_+(s),(2Y)^s Z_-(s)) for every s>0",
            "status": "closed",
        },
        {
            "name": "p018_comparison_condition",
            "formula": "need min_s min(Y^{-s}Z_+(s),(2Y)^s Z_-(s)) <= P^0.18 for each actual block",
            "status": "open_requires_table",
        },
    ]


def obstruction_rows() -> list[dict[str, str]]:
    """说明为什么本步仍不能宣布 P^0.18 比较闭合。"""
    return [
        {
            "obstruction": "profile_hash_not_budget",
            "meaning": "投影 hash 只锁定局部素因子 profile，不给出实际 P、h0、Y 与剩余预算。",
            "next": P018_TABLE,
        },
        {
            "obstruction": "sigma_not_universal",
            "meaning": "不同 dyadic 块的最优 s 可变；固定常数 s 不能替代逐块表。",
            "next": P018_TABLE,
        },
        {
            "obstruction": "failed_weight_row_needs_return",
            "meaning": "若某块 Rankin 上界超过 P^0.18，必须回流热窗口/共同核/PDEC/SAE/固定历史。",
            "next": FAILURE_RETURN,
        },
        {
            "obstruction": "sample_pass_not_proof",
            "meaning": "样本账本只验证公式可执行性；即使通过也不能代表全部 formal unit 与产品块。",
            "next": P018_TABLE,
        },
        {
            "obstruction": "sample_boundary_pressure",
            "meaning": "当前诊断样本已有若干块的粗 Rankin 网格上界超过 P^0.18，说明公式层不能单独闭合。",
            "next": f"{P018_TABLE} AND {FAILURE_RETURN}",
        },
    ]


def decision_row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def decision_rows(flags: dict[str, bool], ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    local_formula_closed = (
        flags["primitive_projection_imported"]
        and flags["candidate_count_symbolic_schema_imported"]
        and flags["rankin_manifest_schema_imported"]
    )
    return [
        decision_row(
            "PrimitiveProductRankinWeightTargetImported",
            True,
            flags["primitive_projection_imported"],
            "上一层已闭合 d 到 primitive profile 的可执行投影规则。",
            HARDPOINT,
        ),
        decision_row(
            "PrimitiveProductLocalRankinWeightFormulaClosed",
            local_formula_closed,
            local_formula_closed,
            "双侧 dyadic Rankin 指示函数与局部 Euler product 权重公式已自足闭合。",
            LOCAL_FORMULA,
        ),
        decision_row(
            "PrimitiveProductEulerProfileSumBoundClosed",
            local_formula_closed,
            local_formula_closed,
            "允许 primitive 因子域上的 sum d^{±s} 已分解为有限 Euler product。",
            EULER_BOUND,
        ),
        decision_row(
            "DiagnosticSampleLedgerExecutable",
            True,
            True,
            "样本账本可执行；该项只校验公式管线，不作为全体产品块证明。",
            "diagnostic only",
        ),
        decision_row(
            "DiagnosticSampleAllRowsPassGridP018",
            True,
            ledger["all_sample_rows_pass_grid_p018"],
            "诊断样本是否全部通过 P^0.18 网格比较；失败表示需要更细预算表或回流包。",
            f"{P018_TABLE} AND {FAILURE_RETURN}",
        ),
        decision_row(
            "PrimitiveProductRankinP018InequalityTablePresent",
            False,
            False,
            "尚未列出全部实际 formal unit / dyadic block 的 P、h0、Y、s 与剩余预算比较。",
            P018_TABLE,
        ),
        decision_row(
            "PrimitiveProductRankinFailureReturnPacketLedgerClosed",
            False,
            False,
            "尚未为 P^0.18 比较失败块生成热窗口/共同核/PDEC/SAE 回流包。",
            FAILURE_RETURN,
        ),
        decision_row(
            "PrimitiveProductRankinWeightP018ComparisonProved",
            False,
            False,
            "公式层已闭合，但缺全体实际块的不等式表和失败回流处理。",
            f"{P018_TABLE} AND {FAILURE_RETURN}",
        ),
        decision_row(
            "ColdProductBlockCandidateCountOrSymbolicBoundProved",
            False,
            False,
            "Rankin 权重比较未闭合，因此 cold 产品候选计数符号界仍未闭合。",
            CANDIDATE_BOUND,
        ),
        decision_row(
            "PrimitiveProductSupportRankinLedgerProved",
            False,
            False,
            "权重比较和失败回流未完成，原始产品支撑 Rankin 门仍未闭合。",
            SUPPORT_RANKIN,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链与真实结构链的终端矛盾。",
            f"{P018_TABLE} AND {FAILURE_RETURN} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 Rankin 权重比较路由证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    ledger = sample_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, indent=2, sort_keys=True), encoding="utf-8")
    flags = imported_flags()
    decisions = decision_rows(flags, ledger)
    local_closed = bool(
        next(item for item in decisions if item["gate"] == "PrimitiveProductLocalRankinWeightFormulaClosed")[
            "proved"
        ]
    )
    return {
        "certificate_type": "prime_matrix_strict_primitive_product_rankin_weight_comparison_router",
        "status": "primitive_rankin_local_weight_formula_closed_p018_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{P018_TABLE} AND {FAILURE_RETURN}",
        "next_direct_attack_target": P018_TABLE,
        "imported_flags": flags,
        "formula_rows": formula_rows(),
        "obstruction_rows": obstruction_rows(),
        "decision_table": decisions,
        "primitive_product_local_rankin_weight_formula_closed": local_closed,
        "primitive_product_euler_profile_sum_bound_closed": local_closed,
        "primitive_product_rankin_p018_inequality_table_present": False,
        "primitive_product_rankin_failure_return_packet_ledger_closed": False,
        "primitive_product_rankin_weight_p018_comparison_proved": False,
        "cold_product_block_candidate_count_or_symbolic_bound_proved": False,
        "primitive_product_support_rankin_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`PrimitiveProductRankinWeightP018Comparison` 的公式层已经推进："
            "对任意 dyadic 产品块 `(Y,2Y]` 与任意 `s>0`，候选数满足 "
            "`N_B<=min(Y^{-s}Z_+(s),(2Y)^sZ_-(s))`，其中 `Z_±` 是允许 primitive "
            "因子域上的有限 Euler product。这个结论自足且可复算。"
            "但要推出 `P^0.18` 仍必须给出全部实际块的 `P,h0,Y,s` 预算表，"
            "并为失败块登记回流包；因此完整权重比较尚未闭合。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict primitive product Rankin 权重比较路由器",
        "",
        "## 结论",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"status={result['status']}",
        f"hardpoint_before={result['hardpoint_before_router']}",
        f"hardpoint_after={result['hardpoint_after_router']}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        f"primitive_product_local_rankin_weight_formula_closed={fmt_bool(result['primitive_product_local_rankin_weight_formula_closed'])}",
        f"primitive_product_rankin_weight_p018_comparison_proved={fmt_bool(result['primitive_product_rankin_weight_p018_comparison_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 已闭合公式",
        "",
        "| 名称 | 公式 | 状态 |",
        "|---|---|---|",
    ]
    for item in result["formula_rows"]:
        lines.append(
            f"| `{table_cell(item['name'])}` | {table_cell(item['formula'])} | `{table_cell(item['status'])}` |"
        )
    lines.extend(
        [
            "",
            "## 剩余阻断",
            "",
            "| 阻断 | 含义 | 下一步 |",
            "|---|---|---|",
        ]
    )
    for item in result["obstruction_rows"]:
        lines.append(
            f"| `{table_cell(item['obstruction'])}` | {table_cell(item['meaning'])} | `{table_cell(item['next'])}` |"
        )
    lines.extend(
        [
            "",
            "## 判定表",
            "",
            "| Gate | Closed | Proved | Meaning | Remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["decision_table"]:
        lines.append(
            "| `{}` | `{}` | `{}` | {} | `{}` |".format(
                table_cell(item["gate"]),
                fmt_bool(item["closed"]),
                fmt_bool(item["proved"]),
                table_cell(item["meaning"]),
                table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 样本账本",
            "",
            f"- 路径：`{OUT_LEDGER.relative_to(ROOT)}`",
            "- 用途：只校验公式和计算管线，不作为全体产品块证明。",
            "",
            "## 依赖哈希",
            "",
            "| 文件 | SHA256 |",
            "|---|---|",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、Markdown 与样本账本。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "primitive_product_local_rankin_weight_formula_closed="
        f"{fmt_bool(result['primitive_product_local_rankin_weight_formula_closed'])}"
    )
    print(
        "primitive_product_rankin_weight_p018_comparison_proved="
        f"{fmt_bool(result['primitive_product_rankin_weight_p018_comparison_proved'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
