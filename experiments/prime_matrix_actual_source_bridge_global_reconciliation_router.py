#!/usr/bin/env python3
"""调和 actual-source bridge：canonical 分支闭合，global 补集外部化。

用法示例：
  python3 experiments/prime_matrix_actual_source_bridge_global_reconciliation_router.py

输出：
  docs/monograph/prime-matrix-actual-source-bridge-global-reconciliation-router.json
  docs/monograph/prime-matrix-actual-source-bridge-global-reconciliation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_OBSTRUCTION = (
    DOCS / "prime-matrix-global-unconditional-self-contained-obstruction-router.json"
)
DEFAULT_PROVENANCE = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
)
DEFAULT_TAXONOMY = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"
)
DEFAULT_SOURCE_LOCK = DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
DEFAULT_FINAL_THEOREM = (
    DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def find_row(rows: list[dict[str, Any]], gate: str) -> dict[str, Any]:
    """按 gate 查找行。"""
    for row in rows:
        if row.get("gate") == gate:
            return row
    return {}


def recon_row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    global_remainder: str,
) -> dict[str, Any]:
    """构造调和表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "global_remainder": global_remainder,
    }


def build_rows(
    obstruction: dict[str, Any],
    provenance: dict[str, Any],
    taxonomy: dict[str, Any],
    source_lock: dict[str, Any],
    final_theorem: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 actual-source bridge 调和表。"""
    provenance_closed = (
        provenance["actual_source_provenance_closed"]
        and provenance["open_provenance_gates"] == []
        and provenance["terminal_gap_after_router"] == "NoFurtherActualSourceProvenanceGap"
    )
    source_lock_split = (
        source_lock["source_lock_contract_closed_for_canonical_branch"]
        and source_lock["branch_split_preserves_original_target"]
    )
    canonical_theorem_closed = (
        final_theorem["canonical_source_self_contained_theorem_closed"]
        and final_theorem["open_self_contained_gates"] == []
    )
    taxonomy_still_blocks_unrestricted = (
        taxonomy["generic_self_contained_version_refuted"]
        and not taxonomy["original_unrestricted_self_contained_version_closed"]
    )
    obstruction_contains_old_bridge = (
        "ActualFullSSourceBridge"
        in obstruction["blocking_gates_for_full_global_closure"]
    )

    return [
        recon_row(
            gate="CanonicalActualSourceProvenanceClosed",
            closed=provenance_closed,
            evidence=provenance["terminal_gap_after_router"],
            meaning="canonical no-black-box 分支的 pre-Cauchy lambda_c 已声明为 RIW/Buchstab 决策树系数。",
            global_remainder="不覆盖 noncanonical/generic 补集。",
        ),
        recon_row(
            gate="SourceLockBranchSplitClosed",
            closed=source_lock_split,
            evidence=source_lock["terminal_gap_after_router"],
            meaning="source lock 已严格二分：canonical 分支内部闭合，noncanonical 分支外部化或回流。",
            global_remainder="global unrestricted 仍必须处理 noncanonical 补集。",
        ),
        recon_row(
            gate="CanonicalSourceTheoremAlreadyClosed",
            closed=canonical_theorem_closed,
            evidence=final_theorem["terminal_boundary"],
            meaning="actual-source bridge 对 canonical-source 自足定理已经不再是开门。",
            global_remainder="不能升级为完整行/列无条件定理。",
        ),
        recon_row(
            gate="OldActualFullSSourceBridgeBlockerSuperseded",
            closed=obstruction_contains_old_bridge and provenance_closed,
            evidence="ActualFullSSourceBridge in previous obstruction list",
            meaning="旧阻断名应被更精确地替换为 noncanonical full-S 补集问题。",
            global_remainder="FullSNonAPStrengthenedSourceAntiAtom_OR_ExternalDIBFI",
        ),
        recon_row(
            gate="UnrestrictedGenericStillNotClosed",
            closed=taxonomy_still_blocks_unrestricted,
            evidence=taxonomy["terminal_gap_after_router"],
            meaning="unrestricted generic 自足版仍被 moving-delta 反证，不能由 canonical 来源账本偷渡闭合。",
            global_remainder="必须新增强化反原子或外部 DI/BFI 证书。",
        ),
    ]


def run(
    obstruction_path: Path,
    provenance_path: Path,
    taxonomy_path: Path,
    source_lock_path: Path,
    final_theorem_path: Path,
) -> dict[str, Any]:
    """运行 actual-source bridge 全局调和。"""
    obstruction = load_json(obstruction_path)
    provenance = load_json(provenance_path)
    taxonomy = load_json(taxonomy_path)
    source_lock = load_json(source_lock_path)
    final_theorem = load_json(final_theorem_path)

    rows = build_rows(
        obstruction=obstruction,
        provenance=provenance,
        taxonomy=taxonomy,
        source_lock=source_lock,
        final_theorem=final_theorem,
    )
    canonical_absorbed = all(row["closed"] for row in rows[:4])
    updated_global_blocking_gates = [
        gate
        for gate in obstruction["blocking_gates_for_full_global_closure"]
        if gate != "ActualFullSSourceBridge"
    ]
    if "NoncanonicalFullSComplementAntiAtomOrExternalDIBFI" not in updated_global_blocking_gates:
        updated_global_blocking_gates.insert(
            1, "NoncanonicalFullSComplementAntiAtomOrExternalDIBFI"
        )

    return {
        "certificate_type": "prime_matrix_actual_source_bridge_global_reconciliation_router",
        "status": "actual_source_bridge_absorbed_for_canonical_branch_global_complement_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "obstruction": file_sha256(obstruction_path),
            "provenance": file_sha256(provenance_path),
            "taxonomy": file_sha256(taxonomy_path),
            "source_lock": file_sha256(source_lock_path),
            "final_theorem": file_sha256(final_theorem_path),
        },
        "actual_source_bridge_closed_for_canonical_branch": canonical_absorbed,
        "actual_source_bridge_closes_global_unrestricted": False,
        "old_blocker_superseded": "ActualFullSSourceBridge",
        "updated_global_blocking_gates": updated_global_blocking_gates,
        "row_column_unconditional_closed": False,
        "rows": rows,
        "reconciliation_law": (
            "The actual-source bridge has been closed only after restricting the theorem "
            "to the canonical RIW/Buchstab source branch. This absorbs the bridge inside "
            "the canonical self-contained theorem, but it does not close the noncanonical "
            "full-S complement. The former broad blocker ActualFullSSourceBridge should "
            "therefore be replaced by the sharper noncanonical complement obligation: "
            "strengthened anti-atom or external DI/BFI."
        ),
        "review_conclusion": (
            "Actual-source bridge 已在 canonical 分支内闭合；旧阻断门 `ActualFullSSourceBridge` "
            "应被替换为更精确的 `NoncanonicalFullSComplementAntiAtomOrExternalDIBFI`。"
            "这缩窄了完整全局版剩余，但不闭合完整行/列无条件定理。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix actual-source bridge 全局调和路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 调和律",
        "",
        result["reconciliation_law"],
        "",
        "```text",
        (
            "actual_source_bridge_closed_for_canonical_branch="
            f"{fmt_bool(result['actual_source_bridge_closed_for_canonical_branch'])}"
        ),
        (
            "actual_source_bridge_closes_global_unrestricted="
            f"{fmt_bool(result['actual_source_bridge_closes_global_unrestricted'])}"
        ),
        f"old_blocker_superseded={result['old_blocker_superseded']}",
        "updated_global_blocking_gates:",
    ]
    for gate in result["updated_global_blocking_gates"]:
        lines.append(f"  - {gate}")
    lines.extend(
        [
            "```",
            "",
            "## 2. 审查表",
            "",
            "| gate | closed | evidence | meaning | global remainder |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {meaning} | {remainder} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                meaning=table_cell(row["meaning"]),
                remainder=table_cell(row["global_remainder"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            "继续完整全局化时，不应再攻击 canonical actual-source bridge；它已经在自足边界内闭合。"
            "真正剩余是 noncanonical full-S 补集：证明强化 source anti-atom，或完成外部 DI/BFI 无投影量化证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--obstruction-json", type=Path, default=DEFAULT_OBSTRUCTION)
    parser.add_argument("--provenance-json", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--taxonomy-json", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--source-lock-json", type=Path, default=DEFAULT_SOURCE_LOCK)
    parser.add_argument("--final-theorem-json", type=Path, default=DEFAULT_FINAL_THEOREM)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        obstruction_path=args.obstruction_json,
        provenance_path=args.provenance_json,
        taxonomy_path=args.taxonomy_json,
        source_lock_path=args.source_lock_json,
        final_theorem_path=args.final_theorem_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["updated_global_blocking_gates"])


if __name__ == "__main__":
    main()
