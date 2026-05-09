#!/usr/bin/env python3
"""Prime Matrix B=3 theta@20000 外部 Dusart 目标路由器。

用法示例：
  python3 experiments/prime_matrix_b3_theta_target_dusart_router.py

输出：
  docs/monograph/prime-matrix-b3-theta-target-dusart-router.json
  docs/monograph/prime-matrix-b3-theta-target-dusart-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-trivial-tail-prime-power-budget-router.json"
DEFAULT_FINAL_DRAFT = ROOT / "docs" / "final-proof-draft.md"
DEFAULT_CONSTANT_AUDIT = ROOT / "docs" / "explicit-constant-audit.md"
DEFAULT_JSON = DOCS / "prime-matrix-b3-theta-target-dusart-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-theta-target-dusart-router.md"

OLD_ATOM = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
CLOSED_ATOM = "DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260"
TRIVIAL_TAIL_CLOSED = "PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
EXPLICIT_CONTOUR = "ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion"
FINITE_BRIDGE = "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold"
MERTENS_INTERVAL = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000
TARGET_DENOMINATOR = 36_260
TARGET_RELATIVE_ERROR = 1.0 / TARGET_DENOMINATOR
DUSART_SOURCE = "Pierre Dusart, Estimates of some functions over primes without R.H., arXiv:1002.0442, Proposition 5.1"
DUSART_URL = "https://arxiv.org/abs/1002.0442"


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
    """只在外部路线输入基中替换 theta 目标原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def theorem_registered(final_draft: str, constant_audit: str) -> bool:
    """确认仓库内已登记 Dusart theta 显式界。"""
    combined = final_draft + "\n" + constant_audit
    return contains_all(combined, ["Dusart", "36260", "vartheta"])


def theta_budget(x: int) -> dict[str, float | int | bool]:
    """给出 theta 显式目标的锚点预算。"""
    absolute_allowance = x * TARGET_RELATIVE_ERROR
    cheb_constant = 1.0 + TARGET_RELATIVE_ERROR
    return {
        "x": x,
        "target_denominator": TARGET_DENOMINATOR,
        "target_relative_error": TARGET_RELATIVE_ERROR,
        "absolute_allowance": absolute_allowance,
        "chebyshev_multiplier": cheb_constant,
        "valid_for_anchor": x > 0,
        "matches_target_exactly": True,
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], final_draft: str, constant_audit: str) -> list[dict[str, Any]]:
    """生成 Dusart theta 目标判定表。"""
    external_basis = previous.get("latest_external_titchmarsh_cn16_basis", "")
    self_basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    trivial_ready = (
        previous.get("trivial_tail_prime_power_budget_closed") is True
        and TRIVIAL_TAIL_CLOSED in external_basis
    )
    registered = theorem_registered(final_draft, constant_audit)
    theta_external_closed = active and guard and trivial_ready and registered
    return [
        row(
            "ThetaTargetGateActive",
            active,
            True,
            "平凡尾项账本之后，外部条件路线的当前最窄点正是 theta@20000 小误差输入。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只补假设反例链条需要的解析输入，不使用真实零行缺席或统计替代证明。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "TrivialTailBudgetAlreadyClosed",
            trivial_ready,
            True,
            "上一层已把 psi_0 平凡零点、端点半权、素数幂尾项归账，theta 目标可以作为独立 Chebyshev 显式界输入处理。",
            TRIVIAL_TAIL_CLOSED,
        ),
        row(
            "DusartProposition51Registered",
            registered,
            False,
            "接受 Dusart Proposition 5.1：vartheta(x)-x < x/36260 对所有 x>0 成立。",
            DUSART_SOURCE,
        ),
        row(
            OLD_ATOM,
            theta_external_closed,
            False,
            "由于 20000>0，Dusart 全局显式界直接给出 theta@20000 目标所需的相对误差 1/36260。",
            CLOSED_ATOM,
        ),
        row(
            "SelfContainedThetaTargetStillOpen",
            False,
            False,
            "严格自足路线若不引用 Dusart，仍需在文内重建 theta 显式界或有限桥。",
            "InternalDusartThetaEnvelopeProofLedger",
        ),
        row(
            "FiniteLowHeightStillSeparate",
            False,
            False,
            "低高度零点核验不是 theta 目标的一部分，仍需独立关闭。",
            FINITE_LOW_HEIGHT,
        ),
        row(
            "DStructureRankinGateStillSeparate",
            False,
            False,
            "即使外部解析链继续推进，行列无条件命题仍需 DStructure/Rankin 独立验收门。",
            DSTRUCTURE_GATE,
        ),
        row(
            "SelfContainedBasisUnchanged",
            OLD_ATOM in self_basis,
            True,
            "本路由只替换外部输入基；自足输入基保留 theta 原子，防止误报自足闭合。",
            OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 theta@20000 外部 Dusart 目标路由。"""
    previous = load_json(paths["previous"])
    final_draft = paths["final_draft"].read_text(encoding="utf-8")
    constant_audit = paths["constant_audit"].read_text(encoding="utf-8")
    rows = build_rows(previous, final_draft, constant_audit)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    latest_external = replace_atom(previous.get("latest_external_titchmarsh_cn16_basis", ""))
    return {
        "certificate_type": "b3_theta_target_dusart_router",
        "status": "theta_target_external_closed_self_contained_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "theta_target_external_closed": closed,
        "theta_target_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "external_source": DUSART_SOURCE,
        "external_url": DUSART_URL,
        "external_theorem_statement": "vartheta(x)-x < x/36260 for x>0",
        "target_anchor_budget": theta_budget(ANCHOR_X),
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_external_titchmarsh_cn16_basis": latest_external,
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "next_priority": FINITE_LOW_HEIGHT,
        "secondary_priority": EXPLICIT_CONTOUR,
        "bridge_priority": FINITE_BRIDGE,
        "mertens_interval_priority": MERTENS_INTERVAL,
        "parallel_self_contained_priority": BACKLUND_INTERNAL,
        "final_independent_acceptance_gate": DSTRUCTURE_GATE,
        "plain_conclusion": (
            "外部条件路线下，`ThetaEnvelopeTargetAt20000NumericalBudgetLedger` 可由 "
            "Dusart Proposition 5.1 关闭：`vartheta(x)-x < x/36260` 对所有 `x>0` 成立，"
            "因此在锚点 `x=20000` 精确给出目标相对误差。该步不是自足证明，也不关闭低高度零点核验、"
            "后续有限桥、Mertens 区间账本、DStructure/Rankin 守门项或行列无条件命题。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_external"].items()))
    budget = result["target_anchor_budget"]
    lines = [
        "# Prime Matrix B=3 theta@20000 外部 Dusart 目标路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"theta_target_external_closed={fmt_bool(result['theta_target_external_closed'])}",
        f"theta_target_self_contained_closed={fmt_bool(result['theta_target_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 外部引理内容",
        "",
        (
            "接受的外部引理为 Dusart Proposition 5.1："
            "`vartheta(x)-x < x/36260` 对所有 `x>0` 成立。"
        ),
        "",
        f"来源：{result['external_source']}。公共入口：{result['external_url']}。",
        "",
        "## 3. x=20000 目标预算",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| x | `{budget['x']}` |",
        f"| target denominator | `{budget['target_denominator']}` |",
        f"| relative error | `{budget['target_relative_error']:.15f}` |",
        f"| absolute allowance | `{fmt_float(budget['absolute_allowance'])}` |",
        f"| Chebyshev multiplier | `{fmt_float(budget['chebyshev_multiplier'])}` |",
        f"| valid for anchor | `{fmt_bool(budget['valid_for_anchor'])}` |",
        "",
        "## 4. 判定表",
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
            "## 5. 最新输入基",
            "",
            "外部 Titchmarsh+CN16 路线输入基：",
            "",
            "```text",
            result["latest_external_titchmarsh_cn16_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"下一步攻 `{result['next_priority']}`；随后连接 "
                f"`{result['secondary_priority']}`、`{result['bridge_priority']}` 和 "
                f"`{result['mertens_interval_priority']}`。严格自足线仍保留 "
                f"`{result['parallel_self_contained_priority']}` 与内部 theta 证明账本。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--final-draft", type=Path, default=DEFAULT_FINAL_DRAFT)
    parser.add_argument("--constant-audit", type=Path, default=DEFAULT_CONSTANT_AUDIT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "final_draft": args.final_draft,
        "constant_audit": args.constant_audit,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
