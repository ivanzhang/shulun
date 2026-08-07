#!/usr/bin/env python3
"""审计 MFAC 半素数三项 global payload 的 actual dispatch 证据。

用法示例：
  python3 experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit.py
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

from prime_matrix_mfac_colored_divisor_word_transport_audit import (
    build_colored_record,
    is_prime,
    source_payload,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-semiprime-triad-dispatch-audit"

REQUIRED_DISPATCH_FIELDS = (
    "pre_cauchy",
    "independent_of_downstream",
    "origin_selector",
    "actual_emitter_registered",
    "row_key",
    "orientation",
    "local_factor",
    "prepushforward_identity",
)


def build_semiprime_triad(p: int, q: int) -> list[dict[str, Any]]:
    """构造 `p<q` 对应的三项非零 Möbius global payload。"""
    if not is_prime(p) or not is_prime(q) or p >= q:
        raise ValueError("p、q 必须是满足 p<q 的素数")
    value = p * q
    entries: list[dict[str, Any]] = []
    for divisor in (p, q, value):
        record = build_colored_record(value, divisor)
        entries.append(
            {
                "divisor": divisor,
                "cofactor": value // divisor,
                "global_payload": source_payload(record),
            }
        )
    return entries


def audit_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """检查每个 triad 项是否携带完整的前向 dispatch 字段。"""
    audited: list[dict[str, Any]] = []
    for entry in entries:
        missing_fields = [
            field for field in REQUIRED_DISPATCH_FIELDS if not entry.get(field)
        ]
        audited.append(
            {
                **entry,
                "missing_fields": missing_fields,
                "admissible": not missing_fields,
            }
        )
    return audited


def audit_triad_dispatch(dispatch: dict[str, Any]) -> dict[str, Any]:
    """判定 triad 是 actual dispatch、canonical collapse 还是字段缺失。"""
    entries_value = dispatch.get("entries")
    if not isinstance(entries_value, list) or len(entries_value) != 3:
        raise ValueError("dispatch 必须包含恰好三条 triad entries")
    entries = audit_entries(entries_value)
    row_keys = {entry.get("row_key") for entry in entries}
    same_row = len(row_keys) == 1 and None not in row_keys
    zero_sum = math.isclose(
        sum(float(entry["global_payload"]) for entry in entries),
        0.0,
        abs_tol=1e-12,
    )
    actual_dispatch = all(entry["admissible"] for entry in entries) and any(
        entry.get("source_class") == "actual_noncanonical" for entry in entries
    )
    return {
        "entries": entries,
        "global_payload_zero_sum": zero_sum,
        "canonical_zero_sum_collapse": same_row and zero_sum and not actual_dispatch,
        "actual_dispatch_present": actual_dispatch,
    }


def complete_synthetic_dispatch() -> dict[str, Any]:
    """返回完整、前向且非同-row 的合成 actual dispatch。"""
    entries = build_semiprime_triad(2, 3)
    for index, entry in enumerate(entries):
        entry.update(
            {
                "pre_cauchy": True,
                "independent_of_downstream": True,
                "origin_selector": f"synthetic-origin-{index}",
                "actual_emitter_registered": True,
                "row_key": f"synthetic-row-{index}",
                "orientation": 1 if index != 1 else -1,
                "local_factor": 1.0,
                "prepushforward_identity": True,
                "source_class": "actual_noncanonical",
            }
        )
    return {"entries": entries}


def load_json(path: Path) -> dict[str, Any]:
    """读取单个 JSON 证书并拒绝非对象载荷。"""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"证书必须是对象：{path}")
    return payload


def audit_current_corpus(docs: Path) -> dict[str, Any]:
    """审计当前语料对最小半素数 triad 的 dispatch 证据。"""
    colored = load_json(docs / "prime-matrix-mfac-colored-divisor-word-transport-audit.json")
    actual_record = load_json(
        docs / "prime-matrix-mfac-actual-record-constructor-audit.json"
    )
    provenance = load_json(
        docs / "prime-matrix-mfac-orientation-provenance-no-go-audit.json"
    )
    result = audit_triad_dispatch({"entries": build_semiprime_triad(2, 3)})
    return {
        **result,
        "certificate_type": "prime_matrix_mfac_semiprime_triad_dispatch_audit",
        "status": "global_semiprime_triad_reconstructed_actual_dispatch_open",
        "verified_date": "2026-08-07",
        "global_triad_reconstructed": colored.get("record_reconstruction_verified") is True,
        "actual_record_constructor_present": actual_record.get(
            "actual_noncanonical_atomic_record_present"
        )
        is True,
        "orientation_source_present": provenance.get(
            "admissible_orientation_source_present"
        )
        is True,
        "earliest_missing_field": "origin_selector",
        "next_positive_gate": "OffDiagonalSemiprimeTriadActualDispatchBeforePushforward",
        "mathematical_nonexistence_proved": False,
        "rh_proved": False,
        "row_column_unconditional_closed": False,
    }


def render_markdown(certificate: dict[str, Any]) -> str:
    """将 triad dispatch 审计渲染为 Markdown 证书。"""
    lines = [
        "# MFAC 半素数三项 dispatch 审计",
        "",
        f"**状态：** `{certificate['status']}`",
        f"**核验日期：** `{certificate['verified_date']}`",
        "",
        "```text",
        "global_triad_reconstructed="
        f"{str(certificate['global_triad_reconstructed']).lower()}",
        "actual_dispatch_present="
        f"{str(certificate['actual_dispatch_present']).lower()}",
        "canonical_zero_sum_collapse="
        f"{str(certificate['canonical_zero_sum_collapse']).lower()}",
        f"earliest_missing_field={certificate['earliest_missing_field']}",
        f"next_positive_gate={certificate['next_positive_gate']}",
        "mathematical_nonexistence_proved="
        f"{str(certificate['mathematical_nonexistence_proved']).lower()}",
        f"rh_proved={str(certificate['rh_proved']).lower()}",
        "row_column_unconditional_closed="
        f"{str(certificate['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "当前语料未提交从半素数三项 global payload 到 actual primitive row 的前向 dispatch。",
        "当前 triad 缺少 `row_key`，因此不能把未分派的零和 payload 误报为 canonical collapse。",
        "这不表示数学上不可能存在 dispatch，也不证明 signed transport、`ψ` 平滑误差、零点排除、行/列命题或 RH。",
        "",
        "## 三项",
        "",
        "| divisor | cofactor | global payload | missing fields |",
        "| ---: | ---: | ---: | --- |",
    ]
    for entry in certificate["entries"]:
        missing_fields = ", ".join(entry["missing_fields"]) or "none"
        lines.append(
            "| {divisor} | {cofactor} | {payload:.12g} | `{missing}` |".format(
                divisor=entry["divisor"],
                cofactor=entry["cofactor"],
                payload=entry["global_payload"],
                missing=missing_fields,
            )
        )
    lines.extend(
        [
            "",
            "## 正向门",
            "",
            "必须在 pre-Cauchy 层为三项提交 actual record、row dispatch、orientation、"
            "local factor 与 prepushforward identity；仅有 D/E global transport 不能替代该门。",
            "",
        ]
    )
    return "\n".join(lines)


def write_certificate(certificate: dict[str, Any], json_out: Path, markdown_out: Path) -> None:
    """写出机器可读和人工可读的 triad dispatch 证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_out.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """运行当前语料审计并写出默认 monograph 证书。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs", type=Path, default=DOCS)
    parser.add_argument("--json-out", type=Path, default=DOCS / f"{SLUG}.json")
    parser.add_argument("--md-out", type=Path, default=DOCS / f"{SLUG}.md")
    args = parser.parse_args()

    certificate = audit_current_corpus(args.docs)
    write_certificate(certificate, args.json_out, args.md_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.md_out}")


if __name__ == "__main__":
    main()


def same_row_zero_sum_dispatch() -> dict[str, Any]:
    """返回完整但被 canonical 同-row 合并的合成三项。"""
    entries = build_semiprime_triad(2, 3)
    for entry in entries:
        entry.update(
            {
                "pre_cauchy": True,
                "independent_of_downstream": True,
                "origin_selector": "canonical-lpf-selector",
                "actual_emitter_registered": True,
                "row_key": "canonical-lpf-row-2",
                "orientation": 1,
                "local_factor": 1.0,
                "prepushforward_identity": True,
                "source_class": "canonical",
            }
        )
    return {"entries": entries}
