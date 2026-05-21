#!/usr/bin/env python3
"""生成 latest constructor new-payload/source-atom alignment 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_new_payload_source_atom_alignment_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_TRACE_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-router.json"
)
OLD_CONSTRUCTOR_ALIGNMENT_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-sync-router.json"
)
STRICT_ALIGNMENT_CERT = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"
SIGNED_LANE_CYCLE_CERT = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
SOURCE_ATOM_CERT = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
POINTWISE_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
SOURCE_RANK_ATOM = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
NONZERO_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当成闭合证明。"""
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


def source_atoms() -> str:
    """返回 constructor 分支继续携带的 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def dependency_paths() -> list[Path]:
    """列出本层依赖证书。"""
    return [
        CURRENT_TRACE_REBASE_CERT,
        OLD_CONSTRUCTOR_ALIGNMENT_CERT,
        STRICT_ALIGNMENT_CERT,
        SIGNED_LANE_CYCLE_CERT,
        SOURCE_ATOM_CERT,
        POINTWISE_CERT,
        EXACTUV_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    atoms = source_atoms()
    return (
        f"(({atoms} AND {ROW_MASS} AND {DOMAIN_ENTROPY}) OR {TERMINAL_DESCENT} "
        f"OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) AND {NONZERO_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY_MULT} AND {EXACTUV_PAIR} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )


def source_atom_contract() -> list[dict[str, str]]:
    """列出 new-payload 破环时必须携带的 source 原子字段。"""
    atoms = source_atoms()
    return [
        {
            "field": "same_trace_key_lock",
            "requirement": "继承 latest constructor trace rebase 的同一 pre-Cauchy trace key。",
            "remaining": NEW_PAYLOAD,
        },
        {
            "field": "constructor_source_three_atoms",
            "requirement": "继续携带 alpha anchor、arithmetic identity 与 ExactUV rank multiplicity 三原子。",
            "remaining": atoms,
        },
        {
            "field": "same_unit_row_mass_and_signed_survival",
            "requirement": "new payload 不替代 row-mass/no-heavy-row 或 signed survival。",
            "remaining": f"{ROW_MASS} AND {NONZERO_SURVIVAL}",
        },
        {
            "field": "source_domain_absolute_entropy",
            "requirement": "actual source domain 必须有足够绝对熵，不能坍缩到少数 rows、keys 或 fibers。",
            "remaining": DOMAIN_ENTROPY,
        },
        {
            "field": "complete_key_partition",
            "requirement": "必须在发射前给出 complete primitive emitter key partition。",
            "remaining": COMPLETE_KEY,
        },
        {
            "field": "fixed_key_exact_uv_local_multiplicity",
            "requirement": "固定 key 与 exact `(u,v)` 后仍需局部重数控制。",
            "remaining": FIXED_KEY_MULT,
        },
        {
            "field": "named_nonproductive_exits",
            "requirement": "terminal、same-set PDEC 或逐点表只能作为命名出口。",
            "remaining": f"{TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}",
        },
    ]


def largest_slot_sample(current_trace: dict[str, Any]) -> dict[str, Any]:
    """抽取当前 trace rebase 的最大 slot 样本。"""
    return current_trace.get("imported_largest_slot_sample", {})


def build_rows(
    current_trace: dict[str, Any],
    old_alignment: dict[str, Any],
    strict_alignment: dict[str, Any],
    signed_cycle: dict[str, Any],
    source_atom: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 new-payload source-atom alignment rebase 判定表。"""
    strict_agg = strict_alignment.get("aggregate", {})
    atoms = source_atoms()
    current_new_payload = (
        current_trace.get("next_primary_attack_target") == NEW_PAYLOAD
        and current_trace.get("signed_atom_trace_rebased") is True
    )
    old_alignment_reusable = (
        old_alignment.get("target_input_before_router") == NEW_PAYLOAD
        and old_alignment.get("latest_constructor_new_payload_reduced_to_source_rank_atom") is True
        and old_alignment.get("next_primary_attack_target") == DOMAIN_ENTROPY
    )
    strict_imported = (
        strict_alignment.get("status")
        == "strict_new_primitive_payload_reduced_to_actual_source_rank_atom_open"
    )
    source_rank_imported = (
        strict_agg.get("source_rank_atom_imported") is True
        or source_atom.get("terminal_gap_after_router") == SOURCE_RANK_ATOM
    )
    alignment_rebased = (
        current_new_payload
        and old_alignment_reusable
        and strict_imported
        and source_rank_imported
        and strict_agg.get("new_primitive_artifact_reduced_to_source_rank_atom") is True
    )
    return [
        row(
            "LatestRebasedNewPayloadImported",
            current_new_payload,
            False,
            "上一层 rebase 已把生产性硬点定位到 new primitive payload/trace。",
            NEW_PAYLOAD,
        ),
        row(
            "ExistingConstructorNewPayloadAlignmentReusable",
            old_alignment_reusable,
            False,
            "旧 constructor new-payload/source-atom alignment 输入相同，可在新 rebase 前沿复用。",
            DOMAIN_ENTROPY,
        ),
        row(
            "ConstructorSourceAndSideGatesCarried",
            atoms in current_trace.get("paired_constructor_required_targets", [])
            and current_trace.get("parallel_constructor_side_gates") == f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
            False,
            "new-payload alignment 只替换 new payload；source 三原子、row-mass 与 signed survival 继续携带。",
            f"{atoms} AND {ROW_MASS} AND {NONZERO_SURVIVAL}",
        ),
        row(
            "UnsignedLabelsCannotPayPayload",
            current_trace.get("closed_unsigned_labels_carried") is True,
            True,
            "LPF/Phi/Ferrers 的无符号 labels 只给输入域，不产生 signed coefficient、local factor 或 orientation。",
            NEW_PAYLOAD,
        ),
        row(
            "SignedLaneCycleCutCarried",
            signed_cycle.get("signed_lane_cycle_closed") is True
            and signed_cycle.get("signed_lane_self_proof_eliminated") is True
            and current_trace.get("trace_self_proof_cycle_cut_synced") is True,
            True,
            "trace rebase 继承 signed-lane 自证环删除；new payload 不能只是环内改名。",
            NEW_PAYLOAD,
        ),
        row(
            "StrictNewPayloadAlignmentImported",
            strict_imported,
            False,
            "strict 证书已说明 new primitive 工件若要破环，必须携带 actual source-rank/no-collapse 包。",
            SOURCE_RANK_ATOM,
        ),
        row(
            "NewPayloadReducedToSourceRankAtom",
            alignment_rebased,
            False,
            "source-rank/no-collapse 包展开为 source entropy、complete key 与 fixed-key ExactUV local multiplicity。",
            f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "IndependentNewPayloadTerminalRejected",
            strict_agg.get("new_primitive_artifact_independent_terminal_present") is False
            and current_trace.get("new_primitive_payload_or_trace_artifact_present") is False,
            True,
            "当前语料没有独立 new primitive 工件；缺三原子时只能是改名或命名出口。",
            SOURCE_RANK_ATOM,
        ),
        row(
            "ConstructorSourceAtomsStillOpen",
            current_trace.get("constructor_source_atoms_carried_forward") is True,
            False,
            "source 三原子仍是 constructor 分支配套硬点，不能由 new-payload 名称自动给出。",
            atoms,
        ),
        row(
            "ConstructorRowMassAndSurvivalStillOpen",
            current_trace.get("nonzero_signed_row_survival_proved") is False
            and current_trace.get("same_formal_unit_row_mass_normalization_proved") is False,
            False,
            "row-mass/no-heavy-row 与 signed survival 仍需独立账本。",
            f"{ROW_MASS} AND {NONZERO_SURVIVAL}",
        ),
        row(
            "SourceEntropyStillFirstAtom",
            strict_agg.get("actual_source_domain_entropy_proved") is False,
            False,
            "三原子包的第一直接硬点仍是 actual pre-Cauchy source-domain absolute entropy。",
            DOMAIN_ENTROPY,
        ),
        row(
            "CompleteKeyStillOpen",
            strict_agg.get("complete_primitive_emitter_key_partition_proved") is False,
            False,
            "complete key partition 仍未证明，不能由 Phi-LPF label 后验补齐。",
            COMPLETE_KEY,
        ),
        row(
            "FixedKeyMultiplicityStillOpen",
            strict_agg.get("fixed_key_exact_uv_local_multiplicity_proved") is False,
            False,
            "fixed-key ExactUV local multiplicity 仍未证明，不能由单条 edge label 排除 fiber 坍缩。",
            FIXED_KEY_MULT,
        ),
        row(
            "PointwiseTableStillAlternative",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed table 仍是并行替代，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "ExactUVStillIndependent",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "source entropy 与 fixed exact-pair fiber 控制不能由 trace rebase 自动推出。",
            EXACTUV_PAIR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只做 rebase 同步；未证明三命题无条件闭合。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    current_trace = load_json(CURRENT_TRACE_REBASE_CERT)
    old_alignment = load_json(OLD_CONSTRUCTOR_ALIGNMENT_CERT)
    strict_alignment = load_json(STRICT_ALIGNMENT_CERT)
    signed_cycle = load_json(SIGNED_LANE_CYCLE_CERT)
    source_atom = load_json(SOURCE_ATOM_CERT)
    pointwise = load_json(POINTWISE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(
        current_trace, old_alignment, strict_alignment, signed_cycle, source_atom, pointwise, exactuv
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_new_payload_source_atom_alignment_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_new_payload_source_atom_alignment_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_rebased_new_payload_imported": rows[0]["closed"],
        "existing_constructor_new_payload_alignment_reusable": rows[1]["closed"],
        "constructor_source_and_side_gates_carried": rows[2]["closed"],
        "unsigned_labels_cannot_pay_payload": rows[3]["closed"],
        "signed_lane_cycle_cut_carried": rows[4]["closed"],
        "strict_new_payload_alignment_imported": rows[5]["closed"],
        "new_payload_reduced_to_source_rank_atom": rows[6]["closed"],
        "latest_constructor_new_payload_reduced_to_source_rank_atom": rows[6]["closed"],
        "independent_new_payload_terminal_present": False,
        "constructor_source_atoms_carried_forward": rows[8]["closed"],
        "constructor_row_mass_and_survival_still_open": rows[9]["closed"],
        "actual_source_domain_entropy_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": NEW_PAYLOAD,
        "absorbed_to": SOURCE_RANK_ATOM,
        "next_primary_attack_target": DOMAIN_ENTROPY,
        "parallel_attack_targets": [
            source_atoms(),
            ROW_MASS,
            NONZERO_SURVIVAL,
            COMPLETE_KEY,
            FIXED_KEY_MULT,
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            POINTWISE_TABLE,
            EXACTUV_PAIR,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "latest_retained_basis_after_router": retained_basis(),
        "source_atom_contract": source_atom_contract(),
        "imported_largest_slot_sample": largest_slot_sample(current_trace),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 rebase 后的 constructor `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` "
            "接到 strict source-atom alignment。无符号 label 与 signed-lane trace 不能生产新 payload；"
            "若 new-payload 要成为真正新工件，就必须携带 actual pre-Cauchy source-rank/no-collapse 三原子。"
            "当前第一直接硬点推进到 `ActualPreCauchySourceDomainAbsoluteEntropyLedger`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor new-payload source-atom alignment rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_rebased_new_payload_imported={fmt_bool(result['latest_rebased_new_payload_imported'])}",
        f"existing_constructor_new_payload_alignment_reusable={fmt_bool(result['existing_constructor_new_payload_alignment_reusable'])}",
        f"constructor_source_and_side_gates_carried={fmt_bool(result['constructor_source_and_side_gates_carried'])}",
        f"unsigned_labels_cannot_pay_payload={fmt_bool(result['unsigned_labels_cannot_pay_payload'])}",
        f"signed_lane_cycle_cut_carried={fmt_bool(result['signed_lane_cycle_cut_carried'])}",
        f"strict_new_payload_alignment_imported={fmt_bool(result['strict_new_payload_alignment_imported'])}",
        f"new_payload_reduced_to_source_rank_atom={fmt_bool(result['new_payload_reduced_to_source_rank_atom'])}",
        f"independent_new_payload_terminal_present={fmt_bool(result['independent_new_payload_terminal_present'])}",
        f"constructor_source_atoms_carried_forward={fmt_bool(result['constructor_source_atoms_carried_forward'])}",
        f"constructor_row_mass_and_survival_still_open={fmt_bool(result['constructor_row_mass_and_survival_still_open'])}",
        f"actual_source_domain_entropy_proved={fmt_bool(result['actual_source_domain_entropy_proved'])}",
        f"complete_primitive_emitter_key_partition_proved={fmt_bool(result['complete_primitive_emitter_key_partition_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_proved={fmt_bool(result['fixed_key_exact_uv_local_multiplicity_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. source-atom 合同",
        "",
        "| field | requirement | remaining |",
        "| --- | --- | --- |",
    ]
    for item in result["source_atom_contract"]:
        lines.append(
            f"| `{cell(item['field'])}` | {cell(item['requirement'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    sample = result.get("imported_largest_slot_sample", {})
    if sample:
        lines.extend(
            [
                "",
                "## 3. 导入 latest slot 样本",
                "",
                "| N | canonical edges | open slots | trace packets |",
                "| --- | ---: | ---: | ---: |",
                (
                    f"| {sample['N']} | {sample['canonical_edges']} | "
                    f"{sample['open_signed_field_slots']} | {sample['same_trace_packets_required']} |"
                ),
            ]
        )
    lines.extend(
        [
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "并行出口：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
