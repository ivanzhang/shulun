#!/usr/bin/env python3
"""收束 NoncanonicalFullSComplementPackage 的三歧闭合边界。

用法示例：
  python3 experiments/prime_matrix_noncanonical_complement_trilemma_router.py

输出：
  docs/monograph/prime-matrix-noncanonical-complement-trilemma-router.json
  docs/monograph/prime-matrix-noncanonical-complement-trilemma-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_CONTRACT = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.json"
DEFAULT_SOURCE_ANTIATOM = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
)
DEFAULT_ANTIATOM_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
)
DEFAULT_FULL_S_INPUT = (
    DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
)
DEFAULT_EXTERNAL_FULL_S = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
)
DEFAULT_ACTUAL_SOURCE = (
    DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
)
DEFAULT_FINAL_THEOREM = (
    DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-noncanonical-complement-trilemma-router.json"
DEFAULT_MD = DOCS / "prime-matrix-noncanonical-complement-trilemma-router.md"


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
    gate: str,
    closed: bool,
    verdict: str,
    evidence: str,
    consequence: str,
    remaining: str,
) -> dict[str, Any]:
    """构造第二包三歧审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "verdict": verdict,
        "evidence": evidence,
        "consequence": consequence,
        "remaining": remaining,
    }


def build_rows(
    contract: dict[str, Any],
    source_antiatom: dict[str, Any],
    antiatom_nogo: dict[str, Any],
    full_s_input: dict[str, Any],
    external_full_s: dict[str, Any],
    actual_source: dict[str, Any],
    final_theorem: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 noncanonical 补集三歧审查表。"""
    canonical_subtracted = (
        contract.get("canonical_branch_removed_from_remainder") is True
        and actual_source.get("actual_source_bridge_closed_for_canonical_branch") is True
        and final_theorem.get("canonical_source_self_contained_theorem_closed") is True
    )
    contract_pinned = (
        contract.get("contract_boundary_closed") is True
        and contract.get("generic_wfd_template_available") is False
    )
    antiatom_reduced = (
        source_antiatom.get("terminal_gap_after_router")
        == "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"
        and "FullSNonAPStrengthenedSourceAntiAtomContract"
        in source_antiatom.get("terminal_gap_expansion", [])
    )
    generic_refuted = (
        antiatom_nogo.get("self_contained_generic_version_refuted") is True
        and antiatom_nogo.get("self_contained_generic_version_closed_as_proof") is False
        and antiatom_nogo.get("open_nogo_gates") == []
    )
    theorem_input_pinned = (
        full_s_input.get("terminal_gap_after_router") == "FullSNonAPWFDKLSTheoremInput"
        and full_s_input.get("open_input_gates") == ["FullSNonAPWFDKLSTheoremInput"]
    )
    external_contract_closed = (
        external_full_s.get("external_theorem_contract_closed") is True
        and external_full_s.get("self_contained_primary_source_proof_closed") is False
        and external_full_s.get("open_specialization_gates")
        == ["DIBFIPrimarySourceSpecializationProof"]
    )

    return [
        row(
            gate="CanonicalBranchSubtracted",
            closed=canonical_subtracted,
            verdict="closed_for_canonical_branch",
            evidence="actual-source bridge + canonical-source final theorem",
            consequence="canonical RIW/Buchstab 分支已移出 noncanonical 补集。",
            remaining="none inside canonical branch",
        ),
        row(
            gate="NoncanonicalContractPinned",
            closed=contract_pinned,
            verdict="contract_closed",
            evidence="noncanonical complement input contract",
            consequence="第二包不是 generic WFD 自足引理，而是实际源/强化反原子/外部定理三歧。",
            remaining="choose one legal closure mode",
        ),
        row(
            gate="SourceAntiAtomReduction",
            closed=antiatom_reduced,
            verdict="reduced_not_proved",
            evidence="full-S source anti-atom router",
            consequence="支撑与容量兼容已等价压成最终 source capacity measure 的强化反原子。",
            remaining="prove strengthened source anti-atom or take external route",
        ),
        row(
            gate="GenericSelfContainedAntiAtomNoGo",
            closed=generic_refuted,
            verdict="refuted",
            evidence="self-contained anti-atom no-go router",
            consequence="当前 generic full-S 自足反原子在 moving-delta 模型下为假。",
            remaining="must strengthen source, restrict to canonical, or accept external FullS-KLS-ext",
        ),
        row(
            gate="FullSNonAPWFDKLSInputPinned",
            closed=theorem_input_pinned,
            verdict="single_external_atom",
            evidence="new full-S theorem input router",
            consequence="外部/新深定理路线已压成一个 full-S non-AP WFD KLS 定理输入。",
            remaining="prove or cite exact FullS-KLS-ext",
        ),
        row(
            gate="ExternalContractClosedIfAccepted",
            closed=external_contract_closed,
            verdict="conditional_external_closed",
            evidence="FullS-KLS-ext specialization router",
            consequence="接受 FullS-KLS-ext 时，scale/object/no-projection 合同已经闭合。",
            remaining="primary-source derivation or explicit external acceptance",
        ),
    ]


def run(
    contract_path: Path,
    source_antiatom_path: Path,
    antiatom_nogo_path: Path,
    full_s_input_path: Path,
    external_full_s_path: Path,
    actual_source_path: Path,
    final_theorem_path: Path,
) -> dict[str, Any]:
    """运行第二包三歧边界路由。"""
    contract = load_json(contract_path)
    source_antiatom = load_json(source_antiatom_path)
    antiatom_nogo = load_json(antiatom_nogo_path)
    full_s_input = load_json(full_s_input_path)
    external_full_s = load_json(external_full_s_path)
    actual_source = load_json(actual_source_path)
    final_theorem = load_json(final_theorem_path)
    rows = build_rows(
        contract=contract,
        source_antiatom=source_antiatom,
        antiatom_nogo=antiatom_nogo,
        full_s_input=full_s_input,
        external_full_s=external_full_s,
        actual_source=actual_source,
        final_theorem=final_theorem,
    )
    boundary_closed = all(item["closed"] for item in rows)
    evidence_paths = [
        contract_path,
        source_antiatom_path,
        antiatom_nogo_path,
        full_s_input_path,
        external_full_s_path,
        actual_source_path,
        final_theorem_path,
    ]
    return {
        "certificate_type": "prime_matrix_noncanonical_complement_trilemma_router",
        "status": (
            "noncanonical_complement_trilemma_boundary_closed_inputs_still_conditional"
            if boundary_closed
            else "noncanonical_complement_trilemma_boundary_missing_gate"
        ),
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "trilemma_boundary_closed": boundary_closed,
        "self_contained_noncanonical_package_closed": False,
        "external_contract_package_closed_if_fulls_kls_ext_accepted": boundary_closed,
        "row_column_unconditional_closed": False,
        "legal_closure_modes": [
            "实际源恒等：证明 actual full-S non-AP source 等于 canonical RIW/Buchstab",
            "强化实际源反原子：证明最终 source capacity measure 没有 moving same-(u,v) atom",
            "外部/新深定理：接受或证明 FullS-KLS-ext / FullSNonAPWFDKLSTheoremInput",
        ],
        "open_inputs_after_trilemma": [
            "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource",
            "DIBFIPrimarySourceSpecializationProof OR explicit acceptance of FullS-KLS-ext as external theorem",
            "DStructureTailLog4FiniteRankinIndependentAcceptance for final theorem promotion",
        ],
        "rows": rows,
        "trilemma_law": (
            "扣除 canonical RIW/Buchstab 分支后，noncanonical full-S 补集只有三种合法闭合模式。"
            "generic 自足 WFD 反原子路线已被 moving-delta capacity model 反证，所以不能由 formal WFD、"
            "Type/Fourier、K4/K6 或朴素 incidence 修复。必须证明实际源恒等、证明强化实际源反原子，"
            "或接受/证明直接作用于当前未中心化无投影 non-AP WFD 对象的精确 FullS-KLS-ext 定理。"
        ),
        "review_conclusion": (
            "第二包三歧边界已闭合：扣除 canonical 分支后，generic 自足反原子被 moving-delta "
            "反例排除；外部路线压成 `FullS-KLS-ext`/`FullSNonAPWFDKLSTheoremInput`；自足路线"
            "只能新增实际源恒等或强化实际源反原子。当前材料仍未自足证明 noncanonical 补集本身。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Noncanonical 补集三歧边界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 三歧律",
        "",
        result["trilemma_law"],
        "",
        "```text",
        f"trilemma_boundary_closed={fmt_bool(result['trilemma_boundary_closed'])}",
        (
            "self_contained_noncanonical_package_closed="
            f"{fmt_bool(result['self_contained_noncanonical_package_closed'])}"
        ),
        (
            "external_contract_package_closed_if_fulls_kls_ext_accepted="
            f"{fmt_bool(result['external_contract_package_closed_if_fulls_kls_ext_accepted'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 审查表",
        "",
        "| gate | closed | verdict | evidence | consequence | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{verdict}` | {evidence} | {consequence} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                verdict=table_cell(item["verdict"]),
                evidence=table_cell(item["evidence"]),
                consequence=table_cell(item["consequence"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(["", "## 3. 合法闭合模式", ""])
    for item in result["legal_closure_modes"]:
        lines.append(f"- {item}")
    lines.extend(["", "## 4. 仍需输入", ""])
    for item in result["open_inputs_after_trilemma"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 5. 判定",
            "",
            "这一步闭合的是第二包的“边界形状”，不是把第二包无条件证明完。"
            "完全自足 generic full-S 反原子路线已经被反例排除；"
            "若不接受外部 `FullS-KLS-ext`，就必须新增并证明实际源恒等或强化实际源反原子。"
            "即便第二包用外部定理版闭合，完整行/列定理仍需第三包 `DStructure/Rankin` 晋级输入。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract-json", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--source-antiatom-json", type=Path, default=DEFAULT_SOURCE_ANTIATOM)
    parser.add_argument("--antiatom-nogo-json", type=Path, default=DEFAULT_ANTIATOM_NOGO)
    parser.add_argument("--full-s-input-json", type=Path, default=DEFAULT_FULL_S_INPUT)
    parser.add_argument("--external-full-s-json", type=Path, default=DEFAULT_EXTERNAL_FULL_S)
    parser.add_argument("--actual-source-json", type=Path, default=DEFAULT_ACTUAL_SOURCE)
    parser.add_argument("--final-theorem-json", type=Path, default=DEFAULT_FINAL_THEOREM)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        contract_path=args.contract_json,
        source_antiatom_path=args.source_antiatom_json,
        antiatom_nogo_path=args.antiatom_nogo_json,
        full_s_input_path=args.full_s_input_json,
        external_full_s_path=args.external_full_s_json,
        actual_source_path=args.actual_source_json,
        final_theorem_path=args.final_theorem_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["open_inputs_after_trilemma"])


if __name__ == "__main__":
    main()
