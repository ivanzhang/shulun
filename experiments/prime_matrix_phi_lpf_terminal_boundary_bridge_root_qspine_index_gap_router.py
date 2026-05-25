#!/usr/bin/env python3
"""审计 moving endpoint barrier 是否等价于 q-spine 索引间隔。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_index_gap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-router.md

本层承接 moving endpoint barrier 证书。上一层把 endpoint slack 写成

    (P-g*r)-q_bridge.

由于有限账本中 bridge roots 与 moving barriers 都落在同一条 q-spine
577 -> 607 -> 631 上，本层把 barrier order 再改写成 q-spine 索引间隔：

    endpoint_slack = sum of adjacent q-spine gaps from bridge index to barrier index.

该层仍不证明统一 q-spine index-order law，只把最新硬点压成离散索引顺序或 PDEC。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

MOVING_BARRIER_JSON = DOCS / (
    "prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.json"
)
QSPINE_JSON = DOCS / (
    "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json"
)

INDEX_ORDER_LAW = "BridgeRootQSpineIndexBarrierOrderLawOrPDEC"
TAIL_OVERHANG_LAW = "RightSelectedTerminalTailOverhangPDEC"
MASS_RATIO_LAW = "BoundaryAdjacentRunMassRatioLawOrPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
GROUP_ORBIT_INPUT = "AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), MOVING_BARRIER_JSON, QSPINE_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def q_gap_vector(q_nodes: list[int]) -> list[int]:
    """相邻 q-spine gap。"""
    return [q_nodes[i + 1] - q_nodes[i] for i in range(len(q_nodes) - 1)]


def gap_sum(q_nodes: list[int], start_index: int, end_index: int) -> int:
    """沿 q-spine 从 start_index 到 end_index 的有向 gap 和。"""
    if start_index <= end_index:
        return sum(q_nodes[i + 1] - q_nodes[i] for i in range(start_index, end_index))
    return -sum(q_nodes[i + 1] - q_nodes[i] for i in range(end_index, start_index))


def node_role(q_value: int, q_nodes: list[int], shared_pivot: int | None) -> str:
    """给 q-spine 节点一个局部角色名。"""
    if q_value == shared_pivot:
        return "shared_pivot"
    if q_value == q_nodes[0]:
        return "left_bridge_root"
    if q_value == q_nodes[-1]:
        return "right_terminal_node"
    return "interior_spine_node"


def index_gap_rows(
    moving_payload: dict[str, Any],
    qspine_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    """把 moving barrier rows 改写成 q-spine index-gap rows。"""
    q_nodes = [int(q) for q in moving_payload["q_spine_nodes"]]
    shared_pivot = qspine_payload["q_spine_summary"].get("shared_pivot_q")
    rows: list[dict[str, Any]] = []
    for row in moving_payload["barrier_rows"]:
        bridge_q = int(row["bridge_root_q"])
        barrier_q = int(row["moving_endpoint_barrier_q"])
        bridge_index = q_nodes.index(bridge_q)
        barrier_index = q_nodes.index(barrier_q)
        index_gap = barrier_index - bridge_index
        q_gap_distance = gap_sum(q_nodes, bridge_index, barrier_index)
        endpoint_slack = int(row["endpoint_slack"])
        rows.append(
            {
                "packet_id": row["packet_id"],
                "atom_key": row["atom_key"],
                "transition": row["transition"],
                "m": int(row["m"]),
                "r": int(row["r"]),
                "g": int(row["g"]),
                "bridge_root_q": bridge_q,
                "moving_endpoint_barrier_q": barrier_q,
                "bridge_qspine_index": bridge_index,
                "barrier_qspine_index": barrier_index,
                "qspine_index_gap": index_gap,
                "index_order_closed": index_gap >= 0,
                "qspine_gap_distance": q_gap_distance,
                "endpoint_slack": endpoint_slack,
                "endpoint_slack_equals_qspine_gap_sum": q_gap_distance == endpoint_slack,
                "zero_index_contact": index_gap == 0,
                "bridge_node_role": node_role(bridge_q, q_nodes, shared_pivot),
                "barrier_node_role": node_role(barrier_q, q_nodes, shared_pivot),
            }
        )
    return rows


def index_shift_summary(rows: list[dict[str, Any]], q_nodes: list[int]) -> dict[str, Any]:
    """汇总两包之间的 q-spine 索引漂移。"""
    ordered = sorted(rows, key=lambda row: row["packet_id"])
    if len(ordered) != 2:
        return {"packet_count": len(ordered), "two_packet_index_shift_closed": False}
    first, second = ordered
    bridge_index_shift = second["bridge_qspine_index"] - first["bridge_qspine_index"]
    barrier_index_shift = second["barrier_qspine_index"] - first["barrier_qspine_index"]
    index_gap_drop = first["qspine_index_gap"] - second["qspine_index_gap"]
    slack_drop = first["endpoint_slack"] - second["endpoint_slack"]
    return {
        "packet_count": len(ordered),
        "two_packet_index_shift_closed": True,
        "bridge_index_shift": bridge_index_shift,
        "barrier_index_shift": barrier_index_shift,
        "index_gap_drop": index_gap_drop,
        "index_gap_drop_equals_bridge_minus_barrier_index_shift": index_gap_drop
        == bridge_index_shift - barrier_index_shift,
        "slack_drop": slack_drop,
        "slack_drop_equals_first_full_spine_gap_sum": slack_drop == gap_sum(
            q_nodes,
            first["bridge_qspine_index"],
            first["barrier_qspine_index"],
        ),
        "zero_contact_transition": next(
            (row["transition"] for row in ordered if row["zero_index_contact"]),
            None,
        ),
    }


def build_certificate() -> dict[str, Any]:
    """组装 q-spine index-gap 证书。"""
    moving_payload = load_json(MOVING_BARRIER_JSON)
    qspine_payload = load_json(QSPINE_JSON)
    q_nodes = [int(q) for q in moving_payload["q_spine_nodes"]]
    rows = index_gap_rows(moving_payload, qspine_payload)
    summary = index_shift_summary(rows, q_nodes)
    all_gap_sum_closed = all(row["endpoint_slack_equals_qspine_gap_sum"] for row in rows)
    finite_index_order_closed = all(row["index_order_closed"] for row in rows)
    zero_contact_count = sum(1 for row in rows if row["zero_index_contact"])
    index_gaps = [int(row["qspine_index_gap"]) for row in rows]
    reduction_closed = (
        moving_payload.get("bridge_root_moving_endpoint_barrier_reduction_closed") is True
        and len(rows) == 2
        and all_gap_sum_closed
        and finite_index_order_closed
        and summary.get("two_packet_index_shift_closed") is True
    )
    latest_gate = (
        f"{INDEX_ORDER_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
        f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} "
        f"AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_index_gap_router",
        "status": "bridge_root_qspine_index_gap_reduction_closed_uniform_index_order_law_open",
        "verified_date": "2026-05-25",
        "previous_moving_endpoint_barrier_reduction_closed": moving_payload.get(
            "bridge_root_moving_endpoint_barrier_reduction_closed"
        )
        is True,
        "q_spine_nodes": q_nodes,
        "q_spine_gap_vector": q_gap_vector(q_nodes),
        "q_spine_index_gap_row_count": len(rows),
        "endpoint_slack_equals_qspine_gap_sum_closed": all_gap_sum_closed,
        "finite_qspine_index_order_closed": finite_index_order_closed,
        "qspine_index_gaps": index_gaps,
        "min_qspine_index_gap": min(index_gaps) if index_gaps else None,
        "zero_index_contact_count": zero_contact_count,
        "bridge_root_qspine_index_gap_reduction_closed": reduction_closed,
        "bridge_root_uniform_qspine_index_order_law_proved": False,
        "right_tail_overhang_pdec_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "identity": (
            "endpoint_slack equals the q-spine adjacent-gap sum from bridge index "
            "to moving-barrier index"
        ),
        "index_gap_rows": rows,
        "two_packet_index_shift_summary": summary,
        "next_primary_attack_target": INDEX_ORDER_LAW,
        "latest_open_gate": latest_gate,
        "plain_conclusion": (
            "Moving endpoint barrier order is equivalent in the audited rows to "
            "nonnegative q-spine index gap.  The first row consumes both adjacent "
            "q-spine gaps 30+24=54, while the thin second row is exact index contact. "
            "The remaining uniform problem is the q-spine index barrier order law or PDEC."
        ),
        "gate_rows": [
            {
                "gate": "MovingEndpointBarrierImported",
                "closed": moving_payload.get("bridge_root_moving_endpoint_barrier_reduction_closed")
                is True,
                "proved": moving_payload.get("bridge_root_moving_endpoint_barrier_reduction_closed")
                is True,
                "meaning": "the moving endpoint barrier reduction is imported.",
                "remaining": "none for import",
            },
            {
                "gate": "SlackAsQSpineGapSum",
                "closed": all_gap_sum_closed,
                "proved": all_gap_sum_closed,
                "meaning": "endpoint slack equals the adjacent q-spine gap sum.",
                "remaining": "finite q-spine gap ledger",
            },
            {
                "gate": "FiniteQSpineIndexOrder",
                "closed": finite_index_order_closed,
                "proved": finite_index_order_closed,
                "meaning": "in the audited rows bridge index does not exceed barrier index.",
                "remaining": "finite index-order ledger",
            },
            {
                "gate": "UniformQSpineIndexBarrierOrderLaw",
                "closed": False,
                "proved": False,
                "meaning": "a uniform law must force nonnegative q-spine index gap.",
                "remaining": INDEX_ORDER_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite q-spine index-gap reduction, not a global parity-breaking theorem.",
                "remaining": (
                    f"{INDEX_ORDER_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
                    f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}"
                ),
            },
        ],
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal boundary bridge-root q-spine index-gap 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 moving endpoint barrier 顺序继续压成 q-spine 索引间隔。",
        "",
        "```text",
        f"previous_moving_endpoint_barrier_reduction_closed={fmt_bool(payload['previous_moving_endpoint_barrier_reduction_closed'])}",
        f"q_spine_nodes={payload['q_spine_nodes']}",
        f"q_spine_gap_vector={payload['q_spine_gap_vector']}",
        f"q_spine_index_gap_row_count={payload['q_spine_index_gap_row_count']}",
        f"endpoint_slack_equals_qspine_gap_sum_closed={fmt_bool(payload['endpoint_slack_equals_qspine_gap_sum_closed'])}",
        f"finite_qspine_index_order_closed={fmt_bool(payload['finite_qspine_index_order_closed'])}",
        f"qspine_index_gaps={payload['qspine_index_gaps']}",
        f"min_qspine_index_gap={payload['min_qspine_index_gap']}",
        f"zero_index_contact_count={payload['zero_index_contact_count']}",
        f"bridge_root_qspine_index_gap_reduction_closed={fmt_bool(payload['bridge_root_qspine_index_gap_reduction_closed'])}",
        f"bridge_root_uniform_qspine_index_order_law_proved={fmt_bool(payload['bridge_root_uniform_qspine_index_order_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "核心恒等式：",
        "",
        "```text",
        payload["identity"],
        "```",
        "",
        "## 1. index-gap rows",
        "",
        "| transition | bridge index | barrier index | index gap | q-gap sum | slack | bridge role | barrier role |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in payload["index_gap_rows"]:
        lines.append(
            "| {transition} | {bridge_i} | {barrier_i} | {index_gap} | {qgap} | {slack} | `{bridge_role}` | `{barrier_role}` |".format(
                transition=row["transition"],
                bridge_i=row["bridge_qspine_index"],
                barrier_i=row["barrier_qspine_index"],
                index_gap=row["qspine_index_gap"],
                qgap=row["qspine_gap_distance"],
                slack=row["endpoint_slack"],
                bridge_role=row["bridge_node_role"],
                barrier_role=row["barrier_node_role"],
            )
        )
    lines.extend(
        [
            "",
            "## 2. two-packet index shift summary",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in payload["two_packet_index_shift_summary"].items():
        lines.append(f"| `{key}` | `{cell(value)}` |")
    lines.extend(
        [
            "",
            "## 3. 门控表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload["gate_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=cell(row["meaning"]),
                remaining=cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.extend(["", "行/列命题仍未无条件闭合。", ""])
    return "\n".join(lines)


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")


def main() -> None:
    """命令入口。"""
    payload = build_certificate()
    write_outputs(payload)
    print(
        "bridge_root_qspine_index_gap_reduction_closed="
        f"{fmt_bool(payload['bridge_root_qspine_index_gap_reduction_closed'])}"
    )
    print(f"q_spine_gap_vector={payload['q_spine_gap_vector']}")
    print(f"qspine_index_gaps={payload['qspine_index_gaps']}")
    print(f"zero_index_contact_count={payload['zero_index_contact_count']}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
