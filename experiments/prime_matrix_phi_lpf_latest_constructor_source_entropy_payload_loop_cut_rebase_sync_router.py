#!/usr/bin/env python3
"""生成 latest constructor source-entropy payload-loop cut 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_source_entropy_payload_loop_cut_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_SOURCE_ATOM_REBASE_CERT = (
    DOCS
    / "prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-router.json"
)
OLD_CONSTRUCTOR_LOOP_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-sync-router.json"
)
STRICT_SOURCE_ENTROPY_DOWNSTREAM_CERT = (
    DOCS / "prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json"
)
STRICT_UNIFIED_FRONTIER_CERT = (
    DOCS / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json"
)
CONSTRUCTOR_TRIAD_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.json"
)
CONSTRUCTOR_JOINT_DECL_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-router.json"
)
CONSTRUCTOR_BUILTIN_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-router.json"
)
SOURCE_ENTROPY_ATOM_CERT = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"
SOURCE_SURVIVAL_CERT = DOCS / "prime-matrix-phi-lpf-source-entropy-signed-survival-router.json"

DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
CYCLE_OR_TERMINAL = (
    "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput_OR_"
    "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
)
CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
FRESH_JOINT_DECL = "FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
INDEPENDENT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_UNIT_MULT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
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


def dependency_paths() -> list[Path]:
    """列出本层依赖证书。"""
    return [
        CURRENT_SOURCE_ATOM_REBASE_CERT,
        OLD_CONSTRUCTOR_LOOP_CERT,
        STRICT_SOURCE_ENTROPY_DOWNSTREAM_CERT,
        STRICT_UNIFIED_FRONTIER_CERT,
        CONSTRUCTOR_TRIAD_CERT,
        CONSTRUCTOR_JOINT_DECL_CERT,
        CONSTRUCTOR_BUILTIN_CERT,
        SOURCE_ENTROPY_ATOM_CERT,
        SOURCE_SURVIVAL_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def joint_field_basis() -> str:
    """返回 joint declaration 的完整生产性字段基。"""
    return f"{JOINT_DECL} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}"


def fresh_joint_field_basis() -> str:
    """返回禁止 constructor-payload 回环后的新鲜 joint 字段基。"""
    return f"{FRESH_JOINT_DECL} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}"


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    return (
        f"(({ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_MULT} "
        f"AND {ROW_MASS} AND {FRESH_JOINT_DECL}) OR {CANONICAL_LOCK} "
        f"OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {POINTWISE_TABLE} "
        f"OR {EXTERNAL_DIBFI}) AND {SIGNED_SURVIVAL} AND {COMPLETE_KEY} "
        f"AND {FIXED_KEY_MULT} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} "
        f"AND {DSTRUCTURE}"
    )


def loop_edges() -> list[dict[str, str]]:
    """列出被切掉的 constructor payload 自证环。"""
    return [
        {
            "from": JOINT_DECL,
            "to": BUILTIN_PAIRING,
            "meaning": "constructor joint-declaration antisplit 同步把 joint declaration 接到 built-in pairing。",
        },
        {
            "from": BUILTIN_PAIRING,
            "to": NEW_PAYLOAD,
            "meaning": "constructor built-in trace 同步把 built-in pairing 接到 new primitive payload。",
        },
        {
            "from": NEW_PAYLOAD,
            "to": DOMAIN_ENTROPY,
            "meaning": "constructor new-payload/source-atom 同步要求 actual source-domain entropy。",
        },
        {
            "from": DOMAIN_ENTROPY,
            "to": CYCLE_OR_TERMINAL,
            "meaning": "strict source-entropy downstream 把 source entropy 展开到 cycle-cut 或 terminal descent。",
        },
        {
            "from": CYCLE_OR_TERMINAL,
            "to": JOINT_DECL,
            "meaning": "strict cycle-cut/terminal/PDEC 统一前沿回到 joint declaration line。",
        },
    ]


def build_rows(
    current_source: dict[str, Any],
    old_loop: dict[str, Any],
    source_downstream: dict[str, Any],
    unified: dict[str, Any],
    triad: dict[str, Any],
    joint_decl: dict[str, Any],
    builtin: dict[str, Any],
    entropy_atom: dict[str, Any],
    survival: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 source-entropy payload-loop cut rebase 判定表。"""
    current_entropy_imported = (
        current_source.get("next_primary_attack_target") == DOMAIN_ENTROPY
        and current_source.get("actual_source_domain_entropy_proved") is False
    )
    old_loop_reusable = (
        old_loop.get("target_input_before_router") == DOMAIN_ENTROPY
        and old_loop.get("constructor_payload_source_entropy_loop_detected") is True
        and old_loop.get("next_primary_attack_target") == FRESH_JOINT_DECL
    )
    entropy_to_cycle_or_terminal = (
        source_downstream.get("next_direct_attack_target") == CYCLE_OR_TERMINAL
        and source_downstream.get("source_entropy_downstream_edges_closed") is True
    )
    cycle_terminal_to_joint = (
        unified.get("next_direct_attack_target") == JOINT_DECL
        and unified.get("new_joint_formula_reduced_to_declaration_line") is True
    )
    upstream_joint_to_payload = (
        triad.get("next_primary_attack_target") == JOINT_DECL
        and joint_decl.get("target_input_before_router") == JOINT_DECL
        and joint_decl.get("next_primary_attack_target") == BUILTIN_PAIRING
        and builtin.get("target_input_before_router") == BUILTIN_PAIRING
        and builtin.get("next_primary_attack_target") == NEW_PAYLOAD
    )
    loop_detected = (
        current_entropy_imported
        and old_loop_reusable
        and entropy_to_cycle_or_terminal
        and cycle_terminal_to_joint
        and upstream_joint_to_payload
    )
    return [
        row(
            "LatestRebasedSourceEntropyImported",
            current_entropy_imported,
            False,
            "上一层 rebase 已把第一硬点压到 actual source-domain entropy。",
            DOMAIN_ENTROPY,
        ),
        row(
            "ExistingConstructorPayloadLoopCutReusable",
            old_loop_reusable,
            False,
            "旧 constructor source-entropy payload-loop cut 输入相同，可在新 rebase 前沿复用。",
            FRESH_JOINT_DECL,
        ),
        row(
            "SourceEntropyAtomBoundaryCarried",
            entropy_atom.get("actual_source_domain_entropy_atomization_closed") is True,
            True,
            "source entropy 原子化只给 signed row-mass entropy 包，不证明 signed law、row-mass 或 row support。",
            f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "PhiLPFCandidateCapacityStillUnsigned",
            survival.get("candidate_rows_are_actual_signed_rows") is False,
            True,
            "LPF/Phi 桶恒等式支付候选容量，但候选 row 仍不是 actual signed row。",
            SIGNED_SURVIVAL,
        ),
        row(
            "StrictSourceEntropyDownstreamToCycleOrTerminal",
            entropy_to_cycle_or_terminal,
            False,
            "沿 strict source-entropy downstream 展开，source entropy 进入 cycle-cut 或 terminal descent 二出口。",
            f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
        ),
        row(
            "CycleOrTerminalUnifiedToJointDeclaration",
            cycle_terminal_to_joint,
            False,
            "cycle-cut、terminal descent 与 PDEC 内部分支在现有 strict 语料中统一回 joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "ConstructorUpstreamJointToPayloadChainImported",
            upstream_joint_to_payload,
            False,
            "constructor 上游已经使用 joint declaration 到 built-in pairing 再到 new payload 的链。",
            f"{JOINT_DECL} -> {BUILTIN_PAIRING} -> {NEW_PAYLOAD}",
        ),
        row(
            "ConstructorPayloadSourceEntropyLoopDetected",
            loop_detected,
            True,
            "若用当前 constructor 语料证明 source entropy，会形成 joint declaration -> payload -> source entropy -> joint declaration 的自证环。",
            "constructor-loop cut",
        ),
        row(
            "RawConstructorPayloadLoopCountsAsClosure",
            False,
            False,
            "该回环只说明接口相互依赖，不能作为非循环证明或全局矛盾。",
            FRESH_JOINT_DECL,
        ),
        row(
            "FreshJointDeclarationOutsideLoopCurrentCorpusProved",
            False,
            False,
            "当前语料没有提交不经 constructor payload/source-entropy 回环的独立 joint declaration line。",
            fresh_joint_field_basis(),
        ),
        row(
            "CanonicalLockOrIndependentBridgeStillOpen",
            False,
            False,
            "terminal 宏循环仍可由 canonical-lock 或 independent source bridge 打破，但当前都未证明。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}",
        ),
        row(
            "CompleteFixedKeyAndSignedMassStillParallel",
            False,
            False,
            "complete key、fixed-key multiplicity、signed survival 与 row-mass/no-heavy-row 仍是独立守门项。",
            f"{COMPLETE_KEY} AND {FIXED_KEY_MULT} AND {SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只做 rebase 同步并切掉 constructor payload/source-entropy 自证环；未证明三命题无条件闭合。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    current_source = load_json(CURRENT_SOURCE_ATOM_REBASE_CERT)
    old_loop = load_json(OLD_CONSTRUCTOR_LOOP_CERT)
    source_downstream = load_json(STRICT_SOURCE_ENTROPY_DOWNSTREAM_CERT)
    unified = load_json(STRICT_UNIFIED_FRONTIER_CERT)
    triad = load_json(CONSTRUCTOR_TRIAD_CERT)
    joint_decl = load_json(CONSTRUCTOR_JOINT_DECL_CERT)
    builtin = load_json(CONSTRUCTOR_BUILTIN_CERT)
    entropy_atom = load_json(SOURCE_ENTROPY_ATOM_CERT)
    survival = load_json(SOURCE_SURVIVAL_CERT)
    rows = build_rows(
        current_source,
        old_loop,
        source_downstream,
        unified,
        triad,
        joint_decl,
        builtin,
        entropy_atom,
        survival,
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_source_entropy_payload_loop_cut_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_source_entropy_payload_loop_cut_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_rebased_source_entropy_imported": rows[0]["closed"],
        "existing_constructor_payload_loop_cut_reusable": rows[1]["closed"],
        "source_entropy_atom_boundary_carried": rows[2]["closed"],
        "phi_lpf_candidate_capacity_still_unsigned": rows[3]["closed"],
        "strict_source_entropy_downstream_to_cycle_or_terminal": rows[4]["closed"],
        "cycle_or_terminal_unified_to_joint_declaration": rows[5]["closed"],
        "constructor_upstream_joint_to_payload_chain_imported": rows[6]["closed"],
        "constructor_payload_source_entropy_loop_detected": rows[7]["closed"],
        "raw_constructor_payload_loop_counts_as_closure": False,
        "fresh_joint_declaration_outside_loop_proved": False,
        "canonical_lock_proved": False,
        "independent_actual_source_bridge_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": DOMAIN_ENTROPY,
        "absorbed_loop_back_to": JOINT_DECL,
        "next_primary_attack_target": FRESH_JOINT_DECL,
        "productive_joint_atom_underlying_target": JOINT_DECL,
        "constructor_payload_loop_edges": loop_edges(),
        "latest_joint_field_basis": joint_field_basis(),
        "fresh_joint_field_basis": fresh_joint_field_basis(),
        "latest_retained_basis_after_router": retained_basis(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 rebase 后的 constructor `ActualPreCauchySourceDomainAbsoluteEntropyLedger` "
            "沿 strict source-entropy downstream 与 cycle-cut/terminal/PDEC 统一前沿展开。展开后回到 "
            "`PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple`；"
            "而该 joint declaration 正是 constructor 上游推出 built-in pairing、new payload 和 source entropy 的入口。"
            "因此当前 constructor 内部路线形成 payload/source-entropy 自证环，不能作为闭合证明；"
            "非循环推进必须提交不经该回环的新鲜独立 joint declaration。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor source-entropy payload-loop cut rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_rebased_source_entropy_imported={fmt_bool(result['latest_rebased_source_entropy_imported'])}",
        f"existing_constructor_payload_loop_cut_reusable={fmt_bool(result['existing_constructor_payload_loop_cut_reusable'])}",
        f"source_entropy_atom_boundary_carried={fmt_bool(result['source_entropy_atom_boundary_carried'])}",
        f"phi_lpf_candidate_capacity_still_unsigned={fmt_bool(result['phi_lpf_candidate_capacity_still_unsigned'])}",
        f"strict_source_entropy_downstream_to_cycle_or_terminal={fmt_bool(result['strict_source_entropy_downstream_to_cycle_or_terminal'])}",
        f"cycle_or_terminal_unified_to_joint_declaration={fmt_bool(result['cycle_or_terminal_unified_to_joint_declaration'])}",
        f"constructor_upstream_joint_to_payload_chain_imported={fmt_bool(result['constructor_upstream_joint_to_payload_chain_imported'])}",
        f"constructor_payload_source_entropy_loop_detected={fmt_bool(result['constructor_payload_source_entropy_loop_detected'])}",
        f"raw_constructor_payload_loop_counts_as_closure={fmt_bool(result['raw_constructor_payload_loop_counts_as_closure'])}",
        f"fresh_joint_declaration_outside_loop_proved={fmt_bool(result['fresh_joint_declaration_outside_loop_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 被切掉的 constructor payload 回环",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["constructor_payload_loop_edges"]:
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
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新非循环主攻",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "底层 joint 原子仍是：",
            "",
            "```text",
            result["productive_joint_atom_underlying_target"],
            "```",
            "",
            "完整 joint 字段基：",
            "",
            "```text",
            result["fresh_joint_field_basis"],
            "```",
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
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
