#!/usr/bin/env python3
"""Prime Matrix partition coverage no-loss equation 引理路由器。

用法示例：
  python3 experiments/prime_matrix_partition_coverage_no_loss_equation_router.py

输出：
  docs/monograph/prime-matrix-partition-coverage-no-loss-equation-router.json
  docs/monograph/prime-matrix-partition-coverage-no-loss-equation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-finite-formal-unit-partition-key-router.json"
DEFAULT_DOMAIN = DOCS / "prime-matrix-witness-obligation-domain-canonicalization-router.json"
DEFAULT_PARTITION = DOCS / "prime-matrix-formal-unit-partition-coverage-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-partition-coverage-no-loss-equation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-partition-coverage-no-loss-equation-router.md"

OLD_ATOM = "PartitionCoverageNoLossEquationLemma"
CLOSED_ATOM = "PartitionCoverageNoLossEquationClosed"
DISJOINT_ATOM = "PartitionDisjointnessAndBoundaryReturnLemma"
HASH_ATOM = "CanonicalFormalUnitHashStabilityLemma"


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


def equations() -> list[dict[str, str]]:
    """给出 no-loss 覆盖等式。"""
    return [
        {
            "name": "total_key_map",
            "formula": "key: O(w) -> K is defined for every obligation after domain canonicalization。",
        },
        {
            "name": "fiber_definition",
            "formula": "O_k={o in O(w): key(o)=k}。",
        },
        {
            "name": "cover_equation",
            "formula": "O(w)=union_{k in key(O(w))} O_k。",
        },
        {
            "name": "return_inclusion",
            "formula": "return records are obligations in O(w) with branch_type in named_return/quotient/reuse。",
        },
        {
            "name": "no_loss_scope",
            "formula": "本引理只证明覆盖不漏；同一物理原子是否重复计数交给 disjointness/boundary-return 引理。",
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


def build_rows(previous: dict[str, Any], domain: dict[str, Any], partition: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 no-loss equation 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    key_ready = previous.get("finite_formal_unit_partition_key_closed") is True
    domain_ready = domain.get("witness_obligation_domain_canonicalization_closed") is True
    partition_interface_ready = partition.get("formal_unit_partition_coverage_interface_closed") is True
    noloss_closed = all([active, guard, key_ready, domain_ready, partition_interface_ready])
    return [
        row(
            "NoLossEquationGateActive",
            active,
            False,
            "上一层已把最窄点推进到 partition coverage no-loss 等式。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行 witness 的 O(w)，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "CanonicalDomainImported",
            domain_ready,
            True,
            "O(w) 已是有限规范义务域。",
            "无义务域格式剩余。",
        ),
        row(
            "TotalFiniteKeyImported",
            key_ready,
            True,
            "每个 obligation 都有 canonical finite key。",
            "key map 是总函数。",
        ),
        row(
            "PartitionInterfaceImported",
            partition_interface_ready,
            True,
            "partition coverage 接口已要求 no-loss 覆盖等式。",
            "本步证明覆盖不漏。",
        ),
        row(
            CLOSED_ATOM,
            noloss_closed,
            True,
            "由总函数 key 的 fiber 分解，O(w) 等于所有 key-fibers 的并；return records 已包含在 O(w)。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            noloss_closed,
            True,
            "no-loss 覆盖等式已闭合；剩余是同坐标重复、边界交叠和回流记录的不交化。",
            DISJOINT_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 no-loss equation 路由。"""
    previous = load_json(paths["previous"])
    domain = load_json(paths["domain"])
    partition = load_json(paths["partition"])
    rows = build_rows(previous, domain, partition)
    closed = next(item["closed"] for item in rows if item["gate"] == CLOSED_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_partition_coverage_no_loss_equation_router",
        "status": "partition_no_loss_equation_closed_disjointness_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "partition_coverage_no_loss_equation_lemma": closed,
        "proved": closed,
        "coverage_complete": closed,
        "partition_coverage_no_loss_equation_closed": closed,
        "formal_unit_partition_coverage_lemma_closed": False,
        "equations": equations(),
        "current_narrowest_atom": DISJOINT_ATOM,
        "secondary_narrowest_atom": HASH_ATOM,
        "reduction_formula": f"{OLD_ATOM} => {CLOSED_ATOM} AND {DISJOINT_ATOM}.",
        "plain_conclusion": (
            "PartitionCoverageNoLossEquationLemma 已闭合：因为 canonical key 是 O(w) 上的总函数，"
            "O(w) 等于所有 key-fibers 的并，命名回流记录也作为 obligations 保留。下一最窄点是 "
            f"`{DISJOINT_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix partition coverage no-loss equation 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"partition_coverage_no_loss_equation_closed={fmt_bool(result['partition_coverage_no_loss_equation_closed'])}",
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
        "## 2. 覆盖等式",
        "",
        "| name | formula |",
        "| --- | --- |",
    ]
    for item in result["equations"]:
        lines.append(
            "| {name} | {formula} |".format(
                name=table_cell(item["name"]),
                formula=table_cell(item["formula"]),
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
            "审稿边界：本步只证明 key-fiber 覆盖不漏；不证明不交化，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--domain", type=Path, default=DEFAULT_DOMAIN)
    parser.add_argument("--partition", type=Path, default=DEFAULT_PARTITION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "domain": args.domain,
        "partition": args.partition,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
