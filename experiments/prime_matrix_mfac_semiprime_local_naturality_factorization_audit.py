#!/usr/bin/env python3
"""审计半素数 triad 是否仅重用既有局部乘法资料。

用法示例：
  python3 experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py
"""

from __future__ import annotations

import argparse
import json
from typing import Any
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-semiprime-local-naturality-factorization-audit"


REQUIRED_INDEPENDENT_FIELDS = (
    "origin_selector",
    "actual_emitter_registered",
    "orientation",
    "local_factor",
    "exact_uv",
    "prepushforward_identity",
)


def build_candidate_families(p: int, q: int) -> list[dict[str, Any]]:
    """构造固定素数对的五类现有候选，不虚构 actual primitive row。"""
    if p >= q:
        raise ValueError("候选族要求满足 p < q")

    shared = {
        "prime_pair": (p, q),
        "pre_cauchy": True,
        "independent_of_downstream": True,
        "local_data_only": True,
        "prime_renaming_natural": True,
        "local_coefficient_law": True,
        "adds_primitive_arithmetic_functional": False,
    }
    return [
        {
            **shared,
            "name": "global_mobius_lambda",
            "row_kind": "global_only",
            "fallback_classification": "global_only_zero_sum",
        },
        {
            **shared,
            "name": "de_colored_divisor_word",
            "row_kind": "global_only",
            "fallback_classification": "global_only_transport",
        },
        {
            **shared,
            "name": "lpf_phi_factor_word",
            "row_kind": "support_only",
            "fallback_classification": "unsigned_or_canonical_support",
        },
        {
            **shared,
            "name": "square_base_parity",
            "row_kind": "posterior_only",
            "fallback_classification": "posterior_state_only",
        },
        {
            **shared,
            "name": "canonical_riw_buchstab_t1",
            "row_kind": "canonical",
            "fallback_classification": "canonical_factorization",
        },
    ]


def classify_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    """在显式局部自然性模型内分类一个候选，而不声称普遍数学定理。"""
    result = {**candidate, "actual_noncanonical_declaration": False}
    if not result.get("pre_cauchy") or not result.get("independent_of_downstream"):
        result["classification"] = "downstream_dependent_rejected"
        return result
    if result.get("row_kind") == "canonical":
        result["classification"] = "canonical_factorization"
        return result
    if result.get("row_kind") == "same_row" and result.get("local_coefficient_law"):
        result["classification"] = "rowwise_cancellation"
        result["row_coefficient"] = 0.0
        return result
    result["classification"] = result.get(
        "fallback_classification", "unclassified_local_model_candidate"
    )
    return result


def find_minimal_collision_certificate(
    candidates: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """返回首个完整越界候选；缺字段或下游依赖均不是 collision。"""
    for candidate in candidates:
        classified = classify_candidate(candidate)
        if classified["classification"] == "downstream_dependent_rejected":
            continue
        if not candidate.get("adds_primitive_arithmetic_functional"):
            continue
        if candidate.get("row_kind") != "noncanonical":
            continue
        missing_fields = [
            field for field in REQUIRED_INDEPENDENT_FIELDS if not candidate.get(field)
        ]
        if missing_fields:
            continue
        return {
            "candidate_name": candidate["name"],
            "reason": "complete_independent_noncanonical_candidate",
            "required_fields": list(REQUIRED_INDEPENDENT_FIELDS),
            "mathematical_nonexistence_proved": False,
        }
    return None


def load_json(path: Path) -> dict[str, Any]:
    """读取单个 JSON 证书并拒绝非对象载荷。"""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"证书必须是对象：{path}")
    return payload


def audit_current_corpus(docs: Path) -> dict[str, Any]:
    """以既有证书审计当前语料，而不扩大为数学不存在性结论。"""
    colored = load_json(docs / "prime-matrix-mfac-colored-divisor-word-transport-audit.json")
    provenance = load_json(
        docs / "prime-matrix-mfac-orientation-provenance-no-go-audit.json"
    )
    triad = load_json(docs / "prime-matrix-mfac-semiprime-triad-dispatch-audit.json")
    classifications = [
        classify_candidate(candidate) for candidate in build_candidate_families(2, 3)
    ]
    collision = find_minimal_collision_certificate(classifications)
    independent_line = bool(
        colored.get("actual_primitive_unit_binding_constructed")
        and provenance.get("admissible_orientation_source_present")
        and triad.get("actual_dispatch_present")
    )
    return {
        "certificate_type": "prime_matrix_mfac_semiprime_local_naturality_factorization_audit",
        "status": "current_corpus_candidate_families_classified_independent_declaration_open",
        "verified_date": "2026-08-07",
        "conditional_scope": "explicit_local_naturality_model_only",
        "prime_pair": [2, 3],
        "candidate_classifications": classifications,
        "current_corpus_has_independent_semiprime_declaration_line": independent_line,
        "minimal_collision_certificate_present": collision is not None,
        "minimal_collision_certificate": collision,
        "global_payload_transport_closed": colored.get(
            "global_payload_conservation_verified"
        )
        is True,
        "actual_primitive_unit_binding_constructed": colored.get(
            "actual_primitive_unit_binding_constructed"
        )
        is True,
        "admissible_orientation_source_present": provenance.get(
            "admissible_orientation_source_present"
        )
        is True,
        "actual_triad_dispatch_present": triad.get("actual_dispatch_present") is True,
        "mathematical_nonexistence_proved": False,
        "rh_proved": False,
        "row_column_unconditional_closed": False,
        "next_positive_gate": "SemiprimeTriadDeclarationLineFromIndependentArithmeticIdentity",
    }


def write_certificate(
    certificate: dict[str, Any], json_out: Path, markdown_out: Path
) -> None:
    """写出机器证书和人读边界说明。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    classifications = "\n".join(
        f"| `{candidate['name']}` | `{candidate['classification']}` |"
        for candidate in certificate["candidate_classifications"]
    )
    markdown_out.write_text(
        "\n".join(
            [
                "# MFAC 半素数局部自然性分解审计",
                "",
                "**状态：** `current_corpus_candidate_families_classified_independent_declaration_open`",
                "",
                "本证书仅在显式局部自然性模型内分类五个既有候选族。它不表示数学上不存在独立的 noncanonical pre-Cauchy identity，也不把有限候选分类升级为普遍 no-go 定理。",
                "",
                "## 候选分类",
                "",
                "| 候选族 | 审计分类 |",
                "| --- | --- |",
                classifications,
                "",
                "## 当前语料结论",
                "",
                "```text",
                f"current_corpus_has_independent_semiprime_declaration_line={str(certificate['current_corpus_has_independent_semiprime_declaration_line']).lower()}",
                f"minimal_collision_certificate_present={str(certificate['minimal_collision_certificate_present']).lower()}",
                "mathematical_nonexistence_proved=false",
                "rh_proved=false",
                "row_column_unconditional_closed=false",
                f"next_positive_gate={certificate['next_positive_gate']}",
                "```",
                "",
                "全局 D/E payload、LPF/Phi 支撑、square-base parity 与 canonical RIW/Buchstab 行均未提供 actual primitive-unit binding、独立 origin selector 与 prepushforward identity 的完整组合。真正正向输入仍须由下一正向门独立给出。",
                "",
            ]
        ),
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    """解析证书输出位置。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", type=Path, default=DOCS / f"{SLUG}.json")
    parser.add_argument("--markdown-out", type=Path, default=DOCS / f"{SLUG}.md")
    return parser.parse_args()


def main() -> None:
    """运行当前语料审计并写出两个证书。"""
    args = parse_args()
    certificate = audit_current_corpus(DOCS)
    write_certificate(certificate, args.json_out, args.markdown_out)
    print(f"写入 JSON 证书：{args.json_out}")
    print(f"写入 Markdown 证书：{args.markdown_out}")


if __name__ == "__main__":
    main()
