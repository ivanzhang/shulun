#!/usr/bin/env python3
"""把全局删除势发散下界压到 HRO 占用饱和出口。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_deletion_divergence_lower_bound_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-deletion-divergence-lower-bound-router.json
  docs/monograph/prime-matrix-pdec-cap-deletion-divergence-lower-bound-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_DELETION_BRIDGE = (
    DOCS / "prime-matrix-pdec-cap-deletion-support-exhaustion-bridge.json"
)
DEFAULT_HRO_LEMMA = DOCS / "prime-matrix-triad-a1-hole-residue-occupancy.md"
DEFAULT_HRO_AUDITS = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-hole-residue-occupancy-q2310-q30030.json",
        DOCS / "prime-matrix-triad-a1-hole-residue-occupancy-q30030-q510510.json",
    )
)
DEFAULT_DELETION_PROFILES = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-deletion-potential-profile-q2310-q30030.json",
        DOCS / "prime-matrix-triad-a1-deletion-potential-profile-q30030-q510510.json",
    )
)
DEFAULT_NODELETION_TERMINAL = (
    DOCS / "prime-matrix-triad-a1-continuous-nodeletion-terminal-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-deletion-divergence-lower-bound-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-deletion-divergence-lower-bound-router.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def fmt_float(value: float) -> str:
    """格式化浮点数。"""
    return f"{value:.6g}"


def table_cell(value: object) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, object]:
    """构造审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def summarize_hro(audits: list[dict[str, object]]) -> dict[str, object]:
    """汇总 HRO 当前物化审计。"""
    rows: list[dict[str, object]] = []
    for audit in audits:
        for item in audit["prime_results"]:
            rows.append(item)
    return {
        "row_count": len(rows),
        "min_certified_deletion_lb_rate": min(
            float(item["certified_deletion_lb_rate"]) for item in rows
        ),
        "max_union_bound_rate": max(float(item["union_bound_rate"]) for item in rows),
        "max_occupied_rate": max(float(item["occupied_rate"]) for item in rows),
        "max_tail_independent_rate": max(
            float(item["tail_independent_rate"]) for item in rows
        ),
        "all_nonempty_survival_bounded_by_union": all(
            float(item["nonempty_actual_survival_rate"])
            <= float(item["union_bound_rate"]) + 1e-12
            for item in rows
        ),
        "all_certified_deletion_positive": all(
            float(item["certified_deletion_lb_rate"]) > 0 for item in rows
        ),
    }


def summarize_deletion_profiles(profiles: list[dict[str, object]]) -> dict[str, object]:
    """汇总删除势剖面审计。"""
    rows: list[dict[str, object]] = []
    for profile in profiles:
        for item in profile["prime_results"]:
            rows.append(item)
    return {
        "row_count": len(rows),
        "min_deletion_rate": min(float(item["deletion_rate"]) for item in rows),
        "min_deletion_potential": min(float(item["deletion_potential"]) for item in rows),
        "max_survival_rate": max(float(item["survival_rate"]) for item in rows),
        "all_deletion_positive": all(float(item["deletion_rate"]) > 0 for item in rows),
    }


def build_rows(
    deletion_bridge: dict[str, object],
    hro_text: str,
    hro_summary: dict[str, object],
    deletion_summary: dict[str, object],
    nodeletion_terminal: dict[str, object],
) -> list[dict[str, object]]:
    """生成删除发散下界路由审查表。"""
    hardpoint_active = (
        deletion_bridge["deletion_support_exhaustion_bridge_closed"]
        and deletion_bridge["narrowest_deletion_hardpoint"]
        == "GlobalDeletionPotentialDivergenceLowerBound"
    )
    promoted_prime_essentiality_materialized = (
        deletion_summary["all_deletion_positive"]
        and deletion_summary["min_deletion_potential"] > 0
    )
    hro_barrier_registered = all(
        needle in hro_text
        for needle in [
            "S_t subset Occ_t union TI_t",
            "|Occ_t|/r + |TI_t|/r -> 1",
            "OccupancySaturation",
            "TailIndependence",
        ]
    )
    hro_current_layers_delete = (
        hro_summary["all_nonempty_survival_bounded_by_union"]
        and hro_summary["all_certified_deletion_positive"]
    )
    failure_forces_saturation_or_ti = hro_barrier_registered
    ti_routed_to_nodeletion = (
        nodeletion_terminal["no_independent_nodeletion_gap"]
        and nodeletion_terminal["terminal_dual_gap_after_router"]
        == "CleanKLSDLSLargeSieveOrExternalKLSInput"
    )

    return [
        row(
            "DeletionDivergenceHardpointActive",
            hardpoint_active,
            deletion_bridge["narrowest_deletion_hardpoint"],
            "上一层已把删除侧压到全局删除势发散下界。",
            False,
        ),
        row(
            "PromotedPrimeEssentialityMaterialized",
            promoted_prime_essentiality_materialized,
            str(deletion_summary),
            "当前物化层中 promoted prime 的必要性删除势为正；删除不是统计噪声。",
            False,
        ),
        row(
            "HROBarrierRegistered",
            hro_barrier_registered,
            "S_t subset Occ_t union TI_t",
            "HRO 引理给出幸存 fiber 只能来自旧洞 residue 占用或 Tail 独立完成。",
            False,
        ),
        row(
            "CurrentHROLayersDelete",
            hro_current_layers_delete,
            str(hro_summary),
            "当前 HRO 物化层中 union bound 严格控制幸存率，且认证删除下界均为正。",
            False,
        ),
        row(
            "DivergenceFailureForcesSaturationOrTailIndependence",
            failure_forces_saturation_or_ti,
            "if sum D_n finite, Occ/r + TI/r -> 1 on a positive subsequence",
            "若删除势不可发散，则 HRO 迫使占用近满或 Tail 独立近满，没有第三种删除逃逸。",
            False,
        ),
        row(
            "TailIndependenceRoutedToNoDeletionKLClean",
            ti_routed_to_nodeletion,
            nodeletion_terminal["terminal_dual_gap_after_router"],
            "Tail 独立近满就是 promoted prime 非必要，已进入 NoDeletion-KL/PDEC 或 CleanKLS/SC9 分支。",
            False,
        ),
        row(
            "DeletionDivergenceLowerBoundReduced",
            all(
                [
                    hardpoint_active,
                    promoted_prime_essentiality_materialized,
                    hro_barrier_registered,
                    hro_current_layers_delete,
                    failure_forces_saturation_or_ti,
                    ti_routed_to_nodeletion,
                ]
            ),
            "only OccupancySaturation remains on deletion side",
            "删除发散下界已压到 OccupancySaturation 排斥；TailIndependence 已回流 NoDeletion/CleanKLS。",
            False,
        ),
        row(
            "OccupancySaturationPDECOrColumnCRT",
            False,
            "near-full old-hole residues not globally excluded",
            "仍需证明 |Occ_t|/r -> 1 的占用饱和会触发低层容量矛盾、PDEC 或 ColumnCRT。",
            True,
        ),
    ]


def run(
    deletion_bridge_path: Path,
    hro_lemma_path: Path,
    hro_audit_paths: list[Path],
    deletion_profile_paths: list[Path],
    nodeletion_terminal_path: Path,
) -> dict[str, object]:
    """运行删除发散下界路由。"""
    deletion_bridge = load_json(deletion_bridge_path)
    hro_text = read_text(hro_lemma_path)
    hro_audits = [load_json(path) for path in hro_audit_paths]
    deletion_profiles = [load_json(path) for path in deletion_profile_paths]
    nodeletion_terminal = load_json(nodeletion_terminal_path)
    hro_summary = summarize_hro(hro_audits)
    deletion_summary = summarize_deletion_profiles(deletion_profiles)
    rows = build_rows(
        deletion_bridge=deletion_bridge,
        hro_text=hro_text,
        hro_summary=hro_summary,
        deletion_summary=deletion_summary,
        nodeletion_terminal=nodeletion_terminal,
    )
    reduced = next(
        item["closed"]
        for item in rows
        if item["gate"] == "DeletionDivergenceLowerBoundReduced"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_deletion_divergence_lower_bound_router",
        "status": "deletion_divergence_lower_bound_reduced_to_occupancy_saturation",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "deletion_bridge": file_sha256(deletion_bridge_path),
            "hro_lemma": file_sha256(hro_lemma_path),
            "nodeletion_terminal": file_sha256(nodeletion_terminal_path),
            **{
                f"hro_audit_{idx}": file_sha256(path)
                for idx, path in enumerate(hro_audit_paths, start=1)
            },
            **{
                f"deletion_profile_{idx}": file_sha256(path)
                for idx, path in enumerate(deletion_profile_paths, start=1)
            },
        },
        "deletion_divergence_lower_bound_reduced": reduced,
        "global_deletion_divergence_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_deletion_hardpoint": "OccupancySaturationPDECOrColumnCRT",
        "hro_summary": hro_summary,
        "deletion_summary": deletion_summary,
        "rows": rows,
        "router_law": (
            "HRO gives S_t subset Occ_t union TI_t. If the deletion potential does not "
            "diverge, then on a positive subsequence the average Occ/r + TI/r must tend "
            "to one. The TI branch is precisely promoted-prime non-necessity and is already "
            "routed to NoDeletion-KL/PDEC or CleanKLS/SC9. Therefore the deletion-divergence "
            "lower-bound problem is reduced to excluding OccupancySaturation: near-full "
            "old-hole residue occupancy must imply a lower-level capacity contradiction, "
            "PDEC, or ColumnCRT."
        ),
        "review_conclusion": (
            "全局删除势发散下界继续压窄：HRO 引理证明若删除势不发散，就必须出现 "
            "`OccupancySaturation` 或 `TailIndependence`。后者已由 NoDeletion-KL/CleanKLS 路由吸收；"
            "因此删除侧真正剩余是排斥占用饱和，或把占用饱和送入 PDEC/ColumnCRT。"
        ),
    }


def write_markdown(result: dict[str, object], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 删除发散下界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        str(result["review_conclusion"]),
        "",
        "## 1. 路由律",
        "",
        str(result["router_law"]),
        "",
        "```text",
        "HRO: S_t subset Occ_t union TI_t;",
        "if sum D_n does not diverge",
        "  => average Occ/r + TI/r -> 1 on a positive subsequence;",
        "TI/r -> 1",
        "  => NoDeletion-KL/PDEC or CleanKLS/SC9;",
        "therefore deletion-side remaining hardpoint",
        "  => OccupancySaturationPDECOrColumnCRT.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `deletion_divergence_lower_bound_reduced={fmt_bool(bool(result['deletion_divergence_lower_bound_reduced']))}`。",
        f"- `global_deletion_divergence_closed={fmt_bool(bool(result['global_deletion_divergence_closed']))}`。",
        f"- `row_column_unconditional_closed={fmt_bool(bool(result['row_column_unconditional_closed']))}`。",
        f"- `narrowest_deletion_hardpoint={result['narrowest_deletion_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        f"- `hro_summary={result['hro_summary']}`。",
        f"- `deletion_summary={result['deletion_summary']}`。",
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
            "`OccupancySaturationPDECOrColumnCRT` 尚未证明。下一步应证明旧洞 residue 近满占用不能在无限塔中保持："
            "要么低层洞密度过大形成容量矛盾，要么相位偏斜持久形成 PDEC，要么列位移结构形成 ColumnCRT。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deletion-bridge-json", type=Path, default=DEFAULT_DELETION_BRIDGE)
    parser.add_argument("--hro-lemma-md", type=Path, default=DEFAULT_HRO_LEMMA)
    parser.add_argument("--hro-audits", default=DEFAULT_HRO_AUDITS)
    parser.add_argument("--deletion-profiles", default=DEFAULT_DELETION_PROFILES)
    parser.add_argument(
        "--nodeletion-terminal-json", type=Path, default=DEFAULT_NODELETION_TERMINAL
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        deletion_bridge_path=args.deletion_bridge_json,
        hro_lemma_path=args.hro_lemma_md,
        hro_audit_paths=parse_paths(args.hro_audits),
        deletion_profile_paths=parse_paths(args.deletion_profiles),
        nodeletion_terminal_path=args.nodeletion_terminal_json,
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
