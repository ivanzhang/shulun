#!/usr/bin/env python3
"""生成 strict carrier-lcm valuation overflow 吸收前沿路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_carrier_lcm_overflow_absorption_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.json

输出：
  data/carrier-lcm-overflow-atom-sample-ledger.json
  docs/monograph/prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.json
  docs/monograph/prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.md"
OUT_LEDGER = DATA / "carrier-lcm-overflow-atom-sample-ledger.json"

HARDPOINT = "CarrierLCMValuationOverflowReturnExclusionOrAbsorption"
PREFIX_OVERFLOW = "PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn"
STEP_ORIGIN = "ColdPrefixStepQuotientOriginMapToCarrierRows"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json",
    DOCS / "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    DOCS / "prime-matrix-strict-unified-budget-after-named-sync-router.json",
    DOCS / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
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
    """用确定性试除分解正整数；仅用于证书样本。"""
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


def max_budget(carrier_quotients: list[int]) -> dict[int, int]:
    """计算 carrier-lcm 的素数指数预算。"""
    result: dict[int, int] = {}
    for quotient in carrier_quotients:
        for prime, exp in factor(quotient).items():
            result[prime] = max(result.get(prime, 0), exp)
    return result


def classify_overflow_atoms(carrier_quotients: list[int], prefix_steps: list[int]) -> dict[str, Any]:
    """把 valuation overflow 拆成来源域缺陷或重复 token 溢出。"""
    budget = max_budget(carrier_quotients)
    step_factors = [factor(step) for step in prefix_steps]
    usage: dict[int, int] = {}
    for row in step_factors:
        for prime, exp in row.items():
            usage[prime] = usage.get(prime, 0) + exp

    atoms = []
    for prime, used in sorted(usage.items()):
        allowed = budget.get(prime, 0)
        if used <= allowed:
            continue
        per_step_over = [
            {"step_index": idx, "step": prefix_steps[idx], "step_exp": row.get(prime, 0)}
            for idx, row in enumerate(step_factors)
            if row.get(prime, 0) > allowed
        ]
        hit_steps = [idx for idx, row in enumerate(step_factors) if row.get(prime, 0) > 0]
        if per_step_over:
            atom_type = "single_step_domain_overflow"
            route = STEP_ORIGIN
        elif len(hit_steps) >= 2:
            atom_type = "repeated_token_overflow"
            route = NAMED_RETURN
        else:
            atom_type = "unregistered_carrier_capacity_gap"
            route = STEP_ORIGIN
        atoms.append(
            {
                "prime": prime,
                "used_exp": used,
                "allowed_exp": allowed,
                "deficit": used - allowed,
                "hit_steps": hit_steps,
                "atom_type": atom_type,
                "route": route,
                "per_step_over": per_step_over,
            }
        )
    return {
        "carrier_quotients": carrier_quotients,
        "prefix_steps": prefix_steps,
        "carrier_budget": {str(k): v for k, v in sorted(budget.items())},
        "overflow_atoms": atoms,
        "has_overflow": bool(atoms),
        "all_overflows_named": all(atom["route"] in {STEP_ORIGIN, NAMED_RETURN} for atom in atoms),
    }


def sample_ledger() -> dict[str, Any]:
    """生成 overflow 原子拆分样本。"""
    samples = [
        {
            "case": "multi_step_repeated_token",
            "carrier_quotients": [6, 10],
            "prefix_steps": [2, 2, 3],
        },
        {
            "case": "single_step_outside_carrier_domain",
            "carrier_quotients": [3, 5],
            "prefix_steps": [4],
        },
        {
            "case": "prime_power_repeat_beyond_lcm_height",
            "carrier_quotients": [4, 9],
            "prefix_steps": [2, 2, 2],
        },
    ]
    rows = []
    for item in samples:
        rows.append({**item, "classification": classify_overflow_atoms(item["carrier_quotients"], item["prefix_steps"])})
    return {
        "ledger_type": "carrier_lcm_overflow_atom_sample_ledger",
        "rule": "split overflow into single-step domain defect or repeated-token named return",
        "rows": rows,
        "all_sample_overflows_named": all(row["classification"]["all_overflows_named"] for row in rows),
        "sample_contains_step_origin_defect": any(
            any(atom["route"] == STEP_ORIGIN for atom in row["classification"]["overflow_atoms"])
            for row in rows
        ),
        "sample_contains_named_return": any(
            any(atom["route"] == NAMED_RETURN for atom in row["classification"]["overflow_atoms"])
            for row in rows
        ),
    }


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_carrier_lcm_overflow_absorption_frontier_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/carrier-lcm-overflow-atom-sample-ledger.json": sha256(OUT_LEDGER),
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取 overflow 吸收前沿需要的导入。"""
    prefix = load_json(DOCS / "prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json")
    named = load_json(DOCS / "prime-matrix-strict-named-return-after-rowfree-sync-router.json")
    unified = load_json(DOCS / "prime-matrix-strict-unified-budget-after-named-sync-router.json")
    sparse = load_json(DOCS / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json")
    kernel = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    return {
        "target_imported": prefix.get("next_direct_attack_target") == HARDPOINT,
        "overflow_named_return_ledger_imported": bool(
            prefix.get("carrier_lcm_valuation_overflow_named_return_ledger_closed")
        ),
        "named_return_alphabet_compression_imported": bool(named.get("named_return_alphabet_compression_closed")),
        "nonpersistent_to_budget_imported": named.get("nonpersistent_named_return_budget_absorbed") is False,
        "unified_budget_latest_sync_imported": bool(unified.get("unified_budget_latest_sync_closed")),
        "sparse_budget_still_open": unified.get("sparse_history_demand_exceeds_nonpersistent_supply_budget_proved")
        is False,
        "persistent_terminal_still_open": unified.get("persistent_terminal_family_excluded") is False,
        "sparse_history_no_silent_collapse_imported": bool(
            sparse.get("prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget")
        ),
        "common_kernel_no_free_cycle_imported": bool(kernel.get("free_common_kernel_return_cycle_excluded")),
    }


def split_rows() -> list[dict[str, str]]:
    """列出 overflow 原子拆分。"""
    return [
        {
            "atom": "single_step_domain_overflow",
            "trigger": "some step g has v_p(g)>B_p",
            "route": STEP_ORIGIN,
            "meaning": "该 step 本身不属于 carrier-lcm 商域，必须证明来源映射或登记来源域缺陷。",
        },
        {
            "atom": "repeated_token_overflow",
            "trigger": "each step fits locally, but sum_step v_p(g)>B_p",
            "route": NAMED_RETURN,
            "meaning": "多步重复消耗同一 p-token；进入素数幂级联/共同核/固定历史/PDEC/SAE/热核心。",
        },
        {
            "atom": "nonpersistent_named_overflow",
            "trigger": "overflow key does not persist beyond finite threshold",
            "route": UNIFIED_BUDGET,
            "meaning": "非持久回流不是独立出口，必须由同参数 U_cold/稀疏历史预算吸收。",
        },
        {
            "atom": "persistent_named_overflow",
            "trigger": "same overflow key persists beyond threshold",
            "route": PERSISTENT_TERMINAL,
            "meaning": "持久复现进入固定历史、PDEC/CleanKLS 或 moving-atom 终端族。",
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
    atom_split_closed = (
        flags["target_imported"]
        and flags["overflow_named_return_ledger_imported"]
        and ledger["all_sample_overflows_named"]
    )
    reduction_closed = (
        atom_split_closed
        and flags["named_return_alphabet_compression_imported"]
        and flags["unified_budget_latest_sync_imported"]
        and flags["sparse_history_no_silent_collapse_imported"]
        and flags["common_kernel_no_free_cycle_imported"]
    )
    return [
        decision_row(
            "CarrierLCMOverflowTargetImported",
            True,
            flags["target_imported"],
            "上一层已把剩余压成 valuation overflow return 的排斥或吸收。",
            HARDPOINT,
        ),
        decision_row(
            "OverflowAtomSplitClosed",
            atom_split_closed,
            atom_split_closed,
            "overflow 原子只能是单步来源域缺陷或多步重复 token 命名回流。",
            f"{STEP_ORIGIN} OR {NAMED_RETURN}",
        ),
        decision_row(
            "NamedReturnAlphabetCompressionImported",
            True,
            flags["named_return_alphabet_compression_imported"],
            "命名回流字母表已压成非持久预算吸收与持久终端族排斥。",
            f"{UNIFIED_BUDGET} AND {PERSISTENT_TERMINAL}",
        ),
        decision_row(
            "CarrierLCMOverflowIndependentHardpointRemoved",
            reduction_closed,
            reduction_closed,
            "carrier-lcm overflow 不再是独立未命名硬点；它归入来源域、统一预算或持久终端族。",
            f"{STEP_ORIGIN} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        ),
        decision_row(
            "CarrierLCMValuationOverflowReturnExclusionOrAbsorptionProved",
            False,
            False,
            "虽然独立硬点已压缩，但 step 来源域、非持久预算反超和持久终端族排斥仍未完成。",
            f"{STEP_ORIGIN} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        ),
        decision_row(
            "ColdPrefixProductDividesCarrierLCMH0LedgerProved",
            False,
            False,
            "overflow 分支尚未全部排斥或吸收，仍不能声明所有 prefix product 整除 carrier-lcm h0。",
            HARDPOINT,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{STEP_ORIGIN} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 overflow 吸收前沿证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    ledger = sample_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    flags = imported_flags()
    decisions = decision_rows(flags, ledger)
    independent_removed = next(
        item for item in decisions if item["gate"] == "CarrierLCMOverflowIndependentHardpointRemoved"
    )["proved"]
    return {
        "certificate_type": "prime_matrix_strict_carrier_lcm_overflow_absorption_frontier_router",
        "status": "carrier_lcm_overflow_reduced_to_origin_budget_persistent_terminal_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{STEP_ORIGIN} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        "next_direct_attack_target": STEP_ORIGIN,
        "parallel_attack_targets": [SPARSE_BUDGET, PERSISTENT_TERMINAL, DSTRUCTURE],
        "imported_flags": flags,
        "overflow_atom_split_rows": split_rows(),
        "sample_ledger_path": str(OUT_LEDGER.relative_to(ROOT)),
        "sample_ledger_sha256": sha256(OUT_LEDGER),
        "decision_table": decisions,
        "overflow_atom_split_closed": bool(
            next(item for item in decisions if item["gate"] == "OverflowAtomSplitClosed")["proved"]
        ),
        "carrier_lcm_overflow_independent_hardpoint_removed": bool(independent_removed),
        "carrier_lcm_valuation_overflow_return_exclusion_or_absorption_proved": False,
        "cold_prefix_step_quotient_origin_map_to_carrier_rows_proved": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "persistent_terminal_family_excluded": False,
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`CarrierLCMValuationOverflowReturnExclusionOrAbsorption` 已被压缩："
            "overflow 原子只有两种非循环形态。若单个 step 的 p-adic 指数已超过 `h0^car` 预算，"
            "那是 `ColdPrefixStepQuotientOriginMapToCarrierRows` 来源域缺陷；若每步局部可容纳但多步累计超载，"
            "那是重复 p-token，必须进入已命名的素数幂级联/共同核/固定历史/PDEC/SAE/热核心出口。"
            "因此 carrier-lcm overflow 不再是独立无名硬点。真正剩余为：step 来源域映射、"
            "非持久稀疏历史预算反超，以及持久终端族排斥。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict carrier-lcm overflow 吸收前沿路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "overflow_atom_split_closed",
        "carrier_lcm_overflow_independent_hardpoint_removed",
        "carrier_lcm_valuation_overflow_return_exclusion_or_absorption_proved",
        "cold_prefix_step_quotient_origin_map_to_carrier_rows_proved",
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved",
        "persistent_terminal_family_excluded",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. Overflow 原子拆分")
    lines.append("")
    lines.append("| atom | trigger | route | meaning |")
    lines.append("| --- | --- | --- | --- |")
    for item in result["overflow_atom_split_rows"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["atom", "trigger", "route", "meaning"])
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
    lines.append(f"- 同步硬点：`{SPARSE_BUDGET}` 与 `{PERSISTENT_TERMINAL}`。")
    lines.append("- 边界：本步删除 overflow 独立黑箱，不排斥所有 overflow 分支。")
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
    print(f"overflow_atom_split_closed={fmt_bool(result['overflow_atom_split_closed'])}")
    print(
        "carrier_lcm_overflow_independent_hardpoint_removed="
        f"{fmt_bool(result['carrier_lcm_overflow_independent_hardpoint_removed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
