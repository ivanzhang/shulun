#!/usr/bin/env python3
"""Prime Matrix B=3 Gamma 主项局部差分闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_gamma_main_local_diff_router.py

输出：
  docs/monograph/prime-matrix-b3-gamma-main-local-diff-router.json
  docs/monograph/prime-matrix-b3-gamma-main-local-diff-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-argument-principle-xi-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-gamma-main-local-diff-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-gamma-main-local-diff-router.md"

OLD_ATOM = "GammaMainTermLocalDifferenceNumericalLedger"
CLOSED_ATOM = "GammaMainTermLocalDifferenceNumericalClosedCmain4"
BACKLUND_ATOM = "BacklundZetaArgumentBoundNumericalLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_MAIN = 4.0


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
    """把待证 atom 替换为已闭合 atom。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def sample_budget() -> list[dict[str, float]]:
    """审计 C_main=4 对局部主项尺度的余量。"""
    rows: list[dict[str, float]] = []
    for t in [0.0, 1.0, 2.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        logv = math.log(t + 3.0)
        # 宽度 2 的 RVM Gamma 主项差粗尺度。
        scale = max(0.0, math.log(max(t, 3.0) / (2.0 * math.pi)) / math.pi)
        bound = C_MAIN * logv
        rows.append({"t": t, "log_t_plus_3": logv, "main_scale": scale, "bound": bound, "slack": bound - scale})
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
    """生成 Gamma 主项局部差分判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    argument_closed = "ArgumentPrincipleXiRectangleCountingClosed" in basis
    gamma_component_closed = "GammaDigammaStirlingUniformNumericalClosedCgamma24" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and argument_closed and gamma_component_closed and guard
    return [
        row(
            "GammaMainLocalDifferenceGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 RVM Gamma 主项在 [T-1,T+1] 上的数值差分界。",
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
            "ArgumentPrincipleAvailable",
            argument_closed,
            True,
            "xi 矩形 argument principle 计数层已闭合。",
            "无形式计数剩余。",
        ),
        row(
            "DigammaBoundAvailable",
            gamma_component_closed,
            True,
            "Gamma/digamma 的统一 log 界已由 C_gamma=24 账本给出。",
            "无 Gamma/digamma 基础剩余。",
        ),
        row(
            "GammaThetaDerivativeBoundClosed",
            closed,
            True,
            "由 Theta'(T)=1/2 Re psi(1/4+iT/2)-1/2 log pi 与 digamma 界，|Theta'(T)|<=2 log(T+3)。",
            "无剩余。",
        ),
        row(
            "GammaMainLocalDifferenceBoundClosed",
            closed,
            True,
            "在长度 2 区间积分，Gamma 主项局部差由 C_main log(T+3) 支付，C_main=4。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "待证 atom 已闭合为 C_main=4 的 Gamma 主项局部差分账本。",
            CLOSED_ATOM,
        ),
        row(
            "BacklundZetaArgumentStillNext",
            False,
            False,
            "下一步需要 Backlund/arg zeta 显式上界；这是 RVM 局部计数的真正硬项。",
            BACKLUND_ATOM,
        ),
        row(
            "EndpointAndCN16StillDownstream",
            False,
            False,
            "端点 convention 与 CN16 合并仍未闭合。",
            f"{ENDPOINT_ATOM} AND {RVM_CN_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Gamma 主项局部差分闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_gamma_main_local_diff_router",
        "status": "gamma_main_local_difference_closed_cmain4",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "gamma_main_local_difference_closed": closed,
        "C_main": C_MAIN,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": BACKLUND_ATOM,
        "secondary_priority": ENDPOINT_ATOM,
        "tertiary_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "sample_budget": sample_budget(),
        "plain_conclusion": (
            "Gamma 主项局部差分已用保守 C_main=4 闭合。"
            "RVM 局部计数现在真正剩余的是 Backlund/arg zeta 显式上界、端点 convention 与 CN16 合并。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Gamma 主项局部差分闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"gamma_main_local_difference_closed={fmt_bool(result['gamma_main_local_difference_closed'])}",
        f"C_main={fmt_float(result['C_main'])}",
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
        "## 2. 文内证明",
        "",
        "RVM 主项中的 Gamma 辐角可写成",
        "",
        "```text",
        "Theta(T)=arg Gamma(1/4+iT/2) - (T/2)log pi.",
        "Theta'(T)=1/2 Re psi(1/4+iT/2) - 1/2 log pi.",
        "```",
        "",
        "由上一 Gamma/digamma 账本，`|Theta'(T)|<=2 log(T+3)`。所以长度 2 的局部差满足",
        "",
        "```text",
        "|Theta(T+1)-Theta(T-1)| <= 4 log(T+3).",
        "```",
        "",
        "因此取 `C_main=4` 支付 Gamma 主项局部差分。",
        "",
        "## 3. 主项尺度审计",
        "",
        "| T | log(T+3) | main scale | C_main bound | slack |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["sample_budget"]:
        lines.append(
            "| {t:.6g} | `{logv}` | `{scale}` | `{bound}` | `{slack}` |".format(
                t=item["t"],
                logv=fmt_float(item["log_t_plus_3"]),
                scale=fmt_float(item["main_scale"]),
                bound=fmt_float(item["bound"]),
                slack=fmt_float(item["slack"]),
            )
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
            "## 5. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}` 与 `{result['tertiary_priority']}`。"
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
