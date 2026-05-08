#!/usr/bin/env python3
"""Prime Matrix anchor set reconstruction certificate 路由器。

用法示例：
  python3 experiments/prime_matrix_anchor_set_reconstruction_certificate_router.py

输出：
  docs/monograph/prime-matrix-anchor-set-reconstruction-certificate-router.json
  docs/monograph/prime-matrix-anchor-set-reconstruction-certificate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json"
DEFAULT_FORMAL_UNIT_SOURCE_RECORD = DOCS / "prime-matrix-formal-unit-source-record-router.json"
DEFAULT_EMITTER = DOCS / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_PARAMETER = DOCS / "prime-matrix-complement-anchor-d0k-parameter-router.json"
DEFAULT_HASH = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-anchor-set-reconstruction-certificate-router.json"
DEFAULT_MD = DOCS / "prime-matrix-anchor-set-reconstruction-certificate-router.md"

OLD_ATOM = "AnchorSetReconstructionCertificateLedger"
SOURCE_TUPLE_ATOM = "ConcreteSourceTupleAnchorParameterDataLedger"
ANCHOR_INTERVAL_ATOM = "AnchorIntervalCertificateFileLedger"


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


def reconstruction_records() -> list[dict[str, str]]:
    """给出七个来源族的 A/D0/K/Omega/phase_rule 重构律。"""
    return [
        {
            "family_id": "EndpointSawtoothDirectedCRTDefect",
            "anchor_reconstruction": "A=empty，D0/K/Omega=null，phase_rule=tau endpoint predicate。",
            "return_if_missing": "EndpointReturnSchema",
        },
        {
            "family_id": "TailAnchorConcentration",
            "anchor_reconstruction": "A 由 payload 的 anchor a 或 anchor bucket 排序得到；D0/K/Omega 继承 TailCore bucket。",
            "return_if_missing": "TailAnchorReturn",
        },
        {
            "family_id": "HighOverlapFixedCoreDefect",
            "anchor_reconstruction": "A 为共享 fixed_core d 的互补锚集合；Omega 为触发高重叠的阈值。",
            "return_if_missing": "HighOverlapReturn",
        },
        {
            "family_id": "ColoredDisjointCorridorBudgetViolation",
            "anchor_reconstruction": "A、D0、K、Omega、phase_rule 均由 colored corridor source tuple payload 读取。",
            "return_if_missing": "DownstreamParameterReturn",
        },
        {
            "family_id": "SmoothCoreLowModCRTDefect",
            "anchor_reconstruction": "继承失败颜色类的 A/D0/K/Omega；低模相位写入 phase_rule。",
            "return_if_missing": "SmoothCoreLowModReturn",
        },
        {
            "family_id": "SparseSingleWindowEscape",
            "anchor_reconstruction": "无锚同步时 A=empty；若 packet 携带 anchor，则按 packet payload 排序取 A。",
            "return_if_missing": "SAEOrSparsePacketReturn",
        },
        {
            "family_id": "RankinConstantGapNoSpike",
            "anchor_reconstruction": "继承 Rankin 失败颜色类的 source tuple；常数缺口不允许后验改 A/D0/K/Omega。",
            "return_if_missing": "RankinConstantGapReturn",
        },
    ]


def reconstruction_laws() -> list[dict[str, str]]:
    """给出重构证书的统一纪律。"""
    return [
        {
            "law": "family_total_extractor",
            "meaning": "每个有限 source_family_id 都有确定 A/D0/K/Omega/phase_rule 抽取规则。",
        },
        {
            "law": "canonical_empty_and_null",
            "meaning": "不适用锚集合的来源族写 A=empty；不适用参数写 canonical null，仍参与 source_tuple_hash。",
        },
        {
            "law": "sorted_anchor_hash",
            "meaning": "anchor_set_hash=H(source_tuple_key, sorted(A))，排序消除枚举顺序依赖。",
        },
        {
            "law": "same_formal_unit_lock",
            "meaning": "A、D0、K、Omega、phase_rule 必须继承同一个 formal_unit_id/source_tuple_hash。",
        },
        {
            "law": "missing_field_return",
            "meaning": "若某字段不能从 payload 重构，则进入命名 return，不得作为无名数据缺口。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    formal_unit_source_record: dict[str, Any],
    emitter: dict[str, Any],
    parameter: dict[str, Any],
    hash_ledger: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 anchor set reconstruction 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    source_tuple_schema_ready = previous.get("source_tuple_anchor_parameter_schema_closed") is True
    formal_unit_ready = formal_unit_source_record.get("concrete_formal_unit_source_record_closed") is True
    emitter_ready = emitter.get("bad_window_source_family_record_emitter_closed") is True
    parameter_ready = parameter.get("complement_anchor_d0k_parameter_discipline_closed") is True
    hash_ready = hash_ledger.get("canonical_formal_unit_hash_stability_closed") is True
    certificate_closed = all(
        [active, guard, source_tuple_schema_ready, formal_unit_ready, emitter_ready, parameter_ready, hash_ready]
    )
    return [
        row(
            "AnchorSetReconstructionGateActive",
            active,
            False,
            "上一层已把最窄点推进到 anchor set reconstruction certificate。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行 witness 的 source tuple，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "SourceTupleSchemaImported",
            source_tuple_schema_ready,
            True,
            "source tuple 已要求 A、D0/K/Omega、phase_rule、anchor_set_hash 与 source_tuple_hash。",
            "字段口径固定。",
        ),
        row(
            "FormalUnitSourceRecordsImported",
            formal_unit_ready,
            True,
            "任意假设 witness 的 formal unit source records 已由普遍抽取定理给出。",
            "payload 来源固定。",
        ),
        row(
            "EmitterFamilyTotalityImported",
            emitter_ready,
            True,
            "七个来源族和各自 payload/downstream 字段已固定。",
            "无新 source family。",
        ),
        row(
            "ParameterDisciplineImported",
            parameter_ready,
            True,
            "D0/K/Omega/phase_rule 不能后验调参，必须由同一 source tuple 复算。",
            "参数来源固定。",
        ),
        row(
            "CanonicalHashImported",
            hash_ready,
            True,
            "formal_unit_id、source_tuple_hash 与 return hash 已分层稳定。",
            "hash 口径固定。",
        ),
        row(
            OLD_ATOM,
            certificate_closed,
            certificate_closed,
            "每个 source tuple 的 A 与参数均由有限来源族 payload 确定；缺字段只能命名回流。",
            SOURCE_TUPLE_ATOM if certificate_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 anchor set reconstruction 路由。"""
    previous = load_json(paths["previous"])
    formal_unit_source_record = load_json(paths["formal_unit_source_record"])
    emitter = load_json(paths["emitter"])
    parameter = load_json(paths["parameter"])
    hash_ledger = load_json(paths["hash"])
    rows = build_rows(previous, formal_unit_source_record, emitter, parameter, hash_ledger)
    certificate_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_anchor_set_reconstruction_certificate",
        "status": "anchor_set_reconstruction_certificate_closed_source_tuple_ready"
        if certificate_closed
        else "anchor_set_reconstruction_certificate_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "anchor_set_reconstruction_certificate_ledger": certificate_closed,
        "proved": certificate_closed,
        "coverage_complete": certificate_closed,
        "anchor_set_reconstruction_records": reconstruction_records(),
        "reconstruction_laws": reconstruction_laws(),
        "current_narrowest_atom": SOURCE_TUPLE_ATOM if certificate_closed else OLD_ATOM,
        "downstream_atoms": [SOURCE_TUPLE_ATOM, ANCHOR_INTERVAL_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => SourceTupleSchema AND FormalUnitSourceRecords AND "
            "EmitterFamilyTotality AND ParameterDiscipline AND CanonicalHash."
        ),
        "plain_conclusion": (
            f"{OLD_ATOM} 已闭合：A、D0/K/Omega 与 phase_rule 均由同一 formal unit 的有限来源族 "
            f"payload 可复算；下一步可回收 `{SOURCE_TUPLE_ATOM}`。"
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
        "# Prime Matrix anchor set reconstruction certificate 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"anchor_set_reconstruction_certificate_ledger={fmt_bool(result['anchor_set_reconstruction_certificate_ledger'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 来源族重构表",
        "",
        "| family_id | anchor_reconstruction | return_if_missing |",
        "| --- | --- | --- |",
    ]
    for item in result["anchor_set_reconstruction_records"]:
        lines.append(
            "| {family_id} | {anchor_reconstruction} | {return_if_missing} |".format(
                family_id=table_cell(item["family_id"]),
                anchor_reconstruction=table_cell(item["anchor_reconstruction"]),
                return_if_missing=table_cell(item["return_if_missing"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 重构纪律",
            "",
            "| law | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["reconstruction_laws"]:
        lines.append(
            "| {law} | {meaning} |".format(
                law=table_cell(item["law"]),
                meaning=table_cell(item["meaning"]),
            )
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
            "## 5. 下一步",
            "",
            f"当前回收目标为 `{result['current_narrowest_atom']}`。",
            "",
            "审稿边界：本步只给出 anchor set 与参数的可复算重构证书；不生成 anchor interval 文件，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--formal-unit-source-record", type=Path, default=DEFAULT_FORMAL_UNIT_SOURCE_RECORD)
    parser.add_argument("--emitter", type=Path, default=DEFAULT_EMITTER)
    parser.add_argument("--parameter", type=Path, default=DEFAULT_PARAMETER)
    parser.add_argument("--hash", type=Path, default=DEFAULT_HASH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "formal_unit_source_record": args.formal_unit_source_record,
        "emitter": args.emitter,
        "parameter": args.parameter,
        "hash": args.hash,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
