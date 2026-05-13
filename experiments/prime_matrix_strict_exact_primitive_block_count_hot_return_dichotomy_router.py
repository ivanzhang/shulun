#!/usr/bin/env python3
"""生成 exact primitive 块计数 fallback 的 hot-return 二分证书。

用法示例：
  python3 experiments/prime_matrix_strict_exact_primitive_block_count_hot_return_dichotomy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json

输出：
  docs/monograph/prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json
  docs/monograph/prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json"
OUT_MD = DOCS / "prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.md"

HARDPOINT = "ExactPrimitiveBlockCountP018FallbackTable"
HOT_RETURN = "TerminalCoreHotDivisorWindowPDECorSAE"
FAILURE_PACKET = "PrimitiveProductRankinFailureReturnPacketLedger"
SIGMA_TABLE = "PerBlockRankinSigmaSelectionTable"
RETURN_ABSORB = "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.json",
    DOCS / "prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.json",
    DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json",
    DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json",
    DATA / "primitive-product-rankin-p018-sample-table.json",
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
        "experiments/prime_matrix_strict_exact_primitive_block_count_hot_return_dichotomy_router.py": sha256(
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
    """读取 hot-return 二分需要的导入。"""
    fallback = load_json(DOCS / "prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.json")
    packet = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.json")
    cold_split = load_json(DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json")
    density = load_json(DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json")
    return {
        "exact_fallback_target_imported": fallback.get("next_direct_attack_target") == HARDPOINT,
        "rankin_failure_support_failure_separated": fallback.get(
            "rankin_failure_not_equivalent_to_support_failure_closed"
        )
        is True,
        "failure_packet_schema_closed": packet.get(
            "primitive_product_rankin_failure_return_packet_schema_closed"
        )
        is True,
        "cold_overload_split_closed": cold_split.get("overload_block_structural_split_closed") is True,
        "hot_density_certificate_closed": density.get("hot_density_certificate_closed") is True,
    }


def exact_count_dichotomy_rows() -> list[dict[str, str]]:
    """给出 exact count fallback 的二分。"""
    return [
        {
            "case": "exact_count_pass",
            "condition": "C_B<=P^0.18",
            "effect": "该块实际支撑在预算内，即使 Rankin 上界失败也不回流。",
        },
        {
            "case": "hot_density_return",
            "condition": "C_B>P^0.18",
            "effect": f"同一 dyadic 窗口 `(Y,2Y]` 内已有过预算支撑，登记为 {HOT_RETURN}。",
        },
        {
            "case": "no_clean_overbudget",
            "condition": "C_B>P^0.18 and no named trigger",
            "effect": "与 hot_density_return 的定义性触发矛盾；不能成为 clean residual。",
        },
        {
            "case": "payload_missing",
            "condition": "C_B 未给出也无可复核上界",
            "effect": "只能作为 replay/table 任务保留，不能宣布实际 pass。",
        },
    ]


def hot_packet_payload_rows() -> list[dict[str, str]]:
    """定义 hot-density 回流包最小 payload。"""
    return [
        {"field": "source_tuple_hash", "role": "绑定反例 formal unit。"},
        {"field": "block_id", "role": "绑定 dyadic 窗口 `(Y,2Y]`。"},
        {"field": "Y", "role": "给出热窗口左端点。"},
        {"field": "exact_count_or_cap", "role": "证明 `C_B>P^0.18` 的计数或下界证书。"},
        {"field": "p018_budget", "role": "同参数预算阈值。"},
        {"field": "overload_ratio", "role": "`C_B/P^0.18`，作为 hot-density packet 的强度。"},
    ]


def diagnostic_rows() -> list[dict[str, Any]]:
    """复用诊断样本展示本二分。"""
    sample = load_json(DATA / "primitive-product-rankin-p018-sample-table.json")
    result: list[dict[str, Any]] = []
    for item in sample.get("sample_fail_rows", []):
        count = int(item["actual_count_diagnostic_only"])
        budget = float(item["p018_budget"])
        result.append(
            {
                "sample_row_id": item["sample_row_id"],
                "Y": item["Y"],
                "h0": item["h0"],
                "exact_count_diagnostic_only": count,
                "integer_budget_floor": math.floor(budget),
                "p018_budget": budget,
                "hot_return_triggered_diagnostic": count > budget,
                "refined_diagnostic_verdict": "hot_density_return" if count > budget else "exact_count_pass",
            }
        )
    return result


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "ExactFallbackTargetImported",
            result["exact_fallback_target_imported"],
            result["exact_fallback_target_imported"],
            "上一层已把 clean primitive 残项压成精确块计数 fallback。",
            HARDPOINT,
        ),
        row(
            "ExactCountPassOrHotReturnDichotomyClosed",
            result["exact_count_pass_or_hot_return_dichotomy_closed"],
            result["exact_count_pass_or_hot_return_dichotomy_closed"],
            "每个 actual 块按 `C_B<=P^0.18` 或 `C_B>P^0.18` 二分；后者就是 hot-density 回流。",
            "pass-or-hot-return",
        ),
        row(
            "CleanExactOverbudgetWithoutNamedReturnExcluded",
            result["clean_exact_overbudget_without_named_return_excluded"],
            result["clean_exact_overbudget_without_named_return_excluded"],
            "精确计数超预算自身触发 dyadic 热窗口，因此无名 clean exact overbudget 不存在。",
            HOT_RETURN,
        ),
        row(
            "DiagnosticExactRowsRemainPass",
            result["diagnostic_exact_rows_all_pass_not_hot"],
            result["diagnostic_exact_rows_all_pass_not_hot"],
            "当前诊断 Rankin 失败行仍全部是 exact_count_pass，没有触发 hot return。",
            "diagnostic only",
        ),
        row(
            "TerminalCoreHotDivisorWindowExcluded",
            False,
            False,
            "hot-density 被命名回流，但热窗口/PDEC/SAE 终端尚未排斥或吸收。",
            HOT_RETURN,
        ),
        row(
            "ExactPrimitiveBlockCountReplayTablePresent",
            False,
            False,
            "本步给出逻辑二分，不提供全体 actual replay 表。",
            "optional replay certificate",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{HOT_RETURN} AND {RETURN_ABSORB} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 hot-return 二分证书。"""
    flags = imported_flags()
    diagnostic = diagnostic_rows()
    dichotomy_closed = (
        flags["rankin_failure_support_failure_separated"]
        and flags["failure_packet_schema_closed"]
        and flags["cold_overload_split_closed"]
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_exact_primitive_block_count_hot_return_dichotomy_router",
        "status": "exact_count_fallback_dichotomy_closed_hot_return_terminal_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "exact_count_pass_or_hot_return_dichotomy_closed": dichotomy_closed,
        "clean_exact_overbudget_without_named_return_excluded": dichotomy_closed,
        "clean_primitive_dispersion_rankin_failure_residual_removed": dichotomy_closed,
        "diagnostic_exact_rows_all_pass_not_hot": bool(diagnostic)
        and all(not item["hot_return_triggered_diagnostic"] for item in diagnostic),
        "terminal_core_hot_divisor_window_pdec_or_sae_excluded": False,
        "exact_primitive_block_count_replay_table_present": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": HOT_RETURN,
        "next_direct_attack_target": HOT_RETURN,
        "parallel_attack_targets": [
            SIGMA_TABLE,
            FAILURE_PACKET,
            RETURN_ABSORB,
            SPARSE_BUDGET,
            PERSISTENT_TERMINAL,
            DSTRUCTURE,
        ],
        "exact_count_dichotomy_rows": exact_count_dichotomy_rows(),
        "hot_packet_payload_rows": hot_packet_payload_rows(),
        "diagnostic_exact_count_rows": diagnostic,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ExactPrimitiveBlockCountP018FallbackTable` 的核心逻辑二分已闭合："
            "actual dyadic 块若精确计数 `C_B<=P^0.18`，则是 exact_count_pass；"
            "若 `C_B>P^0.18`，同一 `(Y,2Y]` 窗口已形成热除数窗口，必须登记为 "
            f"`{HOT_RETURN}`。因此 clean exact overbudget 不能作为无名残项停留。"
            "但 hot-density/PDEC/SAE 终端本身仍未排斥，行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix strict exact primitive 块计数 hot-return 二分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_count_pass_or_hot_return_dichotomy_closed={fmt_bool(result['exact_count_pass_or_hot_return_dichotomy_closed'])}",
        f"clean_exact_overbudget_without_named_return_excluded={fmt_bool(result['clean_exact_overbudget_without_named_return_excluded'])}",
        f"terminal_core_hot_divisor_window_pdec_or_sae_excluded={fmt_bool(result['terminal_core_hot_divisor_window_pdec_or_sae_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确计数二分",
        "",
        "| case | condition | effect |",
        "| --- | --- | --- |",
    ]
    for item in result["exact_count_dichotomy_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['case'])}`",
                    table_cell(item["condition"]),
                    table_cell(item["effect"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. hot-density packet payload",
            "",
            "| field | role |",
            "| --- | --- |",
        ]
    )
    for item in result["hot_packet_payload_rows"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['role'])} |")
    lines.extend(
        [
            "",
            "## 3. 诊断样本",
            "",
            "| sample_row_id | Y | h0 | exact_count | floor(P^0.18) | refined_verdict |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["diagnostic_exact_count_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(item["sample_row_id"]),
                    str(item["Y"]),
                    str(item["h0"]),
                    str(item["exact_count_diagnostic_only"]),
                    str(item["integer_budget_floor"]),
                    f"`{table_cell(item['refined_diagnostic_verdict'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 含义：clean primitive 无名残项已被删除，剩余转为热除数窗口/PDEC/SAE 终端排斥或预算吸收。",
            "- 边界：本步不排斥 hot-density 终端，不声明行/列命题无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
