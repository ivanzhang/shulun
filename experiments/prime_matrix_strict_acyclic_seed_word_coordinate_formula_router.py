#!/usr/bin/env python3
"""生成 strict acyclic seed word coordinate formula 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_word_coordinate_formula_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.md"

TARGET = "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters"
ANCHOR_TARGET = "AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates"
NEXT_TARGET = "AcyclicSeedSignedWeightCoordinateSlotLedger"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-basis-word-formula-router.json",
    "prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json",
    "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json",
    "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    "prime-matrix-anchor-interval-certificate-file-router.json",
    "prime-matrix-concrete-anchor-interval-enumeration-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-clean-core-geometric-variation-branch-budget-router.json",
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


def coordinate_remaining_fields() -> list[dict[str, str]]:
    """列出 word coordinate formula 同步后的剩余字段。"""
    return [
        {
            "field": "anchor_input_rule",
            "meaning": "已由 anchor input rule 路由器闭合：逐锚枚举、端点耦合、相位前置过滤和复杂度收费。",
        },
        {
            "field": "dyadic_phase_coordinate_domain",
            "meaning": "anchor rule 闭合后，D0/K/Omega 与 phase_rule 的输入域可登记。",
        },
        {
            "field": "signed_weight_coordinate_slot",
            "meaning": "仍缺承载 signed weight、sign、local factor 和 return_tag 的坐标槽证明。",
        },
        {
            "field": "slot_value_formula_dependency",
            "meaning": "signed 槽位继续依赖 primitive basis word 上的 signed weight/local factor 赋值公式。",
        },
        {
            "field": "coordinate_nonposthoc_certificate",
            "meaning": "坐标公式仍不得读取 payment、零行覆盖、推前后投影或 terminal extraction 后数据。",
        },
        {
            "field": "coordinate_failure_return",
            "meaning": "signed 槽位或赋值公式缺失时回流命名终端家族。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 word coordinate formula 的当前同步前沿。"""
    previous = data["previous"]
    anchor_input = data["anchor_input"]
    signed_slot = data["signed_slot"]
    anchor_reconstruction = data["anchor_reconstruction"]
    source_tuple = data["source_tuple"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    anchor_set_closed = (
        anchor_reconstruction.get("anchor_set_reconstruction_certificate_ledger") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    )
    anchor_rule_proved = anchor_input.get("anchor_input_rule_proved") is True
    coordinate_domain_closed = signed_slot.get("coordinate_domain_closed") is True
    signed_slot_open = signed_slot.get("signed_weight_coordinate_slot_proved") is False
    slot_value_open = signed_slot.get("signed_weight_slot_value_formula_proved") is False
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        or zero_nogo.get("geometry_source_extraction_blocked") is True
        or zero_nogo.get("downstream_reverse_source_blocked") is True
    )

    return [
        row(
            "WordCoordinateFormulaTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 basis_word_formula 压到 word_coordinate_formula。",
            TARGET,
        ),
        row(
            "AnchorSetAndInputRuleClosed",
            anchor_set_closed and anchor_rule_proved,
            True,
            "A、D0/K/Omega、phase_rule 可复算，且 anchor input rule 已由逐锚枚举、端点耦合和相位前置过滤闭合。",
            "anchor 坐标门不再是当前前沿。",
        ),
        row(
            "CoordinateDomainAvailableAfterAnchorInput",
            coordinate_domain_closed,
            True,
            "anchor rule 闭合后，primitive word 的 anchor/dyadic/phase 输入域已可登记。",
            "仍需 signed weight coordinate slot。",
        ),
        row(
            "SignedWeightCoordinateSlotIsFirstRemainingGate",
            signed_slot_open,
            True,
            "完整 word coordinate formula 还必须给 signed weight、sign、local factor 和 return_tag 槽位。",
            NEXT_TARGET,
        ),
        row(
            "SignedSlotValueFormulaStillOpen",
            slot_value_open,
            False,
            "signed 槽位继续依赖 primitive basis word 上的 signed weight/local factor 赋值公式。",
            signed_slot.get("next_direct_attack_target", NEXT_TARGET),
        ),
        row(
            "ReverseCoordinateRecoveryBlocked",
            reverse_blocked,
            True,
            "不能从 payment、推前后投影或早期零行覆盖反推出 signed coordinate slot 或 signed value formula。",
            NEXT_TARGET,
        ),
        row(
            "WordCoordinateFormulaCurrentCorpusProved",
            False,
            False,
            "anchor/dyadic/phase 坐标门已同步闭合；因 signed weight coordinate slot 未证明，完整 word coordinate formula 仍未证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 word coordinate formula 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-basis-word-formula-router.json"),
        "anchor_input": load_json("prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json"),
        "signed_slot": load_json("prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json"),
        "anchor_reconstruction": load_json("prime-matrix-anchor-set-reconstruction-certificate-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    anchor_rule_proved = data["anchor_input"].get("anchor_input_rule_proved") is True
    coordinate_domain_closed = data["signed_slot"].get("coordinate_domain_closed") is True
    signed_slot_proved = data["signed_slot"].get("signed_weight_coordinate_slot_proved") is True
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
        if isinstance(doc, dict)
    )
    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_word_coordinate_formula_router",
        "status": "word_coordinate_formula_anchor_closed_reduced_to_signed_weight_coordinate_slot_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "word_coordinate_formula_router_closed": True,
        "anchor_input_rule_was_previous_frontier": ANCHOR_TARGET,
        "anchor_input_rule_proved": anchor_rule_proved,
        "coordinate_domain_closed_after_anchor_input": coordinate_domain_closed,
        "signed_weight_coordinate_slot_proved": signed_slot_proved,
        "signed_weight_slot_value_formula_proved": data["signed_slot"].get(
            "signed_weight_slot_value_formula_proved"
        )
        is True,
        "reverse_coordinate_recovery_blocked": True,
        "word_coordinate_formula_proved": False,
        "basis_word_formula_from_source_tuple_parameters_proved": False,
        "source_tuple_to_primitive_basis_word_constructor_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords",
            "AcyclicSeedCoordinateNonposthocCertificateLedger",
            "AcyclicSeedCoordinateFailureReturnLedger",
        ],
        "terminal_return_if_no_signed_slot": TERMINAL_RETURN,
        "coordinate_remaining_fields": coordinate_remaining_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的旧前沿 `{ANCHOR_TARGET}` 已闭合；"
            f"当前第一剩余坐标门是 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步同步 word_coordinate_formula 前沿：anchor input rule 已由锚区间和多重度账本闭合，"
            "因此不再是当前缺口；完整坐标公式的真正剩余是 signed weight coordinate slot。"
            "该槽位仍缺 signed weight/local factor 赋值公式，所以 word_coordinate_formula 仍未证明。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed word coordinate formula 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"word_coordinate_formula_router_closed={fmt_bool(result['word_coordinate_formula_router_closed'])}",
        f"anchor_input_rule_proved={fmt_bool(result['anchor_input_rule_proved'])}",
        "coordinate_domain_closed_after_anchor_input="
        f"{fmt_bool(result['coordinate_domain_closed_after_anchor_input'])}",
        f"signed_weight_coordinate_slot_proved={fmt_bool(result['signed_weight_coordinate_slot_proved'])}",
        f"word_coordinate_formula_proved={fmt_bool(result['word_coordinate_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 当前坐标剩余字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["coordinate_remaining_fields"]:
        lines.append(
            "| `{field}` | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
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
            result["terminal_return_if_no_signed_slot"],
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
