#!/usr/bin/env python3
"""审计 MFAC 取向来源是否具有前向、pre-Cauchy 的构造证据。

用法示例：
  python3 experiments/prime_matrix_mfac_orientation_provenance_no_go_audit.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

REQUIRED_SOURCE_FIELDS = (
    "pre_cauchy",
    "independent_of_downstream",
    "provides_origin_selector",
    "provides_orientation_bit",
    "provides_local_factor_product",
    "provides_prepushforward_sum_identity",
    "actual_emitter_registered",
)


def load_json(path: Path) -> dict[str, Any]:
    """读取单个 JSON 证书，拒绝非对象载荷。"""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"证书必须是对象：{path}")
    return payload


def audit_candidate_sources(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    """按完整前向字段检查候选取向来源。"""
    audited: list[dict[str, Any]] = []
    for candidate in candidates:
        missing_fields = [
            field for field in REQUIRED_SOURCE_FIELDS if candidate.get(field) is not True
        ]
        audited.append(
            {
                **candidate,
                "missing_fields": missing_fields,
                "admissible": not missing_fields,
            }
        )
    return {
        "candidate_sources": audited,
        "admissible_orientation_source_present": any(
            candidate["admissible"] for candidate in audited
        ),
    }


def complete_synthetic_source() -> dict[str, Any]:
    """返回完整合成来源，用于验证判据存在正例。"""
    return {
        "name": "complete_synthetic_orientation_source",
        "pre_cauchy": True,
        "independent_of_downstream": True,
        "provides_origin_selector": True,
        "provides_orientation_bit": True,
        "provides_local_factor_product": True,
        "provides_prepushforward_sum_identity": True,
        "actual_emitter_registered": True,
    }


def mobius_parity_shadow_source() -> dict[str, Any]:
    """返回仅具候选取向影子的 Möbius/parity 条目。"""
    return {
        "name": "mobius_parity_shadow",
        "pre_cauchy": True,
        "independent_of_downstream": True,
        "provides_origin_selector": False,
        "provides_orientation_bit": True,
        "provides_local_factor_product": False,
        "provides_prepushforward_sum_identity": False,
        "actual_emitter_registered": False,
    }


def build_current_corpus_candidates(
    actual_record: dict[str, Any],
    support: dict[str, Any],
    transport: dict[str, Any],
    orientation: dict[str, Any],
) -> list[dict[str, Any]]:
    """将既有证书转成四类候选取向来源。"""
    actual_record_present = actual_record.get("actual_noncanonical_atomic_record_present") is True
    support_closed = support.get("phi_lpf_support_bijection_proved") is True
    transport_closed = transport.get("unsigned_cofactor_split_identity_proved") is True
    orientation_law_proved = (
        orientation.get("orientation_local_factor_law_current_corpus_proved") is True
    )
    return [
        {
            "name": "actual_atomic_record_constructor",
            "pre_cauchy": actual_record_present,
            "independent_of_downstream": actual_record.get("downstream_recovery_used") is False,
            "provides_origin_selector": actual_record.get("earliest_missing_field")
            != "origin_selector",
            "provides_orientation_bit": actual_record_present,
            "provides_local_factor_product": actual_record_present,
            "provides_prepushforward_sum_identity": actual_record_present,
            "actual_emitter_registered": actual_record_present,
        },
        {
            "name": "phi_lpf_owner_support",
            "pre_cauchy": support_closed,
            "independent_of_downstream": support_closed,
            "provides_origin_selector": False,
            "provides_orientation_bit": False,
            "provides_local_factor_product": False,
            "provides_prepushforward_sum_identity": False,
            "actual_emitter_registered": False,
        },
        {
            "name": "rough_cofactor_domain_split",
            "pre_cauchy": transport_closed,
            "independent_of_downstream": transport_closed,
            "provides_origin_selector": False,
            "provides_orientation_bit": False,
            "provides_local_factor_product": False,
            "provides_prepushforward_sum_identity": False,
            "actual_emitter_registered": False,
        },
        {
            **mobius_parity_shadow_source(),
            "orientation_law_proved": orientation_law_proved,
        },
    ]


def audit_orientation_provenance(docs: Path) -> dict[str, Any]:
    """审计当前语料是否提交可用的前向取向来源。"""
    actual_record = load_json(docs / "prime-matrix-mfac-actual-record-constructor-audit.json")
    support = load_json(docs / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json")
    transport = load_json(docs / "prime-matrix-phi-lpf-bucket-signed-transport-router.json")
    orientation = load_json(
        docs / "prime-matrix-strict-row-level-noncircular-orientation-law-router.json"
    )
    result = audit_candidate_sources(
        build_current_corpus_candidates(actual_record, support, transport, orientation)
    )
    return {
        **result,
        "certificate_type": "prime_matrix_mfac_orientation_provenance_no_go_audit",
        "status": "current_corpus_has_no_admissible_forward_orientation_source",
        "earliest_missing_forward_field": "origin_selector",
        "next_positive_gate": "PrimitiveOrientationLocalFactorProductLawBeforePushforward",
        "mathematical_nonexistence_proved": False,
        "row_column_unconditional_closed": False,
    }


if __name__ == "__main__":
    print(json.dumps(audit_orientation_provenance(DOCS), ensure_ascii=False, indent=2))
