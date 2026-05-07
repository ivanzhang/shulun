#!/usr/bin/env python3
"""审查 PDEC-CAP 同集全局对偶证书的当前最窄前沿。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_same_set_global_dual_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-same-set-global-dual-router.json
  docs/monograph/prime-matrix-pdec-cap-same-set-global-dual-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SELF_BOTTLENECK = (
    DOCS / "prime-matrix-self-contained-terminal-bottleneck-router.json"
)
DEFAULT_PDEC_ROUTE = DOCS / "prime-matrix-triad-a1-pdec-capacity-upper-route.md"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MASS_SOURCE = DOCS / "prime-matrix-triad-a1-pdec-mass-source-router.json"
DEFAULT_PERSISTENT = DOCS / "prime-matrix-triad-a1-persistentcap-terminal-router.json"
DEFAULT_FORCED = DOCS / "prime-matrix-triad-a1-forcedcap-terminal-router.json"
DEFAULT_APS = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-router.json"
DEFAULT_TOWER = DOCS / "prime-matrix-triad-a1-newlayer-tower-gate.json"
DEFAULT_NO_CYCLE = DOCS / "prime-matrix-pdec-cap-refinement-no-cycle.md"
DEFAULT_PROJECTION = (
    DOCS / "prime-matrix-triad-a1-newlayer-projection-monotonicity-lemma.md"
)
DEFAULT_APS_CONTRACT = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-contract.md"
DEFAULT_PROFINITE_APS = DOCS / "prime-matrix-profinite-actual-payment-stitching-router.json"
DEFAULT_DIFFUSE_TERMINAL = (
    DOCS / "prime-matrix-pdec-cap-diffuse-terminal-split-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-same-set-global-dual-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-same-set-global-dual-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


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
    """构造审查表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    self_bottleneck: dict[str, Any],
    pdec_route_text: str,
    dualcap: dict[str, Any],
    mass_source: dict[str, Any],
    persistent: dict[str, Any],
    forced: dict[str, Any],
    aps: dict[str, Any],
    tower: dict[str, Any],
    no_cycle_text: str,
    projection_text: str,
    aps_contract_text: str,
    profinite_aps: dict[str, Any],
    diffuse_terminal: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 PDEC-CAP 前沿审查表。"""
    self_bottleneck_accepts_pdec = (
        self_bottleneck["self_contained_terminal_bottleneck_is_pdec_cap"]
        and self_bottleneck["narrowest_self_contained_hardpoint"]
        == "PDEC_CAP_SameSetGlobalDualCertificate"
    )
    pdec_same_set_protocol_registered = has_all(
        pdec_route_text,
        [
            "Triad-A1：PDEC 同一坏窗容量上界路线",
            "U_CRT<L_PDEC",
            "Same-Set Law",
        ],
    )
    dualcap_materialized = (
        dualcap["status"] == "pdec_dualcap_candidates_materialized"
        and dualcap["aggregate_class_counts"].get("SparseCap") == 16
        and dualcap["aggregate_class_counts"].get("PersistentCap") == 68
        and dualcap["aggregate_class_counts"].get("ForcedPersistentByDensityBarrier")
        == 24
    )
    mass_and_early_exit_closed = (
        mass_source["all_current_dualcap_mass_sources_verified"]
        and mass_source["all_current_dualcap_pxp_exits_closed"]
    )
    persistent_current_routed = (
        persistent["all_counts_match"]
        and persistent["all_current_persistent_caps_routed"]
        and persistent["gates"]["promotion_deletion_potential_positive"]
    )
    forced_current_routed = (
        forced["all_counts_match"]
        and forced["all_current_forced_caps_routed"]
        and forced["gates"]["single_residue_actual_payment_excluded"]
        and forced["gates"]["single_column_residue_actual_payment_excluded"]
    )
    aps_current_routed = (
        aps["all_counts_match"]
        and aps["all_current_forced_multibucket_rows_routed_to_aps"]
        and aps["gates"]["forced_signature_or_small_ambiguous_gate_active"]
        and aps["gates"]["small_ambiguous_successor_routed_before_clean_terminal"]
    )
    lhb_projection_stitching_removed = (
        tower["all_layers_monotone"]
        and has_all(
            projection_text,
            [
                "projection_monotonicity_proved_for_lhb_M_support",
                "N=empty",
                "\\pi(A_{Q'})\\subseteq A_Q",
            ],
        )
    )
    no_cycle_registered = has_all(
        no_cycle_text,
        [
            "pdec_cap_refinement_no_cycle_reduction_not_exit_exclusion",
            "固定 G 内 refined PDEC 不能无限循环",
            "New-layer 塔熵合同",
        ],
    )
    finite_tower_evidence_registered = (
        tower["all_layers_have_valid_accounting"]
        and tower["all_layers_resparse"]
        and tower["status"] == "newlayer_tower_gate_materialized_not_global_proof"
    )
    aps_contract_open = has_all(
        aps_contract_text,
        [
            "actual_payment_stitching_contract_open",
            "PersistentStitching",
            "NoPersistentStitching",
            "APS-1",
        ],
    )
    profinite_aps_dichotomy_closed = (
        profinite_aps["status"]
        == "profinite_actual_payment_stitching_dichotomy_closed_terminal_estimates_open"
        and profinite_aps["profinite_aps_dichotomy_closed"]
    )
    diffuse_terminal_split_closed = (
        diffuse_terminal["status"]
        == "pdec_cap_diffuse_terminal_split_reduced_to_fixed_shell_or_sc9"
        and diffuse_terminal["diffuse_terminal_split_closed"]
        and diffuse_terminal["narrowest_diffuse_hardpoint"]
        == "FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9"
    )

    return [
        row(
            "SelfContainedBottleneckAccepted",
            self_bottleneck_accepts_pdec,
            self_bottleneck["narrowest_self_contained_hardpoint"],
            "上一轮已把完全自足路线压到 PDEC-CAP 同集全局对偶证书。",
            False,
        ),
        row(
            "SameSetPDECProtocolRegistered",
            pdec_same_set_protocol_registered,
            "Same-Set Law and U_CRT<L_PDEC protocol",
            "PDEC 比较必须作用于同一坏窗推前计数，失败必须输出 DualCap 或缺失行。",
            False,
        ),
        row(
            "DualCapFailureMaterialized",
            dualcap_materialized,
            str(dualcap["aggregate_class_counts"]),
            "固定 Q 的 PDEC 对偶失败已分解为 Sparse、Persistent、Forced 三类 DualCap。",
            False,
        ),
        row(
            "SameMassAndEarlyExitClosedForCurrentDualCaps",
            mass_and_early_exit_closed,
            "mass verified; P×P exits closed",
            "当前 DualCap 都有同一 M_Q 质量来源，早期 P×P 出口由 Sparse/BTLS/LFTE 接线关闭。",
            False,
        ),
        row(
            "PersistentCapsCurrentLayerRouted",
            persistent_current_routed,
            str(persistent["current_layer_metrics"]["promotion_class_counts"]),
            "当前 68 个 PersistentCap 已进入晋升删除势、NoDeletion-KL/CleanKLS 或固定签名 PDEC 路线。",
            False,
        ),
        row(
            "ForcedCapsCurrentLayerRouted",
            forced_current_routed,
            str(forced["current_layer_metrics"]["dominance_route_counts"]),
            "当前 24 个 ForcedCap 已退出固定 Q 循环，单桶实际支付被排除，剩余进入多桶 PDEC/APS。",
            False,
        ),
        row(
            "ActualPaymentStitchingCurrentRowsRouted",
            aps_current_routed,
            aps["route"],
            "当前 48 个多桶矩阵行已路由到 APS：持久 Gamma 进 MFU/PDEC，不持久进分散 CleanKLS/DLS。",
            False,
        ),
        row(
            "LHBProjectionStitchingRemoved",
            lhb_projection_stitching_removed,
            "pi(A_Q') subset A_Q for same C_P support",
            "同一 LHB 全周期完成集合口径下，升层坏项 N 为空，ProjectionStitching 不再是当前分支出口。",
            False,
        ),
        row(
            "PDECCapNoCycleRegistered",
            no_cycle_registered,
            "finite Boolean algebra refinement; new-layer entropy contract",
            "固定有限签名群内 PDEC cap 细化不能无限循环；升层必须进入 new-layer PDEC 或 CleanKLS。",
            False,
        ),
        row(
            "FiniteTowerEvidenceRegistered",
            finite_tower_evidence_registered,
            str(tower["layer_classes"]),
            "已物化两层均为 FiberDeletionLayer，但这仍只是有限塔证据，不是全局证明。",
            False,
        ),
        row(
            "ProfiniteActualPaymentStitchingDichotomy",
            profinite_aps_dichotomy_closed,
            "finite projection compactness / pigeonhole dichotomy",
            "真实支付图 Gamma 的 PersistentStitching / NoPersistentStitching 二分逻辑已闭合到两侧终端估计。",
            False,
        ),
        row(
            "SameSetPDECDualComparisonForPersistentMFU",
            False,
            "U_CRT^multi<L_PDEC^multi not submitted for all persistent MFU",
            "若 Gamma 持久缝合成多桶 formal unit，仍需提交同集多桶 PDEC 对偶容量证书。",
            True,
        ),
        row(
            "DiffuseTerminalSplitRouted",
            diffuse_terminal_split_closed,
            diffuse_terminal["narrowest_diffuse_hardpoint"],
            "不持久 Gamma 分支已合成为删除势/NoDeletion-KL/CleanKLS 的终端分裂，无名 diffuse 出口关闭。",
            False,
        ),
        row(
            "DiffuseFixedShellPDECColumnCRTOrSelfContainedSC9",
            False,
            str(diffuse_terminal["open_final_gates"]),
            "不持久 Gamma 分支剩余自足义务：固定壳低模持久偏斜的 PDEC/ColumnCRT 排斥，或 KL/多壳平坦 clean 残余的 SC-9 谱大筛原子。",
            True,
        ),
        row(
            "ActualPaymentStitchingContractSupersededByProfiniteDichotomy",
            aps_contract_open and profinite_aps_dichotomy_closed,
            "contract open text superseded by profinite APS router",
            "原 APS 合同中的二分缺口已由投影塔二分路由器闭合；它不再是独立终端阻塞。",
            False,
        ),
    ]


def run(
    self_bottleneck_path: Path,
    pdec_route_path: Path,
    dualcap_path: Path,
    mass_source_path: Path,
    persistent_path: Path,
    forced_path: Path,
    aps_path: Path,
    tower_path: Path,
    no_cycle_path: Path,
    projection_path: Path,
    aps_contract_path: Path,
    profinite_aps_path: Path,
    diffuse_terminal_path: Path,
) -> dict[str, Any]:
    """运行 PDEC-CAP 前沿审查。"""
    self_bottleneck = load_json(self_bottleneck_path)
    pdec_route_text = read_text(pdec_route_path)
    dualcap = load_json(dualcap_path)
    mass_source = load_json(mass_source_path)
    persistent = load_json(persistent_path)
    forced = load_json(forced_path)
    aps = load_json(aps_path)
    tower = load_json(tower_path)
    no_cycle_text = read_text(no_cycle_path)
    projection_text = read_text(projection_path)
    aps_contract_text = read_text(aps_contract_path)
    profinite_aps = load_json(profinite_aps_path)
    diffuse_terminal = load_json(diffuse_terminal_path)

    rows = build_rows(
        self_bottleneck=self_bottleneck,
        pdec_route_text=pdec_route_text,
        dualcap=dualcap,
        mass_source=mass_source,
        persistent=persistent,
        forced=forced,
        aps=aps,
        tower=tower,
        no_cycle_text=no_cycle_text,
        projection_text=projection_text,
        aps_contract_text=aps_contract_text,
        profinite_aps=profinite_aps,
        diffuse_terminal=diffuse_terminal,
    )
    closed_current_materialized = all(
        item["closed"] for item in rows if not item["blocks_final"]
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_same_set_global_dual_router",
        "status": "pdec_cap_same_set_global_dual_frontier_reduced_to_terminal_estimates_not_closed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "self_bottleneck": file_sha256(self_bottleneck_path),
            "pdec_route": file_sha256(pdec_route_path),
            "dualcap": file_sha256(dualcap_path),
            "mass_source": file_sha256(mass_source_path),
            "persistent": file_sha256(persistent_path),
            "forced": file_sha256(forced_path),
            "actual_payment_stitching": file_sha256(aps_path),
            "tower": file_sha256(tower_path),
            "no_cycle": file_sha256(no_cycle_path),
            "projection": file_sha256(projection_path),
            "aps_contract": file_sha256(aps_contract_path),
            "profinite_aps": file_sha256(profinite_aps_path),
            "diffuse_terminal": file_sha256(diffuse_terminal_path),
        },
        "closed_current_materialized_pdec_gates": closed_current_materialized,
        "pdec_cap_same_set_global_dual_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": (
            "SameSetPDECDualComparisonForPersistentMFU_OR_FixedShellPDECColumnCRTOrSC9"
        ),
        "rows": rows,
        "frontier_law": (
            "The current same-set PDEC-CAP obligation is no longer an unnamed Fourier "
            "constant search. Materialized DualCaps have same-M_Q mass sources and closed "
            "early P-row exits; current PersistentCaps route to promotion deletion or "
            "NoDeletion-KL/CleanKLS/PDEC; current ForcedCaps route to multi-bucket actual "
            "payment stitching. The profinite ActualPaymentStitching dichotomy for the real "
            "payment graph Gamma is now closed as a routing law. Persistent Gamma gives a "
            "multi-bucket same-set PDEC dual comparison; nonpersistent Gamma must enter "
            "FiberDeletion/NoDeletion-KL/CleanKLS. The diffuse terminal split is now routed "
            "further to fixed-shell low-mod PDEC/ColumnCRT persistence or the self-contained "
            "Kuznetsov-LS atom SC-9. The remaining global final gates are "
            "the persistent same-set PDEC dual comparison and the narrowed diffuse terminal "
            "estimates, not an unnamed APS exit."
        ),
        "review_conclusion": (
            "PDEC-CAP 的当前已物化中间门全部可路由，APS 投影塔二分也已闭合；"
            "diffuse 分支又被压到固定壳低模 PDEC/ColumnCRT 持久偏斜或自足 SC-9。"
            "但全局同集对偶证书仍未闭合。最新最窄剩余是：持久 `Gamma` 的多桶同集 "
            "PDEC 对偶比较 `U_CRT^multi<L_PDEC^multi`，以及不持久 `Gamma` 的 "
            "`FixedShellLowModPersistencePDECOrColumnCRT` 或 `SelfContainedKuznetsovLSAtomSC9`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 同集全局对偶前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 前沿律",
        "",
        result["frontier_law"],
        "",
        "```text",
        "PDEC_CAP_SameSetGlobalDualCertificate",
        "  -> current DualCap families routed;",
        "  -> current PersistentCap routed by promotion deletion / NoDeletion-KL;",
        "  -> current ForcedCap routed to multi-bucket ActualPaymentStitching;",
        "  -> APS profinite dichotomy routed;",
        "  -> remaining terminal estimates:",
        "       persistent MFU PDEC or diffuse FixedShellPDECColumnCRT / SC-9.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `closed_current_materialized_pdec_gates={fmt_bool(result['closed_current_materialized_pdec_gates'])}`。",
        f"- `pdec_cap_same_set_global_dual_closed={fmt_bool(result['pdec_cap_same_set_global_dual_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
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
            "## 4. 下一步",
            "",
            "下一步直接攻两侧终端估计：持久 `Gamma` 分支的多桶同集 PDEC 对偶容量证书 "
            "`U_CRT^multi<L_PDEC^multi`；以及无持久 `Gamma` 分支中的固定壳低模持久 PDEC/ColumnCRT "
            "或自足 `SelfContainedKuznetsovLSAtomSC9`。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-bottleneck-json", type=Path, default=DEFAULT_SELF_BOTTLENECK)
    parser.add_argument("--pdec-route-md", type=Path, default=DEFAULT_PDEC_ROUTE)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--mass-source-json", type=Path, default=DEFAULT_MASS_SOURCE)
    parser.add_argument("--persistent-json", type=Path, default=DEFAULT_PERSISTENT)
    parser.add_argument("--forced-json", type=Path, default=DEFAULT_FORCED)
    parser.add_argument("--aps-json", type=Path, default=DEFAULT_APS)
    parser.add_argument("--tower-json", type=Path, default=DEFAULT_TOWER)
    parser.add_argument("--no-cycle-md", type=Path, default=DEFAULT_NO_CYCLE)
    parser.add_argument("--projection-md", type=Path, default=DEFAULT_PROJECTION)
    parser.add_argument("--aps-contract-md", type=Path, default=DEFAULT_APS_CONTRACT)
    parser.add_argument("--profinite-aps-json", type=Path, default=DEFAULT_PROFINITE_APS)
    parser.add_argument("--diffuse-terminal-json", type=Path, default=DEFAULT_DIFFUSE_TERMINAL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        self_bottleneck_path=args.self_bottleneck_json,
        pdec_route_path=args.pdec_route_md,
        dualcap_path=args.dualcap_json,
        mass_source_path=args.mass_source_json,
        persistent_path=args.persistent_json,
        forced_path=args.forced_json,
        aps_path=args.aps_json,
        tower_path=args.tower_json,
        no_cycle_path=args.no_cycle_md,
        projection_path=args.projection_md,
        aps_contract_path=args.aps_contract_md,
        profinite_aps_path=args.profinite_aps_json,
        diffuse_terminal_path=args.diffuse_terminal_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_next_hardpoint"])


if __name__ == "__main__":
    main()
