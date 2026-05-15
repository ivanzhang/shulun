#!/usr/bin/env python3
"""审查 k0 根缺陷闭合所需的平方窗输入边界。

用法示例：
  python3 experiments/prime_matrix_square_phase_rootdefect_input_boundary_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-rootdefect-input-boundary-router.json

输出：
  data/square-phase-rootdefect-input-boundary-ledger.json
  docs/monograph/prime-matrix-square-phase-rootdefect-input-boundary-router.json
  docs/monograph/prime-matrix-square-phase-rootdefect-input-boundary-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

K0_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_k0_rootwindow_defect_router.py"

OUT_LEDGER = DATA / "square-phase-rootdefect-input-boundary-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-rootdefect-input-boundary-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-rootdefect-input-boundary-router.md"

MAIN_TARGET = "SquareWindowRootDefectLowerBoundOrRootWindowPDEC"
NEXT_TARGET = "PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC"


def load_k0_router() -> Any:
    """加载上一层 k0 根缺陷路由器，复用已审计过的定义。"""
    spec = importlib.util.spec_from_file_location("k0_rootwindow_defect_router", K0_ROUTER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K0_ROUTER}")
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


def count_threshold_gt_2sqrt(p: int) -> int:
    """返回整数条件 W>2sqrt(P) 等价的最小 W。"""
    return isqrt(4 * p) + 1


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩记录字段，便于写入报告。"""
    return {
        "p": record["p"],
        "side": record["side"],
        "prime_window": record["prime_window"],
        "root_load": record["root_load"],
        "root_length": record["root_length"],
        "root_q_interval": record["root_q_interval"],
        "four_root_load": record["four_root_load"],
        "gt_2sqrt_threshold": record["gt_2sqrt_threshold"],
        "beats_exact_root_defect": record["beats_exact_root_defect"],
        "beats_2sqrt_sufficient_input": record["beats_2sqrt_sufficient_input"],
        "terminal_k0_branch": record["terminal_k0_branch"],
        "margin_vs_4root": record["margin_vs_4root"],
        "margin_vs_2sqrt_threshold": record["margin_vs_2sqrt_threshold"],
    }


def audit_side(k0: Any, p: int, side: str, prime_flags: bytearray) -> dict[str, Any]:
    """审计单侧根缺陷输入边界。"""
    root = k0.root_load(p, side, prime_flags)
    prime_window = k0.square_prime_count(p, side, prime_flags)
    no_slot = k0.no_slot_load(p, side, prime_flags)
    threshold = (prime_window + 1) // 2
    root_load = root["root_load"]
    root_length = root["b_length"]
    gt_2sqrt_threshold = count_threshold_gt_2sqrt(p)
    return {
        "p": p,
        "side": side,
        "prime_window": prime_window,
        "root_load": root_load,
        "root_length": root_length,
        "root_q_interval": [root["q_lo"], root["q_hi"]],
        "root_load_le_length_ok": root_load <= root_length,
        "root_length_sqrt_envelope_ok": 4 * root_length * root_length <= p,
        "root_load_sqrt_envelope_ok": 4 * root_load * root_load <= p,
        "four_root_load": 4 * root_load,
        "gt_2sqrt_threshold": gt_2sqrt_threshold,
        "beats_exact_root_defect": prime_window > 4 * root_load,
        "beats_2sqrt_sufficient_input": prime_window >= gt_2sqrt_threshold,
        "k0_large_branch": 2 * root_load >= threshold,
        "no_slot_large_branch": no_slot >= threshold,
        "terminal_k0_branch": 2 * root_load >= threshold and no_slot >= threshold,
        "margin_vs_4root": prime_window - 4 * root_load,
        "margin_vs_2sqrt_threshold": prime_window - gt_2sqrt_threshold,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "rootload_sqrt_envelope",
            "status": "closed",
            "statement": "For both signs, the k=0 root-window load satisfies R0_sign(P)<=sqrt(P)/2.",
        },
        {
            "name": "primewindow_gt_2sqrt_closes_k0",
            "status": "closed",
            "statement": "If PrimeWindow_sign(P)>2sqrt(P), then PrimeWindow_sign(P)>4R0_sign(P), so the k0 root-defect branch is excluded.",
        },
        {
            "name": "external_0525_not_enough",
            "status": "closed_as_boundary",
            "statement": "A generic X^0.525 short-interval theorem gives length P^1.05 at X=P^2 and does not supply the needed length P count.",
        },
        {
            "name": "prime_square_endpoint_count_input",
            "status": "open",
            "statement": "A global self-contained closure still needs PrimeWindow_sign(P)>2sqrt(P), or a RootWindow-PDEC exclusion.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "RootLoadSqrtEnvelopeClosed",
            "closed": result["root_sqrt_envelope_failure_count"] == 0,
            "proved": True,
            "meaning": "根窗长度给出 R0<=sqrt(P)/2，因此 4R0<=2sqrt(P)。",
            "remaining": "closed",
        },
        {
            "gate": "CountGt2SqrtWouldCloseK0Closed",
            "closed": True,
            "proved": True,
            "meaning": "若平方窗素数数大于 2sqrt(P)，则必然压过 4R0。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteExactRootDefectOnlySmallNonterminal",
            "closed": result["terminal_k0_branch_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中精确根缺陷只出现在小样本，且没有终端 k0 分支。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GenericBHP0525InputSufficient",
            "closed": False,
            "proved": False,
            "meaning": "通用 X^0.525 短区间输入在 X=P^2 后长于目标窗口，不能关闭本门。",
            "remaining": "theta<=1/2 on prime-square endpoints",
        },
        {
            "gate": "PrimeSquareEndpointCountGt2SqrtPProved",
            "closed": False,
            "proved": False,
            "meaning": "当前仓库尚未证明每个素数 P 的 P^2 正负长度 P 窗口中有超过 2sqrt(P) 个素数。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 k0 根缺陷的外部/内部输入边界定清，不关闭全局行/列命题。",
            "remaining": f"{NEXT_TARGET} AND KGe1MovingLayerAggregateBoundOrPDEC",
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    k0 = load_k0_router()
    prime_flags = k0.sieve(max_p * max_p + max_p)
    small_flags = k0.sieve(max_p)
    p_values = [p for p in range(3, max_p + 1) if small_flags[p]]
    records = [
        audit_side(k0, p, side, prime_flags)
        for p in p_values
        for side in ("plus", "minus")
    ]
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    root_failures = [
        record
        for record in records
        if not record["root_load_le_length_ok"]
        or not record["root_length_sqrt_envelope_ok"]
        or not record["root_load_sqrt_envelope_ok"]
    ]
    exact_root_defects = [record for record in records if not record["beats_exact_root_defect"]]
    count_input_failures = [
        record for record in records if not record["beats_2sqrt_sufficient_input"]
    ]
    terminal_records = [record for record in records if record["terminal_k0_branch"]]
    worst_vs_4root = min(records, key=lambda record: record["margin_vs_4root"], default=None)
    worst_vs_2sqrt = min(records, key=lambda record: record["margin_vs_2sqrt_threshold"], default=None)
    max_root_load = max(records, key=lambda record: record["root_load"], default=None)

    aggregate = {
        "record_count": len(records),
        "combined_prime_window": sum(record["prime_window"] for record in records),
        "combined_root_load": sum(record["root_load"] for record in records),
        "root_sqrt_envelope_failure_count": len(root_failures),
        "exact_root_defect_record_count": len(exact_root_defects),
        "gt_2sqrt_input_failure_count": len(count_input_failures),
        "terminal_k0_branch_count": len(terminal_records),
        "min_margin_vs_4root": worst_vs_4root["margin_vs_4root"] if worst_vs_4root else None,
        "min_margin_vs_2sqrt_threshold": worst_vs_2sqrt["margin_vs_2sqrt_threshold"] if worst_vs_2sqrt else None,
        "max_root_load": max_root_load["root_load"] if max_root_load else 0,
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "root_sqrt_envelope_failure_count": len(root_failures),
        "exact_root_defect_record_count": len(exact_root_defects),
        "gt_2sqrt_input_failure_count": len(count_input_failures),
        "terminal_k0_branch_count": len(terminal_records),
        "worst_vs_4root_record": compact(worst_vs_4root) if worst_vs_4root else None,
        "worst_vs_2sqrt_record": compact(worst_vs_2sqrt) if worst_vs_2sqrt else None,
        "max_root_load_record": compact(max_root_load) if max_root_load else None,
        "exact_root_defect_records": [compact(record) for record in exact_root_defects[:80]],
        "gt_2sqrt_input_failure_records": [compact(record) for record in count_input_failures[:120]],
        "terminal_k0_records": [compact(record) for record in terminal_records[:50]],
        "sample_records": [compact(record) for record in sample_records],
        "root_sqrt_envelope_failures": [compact(record) for record in root_failures[:20]],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_rootdefect_input_boundary_router",
        "status": "k0_rootdefect_reduced_to_prime_square_endpoint_count_or_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "root_sqrt_envelope_failure_count": len(root_failures),
        "exact_root_defect_record_count": len(exact_root_defects),
        "gt_2sqrt_input_failure_count": len(count_input_failures),
        "terminal_k0_branch_count": len(terminal_records),
        "worst_vs_4root_record": ledger["worst_vs_4root_record"],
        "worst_vs_2sqrt_record": ledger["worst_vs_2sqrt_record"],
        "max_root_load_record": ledger["max_root_load_record"],
        "sample_records": ledger["sample_records"],
        "rootload_sqrt_envelope_closed": len(root_failures) == 0,
        "primewindow_gt_2sqrt_closes_k0_closed": True,
        "generic_0525_short_interval_sufficient": False,
        "prime_square_endpoint_count_gt_2sqrt_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "alternative_attack_target": "KGe1MovingLayerAggregateBoundOrPDEC",
        "theorem_rows": theorem_rows(),
        "external_input_boundary": {
            "sufficient_input": "For every odd prime P and each sign, PrimeWindow_sign(P)>2*sqrt(P).",
            "why_sufficient": "R0_sign(P)<=sqrt(P)/2, hence 4*R0_sign(P)<=2*sqrt(P).",
            "known_generic_short_interval_gap": "Baker-Harman-Pintz X^0.525 gives P^1.05 at X=P^2, not length P.",
            "cannot_claim_self_contained_closure": True,
        },
        "source_hashes": {
            "experiments/prime_matrix_square_phase_rootdefect_input_boundary_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_k0_rootwindow_defect_router.py": sha256(K0_ROUTER),
            "data/square-phase-rootdefect-input-boundary-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "`k=0` 根缺陷现在有精确输入边界：根窗本身可无条件压到 "
            "`RootLoad<=sqrt(P)/2`，所以若能证明平方窗素数数 `PrimeWindow>2sqrt(P)`，"
            "则自动得到 `PrimeWindow>4*RootLoad` 并排除 k0 分支。"
            "但这个平方窗计数输入正处在 `X=P^2` 的 `X^(1/2)` 短区间尺度，"
            "通用 `X^0.525` 定理不能给出它；因此当前自足路线仍需证明该特殊素数平方端点计数，"
            "或将失败登记并排斥为 RootWindow-PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    boundary = result["external_input_boundary"]
    lines = [
        "# Prime Matrix square-phase root-defect input boundary router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"root_sqrt_envelope_failure_count={result['root_sqrt_envelope_failure_count']}",
        f"exact_root_defect_record_count={result['exact_root_defect_record_count']}",
        f"gt_2sqrt_input_failure_count={result['gt_2sqrt_input_failure_count']}",
        f"terminal_k0_branch_count={result['terminal_k0_branch_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 无条件可证部分",
        "",
        "根窗长度给出",
        "",
        "```text",
        "RootLoad_sign(P) <= root window length <= sqrt(P)/2.",
        "```",
        "",
        "因此",
        "",
        "```text",
        "4*RootLoad_sign(P) <= 2*sqrt(P).",
        "```",
        "",
        "所以以下输入足以关闭 k0 根缺陷：",
        "",
        "```text",
        "PrimeWindow_sign(P) > 2*sqrt(P).",
        "```",
        "",
        "## 2. 输入边界",
        "",
        "| item | value |",
        "| --- | --- |",
        f"| sufficient input | {table_cell(boundary['sufficient_input'])} |",
        f"| why sufficient | {table_cell(boundary['why_sufficient'])} |",
        f"| generic short interval gap | {table_cell(boundary['known_generic_short_interval_gap'])} |",
        f"| self-contained closure claimed | `{fmt_bool(not boundary['cannot_claim_self_contained_closure'])}` |",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| combined PrimeWindow | {agg['combined_prime_window']} |",
        f"| combined RootLoad | {agg['combined_root_load']} |",
        f"| root sqrt envelope failures | {agg['root_sqrt_envelope_failure_count']} |",
        f"| exact root-defect records | {agg['exact_root_defect_record_count']} |",
        f"| >2sqrt input failures | {agg['gt_2sqrt_input_failure_count']} |",
        f"| terminal k0 branch count | {agg['terminal_k0_branch_count']} |",
        f"| min margin vs 4RootLoad | {agg['min_margin_vs_4root']} |",
        f"| min margin vs >2sqrt threshold | {agg['min_margin_vs_2sqrt_threshold']} |",
        f"| max RootLoad | {agg['max_root_load']} |",
        "",
        "## 4. 关键记录",
        "",
        "| label | P | side | PrimeWindow | RootLoad | 4RootLoad | >2sqrt threshold | margin vs 4R | margin vs threshold | terminal |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for label, record in [
        ("worst vs 4RootLoad", result["worst_vs_4root_record"]),
        ("worst vs >2sqrt", result["worst_vs_2sqrt_record"]),
        ("max RootLoad", result["max_root_load_record"]),
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
                    str(record["root_load"]),
                    str(record["four_root_load"]),
                    str(record["gt_2sqrt_threshold"]),
                    str(record["margin_vs_4root"]),
                    str(record["margin_vs_2sqrt_threshold"]),
                    f"`{fmt_bool(record['terminal_k0_branch'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 命题行",
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
            "## 6. 决策表",
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
            "## 7. 下一步",
            "",
            "- 主攻：`PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC`。",
            "- 这不是普通 `X^0.525` 短区间输入能给出的结论；若不引入外部新定理，必须继续从 square-phase 覆盖失败中抽取 RootWindow-PDEC/SAE。",
            "- 并行保留：`KGe1MovingLayerAggregateBoundOrPDEC`。",
            "",
            "## 8. 依赖哈希",
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
        default="13,17,19,23,29,31,73,101,499,1009,2003,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-rootdefect-input-boundary-router.md"] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "status": result["status"],
            "max_p": args.max_p,
            "root_sqrt_envelope_failure_count": result["root_sqrt_envelope_failure_count"],
            "exact_root_defect_record_count": result["exact_root_defect_record_count"],
            "gt_2sqrt_input_failure_count": result["gt_2sqrt_input_failure_count"],
            "next_direct_attack_target": result["next_direct_attack_target"],
            "row_column_unconditional_closed": result["row_column_unconditional_closed"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
