#!/usr/bin/env python3
"""Prime Matrix noncanonical 二选一最终输入路由器。

用法示例：
  python3 experiments/prime_matrix_noncanonical_two_lane_final_input_router.py

输出：
  docs/monograph/prime-matrix-noncanonical-two-lane-final-input-router.json
  docs/monograph/prime-matrix-noncanonical-two-lane-final-input-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_ACTIVE = DOCS / "prime-matrix-active-final-inputs-router.json"
DEFAULT_TRILEMMA = DOCS / "prime-matrix-noncanonical-complement-trilemma-router.json"
DEFAULT_SOURCE = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
DEFAULT_SPECTRAL = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-noncanonical-two-lane-final-input-router.json"
DEFAULT_MD = DOCS / "prime-matrix-noncanonical-two-lane-final-input-router.md"

ACTIVE_ATOM = "NoncanonicalTwoLaneMathInput"
SOURCE_ATOM = "ActualFullSNonAPSourceCapacityAntiAtomForActualSource"
SPECTRAL_ATOM = "CDependentResidueWeightSpectralCancellationInput"
DSTRUCTURE_ATOM = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def row(
    lane: str,
    active: bool,
    boundary_closed: bool,
    proved_or_accepted: bool,
    role: str,
    blocked_shortcuts: list[str],
    required_input: str,
) -> dict[str, Any]:
    """构造 lane 表行。"""
    return {
        "lane": lane,
        "active": active,
        "boundary_closed": boundary_closed,
        "proved_or_accepted": proved_or_accepted,
        "role": role,
        "blocked_shortcuts": blocked_shortcuts,
        "required_input": required_input,
    }


def build_rows(
    active: dict[str, Any],
    trilemma: dict[str, Any],
    source: dict[str, Any],
    spectral: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 noncanonical 二选一 lane 判定表。"""
    active_gate = ACTIVE_ATOM in active.get("currently_active_final_inputs", [])
    trilemma_closed = trilemma.get("trilemma_boundary_closed") is True
    source_boundary = (
        "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"
        in source.get("open_antiatom_gates", [])
        and source.get("source_antiatom_reduction_closed") is False
    )
    spectral_boundary = (
        SPECTRAL_ATOM in spectral.get("open_spectral_gap_gates", [])
        and spectral.get("completed_weight_spectral_gap_closed") is False
    )
    return [
        row(
            lane="ActiveNoncanonicalGateImported",
            active=active_gate,
            boundary_closed=active_gate and trilemma_closed,
            proved_or_accepted=active_gate and trilemma_closed,
            role="最终数学输入已缩为 noncanonical 二选一。",
            blocked_shortcuts=[],
            required_input=f"{SOURCE_ATOM} OR {SPECTRAL_ATOM}",
        ),
        row(
            lane=SOURCE_ATOM,
            active=True,
            boundary_closed=source_boundary,
            proved_or_accepted=False,
            role="自足 lane：证明实际源没有 moving same-(u,v) 原子，或进一步证明实际源等于 canonical RIW/Buchstab。",
            blocked_shortcuts=source.get("blocked_shortcuts", []),
            required_input=source.get("antiatom_contract", "source capacity anti-atom theorem"),
        ),
        row(
            lane=SPECTRAL_ATOM,
            active=True,
            boundary_closed=spectral_boundary,
            proved_or_accepted=False,
            role="外部/新深定理 lane：对 c-dependent、未中心化、无投影 residue 权重取得谱平均抵消。",
            blocked_shortcuts=[
                "pointwise Weil + L2",
                "ordinary large sieve",
                "flat or centered residue shortcut",
            ],
            required_input="; ".join(spectral.get("required_theorem_clauses", [])),
        ),
        row(
            lane=DSTRUCTURE_ATOM,
            active=True,
            boundary_closed=active.get("promotion_narrowest_atom") == DSTRUCTURE_ATOM,
            proved_or_accepted=False,
            role="并行晋级验收 lane：即使 noncanonical 数学输入闭合，也仍需独立接受。",
            blocked_shortcuts=["author-side self-promotion"],
            required_input="independent promotion acceptance",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 noncanonical 二选一最终输入路由。"""
    active = load_json(paths["active"])
    trilemma = load_json(paths["trilemma"])
    source = load_json(paths["source"])
    spectral = load_json(paths["spectral"])
    rows = build_rows(active, trilemma, source, spectral)
    noncanonical_rows = [item for item in rows if item["lane"] in {SOURCE_ATOM, SPECTRAL_ATOM}]
    return {
        "certificate_type": "prime_matrix_noncanonical_two_lane_final_input_router",
        "status": "noncanonical_two_lane_pinned_source_or_spectral_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "noncanonical_two_lane_boundary_closed": all(item["boundary_closed"] for item in rows),
        "noncanonical_two_lane_proved_or_accepted": any(
            item["proved_or_accepted"] for item in noncanonical_rows
        ),
        "self_contained_priority": SOURCE_ATOM,
        "external_or_new_deep_theorem_priority": SPECTRAL_ATOM,
        "parallel_acceptance_priority": DSTRUCTURE_ATOM,
        "minimum_unconditional_basis": (
            f"({SOURCE_ATOM} OR {SPECTRAL_ATOM}) AND {DSTRUCTURE_ATOM}"
        ),
        "next_priority": SOURCE_ATOM,
        "fallback_priority": SPECTRAL_ATOM,
        "reduction_formula": (
            f"{ACTIVE_ATOM} => ({SOURCE_ATOM} OR {SPECTRAL_ATOM}); "
            f"final theorem still requires {DSTRUCTURE_ATOM}."
        ),
        "plain_conclusion": (
            "NoncanonicalTwoLaneMathInput 已拆成两条互斥可审稿 lane：自足路线必须证明实际源反原子"
            "或实际源恒等；外部路线必须证明/接受 c-dependent 完成型谱抵消。当前两条 lane 都未证明，"
            "所以行列无条件定理仍未闭合。"
        ),
        "rows": rows,
        "closed_lanes": [item["lane"] for item in rows if item["boundary_closed"]],
        "open_lanes": [item["lane"] for item in rows if not item["proved_or_accepted"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix noncanonical 二选一最终输入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"noncanonical_two_lane_boundary_closed={fmt_bool(result['noncanonical_two_lane_boundary_closed'])}",
        f"noncanonical_two_lane_proved_or_accepted={fmt_bool(result['noncanonical_two_lane_proved_or_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. Lane 表",
        "",
        "| lane | active | boundary_closed | proved_or_accepted | role | required_input |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {lane} | `{active}` | `{closed}` | `{proved}` | {role} | {required} |".format(
                lane=table_cell(item["lane"]),
                active=fmt_bool(item["active"]),
                closed=fmt_bool(item["boundary_closed"]),
                proved=fmt_bool(item["proved_or_accepted"]),
                role=table_cell(item["role"]),
                required=table_cell(item["required_input"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"优先自足硬攻：`{result['self_contained_priority']}`。",
            f"外部/新深定理备选：`{result['external_or_new_deep_theorem_priority']}`。",
            f"并行晋级验收：`{result['parallel_acceptance_priority']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--active", type=Path, default=DEFAULT_ACTIVE)
    parser.add_argument("--trilemma", type=Path, default=DEFAULT_TRILEMMA)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--spectral", type=Path, default=DEFAULT_SPECTRAL)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "active": args.active,
        "trilemma": args.trilemma,
        "source": args.source,
        "spectral": args.spectral,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
