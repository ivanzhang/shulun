#!/usr/bin/env python3
"""生成 source entropy 下游 signed 坐标-来源环同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_source_entropy_downstream_cycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json

输出：
  data/prime-matrix-strict-source-entropy-downstream-cycle-sync-ledger.json
  docs/monograph/prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json
  docs/monograph/prime-matrix-strict-source-entropy-downstream-cycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-source-entropy-downstream-cycle-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-source-entropy-downstream-cycle-sync-router.md"

NEW_PRIMITIVE = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"
SOURCE_ENTROPY = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"
PRIMITIVE_COEFF = DOCS / "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"
BASIS_SOURCE = DOCS / "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json"
INTERNAL_EXPANSION = DOCS / "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json"
COORD_CYCLE = DOCS / "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"
TERMINAL_TO_KERNEL = DOCS / "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json"

DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
SIGNED_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
BASIS_WEIGHT = "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows"
INTERNAL_BASIS = "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy"
BASIS_ALPHABET = "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger"
CYCLE_CUT_INPUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_SPECTRAL = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失返回空对象，避免把缺失当证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        NEW_PRIMITIVE,
        SOURCE_ENTROPY,
        PRIMITIVE_COEFF,
        BASIS_SOURCE,
        INTERNAL_EXPANSION,
        COORD_CYCLE,
        TERMINAL_TO_KERNEL,
    ]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def downstream_edges(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """整理 source entropy 到坐标-来源环的下游边。"""
    return [
        {
            "from": DOMAIN_ENTROPY,
            "to": SIGNED_LAW,
            "closed": data["source_entropy"].get("next_direct_attack_target") == SIGNED_LAW,
            "meaning": "source-domain entropy 的首原子压到 signed row emitter 内每行 signed coefficient law。",
        },
        {
            "from": SIGNED_LAW,
            "to": BASIS_WEIGHT,
            "closed": data["primitive_coeff"].get("next_direct_attack_target") == BASIS_WEIGHT,
            "meaning": "primitive row signed coefficient law 的第一不可替代字段是 basis weight source。",
        },
        {
            "from": BASIS_WEIGHT,
            "to": INTERNAL_BASIS,
            "closed": data["basis_source"].get("next_direct_attack_target") == INTERNAL_BASIS,
            "meaning": "basis weight source 必须由 seed 内部 pre-Cauchy 算术基展开给出。",
        },
        {
            "from": INTERNAL_BASIS,
            "to": BASIS_ALPHABET,
            "closed": data["internal_expansion"].get("next_direct_attack_target") == BASIS_ALPHABET,
            "meaning": "内部算术基展开首先需要 noncanonical pre-Cauchy basis alphabet。",
        },
        {
            "from": BASIS_ALPHABET,
            "to": "WordCoordinateFormula cycle",
            "closed": data["coord_cycle"].get("seed_coordinate_source_cycle_detected") is True,
            "meaning": "继续沿 basis alphabet、basis word generation、word formula 会回到 word coordinate 依赖环。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    new_primitive_imported = data["new_primitive"].get("next_direct_attack_target") == DOMAIN_ENTROPY
    edges = downstream_edges(data)
    source_chain_closed = all(item["closed"] for item in edges)
    cycle_guard = data["coord_cycle"]
    terminal_kernel = data["terminal_to_kernel"]
    cycle_detected = cycle_guard.get("seed_coordinate_source_cycle_detected") is True
    raw_cycle_rejected = cycle_guard.get("raw_cycle_counts_as_closure") is False
    cycle_cut_missing = cycle_guard.get("primitive_basis_and_coefficient_source_input_proved") is False
    terminal_descent_open = (
        cycle_guard.get("acyclic_terminal_return_well_founded_descent_proved") is False
    )
    terminal_to_kernel_synced = (
        terminal_kernel.get("next_direct_attack_target")
        == "AlphaRowAnchorPhaseEmissionFormulaLedger"
    )

    return [
        row(
            "NewPrimitiveImportsSourceEntropyAtom",
            new_primitive_imported,
            False,
            "上一轮 new primitive 出口已把直接主攻压到 actual source-domain absolute entropy。",
            DOMAIN_ENTROPY,
        ),
        row(
            "SourceEntropyDownstreamEdgesClosed",
            source_chain_closed,
            True,
            "source entropy -> signed coefficient law -> basis weight source -> internal basis expansion -> basis alphabet 的下游同步闭合。",
            "cycle guard",
        ),
        row(
            "SeedCoordinateSourceCycleImported",
            cycle_detected and raw_cycle_rejected,
            True,
            "basis alphabet 继续展开后进入 signed 坐标-来源闭合依赖环；该环已被判定不能作为证明。",
            CYCLE_CUT_INPUT,
        ),
        row(
            "PrimitiveBasisCoefficientCycleCutInputCurrentCorpusProved",
            False,
            False,
            "当前语料没有提交同时给 primitive basis words 与 signed coefficients 的无环 pre-Cauchy 源输入。",
            CYCLE_CUT_INPUT,
        ),
        row(
            "TerminalDescentAlternativeStillOpen",
            True,
            False,
            "若拒绝循环定义，source entropy 分支只能回流 terminal family；该分支仍需 well-founded descent 或 canonical-lock。",
            TERMINAL_DESCENT,
        ),
        row(
            "TerminalDescentDownstreamSyncedToKernelTable",
            terminal_to_kernel_synced,
            False,
            "terminal descent 下游已同步到 pointwise primitive kernel table/alpha row formula，但该路也未闭合。",
            "AlphaRowAnchorPhaseEmissionFormulaLedger",
        ),
        row(
            "CompleteKeyAndFixedKeyStillParallel",
            True,
            False,
            "本步只关闭 source-domain entropy 首原子的下游口径；source rank/no-collapse 包的 complete-key 与 fixed-key multiplicity 仍独立开放。",
            f"{COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步到 signed 坐标-来源环守卫；未证明 cycle-cut 输入、terminal descent、PDEC、外部谱、complete/fixed-key 或 DStructure。",
            (
                f"(({CYCLE_CUT_INPUT} AND {COMPLETE_KEY} AND {FIXED_KEY}) "
                f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}) "
                f"AND {DSTRUCTURE}"
            ),
        ),
    ]


def build_result() -> dict[str, Any]:
    """生成同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "new_primitive": load_json(NEW_PRIMITIVE),
        "source_entropy": load_json(SOURCE_ENTROPY),
        "primitive_coeff": load_json(PRIMITIVE_COEFF),
        "basis_source": load_json(BASIS_SOURCE),
        "internal_expansion": load_json(INTERNAL_EXPANSION),
        "coord_cycle": load_json(COORD_CYCLE),
        "terminal_to_kernel": load_json(TERMINAL_TO_KERNEL),
    }
    edges = downstream_edges(data)
    rows = build_rows(data)
    activity_basis = (
        f"(({CYCLE_CUT_INPUT} AND {COMPLETE_KEY} AND {FIXED_KEY}) "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}) "
        f"AND {DSTRUCTURE}"
    )
    result = {
        "certificate_type": "prime_matrix_strict_source_entropy_downstream_cycle_sync_router",
        "status": "source_entropy_downstream_synced_to_seed_coordinate_cycle_guard_open",
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "source_entropy_downstream_edges_closed": all(item["closed"] for item in edges),
        "seed_coordinate_source_cycle_detected": data["coord_cycle"].get("seed_coordinate_source_cycle_detected") is True,
        "raw_cycle_counts_as_closure": False,
        "primitive_basis_and_coefficient_source_input_proved": False,
        "acyclic_terminal_descent_proved": False,
        "complete_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_proved": False,
        "row_column_unconditional_closed": False,
        "downstream_edges": edges,
        "imported_cycle_edges": data["coord_cycle"].get("cycle_edges", []),
        "decision_rows": rows,
        "next_direct_attack_target": f"{CYCLE_CUT_INPUT}_OR_{TERMINAL_DESCENT}",
        "latest_strict_activity_basis": activity_basis,
        "plain_conclusion": (
            f"本步把上一轮的 `{DOMAIN_ENTROPY}` 沿既有下游证书同步到底："
            "source entropy 首原子经 signed coefficient law、basis weight source、internal basis expansion "
            "和 basis alphabet 后进入 signed 坐标-来源闭合依赖环。该环不能作为证明；若不提交无环 "
            f"`{CYCLE_CUT_INPUT}`，只能回流 `{TERMINAL_DESCENT}` 或其他独立出口。"
            "complete-key、fixed-key、PDEC/外部谱与 DStructure/Rankin 仍开放，行/列命题未无条件闭合。"
        ),
        "source_hashes": source_hashes(),
    }
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict source entropy downstream cycle sync router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"source_entropy_downstream_edges_closed={fmt_bool(result['source_entropy_downstream_edges_closed'])}",
        f"seed_coordinate_source_cycle_detected={fmt_bool(result['seed_coordinate_source_cycle_detected'])}",
        f"raw_cycle_counts_as_closure={fmt_bool(result['raw_cycle_counts_as_closure'])}",
        f"primitive_basis_and_coefficient_source_input_proved={fmt_bool(result['primitive_basis_and_coefficient_source_input_proved'])}",
        f"acyclic_terminal_descent_proved={fmt_bool(result['acyclic_terminal_descent_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 下游同步链",
        "",
        "| from | to | closed | meaning |",
        "| --- | --- | ---: | --- |",
    ]
    for item in result["downstream_edges"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['from'])}`",
                    f"`{table_cell(item['to'])}`",
                    fmt_bool(item["closed"]),
                    table_cell(item["meaning"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 坐标-来源环",
            "",
            "| node | next | edge matches |",
            "| --- | --- | ---: |",
        ]
    )
    for item in result["imported_cycle_edges"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item.get('node', ''))}`",
                    f"`{table_cell(item.get('actual_next', ''))}`",
                    fmt_bool(item.get("edge_matches")),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    fmt_bool(item["closed"]),
                    fmt_bool(item["proved"]),
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 最新剩余基",
            "",
            "```text",
            result["latest_strict_activity_basis"],
            "```",
            "",
            "## 5. 结论边界",
            "",
            "- 本步是下游同步和闭环守卫，不是行/列命题证明。",
            "- source entropy 首原子不能通过 signed 坐标-来源环自证。",
            "- 当前下一主攻为 cycle-cut primitive basis/coefficient 源输入或 terminal descent。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(name)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """入口。"""
    result = build_result()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
