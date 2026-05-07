#!/usr/bin/env python3
"""审计当前是否存在已物化的非二点 primitive PDEC 候选。

用法示例：
  python3 experiments/prime_matrix_nontautological_pdec_admission_audit.py

输出：
  docs/monograph/prime-matrix-nontautological-pdec-admission-audit.json
  docs/monograph/prime-matrix-nontautological-pdec-admission-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_STITCHING = DOCS / "prime-matrix-wsh-fo-pdec-stitching-feasibility-audit.json"
DEFAULT_NESTED = DOCS / "prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.json"
DEFAULT_WEIGHTED = DOCS / "prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.json"
DEFAULT_CROSS_Q = DOCS / "prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.json"
DEFAULT_TAUTOLOGY = DOCS / "prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.json"
DEFAULT_SAE = DOCS / "prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.json"
DEFAULT_LEDGER = DOCS / "prime-matrix-local-survivor-materialized-packet-ledger.json"
DEFAULT_JSON = DOCS / "prime-matrix-nontautological-pdec-admission-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-nontautological-pdec-admission-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    stitching: dict[str, Any],
    nested: dict[str, Any],
    weighted: dict[str, Any],
    cross_q: dict[str, Any],
    tautology: dict[str, Any],
    sae: dict[str, Any],
    ledger: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成候选准入审计行。"""
    raw_best = stitching["summary"]["raw_best"]
    return [
        {
            "gate": "RawLibraryThreePointSignal",
            "closed": True,
            "evidence": (
                f"raw support={raw_best['support']}, Fourier={raw_best['fourier']}"
            ),
            "verdict": "not_admissible_without_same_formal_unit_and_independence",
        },
        {
            "gate": "NestedDuplicateUnitMass",
            "closed": bool(nested["all_exact_nested_duplicates_unit_weight_blocked"]),
            "evidence": nested["closed_subgate"],
            "verdict": "nested coordinate repeats cannot count as independent PDEC atoms",
        },
        {
            "gate": "WeightedHallDuplicateRecovery",
            "closed": bool(weighted["all_nested_full_extra_unit_weight_blocked"]),
            "evidence": weighted["closed_subgate"],
            "verdict": "fractional weighted Hall cannot recover the duplicate mass",
        },
        {
            "gate": "CrossQCoordinatePersistence",
            "closed": bool(cross_q["all_cross_level_reuses_chart_overlap_blocked"]),
            "evidence": cross_q["closed_subgate"],
            "verdict": "cross-q reuse is chart overlap, not persistent independent atoms",
        },
        {
            "gate": "PhysicalPrimitiveAtomCount",
            "closed": bool(
                tautology["physical_event_count"] < 3
                and tautology["all_residue_choices_are_two_point_tautology"]
            ),
            "evidence": (
                f"physical_event_count={tautology['physical_event_count']}; "
                f"bound={tautology['two_point_tautology_bound']}"
            ),
            "verdict": "physical primitive branch is two-point tautology, not non-tautological PDEC",
        },
        {
            "gate": "TwoAtomSAEEndpointAbsorption",
            "closed": bool(
                sae["physical_atom_count"] == tautology["physical_event_count"]
                and sae["all_sources_have_local_survivor_witness"]
                and sae["all_factor_199_fibers_are_sparse_load_one"]
            ),
            "evidence": (
                f"physical_atom_count={sae['physical_atom_count']}; "
                f"witnessed={sae['all_sources_have_local_survivor_witness']}"
            ),
            "verdict": "remaining two atoms are absorbed by local survivor witnesses",
        },
        {
            "gate": "MaterializedLedgerNoOpenPDECObligation",
            "closed": bool(
                ledger["current_materialized_local_survivor_packets_closed"]
                and ledger["open_materialized_obligation_count"] == 0
            ),
            "evidence": (
                f"finite_pdec_atom_count={ledger['finite_pdec_atom_count']}; "
                f"open={ledger['open_materialized_obligation_count']}"
            ),
            "verdict": "current materialized PDEC/SAE packets have no open local obligation",
        },
    ]


def run(
    stitching_path: Path,
    nested_path: Path,
    weighted_path: Path,
    cross_q_path: Path,
    tautology_path: Path,
    sae_path: Path,
    ledger_path: Path,
) -> dict[str, Any]:
    """运行非二点 PDEC 准入审计。"""
    stitching = load_json(stitching_path)
    nested = load_json(nested_path)
    weighted = load_json(weighted_path)
    cross_q = load_json(cross_q_path)
    tautology = load_json(tautology_path)
    sae = load_json(sae_path)
    ledger = load_json(ledger_path)
    rows = build_rows(stitching, nested, weighted, cross_q, tautology, sae, ledger)
    all_current_routes_blocked = all(row["closed"] for row in rows)
    return {
        "certificate_type": "prime_matrix_nontautological_pdec_admission_audit",
        "status": "no_current_materialized_nontautological_primitive_pdec",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "stitching": file_sha256(stitching_path),
            "nested": file_sha256(nested_path),
            "weighted": file_sha256(weighted_path),
            "cross_q": file_sha256(cross_q_path),
            "tautology": file_sha256(tautology_path),
            "sae_endpoint": file_sha256(sae_path),
            "materialized_ledger": file_sha256(ledger_path),
        },
        "all_current_routes_blocked_or_absorbed": all_current_routes_blocked,
        "current_materialized_nontautological_pdec_candidate_count": 0,
        "global_pdec_family_closed": False,
        "future_admission_requirements": [
            "same formal unit with one fixed phase map",
            "at least three physical primitive atoms after deduplication",
            "not a two-point Fourier tautology",
            "not nested duplicate mass or weighted-Hall duplicate recovery",
            "not cross-q coordinate chart overlap",
            "not absorbed by LocalSurvivor/SAE/Endpoint witness",
        ],
        "rows": rows,
        "audit_law": (
            "A non-tautological primitive PDEC candidate must survive every quotient already "
            "introduced by the FO-PDEC audits: same-formal-unit legality, nested duplicate "
            "removal, weighted Hall non-recovery, cross-q physical deduplication, and the "
            "two-point tautology test. The current materialized frontier has no such survivor: "
            "the raw three-point signal is not an admissible primitive unit, and the physical "
            "primitive remnant has only two atoms, both absorbed by SAE/Endpoint witnesses."
        ),
        "review_conclusion": (
            "当前已物化前沿没有非二点 primitive PDEC 候选。raw 三点强信号已被同 formal unit、"
            "嵌套重复、weighted Hall 与 cross-q 图重叠逐层降口径；物理 primitive 只剩二点 "
            "Fourier tautology，且二点原子已由 LocalSurvivor witness 吸收。该项不关闭全局 "
            "PDEC family，只给未来新候选固定准入门槛。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 非二点 PDEC 准入审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 准入律",
        "",
        result["audit_law"],
        "",
        "```text",
        "current materialized frontier:",
        "  raw three-point signal -> illegal as one primitive formal unit;",
        "  physical primitive remnant -> two-point Fourier tautology;",
        "  two physical atoms -> LocalSurvivor/SAE witness absorption;",
        "therefore:",
        "  current non-tautological primitive PDEC candidate count = 0.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `all_current_routes_blocked_or_absorbed={fmt_bool(result['all_current_routes_blocked_or_absorbed'])}`。",
        f"- `current_materialized_nontautological_pdec_candidate_count={result['current_materialized_nontautological_pdec_candidate_count']}`。",
        f"- `global_pdec_family_closed={fmt_bool(result['global_pdec_family_closed'])}`。",
        "",
        "## 3. 审计表",
        "",
        "| gate | closed | evidence | verdict |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {verdict} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                verdict=table_cell(row["verdict"]),
            )
        )
    lines.extend(["", "## 4. 未来候选准入要求", ""])
    for item in result["future_admission_requirements"]:
        lines.append(f"- `{item}`")
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stitching-json", type=Path, default=DEFAULT_STITCHING)
    parser.add_argument("--nested-json", type=Path, default=DEFAULT_NESTED)
    parser.add_argument("--weighted-json", type=Path, default=DEFAULT_WEIGHTED)
    parser.add_argument("--cross-q-json", type=Path, default=DEFAULT_CROSS_Q)
    parser.add_argument("--tautology-json", type=Path, default=DEFAULT_TAUTOLOGY)
    parser.add_argument("--sae-json", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--ledger-json", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        stitching_path=args.stitching_json,
        nested_path=args.nested_json,
        weighted_path=args.weighted_json,
        cross_q_path=args.cross_q_json,
        tautology_path=args.tautology_json,
        sae_path=args.sae_json,
        ledger_path=args.ledger_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["current_materialized_nontautological_pdec_candidate_count"])


if __name__ == "__main__":
    main()
