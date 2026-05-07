#!/usr/bin/env python3
"""审计 Triad-A1 PDEC DualCap 是否已有同一 formal-unit 的 M_Q 质量来源。

用法示例：
  python3 experiments/prime_matrix_triad_a1_pdec_mass_source_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-pdec-mass-source-router.json
  docs/monograph/prime-matrix-triad-a1-pdec-mass-source-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_SPARSE = DOCS / "prime-matrix-triad-a1-sparsecap-local-survivor.json"
DEFAULT_FORCED = DOCS / "prime-matrix-triad-a1-forcedcap-lift-audit.json"
DEFAULT_PERSISTENT = DOCS / "prime-matrix-triad-a1-persistent-columntail-payment.json"
DEFAULT_BOUNDARY = DOCS / "prime-matrix-triad-a1-materialized-support-boundary-terminal-audit.json"
DEFAULT_ALL_PHASE = DOCS / "prime-matrix-triad-a1-all-phase-residue-terminal-audit.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-pdec-mass-source-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-pdec-mass-source-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件指纹，保证账本来源可追踪。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def int_from_counts(counts: dict[str, Any], key: str) -> int:
    """从计数字典安全取整数。"""
    return int(counts.get(key, 0))


def build_family_routes(
    dual: dict[str, Any],
    sparse: dict[str, Any],
    forced: dict[str, Any],
    persistent: dict[str, Any],
    boundary: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成三类 DualCap 的质量来源与早期出口路由。"""
    class_counts = dual["aggregate_class_counts"]
    sparse_count = int_from_counts(class_counts, "SparseCap")
    persistent_count = int_from_counts(class_counts, "PersistentCap")
    forced_count = int_from_counts(class_counts, "ForcedPersistentByDensityBarrier")

    boundary_closed = bool(boundary["all_boundary_terminals_excluded"])
    boundary_local = bool(boundary["all_phase_le_p_have_local_survivor"])

    return [
        {
            "family": "SparseCap",
            "count": sparse_count,
            "mass_source": "Q=2310 M_Q(t) from LHB multiplicity cap; sparse phase atoms are subsets of supp(M_Q).",
            "mass_source_verified": sparse_count == int(sparse["sparse_descriptor_count"]),
            "pxp_exit_route": "SparseLocalSurvivorOrFinitePDEC",
            "pxp_exit_closed": bool(sparse["all_sparse_caps_closed_for_pxP"]),
            "remaining_terminal_obligation": "finite PDEC packet beyond P; no P-row exit in current sparse atoms.",
        },
        {
            "family": "PersistentCap",
            "count": persistent_count,
            "mass_source": "Q=2310 M_Q(t); cap intersections were recomputed and phase M counts match payment ledger.",
            "mass_source_verified": (
                persistent_count == int(persistent["persistent_cap_count"])
                and bool(persistent["all_intersections_recomputed"])
                and bool(persistent["all_phase_m_counts_match"])
            ),
            "pxp_exit_route": "BoundarySubsetBTLS",
            "pxp_exit_closed": boundary_closed and boundary_local,
            "remaining_terminal_obligation": "ColumnTail/TailAnchor PDEC or distributed CleanKLS/DLS.",
        },
        {
            "family": "ForcedPersistentByDensityBarrier",
            "count": forced_count,
            "mass_source": "Q=2310 M_Q(t), then lifted to Q'=30030 support ledger; old intersections recomputed.",
            "mass_source_verified": (
                forced_count == int(forced["forced_cap_count"])
                and bool(forced["all_old_intersections_recomputed"])
            ),
            "pxp_exit_route": "BoundarySubsetBTLS plus lift monotonicity",
            "pxp_exit_closed": boundary_closed and boundary_local,
            "remaining_terminal_obligation": "next lift, column-tail rows, PDECEntropy, or CleanKLS.",
        },
    ]


def run(args: argparse.Namespace) -> dict[str, Any]:
    """运行 PDEC 质量来源路由审计。"""
    dual = load_json(args.dualcap_json)
    sparse = load_json(args.sparse_json)
    forced = load_json(args.forced_json)
    persistent = load_json(args.persistent_json)
    boundary = load_json(args.boundary_json)
    all_phase = load_json(args.all_phase_json)

    family_routes = build_family_routes(dual, sparse, forced, persistent, boundary)
    all_mass_sources_verified = all(row["mass_source_verified"] for row in family_routes)
    all_pxp_exits_closed = all(row["pxp_exit_closed"] for row in family_routes)

    return {
        "certificate_type": "triad_a1_pdec_mass_source_router",
        "status": "current_dualcap_mass_sources_routed_to_btls_lfte_terminal_open",
        "source_hashes": {
            "router_script": file_sha256(Path(__file__).resolve()),
            "dualcap_json": file_sha256(args.dualcap_json),
            "sparse_json": file_sha256(args.sparse_json),
            "forced_json": file_sha256(args.forced_json),
            "persistent_json": file_sha256(args.persistent_json),
            "boundary_json": file_sha256(args.boundary_json),
            "all_phase_json": file_sha256(args.all_phase_json),
        },
        "dualcap_class_counts": dual["aggregate_class_counts"],
        "dualcap_route_counts": dual["aggregate_route_counts"],
        "family_routes": family_routes,
        "all_current_dualcap_mass_sources_verified": all_mass_sources_verified,
        "all_current_dualcap_pxp_exits_closed": all_pxp_exits_closed,
        "boundary_support_closure": {
            "all_boundary_terminals_excluded": boundary["all_boundary_terminals_excluded"],
            "all_phase_le_p_have_local_survivor": boundary["all_phase_le_p_have_local_survivor"],
            "total_phase_le_p_count": boundary["total_phase_le_p_count"],
            "total_y0_completion_le_p_count": boundary["total_y0_completion_le_p_count"],
        },
        "materialized_lfte_closure": {
            "all_phase_mass_identities_hold": all_phase["all_phase_mass_identities_hold"],
            "all_terminal_gt_p": all_phase["all_terminal_gt_p"],
            "total_nonzero_phase_count": all_phase["total_nonzero_phase_count"],
            "total_terminal_le_p_count": all_phase["total_terminal_le_p_count"],
        },
        "structural_law": (
            "A legal PDEC cap must first attach to the same formal unit C_P and inherit M_Q(t). "
            "If it is a subset of supp(M_Q) and Q>P, BTLS closes the P-row boundary exit. "
            "If a concrete atom is extracted, LFTE expands its remaining high-prime fiber locally."
        ),
        "remaining_obligations": [
            "Prove S subset Z_LHB or an equivalent attachment for any new formal PDEC branch.",
            "For persistent current caps, finish ColumnTail/TailAnchor PDEC or distributed CleanKLS/DLS.",
            "For forced persistent caps, continue lift deletion/KL/CleanKLS routing.",
            "For any cap without same M_Q source, return to Multiplicity-Stitching instead of using BTLS/LFTE.",
        ],
        "review_conclusion": (
            "当前 DualCap 三族都已有可追踪的 M_Q 质量来源；其 P×P 早期出口由 SparseLocalSurvivor "
            "或全支撑 BTLS 子集继承关闭。剩余不是早期行出口，而是 PDEC/CleanKLS 等终端证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 PDEC 质量来源路由器",
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
        "PDEC cap legal use:",
        "  S subset same C_P formal unit;",
        "  g(t)<=M_Q(t);",
        "  cap C subset supp(M_Q);",
        "  Q>P => BTLS checks only C cap [1,P];",
        "  extracted atom => LFTE local fiber expansion.",
        "```",
        "",
        "## 2. DualCap 三族",
        "",
        f"- `dualcap_class_counts={result['dualcap_class_counts']}`。",
        f"- `dualcap_route_counts={result['dualcap_route_counts']}`。",
        f"- `all_current_dualcap_mass_sources_verified={result['all_current_dualcap_mass_sources_verified']}`。",
        f"- `all_current_dualcap_pxp_exits_closed={result['all_current_dualcap_pxp_exits_closed']}`。",
        "",
        "| family | count | mass source verified | P×P exit route | P×P exit closed | remaining obligation |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for row in result["family_routes"]:
        lines.append(
            "| {family} | {count} | `{mass}` | `{route}` | `{closed}` | {obligation} |".format(
                family=row["family"],
                count=row["count"],
                mass=row["mass_source_verified"],
                route=row["pxp_exit_route"],
                closed=row["pxp_exit_closed"],
                obligation=row["remaining_terminal_obligation"],
            )
        )

    boundary = result["boundary_support_closure"]
    lfte = result["materialized_lfte_closure"]
    lines.extend(
        [
            "",
            "## 3. 早期出口读数",
            "",
            f"- `all_boundary_terminals_excluded={boundary['all_boundary_terminals_excluded']}`。",
            f"- `all_phase_le_p_have_local_survivor={boundary['all_phase_le_p_have_local_survivor']}`。",
            f"- `total_phase_le_p_count={boundary['total_phase_le_p_count']}`。",
            f"- `total_y0_completion_le_p_count={boundary['total_y0_completion_le_p_count']}`。",
            f"- `all_phase_mass_identities_hold={lfte['all_phase_mass_identities_hold']}`。",
            f"- `all_terminal_gt_p={lfte['all_terminal_gt_p']}`。",
            f"- `total_nonzero_phase_count={lfte['total_nonzero_phase_count']}`。",
            f"- `total_terminal_le_p_count={lfte['total_terminal_le_p_count']}`。",
            "",
            "## 4. 剩余义务",
            "",
        ]
    )
    for item in result["remaining_obligations"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 5. 读法",
            "",
            "这一步没有排除全部 PDEC，也没有完成全局行命题。",
            "它完成的是当前 DualCap 族的质量来源与早期出口接线：",
            "",
            "```text",
            "SparseCap     => SparseLocalSurvivor / finite PDEC beyond P；",
            "PersistentCap => BTLS 关闭 P 行出口，终端转 ColumnTail 或 CleanKLS；",
            "ForcedCap     => BTLS 关闭 P 行出口，升层后继续 deletion/KL/CleanKLS。",
            "```",
            "",
            "因此当前 PDEC 硬点已经从“是否可能在 P 行内出零行”推进为：",
            "",
            "```text",
            "同一 formal unit 的 PDEC 上界；",
            "或持久支付签名的 ColumnTail/TailAnchor 排斥；",
            "或 clean residual 的 KLS/DLS 证书。",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--sparse-json", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--forced-json", type=Path, default=DEFAULT_FORCED)
    parser.add_argument("--persistent-json", type=Path, default=DEFAULT_PERSISTENT)
    parser.add_argument("--boundary-json", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--all-phase-json", type=Path, default=DEFAULT_ALL_PHASE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_mass_sources_verified": result["all_current_dualcap_mass_sources_verified"],
                "all_pxp_exits_closed": result["all_current_dualcap_pxp_exits_closed"],
                "class_counts": result["dualcap_class_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
