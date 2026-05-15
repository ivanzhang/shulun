#!/usr/bin/env python3
"""把 k>=1 moving-layer 聚合分支压缩为压力缺陷。

用法示例：
  python3 experiments/prime_matrix_square_phase_kge1_aggregate_pressure_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-kge1-aggregate-pressure-router.json

输出：
  data/square-phase-kge1-aggregate-pressure-ledger.json
  docs/monograph/prime-matrix-square-phase-kge1-aggregate-pressure-router.json
  docs/monograph/prime-matrix-square-phase-kge1-aggregate-pressure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SPLIT_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py"

OUT_LEDGER = DATA / "square-phase-kge1-aggregate-pressure-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-kge1-aggregate-pressure-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-kge1-aggregate-pressure-router.md"

MAIN_TARGET = "KGe1MovingLayerAggregateBoundOrPDEC"
NEXT_TARGET = "KGe1AggregatePressureDefectOrMovingLayerPDEC"


def load_split_router() -> Any:
    """加载上一层 k0/k>=1 分裂路由器。"""
    spec = importlib.util.spec_from_file_location("noslot_k0_split_router", SPLIT_ROUTER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SPLIT_ROUTER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩记录字段。"""
    return {
        "p": record["p"],
        "side": record["side"],
        "prime_window": record["prime_window"],
        "threshold": record["threshold"],
        "kge1_load": record["kge1_load"],
        "k0_load": record["k0_load"],
        "no_slot_load": record["no_slot_load"],
        "support_b_count": record["support_b_count"],
        "tail_b_max": record["tail_b_max"],
        "kge1_pressure_branch": record["kge1_pressure_branch"],
        "terminal_kge1_branch": record["terminal_kge1_branch"],
        "margin_vs_4kge1": record["margin_vs_4kge1"],
        "margin_vs_support": record["margin_vs_support"],
    }


def kge1_support_b_count(split: Any, p: int, side: str) -> int:
    """计算 k>=1 无槽支撑在 b 轴上的整数点数，不要求 q 为素数。"""
    total = 0
    for b_value in range(1, split.b_max_for_tail(p) + 1):
        k_value = split.layer_k(p, b_value)
        if k_value >= 1 and split.side_formula_holds(p, b_value, k_value, side):
            total += 1
    return total


def audit_side(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """审计单侧 k>=1 聚合压力。"""
    record = split.audit_p(p, prime_flags, pi_prefix)
    prime_window = record[f"{side}_prime_window"]
    threshold = record[f"{side}_threshold_half_primewindow"]
    kge1_load = record[f"{side}_kge1_load"]
    k0_load = record[f"{side}_k0_load"]
    no_slot_load = record[f"{side}_no_slot_load"]
    support_count = kge1_support_b_count(split, p, side)
    pressure_branch = 2 * kge1_load >= threshold
    no_slot_large = no_slot_load >= threshold
    return {
        "p": p,
        "side": side,
        "prime_window": prime_window,
        "threshold": threshold,
        "kge1_load": kge1_load,
        "k0_load": k0_load,
        "no_slot_load": no_slot_load,
        "support_b_count": support_count,
        "tail_b_max": split.b_max_for_tail(p),
        "kge1_load_le_support_ok": kge1_load <= support_count,
        "kge1_pressure_branch": pressure_branch,
        "kge1_pressure_forces_defect_ok": (not pressure_branch) or prime_window <= 4 * kge1_load,
        "no_slot_large_branch": no_slot_large,
        "terminal_kge1_branch": pressure_branch and no_slot_large,
        "margin_vs_4kge1": prime_window - 4 * kge1_load,
        "margin_vs_support": prime_window - 4 * support_count,
        "support_density_in_tail_b": None if split.b_max_for_tail(p) == 0 else support_count / split.b_max_for_tail(p),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "kge1_aggregate_exact_load",
            "status": "closed",
            "statement": "The k>=1 branch load is exactly the aggregate prime-load over all nonzero moving layers.",
        },
        {
            "name": "kge1_load_support_envelope",
            "status": "closed",
            "statement": "The k>=1 prime-load is bounded by its explicit b-axis no-slot support count.",
        },
        {
            "name": "kge1_pressure_forces_squarewindow_defect",
            "status": "closed",
            "statement": "If the k>=1 branch carries the split threshold, then PrimeWindow<=4*KGe1Load.",
        },
        {
            "name": "kge1_pressure_defect_exclusion",
            "status": "open",
            "statement": "A global proof still needs PrimeWindow>4*KGe1Load, or a MovingLayer-PDEC exclusion of persistent aggregate pressure.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "KGe1AggregateLoadClosed",
            "closed": True,
            "proved": True,
            "meaning": "k>=1 聚合负载由上一层 moving layer 原子精确给出。",
            "remaining": "closed",
        },
        {
            "gate": "KGe1SupportEnvelopeClosed",
            "closed": result["support_envelope_failure_count"] == 0,
            "proved": True,
            "meaning": "k>=1 prime-load 不超过显式 b 支撑点数。",
            "remaining": "closed",
        },
        {
            "gate": "KGe1PressureImpliesSquareWindowDefectClosed",
            "closed": result["pressure_implication_failure_count"] == 0,
            "proved": True,
            "meaning": "若 k>=1 分支承担半阈值，则 PrimeWindow<=4*KGe1Load。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoTerminalKGe1Branch",
            "closed": result["terminal_kge1_branch_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 未出现终端 k>=1 分支。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "KGe1AggregatePressureDefectExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明平方窗素数数压过 k>=1 聚合负载四倍，或排斥持久 moving-layer 聚合压力缺陷。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 k>=1 分支压成压力缺陷，不关闭全局行/列命题。",
            "remaining": "PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC AND KGe1AggregatePressureDefectOrMovingLayerPDEC",
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    split = load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = split.sieve(max_p)
    p_values = [p for p in range(3, max_p + 1) if small_flags[p]]
    records = [
        audit_side(split, p, side, prime_flags, pi_prefix)
        for p in p_values
        for side in ("plus", "minus")
    ]
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    support_failures = [record for record in records if not record["kge1_load_le_support_ok"]]
    pressure_implication_failures = [
        record for record in records if not record["kge1_pressure_forces_defect_ok"]
    ]
    pressure_records = [record for record in records if record["kge1_pressure_branch"]]
    terminal_records = [record for record in records if record["terminal_kge1_branch"]]
    worst_vs_4k = min(records, key=lambda record: record["margin_vs_4kge1"], default=None)
    worst_vs_support = min(records, key=lambda record: record["margin_vs_support"], default=None)
    max_kge1 = max(records, key=lambda record: record["kge1_load"], default=None)
    max_support_density = max(
        [record for record in records if record["support_density_in_tail_b"] is not None],
        key=lambda record: record["support_density_in_tail_b"],
        default=None,
    )
    aggregate = {
        "record_count": len(records),
        "combined_prime_window": sum(record["prime_window"] for record in records),
        "combined_kge1_load": sum(record["kge1_load"] for record in records),
        "combined_support_b_count": sum(record["support_b_count"] for record in records),
        "support_envelope_failure_count": len(support_failures),
        "pressure_implication_failure_count": len(pressure_implication_failures),
        "kge1_pressure_branch_count": len(pressure_records),
        "terminal_kge1_branch_count": len(terminal_records),
        "min_margin_vs_4kge1": worst_vs_4k["margin_vs_4kge1"] if worst_vs_4k else None,
        "min_margin_vs_support": worst_vs_support["margin_vs_support"] if worst_vs_support else None,
        "max_kge1_load": max_kge1["kge1_load"] if max_kge1 else 0,
        "max_support_density_in_tail_b": (
            max_support_density["support_density_in_tail_b"] if max_support_density else None
        ),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "support_envelope_failure_count": len(support_failures),
        "pressure_implication_failure_count": len(pressure_implication_failures),
        "kge1_pressure_branch_count": len(pressure_records),
        "terminal_kge1_branch_count": len(terminal_records),
        "worst_vs_4kge1_record": compact(worst_vs_4k) if worst_vs_4k else None,
        "worst_vs_support_record": compact(worst_vs_support) if worst_vs_support else None,
        "max_kge1_record": compact(max_kge1) if max_kge1 else None,
        "max_support_density_record": compact(max_support_density) if max_support_density else None,
        "pressure_records": [compact(record) for record in pressure_records[:80]],
        "terminal_kge1_records": [compact(record) for record in terminal_records[:50]],
        "sample_records": [compact(record) for record in sample_records],
        "support_failures": [compact(record) for record in support_failures[:20]],
        "pressure_implication_failures": [
            compact(record) for record in pressure_implication_failures[:20]
        ],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_kge1_aggregate_pressure_router",
        "status": "kge1_aggregate_branch_reduced_to_squarewindow_pressure_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "support_envelope_failure_count": len(support_failures),
        "pressure_implication_failure_count": len(pressure_implication_failures),
        "kge1_pressure_branch_count": len(pressure_records),
        "terminal_kge1_branch_count": len(terminal_records),
        "worst_vs_4kge1_record": ledger["worst_vs_4kge1_record"],
        "worst_vs_support_record": ledger["worst_vs_support_record"],
        "max_kge1_record": ledger["max_kge1_record"],
        "max_support_density_record": ledger["max_support_density_record"],
        "pressure_records": ledger["pressure_records"],
        "sample_records": ledger["sample_records"],
        "kge1_support_envelope_closed": len(support_failures) == 0,
        "kge1_pressure_implication_closed": len(pressure_implication_failures) == 0,
        "kge1_aggregate_pressure_defect_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "alternative_attack_target": "PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC",
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_kge1_aggregate_pressure_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(
                SPLIT_ROUTER
            ),
            "data/square-phase-kge1-aggregate-pressure-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 `KGe1MovingLayerAggregateBoundOrPDEC` 精确压成压力缺陷："
            "若 k>=1 聚合分支承担 split 半阈值，则必有 `PrimeWindow<=4*KGe1Load`。"
            "`KGe1Load` 仍是显式 moving-layer 原子上的素数负载，并受 b 轴无槽支撑点数控制。"
            "有限审计只出现一个压力样本且不是终端 no-slot 分支；全局仍需排斥持久聚合压力缺陷。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase k>=1 aggregate pressure router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"support_envelope_failure_count={result['support_envelope_failure_count']}",
        f"pressure_implication_failure_count={result['pressure_implication_failure_count']}",
        f"kge1_pressure_branch_count={result['kge1_pressure_branch_count']}",
        f"terminal_kge1_branch_count={result['terminal_kge1_branch_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确压缩",
        "",
        "设 `K1_sign(P)` 为所有 `k>=1` moving-layer 原子上的 prime-load 聚合。若该分支承担 split 半阈值，则",
        "",
        "```text",
        "2*K1_sign(P) >= ceil(PrimeWindow_sign(P)/2),",
        "```",
        "",
        "从而必有",
        "",
        "```text",
        "PrimeWindow_sign(P) <= 4*K1_sign(P).",
        "```",
        "",
        "因此 k>=1 分支的终端反例必须是平方窗素数数相对 moving-layer 聚合负载过小的压力缺陷。",
        "",
        "## 2. 支撑包络",
        "",
        "`K1_sign(P)` 只计入满足 k>=1 无槽二次相位不等式且 `q=P-2b` 为素数的 b；因此",
        "",
        "```text",
        "K1_sign(P) <= #{b: k(b)>=1 and b lies in the sign no-slot support}.",
        "```",
        "",
        "这个包络无条件正确，但单靠它仍不足以全局闭合，需要更细的素数负载界或 PDEC 排斥。",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| combined PrimeWindow | {agg['combined_prime_window']} |",
        f"| combined KGe1Load | {agg['combined_kge1_load']} |",
        f"| combined support b count | {agg['combined_support_b_count']} |",
        f"| support envelope failures | {agg['support_envelope_failure_count']} |",
        f"| pressure implication failures | {agg['pressure_implication_failure_count']} |",
        f"| k>=1 pressure branch count | {agg['kge1_pressure_branch_count']} |",
        f"| terminal k>=1 branch count | {agg['terminal_kge1_branch_count']} |",
        f"| min margin vs 4KGe1 | {agg['min_margin_vs_4kge1']} |",
        f"| min margin vs support | {agg['min_margin_vs_support']} |",
        f"| max KGe1Load | {agg['max_kge1_load']} |",
        f"| max support density in tail b | {agg['max_support_density_in_tail_b']} |",
        "",
        "## 4. 关键记录",
        "",
        "| label | P | side | PrimeWindow | KGe1 | support | no-slot | margin vs 4K | terminal |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for label, record in [
        ("worst vs 4KGe1", result["worst_vs_4kge1_record"]),
        ("worst vs support", result["worst_vs_support_record"]),
        ("max KGe1", result["max_kge1_record"]),
        ("max support density", result["max_support_density_record"]),
    ]:
        if not record:
            continue
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(label),
                    str(record["p"]),
                    table_cell(record["side"]),
                    str(record["prime_window"]),
                    str(record["kge1_load"]),
                    str(record["support_b_count"]),
                    str(record["no_slot_load"]),
                    str(record["margin_vs_4kge1"]),
                    f"`{fmt_bool(record['terminal_kge1_branch'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 压力样本",
            "",
            "| P | side | PrimeWindow | KGe1 | K0 | no-slot | support | terminal |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for record in result["pressure_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    table_cell(record["side"]),
                    str(record["prime_window"]),
                    str(record["kge1_load"]),
                    str(record["k0_load"]),
                    str(record["no_slot_load"]),
                    str(record["support_b_count"]),
                    f"`{fmt_bool(record['terminal_kge1_branch'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 6. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 7. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 8. 下一步",
            "",
            "- 主攻：`KGe1AggregatePressureDefectOrMovingLayerPDEC`。",
            "- 与 k0 分支并行，最终还需 `PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC` 或更精细的平方窗/聚合负载比较。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 9. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument(
        "--sample-ps",
        type=str,
        default="13,17,19,23,29,31,73,101,499,523,1009,2003,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-kge1-aggregate-pressure-router.md"] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "status": result["status"],
            "max_p": args.max_p,
            "kge1_pressure_branch_count": result["kge1_pressure_branch_count"],
            "terminal_kge1_branch_count": result["terminal_kge1_branch_count"],
            "next_direct_attack_target": result["next_direct_attack_target"],
            "row_column_unconditional_closed": result["row_column_unconditional_closed"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
