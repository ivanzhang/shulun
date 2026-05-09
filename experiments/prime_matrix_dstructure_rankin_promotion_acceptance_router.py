#!/usr/bin/env python3
"""固定 DStructureRankinPromotionPackage 的最终晋级验收边界。

用法示例：
  python3 experiments/prime_matrix_dstructure_rankin_promotion_acceptance_router.py

输出：
  docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.json
  docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph"

DEFAULT_ATLAS = DOCS / "prime-matrix-closure-input-atlas-router.json"
DEFAULT_TERMINAL_PROMOTION = (
    DOCS / "prime-matrix-canonical-terminal-promotion-closure-router.json"
)
DEFAULT_LINE_REF = DOCS / "line-by-line-internal-referee-matrix.md"
DEFAULT_RANKIN_ACCEPTANCE = DOCS / "prime-matrix-bpn-rankin-ledger-acceptance-theorem.md"
DEFAULT_RANKIN_AUDIT = DOCS / "prime-matrix-bpn-rankin-ledger-certificate-audit.json"
DEFAULT_FULL_RANKIN = DOCS / "prime-matrix-full-rankin-ledger-inventory-router.json"
DEFAULT_CLAIM_STATUS = DOCS / "claim-status-table.md"
DEFAULT_MAIN_TEX = PAPER / "contradiction-field-monograph.tex"
DEFAULT_JSON = (
    DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
)
DEFAULT_MD = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    boundary_closed: bool,
    accepted: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造第三包验收边界行。"""
    return {
        "gate": gate,
        "boundary_closed": boundary_closed,
        "accepted": accepted,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    atlas: dict[str, Any],
    terminal_promotion: dict[str, Any],
    line_ref_text: str,
    rankin_acceptance_text: str,
    rankin_audit: dict[str, Any],
    full_rankin: dict[str, Any],
    claim_status_text: str,
    main_tex_text: str,
) -> list[dict[str, Any]]:
    """生成 D-structure/Rankin 晋级验收边界表。"""
    package_listed = any(
        item.get("input") == "DStructureRankinPromotionPackage"
        for item in atlas.get("minimal_input_basis", [])
    )
    separated_from_canonical = (
        terminal_promotion.get("open_final_gates") == ["DStructureRankinRefereeStillOpen"]
        and terminal_promotion.get("row_column_unconditional_closed") is False
    )
    d_structure_guarded = contains_all(
        line_ref_text,
        [
            "PM-5",
            "PASS-CONDITIONAL",
            "Structured-EHPD",
            "PM-16",
            "BLOCK-REFEREE",
        ],
    )
    tail_log4_guarded = contains_all(
        line_ref_text,
        ["PM-7", "Tail-log4", "PASS-CONDITIONAL", "BG/RKS 外部定理号仍需核验"],
    )
    finite_verification_guarded = contains_all(
        line_ref_text,
        ["PM-15", "有限验证", "PASS-CONDITIONAL", "脚本 hash"],
    )
    rankin_schema_ready = contains_all(
        rankin_acceptance_text,
        [
            "Theorem RLA-1",
            "Rankin certificates for all colored corridors",
            "low-mod core CRTDefect",
        ],
    ) and (
        rankin_audit.get("status")
        == "finite_rankin_ledger_computable_with_lowmod_residue_report"
        and rankin_audit.get("rankin_budget_pass") is True
            and rankin_audit.get("exact_budget_pass") is True
    )
    full_rankin_pass_or_return_closed = (
        full_rankin.get("full_rankin_ledger_still_open_closed") is True
        and full_rankin.get("batch_rankin_pass_or_return_closed") is True
        and full_rankin.get("concrete_rankin_batch_manifest_data_closed") is True
        and full_rankin.get("row_column_unconditional_closed") is False
    )
    no_author_promotion = contains_all(
        line_ref_text,
        ["本轮没有把任何 `BLOCK-REFEREE` 改写为 `PASS-AUTHOR`", "不能升级为"],
    ) and contains_all(
        main_tex_text,
        [
            "An author-side check cannot replace independent referee verification",
            "not yet a final unconditional theorem manuscript",
        ],
    )

    return [
        row(
            gate="PromotionPackageListedAsMinimalInput",
            boundary_closed=package_listed,
            accepted=False,
            evidence="closure input atlas",
            meaning="第三包已经作为最小输入基的一项独立列出。",
            remaining="accept D-structure/Tail-log4/finite Rankin interfaces",
        ),
        row(
            gate="SeparatedFromCanonicalSelfContainedBoundary",
            boundary_closed=separated_from_canonical,
            accepted=False,
            evidence="canonical terminal promotion closure",
            meaning="DStructureRankinReferee 是最终定理晋级门，不是 canonical 自足边界缺口。",
            remaining="independent final-promotion review",
        ),
        row(
            gate="DStructureStructuredEHPDGuarded",
            boundary_closed=d_structure_guarded,
            accepted=False,
            evidence="line-by-line matrix PM-5/PM-16",
            meaning="行/列反例到 Structured-EHPD 的入口为条件通过，终局保持外审阻断。",
            remaining="independent acceptance of D-group definitions and reductions",
        ),
        row(
            gate="TailLog4Guarded",
            boundary_closed=tail_log4_guarded,
            accepted=False,
            evidence="line-by-line matrix PM-7",
            meaning="Tail-log4 已定理化为接口，但 BG/RKS 外部定理号和适配仍需核验。",
            remaining="verify BG/RKS theorem numbers and Tail-log4 adaptation",
        ),
        row(
            gate="FiniteVerificationGuarded",
            boundary_closed=finite_verification_guarded,
            accepted=False,
            evidence="line-by-line matrix PM-15",
            meaning="阈值以下有限验证是条件通过，需复现环境和脚本 hash。",
            remaining="reproducible finite-verification archive",
        ),
        row(
            gate="FiniteRankinSchemaReady",
            boundary_closed=rankin_schema_ready,
            accepted=False,
            evidence="Rankin acceptance theorem + sample audit",
            meaning="Rankin 账本已从口头常数变为可验收证书格式，样本证书通过。",
            remaining="full pass-or-return ledger imported in the next row",
        ),
        row(
            gate="FullRankinLedgerPassOrReturnClosed",
            boundary_closed=full_rankin_pass_or_return_closed,
            accepted=False,
            evidence="full Rankin ledger inventory router",
            meaning="正式 Rankin 证书全集缺口已由 concrete manifest/data 与 BatchRankin pass-or-return 回收。",
            remaining="independent acceptance of the Rankin subledger and downstream returns",
        ),
        row(
            gate="NoAuthorSidePromotion",
            boundary_closed=no_author_promotion,
            accepted=False,
            evidence="line-by-line matrix + main theorem boundary",
            meaning="作者侧复核不能替代独立外审，主稿不得升级为最终无条件定理。",
            remaining="external/referee acceptance",
        ),
    ]


def run(
    atlas_path: Path,
    terminal_promotion_path: Path,
    line_ref_path: Path,
    rankin_acceptance_path: Path,
    rankin_audit_path: Path,
    full_rankin_path: Path,
    claim_status_path: Path,
    main_tex_path: Path,
) -> dict[str, Any]:
    """运行 D-structure/Rankin 晋级验收边界路由。"""
    atlas = load_json(atlas_path)
    terminal_promotion = load_json(terminal_promotion_path)
    line_ref_text = read_text(line_ref_path)
    rankin_acceptance_text = read_text(rankin_acceptance_path)
    rankin_audit = load_json(rankin_audit_path)
    full_rankin = load_json(full_rankin_path)
    claim_status_text = read_text(claim_status_path)
    main_tex_text = read_text(main_tex_path)
    rows = build_rows(
        atlas=atlas,
        terminal_promotion=terminal_promotion,
        line_ref_text=line_ref_text,
        rankin_acceptance_text=rankin_acceptance_text,
        rankin_audit=rankin_audit,
        full_rankin=full_rankin,
        claim_status_text=claim_status_text,
        main_tex_text=main_tex_text,
    )
    boundary_closed = all(item["boundary_closed"] for item in rows)
    accepted = all(item["accepted"] for item in rows)
    evidence_paths = [
        atlas_path,
        terminal_promotion_path,
        line_ref_path,
        rankin_acceptance_path,
        rankin_audit_path,
        full_rankin_path,
        claim_status_path,
        main_tex_path,
    ]
    return {
        "certificate_type": "prime_matrix_dstructure_rankin_promotion_acceptance_router",
        "status": (
            "dstructure_rankin_promotion_boundary_closed_referee_acceptance_open"
            if boundary_closed and not accepted
            else "dstructure_rankin_promotion_boundary_missing_gate"
        ),
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "promotion_package_boundary_closed": boundary_closed,
        "promotion_package_independently_accepted": accepted,
        "row_column_unconditional_closed": False,
        "rankin_sample_exact_count": rankin_audit.get("core_count_exact"),
        "rankin_sample_allowed_budget": rankin_audit.get("allowed_budget"),
        "rankin_sample_pass": bool(
            rankin_audit.get("rankin_budget_pass") and rankin_audit.get("exact_budget_pass")
        ),
        "full_rankin_ledger_still_open_closed": (
            full_rankin.get("full_rankin_ledger_still_open_closed") is True
        ),
        "batch_rankin_pass_or_return_closed": (
            full_rankin.get("batch_rankin_pass_or_return_closed") is True
        ),
        "required_acceptance_items": [
            "D-structure / Structured-EHPD 入口与归约被独立接受",
            "Tail-log4 的 BG/RKS 定理号与适配审计被接受",
            "有限验证归档与脚本 hash 可复现",
            "Rankin pass-or-return 子账本及其失败回流被独立接受",
            "作者侧 BLOCK-REFEREE 只能由独立审稿接受后升级",
        ],
        "rows": rows,
        "promotion_law": (
            "第三包是最终晋级验收包，不是另一个隐藏的自足终端。它的边界已经闭合："
            "D-structure/Tail-log4/finite Rankin 接口已命名，Rankin 证书格式可检查，"
            "canonical-source 定理边界也明确把这个 referee gate 分离出去。但当前材料还没有"
            "独立接受该包，所以它不能把行/列命题升级为完整全局无条件定理。"
        ),
        "review_conclusion": (
            "第三包验收边界已闭合但未被当前材料独立接受：D-structure/Tail-log4/finite Rankin "
            "都是命名晋级门，Rankin pass-or-return 子账本已经内部闭合且格式可验收；"
            "但 D-structure 归约、Tail-log4 外部适配、有限验证 hash 和独立审稿仍未完成。"
            "因此完整行/列无条件定理仍不能声明。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix DStructure/Rankin 晋级验收边界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 晋级律",
        "",
        result["promotion_law"],
        "",
        "```text",
        f"promotion_package_boundary_closed={fmt_bool(result['promotion_package_boundary_closed'])}",
        (
            "promotion_package_independently_accepted="
            f"{fmt_bool(result['promotion_package_independently_accepted'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"rankin_sample_pass={fmt_bool(result['rankin_sample_pass'])}",
        f"full_rankin_ledger_still_open_closed={fmt_bool(result['full_rankin_ledger_still_open_closed'])}",
        f"batch_rankin_pass_or_return_closed={fmt_bool(result['batch_rankin_pass_or_return_closed'])}",
        "```",
        "",
        "## 2. 审查表",
        "",
        "| gate | boundary closed | accepted | evidence | meaning | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{boundary}` | `{accepted}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                boundary=fmt_bool(bool(item["boundary_closed"])),
                accepted=fmt_bool(bool(item["accepted"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(["", "## 3. 必须补齐的验收项", ""])
    for item in result["required_acceptance_items"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            "第三包已经从“模糊的最终障碍”变成可检查的验收清单。"
            "这一步不产生新的数学逃逸口，也不允许作者侧自审升级。"
            "只有当 D-structure/Tail-log4/finite Rankin/finite verification 全部被独立接受后，"
            "完整行/列无条件命题才可从当前边界晋级。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atlas-json", type=Path, default=DEFAULT_ATLAS)
    parser.add_argument("--terminal-promotion-json", type=Path, default=DEFAULT_TERMINAL_PROMOTION)
    parser.add_argument("--line-ref-md", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--rankin-acceptance-md", type=Path, default=DEFAULT_RANKIN_ACCEPTANCE)
    parser.add_argument("--rankin-audit-json", type=Path, default=DEFAULT_RANKIN_AUDIT)
    parser.add_argument("--full-rankin-json", type=Path, default=DEFAULT_FULL_RANKIN)
    parser.add_argument("--claim-status-md", type=Path, default=DEFAULT_CLAIM_STATUS)
    parser.add_argument("--main-tex", type=Path, default=DEFAULT_MAIN_TEX)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        atlas_path=args.atlas_json,
        terminal_promotion_path=args.terminal_promotion_json,
        line_ref_path=args.line_ref_md,
        rankin_acceptance_path=args.rankin_acceptance_md,
        rankin_audit_path=args.rankin_audit_json,
        full_rankin_path=args.full_rankin_json,
        claim_status_path=args.claim_status_md,
        main_tex_path=args.main_tex,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["required_acceptance_items"])


if __name__ == "__main__":
    main()
