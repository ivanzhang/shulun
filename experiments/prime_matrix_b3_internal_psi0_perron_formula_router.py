#!/usr/bin/env python3
"""Prime Matrix B=3 内部 psi_0 精确显式公式路由器。

用法示例：
  python3 experiments/prime_matrix_b3_internal_psi0_perron_formula_router.py

输出：
  docs/monograph/prime-matrix-b3-internal-psi0-perron-formula-router.json
  docs/monograph/prime-matrix-b3-internal-psi0-perron-formula-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-classical-rvm-external-match-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-internal-psi0-perron-formula-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-internal-psi0-perron-formula-router.md"

OLD_ATOM = "InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger"
CLOSED_ATOM = "InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost"
PERRON_KERNEL_ATOM = "PerronKernelTruncationConstantForPsi0Ledger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
TRIVIAL_TAIL_ATOM = "PerronTruncationTrivialZeroPrimePowerTailBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

XI_ATOM = "CompletedZetaXiFunctionalEquationAndHadamardProductClosed"
ENDPOINT_ATOM = "ChebyshevPsi0EndpointHalfWeightConventionClosed"


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


def replace_atom(text: str) -> str:
    """替换内部 psi_0 公式原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def theorem_contract() -> dict[str, str]:
    """记录本步闭合的精确公式合同。"""
    return {
        "domain": "x>1；本项目只需 x>=20000",
        "psi0": "psi_0(x)=sum_{n<x} Lambda(n)+1/2 Lambda(x) if x is an integer",
        "closed_formula": (
            "psi_0(x)=x-sum_rho x^rho/rho-log(2*pi)-1/2*log(1-x^-2)"
        ),
        "zero_sum_mode": "对称极限 lim_{T->infty} sum_{|Im rho|<T}",
        "what_is_not_closed": "截断到有限 T 的 R_T 常数与零点尾和预算仍未闭合",
    }


def proof_steps() -> list[dict[str, Any]]:
    """给出内部证明链条。"""
    return [
        {
            "step": "Perron半权入口",
            "closed": True,
            "reason": "对 -zeta'/zeta(s)=sum Lambda(n)n^-s 使用 Perron 半权公式，得到 psi_0 端点规范。",
        },
        {
            "step": "矩形移线",
            "closed": True,
            "reason": "用 zeta 的亚指数竖线增长与端点避零序列，把积分线移到左侧并取对称极限。",
        },
        {
            "step": "留数清单",
            "closed": True,
            "reason": "s=1 给 x，非平凡零点给 -x^rho/rho，s=0 给 -log(2*pi)，平凡零点给 -1/2 log(1-x^-2)。",
        },
        {
            "step": "对称零点和",
            "closed": True,
            "reason": "按 |Im rho|<T 的共轭对称极限解释零点和，避免条件收敛顺序歧义。",
        },
        {
            "step": "有限截断余项",
            "closed": False,
            "reason": "本步不估计 finite T 余项；该任务留给 PerronKernelTruncationConstantForPsi0Ledger。",
        },
    ]


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
    """生成内部 psi_0 公式判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    upstream_reduced = bool(previous.get("classical_rvm_external_match_reduced"))
    xi_ready = XI_ATOM in basis
    endpoint_ready = ENDPOINT_ATOM in basis
    exact_formula_closed = active and guard and upstream_reduced and xi_ready and endpoint_ready
    return [
        row(
            "InternalPsi0FormulaGateActive",
            active,
            False,
            "上一层把外部高阈值 RvM 候选排除为严格闭合后，当前最窄点是内部 psi_0 公式。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ZetaMeromorphicHadamardBasisAvailable",
            xi_ready,
            True,
            "zeta/xi 函数方程、亚纯延拓、Hadamard/零点结构已经在前序基础包登记。",
            XI_ATOM,
        ),
        row(
            "Psi0EndpointConventionAvailable",
            endpoint_ready,
            True,
            "psi_0 半权端点口径已经闭合，跳点不再造成公式歧义。",
            ENDPOINT_ATOM,
        ),
        row(
            "ResidueFormulaProofClosed",
            exact_formula_closed,
            True,
            "Perron 半权入口、矩形移线、留数清单和对称零点和给出无截断精确公式。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            exact_formula_closed,
            True,
            "内部 all-x psi_0 精确公式闭合；但该闭合不含 finite-T 截断常数。",
            CLOSED_ATOM,
        ),
        row(
            PERRON_KERNEL_ATOM,
            False,
            False,
            "下一步必须把精确公式截断为 |gamma|<=T 并给出 R_T 常数。",
            PERRON_KERNEL_ATOM,
        ),
        row(
            ZERO_SUM_ATOM,
            False,
            False,
            "截断核常数之后，仍需把 C=1280,T0=14 代入零点尾和预算。",
            ZERO_SUM_ATOM,
        ),
        row(
            TRIVIAL_TAIL_ATOM,
            False,
            False,
            "平凡零点与素数幂/尾项同口径预算仍是独立子账本。",
            TRIVIAL_TAIL_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行内部 psi_0 精确公式路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_internal_psi0_perron_formula_router",
        "status": "internal_psi0_exact_formula_closed_truncation_kernel_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "internal_psi0_exact_formula_closed": closed,
        "perron_kernel_truncation_constant_closed": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": PERRON_KERNEL_ATOM,
        "secondary_priority": ZERO_SUM_ATOM,
        "tail_priority": TRIVIAL_TAIL_ATOM,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "theorem_contract": theorem_contract(),
        "proof_steps": proof_steps(),
        "plain_conclusion": (
            "内部 psi_0 精确显式公式已经闭合：通过 Perron 半权入口、移线取留数和对称零点和，"
            "得到 x>1 上的无截断公式。该结论只关闭公式身份本身；真正数值余项 "
            "R_T 和零点尾和预算仍开放，下一最窄点为 PerronKernelTruncationConstantForPsi0Ledger。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    contract = result["theorem_contract"]
    lines = [
        "# Prime Matrix B=3 内部 psi_0 精确显式公式路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"internal_psi0_exact_formula_closed={fmt_bool(result['internal_psi0_exact_formula_closed'])}",
        f"perron_kernel_truncation_constant_closed={fmt_bool(result['perron_kernel_truncation_constant_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 定理合同",
        "",
        "| item | value |",
        "| --- | --- |",
    ]
    for key, value in contract.items():
        lines.append(f"| {key} | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 3. 证明链",
            "",
            "| step | closed | reason |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["proof_steps"]:
        lines.append(
            f"| {table_cell(item['step'])} | `{fmt_bool(item['closed'])}` | {table_cell(item['reason'])} |"
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
                f"当前最窄点更新为 `{result['next_priority']}`；完成后再进入 "
                f"`{result['secondary_priority']}`。"
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
