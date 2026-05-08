#!/usr/bin/env python3
"""内外两线共同核心调和路由器。

用法示例：
  python3 experiments/prime_matrix_dual_lane_common_core_reconciliation_router.py

输出：
  docs/monograph/prime-matrix-dual-lane-common-core-reconciliation-router.json
  docs/monograph/prime-matrix-dual-lane-common-core-reconciliation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_DUAL = DOCS / "prime-matrix-dual-lane-terminal-reduction-router.json"
DEFAULT_CDEP = DOCS / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json"
DEFAULT_NCBLK = DOCS / "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json"
DEFAULT_SPLIT = DOCS / "prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.json"
DEFAULT_TAXONOMY = DOCS / "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-dual-lane-common-core-reconciliation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-dual-lane-common-core-reconciliation-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写字符串。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    dual: dict[str, Any],
    cdep: dict[str, Any],
    ncblk: dict[str, Any],
    split: dict[str, Any],
    taxonomy: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成共同核心调和判定行。"""
    return [
        {
            "gate": "DualLaneTerminalPinned",
            "closed": dual.get("terminal_reduction_boundary_closed") is True
            and dual.get("external_terminal_input")
            == "CDependentResidueWeightSpectralCancellationInput",
            "meaning": "上一层已把外部线压成 c-dependent residue 谱抵消，内部线压成强化源反原子。",
            "consequence": "可以检查这两个终端是否独立。",
        },
        {
            "gate": "CDependentResidueReturnsToNCBLK",
            "closed": cdep.get("terminal_gap_after_router")
            == "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
            "meaning": "c-dependent residue 谱输入经有限 Fourier 接入 BWFD/BSC/KFLS 链。",
            "consequence": "自足证明时它不是新普通大筛原子，而是回到 actual same-(u,v) 非集中或外部定理。",
        },
        {
            "gate": "NCBLKAlignsToExactSourceEntropy",
            "closed": ncblk.get("terminal_gap_after_router")
            == "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov",
            "meaning": "NC-BLK 自足路线必须证明 exact full-S non-AP source entropy，不能偷用 canonical 分支。",
            "consequence": "该目标与内部强化源反原子是同一 moving-block 核心的两种表述。",
        },
        {
            "gate": "ExternalContractSeparatedFromSelfContainedCore",
            "closed": split.get("terminal_gap_after_router")
            == "NewFullSNonAPSourceAntiAtomTheoremInput"
            and split.get("external_contract_version_closed") is True,
            "meaning": "接受 FullS-KLS-ext 外部合同时外部版闭合；自足/主来源逐项版仍剩新源反原子输入。",
            "consequence": "外部定理可作为黑箱输入，但不能冒充自足证明。",
        },
        {
            "gate": "SelfContainedTaxonomyCommonCorePinned",
            "closed": taxonomy.get("actual_source_bridge_pinned") is True
            and taxonomy.get("actual_source_bridge_theorem_closed") is False,
            "meaning": "完全自足路线只剩实际源恒等或实际源强化反原子。",
            "consequence": "unrestricted generic WFD 自足版已被 moving-delta 反证。",
        },
        {
            "gate": "DStructurePromotionStillSeparate",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级门。",
            "consequence": "数学输入闭合后仍需独立验收才能升级为完整行/列无条件定理。",
        },
    ]


def run(
    dual_path: Path,
    cdep_path: Path,
    ncblk_path: Path,
    split_path: Path,
    taxonomy_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行共同核心调和。"""
    source_paths = [
        dual_path,
        cdep_path,
        ncblk_path,
        split_path,
        taxonomy_path,
        dstructure_path,
    ]
    dual = load_json(dual_path)
    cdep = load_json(cdep_path)
    ncblk = load_json(ncblk_path)
    split = load_json(split_path)
    taxonomy = load_json(taxonomy_path)
    dstructure = load_json(dstructure_path)

    rows = build_rows(
        dual=dual,
        cdep=cdep,
        ncblk=ncblk,
        split=split,
        taxonomy=taxonomy,
        dstructure=dstructure,
    )
    common_core_reconciliation_closed = all(row["closed"] for row in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_dual_lane_common_core_reconciliation_router",
        "status": "dual_lane_common_core_reconciled_external_or_new_source_antiatom_open",
        "common_core_reconciliation_closed": common_core_reconciliation_closed,
        "self_contained_common_core_proved": False,
        "external_contract_accepted_as_final_input": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_basis": dual.get("refined_final_basis"),
        "self_contained_common_core": (
            "ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput"
        ),
        "external_contract_input": (
            "AcceptedFullSKLSExtOrCDependentResidueWeightSpectralCancellationInput"
        ),
        "reconciled_final_basis": (
            "((ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput) OR "
            "AcceptedFullSKLSExtOrCDependentResidueWeightSpectralCancellationInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "self_contained_basis_without_external_black_box": (
            "ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "core_law": (
            "CDependentResidueWeightSpectralCancellationInput 若被接受，就是外部定理输入。"
            "若试图从当前材料内部证明它，有限 Fourier completion 会把它降回 BWFD/BSC/KFLS，"
            "再降回 actual same-(u,v) block non-concentration。"
            "这与内部线的 source-antiatom / moving-block 共同核心是同一个数学义务。"
        ),
        "plain_conclusion": (
            "两条线在自足版本中已经汇合：外部 c-dependent 谱抵消若不作为外部定理接受，"
            "会通过 BWFD/BSC/KFLS 回到 actual same-(u,v) 非集中，也就是内部强化源反原子核心。"
            "因此当前没有两个独立自足硬点；真正二选一是接受外部 FullS-KLS/c-dependent 谱定理，"
            "或证明实际源恒等/新 full-S 源反原子。DStructure/Rankin 晋级仍独立开放。"
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
        "# Prime Matrix 内外两线共同核心调和路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"common_core_reconciliation_closed={fmt_bool(result['common_core_reconciliation_closed'])}",
        f"self_contained_common_core_proved={fmt_bool(result['self_contained_common_core_proved'])}",
        f"external_contract_accepted_as_final_input={fmt_bool(result['external_contract_accepted_as_final_input'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 调和判定表",
        "",
        "| gate | closed | meaning | consequence |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {meaning} | {consequence} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                meaning=table_cell(row["meaning"]),
                consequence=table_cell(row["consequence"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 上一层输入基",
            "",
            "```text",
            str(result["previous_basis"]),
            "```",
            "",
            "## 3. 调和后输入基",
            "",
            "```text",
            result["reconciled_final_basis"],
            "```",
            "",
            "## 4. 完全自足版输入基",
            "",
            "```text",
            result["self_contained_basis_without_external_black_box"],
            "```",
            "",
            "## 5. 核心律",
            "",
            result["core_law"],
            "",
            "## 6. 当前结论",
            "",
            "若不接受外部 FullS-KLS/c-dependent 谱定理，当前最窄自足目标就是证明实际源恒等或新 full-S 源反原子。",
            "这一步没有证明该新源定理，也没有完成 DStructure/Rankin 独立验收。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dual", type=Path, default=DEFAULT_DUAL)
    parser.add_argument("--cdep", type=Path, default=DEFAULT_CDEP)
    parser.add_argument("--ncblk", type=Path, default=DEFAULT_NCBLK)
    parser.add_argument("--split", type=Path, default=DEFAULT_SPLIT)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        dual_path=args.dual,
        cdep_path=args.cdep,
        ncblk_path=args.ncblk,
        split_path=args.split,
        taxonomy_path=args.taxonomy,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["reconciled_final_basis"])


if __name__ == "__main__":
    main()
