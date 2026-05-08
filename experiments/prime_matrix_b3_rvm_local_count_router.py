#!/usr/bin/env python3
"""Prime Matrix B=3 Riemann-von Mangoldt 局部计数路由器。

用法示例：
  python3 experiments/prime_matrix_b3_rvm_local_count_router.py

输出：
  docs/monograph/prime-matrix-b3-rvm-local-count-router.json
  docs/monograph/prime-matrix-b3-rvm-local-count-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-zero-count-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-rvm-local-count-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-rvm-local-count-router.md"

OLD_ATOM = "RiemannVonMangoldtExplicitLocalCountingLedger"
ARG_ATOM = "ArgumentPrincipleXiRectangleCountingLedger"
GAMMA_MAIN_ATOM = "GammaMainTermLocalDifferenceNumericalLedger"
BACKLUND_ATOM = "BacklundZetaArgumentBoundNumericalLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
BOUNDARY_ATOM = "XiBoundaryLogMajorantNumericalLedger"
ANCHOR_ATOM = "JensenDiskLowerAnchorNumericalLedger"
LOCAL_ATOM = "LocalZeroCountCNConventionLedger"
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
    """写出 RVM 局部计数的替换包。"""
    return f"({ARG_ATOM} AND {GAMMA_MAIN_ATOM} AND {BACKLUND_ATOM} AND {ENDPOINT_ATOM} AND {RVM_CN_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧 RVM 局部计数原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def gamma_main_budget_table() -> list[dict[str, float]]:
    """审计局部主项尺度和 CN=16 的余量。"""
    rows: list[dict[str, float]] = []
    for t in [2.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        logv = math.log(t + 3.0)
        # 宽度 2 的 RVM 主项差约 (1/pi) log(T/2pi)，这里仅作尺度审计。
        main_scale = max(0.0, math.log(max(t, 3.0) / (2.0 * math.pi)) / math.pi)
        rows.append(
            {
                "t": t,
                "log_t_plus_3": logv,
                "local_main_scale": main_scale,
                "CN16_bound": CN_CANDIDATE * logv,
                "slack": CN_CANDIDATE * logv - main_scale,
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
    """生成 RVM 局部计数判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    zeta_xi_ready = all(
        atom in basis
        for atom in [
            "ThetaMellinZetaContinuationFunctionalEquationClosed",
            "XiEntireOrderOneGrowthClosed",
            "HadamardFactorizationLogDerivativeClosed",
        ]
    )
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and guard and zeta_xi_ready
    return [
        row(
            "RVMLocalCountingGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Riemann-von Mangoldt 显式局部零点计数。",
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
            "ZetaXiAnalyticBasisAvailable",
            zeta_xi_ready,
            True,
            "theta-Mellin、xi 整函数与 Hadamard 层已闭合，可供 argument principle 使用。",
            "无基础解析剩余。",
        ),
        row(
            "ArgumentPrincipleXiRectangleCountingMissing",
            False,
            False,
            "还需把 xi 零点计数写成矩形边界上 Delta arg xi 的形式，并固定避零边界。",
            ARG_ATOM,
        ),
        row(
            "GammaMainTermLocalDifferenceMissing",
            False,
            False,
            "还需数值核算 Gamma/主项差分在 [T-1,T+1] 上为 O(log(T+3))。",
            GAMMA_MAIN_ATOM,
        ),
        row(
            "BacklundZetaArgumentBoundMissing",
            False,
            False,
            "还需 Backlund/arg zeta 显式上界，控制 S(T+1)-S(T-1)。",
            BACKLUND_ATOM,
        ),
        row(
            "EndpointMultiplicityConventionMissing",
            False,
            False,
            "还需端点落零、重零点和 T<2 低高度区间的计数 convention。",
            ENDPOINT_ATOM,
        ),
        row(
            "RVMToCN16LocalInequalityMissing",
            False,
            False,
            "还需把主项、arg 项和端点项合并为 N(T+1)-N(T-1)<=16 log(T+3)。",
            RVM_CN_ATOM,
        ),
        row(
            "RVMExplicitLocalCountingReducedToFiveMicroLedgers",
            reduced,
            False,
            "旧 RVM 局部计数原子已压成 argument principle、Gamma 主项、Backlund 辐角、端点 convention、CN16 转移五包。",
            replacement_pair(),
        ),
        row(
            "JensenBoundaryAndAnchorStillDownstream",
            False,
            False,
            "RVM 局部计数之外，Jensen 路线仍需 xi 边界上界、圆心下界和 CN convention。",
            f"{BOUNDARY_ATOM} AND {ANCHOR_ATOM} AND {LOCAL_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 RVM 局部计数路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "RVMExplicitLocalCountingReducedToFiveMicroLedgers"
    )
    return {
        "certificate_type": "b3_rvm_local_count_router",
        "status": "rvm_local_count_reduced_to_five_micro_ledgers_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "rvm_local_count_reduced": reduced,
        "rvm_local_count_self_contained_proved": False,
        "C_N_candidate": CN_CANDIDATE,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": ARG_ATOM,
        "secondary_priority": GAMMA_MAIN_ATOM,
        "tertiary_priority": BACKLUND_ATOM,
        "quaternary_priority": ENDPOINT_ATOM,
        "quinary_priority": RVM_CN_ATOM,
        "post_rvm_priority": BOUNDARY_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "gamma_main_budget_table": gamma_main_budget_table(),
        "plain_conclusion": (
            "RVM 显式局部计数尚未自足闭合，但已压成五个可审稿微账本。"
            "核心新增硬点不是主项，而是 Backlund/arg zeta 显式上界与端点 convention。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Riemann-von Mangoldt 局部计数路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"rvm_local_count_reduced={fmt_bool(result['rvm_local_count_reduced'])}",
        f"rvm_local_count_self_contained_proved={fmt_bool(result['rvm_local_count_self_contained_proved'])}",
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
        "## 2. 主项尺度审计",
        "",
        "| T | log(T+3) | local main scale | CN16 bound | slack |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["gamma_main_budget_table"]:
        lines.append(
            "| {t:.6g} | `{logv}` | `{main}` | `{bound}` | `{slack}` |".format(
                t=item["t"],
                logv=fmt_float(item["log_t_plus_3"]),
                main=fmt_float(item["local_main_scale"]),
                bound=fmt_float(item["CN16_bound"]),
                slack=fmt_float(item["slack"]),
            )
        )
    lines.extend(
        [
            "",
            "主项远小于 `16 log(T+3)`；真正需核验的是 `arg zeta` 与端点/低高度 convention。",
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
                f"`{result['quaternary_priority']}`、`{result['quinary_priority']}`。"
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
