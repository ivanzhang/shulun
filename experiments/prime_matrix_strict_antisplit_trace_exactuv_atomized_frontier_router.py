#!/usr/bin/env python3
"""生成反分裂 trace-cycle 与 ExactUV 原子化统一前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_antisplit_trace_exactuv_atomized_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json

输出：
  data/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-ledger.json
  docs/monograph/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json
  docs/monograph/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.md"

DOWNSTREAM = DOCS / "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json"
BUILTIN = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
SIGNED_CYCLE = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
SOURCE_ENTROPY_ATOM = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"
FIXED_FIBER = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json"

BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
BRANCH_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
EMITTER_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
SIGNED_ROW_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
ROW_MASS_ENTROPY = "ActualPreCauchySourceDomainEntropyFromSignedRowsAndRowMassLedger"
FIXED_PAIR_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，缺失不当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        DOWNSTREAM,
        BUILTIN,
        SIGNED_CYCLE,
        SOURCE_ENTROPY_ATOM,
        FIXED_FIBER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_edges() -> list[dict[str, str]]:
    """列出本次同步边。"""
    return [
        {
            "from": BUILTIN_PAIRING,
            "to": BRANCH_TRACE,
            "meaning": "built-in pairing 的非循环闭式需要 exact atomic branch trace。",
        },
        {
            "from": BRANCH_TRACE,
            "to": "signed-lane dependency cycle",
            "meaning": "exact branch trace 沿 signed payload/origin identity 回到 common source packet，不能自证。",
        },
        {
            "from": "signed-lane dependency cycle",
            "to": f"{NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
            "meaning": "打破闭环必须提交新 primitive payload/trace、well-founded terminal descent 或 same-set PDEC。",
        },
        {
            "from": EMITTER_ENTROPY,
            "to": ROW_MASS_ENTROPY,
            "meaning": "source-domain entropy 继承 actual pre-Cauchy signed row-mass entropy 原子化。",
        },
        {
            "from": ROW_MASS_ENTROPY,
            "to": SIGNED_ROW_LAW,
            "meaning": "row-mass entropy 的当前第一生产性单点是 signed primitive row coefficient law。",
        },
        {
            "from": FIXED_PAIR_FIBER,
            "to": f"{REGISTERED_KEY} AND {FIXED_KEY_MULT}",
            "meaning": "fixed-pair fiber bound 被拆成 registered complete key 分区与 fixed-key exact-UV 局部重数。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """合并各证书读数。"""
    downstream = data["downstream"]
    builtin = data["builtin"]
    signed_cycle = data["signed_cycle"]
    entropy = data["entropy"]
    fiber = data["fiber"]

    downstream_active = downstream.get("next_direct_attack_target") == BUILTIN_PAIRING
    builtin_to_trace = builtin.get("next_direct_attack_target") == BRANCH_TRACE
    signed_cycle_closed = signed_cycle.get("signed_lane_cycle_closed") is True
    signed_selfproof_removed = signed_cycle.get("signed_lane_self_proof_eliminated") is True
    entropy_to_signed_rows = entropy.get("next_direct_attack_target") == SIGNED_ROW_LAW
    fiber_atomized = fiber.get("terminal_gap_after_router") == f"{REGISTERED_KEY} AND {FIXED_KEY_MULT}"

    return [
        row(
            "AntiSplitDownstreamBasisImported",
            downstream_active,
            False,
            "上一层已把反分裂 atomic rows 的 signed 缺口压成 built-in pairing。",
            BUILTIN_PAIRING,
        ),
        row(
            "BuiltInPairingReducedToBranchTrace",
            builtin_to_trace,
            False,
            "built-in pairing 的真正非循环闭式必须给 exact atomic branch trace signed coefficient formula。",
            BRANCH_TRACE,
        ),
        row(
            "SignedLaneTraceCycleImported",
            signed_cycle_closed and signed_selfproof_removed,
            True,
            "exact branch trace 已在 signed-lane 闭环中；环内节点不能互相自证。",
            f"{NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
        ),
        row(
            "NewPrimitiveTracePayloadStillAbsent",
            signed_cycle.get("new_primitive_payload_or_trace_artifact_present") is False,
            False,
            "当前材料没有能打破 signed-lane 闭环的新 primitive trace/payload 工件。",
            NEW_PAYLOAD,
        ),
        row(
            "EmitterEntropyAtomizationImported",
            entropy_to_signed_rows,
            False,
            "Actual emitter source-domain entropy 已对齐到 signed row-mass entropy 包。",
            ROW_MASS_ENTROPY,
        ),
        row(
            "SignedRowLawStillOpen",
            entropy.get("acyclic_seed_primitive_row_signed_coefficient_law_proved") is False,
            False,
            "signed row-mass entropy 的第一生产性行权重律仍未证明。",
            SIGNED_ROW_LAW,
        ),
        row(
            "FixedPairFiberAtomized",
            fiber_atomized,
            False,
            "fixed-pair polylog fiber bound 已拆成 complete key 分区和 fixed-key 局部 O(1) 重数。",
            f"{REGISTERED_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "RegisteredCompleteKeyStillOpen",
            fiber.get("registered_complete_primitive_emitter_key_partition_polylog_proved") is False,
            False,
            "当前材料没有证明 actual noncanonical primitive emitter 的 complete key 数为 log^O(1)。",
            REGISTERED_KEY,
        ),
        row(
            "FixedKeyMultiplicityStillOpen",
            fiber.get("fixed_key_exact_uv_local_multiplicity_o1_proved") is False,
            False,
            "当前材料没有证明固定 complete key 与 fixed exact `(u,v)` 下只有 O(1) 原像。",
            FIXED_KEY_MULT,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只完成 trace-cycle 与 ExactUV 原子化同步；未证明新 payload、signed row law、key/fiber 或晋级门。",
            "row/column theorem still open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """生成统一原子化前沿证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "downstream": load_json(DOWNSTREAM),
        "builtin": load_json(BUILTIN),
        "signed_cycle": load_json(SIGNED_CYCLE),
        "entropy": load_json(SOURCE_ENTROPY_ATOM),
        "fiber": load_json(FIXED_FIBER),
    }
    rows = build_rows(data)
    internal_basis = (
        f"({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) "
        f"AND {ROW_MASS_ENTROPY} AND {REGISTERED_KEY} AND {FIXED_KEY_MULT}"
    )
    fine_atom_basis = (
        f"({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) "
        f"AND {SIGNED_ROW_LAW} AND {REGISTERED_KEY} AND {FIXED_KEY_MULT}"
    )
    retained_basis = f"({fine_atom_basis}) AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    result = {
        "certificate_type": "prime_matrix_strict_antisplit_trace_exactuv_atomized_frontier_router",
        "status": "antisplit_builtin_pairing_synced_to_trace_cycle_and_exactuv_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "built_in_pairing_reduced_to_branch_trace": rows[1]["closed"],
        "signed_lane_trace_cycle_imported": rows[2]["closed"],
        "new_primitive_payload_or_trace_artifact_present": False,
        "emitter_entropy_atomized_to_signed_row_mass": rows[4]["closed"],
        "fixed_pair_fiber_atomized": rows[6]["closed"],
        "acyclic_seed_primitive_row_signed_coefficient_law_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_PAYLOAD,
        "parallel_direct_attack_targets": [
            SIGNED_ROW_LAW,
            REGISTERED_KEY,
            FIXED_KEY_MULT,
        ],
        "strict_internal_basis_after_router": internal_basis,
        "fine_atom_basis_after_router": fine_atom_basis,
        "unified_retained_remaining_basis": retained_basis,
        "sync_edges": sync_edges(),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把反分裂 built-in pairing 继续同步到 exact atomic branch trace；"
            "但 branch trace 已被 signed-lane cycle 证书登记为闭环中的节点，不能自证。"
            "因此 signed 侧非循环出口回到 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` "
            "或 terminal/PDEC/外部输入。并行 ExactUV 侧被原子化为 signed row-mass entropy、"
            "registered complete key 分区和 fixed-key exact-UV 局部重数。上述原子当前均未证明，"
            "行/列命题仍未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 反分裂 trace-cycle / ExactUV 原子化前沿",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"built_in_pairing_reduced_to_branch_trace={fmt_bool(result['built_in_pairing_reduced_to_branch_trace'])}",
        f"signed_lane_trace_cycle_imported={fmt_bool(result['signed_lane_trace_cycle_imported'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(result['new_primitive_payload_or_trace_artifact_present'])}",
        f"emitter_entropy_atomized_to_signed_row_mass={fmt_bool(result['emitter_entropy_atomized_to_signed_row_mass'])}",
        f"fixed_pair_fiber_atomized={fmt_bool(result['fixed_pair_fiber_atomized'])}",
        f"acyclic_seed_primitive_row_signed_coefficient_law_proved={fmt_bool(result['acyclic_seed_primitive_row_signed_coefficient_law_proved'])}",
        f"registered_complete_primitive_emitter_key_partition_polylog_proved={fmt_bool(result['registered_complete_primitive_emitter_key_partition_polylog_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_o1_proved={fmt_bool(result['fixed_key_exact_uv_local_multiplicity_o1_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "parallel_direct_attack_targets=" + ", ".join(result["parallel_direct_attack_targets"]),
        "```",
        "",
        "## 1. 同步边",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_edges"]:
        lines.append(
            "| "
            + " | ".join([f"`{cell(item['from'])}`", f"`{cell(item['to'])}`", cell(item["meaning"])])
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
                    f"`{cell(item['gate'])}`",
                    fmt_bool(item["closed"]),
                    fmt_bool(item["proved"]),
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 粗内部基",
            "",
            "```text",
            result["strict_internal_basis_after_router"],
            "```",
            "",
            "## 4. 细原子基",
            "",
            "```text",
            result["fine_atom_basis_after_router"],
            "```",
            "",
            "## 5. 统一保留剩余基",
            "",
            "```text",
            result["unified_retained_remaining_basis"],
            "```",
            "",
            "## 6. 结论边界",
            "",
            "- 本文件是 trace-cycle 与 ExactUV atomization 同步，不是行/列命题证明。",
            "- exact branch trace 在 signed-lane 闭环内，不能作为自足闭合。",
            "- 下一 signed 侧非循环出口是 new primitive payload/trace；ExactUV 侧并行要求 signed row law、registered key 与 fixed-key multiplicity。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(name)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """入口。"""
    result = build_result()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
