#!/usr/bin/env python3
"""逐项攻坚四类最终开放输入，并给出条件闭合定理。

用法示例：
  python3 experiments/prime_matrix_four_open_inputs_closure_attack_router.py

输出：
  docs/monograph/prime-matrix-four-open-inputs-closure-attack-router.json
  docs/monograph/prime-matrix-four-open-inputs-closure-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_FIREWALL = DOCS / "prime-matrix-final-input-firewall-boundary-router.json"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"
DEFAULT_NONCANONICAL = DOCS / "prime-matrix-noncanonical-complement-trilemma-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_ACTUAL_SOURCE = DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
DEFAULT_FULLS_NOGO = DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
DEFAULT_FULLS_INPUT = DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
DEFAULT_FULLS_EXT = DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-four-open-inputs-closure-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-four-open-inputs-closure-attack-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    input_name: str,
    current_boundary_closed: bool,
    current_obligation_exists: bool,
    closed_in_current_corpus: bool,
    evidence: str,
    attack_result: str,
    minimum_completion: str,
) -> dict[str, Any]:
    """构造四输入攻坚表格行。"""
    return {
        "input": input_name,
        "current_boundary_closed": current_boundary_closed,
        "current_obligation_exists": current_obligation_exists,
        "closed_in_current_corpus": closed_in_current_corpus,
        "evidence": evidence,
        "attack_result": attack_result,
        "minimum_completion": minimum_completion,
    }


def build_rows(
    pdec: dict[str, Any],
    sparse: dict[str, Any],
    noncanonical: dict[str, Any],
    dstructure: dict[str, Any],
    actual_source: dict[str, Any],
    fulls_nogo: dict[str, Any],
    fulls_input: dict[str, Any],
    fulls_ext: dict[str, Any],
) -> list[dict[str, Any]]:
    """逐项判定四类最终开放输入。"""
    pdec_frontier_zero = (
        pdec.get("pdec_family_explicit_input_boundary_closed") is True
        and pdec.get("current_materialized_pdec_frontier_closed") is True
    )
    sparse_frontier_zero = (
        sparse.get("future_sparse_packet_schema_boundary_closed") is True
        and sparse.get("current_materialized_sparse_frontier_closed") is True
    )
    noncanonical_boundary = noncanonical.get("trilemma_boundary_closed") is True
    canonical_only = (
        actual_source.get("actual_source_bridge_closed_for_canonical_branch") is True
        and actual_source.get("actual_source_bridge_closes_global_unrestricted") is False
    )
    fulls_primary_source_rejected = (
        fulls_nogo.get("primary_source_specialization_closed") is False
        and "NewFullSTheoremInput" in fulls_nogo.get("open_nogo_gates", [])
    )
    fulls_theorem_input_open = (
        fulls_input.get("new_full_s_theorem_input_closed") is False
        and "FullSNonAPWFDKLSTheoremInput" in fulls_input.get("open_input_gates", [])
    )
    fulls_external_contract_ready = (
        fulls_ext.get("external_theorem_contract_closed") is True
        and fulls_ext.get("self_contained_primary_source_proof_closed") is False
    )
    dstructure_boundary = dstructure.get("promotion_package_boundary_closed") is True
    dstructure_accepted = dstructure.get("promotion_package_independently_accepted") is True

    return [
        row(
            input_name="FutureExplicitPrimitivePDECSchema",
            current_boundary_closed=pdec_frontier_zero,
            current_obligation_exists=False,
            closed_in_current_corpus=pdec_frontier_zero,
            evidence="PDEC family explicit input boundary",
            attack_result="当前没有已物化合法非二点 primitive PDEC 候选；该输入只在未来新增 PDEC family 时触发。",
            minimum_completion="若未来新增，提交同 formal unit、三物理原子以上、二秩以上、cap-stable schema；否则当前无待证义务。",
        ),
        row(
            input_name="FutureExplicitSparsePacketExtractorSchema",
            current_boundary_closed=sparse_frontier_zero,
            current_obligation_exists=False,
            closed_in_current_corpus=sparse_frontier_zero,
            evidence="future sparse packet extractor schema boundary",
            attack_result="当前 sparse/LocalSurvivor 物化前沿清零；该输入只在未来新增 sparse route 时触发。",
            minimum_completion="若未来新增，提交有限窗口、候选集、blocker 投影、witness/deficit、签名持久性和可复现账本；否则当前无待证义务。",
        ),
        row(
            input_name="NoncanonicalFullSComplementTrilemma",
            current_boundary_closed=(
                noncanonical_boundary
                and canonical_only
                and fulls_primary_source_rejected
                and fulls_theorem_input_open
                and fulls_external_contract_ready
            ),
            current_obligation_exists=True,
            closed_in_current_corpus=False,
            evidence="noncanonical trilemma + actual-source reconciliation + FullS primary-source no-go",
            attack_result=(
                "canonical 实际源分支已闭合，但 unrestricted noncanonical 补集未闭合；"
                "现有 DI/BFI 主来源不能推出所需 full-S non-AP WFD KLS 估计。"
            ),
            minimum_completion=(
                "三选一：证明 actual noncanonical source 等于 canonical RIW/Buchstab；"
                "证明实际源强化反原子/APSourceLift；或接受/证明 FullSNonAPWFDKLSTheoremInput。"
            ),
        ),
        row(
            input_name="DStructureRankinPromotion",
            current_boundary_closed=dstructure_boundary,
            current_obligation_exists=True,
            closed_in_current_corpus=dstructure_accepted,
            evidence="DStructure/Rankin promotion acceptance router",
            attack_result="晋级包边界闭合、Rankin 样本通过，但正式全集和独立验收未完成；作者侧不能自我升级。",
            minimum_completion="独立接受 D-structure/Structured-EHPD、Tail-log4 BG/RKS 适配、有限验证 hash 和全部正式 Rankin 证书。",
        ),
    ]


def run(
    firewall_path: Path,
    pdec_path: Path,
    sparse_path: Path,
    noncanonical_path: Path,
    dstructure_path: Path,
    actual_source_path: Path,
    fulls_nogo_path: Path,
    fulls_input_path: Path,
    fulls_ext_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行四开放输入攻坚路由。"""
    firewall = load_json(firewall_path)
    pdec = load_json(pdec_path)
    sparse = load_json(sparse_path)
    noncanonical = load_json(noncanonical_path)
    dstructure = load_json(dstructure_path)
    actual_source = load_json(actual_source_path)
    fulls_nogo = load_json(fulls_nogo_path)
    fulls_input = load_json(fulls_input_path)
    fulls_ext = load_json(fulls_ext_path)

    rows = build_rows(
        pdec=pdec,
        sparse=sparse,
        noncanonical=noncanonical,
        dstructure=dstructure,
        actual_source=actual_source,
        fulls_nogo=fulls_nogo,
        fulls_input=fulls_input,
        fulls_ext=fulls_ext,
    )
    current_frontier_zero = (
        firewall.get("current_materialized_terminal_frontier_closed") is True
        and rows[0]["closed_in_current_corpus"]
        and rows[1]["closed_in_current_corpus"]
    )
    all_current_obligations_closed = all(
        item["closed_in_current_corpus"]
        for item in rows
        if item["current_obligation_exists"]
    )
    conditional_closure_ready = (
        firewall.get("no_hidden_terminal_remaining") is True
        and current_frontier_zero
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_four_open_inputs_closure_attack_router",
        "status": "four_open_inputs_attacked_conditional_chain_complete_unconditional_open",
        "attack_law": (
            "四类最终输入逐项硬攻后，前两类不是当前实际待证义务，而是未来新增路线的准入防火墙；"
            "后两类是真正阻断全局无条件闭合的输入。"
            "因此当前逻辑链已经形成条件闭合定理，但不能由现有材料升级为完整无条件定理。"
        ),
        "current_materialized_frontier_zero": current_frontier_zero,
        "no_hidden_terminal_remaining": firewall.get("no_hidden_terminal_remaining") is True,
        "all_current_obligations_closed": all_current_obligations_closed,
        "conditional_closure_chain_complete": conditional_closure_ready,
        "row_column_unconditional_closed": False,
        "unconditional_closure_possible_from_current_corpus": False,
        "conditional_closure_theorem": (
            "若未来 PDEC/sparse 新路线均按显式 schema 消解或没有新增，"
            "且 noncanonical full-S 补集三歧中至少一支被证明/接受，"
            "且 DStructureRankinPromotion 被独立接受，"
            "则当前无隐藏终端链可把行/列命题升级为完整闭合。"
        ),
        "current_corpus_no_go_theorem": (
            "在不新增 FullSNonAPWFDKLSTheoremInput/APSourceLift/强化实际源反原子且不取得 "
            "DStructureRankinPromotion 独立接受的情况下，当前材料不能诚实推出完整行/列无条件定理。"
        ),
        "rows": rows,
        "next_single_best_attack": (
            "NoncanonicalFullSComplementTrilemma：优先尝试 APSourceLift 或实际源强化反原子；"
            "若不能新增深解析定理，则只能走显式外部 FullSNonAPWFDKLSTheoremInput。"
        ),
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path)
            for path in [
                firewall_path,
                pdec_path,
                sparse_path,
                noncanonical_path,
                dstructure_path,
                actual_source_path,
                fulls_nogo_path,
                fulls_input_path,
                fulls_ext_path,
            ]
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 审查报告。"""
    lines: list[str] = [
        "# Prime Matrix 四开放输入攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["attack_law"],
        "",
        "```text",
        f"current_materialized_frontier_zero={fmt_bool(result['current_materialized_frontier_zero'])}",
        f"no_hidden_terminal_remaining={fmt_bool(result['no_hidden_terminal_remaining'])}",
        f"all_current_obligations_closed={fmt_bool(result['all_current_obligations_closed'])}",
        f"conditional_closure_chain_complete={fmt_bool(result['conditional_closure_chain_complete'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"unconditional_closure_possible_from_current_corpus={fmt_bool(result['unconditional_closure_possible_from_current_corpus'])}",
        "```",
        "",
        "## 1. 逐项攻坚表",
        "",
        "| input | boundary_closed | current_obligation | closed_in_current_corpus | evidence | attack_result | minimum_completion |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{input}` | `{boundary}` | `{obligation}` | `{closed}` | {evidence} | {attack} | {minimum} |".format(
                input=table_cell(item["input"]),
                boundary=fmt_bool(item["current_boundary_closed"]),
                obligation=fmt_bool(item["current_obligation_exists"]),
                closed=fmt_bool(item["closed_in_current_corpus"]),
                evidence=table_cell(item["evidence"]),
                attack=table_cell(item["attack_result"]),
                minimum=table_cell(item["minimum_completion"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 条件闭合定理",
            "",
            result["conditional_closure_theorem"],
            "",
            "## 3. 当前材料不可能性定理",
            "",
            result["current_corpus_no_go_theorem"],
            "",
            "## 4. 下一最优硬攻点",
            "",
            result["next_single_best_attack"],
            "",
            "## 5. 判定",
            "",
            (
                "四类输入已经被逐项攻到最窄形态：前两类当前无待证义务，后两类是真正开放输入。"
                "所以逻辑推理链条已经条件完整；完整无条件闭合仍需要新增证明或独立验收。"
            ),
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--firewall", type=Path, default=DEFAULT_FIREWALL)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--noncanonical", type=Path, default=DEFAULT_NONCANONICAL)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--actual-source", type=Path, default=DEFAULT_ACTUAL_SOURCE)
    parser.add_argument("--fulls-nogo", type=Path, default=DEFAULT_FULLS_NOGO)
    parser.add_argument("--fulls-input", type=Path, default=DEFAULT_FULLS_INPUT)
    parser.add_argument("--fulls-ext", type=Path, default=DEFAULT_FULLS_EXT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        firewall_path=args.firewall,
        pdec_path=args.pdec,
        sparse_path=args.sparse,
        noncanonical_path=args.noncanonical,
        dstructure_path=args.dstructure,
        actual_source_path=args.actual_source,
        fulls_nogo_path=args.fulls_nogo,
        fulls_input_path=args.fulls_input,
        fulls_ext_path=args.fulls_ext,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["next_single_best_attack"])


if __name__ == "__main__":
    main()
