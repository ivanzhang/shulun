#!/usr/bin/env python3
"""审计 bridge-root endpoint slack 是否来自移动端点屏障顺序。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_moving_endpoint_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.md

本层承接 endpoint slack 证书。对 D-singleton，上一层的 slack

    P-q-g*(1+r)

等于

    (P-g*r)-q_next,

其中 q_next 是 bridge root。因此 endpoint slack 非负被压成
bridge root 不超过移动屏障 q_barrier=P-g*r。有限审计中两个 barrier
值 631 与 607 都落在同一条 q-spine 577->607->631 上。
该层仍不证明统一 barrier-order law。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ENDPOINT_SLACK_JSON = DOCS / (
    "prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.json"
)
QSPINE_JSON = DOCS / (
    "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json"
)

BARRIER_ORDER_LAW = "BridgeRootMovingEndpointBarrierOrderLawOrPDEC"
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
    paths = [Path(__file__).resolve(), ENDPOINT_SLACK_JSON, QSPINE_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def transition_label(row: dict[str, Any]) -> str:
    """微转移标签。"""
    return f"m{row['m']} q{row['q']}->{row['q_next']}"


def d_singleton_rows(endpoint_payload: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取 D-singleton endpoint-slack 行。"""
    return [
        row
        for row in endpoint_payload["endpoint_slack_rows"]
        if row["micro_role"] == "D_singleton_bridge_old"
    ]


def barrier_rows(
    endpoint_payload: dict[str, Any],
    qspine_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    """把 D-singleton slack 行改写成 moving endpoint barrier 行。"""
    q_nodes = list(qspine_payload["q_spine_summary"]["q_spine_nodes"])
    rows: list[dict[str, Any]] = []
    for row in d_singleton_rows(endpoint_payload):
        P = int(row["P"])
        r = int(row["r"])
        g = int(row["g"])
        bridge_q = int(row["q_next"])
        barrier_q = P - g * r
        barrier_distance = barrier_q - bridge_q
        endpoint_slack = int(row["endpoint_slack"])
        rows.append(
            {
                "packet_id": row["packet_id"],
                "atom_key": row["atom_key"],
                "transition": transition_label(row),
                "P": P,
                "m": int(row["m"]),
                "r": r,
                "g": g,
                "bridge_root_q": bridge_q,
                "moving_endpoint_barrier_q": barrier_q,
                "endpoint_slack": endpoint_slack,
                "barrier_distance_to_bridge": barrier_distance,
                "endpoint_slack_equals_barrier_distance": barrier_distance == endpoint_slack,
                "barrier_on_qspine": barrier_q in q_nodes,
                "bridge_on_qspine": bridge_q in q_nodes,
                "barrier_qspine_index": q_nodes.index(barrier_q) if barrier_q in q_nodes else None,
                "bridge_qspine_index": q_nodes.index(bridge_q) if bridge_q in q_nodes else None,
                "barrier_order_closed": bridge_q <= barrier_q,
                "zero_barrier_contact": bridge_q == barrier_q,
                "phase_delta_num": int(row["phase_delta_num"]),
                "residual_term_gD": int(row["residual_term_gD"]),
            }
        )
    return rows


def shift_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总两条 D-singleton 行的移动屏障漂移。"""
    ordered = sorted(rows, key=lambda row: row["packet_id"])
    if len(ordered) != 2:
        return {"packet_count": len(ordered), "two_packet_shift_closed": False}
    first, second = ordered
    m_gap = second["m"] - first["m"]
    r_gap = second["r"] - first["r"]
    bridge_shift = second["bridge_root_q"] - first["bridge_root_q"]
    barrier_shift = second["moving_endpoint_barrier_q"] - first["moving_endpoint_barrier_q"]
    slack_drop = first["endpoint_slack"] - second["endpoint_slack"]
    return {
        "packet_count": len(ordered),
        "two_packet_shift_closed": True,
        "m_gap": m_gap,
        "r_gap": r_gap,
        "common_D_gap_g": first["g"] if first["g"] == second["g"] else None,
        "bridge_shift": bridge_shift,
        "barrier_shift": barrier_shift,
        "barrier_slope_times_r_gap": -first["g"] * r_gap,
        "slack_drop": slack_drop,
        "slack_drop_equals_bridge_shift_minus_barrier_shift": slack_drop
        == bridge_shift - barrier_shift,
        "first_barrier": first["moving_endpoint_barrier_q"],
        "second_barrier": second["moving_endpoint_barrier_q"],
        "zero_contact_transition": next(
            (row["transition"] for row in ordered if row["zero_barrier_contact"]),
            None,
        ),
    }


def build_certificate() -> dict[str, Any]:
    """组装 moving endpoint barrier 证书。"""
    endpoint_payload = load_json(ENDPOINT_SLACK_JSON)
    qspine_payload = load_json(QSPINE_JSON)
    rows = barrier_rows(endpoint_payload, qspine_payload)
    summary = shift_summary(rows)
    all_distance_closed = all(row["endpoint_slack_equals_barrier_distance"] for row in rows)
    all_barriers_on_spine = all(row["barrier_on_qspine"] for row in rows)
    all_bridges_on_spine = all(row["bridge_on_qspine"] for row in rows)
    finite_barrier_order_closed = all(row["barrier_order_closed"] for row in rows)
    zero_contact_count = sum(1 for row in rows if row["zero_barrier_contact"])
    reduction_closed = (
        endpoint_payload.get("bridge_root_endpoint_slack_reduction_closed") is True
        and len(rows) == 2
        and all_distance_closed
        and all_barriers_on_spine
        and all_bridges_on_spine
        and finite_barrier_order_closed
        and summary.get("two_packet_shift_closed") is True
    )
    latest_gate = (
        f"{BARRIER_ORDER_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
        f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} "
        f"AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_bridge_root_moving_endpoint_barrier_router",
        "status": "bridge_root_moving_endpoint_barrier_reduction_closed_uniform_order_law_open",
        "verified_date": "2026-05-25",
        "previous_endpoint_slack_reduction_closed": endpoint_payload.get(
            "bridge_root_endpoint_slack_reduction_closed"
        )
        is True,
        "D_singleton_barrier_row_count": len(rows),
        "endpoint_slack_equals_barrier_distance_closed": all_distance_closed,
        "all_barriers_lie_on_qspine": all_barriers_on_spine,
        "all_bridge_roots_lie_on_qspine": all_bridges_on_spine,
        "finite_bridge_root_barrier_order_closed": finite_barrier_order_closed,
        "zero_barrier_contact_count": zero_contact_count,
        "bridge_root_moving_endpoint_barrier_reduction_closed": reduction_closed,
        "bridge_root_uniform_barrier_order_law_proved": False,
        "right_tail_overhang_pdec_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "identity": "D-singleton endpoint_slack = (P-g*r)-q_bridge, where q_bridge=q_next",
        "q_spine_nodes": qspine_payload["q_spine_summary"]["q_spine_nodes"],
        "barrier_rows": rows,
        "two_packet_shift_summary": summary,
        "next_primary_attack_target": BARRIER_ORDER_LAW,
        "latest_open_gate": latest_gate,
        "plain_conclusion": (
            "Endpoint slack nonnegativity is equivalent in the audited D-singletons "
            "to bridge_root_q <= P-g*r.  Both moving barriers lie on the same q-spine; "
            "the thin m761 row is exact barrier contact at q=607.  The remaining "
            "uniform problem is the moving endpoint barrier order law or PDEC."
        ),
        "gate_rows": [
            {
                "gate": "EndpointSlackImported",
                "closed": endpoint_payload.get("bridge_root_endpoint_slack_reduction_closed") is True,
                "proved": endpoint_payload.get("bridge_root_endpoint_slack_reduction_closed") is True,
                "meaning": "the endpoint slack reduction is imported.",
                "remaining": "none for import",
            },
            {
                "gate": "SlackAsBarrierDistance",
                "closed": all_distance_closed,
                "proved": all_distance_closed,
                "meaning": "D-singleton endpoint slack equals (P-g*r)-bridge_root_q.",
                "remaining": "finite barrier-distance identity",
            },
            {
                "gate": "BarrierNodesOnQSpine",
                "closed": all_barriers_on_spine and all_bridges_on_spine,
                "proved": all_barriers_on_spine and all_bridges_on_spine,
                "meaning": "both bridge roots and both moving barriers are q-spine nodes.",
                "remaining": "finite q-spine barrier ledger",
            },
            {
                "gate": "FiniteBridgeRootBarrierOrder",
                "closed": finite_barrier_order_closed,
                "proved": finite_barrier_order_closed,
                "meaning": "in the audited rows bridge_root_q <= moving_endpoint_barrier_q.",
                "remaining": "finite barrier order ledger",
            },
            {
                "gate": "UniformMovingEndpointBarrierOrderLaw",
                "closed": False,
                "proved": False,
                "meaning": "a uniform law must force bridge roots not to pass the moving endpoint barrier.",
                "remaining": BARRIER_ORDER_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite moving-barrier reduction, not a global parity-breaking theorem.",
                "remaining": (
                    f"{BARRIER_ORDER_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
                    f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}"
                ),
            },
        ],
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal boundary bridge-root moving endpoint barrier 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 endpoint slack 非负门继续压成 moving endpoint barrier 顺序。",
        "",
        "```text",
        f"previous_endpoint_slack_reduction_closed={fmt_bool(payload['previous_endpoint_slack_reduction_closed'])}",
        f"D_singleton_barrier_row_count={payload['D_singleton_barrier_row_count']}",
        f"endpoint_slack_equals_barrier_distance_closed={fmt_bool(payload['endpoint_slack_equals_barrier_distance_closed'])}",
        f"all_barriers_lie_on_qspine={fmt_bool(payload['all_barriers_lie_on_qspine'])}",
        f"all_bridge_roots_lie_on_qspine={fmt_bool(payload['all_bridge_roots_lie_on_qspine'])}",
        f"finite_bridge_root_barrier_order_closed={fmt_bool(payload['finite_bridge_root_barrier_order_closed'])}",
        f"zero_barrier_contact_count={payload['zero_barrier_contact_count']}",
        f"bridge_root_moving_endpoint_barrier_reduction_closed={fmt_bool(payload['bridge_root_moving_endpoint_barrier_reduction_closed'])}",
        f"bridge_root_uniform_barrier_order_law_proved={fmt_bool(payload['bridge_root_uniform_barrier_order_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "核心恒等式：",
        "",
        "```text",
        payload["identity"],
        "```",
        "",
        f"q-spine nodes: `{payload['q_spine_nodes']}`",
        "",
        "## 1. barrier rows",
        "",
        "| transition | r | bridge q | barrier q=P-gr | slack | barrier on spine | contact |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in payload["barrier_rows"]:
        lines.append(
            "| {transition} | {r} | {bridge} | {barrier} | {slack} | `{on_spine}` | `{contact}` |".format(
                transition=row["transition"],
                r=row["r"],
                bridge=row["bridge_root_q"],
                barrier=row["moving_endpoint_barrier_q"],
                slack=row["endpoint_slack"],
                on_spine=fmt_bool(row["barrier_on_qspine"]),
                contact=fmt_bool(row["zero_barrier_contact"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. two-packet shift summary",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in payload["two_packet_shift_summary"].items():
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
        "bridge_root_moving_endpoint_barrier_reduction_closed="
        f"{fmt_bool(payload['bridge_root_moving_endpoint_barrier_reduction_closed'])}"
    )
    print(f"q_spine_nodes={payload['q_spine_nodes']}")
    print(f"zero_barrier_contact_count={payload['zero_barrier_contact_count']}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
