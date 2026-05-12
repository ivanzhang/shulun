#!/usr/bin/env python3
"""生成 strict 有限 verified-zero 到零点自由尾项桥接路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_finite_verified_zero_tail_transition_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-finite-verified-zero-tail-transition-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-finite-verified-zero-tail-transition-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-finite-verified-zero-tail-transition-router.md"

EXPLICIT_TAIL = MONOGRAPH / "prime-matrix-strict-explicit-zero-free-table-tail-router.json"
LARGE_RH = MONOGRAPH / "prime-matrix-strict-large-finite-rh-verification-router.json"
GENERATOR = MONOGRAPH / "prime-matrix-strict-epsilon-table-generator-audit-router.json"
PSI_TABLE = MONOGRAPH / "prime-matrix-strict-schoenfeld-dusart-psi-table-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [EXPLICIT_TAIL, LARGE_RH, GENERATOR, PSI_TABLE, CLAIM_STATUS]

TARGET = "FiniteVerifiedZerosToZeroFreeTailTransitionLedger"
FINITE_ENDPOINT = "FiniteRHHeightEndpointLedger"
TAIL_START = "ZeroFreeTailStartHeightLedger"
NO_GAP = "FiniteToTailNoGapNoOverlapLedger"
BUDGET = "PsiEpsilonBudgetPartitionLedger"
CONVENTION = "SameExplicitFormulaConventionLedger"
HASH_INTERFACE = "TableGeneratorHashInterfaceLedger"
GOURDON_EXTERNAL = "Gourdon10^13FiniteRHVerificationExternalAcceptedForTableInput"
KADIRI_EXTERNAL = "Kadiri2004ExplicitZeroFreeRegionExternalAcceptedForTableTail"
DUSART_TABLE_EXTERNAL = "DusartSchoenfeldPsiEpsilonTableExternalComputationAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

PSI_EPS_28 = "eps_psi(28)<=0.00002224"
PSI_MIDDLE = "psi(x)<1.00002841x for 8e11<=x<=e^28"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_common_variable_table() -> list[dict[str, Any]]:
    """列出桥接必须共用的变量，而不是让各块各用一套口径。"""
    return [
        {
            "variable": "x_range",
            "required_by": "epsilon table / Dusart P5.1",
            "must_cover": "x>=e^28 high tail and 8e11<=x<=e^28 middle band",
            "current_status": "statement extracted, computation proof open",
        },
        {
            "variable": "finite_zero_height_H",
            "required_by": FINITE_ENDPOINT,
            "must_cover": "verified nontrivial zeros up to the exact height used by the table generator",
            "current_status": "external Gourdon source identified, endpoint-to-table mapping open",
        },
        {
            "variable": "zero_free_region_R_and_t0",
            "required_by": TAIL_START,
            "must_cover": "tail zero-free estimates from the first height where the table tail uses them",
            "current_status": "external Kadiri source identified, table constants and thresholds open",
        },
        {
            "variable": "explicit_formula_kernel",
            "required_by": CONVENTION,
            "must_cover": "same psi/theta formula, truncation, smoothing and prime-power convention",
            "current_status": "not yet matched to the table generator hash",
        },
        {
            "variable": "remainder_budget",
            "required_by": BUDGET,
            "must_cover": f"{PSI_EPS_28} and {PSI_MIDDLE}",
            "current_status": "budget partition open; rough C=1280,C_Z=65536 template is far too weak",
        },
        {
            "variable": "rounding_and_hash",
            "required_by": HASH_INTERFACE,
            "must_cover": "directed rounding, interval propagation and reproducible table output",
            "current_status": "table value extraction closed, reproducible computation hash open",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造有限 verified-zero 到零点自由尾项桥接证书。"""
    explicit_tail = load_json(EXPLICIT_TAIL)
    large_rh = load_json(LARGE_RH)
    generator = load_json(GENERATOR)
    psi_table = load_json(PSI_TABLE)
    active = explicit_tail.get("next_direct_attack_target") == TARGET
    external_pieces_identified = (
        large_rh.get("external_gourdon_conditional_lane_available") is True
        and explicit_tail.get("kadiri_external_source_identified") is True
    )
    table_values_extracted = generator.get("epsilon_table_statement_extraction_closed") is True
    splice_ready = psi_table.get("p51_arithmetic_splice_ready") is True
    common_variables = build_common_variable_table()
    taxonomy_closed = active and external_pieces_identified and table_values_extracted and splice_ready
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            explicit_tail.get("counterexample_assumption_only") is True
            and explicit_tail.get("row_column_unconditional_closed") is False,
            True,
            "本步仍只处理早期零行反例链可调用的解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "FiniteVerifiedZeroTailTransitionGateActive",
            active,
            True,
            "上一证书把下一最窄点设为有限 verified-zero 窗口与零点自由尾项的桥接。",
            TARGET,
        ),
        row(
            "ExternalPiecesIdentifiedButNotAutomaticallyComposed",
            external_pieces_identified,
            True,
            "Gourdon 有限零点与 Kadiri 零点自由区可登记为外部块，但二者不会自动生成 Dusart epsilon 表。",
            f"{TARGET} or {DUSART_TABLE_EXTERNAL}",
        ),
        row(
            "CommonVariableInterfaceTaxonomyClosed",
            taxonomy_closed,
            True,
            "桥接必须共用 x 区间、高度端点、零点自由阈值、显式公式核、余项预算和舍入 hash 六类变量。",
            f"{FINITE_ENDPOINT} AND {TAIL_START} AND {NO_GAP} AND {BUDGET} AND {CONVENTION} AND {HASH_INTERFACE}",
        ),
        row(
            FINITE_ENDPOINT,
            False,
            False,
            "需要把外部零点数量或验证高度转成表生成器实际调用的精确高度端点。",
            GOURDON_EXTERNAL,
        ),
        row(
            TAIL_START,
            False,
            False,
            "需要登记零点自由区公式、常数 R、适用 t0，并说明表尾项从哪里开始使用。",
            KADIRI_EXTERNAL,
        ),
        row(
            NO_GAP,
            False,
            False,
            "需要证明有限 RH 覆盖段、零点自由尾段和显式公式截断段没有高度缺口、重叠重复扣费或变量换口径。",
            f"{FINITE_ENDPOINT} AND {TAIL_START} AND {CONVENTION}",
        ),
        row(
            CONVENTION,
            False,
            False,
            "需要证明 zero sum、zero-free tail、prime-power correction 与 psi/theta 表使用同一显式公式规范。",
            "SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger",
        ),
        row(
            BUDGET,
            False,
            False,
            "需要把 finite-zero 主块、zero-free tail、平凡零点、素数幂和舍入误差分配到表值余量内。",
            f"{PSI_EPS_28} AND {PSI_MIDDLE}",
        ),
        row(
            HASH_INTERFACE,
            False,
            False,
            "需要给出可复现表生成 hash，证明上述预算确实输出 0.00002224 和 1.00002841。",
            "ReproduciblePsiEpsilonTableComputationHashLedger",
        ),
        row(
            TARGET,
            False,
            False,
            "当前完成的是桥接接口压缩和变量表，不是自足闭合；缺任一变量账本都不能推出 epsilon 表。",
            f"{FINITE_ENDPOINT} AND {TAIL_START} AND {NO_GAP} AND {CONVENTION} AND {BUDGET} AND {HASH_INTERFACE}",
        ),
        row(
            "ExternalConditionalBridgeAvailable",
            True,
            False,
            "若显式接受 Dusart/Schoenfeld 表计算为外部合同，可条件跳过内部桥接账本。",
            DUSART_TABLE_EXTERNAL,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "有限零点到尾项桥接仍是解析输入审计；尚未产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_finite_verified_zero_tail_transition_router",
        "status": "finite_verified_zero_tail_transition_interface_taxonomy_closed_bridge_budgets_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "external_pieces_identified_but_not_composed": external_pieces_identified,
        "common_variable_interface_taxonomy_closed": taxonomy_closed,
        "finite_verified_zero_to_tail_transition_closed": False,
        "finite_rh_height_endpoint_closed": False,
        "zero_free_tail_start_height_closed": False,
        "finite_to_tail_no_gap_no_overlap_closed": False,
        "same_explicit_formula_convention_closed": False,
        "psi_epsilon_budget_partition_closed": False,
        "table_generator_hash_interface_closed": False,
        "external_conditional_bridge_available": True,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "common_variable_table": common_variables,
        "replacement_self_contained": {
            TARGET: (
                f"{FINITE_ENDPOINT} AND {TAIL_START} AND {NO_GAP} AND "
                f"{CONVENTION} AND {BUDGET} AND {HASH_INTERFACE}"
            ),
            DUSART_TABLE_EXTERNAL: "external contract only; does not close repository self-contained route",
        },
        "next_direct_attack_target": BUDGET,
        "parallel_attack_targets": [CONVENTION, FINITE_ENDPOINT, TAIL_START, NO_GAP, HASH_INTERFACE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "有限 verified-zero 到零点自由尾项的真正硬点不是再登记一个外部常数，而是共同变量接口。"
            "Gourdon 和 Kadiri 两块即使都可外部引用，也必须经由同一显式公式、同一高度端点、同一尾项阈值、"
            "同一预算分摊和同一可复现 hash，才能推出 Dusart/Schoenfeld 的 epsilon 表值。"
            "本步关闭接口分类，但不关闭自足桥接；最新最窄点压到 psi epsilon 预算分摊账本。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 有限 verified-zero 到零点自由尾项桥接路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"external_pieces_identified_but_not_composed={fmt_bool(result['external_pieces_identified_but_not_composed'])}",
        f"common_variable_interface_taxonomy_closed={fmt_bool(result['common_variable_interface_taxonomy_closed'])}",
        f"finite_verified_zero_to_tail_transition_closed={fmt_bool(result['finite_verified_zero_to_tail_transition_closed'])}",
        f"finite_rh_height_endpoint_closed={fmt_bool(result['finite_rh_height_endpoint_closed'])}",
        f"zero_free_tail_start_height_closed={fmt_bool(result['zero_free_tail_start_height_closed'])}",
        f"finite_to_tail_no_gap_no_overlap_closed={fmt_bool(result['finite_to_tail_no_gap_no_overlap_closed'])}",
        f"same_explicit_formula_convention_closed={fmt_bool(result['same_explicit_formula_convention_closed'])}",
        f"psi_epsilon_budget_partition_closed={fmt_bool(result['psi_epsilon_budget_partition_closed'])}",
        f"table_generator_hash_interface_closed={fmt_bool(result['table_generator_hash_interface_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 共同变量表",
        "",
        "| variable | required_by | must_cover | current_status |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["common_variable_table"]:
        lines.append(
            "| `{variable}` | `{required_by}` | {must_cover} | {current_status} |".format(
                variable=table_cell(item["variable"]),
                required_by=table_cell(item["required_by"]),
                must_cover=table_cell(item["must_cover"]),
                current_status=table_cell(item["current_status"]),
            )
        )
    lines.extend(["", "## 2. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 3. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
