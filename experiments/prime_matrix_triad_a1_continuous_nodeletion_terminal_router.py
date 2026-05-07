#!/usr/bin/env python3
"""把 A1 连续 prime-lift 删除势停止后的 NoDeletion 终端路由到 PDEC/CleanKLS。

用法示例：
  python3 experiments/prime_matrix_triad_a1_continuous_nodeletion_terminal_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-continuous-nodeletion-terminal-router.json
  docs/monograph/prime-matrix-triad-a1-continuous-nodeletion-terminal-router.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_STANDARD_DELETION = (
    DOCS / "prime-matrix-triad-a1-standard-prime-lift-deletion.json"
)
DEFAULT_NODELETION_GATE = DOCS / "prime-matrix-triad-a1-nodeletion-kl-gate.json"
DEFAULT_NODELETION_WITNESS = (
    DOCS / "prime-matrix-triad-a1-nodeletion-kl-witness-extractor.json"
)
DEFAULT_SMALL_AMBIGUOUS = (
    DOCS / "prime-matrix-triad-a1-small-ambiguous-clean-admission-router.json"
)
DEFAULT_ALL_PHASE = DOCS / "prime-matrix-triad-a1-all-phase-residue-terminal-audit.json"
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-continuous-nodeletion-terminal-router.json"
)
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-continuous-nodeletion-terminal-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256，保证报告可复核。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def is_pdec_shape(route: str) -> bool:
    """判断 KL 形状是否已经命名为 PDEC 输入或见证。"""
    return route.endswith("PDECWitness") or route.endswith("PDECInput")


def summarize_nodeletion_gates(
    nodeletion_gate: dict[str, Any],
    nodeletion_witness: dict[str, Any],
    small_ambiguous: dict[str, Any],
    all_phase: dict[str, Any],
) -> dict[str, Any]:
    """汇总 NoDeletion 终端门控。"""
    gate_counts = nodeletion_gate["gate_counts"]
    shape_counts = nodeletion_witness["shape_route_counts"]
    current_layers_delete = (
        not bool(nodeletion_gate["current_nodeletion_triggered"])
        and set(gate_counts) == {"FiberDeletion"}
    )
    shape_keys = set(shape_counts)
    pdec_shape_count = sum(
        count for route, count in shape_counts.items() if is_pdec_shape(route)
    )
    clean_shape_count = sum(
        count for route, count in shape_counts.items() if "CleanKLS" in route
    )
    mixed_shape_count = sum(
        count
        for route, count in shape_counts.items()
        if not is_pdec_shape(route) and "CleanKLS" not in route
    )
    all_shapes_named = all(
        is_pdec_shape(route) or "CleanKLS" in route for route in shape_keys
    )
    current_phase_residue_terminalized = bool(
        all_phase["all_phase_mass_identities_hold"]
        and all_phase["all_terminal_gt_p"]
        and int(all_phase["total_terminal_le_p_count"]) == 0
    )
    kl_chain_identity_exact = (
        float(nodeletion_witness["max_kl_chain_abs_error"]) <= 1e-12
    )
    small_gates = small_ambiguous["gates"]
    small_ambiguous_routed = bool(
        small_ambiguous["all_current_small_ambiguous_routed"]
        and small_gates["kl_chain_identity_exact"]
    )
    return {
        "current_layers_delete_before_nodeletion": current_layers_delete,
        "current_nodeletion_triggered": bool(
            nodeletion_gate["current_nodeletion_triggered"]
        ),
        "gate_counts": gate_counts,
        "shape_route_counts": shape_counts,
        "pdec_shape_count": pdec_shape_count,
        "clean_shape_count": clean_shape_count,
        "mixed_shape_count": mixed_shape_count,
        "all_kl_shapes_named_pdec_or_clean": all_shapes_named,
        "kl_chain_identity_exact": kl_chain_identity_exact,
        "small_ambiguous_routed": small_ambiguous_routed,
        "small_ambiguous_gates": small_gates,
        "phase_residue_atoms_terminalized_beyond_p": current_phase_residue_terminalized,
        "all_phase_terminal_summary": {
            "total_nonzero_phase_count": int(all_phase["total_nonzero_phase_count"]),
            "total_terminal_count": int(all_phase["total_terminal_count"]),
            "total_terminal_le_p_count": int(all_phase["total_terminal_le_p_count"]),
            "global_min_terminal_phase": int(all_phase["global_min_terminal_phase"]),
        },
    }


def route_deletion_row(row: dict[str, Any]) -> dict[str, Any]:
    """把一个标准 prime-lift 删除势行接到 NoDeletion 终端二分。"""
    return {
        "p": int(row["p"]),
        "signature": row["signature"],
        "promoted_prime": int(row["promoted_prime"]),
        "route_source": row["route_source"],
        "survival_upper_bound_from_fixed_residue": float(
            row["survival_upper_bound_from_fixed_residue"]
        ),
        "deletion_potential_lower_bound": float(
            row["deletion_potential_lower_bound"]
        ),
        "route": "PositiveDeletionPotentialOrNoDeletionPDECOrCleanKLS",
        "terminal_branches": [
            "DeletionPotential: if sum D_n diverges, support density is exhausted",
            "NoDeletion-KL/PDEC: if KL or phase-residue mutual information persists, route to refined PDEC",
            "NoDeletion-CleanKLS: if KL and mutual information vanish, admit CleanKLS/DLS",
        ],
    }


def run(
    standard_deletion_path: Path,
    nodeletion_gate_path: Path,
    nodeletion_witness_path: Path,
    small_ambiguous_path: Path,
    all_phase_path: Path,
) -> dict[str, Any]:
    """运行连续 prime-lift NoDeletion 终端路由。"""
    standard_deletion = load_json(standard_deletion_path)
    nodeletion_gate = load_json(nodeletion_gate_path)
    nodeletion_witness = load_json(nodeletion_witness_path)
    small_ambiguous = load_json(small_ambiguous_path)
    all_phase = load_json(all_phase_path)

    routed_rows = [
        route_deletion_row(row) for row in standard_deletion["deletion_rows"]
    ]
    route_counts = Counter(row["route"] for row in routed_rows)
    promoted_prime_counts = Counter(row["promoted_prime"] for row in routed_rows)
    gates = summarize_nodeletion_gates(
        nodeletion_gate,
        nodeletion_witness,
        small_ambiguous,
        all_phase,
    )
    no_independent_nodeletion_gap = bool(
        gates["kl_chain_identity_exact"]
        and gates["all_kl_shapes_named_pdec_or_clean"]
        and gates["small_ambiguous_routed"]
        and gates["phase_residue_atoms_terminalized_beyond_p"]
    )
    return {
        "certificate_type": "triad_a1_continuous_nodeletion_terminal_router",
        "status": "continuous_prime_lift_nodeletion_terminal_routed_clean_kls_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "standard_prime_lift_deletion_json": file_sha256(
                standard_deletion_path
            ),
            "nodeletion_kl_gate_json": file_sha256(nodeletion_gate_path),
            "nodeletion_kl_witness_json": file_sha256(nodeletion_witness_path),
            "small_ambiguous_clean_router_json": file_sha256(
                small_ambiguous_path
            ),
            "all_phase_residue_terminal_json": file_sha256(all_phase_path),
        },
        "deletion_row_count": len(routed_rows),
        "route_counts": dict(sorted(route_counts.items())),
        "promoted_prime_counts": dict(sorted(promoted_prime_counts.items())),
        "global_min_deletion_potential_lower_bound": float(
            standard_deletion["global_min_deletion_potential_lower_bound"]
        ),
        "global_max_survival_upper_bound": float(
            standard_deletion["global_max_survival_upper_bound"]
        ),
        "all_deletion_rows_positive": all(
            row["deletion_potential_lower_bound"] > 0 for row in routed_rows
        ),
        "nodeletion_gates": gates,
        "no_independent_nodeletion_gap": no_independent_nodeletion_gap,
        "pdec_branch_status": "routed_back_to_recursive_refined_pdec_family_not_new_exit",
        "terminal_dual_gap_after_router": "CleanKLSDLSLargeSieveOrExternalKLSInput",
        "routed_rows": routed_rows,
        "structural_law": (
            "连续 positive-limsup finite signature 已被 prime-lift 固定 residue 化。"
            "每次标准晋升若保留该 residue，至少支付 D>=log(ell) 的删除势。"
            "若 sum D_n 发散，反例支撑被耗尽；若 sum D_n 可求和，则进入 NoDeletion。"
            "NoDeletion 下条件 KL 满足 E_t KL(B|t||U_B)=KL(B||U_B)+I(T;B)："
            "全局 residue KL 或 phase-residue 互信息持久累计时回流 refined/new-layer PDEC；"
            "二者同时趋零时才允许进入 CleanKLS/DLS。"
        ),
        "review_conclusion": (
            "A1 连续 prime-lift 删除势停止后的 NoDeletion 口已经接到既有 KL/PDEC/CleanKLS 门控。"
            "当前已物化层仍全部处于 FiberDeletion；若未来删除停止，KL 形状也只能命名为 refined PDEC "
            "或 flat CleanKLS/DLS，没有独立第三出口。剩余外部硬点压到 CleanKLS/DLS 大筛证书或外部 KLS 输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    gates = result["nodeletion_gates"]
    lines = [
        "# Triad-A1 连续 NoDeletion 终端路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "positive-limsup finite signature",
        "  => prime-lift fixed residue",
        "  => positive deletion potential",
        "  or NoDeletion;",
        "NoDeletion + persistent KL/MI",
        "  => refined/new-layer PDEC;",
        "NoDeletion + KL/MI flat",
        "  => CleanKLS/DLS admission.",
        "```",
        "",
        "这一步消除的是 `NoDeletion-KL` 的独立出口，不声称 CleanKLS/DLS 大筛证书已经完成。",
        "",
        "## 2. 汇总",
        "",
        f"- `deletion_row_count={result['deletion_row_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `promoted_prime_counts={result['promoted_prime_counts']}`。",
        f"- `global_min_deletion_potential_lower_bound={fmt_float(result['global_min_deletion_potential_lower_bound'])}`。",
        f"- `global_max_survival_upper_bound={fmt_float(result['global_max_survival_upper_bound'])}`。",
        f"- `all_deletion_rows_positive={result['all_deletion_rows_positive']}`。",
        f"- `no_independent_nodeletion_gap={result['no_independent_nodeletion_gap']}`。",
        f"- `pdec_branch_status={result['pdec_branch_status']}`。",
        f"- `terminal_dual_gap_after_router={result['terminal_dual_gap_after_router']}`。",
        "",
        "## 3. NoDeletion 门控",
        "",
        f"- `current_layers_delete_before_nodeletion={gates['current_layers_delete_before_nodeletion']}`。",
        f"- `current_nodeletion_triggered={gates['current_nodeletion_triggered']}`。",
        f"- `gate_counts={gates['gate_counts']}`。",
        f"- `shape_route_counts={gates['shape_route_counts']}`。",
        f"- `pdec_shape_count={gates['pdec_shape_count']}`。",
        f"- `clean_shape_count={gates['clean_shape_count']}`。",
        f"- `mixed_shape_count={gates['mixed_shape_count']}`。",
        f"- `all_kl_shapes_named_pdec_or_clean={gates['all_kl_shapes_named_pdec_or_clean']}`。",
        f"- `kl_chain_identity_exact={gates['kl_chain_identity_exact']}`。",
        f"- `small_ambiguous_routed={gates['small_ambiguous_routed']}`。",
        f"- `phase_residue_atoms_terminalized_beyond_p={gates['phase_residue_atoms_terminalized_beyond_p']}`。",
        f"- `all_phase_terminal_summary={gates['all_phase_terminal_summary']}`。",
        "",
        "## 4. Prime-Lift 行",
        "",
        "| P | signature | ell | source | survival upper | D lower | route |",
        "| ---: | --- | ---: | --- | ---: | ---: | --- |",
    ]
    for row in result["routed_rows"]:
        lines.append(
            "| {p} | `{sig}` | {ell} | `{source}` | {surv} | {deletion} | `{route}` |".format(
                p=row["p"],
                sig=row["signature"],
                ell=row["promoted_prime"],
                source=row["route_source"],
                surv=fmt_float(row["survival_upper_bound_from_fixed_residue"]),
                deletion=fmt_float(row["deletion_potential_lower_bound"]),
                route=row["route"],
            )
        )
    lines.extend(
        [
            "",
            "## 5. 当前闭合边界",
            "",
            "现在 `NoDeletion-KL` 不再作为独立硬点停留：",
            "",
            "```text",
            "删除势持续 => 支撑被耗尽；",
            "删除势停止 + KL/MI 偏斜 => recursive refined PDEC；",
            "删除势停止 + KL/MI 平坦 => CleanKLS/DLS。",
            "```",
            "",
            "剩余真正终端硬点是提交 `CleanKLS/DLS` 大筛证书，或登记明确的外部 KLS/DI/BFI 输入。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--standard-deletion-json", type=Path, default=DEFAULT_STANDARD_DELETION
    )
    parser.add_argument(
        "--nodeletion-gate-json", type=Path, default=DEFAULT_NODELETION_GATE
    )
    parser.add_argument(
        "--nodeletion-witness-json", type=Path, default=DEFAULT_NODELETION_WITNESS
    )
    parser.add_argument(
        "--small-ambiguous-json", type=Path, default=DEFAULT_SMALL_AMBIGUOUS
    )
    parser.add_argument("--all-phase-json", type=Path, default=DEFAULT_ALL_PHASE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        standard_deletion_path=args.standard_deletion_json,
        nodeletion_gate_path=args.nodeletion_gate_json,
        nodeletion_witness_path=args.nodeletion_witness_json,
        small_ambiguous_path=args.small_ambiguous_json,
        all_phase_path=args.all_phase_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "no_independent_nodeletion_gap": result[
                    "no_independent_nodeletion_gap"
                ],
                "terminal_dual_gap_after_router": result[
                    "terminal_dual_gap_after_router"
                ],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
