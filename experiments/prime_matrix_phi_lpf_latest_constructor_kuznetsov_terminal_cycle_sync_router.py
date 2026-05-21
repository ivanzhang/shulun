#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor Kuznetsov terminal-cycle 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_kuznetsov_terminal_cycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CONSTRUCTOR_SPLIT_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-split-sync-router.json"
)
KUZNETSOV_SYNC_CERT = DOCS / "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json"
TERMINAL_SATURATION_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-router.json"
)

KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
NONRECURSIVE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
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
    return [CONSTRUCTOR_SPLIT_CERT, KUZNETSOV_SYNC_CERT, TERMINAL_SATURATION_CERT]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def terminal_tail_model_basis() -> str:
    """把模型账本替换成高段尾账本后的 KZ 回流基。"""
    return (
        f"{SEED} AND {TERMINAL_FAMILY} AND ({HARMONIC} AND {SKELETON}) "
        f"AND {DSTRUCTURE}"
    )


def retained_parallel_basis() -> str:
    """给出 constructor 语境下仍并行保留的硬点。"""
    return (
        f"({PDEC_SCOPE} OR {terminal_tail_model_basis()} OR {NONRECURSIVE_BREAKER} "
        f"OR {NEW_JOINT}) AND {HARMONIC} AND {SKELETON} AND {DSTRUCTURE} "
        f"AND {RATE} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN} "
        f"AND {SOURCE_EXACTUV} AND {SIGNED_SURVIVAL} AND {ROW_MASS} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY}"
    )


def build_rows(
    constructor_split: dict[str, Any],
    kuz: dict[str, Any],
    terminal_saturation: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 constructor KZ terminal-cycle 同步判定表。"""
    kz_arm_active = (
        constructor_split.get("next_primary_attack_target") == KUZNETSOV_DLS
        and constructor_split.get("terminal_hardpoint_split_sync_closed") is True
    )
    kz_sync_imported = (
        kuz.get("terminal_gap_before_router") == KUZNETSOV_DLS
        and kuz.get("kz_abcd_internal_spine_closed") is True
        and kuz.get("kuznetsov_route_returns_to_terminal_family") is True
    )
    kz_not_proved = kuz.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is False
    ncblk_return = (
        kuz.get("kz_e_reduced_to_acyclic_ncblk") is True
        and kuz.get("acyclic_ncblk_not_independent_terminal") is True
    )
    model_factorized = (
        constructor_split.get("high_segment_model_gap_factorization_imported") is True
        and constructor_split.get("tail_harmonic_upper_0850_proved") is False
        and constructor_split.get("tail_skeleton_lower_401_proved") is False
    )
    pdec_scope_still_open = constructor_split.get("acyclic_same_set_scope_match_proved") is False
    terminal_saturation_agrees = (
        terminal_saturation.get("clean_kls_kuznetsov_route_returns_terminal") is True
        and terminal_saturation.get("pdec_scope_branch_saturated_to_new_joint") is True
        and terminal_saturation.get("new_explicit_joint_constructor_formula_artifact_present") is False
    )
    constructor_kz_cycle_removed = (
        kz_arm_active and kz_sync_imported and ncblk_return and model_factorized
    )

    return [
        row(
            "ConstructorKuznetsovArmImported",
            kz_arm_active,
            False,
            "上一层 constructor terminal split 把首攻钉到自足 Kuznetsov/DLS 大筛手臂。",
            KUZNETSOV_DLS,
        ),
        row(
            "StrictKuznetsovTerminalSyncImported",
            kz_sync_imported,
            False,
            "strict KZ/DLS 同步显示 KZ-A/B/C/D 已到位，但 KZ-E 回到 NC-BLK/source anti-atom 和终端家族。",
            f"{SEED} AND {TERMINAL_FAMILY} AND {MODEL_GAP}",
        ),
        row(
            "KuznetsovDLSTheoremStillUnproved",
            kz_not_proved,
            False,
            "本层没有证明自足 Kuznetsov/DLS log-saving 不等式，只删除其无名终端解释。",
            KUZNETSOV_DLS,
        ),
        row(
            "NCBLKReturnToTerminalFamilyImported",
            ncblk_return,
            True,
            "KZ-E 失败转成 acyclic NC-BLK/source anti-atom；该对象不能独立停留，又回到 moving atom/global terminal。",
            TERMINAL_FAMILY,
        ),
        row(
            "ModelGapTailFactorizationCarried",
            model_factorized,
            False,
            "KZ 回流中的模型账本继续沿上一层拆成 harmonic-window 与 rough-skeleton 尾账本。",
            f"{HARMONIC} AND {SKELETON}",
        ),
        row(
            "PDECScopeArmStillParallel",
            pdec_scope_still_open,
            False,
            "PDEC scope 手臂没有被 KZ 回流证明或排除，仍作为并行开放输入保留。",
            PDEC_SCOPE,
        ),
        row(
            "TerminalSaturationAgreesWithNewJointBreaker",
            terminal_saturation_agrees,
            False,
            "既有 Phi-LPF terminal saturation 同步也确认：KZ 线回终端，PDEC scope 线在内部语料中压到 new-joint。",
            f"{NONRECURSIVE_BREAKER} OR {NEW_JOINT}",
        ),
        row(
            "ConstructorKuznetsovIndependentExitRemoved",
            constructor_kz_cycle_removed,
            False,
            "constructor 语境下，KZ/DLS 不能作为新的独立主攻出口；继续推进必须攻击终端家族/破环包/模型尾账本。",
            f"{terminal_tail_model_basis()} OR {NONRECURSIVE_BREAKER} OR {NEW_JOINT}",
        ),
        row(
            "TailInputsStillOpen",
            True,
            False,
            "调和窗口上界与动态粗骨架下界仍未解析证明。",
            f"{HARMONIC} AND {SKELETON}",
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
            "本层只识别 KZ 回流循环，没有排除终端家族、破环包或模型尾账本。",
            retained_parallel_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    constructor_split = load_json(CONSTRUCTOR_SPLIT_CERT)
    kuz = load_json(KUZNETSOV_SYNC_CERT)
    terminal_saturation = load_json(TERMINAL_SATURATION_CERT)
    rows = build_rows(constructor_split, kuz, terminal_saturation)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_kuznetsov_terminal_cycle_sync_router",
        "status": "phi_lpf_latest_constructor_kuznetsov_arm_synced_to_terminal_cycle_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "constructor_kuznetsov_arm_imported": rows[0]["closed"],
        "strict_kuznetsov_terminal_sync_imported": rows[1]["closed"],
        "kuznetsov_dls_theorem_still_unproved": rows[2]["closed"],
        "ncblk_return_to_terminal_family_imported": rows[3]["closed"],
        "model_gap_tail_factorization_carried": rows[4]["closed"],
        "pdec_scope_arm_still_parallel": rows[5]["closed"],
        "terminal_saturation_agrees_with_new_joint_breaker": rows[6]["closed"],
        "constructor_kuznetsov_independent_exit_removed": rows[7]["closed"],
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "nonrecursive_constructor_rule_and_signed_lift_package_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "acyclic_same_set_scope_match_proved": False,
        "tail_harmonic_upper_0850_proved": False,
        "tail_skeleton_lower_401_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": KUZNETSOV_DLS,
        "absorbed_to": terminal_tail_model_basis(),
        "next_primary_attack_target": TERMINAL_FAMILY,
        "parallel_attack_targets": [
            SEED,
            NONRECURSIVE_BREAKER,
            NEW_JOINT,
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
            KUZNETSOV_DLS,
            "KZ-A/B/C/D spine + KZ-E",
            "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom",
            terminal_tail_model_basis(),
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步直接攻击 constructor terminal split 后的 KZ/DLS 手臂。strict KZ/DLS 证书已经显示："
            "KZ-A/B/C/D 形式谱脊柱可同步，但 KZ-E 转成 acyclic NC-BLK/source anti-atom，"
            "该对象又回到 strict acyclic terminal family 与模型账本。因此在 constructor 语境下，"
            "`SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks` 不能作为新的独立"
            "无名终端；最新显式剩余回到 terminal family、nonrecursive breaker/new-joint、PDEC scope "
            "以及 harmonic-window/rough-skeleton 模型尾账本。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor Kuznetsov terminal-cycle sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"constructor_kuznetsov_arm_imported={fmt_bool(result['constructor_kuznetsov_arm_imported'])}",
        f"strict_kuznetsov_terminal_sync_imported={fmt_bool(result['strict_kuznetsov_terminal_sync_imported'])}",
        f"ncblk_return_to_terminal_family_imported={fmt_bool(result['ncblk_return_to_terminal_family_imported'])}",
        f"model_gap_tail_factorization_carried={fmt_bool(result['model_gap_tail_factorization_carried'])}",
        f"constructor_kuznetsov_independent_exit_removed={fmt_bool(result['constructor_kuznetsov_independent_exit_removed'])}",
        f"self_contained_kuznetsov_dls_large_sieve_inequality_proved={fmt_bool(result['self_contained_kuznetsov_dls_large_sieve_inequality_proved'])}",
        f"strict_acyclic_terminal_family_proved={fmt_bool(result['strict_acyclic_terminal_family_proved'])}",
        f"tail_harmonic_upper_0850_proved={fmt_bool(result['tail_harmonic_upper_0850_proved'])}",
        f"tail_skeleton_lower_401_proved={fmt_bool(result['tail_skeleton_lower_401_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
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
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
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
