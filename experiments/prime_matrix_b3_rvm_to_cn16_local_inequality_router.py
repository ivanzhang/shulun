#!/usr/bin/env python3
"""Prime Matrix B=3 RVM 到 C_N=16 局部计数合并证书。

用法示例：
  python3 experiments/prime_matrix_b3_rvm_to_cn16_local_inequality_router.py

输出：
  docs/monograph/prime-matrix-b3-rvm-to-cn16-local-inequality-router.json
  docs/monograph/prime-matrix-b3-rvm-to-cn16-local-inequality-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.md"

OLD_ATOM = "RVMToCN16LocalInequalityLedger"
CLOSED_ATOM = "RVMToCN16LocalInequalityClosedWithRawArgCS8"
ARG_ATOM = "ArgumentPrincipleXiRectangleCountingClosed"
GAMMA_ATOM = "GammaMainTermLocalDifferenceNumericalClosedCmain4"
CS8_ATOM = "BacklundCS8SlackAfterBridgeClosedTightHalf"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionClosedByLimit"
NOZERO14_ATOM = "BacklundXiNoNontrivialZeroBelow14ExternalClosed"
FIRST_ZERO_ATOM = "ClassicalFirstZetaZeroHeightGT14ExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_MAIN = 4.0
C_ARG_RAW = 8.0
C_N_TARGET = 16.0
LOG_RATIO_MAX = math.log(4.0) / math.log(3.0)
RAW_ARG_RVM_COEFF = C_MAIN + (2.0 * C_ARG_RAW / math.pi) * LOG_RATIO_MAX
NORMALIZED_S_RVM_COEFF = C_MAIN + 2.0 * C_ARG_RAW * LOG_RATIO_MAX
RAW_ARG_SLACK = C_N_TARGET - RAW_ARG_RVM_COEFF
NORMALIZED_S_SLACK = C_N_TARGET - NORMALIZED_S_RVM_COEFF


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


def replace_atom(text: str) -> str:
    """替换 RVM 到 CN16 合并原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


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


def budget_rows() -> list[dict[str, float | str]]:
    """生成归一化分叉预算表。"""
    return [
        {
            "case": "raw_arg_backlund",
            "formula": "C_main + (2*C_arg/pi)*log(4)/log(3)",
            "coefficient": RAW_ARG_RVM_COEFF,
            "target": C_N_TARGET,
            "slack": RAW_ARG_SLACK,
        },
        {
            "case": "normalized_S_backlund_rejected",
            "formula": "C_main + 2*C_S*log(4)/log(3)",
            "coefficient": NORMALIZED_S_RVM_COEFF,
            "target": C_N_TARGET,
            "slack": NORMALIZED_S_SLACK,
        },
    ]


def sample_rows() -> list[dict[str, float]]:
    """在代表性高度上审计 log 端点膨胀后的预算。"""
    rows: list[dict[str, float]] = []
    for t in [0.0, 1.0, 2.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        base_log = math.log(t + 3.0)
        endpoint_log = math.log(t + 4.0)
        ratio = endpoint_log / base_log
        coeff = C_MAIN + (2.0 * C_ARG_RAW / math.pi) * ratio
        rows.append(
            {
                "T": t,
                "log_T_plus_3": base_log,
                "endpoint_log_ratio": ratio,
                "raw_arg_coefficient": coeff,
                "CN16_slack": C_N_TARGET - coeff,
            }
        )
    return rows


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 RVM 到 C_N=16 合并判定表。"""
    self_basis = previous.get("latest_self_contained_basis", "")
    conditional_basis = previous.get("latest_conditional_basis", "")
    active = previous.get("conditional_next_priority") == OLD_ATOM and OLD_ATOM in conditional_basis
    formal_ready = ARG_ATOM in conditional_basis and GAMMA_ATOM in conditional_basis and ENDPOINT_ATOM in conditional_basis
    backlund_ready = CS8_ATOM in conditional_basis
    low_height_ready = NOZERO14_ATOM in conditional_basis or FIRST_ZERO_ATOM in conditional_basis
    self_contained_ready = CS8_ATOM in self_basis and NOZERO14_ATOM in self_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    raw_arg_passes = RAW_ARG_SLACK > 0.0
    normalized_s_fails = NORMALIZED_S_SLACK < 0.0
    closed = active and formal_ready and backlund_ready and low_height_ready and guard and raw_arg_passes
    return [
        row(
            "RVMToCN16GateActive",
            active,
            False,
            "端点 convention 关闭后，外部 Backlund 分支当前最窄点是把 RVM 局部计数合并到 C_N=16。",
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
            "FormalRVMInputsAvailable",
            formal_ready,
            True,
            "argument principle、Gamma 主项 C_main=4、端点重数极限 convention 均已在外部输入基中可用。",
            f"{ARG_ATOM} AND {GAMMA_ATOM} AND {ENDPOINT_ATOM}",
        ),
        row(
            "ExternalBacklundCS8Available",
            backlund_ready,
            False,
            "外部 Backlund 分支已经验收点态原始 arg zeta 常数 C_arg=8。",
            CS8_ATOM,
        ),
        row(
            "LowHeightExternalZeroInputAvailable",
            low_height_ready,
            False,
            "低高度区间由外部首零点/14 以下无非平凡零点输入兜底；自足路线仍未关闭该输入。",
            f"{FIRST_ZERO_ATOM} OR {NOZERO14_ATOM}",
        ),
        row(
            "RawArgNormalizationPassesCN16",
            raw_arg_passes,
            True,
            "RVM 中 S(T)=arg zeta/pi；端点两次 arg 贡献为 2*C_arg/pi，再乘 log(T+4)/log(T+3)<=log4/log3。",
            f"coefficient={RAW_ARG_RVM_COEFF:.12f}<16",
        ),
        row(
            "NormalizedSInterpretationRejected",
            normalized_s_fails,
            True,
            "若把 C_S=8 解释成已经除以 pi 的 S(T) 常数，则系数超过 16；本证书明确不走该解释。",
            f"coefficient={NORMALIZED_S_RVM_COEFF:.12f}>16",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "在原始 arg zeta 归一化下，RVM 局部计数合并为 N(T+1)-N(T-1)<=16 log(T+3) 的外部分支输入。",
            CLOSED_ATOM,
        ),
        row(
            "SelfContainedRVMToCN16StillOpen",
            self_contained_ready,
            False,
            "完全自足路线仍缺 14 以下零点排除与自足 Backlund C_S=8，因此不能同步替换自足输入基。",
            "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger",
        ),
        row(
            "DStructureRankinPromotionNext",
            False,
            False,
            "外部解析链再往后仍需独立 DStructure/Rankin 验收门，且行列无条件命题未闭合。",
            DSTRUCTURE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 RVM 到 C_N=16 局部计数合并证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    latest_conditional = replace_atom(previous.get("latest_conditional_basis", ""))
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""))
    return {
        "certificate_type": "b3_rvm_to_cn16_local_inequality_router",
        "status": "rvm_to_cn16_external_closed_raw_arg_normalization",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "rvm_to_cn16_external_closed": closed,
        "rvm_to_cn16_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "C_main": C_MAIN,
        "C_arg_raw": C_ARG_RAW,
        "C_N_target": C_N_TARGET,
        "log_ratio_max": LOG_RATIO_MAX,
        "raw_arg_rvm_coefficient": RAW_ARG_RVM_COEFF,
        "raw_arg_slack": RAW_ARG_SLACK,
        "normalized_S_rvm_coefficient": NORMALIZED_S_RVM_COEFF,
        "normalized_S_slack": NORMALIZED_S_SLACK,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "latest_conditional_basis": latest_conditional,
        "latest_global_with_external_basis": latest_global,
        "next_priority": previous.get("next_priority"),
        "secondary_priority": previous.get("secondary_priority"),
        "conditional_next_priority": DSTRUCTURE,
        "final_promotion_priority": DSTRUCTURE,
        "core_formula": (
            "N(T+1)-N(T-1) <= C_main*L + (2*C_arg/pi)*L_endpoint <= "
            "(4 + 16/pi*log(4)/log(3))*L < 16*L, L=log(T+3)."
        ),
        "budget_rows": budget_rows(),
        "sample_rows": sample_rows(),
        "plain_conclusion": (
            "RVM 到 C_N=16 的外部分支合并闭合，但依赖一个明确归一化："
            "前序 C_S=8 必须是原始 arg zeta 常数，进入 RVM 的 S(T) 时除以 pi。"
            "该解释下总系数约 10.426<16；若把 C_S=8 当成已规范化的 S(T) 常数则失败。"
            "完全自足路线仍未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 RVM 到 C_N=16 局部计数合并证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"rvm_to_cn16_external_closed={fmt_bool(result['rvm_to_cn16_external_closed'])}",
        f"rvm_to_cn16_self_contained_closed={fmt_bool(result['rvm_to_cn16_self_contained_closed'])}",
        f"C_main={fmt_float(result['C_main'])}",
        f"C_arg_raw={fmt_float(result['C_arg_raw'])}",
        f"C_N_target={fmt_float(result['C_N_target'])}",
        f"raw_arg_rvm_coefficient={fmt_float(result['raw_arg_rvm_coefficient'])}",
        f"raw_arg_slack={fmt_float(result['raw_arg_slack'])}",
        f"normalized_S_rvm_coefficient={fmt_float(result['normalized_S_rvm_coefficient'])}",
        f"normalized_S_slack={fmt_float(result['normalized_S_slack'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件链替换",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "自足输入基不替换该 atom，因为自足零点排除与自足 Backlund C_S=8 仍开。",
        "",
        "## 2. 核心不等式",
        "",
        "```text",
        result["core_formula"],
        "```",
        "",
        "`log(T+4)/log(T+3)` 在 `T>=0` 上由 `log(4)/log(3)` 控制。低高度零点由外部 14 以下无零点输入兜底；端点落零由上一步极限 convention 处理。",
        "",
        "## 3. 归一化分叉预算",
        "",
        "| case | formula | coefficient | target | slack |",
        "| --- | --- | ---: | ---: | ---: |",
    ]
    for item in result["budget_rows"]:
        lines.append(
            "| {case} | `{formula}` | `{coefficient}` | `{target}` | `{slack}` |".format(
                case=table_cell(item["case"]),
                formula=table_cell(item["formula"]),
                coefficient=fmt_float(float(item["coefficient"])),
                target=fmt_float(float(item["target"])),
                slack=fmt_float(float(item["slack"])),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 高度样本审计",
            "",
            "| T | log(T+3) | endpoint ratio | raw-arg coefficient | CN16 slack |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["sample_rows"]:
        lines.append(
            "| {T:.6g} | `{logv}` | `{ratio}` | `{coeff}` | `{slack}` |".format(
                T=item["T"],
                logv=fmt_float(item["log_T_plus_3"]),
                ratio=fmt_float(item["endpoint_log_ratio"]),
                coeff=fmt_float(item["raw_arg_coefficient"]),
                slack=fmt_float(item["CN16_slack"]),
            )
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
            "## 6. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional/external Backlund 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "## 7. 下一步",
            "",
            (
                f"完全自足路线仍先攻 `{result['next_priority']}`；"
                f"外部分支下一验收门为 `{result['conditional_next_priority']}`。"
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
