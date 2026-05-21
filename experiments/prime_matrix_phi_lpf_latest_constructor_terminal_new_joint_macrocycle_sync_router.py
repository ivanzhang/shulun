#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor terminal new-joint macrocycle 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_terminal_new_joint_macrocycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-new-joint-macrocycle-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-terminal-new-joint-macrocycle-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-new-joint-macrocycle-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-new-joint-macrocycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-terminal-new-joint-macrocycle-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

TERMINAL_FAMILY_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-terminal-family-saturation-sync-router.json"
)
TRIAD_CERT = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.json"
DECL_ANTISPLIT_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-router.json"
)
MACROCYCLE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync-router.json"
)
SOURCE_LOOP_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-sync-router.json"
)

SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
ROW_LEVEL = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
SOURCE_EXACTUV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
HARMONIC = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
TERMINAL_WFD = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典，避免误判为已证。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
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
    """返回本层依赖证书。"""
    return [
        TERMINAL_FAMILY_CERT,
        TRIAD_CERT,
        DECL_ANTISPLIT_CERT,
        MACROCYCLE_CERT,
        SOURCE_LOOP_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def signed_side_gate() -> str:
    """给出删除 new-joint 宏循环后的 mandatory signed 侧门。"""
    return f"{ROW_LEVEL} AND {SIGNED_SURVIVAL} AND {ROW_MASS}"


def constructor_new_joint_absorber() -> str:
    """给出当前 constructor 线中 new-joint 的实际吸收目标。"""
    return f"{SEED} AND ({PDEC_SCOPE} OR ({signed_side_gate()})) AND {HARMONIC} AND {SKELETON} AND {DSTRUCTURE}"


def retained_parallel_basis() -> str:
    """给出本层同步后的最新保留基。"""
    return (
        f"{constructor_new_joint_absorber()} AND {RATE} AND {JOINT_ROWS} AND "
        f"{JOINT_IDENTITY} AND {JOINT_RETURN} AND {SOURCE_EXACTUV} AND "
        f"{COMPLETE_KEY} AND {FIXED_KEY}"
    )


def build_rows(
    terminal: dict[str, Any],
    triad: dict[str, Any],
    decl: dict[str, Any],
    macro: dict[str, Any],
    source_loop: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 terminal new-joint macrocycle 同步判定表。"""
    terminal_new_joint_active = (
        terminal.get("next_primary_attack_target") == NEW_JOINT
        and terminal.get("constructor_terminal_family_unnamed_exit_removed") is True
    )
    new_joint_to_declaration = (
        triad.get("new_joint_reduced_to_declaration_line_imported") is True
        and triad.get("absorbed_to") == JOINT_DECL
    )
    declaration_to_builtin = (
        decl.get("ordinary_constructor_route_rejected_as_fixed_point") is True
        and decl.get("atomic_rows_reduced_to_builtin_pairing") is True
        and decl.get("absorbed_to") == BUILTIN_PAIRING
    )
    builtin_macrocycle_cut = (
        macro.get("constructor_signed_macrocycle_closed") is True
        and macro.get("constructor_macrocycle_self_proof_rejected") is True
        and macro.get("next_primary_attack_target") == ROW_LEVEL
    )
    source_payload_loop_carried = (
        source_loop.get("constructor_payload_source_entropy_loop_detected") is True
        and source_loop.get("raw_constructor_payload_loop_counts_as_closure") is False
    )
    signed_side_mandatory = (
        macro.get("signed_survival_gate_mandatory_in_latest_basis") is True
        and macro.get("signed_survival_reduced_to_row_level_origin_table") is True
    )
    new_joint_coarse_exit_removed = (
        terminal_new_joint_active
        and new_joint_to_declaration
        and declaration_to_builtin
        and builtin_macrocycle_cut
        and source_payload_loop_carried
        and signed_side_mandatory
    )

    return [
        row(
            "TerminalFamilyNewJointTargetImported",
            terminal_new_joint_active,
            False,
            "上一层 constructor terminal-family saturation 把内部主攻钉到 new-joint 显式公式。",
            NEW_JOINT,
        ),
        row(
            "NewJointToDeclarationLineImported",
            new_joint_to_declaration,
            False,
            "constructor triad 统一层显示 new-joint 的第一生产性字段是 pre-Cauchy joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "DeclarationAntisplitToBuiltinImported",
            declaration_to_builtin,
            False,
            "普通 declaration 展开回到 signed-source 固定点；anti-split 路线把首个 signed 缺口压到 built-in pairing。",
            BUILTIN_PAIRING,
        ),
        row(
            "BuiltInMacrocycleCutImported",
            builtin_macrocycle_cut,
            False,
            "built-in -> new payload -> alpha kernel -> moving atom -> signed table -> origin -> triad -> declaration -> built-in 构成宏循环。",
            ROW_LEVEL,
        ),
        row(
            "SourcePayloadLoopCarried",
            source_payload_loop_carried,
            True,
            "source entropy/payload 旧路线也已登记为 declaration -> payload -> source entropy -> declaration 自证环。",
            "FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop",
        ),
        row(
            "MandatorySignedSideGateImported",
            signed_side_mandatory,
            False,
            "删除环内自证后，mandatory signed 侧门同步为 row-level clean-core origin table、signed survival 和 row-mass。",
            signed_side_gate(),
        ),
        row(
            "NewJointCoarseArtifactRemoved",
            new_joint_coarse_exit_removed,
            False,
            "constructor 线中 new-joint 不再作为粗原子停留；它同步到 row-level/signed-side 侧门或 PDEC scope。",
            f"{PDEC_SCOPE} OR ({signed_side_gate()})",
        ),
        row(
            "PDECScopeConditionalBranchRetained",
            True,
            False,
            "PDEC same-set scope 仍可作为新 scope 证书或外部/条件性输入保留，本层不把它当已证。",
            f"{PDEC_SCOPE} OR {EXTERNAL_DIBFI}",
        ),
        row(
            "TerminalAlternativeBranchesStillParallel",
            True,
            False,
            "canonical lock、independent bridge、terminal WFD 和逐点 signed table 仍是并行出口。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {TERMINAL_WFD} OR {POINTWISE_TABLE}",
        ),
        row(
            "TailAndConstructorSiblingFieldsStillParallel",
            True,
            False,
            "本层不证明 harmonic/skeleton、joint rows、identity、return、ExactUV/source entropy、key、Rate 或 DStructure。",
            (
                f"{HARMONIC} AND {SKELETON} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND "
                f"{JOINT_RETURN} AND {SOURCE_EXACTUV} AND {COMPLETE_KEY} AND {FIXED_KEY} "
                f"AND {RATE} AND {DSTRUCTURE}"
            ),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只切除 terminal new-joint 宏循环，没有给出无条件全局矛盾。",
            retained_parallel_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    terminal = load_json(TERMINAL_FAMILY_CERT)
    triad = load_json(TRIAD_CERT)
    decl = load_json(DECL_ANTISPLIT_CERT)
    macro = load_json(MACROCYCLE_CERT)
    source_loop = load_json(SOURCE_LOOP_CERT)
    rows = build_rows(terminal, triad, decl, macro, source_loop)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_terminal_new_joint_macrocycle_sync_router",
        "status": "phi_lpf_latest_constructor_terminal_new_joint_macrocycle_cut_to_row_level_signed_side_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "terminal_family_new_joint_target_imported": rows[0]["closed"],
        "new_joint_to_declaration_line_imported": rows[1]["closed"],
        "declaration_antisplit_to_builtin_imported": rows[2]["closed"],
        "builtin_macrocycle_cut_imported": rows[3]["closed"],
        "source_payload_loop_carried": rows[4]["closed"],
        "mandatory_signed_side_gate_imported": rows[5]["closed"],
        "new_joint_coarse_artifact_removed": rows[6]["closed"],
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "row_level_clean_core_origin_generation_table_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "tail_harmonic_upper_0850_proved": False,
        "tail_skeleton_lower_401_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": NEW_JOINT,
        "absorbed_to": constructor_new_joint_absorber(),
        "next_primary_attack_target": ROW_LEVEL,
        "conditional_scope_or_external_target_retained": f"{PDEC_SCOPE} OR {EXTERNAL_DIBFI}",
        "parallel_attack_targets": [
            SEED,
            PDEC_SCOPE,
            SIGNED_SURVIVAL,
            ROW_MASS,
            HARMONIC,
            SKELETON,
            DSTRUCTURE,
            RATE,
            JOINT_ROWS,
            JOINT_IDENTITY,
            JOINT_RETURN,
            SOURCE_EXACTUV,
            COMPLETE_KEY,
            FIXED_KEY,
            CANONICAL_LOCK,
            INDEPENDENT_BRIDGE,
            TERMINAL_WFD,
            POINTWISE_TABLE,
        ],
        "latest_retained_basis_after_router": retained_parallel_basis(),
        "sync_chain": [
            NEW_JOINT,
            JOINT_DECL,
            BUILTIN_PAIRING,
            "constructor signed macrocycle",
            signed_side_gate(),
            constructor_new_joint_absorber(),
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 terminal-family saturation 后的 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` "
            "接入已有 constructor new-joint 下游。new-joint 的第一生产性字段是 pre-Cauchy joint declaration line；"
            "ordinary declaration 会回到 signed-source 固定点，anti-split 路线又压到 built-in signed pairing。"
            "已有 constructor macrocycle 证书显示 built-in -> payload -> alpha kernel -> moving atom -> signed table -> "
            "origin -> triad -> declaration -> built-in 是自证环，source-entropy/payload 线也回到同一 declaration 环。"
            "因此本层删除 new-joint 粗原子，把内部主攻压到 row-level clean-core origin table，并强制并行保留 "
            "signed survival 与 row-mass/no-heavy-row。PDEC scope、canonical lock、independent bridge、ExactUV、"
            "harmonic/skeleton、Rate、DStructure 和 constructor 兄弟字段仍开放；行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor terminal new-joint macrocycle sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_family_new_joint_target_imported={fmt_bool(result['terminal_family_new_joint_target_imported'])}",
        f"new_joint_to_declaration_line_imported={fmt_bool(result['new_joint_to_declaration_line_imported'])}",
        f"declaration_antisplit_to_builtin_imported={fmt_bool(result['declaration_antisplit_to_builtin_imported'])}",
        f"builtin_macrocycle_cut_imported={fmt_bool(result['builtin_macrocycle_cut_imported'])}",
        f"source_payload_loop_carried={fmt_bool(result['source_payload_loop_carried'])}",
        f"mandatory_signed_side_gate_imported={fmt_bool(result['mandatory_signed_side_gate_imported'])}",
        f"new_joint_coarse_artifact_removed={fmt_bool(result['new_joint_coarse_artifact_removed'])}",
        f"row_level_clean_core_origin_generation_table_proved={fmt_bool(result['row_level_clean_core_origin_generation_table_proved'])}",
        f"nonzero_signed_row_survival_proved={fmt_bool(result['nonzero_signed_row_survival_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(result['same_formal_unit_row_mass_normalization_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
    ]
    lines.extend(result["sync_chain"])
    lines.extend(
        [
            "```",
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
            "## 3. 最新保留基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
            "```",
            "",
            "下一内部主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "条件性 scope/外部输入仍保留：",
            "",
            "```text",
            result["conditional_scope_or_external_target_retained"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 4. 依赖哈希",
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
