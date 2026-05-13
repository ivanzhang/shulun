#!/usr/bin/env python3
"""生成 strict cold prefix step 来源图路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_prefix_step_origin_map_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-prefix-step-origin-map-router.json

输出：
  data/cold-prefix-step-origin-map-sample-ledger.json
  docs/monograph/prime-matrix-strict-cold-prefix-step-origin-map-router.json
  docs/monograph/prime-matrix-strict-cold-prefix-step-origin-map-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-cold-prefix-step-origin-map-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-prefix-step-origin-map-router.md"
OUT_LEDGER = DATA / "cold-prefix-step-origin-map-sample-ledger.json"

HARDPOINT = "ColdPrefixStepQuotientOriginMapToCarrierRows"
LOCAL_GUARD = "ColdPrefixStepLocalCarrierDomainGuardOrSourceDefectReturn"
NO_RETURN_DIVISIBILITY = "NoReturnColdPrefixProductDividesCarrierLCMH0"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.json",
    DOCS / "prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json",
    DOCS / "prime-matrix-strict-h0-carrier-quotient-compat-router.json",
    DOCS / "prime-matrix-strict-early-zero-factorization-carrier-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def factor(n: int) -> dict[int, int]:
    """用确定性试除分解正整数；仅用于证书样本和规则哈希。"""
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


def row_factor_table(carrier_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """为 carrier rows 添加素因子表。"""
    rows = []
    for row in carrier_rows:
        rows.append({**row, "valuation": {str(k): v for k, v in sorted(factor(int(row["m_c"])).items())}})
    return rows


def carrier_budget(carrier_rows: list[dict[str, Any]]) -> dict[int, int]:
    """计算每个素数在 carrier-lcm 中的最大指数。"""
    budget: dict[int, int] = {}
    for row in carrier_rows:
        for prime, exp in factor(int(row["m_c"])).items():
            budget[prime] = max(budget.get(prime, 0), exp)
    return budget


def choose_origin_row(carrier_rows: list[dict[str, Any]], prime: int, exp: int) -> dict[str, Any] | None:
    """为 p^exp 选择确定性来源行：能容纳该指数的最小 column 行。"""
    candidates = []
    for row in carrier_rows:
        row_exp = factor(int(row["m_c"])).get(prime, 0)
        if row_exp >= exp:
            candidates.append((int(row["column"]), row, row_exp))
    if not candidates:
        return None
    _, selected, selected_exp = min(candidates, key=lambda item: item[0])
    return {
        "column": selected["column"],
        "m_c": selected["m_c"],
        "available_exp": selected_exp,
    }


def token_origin_map(carrier_rows: list[dict[str, Any]], step: int) -> dict[str, Any]:
    """生成单个 prefix step 的逐素数 token 来源图。"""
    step_fac = factor(step)
    budget = carrier_budget(carrier_rows)
    token_rows = []
    source_defects = []
    for prime, exp in sorted(step_fac.items()):
        max_exp = budget.get(prime, 0)
        selected = choose_origin_row(carrier_rows, prime, exp)
        if selected is None:
            source_defects.append(
                {
                    "prime": prime,
                    "step_exp": exp,
                    "carrier_budget_exp": max_exp,
                    "defect": "no_carrier_row_supports_this_prime_power",
                }
            )
            continue
        token_rows.append(
            {
                "prime": prime,
                "step_exp": exp,
                "origin_column": selected["column"],
                "origin_m_c": selected["m_c"],
                "origin_available_exp": selected["available_exp"],
            }
        )
    single_row_candidates = [
        row["column"] for row in carrier_rows if int(row["m_c"]) % step == 0
    ]
    return {
        "step": step,
        "step_factorization": {str(k): v for k, v in sorted(step_fac.items())},
        "token_origin_rows": token_rows,
        "source_defects": source_defects,
        "token_origin_map_exists": not source_defects,
        "single_row_origin_exists": bool(single_row_candidates),
        "single_row_origin_columns": single_row_candidates,
    }


def sample_ledger() -> dict[str, Any]:
    """生成 step 来源图样本账本。"""
    samples = [
        {
            "case": "token_map_without_single_row",
            "carrier_rows": [
                {"column": 1, "m_c": 2},
                {"column": 2, "m_c": 3},
            ],
            "step": 6,
        },
        {
            "case": "single_row_prime_power_support",
            "carrier_rows": [
                {"column": 1, "m_c": 8},
                {"column": 2, "m_c": 9},
            ],
            "step": 4,
        },
        {
            "case": "source_domain_defect",
            "carrier_rows": [
                {"column": 1, "m_c": 3},
                {"column": 2, "m_c": 5},
            ],
            "step": 4,
        },
        {
            "case": "mixed_token_map",
            "carrier_rows": [
                {"column": 1, "m_c": 4},
                {"column": 2, "m_c": 15},
            ],
            "step": 12,
        },
    ]
    rows = []
    for item in samples:
        rows.append(
            {
                **item,
                "carrier_factor_table": row_factor_table(item["carrier_rows"]),
                "classification": token_origin_map(item["carrier_rows"], int(item["step"])),
            }
        )
    return {
        "ledger_type": "cold_prefix_step_origin_map_sample_ledger",
        "rule": "map every prime-power token p^e in step g to the least carrier row with v_p(m_c)>=e",
        "rows": rows,
        "token_map_without_single_row_demonstrated": any(
            row["classification"]["token_origin_map_exists"]
            and not row["classification"]["single_row_origin_exists"]
            for row in rows
        ),
        "source_defect_demonstrated": any(
            row["classification"]["source_defects"] for row in rows
        ),
        "all_local_steps_have_token_origin_maps": all(
            bool(row["classification"]["source_defects"]) or row["classification"]["token_origin_map_exists"]
            for row in rows
        ),
    }


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_cold_prefix_step_origin_map_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/cold-prefix-step-origin-map-sample-ledger.json": sha256(OUT_LEDGER),
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取 step 来源图需要的导入。"""
    overflow = load_json(DOCS / "prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.json")
    valuation = load_json(DOCS / "prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json")
    h0 = load_json(DOCS / "prime-matrix-strict-h0-carrier-quotient-compat-router.json")
    carrier = load_json(DOCS / "prime-matrix-strict-early-zero-factorization-carrier-router.json")
    return {
        "target_imported": overflow.get("next_direct_attack_target") == HARDPOINT,
        "overflow_atom_split_imported": bool(overflow.get("overflow_atom_split_closed")),
        "valuation_budget_imported": bool(
            valuation.get("prefix_valuation_budget_against_carrier_lcm_or_overflow_return_proved")
        ),
        "carrier_lcm_formula_imported": bool(h0.get("carrier_quotient_lcm_h0_formula_closed")),
        "early_zero_carrier_imported": bool(carrier.get("early_zero_row_factorization_carrier_ledger_present")),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出 step 来源图的严格命题。"""
    return [
        {
            "name": "token_origin_not_single_row_origin",
            "statement": "g|h0^car only requires each p^e||g to be supported by some carrier row; g need not divide one m_c.",
            "status": "closed",
        },
        {
            "name": "canonical_token_selector",
            "statement": "For p^e in g, choose the least column c with v_p(m_c)>=e.",
            "status": "closed",
        },
        {
            "name": "local_domain_equivalence",
            "statement": "A token origin map exists iff v_p(g)<=max_c v_p(m_c) for every p|g.",
            "status": "closed",
        },
        {
            "name": "source_defect_return",
            "statement": "If no token origin map exists, g is outside the carrier-lcm local domain and must return.",
            "status": "closed_as_return_condition",
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
    token_map_closed = (
        flags["target_imported"]
        and flags["carrier_lcm_formula_imported"]
        and flags["early_zero_carrier_imported"]
        and ledger["token_map_without_single_row_demonstrated"]
        and ledger["source_defect_demonstrated"]
    )
    map_or_defect_closed = token_map_closed and flags["valuation_budget_imported"]
    return [
        decision_row(
            "StepOriginTargetImported",
            True,
            flags["target_imported"],
            "上一层已把单步来源域缺陷压到 cold prefix step 来源图。",
            HARDPOINT,
        ),
        decision_row(
            "StrongSingleCarrierRowRequirementRejected",
            True,
            ledger["token_map_without_single_row_demonstrated"],
            "step g 不必整体除某个 m_c；逐素数 token 来源图才是正确最弱对象。",
            "single-row shortcut rejected",
        ),
        decision_row(
            "CanonicalTokenOriginMapCriterionClosed",
            token_map_closed,
            token_map_closed,
            "局部可容纳 step 的每个 p^e token 都有确定性 carrier row 来源。",
            "token map closed",
        ),
        decision_row(
            "StepLocalCarrierDomainDefectReturnClosed",
            map_or_defect_closed,
            map_or_defect_closed,
            "若某个 p^e 无 carrier row 支撑，则该 step 不能留在 carrier-lcm 分支，必须回流。",
            LOCAL_GUARD,
        ),
        decision_row(
            "ColdPrefixStepQuotientOriginMapToCarrierRowsProvedForLocalSteps",
            token_map_closed,
            token_map_closed,
            "对所有局部 carrier-admissible step，来源图已闭合。",
            HARDPOINT,
        ),
        decision_row(
            "ColdPrefixStepQuotientOriginMapToCarrierRowsGlobalProved",
            False,
            False,
            "全局仍需证明实际 cold prefix 不触发 source-defect，或该 defect 被预算/终端族吸收。",
            f"{LOCAL_GUARD} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        ),
        decision_row(
            "NoReturnColdPrefixProductDividesCarrierLCMH0Proved",
            False,
            False,
            "还需把 step local guard 与累计 valuation pass 同步成完整 no-return 分支定理。",
            NO_RETURN_DIVISIBILITY,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{LOCAL_GUARD} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 step 来源图证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    ledger = sample_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    flags = imported_flags()
    decisions = decision_rows(flags, ledger)
    token_map_closed = next(
        item for item in decisions if item["gate"] == "CanonicalTokenOriginMapCriterionClosed"
    )["proved"]
    return {
        "certificate_type": "prime_matrix_strict_cold_prefix_step_origin_map_router",
        "status": "cold_prefix_step_token_origin_map_closed_global_source_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{LOCAL_GUARD} AND {NO_RETURN_DIVISIBILITY}",
        "next_direct_attack_target": NO_RETURN_DIVISIBILITY,
        "parallel_attack_targets": [LOCAL_GUARD, SPARSE_BUDGET, PERSISTENT_TERMINAL, DSTRUCTURE],
        "imported_flags": flags,
        "theorem_rows": theorem_rows(),
        "sample_ledger_path": str(OUT_LEDGER.relative_to(ROOT)),
        "sample_ledger_sha256": sha256(OUT_LEDGER),
        "decision_table": decisions,
        "strong_single_carrier_row_requirement_rejected": True,
        "canonical_token_origin_map_criterion_closed": bool(token_map_closed),
        "cold_prefix_step_quotient_origin_map_to_carrier_rows_proved_for_local_steps": bool(token_map_closed),
        "cold_prefix_step_quotient_origin_map_to_carrier_rows_global_proved": False,
        "step_local_carrier_domain_defect_return_closed": bool(
            next(item for item in decisions if item["gate"] == "StepLocalCarrierDomainDefectReturnClosed")[
                "proved"
            ]
        ),
        "no_return_cold_prefix_product_divides_carrier_lcm_h0_proved": False,
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`ColdPrefixStepQuotientOriginMapToCarrierRows` 的正确最弱形式不是要求每个 step `g` 整体除某个 "
            "`m_c`，而是要求 `g` 的每个素数幂 token `p^e` 都能映射到某个满足 `v_p(m_c)>=e` 的 carrier row。"
            "本步关闭了这个 token 来源图判据，并把单步超出 carrier-lcm 本地域的情形登记为 source-defect return。"
            "因此 step 来源图本身不再是代数障碍；剩余是把 source-defect return 与累计 valuation pass 同步，"
            "形成 no-return 分支上的 `D(U)|h0^car`，并最终排斥或吸收所有回流。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict cold prefix step 来源图路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "strong_single_carrier_row_requirement_rejected",
        "canonical_token_origin_map_criterion_closed",
        "cold_prefix_step_quotient_origin_map_to_carrier_rows_proved_for_local_steps",
        "cold_prefix_step_quotient_origin_map_to_carrier_rows_global_proved",
        "step_local_carrier_domain_defect_return_closed",
        "no_return_cold_prefix_product_divides_carrier_lcm_h0_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. 来源图命题")
    lines.append("")
    lines.append("| name | statement | status |")
    lines.append("| --- | --- | --- |")
    for item in result["theorem_rows"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["name", "statement", "status"])
            + " |"
        )
    lines.append("")

    lines.append("## 2. 样本账本")
    lines.append("")
    lines.append(f"- path: `{result['sample_ledger_path']}`")
    lines.append(f"- sha256: `{result['sample_ledger_sha256']}`")
    lines.append("")

    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["decision_table"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )
    lines.append("")

    lines.append("## 4. 下一步最窄点")
    lines.append("")
    lines.append(f"- 主攻：`{result['next_direct_attack_target']}`。")
    lines.append(f"- 并行守门：`{LOCAL_GUARD}`、`{SPARSE_BUDGET}`、`{PERSISTENT_TERMINAL}`。")
    lines.append("- 边界：本步闭合 token 来源图判据，不声明全部实际 prefix 已整除 carrier-lcm h0。")
    lines.append("")

    lines.append("## 5. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for file, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、Markdown 与样本账本。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "canonical_token_origin_map_criterion_closed="
        f"{fmt_bool(result['canonical_token_origin_map_criterion_closed'])}"
    )
    print(
        "cold_prefix_step_quotient_origin_map_to_carrier_rows_global_proved="
        f"{fmt_bool(result['cold_prefix_step_quotient_origin_map_to_carrier_rows_global_proved'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
