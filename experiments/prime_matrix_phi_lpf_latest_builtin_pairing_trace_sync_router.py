#!/usr/bin/env python3
"""生成 Phi-LPF latest built-in pairing/branch-trace 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_builtin_pairing_trace_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_ANTISPLIT = DOCS / "prime-matrix-phi-lpf-latest-antisplit-downstream-sync-router.json"
BUILTIN_FRONTIER = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
GLOBAL_BRANCH_TRACE = DOCS / "prime-matrix-global-crt-branch-trace-frontier-router.json"
SIGNED_LANE_CYCLE = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
INCIDENCE_ENTROPY = DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"
FIXED_PAIR_FIBER = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json"
SOURCE_ENTROPY_ATOM = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"

BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
BRANCH_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SIGNED_PAYLOAD = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
ORIGIN_IDENTITY = "NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
EXACTUV_PAIR = f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能作为证明。"""
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
    """登记本层依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_ANTISPLIT,
        BUILTIN_FRONTIER,
        GLOBAL_BRANCH_TRACE,
        SIGNED_LANE_CYCLE,
        INCIDENCE_ENTROPY,
        FIXED_PAIR_FIBER,
        SOURCE_ENTROPY_ATOM,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出本层从 latest built-in pairing 到非循环出口的同步链。"""
    return [
        {
            "from": BUILTIN_PAIRING,
            "to": BRANCH_TRACE,
            "meaning": "strict built-in pairing 证书要求在 Cauchy/Phi/payment 前给出 exact atomic branch trace。",
        },
        {
            "from": BRANCH_TRACE,
            "to": SIGNED_PAYLOAD,
            "meaning": "branch trace 若只沿现有 signed 子线展开，会进入 signed payload constructor。",
        },
        {
            "from": SIGNED_PAYLOAD,
            "to": ORIGIN_IDENTITY,
            "meaning": "signed payload 的来源恒等式继续回到 atomic basis word/signed coefficient origin。",
        },
        {
            "from": ORIGIN_IDENTITY,
            "to": COMMON_PACKET,
            "meaning": "origin identity 与 ExactUV 子线共同回到 common source declaration packet。",
        },
        {
            "from": COMMON_PACKET,
            "to": BUILTIN_PAIRING,
            "meaning": "common packet 的 signed 子线又同步回 built-in pairing，形成闭环。",
        },
        {
            "from": BRANCH_TRACE,
            "to": f"{NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
            "meaning": "排除环内自证后，只能提交新 primitive trace/payload、证明 terminal descent，或走 same-set PDEC。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    builtin: dict[str, Any],
    global_trace: dict[str, Any],
    signed_cycle: dict[str, Any],
    incidence: dict[str, Any],
    fixed_fiber: dict[str, Any],
    source_entropy: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest built-in pairing/trace 同步判定表。"""
    latest_imported = latest.get("next_primary_attack_target") == BUILTIN_PAIRING
    builtin_to_trace = builtin.get("next_direct_attack_target") == BRANCH_TRACE
    global_trace_aligned = (
        global_trace.get("builtin_pairing_reduced_to_exact_branch_trace") is True
        and BRANCH_TRACE in str(global_trace.get("latest_strict_activity_basis", ""))
    )
    signed_cycle_closed = (
        signed_cycle.get("signed_lane_cycle_closed") is True
        and signed_cycle.get("signed_lane_self_proof_eliminated") is True
    )
    exactuv_pair_imported = (
        latest.get("parallel_primary_attack_target") == EXACTUV_PAIR
        and incidence.get("next_direct_attack_target") == EXACTUV_PAIR
    )
    fixed_fiber_atomized = fixed_fiber.get("terminal_gap_after_router") == (
        f"{REGISTERED_KEY} AND {FIXED_KEY_MULT}"
    )
    source_entropy_downstream = source_entropy.get("next_direct_attack_target") == (
        "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
    )
    return [
        row(
            "LatestBuiltInPairingImported",
            latest_imported,
            False,
            "latest antisplit downstream 已把 signed 主硬点压到 built-in signed coefficient/pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "StrictBuiltInPairingFrontierImported",
            builtin_to_trace,
            True,
            "strict built-in pairing 前沿已说明内置闭式必须由 exact atomic branch trace 给出。",
            BRANCH_TRACE,
        ),
        row(
            "OddSignedDataNotGeneratedByPhiLPFBuckets",
            builtin.get("builtin_signed_coefficient_pairing_proved") is False
            and latest.get("built_in_signed_pairing_proved") is False,
            True,
            "LPF/Phi 桶与 unsigned skeleton 只给支撑和容量；signed coefficient 的取向/local factor 奇数据仍未生成。",
            BRANCH_TRACE,
        ),
        row(
            "GlobalBranchTraceFrontierAligned",
            global_trace_aligned,
            False,
            "global CRT 前沿同样把 new joint/built-in pairing 分支压到 PDEC scope 或 exact branch trace。",
            f"{PDEC_SCOPE} OR {BRANCH_TRACE}",
        ),
        row(
            "ExactBranchTraceCurrentCorpusProved",
            False,
            False,
            "当前语料没有提交每条 atomic joint row 的 exact branch trace signed coefficient 公式。",
            BRANCH_TRACE,
        ),
        row(
            "SignedLaneCycleImported",
            signed_cycle_closed,
            True,
            "existing signed/payload 子线已形成 common packet -> built-in pairing -> branch trace -> payload -> origin -> common packet 的闭环。",
            "cycle is diagnostic, not proof",
        ),
        row(
            "BranchTraceSelfProofRejected",
            signed_cycle.get("next_direct_attack_target") == NEW_PAYLOAD
            and signed_cycle_closed,
            True,
            "branch trace 不能用环内 payload/origin/common packet 自证；必须新增 primitive trace/payload 或走受控出口。",
            f"{NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
        ),
        row(
            "NewPrimitivePayloadOrTraceCurrentCorpusProved",
            False,
            False,
            "当前语料没有新增 primitive atomic signed payload 或 trace formula 工件。",
            NEW_PAYLOAD,
        ),
        row(
            "ExactUVEntropyFiberPairImported",
            exactuv_pair_imported,
            False,
            "latest antisplit 的 ExactUV 并行门与 strict incidence entropy split 是同一个 source entropy/fixed-fiber 合取。",
            EXACTUV_PAIR,
        ),
        row(
            "ActualSourceEntropyStillOpen",
            incidence.get("actual_emitter_source_domain_entropy_proved") is False
            and source_entropy_downstream,
            False,
            "actual source-domain entropy 继续下钻到 primitive row signed coefficient law，不能由 branch trace 同步自动得到。",
            SOURCE_ENTROPY,
        ),
        row(
            "FixedPairFiberAtomizedButOpen",
            fixed_fiber_atomized
            and fixed_fiber.get("exact_uv_map_fixed_pair_polylog_fiber_bound_proved") is False,
            False,
            "fixed-pair fiber bound 已被原子化为 complete key polylog 分区与 fixed-key O(1) 局部重数，但二者未证。",
            f"{REGISTERED_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 latest built-in pairing 到 branch-trace/闭环出口；未证明三命题无条件闭合。",
            f"({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}) AND {EXACTUV_PAIR}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 latest built-in pairing/trace 同步证书。"""
    latest = load_json(LATEST_ANTISPLIT)
    builtin = load_json(BUILTIN_FRONTIER)
    global_trace = load_json(GLOBAL_BRANCH_TRACE)
    signed_cycle = load_json(SIGNED_LANE_CYCLE)
    incidence = load_json(INCIDENCE_ENTROPY)
    fixed_fiber = load_json(FIXED_PAIR_FIBER)
    source_entropy = load_json(SOURCE_ENTROPY_ATOM)
    rows = build_rows(
        latest=latest,
        builtin=builtin,
        global_trace=global_trace,
        signed_cycle=signed_cycle,
        incidence=incidence,
        fixed_fiber=fixed_fiber,
        source_entropy=source_entropy,
    )
    latest_trace_basis = f"({BRANCH_TRACE} OR {PDEC_SCOPE}) AND {EXACTUV_PAIR}"
    latest_noncycle_basis = (
        f"({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}) AND {EXACTUV_PAIR}"
    )
    retained_basis = (
        f"(({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}) AND {SOURCE_ENTROPY} "
        f"AND {FIXED_FIBER}) OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {EXTERNAL_DIBFI}"
    )
    retained_basis = (
        f"({retained_basis}) AND {REGISTERED_KEY} AND {FIXED_KEY_MULT} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_builtin_pairing_trace_sync_router",
        "status": "phi_lpf_latest_builtin_pairing_synced_to_branch_trace_cycle_exit_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_builtin_pairing_imported": rows[0]["closed"],
        "strict_builtin_pairing_frontier_imported": rows[1]["closed"],
        "odd_signed_data_not_generated_by_phi_lpf_buckets": rows[2]["closed"],
        "global_branch_trace_frontier_aligned": rows[3]["closed"],
        "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved": False,
        "signed_lane_cycle_imported": rows[5]["closed"],
        "branch_trace_self_proof_rejected": rows[6]["closed"],
        "new_primitive_payload_or_trace_artifact_present": False,
        "exactuv_entropy_fiber_pair_imported": rows[8]["closed"],
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": BUILTIN_PAIRING,
        "intermediate_primary_attack_target": BRANCH_TRACE,
        "next_primary_attack_target": NEW_PAYLOAD,
        "parallel_primary_attack_targets": [
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            EXACTUV_PAIR,
            REGISTERED_KEY,
            FIXED_KEY_MULT,
        ],
        "latest_trace_basis_before_cycle_guard": latest_trace_basis,
        "latest_noncycle_basis_after_router": latest_noncycle_basis,
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` "
            "接到 strict built-in pairing 前沿。LPF/Phi 桶和 unsigned skeleton 仍只支付支撑、容量、"
            "相位与 row 形状；signed coefficient 的取向/local factor 奇数据必须由 "
            f"`{BRANCH_TRACE}` 正向给出。但该 branch trace 若沿当前 signed/payload 子线展开，"
            "会回到 common source packet，形成自证环；因此最新非循环主硬点不是环内节点，"
            f"而是 `{NEW_PAYLOAD}`，或受控出口 `{TERMINAL_DESCENT}`、`{PDEC_SCOPE}`。"
            f"并行 ExactUV 门仍是 `{EXACTUV_PAIR}`，其中 fixed-pair fiber 又下钻为 "
            f"`{REGISTERED_KEY}` 与 `{FIXED_KEY_MULT}`。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF latest built-in pairing trace-sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_builtin_pairing_imported={fmt_bool(cert['latest_builtin_pairing_imported'])}",
        f"strict_builtin_pairing_frontier_imported={fmt_bool(cert['strict_builtin_pairing_frontier_imported'])}",
        f"odd_signed_data_not_generated_by_phi_lpf_buckets={fmt_bool(cert['odd_signed_data_not_generated_by_phi_lpf_buckets'])}",
        f"global_branch_trace_frontier_aligned={fmt_bool(cert['global_branch_trace_frontier_aligned'])}",
        "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved="
        f"{fmt_bool(cert['exact_atomic_joint_branch_trace_signed_coefficient_formula_proved'])}",
        f"signed_lane_cycle_imported={fmt_bool(cert['signed_lane_cycle_imported'])}",
        f"branch_trace_self_proof_rejected={fmt_bool(cert['branch_trace_self_proof_rejected'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(cert['new_primitive_payload_or_trace_artifact_present'])}",
        f"exactuv_entropy_fiber_pair_imported={fmt_bool(cert['exactuv_entropy_fiber_pair_imported'])}",
        f"actual_emitter_source_domain_entropy_proved={fmt_bool(cert['actual_emitter_source_domain_entropy_proved'])}",
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved="
        f"{fmt_bool(cert['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        "registered_complete_primitive_emitter_key_partition_polylog_proved="
        f"{fmt_bool(cert['registered_complete_primitive_emitter_key_partition_polylog_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_o1_proved={fmt_bool(cert['fixed_key_exact_uv_local_multiplicity_o1_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"intermediate_primary_attack_target={cert['intermediate_primary_attack_target']}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
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
            "## 3. cycle guard 前 trace 基",
            "",
            "```text",
            cert["latest_trace_basis_before_cycle_guard"],
            "```",
            "",
            "## 4. cycle guard 后非循环基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 5. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
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
