#!/usr/bin/env python3
"""生成 strict canonical h0 因式分解恒等式路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_canonical_h0_factorization_identity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-canonical-h0-factorization-identity-router.json

输出：
  docs/monograph/prime-matrix-strict-canonical-h0-factorization-identity-router.json
  docs/monograph/prime-matrix-strict-canonical-h0-factorization-identity-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-canonical-h0-factorization-identity-router.json"
OUT_MD = DOCS / "prime-matrix-strict-canonical-h0-factorization-identity-router.md"

HARDPOINT = "CanonicalH0FromEarlyZeroRowFactorizationIdentity"
CARRIER = "EarlyZeroRowFactorizationCarrierLedger"
QUOTIENT_COMPAT = "H0CarrierQuotientCompatibilityWithColdPrefixes"
NO_POSTHOC = "H0NoPostHocEnvelopeDiscipline"
H0_COVERAGE = "H0DivisibilityCoverageNoChoiceLedger"
H0_EMITTER = "ActualProductDivisorDomainH0EmitterForFormalUnit"
ACTUAL_BLOCK = "ActualColdProductBlockParameterLedgerForP018Table"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-actual-h0-product-divisor-emitter-router.json",
    DOCS / "prime-matrix-formal-unit-source-record-router.json",
    DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json",
    DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json",
    DOCS / "prime-matrix-strict-iterated-scaled-core-density-router.json",
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
        "experiments/prime_matrix_strict_canonical_h0_factorization_identity_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取 h0 恒等式相关导入。"""
    h0 = load_json(DOCS / "prime-matrix-strict-actual-h0-product-divisor-emitter-router.json")
    formal = load_json(DOCS / "prime-matrix-formal-unit-source-record-router.json")
    prefix = load_json(DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json")
    fiber = load_json(DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json")
    candidate = load_json(DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json")
    scaled = load_json(DOCS / "prime-matrix-strict-iterated-scaled-core-density-router.json")
    return {
        "h0_identity_target_imported": h0.get("next_direct_attack_target") == HARDPOINT,
        "formal_unit_witness_extractor_imported": bool(formal.get("concrete_formal_unit_source_record_closed")),
        "prefix_residual_frequency_interface_imported": "H_U=h_0/D(U)"
        in json.dumps(prefix, ensure_ascii=False),
        "product_fiber_h0_interface_imported": "h_0" in json.dumps(fiber, ensure_ascii=False),
        "candidate_window_divisor_identity_imported": bool(
            candidate.get("window_divisor_count_envelope_closed")
        ),
        "scaled_frequency_symbolic_law_imported": "h_0" in json.dumps(scaled, ensure_ascii=False),
    }


def interface_rows() -> list[dict[str, str]]:
    """列出已有 h0 符号接口与其限制。"""
    return [
        {
            "interface": "prefix_residual_frequency",
            "formula": "H_U=h0/D(U)",
            "usable_part": "若 h0 已存在，则同前缀子分叉共享同一残余频率。",
            "not_provided": "没有说明 h0 如何由早期零行 witness 产生。",
        },
        {
            "interface": "candidate_window_count",
            "formula": "#Cand(B)<=N_{h0}(Y,2Y]",
            "usable_part": "若 h0 已存在，候选数被窗口除数数控制。",
            "not_provided": "没有证明 actual cold 产品都除同一 h0。",
        },
        {
            "interface": "product_fiber_support",
            "formula": "d ranges over products dividing h0",
            "usable_part": "产品纤维商化后只数 d 支撑。",
            "not_provided": "没有正向发射 d|h0 的载体恒等式。",
        },
        {
            "interface": "scaled_frequency_descent",
            "formula": "h_r=h0/prod b_i c_i",
            "usable_part": "若 h0 已固定，固定商型链给出高度下降。",
            "not_provided": "没有给出初始 h0 的 witness 来源。",
        },
    ]


def required_identity_rows() -> list[dict[str, str]]:
    """定义规范 h0 恒等式必须证明的内容。"""
    return [
        {
            "piece": "factorization_carrier",
            "requirement": "从早期零行 witness 的每列覆盖因式/商数据生成同一载体对象 C(w)。",
            "why": "没有载体对象，就没有可定义 h0 的非循环输入。",
        },
        {
            "piece": "carrier_to_h0_formula",
            "requirement": "给出 h0=F(C(w)) 的整数公式，且 F 不读取下游候选集合。",
            "why": "排除用 d|h0 反向定义 h0 的循环。",
        },
        {
            "piece": "prefix_quotient_compatibility",
            "requirement": "每个 cold prefix U 的残余频率确为 h0/D(U)。",
            "why": "把下游 `H_U=h0/D(U)` 符号接口接回 actual witness。",
        },
        {
            "piece": "coverage",
            "requirement": "每个 actual cold product support d 都满足 d|h0。",
            "why": "使窗口除数计数和 Euler product 合法。",
        },
        {
            "piece": "no_posthoc_enlargement",
            "requirement": "若需要扩大 h0 才覆盖 d，则该 d 进入命名回流而不是修改 h0。",
            "why": "防止 Rankin 预算被后验 h0 调参污染。",
        },
    ]


def invalid_identity_candidates() -> list[dict[str, str]]:
    """列出当前语料中不能闭合恒等式的候选。"""
    return [
        {
            "candidate": "symbolic H_U=h0/D(U)",
            "failure": "这是下游兼容接口，不是初始 h0 的定义。",
            "remaining": CARRIER,
        },
        {
            "candidate": "all small-prime primorial",
            "failure": "会回到粗 tau(h0) 失败路线，且不是 actual formal unit 的最小载体。",
            "remaining": NO_POSTHOC,
        },
        {
            "candidate": "lcm of observed cold products",
            "failure": "observed cold products 已经用 d|h0 定义，循环。",
            "remaining": NO_POSTHOC,
        },
        {
            "candidate": "anchor set A / D0,K,Omega",
            "failure": "这些是几何和重叠参数，没有覆盖所有 product support 的除法恒等式。",
            "remaining": H0_COVERAGE,
        },
        {
            "candidate": "diagnostic sample h0",
            "failure": "样本不绑定任意 early-zero witness，也没有同 formal unit 哈希。",
            "remaining": CARRIER,
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
    interfaces_ready = (
        flags["prefix_residual_frequency_interface_imported"]
        and flags["candidate_window_divisor_identity_imported"]
        and flags["product_fiber_h0_interface_imported"]
    )
    return [
        decision_row(
            "CanonicalH0IdentityTargetImported",
            True,
            flags["h0_identity_target_imported"],
            "上一层已把 h0 发射器首缺口压成规范 h0 因式分解恒等式。",
            HARDPOINT,
        ),
        decision_row(
            "DownstreamH0SymbolInterfacesImported",
            True,
            interfaces_ready,
            "H_U=h0/D(U)、窗口除数计数和产品纤维支撑接口可复用。",
            "interfaces ready",
        ),
        decision_row(
            "InterfacesAreNotSourceIdentity",
            True,
            True,
            "这些接口都以 h0 已存在为前提，不能反向证明 h0 来源。",
            CARRIER,
        ),
        decision_row(
            "EarlyZeroRowFactorizationCarrierLedgerPresent",
            False,
            False,
            "当前语料没有把早期零行每列覆盖因式/商数据整理成单一载体 C(w)。",
            CARRIER,
        ),
        decision_row(
            "H0CarrierQuotientCompatibilityWithColdPrefixesProved",
            False,
            False,
            "尚未证明每个 cold prefix 的残余频率确为 h0/D(U)。",
            QUOTIENT_COMPAT,
        ),
        decision_row(
            "H0NoPostHocEnvelopeDisciplineClosed",
            False,
            False,
            "尚未证明不能为覆盖失败行后验扩大 h0。",
            NO_POSTHOC,
        ),
        decision_row(
            "CanonicalH0FromEarlyZeroRowFactorizationIdentityProved",
            False,
            False,
            "缺载体、商兼容和无后验选择纪律，因此规范 h0 恒等式未证。",
            f"{CARRIER} AND {QUOTIENT_COMPAT} AND {NO_POSTHOC}",
        ),
        decision_row(
            "ActualProductDivisorDomainH0EmitterForFormalUnitProved",
            False,
            False,
            "h0 源恒等式未证，h0 发射器不能闭合。",
            H0_EMITTER,
        ),
        decision_row(
            "ActualColdProductBlockParameterLedgerPresent",
            False,
            False,
            "h0 发射器未闭合，实际产品块参数表仍不存在。",
            ACTUAL_BLOCK,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{CARRIER} AND {FAILURE_RETURN} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造规范 h0 恒等式路由证书。"""
    flags = imported_flags()
    rows = decision_rows(flags)
    return {
        "certificate_type": "prime_matrix_strict_canonical_h0_factorization_identity_router",
        "status": "canonical_h0_identity_reduced_to_factorization_carrier_quotient_compat_no_posthoc",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{CARRIER} AND {QUOTIENT_COMPAT} AND {NO_POSTHOC}",
        "next_direct_attack_target": CARRIER,
        "parallel_attack_targets": [QUOTIENT_COMPAT, NO_POSTHOC, FAILURE_RETURN, DSTRUCTURE],
        "imported_flags": flags,
        "h0_symbol_interface_rows": interface_rows(),
        "required_identity_rows": required_identity_rows(),
        "invalid_identity_candidates": invalid_identity_candidates(),
        "decision_table": rows,
        "downstream_h0_symbol_interfaces_imported": bool(
            next(item for item in rows if item["gate"] == "DownstreamH0SymbolInterfacesImported")["proved"]
        ),
        "early_zero_row_factorization_carrier_ledger_present": False,
        "h0_carrier_quotient_compatibility_with_cold_prefixes_proved": False,
        "h0_no_posthoc_envelope_discipline_closed": False,
        "canonical_h0_from_early_zero_row_factorization_identity_proved": False,
        "actual_product_divisor_domain_h0_emitter_for_formal_unit_proved": False,
        "actual_cold_product_block_parameter_ledger_present": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`CanonicalH0FromEarlyZeroRowFactorizationIdentity` 不能由现有 `H_U=h0/D(U)` 等符号接口直接闭合。"
            "这些接口都以 h0 已存在为前提；它们可复用为下游兼容律，却不是 h0 的来源。"
            "真正缺口是把早期零行 witness 的逐列覆盖因式/商数据整理成单一载体，"
            "再证明该载体产生 h0、兼容所有 cold prefix 商化，并排除后验扩大 h0。"
            "最新最窄点为 `EarlyZeroRowFactorizationCarrierLedger`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict canonical h0 因式分解恒等式路由器",
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
        f"canonical_h0_from_early_zero_row_factorization_identity_proved={fmt_bool(result['canonical_h0_from_early_zero_row_factorization_identity_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 已有 h0 符号接口",
        "",
        "| 接口 | 公式 | 可用部分 | 未提供 |",
        "|---|---|---|---|",
    ]
    for item in result["h0_symbol_interface_rows"]:
        lines.append(
            "| `{}` | `{}` | {} | {} |".format(
                table_cell(item["interface"]),
                table_cell(item["formula"]),
                table_cell(item["usable_part"]),
                table_cell(item["not_provided"]),
            )
        )
    lines.extend(["", "## 恒等式必须证明的内容", "", "| 部件 | 要求 | 原因 |", "|---|---|---|"])
    for item in result["required_identity_rows"]:
        lines.append(
            f"| `{table_cell(item['piece'])}` | {table_cell(item['requirement'])} | {table_cell(item['why'])} |"
        )
    lines.extend(["", "## 无效候选", "", "| 候选 | 失败原因 | 剩余 |", "|---|---|---|"])
    for item in result["invalid_identity_candidates"]:
        lines.append(
            f"| `{table_cell(item['candidate'])}` | {table_cell(item['failure'])} | `{table_cell(item['remaining'])}` |"
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
        "canonical_h0_from_early_zero_row_factorization_identity_proved="
        f"{fmt_bool(result['canonical_h0_from_early_zero_row_factorization_identity_proved'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
