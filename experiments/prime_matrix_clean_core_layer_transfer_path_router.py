#!/usr/bin/env python3
"""Prime Matrix clean-core 层转移路径分割路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_layer_transfer_path_router.py

输出：
  docs/monograph/prime-matrix-clean-core-layer-transfer-path-router.json
  docs/monograph/prime-matrix-clean-core-layer-transfer-path-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SUPPORT_ATTACK = DOCS / "prime-matrix-clean-core-support-incidence-attack-router.json"
DEFAULT_LAYER_TRANSFER = DOCS / "prime-matrix-triad-a1-layer-transfer-router.json"
DEFAULT_SELECTOR = DOCS / "prime-matrix-triad-a1-selector-retention-router.json"
DEFAULT_DECISION_TREE = DOCS / "prime-matrix-triad-a1-decision-tree-formula-router.json"
DEFAULT_SOURCE_ID = DOCS / "prime-matrix-triad-a1-source-identification-router.json"
DEFAULT_PROVENANCE = DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
DEFAULT_GLOBAL_BRIDGE = DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
DEFAULT_COMPLETED_KLS = DOCS / "prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-layer-transfer-path-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-layer-transfer-path-router.md"


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


def retention_model() -> list[dict[str, Any]]:
    """给出有限路径签名保留率模型。"""
    rows: list[dict[str, Any]] = []
    for k in range(3, 10):
        log_y = 2.302585092994046 * k
        raw_support = log_y**5
        path_count = log_y**2
        retained = raw_support / path_count
        required = log_y**3
        rows.append(
            {
                "k": k,
                "log_y": log_y,
                "raw_support": raw_support,
                "path_count": path_count,
                "retained_support": retained,
                "required_support": required,
                "suffices": retained + 1e-9 >= required,
            }
        )
    return rows


def router_rows(
    support_attack: dict[str, Any],
    layer_transfer: dict[str, Any],
    selector: dict[str, Any],
    decision_tree: dict[str, Any],
    source_id: dict[str, Any],
    provenance: dict[str, Any],
    global_bridge: dict[str, Any],
    completed_kls: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 clean-core 层转移路径分割判定表。"""
    return [
        {
            "gate": "PriorLayerTransferInputPinned",
            "closed": support_attack.get("latest_internal_subinput")
            == "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn",
            "proved": False,
            "meaning": "上一层已把支撑关联压成 clean-core exact 层承认、非零转移与薄块回流。",
            "remaining": "继续拆解层承认到底需要哪类系数结构。",
        },
        {
            "gate": "LayerTransferReducesToSelectorRetention",
            "closed": layer_transfer.get("conditional_selector_retention_implies_layer_transfer")
            is True,
            "proved": False,
            "meaning": "层承认和非零转移可由 selector 保留率加 clean return 合同推出。",
            "remaining": "为 actual clean-core 系数给出 selector/path 账本。",
        },
        {
            "gate": "SelectorRetentionReducesToFinitePathSignatures",
            "closed": selector.get("conditional_finite_signature_implies_selector_retention")
            is True,
            "proved": False,
            "meaning": "若 raw support 被 polylog 多个 exact 路径签名分割，则最大签名保留 log-power 支撑。",
            "remaining": "证明 clean-core actual 路径分割、无抵消和失败回流。",
        },
        {
            "gate": "CanonicalDecisionTreeTemplateAvailable",
            "closed": decision_tree.get("recursive_formula_closed_algebraically") is True,
            "proved": False,
            "meaning": "canonical RIW/Buchstab 递归可展开为有限互斥决策树。",
            "remaining": "这只是模板，仍需 actual clean-core 系数来源或独立路径公式。",
        },
        {
            "gate": "FormalWFDSourceRejected",
            "closed": source_id.get("formal_wfd_source_rejected") is True,
            "proved": True,
            "meaning": "仅有 well-factorable 性质不能推出 source entropy 或路径支撑。",
            "remaining": "clean-core 不能用 generic WFD 形式假设冒充路径账本。",
        },
        {
            "gate": "CanonicalProvenanceClosedButScoped",
            "closed": provenance.get("actual_source_provenance_closed") is True
            and global_bridge.get("actual_source_bridge_closes_global_unrestricted") is False,
            "proved": True,
            "meaning": "canonical 来源账本已闭合，但只覆盖 canonical 分支，不覆盖 noncanonical clean-core。",
            "remaining": "clean-core 要么证明自己的实际系数路径分割，要么转外部/回流。",
        },
        {
            "gate": "CleanCorePathPartitionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有给出 actual clean-core 系数的有限路径分割、同路径非零和薄块回流合同。",
            "remaining": "证明 CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn。",
        },
        {
            "gate": "ExternalCompletedKLSStillOpen",
            "closed": completed_kls.get("terminal_gap_after_router")
            == "ModulusDependentCompletedFullSKLSInput",
            "proved": False,
            "meaning": "外部替代仍是 modulus-dependent completed Full-S KLS。",
            "remaining": "证明或独立接受该 completed KLS 输入。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧完成后仍需独立验收。",
        },
    ]


def run(
    support_attack_path: Path,
    layer_transfer_path: Path,
    selector_path: Path,
    decision_tree_path: Path,
    source_id_path: Path,
    provenance_path: Path,
    global_bridge_path: Path,
    completed_kls_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core 层转移路径分割路由。"""
    source_paths = [
        support_attack_path,
        layer_transfer_path,
        selector_path,
        decision_tree_path,
        source_id_path,
        provenance_path,
        global_bridge_path,
        completed_kls_path,
        dstructure_path,
    ]
    support_attack = load_json(support_attack_path)
    layer_transfer = load_json(layer_transfer_path)
    selector = load_json(selector_path)
    decision_tree = load_json(decision_tree_path)
    source_id = load_json(source_id_path)
    provenance = load_json(provenance_path)
    global_bridge = load_json(global_bridge_path)
    completed_kls = load_json(completed_kls_path)
    dstructure = load_json(dstructure_path)

    rows = router_rows(
        support_attack=support_attack,
        layer_transfer=layer_transfer,
        selector=selector,
        decision_tree=decision_tree,
        source_id=source_id,
        provenance=provenance,
        global_bridge=global_bridge,
        completed_kls=completed_kls,
        dstructure=dstructure,
    )
    boundary_closed = all(
        row["closed"] for row in rows if row["gate"] != "CleanCorePathPartitionCurrentCorpusProved"
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_layer_transfer_path_router",
        "status": "clean_core_layer_transfer_reduced_to_path_partition_open",
        "clean_core_layer_transfer_path_boundary_closed": boundary_closed,
        "selector_retention_template_available": layer_transfer.get(
            "conditional_selector_retention_implies_layer_transfer"
        )
        is True
        and selector.get("conditional_finite_signature_implies_selector_retention") is True,
        "canonical_provenance_closed_but_scoped": provenance.get("actual_source_provenance_closed")
        is True
        and global_bridge.get("actual_source_bridge_closes_global_unrestricted") is False,
        "clean_core_path_partition_proved": False,
        "clean_core_exact_layer_transfer_proved": False,
        "external_completed_kls_accepted": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_input": "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn",
        "latest_internal_subinput": "CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn",
        "latest_conditional_basis": (
            "(CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn OR "
            "ModulusDependentCompletedFullSKLSInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            "CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "path_partition_law": (
            "若 actual clean-core 系数能被分割为 polylog 多个互斥 exact 路径签名，且每条路径同号或非零，"
            "则 pigeonhole 给出 selector retention；再结合 raw Buchstab support 与 thin/rejected return，"
            "即可推出 clean-core exact layer transfer。"
        ),
        "scope_law": (
            "canonical RIW/Buchstab 决策树和来源账本已经闭合，但只在 canonical-source 分支内有效。"
            "clean-core noncanonical 残余不能导入该来源；它必须给出自己的 actual coefficient path "
            "partition，或走 completed KLS/命名回流。"
        ),
        "plain_conclusion": (
            "最新真正剩余继续缩小为 clean-core actual 系数的路径分割账本：证明其有 polylog "
            "多条互斥路径、同路径非零/无抵消，并把薄块或路径失败回流到命名出口。当前材料尚未证明该账本。"
        ),
        "rows": rows,
        "retention_model": retention_model(),
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
    """写出 Markdown 研究证书。"""
    lines: list[str] = [
        "# Prime Matrix clean-core 层转移路径分割路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"clean_core_layer_transfer_path_boundary_closed={fmt_bool(result['clean_core_layer_transfer_path_boundary_closed'])}",
        f"clean_core_path_partition_proved={fmt_bool(result['clean_core_path_partition_proved'])}",
        f"clean_core_exact_layer_transfer_proved={fmt_bool(result['clean_core_exact_layer_transfer_proved'])}",
        f"external_completed_kls_accepted={fmt_bool(result['external_completed_kls_accepted'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 路径分割律",
            "",
            result["path_partition_law"],
            "",
            "## 3. 作用域律",
            "",
            result["scope_law"],
            "",
            "## 4. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "`CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn` 要求：",
            "",
            "- actual clean-core `alpha/delta` 系数在同一 formal unit 中有 exact 路径签名分割；",
            "- 路径签名数量为 polylog，足以用 pigeonhole 保留 log-power 支撑；",
            "- 同路径贡献非零且无抵消，或进一步细分直到互斥；",
            "- thin、路径超预算、抵消或来源失败必须回流到 PDEC/SAE/ColumnCRT/CleanKLS 或外部 KLS。",
            "",
            "## 5. 保留率模型",
            "",
            "| k | log y | raw support | path count | retained support | required support | suffices |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["retention_model"]:
        lines.append(
            "| {k} | {log_y:.6g} | {raw_support:.6g} | {path_count:.6g} | "
            "{retained_support:.6g} | {required_support:.6g} | `{suffices}` |".format(**row)
        )
    lines.extend(
        [
            "",
            "## 6. 当前结论",
            "",
            "本步没有证明 clean-core 路径分割账本；它把层承认/非零转移硬点压成了一个可审稿的",
            "actual coefficient path-partition 合同，并明确 canonical 决策树不能跨分支偷渡。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(
        description="Route clean-core exact layer transfer to path partition ledger."
    )
    parser.add_argument("--support-attack", type=Path, default=DEFAULT_SUPPORT_ATTACK)
    parser.add_argument("--layer-transfer", type=Path, default=DEFAULT_LAYER_TRANSFER)
    parser.add_argument("--selector", type=Path, default=DEFAULT_SELECTOR)
    parser.add_argument("--decision-tree", type=Path, default=DEFAULT_DECISION_TREE)
    parser.add_argument("--source-id", type=Path, default=DEFAULT_SOURCE_ID)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--global-bridge", type=Path, default=DEFAULT_GLOBAL_BRIDGE)
    parser.add_argument("--completed-kls", type=Path, default=DEFAULT_COMPLETED_KLS)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        support_attack_path=args.support_attack,
        layer_transfer_path=args.layer_transfer,
        selector_path=args.selector,
        decision_tree_path=args.decision_tree,
        source_id_path=args.source_id,
        provenance_path=args.provenance,
        global_bridge_path=args.global_bridge,
        completed_kls_path=args.completed_kls,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_internal_subinput"])


if __name__ == "__main__":
    main()
