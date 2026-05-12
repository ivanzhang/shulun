#!/usr/bin/env python3
"""生成 strict primitive summand signed coefficient 来源恒等式攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_primitive_summand_origin_identity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-primitive-summand-origin-identity-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-primitive-summand-origin-identity-router.json"
OUT_MD = DOCS / "prime-matrix-strict-primitive-summand-origin-identity-router.md"

TARGET = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
NEXT_TARGET = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"

SOURCE_FILES = [
    "prime-matrix-strict-primitive-summand-signed-expression-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-prepushforward-emitter-origin-ledger-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-clean-core-external-lemma-parameter-match-router.json",
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


def row_table_fields() -> list[dict[str, str]]:
    """列出逐行原始生成表字段。"""
    return [
        {"field": "formal_unit_id", "meaning": "锁定同一反例 witness 的 formal unit。"},
        {"field": "source_tuple_hash", "meaning": "锁定 pre-Cauchy source tuple 与 anchor 参数。"},
        {"field": "primitive_row_index", "meaning": "给出 alpha/delta primitive summand 的有限行索引。"},
        {"field": "signed_coefficient", "meaning": "逐行 signed coefficient 的正向公式。"},
        {"field": "sign_local_factor", "meaning": "符号与 local factor 非零证明，失败则命名回流。"},
        {"field": "uv_branch_key", "meaning": "同步输出 exact `(u,v)` 与 branch key。"},
        {"field": "prepushforward_sum_identity", "meaning": "这些行在 Phi/payment 推前前求和等于 actual alpha/delta 系数。"},
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查来源恒等式能否由现有材料闭合。"""
    expression = data["expression"]
    source_law = data["source_law"]
    prepush = data["prepush"]
    source_loop = data["source_loop"]
    formal_record = data["formal_record"]
    source_tuple = data["source_tuple"]
    unsigned = data["unsigned"]
    external = data["external"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    return [
        row(
            "OriginIdentityTargetActive",
            expression.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 primitive summand signed expression 压成 signed coefficient 来源恒等式。",
            TARGET,
        ),
        row(
            "OriginIdentityIsRowLevelOriginGeneration",
            source_law.get("origin_generation_ledger_implication_closed") is True,
            True,
            "若存在 clean-core 原始生成账本，其逐行限制即可给出来源恒等式。",
            NEXT_TARGET,
        ),
        row(
            "PrepushforwardEmitterAlreadyPointsToOriginLedger",
            prepush.get("terminal_gap_after_router") == "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
            True,
            "pre-pushforward emitter origin ledger 已把同一缺口指向原始生成账本。",
            "但未给逐行表。",
        ),
        row(
            "SourceLoopSelfProofCut",
            source_loop.get("source_loop_cut_closed") is True
            and source_loop.get("circular_reverse_derivation_rejected") is True,
            True,
            "origin ledger、formula、emitter、payment 之间的循环来源证明已被切断。",
            "不能由来源环自证逐行生成表。",
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
            "UnsignedSkeletonReadyButNotSignedOrigin",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
            and unsigned.get("alpha_formula_signed_coefficient_lift_proved") is False,
            False,
            "carry-shell、P列锚和 layered-wheel 已给 unsigned row skeleton。",
            "仍需 signed coefficient 来源表。",
        ),
        row(
            "ExternalAndReverseRoutesRejected",
            external.get("external_lemmas_match_constructor_formula") is False
            and reverse.get("pushforward_reverse_uniqueness_rejected") is True
            and zero_nogo.get("zero_row_seed_extraction_blocked") is True,
            True,
            "外部谱、payment 反推和早期零行覆盖都不能生成逐行 signed origin。",
            NEXT_TARGET,
        ),
        row(
            "CleanCoreOriginalGenerationLedgerCurrentCorpusProved",
            source_law.get("clean_core_original_coefficient_generation_ledger_proved") is True,
            False,
            "当前 clean-core 原始生成账本仍未证明。",
            "CleanCoreOriginalCoefficientGenerationLedgerAndReturn。",
        ),
        row(
            "RowLevelOriginTableCurrentCorpusProved",
            False,
            False,
            "当前材料没有逐 actual noncanonical primitive summand 的原始生成表。",
            NEXT_TARGET,
        ),
        row(
            "PrimitiveSummandOriginIdentityCurrentCorpusProved",
            False,
            False,
            "没有逐行原始生成表，signed coefficient 来源恒等式仍未证明。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造来源恒等式攻坚证书。"""
    data = {
        "expression": load_json("prime-matrix-strict-primitive-summand-signed-expression-router.json"),
        "source_law": load_json("prime-matrix-clean-core-precauchy-source-law-atom-router.json"),
        "prepush": load_json("prime-matrix-prepushforward-emitter-origin-ledger-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "formal_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "external": load_json("prime-matrix-clean-core-external-lemma-parameter-match-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_primitive_summand_origin_identity_router",
        "status": "primitive_summand_origin_identity_reduced_to_row_level_origin_generation_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "primitive_summand_origin_identity_router_closed": True,
        "origin_identity_is_row_level_origin_generation": True,
        "source_loop_self_proof_cut": True,
        "unsigned_skeleton_not_signed_origin": True,
        "row_level_clean_core_origin_generation_table_proved": False,
        "primitive_summand_signed_coefficient_origin_identity_proved": False,
        "primitive_summand_signed_weight_expression_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "row_table_fields": row_table_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 等价于提交 `{NEXT_TARGET}`：在同一 formal unit 内列出 actual noncanonical primitive "
            "summand 的逐行原始生成表。已有 unsigned skeleton 只能给几何行，不能给 signed coefficient。"
        ),
        "plain_conclusion": (
            "本步把 signed coefficient 来源恒等式继续压到逐行 clean-core 原始生成表。"
            "如果该表存在，来源恒等式、exact signed weight、constructor row 输出和推前前求和恒等式同时得到；"
            "但当前材料仍只给 formal-unit/source-tuple 容器和 unsigned skeleton，没有 signed coefficient 的逐行来源表。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict primitive summand 来源恒等式路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"primitive_summand_origin_identity_router_closed={fmt_bool(result['primitive_summand_origin_identity_router_closed'])}",
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
        "## 2. 逐行原始生成表字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["row_table_fields"]:
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
