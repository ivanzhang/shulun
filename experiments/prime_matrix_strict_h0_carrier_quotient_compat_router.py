#!/usr/bin/env python3
"""生成 strict h0 载体商兼容路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_h0_carrier_quotient_compat_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-h0-carrier-quotient-compat-router.json

输出：
  docs/monograph/prime-matrix-strict-h0-carrier-quotient-compat-router.json
  docs/monograph/prime-matrix-strict-h0-carrier-quotient-compat-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-h0-carrier-quotient-compat-router.json"
OUT_MD = DOCS / "prime-matrix-strict-h0-carrier-quotient-compat-router.md"

HARDPOINT = "H0CarrierQuotientCompatibilityWithColdPrefixes"
CARRIER_LCM = "CarrierQuotientLCMH0Formula"
COLD_PREFIX_DIVIDES = "ColdPrefixProductDividesCarrierLCMH0Ledger"
PREFIX_QUOTIENT = "PrefixResidualFrequencyEqualsCarrierLCMQuotient"
NO_POSTHOC = "H0NoPostHocEnvelopeDiscipline"
CANONICAL_H0 = "CanonicalH0FromEarlyZeroRowFactorizationIdentity"
H0_EMITTER = "ActualProductDivisorDomainH0EmitterForFormalUnit"
ACTUAL_BLOCK = "ActualColdProductBlockParameterLedgerForP018Table"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-early-zero-factorization-carrier-router.json",
    DOCS / "prime-matrix-strict-canonical-h0-factorization-identity-router.json",
    DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json",
    DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json",
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
        "experiments/prime_matrix_strict_h0_carrier_quotient_compat_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取商兼容需要的导入。"""
    carrier = load_json(DOCS / "prime-matrix-strict-early-zero-factorization-carrier-router.json")
    canonical = load_json(DOCS / "prime-matrix-strict-canonical-h0-factorization-identity-router.json")
    prefix = load_json(DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json")
    fiber = load_json(DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json")
    candidate = load_json(DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json")
    return {
        "compat_target_imported": carrier.get("next_direct_attack_target") == HARDPOINT,
        "carrier_ledger_imported": bool(carrier.get("early_zero_row_factorization_carrier_ledger_present")),
        "canonical_h0_target_imported": canonical.get("next_direct_attack_target")
        == "EarlyZeroRowFactorizationCarrierLedger",
        "prefix_hu_interface_imported": "H_U=h_0/D(U)" in json.dumps(prefix, ensure_ascii=False),
        "product_fiber_h0_interface_imported": "h_0" in json.dumps(fiber, ensure_ascii=False),
        "candidate_divisor_identity_imported": bool(candidate.get("window_divisor_count_envelope_closed")),
    }


def formula_rows() -> list[dict[str, str]]:
    """定义从载体到 h0 的非后验候选公式。"""
    return [
        {
            "name": "carrier_rows",
            "formula": "C(w)={(c,N_c,q_c,m_c): q_c=min prime<=P dividing N_c, m_c=N_c/q_c}",
            "status": "imported_closed",
        },
        {
            "name": "carrier_lcm_h0",
            "formula": "h0^car(w)=lcm_c m_c",
            "status": "closed_definition",
        },
        {
            "name": "h0_hash",
            "formula": "H(source_tuple_hash,'carrier_lcm_h0',sorted carrier row hashes)",
            "status": "closed_definition",
        },
        {
            "name": "no_posthoc_rule",
            "formula": "h0 is computed before cold prefix enumeration; failures route, not enlarge h0",
            "status": "closed_discipline",
        },
        {
            "name": "cold_prefix_compatibility",
            "formula": "for every cold prefix U with product D(U), require D(U)|h0^car",
            "status": "open",
        },
    ]


def obstruction_rows() -> list[dict[str, str]]:
    """列出剩余商兼容阻断。"""
    return [
        {
            "obstruction": "prefix_product_not_yet_tied_to_quotients",
            "meaning": "载体给出每列 m_c；但 cold prefix product D(U) 是否由这些 m_c 的因子组成尚未证明。",
            "next": COLD_PREFIX_DIVIDES,
        },
        {
            "obstruction": "prefix_tree_may_use_downstream_grouping",
            "meaning": "若 U 的定义读取 cold/Rankin 后验分组，就不能直接保证 D(U)|h0^car。",
            "next": COLD_PREFIX_DIVIDES,
        },
        {
            "obstruction": "symbolic_HU_needs_actual_substitution",
            "meaning": "已有 H_U=h0/D(U) 接口必须替换为 h0^car/D(U)，并证明整数性。",
            "next": PREFIX_QUOTIENT,
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
    lcm_formula_closed = flags["compat_target_imported"] and flags["carrier_ledger_imported"]
    return [
        decision_row(
            "H0CarrierQuotientCompatibilityTargetImported",
            True,
            flags["compat_target_imported"],
            "上一层已把最窄点压成 h0 载体与 cold prefix 商化兼容。",
            HARDPOINT,
        ),
        decision_row(
            "CarrierQuotientLCMH0FormulaClosed",
            lcm_formula_closed,
            lcm_formula_closed,
            "用逐列商 m_c 的 lcm 定义非后验候选 h0^car。",
            CARRIER_LCM,
        ),
        decision_row(
            "H0NoPostHocEnvelopeDisciplineClosed",
            lcm_formula_closed,
            lcm_formula_closed,
            "h0^car 在 cold prefix 枚举前由 carrier 固定；失败不能扩大 h0，只能回流。",
            NO_POSTHOC,
        ),
        decision_row(
            "ColdPrefixProductDividesCarrierLCMH0LedgerProved",
            False,
            False,
            "尚未证明每个 cold prefix product D(U) 都除 h0^car。",
            COLD_PREFIX_DIVIDES,
        ),
        decision_row(
            "PrefixResidualFrequencyEqualsCarrierLCMQuotientProved",
            False,
            False,
            "尚未把下游符号 H_U=h0/D(U) 替换为实际整数 h0^car/D(U)。",
            PREFIX_QUOTIENT,
        ),
        decision_row(
            "H0CarrierQuotientCompatibilityWithColdPrefixesProved",
            False,
            False,
            "h0 公式和无后验纪律已推进，但 cold prefix 整除兼容未证。",
            f"{COLD_PREFIX_DIVIDES} AND {PREFIX_QUOTIENT}",
        ),
        decision_row(
            "CanonicalH0FromEarlyZeroRowFactorizationIdentityProved",
            False,
            False,
            "商兼容未闭合，规范 h0 恒等式仍未闭合。",
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
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{COLD_PREFIX_DIVIDES} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 h0 载体商兼容证书。"""
    flags = imported_flags()
    rows = decision_rows(flags)
    lcm_closed = bool(next(item for item in rows if item["gate"] == "CarrierQuotientLCMH0FormulaClosed")["proved"])
    return {
        "certificate_type": "prime_matrix_strict_h0_carrier_quotient_compat_router",
        "status": "carrier_lcm_h0_formula_closed_cold_prefix_divisibility_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{COLD_PREFIX_DIVIDES} AND {PREFIX_QUOTIENT}",
        "next_direct_attack_target": COLD_PREFIX_DIVIDES,
        "parallel_attack_targets": [PREFIX_QUOTIENT, DSTRUCTURE],
        "imported_flags": flags,
        "formula_rows": formula_rows(),
        "obstruction_rows": obstruction_rows(),
        "decision_table": rows,
        "carrier_quotient_lcm_h0_formula_closed": lcm_closed,
        "h0_no_posthoc_envelope_discipline_closed": lcm_closed,
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_proved": False,
        "prefix_residual_frequency_equals_carrier_lcm_quotient_proved": False,
        "h0_carrier_quotient_compatibility_with_cold_prefixes_proved": False,
        "canonical_h0_from_early_zero_row_factorization_identity_proved": False,
        "actual_product_divisor_domain_h0_emitter_for_formal_unit_proved": False,
        "actual_cold_product_block_parameter_ledger_present": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`H0CarrierQuotientCompatibilityWithColdPrefixes` 已推进到一个非后验候选公式："
            "令 `h0^car` 为早期零行载体中全部商 `m_c` 的 lcm。"
            "这个公式由 witness 先验确定，因此关闭了 h0 后验扩大纪律。"
            "但还没有证明每个 cold prefix 的产品 `D(U)` 都除 `h0^car`，"
            "也没有把符号 `H_U=h0/D(U)` 替换成实际整数 `h0^car/D(U)`。"
            "最新最窄点为 `ColdPrefixProductDividesCarrierLCMH0Ledger`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict h0 载体商兼容路由器",
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
        f"carrier_quotient_lcm_h0_formula_closed={fmt_bool(result['carrier_quotient_lcm_h0_formula_closed'])}",
        f"h0_carrier_quotient_compatibility_with_cold_prefixes_proved={fmt_bool(result['h0_carrier_quotient_compatibility_with_cold_prefixes_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 公式与纪律",
        "",
        "| 名称 | 公式 | 状态 |",
        "|---|---|---|",
    ]
    for item in result["formula_rows"]:
        lines.append(f"| `{table_cell(item['name'])}` | {table_cell(item['formula'])} | `{table_cell(item['status'])}` |")
    lines.extend(["", "## 剩余阻断", "", "| 阻断 | 含义 | 下一步 |", "|---|---|---|"])
    for item in result["obstruction_rows"]:
        lines.append(
            f"| `{table_cell(item['obstruction'])}` | {table_cell(item['meaning'])} | `{table_cell(item['next'])}` |"
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
    print(f"carrier_quotient_lcm_h0_formula_closed={fmt_bool(result['carrier_quotient_lcm_h0_formula_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
