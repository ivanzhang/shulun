#!/usr/bin/env python3
"""Prime Matrix clean-core 终局输入标准形路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_terminal_normal_form_router.py

输出：
  docs/monograph/prime-matrix-clean-core-terminal-normal-form-router.json
  docs/monograph/prime-matrix-clean-core-terminal-normal-form-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SHARP = DOCS / "prime-matrix-clean-core-moving-atom-sharp-input-router.json"
DEFAULT_SOURCE_ENTROPY = DOCS / "prime-matrix-triad-a1-source-block-entropy-router.json"
DEFAULT_EXACT_WFD = DOCS / "prime-matrix-triad-a1-exact-wfd-source-entropy-router.json"
DEFAULT_NCBLK_ALIGN = DOCS / "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json"
DEFAULT_KLS_COMPLETION = DOCS / "prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json"
DEFAULT_IRREDUCIBLE = DOCS / "prime-matrix-irreducible-math-input-refinement-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-terminal-normal-form-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-terminal-normal-form-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def normal_form_rows(
    sharp: dict[str, Any],
    source_entropy: dict[str, Any],
    exact_wfd: dict[str, Any],
    ncblk_align: dict[str, Any],
    kls_completion: dict[str, Any],
    irreducible: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成终局输入标准形判定表。"""
    return [
        {
            "gate": "SharpMovingAtomPinned",
            "closed": sharp.get("new_source_microinput")
            == "ActualNoncanonicalCleanCoreMovingAtomExclusion",
            "proved_or_accepted": False,
            "meaning": "上一层已把 self-contained sharp 输入固定为 clean-core moving atom 排斥。",
            "remaining": "判断它的最清晰标准形。",
        },
        {
            "gate": "MovingAtomEqualsSourceEntropy",
            "closed": True,
            "proved_or_accepted": False,
            "meaning": "无 moving 大原子就是 max_b M_b/M <= log^{-2A} 的 exact source entropy 表述。",
            "remaining": "证明 actual clean-core 系数满足该熵界。",
        },
        {
            "gate": "SourceEntropyImpliesNCBLK",
            "closed": source_entropy.get("conditional_source_entropy_implies_ncblk") is True,
            "proved_or_accepted": False,
            "meaning": "source entropy 一旦证明，立即给出 NC-BLK 块能量节省。",
            "remaining": "source entropy 本身仍未证明。",
        },
        {
            "gate": "ExactWFDSourceEntropyReduced",
            "closed": exact_wfd.get("conditional_factor_support_implies_exact_source_entropy") is True,
            "proved_or_accepted": False,
            "meaning": "exact source entropy 可由 exact factor support 与容量兼容推出。",
            "remaining": "exact factor support 不是当前 ledger 已证事实。",
        },
        {
            "gate": "NoCanonicalOrFormalShortcut",
            "closed": "FormalWFDInputsDoNotForceSourceEntropy"
            in ncblk_align.get("closed_alignment_gates", []),
            "proved_or_accepted": False,
            "meaning": "canonical 偷渡、APSourceLift 与 formal WFD 推出 source entropy 的路线已阻断。",
            "remaining": "必须证明 actual clean-core exact entropy，而非 generic 模板。",
        },
        {
            "gate": "ExternalKLSNormalFormPinned",
            "closed": kls_completion.get("terminal_gap_after_router")
            == "ModulusDependentCompletedFullSKLSInput",
            "proved_or_accepted": False,
            "meaning": "外部 FullS KLS 输入已被完成分解压成 c-dependent completed KLS。",
            "remaining": "证明或引用 ModulusDependentCompletedFullSKLSInput。",
        },
        {
            "gate": "InternalExternalNormalFormComplete",
            "closed": irreducible.get("refinement_boundary_closed") is True,
            "proved_or_accepted": False,
            "meaning": "内部 moving-block 与外部 FullS KLS 两线已归一化为 exact entropy 或 completed KLS。",
            "remaining": "二者至少一项仍需证明或独立接受。",
        },
        {
            "gate": "TerminalNormalFormCurrentCorpusProved",
            "closed": False,
            "proved_or_accepted": False,
            "meaning": "当前材料没有证明 exact clean-core source entropy，也没有接受 completed KLS 外部输入。",
            "remaining": "证明 ExactCleanCoreFullSNonAPWFDSourceEntropy，或接受 ModulusDependentCompletedFullSKLSInput。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved_or_accepted": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "数学输入完成后仍需独立验收。",
        },
    ]


def run(
    sharp_path: Path,
    source_entropy_path: Path,
    exact_wfd_path: Path,
    ncblk_align_path: Path,
    kls_completion_path: Path,
    irreducible_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core 终局输入标准形路由。"""
    source_paths = [
        sharp_path,
        source_entropy_path,
        exact_wfd_path,
        ncblk_align_path,
        kls_completion_path,
        irreducible_path,
        dstructure_path,
    ]
    sharp = load_json(sharp_path)
    source_entropy = load_json(source_entropy_path)
    exact_wfd = load_json(exact_wfd_path)
    ncblk_align = load_json(ncblk_align_path)
    kls_completion = load_json(kls_completion_path)
    irreducible = load_json(irreducible_path)
    dstructure = load_json(dstructure_path)
    rows = normal_form_rows(
        sharp=sharp,
        source_entropy=source_entropy,
        exact_wfd=exact_wfd,
        ncblk_align=ncblk_align,
        kls_completion=kls_completion,
        irreducible=irreducible,
        dstructure=dstructure,
    )
    normal_form_closed = all(
        row["closed"] for row in rows if row["gate"] != "TerminalNormalFormCurrentCorpusProved"
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_terminal_normal_form_router",
        "status": "clean_core_terminal_normal_form_closed_inputs_open",
        "clean_core_terminal_normal_form_closed": normal_form_closed,
        "internal_exact_entropy_proved": False,
        "external_completed_kls_accepted": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_source_microinput": sharp.get("new_source_microinput"),
        "internal_normal_form": "ExactCleanCoreFullSNonAPWFDSourceEntropy",
        "external_normal_form": "ModulusDependentCompletedFullSKLSInput",
        "latest_conditional_basis": (
            "(ExactCleanCoreFullSNonAPWFDSourceEntropy OR "
            "ModulusDependentCompletedFullSKLSInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "self_contained_basis": (
            "ExactCleanCoreFullSNonAPWFDSourceEntropy AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "normal_form_law": (
            "ActualNoncanonicalCleanCoreMovingAtomExclusion 的内部标准形就是 exact clean-core "
            "source entropy：max_b M_b/M <= log^{-2A}。外部替代标准形不是泛称 DI/BFI，"
            "而是 full-S 完成后带 c-dependent residue weights 的 ModulusDependentCompletedFullSKLSInput。"
        ),
        "plain_conclusion": (
            "最新终局输入已归一化：完全自足路线必须证明 exact clean-core full-S non-AP WFD "
            "source entropy；外部路线必须证明或接受 completed、modulus-dependent 的 full-S KLS 输入。"
            "当前材料只关闭命名和等价边界，没有证明任一输入。"
        ),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix clean-core 终局输入标准形路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"clean_core_terminal_normal_form_closed={fmt_bool(result['clean_core_terminal_normal_form_closed'])}",
        f"internal_exact_entropy_proved={fmt_bool(result['internal_exact_entropy_proved'])}",
        f"external_completed_kls_accepted={fmt_bool(result['external_completed_kls_accepted'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved/accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved_or_accepted}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved_or_accepted=fmt_bool(row["proved_or_accepted"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 标准形律",
            "",
            result["normal_form_law"],
            "",
            "## 3. 输入基",
            "",
            "上一层源侧微输入：",
            "",
            "```text",
            result["previous_source_microinput"],
            "```",
            "",
            "内部标准形：",
            "",
            "```text",
            result["internal_normal_form"],
            "```",
            "",
            "外部标准形：",
            "",
            "```text",
            result["external_normal_form"],
            "```",
            "",
            "条件终局输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["self_contained_basis"],
            "```",
            "",
            "## 4. 当前结论",
            "",
            "本步没有证明 exact source entropy，也没有接受 completed KLS；它关闭的是终局输入标准形。",
            "下一步若坚持完全自足，应直接证明 `ExactCleanCoreFullSNonAPWFDSourceEntropy`。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sharp", type=Path, default=DEFAULT_SHARP)
    parser.add_argument("--source-entropy", type=Path, default=DEFAULT_SOURCE_ENTROPY)
    parser.add_argument("--exact-wfd", type=Path, default=DEFAULT_EXACT_WFD)
    parser.add_argument("--ncblk-align", type=Path, default=DEFAULT_NCBLK_ALIGN)
    parser.add_argument("--kls-completion", type=Path, default=DEFAULT_KLS_COMPLETION)
    parser.add_argument("--irreducible", type=Path, default=DEFAULT_IRREDUCIBLE)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        sharp_path=args.sharp,
        source_entropy_path=args.source_entropy,
        exact_wfd_path=args.exact_wfd,
        ncblk_align_path=args.ncblk_align,
        kls_completion_path=args.kls_completion,
        irreducible_path=args.irreducible,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_conditional_basis"])


if __name__ == "__main__":
    main()
