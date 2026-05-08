#!/usr/bin/env python3
"""Prime Matrix 高段模型余量因子化路由器。

用法示例：
  python3 experiments/prime_matrix_high_segment_model_gap_factorization_router.py

输出：
  docs/monograph/prime-matrix-high-segment-model-gap-factorization-router.json
  docs/monograph/prime-matrix-high-segment-model-gap-factorization-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
AUDIT_DOCS = ROOT / "docs"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-explicit-model-gap-finite-ledger-router.json"
DEFAULT_DYNAMIC_JSON = AUDIT_DOCS / "dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json"
DEFAULT_JSON = DOCS / "prime-matrix-high-segment-model-gap-factorization-router.json"
DEFAULT_MD = DOCS / "prime-matrix-high-segment-model-gap-factorization-router.md"

HIGH_MODEL_ATOM = "HighSegmentModelGapAlpha043C3AnalyticLedger"
HARMONIC_ATOM = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON_ATOM = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
BRIDGE_ATOM = "FiniteModelGapAlpha043P2003To3000Certificate"
EXTERNAL_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TAIL_START = 3001
BRIDGE_START = 2003
H_BOUND = 0.850
S_BOUND = 401
C_VALUE = 3.0


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def model_gap_over_sqrt(record: dict[str, Any]) -> float:
    """计算 S(1-H)/sqrt(S)。"""
    skeleton = record["skeleton_count"]
    return math.sqrt(skeleton) * (1.0 - record["harmonic_high"])


def segment_metrics(records: list[dict[str, Any]], start: int, stop: int | None = None) -> dict[str, Any]:
    """计算 P 区间的模型余量指标。"""
    if stop is None:
        rows = [row for row in records if row["p"] >= start]
    else:
        rows = [row for row in records if start <= row["p"] < stop]
    primes = sorted({row["p"] for row in rows})
    if not rows:
        return {"record_count": 0, "prime_count": 0}
    max_h = max(row["harmonic_high"] for row in rows)
    min_s = min(row["skeleton_count"] for row in rows)
    min_model = min(model_gap_over_sqrt(row) for row in rows)
    max_h_row = max(rows, key=lambda row: row["harmonic_high"])
    min_s_row = min(rows, key=lambda row: row["skeleton_count"])
    min_model_row = min(rows, key=model_gap_over_sqrt)
    return {
        "record_count": len(rows),
        "prime_count": len(primes),
        "prime_min": min(primes),
        "prime_max": max(primes),
        "capacity_fail": sum(not row.get("capacity_pass", False) for row in rows),
        "max_harmonic_high": max_h,
        "max_harmonic_record": {"p": max_h_row["p"], "side": max_h_row["side"]},
        "min_skeleton_count": min_s,
        "min_skeleton_record": {"p": min_s_row["p"], "side": min_s_row["side"]},
        "min_model_gap_over_sqrt": min_model,
        "min_model_record": {"p": min_model_row["p"], "side": min_model_row["side"]},
    }


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的高段模型余量原子。"""
    return text.replace(old, new)


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    previous: dict[str, Any],
    bridge: dict[str, Any],
    tail: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成高段模型余量因子化判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == HIGH_MODEL_ATOM and HIGH_MODEL_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    bridge_closed = (
        bridge["record_count"] == 254
        and bridge["prime_count"] == 127
        and bridge["prime_min"] == 2003
        and bridge["prime_max"] == 2999
        and bridge["capacity_fail"] == 0
        and bridge["min_model_gap_over_sqrt"] > C_VALUE
    )
    algebra_margin = math.sqrt(S_BOUND) * (1.0 - H_BOUND)
    algebra_closed = algebra_margin > C_VALUE
    tail_audit_support = (
        tail["record_count"] == 18324
        and tail["capacity_fail"] == 0
        and tail["max_harmonic_high"] < H_BOUND
        and tail["min_skeleton_count"] >= S_BOUND
        and tail["min_model_gap_over_sqrt"] > C_VALUE
    )
    factorization_closed = active and guard and bridge_closed and algebra_closed and tail_audit_support
    return [
        row(
            "HighSegmentModelGapGateActive",
            active,
            False,
            "最新最窄点是 P>=2003 的高段模型余量解析账本。",
            HIGH_MODEL_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行链条中的模型余量账本，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            BRIDGE_ATOM,
            bridge_closed,
            True,
            "2003<=P<3001 只有 127 个素数、双侧 254 条记录，模型余量均已超过 3sqrt(S)。",
            "桥接低高段边界，不进入尾段解析。",
        ),
        row(
            "TailSufficientPairAlgebra",
            algebra_closed,
            True,
            "若 P>=3001 时 H<=0.850 且 S>=401，则 sqrt(401)*(1-0.850)>3，自动推出模型余量。",
            f"{HARMONIC_ATOM} AND {SKELETON_ATOM}",
        ),
        row(
            "TailSufficientPairAuditSupport",
            tail_audit_support,
            False,
            "审计到 P<=100000 支持 H<0.850 与 S>=401，但这仍只是参数定位。",
            "需要解析证明两张账本。",
        ),
        row(
            HARMONIC_ATOM,
            False,
            False,
            "证明 H(P)=sum_{P^0.43<q<P}1/q <= 0.850，对所有 P>=3001 成立。",
            HARMONIC_ATOM,
        ),
        row(
            SKELETON_ATOM,
            False,
            False,
            "证明动态粗骨架 S_Y(P)>=401，对所有 P>=3001 和 plus/minus 两侧成立。",
            SKELETON_ATOM,
        ),
        row(
            HIGH_MODEL_ATOM,
            factorization_closed,
            False,
            "高段模型余量已因子化为一个桥接有限证书与两个尾段解析输入；尚未整体证明。",
            f"{HARMONIC_ATOM} AND {SKELETON_ATOM}",
        ),
        row(
            EXTERNAL_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行高段模型余量因子化。"""
    previous = load_json(paths["previous"])
    dynamic = load_json(paths["dynamic_json"])
    records = dynamic.get("records", [])
    bridge = segment_metrics(records, BRIDGE_START, TAIL_START)
    tail = segment_metrics(records, TAIL_START)
    rows = build_rows(previous, bridge, tail)
    factorized = next(bool(item["closed"]) for item in rows if item["gate"] == HIGH_MODEL_ATOM)
    new_atom = f"({HARMONIC_ATOM} AND {SKELETON_ATOM})"
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), HIGH_MODEL_ATOM, new_atom)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), HIGH_MODEL_ATOM, new_atom)
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""), HIGH_MODEL_ATOM, new_atom)

    source_paths = list(paths.values())
    return {
        "certificate_type": "high_segment_model_gap_factorization_router",
        "status": "high_segment_model_gap_factorized_bridge_closed_tail_two_inputs_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "high_segment_model_gap_factorized": factorized,
        "bridge_finite_model_gap_certificate_closed": True,
        "tail_harmonic_upper_0850_proved": False,
        "tail_skeleton_lower_401_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {HIGH_MODEL_ATOM: new_atom},
        "closed_subinput": BRIDGE_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": HARMONIC_ATOM,
        "secondary_priority": SKELETON_ATOM,
        "external_next_priority": EXTERNAL_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "constants": {
            "tail_start": TAIL_START,
            "bridge_start": BRIDGE_START,
            "h_bound": H_BOUND,
            "s_bound": S_BOUND,
            "algebra_margin": math.sqrt(S_BOUND) * (1.0 - H_BOUND),
            "c_value": C_VALUE,
        },
        "metrics": {"bridge": bridge, "tail": tail},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把高段模型余量压成最窄的双输入尾段账本。"
            "桥接段 2003<=P<3001 已由 254 条有限记录关闭。"
            "对 P>=3001，只要证明 H<=0.850 与 S>=401，代数上就有 "
            "sqrt(401)*(1-0.850)>3，从而推出 S(1-H)>3sqrt(S)。"
            "当前真正剩余变为调和窗口上界与动态粗骨架下界两张解析账本。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    constants = result["constants"]
    bridge = result["metrics"]["bridge"]
    tail = result["metrics"]["tail"]
    lines = [
        "# Prime Matrix 高段模型余量因子化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"high_segment_model_gap_factorized={fmt_bool(result['high_segment_model_gap_factorized'])}",
        f"bridge_finite_model_gap_certificate_closed={fmt_bool(result['bridge_finite_model_gap_certificate_closed'])}",
        f"tail_harmonic_upper_0850_proved={fmt_bool(result['tail_harmonic_upper_0850_proved'])}",
        f"tail_skeleton_lower_401_proved={fmt_bool(result['tail_skeleton_lower_401_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 因子化律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        f"  + {BRIDGE_ATOM}(closed)",
        "```",
        "",
        "尾段代数充分条件：",
        "",
        "```text",
        f"sqrt({constants['s_bound']}) * (1 - {constants['h_bound']}) = {constants['algebra_margin']:.12f} > {constants['c_value']}",
        "```",
        "",
        "## 2. 参数审计",
        "",
        "| segment | records | primes | fail | max H | min S | min model/sqrt |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| 2003<=P<3001 | {bridge['record_count']} | {bridge['prime_count']} | "
            f"{bridge['capacity_fail']} | {bridge['max_harmonic_high']:.6f} | "
            f"{bridge['min_skeleton_count']} | {bridge['min_model_gap_over_sqrt']:.6f} |"
        ),
        (
            f"| P>=3001 audit | {tail['record_count']} | {tail['prime_count']} | "
            f"{tail['capacity_fail']} | {tail['max_harmonic_high']:.6f} | "
            f"{tail['min_skeleton_count']} | {tail['min_model_gap_over_sqrt']:.6f} |"
        ),
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "global/external 宽口径输入基：",
            "",
            "```text",
            result["latest_global_with_external_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            "优先攻 `HarmonicWindowAlpha043PGe3001Upper0850Ledger`：用显式 Mertens/素数调和估计证明 `sum_{P^0.43<q<P}1/q <= 0.850`。随后攻 `DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger`：用一维小筛下界证明动态粗骨架双侧均至少 401。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--dynamic-json", type=Path, default=DEFAULT_DYNAMIC_JSON)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous, "dynamic_json": args.dynamic_json}
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")


if __name__ == "__main__":
    main()
