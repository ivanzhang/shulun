#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor terminal-family saturation 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_terminal_family_saturation_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-family-saturation-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-terminal-family-saturation-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-family-saturation-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-family-saturation-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-terminal-family-saturation-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CONSTRUCTOR_KZ_CYCLE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync-router.json"
)
STRICT_TERMINAL_FAMILY_CERT = (
    DOCS / "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json"
)
NONRECURSIVE_BREAKER_CERT = (
    DOCS / "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json"
)
SEED_CYCLE_CERT = DOCS / "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"
PDEC_SCOPE_CERT = DOCS / "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
GLOBAL_CRT_CERT = DOCS / "prime-matrix-global-crt-terminal-saturation-sync-router.json"

TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
NONRECURSIVE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
HARMONIC = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
SOURCE_EXACTUV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典，避免把缺失误当证明。"""
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
        CONSTRUCTOR_KZ_CYCLE_CERT,
        STRICT_TERMINAL_FAMILY_CERT,
        NONRECURSIVE_BREAKER_CERT,
        SEED_CYCLE_CERT,
        PDEC_SCOPE_CERT,
        GLOBAL_CRT_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def pdec_or_new_joint_basis() -> str:
    """给出当前内部语料下的终端饱和破环前沿。"""
    return f"{PDEC_SCOPE} OR {NEW_JOINT}"


def constructor_terminal_saturated_basis() -> str:
    """给出 constructor KZ 回流后保留的最新显式基。"""
    return (
        f"{SEED} AND ({pdec_or_new_joint_basis()}) AND {HARMONIC} AND {SKELETON} "
        f"AND {DSTRUCTURE}"
    )


def retained_parallel_basis() -> str:
    """给出 constructor 语境下仍并行保留的全部硬点。"""
    return (
        f"{constructor_terminal_saturated_basis()} AND {RATE} AND {JOINT_ROWS} "
        f"AND {JOINT_IDENTITY} AND {JOINT_RETURN} AND {SOURCE_EXACTUV} "
        f"AND {SIGNED_SURVIVAL} AND {ROW_MASS} AND {COMPLETE_KEY} AND {FIXED_KEY}"
    )


def build_rows(
    constructor_kz: dict[str, Any],
    terminal_family: dict[str, Any],
    nonrecursive: dict[str, Any],
    seed_cycle: dict[str, Any],
    pdec_scope: dict[str, Any],
    global_crt: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 constructor terminal-family saturation 同步判定表。"""
    constructor_terminal_active = (
        constructor_kz.get("next_primary_attack_target") == TERMINAL_FAMILY
        and constructor_kz.get("constructor_kuznetsov_independent_exit_removed") is True
    )
    terminal_family_saturated = (
        terminal_family.get("terminal_gap_before_router") == TERMINAL_FAMILY
        and terminal_family.get("strict_terminal_family_gate_active") is True
        and terminal_family.get("three_atom_split_imported") is True
        and terminal_family.get("internal_terminal_cycle_obstruction_closed") is True
    )
    terminal_family_not_proved = terminal_family.get("strict_acyclic_terminal_family_proved") is False
    nonrecursive_cycle = (
        nonrecursive.get("latest_terminal_primary_target") == NONRECURSIVE_BREAKER
        and nonrecursive.get("current_chain_contains_nonproof_cycle") is True
        and nonrecursive.get("nonrecursive_breaker_package_proved") is False
    )
    seed_cycle_saturated = (
        seed_cycle.get("seed_cycle_cut_branch_saturated") is True
        and seed_cycle.get("next_direct_attack_target")
        == f"{PDEC_SCOPE}_OR_{NEW_JOINT}"
    )
    pdec_scope_saturated = (
        pdec_scope.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
        and pdec_scope.get("next_direct_attack_target") == NEW_JOINT
    )
    global_crt_agrees = (
        global_crt.get("pdec_scope_branch_saturated") is True
        and global_crt.get("seed_cycle_cut_branch_saturated") is True
        and PDEC_SCOPE in global_crt.get("latest_strict_activity_basis", "")
        and NEW_JOINT in global_crt.get("latest_strict_activity_basis", "")
    )
    tail_inputs_carried = (
        constructor_kz.get("tail_harmonic_upper_0850_proved") is False
        and constructor_kz.get("tail_skeleton_lower_401_proved") is False
    )
    constructor_terminal_family_removed = (
        constructor_terminal_active
        and terminal_family_saturated
        and nonrecursive_cycle
        and seed_cycle_saturated
        and global_crt_agrees
    )

    return [
        row(
            "ConstructorTerminalFamilyTargetImported",
            constructor_terminal_active,
            False,
            "上一层 constructor KZ 回流把直接主攻钉到 acyclic noncanonical 终端家族。",
            TERMINAL_FAMILY,
        ),
        row(
            "StrictTerminalFamilyLatestSaturationImported",
            terminal_family_saturated,
            False,
            "strict 终端家族已拆成 canonical-lock、direct PDEC、CleanKLS/DLS 三手臂并显示内部循环。",
            f"{NONRECURSIVE_BREAKER} OR {PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "StrictTerminalFamilyStillUnproved",
            terminal_family_not_proved,
            False,
            "三手臂饱和只删除无名黑箱；没有证明 acyclic noncanonical 终端家族为空。",
            TERMINAL_FAMILY,
        ),
        row(
            "NonrecursiveBreakerCycleImported",
            nonrecursive_cycle,
            False,
            "非递归 constructor/signed-lift 破环包继续展开会落到 signed 坐标-来源闭环。",
            f"{SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "SeedCycleCutSaturationImported",
            seed_cycle_saturated,
            False,
            "seed-cycle-cut 分支已攻到联合发射器/row-level 固定点；不是独立闭合出口。",
            pdec_or_new_joint_basis(),
        ),
        row(
            "PDECScopeBranchInternalSaturationImported",
            pdec_scope_saturated,
            False,
            "PDEC same-set scope 仍可作为新 scope 证书或外部输入；当前内部语料中会压到 new-joint。",
            NEW_JOINT,
        ),
        row(
            "GlobalCRTSaturationAgrees",
            global_crt_agrees,
            False,
            "global CRT 饱和同步给出同一二分：PDEC same-set scope 或 new-joint 显式公式。",
            pdec_or_new_joint_basis(),
        ),
        row(
            "ConstructorSeedCarriedForward",
            True,
            False,
            "本层只攻击 terminal family；KZ-E 回流携带的 acyclic pre-Cauchy source seed 仍未证明。",
            SEED,
        ),
        row(
            "TailLedgersCarriedForward",
            tail_inputs_carried,
            False,
            "constructor KZ 回流后的 harmonic-window 与 rough-skeleton 两张尾账本继续保留。",
            f"{HARMONIC} AND {SKELETON}",
        ),
        row(
            "ConstructorTerminalFamilyUnnamedExitRemoved",
            constructor_terminal_family_removed,
            False,
            "constructor 语境下 terminal family 不能继续作为粗终端；它同步到 PDEC scope/new-joint 饱和前沿。",
            constructor_terminal_saturated_basis(),
        ),
        row(
            "ConstructorSiblingFieldsStillParallel",
            True,
            False,
            "本层不处理 joint rows、identity、return、ExactUV/source entropy、signed mass 与 key ledgers。",
            (
                f"{JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN} AND "
                f"{SOURCE_EXACTUV} AND {SIGNED_SURVIVAL} AND {ROW_MASS} AND "
                f"{COMPLETE_KEY} AND {FIXED_KEY}"
            ),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只完成终端家族饱和同步，没有给出排除反例链的无条件矛盾。",
            retained_parallel_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    constructor_kz = load_json(CONSTRUCTOR_KZ_CYCLE_CERT)
    terminal_family = load_json(STRICT_TERMINAL_FAMILY_CERT)
    nonrecursive = load_json(NONRECURSIVE_BREAKER_CERT)
    seed_cycle = load_json(SEED_CYCLE_CERT)
    pdec_scope = load_json(PDEC_SCOPE_CERT)
    global_crt = load_json(GLOBAL_CRT_CERT)
    rows = build_rows(
        constructor_kz,
        terminal_family,
        nonrecursive,
        seed_cycle,
        pdec_scope,
        global_crt,
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_terminal_family_saturation_sync_router",
        "status": "phi_lpf_latest_constructor_terminal_family_saturated_to_pdec_scope_or_new_joint_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "constructor_terminal_family_target_imported": rows[0]["closed"],
        "strict_terminal_family_latest_saturation_imported": rows[1]["closed"],
        "strict_terminal_family_still_unproved": rows[2]["closed"],
        "nonrecursive_breaker_cycle_imported": rows[3]["closed"],
        "seed_cycle_cut_saturation_imported": rows[4]["closed"],
        "pdec_scope_branch_internal_saturation_imported": rows[5]["closed"],
        "global_crt_saturation_agrees": rows[6]["closed"],
        "constructor_seed_carried_forward": rows[7]["closed"],
        "tail_ledgers_carried_forward": rows[8]["closed"],
        "constructor_terminal_family_unnamed_exit_removed": rows[9]["closed"],
        "strict_acyclic_terminal_family_proved": False,
        "nonrecursive_constructor_rule_and_signed_lift_package_proved": False,
        "seed_cycle_cut_source_input_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "tail_harmonic_upper_0850_proved": False,
        "tail_skeleton_lower_401_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TERMINAL_FAMILY,
        "absorbed_to": constructor_terminal_saturated_basis(),
        "next_primary_attack_target": NEW_JOINT,
        "conditional_scope_or_external_target_retained": PDEC_SCOPE,
        "parallel_attack_targets": [
            SEED,
            PDEC_SCOPE,
            HARMONIC,
            SKELETON,
            DSTRUCTURE,
            RATE,
            JOINT_ROWS,
            JOINT_IDENTITY,
            JOINT_RETURN,
            SOURCE_EXACTUV,
            SIGNED_SURVIVAL,
            ROW_MASS,
            COMPLETE_KEY,
            FIXED_KEY,
        ],
        "latest_retained_basis_after_router": retained_parallel_basis(),
        "structural_chain": [
            TERMINAL_FAMILY,
            f"{NONRECURSIVE_BREAKER} OR {PDEC_SCOPE} OR {NEW_JOINT}",
            f"{SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT}",
            pdec_or_new_joint_basis(),
            constructor_terminal_saturated_basis(),
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步直接攻击 constructor KZ 回流后留下的 acyclic noncanonical terminal family。"
            "strict 终端家族最新饱和证书显示三手臂已经展开：canonical-lock 只给 scoped canonical，"
            "direct PDEC 卡在同集作用域匹配，CleanKLS/DLS 回到终端循环。继续沿 nonrecursive "
            "breaker 与 seed-cycle-cut 展开，会回到 signed-source 固定点；global CRT 同步也给出同一前沿。"
            "因此 constructor 语境下 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily` "
            "不再作为粗黑箱保留，而是压到 PDEC same-set scope 或新的显式 joint alpha/delta 公式。"
            "这不是无条件闭合；source seed、PDEC scope、新 joint、harmonic、skeleton、Rate、DStructure "
            "与 constructor 兄弟字段仍开放。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor terminal-family saturation sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"constructor_terminal_family_target_imported={fmt_bool(result['constructor_terminal_family_target_imported'])}",
        f"strict_terminal_family_latest_saturation_imported={fmt_bool(result['strict_terminal_family_latest_saturation_imported'])}",
        f"nonrecursive_breaker_cycle_imported={fmt_bool(result['nonrecursive_breaker_cycle_imported'])}",
        f"seed_cycle_cut_saturation_imported={fmt_bool(result['seed_cycle_cut_saturation_imported'])}",
        f"pdec_scope_branch_internal_saturation_imported={fmt_bool(result['pdec_scope_branch_internal_saturation_imported'])}",
        f"global_crt_saturation_agrees={fmt_bool(result['global_crt_saturation_agrees'])}",
        f"constructor_terminal_family_unnamed_exit_removed={fmt_bool(result['constructor_terminal_family_unnamed_exit_removed'])}",
        f"strict_acyclic_terminal_family_proved={fmt_bool(result['strict_acyclic_terminal_family_proved'])}",
        f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        f"conditional_scope_or_external_target_retained={result['conditional_scope_or_external_target_retained']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
    ]
    lines.extend(result["structural_chain"])
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
