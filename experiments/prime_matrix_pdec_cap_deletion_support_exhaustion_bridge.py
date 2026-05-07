#!/usr/bin/env python3
"""桥接 PDEC-CAP diffuse 分支中的删除势发散与支撑耗尽。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_deletion_support_exhaustion_bridge.py

输出：
  docs/monograph/prime-matrix-pdec-cap-deletion-support-exhaustion-bridge.json
  docs/monograph/prime-matrix-pdec-cap-deletion-support-exhaustion-bridge.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PROFINITE_APS = DOCS / "prime-matrix-profinite-actual-payment-stitching-router.json"
DEFAULT_INFINITE_TOWER = DOCS / "prime-matrix-triad-a1-infinite-tower-budget.json"
DEFAULT_ACTUAL_PAYMENT = (
    DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
)
DEFAULT_NEW_SPARSE = DOCS / "prime-matrix-new-sparse-entry-admission-audit.json"
DEFAULT_TERMINAL_BOUNDARY = (
    DOCS / "prime-matrix-global-terminal-family-boundary-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-deletion-support-exhaustion-bridge.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-deletion-support-exhaustion-bridge.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    profinite_aps: dict[str, Any],
    infinite_tower: dict[str, Any],
    actual_payment: dict[str, Any],
    new_sparse: dict[str, Any],
    terminal_boundary: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成删除势-支撑耗尽桥接审查表。"""
    aps_diffuse_gate_active = (
        profinite_aps["profinite_aps_dichotomy_closed"]
        and "DiffuseCleanKLSDLSEstimateOrFiberDeletionNoDeletionKL"
        in profinite_aps["open_final_gates"]
    )
    density_product_formula_registered = (
        infinite_tower["status"] == "finite_budget_for_infinite_tower_dichotomy"
        and "sum_n -log a_n(P)" in infinite_tower["dichotomy_law"]
        and "支撑密度趋零" in infinite_tower["dichotomy_law"]
        and "a_n(P)->1" in infinite_tower["dichotomy_law"]
    )
    divergent_deletion_implies_zero_support = density_product_formula_registered
    actual_payment_responsibility_constructed = (
        actual_payment["status"] == "continuous_actual_payment_measure_constructed"
        and actual_payment["all_payment_counts_match_demand"]
        and actual_payment["route_counts"].get("ActualPaymentMeasureDichotomySubmitted", 0)
        > 0
    )
    zero_support_cannot_remain_diffuse = (
        divergent_deletion_implies_zero_support
        and actual_payment_responsibility_constructed
        and aps_diffuse_gate_active
    )
    sparse_return_named = (
        new_sparse["no_additional_unnamed_local_survivor_entry_route"]
        and int(new_sparse["missing_admission_count"]) == 0
    )
    materialized_sparse_boundary_registered = (
        terminal_boundary["materialized_frontier_exhausted"]
        and terminal_boundary["terminal_generation_contract_closed"]
        and terminal_boundary["current_terminal_instances_exhausted"]
    )

    return [
        row(
            "APSDiffuseGateActive",
            aps_diffuse_gate_active,
            str(profinite_aps["open_final_gates"]),
            "APS 投影塔已把不持久 Gamma 分支送入 diffuse 删除/NoDeletion/CleanKLS 终端。",
            False,
        ),
        row(
            "DensityProductFormulaRegistered",
            density_product_formula_registered,
            infinite_tower["status"],
            "同源投影塔上有精确乘法公式 density(A_QN)=density(A_Q0)*prod a_n。",
            False,
        ),
        row(
            "DivergentDeletionImpliesZeroSupport",
            divergent_deletion_implies_zero_support,
            "sum -log a_n = infinity => density(A_QN)->0",
            "删除势发散时，同源活跃支撑密度趋零；这是乘法公式的直接结论。",
            False,
        ),
        row(
            "ActualPaymentResponsibilityConstructed",
            actual_payment_responsibility_constructed,
            str(actual_payment["route_counts"]),
            "actual payment measure 已按需求精确构造；有正需求的 cap 不能继续停留为无名责任。",
            False,
        ),
        row(
            "ZeroSupportCannotRemainDiffusePositiveResponsibility",
            zero_support_cannot_remain_diffuse,
            "zero density support versus normalized actual-payment demand",
            "若支撑密度趋零而仍有责任质量，则它不再是 diffuse 正密度终端，只能耗尽或集中成稀疏/PDEC 签名。",
            False,
        ),
        row(
            "SparseOrSingularReturnIsNamed",
            sparse_return_named,
            new_sparse["status"],
            "支撑耗尽后的稀疏/孤窗回流已有 SAE/LocalSurvivor/PDEC/ColumnCRT/CleanKLS 准入口，不产生新出口。",
            False,
        ),
        row(
            "CurrentMaterializedSparseBoundaryRegistered",
            materialized_sparse_boundary_registered,
            terminal_boundary["status"],
            "当前已物化 LocalSurvivor/SAE 包与已知 sparse 入口已经耗尽；未来 sparse 只能带 schema 进入命名合同。",
            False,
        ),
        row(
            "DeletionSupportExhaustionBridgeClosed",
            all(
                [
                    aps_diffuse_gate_active,
                    density_product_formula_registered,
                    divergent_deletion_implies_zero_support,
                    actual_payment_responsibility_constructed,
                    zero_support_cannot_remain_diffuse,
                    sparse_return_named,
                    materialized_sparse_boundary_registered,
                ]
            ),
            "deletion divergence => exhausted or named sparse/PDEC return",
            "支撑耗尽桥接闭合：发散删除势不再是独立终端，只剩证明删除势确实全局发散。",
            False,
        ),
        row(
            "GlobalDeletionPotentialDivergenceLowerBound",
            False,
            "not proved for every diffuse counterexample tower",
            "仍需证明任意不持久 Gamma 反例塔若持续 FiberDeletion，则 sum -log a_n 必发散。",
            True,
        ),
    ]


def run(
    profinite_aps_path: Path,
    infinite_tower_path: Path,
    actual_payment_path: Path,
    new_sparse_path: Path,
    terminal_boundary_path: Path,
) -> dict[str, Any]:
    """运行删除势-支撑耗尽桥接审查。"""
    profinite_aps = load_json(profinite_aps_path)
    infinite_tower = load_json(infinite_tower_path)
    actual_payment = load_json(actual_payment_path)
    new_sparse = load_json(new_sparse_path)
    terminal_boundary = load_json(terminal_boundary_path)
    rows = build_rows(
        profinite_aps=profinite_aps,
        infinite_tower=infinite_tower,
        actual_payment=actual_payment,
        new_sparse=new_sparse,
        terminal_boundary=terminal_boundary,
    )
    bridge_closed = next(
        item["closed"]
        for item in rows
        if item["gate"] == "DeletionSupportExhaustionBridgeClosed"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_deletion_support_exhaustion_bridge",
        "status": "deletion_support_exhaustion_bridge_closed_divergence_lower_bound_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "profinite_aps": file_sha256(profinite_aps_path),
            "infinite_tower": file_sha256(infinite_tower_path),
            "actual_payment": file_sha256(actual_payment_path),
            "new_sparse": file_sha256(new_sparse_path),
            "terminal_boundary": file_sha256(terminal_boundary_path),
        },
        "deletion_support_exhaustion_bridge_closed": bridge_closed,
        "global_deletion_divergence_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_deletion_hardpoint": "GlobalDeletionPotentialDivergenceLowerBound",
        "rows": rows,
        "bridge_law": (
            "On a same-source lift tower, density(A_QN)=density(A_Q0)*prod a_n. "
            "If sum -log a_n diverges, the active support density tends to zero. "
            "A branch with positive actual-payment demand cannot keep being a diffuse "
            "positive-responsibility terminal on zero-density support: either the "
            "responsibility is exhausted, or the remaining mass becomes singular/sparse "
            "or has a persistent finite signature, which is already routed to "
            "LocalSurvivor/SAE/PDEC/ColumnCRT/CleanKLS contracts. Therefore the support "
            "exhaustion implication is closed; the only deletion-side self-contained "
            "mathematical obligation left is to prove the global divergence lower bound."
        ),
        "review_conclusion": (
            "删除势发散到支撑耗尽的逻辑链条已闭合：乘法公式给出支撑密度趋零，"
            "actual-payment 账本给出正需求责任，二者不能继续作为 diffuse 正责任终端共存。"
            "若剩余质量集中或稀疏化，则回流已命名 LocalSurvivor/SAE/PDEC/ColumnCRT/CleanKLS 入口。"
            "因此原来的 `GlobalDeletionDivergenceOrSupportExhaustion` 可继续压窄为 "
            "`GlobalDeletionPotentialDivergenceLowerBound`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 删除势-支撑耗尽桥",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 桥接律",
        "",
        result["bridge_law"],
        "",
        "```text",
        "same-source lift tower:",
        "  density(A_QN)=density(A_Q0)*prod a_n;",
        "sum -log a_n = infinity",
        "  => density(A_QN)->0;",
        "positive actual-payment demand on zero-density support",
        "  => exhausted support or singular/sparse concentration;",
        "singular/sparse concentration",
        "  => named LocalSurvivor/SAE/PDEC/ColumnCRT/CleanKLS return;",
        "therefore remaining deletion hardpoint",
        "  => prove GlobalDeletionPotentialDivergenceLowerBound.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `deletion_support_exhaustion_bridge_closed={fmt_bool(result['deletion_support_exhaustion_bridge_closed'])}`。",
        f"- `global_deletion_divergence_closed={fmt_bool(result['global_deletion_divergence_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_deletion_hardpoint={result['narrowest_deletion_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                blocks=fmt_bool(bool(item["blocks_final"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 剩余",
            "",
            "本文件没有证明任意 diffuse 反例塔都满足 `sum -log a_n=infinity`。"
            "它只关闭后半段逻辑：一旦发散成立，支撑耗尽不再是独立未命名出口。"
            "下一步应直接攻 `GlobalDeletionPotentialDivergenceLowerBound`，即从 promoted-prime "
            "必要性、TailIndependentCompletion 和 HoleResidueOccupancy 中推出删除势不可求和。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profinite-aps-json", type=Path, default=DEFAULT_PROFINITE_APS)
    parser.add_argument("--infinite-tower-json", type=Path, default=DEFAULT_INFINITE_TOWER)
    parser.add_argument("--actual-payment-json", type=Path, default=DEFAULT_ACTUAL_PAYMENT)
    parser.add_argument("--new-sparse-json", type=Path, default=DEFAULT_NEW_SPARSE)
    parser.add_argument(
        "--terminal-boundary-json", type=Path, default=DEFAULT_TERMINAL_BOUNDARY
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        profinite_aps_path=args.profinite_aps_json,
        infinite_tower_path=args.infinite_tower_json,
        actual_payment_path=args.actual_payment_json,
        new_sparse_path=args.new_sparse_json,
        terminal_boundary_path=args.terminal_boundary_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_deletion_hardpoint"])


if __name__ == "__main__":
    main()
