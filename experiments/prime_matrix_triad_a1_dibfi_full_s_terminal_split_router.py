#!/usr/bin/env python3
"""拆分 full-S 终端：外部合同版闭合，自足版剩新反原子定理输入。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_full_s_terminal_split_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_SOURCE_ANTIATOM = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
)
DEFAULT_FULL_S_KLS_EXT = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
)
DEFAULT_PRIMARY_SOURCE_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
)
DEFAULT_AP_SOURCE_LIFT_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    source_antiatom: dict[str, Any],
    full_s_kls_ext: dict[str, Any],
    primary_source_nogo: dict[str, Any],
    ap_source_lift_nogo: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造 full-S terminal split 账本。"""
    prior_ready = (
        source_antiatom["terminal_gap_after_router"]
        == "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"
        and source_antiatom["open_antiatom_gates"]
        == ["FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"]
    )
    external_contract_closed = (
        full_s_kls_ext["external_theorem_contract_closed"]
        and "ExternalContractVersionClosed" in full_s_kls_ext["closed_specialization_gates"]
    )
    primary_source_rejected = (
        primary_source_nogo["terminal_gap_after_router"]
        == "NewFullSTheoremInputOrAPSourceLift"
        and "NewFullSTheoremInput" in primary_source_nogo["open_nogo_gates"]
    )
    ap_lift_rejected = (
        ap_source_lift_nogo["ap_source_lift_rejected"]
        and ap_source_lift_nogo["terminal_gap_after_router"] == "NewFullSTheoremInput"
    )
    antiatom_is_new_input = prior_ready and primary_source_rejected and ap_lift_rejected
    terminal_split_closed = all(
        [
            prior_ready,
            external_contract_closed,
            primary_source_rejected,
            ap_lift_rejected,
            antiatom_is_new_input,
        ]
    )
    return [
        {
            "gate": "PriorSourceAntiAtomTerminalPinned",
            "closed": prior_ready,
            "evidence": (
                f"previous terminal={source_antiatom['terminal_gap_after_router']}; "
                f"open={source_antiatom['open_antiatom_gates']}."
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "ExternalContractOrSelfContainedInputSplit",
        },
        {
            "gate": "ExternalFullSKLSExtContractAvailable",
            "closed": external_contract_closed,
            "evidence": (
                "FullS-KLS-ext is already materialized as an external theorem contract "
                "for the current uncentered no-projection full-S non-AP WFD object."
            ),
            "remaining": "closed only for the external-theorem version",
            "next_target": "ExternalContractVersionClosed",
        },
        {
            "gate": "PrimarySourceSpecializationRejected",
            "closed": primary_source_rejected,
            "evidence": (
                "Existing DI/BFI primary sources do not imply the custom full-S KLS-ext theorem."
            ),
            "remaining": "no primary-source self-contained derivation is available",
            "next_target": "NewFullSSourceAntiAtomTheoremInput",
        },
        {
            "gate": "APSourceLiftRejected",
            "closed": ap_lift_rejected,
            "evidence": "APSourceLift was rejected; non-AP full-S WFD cannot return to the AP-source BFI branch.",
            "remaining": "no AP lift shortcut remains",
            "next_target": "NewFullSSourceAntiAtomTheoremInput",
        },
        {
            "gate": "SourceAntiAtomIsNewTheoremInput",
            "closed": antiatom_is_new_input,
            "evidence": (
                "Since formal WFD/K4/K6/incidence/canonical shortcuts are blocked and AP lift is rejected, "
                "the strengthened anti-atom contract is a genuinely new source theorem input."
            ),
            "remaining": "prove or assume this new source theorem for the self-contained route",
            "next_target": "NewFullSNonAPSourceAntiAtomTheoremInput",
        },
        {
            "gate": "TerminalSplitClosedAtRoutingLevel",
            "closed": terminal_split_closed,
            "evidence": (
                "The full-S branch is now separated into external-contract closure and self-contained new-input obligation."
            ),
            "remaining": "none at split-definition level",
            "next_target": "NewFullSNonAPSourceAntiAtomTheoremInput",
        },
        {
            "gate": "NewFullSNonAPSourceAntiAtomTheoremInput",
            "closed": False,
            "evidence": (
                "The repository still lacks a proof of the source anti-atom theorem for the final "
                "full-S non-AP WFD capacity measure."
            ),
            "remaining": "prove this new anti-atom theorem, or explicitly accept FullS-KLS-ext as external input",
            "next_target": "NewFullSNonAPSourceAntiAtomTheoremInput",
        },
    ]


def run(
    source_antiatom_path: Path,
    full_s_kls_ext_path: Path,
    primary_source_nogo_path: Path,
    ap_source_lift_nogo_path: Path,
) -> dict[str, Any]:
    """运行 full-S terminal split 路由。"""
    source_antiatom = load_json(source_antiatom_path)
    full_s_kls_ext = load_json(full_s_kls_ext_path)
    primary_source_nogo = load_json(primary_source_nogo_path)
    ap_source_lift_nogo = load_json(ap_source_lift_nogo_path)
    rows = build_rows(
        source_antiatom,
        full_s_kls_ext,
        primary_source_nogo,
        ap_source_lift_nogo,
    )
    return {
        "certificate_type": "triad_a1_dibfi_full_s_terminal_split_router",
        "status": "full_s_external_contract_closed_self_contained_antiatom_input_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "source_antiatom_json": file_sha256(source_antiatom_path),
            "full_s_kls_ext_json": file_sha256(full_s_kls_ext_path),
            "primary_source_nogo_json": file_sha256(primary_source_nogo_path),
            "ap_source_lift_nogo_json": file_sha256(ap_source_lift_nogo_path),
        },
        "previous_terminal_gap": source_antiatom["terminal_gap_after_router"],
        "split_rows": rows,
        "closed_split_gates": [row["gate"] for row in rows if row["closed"]],
        "open_split_gates": [row["gate"] for row in rows if not row["closed"]],
        "external_contract_version_closed": True,
        "self_contained_version_closed": False,
        "terminal_gap_after_router": "NewFullSNonAPSourceAntiAtomTheoremInput",
        "terminal_gap_expansion": [
            "NewFullSNonAPSourceAntiAtomTheoremInput",
        ],
        "external_contract": "FullS-KLS-ext",
        "self_contained_boundary": (
            "External-contract version may accept FullS-KLS-ext. Fully self-contained or "
            "primary-source-specialized version still needs a new source anti-atom theorem."
        ),
        "structural_law": (
            "The current full-S terminal is no longer a hidden structural ambiguity. "
            "If FullS-KLS-ext is accepted as an external theorem, the external branch is closed. "
            "If the proof must be self-contained or derived from existing DI/BFI primary sources, "
            "the only remaining input is a new anti-atom theorem for the final full-S non-AP source measure."
        ),
        "review_conclusion": (
            "full-S 终端已拆分：外部合同版由 `FullS-KLS-ext` 闭合；"
            "完全自足/主来源逐项版只剩 `NewFullSNonAPSourceAntiAtomTheoremInput`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI full-S terminal split 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 版本边界",
        "",
        f"- `external_contract_version_closed={fmt_bool(result['external_contract_version_closed'])}`。",
        f"- `self_contained_version_closed={fmt_bool(result['self_contained_version_closed'])}`。",
        f"- `external_contract={result['external_contract']}`。",
        f"- `self_contained_boundary={result['self_contained_boundary']}`。",
        "",
        "## 2. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "previous terminal:",
        f"  {result['previous_terminal_gap']};",
        "",
        "new self-contained terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "expansion:",
        f"  {result['terminal_gap_expansion']}.",
        "```",
        "",
        "## 3. 汇总",
        "",
        f"- `closed_split_gates={result['closed_split_gates']}`。",
        f"- `open_split_gates={result['open_split_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 4. 路由账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["split_rows"]:
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
            "## 5. 当前结论",
            "",
            "若接受外部深定理合同，full-S non-AP 分支由 `FullS-KLS-ext` 关闭。",
            "若要求完全自足或现有 DI/BFI 主来源逐项推出，唯一剩余为：",
            "",
            "```text",
            "NewFullSNonAPSourceAntiAtomTheoremInput",
            "```",
            "",
            "这一步不宣称自足闭合；它把外部合同版与自足版边界固定下来。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-antiatom-json", type=Path, default=DEFAULT_SOURCE_ANTIATOM
    )
    parser.add_argument(
        "--full-s-kls-ext-json", type=Path, default=DEFAULT_FULL_S_KLS_EXT
    )
    parser.add_argument(
        "--primary-source-nogo-json", type=Path, default=DEFAULT_PRIMARY_SOURCE_NOGO
    )
    parser.add_argument(
        "--ap-source-lift-nogo-json", type=Path, default=DEFAULT_AP_SOURCE_LIFT_NOGO
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        source_antiatom_path=args.source_antiatom_json,
        full_s_kls_ext_path=args.full_s_kls_ext_json,
        primary_source_nogo_path=args.primary_source_nogo_json,
        ap_source_lift_nogo_path=args.ap_source_lift_nogo_json,
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
                "terminal_gap_after_router": result["terminal_gap_after_router"],
                "external_contract_version_closed": result[
                    "external_contract_version_closed"
                ],
                "open_split_gates": result["open_split_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
