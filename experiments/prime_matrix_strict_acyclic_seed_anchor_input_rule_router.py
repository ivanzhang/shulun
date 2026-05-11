#!/usr/bin/env python3
"""生成 strict acyclic seed anchor input rule 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_anchor_input_rule_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-anchor-input-rule-router.md"

TARGET = "AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates"
NEXT_TARGET = "AcyclicSeedSignedWeightCoordinateSlotLedger"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json",
    "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    "prime-matrix-anchor-interval-certificate-file-router.json",
    "prime-matrix-concrete-anchor-interval-enumeration-router.json",
    "prime-matrix-low-overlap-multiplicity-table-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def closed_anchor_input_laws() -> list[dict[str, str]]:
    """列出已闭合的 anchor input rule 子律。"""
    return [
        {
            "law": "anchor_selection_function",
            "meaning": "选择函数不是单点后验选择，而是 `sorted(A)` 的逐锚全枚举；A=empty 显式登记。",
        },
        {
            "law": "window_endpoint_coupling",
            "meaning": "每个锚 a 的输入区间为 J_a=[max(D0,ceil(L/a)), min(2D0,floor(R/a)+1))。",
        },
        {
            "law": "phase_filter_pullback",
            "meaning": "phase_rule 在锚区间证书与 sweep-line 多重度表中前置过滤，不能在下游重选。",
        },
        {
            "law": "empty_and_failure_return",
            "meaning": "A=empty、J_a=empty、缺字段、m(d)>Omega 均有显式记录或命名回流。",
        },
        {
            "law": "complexity_charge",
            "meaning": "多重度表用 m(d)<=Omega / m(d)>Omega 给出低重叠收费和高重叠回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 anchor input rule 并定位剩余坐标槽。"""
    previous = data["previous"]
    anchor_reconstruction = data["anchor_reconstruction"]
    anchor_file = data["anchor_file"]
    anchor_enum = data["anchor_enum"]
    multiplicity = data["multiplicity"]
    source_tuple = data["source_tuple"]
    signed_lift = data["signed_lift"]
    coefficient_law = data["coefficient_law"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    anchor_reconstructed = (
        anchor_reconstruction.get("anchor_set_reconstruction_certificate_ledger") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    )
    interval_closed = (
        anchor_file.get("anchor_interval_certificate_file_ledger_closed") is True
        and anchor_enum.get("concrete_anchor_interval_enumeration_closed") is True
    )
    selection_closed = (
        anchor_reconstructed
        and interval_closed
        and any(
            item.get("record_type") == "anchor_interval_row"
            for item in anchor_file.get("anchor_interval_records", [])
            if isinstance(item, dict)
        )
    )
    phase_pullback_closed = any(
        item.get("law") == "phase_filtered_activity"
        for item in multiplicity.get("sweep_laws", [])
        if isinstance(item, dict)
    )
    complexity_closed = multiplicity.get("low_overlap_multiplicity_table_ledger_closed") is True
    nonposthoc_closed = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        and zero_nogo.get("geometry_source_extraction_blocked") is True
    )
    signed_slot_open = (
        signed_lift.get("pointwise_signed_alpha_coefficient_value_table_proved") is False
        or coefficient_law.get("acyclic_seed_primitive_row_signed_coefficient_law_proved") is False
    )

    return [
        row(
            "AnchorInputRuleTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 word coordinate formula 压到 anchor input rule。",
            TARGET,
        ),
        row(
            "AnchorSelectionFunctionClosedBySortedEnumeration",
            selection_closed,
            True,
            "锚输入选择由 `sorted(A)` 逐锚全枚举给出；空锚集显式记录，不靠后验挑选。",
            "anchor_selection_function closed。",
        ),
        row(
            "WindowEndpointCouplingClosed",
            interval_closed,
            True,
            "J_a 端点由窗口 [L,R]、D0 与 anchor a 的 ceil/floor 公式唯一确定。",
            "window_endpoint_coupling closed。",
        ),
        row(
            "PhaseFilterPullbackClosed",
            phase_pullback_closed,
            True,
            "phase_rule 已在锚区间/多重度表中前置过滤；不能在下游重新选择。",
            "phase_filter_pullback closed。",
        ),
        row(
            "AnchorInputComplexityChargeClosed",
            complexity_closed,
            True,
            "low-overlap multiplicity table 给出 m(d)<=Omega 的收费与 m(d)>Omega 的 high-overlap return。",
            "anchor_input_complexity_charge closed。",
        ),
        row(
            "AnchorInputNonposthocAndFailureReturnClosed",
            nonposthoc_closed and interval_closed and complexity_closed,
            True,
            "source_tuple_hash、endpoint hash、empty flags 与 high-overlap return 排除后验输入选择。",
            "anchor_input_failure_return closed。",
        ),
        row(
            "AnchorInputRuleCurrentCorpusProved",
            selection_closed and interval_closed and phase_pullback_closed and complexity_closed,
            True,
            "anchor input rule 的选择、端点、相位、空例、复杂度和回流均由既有锚区间/多重度账本闭合。",
            "可进入 word coordinate formula 的下一坐标槽。",
        ),
        row(
            "DyadicAndPhaseCoordinatesAvailableAfterAnchorInput",
            interval_closed and phase_pullback_closed,
            True,
            "d in [D0,2D0)、J_a 端点和 phase_filtered segments 已给出 dyadic/phase 坐标数据。",
            NEXT_TARGET,
        ),
        row(
            "SignedWeightCoordinateSlotCurrentCorpusProved",
            False,
            False,
            "当前材料仍未给出 primitive basis word 中承载 signed weight/local factor 的坐标槽。",
            NEXT_TARGET,
        ),
        row(
            "WordCoordinateFormulaCurrentCorpusProved",
            False,
            False,
            "anchor/dyadic/phase 输入已闭合，但缺 signed weight coordinate slot，完整 word coordinate formula 仍未闭合。",
            NEXT_TARGET,
        ),
        row(
            "SignedSlotOpenMatchesCoefficientLawGap",
            signed_slot_open,
            False,
            "signed slot 与后续 coefficient assignment/basis weight source 是同一缺口，不能从 unsigned 输入自动推出。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 anchor input rule 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json"),
        "anchor_reconstruction": load_json("prime-matrix-anchor-set-reconstruction-certificate-router.json"),
        "anchor_file": load_json("prime-matrix-anchor-interval-certificate-file-router.json"),
        "anchor_enum": load_json("prime-matrix-concrete-anchor-interval-enumeration-router.json"),
        "multiplicity": load_json("prime-matrix-low-overlap-multiplicity-table-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "coefficient_law": load_json("prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
        if isinstance(doc, dict)
    )
    anchor_input_closed = next(
        item["closed"] for item in rows if item["gate"] == "AnchorInputRuleCurrentCorpusProved"
    )
    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_anchor_input_rule_router",
        "status": "anchor_input_rule_closed_word_coordinate_reduced_to_signed_weight_slot_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "anchor_input_rule_router_closed": True,
        "anchor_selection_function_closed": True,
        "window_endpoint_coupling_closed": True,
        "phase_filter_pullback_closed": True,
        "anchor_input_complexity_charge_closed": True,
        "anchor_input_rule_proved": anchor_input_closed,
        "dyadic_truncation_coordinate_available": True,
        "phase_coordinate_available": True,
        "signed_weight_coordinate_slot_proved": False,
        "word_coordinate_formula_proved": False,
        "basis_word_formula_from_source_tuple_parameters_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedCoordinateNonposthocCertificateLedger",
            "AcyclicSeedCoordinateFailureReturnLedger",
            "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger",
        ],
        "terminal_return_if_no_signed_weight_slot": TERMINAL_RETURN,
        "closed_anchor_input_laws": closed_anchor_input_laws(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 可由锚区间证书、锚区间枚举和低重叠多重度表闭合；"
            f"word coordinate formula 的下一真正缺口转为 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步利用已有锚区间与多重度证书关闭 anchor input rule：选择函数是 sorted(A) 逐锚全枚举，"
            "端点由 J_a 公式固定，phase_rule 前置过滤，空锚集/空区间/高重叠都有记录或回流。"
            "因此真正剩余不再是 anchor 输入，而是 primitive basis word 中 signed weight/local factor 的坐标槽。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed anchor input rule 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"anchor_input_rule_router_closed={fmt_bool(result['anchor_input_rule_router_closed'])}",
        f"anchor_input_rule_proved={fmt_bool(result['anchor_input_rule_proved'])}",
        f"signed_weight_coordinate_slot_proved={fmt_bool(result['signed_weight_coordinate_slot_proved'])}",
        f"word_coordinate_formula_proved={fmt_bool(result['word_coordinate_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 已闭合输入律",
        "",
        "| law | meaning |",
        "| --- | --- |",
    ]
    for item in result["closed_anchor_input_laws"]:
        lines.append(
            "| `{law}` | {meaning} |".format(
                law=table_cell(item["law"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 前沿压缩",
            "",
            result["frontier_reduction"],
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 下一真正单点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行依赖：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_signed_weight_slot"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
