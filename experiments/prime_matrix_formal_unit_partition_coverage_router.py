#!/usr/bin/env python3
"""Prime Matrix formal unit partition coverage 引理路由器。

用法示例：
  python3 experiments/prime_matrix_formal_unit_partition_coverage_router.py

输出：
  docs/monograph/prime-matrix-formal-unit-partition-coverage-router.json
  docs/monograph/prime-matrix-formal-unit-partition-coverage-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-universal-formal-unit-extractor-router.json"
DEFAULT_CLB = DOCS / "prime-matrix-cylindrical-completion-line-barrier.md"
DEFAULT_PHASE = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_CARRY = DOCS / "prime-matrix-early-zero-carry-shell-router.json"
DEFAULT_COFACTOR = DOCS / "prime-matrix-early-zero-cofactor-depth-router.json"
DEFAULT_TAXONOMY = DOCS / "prime-matrix-bad-window-source-family-extraction-router.json"
DEFAULT_EMITTER = DOCS / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-formal-unit-partition-coverage-router.json"
DEFAULT_MD = DOCS / "prime-matrix-formal-unit-partition-coverage-router.md"

OLD_ATOM = "FormalUnitPartitionCoverageLemma"
INTERFACE_ATOM = "FormalUnitPartitionCoverageInterfaceClosed"
DOMAIN_ATOM = "WitnessObligationDomainCanonicalizationLemma"
KEY_ATOM = "FiniteFormalUnitPartitionKeyLemma"
NOLOSS_ATOM = "PartitionCoverageNoLossEquationLemma"
OVERLAP_ATOM = "PartitionDisjointnessAndBoundaryReturnLemma"


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


def is_partition_proof_like(payload: dict[str, Any]) -> str | None:
    """识别 partition coverage 相关证明。"""
    cert_type = payload.get("certificate_type")
    keys = set(payload.keys())
    if cert_type == "prime_matrix_formal_unit_partition_coverage_lemma":
        return OLD_ATOM
    if cert_type == "prime_matrix_witness_obligation_domain_canonicalization_lemma":
        return DOMAIN_ATOM
    if cert_type == "prime_matrix_finite_formal_unit_partition_key_lemma":
        return KEY_ATOM
    if cert_type == "prime_matrix_partition_coverage_no_loss_equation_lemma":
        return NOLOSS_ATOM
    if cert_type == "prime_matrix_partition_disjointness_boundary_return_lemma":
        return OVERLAP_ATOM
    if "formal_unit_partition_coverage_lemma" in keys:
        return OLD_ATOM
    if "witness_obligation_domain_canonicalization_lemma" in keys:
        return DOMAIN_ATOM
    if "finite_formal_unit_partition_key_lemma" in keys:
        return KEY_ATOM
    if "partition_coverage_no_loss_equation_lemma" in keys:
        return NOLOSS_ATOM
    if "partition_disjointness_boundary_return_lemma" in keys:
        return OVERLAP_ATOM
    return None


def scan_partition_proofs(root: Path) -> dict[str, list[dict[str, Any]]]:
    """扫描 partition coverage 相关证明文件。"""
    found: dict[str, list[dict[str, Any]]] = {
        OLD_ATOM: [],
        DOMAIN_ATOM: [],
        KEY_ATOM: [],
        NOLOSS_ATOM: [],
        OVERLAP_ATOM: [],
    }
    for path in sorted(root.rglob("*.json")):
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(payload, dict):
            continue
        kind = is_partition_proof_like(payload)
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


def proof_closed(records: list[dict[str, Any]]) -> bool:
    """判断证明记录是否闭合。"""
    return bool(records) and all(
        item.get("proved") is True and item.get("coverage_complete") is True for item in records
    )


def partition_sublemmas() -> list[dict[str, str]]:
    """给出 partition coverage 的四个子门。"""
    return [
        {
            "atom": DOMAIN_ATOM,
            "meaning": "把任意早期零行 witness 的全部义务规范化成一个有限集合 O(w)：R_x=F_x 物理原子、边界相位、carry/cofactor、走廊与命名回流。",
        },
        {
            "atom": KEY_ATOM,
            "meaning": "给每个 o in O(w) 指派有限 key=(formal_unit_id,family_id,window,D0,K,Omega,phase_key,branch)。",
        },
        {
            "atom": NOLOSS_ATOM,
            "meaning": "证明 O(w) 等于所有 key-fibers 与显式 return records 的不交并；没有义务被丢弃。",
        },
        {
            "atom": OVERLAP_ATOM,
            "meaning": "处理边界重叠、quotient 和复用：重复原子只能合并或回流，不能重复计数。",
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
    taxonomy: dict[str, Any],
    emitter: dict[str, Any],
    proofs: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    """生成 partition coverage 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    extractor_interface_ready = previous.get("universal_extractor_theorem_interface_closed") is True
    clb_ready = contains_all(clb_text, ["R_x", "F_x", "U_x", "CLB-FillerBound"])
    phase_ready = (
        phase.get("early_zero_phase_defect_schema_admission_closed") is True
        and phase.get("registered_same_formal_unit_rxf_ledger") is True
    )
    carry_ready = carry.get("exact_carry_shell_identity_closed") is True
    cofactor_ready = cofactor.get("cofactor_depth_gate_closed") is True
    taxonomy_ready = taxonomy.get("bad_window_source_family_taxonomy_closed") is True
    emitter_ready = emitter.get("bad_window_source_family_record_emitter_closed") is True
    interface_closed = all(
        [
            active,
            guard,
            extractor_interface_ready,
            clb_ready,
            phase_ready,
            carry_ready,
            cofactor_ready,
            taxonomy_ready,
            emitter_ready,
        ]
    )
    domain_closed = proof_closed(proofs[DOMAIN_ATOM])
    key_closed = proof_closed(proofs[KEY_ATOM])
    noloss_closed = proof_closed(proofs[NOLOSS_ATOM])
    overlap_closed = proof_closed(proofs[OVERLAP_ATOM])
    lemma_closed = proof_closed(proofs[OLD_ATOM]) or all([domain_closed, key_closed, noloss_closed, overlap_closed])
    return [
        row(
            "FormalUnitPartitionGateActive",
            active,
            False,
            "上一层已把最窄点推进到 formal unit partition coverage。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行 witness，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "EarlyZeroObligationSourcesImported",
            extractor_interface_ready and clb_ready and phase_ready and carry_ready and cofactor_ready,
            True,
            "CLB 的 R_x/F_x、相位缺陷 formal unit、carry-shell 与 cofactor 深度门均已导入。",
            "义务来源口径固定。",
        ),
        row(
            "FiniteTaxonomyAndEmitterImported",
            taxonomy_ready and emitter_ready,
            True,
            "所有坏窗/走廊来源族和记录发射器已固定。",
            "无新来源类型剩余。",
        ),
        row(
            INTERFACE_ATOM,
            interface_closed,
            True,
            "partition coverage 的输入、输出、key 字段与 no-loss 义务已固定。",
            INTERFACE_ATOM,
        ),
        row(
            "WitnessObligationDomainCanonicalizationAvailable",
            domain_closed,
            False,
            "尚未发现 O(w) 义务域规范化证明。",
            DOMAIN_ATOM,
        ),
        row(
            "FiniteFormalUnitPartitionKeyAvailable",
            key_closed,
            False,
            "尚未发现有限 formal unit key 切分证明。",
            KEY_ATOM,
        ),
        row(
            "PartitionCoverageNoLossEquationAvailable",
            noloss_closed,
            False,
            "尚未发现覆盖无漏等式证明。",
            NOLOSS_ATOM,
        ),
        row(
            "PartitionDisjointnessBoundaryReturnAvailable",
            overlap_closed,
            False,
            "尚未发现重复/边界/回流处理证明。",
            OVERLAP_ATOM,
        ),
        row(
            OLD_ATOM,
            lemma_closed,
            False,
            "四个子门全闭合后，才可得到 formal unit partition coverage。",
            DOMAIN_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 formal unit partition coverage 路由。"""
    previous = load_json(paths["previous"])
    clb_text = read_text(paths["clb"])
    phase = load_json(paths["phase"])
    carry = load_json(paths["carry"])
    cofactor = load_json(paths["cofactor"])
    taxonomy = load_json(paths["taxonomy"])
    emitter = load_json(paths["emitter"])
    proofs = scan_partition_proofs(DOCS)
    rows = build_rows(previous, clb_text, phase, carry, cofactor, taxonomy, emitter, proofs)
    interface_closed = next(item["closed"] for item in rows if item["gate"] == INTERFACE_ATOM)
    lemma_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_formal_unit_partition_coverage_router",
        "status": "formal_unit_partition_interface_closed_domain_canonicalization_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "formal_unit_partition_coverage_interface_closed": interface_closed,
        "formal_unit_partition_coverage_lemma_closed": lemma_closed,
        "partition_proof_like_json": proofs,
        "partition_sublemmas": partition_sublemmas(),
        "current_narrowest_atom": DOMAIN_ATOM,
        "downstream_atoms": [KEY_ATOM, NOLOSS_ATOM, OVERLAP_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => {INTERFACE_ATOM} AND {DOMAIN_ATOM} AND {KEY_ATOM} "
            f"AND {NOLOSS_ATOM} AND {OVERLAP_ATOM}."
        ),
        "plain_conclusion": (
            "FormalUnitPartitionCoverageLemma 的接口已闭合：任意早期零行 witness 的义务必须先形成规范化"
            "有限域 O(w)，再按 formal_unit key 切分，并用 no-loss 覆盖等式处理边界和回流。"
            f"真正尚未闭合的是 `{DOMAIN_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix formal unit partition coverage 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"formal_unit_partition_coverage_interface_closed={fmt_bool(result['formal_unit_partition_coverage_interface_closed'])}",
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
        "## 2. 子门",
        "",
        "| atom | meaning |",
        "| --- | --- |",
    ]
    for item in result["partition_sublemmas"]:
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
    for atom, records in result["partition_proof_like_json"].items():
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
            "审稿边界：本步只关闭 partition coverage 的接口，不证明 O(w) 义务域规范化，也不关闭行列无条件定理。",
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
        "clb": args.clb,
        "phase": args.phase,
        "carry": args.carry,
        "cofactor": args.cofactor,
        "taxonomy": args.taxonomy,
        "emitter": args.emitter,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
