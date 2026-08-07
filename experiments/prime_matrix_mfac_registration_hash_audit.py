#!/usr/bin/env python3
"""审计 MFAC formal-unit 哈希是否含 actual emitter registration 证据。

用法示例：
  python3 experiments/prime_matrix_mfac_registration_hash_audit.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-registration-hash-audit"
MANIFEST_TYPE = "prime_matrix_actual_noncanonical_atomic_record_constructor"
REGISTRATION_FIELDS = (
    "emitter_id",
    "primitive_slot",
    "same_formal_unit_certificate",
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
DEFAULT_PATHS = {
    "hash": DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json",
    "source_table": DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json",
    "manifest_root": DOCS,
}


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def is_constructor_manifest(payload: dict[str, Any]) -> bool:
    """判断 payload 是否为 actual constructor manifest。"""
    return payload.get("certificate_type") == MANIFEST_TYPE


def discover_constructor_manifests(root: Path) -> list[tuple[Path, dict[str, Any]]]:
    """发现已登记的 actual constructor manifest。"""
    manifests: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(root.rglob("*.json")):
        try:
            payload = load_json(path)
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        if is_constructor_manifest(payload):
            manifests.append((path, payload))
    return manifests


def hash_contains_registration_fields(hash_certificate: dict[str, Any]) -> bool:
    """检查各层哈希公式是否显式含 registration 三元组。"""
    hash_layers = hash_certificate.get("hash_layers")
    if not isinstance(hash_layers, list):
        return False
    formulas = "\n".join(
        str(layer.get("formula", ""))
        for layer in hash_layers
        if isinstance(layer, dict)
    )
    return all(field in formulas for field in REGISTRATION_FIELDS)


def audit_manifest_registration(payload: dict[str, Any]) -> dict[str, Any]:
    """检查 manifest 是否前向输出完整 registration 且不读取下游。"""
    constructor = payload.get("constructor")
    registration = payload.get("registration")
    if not isinstance(constructor, dict):
        constructor = {}
    if not isinstance(registration, dict):
        registration = {}
    dependencies = constructor.get("dependencies")
    if not isinstance(dependencies, list):
        dependencies = []
    forbidden_dependencies = sorted(
        dependency
        for dependency in dependencies
        if isinstance(dependency, str) and dependency in FORBIDDEN_DEPENDENCIES
    )
    missing_fields = [field for field in REGISTRATION_FIELDS if not registration.get(field)]
    return {
        "missing_registration_fields": missing_fields,
        "forbidden_dependencies": forbidden_dependencies,
    }


def earliest_missing_registration_field(manifest_audits: list[dict[str, Any]]) -> str | None:
    """按 registration 三元组固定顺序给出最早缺字段。"""
    if not manifest_audits:
        return REGISTRATION_FIELDS[0]
    missing_fields = {
        field
        for manifest in manifest_audits
        for field in manifest["missing_registration_fields"]
    }
    for field in REGISTRATION_FIELDS:
        if field in missing_fields:
            return field
    return None


def audit_registration_evidence(paths: dict[str, Path]) -> dict[str, Any]:
    """合取 hash、source table 与 manifest 的 registration 证据。"""
    hash_certificate = load_json(paths["hash"])
    source_table = load_json(paths["source_table"])
    manifest_audits = [
        audit_manifest_registration(payload)
        for _, payload in discover_constructor_manifests(paths["manifest_root"])
    ]
    hash_fields_present = hash_contains_registration_fields(hash_certificate)
    source_table_constructed = (
        source_table.get("actual_noncanonical_primitive_emitter_source_table_proved")
        is True
    )
    downstream_recovery_used = any(
        manifest["forbidden_dependencies"] for manifest in manifest_audits
    )
    valid_registrations = [
        manifest
        for manifest in manifest_audits
        if not manifest["missing_registration_fields"]
        and not manifest["forbidden_dependencies"]
    ]
    return {
        "certificate_type": "prime_matrix_mfac_registration_hash_audit",
        "status": "formal_unit_hash_does_not_supply_actual_emitter_registration",
        "verified_date": "2026-08-07",
        "hash_contains_registration_fields": hash_fields_present,
        "actual_source_table_constructed": source_table_constructed,
        "registration_recoverable_from_hash": (
            hash_fields_present and source_table_constructed and bool(valid_registrations)
        ),
        "earliest_missing_registration_field": earliest_missing_registration_field(
            manifest_audits
        ),
        "downstream_recovery_used": downstream_recovery_used,
        "manifest_audits": manifest_audits,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "当前语料未提交由 formal-unit/source-tuple/source-record hash 前向恢复 "
            "actual emitter registration 的证据；首缺字段为 emitter_id。"
        ),
    }


def complete_registration_fixture(root: Path) -> dict[str, Path]:
    """写入测试用完整 registration fixture，不代表项目已有该构造。"""
    hash_path = root / "hash.json"
    source_table_path = root / "source-table.json"
    manifest_path = root / "manifest.json"
    hash_path.write_text(
        json.dumps(
            {
                "hash_layers": [
                    {
                        "formula": (
                            "H(emitter_id, primitive_slot, "
                            "same_formal_unit_certificate)"
                        )
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    source_table_path.write_text(
        json.dumps(
            {"actual_noncanonical_primitive_emitter_source_table_proved": True},
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    manifest_path.write_text(
        json.dumps(
            {
                "certificate_type": MANIFEST_TYPE,
                "constructor": {"dependencies": ["divisibility", "factor_history"]},
                "registration": {
                    "emitter_id": "synthetic-emitter",
                    "primitive_slot": "synthetic-slot",
                    "same_formal_unit_certificate": "synthetic-unit",
                },
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return {
        "hash": hash_path,
        "source_table": source_table_path,
        "manifest_root": root,
        "manifest": manifest_path,
    }


def render_markdown(certificate: dict[str, Any]) -> str:
    """渲染 registration-hash 审计报告。"""
    return "\n".join(
        [
            "# MFAC registration 与 formal-unit hash 审计",
            "",
            f"**状态：** `{certificate['status']}`",
            "",
            "```text",
            "hash_contains_registration_fields="
            f"{str(certificate['hash_contains_registration_fields']).lower()}",
            "actual_source_table_constructed="
            f"{str(certificate['actual_source_table_constructed']).lower()}",
            "registration_recoverable_from_hash="
            f"{str(certificate['registration_recoverable_from_hash']).lower()}",
            "earliest_missing_registration_field="
            f"{certificate['earliest_missing_registration_field']}",
            "downstream_recovery_used="
            f"{str(certificate['downstream_recovery_used']).lower()}",
            "row_column_unconditional_closed=false",
            "```",
            "",
            certificate["plain_conclusion"],
            "",
            "本证书只表示当前语料未提交 registration 前向证据；不表示数学上不可能存在此类构造，"
            "不声称哈希函数不可逆，更不推出零点排除、ψ 平滑误差或 RH。",
            "",
            "下一门必须是：",
            "",
            "```text",
            "PreCauchyCarrierColoredWordSameFormalUnitSourceRegistrationOrNamedReturn",
            "```",
            "",
        ]
    )


def write_certificate(certificate: dict[str, Any], json_out: Path, markdown_out: Path) -> None:
    """写出机器可读与人工可读证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_out.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """运行审计并输出默认 monograph 证书。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--hash", type=Path, default=DEFAULT_PATHS["hash"])
    parser.add_argument("--source-table", type=Path, default=DEFAULT_PATHS["source_table"])
    parser.add_argument("--manifest-root", type=Path, default=DEFAULT_PATHS["manifest_root"])
    parser.add_argument("--json-out", type=Path, default=DOCS / f"{SLUG}.json")
    parser.add_argument("--md-out", type=Path, default=DOCS / f"{SLUG}.md")
    args = parser.parse_args()

    certificate = audit_registration_evidence(
        {
            "hash": args.hash,
            "source_table": args.source_table,
            "manifest_root": args.manifest_root,
        }
    )
    write_certificate(certificate, args.json_out, args.md_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.md_out}")


if __name__ == "__main__":
    main()
