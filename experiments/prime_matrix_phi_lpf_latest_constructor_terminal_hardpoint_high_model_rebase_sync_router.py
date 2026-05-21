#!/usr/bin/env python3
"""生成 latest constructor terminal hardpoint/high-model 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_terminal_hardpoint_high_model_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_TERMINAL_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-rebase-sync-router.json"
)
STRICT_TERMINAL_HARDPOINT_CERT = DOCS / "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"
STRICT_GLOBAL_SCOPE_CERT = DOCS / "prime-matrix-strict-global-terminal-scope-router.json"
MOVING_BLOCK_DPRC_COMPAT_CERT = DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json"

PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
FINITE_DPRC = "FiniteDPRCAlpha043PBelow2003Certificate"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
SCOPE_MATCH = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
SAME_UNIT_MULT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失依赖不能当成证明。"""
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


def contains(value: Any, needle: str) -> bool:
    """检查证书文本字段是否携带目标原子名。"""
    return needle in str(value)


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
        CURRENT_TERMINAL_REBASE_CERT,
        STRICT_TERMINAL_HARDPOINT_CERT,
        STRICT_GLOBAL_SCOPE_CERT,
        MOVING_BLOCK_DPRC_COMPAT_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def refined_terminal_pair() -> str:
    """给出宽终端门与模型账本拆分后的实际开放对。"""
    return f"({SCOPE_MATCH} OR {KUZNETSOV_DLS}) AND {HIGH_MODEL}"


def retained_basis() -> str:
    """给出替换宽终端门后的 constructor 保留基。"""
    terminal_pair = refined_terminal_pair()
    return (
        f"(({ALPHA_ROW} AND {terminal_pair} AND {SAME_UNIT_MULT} AND {ROW_MASS} "
        f"AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}) "
        f"OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {SCOPE_MATCH} "
        f"OR {POINTWISE_TABLE} OR {EXTERNAL_DIBFI}) AND {SIGNED_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR} "
        f"AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(
    current: dict[str, Any],
    terminal: dict[str, Any],
    scope: dict[str, Any],
    dprc: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 terminal hardpoint/high-model rebase 判定表。"""
    current_pair_active = (
        current.get("next_direct_attack_target") == f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}"
        and current.get("constructor_moving_block_unnamed_exit_removed") is True
    )
    terminal_split_imported = (
        terminal.get("terminal_split_router_closed") is True
        and terminal.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )
    pdec_scope_open = terminal.get("acyclic_same_set_scope_match_proved") is False
    kuznetsov_open = terminal.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is False
    high_model_split_imported = (
        scope.get("finite_dprc_segment_closed") is True
        and scope.get("high_segment_model_gap_alpha043_c3_analytic_ledger_proved") is False
        and contains(scope.get("terminal_gap_after_router"), HIGH_MODEL)
    )
    dprc_compat_closed = dprc.get("exact_model_gap_dprc_compatibility_proved") is True
    wide_pair_removed = (
        current_pair_active and terminal_split_imported and high_model_split_imported and dprc_compat_closed
    )
    return [
        row(
            "LatestConstructorTerminalPairImported",
            current_pair_active,
            False,
            "上一层已把 constructor moving-block/NC-BLK 无名出口压到 PDEC/CleanKLS 与模型账本对。",
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ),
        row(
            "StrictPDECCleanKLSTerminalSplitImported",
            terminal_split_imported,
            True,
            "strict 终端硬点证书把宽门精确拆成直接 PDEC 作用域匹配或自足 Kuznetsov/DLS 大筛。",
            f"{SCOPE_MATCH} OR {KUZNETSOV_DLS}",
        ),
        row(
            "DirectPDECScopeMatchStillOpen",
            not pdec_scope_open,
            not pdec_scope_open,
            "PDEC 手臂需要同 formal unit、同坏窗集合、同容量口径和同质量推前。",
            SCOPE_MATCH,
        ),
        row(
            "SelfContainedKuznetsovDLSAtomStillOpen",
            not kuznetsov_open,
            not kuznetsov_open,
            "CleanKLS 手臂已到窗口 DLS normal form；真正解析原子仍是自足 Kuznetsov/DLS 大筛不等式。",
            KUZNETSOV_DLS,
        ),
        row(
            "ExplicitModelGapFiniteHighSplitImported",
            high_model_split_imported,
            True,
            "ExplicitModelGapAndFiniteDPRCLedger 已拆成 P<2003 有限段闭合和 P>=2003 高段模型余量开放。",
            HIGH_MODEL,
        ),
        row(
            "FiniteDPRCSegmentClosedButNotHighModel",
            scope.get("finite_dprc_segment_closed") is True,
            True,
            "有限 DPRC 段可导入为已闭合账本，但不能替代高段解析模型余量。",
            FINITE_DPRC,
        ),
        row(
            "MovingBlockDPRCCompatibilityClosed",
            dprc_compat_closed,
            True,
            "moving-block 替换没有产生额外 DPRC 账本对象；只保留模型账本自身。",
            MODEL_GAP,
        ),
        row(
            "WideTerminalModelPairRemoved",
            wide_pair_removed,
            False,
            "宽口径 PDEC/CleanKLS + ExplicitModelGap 对已被替换为两个终端手臂加高段模型余量。",
            refined_terminal_pair(),
        ),
        row(
            "ExternalDIBFIStillConditionalOnly",
            False,
            False,
            "外部 DI/BFI/Kuznetsov 只能作为条件线，不能替代 strict 自足闭合。",
            EXTERNAL_DIBFI,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只做前沿精炼；未证明终端矛盾，也未证明三命题无条件闭合。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    current = load_json(CURRENT_TERMINAL_REBASE_CERT)
    terminal = load_json(STRICT_TERMINAL_HARDPOINT_CERT)
    scope = load_json(STRICT_GLOBAL_SCOPE_CERT)
    dprc = load_json(MOVING_BLOCK_DPRC_COMPAT_CERT)
    rows = build_rows(current, terminal, scope, dprc)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_terminal_hardpoint_high_model_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_terminal_hardpoint_high_model_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_constructor_terminal_pair_imported": rows[0]["closed"],
        "strict_pdec_clean_kls_terminal_split_imported": rows[1]["closed"],
        "direct_pdec_scope_match_proved": False,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "explicit_model_gap_finite_high_split_imported": rows[4]["closed"],
        "finite_dprc_segment_closed": rows[5]["closed"],
        "moving_block_dprc_compatibility_closed": rows[6]["closed"],
        "wide_terminal_model_pair_removed": rows[7]["closed"],
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        "absorbed_to": refined_terminal_pair(),
        "next_primary_attack_target": KUZNETSOV_DLS,
        "next_direct_attack_target": f"{KUZNETSOV_DLS} AND {HIGH_MODEL}",
        "parallel_attack_targets": [
            SCOPE_MATCH,
            HIGH_MODEL,
            JOINT_ROWS,
            JOINT_IDENTITY,
            JOINT_RETURN,
            EXACTUV_PAIR,
            SIGNED_SURVIVAL,
            ROW_MASS,
            COMPLETE_KEY,
            FIXED_KEY,
            RATE,
            DSTRUCTURE,
        ],
        "latest_retained_basis_after_router": retained_basis(),
        "structural_chain": [
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
            f"({SCOPE_MATCH} OR {KUZNETSOV_DLS}) AND ({FINITE_DPRC} closed + {HIGH_MODEL})",
            refined_terminal_pair(),
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor 的宽终端对 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND "
            "ExplicitModelGapAndFiniteDPRCLedger` 接入 strict 终端硬点二分和 strict model-gap "
            "高段拆分。宽门不再作为无名硬点保留；剩余是 PDEC 作用域匹配或自足 Kuznetsov/DLS "
            "大筛原子，并且仍需高段模型余量。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor terminal hardpoint/high-model rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_terminal_pair_imported={fmt_bool(result['latest_constructor_terminal_pair_imported'])}",
        f"strict_pdec_clean_kls_terminal_split_imported={fmt_bool(result['strict_pdec_clean_kls_terminal_split_imported'])}",
        f"explicit_model_gap_finite_high_split_imported={fmt_bool(result['explicit_model_gap_finite_high_split_imported'])}",
        f"finite_dprc_segment_closed={fmt_bool(result['finite_dprc_segment_closed'])}",
        f"moving_block_dprc_compatibility_closed={fmt_bool(result['moving_block_dprc_compatibility_closed'])}",
        f"wide_terminal_model_pair_removed={fmt_bool(result['wide_terminal_model_pair_removed'])}",
        f"direct_pdec_scope_match_proved={fmt_bool(result['direct_pdec_scope_match_proved'])}",
        f"self_contained_kuznetsov_dls_large_sieve_inequality_proved={fmt_bool(result['self_contained_kuznetsov_dls_large_sieve_inequality_proved'])}",
        f"high_segment_model_gap_alpha043_c3_analytic_ledger_proved={fmt_bool(result['high_segment_model_gap_alpha043_c3_analytic_ledger_proved'])}",
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
            "## 3. 最新保留基",
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
