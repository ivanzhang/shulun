#!/usr/bin/env python3
"""审计 dominant sign word 的完整 m-pair 坐标分区。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_dominant_sign_word_mpair_coordinate_partition_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-m-pair-coordinate-partition-audit.json

上一层已经把 dominant m-pair `[769, 773]` 的 20 质量拆成两个端点
坐标 witness。本层把 dominant sign word `--+-+` 的全部 30 质量统一
落到 m-pair/offset/orientation 坐标分区：两个 `[769, 773]` witness 加
一个 `[757, 761]` singleton witness。该层只关闭有限坐标分区账本，不证明
全局 signed collision bound。
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "gap2-gap4-top-two-core-largest-atom-dominant-sign-word-m-pair-coordinate-partition"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"
TARGET_SIGN_WORD = "--+-+"
DOMINANT_M_PAIR = "[769, 773]"
RESIDUAL_SINGLETON_M_PAIR = "[757, 761]"

PREVIOUS_PATH_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-path-audit.json"
)

PREVIOUS_DOMINANT_M_PAIR_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-dominant-m-pair-path-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_PATH_AUDIT,
    PREVIOUS_DOMINANT_M_PAIR_AUDIT,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

STEP_RE = re.compile(r"g=(?P<gap>-?\d+),c=(?P<carry>-?\d+)(?:,A=(?P<sign>[a-z]+))?")


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def edge_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成 edge-mass 表。"""
    return [
        {field: key, "edge_mass": counter[key], "edge_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def parse_path(text: str) -> list[dict[str, Any]]:
    """解析 `g=...,c=...[,A=...]` 路径坐标。"""
    coords: list[dict[str, Any]] = []
    for index, chunk in enumerate(text.split(" -> "), start=1):
        match = STEP_RE.fullmatch(chunk)
        if not match:
            raise ValueError(f"bad coordinate chunk: {chunk}")
        item: dict[str, Any] = {
            "step": index,
            "gap": int(match.group("gap")),
            "carry": int(match.group("carry")),
        }
        if match.group("sign") is not None:
            item["sign"] = match.group("sign")
        coords.append(item)
    return coords


def sign_word_from_coords(coords: list[dict[str, Any]]) -> str:
    """把 signed-child 坐标转为 +/- 词。"""
    letters = []
    for coord in coords:
        sign = coord.get("sign")
        if sign == "positive":
            letters.append("+")
        elif sign == "negative":
            letters.append("-")
        else:
            raise ValueError(f"bad sign coordinate: {coord}")
    return "".join(letters)


def sign_switch_count(sign_word: str) -> int:
    """计算相邻符号切换次数。"""
    return sum(left != right for left, right in zip(sign_word, sign_word[1:]))


def sign_balance(sign_word: str) -> str:
    """输出符号平衡摘要。"""
    return f"plus={sign_word.count('+')},minus={sign_word.count('-')}"


def m_pair_list(label: str) -> list[int]:
    """把 `[a, b]` 形式转成整数 pair。"""
    pair = json.loads(label)
    if not isinstance(pair, list) or len(pair) != 2:
        raise ValueError(f"bad m-pair: {label}")
    return [int(pair[0]), int(pair[1])]


def endpoint_orientation(P: int, pair: list[int]) -> str:
    """判定 m-pair 相对 P 的位置。"""
    if all(m > P for m in pair):
        return "above_P"
    if all(m < P for m in pair):
        return "below_P"
    if any(m == P for m in pair):
        return "touches_P"
    return "straddles_P"


def load_json(path: Path) -> dict[str, Any]:
    """读入 JSON 证书。"""
    return json.loads(path.read_text())


def build_coordinate_row(row: dict[str, Any]) -> dict[str, Any]:
    """把 path witness 行扩展为 m-pair endpoint coordinate witness。"""
    P = int(row["P"])
    pair = m_pair_list(row["m_pair"])
    raw_coords = parse_path(row["raw_base_template"])
    signed_coords = parse_path(row["signed_child"])
    signed_word = sign_word_from_coords(signed_coords)
    offsets = [m - P for m in pair]
    orientation = endpoint_orientation(P, pair)
    pair_id = f"{pair[0]}_{pair[1]}"
    return {
        "witness_id": f"P{P}_packet{row['packet_index']}_q{row['q_prefix_count']}_mpair_{pair_id}",
        "P": P,
        "P_band": row["P_band"],
        "packet_index": row["packet_index"],
        "edge_mass": row["edge_mass"],
        "m_pair": row["m_pair"],
        "m_left": pair[0],
        "m_right": pair[1],
        "m_offsets_from_P": offsets,
        "m_offset_pair": str(offsets),
        "endpoint_orientation": orientation,
        "integer_gap": row["integer_gap"],
        "occurrence_count": row["occurrence_count"],
        "q_prefix_count": row["q_prefix_count"],
        "q_prefix_band": row["q_prefix_band"],
        "m_shell_prime_count": row["m_shell_prime_count"],
        "m_shell_band": row["m_shell_band"],
        "cycle_length": len(raw_coords),
        "raw_base_template": row["raw_base_template"],
        "signed_child": row["signed_child"],
        "raw_coordinate_path": raw_coords,
        "signed_coordinate_path": signed_coords,
        "coordinate_fingerprint": (
            f"P={P}|packet={row['packet_index']}|m_pair={row['m_pair']}|"
            f"offset={offsets}|q={row['q_prefix_count']}|raw={row['raw_base_template']}"
        ),
        "sign_word": signed_word,
        "sign_switch_count": sign_switch_count(signed_word),
        "sign_balance": sign_balance(signed_word),
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 dominant sign-word 的完整 m-pair 坐标分区。"""
    path_payload = load_json(PREVIOUS_PATH_AUDIT)
    dominant_m_pair_payload = load_json(PREVIOUS_DOMINANT_M_PAIR_AUDIT)
    previous = path_payload["finite_audit"]
    rows = [
        row
        for row in previous["path_witness_rows"]
        if row["P"] <= max_prime and row.get("m_pair") in {DOMINANT_M_PAIR, RESIDUAL_SINGLETON_M_PAIR}
    ]
    coordinate_rows = [build_coordinate_row(row) for row in rows]

    total_witness_count = len(coordinate_rows)
    total_edge_mass = sum(row["edge_mass"] for row in coordinate_rows)

    m_pair_edge_mass: Counter[str] = Counter()
    orientation_edge_mass: Counter[str] = Counter()
    q_prefix_band_edge_mass: Counter[str] = Counter()
    q_prefix_count_edge_mass: Counter[int] = Counter()
    m_shell_prime_count_edge_mass: Counter[int] = Counter()
    m_offset_pair_edge_mass: Counter[str] = Counter()
    coordinate_fingerprint_edge_mass: Counter[str] = Counter()
    raw_base_edge_mass: Counter[str] = Counter()
    signed_child_edge_mass: Counter[str] = Counter()

    for row in coordinate_rows:
        mass = row["edge_mass"]
        m_pair_edge_mass[row["m_pair"]] += mass
        orientation_edge_mass[row["endpoint_orientation"]] += mass
        q_prefix_band_edge_mass[row["q_prefix_band"]] += mass
        q_prefix_count_edge_mass[row["q_prefix_count"]] += mass
        m_shell_prime_count_edge_mass[row["m_shell_prime_count"]] += mass
        m_offset_pair_edge_mass[row["m_offset_pair"]] += mass
        coordinate_fingerprint_edge_mass[row["coordinate_fingerprint"]] += mass
        raw_base_edge_mass[row["raw_base_template"]] += mass
        signed_child_edge_mass[row["signed_child"]] += mass

    all_edge_mass_ten = all(row["edge_mass"] == 10 for row in coordinate_rows)
    all_gap4 = all(row["integer_gap"] == 4 for row in coordinate_rows)
    all_occurrence_count_two = all(row["occurrence_count"] == 2 for row in coordinate_rows)
    all_m_shell_le_4 = all(row["m_shell_band"] == "m<=4" for row in coordinate_rows)
    all_cycle_length_five = all(row["cycle_length"] == 5 for row in coordinate_rows)
    all_sign_word_target = all(row["sign_word"] == TARGET_SIGN_WORD for row in coordinate_rows)
    all_switch_count_three = all(row["sign_switch_count"] == 3 for row in coordinate_rows)
    all_sign_balance_fixed = all(row["sign_balance"] == "plus=2,minus=3" for row in coordinate_rows)

    residual_singleton_rows = [
        row for row in coordinate_rows if row["m_pair"] == RESIDUAL_SINGLETON_M_PAIR
    ]
    residual_singleton_coordinate_closed = (
        len(residual_singleton_rows) == 1
        and residual_singleton_rows[0]["P"] == 739
        and residual_singleton_rows[0]["edge_mass"] == 10
        and residual_singleton_rows[0]["endpoint_orientation"] == "above_P"
        and residual_singleton_rows[0]["m_offsets_from_P"] == [18, 22]
        and residual_singleton_rows[0]["q_prefix_band"] == "q>20"
        and residual_singleton_rows[0]["q_prefix_count"] == 28
    )

    ledger_closed = (
        path_payload["dominant_sign_word_path_ledger_closed"]
        and dominant_m_pair_payload["dominant_m_pair_endpoint_coordinate_path_ledger_closed"]
        and previous["path_template_count"] == 3
        and previous["path_edge_mass"] == 30
        and total_witness_count == 3
        and total_edge_mass == 30
        and all_edge_mass_ten
        and all_gap4
        and all_occurrence_count_two
        and all_m_shell_le_4
        and all_cycle_length_five
        and all_sign_word_target
        and all_switch_count_three
        and all_sign_balance_fixed
        and len(m_pair_edge_mass) == 2
        and m_pair_edge_mass[DOMINANT_M_PAIR] == 20
        and m_pair_edge_mass[RESIDUAL_SINGLETON_M_PAIR] == 10
        and orientation_edge_mass["above_P"] == 20
        and orientation_edge_mass["below_P"] == 10
        and q_prefix_band_edge_mass["q<=10"] == 20
        and q_prefix_band_edge_mass["q>20"] == 10
        and len(coordinate_fingerprint_edge_mass) == 3
        and len(raw_base_edge_mass) == 3
        and len(signed_child_edge_mass) == 3
        and residual_singleton_coordinate_closed
    )

    return {
        "max_prime": max_prime,
        "previous_dominant_sign_word_path_ledger_closed": path_payload[
            "dominant_sign_word_path_ledger_closed"
        ],
        "previous_dominant_m_pair_endpoint_coordinate_path_ledger_closed": dominant_m_pair_payload[
            "dominant_m_pair_endpoint_coordinate_path_ledger_closed"
        ],
        "target_sign_word": TARGET_SIGN_WORD,
        "dominant_sign_word_m_pair_coordinate_partition_ledger_closed": ledger_closed,
        "path_template_count": total_witness_count,
        "path_edge_mass": total_edge_mass,
        "all_path_edge_mass_equals_10": all_edge_mass_ten,
        "all_path_integer_gap_equals_4": all_gap4,
        "all_path_occurrence_count_equals_2": all_occurrence_count_two,
        "all_path_m_shell_band_m_le_4": all_m_shell_le_4,
        "all_path_cycle_length_equals_5": all_cycle_length_five,
        "all_path_sign_word_is_target": all_sign_word_target,
        "all_path_sign_switch_count_equals_3": all_switch_count_three,
        "all_path_sign_balance_plus2_minus3": all_sign_balance_fixed,
        "distinct_m_pair_count": len(m_pair_edge_mass),
        "dominant_m_pair": DOMINANT_M_PAIR,
        "dominant_m_pair_edge_mass": m_pair_edge_mass[DOMINANT_M_PAIR],
        "residual_singleton_m_pair": RESIDUAL_SINGLETON_M_PAIR,
        "residual_singleton_m_pair_edge_mass": m_pair_edge_mass[RESIDUAL_SINGLETON_M_PAIR],
        "residual_singleton_coordinate_closed": residual_singleton_coordinate_closed,
        "above_P_edge_mass": orientation_edge_mass["above_P"],
        "below_P_edge_mass": orientation_edge_mass["below_P"],
        "q_prefix_band_q_le_10_edge_mass": q_prefix_band_edge_mass["q<=10"],
        "q_prefix_band_q_gt_20_edge_mass": q_prefix_band_edge_mass["q>20"],
        "distinct_coordinate_fingerprint_count": len(coordinate_fingerprint_edge_mass),
        "distinct_raw_base_template_count": len(raw_base_edge_mass),
        "distinct_signed_child_count": len(signed_child_edge_mass),
        "m_pair_edge_rows": edge_rows(m_pair_edge_mass, total_edge_mass, "m_pair"),
        "orientation_edge_rows": edge_rows(
            orientation_edge_mass, total_edge_mass, "endpoint_orientation"
        ),
        "q_prefix_band_edge_rows": edge_rows(
            q_prefix_band_edge_mass, total_edge_mass, "q_prefix_band"
        ),
        "q_prefix_count_edge_rows": edge_rows(
            q_prefix_count_edge_mass, total_edge_mass, "q_prefix_count"
        ),
        "m_shell_prime_count_edge_rows": edge_rows(
            m_shell_prime_count_edge_mass, total_edge_mass, "m_shell_prime_count"
        ),
        "m_offset_pair_edge_rows": edge_rows(
            m_offset_pair_edge_mass, total_edge_mass, "m_offset_pair"
        ),
        "endpoint_coordinate_witness_rows": sorted(
            coordinate_rows, key=lambda row: (row["P"], row["packet_index"])
        ),
        "dominant_sign_word_endpoint_coordinate_family_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    path_payload = load_json(PREVIOUS_PATH_AUDIT)
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_dominant_sign_word_m_pair_coordinate_partition_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "dominant_sign_word_m_pair_coordinate_partition_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the full dominant sign-word block is the current smallest concrete open block after splitting the dominant m-pair",
        "current_object": {
            "input": "all three path witnesses of dominant sign word --+-+",
            "operation": "split the full 30 edge mass into m-pair/offset/orientation coordinate witnesses",
            "dominant_shape": "three mass-10 coordinate witnesses across two m-pairs and two endpoint orientations",
            "remaining": "prove a uniform endpoint-coordinate family bound or route the three witnesses through PDEC/SAE",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "DominantSignWordPathLedgerImported",
                finite_audit["previous_dominant_sign_word_path_ledger_closed"],
                finite_audit["previous_dominant_sign_word_path_ledger_closed"],
                "The 3-path dominant sign-word ledger is imported.",
                "none for import",
            ),
            gate(
                "DominantMPairEndpointCoordinatePathLedgerImported",
                finite_audit[
                    "previous_dominant_m_pair_endpoint_coordinate_path_ledger_closed"
                ],
                finite_audit[
                    "previous_dominant_m_pair_endpoint_coordinate_path_ledger_closed"
                ],
                "The [769,773] endpoint-coordinate subledger is imported.",
                "none for import",
            ),
            gate(
                "ResidualSingletonMPairCoordinateLedger",
                finite_audit["residual_singleton_coordinate_closed"],
                finite_audit["residual_singleton_coordinate_closed"],
                "The [757,761] singleton witness is fixed at P=739 with offsets [18,22].",
                "none for the finite singleton coordinate",
            ),
            gate(
                "DominantSignWordMPairCoordinatePartitionLedger",
                finite_audit["dominant_sign_word_m_pair_coordinate_partition_ledger_closed"],
                finite_audit["dominant_sign_word_m_pair_coordinate_partition_ledger_closed"],
                "The full --+-+ mass 30 is split into three endpoint-coordinate witnesses.",
                "none for the finite coordinate partition",
            ),
            gate(
                "DominantSignWordEndpointCoordinateUniformFamilyBound",
                False,
                False,
                "Control the three coordinate witnesses as a uniform family.",
                "finite coordinate partition gives exact witnesses but no global theorem",
            ),
        ],
        "external_sources_consulted": path_payload["external_sources_consulted"],
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "the three fixed coordinate witnesses still need completion into a nonlocal trace or bilinear family",
            "prime_gap_inputs": "gap4 adjacency labels remain structural; prime-gap existence theorems do not bound signed template equality",
            "short_interval_prime_inputs": "theta=0.52 does not imply a pointwise half-scale endpoint coordinate estimate",
        },
        "latest_narrowest_mouth": [
            "DominantSignWordEndpointCoordinateUniformFamilyBound(--+-+; m_pair partition)",
            "AND OtherLargestAtomTemplateWitnessFamilyBounds",
            "AND OtherCoreRouteCycleSwitchAtomBounds",
            "AND TopTwoNonCoreSignCycleResidualBound",
            "AND Gap2LowerWingTwinCollisionBound",
            "AND Gap2RightTailTwoSidedTwinResidualCollisionBound",
            "AND Gap4RightTailLeftCollarCousinCollisionBound",
            "AND Gap4UpperWingCousinResidualCollisionBound",
            "AND Gap4LowerWingCousinResidualCollisionBound",
            "AND Gap6SexyAdjacentPairCollisionBound",
            "AND GapGe8AdjacentPairCollisionBound",
            "AND NonAdjacentPrimePairCollisionBound",
            "AND AdjacentPrimeChainCollisionBound",
            "AND MultiPacketDuplicateTransportBound",
            "AND SinglePacketSingleMMultiCycleSuppression",
            "AND RepeatedOccurrenceAggregationOrPDEC",
            "AND CycleOccurrenceProductBoundOrPDEC",
            "AND SinglePSliceEndpointPacketSummationOrPDEC",
            "AND MultiPPureEndpointTraceKloostermanCompletion",
            "AND PureEndpointCarrierPhaseSaving",
            "AND MixedRightTailEndpointRouterNoLoss",
            "AND UnequalMirrorPairResidualPhaseSaving",
            "AND ThinPSupportCarrierSummationWithoutLoss",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "dominant_sign_word_m_pair_coordinate_partition_ledger_closed": finite_audit[
            "dominant_sign_word_m_pair_coordinate_partition_ledger_closed"
        ],
        "dominant_sign_word_endpoint_coordinate_family_bound_proved": False,
        "other_largest_atom_template_witness_family_bounds_proved": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def markdown_table(rows: list[dict[str, Any]], fields: list[str]) -> list[str]:
    """生成 Markdown 表格。"""
    lines = [
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join(["---"] * len(fields)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit_result = payload["finite_audit"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom dominant-sign-word m-pair coordinate partition 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"operation={current['operation']}",
        f"dominant_shape={current['dominant_shape']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. m-pair coordinate partition 审计",
        "",
        "```text",
        f"max_prime={audit_result['max_prime']}",
        f"dominant_sign_word_m_pair_coordinate_partition_ledger_closed={str(audit_result['dominant_sign_word_m_pair_coordinate_partition_ledger_closed']).lower()}",
        f"target_sign_word={audit_result['target_sign_word']}",
        f"path_template_count={audit_result['path_template_count']}",
        f"path_edge_mass={audit_result['path_edge_mass']}",
        f"all_path_edge_mass_equals_10={str(audit_result['all_path_edge_mass_equals_10']).lower()}",
        f"all_path_integer_gap_equals_4={str(audit_result['all_path_integer_gap_equals_4']).lower()}",
        f"all_path_occurrence_count_equals_2={str(audit_result['all_path_occurrence_count_equals_2']).lower()}",
        f"all_path_m_shell_band_m_le_4={str(audit_result['all_path_m_shell_band_m_le_4']).lower()}",
        f"all_path_cycle_length_equals_5={str(audit_result['all_path_cycle_length_equals_5']).lower()}",
        f"all_path_sign_word_is_target={str(audit_result['all_path_sign_word_is_target']).lower()}",
        f"distinct_m_pair_count={audit_result['distinct_m_pair_count']}",
        f"dominant_m_pair={audit_result['dominant_m_pair']}",
        f"dominant_m_pair_edge_mass={audit_result['dominant_m_pair_edge_mass']}",
        f"residual_singleton_m_pair={audit_result['residual_singleton_m_pair']}",
        f"residual_singleton_m_pair_edge_mass={audit_result['residual_singleton_m_pair_edge_mass']}",
        f"residual_singleton_coordinate_closed={str(audit_result['residual_singleton_coordinate_closed']).lower()}",
        f"above_P_edge_mass={audit_result['above_P_edge_mass']}",
        f"below_P_edge_mass={audit_result['below_P_edge_mass']}",
        f"q_prefix_band_q_le_10_edge_mass={audit_result['q_prefix_band_q_le_10_edge_mass']}",
        f"q_prefix_band_q_gt_20_edge_mass={audit_result['q_prefix_band_q_gt_20_edge_mass']}",
        f"distinct_coordinate_fingerprint_count={audit_result['distinct_coordinate_fingerprint_count']}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "coordinate witnesses：",
        "",
        *markdown_table(
            audit_result["endpoint_coordinate_witness_rows"],
            [
                "witness_id",
                "P",
                "P_band",
                "packet_index",
                "edge_mass",
                "m_pair",
                "endpoint_orientation",
                "m_offsets_from_P",
                "q_prefix_count",
                "q_prefix_band",
                "m_shell_prime_count",
                "sign_word",
                "sign_switch_count",
            ],
        ),
        "",
        "subledgers：",
        "",
        *markdown_table(audit_result["m_pair_edge_rows"], ["m_pair", "edge_mass", "edge_ratio"]),
        "",
        *markdown_table(
            audit_result["orientation_edge_rows"],
            ["endpoint_orientation", "edge_mass", "edge_ratio"],
        ),
        "",
        *markdown_table(
            audit_result["q_prefix_band_edge_rows"],
            ["q_prefix_band", "edge_mass", "edge_ratio"],
        ),
        "",
        "## 3. 门控表",
        "",
        *markdown_table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        *markdown_table(payload["external_sources_consulted"], ["key", "url", "role"]),
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：dominant sign word `--+-+` 的 30 质量已经完整落到 3 个 m-pair endpoint-coordinate witness。",
        "该账本仍是有限结构结果，尚未给出全局 signed collision bound。",
        "",
        "## 5. 最新最窄口",
        "",
        "```text",
        *payload["latest_narrowest_mouth"],
        "```",
        "",
        "状态边界：",
        "",
        "```text",
        f"dominant_sign_word_m_pair_coordinate_partition_ledger_closed={str(payload['dominant_sign_word_m_pair_coordinate_partition_ledger_closed']).lower()}",
        f"dominant_sign_word_endpoint_coordinate_family_bound_proved={str(payload['dominant_sign_word_endpoint_coordinate_family_bound_proved']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
    ]
    return "\n".join(lines)


def main() -> None:
    """生成审计证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n")
    OUT_JSON.write_text(text + "\n")
    OUT_MD.write_text(build_markdown(payload).rstrip() + "\n")
    audit_result = payload["finite_audit"]
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(
        "dominant_sign_word_m_pair_coordinate_partition_ledger_closed="
        f"{payload['dominant_sign_word_m_pair_coordinate_partition_ledger_closed']}"
    )
    print(f"path_edge_mass={audit_result['path_edge_mass']}")
    print(f"path_template_count={audit_result['path_template_count']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
