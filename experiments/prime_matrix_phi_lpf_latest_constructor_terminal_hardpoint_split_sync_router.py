#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor terminal hardpoint split 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_terminal_hardpoint_split_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-split-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-split-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-split-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-split-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-split-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CONSTRUCTOR_TERMINAL_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync-router.json"
)
PDEC_CLEAN_KLS_CERT = DOCS / "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"
MODEL_GAP_CERT = DOCS / "prime-matrix-explicit-model-gap-finite-ledger-router.json"
HIGH_MODEL_CERT = DOCS / "prime-matrix-high-segment-model-gap-factorization-router.json"

PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
SCOPE_MATCH = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
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
    """读取 JSON 证书；缺失时返回空字典，避免把缺失误当作证明。"""
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
        CONSTRUCTOR_TERMINAL_CERT,
        PDEC_CLEAN_KLS_CERT,
        MODEL_GAP_CERT,
        HIGH_MODEL_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def split_target() -> str:
    """给出本层拆分后的显式硬点。"""
    return (
        f"(({SCOPE_MATCH} OR {KUZNETSOV_DLS}) "
        f"AND ({HARMONIC} AND {SKELETON}) "
        f"AND {DSTRUCTURE})"
    )


def retained_parallel_basis() -> str:
    """给出 constructor 语境下仍并行保留的硬点。"""
    return (
        f"{split_target()} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN} "
        f"AND {SOURCE_EXACTUV} AND {SIGNED_SURVIVAL} AND {ROW_MASS} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {RATE}"
    )


def build_rows(
    constructor_terminal: dict[str, Any],
    pdec_clean: dict[str, Any],
    model_gap: dict[str, Any],
    high_model: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 constructor terminal hardpoint split 同步判定表。"""
    constructor_terminal_active = (
        constructor_terminal.get("constructor_moving_block_unnamed_exit_removed") is True
        and constructor_terminal.get("next_direct_attack_target")
        == f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}"
    )
    pdec_clean_split = (
        pdec_clean.get("terminal_split_router_closed") is True
        and pdec_clean.get("hardpoint_before_router") == PDEC_CLEAN_KLS
        and SCOPE_MATCH in pdec_clean.get("hardpoint_after_router", "")
        and KUZNETSOV_DLS in pdec_clean.get("hardpoint_after_router", "")
    )
    pdec_arm_open = pdec_clean.get("acyclic_same_set_scope_match_proved") is False
    kls_arm_open = pdec_clean.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is False
    model_split = (
        model_gap.get("explicit_model_gap_and_finite_dprc_ledger_split_closed") is True
        and model_gap.get("finite_dprc_alpha043_p_below_2003_certificate_closed") is True
        and model_gap.get("next_priority") == HIGH_MODEL
    )
    high_model_factorized = (
        high_model.get("high_segment_model_gap_factorized") is True
        and high_model.get("bridge_finite_model_gap_certificate_closed") is True
        and high_model.get("next_priority") == HARMONIC
        and high_model.get("secondary_priority") == SKELETON
    )
    harmonic_open = high_model.get("tail_harmonic_upper_0850_proved") is False
    skeleton_open = high_model.get("tail_skeleton_lower_401_proved") is False
    terminal_hardpoint_split_closed = (
        constructor_terminal_active
        and pdec_clean_split
        and model_split
        and high_model_factorized
    )

    return [
        row(
            "ConstructorTerminalGateImported",
            constructor_terminal_active,
            False,
            "上一层把 constructor moving-block/NC-BLK 同步到 PDEC/CleanKLS 与模型余量账本。",
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ),
        row(
            "PDECCleanKLSSplitImported",
            pdec_clean_split,
            True,
            "strict 终端硬点已经拆成同集 PDEC scope 手臂与自足 Kuznetsov/DLS 手臂。",
            f"{SCOPE_MATCH} OR {KUZNETSOV_DLS}",
        ),
        row(
            "PDECScopeArmStillOpen",
            pdec_arm_open,
            False,
            "同集 PDEC 手臂还缺 strict acyclic 证书与 canonical same-set 证书的同口径作用域匹配。",
            SCOPE_MATCH,
        ),
        row(
            "KuznetsovDLSArmStillOpen",
            kls_arm_open,
            False,
            "CleanKLS 手臂已压到自足 Kuznetsov/DLS 大筛原子，但该原子当前未证。",
            KUZNETSOV_DLS,
        ),
        row(
            "ExplicitModelGapFiniteLedgerSplitImported",
            model_split,
            False,
            "ExplicitModelGapAndFiniteDPRCLedger 已分解：P<2003 有限段闭合，高段模型余量仍开放。",
            HIGH_MODEL,
        ),
        row(
            "HighSegmentModelGapFactorizationImported",
            high_model_factorized,
            False,
            "高段模型余量已经因子化为调和窗口上界与动态粗骨架下界两张尾段账本。",
            f"{HARMONIC} AND {SKELETON}",
        ),
        row(
            "HarmonicWindowTailInputStillOpen",
            harmonic_open,
            False,
            "仍需解析证明 sum_{P^0.43<q<P} 1/q <= 0.850，对所有 P>=3001 成立。",
            HARMONIC,
        ),
        row(
            "DynamicRoughSkeletonTailInputStillOpen",
            skeleton_open,
            False,
            "仍需解析证明动态粗骨架双侧均至少 401，对所有 P>=3001 成立。",
            SKELETON,
        ),
        row(
            "TerminalHardpointSplitSyncClosed",
            terminal_hardpoint_split_closed,
            False,
            "constructor 终端混合硬点已同步为 PDEC/KLS 二分与模型余量双账本；没有证明任一开放原子。",
            split_target(),
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
            "本层只是拆分并同步终端硬点，没有产生全局矛盾或无条件闭合。",
            retained_parallel_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    constructor_terminal = load_json(CONSTRUCTOR_TERMINAL_CERT)
    pdec_clean = load_json(PDEC_CLEAN_KLS_CERT)
    model_gap = load_json(MODEL_GAP_CERT)
    high_model = load_json(HIGH_MODEL_CERT)
    rows = build_rows(constructor_terminal, pdec_clean, model_gap, high_model)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_terminal_hardpoint_split_sync_router",
        "status": "phi_lpf_latest_constructor_terminal_hardpoint_split_synced_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "constructor_terminal_gate_imported": rows[0]["closed"],
        "pdec_clean_kls_split_imported": rows[1]["closed"],
        "pdec_scope_arm_still_open": rows[2]["closed"],
        "kuznetsov_dls_arm_still_open": rows[3]["closed"],
        "explicit_model_gap_finite_ledger_split_imported": rows[4]["closed"],
        "high_segment_model_gap_factorization_imported": rows[5]["closed"],
        "harmonic_window_tail_input_still_open": rows[6]["closed"],
        "dynamic_rough_skeleton_tail_input_still_open": rows[7]["closed"],
        "terminal_hardpoint_split_sync_closed": rows[8]["closed"],
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "tail_harmonic_upper_0850_proved": False,
        "tail_skeleton_lower_401_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        "absorbed_to": split_target(),
        "next_primary_attack_target": KUZNETSOV_DLS,
        "parallel_attack_targets": [
            SCOPE_MATCH,
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
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
            f"({SCOPE_MATCH} OR {KUZNETSOV_DLS}) AND {HIGH_MODEL}",
            split_target(),
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor fresh-joint 路线刚到达的 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve "
            "AND ExplicitModelGapAndFiniteDPRCLedger` 同步到更窄的现有终端接口。PDEC/CleanKLS "
            "部分拆成 `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate` 或 "
            "`SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`；模型账本部分"
            "先删除 P<2003 有限段，再把高段模型余量因子化为 "
            "`HarmonicWindowAlpha043PGe3001Upper0850Ledger` 与 "
            "`DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger`。这些都是开放原子，"
            "不是证明。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor terminal hardpoint split sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"constructor_terminal_gate_imported={fmt_bool(result['constructor_terminal_gate_imported'])}",
        f"pdec_clean_kls_split_imported={fmt_bool(result['pdec_clean_kls_split_imported'])}",
        f"explicit_model_gap_finite_ledger_split_imported={fmt_bool(result['explicit_model_gap_finite_ledger_split_imported'])}",
        f"high_segment_model_gap_factorization_imported={fmt_bool(result['high_segment_model_gap_factorization_imported'])}",
        f"terminal_hardpoint_split_sync_closed={fmt_bool(result['terminal_hardpoint_split_sync_closed'])}",
        f"self_contained_kuznetsov_dls_large_sieve_inequality_proved={fmt_bool(result['self_contained_kuznetsov_dls_large_sieve_inequality_proved'])}",
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
