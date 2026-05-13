#!/usr/bin/env python3
"""生成 strict 早期零行因式分解载体账本证书。

用法示例：
  python3 experiments/prime_matrix_strict_early_zero_factorization_carrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-early-zero-factorization-carrier-router.json

输出：
  docs/monograph/prime-matrix-strict-early-zero-factorization-carrier-router.json
  docs/monograph/prime-matrix-strict-early-zero-factorization-carrier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-early-zero-factorization-carrier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-early-zero-factorization-carrier-router.md"

HARDPOINT = "EarlyZeroRowFactorizationCarrierLedger"
QUOTIENT_COMPAT = "H0CarrierQuotientCompatibilityWithColdPrefixes"
NO_POSTHOC = "H0NoPostHocEnvelopeDiscipline"
CANONICAL_H0 = "CanonicalH0FromEarlyZeroRowFactorizationIdentity"
H0_EMITTER = "ActualProductDivisorDomainH0EmitterForFormalUnit"
ACTUAL_BLOCK = "ActualColdProductBlockParameterLedgerForP018Table"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-canonical-h0-factorization-identity-router.json",
    DOCS / "prime-matrix-formal-unit-source-record-router.json",
    DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json",
    DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
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
        "experiments/prime_matrix_strict_early_zero_factorization_carrier_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取载体账本需要的导入。"""
    h0 = load_json(DOCS / "prime-matrix-strict-canonical-h0-factorization-identity-router.json")
    formal = load_json(DOCS / "prime-matrix-formal-unit-source-record-router.json")
    hash_doc = load_json(DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json")
    return {
        "carrier_target_imported": h0.get("next_direct_attack_target") == HARDPOINT,
        "formal_unit_witness_extractor_imported": bool(formal.get("concrete_formal_unit_source_record_closed")),
        "hash_stability_imported": bool(hash_doc.get("canonical_formal_unit_hash_stability_closed")),
    }


def carrier_schema_rows() -> list[dict[str, str]]:
    """定义早期零行因式分解载体字段。"""
    return [
        {
            "field": "witness_id",
            "definition": "H(P,row_index,r/source_tuple_hash)",
            "status": "closed_schema",
        },
        {
            "field": "column",
            "definition": "1<=c<P within the assumed early zero row",
            "status": "closed_schema",
        },
        {
            "field": "N_c",
            "definition": "row value, e.g. xP+c under the fixed row convention",
            "status": "closed_schema",
        },
        {
            "field": "q_c",
            "definition": "least prime q<=P dividing N_c",
            "status": "closed_by_early_zero_assumption",
        },
        {
            "field": "m_c",
            "definition": "N_c/q_c",
            "status": "closed_by_divisibility",
        },
        {
            "field": "carrier_row_hash",
            "definition": "H(witness_id,column,N_c,q_c,m_c)",
            "status": "closed_schema",
        },
    ]


def proof_rows() -> list[dict[str, str]]:
    """列出载体账本闭合的证明步骤。"""
    return [
        {
            "step": "existence",
            "argument": "早期零行假设说明每个列值 N_c 都被某个 P 以内素数覆盖。",
            "status": "closed_under_counterexample_assumption",
        },
        {
            "step": "canonical_selector",
            "argument": "取满足 q|N_c 且 q<=P 的最小素数，消除多因子选择歧义。",
            "status": "closed",
        },
        {
            "step": "quotient_row",
            "argument": "定义 m_c=N_c/q_c；这是整数且由同一列唯一确定。",
            "status": "closed",
        },
        {
            "step": "hash_stability",
            "argument": "carrier_row_hash 继承 source_tuple_hash/formal_unit hash，不后验读取 Rankin 或 cold 产品块。",
            "status": "closed",
        },
        {
            "step": "h0_not_yet_defined",
            "argument": "载体 C(w) 是逐列因式/商表；单一 h0=F(C(w)) 仍需额外公式。",
            "status": "open_next",
        },
    ]


def boundary_rows() -> list[dict[str, str]]:
    """说明载体账本不能越权推出的内容。"""
    return [
        {
            "boundary": "carrier_not_h0",
            "meaning": "C(w) 是逐列 q_c,m_c 表，不是单一产品除数域 h0。",
            "remaining": QUOTIENT_COMPAT,
        },
        {
            "boundary": "least_factor_not_cold_product",
            "meaning": "q_c 是覆盖素标签；cold 产品 d 可能是多步前缀乘子，需证明 d|F(C(w))。",
            "remaining": QUOTIENT_COMPAT,
        },
        {
            "boundary": "no_posthoc_h0",
            "meaning": "不能把所有下游失败 d 再并入 h0；失败必须回流。",
            "remaining": NO_POSTHOC,
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
    carrier_closed = (
        flags["carrier_target_imported"]
        and flags["formal_unit_witness_extractor_imported"]
        and flags["hash_stability_imported"]
    )
    return [
        decision_row(
            "CarrierTargetImported",
            True,
            flags["carrier_target_imported"],
            "上一层已把 h0 源恒等式首缺口压成早期零行因式分解载体账本。",
            HARDPOINT,
        ),
        decision_row(
            "EarlyZeroAssumptionGivesPerColumnSmallPrime",
            True,
            True,
            "在假设反例链内，每列 N_c 都有 P 以内素因子。",
            "counterexample assumption",
        ),
        decision_row(
            "LeastSmallPrimeSelectorCanonical",
            True,
            True,
            "选择最小 q_c 消除多覆盖素因子歧义。",
            "selector closed",
        ),
        decision_row(
            "CarrierRowHashSchemaClosed",
            True,
            flags["hash_stability_imported"],
            "carrier row 继承 formal unit/source tuple hash。",
            "hash closed",
        ),
        decision_row(
            "EarlyZeroRowFactorizationCarrierLedgerPresent",
            carrier_closed,
            carrier_closed,
            "逐列 (N_c,q_c,m_c) 载体账本可由假设早期零行 witness 规范生成。",
            HARDPOINT,
        ),
        decision_row(
            "H0CarrierQuotientCompatibilityWithColdPrefixesProved",
            False,
            False,
            "尚未证明该载体产生的单一 h0 与所有 cold prefix 商化兼容。",
            QUOTIENT_COMPAT,
        ),
        decision_row(
            "H0NoPostHocEnvelopeDisciplineClosed",
            False,
            False,
            "尚未证明后验扩大 h0 的所有情形都回流。",
            NO_POSTHOC,
        ),
        decision_row(
            "CanonicalH0FromEarlyZeroRowFactorizationIdentityProved",
            False,
            False,
            "载体账本闭合，但 h0 公式、商兼容和无后验选择未闭合。",
            CANONICAL_H0,
        ),
        decision_row(
            "ActualProductDivisorDomainH0EmitterForFormalUnitProved",
            False,
            False,
            "规范 h0 恒等式未闭合，h0 发射器仍未闭合。",
            H0_EMITTER,
        ),
        decision_row(
            "ActualColdProductBlockParameterLedgerPresent",
            False,
            False,
            "h0 发射器未闭合，实际产品块参数账本仍不存在。",
            ACTUAL_BLOCK,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到反例链与真实结构链的终端矛盾。",
            f"{QUOTIENT_COMPAT} AND {NO_POSTHOC} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造早期零行因式分解载体证书。"""
    flags = imported_flags()
    rows = decision_rows(flags)
    carrier_closed = bool(
        next(item for item in rows if item["gate"] == "EarlyZeroRowFactorizationCarrierLedgerPresent")[
            "proved"
        ]
    )
    return {
        "certificate_type": "prime_matrix_strict_early_zero_factorization_carrier_router",
        "status": "early_zero_factorization_carrier_closed_h0_quotient_compat_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{QUOTIENT_COMPAT} AND {NO_POSTHOC}",
        "next_direct_attack_target": QUOTIENT_COMPAT,
        "parallel_attack_targets": [NO_POSTHOC, DSTRUCTURE],
        "imported_flags": flags,
        "carrier_schema_rows": carrier_schema_rows(),
        "proof_rows": proof_rows(),
        "boundary_rows": boundary_rows(),
        "decision_table": rows,
        "early_zero_row_factorization_carrier_ledger_present": carrier_closed,
        "h0_carrier_quotient_compatibility_with_cold_prefixes_proved": False,
        "h0_no_posthoc_envelope_discipline_closed": False,
        "canonical_h0_from_early_zero_row_factorization_identity_proved": False,
        "actual_product_divisor_domain_h0_emitter_for_formal_unit_proved": False,
        "actual_cold_product_block_parameter_ledger_present": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`EarlyZeroRowFactorizationCarrierLedger` 可以在假设反例链内闭合："
            "早期零行保证每列 `N_c` 有某个 `q<=P` 素因子，取最小这样的 `q_c`，"
            "并定义 `m_c=N_c/q_c`，即可得到同 formal unit、无选择的逐列因式/商载体。"
            "但这个载体还不是单一 `h0`；仍需证明 carrier 产生的 `h0` 与所有 cold prefix 的 `H_U=h0/D(U)` 商化兼容，"
            "并排除后验扩大 `h0`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 早期零行因式分解载体路由器",
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
        f"early_zero_row_factorization_carrier_ledger_present={fmt_bool(result['early_zero_row_factorization_carrier_ledger_present'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 载体字段",
        "",
        "| 字段 | 定义 | 状态 |",
        "|---|---|---|",
    ]
    for item in result["carrier_schema_rows"]:
        lines.append(
            f"| `{table_cell(item['field'])}` | {table_cell(item['definition'])} | `{table_cell(item['status'])}` |"
        )
    lines.extend(["", "## 证明步骤", "", "| 步骤 | 论证 | 状态 |", "|---|---|---|"])
    for item in result["proof_rows"]:
        lines.append(
            f"| `{table_cell(item['step'])}` | {table_cell(item['argument'])} | `{table_cell(item['status'])}` |"
        )
    lines.extend(["", "## 边界", "", "| 边界 | 含义 | 剩余 |", "|---|---|---|"])
    for item in result["boundary_rows"]:
        lines.append(
            f"| `{table_cell(item['boundary'])}` | {table_cell(item['meaning'])} | `{table_cell(item['remaining'])}` |"
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
        "early_zero_row_factorization_carrier_ledger_present="
        f"{fmt_bool(result['early_zero_row_factorization_carrier_ledger_present'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
