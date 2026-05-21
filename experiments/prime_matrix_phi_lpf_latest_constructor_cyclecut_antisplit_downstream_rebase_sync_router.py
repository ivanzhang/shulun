#!/usr/bin/env python3
"""生成 latest constructor cycle-cut/antisplit downstream rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_cyclecut_antisplit_downstream_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-cyclecut-antisplit-downstream-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-cyclecut-antisplit-downstream-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-cyclecut-antisplit-downstream-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-cyclecut-antisplit-downstream-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-cyclecut-antisplit-downstream-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_MACROCYCLE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-router.json"
)
SEED_CYCLE_SATURATION_CERT = DOCS / "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"
STRICT_UNIFIED_FRONTIER_CERT = DOCS / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json"
STRICT_ANTISPLIT_DOWNSTREAM_CERT = DOCS / "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json"
STRICT_HIGH_TAIL_CERT = DOCS / "prime-matrix-strict-high-model-tail-update-router.json"

SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_PRIMITIVE = "NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle"
EXTERNAL_KZ = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
SOURCE_EXACTUV = f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"
BETA_APPENDIX = "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix"
BETA_99 = "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000"
SAWTOOTH = "ExactResidueWeightedFloorSawtoothTenPercentBound"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失依赖不能当成闭合。"""
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
        LATEST_MACROCYCLE_CERT,
        SEED_CYCLE_SATURATION_CERT,
        STRICT_UNIFIED_FRONTIER_CERT,
        STRICT_ANTISPLIT_DOWNSTREAM_CERT,
        STRICT_HIGH_TAIL_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def tail_package() -> str:
    """给出高段模型余量的严格自足尾包。"""
    return f"{BETA_APPENDIX} AND {BETA_99} AND {SAWTOOTH}"


def internal_downstream_basis() -> str:
    """给出反分裂下游后的内部基。"""
    return f"{BUILTIN_PAIRING} AND {SOURCE_EXACTUV}"


def latest_internal_basis() -> str:
    """给出 latest constructor 当前内部非循环基。"""
    return f"{internal_downstream_basis()} AND {tail_package()} AND {RATE} AND {DSTRUCTURE}"


def retained_basis() -> str:
    """给出保留旁路线后的 latest constructor 基。"""
    alternatives = (
        f"{internal_downstream_basis()} OR {PDEC_SCOPE} OR {NEW_PRIMITIVE} "
        f"OR {EXTERNAL_KZ} OR {NEW_JOINT} OR {JOINT_DECL}"
    )
    return (
        f"(({alternatives}) AND {tail_package()}) AND {RATE} AND {DSTRUCTURE} "
        f"AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {SIGNED_SURVIVAL} AND {ROW_MASS}"
    )


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 cycle-cut/antisplit downstream rebase 判定表。"""
    latest = data["latest"]
    seed = data["seed"]
    unified = data["unified"]
    downstream = data["downstream"]
    high_tail = data["high_tail"]

    latest_seed_active = (
        latest.get("next_primary_attack_target") == SEED_CYCLE_CUT
        and latest.get("acyclic_seed_cycle_cut_primitive_basis_and_coefficient_source_input_proved") is False
    )
    seed_saturated = (
        seed.get("seed_cycle_cut_branch_saturated") is True
        and seed.get("seed_cycle_cut_source_input_proved") is False
    )
    unified_to_decl = (
        unified.get("next_direct_attack_target") == JOINT_DECL
        and unified.get("pre_cauchy_joint_declaration_line_proved") is False
    )
    antisplit_to_pairing = (
        downstream.get("next_direct_attack_target") == BUILTIN_PAIRING
        and downstream.get("built_in_signed_pairing_proved") is False
    )
    exactuv_split = (
        downstream.get("parallel_direct_attack_target") == SOURCE_EXACTUV
        and downstream.get("actual_emitter_source_domain_entropy_proved") is False
        and downstream.get("exact_uv_map_fixed_pair_polylog_fiber_bound_proved") is False
    )
    finite_bridge_boundary = (
        high_tail.get("dynamic_skeleton_finite_bridge_closed_imported") is True
        and high_tail.get("terminal_gap_after_router") == tail_package()
    )
    tail_still_open = (
        high_tail.get("self_contained_beta_sieve_appendix_proved") is False
        and high_tail.get("beta_sieve_main_coefficient_99_proved") is False
        and high_tail.get("exact_residue_weighted_floor_sawtooth_bound_proved") is False
    )
    rebase_closed = all(
        [
            latest_seed_active,
            seed_saturated,
            unified_to_decl,
            antisplit_to_pairing,
            exactuv_split,
            finite_bridge_boundary,
        ]
    )

    return [
        row(
            "LatestConstructorSeedCycleCutImported",
            latest_seed_active,
            False,
            "上一层 latest constructor 的首攻点是 seed cycle-cut 输入加高段尾包。",
            SEED_CYCLE_CUT,
        ),
        row(
            "SeedCycleCutBranchSaturated",
            seed_saturated,
            False,
            "seed cycle-cut 顺序拆分已被排除；联合 emitter 路线回到 row-level 固定点或 PDEC/new-joint。",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "CyclecutTerminalUnifiedToJointDeclaration",
            unified_to_decl,
            False,
            "cycle-cut、terminal descent 与 PDEC 内部分支统一压到 pre-Cauchy joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "OrdinaryJointRouteRejectedByAntiSplitDownstream",
            downstream.get("ordinary_joint_declaration_route_rejected_as_nonproof") is True,
            True,
            "普通 joint declaration/constructor 继续展开会回到 signed-source 固定点，不能作为非循环证明。",
            "Atomic anti-split joint rows route",
        ),
        row(
            "AtomicRowsReducedToBuiltInPairing",
            antisplit_to_pairing,
            False,
            "反分裂 atomic rows 的首个 signed 缺口是内置 signed coefficient/pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberSplitImported",
            exactuv_split,
            False,
            "ExactUV bounded incidence 并行拆成 source-domain entropy 与 fixed-pair polylog fiber bound。",
            SOURCE_EXACTUV,
        ),
        row(
            "ThresholdFiniteVerificationBoundaryPreserved",
            finite_bridge_boundary,
            True,
            "高阈值加有限验证只关闭已登记有限桥；尾段仍是 beta-sieve/sawtooth 自足包。",
            tail_package(),
        ),
        row(
            "BetaSieveSawtoothTailStillOpen",
            tail_still_open,
            False,
            "Rosser-Iwaniec beta-sieve 构造、99% 主系数与 exact sawtooth 仍未证明。",
            tail_package(),
        ),
        row(
            "LatestInternalRouteReducedToBuiltinPairingAndExactUV",
            rebase_closed,
            False,
            "latest constructor 的 cycle-cut 主攻已继续压到 built-in signed pairing 与 ExactUV entropy/fiber 并行门。",
            latest_internal_basis(),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 cycle-cut 下游；没有证明 built-in pairing、ExactUV entropy/fiber、beta-sieve/sawtooth、Rate 或 DStructure。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "latest": load_json(LATEST_MACROCYCLE_CERT),
        "seed": load_json(SEED_CYCLE_SATURATION_CERT),
        "unified": load_json(STRICT_UNIFIED_FRONTIER_CERT),
        "downstream": load_json(STRICT_ANTISPLIT_DOWNSTREAM_CERT),
        "high_tail": load_json(STRICT_HIGH_TAIL_CERT),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_cyclecut_antisplit_downstream_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_cyclecut_antisplit_downstream_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_constructor_seed_cyclecut_imported": rows[0]["closed"],
        "seed_cycle_cut_branch_saturated": rows[1]["closed"],
        "cyclecut_terminal_unified_to_joint_declaration": rows[2]["closed"],
        "ordinary_joint_route_rejected_by_antisplit_downstream": rows[3]["closed"],
        "atomic_rows_reduced_to_builtin_pairing": rows[4]["closed"],
        "exactuv_entropy_fiber_split_imported": rows[5]["closed"],
        "threshold_finite_verification_boundary_preserved": rows[6]["closed"],
        "beta_sieve_sawtooth_tail_still_open": rows[7]["closed"],
        "latest_internal_route_reduced_to_builtin_pairing_and_exactuv": rows[8]["closed"],
        "built_in_signed_pairing_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": f"{SEED_CYCLE_CUT} AND {tail_package()}",
        "absorbed_to": latest_internal_basis(),
        "latest_internal_basis_after_router": latest_internal_basis(),
        "latest_retained_basis_after_router": retained_basis(),
        "next_primary_attack_target": BUILTIN_PAIRING,
        "parallel_primary_attack_target": SOURCE_EXACTUV,
        "next_direct_attack_target": (
            f"{BUILTIN_PAIRING} AND {SOURCE_ENTROPY}_AND_{FIXED_FIBER} "
            f"AND {BETA_APPENDIX}_THEN_ExactSawtooth"
        ),
        "parallel_attack_targets": [
            SOURCE_ENTROPY,
            FIXED_FIBER,
            PDEC_SCOPE,
            NEW_PRIMITIVE,
            EXTERNAL_KZ,
            NEW_JOINT,
            BETA_APPENDIX,
            BETA_99,
            SAWTOOTH,
            RATE,
            DSTRUCTURE,
            JOINT_ROWS,
            JOINT_IDENTITY,
            JOINT_RETURN,
            COMPLETE_KEY,
            FIXED_KEY,
            SIGNED_SURVIVAL,
            ROW_MASS,
        ],
        "structural_chain": [
            f"{SEED_CYCLE_CUT} AND {tail_package()}",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
            JOINT_DECL,
            "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing",
            f"{BUILTIN_PAIRING} AND {SOURCE_EXACTUV}",
            f"{internal_downstream_basis()} AND {tail_package()}",
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor 的 seed cycle-cut 主攻接入 strict seed-cycle-cut 饱和、"
            "cycle-cut/terminal 统一前沿与反分裂下游同步。seed cycle-cut 不能作为独立出口；"
            "普通 joint declaration/constructor 会回到 signed-source 固定点，真正下游首口是 "
            "built-in signed coefficient pairing，且 ExactUV source entropy/fixed fiber 是并行门。"
            "高阈值加有限验证仍只关闭有限桥；尾段继续需要 beta-sieve、99% 主系数和 exact sawtooth。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor cycle-cut/antisplit downstream rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_seed_cyclecut_imported={fmt_bool(result['latest_constructor_seed_cyclecut_imported'])}",
        f"seed_cycle_cut_branch_saturated={fmt_bool(result['seed_cycle_cut_branch_saturated'])}",
        f"cyclecut_terminal_unified_to_joint_declaration={fmt_bool(result['cyclecut_terminal_unified_to_joint_declaration'])}",
        f"ordinary_joint_route_rejected_by_antisplit_downstream={fmt_bool(result['ordinary_joint_route_rejected_by_antisplit_downstream'])}",
        f"atomic_rows_reduced_to_builtin_pairing={fmt_bool(result['atomic_rows_reduced_to_builtin_pairing'])}",
        f"exactuv_entropy_fiber_split_imported={fmt_bool(result['exactuv_entropy_fiber_split_imported'])}",
        f"threshold_finite_verification_boundary_preserved={fmt_bool(result['threshold_finite_verification_boundary_preserved'])}",
        f"beta_sieve_sawtooth_tail_still_open={fmt_bool(result['beta_sieve_sawtooth_tail_still_open'])}",
        f"latest_internal_route_reduced_to_builtin_pairing_and_exactuv={fmt_bool(result['latest_internal_route_reduced_to_builtin_pairing_and_exactuv'])}",
        f"built_in_signed_pairing_proved={fmt_bool(result['built_in_signed_pairing_proved'])}",
        f"actual_emitter_source_domain_entropy_proved={fmt_bool(result['actual_emitter_source_domain_entropy_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"self_contained_beta_sieve_appendix_proved={fmt_bool(result['self_contained_beta_sieve_appendix_proved'])}",
        f"exact_residue_weighted_floor_sawtooth_bound_proved={fmt_bool(result['exact_residue_weighted_floor_sawtooth_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
        "\n".join(result["structural_chain"]),
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新内部基",
            "",
            "```text",
            result["latest_internal_basis_after_router"],
            "```",
            "",
            "## 4. 保留条件基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
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
