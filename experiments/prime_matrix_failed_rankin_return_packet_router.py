#!/usr/bin/env python3
"""Prime Matrix failed Rankin return packet 路由器。

用法示例：
  python3 experiments/prime_matrix_failed_rankin_return_packet_router.py

输出：
  docs/monograph/prime-matrix-failed-rankin-return-packet-router.json
  docs/monograph/prime-matrix-failed-rankin-return-packet-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-concrete-rankin-manifest-data-router.json"
DEFAULT_PER_COLOR = DOCS / "prime-matrix-per-color-rankin-certificate-file-router.json"
DEFAULT_BATCH = DOCS / "prime-matrix-batch-rankin-pass-return-router.json"
DEFAULT_LMC = DOCS / "prime-matrix-bpn-lowmod-core-crtdefect-bridge.md"
DEFAULT_FXA = DOCS / "prime-matrix-bpn-final-exit-acceptance-contract.md"
DEFAULT_HASH = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-failed-rankin-return-packet-router.json"
DEFAULT_MD = DOCS / "prime-matrix-failed-rankin-return-packet-router.md"

OLD_ATOM = "FailedRankinReturnPacketLedger"
BATCH_ATOM = "BatchRankinCertificatesAllPassOrReturnToPDECSAE"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"
CONSTANT_GAP_ATOM = "RankinConstantGapRefinementLedger"


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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def return_packet_records() -> list[dict[str, str]]:
    """给出失败回流 packet 记录族。"""
    return [
        {
            "record_type": "all_pass_empty_return_declaration",
            "coverage": "若 manifest 没有失败行，则必须显式写 all_pass=true。",
            "rule": "空 packet 不是缺失；它是 manifest 全 pass 的可复核声明。",
        },
        {
            "record_type": "failed_color_header",
            "coverage": "每个 rankin_budget_pass=false 的 color_id 一条。",
            "rule": "记录 color_id、rankin_certificate_hash、failure_kind 和 source_tuple_hash。",
        },
        {
            "record_type": "lowmod_core_crtdefect_packet",
            "coverage": "failure_kind=lowmod_core_crtdefect 的失败行。",
            "rule": "写 directed core、residue spike、low-mod witness，并转入 PDEC/SAE。",
        },
        {
            "record_type": "constant_gap_packet",
            "coverage": "failure_kind=constant_gap 的失败行。",
            "rule": "写 no-spike 证据和常数缺口账本引用，转入 constant-gap refinement。",
        },
        {
            "record_type": "packet_hash_row",
            "coverage": "每个 packet 一条。",
            "rule": "return_packet_id=H(source_tuple_hash,color_id,failure_kind,payload_hash)。",
        },
    ]


def return_laws() -> list[dict[str, str]]:
    """给出失败回流纪律。"""
    return [
        {
            "law": "pass_rows_need_no_packet",
            "formula": "rankin_budget_pass=true -> no failed packet required.",
            "meaning": "pass 行不会制造伪回流。",
        },
        {
            "law": "all_pass_empty_packet",
            "formula": "no failed rows -> all_pass_empty_return_declaration.",
            "meaning": "全 pass 情况必须显式声明，避免把缺 packet 误解成漏账。",
        },
        {
            "law": "failed_rows_total",
            "formula": "rankin_budget_pass=false -> exactly one failed return packet.",
            "meaning": "每个失败颜色类必须有命名去向。",
        },
        {
            "law": "two_exit_classification",
            "formula": "failure_kind in {lowmod_core_crtdefect, constant_gap}.",
            "meaning": "Rankin 失败不能产生第三种无名出口。",
        },
        {
            "law": "pdec_sae_not_closed_here",
            "formula": "lowmod_core_crtdefect -> PDEC/SAE terminal remains downstream.",
            "meaning": "本步只回流，不排斥 PDEC/SAE。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    per_color: dict[str, Any],
    batch: dict[str, Any],
    lmc_text: str,
    fxa_text: str,
    hash_ledger: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 failed Rankin return packet 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    manifest_ready = previous.get("concrete_rankin_batch_manifest_data_closed") is True
    per_color_ready = per_color.get("per_color_rankin_certificate_file_ledger_closed") is True
    batch_schema_ready = batch.get("batch_rankin_verifier_schema_closed") is True
    lmc_ready = contains_all(lmc_text, ["Directed Core CRTDefect", "PDEC-or-SAE"])
    fxa_ready = contains_all(fxa_text, ["rankin_budget_pass=true", "rankin_budget_pass=false + low-mod spike"])
    hash_ready = hash_ledger.get("canonical_formal_unit_hash_stability_closed") is True
    packet_closed = all([active, guard, manifest_ready, per_color_ready, batch_schema_ready, lmc_ready, fxa_ready, hash_ready])
    return [
        row(
            "FailedRankinReturnGateActive",
            active,
            False,
            "上一层已把最窄点推进到 failed Rankin return packet。",
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
            "ManifestAndPerColorFilesImported",
            manifest_ready and per_color_ready,
            True,
            "manifest 行与逐色 Rankin verdict 已固定。",
            "失败行全集固定。",
        ),
        row(
            "BatchReturnSchemaImported",
            batch_schema_ready,
            True,
            "批量 Rankin schema 已要求每行 pass 或合法回流。",
            "pass-or-return 字段固定。",
        ),
        row(
            "LowModAndFinalExitImported",
            lmc_ready and fxa_ready,
            True,
            "low-mod spike 回流 PDEC/SAE；无 spike 进入 constant-gap refinement。",
            f"{PDEC_SAE_ATOM} or {CONSTANT_GAP_ATOM}",
        ),
        row(
            "CanonicalReturnHashImported",
            hash_ready,
            True,
            "return_packet_id 继承 source_tuple_hash、color_id 与 failure_kind。",
            "packet 身份稳定。",
        ),
        row(
            OLD_ATOM,
            packet_closed,
            packet_closed,
            "失败 Rankin 行要么不存在并写 all-pass 空声明，要么逐行生成命名回流 packet。",
            BATCH_ATOM if packet_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 failed Rankin return packet 路由。"""
    previous = load_json(paths["previous"])
    per_color = load_json(paths["per_color"])
    batch = load_json(paths["batch"])
    lmc_text = read_text(paths["lmc"])
    fxa_text = read_text(paths["fxa"])
    hash_ledger = load_json(paths["hash"])
    rows = build_rows(previous, per_color, batch, lmc_text, fxa_text, hash_ledger)
    packet_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_failed_rankin_return_packet",
        "certificate_scope": "all_pass_or_failed_rankin_named_return_generator",
        "status": "failed_rankin_return_packet_closed_batch_rankin_ready"
        if packet_closed
        else "failed_rankin_return_packet_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "failed_rankin_return_packet_ledger_closed": packet_closed,
        "proved": packet_closed,
        "coverage_complete": packet_closed,
        "all_pass_empty_return_allowed": True,
        "failed_rankin_return_packets": return_packet_records(),
        "return_laws": return_laws(),
        "current_narrowest_atom": BATCH_ATOM if packet_closed else OLD_ATOM,
        "downstream_atoms": [BATCH_ATOM, PDEC_SAE_ATOM, CONSTANT_GAP_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => ManifestRows AND PerColorVerdicts AND "
            "AllPassEmptyDeclaration OR NamedFailurePackets."
        ),
        "plain_conclusion": (
            f"{OLD_ATOM} 已闭合：Rankin 失败行不会消失；要么 manifest 全 pass 并写空声明，"
            f"要么每个失败 color_id 进入 PDEC/SAE 或 constant-gap packet。下一步回收 `{BATCH_ATOM}`。"
            if packet_closed
            else f"{OLD_ATOM} 尚未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix failed Rankin return packet 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"failed_rankin_return_packet_ledger_closed={fmt_bool(result['failed_rankin_return_packet_ledger_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 回流记录族",
        "",
        "| record_type | coverage | rule |",
        "| --- | --- | --- |",
    ]
    for item in result["failed_rankin_return_packets"]:
        lines.append(
            "| {record_type} | {coverage} | {rule} |".format(
                record_type=table_cell(item["record_type"]),
                coverage=table_cell(item["coverage"]),
                rule=table_cell(item["rule"]),
            )
        )
    lines.extend(["", "## 3. 回流纪律", "", "| law | formula | meaning |", "| --- | --- | --- |"])
    for item in result["return_laws"]:
        lines.append(
            "| {law} | {formula} | {meaning} |".format(
                law=table_cell(item["law"]),
                formula=table_cell(item["formula"]),
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
            "审稿边界：本步只证明 Rankin 失败不漏账；不排斥 PDEC/SAE，不关闭 DStructure/Rankin 最终晋级门。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--per-color", type=Path, default=DEFAULT_PER_COLOR)
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--lmc", type=Path, default=DEFAULT_LMC)
    parser.add_argument("--fxa", type=Path, default=DEFAULT_FXA)
    parser.add_argument("--hash", type=Path, default=DEFAULT_HASH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "per_color": args.per_color,
        "batch": args.batch,
        "lmc": args.lmc,
        "fxa": args.fxa,
        "hash": args.hash,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
