#!/usr/bin/env python3
"""Prime Matrix 普遍 formal unit 抽取定理路由器。

用法示例：
  python3 experiments/prime_matrix_universal_formal_unit_extractor_router.py

输出：
  docs/monograph/prime-matrix-universal-formal-unit-extractor-router.json
  docs/monograph/prime-matrix-universal-formal-unit-extractor-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-formal-unit-source-record-router.json"
DEFAULT_TAXONOMY = MONOGRAPH / "prime-matrix-bad-window-source-family-extraction-router.json"
DEFAULT_EMITTER = MONOGRAPH / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-universal-formal-unit-extractor-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-universal-formal-unit-extractor-router.md"

OLD_ATOM = "UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger"
INTERFACE_ATOM = "UniversalExtractorTheoremInterfaceClosed"
PARTITION_ATOM = "FormalUnitPartitionCoverageLemma"
ASSIGNMENT_ATOM = "SourceFamilyAssignmentTotalityLemma"
NOLOSS_ATOM = "NoLossReturnAccountingLemma"
HASH_ATOM = "CanonicalFormalUnitHashStabilityLemma"
SOURCE_RECORD_ATOM = "ConcreteFormalUnitSourceRecordLedger"


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


def is_extractor_proof_like(payload: dict[str, Any]) -> str | None:
    """识别普遍抽取定理或子引理证明。"""
    cert_type = payload.get("certificate_type")
    keys = set(payload.keys())
    if cert_type == "prime_matrix_universal_formal_unit_extractor_theorem":
        return OLD_ATOM
    if cert_type == "prime_matrix_formal_unit_partition_coverage_lemma":
        return PARTITION_ATOM
    if cert_type == "prime_matrix_source_family_assignment_totality_lemma":
        return ASSIGNMENT_ATOM
    if cert_type == "prime_matrix_no_loss_return_accounting_lemma":
        return NOLOSS_ATOM
    if cert_type == "prime_matrix_canonical_formal_unit_hash_stability_lemma":
        return HASH_ATOM
    if "universal_formal_unit_extractor_theorem" in keys:
        return OLD_ATOM
    if "formal_unit_partition_coverage_lemma" in keys:
        return PARTITION_ATOM
    if "source_family_assignment_totality_lemma" in keys:
        return ASSIGNMENT_ATOM
    if "no_loss_return_accounting_lemma" in keys:
        return NOLOSS_ATOM
    if "canonical_formal_unit_hash_stability_lemma" in keys:
        return HASH_ATOM
    return None


def scan_proofs(root: Path, exclude_paths: list[Path] | None = None) -> dict[str, list[dict[str, Any]]]:
    """扫描普遍抽取定理相关证明。"""
    excluded = {path.resolve() for path in (exclude_paths or [])}
    found: dict[str, list[dict[str, Any]]] = {
        OLD_ATOM: [],
        PARTITION_ATOM: [],
        ASSIGNMENT_ATOM: [],
        NOLOSS_ATOM: [],
        HASH_ATOM: [],
    }
    for path in sorted(root.rglob("*.json")):
        if "__pycache__" in path.parts:
            continue
        if path.resolve() in excluded:
            continue
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(payload, dict):
            continue
        kind = is_extractor_proof_like(payload)
        if kind is None:
            continue
        found[kind].append(
            {
                "path": str(path.relative_to(ROOT)),
                "status": payload.get("status"),
                "proved": payload.get("proved"),
                "coverage_complete": payload.get("coverage_complete"),
            }
        )
    return found


def theorem_sublemmas() -> list[dict[str, str]]:
    """给出普遍抽取定理的四个子门。"""
    return [
        {
            "atom": PARTITION_ATOM,
            "meaning": "任意早期零行 witness 诱导的窗口/核心/走廊义务可分割成有限 formal units，且无遗漏。",
        },
        {
            "atom": ASSIGNMENT_ATOM,
            "meaning": "每个 formal unit 都能归入已闭合 taxonomy 的有限来源族之一。",
        },
        {
            "atom": NOLOSS_ATOM,
            "meaning": "未进入某来源族的义务必须显式回流 PDEC/SAE/Rankin/constant-gap，不能消失。",
        },
        {
            "atom": HASH_ATOM,
            "meaning": "formal_unit_id、source_hash 与下游 source_tuple_hash 在分割和回流下稳定。",
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


def proof_closed(records: list[dict[str, Any]]) -> bool:
    """判断证明记录是否全量闭合。"""
    return bool(records) and all(
        item.get("proved") is True and item.get("coverage_complete") is True for item in records
    )


def build_rows(
    previous: dict[str, Any],
    taxonomy: dict[str, Any],
    emitter: dict[str, Any],
    proofs: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    """生成普遍抽取定理判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    source_schema_ready = previous.get("formal_unit_source_record_schema_closed") is True
    taxonomy_ready = taxonomy.get("bad_window_source_family_taxonomy_closed") is True
    emitter_ready = emitter.get("bad_window_source_family_record_emitter_closed") is True
    interface_closed = all([active, guard, source_schema_ready, taxonomy_ready, emitter_ready])
    partition_closed = proof_closed(proofs[PARTITION_ATOM])
    assignment_closed = proof_closed(proofs[ASSIGNMENT_ATOM])
    noloss_closed = proof_closed(proofs[NOLOSS_ATOM])
    hash_closed = proof_closed(proofs[HASH_ATOM])
    theorem_closed = all([partition_closed, assignment_closed, noloss_closed, hash_closed])
    first_open = next(
        (
            atom
            for atom, closed in [
                (PARTITION_ATOM, partition_closed),
                (ASSIGNMENT_ATOM, assignment_closed),
                (NOLOSS_ATOM, noloss_closed),
                (HASH_ATOM, hash_closed),
            ]
            if not closed
        ),
        OLD_ATOM,
    )
    remaining_after_theorem = SOURCE_RECORD_ATOM if theorem_closed else first_open
    theorem_meaning = (
        "四个子门已全部闭合，得到任意早期零行 witness 的 formal unit records。"
        if theorem_closed
        else "四个子门全闭合后，才可得到任意早期零行 witness 的 formal unit records。"
    )
    return [
        row(
            "UniversalExtractorGateActive",
            active,
            False,
            "上一层已把最窄点推进到普遍 early-zero-row formal unit 抽取定理。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只从假设 witness 推导，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "TaxonomyAndEmitterImported",
            taxonomy_ready and emitter_ready and source_schema_ready,
            True,
            "来源族 taxonomy、记录发射器和源记录 schema 均已闭合。",
            "无来源格式剩余。",
        ),
        row(
            INTERFACE_ATOM,
            interface_closed,
            True,
            "普遍抽取定理的输入、输出和四个子门已固定。",
            INTERFACE_ATOM,
        ),
        row(
            "FormalUnitPartitionCoverageAvailable",
            partition_closed,
            partition_closed,
            "partition coverage 子引理证明状态。",
            PARTITION_ATOM,
        ),
        row(
            "SourceFamilyAssignmentTotalityAvailable",
            assignment_closed,
            assignment_closed,
            "source family assignment totality 子引理证明状态。",
            ASSIGNMENT_ATOM,
        ),
        row(
            "NoLossReturnAccountingAvailable",
            noloss_closed,
            noloss_closed,
            "no-loss return accounting 子引理证明状态。",
            NOLOSS_ATOM,
        ),
        row(
            "CanonicalHashStabilityAvailable",
            hash_closed,
            hash_closed,
            "canonical formal unit hash stability 子引理证明状态。",
            HASH_ATOM,
        ),
        row(
            OLD_ATOM,
            theorem_closed,
            theorem_closed,
            theorem_meaning,
            remaining_after_theorem,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行普遍 formal unit 抽取定理路由。"""
    previous = load_json(paths["previous"])
    taxonomy = load_json(paths["taxonomy"])
    emitter = load_json(paths["emitter"])
    proofs = scan_proofs(
        DOCS,
        exclude_paths=[DEFAULT_JSON, paths.get("json_out", DEFAULT_JSON)],
    )
    rows = build_rows(previous, taxonomy, emitter, proofs)
    interface_closed = next(item["closed"] for item in rows if item["gate"] == INTERFACE_ATOM)
    theorem_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = [paths[key] for key in ["previous", "taxonomy", "emitter"]]
    for records in proofs.values():
        evidence_paths.extend(ROOT / item["path"] for item in records)
    evidence_paths = list(dict.fromkeys(evidence_paths))
    partition_closed = proof_closed(proofs[PARTITION_ATOM])
    assignment_closed = proof_closed(proofs[ASSIGNMENT_ATOM])
    noloss_closed = proof_closed(proofs[NOLOSS_ATOM])
    hash_closed = proof_closed(proofs[HASH_ATOM])
    first_open = next(
        (
            atom
            for atom, closed in [
                (PARTITION_ATOM, partition_closed),
                (ASSIGNMENT_ATOM, assignment_closed),
                (NOLOSS_ATOM, noloss_closed),
                (HASH_ATOM, hash_closed),
            ]
            if not closed
        ),
        OLD_ATOM,
    )
    current_narrowest = SOURCE_RECORD_ATOM if theorem_closed else first_open
    status = (
        "universal_extractor_closed"
        if theorem_closed
        else f"universal_extractor_interface_closed_{current_narrowest}_open"
    )
    plain_conclusion = (
        "UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger 已闭合：四个子门全部闭合，任意早期零行"
        " witness 都可产出有限、无漏、可哈希的 formal unit records。"
        if theorem_closed
        else "UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger 的接口已闭合；已吸收当前闭合子门。"
        f"下一最窄点是 `{current_narrowest}`。"
    )
    return {
        "certificate_type": "prime_matrix_universal_formal_unit_extractor_router",
        "status": status,
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "universal_formal_unit_extractor_theorem": theorem_closed,
        "proved": theorem_closed,
        "coverage_complete": theorem_closed,
        "universal_extractor_theorem_interface_closed": interface_closed,
        "universal_extractor_theorem_closed": theorem_closed,
        "proof_like_json": proofs,
        "theorem_sublemmas": theorem_sublemmas(),
        "current_narrowest_atom": current_narrowest,
        "downstream_atoms": [SOURCE_RECORD_ATOM] if theorem_closed else [ASSIGNMENT_ATOM, NOLOSS_ATOM, HASH_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => {INTERFACE_ATOM} AND {PARTITION_ATOM} AND {ASSIGNMENT_ATOM} "
            f"AND {NOLOSS_ATOM} AND {HASH_ATOM}."
        ),
        "plain_conclusion": plain_conclusion,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 普遍 formal unit 抽取定理路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"universal_extractor_theorem_interface_closed={fmt_bool(result['universal_extractor_theorem_interface_closed'])}",
        f"universal_extractor_theorem_closed={fmt_bool(result['universal_extractor_theorem_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 子门",
        "",
        "| atom | meaning |",
        "| --- | --- |",
    ]
    for item in result["theorem_sublemmas"]:
        lines.append(
            "| {atom} | {meaning} |".format(
                atom=table_cell(item["atom"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 当前扫描",
            "",
        ]
    )
    for atom, records in result["proof_like_json"].items():
        lines.append(f"- {atom}: `{len(records)}`")
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
            "## 5. 下一步",
            "",
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。",
            "",
            (
                "审稿边界：本步关闭普遍抽取定理，但不排斥 PDEC/SAE/Rankin 终端，也不关闭行列无条件定理。"
                if result["universal_extractor_theorem_closed"]
                else "审稿边界：本步只更新普遍抽取定理的子门进度，不排斥 PDEC/SAE/Rankin 终端，也不关闭行列无条件定理。"
            ),
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--emitter", type=Path, default=DEFAULT_EMITTER)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "taxonomy": args.taxonomy,
        "emitter": args.emitter,
        "json_out": args.json_out,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
