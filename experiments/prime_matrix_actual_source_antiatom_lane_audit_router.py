#!/usr/bin/env python3
"""Prime Matrix actual-source 反原子 lane 审计路由器。

用法示例：
  python3 experiments/prime_matrix_actual_source_antiatom_lane_audit_router.py

输出：
  docs/monograph/prime-matrix-actual-source-antiatom-lane-audit-router.json
  docs/monograph/prime-matrix-actual-source-antiatom-lane-audit-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_TWO_LANE = DOCS / "prime-matrix-noncanonical-two-lane-final-input-router.json"
DEFAULT_BRIDGE = DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
DEFAULT_PROVENANCE = DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
DEFAULT_NOGO = DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
DEFAULT_SOURCE = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-actual-source-antiatom-lane-audit-router.json"
DEFAULT_MD = DOCS / "prime-matrix-actual-source-antiatom-lane-audit-router.md"

SOURCE_ATOM = "ActualFullSNonAPSourceCapacityAntiAtomForActualSource"
SPECTRAL_ATOM = "CDependentResidueWeightSpectralCancellationInput"
DSTRUCTURE_ATOM = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
NEW_AXIOM_ATOM = "AddStrengthenedActualSourceAntiAtomTheorem"


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
    two_lane: dict[str, Any],
    bridge: dict[str, Any],
    provenance: dict[str, Any],
    nogo: dict[str, Any],
    source: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 actual-source 反原子 lane 审计表。"""
    lane_active = two_lane.get("next_priority") == SOURCE_ATOM
    canonical_branch_closed = (
        bridge.get("actual_source_bridge_closed_for_canonical_branch") is True
        and provenance.get("actual_source_provenance_closed") is True
    )
    global_unrestricted_not_closed = bridge.get("actual_source_bridge_closes_global_unrestricted") is False
    generic_refuted = (
        nogo.get("self_contained_generic_version_refuted") is True
        and nogo.get("self_contained_generic_version_closed_as_proof") is False
    )
    source_contract_pinned = (
        source.get("terminal_gap_after_router")
        == "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"
        and bool(source.get("antiatom_contract"))
    )
    new_axiom_needed = all(
        [lane_active, canonical_branch_closed, global_unrestricted_not_closed, generic_refuted, source_contract_pinned]
    )
    return [
        row(
            "ActualSourceAntiAtomLaneActive",
            lane_active,
            False,
            "noncanonical 二选一路由把自足优先点设为 actual-source 反原子。",
            SOURCE_ATOM,
        ),
        row(
            "CanonicalActualSourceBranchClosed",
            canonical_branch_closed,
            True,
            "canonical RIW/Buchstab source 分支的 actual-source provenance 与 bridge 已闭合。",
            "不覆盖 noncanonical/generic 补集。",
        ),
        row(
            "GlobalUnrestrictedStillOpen",
            global_unrestricted_not_closed,
            False,
            "actual-source bridge 明确不关闭 global unrestricted/noncanonical 补集。",
            "noncanonical complement remains.",
        ),
        row(
            "GenericSelfContainedAntiAtomRefuted",
            generic_refuted,
            True,
            "generic full-S 自足反原子被 moving-delta capacity model 反证。",
            "不能由 formal WFD/Type/Fourier/K4K6 推出。",
        ),
        row(
            "StrengthenedSourceContractPinned",
            source_contract_pinned,
            True,
            "剩余 source lane 已精确成为最终容量测度的无 moving same-(u,v) atom 定理。",
            NEW_AXIOM_ATOM,
        ),
        row(
            "NoExistingProofOfActualSourceAntiAtom",
            new_axiom_needed,
            False,
            "现有材料只能给 canonical 分支闭合和 generic 反例；不能推出 global actual-source 反原子。",
            f"{NEW_AXIOM_ATOM} OR {SPECTRAL_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 actual-source 反原子 lane 审计。"""
    two_lane = load_json(paths["two_lane"])
    bridge = load_json(paths["bridge"])
    provenance = load_json(paths["provenance"])
    nogo = load_json(paths["nogo"])
    source = load_json(paths["source"])
    rows = build_rows(two_lane, bridge, provenance, nogo, source)
    no_existing_proof = next(item["closed"] for item in rows if item["gate"] == "NoExistingProofOfActualSourceAntiAtom")
    return {
        "certificate_type": "prime_matrix_actual_source_antiatom_lane_audit_router",
        "status": "actual_source_antiatom_lane_requires_new_axiom_or_spectral_input"
        if no_existing_proof
        else "actual_source_antiatom_lane_audit_incomplete",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "actual_source_antiatom_lane_boundary_closed": no_existing_proof,
        "actual_source_antiatom_proved": False,
        "canonical_branch_closed_only": True,
        "generic_self_contained_antiatom_refuted": True,
        "self_contained_source_lane_remaining": NEW_AXIOM_ATOM,
        "recommended_next_without_new_source_axiom": SPECTRAL_ATOM,
        "parallel_acceptance_priority": DSTRUCTURE_ATOM,
        "reduction_formula": (
            f"{SOURCE_ATOM} => canonical branch already closed; generic branch refuted; "
            f"global route needs {NEW_AXIOM_ATOM} or {SPECTRAL_ATOM}."
        ),
        "plain_conclusion": (
            "actual-source 反原子 lane 已被进一步压窄：canonical source 分支已经闭合；generic "
            "self-contained 反原子为假；因此若不新增强化实际源反原子定理/公理，当前数学硬攻应转向 "
            "c-dependent 完成型谱抵消。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix actual-source 反原子 lane 审计路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"actual_source_antiatom_lane_boundary_closed={fmt_bool(result['actual_source_antiatom_lane_boundary_closed'])}",
        f"actual_source_antiatom_proved={fmt_bool(result['actual_source_antiatom_proved'])}",
        f"generic_self_contained_antiatom_refuted={fmt_bool(result['generic_self_contained_antiatom_refuted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 判定表",
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
            "## 3. 下一步",
            "",
            f"若坚持完全自足，需要新增并证明 `{result['self_contained_source_lane_remaining']}`。",
            f"若不新增源公理，当前数学最窄点转为 `{result['recommended_next_without_new_source_axiom']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--two-lane", type=Path, default=DEFAULT_TWO_LANE)
    parser.add_argument("--bridge", type=Path, default=DEFAULT_BRIDGE)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--nogo", type=Path, default=DEFAULT_NOGO)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "two_lane": args.two_lane,
        "bridge": args.bridge,
        "provenance": args.provenance,
        "nogo": args.nogo,
        "source": args.source,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
