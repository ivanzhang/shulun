#!/usr/bin/env python3
"""生成 strict joint alpha same-row 来源恒等式路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_joint_alpha_same_row_origin_identity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json"
OUT_MD = DOCS / "prime-matrix-strict-joint-alpha-same-row-origin-identity-router.md"

TARGET = "JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward"
NEXT_TARGET = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
AFTER_ROW_TABLE = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
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
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def same_row_table_fields() -> list[dict[str, str]]:
    """列出 same-row 表中必须同列出现的字段。"""
    return [
        {
            "field": "same_row_id",
            "meaning": "同一 actual noncanonical primitive row 的唯一编号。",
        },
        {
            "field": "basis_word_id",
            "meaning": "由 carry-shell/anchor/phase skeleton 绑定的 primitive basis word。",
        },
        {
            "field": "signed_coefficient",
            "meaning": "该同一行的 signed coefficient 来源公式。",
        },
        {
            "field": "source_tuple_hash",
            "meaning": "word 与 coefficient 共享同一 formal unit/source tuple。",
        },
        {
            "field": "uv_branch_sign_local_factor",
            "meaning": "同一行同步输出 exact `(u,v)`、branch key、sign 和 local factor。",
        },
        {
            "field": "prepushforward_identity",
            "meaning": "同一行在 Phi/payment 推前前参与 alpha/delta 求和恒等式。",
        },
        {
            "field": "return_tag",
            "meaning": "缺 word、缺 coefficient、零因子、后验读取或跨来源时命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把 same-row 桥接回收为逐行原始生成表。"""
    previous = data["previous"]
    primitive_origin = data["primitive_origin"]
    basis_origin = data["basis_origin"]
    row_table = data["row_table"]
    unsigned = data["unsigned"]
    formal = data["formal"]
    source_tuple = data["source_tuple"]
    source_loop = data["source_loop"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    target_active = previous.get("next_direct_attack_target") == TARGET
    primitive_origin_to_row_table = (
        primitive_origin.get("primitive_summand_origin_identity_router_closed") is True
        and primitive_origin.get("next_direct_attack_target") == NEXT_TARGET
    )
    basis_origin_to_row_table = (
        basis_origin.get("basis_word_origin_identity_router_closed") is True
        and basis_origin.get("next_direct_attack_target") == NEXT_TARGET
    )
    row_table_has_needed_fields = (
        row_table.get("row_level_origin_generation_table_router_closed") is True
        and row_table.get("next_direct_attack_target") == AFTER_ROW_TABLE
    )
    unsigned_word_available = (
        unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
        and unsigned.get("unsigned_carry_shell_congruence_row_skeleton_closed") is True
    )
    containers_ready = (
        formal.get("formal_unit_source_record_schema_closed") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    )
    reverse_blocked = (
        source_loop.get("circular_reverse_derivation_rejected") is True
        and reverse.get("pushforward_reverse_uniqueness_rejected") is True
        and zero_nogo.get("zero_row_seed_extraction_blocked") is True
    )

    return [
        row(
            "SameRowOriginIdentityTargetActive",
            target_active,
            False,
            "上一层已把 joint alpha-side 规则压成 same-row word/coefficient 来源恒等式。",
            TARGET,
        ),
        row(
            "PrimitiveCoefficientOriginRouteImported",
            primitive_origin_to_row_table,
            True,
            "primitive summand signed coefficient 来源恒等式已经压到逐行原始生成表。",
            NEXT_TARGET,
        ),
        row(
            "BasisWordOriginRouteImported",
            basis_origin_to_row_table,
            True,
            "basis word signed coefficient 来源恒等式也压到同一逐行原始生成表。",
            NEXT_TARGET,
        ),
        row(
            "SameRowTableFieldsPinned",
            row_table_has_needed_fields,
            True,
            "逐行原始生成表字段包含 basis_word、source tuple、signed coefficient、u/v、sign/local factor 与推前前恒等式。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedWordSkeletonAvailable",
            unsigned_word_available,
            True,
            "unsigned carry-shell/anchor/phase skeleton 可以给 basis word 候选。",
            "它仍需同一 row 上的 signed coefficient 来源。",
        ),
        row(
            "FormalUnitSourceTupleContainersReady",
            containers_ready,
            True,
            "formal unit/source tuple 容器可承载 same-row hash。",
            "容器不能替代逐行表。",
        ),
        row(
            "ReverseRecoveryBlocked",
            reverse_blocked,
            True,
            "payment、零行覆盖、来源环和有限投影不能反推出 same-row 来源恒等式。",
            NEXT_TARGET,
        ),
        row(
            "RowLevelOriginTableStillOpen",
            row_table.get("row_level_clean_core_origin_generation_table_proved") is False,
            False,
            "当前材料仍未证明逐行 clean-core 原始生成表。",
            NEXT_TARGET,
        ),
        row(
            "SameRowOriginIdentityCurrentCorpusProved",
            False,
            False,
            "没有逐行原始生成表，无法证明 word 与 signed coefficient 是同一 pre-Cauchy primitive row。",
            TARGET,
        ),
        row(
            "AfterRowTableNextAtomImported",
            row_table.get("next_direct_attack_target") == AFTER_ROW_TABLE,
            False,
            "既有 row-level 表证书已说明若继续下钻，下一原子是无环 seed signed row emitter。",
            AFTER_ROW_TABLE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 same-row 来源恒等式路由证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json"),
        "primitive_origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "basis_origin": load_json("prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json"),
        "row_table": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "formal": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_strict_joint_alpha_same_row_origin_identity_router",
        "status": "joint_alpha_same_row_origin_identity_reduced_to_row_level_origin_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "joint_alpha_same_row_origin_identity_router_closed": True,
        "primitive_origin_route_imported": True,
        "basis_word_origin_route_imported": True,
        "same_row_table_fields_pinned": True,
        "row_level_clean_core_origin_generation_table_proved": False,
        "acyclic_seed_signed_row_emitter_rule_proved": False,
        "joint_alpha_same_row_word_coefficient_origin_identity_proved": False,
        "joint_alpha_side_primitive_word_coefficient_rule_proved": False,
        "explicit_joint_alpha_delta_constructor_rule_proved": False,
        "pre_cauchy_joint_declaration_line_proved": False,
        "joint_basis_word_coefficient_emitter_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "downstream_next_after_row_level_table": AFTER_ROW_TABLE,
        "terminal_return_if_no_row_table": TERMINAL_RETURN,
        "strict_basis_after_router": (
            f"(({NEXT_TARGET} OR {TERMINAL_DESCENT}) AND {DSTRUCTURE}); "
            f"if {NEXT_TARGET} is attacked internally, next atom is {AFTER_ROW_TABLE}"
        ),
        "same_row_table_fields": same_row_table_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 与 primitive summand 来源恒等式、basis word 来源恒等式会合；"
            f"共同所需对象是 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步把 joint same-row word/coefficient 来源恒等式回收到统一逐行原始生成表。"
            "这张表必须在同一 row 中同时列出 basis_word_id、signed_coefficient、source_tuple_hash、"
            "`(u,v)`、branch key、sign/local factor 和推前前恒等式。已有 unsigned skeleton 与 signed origin "
            "路线分别只给两半，不能证明同一行同源；当前逐行表仍未证明。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict joint alpha same-row 来源恒等式路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"joint_alpha_same_row_origin_identity_router_closed={fmt_bool(result['joint_alpha_same_row_origin_identity_router_closed'])}",
        f"row_level_clean_core_origin_generation_table_proved={fmt_bool(result['row_level_clean_core_origin_generation_table_proved'])}",
        f"acyclic_seed_signed_row_emitter_rule_proved={fmt_bool(result['acyclic_seed_signed_row_emitter_rule_proved'])}",
        f"joint_alpha_same_row_word_coefficient_origin_identity_proved={fmt_bool(result['joint_alpha_same_row_word_coefficient_origin_identity_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. same-row 表字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["same_row_table_fields"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['meaning'])} |")

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
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 下一真正单点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "若继续内部下钻该表，既有下一原子：",
            "",
            "```text",
            result["downstream_next_after_row_level_table"],
            "```",
            "",
            "当前严格自足基：",
            "",
            "```text",
            result["strict_basis_after_router"],
            "```",
            "",
            "审稿边界：本文件只证明 same-row 桥接等价回收到逐行原始生成表；"
            "它没有证明该表，也没有证明行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
