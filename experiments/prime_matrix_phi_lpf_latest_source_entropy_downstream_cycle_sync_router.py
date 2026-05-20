#!/usr/bin/env python3
"""生成 Phi-LPF latest source-entropy 下游环守卫同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_source_entropy_downstream_cycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_SOURCE_ATOM_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.json"
)
PHI_LPF_SOURCE_ENTROPY_CERT = DOCS / "prime-matrix-phi-lpf-source-entropy-signed-survival-router.json"
STRICT_DOWNSTREAM_CERT = DOCS / "prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json"
SOURCE_ENTROPY_CERT = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"
COORD_CYCLE_CERT = DOCS / "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"
TERMINAL_TO_KERNEL_CERT = DOCS / "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
SIGNED_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
BASIS_WEIGHT = "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows"
INTERNAL_BASIS = "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy"
BASIS_ALPHABET = "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger"
CYCLE_CUT_INPUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
SIGNED_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_SPECTRAL = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_SOURCE_ATOM_CERT,
        PHI_LPF_SOURCE_ENTROPY_CERT,
        STRICT_DOWNSTREAM_CERT,
        SOURCE_ENTROPY_CERT,
        COORD_CYCLE_CERT,
        TERMINAL_TO_KERNEL_CERT,
        POINTWISE_FRONTIER_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def largest_capacity_sample(phi_lpf_source: dict[str, Any]) -> dict[str, Any]:
    """抽取 Phi-LPF 容量审计中的最大 N 样本。"""
    samples = phi_lpf_source.get("sample_capacity_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def imported_downstream_edges(strict_downstream: dict[str, Any]) -> list[dict[str, Any]]:
    """导入 strict source entropy 下游边。"""
    edges = strict_downstream.get("downstream_edges", [])
    if edges:
        return edges
    return [
        {
            "from": DOMAIN_ENTROPY,
            "to": SIGNED_LAW,
            "closed": False,
            "meaning": "strict downstream 证书缺失时不能视为已同步。",
        },
        {
            "from": SIGNED_LAW,
            "to": BASIS_WEIGHT,
            "closed": False,
            "meaning": "strict downstream 证书缺失时不能视为已同步。",
        },
        {
            "from": BASIS_WEIGHT,
            "to": INTERNAL_BASIS,
            "closed": False,
            "meaning": "strict downstream 证书缺失时不能视为已同步。",
        },
        {
            "from": INTERNAL_BASIS,
            "to": BASIS_ALPHABET,
            "closed": False,
            "meaning": "strict downstream 证书缺失时不能视为已同步。",
        },
    ]


def support_boundary(phi_lpf_source: dict[str, Any]) -> list[dict[str, str]]:
    """列出 LPF/Phi 能支付与不能支付的 source-entropy 子字段。"""
    atoms = phi_lpf_source.get("split_atoms", [])
    if atoms:
        return atoms
    return [
        {
            "atom": "PhiLPFCandidateRowCapacityLowerBoundLedger",
            "status": "closed_unsigned",
            "role": "LPF/Phi 桶只支付候选 row 容量。",
        },
        {
            "atom": SIGNED_SURVIVAL,
            "status": "open_signed",
            "role": "actual source entropy 仍需非零 signed row 存活。",
        },
        {
            "atom": ROW_MASS,
            "status": "open_signed",
            "role": "同一 formal unit 中仍需 row-mass/no-heavy-row 账本。",
        },
        {
            "atom": SIGNED_EXPR,
            "status": "open_formula",
            "role": "仍需逐 primitive summand 的推前前 signed coefficient 表达式。",
        },
    ]


def build_rows(
    latest_source: dict[str, Any],
    phi_lpf_source: dict[str, Any],
    strict_downstream: dict[str, Any],
    source_entropy: dict[str, Any],
    coord_cycle: dict[str, Any],
    terminal_to_kernel: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest source-entropy 下游同步判定表。"""
    latest_imported = (
        latest_source.get("next_primary_attack_target") == DOMAIN_ENTROPY
        and latest_source.get("actual_source_domain_entropy_proved") is False
    )
    phi_boundary = (
        phi_lpf_source.get("phi_lpf_candidate_capacity_ledger_closed") is True
        and phi_lpf_source.get("candidate_rows_are_actual_signed_rows") is False
    )
    downstream_closed = strict_downstream.get("source_entropy_downstream_edges_closed") is True
    cycle_cut_open = (
        coord_cycle.get("primitive_basis_and_coefficient_source_input_proved") is False
        or strict_downstream.get("primitive_basis_and_coefficient_source_input_proved") is False
    )
    terminal_kernel_synced = terminal_to_kernel.get("next_direct_attack_target") == (
        "AlphaRowAnchorPhaseEmissionFormulaLedger"
    )
    return [
        row(
            "LatestSourceEntropyImported",
            latest_imported,
            False,
            "latest new-payload/source-atom 层已把第一直接硬点压到 source-domain absolute entropy。",
            DOMAIN_ENTROPY,
        ),
        row(
            "PhiLPFBucketCapacityBoundaryCarried",
            phi_boundary,
            True,
            "LPF/Phi 桶恒等式只支付无符号候选容量，不能把候选 row 直接升级成 actual signed source entropy。",
            f"{SIGNED_SURVIVAL} AND {ROW_MASS} AND {SIGNED_EXPR}",
        ),
        row(
            "SourceEntropyAtomSendsToSignedLaw",
            source_entropy.get("next_direct_attack_target") == SIGNED_LAW,
            False,
            "actual source-domain entropy 的首个下游字段是 primitive row signed coefficient law。",
            SIGNED_LAW,
        ),
        row(
            "StrictSourceEntropyDownstreamImported",
            downstream_closed,
            True,
            "strict downstream 已把 source entropy 同步到 signed law、basis source、internal basis 与 basis alphabet。",
            "seed coordinate/source cycle guard",
        ),
        row(
            "SeedCoordinateSourceCycleImported",
            strict_downstream.get("seed_coordinate_source_cycle_detected") is True
            and strict_downstream.get("raw_cycle_counts_as_closure") is False,
            True,
            "basis alphabet 继续展开会落入 signed 坐标-来源闭合依赖环；该环不能作为证明。",
            CYCLE_CUT_INPUT,
        ),
        row(
            "PrimitiveBasisCoefficientCycleCutInputCurrentCorpusProved",
            False,
            False,
            "当前语料仍没有提交同时生成 primitive basis words 与 signed coefficients 的无环源输入。",
            CYCLE_CUT_INPUT,
        ),
        row(
            "TerminalDescentAlternativeStillOpen",
            strict_downstream.get("acyclic_terminal_descent_proved") is False,
            False,
            "若拒绝坐标-来源环，只能回流 terminal family；该分支仍需 well-founded descent 或 canonical-lock。",
            TERMINAL_DESCENT,
        ),
        row(
            "TerminalDescentDownstreamSyncedToKernelTable",
            terminal_kernel_synced,
            False,
            "terminal descent 下游已同步到 pointwise primitive kernel/alpha-row 表，但该路没有闭合。",
            "AlphaRowAnchorPhaseEmissionFormulaLedger",
        ),
        row(
            "CompleteKeyAndFixedKeyStillParallel",
            latest_source.get("complete_primitive_emitter_key_partition_proved") is False
            and latest_source.get("fixed_key_exact_uv_local_multiplicity_proved") is False,
            False,
            "source-rank/no-collapse 包中的 complete key 与 fixed-key ExactUV local multiplicity 仍是独立原子。",
            f"{COMPLETE_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "PointwiseAndExactUVStillAlternative",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
            and exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "若不走 cycle-cut/terminal descent，只能提交逐点 signed table 或独立 ExactUV source/fiber 控制。",
            f"{POINTWISE_TABLE} OR {EXACTUV_PAIR}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 latest source entropy 接到下游环守卫；未证明 cycle-cut、terminal descent、complete/fixed-key、PDEC、ExactUV 或 DStructure。",
            (
                f"(({CYCLE_CUT_INPUT} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}) "
                f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE} "
                f"OR {EXTERNAL_SPECTRAL}) AND {EXACTUV_PAIR} AND {DSTRUCTURE}"
            ),
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 latest source-entropy downstream cycle 同步证书。"""
    latest_source = load_json(LATEST_SOURCE_ATOM_CERT)
    phi_lpf_source = load_json(PHI_LPF_SOURCE_ENTROPY_CERT)
    strict_downstream = load_json(STRICT_DOWNSTREAM_CERT)
    source_entropy = load_json(SOURCE_ENTROPY_CERT)
    coord_cycle = load_json(COORD_CYCLE_CERT)
    terminal_to_kernel = load_json(TERMINAL_TO_KERNEL_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(
        latest_source,
        phi_lpf_source,
        strict_downstream,
        source_entropy,
        coord_cycle,
        terminal_to_kernel,
        pointwise,
        exactuv,
    )
    downstream_edges = imported_downstream_edges(strict_downstream)
    latest_basis = (
        f"(({CYCLE_CUT_INPUT} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}) "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE} "
        f"OR {EXTERNAL_SPECTRAL}) AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_source_entropy_downstream_cycle_sync_router",
        "status": "phi_lpf_latest_source_entropy_synced_to_downstream_cycle_guard_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_source_entropy_imported": rows[0]["closed"],
        "phi_lpf_candidate_capacity_boundary_carried": rows[1]["closed"],
        "candidate_rows_are_actual_signed_rows": False,
        "source_entropy_atom_sends_to_signed_law": rows[2]["closed"],
        "source_entropy_downstream_edges_closed": all(item.get("closed") for item in downstream_edges),
        "seed_coordinate_source_cycle_detected": strict_downstream.get("seed_coordinate_source_cycle_detected") is True,
        "raw_cycle_counts_as_closure": False,
        "primitive_basis_and_coefficient_source_input_proved": False,
        "acyclic_terminal_descent_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": DOMAIN_ENTROPY,
        "support_boundary_from_phi_lpf": support_boundary(phi_lpf_source),
        "largest_capacity_sample": largest_capacity_sample(phi_lpf_source),
        "downstream_edges": downstream_edges,
        "imported_cycle_edges": strict_downstream.get("imported_cycle_edges", []),
        "gates": rows,
        "next_primary_attack_target": f"{CYCLE_CUT_INPUT}_OR_{TERMINAL_DESCENT}",
        "parallel_attack_targets": [
            COMPLETE_KEY,
            FIXED_KEY_MULT,
            PDEC_SCOPE,
            POINTWISE_TABLE,
            EXACTUV_PAIR,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "latest_retained_basis_after_router": latest_basis,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest `ActualPreCauchySourceDomainAbsoluteEntropyLedger` 接到 strict "
            "source entropy downstream cycle guard。LPF/Phi 桶恒等式已经关闭无符号候选容量，"
            "但候选 row 不是 actual signed row，不能支付 signed survival、row-mass 或推前前 "
            "signed coefficient。沿 strict downstream 展开后，source entropy 进入 signed law、"
            "basis source、internal basis 与 basis alphabet，并落入 signed 坐标-来源环；该环不能"
            "作为证明。最新直接主攻变为无环 cycle-cut primitive basis/coefficient source input "
            "或 terminal descent，complete key、fixed-key、PDEC、逐点表、ExactUV、模型、Rate 与 "
            "DStructure 仍开放，行/列命题未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest source-entropy downstream cycle sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_source_entropy_imported={fmt_bool(cert['latest_source_entropy_imported'])}",
        f"phi_lpf_candidate_capacity_boundary_carried={fmt_bool(cert['phi_lpf_candidate_capacity_boundary_carried'])}",
        f"candidate_rows_are_actual_signed_rows={fmt_bool(cert['candidate_rows_are_actual_signed_rows'])}",
        f"source_entropy_atom_sends_to_signed_law={fmt_bool(cert['source_entropy_atom_sends_to_signed_law'])}",
        f"source_entropy_downstream_edges_closed={fmt_bool(cert['source_entropy_downstream_edges_closed'])}",
        f"seed_coordinate_source_cycle_detected={fmt_bool(cert['seed_coordinate_source_cycle_detected'])}",
        f"raw_cycle_counts_as_closure={fmt_bool(cert['raw_cycle_counts_as_closure'])}",
        f"primitive_basis_and_coefficient_source_input_proved={fmt_bool(cert['primitive_basis_and_coefficient_source_input_proved'])}",
        f"acyclic_terminal_descent_proved={fmt_bool(cert['acyclic_terminal_descent_proved'])}",
        f"complete_primitive_emitter_key_partition_proved={fmt_bool(cert['complete_primitive_emitter_key_partition_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_proved={fmt_bool(cert['fixed_key_exact_uv_local_multiplicity_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. LPF/Phi 支撑边界",
        "",
        "| atom | status | role |",
        "| --- | --- | --- |",
    ]
    for item in cert["support_boundary_from_phi_lpf"]:
        lines.append(
            f"| `{cell(item.get('atom', ''))}` | `{cell(item.get('status', ''))}` | "
            f"{cell(item.get('role', ''))} |"
        )
    sample = cert.get("largest_capacity_sample", {})
    if sample:
        lines.extend(
            [
                "",
                "最大样本读数：",
                "",
                "```text",
                (
                    f"N={sample.get('N')} candidate_rows={sample.get('phi_lpf_candidate_rows')} "
                    f"composites={sample.get('composite_count')} primes={sample.get('prime_count')} "
                    f"pi_from_phi={sample.get('pi_from_phi')}"
                ),
                "```",
            ]
        )
    lines.extend(
        [
            "",
            "## 2. 下游同步链",
            "",
            "| from | to | closed | meaning |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in cert["downstream_edges"]:
        lines.append(
            f"| `{cell(item.get('from', ''))}` | `{cell(item.get('to', ''))}` | "
            f"`{fmt_bool(item.get('closed'))}` | {cell(item.get('meaning', ''))} |"
        )
    lines.extend(
        [
            "",
            "## 3. 导入的坐标-来源环",
            "",
            "| node | next | edge matches |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["imported_cycle_edges"]:
        lines.append(
            f"| `{cell(item.get('node', ''))}` | `{cell(item.get('actual_next', ''))}` | "
            f"`{fmt_bool(item.get('edge_matches'))}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "并行出口：",
            "",
            "```text",
            "\n".join(cert["parallel_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
