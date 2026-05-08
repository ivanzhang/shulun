#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen 局部零点计数账本路由器。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_zero_count_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-zero-count-router.json
  docs/monograph/prime-matrix-b3-jensen-zero-count-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-gamma-digamma-clog-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-zero-count-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-zero-count-router.md"

OLD_ATOM = "JensenZeroCountingLocalNumericalLedger"
RVM_ATOM = "RiemannVonMangoldtExplicitLocalCountingLedger"
BOUNDARY_ATOM = "XiBoundaryLogMajorantNumericalLedger"
ANCHOR_ATOM = "JensenDiskLowerAnchorNumericalLedger"
LOCAL_ATOM = "LocalZeroCountCNConventionLedger"
PARTIAL_FRACTION_ATOM = "HadamardPartialFractionRemainderNumericalLedger"
AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

CN_CANDIDATE = 16.0


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


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replacement_pair() -> str:
    """写出 Jensen 局部计数的替换包。"""
    return f"({RVM_ATOM} AND {BOUNDARY_ATOM} AND {ANCHOR_ATOM} AND {LOCAL_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧 Jensen 计数原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def candidate_table() -> list[dict[str, float]]:
    """给 C_N=16 的候选预算生成审计表。"""
    rows: list[dict[str, float]] = []
    for t in [0.0, 1.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        lval = math.log(abs(t) + 3.0)
        rows.append(
            {
                "t": t,
                "log_t_plus_3": lval,
                "CN_log_bound": CN_CANDIDATE * lval,
                "rvm_main_local_scale": max(0.0, math.log(abs(t) + 3.0) / math.pi),
                "budget_ratio_to_rvm_scale": CN_CANDIDATE * math.pi,
            }
        )
    return rows


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Jensen 局部零点计数判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    gamma_closed = "GammaDigammaStirlingUniformNumericalClosedCgamma24" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and gamma_closed and guard
    return [
        row(
            "JensenZeroCountingGateActive",
            active,
            False,
            "上一层唯一内部最窄点是局部零点计数 N(t+1)-N(t-1)<=C_N log(|t|+3)。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "GammaComponentAvailable",
            gamma_closed,
            True,
            "Gamma/digamma 分量已由 C_gamma=24 支付。",
            "无 Gamma 项剩余。",
        ),
        row(
            "RiemannVonMangoldtLocalCountingMissing",
            False,
            False,
            "还需 argument principle/Riemann-von Mangoldt 显式版本给出局部零点主尺度。",
            RVM_ATOM,
        ),
        row(
            "XiBoundaryMajorantMissing",
            False,
            False,
            "若走 Jensen 圆盘法，还需 xi 在圆盘边界上的显式 log majorant。",
            BOUNDARY_ATOM,
        ),
        row(
            "JensenLowerAnchorMissing",
            False,
            False,
            "Jensen 法还需圆心处 xi 不过小的显式下界，避免只给上界无法计数。",
            ANCHOR_ATOM,
        ),
        row(
            "LocalCNConventionMissing",
            False,
            False,
            "还需把低高度分界、重零点计数 convention 和 C_N=16 聚合成统一账本。",
            LOCAL_ATOM,
        ),
        row(
            "JensenZeroCountingReducedToFourMicroLedgers",
            reduced,
            False,
            "旧 Jensen 局部计数原子已压成 RVM/边界上界/圆心下界/C_N convention 四包。",
            replacement_pair(),
        ),
        row(
            "HadamardPartialFractionRemainderStillNext",
            False,
            False,
            "局部零点计数完成后，才可处理 Hadamard 远零点与 1/rho 余项。",
            PARTIAL_FRACTION_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Jensen 局部零点计数路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(
        bool(item["closed"]) for item in rows if item["gate"] == "JensenZeroCountingReducedToFourMicroLedgers"
    )
    return {
        "certificate_type": "b3_jensen_zero_count_router",
        "status": "jensen_zero_count_reduced_to_four_micro_ledgers_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "jensen_zero_count_reduced": reduced,
        "jensen_zero_count_self_contained_proved": False,
        "C_N_candidate": CN_CANDIDATE,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": RVM_ATOM,
        "secondary_priority": BOUNDARY_ATOM,
        "tertiary_priority": ANCHOR_ATOM,
        "quaternary_priority": LOCAL_ATOM,
        "post_zero_count_priority": PARTIAL_FRACTION_ATOM,
        "post_partial_fraction_priority": AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "candidate_table": candidate_table(),
        "plain_conclusion": (
            "Jensen 局部零点计数尚未闭合；它已压成 Riemann-von Mangoldt/边界上界/圆心下界/"
            "C_N convention 四个微账本。候选 C_N=16 很保守，但必须由这些账本逐项支撑后才能使用。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen 局部零点计数账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"jensen_zero_count_reduced={fmt_bool(result['jensen_zero_count_reduced'])}",
        f"jensen_zero_count_self_contained_proved={fmt_bool(result['jensen_zero_count_self_contained_proved'])}",
        f"C_N_candidate={fmt_float(result['C_N_candidate'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 候选预算",
        "",
        "| t | log(|t|+3) | C_N log bound | local RVM scale | budget ratio |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["candidate_table"]:
        lines.append(
            "| {t:.6g} | `{logv}` | `{bound}` | `{scale}` | `{ratio}` |".format(
                t=item["t"],
                logv=fmt_float(item["log_t_plus_3"]),
                bound=fmt_float(item["CN_log_bound"]),
                scale=fmt_float(item["rvm_main_local_scale"]),
                ratio=fmt_float(item["budget_ratio_to_rvm_scale"]),
            )
        )
    lines.extend(
        [
            "",
            "候选 `C_N=16` 明显大于 RVM 局部主尺度，但仍不能代替显式 argument principle 或 Jensen 证明。",
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 5. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`、`{result['tertiary_priority']}`、"
                f"`{result['quaternary_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
