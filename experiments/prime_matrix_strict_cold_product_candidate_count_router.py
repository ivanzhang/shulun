#!/usr/bin/env python3
"""生成 strict cold 产品块候选计数/符号界路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_product_candidate_count_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-product-candidate-count-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-product-candidate-count-router.json
  docs/monograph/prime-matrix-strict-cold-product-candidate-count-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-product-candidate-count-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-product-candidate-count-router.md"

HARDPOINT = "ColdProductBlockCandidateCountOrSymbolicBound"
WINDOW_COUNT = "WindowDivisorCountEnvelopeForColdProductBlock"
RETURN_EXCESS = "CandidateExcessHotDensityOrCommonKernelReturnLedger"
PRIMITIVE_PROJECTION = "PrimitiveProductProjectionRuleExecutableHash"
RANKIN_WEIGHT = "PrimitiveProductRankinWeightP018Comparison"
FINITE_RUNNER = "FiniteColdProductBlockCandidateRunnerHash"
BLOCK_INVENTORY = "ColdProductDyadicBlockInventoryLedger"
CONCRETE_DATA = "ConcretePrimitiveProductRankinEmbeddingDataLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json",
    DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json",
    DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json",
    DOCS / "prime-matrix-strict-cold-filtered-divisor-support-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_cold_product_candidate_count_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


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


def imported_flags() -> dict[str, bool]:
    """读取候选计数硬点需要的导入。"""
    block = load_json(DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json")
    density = load_json(DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json")
    sparse = load_json(DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json")
    kernel = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    return {
        "block_inventory_schema_closed": bool(block.get("cold_product_dyadic_block_inventory_schema_closed")),
        "candidate_set_generator_closed": bool(block.get("cold_product_candidate_set_generator_rule_closed")),
        "hot_density_certificate_closed": bool(density.get("hot_density_certificate_closed")),
        "generic_tau_closure_rejected": bool(density.get("generic_tau_closure_rejected")),
        "dyadic_overload_certificate_closed": bool(sparse.get("dyadic_overload_certificate_closed")),
        "free_common_kernel_return_cycle_excluded": bool(kernel.get("free_common_kernel_return_cycle_excluded")),
    }


def envelope_rows() -> list[dict[str, str]]:
    """列出候选计数可用的封套。"""
    return [
        {
            "name": "raw_window_count",
            "formula": "#Cand(B) <= N_{h0}(Y,2Y]",
            "status": "closed_identity",
            "meaning": "候选产品必须是 h0 在该 dyadic 窗口内的除数。",
        },
        {
            "name": "cold_filter",
            "formula": "Cand(B) = raw_window_count minus hot/common/named-return candidates",
            "status": "closed_definition",
            "meaning": "cold/no-return 条件只删候选，不增加候选。",
        },
        {
            "name": "excess_to_return",
            "formula": "too many candidates before primitive projection -> hot density or common-kernel return",
            "status": "registered_not_excluded",
            "meaning": "过量候选不是免费支撑，必须登记为热窗口或共同核回流。",
        },
        {
            "name": "primitive_symbolic_envelope",
            "formula": "#Cand(B) <= RankinWeight(primitive profiles) + Return(B)",
            "status": "schema_open_projection",
            "meaning": "真正可和封套需要 primitive 投影规则和权重比较。",
        },
    ]


def obstruction_rows() -> list[dict[str, str]]:
    """说明本步不能直接闭合的原因。"""
    return [
        {
            "obstruction": "raw_tau_reuse",
            "reason": "N_{h0}(Y,2Y] 的粗全局求和会退回 tau(h0)，该路线已在 P=100000 边界失败。",
            "required": f"{PRIMITIVE_PROJECTION} OR {FINITE_RUNNER}",
        },
        {
            "obstruction": "cold_filter_not_quantified",
            "reason": "cold/no-return guard 定义了删选集合，但没有给出删选后数量的数值界。",
            "required": RETURN_EXCESS,
        },
        {
            "obstruction": "rankin_without_projection",
            "reason": "没有 d -> primitive rank profile，Rankin 权不能作用到当前候选集合。",
            "required": PRIMITIVE_PROJECTION,
        },
        {
            "obstruction": "finite_runner_missing",
            "reason": "没有当前 source tuple / block 的可复算枚举输出和 hash。",
            "required": FINITE_RUNNER,
        },
    ]


def decision_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    window_envelope_closed = flags["block_inventory_schema_closed"] and flags["candidate_set_generator_closed"]
    return [
        row(
            "CandidateCountTargetImported",
            True,
            flags["candidate_set_generator_closed"],
            "上一层已定义 cold 产品块候选集合，当前需给出计数或符号界。",
            HARDPOINT,
        ),
        row(
            "WindowDivisorCountEnvelopeClosed",
            window_envelope_closed,
            window_envelope_closed,
            "候选数被同一窗口内的 h0 除数数 N_{h0}(Y,2Y] 控制。",
            WINDOW_COUNT,
        ),
        row(
            "RawTauClosureRejectedForCandidateCount",
            True,
            flags["generic_tau_closure_rejected"],
            "不能把窗口除数数再粗化为全局 tau(h0) 并宣称闭合。",
            f"{PRIMITIVE_PROJECTION} OR {FINITE_RUNNER}",
        ),
        row(
            "CandidateExcessReturnRouteRegistered",
            True,
            False,
            "若候选块过量且不进入 primitive 分散支撑，则必须回流热窗口或共同核；回流排斥未闭合。",
            RETURN_EXCESS,
        ),
        row(
            "PrimitiveSymbolicEnvelopeSchemaClosed",
            True,
            False,
            "候选计数可写成 primitive Rankin 权重加回流项，但投影规则和权重比较仍缺。",
            f"{PRIMITIVE_PROJECTION} AND {RANKIN_WEIGHT}",
        ),
        row(
            "ColdProductBlockCandidateCountOrSymbolicBoundProved",
            False,
            False,
            "窗口计数恒等式闭合，但没有可用数值界；必须走 primitive 投影/Rankin 或有限 runner。",
            f"({PRIMITIVE_PROJECTION} AND {RANKIN_WEIGHT}) OR {FINITE_RUNNER}",
        ),
        row(
            "ColdProductDyadicBlockInventoryLedgerProved",
            False,
            False,
            "候选计数/符号界未闭合，产品块 inventory 仍未闭合。",
            BLOCK_INVENTORY,
        ),
        row(
            "ConcretePrimitiveProductRankinEmbeddingDataLedgerProved",
            False,
            False,
            "产品块候选界未闭合，concrete Rankin data 仍未闭合。",
            CONCRETE_DATA,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链终端矛盾。",
            f"{PRIMITIVE_PROJECTION} AND {RANKIN_WEIGHT} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造候选计数/符号界证书。"""
    flags = imported_flags()
    decisions = decision_rows(flags)
    return {
        "certificate_type": "prime_matrix_strict_cold_product_candidate_count_router",
        "status": "candidate_window_count_identity_closed_symbolic_bound_needs_projection_or_runner",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"({PRIMITIVE_PROJECTION} AND {RANKIN_WEIGHT}) OR {FINITE_RUNNER}",
        "next_direct_attack_target": PRIMITIVE_PROJECTION,
        "imported_flags": flags,
        "candidate_envelopes": envelope_rows(),
        "obstructions": obstruction_rows(),
        "decision_table": decisions,
        "window_divisor_count_envelope_closed": bool(
            next(item for item in decisions if item["gate"] == "WindowDivisorCountEnvelopeClosed")["proved"]
        ),
        "raw_tau_closure_rejected_for_candidate_count": bool(
            next(item for item in decisions if item["gate"] == "RawTauClosureRejectedForCandidateCount")["closed"]
        ),
        "candidate_excess_return_route_registered": True,
        "primitive_symbolic_envelope_schema_closed": True,
        "cold_product_block_candidate_count_or_symbolic_bound_proved": False,
        "cold_product_dyadic_block_inventory_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`ColdProductBlockCandidateCountOrSymbolicBound` 的可用恒等式已压实："
            "候选数至多为同一 dyadic 窗口中的除数数，且 cold/no-return guard 只能删候选。"
            "但把它粗化为全局 `tau(h0)` 会回到已失败路线；真正可闭合的路只剩两条："
            "给出 `d -> primitive rank profile` 的可执行投影并完成 Rankin 权重比较，"
            "或提供有限 runner/hash。最新最窄点因此转为 `PrimitiveProductProjectionRuleExecutableHash`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict cold 产品候选计数/符号界路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "window_divisor_count_envelope_closed",
        "raw_tau_closure_rejected_for_candidate_count",
        "candidate_excess_return_route_registered",
        "primitive_symbolic_envelope_schema_closed",
        "cold_product_block_candidate_count_or_symbolic_bound_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. 候选封套")
    lines.append("")
    lines.append("| name | formula | status | meaning |")
    lines.append("| --- | --- | --- | --- |")
    for item in result["candidate_envelopes"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["name", "formula", "status", "meaning"])
            + " |"
        )
    lines.append("")

    lines.append("## 2. 未闭合原因")
    lines.append("")
    lines.append("| obstruction | reason | required |")
    lines.append("| --- | --- | --- |")
    for item in result["obstructions"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["obstruction", "reason", "required"])
            + " |"
        )
    lines.append("")

    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["decision_table"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )
    lines.append("")

    lines.append("## 4. 下一步最窄点")
    lines.append("")
    lines.append(f"- 主攻：`{result['next_direct_attack_target']}`。")
    lines.append(f"- 同步：`{RANKIN_WEIGHT}`。")
    lines.append(f"- 备选：`{FINITE_RUNNER}`。")
    lines.append("- 边界：本步只关闭窗口计数恒等式，不证明候选数足够小。")
    lines.append("")

    lines.append("## 5. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for file, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 文件。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"window_divisor_count_envelope_closed={fmt_bool(result['window_divisor_count_envelope_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
