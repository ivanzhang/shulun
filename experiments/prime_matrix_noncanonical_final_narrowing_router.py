#!/usr/bin/env python3
"""将 noncanonical full-S 补集压窄到最后两个真实输入。

用法示例：
  python3 experiments/prime_matrix_noncanonical_final_narrowing_router.py

输出：
  docs/monograph/prime-matrix-noncanonical-final-narrowing-router.json
  docs/monograph/prime-matrix-noncanonical-final-narrowing-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_TRILEMMA = DOCS / "prime-matrix-noncanonical-complement-trilemma-router.json"
DEFAULT_ACTUAL_SOURCE = DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
DEFAULT_AP_LIFT = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json"
DEFAULT_SOURCE_ANTIATOM = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
DEFAULT_GENERIC_NOGO = DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
DEFAULT_SOURCE_ENTROPY = DOCS / "prime-matrix-triad-a1-source-block-entropy-router.json"
DEFAULT_FULLS_INPUT = DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
DEFAULT_FULLS_EXT = DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-noncanonical-final-narrowing-router.json"
DEFAULT_MD = DOCS / "prime-matrix-noncanonical-final-narrowing-router.md"


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
    """构造 noncanonical 压窄表格行。"""
    return {
        "gate": gate,
        "closed": closed,
        "verdict": verdict,
        "evidence": evidence,
        "consequence": consequence,
        "remaining": remaining,
    }


def build_rows(
    trilemma: dict[str, Any],
    actual_source: dict[str, Any],
    ap_lift: dict[str, Any],
    source_antiatom: dict[str, Any],
    generic_nogo: dict[str, Any],
    source_entropy: dict[str, Any],
    fulls_input: dict[str, Any],
    fulls_ext: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 noncanonical 最终压窄审查表。"""
    canonical_branch_closed = (
        actual_source.get("actual_source_bridge_closed_for_canonical_branch") is True
        and actual_source.get("actual_source_bridge_closes_global_unrestricted") is False
    )
    ap_lift_rejected = (
        ap_lift.get("ap_source_lift_rejected") is True
        and ap_lift.get("ap_source_lift_available") is False
    )
    source_antiatom_reduced = (
        source_antiatom.get("source_antiatom_reduction_closed") is False
        and "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"
        in source_antiatom.get("open_antiatom_gates", [])
    )
    generic_refuted = (
        generic_nogo.get("self_contained_generic_version_refuted") is True
        and generic_nogo.get("external_contract_version_closed") is True
    )
    entropy_not_forced = (
        source_entropy.get("current_internal_source_entropy_closed") is False
        and source_entropy.get("conditional_source_entropy_implies_ncblk") is True
    )
    fulls_input_open = (
        fulls_input.get("new_full_s_theorem_input_closed") is False
        and "FullSNonAPWFDKLSTheoremInput" in fulls_input.get("open_input_gates", [])
    )
    external_contract_ready = (
        fulls_ext.get("external_theorem_contract_closed") is True
        and fulls_ext.get("self_contained_primary_source_proof_closed") is False
    )
    trilemma_closed = trilemma.get("trilemma_boundary_closed") is True

    return [
        row(
            gate="CanonicalBranchRemoved",
            closed=canonical_branch_closed,
            verdict="closed_for_canonical_only",
            evidence="actual-source global reconciliation",
            consequence="canonical RIW/Buchstab 分支已闭合，不能再当作 noncanonical 缺口。",
            remaining="noncanonical complement only",
        ),
        row(
            gate="APSourceLiftRejected",
            closed=ap_lift_rejected,
            verdict="route_rejected",
            evidence="AP-source lift no-go router",
            consequence="non-AP generic WFD 补集不能无损回提为 BFI prime-AP discrepancy。",
            remaining="NewFullSTheoremInput or strengthened source theorem",
        ),
        row(
            gate="GenericSelfContainedAntiAtomRefuted",
            closed=generic_refuted,
            verdict="generic_statement_false",
            evidence="moving-delta anti-atom no-go router",
            consequence="形式 WFD/Type/Fourier 假设下的 generic 反原子命题为假。",
            remaining="strengthen actual source, restrict source, or accept external theorem",
        ),
        row(
            gate="SourceAntiAtomReductionPinned",
            closed=source_antiatom_reduced,
            verdict="reduced_open",
            evidence="full-S source anti-atom router",
            consequence="支撑+容量兼容已等价压成最终 source capacity measure 无 moving atom。",
            remaining="prove strengthened source anti-atom or external dispersion match",
        ),
        row(
            gate="ExactWFDSourceEntropyNotForced",
            closed=entropy_not_forced,
            verdict="sufficient_but_unproved",
            evidence="source block entropy router",
            consequence="ExactWFDSourceEntropy 一旦成立可推出 NC-BLK，但不由当前形式输入强制。",
            remaining="prove exact entropy for actual coefficients",
        ),
        row(
            gate="FullSNonAPWFDKLSInputPinned",
            closed=fulls_input_open,
            verdict="single_external_or_new_deep_theorem_atom",
            evidence="new full-S theorem input router",
            consequence="外部/新深定理路线已压成一个未中心化、无投影、full-S non-AP WFD KLS 输入。",
            remaining="prove or accept FullSNonAPWFDKLSTheoremInput",
        ),
        row(
            gate="ExternalContractReadyIfAccepted",
            closed=external_contract_ready,
            verdict="conditional_external_closed",
            evidence="FullS-KLS-ext specialization router",
            consequence="接受 FullS-KLS-ext 时对象/尺度/无投影兼容已经写入合同。",
            remaining="explicit external acceptance or new proof",
        ),
        row(
            gate="TrilemmaBoundaryStillHonest",
            closed=trilemma_closed,
            verdict="boundary_closed_not_theorem",
            evidence="noncanonical complement trilemma router",
            consequence="三歧边界闭合，但自足 noncanonical 补集没有由当前材料证明。",
            remaining="two real choices remain",
        ),
    ]


def run(
    trilemma_path: Path,
    actual_source_path: Path,
    ap_lift_path: Path,
    source_antiatom_path: Path,
    generic_nogo_path: Path,
    source_entropy_path: Path,
    fulls_input_path: Path,
    fulls_ext_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 noncanonical 最终压窄路由。"""
    trilemma = load_json(trilemma_path)
    actual_source = load_json(actual_source_path)
    ap_lift = load_json(ap_lift_path)
    source_antiatom = load_json(source_antiatom_path)
    generic_nogo = load_json(generic_nogo_path)
    source_entropy = load_json(source_entropy_path)
    fulls_input = load_json(fulls_input_path)
    fulls_ext = load_json(fulls_ext_path)

    rows = build_rows(
        trilemma=trilemma,
        actual_source=actual_source,
        ap_lift=ap_lift,
        source_antiatom=source_antiatom,
        generic_nogo=generic_nogo,
        source_entropy=source_entropy,
        fulls_input=fulls_input,
        fulls_ext=fulls_ext,
    )
    narrowing_closed = all(item["closed"] for item in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_noncanonical_final_narrowing_router",
        "status": "noncanonical_final_narrowed_to_exact_source_entropy_or_full_s_kls_input",
        "narrowing_law": (
            "noncanonical full-S 补集的可行路线继续压窄：APSourceLift 被拒绝，"
            "generic 自足反原子被 moving-delta 反证，canonical 分支已经移出。"
            "当前只剩两个真实输入：证明 exact/actual source entropy 或强化实际源反原子；"
            "或者接受/证明 FullSNonAPWFDKLSTheoremInput。"
        ),
        "noncanonical_narrowing_boundary_closed": narrowing_closed,
        "ap_source_lift_rejected": ap_lift.get("ap_source_lift_rejected") is True,
        "generic_self_contained_antiatom_refuted": generic_nogo.get("self_contained_generic_version_refuted") is True,
        "exact_source_entropy_closed": source_entropy.get("current_internal_source_entropy_closed") is True,
        "external_full_s_contract_closed_if_accepted": fulls_ext.get("external_theorem_contract_closed") is True,
        "self_contained_noncanonical_closed": False,
        "row_column_unconditional_closed": False,
        "remaining_noncanonical_choices": [
            "InternalNewTheorem: prove ExactWFDSourceEntropy / FullSNonAPStrengthenedSourceAntiAtom for the actual source",
            "ExternalDeepInput: accept or prove FullSNonAPWFDKLSTheoremInput",
        ],
        "review_conclusion": (
            "Noncanonical 补集已从三歧继续压成两项真实输入：内部新增 exact source entropy/强化反原子，"
            "或外部/新证 FullSNonAPWFDKLSTheoremInput。APSourceLift 与 generic 反原子路线不再可用；"
            "当前材料仍未闭合 self-contained noncanonical 包。"
        ),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path)
            for path in [
                trilemma_path,
                actual_source_path,
                ap_lift_path,
                source_antiatom_path,
                generic_nogo_path,
                source_entropy_path,
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
        "# Prime Matrix Noncanonical 最终压窄路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 压窄律",
        "",
        result["narrowing_law"],
        "",
        "```text",
        f"noncanonical_narrowing_boundary_closed={fmt_bool(result['noncanonical_narrowing_boundary_closed'])}",
        f"ap_source_lift_rejected={fmt_bool(result['ap_source_lift_rejected'])}",
        f"generic_self_contained_antiatom_refuted={fmt_bool(result['generic_self_contained_antiatom_refuted'])}",
        f"exact_source_entropy_closed={fmt_bool(result['exact_source_entropy_closed'])}",
        f"external_full_s_contract_closed_if_accepted={fmt_bool(result['external_full_s_contract_closed_if_accepted'])}",
        f"self_contained_noncanonical_closed={fmt_bool(result['self_contained_noncanonical_closed'])}",
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
                closed=fmt_bool(item["closed"]),
                verdict=table_cell(item["verdict"]),
                evidence=table_cell(item["evidence"]),
                consequence=table_cell(item["consequence"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(["", "## 3. 剩余真实选择", ""])
    lines.extend(f"- `{item}`" for item in result["remaining_noncanonical_choices"])
    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            (
                "noncanonical 最窄点已经不是 APSourceLift，也不是 generic WFD 反原子。"
                "当前内部路线必须证明 actual/exact source entropy；外部路线必须接受或证明 full-S non-AP WFD KLS 输入。"
            ),
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trilemma", type=Path, default=DEFAULT_TRILEMMA)
    parser.add_argument("--actual-source", type=Path, default=DEFAULT_ACTUAL_SOURCE)
    parser.add_argument("--ap-lift", type=Path, default=DEFAULT_AP_LIFT)
    parser.add_argument("--source-antiatom", type=Path, default=DEFAULT_SOURCE_ANTIATOM)
    parser.add_argument("--generic-nogo", type=Path, default=DEFAULT_GENERIC_NOGO)
    parser.add_argument("--source-entropy", type=Path, default=DEFAULT_SOURCE_ENTROPY)
    parser.add_argument("--fulls-input", type=Path, default=DEFAULT_FULLS_INPUT)
    parser.add_argument("--fulls-ext", type=Path, default=DEFAULT_FULLS_EXT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        trilemma_path=args.trilemma,
        actual_source_path=args.actual_source,
        ap_lift_path=args.ap_lift,
        source_antiatom_path=args.source_antiatom,
        generic_nogo_path=args.generic_nogo,
        source_entropy_path=args.source_entropy,
        fulls_input_path=args.fulls_input,
        fulls_ext_path=args.fulls_ext,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["remaining_noncanonical_choices"])


if __name__ == "__main__":
    main()
