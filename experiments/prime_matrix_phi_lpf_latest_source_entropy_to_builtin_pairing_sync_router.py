#!/usr/bin/env python3
"""生成 Phi-LPF latest source-entropy 到 built-in pairing 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_source_entropy_to_builtin_pairing_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_ORIENTATION_SOURCE_RANK = (
    DOCS / "prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync-router.json"
)
SOURCE_ENTROPY_DOWNSTREAM = (
    DOCS / "prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync-router.json"
)
CYCLECUT_TERMINAL_UNIFIED = (
    DOCS / "prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync-router.json"
)
ANTISPLIT_DOWNSTREAM = DOCS / "prime-matrix-phi-lpf-latest-antisplit-downstream-sync-router.json"
BUILTIN_TRACE_SYNC = DOCS / "prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json"
TRACE_EXIT_SOURCE_RANK = (
    DOCS / "prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json"
)

SOURCE_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
ATOMIC_ROWS = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
EMITTER_SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
EXACTUV_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
NEW_PRIMITIVE = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作闭合。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值写成小写文本。"""
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


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    paths = [
        LATEST_ORIENTATION_SOURCE_RANK,
        SOURCE_ENTROPY_DOWNSTREAM,
        CYCLECUT_TERMINAL_UNIFIED,
        ANTISPLIT_DOWNSTREAM,
        BUILTIN_TRACE_SYNC,
        TRACE_EXIT_SOURCE_RANK,
    ]
    return [str(path.relative_to(ROOT)) for path in paths if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希，便于审计。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_ORIENTATION_SOURCE_RANK,
        SOURCE_ENTROPY_DOWNSTREAM,
        CYCLECUT_TERMINAL_UNIFIED,
        ANTISPLIT_DOWNSTREAM,
        BUILTIN_TRACE_SYNC,
        TRACE_EXIT_SOURCE_RANK,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def exactuv_pair() -> str:
    """返回 ExactUV 并行门。"""
    return f"{EMITTER_SOURCE_ENTROPY} AND {EXACTUV_FIBER}"


def retained_basis() -> str:
    """返回本层之后仍需保留的完整基。"""
    return (
        f"(({BUILTIN_PAIRING} AND {exactuv_pair()}) OR {CANONICAL_LOCK} OR "
        f"{INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) AND "
        f"{COMPLETE_KEY} AND {FIXED_KEY_MULT} AND {MODEL_GAP} AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(deps: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成最新 source-entropy 到 built-in pairing 的同步判定表。"""
    latest = deps["latest"]
    source_downstream = deps["source_downstream"]
    cyclecut = deps["cyclecut"]
    antisplit = deps["antisplit"]
    builtin_trace = deps["builtin_trace"]
    trace_exit = deps["trace_exit"]
    cycle_or_terminal = f"{CYCLE_CUT}_OR_{TERMINAL_DESCENT}"

    return [
        row(
            "LatestOrientationSourceEntropyImported",
            latest.get("next_direct_attack_target") == SOURCE_ENTROPY
            and latest.get("actual_source_domain_entropy_proved") is False,
            False,
            "最新 orientation/trace/payload/source-rank 同步层把直接主攻压到 actual pre-Cauchy source entropy。",
            SOURCE_ENTROPY,
        ),
        row(
            "SourceEntropyDownstreamCycleImported",
            source_downstream.get("next_primary_attack_target") == cycle_or_terminal
            and source_downstream.get("source_entropy_downstream_edges_closed") is True,
            True,
            "source entropy 下游边已登记：signed law、basis source、internal basis 与 basis alphabet 会回到 seed coordinate/source 环。",
            f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
        ),
        row(
            "SourceEntropyRawCycleRejected",
            source_downstream.get("seed_coordinate_source_cycle_detected") is True
            and source_downstream.get("raw_cycle_counts_as_closure") is False,
            True,
            "basis alphabet 的返回环只能删除自证路线，不能证明 source entropy。",
            f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
        ),
        row(
            "CycleCutTerminalUnifiedImported",
            cyclecut.get("next_primary_attack_target") == JOINT_DECL
            and cyclecut.get("strict_unified_frontier_imported") is True,
            True,
            "cycle-cut/terminal/PDEC 统一前沿已把二选一出口同步到 pre-Cauchy joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "TerminalAndPDECStillNotInternalClosure",
            cyclecut.get("terminal_descent_macrocycle_detected") is True
            and cyclecut.get("pdec_scope_internal_saturation_imported") is True,
            False,
            "terminal descent 在当前语料中是宏循环；same-set PDEC 内部分支也不能提供自足闭合。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}",
        ),
        row(
            "AntisplitDownstreamImported",
            antisplit.get("next_primary_attack_target") == BUILTIN_PAIRING
            and antisplit.get("strict_antisplit_downstream_imported") is True,
            True,
            "普通 joint declaration 会回到 constructor 固定点；非循环内部路线必须走 atomic antisplit rows。",
            ATOMIC_ROWS,
        ),
        row(
            "AtomicRowsReducedToBuiltInPairing",
            antisplit.get("atomic_rows_reduced_to_builtin_pairing") is True,
            False,
            "atomic joint rows 的 signed 首缺口是每条 row 的内置 signed coefficient/pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberParallelImported",
            antisplit.get("parallel_primary_attack_target") == exactuv_pair()
            and antisplit.get("exactuv_entropy_fiber_split_imported") is True,
            False,
            "ExactUV 并行门仍是 actual emitter source-domain entropy 与 fixed exact-pair polylog fiber bound。",
            exactuv_pair(),
        ),
        row(
            "BuiltInPairingTraceCycleCarried",
            builtin_trace.get("next_primary_attack_target") == NEW_PRIMITIVE
            and builtin_trace.get("branch_trace_self_proof_rejected") is True,
            True,
            "若继续用 existing branch trace 解释 built-in pairing，会回到 signed payload/source packet 环；这只删除 trace 自证。",
            NEW_PRIMITIVE,
        ),
        row(
            "TraceExitSourceRankConvergenceCarried",
            trace_exit.get("next_primary_attack_target") == ALPHA_ANCHOR
            and trace_exit.get("post_antisplit_convergence_imported") is True,
            False,
            "new payload/trace 出口已知会重新要求 source-rank/no-collapse 与 pointwise kernel；这说明本层只是把最新入口接回该链。",
            ALPHA_ANCHOR,
        ),
        row(
            "BuiltInSignedPairingCurrentCorpusProved",
            False,
            False,
            "当前没有给出 atomic joint row 的 signed coefficient/pairing 闭式或同源发射公式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberCurrentCorpusProved",
            False,
            False,
            "ExactUV source entropy 与 fixed-pair fiber bound 仍不能由 LPF/Phi 无符号桶或 built-in pairing 名称推出。",
            exactuv_pair(),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只完成最新 source entropy 入口到 built-in pairing/ExactUV 并行门的同步；没有关闭行/列命题。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    deps = {
        "latest": load_json(LATEST_ORIENTATION_SOURCE_RANK),
        "source_downstream": load_json(SOURCE_ENTROPY_DOWNSTREAM),
        "cyclecut": load_json(CYCLECUT_TERMINAL_UNIFIED),
        "antisplit": load_json(ANTISPLIT_DOWNSTREAM),
        "builtin_trace": load_json(BUILTIN_TRACE_SYNC),
        "trace_exit": load_json(TRACE_EXIT_SOURCE_RANK),
    }
    rows = build_rows(deps)
    sync_chain = [
        {
            "from": SOURCE_ENTROPY,
            "to": f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
            "meaning": "source entropy 下游展开回到 seed coordinate/source 环；非循环路线必须切环或走 terminal。",
        },
        {
            "from": f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
            "to": JOINT_DECL,
            "meaning": "cycle-cut/terminal/PDEC 统一前沿把生产性内部字段压到 joint declaration line。",
        },
        {
            "from": JOINT_DECL,
            "to": ATOMIC_ROWS,
            "meaning": "普通 constructor 路线是 fixed point；要非循环必须走 atomic antisplit rows。",
        },
        {
            "from": ATOMIC_ROWS,
            "to": BUILTIN_PAIRING,
            "meaning": "atomic rows 的 signed 首缺口是内置 word/coefficient pairing 闭式。",
        },
        {
            "from": "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem",
            "to": exactuv_pair(),
            "meaning": "ExactUV bounded incidence 并行拆成 source entropy 与 fixed-pair fiber bound。",
        },
    ]
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_source_entropy_to_builtin_pairing_sync_router",
        "status": "phi_lpf_latest_source_entropy_synced_to_builtin_pairing_and_exactuv_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_lpf_phi_identity_used_as_unsigned_support_only": True,
        "latest_source_entropy_imported": rows[0]["closed"],
        "source_entropy_downstream_cycle_imported": rows[1]["closed"],
        "source_entropy_raw_cycle_rejected": rows[2]["closed"],
        "cycle_cut_terminal_unified_imported": rows[3]["closed"],
        "terminal_and_pdec_not_internal_closure": rows[4]["closed"],
        "antisplit_downstream_imported": rows[5]["closed"],
        "ordinary_joint_declaration_route_rejected_as_fixed_point": rows[5]["closed"],
        "atomic_rows_reduced_to_builtin_pairing": rows[6]["closed"],
        "exactuv_entropy_fiber_split_imported": rows[7]["closed"],
        "builtin_pairing_trace_cycle_carried": rows[8]["closed"],
        "trace_exit_source_rank_convergence_carried": rows[9]["closed"],
        "built_in_signed_pairing_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SOURCE_ENTROPY,
        "next_primary_attack_target": BUILTIN_PAIRING,
        "parallel_primary_attack_target": exactuv_pair(),
        "retained_basis_after_router": retained_basis(),
        "sync_chain": sync_chain,
        "gates": rows,
        "missing_sources": missing_sources(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步把最新 `{SOURCE_ENTROPY}` 入口接入已有 source-entropy downstream、"
            "cycle-cut/terminal unified 与 antisplit downstream 三段证书。LPF/Phi 桶恒等式已经固定"
            "无符号支撑和容量，但 source entropy 的 signed 下游不能靠坐标-来源环自证；"
            f"cycle-cut/terminal/PDEC 统一后，普通 joint constructor 仍是固定点，生产性内部路线必须走 `{ATOMIC_ROWS}`。"
            f"因此最新 signed 主攻同步为 `{BUILTIN_PAIRING}`，ExactUV 并行主攻为 `{exactuv_pair()}`。"
            "built-in pairing、ExactUV entropy/fiber、complete/fixed-key、terminal/PDEC/外部谱、模型、Rate "
            "与 DStructure 仍开放；行/列命题未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest source-entropy to built-in pairing sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_source_entropy_imported={fmt_bool(cert['latest_source_entropy_imported'])}",
        f"source_entropy_downstream_cycle_imported={fmt_bool(cert['source_entropy_downstream_cycle_imported'])}",
        f"source_entropy_raw_cycle_rejected={fmt_bool(cert['source_entropy_raw_cycle_rejected'])}",
        f"cycle_cut_terminal_unified_imported={fmt_bool(cert['cycle_cut_terminal_unified_imported'])}",
        f"terminal_and_pdec_not_internal_closure={fmt_bool(cert['terminal_and_pdec_not_internal_closure'])}",
        f"antisplit_downstream_imported={fmt_bool(cert['antisplit_downstream_imported'])}",
        f"ordinary_joint_declaration_route_rejected_as_fixed_point={fmt_bool(cert['ordinary_joint_declaration_route_rejected_as_fixed_point'])}",
        f"atomic_rows_reduced_to_builtin_pairing={fmt_bool(cert['atomic_rows_reduced_to_builtin_pairing'])}",
        f"exactuv_entropy_fiber_split_imported={fmt_bool(cert['exactuv_entropy_fiber_split_imported'])}",
        f"builtin_pairing_trace_cycle_carried={fmt_bool(cert['builtin_pairing_trace_cycle_carried'])}",
        f"trace_exit_source_rank_convergence_carried={fmt_bool(cert['trace_exit_source_rank_convergence_carried'])}",
        f"built_in_signed_pairing_proved={fmt_bool(cert['built_in_signed_pairing_proved'])}",
        f"actual_emitter_source_domain_entropy_proved={fmt_bool(cert['actual_emitter_source_domain_entropy_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(cert['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        f"parallel_primary_attack_target={cert['parallel_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 最新保留基",
            "",
            "```text",
            cert["retained_basis_after_router"],
            "```",
            "",
            "下一主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行主攻：",
            "",
            "```text",
            cert["parallel_primary_attack_target"],
            "```",
            "",
            "## 4. 结论边界",
            "",
            "- 本层是最新 source entropy 入口的前沿同步，不是 built-in pairing 证明。",
            "- LPF/Phi 桶恒等式只封闭无符号 ownership、support 和 capacity；signed coefficient 仍需正向发射。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    if cert["missing_sources"]:
        lines.extend(["", "缺失依赖：", ""])
        for path in cert["missing_sources"]:
            lines.append(f"- `{path}`")
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
