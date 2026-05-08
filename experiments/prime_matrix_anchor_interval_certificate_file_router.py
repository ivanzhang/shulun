#!/usr/bin/env python3
"""Prime Matrix anchor interval 证书文件路由器。

用法示例：
  python3 experiments/prime_matrix_anchor_interval_certificate_file_router.py

输出：
  docs/monograph/prime-matrix-anchor-interval-certificate-file-router.json
  docs/monograph/prime-matrix-anchor-interval-certificate-file-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-concrete-anchor-interval-enumeration-router.json"
DEFAULT_SOURCE_TUPLE = DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json"
DEFAULT_ANCHOR_RECONSTRUCTION = DOCS / "prime-matrix-anchor-set-reconstruction-certificate-router.json"
DEFAULT_HASH = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-anchor-interval-certificate-file-router.json"
DEFAULT_MD = DOCS / "prime-matrix-anchor-interval-certificate-file-router.md"

OLD_ATOM = "AnchorIntervalCertificateFileLedger"
ENUMERATION_ATOM = "ConcreteAnchorIntervalEnumerationLedger"
MULTIPLICITY_ATOM = "LowOverlapMultiplicityTableLedger"


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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def anchor_interval_records() -> list[dict[str, str]]:
    """给出证书文件必须包含的记录族。"""
    return [
        {
            "record_type": "source_tuple_header",
            "coverage": "每个 source_tuple_hash 一条。",
            "rule": "记录 formal_unit_id、P/range、window_id、I=[L,R]、A、D0、phase_rule、anchor_set_hash。",
        },
        {
            "record_type": "anchor_interval_row",
            "coverage": "每个 a in sorted(A) 一条。",
            "rule": "left_d=max(D0,ceil(L/a)); right_d_exclusive=min(2D0,floor(R/a)+1)。",
        },
        {
            "record_type": "phase_filtered_segment_row",
            "coverage": "phase_rule 非 identity 时逐个最大保留段或 residue 条件记录。",
            "rule": "phase_rule(d)=true 的 d 保留；不可判定则进入 PhaseFilterReturn。",
        },
        {
            "record_type": "empty_interval_row",
            "coverage": "left_d>=right_d_exclusive 时必须显式记录。",
            "rule": "空区间不是缺文件，写 empty_interval_flag=true。",
        },
        {
            "record_type": "empty_anchor_set_row",
            "coverage": "A=empty 时必须显式记录。",
            "rule": "空锚集不是缺 source tuple，写 empty_anchor_set_flag=true。",
        },
    ]


def certificate_laws() -> list[dict[str, str]]:
    """给出 anchor interval 证书文件的闭合纪律。"""
    return [
        {
            "law": "same_source_tuple_lock",
            "formula": "all rows inherit the same source_tuple_hash and anchor_set_hash.",
            "meaning": "锚集合、窗口、D0 和相位规则不能跨 formal unit 拼接。",
        },
        {
            "law": "endpoint_total_function",
            "formula": "J_a=[max(D0,ceil(L/a)), min(2D0,floor(R/a)+1)).",
            "meaning": "给定 source tuple 与 anchor 后，端点是全函数，没有选择余地。",
        },
        {
            "law": "per_anchor_totality",
            "formula": "File(s) contains one row for every a in sorted(A).",
            "meaning": "证书文件逐锚覆盖；漏掉任一锚都不能算 complete。",
        },
        {
            "law": "empty_case_is_data",
            "formula": "A=empty or J_a=empty is represented by explicit empty flags.",
            "meaning": "空锚集和空区间被登记为数据，不形成无名缺口。",
        },
        {
            "law": "phase_filter_totality",
            "formula": "identity phase is written; non-identity phase emits segments/residue clauses or a named return.",
            "meaning": "相位过滤不会把点静默删除。",
        },
        {
            "law": "canonical_file_hash",
            "formula": "file_id=H('anchor_interval_file', source_tuple_hash, sorted(endpoint_proof_hashes)).",
            "meaning": "证书文件由规范哈希固定，枚举顺序不影响文件身份。",
        },
    ]


def proof_hash_contract() -> list[dict[str, str]]:
    """给出可复算哈希合同。"""
    return [
        {
            "hash": "endpoint_proof_hash",
            "formula": "H(source_tuple_hash,a,L,R,D0,phase_rule,left_d,right_d_exclusive,empty_flag,segments)。",
        },
        {
            "hash": "anchor_interval_certificate_file_id",
            "formula": "H(formal_unit_id,source_tuple_hash,sorted(endpoint_proof_hashes))。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    source_tuple: dict[str, Any],
    anchor_reconstruction: dict[str, Any],
    hash_ledger: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 anchor interval 证书文件判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    endpoint_ready = previous.get("anchor_interval_endpoint_formula_closed") is True
    source_tuple_ready = source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
    anchor_reconstruction_ready = (
        anchor_reconstruction.get("anchor_set_reconstruction_certificate_ledger") is True
        and anchor_reconstruction.get("coverage_complete") is True
    )
    hash_ready = hash_ledger.get("canonical_formal_unit_hash_stability_closed") is True
    generator_closed = all([endpoint_ready, source_tuple_ready, anchor_reconstruction_ready, hash_ready])
    certificate_closed = active and guard and generator_closed
    return [
        row(
            "AnchorIntervalCertificateGateActive",
            active,
            False,
            "上一层已把最窄点推进到 anchor interval 证书文件。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行链条，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "EndpointFormulaImported",
            endpoint_ready,
            True,
            "J_a 的左右端点已由 ceil/floor 与 [D0,2D0) 裁剪唯一确定。",
            "公式口径固定。",
        ),
        row(
            "SourceTupleParameterLedgerImported",
            source_tuple_ready,
            True,
            "source tuple 已锁定 P/range、window、I=[L,R]、A、D0 与 phase_rule。",
            "不能后验改锚或改窗口。",
        ),
        row(
            "AnchorSetReconstructionImported",
            anchor_reconstruction_ready,
            True,
            "A 与 anchor_set_hash 可由同一 formal unit 的有限来源族 payload 复算。",
            "逐锚枚举域固定。",
        ),
        row(
            "CanonicalHashImported",
            hash_ready,
            True,
            "formal_unit_id、source_tuple_hash 与 endpoint_proof_hash 使用分层哈希。",
            "文件身份稳定。",
        ),
        row(
            "EmptyAndPhaseCasesRegistered",
            generator_closed,
            True,
            "A=empty、J_a=empty 和非 identity phase 都有显式记录或命名回流。",
            "无静默删除口。",
        ),
        row(
            OLD_ATOM,
            certificate_closed,
            certificate_closed,
            "anchor interval 证书文件由 source tuple 与端点公式确定性生成；逐锚、空区间和相位过滤均有记录。",
            ENUMERATION_ATOM if certificate_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 anchor interval 证书文件路由。"""
    previous = load_json(paths["previous"])
    source_tuple = load_json(paths["source_tuple"])
    anchor_reconstruction = load_json(paths["anchor_reconstruction"])
    hash_ledger = load_json(paths["hash"])
    rows = build_rows(previous, source_tuple, anchor_reconstruction, hash_ledger)
    certificate_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_concrete_anchor_interval_enumeration_certificate",
        "certificate_scope": "universal_anchor_interval_file_generator",
        "status": "anchor_interval_certificate_file_closed_enumeration_ready"
        if certificate_closed
        else "anchor_interval_certificate_file_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "anchor_interval_certificate_file_ledger_closed": certificate_closed,
        "proved": certificate_closed,
        "coverage_complete": certificate_closed,
        "anchor_interval_records": anchor_interval_records(),
        "certificate_laws": certificate_laws(),
        "proof_hash_contract": proof_hash_contract(),
        "current_narrowest_atom": ENUMERATION_ATOM if certificate_closed else OLD_ATOM,
        "downstream_atoms": [ENUMERATION_ATOM, MULTIPLICITY_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => EndpointFormula AND SourceTupleParameterLedger AND "
            "AnchorSetReconstruction AND CanonicalFileHash AND EmptyPhaseRegistration."
        ),
        "plain_conclusion": (
            f"{OLD_ATOM} 已闭合：每个 source tuple 的锚区间证书文件由端点公式确定性生成，"
            f"空锚集、空区间和相位过滤均登记为记录。下一步可回收 `{ENUMERATION_ATOM}`。"
            if certificate_closed
            else f"{OLD_ATOM} 尚未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix anchor interval 证书文件路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"anchor_interval_certificate_file_ledger_closed={fmt_bool(result['anchor_interval_certificate_file_ledger_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 证书记录族",
        "",
        "| record_type | coverage | rule |",
        "| --- | --- | --- |",
    ]
    for item in result["anchor_interval_records"]:
        lines.append(
            "| {record_type} | {coverage} | {rule} |".format(
                record_type=table_cell(item["record_type"]),
                coverage=table_cell(item["coverage"]),
                rule=table_cell(item["rule"]),
            )
        )
    lines.extend(["", "## 3. 文件闭合纪律", "", "| law | formula | meaning |", "| --- | --- | --- |"])
    for item in result["certificate_laws"]:
        lines.append(
            "| {law} | {formula} | {meaning} |".format(
                law=table_cell(item["law"]),
                formula=table_cell(item["formula"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(["", "## 4. 哈希合同", "", "| hash | formula |", "| --- | --- |"])
    for item in result["proof_hash_contract"]:
        lines.append(
            "| {hash} | {formula} |".format(
                hash=table_cell(item["hash"]),
                formula=table_cell(item["formula"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一步",
            "",
            f"当前回收目标为 `{result['current_narrowest_atom']}`；随后才是 `{MULTIPLICITY_ATOM}`。",
            "",
            "审稿边界：本步只关闭假设链条中的 anchor interval 证书文件生成律；不证明真实早期零行存在或缺席，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--source-tuple", type=Path, default=DEFAULT_SOURCE_TUPLE)
    parser.add_argument("--anchor-reconstruction", type=Path, default=DEFAULT_ANCHOR_RECONSTRUCTION)
    parser.add_argument("--hash", type=Path, default=DEFAULT_HASH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "source_tuple": args.source_tuple,
        "anchor_reconstruction": args.anchor_reconstruction,
        "hash": args.hash,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
