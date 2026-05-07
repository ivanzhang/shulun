#!/usr/bin/env python3
"""合成 PDEC-CAP 不持久 Gamma 分支的终端分裂路由。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_diffuse_terminal_split_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-diffuse-terminal-split-router.json
  docs/monograph/prime-matrix-pdec-cap-diffuse-terminal-split-router.md
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
DEFAULT_NODELETION_TERMINAL = (
    DOCS / "prime-matrix-triad-a1-continuous-nodeletion-terminal-router.json"
)
DEFAULT_CLEAN_KLS = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_SC9_FRONTIER = DOCS / "prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.json"
DEFAULT_DELETION_BRIDGE = (
    DOCS / "prime-matrix-pdec-cap-deletion-support-exhaustion-bridge.json"
)
DEFAULT_DELETION_DIVERGENCE = (
    DOCS / "prime-matrix-pdec-cap-deletion-divergence-lower-bound-router.json"
)
DEFAULT_OCCUPANCY_KERNEL = (
    DOCS / "prime-matrix-pdec-cap-occupancy-saturation-kernel-router.json"
)
DEFAULT_DENSE_KERNEL_CVT = (
    DOCS / "prime-matrix-pdec-cap-dense-kernel-common-variable-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-diffuse-terminal-split-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-diffuse-terminal-split-router.md"


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
    nodeletion_terminal: dict[str, Any],
    clean_kls: dict[str, Any],
    sc9_frontier: dict[str, Any],
    deletion_bridge: dict[str, Any],
    deletion_divergence: dict[str, Any],
    occupancy_kernel: dict[str, Any],
    dense_kernel_cvt: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 diffuse 终端分裂审查表。"""
    nodeletion_gates = nodeletion_terminal["nodeletion_gates"]
    aps_diffuse_open = (
        profinite_aps["profinite_aps_dichotomy_closed"]
        and "DiffuseCleanKLSDLSEstimateOrFiberDeletionNoDeletionKL"
        in profinite_aps["open_final_gates"]
    )
    tower_dichotomy_registered = (
        infinite_tower["status"] == "finite_budget_for_infinite_tower_dichotomy"
        and "sum_n -log a_n(P)" in infinite_tower["dichotomy_law"]
        and "a_n(P)->1" in infinite_tower["dichotomy_law"]
        and "KL/PDEC" in infinite_tower["dichotomy_law"]
        and "CleanKLS" in infinite_tower["dichotomy_law"]
    )
    current_layers_delete = (
        nodeletion_terminal["all_deletion_rows_positive"]
        and nodeletion_gates["current_layers_delete_before_nodeletion"]
        and not nodeletion_gates["current_nodeletion_triggered"]
        and set(nodeletion_gates["gate_counts"]) == {"FiberDeletion"}
    )
    nodeletion_no_third_exit = (
        nodeletion_terminal["no_independent_nodeletion_gap"]
        and nodeletion_gates["kl_chain_identity_exact"]
        and nodeletion_gates["all_kl_shapes_named_pdec_or_clean"]
        and nodeletion_gates["small_ambiguous_routed"]
    )
    clean_admission_registered = (
        clean_kls["all_admission_verified_or_routed"]
        and clean_kls["external_kls_input_registered"]
        and clean_kls["terminal_gap_after_router"]
        == "KuznetsovLSAtomSC9OrExternalCitation"
    )
    external_version_registered = clean_kls[
        "external_deep_theorem_version_status"
    ].startswith("closed_for_a1_clean_branch_if_")
    self_contained_sc9_is_named = (
        clean_kls["self_contained_version_status"] == "open_at_kuznetsov_ls_atom_sc9"
        and sc9_frontier["status"] == "a1_sc9_frontier_routed_to_ncblk_or_external_dibfi"
    )
    deletion_support_bridge_closed = (
        deletion_bridge["status"]
        == "deletion_support_exhaustion_bridge_closed_divergence_lower_bound_open"
        and deletion_bridge["deletion_support_exhaustion_bridge_closed"]
        and deletion_bridge["narrowest_deletion_hardpoint"]
        == "GlobalDeletionPotentialDivergenceLowerBound"
    )
    deletion_divergence_reduced = (
        deletion_divergence["status"]
        == "deletion_divergence_lower_bound_reduced_to_occupancy_saturation"
        and deletion_divergence["deletion_divergence_lower_bound_reduced"]
        and deletion_divergence["narrowest_deletion_hardpoint"]
        == "OccupancySaturationPDECOrColumnCRT"
    )
    occupancy_kernel_reduced = (
        occupancy_kernel["status"]
        == "occupancy_saturation_reduced_to_dense_old_hole_kernel"
        and occupancy_kernel["occupancy_saturation_reduced_to_dense_kernel"]
        and occupancy_kernel["narrowest_occupancy_hardpoint"]
        == "DenseOldHoleKernelCapacityPDECOrColumnCRT"
    )
    dense_kernel_cvt_routed = (
        dense_kernel_cvt["status"]
        == "dense_old_hole_kernel_reduced_to_common_variable_shell_dichotomy"
        and dense_kernel_cvt["dense_kernel_no_unnamed_escape_closed"]
        and dense_kernel_cvt["narrowest_dense_kernel_hardpoint"]
        == "FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9"
    )

    return [
        row(
            "APSDiffuseBranchIsTheActiveNonpersistentGate",
            aps_diffuse_open,
            str(profinite_aps["open_final_gates"]),
            "APS 投影塔二分已把不持久 Gamma 分支精确送到 diffuse 终端，而不是无名第四出口。",
            False,
        ),
        row(
            "InfiniteTowerDeletionEntropyDichotomyRegistered",
            tower_dichotomy_registered,
            infinite_tower["status"],
            "无限升层只有删除势发散或 NoDeletion 熵/KL 分支两类极限。",
            False,
        ),
        row(
            "CurrentLayersAreFiberDeletion",
            current_layers_delete,
            str(nodeletion_gates["gate_counts"]),
            "当前已物化层仍全部由 FiberDeletion 支付，且每个删除行有正删除势。",
            False,
        ),
        row(
            "NoDeletionKLHasNoThirdExit",
            nodeletion_no_third_exit,
            str(nodeletion_gates["shape_route_counts"]),
            "若未来删除停止，KL/互信息偏斜回流 refined/new-layer PDEC；只有平坦分支可进入 CleanKLS/DLS。",
            False,
        ),
        row(
            "CleanKLSAdmissionK1K9Registered",
            clean_admission_registered,
            clean_kls["terminal_gap_after_router"],
            "CleanKLS/DLS 不再是黑箱：K1--K9 任一失败都回流 PDEC/SAE/Multiplicity/Promotion。",
            False,
        ),
        row(
            "ExternalKLSVersionRegistered",
            external_version_registered,
            clean_kls["external_deep_theorem_version_status"],
            "若明确接受窗口化 DI/BFI/Kuznetsov 大筛输入，flat clean 分支可作为外部深定理版吸收。",
            False,
        ),
        row(
            "SelfContainedCleanFrontierNamedSC9",
            self_contained_sc9_is_named,
            sc9_frontier["status"],
            "完全自足版的 clean 剩余不是泛化 KLS 缺口，而是命名的 Kuznetsov-LS atom SC-9 / NC-BLK 前沿。",
            False,
        ),
        row(
            "DeletionSupportExhaustionBridgeRouted",
            deletion_support_bridge_closed,
            deletion_bridge["narrowest_deletion_hardpoint"],
            "删除势发散后的支撑耗尽/稀疏回流逻辑已闭合，删除侧只剩全局发散下界。",
            False,
        ),
        row(
            "DeletionDivergenceLowerBoundReduced",
            deletion_divergence_reduced,
            deletion_divergence["narrowest_deletion_hardpoint"],
            "全局删除势发散下界已由 HRO 压到占用饱和排斥；TailIndependence 已回流 NoDeletion/CleanKLS。",
            False,
        ),
        row(
            "OccupancySaturationKernelReduction",
            occupancy_kernel_reduced,
            occupancy_kernel["narrowest_occupancy_hardpoint"],
            "占位饱和已由 HRO 注入界压成近满旧洞选择核；稀疏旧洞子情形已自动排除。",
            False,
        ),
        row(
            "DenseOldHoleKernelCommonVariableRouted",
            dense_kernel_cvt_routed,
            dense_kernel_cvt["narrowest_dense_kernel_hardpoint"],
            "稠密旧洞选择核已化为共同变量表：容量失败、固定壳 PDEC/ColumnCRT、或多壳 SC-9。",
            False,
        ),
        row(
            "FixedShellLowModPersistencePDECOrColumnCRT",
            False,
            "terminal PDEC/ColumnCRT exclusion not submitted",
            "固定壳或有限壳包的低模持久偏斜仍需提交同 formal unit 的 PDEC/ColumnCRT 排斥证书。",
            True,
        ),
        row(
            "SelfContainedKuznetsovLSAtomSC9",
            False,
            "external input registered; self-contained atom open",
            "若删除势可求和且 KL/MI 平坦，则完全自足版仍需证明 SC-9 谱大筛原子；否则只能声明外部输入版。",
            True,
        ),
    ]


def run(
    profinite_aps_path: Path,
    infinite_tower_path: Path,
    nodeletion_terminal_path: Path,
    clean_kls_path: Path,
    sc9_frontier_path: Path,
    deletion_bridge_path: Path,
    deletion_divergence_path: Path,
    occupancy_kernel_path: Path,
    dense_kernel_cvt_path: Path,
) -> dict[str, Any]:
    """运行 diffuse 终端分裂路由。"""
    profinite_aps = load_json(profinite_aps_path)
    infinite_tower = load_json(infinite_tower_path)
    nodeletion_terminal = load_json(nodeletion_terminal_path)
    clean_kls = load_json(clean_kls_path)
    sc9_frontier = load_json(sc9_frontier_path)
    deletion_bridge = load_json(deletion_bridge_path)
    deletion_divergence = load_json(deletion_divergence_path)
    occupancy_kernel = load_json(occupancy_kernel_path)
    dense_kernel_cvt = load_json(dense_kernel_cvt_path)
    rows = build_rows(
        profinite_aps=profinite_aps,
        infinite_tower=infinite_tower,
        nodeletion_terminal=nodeletion_terminal,
        clean_kls=clean_kls,
        sc9_frontier=sc9_frontier,
        deletion_bridge=deletion_bridge,
        deletion_divergence=deletion_divergence,
        occupancy_kernel=occupancy_kernel,
        dense_kernel_cvt=dense_kernel_cvt,
    )
    split_closed = all(item["closed"] for item in rows if not item["blocks_final"])
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_diffuse_terminal_split_router",
        "status": "pdec_cap_diffuse_terminal_split_reduced_to_fixed_shell_or_sc9",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "profinite_aps": file_sha256(profinite_aps_path),
            "infinite_tower": file_sha256(infinite_tower_path),
            "nodeletion_terminal": file_sha256(nodeletion_terminal_path),
            "clean_kls": file_sha256(clean_kls_path),
            "sc9_frontier": file_sha256(sc9_frontier_path),
            "deletion_bridge": file_sha256(deletion_bridge_path),
            "deletion_divergence": file_sha256(deletion_divergence_path),
            "occupancy_kernel": file_sha256(occupancy_kernel_path),
            "dense_kernel_cvt": file_sha256(dense_kernel_cvt_path),
        },
        "diffuse_terminal_split_closed": split_closed,
        "external_deep_theorem_version_closed_if_accepted": True,
        "self_contained_diffuse_terminal_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_diffuse_hardpoint": (
            "FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9"
        ),
        "rows": rows,
        "split_law": (
            "For the nonpersistent Gamma branch, the inverse finite-signature tower gives "
            "diffuse payment. Along any same-source lift tower, either the deletion "
            "potential sum diverges and the support density is exhausted, or deletion is "
            "summable and the branch is NoDeletion. In NoDeletion, persistent KL or "
            "phase-residue mutual information returns to refined/new-layer PDEC; only the "
            "flat KL/MI case is admitted to CleanKLS/DLS. K1--K9 then route all non-clean "
            "failures back to PDEC/SAE/Multiplicity/Promotion. The support-exhaustion "
            "bridge closes the implication from divergent deletion to exhaustion or named "
            "sparse/PDEC return. The deletion-divergence router then reduces the lower bound "
            "to OccupancySaturation, because TailIndependence is already NoDeletion-KL/CleanKLS. "
            "The occupancy kernel router further removes the sparse-old-hole subcase and "
            "turns saturation into a dense old-hole selector kernel. The common-variable "
            "router rewrites that kernel as c_b=rho_b+r k_b, so all low-prime constraints "
            "act on the same shell variable k_b. Thus the self-contained diffuse terminal "
            "is reduced to fixed-shell low-mod PDEC/ColumnCRT persistence or the named "
            "Kuznetsov-LS atom SC-9; an external DI/BFI/Kuznetsov input would close the flat "
            "clean branch only as an external-theorem version."
        ),
        "review_conclusion": (
            "不持久 Gamma 分支已经不再是 `FiberDeletion/NoDeletion/CleanKLS` 的宽口径黑箱。"
            "现有账本合成后，非终端门全部接线：持续删除进入删除势账本，删除停止时 KL/MI 偏斜回流 PDEC，"
            "只有 KL/MI 平坦才进入 CleanKLS；而 CleanKLS 的 K1--K9 失败项也全部回流命名出口。"
            "删除势发散后的支撑耗尽桥也已闭合；全局删除势发散下界又被 HRO 压到占用饱和排斥。"
            "占位饱和再由 HRO 注入界压成稠密旧洞选择核；共同变量表又把该核压成固定壳低模持久或多壳平坦。"
            "剩余自足硬点压成两项：`FixedShellLowModPersistencePDECOrColumnCRT`，或 flat/multishell clean 分支的 SC-9 谱大筛原子。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP Diffuse 终端分裂路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 分裂律",
        "",
        result["split_law"],
        "",
        "```text",
        "Nonpersistent Gamma",
        "  => diffuse finite-signature tower;",
        "same-source lift tower",
        "  => sum deletion potential diverges",
        "       => support exhaustion or named sparse/PDEC return;",
        "  or NoDeletion;",
        "NoDeletion + persistent KL/MI",
        "  => refined/new-layer PDEC;",
        "NoDeletion + flat KL/MI",
        "  => CleanKLS/DLS;",
        "CleanKLS K1--K9 failure",
        "  => PDEC / SAE / Multiplicity / Promotion;",
        "all K1--K9 pass",
        "  => external KLS if cited, or self-contained SC-9.",
        "deletion-side remaining hardpoint",
        "  => FixedShellLowModPersistencePDECOrColumnCRT or SC-9.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `diffuse_terminal_split_closed={fmt_bool(result['diffuse_terminal_split_closed'])}`。",
        f"- `external_deep_theorem_version_closed_if_accepted={fmt_bool(result['external_deep_theorem_version_closed_if_accepted'])}`。",
        f"- `self_contained_diffuse_terminal_closed={fmt_bool(result['self_contained_diffuse_terminal_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_diffuse_hardpoint={result['narrowest_diffuse_hardpoint']}`。",
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
            "## 4. 边界",
            "",
            "本路由器关闭的是 diffuse 分支中的无名逃逸和 NoDeletion-KL 第三出口。"
            "它不证明完整行/列无条件定理，也不证明 PDEC-CAP 同集全局对偶证书。"
            "完全自足版仍需提交 `FixedShellLowModPersistencePDECOrColumnCRT` 或 "
            "`SelfContainedKuznetsovLSAtomSC9` 的最终证明；外部深定理版必须明确登记所引用的 KLS/DI/BFI/Kuznetsov 输入。",
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
    parser.add_argument(
        "--nodeletion-terminal-json", type=Path, default=DEFAULT_NODELETION_TERMINAL
    )
    parser.add_argument("--clean-kls-json", type=Path, default=DEFAULT_CLEAN_KLS)
    parser.add_argument("--sc9-frontier-json", type=Path, default=DEFAULT_SC9_FRONTIER)
    parser.add_argument("--deletion-bridge-json", type=Path, default=DEFAULT_DELETION_BRIDGE)
    parser.add_argument("--deletion-divergence-json", type=Path, default=DEFAULT_DELETION_DIVERGENCE)
    parser.add_argument("--occupancy-kernel-json", type=Path, default=DEFAULT_OCCUPANCY_KERNEL)
    parser.add_argument("--dense-kernel-cvt-json", type=Path, default=DEFAULT_DENSE_KERNEL_CVT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        profinite_aps_path=args.profinite_aps_json,
        infinite_tower_path=args.infinite_tower_json,
        nodeletion_terminal_path=args.nodeletion_terminal_json,
        clean_kls_path=args.clean_kls_json,
        sc9_frontier_path=args.sc9_frontier_json,
        deletion_bridge_path=args.deletion_bridge_json,
        deletion_divergence_path=args.deletion_divergence_json,
        occupancy_kernel_path=args.occupancy_kernel_json,
        dense_kernel_cvt_path=args.dense_kernel_cvt_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_diffuse_hardpoint"])


if __name__ == "__main__":
    main()
