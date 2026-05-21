#!/usr/bin/env python3
"""生成当前 latest built-in pairing 到 branch-trace 出口的桥接同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_builtin_pairing_trace_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-builtin-pairing-trace-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-builtin-pairing-trace-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-builtin-pairing-trace-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-builtin-pairing-trace-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-builtin-pairing-trace-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_BUILTIN = DOCS / (
    "prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-router.json"
)
BUILTIN_TRACE_SYNC = DOCS / "prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json"
STRICT_BUILTIN_FRONTIER = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
GLOBAL_BRANCH_TRACE = DOCS / "prime-matrix-global-crt-branch-trace-frontier-router.json"
SIGNED_LANE_CYCLE = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
FIXED_PAIR_FIBER = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json"
SOURCE_ENTROPY_ATOM = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"

BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
BRANCH_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
NEW_TRACE = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失依赖不能算证明。"""
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


def dependency_paths() -> list[Path]:
    """返回本层依赖证书。"""
    return [
        CURRENT_BUILTIN,
        BUILTIN_TRACE_SYNC,
        STRICT_BUILTIN_FRONTIER,
        GLOBAL_BRANCH_TRACE,
        SIGNED_LANE_CYCLE,
        FIXED_PAIR_FIBER,
        SOURCE_ENTROPY_ATOM,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def exactuv_pair() -> str:
    """返回 ExactUV 并行对。"""
    return f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"


def open_basis() -> str:
    """返回本层之后的开放基。"""
    return (
        f"({NEW_TRACE} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}) AND {SOURCE_ENTROPY} "
        f"AND {FIXED_FIBER} AND {REGISTERED_KEY} AND {FIXED_KEY} AND {MODEL} "
        f"AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(
    current: dict[str, Any],
    trace: dict[str, Any],
    strict_builtin: dict[str, Any],
    global_trace: dict[str, Any],
    signed_cycle: dict[str, Any],
    fixed_fiber: dict[str, Any],
    source_entropy: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成桥接同步判定表。"""
    return [
        row(
            "CurrentLatestBuiltInPairingImported",
            current.get("next_primary_attack_target") == BUILTIN_PAIRING,
            False,
            "当前 latest new-joint/antisplit 下游已经把直接 signed 主攻压到 built-in pairing。",
            BUILTIN_PAIRING,
        ),
        row(
            "LegacyBuiltInTraceRouterSameTarget",
            trace.get("target_input_before_router") == BUILTIN_PAIRING
            and trace.get("latest_builtin_pairing_imported") is True,
            True,
            "既有 latest built-in trace 同步证书的输入目标与当前目标相同，可作为下游桥接证据。",
            BUILTIN_PAIRING,
        ),
        row(
            "StrictBuiltInFrontierImported",
            strict_builtin.get("next_direct_attack_target") == BRANCH_TRACE
            and trace.get("strict_builtin_pairing_frontier_imported") is True,
            True,
            "strict built-in frontier 将内置 signed pairing 压到 exact atomic branch trace。",
            BRANCH_TRACE,
        ),
        row(
            "OddSignedDataBoundaryImported",
            trace.get("odd_signed_data_not_generated_by_phi_lpf_buckets") is True
            and strict_builtin.get("old_signed_value_route_circular") is True,
            True,
            "LPF/Phi unsigned bucket 与旧 signed-value/origin-table 路线不能生成取向/local factor 奇数据。",
            BRANCH_TRACE,
        ),
        row(
            "GlobalBranchTraceFrontierAligned",
            global_trace.get("builtin_pairing_reduced_to_exact_branch_trace") is True,
            False,
            "global CRT 前沿同样把 new-joint/built-in pairing 侧压到 same-set PDEC 或 exact branch trace。",
            f"{PDEC_SCOPE} OR {BRANCH_TRACE}",
        ),
        row(
            "SignedLaneCycleImported",
            signed_cycle.get("aggregate", {}).get("signed_lane_cycle_closed") is True
            and signed_cycle.get("aggregate", {}).get("signed_lane_self_proof_eliminated") is True,
            True,
            "common packet、built-in pairing、branch trace、signed payload、origin identity 已形成自证环。",
            "cycle is diagnostic, not proof",
        ),
        row(
            "BranchTraceSelfProofRejected",
            trace.get("branch_trace_self_proof_rejected") is True
            and trace.get("new_primitive_payload_or_trace_artifact_present") is False,
            True,
            "branch trace 不能由环内 payload/origin/common packet 自证；必须新增 primitive trace/payload 或走受控出口。",
            f"{NEW_TRACE} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
        ),
        row(
            "NewPrimitivePayloadOrTraceCurrentCorpusProved",
            False,
            False,
            "当前语料没有提交新 primitive atomic signed payload 或 trace formula 工件。",
            NEW_TRACE,
        ),
        row(
            "ExactUVEntropyFiberPairCarried",
            current.get("parallel_primary_attack_target") == exactuv_pair()
            and trace.get("exactuv_entropy_fiber_pair_imported") is True,
            False,
            "当前并行 ExactUV 门与既有 trace 同步保持同一个 source entropy/fixed fiber 合取。",
            exactuv_pair(),
        ),
        row(
            "SourceEntropyStillSignedRowLaw",
            source_entropy.get("next_direct_attack_target")
            == "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward",
            False,
            "actual source-domain entropy 仍下钻到 signed row law、row-mass normalization 与 row support。",
            SOURCE_ENTROPY,
        ),
        row(
            "FixedPairFiberAtomized",
            fixed_fiber.get("terminal_gap_after_router") == f"{REGISTERED_KEY} AND {FIXED_KEY}",
            False,
            "fixed-pair fiber 已原子化为 complete key polylog 分区与 fixed-key O(1) 局部重数。",
            f"{REGISTERED_KEY} AND {FIXED_KEY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把当前 latest built-in pairing 接到 branch-trace/闭环出口；没有得到无条件闭合。",
            open_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    current = load_json(CURRENT_BUILTIN)
    trace = load_json(BUILTIN_TRACE_SYNC)
    strict_builtin = load_json(STRICT_BUILTIN_FRONTIER)
    global_trace = load_json(GLOBAL_BRANCH_TRACE)
    signed_cycle = load_json(SIGNED_LANE_CYCLE)
    fixed_fiber = load_json(FIXED_PAIR_FIBER)
    source_entropy = load_json(SOURCE_ENTROPY_ATOM)
    rows = build_rows(current, trace, strict_builtin, global_trace, signed_cycle, fixed_fiber, source_entropy)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_builtin_pairing_trace_sync_router",
        "status": "phi_lpf_latest_current_builtin_pairing_synced_to_branch_trace_cycle_exit_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "current_latest_builtin_pairing_imported": rows[0]["closed"],
        "legacy_builtin_trace_router_same_target": rows[1]["closed"],
        "strict_builtin_frontier_imported": rows[2]["closed"],
        "odd_signed_data_boundary_imported": rows[3]["closed"],
        "global_branch_trace_frontier_aligned": rows[4]["closed"],
        "signed_lane_cycle_imported": rows[5]["closed"],
        "branch_trace_self_proof_rejected": rows[6]["closed"],
        "new_primitive_payload_or_trace_artifact_present": False,
        "exactuv_entropy_fiber_pair_carried": rows[8]["closed"],
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "row_column_unconditional_closed": False,
        "intermediate_primary_attack_target": BRANCH_TRACE,
        "next_primary_attack_target": NEW_TRACE,
        "controlled_exit_targets": [TERMINAL_DESCENT, PDEC_SCOPE],
        "parallel_primary_attack_target": exactuv_pair(),
        "latest_noncycle_basis_after_sync": open_basis(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把当前 latest `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` "
            "桥接到既有 built-in pairing/branch-trace 同步证书。内置 signed pairing 的直接前沿是 "
            "`ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`；但该 trace 若沿现有 "
            "signed payload/origin/common packet 子线展开，会回到 signed-lane 自证环。因此最新非循环"
            "主硬点变成 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact`，或受控出口 "
            "`AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate`、"
            "`AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate`。并行 ExactUV 门仍是 "
            "`ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger`，"
            "其中 fixed fiber 已原子化为 complete key 与 fixed-key 局部重数。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF latest current built-in pairing to branch trace sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"current_latest_builtin_pairing_imported={fmt_bool(result['current_latest_builtin_pairing_imported'])}",
        f"legacy_builtin_trace_router_same_target={fmt_bool(result['legacy_builtin_trace_router_same_target'])}",
        f"strict_builtin_frontier_imported={fmt_bool(result['strict_builtin_frontier_imported'])}",
        f"odd_signed_data_boundary_imported={fmt_bool(result['odd_signed_data_boundary_imported'])}",
        f"global_branch_trace_frontier_aligned={fmt_bool(result['global_branch_trace_frontier_aligned'])}",
        f"signed_lane_cycle_imported={fmt_bool(result['signed_lane_cycle_imported'])}",
        f"branch_trace_self_proof_rejected={fmt_bool(result['branch_trace_self_proof_rejected'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(result['new_primitive_payload_or_trace_artifact_present'])}",
        f"exactuv_entropy_fiber_pair_carried={fmt_bool(result['exactuv_entropy_fiber_pair_carried'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"intermediate_primary_attack_target={result['intermediate_primary_attack_target']}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        f"parallel_primary_attack_target={result['parallel_primary_attack_target']}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 最新开放基",
            "",
            "```text",
            result["latest_noncycle_basis_after_sync"],
            "```",
            "",
            "受控出口：",
            "",
            "```text",
            "\n".join(result["controlled_exit_targets"]),
            "```",
            "",
            "## 3. 边界",
            "",
            "- 本层是桥接同步，不重新证明 branch trace 下游。",
            "- LPF/Phi 桶恒等式仍不生成 signed coefficient 或 trace 奇数据。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 和 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_primary_attack_target={result['next_primary_attack_target']}")
    print(f"parallel_primary_attack_target={result['parallel_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
