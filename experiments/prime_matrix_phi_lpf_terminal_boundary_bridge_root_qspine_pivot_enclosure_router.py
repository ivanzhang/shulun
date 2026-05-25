#!/usr/bin/env python3
"""审计 q-spine index gap 是否来自 shared-pivot enclosure。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_pivot_enclosure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.md

本层承接 q-spine index-gap 证书。上一层的最新硬点是 bridge index 不超过
barrier index。本层利用 q-spine microtemplate 中的 shared pivot q=607，把它
进一步拆成：

    bridge_index <= pivot_index <= barrier_index.

有限审计中第一包为 577 <= 607 <= 631，第二包为 607 = 607 = 607。endpoint
slack 也分解成 bridge-to-pivot gap 与 pivot-to-barrier gap 的和。
该层仍不证明统一 pivot-enclosure law。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

INDEX_GAP_JSON = DOCS / (
    "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-router.json"
)
QSPINE_JSON = DOCS / (
    "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json"
)

PIVOT_ENCLOSURE_LAW = "BridgeRootQSpinePivotEnclosureLawOrPDEC"
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
    paths = [Path(__file__).resolve(), INDEX_GAP_JSON, QSPINE_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def gap_sum(q_nodes: list[int], start_index: int, end_index: int) -> int:
    """沿 q-spine 从 start_index 到 end_index 的有向 gap 和。"""
    if start_index <= end_index:
        return sum(q_nodes[i + 1] - q_nodes[i] for i in range(start_index, end_index))
    return -sum(q_nodes[i + 1] - q_nodes[i] for i in range(end_index, start_index))


def pivot_enclosure_rows(
    index_payload: dict[str, Any],
    pivot_index: int,
) -> list[dict[str, Any]]:
    """把 index-gap rows 改写成 shared-pivot enclosure rows。"""
    q_nodes = [int(q) for q in index_payload["q_spine_nodes"]]
    rows: list[dict[str, Any]] = []
    for row in index_payload["index_gap_rows"]:
        bridge_index = int(row["bridge_qspine_index"])
        barrier_index = int(row["barrier_qspine_index"])
        bridge_to_pivot = pivot_index - bridge_index
        pivot_to_barrier = barrier_index - pivot_index
        left_gap_sum = gap_sum(q_nodes, bridge_index, pivot_index)
        right_gap_sum = gap_sum(q_nodes, pivot_index, barrier_index)
        endpoint_slack = int(row["endpoint_slack"])
        rows.append(
            {
                "packet_id": row["packet_id"],
                "atom_key": row["atom_key"],
                "transition": row["transition"],
                "m": int(row["m"]),
                "bridge_root_q": int(row["bridge_root_q"]),
                "moving_endpoint_barrier_q": int(row["moving_endpoint_barrier_q"]),
                "bridge_qspine_index": bridge_index,
                "pivot_qspine_index": pivot_index,
                "barrier_qspine_index": barrier_index,
                "bridge_to_pivot_index_gap": bridge_to_pivot,
                "pivot_to_barrier_index_gap": pivot_to_barrier,
                "pivot_enclosure_closed": bridge_to_pivot >= 0 and pivot_to_barrier >= 0,
                "bridge_to_pivot_gap_sum": left_gap_sum,
                "pivot_to_barrier_gap_sum": right_gap_sum,
                "pivot_gap_sum_total": left_gap_sum + right_gap_sum,
                "endpoint_slack": endpoint_slack,
                "endpoint_slack_equals_pivot_gap_sum": left_gap_sum + right_gap_sum
                == endpoint_slack,
                "exact_pivot_contact": bridge_index == pivot_index == barrier_index,
            }
        )
    return rows


def pivot_shift_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总两包相对于 shared pivot 的靠拢模式。"""
    ordered = sorted(rows, key=lambda row: row["packet_id"])
    if len(ordered) != 2:
        return {"packet_count": len(ordered), "two_packet_pivot_shift_closed": False}
    first, second = ordered
    bridge_to_pivot_drop = (
        first["bridge_to_pivot_index_gap"] - second["bridge_to_pivot_index_gap"]
    )
    pivot_to_barrier_drop = (
        first["pivot_to_barrier_index_gap"] - second["pivot_to_barrier_index_gap"]
    )
    return {
        "packet_count": len(ordered),
        "two_packet_pivot_shift_closed": True,
        "first_bridge_to_pivot_index_gap": first["bridge_to_pivot_index_gap"],
        "first_pivot_to_barrier_index_gap": first["pivot_to_barrier_index_gap"],
        "second_bridge_to_pivot_index_gap": second["bridge_to_pivot_index_gap"],
        "second_pivot_to_barrier_index_gap": second["pivot_to_barrier_index_gap"],
        "bridge_to_pivot_drop": bridge_to_pivot_drop,
        "pivot_to_barrier_drop": pivot_to_barrier_drop,
        "both_sides_collapse_to_pivot": bridge_to_pivot_drop == 1
        and pivot_to_barrier_drop == 1,
        "exact_contact_transition": next(
            (row["transition"] for row in ordered if row["exact_pivot_contact"]),
            None,
        ),
    }


def build_certificate() -> dict[str, Any]:
    """组装 q-spine pivot-enclosure 证书。"""
    index_payload = load_json(INDEX_GAP_JSON)
    qspine_payload = load_json(QSPINE_JSON)
    q_nodes = [int(q) for q in index_payload["q_spine_nodes"]]
    shared_pivot_q = int(qspine_payload["q_spine_summary"]["shared_pivot_q"])
    pivot_index = q_nodes.index(shared_pivot_q)
    rows = pivot_enclosure_rows(index_payload, pivot_index)
    summary = pivot_shift_summary(rows)
    finite_enclosure_closed = all(row["pivot_enclosure_closed"] for row in rows)
    all_gap_sum_closed = all(row["endpoint_slack_equals_pivot_gap_sum"] for row in rows)
    exact_contact_count = sum(1 for row in rows if row["exact_pivot_contact"])
    reduction_closed = (
        index_payload.get("bridge_root_qspine_index_gap_reduction_closed") is True
        and len(rows) == 2
        and finite_enclosure_closed
        and all_gap_sum_closed
        and exact_contact_count == 1
        and summary.get("two_packet_pivot_shift_closed") is True
    )
    latest_gate = (
        f"{PIVOT_ENCLOSURE_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
        f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} "
        f"AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_pivot_enclosure_router",
        "status": "bridge_root_qspine_pivot_enclosure_reduction_closed_uniform_enclosure_law_open",
        "verified_date": "2026-05-25",
        "previous_qspine_index_gap_reduction_closed": index_payload.get(
            "bridge_root_qspine_index_gap_reduction_closed"
        )
        is True,
        "q_spine_nodes": q_nodes,
        "shared_pivot_q": shared_pivot_q,
        "shared_pivot_index": pivot_index,
        "pivot_enclosure_row_count": len(rows),
        "finite_pivot_enclosure_closed": finite_enclosure_closed,
        "endpoint_slack_equals_pivot_gap_sum_closed": all_gap_sum_closed,
        "exact_pivot_contact_count": exact_contact_count,
        "bridge_root_qspine_pivot_enclosure_reduction_closed": reduction_closed,
        "bridge_root_uniform_qspine_pivot_enclosure_law_proved": False,
        "right_tail_overhang_pdec_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "identity": "index order is certified by bridge_index <= pivot_index <= barrier_index",
        "pivot_enclosure_rows": rows,
        "two_packet_pivot_shift_summary": summary,
        "next_primary_attack_target": PIVOT_ENCLOSURE_LAW,
        "latest_open_gate": latest_gate,
        "plain_conclusion": (
            "The audited q-spine index order is explained by shared-pivot enclosure. "
            "The first row encloses q=607 between 577 and 631; the second row is exact "
            "pivot contact.  The remaining uniform problem is the q-spine pivot "
            "enclosure law or PDEC."
        ),
        "gate_rows": [
            {
                "gate": "QSpineIndexGapImported",
                "closed": index_payload.get("bridge_root_qspine_index_gap_reduction_closed")
                is True,
                "proved": index_payload.get("bridge_root_qspine_index_gap_reduction_closed")
                is True,
                "meaning": "the q-spine index-gap reduction is imported.",
                "remaining": "none for import",
            },
            {
                "gate": "SharedPivotImported",
                "closed": qspine_payload.get("unit_to_bridge_pivot_alignment_closed") is True,
                "proved": qspine_payload.get("unit_to_bridge_pivot_alignment_closed") is True,
                "meaning": "the q-spine has shared pivot q=607.",
                "remaining": "none for import",
            },
            {
                "gate": "FinitePivotEnclosure",
                "closed": finite_enclosure_closed,
                "proved": finite_enclosure_closed,
                "meaning": "bridge index <= pivot index <= barrier index in the audited rows.",
                "remaining": "finite pivot enclosure ledger",
            },
            {
                "gate": "SlackAsPivotGapSum",
                "closed": all_gap_sum_closed,
                "proved": all_gap_sum_closed,
                "meaning": "endpoint slack splits into bridge-to-pivot and pivot-to-barrier gap sums.",
                "remaining": "finite pivot gap ledger",
            },
            {
                "gate": "UniformQSpinePivotEnclosureLaw",
                "closed": False,
                "proved": False,
                "meaning": "a uniform law must force the shared pivot to lie between bridge root and barrier.",
                "remaining": PIVOT_ENCLOSURE_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite pivot-enclosure reduction, not a global parity-breaking theorem.",
                "remaining": (
                    f"{PIVOT_ENCLOSURE_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
                    f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}"
                ),
            },
        ],
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal boundary bridge-root q-spine pivot-enclosure 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 q-spine index-gap 顺序继续压成 shared-pivot enclosure。",
        "",
        "```text",
        f"previous_qspine_index_gap_reduction_closed={fmt_bool(payload['previous_qspine_index_gap_reduction_closed'])}",
        f"q_spine_nodes={payload['q_spine_nodes']}",
        f"shared_pivot_q={payload['shared_pivot_q']}",
        f"shared_pivot_index={payload['shared_pivot_index']}",
        f"pivot_enclosure_row_count={payload['pivot_enclosure_row_count']}",
        f"finite_pivot_enclosure_closed={fmt_bool(payload['finite_pivot_enclosure_closed'])}",
        f"endpoint_slack_equals_pivot_gap_sum_closed={fmt_bool(payload['endpoint_slack_equals_pivot_gap_sum_closed'])}",
        f"exact_pivot_contact_count={payload['exact_pivot_contact_count']}",
        f"bridge_root_qspine_pivot_enclosure_reduction_closed={fmt_bool(payload['bridge_root_qspine_pivot_enclosure_reduction_closed'])}",
        f"bridge_root_uniform_qspine_pivot_enclosure_law_proved={fmt_bool(payload['bridge_root_uniform_qspine_pivot_enclosure_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "核心恒等式：",
        "",
        "```text",
        payload["identity"],
        "```",
        "",
        "## 1. pivot-enclosure rows",
        "",
        "| transition | bridge q | pivot q | barrier q | bridge->pivot index | pivot->barrier index | left gap | right gap | slack | contact |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in payload["pivot_enclosure_rows"]:
        lines.append(
            "| {transition} | {bridge_q} | {pivot_q} | {barrier_q} | {left_i} | {right_i} | {left_gap} | {right_gap} | {slack} | `{contact}` |".format(
                transition=row["transition"],
                bridge_q=row["bridge_root_q"],
                pivot_q=payload["shared_pivot_q"],
                barrier_q=row["moving_endpoint_barrier_q"],
                left_i=row["bridge_to_pivot_index_gap"],
                right_i=row["pivot_to_barrier_index_gap"],
                left_gap=row["bridge_to_pivot_gap_sum"],
                right_gap=row["pivot_to_barrier_gap_sum"],
                slack=row["endpoint_slack"],
                contact=fmt_bool(row["exact_pivot_contact"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. two-packet pivot shift summary",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in payload["two_packet_pivot_shift_summary"].items():
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
        "bridge_root_qspine_pivot_enclosure_reduction_closed="
        f"{fmt_bool(payload['bridge_root_qspine_pivot_enclosure_reduction_closed'])}"
    )
    print(f"shared_pivot_q={payload['shared_pivot_q']}")
    print(f"shared_pivot_index={payload['shared_pivot_index']}")
    print(f"exact_pivot_contact_count={payload['exact_pivot_contact_count']}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
