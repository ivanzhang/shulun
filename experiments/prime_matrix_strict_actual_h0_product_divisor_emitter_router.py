#!/usr/bin/env python3
"""生成 strict actual h0 产品除数域发射器路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_actual_h0_product_divisor_emitter_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-actual-h0-product-divisor-emitter-router.json

输出：
  docs/monograph/prime-matrix-strict-actual-h0-product-divisor-emitter-router.json
  docs/monograph/prime-matrix-strict-actual-h0-product-divisor-emitter-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-actual-h0-product-divisor-emitter-router.json"
OUT_MD = DOCS / "prime-matrix-strict-actual-h0-product-divisor-emitter-router.md"

HARDPOINT = "ActualProductDivisorDomainH0EmitterForFormalUnit"
H0_IDENTITY = "CanonicalH0FromEarlyZeroRowFactorizationIdentity"
H0_COVERAGE = "H0DivisibilityCoverageNoChoiceLedger"
H0_HASH = "H0CanonicalHashAndNoPostHocChoiceDiscipline"
BLOCK_ENUMERATOR = "ActualDyadicColdProductBlockEnumeratorForH0"
KERNEL_REGISTER = "PerBlockRegisteredCommonKernelLedger"
ACTUAL_BLOCK = "ActualColdProductBlockParameterLedgerForP018Table"
P018_TABLE = "PrimitiveProductRankinP018InequalityTable"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-actual-cold-product-block-parameter-router.json",
    DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    DOCS / "prime-matrix-formal-unit-source-record-router.json",
    DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json",
    DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json",
    DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_actual_h0_product_divisor_emitter_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取 h0 发射器需要的导入。"""
    actual = load_json(DOCS / "prime-matrix-strict-actual-cold-product-block-parameter-router.json")
    source = load_json(DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json")
    formal = load_json(DOCS / "prime-matrix-formal-unit-source-record-router.json")
    hash_doc = load_json(DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json")
    inventory = load_json(DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json")
    projection = load_json(DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json")
    return {
        "h0_target_imported": actual.get("next_direct_attack_target") == HARDPOINT,
        "source_tuple_schema_imported": bool(source.get("source_tuple_anchor_parameter_schema_closed")),
        "source_tuple_data_imported": bool(source.get("concrete_source_tuple_anchor_parameter_data_closed")),
        "formal_unit_source_record_imported": bool(formal.get("concrete_formal_unit_source_record_closed")),
        "hash_stability_imported": bool(hash_doc.get("canonical_formal_unit_hash_stability_closed")),
        "cold_candidate_rule_imported": bool(inventory.get("cold_product_candidate_set_generator_rule_closed")),
        "primitive_projection_imported": bool(
            projection.get("primitive_product_projection_rule_executable_hash_closed")
        ),
    }


def source_tuple_field_audit() -> list[dict[str, str]]:
    """审查 source tuple 字段是否能发射 h0。"""
    return [
        {
            "field": "formal_unit_id/source_tuple_hash",
            "available": "yes",
            "h0_use": "row identity key",
            "gap": "does not define product divisor domain",
        },
        {
            "field": "P_or_P_range",
            "available": "yes",
            "h0_use": "budget scale",
            "gap": "does not determine divisors d|h0",
        },
        {
            "field": "window_id,L,R",
            "available": "yes",
            "h0_use": "local window geometry",
            "gap": "window endpoints alone do not define multiplicative product carrier",
        },
        {
            "field": "A",
            "available": "yes",
            "h0_use": "anchor set",
            "gap": "no theorem says h0 is lcm/product of A or that every cold d divides it",
        },
        {
            "field": "D0,K,Omega",
            "available": "yes",
            "h0_use": "sieve/overlap parameters",
            "gap": "scale and overlap parameters are not a canonical integer h0",
        },
        {
            "field": "phase_rule",
            "available": "yes",
            "h0_use": "finite phase predicate",
            "gap": "phase predicate cannot be used as Euler product divisor domain",
        },
        {
            "field": "h0",
            "available": "no",
            "h0_use": "required product divisor domain",
            "gap": H0_IDENTITY,
        },
    ]


def invalid_shortcuts() -> list[dict[str, str]]:
    """列出不能作为 h0 发射器证明的捷径。"""
    return [
        {
            "shortcut": "diagnostic_h0_samples",
            "reason": "样本中的 2310/4320/840 只验证投影和 Rankin 公式，未绑定任意 actual formal unit。",
            "return": H0_IDENTITY,
        },
        {
            "shortcut": "choose_h0_as_lcm_of_candidates",
            "reason": "候选集合本身定义为 d|h0；反过来用候选集合定义 h0 是循环。",
            "return": H0_HASH,
        },
        {
            "shortcut": "choose_h0_as_product_of_A",
            "reason": "现有 source tuple 只给 anchor set A，没有证明所有 cold 产品 d 都来自 A 的除数格。",
            "return": H0_COVERAGE,
        },
        {
            "shortcut": "choose_h0_from_D0_K_Omega",
            "reason": "D0/K/Omega 是尺度和重叠参数，不是已证明的产品除数域。",
            "return": H0_IDENTITY,
        },
        {
            "shortcut": "posthoc_enlarge_h0_until_pass",
            "reason": "会改变 Euler product 和 Rankin 预算，是后验选择，破坏同 formal unit 哈希纪律。",
            "return": H0_HASH,
        },
    ]


def required_h0_emitter_schema() -> list[dict[str, str]]:
    """定义 h0 发射器必须包含的最小字段。"""
    return [
        {
            "field": "input_witness",
            "definition": "early-zero witness / formal_unit source record",
            "why_needed": "h0 必须来自假设反例链，而不是真实缺席或诊断样本。",
        },
        {
            "field": "factorization_identity",
            "definition": "canonical formula producing integer h0 from row factorization / quotient data",
            "why_needed": "给出产品除数域的非循环来源。",
        },
        {
            "field": "coverage_law",
            "definition": "every cold product support d in this formal unit satisfies d|h0",
            "why_needed": "让候选集合定义 `{d:d|h0}` 合法。",
        },
        {
            "field": "minimality_or_no_choice_law",
            "definition": "same witness gives same h0; enlargements route to named return",
            "why_needed": "防止后验选择 h0 以调节 Rankin 权重。",
        },
        {
            "field": "h0_hash",
            "definition": "H(source_tuple_hash, factorization_identity_hash, h0)",
            "why_needed": "让下游 block 和 Rankin 表可复算。",
        },
        {
            "field": "failure_return",
            "definition": "if no such h0 exists, route to PDEC/SAE/ColumnCRT/fixed-history",
            "why_needed": "h0 发射失败必须成为终端回流，而不是静默缺口。",
        },
    ]


def decision_row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def decision_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    upstream_ready = (
        flags["h0_target_imported"]
        and flags["source_tuple_data_imported"]
        and flags["formal_unit_source_record_imported"]
        and flags["hash_stability_imported"]
        and flags["cold_candidate_rule_imported"]
        and flags["primitive_projection_imported"]
    )
    return [
        decision_row(
            "H0EmitterTargetImported",
            True,
            flags["h0_target_imported"],
            "上一层已把 actual 参数账本首要缺口压成 h0 产品除数域发射器。",
            HARDPOINT,
        ),
        decision_row(
            "UpstreamFormalUnitContainerReady",
            True,
            upstream_ready,
            "source tuple、formal unit source record、hash、cold candidate rule 与 projection 均可作为输入。",
            "input ready",
        ),
        decision_row(
            "SourceTupleContainsH0Field",
            True,
            False,
            "source tuple 字段审查显示 h0 不在当前 schema 中。",
            H0_IDENTITY,
        ),
        decision_row(
            "CanonicalH0FromEarlyZeroRowFactorizationIdentityProved",
            False,
            False,
            "尚未给出从早期零行 witness/行因式分解到单一 h0 的非循环恒等式。",
            H0_IDENTITY,
        ),
        decision_row(
            "H0DivisibilityCoverageNoChoiceLedgerProved",
            False,
            False,
            "尚未证明所有 cold 产品支撑 d 均除同一 h0，且 h0 不能后验扩大。",
            H0_COVERAGE,
        ),
        decision_row(
            "H0CanonicalHashAndNoPostHocChoiceDisciplineClosed",
            False,
            False,
            "尚未建立 h0_hash 与后验选择排斥纪律。",
            H0_HASH,
        ),
        decision_row(
            "ActualProductDivisorDomainH0EmitterForFormalUnitProved",
            False,
            False,
            "需要 h0 恒等式、覆盖律和无选择哈希纪律三者同时成立。",
            f"{H0_IDENTITY} AND {H0_COVERAGE} AND {H0_HASH}",
        ),
        decision_row(
            "ActualColdProductBlockParameterLedgerPresent",
            False,
            False,
            "h0 发射器未闭合，实际 cold 产品块参数账本仍不存在。",
            ACTUAL_BLOCK,
        ),
        decision_row(
            "PrimitiveProductRankinP018InequalityTablePresent",
            False,
            False,
            "缺 h0 与实际产品块，P^0.18 表仍不能生成。",
            P018_TABLE,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{H0_IDENTITY} AND {FAILURE_RETURN} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 h0 发射器路由证书。"""
    flags = imported_flags()
    rows = decision_rows(flags)
    return {
        "certificate_type": "prime_matrix_strict_actual_h0_product_divisor_emitter_router",
        "status": "h0_emitter_reduced_to_canonical_factorization_identity_coverage_nochoice",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{H0_IDENTITY} AND {H0_COVERAGE} AND {H0_HASH}",
        "next_direct_attack_target": H0_IDENTITY,
        "parallel_attack_targets": [H0_COVERAGE, H0_HASH, FAILURE_RETURN, DSTRUCTURE],
        "imported_flags": flags,
        "source_tuple_field_audit": source_tuple_field_audit(),
        "invalid_shortcuts": invalid_shortcuts(),
        "required_h0_emitter_schema": required_h0_emitter_schema(),
        "decision_table": rows,
        "source_tuple_contains_h0_field": False,
        "canonical_h0_from_early_zero_row_factorization_identity_proved": False,
        "h0_divisibility_coverage_nochoice_ledger_proved": False,
        "h0_canonical_hash_and_no_posthoc_choice_discipline_closed": False,
        "actual_product_divisor_domain_h0_emitter_for_formal_unit_proved": False,
        "actual_cold_product_block_parameter_ledger_present": False,
        "primitive_product_rankin_p018_inequality_table_present": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`ActualProductDivisorDomainH0EmitterForFormalUnit` 已被压到真正源头："
            "必须新增并证明一个从早期零行 witness/同 formal unit 因式分解数据到单一整数 `h0` 的规范恒等式，"
            "同时证明所有 cold 产品支撑 `d` 都满足 `d|h0`，且不能后验扩大 `h0`。"
            "现有 source tuple 字段没有 `h0`，诊断样本和按候选反推 h0 都不能作为证明。"
            "下一最窄点为 `CanonicalH0FromEarlyZeroRowFactorizationIdentity`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict actual h0 产品除数域发射器路由器",
        "",
        "## 结论",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"status={result['status']}",
        f"hardpoint_before={result['hardpoint_before_router']}",
        f"hardpoint_after={result['hardpoint_after_router']}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        f"actual_product_divisor_domain_h0_emitter_for_formal_unit_proved={fmt_bool(result['actual_product_divisor_domain_h0_emitter_for_formal_unit_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## Source Tuple 字段审查",
        "",
        "| 字段 | 是否已有 | h0 相关用途 | 缺口 |",
        "|---|---:|---|---|",
    ]
    for item in result["source_tuple_field_audit"]:
        lines.append(
            "| `{}` | `{}` | {} | `{}` |".format(
                table_cell(item["field"]),
                table_cell(item["available"]),
                table_cell(item["h0_use"]),
                table_cell(item["gap"]),
            )
        )
    lines.extend(["", "## 禁止捷径", "", "| 捷径 | 为什么无效 | 回到 |", "|---|---|---|"])
    for item in result["invalid_shortcuts"]:
        lines.append(
            f"| `{table_cell(item['shortcut'])}` | {table_cell(item['reason'])} | `{table_cell(item['return'])}` |"
        )
    lines.extend(["", "## 发射器最小 schema", "", "| 字段 | 定义 | 作用 |", "|---|---|---|"])
    for item in result["required_h0_emitter_schema"]:
        lines.append(
            f"| `{table_cell(item['field'])}` | {table_cell(item['definition'])} | {table_cell(item['why_needed'])} |"
        )
    lines.extend(
        [
            "",
            "## 判定表",
            "",
            "| Gate | Closed | Proved | Meaning | Remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["decision_table"]:
        lines.append(
            "| `{}` | `{}` | `{}` | {} | `{}` |".format(
                table_cell(item["gate"]),
                fmt_bool(item["closed"]),
                fmt_bool(item["proved"]),
                table_cell(item["meaning"]),
                table_cell(item["remaining"]),
            )
        )
    lines.extend(["", "## 依赖哈希", "", "| 文件 | SHA256 |", "|---|---|"])
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "actual_product_divisor_domain_h0_emitter_for_formal_unit_proved="
        f"{fmt_bool(result['actual_product_divisor_domain_h0_emitter_for_formal_unit_proved'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
