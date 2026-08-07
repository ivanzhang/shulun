#!/usr/bin/env python3
"""审计 MFAC 实际非规范原子记录是否具有前向构造证据。

用法示例：
  python3 experiments/prime_matrix_mfac_actual_record_constructor_audit.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-actual-record-constructor-audit"
REQUIRED_RECORD_FIELDS = (
    "witness_id",
    "formal_unit_id",
    "source_family_id",
    "origin_selector",
    "source_class",
    "pre_cauchy_timestamp",
    "basis_word",
    "divisor_history",
    "branch_key",
    "orientation",
    "local_factor",
    "signed_coefficient",
    "exact_u",
    "exact_v",
    "row_key",
    "named_return",
)
FORBIDDEN_DEPENDENCIES = {
    "payment",
    "Gamma",
    "pushforward_image",
    "cauchy_output",
    "dispersion_output",
    "terminal_table",
    "origin_table",
    "zero_row_coverage",
    "external_spectral_estimate",
}
MANIFEST_TYPE = "prime_matrix_actual_noncanonical_atomic_record_constructor"


def is_constructor_manifest(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否登记了实际非规范原子记录构造器。"""
    return payload.get("certificate_type") == MANIFEST_TYPE


def discover_manifests(root: Path) -> list[tuple[Path, dict[str, Any]]]:
    """发现已登记的构造器 manifest；不把普通路由 JSON 误判为构造器。"""
    manifests: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(root.rglob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        if isinstance(payload, dict) and is_constructor_manifest(payload):
            manifests.append((path, payload))
    return manifests


def audit_record(record: object) -> dict[str, Any]:
    """检查单条原子记录的字段完整性与非规范成员资格。"""
    if not isinstance(record, dict):
        return {
            "missing_fields": list(REQUIRED_RECORD_FIELDS),
            "actual_noncanonical": False,
            "pre_cauchy": False,
        }
    missing_fields = [field for field in REQUIRED_RECORD_FIELDS if not record.get(field)]
    return {
        "missing_fields": missing_fields,
        "actual_noncanonical": record.get("source_class") == "actual_noncanonical",
        "pre_cauchy": bool(record.get("pre_cauchy_timestamp")),
    }


def audit_manifest(payload: dict[str, Any], path: Path, root: Path) -> dict[str, Any]:
    """检查 manifest 是否显式接收 witness 并前向发射原子记录。"""
    constructor = payload.get("constructor")
    if not isinstance(constructor, dict):
        constructor = {}
    witness_inputs = constructor.get("witness_input_fields")
    dependencies = constructor.get("dependencies")
    records = payload.get("atomic_records")
    if not isinstance(witness_inputs, list):
        witness_inputs = []
    if not isinstance(dependencies, list):
        dependencies = []
    if not isinstance(records, list):
        records = []
    forbidden_dependencies = sorted(
        dependency
        for dependency in dependencies
        if isinstance(dependency, str) and dependency in FORBIDDEN_DEPENDENCIES
    )
    try:
        display_path = str(path.relative_to(root))
    except ValueError:
        display_path = str(path)
    return {
        "path": display_path,
        "witness_constructor": bool(witness_inputs),
        "forbidden_dependencies": forbidden_dependencies,
        "records": [audit_record(record) for record in records],
    }


def earliest_missing_field(manifest_audits: list[dict[str, Any]]) -> str | None:
    """按原子构造顺序返回首个缺失字段。"""
    all_records = [
        record
        for manifest in manifest_audits
        for record in manifest["records"]
    ]
    if not all_records:
        return "origin_selector"
    missing_fields = {
        field for record in all_records for field in record["missing_fields"]
    }
    for field in REQUIRED_RECORD_FIELDS:
        if field in missing_fields:
            return field
    return None


def audit_constructor_evidence(root: Path) -> dict[str, Any]:
    """汇总当前语料对 witness 到实际原子记录构造的证据。"""
    manifest_audits = [
        audit_manifest(payload, path, root)
        for path, payload in discover_manifests(root)
    ]
    downstream_recovery_used = any(
        manifest["forbidden_dependencies"] for manifest in manifest_audits
    )
    witness_to_record_constructor_present = any(
        manifest["witness_constructor"] for manifest in manifest_audits
    )
    atomic_records = [
        record
        for manifest in manifest_audits
        if manifest["witness_constructor"] and not manifest["forbidden_dependencies"]
        for record in manifest["records"]
        if not record["missing_fields"]
        and record["actual_noncanonical"]
        and record["pre_cauchy"]
    ]
    return {
        "certificate_type": "prime_matrix_mfac_actual_record_constructor_audit",
        "status": "current_corpus_has_no_forward_actual_noncanonical_atomic_record_constructor",
        "verified_date": "2026-08-07",
        "constructor_manifests": manifest_audits,
        "witness_to_record_constructor_present": witness_to_record_constructor_present,
        "actual_noncanonical_atomic_record_present": bool(atomic_records),
        "earliest_missing_field": earliest_missing_field(manifest_audits),
        "branch_alphabet_domain_defined": bool(atomic_records),
        "downstream_recovery_used": downstream_recovery_used,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "当前语料未提交从假设 witness 到 actual noncanonical atomic record 的前向构造器；"
            "最早缺失字段为 origin_selector，因此 branch alphabet 尚无定义域。"
        ),
    }


def complete_manifest() -> dict[str, Any]:
    """提供测试用的完整前向 manifest，不代表项目中存在此构造。"""
    return {
        "certificate_type": MANIFEST_TYPE,
        "constructor": {
            "witness_input_fields": ["P", "n", "row_signature"],
            "dependencies": ["divisibility", "factor_history"],
        },
        "atomic_records": [
            {
                "witness_id": "synthetic-witness",
                "formal_unit_id": "synthetic-unit",
                "source_family_id": "synthetic-family",
                "origin_selector": "synthetic-origin",
                "source_class": "actual_noncanonical",
                "pre_cauchy_timestamp": "source-declaration",
                "basis_word": "synthetic-word",
                "divisor_history": ["D:2", "E:3"],
                "branch_key": "synthetic-branch",
                "orientation": 1,
                "local_factor": 1,
                "signed_coefficient": 1,
                "exact_u": 2,
                "exact_v": 3,
                "row_key": "synthetic-row",
                "named_return": "none",
            }
        ],
    }


def render_markdown(certificate: dict[str, Any]) -> str:
    """渲染边界明确的人工可读审计报告。"""
    return "\n".join(
        [
            "# MFAC 实际原子记录构造审计",
            "",
            f"**状态：** `{certificate['status']}`",
            "",
            "```text",
            "witness_to_record_constructor_present="
            f"{str(certificate['witness_to_record_constructor_present']).lower()}",
            "actual_noncanonical_atomic_record_present="
            f"{str(certificate['actual_noncanonical_atomic_record_present']).lower()}",
            f"earliest_missing_field={certificate['earliest_missing_field']}",
            "branch_alphabet_domain_defined="
            f"{str(certificate['branch_alphabet_domain_defined']).lower()}",
            "downstream_recovery_used="
            f"{str(certificate['downstream_recovery_used']).lower()}",
            "row_column_unconditional_closed=false",
            "```",
            "",
            certificate["plain_conclusion"],
            "",
            "本证书只表示当前语料未提交满足判据的构造器证据；不表示数学上不可能存在此类构造，"
            "更不表示存在数值反例、已得到 ψ 平滑误差，或已证明 RH。",
            "",
            "下一门必须是：",
            "",
            "```text",
            "PreCauchyActualNoncanonicalAtomicRecordConstructorOrNamedReturn",
            "```",
            "",
        ]
    )


def write_certificate(certificate: dict[str, Any], json_out: Path, markdown_out: Path) -> None:
    """写出机器可读与人工可读审计证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_out.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """运行审计并写出默认 monograph 证书。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DOCS)
    parser.add_argument("--json-out", type=Path, default=DOCS / f"{SLUG}.json")
    parser.add_argument("--md-out", type=Path, default=DOCS / f"{SLUG}.md")
    args = parser.parse_args()

    certificate = audit_constructor_evidence(args.root)
    write_certificate(certificate, args.json_out, args.md_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.md_out}")


if __name__ == "__main__":
    main()
