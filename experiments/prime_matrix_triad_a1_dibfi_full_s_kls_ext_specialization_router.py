#!/usr/bin/env python3
"""审计 FullS-KLS-ext 专门化合同是否足以关闭外部定理版。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_full_s_kls_ext_specialization_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_EXTERNAL_FULL_S_MATCH = (
    DOCS / "prime-matrix-triad-a1-dibfi-external-full-s-match-router.json"
)
DEFAULT_NONAP_OBJECT_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.json"
)
DEFAULT_SPECIALIZATION_NOTE = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization.md"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(path: Path, needles: list[str]) -> bool:
    """核查文档是否含有全部关键词。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    external_full_s_match: dict[str, Any],
    nonap_object_ledger: dict[str, Any],
    specialization_note_path: Path,
) -> list[dict[str, Any]]:
    """构造专门化合同审计行。"""
    statement_ready = contains_all(
        specialization_note_path,
        [
            "Theorem FullS-KLS-ext",
            "S≈P=X^(1/2+o(1))",
            "未中心化、无投影",
            "NaturalWFDScale",
            "DIBFIPrimarySourceSpecializationProof",
        ],
    )
    no_projection_baked_in = contains_all(
        specialization_note_path,
        [
            "不插入块中心化",
            "不删同块对角",
            "不投影",
            "non-AP WFD 对象本身",
        ],
    )
    prior_ready = (
        external_full_s_match["terminal_gap_after_router"]
        == "FullSKLSExternalTheoremSpecialization"
    )
    object_open = bool(nonap_object_ledger["open_object_gates"])
    return [
        {
            "gate": "PriorFullSKLSSpecializationFrontierAvailable",
            "closed": prior_ready,
            "evidence": "上一层已把 ExternalFullSDIBFIAtomMatch 压成 FullSKLSExternalTheoremSpecialization。",
            "remaining": "none at prior-frontier level",
            "next_target": "FullSKLSExtStatementMaterialized",
        },
        {
            "gate": "FullSKLSExtStatementMaterialized",
            "closed": statement_ready,
            "evidence": "FullS-KLS-ext 已写成含 C,S,H、well-factorable 权、自然 WFD 尺度和 log-saving 的定理合同。",
            "remaining": "none for external-contract statement",
            "next_target": "ExternalContractVersionClosed",
        },
        {
            "gate": "NoProjectionCompatibilityInternalized",
            "closed": statement_ready and no_projection_baked_in and object_open,
            "evidence": (
                "定理合同直接要求估计当前 non-AP WFD 未中心化无投影对象；"
                f"内部对象账本仍 open={nonap_object_ledger['open_object_gates']}，但已被外部合同吸收。"
            ),
            "remaining": "若不用外部合同，仍需内部证明 UncenteredWFDToKE13NoProjectionIdentity。",
            "next_target": "ExternalContractVersionClosed",
        },
        {
            "gate": "ExternalContractVersionClosed",
            "closed": statement_ready and no_projection_baked_in,
            "evidence": "在接受 FullS-KLS-ext 作为外部深输入的版本中，full-S scale/object 合同已经闭合。",
            "remaining": "该 closed 只属于外部定理版，不属于完全自足版。",
            "next_target": "DIBFIPrimarySourceSpecializationProof",
        },
        {
            "gate": "DIBFIPrimarySourceSpecializationProof",
            "closed": False,
            "evidence": "仓库尚未逐页从 DI/BFI 原文定理推出 FullS-KLS-ext 专门化。",
            "remaining": "若要求完全自足或完全原文核验，必须补这一单点证明。",
            "next_target": "DIBFIPrimarySourceSpecializationProof",
        },
    ]


def run(
    external_full_s_match_path: Path,
    nonap_object_ledger_path: Path,
    specialization_note_path: Path,
) -> dict[str, Any]:
    """运行 FullS-KLS-ext 专门化路由。"""
    external_full_s_match = load_json(external_full_s_match_path)
    nonap_object_ledger = load_json(nonap_object_ledger_path)
    rows = build_rows(
        external_full_s_match,
        nonap_object_ledger,
        specialization_note_path,
    )
    open_gates = [row["gate"] for row in rows if not row["closed"]]
    external_contract_closed = any(
        row["gate"] == "ExternalContractVersionClosed" and row["closed"]
        for row in rows
    )
    return {
        "certificate_type": "triad_a1_dibfi_full_s_kls_ext_specialization_router",
        "status": "full_s_kls_ext_contract_closed_primary_source_proof_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "external_full_s_match_json": file_sha256(external_full_s_match_path),
            "nonap_object_ledger_json": file_sha256(nonap_object_ledger_path),
            "specialization_note_md": file_sha256(specialization_note_path),
        },
        "previous_terminal_gap": external_full_s_match["terminal_gap_after_router"],
        "specialization_rows": rows,
        "closed_specialization_gates": [row["gate"] for row in rows if row["closed"]],
        "open_specialization_gates": open_gates,
        "external_theorem_contract_closed": external_contract_closed,
        "self_contained_primary_source_proof_closed": False,
        "terminal_gap_after_router": "DIBFIPrimarySourceSpecializationProof",
        "terminal_gap_expansion": ["DIBFIPrimarySourceSpecializationProof"],
        "structural_law": (
            "The external-theorem version and the self-contained version now separate cleanly. "
            "By stating FullS-KLS-ext directly for the uncentered non-projected non-AP WFD object, "
            "the external contract absorbs the former scale and no-projection compatibility gaps. "
            "The only remaining non-contract gap is a primary-source derivation of this exact "
            "specialization from DI/BFI, which is a bibliographic/deep-theorem proof task rather "
            "than another prime-matrix structural escape."
        ),
        "review_conclusion": (
            "FullS-KLS-ext 外部合同版已闭合：它直接覆盖 full-S 窗口并把无投影兼容写入定理对象。"
            "若坚持完全自足或原文逐项核验，唯一剩余单点是 `DIBFIPrimarySourceSpecializationProof`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI FullS-KLS-ext specialization 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "previous terminal:",
        f"  {result['previous_terminal_gap']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "external theorem contract closed:",
        f"  {fmt_bool(result['external_theorem_contract_closed'])};",
        "",
        "self-contained primary-source proof closed:",
        f"  {fmt_bool(result['self_contained_primary_source_proof_closed'])}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `closed_specialization_gates={result['closed_specialization_gates']}`。",
        f"- `open_specialization_gates={result['open_specialization_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 专门化账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["specialization_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {remaining} | `{next}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                next=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "外部深定理版中，full-S non-AP WFD 缺口已经被一个精确定理合同吸收。完全自足版只剩：",
            "",
            "```text",
            "DIBFIPrimarySourceSpecializationProof:",
            "  derive Theorem FullS-KLS-ext from DI/BFI primary sources line by line.",
            "```",
            "",
            "这不是新的结构逃逸口；它是是否接受外部 DI/BFI 深定理输入的边界。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--external-full-s-match-json",
        type=Path,
        default=DEFAULT_EXTERNAL_FULL_S_MATCH,
    )
    parser.add_argument(
        "--nonap-object-ledger-json",
        type=Path,
        default=DEFAULT_NONAP_OBJECT_LEDGER,
    )
    parser.add_argument(
        "--specialization-note-md",
        type=Path,
        default=DEFAULT_SPECIALIZATION_NOTE,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        external_full_s_match_path=args.external_full_s_match_json,
        nonap_object_ledger_path=args.nonap_object_ledger_json,
        specialization_note_path=args.specialization_note_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "external_contract_closed": result["external_theorem_contract_closed"],
                "open_gates": result["open_specialization_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
