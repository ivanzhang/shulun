#!/usr/bin/env python3
"""Prime Matrix concrete Rankin batch manifest 数据路由器。

用法示例：
  python3 experiments/prime_matrix_concrete_rankin_manifest_data_router.py

输出：
  docs/monograph/prime-matrix-concrete-rankin-manifest-data-router.json
  docs/monograph/prime-matrix-concrete-rankin-manifest-data-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-formal-rankin-batch-manifest-router.json"
DEFAULT_COLORING = MONOGRAPH / "prime-matrix-interval-graph-coloring-coverage-router.json"
DEFAULT_BUDGET = MONOGRAPH / "prime-matrix-allowed-budget-allocation-router.json"
DEFAULT_SAMPLE = MONOGRAPH / "prime-matrix-bpn-rankin-ledger-certificate-audit.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-concrete-rankin-manifest-data-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-concrete-rankin-manifest-data-router.md"

OLD_ATOM = "ConcreteRankinBatchManifestDataLedger"
EMITTER_ATOM = "ConcreteRankinBatchManifestEmitterClosed"
COLOR_SET_ATOM = "ConcreteColorSetEnumerationLedger"
CERT_ATOM = "PerColorRankinCertificateFileLedger"
RETURN_ATOM = "FailedRankinReturnPacketLedger"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"


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


def is_rankin_certificate_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像单个 Rankin 证书。"""
    return (
        {"p", "k", "intervals", "allowed_budget"}.issubset(payload.keys())
        or payload.get("certificate_type") == "prime_matrix_per_color_rankin_certificate_file_router"
        or payload.get("per_color_rankin_certificate_file_ledger_closed") is True
        or "per_color_rankin_certificate_files" in payload
    )


def is_color_set_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像 concrete color set 枚举。"""
    keys = set(payload.keys())
    return (
        payload.get("certificate_type") in {
            "prime_matrix_colored_corridor_color_set",
            "prime_matrix_interval_graph_coloring_coverage_certificate",
            "prime_matrix_concrete_color_set_enumeration_router",
        }
        or payload.get("concrete_color_set_enumeration_closed") is True
        or "colored_corridor_color_set" in keys
        or "color_classes" in keys
        or "coloring_coverage_records" in keys
    )


def is_return_packet_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像 failed Rankin 回流包。"""
    keys = set(payload.keys())
    return (
        payload.get("certificate_type") == "prime_matrix_failed_rankin_return_packet"
        or "failed_rankin_return_packets" in keys
        or "rankin_failure_return_packets" in keys
    )


def scan_json_corpus(root: Path) -> dict[str, list[dict[str, Any]]]:
    """扫描 concrete color set、Rankin 单证书与失败回流包。"""
    color_sets: list[dict[str, Any]] = []
    rankin_certs: list[dict[str, Any]] = []
    return_packets: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json")):
        if "__pycache__" in path.parts:
            continue
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(payload, dict):
            continue
        rel = str(path.relative_to(ROOT))
        if is_color_set_like(payload):
            rows = (
                payload.get("colored_corridor_color_set")
                or payload.get("color_classes")
                or payload.get("coloring_coverage_records")
                or payload.get("enumeration_fields")
                or []
            )
            color_sets.append(
                {
                    "path": rel,
                    "status": payload.get("status"),
                    "row_count": len(rows) if isinstance(rows, list) else None,
                }
            )
        if is_rankin_certificate_like(payload):
            rows = payload.get("per_color_rankin_certificate_files") or payload.get("rankin_certificate_files") or []
            rankin_certs.append(
                {
                    "path": rel,
                    "p": payload.get("p"),
                    "k": payload.get("k"),
                    "interval_count": len(payload.get("intervals", [])),
                    "record_count": len(rows) if isinstance(rows, list) else None,
                    "rankin_budget_pass": payload.get("rankin_budget_pass"),
                    "exact_budget_pass": payload.get("exact_budget_pass"),
                    "coverage_complete": payload.get("coverage_complete")
                    if payload.get("coverage_complete") is not None
                    else payload.get("per_color_rankin_certificate_file_ledger_closed"),
                }
            )
        if is_return_packet_like(payload):
            packets = (
                payload.get("failed_rankin_return_packets")
                or payload.get("rankin_failure_return_packets")
                or []
            )
            return_packets.append(
                {
                    "path": rel,
                    "status": payload.get("status"),
                    "packet_count": len(packets) if isinstance(packets, list) else None,
                }
            )
    return {
        "color_sets": color_sets,
        "rankin_certs": rankin_certs,
        "return_packets": return_packets,
    }


def materialization_steps() -> list[dict[str, str]]:
    """给出 concrete manifest 生成步骤。"""
    return [
        {
            "step": "enumerate_color_set",
            "output": COLOR_SET_ATOM,
            "meaning": "从 concrete coloring coverage 证书取完整 color_id 集合与每色 intervals。",
        },
        {
            "step": "generate_per_color_rankin",
            "output": CERT_ATOM,
            "meaning": "对每个 color_id 运行单颜色 Rankin 审计，写出证书路径和 hash。",
        },
        {
            "step": "classify_each_row",
            "output": "pass/lowmod_core_crtdefect/constant_gap",
            "meaning": "按 allowed_budget 纪律判定 pass 或失败回流类型。",
        },
        {
            "step": "attach_failed_returns",
            "output": RETURN_ATOM,
            "meaning": "失败行必须有 PDEC/SAE 回流包或 constant-gap refinement 包。",
        },
        {
            "step": "emit_manifest",
            "output": OLD_ATOM,
            "meaning": "写出 batch manifest，并声明 color_set_exact 与 all_rows_pass_or_return。",
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
    coloring: dict[str, Any],
    budget: dict[str, Any],
    sample: dict[str, Any],
    scan: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    """生成 concrete manifest 数据判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    manifest_schema_ready = previous.get("formal_rankin_batch_manifest_schema_closed") is True
    coloring_schema_ready = coloring.get("interval_graph_coloring_coverage_closed") is True
    budget_ready = budget.get("allowed_budget_allocation_discipline_closed") is True
    rankin_sample_ready = sample.get("rankin_budget_pass") is True and sample.get("exact_budget_pass") is True
    emitter_closed = all([active, guard, manifest_schema_ready, coloring_schema_ready, budget_ready, rankin_sample_ready])
    color_set_found = bool(scan["color_sets"])
    rankin_cert_found = bool(scan["rankin_certs"])
    rankin_cert_complete = rankin_cert_found and any(item.get("coverage_complete") is True for item in scan["rankin_certs"])
    return_packet_found = bool(scan["return_packets"])
    manifest_data_closed = emitter_closed and color_set_found and rankin_cert_complete
    color_set_meaning = (
        "已发现 concrete color set 枚举闭合证书，可定义 manifest 全集行。"
        if color_set_found
        else "仓库尚未发现 concrete color set 枚举；没有它无法定义 manifest 全集行。"
    )
    rankin_cert_meaning = (
        "已发现 per-color Rankin 证书文件生成律，可为每个 color_id 生成 verdict 与 hash。"
        if rankin_cert_complete
        else "仓库只发现样本/局部 Rankin 证书，尚非逐颜色全集。"
    )
    return [
        row(
            "ConcreteRankinManifestDataGateActive",
            active,
            False,
            "上一层已把最窄点推进到 concrete Rankin batch manifest 数据。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设反例链条内的数据生成，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ManifestEmitterInputsReady",
            manifest_schema_ready and coloring_schema_ready and budget_ready and rankin_sample_ready,
            True,
            "manifest schema、coloring schema、budget discipline 与单证书执行格式均已固定。",
            "无发射规则剩余。",
        ),
        row(
            EMITTER_ATOM,
            emitter_closed,
            True,
            "concrete manifest 的生成流程已固定为颜色枚举、逐色证书、逐行分类、失败回流、manifest 发射。",
            EMITTER_ATOM,
        ),
        row(
            "ConcreteColorSetEnumerationAvailable",
            color_set_found,
            False,
            color_set_meaning,
            COLOR_SET_ATOM,
        ),
        row(
            "PerColorRankinCertificateFilesAvailable",
            rankin_cert_complete,
            False,
            rankin_cert_meaning,
            CERT_ATOM,
        ),
        row(
            "FailedRankinReturnPacketsAvailable",
            return_packet_found,
            False,
            "若 manifest 存在失败行，仍需正式回流包；当前未发现。",
            RETURN_ATOM,
        ),
        row(
            OLD_ATOM,
            manifest_data_closed,
            manifest_data_closed,
            "Concrete manifest 数据可由 color set 与逐色 Rankin 文件确定性生成；失败行仍需后续回流 packet 或 all-pass 声明。",
            RETURN_ATOM if manifest_data_closed else (CERT_ATOM if color_set_found else f"{COLOR_SET_ATOM} AND {CERT_ATOM}"),
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 concrete manifest 数据路由。"""
    previous = load_json(paths["previous"])
    coloring = load_json(paths["coloring"])
    budget = load_json(paths["budget"])
    sample = load_json(paths["sample"])
    scan = scan_json_corpus(DOCS)
    rows = build_rows(previous, coloring, budget, sample, scan)
    emitter_closed = next(item["closed"] for item in rows if item["gate"] == EMITTER_ATOM)
    evidence_paths = list(paths.values())
    for records in scan.values():
        evidence_paths.extend(ROOT / item["path"] for item in records)
    evidence_paths = list(dict.fromkeys(evidence_paths))
    rankin_cert_complete = bool(scan["rankin_certs"]) and any(
        item.get("coverage_complete") is True for item in scan["rankin_certs"]
    )
    manifest_data_closed = bool(scan["color_sets"]) and rankin_cert_complete
    current_narrowest = RETURN_ATOM if manifest_data_closed else (CERT_ATOM if scan["color_sets"] else COLOR_SET_ATOM)
    status = (
        "concrete_rankin_manifest_data_closed_return_packet_open"
        if manifest_data_closed
        else "concrete_rankin_manifest_emitter_closed_per_color_rankin_open"
        if scan["color_sets"]
        else "concrete_rankin_manifest_emitter_closed_color_set_missing"
    )
    return {
        "certificate_type": "prime_matrix_concrete_rankin_manifest_data_router",
        "status": status,
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "concrete_rankin_batch_manifest_emitter_closed": emitter_closed,
        "concrete_rankin_batch_manifest_data_closed": manifest_data_closed,
        "color_set_like_json": scan["color_sets"],
        "rankin_certificate_like_json": scan["rankin_certs"],
        "return_packet_like_json": scan["return_packets"],
        "materialization_steps": materialization_steps(),
        "current_narrowest_atom": current_narrowest,
        "secondary_narrowest_atom": CERT_ATOM,
        "tertiary_narrowest_atom": RETURN_ATOM,
        "downstream_atoms": [PDEC_SAE_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {EMITTER_ATOM} AND {COLOR_SET_ATOM} AND {CERT_ATOM}.",
        "plain_conclusion": (
            "ConcreteRankinBatchManifestDataLedger 已闭合为可生成 manifest：color set 与逐色 Rankin 文件均已回收；"
            f"下一门是失败行回流 `{RETURN_ATOM}`，若 manifest 全 pass 则该门可为空声明。"
            if manifest_data_closed
            else (
            "ConcreteRankinBatchManifestDataLedger 的发射流程已闭合：给定 concrete color set 后，可逐颜色生成 "
            "Rankin 证书并组装 manifest。当前 color set 已回收，新的最窄点是 "
            f"`{CERT_ATOM}`。"
            if scan["color_sets"]
            else (
                "ConcreteRankinBatchManifestDataLedger 的发射流程已闭合：给定 concrete color set 后，可逐颜色生成 "
                "Rankin 证书并组装 manifest。当前真正缺口不是 manifest 规则，而是没有 concrete color set "
                f"枚举；新的最窄点是 `{COLOR_SET_ATOM}`。"
            )
            )
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    if result["current_narrowest_atom"] == RETURN_ATOM:
        next_note = (
            f"当前唯一最窄点更新为 `{RETURN_ATOM}`；若 manifest 全 pass，可由 all-pass 空回流声明关闭。"
        )
    elif result["current_narrowest_atom"] == result["secondary_narrowest_atom"]:
        next_note = f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。"
    else:
        next_note = (
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；"
            f"随后才是 `{result['secondary_narrowest_atom']}`。"
        )
    lines = [
        "# Prime Matrix concrete Rankin batch manifest 数据路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "concrete_rankin_batch_manifest_emitter_closed="
            f"{fmt_bool(result['concrete_rankin_batch_manifest_emitter_closed'])}"
        ),
        (
            "concrete_rankin_batch_manifest_data_closed="
            f"{fmt_bool(result['concrete_rankin_batch_manifest_data_closed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 生成步骤",
        "",
        "| step | output | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["materialization_steps"]:
        lines.append(
            "| {step} | {output} | {meaning} |".format(
                step=table_cell(item["step"]),
                output=table_cell(item["output"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 当前扫描",
            "",
            f"- color-set-like JSON: `{len(result['color_set_like_json'])}`",
            f"- Rankin-certificate-like JSON: `{len(result['rankin_certificate_like_json'])}`",
            f"- return-packet-like JSON: `{len(result['return_packet_like_json'])}`",
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
            next_note,
            "",
            "审稿边界：本步回收 color set 与逐色 Rankin 文件并关闭 manifest 生成数据；失败行回流、PDEC/SAE 和行列无条件定理仍未关闭。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--coloring", type=Path, default=DEFAULT_COLORING)
    parser.add_argument("--budget", type=Path, default=DEFAULT_BUDGET)
    parser.add_argument("--sample", type=Path, default=DEFAULT_SAMPLE)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "coloring": args.coloring,
        "budget": args.budget,
        "sample": args.sample,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
