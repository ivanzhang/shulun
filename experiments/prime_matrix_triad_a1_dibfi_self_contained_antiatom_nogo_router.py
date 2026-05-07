#!/usr/bin/env python3
"""核查自足版 full-S non-AP source anti-atom 输入是否可由当前假设推出。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_self_contained_antiatom_nogo_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_TERMINAL_SPLIT = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.json"
)
DEFAULT_SOURCE_ANTIATOM = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
)
DEFAULT_SOURCE_BLOCK_ENTROPY = (
    DOCS / "prime-matrix-triad-a1-source-block-entropy-router.json"
)
DEFAULT_EXACT_FACTOR_SUPPORT = (
    DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
)
DEFAULT_FACTOR_RESIDUE_INCIDENCE = (
    DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
)
DEFAULT_FULL_S_KLS_EXT = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.md"
)


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


def source_gate_open(source_block_entropy: dict[str, Any], gate: str) -> bool:
    """核查 source entropy 指定门控是否未闭合。"""
    return any(
        row["gate"] == gate and not row["closed"]
        for row in source_block_entropy["gate_rows"]
    )


def build_rows(
    terminal_split: dict[str, Any],
    source_antiatom: dict[str, Any],
    source_block_entropy: dict[str, Any],
    exact_factor_support: dict[str, Any],
    factor_residue_incidence: dict[str, Any],
    full_s_kls_ext: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造自足反原子 no-go 账本。"""
    prior_ready = (
        terminal_split["terminal_gap_after_router"]
        == "NewFullSNonAPSourceAntiAtomTheoremInput"
        and terminal_split["open_split_gates"]
        == ["NewFullSNonAPSourceAntiAtomTheoremInput"]
        and terminal_split["self_contained_version_closed"] is False
    )
    antiatom_contract_pinned = (
        "max_{u,v} M_{u,v}/sum_{u,v}M_{u,v} <= log^{-2A}"
        in source_antiatom["antiatom_contract"]
    )
    moving_delta_countermodel = (
        source_block_entropy["source_entropy_gap_exists"]
        and source_block_entropy["all_moving_delta_models_violate_source_entropy"]
        and source_gate_open(source_block_entropy, "WellFactorableConvolution")
        and source_gate_open(source_block_entropy, "TypeITypeIIDecomposition")
        and source_gate_open(source_block_entropy, "FourierSmoothing")
    )
    projection_repairs_blocked = (
        exact_factor_support["k4_k6_imply_exact_factor_support"] is False
        and factor_residue_incidence["naive_incidence_bridge_valid"] is False
    )
    external_contract_available = full_s_kls_ext["external_theorem_contract_closed"]
    self_contained_refuted = all(
        [
            prior_ready,
            antiatom_contract_pinned,
            moving_delta_countermodel,
            projection_repairs_blocked,
        ]
    )
    route_classification_closed = self_contained_refuted and external_contract_available
    return [
        {
            "gate": "PriorSelfContainedAntiAtomInputPinned",
            "closed": prior_ready,
            "evidence": (
                f"previous terminal={terminal_split['terminal_gap_after_router']}; "
                f"open={terminal_split['open_split_gates']}; "
                f"self_contained_closed={terminal_split['self_contained_version_closed']}."
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "AntiAtomTheoremValidityTest",
        },
        {
            "gate": "AntiAtomContractPinned",
            "closed": antiatom_contract_pinned,
            "evidence": source_antiatom["antiatom_contract"],
            "remaining": "none at statement level",
            "next_target": "MovingDeltaCountermodel",
        },
        {
            "gate": "MovingDeltaCountermodelAdmissible",
            "closed": moving_delta_countermodel,
            "evidence": (
                "SourceBlockEntropy records moving-delta models: formal well-factorable, "
                "Type-I/II, and Fourier-smoothing templates may all pass while one moving "
                "(u,v) block carries all capacity."
            ),
            "remaining": "anti-atom is false for the current generic template class",
            "next_target": "SelfContainedGenericAntiAtomRefuted",
        },
        {
            "gate": "ProjectionRepairRoutesBlocked",
            "closed": projection_repairs_blocked,
            "evidence": (
                "K4/K6 do not imply moving factor support, and naive factor-residue incidence "
                "is blocked by the internal atom fiber."
            ),
            "remaining": "no existing internal projection route repairs the countermodel",
            "next_target": "SelfContainedGenericAntiAtomRefuted",
        },
        {
            "gate": "ExternalFullSKLSExtStillAvailable",
            "closed": external_contract_available,
            "evidence": "FullS-KLS-ext external theorem contract is already closed.",
            "remaining": "this is an external-contract closure, not a self-contained proof",
            "next_target": "ExternalContractOnlyOrStrengthenedSource",
        },
        {
            "gate": "SelfContainedGenericAntiAtomRefuted",
            "closed": self_contained_refuted,
            "evidence": (
                "The demanded anti-atom inequality fails on the admissible moving-delta "
                "capacity model: max M_{u,v}/sum M_{u,v}=1, not log^{-2A}."
            ),
            "remaining": "current generic full-S self-contained branch cannot be closed as stated",
            "next_target": "StrengthenedSourceAxiomOrExternalContract",
        },
        {
            "gate": "RouteClassificationClosed",
            "closed": route_classification_closed,
            "evidence": (
                "The branch is classified completely: external-contract version is closed; "
                "current generic self-contained version is refuted unless the source contract is strengthened."
            ),
            "remaining": "none at route-classification level",
            "next_target": "NoCurrentSelfContainedGenericClosureWithoutNewAxiom",
        },
    ]


def run(
    terminal_split_path: Path,
    source_antiatom_path: Path,
    source_block_entropy_path: Path,
    exact_factor_support_path: Path,
    factor_residue_incidence_path: Path,
    full_s_kls_ext_path: Path,
) -> dict[str, Any]:
    """运行自足反原子 no-go 路由。"""
    terminal_split = load_json(terminal_split_path)
    source_antiatom = load_json(source_antiatom_path)
    source_block_entropy = load_json(source_block_entropy_path)
    exact_factor_support = load_json(exact_factor_support_path)
    factor_residue_incidence = load_json(factor_residue_incidence_path)
    full_s_kls_ext = load_json(full_s_kls_ext_path)
    rows = build_rows(
        terminal_split,
        source_antiatom,
        source_block_entropy,
        exact_factor_support,
        factor_residue_incidence,
        full_s_kls_ext,
    )
    closed_by_gate = {row["gate"]: bool(row["closed"]) for row in rows}
    external_contract_closed = closed_by_gate["ExternalFullSKLSExtStillAvailable"]
    self_contained_refuted = closed_by_gate["SelfContainedGenericAntiAtomRefuted"]
    route_classification_closed = closed_by_gate["RouteClassificationClosed"]
    terminal_gap = (
        "NoCurrentSelfContainedGenericFullSClosureWithoutNewSourceAxiom"
        if route_classification_closed
        else "SelfContainedGenericAntiAtomNoGoRouterIncomplete"
    )
    status = (
        "self_contained_generic_full_s_antiatom_refuted_external_contract_closed"
        if route_classification_closed
        else "self_contained_generic_full_s_antiatom_nogo_incomplete"
    )
    return {
        "certificate_type": "triad_a1_dibfi_self_contained_antiatom_nogo_router",
        "status": status,
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "terminal_split_json": file_sha256(terminal_split_path),
            "source_antiatom_json": file_sha256(source_antiatom_path),
            "source_block_entropy_json": file_sha256(source_block_entropy_path),
            "exact_factor_support_json": file_sha256(exact_factor_support_path),
            "factor_residue_incidence_json": file_sha256(
                factor_residue_incidence_path
            ),
            "full_s_kls_ext_json": file_sha256(full_s_kls_ext_path),
        },
        "previous_terminal_gap": terminal_split["terminal_gap_after_router"],
        "nogo_rows": rows,
        "closed_nogo_gates": [row["gate"] for row in rows if row["closed"]],
        "open_nogo_gates": [row["gate"] for row in rows if not row["closed"]],
        "external_contract_version_closed": external_contract_closed,
        "self_contained_generic_version_refuted": self_contained_refuted,
        "self_contained_generic_version_closed_as_proof": False,
        "terminal_gap_after_router": terminal_gap,
        "terminal_gap_expansion": [
            "AcceptExternalFullSKLSExt",
            "AddStrengthenedSourceAntiAtomAxiom",
            "RestrictToCanonicalSourceBranch",
        ],
        "moving_delta_counterexample": {
            "model": "one moving same-(u,v) block carries all final source capacity",
            "antiatom_left_side": "max M_{u,v}/sum M_{u,v}=1",
            "antiatom_required": "log^{-2A}",
            "verdict": "violates anti-atom for large P",
        },
        "structural_law": (
            "The current generic full-S non-AP self-contained branch is not merely unproved; "
            "its final anti-atom theorem is false under the recorded formal WFD/Type/Fourier "
            "hypotheses. A moving-delta capacity measure passes those formal templates while "
            "violating the required log-power anti-atom bound. Therefore no self-contained "
            "closure exists for the current generic statement without adding a strengthened "
            "source anti-atom axiom, restricting the source branch, or accepting FullS-KLS-ext externally."
        ),
        "review_conclusion": (
            "自足版 generic full-S 反原子输入被 moving-delta 模型反证；"
            "外部合同版已由 FullS-KLS-ext 闭合。当前 generic 自足版若不增强源头假设，"
            "不存在有效闭合证明。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI self-contained anti-atom no-go 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "## 2. moving-delta 反例",
        "",
    ]
    for key, value in result["moving_delta_counterexample"].items():
        lines.append(f"- `{key}={value}`。")
    lines.extend(
        [
            "",
            "```text",
            "previous terminal:",
            f"  {result['previous_terminal_gap']};",
            "",
            "new classification:",
            f"  {result['terminal_gap_after_router']};",
            "",
            "legal exits:",
            f"  {result['terminal_gap_expansion']}.",
            "```",
            "",
            "## 3. 汇总",
            "",
            f"- `external_contract_version_closed={fmt_bool(result['external_contract_version_closed'])}`。",
            f"- `self_contained_generic_version_refuted={fmt_bool(result['self_contained_generic_version_refuted'])}`。",
            f"- `self_contained_generic_version_closed_as_proof={fmt_bool(result['self_contained_generic_version_closed_as_proof'])}`。",
            f"- `closed_nogo_gates={result['closed_nogo_gates']}`。",
            f"- `open_nogo_gates={result['open_nogo_gates']}`。",
            "",
            "## 4. no-go 账本表",
            "",
            "| gate | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["nogo_rows"]:
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
            "当前 generic full-S 自足版不能在现有假设下闭合为证明。合法选择只剩：",
            "",
            "```text",
            "1. 接受外部 FullS-KLS-ext；",
            "2. 新增并证明 StrengthenedSourceAntiAtomAxiom；",
            "3. 限制到已分离的 canonical source branch。",
            "```",
            "",
            "这一步是负向闭合：它关闭的是“现有 generic 自足版可直接证明”的可能性，"
            "不把外部合同版伪装成自足证明。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--terminal-split-json", type=Path, default=DEFAULT_TERMINAL_SPLIT
    )
    parser.add_argument(
        "--source-antiatom-json", type=Path, default=DEFAULT_SOURCE_ANTIATOM
    )
    parser.add_argument(
        "--source-block-entropy-json",
        type=Path,
        default=DEFAULT_SOURCE_BLOCK_ENTROPY,
    )
    parser.add_argument(
        "--exact-factor-support-json", type=Path, default=DEFAULT_EXACT_FACTOR_SUPPORT
    )
    parser.add_argument(
        "--factor-residue-incidence-json",
        type=Path,
        default=DEFAULT_FACTOR_RESIDUE_INCIDENCE,
    )
    parser.add_argument(
        "--full-s-kls-ext-json", type=Path, default=DEFAULT_FULL_S_KLS_EXT
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        terminal_split_path=args.terminal_split_json,
        source_antiatom_path=args.source_antiatom_json,
        source_block_entropy_path=args.source_block_entropy_json,
        exact_factor_support_path=args.exact_factor_support_json,
        factor_residue_incidence_path=args.factor_residue_incidence_json,
        full_s_kls_ext_path=args.full_s_kls_ext_json,
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
                "self_contained_generic_version_refuted": result[
                    "self_contained_generic_version_refuted"
                ],
                "open_nogo_gates": result["open_nogo_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
