#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor moving-block terminal 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_moving_block_terminal_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

FRESH_JOINT_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-sync-router.json"
)
STRICT_MOVING_BLOCK_CERT = DOCS / "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json"
GLOBAL_SPLIT_CERT = DOCS / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json"
PRECAUCHY_ALPHA_TERMINAL_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.json"
)

FRESH_JOINT_DECL = "FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop"
MOVING_BLOCK = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
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
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"


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
        FRESH_JOINT_CERT,
        STRICT_MOVING_BLOCK_CERT,
        GLOBAL_SPLIT_CERT,
        PRECAUCHY_ALPHA_TERMINAL_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def constructor_terminal_basis_after_router() -> str:
    """给出替换 moving-block 后的 constructor 保留基。"""
    terminal_pair = f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}"
    return (
        f"(({ALPHA_ROW} AND {terminal_pair} AND {SAME_UNIT_MULT} AND {ROW_MASS} "
        f"AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}) "
        f"OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} "
        f"OR {POINTWISE_TABLE} OR {EXTERNAL_DIBFI}) AND {SIGNED_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR} "
        f"AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(
    fresh: dict[str, Any],
    moving: dict[str, Any],
    global_split: dict[str, Any],
    alpha_terminal: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 constructor moving-block terminal 同步判定表。"""
    fresh_input_active = (
        fresh.get("target_input_before_router") == FRESH_JOINT_DECL
        and fresh.get("next_primary_attack_target") == MOVING_BLOCK
        and fresh.get("fresh_joint_declaration_reduced_to_moving_block") is True
    )
    strict_router_closed = (
        moving.get("terminal_gap_before_router") == MOVING_BLOCK
        and moving.get("terminal_gap_after_router") == f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}"
        and moving.get("strict_actual_moving_block_router_closed") is True
    )
    global_terminal_imported = (
        global_split.get("terminal_gap_after_router") == PDEC_CLEAN_KLS
        and global_split.get("global_pdec_sparse_terminal_split_reconciled") is True
    )
    current_frontier_zero = global_split.get("current_materialized_frontier_exhausted") is True
    alpha_branch_agrees = (
        alpha_terminal.get("moving_block_to_global_terminal_modelgap_imported") is True
        and alpha_terminal.get("next_primary_attack_target") == PDEC_CLEAN_KLS
    )
    constructor_moving_block_exit_removed = (
        fresh_input_active and strict_router_closed and global_terminal_imported
    )

    return [
        row(
            "LatestConstructorFreshJointMovingBlockInputImported",
            fresh_input_active,
            False,
            "上一层已把 constructor fresh joint declaration 压到 actual moving-block/NC-BLK。",
            MOVING_BLOCK,
        ),
        row(
            "StrictActualMovingBlockRouterImported",
            strict_router_closed,
            True,
            "strict moving-block 路由已说明该输入不能作为无名终端停留。",
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            moving.get("counterexample_assumption_only") is True,
            True,
            "本层只在反例链内部同步，不用真实零行缺席或有限数值现象作全局证明。",
            "所有输出仍必须是命名终端、模型账本或并行开放字段。",
        ),
        row(
            "GlobalPDECSparseSplitImported",
            global_terminal_imported,
            True,
            "moving-block 的 global PDEC/sparse terminal 已经由全局拆分回到 PDEC/CleanKLS 容量门。",
            PDEC_CLEAN_KLS,
        ),
        row(
            "CurrentMaterializedTerminalFrontierExhausted",
            current_frontier_zero,
            True,
            "当前已物化 PDEC/sparse 前沿清零；这只是当前材料边界，不是未来 family 的不存在性证明。",
            PDEC_CLEAN_KLS,
        ),
        row(
            "PreCauchyAlphaTerminalSyncAgrees",
            alpha_branch_agrees,
            True,
            "latest pre-Cauchy alpha productive 分支也把 moving-block 回接到同一 PDEC/CleanKLS 与模型账本。",
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ),
        row(
            "ConstructorMovingBlockUnnamedExitRemoved",
            constructor_moving_block_exit_removed,
            True,
            "constructor fresh-joint 路线不能把 moving-block/NC-BLK 作为新的独立黑箱。",
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ),
        row(
            "ModelGapLedgerRetained",
            True,
            False,
            "moving-block 专属 DPRC 兼容门可删除，但显式模型余量与有限 DPRC 账本仍需证明。",
            MODEL_GAP,
        ),
        row(
            "ConstructorJointRowsIdentityReturnStillParallel",
            True,
            False,
            "本层只替换 moving-block 原子；joint rows、word/coefficient identity 与 no-downstream return ledger 仍未证明。",
            f"{JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}",
        ),
        row(
            "SourceExactUVAndSignedMassStillParallel",
            True,
            False,
            "source entropy/ExactUV、signed survival、row-mass、complete/fixed key 仍不是 moving-block 路由的结论。",
            f"{EXACTUV_PAIR} AND {SIGNED_SURVIVAL} AND {ROW_MASS} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "RateDStructureStillParallel",
            True,
            False,
            "Rate preservation 与 DStructure/Tail-log4/finite Rankin 独立验收门继续保留。",
            f"{RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层没有证明 PDEC/CleanKLS、模型余量或行/列命题，只完成 constructor moving-block 终端同步。",
            constructor_terminal_basis_after_router(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    fresh = load_json(FRESH_JOINT_CERT)
    moving = load_json(STRICT_MOVING_BLOCK_CERT)
    global_split = load_json(GLOBAL_SPLIT_CERT)
    alpha_terminal = load_json(PRECAUCHY_ALPHA_TERMINAL_CERT)
    rows = build_rows(fresh, moving, global_split, alpha_terminal)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_moving_block_terminal_sync_router",
        "status": "phi_lpf_latest_constructor_moving_block_synced_to_global_terminal_modelgap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "constructor_moving_block_terminal_sync_closed": rows[6]["closed"],
        "fresh_joint_moving_block_input_imported": rows[0]["closed"],
        "strict_actual_moving_block_router_imported": rows[1]["closed"],
        "counterexample_branch_guard_preserved": rows[2]["closed"],
        "global_pdec_sparse_split_imported": rows[3]["closed"],
        "current_materialized_terminal_frontier_exhausted": rows[4]["closed"],
        "precauchy_alpha_terminal_sync_agrees": rows[5]["closed"],
        "constructor_moving_block_unnamed_exit_removed": rows[6]["closed"],
        "actual_noncanonical_moving_block_spread_ncb_lk_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "joint_emitter_rows_formula_proved": False,
        "joint_word_coefficient_identity_proved": False,
        "joint_emitter_no_downstream_named_return_ledger_proved": False,
        "actual_source_domain_entropy_and_exactuv_pair_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": MOVING_BLOCK,
        "absorbed_to": f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        "next_primary_attack_target": PDEC_CLEAN_KLS,
        "next_direct_attack_target": f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        "parallel_attack_targets": [
            MODEL_GAP,
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
        "latest_retained_basis_after_router": constructor_terminal_basis_after_router(),
        "structural_chain": [
            FRESH_JOINT_DECL,
            MOVING_BLOCK,
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor fresh-joint taxonomy 留下的 "
            "`ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn` "
            "接入已有 strict moving-block 终端路由。该输入在反例链中不能作为新的无名黑箱："
            "有登记低维签名时进入 PDEC/SAE/ColumnCRT/sparse 终端，无登记签名时进入早期零行"
            "终端包；全局拆分再把该包压到 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`。"
            "`ExplicitModelGapAndFiniteDPRCLedger` 仍独立保留。因此 constructor 路线的最新"
            "直接硬点同步为 PDEC/CleanKLS 容量门与模型余量账本；joint rows、identity、"
            "return、ExactUV、signed survival、row-mass、complete/fixed key、Rate 与 DStructure "
            "仍未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor moving-block terminal sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fresh_joint_moving_block_input_imported={fmt_bool(result['fresh_joint_moving_block_input_imported'])}",
        f"strict_actual_moving_block_router_imported={fmt_bool(result['strict_actual_moving_block_router_imported'])}",
        f"global_pdec_sparse_split_imported={fmt_bool(result['global_pdec_sparse_split_imported'])}",
        f"precauchy_alpha_terminal_sync_agrees={fmt_bool(result['precauchy_alpha_terminal_sync_agrees'])}",
        f"constructor_moving_block_unnamed_exit_removed={fmt_bool(result['constructor_moving_block_unnamed_exit_removed'])}",
        f"actual_noncanonical_moving_block_spread_ncb_lk_proved={fmt_bool(result['actual_noncanonical_moving_block_spread_ncb_lk_proved'])}",
        f"pdec_cap_or_internal_clean_kls_large_sieve_proved={fmt_bool(result['pdec_cap_or_internal_clean_kls_large_sieve_proved'])}",
        f"explicit_model_gap_and_finite_dprc_ledger_proved={fmt_bool(result['explicit_model_gap_and_finite_dprc_ledger_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
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
