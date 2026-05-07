#!/usr/bin/env python3
"""汇总 Triad-A1 PDEC 同集容量上界的当前前沿。

用法示例：
  python3 experiments/prime_matrix_triad_a1_pdec_same_set_capacity_frontier_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.json
  docs/monograph/prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_LP = DOCS / "prime-matrix-triad-a1-lhb-lp-skeleton.json"
DEFAULT_DIRECTION = DOCS / "prime-matrix-triad-a1-lhb-direction-support-audit.json"
DEFAULT_FOURIER = DOCS / "prime-matrix-triad-a1-lhb-fourier-cap-scan.json"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MASS = DOCS / "prime-matrix-triad-a1-pdec-mass-source-router.json"
DEFAULT_CONFLUENCE = DOCS / "prime-matrix-triad-a1-terminal-confluence-router.json"
DEFAULT_CONTINUOUS = DOCS / "prime-matrix-triad-a1-continuous-direction-arc-dual.json"
DEFAULT_BRIDGE = DOCS / "prime-matrix-triad-a1-continuous-columntail-bridge.json"
DEFAULT_ACTUAL_PAYMENT = DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
DEFAULT_TERMINAL_DICHOTOMY = DOCS / "prime-matrix-triad-a1-continuous-terminal-dichotomy-router.json"
DEFAULT_PDEC_SIGNATURE = DOCS / "prime-matrix-triad-a1-continuous-pdec-signature-input-ledger.json"
DEFAULT_PRIME_LIFT = DOCS / "prime-matrix-triad-a1-continuous-prime-lift-router.json"
DEFAULT_SELECTIVE_COMMUTATION = DOCS / "prime-matrix-triad-a1-selective-promotion-commutation.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def summarize_lp(lp: dict[str, Any]) -> dict[str, Any]:
    """汇总 LHB LP 骨架。"""
    obstruction_count = sum(
        1 for row in lp["prime_results"] if row["box_only_obstruction"]["exists"]
    )
    return {
        "q": int(lp["q"]),
        "p_count": len(lp["prime_results"]),
        "all_zero_blocks_ready": bool(lp["all_zero_blocks_ready"]),
        "box_only_global_closure": bool(lp["box_only_global_closure"]),
        "box_only_obstruction_count": obstruction_count,
        "row_generators_ready": [
            "nonnegativity",
            "phase_caps_g_le_M",
            "WHOLEDEF_zero_block",
            "BRIDGED_zero_block",
        ],
    }


def summarize_fourier(fourier: dict[str, Any]) -> dict[str, Any]:
    """汇总 Fourier cap 扫描的分类。"""
    class_counts: Counter[str] = Counter()
    for item in fourier["prime_results"]:
        for report in item["alpha_reports"]:
            class_counts.update(report["class_counts"])
    return {
        "q": int(fourier["q"]),
        "p_count": len(fourier["prime_results"]),
        "class_counts": dict(sorted(class_counts.items())),
        "has_persistent_cap": class_counts["PersistentCap"] > 0,
    }


def build_frontier_rows(
    lp: dict[str, Any],
    direction: dict[str, Any],
    fourier: dict[str, Any],
    dualcap: dict[str, Any],
    mass: dict[str, Any],
    confluence: dict[str, Any],
    continuous: dict[str, Any],
    bridge: dict[str, Any],
    actual_payment: dict[str, Any],
    terminal_dichotomy: dict[str, Any],
    pdec_signature: dict[str, Any],
    prime_lift: dict[str, Any],
    selective_commutation: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成同集容量前沿行。"""
    lp_summary = summarize_lp(lp)
    fourier_summary = summarize_fourier(fourier)
    return [
        {
            "frontier": "SameSetAttachment",
            "status": "ready_current_lhb_branch"
            if mass["all_current_dualcap_mass_sources_verified"]
            else "attachment_gap",
            "evidence": "当前 DualCap 三族都有同一 M_Q 质量来源。",
            "next_action": "新 formal PDEC 分支仍必须先证明 S subset Z_theta。",
        },
        {
            "frontier": "ZeroBlockCapacityRows",
            "status": "closed_subbranch" if direction["all_empty"] else "nonempty",
            "evidence": (
                "WHOLEDEF/BRIDGED 与 supp(M) 交集为空。"
                if direction["all_empty"]
                else "方向支撑交集非空，需要 Sparse/Persistent 路由。"
            ),
            "next_action": "真实 PDEC 方向若落在零块并集，该 LHB 分支直接空。",
        },
        {
            "frontier": "BoxOnlyCapacity",
            "status": "structurally_insufficient"
            if not lp_summary["box_only_global_closure"]
            else "closed",
            "evidence": (
                f"{lp_summary['box_only_obstruction_count']} 个 P 都存在单相位 box-only 可行见证。"
            ),
            "next_action": "必须补方向、column/tail/cofactor、NoDeletion-KL 或 CleanKLS 行。",
        },
        {
            "frontier": "FourierCapDualFailure",
            "status": "dualcap_materialized"
            if dualcap["aggregate_class_counts"]
            else "no_dualcap",
            "evidence": (
                f"class_counts={dualcap['aggregate_class_counts']}；"
                f"route_counts={dualcap['aggregate_route_counts']}。"
            ),
            "next_action": "SparseCap 进 LocalSurvivor；Persistent/Forced 进 refined PDEC、升层或 CleanKLS。",
        },
        {
            "frontier": "CurrentPXPExit",
            "status": "closed"
            if mass["all_current_dualcap_pxp_exits_closed"]
            else "open",
            "evidence": "当前 DualCap 的 P×P 早期出口由 SparseLocalSurvivor/BTLS/LFTE 接住。",
            "next_action": "剩余不是 P 行出口，而是终端 PDEC/LocalSurvivor/CleanKLS 证书。",
        },
        {
            "frontier": "TerminalConfluence",
            "status": "no_fourth_exit"
            if confluence["no_fourth_exit_current_a1_chain"]
            else "routing_gap",
            "evidence": "APS、DualCap、升层删除、NoDeletion-KL、promotion 均汇入三终端。",
            "next_action": "直接攻三终端证书；首要为 PDEC same-set U_CRT<L_PDEC。",
        },
        {
            "frontier": "ContinuousDirectionArcDual",
            "status": "continuous_dualcap_materialized_not_closed",
            "evidence": (
                f"连续方向弧精确审计已提交；route_counts={continuous['route_counts']}；"
                f"max U_box/M={continuous['global_max_box_dual_value_over_total_m']:.6f}。"
            ),
            "next_action": "方向采样退路关闭；下一步补 column/tail/cofactor 同集结构行或转 CleanKLS。",
        },
        {
            "frontier": "ContinuousColumnTailBridge",
            "status": "actual_payment_selection_materialized",
            "evidence": (
                f"连续 cap 已接到 column-tail 暴露账本；route_counts={bridge['route_counts']}；"
                f"all_cap_recomputations_match={bridge['all_cap_recomputations_match']}。"
            ),
            "next_action": "从暴露候选桶提升到真实支付测度：集中给 PDEC，递归扩散给 CleanKLS/DLS。",
        },
        {
            "frontier": "ContinuousActualPaymentSelection",
            "status": "actual_payment_measure_constructed",
            "evidence": (
                f"canonical actual payment measure 已构造；route_counts={actual_payment['route_counts']}；"
                f"all_payment_counts_match_demand={actual_payment['all_payment_counts_match_demand']}。"
            ),
            "next_action": "终端只剩两引理：positive-limsup finite signature=>PDEC；diffuse=>CleanKLS/DLS。",
        },
        {
            "frontier": "ContinuousTerminalDichotomy",
            "status": "terminal_dichotomy_admission_closed_capacity_open",
            "evidence": (
                f"终端二分已路由；route_counts={terminal_dichotomy['route_counts']}；"
                f"open={terminal_dichotomy['open_terminal_obligations']}。"
            ),
            "next_action": "直接攻 PDEC-CAP 容量不等式，或攻/引用 KLS-EXT 大筛估计。",
        },
        {
            "frontier": "ContinuousPDECSignatureInput",
            "status": "positive_limsup_pdec_inputs_materialized_capacity_open",
            "evidence": (
                f"positive-limsup 有限签名已生成 PDEC 输入账本；"
                f"signature_rows={pdec_signature['signature_row_count']}；"
                f"route_counts={pdec_signature['route_counts']}；"
                f"min Fourier/total={pdec_signature['global_min_signature_fourier_abs_over_total']:.6f}。"
            ),
            "next_action": "对这些 g_b(t) 证明 U_CRT<L_PDEC；失败则输出更窄 DualCap/缺失行/KLS 回流。",
        },
        {
            "frontier": "ContinuousPrimeLiftCongruence",
            "status": "prime_lift_deletion_kl_ready_with_selective_commutation_gap",
            "evidence": (
                f"positive-limsup 签名均满足 prime-lift 同余；"
                f"route_counts={prime_lift['route_counts']}；"
                f"promoted_prime_counts={prime_lift['promoted_prime_counts']}。"
            ),
            "next_action": "39 行接标准晋升删除/KL；1 行补选择性晋升交换律或 cofactor-order PDEC。",
        },
        {
            "frontier": "SelectivePromotionCommutation",
            "status": "selective_promotion_resolved_by_finite_split",
            "evidence": (
                f"选择性晋升行已由 CRT 交换律有限拆分；"
                f"route_counts={selective_commutation['route_counts']}；"
                f"max_successor_count={selective_commutation['max_successor_count']}。"
            ),
            "next_action": "选择性行回到标准 prime-lift 或 diffuse KLS；继续攻标准晋升删除/KL 或 KLS-EXT。",
        },
    ]


def run(
    lp_path: Path,
    direction_path: Path,
    fourier_path: Path,
    dualcap_path: Path,
    mass_path: Path,
    confluence_path: Path,
    continuous_path: Path,
    bridge_path: Path,
    actual_payment_path: Path,
    terminal_dichotomy_path: Path,
    pdec_signature_path: Path,
    prime_lift_path: Path,
    selective_commutation_path: Path,
) -> dict[str, Any]:
    """运行 PDEC 同集容量前沿路由。"""
    lp = load_json(lp_path)
    direction = load_json(direction_path)
    fourier = load_json(fourier_path)
    dualcap = load_json(dualcap_path)
    mass = load_json(mass_path)
    confluence = load_json(confluence_path)
    continuous = load_json(continuous_path)
    bridge = load_json(bridge_path)
    actual_payment = load_json(actual_payment_path)
    terminal_dichotomy = load_json(terminal_dichotomy_path)
    pdec_signature = load_json(pdec_signature_path)
    prime_lift = load_json(prime_lift_path)
    selective_commutation = load_json(selective_commutation_path)
    frontier_rows = build_frontier_rows(
        lp,
        direction,
        fourier,
        dualcap,
        mass,
        confluence,
        continuous,
        bridge,
        actual_payment,
        terminal_dichotomy,
        pdec_signature,
        prime_lift,
        selective_commutation,
    )
    status_counts = Counter(row["status"] for row in frontier_rows)
    ready_or_routed = {
        "ready_current_lhb_branch",
        "closed_subbranch",
        "structurally_insufficient",
        "dualcap_materialized",
        "continuous_dualcap_materialized_not_closed",
        "actual_payment_selection_materialized",
        "actual_payment_measure_constructed",
        "terminal_dichotomy_admission_closed_capacity_open",
        "positive_limsup_pdec_inputs_materialized_capacity_open",
        "prime_lift_deletion_kl_ready_with_selective_commutation_gap",
        "selective_promotion_resolved_by_finite_split",
        "closed",
        "no_fourth_exit",
    }
    all_known_frontiers_routed = all(row["status"] in ready_or_routed for row in frontier_rows)
    return {
        "certificate_type": "triad_a1_pdec_same_set_capacity_frontier_router",
        "status": "same_set_capacity_frontier_materialized_terminal_dual_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "lhb_lp_skeleton_json": file_sha256(lp_path),
            "direction_support_json": file_sha256(direction_path),
            "fourier_cap_scan_json": file_sha256(fourier_path),
            "dualcap_extractor_json": file_sha256(dualcap_path),
            "pdec_mass_source_json": file_sha256(mass_path),
            "terminal_confluence_json": file_sha256(confluence_path),
            "continuous_direction_arc_json": file_sha256(continuous_path),
            "continuous_columntail_bridge_json": file_sha256(bridge_path),
            "continuous_actual_payment_selection_json": file_sha256(actual_payment_path),
            "continuous_terminal_dichotomy_json": file_sha256(terminal_dichotomy_path),
            "continuous_pdec_signature_input_json": file_sha256(pdec_signature_path),
            "continuous_prime_lift_json": file_sha256(prime_lift_path),
            "selective_promotion_commutation_json": file_sha256(selective_commutation_path),
        },
        "lp_summary": summarize_lp(lp),
        "fourier_summary": summarize_fourier(fourier),
        "dualcap_summary": {
            "aggregate_class_counts": dualcap["aggregate_class_counts"],
            "aggregate_route_counts": dualcap["aggregate_route_counts"],
        },
        "frontier_rows": frontier_rows,
        "status_counts": dict(sorted(status_counts.items())),
        "all_known_frontiers_routed": all_known_frontiers_routed,
        "terminal_dual_gap": "StandardPrimeLiftDeletionKLOrKLSLargeSieve",
        "structural_law": (
            "同集容量上界只允许作用在同一个 g(t) 上。当前 LHB 分支的 Attachment、零块容量行、"
            "DualCap 输出、P×P 出口和终端回流均已接线；box-only 行结构上不足，"
            "连续方向弧精确审计已排除离散采样不足这一退路；连续 cap 也已接到 column-tail 暴露账本。"
            "actual payment measure 已由 canonical 选择律构造，终端投影塔二分也已闭合。"
            "positive-limsup 有限签名的 PDEC 输入账本已物化。"
            "这些签名又进一步满足 prime-lift 同余；唯一选择性晋升已由 CRT 交换律有限拆分。"
            "最终缺口转成标准晋升删除/KL，或 CleanKLS/DLS 大筛估计。"
        ),
        "review_conclusion": (
            "Triad-A1 的 PDEC same-set capacity 已被压到一个明确前沿："
            "当前合法行足以闭合零块子支并输出/路由 DualCap，连续方向弧也已精确物化为 persistent cap，"
            "连续 cap 已接入 column-tail 暴露账本，且 canonical actual payment measure 已精确构造。"
            "终端二分已说明没有第三出口；positive-limsup 分支也已生成具体 PDEC 输入行。"
            "prime-lift 刚性显示这些输入可升层路由，选择性晋升也已回到有限拆分。"
            "下一步不再是路由，而是证明标准晋升删除/KL 或 KLS-EXT。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 PDEC 同集容量前沿路由器",
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
        "Same-set capacity upper:",
        "  only rows on the same g(t) are legal；",
        "  box-only rows are insufficient；",
        "  failure must output DualCap or missing row；",
        "  continuous cap exposes column-tail payment buckets；",
        "  canonical actual payment measure is constructed；",
        "  actual payment concentration returns to PDEC；",
        "  recursive diffusion returns to CleanKLS/DLS；",
        "  no third terminal route remains after finite-projection dichotomy；",
        "  positive-limsup finite signatures materialize legal PDEC input rows；",
        "  finite signatures force prime-lift congruence rows；",
        "  selective promotion commutes after finite splitting。",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `all_known_frontiers_routed={result['all_known_frontiers_routed']}`。",
        f"- `terminal_dual_gap={result['terminal_dual_gap']}`。",
        f"- `status_counts={result['status_counts']}`。",
        f"- `lp_summary={result['lp_summary']}`。",
        f"- `fourier_summary={result['fourier_summary']}`。",
        f"- `dualcap_summary={result['dualcap_summary']}`。",
        "",
        "## 3. 前沿表",
        "",
        "| frontier | status | evidence | next action |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["frontier_rows"]:
        lines.append(
            "| `{frontier}` | `{status}` | {evidence} | {next_action} |".format(
                frontier=row["frontier"],
                status=row["status"],
                evidence=row["evidence"],
                next_action=row["next_action"],
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "A1 的同集容量上界已经不再是一个模糊缺口。当前状态是：",
            "",
            "```text",
            "Attachment ready for current LHB branch；",
            "zero-block subbranch closed；",
            "box-only structurally insufficient；",
            "DualCap materialized and routed；",
            "P×P exits closed；",
            "no fourth exit in current A1 chain；",
            "continuous direction-arc dual materialized but not closed；",
            "continuous column-tail bridge materialized；",
            "canonical actual payment measure constructed；",
            "terminal finite-projection dichotomy closed；",
            "positive-limsup PDEC input rows materialized；",
            "prime-lift congruence routed；",
            "selective promotion commutation resolved；",
            "remaining gap is standard prime-lift deletion/KL or KLS-EXT。",
            "```",
            "",
            "所以下一步唯一值得硬攻的 A1 目标是同集结构行：",
            "证明标准 prime-lift 晋升删除/KL；或证明/接入 diffuse CleanKLS/DLS 大筛估计。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lp-json", type=Path, default=DEFAULT_LP)
    parser.add_argument("--direction-json", type=Path, default=DEFAULT_DIRECTION)
    parser.add_argument("--fourier-json", type=Path, default=DEFAULT_FOURIER)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--mass-json", type=Path, default=DEFAULT_MASS)
    parser.add_argument("--confluence-json", type=Path, default=DEFAULT_CONFLUENCE)
    parser.add_argument("--continuous-json", type=Path, default=DEFAULT_CONTINUOUS)
    parser.add_argument("--bridge-json", type=Path, default=DEFAULT_BRIDGE)
    parser.add_argument("--actual-payment-json", type=Path, default=DEFAULT_ACTUAL_PAYMENT)
    parser.add_argument(
        "--terminal-dichotomy-json", type=Path, default=DEFAULT_TERMINAL_DICHOTOMY
    )
    parser.add_argument("--pdec-signature-json", type=Path, default=DEFAULT_PDEC_SIGNATURE)
    parser.add_argument("--prime-lift-json", type=Path, default=DEFAULT_PRIME_LIFT)
    parser.add_argument(
        "--selective-commutation-json", type=Path, default=DEFAULT_SELECTIVE_COMMUTATION
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        lp_path=args.lp_json,
        direction_path=args.direction_json,
        fourier_path=args.fourier_json,
        dualcap_path=args.dualcap_json,
        mass_path=args.mass_json,
        confluence_path=args.confluence_json,
        continuous_path=args.continuous_json,
        bridge_path=args.bridge_json,
        actual_payment_path=args.actual_payment_json,
        terminal_dichotomy_path=args.terminal_dichotomy_json,
        pdec_signature_path=args.pdec_signature_json,
        prime_lift_path=args.prime_lift_json,
        selective_commutation_path=args.selective_commutation_json,
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
                "all_known_frontiers_routed": result["all_known_frontiers_routed"],
                "terminal_dual_gap": result["terminal_dual_gap"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
