#!/usr/bin/env python3
"""把 bridge-root q-spine pivot 硬口压成 shared-pivot hinge 合同。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_bridge_root_shared_pivot_hinge_contract_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-router.json

输出：
  data/prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-ledger.json
  docs/monograph/prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-router.json
  docs/monograph/prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-router.md

本层承接 boundary ratio q-spine pivot reduction。核心收缩是：

  endpoint_slack = moving_barrier_q - bridge_root_q
                 = P - q - g*(1+r),

并把 shared pivot q=607 的有限角色明确化：

  packet 1 unit_root = packet 2 bridge_root = packet 2 barrier = 607,
  packet 1 barrier  = packet 2 unit_root = 631.

这仍不是统一证明；它把 BridgeRootQSpinePivotEnclosureLawOrPDEC 拆成
shared-pivot 来源律、endpoint slack 非负律、q-spine gap 支付律和 sibling
q-spine payment 等更小接口。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

BOUNDARY_REDUCTION_JSON = DOCS / "prime-matrix-phi-lpf-boundary-ratio-qspine-pivot-reduction-router.json"
CARRY_BREAK_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.json"
QSPINE_MICRO_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json"
ENDPOINT_SLACK_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.json"
MOVING_BARRIER_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.json"
INDEX_GAP_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-router.json"
PIVOT_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json"
SIBLING_KERNEL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json"
LPF_BUCKET_JSON = DOCS / "prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json"
AFFINE_PARITY_JSON = DOCS / "prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.json"

SOURCE_FILES = [
    Path(__file__).resolve(),
    BOUNDARY_REDUCTION_JSON,
    CARRY_BREAK_JSON,
    QSPINE_MICRO_JSON,
    ENDPOINT_SLACK_JSON,
    MOVING_BARRIER_JSON,
    INDEX_GAP_JSON,
    PIVOT_JSON,
    SIBLING_KERNEL_JSON,
    LPF_BUCKET_JSON,
    AFFINE_PARITY_JSON,
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    DOCS / "external-theorem-index.md",
]

SHARED_PIVOT_LAW = "BridgeRootSharedPivotHingeLawOrPDEC"
ENDPOINT_SLACK_LAW = "BridgeRootEndpointSlackNonnegativeLawOrPDEC"
QSPINE_GAP_PAYMENT_LAW = "BridgeRootQSpineGapPaymentLawOrPDEC"
SIBLING_KERNEL_LAW = "TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
GROUP_ORBIT_INPUT = "AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def compact_fraction(record: Any) -> str:
    """压缩 JSON 分数字段。"""
    if isinstance(record, dict) and "fraction" in record and "decimal" in record:
        return f"{record['decimal']} ({record['fraction']})"
    return str(record)


def by_packet(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 packet_id 建索引。"""
    return {int(row["packet_id"]): row for row in rows}


def endpoint_d_rows(endpoint_payload: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """抽取 D-singleton endpoint slack 行。"""
    rows = [
        row
        for row in endpoint_payload["endpoint_slack_rows"]
        if row["micro_role"] == "D_singleton_bridge_old"
    ]
    return by_packet(rows)


def packet_hinge_rows(
    carry_payload: dict[str, Any],
    endpoint_payload: dict[str, Any],
    barrier_payload: dict[str, Any],
    pivot_payload: dict[str, Any],
    shared_pivot_q: int,
) -> list[dict[str, Any]]:
    """组装两个 bridge-root packet 的 hinge 行。"""
    carry_rows = by_packet(carry_payload["packet_rows"])
    endpoint_rows = endpoint_d_rows(endpoint_payload)
    barrier_rows = by_packet(barrier_payload["barrier_rows"])
    pivot_rows = by_packet(pivot_payload["pivot_enclosure_rows"])
    rows: list[dict[str, Any]] = []
    for packet_id in sorted(endpoint_rows):
        endpoint = endpoint_rows[packet_id]
        carry = carry_rows[packet_id]
        barrier = barrier_rows[packet_id]
        pivot = pivot_rows[packet_id]
        P = int(endpoint["P"])
        q = int(endpoint["q"])
        g = int(endpoint["g"])
        r = int(endpoint["r"])
        bridge_from_endpoint = q + g
        barrier_from_endpoint = P - g * r
        endpoint_slack_formula = P - q - g * (1 + r)
        bridge_root_q = int(carry["bridge_root_q"])
        unit_root_q = int(carry["unit_root_q"])
        moving_barrier_q = int(barrier["moving_endpoint_barrier_q"])
        endpoint_slack = int(endpoint["endpoint_slack"])
        rows.append(
            {
                "packet_id": packet_id,
                "atom_key": endpoint["atom_key"],
                "transition": pivot["transition"],
                "m": int(endpoint["m"]),
                "P": P,
                "q_before_bridge": q,
                "g": g,
                "r": r,
                "bridge_root_q": bridge_root_q,
                "unit_root_q": unit_root_q,
                "moving_endpoint_barrier_q": moving_barrier_q,
                "shared_pivot_q": shared_pivot_q,
                "endpoint_slack": endpoint_slack,
                "endpoint_slack_formula": endpoint_slack_formula,
                "bridge_from_endpoint_formula": bridge_from_endpoint,
                "barrier_from_endpoint_formula": barrier_from_endpoint,
                "barrier_minus_bridge": moving_barrier_q - bridge_root_q,
                "slack_identity_closed": endpoint_slack == endpoint_slack_formula,
                "bridge_formula_closed": bridge_root_q == bridge_from_endpoint,
                "barrier_formula_closed": moving_barrier_q == barrier_from_endpoint,
                "slack_as_barrier_minus_bridge_closed": endpoint_slack == moving_barrier_q - bridge_root_q,
                "bridge_to_pivot_gap_sum": int(pivot["bridge_to_pivot_gap_sum"]),
                "pivot_to_barrier_gap_sum": int(pivot["pivot_to_barrier_gap_sum"]),
                "pivot_gap_sum_total": int(pivot["pivot_gap_sum_total"]),
                "pivot_gap_sum_equals_slack": bool(pivot["endpoint_slack_equals_pivot_gap_sum"]),
                "bridge_is_shared_pivot": bridge_root_q == shared_pivot_q,
                "unit_is_shared_pivot": unit_root_q == shared_pivot_q,
                "barrier_is_shared_pivot": moving_barrier_q == shared_pivot_q,
                "pivot_enclosure_closed": bool(pivot["pivot_enclosure_closed"]),
            }
        )
    return rows


def hinge_summary(rows: list[dict[str, Any]], q_spine_nodes: list[int], shared_pivot_q: int) -> dict[str, Any]:
    """提炼连续两包 shared-pivot hinge。"""
    ordered = sorted(rows, key=lambda row: row["packet_id"])
    if len(ordered) != 2:
        return {"packet_count": len(ordered), "two_packet_hinge_closed": False}
    first, second = ordered
    return {
        "packet_count": 2,
        "q_spine_nodes": q_spine_nodes,
        "q_spine_gap_vector": [q_spine_nodes[i + 1] - q_spine_nodes[i] for i in range(len(q_spine_nodes) - 1)],
        "shared_pivot_q": shared_pivot_q,
        "first_unit_equals_shared_pivot": first["unit_root_q"] == shared_pivot_q,
        "second_bridge_equals_shared_pivot": second["bridge_root_q"] == shared_pivot_q,
        "second_barrier_equals_shared_pivot": second["moving_endpoint_barrier_q"] == shared_pivot_q,
        "first_barrier_equals_second_unit": first["moving_endpoint_barrier_q"] == second["unit_root_q"],
        "first_slack_is_full_qspine_gap_sum": first["endpoint_slack"] == q_spine_nodes[-1] - q_spine_nodes[0],
        "second_slack_is_exact_contact": second["endpoint_slack"] == 0,
        "two_packet_hinge_closed": (
            first["unit_root_q"] == shared_pivot_q
            and second["bridge_root_q"] == shared_pivot_q
            and second["moving_endpoint_barrier_q"] == shared_pivot_q
            and first["moving_endpoint_barrier_q"] == second["unit_root_q"]
            and first["endpoint_slack"] == q_spine_nodes[-1] - q_spine_nodes[0]
            and second["endpoint_slack"] == 0
        ),
        "hinge_word": (
            f"{first['bridge_root_q']} -> {shared_pivot_q} -> {first['moving_endpoint_barrier_q']}; "
            f"{second['bridge_root_q']} = {shared_pivot_q} = {second['moving_endpoint_barrier_q']}"
        ),
    }


def external_applicability_rows() -> list[dict[str, Any]]:
    """记录外部前沿定理目前能否直接套用。"""
    return [
        {
            "input": "FKMS trace-function bilinear technology",
            "usable_now": False,
            "blocker": "需要从 hinge packets 构造 admissible signed trace family。",
        },
        {
            "input": "Milićević-Qin-Wu / Pascadi Kloosterman bilinear inputs",
            "usable_now": False,
            "blocker": "当前只有有限 q-spine 三分母核，没有 uniform Type-II coefficient factorability。",
        },
        {
            "input": "Wright trilinear Kloosterman fractions",
            "usable_now": False,
            "blocker": "需要三线性变量族和 conductor control；shared pivot 仍是固定有限 hinge。",
        },
        {
            "input": "Runbo Li AP/Harman-sieve refinements",
            "usable_now": False,
            "blocker": "LPF/Phi 分桶仍是无符号粗数计数，尚未给出 prime-extraction signed payload。",
        },
        {
            "input": "finite group orbit / thin group expansion",
            "usable_now": False,
            "blocker": "需要实际 group orbit 与 expansion；目前只有两包 q-spine hinge。",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装 shared-pivot hinge 合同证书。"""
    boundary = load_json(BOUNDARY_REDUCTION_JSON)
    carry = load_json(CARRY_BREAK_JSON)
    qspine = load_json(QSPINE_MICRO_JSON)
    endpoint = load_json(ENDPOINT_SLACK_JSON)
    barrier = load_json(MOVING_BARRIER_JSON)
    index_gap = load_json(INDEX_GAP_JSON)
    pivot = load_json(PIVOT_JSON)
    sibling = load_json(SIBLING_KERNEL_JSON)
    lpf_bucket = load_json(LPF_BUCKET_JSON)
    affine = load_json(AFFINE_PARITY_JSON)

    q_summary = qspine["q_spine_summary"]
    q_spine_nodes = [int(q) for q in q_summary["q_spine_nodes"]]
    shared_pivot_q = int(q_summary["shared_pivot_q"])
    rows = packet_hinge_rows(carry, endpoint, barrier, pivot, shared_pivot_q)
    summary = hinge_summary(rows, q_spine_nodes, shared_pivot_q)

    finite_endpoint_algebra_closed = all(
        row["slack_identity_closed"]
        and row["bridge_formula_closed"]
        and row["barrier_formula_closed"]
        and row["slack_as_barrier_minus_bridge_closed"]
        for row in rows
    )
    finite_gap_payment_closed = all(
        row["pivot_gap_sum_equals_slack"] and row["pivot_enclosure_closed"] for row in rows
    )
    pivot_to_hinge_contract_closed = all(
        [
            boundary.get("boundary_ratio_source_key_law_reduced_to_qspine_pivot") is True,
            pivot.get("bridge_root_qspine_pivot_enclosure_reduction_closed") is True,
            endpoint.get("bridge_root_endpoint_slack_reduction_closed") is True,
            barrier.get("bridge_root_moving_endpoint_barrier_reduction_closed") is True,
            index_gap.get("bridge_root_qspine_index_gap_reduction_closed") is True,
            qspine.get("bridge_root_qspine_microtemplate_closed") is True,
            finite_endpoint_algebra_closed,
            finite_gap_payment_closed,
            summary.get("two_packet_hinge_closed") is True,
        ]
    )

    latest_open_gate = (
        f"BoundaryRatioQSpinePivotReductionClosed AND {SHARED_PIVOT_LAW} "
        f"AND {ENDPOINT_SLACK_LAW} AND {QSPINE_GAP_PAYMENT_LAW} "
        f"AND {SIBLING_KERNEL_LAW} AND {ORIENTATION_LAW} AND "
        f"{MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_bridge_root_shared_pivot_hinge_contract_router",
        "status": "bridge_root_qspine_pivot_reduced_to_shared_pivot_hinge_contract_uniform_laws_open",
        "verified_date": "2026-05-26",
        "previous_boundary_ratio_qspine_pivot_reduction_closed": boundary.get(
            "boundary_ratio_source_key_law_reduced_to_qspine_pivot"
        )
        is True,
        "previous_pivot_enclosure_reduction_closed": pivot.get(
            "bridge_root_qspine_pivot_enclosure_reduction_closed"
        )
        is True,
        "previous_endpoint_slack_reduction_closed": endpoint.get("bridge_root_endpoint_slack_reduction_closed")
        is True,
        "previous_moving_endpoint_barrier_reduction_closed": barrier.get(
            "bridge_root_moving_endpoint_barrier_reduction_closed"
        )
        is True,
        "q_spine_nodes": q_spine_nodes,
        "shared_pivot_q": shared_pivot_q,
        "packet_hinge_rows": rows,
        "two_packet_hinge_summary": summary,
        "finite_endpoint_algebra_closed": finite_endpoint_algebra_closed,
        "finite_gap_payment_closed": finite_gap_payment_closed,
        "bridge_root_qspine_pivot_to_shared_hinge_contract_closed": pivot_to_hinge_contract_closed,
        "bridge_root_shared_pivot_hinge_law_proved": False,
        "bridge_root_endpoint_slack_uniform_nonnegative_law_proved": False,
        "bridge_root_qspine_gap_payment_law_proved": False,
        "terminal_sibling_qspine_payment_law_proved": bool(
            sibling.get("terminal_double_awrap_sibling_qspine_kernel_payment_law_proved")
        ),
        "lpf_bucket_correction_imported": {
            "exact_formula": lpf_bucket.get("exact_formula"),
            "exact_lpf_bucket_identity_closed": bool(lpf_bucket.get("exact_lpf_bucket_identity_closed")),
            "unsigned_lpf_bucket_count_sufficient_for_prime_extraction": bool(
                lpf_bucket.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction")
            ),
        },
        "affine_euler_lpf_normalization_imported": {
            "affine_sieve_bijection_verified_all_samples": bool(
                affine.get("affine_sieve_bijection_verified_all_samples")
            ),
            "euler_product_half_main_error_proved": bool(affine.get("euler_product_half_main_error_proved")),
            "row_column_unconditional_closed": bool(affine.get("row_column_unconditional_closed")),
        },
        "external_frontier_applicability_rows": external_applicability_rows(),
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "next_primary_attack_target": SHARED_PIVOT_LAW,
        "latest_open_gate": latest_open_gate,
        "plain_conclusion": (
            "The finite q-spine pivot enclosure is now a shared-pivot hinge contract. "
            "The algebraic slack identity, moving endpoint barrier, q-spine gap sum, "
            "and two-packet pivot roles all close in the audited ledger.  The proof "
            "still needs uniform shared-pivot, endpoint-slack, q-spine payment, and "
            "signed trace/Type-II interfaces; LPF bucket counts remain unsigned."
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF bridge-root shared-pivot hinge contract 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 总裁定",
        "",
        "```text",
        "previous_boundary_ratio_qspine_pivot_reduction_closed="
        f"{fmt_bool(payload['previous_boundary_ratio_qspine_pivot_reduction_closed'])}",
        "previous_pivot_enclosure_reduction_closed="
        f"{fmt_bool(payload['previous_pivot_enclosure_reduction_closed'])}",
        f"q_spine_nodes={payload['q_spine_nodes']}",
        f"shared_pivot_q={payload['shared_pivot_q']}",
        f"finite_endpoint_algebra_closed={fmt_bool(payload['finite_endpoint_algebra_closed'])}",
        f"finite_gap_payment_closed={fmt_bool(payload['finite_gap_payment_closed'])}",
        "bridge_root_qspine_pivot_to_shared_hinge_contract_closed="
        f"{fmt_bool(payload['bridge_root_qspine_pivot_to_shared_hinge_contract_closed'])}",
        "bridge_root_shared_pivot_hinge_law_proved="
        f"{fmt_bool(payload['bridge_root_shared_pivot_hinge_law_proved'])}",
        "bridge_root_endpoint_slack_uniform_nonnegative_law_proved="
        f"{fmt_bool(payload['bridge_root_endpoint_slack_uniform_nonnegative_law_proved'])}",
        "row_column_unconditional_closed="
        f"{fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "核心恒等式：",
        "",
        "```text",
        "endpoint_slack = moving_barrier_q - bridge_root_q = P - q - g*(1+r)",
        "packet1.unit_root = packet2.bridge_root = packet2.barrier = shared_pivot_q",
        "packet1.barrier = packet2.unit_root",
        "```",
        "",
        "## 2. packet hinge rows",
        "",
        "| packet | transition | bridge | unit | barrier | slack | formula slack | bridge->pivot | pivot->barrier | roles |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in payload["packet_hinge_rows"]:
        roles = []
        if row["bridge_is_shared_pivot"]:
            roles.append("bridge=pivot")
        if row["unit_is_shared_pivot"]:
            roles.append("unit=pivot")
        if row["barrier_is_shared_pivot"]:
            roles.append("barrier=pivot")
        lines.append(
            "| {packet} | {transition} | {bridge} | {unit} | {barrier} | {slack} | {formula} | {left_gap} | {right_gap} | {roles} |".format(
                packet=row["packet_id"],
                transition=row["transition"],
                bridge=row["bridge_root_q"],
                unit=row["unit_root_q"],
                barrier=row["moving_endpoint_barrier_q"],
                slack=row["endpoint_slack"],
                formula=row["endpoint_slack_formula"],
                left_gap=row["bridge_to_pivot_gap_sum"],
                right_gap=row["pivot_to_barrier_gap_sum"],
                roles=", ".join(roles) or "-",
            )
        )
    lines.extend(
        [
            "",
            "## 3. two-packet hinge summary",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in payload["two_packet_hinge_summary"].items():
        lines.append(f"| `{key}` | `{cell(value)}` |")
    lines.extend(
        [
            "",
            "## 4. LPF/Phi 修正边界",
            "",
            "```text",
            f"exact_formula={payload['lpf_bucket_correction_imported']['exact_formula']}",
            "exact_lpf_bucket_identity_closed="
            f"{fmt_bool(payload['lpf_bucket_correction_imported']['exact_lpf_bucket_identity_closed'])}",
            "unsigned_lpf_bucket_count_sufficient_for_prime_extraction="
            f"{fmt_bool(payload['lpf_bucket_correction_imported']['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}",
            "affine_sieve_bijection_verified_all_samples="
            f"{fmt_bool(payload['affine_euler_lpf_normalization_imported']['affine_sieve_bijection_verified_all_samples'])}",
            "euler_product_half_main_error_proved="
            f"{fmt_bool(payload['affine_euler_lpf_normalization_imported']['euler_product_half_main_error_proved'])}",
            "```",
            "",
            "## 5. 外部前沿接口状态",
            "",
            "| input | usable now | blocker |",
            "| --- | --- | --- |",
        ]
    )
    for row in payload["external_frontier_applicability_rows"]:
        lines.append(
            f"| {cell(row['input'])} | `{fmt_bool(row['usable_now'])}` | {cell(row['blocker'])} |"
        )
    lines.extend(
        [
            "",
            "## 6. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 7. 依赖哈希",
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
        "bridge_root_qspine_pivot_to_shared_hinge_contract_closed="
        f"{fmt_bool(payload['bridge_root_qspine_pivot_to_shared_hinge_contract_closed'])}"
    )
    print(f"shared_pivot_q={payload['shared_pivot_q']}")
    print(f"next_primary_attack_target={payload['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
