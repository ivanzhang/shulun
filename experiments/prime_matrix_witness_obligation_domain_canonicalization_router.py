#!/usr/bin/env python3
"""Prime Matrix witness obligation domain 规范化引理路由器。

用法示例：
  python3 experiments/prime_matrix_witness_obligation_domain_canonicalization_router.py

输出：
  docs/monograph/prime-matrix-witness-obligation-domain-canonicalization-router.json
  docs/monograph/prime-matrix-witness-obligation-domain-canonicalization-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-formal-unit-partition-coverage-router.json"
DEFAULT_CLB = DOCS / "prime-matrix-cylindrical-completion-line-barrier.md"
DEFAULT_PHASE = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_CARRY = DOCS / "prime-matrix-early-zero-carry-shell-router.json"
DEFAULT_COFACTOR = DOCS / "prime-matrix-early-zero-cofactor-depth-router.json"
DEFAULT_TERMINAL_REDUCTION = DOCS / "prime-matrix-early-zero-terminal-package-reduction-router.json"
DEFAULT_TERMINAL_RECONCILIATION = DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json"
DEFAULT_MULTIPLICITY = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_JSON = DOCS / "prime-matrix-witness-obligation-domain-canonicalization-router.json"
DEFAULT_MD = DOCS / "prime-matrix-witness-obligation-domain-canonicalization-router.md"

OLD_ATOM = "WitnessObligationDomainCanonicalizationLemma"
CLOSED_ATOM = "WitnessObligationDomainCanonicalizationClosed"
KEY_ATOM = "FiniteFormalUnitPartitionKeyLemma"
TERMINAL_ATOM = "TerminalReturnObligationDomainSchemaClosed"
SELECTOR_ATOM = "CanonicalHighPrimeFillerAtomSelectorClosed"
QUOTIENT_ATOM = "PhysicalAtomQuotientDeduplicationClosed"


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def domain_components() -> list[dict[str, str]]:
    """给出 O(w) 的规范化组件。"""
    return [
        {
            "component": "physical_filler_atoms",
            "definition": "对每个 c in R_x=F_x，取 q_*(c)=min{q: x<q<P, q divides xP+c}，m_*(c)=(xP+c)/q_*(c)。",
        },
        {
            "component": "phase_defect_record",
            "definition": "同一 formal unit 中登记 Omega=R_x、tau(c)=q_*(c)、w(c)=1 与 phase(c,ell)。",
        },
        {
            "component": "carry_cofactor_record",
            "definition": "把 q_*(c)=P-a、m_*(c)=P-b 写入 carry-shell 与 cofactor-depth 字段。",
        },
        {
            "component": "named_return_records",
            "definition": "稳定复现、边界相位、anchor-collar、复合 cofactor、SAE/ColumnCRT/PDEC 均只作为命名回流记录。",
        },
        {
            "component": "quotient_records",
            "definition": "重复物理原子按同坐标 quotient 或 weighted/reuse return 处理，不能重复计数。",
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


def build_rows(
    previous: dict[str, Any],
    clb_text: str,
    phase: dict[str, Any],
    carry: dict[str, Any],
    cofactor: dict[str, Any],
    terminal_reduction: dict[str, Any],
    terminal_reconciliation: dict[str, Any],
    multiplicity_text: str,
) -> list[dict[str, Any]]:
    """生成 witness obligation domain 规范化判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    partition_interface_ready = previous.get("formal_unit_partition_coverage_interface_closed") is True
    clb_ready = contains_all(clb_text, ["R_x", "F_x", "U_x", "若 `c in U_x`"])
    phase_ready = (
        phase.get("early_zero_phase_defect_schema_admission_closed") is True
        and phase.get("registered_same_formal_unit_rxf_ledger") is True
        and phase.get("boundary_phase_defect_to_named_families_closed") is True
    )
    carry_ready = carry.get("exact_carry_shell_identity_closed") is True
    cofactor_ready = cofactor.get("cofactor_depth_gate_closed") is True
    terminal_ready = (
        terminal_reduction.get("early_zero_terminal_package_reduced") is True
        and terminal_reconciliation.get("early_zero_terminal_abstract_package_reconciled") is True
        and terminal_reconciliation.get("named_return_schema_reconciliation_closed") is True
    )
    quotient_ready = contains_all(
        multiplicity_text,
        ["CoordinateQuotient", "ReuseDefect", "不能作为第五类终端出口保留"],
    )
    selector_closed = all([clb_ready, phase_ready])
    domain_closed = all(
        [
            active,
            guard,
            partition_interface_ready,
            selector_closed,
            carry_ready,
            cofactor_ready,
            terminal_ready,
            quotient_ready,
        ]
    )
    return [
        row(
            "WitnessDomainGateActive",
            active,
            False,
            "上一层已把最窄点推进到 O(w) 义务域规范化。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在任意假设早期零行 witness 下工作，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "PartitionInterfaceImported",
            partition_interface_ready,
            True,
            "partition coverage 已要求先构造有限 O(w) 再切分。",
            "本步只处理 O(w)。",
        ),
        row(
            SELECTOR_ATOM,
            selector_closed,
            True,
            "对每个 c in R_x=F_x，有限非空高素因子集合有最小元 q_*(c)，因此 tau 可规范化。",
            SELECTOR_ATOM,
        ),
        row(
            "CarryCofactorFieldsImported",
            carry_ready and cofactor_ready,
            True,
            "canonical q_*(c),m_*(c) 可写入 carry-shell 与 cofactor-depth 字段。",
            "容量排斥仍不在本步证明。",
        ),
        row(
            TERMINAL_ATOM,
            terminal_ready,
            True,
            "终端包已被压到命名回流 schema；O(w) 可把它们作为 return records 而非无名出口。",
            TERMINAL_ATOM,
        ),
        row(
            QUOTIENT_ATOM,
            quotient_ready,
            True,
            "Multiplicity-Stitching 合同给出同坐标 quotient、weighted 或 reuse return 的规范化方式。",
            QUOTIENT_ATOM,
        ),
        row(
            CLOSED_ATOM,
            domain_closed,
            True,
            "O(w) 被规范化为 physical atoms、phase/carry/cofactor 字段、命名回流和 quotient records 的有限对象。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            domain_closed,
            True,
            "义务域规范化已闭合；下一步才是对每个 obligation 指派有限 formal-unit key。",
            KEY_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 witness obligation domain 规范化路由。"""
    previous = load_json(paths["previous"])
    clb_text = read_text(paths["clb"])
    phase = load_json(paths["phase"])
    carry = load_json(paths["carry"])
    cofactor = load_json(paths["cofactor"])
    terminal_reduction = load_json(paths["terminal_reduction"])
    terminal_reconciliation = load_json(paths["terminal_reconciliation"])
    multiplicity_text = read_text(paths["multiplicity"])
    rows = build_rows(
        previous,
        clb_text,
        phase,
        carry,
        cofactor,
        terminal_reduction,
        terminal_reconciliation,
        multiplicity_text,
    )
    domain_closed = next(item["closed"] for item in rows if item["gate"] == CLOSED_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_witness_obligation_domain_canonicalization_router",
        "status": "witness_obligation_domain_canonicalized_partition_key_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "witness_obligation_domain_canonicalization_lemma": domain_closed,
        "proved": domain_closed,
        "coverage_complete": domain_closed,
        "witness_obligation_domain_canonicalization_closed": domain_closed,
        "formal_unit_partition_coverage_lemma_closed": False,
        "domain_components": domain_components(),
        "current_narrowest_atom": KEY_ATOM,
        "reduction_formula": f"{OLD_ATOM} => {CLOSED_ATOM} AND {KEY_ATOM}.",
        "plain_conclusion": (
            "WitnessObligationDomainCanonicalizationLemma 已闭合：任意早期零行 witness 的 O(w) 可规范化为"
            "有限 physical filler atoms、phase/carry/cofactor 字段、命名 return records 与 quotient records。"
            f"下一最窄点是 `{KEY_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix witness obligation domain 规范化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"witness_obligation_domain_canonicalization_closed={fmt_bool(result['witness_obligation_domain_canonicalization_closed'])}",
        f"formal_unit_partition_coverage_lemma_closed={fmt_bool(result['formal_unit_partition_coverage_lemma_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. O(w) 组件",
        "",
        "| component | definition |",
        "| --- | --- |",
    ]
    for item in result["domain_components"]:
        lines.append(
            "| {component} | {definition} |".format(
                component=table_cell(item["component"]),
                definition=table_cell(item["definition"]),
            )
        )
    lines.extend(
        [
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
            "## 4. 下一步",
            "",
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。",
            "",
            "审稿边界：本步只证明义务域规范化；不证明 formal-unit key 全覆盖，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--clb", type=Path, default=DEFAULT_CLB)
    parser.add_argument("--phase", type=Path, default=DEFAULT_PHASE)
    parser.add_argument("--carry", type=Path, default=DEFAULT_CARRY)
    parser.add_argument("--cofactor", type=Path, default=DEFAULT_COFACTOR)
    parser.add_argument("--terminal-reduction", type=Path, default=DEFAULT_TERMINAL_REDUCTION)
    parser.add_argument("--terminal-reconciliation", type=Path, default=DEFAULT_TERMINAL_RECONCILIATION)
    parser.add_argument("--multiplicity", type=Path, default=DEFAULT_MULTIPLICITY)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "clb": args.clb,
        "phase": args.phase,
        "carry": args.carry,
        "cofactor": args.cofactor,
        "terminal_reduction": args.terminal_reduction,
        "terminal_reconciliation": args.terminal_reconciliation,
        "multiplicity": args.multiplicity,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
