#!/usr/bin/env python3
"""审查完整全局无条件行命题能否由当前材料自足闭合。

用法示例：
  python3 experiments/prime_matrix_global_unconditional_self_contained_obstruction_router.py

输出：
  docs/monograph/prime-matrix-global-unconditional-self-contained-obstruction-router.json
  docs/monograph/prime-matrix-global-unconditional-self-contained-obstruction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_FINAL_THEOREM = (
    DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json"
)
DEFAULT_TAXONOMY = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"
)
DEFAULT_SOURCE_ANTIATOM = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
)
DEFAULT_DIBFI_TRANSFER = (
    DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
)
DEFAULT_LINE_REF = DOCS / "line-by-line-internal-referee-matrix.md"
DEFAULT_CLAIM_STATUS = DOCS / "claim-status-table.md"
DEFAULT_JSON = (
    DOCS / "prime-matrix-global-unconditional-self-contained-obstruction-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-global-unconditional-self-contained-obstruction-router.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def obstruction_row(
    gate: str,
    verdict: str,
    evidence: str,
    implication: str,
    required_for_global_closure: bool,
) -> dict[str, Any]:
    """构造全局无条件自足闭合阻断审查行。"""
    return {
        "gate": gate,
        "verdict": verdict,
        "evidence": evidence,
        "implication": implication,
        "required_for_global_closure": required_for_global_closure,
    }


def build_rows(
    final_theorem: dict[str, Any],
    taxonomy: dict[str, Any],
    source_antiatom: dict[str, Any],
    dibfi_transfer: dict[str, Any],
    line_ref_text: str,
    claim_status_text: str,
) -> list[dict[str, Any]]:
    """生成阻断审查表。"""
    canonical_closed = (
        final_theorem["canonical_source_self_contained_theorem_closed"]
        and final_theorem["open_self_contained_gates"] == []
    )
    generic_refuted = (
        taxonomy["generic_self_contained_version_refuted"]
        and not taxonomy["original_unrestricted_self_contained_version_closed"]
    )
    actual_source_bridge_open = not taxonomy["actual_source_bridge_theorem_closed"]
    antiatom_open = not source_antiatom["source_antiatom_reduction_closed"]
    dibfi_no_projection_open = not dibfi_transfer["all_certificate_rows_closed"]
    referee_open = "BLOCK-REFEREE" in line_ref_text
    status_disciplined = has_all(
        claim_status_text,
        [
            "canonical-source自足命题最终闭合路由",
            "完整 Prime Matrix 行/列无条件定理",
            "DStructureRankinReferee",
        ],
    )

    return [
        obstruction_row(
            gate="CanonicalSourceExactBoundaryClosed",
            verdict="closed",
            evidence=final_theorem["terminal_boundary"],
            implication="精确 canonical-source 自足命题已经闭合，不能再把它当作未完成硬点。",
            required_for_global_closure=False,
        ),
        obstruction_row(
            gate="UnrestrictedGenericWFD",
            verdict="refuted_not_claimed" if generic_refuted else "ambiguous",
            evidence=taxonomy["terminal_gap_after_router"],
            implication=(
                "unrestricted generic WFD 不能通过当前自足链闭合；若要全局化，必须改变源命题，"
                "证明实际源锁定或强化反原子，而不是重用已反证模板。"
            ),
            required_for_global_closure=True,
        ),
        obstruction_row(
            gate="ActualFullSSourceBridge",
            verdict="open" if actual_source_bridge_open else "closed",
            evidence=", ".join(taxonomy["open_taxonomy_gates"]),
            implication="必须证明实际 full-S non-AP 源头等于 canonical 源，或满足强化 source anti-atom。",
            required_for_global_closure=True,
        ),
        obstruction_row(
            gate="FullSNonAPStrengthenedSourceAntiAtom",
            verdict="open" if antiatom_open else "closed",
            evidence=", ".join(source_antiatom["open_antiatom_gates"]),
            implication="当前已知形式 WFD/K4-K6/因子-余数 incidence 都不能推出所需反原子。",
            required_for_global_closure=True,
        ),
        obstruction_row(
            gate="DIBFIQuantifiedNoProjectionWindowCertificate",
            verdict="open_external_or_new_proof_needed"
            if dibfi_no_projection_open
            else "closed",
            evidence="; ".join(dibfi_transfer["open_terminal_targets"]),
            implication=(
                "若走 generic/external DI/BFI 路线，仍需无投影未中心化 dispersion 恒等式与量化窗口代入。"
            ),
            required_for_global_closure=True,
        ),
        obstruction_row(
            gate="DStructureTailLog4FiniteRankinPromotion",
            verdict="referee_block" if referee_open else "closed",
            evidence="PM-16 BLOCK-REFEREE" if referee_open else "no block token",
            implication=(
                "完整行/列无条件定理晋级仍需 D-structure/Tail-log4/finite Rankin 接口被独立接受。"
            ),
            required_for_global_closure=True,
        ),
        obstruction_row(
            gate="ClaimStatusDiscipline",
            verdict="guarded" if status_disciplined else "needs_update",
            evidence="claim-status table separates closed canonical theorem from global non-claim",
            implication="当前材料已经防止把条件/边界闭合误写成完整无条件闭合。",
            required_for_global_closure=False,
        ),
    ]


def run(
    final_theorem_path: Path,
    taxonomy_path: Path,
    source_antiatom_path: Path,
    dibfi_transfer_path: Path,
    line_ref_path: Path,
    claim_status_path: Path,
) -> dict[str, Any]:
    """运行完整全局无条件自足闭合阻断审查。"""
    final_theorem = load_json(final_theorem_path)
    taxonomy = load_json(taxonomy_path)
    source_antiatom = load_json(source_antiatom_path)
    dibfi_transfer = load_json(dibfi_transfer_path)
    line_ref_text = read_text(line_ref_path)
    claim_status_text = read_text(claim_status_path)

    rows = build_rows(
        final_theorem=final_theorem,
        taxonomy=taxonomy,
        source_antiatom=source_antiatom,
        dibfi_transfer=dibfi_transfer,
        line_ref_text=line_ref_text,
        claim_status_text=claim_status_text,
    )
    blocking_gates = [
        row["gate"]
        for row in rows
        if row["required_for_global_closure"]
        and row["verdict"] not in {"closed", "guarded"}
    ]
    current_corpus_global_closure_possible = not blocking_gates

    return {
        "certificate_type": "prime_matrix_global_unconditional_self_contained_obstruction_router",
        "status": "global_unconditional_self_contained_closure_blocked_by_named_external_or_new_inputs",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "final_theorem": file_sha256(final_theorem_path),
            "taxonomy": file_sha256(taxonomy_path),
            "source_antiatom": file_sha256(source_antiatom_path),
            "dibfi_transfer": file_sha256(dibfi_transfer_path),
            "line_referee": file_sha256(line_ref_path),
            "claim_status": file_sha256(claim_status_path),
        },
        "canonical_source_self_contained_theorem_closed": final_theorem[
            "canonical_source_self_contained_theorem_closed"
        ],
        "current_corpus_global_unconditional_self_contained_closure_possible": (
            current_corpus_global_closure_possible
        ),
        "row_column_unconditional_closed": False,
        "global_unrestricted_terminal_family_exclusion_closed": False,
        "blocking_gates_for_full_global_closure": blocking_gates,
        "minimal_new_inputs_to_attempt_full_closure": [
            "ActualA1FullSSourceLockTheorem_OR_FullSNonAPStrengthenedSourceAntiAtom",
            "NoProjectionUncenteredDispersionIdentity",
            "QuantifiedDIBFIWindowSubstitution",
            "DStructureTailLog4FiniteRankinIndependentAcceptance",
        ],
        "rows": rows,
        "obstruction_law": (
            "The current corpus fully closes the canonical-source self-contained theorem "
            "boundary, but it cannot honestly close the unrestricted/global row-column "
            "theorem. The generic WFD self-contained strengthening is refuted, the actual "
            "full-S source bridge or strengthened anti-atom theorem is open, the DI/BFI "
            "no-projection quantified certificate is open, and final D-structure/Rankin "
            "promotion remains a referee block."
        ),
        "review_conclusion": (
            "完整全局无条件自足闭合不能由当前材料直接完成。当前已闭合的是 canonical-source "
            "自足命题；要继续越过边界，必须新增实际 full-S 源锁定/强化反原子证明，或完成 "
            "DI/BFI 无投影量化证书，并通过 D-structure/Tail-log4/finite Rankin 独立晋级门。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 完整全局无条件自足闭合阻断路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 阻断律",
        "",
        result["obstruction_law"],
        "",
        "```text",
        f"canonical_source_self_contained_theorem_closed={fmt_bool(result['canonical_source_self_contained_theorem_closed'])}",
        (
            "current_corpus_global_unconditional_self_contained_closure_possible="
            f"{fmt_bool(result['current_corpus_global_unconditional_self_contained_closure_possible'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 完整闭合所需新增输入",
        "",
    ]
    for item in result["minimal_new_inputs_to_attempt_full_closure"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 3. 审查表",
            "",
            "| gate | verdict | required for global closure | evidence | implication |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{verdict}` | `{required}` | {evidence} | {implication} |".format(
                gate=table_cell(row["gate"]),
                verdict=table_cell(row["verdict"]),
                required=fmt_bool(bool(row["required_for_global_closure"])),
                evidence=table_cell(row["evidence"]),
                implication=table_cell(row["implication"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最终判定",
            "",
            "当前材料不能把完整全局无条件行/列命题自足闭合。继续推进必须选择一个新增输入方向："
            "证明实际 full-S 源锁定/强化反原子，或完成外部 DI/BFI 的无投影量化证书，或通过"
            " D-structure/Tail-log4/finite Rankin 独立审稿晋级门。否则只能保持 canonical-source"
            " 自足命题闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-theorem-json", type=Path, default=DEFAULT_FINAL_THEOREM)
    parser.add_argument("--taxonomy-json", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument(
        "--source-antiatom-json", type=Path, default=DEFAULT_SOURCE_ANTIATOM
    )
    parser.add_argument("--dibfi-transfer-json", type=Path, default=DEFAULT_DIBFI_TRANSFER)
    parser.add_argument("--line-ref-md", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--claim-status-md", type=Path, default=DEFAULT_CLAIM_STATUS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        final_theorem_path=args.final_theorem_json,
        taxonomy_path=args.taxonomy_json,
        source_antiatom_path=args.source_antiatom_json,
        dibfi_transfer_path=args.dibfi_transfer_json,
        line_ref_path=args.line_ref_md,
        claim_status_path=args.claim_status_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["blocking_gates_for_full_global_closure"])


if __name__ == "__main__":
    main()
