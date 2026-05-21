#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor built-in pairing 到 trace 出口的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_builtin_trace_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_BUILTIN = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-antisplit-downstream-sync-router.json"
GENERIC_BUILTIN_TRACE = DOCS / "prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json"
STRICT_BUILTIN = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
STRICT_BRANCH_PAYLOAD = DOCS / "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json"
SIGNED_LANE_CYCLE = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
FIXED_PAIR_FIBER = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json"
SOURCE_ENTROPY = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"

BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
BRANCH_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SIGNED_PAYLOAD = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SOURCE_ENTROPY_TARGET = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER_TARGET = "ExactUVMapFixedPairPolylogFiberBoundLedger"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖哈希。"""
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


def exactuv_pair() -> str:
    """返回 ExactUV 并行对。"""
    return f"{SOURCE_ENTROPY_TARGET} AND {FIXED_FIBER_TARGET}"


def dependency_paths() -> list[Path]:
    """列出本层依赖。"""
    return [
        LATEST_BUILTIN,
        GENERIC_BUILTIN_TRACE,
        STRICT_BUILTIN,
        STRICT_BRANCH_PAYLOAD,
        SIGNED_LANE_CYCLE,
        FIXED_PAIR_FIBER,
        SOURCE_ENTROPY,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """给出同步链。"""
    return [
        {
            "from": BUILTIN_PAIRING,
            "to": BRANCH_TRACE,
            "meaning": "strict built-in pairing 前沿要求 exact atomic branch trace 正向给出 signed coefficient。",
        },
        {
            "from": BRANCH_TRACE,
            "to": SIGNED_PAYLOAD,
            "meaning": "branch trace 的现有下游先进入 signed payload constructor。",
        },
        {
            "from": SIGNED_PAYLOAD,
            "to": "signed-lane cycle",
            "meaning": "payload/origin/common packet 子线已登记为 built-in pairing 自证环。",
        },
        {
            "from": "signed-lane cycle removed",
            "to": f"{NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
            "meaning": "删除环内自证后，只剩新 primitive payload/trace 或受控 terminal/PDEC 出口。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    generic: dict[str, Any],
    strict_builtin: dict[str, Any],
    branch_payload: dict[str, Any],
    signed_cycle: dict[str, Any],
    fixed_fiber: dict[str, Any],
    source_entropy: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "LatestConstructorBuiltInPairingImported",
            latest.get("next_primary_attack_target") == BUILTIN_PAIRING
            and latest.get("built_in_signed_pairing_proved") is False,
            False,
            "上一层已把 constructor productive 路线压到 built-in signed coefficient/pairing。",
            BUILTIN_PAIRING,
        ),
        row(
            "GenericBuiltInTraceSameTargetImported",
            generic.get("target_input_before_router") == BUILTIN_PAIRING
            and generic.get("next_primary_attack_target") == NEW_PAYLOAD
            and generic.get("branch_trace_self_proof_rejected") is True,
            True,
            "既有 latest built-in trace 证书的输入目标相同，可直接导入 branch-trace/cycle guard。",
            NEW_PAYLOAD,
        ),
        row(
            "StrictBuiltInFrontierImported",
            strict_builtin.get("next_direct_attack_target") == BRANCH_TRACE,
            True,
            "内置 signed pairing 的直接 strict 前沿是 exact atomic joint branch trace。",
            BRANCH_TRACE,
        ),
        row(
            "BranchTracePayloadFrontierImported",
            branch_payload.get("target_input_before_router") == BRANCH_TRACE
            and branch_payload.get("next_direct_attack_target") == SIGNED_PAYLOAD,
            False,
            "branch trace 若继续展开，会进入 signed payload constructor，而非直接闭合。",
            SIGNED_PAYLOAD,
        ),
        row(
            "SignedLaneCycleGuardImported",
            signed_cycle.get("signed_lane_cycle_closed") is True
            or signed_cycle.get("aggregate", {}).get("signed_lane_cycle_closed") is True,
            True,
            "signed payload、origin identity、common packet 与 built-in pairing 已构成自证环。",
            f"{NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
        ),
        row(
            "NewPrimitivePayloadCurrentCorpusProved",
            False,
            False,
            "当前语料没有新增 primitive atomic signed payload 或 trace formula 工件。",
            NEW_PAYLOAD,
        ),
        row(
            "ExactUVParallelCarried",
            latest.get("parallel_primary_attack_target") == exactuv_pair()
            and generic.get("exactuv_entropy_fiber_pair_imported") is True,
            False,
            "constructor 下游与 built-in trace 线保留同一个 ExactUV entropy/fiber 并行门。",
            exactuv_pair(),
        ),
        row(
            "SourceEntropyStillOpen",
            source_entropy.get("next_direct_attack_target")
            == "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward",
            False,
            "source-domain entropy 仍下钻到 primitive row signed coefficient law，未由 trace 同步支付。",
            SOURCE_ENTROPY_TARGET,
        ),
        row(
            "FixedPairFiberStillOpen",
            fixed_fiber.get("terminal_gap_after_router") == f"{REGISTERED_KEY} AND {FIXED_KEY}",
            False,
            "fixed-pair fiber 已原子化为 complete key polylog 分区与 fixed-key O(1) 局部重数，二者仍未证。",
            f"{REGISTERED_KEY} AND {FIXED_KEY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只是 latest constructor-built-in 口径同步，不是无条件闭合。",
            "row/column theorem still open",
        ),
    ]


def retained_basis() -> str:
    """返回最新保留基。"""
    return (
        f"(({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}) AND {exactuv_pair()}) "
        f"AND {REGISTERED_KEY} AND {FIXED_KEY} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    latest = load_json(LATEST_BUILTIN)
    generic = load_json(GENERIC_BUILTIN_TRACE)
    strict_builtin = load_json(STRICT_BUILTIN)
    branch_payload = load_json(STRICT_BRANCH_PAYLOAD)
    signed_cycle = load_json(SIGNED_LANE_CYCLE)
    fixed_fiber = load_json(FIXED_PAIR_FIBER)
    source_entropy = load_json(SOURCE_ENTROPY)
    rows = build_rows(latest, generic, strict_builtin, branch_payload, signed_cycle, fixed_fiber, source_entropy)
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_constructor_builtin_trace_sync_router",
        "status": "phi_lpf_latest_constructor_builtin_pairing_synced_to_new_payload_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "latest_constructor_builtin_pairing_imported": rows[0]["closed"],
        "generic_builtin_trace_same_target_imported": rows[1]["closed"],
        "strict_builtin_frontier_imported": rows[2]["closed"],
        "branch_trace_payload_frontier_imported": rows[3]["closed"],
        "signed_lane_cycle_guard_imported": rows[4]["closed"],
        "new_primitive_payload_or_trace_artifact_present": False,
        "exactuv_parallel_carried": rows[6]["closed"],
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": BUILTIN_PAIRING,
        "intermediate_primary_attack_target": BRANCH_TRACE,
        "absorbed_to": NEW_PAYLOAD,
        "next_primary_attack_target": NEW_PAYLOAD,
        "parallel_primary_attack_target": exactuv_pair(),
        "latest_retained_basis_after_router": retained_basis(),
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor 口径下的 latest built-in pairing 接入既有 branch-trace/cycle guard。"
            f"built-in pairing 的直接前沿是 `{BRANCH_TRACE}`，但现有 trace/payload/origin/common packet "
            f"子线是 signed-lane 自证环；删除该环后，最新非循环主攻为 `{NEW_PAYLOAD}`，"
            f"并行 ExactUV 门仍为 `{exactuv_pair()}`。行/列命题仍未无条件闭合。"
        ),
    }
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix Phi-LPF latest constructor built-in trace sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
    ]
    for key in [
        "latest_constructor_builtin_pairing_imported",
        "generic_builtin_trace_same_target_imported",
        "strict_builtin_frontier_imported",
        "branch_trace_payload_frontier_imported",
        "signed_lane_cycle_guard_imported",
        "new_primitive_payload_or_trace_artifact_present",
        "exactuv_parallel_carried",
        "row_column_unconditional_closed",
        "intermediate_primary_attack_target",
        "next_primary_attack_target",
        "parallel_primary_attack_target",
    ]:
        value = cert[key]
        lines.append(f"{key}={value if not isinstance(value, bool) else fmt_bool(value)}")
    lines.extend(
        [
            "```",
            "",
            "## 1. 同步链",
            "",
            "| from | to | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for edge in cert["sync_chain"]:
        lines.append(f"| `{cell(edge['from'])}` | `{cell(edge['to'])}` | {cell(edge['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for gate in cert["gates"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
                gate=cell(gate["gate"]),
                closed=fmt_bool(gate["closed"]),
                proved=fmt_bool(gate["proved"]),
                meaning=cell(gate["meaning"]),
                remaining=cell(gate["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 最新主攻",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行 ExactUV 主攻：",
            "",
            "```text",
            cert["parallel_primary_attack_target"],
            "```",
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "```json",
            json.dumps(cert["source_hashes"], ensure_ascii=False, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 ledger、JSON 与 Markdown。"""
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"parallel_primary_attack_target={cert['parallel_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
