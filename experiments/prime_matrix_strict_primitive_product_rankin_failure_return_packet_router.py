#!/usr/bin/env python3
"""生成 strict primitive product Rankin 失败回流包路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_primitive_product_rankin_failure_return_packet_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.json

输出：
  docs/monograph/prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.json
  docs/monograph/prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.json"
OUT_MD = DOCS / "prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.md"

HARDPOINT = "PrimitiveProductRankinFailureReturnPacketLedger"
PACKET_SCHEMA = "PrimitiveProductRankinFailureReturnPacketSchema"
ACTUAL_PACKET_TABLE = "ActualPrimitiveProductRankinFailurePacketPayloadTable"
SIGMA_TABLE = "PerBlockRankinSigmaSelectionTable"
CLEAN_PRIMITIVE = "CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass"
RETURN_ABSORB = "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.json",
    DATA / "primitive-product-rankin-p018-sample-table.json",
    DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
    DOCS / "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    DOCS / "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json",
    DOCS / "prime-matrix-early-band-local-survivor-return-schema-router.json",
    DOCS / "prime-matrix-support-failure-packet-return-dichotomy-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_hash(payload: Any) -> str:
    """对结构化 payload 计算稳定哈希。"""
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_primitive_product_rankin_failure_return_packet_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
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


def imported_flags() -> dict[str, bool]:
    """读取失败回流包账本需要的导入。"""
    pass_return = load_json(DOCS / "prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.json")
    sample = load_json(DATA / "primitive-product-rankin-p018-sample-table.json")
    cold_split = load_json(DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json")
    common_kernel = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    named_return = load_json(DOCS / "prime-matrix-strict-named-return-after-rowfree-sync-router.json")
    carrier_return = load_json(DOCS / "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json")
    local_survivor = load_json(DOCS / "prime-matrix-early-band-local-survivor-return-schema-router.json")
    support_failure = load_json(DOCS / "prime-matrix-support-failure-packet-return-dichotomy-router.json")
    return {
        "failure_return_target_imported": pass_return.get("next_direct_attack_target") == HARDPOINT,
        "p018_pass_return_schema_closed": pass_return.get(
            "no_return_rankin_p018_pass_or_return_schema_closed"
        )
        is True,
        "diagnostic_fail_rows_present": bool(sample.get("sample_fail_rows")),
        "cold_overload_split_closed": cold_split.get("overload_block_structural_split_closed") is True,
        "common_kernel_cycle_closed": common_kernel.get("free_common_kernel_return_cycle_excluded") is True,
        "named_return_alphabet_closed": named_return.get("named_return_alphabet_compression_closed") is True,
        "carrier_return_frontier_closed": carrier_return.get("return_branch_alphabet_frontier_closed") is True,
        "early_local_survivor_schema_closed": local_survivor.get("early_band_local_survivor_return_schema_closed")
        is True,
        "support_failure_alphabet_closed": support_failure.get("support_failure_packet_return_dichotomy_closed")
        is True,
    }


def packet_alphabet_rows() -> list[dict[str, str]]:
    """列出 primitive Rankin 失败允许的回流包字母表。"""
    return [
        {
            "packet_type": "hot_density_return",
            "trigger": "失败块在短乘法窗口或 sibling family 中显示局部密度过载。",
            "route": "TerminalCoreHotDivisorWindowPDECorSAE / DLSShortWindowSAEBoundOrNamedReturn",
            "status": "named_return_open",
        },
        {
            "packet_type": "common_kernel_return",
            "trigger": "失败块共享低乘子核、固定商型、重复 gcd 或兄弟重叠键。",
            "route": "CommonKernelReturnCycleDescentOrPDECLedger",
            "status": "free_cycle_excluded_named_exits_open",
        },
        {
            "packet_type": "pdec_sae_return",
            "trigger": "失败块携带 low-mod spike、相位缺陷、ColumnCRT、point-load 或局部幸存 packet。",
            "route": "PDEC/SAE/ColumnCRT named terminal family",
            "status": "named_return_open",
        },
        {
            "packet_type": "fixed_history_return",
            "trigger": "同 formal unit 下有限历史、商型或 packet 签名持久复现。",
            "route": "FixedTypeHistoryPDECExclusion / persistent terminal family",
            "status": "persistent_terminal_open",
        },
        {
            "packet_type": "carrier_lcm_return",
            "trigger": "no-return guard 被 source-defect、valuation-overflow 或 carrier-lcm 兼容缺陷破坏。",
            "route": "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption",
            "status": "budget_or_persistent_terminal_open",
        },
    ]


def residual_rows() -> list[dict[str, str]]:
    """列出非合法终端残项。"""
    return [
        {
            "residual": "clean_primitive_failure",
            "definition": "五类命名回流均不触发，但 Rankin bound 仍大于 P^0.18。",
            "forced_next": CLEAN_PRIMITIVE,
            "meaning": "它不能作为第六类无名出口；必须证明存在更优 sigma 通过预算，或推出 clean primitive 分散失败不可能。",
        },
        {
            "residual": "actual_payload_missing",
            "definition": "失败行只有诊断样本或 schema，没有 actual source_tuple/block witness。",
            "forced_next": ACTUAL_PACKET_TABLE,
            "meaning": "只能生成 packet stub；不能把诊断样本升级为全体证明。",
        },
    ]


def packet_laws() -> list[dict[str, str]]:
    """给出失败回流包纪律。"""
    return [
        {
            "law": "failed_row_totality",
            "formula": "verdict=return_required -> one named packet or one clean residual witness",
            "meaning": "失败行不能静默留在 primitive dispersion。",
        },
        {
            "law": "packet_hash_stability",
            "formula": "packet_id=H(source_tuple_hash,block_id,sigma,rankin_ratio,packet_type,payload_hash)",
            "meaning": "同一 formal unit 下回流身份稳定，不允许后验换包。",
        },
        {
            "law": "diagnostic_stub_boundary",
            "formula": "diagnostic_only=true -> packet_stub, not actual proof row",
            "meaning": "样表只证明字段必要性，不证明全体失败已命名。",
        },
        {
            "law": "clean_residual_not_terminal",
            "formula": "no named trigger -> CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass",
            "meaning": "无触发的 clean primitive 失败是下一证明原子，不是闭合结论。",
        },
        {
            "law": "counterexample_branch_guard",
            "formula": "Assume EarlyZeroRowWithinP only; empirical absence not used",
            "meaning": "仍在反例链内部推导，不调用真实零行缺席。",
        },
    ]


def diagnostic_packet_stubs() -> list[dict[str, Any]]:
    """把诊断失败行物化为 packet stub，避免把缺包误记为已闭合。"""
    sample = load_json(DATA / "primitive-product-rankin-p018-sample-table.json")
    stubs: list[dict[str, Any]] = []
    for item in sample.get("sample_fail_rows", []):
        ratio = float(item["rankin_bound"]) / float(item["p018_budget"])
        payload = {
            "sample_row_id": item["sample_row_id"],
            "P": item["P"],
            "h0": item["h0"],
            "Y": item["Y"],
            "sigma": item["sigma"],
            "rankin_ratio": ratio,
        }
        stubs.append(
            {
                **payload,
                "diagnostic_only": True,
                "packet_stub_id": stable_hash(payload),
                "rankin_overbudget_ratio": ratio,
                "packet_status": "diagnostic_stub_requires_actual_trigger_payload",
                "current_return_packet_field": item.get("return_packet"),
                "allowed_packet_types": [entry["packet_type"] for entry in packet_alphabet_rows()],
                "residual_if_no_trigger": CLEAN_PRIMITIVE,
            }
        )
    return stubs


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "FailureReturnTargetImported",
            result["failure_return_target_imported"],
            result["failure_return_target_imported"],
            "上一层 no-return P^0.18 pass/return 已把当前点推进到失败回流包账本。",
            HARDPOINT,
        ),
        row(
            "P018PassReturnSchemaImported",
            result["p018_pass_return_schema_closed"],
            result["p018_pass_return_schema_closed"],
            "每个 no-return dyadic 块已经强制二分为 Rankin pass 或 return_required。",
            "NoReturnPrimitiveProductRankinP018PassOrFailureReturnTable",
        ),
        row(
            "ReturnAlphabetForPrimitiveRankinFailureClosed",
            result["return_packet_alphabet_closed"],
            result["return_packet_alphabet_closed"],
            "热窗口、共同核、PDEC/SAE、固定历史与 carrier-lcm 五类回流覆盖所有非 clean primitive 失败触发。",
            PACKET_SCHEMA,
        ),
        row(
            "PacketHashAndNoPosthocDisciplineClosed",
            result["packet_hash_discipline_closed"],
            result["packet_hash_discipline_closed"],
            "失败包必须绑定 source tuple、block、sigma、overbudget ratio 与 payload hash。",
            "canonical packet identity",
        ),
        row(
            "DiagnosticFailRowsMaterializedAsStubs",
            result["diagnostic_failure_packet_stub_ledger_closed"],
            result["diagnostic_failure_packet_stub_ledger_closed"],
            "诊断样表中的失败行已变成 packet stub，说明缺包字段不能忽略。",
            "diagnostic only",
        ),
        row(
            "ActualAllFailRowsHaveNamedPackets",
            False,
            False,
            "尚未给出全体 actual P^0.18 失败行的 payload 与触发分类。",
            ACTUAL_PACKET_TABLE,
        ),
        row(
            "CleanPrimitiveResidualExcludedOrSigmaPass",
            False,
            False,
            "若五类回流均不触发，仍需证明 clean primitive 分散失败会被某个 sigma 压回 P^0.18，或推出矛盾。",
            CLEAN_PRIMITIVE,
        ),
        row(
            "PrimitiveProductRankinFailureReturnPacketLedgerClosed",
            False,
            False,
            "本步关闭 schema/字母表/哈希纪律，但未证明全体实际失败行都已命名或 clean residual 被排除。",
            f"{ACTUAL_PACKET_TABLE} AND {CLEAN_PRIMITIVE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{CLEAN_PRIMITIVE} AND {RETURN_ABSORB} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造失败回流包路由证书。"""
    flags = imported_flags()
    alphabet_closed = all(
        [
            flags["p018_pass_return_schema_closed"],
            flags["cold_overload_split_closed"],
            flags["common_kernel_cycle_closed"],
            flags["named_return_alphabet_closed"],
            flags["carrier_return_frontier_closed"],
            flags["early_local_survivor_schema_closed"],
            flags["support_failure_alphabet_closed"],
        ]
    )
    stubs = diagnostic_packet_stubs()
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_primitive_product_rankin_failure_return_packet_router",
        "status": "primitive_rankin_failure_packet_schema_closed_actual_payload_and_clean_residual_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "return_packet_alphabet_closed": alphabet_closed,
        "packet_hash_discipline_closed": True,
        "diagnostic_failure_packet_stub_ledger_closed": bool(stubs),
        "primitive_product_rankin_failure_return_packet_schema_closed": alphabet_closed,
        "primitive_product_rankin_failure_return_packet_ledger_closed": False,
        "all_actual_rankin_failure_rows_packeted": False,
        "clean_primitive_dispersion_rankin_failure_excluded_or_sigma_pass_proved": False,
        "per_block_rankin_sigma_selection_table_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": (
            f"{ACTUAL_PACKET_TABLE} AND ({SIGMA_TABLE} OR {CLEAN_PRIMITIVE}) AND {RETURN_ABSORB}"
        ),
        "next_direct_attack_target": CLEAN_PRIMITIVE,
        "parallel_attack_targets": [
            ACTUAL_PACKET_TABLE,
            SIGMA_TABLE,
            RETURN_ABSORB,
            SPARSE_BUDGET,
            PERSISTENT_TERMINAL,
            DSTRUCTURE,
        ],
        "packet_alphabet_rows": packet_alphabet_rows(),
        "packet_laws": packet_laws(),
        "residual_rows": residual_rows(),
        "diagnostic_packet_stubs": stubs,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PrimitiveProductRankinFailureReturnPacketLedger` 的当前可闭合部分是回流包字母表、"
            "哈希身份与诊断失败 stub：Rankin 失败块若不是热窗口、共同核、PDEC/SAE、固定历史或 "
            "carrier-lcm return，就不能留下第六类无名出口，只能成为 clean primitive 分散失败残项。"
            "因此本步把硬点压缩为：为 actual 失败行给出 payload，并证明 clean primitive 失败必有更优 "
            "sigma 通过 P^0.18 或导出矛盾。全体实际失败包和行/列无条件闭合仍未完成。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix strict primitive product Rankin 失败回流包路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"primitive_product_rankin_failure_return_packet_schema_closed={fmt_bool(result['primitive_product_rankin_failure_return_packet_schema_closed'])}",
        f"primitive_product_rankin_failure_return_packet_ledger_closed={fmt_bool(result['primitive_product_rankin_failure_return_packet_ledger_closed'])}",
        f"all_actual_rankin_failure_rows_packeted={fmt_bool(result['all_actual_rankin_failure_rows_packeted'])}",
        f"clean_primitive_dispersion_rankin_failure_excluded_or_sigma_pass_proved={fmt_bool(result['clean_primitive_dispersion_rankin_failure_excluded_or_sigma_pass_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 失败回流包字母表",
        "",
        "| packet_type | trigger | route | status |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["packet_alphabet_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['packet_type'])}`",
                    table_cell(item["trigger"]),
                    table_cell(item["route"]),
                    table_cell(item["status"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 非合法终端残项",
            "",
            "| residual | definition | forced_next | meaning |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["residual_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['residual'])}`",
                    table_cell(item["definition"]),
                    table_cell(item["forced_next"]),
                    table_cell(item["meaning"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 回流包纪律",
            "",
            "| law | formula | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["packet_laws"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['law'])}`",
                    table_cell(item["formula"]),
                    table_cell(item["meaning"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 诊断失败 stub",
            "",
            "| sample_row_id | Y | h0 | sigma | rankin_overbudget_ratio | packet_status |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["diagnostic_packet_stubs"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(item["sample_row_id"]),
                    str(item["Y"]),
                    str(item["h0"]),
                    str(item["sigma"]),
                    f"{item['rankin_overbudget_ratio']:.6f}",
                    table_cell(item["packet_status"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
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
            "## 6. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 并行保留：`{ACTUAL_PACKET_TABLE}`、`{SIGMA_TABLE}`、carrier-lcm return、非持久预算、持久终端族与 DStructure/Rankin 独立验收门。",
            "- 边界：本步不声明全体 actual 失败行已 packeted，也不声明行/列命题无条件闭合。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(json.dumps({"status": result["status"], "next": result["next_direct_attack_target"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
