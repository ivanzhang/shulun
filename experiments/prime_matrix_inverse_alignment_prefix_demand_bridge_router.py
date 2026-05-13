#!/usr/bin/env python3
"""把逆元对齐零行行号桥接到 prefix demand / M# 预算链。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_prefix_demand_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-prefix-demand-bridge-router.json

输出：
  data/inverse-alignment-prefix-demand-bridge-sample-ledger.json
  docs/monograph/prime-matrix-inverse-alignment-prefix-demand-bridge-router.json
  docs/monograph/prime-matrix-inverse-alignment-prefix-demand-bridge-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-prefix-demand-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-prefix-demand-bridge-router.md"
OUT_LEDGER = DATA / "inverse-alignment-prefix-demand-bridge-sample-ledger.json"

NORMALIZED_POTENTIAL = "NormalizedPrefixResidualPotentialLowerBound"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
SHORT_INTERVAL = "PrimeGapBelowP2ForAllPBlocks"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-inverse-alignment-covering-system-router.json",
    DOCS / "prime-matrix-strict-prefix-residual-transfer-router.json",
    DOCS / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json",
    DOCS / "prime-matrix-strict-normalized-prefix-potential-router.json",
    DOCS / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json",
    DOCS / "prime-matrix-strict-sparse-budget-after-unified-sync-router.json",
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


def zero_row(P: int, x: int) -> bool:
    """判断行 x 是否被所有 q<P 覆盖。"""
    qs = primes_upto(P - 1)
    return all(any((x * P + c) % q == 0 for q in qs) for c in range(1, P))


def row_phase(P: int, x: int) -> list[dict[str, int]]:
    """生成行 x 的逆元相位向量。"""
    rows = []
    for q in primes_upto(P - 1):
        residue = (-x * P) % q
        positive = q if residue == 0 else residue
        mu = 1 + (P - 1 - positive) // q if positive <= P - 1 else 0
        rows.append({"q": q, "covered_c_mod_q": residue, "positive_representative": positive, "mu_q": mu})
    return rows


def prefix_atoms(P: int, x: int, z: int) -> list[dict[str, Any]]:
    """由逆元相位向量生成 prefix 残洞 atom。"""
    qs = primes_upto(P - 1)
    small = [q for q in qs if q <= z]
    large = [q for q in qs if q > z]
    atoms: list[dict[str, Any]] = []
    for c in range(1, P):
        if any((x * P + c) % q == 0 for q in small):
            continue
        tau = next((q for q in large if (x * P + c) % q == 0), None)
        if tau is None:
            atoms.append({"c": c, "tau_z": None, "status": "uncovered_after_z"})
            continue
        positive = (-x * P) % tau
        positive = tau if positive == 0 else positive
        mu = 1 + (P - 1 - positive) // tau if positive <= P - 1 else 0
        atoms.append(
            {
                "c": c,
                "tau_z": tau,
                "mu_tau": mu,
                "weight": 1 / mu if mu else None,
                "label_band": "completed_internal" if tau <= x else "incomplete_external",
                "status": "prefix_atom",
            }
        )
    return atoms


def sample_ledger() -> dict[str, Any]:
    """生成小样本，展示逆元行号如何产生 prefix demand。"""
    samples = [
        {"P": 13, "x": 168, "z_values": [3, 5, 7]},
        {"P": 23, "x": 58, "z_values": [5, 7, 11]},
    ]
    rows: list[dict[str, Any]] = []
    for sample in samples:
        P = sample["P"]
        x = sample["x"]
        z_rows = []
        for z in sample["z_values"]:
            atoms = prefix_atoms(P, x, z)
            weights = [a["weight"] for a in atoms if a.get("weight") is not None]
            z_rows.append(
                {
                    "z": z,
                    "R_xz_size": len(atoms),
                    "all_atoms_labeled": all(a.get("tau_z") is not None for a in atoms),
                    "Msharp_exact": sum(weights),
                    "atoms": atoms,
                }
            )
        rows.append(
            {
                "P": P,
                "x": x,
                "zero_row_verified": zero_row(P, x),
                "phase_vector": row_phase(P, x),
                "z_rows": z_rows,
            }
        )
    return {
        "ledger_type": "inverse_alignment_prefix_demand_bridge_sample_ledger",
        "diagnostic_only": True,
        "rows": rows,
    }


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_prefix_demand_bridge_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/inverse-alignment-prefix-demand-bridge-sample-ledger.json": sha256(OUT_LEDGER),
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取桥接依赖状态。"""
    inverse = load_json(DOCS / "prime-matrix-inverse-alignment-covering-system-router.json")
    transfer = load_json(DOCS / "prime-matrix-strict-prefix-residual-transfer-router.json")
    capacity = load_json(DOCS / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json")
    normalized = load_json(DOCS / "prime-matrix-strict-normalized-prefix-potential-router.json")
    forced = load_json(DOCS / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json")
    sparse = load_json(DOCS / "prime-matrix-strict-sparse-budget-after-unified-sync-router.json")
    return {
        "inverse_alignment_equivalence_imported": inverse.get("gcd_system_equivalence_closed") is True
        and inverse.get("inverse_residue_formula_closed") is True,
        "global_min_x_gt_p_proved": inverse.get("global_minimal_alignment_x_gt_P_proved") is True,
        "prefix_transfer_imported": transfer.get("prefix_residual_to_weighted_formal_unit_obligation_transfer_proved")
        is True,
        "capacity_multiplier_imported": capacity.get("registered_prefix_capacity_multiplier_discipline_proved")
        is True,
        "normalized_potential_reduction_imported": normalized.get("multiplier_to_rough_count_reduction_closed")
        is True,
        "forced_load_accounting_imported": forced.get("forced_load_criterion_closed") is True,
        "sparse_budget_normal_form_imported": sparse.get("same_parameter_sparse_demand_cold_supply_normal_form_closed")
        is True,
    }


def bridge_rows() -> list[dict[str, str]]:
    """列出桥接结论。"""
    return [
        {
            "name": "zero_row_position_equals_alignment_solution",
            "statement": "行 x 是零行 iff every c in [1,P-1] is covered by some inverse class q<P.",
            "status": "closed",
        },
        {
            "name": "phase_vector_source",
            "statement": "the vector rho_q(x)=-xP mod q gives the row-position source for all prefix labels.",
            "status": "closed",
        },
        {
            "name": "prefix_atom_selector",
            "statement": "R_{x,z} is exactly the set of columns not hit by q<=z; tau_z(c) is the least q>z hitting c.",
            "status": "closed",
        },
        {
            "name": "capacity_multiplier_match",
            "statement": "mu_q(x;P)=#{1<=c<P:c=rho_q(x) mod q}, matching the existing capacity discipline.",
            "status": "closed",
        },
        {
            "name": "numeric_lower_bound_boundary",
            "statement": "the bridge does not prove |R_{x,z}| lower bounds; it routes them to sieve or short-prime-gap input.",
            "status": "open_boundary",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "InverseAlignmentImportedAsZeroRowPosition",
            "closed": result["inverse_alignment_equivalence_imported"],
            "proved": result["inverse_alignment_equivalence_imported"],
            "meaning": "零行 x 与全 r 逆元覆盖对齐严格等价，x 是实际行号源，不是后验抽象标签。",
            "remaining": "none for row-position interface",
        },
        {
            "gate": "PrefixDemandBridgeClosed",
            "closed": result["inverse_alignment_prefix_demand_bridge_closed"],
            "proved": result["inverse_alignment_prefix_demand_bridge_closed"],
            "meaning": "逆元相位向量直接生成 R_{x,z}、tau_z(c)、mu_q 和 M# 字段。",
            "remaining": "numeric lower bound still open",
        },
        {
            "gate": "CapacityAndForcedLoadCompatibilityClosed",
            "closed": result["capacity_and_forced_load_compatibility_closed"],
            "proved": result["capacity_and_forced_load_compatibility_closed"],
            "meaning": "新行号相位源与既有容量乘子、prefix 转移、强制负载守恒链条完全同字段匹配。",
            "remaining": SPARSE_BUDGET,
        },
        {
            "gate": "MinXGreaterThanPClosedByAlignment",
            "closed": False,
            "proved": False,
            "meaning": "逆元系统本身仍不能证明全局 min x>P；该断言需要短区间素数输入。",
            "remaining": SHORT_INTERVAL,
        },
        {
            "gate": "NormalizedPrefixPotentialProved",
            "closed": False,
            "proved": False,
            "meaning": "R_{x,z} 的字段来源已更具体，但 |R_{x,z}| 统一下界仍需 beta-sieve/有限证书或短区间素数路线。",
            "remaining": NORMALIZED_POTENTIAL,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步加强了反例链源字段和非循环性，不产生最终无条件矛盾。",
            "remaining": f"{SPARSE_BUDGET} AND {DSTRUCTURE}",
        },
    ]


def build_result(ledger: dict[str, Any]) -> dict[str, Any]:
    """构造桥接证书。"""
    flags = imported_flags()
    bridge_closed = all(
        [
            flags["inverse_alignment_equivalence_imported"],
            flags["prefix_transfer_imported"],
            flags["capacity_multiplier_imported"],
            flags["normalized_potential_reduction_imported"],
            flags["forced_load_accounting_imported"],
            flags["sparse_budget_normal_form_imported"],
        ]
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_prefix_demand_bridge_router",
        "status": "inverse_alignment_zero_row_position_synced_to_prefix_demand_numeric_lower_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "inverse_alignment_prefix_demand_bridge_closed": bridge_closed,
        "capacity_and_forced_load_compatibility_closed": bridge_closed,
        "normalized_prefix_potential_lower_bound_proved": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SPARSE_BUDGET,
        "hardpoint_after_router": f"{NORMALIZED_POTENTIAL} OR {SHORT_INTERVAL}",
        "next_direct_attack_target": NORMALIZED_POTENTIAL,
        "alternative_attack_target": SHORT_INTERVAL,
        "bridge_rows": bridge_rows(),
        "sample_ledger": ledger,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "逆元对齐系统可以直接并入当前前沿：假设早期零行存在时，行号 `x` 本身给出"
            "相位向量 `rho_q(x)=-xP mod q`；`R_{x,z}` 正是未被 `q<=z` 命中的列，"
            "`tau_z(c)` 是最小的 `q>z` 覆盖标签，`mu_q` 与现有容量乘子公式完全一致。"
            "因此你的同余方程组不是旁路，而是 `M#_{x,z}` 需求项的具体行号模型。"
            "但它仍不自动给出 `|R_{x,z}|` 的全局下界；若取自然 cutoff 试图证明 `min x>P`，"
            "硬点等价转为短区间素数输入。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix 逆元对齐到 Prefix Demand 桥接路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"inverse_alignment_prefix_demand_bridge_closed={fmt_bool(result['inverse_alignment_prefix_demand_bridge_closed'])}",
        f"capacity_and_forced_load_compatibility_closed={fmt_bool(result['capacity_and_forced_load_compatibility_closed'])}",
        f"normalized_prefix_potential_lower_bound_proved={fmt_bool(result['normalized_prefix_potential_lower_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 桥接结论",
        "",
        "| name | statement | status |",
        "| --- | --- | --- |",
    ]
    for item in result["bridge_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['name'])}`",
                    table_cell(item["statement"]),
                    f"`{table_cell(item['status'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 样本 M# 字段",
            "",
            "| P | x | z | zero row | |R_xz| | all labeled | M# exact |",
            "| ---: | ---: | ---: | --- | ---: | --- | ---: |",
        ]
    )
    for row in result["sample_ledger"]["rows"]:
        for z_row in row["z_rows"]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(row["P"]),
                        str(row["x"]),
                        str(z_row["z"]),
                        f"`{fmt_bool(row['zero_row_verified'])}`",
                        str(z_row["R_xz_size"]),
                        f"`{fmt_bool(z_row['all_atoms_labeled'])}`",
                        f"{z_row['Msharp_exact']:.6f}",
                    ]
                )
                + " |"
            )
    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 备选闭合口：`{result['alternative_attack_target']}`。",
            "- 边界：本步只关闭逆元行号源到 M# 字段的桥接，不证明全局 |R_xz| 下界。",
            "",
            "## 5. 依赖哈希",
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
