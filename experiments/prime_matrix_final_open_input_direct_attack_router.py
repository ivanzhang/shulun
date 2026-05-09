#!/usr/bin/env python3
"""Prime Matrix 最终开放输入直接攻击路由器。

用法示例：
  python3 experiments/prime_matrix_final_open_input_direct_attack_router.py

输出：
  docs/monograph/prime-matrix-final-open-input-direct-attack-router.json
  docs/monograph/prime-matrix-final-open-input-direct-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_FINAL_COMPRESSION = DOCS / "prime-matrix-final-math-input-compression-router.json"
DEFAULT_SOURCE_LANE = DOCS / "prime-matrix-actual-source-antiatom-lane-audit-router.json"
DEFAULT_MULTIPLIER = DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json"
DEFAULT_EXACT_UV = DOCS / "prime-matrix-exact-uv-support-terminal-attack-router.json"
DEFAULT_FULLS_EXT = DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-final-open-input-direct-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-final-open-input-direct-attack-router.md"

SOURCE_AXIOM = "AddStrengthenedActualSourceAntiAtomTheorem"
EXACT_UV = "ActualNoncanonicalExactUVSupportLowerBound"
EXTERNAL_FULLS = "FullSNonAPWFDKLSTheoremInput_OR_DIBFIPrimarySourceSpecializationProof"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
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
    role: str,
    evidence: str,
    remaining: str,
) -> dict[str, Any]:
    """构造攻击判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved_or_accepted": proved_or_accepted,
        "role": role,
        "evidence": evidence,
        "remaining": remaining,
    }


def build_rows(
    final_compression: dict[str, Any],
    source_lane: dict[str, Any],
    multiplier: dict[str, Any],
    exact_uv: dict[str, Any],
    fulls_ext: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成最终开放输入直接攻击表。"""
    final_input_imported = (
        final_compression.get("final_math_input_compression_closed") is True
        and final_compression.get("self_contained_math_input") == SOURCE_AXIOM
        and final_compression.get("external_math_input") == EXTERNAL_FULLS
        and final_compression.get("final_math_input_proved_or_accepted") is False
    )
    source_lane_requires_axiom = (
        source_lane.get("actual_source_antiatom_lane_boundary_closed") is True
        and source_lane.get("actual_source_antiatom_proved") is False
        and source_lane.get("self_contained_source_lane_remaining") == SOURCE_AXIOM
    )
    multiplier_closed = (
        multiplier.get("registered_capacity_multiplier_discipline_closed") is True
        and multiplier.get("remaining_source_microinput") == EXACT_UV
    )
    exact_uv_unique_open = (
        exact_uv.get("exact_uv_support_terminal_boundary_closed") is True
        and exact_uv.get("unique_source_terminal_input") == EXACT_UV
        and exact_uv.get("exact_uv_support_proved") is False
    )
    source_axiom_decomposed = (
        source_lane_requires_axiom and multiplier_closed and exact_uv_unique_open
    )
    external_lane_open = (
        fulls_ext.get("external_theorem_contract_closed") is True
        and fulls_ext.get("self_contained_primary_source_proof_closed") is False
    )
    dstructure_open = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )
    return [
        row(
            "FinalMathInputCompressionImported",
            final_input_imported,
            False,
            "导入上一层最终数学输入压缩式。",
            "final compression router",
            f"({SOURCE_AXIOM} OR {EXTERNAL_FULLS}) AND {DSTRUCTURE}",
        ),
        row(
            "SourceLaneRequiresStrengthenedActualSourceAxiom",
            source_lane_requires_axiom,
            False,
            "actual-source lane 不能由现有 canonical/generic 材料推出，只能新增实际源强化反原子或转外部谱输入。",
            "actual-source antiatom lane audit",
            SOURCE_AXIOM,
        ),
        row(
            "RegisteredCapacityMultiplierDisciplineDischarged",
            multiplier_closed,
            True,
            "Type/Fourier/fiber 等成本已在同一 formal unit 登记为 log-power 乘子，不再是开放数学输入。",
            "registered capacity multiplier discipline",
            EXACT_UV,
        ),
        row(
            "StrengthenedActualSourceAxiomReducedToExactUV",
            source_axiom_decomposed,
            False,
            "在乘子纪律闭合后，强化实际源反原子等价压到 actual noncanonical exact u/v 支撑下界。",
            "source lane + multiplier + ExactUV terminal audit",
            EXACT_UV,
        ),
        row(
            "ExactUVSupportStillUnproved",
            exact_uv_unique_open,
            False,
            "当前材料没有证明 actual noncanonical exact u/v 支撑；K4/K6、朴素 incidence、canonical 支撑链均不能偷渡。",
            "ExactUV terminal attack",
            f"prove {EXACT_UV} or prove final capacity anti-atom directly",
        ),
        row(
            "ExternalFullSLaneStillOpen",
            external_lane_open,
            False,
            "外部 FullS-KLS 合同对象已固定，但主来源专门化证明或明确外部接受仍未完成。",
            "FullS-KLS external specialization router",
            EXTERNAL_FULLS,
        ),
        row(
            "DStructureRankinAcceptanceStillIndependent",
            dstructure_open,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门，不能由作者侧路由自审关闭。",
            "DStructure/Rankin promotion acceptance router",
            DSTRUCTURE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行最终开放输入直接攻击。"""
    final_compression = load_json(paths["final_compression"])
    source_lane = load_json(paths["source_lane"])
    multiplier = load_json(paths["multiplier"])
    exact_uv = load_json(paths["exact_uv"])
    fulls_ext = load_json(paths["fulls_ext"])
    dstructure = load_json(paths["dstructure"])
    rows = build_rows(
        final_compression=final_compression,
        source_lane=source_lane,
        multiplier=multiplier,
        exact_uv=exact_uv,
        fulls_ext=fulls_ext,
        dstructure=dstructure,
    )
    boundary_closed = all(item["closed"] for item in rows)
    final_proved_or_accepted = (
        exact_uv.get("exact_uv_support_proved") is True
        or final_compression.get("final_math_input_proved_or_accepted") is True
    ) and dstructure.get("promotion_package_independently_accepted") is True
    latest_basis = f"({EXACT_UV} OR {EXTERNAL_FULLS}) AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_final_open_input_direct_attack_router",
        "status": "final_open_input_reduced_to_exact_uv_or_external_fulls_plus_dstructure_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "final_open_input_direct_attack_boundary_closed": boundary_closed,
        "final_open_input_proved_or_accepted": final_proved_or_accepted,
        "source_axiom_before_attack": SOURCE_AXIOM,
        "self_contained_source_input_after_attack": EXACT_UV,
        "external_source_input_after_attack": EXTERNAL_FULLS,
        "promotion_input": DSTRUCTURE,
        "latest_unconditional_basis": latest_basis,
        "next_priority": EXACT_UV,
        "external_fallback_priority": EXTERNAL_FULLS,
        "parallel_acceptance_priority": DSTRUCTURE,
        "attack_formula": (
            f"{SOURCE_AXIOM} + RegisteredCapacityMultiplierDiscipline "
            f"=> {EXACT_UV}; hence final basis becomes {latest_basis}."
        ),
        "plain_conclusion": (
            "最终开放输入被继续压窄：`AddStrengthenedActualSourceAntiAtomTheorem` 不再作为一个"
            "黑箱大名停留。乘子纪律已经闭合，所以完全自足路线的实质只剩 "
            "`ActualNoncanonicalExactUVSupportLowerBound`。外部路线仍是精确 FullS non-AP WFD KLS"
            " 或 DI/BFI 主来源专门化；最终晋级仍需 DStructure/Rankin 独立验收。当前没有无条件闭合。"
        ),
        "conditional_closure_statement": (
            f"If {EXACT_UV} is proved, then the registered multiplier ledger gives the final "
            f"capacity anti-atom for the actual source; with {DSTRUCTURE}, the current "
            "final-input chain can promote. Without ExactUV or external FullS acceptance, it cannot."
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved_or_accepted"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 最终开放输入直接攻击路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"final_open_input_direct_attack_boundary_closed={fmt_bool(result['final_open_input_direct_attack_boundary_closed'])}",
        f"final_open_input_proved_or_accepted={fmt_bool(result['final_open_input_proved_or_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 直接攻击公式",
        "",
        "```text",
        result["attack_formula"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved_or_accepted | role | evidence | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {role} | {evidence} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved_or_accepted"]),
                role=table_cell(item["role"]),
                evidence=table_cell(item["evidence"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 最新最小输入基",
            "",
            f"`{result['latest_unconditional_basis']}`",
            "",
            "## 4. 条件闭合语句",
            "",
            result["conditional_closure_statement"],
            "",
            "## 5. 下一步",
            "",
            f"内部最窄点：`{result['next_priority']}`。",
            f"外部备选点：`{result['external_fallback_priority']}`。",
            f"并行验收点：`{result['parallel_acceptance_priority']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-compression", type=Path, default=DEFAULT_FINAL_COMPRESSION)
    parser.add_argument("--source-lane", type=Path, default=DEFAULT_SOURCE_LANE)
    parser.add_argument("--multiplier", type=Path, default=DEFAULT_MULTIPLIER)
    parser.add_argument("--exact-uv", type=Path, default=DEFAULT_EXACT_UV)
    parser.add_argument("--fulls-ext", type=Path, default=DEFAULT_FULLS_EXT)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "final_compression": args.final_compression,
        "source_lane": args.source_lane,
        "multiplier": args.multiplier,
        "exact_uv": args.exact_uv,
        "fulls_ext": args.fulls_ext,
        "dstructure": args.dstructure,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
