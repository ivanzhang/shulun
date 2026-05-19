#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit variation run/boundary 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_variation_run_boundary_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedVariationPDECCap"
)

IMPORT = "StableLadderEndpointOrbitSignedVariationImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterVariationRunBoundaryLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterVariationRunBoundaryLedger"
SIGNED_SIDE = "StableLadderEndpointOrbitVariationSignedSideChoiceLedger"
POSITIVE_EDGES = "StableLadderEndpointOrbitPositiveIncrementEdgeSetLedger"
RUN_PARTITION = "StableLadderEndpointOrbitVariationRunPartitionLedger"
BOUNDARY_BUDGET = "StableLadderEndpointOrbitVariationRunBoundaryBudgetDichotomyLedger"
RUN_PACKET = "StableLadderEndpointOrbitIncrementRunSurplusPacketLedger"
BOUNDARY_PACKET = "StableLadderEndpointOrbitVariationBoundaryFluxPacketLedger"
NO_ANON = "NoAnonymousSignedVariationExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterVariationRunBoundaryLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementRunSurplusSAE"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {SIGNED_SIDE} "
    f"AND {POSITIVE_EDGES} AND {RUN_PARTITION} AND {BOUNDARY_BUDGET} "
    f"AND {RUN_PACKET} AND {BOUNDARY_PACKET} AND {NO_ANON} "
    f"AND {SPARSE} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的 signed variation 硬点替换成 run/boundary 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 variation run/boundary 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitSignedVariationImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、full-cycle mean atom、signed variation cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterVariationRunBoundary",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterVariationRunBoundary",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitVariationSignedSideChoice",
            True,
            True,
            "从正 variation 或负 variation 中固定一侧，写成 Z_j=sigma Y_j 且 sum_K (Z_j)_+>=G。",
            SIGNED_SIDE,
        ),
        row(
            "StableLadderEndpointOrbitPositiveIncrementEdgeSet",
            True,
            True,
            "把 K 内满足 Z_j>0 的边作为 active positive increment edges。",
            POSITIVE_EDGES,
        ),
        row(
            "StableLadderEndpointOrbitVariationRunPartition",
            True,
            True,
            "active positive edges 唯一分解为极大连续同符号增量 runs。",
            RUN_PARTITION,
        ),
        row(
            "StableLadderEndpointOrbitVariationRunBoundaryBudgetDichotomy",
            True,
            True,
            "对任意边界预算 B，若 run 数大于 B 则边界通量出口；否则某个 run 承担至少 G/B 的正增量质量。",
            BOUNDARY_BUDGET,
        ),
        row(
            "StableLadderEndpointOrbitIncrementRunSurplusPacket",
            True,
            False,
            "低边界支路登记为同符号增量 run surplus；本步不证明其 SAE。",
            RUN_PACKET,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxPacket",
            True,
            False,
            "高切换支路登记为 variation boundary flux PDEC/cap；本步不排斥该 cap。",
            BOUNDARY_PACKET,
        ),
        row(
            "NoAnonymousSignedVariationExit",
            True,
            True,
            "剩余不再是匿名 signed variation，而是同符号增量 run 或边界通量。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterVariationRunBoundary",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitVariationRunBoundaryCapStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean atom、increment-run SAE、variation boundary flux PDEC/cap 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、increment run、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 variation run/boundary 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "signed variation cap 给出某个有向支撑 K 与符号 sigma，使 sum_{j in K}(sigma Y_j)_+>=G。"
        "把正增量边分解为极大连续 runs。给定边界预算 B，若 run 数超过 B，"
        "则得到高切换边界通量出口；若 run 数不超过 B，则 pigeonhole 给出某个同符号增量 run "
        "承载至少 G/B 的实际增量质量。于是 signed variation 被压成 increment-run surplus 或 variation-boundary flux。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_variation_run_boundary_router",
        "status": "endpoint_orbit_signed_variation_reduced_to_increment_run_or_boundary_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_signed_variation_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_variation_signed_side_choice_closed": True,
        "endpoint_orbit_positive_increment_edge_set_closed": True,
        "endpoint_orbit_variation_run_partition_closed": True,
        "endpoint_orbit_variation_run_boundary_budget_dichotomy_closed": True,
        "endpoint_orbit_increment_run_surplus_packet_registered": True,
        "endpoint_orbit_variation_boundary_flux_packet_registered": True,
        "anonymous_signed_variation_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_increment_run_surplus_sae_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "variation_run_boundary_formulas": {
            "imported_variation": "sum_{j in K}(sigma*Y_j)_+>=G",
            "positive_edges": "E_+={j in K: sigma*Y_j>0}",
            "run_partition": "E_+=disjoint union of maximal consecutive runs R_h",
            "budget_boundary": "if number_of_runs>B then VariationBoundaryFluxPDECCap",
            "budget_run": "if number_of_runs<=B then exists h: sum_{j in R_h}sigma*Y_j>=G/B",
            "new_exit": "EndpointOrbitIncrementRunSurplusSAEOrEndpointOrbitVariationBoundaryFluxPDECCap",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix stable-ladder endpoint orbit variation run/boundary 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_signed_variation_imported={fmt_bool(cert['endpoint_orbit_signed_variation_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_variation_signed_side_choice_closed={fmt_bool(cert['endpoint_orbit_variation_signed_side_choice_closed'])}",
        f"endpoint_orbit_positive_increment_edge_set_closed={fmt_bool(cert['endpoint_orbit_positive_increment_edge_set_closed'])}",
        f"endpoint_orbit_variation_run_partition_closed={fmt_bool(cert['endpoint_orbit_variation_run_partition_closed'])}",
        f"endpoint_orbit_variation_run_boundary_budget_dichotomy_closed={fmt_bool(cert['endpoint_orbit_variation_run_boundary_budget_dichotomy_closed'])}",
        f"endpoint_orbit_increment_run_surplus_packet_registered={fmt_bool(cert['endpoint_orbit_increment_run_surplus_packet_registered'])}",
        f"endpoint_orbit_variation_boundary_flux_packet_registered={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_packet_registered'])}",
        f"anonymous_signed_variation_removed={fmt_bool(cert['anonymous_signed_variation_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_increment_run_surplus_sae_proved={fmt_bool(cert['endpoint_orbit_increment_run_surplus_sae_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. signed variation 包",
        "",
        "上一层给出某个有向支撑 `K` 与符号 `sigma`：",
        "",
        "```text",
        "sum_{j in K}(sigma*Y_j)_+ >= G.",
        "```",
        "",
        "## 2. 正增量边与 runs",
        "",
        "令：",
        "",
        "```text",
        "E_+={j in K: sigma*Y_j>0}.",
        "```",
        "",
        "`E_+` 唯一分解为极大连续 runs：",
        "",
        "```text",
        "E_+=R_1 disjoint union ... disjoint union R_b.",
        "```",
        "",
        "## 3. 边界预算二分",
        "",
        "给定边界预算 `B`。若 `b>B`，登记为 variation boundary flux PDEC/cap。若 `b<=B`，则由 pigeonhole：",
        "",
        "```text",
        "exists h: sum_{j in R_h} sigma*Y_j >= G/B.",
        "```",
        "",
        "这就是新的 increment-run surplus packet。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 endpoint orbit signed variation PDEC/cap 变成 increment-run surplus SAE 或 variation-boundary flux PDEC/cap，外加 endpoint singleton atom、full-cycle mean atom 与 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 5. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有证明 endpoint singleton atom/SAE。",
            "- 本证书没有证明 EndpointOrbitFullCycleMeanAtomSAE。",
            "- 本证书没有证明 EndpointOrbitIncrementRunSurplusSAE。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 signed variation cap 压成同符号增量 run 或高边界通量二分。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """生成 JSON、ledger 与 Markdown 归档。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
