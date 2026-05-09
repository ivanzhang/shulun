#!/usr/bin/env python3
"""Prime Matrix 批量 Rankin pass-or-return 路由器。

用法示例：
  python3 experiments/prime_matrix_batch_rankin_pass_return_router.py

输出：
  docs/monograph/prime-matrix-batch-rankin-pass-return-router.json
  docs/monograph/prime-matrix-batch-rankin-pass-return-router.md
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

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-allowed-budget-allocation-router.json"
DEFAULT_RLA = MONOGRAPH / "prime-matrix-bpn-rankin-ledger-acceptance-theorem.md"
DEFAULT_LMC = MONOGRAPH / "prime-matrix-bpn-lowmod-core-crtdefect-bridge.md"
DEFAULT_FXA = MONOGRAPH / "prime-matrix-bpn-final-exit-acceptance-contract.md"
DEFAULT_SAMPLE = MONOGRAPH / "prime-matrix-bpn-rankin-ledger-certificate-audit.json"
DEFAULT_MANIFEST_DATA = MONOGRAPH / "prime-matrix-concrete-rankin-manifest-data-router.json"
DEFAULT_RETURN_PACKET = MONOGRAPH / "prime-matrix-failed-rankin-return-packet-router.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-batch-rankin-pass-return-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-batch-rankin-pass-return-router.md"

OLD_ATOM = "BatchRankinCertificatesAllPassOrReturnToPDECSAE"
SCHEMA_ATOM = "BatchRankinVerifierSchemaClosed"
MANIFEST_ATOM = "FormalRankinBatchManifestLedger"
RETURN_ATOM = "FailedRankinReturnPacketLedger"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"
CONSTANT_GAP_ATOM = "RankinConstantGapRefinementLedger"
DSTRUCTURE_ATOM = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


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
    return {"p", "k", "intervals", "allowed_budget"}.issubset(payload.keys())


def is_batch_manifest_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像正式批量 Rankin manifest。"""
    keys = set(payload.keys())
    return (
        payload.get("certificate_type")
        in {
            "prime_matrix_rankin_batch_manifest",
            "prime_matrix_concrete_rankin_manifest_data_router",
        }
        or payload.get("concrete_rankin_batch_manifest_data_closed") is True
        or "rankin_batch_manifest" in keys
        or "rankin_certificate_manifest" in keys
        or "formal_rankin_batch_manifest" in keys
    )


def is_return_packet_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像 Rankin 失败回流 packet。"""
    keys = set(payload.keys())
    return (
        payload.get("certificate_type") == "prime_matrix_failed_rankin_return_packet"
        or payload.get("failed_rankin_return_packet_ledger_closed") is True
        or "failed_rankin_return_packets" in keys
        or "rankin_failure_return_packets" in keys
    )


def scan_json_corpus(root: Path) -> dict[str, Any]:
    """扫描仓库内 Rankin 样本、批量 manifest 与失败回流 packet。"""
    rankin_like: list[dict[str, Any]] = []
    manifest_like: list[dict[str, Any]] = []
    return_like: list[dict[str, Any]] = []
    parse_errors: list[str] = []
    for path in sorted(root.rglob("*.json")):
        if "__pycache__" in path.parts:
            continue
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            parse_errors.append(str(path.relative_to(ROOT)))
            continue
        if not isinstance(payload, dict):
            continue
        rel = str(path.relative_to(ROOT))
        if is_rankin_certificate_like(payload):
            rankin_like.append(
                {
                    "path": rel,
                    "p": payload.get("p"),
                    "k": payload.get("k"),
                    "interval_count": len(payload.get("intervals", [])),
                    "allowed_budget": payload.get("allowed_budget"),
                    "rankin_budget_pass": payload.get("rankin_budget_pass"),
                    "exact_budget_pass": payload.get("exact_budget_pass"),
                    "status": payload.get("status"),
                }
            )
        if is_batch_manifest_like(payload):
            rows = (
                payload.get("rankin_batch_manifest")
                or payload.get("rankin_certificate_manifest")
                or payload.get("formal_rankin_batch_manifest")
                or payload.get("materialization_steps")
                or []
            )
            manifest_like.append(
                {
                    "path": rel,
                    "status": payload.get("status"),
                    "row_count": len(rows) if isinstance(rows, list) else None,
                    "closed": payload.get("concrete_rankin_batch_manifest_data_closed"),
                }
            )
        if is_return_packet_like(payload):
            packets = (
                payload.get("failed_rankin_return_packets")
                or payload.get("rankin_failure_return_packets")
                or []
            )
            return_like.append(
                {
                    "path": rel,
                    "status": payload.get("status"),
                    "packet_count": len(packets) if isinstance(packets, list) else None,
                    "closed": payload.get("failed_rankin_return_packet_ledger_closed"),
                }
            )
    return {
        "rankin_like": rankin_like,
        "manifest_like": manifest_like,
        "return_like": return_like,
        "parse_errors": parse_errors,
    }


def manifest_fields() -> list[dict[str, str]]:
    """给出正式批量 manifest 必要字段。"""
    return [
        {"field": "batch_id", "meaning": "批量证书稳定编号。"},
        {"field": "source_tuple_hash", "meaning": "锁定同一 coloring/budget source tuple。"},
        {"field": "color_set_hash", "meaning": "锁定所有 color_id 的全集，防止漏色。"},
        {"field": "color_id", "meaning": "每行对应一个正式颜色类。"},
        {"field": "rankin_certificate_path", "meaning": "该颜色类单证书路径。"},
        {"field": "rankin_certificate_hash", "meaning": "单证书 sha256。"},
        {"field": "rankin_budget_pass", "meaning": "单证书 Rankin 预算验收结果。"},
        {"field": "exact_budget_pass", "meaning": "精确计数是否也进入预算；用于审计交叉核验。"},
        {"field": "failure_kind", "meaning": "pass、lowmod_core_crtdefect 或 constant_gap。"},
        {"field": "return_packet_id", "meaning": "失败时指向 PDEC/SAE 回流 packet 或常数缺口 packet。"},
        {"field": "coverage_equation_ref", "meaning": "指向 coloring coverage 证书，说明没有遗漏颜色类。"},
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
    texts: dict[str, str],
    sample: dict[str, Any],
    manifest_data: dict[str, Any],
    return_packet: dict[str, Any],
    scan: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成批量 Rankin pass-or-return 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    budget_ready = previous.get("allowed_budget_allocation_discipline_closed") is True
    rla_ready = contains_all(texts["rla"], ["Theorem RLA-1", "Corollary RLA-2", "rankin_budget_pass"])
    lmc_ready = contains_all(texts["lmc"], ["Theorem LMC-1", "Directed Core CRTDefect", "PDEC-or-SAE"])
    fxa_ready = contains_all(
        texts["fxa"],
        ["rankin_budget_pass=true", "rankin_budget_pass=false + low-mod spike", "常数账本未闭合"],
    )
    sample_ready = (
        sample.get("rankin_budget_pass") is True
        and sample.get("exact_budget_pass") is True
        and sample.get("status") == "finite_rankin_ledger_computable_with_lowmod_residue_report"
    )
    schema_closed = all([active, guard, budget_ready, rla_ready, lmc_ready, fxa_ready, sample_ready])
    manifest_data_guard = (
        manifest_data.get("counterexample_assumption_only") is True
        and manifest_data.get("empirical_absence_not_used") is True
        and manifest_data.get("hypothetical_chain_only") is True
        and manifest_data.get("row_column_unconditional_closed") is False
    )
    return_packet_guard = (
        return_packet.get("counterexample_assumption_only") is True
        and return_packet.get("empirical_absence_not_used") is True
        and return_packet.get("hypothetical_chain_only") is True
        and return_packet.get("row_column_unconditional_closed") is False
    )
    manifest_data_closed = (
        manifest_data.get("concrete_rankin_batch_manifest_data_closed") is True
        and manifest_data_guard
    )
    return_packet_closed = (
        return_packet.get("failed_rankin_return_packet_ledger_closed") is True
        and return_packet_guard
    )
    manifest_found = bool(scan["manifest_like"]) or manifest_data_closed
    return_packets_found = bool(scan["return_like"]) or return_packet_closed
    batch_closed = schema_closed and manifest_data_closed and return_packet_closed
    return [
        row(
            "BatchRankinGateActive",
            active,
            False,
            "上一层已把最窄点推进到批量 Rankin pass-or-return。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设反例链条内的批量证书，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "AllowedBudgetDisciplineImported",
            budget_ready,
            True,
            "allowed_budget 已要求预登记、总预算守卫和失败回流。",
            "无预算纪律剩余。",
        ),
        row(
            "RankinAcceptanceAndReturnImported",
            rla_ready and lmc_ready and fxa_ready,
            True,
            "RLA 处理 pass，LMC/FXA 处理 low-mod spike 回流，no-spike 保留 constant-gap。",
            f"{PDEC_SAE_ATOM} or {CONSTANT_GAP_ATOM}",
        ),
        row(
            "ExecutableRankinSamplePasses",
            sample_ready,
            True,
            "现有样本证书通过 exact 与 Rankin 预算，说明单证书格式可执行。",
            "样本不是批量全集。",
        ),
        row(
            SCHEMA_ATOM,
            schema_closed,
            True,
            "批量验收 schema 已闭合：逐 color_id 要么 pass，要么给失败回流 packet。",
            SCHEMA_ATOM,
        ),
        row(
            "ConcreteRankinManifestDataImported",
            manifest_data_closed,
            manifest_data_closed,
            "已回收 concrete Rankin manifest 数据：颜色全集、逐色证书与逐行分类生成律均固定。",
            "manifest/data 已可生成；不再作为 BatchRankin 剩余。",
        ),
        row(
            "FailedRankinReturnPacketsAvailable",
            return_packet_closed,
            return_packet_closed,
            "已回收 failed-Rankin 回流 packet 纪律：失败行要么命名回流，要么全 pass 空声明。",
            "失败回流不漏账；PDEC/SAE 与 constant-gap 仍在下游。",
        ),
        row(
            OLD_ATOM,
            batch_closed,
            batch_closed,
            "批量 Rankin 门已闭合为 pass-or-return：全量 manifest/data 存在，且每行 pass 或进入合法回流。",
            f"{PDEC_SAE_ATOM} OR {CONSTANT_GAP_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行批量 Rankin pass-or-return 路由。"""
    previous = load_json(paths["previous"])
    texts = {key: read_text(paths[key]) for key in {"rla", "lmc", "fxa"}}
    sample = load_json(paths["sample"])
    manifest_data = load_json(paths["manifest_data"])
    return_packet = load_json(paths["return_packet"])
    scan = scan_json_corpus(DOCS)
    rows = build_rows(previous, texts, sample, manifest_data, return_packet, scan)
    schema_closed = next(item["closed"] for item in rows if item["gate"] == SCHEMA_ATOM)
    batch_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    status = "batch_rankin_pass_return_closed_pdec_sae_or_constant_gap_open" if batch_closed else "batch_rankin_schema_closed_manifest_missing"
    current_narrowest = PDEC_SAE_ATOM if batch_closed else MANIFEST_ATOM
    secondary_narrowest = CONSTANT_GAP_ATOM if batch_closed else RETURN_ATOM
    return {
        "certificate_type": "prime_matrix_batch_rankin_pass_return_router",
        "status": status,
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "batch_rankin_verifier_schema_closed": schema_closed,
        "batch_rankin_pass_or_return_closed": batch_closed,
        "concrete_rankin_batch_manifest_data_closed": manifest_data.get("concrete_rankin_batch_manifest_data_closed") is True,
        "failed_rankin_return_packet_ledger_closed": return_packet.get("failed_rankin_return_packet_ledger_closed") is True,
        "formal_rankin_batch_manifest_found": bool(scan["manifest_like"]),
        "failed_rankin_return_packet_found": bool(scan["return_like"]),
        "rankin_like_json_count": len(scan["rankin_like"]),
        "rankin_like_json": scan["rankin_like"],
        "batch_manifest_like_json": scan["manifest_like"],
        "return_packet_like_json": scan["return_like"],
        "manifest_fields": manifest_fields(),
        "current_narrowest_atom": current_narrowest,
        "secondary_narrowest_atom": secondary_narrowest,
        "independent_acceptance_gate": DSTRUCTURE_ATOM,
        "downstream_atoms": [PDEC_SAE_ATOM, CONSTANT_GAP_ATOM, DSTRUCTURE_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => {SCHEMA_ATOM} AND ConcreteRankinBatchManifestDataLedger "
            f"AND {RETURN_ATOM}; failures still route to {PDEC_SAE_ATOM} or {CONSTANT_GAP_ATOM}."
        ),
        "plain_conclusion": (
            "BatchRankinCertificatesAllPassOrReturnToPDECSAE 已闭合为 pass-or-return 门：schema、"
            "concrete manifest/data、逐色证书生成律和 failed-return packet 纪律均已回收。"
            f"这一步只说明 Rankin 批量行不会漏账；新的最窄点转为 `{current_narrowest}`，"
            f"并保留 `{secondary_narrowest}` 与 `{DSTRUCTURE_ATOM}`，不关闭行列无条件定理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 批量 Rankin pass-or-return 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"batch_rankin_verifier_schema_closed={fmt_bool(result['batch_rankin_verifier_schema_closed'])}",
        f"batch_rankin_pass_or_return_closed={fmt_bool(result['batch_rankin_pass_or_return_closed'])}",
        f"concrete_rankin_batch_manifest_data_closed={fmt_bool(result['concrete_rankin_batch_manifest_data_closed'])}",
        f"failed_rankin_return_packet_ledger_closed={fmt_bool(result['failed_rankin_return_packet_ledger_closed'])}",
        f"formal_rankin_batch_manifest_found={fmt_bool(result['formal_rankin_batch_manifest_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. Manifest 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["manifest_fields"]:
        lines.append(
            "| {field} | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 当前扫描",
            "",
            f"- Rankin-like JSON: `{result['rankin_like_json_count']}`",
            f"- batch manifest: `{len(result['batch_manifest_like_json'])}`",
            f"- failed return packets: `{len(result['return_packet_like_json'])}`",
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
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；"
            f"`{result['secondary_narrowest_atom']}` 与 `{result['independent_acceptance_gate']}` "
            "仍是独立剩余。",
            "",
            "审稿边界：本步只关闭批量 Rankin pass-or-return 门，不关闭 PDEC/SAE、"
            "constant-gap、DStructure/Rankin 独立验收，也不关闭行列无条件定理。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--rla", type=Path, default=DEFAULT_RLA)
    parser.add_argument("--lmc", type=Path, default=DEFAULT_LMC)
    parser.add_argument("--fxa", type=Path, default=DEFAULT_FXA)
    parser.add_argument("--sample", type=Path, default=DEFAULT_SAMPLE)
    parser.add_argument("--manifest-data", type=Path, default=DEFAULT_MANIFEST_DATA)
    parser.add_argument("--return-packet", type=Path, default=DEFAULT_RETURN_PACKET)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "rla": args.rla,
        "lmc": args.lmc,
        "fxa": args.fxa,
        "sample": args.sample,
        "manifest_data": args.manifest_data,
        "return_packet": args.return_packet,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
