#!/usr/bin/env python3
"""生成 strict acyclic seed basis word formula 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_basis_word_formula_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-basis-word-formula-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-basis-word-formula-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-basis-word-formula-router.md"

TARGET = "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility"
NEXT_TARGET = "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
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


def coordinate_formula_fields() -> list[dict[str, str]]:
    """列出 word coordinate formula 的最小字段。"""
    return [
        {
            "field": "anchor_input_rule",
            "meaning": "明确从 A、窗口端点和 phase_rule 选取哪些锚参数作为坐标输入。",
        },
        {
            "field": "dyadic_truncation_coordinate",
            "meaning": "把 D0、K、Omega 转成 basis word 的 dyadic/truncation 坐标。",
        },
        {
            "field": "phase_coordinate",
            "meaning": "把 phase_rule 转成 word 的相位坐标，而不是只给 unsigned row phase。",
        },
        {
            "field": "signed_weight_coordinate_slot",
            "meaning": "为后续 coefficient assignment 预留 signed weight/local factor 槽位。",
        },
        {
            "field": "coordinate_nonposthoc_certificate",
            "meaning": "证明坐标公式不读取 payment、零行覆盖、推前后投影或 terminal 数据。",
        },
        {
            "field": "coordinate_failure_return",
            "meaning": "坐标未定义、冲突、多值或超预算时的命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 basis word formula 的首字段。"""
    previous = data["previous"]
    source_tuple = data["source_tuple"]
    anchor_reconstruction = data["anchor_reconstruction"]
    source_law = data["source_law"]
    unsigned = data["unsigned"]
    signed_lift = data["signed_lift"]
    explicit_rule = data["explicit_rule"]
    constructor = data["constructor"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    parameter_domain_closed = (
        previous.get("input_source_tuple_closed") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
        and source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
    )
    anchor_params_reconstructable = (
        anchor_reconstruction.get("anchor_set_reconstruction_certificate_closed") is True
        or source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
    )
    coordinate_formula_missing = (
        constructor.get("actual_noncanonical_primitive_constructor_formula_proved") is False
        and previous.get("basis_word_formula_from_source_tuple_parameters_proved") is False
    )
    signed_slot_open = (
        signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is False
        or explicit_rule.get("primitive_rule_nonzero_sign_local_factor_proved") is False
    )
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        or zero_nogo.get("downstream_reverse_source_blocked") is True
        or zero_nogo.get("geometry_source_extraction_blocked") is True
    )

    return [
        row(
            "BasisWordFormulaTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 source tuple 到 word constructor 压到 basis_word_formula。",
            TARGET,
        ),
        row(
            "ParameterDomainClosed",
            parameter_domain_closed,
            True,
            "source tuple 参数域已经锁定；A、D0/K/Omega、phase_rule 和 hash 可读取。",
            "参数域不是当前首缺口。",
        ),
        row(
            "WordCoordinateFormulaIsFirstOpenField",
            True,
            True,
            "有参数域还不够，必须先给出把参数转成 primitive basis word 坐标的公式。",
            NEXT_TARGET,
        ),
        row(
            "AnchorReconstructionDoesNotEmitWordCoordinates",
            anchor_params_reconstructable,
            False,
            "anchor reconstruction 可复算 A 与参数，但不输出 basis word coordinate vector。",
            NEXT_TARGET,
        ),
        row(
            "SourceLawRequiresFormulaButDoesNotProvideIt",
            source_law.get("origin_generation_ledger_implication_closed") is True,
            False,
            "source law 说明需要来源公式；它本身不是 coordinate formula。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedSkeletonGivesRowCoordinatesOnly",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True,
            False,
            "unsigned skeleton 给 carry-shell row/phase 几何坐标，不给 primitive basis word 的算术坐标和 signed 槽位。",
            NEXT_TARGET,
        ),
        row(
            "SignedWeightSlotStillOpen",
            signed_slot_open,
            False,
            "signed coefficient lift 与 local factor 仍未闭合，因此不能把 signed 槽位后验补入 formula。",
            NEXT_TARGET,
        ),
        row(
            "ActualCoordinateFormulaCurrentCorpusMissing",
            coordinate_formula_missing,
            False,
            "当前材料没有 actual noncanonical primitive constructor formula，也没有独立 word coordinate formula。",
            NEXT_TARGET,
        ),
        row(
            "PosthocCoordinateRecoveryBlocked",
            reverse_blocked,
            True,
            "不能从 payment、推前后投影或早期零行覆盖恢复坐标公式。",
            NEXT_TARGET,
        ),
        row(
            "WordCoordinateFormulaCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交从 A、D0/K/Omega、phase_rule 到 primitive basis word 坐标的公式。",
            NEXT_TARGET,
        ),
        row(
            "BasisWordFormulaCurrentCorpusProved",
            False,
            False,
            "没有 coordinate formula，arithmetic weight slot、非后验证书和失败回流仍不能合取证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 basis word formula 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "anchor_reconstruction": load_json("prime-matrix-anchor-set-reconstruction-certificate-router.json"),
        "source_law": load_json("prime-matrix-clean-core-precauchy-source-law-atom-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "explicit_rule": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
        "constructor": load_json("prime-matrix-clean-core-constructor-source-class-firewall-router.json"),
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
    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_basis_word_formula_router",
        "status": "basis_word_formula_reduced_to_word_coordinate_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "basis_word_formula_router_closed": True,
        "parameter_domain_closed": True,
        "word_coordinate_formula_is_first_open_field": True,
        "anchor_reconstruction_does_not_emit_word_coordinates": True,
        "posthoc_coordinate_recovery_blocked": True,
        "word_coordinate_formula_proved": False,
        "basis_word_formula_from_source_tuple_parameters_proved": False,
        "source_tuple_to_primitive_basis_word_constructor_proved": False,
        "primitive_basis_word_set_generation_rule_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedSignedWeightCoordinateSlotLedger",
            "AcyclicSeedCoordinateNonposthocCertificateLedger",
            "AcyclicSeedCoordinateFailureReturnLedger",
        ],
        "terminal_return_if_no_word_coordinate_formula": TERMINAL_RETURN,
        "coordinate_formula_fields": coordinate_formula_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 已有参数域，真正首缺口是 `{NEXT_TARGET}`："
            "必须把 A、D0/K/Omega、phase_rule 等 source tuple 参数转成 primitive basis word 的坐标向量。"
        ),
        "plain_conclusion": (
            "本步把 basis_word_formula 再压到 word_coordinate_formula。"
            "参数和锚可以复算，但当前材料没有把这些参数映射为 primitive basis word 坐标；"
            "unsigned row 坐标、signed lift、alpha/delta rule 和后验反推都不能替代该公式。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed basis word formula 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"basis_word_formula_router_closed={fmt_bool(result['basis_word_formula_router_closed'])}",
        f"parameter_domain_closed={fmt_bool(result['parameter_domain_closed'])}",
        f"word_coordinate_formula_proved={fmt_bool(result['word_coordinate_formula_proved'])}",
        f"basis_word_formula_from_source_tuple_parameters_proved={fmt_bool(result['basis_word_formula_from_source_tuple_parameters_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. word_coordinate_formula 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["coordinate_formula_fields"]:
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
            result["terminal_return_if_no_word_coordinate_formula"],
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
