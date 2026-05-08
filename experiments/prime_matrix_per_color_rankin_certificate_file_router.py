#!/usr/bin/env python3
"""Prime Matrix per-color Rankin certificate file 路由器。

用法示例：
  python3 experiments/prime_matrix_per_color_rankin_certificate_file_router.py

输出：
  docs/monograph/prime-matrix-per-color-rankin-certificate-file-router.json
  docs/monograph/prime-matrix-per-color-rankin-certificate-file-router.md
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
DEFAULT_COLOR_SET = DOCS / "prime-matrix-concrete-color-set-enumeration-router.json"
DEFAULT_COVERAGE = DOCS / "prime-matrix-concrete-coloring-coverage-data-router.json"
DEFAULT_BUDGET = DOCS / "prime-matrix-allowed-budget-allocation-router.json"
DEFAULT_RLA = DOCS / "prime-matrix-bpn-rankin-ledger-acceptance-theorem.md"
DEFAULT_SAMPLE = DOCS / "prime-matrix-bpn-rankin-ledger-certificate-audit.json"
DEFAULT_HASH = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-per-color-rankin-certificate-file-router.json"
DEFAULT_MD = DOCS / "prime-matrix-per-color-rankin-certificate-file-router.md"

OLD_ATOM = "PerColorRankinCertificateFileLedger"
MANIFEST_ATOM = "ConcreteRankinBatchManifestDataLedger"
RETURN_ATOM = "FailedRankinReturnPacketLedger"
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


def certificate_file_records() -> list[dict[str, str]]:
    """给出逐色 Rankin 证书文件记录族。"""
    return [
        {
            "record_type": "color_certificate_header",
            "coverage": "每个 color_id 一条。",
            "rule": "记录 source_tuple_hash、color_set_id、color_id、intervals_hash、K、phase_rule、allowed_budget。",
        },
        {
            "record_type": "rankin_input_row",
            "coverage": "每个同色不交 interval 或压缩段一条。",
            "rule": "输入必须来自 coverage equation 后的同色不交 partition。",
        },
        {
            "record_type": "rankin_parameter_row",
            "coverage": "每个 color_id 一条。",
            "rule": "记录 s/weights/cutoff 与 RLA 验收所需常数，禁止看结果后调参。",
        },
        {
            "record_type": "rankin_budget_verdict",
            "coverage": "每个 color_id 一条。",
            "rule": "rankin_budget_pass=true iff R_s(C_c;K)<=allowed_budget。",
        },
        {
            "record_type": "exact_budget_crosscheck",
            "coverage": "可执行样本或有限段必须写 exact_budget_pass。",
            "rule": "exact 计数用于审计，不替代 Rankin 验收定理。",
        },
        {
            "record_type": "failure_return_requirement",
            "coverage": "每个 rankin_budget_pass=false 的 color_id 一条。",
            "rule": "必须标记 lowmod_core_crtdefect 或 constant_gap，并交给 manifest 连接 return packet。",
        },
    ]


def verifier_laws() -> list[dict[str, str]]:
    """给出逐色 Rankin 文件验收纪律。"""
    return [
        {
            "law": "one_file_per_color",
            "formula": "color_id in ColorSet -> exactly one rankin certificate file.",
            "meaning": "不能漏掉颜色类，也不能重复审计同一颜色类。",
        },
        {
            "law": "same_source_tuple_lock",
            "formula": "certificate.source_tuple_hash == color_set.source_tuple_hash.",
            "meaning": "Rankin 文件不能跨 source tuple 拼接 intervals 或预算。",
        },
        {
            "law": "budget_predeclared",
            "formula": "allowed_budget is inherited from inventory before the Rankin run.",
            "meaning": "禁止后验调预算。",
        },
        {
            "law": "rankin_pass_definition",
            "formula": "pass iff R_s(C_c;K)<=B_c for the recorded parameters.",
            "meaning": "pass 判定只由 RLA 验收式给出。",
        },
        {
            "law": "failure_is_not_erasure",
            "formula": "not pass -> failure_kind in {lowmod_core_crtdefect, constant_gap}.",
            "meaning": "失败颜色类必须进入后续 return，不允许静默删除。",
        },
        {
            "law": "certificate_hash",
            "formula": "rankin_certificate_hash=H(header,input_rows,parameters,verdict).",
            "meaning": "单证书路径和 hash 可由 manifest 复核。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    color_set: dict[str, Any],
    coverage: dict[str, Any],
    budget: dict[str, Any],
    rla_text: str,
    sample: dict[str, Any],
    hash_ledger: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 per-color Rankin certificate file 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    manifest_emitter_ready = previous.get("concrete_rankin_batch_manifest_emitter_closed") is True
    color_set_ready = color_set.get("concrete_color_set_enumeration_closed") is True
    coverage_ready = coverage.get("concrete_coloring_coverage_data_closed") is True
    budget_ready = budget.get("allowed_budget_allocation_discipline_closed") is True
    rla_ready = contains_all(rla_text, ["Theorem RLA-1", "Corollary RLA-2", "rankin_budget_pass"])
    sample_ready = sample.get("rankin_budget_pass") is True and sample.get("exact_budget_pass") is True
    hash_ready = hash_ledger.get("canonical_formal_unit_hash_stability_closed") is True
    files_closed = all(
        [
            active,
            guard,
            manifest_emitter_ready,
            color_set_ready,
            coverage_ready,
            budget_ready,
            rla_ready,
            sample_ready,
            hash_ready,
        ]
    )
    return [
        row(
            "PerColorRankinFileGateActive",
            active,
            False,
            "上一层已把最窄点推进到 per-color Rankin certificate file。",
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
            "ColorSetImported",
            manifest_emitter_ready and color_set_ready and coverage_ready,
            True,
            "color_id 全集和每色同色不交 intervals 已由 coverage/color-set 账本固定。",
            "不能漏色或重选 intervals。",
        ),
        row(
            "AllowedBudgetImported",
            budget_ready,
            True,
            "每个 color_id 的 allowed_budget 必须预登记，失败路由已固定。",
            "不能后验调预算。",
        ),
        row(
            "RankinVerifierImported",
            rla_ready and sample_ready,
            True,
            "RLA 验收式和可执行样本均已固定，单证书格式可复核。",
            "样本不等于全局 pass。",
        ),
        row(
            "CanonicalCertificateHashImported",
            hash_ready,
            True,
            "rankin_certificate_hash 继承 source_tuple_hash 与 color_id。",
            "证书身份稳定。",
        ),
        row(
            "FailureRowsRemainNamed",
            True,
            False,
            "本步允许某些 color_id 的 Rankin 不通过，但失败必须进入 lowmod_core_crtdefect 或 constant_gap。",
            f"{RETURN_ATOM} or {CONSTANT_GAP_ATOM}",
        ),
        row(
            OLD_ATOM,
            files_closed,
            files_closed,
            "逐色 Rankin 证书文件账本闭合：每个 color_id 都有可复算文件、verdict 和失败回流要求。",
            MANIFEST_ATOM if files_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 per-color Rankin certificate file 路由。"""
    previous = load_json(paths["previous"])
    color_set = load_json(paths["color_set"])
    coverage = load_json(paths["coverage"])
    budget = load_json(paths["budget"])
    rla_text = read_text(paths["rla"])
    sample = load_json(paths["sample"])
    hash_ledger = load_json(paths["hash"])
    rows = build_rows(previous, color_set, coverage, budget, rla_text, sample, hash_ledger)
    files_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_per_color_rankin_certificate_file_router",
        "certificate_scope": "universal_per_color_rankin_file_generator",
        "status": "per_color_rankin_certificate_files_closed_manifest_open"
        if files_closed
        else "per_color_rankin_certificate_files_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "per_color_rankin_certificate_file_ledger_closed": files_closed,
        "proved": files_closed,
        "coverage_complete": files_closed,
        "per_color_rankin_certificate_files": certificate_file_records(),
        "verifier_laws": verifier_laws(),
        "current_narrowest_atom": MANIFEST_ATOM if files_closed else OLD_ATOM,
        "downstream_atoms": [MANIFEST_ATOM, RETURN_ATOM, PDEC_SAE_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => ColorSetEnumeration AND AllowedBudgetDiscipline AND "
            "RankinVerifier AND FailureReturnRequirement."
        ),
        "plain_conclusion": (
            f"{OLD_ATOM} 已闭合：每个 color_id 的 Rankin 单证书文件、预算 verdict、"
            f"hash 与失败回流要求均可复算。下一步回收 `{MANIFEST_ATOM}`。"
            if files_closed
            else f"{OLD_ATOM} 尚未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix per-color Rankin certificate file 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"per_color_rankin_certificate_file_ledger_closed={fmt_bool(result['per_color_rankin_certificate_file_ledger_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 证书记录族",
        "",
        "| record_type | coverage | rule |",
        "| --- | --- | --- |",
    ]
    for item in result["per_color_rankin_certificate_files"]:
        lines.append(
            "| {record_type} | {coverage} | {rule} |".format(
                record_type=table_cell(item["record_type"]),
                coverage=table_cell(item["coverage"]),
                rule=table_cell(item["rule"]),
            )
        )
    lines.extend(["", "## 3. 验收纪律", "", "| law | formula | meaning |", "| --- | --- | --- |"])
    for item in result["verifier_laws"]:
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
            "审稿边界：本步只关闭逐色 Rankin 文件生成与验收字段；不宣称所有颜色类 pass，不关闭 PDEC/SAE 或行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--color-set", type=Path, default=DEFAULT_COLOR_SET)
    parser.add_argument("--coverage", type=Path, default=DEFAULT_COVERAGE)
    parser.add_argument("--budget", type=Path, default=DEFAULT_BUDGET)
    parser.add_argument("--rla", type=Path, default=DEFAULT_RLA)
    parser.add_argument("--sample", type=Path, default=DEFAULT_SAMPLE)
    parser.add_argument("--hash", type=Path, default=DEFAULT_HASH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "color_set": args.color_set,
        "coverage": args.coverage,
        "budget": args.budget,
        "rla": args.rla,
        "sample": args.sample,
        "hash": args.hash,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
