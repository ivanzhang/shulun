#!/usr/bin/env python3
"""Prime Matrix strict 速率尾段 Mertens 最新前沿同步路由器。

用法示例：
  python3 experiments/prime_matrix_strict_rate_bearing_tail_mertens_latest_sync_router.py

输出：
  docs/monograph/prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json
  docs/monograph/prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_BRIDGE = DOCS / "prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json"
DEFAULT_MERTENS_FRONTIER = DOCS / "prime-matrix-strict-self-contained-mertens-tail-frontier-router.json"
DEFAULT_POST_FINITE = DOCS / "prime-matrix-strict-post-finite-theta-frontier-sync-router.json"
DEFAULT_GLOBAL_THETA = DOCS / "prime-matrix-strict-global-theta-envelope-external-match-router.json"
DEFAULT_MEISSEL_EXTERNAL = DOCS / "prime-matrix-b3-meissel-mertens-interval-external-router.json"
DEFAULT_ORDERED = DOCS / "prime-matrix-ordered-remaining-task-execution-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json"
DEFAULT_MD = DOCS / "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.md"

PDEC_KLS_PACKET = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
OLD_MERTENS = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
ZERO_THETA = "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000"
MEISSEL_INTERVAL = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
INTERNAL_CONTOUR = "InternalZeroFreeRegionToThetaContourEnvelopeLedger"
LOW_HEIGHT = "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
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


def build_rows(certs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 Mertens 最新同步判定表。"""
    bridge = certs["bridge"]
    frontier = certs["mertens_frontier"]
    post_finite = certs["post_finite"]
    global_theta = certs["global_theta"]
    meissel = certs["meissel_external"]
    ordered = certs["ordered"]

    guard = (
        bridge.get("counterexample_assumption_only") is True
        and bridge.get("empirical_absence_not_used") is True
        and bridge.get("row_column_unconditional_closed") is False
        and frontier.get("row_column_unconditional_closed") is False
    )
    bridge_active = (
        bridge.get("tail_ledger_strict_self_contained_proved") is False
        and bridge.get("strict_self_contained_replacement") == OLD_MERTENS
    )
    frontier_compressed = (
        frontier.get("finite_prime_steps_to_20000_closed") is True
        and frontier.get("partial_summation_interface_closed") is True
        and frontier.get("self_contained_mertens_tail_proved") is False
    )
    post_finite_synced = (
        post_finite.get("finite_theta_anchor_and_bridge_self_contained_closed") is True
        and post_finite.get("internal_zero_free_region_to_theta_contour_closed") is False
    )
    external_theta_ready = (
        global_theta.get("explicit_psi_theta_contour_envelope_strict_external_closed") is True
        and global_theta.get("finite_theta_bridge_strict_external_closed") is True
    )
    external_meissel_ready = meissel.get("meissel_mertens_interval_external_closed") is True
    ordered_basis_ready = (
        ordered.get("external_mertens_route_closed") is True
        and ordered.get("self_contained_mertens_tail_proved") is False
        and ordered.get("next_priority") == ZERO_THETA
    )

    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只同步尾段筛输入的解析前沿，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "OldSelfContainedDusartAtomIsActiveButOutdated",
            bridge_active,
            False,
            "`SelfContainedDusartReciprocalPrimeProofAppendixXGe10372` 是上一桥接层的粗命名，后续语料已将其继续展开。",
            OLD_MERTENS,
        ),
        row(
            "MertensTailFrontierCompressed",
            frontier_compressed,
            False,
            "有限素数倒数跳点、分部求和接口、DVP 符号排斥和初等尾项可复用；剩余进入显式 PNT/Mertens 包。",
            f"{ZERO_THETA} AND {MEISSEL_INTERVAL}",
        ),
        row(
            "PostFiniteThetaSyncImported",
            post_finite_synced,
            False,
            "theta@20000 与有限 theta 桥已自足移出；当前细化主攻点是 x>=20000 的内部 theta/PNT contour 包络。",
            INTERNAL_CONTOUR,
        ),
        row(
            "ExternalThetaAndMeisselRouteReady",
            external_theta_ready and external_meissel_ready,
            False,
            "外部条件路线下，theta 包络、有限桥和 Meissel-Mertens 区间均已严格匹配到 DStructure 门。",
            DSTRUCTURE,
        ),
        row(
            "OrderedCondensedBasisReady",
            ordered_basis_ready,
            False,
            "按序推进证书给出的严格自足替代基为显式零点自由 theta 包加 Meissel-Mertens 常数区间。",
            f"{ZERO_THETA} AND {MEISSEL_INTERVAL}",
        ),
        row(
            "StrictSelfContainedMertensTailStillOpen",
            False,
            False,
            "严格自足线仍未证明完整 Mertens 尾段，不能把外部 theta/Mertens 输入改写成作者侧自足证明。",
            f"{ZERO_THETA} AND {MEISSEL_INTERVAL}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "该同步只更新尾段解析前沿；速率 PDEC/CleanKLS、RatePreservation 与 DStructure 仍未全部完成。",
            f"{PDEC_KLS_PACKET} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Mertens 最新前沿同步。"""
    certs = {name: load_json(path) for name, path in paths.items()}
    rows = build_rows(certs)
    strict_condensed = (
        f"{PDEC_KLS_PACKET} AND ({ZERO_THETA} AND {MEISSEL_INTERVAL}) "
        f"AND {RATE} AND {DSTRUCTURE}"
    )
    strict_expanded_next = (
        f"{PDEC_KLS_PACKET} AND ({INTERNAL_CONTOUR} AND {LOW_HEIGHT} "
        f"AND {MEISSEL_INTERVAL}) AND {RATE} AND {DSTRUCTURE}"
    )
    external_basis = f"{PDEC_KLS_PACKET} AND {RATE} AND {DSTRUCTURE}"

    return {
        "certificate_type": "prime_matrix_strict_rate_bearing_tail_mertens_latest_sync_router",
        "status": "rate_bearing_tail_mertens_latest_sync_self_contained_pnt_package_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "old_self_contained_dusart_atom_refined": True,
        "external_mertens_theta_route_closed_to_dstructure": True,
        "strict_self_contained_mertens_tail_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "strict_self_contained_condensed_basis": strict_condensed,
        "strict_self_contained_expanded_next_basis": strict_expanded_next,
        "external_or_standard_remaining_basis": external_basis,
        "next_direct_attack_target": INTERNAL_CONTOUR,
        "secondary_attack_target": MEISSEL_INTERVAL,
        "parallel_attack_targets": [PDEC_KLS_PACKET, RATE, DSTRUCTURE],
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "source_hashes": {str(path.relative_to(ROOT)): sha256(path) for path in paths.values()},
        "plain_conclusion": (
            "本步把速率尾段中的旧 `SelfContainedDusart...` 粗原子同步到最新解析前沿："
            "严格自足替代线应写成显式零点自由 theta/PNT 包加 Meissel-Mertens 常数区间；"
            "更细的当前主攻点是 `InternalZeroFreeRegionToThetaContourEnvelopeLedger`。"
            "外部 Mertens/theta 路线可条件移除此尾段，但行/列命题仍未无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写出 Markdown 归档。"""
    lines = [
        "# Prime Matrix strict 速率尾段 Mertens 最新前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"old_self_contained_dusart_atom_refined={fmt_bool(result['old_self_contained_dusart_atom_refined'])}",
        f"external_mertens_theta_route_closed_to_dstructure={fmt_bool(result['external_mertens_theta_route_closed_to_dstructure'])}",
        f"strict_self_contained_mertens_tail_proved={fmt_bool(result['strict_self_contained_mertens_tail_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 剩余基",
        "",
        "严格自足压缩基：",
        "",
        "```text",
        result["strict_self_contained_condensed_basis"],
        "```",
        "",
        "当前细化主攻基：",
        "",
        "```text",
        result["strict_self_contained_expanded_next_basis"],
        "```",
        "",
        "接受外部或标准输入后的基：",
        "",
        "```text",
        result["external_or_standard_remaining_basis"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"直接攻 `{result['next_direct_attack_target']}`，并行保留 `{result['secondary_attack_target']}`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bridge", type=Path, default=DEFAULT_BRIDGE)
    parser.add_argument("--mertens-frontier", type=Path, default=DEFAULT_MERTENS_FRONTIER)
    parser.add_argument("--post-finite", type=Path, default=DEFAULT_POST_FINITE)
    parser.add_argument("--global-theta", type=Path, default=DEFAULT_GLOBAL_THETA)
    parser.add_argument("--meissel-external", type=Path, default=DEFAULT_MEISSEL_EXTERNAL)
    parser.add_argument("--ordered", type=Path, default=DEFAULT_ORDERED)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "bridge": args.bridge,
        "mertens_frontier": args.mertens_frontier,
        "post_finite": args.post_finite,
        "global_theta": args.global_theta,
        "meissel_external": args.meissel_external,
        "ordered": args.ordered,
    }
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
