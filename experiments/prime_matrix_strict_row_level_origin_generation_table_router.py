#!/usr/bin/env python3
"""生成 strict 逐行 clean-core 原始生成表攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_row_level_origin_generation_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-row-level-origin-generation-table-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-row-level-origin-generation-table-router.json"
OUT_MD = DOCS / "prime-matrix-strict-row-level-origin-generation-table-router.md"

TARGET = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
NEXT_TARGET = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
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


def emitter_fields() -> list[dict[str, str]]:
    """列出 signed row emitter 规则的必要字段。"""
    return [
        {
            "field": "acyclic_source_seed",
            "meaning": "Cauchy/dispersion 前声明的 actual noncanonical primitive source seed。",
        },
        {
            "field": "row_emitter_map",
            "meaning": "从 seed/source tuple 到有限 alpha/delta primitive rows 的确定性发射映射。",
        },
        {
            "field": "signed_coefficient_law",
            "meaning": "每条 row 的 signed coefficient 公式，含筛权、符号和 branch/local factor。",
        },
        {
            "field": "prepushforward_sum_identity",
            "meaning": "这些 row 在 Phi/payment 推前前求和等于 actual alpha/delta 系数。",
        },
        {
            "field": "uv_key_sync",
            "meaning": "每条 row 同步输出 exact `(u,v)` 和 branch key。",
        },
        {
            "field": "terminal_return_if_missing",
            "meaning": "seed 缺失、row 缺失、零权重、符号冲突或超预算时进入命名终端家族。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查逐行原始生成表的下一精确缺口。"""
    previous = data["previous"]
    source_loop = data["source_loop"]
    zero_nogo = data["zero_nogo"]
    seed_fusion = data["seed_fusion"]
    unsigned = data["unsigned"]
    signed_lift = data["signed_lift"]
    pointwise = data["pointwise"]
    support_seed = data["support_seed"]
    source_table = data["source_table"]
    formal_record = data["formal_record"]
    source_tuple = data["source_tuple"]

    seed_fused_to_terminal = (
        seed_fusion.get("acyclic_pre_cauchy_seed_independent_input_removed") is True
        and seed_fusion.get("acyclic_pre_cauchy_seed_proved") is False
        and seed_fusion.get("terminal_gap_after_router") == TERMINAL_RETURN
    )

    return [
        row(
            "RowLevelOriginTableTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 primitive summand 来源恒等式压到逐行 clean-core 原始生成表。",
            TARGET,
        ),
        row(
            "TableRequiresAcyclicSeedWithEmitter",
            True,
            True,
            "逐行表不是后验枚举；必须由无环 pre-Cauchy seed 自带 signed row emitter 规则产生。",
            NEXT_TARGET,
        ),
        row(
            "SourceLoopCutImported",
            source_loop.get("source_loop_cut_closed") is True
            and source_loop.get("circular_reverse_derivation_rejected") is True,
            True,
            "origin/formula/emitter/payment 等价环不能自证逐行表。",
            NEXT_TARGET,
        ),
        row(
            "ZeroRowCannotSupplySeedOrSignedRows",
            zero_nogo.get("zero_row_seed_extraction_blocked") is True
            and zero_nogo.get("geometry_source_extraction_blocked") is True,
            True,
            "早期零行假设只给 unsigned cover/Phi 数据，不能生成 signed seed 或 signed rows。",
            NEXT_TARGET,
        ),
        row(
            "SeedFusionDoesNotProveTable",
            seed_fused_to_terminal,
            True,
            "全局终局中 seed 已通过存在/不存在二分并入终端门；这不等于提交了逐行生成表。",
            "若继续走 signed-source 表路线，仍需 seed+emitter；若缺失则回流终端家族。",
        ),
        row(
            "FormalUnitAndSourceTupleContainersReady",
            formal_record.get("formal_unit_source_record_schema_closed") is True
            and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True,
            True,
            "formal unit/source tuple/anchor 参数容器可用。",
            "容器不产生 signed coefficient。",
        ),
        row(
            "UnsignedSkeletonReadyButInsufficient",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
            and unsigned.get("alpha_formula_signed_coefficient_lift_proved") is False,
            False,
            "unsigned carry-shell/P列锚/layered-wheel skeleton 已能定位候选几何行。",
            "缺 signed coefficient law。",
        ),
        row(
            "SignedLiftStillPointwiseValueTableOpen",
            signed_lift.get("alpha_signed_coefficient_lift_hardpoint_router_closed") is True
            and signed_lift.get("pointwise_signed_alpha_coefficient_value_table_proved") is False,
            False,
            "signed lift 已压成逐 skeleton row 的 signed value table，但该表未给出。",
            "signed row emitter 必须输出这些值。",
        ),
        row(
            "PointwiseWeightFormulaStillNeedsOriginRows",
            pointwise.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "逐行 signed alpha weight 公式仍缺 primitive summand 推前前表达式。",
            NEXT_TARGET,
        ),
        row(
            "SupportSeedIsNotRowEmitter",
            support_seed.get("elementary_mass_support_lemma_closed") is True
            and support_seed.get("acyclic_pre_cauchy_seed_proved") is False,
            False,
            "actual source-support 路线给出支撑能量形式，但不生成 row emitter。",
            NEXT_TARGET,
        ),
        row(
            "SourceTableRequiresSameRows",
            source_table.get("actual_emitter_source_table_router_closed") is True
            and source_table.get("actual_noncanonical_primitive_emitter_source_table_proved") is False,
            False,
            "actual emitter source table 也需要同一批 primitive rows，不能反过来自证 row table。",
            NEXT_TARGET,
        ),
        row(
            "RowLevelOriginGenerationTableCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交 seed 自带的 signed row emitter 和推前前求和恒等式。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造逐行原始生成表攻坚证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "seed_fusion": load_json("prime-matrix-strict-acyclic-seed-terminal-fusion-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "pointwise": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "support_seed": load_json("prime-matrix-strict-actual-source-support-seed-router.json"),
        "source_table": load_json("prime-matrix-strict-actual-emitter-source-table-router.json"),
        "formal_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_row_level_origin_generation_table_router",
        "status": "row_level_origin_generation_table_reduced_to_acyclic_seed_signed_row_emitter_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "row_level_origin_generation_table_router_closed": True,
        "table_requires_acyclic_seed_with_emitter": True,
        "source_loop_cut_imported": True,
        "zero_row_signed_seed_blocked_imported": True,
        "seed_fusion_not_table_proof": True,
        "acyclic_seed_signed_row_emitter_rule_proved": False,
        "row_level_clean_core_origin_generation_table_proved": False,
        "primitive_summand_signed_coefficient_origin_identity_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "terminal_return_if_no_emitter": TERMINAL_RETURN,
        "emitter_fields": emitter_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 必须由 `{NEXT_TARGET}` 生成。若该 seed/emitter 不能提交，"
            f"按 seed 融合与 no-go 纪律回流 `{TERMINAL_RETURN}`；不能从 unsigned skeleton 或 payment 图反推。"
        ),
        "plain_conclusion": (
            "本步继续攻击逐行 clean-core 原始生成表。结论是：表的真正生成器不是 formal-unit 容器、"
            "不是 unsigned carry-shell skeleton，也不是 source table 名称，而是一个无环 pre-Cauchy actual "
            "noncanonical source seed 自带的 signed row emitter 规则。该规则必须逐行输出 signed coefficient、"
            "sign/local factor、exact `(u,v)`、branch key，并证明推前前求和恒等式。当前材料没有该规则；"
            "若无法提交，则只能按已登记纪律回流 acyclic 终端家族。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 逐行原始生成表路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_level_origin_generation_table_router_closed={fmt_bool(result['row_level_origin_generation_table_router_closed'])}",
        f"acyclic_seed_signed_row_emitter_rule_proved={fmt_bool(result['acyclic_seed_signed_row_emitter_rule_proved'])}",
        f"row_level_clean_core_origin_generation_table_proved={fmt_bool(result['row_level_clean_core_origin_generation_table_proved'])}",
        f"primitive_summand_signed_coefficient_origin_identity_proved={fmt_bool(result['primitive_summand_signed_coefficient_origin_identity_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. signed row emitter 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["emitter_fields"]:
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
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_emitter"],
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
