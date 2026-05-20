#!/usr/bin/env python3
"""生成 Phi-LPF latest signed 宏环与 ExactUV source-table 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_signed_macrocycle_exactuv_source_table_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SOURCE_TO_BUILTIN = DOCS / "prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync-router.json"
BUILTIN_TRACE = DOCS / "prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json"
TRACE_EXIT = DOCS / "prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json"
ALPHA_THREE = DOCS / "prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-router.json"
MOVING_BUCKET = DOCS / "prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-router.json"
MOVING_SPLIT = DOCS / "prime-matrix-phi-lpf-moving-atom-signed-injection-split-router.json"
POINTWISE_ORIENTATION = DOCS / "prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json"
ORIENTATION_SOURCE_RANK = DOCS / "prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync-router.json"
EXACTUV_ATOMIZED = DOCS / "prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json"
FIXED_FIBER = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json"
COMPLETE_KEY = DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.json"
SOURCE_TABLE = DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json"

SOURCE_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
NEW_PRIMITIVE = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
SIGNED_INJECTION = "LPFMovingAtomSignedPreimageMassInjectionLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ORIENTATION = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
EMITTER_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
EXACTUV_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
SIGNED_ROW_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SOURCE_TABLE_LEDGER = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
PRECAUCHY_DECL = "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
SUMMAND_ROWS = "PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable"
ALPHA_DELTA_ID = "AlphaDeltaCoefficientIdentityBeforePushforwardLedger"
SOURCE_RETURN = "SourceTableNoDownstreamRecoveryAndNamedReturnLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不当作证明。"""
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
    """本层依赖文件。"""
    return [
        SOURCE_TO_BUILTIN,
        BUILTIN_TRACE,
        TRACE_EXIT,
        ALPHA_THREE,
        MOVING_BUCKET,
        MOVING_SPLIT,
        POINTWISE_ORIENTATION,
        ORIENTATION_SOURCE_RANK,
        EXACTUV_ATOMIZED,
        FIXED_FIBER,
        COMPLETE_KEY,
        SOURCE_TABLE,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希，便于复核。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def exactuv_pair() -> str:
    """返回 ExactUV 并行门。"""
    return f"{EMITTER_ENTROPY} AND {EXACTUV_FIBER}"


def source_table_fields() -> str:
    """返回 actual source table 的字段基。"""
    return f"{PRECAUCHY_DECL} AND {SUMMAND_ROWS} AND {ALPHA_DELTA_ID} AND {SOURCE_RETURN}"


def retained_basis() -> str:
    """返回本层之后的保留基。"""
    return (
        f"(({PRECAUCHY_DECL} AND {SIGNED_ROW_LAW} AND {FIXED_KEY_MULT}) "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) "
        f"AND {MODEL_GAP} AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(deps: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 signed 宏环与 ExactUV 原子化同步判定表。"""
    source_to_builtin = deps["source_to_builtin"]
    builtin_trace = deps["builtin_trace"]
    trace_exit = deps["trace_exit"]
    alpha_three = deps["alpha_three"]
    moving_bucket = deps["moving_bucket"]
    moving_split = deps["moving_split"]
    pointwise_orientation = deps["pointwise_orientation"]
    orientation_source_rank = deps["orientation_source_rank"]
    exactuv_atomized = deps["exactuv_atomized"]
    fixed_fiber = deps["fixed_fiber"]
    complete_key = deps["complete_key"]
    source_table = deps["source_table"]

    macrocycle_closed = (
        source_to_builtin.get("next_primary_attack_target") == BUILTIN_PAIRING
        and builtin_trace.get("next_primary_attack_target") == NEW_PRIMITIVE
        and trace_exit.get("next_primary_attack_target") == ALPHA_ANCHOR
        and alpha_three.get("next_primary_attack_target") == MOVING_ATOM
        and moving_bucket.get("next_primary_attack_target") == SIGNED_INJECTION
        and moving_split.get("next_primary_attack_target") == POINTWISE_TABLE
        and pointwise_orientation.get("next_primary_attack_target") == ORIENTATION
        and orientation_source_rank.get("next_direct_attack_target") == SOURCE_ENTROPY
    )

    return [
        row(
            "SourceEntropyToBuiltInImported",
            source_to_builtin.get("next_primary_attack_target") == BUILTIN_PAIRING,
            False,
            "上一层已把 latest source entropy 同步到 built-in pairing，并保留 ExactUV 并行门。",
            f"{BUILTIN_PAIRING} AND {exactuv_pair()}",
        ),
        row(
            "BuiltInToNewPrimitiveTraceCycleImported",
            builtin_trace.get("next_primary_attack_target") == NEW_PRIMITIVE
            and builtin_trace.get("branch_trace_self_proof_rejected") is True,
            True,
            "built-in pairing 若走 existing branch trace 会落入 signed payload/source packet 环。",
            NEW_PRIMITIVE,
        ),
        row(
            "NewPrimitiveToPointwiseKernelImported",
            trace_exit.get("next_primary_attack_target") == ALPHA_ANCHOR
            and trace_exit.get("post_antisplit_convergence_imported") is True,
            False,
            "new payload/trace 出口已收敛到 source-rank/no-collapse 与逐 primitive kernel。",
            ALPHA_ANCHOR,
        ),
        row(
            "AlphaFrontierToMovingAtomImported",
            alpha_three.get("next_primary_attack_target") == MOVING_ATOM
            and alpha_three.get("terminal_three_atoms_pinned") is True,
            False,
            "alpha terminal 三原子同步后，最窄活动口是 clean-core moving atom 排斥。",
            MOVING_ATOM,
        ),
        row(
            "MovingAtomUnsignedLPFPreimageClosed",
            moving_bucket.get("moving_atom_unsigned_source_preimage_partition_closed") is True,
            True,
            "LPF/Phi 桶恒等式关闭 moving atom 的无符号源前像自由度。",
            SIGNED_INJECTION,
        ),
        row(
            "MovingAtomSignedInjectionToPointwiseTableImported",
            moving_split.get("next_primary_attack_target") == POINTWISE_TABLE
            and moving_split.get("half_mass_sign_lane_extraction_finite_algebra_closed") is True,
            False,
            "signed injection 已无剩余无符号计数自由度，缺口是逐点 signed value table。",
            POINTWISE_TABLE,
        ),
        row(
            "PointwiseTableToOrientationImported",
            pointwise_orientation.get("next_primary_attack_target") == ORIENTATION,
            False,
            "逐点 signed table 下游首个 orientation-sensitive 字段是 primitive orientation/local-factor law。",
            ORIENTATION,
        ),
        row(
            "OrientationReturnsToSourceEntropyImported",
            orientation_source_rank.get("next_direct_attack_target") == SOURCE_ENTROPY,
            False,
            "orientation trace/payload 审查回到 source-rank/no-collapse 的 source entropy 首原子。",
            SOURCE_ENTROPY,
        ),
        row(
            "FullSignedMacrocycleClosedAsNonProof",
            macrocycle_closed,
            True,
            "source entropy -> built-in pairing -> trace/new payload -> alpha/moving atom -> signed table -> orientation -> source entropy 已闭成诊断环。",
            "remove internal signed self-proof",
        ),
        row(
            "LPFPhiUnsignedCapacityExhausted",
            moving_bucket.get("lpf_phi_composite_ownership_identity_imported") is True
            and moving_bucket.get("moving_atom_unsigned_source_preimage_partition_closed") is True,
            True,
            "LPF/Phi 精准桶只剩 signed 发射、source table 与 ExactUV 局部重数问题；无符号 support/capacity 不再是缺口。",
            f"{PRECAUCHY_DECL} AND {FIXED_KEY_MULT}",
        ),
        row(
            "ExactUVAtomizationImported",
            exactuv_atomized.get("fixed_pair_fiber_atomized") is True
            and exactuv_atomized.get("registered_complete_primitive_emitter_key_partition_polylog_proved") is False,
            False,
            "ExactUV 并行门已原子化为 signed row law、registered complete key 与 fixed-key local multiplicity。",
            f"{SIGNED_ROW_LAW} AND {REGISTERED_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "FixedPairFiberFormalInequalityClosed",
            fixed_fiber.get("deterministic_key_fiber_inequality_closed") is True,
            True,
            "fixed-pair 纤维的 key-count x fixed-key O(1) 形式不等式已闭合。",
            f"{REGISTERED_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "RegisteredCompleteKeyReducedToSourceTable",
            complete_key.get("next_direct_attack_target") == SOURCE_TABLE_LEDGER
            and complete_key.get("source_table_to_complete_key_implication_closed") is True,
            False,
            "complete key 不能后验补标签，必须来自 actual noncanonical primitive emitter source table。",
            SOURCE_TABLE_LEDGER,
        ),
        row(
            "SourceTableReducedToPreCauchyDeclaration",
            source_table.get("next_direct_attack_target") == PRECAUCHY_DECL
            and source_table.get("source_table_field_decomposition_pinned") is True,
            False,
            "actual source table 的首行必须是 Cauchy/dispersion 前的 constructor declaration。",
            PRECAUCHY_DECL,
        ),
        row(
            "PreCauchyDeclarationCurrentCorpusProved",
            False,
            False,
            "当前语料尚未给出 actual noncanonical emitter 的无环 pre-Cauchy declaration line。",
            PRECAUCHY_DECL,
        ),
        row(
            "FixedKeyLocalMultiplicityCurrentCorpusProved",
            False,
            False,
            "固定 complete key 与 fixed exact UV 下 O(1) 原像仍未由 actual emitter 公式/Jacobian/三角恢复律证明。",
            FIXED_KEY_MULT,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只删除完整 signed 宏环并同步 ExactUV/source-table 原子；没有关闭行/列命题。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    deps = {
        "source_to_builtin": load_json(SOURCE_TO_BUILTIN),
        "builtin_trace": load_json(BUILTIN_TRACE),
        "trace_exit": load_json(TRACE_EXIT),
        "alpha_three": load_json(ALPHA_THREE),
        "moving_bucket": load_json(MOVING_BUCKET),
        "moving_split": load_json(MOVING_SPLIT),
        "pointwise_orientation": load_json(POINTWISE_ORIENTATION),
        "orientation_source_rank": load_json(ORIENTATION_SOURCE_RANK),
        "exactuv_atomized": load_json(EXACTUV_ATOMIZED),
        "fixed_fiber": load_json(FIXED_FIBER),
        "complete_key": load_json(COMPLETE_KEY),
        "source_table": load_json(SOURCE_TABLE),
    }
    rows = build_rows(deps)
    macrocycle_chain = [
        {"from": SOURCE_ENTROPY, "to": BUILTIN_PAIRING, "meaning": "latest source entropy 已同步到 built-in pairing。"},
        {"from": BUILTIN_PAIRING, "to": NEW_PRIMITIVE, "meaning": "built-in pairing 的 existing trace 路线被 signed-lane cycle guard 删除。"},
        {"from": NEW_PRIMITIVE, "to": ALPHA_ANCHOR, "meaning": "new payload/trace 出口收敛到 source-rank/pointwise kernel。"},
        {"from": ALPHA_ANCHOR, "to": MOVING_ATOM, "meaning": "alpha terminal 三原子同步后转向 moving atom 排斥。"},
        {"from": MOVING_ATOM, "to": SIGNED_INJECTION, "meaning": "LPF/Phi 关闭无符号前像后，剩余 signed mass injection。"},
        {"from": SIGNED_INJECTION, "to": POINTWISE_TABLE, "meaning": "signed injection 缺口化为逐点 Phi-LPF signed value table。"},
        {"from": POINTWISE_TABLE, "to": ORIENTATION, "meaning": "逐点 signed table 回到 orientation/local-factor law。"},
        {"from": ORIENTATION, "to": SOURCE_ENTROPY, "meaning": "orientation trace/payload 审查回到 source-rank/source entropy。"},
    ]
    exactuv_chain = [
        {"from": exactuv_pair(), "to": f"{SIGNED_ROW_LAW} AND {REGISTERED_KEY} AND {FIXED_KEY_MULT}", "meaning": "ExactUV 并行门被拆成 signed row law、registered key 与 fixed-key local multiplicity。"},
        {"from": EXACTUV_FIBER, "to": f"{REGISTERED_KEY} AND {FIXED_KEY_MULT}", "meaning": "fixed-pair fiber bound 的形式不等式已闭合，实际输入是 key 分区与局部重数。"},
        {"from": REGISTERED_KEY, "to": SOURCE_TABLE_LEDGER, "meaning": "registered complete key 必须由 actual source table 生成。"},
        {"from": SOURCE_TABLE_LEDGER, "to": source_table_fields(), "meaning": "source table 拆成 declaration、rows、identity 与 no-recovery returns。"},
    ]
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_signed_macrocycle_exactuv_source_table_sync_router",
        "status": "phi_lpf_latest_signed_macrocycle_exactuv_synced_to_precauchy_source_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_lpf_phi_identity_used_as_unsigned_support_only": True,
        "source_entropy_to_builtin_imported": rows[0]["closed"],
        "builtin_to_new_primitive_trace_cycle_imported": rows[1]["closed"],
        "new_primitive_to_pointwise_kernel_imported": rows[2]["closed"],
        "alpha_frontier_to_moving_atom_imported": rows[3]["closed"],
        "moving_atom_unsigned_lpf_preimage_closed": rows[4]["closed"],
        "moving_atom_signed_injection_to_pointwise_table_imported": rows[5]["closed"],
        "pointwise_table_to_orientation_imported": rows[6]["closed"],
        "orientation_returns_to_source_entropy_imported": rows[7]["closed"],
        "full_signed_macrocycle_closed_as_nonproof": rows[8]["closed"],
        "lpf_phi_unsigned_capacity_exhausted": rows[9]["closed"],
        "exactuv_atomization_imported": rows[10]["closed"],
        "fixed_pair_fiber_formal_inequality_closed": rows[11]["closed"],
        "registered_complete_key_reduced_to_source_table": rows[12]["closed"],
        "source_table_reduced_to_precauchy_declaration": rows[13]["closed"],
        "pre_cauchy_constructor_declaration_line_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "built_in_signed_pairing_proved": False,
        "row_column_unconditional_closed": False,
        "next_primary_attack_target": PRECAUCHY_DECL,
        "parallel_primary_attack_targets": [
            FIXED_KEY_MULT,
            SIGNED_ROW_LAW,
            PDEC_SCOPE,
            EXTERNAL_DIBFI,
            MODEL_GAP,
            RATE,
            DSTRUCTURE,
        ],
        "retained_basis_after_router": retained_basis(),
        "macrocycle_chain": macrocycle_chain,
        "exactuv_source_table_chain": exactuv_chain,
        "gates": rows,
        "missing_sources": missing_sources(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest signed 路线从 source entropy 到 built-in pairing、trace/new payload、"
            "alpha/moving atom、pointwise signed table、orientation 再回到 source entropy 的完整宏环登记为"
            "非证明闭环。LPF/Phi 桶恒等式已经关闭无符号 support/capacity，但不能生成 signed source table。"
            f"环外 ExactUV 侧被原子化为 `{SIGNED_ROW_LAW}`、`{REGISTERED_KEY}` 与 `{FIXED_KEY_MULT}`；"
            f"`{REGISTERED_KEY}` 又必须来自 `{SOURCE_TABLE_LEDGER}`，其首行是 `{PRECAUCHY_DECL}`。"
            f"因此最新主攻压到 `{PRECAUCHY_DECL}`，并行保留 `{FIXED_KEY_MULT}` 与 PDEC/外部谱、模型、Rate、DStructure。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest signed macrocycle ExactUV source-table sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"source_entropy_to_builtin_imported={fmt_bool(cert['source_entropy_to_builtin_imported'])}",
        f"builtin_to_new_primitive_trace_cycle_imported={fmt_bool(cert['builtin_to_new_primitive_trace_cycle_imported'])}",
        f"new_primitive_to_pointwise_kernel_imported={fmt_bool(cert['new_primitive_to_pointwise_kernel_imported'])}",
        f"alpha_frontier_to_moving_atom_imported={fmt_bool(cert['alpha_frontier_to_moving_atom_imported'])}",
        f"moving_atom_unsigned_lpf_preimage_closed={fmt_bool(cert['moving_atom_unsigned_lpf_preimage_closed'])}",
        f"moving_atom_signed_injection_to_pointwise_table_imported={fmt_bool(cert['moving_atom_signed_injection_to_pointwise_table_imported'])}",
        f"pointwise_table_to_orientation_imported={fmt_bool(cert['pointwise_table_to_orientation_imported'])}",
        f"orientation_returns_to_source_entropy_imported={fmt_bool(cert['orientation_returns_to_source_entropy_imported'])}",
        f"full_signed_macrocycle_closed_as_nonproof={fmt_bool(cert['full_signed_macrocycle_closed_as_nonproof'])}",
        f"lpf_phi_unsigned_capacity_exhausted={fmt_bool(cert['lpf_phi_unsigned_capacity_exhausted'])}",
        f"exactuv_atomization_imported={fmt_bool(cert['exactuv_atomization_imported'])}",
        f"fixed_pair_fiber_formal_inequality_closed={fmt_bool(cert['fixed_pair_fiber_formal_inequality_closed'])}",
        f"registered_complete_key_reduced_to_source_table={fmt_bool(cert['registered_complete_key_reduced_to_source_table'])}",
        f"source_table_reduced_to_precauchy_declaration={fmt_bool(cert['source_table_reduced_to_precauchy_declaration'])}",
        f"pre_cauchy_constructor_declaration_line_proved={fmt_bool(cert['pre_cauchy_constructor_declaration_line_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_o1_proved={fmt_bool(cert['fixed_key_exact_uv_local_multiplicity_o1_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. Signed 宏环",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["macrocycle_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. ExactUV / Source-Table 链",
            "",
            "| from | to | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["exactuv_source_table_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 最新保留基",
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
            "\n".join(cert["parallel_primary_attack_targets"]),
            "```",
            "",
            "## 5. 结论边界",
            "",
            "- 本层删除的是完整 signed 宏环的自证路线，不是 signed coefficient 证明。",
            "- LPF/Phi 桶恒等式只支付无符号 ownership、support 和 capacity。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
