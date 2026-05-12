#!/usr/bin/env python3
"""生成 strict atomic signed payload 来源恒等式证书。

用法示例：
  python3 experiments/prime_matrix_strict_atomic_payload_origin_identity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-atomic-payload-origin-identity-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-atomic-payload-origin-identity-router.json"
OUT_MD = DOCS / "prime-matrix-strict-atomic-payload-origin-identity-router.md"

TARGET = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
NEXT_TARGET = "NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward"
SLOT_VALUE = "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords"
ASSIGNMENT = "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger"
VALUE_MAP = "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula"
ORIGIN_ID = "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json",
    "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json",
    "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-branch-trace-signed-payload-cycle-router.json",
    "prime-matrix-strict-actual-emitter-incidence-entropy-router.json",
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


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不能当成证明。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def origin_fields() -> list[dict[str, str]]:
    """列出 atomic 来源恒等式必须给出的字段。"""
    return [
        {
            "field": "atomic_formal_unit",
            "requirement": "锁定同一 early-zero counterexample formal unit 与 atomic branch trace。",
        },
        {
            "field": "source_tuple_origin",
            "requirement": "给出产生该 basis word/signed coefficient 的 pre-Cauchy source tuple。",
        },
        {
            "field": "basis_word_identity",
            "requirement": "证明 source tuple 正向生成的 primitive basis word 正是 atomic trace 的 word。",
        },
        {
            "field": "signed_coefficient_formula",
            "requirement": "给出 signed coefficient、orientation、local factor、truncation weight 的闭式或有限递推。",
        },
        {
            "field": "prepushforward_equality",
            "requirement": "证明该公式在 Cauchy/Phi/payment 推前前等于 actual alpha/delta 贡献。",
        },
        {
            "field": "nonzero_or_return",
            "requirement": "非零、符号、local factor 与预算成立；失败则命名回流。",
        },
        {
            "field": "no_row_table_or_payment_recovery",
            "requirement": "证明未使用 row-level origin table、payment skeleton、零行覆盖或 terminal certificate 反推。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把 atomic payload constructor 压到非循环来源恒等式。"""
    previous = data["previous"]
    signed_slot = data["signed_slot"]
    slot_value = data["slot_value"]
    assignment = data["assignment"]
    value_map = data["value_map"]
    primitive_origin = data["primitive_origin"]
    row_level = data["row_level"]
    trace_cycle = data["trace_cycle"]
    incidence = data["incidence"]

    assignment_chain = (
        signed_slot.get("next_direct_attack_target") == SLOT_VALUE
        and slot_value.get("next_direct_attack_target") == ASSIGNMENT
        and assignment.get("next_direct_attack_target") == VALUE_MAP
        and value_map.get("next_direct_attack_target") == ORIGIN_ID
    )
    origin_returns_to_row_table = (
        value_map.get("basis_word_signed_coefficient_origin_identity_proved") is False
        and primitive_origin.get("next_direct_attack_target") == ROW_TABLE
        and row_level.get("row_level_clean_core_origin_generation_table_proved") is False
    )

    return [
        row(
            "AtomicPayloadTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 exact atomic trace 的剩余压成 signed payload constructor。",
            TARGET,
        ),
        row(
            "PayloadSlotValueNeedsAssignment",
            slot_value.get("next_direct_attack_target") == ASSIGNMENT,
            True,
            "signed slot value formula 的第一字段是 basis word 到 signed coefficient 的 assignment。",
            ASSIGNMENT,
        ),
        row(
            "AssignmentNeedsValueMap",
            assignment.get("next_direct_attack_target") == VALUE_MAP,
            True,
            "coefficient assignment 的第一字段是 basis word -> signed coefficient value map。",
            VALUE_MAP,
        ),
        row(
            "ValueMapMustBeOriginIdentity",
            value_map.get("value_map_must_be_origin_identity") is True,
            True,
            "value map 不能只是表；必须给 pre-Cauchy source tuple 的来源恒等式。",
            ORIGIN_ID,
        ),
        row(
            "SignedAssignmentChainSynced",
            assignment_chain,
            True,
            "payload 的 signed coefficient 部分已同步到来源恒等式，而不是 UV 或 return tag。",
            NEXT_TARGET,
        ),
        row(
            "ExistingOriginRouteReturnsRowTable",
            origin_returns_to_row_table,
            False,
            "既有来源路线会回到 row-level origin generation table，不能作为非循环 payload 证明。",
            ROW_TABLE,
        ),
        row(
            "BranchTracePayloadCycleImported",
            trace_cycle.get("signed_payload_trace_returns_to_row_level_origin_table") is True,
            True,
            "branch trace signed payload 已被审查为当前语料中的 row-level 回流。",
            NEXT_TARGET,
        ),
        row(
            "NoncircularAtomicOriginIdentityWouldClosePayloadConditionally",
            True,
            True,
            "若新增非循环 atomic 来源恒等式，则 signed coefficient、local factor、same-row identity 和推前前等式可同时获得。",
            f"prove {NEXT_TARGET}",
        ),
        row(
            "ActualEmitterExactUVStillParallel",
            incidence.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "来源恒等式可输出行级 UV，但 bounded multiplicity incidence 仍需独立验收。",
            EXACT_UV,
        ),
        row(
            "NoncircularAtomicOriginIdentityCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交不经 row-level 表的 atomic basis word/signed coefficient 来源恒等式。",
            NEXT_TARGET,
        ),
        row(
            "AtomicSignedPayloadConstructorCurrentCorpusProved",
            False,
            False,
            "没有非循环来源恒等式，payload constructor 仍未证明。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "缺少 atomic 来源恒等式、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 验收门。",
            f"{NEXT_TARGET} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 atomic signed payload 来源恒等式证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json"),
        "signed_slot": load_json("prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json"),
        "slot_value": load_json("prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json"),
        "assignment": load_json("prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json"),
        "value_map": load_json("prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json"),
        "primitive_origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "row_level": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "trace_cycle": load_json("prime-matrix-strict-branch-trace-signed-payload-cycle-router.json"),
        "incidence": load_json("prime-matrix-strict-actual-emitter-incidence-entropy-router.json"),
    }
    rows = build_rows(data)
    strict_basis = f"{NEXT_TARGET} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_atomic_payload_origin_identity_router",
        "status": "atomic_signed_payload_reduced_to_noncircular_origin_identity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "target_input_before_router": TARGET,
        "atomic_payload_origin_identity_router_closed": True,
        "signed_assignment_chain_synced": any(
            item["gate"] == "SignedAssignmentChainSynced" and item["closed"] is True for item in rows
        ),
        "existing_origin_route_returns_row_table": any(
            item["gate"] == "ExistingOriginRouteReturnsRowTable" and item["closed"] is True for item in rows
        ),
        "noncircular_atomic_origin_identity_conditionally_suffices": True,
        "noncircular_atomic_origin_identity_proved": False,
        "atomic_signed_payload_constructor_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": data["incidence"].get(
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "strict_author_side_remaining_basis": strict_basis,
        "origin_fields": origin_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步直接攻击 `AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn`。"
            "payload 的第一生产性字段是 basis word 到 signed coefficient 的赋值；该赋值继续压到 value map，"
            "而 value map 必须是 pre-Cauchy 来源恒等式。既有来源路线会回到 row-level origin table，"
            "因此不能作为非循环证明。真正最窄点压成 "
            "`NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward`："
            "同一 atomic formal unit 内正向给出 source tuple、basis word identity、signed coefficient/local factor 公式、"
            "prepushforward equality 和命名回流，且不调用 row-level 表或 payment/零行反推。"
            "当前材料没有该非循环来源恒等式，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict atomic signed payload 来源恒等式",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_assignment_chain_synced={fmt_bool(result['signed_assignment_chain_synced'])}",
        f"existing_origin_route_returns_row_table={fmt_bool(result['existing_origin_route_returns_row_table'])}",
        (
            "noncircular_atomic_origin_identity_conditionally_suffices="
            f"{fmt_bool(result['noncircular_atomic_origin_identity_conditionally_suffices'])}"
        ),
        f"noncircular_atomic_origin_identity_proved={fmt_bool(result['noncircular_atomic_origin_identity_proved'])}",
        f"atomic_signed_payload_constructor_proved={fmt_bool(result['atomic_signed_payload_constructor_proved'])}",
        (
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved="
            f"{fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 非循环来源恒等式字段",
        "",
        "| field | requirement |",
        "| --- | --- |",
    ]
    for item in result["origin_fields"]:
        lines.append(
            "| `{field}` | {requirement} |".format(
                field=table_cell(item["field"]),
                requirement=table_cell(item["requirement"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 作者侧剩余基",
            "",
            "```text",
            result["strict_author_side_remaining_basis"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    if result["missing_sources"]:
        lines.extend(["", "## 4. 缺失依赖", ""])
        for item in result["missing_sources"]:
            lines.append(f"- `{item}`")
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
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
