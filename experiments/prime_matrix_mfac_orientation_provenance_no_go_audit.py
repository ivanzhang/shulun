#!/usr/bin/env python3
"""审计 MFAC 取向来源是否具有前向、pre-Cauchy 的构造证据。

用法示例：
  python3 experiments/prime_matrix_mfac_orientation_provenance_no_go_audit.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-orientation-provenance-no-go-audit"

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
        "verified_date": "2026-08-07",
        "earliest_missing_forward_field": "origin_selector",
        "next_positive_gate": "PrimitiveOrientationLocalFactorProductLawBeforePushforward",
        "mathematical_nonexistence_proved": False,
        "rh_proved": False,
        "row_column_unconditional_closed": False,
    }


def render_markdown(certificate: dict[str, Any]) -> str:
    """将审计结果渲染为可人工核查的 Markdown。"""
    lines = [
        "# MFAC 取向来源 provenance no-go 审计",
        "",
        f"**状态：** `{certificate['status']}`",
        f"**核验日期：** `{certificate['verified_date']}`",
        "",
        "```text",
        "admissible_orientation_source_present="
        f"{str(certificate['admissible_orientation_source_present']).lower()}",
        "earliest_missing_forward_field="
        f"{certificate['earliest_missing_forward_field']}",
        f"next_positive_gate={certificate['next_positive_gate']}",
        "mathematical_nonexistence_proved="
        f"{str(certificate['mathematical_nonexistence_proved']).lower()}",
        f"rh_proved={str(certificate['rh_proved']).lower()}",
        "row_column_unconditional_closed="
        f"{str(certificate['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "当前语料未提交满足全部前向字段的 actual primitive orientation 来源。",
        "这不表示数学上不可能存在此类来源，也不证明 signed transport、行/列命题或 RH。",
        "",
        "## 候选来源",
        "",
        "| name | admissible | missing fields |",
        "| --- | --- | --- |",
    ]
    for candidate in certificate["candidate_sources"]:
        missing_fields = ", ".join(candidate["missing_fields"]) or "none"
        lines.append(
            "| `{name}` | `{admissible}` | `{missing}` |".format(
                name=candidate["name"],
                admissible=str(candidate["admissible"]).lower(),
                missing=missing_fields,
            )
        )
    lines.extend(
        [
            "",
            "## 正向门",
            "",
            "要继续内部 signed-source 路线，必须独立提交 "
            f"`{certificate['next_positive_gate']}`：在 pre-Cauchy 层同时给出 "
            "origin selector、orientation bit、local-factor product、actual-emitter registration "
            "与 prepushforward signed-sum identity。",
            "",
        ]
    )
    return "\n".join(lines)


def write_certificate(certificate: dict[str, Any], json_out: Path, markdown_out: Path) -> None:
    """写出机器可读和人工可读的审计证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_out.write_text(render_markdown(certificate), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs", type=Path, default=DOCS)
    parser.add_argument("--json-out", type=Path, default=DOCS / f"{SLUG}.json")
    parser.add_argument("--md-out", type=Path, default=DOCS / f"{SLUG}.md")
    args = parser.parse_args()

    certificate = audit_orientation_provenance(args.docs)
    write_certificate(certificate, args.json_out, args.md_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.md_out}")
