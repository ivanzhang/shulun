#!/usr/bin/env python3
"""Prime Matrix 最终数学输入压缩路由器。

用法示例：
  python3 experiments/prime_matrix_final_math_input_compression_router.py

输出：
  docs/monograph/prime-matrix-final-math-input-compression-router.json
  docs/monograph/prime-matrix-final-math-input-compression-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SOURCE_AUDIT = DOCS / "prime-matrix-actual-source-antiatom-lane-audit-router.json"
DEFAULT_CDEP = DOCS / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json"
DEFAULT_FULLS_EXT = DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
DEFAULT_NEW_FULLS = DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-final-math-input-compression-router.json"
DEFAULT_MD = DOCS / "prime-matrix-final-math-input-compression-router.md"

SOURCE_AXIOM = "AddStrengthenedActualSourceAntiAtomTheorem"
EXTERNAL_FULLS = "FullSNonAPWFDKLSTheoremInput_OR_DIBFIPrimarySourceSpecializationProof"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    proved_or_accepted: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved_or_accepted": proved_or_accepted,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    source_audit: dict[str, Any],
    cdep: dict[str, Any],
    fulls_ext: dict[str, Any],
    new_fulls: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成最终数学输入压缩表。"""
    source_lane_compressed = (
        source_audit.get("actual_source_antiatom_lane_boundary_closed") is True
        and source_audit.get("actual_source_antiatom_proved") is False
        and source_audit.get("self_contained_source_lane_remaining") == SOURCE_AXIOM
    )
    cdep_to_ncblk_or_external = (
        cdep.get("terminal_gap_after_router") == "NCBLKActualBlockNonConcentrationOrExternalDIBFI"
        and cdep.get("c_dependent_residue_spectral_reduction_closed") is False
    )
    external_contract_ready = (
        fulls_ext.get("external_theorem_contract_closed") is True
        and fulls_ext.get("self_contained_primary_source_proof_closed") is False
    )
    new_fulls_pinned = (
        new_fulls.get("terminal_gap_after_router") == "FullSNonAPWFDKLSTheoremInput"
        and new_fulls.get("new_full_s_theorem_input_closed") is False
    )
    compression_closed = all(
        [source_lane_compressed, cdep_to_ncblk_or_external, external_contract_ready, new_fulls_pinned]
    )
    return [
        row(
            "SourceLaneCompressedToNewAxiom",
            source_lane_compressed,
            False,
            "自足 source lane 不能由现有账本推出；若坚持自足，必须新增强化实际源反原子定理。",
            SOURCE_AXIOM,
        ),
        row(
            "CDependentSpectralReducesToNCBLKOrExternal",
            cdep_to_ncblk_or_external,
            False,
            "c-dependent residue 谱输入的自足版回到实际块非集中；外部版回到 DI/BFI/Kuznetsov。",
            f"{SOURCE_AXIOM} OR external dispersion",
        ),
        row(
            "ExternalFullSContractReadyButPrimaryProofOpen",
            external_contract_ready,
            False,
            "FullS-KLS-ext 合同对象已固定，但尚无逐主来源专门化证明。",
            "DIBFIPrimarySourceSpecializationProof or explicit external acceptance",
        ),
        row(
            "FullSNonAPWFDKLSTheoremInputPinned",
            new_fulls_pinned,
            False,
            "新 full-S non-AP WFD KLS 定理输入已是单一可审稿原子。",
            "prove or accept exact FullS-KLS theorem",
        ),
        row(
            "FinalMathInputCompressed",
            compression_closed,
            False,
            "最终数学输入压缩为：新增强化实际源反原子定理，或证明/接受精确 FullS-KLS 外部深定理。",
            f"{SOURCE_AXIOM} OR {EXTERNAL_FULLS}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行最终数学输入压缩。"""
    source_audit = load_json(paths["source_audit"])
    cdep = load_json(paths["cdep"])
    fulls_ext = load_json(paths["fulls_ext"])
    new_fulls = load_json(paths["new_fulls"])
    rows = build_rows(source_audit, cdep, fulls_ext, new_fulls)
    compression_closed = next(item["closed"] for item in rows if item["gate"] == "FinalMathInputCompressed")
    return {
        "certificate_type": "prime_matrix_final_math_input_compression_router",
        "status": "final_math_input_compressed_source_axiom_or_external_fulls_open"
        if compression_closed
        else "final_math_input_compression_incomplete",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "final_math_input_compression_closed": compression_closed,
        "final_math_input_proved_or_accepted": False,
        "self_contained_math_input": SOURCE_AXIOM,
        "external_math_input": EXTERNAL_FULLS,
        "promotion_input": DSTRUCTURE,
        "minimum_unconditional_basis": f"({SOURCE_AXIOM} OR {EXTERNAL_FULLS}) AND {DSTRUCTURE}",
        "next_priority": SOURCE_AXIOM,
        "external_fallback_priority": EXTERNAL_FULLS,
        "reduction_formula": (
            "Noncanonical final math input => "
            f"{SOURCE_AXIOM} OR {EXTERNAL_FULLS}; final promotion still requires {DSTRUCTURE}."
        ),
        "plain_conclusion": (
            "最终数学输入已压缩到两个不可再偷换的入口：完全自足路线必须新增并证明强化实际源反原子定理；"
            "外部/新深定理路线必须证明或明确接受精确 FullS non-AP WFD KLS 定理，并完成主来源专门化。"
            "二者当前都未证明或接受。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved_or_accepted"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 最终数学输入压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"final_math_input_compression_closed={fmt_bool(result['final_math_input_compression_closed'])}",
        f"final_math_input_proved_or_accepted={fmt_bool(result['final_math_input_proved_or_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved_or_accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved_or_accepted"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 最小无条件输入基",
            "",
            f"`{result['minimum_unconditional_basis']}`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-audit", type=Path, default=DEFAULT_SOURCE_AUDIT)
    parser.add_argument("--cdep", type=Path, default=DEFAULT_CDEP)
    parser.add_argument("--fulls-ext", type=Path, default=DEFAULT_FULLS_EXT)
    parser.add_argument("--new-fulls", type=Path, default=DEFAULT_NEW_FULLS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "source_audit": args.source_audit,
        "cdep": args.cdep,
        "fulls_ext": args.fulls_ext,
        "new_fulls": args.new_fulls,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
