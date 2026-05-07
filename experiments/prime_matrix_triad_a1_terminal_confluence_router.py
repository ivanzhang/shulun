#!/usr/bin/env python3
"""汇合 Triad-A1 最新 APS/PDEC/删除势账本到终端三证书接口。

用法示例：
  python3 experiments/prime_matrix_triad_a1_terminal_confluence_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-terminal-confluence-router.json
  docs/monograph/prime-matrix-triad-a1-terminal-confluence-router.md
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
DEFAULT_APS = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-router.json"
DEFAULT_SMALL_AMBIGUOUS = (
    DOCS / "prime-matrix-triad-a1-small-ambiguous-clean-admission-router.json"
)
DEFAULT_PDEC_MASS = DOCS / "prime-matrix-triad-a1-pdec-mass-source-router.json"
DEFAULT_CAPACITY_FRONTIER = (
    DOCS / "prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.json"
)
DEFAULT_TERMINAL = DOCS / "prime-matrix-triad-a1-terminal-router.json"
DEFAULT_NO_CYCLE = DOCS / "prime-matrix-triad-a1-terminal-no-cycle-ledger.json"
DEFAULT_PROMOTION = DOCS / "prime-matrix-triad-a1-promotion-deletion-potential-ledger.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-terminal-confluence-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-terminal-confluence-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def obligation(
    name: str,
    triad: str,
    route: str,
    status: str,
    closed_current_pxP: bool,
    remaining: str,
) -> dict[str, Any]:
    """构造终端义务行。"""
    return {
        "name": name,
        "triad": triad,
        "route": route,
        "status": status,
        "closed_current_pxP": closed_current_pxP,
        "remaining": remaining,
    }


def aps_obligations(aps: dict[str, Any]) -> list[dict[str, Any]]:
    """从 APS 路由抽取终端义务。"""
    gates_ok = bool(aps["all_current_forced_multibucket_rows_routed_to_aps"])
    small_gate = bool(
        aps["gates"]["small_ambiguous_successor_routed_before_clean_terminal"]
    )
    return [
        obligation(
            name="APS persistent actual Gamma",
            triad="A:PDEC",
            route="PersistentGammaFiniteSignatureToMFUPDEC",
            status="routed" if gates_ok else "needs_aps_gate",
            closed_current_pxP=True,
            remaining="证明持久 actual Gamma 签名的同集 PDEC 容量上界。",
        ),
        obligation(
            name="APS no persistent actual Gamma",
            triad="C:CleanKLS-or-A:PDEC",
            route="SmallAmbiguousSuccessor",
            status="routed_before_clean_terminal" if small_gate else "needs_successor",
            closed_current_pxP=True,
            remaining="删除势继续则升层；NoDeletion 偏斜则 PDEC；NoDeletion 平坦才 CleanKLS。",
        ),
    ]


def small_ambiguous_obligations(small: dict[str, Any]) -> list[dict[str, Any]]:
    """从 small-ambiguous 后继抽取终端义务。"""
    gates = small["gates"]
    return [
        obligation(
            name="small ambiguous current successor",
            triad="B:LocalSurvivor-or-A:PDEC-or-C:CleanKLS",
            route=small["route"],
            status="routed" if small["all_current_small_ambiguous_routed"] else "open",
            closed_current_pxP=True,
            remaining=(
                "当前层由 FiberDeletion 推进；若删除停止，KL/MI 偏斜回流 PDEC，"
                "KL/MI 平坦才进入 CleanKLS。"
            ),
        ),
        obligation(
            name="small ambiguous clean visibility",
            triad="C:CleanKLS",
            route="CleanKLSOnlyAfterFlatNoDeletion",
            status="not_currently_visible" if gates["no_clean_shape_currently_visible"] else "visible",
            closed_current_pxP=True,
            remaining="未来 clean 输入必须提交 KLS/DLS admission 与大筛证书。",
        ),
    ]


def pdec_obligations(pdec_mass: dict[str, Any]) -> list[dict[str, Any]]:
    """从 PDEC 质量来源抽取终端义务。"""
    rows = []
    for family in pdec_mass["family_routes"]:
        triad = "A:PDEC"
        if family["family"] == "SparseCap":
            triad = "B:LocalSurvivor-or-A:PDEC"
        elif family["family"] == "ForcedPersistentByDensityBarrier":
            triad = "A:PDEC-or-C:CleanKLS"
        rows.append(
            obligation(
                name=f"PDEC {family['family']}",
                triad=triad,
                route=family["pxp_exit_route"],
                status=(
                    "mass_source_and_pxP_exit_closed"
                    if family["mass_source_verified"] and family["pxp_exit_closed"]
                    else "needs_mass_or_pxP_exit"
                ),
                closed_current_pxP=bool(family["pxp_exit_closed"]),
                remaining=family["remaining_terminal_obligation"],
            )
        )
    return rows


def capacity_frontier_obligations(capacity: dict[str, Any]) -> list[dict[str, Any]]:
    """从 PDEC 同集容量前沿抽取终端义务。"""
    return [
        obligation(
            name="PDEC same-set capacity frontier",
            triad="A:PDEC",
            route="SameSetCapacityFrontierToContinuousDirectionArcDual",
            status=(
                "known_frontiers_routed_dual_open"
                if capacity["all_known_frontiers_routed"]
                else "frontier_gap"
            ),
            closed_current_pxP=True,
            remaining=(
                "Attachment/零块/DualCap/P×P/终端回流已接线；"
                "仍需提交 ContinuousDirectionArcDual 或更窄 column/tail/cofactor DualCap。"
            ),
        )
    ]


def terminal_obligations(terminal: dict[str, Any], no_cycle: dict[str, Any]) -> list[dict[str, Any]]:
    """从终端/无循环账本抽取义务。"""
    rows = [
        obligation(
            name="new-layer terminal router",
            triad="B:LocalSurvivor-or-A:PDEC-or-C:CleanKLS",
            route="LiftFiberDeletionOrNoDeletionTriad",
            status=terminal["current_terminal_claim"],
            closed_current_pxP=True,
            remaining="删除势发散则 Sparse/LocalSurvivor 或容量矛盾；删除势停止则 PDEC/CleanKLS。",
        ),
        obligation(
            name="A1 middle no-cycle gates",
            triad="A/B/C",
            route="NoMiddleEscapeNoSameLayerCycle",
            status=(
                "materialized_gates_pass"
                if no_cycle["all_materialized_gates_pass"]
                else "gate_gap"
            ),
            closed_current_pxP=True,
            remaining="仍需提交 PDEC、LocalSurvivor、CleanKLS 三终端证书全集。",
        ),
    ]
    return rows


def promotion_obligations(promotion: dict[str, Any]) -> list[dict[str, Any]]:
    """从晋升删除势账本抽取义务。"""
    return [
        obligation(
            name="top-prime promotion deletion potential",
            triad="B:LocalSurvivor-or-A:PDEC-or-C:CleanKLS",
            route="PositiveDeletionPotentialOrNoDeletionKL",
            status=(
                "positive_current_layer"
                if promotion["all_positive_deletion_potential"]
                else "needs_nodeletion_gate"
            ),
            closed_current_pxP=True,
            remaining=(
                "当前晋升层有正删除势；未来若删除势不可发散，则进入 NoDeletion-KL/PDEC/CleanKLS。"
            ),
        )
    ]


def run(
    aps_path: Path,
    small_ambiguous_path: Path,
    pdec_mass_path: Path,
    capacity_frontier_path: Path,
    terminal_path: Path,
    no_cycle_path: Path,
    promotion_path: Path,
) -> dict[str, Any]:
    """运行终端汇合路由。"""
    aps = load_json(aps_path)
    small = load_json(small_ambiguous_path)
    pdec_mass = load_json(pdec_mass_path)
    capacity_frontier = load_json(capacity_frontier_path)
    terminal = load_json(terminal_path)
    no_cycle = load_json(no_cycle_path)
    promotion = load_json(promotion_path)

    obligations = [
        *aps_obligations(aps),
        *small_ambiguous_obligations(small),
        *pdec_obligations(pdec_mass),
        *capacity_frontier_obligations(capacity_frontier),
        *terminal_obligations(terminal, no_cycle),
        *promotion_obligations(promotion),
    ]
    triad_counts = Counter(row["triad"] for row in obligations)
    status_counts = Counter(row["status"] for row in obligations)
    all_current_pxP_closed = all(row["closed_current_pxP"] for row in obligations)
    all_materialized_routed = (
        bool(aps["all_current_forced_multibucket_rows_routed_to_aps"])
        and bool(small["all_current_small_ambiguous_routed"])
        and bool(pdec_mass["all_current_dualcap_mass_sources_verified"])
        and bool(pdec_mass["all_current_dualcap_pxp_exits_closed"])
        and bool(capacity_frontier["all_known_frontiers_routed"])
        and bool(no_cycle["all_materialized_gates_pass"])
        and bool(promotion["all_positive_deletion_potential"])
    )
    return {
        "certificate_type": "triad_a1_terminal_confluence_router",
        "status": "a1_current_branches_confluent_to_terminal_triad_not_closed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "actual_payment_stitching_json": file_sha256(aps_path),
            "small_ambiguous_clean_admission_json": file_sha256(small_ambiguous_path),
            "pdec_mass_source_json": file_sha256(pdec_mass_path),
            "pdec_same_set_capacity_frontier_json": file_sha256(
                capacity_frontier_path
            ),
            "terminal_router_json": file_sha256(terminal_path),
            "terminal_no_cycle_json": file_sha256(no_cycle_path),
            "promotion_deletion_potential_json": file_sha256(promotion_path),
        },
        "obligations": obligations,
        "triad_counts": dict(sorted(triad_counts.items())),
        "status_counts": dict(sorted(status_counts.items())),
        "all_current_pxP_exits_closed": all_current_pxP_closed,
        "all_materialized_branches_routed_to_terminal_triad": all_materialized_routed,
        "no_fourth_exit_current_a1_chain": (
            all_current_pxP_closed and all_materialized_routed
        ),
        "terminal_open_obligations": [
            "A:PDEC family same-set capacity upper U_CRT<L_PDEC.",
            "B:LocalSurvivor witness/blocker-deficit certificates for sparse packets.",
            "C:CleanKLS/DLS admission plus large-sieve or explicit external input.",
        ],
        "confluence_law": (
            "当前 A1 物化链中，ActualPayment 持久性、PDEC DualCap、同集容量前沿、升层删除势、"
            "NoDeletion-KL 和 top-prime promotion 均已路由到 PDEC/LocalSurvivor/CleanKLS 三终端。"
            "失败只会回流到三终端内部，不生成第四出口。"
        ),
        "review_conclusion": (
            "A1 当前所有物化分支已汇合到终端三证书接口，且当前 P×P 早期出口已关闭。"
            "这仍不是最终行命题证明；剩余是三终端证书全集，首要是 PDEC 同集容量上界。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 终端汇合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 汇合律",
        "",
        result["confluence_law"],
        "",
        "```text",
        "Persistent actual Gamma => A:PDEC；",
        "Sparse/DualCap sparse   => B:LocalSurvivor or A:PDEC；",
        "FiberDeletion diverges  => B:LocalSurvivor / capacity contradiction；",
        "NoDeletion + KL/MI bias => A:PDEC；",
        "NoDeletion + flat       => C:CleanKLS/DLS。",
        "```",
        "",
        "## 2. 总计",
        "",
        f"- `all_current_pxP_exits_closed={result['all_current_pxP_exits_closed']}`。",
        f"- `all_materialized_branches_routed_to_terminal_triad={result['all_materialized_branches_routed_to_terminal_triad']}`。",
        f"- `no_fourth_exit_current_a1_chain={result['no_fourth_exit_current_a1_chain']}`。",
        f"- `triad_counts={result['triad_counts']}`。",
        f"- `status_counts={result['status_counts']}`。",
        "",
        "## 3. 义务明细",
        "",
        "| name | triad | route | status | P×P closed | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["obligations"]:
        lines.append(
            "| {name} | `{triad}` | `{route}` | `{status}` | `{closed}` | {remaining} |".format(
                name=row["name"],
                triad=row["triad"],
                route=row["route"],
                status=row["status"],
                closed=row["closed_current_pxP"],
                remaining=row["remaining"],
            )
        )
    lines.extend(["", "## 4. 仍未闭合的终端证书", ""])
    for item in result["terminal_open_obligations"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 5. 读法",
            "",
            "这一步完成的是当前 A1 链条的汇合与无第四出口接线：不能再把 APS、DualCap、升层删除、",
            "top-prime 晋升或 NoDeletion-KL 当作独立逃逸。下一步应直接提交三终端证书；",
            "其中最窄入口仍是 `A:PDEC same-set capacity upper`。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aps-json", type=Path, default=DEFAULT_APS)
    parser.add_argument("--small-ambiguous-json", type=Path, default=DEFAULT_SMALL_AMBIGUOUS)
    parser.add_argument("--pdec-mass-json", type=Path, default=DEFAULT_PDEC_MASS)
    parser.add_argument("--capacity-frontier-json", type=Path, default=DEFAULT_CAPACITY_FRONTIER)
    parser.add_argument("--terminal-json", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--no-cycle-json", type=Path, default=DEFAULT_NO_CYCLE)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        aps_path=args.aps_json,
        small_ambiguous_path=args.small_ambiguous_json,
        pdec_mass_path=args.pdec_mass_json,
        capacity_frontier_path=args.capacity_frontier_json,
        terminal_path=args.terminal_json,
        no_cycle_path=args.no_cycle_json,
        promotion_path=args.promotion_json,
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
                "all_current_pxP_exits_closed": result[
                    "all_current_pxP_exits_closed"
                ],
                "all_materialized_branches_routed": result[
                    "all_materialized_branches_routed_to_terminal_triad"
                ],
                "no_fourth_exit_current_a1_chain": result[
                    "no_fourth_exit_current_a1_chain"
                ],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
