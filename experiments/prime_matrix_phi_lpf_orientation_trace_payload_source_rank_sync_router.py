#!/usr/bin/env python3
"""生成 Phi-LPF 取向律到 trace/payload/source-rank 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_orientation_trace_payload_source_rank_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync-router.json

输出：
  data/prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_ORIENTATION = DOCS / "prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json"
ORIENTATION_TRACE = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
TRACE_PAYLOAD_CYCLE = DOCS / "prime-matrix-strict-branch-trace-signed-payload-cycle-router.json"
COMMON_PACKET = DOCS / "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json"
NEW_PRIMITIVE = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"
SOURCE_ATOM = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
GLOBAL_AFTER_TRACE = DOCS / "prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json"

ORIENTATION = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
ACTUAL_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
TRACE_PAYLOAD = "SignedPayloadTraceConstructorBeforeAssignmentOrReturn"
NEW_PRIMITIVE_ARTIFACT = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
COMMON_PACKET_TARGET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
SOURCE_RANK = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
SOURCE_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
KEY_PARTITION = "CompletePrimitiveEmitterKeyPartitionLedger"
LOCAL_MULTIPLICITY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_SPECTRAL = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时按未闭合处理。"""
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


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希，便于之后审计。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_ORIENTATION,
        ORIENTATION_TRACE,
        TRACE_PAYLOAD_CYCLE,
        COMMON_PACKET,
        NEW_PRIMITIVE,
        SOURCE_ATOM,
        GLOBAL_AFTER_TRACE,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不能当作证明。"""
    paths = [
        LATEST_ORIENTATION,
        ORIENTATION_TRACE,
        TRACE_PAYLOAD_CYCLE,
        COMMON_PACKET,
        NEW_PRIMITIVE,
        SOURCE_ATOM,
        GLOBAL_AFTER_TRACE,
    ]
    return [str(path.relative_to(ROOT)) for path in paths if not path.exists()]


def build_rows(deps: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把取向律硬点同步到 trace/payload/source-rank 审查。"""
    latest = deps["latest"]
    orientation_trace = deps["orientation_trace"]
    trace_cycle = deps["trace_cycle"]
    common_packet = deps["common_packet"]
    new_primitive = deps["new_primitive"]
    source_atom = deps["source_atom"]
    global_after_trace = deps["global_after_trace"]
    packet_aggregate = common_packet.get("aggregate", {})
    aggregate = new_primitive.get("aggregate", {})

    return [
        row(
            "LatestOrientationLawImported",
            latest.get("next_primary_attack_target") == ORIENTATION,
            False,
            "上一 Phi-LPF 同步层已把逐点 signed 表压到 primitive orientation/local-factor 乘积律。",
            ORIENTATION,
        ),
        row(
            "OrientationLawReducedToActualBranchTrace",
            orientation_trace.get("active_previous_target") == ORIENTATION
            and orientation_trace.get("next_direct_attack_target") == ACTUAL_TRACE,
            False,
            "取向/local-factor 若要正向生成，必须由 actual noncanonical primitive branch trace 同时登记 orientation、local factor、sign、UV 与 return。",
            ACTUAL_TRACE,
        ),
        row(
            "TracePayloadCycleImported",
            trace_cycle.get("active_previous_target") == ACTUAL_TRACE
            and trace_cycle.get("signed_payload_trace_returns_to_row_level_origin_table") is True
            and trace_cycle.get("branch_trace_route_counts_as_independent_proof") is False,
            True,
            "当前内部展开中，branch trace 的可见坐标可定位，但 signed payload 会经 slot/value-map/origin 回到 row-level 表。",
            TRACE_PAYLOAD,
        ),
        row(
            "VisibleTraceCannotGenerateOddPayload",
            trace_cycle.get("visible_coordinate_trace_reduced_to_word_coordinate_chain") is True,
            True,
            "anchor、D0/K/Omega、phase、word-coordinate 都是可见坐标字段，不能生成反变号 orientation 或 signed coefficient。",
            TRACE_PAYLOAD,
        ),
        row(
            "CommonPacketNeedImported",
            packet_aggregate.get("common_source_declaration_packet") == COMMON_PACKET_TARGET
            and packet_aggregate.get("common_packet_proved") is False,
            False,
            "signed payload 与 ExactUV 线合流到同一个 pre-Cauchy actual source declaration packet；该 packet 当前未证明。",
            COMMON_PACKET_TARGET,
        ),
        row(
            "NewPrimitiveArtifactAlignedToSourceRank",
            aggregate.get("new_primitive_artifact_reduced_to_source_rank_atom") is True
            and new_primitive.get("next_direct_attack_target") == SOURCE_ENTROPY,
            False,
            "若要新增 primitive payload/trace 工件，它不能只改名 trace 或 origin；必须携带 source rank/no-collapse 包。",
            SOURCE_RANK,
        ),
        row(
            "SourceRankAtomPackageImported",
            source_atom.get("terminal_gap_after_router") == SOURCE_RANK
            and source_atom.get("next_direct_attack_target") == SOURCE_ENTROPY,
            False,
            "preterminal fiber-dispersion 审查已把 source rank/no-collapse 拆成 source entropy、complete key partition、fixed-key local multiplicity 三原子。",
            f"{SOURCE_ENTROPY} AND {KEY_PARTITION} AND {LOCAL_MULTIPLICITY}",
        ),
        row(
            "BranchTraceSelfProofAlreadyEliminated",
            global_after_trace.get("branch_trace_self_proof_eliminated") is True,
            True,
            "全局前沿已把 branch trace 自证从活动证明路径删除；不能把 trace 格式本身当作非循环证明。",
            f"{SOURCE_RANK} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}",
        ),
        row(
            "LPFPhiBucketsOnlyFixUnsignedSupport",
            True,
            True,
            "LPF/Phi 桶恒等式给出合数最小素因子归属、容量和支撑前像；它不提供 signed orientation payload。",
            SOURCE_ENTROPY,
        ),
        row(
            "ActualSourceDomainEntropyCurrentCorpusProved",
            source_atom.get("actual_precauchy_source_domain_absolute_entropy_ledger_proved") is True,
            False,
            "当前材料尚未证明 actual pre-Cauchy source 域的绝对质量不集中账本。",
            SOURCE_ENTROPY,
        ),
        row(
            "CompleteKeyPartitionCurrentCorpusProved",
            source_atom.get("complete_primitive_emitter_key_partition_ledger_proved") is True,
            False,
            "complete key 必须在发射前登记 formal unit、branch path、exact UV、sign/local factor 和 truncation 状态。",
            KEY_PARTITION,
        ),
        row(
            "FixedKeyLocalMultiplicityCurrentCorpusProved",
            source_atom.get("fixed_key_exact_uv_local_multiplicity_o1_ledger_proved") is True,
            False,
            "固定 complete key 与 fixed exact UV 下的 O(1) 局部重数尚未证明。",
            LOCAL_MULTIPLICITY,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只同步并压窄 hardpoint；source 三原子、terminal/PDEC/外部谱出口、RatePreservation 与 DStructure/Rankin 仍未全部闭合。",
            f"({SOURCE_ENTROPY} AND {KEY_PARTITION} AND {LOCAL_MULTIPLICITY}) OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}; {RATE}; {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    deps = {
        "latest": load_json(LATEST_ORIENTATION),
        "orientation_trace": load_json(ORIENTATION_TRACE),
        "trace_cycle": load_json(TRACE_PAYLOAD_CYCLE),
        "common_packet": load_json(COMMON_PACKET),
        "new_primitive": load_json(NEW_PRIMITIVE),
        "source_atom": load_json(SOURCE_ATOM),
        "global_after_trace": load_json(GLOBAL_AFTER_TRACE),
    }
    rows = build_rows(deps)
    sync_chain = [
        {
            "from": ORIENTATION,
            "to": ACTUAL_TRACE,
            "meaning": "取向/local-factor 乘积律必须由完整 actual branch trace 正向生成。",
        },
        {
            "from": ACTUAL_TRACE,
            "to": TRACE_PAYLOAD,
            "meaning": "trace 的可见坐标已定位；signed payload 仍是未给出的奇数据。",
        },
        {
            "from": TRACE_PAYLOAD,
            "to": COMMON_PACKET_TARGET,
            "meaning": "payload 与 ExactUV 都需要同一 pre-Cauchy actual source packet。",
        },
        {
            "from": NEW_PRIMITIVE_ARTIFACT,
            "to": SOURCE_RANK,
            "meaning": "若新增 primitive payload/trace 工件，必须同时给 source entropy、complete key 与 fixed-key local multiplicity。",
        },
        {
            "from": SOURCE_RANK,
            "to": f"{SOURCE_ENTROPY} AND {KEY_PARTITION} AND {LOCAL_MULTIPLICITY}",
            "meaning": "source rank/no-collapse 包的首攻项是 actual source-domain absolute entropy。",
        },
    ]
    strict_basis = (
        f"(({SOURCE_ENTROPY} AND {KEY_PARTITION} AND {LOCAL_MULTIPLICITY}) OR "
        f"{TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}) AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_orientation_trace_payload_source_rank_sync_router",
        "status": "phi_lpf_orientation_law_synced_to_trace_payload_source_rank_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_lpf_phi_identity_used_as_unsigned_support_only": True,
        "orientation_law_before_router": ORIENTATION,
        "orientation_reduced_to_actual_branch_trace": rows[1]["closed"],
        "trace_payload_cycle_imported": rows[2]["closed"],
        "visible_trace_cannot_generate_odd_payload": rows[3]["closed"],
        "common_packet_need_imported": rows[4]["closed"],
        "new_primitive_artifact_aligned_to_source_rank": rows[5]["closed"],
        "source_rank_atom_package_imported": rows[6]["closed"],
        "actual_source_domain_entropy_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_proved": False,
        "orientation_local_factor_law_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SOURCE_ENTROPY,
        "parallel_direct_attack_targets": [
            KEY_PARTITION,
            LOCAL_MULTIPLICITY,
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            EXTERNAL_SPECTRAL,
            RATE,
            DSTRUCTURE,
        ],
        "latest_strict_activity_basis": strict_basis,
        "sync_chain": sync_chain,
        "gates": rows,
        "missing_sources": missing_sources(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步把最新 `{ORIENTATION}` 同步到已有 trace/payload/source-rank 更深前沿。"
            f"完整 branch trace 只是取向律的正确格式；在当前内部材料中，其 signed payload 部分会回到"
            " row-level/source packet 闭环，不能自证。若要新增真正 primitive payload/trace 工件，"
            f"它必须携带 `{SOURCE_RANK}`，也就是 source-domain entropy、complete key partition "
            "和 fixed-key exact-UV local multiplicity 三原子。LPF/Phi 精准桶恒等式已固定无符号支撑，"
            f"但不能生成 signed orientation；所以下一直接主攻为 `{SOURCE_ENTROPY}`。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF orientation trace payload source-rank sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"orientation_reduced_to_actual_branch_trace={fmt_bool(cert['orientation_reduced_to_actual_branch_trace'])}",
        f"trace_payload_cycle_imported={fmt_bool(cert['trace_payload_cycle_imported'])}",
        f"visible_trace_cannot_generate_odd_payload={fmt_bool(cert['visible_trace_cannot_generate_odd_payload'])}",
        f"common_packet_need_imported={fmt_bool(cert['common_packet_need_imported'])}",
        f"new_primitive_artifact_aligned_to_source_rank={fmt_bool(cert['new_primitive_artifact_aligned_to_source_rank'])}",
        f"source_rank_atom_package_imported={fmt_bool(cert['source_rank_atom_package_imported'])}",
        f"actual_source_domain_entropy_proved={fmt_bool(cert['actual_source_domain_entropy_proved'])}",
        f"complete_primitive_emitter_key_partition_proved={fmt_bool(cert['complete_primitive_emitter_key_partition_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_proved={fmt_bool(cert['fixed_key_exact_uv_local_multiplicity_proved'])}",
        f"orientation_local_factor_law_proved={fmt_bool(cert['orientation_local_factor_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={cert['next_direct_attack_target']}",
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
            "## 3. 最新 strict 基",
            "",
            "```text",
            cert["latest_strict_activity_basis"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_direct_attack_targets"]),
            "```",
            "",
            "## 4. 结论边界",
            "",
            "- 本层不是取向律证明，而是把取向律接入更深的 trace/payload/source-rank 审查。",
            "- LPF/Phi 桶恒等式在这里的作用是封死无符号支撑自由度，不产生 signed coefficient。",
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
